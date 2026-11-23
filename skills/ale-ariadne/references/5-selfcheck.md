# Step 5: Self-check and trial runs

Before submission, have an agent solve the task once or twice on the expert's machine, then conduct a self-review. The purpose is to discover problems with the task itself before submission. When a problem is found, return to the step where it originates, correct it, and then redo this step.

## Trial runs

1. Open a separate session. It has access only to the task statement and the solving environment, not to `research/`, `tests/` or `calibration/`.
2. Have it work through the task from the start as in a real attempt, submit an answer, and obtain a score from the agent judge.
3. Carry this out once or twice, recording the process and score of each run in `research/selfcheck.md`. Where a trial run submits a partially correct answer, ask the expert for an expected score and add it to `calibration/` as a calibration case, with a corresponding `[[calibration]]` entry in `task.toml`.

For a task intended for RSI, use one of these trials to test a revision. After the first submission, give the same solving session only the feedback specified in the plan. Have it revise the candidate and submit again under the same conditions. Record the feedback, what changed and both results in the trial-run remarks. Check whether the feedback allowed a meaningful revision and whether the judge assessed it consistently, even if the score stayed the same or fell. If a required observation is unavailable, record which part of the trial remains untested.

Matters the trial runs must confirm:

- The environment starts, and the software and data named in the task statement are present.
- The task statement alone suffices to determine what is to be solved and submitted.
- An answer can be submitted, and the agent judge produces a score.
- Each leaf's verdict and evidence in `verification.json` correspond to the submission; the agent judge actually called the tools specified in the problem tree and did not rely on values reported by the submitter.
- The agent judge reviewed the evidence of all leaves together and can detect shortcuts such as artificial driving terms or imposed outcomes.
- The time limit and resources are sufficient.

For a task at physical-world observation level 2, the part requiring an experiment yields no score; record this faithfully in `research/selfcheck.md`.

## Self-review

1. Open another separate session. It has access only to the task package and the trial-run records, not to `research/` or to the construction process.
2. Have it judge, from these materials alone, whether the task has any problems.
3. Classify each shortcoming found into one of three categories:

| Category | Examples | Action |
|---|---|---|
| A problem with the task itself | The task statement is ambiguous; the environment lacks a component; the agent judge marks a correct answer as wrong or a wrong answer as correct | Correct the task; see below |
| An error by the solving agent | The task is sound; the solving agent miscalculated or went astray | Do not change the task |
| An environment or infrastructure failure | Machine, network or container failure unrelated to the task | Stop, resolve the failure, then try again |

## Correcting the task

1. **Reproduce first.** Run again to confirm that the problem is real.
2. **Locate the problem.** Task statement, environment, scoring or calibration cases.
3. **Correct the whole class of error together.** Do not correct only the instance found. For example, if one unit was not stated, check every quantity in the task statement.
4. **Test two examples after the correction.** An answer that takes a different approach but is still correct should pass; a wrong answer lying just beyond the boundary should not.
5. **Rerun `ale lint` and `ale calibrate`** and confirm that the four completion conditions of step 4 still hold.
6. **Record the correction.** Record the change and its reason in `research/selfcheck.md`.
7. **Repeat the trial runs and self-review.** After a correction, conduct another round of trial runs and self-review to confirm that the problem has been resolved.

The trial runs and self-review must be completed in full at least once. Thereafter the number of rounds is unlimited: at the end of each round, report unresolved problems to the expert, who decides whether to continue revising or to submit now.

## Situations requiring a return to the expert

If a correction would affect any of the following, it is not for the agent to decide; return to step 2 and consult the expert:

- The scientific meaning of the agent judge's checks, or the problem tree itself.
- The tolerance or scoring range.
- The goal or deliverables of the task.

After the change, update the plan as required in step 3, obtain the expert's reconfirmation, revise the task package according to the new plan, and redo this step in full. The step to return to in each situation is given in "Returning to earlier steps" in `SKILL.md`.

## Completion conditions for this step

This step is complete when all three of the following are met. Once the trial runs and self-review have been completed in full and recorded in `research/selfcheck.md`, the expert may also decide to submit with problems still unresolved; in that case follow the expert's decision and record the unresolved problems in `research/selfcheck.md`.

- A trial run completes from start to finish and obtains a score.
- The self-review finds no further problems with the task itself; where the task was corrected, this refers to the round conducted after the correction.
- All corrections are recorded.

## Output

`research/selfcheck.md`.
