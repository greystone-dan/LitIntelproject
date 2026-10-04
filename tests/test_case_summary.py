from datetime import date
from types import SimpleNamespace as Row

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.dialects import postgresql

from backend.case_formatter import format_decision
from backend.case_summary import (
    ACTIVE_TAG_TAXONOMY_VERSION,
    build_case_summary,
    get_db,
    project_case_summary,
    router,
)
from backend.models import (
    CaseEvidenceSummaryResponse,
    CaseDiscussionUnitSummaryResponse,
    CaseSubThemeSummaryResponse,
)
from backend.reader_service import _build_case_summary


def _summary_with_roles(roles: list[str]) -> CaseEvidenceSummaryResponse:
    return CaseEvidenceSummaryResponse(
        method="discussion_unit_v1",
        version="1.4",
        total_units=1,
        total_subthemes=1,
        note="test",
        units=[
            CaseDiscussionUnitSummaryResponse(
                discussion_unit_id="1093:1",
                unit_index=1,
                start_paragraph=0,
                end_paragraph=2,
                paragraph_count=3,
                subthemes=[
                    CaseSubThemeSummaryResponse(
                        subtheme_id="1093:1:1",
                        paragraph_indices=[0, 1],
                        key_terms=["review"],
                        display_key_terms=["review"],
                        argument_roles=roles,
                        explanation="Deterministic source explanation.",
                        evidence=[],
                    )
                ],
            )
        ],
    )


def test_case_summary_uses_stable_section_order_and_role_mapping():
    summary = _build_case_summary(_summary_with_roles(["issue", "reasoning_application"]))

    assert summary is not None
    assert [section.section_id for section in summary.sections] == [
        "issue",
        "party_positions",
        "facts",
        "governing_law",
        "reasoning",
        "limitations",
        "disposition",
    ]
    assert summary.total_available_sections == 2
    assert summary.sections[0].items[0].paragraph_indices == [0, 1]
    assert summary.sections[4].items[0].text == "Deterministic source explanation."


def test_case_summary_marks_missing_roles_explicitly():
    summary = _build_case_summary(_summary_with_roles([]))

    assert summary is not None
    assert summary.total_available_sections == 0
    assert summary.total_unavailable_sections == 7
    assert all(
        section.unavailable_reason == "Not detected in available evidence."
        for section in summary.sections
    )


# The public stored summary is separate from the technical reader summary above.


def case(text="", **values):
    return Row(
        id=42, title=values.get("title", "Élodie v Canada"),
        citation=values.get("citation", "2026 FC 42"),
        court=values.get("court", "Federal Court"),
        date=values.get("date", date(2026, 1, 2)), full_text=text,
    )


def outcome(text, evidence, start=None, **values):
    start = text.index(evidence) if start is None else start
    defaults = dict(
        decision_outcome="allowed", source="stored_rule",
        disposition_evidence=evidence, evidence_offset_start=start,
        evidence_offset_end=start + len(evidence),
    )
    defaults.update(values)
    return Row(**defaults)


def tag(text, evidence="review", **values):
    start = text.index(evidence)
    defaults = dict(
        category="legal", value="review", score=0.8, source="stored_tag",
        taxonomy_version=ACTIVE_TAG_TAXONOMY_VERSION, evidence=evidence,
        offset_start=start, offset_end=start + len(evidence),
    )
    defaults.update(values)
    return Row(**defaults)


def statute(key, **values):
    defaults = dict(instrument_key=key, reference_kind="statute")
    defaults.update(values)
    return Row(**defaults)


def assert_slice(text, excerpt):
    assert excerpt.text == text[excerpt.start:excerpt.end]
    block = next(b for b in format_decision(text) if b["start"] == excerpt.block_start)
    assert block["type"] == "para"
    assert block["num"] == excerpt.paragraph_number


def test_unicode_repeated_evidence_uses_stored_offsets_and_continuation():
    text = (
        "É😀 header\n[1] The application is allowed.\n"
        "[1] Élodie succeeds.\nThe application is allowed.\n"
        "(a) Costs follow.\n[2] Other reasons."
    )
    evidence = "The application is allowed."
    stored_start = text.rindex(evidence)
    summary = project_case_summary(case(text), outcome(text, evidence, stored_start))
    assert summary.disposition.text == (
        "[1] Élodie succeeds.\nThe application is allowed.\n(a) Costs follow."
    )
    assert summary.disposition.block_start == text.index("[1] Élodie")
    assert_slice(text, summary.disposition)


def test_evidence_spanning_continuation_and_quote_block_is_verbatim():
    quote = '“' + "The application is allowed and the matter is returned for reconsideration. " * 2 + '”'
    text = "[1] Reasons.\n" + quote + "\nThe order follows.\n[2] End."
    evidence = quote + "\nThe order follows."
    result = project_case_summary(case(text), outcome(text, evidence))
    assert result.disposition.text == text[:text.index("\n[2]")]
    assert_slice(text, result.disposition)


@pytest.mark.parametrize("invalid", [
    {"disposition_evidence": "Invented evidence"},
    {"evidence_offset_start": -1},
    {"evidence_offset_start": True},
    {"evidence_offset_start": None},
    {"evidence_offset_end": 10000},
    {"evidence_offset_end": None},
])
def test_invalid_offsets_never_search_for_replacement(invalid):
    text = "[1] The application is allowed.\n[2] Other reasons."
    result = project_case_summary(case(text), outcome(text, "allowed", **invalid))
    assert result.disposition is None
    assert result.decision_outcome == "allowed"
    assert result.outcome_source == "stored_rule"


@pytest.mark.parametrize("text,evidence", [
    ("The application is allowed.\n[1] Reasons.", "allowed"),
    ("[1] Reasons.\nDisposition\nThe application is allowed.", "allowed"),
    ("[1] Reasons allowed.\n[2] Other reasons.", "allowed.\n[2] Other"),
])
def test_unnumbered_and_crossparagraph_evidence_omitted(text, evidence):
    result = project_case_summary(case(text), outcome(text, evidence))
    assert result.disposition is None


def test_stale_repeated_text_offset_does_not_get_relocated():
    text = "[1] Different text.\n[2] The application is allowed."
    result = project_case_summary(case(text), outcome(text, "allowed", start=4))
    assert result.disposition is None


@pytest.mark.parametrize("body", [
    "The issue is whether Dr. Élodie met s. 25. The record is complete.",
    "The issue is whether Mr. Smith succeeds in Canada v. Smith. This is contested.",
    "The issue is whether examples, e.g. these records, suffice. The record is complete.",
    "The issue is whether the record suffices? The parties disagree!",
])
def test_issue_sentences_abbreviations_and_unicode(body):
    text = "😀 heading\n[1] " + body + "\n[2] Background."
    result = project_case_summary(case(text))
    assert result.issue.kind == "issue"
    assert result.issue.text == body
    assert_slice(text, result.issue)


def test_issue_selects_at_most_two_sentences_without_generated_prose():
    text = "[1] The issue is whether the record suffices. It is disputed. Other matters follow."
    excerpt = project_case_summary(case(text)).issue
    assert excerpt.text == "The issue is whether the record suffices. It is disputed."
    assert_slice(text, excerpt)


@pytest.mark.parametrize("body", [
    "The issue is whether the record suffices",
    "The issue is whether the record suffices. An unfinished tail",
    "The issue is whether Acme Ltd. succeeds. Other matters follow.",
    "The issue is whether J. Smith succeeds.",
    "The issue is whether Adm. Smith succeeds.",
    "The issue is whether the record... suffices.",
    'The issue is whether "sufficient." means anything.',
    "The issue is whether Dr.",
    "The issue is whether 1.5 records suffice.",
    "The issue is whether records suffice; e.g.",
])
def test_incomplete_or_ambiguous_sentences_are_omitted(body):
    assert project_case_summary(case("[1] " + body)).issue is None


def test_issue_prioritized_over_review_and_heading_rules():
    text = (
        "[1] The standard of review is reasonableness.\n"
        "II. Issues\n[2] Does this record suffice?\nA second question arises.\n"
        "[3] Background follows."
    )
    result = project_case_summary(case(text))
    assert result.issue.kind == "issue"
    assert result.issue.text == "Does this record suffice?\nA second question arises."
    assert_slice(text, result.issue)
    review = project_case_summary(case("[1] The standard of review is reasonableness."))
    assert review.issue.kind == "standard_of_review"
    heading = project_case_summary(case("[1] Background.\nStandard of review\n[2] Reasonableness applies."))
    assert heading.issue.kind == "standard_of_review"


def test_no_generated_fallback_and_no_unrelated_heading_paragraph():
    row = case("[1] Background.\nIssues\n[2] Incomplete question\n[3] A complete unrelated sentence.")
    row.summary = "Generated summary that must not be used."
    row.issues = ["Invented issue"]
    assert project_case_summary(row).issue is None


def test_heading_does_not_skip_unnumbered_text_to_label_unrelated_paragraph():
    text = "[1] Background.\nIssues\nAn incomplete unnumbered issue\n[2] Other matters follow."
    assert project_case_summary(case(text)).issue is None


def test_missing_fields_unclassified_and_unknown_source_serialized_omission():
    row = case(title=None, citation=None, court=None, date=None)
    result = project_case_summary(row)
    assert result.model_dump(exclude_none=True) == {
        "case_id": 42, "decision_outcome": "unclassified", "outcome_source": "unknown",
        "top_statutes": [], "top_tags": [],
    }
    text = "[1] The application is allowed."
    result = project_case_summary(case(text), outcome(
        text, "allowed", decision_outcome=None, source=None,
    ))
    assert result.decision_outcome == "unclassified"
    assert result.outcome_source == "unknown"
    assert result.disposition is not None


def test_statute_counts_instrument_grouping_ranking_and_optional_exact_evidence():
    text = "[1] IRPA review."
    references = [
        statute("IRPA", pinpoint="25", reference_text="IRPA", offset_start=4, offset_end=8),
        statute("IRPA", pinpoint="26"), statute("IRPA", pinpoint="26"),
        statute("IRPR"), statute("IRPR", reference_kind="instrument"),
        statute("A"), statute(None), statute("not-a-statute", reference_kind="case"),
        statute(None, normalized_reference="invented fallback"),
    ]
    result = project_case_summary(case(text), statute_references=references)
    assert [(r.instrument_key, r.count) for r in result.top_statutes] == [
        ("IRPA", 3), ("IRPR", 2), ("A", 1),
    ]
    assert_slice(text, result.top_statutes[0].evidence)
    assert result.top_statutes[1].evidence is None
    reversed_result = project_case_summary(case(text), statute_references=reversed(references))
    assert reversed_result == result


def test_active_tags_deduplicated_verified_ranked_and_bounded_deterministically():
    text = "[1] review review."
    tags = [
        tag(text, value="z", score=0.9), tag(text, value="a", score=0.9),
        tag(text, value="a", score=0.8),
        tag(text, value="stale", offset_start=0),
        tag(text, value="old", taxonomy_version="old"),
        tag(text, value="nonfinite", score=float("nan")),
        tag(text, value="missing", score=None),
    ] + [tag(text, value=str(i), score=0.5) for i in range(8)]
    result = project_case_summary(
        case(text), tags=tags,
        statute_references=[statute(str(i)) for i in range(8)],
    )
    assert [t.value for t in result.top_tags] == ["a", "z", "0", "1", "2"]
    assert len(result.top_statutes) == 5
    for stored_tag in result.top_tags:
        assert_slice(text, stored_tag.evidence)
    assert project_case_summary(
        case(text), tags=reversed(tags),
        statute_references=[statute(str(i)) for i in reversed(range(8))],
    ) == result


def test_chunk_relative_statutes_keep_counts_without_false_document_links():
    text = "[1] IRPA review.\n[2] IRPA review."
    references = [
        statute("IRPA", chunk_id=91, reference_text="IRPA", offset_start=4, offset_end=8),
    ]
    result = project_case_summary(case(text), statute_references=references)
    assert result.top_statutes[0].count == 1
    assert result.top_statutes[0].evidence is None


class FakeSession:
    """Only read methods exist: unexpected database writes fail immediately."""

    def __init__(self, row, stored_outcome=None, tags=(), references=()):
        self.row = row
        self.outcome = stored_outcome
        self.tags = tags
        self.references = references
        self.queries = []

    def scalar(self, statement):
        self.queries.append(statement)
        entity = statement.column_descriptions[0]["entity"]
        return self.row if entity.__name__ == "Case" else self.outcome

    def scalars(self, statement):
        self.queries.append(statement)
        entity = statement.column_descriptions[0]["entity"]
        return iter(self.tags if entity.__name__ == "CaseTag" else self.references)


def client_for(session):
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[get_db] = lambda: session
    return TestClient(app)


def test_read_only_service_query_contract_latest_outcome_and_active_taxonomy():
    session = FakeSession(case())
    assert build_case_summary(42, session).case_id == 42
    queries = [str(q.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
               for q in session.queries]
    assert len(queries) == 4
    assert all(q.startswith("SELECT") for q in queries)
    assert "cases.id = 42" in queries[0]
    assert "case_outcomes.case_id = 42" in queries[1]
    assert "ORDER BY case_outcomes.updated_at DESC, case_outcomes.id DESC" in queries[1]
    assert "LIMIT 1" in queries[1]
    assert "case_tags.case_id = 42" in queries[2]
    assert ACTIVE_TAG_TAXONOMY_VERSION in queries[2]
    assert "statute_references.source_case_id = 42" in queries[3]


def test_typed_endpoint_exact_route_serialization_and_evidence_contract():
    text = "[1] The issue is whether review applies.\n[2] The application is allowed."
    session = FakeSession(case(text), outcome(text, "allowed"), [tag(text)], [statute("IRPA")])
    with client_for(session) as client:
        response = client.get("/api/cases/42/summary")
        assert response.status_code == 200
        payload = response.json()
        assert payload["case_id"] == 42
        assert payload["style_of_cause"] == "Élodie v Canada"
        assert payload["date"] == "2026-01-02"
        assert payload["decision_outcome"] == "allowed"
        assert payload["outcome_source"] == "stored_rule"
        for key in ("issue", "disposition"):
            excerpt = payload[key]
            assert excerpt["text"] == text[excerpt["start"]:excerpt["end"]]
        assert "evidence" not in payload["top_statutes"][0]
        schema = client.get("/openapi.json").json()
        assert "/api/cases/{case_id}/summary" in schema["paths"]
        assert "StoredCaseSummaryResponse" in schema["components"]["schemas"]


def test_endpoint_404_and_invalid_id_no_extra_queries():
    session = FakeSession(None)
    with client_for(session) as client:
        response = client.get("/api/cases/42/summary")
        assert response.status_code == 404
        assert response.json() == {"detail": "Case not found"}
        assert len(session.queries) == 1
        assert client.get("/api/cases/not-an-id/summary").status_code == 422
        assert len(session.queries) == 1


def test_endpoint_omits_absent_facts_and_excerpts():
    with client_for(FakeSession(case(title=None, citation=None, court=None, date=None))) as client:
        assert client.get("/api/cases/42/summary").json() == {
            "case_id": 42, "decision_outcome": "unclassified", "outcome_source": "unknown",
            "top_statutes": [], "top_tags": [],
        }


def test_application_registers_summary_route_and_preserves_reader_routes():
    from backend.main import app

    text = "[1] The application is allowed."
    session = FakeSession(case(text), outcome(text, "allowed"))
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = lambda: session
    try:
        # Do not enter application lifespan: startup is production-owned.
        client = TestClient(app)
        response = client.get("/api/cases/42/summary")
        assert response.status_code == 200
        assert response.json()["disposition"]["text"] == text
        paths = {route.path for route in app.routes}
        assert "/cases/{case_id}/reader-data" in paths
        assert "/data-explorer" in paths
        assert "/api/cases/{case_id}/summary" in paths
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous
