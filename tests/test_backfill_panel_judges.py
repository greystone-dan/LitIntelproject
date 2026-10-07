import datetime

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, CaseJudgeProfile, JudgeProfile
from scripts.backfill_judge_profiles import normalize_judge_name
from scripts.backfill_panel_judges import backfill_panels


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "judge_profiles", "case_judge_profiles", "citations")])
	with Session(engine) as session:
		panel = lambda text: {"reader_extracted": {"judge": text}}
		for i, (court, text) in enumerate([
			("SCC", "Wagner, Richard; Abella, Rosalie Silberman; Rowe, Malcolm"),
			("SCC", "Wagner, Richard; Rowe, Malcolm; Martin, Sheilah"),
			("SCC", ""),
			("FC", "Shore J."),
		], start=1):
			session.add(Case(id=i, title=f"C{i}", citation=f"c{i}", court=court, full_text="x",
				date=datetime.date(2020, 1, i), metadata_json=panel(text)))
		session.commit()
		yield session


def test_dry_run_changes_nothing_and_apply_is_idempotent(db):
	stats = backfill_panels(db, ["SCC"])
	assert stats["panel_cases"] == 2 and stats["profiles_created"] == 4 and stats["links_would_create"] == 6
	assert db.scalar(select(JudgeProfile.id)) is None
	backfill_panels(db, ["SCC"], apply=True)
	again = backfill_panels(db, ["SCC"], apply=True)
	assert again.get("profiles_created", 0) == 0 and again.get("links_created", 0) == 0
	wagner = db.scalar(select(JudgeProfile).where(JudgeProfile.slug == "judge-richard-wagner"))
	assert wagner.display_name == "Justice Richard Wagner" and wagner.primary_court == "SCC"
	assert len(wagner.case_links) == 2
	assert db.query(CaseJudgeProfile).count() == 6


def test_same_name_profile_from_another_court_is_not_reused(db):
	db.add(JudgeProfile(slug="judge-rowe", display_name="Rowe J.", normalized_name="rowe", primary_court="FC", aliases=[]))
	db.add(Case(id=9, title="C9", citation="c9", court="SCC", full_text="x", date=datetime.date(1918, 1, 1),
		metadata_json={"reader_extracted": {"judge": "Rowe; Smith"}}))
	db.commit()
	backfill_panels(db, ["SCC"], apply=True)
	fc = db.scalar(select(JudgeProfile).where(JudgeProfile.slug == "judge-rowe"))
	assert not fc.case_links
	assert db.scalar(select(JudgeProfile).where(JudgeProfile.slug == "judge-rowe-scc")) is not None


def test_fca_bench_links_reuse_authoring_profile_and_skip_clerks(db):
	db.add(JudgeProfile(slug="judge-stratas-j-a", display_name="STRATAS J.A.", normalized_name=normalize_judge_name("STRATAS J.A."), primary_court="FCA", aliases=[]))
	db.add(Case(id=20, title="C20", citation="c20", court="FCA", full_text="x", date=datetime.date(2020, 1, 1),
		metadata_json={"reader_extracted": {"judge": "STRATAS J.A.", "present": "GAUTHIER J.A.\nSTRATAS J.A.\nLOCKE J.A.\nKARINE TURGEON, Assessment Officer"}}))
	db.commit()
	stats = backfill_panels(db, ["FCA"], apply=True)
	assert stats["profiles_created"] == 2 and stats["links_created"] == 3
	names = sorted(p.display_name for p in db.scalars(select(JudgeProfile)))
	assert names == ["GAUTHIER J.A.", "LOCKE J.A.", "STRATAS J.A."]
	assert backfill_panels(db, ["FCA"], apply=True).get("links_created", 0) == 0
