# ALE skills

Agent skills for people working on [Agents' Last Exam](https://github.com/AgentsLastExam/orbit).
Each folder under `skills/` is one skill: a `SKILL.md` with instructions an AI coding agent
(Claude Code, Codex and others that read `SKILL.md`) follows, plus any scripts it uses. They are
also plain documentation for people.

| Skill | Use it to |
|---|---|
| [`ale-contribute`](skills/ale-contribute/SKILL.md) | submit a Task to your domain's repository with its material on Hugging Face, and upload the run records (trajectories) `ale run` produces |

## Install

Copy or link a skill folder where your agent looks for skills, for example:

```bash
git clone https://github.com/AgentsLastExam/ale-skills
mkdir -p ~/.claude/skills && ln -s "$PWD/ale-skills/skills/ale-contribute" ~/.claude/skills/ale-contribute
```

For a single project, use `<project>/.claude/skills/` (Claude Code) or `<project>/.agents/skills/`.
Pull this repository to update.
