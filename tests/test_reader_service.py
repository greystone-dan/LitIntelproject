from copy import deepcopy
from datetime import date
import json
from types import SimpleNamespace

import pytest

from backend import reader_service
from backend.case_formatter import format_decision
from backend.metadata import extract_case_metadata
from backend.reader_service import _build_reader_outcome_metadata, _build_reader_extracted_summary


def summary_case(text, **overrides):
    return SimpleNamespace(
        **(dict(full_text=text, court="Federal Court", date=date(2025, 1, 2),
                metadata_json={}) | overrides)
    )


def source_tag(text, excerpt, value, score=1, **overrides):
    start = text.index(excerpt)
    return SimpleNamespace(**(dict(
        category="issue", value=value, score=score, source="stored_tag",
        evidence=excerpt, offset_start=start, offset_end=start + len(excerpt),
    ) | overrides))


@pytest.mark.parametrize("has_outcome", [True, False])
def test_summary_each_item_has_exact_stored_source_and_formatter_identity(has_outcome):
    text = ("Federal Court\nDate: 20250102\nJudge: Justice Smith\nDecision Content\n"
            "[1] Refugee evidence.\n[2] The application is dismissed.")
    case = summary_case(text)
    blocks = format_decision(text)
    before = deepcopy((vars(case), blocks))
    judge = reader_service.CaseReaderMetadataFieldResponse(
        key="judge", value="Justice Smith", source="reader_extracted", evidence="Justice Smith",
    )
    tags = [source_tag(text, "Refugee evidence", "refugee")]
    outcome = stored_outcome(text, "application is dismissed") if has_outcome else None
    rows = _build_reader_extracted_summary(case, outcome, blocks, tags, [judge])
    by_key = {row.key: row for row in rows}
    assert set(by_key) == (
        {"court", "date", "judge", "tag:issue"} |
        ({"outcome", "outcome_source", "disposition"} if has_outcome else set())
    )
    assert by_key["date"].value == "20250102"  # verbatim header, not reformatted prose
    for row in rows:
        assert text[row.start:row.end] == row.evidence
        block = next(block for block in blocks if block["start"] == row.block_start)
        assert block["type"] == row.block_type
        assert row.paragraph_number == (block["num"] if block["type"] == "para" else None)
        assert block["start"] <= row.start < row.end <= block["end"]
    assert by_key["tag:issue"].paragraph_number == 1
    if has_outcome:
        assert by_key["outcome"].paragraph_number == 2
        assert by_key["outcome"].block_start == by_key["outcome_source"].block_start
        assert by_key["outcome"].evidence == by_key["outcome_source"].evidence
        assert by_key["disposition"].value == "[2] The application is dismissed."
    assert (vars(case), blocks) == before


def test_summary_only_top_three_distinct_verified_tags_are_selected():
    text = "[1] First. Second. Third. Fourth."
    tags = [
        source_tag(text, "Fourth", "fourth", 0.1),
        source_tag(text, "First", "first", 0.9),
        source_tag(text, "First", "first", 0.8),
        source_tag(text, "Second", "second", 0.7),
        source_tag(text, "Third", "third", 0.6),
        source_tag(text, "First", "unverified", 1, evidence="stale excerpt"),
    ]
    rows = _build_reader_extracted_summary(summary_case(text), None, format_decision(text), tags, [])
    assert [row.value for row in rows] == ["first", "second", "third"]


@pytest.mark.parametrize("overrides", [
    {"disposition_evidence": None}, {"evidence_offset_start": None},
    {"evidence_offset_start": -1}, {"evidence_offset_end": 999},
    {"disposition_evidence": "invented evidence"},
])
def test_summary_unverified_outcome_and_source_are_both_omitted(overrides):
    text = "[1] The application is dismissed."
    rows = _build_reader_extracted_summary(
        summary_case(text), stored_outcome(text, "application is dismissed", **overrides),
        format_decision(text), [], [],
    )
    assert rows == []


def test_summary_never_uses_body_mentions_as_header_facts_or_relocates_stale_evidence():
    text = ("Decision Content\n[1] Federal Court\n"
            "Date: 20250102\nJudge: Justice Smith\n[2] Refugee evidence.\n"
            "[3] Refugee evidence.")
    judge = reader_service.CaseReaderMetadataFieldResponse(
        key="judge", value="Justice Smith", source="reader_extracted", evidence="Justice Smith",
    )
    tag = source_tag(text, "Refugee evidence", "refugee", offset_start=0, offset_end=16)
    assert _build_reader_extracted_summary(
        summary_case(text), None, format_decision(text), [tag], [judge],
    ) == []


def test_summary_unnumbered_or_cross_paragraph_outcome_evidence_is_omitted():
    for text, evidence in [
        ("Application dismissed\nDecision Content\n[1] Background.", "Application dismissed"),
        ("[1] The application\n[2] is dismissed.", "application\n[2] is dismissed"),
    ]:
        assert _build_reader_extracted_summary(
            summary_case(text), stored_outcome(text, evidence), format_decision(text), [], [],
        ) == []


def test_summary_quote_survives_missing_outcome_label():
    text = "[8] The application is dismissed."
    rows = _build_reader_extracted_summary(
        summary_case(text), stored_outcome(text, "application is dismissed", decision_outcome=None),
        format_decision(text), [], [],
    )
    assert [(row.key, row.value) for row in rows] == [("disposition", text)]


@pytest.mark.parametrize("source_text", ["Justice Smith", "unverified judge"])
def test_summary_stored_judge_provenance_must_match_labelled_header(source_text):
    text = "Judge: Justice Smith\nDecision Content\n[1] Background."
    case = summary_case(text, metadata_json={"reader_extracted": {
        "judge": "Justice Smith", "_field_sources": {"judge": {"text": source_text}},
    }})
    rows = _build_reader_extracted_summary(case, None, format_decision(text), [], [])
    assert [row.value for row in rows] == (["Justice Smith"] if source_text == "Justice Smith" else [])


@pytest.mark.parametrize("use_stored_payload", [True, False])
def test_summary_normalized_honourable_judge_links_exact_name_without_changing_offsets(use_stored_payload):
    text = (
        "Date: 20060914\nDocket: IMM-123-05\nCitation: 2006 FC 1160\n"
        "PRESENT: The Honourable Paul U.C. Rouleau\n"
        "BETWEEN:\nFADILA KHARCHI\nApplicant\nand\n"
        "THE MINISTER OF CITIZENSHIP AND IMMIGRATION\nRespondent\n"
        "REASONS FOR JUDGMENT\n[1] The application is dismissed.\n"
    )
    stored = extract_case_metadata(text)
    name = "Paul U.C. Rouleau"
    assert stored["judge"] == name
    case = summary_case(text, metadata_json={"reader_extracted": stored})
    blocks = format_decision(text)
    before = deepcopy((vars(case), blocks))
    metadata = [] if use_stored_payload else [
        reader_service.CaseReaderMetadataFieldResponse(
            key="judge", value=name, source="reader_extracted", evidence=name,
        ),
    ]
    if not use_stored_payload:
        case.metadata_json = {}
        before = deepcopy((vars(case), blocks))
    rows = _build_reader_extracted_summary(case, None, blocks, [], metadata)
    judge = next(row for row in rows if row.key == "judge")
    assert judge.value == judge.evidence == name
    assert judge.source == "reader_extracted"
    assert (judge.start, judge.end) == (text.index(name), text.index(name) + len(name))
    assert text[judge.start:judge.end] == name
    header = next(block for block in blocks if block["start"] == judge.block_start)
    assert header["type"] == judge.block_type == "courtline"
    assert "PRESENT: The Honourable " + name in text[header["start"]:header["end"]]
    assert header["start"] <= judge.start < judge.end <= header["end"]
    assert judge.paragraph_number is None
    assert (vars(case), blocks) == before


@pytest.mark.parametrize("prefix", [
    "The Right Honourable ", "Honorable ", "L’honorable ",
    "The Honourable Mr. Justice ", "Madame Justice ",
    "monsieur le juge en chef par intérim ",
    "Counsel ", "The distinguished ", "The Honourable Counsel ",
])
def test_summary_judge_header_only_allows_supported_normalizer_prefixes(prefix):
    name = "Paul U.C. Rouleau"
    text = f"PRESENT: {prefix}{name}\nREASONS FOR JUDGMENT\n[1] Background."
    case = summary_case(text, metadata_json={"reader_extracted": {
        "judge": name, "_field_sources": {"judge": {"text": name}},
    }})
    rows = _build_reader_extracted_summary(case, None, format_decision(text), [], [])
    assert [row.value for row in rows] == (
        [] if prefix in {"Counsel ", "The distinguished ", "The Honourable Counsel "} else [name]
    )


def test_summary_unsupported_header_values_are_omitted_without_body_fallback():
    text = ("Federal Court\nDate: 20260102\nJudge: Justice Jones\nDecision Content\n"
            "[1] FC. Date: 20250102. Judge: Justice Smith.")
    judge = reader_service.CaseReaderMetadataFieldResponse(
        key="judge", value="Justice Smith", source="reader_extracted", evidence="Justice Smith",
    )
    assert _build_reader_extracted_summary(
        summary_case(text, court="FC"), None, format_decision(text), [], [judge],
    ) == []


def test_summary_repeated_paragraph_numbers_keep_stored_location_not_first_match():
    text = "[1] First.\n[1] The application is dismissed."
    second = text.index("[1]", 1)
    blocks = [
        {"type": "para", "num": 1, "start": 0, "end": second - 1},
        {"type": "para", "num": 1, "start": second, "end": len(text)},
    ]
    rows = _build_reader_extracted_summary(
        summary_case(text), stored_outcome(text, "application is dismissed"), blocks, [], [],
    )
    assert all(row.block_start == second and row.paragraph_number == 1 for row in rows)


def stored_outcome(text, evidence, **overrides):
    start = text.index(evidence)
    values = dict(
        decision_outcome="dismissed", source="deterministic_outcome",
        disposition_evidence=evidence, evidence_offset_start=start,
        evidence_offset_end=start + len(evidence),
    )
    values.update(overrides)
    return SimpleNamespace(**values)


def test_reader_outcome_quote_is_exact_paragraph_and_preserves_offsets():
    text = "Decision Content\n[1] Background 😀.\nConclusion\n[42] The application is dismissed.\nCosts remain <reserved> & unpaid.\n“Justice Smith”\n"
    case = SimpleNamespace(full_text=text)
    blocks = format_decision(text)
    original = deepcopy(blocks)
    outcome = stored_outcome(text, "application is dismissed")
    rows = {row.key: row for row in _build_reader_outcome_metadata(case, outcome, blocks)}

    assert rows["decision_outcome"].value == "dismissed"
    assert rows["decision_outcome"].source == "deterministic_outcome"
    assert rows["disposition_paragraph"].value == (
        "[42] The application is dismissed.\nCosts remain <reserved> & unpaid."
    )
    assert rows["disposition_paragraph"].evidence == rows["disposition_paragraph"].value
    assert rows["disposition_paragraph_number"].value == "42"
    assert blocks == original
    assert case.full_text == text


def test_reader_missing_outcome_is_omitted_not_inferred():
    text = "[1] The application is dismissed."
    assert _build_reader_outcome_metadata(SimpleNamespace(full_text=text), None, format_decision(text)) == []


@pytest.mark.parametrize("overrides", [
    {"disposition_evidence": None},
    {"evidence_offset_start": None},
    {"evidence_offset_start": -1},
    {"evidence_offset_end": 999},
    {"disposition_evidence": "invented evidence"},
])
def test_reader_outcome_alone_or_invalid_evidence_never_supplies_disposition(overrides):
    text = "[1] The application is dismissed."
    rows = _build_reader_outcome_metadata(
        SimpleNamespace(full_text=text),
        stored_outcome(text, "application is dismissed", **overrides),
        format_decision(text),
    )
    assert [row.key for row in rows] == ["decision_outcome"]


def test_reader_quote_can_exist_without_outcome_label():
    text = "[8] The application is dismissed."
    rows = _build_reader_outcome_metadata(
        SimpleNamespace(full_text=text),
        stored_outcome(text, "application is dismissed", decision_outcome=None),
        format_decision(text),
    )
    assert [row.key for row in rows] == ["disposition_paragraph", "disposition_paragraph_number"]


def test_reader_does_not_link_evidence_in_caption_or_across_paragraphs():
    for text, evidence in [
        ("Application dismissed\nDecision Content\n[1] Background.", "Application dismissed"),
        ("[1] The application\n[2] is dismissed.", "application\n[2] is dismissed"),
    ]:
        rows = _build_reader_outcome_metadata(
            SimpleNamespace(full_text=text), stored_outcome(text, evidence), format_decision(text),
        )
        assert [row.key for row in rows] == ["decision_outcome"]


@pytest.mark.parametrize("has_outcome", [True, False], ids=["stored-outcome", "no-outcome"])
def test_build_case_reader_data_serializes_stored_outcome_read_only(monkeypatch, has_outcome):
    text = (
        "Decision Content\n[1] Background 😀.\nConclusion\n"
        "[42] The application is dismissed.\nCosts remain <reserved> & unpaid.\n"
        "“Justice Smith”\n"
    )
    case = SimpleNamespace(
        id=67, title="Synthetic reader case", court="FC", date=date(2025, 1, 2),
        full_text=text, summary=None,
    )
    original_case = deepcopy(vars(case))
    expected_blocks = deepcopy(format_decision(text))
    outcome = stored_outcome(text, "application is dismissed") if has_outcome else None
    baseline_metadata = reader_service.CaseReaderMetadataFieldResponse(
        key="test_baseline", value="preserved", source="test",
    )
    monkeypatch.setattr(reader_service, "_build_reader_inferred_tags", lambda *args: [])
    monkeypatch.setattr(
        reader_service, "_build_reader_extracted_metadata",
        lambda *args: [baseline_metadata],
    )

    class EmptyRows(list):
        def all(self):
            return list(self)

    class ReadOnlyDB:
        def __init__(self):
            self.scalar_entities = []
            self.collection_entities = []
            self.execute_count = 0
            self.write_calls = []

        def scalar(self, statement):
            assert statement.is_select
            entity = statement.column_descriptions[0]["entity"]
            self.scalar_entities.append(entity)
            if entity is reader_service.Citation:
                # The live "cited by" count: distinct citing cases for this authority.
                assert "count(distinct(citations.source_case_id))" in str(statement)
                assert statement.compile().params["target_case_id_1"] == case.id
                return 0
            assert statement.compile().params["case_id_1" if entity is not reader_service.Case else "id_1"] == case.id
            if entity is reader_service.Case:
                return case
            if entity is reader_service.CitationMetrics:
                return None
            assert entity is reader_service.CaseOutcome
            sql = str(statement)
            assert "ORDER BY case_outcomes.updated_at DESC, case_outcomes.id DESC" in sql
            assert 1 in statement.compile().params.values()
            return outcome

        def scalars(self, statement):
            assert statement.is_select
            entity = statement.column_descriptions[0]["entity"]
            assert entity in (
                reader_service.CaseSource, reader_service.CaseChunk, reader_service.CaseTag,
            )
            self.collection_entities.append(entity)
            return []

        def execute(self, statement):
            assert statement.is_select
            self.execute_count += 1
            return EmptyRows()

        def forbidden_write(self, *args, **kwargs):
            self.write_calls.append((args, kwargs))
            pytest.fail("Reader assembly attempted a database write")

        add = add_all = delete = flush = commit = rollback = merge = forbidden_write

    db = ReadOnlyDB()
    response = reader_service.build_case_reader_data(case.id, db)
    payload = json.loads(response.model_dump_json())

    expected_metadata = [baseline_metadata.model_dump(mode="json")]
    if has_outcome:
        quote = "[42] The application is dismissed.\nCosts remain <reserved> & unpaid."
        expected_metadata += [
            {
                "key": "decision_outcome", "value": "dismissed",
                "source": "deterministic_outcome", "evidence": None,
            },
            {
                "key": "disposition_paragraph", "value": quote,
                "source": "deterministic_outcome", "evidence": quote,
            },
            {
                "key": "disposition_paragraph_number", "value": "42",
                "source": "formatter", "evidence": None,
            },
        ]
    assert payload["extracted_metadata"] == expected_metadata
    assert [row["key"] for row in payload["extracted_summary"]] == (
        ["disposition", "outcome", "outcome_source"] if has_outcome else []
    )
    assert payload["case"]["full_text"] == text
    assert payload["format_blocks"] == expected_blocks
    assert response.format_blocks == expected_blocks
    assert vars(case) == original_case
    assert db.scalar_entities == [
        reader_service.Case, reader_service.CitationMetrics, reader_service.Citation,
        reader_service.CaseOutcome,
    ]
    assert db.collection_entities == [
        reader_service.CaseSource, reader_service.CaseChunk, reader_service.CaseTag,
    ]
    assert db.execute_count == 2
    assert db.write_calls == []


def test_unit_roles_come_from_stored_paragraph_text_and_skip_reports_without_it():
    from backend import reader_service

    report = {
        "paragraphs": [
            {"paragraph_index": 0, "text": "[1] This is an application for judicial review of a RAD decision."},
            {"paragraph_index": 1, "text": "[2] I find that the RAD erred."},
            {"paragraph_index": 2, "text": "[3] For these reasons, the application is allowed."},
        ],
        "discussion_units": [
            {"start_paragraph": 0, "end_paragraph": 0},
            {"start_paragraph": 1, "end_paragraph": 1},
            {"start_paragraph": 2, "end_paragraph": 2},
        ],
    }
    assert reader_service._unit_roles(report) == ["overview", "analysis", "disposition"]
    assert reader_service._unit_roles({"discussion_units": report["discussion_units"]}) == []
