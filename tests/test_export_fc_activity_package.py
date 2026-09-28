import json
from datetime import date, datetime, timezone
from types import SimpleNamespace

from scripts.export_fc_activity_package import (
    CohortOptions,
    EXPORT_VERSION,
    _case_record,
    _classification_record,
    _document_record,
    _manifest,
    _case_matches,
    _sample_key,
)


def test_layer_records_preserve_source_links_and_raw_evidence():
    case = SimpleNamespace(
        id=12,
        source_key="case-key",
        citation="IMM-12-26",
        year=2026,
        case_name="Example v Canada",
        date_filed=date(2026, 1, 2),
        city_filed="Toronto",
        nature="JR",
        case_class="IMM",
        track="A",
        source_url="https://example.test/activity",
        scraped_timestamp=datetime(2026, 1, 3, tzinfo=timezone.utc),
        raw_payload={"imm_number": "IMM-12-26", "entries_json": []},
    )
    document = SimpleNamespace(
        id=34,
        case_id=12,
        re_no="1",
        docno="2",
        doc_dt=date(2026, 1, 2),
        recorded_entry="Application filed",
        entry_hash="hash",
        raw_document={"source": "portal"},
    )
    classification = SimpleNamespace(
        id=56,
        source_case_id=12,
        source_key="case-key",
        imm_number="IMM-12-26",
        year=2026,
        case_name="Example v Canada",
        date_filed=date(2026, 1, 2),
        city_filed="Toronto",
        nature="JR",
        case_class="IMM",
        track="A",
        source_url="https://example.test/activity",
        scraped_timestamp=datetime(2026, 1, 3, tzinfo=timezone.utc),
        classifier_version="fc_activity_v3",
        classified_at=datetime(2026, 1, 4, tzinfo=timezone.utc),
        updated_at=datetime(2026, 1, 4, tzinfo=timezone.utc),
        classification_json={"application_filed": {"status": "yes", "doc_id": 34}},
    )

    case_record = _case_record(case)
    document_record = _document_record(document)
    classification_record = _classification_record(classification)

    assert case_record["raw_payload"]["entries_json"] == []
    assert document_record["activity_case_id"] == case_record["activity_case_id"]
    assert document_record["raw_document"]["source"] == "portal"
    assert classification_record["activity_case_id"] == case_record["activity_case_id"]
    assert classification_record["classification"]["application_filed"]["doc_id"] == document.id


def test_manifest_declares_layers_and_selection():
    options = CohortOptions(cohort_name="fixture", limit=3, sample_seed=7)
    manifest = _manifest(
        counts={"cases": 3, "documents": 2, "classifications": 1},
        classifier_versions=["fc_activity_v3"],
        options=options,
        total_matching=4,
    )

    json.dumps(manifest, ensure_ascii=False)
    assert manifest["export_version"] == EXPORT_VERSION
    assert manifest["selection"]["case_limit"] == 3
    assert manifest["cohort_name"] == "fixture"
    assert manifest["total_matching_cases_before_sampling"] == 4
    assert manifest["counts"]["documents"] == 2
    assert "raw_payload" in manifest["files"]["cases.jsonl"]
    assert manifest["relationships"]["documents.activity_case_id"] == "cases.activity_case_id"
    assert "BOM" in " ".join(manifest["known_limitations"])


def test_same_seed_produces_same_order():
    source_keys = ["case-a", "case-b", "case-c"]
    first = sorted(source_keys, key=lambda key: _sample_key(key, 20260926))
    second = sorted(source_keys, key=lambda key: _sample_key(key, 20260926))
    assert first == second
    assert _sample_key("case-a", 20260926) != _sample_key("case-a", 20260927)


def _fixture_rows():
    case = {"citation": "IMM-7-24", "year": 2024, "raw_payload": {"imm_number": "IMM-7-24"}}
    documents = [
        {"recorded_entry": "Notice of Motion: stay of removal", "docno": "1"},
        {"recorded_entry": "Result of Hearing; application for leave granted", "docno": "2"},
    ]
    classifications = [{
        "classification": {
            "stay_decision": {"status": "yes"},
            "judicial_review_result": {"result": "allowed"},
        }
    }]
    return case, documents, classifications


def test_each_cohort_filter_matches_fixture():
    case, documents, classifications = _fixture_rows()
    options = [
        CohortOptions(year_from=2024, year_to=2024),
        CohortOptions(classification_filters=(("stay_decision.status", ("yes",)),)),
        CohortOptions(entry_regexes=("stay of removal",)),
        CohortOptions(entry_regex_exclude="withdrawn", entry_regexes=("stay",)),
        CohortOptions(min_entries_matching=("Notice of Motion", 1)),
    ]
    for option in options:
        assert _case_matches(case, documents, classifications, option)

    assert _case_matches(case, documents, classifications, CohortOptions(no_classification=False))
    assert not _case_matches(case, [], classifications, CohortOptions(no_classification=True))
    assert _case_matches(case, documents, [], CohortOptions(no_classification=True))
    bom_case = {**case, "citation": "\ufeffIMM-7-24"}
    assert _case_matches(bom_case, documents, classifications, CohortOptions(bom=True))
    assert _case_matches(case, documents, classifications, CohortOptions(duplicate_court_file=True), {"IMM-7-24"})
    assert not _case_matches(case, documents, classifications, CohortOptions(year_from=2025))


def test_empty_history_filter_matches_only_empty_documents():
    case, _, classifications = _fixture_rows()
    assert _case_matches(case, [], classifications, CohortOptions(empty_history=True))
    assert not _case_matches(case, [{"recorded_entry": "entry"}], classifications, CohortOptions(empty_history=True))
