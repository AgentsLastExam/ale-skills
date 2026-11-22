#!/usr/bin/env python3
"""Installs the hook for an expert who has chosen to submit the full conversation.
Run in the expert's working directory:

    python3 <skill directory>/scripts/install_hook.py --agent claude --task <task name>
    python3 <skill directory>/scripts/install_hook.py --agent codex --task <task name>

Once installed, at the end of each round of conversation the hook runs save_conversation.py,
which copies the session's record file into <task name>/research/conversation/.
A new session must be started for the hook to take effect.

- Claude Code: adds Stop and SessionEnd hooks to .claude/settings.local.json in the working directory.
- Codex: adds a Stop hook to .codex/hooks.json in the working directory, and enables
  codex_hooks under [features] in ~/.codex/config.toml.
Running it again replaces the previously installed hook rather than adding a duplicate. Other
hooks and settings remain unchanged.
"""
import argparse
import json
import pathlib
import re
import shlex
import sys

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = HERE / "save_conversation.py"


def hook_command(agent, task_dir):
    parts = [sys.executable or "python3", str(SCRIPT), agent, str(task_dir)]
    return " ".join(shlex.quote(p) for p in parts)


def add_hooks(config_path, events, command):
    text = config_path.read_text() if config_path.exists() else ""
    config = json.loads(text) if text.strip() else {}
    hooks = config.setdefault("hooks", {})
    for event in events:
        groups = hooks.setdefault(event, [])
        for group in groups:
            group["hooks"] = [h for h in group.get("hooks", [])
                              if "save_conversation.py" not in h.get("command", "")]
        groups[:] = [g for g in groups if g.get("hooks")]
        groups.append({"hooks": [{"type": "command", "command": command, "timeout": 30}]})
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n")


def enable_codex_hooks():
    path = pathlib.Path.home() / ".codex" / "config.toml"
    lines = path.read_text().splitlines() if path.exists() else []
    for i, line in enumerate(lines):
        if re.match(r"\s*codex_hooks\s*=", line):
            lines[i] = "codex_hooks = true"
            break
    else:
        stripped = [l.strip() for l in lines]
        if "[features]" in stripped:
            lines.insert(stripped.index("[features]") + 1, "codex_hooks = true")
        else:
            lines += ["", "[features]", "codex_hooks = true"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")
    return path


def main():
    parser = argparse.ArgumentParser(description="Install the hook that saves the session record into the task's research/conversation/ every round")
    parser.add_argument("--agent", choices=["claude", "codex"], required=True)
    parser.add_argument("--task", required=True, help="task name, which is also the task folder name")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9_]+", args.task):
        sys.exit("The task name may contain only lowercase letters, digits and underscores")
    workdir = pathlib.Path.cwd()
    task_dir = workdir / args.task
    (task_dir / "research" / "conversation").mkdir(parents=True, exist_ok=True)
    command = hook_command(args.agent, task_dir)

    if args.agent == "claude":
        config = workdir / ".claude" / "settings.local.json"
        add_hooks(config, ["Stop", "SessionEnd"], command)
        print(f"Wrote {config}")
    else:
        config = workdir / ".codex" / "hooks.json"
        add_hooks(config, ["Stop"], command)
        print(f"Wrote {config}")
        print(f"Enabled codex_hooks in {enable_codex_hooks()}")
    print(f"Session records will be saved to {task_dir / 'research' / 'conversation'}")
    print("Start a new session for it to take effect.")


if __name__ == "__main__":
    main()
