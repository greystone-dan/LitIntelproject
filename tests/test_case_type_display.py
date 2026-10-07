"""Stored case types are shown in the reader; nothing is classified or sent to a model at read time."""

from datetime import date
from types import SimpleNamespace

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.case_types import TAXONOMY_VERSION
from backend.case_types.display import case_type_payload, provision_text
from backend.database import Base, Case, CaseTypeLabel
from backend.reader_service import build_case_reader_data


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


def row(**kwargs):
    base = dict(taxonomy_version=TAXONOMY_VERSION, status="classified", primary_type="inadmissibility_security",
                primary_detail="34(1)(f)", second_type=None, second_detail=None, issues=[])
    base.update(kwargs)
    return SimpleNamespace(**base)


def test_provision_text() -> None:
    assert provision_text("34(1)(f)") == "s. 34(1)(f)"
    assert provision_text("1F(b)") == "Art. 1F(b)"
    assert provision_text(None) is None


def test_payload_has_primary_second_and_provisions() -> None:
    payload = case_type_payload(row(second_type="removal_admissibility_proceedings", second_detail="44(1)"))
    assert payload["primary"]["provision"] == "s. 34(1)(f)"
    assert payload["primary"]["label"]
    assert payload["second"]["provision"] == "s. 44(1)"


@pytest.mark.parametrize("status", ["unclear", "not_immigration", "insufficient_text"])
def test_payload_is_empty_for_non_labels(status) -> None:
    assert case_type_payload(row(status=status, primary_type=None)) is None


def test_payload_ignores_other_taxonomy_versions_and_missing_rows() -> None:
    assert case_type_payload(row(taxonomy_version="case_types_v0")) is None
    assert case_type_payload(None) is None


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all([
            Case(id=1, title="A v. Canada", citation="2024 FC 1", court="FC", date=date(2024, 1, 1),
                 full_text="Decision Content\n[1] Opening paragraph.\n"),
            Case(id=2, title="B v. Canada", citation="2024 FC 2", court="FC", date=date(2024, 1, 2),
                 full_text="Decision Content\n[1] Opening paragraph.\n"),
        ])
        session.flush()
        session.add(CaseTypeLabel(case_id=1, taxonomy_version=TAXONOMY_VERSION, status="classified",
                                  primary_type="humanitarian_compassionate", primary_detail="25(1)", confidence=0.9))
        session.commit()
        yield session
    engine.dispose()


def test_reader_data_carries_the_stored_case_type_only_when_there_is_one(db) -> None:
    with_label = build_case_reader_data(1, db)
    assert with_label.case_type["primary"]["key"] == "humanitarian_compassionate"
    assert with_label.case_type["primary"]["provision"] == "s. 25(1)"
    assert build_case_reader_data(2, db).case_type is None


def test_reader_page_shows_the_case_type_chip_and_about_row() -> None:
    from pathlib import Path

    source = (Path(__file__).resolve().parents[1] / "backend" / "pages" / "data_explorer.py").read_text(encoding="utf-8")
    assert "function sideCaseTypeText" in source
    assert "rh-casetype" in source
    assert "sideFact('Case type'" in source
