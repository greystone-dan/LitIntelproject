from datetime import date
from types import SimpleNamespace

from backend.legal_tagger import LegalTagger
from scripts.tag_cases import build_case_tags


def test_legal_tagger_extracts_multidimensional_immigration_tags():
    text = """
    This application for judicial review challenges an RPD refugee decision.
    The applicant alleges procedural fairness and unreasonable credibility findings
    under sections 96 and 97 of the IRPA. The application is allowed, the decision
    is quashed, and the matter is remitted for redetermination under Vavilov.
    """

    result = LegalTagger().tag(text, language="en")
    values = {(tag.category, tag.value) for tag in result}

    assert ("legal_area", "immigration_refugee") in values
    assert ("proceeding", "judicial_review") in values
    assert ("tribunal", "rpd") in values
    assert ("issue", "procedural_fairness") in values
    assert ("issue", "credibility") in values
    assert ("standard_of_review", "reasonableness") in values
    assert ("outcome", "allowed") in values
    assert ("remedy", "quashing") in values
    assert ("remedy", "redetermination") in values
    assert ("statute", "irpa_s_96") in values
    assert ("statute", "irpa_s_97") in values
    assert ("authority", "vavilov") in values
    assert all(tag.score > 0 for tag in result)
    assert all(tag.evidence for tag in result)

def test_tagger_v2_captures_section_97_analysis_and_exceptions():
    text = (
        "The RAD failed to conduct an individualized inquiry into the applicant's "
        "prospective personalized risk. It conflated the reason for targeting with "
        "the risk itself and treated the threats as generalized risk. The medical "
        "exception in subparagraph 97(1)(b)(iv) was also considered."
    )

    tags = LegalTagger().tag(text)
    values = {(tag.category, tag.value) for tag in tags}

    assert ("issue", "individualized_risk_inquiry") in values
    assert ("issue", "prospective_risk") in values
    assert ("issue", "generalized_risk") in values
    assert ("issue", "reason_for_targeting_vs_risk") in values
    assert ("issue", "medical_exception") in values
    assert all(tag.taxonomy_version == "ca_legal_v2" for tag in tags)

def test_tagger_v2_captures_exclusion_and_complicity_framework():
    text = (
        "Under Article 1F(a), there were serious reasons for considering whether "
        "the claimant made a voluntary, significant and knowing contribution to "
        "crimes against humanity. Duress and superior orders were also raised."
    )

    tags = LegalTagger().tag(text)
    values = {(tag.category, tag.value) for tag in tags}

    assert ("issue", "exclusion_article_1fa") in values
    assert ("issue", "serious_reasons_for_considering") in values
    assert ("issue", "complicity_significant_contribution") in values
    assert ("issue", "duress") in values
    assert ("issue", "superior_orders") in values

def test_tagger_v2_captures_cbsa_detention_and_removal_operations():
    text = (
        "CBSA alleged that the detainee was a danger to the public and unlikely "
        "to appear. At the detention review, counsel proposed a bondsperson and "
        "community case management as alternatives to detention. Separately, a "
        "temporary suspension of removals and travel document impediment delayed "
        "enforcement of the deportation order."
    )

    tags = LegalTagger().tag(text)
    values = {(tag.category, tag.value) for tag in tags}

    assert ("agency", "cbsa") in values
    assert ("detention_ground", "danger_to_public") in values
    assert ("detention_ground", "flight_risk") in values
    assert ("proceeding", "detention_review") in values
    assert ("cbsa_program", "alternatives_to_detention") in values
    assert ("release_mechanism", "bondsperson") in values
    assert ("release_mechanism", "community_case_management") in values
    assert ("enforcement_impediment", "temporary_suspension_removals") in values
    assert ("enforcement_impediment", "travel_documents") in values
    assert ("enforcement_action", "deportation_order") in values

def test_tagger_v2_captures_irb_guideline_and_procedural_concepts():
    text = (
        "Chairperson's Guideline 8 required procedural accommodations, "
        "trauma-informed adjudication and an intersectional assessment of a "
        "vulnerable person. The decision also addressed the best interests of "
        "the child and SOGIESC."
    )

    tags = LegalTagger().tag(text)
    values = {(tag.category, tag.value) for tag in tags}

    assert ("guideline", "irb_chairperson_guideline_8") in values
    assert ("issue", "procedural_accommodation") in values
    assert ("issue", "trauma_informed_adjudication") in values
    assert ("issue", "intersectionality") in values
    assert ("issue", "vulnerable_person") in values
    assert ("issue", "best_interests_child") in values
    assert ("issue", "sogiesc") in values


def test_legal_tagger_covers_broad_legal_topics_and_french():
    text = """
    La Cour accueille l'appel concernant la Charte canadienne. The criminal appeal
    concerns section 7 and section 15 of the Charter, expert evidence, and an
    injunction. The standard is palpable and overriding error.
    """

    values = {(tag.category, tag.value) for tag in LegalTagger().tag(text, language="fr")}

    assert ("language", "fr") in values
    assert ("legal_area", "criminal") in values
    assert ("legal_area", "constitutional_charter") in values
    assert ("proceeding", "appeal") in values
    assert ("evidence", "expert_evidence") in values
    assert ("remedy", "injunction") in values
    assert ("standard_of_review", "palpable_overriding_error") in values
    assert ("statute", "charter_s_7") in values
    assert ("statute", "charter_s_15") in values


def test_build_case_tags_includes_structured_metadata_tags():
    case = SimpleNamespace(
        id=42,
        title="Doe v Canada",
        court="FC",
        jurisdiction="Canada",
        date=date(2024, 2, 3),
        citation="2024 FC 123",
        summary=None,
        full_text="Application for judicial review dismissed.",
        language="en",
        source_type="a2aj_parquet",
        metadata_json={
            "judge": "Justice Example",
            "docket_number": "IMM-1234-24",
            "topic_keywords": ["refugee_protection"],
        },
        cases_cited=["2019 SCC 65"],
        citing_cases_count=7,
    )

    tags = build_case_tags(case, LegalTagger())
    values = {(tag.category, tag.value) for tag in tags}

    assert ("court", "fc") in values
    assert ("decision_year", "2024") in values
    assert ("source", "a2aj_parquet") in values
    assert ("judge", "justice_example") in values
    assert ("docket_type", "imm") in values
    assert ("citation_network", "cites_cases") in values
    assert ("citation_network", "cited_by_cases") in values
    assert ("legacy_topic", "refugee_protection") in values


def test_legal_tagger_captures_cbsa_program_and_removal_effects():
    text = """
    The CBSA prepared a subsection 44(1) report for the Minister of Public Safety.
    A deportation order became enforceable, but the applicant seeks a stay of removal.
    The Court stayed the scheduled removal, delaying enforcement pending judicial review.
    """

    values = {(tag.category, tag.value) for tag in LegalTagger().tag(text)}

    assert ("agency", "cbsa") in values
    assert ("minister", "mpsep") in values
    assert ("cbsa_program", "section_44_report") in values
    assert ("cbsa_program", "removals") in values
    assert ("enforcement_action", "deportation_order") in values
    assert ("enforcement_impediment", "judicial_stay") in values
    assert ("program_impact", "removal_delayed") in values


def test_legal_tagger_captures_legislation_international_law_and_country_entities():
    text = """
    Sections 34 and 37 of IRPA and section 245 of the Immigration and Refugee
    Protection Regulations (IRPR) are discussed. The claimant from Bangladesh
    belonged to the Bangladesh Nationalist Party (BNP), while the Nigerian record
    discusses the Indigenous People of Biafra (IPOB). Article 3 of the Convention
    against Torture and the Refugee Convention prohibit refoulement.
    """

    result = LegalTagger().tag(text)
    values = {(tag.category, tag.value) for tag in result}

    assert ("statute", "irpa_s_34") in values
    assert ("statute", "irpa_s_37") in values
    assert ("regulation", "irpr_s_245") in values
    assert ("international_instrument", "convention_against_torture") in values
    assert ("international_instrument", "refugee_convention") in values
    assert ("issue", "non_refoulement") in values
    assert ("country", "bangladesh") in values
    assert ("country", "nigeria") in values
    assert ("organization", "bangladesh_nationalist_party") in values
    assert ("organization", "ipob") in values
    assert all(tag.evidence for tag in result)


def test_legal_tagger_preserves_nested_statute_subsections():
    text = "The panel relied on IRPA section 3(2)(a) and IRPR subsection 245(1)(c)."

    values = {(tag.category, tag.value) for tag in LegalTagger().tag(text)}

    assert ("statute", "irpa_s_3(2)(a)") in values
    assert ("regulation", "irpr_s_245(1)(c)") in values
