from scripts.audit_fc_activity_motion_unknowns_openai import (
    build_messages,
    estimate_batch_cost,
    extract_unknown_motions,
    parse_suggestions,
)


def test_extracts_all_unknown_motion_events_and_estimates_bounded_batch():
    report = {"cases": [{"activity_case_id": 1, "classification": {"procedural_events": [
        {"event_type": "motion_filed", "subtype": "unknown", "doc_id": 2, "text": "Motion Record"},
        {"event_type": "motion_decision", "subtype": "production", "doc_id": 3, "text": "known"},
    ]}}]}
    motions = extract_unknown_motions(report)
    assert len(motions) == 1
    assert estimate_batch_cost(motions) > 0
    assert "motions" in build_messages(motions)[1]["content"]


def test_parse_suggestions_keeps_only_expected_allowed_review_values():
    expected = [{"activity_case_id": 1, "doc_id": 2, "event_type": "motion_filed"}]
    parsed = parse_suggestions(
        '{"suggestions": [{"activity_case_id": 1, "doc_id": 2, "event_type": "motion_filed", "suggested_subtype": "stay_removal", "confidence": "high", "reasoning": "explicit removal"}, {"activity_case_id": 9, "doc_id": 9, "suggested_subtype": "stay"}]}',
        expected,
    )
    assert parsed == [{"activity_case_id": 1, "doc_id": 2, "event_type": "motion_filed", "suggested_subtype": "stay_removal", "confidence": "high", "reasoning": "explicit removal"}]