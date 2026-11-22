# Step 1: Screening

This step determines whether the problem is suitable for construction here. Two further tasks are carried out at the same time: establishing the time and cost of one verification, and recording the problem sense obtained from the expert. The outputs are a problem card, confirmed by the expert, and a problem-sense record.

## Procedure

1. **Hear the expert's account of the problem.** Ask the expert to explain in their own words what the problem is, why it matters, where the current difficulty lies, and what result would constitute progress. If the problem comes from the project team's problem list, read that entry in full before the conversation.
2. **Accumulate problem sense.** Before the conversation, read the matching `references/problem-sense/<discipline>.md`. While the expert describes the problem, follow up on the research direction: which problems matter, why, and what constitutes a good result. Afterwards, record this in `research/problem-sense-notes.md`; see `references/problem-sense.md`.
3. **Investigate first.** Read the papers, data and code the expert provides. Verify that the data and code can be obtained, that their licences permit inclusion in a task, and that the code runs on the current machine. Bring the findings back to the expert for confirmation rather than asking the expert to investigate on the agent's behalf.
4. **Read the "Screening criteria" in the discipline file.** The files are in `references/disciplines/`, selected by discipline.
5. **Determine the three classifications.** Problem class, scientific discovery level and physical-world observation level, defined in `SKILL.md`. The problem class is assigned by the expert; once it is assigned, read the matching class module `references/classes/*.md` and, in the course of the conversation, settle its "Matters to confirm with the expert for this class". When either of the other two classifications is uncertain, explain the agent's reasoning to the expert and let the expert decide.
6. **Establish the verification cycle and verification cost.** See "Verification cycle and verification cost" below.
7. **Estimate the curation cost.** Give an estimate with its basis: the effort required to turn the problem into a task, whether the data are ready or require cleaning, and whether known results exist that can serve as calibration cases.
8. **Determine the outcome.** According to the table below.
9. **Ask the expert to review the problem card.** Ask the expert to confirm its content and to decide whether to proceed. Enter step 2 only after the expert decides to proceed.

## Verification cycle and verification cost

"One verification" means the whole process from the completion of a submission to an evaluation of its quality.

In each ALE evaluation, every submission is reviewed once. The time and expense of one verification determine whether the task can actually be run in an evaluation and what the evaluation costs in total.

Establish the following with the expert and record it in the "Expert estimate" column of "Verification cycle and cost" in the problem card. Where a precise figure cannot be given, record a range with its basis; step 2 will measure it.

- **Cycle.** Under current practice in the field, the time needed to verify a result (seconds, minutes, hours or days), and where that time is chiefly spent.
- **Computational budget.** The compute needed for one verification: CPU or GPU, core-hours, memory.
- **Experimental budget.** Whether verification requires an experiment or new observation; if so, the time per run, the materials and expense, the equipment required, and the number of runs possible per day.
- **Personnel.** Whether verification can be carried out entirely by program; where human judgement is needed, who provides it and how long each judgement takes.
- **Other costs.** Paid data, software licences, external service calls.
- **Form of the score.** Whether verification yields a continuous quantity (an error, a metric, a bound) or only correct and incorrect; whether a better answer receives a higher score; whether repeated verification of the same answer gives the same result.
- **Cost of a single attempt.** The approximate time and compute an agent needs from receiving the task to submitting an answer.

Establish one further matter with the expert: **whether a faster, cheaper method of verification exists that the expert would still accept.** Examples include screening with an inexpensive method before confirming with an expensive one, substituting a small system for a large one, or substituting existing data for new measurement. Record which methods the expert accepts and which not, with the reasons. The check tried first in step 2 is often determined by this.

Notes:

- These are matters the expert can answer from experience. Raise them in the course of the conversation rather than all at once.
- The agent's responsibility is only to obtain and record these figures accurately. Do not persuade the expert to change the problem because verification is slow or expensive, and do not judge on your own whether the task is fast enough.
- For tasks at physical-world observation level 2, the experimental budget requires particular attention.

## Outcome

| Situation | Action |
|---|---|
| Pure computation, or uses existing data | Proceed to step 2 |
| Requires a new observation obtainable within six hours | Proceed to step 2. First establish the resource category (AutoLab, benchtop instruments, large instruments, robotics) and each instrument to be used (name, model), and record them in the problem card |
| Requires a new observation taking more than six hours | Do not build. State the reason in the problem card |
| Falls under "Hold for now" in the discipline file | Explain the reason to the expert and consider together whether an equally valuable and verifiable formulation exists. Whether to change the formulation is the expert's decision. Never alter the problem until it loses its meaning merely to make it easier to score |

## Matters to confirm before this step ends

- The problem can be stated clearly in one or two sentences, and the expert accepts the statement.
- The expert has specified what constitutes progress in concrete terms (a quantity, a bound, a metric), not "looks reasonable".
- The possible sources of the true value: an exact solution, recomputation, existing data, or comparison with a baseline.
- The data and code can be obtained, and their licences are clear.
- The three classifications are determined, the problem class having been assigned by the expert.
- The "Matters to confirm with the expert for this class" in the class module are settled.
- The approximate compute required, and whether the expert has access to it.
- The approximate time and cost of one verification (compute, experiment, personnel, other costs), with the expert's estimate and its basis.
- Whether the score is a continuous quantity or only correct and incorrect.
- Whether a faster, cheaper method of verification exists that the expert would still accept.
- Physical-world observation level 2: the resource category and the instruments are established.
- The problem sense obtained from the expert has been recorded in the problem-sense notes.

## Output

- `research/problem-card.md`, written from `templates/problem-card.md`.
- `research/problem-sense-notes.md`, with no fixed format; see `references/problem-sense.md`.
