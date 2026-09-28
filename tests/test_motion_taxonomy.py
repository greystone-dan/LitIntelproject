from datetime import date

from scripts.classify_fc_activity import (
    ActivityEvent,
    classify_events,
    extract_procedural_events,
    validate_fc_activity_classification,
)


def event(doc_id: int, text: str, re_no: str | None = None) -> ActivityEvent:
    return ActivityEvent(1, "IMM-1-24", "Example v. Canada", doc_id, date(2024, 1, doc_id), text, re_no=re_no)


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


def test_motion_subtype_covers_explicit_french_and_gerund_variants():
    extracted = extract_procedural_events(
        [
            event(1, "Order staying their removal to Canada."),
            event(2, "Ordonnance accordant la requête pour jugement par consentement."),
            event(3, "Demande de sursis à l'exécution du renvoi."),
        ]
    )

    motions = [item for item in extracted if item["event_type"].startswith("motion")]
    assert [item["subtype"] for item in motions] == [
        "stay_removal",
        "consent_judgment",
        "stay_removal",
    ]


def test_motion_context_propagates_only_one_specific_subtype_within_record():
    extracted = extract_procedural_events(
        [
            event(1, "Notice of Motion to extend time to file the record.", re_no="R-1"),
            event(2, "Motion Record filed on behalf of the applicant.", re_no="R-1"),
            event(3, "Unrelated Motion Record filed.", re_no="R-2"),
            event(4, "Notice of Motion for a stay.", re_no="R-3"),
            event(5, "Another Motion Record filed.", re_no="R-3"),
        ]
    )

    motions = [item for item in extracted if item["event_type"].startswith("motion")]
    assert motions[0]["subtype"] == "extension_of_time"
    assert motions[1]["subtype"] == "extension_of_time"
    assert motions[1]["subtype_source_doc_id"] == 1
    assert motions[2]["subtype"] == "unknown"
    assert motions[3]["subtype"] == "stay"
    assert motions[4]["subtype"] == "unknown"


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