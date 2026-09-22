from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

from backend.database import Case, SessionLocal
from backend.metadata_subjects import _derive_case_subject_fields
from scripts.inspect_discussion_units import inspect_case

DEFAULT_START = date(2020, 9, 22)
DEFAULT_END = date(2026, 9, 22)


@dataclass(frozen=True)
class ThemeDefinition:
    theme_id: str
    label: str
    phrases: tuple[str, ...] = ()
    tag_values: tuple[str, ...] = ()
    instrument_keys: tuple[str, ...] = ()
    provision_sections: tuple[str, ...] = ()


THEMES = (
    ThemeDefinition(
        "procedural_fairness",
        "Procedural fairness",
        ("procedural fairness", "right to be heard", "reasonable apprehension of bias"),
        ("procedural_fairness",),
    ),
    ThemeDefinition(
        "reasonableness_review",
        "Reasonableness review",
        ("reasonableness review", "reasonableness standard", "Vavilov"),
        ("reasonableness", "judicial_review"),
    ),
    ThemeDefinition(
        "humanitarian_compassionate",
        "Humanitarian and compassionate relief",
        ("humanitarian and compassionate", "H&C", "best interests of the child"),
        ("humanitarian_compassionate", "best_interests_child"),
        ("canada.immigration_and_refugee_protection_act",),
        ("25",),
    ),
    ThemeDefinition(
        "refugee_protection",
        "Refugee protection",
        ("refugee protection", "Convention refugee", "well-founded fear", "non-refoulement"),
        ("refugee_protection", "state_protection", "non_refoulement"),
        ("canada.immigration_and_refugee_protection_act",),
        ("96", "97"),
    ),
    ThemeDefinition(
        "credibility_evidence",
        "Credibility and evidence",
        ("credibility assessment", "credibility findings", "evidentiary assessment"),
        ("credibility", "evidence"),
    ),
    ThemeDefinition(
        "inadmissibility_security",
        "Inadmissibility and security",
        ("inadmissibility", "security grounds", "organized criminality", "serious criminality"),
        ("inadmissibility", "security", "organized_criminality"),
        ("canada.immigration_and_refugee_protection_act",),
        ("34", "35", "36", "37"),
    ),
    ThemeDefinition(
        "detention_release",
        "Detention and release",
        ("detention review", "continued detention", "release from detention", "bondsperson"),
        ("detention", "detention_review"),
        ("canada.immigration_and_refugee_protection_act",),
        ("55", "58"),
    ),
    ThemeDefinition(
        "removal_stay",
        "Removal and stays",
        ("removal order", "stay of removal", "deportation order", "removal proceedings"),
        ("removal", "stay_of_removal"),
    ),
    ThemeDefinition(
        "charter_rights",
        "Charter rights",
        ("Canadian Charter of Rights", "Charter rights", "section 7 of the Charter"),
        ("constitutional_charter", "charter"),
        ("canada.charter_of_rights_and_freedoms",),
    ),
    ThemeDefinition(
        "family_reunification",
        "Family reunification",
        ("family reunification", "family class", "spousal sponsorship"),
        ("family_reunification", "sponsorship"),
    ),
)


ROLE_WEIGHTS = {
    "issue": 4,
    "reasoning_application": 4,
    "governing_rule": 3,
    "party_position": 2,
    "disposition": 2,
    "counterargument_limitation": 1,
    "evidence_fact": 1,
}


def _normal(value: object) -> str:
    return str(value or "").strip().casefold()


def _text_evidence(theme: ThemeDefinition, text: str) -> list[dict[str, str]]:
    lowered = text.casefold()
    return [
        {"kind": "phrase", "value": phrase}
        for phrase in theme.phrases
        if phrase.casefold() in lowered
    ]


def _tag_evidence(theme: ThemeDefinition, tags: Iterable[Any]) -> list[dict[str, object]]:
    values = {_normal(value) for value in theme.tag_values}
    return [
        {
            "kind": "tag",
            "value": tag.value,
            "category": tag.category,
            "score": tag.score,
            "taxonomy_version": tag.taxonomy_version,
            "evidence": tag.evidence,
            "offset_start": tag.offset_start,
            "offset_end": tag.offset_end,
        }
        for tag in tags
        if _normal(tag.value) in values
    ]


def _statute_evidence(theme: ThemeDefinition, statutes: Iterable[Any]) -> list[dict[str, object]]:
    instruments = {_normal(value) for value in theme.instrument_keys}
    sections = {_normal(value) for value in theme.provision_sections}
    evidence = []
    for statute in statutes:
        instrument = _normal(statute.instrument_key)
        section = _normal(statute.provision_section or statute.pinpoint)
        section_match = any(section == value or section.startswith(value + "(") for value in sections)
        instrument_match = instrument and instrument in instruments and not sections
        if instrument_match or section_match:
            evidence.append(
                {
                    "kind": "statute",
                    "value": statute.reference_text or statute.normalized_reference or statute.pinpoint,
                    "instrument_key": statute.instrument_key,
                    "provision_section": statute.provision_section,
                    "pinpoint": statute.pinpoint,
                    "offset_start": statute.offset_start,
                    "offset_end": statute.offset_end,
                }
            )
    return evidence


def _role_evidence(theme: ThemeDefinition, discussion: dict[str, Any] | None) -> list[dict[str, object]]:
    if not discussion:
        return []
    evidence = []
    theme_terms = {_normal(value) for value in theme.phrases}
    for unit in discussion.get("discussion_units", []):
        for subtheme in unit.get("subthemes", []):
            text = _normal(subtheme.get("text") or subtheme.get("explanation"))
            key_terms = {_normal(value) for value in subtheme.get("key_terms", [])}
            if not (any(term and (term in text or term in key_terms) for term in theme_terms)):
                continue
            for role in subtheme.get("argument_roles", []):
                evidence.append(
                    {
                        "kind": "discussion_role",
                        "role": role,
                        "subtheme_id": subtheme.get("subtheme_id"),
                        "paragraph_indices": subtheme.get("paragraph_indices", []),
                        "explanation": subtheme.get("explanation"),
                    }
                )
    return evidence


def classify_theme(theme: ThemeDefinition, *, text: str, tags: Iterable[Any], statutes: Iterable[Any], subjects: dict[str, tuple[str, float]], discussion: dict[str, Any] | None = None) -> dict[str, object] | None:
    evidence = _text_evidence(theme, text)
    evidence.extend(_tag_evidence(theme, tags))
    evidence.extend(_statute_evidence(theme, statutes))
    role_evidence = _role_evidence(theme, discussion)
    evidence.extend(role_evidence)
    subject_values = {_normal(value[0]) for value in subjects.values()}
    if any(_normal(theme.theme_id) in value or any(_normal(tag) in value for tag in theme.tag_values) for value in subject_values):
        evidence.append({"kind": "subject", "value": ", ".join(value[0] for value in subjects.values())})
    if not evidence:
        return None
    role_score = sum(ROLE_WEIGHTS.get(str(item.get("role")), 0) for item in role_evidence)
    independent_kinds = {str(item["kind"]) for item in evidence}
    if role_score >= 4:
        status = "central_issue"
        threshold_met = "role_score >= 4"
    elif "tag" in independent_kinds and "statute" in independent_kinds:
        status = "central_issue"
        threshold_met = "tag + statute evidence"
    elif len(independent_kinds) >= 3:
        status = "central_issue"
        threshold_met = "3+ independent evidence kinds"
    elif role_score or len(independent_kinds) >= 2:
        status = "material_issue"
        threshold_met = "role evidence or 2+ independent evidence kinds"
    elif "phrase" in independent_kinds or "tag" in independent_kinds or "statute" in independent_kinds:
        status = "mentioned"
        threshold_met = "single direct evidence kind"
    else:
        status = "mentioned"
        threshold_met = "fallback evidence"
    score = role_score * 2 + len(independent_kinds)
    return {
        "theme_id": theme.theme_id,
        "label": theme.label,
        "status": status,
        "score": score,
        "classification_factors": {
            "role_score": role_score,
            "independent_evidence_kinds": sorted(independent_kinds),
            "threshold_met": threshold_met,
        },
        "evidence_count": len(evidence),
        "evidence_kinds": sorted(independent_kinds),
        "evidence": evidence,
    }


def build_case_theme_record(case: Any, *, tags: Iterable[Any] = (), statutes: Iterable[Any] = (), discussion: dict[str, Any] | None = None) -> dict[str, object]:
    tags = tuple(tags)
    statutes = tuple(statutes)
    text = "\n".join(value for value in (case.title, case.summary, case.full_text) if value)
    subjects = _derive_case_subject_fields(text, case.metadata_json or {})
    themes = [
        result
        for theme in THEMES
        if (result := classify_theme(theme, text=text, tags=tags, statutes=statutes, subjects=subjects, discussion=discussion))
    ]
    themes.sort(key=lambda item: (-int(item["score"]), str(item["theme_id"])))
    return {
        "case_id": case.id,
        "title": case.title,
        "date": case.date.isoformat() if case.date else None,
        "court": case.court,
        "citation": case.citation,
        "subjects": {key: {"value": value, "confidence": confidence} for key, (value, confidence) in subjects.items()},
        "themes": themes,
        "primary_themes": [theme for theme in themes if theme["status"] == "central_issue"],
        "secondary_themes": [theme for theme in themes if theme["status"] == "material_issue"],
        "mentioned_themes": [theme for theme in themes if theme["status"] == "mentioned"],
        "evidence_summary": {
            "tag_count": len(tuple(tags)),
            "statute_count": len(tuple(statutes)),
            "citation_count": len(getattr(case, "outgoing_citations", ()) or ()),
            "discussion_unit_count": len((discussion or {}).get("discussion_units", [])),
        },
    }


def build_report(session, start_date: date = DEFAULT_START, end_date: date = DEFAULT_END, limit: int | None = None, chunk_set: str = "paragraph") -> dict[str, object]:
    query = select(Case).where(Case.date.between(start_date, end_date)).order_by(Case.date, Case.id)
    if limit:
        query = query.limit(limit)
    cases = session.scalars(query).all()
    records = []
    for case in cases:
        tags = tuple(case.tags)
        statutes = tuple(case.statute_references)
        discussion = inspect_case(
            session,
            case.id,
            chunk_set=chunk_set,
            threshold=0.35,
            consecutive_low_scores=2,
        )
        records.append(build_case_theme_record(case, tags=tags, statutes=statutes, discussion=discussion))
    return {
        "method": "recent_case_theme_discovery",
        "version": "1.0",
        "date_window": {"start": start_date.isoformat(), "end": end_date.isoformat()},
        "discussion_units": {"chunk_set": chunk_set, "threshold": 0.35, "consecutive_low_scores": 2},
        "theme_definitions": [{"theme_id": theme.theme_id, "label": theme.label} for theme in THEMES],
        "case_count": len(records),
        "cases_with_themes": sum(bool(record["themes"]) for record in records),
        "records": records,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a read-only recent-case issue theme report.")
    parser.add_argument("--start-date", type=date.fromisoformat, default=DEFAULT_START)
    parser.add_argument("--end-date", type=date.fromisoformat, default=DEFAULT_END)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--chunk-set", default="paragraph")
    parser.add_argument("--output", type=Path, default=Path("data/eval/reports/recent_case_themes.json"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with SessionLocal() as session:
        report = build_report(session, args.start_date, args.end_date, args.limit, args.chunk_set)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("method", "version", "date_window", "case_count", "cases_with_themes")}))


if __name__ == "__main__":
    main()
