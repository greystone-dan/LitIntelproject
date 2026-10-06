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
    match = re.match(r"(?P<section>\d{1,3}(?:\.\d+)?[A-Za-z]?)(?P<tail>(?:\([^()]+\))*)", value)
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
    "canada.fc_citizenship_immigration_rules": {
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
        "citation": "Immigration Appeal Division Rules, SOR/2002-230",
        "source_url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-230/",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-230/section-{section}.html",
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
