"""Invented, offline memo payload and UI contracts; no canonical data required."""

import asyncio
from io import BytesIO
from types import SimpleNamespace

import pytest
from docx import Document
from starlette.datastructures import UploadFile

from backend import memo_citation_check as memo
from backend.citations import extract_statute_reference_matches
from backend.models import MemoCitationCheckResponse
from backend.pages.memo_citation_check import memo_citation_check_page_html
from backend.memo_suggestion_models import MemoAuthoritySuggestions


def make_docx(text):
    document = Document()
    document.add_paragraph(text)
    stream = BytesIO()
    document.save(stream)
    return stream.getvalue()


@pytest.mark.parametrize("text", [
    "Procedural fairness: IRPA, s. 34(1)(f), and IRPR s 245(1)(c).",
    "Paragraph 34(1)(f) of IRPA and IRPR s. 87(2)(a) are relevant.",
])
def test_real_document_extraction_reused_and_exact_nested_spans(text, caplog):
    payload = memo.analyze_memo_citations(make_docx(text), "invented.docx")
    assert payload["text"] == text
    matches = extract_statute_reference_matches(text)
    assert len(matches) == 2
    assert payload["suggestions"]["signals"]["statutes"] == sorted({
        match.normalized_citation for match in matches
    })
    for row, match in zip(payload["statute_references"], matches):
        assert row["normalized_reference"] == match.normalized_citation
        assert text[row["offset_start"]:row["offset_end"]] == row["reference_text"]
        assert "(" in row["normalized_reference"]
    assert payload["suggestions"]["status"] == "session_unavailable"
    assert MemoAuthoritySuggestions.model_validate(payload["suggestions"]).disclaimer == (
        "Suggestions, not legal advice"
    )
    assert payload["gap_suggestions"]["status"] == "session_unavailable"
    assert payload["gap_suggestions"]["disclaimer"] == (
        "Suggestions for review, not legal advice"
    )
    assert text not in caplog.text
    # No-session legacy output has no enhanced fields; do not invent them.
    assert "missing_authorities" not in payload and "memo_analysis" not in payload


def test_incomplete_nested_extraction_does_not_broaden_suggestion_signal():
    text = "IRPA s. 112(2)(b.1)"
    payload = memo.analyze_memo_citations(make_docx(text), "invented.docx")
    # Preserve the existing extraction exactly, but do not use its partial
    # subsection as an exact suggestion identity for a deeper provision.
    assert payload["statute_references"][0]["reference_text"] == "IRPA s. 112(2)"
    assert payload["suggestions"]["signals"]["statutes"] == []


def test_no_session_preserves_every_existing_analysis_field(monkeypatch):
    original = {
        "filename": "invented.docx", "text": "", "text_length": 0,
        "paragraph_count": 0, "case_citations": [], "statute_references": [],
        "summary": {"case_citations": 0}, "future_legacy_field": {"keep": True},
    }
    monkeypatch.setattr(memo, "analyze_document", lambda *args: original)
    payload = memo.analyze_memo_citations(b"invented", "invented.docx")
    assert {
        key: value for key, value in payload.items()
        if key not in {"suggestions", "gap_suggestions"}
    } == original
    assert "suggestions" not in original
    assert "gap_suggestions" not in original
    assert payload["suggestions"]["missing"] == payload["suggestions"]["contrary"] == []
    assert payload["gap_suggestions"]["status"] == "empty_memo"


def test_legacy_treatment_related_and_missing_outputs_unchanged(monkeypatch):
    cited = {"resolved_case_id": 17, "reference_text": "2020 FC 17"}
    original = {
        "filename": "invented.docx", "text": "", "text_length": 0,
        "paragraph_count": 0, "case_citations": [cited], "statute_references": [],
        "summary": {"case_citations": 1},
    }
    target = SimpleNamespace(id=17, issues=["invented issue"])
    uncited = SimpleNamespace(
        id=99, title="Invented v Canada", citation="2020 FC 99", court="FC",
        date=None, citing_cases_count=8, issues=["invented issue"],
    )

    class Query:
        def filter(self, *args):
            return self

        def first(self):
            return target

        def order_by(self, *args):
            return self

        def limit(self, *args):
            return self

        def all(self):
            return [uncited]

    session = SimpleNamespace(query=lambda *args: Query())
    treatment = {"has_treatment": True, "treatment_flags": ["positive_treatment"]}
    related = [{"id": 99, "title": "Legacy related"}]
    monkeypatch.setattr(memo, "analyze_document", lambda *args: original)
    monkeypatch.setattr(memo, "_get_treatment_status", lambda *args: treatment)
    monkeypatch.setattr(memo, "_find_related_authorities", lambda *args: related)
    payload = memo.analyze_memo_citations(b"invented", "invented.docx", session=session)
    assert payload["case_citations"] == [{**cited, "treatment": treatment,
                                        "related_authorities": related}]
    assert payload["missing_authorities"] == [{
        "id": 99, "title": "Invented v Canada", "citation": "2020 FC 99",
        "court": "FC", "date": None, "citing_count": 8, "issues": ["invented issue"],
        "reason": "Commonly cited on issues present in draft but not cited",
    }]
    assert payload["memo_analysis"] == {
        "total_authorities_cited": 1, "resolved_authorities": 1,
        "authorities_with_treatment": 1, "missing_authorities_found": 1,
    }
    assert payload["gap_suggestions"]["status"] == "empty_memo"
    assert payload["summary"] == original["summary"]
    validated = MemoCitationCheckResponse.model_validate(payload).model_dump()
    assert validated["suggestions"]["status"] == "no_signals"
    assert validated["missing_authorities"] == payload["missing_authorities"]


def test_existing_route_serializes_suggestions_without_route_change(monkeypatch):
    from backend import routes

    payload = {
        "filename": "invented.docx", "text": "Invented", "text_length": 8,
        "paragraph_count": 1, "case_citations": [], "statute_references": [],
        "missing_authorities": [],
        "memo_analysis": {"total_authorities_cited": 0, "resolved_authorities": 0,
                          "authorities_with_treatment": 0, "missing_authorities_found": 0},
        "suggestions": MemoAuthoritySuggestions(status="empty_cohort").model_dump(),
        "gap_suggestions": {"disclaimer": "Suggestions for review, not legal advice"},
    }
    monkeypatch.setattr(routes, "analyze_memo_citations", lambda *args: payload)
    result = asyncio.run(routes.memo_citation_check_analyze(
        file=UploadFile(BytesIO(b"invented"), filename="invented.docx"),
        db=SimpleNamespace(),
    ))
    assert result.model_dump()["suggestions"] == payload["suggestions"]
    assert result.model_dump()["gap_suggestions"] == payload["gap_suggestions"]


def test_page_keeps_old_sections_and_adds_safe_descriptive_renderer():
    html = memo_citation_check_page_html()
    for identifier in ("cited", "treatment", "missing", "suggestedMissing",
                       "suggestedContrary", "suggestionCoverage", "contraryHidden",
                       "memoGapSuggestions", "gapMissing", "gapContrary",
                       "gapCoverage", "gapContraryHidden"):
        assert f'id="{identifier}"' in html
    assert "Suggestions, not legal advice" in html
    assert "Suggestions for review, not legal advice" in html
    assert "renderAuthoritySuggestions(data.suggestions);" in html
    assert "renderMemoGapSuggestions(data.gap_suggestions);" in html
    assert "data.missing_authorities||[]" in html
    assert "unclassified" in html and "denominator" in html
    assert "coverage.partial" in html and "contrary_hidden_below_threshold" in html
    assert "fewer than 5 distinct citing decisions" in html
    assert "this does not establish citation completeness" in html
    assert "(why.shared_tags||[]).map(esc)" in html
    assert "(why.shared_statutes||[]).map(esc)" in html
    assert "esc(authority.title)" in html
    assert "encodeURIComponent(authority.id)" in html
    assert "localStorage" not in html and "sessionStorage" not in html
    assert html.count("renderAuthoritySuggestions(data.suggestions);") == 1
    assert html.count('id="authoritySuggestions"') == 1
