"""Create a conservative review shortlist from an LLM tag report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.legal_tagger import COUNTRIES, ORGANIZATIONS, RULES
from backend.legal_tagger_v2 import CORE_TERMS


ALLOWED_CATEGORIES = {
    "immigration_keyword", "immigration_status", "immigration_program", "proceeding",
    "procedural_issue", "remedy", "risk", "inadmissibility_organization", "country_or_territory",
}
CANONICAL_CATEGORY = {
    "procedural_issue": "immigration_keyword",
    "remedy": "immigration_keyword",
    "risk": "immigration_keyword",
}
AGENCY_OR_TRIBUNAL = {
    "canada border services agency", "immigration and refugee board", "refugee protection division",
    "refugee appeal division", "immigration appeal division", "immigration division", "ircc", "cbsa", "crdd", "rpd", "rad", "iad",
}
NON_GROUP_ORGANIZATION_TERMS = {
    "agency", "commission", "division", "immigration officer", "officer", "tribunal",
    "united nations", "amnesty international", "interpol",
}
DOMESTIC_ORGANIZATION_TERMS = {"canadian", "canada", "ontario", "quebec", "alberta", "labrador"}
GENERIC_TERMS = {
    "appeal", "application", "canada", "claim", "credibility", "decision", "evidence", "immigration",
    "applicant", "jurisdiction", "law", "person", "refugee", "remedy", "review", "risk", "status", "treatment",
}
BAD_VARIATIONS = {"aprra@", "ah & c application@", "pre-release risk assessment"}
COUNTRY_NAMES = {"canada"} | {" ".join(value.lower().split()) for value in COUNTRIES}
ORGANIZATION_NAMES = {" ".join(value.lower().split()) for value in ORGANIZATIONS}
MISCLASSIFIED_TERMS = {
    "immigration_program": {"canada pension plan", "immigration and refugee protection act", "irpa", "refugee appeal division", "refugee protection division"},
    "immigration_status": {"applicant", "inadmissibility", "judicial review", "permanent residence", "refusal", "refugee claim", "visitor's visa"},
}


def normalize(value: object) -> str:
    return re.sub(r"\s+", " ", str(value).lower().replace("’", "'")).strip(" .,:;()[]")


EXISTING_VALUES_BY_CATEGORY = defaultdict(set)
for rule in RULES:
    EXISTING_VALUES_BY_CATEGORY[rule.category].add(normalize(rule.value.replace("_", " ")))
EXISTING_VALUES_BY_CATEGORY["country_or_territory"].update(normalize(value.replace("_", " ")) for value in COUNTRIES)
EXISTING_VALUES_BY_CATEGORY["inadmissibility_organization"].update(normalize(value.replace("_", " ")) for value in ORGANIZATIONS)
CORE_VALUES = {
    normalize(value.replace("_", " "))
    for values in CORE_TERMS.values()
    for value in values
}
EXISTING_CATEGORY_MAP = {
    "immigration_keyword": {"issue", "proceeding", "procedural_issue", "remedy", "risk", "inadmissibility", "cbsa_program", "enforcement_action", "enforcement_impediment", "program_impact", "detention_ground", "release_mechanism", "evidence", "document_type", "standard_of_review", "outcome", "procedural_posture", "procedural_step", "evidence_issue"},
    "immigration_program": {"immigration_program"},
    "immigration_status": {"immigration_status"},
    "proceeding": {"proceeding"},
    "country_or_territory": {"country_or_territory"},
    "inadmissibility_organization": {"organization"},
}


def is_existing_candidate(category: str, canonical: str) -> bool:
    normalized = normalize(canonical)
    return any(
        normalized == existing
        for existing_category in EXISTING_CATEGORY_MAP.get(category, {category})
        for existing in EXISTING_VALUES_BY_CATEGORY.get(existing_category, set())
    )


def coverage_for_candidate(category: str, canonical: str) -> str:
    if normalize(canonical) in CORE_VALUES:
        return "core_v2"
    if is_existing_candidate(category, canonical):
        return "advanced_v1"
    return "candidate_new"


def is_clean_term(term: str) -> bool:
    words = term.split()
    return bool(
        term
        and re.fullmatch(r"[a-z][a-z' -]*", term)
        and len(term) >= 4
        and len(words) <= 8
        and not any(word in {"the", "this", "that", "his", "her", "their"} for word in words[:1])
        and not term.startswith(("application for ", "letter from ", "president of "))
        and term not in GENERIC_TERMS
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/eval/reports/llm-tag-candidate-review-500.json"))
    parser.add_argument("--output", type=Path, default=Path("data/eval/reports/llm-tag-proposals-500.json"))
    parser.add_argument("--minimum-cases", type=int, default=3)
    args = parser.parse_args()
    report = json.loads(args.input.read_text(encoding="utf-8"))
    grouped: defaultdict[tuple[str, str], dict] = defaultdict(lambda: {"variations": set(), "samples": [], "case_count": 0, "confidence_max": 0.0})
    for item in report.get("tags", []):
        category = CANONICAL_CATEGORY.get(normalize(item.get("category")), normalize(item.get("category")))
        term = normalize(item.get("canonical"))
        if category not in ALLOWED_CATEGORIES or not is_clean_term(term):
            continue
        if term in MISCLASSIFIED_TERMS.get(category, set()):
            continue
        if category == "country_or_territory" and term not in COUNTRY_NAMES:
            continue
        if category == "inadmissibility_organization":
            words = set(term.split())
            if term in AGENCY_OR_TRIBUNAL or term in ORGANIZATION_NAMES:
                continue
            if term in NON_GROUP_ORGANIZATION_TERMS or words & DOMESTIC_ORGANIZATION_TERMS:
                continue
        key = (category, term)
        value = grouped[key]
        value["case_count"] = max(value["case_count"], int(item.get("case_count", 0)))
        value["confidence_max"] = max(value["confidence_max"], float(item.get("confidence_max", 0)))
        value["variations"].update(
            variation for variation in (normalize(v) for v in item.get("variations", []))
            if variation and variation not in BAD_VARIATIONS and is_clean_term(variation)
        )
        value["samples"].extend(item.get("samples", [])[:3])

    proposals = []
    for (category, term), value in grouped.items():
        if value["case_count"] < args.minimum_cases:
            continue
        proposals.append({
            "category": category,
            "canonical": term,
            "coverage": coverage_for_candidate(category, term),
            "variations": sorted(value["variations"]),
            "case_count": value["case_count"],
            "confidence_max": value["confidence_max"],
            "samples": value["samples"][:3],
        })
    proposals.sort(key=lambda item: (item["category"], -item["case_count"], item["canonical"]))
    cleaned = {"source_report": str(args.input), "processed_cases": report.get("processed_cases"), "minimum_cases": args.minimum_cases, "tags": proposals}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(cleaned, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown = ["# LLM Tag Proposals", "", f"Source: {cleaned['processed_cases']} cases. Minimum recurring cases: {args.minimum_cases}.", "Review candidates only; nothing has been added to production tagging.", ""]
    for category in sorted({item["category"] for item in proposals}):
        markdown.extend([f"## {category}", ""])
        for item in [item for item in proposals if item["category"] == category]:
            variations = ", ".join(item["variations"][:8])
            markdown.append(f"- **{item['canonical']}** [{item['coverage']}] ({item['case_count']} cases, confidence {item['confidence_max']:.2f})" + (f"; variations: {variations}" if variations else ""))
        markdown.append("")
    args.output.with_suffix(".md").write_text("\n".join(markdown), encoding="utf-8")
    print(f"processed_cases={cleaned['processed_cases']}")
    print(f"proposals={len(proposals)}")
    print(f"report_json={args.output}")


if __name__ == "__main__":
    main()