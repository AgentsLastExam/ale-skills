# Merging new records into the discipline's problem sense

This file is for the project team. The expert's agent does not need to read it and must not act on it.

`references/problem-sense/<discipline>.md` records the project team's understanding of the discipline. It is intended for the agent, not for human readers, and has no fixed format.

On receiving a new `research/problem-sense-notes.md`:

- Read the new record and the discipline's existing file, then rewrite the file as a whole so that it reads as one coherent understanding of the field. Do not append records one by one at the end.
- Keep reasons and concrete examples. Content reduced to conclusions cannot be understood later.
- Where experts disagree, set out both views with their reasons; do not reduce them to a single compromise statement.
- Record only what experts have stated and understanding supported by the records; add nothing of your own.
- Do not record experts' names or anything that could identify them, such as institutions, collaborators or unpublished work.
- Where the verification cycle and cost figures in the same task's problem card bear on the understanding of the field (which kinds of result can be verified quickly, which are slow or expensive), include them.
- Revise the Chinese and English versions together.

## Source of the records and where revised files are placed

- Records submitted through the ALE Brew tools are exported with `ale-brew-mcp export-notes --data <data directory> --discipline <discipline> --output <directory>`: the problem-sense notes and problem card of each task, together with an `index.json` containing each task's verification cycle and cost figures. Exported files carry only account numbers, not names.
- Revised files are placed in the ALE Brew data directory at `problem-sense/zh/<discipline>.md` and `problem-sense/en/<discipline>.md`; the expert's agent obtains the new version the next time it calls `get_guide`. The copies under the Skill's `references/problem-sense/` are replaced with the next update of the Skill.

## Merging pitfall records

`references/pitfalls/<step file name>` holds the pitfall records that originate in each step; `references/pitfalls.md` tells the expert's agent how to read and write them. On receiving a task folder, read the "Pitfall records" section of its `research/research-log.md`.

- File each record under the step in which the problem originated, not the step in which it was found.
- Keep the task name, the leaf, script or calibration case concerned, and the numbers that show the failure: scores, thresholds, counts, times. A record reduced to its rule is general advice again and cannot be compared with another task.
- Remove reference answers, held-out values and anything from which the answer to a task could be recovered; these files are read on other experts' machines. Remove anything that could identify the expert.
- Check each number against the numbered run it cites in the same research log. Leave out a number that cannot be traced to a run, and say that it was left out.
- Keep "Where the rule stops" with its rule. Where two records disagree, set out both with their tasks and numbers; do not reduce them to one compromise rule.
- When a new record is another instance of an existing one, add it to that record as a further instance with its own task and numbers, and revise the rule or its limit if the new instance requires it.
- When a record is shown to be wrong, keep it, mark it as superseded, and state what replaced it and what following it cost.
- Add nothing that no submitted record supports. Do not write records from memory or by analogy with other projects.
- Where a record shows that a step file, a class module or a discipline file is wrong or silent, correct that file as well, and leave the record in place as the evidence for the correction.

Revised files are placed under the Skill's `references/pitfalls/` and reach experts with the next update of the Skill.
