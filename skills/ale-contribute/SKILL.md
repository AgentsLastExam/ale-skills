---
name: ale-contribute
description: How a participant in Agents' Last Exam (ALE) submits a Task to their domain's repository (AgentsLastExam/ale-tasks-<domain>) with its material on Hugging Face, and submits the run records (trajectories) that `ale run` produces to the domain's run-record dataset. Use when asked to add, change or submit an ALE Task, push Task assets, run a Task with an agent, or upload / share ALE run traces.
---

# Contributing Tasks and run records to ALE

Every ALE domain has three places, all named after the domain's Task repository:

| What | Where | Holds |
|---|---|---|
| Task code | GitHub `AgentsLastExam/ale-tasks-<domain>` (private) | `task.toml`, `instruction.md`, Dockerfile, verifier and solution code |
| Task material | Hugging Face `<organization>/ale-tasks-<domain>` (gated) | every input, reference deliverable, rubric and source document, at the same paths |
| Run records | Hugging Face `<organization>/ale-tasks-<domain>-runs` (gated) | the episodes `ale run` produced, filed by Task version |

Your domain repository's README names its organization and both datasets; read it first. The
shared rules are in the [`ale-tasks-base` README](https://github.com/AgentsLastExam/ale-tasks-base#code-in-git-material-on-the-hub),
the Task format in the engine's
[task-authoring.md](https://github.com/AgentsLastExam/ale/blob/main/docs/specs/task-authoring.md) and
what makes a Task acceptable in its
[task-quality-standard.md](https://github.com/AgentsLastExam/ale/blob/main/docs/specs/task-quality-standard.md).

## 0. Set up once

1. Ask your domain's maintainer for access to the GitHub repository, and request access on both
   Hugging Face dataset pages (they are gated; an administrator approves).
2. Clone the engine and the domain repository side by side, then install the engine:
   ```bash
   git clone https://github.com/AgentsLastExam/ale
   git clone https://github.com/AgentsLastExam/ale-tasks-<domain>
   cd ale && uv sync --frozen
   ```
3. In `ale/.env` put a Hugging Face token with read access (write access to push material):
   ```bash
   ALE_HF_TOKEN=hf_...
   ALE_ASSETS_NAMESPACE=<organization>     # from your domain README; omit only for agents-last-exam
   ```
   Keep `.env` out of every commit, message and log. If one engine checkout serves several
   domains, leave `ALE_ASSETS_NAMESPACE` out of `.env` and put it in front of each command instead.
4. Fetch the existing material: `uv run ale assets pull /abs/path/ale-tasks-<domain>`.

## 1. Submit a Task

1. Branch: `git -C ale-tasks-<domain> switch -c task/<name>`.
2. Scaffold: `uv run ale new-task /abs/path/ale-tasks-<domain>/tasks/<name>` (it passes `ale lint`).
3. Write the Task:
   - `instruction.md` names literal paths: inputs under `/home/user/input/`, deliverables under
     `/home/user/output/` (declared in `task.toml` `artifacts`).
   - **All material goes in an `assets/` root**, whatever its size, never in Git:
     inputs in `environment/assets/` (the Dockerfile copies them, e.g. `COPY assets/input/ /home/user/input/`),
     the verifier's rubrics and expected values in `tests/assets/`, the reference deliverables in
     `solution/assets/` (`solve.sh` copies them to the output). Git keeps only code and configuration.
   - `tests/verify.py` scores with `ale_verify` (`write`, `checks`, `judge`); it never trusts the
     agent's own claims and never scores a verifier crash as 0.
   - Nothing the agent must not see goes in `environment/`; `tests/` and `solution/` are hidden
     from the agent.
4. Check:
   ```bash
   cd /abs/path/ale
   uv run ale lint /abs/path/ale-tasks-<domain>/tasks/<name>
   uv run ale validate /abs/path/ale-tasks-<domain>/tasks/<name>   # untouched must score 0, the oracle 1
   ```
   `validate` builds the image and, for Judge-scored Tasks, needs the run's Judge configuration.
5. Push the material, then the code:
   ```bash
   uv run ale assets push /abs/path/ale-tasks-<domain>/tasks/<name>
   uv run ale assets status /abs/path/ale-tasks-<domain>/tasks/<name>   # must say clean
   git -C /abs/path/ale-tasks-<domain> push -u origin task/<name>
   ```
6. Open a pull request with what the Task tests, how it is scored, and the `validate` result.
   One Task per pull request. If the Task is blocked on something outside the repository (missing
   material, a service, a licence), say so in the pull request and set `[metadata] blocked = true`
   and `blocked_reason` in `task.toml`.
7. If the repository has `taxonomy/`, add one `primary` row for your Task to
   `taxonomy/mapping.json` (status `proposed`, with a one-line `basis`) and run
   `python3 taxonomy/check.py`; see the README's "Taxonomy and placements".

## 2. Submit run records (traces)

1. Run from a clean, pushed checkout: the Task's code committed and its assets `clean`, so the
   run can be filed under a Task version.
   ```bash
   cd /abs/path/ale
   uv run ale run /abs/path/ale-tasks-<domain>/tasks/<name> --agent <agent> --model <model> -n <episodes>
   ```
   Each run writes `runs/<run id>/<episode id>/` with `result.json`, `lock.json`,
   `trajectory.json`, `verification.json`, traces and `blobs/`
   ([what each holds](https://github.com/AgentsLastExam/ale/blob/main/docs/specs/trace.md)).
2. Review the run before sharing it: `result.json` status and rewards, and that no credential or
   private note appears in the trajectory (ALE redacts the credentials it knows; check anyway).
3. Upload with this skill's script, dry run first:
   ```bash
   python3 scripts/upload_runs.py /abs/path/ale/runs/<run id> \
     --repo-dir /abs/path/ale-tasks-<domain> \
     --runs-dataset <organization>/ale-tasks-<domain>-runs \
     --hf-token-env-file /abs/path/ale/.env --dry-run
   ```
   It reads every episode's `lock.json`, refuses the whole run if any episode used uncommitted
   Task code, dirty or unsynchronized assets, or an unknown engine commit, derives the Task version
   (the Task folder's git tree plus its material tree on the asset dataset), and shows where each
   episode will go: `tasks/<path>/<version>/<run id>/<episode id>/`, with a `version.json`. Drop
   `--dry-run` to upload; it needs `huggingface_hub` (`uv run --with huggingface_hub python3 …`).
4. Episodes are uploaded exactly as `ale run` wrote them. Results are compared only within one Task
   version; never edit, merge or re-file a run under another version.

## Troubleshooting

| Message | Fix |
|---|---|
| `HTTP 401` / `403` on a dataset | request access on the dataset page; check `ALE_HF_TOKEN` |
| `ale assets push` rejected as `non-fast-forward`, later Tasks skipped | the Task's cached asset branch is stale: remove `.ale-cache/asset-worktrees/tasks/<path>` (`git worktree remove` in `.git/ale-assets/repository`), the branch `manual/tasks/<path>` there and `<path>.publication.json`, push again, then `ale assets status` |
| `asset workspace belongs to a different Task repository` | the dataset moved organization since this checkout last pushed: delete the checkout's `.ale-cache/` and `.git/ale-assets/` once and use the new `ALE_ASSETS_NAMESPACE` |
| `upload_runs.py`: `commit … is not in …` | `git fetch` the Task repository; the run used a commit your clone does not have |
| `upload_runs.py`: assets dirty or unsynchronized | push the Task's assets, rerun, upload the new run |
| `schema_version: Input should be …` from `ale lint` | the engine's Task format changed; update `schema_version` as the engine's task-authoring.md says |
