import json

from scripts.run_v2_pipeline import STAGES, run


def test_v2_pipeline_dry_run_records_all_stages_without_writes(tmp_path):
    state = run(limit=1, case_ids=None, batch_size=1, timeout=1, retries=1, stage_timeout=1, run_dir=tmp_path, dry_run=True)

    assert state["status"] == "dry_run"
    assert tuple(state["selected_stages"]) == STAGES
    assert len(state["cases"]) == 1
    case_state = next(iter(state["cases"].values()))
    assert set(case_state["stages"]) == set(STAGES)
    assert all(value == "planned" for value in case_state["stages"].values())
    assert json.loads((tmp_path / "state.json").read_text(encoding="utf-8"))["status"] == "dry_run"


def test_pipeline_uses_internal_case_citation_stage_name():
    from scripts.run_v2_pipeline import PROCESSING_STAGE_NAMES

    assert PROCESSING_STAGE_NAMES["citations"] == "case_citations"


def test_large_mapping_threshold_is_bounded():
    from backend.document_structure import LARGE_MAPPING_THRESHOLD

    assert LARGE_MAPPING_THRESHOLD <= 150_000
