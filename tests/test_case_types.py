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
