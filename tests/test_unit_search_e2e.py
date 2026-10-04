"""End-to-end test for unit search and theme discovery with judge analytics."""

import json
from datetime import date
from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from backend.database import (
    Base,
    Case,
    CaseChunk,
    CaseJudgeProfile,
    CaseOutcome,
    DiscussionUnitCache,
    JudgeProfile,
)
from backend.unit_search import (
    search_units_by_embedding,
    get_unit_judge_analytics,
    UnitSearchResult,
)


@pytest.fixture
def test_db():
    """Create an in-memory SQLite database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


def test_keyword_search_basic(test_db: Session):
    """Test basic keyword search functionality."""
    # Create judge profile first
    judge_profile = JudgeProfile(
        slug="justice-smith",
        display_name="Justice Smith",
        normalized_name="smith",
        primary_court="Federal Court",
    )
    test_db.add(judge_profile)
    test_db.flush()

    # Create test case
    case = Case(
        title="Test Case: Credibility Assessment",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2020, 1, 15),
        citation="2020 FC 100",
        docket_number="T-1234-20",
    )
    test_db.add(case)
    test_db.flush()

    # Create test chunk
    chunk = CaseChunk(
        case_id=case.id,
        chunk_set="legacy",
        chunk_index=0,
        chunk_label="Introduction",
        paragraph_start=0,
        paragraph_end=2,
        text="The applicant contests the credibility determination made by the Minister. The concept of credibility assessment is well established.",
        text_hash="abc123",
        token_estimate=20,
    )
    test_db.add(chunk)
    test_db.flush()

    # Create case-judge profile link
    case_judge = CaseJudgeProfile(
        case_id=case.id,
        judge_profile_id=judge_profile.id,
        raw_name="Justice Smith",
    )
    test_db.add(case_judge)
    test_db.flush()

    # Create outcome
    outcome = CaseOutcome(
        case_id=case.id,
        classifier_version="v1.0",
        decision_outcome="Allowed",
        outcome_status="Final",
        winner_side="Applicant",
    )
    test_db.add(outcome)
    test_db.commit()

    # Search for "credibility"
    results = search_units_by_embedding("credibility", test_db, limit=5)

    assert len(results) > 0
    assert results[0].case_id == case.id
    assert results[0].match_type == "keyword"
    assert "credibility" in results[0].key_terms or any("credibility" in t.lower() for t in results[0].key_terms)
    assert results[0].disposition == "Allowed"
    assert "Justice Smith" in results[0].judges


def test_judge_analytics_aggregation(test_db: Session):
    """Test judge analytics data aggregation."""
    # Create judge profiles first
    judge_smith = JudgeProfile(
        slug="justice-smith",
        display_name="Justice Smith",
        normalized_name="smith",
        primary_court="Federal Court",
    )
    judge_johnson = JudgeProfile(
        slug="justice-johnson",
        display_name="Justice Johnson",
        normalized_name="johnson",
        primary_court="Federal Court",
    )
    test_db.add(judge_smith)
    test_db.add(judge_johnson)
    test_db.flush()

    # Create multiple cases with different judges and outcomes
    judges_data = [
        (judge_smith.id, "Justice Smith", "Allowed", "Applicant"),
        (judge_smith.id, "Justice Smith", "Dismissed", "Respondent"),
        (judge_johnson.id, "Justice Johnson", "Allowed", "Applicant"),
        (judge_johnson.id, "Justice Johnson", "Allowed", "Applicant"),
    ]

    for i, (judge_profile_id, judge_name, outcome, winner) in enumerate(judges_data):
        case = Case(
            title=f"Test Case {i}",
            court="Federal Court",
            jurisdiction="Canada",
            date=date(2020, 1, 15 + i),
            citation=f"2020 FC {100 + i}",
            docket_number=f"T-1234-{i}",
        )
        test_db.add(case)
        test_db.flush()

        # Add case-judge profile link
        case_judge = CaseJudgeProfile(
            case_id=case.id,
            judge_profile_id=judge_profile_id,
            raw_name=judge_name,
        )
        test_db.add(case_judge)
        test_db.flush()

        # Add outcome
        case_outcome = CaseOutcome(
            case_id=case.id,
            classifier_version="v1.0",
            decision_outcome=outcome,
            outcome_status="Final",
            winner_side=winner,
        )
        test_db.add(case_outcome)
        test_db.flush()

        # Add chunk
        chunk = CaseChunk(
            case_id=case.id,
            chunk_set="legacy",
            chunk_index=0,
            chunk_label="Section",
            paragraph_start=0,
            paragraph_end=1,
            text="Test procedural fairness content",
            text_hash=f"hash_{i}",
            token_estimate=10,
        )
        test_db.add(chunk)

    test_db.commit()

    # Test judge analytics
    analytics = get_unit_judge_analytics(case_id=1, unit_index=0, db=test_db)

    assert "judges" in analytics
    assert "disposition" in analytics
    assert analytics["judges"] == ["Justice Smith"]
    assert analytics["disposition"] == "Allowed"


def test_keyword_search_with_multiple_chunks(test_db: Session):
    """Test keyword search across multiple case chunks."""
    # Create judge profile
    judge_profile = JudgeProfile(
        slug="justice-lee",
        display_name="Justice Lee",
        normalized_name="lee",
        primary_court="Federal Court",
    )
    test_db.add(judge_profile)
    test_db.flush()

    case = Case(
        title="Complex Case with Multiple Chunks",
        court="Federal Court",
        jurisdiction="Canada",
        date=date(2021, 6, 10),
        citation="2021 FC 250",
        docket_number="T-5000-21",
    )
    test_db.add(case)
    test_db.flush()

    # Add multiple chunks about procedural fairness
    chunks_text = [
        "Procedural fairness requires notice to all parties.",
        "The concept of procedural fairness has been established since common law.",
        "Procedural fairness is a fundamental principle of natural justice.",
        "The Minister failed to provide procedural fairness in this case.",
    ]

    for idx, text in enumerate(chunks_text):
        chunk = CaseChunk(
            case_id=case.id,
            chunk_set="legacy",
            chunk_index=idx,
            chunk_label=f"Section {idx}",
            paragraph_start=idx,
            paragraph_end=idx,
            text=text,
            text_hash=f"hash_{idx}",
            token_estimate=10,
        )
        test_db.add(chunk)

    # Add case-judge profile link
    case_judge = CaseJudgeProfile(
        case_id=case.id,
        judge_profile_id=judge_profile.id,
        raw_name="Justice Lee",
    )
    test_db.add(case_judge)

    # Add outcome
    outcome = CaseOutcome(
        case_id=case.id,
        classifier_version="v1.0",
        decision_outcome="Allowed",
        outcome_status="Final",
        winner_side="Applicant",
    )
    test_db.add(outcome)
    test_db.commit()

    # Search for procedural fairness
    results = search_units_by_embedding("procedural fairness", test_db, limit=10)

    assert len(results) > 0
    assert results[0].case_id == case.id
    # Should find procedural and/or fairness in key terms
    assert any(term in ["procedural", "fairness"] for term in results[0].key_terms)


def test_search_no_results(test_db: Session):
    """Test search with query that matches no documents."""
    case = Case(
        title="Unrelated Case",
        court="Provincial Court",
        jurisdiction="Canada",
        date=date(2022, 3, 5),
        citation="2022 PC 500",
        docket_number="T-9999-22",
    )
    test_db.add(case)
    test_db.flush()

    chunk = CaseChunk(
        case_id=case.id,
        chunk_set="legacy",
        chunk_index=0,
        chunk_label="Content",
        paragraph_start=0,
        paragraph_end=0,
        text="This is about property disputes and contract law.",
        text_hash="prop123",
        token_estimate=10,
    )
    test_db.add(chunk)
    test_db.commit()

    # Search for something not in the case
    results = search_units_by_embedding("credibility assessment immigration", test_db, limit=5)

    # Should return empty list or results that don't match the query
    assert len(results) == 0 or all(
        q_word in r.text.lower() for r in results
        for q_word in ["credibility", "assessment", "immigration"]
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
