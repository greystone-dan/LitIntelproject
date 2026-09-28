import json

from scripts.evidence_gate import validate_state


def complete_state():
    return {
        "task_id": "test",
        "run_id": "run",
        "phase": "complete",
        "owner_surface": "tests",
        "heartbeat_at": "now",
        "commands": [{"exit_code": 0}],
        "evidence": [{"type": "command"}],
        "phase_before_complete": "validating",
    }


def test_evidence_gate_accepts_complete_state_with_document_paths():
    failures = validate_state(
        complete_state(),
        task_text=(
            "Canonical: SYSTEM_REFERENCE.md\nSwimm: .swm/system-map.ovnldklv.sw.md\n"
            "Files changed: scripts/x.py\nDelegated work: none\n"
            "Focused validation: pytest\nResidual risk: none\nNext bounded task: none"
        ),
        required_docs=["SYSTEM_REFERENCE.md", ".swm/system-map.ovnldklv.sw.md"],
    )
    assert failures == []


def test_evidence_gate_rejects_incomplete_state():
    failures = validate_state({}, task_text="", required_docs=["SYSTEM_REFERENCE.md"])
    assert "phase-not-complete:None" in failures
    assert "missing-documentation-path:SYSTEM_REFERENCE.md" in failures


def test_evidence_gate_rejects_completion_without_structured_evidence():
    state = complete_state()
    state["phase_before_complete"] = "planned"
    failures = validate_state(state, task_text="", required_docs=[])

    assert "completion-not-after-validation-or-documentation" in failures
    assert "missing-completion-evidence:Files changed" in failures
    assert "missing-completion-evidence:Next bounded task" in failures


def test_evidence_gate_requires_every_declared_criterion_to_pass():
    state = complete_state()
    state["criteria"] = ["first", "second"]
    state["criterion_results"] = [{"index": 0, "passed": True, "evidence_command": 1}]

    failures = validate_state(state, task_text="", required_docs=[])

    assert "criterion-results-count-mismatch" in failures
