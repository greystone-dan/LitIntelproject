"""Validate manager-owned completion evidence for a task run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_STATE_KEYS = {
    "task_id",
    "run_id",
    "phase",
    "owner_surface",
    "heartbeat_at",
    "commands",
    "evidence",
}


def validate_state(state: dict, *, task_text: str, required_docs: list[str]) -> list[str]:
    failures: list[str] = []
    failures.extend(f"missing-state:{key}" for key in sorted(REQUIRED_STATE_KEYS - state.keys()))
    if state.get("phase") != "complete":
        failures.append(f"phase-not-complete:{state.get('phase')}")
    if not state.get("commands"):
        failures.append("no-command-evidence")
    if not state.get("evidence"):
        failures.append("no-evidence")
    for path in required_docs:
        if path not in task_text:
            failures.append(f"missing-documentation-path:{path}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", type=Path)
    parser.add_argument("task", type=Path)
    parser.add_argument("--doc", action="append", default=[])
    args = parser.parse_args()
    state = json.loads(args.state.read_text(encoding="utf-8"))
    task_text = args.task.read_text(encoding="utf-8")
    failures = validate_state(state, task_text=task_text, required_docs=args.doc)
    if failures:
        print(json.dumps({"ok": False, "failures": failures}, indent=2))
        return 1
    print(json.dumps({"ok": True, "run_id": state["run_id"], "commands": len(state["commands"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
