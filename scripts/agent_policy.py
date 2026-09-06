"""Fail-closed policy checks for managed-task command requests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PROTECTED_PATHS = (
    ".github/project-manager/runs",
    ".github/project-manager/tasks",
    ".github/hooks",
    "scripts/agent_harness.py",
    "scripts/agent_policy.py",
)
DENIED_COMMANDS = {"git reset", "git clean", "git push", "git commit"}


def decision(*, actor: str, operation: str, paths: list[str], command: str = "") -> dict[str, object]:
    normalized = command.strip().lower()
    if actor == "worker" and operation in {"write", "edit", "delete"}:
        if any(path.replace("\\", "/").startswith(PROTECTED_PATHS) for path in paths):
            return {"decision": "deny", "reason": "worker-cannot-edit-manager-state"}
    if any(normalized.startswith(prefix) for prefix in DENIED_COMMANDS):
        return {"decision": "ask", "reason": "privileged-or-destructive-command"}
    return {"decision": "allow", "reason": "within-default-policy"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actor", choices=("manager", "worker"), required=True)
    parser.add_argument("--operation", choices=("read", "write", "edit", "delete", "execute"), required=True)
    parser.add_argument("--path", action="append", default=[])
    parser.add_argument("--command", default="")
    args = parser.parse_args()
    print(json.dumps(decision(actor=args.actor, operation=args.operation, paths=args.path, command=args.command)))


if __name__ == "__main__":
    main()
