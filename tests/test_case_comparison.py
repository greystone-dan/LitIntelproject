"""Isolated SQLite/HTTP fixtures; no production connection or classification."""

from datetime import date, datetime
from html import escape
import re
import subprocess
import shutil

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, event, update
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.case_comparison import fetch_case_comparison
from backend.database import Base, Case, CaseChunk, CaseOutcome, CaseTag, Citation, StatuteReference
from backend.case_compare import compare_case_inputs
from backend.legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from backend.pages.case_compare import case_compare_page_html
from backend.pages.data_explorer import data_explorer_page_html


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    Base.metadata.create_all(engine, tables=[
        model.__table__ for model in (Case, CaseOutcome, CaseTag, Citation, StatuteReference, CaseChunk)
    ])
    with Session(engine) as session:
        session.add_all([
            Case(id=1, title='<script>alert("case")</script>', citation="2024 FC 1",
                 court="FC", date=date(2024, 1, 1),
                 metadata_json={"reader_extracted": {
                     "judge": "<b>Judge A</b>", "decision outcome": "dismissed"}}),
            Case(id=2, title="Case B", citation="2024 FCA 2", court="FCA", date=date(2024, 2, 2),
                 metadata_json={"reader_extracted": {
                     "decision outcome": " Novel  LABEL ",
                     "_field_sources": {"decision outcome": {"derived": " Novel  LABEL "}},
                     "_field_confidence": {"decision outcome": .4}}}),
            Case(id=3, title="Empty", court="FC", date=date(2024, 1, 1), metadata_json={}),
            Case(id=100, title="Authority", citation="2019 SCC 65", court="SCC", date=date(2019, 1, 1)),
            Case(id=101, title="Other authority", citation="2000 FC 9", court="FC", date=date(2000, 1, 1)),
        ])
        session.flush()
        session.add_all([
            CaseOutcome(case_id=1, classifier_version="old", decision_outcome="dismissed",
                        updated_at=datetime(2024, 1, 1)),
            CaseOutcome(case_id=1, classifier_version="v2", decision_outcome="allowed",
                        updated_at=datetime(2025, 1, 1)),
            CaseOutcome(case_id=1, classifier_version="reviewed", decision_outcome="Novel assignment",
                        source="manual_review", confidence=.9, outcome_status="undetermined",
                        disposition_evidence="<img src=x onerror=alert(1)>",
                        evidence_offset_start=10, evidence_offset_end=20,
                        updated_at=datetime(2025, 1, 1)),
        ])
        for case_id, category, value, taxonomy in (
            (1, "issue", "fairness", ACTIVE_TAG_TAXONOMY_VERSION),
            (1, "issue", "fairness", ACTIVE_TAG_TAXONOMY_VERSION),
            (2, "issue", "fairness", ACTIVE_TAG_TAXONOMY_VERSION),
            (1, "legal_area", "immigration", ACTIVE_TAG_TAXONOMY_VERSION),
            (2, "issue", "unique b", ACTIVE_TAG_TAXONOMY_VERSION),
            (1, "issue", "obsolete", "old"),
        ):
            session.add(CaseTag(case_id=case_id, category=category, value=value,
                                score=1, evidence="test", source="fixture", taxonomy_version=taxonomy))
        for source, target, normalized, raw, kind in (
            (1, 100, "alias a", "paragraph 1", "case"),
            (1, 100, "alias b", "paragraph 2", "case"),
            (2, 100, "canonical", "other spelling", "case"),
            (1, None, " 2000   FC 9 ", "first mention", "case"),
            (1, None, None, "2000 fc 9", "case"),
            (2, None, "2000 fc 9", "shared", "unknown"),
            (2, 101, "2000 FC 9", "resolved distinct from unresolved", "case"),
            (1, None, None, None, "unknown"),
            (1, None, "not a case", "statute text", "statute"),
            (1, None, "not a case either", "statute text", "statute_short"),
        ):
            session.add(Citation(source_case_id=source, target_case_id=target,
                                 normalized_citation=normalized, citation_text=raw, citation_kind=kind))
        for source, instrument, pinpoint, section, subsection in (
            (1, "IRPA", "96", None, None),
            (1, " irpa ", "96", None, None),
            (2, "irpa", None, "96", None),
            (1, "IRPR", "96", None, None),
            (2, "IRPA", "97(1)", None, None),
            (2, "IRPA", None, "97", "1"),
        ):
            session.add(StatuteReference(source_case_id=source, instrument_key=instrument,
                                        pinpoint=pinpoint, provision_section=section,
                                        provision_subsection=subsection, reference_kind="statute"))
        session.commit()
        yield session
    engine.dispose()


def test_distinct_shared_unique_and_separate_signals(db):
    result = fetch_case_comparison(db, 1, 2)
    assert result["status"] == "ok"
    for section in ("tags", "statutes"):
        assert result[section]["counts"] == {
            "a": 2, "b": 2, "shared": 1, "unique_a": 1, "unique_b": 1}
    assert result["authorities"]["counts"] == {
        "a": 2, "b": 3, "shared": 2, "unique_a": 0, "unique_b": 1}
    authorities = result["authorities"]["items"]
    assert next(row for row in authorities if row["target_case_id"] == 100)["shared"]
    assert not next(row for row in authorities if row["target_case_id"] == 101)["shared"]
    assert next(row for row in authorities if not row["resolved"])["label"] == "2000 fc 9"
    assert "obsolete" not in str(result["tags"])
    assert {row["label"] for row in result["statutes"]["items"]} == {"irpa 96", "irpr 96", "irpa 97(1)"}
    assert result["cases"]["a"]["judge"] == "<b>Judge A</b>"
    assert result["cases"]["a"]["url"] == "/data-explorer?case_id=1"


def test_latest_assignment_unknown_raw_and_metadata_fallback(db):
    result = fetch_case_comparison(db, 1, 2)
    a, b = (result["cases"][side]["outcome"] for side in ("a", "b"))
    assert a["label"] == b["label"] == "unclassified"
    assert a["raw_label"] == "Novel assignment"  # no conflicting metadata fallback
    assert a["provenance"]["storage"] == "case_outcomes"
    assert a["provenance"]["classifier_version"] == "reviewed"
    assert a["provenance"]["source"] == "manual_review"
    assert a["provenance"]["confidence"] == .9
    assert a["provenance"]["evidence_offset_start"] == 10
    assert b["raw_label"] == " Novel  LABEL "
    assert b["provenance"]["storage"] == "metadata_fallback"
    assert b["provenance"]["field_sources"] == {"derived": " Novel  LABEL "}
    db.execute(update(CaseOutcome).where(CaseOutcome.classifier_version == "reviewed")
               .values(decision_outcome=None))
    missing = fetch_case_comparison(db, 1, 2)["cases"]["a"]["outcome"]
    assert missing["label"] == "unclassified" and missing["raw_label"] is None
    assert missing["provenance"]["storage"] == "case_outcomes"


def test_unresolved_full_and_short_pinpoints_share_stored_authority(db):
    for source, kind, normalized, raw, anchor in (
        (1, "case", "Alpha v Beta, 2000 FC 9, at para. 1", "full at 1", None),
        (1, "neutral", "2000 FC 9, at para. 2", "full at 2", None),
        (2, "case", None, "Other party label, 2000 FC 9 at paras. 3-4", None),
        (1, "case_short", "Alpha, at para. 5", "Alpha at 5",
         "Alpha v Beta, 2000 FC 9, at para. 1"),
        (1, "case_short", "Different alias, at para. 6", "Different alias at 6",
         "Alpha v Beta, 2000 FC 9, at para. 2"),
        (2, "case_short", "Alpha, at p. 7", "Alpha at 7", "2000 FC 9"),
    ):
        db.add(Citation(source_case_id=source, citation_kind=kind,
                        normalized_citation=normalized, citation_text=raw,
                        anchor_citation_text=anchor))
    db.commit()
    result = fetch_case_comparison(db, 1, 2)
    assert result["authorities"]["counts"] == {
        "a": 2, "b": 3, "shared": 2, "unique_a": 0, "unique_b": 1}
    unresolved = [row for row in result["authorities"]["items"] if not row["resolved"]]
    assert len(unresolved) == 1
    assert unresolved[0]["label"] == "2000 fc 9" and unresolved[0]["shared"]
    assert next(row for row in result["authorities"]["items"]
                if row["target_case_id"] == 101)["resolved"]
    assert "Only case_short" in result["semantics"]["authorities"]
    assert not db.dirty and not db.deleted


def test_unresolved_reporter_pinpoints_and_party_labels(db):
    for source, label in (
        (1, "Alpha v Beta, [1999] 2 S.C.R. 817, at para. 1"),
        (1, "[1999] 2 SCR 817, at pp. 820-821"),
        (2, "Other party label, (1999) 2 S. C. R. 817, at para. 2"),
    ):
        db.add(Citation(source_case_id=source, citation_kind="case",
                        normalized_citation=label))
    db.commit()
    result = fetch_case_comparison(db, 1, 2)["authorities"]
    assert result["counts"] == {
        "a": 3, "b": 4, "shared": 3, "unique_a": 0, "unique_b": 1}
    reporter = next(row for row in result["items"] if row["label"] == "1999 2 scr 817")
    assert reporter["shared"] and not reporter["resolved"] and reporter["url"] is None


def test_unresolved_label_fallback_is_conservative_and_anchor_only_for_short(db):
    for kind, label, anchor in (
        ("case_name", "Alpha v Beta, at para. 1", "1990 FC 123"),
        ("case_name", "Alpha v Beta at pp. 2-3", None),
        ("case_short", "Alias, at para. 4", "Alpha v Beta, at para. 2"),
        ("case_short", "Other alias, at p. 5", "Alpha v Beta"),
        ("case_name", "Page 1", None),
        ("case_name", "Page 2", None),
        ("case_name", "Alpha v Paragraph 1 Ltd", None),
        ("case_name", "Alpha v Paragraph 2 Ltd", None),
        ("case_name", "Alpha v Beta at para. jurisdiction", None),
    ):
        db.add(Citation(source_case_id=3, citation_kind=kind,
                        normalized_citation=label, anchor_citation_text=anchor))
    db.commit()
    result = fetch_case_comparison(db, 3, 3)["authorities"]
    assert result["counts"] == {
        "a": 6, "b": 6, "shared": 6, "unique_a": 0, "unique_b": 0}
    assert {row["label"] for row in result["items"]} == {
        "alpha v beta", "page 1", "page 2", "alpha v paragraph 1 ltd",
        "alpha v paragraph 2 ltd", "alpha v beta at para. jurisdiction",
    }


def test_nested_statute_provisions_keep_instruments_ranges_and_lists_distinct(db):
    for source, instrument, pinpoint in (
        (1, "IRPA", "34(1)(f)"),
        (1, "IRPA", "34 (1) (F)"),
        (2, "IRPA", "34 (1) (F)"),
        (1, "IRPR", "34 (1) (F)"),
        (1, "IRPA", "34(1)(f)-34(1)(g)"),
        (1, "IRPA", "34(1)(f), 34(1)(g)"),
        (2, "IRPA", "34 (1) (F) - 34 (1) (G)"),
        (2, "IRPA", "34 (1) (F), 34 (1) (G)"),
    ):
        db.add(StatuteReference(source_case_id=source, instrument_key=instrument,
                               pinpoint=pinpoint, provision_section="34",
                               provision_subsection="1", provision_paragraph="f",
                               reference_kind="statute"))
    # Structured storage must share the same nested identity as the pinpoint.
    db.add(StatuteReference(source_case_id=2, instrument_key="IRPA",
                           provision_section="34", provision_subsection="1",
                           provision_paragraph="F", reference_kind="statute"))
    db.commit()
    result = fetch_case_comparison(db, 1, 2)["statutes"]
    assert result["counts"] == {
        "a": 6, "b": 5, "shared": 4, "unique_a": 2, "unique_b": 1}
    nested = [row for row in result["items"] if row["provision"].startswith("34")]
    assert {row["label"] for row in nested} == {
        "irpa 34(1)(f)", "irpr 34(1)(f)",
        "irpa 34(1)(f)-34(1)(g)", "irpa 34(1)(f),34(1)(g)",
    }
    assert all(row["shared"] == (row["instrument_key"] == "irpa") for row in nested)


@pytest.mark.parametrize("label", ["allowed", "dismissed", "mixed", "withdrawn", "set_aside", "remitted"])
def test_known_stored_labels_are_not_reclassified(db, label):
    db.execute(update(CaseOutcome).where(CaseOutcome.classifier_version == "reviewed")
               .values(decision_outcome=label))
    assert fetch_case_comparison(db, 1, 2)["cases"]["a"]["outcome"]["label"] == label


def test_unresolved_statutes_use_normalized_label_and_ignore_empty_rows(db):
    for source, normalized, raw in (
        (1, "  Unknown   Act s. 3 ", "first"),
        (1, None, "unknown act s. 3"),
        (2, "unknown act s. 3", "shared"),
        (1, None, None),
    ):
        db.add(StatuteReference(source_case_id=source, normalized_reference=normalized,
                               reference_text=raw, reference_kind="statute"))
    db.commit()
    result = fetch_case_comparison(db, 1, 2)["statutes"]
    assert result["counts"] == {"a": 3, "b": 3, "shared": 2, "unique_a": 1, "unique_b": 1}
    row = next(item for item in result["items"] if item["instrument_key"] is None)
    assert row["label"] == "unknown act s. 3" and row["shared"]


@pytest.mark.parametrize("metadata", [None, [], {"reader_extracted": []}, {"reader_extracted": "bad"}])
def test_malformed_metadata_is_unclassified(db, metadata):
    db.execute(update(Case).where(Case.id == 3).values(metadata_json=metadata))
    result = fetch_case_comparison(db, 3, 3)
    assert result["cases"]["a"]["outcome"]["label"] == "unclassified"
    assert result["cases"]["a"]["outcome"]["raw_label"] is None


def test_unknown_empty_same_and_swapped(db):
    assert fetch_case_comparison(db, 999, 998) == {
        "status": "unknown_case", "unknown_ids": [999, 998]}
    assert fetch_case_comparison(db, 999, 999)["unknown_ids"] == [999]
    empty = fetch_case_comparison(db, 3, 3)
    assert empty["cases"]["a"] == empty["cases"]["b"]
    assert empty["tags"]["items"] == empty["authorities"]["items"] == empty["statutes"]["items"] == []
    same = fetch_case_comparison(db, 1, 1)
    assert all(row["shared"] for row in same["authorities"]["items"])
    forward, backward = fetch_case_comparison(db, 1, 2), fetch_case_comparison(db, 2, 1)
    assert forward["cases"]["a"] == backward["cases"]["b"]
    assert backward["authorities"]["counts"]["unique_a"] == 1


def test_only_selects_and_no_autoflush(db):
    pending = Case(title="Pending", court="FC", date=date(2025, 1, 1))
    db.add(pending)
    statements = []

    def capture(connection, cursor, statement, parameters, context, executemany):
        statements.append(statement)

    event.listen(db.bind, "before_cursor_execute", capture)
    try:
        fetch_case_comparison(db, 1, 2)
        fetch_case_comparison(db, 999, 2)
    finally:
        event.remove(db.bind, "before_cursor_execute", capture)
    assert statements and all(sql.lstrip().upper().startswith("SELECT") for sql in statements)
    assert pending in db.new and pending.id is None
    assert not db.dirty and not db.deleted


def test_renderer_escaping_page_and_search_contract(db):
    html = case_compare_page_html(fetch_case_comparison(db, 1, 2))
    assert '<script>alert("case")</script>' not in html
    assert "&lt;script&gt;" in html and "&lt;b&gt;Judge A&lt;/b&gt;" in html
    assert "<img src=x" not in html and "&lt;img" in html
    assert 'href="/data-explorer?case_id=1"' in html
    assert 'href="/data-explorer?case_id=100"' in html
    assert "Assignment provenance" in html and "metadata_fallback" in html
    assert "raw label:  Novel  LABEL " in html
    assert "Distinct counts: A 2; B 3; shared 2; unique A 0; unique B 1" in html
    assert "Unique B" in html and "(unresolved)" in html
    assert "search-a" in html and "search-b" in html
    assert "/analytics/search/cases?" in html
    assert "row.case_id" in html and "data.results" in html
    assert "search_full_text:'false'" in html
    assert "textContent" in html and "innerHTML" not in html
    assert "AbortController" in html and "current !== sequence" in html
    assert '@media(max-width:760px)' in html
    assert 'min-width:0;overflow-wrap:anywhere' in html
    node = shutil.which("node")
    if node:
        script = re.search(r"<script>(.*?)</script>", html, re.I | re.S).group(1)
        checked = subprocess.run([node, "--check"], input=script, text=True, capture_output=True)
        assert checked.returncode == 0, checked.stderr


def _signal_columns(html, section):
    block = re.search(rf'<section id="signals-{section}">(.*?)</section>', html, re.S).group(1)
    assert '<div class="pair">' in block
    return {
        side: re.search(rf'<div data-side="{side}">(.*?)</div>', block, re.S).group(1)
        for side in ("a", "b")
    }


def test_renderer_per_case_signals_and_highlights_preserve_union(db):
    result = fetch_case_comparison(db, 1, 2)
    html = case_compare_page_html(result)
    for section in ("tags", "statutes", "authorities"):
        columns = _signal_columns(html, section)
        for side, column in columns.items():
            assert f"<h3>Case {side.upper()}</h3>" in column
            assert column.count("<li ") == result[section]["counts"][side]
            for item in result[section]["items"]:
                label = escape(item["label"], quote=True)
                assert (label in column) == item[f"in_{side}"]
                if item[f"in_{side}"]:
                    highlight = "shared" if item["shared"] else f"unique-{side}"
                    badge = "Shared" if item["shared"] else f"Unique {side.upper()}"
                    assert f'<li class="{highlight}">' in column
                    assert f'<span class="badge">{badge}</span>' in column
            assert f'class="unique-{"b" if side == "a" else "a"}"' not in column
        # Rendering duplicates shared signals visually, not in the union payload.
        assert len(result[section]["items"]) == sum(
            result[section]["counts"][key] for key in ("shared", "unique_a", "unique_b")
        )
    styles = [
        re.search(rf'\.signals \.{name}\{{([^}}]+)\}}', html).group(1)
        for name in ("shared", "unique-a", "unique-b")
    ]
    assert len(set(styles)) == 3
    for property_name in ("background", "border"):
        assert len({re.search(rf'{property_name}:([^;}}]+)', style).group(1)
                    for style in styles}) == 3


def test_renderer_signal_label_and_link_escaping(db):
    result = fetch_case_comparison(db, 1, 2)
    label = '<img src=x onerror="alert(1)"> & signal'
    url = '/data-explorer?case_id=100&extra="unsafe"'
    shared = next(item for item in result["authorities"]["items"] if item["shared"])
    shared.update(label=label, url=url)
    html = case_compare_page_html(result)
    assert label not in html and url not in html
    for column in _signal_columns(html, "authorities").values():
        assert escape(label, quote=True) in column
        assert f'href="{escape(url, quote=True)}"' in column


@pytest.mark.parametrize("a,b", [(1, 1), (3, 3), (1, 3)])
def test_renderer_same_and_empty_signal_columns(db, a, b):
    result = fetch_case_comparison(db, a, b)
    html = case_compare_page_html(result)
    for section in ("tags", "statutes", "authorities"):
        columns = _signal_columns(html, section)
        for side, column in columns.items():
            count = result[section]["counts"][side]
            assert column.count("<li ") == count
            assert ("No stored signals." in column) == (count == 0)
            if a == b:
                assert 'class="unique-' not in column
                assert column.count('class="shared"') == count
        if a == b:
            assert columns["a"].replace("Case A", "Case B") == columns["b"]


def test_http_route_precedence_validation_unknowns_and_empty_page(db, monkeypatch):
    from backend import routes
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[routes.get_db] = lambda: db
    # No startup or live DB: only an isolated router and fixture Session.
    with TestClient(app) as client:
        response = client.get("/cases/compare?a=1&b=2")
        assert response.status_code == 200
        assert response.json() == fetch_case_comparison(db, 1, 2)
        assert client.get("/cases/compare?a=1").status_code == 422
        assert client.get("/cases/compare?a=&b=2").status_code == 422
        assert client.get("/cases/compare?a=0&b=2").status_code == 422
        unknown = client.get("/cases/compare?a=999&b=2")
        assert unknown.status_code == 404
        assert unknown.json()["detail"]["unknown_ids"] == [999]
        assert client.get("/case-compare?a=999&b=2").status_code == 404
        assert client.get("/case-compare?a=bad&b=2").status_code == 422
        assert client.get("/case-compare?a=&b=").status_code == 200
        page = client.get("/case-compare?a=1&b=2")
        assert page.status_code == 200 and "Assignment provenance" in page.text
        assert '<form action="/case-compare" method="get">' in page.text
        by_citation = client.get("/api/compare?a=2024%20FC%201&b=2024%20FCA%202")
        assert by_citation.status_code == 200
        assert by_citation.json()["cases"]["a"]["case_id"] == 1
        assert by_citation.json()["fact_provenance"]["court"]["verification"] == "unverified"
        compare_page = client.get("/compare?a=2024%20FC%201&b=2024%20FCA%202")
        assert compare_page.status_code == 200
        assert '<form action="/compare" method="get">' in compare_page.text
        unresolved = client.get("/api/compare?a=not-a-case&b=2024%20FCA%202")
        assert unresolved.status_code == 404
        assert "case ID or citation" in unresolved.json()["detail"]["message"]
        assert client.get("/compare?a=not-a-case&b=2024%20FCA%202").status_code == 404
        same = client.get("/api/compare?a=1&b=2024%20FC%201")
        assert same.status_code == 400
        assert same.json()["detail"]["message"] == "Choose two different decisions to compare."
        same_page = client.get("/compare?a=1&b=2024%20FC%201")
        assert same_page.status_code == 400 and "Choose two different decisions" in same_page.text
        assert client.get("/cases/1").status_code == 200
        calls = []

        def search(database, **kwargs):
            calls.append(kwargs)
            return {"results": [{"case_id": 1, "citation": "2024 FC 1", "title": "A"}],
                    "limit": 8, "offset": 0}

        monkeypatch.setattr(routes, "fetch_analytics_search_cases", search)
        search_result = client.get("/analytics/search/cases",
                                   params={"query": "2024 FC 1", "limit": 8, "search_full_text": "false"})
        assert search_result.json()["results"][0]["case_id"] == 1
        assert calls[0]["search_full_text"] is False and calls[0]["query"] == "2024 FC 1"


def test_compare_resolution_distinct_tags_cross_citation_and_stored_pinpoints(db):
    from backend.database import CaseChunk

    chunk = CaseChunk(case_id=1, chunk_set="paragraph", chunk_index=0,
                      paragraph_start=7, paragraph_end=8, text="paragraphs 7-8",
                      text_hash="fixture", token_estimate=2)
    db.add(chunk)
    db.flush()
    db.add(Citation(source_case_id=1, target_case_id=2, citation_kind="case",
                    citation_text="2024 FCA 2 at para 12", normalized_citation="2024 FCA 2",
                    target_paragraph=12, chunk_id=chunk.id))
    db.add(Citation(source_case_id=2, target_case_id=1, citation_kind="case",
                    citation_text="2024 FC 1 at para 5", normalized_citation="2024 FC 1",
                    target_paragraph=5))
    # A matching mention without the stored resolved target must not imply A cites B.
    db.add(Citation(source_case_id=1, target_case_id=None, citation_kind="case",
                    citation_text="2024 FCA 2 at para 99", normalized_citation="2024 FCA 2",
                    target_paragraph=99))
    db.commit()

    result = compare_case_inputs(db, "2024 FC 1", "2")
    assert result["status"] == "ok"
    assert result["tags"]["counts"] == {
        "a": 2, "b": 2, "shared": 1, "unique_a": 1, "unique_b": 1,
    }
    assert result["cross_citations"]["a_cites_b"]["cites"] is True
    forward = result["cross_citations"]["a_cites_b"]["occurrences"][0]
    assert forward["target_paragraph"] == 12
    assert len(result["cross_citations"]["a_cites_b"]["occurrences"]) == 1
    assert (forward["source_paragraph_start"], forward["source_paragraph_end"]) == (7, 8)
    assert result["cross_citations"]["b_cites_a"]["occurrences"][0]["target_paragraph"] == 5
    cited_b = next(item for item in result["authorities"]["items"] if item["target_case_id"] == 2)
    assert cited_b["pinpoints_by_side"] == {"a": [12], "b": []}
    html = case_compare_page_html(result)
    assert "A cites B: Yes" in html and "B cites A: Yes" in html
    assert (
        "source occurrence paragraphs 7–8; cited decision paragraph 12"
        in html
    )
    assert "Stored cited-decision paragraph pinpoints: 12" in html
    assert "source occurrence paragraphs are taken from the citing decision" in html


def test_comparison_page_progressive_enhancement_and_reader_features_preserved(db):
    html = case_compare_page_html(None, "2024 FC 1", "", action="/compare")
    assert 'name="a" value="2024 FC 1" required' in html
    assert 'readonly' not in html
    assert '<form action="/compare" method="get">' in html
    assert 'Search citation or case name' in html

    reader = data_explorer_page_html()
    # Compatibility slice: retain keyboard help/navigation, visible highlight,
    # print pagination/citation, and existing reader panels/features.
    for marker in (
        "Compare with…", "/compare?a=${encodeURIComponent(caseId)}",
        "j</kbd> / <kbd>n", "k</kbd> / <kbd>p", "readerTypingTarget",
        "is-reader-current", "break-inside:avoid", "readerPrintCitation",
        "readerMostCited", "readerSummaryDetail", "readerCaseSummaryDetail",
        "paragraph-assessment", "is-cited-by",
    ):
        assert marker in reader
    assert ".reader-compare-link{display:none!important}" in reader
