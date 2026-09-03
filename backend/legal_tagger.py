"""Deterministic, evidence-bearing tags for Canadian legal decisions."""

from __future__ import annotations

import re
from dataclasses import dataclass


TAXONOMY_VERSION = "ca_legal_v2"


@dataclass(frozen=True)
class LegalTag:
    category: str
    value: str
    score: float
    evidence: str
    source: str = "text_rule"
    taxonomy_version: str = TAXONOMY_VERSION


@dataclass(frozen=True)
class LegalTagOccurrence:
    category: str
    value: str
    score: float
    evidence: str
    offset_start: int
    offset_end: int
    source: str = "text_rule"
    taxonomy_version: str = TAXONOMY_VERSION

    def as_tag(self) -> LegalTag:
        return LegalTag(
            self.category,
            self.value,
            self.score,
            self.evidence,
            self.source,
            self.taxonomy_version,
        )


@dataclass(frozen=True)
class TagRule:
    category: str
    value: str
    pattern: str
    score: float = 1.0


RULES = (
    # Legal areas and proceedings
    TagRule("legal_area", "immigration_refugee", r"\b(?:IRPA|IRPR|immigration|refugee|asylum|removal|inadmissib\w*)\b", 0.95),
    TagRule("legal_area", "criminal", r"\b(?:criminal|Criminal Code|indictable|summary conviction)\b", 0.9),
    TagRule("legal_area", "constitutional_charter", r"\b(?:Canadian Charter|Charte canadienne|Charter (?:right|challenge|claim)|constitution(?:al)?)\b", 0.9),
    TagRule("proceeding", "judicial_review", r"\b(?:application for (?:leave and )?judicial review|contr[oô]le judiciaire)\b"),
    TagRule("proceeding", "appeal", r"\b(?:appeal|appel)\b", 0.9),
    TagRule("proceeding", "admissibility_hearing", r"\b(?:admissibility hearing|enqu[eê]te en mati[eè]re d['’]immigration)\b"),
    TagRule("proceeding", "detention_review", r"\b(?:detention review|contr[oô]le des motifs de d[eé]tention)\b"),
    TagRule("proceeding", "prra", r"\b(?:pre[- ]removal risk assessment|PRRA|examen des risques avant renvoi|ERAR)\b"),
    TagRule("proceeding", "humanitarian_compassionate", r"\b(?:humanitarian and compassionate|H\s*&\s*C|motifs d['’]ordre humanitaire)\b"),

    # Procedural posture
    TagRule("procedural_posture", "leave_application", r"\b(?:application for leave|demande d['’]autorisation)\b"),
    TagRule("procedural_posture", "motion", r"\b(?:motion|requ[eê]te)\b(?:\s+to\s+(?:stay|strike|amend|dismiss))?"),
    TagRule("procedural_posture", "interlocutory_motion", r"\b(?:interlocutory motion|motion on an interlocutory basis|requ[eê]te interlocutoire)\b"),
    TagRule("procedural_posture", "judicial_review_application", r"\b(?:application for judicial review|demande de contr[oô]le judiciaire)\b"),

    # Immigration status
    TagRule("immigration_status", "permanent_resident", r"\b(?:permanent resident|landed immigrant|r[eé]sident permanent)\b"),
    TagRule("immigration_status", "temporary_resident", r"\btemporary resident\b|\br[eé]sident temporaire\b"),
    TagRule("immigration_status", "refugee_claimant", r"\b(?:refugee claimant|refugee protection claimant|demandeur d['’]asile)\b"),
    TagRule("immigration_status", "protected_person", r"\b(?:protected person|person in need of protection|personne prot[eé]g[eé]e)\b"),
    TagRule("immigration_status", "foreign_national", r"\b(?:foreign national|ressortissant [eé]tranger)\b"),
    TagRule("immigration_status", "canadian_citizen", r"\b(?:Canadian citizen|citoyen canadien|citoyenne canadienne)\b"),
    TagRule("immigration_status", "refugee", r"\b(?:Convention refugee|recognized refugee|r[eé]fugi[eé] au sens de la Convention)\b"),
    TagRule("immigration_status", "visitor", r"\b(?:visitor|visiteur)\b"),
    TagRule("immigration_status", "international_student", r"\b(?:international student|foreign student|student permit holder|[eé]tudiant [eé]tranger)\b"),
    TagRule("immigration_status", "temporary_worker", r"\b(?:temporary foreign worker|foreign worker|work permit holder|travailleur [eé]tranger)\b"),

    # Claimant characteristics and vulnerability
    TagRule("claimant_characteristic", "child", r"\b(?:child claimant|minor claimant|claimant who is a child|enfant demandeur|mineur demandeur)\b"),
    TagRule("claimant_characteristic", "elderly_person", r"\b(?:elderly claimant|elderly person|older claimant|personne [aâ]g[eé]e)\b"),
    TagRule("claimant_characteristic", "disability", r"\b(?:claimant with a disability|person with a disability|disability-related accommodation|personne handicap[eé]e)\b"),
    TagRule("claimant_characteristic", "single_parent", r"\b(?:single parent|single mother|single father|parent seul|m[eè]re monoparentale|p[eè]re monoparental)\b"),
    TagRule("claimant_characteristic", "pregnancy", r"\b(?:pregnant claimant|pregnant woman|pregnancy|grossesse|enceinte)\b"),
    TagRule("claimant_characteristic", "family_unit", r"\b(?:family unit|family members? accompanying)\b"),
    TagRule("claimant_factor", "psychological_condition", r"\b(?:psychological condition|mental health condition|post[- ]traumatic stress disorder|PTSD|psychological vulnerability)\b"),
    TagRule("claimant_factor", "economic_vulnerability", r"\b(?:economic vulnerability|financial hardship|extreme poverty|economic circumstances)\b"),
    TagRule("case_history", "travel_history", r"\b(?:travel history|immigration travel history|historique de voyage)\b"),
    TagRule("case_history", "previous_refugee_claim", r"\b(?:previous refugee claim|prior refugee claim|earlier refugee claim|demande d['’]asile ant[eé]rieure)\b"),
    TagRule("case_history", "previous_immigration_application", r"\b(?:previous immigration application|prior immigration application|earlier application for permanent residence)\b"),
    TagRule("case_history", "visa_refusal", r"\b(?:visa refusal|visa was refused|refusal of a visa|refus de visa)\b"),
    TagRule("case_history", "entry_to_canada", r"\b(?:entry to Canada|entered Canada|arrival in Canada|entr[eé]e au Canada)\b"),
    TagRule("family_relationship", "spouse", r"\b(?:spouse|spousal|husband|wife|conjoint[e]?)\b"),
    TagRule("family_relationship", "common_law_partner", r"\b(?:common[- ]law partner|common[- ]law spouse|conjoint[e]? de fait)\b"),
    TagRule("family_relationship", "dependent_child", r"\b(?:dependent child|dependent children|enfant [aà] charge)\b"),
    TagRule("family_relationship", "family_separation", r"\b(?:family separation|separation from family|separation familiale)\b"),

    # Institutions and responsible ministers
    TagRule("tribunal", "rpd", r"\b(?:RPD|Refugee Protection Division|Section de la protection des r[eé]fugi[eé]s)\b"),
    TagRule("tribunal", "rad", r"\b(?:RAD|Refugee Appeal Division|Section d['’]appel des r[eé]fugi[eé]s)\b"),
    TagRule("tribunal", "id", r"\b(?:Immigration Division|Section de l['’]immigration)\b"),
    TagRule("tribunal", "iad", r"\b(?:IAD|Immigration Appeal Division|Section d['’]appel de l['’]immigration)\b"),
    TagRule("agency", "cbsa", r"\b(?:CBSA|Canada Border Services Agency|ASFC|Agence des services frontaliers du Canada)\b"),
    TagRule("agency", "ircc", r"\b(?:IRCC|Immigration,? Refugees and Citizenship Canada|Citizenship and Immigration Canada|CIC)\b"),
    TagRule("minister", "mpsep", r"\b(?:MPSEP|Minister of Public Safety(?: and Emergency Preparedness)?|Ministre de la S[eé]curit[eé] publique)\b"),
    TagRule("minister", "mci", r"\b(?:MCI|Minister of Citizenship and Immigration|Minister of Immigration, Refugees and Citizenship)\b"),

    # Refugee protection doctrine
    TagRule("issue", "credibility", r"\b(?:credibility|credible|cr[eé]dibilit[eé])\b"),
    TagRule("issue", "procedural_fairness", r"\b(?:procedural fairness|natural justice|fairness|[eé]quit[eé] proc[eé]durale|justice naturelle)\b"),
    TagRule("issue", "state_protection", r"\b(?:state protection|protection de l['’][ÉEée]tat|adequate protection)\b"),
    TagRule("issue", "internal_flight_alternative", r"\b(?:internal flight alternative|internal relocation alternative|IFA|possibilit[eé] de refuge int[eé]rieur|PRI)\b"),
    TagRule("issue", "nexus", r"\b(?:Convention nexus|nexus to (?:a )?Convention ground|lien avec (?:un )?motif)\b"),
    TagRule("issue", "subjective_fear", r"\b(?:subjective fear|crainte subjective)\b"),
    TagRule("issue", "objective_basis", r"\b(?:objective basis|fondement objectif|well[- ]founded fear|crainte fond[eé]e)\b"),
    TagRule("issue", "sur_place_claim", r"\b(?:sur place claim|refugee sur place|r[eé]fugi[eé] sur place)\b"),
    TagRule("issue", "reavailment", r"\b(?:reavailment|se r[eé]clamer de nouveau de la protection|national passport)\b"),
    TagRule("issue", "cessation", r"\b(?:cessation of refugee protection|cessation application|perte de l['’]asile)\b"),
    TagRule("issue", "vacation", r"\b(?:vacate refugee protection|vacation application|annulation de la d[eé]cision)\b"),
    TagRule("issue", "exclusion_article_1e", r"\b(?:Article 1E|article 1E exclusion|rights and obligations of a national)\b"),
    TagRule("issue", "exclusion_article_1f", r"\b(?:Article 1F|article 1F exclusion|serious non[- ]political crime|crimes? against humanity|war crimes?)\b"),
    TagRule("issue", "exclusion_article_1fa", r"\b(?:Article 1F\s*\(a\)|1F\s*\(a\))(?=\W|$)"),
    TagRule("issue", "exclusion_article_1fb", r"\b(?:(?:Article )?1F\s*\(b\)(?=\W|$)|serious non[- ]political crime\b)"),
    TagRule("issue", "exclusion_article_1fc", r"\b(?:(?:Article )?1F\s*\(c\)(?=\W|$)|acts contrary to the purposes and principles of the United Nations\b)"),
    TagRule("issue", "serious_reasons_for_considering", r"\bserious reasons for consider(?:ing|ation)\b"),
    TagRule("issue", "complicity_significant_contribution", r"\b(?:voluntary,?\s+significant\s+and\s+knowing contribution|significant contribution test|complicity by association)\b"),
    TagRule("issue", "duress", r"\bduress\b"),
    TagRule("issue", "superior_orders", r"\b(?:superior orders?|orders? of (?:a |the )?military superior)\b"),
    TagRule("issue", "generalized_risk", r"\b(?:generalized risk|risk faced generally|risque g[eé]n[eé]ralis[eé])\b"),
    TagRule("issue", "individualized_risk_inquiry", r"\b(?:individualized inquiry|individualized risk (?:inquiry|assessment))\b"),
    TagRule("issue", "prospective_risk", r"\b(?:prospective|forward[- ]looking|ongoing future)\s+(?:personalized\s+)?risk\b"),
    TagRule("issue", "reason_for_targeting_vs_risk", r"\b(?:conflat\w+\s+the\s+reason for targeting with\s+the\s+risk|reason for targeting (?:versus|vs\.?|and) the risk)\b"),
    TagRule("issue", "lawful_sanctions_exception", r"\blawful sanctions exception\b"),
    TagRule("issue", "medical_exception", r"\b(?:medical exception|97\s*\(1\)\s*\(b\)\s*\(iv\))\b"),
    TagRule("issue", "non_refoulement", r"\b(?:non[- ]refoulement|refoulement)\b"),
    TagRule("issue", "best_interests_child", r"\b(?:best interests? of the child|BIOC|int[eé]r[eê]t sup[eé]rieur de l['’]enfant)\b"),
    TagRule("issue", "country_conditions", r"\b(?:country conditions?|country of origin information|COI|National Documentation Package|NDP)\b"),
    TagRule("issue", "procedural_accommodation", r"\bprocedural accommodations?\b"),
    TagRule("issue", "trauma_informed_adjudication", r"\btrauma[- ]informed adjudication\b"),
    TagRule("issue", "intersectionality", r"\bintersectional(?:ity| assessment)?\b"),
    TagRule("issue", "vulnerable_person", r"\bvulnerable persons?\b"),
    TagRule("issue", "sogiesc", r"\b(?:SOGIESC|sexual orientation,? gender identity and expression,? and sex characteristics)\b"),
    TagRule("guideline", "irb_chairperson_guideline_2", r"\b(?:IRB )?Chairperson['’]?s? Guideline 2\b"),
    TagRule("guideline", "irb_chairperson_guideline_3", r"\b(?:IRB )?Chairperson['’]?s? Guideline 3\b"),
    TagRule("guideline", "irb_chairperson_guideline_4", r"\b(?:IRB )?Chairperson['’]?s? Guideline 4\b"),
    TagRule("guideline", "irb_chairperson_guideline_8", r"\b(?:IRB )?Chairperson['’]?s? Guideline 8\b"),
    TagRule("guideline", "irb_chairperson_guideline_9", r"\b(?:IRB )?Chairperson['’]?s? Guideline 9\b"),

    # Convention grounds and risk types
    TagRule("convention_ground", "race", r"\b(?:race|racial|ethnic(?:ity)?)\b"),
    TagRule("convention_ground", "religion", r"\b(?:religion|religious faith|religious belief)\b"),
    TagRule("convention_ground", "nationality", r"\b(?:nationality|citizenship|stateless(?:ness)?)\b"),
    TagRule("convention_ground", "political_opinion", r"\b(?:political opinion|imputed political opinion)\b"),
    TagRule("convention_ground", "particular_social_group", r"\b(?:particular social group|PSG|groupe social)\b"),
    TagRule("risk", "persecution", r"\bpersecut(?:ion|ed|ory)\b"),
    TagRule("risk", "torture", r"\b(?:torture|CAT risk)\b"),
    TagRule("risk", "risk_to_life", r"\brisk to life\b"),
    TagRule("risk", "cruel_unusual_treatment", r"\bcruel and unusual treatment or punishment\b"),
    TagRule("risk", "gender_based_violence", r"\b(?:gender[- ]based violence|domestic violence|intimate partner violence|forced marriage|honou?r crime)\b"),
    TagRule("risk", "sexual_orientation_gender_identity", r"\b(?:sexual orientation|gender identity|gender expression|SOGIE|LGBTQ\w*)\b"),
    TagRule("risk", "female_genital_mutilation", r"\b(?:female genital mutilation|female genital cutting|FGM|FGC)\b"),
    TagRule("risk", "gang_cartel", r"\b(?:gang violence|criminal gang|drug cartel|organized crime)\b"),

    # Inadmissibility and CBSA enforcement program effects
    TagRule("inadmissibility", "security", r"\b(?:security inadmissibility|inadmissible (?:on|for) security grounds|espionage|subversion|terrorism)\b"),
    TagRule("inadmissibility", "human_rights_violations", r"\b(?:human or international rights violations|war crimes?|crimes? against humanity|genocide)\b"),
    TagRule("inadmissibility", "serious_criminality", r"\b(?:serious criminality|grande criminalit[eé])\b"),
    TagRule("inadmissibility", "criminality", r"\b(?:criminal inadmissibility|inadmissible (?:for|on grounds of) criminality)\b"),
    TagRule("inadmissibility", "organized_criminality", r"\b(?:organized criminality|organized crime inadmissibility)\b"),
    TagRule("inadmissibility", "misrepresentation", r"\b(?:misrepresentation|withholding material facts?|fausses? d[eé]clarations?)\b"),
    TagRule("inadmissibility", "non_compliance", r"\b(?:non[- ]compliance with (?:the )?Act|failure to comply with IRPA)\b"),
    TagRule("inadmissibility", "inadmissible_family_member", r"\b(?:inadmissible family member|family inadmissibility)\b"),
    TagRule("cbsa_program", "section_44_report", r"\b(?:section|subsection|s\.)\s*44\s*\(?1\)?\s*(?:report)?\b|\b44\(1\) report\b"),
    TagRule("cbsa_program", "removals", r"\b(?:removal(?:s)? program|enforce(?:d|able|ment of)? (?:a )?removal|scheduled removal|removal arrangements?)\b"),
    TagRule("cbsa_program", "detention", r"\b(?:immigration detention|detained under IRPA|continued detention)\b"),
    TagRule("cbsa_program", "alternatives_to_detention", r"\b(?:alternative(?:s)? to detention|ATD program|community case management)\b"),
    TagRule("cbsa_program", "border_examination", r"\b(?:port of entry examination|border examination|secondary examination)\b"),
    TagRule("cbsa_program", "investigation", r"\b(?:CBSA investigation|immigration investigation|enforcement investigation)\b"),
    TagRule("cbsa_program", "warrant", r"\b(?:immigration warrant|Canada-wide warrant|warrant for (?:their |his |her )?arrest)\b"),
    TagRule("detention_ground", "danger_to_public", r"\b(?:danger to the public|danger to society)\b"),
    TagRule("detention_ground", "flight_risk", r"\b(?:unlikely to appear|flight risk)\b"),
    TagRule("detention_ground", "identity", r"\b(?:unable to satisfy (?:an |the )?officer of (?:their |his |her )?identity|identity not established)\b"),
    TagRule("release_mechanism", "bondsperson", r"\bbondsperson\b"),
    TagRule("release_mechanism", "deposit", r"\brelease on (?:a )?deposit\b"),
    TagRule("release_mechanism", "reporting_conditions", r"\b(?:release on )?reporting conditions?\b"),
    TagRule("release_mechanism", "community_case_management", r"\bcommunity case management(?: and supervision)?\b"),
    TagRule("release_mechanism", "electronic_monitoring", r"\belectronic monitoring\b"),
    TagRule("enforcement_action", "departure_order", r"\bdeparture order\b"),
    TagRule("enforcement_action", "exclusion_order", r"\bexclusion order\b"),
    TagRule("enforcement_action", "deportation_order", r"\bdeportation order\b"),
    TagRule("enforcement_action", "removal_order", r"\bremoval order\b"),
    TagRule("enforcement_impediment", "judicial_stay", r"\b(?:stay of removal|motion to stay|interlocutory stay)\b"),
    TagRule("enforcement_impediment", "statutory_stay", r"\b(?:statutory stay|regulatory stay|stay under (?:the )?IRPR)\b"),
    TagRule("enforcement_impediment", "administrative_deferral", r"\b(?:administrative deferral of removal|ADR)\b"),
    TagRule("enforcement_impediment", "temporary_suspension_removals", r"\b(?:temporary suspension of removals?|TSR)\b"),
    TagRule("enforcement_impediment", "travel_documents", r"\b(?:travel document(?:s)?|identity document(?:s)?)\b"),
    TagRule("program_impact", "removal_delayed", r"\b(?:removal (?:is |was )?(?:delayed|deferred|postponed|stayed)|impediment to removal|stay(?:ed)?\b.{0,60}\b(?:removal|delaying enforcement))\b"),
    TagRule("program_impact", "removal_resumes", r"\b(?:removal may (?:now )?proceed|resume removals?|stay (?:is )?lifted)\b"),
    TagRule("program_impact", "redetermination_required", r"\b(?:remitted|sent back|returned)\b.{0,80}\b(?:redetermination|reconsideration)\b"),

    # Evidence, review, disposition, and remedies
    TagRule("evidence", "expert_evidence", r"\b(?:expert evidence|expert report|opinion evidence)\b"),
    TagRule("evidence", "documentary_evidence", r"\b(?:documentary evidence|objective evidence)\b"),
    TagRule("evidence", "medical_evidence", r"\b(?:medical evidence|medical report|psychological report|medical records?)\b|\bpreuve m[eé]dicale\b"),
    TagRule("evidence", "oral_testimony", r"\b(?:oral testimony|oral evidence|testimonial evidence|t[eé]moignage oral)\b"),
    TagRule("evidence", "corroboration", r"\b(?:corroborat(?:e|ed|ing|ion)|corroborative evidence|corroboration)\b"),
    TagRule("evidence", "identity_evidence", r"\b(?:identity evidence|proof of identity|preuve d['’]identit[eé])\b"),
    TagRule("evidence", "translation_interpretation", r"\b(?:translation|interpretation)\s+(?:of|services?|evidence|documents?)\b|\btraduction\b|\binterpr[eé]tation\b"),
    TagRule("document_type", "passport", r"\bpassports?\b|\bpasseports?\b"),
    TagRule("document_type", "visa", r"\bvisas?\b"),
    TagRule("document_type", "work_permit", r"\bwork permits?\b|\bpermis de travail\b"),
    TagRule("document_type", "study_permit", r"\bstudy permits?\b|\bpermis d['’]études?\b"),
    TagRule("document_type", "travel_document", r"\btravel documents?\b|\bdocuments? de voyage\b"),
    TagRule("document_type", "police_certificate", r"\b(?:police certificates?|police clearance certificates?|certificat de police)\b"),
    TagRule("document_type", "birth_certificate", r"\bbirth certificates?\b|\bcertificat[s]? de naissance\b"),
    TagRule("document_type", "medical_exam", r"\b(?:medical examination|immigration medical examination|examen m[eé]dical)\b"),
    TagRule("document_type", "national_identity_card", r"\b(?:national identity card|national identification card|carte nationale d['’]identit[eé])\b"),
    TagRule("document_type", "permanent_resident_card", r"\b(?:permanent resident card|PR card|carte de r[eé]sident permanent)\b"),
    TagRule("standard_of_review", "reasonableness", r"\b(?:unreasonable|reasonableness|raisonnabilit[eé])\b"),
    TagRule("standard_of_review", "correctness", r"\b(?:correctness standard|standard of correctness|norme de la d[eé]cision correcte)\b"),
    TagRule("standard_of_review", "palpable_overriding_error", r"\bpalpable and overriding error\b"),
    TagRule("outcome", "allowed", r"\b(?:application|appeal|demande|appel)\s+(?:is |est )?(?:allowed|granted|accueilli[e]?)\b"),
    TagRule("outcome", "dismissed", r"\b(?:application|appeal|demande|appel)\s+(?:is |est )?(?:dismissed|denied|rejet[eé][e]?)\b"),
    TagRule("outcome", "refused", r"\b(?:application|claim|request|demande|revendication)\s+(?:was |is |a été )?refused\b"),
    TagRule("outcome", "withdrawn", r"\b(?:application|appeal|claim|demande|appel|revendication)\s+(?:was |is |a été )?withdrawn\b"),
    TagRule("outcome", "remitted", r"\b(?:matter|application|decision|case)\s+(?:was |is )?(?:remitted|sent back)\b"),
    TagRule("outcome", "stayed", r"\b(?:proceedings?|application|removal)\s+(?:were |was |is )?stayed\b"),
    TagRule("procedural_issue", "delay", r"\b(?:undue delay|unreasonable delay|administrative delay|delai d[eé]raisonnable)\b"),
    TagRule("procedural_issue", "failure_to_consider", r"\b(?:failed to consider|failure to consider|did not consider|omission de tenir compte)\b"),
    TagRule("procedural_issue", "inadequate_reasons", r"\b(?:inadequate reasons?|insufficient reasons?|reasons were deficient|motifs insuffisants?)\b"),
    TagRule("procedural_issue", "jurisdictional_error", r"\b(?:jurisdictional error|exceeded its jurisdiction|exc[eé]d[eé] sa comp[eé]tence)\b"),
    TagRule("decision_maker_action", "ignored_evidence", r"\b(?:ignored the evidence|disregarded the evidence|overlooked the evidence|evidence was ignored)\b"),
    TagRule("decision_maker_action", "credibility_finding", r"\b(?:negative credibility finding|adverse credibility finding|credibility finding)\b"),
    TagRule("decision_maker_action", "interview_conduct", r"\b(?:interview conduct|conduct of the interview|officer['’]s questioning)\b"),
    TagRule("decision_maker_action", "fettered_discretion", r"\b(?:fettered (?:its|his|her) discretion|fettering(?: of)? discretion|discretion was fettered)\b"),
    TagRule("representation", "self_represented", r"\b(?:self[- ]represented|represented himself|represented herself|acting in person|sans avocat)\b"),
    TagRule("representation", "legal_counsel", r"\b(?:legal counsel|counsel for the applicant|counsel for the respondent|avocat de la partie)\b"),
    TagRule("representation", "legal_aid", r"\b(?:legal aid|aide juridique)\b"),
    TagRule("representation", "interpreter", r"\b(?:interpreter|interpretation was required|interpr[eé]te)\b"),
    TagRule("procedural_step", "oral_hearing", r"\b(?:oral hearing|hearing was held|audience orale)\b"),
    TagRule("procedural_step", "written_submissions", r"\b(?:written submissions?|written argument|observations [eé]crites?)\b"),
    TagRule("procedural_step", "cross_examination", r"\b(?:cross[- ]examination|cross[- ]examined|contre[- ]interrogatoire)\b"),
    TagRule("procedural_step", "disclosure", r"\b(?:disclosure obligations?|disclosure of documents?|documents? were disclosed|was disclosed|divulgation de documents?)\b"),
    TagRule("procedural_step", "affidavit", r"\b(?:affidavit|sworn statement|d[eé]claration sous serment)\b"),
    TagRule("evidence_issue", "inconsistent_testimony", r"\b(?:inconsistent testimony|inconsistencies in (?:the )?testimony|incoh[eé]rences? dans le t[eé]moignage)\b"),
    TagRule("evidence_issue", "implausibility", r"\b(?:implausible|implausibility|not plausible|invraisemblable)\b"),
    TagRule("evidence_issue", "lack_of_corroboration", r"\b(?:lack of corroboration|absence of corroboration|no corroborating evidence|absence de corroboration)\b"),
    TagRule("evidence_issue", "late_disclosure", r"\b(?:late disclosure|late[- ]disclosed evidence|belated disclosure|divulgation tardive)\b"),
    TagRule("remedy", "quashing", r"\b(?:quash(?:ed|ing)?|set aside|annul[eé][e]?)\b"),
    TagRule("remedy", "redetermination", r"\b(?:redetermination|reconsideration|nouvel examen)\b"),
    TagRule("remedy", "injunction", r"\b(?:injunction|injonction)\b"),
    TagRule("remedy", "declaration", r"\b(?:declaration of invalidity|declaratory relief)\b"),
    TagRule("remedy", "mandamus", r"\b(?:mandamus|order of mandamus|ordonnance de mandamus)\b"),
    TagRule("remedy", "costs", r"\b(?:with costs|costs were awarded|award of costs|costs payable|d[eé]pens)\b"),
    TagRule("immigration_program", "family_reunification", r"\b(?:family reunification|family class sponsorship|regroupement familial)\b"),
    TagRule("immigration_program", "economic_class", r"\b(?:economic class|economic immigration|immigration [eé]conomique)\b"),
    TagRule("immigration_program", "spousal_sponsorship", r"\b(?:spousal sponsorship|spouse or common-law partner sponsorship|parrainage d['’]un [eé]poux)\b"),
    TagRule("immigration_program", "parent_grandparent_sponsorship", r"\b(?:parent and grandparent program|parents and grandparents program|super visa)\b"),
    TagRule("immigration_program", "citizenship_application", r"\b(?:citizenship application|application for citizenship|demande de citoyennet[eé])\b"),

    # Domestic and international instruments
    TagRule("statute", "charter_s_7", r"\b(?:section|s\.)\s*7\b.{0,60}\bCharter\b|\bCharter\b.{0,60}\b(?:section|s\.)\s*7\b"),
    TagRule("statute", "charter_s_15", r"\b(?:section|s\.)\s*15\b.{0,60}\bCharter\b|\bCharter\b.{0,60}\b(?:section|s\.)\s*15\b"),
    TagRule("international_instrument", "refugee_convention", r"\b(?:1951 Refugee Convention|Convention Relating to the Status of Refugees|Refugee Convention)\b"),
    TagRule("international_instrument", "refugee_protocol", r"\b(?:1967 Protocol|Protocol Relating to the Status of Refugees)\b"),
    TagRule("international_instrument", "convention_against_torture", r"\b(?:Convention\s+against\s+Torture|UNCAT|CAT)\b"),
    TagRule("international_instrument", "iccpr", r"\b(?:International Covenant on Civil and Political Rights|ICCPR)\b"),
    TagRule("international_instrument", "crc", r"\b(?:Convention on the Rights of the Child|CRC)\b"),
    TagRule("international_instrument", "cedaw", r"\b(?:Convention on the Elimination of All Forms of Discrimination against Women|CEDAW)\b"),
    TagRule("international_instrument", "rome_statute", r"\bRome Statute\b"),
)


ORGANIZATIONS = {
    "bangladesh_nationalist_party": r"\b(?:Bangladesh Nationalist Party|BNP)\b",
    "awami_league": r"\b(?:Bangladesh Awami League|Awami League)\b",
    "ipob": r"\b(?:Indigenous People of Biafra|IPOB)\b",
    "ltte": r"\b(?:Liberation Tigers of Tamil Eelam|Tamil Tigers|LTTE)\b",
    "pkk": r"\b(?:Kurdistan Workers['’]? Party|PKK)\b",
    "farc": r"\b(?:Revolutionary Armed Forces of Colombia|FARC)\b",
    "hezbollah": r"\b(?:Hezbollah|Hizballah)\b",
    "hamas": r"\bHamas\b",
    "isis": r"\b(?:ISIS|ISIL|Daesh|Islamic State)\b",
    "taliban": r"\bTaliban\b",
    "al_shabaab": r"\b(?:Al[- ]Shabaab|al-Shabaab)\b",
    "boko_haram": r"\bBoko Haram\b",
    "muslim_brotherhood": r"\b(?:Muslim Brotherhood|Society of the Muslim Brothers)\b",
    "jvp": r"\b(?:Janatha Vimukthi Peramuna|JVP)\b",
    "baloch_liberation_army": r"\b(?:Balochistan Liberation Army|Baloch Liberation Army|BLA)\b",
}


COUNTRIES = {
    "afghanistan": r"\bAfghanistan\b",
    "bangladesh": r"\bBangladesh(?:i)?\b",
    "china": r"\b(?:China|Chinese)\b",
    "colombia": r"\bColombia(?:n)?\b",
    "democratic_republic_congo": r"\b(?:Democratic Republic of (?:the )?Congo|DRC)\b",
    "haiti": r"\bHaiti(?:an)?\b",
    "india": r"\bIndia(?:n)?\b",
    "iran": r"\bIran(?:ian)?\b",
    "iraq": r"\bIraq(?:i)?\b",
    "mexico": r"\bMexic(?:o|an)\b",
    "nigeria": r"\bNigeria(?:n)?\b",
    "pakistan": r"\bPakistan(?:i)?\b",
    "somalia": r"\bSomali(?:a|an)?\b",
    "sri_lanka": r"\bSri Lanka(?:n)?\b",
    "sudan": r"\bSudan(?:ese)?\b",
    "syria": r"\bSyria(?:n)?\b",
    "ukraine": r"\bUkrain(?:e|ian)\b",
    "venezuela": r"\bVenezuela(?:n)?\b",
    "ethiopia": r"\bEthiopia(?:n)?\b",
    "ghana": r"\bGhana(?:ian)?\b",
    "kenya": r"\bKenya(?:n)?\b",
    "uganda": r"\bUganda(?:n)?\b",
    "turkey": r"\b(?:Turkey|Turkish)\b",
    "philippines": r"\b(?:Philippines|Filipino|Filipina)\b",
    "jamaica": r"\bJamaica(?:n)?\b",
    "nepal": r"\bNepal(?:ese)?\b",
    "myanmar": r"\b(?:Myanmar|Burm(?:a|ese))\b",
    "russia": r"\bRussia(?:n)?\b",
}


class LegalTagger:
    def __init__(self) -> None:
        self._rules = tuple((rule, re.compile(rule.pattern, re.IGNORECASE | re.DOTALL)) for rule in RULES)
        self._organizations = tuple((value, re.compile(pattern, re.IGNORECASE)) for value, pattern in ORGANIZATIONS.items())
        self._countries = tuple((value, re.compile(pattern, re.IGNORECASE)) for value, pattern in COUNTRIES.items())

    def tag(self, text: str | None, language: str | None = None) -> list[LegalTag]:
        content = text or ""
        found: dict[tuple[str, str], LegalTag] = {}
        if language:
            self._add(found, LegalTag("language", language.lower(), 1.0, language, "metadata"))

        for rule, pattern in self._rules:
            match = pattern.search(content)
            if match:
                self._add(found, LegalTag(rule.category, rule.value, rule.score, match.group(0).strip()))

        for value, pattern in self._organizations:
            match = pattern.search(content)
            if match:
                self._add(found, LegalTag("organization", value, 1.0, match.group(0)))
        for value, pattern in self._countries:
            match = pattern.search(content)
            if match:
                self._add(found, LegalTag("country", value, 1.0, match.group(0)))

        self._extract_legislation(content, found)
        return sorted(found.values(), key=lambda tag: (tag.category, tag.value))

    def tag_occurrences(self, text: str | None) -> list[LegalTagOccurrence]:
        content = text or ""
        occurrences: list[LegalTagOccurrence] = []

        for rule, pattern in self._rules:
            for match in pattern.finditer(content):
                occurrences.append(
                    LegalTagOccurrence(
                        rule.category,
                        rule.value,
                         rule.score,
                        match.group(0).strip(),
                        match.start(),
                        match.end(),
                    )
                )

        for value, pattern in self._organizations:
            for match in pattern.finditer(content):
                occurrences.append(
                    LegalTagOccurrence(
                        "organization",
                        value,
                        1.0,
                        match.group(0),
                        match.start(),
                        match.end(),
                    )
                )
        for value, pattern in self._countries:
            for match in pattern.finditer(content):
                occurrences.append(
                    LegalTagOccurrence(
                        "country",
                        value,
                        1.0,
                        match.group(0),
                        match.start(),
                        match.end(),
                    )
                )

        return sorted(occurrences, key=lambda occurrence: (occurrence.offset_start, occurrence.offset_end, occurrence.category, occurrence.value))

    @staticmethod
    def _add(found: dict[tuple[str, str], LegalTag], tag: LegalTag) -> None:
        key = (tag.category, tag.value)
        if key not in found or found[key].score < tag.score:
            found[key] = tag

    def _extract_legislation(self, text: str, found: dict[tuple[str, str], LegalTag]) -> None:
        irpa_context = re.search(r"\b(?:IRPA|Immigration and Refugee Protection Act)\b", text, re.IGNORECASE)
        if irpa_context:
            self._add(found, LegalTag("statute", "irpa", 1.0, irpa_context.group(0)))
            for match in re.finditer(r"\b(?:sections?|subsections?|paragraphs?|ss?\.)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)", text, re.IGNORECASE):
                section = re.sub(r"\s+", "", match.group(1))
                self._add(found, LegalTag("statute", f"irpa_s_{section}", 0.95, match.group(0)))
            for citation in re.finditer(
                r"\b(?:sections?|subsections?|paragraphs?|ss?\.)\s*([\dA-Za-z(),.\s-]+(?:and|or|et|ou)[\dA-Za-z(),.\s-]+)",
                text,
                re.IGNORECASE,
            ):
                for section in re.finditer(r"\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*", citation.group(1)):
                    evidence = citation.group(0).strip()
                    section_value = re.sub(r"\s+", "", section.group(0))
                    self._add(found, LegalTag("statute", f"irpa_s_{section_value}", 0.95, evidence))

        irpr_context = re.search(r"\b(?:IRPR|Immigration and Refugee Protection Regulations?)\b", text, re.IGNORECASE)
        if irpr_context:
            self._add(found, LegalTag("regulation", "irpr", 1.0, irpr_context.group(0)))
            for match in re.finditer(r"\b(?:regulations?|sections?|subsections?|paragraphs?|ss?\.)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)", text, re.IGNORECASE):
                section = re.sub(r"\s+", "", match.group(1))
                self._add(found, LegalTag("regulation", f"irpr_s_{section}", 0.95, match.group(0)))
