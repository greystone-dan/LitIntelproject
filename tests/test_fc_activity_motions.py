from datetime import date

import pytest

from scripts.classify_fc_activity import ActivityEvent, _clean_judge_name, _judge_name, classify_events
from scripts.fc_activity_extractors import extract_motions, motion_type


def event(doc_id, doc_date, text, *, docno=None, re_no=None):
    return ActivityEvent(1, "IMM-1-15", "Example v. Canada", doc_id, date.fromisoformat(doc_date), text, re_no=re_no, docno=docno)


def only(register):
    assert len(register["motions"]) == 1
    return register["motions"][0]


def test_motion_linked_by_document_number_with_judge_and_timing():
    motion = only(
        extract_motions(
            [
                event(5, "2013-03-15", "Notice of Motion contained within a Motion Record on behalf of Applicant in writing to be dealt with in the Toronto local office for an extension of time to file the applicants record filed on 15-MAR-2013", docno="4"),
                event(9, "2013-03-29", "Order dated 29-MAR-2013 rendered by Martha Milczynski, Prothonotary Matter considered without personal appearance The Court's decision is with regard to Motion in writing Doc. No. 4 Result: granted Applicant granted extension of 15 days"),
            ]
        )
    )
    assert motion["type"] == "extension_of_time"
    assert motion["filer"] == "applicant"
    assert motion["in_writing"] is True
    assert motion["outcome"] == "granted"
    assert motion["link"] == "doc_number"
    assert motion["judge"]["key"] == "milczynski"
    assert motion["days_to_decision"] == 14


def test_stay_hearing_result_then_formal_order_is_one_motion():
    motion = only(
        extract_motions(
            [
                event(5, "2011-11-08", "Notice of Motion contained within a Motion Record on behalf of Applicant returnable (but no hearing date indicated at this time) for a stay of execution of the removal order scheduled for 12-NOV-2011 to Bogota", docno="5"),
                event(15, "2011-11-14", "Toronto 14-NOV-2011 BEFORE The Honourable Mr. Justice Hughes Language: E Before the Court: Motion Doc. No. 5 on behalf of Applicant Result of Hearing: Matter dismissed held in Court"),
                event(16, "2011-11-14", "Order rendered by The Honourable Mr. Justice Hughes at Toronto on 10-NOV-2011 dismissing the stay of execution Decision filed on 14-NOV-2011"),
            ]
        )
    )
    assert motion["type"] == "stay_of_removal"
    assert motion["outcome"] == "dismissed"
    assert motion["order_doc_id"] == 16
    assert motion["judge"]["key"] == "hughes"


def test_leave_order_with_extension_request_is_not_a_motion_ruling():
    register = extract_motions(
        [event(9, "2006-07-14", "Order rendered by The Honourable Madam Justice Layden-Stevenson at Ottawa on 14-JUL-2006 granting the application for leave with a request for an extension of time (R.6) fixing the hearing")]
    )
    assert register["motions"] == []


def test_old_generic_wording_links_by_document_number():
    motion = only(
        extract_motions(
            [
                event(6, "1995-09-01", "Notice of Motion on behalf of Applicant pursuant to R. 324 for an Order AMENDING THE RELIEF THE APPLICATION FOR LEAVE AND FOR JUDICIAL REVIEW filed on 01-SEP-1995", docno="11"),
                event(9, "1995-09-11", "Order of the Court/ The Honourable Mr. Justice Nadon rendered at Ottawa on 11-SEP-1995 and granting the application for an extension of time 11 which reads as follow: The applicants shall have until Sept.29,1995 to amend"),
            ]
        )
    )
    assert motion["type"] == "amendment"
    assert motion["outcome"] == "granted"
    assert motion["link"] == "doc_number"
    assert motion["judge"]["key"] == "nadon"


def test_withdrawals_and_conditional_wording():
    withdrawn = only(
        extract_motions(
            [
                event(25, "2010-05-19", "Notice of Motion on behalf of Applicant returnable (but no hearing date indicated at this time) for a stay of execution of removal order.", docno="19"),
                event(29, "2010-05-21", "Notice of discontinuance of the Applicant's motion for a stay of removal on behalf of the applicant filed on 21-MAY-2010"),
            ]
        )
    )
    assert withdrawn["outcome"] == "withdrawn"
    pending = only(
        extract_motions(
            [
                event(7, "2010-12-07", "Notice of Motion contained within a Motion Record on behalf of Applicant in writing for an Order TO RECONSIDER THE ORDER DATED 30-NOV-2010.", docno="4"),
                event(15, "2010-12-20", "Letter from counsel for applicant dated 19-DEC-2010 Applicant will be out of time to rely on R.397 if current motion is withdrawn and refiled"),
            ]
        )
    )
    assert pending["outcome"] != "withdrawn"


def test_motion_discontinuance_does_not_close_the_file():
    result = classify_events(
        [
            event(1, "2010-01-05", "Application for leave and judicial review against a decision IRB-RPD filed on 05-JAN-2010"),
            event(25, "2010-05-19", "Notice of Motion on behalf of Applicant for a stay of execution of removal order.", docno="19"),
            event(29, "2010-05-21", "Notice of discontinuance of the Applicant's motion for a stay of removal on behalf of the applicant filed on 21-MAY-2010"),
        ]
    )
    assert result["full_history_resolution"]["status"] != "discontinued"


def test_reconsidered_leave_refusal_lets_the_merits_result_stand():
    result = classify_events(
        [
            event(1, "2010-09-01", "Application for leave and judicial review against a decision visa officer, Embassy of Canada Damascus filed on 01-SEP-2010"),
            event(6, "2010-11-29", "(Final decision) Order rendered by The Honourable Mr. Justice Kelen at Ottawa on 29-NOV-2010 dismissing the application for leave Decision endorsed on the record"),
            event(7, "2010-12-07", "Notice of Motion contained within a Motion Record on behalf of Applicant in writing for an Order TO RECONSIDER THE ORDER DATED 30-NOV-2010.", docno="4"),
            event(18, "2011-01-06", "Order rendered by The Honourable Mr. Justice Kelen at Ottawa on 06-JAN-2011 granting the motion for reconsideration Decision filed on 06-JAN-2011"),
            event(40, "2011-07-06", "(Final decision) Reasons for Judgment and Judgment dated 06-JUL-2011 rendered by The Honourable Mr. Justice Beaudry Matter considered with personal appearance The Court's decision is with regard to Judicial Review Result: dismissed"),
        ]
    )
    assert result["leave_decision"]["result"] == "granted"
    assert result["leave_decision"]["rule"] == "leave_refusal_reconsidered"
    assert result["judicial_review_result"]["result"] == "dismissed"
    assert result["full_history_resolution"]["status"] == "judicial_review_dismissed"


def test_granted_motion_to_allow_the_application_settles_the_file():
    result = classify_events(
        [
            event(1, "2012-10-25", "Application for leave and judicial review against a decision IRB/RPD filed on 25-OCT-2012"),
            event(8, "2013-07-30", "Order rendered by The Honourable Mr. Justice Manson at Ottawa on 30-JUL-2013 granting the application for leave fixing the hearing"),
            event(10, "2013-10-01", "Notice of Motion contained within a Motion Record on behalf of Respondent in writing to be dealt with in the Toronto local office for an Order granting the application for judicial review; and other relief filed on 01-OCT-2013", docno="8"),
            event(16, "2013-10-07", "Order dated 07-OCT-2013 rendered by The Honourable Mr. Justice Hughes Matter considered without personal appearance The Court's decision is with regard to Motion in writing Doc. No. 8 Result: granted Filed on 07-OCT-2013"),
        ]
    )
    assert result["consent_disposition"]["status"] == "granted"
    assert result["consent_disposition"]["date"] == "2013-10-07"
    assert result["full_history_resolution"]["status"] == "resolved_by_consent"


def test_letters_quoting_leave_are_not_leave_decisions():
    result = classify_events(
        [
            event(1, "2017-03-01", "Application for leave and judicial review against a decision IRB-RAD filed on 01-MAR-2017"),
            event(5, "2017-05-15", "Letter from RESPONDENT dated 15-MAY-2017 ...DO NOT OPPOSE LEAVE...RESERVES RIGHT TO FILE SUBMISSIONS IF LEAVE GRANTED... received on 15-MAY-2017"),
            event(9, "2017-07-20", "(Final decision) Order rendered by The Honourable Mr. Justice Diner at Ottawa on 20-JUL-2017 dismissing the application for leave Decision endorsed on the record"),
        ]
    )
    assert result["leave_decision"]["result"] == "refused"
    assert result["judge_roles"]["leave_judge"]["key"] == "diner"


@pytest.mark.parametrize(
    "text,key",
    [
        ("(Décision finale) Ordonnance rendu(e) par L'honorable Orville Frenette, juge suppléant à Ottawa le 24-MAI-2009", "frenette"),
        ("(Final decision) Order of the Court/ The Honourable Mr. Justice MacGuigan acting as an ex officio judge of the Trial Division", "macguigan"),
        ("(Décision finale) Ordonnance de la Cour/ Monsieur le juge Noël rendu(e) à Ottawa le 22-MAR-1994", "noel"),
        ("(Décision finale) Motifs de jugement et jugement en date du 17-OCT-2022 rendus par Monsieur le juge McHaffie Affaire considérée", "mchaffie"),
        ("Order of the Court/ Peter Giles, Esq., Associate Senior Prothonotary rendered at Toronto", "giles"),
        ("Order rendered by Associate Chief Justice Gagné at Ottawa on 06-JUL-2022", "gagne"),
        ("Order rendered by Mandy Aylen, Associate Judge at Ottawa on 10-AUG-2023", "aylen"),
        ("Ottawa 16-MAR-2007 En présence de Monsieur le juge S. Noël Langue : F", "s-noel"),
        ("Oral directions of the Court: Kevin Aalto, Prothonotary dated 09-JUN-2021 directing", "aalto"),
    ],
)
def test_judge_names_across_registry_wordings(text, key):
    assert _clean_judge_name(_judge_name(text))["key"] == key


@pytest.mark.parametrize(
    "relief,expected",
    [
        ("a stay of execution of the removal order scheduled for 12-NOV-2011", "stay_of_removal"),
        ("Judgment on consent", "judgment_on_consent"),
        ("an Order 1. Leave is granted, the judicial review is allowed and the decision set aside", "judgment_on_consent"),
        ("an extension of time to file the Applicant's Record", "extension_of_time"),
        ("an Order TO RECONSIDER THE ORDER DATED 30-NOV-2010", "reconsideration"),
        ("an Order dismissing the Application for Leave and Judicial Review", "dismiss_or_strike"),
        ("prorogation de délai pour déposer le dossier de la partie demanderesse", "extension_of_time"),
    ],
)
def test_motion_types(relief, expected):
    assert motion_type(relief) == expected
