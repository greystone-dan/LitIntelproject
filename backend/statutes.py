"""Canonical statute identity and lightweight citation parsing."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class LegislationCitation:
    instrument_key: str
    pinpoint: str
    legislation_url: str | None = None


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
            r"\b(?:s|ss|sections?|paragraphs?|subsections?)\.?\s*(?=\d)([^,;]+?)(?=\s+of\s+|\s*$|[.;])",
            text,
            re.IGNORECASE,
        )
        if match is None:
            match = re.search(r"\bsections?\s*([^,;]+)", text, re.IGNORECASE)
        if match is None:
            source_url = definition.get("source_url")
            return LegislationCitation(key, "", source_url if isinstance(source_url, str) else None)
        pinpoint = re.sub(r"\s+", "", match.group(1)).strip(".")
        section = re.match(r"\d{1,3}(?:\.\d+)?[A-Za-z]?", pinpoint)
        url_template = definition.get("url")
        url = url_template.format(section=section.group(0)) if section and isinstance(url_template, str) else None
        return LegislationCitation(key, pinpoint, url)
    return None
