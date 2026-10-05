"""Offline synthetic regression set, not measured legal-review accuracy."""

import json
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend import citation_treatment_service as service
from backend import routes
from backend.citation_treatment import CLASSES, classify_paragraph, summarize_treatment

FIXTURES = json.loads((Path(__file__).parent / "fixtures/citation_treatment_invented.json").read_text())


@pytest.mark.parametrize("row", FIXTURES, ids=lambda row: row["id"])
def test_invented_labelled_paragraphs(row):
    events = classify_paragraph(row["text"], row["citations"])
    for expected in row["expected"]:
        observed = {e["class"] for e in events if e["citation_id"] == expected["citation_id"]}
        assert observed == set(expected["classes"])
        if "events" in expected:
            assert [
                {key: event[key] for key in ("matched_phrase", "phrase_start", "phrase_end")}
                for event in events if event["citation_id"] == expected["citation_id"]
            ] == expected["events"]
    for event in events:
        assert f'rule_id={event["rule_id"]}' in event["how_assigned"]
        assert f'phrase="{event["matched_phrase"]}"' in event["how_assigned"]
        if event["class"] != "unknown":
            assert row["text"][event["phrase_start"]:event["phrase_end"]] == event["matched_phrase"]
            assert event["matched_phrase"]


def test_fixture_metrics_have_all_classes_and_exact_citation_spans():
    counts = Counter()
    for row in FIXTURES:
        for citation in row["citations"]:
            assert row["text"][citation["start"]:citation["end"]] == citation["citation_text"]
        for expected in row["expected"]:
            counts.update(expected["classes"])
    assert len(FIXTURES) >= 40
    assert set(counts) == set(CLASSES)
    assert all(count >= 8 for count in counts.values())


def classify(text, labels=("2099 FC 1",)):
    citations = []
    for i, label in enumerate(labels):
        start = text.index(label)
        citations.append({"citation_id": i, "target_case_id": i + 1,
                          "citation_text": label, "start": start, "end": start + len(label)})
    return classify_paragraph(text, citations)


@pytest.mark.parametrize("text", [
    "I follow the statutory procedure when reviewing 2099 FC 1.",
    "I consider my jurisdiction and cite 2099 FC 1.",
    '“I follow 2099 FC 1.”',
    "‘I follow 2099 FC 1.’",
    '"I follow 2099 FC 1.',
    "I do not decline to follow 2099 FC 1.",
    "I never follow 2099 FC 1.",
    "I would follow 2099 FC 1.",
    "I recall that the judge follows 2099 FC 1.",
    "I note that my colleague follows 2099 FC 1.",
    "The witness testified: 'I follow 2099 FC 1.",
    "' I follow 2099 FC 1.",
    "In an earlier decision, I follow 2099 FC 1.",
    "I follow 2099 FC 1 and 2099 FC 2.",
    "I follow Applicant v. Minister, 2099 FC 1.",  # supply the entire stored span below
])
def test_additional_scope_abstentions(text):
    labels = ("2099 FC 1", "2099 FC 2") if "2099 FC 2" in text else ("2099 FC 1",)
    assert {e["class"] for e in classify(text, labels)} == {"unknown"}


def test_entire_named_citation_and_abbreviations_preserve_offsets():
    label = "Invented v. Fiction, 2099 FC 1"
    text = f"I follow {label} at para. 9."
    events = classify(text, (label,))
    assert events[0]["class"] == "followed_applied"
    assert text[events[0]["phrase_start"]:events[0]["phrase_end"]] == "follow"


@pytest.mark.parametrize("text", [
    "I would consider 2099 FC 1 but follow 2099 FC 2.",
    "I said that I follow 2099 FC 1 and I distinguish 2099 FC 2.",
])
def test_governing_attribution_and_modals_survive_coordination(text):
    assert {e["class"] for e in classify(text, ("2099 FC 1", "2099 FC 2"))} == {"unknown"}


def test_governing_negation_does_not_become_positive_in_coordination():
    events = classify("I do not follow 2099 FC 1 and apply 2099 FC 2.",
                      ("2099 FC 1", "2099 FC 2"))
    assert {e["class"] for e in events if e["target_case_id"] == 2} == {"unknown"}
    events = classify("I do not follow 2099 FC 1 but apply 2099 FC 2.",
                      ("2099 FC 1", "2099 FC 2"))
    assert {e["class"] for e in events if e["target_case_id"] == 2} == {"followed_applied"}


def test_mixed_events_for_one_occurrence_remain_separate():
    mixed = classify("I consider 2099 FC 1 problematic.")
    assert {e["class"] for e in mixed} == {"considered_neutral", "criticised_not_followed"}
    assert len(mixed) == 2
    events = classify("I consider and follow 2099 FC 1.")
    # No pronoun/back-reference guessing across clauses: only the bound follow cue.
    assert {e["class"] for e in events} == {"followed_applied"}
    evidence = [
        {**classify("I follow 2099 FC 1.")[0], "source_case_id": 1,
         "paragraph_start": 0, "paragraph_end": 25, "paragraph_text": "I follow 2099 FC 1."},
        {**classify("I distinguish 2099 FC 1.")[0], "source_case_id": 1,
         "paragraph_start": 26, "paragraph_end": 55, "paragraph_text": "I distinguish 2099 FC 1."},
    ]
    result = summarize_treatment(1, evidence)
    assert result["classes"]["followed_applied"]["count"] == 1
    assert result["classes"]["distinguished"]["count"] == 1
    assert result["total_distinct_citing_decisions"] == 1
    assert result["evidence"] == evidence


def test_invalid_span_abstains_with_explanation():
    event = classify_paragraph("I follow 2099 FC 1.", [
        {"citation_id": 1, "citation_text": "2099 FC 1", "start": -1, "end": 8},
    ])[0]
    assert event["class"] == "unknown"
    assert event["reason"] == "invalid_citation_span"


def stored_rows():
    rows = []
    for source_id in range(10, 17):
        text = "[1] I follow 2099 FC 1.\n[2] I distinguish 2099 FC 1 on remedy."
        source = SimpleNamespace(id=source_id, title=f"Invented {source_id}", full_text=text)
        for number, block in enumerate(text.split("\n")):
            chunk = SimpleNamespace(id=source_id * 10 + number, case_id=source_id, text=block)
            offset = block.index("2099 FC 1")
            citation = SimpleNamespace(id=chunk.id, source_case_id=source_id, target_case_id=1,
                citation_kind="neutral", citation_text="2099 FC 1", chunk_id=chunk.id,
                offset_start=offset, offset_end=offset + 9)
            rows.append((citation, chunk, source))
    # Distinct decision with only an unclassifiable paragraph, and missing text.
    for source_id, text in (
        (20, "[1] Counsel follows 2099 FC 1."), (21, None),
        (22, "[1] I did not follow 2099 FC 1."), (23, "[1] I consider 2099 FC 1."),
    ):
        source = SimpleNamespace(id=source_id, title="Unknown", full_text=text)
        offset = text.index("2099 FC 1") if text else None
        citation = SimpleNamespace(id=source_id * 10, source_case_id=source_id, target_case_id=1,
            citation_kind="neutral", citation_text="2099 FC 1", chunk_id=None,
            offset_start=offset, offset_end=offset + 9 if offset is not None else None)
        rows.append((citation, None, source))
    # Unknown paragraph must not put a classifiable decision into unknown.
    source = SimpleNamespace(id=10, title="Invented 10",
        full_text=rows[0][2].full_text)
    bad = SimpleNamespace(id=999, source_case_id=10, target_case_id=1,
        citation_kind="neutral", citation_text="2099 FC 1", chunk_id=None,
        offset_start=999, offset_end=1008)
    rows.append((bad, None, source))
    return rows


class ReadOnlyMock:
    def __init__(self, rows=(), exists=True):
        self.rows = rows
        self.exists = exists
        self.commands = []

    def scalar(self, statement):
        assert statement.is_select
        return SimpleNamespace(id=1) if self.exists else None

    def execute(self, statement):
        assert statement.is_select
        self.commands.append(str(statement))
        return iter(self.rows)


def client(db):
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[routes.get_db] = lambda: db
    return TestClient(app)


def test_mocked_endpoint_distinct_denominator_overlap_examples_and_evidence():
    db = ReadOnlyMock(stored_rows())
    with client(db) as http:
        response = http.get("/api/citation-treatment/1")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "experimental"
    assert data["experimental"] and data["read_only"]
    assert data["total_distinct_citing_decisions"] == 11
    assert set(data["classes"]) == set(CLASSES)
    assert {k: v["count"] for k, v in data["classes"].items()} == {
        "followed_applied": 7, "distinguished": 7, "criticised_not_followed": 1,
        "considered_neutral": 1, "unknown": 2,
    }
    assert len(data["classes"]["followed_applied"]["examples"]) == 5
    assert len(data["classes"]["distinguished"]["examples"]) == 5
    assert all(c["denominator"] == 11 for c in data["classes"].values())
    assert data["classes"]["followed_applied"]["percentage"] == 63.64
    assert len(data["evidence"]) == 19  # no collapsing mixed paragraphs/unknown events
    assert len(db.commands) == 1
    assert "target_case_id" in db.commands[0]
    for event in data["evidence"]:
        if event["class"] != "unknown":
            assert event["paragraph_text"][event["phrase_start"]:event["phrase_end"]] == event["matched_phrase"]
            assert event["phrase_document_start"] == event["paragraph_start"] + event["phrase_start"]


def test_mocked_endpoint_missing_and_empty():
    with client(ReadOnlyMock(exists=False)) as http:
        assert http.get("/api/citation-treatment/999").status_code == 404
    with client(ReadOnlyMock()) as http:
        data = http.get("/api/citation-treatment/1").json()
    assert data["total_distinct_citing_decisions"] == 0
    assert data["status"] == "experimental"
    assert data["evidence"] == []
    assert all(c["count"] == c["denominator"] == 0 and c["examples"] == []
               for c in data["classes"].values())


def test_source_projection_sees_other_authorities_before_filtering_target():
    text = "[1] I follow 2099 FC 1 but distinguish 2099 FC 2."
    source = SimpleNamespace(id=10, title="Invented", full_text=text)
    rows = []
    for i, label in enumerate(("2099 FC 1", "2099 FC 2")):
        start = text.index(label)
        rows.append((SimpleNamespace(id=i, source_case_id=10, target_case_id=i+1,
            citation_kind="neutral", citation_text=label, chunk_id=None,
            offset_start=start, offset_end=start+len(label)), None, source))
    result = service.citation_treatment_summary(ReadOnlyMock(rows), 1)
    assert [e["class"] for e in result["evidence"]] == ["followed_applied"]
    assert all(e["target_case_id"] == 1 for e in result["evidence"])


def test_projection_rejects_ambiguous_chunks_and_unnumbered_context():
    for text, chunk_text in (("[1] repeated\n[2] repeated", "repeated"),
                             ("I follow 2099 FC 1.", "I follow 2099 FC 1.")):
        source = SimpleNamespace(id=10, title="Invented", full_text=text)
        chunk = SimpleNamespace(id=5, case_id=10, text=chunk_text)
        citation = SimpleNamespace(id=1, source_case_id=10, target_case_id=1,
            citation_kind="neutral", citation_text="2099 FC 1", chunk_id=5,
            offset_start=9, offset_end=18)
        result = service.citation_treatment_summary(ReadOnlyMock([(citation, chunk, source)]), 1)
        assert result["classes"]["unknown"]["count"] == 1
        assert result["classes"]["followed_applied"]["count"] == 0
