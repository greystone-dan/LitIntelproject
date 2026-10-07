"""Regression tests for the deterministic case-type classifier (no database, no network, no model)."""

from __future__ import annotations

import pytest

from backend.case_types import (
    CASE_TYPES,
    STATUS_CLASSIFIED,
    STATUS_INSUFFICIENT,
    STATUS_NOT_IMMIGRATION,
    STATUS_UNCLEAR,
    TAXONOMY_VERSION,
    classify_text,
)

FILLER = (
    "The applicant gave evidence at the hearing and the decision-maker considered the documents filed. "
    "The standard of review is reasonableness, as explained in Canada (Minister of Citizenship and Immigration) v Vavilov. "
    "The Court must ask whether the decision is justified, transparent and intelligible. "
)


def decision(opening: str, *body: str, docket: str = "IMM-1234-20") -> str:
    paragraphs = [f"[{number}] {text}" for number, text in enumerate((opening, *body), start=1)]
    filler = [f"[{len(paragraphs) + index + 1}] {FILLER * 2}" for index in range(8)]
    return (
        f"Decision Content\nDate: 20200101\nDocket: {docket}\nCitation: 2020 FC 1\n"
        + "\n".join(paragraphs + filler)
    )


def classify(text: str, **kwargs):
    return classify_text(text, court=kwargs.pop("court", "FC"), docket=kwargs.pop("docket", "IMM-1234-20"), **kwargs)


def test_cessation_case_beats_generic_refugee_vocabulary() -> None:
    text = decision(
        "The Minister applied under section 108 of the Immigration and Refugee Protection Act [IRPA] to cease the "
        "applicant's refugee protection. The RPD found that the applicant had reavailed herself of the protection of "
        "her country of nationality by renewing her passport.",
        "Paragraph 108(1)(a) of the IRPA provides that refugee protection ceases where the person voluntarily avails "
        "themselves of the protection of the country of nationality. Subsection 108(2) permits the Minister to apply.",
        "The applicant was a Convention refugee under section 96 of the IRPA and a person in need of protection under section 97.",
    )
    result = classify(text)
    assert result.status == STATUS_CLASSIFIED
    assert result.primary_type == "refugee_cessation"
    assert result.primary_detail.startswith("108")


def test_security_inadmissibility_reports_the_paragraph() -> None:
    text = decision(
        "The applicant seeks judicial review of a decision finding him inadmissible on security grounds under "
        "paragraph 34(1)(f) of the Immigration and Refugee Protection Act [IRPA] because he was a member of an organization.",
        "Paragraph 34(1)(f) of the IRPA makes inadmissible a person who is a member of an organization that engages in terrorism. "
        "Membership is given a broad and unrestricted interpretation. Under paragraph 34(1)(f) the Minister need only show reasonable grounds.",
    )
    result = classify(text)
    assert result.primary_type == "inadmissibility_security"
    assert result.primary_detail == "34(1)(f)"


def test_exclusion_article_1f_is_not_a_generic_refugee_claim() -> None:
    text = decision(
        "The RPD excluded the applicants from refugee protection under section 98 of the Immigration and Refugee "
        "Protection Act [IRPA] and Article 1F(b) of the Convention because of a serious non-political crime.",
        "Article 1F(b) of the Convention applies where there are serious reasons for considering the claimant committed a "
        "serious non-political crime outside Canada. Article 1F(b) was applied to the applicant.",
        "The applicants claimed protection under sections 96 and 97 of the IRPA.",
    )
    result = classify(text, court="FC")
    assert result.primary_type == "refugee_exclusion"
    assert "refugee_claim" not in result.secondary_types


def test_rpd_judicial_review_is_a_refugee_claim_even_with_visa_story() -> None:
    text = decision(
        "This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration "
        "and Refugee Board rejecting the applicant's claim under sections 96 and 97 of the Immigration and Refugee Protection Act.",
        "The applicant first came to Canada on a study permit and had earlier applied for a visitor visa. "
        "He later claimed protection. The RPD found his account not credible and found a viable internal flight alternative.",
    )
    result = classify(text)
    assert result.primary_type == "refugee_claim"
    assert result.proceeding == "jr_refugee_protection_division"


def test_removal_deferral_is_labelled_by_the_deferral_question() -> None:
    text = decision(
        "The applicants challenge an officer's refusal to defer their removal from Canada. A stay of removal was granted "
        "pending this application for judicial review. The test for a stay is the Toth test and irreparable harm is required.",
        "The enforcement officer has a limited discretion under section 48 of the Immigration and Refugee Protection Act "
        "to defer removal; the officer is required to enforce a removal order as soon as reasonably practicable.",
        "The applicants rely on a pending application under section 25 of the Act on humanitarian and compassionate grounds.",
    )
    result = classify(text)
    assert result.primary_type == "removal_deferral_stay"


def test_work_permit_case() -> None:
    text = decision(
        "This is an application for judicial review of a refusal of the applicant's work permit application supported by a "
        "Labour Market Impact Assessment (LMIA). The officer found the applicant did not meet the education requirement.",
        "Section 200 of the Immigration and Refugee Protection Regulations governs work permits. Paragraph 200(1)(c) requires "
        "the officer to be satisfied the applicant will leave Canada and the work permit is consistent with the LMIA.",
    )
    result = classify(text)
    assert result.primary_type == "work_permit"


def test_federal_court_decision_with_no_immigration_content_is_not_immigration() -> None:
    text = decision(
        "This is an application for judicial review of a decision of the Canada Revenue Agency under the Income Tax Act "
        "refusing to cancel interest assessed for the 1999 taxation year.",
        "Subsection 220(3.1) of the Income Tax Act permits the Minister of National Revenue to waive interest.",
        docket="T-391-01",
    )
    result = classify_text(text, court="FC", docket="T-391-01")
    assert result.status == STATUS_NOT_IMMIGRATION
    assert result.primary_type is None


def test_short_text_is_insufficient_not_guessed() -> None:
    result = classify_text("The motion is dismissed with costs.", court="FC", docket="IMM-1-20")
    assert result.status == STATUS_INSUFFICIENT


def test_two_equal_case_types_are_reported_unclear_not_forced() -> None:
    text = decision(
        "The applicant sought a study permit and a work permit. The officer refused the study permit application and the "
        "work permit application. Both the study permit and the work permit refusals are challenged.",
    )
    result = classify(text)
    assert result.status == STATUS_UNCLEAR
    assert result.primary_type is None
    assert result.candidates


def test_annex_reproducing_legislation_is_not_discussion() -> None:
    text = decision(
        "This is an application for judicial review of a visa officer's refusal of a visitor visa. The officer was not satisfied "
        "that the applicant would leave Canada at the end of the authorized period under paragraph 179(b) of the Regulations.",
        "The applicant is a citizen of India who applied for a temporary resident visa (TRV).",
    )
    annex = "\nAnnex\n" + "\n".join(
        [f"34 (1) Section 34 is reproduced here for reference. Paragraph 34(1)(f) paragraph 34(1)(f) paragraph 34(1)(f) of the Act {n}" for n in range(30)]
    )
    result = classify(text + annex)
    assert result.primary_type == "visitor_visa"


def test_every_type_has_provisions_or_cues_and_unique_keys() -> None:
    keys = [case_type.key for case_type in CASE_TYPES]
    assert len(keys) == len(set(keys))
    assert all(case_type.provisions or case_type.cues for case_type in CASE_TYPES)
    assert TAXONOMY_VERSION.startswith("case_types_")


@pytest.mark.parametrize("text", ["", None])
def test_empty_text(text) -> None:
    assert classify_text(text).status == STATUS_INSUFFICIENT


def test_criminal_appeal_title_is_not_labelled_as_an_immigration_case() -> None:
    text = decision(
        "The accused pleaded guilty and later says he did not know that a conviction could lead to a removal order under "
        "section 44 of the Immigration and Refugee Protection Act. This appeal concerns when a guilty plea may be withdrawn.",
        "The appellant is a permanent resident and a foreign national in the sense of the Act.",
    )
    result = classify_text(text, court="SCC", title="R. v. Wong")
    assert result.status == STATUS_NOT_IMMIGRATION


def test_appeal_court_decision_with_no_immigration_title_and_few_provisions_is_unclear() -> None:
    text = decision(
        "The appellant challenges a decision of a federal tribunal. In passing the Immigration and Refugee Protection Act, "
        "section 34, is mentioned as an example of a security provision. The test for a stay is irreparable harm.",
    )
    result = classify_text(text, court="FCA", title="Baragar v. Canada (Attorney General)")
    assert result.status == STATUS_UNCLEAR
    assert result.primary_type is None


def test_refugee_claim_reports_the_issue_the_court_calls_determinative() -> None:
    text = decision(
        "This is an application for judicial review of a decision of the Refugee Protection Division rejecting the applicant's "
        "claim under sections 96 and 97 of the Immigration and Refugee Protection Act.",
        "The determinative issue in this case is the availability of an internal flight alternative (IFA) in Mumbai.",
        "The RPD found a viable IFA. The applicant says the IFA is not viable. The IFA test has two prongs.",
    )
    result = classify(text)
    assert result.primary_type == "refugee_claim"
    assert result.issues and result.issues[0] == "internal_flight_alternative"


def test_second_main_type_when_two_provisions_are_both_at_issue() -> None:
    text = decision(
        "The applicant, a permanent resident, was found inadmissible for serious criminality under paragraph 36(1)(a) "
        "of the Immigration and Refugee Protection Act [IRPA] and for organized criminality under paragraph 37(1)(a) of "
        "the IRPA.",
        "The Immigration Division concluded under paragraph 36(1)(a) and paragraph 37(1)(a) that the applicant is "
        "inadmissible. Paragraph 36(1)(a) applies to the conviction; paragraph 37(1)(a) applies to the membership.",
        "On the first ground, section 36(1)(a) is met. On the second, section 37(1)(a) is met.",
    )
    result = classify(text, court="FCA")
    assert result.status == STATUS_CLASSIFIED
    assert {result.primary_type, result.second_type} == {"inadmissibility_serious_criminality", "inadmissibility_organized_crime"}
    assert result.second_detail in {"36(1)(a)", "37(1)(a)"}


def test_single_issue_decision_has_no_second_main_type() -> None:
    text = decision(
        "The Minister applied under section 108 of the Immigration and Refugee Protection Act [IRPA] to cease the "
        "applicant's refugee protection because she reavailed herself of the protection of her country.",
        "Paragraph 108(1)(a) of the IRPA applies where the person voluntarily reavails.",
    )
    result = classify(text)
    assert result.primary_type == "refugee_cessation"
    assert result.second_type is None


def test_prra_officer_deciding_an_h_and_c_application_is_an_h_and_c_case() -> None:
    text = decision(
        "This is an application for judicial review of the decision of a Pre-Removal Risk Assessment officer who "
        "rejected the applicant's humanitarian and compassionate (H&C) application under subsection 25(1) of the "
        "Immigration and Refugee Protection Act [IRPA].",
        "The officer found the hardship in Mexico insufficient under subsection 25(1) and considered the risk factors "
        "described in sections 96 and 97 of the IRPA and section 112 of the IRPA in the pre-removal risk assessment.",
    )
    assert classify(text).primary_type == "humanitarian_compassionate"


def test_motion_to_intervene_is_a_procedural_matter() -> None:
    text = decision(
        "These reasons concern a motion for leave to intervene in the appeal of a decision about inadmissibility under "
        "paragraph 37(1)(a) of the Immigration and Refugee Protection Act [IRPA].",
        "The proposed intervener argues about paragraph 37(1)(a) and section 37 of the IRPA and section 36 of the IRPA.",
    )
    assert classify(text, court="FCA", title="Canada (Public Safety) v. Smith").primary_type == "court_procedure_only"


def test_judicial_review_of_a_prra_decision_is_a_prra_case() -> None:
    text = decision(
        "The applicant challenges a decision by a Senior Immigration Officer rejecting his pre-removal risk assessment "
        "application made under section 112 of the Immigration and Refugee Protection Act [IRPA].",
        "The officer applied sections 96 and 97 of the IRPA and section 113 of the IRPA. Section 112 of the IRPA "
        "and section 113 of the IRPA require a risk assessment before removal; the officer found no risk.",
    )
    assert classify(text).primary_type == "pre_removal_risk_assessment"


def test_immigration_department_party_without_a_named_statute_is_unclear_not_dismissed() -> None:
    text = decision(
        "The Crown seeks an order for an extension of time within which to serve and file a requisition for a hearing.",
        "The respondent did not object to the extension of time sought by the Crown in this proceeding.",
    ).replace("IMM-1234-20", "T-87-01")
    result = classify_text(text, court="FC", title="Canada (Minister of Citizenship and Immigration) v. Smith", docket="T-87-01")
    assert result.status == STATUS_UNCLEAR
    plain = classify_text(text, court="FC", title="Smith v. Canada (Revenue Agency)", docket="T-87-01")
    assert plain.status == STATUS_NOT_IMMIGRATION


def test_claim_issues_are_empty_when_the_court_names_no_determinative_issue() -> None:
    text = decision(
        "The applicant seeks judicial review of a decision of the Refugee Protection Division refusing his claim under "
        "sections 96 and 97 of the Immigration and Refugee Protection Act [IRPA].",
        "The RPD found the applicant not credible and doubted his story. The credibility findings were about the "
        "inconsistencies in his testimony and the omissions in his Basis of Claim narrative.",
    )
    result = classify(text)
    assert result.primary_type == "refugee_claim"
    assert result.issues == []

def test_imm_docket_in_text_header_is_never_not_immigration_when_docket_missing():
    text = ("File numbers IMM-1234-20 Decision Content Date: 20210101 Docket: IMM-1234-20 Citation: 2021 FC 1 "
            "BETWEEN: A and Canada (Citizenship and Immigration). " + "The applicant seeks judicial review of an officer's decision. " * 20)
    result = classify_text(text, court="FC", title="A v. Canada (Citizenship and Immigration)", docket=None)
    assert result.status != "not_immigration"


def test_judicial_review_sentence_names_the_subject():
    from backend.case_types.classifier import jr_subject_type
    assert jr_subject_type("[1] This is an application for judicial review of a decision of the Refugee Protection Division.") == "refugee_claim"
    assert jr_subject_type("[1] An application for judicial review of a refusal of her humanitarian and compassionate (H&C) application.") == "humanitarian_compassionate"
    # The Act's own name is not a refugee-claim cue, a deferral or mandamus is not the subject, and two subjects name none.
    assert jr_subject_type("[1] Judicial review under the Immigration and Refugee Protection Act of a refusal to process.") is None
    assert jr_subject_type("[1] Judicial review of a refusal to defer removal pending an H&C application.") is None
    assert jr_subject_type("[1] Judicial review of a PRRA decision after the Refugee Protection Division refused the claim.") is None
    assert jr_subject_type("[1] Judicial review of a decision of the Immigration Appeal Division on a refugee sponsorship.") is None


def test_opening_subject_rules_pick_one_subject_and_stay_silent_on_two():
    from backend.case_types.classifier import opening_subject_type
    assert opening_subject_type("[1] Les demandeurs sollicitent le contrôle judiciaire d'une décision de la Section d'appel des réfugiés.") == "refugee_claim"
    assert opening_subject_type("[1] Judicial review of a CBSA officer's refusal to defer her removal pending an H&C application.") == "removal_deferral_stay"
    assert opening_subject_type("[1] Judicial review of a decision of the Immigration Appeal Division on a removal order, appealed on H&C grounds.") == "removal_admissibility_proceedings"
    assert opening_subject_type("[1] She claimed refugee status in 2005. This is a judicial review of the refusal of her H&C application.") == "humanitarian_compassionate"
    assert opening_subject_type("[1] The officer refused the study permit and the work permit.") is None
    assert opening_subject_type("[1] Mr. Smith is a citizen of Peru.") is None


def test_stay_motion_opening_is_a_stay_not_its_underlying_ground() -> None:
    text = decision(
        "The Applicants seek an interim stay, pending their application for leave and judicial review, of their removal from "
        "Canada. They rely on a humanitarian and compassionate application under section 25(1) of the Act that is outstanding. "
        "The test for a stay is serious issue, irreparable harm and balance of convenience.",
    )
    assert classify(text).primary_type == "removal_deferral_stay"


def test_referral_to_admissibility_hearing_is_removal_proceedings() -> None:
    text = decision(
        "The applicant seeks judicial review of a decision of the Minister's delegate to refer him to an admissibility hearing "
        "under subsection 44(2) of the Act. The delegate weighed humanitarian and compassionate factors under section 25(1) of the Act "
        "but found the referral warranted because of a conviction under section 36(1)(a).",
    )
    assert classify(text).primary_type == "removal_admissibility_proceedings"


def test_appeal_court_costs_assessment_with_immigration_party_is_court_procedure() -> None:
    text = decision("This is an assessment of costs pursuant to a Judgment of the Court dismissing the appeal with costs.", docket="A-12-18")
    result = classify_text(text, court="FCA", title="Cabral v. Canada (Citizenship and Immigration)")
    assert result.status == STATUS_CLASSIFIED
    assert result.primary_type == "court_procedure_only"


def test_appeal_court_decision_with_no_immigration_subject_is_not_immigration() -> None:
    text = decision("The appellant appeals the striking of a claim for damages against the Crown.", docket="A-12-18")
    result = classify_text(text, court="FCA", title="Almacen v. Canada")
    assert result.status == "not_immigration"


def test_refugee_division_decision_without_statute_names_is_still_typed() -> None:
    text = decision("The claimant, a citizen of Cuba, alleges a well-founded fear of persecution by reason of political opinion.", docket="MA9-09861")
    result = classify_text(text, court="RPD", title="MA9-09861")
    assert result.status != "not_immigration"


def test_appeal_court_matter_under_another_regime_is_not_immigration() -> None:
    text = decision(
        "The Minister suspected the appellants would travel by air to commit a terrorism offence and listed them under the Secure Air Travel Act.",
        "The Immigration and Refugee Protection Act, section 34, is mentioned only in passing.",
        docket="A-12-18",
    )
    result = classify_text(text, court="FCA", title="Brar v. Canada (Public Safety and Emergency Preparedness)")
    assert result.status == "not_immigration"
