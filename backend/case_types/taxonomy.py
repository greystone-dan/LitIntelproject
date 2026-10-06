"""Case-type taxonomy for Canadian immigration and refugee decisions.

Each type is defined only by deterministic evidence: the provisions a decision
discusses and a short list of plain-language cues. No model of any kind is used.

A provision rule is ``(instrument_key, first_section, last_section, subsection)``.
Sections are compared numerically (``25.1`` sorts between ``25`` and ``26``), and
``subsection`` (for example ``"(1)"``) narrows the rule when it is not ``None``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

TAXONOMY_VERSION = "case_types_v1"

IRPA = "canada.irpa"
IRPR = "canada.irpr"
CITACT = "canada.citizenship_act"
CONVENTION = "international.refugee_convention"
CONV_1A = CONVENTION + ":1A"
CONV_1C = CONVENTION + ":1C"
CONV_1E = CONVENTION + ":1E"
CONV_1F = CONVENTION + ":1F"
FC_RULES = "canada.fc_cirp_rules"
RPD_RULES = "canada.rpd_rules"
RAD_RULES = "canada.rad_rules"

ProvisionRule = tuple[str, float, float, str | None]


def rule(instrument: str, first: float, last: float | None = None, subsection: str | None = None) -> ProvisionRule:
    return (instrument, float(first), float(first if last is None else last), subsection)


@dataclass(frozen=True)
class CaseType:
    key: str
    label: str
    group: str
    provisions: tuple[ProvisionRule, ...] = ()
    # Cues are matched case-insensitively. A cue in the opening of the decision (where the
    # court states what the case is about) counts for more than one in the body.
    cues: tuple[str, ...] = ()
    # "general" types lose to a specific type that is also present (a cessation case is
    # decided under ss. 96-97 vocabulary but is a cessation case).
    general: bool = False
    description: str = ""
    compiled_cues: tuple[re.Pattern[str], ...] = field(default=(), compare=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "compiled_cues", tuple(re.compile(cue, re.IGNORECASE) for cue in self.cues)
        )


def _t(key: str, label: str, group: str, provisions=(), cues=(), general=False, description="") -> CaseType:
    return CaseType(key, label, group, tuple(provisions), tuple(cues), general, description)


# Order matters only for display; scoring is independent of order.
CASE_TYPES: tuple[CaseType, ...] = (
    # ---- Refugee protection ------------------------------------------------------------
    _t("refugee_claim", "Refugee / protection claim (ss. 96-97)", "Refugee protection",
       [rule(IRPA, 96, 97), rule(CONV_1A, 0, 99), rule(CONVENTION, 0, 99)],
       [r"convention refugee", r"persons? in need of protection", r"refugee claims?", r"claims? for refugee protection",
        r"Refugee Protection Division", r"Refugee Appeal Division", r"\bRPD\b", r"\bRAD\b", r"\bCRDD\b", r"Convention Refugee Determination Division",
        r"well[- ]founded fear", r"state protection", r"internal flight alternative", r"\bIFA\b",
        r"crédibilité", r"personne à protéger", r"réfugié au sens de la Convention"],
       general=True,
       description="Review or appeal of a decision on whether the person is a Convention refugee or person in need of protection."),
    _t("refugee_cessation", "Refugee cessation (s. 108)", "Refugee protection",
       [rule(IRPA, 108), rule(CONV_1C, 0, 99)],
       [r"cessation", r"ceased to be a (?:convention )?refugee", r"reavail", r"re-avail",
        r"voluntarily re-?established", r"article 1C\b", r"\bArt(?:icle|\.)? 1\(?C\)?", r"perte de l['’]asile",
        r"cessation d['’]asile", r"cesse d['’]être un réfugié"],
       description="The Minister applies to find that protected-person status has ended (reavailment, passport renewal, return to the country, change of circumstances)."),
    _t("refugee_exclusion", "Refugee exclusion (s. 98, Art. 1E/1F)", "Refugee protection",
       [rule(IRPA, 98), rule(CONV_1E, 0, 99), rule(CONV_1F, 0, 99)],
       [r"exclusion clause", r"\bexcluded from (?:refugee )?protection", r"article 1F\b", r"\bArt(?:icle|\.)? 1\(?F\)?",
        r"article 1E\b", r"\bArt(?:icle|\.)? 1\(?E\)?", r"serious reasons for considering", r"complicity", r"crimes? against humanity",
        r"serious non-?political crime", r"exclusion de la protection", r"article 1F\b"],
       description="Claimant is excluded from refugee protection under Article 1E or 1F of the Convention (incorporated by s. 98)."),
    _t("refugee_vacation", "Vacation of refugee status (s. 109)", "Refugee protection",
       [rule(IRPA, 109)],
       [r"\bvacat(?:e|ed|ion|ing)\b", r"application to vacate", r"annulation de la décision", r"annulation de l['’]asile"],
       description="The Minister applies to vacate a prior positive refugee determination obtained through misrepresentation."),
    _t("pre_removal_risk_assessment", "Pre-removal risk assessment (ss. 112-116)", "Refugee protection",
       [rule(IRPA, 112, 116), rule(IRPR, 160, 176)],
       [r"\bPRRA\b", r"pre-removal risk assessment", r"examen des risques avant renvoi", r"\bERAR\b"],
       description="Review of a PRRA officer's decision on risk upon removal, or of a related stay."),
    _t("refugee_eligibility_safe_third", "Refugee eligibility / Safe Third Country (ss. 101-102)", "Refugee protection",
       [rule(IRPA, 101, 102), rule(IRPR, 159.1, 159.7)],
       [r"safe third country", r"\bSTCA\b", r"ineligible to (?:make|have) (?:a )?(?:refugee )?claim", r"ineligib",
        r"tiers pays sûr", r"inadmissible à (?:faire|présenter)"],
       description="Whether a refugee claim may be made or referred at all (Safe Third Country Agreement and other eligibility bars)."),
    _t("refugee_sponsorship_resettlement", "Refugee resettlement / sponsorship (ss. 139-147)", "Refugee protection",
       [rule(IRPA, 139, 147), rule(IRPR, 138, 158)],
       [r"convention refugees? abroad", r"country of asylum class", r"private sponsorship of refugees", r"sponsorship agreement holder",
        r"groups? of five", r"\bSAH\b", r"réfugiés? à l['’]étranger"],
       description="Overseas refugee resettlement and private sponsorship of refugees."),
    # ---- Inadmissibility -----------------------------------------------------------------
    _t("inadmissibility_security", "Inadmissibility - security (s. 34)", "Inadmissibility",
       [rule(IRPA, 34)],
       [r"inadmissible on security grounds", r"danger to the security of Canada", r"membership in an organization",
        r"engag(?:e|ing) in terrorism", r"espionage", r"subversion", r"interdit de territoire pour raison[s]? de sécurité"],
       description="Inadmissibility on security grounds (espionage, subversion, terrorism, membership in a listed kind of organization)."),
    _t("inadmissibility_human_rights", "Inadmissibility - human or international rights violations (s. 35)", "Inadmissibility",
       [rule(IRPA, 35)],
       [r"violating human or international rights", r"crimes against humanity", r"senior official", r"Crimes Against Humanity and War Crimes Act",
        r"atteinte[s]? aux droits humains"],
       description="Inadmissibility for human or international rights violations (including senior-official provisions)."),
    _t("inadmissibility_serious_criminality", "Inadmissibility - serious criminality (s. 36(1))", "Inadmissibility",
       [rule(IRPA, 36, 36, "(1)")],
       [r"serious criminality", r"grande criminalité", r"punishable by a maximum term of imprisonment of at least 10 years"],
       description="Inadmissibility for serious criminality (conviction in Canada or equivalent offence abroad)."),
    _t("inadmissibility_criminality", "Inadmissibility - criminality (s. 36(2)-(3))", "Inadmissibility",
       [rule(IRPA, 36, 36, "(2)"), rule(IRPA, 36, 36, "(3)")],
       [r"inadmissible for criminality", r"\bcriminalité\b", r"deemed rehabilitation", r"criminal rehabilitation",
        r"equivalent offence", r"hybrid offence"],
       description="Inadmissibility for (non-serious) criminality, rehabilitation and equivalency questions."),
    _t("inadmissibility_organized_crime", "Inadmissibility - organized criminality (s. 37)", "Inadmissibility",
       [rule(IRPA, 37)],
       [r"organized criminality", r"criminal organization", r"people smuggling", r"human trafficking", r"money laundering",
        r"criminalité organisée"],
       description="Inadmissibility for membership in a criminal organization, smuggling, trafficking or laundering."),
    _t("inadmissibility_health", "Inadmissibility - health (s. 38)", "Inadmissibility",
       [rule(IRPA, 38)],
       [r"excessive demand", r"medical inadmissib", r"health grounds", r"medical officer", r"demande excessive",
        r"fardeau excessif"],
       description="Medical inadmissibility, mostly excessive demand on health or social services."),
    _t("inadmissibility_financial", "Inadmissibility - financial reasons (s. 39)", "Inadmissibility",
       [rule(IRPA, 39)],
       [r"financial reasons", r"unable or unwilling to support", r"raisons financières"],
       description="Inadmissibility for financial reasons (unable or unwilling to support self or dependants)."),
    _t("inadmissibility_misrepresentation", "Inadmissibility - misrepresentation (s. 40)", "Inadmissibility",
       [rule(IRPA, 40)],
       [r"misrepresentation", r"material fact", r"false (?:document|information|statement)s?", r"five-year (?:period of )?inadmissib",
        r"fausses déclarations", r"présentation erronée des faits", r"fraud"],
       description="Inadmissibility for misrepresentation or withholding a material fact, and the five-year bar."),
    _t("inadmissibility_noncompliance", "Inadmissibility - non-compliance with the Act (s. 41)", "Inadmissibility",
       [rule(IRPA, 41)],
       [r"non-?compliance with (?:the )?Act", r"failed to (?:comply|leave)", r"failure to comply with (?:the )?Act", r"résidence"],
       description="Inadmissibility for failing to comply with the Act or Regulations (for example residency obligation breaches)."),
    _t("inadmissibility_family_member", "Inadmissibility - inadmissible family member (s. 42)", "Inadmissibility",
       [rule(IRPA, 42)],
       [r"inadmissible family member", r"accompanying family member", r"non-accompanying family member", r"membre de la famille"],
       description="A person is inadmissible only because an accompanying or non-accompanying family member is."),
    # ---- Removal, enforcement, detention ------------------------------------------------
    _t("removal_admissibility_proceedings", "Removal order / admissibility proceedings (ss. 44-52)", "Enforcement",
       [rule(IRPA, 44, 47), rule(IRPA, 49, 53), rule(IRPR, 223, 229)],
       [r"admissibility hearing", r"section 44\(1\) report", r"\bs\.? ?44\(1\)", r"report under (?:subsection )?44", r"removal order",
        r"deportation order", r"exclusion order", r"departure order", r"minister['’]s delegate", r"mesure de renvoi",
        r"rapport (?:établi|prévu) (?:en vertu|au) (?:du )?paragraphe 44", r"enforcement officer"],
       description="Section 44 reports, admissibility hearings and the issuing or validity of removal orders."),
    _t("removal_deferral_stay", "Removal enforcement, deferral and stay of removal (s. 48, IRPR 231)", "Enforcement",
       [rule(IRPA, 48), rule(IRPR, 230, 233)],
       [r"stay of (?:the |his |her |their )?removal", r"defer(?:ral)?\b[^.]{0,50}\bremoval", r"refus\w+ to defer", r"deferral request", r"\bToth\b",
        r"irreparable harm", r"as soon as (?:is )?reasonably practicable", r"sursis (?:à|de) (?:l['’]exécution de la )?mesure de renvoi",
        r"report du renvoi"],
       description="Motions to stay removal pending judicial review, and judicial review of refusals to defer removal."),
    _t("detention", "Detention (ss. 54-60)", "Enforcement",
       [rule(IRPA, 54, 60), rule(IRPR, 244, 250)],
       [r"detention reviews?", r"continued detention", r"release from detention", r"detention order",
        r"alternatives? to detention", r"mise en détention", r"contrôle des motifs de la détention"],
       description="Detention and release of foreign nationals and permanent residents, and detention reviews."),
    # ---- Humanitarian and status ---------------------------------------------------------
    _t("humanitarian_compassionate", "Humanitarian and compassionate relief (s. 25)", "Humanitarian and status",
       [rule(IRPA, 25, 25.2)],
       [r"humanitarian and compassionate", r"\bH&C\b", r"\bH ?& ?C\b", r"best interests of the child", r"unusual and undeserved",
        r"disproportionate hardship", r"Kanthasamy", r"considérations d['’]ordre humanitaire", r"intérêt supérieur de l['’]enfant"],
       description="Application for an exemption on humanitarian and compassionate grounds."),
    _t("temporary_resident_permit", "Temporary resident permit (s. 24)", "Humanitarian and status",
       [rule(IRPA, 24)],
       [r"temporary resident permit", r"\bTRP\b", r"permis de séjour temporaire"],
       description="Temporary resident permits for otherwise inadmissible foreign nationals."),
    _t("permanent_resident_status", "Permanent resident status and residency obligation (ss. 27-31)", "Humanitarian and status",
       [rule(IRPA, 27, 31), rule(IRPR, 61, 63)],
       [r"residency obligation", r"loss of permanent resident status", r"permanent resident card", r"obligation de résidence",
        r"cessation of (?:permanent )?residen", r"travel document"],
       description="Residency obligation, loss of permanent resident status, PR cards and travel documents."),
    _t("protected_person_permanent_residence", "Permanent residence for protected persons (s. 21(2))", "Humanitarian and status",
       [rule(IRPA, 21, 21, "(2)"), rule(IRPR, 175, 176)],
       [r"permanent residence as a protected person", r"permanent residen\w+ (?:application )?(?:of|for) (?:a )?protected persons?",
        r"protected person[s]? (?:application|class)", r"identity documents?", r"résidence permanente (?:à titre de|en tant que) personne protégée"],
       description="Applications for permanent residence by people already found to be Convention refugees or protected persons (identity and admissibility)."),
    # ---- Family and economic selection ---------------------------------------------------
    _t("family_class_sponsorship", "Family class sponsorship (s. 12(1), IRPR 116-137)", "Immigration programs",
       [rule(IRPA, 12, None, "(1)"), rule(IRPR, 1, 5), rule(IRPR, 116, 137)],
       [r"family class", r"sponsorship application", r"spousal sponsorship", r"spouse or common-law", r"genuine marriage",
        r"bad faith", r"conjugal partner", r"parent and grandparent", r"\bPGP\b", r"parrainage", r"regroupement familial",
        r"dependent child", r"adoption"],
       description="Sponsorship of spouses, partners, children and parents; genuineness of relationships."),
    _t("economic_immigration", "Economic immigration (skilled worker, CEC, PNP, Express Entry)", "Immigration programs",
       [rule(IRPA, 12, None, "(2)"), rule(IRPR, 70, 87.4), rule(IRPR, 88, 109)],
       [r"federal skilled worker", r"Canadian Experience Class", r"express entry", r"provincial nominee", r"\bFSW\b", r"\bCEC\b",
        r"\bPNP\b", r"start-?up visa", r"self-employed", r"investor", r"entrepreneur", r"comprehensive ranking system",
        r"travailleurs qualifiés", r"catégorie de l['’]expérience canadienne", r"entrée express", r"nominee program", r"Ministerial Instructions", r"minister[’']s instructions"],
       description="Selection of skilled workers, Canadian Experience Class, provincial nominees, business and other economic applicants."),
    _t("caregiver_programs", "Caregiver programs", "Immigration programs",
       [rule(IRPR, 111, 115)],
       [r"live-in caregiver", r"home child care provider", r"home support worker", r"caregiver", r"aide familial"],
       description="Live-in Caregiver Program and the home child care / home support worker pilots."),
    # ---- Temporary residents -------------------------------------------------------------
    _t("work_permit", "Work permit (IRPR 196-209)", "Temporary residents",
       [rule(IRPR, 196, 209.99)],
       [r"work permit", r"labour market impact assessment", r"\bLMIA\b", r"post-graduation work permit", r"\bPGWP\b",
        r"permis de travail", r"closed work permit", r"open work permit", r"temporary foreign worker"],
       description="Applications for work permits, including LMIA-based and open work permits."),
    _t("study_permit", "Study permit (IRPR 210-222)", "Temporary residents",
       [rule(IRPR, 210, 222.99)],
       [r"study permit", r"permis d['’]études", r"designated learning institution", r"letter of acceptance", r"student visa"],
       description="Applications for study permits and related student matters."),
    _t("visitor_visa", "Visitor / temporary resident visa (s. 11, IRPR 179)", "Temporary residents",
       [rule(IRPA, 11), rule(IRPA, 20, 22), rule(IRPR, 179, 195)],
       [r"visitor visa", r"temporary resident visa", r"\bTRV\b", r"visa de résident temporaire", r"super visa",
        r"leave Canada at the end of (?:the )?authorized period", r"intends? to leave canada", r"purpose of (?:her|his|their) visit"],
       description="Refusal of a visitor or temporary resident visa for failing to satisfy the officer the applicant will leave Canada."),
    # ---- Citizenship ----------------------------------------------------------------------
    _t("citizenship_grant", "Citizenship - grant (Citizenship Act s. 5)", "Citizenship",
       [rule(CITACT, 5), rule(CITACT, 14)],
       [r"citizenship judge", r"citizenship application", r"physical presence", r"residence requirement",
        r"juge de la citoyenneté", r"1,?095 days", r"Pourghasemi", r"Koo \(Re\)"],
       description="Applications for a grant of citizenship; residence questions."),
    _t("citizenship_revocation", "Citizenship - revocation (Citizenship Act ss. 10, 10.1)", "Citizenship",
       [rule(CITACT, 10, 10.99)],
       [r"revocation of citizenship", r"citizenship (?:was )?obtained by", r"false representation or fraud", r"révocation de la citoyenneté"],
       description="Revocation of citizenship for fraud or false representation."),
    _t("citizenship_other", "Citizenship - other (proof, prohibitions, loss, lost Canadians)", "Citizenship",
       [rule(CITACT, 3), rule(CITACT, 22), rule(CITACT, 7, 9), rule(CITACT, 11, 13)],
       [r"revok\w+ (?:\w+ )?citizenship", r"proof of citizenship", r"citizenship certificate", r"\blost canadians?\b", r"second-generation cut-?off",
        r"preuve de citoyenneté", r"prohibition", r"renunciation"],
       description="Proof of citizenship, citizenship by descent, prohibitions and renunciation."),
    # ---- Court procedure -------------------------------------------------------------------
    _t("court_procedure_only", "Procedural matter (extension, costs, contempt, leave)", "Court procedure",
       [rule("canada.federal_courts_rules", 1, 500), rule(FC_RULES, 1, 22)],
       [r"extension of time", r"motion for (?:an )?extension", r"\bcosts\b", r"contempt", r"respondent['’]s? motion to strike",
        r"motion to strike", r"intervener", r"prolongation de délai"],
       general=True,
       description="Decisions whose subject is procedural (extensions, costs, motions to strike) rather than the immigration question."),
)

TYPES_BY_KEY: dict[str, CaseType] = {case_type.key: case_type for case_type in CASE_TYPES}

# Types that, when strongly present, make the general "refugee_claim" label a secondary one.
SPECIFIC_PROTECTION_TYPES = frozenset(
    {
        "refugee_cessation",
        "refugee_exclusion",
        "refugee_vacation",
        "pre_removal_risk_assessment",
        "refugee_eligibility_safe_third",
        "refugee_sponsorship_resettlement",
    }
)

# Instruments whose citations count as "this is an immigration or citizenship decision".
IMMIGRATION_INSTRUMENTS = frozenset({IRPA, IRPR, CITACT, RPD_RULES, RAD_RULES, FC_RULES, "canada.id_rules", "canada.iad_rules", "canada.iad_rules_2022"})

# What is being reviewed fixes the subject matter: a judicial review of an RPD or RAD decision is about
# refugee protection whatever visa, permit or family facts the claimant's story mentions.
REFUGEE_GROUP = "Refugee protection"
ALLOWED_GROUPS_BY_PROCEEDING: dict[str, frozenset[str]] = {
    "jr_refugee_protection_division": frozenset({REFUGEE_GROUP, "Court procedure"}),
    "jr_refugee_appeal_division": frozenset({REFUGEE_GROUP, "Court procedure"}),
    "tribunal_decision_rpd": frozenset({REFUGEE_GROUP}),
    "tribunal_decision_rad": frozenset({REFUGEE_GROUP}),
    "jr_prra_officer": frozenset({REFUGEE_GROUP, "Court procedure"}),
}
