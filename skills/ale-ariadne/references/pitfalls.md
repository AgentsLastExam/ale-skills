# Pitfall records

A pitfall is something that went wrong during the construction of a task in a way that was not visible at once: a check that passed a wrong answer, a score that looked sound and was not, a correction that reopened a problem already closed. A pitfall record states, for one such incident, in which task it happened, with which numbers, how it could have been noticed, and how far the lesson reaches.

General advice such as "check that the tolerance is reasonable" changes little, because it does not say when the advice applies or what failure looks like. A record that names the task, the leaf, the script and the values observed can be compared with the task at hand. Records accumulate task by task. Like problem sense, they are intended for the agent itself and are read before the same work is done on the next task.

## Before each step

On entering a step, read the records already accumulated for it, in `references/pitfalls/` under the same file name as the step file, for example `references/pitfalls/2-research.md`. If the file is still empty, begin directly.

When reading a record:

- A record is evidence from one named task under the conditions it states. It does not override `SKILL.md`, the step files or the expert's judgement.
- Read "Where the rule stops" together with the rule. It states what the record does not license.
- Where the situation of a record resembles the present task, run the check named in its "tell" on the present task and enter the result in the research log. Do not decide by reasoning alone that the record applies or does not apply.
- Do not tell the expert which other tasks or experts the records come from.

## When to write a record

Write a record when any of the following occurs, in any step:

- The work returns to an earlier step, as listed in "Returning to earlier steps" in `SKILL.md`.
- A check or the agent judge gives a wrong verdict: a wrong or shortcut submission passes, or a correct submission that takes another approach fails.
- A calibration case scores outside its expected range for a reason other than a programming error.
- A result that was accepted is later found to be wrong: a run that finished without error and measured something else, a score produced without the specified tools being called, a file that was present and incomplete.
- The same correction has to be made a second time.

Do not write a record for the following; they stay in the research log or the record of trial runs only:

- A failure that announces itself and is corrected at once, such as a crash with a clear message or a typing error.
- An error by the solving agent on a sound task, or a failure of the machine, network or container (the second and third categories in step 5).
- A scientific decision of the expert that differs from common practice. That is the expert's judgement, recorded with its reason where the step file says, and is not a pitfall.

## Form of a record

Write the record in the "Pitfall records" section of the task's `research/research-log.md`, when the incident is understood and not at the end of the task. Each record has the following parts.

- **Rule**: one sentence stating what to do, written as an instruction. It is the heading of the record.
- **Task and step**: the task name; the step in which the problem originated and the step in which it was found.
- **What happened**: the leaf, script, calibration case or file concerned, the value observed and the value expected. Take every number from a numbered run in the research log and cite the run.
- **What it looked like**: why it was not noticed at once, that is, what a reader of the output saw.
- **The tell**: the cheapest observation that would have exposed it, stated so that it can be repeated on another task.
- **Cause**: the cause, and the run that established it. Where the cause is a conjecture not yet tested by a run, say so.
- **Correction**: what was changed, every other place changed for the same class of error, and the check that now guards against a recurrence.
- **Cost**: the runs, time, compute and rounds with the expert that the incident took.
- **Where the rule stops**: see the next section.

A record is usable when it could not have been written about another task. Compare:

- Too general: "The amplitude check was too loose and a shortcut passed."
- Usable: "In `<task name>`, leaf `<id>`, `tests/scripts/<script>` scored `<value>` for the submission of run `<n>`, which imposed the initial shape instead of letting the oscillation arise; the plan expects `<range>` for this shortcut. The script compared the amplitude after `<k>` cycles only, so an imposed shape that had not yet decayed passed."

When recording:

- Record only what a run showed. Do not reconstruct a number from memory; where a value was not recorded, write that it was not recorded.
- Write one record per pitfall. When the same pitfall occurs again, add the new instance to the existing record with its own numbers; a second instance often shows that the first statement of the rule was too narrow or too wide.
- When a later run shows that a record was wrong, do not delete it. Mark it as superseded, state what replaced it, and state what following the wrong version cost.

## Where the rule stops

A rule drawn from one incident tends to be applied too widely afterwards. Each record therefore states its limit, in one or more of three forms:

- **A case the rule does not cover.** A situation that resembles the incident and in which following the rule would be wrong. For example, a record about a tolerance that was too loose does not license a tolerance tighter than the error of the reference itself.
- **A correction that was refused.** A change that would have made the symptom disappear and was not made, with the reason. Typical cases are changing the scoring so that a calibration case passes, which step 4 forbids, and making a check pass by placing in the solving environment something that had been withheld from it.
- **What the incident does not show.** One task in one discipline at one scale; state which of these the conclusion depends on.

Where the limit is not yet known, write "not yet known". Do not supply a limit that no run or statement of the expert supports.

Where the pitfall concerns scoring, the submission that exposed it is itself a counter-example the agent judge must handle. Keep it as a calibration case with the expected score set by the expert, as steps 2, 4 and 5 already require, and name that case in the record. `ale calibrate` then tests it again after every later change.

## Where the record goes

The research log is submitted to the project team with the other files in `research/`. The project team merges pitfall records into the files under `references/pitfalls/`, keeping the task name and the numbers that show the failure, and removing reference answers and anything that identifies the expert. The expert must be told this before starting; see `references/0-setup.md`.

Files under `references/pitfalls/` are maintained by the project team; the agent does not modify them. If the task is ultimately not built or is put on hold, its pitfall records are still kept and submitted.
