from datetime import date

from scripts.classify_fc_activity import ActivityEvent, classify_events
from scripts.fc_activity_extractors import (
    extract_appeal,
    extract_certified_question,
    extract_hearings,
    extract_representation,
    extract_respondent_position,
    extract_stay_of_removal,
    leave_refusal_reason,
)


def event(doc_id, doc_date, text, *, docno=None, citation="IMM-1-15"):
    return ActivityEvent(1, citation, "Example v. Canada", doc_id, date.fromisoformat(doc_date), text, docno=docno)


HEARING = (
    "Toronto 17-JUN-2015 BEFORE The Honourable Madam Justice Strickland Language: E Before the Court: Judicial Review "
    "Result of Hearing: Matter reserved held in Court Senior Usher: MIKE GAIDA Duration per day: 17-JUN-2015 from 09:29 to 12:09 "
    "Courtroom : Courtroom No. 4-A - Toronto Court Registrar: Michel Total Duration: 2h40min Appearances: Mr. Lorne Waldman "
    "416-482-6501 representing Applicant Ms. Catherine Vasilaros (416)952-5011 representing Respondent Comments: Neither counsel "
    "have a proposed question for certification. Minutes of Hearing entered in Vol. 173 page(s) 17 - 20"
)


def test_hearing_entry_is_parsed_into_structured_fields():
    hearings = extract_hearings([event(1, "2015-06-17", HEARING)])
    hearing = hearings["judicial_review_hearing"]
    assert hearing["date"] == "2015-06-17"
    assert hearing["city"] == "Toronto"
    assert hearing["judge"]["key"] == "strickland"
    assert hearing["language"] == "english"
    assert hearing["kind"] == "judicial_review"
    assert hearing["result"] == "reserved"
    assert hearing["mode"] == "in_court"
    assert hearing["duration_minutes"] == 160
    roles = {item["role"]: item["name"] for item in hearing["appearances"]}
    assert roles["applicant_counsel"] == "Lorne Waldman"
    assert roles["respondent_counsel"] == "Catherine Vasilaros"


def test_video_hearing_duration_from_time_span():
    text = (
        "Ottawa 21-SEP-2022 BEFORE The Honourable Mr. Justice Manson Language: E Before the Court: Judicial Review Result of Hearing: "
        "Matter reserved held by way of Zoom video conference Duration per day: 21-SEP-2022 from 10:54 to 11:29 Courtroom : Ottawa (Zoom)"
    )
    hearing = extract_hearings([event(1, "2022-09-21", text)])["judicial_review_hearing"]
    assert hearing["mode"] == "video"
    assert hearing["duration_minutes"] == 35


def test_certified_question_statuses():
    certified = extract_certified_question(
        [event(1, "2019-03-01", "(Final decision) Reasons for Judgment and Judgment dated 01-MAR-2019 The Court's decision is with regard to Judicial Review Result: dismissed. The following question is certified: Does the RAD ...")]
    )
    assert certified["status"] == "certified"
    not_certified = extract_certified_question([event(1, "2015-06-17", HEARING)])
    assert not_certified["status"] == "not_certified"
    french = extract_certified_question([event(1, "2020-01-01", "Remarques : Les parties ont confirmé qu'il n'y a pas de question à certifier.")])
    assert french["status"] == "not_certified"
    assert extract_certified_question([event(1, "2020-01-01", "Certified copy of the record sent by IRB")])["status"] == "unknown"


def test_appeal_to_federal_court_of_appeal():
    appeal = extract_appeal(
        [
            event(1, "2015-10-06", "Copy of Notice of Appeal (Appeal Court File No. A-431-15 ) appealing Judgment of Madam Justice Strickland filed in the Court of Appeal on 30-SEP-2015 on behalf of Applicant placed on file on 06-OCT-2015"),
            event(2, "2016-06-02", "Copy of Notice of Discontinuance placed on file on 02-JUN-2016 Original filed on Court File No. A-431-15"),
        ]
    )
    assert appeal["status"] == "appealed"
    assert appeal["fca_files"] == ["A-431-15"]
    assert appeal["appellant"] == "applicant"
    assert appeal["filed_date"] == "2015-09-30"
    assert appeal["outcome"] == "discontinued"


def test_appellant_and_certified_question_inferred_from_judicial_review_result():
    result = classify_events(
        [
            event(1, "2014-11-01", "Application for leave and judicial review against a decision IRB - RPD filed on 01-NOV-2014"),
            event(2, "2015-03-01", "Order rendered by The Honourable Madam Justice Strickland granting the application for leave fixing the hearing"),
            event(3, "2015-09-02", "(Final decision) Reasons for Judgment and Judgment dated 02-SEP-2015 rendered by The Honourable Madam Justice Strickland Matter considered with personal appearance The Court's decision is with regard to Judicial Review Result: dismissed Filed on 02-SEP-2015"),
            event(4, "2015-10-06", "Copy of Notice of Appeal (Appeal Court File No. A-431-15 ) appealing Judgment filed in the Court of Appeal on 30-SEP-2015 on behalf of Appellant placed on file on 06-OCT-2015"),
        ]
    )
    assert result["appeal"]["appellant"] == "applicant_inferred"
    assert result["certified_question"]["status"] == "certified_inferred_from_appeal"


def test_stay_of_removal_request_and_decision():
    stay = extract_stay_of_removal(
        [
            event(1, "2012-11-29", "Notice of Motion contained within a Motion Record on behalf of Applicant returnable (but no hearing date indicated at this time) for a stay of execution of removal scheduled for 1-DEC-2012 to Ireland at 6:30pm filed on 29-NOV-2012"),
            event(2, "2012-11-30", "Order rendered by The Honourable Mr. Justice Russell at Ottawa on 30-NOV-2012 granting the stay of execution Decision filed on 30-NOV-2012 Considered by the Court with personal appearance"),
        ]
    )
    assert stay["status"] == "granted"
    assert stay["removal_date"] == "2012-12-01"
    assert stay["removal_destination"] == "Ireland"
    assert stay["decision_judge"]["key"] == "russell"
    refused = extract_stay_of_removal([event(1, "2018-10-30", "Ordonnance rendu(e) par Monsieur le juge Diner à Ottawa le 30-OCT-2018 rejetant la demande de sursis d'exécution Décision déposée le 30-OCT-2018")])
    assert refused["status"] == "refused"
    hearing_time = extract_stay_of_removal([event(1, "2020-01-01", "Notice of Motion on behalf of Applicant for a stay of removal returnable at General Sitting to begin at 09:30")])
    assert hearing_time["removal_destination"] is None


def test_representation_from_service_certificates_and_hearings():
    events = [
        event(1, "2011-02-25", "Solicitor's certificate of service on behalf of Mario D. Bellissimo confirming service of doc 4 upon Respondent by telecopier on 25-FEB-2011 filed on 25-FEB-2011"),
        event(2, "2011-03-01", "Solicitor's certificate of service on behalf of Brett J. Nash confirming service of Respondent's Memorandum of Argument upon Applicant by Email"),
        event(3, "2015-07-30", "Attestation de signification de l'avocat de la part Me Guillaume Cliche-Rivard attestant la signification du Mémoire supplémentaire de la demanderesse (doc. 21) à la partie défenderesse par télécopie"),
    ]
    representation = extract_representation(events)
    assert representation["status"] == "represented"
    names = [item["name"] for item in representation["all_applicant_counsel"]]
    assert "Mario D. Bellissimo" in names
    assert "Guillaume Cliche-Rivard" in names
    assert "Brett J. Nash" not in names
    self_rep = extract_representation(
        [event(1, "2009-06-01", "Toronto 01-JUN-2009 BEFORE The Honourable Max M. Teitelbaum, Deputy Judge Language: E Before the Court: Motion Doc. No. 3 on behalf of Respondent Result of Hearing: Matter dismissed held in Court Appearances: Ms. Aleese Pereira (self represented) Mr. John Loncar representing Respondent")],
        extract_hearings([event(1, "2009-06-01", "Toronto 01-JUN-2009 BEFORE The Honourable Max M. Teitelbaum, Deputy Judge Language: E Before the Court: Motion Doc. No. 3 on behalf of Respondent Result of Hearing: Matter dismissed held in Court Appearances: Ms. Aleese Pereira (self represented) Mr. John Loncar representing Respondent")]),
    )
    assert self_rep["status"] == "self_represented"


def test_respondent_position_before_leave():
    events = [
        event(1, "2016-09-20", "Letter from respondent dated 20-SEP-2016 confirming that they do not oppose the granting of leave in the Court file received on 20-SEP-2016"),
        event(2, "2016-10-20", "Memorandum of argument on behalf of the respondent filed on 20-OCT-2016 with proof of service on the applicant"),
    ]
    assert extract_respondent_position(events, "2016-12-01")["status"] == "not_opposed"
    assert extract_respondent_position(events[1:], "2016-12-01")["status"] == "opposed"
    assert extract_respondent_position(events[1:], "2016-10-01")["status"] == "unknown"


def test_leave_refusal_reason():
    assert leave_refusal_reason("refused", "2020-05-01", "Order dismissing the application for leave", None) == "not_perfected"
    assert leave_refusal_reason("refused", "2020-05-01", "Order dismissing the application for leave", "2020-02-01") == "refused_after_perfection"
    assert leave_refusal_reason("granted", "2020-05-01", "Order granting leave", "2020-02-01") is None


def test_timeline_and_filing_details_for_full_case():
    result = classify_events(
        [
            event(1, "2015-01-05", "Application for leave and judicial review against a decision IRB-RPD Toronto filed on 05-JAN-2015 Written reasons received by the Applicant Tariff fee of $50.00 received"),
            event(2, "2015-02-04", "Applicant's Record Number of copies received/prepared: 1 on behalf of Applicant filed on 04-FEB-2015"),
            event(3, "2015-04-01", "Order rendered by The Honourable Madam Justice Strickland at Ottawa on 01-APR-2015 granting the application for leave fixing the hearing"),
            event(4, "2015-06-17", HEARING),
            event(5, "2015-09-02", "(Final decision) Reasons for Judgment and Judgment dated 02-SEP-2015 rendered by The Honourable Madam Justice Strickland Matter considered with personal appearance The Court's decision is with regard to Judicial Review Result: granted Filed on 02-SEP-2015"),
        ],
        nature="Imm - Appl. for leave & jud. review - IRB - Refugee",
    )
    timeline = result["timeline"]
    assert timeline["days_filing_to_perfection"] == 30
    assert timeline["days_filing_to_leave_decision"] == 86
    assert timeline["days_leave_grant_to_hearing"] == 77
    assert timeline["days_hearing_to_judgment"] == 77
    assert timeline["judgment_from_bench"] is False
    assert result["filing_details"]["reasons_at_filing"] == "received"
    assert result["filing_details"]["proceeding_language"] == "english"
    assert result["judge_roles"]["merits_judge"]["key"] == "strickland"
    assert result["representation"]["applicant_counsel"]["name"] == "Lorne Waldman"


def test_office_location_motions_parties_and_filing_speed():
    result = classify_events(
        [
            event(1, "2015-10-20", "Application for leave and judicial review against a decision Visa Section, High Commission of Canada, New Delhi, India dated 08-SEP-2015 filed on 20-OCT-2015"),
            event(2, "2015-11-02", "Notice of Motion contained within a Motion Record on behalf of Applicant in writing for an Order extending the time to file the Applicant's Record filed on 02-NOV-2015", docno="3"),
            event(3, "2015-11-03", "Motion Record containing the following original document(s): 3 4 on behalf of Applicant filed on 02-NOV-2015"),
            event(4, "2015-11-10", "Order dated 10-NOV-2015 rendered by The Honourable Mr. Justice Example Matter considered without personal appearance The Court's decision is with regard to Motion in writing Doc. No. 3 Result: granted extension of time"),
        ]
    )
    assert result["office_location"] == {"office": "New Delhi", "abroad": True, "source": "decision_maker"}
    assert result["motion_profile"]["motions_filed"] == 1
    assert result["timeline"]["days_decision_to_filing"] == 42
    assert result["parties"]["joint_applicants"] is False


def test_joint_applicants_from_style_of_cause():
    from scripts.fc_activity_extractors import extract_parties

    joint = ActivityEvent(1, "IMM-1-15", "FERUZA LER ET AL v. MCI", 1, date(2015, 1, 1), "Application")
    pair = ActivityEvent(1, "IMM-1-15", "BOGLARKA KALOTAI AND CSENGE LOSONCZKI v MCI", 1, date(2015, 1, 1), "Application")
    single = ActivityEvent(1, "IMM-1-15", "KEIRAN CURTIS ST. BRICE v. MCI", 1, date(2015, 1, 1), "Application")
    assert extract_parties([joint])["joint_applicants"] is True
    assert extract_parties([pair])["joint_applicants"] is True
    assert extract_parties([single])["joint_applicants"] is False


def test_procedural_deadlines():
    result = classify_events(
        [
            event(1, "2007-10-17", "Application for leave and judicial review against a decision IRB - RPD, TOR, 27-SEP-2007 (rec'd 4-OCT-2007), TA5-12457 filed on 17-OCT-2007 Written reasons received by the Applicant"),
            event(2, "2007-11-19", "Applicant's Record Number of copies received/prepared: 1 on behalf of Applicant filed on 19-NOV-2007"),
            event(3, "2007-12-14", "Memorandum of argument on behalf of the respondent filed on 14-DEC-2007 with proof of service on the applicant"),
            event(4, "2008-01-15", "Order rendered by The Honourable Madam Justice Hansen at Ottawa on 15-JAN-2008 granting the application for leave fixing the hearing"),
            event(5, "2008-04-10", "Toronto 10-APR-2008 BEFORE The Honourable Madam Justice Tremblay-Lamer Language: E Before the Court: Judicial Review Result of Hearing: Matter reserved held in Court"),
        ],
        nature="Imm - Appl. for leave & jud. review - IRB - Refugee",
    )
    deadlines = result["deadlines"]
    assert deadlines["notified_date"] == "2007-10-04"
    assert deadlines["days_notice_to_filing"] == 13
    assert deadlines["filing"] == "within_limit"
    assert deadlines["record"] == "within_a_few_days"
    assert deadlines["respondent_memorandum"] == "on_time"
    assert deadlines["hearing_window"] == "within_window"
