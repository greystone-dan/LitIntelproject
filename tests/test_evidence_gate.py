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
    }


def test_evidence_gate_accepts_complete_state_with_document_paths():
    failures = validate_state(
        complete_state(),
        task_text="Canonical: SYSTEM_REFERENCE.md\nSwimm: .swm/system-map.ovnldklv.sw.md",
        required_docs=["SYSTEM_REFERENCE.md", ".swm/system-map.ovnldklv.sw.md"],
    )
    assert failures == []


def test_evidence_gate_rejects_incomplete_state():
    failures = validate_state({}, task_text="", required_docs=["SYSTEM_REFERENCE.md"])
    assert "phase-not-complete:None" in failures
    assert "missing-documentation-path:SYSTEM_REFERENCE.md" in failures
