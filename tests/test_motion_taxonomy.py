from datetime import date

from scripts.classify_fc_activity import (
    ActivityEvent,
    classify_events,
    extract_procedural_events,
    validate_fc_activity_classification,
)


def event(doc_id: int, text: str) -> ActivityEvent:
    return ActivityEvent(1, "IMM-1-24", "Example v. Canada", doc_id, date(2024, 1, doc_id), text)


def test_beta_motion_subtypes_and_results_preserve_source_evidence():
    events = extract_procedural_events(
        [
            event(1, "Notice of Motion for a stay of execution of the removal order granted in part."),
            event(2, "Notice of Motion under s. 87 IRPA dismissed."),
            event(3, "Notice of Motion to intervene abandoned."),
            event(4, "Notice of Motion for production of documents."),
        ]
    )

    motion_events = [item for item in events if item["event_type"].startswith("motion")]
    assert [(item["subtype"], item["outcome"]) for item in motion_events] == [
        ("stay_removal", "granted_in_part"),
        ("s_87_irpa", "refused"),
        ("intervention", "abandoned"),
        ("production", None),
    ]
    assert all(item["doc_id"] for item in motion_events)
    assert all(item["text"] for item in motion_events)


def test_motion_subtype_preserves_unknown_category():
    extracted = extract_procedural_events([event(1, "Order on the motion dated 01-JAN-2024 granted.")])

    assert extracted[0]["subtype"] == "unknown"
    assert extracted[0]["outcome"] == "granted"


def test_validation_reports_beta_cross_field_contradictions_without_mutation():
    classification = {
        "leave_decision": {"result": "unknown", "date": "2024-04-10"},
        "leave_context": {"status": "pending"},
        "judicial_review_result": {"result": "granted"},
        "judicial_review_final_decision": {"date": "2024-04-01"},
        "history_profile": {"last_any_entry_date": "2024-04-05"},
        "procedural_events": [{"doc_id": 7}],
    }
    before = repr(classification)

    result = validate_fc_activity_classification(classification)

    assert repr(classification) == before
    assert not result["is_valid"]
    assert {issue["rule"] for issue in result["issues"]} == {
        "leave_still_pending_with_jr_result",
        "leave_date_after_jr_date",
        "leave_date_after_latest_activity",
        "leave_na_with_substantive_jr_result",
    }
    assert all(issue["evidence_doc_ids"] == [7] for issue in result["issues"])


def test_validation_accepts_pending_leave_without_review_result():
    result = validate_fc_activity_classification(
        {
            "leave_decision": {"result": "unknown", "date": None},
            "leave_context": {"status": "pending"},
            "judicial_review_result": {"result": "unknown"},
            "history_profile": {"last_any_entry_date": "2024-01-01"},
            "procedural_events": [{"doc_id": 1}],
        }
    )

    assert result == {"is_valid": True, "issues": [], "summary": "No cross-field issues found."}