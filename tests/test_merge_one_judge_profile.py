import datetime

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.database import Base, Case, CaseJudgeProfile, JudgeProfile, JudgeProfileAlias
from scripts.merge_one_judge_profile import describe, problems


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in ("cases", "judge_profiles", "case_judge_profiles", "judge_profile_aliases")])
	with Session(engine) as session:
		for i in (1, 2):
			session.add(Case(id=i, title=f"Case {i}", citation=f"2020 FC {i}", court="FC", full_text="x", date=datetime.date(2020, 1, i)))
		session.add_all([
			JudgeProfile(id=1, slug="a", display_name="Russel W. Zinn", normalized_name="russel w. zinn", primary_court="FC"),
			JudgeProfile(id=2, slug="b", display_name="Zinn", normalized_name="zinn", primary_court="FC"),
			JudgeProfile(id=3, slug="c", display_name="Zinn (CA)", normalized_name="zinn ca", primary_court="FCA"),
			JudgeProfile(id=4, slug="d", display_name="Other", normalized_name="other", primary_court="FC"),
		])
		session.flush()
		session.add_all([CaseJudgeProfile(case_id=1, judge_profile_id=1, raw_name="Zinn"), CaseJudgeProfile(case_id=2, judge_profile_id=2, raw_name="Zinn J.")])
		session.commit()
		yield session


def test_same_person_passes_and_describe_counts(db):
	assert problems(db, db.get(JudgeProfile, 2), db.get(JudgeProfile, 1)) == []
	assert describe(db, db.get(JudgeProfile, 2))["cases"] == 1


def test_refuses_other_court_other_name_and_existing_alias(db):
	assert any("courts" in p for p in problems(db, db.get(JudgeProfile, 3), db.get(JudgeProfile, 1)))
	assert any("shared name" in p for p in problems(db, db.get(JudgeProfile, 4), db.get(JudgeProfile, 1)))
	db.add(JudgeProfileAlias(alias_profile_id=2, canonical_profile_id=1, source="manual"))
	db.commit()
	assert any("already aliased" in p for p in problems(db, db.get(JudgeProfile, 2), db.get(JudgeProfile, 1)))
	assert db.scalars(select(JudgeProfileAlias)).all()
