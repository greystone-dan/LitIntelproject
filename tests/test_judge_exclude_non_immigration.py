"""Judge statistics leave out decisions explicitly labelled not_immigration; unlabelled ones stay in."""

import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.analytics_service import (
	TAXONOMY_VERSION,
	fetch_judge_comparison,
	fetch_judge_profile_by_slug,
	fetch_judge_profile_issues,
	fetch_outcomes_by_year,
)
from backend.database import Base, Case, CaseJudgeProfile, CaseTypeLabel, JudgeProfile
from backend.judge_issue_record import case_is_not_immigration


def _case(i, outcome):
	return Case(
		id=i, title=f"Case {i}", citation=f"2020 FC {i}", court="FC", full_text="x",
		date=datetime.date(2020, 1, i), issues=["fairness"],
		metadata_json={"reader_extracted": {"government outcome": outcome}},
	)


@pytest.fixture
def db():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	names = ("cases", "judge_profiles", "case_judge_profiles", "judge_profile_aliases", "citations", "case_tags", "case_type_labels")
	Base.metadata.create_all(engine, tables=[Base.metadata.tables[n] for n in names])
	with Session(engine) as session:
		# 1, 2: Minister wins; 3: Minister loss; 4: Minister win that is a tax case (flagged);
		# 5: flagged under an OLD taxonomy version only; 6: labelled as ordinary immigration.
		session.add_all([_case(1, "won"), _case(2, "won"), _case(3, "lost"), _case(4, "won"), _case(5, "lost"), _case(6, "won")])
		session.add_all([
			JudgeProfile(id=1, slug="judge-a", display_name="Judge A", normalized_name="judge a", primary_court="FC"),
			JudgeProfile(id=2, slug="judge-b", display_name="Judge B", normalized_name="judge b", primary_court="FC"),
		])
		session.flush()
		session.add_all([CaseJudgeProfile(case_id=i, judge_profile_id=1, raw_name="a") for i in range(1, 7)])
		session.add_all([CaseJudgeProfile(case_id=i, judge_profile_id=2, raw_name="b") for i in (1, 2, 3, 4)])
		session.add_all([
			CaseTypeLabel(case_id=4, taxonomy_version=TAXONOMY_VERSION, status="not_immigration"),
			CaseTypeLabel(case_id=5, taxonomy_version="old_version", status="not_immigration"),
			CaseTypeLabel(case_id=6, taxonomy_version=TAXONOMY_VERSION, status="classified", primary_type="x"),
		])
		session.commit()
		yield session


def test_profile_leaves_out_flagged_cases_and_reports_count(db):
	result = fetch_judge_profile_by_slug(db, "judge-a")
	assert result["excluded_non_immigration"] == 1
	assert sorted(d["case_id"] for d in result["decisions"]) == [1, 2, 3, 5, 6]
	assert result["outcomes"]["all_linked"] == 5
	assert result["outcomes"]["government_wins"] == 3
	assert result["outcomes"]["government_win_rate"] == 60.0


def test_profile_without_flags_reports_zero(db):
	db.query(CaseTypeLabel).delete()
	db.commit()
	result = fetch_judge_profile_by_slug(db, "judge-a")
	assert result["excluded_non_immigration"] == 0
	assert result["outcomes"]["all_linked"] == 6


def test_comparison_excludes_per_judge(db):
	result = fetch_judge_comparison(db, "judge-a", "judge-b")
	assert result["judges"]["a"]["excluded_non_immigration"] == {"count": 1, "denominator": 6}
	assert result["judges"]["a"]["decisions"]["count"] == 5
	assert result["judges"]["b"]["excluded_non_immigration"] == {"count": 1, "denominator": 4}
	assert result["judges"]["b"]["decisions"]["count"] == 3
	assert result["judges"]["b"]["outcomes"]["government_win_rate"]["percent"] == 66.7


def test_issue_record_excludes_and_reports(db):
	result = fetch_judge_profile_issues(db, "judge-a")
	assert result["excluded_non_immigration"] == 1


def test_filter_sql_uses_active_version_and_explicit_flag_only():
	sql = str(case_is_not_immigration().compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
	assert "case_type_labels" in sql and "'not_immigration'" in sql and f"'{TAXONOMY_VERSION}'" in sql


def test_outcomes_by_year_sql_has_not_exists():
	captured = {}

	class Result:
		def mappings(self):
			return self

		def all(self):
			return []

	class FakeDB:
		def execute(self, statement, params=None):
			captured["sql"] = str(statement)
			captured["params"] = params
			return Result()

	assert fetch_outcomes_by_year(FakeDB()) == []
	assert "NOT EXISTS" in captured["sql"] and "case_type_labels" in captured["sql"]
	assert captured["params"] == {"case_type_version": TAXONOMY_VERSION}
