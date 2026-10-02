from datetime import date

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

import scripts.classify_fc_activity as classifier
from backend.database import FCActivityCase, FCActivityClassification, FCActivityDocument, FCActivityMotion, FCActivitySummary


@pytest.fixture()
def session_factory(monkeypatch):
    engine = create_engine("sqlite://")
    for table in (FCActivityCase.__table__, FCActivityDocument.__table__, FCActivityClassification.__table__, FCActivitySummary.__table__, FCActivityMotion.__table__):
        table.create(engine)
    factory = sessionmaker(bind=engine)
    monkeypatch.setattr(classifier, "SessionLocal", factory)
    with factory() as session:
        for index in range(1, 8):
            case = FCActivityCase(id=index, source_key=f"key-{index}", citation=f"IMM-{index}-22", year=2022)
            session.add(case)
            session.add(FCActivityDocument(case_id=index, re_no="1", docno="1", doc_dt=date(2022, 1, 3), recorded_entry="Application for leave and judicial review against a decision of the RPD filed on 03-JAN-2022"))
            session.add(FCActivityDocument(case_id=index, re_no="2", docno=None, doc_dt=date(2022, 4, 5), recorded_entry="(Final decision) Order rendered by The Honourable Mr. Justice Example at Ottawa on 05-APR-2022 dismissing the application for leave"))
        session.commit()
    return factory


@pytest.mark.parametrize("workers", [1, 2])
def test_persist_all_writes_each_case_once_and_resumes(session_factory, tmp_path, workers):
    state_file = tmp_path / "state.json"
    written = classifier.persist_all(3, state_file, workers=workers)
    assert written == 7
    with session_factory() as session:
        rows = list(session.scalars(select(FCActivityClassification).order_by(FCActivityClassification.source_case_id)))
    assert [row.source_case_id for row in rows] == list(range(1, 8))
    assert all(row.classifier_version == classifier.CLASSIFIER_VERSION for row in rows)
    assert rows[0].classification_json["leave_decision"]["result"] == "refused"
    with session_factory() as session:
        summaries = list(session.scalars(select(FCActivitySummary).order_by(FCActivitySummary.source_case_id)))
    assert [row.source_case_id for row in summaries] == list(range(1, 8))
    assert summaries[0].leave_result == "refused"
    assert summaries[0].leave_judge_key == "example"
    assert summaries[0].days_filing_to_leave_decision == 92
    assert classifier.persist_all(3, state_file, workers=workers) == 0


def test_persist_report_updates_stale_rows(session_factory):
    report = classifier.load_report(limit=2)
    assert classifier.persist_report(report) == 2
    with session_factory() as session:
        session.get(FCActivityClassification, 1).classifier_version = "old"
        session.commit()
    assert classifier.persist_report(report) == 1
    assert classifier.persist_report(report, force=True) == 2


def test_inherit_lead_outcomes_copies_the_lead_file_resolution(session_factory, tmp_path):
    classifier.persist_all(10, tmp_path / "state.json")
    with session_factory() as session:
        lead = session.get(FCActivitySummary, 1)
        lead.resolution = "judicial_review_dismissed"
        follower = session.get(FCActivitySummary, 2)
        follower.lead_file = lead.imm_number
        follower.resolution = "unknown"
        session.commit()
    assert classifier.inherit_lead_outcomes() == 1
    with session_factory() as session:
        assert session.get(FCActivitySummary, 2).lead_resolution == "judicial_review_dismissed"
    assert classifier.inherit_lead_outcomes() == 0
