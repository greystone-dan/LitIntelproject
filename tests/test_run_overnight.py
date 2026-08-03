import json
from pathlib import Path

import pytest

from scripts import run_overnight


def test_safe_profile_uses_resumable_fc_pullers_and_no_canlii_or_paid_jobs():
    selected = run_overnight.selected_job_names("safe", None)

    assert selected[:3] == ["fc_decisions", "fc_portal", "fc_history"]
    assert selected.index("chunk_cases") < selected.index("citations")
    assert selected.index("chunk_cases") < selected.index("local_embeddings")
    assert "local_embeddings" in selected
    assert all("canlii" not in name for name in selected)
    assert all("openai" not in name for name in selected)


def test_backend_jobs_use_module_mode_for_import_safety():
    assert run_overnight.JOBS["citations"].arguments[:2] == (
        "-m",
        "scripts.extract_citation_network",
    )
    assert run_overnight.JOBS["local_embeddings"].arguments[:2] == (
        "-m",
        "scripts.embed_local_chunks",
    )


def test_run_lock_rejects_active_owner(tmp_path, monkeypatch):
    lock_path = tmp_path / "overnight.lock"
    lock_path.write_text(json.dumps({"pid": 123, "created_at": "now"}), encoding="utf-8")
    monkeypatch.setattr(run_overnight, "process_is_running", lambda pid: pid == 123)

    with pytest.raises(RuntimeError, match="Another overnight run"):
        with run_overnight.RunLock(lock_path):
            pass


def test_run_lock_replaces_stale_owner_and_cleans_up(tmp_path, monkeypatch):
    lock_path = tmp_path / "overnight.lock"
    lock_path.write_text(json.dumps({"pid": 123}), encoding="utf-8")
    monkeypatch.setattr(run_overnight, "process_is_running", lambda pid: False)

    with run_overnight.RunLock(lock_path):
        assert lock_path.exists()

    assert not lock_path.exists()


def test_execute_jobs_skips_completed_and_records_failure(tmp_path):
    state = run_overnight.create_state(
        "test-run", ["reference_verify", "tag_cases"], continue_on_error=True
    )
    state["jobs"]["reference_verify"]["status"] = "completed"
    calls: list[str] = []

    def fail_tagger(job, command, log_path):
        calls.append(job.name)
        assert Path(command[0]).name in {"python", "python.exe"}
        assert log_path.name == "tag_cases.log"
        return 7

    exit_code = run_overnight.execute_jobs(
        state,
        tmp_path,
        Path("python.exe"),
        runner=fail_tagger,
    )

    saved = json.loads((tmp_path / run_overnight.STATE_FILENAME).read_text(encoding="utf-8"))
    assert exit_code == 1
    assert calls == ["tag_cases"]
    assert saved["status"] == "completed_with_failures"
    assert saved["jobs"]["reference_verify"]["attempts"] == 0
    assert saved["jobs"]["tag_cases"]["status"] == "failed"
    assert saved["jobs"]["tag_cases"]["exit_code"] == 7


def test_load_state_marks_interrupted_job_for_retry(tmp_path):
    state = run_overnight.create_state("test-run", ["fc_portal"], False)
    state["jobs"]["fc_portal"]["status"] = "running"
    run_overnight.atomic_write_json(tmp_path / run_overnight.STATE_FILENAME, state)

    loaded = run_overnight.load_state(tmp_path)

    assert loaded["jobs"]["fc_portal"]["status"] == "interrupted"