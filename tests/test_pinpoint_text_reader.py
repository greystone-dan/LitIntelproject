"""The reader data hands the markup view real paragraph text for a pinpoint, never the wrong chunk."""

from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, CaseChunk, Citation
from backend.reader_service import build_case_reader_data


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


TARGET_TEXT = (
    "Decision Content\n"
    "[1] Opening paragraph.\n"
    "[2] Second paragraph.\n"
    "[3] The test is conjunctive, so an oral hearing is generally required.\n"
    "[4] Closing paragraph.\n"
)


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all([
            Case(id=1, title="Source v. Canada", citation="2024 FC 1", court="FC", date=date(2024, 1, 1),
                 full_text="Decision Content\n[1] See Target v Canada, 2023 FC 9 at para 3.\n"),
            Case(id=2, title="Target v. Canada", citation="2023 FC 9", court="FC", date=date(2023, 1, 1),
                 full_text=TARGET_TEXT),
        ])
        session.flush()
        # Coarse chunks: one wide chunk holds paragraphs 1-4, a footer-like chunk is mislabelled as paragraph 3.
        session.add_all([
            CaseChunk(case_id=2, chunk_set="paragraph", chunk_index=0, paragraph_start=1, paragraph_end=4,
                      text=TARGET_TEXT, text_hash="wide", token_estimate=20),
            CaseChunk(case_id=2, chunk_set="paragraph", chunk_index=1, paragraph_start=3, paragraph_end=3,
                      text="SOLICITORS OF RECORD\nDOCKET: IMM-1-23", text_hash="footer", token_estimate=5),
        ])
        session.flush()
        session.add_all([
            Citation(source_case_id=1, target_case_id=2, citation_kind="case",
                     citation_text="Target v Canada, 2023 FC 9 at para 3", normalized_citation="2023 FC 9 at para 3",
                     offset_start=0, offset_end=10, target_paragraph=3),
            Citation(source_case_id=1, target_case_id=2, citation_kind="case",
                     citation_text="Target v Canada, 2023 FC 9 at para 99", normalized_citation="2023 FC 9 at para 99",
                     offset_start=20, offset_end=30, target_paragraph=99),
        ])
        session.commit()
        yield session
    engine.dispose()


def test_pinpoint_text_is_the_cited_paragraph_or_absent(db):
    rows = {row.target_paragraph: row for row in build_case_reader_data(1, db).citations}
    # Paragraph 3: the text of the stored decision, not the mislabelled footer chunk or the whole wide chunk.
    assert rows[3].target_chunk_text is not None
    assert rows[3].target_chunk_text.startswith("[3] The test is conjunctive")
    assert "SOLICITORS OF RECORD" not in rows[3].target_chunk_text
    assert "[4]" not in rows[3].target_chunk_text
    # A paragraph the cited decision does not have gets no text at all.
    assert rows[99].target_chunk_text is None


def test_on_demand_paragraph_text_and_statute_positions(db):
    from backend.database import StatuteReference
    from backend.reader_service import get_case_paragraph_texts, get_case_statute_references

    texts = get_case_paragraph_texts(2, [3, 99], db)
    assert texts["3"].startswith("[3] The test is conjunctive")
    assert "99" not in texts

    source = db.get(Case, 1)
    chunk_text = source.full_text.split("\n", 1)[1]
    db.add(CaseChunk(id=50, case_id=1, chunk_set="paragraph", chunk_index=0, paragraph_start=1, paragraph_end=1,
                     text=chunk_text, text_hash="s", token_estimate=10))
    db.flush()
    local = chunk_text.index("2023 FC 9")
    db.add(StatuteReference(source_case_id=1, chunk_id=50, offset_start=local, offset_end=local + 9,
                            reference_text="2023 FC 9", normalized_reference="x", reference_kind="statute",
                            section_text="A provision."))
    db.commit()
    row = get_case_statute_references(1, db)[0]
    span = row.layer_spans["full_case"]
    assert source.full_text[span["local_start"]:span["local_end"]] == "2023 FC 9"
    assert row.provision_text == "A provision."
