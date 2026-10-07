"""Map the act name in a stored statute reference to a registered instrument key, deterministically.

Most unkeyed statute_references rows name an act the registry already knows ("Immigration and Refugee
Protection Act, S.C. 2001, c. 27", "Patent Act", "Federal Court Rules", "NOC Regulations"), because they were
stored before the registry grew. This resolves those names without re-reading any decision. It uses only
exact normalized names, never a fuzzy match, and leaves a row alone when the name is generic ("the Act"),
could be a provincial act ("Motor Vehicle Act") or is a repealed act we do not hold.
"""

from __future__ import annotations

import re
from functools import lru_cache

from backend.statutes import LEGISLATION_REGISTRY

FEDERAL_COURTS = frozenset({"FC", "FCA", "FCT"})
FEDERAL_AND_SCC = FEDERAL_COURTS | {"SCC"}

# alias (normalized) -> instrument key. Always safe in any court.
_ALIASES: dict[str, str] = {
    "irpa": "canada.irpa",
    "immigration and refugee protection act": "canada.irpa",
    "irpa regulations": "canada.irpr",
    "irp regulations": "canada.irpr",
    "immigration and refugee protection regulations": "canada.irpr",
    "federal court act": "canada.federal_courts_act",
    "federal courts act": "canada.federal_courts_act",
    "fc act": "canada.federal_courts_act",
    "federal court rules": "canada.federal_courts_rules",
    "federal courts rules": "canada.federal_courts_rules",
    "fc rules": "canada.federal_courts_rules",
    "federal courts immigration and refugee protection rules": "canada.fc_cirp_rules",
    "federal courts citizenship, immigration and refugee protection rules": "canada.fc_cirp_rules",
    "federal courts citizenship immigration and refugee protection rules": "canada.fc_cirp_rules",
    "income tax act": "canada.income_tax_act",
    "income tax regulations": "canada.income_tax_regulations",
    "immigration act": "canada.immigration_act",
    "customs act": "canada.customs_act",
    "citizenship act": "canada.citizenship_act",
    "citizenship regulations": "canada.citizenship_regulations",
    "patent act": "canada.patent_act",
    "copyright act": "canada.copyright_act",
    "noc regulations": "canada.noc_regulations",
    "pmnoc regulations": "canada.noc_regulations",
    "pm noc regulations": "canada.noc_regulations",
    "trade-marks act": "canada.trademarks_act",
    "trademarks act": "canada.trademarks_act",
    "trade marks act": "canada.trademarks_act",
    "tm act": "canada.trademarks_act",
    "competition act": "canada.competition_act",
    "canadian human rights act": "canada.human_rights_act",
    "canada evidence act": "canada.evidence_act",
    "canada labour code": "canada.labour_code",
    "csis act": "canada.csis_act",
    "canadian security intelligence service act": "canada.csis_act",
    "fisheries act": "canada.fisheries_act",
    "excise tax act": "canada.excise_tax_act",
    "gst act": "canada.excise_tax_act",
    "excise act": "canada.excise_act",
    "employment insurance act": "canada.employment_insurance_act",
    "ei act": "canada.employment_insurance_act",
    "employment insurance regulations": "canada.ei_regulations",
    "divorce act": "canada.divorce_act",
    "national defence act": "canada.national_defence_act",
    "food and drugs act": "canada.food_and_drugs_act",
    "food and drug regulations": "canada.food_and_drug_regulations",
    "financial administration act": "canada.financial_administration_act",
    "judges act": "canada.judges_act",
    "rcmp act": "canada.rcmp_act",
    "royal canadian mounted police act": "canada.rcmp_act",
    "extradition act": "canada.extradition_act",
    "public service employment act": "canada.public_service_employment_act",
    "corrections and conditional release act": "canada.corrections_conditional_release_act",
    "corrections and conditional release regulations": "canada.ccr_regulations",
    "crown liability and proceedings act": "canada.crown_liability_proceedings_act",
    "crown liability act": "canada.crown_liability_proceedings_act",
    "bankruptcy and insolvency act": "canada.bankruptcy_insolvency_act",
    "bankruptcy act": "canada.bankruptcy_insolvency_act",
    "controlled drugs and substances act": "canada.controlled_drugs_substances_act",
    "canada transportation act": "canada.transportation_act",
    "telecommunications act": "canada.telecommunications_act",
    "canada marine act": "canada.marine_act",
    "marine liability act": "canada.marine_liability_act",
    "canada elections act": "canada.elections_act",
    "firearms act": "canada.firearms_act",
    "youth criminal justice act": "canada.youth_criminal_justice_act",
    "criminal records act": "canada.criminal_records_act",
    "statutory instruments act": "canada.statutory_instruments_act",
    "tax court of canada act": "canada.tax_court_act",
    "tax court of canada rules": "canada.tax_court_rules_general",
    "tax court of canada rules (general procedure)": "canada.tax_court_rules_general",
    "canada business corporations act": "canada.cbca",
    "health of animals act": "canada.health_of_animals_act",
    "old age security act": "canada.oas_act",
    "oas act": "canada.oas_act",
    "rpd rules": "canada.rpd_rules",
    "refugee protection division rules": "canada.rpd_rules",
    "rad rules": "canada.rad_rules",
    "refugee appeal division rules": "canada.rad_rules",
    "id rules": "canada.id_rules",
    "iad rules": "canada.iad_rules",
    "immigration appeal division rules": "canada.iad_rules",
    "immigration division rules": "canada.id_rules",
    "citt act": "canada.citt_act",
    "canadian international trade tribunal act": "canada.citt_act",
    "special import measures act": "canada.sima",
    "special economic measures act": "canada.sema",
    "terrorist financing act": "canada.pcmltfa",
    "proceeds of crime (money laundering) and terrorist financing act": "canada.pcmltfa",
    "public service labour relations act": "canada.fpslra",
    "federal public sector labour relations act": "canada.fpslra",
    "canada pension plan": "canada.cpp",
    "canadian bill of rights": "canada.bill_of_rights",
    "personal information protection and electronic documents act": "canada.pipeda",
    "piped act": "canada.pipeda",
    "department of citizenship and immigration act": "canada.department_cic_act",
    "government employees compensation act": "canada.gec_act",
    "security of information act": "canada.security_of_information_act",
    "access to information act": "canada.access_to_information_act",
    "refugee convention": "international.refugee_convention",
    "convention relating to the status of refugees": "international.refugee_convention",
}

# Names shared with provincial acts: federal only when the case is in a federal court (or the Supreme Court
# for names that are federal there), and only when the text carries no provincial hint.
_FEDERAL_COURT_ONLY: dict[str, str] = {
    "privacy act": "canada.privacy_act",
    "interpretation act": "canada.interpretation_act",
    "labour code": "canada.labour_code",
    "official languages act": "canada.official_languages_act",
    "information act": "canada.access_to_information_act",
    "access act": "canada.access_to_information_act",
    "human rights act": "canada.human_rights_act",
    "evidence act": "canada.evidence_act",
}
_FEDERAL_COURT_AND_SCC: dict[str, str] = {
    "supreme court act": "canada.supreme_court_act",
}

_PROVINCIAL_HINT_RE = re.compile(
    r"\b(?:ontario|quebec|québec|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|"
    r"newfoundland|prince edward island|yukon|northwest territories|nunavut|r\.?s\.?o\.|s\.?o\.|r\.?s\.?b\.?c\.|"
    r"s\.?b\.?c\.|r\.?s\.?a\.|s\.?a\.|c\.?c\.?s\.?m\.|r\.?s\.?q\.|s\.?q\.|r\.?s\.?n\.?s\.|s\.?s\.|r\.?s\.?n\.?b\.)\b",
    re.IGNORECASE,
)
_TRAILING_PINPOINT_RE = re.compile(
    r"\s+(?:s|ss|sec|secs|section|sections|subsection|subsections|para|paras|paragraph|paragraphs|r|rr|rule|rules|art|"
    r"article|articles|regs?|reg\.)\.?\s*[0-9].*$",
    re.IGNORECASE,
)
_CITATION_TAIL_RE = re.compile(
    r",?\s*(?:\(?\s*(?:r\.?\s?)?s\.?\s?c\.?\s?\d{4}|\(?\s*r\.?\s?s\.?\s?c\.?\s?\d{4}|\(?\s*c\.?\s?r\.?\s?c\.?\b|"
    r"\(?\s*s\.?\s?o\.?\s?\d{4}|\(?\s*r\.?\s?s\.?\s?o\.?\s?\d{4}|\(?\s*sor\s*/|\(?\s*si\s*/|\(?\s*r\.?\s?s\.?\s?b\.?\s?c\.?).*$",
    re.IGNORECASE,
)
_PAREN_RE = re.compile(r"\s*\((?:the\s+)?[\"“”']?(?:act|irpa|code|regulations?|rules?)[\"“”']?\)\s*$", re.IGNORECASE)
_LEAD_RE = re.compile(
    r"^(?:statutes? and regulations? cited|relevant legislation|legislation|in the|under the|re|the|see)\s+",
    re.IGNORECASE,
)
_OLD_CONSOLIDATION_RE = re.compile(r"\br\.?\s?s\.?\s?c\.?\s?(?:19[0-7]\d|198[0-4])\b", re.IGNORECASE)


@lru_cache(maxsize=1)
def _registry_aliases() -> dict[str, str]:
    table: dict[str, str] = {}
    for key, definition in LEGISLATION_REGISTRY.items():
        for alias in definition["aliases"]:  # type: ignore[union-attr]
            if _CITATION_TAIL_RE.search(str(alias)):
                continue  # a citation-only alias (shared name) must not become a plain-name alias
            table.setdefault(normalize_act_name(str(alias)), key)
    return table


def normalize_act_name(value: str) -> str:
    """Lowercase, strip the pinpoint, the citation and 'the Act' parentheticals, and leading filler."""
    text = re.sub(r"\s+", " ", (value or "").replace("’", "'").replace("“", '"').replace("”", '"')).strip()
    text = _TRAILING_PINPOINT_RE.sub("", text)
    text = _CITATION_TAIL_RE.sub("", text)
    for _ in range(3):
        text = _PAREN_RE.sub("", text)
        text = _LEAD_RE.sub("", text)
    return text.strip(" ,.;:-").lower()


def resolve_instrument_key(reference: str | None, court: str | None = None) -> str | None:
    """Return the instrument key for a reference's act name, or None when it cannot be named exactly."""
    raw = reference or ""
    name = normalize_act_name(raw)
    if not name:
        return None
    key = _ALIASES.get(name) or _registry_aliases().get(name)
    if key is not None:
        # An older consolidation (R.S.C. 1952, 1970) is a different text with different section numbers; the
        # Criminal Code keeps its existing treatment.
        if _OLD_CONSOLIDATION_RE.search(raw) and key != "canada.criminal_code":
            return None
        return key
    if _PROVINCIAL_HINT_RE.search(raw):
        return None
    court_code = (court or "").upper()
    if name in _FEDERAL_COURT_ONLY and court_code in FEDERAL_COURTS:
        return _FEDERAL_COURT_ONLY[name]
    if name in _FEDERAL_COURT_AND_SCC and court_code in FEDERAL_AND_SCC:
        return _FEDERAL_COURT_AND_SCC[name]
    return None
