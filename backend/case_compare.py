"""Read-only resolution and comparison helpers for the case comparison page."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .case_comparison import fetch_case_comparison
from .citations import _citation_variants, build_local_case_resolution_index
from .database import Case, CaseChunk, Citation

MAX_CASE_INPUT_CHARS = 512


def resolve_case_input(db: Session, value: str) -> int | None:
    """Resolve a stored ID/citation; reject input over 512 chars before parsing."""
    if len(value) > MAX_CASE_INPUT_CHARS:
        return None
    value = value.strip()
    if not value:
        return None
    if value.isascii() and value.isdigit():
        case_id = int(value)
        return case_id if db.scalar(select(Case.id).where(Case.id == case_id)) is not None else None

    variants = _citation_variants(value)
    if not variants:
        return None
    index = build_local_case_resolution_index(db)
    matches = {index[variant] for variant in variants if variant in index}
    # An ambiguous key or conflicting parallel citations must not guess.
    if None in matches or len(matches) != 1:
        return None
    return next(iter(matches))


def compare_case_inputs(db: Session, a: str, b: str) -> dict[str, Any]:
    """Resolve both user inputs, compare stored data, and expose recorded cross-citations."""
    case_a = resolve_case_input(db, a)
    case_b = resolve_case_input(db, b)
    if case_a is None or case_b is None:
        return {
            "status": "unknown_case",
            "unknown_inputs": [value for value, case_id in ((a, case_a), (b, case_b)) if case_id is None],
        }
    if case_a == case_b:
        return {"status": "same_case", "case_id": case_a}

    result = fetch_case_comparison(db, case_a, case_b)
    if result["status"] != "ok":
        return result

    occurrences: dict[str, list[dict[str, Any]]] = {"a_cites_b": [], "b_cites_a": []}
    authority_pinpoints: dict[str, dict[int, set[int]]] = {"a": {}, "b": {}}
    chunk = CaseChunk.__table__.alias("citation_source_chunk")
    rows = db.execute(
        select(
            Citation, chunk.c.paragraph_start, chunk.c.paragraph_end,
        )
        .outerjoin(chunk, chunk.c.id == Citation.chunk_id)
        .where(
            Citation.source_case_id.in_((case_a, case_b)),
            Citation.target_case_id.is_not(None),
            Citation.citation_kind.in_(("neutral", "case", "case_short", "case_name")),
        )
        .order_by(Citation.id)
    )
    for citation, source_start, source_end in rows:
        side = "a" if citation.source_case_id == case_a else "b"
        # Citation.target_paragraph is the cited decision's pinpoint; source
        # occurrence paragraphs come only from the source chunk below.
        if citation.target_paragraph is not None:
            authority_pinpoints[side].setdefault(citation.target_case_id, set()).add(citation.target_paragraph)
        other_case = case_b if side == "a" else case_a
        # Do not infer a comparison edge from citation text: require the stored
        # resolved target ID to be exactly the other compared canonical case.
        if citation.target_case_id == other_case:
            direction = "a_cites_b" if side == "a" else "b_cites_a"
            occurrences[direction].append({
                "citation_id": citation.id,
                "citation_text": citation.citation_text,
                "target_paragraph": citation.target_paragraph,
                "source_paragraph_start": source_start,
                "source_paragraph_end": source_end,
                "source": "stored citation and source chunk",
                "verification": "unverified",
            })
    for item in result["authorities"]["items"]:
        target_id = item.get("target_case_id")
        item["pinpoints_by_side"] = {
            side: sorted(authority_pinpoints[side].get(target_id, set()))
            for side in ("a", "b")
        }
    result["cross_citations"] = {
        direction: {"cites": bool(items), "occurrences": items}
        for direction, items in occurrences.items()
    }
    result["semantics"]["citation_pinpoints"] = (
        "Citation.target_paragraph is the cited decision's paragraph pinpoint; "
        "source occurrence paragraphs are taken from the citing decision's stored source chunk."
    )
    result["semantics"]["cross_citations"] = (
        "A-to-B/B-to-A is reported only when stored Citation.target_case_id exactly "
        "matches the other compared case ID."
    )
    result["fact_provenance"] = {
        field: {
            "source": f"cases.{column}",
            "verification": "unverified",
        }
        for field, column in (
            ("citation", "citation"), ("court", "court"), ("date", "date"),
        )
    }
    for case in result["cases"].values():
        case["fact_provenance"] = {
            field: dict(provenance)
            for field, provenance in result["fact_provenance"].items()
        }
        case["fact_provenance"]["judge"] = {
            "source": case["judge_source"],
            "verification": "unverified",
        }
        case["judge_verification"] = "unverified"
        case["outcome"]["verification"] = "unverified"
    return result
