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
