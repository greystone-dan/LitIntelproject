import json
import subprocess
import sys

import pytest

from scripts.agent_harness import create_run, run_command, transition
from scripts.agent_policy import decision


def test_harness_creates_atomic_state_and_event_log(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.agent_harness.RUNS_ROOT", tmp_path)
    run_dir = create_run("test-task", "tests/test_*.py")
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    events = (run_dir / "events.jsonl").read_text(encoding="utf-8").splitlines()

    assert state["phase"] == "planned"
    assert state["lease_seconds"] == 1200
    assert len(events) == 1


def test_harness_records_command_evidence(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.agent_harness.RUNS_ROOT", tmp_path)
    run_dir = create_run("test-task", "tests/test_*.py")
    transition(run_dir, "implementing")
    transition(run_dir, "validating")
    evidence = run_command(run_dir, [sys.executable, "-c", "print('ok')"])

    assert evidence["exit_code"] == 0
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    assert len(state["commands"]) == 1
    assert (run_dir / "commands" / "command-1.log").read_text(encoding="utf-8").strip() == "ok"


def test_policy_denies_worker_manager_state_edits():
    result = decision(actor="worker", operation="write", paths=[".github/project-manager/tasks/x.md"])
    assert result["decision"] == "deny"


def test_policy_requires_approval_for_git_push():
    result = decision(actor="manager", operation="execute", paths=[], command="git push origin main")
    assert result["decision"] == "ask"


def test_terminal_run_cannot_transition():
    run_dir = create_run("test-task", "tests/test_*.py")
    transition(run_dir, "complete")
    with pytest.raises(ValueError):
        transition(run_dir, "implementing")
