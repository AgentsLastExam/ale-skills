---
name: ale-ariadne
description: Assist a domain expert in constructing an ALE task from a frontier scientific problem. The expert assigns the problem class (Explanation, Prediction, Inversion, Design, Development); the problem is decomposed into a problem tree by class and investigated with the expert, and for each leaf the checks to be called by the agent judge are specified; after the expert confirms the plan, the task package is built in a preliminary version, self-checked, and submitted to the project team. Applies to physics, chemistry, materials, biology, earth science and medicine problems that are purely computational, that use existing data, or that require a new observation obtainable within six hours. Use when an expert wishes to contribute a task or to turn a research problem of their own into a benchmark task.
---

# Assisting an expert in constructing an ALE task from a scientific problem

## Purpose of this Skill

A domain expert brings a scientific problem. The agent and the expert jointly construct from it an ALE (Agents' Last Exam) task, that is, a task package: another agent solves it from the task statement, and the solution is reviewed by an agent judge, which assigns a score between 0 and 1.

Many frontier problems lack a clear criterion of correctness at the outset. The construction therefore proceeds in the following order: the expert first assigns the problem class, and the problem is decomposed into a problem tree according to that class; the agent and the expert then carry out a round of research and specify the claim, evidence and check for each leaf; the task package is built only after the expert confirms the task plan.

Scoring is performed by the agent judge. Working from the problem tree, the agent judge examines each leaf actively: for every claim it calls tools such as numerical-check scripts, reruns, Lean and search to gather evidence, gives a verdict per leaf, and then combines the verdicts into an overall judgement and a score. See `references/agent-judge.md`.

**The task package built on the expert's side is a preliminary version.** Building and trial-running the package locally serves to confirm that the plan is feasible: the agent judge produces a score, and every calibration case, including the empty submission and the known shortcuts, scores within its expected range. The preliminary package is submitted to the project team together with the research records, but it does not become an official task as it stands. This must be made clear to the expert.

Besides constructing the task, this Skill serves two further purposes:

- **Determining the verification cycle and verification cost**, that is, the time and expense between the completion of a submission and the evaluation of its quality. Step 1 obtains the expert's estimate; step 2 measures it.
- **Accumulating problem sense**, that is, which problems in the field matter and why, and what constitutes a good result. Records are accumulated expert by expert. They are intended for the agent itself and are read before the next conversation with an expert in the same field.

## Principles of communication with the expert

The entire process takes the form of a conversation between the agent and the expert, not the completion of forms.

- **Follow up on the expert's statements.** Ask the expert to describe matters in their own words, then pursue the points raised. Ask no more than one or two questions at a time, and do not repeat questions the expert has already answered.
- **"Matters to confirm" are for the agent's own verification.** Each step file ends with "Matters to confirm before this step ends", and each discipline file contains "Matters to confirm in conversation". These are not read out to the expert, nor is the expert asked to answer them item by item. During the conversation, note which matters have been settled; for those that remain open, raise them as the topic allows, or first investigate or run computations and then ask with the results in hand.
- **Do not ask the expert for information the agent can obtain by investigation or computation.** The expert's time is reserved for matters only the expert can judge: whether a result is scientifically credible, what counts as correct, and how large a deviation counts as wrong.
- **Scientific judgements are made by the expert.** The agent may offer suggestions and evidence but does not decide in the expert's place. When the expert decides, record the decision and its rationale in the corresponding file. Discipline files describe common practice in each discipline for reference; where they differ from the expert's judgement, the expert's judgement prevails.
- **Each report contains three elements:** the work completed, the results obtained, and the matters requiring the expert's judgement.
- **Reply in the expert's language.**

## Before starting

At the start of every session, first read `references/0-setup.md`: determine the task name; in the first session, explain to the expert what will be submitted to the project team, and ask the expert to choose between submitting the full conversation or only the research records. The project team receives only the task folder that is finally submitted and reads no other files on the expert's machine.

## The five steps

Proceed in order. On entering each step, first read the corresponding file.

| Step | Work | Read first | Output | Condition for proceeding |
|---|---|---|---|---|
| 1 Screening | Clarify the problem, have the expert assign the problem class, record problem sense, establish the verification cycle and cost, and judge whether the problem is suitable for construction here | `references/1-screen.md`, `references/problem-sense.md`, the matching `references/problem-sense/*.md`; once the class is assigned, the matching `references/classes/*.md` | `research/problem-card.md`, `research/problem-sense-notes.md` | The expert confirms the problem card and decides to proceed |
| 2 Research and exploration of checks | Build the problem tree, specify claim, evidence and check for each leaf, run the computations and ablations, prepare and trial-run the agent judge, and measure the verification cycle and cost | `references/2-research.md`, `references/agent-judge.md`, the matching `references/classes/*.md`, the matching `references/disciplines/*.md` | `tests/agent-judge/problem-tree.toml`, `research/research-log.md`, `research/verifier-decision.md` | The expert has confirmed the problem tree and the check for each leaf, the rationale is recorded, and shortcut testing has been carried out |
| 3 Expert confirmation of the task plan | Compile the task scope, deliverables and scoring into a task plan | `references/3-plan.md` | `research/plan.md` | The expert explicitly confirms |
| 4 Preliminary build | Build the task package according to the task plan | `references/4-build.md`, `references/agent-judge.md` | The task package (`task.toml`, `instruction.md`, `environment/`, `tests/`, `calibration/`) | All four completion conditions are met |
| 5 Self-check and trial runs | Have an agent solve the task once or twice, have the agent judge review the results, conduct a self-review, and correct any problems | `references/5-selfcheck.md` | `research/selfcheck.md` | A trial run completes, and the self-review finds no problem with the task itself |

The five steps must be completed in full at least once before submission. Thereafter, whether to continue revising and when to submit is for the expert to decide. Submission follows `references/6-submit.md`.

## Returning to earlier steps

The five steps are not strictly linear. When a later step reveals a problem, return to the step where the problem originates, correct it, and then redo the affected later work.

| Step where found | Problem | Return to | Expert must reconfirm the plan |
|---|---|---|---|
| Step 2 | None of the checks tried holds up | Remain in step 2 and try other checks. If none is workable, return to step 1 and reconsider the scope of the problem with the expert, or put the task on hold | Not yet confirmed |
| Step 3 | On reviewing the plan, the expert requires a change in scoring for which no run evidence exists | Return to step 2 for additional runs, then revise the plan | Yes |
| Step 4 | Requirements in the plan conflict or cannot be implemented; a calibration case cannot be brought within its expected range for reasons other than a programming error; a shortcut is found that can only be blocked by changing the scoring | Return to step 2 or step 3 | Yes |
| Steps 4, 5 | The task statement is ambiguous, the environment lacks a component, or the code contains an error, without affecting the goal, deliverables or scoring | Return to step 4 to correct, then redo step 5 | No |
| Step 5 | The agent judge marks a correct answer as wrong or a wrong answer as correct | First determine the cause. For an implementation error, return to step 4; for a flaw in the scoring itself, return to step 2 | Yes, if the scoring changes |
| Step 5 | The time limit or resources are insufficient | Return to step 3 to revise resources and time limit in the plan, then to step 4 to revise the configuration | Yes |

When returning to an earlier step:

- **Propagate changes to the plan.** When the goal, deliverables or scoring change, ask the expert to reconfirm, revise the task package according to the new plan, and redo step 5 in full.
- **Self-check again after corrections.** After correcting the task in step 5, conduct another round of trial runs and self-review to confirm that the problem has been resolved.
- **Record every return.** Record the reason, the step returned to and the changes made in the research log, and reset the step number in the first line of the problem card.
- **The five steps must be completed in full at least once before submission; thereafter the number of rounds is unlimited, and the time of submission is for the expert to decide.** After the first full pass, report the current status and any unresolved problems to the expert at the end of each round. If the expert wishes to continue revising, continue; if the expert decides to submit, submit, neither obstructing nor pressing. Record unresolved problems faithfully.

## ALE Brew tools

No tools are called between steps; all records are written to the task folder. Once the five steps have been completed and the expert decides to submit, use `request_upload` and `submit_task` to submit the entire folder to the project team; see `references/6-submit.md`.

## Mandatory rules

1. Research first, then determine the scoring, and only then build the task. Do not write the task package before the expert confirms the task plan.
2. The check for every leaf of the problem tree must actually be run, and the agent judge must actually be trial-run, with the run results serving as evidence. Nothing may be decided by reasoning alone.
3. After the expert's confirmation, the agent may not change the goal or the scoring of the task on its own. Where a change is needed, revise the task plan and ask the expert to reconfirm.
4. Each task has exactly one score, between 0 and 1.
5. An empty submission must score 0.
6. Neither the reference answer nor any content of `research/` may appear in the task statement or the solving environment.
7. For a task at scientific discovery level 3, the checks the agent judge runs constitute the proxy verifier proposed by the expert, which may consist only of necessary conditions: an answer that passes may hold in some sense, and whether it truly holds is for the expert to judge. In communication with the expert and in every file, never describe "passing the checks" as "the problem is solved".
8. Tasks that require a new observation obtainable within six hours proceed through the five steps as usual. The part that requires an experiment cannot be run on the expert's side; see "Tasks at physical-world observation level 2" in `references/2-research.md`. Tasks requiring more than six hours are not built.
9. Every run is recorded in the research log, including failed runs.
10. If no workable check can be found, put the task on hold and keep the research log. Do not force the construction.
11. Record the verification cycle and cost faithfully: the expert's estimate in step 1 and the measurement in step 2. Do not persuade the expert to change the problem because verification is slow or expensive, and do not judge on your own whether it is fast enough.
12. Files under `references/problem-sense/` are maintained by the project team; the agent reads them but does not modify them. Do not disclose the identity of other experts to the expert.
13. Record a confirmation at the end of the plan, with the expert's own words, only after the expert has explicitly confirmed. Never confirm on the expert's behalf.
14. The task package built on the expert's side is a preliminary version, not an official task. Do not tell the expert that the task will be published as it stands.

## Three classifications

During screening, the problem receives the following three classifications. The requirements of every later step depend on them.

**Problem class**

A scientific problem involves three kinds of object: laws (mechanisms, theories, models), systems (molecules, materials, devices, strata and so on) and phenomena (observed data and the properties exhibited). The five classes are distinguished by which objects are known and which is sought. The problem class is assigned by the expert; the agent does not assign it in the expert's place.

| Class | Known | Sought | Class module |
|---|---|---|---|
| Explanation | System and phenomenon | Law | `references/classes/explanation.md` |
| Prediction | Law and system | Phenomenon | `references/classes/prediction.md` |
| Inversion | Law and observed data | The system that already exists behind the data | `references/classes/inversion.md` |
| Design | Law, and a set of conditions to satisfy | A system, not previously existing, that meets all conditions | `references/classes/design.md` |
| Development | Law, and a metric to improve | The level the metric can reach | `references/classes/development.md` |

All five classes follow the same construction process; they differ in how the problem tree is decomposed, in the necessary conditions, in the calibration cases and in the common shortcuts, which are set out in the class modules. Class modules only add content; they do not alter the provisions of this file or of the step files.

**Scientific discovery level**

| Level | Name | Meaning |
|---|---|---|
| 1 | Workflow execution | Carry out a task by a known procedure; the answer is known |
| 2 | End-to-end research | Conduct a complete piece of research from question to conclusion; may reproduce the results of a published paper |
| 3 | Open problem solving | A well-defined problem not yet solved, or one in which previous results can be surpassed |

**Physical-world observation level**

| Level | Meaning | Treatment |
|---|---|---|
| 0 | Pure computation, simulation, theory | Built |
| 1 | Uses existing data | Built |
| 2 | Requires a new observation obtainable within six hours | Built. The part requiring an experiment cannot be run; see `references/2-research.md` |
| 3 | Requires a new observation taking more than six hours | Not built |

## Working directory

The expert runs the agent in a working directory, in which each task occupies a directory named after the task. `research/` records the work step by step; it is submitted to the project team and never placed in the solving environment. The task package here is a preliminary version.

```
<task-name>/
  task.toml            # task configuration: resources, time limit, network access
  instruction.md       # task statement, given to the solving agent as is
  environment/         # Dockerfile, setup scripts, offline software and data
  tests/               # scoring: test.sh runs the agent judge, which gives a score between 0 and 1
    scripts/           #   numerical-check scripts, called by the agent judge and runnable on their own
    lean/              #   Lean statements and proofs, present only when used
    agent-judge/       #   the agent judge's materials: problem-tree.toml (the problem tree), evaluation-toolkit/, reference/
  calibration/         # calibration cases: one folder per case containing solve.sh; expected scores in [[calibration]] in task.toml
  research/
    problem-card.md      # step 1: problem card, including verification cycle and cost
    problem-sense-notes.md # from step 1: problem sense obtained from this expert; no fixed format
    research-log.md      # step 2: method, result and compute of each run
    verifier-decision.md # step 2: checking plan: tools the agent judge calls for each leaf, evidence, rationale
    plan.md              # step 3: task plan confirmed by the expert
    selfcheck.md         # step 5: record of trial runs and self-review
    sources.md           # sources of data and code
    conversation/        # present only if the expert chose to submit the full conversation: session records saved by the hook
```

Templates are in `templates/`. The hook installation script is in `scripts/`; its use is described in `references/0-setup.md`.

## Resuming after an interruption

At the start of a new session, first read the task's `research/`. The first line of the problem card records the current step; resume from that step. Do not ask the expert again about matters already answered.
