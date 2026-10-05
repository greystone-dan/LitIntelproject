from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.analytics_service import ACTIVE_TAG_TAXONOMY_VERSION, fetch_all_tag_analytics
from backend.database import Base, Case, CaseJudgeProfile, CaseTag, JudgeProfile


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


def test_tag_analytics_runs_and_groups_tags_by_judge():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(
        engine,
        tables=[Case.__table__, CaseTag.__table__, JudgeProfile.__table__, CaseJudgeProfile.__table__],
    )
    with Session(engine) as db:
        db.add(JudgeProfile(id=1, slug="zinn", display_name="Zinn", normalized_name="zinn"))
        for case_id, year in ((1, 2019), (2, 2020)):
            db.add(Case(id=case_id, title=f"A v. B {case_id}", court="FC", date=date(year, 1, 1)))
            db.add(CaseJudgeProfile(case_id=case_id, judge_profile_id=1, raw_name="Zinn J."))
            db.add(
                CaseTag(
                    case_id=case_id,
                    category="issue",
                    value="credibility",
                    score=1.0,
                    evidence="credibility",
                    source="test",
                    taxonomy_version=ACTIVE_TAG_TAXONOMY_VERSION,
                )
            )
        db.commit()
        result = fetch_all_tag_analytics(db)

    assert list(result["trends"]) == ["2020", "2019"]
    assert result["judge_tags"]["Zinn"][0]["case_count"] == 2
    assert result["frequency"][0]["value"] == "credibility"
    assert result["summary"]["unique_cases_tagged"] == 2


def test_tag_analytics_tab_is_registered_with_the_tab_router():
    from fastapi.testclient import TestClient
    from backend.main import app

    html = TestClient(app).get("/data-explorer").text
    assert "'tag-analytics':'tagAnalyticsPanel'" in html
    assert "'tag-analytics','themes'" in html
    assert "window.tgaLoadAnalytics" in html
