from datetime import date

import pytest

from scripts.classify_fc_activity import (
    ActivityEvent,
    CLASSIFIER_VERSION,
    _read_checkpoint,
    _write_checkpoint,
    classification_needs_update,
    classify_events,
    extract_procedural_events,
)


def event(doc_id, doc_date, text, *, docno=None, re_no=None, case_name="Example v. Canada"):
    return ActivityEvent(1, "IMM-1-24", case_name, doc_id, date.fromisoformat(doc_date), text, re_no=re_no, docno=docno)


def test_classification_skip_requires_force_for_current_version():
    assert not classification_needs_update(CLASSIFIER_VERSION)
    assert classification_needs_update(CLASSIFIER_VERSION, force=True)
    assert classification_needs_update("fc_activity_v4")
    assert classification_needs_update(None)


def test_checkpoint_is_atomic_and_version_bound(tmp_path):
    state_file = tmp_path / "state.json"
    _write_checkpoint(state_file, last_source_case_id=42, written=39)

    assert _read_checkpoint(state_file) == {
        "classifier_version": CLASSIFIER_VERSION,
        "last_source_case_id": 42,
        "written": 39,
        "updated_at": _read_checkpoint(state_file)["updated_at"],
    }
    assert not state_file.with_suffix(".json.tmp").exists()


def test_extracts_repeatable_procedural_events_with_source_evidence():
    events = extract_procedural_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed on 03-JAN-2024 before Justice Marie Tremblay."),
            event(2, "2024-02-01", "Motion to stay removal filed."),
            event(3, "2024-02-10", "Order granting the motion to stay removal."),
            event(4, "2024-06-01", "(Final decision) Reasons for Judgment and Judgment rendered."),
        ]
    )

    assert [(item["event_type"], item["outcome"]) for item in events if item["event_type"].startswith("motion")] == [
        ("motion_filed", None),
        ("motion_decision", "granted"),
    ]
    assert any(item["event_type"] == "application_filed" for item in events)
    assert any(item["event_type"] == "decision" for item in events)
    judge = next(item for item in events if item["event_type"] == "judge_identified")
    assert judge["rule"] == "judge_name:Marie Tremblay"
    assert judge["judge_name"] == "Marie Tremblay"
    assert next(item for item in events if item["event_type"] == "application_filed")["date_kind"] == "filing_date"


def test_reports_binary_motion_presence_with_event_evidence():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Notice of Motion for an extension of time filed."),
        ]
    )

    assert result["motion_presence"]["status"] == "yes"
    assert result["motion_presence"]["event_count"] == 1
    assert result["motion_presence"]["doc_ids"] == [2]


def test_reports_no_motion_when_no_motion_event_is_detected():
    result = classify_events([event(1, "2024-01-02", "Application for leave and judicial review filed.")])

    assert result["motion_presence"] == {
        "status": "no",
        "event_count": 0,
        "doc_ids": [],
        "rule": "no_procedural_motion_event",
    }


def test_extracts_conservative_aljr_filer_and_respondent_minister_from_case_name():
    individual = classify_events(
        [event(1, "2024-01-02", "Application for leave and judicial review filed.", case_name="Maria Silva v. MCI")]
    )
    government = classify_events(
        [event(1, "2024-01-02", "Application for leave and judicial review filed.", case_name="Minister of Public Safety v. MCI")]
    )
    organization = classify_events(
        [event(1, "2024-01-02", "Application for leave and judicial review filed.", case_name="Example Union v. MPSEP")]
    )

    assert individual["aljr_filer_type"] == "individual"
    assert individual["respondent_minister"] == "MCI/IRCC"
    assert government["aljr_filer_type"] == "government"
    assert government["respondent_minister"] == "MCI/IRCC"
    assert organization["aljr_filer_type"] == "organization"
    assert organization["respondent_minister"] == "MPSEP/CBSA"


def test_links_motion_filing_description_to_referenced_decision():
    events = extract_procedural_events(
        [
            event(1, "2024-02-01", "Notice of Motion for an extension of time to perfect the application record filed.", docno="5.0"),
            event(2, "2024-02-05", "Written representations contained within a Motion Record in support of Doc. 5 filed."),
            event(3, "2024-02-10", "Motion Doc. No. 5 on behalf of Applicant Result of Hearing: Matter granted."),
            event(4, "2024-02-11", "Motion Doc. No. 6 on behalf of Applicant Result of Hearing: Matter granted."),
        ]
    )

    motions = [item for item in events if item["event_type"].startswith("motion")]
    assert [(item["motion_reference"], item["subtype"]) for item in motions] == [
        ("5", "extension_of_time"),
        ("5", "extension_of_time"),
        ("5", "extension_of_time"),
        ("6", "unknown"),
    ]
    assert motions[1]["subtype_source_doc_id"] == 1
    assert motions[0]["motion_reference_source"] == "docno"
    assert motions[1]["motion_reference_source"] == "text"


def test_extracts_served_notice_of_appearance_without_matching_personal_appearance():
    events = extract_procedural_events(
        [
            event(1, "1998-10-02", "Notice of appearance on behalf of the respondent filed on 02-OCT-1998 with proof of service."),
            event(2, "1998-10-03", "Order considered without personal appearance."),
        ]
    )

    appearance = next(item for item in events if item["event_type"] == "appearance_filed")
    assert appearance["subtype"] == "notice_of_appearance"
    assert appearance["rule"] == "notice_of_appearance"
    assert not any(item["event_type"] == "appearance_filed" and item["doc_id"] == 2 for item in events)


def test_aggregates_judges_by_procedural_stage_with_source_evidence():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed before Justice Leave Name."),
            event(2, "2024-02-01", "Notice of Motion before Justice Motion Name."),
            event(3, "2024-06-01", "(Final decision) Reasons for Judgment rendered by Justice Final Name."),
        ]
    )

    judges = result["judges"]
    assert judges["status"] == "yes"
    assert {item["name"] for item in judges["by_stage"]["leave"]} == {"Leave Name"}
    assert {item["name"] for item in judges["by_stage"]["motion"]} == {"Motion Name"}
    assert {item["name"] for item in judges["by_stage"]["final_decision"]} == {"Final Name"}
    assert all(item["doc_id"] for item in judges["observations"])


def test_final_decision_judge_takes_precedence_over_leave_wording():
    result = classify_events(
        [event(1, "2024-06-01", "Final decision rendered by Justice Final Name at Ottawa dismissing the application for leave.")]
    )

    assert {item["name"] for item in result["judges"]["by_stage"]["final_decision"]} == {"Final Name"}
    assert "leave" not in result["judges"]["by_stage"]


def test_recognizes_unparenthesized_french_final_decision_marker():
    result = classify_events(
        [
            event(
                1,
                "2016-05-06",
                "Jugement en date du 06-MAI-2016 rendu par Madame le juge St-Louis La décision de la Cour concerne le contrôle judiciaire Résultat : affaire accordée Décision finale",
            )
        ]
    )

    assert result["final_decision"]["status"] == "yes"
    assert result["final_decision"]["date"] == "2016-05-06"


def test_does_not_treat_rejected_underlying_decision_as_judicial_review_result():
    result = classify_events(
        [
            event(
                1,
                "2015-04-10",
                "Demande d'autorisation et de contrôle judiciaire contre la décision de CIC rejetant la demande de résidence permanente, rendue le 20-MAR-2015 dans le dossier 2178-6472 déposée le 10-AVR-2015.",
            )
        ]
    )

    assert result["judicial_review_result"]["result"] == "unknown"


def test_does_not_treat_motion_order_language_as_judicial_review_result():
    result = classify_events(
        [
            event(
                1,
                "2016-02-01",
                "Order dated 01-FEB-2016 rendered by Justice Heneghan The Court's decision is with regard to Motion in writing. Result: granted the motion be granted and further that the applicant be removed as an Applicant in this application for leave and judicial review. Interlocutory Decision",
            )
        ]
    )

    assert result["judicial_review_result"]["result"] == "unknown"


def test_extracts_rendered_decision_date_and_judge_name():
    events = extract_procedural_events(
        [event(1, "2025-01-23", "(Final decision) Order rendered by The Honourable Madam Justice Strickland at Ottawa on 23-JAN-2025 dismissing the application for leave.")]
    )

    decision = next(item for item in events if item["event_type"] == "decision")
    assert decision["event_date"] == "2025-01-23"
    assert decision["date_kind"] == "event_date"
    assert decision["judge_name"] == "Strickland"


def test_extracts_chief_and_associate_justice_titles():
    events = extract_procedural_events(
        [
            event(1, "2024-01-02", "Order rendered by Chief Justice Crampton at Ottawa on 01-FEB-2024."),
            event(2, "2024-01-03", "Order rendered by Associate Justice Smith at Vancouver on 02-FEB-2024."),
        ]
    )

    assert events[0]["judge_name"] == "Crampton"
    assert events[1]["judge_name"] == "Smith"


def test_extracts_vba_high_recall_judge_title_variants():
    events = extract_procedural_events(
        [
            event(1, "2024-01-02", "Ordonnance rendue par Madame la juge Bédard à Ottawa le 21-AVR-2024."),
            event(2, "2024-01-03", "Order rendered by Acting Chief Justice Noël at Ottawa on 29-JUN-2024."),
            event(3, "2024-01-04", "Order rendered by Roger Lafrenière, Esq., Prothonotary at Vancouver on 03-JUN-2024."),
            event(4, "2024-01-05", "Written directions received from The Honourable Madam Justice Gagné dated 05-OCT-2024."),
            event(5, "2024-01-06", "Ordonnance rendu(e) par Richard Morneau, protonotaire à Montréal le 10-NOV-2024."),
            event(6, "2024-01-07", "Oral directions of the Court: Kevin Aalto, Prothonotary dated 09-SEP-2024."),
        ]
    )

    assert [item["judge_name"] for item in events] == [
        "Bédard", "Noël", "Roger Lafrenière", "Gagné", "Richard Morneau", "Kevin Aalto"
    ]


def test_leave_decision_prefers_rendered_order_date_over_later_registry_filing_date():
    events = extract_procedural_events(
        [
            event(
                1,
                "2006-01-12",
                "(Final decision) Order rendered by The Honourable Mr. Justice Pinard at Vancouver on 11-JAN-2006 dismissing the application for leave Decision filed on 12-JAN-2006.",
            )
        ]
    )

    leave = next(item for item in events if item["event_type"] == "leave_decision")
    assert leave["event_date"] == "2006-01-11"
    assert leave["date_kind"] == "event_date"
    assert leave["filing_date"] == "2006-01-12"
    assert leave["outcome"] == "refused"
    assert leave["judge_name"] == "Pinard"


def test_hearing_negation_is_not_classified_as_hearing_held():
    result = classify_events([event(1, "2025-01-23", "Hearing proceeded without personal appearance of the parties.")])

    assert result["hearing_held"]["status"] == "unknown"
    assert result["hearing_status"]["status"] == "not_held"
    assert not any(item["event_type"] == "hearing" for item in result["procedural_events"])


def test_hearing_status_distinguishes_scheduled_held_reserved_and_french_not_held():
    results = [
        classify_events([event(1, "2025-01-23", "Hearing scheduled for 14-FEB-2025.")]),
        classify_events([event(1, "2025-01-23", "Result of hearing: held in court.")]),
        classify_events([event(1, "2025-01-23", "Matter reserved for decision.")]),
        classify_events([event(1, "2025-01-23", "L'audience n'a pas eu lieu.")]),
    ]

    assert [result["hearing_status"]["status"] for result in results] == ["scheduled", "held", "reserved", "not_held"]
    assert results[1]["hearing_held"]["status"] == "yes"
    assert results[2]["hearing_held"]["status"] == "yes"


def test_treats_explicit_removal_cancellation_as_granted_stay():
    events = extract_procedural_events(
        [event(1, "2025-03-01", "The removal has been cancelled pending the application.")]
    )

    stay = next(item for item in events if item["event_type"] == "stay")
    assert stay["outcome"] == "granted"
    assert stay["rule"] == "stay_cancellation"

    result = classify_events(
        [event(1, "2025-03-01", "The removal has been cancelled pending the application.")]
    )
    assert result["stay_decision"]["status"] == "yes"


def test_extracts_explicit_removal_schedule_from_stay_event():
    events = extract_procedural_events(
        [event(1, "2007-02-23", "Notice of Motion for a stay of execution of the removal order scheduled for 26-FEB-2007 to Nigeria filed on 23-FEB-2007.")]
    )

    stay = next(item for item in events if item["event_type"] == "stay")
    assert stay["event_date"] == "2007-02-23"
    assert stay["date_kind"] == "filing_date"
    assert stay["removal_scheduled_date"] == "2007-02-26"
    assert stay["removal_destination"] == "Nigeria"


def test_extracts_month_first_removal_schedule_after_on_phrase():
    events = extract_procedural_events(
        [event(1, "2023-01-25", "Motion for a stay of execution of removal of the Applicant from Canada on Monday January 31, 2023 filed on 25-JAN-2023.")]
    )

    stay = next(item for item in events if item["event_type"] == "stay")
    assert stay["removal_scheduled_date"] == "2023-01-31"


def test_classifies_application_leave_final_and_hearing_milestones():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-01-10", "Application Record number of copies received/prepared: 2 on behalf of Applicant filed."),
            event(3, "2024-03-01", "Order rendered granting the application for leave."),
            event(4, "2024-05-10", "Matter reserved held in Court."),
            event(5, "2024-06-01", "(Final decision) Reasons for Judgment and Judgment rendered. Result: granted."),
        ]
    )

    assert result["application_filed"]["status"] == "yes"
    assert result["application_filed"]["date"] == "2024-01-02"
    assert result["application_perfected"]["status"] == "yes"
    assert result["application_perfected"]["date"] == "2024-01-10"
    assert result["leave_decision"]["result"] == "granted"
    assert result["leave_decision"]["date"] == "2024-03-01"
    assert result["final_decision"]["status"] == "yes"
    assert result["final_decision"]["date"] == "2024-06-01"
    assert result["hearing_held"]["status"] == "yes"


def test_does_not_treat_respondent_record_as_application_perfected():
    result = classify_events([event(1, "2024-01-02", "Memorandum of argument on behalf of the respondent filed.")])

    assert result["application_perfected"]["status"] == "unknown"
    assert result["application_perfected"]["date"] is None
    assert result["field_applicability"]["application_perfected"] == {"status": "not_applicable", "reason": "no_originating_application"}


def test_application_perfected_pending_when_filing_has_no_perfection_signal():
    result = classify_events([event(1, "2024-01-02", "Application for leave and judicial review filed.")])

    assert result["field_applicability"]["application_perfected"] == {"status": "pending", "reason": "perfection_signal_not_observed"}


def test_hearing_is_not_applicable_when_leave_is_refused():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Order dismissing the application for leave."),
        ]
    )

    assert result["field_applicability"]["hearing_held"] == {"status": "not_applicable", "reason": "leave_refused"}


def test_hearing_is_not_applicable_when_discontinued_before_leave():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Notice of discontinuance filed."),
        ]
    )

    assert result["field_applicability"]["hearing_held"] == {"status": "not_applicable", "reason": "discontinued_before_leave"}


def test_hearing_applicability_is_known_when_hearing_is_held():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Order granting the application for leave."),
            event(3, "2024-03-15", "Result of hearing: held in court."),
        ]
    )

    assert result["field_applicability"]["hearing_held"] == {"status": "known", "reason": "held", "evidence_status": "yes"}


def test_classifies_english_and_french_applicant_record_wording():
    result = classify_events(
        [
            event(1, "2024-01-02", "Record Number of copies received/prepared: 2 on behalf of Applicant filed."),
            event(2, "2024-01-03", "Dossier (demande) Nombre de copies reçu/préparé: 1 déposée."),
        ]
    )

    assert result["application_perfected"]["status"] == "yes"
    assert result["application_perfected"]["date"] == "2024-01-02"


def test_classifies_french_leave_and_final_decision_wording():
    result = classify_events(
        [
            event(1, "2024-01-02", "Demande d'autorisation et de contrôle judiciaire déposée."),
            event(2, "2024-03-01", "(Décision finale) Ordonnance rejetant la demande d'autorisation."),
        ]
    )

    assert result["application_filed"]["status"] == "yes"
    assert result["leave_decision"]["result"] == "refused"
    assert result["final_decision"]["status"] == "yes"


def test_judicial_review_is_not_reached_when_leave_is_refused():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "(Final decision) Order dismissing the application for leave."),
        ]
    )

    assert result["leave_decision"]["result"] == "refused"
    assert result["judicial_review_result"]["result"] == "not_reached"
    assert result["judicial_review_final_decision"]["status"] == "unknown"
    assert result["field_applicability"]["application_perfected"] == {
        "status": "not_applicable",
        "reason": "leave_refused",
        "explanation": "Not applicable: leave refused.",
    }
    assert result["field_applicability"]["judicial_review_result"]["status"] == "not_applicable"
    assert result["field_applicability"]["judicial_review_final_decision"]["status"] == "not_applicable"


def test_leave_is_not_applicable_when_case_discontinued_before_perfection():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Notice of discontinuance filed."),
        ]
    )

    assert result["application_perfected"]["status"] == "unknown"
    assert result["field_applicability"]["leave_decision"] == {
        "status": "not_applicable",
        "reason": "not_perfected_before_discontinued",
        "explanation": "The case reached discontinued before an applicant record was perfected, so leave could not proceed.",
        "evidence_status": "unknown",
    }


def test_substantive_final_decision_infers_leave_granted():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-06-01", "(Final decision) Order dismissing the application for judicial review."),
        ]
    )

    assert result["leave_context"]["status"] == "inferred_granted"
    assert result["judicial_review_result"]["result"] == "dismissed"
    assert result["field_applicability"]["judicial_review_final_decision"]["status"] == "known"


def test_final_decision_is_not_applicable_after_withdrawal_following_leave_grant():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Order granting the application for leave."),
            event(3, "2024-03-01", "Notice of withdrawal on behalf of the applicant filed."),
        ]
    )

    assert result["field_applicability"]["judicial_review_final_decision"] == {
        "status": "not_applicable",
        "reason": "withdrawn_after_leave_granted",
        "evidence_status": "unknown",
    }


def test_production_order_supports_inferred_leave_grant():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Motion for production of documents granted; production order issued."),
        ]
    )

    assert result["leave_context"]["status"] == "inferred_granted_production_order"
    assert result["field_applicability"]["leave_decision"]["reason"] == "inferred_granted_production_order"


def test_classifies_vba_leave_shorthand_and_french_refusal_wording():
    granted = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Result - leave granted."),
        ]
    )
    refused = classify_events(
        [
            event(1, "2024-01-02", "Demande d'autorisation et de contrôle judiciaire déposée."),
            event(2, "2024-02-01", "Demande d'autorisation refusée."),
        ]
    )

    assert granted["leave_decision"]["result"] == "granted"
    assert granted["leave_decision"]["doc_id"] == 2
    assert refused["leave_decision"]["result"] == "refused"
    assert refused["leave_decision"]["doc_id"] == 2


def test_marks_unresolved_leave_application_as_pending():
    result = classify_events(
        [event(1, "2026-01-02", "Application for leave and judicial review filed.")]
    )

    assert result["leave_decision"]["result"] == "unknown"
    assert result["leave_context"]["status"] == "pending"
    assert result["leave_context"]["rule"] == "leave_decision_not_yet_observed"


def test_judicial_review_final_requires_leave_and_review_result():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Order granting the application for leave."),
            event(3, "2024-06-01", "(Final decision) Reasons for Judgment and Judgment. Judicial Review Result: granted."),
        ]
    )

    assert result["leave_decision"]["result"] == "granted"
    assert result["judicial_review_result"]["result"] == "granted"
    assert result["judicial_review_final_decision"]["status"] == "yes"


def test_closing_status_uses_latest_three_entries_for_discontinuance():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Application Record filed on behalf of Applicant."),
            event(3, "2024-03-01", "Notice of discontinuance on behalf of the Applicant filed."),
            event(4, "2024-03-02", "Solicitor's certificate of service filed."),
        ]
    )

    assert result["closing_status"]["status"] == "discontinued"
    assert result["closing_status"]["date"] == "2024-03-01"


def test_closing_status_detects_administrative_termination():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Letter advising of no reasons on application terminated by S. 87.4(1) of IRPA."),
        ]
    )

    assert result["closing_status"]["status"] == "administratively_terminated"


def test_closing_status_detects_withdrawal_pending_and_case_management():
    withdrawn = classify_events([event(1, "2024-01-02", "Notice of withdrawal on behalf of the applicant filed.")])
    pending = classify_events([event(1, "2024-01-02", "No decision has yet been made, as such, no reasons exist.")])
    managed = classify_events([event(1, "2024-01-02", "Case Management Conference Result of Hearing: Parties are to consult each other to reach consent.")])

    assert withdrawn["closing_status"]["status"] == "withdrawn"
    assert pending["closing_status"]["status"] == "underlying_decision_pending"
    assert managed["closing_status"]["status"] == "case_management"


def test_lifecycle_status_distinguishes_closed_abeyance_active_and_unknown():
    closed = classify_events([event(1, "2024-01-02", "Notice of discontinuance filed.")])
    abeyance = classify_events([event(1, "2024-01-02", "File is held in abeyance until further order.")])
    active = classify_events([event(1, "2024-01-02", "Application Record filed on behalf of Applicant.")])
    unknown = classify_events([])

    assert closed["lifecycle_status"]["status"] == "closed"
    assert closed["lifecycle_status"]["status_kind"] == "discontinued"
    assert abeyance["lifecycle_status"]["status"] == "abeyance"
    assert active["lifecycle_status"]["status"] == "active"
    assert active["lifecycle_status"]["confidence"] == "inferred"
    assert unknown["lifecycle_status"]["status"] == "unknown"


def test_full_history_resolution_survives_later_registry_artifacts():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Order dismissing the application for leave."),
            event(3, "2024-03-01", "Memorandum to file: final order returned to registry."),
        ]
    )

    assert result["closing_status"]["status"] == "leave_refused"
    assert result["full_history_resolution"]["status"] == "leave_refused"


def test_derives_challenged_decision_from_originating_application():
    result = classify_events(
        [
            event(1, "2024-01-01", "Copy of doc. 1 with proof of service filed."),
            event(2, "2024-01-02", "Application for leave and judicial review against a decision IRB RPD, dated 15-OCT-2023, File No. VB1-03122 filed."),
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["status"] == "yes"
    assert challenged["application_type"] == "leave_and_judicial_review"
    assert challenged["decision_maker"] == "IRB RPD"
    assert challenged["decision_date"] == "15-OCT-2023"
    assert "VB1-03122" in challenged["tribunal_file_numbers"]
    assert "irb_refugee_or_appeal" in challenged["challenge_categories"]
    assert challenged["decision_maker_type"] == "irb_refugee_or_appeal"
    assert challenged["filing_date"] == "2024-01-02"
    assert challenged["originating_decision_maker_type"] == "irb_refugee_or_appeal"
    assert challenged["decision_type"] == "refugee_protection"
    assert challenged["underlying_tribunal"] == "IRB RPD"
    assert challenged["underlying_tribunal_type"] == "irb"
    assert challenged["decision_subject"] == "refugee_protection"


def test_extracts_spaced_and_semicolon_challenged_decision_dates():
    results = [
        classify_events(
            [
                event(
                    1,
                    "2015-03-30",
                    "Application for leave and judicial review against a decision Embassy of Canada, Bogota; dated 17 Feb 2015; File#V305316520 filed on 30-MAR-2015.",
                )
            ]
        ),
        classify_events(
            [
                event(
                    1,
                    "2015-03-30",
                    "Application for leave and judicial review against a decision IRB-RPD TORONTO; 2-MAR-2015; TB1-12048 filed on 30-MAR-2015.",
                )
            ]
        ),
        classify_events(
            [
                event(
                    1,
                    "2015-09-17",
                    "Demande d'autorisation et de contrôle judiciaire contre la décision de CIC, rendue le 11 mars 2015 dans le dossier no. 6579-1888; déposée le 17-SEP-2015.",
                )
            ]
        ),
    ]

    assert [result["challenged_decision"]["decision_date"] for result in results] == [
        "17 Feb 2015",
        "2-MAR-2015",
        "11 mars 2015",
    ]


def test_extracts_explicit_refugee_subject_and_decision_maker_variants():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review against a decision IRB-RPD, 19-APR-2024, file TA1-22123 filed on 03-MAY-2024."),
            event(2, "2024-01-03", "Application for leave and judicial review against a decision made by Aaron David Smith, Refugee Appeal Division, dated 26-NOV-2023 filed on 03-JAN-2024."),
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_subject"] == "refugee_protection"
    assert challenged["decision_maker"] == "IRB-RPD"


def test_extracts_refugee_subject_from_french_spr_wording():
    result = classify_events(
        [
            event(
                1,
                "2013-04-26",
                "Demande d'autorisation et de contrôle judiciaire contre la décision de la CISR (SPR), rendue le 7-mar-2013 dans les dossiers MB1-03056 déposée le 26-AVR-2013.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "refugee_protection"


def test_extracts_refugee_subject_from_prra_wording():
    result = classify_events(
        [
            event(
                1,
                "2010-01-07",
                "Application for leave and judicial review against a decision PRRA, Toronto; November 30 2009; 5506-2171 filed on 07-JAN-2010.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "refugee_protection"


def test_extracts_humanitarian_subject_without_collapsing_it_into_permanent_residence():
    result = classify_events(
        [
            event(
                1,
                "2016-04-20",
                "Application for leave and judicial review against a decision CIC (H&C), 12-APR-2016, 6503-2158 filed on 20-APR-2016.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "humanitarian_and_compassionate"


def test_extracts_explicit_visitor_visa_as_temporary_residence():
    result = classify_events(
        [
            event(
                1,
                "2024-01-05",
                "Application for leave and judicial review against a decision of Visa Officer CPC Ottawa wherein the Tribunal refused the Applicant's application for Visitor's Visa filed on 05-JAN-2023.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "temporary_residence"


def test_extracts_backlog_reduction_office_as_permanent_residence():
    result = classify_events(
        [
            event(
                1,
                "2016-10-28",
                "Application for leave and judicial review against a decision of a Senior Immigration Officer at Backlog Reduction Office, CIC, Vancouver, BC, dated 29-Jul-2016, in file numbers 6095-6997 filed on 28-OCT-2016.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "permanent_residence"


def test_extracts_full_ircc_name_as_processing_decision_maker():
    result = classify_events(
        [
            event(
                1,
                "2021-08-05",
                "Application for leave and judicial review against a decision of the Immigration, Refugees and Citizenship Canada officer, dated and received on 22-JULY-2021, wherein the Tribunal refused the Applicant's application for permanent residency.",
            )
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_maker_type"] == "cic_ircc_processing"
    assert challenged["decision_subject"] == "permanent_residence"


def test_extracts_full_refugee_and_appeal_division_names():
    result = classify_events(
        [
            event(1, "2021-08-18", "Application for leave and judicial review against a decision Immigration and Refugee Board, Refugee Appeal Division - Toronto, Ontario dated July 28, 2021 File No. TC1-00695."),
            event(2, "1996-04-01", "Application for leave and judicial review against a decision of the Refugee Division dated 13-MAR-1996 and communicated 19-MAR-1996."),
        ]
    )

    assert result["challenged_decision"]["decision_maker_type"] == "irb_refugee_or_appeal"
    assert result["challenged_decision"]["decision_subject"] == "refugee_protection"


def test_extracts_full_immigration_division_name_as_irb_decision_maker():
    result = classify_events(
        [
            event(
                1,
                "2021-12-14",
                "Application for leave and judicial review against a decision IRB-Immigration Division (Etobicoke, ON), 23-NOV-2021, File no. 0003-C0-00698-02 filed on 14-DEC-2021.",
            )
        ]
    )

    assert result["challenged_decision"]["decision_maker_type"] == "irb_refugee_or_appeal"


@pytest.mark.parametrize(
    ("text", "maker_type", "subject"),
    [
        ("Application for leave and judicial review against a decision PRRA Toronto dated 30-NOV-2009.", "irb_refugee_or_appeal", "refugee_protection"),
        ("Application for leave and judicial review against a decision Enforcement Section dated 06-NOV-2015.", "cbsa_enforcement", "unknown"),
        ("Application for leave and judicial review against a decision Service Canada dated 19-JAN-2015.", "cic_ircc_processing", "unknown"),
        ("Application for leave and judicial review against a decision High Commission of Canada dated 19-JAN-2015.", "visa_office_or_consulate", "unknown"),
    ],
)
def test_originating_maker_aliases_preserve_subject_uncertainty(text, maker_type, subject):
    result = classify_events([event(1, "2015-02-09", text)])

    challenged = result["challenged_decision"]
    assert challenged["originating_decision_maker_type"] == maker_type
    assert challenged["decision_subject"] == subject


def test_subject_uses_explicit_later_history_evidence_when_originating_entry_is_generic():
    result = classify_events(
        [
            event(1, "2021-01-05", "Application for leave and judicial review against a decision IRCC CPC Ottawa filed on 05-JAN-2021."),
            event(2, "2021-03-05", "Certified copy of the decision and reasons sent by Immigration, Refugees and Citizenship Canada. The decision refused the Applicant's application for permanent residence."),
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_subject"] == "permanent_residence"
    assert challenged["decision_subject_doc_id"] == 2


def test_decision_maker_type_uses_explicit_later_history_evidence():
    result = classify_events(
        [
            event(1, "2021-01-05", "Application for leave and judicial review against a decision filed on 05-JAN-2021."),
            event(2, "2021-03-05", "Certified copy of the decision and reasons sent by Immigration, Refugees and Citizenship Canada."),
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_maker_type"] == "cic_ircc_processing"
    assert challenged["decision_maker_evidence_doc_id"] == 2


def test_extracts_explicit_eta_as_temporary_residence():
    result = classify_events(
        [event(1, "2020-02-12", "Application for leave and judicial review against a decision of IRCC wherein the applicant's Electronic Travel Authorization was refused.")]
    )

    assert result["challenged_decision"]["decision_subject"] == "temporary_residence"


def test_extracts_sponsored_landing_application_as_permanent_residence():
    result = classify_events(
        [
            event(1, "2004-08-01", "Application for leave and judicial review filed."),
            event(2, "2004-09-13", "Judicial review of the decision of the Immigration Appeal Division, wherein the Panel Member disallowed the applicant's appeal from a refusal of the sponsored application for landing of his adopted daughter."),
        ]
    )

    assert result["challenged_decision"]["decision_subject"] == "permanent_residence"


def test_extracts_convention_refugee_determination_division():
    result = classify_events(
        [event(1, "1994-06-09", "Application for leave and judicial review against a decision Convention Refugee Determination Division dated 17-MAY-1994.")]
    )

    assert result["challenged_decision"]["decision_subject"] == "refugee_protection"


def test_labels_generic_institution_when_subject_is_not_stated():
    result = classify_events(
        [event(1, "2022-07-20", "Application for leave and judicial review against a decision IRCC CPC OTTAWA, 28-JUN-2022, APPLICATION# S304919344 filed on 20-JUL-2022.")]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_subject"] == "unknown"
    assert challenged["decision_subject_availability"] == "generic_institution_only"
    assert challenged["decision_subject_label"] == "IRCC CPC OTTAWA"


def test_extracts_french_erar_as_refugee_protection():
    result = classify_events(
        [event(1, "2018-11-15", "Demande d'autorisation et de contrôle judiciaire contre la décision d'une agente d'immigration supérieure refusant la demande de risque de retour (ERAR), en date du 2-AOU-2018 déposée le 15-NOV-2018.")]
    )

    assert result["challenged_decision"]["decision_subject"] == "refugee_protection"


def test_extracts_lmia_as_temporary_residence():
    result = classify_events(
        [event(1, "2015-02-09", "Application for leave and judicial review against a decision Service Canada - Foreign Service Worker Program, Toronto, ON by N. Dai dated 19-JAN-2015 re: Employer ID #77927 and LMIA #8121073 filed on 09-FEB-2015.")]
    )

    assert result["challenged_decision"]["decision_subject"] == "temporary_residence"


def test_labels_french_agency_reference_as_generic_when_subject_is_unstated():
    result = classify_events(
        [event(1, "2026-01-05", "Demande d'autorisation et de contrôle judiciaire contre la décision de l'Agence des Services Frontaliers du Canada datée 29 août 2025 dans le dossier L010556851.")]
    )

    challenged = result["challenged_decision"]
    assert challenged["decision_subject"] == "unknown"
    assert challenged["decision_subject_availability"] == "generic_institution_only"


def test_extracts_french_judge_title_and_hearing_before_judge():
    events = extract_procedural_events(
        [
            event(1, "2017-01-16", "Ordonnance rendu(e) par Monsieur le juge S. Noel a Ottawa le 16-JAN-2017 rejetant la demande d'autorisation."),
            event(2, "2021-12-15", "Ottawa 15-DEC-2021 BEFORE The Honourable Mr. Justice McHaffie Language: E Result of Hearing: Matter adjourned."),
        ]
    )

    french_event = next(item for item in events if "Monsieur le juge" in item["text"])
    hearing_event = next(item for item in events if "BEFORE The Honourable" in item["text"])
    assert french_event["judge_name"] == "S. Noel"
    assert hearing_event["judge_name"] == "McHaffie"


def test_milestone_rollup_keeps_stage_results_and_evidence_together():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-02-01", "Application Record filed on behalf of Applicant."),
            event(3, "2024-03-01", "Order granting the application for leave."),
            event(4, "2024-05-10", "Hearing held in court."),
            event(5, "2024-06-01", "(Final decision) Reasons for Judgment rendered."),
        ]
    )

    rollups = result["milestone_rollups"]
    assert rollups["leave"]["result"] == "granted"
    assert rollups["hearing"]["status"] == "held"
    assert rollups["application"]["filed"]["doc_id"] == 1
    assert rollups["final_decision"]["doc_id"] == 5


def test_derives_french_challenged_decision_and_mandamus():
    result = classify_events(
        [
            event(1, "2024-01-01", "Demande d'autorisation et de contrôle judiciaire et mandamus contre la décision de la CISR, Section de la protection des réfugiés, rendue le 12-OCT-2023 dans le dossier MA9-07505 déposée le 01-NOV-2023."),
        ]
    )

    challenged = result["challenged_decision"]
    assert challenged["status"] == "yes"
    assert challenged["application_type"] == "leave_judicial_review_and_mandamus"
    assert challenged["decision_date"] == "12-OCT-2023"
    assert "MA9-07505" in challenged["tribunal_file_numbers"]


def test_later_judicial_review_infers_leave_granted():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-06-01", "(Final decision) Judicial Review Result: granted."),
        ]
    )

    assert result["leave_decision"]["result"] == "unknown"
    assert result["leave_context"]["status"] == "inferred_granted"
    assert result["judicial_review_result"]["result"] == "granted"


def test_discontinuance_makes_unknown_leave_not_relevant():
    result = classify_events(
        [
            event(1, "2024-01-02", "Application for leave and judicial review filed."),
            event(2, "2024-03-01", "Notice of discontinuance on behalf of the Applicant filed."),
        ]
    )

    assert result["leave_decision"]["result"] == "unknown"
    assert result["leave_context"]["status"] == "not_relevant_discontinued"


def test_direct_judicial_review_does_not_use_leave_stage():
    result = classify_events(
        [
            event(1, "2001-10-03", "Notice of application with regard to Judicial Review filed."),
            event(2, "2001-12-06", "Discontinuance on behalf of Applicant filed."),
        ]
    )

    assert result["challenged_decision"]["application_type"] == "direct_judicial_review"
    assert result["leave_context"]["status"] == "not_applicable_direct_judicial_review"
    assert result["field_applicability"]["leave_decision"]["explanation"] == "This application proceeded as direct judicial review and did not require leave."
    assert result["closing_status"]["status"] == "discontinued"


def test_cancelled_entries_are_ignored():
    result = classify_events(
        [
            event(1, "2018-08-01", "Application for leave and judicial review against a decision of the visa officer filed on 01-AUG-2018"),
            event(2, "2018-10-25", "****** CANCELLED ****** (Final decision) Order rendered by The Honourable Madam Justice Gagné at Ottawa on 25-OCT-2018 dismissing the application for leave Decision endorsed on the record"),
            event(3, "2018-12-03", "Notice of discontinuance on behalf of the applicant filed on 03-DEC-2018 with proof of service on the respondent"),
        ]
    )
    assert result["leave_decision"]["result"] == "unknown"
    assert result["full_history_resolution"]["status"] == "discontinued"


def test_paper_dismissal_of_judicial_review_without_leave_is_leave_refusal():
    result = classify_events(
        [
            event(1, "1993-03-01", "Application for leave and for judicial review filed on 01-MAR-1993"),
            event(2, "1993-09-10", "(Final decision) Order of the Court/ The Honourable Mr. Justice Cullen rendered at Ottawa on 10-SEP-1993 dismissing the application for judicial review and COMPLETING THE FILE endorsed on 1 Considered by the Court without personal appearance"),
        ]
    )
    assert result["leave_decision"]["result"] == "refused"
    assert result["leave_decision"]["rule"] == "paper_dismissal_without_leave_grant"
    assert result["judicial_review_result"]["result"] == "not_reached"
    assert result["full_history_resolution"]["status"] == "leave_refused"
    assert result["lifecycle_status"]["status"] == "closed"


def test_judicial_review_dismissed_after_hearing_is_not_a_paper_dismissal():
    result = classify_events(
        [
            event(1, "2014-11-01", "Application for leave and judicial review filed on 01-NOV-2014"),
            event(2, "2015-03-01", "Order rendered by The Honourable Madam Justice Strickland granting the application for leave fixing the hearing"),
            event(3, "2015-09-02", "(Final decision) Reasons for Judgment and Judgment dated 02-SEP-2015 rendered by The Honourable Madam Justice Strickland Matter considered with personal appearance The Court's decision is with regard to Judicial Review and certification of a serious question of general importance Result: dismissed Filed on 02-SEP-2015"),
            event(4, "2016-06-02", "Copy of Notice of Discontinuance placed on file on 02-JUN-2016 Original filed on Court File No. A-431-15"),
        ]
    )
    assert result["leave_decision"]["result"] == "granted"
    assert result["judicial_review_result"]["result"] == "dismissed"
    assert result["full_history_resolution"]["status"] == "judicial_review_dismissed"


def test_consent_motion_then_granting_order_resolves_by_consent():
    result = classify_events(
        [
            event(1, "2018-06-01", "Application for leave and judicial review against a decision of the IRB-IAD filed on 01-JUN-2018"),
            event(2, "2018-11-15", "Notice of Motion contained within a Motion Record on behalf of Applicant in writing to be dealt with in the Toronto local office for Judgment on consent filed on 15-NOV-2018 Draft Order\\Judgment received.", docno="14"),
            event(3, "2018-11-19", "Order dated 19-NOV-2018 rendered by The Honourable Mr. Justice Manson Matter considered without personal appearance The Court's decision is with regard to Motion in writing Doc. No. 14 Result: granted Filed on 19-NOV-2018", docno="19"),
        ]
    )
    consent = result["consent_disposition"]
    assert consent["status"] == "granted"
    assert consent["date"] == "2018-11-19"
    assert result["full_history_resolution"]["status"] == "resolved_by_consent"
    assert result["lifecycle_status"]["status"] == "closed"


def test_consent_to_procedural_relief_is_not_a_consent_disposition():
    result = classify_events(
        [
            event(1, "2020-01-10", "Application for leave and judicial review filed on 10-JAN-2020"),
            event(2, "2020-02-01", "Notice of Motion on behalf of Applicant on consent for an Order extending the time to file the Applicant's Record filed on 01-FEB-2020", docno="5"),
            event(3, "2020-02-05", "Order dated 05-FEB-2020 rendered by The Honourable Mr. Justice Example The Court's decision is with regard to Motion in writing Doc. No. 5 Result: granted"),
        ]
    )
    assert result["consent_disposition"]["status"] == "none"
    assert result["full_history_resolution"]["status"] != "resolved_by_consent"


def test_group_order_dismissal_and_fully_cancelled_file():
    grouped = classify_events(
        [
            event(1, "2012-11-01", "Application for leave and judicial review and mandamus filed on 01-NOV-2012"),
            event(2, "2017-07-05", "Copy of Order dated 05-JUL-2017 rendered by The Honourable Madam Justice Kane concerning The present application and those listed in the attached schedule are dismissed. (Original file : IMM-7502-11) placed on file. Original filed on Court File No. IMM-9024-12"),
        ]
    )
    assert grouped["full_history_resolution"]["status"] == "dismissed_by_group_order"
    assert grouped["lifecycle_status"]["status"] == "closed"
    cancelled = classify_events([event(1, "2020-10-05", "****** CANCELLED ****** Application for leave and judicial review against a decision Test filed on 05-OCT-2020")])
    assert cancelled["full_history_resolution"]["status"] == "file_cancelled"
    assert cancelled["lifecycle_status"]["status"] == "closed"


def test_certificate_of_order_and_hearing_results_are_read():
    leave = classify_events(
        [
            event(1, "2009-01-05", "Application for leave and judicial review filed on 05-JAN-2009"),
            event(2, "2009-05-20", "Certificate of Order rendered by The Honourable Madam Justice Simpson on 19-MAY-2009 endorsed on the record on Doc. 1 received in the Registry on 20-MAY-2009 issued to parties Matter considered without personal appearance concerning the application for leave Result: dismissed Copy of Certificate placed on file"),
        ]
    )
    assert leave["leave_decision"]["result"] == "refused"
    assert leave["full_history_resolution"]["status"] == "leave_refused"
    mislabelled = classify_events(
        [
            event(1, "2007-10-17", "Application for leave and judicial review against a decision IRB - RPD filed on 17-OCT-2007"),
            event(2, "2008-01-15", "Order rendered by The Honourable Madam Justice Hansen at Ottawa on 15-JAN-2008 granting the application for leave fixing the hearing"),
            event(3, "2008-04-11", "(Final decision) Reasons for Judgment and Judgment dated 11-APR-2008 rendered by The Honourable Madam Justice Tremblay-Lamer Matter considered with personal appearance The Court's decision is with regard to the application for leave Result: dismissed Filed on 11-APR-2008"),
        ]
    )
    assert mislabelled["judicial_review_result"]["result"] == "dismissed"
    assert mislabelled["full_history_resolution"]["status"] == "judicial_review_dismissed"
