"""Bounded ProjectManagerGAME harness for the browser_game folder."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from game_policy import GAME_ROOT, confined_path, validate_command

RUNS_ROOT = GAME_ROOT / ".game-manager" / "runs"
TERMINAL_PHASES = {"complete", "blocked", "deferred", "failed_policy"}
PHASES = {
    "planned",
    "researching",
    "implementing",
    "validating",
    "repairing",
    "documenting",
    "complete",
    "blocked",
    "deferred",
    "failed_policy",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    confined_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def append_event(run_dir: Path, event: dict[str, Any]) -> None:
    run_dir = confined_path(run_dir)
    event = {"event_id": str(uuid.uuid4()), "at": now(), **event}
    with (run_dir / "events.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def create_run(task_id: str, owner_surface: str, repair_budget: int = 2) -> Path:
    if not task_id or not owner_surface:
        raise ValueError("task_id and owner_surface are required")
    run_id = f"{task_id}-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"
    run_dir = confined_path(RUNS_ROOT / run_id)
    state = {
        "schema_version": 1,
        "project": "ProjectManagerGAME",
        "task_id": task_id,
        "run_id": run_id,
        "owner_surface": owner_surface,
        "phase": "planned",
        "repair_budget": repair_budget,
        "repair_attempt": 0,
        "commands": [],
        "evidence": [],
        "created_at": now(),
        "updated_at": now(),
    }
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "run_created", "phase": "planned"})
    return run_dir


def load_state(run_dir: Path) -> dict[str, Any]:
    run_dir = confined_path(run_dir)
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    if state.get("phase") not in PHASES:
        raise ValueError(f"unknown phase: {state.get('phase')}")
    return state


def transition(run_dir: Path, phase: str, note: str = "") -> dict[str, Any]:
    if phase not in PHASES:
        raise ValueError(f"unknown phase: {phase}")
    state = load_state(run_dir)
    if state["phase"] in TERMINAL_PHASES and phase != state["phase"]:
        raise ValueError("terminal run cannot transition")
    state["phase"] = phase
    state["updated_at"] = now()
    atomic_write(confined_path(run_dir) / "state.json", state)
    append_event(confined_path(run_dir), {"type": "phase_transition", "phase": phase, "note": note})
    return state


def run_command(run_dir: Path, command: list[str], timeout: int = 120) -> dict[str, Any]:
    run_dir = confined_path(run_dir)
    state = load_state(run_dir)
    if state["phase"] not in {"implementing", "validating", "repairing", "documenting"}:
        raise ValueError("commands require an active implementation or validation phase")
    validate_command(command, GAME_ROOT)
    result = subprocess.run(
        command,
        cwd=GAME_ROOT,
        capture_output=True,
        text=True,
        timeout=min(max(timeout, 1), 120),
        check=False,
        shell=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    log_path = run_dir / "commands" / f"command-{len(state['commands']) + 1}.log"
    confined_path(log_path).parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(output, encoding="utf-8")
    evidence = {
        "command": command,
        "cwd": str(GAME_ROOT),
        "exit_code": result.returncode,
        "output_log": str(log_path),
        "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "ran_at": now(),
    }
    state["commands"].append(evidence)
    state["evidence"].append({"type": "command", **evidence})
    state["updated_at"] = now()
    atomic_write(run_dir / "state.json", state)
    append_event(run_dir, {"type": "command_finished", **evidence})
    if result.returncode:
        raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)
    return evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    create = subparsers.add_parser("create")
    create.add_argument("task_id")
    create.add_argument("owner_surface")
    transition_parser = subparsers.add_parser("transition")
    transition_parser.add_argument("run_dir", type=Path)
    transition_parser.add_argument("phase", choices=sorted(PHASES))
    transition_parser.add_argument("--note", default="")
    command = subparsers.add_parser("command")
    command.add_argument("run_dir", type=Path)
    command.add_argument("--timeout", type=int, default=120)
    command.add_argument("command", nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.action == "create":
        print(create_run(args.task_id, args.owner_surface))
    elif args.action == "transition":
        print(json.dumps(transition(args.run_dir, args.phase, args.note), indent=2))
    else:
        command = args.command[1:] if args.command[:1] == ["--"] else args.command
        print(json.dumps(run_command(args.run_dir, command, args.timeout), indent=2))


if __name__ == "__main__":
    main()
