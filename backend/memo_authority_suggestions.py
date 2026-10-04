"""Bounded, read-only suggestions; uploaded memo text is never persisted."""

from __future__ import annotations

import re
from collections import defaultdict

from sqlalchemy import and_, or_, select

from .database import Case, CaseTag, Citation, StatuteReference
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION, CoreLegalTaggerV3

COHORT_LIMIT = 500
EDGE_LIMIT = 10000
DISPLAY_LIMIT = 10


def _citation_identities(value):
    normalized = " ".join((value or "").upper().split())
    values = {normalized} if normalized else set()
    values.update(re.findall(r"\b\d{4} [A-Z]{2,8} \d+\b", normalized))
    return (
        values
        | {value.replace(" FCT ", " FC ") for value in values}
        | {value.replace(" FC ", " FCT ") for value in values}
    )


def _title_identity(value):
    value = " ".join(re.sub(r"[^\w\s]", " ", (value or "").casefold()).split())
    # Full adversarial labels only, never party fragments or guessed aliases.
    if len(value) >= 8 and re.search(r"\s(?:v|vs|versus|c)\s", value):
        return re.sub(r"\s(?:vs|versus|c)\s", " v ", value)
    return None


def _memo_labels(analysis):
    ids, citations, titles = set(), set(), set()
    for row in analysis.get("case_citations") or []:
        if row.get("resolved_case_id") is not None:
            ids.add(row["resolved_case_id"])
        for field in ("normalized_reference", "reference_text", "resolved_case_citation"):
            citations.update(_citation_identities(row.get(field)))
        for field in ("normalized_reference", "reference_text", "resolved_case_title"):
            title = _title_identity(row.get(field))
            if title:
                titles.add(title)
    return {"ids": ids, "citations": citations, "titles": titles}


def _empty(signals, status):
    return {
        "disclaimer": "Suggestions, not legal advice",
        "status": status,
        "signals": signals,
        "cohort_denominator": 0,
        "missing": [],
        "contrary": [],
        "contrary_hidden_below_threshold": 0,
        "coverage": {
            "partial": False,
            "cohort_limit": COHORT_LIMIT,
            "citation_edge_limit": EDGE_LIMIT,
            "cohort_truncated": False,
            "citation_edges_truncated": False,
            "citation_edges_checked": 0,
            "missing_total": 0,
            "contrary_total": 0,
            "missing_truncated": False,
            "contrary_truncated": False,
            "outcome_source": "cases.metadata_json.reader_extracted.government outcome",
            "note": "Counts describe the checked cohort, not all decisions.",
        },
    }


def rank_authorities(cohort_rows, edge_rows, authority_rows, memo_labels, signals):
    """Rank invented or selected mappings; outcomes are stored Minister-relative values.

    Cohort rows contain id, government_outcome, shared_tags and shared_statutes.
    Edges contain source_case_id and target_case_id. Authority rows contain only
    id, title, citation and secondary_citation. Each source-target pair counts once.
    """
    cohort = {row["id"]: row for row in cohort_rows}
    result = _empty(signals, "complete" if cohort else "empty_cohort")
    result["cohort_denominator"] = len(cohort)
    sources = defaultdict(set)
    for edge in edge_rows:
        if edge["source_case_id"] in cohort and edge["target_case_id"] is not None:
            sources[edge["target_case_id"]].add(edge["source_case_id"])
    result["coverage"]["citation_edges_checked"] = sum(map(len, sources.values()))
    missing = []
    for authority in authority_rows:
        target = authority["id"]
        citing = sources.get(target)
        if not citing or target in memo_labels.get("ids", set()):
            continue
        identities = _citation_identities(authority.get("citation"))
        identities.update(_citation_identities(authority.get("secondary_citation")))
        if identities & memo_labels.get("citations", set()):
            continue
        if _title_identity(authority.get("title")) in memo_labels.get("titles", set()):
            continue
        outcomes = dict.fromkeys(("won", "lost", "mixed", "unclassified"), 0)
        tags, statutes = set(), set()
        for source in citing:
            row = cohort[source]
            outcome = row.get("government_outcome")
            bucket = outcome if isinstance(outcome, str) and outcome in outcomes else "unclassified"
            outcomes[bucket] += 1
            tags.update(set(row.get("shared_tags") or []) & set(signals["tags"]))
            statutes.update(set(row.get("shared_statutes") or []) & set(signals["statutes"]))
        outcomes["denominator"] = len(citing)
        missing.append({
            "id": target,
            "title": authority["title"],
            "citation": authority.get("citation"),
            "citing_decisions": len(citing),
            "cohort_denominator": len(cohort),
            "why": {"shared_tags": sorted(tags), "shared_statutes": sorted(statutes)},
            "outcomes": outcomes,
        })
    missing.sort(key=lambda row: (-row["citing_decisions"], row["id"]))
    majority_lost = [
        row for row in missing
        if row["outcomes"]["lost"] * 2 > row["outcomes"]["denominator"]
    ]
    contrary = [row for row in majority_lost if row["citing_decisions"] >= 5]
    result["contrary_hidden_below_threshold"] = sum(
        row["citing_decisions"] < 5 for row in majority_lost
    )
    result["missing"] = missing[:DISPLAY_LIMIT]
    result["contrary"] = contrary[:DISPLAY_LIMIT]
    result["coverage"].update(
        missing_total=len(missing), contrary_total=len(contrary),
        missing_truncated=len(missing) > DISPLAY_LIMIT,
        contrary_truncated=len(contrary) > DISPLAY_LIMIT,
    )
    return result


def _signal_predicates(signals):
    predicates = []
    for tag in signals["tags"]:
        category, value = tag.split(":", 1)
        predicates.append(select(CaseTag.id).where(
            CaseTag.case_id == Case.id,
            CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
            and_(CaseTag.category == category, CaseTag.value == value),
        ).exists())
    for statute in signals["statutes"]:
        # Exact normalized identity, including every nested provision component.
        predicates.append(select(StatuteReference.id).where(
            StatuteReference.source_case_id == Case.id,
            StatuteReference.normalized_reference == statute,
        ).exists())
    return predicates


def _memo_statutes(analysis):
    """Do not broaden a provision when the existing extractor stopped early."""
    text = analysis.get("text") or ""
    identities = set()
    for row in analysis.get("statute_references") or []:
        end = row.get("offset_end")
        if isinstance(end, int) and 0 <= end < len(text):
            if re.match(r"\s*\([A-Za-z0-9]", text[end:]):
                continue
        if row.get("normalized_reference"):
            identities.add(row["normalized_reference"])
    return sorted(identities)


def build_authority_suggestions(analysis: dict, session=None) -> dict:
    """Use only deterministic memo signals and resolved canonical citation edges."""
    tags = CoreLegalTaggerV3().tag(analysis.get("text")) if analysis.get("text") else []
    signals = {
        "tags": sorted({f"{tag.category}:{tag.value}" for tag in tags}),
        "statutes": _memo_statutes(analysis),
    }
    if not any(signals.values()):
        return _empty(signals, "no_signals")
    if session is None:
        return _empty(signals, "session_unavailable")

    predicates = _signal_predicates(signals)
    statement = select(
        Case.id,
        Case.metadata_json["reader_extracted"]["government outcome"].as_string().label(
            "government_outcome"
        ),
        *(predicate.label(f"signal_{index}") for index, predicate in enumerate(predicates)),
    ).where(or_(*predicates)).order_by(Case.id).limit(COHORT_LIMIT + 1)
    selected = list(session.execute(statement).mappings())
    cohort_truncated = len(selected) > COHORT_LIMIT
    cohort = []
    for row in selected[:COHORT_LIMIT]:
        cohort.append({
            "id": row["id"],
            "government_outcome": row["government_outcome"],
            "shared_tags": [
                tag for index, tag in enumerate(signals["tags"]) if row[f"signal_{index}"]
            ],
            "shared_statutes": [
                statute for index, statute in enumerate(
                    signals["statutes"], start=len(signals["tags"])
                ) if row[f"signal_{index}"]
            ],
        })
    labels = _memo_labels(analysis)
    if not cohort:
        return rank_authorities([], [], [], labels, signals)
    edges = list(session.execute(select(
        Citation.source_case_id, Citation.target_case_id,
    ).join(Case, Case.id == Citation.target_case_id).where(
        Citation.source_case_id.in_([row["id"] for row in cohort]),
    ).distinct().order_by(
        Citation.source_case_id, Citation.target_case_id,
    ).limit(EDGE_LIMIT + 1)).mappings())
    edges_truncated = len(edges) > EDGE_LIMIT
    edges = edges[:EDGE_LIMIT]
    target_ids = sorted({row["target_case_id"] for row in edges})
    authorities = list(session.execute(select(
        Case.id, Case.title, Case.citation, Case.secondary_citation,
    ).where(Case.id.in_(target_ids)).order_by(Case.id)).mappings()) if target_ids else []
    result = rank_authorities(cohort, edges, authorities, labels, signals)
    result["coverage"].update(
        partial=cohort_truncated or edges_truncated,
        cohort_truncated=cohort_truncated,
        citation_edges_truncated=edges_truncated,
    )
    if result["coverage"]["partial"]:
        result["status"] = "partial"
        result["coverage"]["note"] = (
            "Caps truncated the checked cohort or citation edges; counts, rankings and "
            "outcome proportions may differ from complete coverage."
        )
    return result
