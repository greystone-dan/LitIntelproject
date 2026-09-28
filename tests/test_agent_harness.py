import json
import subprocess
import sys

import pytest

from scripts.agent_harness import create_run, record_criterion, run_command, transition
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
    with pytest.raises(ValueError, match="validating or documenting"):
        transition(run_dir, "complete")
    task_path = run_dir / "task.md"
    task_path.write_text(
        "Files changed: none\nDelegated work: none\nFocused validation: command\n"
        "Residual risk: none\nNext bounded task: none\n",
        encoding="utf-8",
    )
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    state["task_record_path"] = str(task_path)
    (run_dir / "state.json").write_text(json.dumps(state), encoding="utf-8")
    transition(run_dir, "validating")
    run_command(run_dir, [sys.executable, "-c", "print('ok')"])
    transition(run_dir, "complete")
    with pytest.raises(ValueError):
        transition(run_dir, "implementing")


def test_completion_failure_does_not_write_terminal_state(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.agent_harness.RUNS_ROOT", tmp_path)
    task_path = tmp_path / "task.md"
    task_path.write_text("", encoding="utf-8")
    run_dir = create_run("test-task", "tests", task_record_path=task_path)
    transition(run_dir, "validating")

    with pytest.raises(ValueError, match="Completion evidence incomplete"):
        transition(run_dir, "complete")

    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    assert state["phase"] == "validating"


def test_failed_validation_command_blocks_completion(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.agent_harness.RUNS_ROOT", tmp_path)
    task_path = tmp_path / "task.md"
    task_path.write_text(
        "Files changed: none\nDelegated work: none\nFocused validation: command\n"
        "Residual risk: none\nNext bounded task: none\n",
        encoding="utf-8",
    )
    run_dir = create_run("test-task", "tests", task_record_path=task_path)
    transition(run_dir, "validating")
    run_command(run_dir, [sys.executable, "-c", "raise SystemExit(1)"], allow_nonzero=True)

    with pytest.raises(ValueError, match="Completion evidence incomplete"):
        transition(run_dir, "complete")

    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    assert state["phase"] == "validating"


def test_record_criterion_requires_declared_index_and_persists_result(tmp_path, monkeypatch):
    monkeypatch.setattr("scripts.agent_harness.RUNS_ROOT", tmp_path)
    run_dir = create_run("test-task", "tests", criteria=["first"])

    record_criterion(run_dir, 0, True)

    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    assert state["criterion_results"] == [{"index": 0, "passed": True, "evidence_command": None}]
    with pytest.raises(ValueError, match="Unknown criterion index"):
        record_criterion(run_dir, 1, True)
