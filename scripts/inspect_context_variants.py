from __future__ import annotations

import argparse
import json
import uuid
from collections import Counter
from hashlib import sha256

from sqlalchemy import select

from backend.contextual_authority import ChunkInput, build_context_units
from backend.contextual_authority.models import CitationInput
from backend.database import CaseChunk, Citation, SessionLocal


def _cohort_hash(case_ids: list[int]) -> str:
    return sha256(",".join(str(case_id) for case_id in sorted(case_ids)).encode("utf-8")).hexdigest()


def inspect_case(session, case_id: int, chunk_set: str, methods: tuple[str, ...]) -> dict[str, object]:
    chunks = session.scalars(
        select(CaseChunk)
        .where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == chunk_set)
        .order_by(CaseChunk.chunk_index, CaseChunk.id)
    ).all()
    citations = session.scalars(
        select(Citation).where(Citation.source_case_id == case_id, Citation.chunk_id.is_not(None))
    ).all()
    chunk_inputs = [
        ChunkInput(
            case_id=chunk.case_id,
            chunk_id=chunk.id,
            ordinal=chunk.chunk_index,
            text=chunk.text,
            chunk_set=chunk.chunk_set,
        )
        for chunk in chunks
    ]
    citation_inputs = [
        CitationInput(citation.id, citation.chunk_id, citation.offset_start, citation.offset_end)
        for citation in citations
    ]
    units = build_context_units(chunk_inputs, citation_inputs, methods=methods)
    checked_segments = 0
    for unit in units:
        chunk_by_id = {chunk.chunk_id: chunk for chunk in chunk_inputs}
        for segment in unit.segments:
            source = chunk_by_id[segment.chunk_id].text[segment.start_offset : segment.end_offset]
            if sha256(source.encode("utf-8")).hexdigest() != segment.text_sha256:
                raise ValueError(f"segment hash mismatch for case {case_id}, chunk {segment.chunk_id}")
            checked_segments += 1
    return {
        "case_id": case_id,
        "chunk_count": len(chunk_inputs),
        "citation_count": len(citation_inputs),
        "unit_count": len(units),
        "segment_count": checked_segments,
        "methods": dict(Counter(unit.method for unit in units)),
        "citation_memberships": sum(len(unit.citation_ids) for unit in units),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect deterministic contextual authority variants without database writes.")
    parser.add_argument("--case-id", type=int, action="append", dest="case_ids", help="Specific case ID; repeat for a bounded cohort.")
    parser.add_argument("--limit", type=int, default=1, help="Maximum cases when --case-id is omitted (default: 1).")
    parser.add_argument("--chunk-set", default="heading_chunks")
    parser.add_argument("--method", action="append", dest="methods", help="Variant method; repeat to restrict methods.")
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 100:
        parser.error("--limit must be between 1 and 100")
    methods = tuple(args.methods or ("sentence_v1", "paragraph_v1", "window_p1", "citation_burst_v1"))
    with SessionLocal() as session:
        case_ids = sorted(set(args.case_ids or []))
        if not case_ids:
            case_ids = list(
                session.scalars(
                    select(CaseChunk.case_id)
                    .where(CaseChunk.chunk_set == args.chunk_set)
                    .distinct()
                    .order_by(CaseChunk.case_id)
                    .limit(args.limit)
                )
            )
        if len(case_ids) > args.limit:
            parser.error("explicit --case-id count cannot exceed --limit")
        results = [inspect_case(session, case_id, args.chunk_set, methods) for case_id in case_ids]
    print(json.dumps({
        "status": "dry_run",
        "snapshot_id": str(uuid.uuid4()),
        "chunk_set": args.chunk_set,
        "methods": methods,
        "cohort_hash": _cohort_hash(case_ids),
        "canonical_writes": 0,
        "contextual_writes": 0,
        "cases": results,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
