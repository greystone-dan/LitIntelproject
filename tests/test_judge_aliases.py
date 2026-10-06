import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.analytics_service import _fetch_judge_profiles_impl, fetch_judge_profile_by_slug
from backend.database import Base, Case, CaseJudgeProfile, JudgeProfile, JudgeProfileAlias


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	tables = [Base.metadata.tables[n] for n in ("cases", "judge_profiles", "case_judge_profiles", "judge_profile_aliases", "citations")]
	Base.metadata.create_all(engine, tables=tables)
	with Session(engine) as session:
		for i in (1, 2, 3):
			session.add(Case(id=i, title=f"Case {i}", citation=f"2020 FC {i}", court="FC", full_text="x", date=__import__("datetime").date(2020, 1, i)))
		session.add_all([
			JudgeProfile(id=1, slug="judge-zinn", display_name="Mr. Justice Zinn", normalized_name="zinn", primary_court="FC"),
			JudgeProfile(id=2, slug="judge-simon-zinn", display_name="Simon Zinn", normalized_name="simon zinn", primary_court="FC"),
			JudgeProfile(id=3, slug="judge-other", display_name="Other", normalized_name="other", primary_court="FC"),
		])
		session.flush()
		session.add_all([
			CaseJudgeProfile(case_id=1, judge_profile_id=1, raw_name="a"),
			CaseJudgeProfile(case_id=2, judge_profile_id=2, raw_name="b"),
			CaseJudgeProfile(case_id=3, judge_profile_id=3, raw_name="c"),
		])
		session.commit()
		yield session


def test_without_aliases_nothing_changes(db):
	rows = _fetch_judge_profiles_impl(db)
	assert {r["slug"]: r["decision_count"] for r in rows} == {"judge-zinn": 1, "judge-simon-zinn": 1, "judge-other": 1}


def test_alias_merges_list_and_profile_and_is_reversible(db):
	db.add(JudgeProfileAlias(alias_profile_id=2, canonical_profile_id=1, source="rule"))
	db.commit()
	rows = {r["slug"]: r for r in _fetch_judge_profiles_impl(db)}
	assert set(rows) == {"judge-zinn", "judge-other"}
	assert rows["judge-zinn"]["decision_count"] == 2 and "Simon Zinn" in rows["judge-zinn"]["aliases"]
	via_alias = fetch_judge_profile_by_slug(db, "judge-simon-zinn")
	assert via_alias["profile"]["slug"] == "judge-zinn" and len(via_alias["decisions"]) == 2
	db.query(JudgeProfileAlias).delete()
	db.commit()
	assert len(_fetch_judge_profiles_impl(db)) == 3


def test_panel_string_profiles_are_hidden_from_the_list(db):
	db.add(JudgeProfile(id=9, slug="judge-panel", display_name="McLachlin C.J. and Abella, Rowe JJ.", normalized_name="panel", primary_court="SCC"))
	db.add(JudgeProfile(id=10, slug="judge-panel2", display_name="Wagner, Richard; Abella, Rosalie", normalized_name="panel2", primary_court="SCC"))
	db.commit()
	assert {r["slug"] for r in _fetch_judge_profiles_impl(db)} == {"judge-zinn", "judge-simon-zinn", "judge-other"}


def test_prune_keeps_rows_in_the_same_group_even_if_canonical_changed(db):
	from scripts.apply_judge_aliases import stale_rows
	db.add_all([
		JudgeProfile(id=4, slug="judge-john-a-okeefe", display_name="Mr. Justice John A. O'Keefe", normalized_name="john a o'keefe", primary_court="FC"),
		JudgeProfile(id=5, slug="judge-john-okeefe-upper", display_name="THE HONOURABLE MR. JUSTICE JOHN A. O'KEEFE", normalized_name="john a o'keefe 2", primary_court="FC"),
		JudgeProfile(id=6, slug="judge-gleason", display_name="Dawn Gleason", normalized_name="dawn gleason", primary_court="FC"),
		JudgeProfile(id=7, slug="judge-gleason-s", display_name="Simon Gleason", normalized_name="simon gleason", primary_court="FC"),
	])
	db.flush()
	for n, pid in enumerate((4, 5, 5, 6, 7), start=10):
		db.add(Case(id=n, title=f"C{n}", citation=f"c{n}", court="FC", full_text="x", date=__import__("datetime").date(2021, 1, 1)))
		db.flush()
		db.add(CaseJudgeProfile(case_id=n, judge_profile_id=pid, raw_name="x"))
	# canonical on the row (4) differs from the biggest profile (5), but both are one person: keep.
	db.add(JudgeProfileAlias(alias_profile_id=4, canonical_profile_id=5, source="rule"))
	# Two different Gleasons were once wrongly merged: remove.
	db.add(JudgeProfileAlias(alias_profile_id=7, canonical_profile_id=6, source="rule"))
	db.commit()
	assert [(r.alias_profile_id, r.canonical_profile_id) for r in stale_rows(db)] == [(7, 6)]
