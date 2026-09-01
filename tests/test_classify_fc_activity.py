from datetime import date

from scripts.classify_fc_activity import ActivityEvent, classify_events


def event(doc_id, doc_date, text):
    return ActivityEvent(1, "IMM-1-24", "Example v. Canada", doc_id, date.fromisoformat(doc_date), text)


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
    assert result["leave_context"]["status"] == "not_relevant_discontinued"
    assert result["closing_status"]["status"] == "discontinued"
