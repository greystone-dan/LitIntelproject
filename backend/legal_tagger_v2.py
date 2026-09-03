"""High-precision whitelist tagging for the independent Tagging V2 layer."""

from __future__ import annotations

import re
import json
from dataclasses import dataclass
from pathlib import Path


TAXONOMY_VERSION = "ca_legal_v2_core"


@dataclass(frozen=True)
class CoreTag:
    category: str
    value: str
    score: float
    evidence: str
    offset_start: int | None = None
    offset_end: int | None = None
    source: str = "core_whitelist"
    taxonomy_version: str = TAXONOMY_VERSION


def _pattern(*terms: str) -> str:
    return r"(?<!\w)(?:" + "|".join(re.escape(term) for term in terms) + r")(?!\w)"


# Keep this list deliberately small. Additions require a canonical value, aliases,
# and a focused regression test before they are promoted into the core layer.
DEFAULT_CORE_TERMS = {
    "agency": {
        "ircc": ("IRCC", "Immigration, Refugees and Citizenship Canada", "Citizenship and Immigration Canada"),
        "cbsa": ("CBSA", "Canada Border Services Agency"),
    },
    "tribunal": {
        "rpd": ("RPD", "Refugee Protection Division"),
        "rad": ("RAD", "Refugee Appeal Division"),
        "id": ("Immigration Division",),
        "iad": ("IAD", "Immigration Appeal Division"),
    },
    "statute": {
        "irpa": ("IRPA", "Immigration and Refugee Protection Act"),
    },
    "regulation": {
        "irpr": ("IRPR", "Immigration and Refugee Protection Regulations"),
    },
    "immigration_term": {
        "prra": ("PRRA", "Pre-Removal Risk Assessment"),
        "h_and_c": ("H&C", "Humanitarian and Compassionate"),
        "ifa": ("IFA", "Internal Flight Alternative"),
        "s_44_report": ("section 44 report", "subsection 44(1) report"),
    },
    "organization": {
        "ipob": ("IPOB", "Indigenous People of Biafra"),
        "ltte": ("LTTE", "Liberation Tigers of Tamil Eelam", "Tamil Tigers"),
        "pkk": ("PKK", "Kurdistan Workers' Party", "Kurdistan Workers’ Party"),
        "farc": ("FARC", "Revolutionary Armed Forces of Colombia"),
        "taliban": ("Taliban",),
        "hamas": ("Hamas",),
        "hezbollah": ("Hezbollah", "Hizballah"),
        "isis": ("ISIS", "ISIL", "Daesh", "Islamic State"),
    },
    "country": {
        "afghanistan": ("Afghanistan",),
        "bangladesh": ("Bangladesh",),
        "china": ("China",),
        "colombia": ("Colombia",),
        "democratic_republic_congo": ("Democratic Republic of the Congo", "DRC"),
        "ethiopia": ("Ethiopia",),
        "ghana": ("Ghana",),
        "haiti": ("Haiti",),
        "india": ("India",),
        "iran": ("Iran",),
        "iraq": ("Iraq",),
        "jamaica": ("Jamaica",),
        "kenya": ("Kenya",),
        "mexico": ("Mexico",),
        "nigeria": ("Nigeria",),
        "pakistan": ("Pakistan",),
        "philippines": ("Philippines",),
        "russia": ("Russia",),
        "somalia": ("Somalia",),
        "sri_lanka": ("Sri Lanka",),
        "sudan": ("Sudan",),
        "syria": ("Syria",),
        "turkey": ("Turkey",),
        "uganda": ("Uganda",),
        "ukraine": ("Ukraine",),
        "venezuela": ("Venezuela",),
    },
}


def load_core_terms() -> dict[str, dict[str, tuple[str, ...]]]:
    whitelist_path = Path(__file__).resolve().parents[1] / "config" / "tagging_v2_core_whitelist.json"
    candidate_path = Path(__file__).resolve().parents[1] / "data" / "eval" / "reports" / "tagging-v2-core-candidates.json"
    try:
        payload = json.loads(whitelist_path.read_text(encoding="utf-8"))
        if payload.get("taxonomy_version") != TAXONOMY_VERSION:
            raise ValueError("whitelist taxonomy version does not match Tagging V2")
        terms = {
            category: {value: tuple(aliases) for value, aliases in values.items()}
            for category, values in payload["categories"].items()
        }
        # Countries and organizations are reviewed entity inventories promoted into V2.
        candidates = json.loads(candidate_path.read_text(encoding="utf-8"))
        for category in ("country", "organization"):
            terms.setdefault(category, {}).update(
                {value: tuple(aliases) for value, aliases in candidates["categories"].get(category, {}).items()}
            )
        return terms
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return DEFAULT_CORE_TERMS


CORE_TERMS = load_core_terms()


class CoreLegalTagger:
    def __init__(self) -> None:
        self._entries = tuple(
            (category, value, re.compile(_pattern(*aliases), re.IGNORECASE))
            for category, values in CORE_TERMS.items()
            for value, aliases in values.items()
        )

    def tag(self, text: str | None) -> list[CoreTag]:
        content = text or ""
        found: dict[tuple[str, str], CoreTag] = {}
        for category, value, pattern in self._entries:
            match = pattern.search(content)
            if match:
                found[(category, value)] = CoreTag(category, value, 1.0, match.group(0))
        return sorted(found.values(), key=lambda tag: (tag.category, tag.value))

    def tag_occurrences(self, text: str | None) -> list[CoreTag]:
        content = text or ""
        occurrences: list[CoreTag] = []
        for category, value, pattern in self._entries:
            for match in pattern.finditer(content):
                occurrences.append(CoreTag(category, value, 1.0, match.group(0), match.start(), match.end()))
        return sorted(occurrences, key=lambda tag: (tag.offset_start or 0, tag.offset_end or 0, tag.category, tag.value))