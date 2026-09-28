from scripts.evaluate_fc_activity_deterministic import (
    _aggregate_delay_metrics,
    _build_delay_metrics,
    _intelligence_coverage,
    _motion_coverage,
    _queryable_analytics,
    evaluate_gold_set,
    sample_case_ids,
)


def test_sample_case_ids_weights_recent_years_and_is_seeded():
    candidates = [(index, 2000 + index // 10) for index in range(100)]

    first = sample_case_ids(candidates, sample_size=20, recent_years=2, recent_share=0.7, seed=7)
    second = sample_case_ids(candidates, sample_size=20, recent_years=2, recent_share=0.7, seed=7)

    assert first == second
    assert len(first) == 20
    assert sum(candidates[index][1] >= 2008 for index in first) >= 14


def test_sample_case_ids_handles_small_or_missing_recent_pool():
    candidates = [(1, None), (2, 2001), (3, 2002)]

    selected = sample_case_ids(candidates, sample_size=10, recent_years=7, recent_share=0.7, seed=2)

    assert selected == [1, 2, 3]


def test_sample_case_ids_scales_without_quadratic_recent_membership_scan():
    candidates = [(index, 2000 + index // 100) for index in range(5000)]

    selected = sample_case_ids(candidates, sample_size=20, recent_years=2, recent_share=0.7, seed=9)

    assert len(selected) == 20


def test_build_delay_metrics_preserves_complete_and_missing_states():
    events = [
        {"event_type": "application_filed", "event_date": "2024-01-01", "date_kind": "filing_date", "doc_id": 1},
        {"event_type": "motion_filed", "event_date": "2024-02-01", "date_kind": "filing_date", "doc_id": 2},
        {"event_type": "stay", "event_date": "2024-02-01", "date_kind": "filing_date", "removal_scheduled_date": "2024-02-11", "doc_id": 2},
    ]

    metrics = _build_delay_metrics(events)
    assert metrics["filing_to_removal"]["days"] == 41
    assert metrics["motion_to_removal"]["days"] == 10

    missing = _build_delay_metrics([events[0]])
    assert missing["filing_to_removal"]["status"] == "missing_removal_date"
    assert missing["motion_to_removal"]["status"] == "missing_removal_date"


def test_aggregate_delay_metrics_reports_status_counts_and_percentiles():
    rows = [
        {"filing_to_removal": {"status": "complete", "days": 10}, "motion_to_removal": {"status": "complete", "days": 4}},
        {"filing_to_removal": {"status": "complete", "days": 20}, "motion_to_removal": {"status": "missing_anchor_date", "days": None}},
        {"filing_to_removal": {"status": "missing_removal_date", "days": None}, "motion_to_removal": {"status": "complete", "days": 8}},
    ]

    metrics = _aggregate_delay_metrics(rows)
    assert metrics["filing_to_removal"]["case_count"] == 3
    assert metrics["filing_to_removal"]["valid_count"] == 2
    assert metrics["filing_to_removal"]["coverage_rate"] == 0.6667
    assert metrics["filing_to_removal"]["status_counts"] == {"complete": 2, "missing_removal_date": 1}
    assert metrics["filing_to_removal"]["valid_delay"]["p50_days"] == 10
    assert metrics["motion_to_removal"]["status_counts"] == {"complete": 2, "missing_anchor_date": 1}


def test_motion_coverage_reports_cases_subtypes_results_and_unknowns():
    metrics = _motion_coverage(
        [
            {
                "activity_case_id": 10,
                "procedural_events": [
                    {"event_type": "motion_filed", "subtype": "production", "outcome": None, "doc_id": 1, "text": "motion", "rule": "motion_reference"},
                    {"event_type": "stay", "subtype": "stay", "outcome": None, "doc_id": 1, "text": "stay", "rule": "stay"},
                ],
            },
            {
                "activity_case_id": 11,
                "procedural_events": [
                    {"event_type": "motion_decision", "subtype": "unknown", "outcome": "granted_in_part", "doc_id": 2, "text": "motion", "rule": "motion_with_explicit_outcome"},
                ],
            },
            {"activity_case_id": 12, "procedural_events": []},
        ]
    )

    assert metrics["motion_case_count"] == 2
    assert metrics["motion_case_rate"] == 0.6667
    assert metrics["motion_event_count"] == 2
    assert metrics["subtype_counts"] == {"production": 1, "unknown": 1}
    assert metrics["result_counts"] == {"granted_in_part": 1, "unknown": 1}
    assert metrics["subtype_coverage_rate"] == 0.5
    assert metrics["result_coverage_rate"] == 0.5
    assert metrics["evidence_complete_count"] == 2


def test_intelligence_coverage_reports_judges_decision_fields_and_lifecycle():
    metrics = _intelligence_coverage(
        [
            {
                "judges": {"by_stage": {"leave": [{"name": "One"}], "final_decision": []}},
                "challenged_decision": {"decision_maker_type": "irb_refugee_or_appeal", "decision_subject": "removal_or_exclusion"},
                "lifecycle_status": {"status": "closed"},
            },
            {
                "judges": {"by_stage": {"final_decision": [{"name": "Two"}]}},
                "challenged_decision": {"decision_maker_type": "unknown", "decision_subject": "unknown"},
                "lifecycle_status": {"status": "active"},
            },
        ]
    )

    assert metrics["judge_stage_case_counts"] == {"final_decision": 1, "leave": 1}
    assert metrics["judge_stage_coverage"]["leave"] == 0.5
    assert metrics["decision_maker_type_counts"]["unknown"] == 1
    assert metrics["lifecycle_status_counts"] == {"active": 1, "closed": 1}


def test_analytics_counts_only_milestone_stages_with_known_signals():
    metrics = _queryable_analytics(
        [
            {
                "lifecycle_status": {"status": "unknown"},
                "hearing_status": {"status": "unknown"},
                "challenged_decision": {},
                "milestone_rollups": {
                    "application": {"filed": {"status": "yes"}},
                    "leave": {"result": "unknown"},
                    "motion": {"latest_decision": {"status": "unknown"}},
                },
            }
        ]
    )

    assert metrics["dimensions"]["milestone_stage"] == {"application": 1}


def test_queryable_analytics_counts_stabilized_dimensions():
    analytics = _queryable_analytics(
        [
            {
                "lifecycle_status": {"status": "active"},
                "hearing_status": {"status": "scheduled"},
                "challenged_decision": {
                    "decision_maker_type": "irb_refugee_or_appeal",
                    "underlying_tribunal_type": "irb",
                    "decision_subject": "removal_or_exclusion",
                },
                "milestone_rollups": {
                    "application": {"filed": {"status": "yes"}},
                    "hearing": {"status": "scheduled"},
                },
            }
        ]
    )

    assert analytics["dimensions"]["hearing_status"] == {"scheduled": 1}
    assert analytics["dimensions"]["underlying_tribunal_type"] == {"irb": 1}
    assert analytics["dimensions"]["milestone_stage"] == {"application": 1, "hearing": 1}


def test_evaluate_gold_set_reports_accuracy_coverage_and_disagreements():
    classifications = [
        {
            "activity_case_id": 10,
            "classification": {
                "hearing_status": {"status": "held"},
                "lifecycle_status": {"status": "closed"},
            },
        }
    ]

    metrics = evaluate_gold_set(
        classifications,
        [
            {"activity_case_id": 10, "expected": {"hearing_status.status": "held", "lifecycle_status.status": "active"}},
            {"activity_case_id": 11, "expected": {"hearing_status.status": "not_held"}},
        ],
    )

    assert metrics["field_count"] == 3
    assert metrics["covered_count"] == 2
    assert metrics["matched_count"] == 1
    assert metrics["coverage_rate"] == 0.6667
    assert len(metrics["disagreements"]) == 2