"""Rule-based, read-only authority gap suggestions for ephemeral memos."""

from __future__ import annotations

from collections import Counter, defaultdict

from sqlalchemy import and_, or_, select

from .database import Case, CaseTag, Citation
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION, CoreLegalTaggerV3
from .memo_authority_suggestions import (
    _citation_identities,
    _memo_labels,
    _title_identity,
)

TOP_TAG_LIMIT = 5
COHORT_LIMIT = 500
EDGE_LIMIT = 10000
DISPLAY_LIMIT = 10
CONTRARY_MIN_N = 8
OUTCOME_BUCKETS = ("won", "lost", "mixed", "unclassified")


def _empty(top_tags=None, status="empty_memo"):
    return {
        "disclaimer": "Suggestions for review, not legal advice",
        "status": status,
        "top_tags": top_tags or [],
        "cohort_denominator": 0,
        "missing": [],
        "possibly_contrary": [],
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
            "note": (
                "Counts describe the checked tagged-decision cohorts, "
                "not all decisions."
            ),
        },
    }


def _top_tags(text):
    occurrences = CoreLegalTaggerV3().tag_occurrences(text)
    counts = Counter(f"{tag.category}:{tag.value}" for tag in occurrences)
    return [
        {"tag": tag, "memo_mentions": count}
        for tag, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[
            :TOP_TAG_LIMIT
        ]
    ]


def _tag_predicates(top_tags):
    predicates = []
    for item in top_tags:
        category, value = item["tag"].split(":", 1)
        predicates.append(
            select(CaseTag.id).where(
                CaseTag.case_id == Case.id,
                CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
                and_(CaseTag.category == category, CaseTag.value == value),
            ).exists()
        )
    return predicates


def _outcome(value):
    if isinstance(value, str) and value in OUTCOME_BUCKETS[:-1]:
        return value
    return "unclassified"


def _outcomes(case_ids, cohort):
    counts = dict.fromkeys(OUTCOME_BUCKETS, 0)
    for case_id in case_ids:
        counts[_outcome(cohort[case_id].get("government_outcome"))] += 1
    return counts


def _rate(count, denominator):
    return round(count / denominator * 100, 1) if denominator else None


def _tag_detail(tag, source_ids, cohort, tag_case_ids):
    citing_ids = source_ids & tag_case_ids[tag]
    if not citing_ids:
        return None
    outcomes = _outcomes(citing_ids, cohort)
    baseline = _outcomes(tag_case_ids[tag], cohort)
    return {
        "tag": tag,
        "citing_decisions": len(citing_ids),
        "tag_denominator": len(tag_case_ids[tag]),
        "outcomes": outcomes,
        "baseline_outcomes": baseline,
    }


def _excluded(authority, labels):
    if authority["id"] in labels["ids"]:
        return True
    identities = _citation_identities(authority.get("citation"))
    identities.update(_citation_identities(authority.get("secondary_citation")))
    if identities & labels["citations"]:
        return True
    title = _title_identity(authority.get("title"))
    return bool(title and title in labels["titles"])


def rank_gap_suggestions(cohort_rows, edge_rows, authority_rows, memo_labels, top_tags):
    """Rank distinct tagged-source citations and compare losses with tag baselines."""
    cohort = {row["id"]: row for row in cohort_rows}
    result = _empty(top_tags, "complete" if cohort else "empty_cohort")
    result["cohort_denominator"] = len(cohort)
    tag_case_ids = defaultdict(set)
    for case_id, row in cohort.items():
        for tag in set(row.get("tags") or []):
            tag_case_ids[tag].add(case_id)

    sources_by_target = defaultdict(set)
    for edge in edge_rows:
        source_id, target_id = edge["source_case_id"], edge.get("target_case_id")
        if source_id in cohort and target_id is not None:
            sources_by_target[target_id].add(source_id)
    result["coverage"]["citation_edges_checked"] = sum(
        len(sources) for sources in sources_by_target.values()
    )

    missing = []
    contrary = []
    hidden_below_threshold = 0
    for authority in authority_rows:
        if _excluded(authority, memo_labels):
            continue
        source_ids = sources_by_target.get(authority["id"], set())
        if not source_ids:
            continue
        tag_details = [
            detail
            for tag in sorted(tag_case_ids)
            if (detail := _tag_detail(tag, source_ids, cohort, tag_case_ids))
        ]
        if not tag_details:
            continue
        item = {
            "id": authority["id"],
            "title": authority["title"],
            "citation": authority.get("citation"),
            "citing_decisions": len(source_ids),
            "cohort_denominator": len(cohort),
            "tags_matched": tag_details,
            "why": (
                "Cited by distinct decisions in the memo's tagged cohorts: "
                + "; ".join(
                    f"{row['tag']} ({row['citing_decisions']}/{row['tag_denominator']})"
                    for row in tag_details
                )
                + "."
            ),
        }
        missing.append(item)
        contrary_tags = []
        for detail in tag_details:
            n = detail["citing_decisions"]
            lost = detail["outcomes"]["lost"]
            baseline_n = detail["tag_denominator"]
            baseline_lost = detail["baseline_outcomes"]["lost"]
            if lost * baseline_n <= baseline_lost * n:
                continue
            if n < CONTRARY_MIN_N:
                hidden_below_threshold += 1
                continue
            contrary_tags.append({
                "tag": detail["tag"],
                "authority": {
                    "against_minister": lost,
                    "unclassified": detail["outcomes"]["unclassified"],
                    "denominator": n,
                    "rate_percent": _rate(lost, n),
                },
                "tag_baseline": {
                    "against_minister": baseline_lost,
                    "unclassified": detail["baseline_outcomes"]["unclassified"],
                    "denominator": baseline_n,
                    "rate_percent": _rate(baseline_lost, baseline_n),
                },
            })
        if contrary_tags:
            contrary.append({**item, "contrary_tags": contrary_tags})

    missing.sort(key=lambda row: (-row["citing_decisions"], row["id"]))
    contrary.sort(
        key=lambda row: (
            -max(
                tag["authority"]["rate_percent"] - tag["tag_baseline"]["rate_percent"]
                for tag in row["contrary_tags"]
            ),
            -row["citing_decisions"],
            row["id"],
        )
    )
    result["missing"] = missing[:DISPLAY_LIMIT]
    result["possibly_contrary"] = contrary[:DISPLAY_LIMIT]
    result["contrary_hidden_below_threshold"] = hidden_below_threshold
    result["coverage"].update(
        missing_total=len(missing),
        contrary_total=len(contrary),
        missing_truncated=len(missing) > DISPLAY_LIMIT,
        contrary_truncated=len(contrary) > DISPLAY_LIMIT,
    )
    return result


def build_memo_gap_suggestions(analysis, session=None):
    """Tag the in-memory memo and compare its tags with bounded local case data."""
    text = analysis.get("text") or ""
    if not text.strip():
        return _empty()
    top_tags = _top_tags(text)
    if not top_tags:
        return _empty(status="no_tags")
    if session is None:
        return _empty(top_tags, "session_unavailable")

    tags = [item["tag"] for item in top_tags]
    predicates = _tag_predicates(top_tags)
    statement = select(
        Case.id,
        Case.metadata_json["reader_extracted"]["government outcome"].as_string().label(
            "government_outcome"
        ),
        *(
            predicate.label(f"tag_{index}")
            for index, predicate in enumerate(predicates)
        ),
    ).where(or_(*predicates)).order_by(Case.id).limit(COHORT_LIMIT + 1)
    selected = list(session.execute(statement).mappings())
    cohort_truncated = len(selected) > COHORT_LIMIT
    cohort = [
        {
            "id": row["id"],
            "government_outcome": row["government_outcome"],
            "tags": [tag for index, tag in enumerate(tags) if row[f"tag_{index}"]],
        }
        for row in selected[:COHORT_LIMIT]
    ]
    if not cohort:
        return rank_gap_suggestions([], [], [], _memo_labels(analysis), top_tags)

    edges = list(
        session.execute(
            select(Citation.source_case_id, Citation.target_case_id)
            .where(
                Citation.source_case_id.in_([row["id"] for row in cohort]),
                Citation.target_case_id.is_not(None),
            )
            .distinct()
            .order_by(Citation.source_case_id, Citation.target_case_id)
            .limit(EDGE_LIMIT + 1)
        ).mappings()
    )
    edges_truncated = len(edges) > EDGE_LIMIT
    edges = edges[:EDGE_LIMIT]
    target_ids = sorted({row["target_case_id"] for row in edges})
    authorities = (
        list(
            session.execute(
                select(Case.id, Case.title, Case.citation, Case.secondary_citation)
                .where(Case.id.in_(target_ids))
                .order_by(Case.id)
            ).mappings()
        )
        if target_ids
        else []
    )
    result = rank_gap_suggestions(
        cohort, edges, authorities, _memo_labels(analysis), top_tags
    )
    result["coverage"].update(
        partial=cohort_truncated or edges_truncated,
        cohort_truncated=cohort_truncated,
        citation_edges_truncated=edges_truncated,
    )
    if result["coverage"]["partial"]:
        result["status"] = "partial"
        result["coverage"]["note"] = (
            "Caps truncated the checked cohort or citation edges; rankings and outcome "
            "rates may differ from complete coverage."
        )
    return result
