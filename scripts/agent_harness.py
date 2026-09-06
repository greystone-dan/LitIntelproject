"""Small repo-local control plane for managed agent task runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUNS_ROOT = ROOT / ".github" / "project-manager" / "runs"
TERMINAL_STATES = {"complete", "blocked", "deferred", "failed_policy", "paused_recoverable"}
VALID_PHASES = {
    "planned",
    "researching",
    "delegated",
    "implementing",
    "validating",
    "repairing",
    "documenting",
    "complete",
    "blocked",
    "deferred",
    "failed_policy",
    "paused_recoverable",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def append_event(run_dir: Path, event: dict[str, Any]) -> None:
    event = {"event_id": str(uuid.uuid4()), "at": now(), **event}
    with (run_dir / "events.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def command_evidence(command: list[str], cwd: Path, result: subprocess.CompletedProcess[str], log_path: Path) -> dict[str, Any]:
    output = (result.stdout or "") + (result.stderr or "")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(output, encoding="utf-8")
    return {
        "command": command,
        "cwd": str(cwd),
        "exit_code": result.returncode,
        "output_log": str(log_path),
        "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "ran_at": now(),
    }


def create_run(task_id: str, owner_surface: str, *, lease_seconds: int = 1200, repair_budget: int = 3) -> Path:
    run_id = f"{task_id}-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_ROOT / run_id
    state = {
        "schema_version": 1,
        "task_id": task_id,
        "run_id": run_id,
        "owner_surface": owner_surface,
        "phase": "planned",
        "status": "planned",
        "lease_seconds": lease_seconds,
        "lease_deadline": None,
        "heartbeat_at": now(),
        "repair_budget": repair_budget,
        "repair_attempt": 0,
        "criteria": [],
        "evidence": [],
        "commands": [],
        "created_at": now(),
        "updated_at": now(),
    }
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "run_created", "phase": "planned"})
    return run_dir


def load_state(run_dir: Path) -> dict[str, Any]:
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    if state.get("phase") not in VALID_PHASES:
        raise ValueError(f"Unknown phase: {state.get('phase')}")
    return state


def transition(run_dir: Path, phase: str, *, note: str = "") -> dict[str, Any]:
    if phase not in VALID_PHASES:
        raise ValueError(f"Unknown phase: {phase}")
    state = load_state(run_dir)
    if state.get("phase") in TERMINAL_STATES and phase != state["phase"]:
        raise ValueError("Terminal run cannot transition without an explicit new run")
    state["phase"] = phase
    state["status"] = phase
    state["heartbeat_at"] = now()
    state["updated_at"] = now()
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "phase_transition", "phase": phase, "note": note})
    return state


def heartbeat(run_dir: Path) -> dict[str, Any]:
    state = load_state(run_dir)
    state["heartbeat_at"] = now()
    state["updated_at"] = now()
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "heartbeat", "phase": state["phase"]})
    return state


def run_command(run_dir: Path, command: list[str], *, timeout: int | None = None, allow_nonzero: bool = False) -> dict[str, Any]:
    state = load_state(run_dir)
    if state["phase"] not in {"implementing", "validating", "repairing", "documenting"}:
        raise ValueError("Commands require an implementing, validating, repairing, or documenting phase")
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=timeout, check=False)
    log_path = run_dir / "commands" / f"command-{len(state['commands']) + 1}.log"
    evidence = command_evidence(command, ROOT, result, log_path)
    state["commands"].append(evidence)
    state["evidence"].append({"type": "command", **evidence})
    state["updated_at"] = now()
    state["heartbeat_at"] = now()
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "command_finished", **evidence})
    if result.returncode and not allow_nonzero:
        raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)
    return evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    create = subparsers.add_parser("create")
    create.add_argument("task_id")
    create.add_argument("owner_surface")
    create.add_argument("--lease-seconds", type=int, default=1200)
    create.add_argument("--repair-budget", type=int, default=3)
    transition_parser = subparsers.add_parser("transition")
    transition_parser.add_argument("run_dir", type=Path)
    transition_parser.add_argument("phase", choices=sorted(VALID_PHASES))
    transition_parser.add_argument("--note", default="")
    heartbeat_parser = subparsers.add_parser("heartbeat")
    heartbeat_parser.add_argument("run_dir", type=Path)
    command = subparsers.add_parser("command")
    command.add_argument("run_dir", type=Path)
    command.add_argument("--timeout", type=int)
    command.add_argument("command", nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.action == "create":
        print(create_run(args.task_id, args.owner_surface, lease_seconds=args.lease_seconds, repair_budget=args.repair_budget))
    elif args.action == "transition":
        print(json.dumps(transition(args.run_dir, args.phase, note=args.note), indent=2))
    elif args.action == "heartbeat":
        print(json.dumps(heartbeat(args.run_dir), indent=2))
    elif args.action == "command":
        command = args.command[1:] if args.command[:1] == ["--"] else args.command
        print(json.dumps(run_command(args.run_dir, command, timeout=args.timeout), indent=2))


if __name__ == "__main__":
    main()
