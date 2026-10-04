"""Paragraph cited-by batch: signal phrases, aggregation, resumable writes, reader loaders (SQLite, no network)."""

from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, func, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import (
    Base,
    Case,
    CaseChunk,
    Citation,
    ParagraphCitationEdge,
    ParagraphCitationStatus,
)
from backend.paragraph_cited_by import (
    ALGO_VERSION,
    Occurrence,
    build_edges,
    citation_target_paragraph,
    classify_signal,
    dominant_purpose,
)
from backend.paragraph_cited_by_db import (
    compute_source_edges,
    count_pending_sources,
    load_paragraph_cited_by,
    load_target_cited_by,
    pending_source_ids,
    write_source_edges,
)


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


@pytest.mark.parametrize(
    "window, purpose",
    [
        ("The test was set out in ", "followed"),
        ("I am bound by ", "followed"),
        ("See also ", "see"),
        ("But see ", "disagreed"),
        ("I decline to follow ", "disagreed"),
        ("That case is distinguished from ", "distinguished"),
        ("It is distinguished, see ", "see"),
        ("As the Court said: \"the standard is reasonableness\" (", "quoted"),
        ("Cf. ", "compared"),
        ("The applicant also relies on a different case. Counsel cited ", "mentioned"),
        ("The Minister applied the policy. Counsel cited ", "mentioned"),
        ("", "mentioned"),
    ],
)
def test_classify_signal(window, purpose):
    assert classify_signal(window)[0] == purpose


def test_citation_target_paragraph_prefers_stored_then_text():
    assert citation_target_paragraph("2019 SCC 65 at para 12", None, 7) == 7
    assert citation_target_paragraph("2019 SCC 65 at para 12", None, None) == 12
    assert citation_target_paragraph("2019 SCC 65", None, None) is None


def test_build_edges_groups_counts_and_ignores_previous_citation():
    text = "Intro. See also AAA at para 5. Later, as held in BBB at para 5, and again BBB at para 5."
    a_end = text.index("AAA at para 5") + len("AAA at para 5")
    b1 = text.index("BBB")
    b2 = text.rindex("BBB")
    occ = [Occurrence(1, 5, text.index("AAA"), a_end), Occurrence(2, 5, b1, b1 + 13), Occurrence(2, 5, b2, b2 + 13)]
    edges = {(e.target_case_id, e.target_paragraph): e for e in build_edges(text, occ, [(o.start, o.end) for o in occ])}
    assert edges[(1, 5)].purpose == "see" and edges[(1, 5)].mentions == 1
    assert edges[(2, 5)].mentions == 2 and edges[(2, 5)].purpose == "followed"
    assert sum(edges[(2, 5)].purpose_counts.values()) == 2


def test_dominant_purpose_prefers_real_signal_over_mentioned():
    assert dominant_purpose({"mentioned": 5, "see": 1}) == "see"
    assert dominant_purpose({"mentioned": 2}) == "mentioned"
    assert dominant_purpose({"see": 1, "followed": 1}) == "followed"  # tie goes to the stronger label


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine, tables=[m.__table__ for m in (
        Case, CaseChunk, Citation, ParagraphCitationEdge, ParagraphCitationStatus)])
    with Session(engine) as session:
        session.add(Case(id=1, title="Authority", citation="2019 SCC 65", court="SCC", date=date(2019, 1, 1), full_text="x"))
        for cid, label, sentence in ((2, "2020 FC 1", "The test was applied in"), (3, "2021 FC 2", "See also")):
            full = f"Reasons. {sentence} Authority, 2019 SCC 65 at para 12. End."
            start = full.index("Authority")
            session.add(Case(id=cid, title=f"Citer {cid}", citation=label, court="FC", date=date(2020 + cid - 2, 1, 1), full_text=full))
            session.add(Citation(source_case_id=cid, target_case_id=1, citation_kind="neutral",
                                 citation_text="Authority, 2019 SCC 65 at para 12", normalized_citation="2019 SCC 65",
                                 target_paragraph=12, offset_start=start, offset_end=start + 34))
        session.add(Case(id=4, title="Self", citation="2022 FC 3", court="FC", date=date(2022, 1, 1), full_text="2019 SCC 65 at para 3"))
        session.add(Citation(source_case_id=4, target_case_id=4, citation_kind="neutral", citation_text="x",
                             normalized_citation="x", target_paragraph=3, offset_start=0, offset_end=5))
        session.commit()
        yield session


def test_batch_is_resumable_idempotent_and_covers_partially_then_fully(db):
    assert pending_source_ids(db, 0, 10) == [2, 3, 4]
    assert count_pending_sources(db) == (3, 0)
    assert load_paragraph_cited_by(db, 1) is None  # nothing processed yet

    edges, used = compute_source_edges(db, 2)
    assert used == 1 and (edges[0].target_paragraph, edges[0].purpose) == (12, "followed")
    write_source_edges(db, 2, edges)
    db.commit()
    partial = load_paragraph_cited_by(db, 1)
    assert partial["coverage"] == {"sources_total": 2, "sources_processed": 1, "complete": False}
    assert load_target_cited_by(db, [(1, 12)]) == {}  # not shown to a reader until coverage is complete

    for sid in pending_source_ids(db, 0, 10):
        edges, _ = compute_source_edges(db, sid)
        write_source_edges(db, sid, edges)
    db.commit()
    write_source_edges(db, 2, compute_source_edges(db, 2)[0])  # re-run is harmless
    db.commit()
    assert pending_source_ids(db, 0, 10) == []
    assert db.scalar(select(func.count()).select_from(ParagraphCitationEdge)) == 2  # self-citation excluded

    full = load_paragraph_cited_by(db, 1)
    assert full["coverage"]["complete"] is True
    para = full["paragraphs"][0]
    assert para["paragraph"] == 12 and para["citer_count"] == 2
    assert para["purposes"] == {"followed": 1, "see": 1}
    assert {c["case_id"] for c in para["citers"]} == {2, 3}
    assert load_target_cited_by(db, [(1, 12), (1, 99)]) == {
        (1, 12): {"citer_count": 2, "mention_count": 2, "purposes": {"followed": 1, "see": 1}}
    }


def test_algo_version_bump_makes_everything_pending_again(db, monkeypatch):
    for sid in (2, 3):
        write_source_edges(db, sid, compute_source_edges(db, sid)[0])
    db.commit()
    assert 2 not in pending_source_ids(db, 0, 10)
    monkeypatch.setattr("backend.paragraph_cited_by_db.ALGO_VERSION", ALGO_VERSION + 1)
    assert 2 in pending_source_ids(db, 0, 10)
