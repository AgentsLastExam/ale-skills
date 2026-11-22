# Accumulating problem sense

In constructing tasks with experts, the agent obtains a great deal of information about the field: which problems matter and why; what constitutes a good result; on what basis peers accept a result; which approaches have been tried without success. Recording this information expert by expert builds up an understanding of the field, that is, the discipline's "problem sense".

These records are intended for the agent itself, not for human readers. Reading them before the next conversation with an expert in the same field allows that conversation to build on existing understanding rather than start from nothing. They therefore have no fixed format; write them in whatever way will best support later understanding of the field.

## Before the conversation

Read the understanding already accumulated for the discipline, in `references/problem-sense/<discipline>.md` supplied with the Skill. It contains what has been learned from earlier conversations with experts in the discipline. If the file is still empty, begin directly.

## During the conversation

No separate round of questions is needed. When the expert describes their problem, they will usually speak of its importance, the current difficulty and what result would constitute progress. Follow up on these points and widen the topic from the task to the research direction. Points worth pursuing include, for example:

- Other problems in the direction that the expert considers important, and the reasons.
- What constitutes a good result, and on what basis peers accept it.
- Problems the expert once considered and later set aside, and why.

Note such views whenever the expert expresses them in later steps as well, for example when describing in step 2 how the field judges whether a result is credible.

After reading the existing material, where something is unclear or the expert's view differs from it, ask about it when a related topic arises. Do not disclose the identity of other experts.

This work must not take time away from constructing the task. If the expert wishes to proceed directly with the task, give the task priority.

## Recording after the conversation

Write the record to the task's `research/problem-sense-notes.md`. No format is required; record the new understanding gained from this expert, for example:

- Which problems in the direction matter, and in what respect.
- What constitutes a good result, and on what basis peers accept it.
- How the field judges whether a result is credible.
- Problems the expert considers not worth pursuing, or that have been tried without success, and the reasons.
- Which results can be judged correct or incorrect quickly, and which require a long wait or high cost.

When recording:

- Record the reasons. Conclusions without reasons cannot be understood later.
- Distinguish between what the expert said and the agent's own understanding. Record the expert's statements as close to verbatim as possible.
- Do not supply on the expert's behalf what the expert did not say.

If the task is ultimately not built or is put on hold, this record is still kept and submitted.

## Where the record goes

The record is submitted to the project team with the other files in `research/`. The project team merges the records into the file for the corresponding discipline under `references/problem-sense/`, without the expert's name. The expert must be told this before starting; see `references/0-setup.md`.

Files under `references/problem-sense/` are maintained by the project team; the agent does not modify them.
