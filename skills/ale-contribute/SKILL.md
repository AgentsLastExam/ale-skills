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

## 1. Rules every Task submission follows

These are the repository conventions (the README's "Code in Git, material on the Hub", "Versions",
"Taxonomy and placements" and "Merging Tasks") and the engine's Task quality standard, as they
apply to one submission. A pull request that breaks one of them is sent back.

### 1.1 One Task, one pull request

- A pull request adds or changes **exactly one Task** and touches **only `tasks/<path>/`**: no other
  Task, no README, no `taxonomy/`, no CI or repository files. Repository-wide changes are separate
  pull requests by the maintainers.
- Branch `task/<path>`; title `Add <path>: <what the agent must produce>` (a later change:
  `Update <path>: <what changed>`).
- The folder name is the Task's permanent identity: lowercase, words joined the way the
  repository's other Tasks join them, never renamed (a rename is a new Task). `[task].name` is
  `agentslastexam/<folder>`.
- A Task blocked on something outside the repository (missing material, a service, a licence) is
  still one pull request, opened as a draft, with `[metadata] blocked = true` and `blocked_reason`
  in `task.toml`; its description says what would unblock it.
- It merges when the CI check (`ale lint`) passes, `ale validate` passed, the Task's material is
  clean on the dataset, and a reviewer approved it.

### 1.2 Code in Git, all material on the Hub

| Material | Goes in | Reached by |
|---|---|---|
| Inputs the agent works from | `environment/assets/` | the Dockerfile: `COPY assets/input/ /home/user/input/` |
| Rubrics, expected values, reference and source documents of the verifier | `tests/assets/` | `verify.py` reads `assets/…` by relative path |
| Reference deliverables of the oracle | `solution/assets/` | `solve.sh`: `cp -a assets/reference/. /home/user/output/` |

- **Every** document, spreadsheet, image, data file, rubric workbook or expected output goes in an
  `assets/` root, whatever its size. Git holds only `task.toml`, `instruction.md`, the Dockerfile and
  build scripts, `setup/`, `test.sh`, `verify.py` and other verifier code, and `solve.sh`.
- The asset roots are ignored by Git; never force-add them. Push them with
  `ale assets push <the Task's path>` (never the whole repository), and only when the code is ready:
  material pushed for an existing Task changes what `main` runs immediately, so say so in the
  pull request.
- Before asking for review, `ale assets status <the Task's path>` says `clean`.

### 1.3 The Task contract

From the engine's [Task quality standard](https://github.com/AgentsLastExam/ale/blob/main/docs/specs/task-quality-standard.md),
which governs:

- **Instruction**: the required outcome, with literal paths (`/home/user/input/…`,
  `/home/user/output/…`), formats and tolerances wherever correctness depends on them. Every
  deliverable path is declared in `task.toml` `artifacts`.
- **Initial context**: everything a normal solution route needs (software, inputs, services) is in
  the image before the agent starts. The agent has no network by default; an allowlist or open
  network needs a reason in `[metadata]`.
- **Verification**: scores exactly what the instruction asks, no more; gives equal credit to
  equivalent correct answers and none to empty, placeholder or materially wrong ones; uses an LLM
  or Agent Judge (`ale_verify.judge`) where deterministic checks cannot judge the property. A
  verifier crash is a verifier failure, never a score of 0.
- **No shortcuts**: nothing in `environment/` reveals the answer; reference data stays in
  `tests/` and `solution/`, which the agent never sees; self-reported success earns nothing.
- `ale validate`: the untouched Sandbox scores 0 and the oracle scores 1.

### 1.4 Versions

There is no version field to edit. A Task's version is derived from its code (the folder's git tree
on `main`) and its material (the folder's tree on the asset dataset); changing either makes a new
version, and run records are filed under the version they ran. Never change a merged Task's
material or code outside a pull request.

### 1.5 Taxonomy placement

If the repository has `taxonomy/`, every Task gets a place on its tree, but the pull request does
not edit `taxonomy/mapping.json` (concurrent Task pull requests would conflict on it). Instead:

1. Find the node: the deepest node of `taxonomy/tree.json` that the Task's work belongs to, by id:
   ```bash
   python3 -c "import json,sys; t=json.load(open('taxonomy/tree.json'))['root']
   def w(n,p):
       q=p+[n.get('name_en','')]
       if sys.argv[1].lower() in ' '.join(q).lower(): print(n['id'],' > '.join(q[1:]))
       [w(c,q) for c in n.get('children',[])]
   w(t,[])" "<keyword>"
   ```
2. Put the placement in the pull request description (template below): exactly one **primary**
   node, at most two **secondary** nodes, a confidence (`high`/`medium`/`low`), one sentence of
   basis, and `same_as` when a tree leaf is this same case under another id. If no node fits, say
   `node: null` and what the tree is missing: that is a useful finding, not a failure.
3. A maintainer records it in `taxonomy/mapping.json` on `main` as `proposed`; the domain owner
   later marks it `confirmed` or replaces it.

### 1.6 Imported batches

Converting a batch from another source: each Task's `[metadata]` records `source_platform`,
`source_id`, a link to the source item, `source_snapshot` (date) and `conversion_notes`, one line per
change made in conversion. Each Task is still its own pull request (or a maintainer imports the
ready ones together and opens one pull request per blocked Task), and the repository's
`IMPORT.md` lists the batch.

## 2. Submit a Task

1. Branch: `git -C ale-tasks-<domain> switch -c task/<path>`.
2. Scaffold: `uv run ale new-task /abs/path/ale-tasks-<domain>/tasks/<path>` (it passes `ale lint`).
3. Write `instruction.md`, `environment/` (Dockerfile + `environment/assets/`), `tests/`
   (`test.sh`, `verify.py` + `tests/assets/`) and `solution/` (`solve.sh` + `solution/assets/`)
   following section 1.
4. Check:
   ```bash
   cd /abs/path/ale
   uv run ale lint /abs/path/ale-tasks-<domain>/tasks/<path>
   uv run ale validate /abs/path/ale-tasks-<domain>/tasks/<path>   # untouched 0, oracle 1
   ```
   `validate` builds the image and, for Judge-scored Tasks, needs the run's Judge configuration.
5. Push the material, then the code:
   ```bash
   uv run ale assets push /abs/path/ale-tasks-<domain>/tasks/<path>
   uv run ale assets status /abs/path/ale-tasks-<domain>/tasks/<path>   # must say clean
   git -C /abs/path/ale-tasks-<domain> add tasks/<path>
   git -C /abs/path/ale-tasks-<domain> diff --cached --stat               # only tasks/<path>/, no material
   git -C /abs/path/ale-tasks-<domain> commit -m "Add <path>: <outcome>"
   git -C /abs/path/ale-tasks-<domain> push -u origin task/<path>
   ```
6. Open the pull request with this description:

   ```markdown
   ## Task
   <what the agent must produce, from which inputs; who would do this work for real>

   ## Scoring
   <how verify.py scores it: deterministic checks / LLM Judge / Agent Judge; what full credit requires>

   ## Checks
   - ale lint: pass
   - ale validate: untouched <0.0>, oracle <1.0> (engine commit <sha>)
   - assets: pushed, `ale assets status` clean; <n> files in environment/tests/solution assets

   ## Taxonomy placement
   - primary: <node id> (<node name>) — confidence <high|medium|low> — <one-sentence basis>
   - secondary: <node id or none>
   - same_as: <leaf id or none>

   ## Status
   ready | blocked: <what is missing and what would unblock it>
   ```

## 3. Submit run records (traces)

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
