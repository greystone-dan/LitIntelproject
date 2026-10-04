"""Ephemeral, bounded V3-tag-to-resolved-authority research aid.

Input text is never returned, cached, persisted or logged. Tags on *citing*
decisions are retrieval signals, not evidence of an authority's legal treatment.
"""

from __future__ import annotations

from collections import Counter

from sqlalchemy import func, or_, select

from .citations import (
    CASE_CITATION_KINDS,
    extract_statute_reference_matches,
)
from .database import Case, CaseTag, Citation
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION, CoreLegalTaggerV3

MAX_CHARACTERS = 3000
MAX_BODY_BYTES = 40000  # Also accommodates JSON-escaped non-BMP characters.
SIGNALS = 24
POSTINGS_PER_TAG = 128
CITING_DECISIONS = 64
CITATIONS_PER_DECISION = 128
AUTHORITIES = 256
RESULTS = 20
EXCERPT_CHARACTERS = 280
NO_STORE = {"Cache-Control": "no-store", "Pragma": "no-cache"}

# Legacy canonical rows may predate provenance fields. Explicit noncanonical
# sources are never promoted into this research surface.
CANONICAL_SOURCES = (
    "federal_court", "fc_scraper", "official_court", "canlii_html_seed",
    "canlii", "a2aj_parquet", "a2aj_api_seed", "a2aj_curated",
    "a2aj_immigration_core", "huggingface", "canlii_html_seed_fallback",
)
NONCANONICAL_DATASETS = (
    "synthetic", "staged", "discovered", "activity", "reference",
    "side_project", "side-project",
)


def _canonical():
    dataset = func.lower(func.coalesce(Case.dataset_version, ""))
    return (
        or_(Case.source_type.is_(None), Case.source_type.in_(CANONICAL_SOURCES)),
        *(~dataset.like(prefix + "%") for prefix in NONCANONICAL_DATASETS),
    )


def _outcome(metadata):
    extracted = metadata.get("reader_extracted") if isinstance(metadata, dict) else None
    value = extracted.get("government outcome") if isinstance(extracted, dict) else None
    return {
        "won": "government_won", "government won": "government_won",
        "lost": "government_lost", "government lost": "government_lost",
        "mixed": "mixed",
    }.get(str(value or "").strip().lower(), "unclassified")


def find_precedents(proposition: str, db) -> dict:
    """Rank by distinct citing decisions, distinct shared tags, date, citation.

    Every SELECT has a limit. Posting budgets count rows before deduplication.
    No aggregate corpus scan, full decision projection or ORM writes are used.
    """
    if not isinstance(proposition, str) or len(proposition) > MAX_CHARACTERS:
        raise ValueError("Proposition must be text of at most 3000 characters.")
    tags = sorted({(tag.category, tag.value)
                   for tag in CoreLegalTaggerV3().tag(proposition)})
    # Return normalized instrument labels only, never verbatim evidence/input.
    statutes = sorted({match.normalized_citation
                       for match in extract_statute_reference_matches(proposition)})
    payload = {
        "tags": [f"{category}:{value}" for category, value in tags],
        "statutes": statutes,
        "authorities": [],
        "message": "",
        "coverage": {
            "partial": len(tags) > SIGNALS,
            "signal_budget": SIGNALS,
            "postings_per_tag": POSTINGS_PER_TAG,
            "citing_decision_budget": CITING_DECISIONS,
            "citations_per_decision": CITATIONS_PER_DECISION,
            "authority_budget": AUTHORITIES,
            "result_limit": RESULTS,
            "note": "Bounded stored-tag and resolved-citation search, not exhaustive. "
                    "Tags match citing decisions, not legal treatment. Statutes are "
                    "extracted separately and do not affect ranking.",
        },
    }
    if not proposition.strip():
        payload["message"] = "Enter a short legal proposition (up to 3000 characters)."
        return payload
    if not tags:
        payload["message"] = (
            "No V3 legal tags recognized. Try naming the legal issue or doctrine; "
            "statute references alone do not rank authorities."
        )
        return payload

    partial = payload["coverage"]["partial"]
    matched = {}
    for category, value in tags[:SIGNALS]:
        rows = list(db.execute(
            select(CaseTag.case_id, CaseTag.id)
            .where(CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
                   CaseTag.category == category, CaseTag.value == value)
            .order_by(CaseTag.case_id, CaseTag.id).limit(POSTINGS_PER_TAG + 1)
        ))
        partial |= len(rows) > POSTINGS_PER_TAG
        for row in rows[:POSTINGS_PER_TAG]:
            matched.setdefault(row.case_id, set()).add(f"{category}:{value}")
    ids = sorted(matched)
    partial |= len(ids) > CITING_DECISIONS
    sources = list(db.execute(
        select(Case.id, Case.metadata_json).where(
            Case.id.in_(ids[:CITING_DECISIONS]), *_canonical()
        ).order_by(Case.id).limit(CITING_DECISIONS)
    )) if ids else []
    candidates = {}
    source_outcomes = {}
    for source in sources:
        source_outcomes[source.id] = _outcome(source.metadata_json)
        rows = list(db.execute(
            select(Citation.id, Citation.target_case_id).where(
                Citation.source_case_id == source.id,
                Citation.target_case_id.is_not(None),
                Citation.target_case_id != source.id,
                Citation.citation_kind.in_(sorted(CASE_CITATION_KINDS)),
            ).order_by(Citation.id).limit(CITATIONS_PER_DECISION + 1)
        ))
        partial |= len(rows) > CITATIONS_PER_DECISION
        for row in rows[:CITATIONS_PER_DECISION]:
            candidates.setdefault(row.target_case_id, set()).add(source.id)
    target_ids = sorted(candidates)
    partial |= len(target_ids) > AUTHORITIES
    targets = list(db.execute(
        select(Case.id, Case.citation, Case.court, Case.date,
               func.substr(Case.full_text, 1, EXCERPT_CHARACTERS).label("excerpt"))
        .where(Case.id.in_(target_ids[:AUTHORITIES]), Case.citation.is_not(None),
               *_canonical()).order_by(Case.id).limit(AUTHORITIES)
    )) if target_ids else []
    ranked = []
    for target in targets:
        if not target.citation.strip():
            continue
        citing = candidates[target.id]
        shared = sorted(set().union(*(matched[owner] for owner in citing)))
        counts = Counter(source_outcomes[owner] for owner in citing)
        recency = int(target.date.strftime("%Y%m%d")) if target.date else 0
        ranked.append({
            "case_id": target.id, "citation": target.citation,
            "court": target.court, "date": target.date.isoformat() if target.date else None,
            "matched_tags": shared,
            "matching_citing_decisions": len(citing),
            "matched_tag_count": len(shared),
            "recency_key": recency,
            "rank_numbers": [len(citing), len(shared), recency],
            "explanation": (
                f"{len(citing)} distinct matching citing decisions; "
                f"{len(shared)} distinct matched V3 tags; "
                f"{recency} authority recency key (YYYYMMDD)."
            ),
            "excerpt": " ".join((target.excerpt or "").split()) or None,
            "outcome_mix": {
                **{key: counts[key] for key in
                   ("government_won", "government_lost", "mixed", "unclassified")},
                "denominator": len(citing),
                "basis": "Stored reader_extracted government outcomes of matching "
                         "citing decisions; not outcomes of the authority.",
            },
        })
    ranked.sort(key=lambda row: (
        -row["matching_citing_decisions"], -row["matched_tag_count"],
        -row["recency_key"], row["citation"], row["case_id"],
    ))
    payload["authorities"] = ranked[:RESULTS]
    payload["coverage"]["partial"] = bool(partial)
    payload["coverage"]["matching_citing_decisions_checked"] = len(sources)
    if not ranked:
        payload["message"] = (
            "No resolved canonical authorities found within the posting budgets. "
            "Try another legal issue; this is not proof that no precedent exists."
        )
    return payload
