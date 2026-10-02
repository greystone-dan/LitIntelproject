from datetime import date

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import backend.fc_activity_insights as insights
import scripts.classify_fc_activity as classifier
from backend.database import FCActivityCase, FCActivityClassification, FCActivityDocument, FCActivityMotion, FCActivitySummary

GRANTED = [
    ("2015-01-04", "Solicitor's certificate of service on behalf of Mario D. Bellissimo confirming service of doc 1 upon Respondent by email on 04-JAN-2015 filed on 04-JAN-2015"),
    ("2015-01-05", "Application for leave and judicial review against a decision IRB-RPD Toronto filed on 05-JAN-2015 Written reasons received by the Applicant"),
    ("2015-02-04", "Applicant's Record Number of copies received/prepared: 1 on behalf of Applicant filed on 04-FEB-2015"),
    ("2015-04-01", "Order rendered by The Honourable Madam Justice Strickland at Ottawa on 01-APR-2015 granting the application for leave fixing the hearing"),
    ("2015-06-17", "Toronto 17-JUN-2015 BEFORE The Honourable Madam Justice Strickland Language: E Before the Court: Judicial Review Result of Hearing: Matter reserved held in Court Total Duration: 1h"),
    ("2015-09-02", "(Final decision) Reasons for Judgment and Judgment dated 02-SEP-2015 rendered by The Honourable Madam Justice Strickland Matter considered with personal appearance The Court's decision is with regard to Judicial Review Result: granted Filed on 02-SEP-2015"),
]
STAY = [
    ("2014-06-01", "Application for leave and judicial review against a decision CBSA Inland Enforcement Toronto filed on 01-JUN-2014"),
    ("2014-06-25", "Notice of Motion contained within a Motion Record on behalf of Applicant returnable (but no hearing date indicated at this time) for a stay of execution of removal to Kosovo scheduled for 03-JUL-2014"),
    ("2014-06-26", "Order rendered by The Honourable Madam Justice Strickland at Toronto on 26-JUN-2014 granting the stay of execution Decision filed on 26-JUN-2014"),
]
REFUSED = [
    ("2016-01-05", "Application for leave and judicial review against a decision visa officer, High Commission of Canada filed on 05-JAN-2016"),
    ("2016-05-01", "(Final decision) Order rendered by The Honourable Madam Justice Strickland at Ottawa on 01-MAY-2016 dismissing the application for leave Decision endorsed on the record"),
]


@pytest.fixture()
def session_factory(monkeypatch, tmp_path):
    engine = create_engine("sqlite://")
    for table in (FCActivityCase.__table__, FCActivityDocument.__table__, FCActivityClassification.__table__, FCActivitySummary.__table__, FCActivityMotion.__table__):
        table.create(engine)
    factory = sessionmaker(bind=engine)
    monkeypatch.setattr(classifier, "SessionLocal", factory)
    insights._CACHE.clear()
    with factory() as session:
        for case_id, (entries, city, year) in enumerate([(GRANTED, "Toronto", 2015), (REFUSED, "Ottawa", 2016), (REFUSED, "Ottawa", 2016), (STAY, "Toronto", 2014)], start=1):
            session.add(FCActivityCase(id=case_id, source_key=f"k{case_id}", citation=f"IMM-{case_id}-{year % 100}", year=year, city_filed=city, nature="Imm - Appl. for leave & jud. review - IRB - Refugee"))
            for index, (doc_date, text) in enumerate(entries, start=1):
                session.add(FCActivityDocument(case_id=case_id, re_no=str(index), docno=str(index), doc_dt=date.fromisoformat(doc_date), recorded_entry=text))
        session.commit()
    classifier.persist_all(10, tmp_path / "state.json")
    return factory


def test_insights_summarize_rates_durations_and_breakdowns(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_insights(db)
    assert result["total_files"] == 4
    assert result["headline"]["leave_decisions"] == 3
    assert result["headline"]["leave_grant_rate"] == pytest.approx(1 / 3, abs=1e-3)
    assert result["headline"]["judicial_review_grant_rate"] == 1.0
    assert result["durations"]["days_filing_to_leave_decision"]["count"] == 3
    bodies = {row["value"]: row["count"] for row in result["breakdowns"]["decision_body"]["rows"]}
    assert bodies == {"irb_rpd": 1, "visa_office": 2, "cbsa": 1}
    reasons = {row["value"]: row["count"] for row in result["breakdowns"]["leave_refusal_reason"]["rows"]}
    assert reasons == {"not_perfected": 2, "not_applicable": 2}


def test_insights_filter_by_city(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_insights(db, city="Ottawa")
    assert result["total_files"] == 2
    assert result["headline"]["leave_grant_rate"] == 0.0


def test_judge_table_counts_leave_and_merits_decisions(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_judges(db, min_decisions=1)
    judge = next(row for row in result["judges"] if row["key"] == "strickland")
    assert judge["leave_decisions"] == 3
    assert judge["leave_grant_rate"] == pytest.approx(1 / 3, abs=1e-3)
    assert judge["jr_decisions"] == 1
    assert judge["median_days_hearing_to_judgment"] == 77
    assert judge["stay_decisions"] == 1
    assert judge["stay_grant_rate"] == 1.0


def test_motions_by_type(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_motions(db)
    stay = next(row for row in result["types"] if row["type"] == "stay_of_removal")
    assert stay["motions"] == 1
    assert stay["grant_rate"] == 1.0
    assert stay["median_days_to_ruling"] == 1
    assert stay["person_grant_rate"] == 1.0


def test_case_lookup_returns_compact_classification(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_case(db, "imm-1-15")
        assert result["classification"]["judicial_review_result"]["result"] == "granted"
        assert "procedural_events" not in result["classification"]
        with pytest.raises(HTTPException) as missing:
            insights.fetch_fc_activity_case(db, "IMM-999-20")
        assert missing.value.status_code == 404
        with pytest.raises(HTTPException) as invalid:
            insights.fetch_fc_activity_case(db, "not a number")
        assert invalid.value.status_code == 422


def test_rates_by_decision_body_and_new_breakdowns(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_insights(db)
    bodies = {row["decision_body"]: row for row in result["by_decision_body"]}
    assert bodies["irb_rpd"]["leave_grant_rate"] == 1.0
    assert bodies["visa_office"]["leave_grant_rate"] == 0.0
    assert {row["value"] for row in result["breakdowns"]["joint_applicants"]["rows"]} == {"unknown"}
    assert "days_decision_to_filing" in result["durations"]


def test_counsel_table(session_factory):
    with session_factory() as db:
        result = insights.fetch_fc_activity_counsel(db, min_files=1)
    assert result["counsel"] == [
        {
            "key": "mario-bellissimo",
            "name": "Mario D. Bellissimo",
            "files": 1,
            "leave_decisions": 1,
            "leave_grant_rate": 1.0,
            "jr_decisions": 1,
            "jr_grant_rate": 1.0,
            "resolved_by_consent": 0,
        }
    ]
