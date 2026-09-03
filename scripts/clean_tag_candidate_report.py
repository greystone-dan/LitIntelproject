"""Create a conservative, review-ready list from a tag candidate report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.legal_tagger import COUNTRIES, ORGANIZATIONS, RULES
import pycountry


MONTHS = {
    "april", "august", "december", "february", "january", "july", "june",
    "march", "may", "november", "october", "september",
}
GENERIC_TERMS = {
    "a", "act", "action", "appeal", "application", "argument", "case", "claim",
    "canada", "court", "decision", "evidence", "found", "government", "hearing",
    "immigration", "issue", "judicial", "law", "matter", "minister", "motion",
    "party", "person", "proceeding", "refugee", "review", "rule", "section",
    "subsection", "tribunal", "v",
}
GENERIC_ORGANIZATION_TERMS = {
    "association", "army", "church", "committee", "council", "force", "government",
    "group", "organization", "organisation", "party", "union",
}
ORGANIZATION_SIGNAL_TERMS = {
    "army", "brigade", "cartel", "front", "forces", "force", "liberation", "militia",
    "movement", "party", "rebels", "resistance", "tigers", "union", "wing",
}
DOMESTIC_ORGANIZATION_TERMS = {
    "alberta", "canada", "canadian", "federal", "labrador", "ontario", "quebec",
    "toronto", "vancouver", "government", "nurses", "teachers",
}
GENERIC_COUNTRY_TERMS = MONTHS | {
    "appeal", "citizenship", "claim", "employment", "imm", "irpa", "review", "rule",
    "vavilov",
}
GENERIC_EDGE_TERMS = {
    "applicant", "applicants", "board", "canada", "case", "court", "decision",
    "found", "her", "his", "maker", "matter", "officer", "party", "person",
    "proceeding", "their", "this", "tribunal", "v",
}
EXCLUDED_ORGANIZATION_PHRASES = {
    "third party", "independent third party", "moving party", "regular force", "reserve force",
}
EXCLUDED_PROPOSAL_CATEGORIES = {
    "authority", "agency", "case_history", "convention_ground",
}
SUPPLEMENTAL_COUNTRIES = {
    "kosovo", "palestine", "state of palestine", "taiwan", "western sahara",
    "somaliland", "transnistria", "northern cyprus", "east timor", "burma",
}
WORD_RE = re.compile(r"[a-z][a-z'’-]*")


def normalize(value: str) -> str:
    value = " ".join(value.lower().replace("’", "'").split()).strip(" ,.;:()[]")
    return re.sub(r"\b([a-z]+)'s\b", r"\1", value)


def meaningful_words(value: str) -> list[str]:
    return WORD_RE.findall(normalize(value))


def is_generic_phrase(value: str) -> bool:
    if not re.fullmatch(r"[a-z][a-z' -]*", normalize(value)):
        return True
    words = meaningful_words(value)
    if not words or len(normalize(value)) < 5 or any(word in MONTHS for word in words):
        return True
    if words[0] in GENERIC_EDGE_TERMS or words[-1] in GENERIC_EDGE_TERMS:
        return True
    if "minister" in words and ("canada" in words or "citizenship" in words):
        return True
    if "canada" in words and "v" in words:
        return True
    if len(words) == 1 and words[0] in GENERIC_TERMS:
        return True
    return sum(word in GENERIC_TERMS for word in words) >= max(1, len(words) // 2)


def useful_candidates(items: list[dict], existing: set[str], minimum: int, maximum: int | None = None) -> list[dict]:
    candidates = []
    for item in items:
        term = normalize(str(item.get("term", "")))
        words = meaningful_words(term)
        if int(item.get("occurrences", 0)) < minimum or is_generic_phrase(term):
            continue
        if term in existing or not words:
            continue
        candidates.append({"term": term, "occurrences": int(item["occurrences"]), "samples": item.get("samples", [])})

    candidates.sort(key=lambda item: (item["occurrences"], len(item["term"])), reverse=True)
    kept: list[dict] = []
    for candidate in candidates:
        candidate_words = set(meaningful_words(candidate["term"]))
        if any(candidate_words < set(meaningful_words(item["term"])) for item in kept):
            continue
        kept.append(candidate)
    return kept[:maximum] if maximum else kept


def organization_candidates(items: list[dict], minimum: int) -> list[dict]:
    by_term: dict[str, dict] = {}
    for item in items:
        term = normalize(str(item.get("term", "")))
        words = meaningful_words(term)
        if int(item.get("occurrences", 0)) < minimum or len(words) < 2:
            continue
        if term in EXCLUDED_ORGANIZATION_PHRASES:
            continue
        if not re.fullmatch(r"[a-z][a-z' -]*", term) or any(word in MONTHS for word in words):
            continue
        if any(word in DOMESTIC_ORGANIZATION_TERMS for word in words):
            continue
        if not any(word in ORGANIZATION_SIGNAL_TERMS for word in words):
            continue
        if all(word in GENERIC_ORGANIZATION_TERMS or word in GENERIC_EDGE_TERMS for word in words):
            continue
        candidate = {"term": term, "occurrences": int(item["occurrences"]), "samples": item.get("samples", [])}
        current = by_term.get(term)
        if current is None or candidate["occurrences"] > current["occurrences"]:
            by_term[term] = candidate
    candidates = list(by_term.values())
    candidates.sort(key=lambda item: (item["occurrences"], len(item["term"])), reverse=True)
    kept: list[dict] = []
    for candidate in candidates:
        candidate_words = set(meaningful_words(candidate["term"]))
        if any(candidate_words < set(meaningful_words(item["term"])) for item in kept):
            continue
        kept.append(candidate)
    return kept[:200]


def country_names() -> set[str]:
    names = {normalize(country.name) for country in pycountry.countries}
    names.update(SUPPLEMENTAL_COUNTRIES)
    names.update({"democratic republic of the congo", "dr congo", "south korea", "north korea"})
    return names


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/eval/reports/tag-candidate-review.json"))
    parser.add_argument("--output", type=Path, default=Path("data/eval/reports/tag-candidate-proposals.json"))
    parser.add_argument("--minimum-occurrences", type=int, default=25)
    parser.add_argument("--maximum-per-category", type=int, default=20)
    args = parser.parse_args()

    report = json.loads(args.input.read_text(encoding="utf-8"))
    existing = {normalize(rule.value) for rule in RULES}
    existing.update(normalize(value) for value in COUNTRIES)
    existing.update(normalize(value) for value in ORGANIZATIONS)

    categories = {}
    for category, data in report["categories"].items():
        if category in EXCLUDED_PROPOSAL_CATEGORIES:
            continue
        candidates = useful_candidates(
            data["candidate_phrases"], existing, args.minimum_occurrences, args.maximum_per_category
        )
        if candidates:
            categories[category] = candidates

    organizations = organization_candidates(report["candidate_organizations"], args.minimum_occurrences)
    known_organizations = sorted(ORGANIZATIONS)
    manual_organization_review = [
        {"term": "people's liberation army (pla)", "reason": "manual inadmissibility-group review candidate"},
    ]
    whitelist = country_names()
    countries = [
        item for item in useful_candidates(report["candidate_countries"], set(), args.minimum_occurrences, 250)
        if normalize(item["term"]) in whitelist
        and not any(word in GENERIC_COUNTRY_TERMS for word in meaningful_words(item["term"]))
    ]
    cleaned = {
        "source_report": str(args.input),
        "scanned_cases": report["scanned_cases"],
        "minimum_occurrences": args.minimum_occurrences,
        "maximum_per_category": args.maximum_per_category,
        "excluded_proposal_categories": sorted(EXCLUDED_PROPOSAL_CATEGORIES),
        "country_source": "pycountry ISO 3166 names plus explicit disputed/non-sovereign supplements",
        "categories": categories,
        "candidate_organizations": organizations,
        "known_inadmissibility_organizations": known_organizations,
        "manual_organization_review": manual_organization_review,
        "candidate_countries": countries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(cleaned, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown = [
        "# Proposed Tag Candidates",
        "",
        f"Source scan: {cleaned['scanned_cases']} cases. Minimum occurrences: {args.minimum_occurrences}.",
        "These are review candidates only; they have not been added to the taxonomy.",
        "Authority, agency, case-history, and convention-ground mining are excluded because their candidates are too noisy; existing canonical tags remain available where tested.",
        "",
    ]
    for category, items in categories.items():
        markdown.extend([f"## {category}", ""])
        markdown.extend(f"- `{item['term']}` ({item['occurrences']})" for item in items)
        markdown.append("")
    markdown.extend(["## Organizations", ""])
    markdown.extend(f"- `{item['term']}` ({item['occurrences']})" for item in organizations)
    markdown.extend(["", "## Existing Inadmissibility Organizations", ""])
    markdown.extend(f"- `{term}`" for term in known_organizations)
    markdown.extend(["", "## Manual Organization Review", ""])
    markdown.extend(f"- `{item['term']}`: {item['reason']}" for item in manual_organization_review)
    markdown.extend(["", "## Countries", ""])
    markdown.extend(f"- `{item['term']}` ({item['occurrences']})" for item in countries)
    args.output.with_suffix(".md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    print(f"scanned_cases={cleaned['scanned_cases']}")
    print(f"categories={len(categories)}")
    print(f"category_candidates={sum(len(items) for items in categories.values())}")
    print(f"candidate_organizations={len(organizations)}")
    print(f"candidate_countries={len(countries)}")
    print(f"report_json={args.output}")


if __name__ == "__main__":
    main()