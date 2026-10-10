"""Shared behavior between the stored-case and Live Analysis readers."""

from contextlib import nullcontext
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pytest

from backend import reader_service
from backend.case_formatter import format_decision
from backend.citation_refine.pinpoints import target_paragraphs
from backend.database import (
    Case,
    CaseChunk,
    CaseOutcome,
    CaseTypeLabel,
    Citation,
    CitationMetrics,
    StatuteReference,
)
from backend.live_analysis import paragraphs_from_pasted_text
from backend.live_reader import build_live_reader_payload
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.live_analysis import live_analysis_page_html


DECISION = (
    "Citation: Example v Canada, 2024 FC 123\n"
    "Date: 20240102\n"
    "REASONS FOR JUDGMENT\n"
    "Decision Content\n"
    "[1] The Federal Court reviews the refugee decision under the Immigration and Refugee Protection Act.\n"
    "[2] The officer applied the reasonableness standard.\n"
    "[3] Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 10, explains the test.\n"
    "[4] The provision is IRPA s. 34(1)(f).\n"
    "[5] The record supports the finding.\n"
    "[6] The application is dismissed.\n"
)


class QueryRows(list):
    def all(self):
        return list(self)


class ReaderSession:
    """A query-shaped fixture session; it never connects to a database."""

    def __init__(self, case, citations=(), statute_references=(), target_text=""):
        self.case = case
        self.citations = list(citations)
        self.statute_references = list(statute_references)
        self.target_text = target_text

    def scalar(self, statement):
        selected = statement.column_descriptions[0]["expr"]
        if selected is Case:
            return self.case
        if selected is Case.id:
            return self.case.id
        if selected is Case.full_text:
            return self.case.full_text
        if selected is CitationMetrics:
            return None
        if selected is CaseOutcome or selected is CaseTypeLabel:
            return None
        return 0

    def scalars(self, statement):
        entity = statement.column_descriptions[0]["entity"]
        return self.statute_references if entity is StatuteReference else []

    def execute(self, statement):
        entity = statement.column_descriptions[0]["entity"]
        if entity is Citation:
            return QueryRows(
                (citation, citation.target_case_id, "Vavilov v Canada", "2019 SCC 65")
                for citation in self.citations
            )
        if entity is CaseChunk:
            return QueryRows([(11, self.case.full_text)])
        if entity is Case:
            return QueryRows([(77, self.target_text)] if self.target_text else [])
        return QueryRows()

    def begin_nested(self):
        return nullcontext()


@pytest.fixture
def reader_pair(monkeypatch):
    statute_match = next(
        match for match in reader_service.extract_statute_reference_matches(DECISION)
        if "34(1)(f)" in match.citation_text
    )
    case_match = next(
        match for match in reader_service.extract_case_citation_matches(DECISION)
        if "Vavilov" in match.citation_text
    )
    case = SimpleNamespace(
        id=1,
        title="Example v Canada",
        citation="2024 FC 123",
        court="Federal Court",
        date=date(2024, 1, 2),
        full_text=DECISION,
        summary=None,
    )
    citation = SimpleNamespace(
        id=10,
        citation_kind=case_match.kind,
        chunk_id=None,
        offset_start=case_match.offset_start,
        offset_end=case_match.offset_end,
        citation_text=case_match.citation_text,
        normalized_citation=case_match.normalized_citation,
        target_case_id=77,
        target_paragraph=None,
        provenance="local",
        unresolved=False,
    )
    statute = SimpleNamespace(
        id=20,
        reference_kind=statute_match.kind,
        chunk_id=11,
        offset_start=statute_match.offset_start,
        offset_end=statute_match.offset_end,
        reference_text=statute_match.citation_text,
        normalized_reference=statute_match.normalized_citation,
        instrument_key=None,
        pinpoint=None,
        provision_section=None,
        provision_subsection=None,
        provision_paragraph=None,
        provision_is_range_or_list=False,
        legislation_url=None,
        section_text=None,
    )
    document = SimpleNamespace(title="Immigration and Refugee Protection Act", source_url=None)
    section = SimpleNamespace(section_number="34", text="(1) A person is inadmissible.")
    resolution = SimpleNamespace(
        instrument_key="canada.irpa",
        pinpoint="34(1)(f)",
        resolution_status="resolved_provision",
        document=document,
        section=section,
        provision_section="34",
        provision_subsection="(1)",
        provision_paragraph="(f)",
        provision_nested_depth=2,
        is_range_or_list=False,
    )
    monkeypatch.setattr(reader_service, "resolve_legislation_reference", lambda *_: resolution)
    monkeypatch.setattr(reader_service, "_incoming_cited_case_counts", lambda *_: {})
    session = ReaderSession(case, [citation], [statute], "Decision Content\n[10] Vavilov test.")
    case_reader = reader_service.build_case_reader_data(case.id, session, include_evidence=False)
    statute_rows = reader_service.get_case_statute_references(case.id, session)
    text, paragraphs = paragraphs_from_pasted_text(DECISION)
    live_reader = build_live_reader_payload(text, paragraphs, "Example decision")
    return case_reader, statute_rows, live_reader


def test_paragraph_numbers_anchors_and_pinpoints_match(reader_pair):
    case_reader, _, live_reader = reader_pair

    assert case_reader.format_blocks == format_decision(DECISION) == live_reader["readerData"]["format_blocks"]
    paragraph_blocks = [block for block in case_reader.format_blocks if block["type"] == "para"]
    assert [block["num"] for block in paragraph_blocks] == [1, 2, 3, 4, 5, 6]
    for block in paragraph_blocks:
        assert DECISION[block["start"]:block["end"]].startswith(f"[{block['num']}]")

    stored = case_reader.citations[0]
    live = next(row for row in live_reader["citations"] if "Vavilov" in row["citation_text"])
    assert DECISION[stored.offset_start:stored.offset_end] == stored.citation_text
    assert DECISION[live["offset_start"]:live["offset_end"]] == live["citation_text"]
    stored_pinpoint = target_paragraphs(stored.citation_text, stored.normalized_citation)
    live_pinpoint = target_paragraphs(live["citation_text"], live["normalized_citation"])
    assert stored_pinpoint.paragraphs == live_pinpoint.paragraphs == (10,)
    assert stored.target_chunk_text == "[10] Vavilov test."


def test_statute_chips_keep_instrument_pinpoint_and_exact_source_spans(reader_pair):
    _, statute_rows, live_reader = reader_pair
    stored = statute_rows[0]
    live = next(
        row for row in live_reader["citations"]
        if row["citation_kind"] == "statute" and row["pinpoint"] == "34(1)(f)"
    )

    assert (stored.instrument_key, stored.pinpoint) == ("canada.irpa", "34(1)(f)")
    assert (live["instrument_key"], live["pinpoint"]) == (stored.instrument_key, stored.pinpoint)
    span = stored.layer_spans["full_case"]
    assert DECISION[span["local_start"]:span["local_end"]] == stored.citation_text
    assert DECISION[live["offset_start"]:live["offset_end"]] == live["citation_text"]


def test_both_readers_use_the_same_hover_and_side_panel_assets():
    case_html = data_explorer_page_html()
    live_html = live_analysis_page_html()
    assets = Path(__file__).resolve().parents[1] / "backend" / "pages"
    css = (assets / "reader_v6.css").read_text(encoding="utf-8")
    js = (assets / "reader_v6.js").read_text(encoding="utf-8")

    assert css in case_html and css in live_html
    assert js in case_html and js in live_html
    for behavior in ("hoverCitationInfo", "target_pinpoint_label"):
        assert behavior in case_html and behavior in live_html
    for behavior in (
        "v6-cited",
        "['about','About'],['auth','Authorities'],['intel','Intelligence']",
        "data-v6-tab", "data-v6-find",
    ):
        assert behavior in js
