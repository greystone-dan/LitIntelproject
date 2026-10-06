"""Canonical statute identity and lightweight citation parsing."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class LegislationCitation:
    instrument_key: str
    pinpoint: str
    legislation_url: str | None = None
    section: str | None = None
    subsection: str | None = None
    paragraph: str | None = None
    nested_depth: int | None = None
    is_range_or_list: bool = False


def normalize_provision_pinpoint(pinpoint: str | None) -> str:
    value = re.sub(r"\s+", "", pinpoint or "").strip(".")
    if not value:
        return ""
    value = re.sub(r"\(([A-Za-z0-9]+)\)", lambda match: f"({match.group(1).lower()})", value)
    value = re.sub(r"(?<=\d)([A-Z])(?=(?:\(|$))", lambda match: match.group(1).lower(), value)
    return value


_PROVISION_ITEM = r"\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*"
_PROVISION_SEP = r"(?:\s*,\s*(?:and|or)?\s*|\s+(?:and|or|to)\s+|\s*[-\u2013]\s*)"
_PROVISION_LIST = _PROVISION_ITEM + r"(?:" + _PROVISION_SEP + _PROVISION_ITEM + r")*"


def expand_pinpoint_list(pinpoint: str | None) -> list[str]:
    """Split a list or range pinpoint ("34,35,37", "96-97", "96 to 98") into single provisions.

    Ranges expand only between plain whole-number sections (capped at 60); anything else is kept as written.
    """
    text = re.sub(r"\s+", " ", pinpoint or "").strip(" .,")
    if not text:
        return []
    parts = [part for part in re.split(r"\s*,\s*(?:and\s+|or\s+)?|\s+(?:and|or)\s+", text) if part]
    expanded: list[str] = []
    for part in parts:
        range_match = re.fullmatch(r"(\d{1,3})\s*(?:-|\u2013|to)\s*(\d{1,3})", part.strip(), re.IGNORECASE)
        if range_match and 0 <= int(range_match.group(2)) - int(range_match.group(1)) <= 60:
            expanded.extend(str(number) for number in range(int(range_match.group(1)), int(range_match.group(2)) + 1))
        else:
            expanded.append(normalize_provision_pinpoint(part))
    return expanded


def parse_provision_identity(pinpoint: str | None) -> tuple[str | None, str | None, str | None, int | None, bool]:
    raw_value = re.sub(r"\s+", " ", pinpoint or "").strip(".")
    value = re.sub(r"\s+", "", pinpoint or "").strip(".")
    if not value:
        return None, None, None, None, False
    match = re.match(r"(?P<section>\d{1,3}(?:\.\d+)?(?:[A-Za-z](?![A-Za-z]))?)(?P<tail>(?:\([^()]+\))*)", value)
    if match is None:
        return None, None, None, None, True
    groups = re.findall(r"\(([^()]+)\)", match.group("tail"))
    is_range_or_list = bool(re.search(r"(?:,|\band\b|\bto\b|[-–])", raw_value, re.IGNORECASE))
    section = match.group("section")
    if section and section[-1].isalpha():
        section = section[:-1] + section[-1].lower()
    return (
        section,
        groups[0].lower() if groups else None,
        groups[1].lower() if len(groups) > 1 else None,
        len(groups) if groups else 0,
        is_range_or_list,
    )


LEGISLATION_REGISTRY: dict[str, dict[str, object]] = {
    "canada.irpa": {
        "aliases": ("IRPA", "Immigration and Refugee Protection Act"),
        "citation": "Immigration and Refugee Protection Act, S.C. 2001, c. 27",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/I-2.5/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/I-2.5/section-{section}.html",
    },
    "canada.irpr": {
        "aliases": ("IRPR", "Immigration and Refugee Protection Regulations"),
        "citation": "Immigration and Refugee Protection Regulations, SOR/2002-227",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/section-{section}.html",
    },
    "canada.criminal_code": {
        "aliases": ("Criminal Code", "Criminal Code of Canada"),
        "citation": "Criminal Code, R.S.C. 1985, c. C-46",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-46/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-46/section-{section}.html",
    },
    "canada.charter": {
        "aliases": ("Charter", "Canadian Charter of Rights and Freedoms"),
        "citation": "Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982",
        "url": None,
    },
    "canada.immigration_act": {
        "aliases": ("Immigration Act",),
        "citation": "Immigration Act, R.S.C. 1985, c. I-2",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/I-2/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/I-2/section-{section}.html",
    },
    "canada.citizenship_act": {
        "aliases": ("Citizenship Act",),
        "citation": "Citizenship Act, R.S.C. 1985, c. C-29",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-29/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-29/section-{section}.html",
    },
    "canada.federal_courts_act": {
        "aliases": ("Federal Courts Act", "Federal Court Act"),
        "citation": "Federal Courts Act, R.S.C. 1985, c. F-7",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/F-7/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/F-7/section-{section}.html",
    },
    "canada.federal_courts_rules": {
        "aliases": ("Federal Courts Rules",),
        "citation": "Federal Courts Rules, SOR/98-106",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/section-{section}.html",
    },
    "canada.income_tax_act": {
        "aliases": ("Income Tax Act",),
        "citation": "Income Tax Act, R.S.C. 1985, c. 1 (5th Supp.)",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-{section}.html",
    },
    "canada.marine_liability_act": {
        "aliases": ("Marine Liability Act",),
        "citation": "Marine Liability Act, S.C. 2001, c. 6",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/M-0.7/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/M-0.7/section-{section}.html",
    },
    "canada.commercial_arbitration_act": {
        "aliases": ("Commercial Arbitration Act",),
        "citation": "Commercial Arbitration Act, R.S.C. 1985, c. C-34.6",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-34.6/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-34.6/section-{section}.html",
    },
    "canada.coastal_fisheries_protection_act": {
        "aliases": ("Coastal Fisheries Protection Act",),
        "citation": "Coastal Fisheries Protection Act, R.S.C. 1985, c. C-33",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-33/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-33/section-{section}.html",
    },
    "canada.customs_act": {
        "aliases": ("Customs Act",),
        "citation": "Customs Act, R.S.C. 1985, c. 1 (2nd Supp.)",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-52.6/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-52.6/section-{section}.html",
    },
    "canada.cbsa_act": {
        "aliases": ("Canada Border Services Agency Act", "CBSA Act"),
        "citation": "Canada Border Services Agency Act, S.C. 2005, c. 38",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-1.4/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-1.4/section-{section}.html",
    },
    "canada.customs_tariff": {
        "aliases": ("Customs Tariff",),
        "citation": "Customs Tariff, S.C. 1997, c. 36",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/C-54.011/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/C-54.011/section-{section}.html",
    },
    "canada.excise_tax_act": {
        "aliases": ("Excise Tax Act",),
        "citation": "Excise Tax Act, R.S.C. 1985, c. E-15",
        "source_url": "https://laws-lois.justice.gc.ca/eng/acts/E-15/",
        "url": "https://laws-lois.justice.gc.ca/eng/acts/E-15/section-{section}.html",
    },
    "canada.fc_cirp_rules": {
        "aliases": (
            "Federal Courts Citizenship, Immigration and Refugee Protection Rules",
            "Federal Court Citizenship, Immigration and Refugee Protection Rules",
        ),
        "citation": "Federal Courts Citizenship, Immigration and Refugee Protection Rules, SOR/93-22",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-93-22/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-93-22/section-{section}.html",
    },
    "canada.rpd_rules": {
        "aliases": ("Refugee Protection Division Rules", "RPD Rules"),
        "citation": "Refugee Protection Division Rules, SOR/2012-256",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2012-256/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2012-256/section-{section}.html",
    },
    "canada.rad_rules": {
        "aliases": ("Refugee Appeal Division Rules", "RAD Rules"),
        "citation": "Refugee Appeal Division Rules, SOR/2012-257",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2012-257/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2012-257/section-{section}.html",
    },
    "canada.id_rules": {
        "aliases": ("Immigration Division Rules", "ID Rules"),
        "citation": "Immigration Division Rules, SOR/2002-229",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-229/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-229/section-{section}.html",
    },
    "canada.iad_rules": {
        "aliases": ("Immigration Appeal Division Rules", "IAD Rules"),
        "citation": "Immigration Appeal Division Rules, 2022, SOR/2022-277",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2022-277/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2022-277/section-{section}.html",
    },
    "canada.citizenship_regulations": {
        "aliases": ("Citizenship Regulations",),
        "citation": "Citizenship Regulations, SOR/93-246",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-93-246/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-93-246/section-{section}.html",
    },
    "international.refugee_convention": {
        "aliases": ("Refugee Convention", "Convention Relating to the Status of Refugees"),
        "citation": "Convention Relating to the Status of Refugees",
        "source_url": "https://www.unhcr.org/media/1951-refugee-convention-relating-status-refugees-and-1967-protocol-relating-status-refugees",
        "url": None,
    },
}


# Further federal instruments whose text is in the library (scripts/index_legislation.py). Aliases are the
# plain federal titles; where provincial acts share the title (Privacy Act, Interpretation Act, Supreme Court Act)
# only the full federal citation counts. "Excise Act, 2001" comes before "Excise Act" because the first alias hit wins.
_MORE_FEDERAL_INSTRUMENTS = (
    ("canada.patent_act", ("Patent Act",), "Patent Act, R.S.C. 1985, c. P-4", "acts/P-4"),
    ("canada.competition_act", ("Competition Act",), "Competition Act, R.S.C. 1985, c. C-34", "acts/C-34"),
    ("canada.bankruptcy_insolvency_act", ("Bankruptcy and Insolvency Act",), "Bankruptcy and Insolvency Act, R.S.C. 1985, c. B-3", "acts/B-3"),
    ("canada.food_and_drugs_act", ("Food and Drugs Act", "Food and Drug Act"), "Food and Drugs Act, R.S.C. 1985, c. F-27", "acts/F-27"),
    ("canada.controlled_drugs_substances_act", ("Controlled Drugs and Substances Act", "CDSA"), "Controlled Drugs and Substances Act, S.C. 1996, c. 19", "acts/C-38.8"),
    ("canada.evidence_act", ("Canada Evidence Act",), "Canada Evidence Act, R.S.C. 1985, c. C-5", "acts/C-5"),
    ("canada.access_to_information_act", ("Access to Information Act",), "Access to Information Act, R.S.C. 1985, c. A-1", "acts/A-1"),
    ("canada.fisheries_act", ("Fisheries Act",), "Fisheries Act, R.S.C. 1985, c. F-14", "acts/F-14"),
    ("canada.labour_code", ("Canada Labour Code",), "Canada Labour Code, R.S.C. 1985, c. L-2", "acts/L-2"),
    ("canada.criminal_records_act", ("Criminal Records Act",), "Criminal Records Act, R.S.C. 1985, c. C-47", "acts/C-47"),
    ("canada.csis_act", ("Canadian Security Intelligence Service Act", "CSIS Act"), "Canadian Security Intelligence Service Act, R.S.C. 1985, c. C-23", "acts/C-23"),
    ("canada.extradition_act", ("Extradition Act",), "Extradition Act, S.C. 1999, c. 18", "acts/E-23.01"),
    ("canada.security_of_information_act", ("Security of Information Act",), "Security of Information Act, R.S.C. 1985, c. O-5", "acts/O-5"),
    ("canada.marine_act", ("Canada Marine Act",), "Canada Marine Act, S.C. 1998, c. 10", "acts/C-6.7"),
    ("canada.employment_insurance_act", ("Employment Insurance Act",), "Employment Insurance Act, S.C. 1996, c. 23", "acts/E-5.6"),
    ("canada.railway_safety_act", ("Railway Safety Act",), "Railway Safety Act, R.S.C. 1985, c. 32 (4th Supp.)", "acts/R-4.2"),
    ("canada.crown_liability_proceedings_act", ("Crown Liability and Proceedings Act",), "Crown Liability and Proceedings Act, R.S.C. 1985, c. C-50", "acts/C-50"),
    ("canada.shipping_act_2001", ("Canada Shipping Act, 2001", "Canada Shipping Act 2001"), "Canada Shipping Act, 2001, S.C. 2001, c. 26", "acts/C-10.15"),
    ("canada.fpslra", ("Federal Public Sector Labour Relations Act", "Public Service Labour Relations Act"), "Federal Public Sector Labour Relations Act, S.C. 2003, c. 22, s. 2", "acts/P-33.3"),
    ("canada.pcmltfa", ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", "PCMLTFA"), "Proceeds of Crime (Money Laundering) and Terrorist Financing Act, S.C. 2000, c. 17", "acts/P-24.501"),
    ("canada.corrections_conditional_release_act", ("Corrections and Conditional Release Act", "CCRA"), "Corrections and Conditional Release Act, S.C. 1992, c. 20", "acts/C-44.6"),
    ("canada.youth_criminal_justice_act", ("Youth Criminal Justice Act", "YCJA"), "Youth Criminal Justice Act, S.C. 2002, c. 1", "acts/Y-1.5"),
    ("canada.indian_act", ("Indian Act",), "Indian Act, R.S.C. 1985, c. I-5", "acts/I-5"),
    ("canada.human_rights_act", ("Canadian Human Rights Act",), "Canadian Human Rights Act, R.S.C. 1985, c. H-6", "acts/H-6"),
    ("canada.excise_act_2001", ("Excise Act, 2001", "Excise Act 2001"), "Excise Act, 2001, S.C. 2002, c. 22", "acts/E-14.1"),
    ("canada.excise_act", ("Excise Act",), "Excise Act, R.S.C. 1985, c. E-14", "acts/E-14"),
    ("canada.privacy_act", ("Privacy Act, R.S.C. 1985, c. P-21",), "Privacy Act, R.S.C. 1985, c. P-21", "acts/P-21"),
    ("canada.interpretation_act", ("Interpretation Act, R.S.C. 1985, c. I-21",), "Interpretation Act, R.S.C. 1985, c. I-21", "acts/I-21"),
    ("canada.supreme_court_act", ("Supreme Court Act, R.S.C. 1985, c. S-26",), "Supreme Court Act, R.S.C. 1985, c. S-26", "acts/S-26"),
    ("canada.noc_regulations", ("Patented Medicines (Notice of Compliance) Regulations", "NOC Regulations", "PM(NOC) Regulations"), "Patented Medicines (Notice of Compliance) Regulations, SOR/93-133", "regulations/SOR-93-133"),
    ("canada.food_and_drug_regulations", ("Food and Drug Regulations",), "Food and Drug Regulations, C.R.C., c. 870", "regulations/C.R.C.,_c._870"),
)
for _key, _aliases, _citation, _path in _MORE_FEDERAL_INSTRUMENTS:
    LEGISLATION_REGISTRY.setdefault(
        _key,
        {
            "aliases": _aliases,
            "citation": _citation,
            "source_url": f"https://laws-lois.justice.gc.ca/eng/{_path}/",
            "url": f"https://laws-lois.justice.gc.ca/eng/{_path}/section-{{section}}.html",
        },
    )


def canonical_citation_name(name: str) -> str:
    """Return the canonical citation prefix for a registered instrument."""
    normalized = re.sub(r"\s+", " ", name).strip().casefold()
    for definition in LEGISLATION_REGISTRY.values():
        aliases = definition["aliases"]
        if any(normalized == alias.casefold() for alias in aliases):
            citation = definition.get("citation")
            if isinstance(citation, str):
                return citation
    return re.sub(r"\s+", " ", name).strip()


def parse_legislation_citation(value: str | None) -> LegislationCitation | None:
    """Parse an explicit instrument and provision without claiming legal resolution."""
    text = re.sub(r"\s+", " ", value or "").strip()
    for key, definition in LEGISLATION_REGISTRY.items():
        aliases = definition["aliases"]
        if not any(re.search(rf"\b{re.escape(alias)}\b", text, re.IGNORECASE) for alias in aliases):
            continue
        match = re.search(
            r"\b(?:ss?|sections?|paragraphs?|paras?|subsections?|subsecs?)\.?\s*(?=\d)(" + _PROVISION_LIST + r")",
            text,
            re.IGNORECASE,
        ) or re.search(
            r"\b(?:s|ss|sections?|paragraphs?|subsections?)\.?\s*(?=\d)([^,;]+?)(?=\s+of\s+|\s*$|[.;])",
            text,
            re.IGNORECASE,
        )
        if match is None:
            match = re.search(r"\bsections?\s*([^,;]+)", text, re.IGNORECASE)
        if match is None:
            source_url = definition.get("source_url")
            return LegislationCitation(key, "", source_url if isinstance(source_url, str) else None)
        pinpoint = normalize_provision_pinpoint(match.group(1))
        provision_section, subsection, paragraph, nested_depth, is_range_or_list = parse_provision_identity(match.group(1))
        section_match = re.match(r"\d{1,3}(?:\.\d+)?[A-Za-z]?", pinpoint)
        url_template = definition.get("url")
        url = url_template.format(section=section_match.group(0)) if section_match and isinstance(url_template, str) else None
        return LegislationCitation(
            key,
            pinpoint,
            url,
            section=provision_section,
            subsection=subsection,
            paragraph=paragraph,
            nested_depth=nested_depth,
            is_range_or_list=is_range_or_list,
        )
    return None
