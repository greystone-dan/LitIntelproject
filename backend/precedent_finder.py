"""Ephemeral, bounded V3-tag-to-resolved-authority research aid.

Input text is never returned, cached, persisted or logged. Tags on *citing*
decisions are retrieval signals, not evidence of an authority's legal treatment.
"""

from __future__ import annotations

import re
from collections import Counter

from sqlalchemy import func, or_, select

from .case_formatter import format_decision
from .citations import (
    CASE_CITATION_KINDS,
    extract_statute_reference_matches,
)
from .database import Case, CaseTag, Citation
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION, CoreLegalTaggerV3
from .paragraph_similarity import (
    TEXT_CHARS,
    _authority,
    _citation_query,
    _located_chunks,
)

MAX_CHARACTERS = 3000
MAX_BODY_BYTES = 40000  # Also accommodates JSON-escaped non-BMP characters.
SIGNALS = 24
POSTINGS_PER_TAG = 128
CITING_DECISIONS = 64
CITATIONS_PER_DECISION = 128
AUTHORITIES = 256
RESULTS = 20
PARAGRAPHS_PER_DECISION = 64
PARAGRAPHS_TOTAL = 512
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


def _paragraph_only(row):
    """Reject structured tails while allowing ordinary paragraph continuations."""
    start = 0
    context = row.text
    if re.match(r"^\d{1,3}\s+(?=\S)", row.text):
        # _located_chunks already verified this actual, bounded SCC context.
        # Never fabricate a marker or restart bare paragraph numbering.
        if row.prefix is None or len(row.prefix) != row.pos - 1:
            return False
        context = row.prefix + row.text
        start = row.pos - 1
    blocks = [block for block in format_decision(context) if block["end"] > start]
    return bool(blocks) and all(
        block["type"] in {"para", "text", "listitem", "quote"} for block in blocks
    )


def _source_excerpts(db, targets, sources, matched, citation_ids):
    """Choose exact citing paragraphs, not authority text or target pinpoints.

    Selection uses distinct *decision-level* matched tags, then source citation
    label, source ID, paragraph number and stored citation row ID. Paragraph
    rows (including rejected rows) share one global budget across all results.
    Canonical occurrence/short-anchor verification and paragraph location are
    the same as paragraph similarity; no offsets are inferred from text.
    """
    wanted = {row["case_id"] for row in targets}
    choices, checked, partial = {}, 0, False
    ordered = sorted(sources, key=lambda source: (
        -len(matched[source.id]), source.citation or "", source.id,
    ))
    for source in ordered:
        ids = citation_ids.get(source.id, {})
        relevant = sorted(row_id for row_id, target in ids.items() if target in wanted)
        if not relevant:
            continue
        budget = min(PARAGRAPHS_PER_DECISION, PARAGRAPHS_TOTAL - checked)
        if budget <= 0:
            partial = True
            break
        # Discovery IDs were charged before filtering. Reverification cannot
        # expand that bounded set or read a full source/target decision.
        spans = list(db.execute(_citation_query().where(
            Citation.id.in_(relevant),
            Citation.source_case_id == source.id,
        ).order_by(Citation.id).limit(CITATIONS_PER_DECISION)))
        paragraphs, capped, consumed = _located_chunks(db, source.id, budget=budget)
        checked += consumed
        partial |= capped
        # One numbered starting block alone does not make headings, signatures,
        # footnotes or footer text in the same stored chunk paragraph evidence.
        paragraphs = [paragraph for paragraph in paragraphs if _paragraph_only(paragraph)]
        for span in spans:
            citation = span[0]
            if _authority(span) != f"case:{ids[citation.id]}":
                continue
            containing = [
                paragraph for paragraph in paragraphs
                if paragraph.pos - 1 <= span.start < span.end
                <= paragraph.pos - 1 + len(paragraph.text)
            ]
            # Overlapping chunks are not a basis for guessing the source number.
            if len(containing) != 1:
                continue
            paragraph = containing[0]
            key = (-len(matched[source.id]), source.citation or "", source.id,
                   paragraph.paragraph_start, citation.id)
            target = ids[citation.id]
            if target in choices and choices[target][0] <= key:
                continue
            choices[target] = (key, paragraph.text, {
                "source_case_id": source.id,
                "source_citation": source.citation,
                "paragraph_number": paragraph.paragraph_start,
                "citation_row_id": citation.id,
                "matched_tags": sorted(matched[source.id]),
                "matched_tag_count": len(matched[source.id]),
                "basis": "Distinct matched V3 tags of the citing source decision "
                         "(decision-level, not paragraph tag evidence or legal "
                         "treatment). Ties: source citation label, source case ID, "
                         "paragraph number, citation row ID. Only verified stored "
                         "citation spans in uniquely located numbered source "
                         "paragraphs are eligible.",
            })
    for target in targets:
        choice = choices.get(target["case_id"])
        target["excerpt"] = choice[1] if choice else None
        target["excerpt_source"] = choice[2] if choice else None
    return checked, partial


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
            "paragraphs_per_decision": PARAGRAPHS_PER_DECISION,
            "paragraph_row_budget": PARAGRAPHS_TOTAL,
            "paragraph_text_character_budget": TEXT_CHARS,
            "paragraph_rows_checked": 0,
            "note": "Bounded stored-tag and resolved-citation search, not exhaustive. "
                    "Tags match citing decisions, not legal treatment. Statutes are "
                    "extracted separately and do not affect ranking. Excerpts are "
                    "verified numbered citing-source paragraphs, not authority "
                    "headers; unavailable or ambiguous evidence is omitted.",
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
        select(Case.id, Case.citation, Case.metadata_json).where(
            Case.id.in_(ids[:CITING_DECISIONS]), *_canonical()
        ).order_by(Case.id).limit(CITING_DECISIONS)
    )) if ids else []
    candidates = {}
    citation_ids = {}
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
            citation_ids.setdefault(source.id, {})[row.id] = row.target_case_id
    target_ids = sorted(candidates)
    partial |= len(target_ids) > AUTHORITIES
    targets = list(db.execute(
        select(Case.id, Case.citation, Case.court, Case.date)
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
    checked, excerpts_partial = _source_excerpts(
        db, payload["authorities"], sources, matched, citation_ids)
    partial |= excerpts_partial
    payload["coverage"]["paragraph_rows_checked"] = checked
    payload["coverage"]["partial"] = bool(partial)
    payload["coverage"]["matching_citing_decisions_checked"] = len(sources)
    if not ranked:
        payload["message"] = (
            "No resolved canonical authorities found within the posting budgets. "
            "Try another legal issue; this is not proof that no precedent exists."
        )
    return payload
