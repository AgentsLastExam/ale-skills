# Submission

The five steps must be completed in full at least once before submission. Thereafter, whether to continue revising and when to submit is for the expert to decide.

Use `submit_task` to submit the task's entire folder to the project team: the preliminary task package and `research/`. If the expert chose to submit the full conversation, the conversation records in `research/conversation/` are submitted with the folder.

## Checks before submission

The first four items indicate that the five steps have been completed once; if any is missing, the task cannot be submitted, and `submit_task` will also refuse it. For the remaining items, report any that are not yet satisfied to the expert, who decides whether to submit now or to complete them first.

- All five parts of the task package are present: `task.toml`, `instruction.md`, `environment/`, `tests/`, `calibration/`.
- All seven records are present in `research/` and up to date.
- The confirmation at the end of the plan applies to the current version. If the plan has changed substantively since confirmation, ask the expert to reconfirm.
- Both the expert-estimate and measured columns of "Verification cycle and cost" in the problem card are filled in. For a task at physical-world observation level 2, parts that cannot be measured are recorded as such.
- `ale lint` and `ale calibrate` pass: every calibration case, including the empty submission, scores within the range set in `[[calibration]]`. For a task at physical-world observation level 2, scores that require an experiment are recorded as not run.
- For a task at physical-world observation level 2, `task.toml` contains `[metadata.wet_lab]`.
- The task statement and solving environment contain no content of `research/` and no reference answer.
- `research/sources.md` gives the source of every piece of data and code used.
- No file contains passwords, keys or personal accounts.
- No file, including the session records in `research/conversation/`, contains data that its licence or data use agreement does not allow to be passed to the project team.
- If the expert chose to submit the full conversation, `research/conversation/` contains the session record files for this task.

If `submit_task` refuses the submission, the `missing` field of its response lists what is lacking.

## Submission procedure

Submission requires two parameters, taken from the problem card and written in the expert's language: `problem`, the one- or two-sentence statement of the problem accepted by the expert, and `progress_criterion`, what result constitutes progress.

Call `request_upload`, run the command it returns in the working directory to upload the task folder, then call `submit_task` with the `upload_id`. Include `research/` in the upload.

`submit_task` first checks the task package: whether all five parts are present, whether files from `research/` have been copied into the task statement or solving environment, whether symbolic links are present, and whether the package is too large. Problems found are listed in the `problems` field of the response; correct them and submit again. Large files that cannot go into the task package are stored in the controlled dataset designated by the project team, as described in step 4.

A task that is not built or has been put on hold has no task package; its folder is still submitted with `submit_task`. The folder must contain the problem card and the problem-sense notes, and the problem card must state the outcome and the reason. The project team uses these two records as well.
