# Before starting: determine the task name and explain what is submitted

The research records and the preliminary task package are written to the task's folder. Nothing is submitted between steps; once the five steps are complete, the entire folder is submitted to the project team at once with the ALE Brew tools. At the start of every session, complete the following before entering step 1.

## 1 Tools required for submission

Submission uses the ALE Brew tools `request_upload` and `submit_task`. First check whether these tools appear in the tool list.

If they are not connected, ask the expert to connect ALE Brew: the expert signs in to the ALE Brew Science website and generates an access token on the "Use in your own agent" page, which also gives the server address and ready-made commands. Ask the expert to place the token in the environment variable `ALE_BREW_TOKEN` and then add the connection:

- Claude Code: `claude mcp add --transport http ale-brew <address> --header "Authorization: Bearer $ALE_BREW_TOKEN"`
- Codex: add a `[mcp_servers.ale-brew]` section to `~/.codex/config.toml` containing `url = "<address>"` and `bearer_token_env_var = "ALE_BREW_TOKEN"`.

The expert adds the connection personally. Never ask the expert to paste the token into the conversation. A new session must be started after connecting.

A missing connection does not affect the first five steps; it need only be in place before submission.

## 2 Determine the task name

The task name consists of a few lowercase English words joined by underscores, for example `ising_gap_scaling`. It is also the name of the task's directory in the working directory and does not change once set. In a first conversation where the problem is not yet clear, listen to the expert before choosing the name.

When continuing an existing task, read `research/` in that task's folder and resume from the step recorded in the first line of the problem card.

## 3 In the first session, explain what is submitted to the project team

In the first session, explain the following points to the expert in the agent's own words, then wait for the expert's reply:

- **What is submitted**: the task's entire folder, submitted once after the five steps are complete. It contains seven research records (problem card, problem-sense notes, research log, checking plan, task plan, record of trial runs and self-review, sources) and the preliminary task package; the problem tree is kept in the task package as material for the agent judge. The verification cycle and cost, and the expert's own words when confirming the plan, are recorded in these files.
- **Whether the conversation is submitted**: the expert chooses one of two options. The first is to submit the full conversation: a hook is installed, and at the end of each round it copies the session's record file into the task's `research/conversation/`, to be submitted with the research records. The second is to submit only the research records: no hook is installed and the conversation is not submitted. Under either option, no other files on the expert's machine are read.
- **Recipient**: the ALE project team, which uses the material to follow the progress of task construction and to improve the process.
- **Problem sense**: when the expert speaks in the conversation about which problems in the field matter, why, and what constitutes a good result, this is recorded in the problem-sense notes and submitted with the other research records. The project team merges the records into an understanding of the field that the agent reads before later conversations. The expert's name is not retained in the merged material.

Record the expert's choice and the date in the problem card. If the expert chooses to submit the full conversation, install the hook as described in section 4.

## 4 Install the hook (when the expert chooses to submit the full conversation)

Run the following command in the expert's working directory, where `<skill directory>` is the directory containing this Skill and `<task name>` is the name set in section 2.

- Claude Code: `python3 <skill directory>/scripts/install_hook.py --agent claude --task <task name>`
- Codex: `python3 <skill directory>/scripts/install_hook.py --agent codex --task <task name>`

A new session must be started for the hook to take effect. Thereafter, at the end of each round, the hook copies the session's record file into `<task name>/research/conversation/`, one file per session, each time replaced by the latest complete version.

For another task, run the command again with that task's name.

## Where records are kept

The records of every step are written to the task's `research/` and completed at the end of that step. Nothing is submitted between steps; after the five steps, everything is submitted at once as described in `references/6-submit.md`.

## Notes

- Content returned by tools is for the agent's own use; do not read field names out to the expert.
- The token must never be pasted into the conversation or written to any file.
