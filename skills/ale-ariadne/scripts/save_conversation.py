#!/usr/bin/env python3
"""Called by the hook at the end of each round of conversation: copies the session's
record file into the task's research/conversation/.

Not to be run manually. install_hook.py writes the following command into the hook settings:
    python3 save_conversation.py <claude|codex> <task directory>
The hook passes a JSON object on standard input, whose transcript_path is the
session's record file. On any error the script exits without interrupting the agent.
"""
import json
import pathlib
import re
import shutil
import sys


def main():
    if len(sys.argv) != 3:
        return
    agent, task_dir = sys.argv[1], pathlib.Path(sys.argv[2])
    data = json.load(sys.stdin)
    src = data.get("transcript_path")
    if not src:
        return
    src = pathlib.Path(src).expanduser()
    if not src.is_file():
        return
    session = re.sub(r"[^A-Za-z0-9_-]", "_", str(data.get("session_id") or src.stem))
    out = task_dir / "research" / "conversation"
    out.mkdir(parents=True, exist_ok=True)
    # Copy the complete record file each time, replacing the previous copy, so that the
    # file always contains the full conversation up to the current round
    shutil.copyfile(src, out / f"{agent}-{session}{src.suffix or '.jsonl'}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
