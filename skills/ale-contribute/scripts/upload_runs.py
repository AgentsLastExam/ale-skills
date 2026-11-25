#!/usr/bin/env python3
"""Upload one `orbit run` run directory to its domain's run-record dataset, filed by Task version.

usage:
  upload_runs.py RUN_DIR --repo-dir /path/to/ale-tasks-<domain> --runs-dataset <org>/ale-tasks-<domain>-runs
                 [--hf-token-env-file /path/to/ale/.env] [--dry-run]

For every episode directory in RUN_DIR (a folder holding result.json and lock.json) it reads the
RunLock and refuses the whole upload unless the episode is reportable as a record of a known Task
version:
  - the Task came from a git repository at a resolved commit, with no uncommitted changes;
  - the Task's assets were clean at a synchronized asset commit (or the Task has no assets);
  - the engine commit is known.
It then derives the Task version from what the lock names (the Task folder's git tree at the
recorded commit, and the Task's material tree on the asset dataset at the recorded asset commit),
writes version.json, and uploads each episode exactly as orbit run wrote it to
  tasks/<path>/<version>/<run id>/<episode id>/
The run-record dataset's root ale-runs.json names the repository, the asset dataset and the
dataset id used in version hashes. Nothing is uploaded with --dry-run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath

HF = "https://huggingface.co"


def canonical(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def hf_json(path: str, token: str | None):
    request = urllib.request.Request(f"{HF}/{path}", headers={"Authorization": f"Bearer {token}"} if token else {})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read())


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout.strip()


def material_tree(dataset: str, revision: str, task_path: str, token: str | None) -> str | None:
    parent = str(PurePosixPath(task_path).parent)
    entries = hf_json(f"api/datasets/{dataset}/tree/{revision}/{urllib.parse.quote(parent)}", token)
    return next((e["oid"] for e in entries if e["type"] == "directory" and e["path"] == task_path), None)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--repo-dir", type=Path, required=True, help="a clone of the Task repository the run used")
    ap.add_argument("--runs-dataset", required=True, help="<org>/ale-tasks-<domain>-runs")
    ap.add_argument("--hf-token-env-file", type=Path, help=".env holding ORBIT_HF_TOKEN (default: $ORBIT_HF_TOKEN)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    token = os.environ.get("ORBIT_HF_TOKEN") or os.environ.get("ALE_HF_TOKEN")
    if a.hf_token_env_file:
        token = next((l.split("=", 1)[1].strip() for l in a.hf_token_env_file.read_text().splitlines()
                      if l.startswith(("ORBIT_HF_TOKEN=", "ALE_HF_TOKEN="))), token)
    config_path = f"datasets/{a.runs_dataset}/resolve/main/ale-runs.json"
    request = urllib.request.Request(f"{HF}/{config_path}", headers={"Authorization": f"Bearer {token}"} if token else {})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            config = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        print(f"cannot read {a.runs_dataset}/ale-runs.json (HTTP {exc.code}): the dataset is gated; request access on "
              f"its page and pass a token with --hf-token-env-file or ORBIT_HF_TOKEN", file=sys.stderr)
        return 1
    repository, asset_dataset, version_dataset = config["repository"], config["asset_dataset"], config["version_dataset_id"]

    run_id = a.run_dir.resolve().name
    episodes = sorted(p for p in a.run_dir.iterdir() if (p / "result.json").is_file() and (p / "lock.json").is_file())
    if not episodes:
        print(f"{a.run_dir}: no episode directories (result.json + lock.json)", file=sys.stderr)
        return 1

    problems, versions = [], {}
    for episode in episodes:
        lock = json.loads((episode / "lock.json").read_text())
        source, asset = lock["task"]["source"], lock.get("asset")
        where = f"{episode.name}"
        if source.get("kind") != "git" or not source.get("commit") or source.get("dirty"):
            problems.append(f"{where}: the Task was not a committed, clean git checkout")
            continue
        if not source["repo"].rstrip("/").removesuffix(".git").endswith(repository.split("/", 1)[1]):
            problems.append(f"{where}: the Task came from {source['repo']}, not {repository}")
            continue
        if asset is not None and (asset.get("dirty") or not asset.get("commit")):
            problems.append(f"{where}: the Task's assets were dirty or unsynchronized")
            continue
        if lock["framework"].get("commit") in (None, "", "unknown"):
            problems.append(f"{where}: the engine commit is unknown")
            continue
        task_path = source["path"].strip("/")
        try:
            code_tree = git(a.repo_dir, "rev-parse", f"{source['commit']}:{task_path}")
        except subprocess.CalledProcessError:
            problems.append(f"{where}: commit {source['commit'][:12]} is not in {a.repo_dir}; git fetch first")
            continue
        assets = None
        if asset is not None:
            tree = material_tree(asset_dataset, asset["commit"], task_path, token)
            if tree is None:
                problems.append(f"{where}: {asset_dataset}@{asset['commit'][:12]} has no {task_path}")
                continue
            assets = {"kind": "hf-dataset", "dataset": version_dataset, "path": task_path, "tree": tree}
        preimage = {"schema": "ale-atlas/task-version@2", "repo": repository, "path": task_path,
                    "code": {"git_object_format": "sha1", "tree": code_tree}, "assets": assets}
        version = "sha256:" + hashlib.sha256(canonical(preimage).encode()).hexdigest()
        record = {"task": task_path, "repository": repository, "commit": source["commit"], "code_tree": code_tree,
                  "dataset": asset_dataset, "dataset_revision": asset["commit"] if asset else None,
                  "material_tree": assets["tree"] if assets else None, "version": version}
        versions.setdefault((task_path, version), {"record": record, "episodes": []})["episodes"].append(episode)

    if problems:
        print("refusing to upload; not reportable as a known Task version:", *problems, sep="\n  ", file=sys.stderr)
        return 1

    plan = []
    for (task_path, version), group in sorted(versions.items()):
        folder = f"{task_path}/{version.replace(':', '-')}"
        plan.append((folder, group))
        print(f"{folder}/{run_id}/  {len(group['episodes'])} episode(s): " + ", ".join(e.name for e in group["episodes"]))
    if a.dry_run:
        for folder, group in plan:
            print(f"version.json for {folder}:\n" + json.dumps(group["record"], indent=1))
        return 0

    from huggingface_hub import CommitOperationAdd, HfApi  # only needed to upload

    api = HfApi(token=token)
    for folder, group in plan:
        operations = [CommitOperationAdd(f"{folder}/version.json", (json.dumps(group["record"], indent=1) + "\n").encode())]
        for episode in group["episodes"]:
            for file in sorted(p for p in episode.rglob("*") if p.is_file()):
                operations.append(CommitOperationAdd(f"{folder}/{run_id}/{episode.name}/{file.relative_to(episode)}", str(file)))
        commit = api.create_commit(a.runs_dataset, operations, repo_type="dataset",
                                   commit_message=f"Add run {run_id} of {group['record']['task']} at {folder.rsplit('/', 1)[1][:19]}")
        print(f"uploaded {len(operations)} files to {a.runs_dataset}/{folder}/{run_id}: {commit.oid[:10]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
