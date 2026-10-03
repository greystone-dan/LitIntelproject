from datetime import date
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend.citation_refine.resolution import split_section_text
from backend.database import Statute, StatuteSection, StatuteVersion
from backend.routes import get_statute_by_code
from backend.statute_versioning import find_statute_version_at_date
from scripts.import_statutes import (
    JusticeLawsXMLClient,
    PHASE1_STATUTES,
    import_statute_from_xml,
    parse_statute_sections_from_xml,
)


FIXTURE_XML = Path(__file__).parent / "fixtures" / "statute_library" / "phase1_sample.xml"
EXPECTED_FIXTURE_SECTIONS = ("34", "35", "36")


def _fixture_root():
    return ET.parse(FIXTURE_XML).getroot()


@pytest.fixture
def statute_db(tmp_path):
    engine = create_engine(f"sqlite:///{tmp_path / 'statute-library.sqlite'}")
    for table in (Statute.__table__, StatuteVersion.__table__, StatuteSection.__table__):
        table.create(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


def _add_statute(db, instrument_key="IRPA"):
    statute = Statute(
        instrument_key=instrument_key,
        title="Immigration and Refugee Protection Act",
        short_title=instrument_key,
        jurisdiction="Federal",
        statute_type="Act",
        source="justice_laws_xml",
    )
    db.add(statute)
    db.flush()
    return statute


def _add_version(db, statute, version_number, start, end):
    version = StatuteVersion(
        statute_id=statute.id,
        version_number=version_number,
        in_force_date=date.fromisoformat(start),
        end_date=date.fromisoformat(end) if end else None,
    )
    db.add(version)
    db.flush()
    return version


def test_phase_one_scope_and_parser_fixture_count():
    root = _fixture_root()
    sections = parse_statute_sections_from_xml(root)

    assert len(PHASE1_STATUTES) == 7
    assert {key for key, info in PHASE1_STATUTES.items() if info.get("skip")} == {"Charter"}
    assert tuple(section["section_number"] for section in sections) == EXPECTED_FIXTURE_SECTIONS


@pytest.mark.parametrize(
    "instrument_key",
    [key for key, info in sorted(PHASE1_STATUTES.items()) if not info.get("skip")],
)
def test_phase_one_xml_import_stores_parser_sections_and_version_dates(statute_db, instrument_key):
    root = _fixture_root()
    statute_info = PHASE1_STATUTES[instrument_key]
    with JusticeLawsXMLClient() as client:
        metadata = client.extract_metadata_from_xml(root)
    statute = import_statute_from_xml(
        statute_db,
        instrument_key,
        statute_info,
        root,
        metadata,
    )

    assert statute is not None
    version = statute_db.query(StatuteVersion).filter_by(statute_id=statute.id).one()
    sections = (
        statute_db.query(StatuteSection)
        .filter_by(statute_version_id=version.id)
        .order_by(StatuteSection.section_number)
        .all()
    )
    assert version.in_force_date == date(2020, 4, 1)
    assert version.end_date == date(2020, 12, 31)
    assert tuple(section.section_number for section in sections) == EXPECTED_FIXTURE_SECTIONS

    section_34 = next(section for section in sections if section.section_number == "34")
    assert ("34", "1", "f") in {unit.path for unit in split_section_text("34", section_34.text)}


def test_point_in_time_lookup_selects_latest_start_in_overlap_and_returns_none_in_gaps(statute_db):
    statute = _add_statute(statute_db)
    first = _add_version(statute_db, statute, "v1", "2020-01-01", "2020-12-31")
    overlap = _add_version(statute_db, statute, "v2", "2020-07-01", "2021-06-30")
    later = _add_version(statute_db, statute, "v3", "2022-01-01", None)

    assert find_statute_version_at_date(statute_db, "IRPA", date(2019, 12, 31)) is None
    assert find_statute_version_at_date(statute_db, "IRPA", date(2020, 6, 30)).id == first.id
    assert find_statute_version_at_date(statute_db, "IRPA", date(2020, 7, 1)).id == overlap.id
    assert find_statute_version_at_date(statute_db, "IRPA", date(2020, 12, 31)).id == overlap.id
    assert find_statute_version_at_date(statute_db, "IRPA", date(2021, 6, 30)).id == overlap.id
    assert find_statute_version_at_date(statute_db, "IRPA", date(2021, 7, 1)) is None
    assert find_statute_version_at_date(statute_db, "IRPA", date(2021, 12, 31)) is None
    assert find_statute_version_at_date(statute_db, "IRPA", date(2022, 1, 1)).id == later.id


def test_as_of_api_does_not_fall_back_to_latest_version_for_a_gap(statute_db):
    statute = _add_statute(statute_db)
    _add_version(statute_db, statute, "v1", "2020-01-01", "2020-12-31")
    _add_version(statute_db, statute, "v2", "2022-01-01", None)

    with pytest.raises(HTTPException) as exc_info:
        get_statute_by_code("IRPA", as_of="2021-06-01", db=statute_db)

    assert exc_info.value.status_code == 404
