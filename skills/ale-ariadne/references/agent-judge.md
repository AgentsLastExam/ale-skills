# The agent judge

Scoring is done by an agent judge. Working from the problem tree, the agent judge checks each leaf actively: for every claim it calls the tools it needs to gather evidence, then reaches a verdict on that evidence. Checking tools such as numerical-check scripts and Lean do not decide the score on their own; the agent judge calls them as needed.

Step 2 prepares the agent judge's tools and materials and trial-runs it; step 4 puts them into the task package; step 5 uses it to review the trial runs.

## Review procedure

1. **Read the submission**: conclusions, code, raw output and the solution trajectory.
2. **Check each leaf**: following the claim and check of that leaf in the problem tree, call the relevant tools to gather evidence.
3. **Give a verdict per leaf**: one of "supported", "partly supported", "unsupported" or "insufficient evidence", with the evidence it rests on.
4. **Review together**: examine the evidence from all leaves together and check its physical consistency. Passing one item alone does not show that the whole holds: a simulation with an artificial external forcing term, for example, can pass the reproduction check on its own.
5. **Overall judgement**: the claims supported, the gaps that remain, and a score between 0 and 1.

The per-leaf verdicts, evidence and overall judgement go into `verification.json`; the score goes into `reward.json`.

## Callable tools

| Tool | Use | Where in the task package |
|---|---|---|
| Numerical-check scripts | Measure characteristic quantities in simulation output (frequency, amplitude, energy balance), compare with data, check convergence and uncertainty. Each script runs on its own: its input is the solving agent's submission, its output the verdict and evidence for that item | `tests/scripts/` |
| Rerunning | Rerun submitted code or ablation simulations, confirm results reproduce, recompute metrics | The review environment provides the software needed |
| Lean tool | Compile statements written in Lean in advance and confirmed by the expert, with their proofs, and check that no proof relies on unapproved axioms | `tests/lean/` |
| Search tool | Search the specified databases for novelty and leakage checks | Listed in the evaluation toolkit |
| Trajectory inspection | Examine the solution process to detect shortcuts such as artificial driving terms or imposed outcomes | The agent judge reads the trajectory directly |

Which tools are used is set by each leaf's check in the problem tree, confirmed by the expert.

## Materials required by the agent judge

| Material | Content | Where |
|---|---|---|
| Problem tree | The root question, the sub-questions, and for each leaf what is given, the claim, the forms of the deliverable, the tools for checking and the criteria | `tests/agent-judge/problem-tree.toml` |
| Evaluation toolkit | The tools it may call, and which ways of checking the solving agent's quantitative results are sound | `tests/agent-judge/evaluation-toolkit/` |
| Reference material | The metrics and domain knowledge the evaluation rests on; explanations already ruled out, with the grounds | `tests/agent-judge/reference/` |

Calibration cases are kept in the top-level `calibration/` of the task package; see "Calibration cases" below.

The rubric goes into `verification_explanation` in `task.toml`. The agent judge works from the problem tree and the rubric.

## Unified output format

Different solutions to the same sub-question submit output in the same format. In the levitated-drop problem, whatever physical effects a simulation includes, the submission is the drop outline as a function of time, and the agent judge checks it with a single numerical-check script. A unified format makes the checking tools independent of the particular solution. Numerical-check scripts are written against the unified format, not against individual physical elements.

## Automatic checks

Some tools can also run on their own before the review, as automatic checks such as submission-format checks and short numerical reproductions. An automatic check shows only that results can be reproduced, not that the conclusions are scientifically correct. In one trial run of the levitated-drop example, the agent stopped after about 8 minutes without a 3D simulation, and the automatic check still gave a full score. Scientific conclusions are therefore judged leaf by leaf by the agent judge.

## Calibration cases

Every task carries a set of calibration cases; a reference solution is not required. Each case has a `solve.sh` in `calibration/<case name>/` that writes the final state of that case; its expected score (a number or a range `[lo, hi]`) is set in `[[calibration]]` in `task.toml`, with `name` matching the folder name.

- **Empty submission**: `solve.sh` writes nothing; expected to score 0.
- **Known results** (if any): the expert's result, a published result or the baseline; expected scores set by the expert.
- **Shortcut and partially correct solutions**: expected scores set by the expert. The class module lists the cases commonly used for that class.

The agent judge must score every case within its expected range; if it does not, revise the rubric or the evaluation toolkit before any evaluation. Calibration cases come from results produced during research and trial runs, and they also serve as the task's milestones. Research runs and the trial runs of step 5 often produce partially correct results; keep them all and ask the expert for expected scores.

## Stability

Review the same submission several times, record the spread of scores, and compare it with the score gap between good and poor answers. If the spread is too large, revise the rubric or the evaluation toolkit to make the basis of judgement more explicit.

## Tasks at scientific discovery level 3

The checks the agent judge runs can usually test only necessary conditions: passing all of them shows the claim may hold, but does not by itself establish it. For a task at scientific discovery level 3, these checks form the proxy verifier proposed by the expert, and results the agent judge finds supported are judged by the expert.
