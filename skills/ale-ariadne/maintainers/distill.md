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
