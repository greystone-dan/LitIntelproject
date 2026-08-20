"""Extract IRPA and IRPR references into the separate statute-reference layer."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_statute_reference_matches
from backend.database import Case, CaseChunk, SessionLocal, StatuteReference

IRPA_IRPR_RE = re.compile(
    r"\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=250, help="Cases per transaction")
    parser.add_argument("--start-after-id", type=int, default=0, help="Resume after this case ID")
    parser.add_argument("--dry-run", action="store_true", help="Count matches without writing")
    return parser.parse_args()


def is_irpa_irpr(reference_text: str | None, normalized_reference: str | None) -> bool:
    return bool(IRPA_IRPR_RE.search(reference_text or "") or IRPA_IRPR_RE.search(normalized_reference or ""))


def extract_case_references(case: Case, chunks: list[CaseChunk]) -> list[StatuteReference]:
    preferred = [chunk for chunk_set in ("paragraph", "section", "legacy") for chunk in chunks if chunk.chunk_set == chunk_set]
    selected_chunks = preferred if preferred else chunks
    references: list[StatuteReference] = []
    seen: set[tuple[int | None, int, int, str]] = set()
    if selected_chunks:
        for chunk in selected_chunks:
            for raw in extract_statute_reference_matches(chunk.text):
                if not is_irpa_irpr(raw.citation_text, raw.normalized_citation):
                    continue
                key = (chunk.id, raw.offset_start, raw.offset_end, raw.normalized_citation)
                if key in seen:
                    continue
                seen.add(key)
                references.append(StatuteReference(source_case_id=case.id, chunk_id=chunk.id, offset_start=raw.offset_start, offset_end=raw.offset_end, reference_text=raw.citation_text, normalized_reference=raw.normalized_citation, reference_kind=raw.kind))
    else:
        for raw in extract_statute_reference_matches(case.full_text or case.summary):
            if is_irpa_irpr(raw.citation_text, raw.normalized_citation):
                references.append(StatuteReference(source_case_id=case.id, chunk_id=None, offset_start=raw.offset_start, offset_end=raw.offset_end, reference_text=raw.citation_text, normalized_reference=raw.normalized_citation, reference_kind=raw.kind))
    return references


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")
    total = 0
    processed = 0
    with SessionLocal() as session:
        last_id = args.start_after_id
        while True:
            cases = list(
                session.scalars(
                    select(Case)
                    .where(Case.id > last_id)
                    .order_by(Case.id)
                    .limit(args.batch_size)
                )
            )
            if not cases:
                break
            case_ids = [case.id for case in cases]
            chunks = list(
                session.scalars(
                    select(CaseChunk)
                    .where(CaseChunk.case_id.in_(case_ids))
                    .order_by(CaseChunk.case_id, CaseChunk.chunk_index)
                )
            )
            chunks_by_case: dict[int, list[CaseChunk]] = {}
            for chunk in chunks:
                chunks_by_case.setdefault(chunk.case_id, []).append(chunk)
            batch_references: list[StatuteReference] = []
            for case in cases:
                batch_references.extend(extract_case_references(case, chunks_by_case.get(case.id, [])))
            total += len(batch_references)
            processed += len(cases)
            if not args.dry_run:
                session.add_all(batch_references)
                session.commit()
            last_id = cases[-1].id
            print(f"processed_cases={processed} references_found={total} last_case_id={last_id}", flush=True)
    print(f"done processed_cases={processed} irpa_irpr_references={total} dry_run={args.dry_run}", flush=True)


if __name__ == "__main__":
    main()
