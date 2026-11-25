# Step 4: Preliminary build

Build the task package according to the task plan confirmed by the expert. This step is carried out mainly by the agent alone; consult the expert where the plan leaves something unspecified.

This is a preliminary build whose purpose is to confirm that the plan is workable in practice. It must nevertheless follow the requirements below strictly, since defects in a plan often become visible only once it is actually built.

## Composition of the task package

| File | Content |
|---|---|
| `task.toml` | Task configuration: resources, time limit, GPU, network access |
| `instruction.md` | The task statement. Given to the solving agent as is; the solving agent has access only to this file and the solving environment |
| `environment/` | `Dockerfile` and setup scripts, with software and data placed offline |
| `tests/` | `test.sh` runs the agent judge and writes a score between 0 and 1 to `reward.json`. Numerical-check scripts are kept in `scripts/`, Lean statements and proofs in `lean/`, and the agent judge's materials in `agent-judge/` |
| `calibration/` | Calibration cases. One folder per case containing `solve.sh`, which writes the final state of that case; expected scores are set in `[[calibration]]` in `task.toml`. A reference solution is not required |

## Procedure

1. **Compile the requirement list.** Working from the problem tree, list each leaf's claim and necessary conditions separately. Provide two examples for each: a submission that should be found supported and one that should be found unsupported. The list must cover the whole problem tree; no leaf may be left unchecked.
2. **Write the calibration cases.** Following the task plan, create a folder with a `solve.sh` in `calibration/` for each case: the empty submission (expected score 0); every shortcut found in step 2; partially correct results produced during research; known results, if any. Enter the expected scores in `[[calibration]]` in `task.toml`.
3. **Build the environment.** Place all software and data in the environment in advance; nothing is downloaded during solving. Large files are kept in the controlled dataset designated by the project team, with only a downloaded copy in the environment. Pin software versions.
4. **Write the task statement.** See "Requirements for the task statement" below.
5. **Check that the calibration cases run.** Every `solve.sh` must run in the solving environment without depending on anything outside it.
6. **Implement the scoring.** Implement the scoring specified in the plan; the review is performed by the agent judge, see `references/agent-judge.md`:
    - Numerical-check scripts are kept in `tests/scripts/`. Each check has one script; each script runs on its own, takes the solving agent's submission as input, and outputs the verdict for that item with evidence. Scripts are written against the unified output format. File names are free.
    - When Lean is used, statements and proofs are kept in `tests/lean/`, with the Lean and Mathlib versions stated. Lean must be installed on the machine used for the review; a `tests/Dockerfile` may be written and set `[verifier] environment_mode = "separate"` in `task.toml`.
    - The agent judge's materials are kept in `tests/agent-judge/`: `problem-tree.toml` (the problem tree written in step 2 and confirmed in step 3), `evaluation-toolkit/` (the tools it may call and their sound use) and `reference/` (the metrics and domain knowledge on which the evaluation rests).
    - The rubric is written into `verification_explanation` in `task.toml`. The agent judge works through the leaves on the basis of `problem-tree.toml` and the rubric.
    - `tests/test.sh` runs the agent judge and writes the score to `reward.json`; it writes each leaf's verdict and evidence, together with the overall judgement (claims supported, gaps, score), to `verification.json`.
    Fix random seeds wherever random numbers are used. Data reserved for the review and the reference answer are kept only in `tests/`.
7. **Check repeatedly until all conditions are met.** Run `ale lint` and `ale calibrate`, correct what they report, and continue until the four completion conditions below are all met. The two commands are described under "`ale lint` and `ale calibrate`" below.

## `ale lint` and `ale calibrate`

Running `ale` successfully on the expert's machine first exposes problems in the plan early. If `ale` is not yet installed on the expert's machine, install it following the instructions the project team gives to experts.

| Command | Function | Prerequisite |
|---|---|---|
| `ale lint` | Checks the format and configuration of the task package without running it, for example whether `task.toml` is correct, whether open network access is justified, whether images have pinned versions, and whether keys are written into the configuration | `ale` installed |
| `ale calibrate` | Runs each calibration case in `calibration/`, each time in a fresh environment: runs the case's `solve.sh`, has the agent judge score the result, and checks that the score falls within the range set in `[[calibration]]`. Failure to build the environment, scoring errors and timeouts all count as failures | Docker, for building the solving environment |

Run `ale lint` first and `ale calibrate` once it passes. The scoring must not be changed to make a calibration case pass; when a score falls outside its range, proceed as described under "Situations requiring a return to the expert" below.

For a task at physical-world observation level 2, scores that require an experiment cannot be obtained here; handle them as described in "Tasks at physical-world observation level 2" in `references/2-research.md`, and record the parts not run in `research/selfcheck.md`.

## Requirements for the task statement

`instruction.md` is given to the solving agent as it stands and follows the structure below. Parts marked "optional" or "where needed" may be omitted; all others are required.

```markdown
# Task title

## Task
The result to be obtained: the problem to be solved and what is finally submitted.

### Sub-questions
(Optional) The sub-questions of the problem tree, listed one by one.

## Input

### Initial state and available materials
The data, software and services already present in the environment, with their real paths (/home/user/...).

### Known conditions
(Optional) Conditions known at the start that cannot be found in the environment: the provenance of samples or data, literature values (with units and uncertainties).

## Output

### Deliverables
The path of each deliverable, consistent with artifacts in task.toml.

### Format
File format and structure, for example each key of a JSON file; where the output of each sub-question is placed.

### Units and conventions
(Where needed) The unit, sign convention and naming convention of each quantity.

## Evaluation

### Correctness criteria
The criterion for each item: the allowed error of a numerical value, or the equivalent forms accepted. Do not include the rubric, the reference answer or the scoring program.

## Constraints
(Optional) Explicit constraints: tools or resources that may not be used, files that may not be modified.
```

In addition:

- Solving can begin from the task statement and the solving environment alone, without further explanation.
- All sub-questions of the problem tree are listed by default; the unified output format is given under "Format".
- Do not reveal the reference answer.
- Include no identifier that could be used to look up the answer: paper titles, database IDs, CAS numbers, dataset accession numbers.
- Include no content from `research/`.

## Settings in task.toml

Begin the file with `schema_version = "1.4+ale.1"`; set `artifacts` to the paths of the deliverables, consistent with the task statement.

- `[task]`: `name` is the task name. Fill in `description` and `keywords` where available.
- `[metadata]`:
    - `verification_explanation`: required. How the quality of an answer is judged, as given in the plan: the rubric, how the per-item verdicts are combined into a score, and the expert's target. The problem tree is not written here; see `tests/agent-judge/problem-tree.toml`.
    - `verification_time_estimate_hours`: required. The expert's estimate, from the problem card, of the hours one verification takes.
    - `verification_cost_estimate`: where the expert has given an estimate, the compute and other costs of one verification.
    - `expert_time_estimate_hours`: where available, the expert's estimate of the hours they would need to solve the task.
    - `subfield`: the specific research area, where available.
    - `network_justification`: required when network access is open.
- `[metadata.science]`: `problem_class` (the problem class assigned by the expert: `explanation`, `prediction`, `inversion`, `design` or `development`), `discovery_level` (scientific discovery level 1, 2 or 3) and `observation_level` (physical-world observation level 0, 1, 2 or 3), as in the problem card.
- `[metadata.wet_lab]`: required for tasks at physical-world observation level 2, as in the problem card. `instrument_category` is the resource category, one of `autolab`, `benchtop` (benchtop instruments), `large_instrument` (large instruments), `robotics`; `instruments` lists each instrument used as "name + model", for example `["BioTek Synergy H1 plate reader", "Bio-Rad CFX96 PCR system"]`.
- `[agent]`: set the time limit `timeout_sec` according to the plan. Network `network_mode`: offline, allowlist or open; an allowlist requires `allowed_hosts`.
- `[environment]`: whether a GPU is needed, and which model. Resource settings must agree with the usage measured in step 2.
- `[[calibration]]`: one entry per calibration case, matching the folders in `calibration/` one to one. `name` is the case name, that is, the folder name; `expect` gives the expected score of `reward` and of any other metric, as a number or a range `[lo, hi]`; `reward` lies between 0 and 1, other metrics are unbounded.

## Completion conditions

The build is complete only when all four of the following are met:

1. The calibration cases include at least the empty submission, with an expected score of 0.
2. Every shortcut found in step 2 has been placed in `calibration/` as a calibration case.
3. Neither the reference answer nor any content of `research/` leaks into the task statement or the solving environment.
4. `ale calibrate` passes: every calibration case scores within the range set in `[[calibration]]`.

## Situations requiring a return to the expert

- Requirements in the plan conflict or cannot be implemented.
- A calibration case cannot be brought within its expected range for reasons other than a programming error.
- A new shortcut is found that can only be blocked by changing the scoring.

In any of these situations, stop, return to step 2 or step 3, consult the expert, revise the plan and obtain reconfirmation. The scoring must not be changed unilaterally. The step to return to in each situation is given in "Returning to earlier steps" in `SKILL.md`.
