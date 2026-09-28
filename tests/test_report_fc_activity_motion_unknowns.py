from scripts.report_fc_activity_motion_unknowns import build_report


def test_build_report_groups_unknown_motion_evidence_without_inference():
    report = build_report(
        {
            "report_version": "fixture",
            "sample_size_actual": 3,
            "cases": [
                {
                    "activity_case_id": 10,
                    "classification": {
                        "procedural_events": [
                            {"event_type": "motion_filed", "subtype": "unknown", "outcome": None, "doc_id": 1, "source_document_date": "2024-01-01", "text": "Motion Record containing Doc. 5"},
                            {"event_type": "motion_decision", "subtype": "unknown", "outcome": "refused", "doc_id": 2, "source_document_date": "2024-01-02", "text": "Result of Hearing: Matter dismissed"},
                        ]
                    },
                },
                {
                    "activity_case_id": 11,
                    "classification": {
                        "procedural_events": [
                            {"event_type": "motion_filed", "subtype": "unknown", "outcome": None, "doc_id": 3, "source_document_date": "2024-01-03", "text": "Urgent stay motion"},
                        ]
                    },
                },
            ],
        },
        candidate_limit=2,
    )

    assert report["unknown_motion_event_count"] == 3
    assert report["phrase_family_counts"] == {
        "generic_stay_reference": 1,
        "hearing_motion_reference": 1,
        "motion_record_reference": 1,
    }
    assert report["outcome_counts"] == {"refused": 1, "unknown": 2}
    assert len(report["candidate_matrix"]) == 2
    assert all(item["review_status"] == "unknown" for item in report["candidate_matrix"])
    assert all(item["suggested_subtype"] is None for item in report["candidate_matrix"])
    assert report["rules_promoted"] is False