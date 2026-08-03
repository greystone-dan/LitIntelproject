"""Create resumable text chunks for canonical cases without embedding calls."""

from __future__ import annotations

import argparse
import logging
import sys
from hashlib import sha256
from pathlib import Path

from sqlalchemy import exists, func, or_, select
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseChunk, SessionLocal

CHUNK_CHARS = 6000
OVERLAP_CHARS = 600

logger = logging.getLogger(__name__)


def split_text(
    text: str,
    *,
    chunk_chars: int = CHUNK_CHARS,
    overlap_chars: int = OVERLAP_CHARS,
) -> list[str]:
    if chunk_chars < 1:
        raise ValueError("chunk_chars must be at least 1")
    if overlap_chars < 0 or overlap_chars >= chunk_chars:
        raise ValueError("overlap_chars must be between 0 and chunk_chars - 1")
    if not text.strip():
        return []

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_chars, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap_chars
    return chunks


def case_text(case: Case) -> str:
    full_text = case.full_text or ""
    if full_text.strip():
        return full_text
    return case.summary or ""


def build_case_chunks(case: Case) -> list[CaseChunk]:
    return [
        CaseChunk(
            case_id=case.id,
            chunk_index=index,
            text=chunk_text,
            text_hash=sha256(chunk_text.encode("utf-8")).hexdigest(),
            token_estimate=max(1, len(chunk_text) // 4),
        )
        for index, chunk_text in enumerate(split_text(case_text(case)))
    ]


def pending_case_query(
    *,
    last_case_id: int = 0,
    court: str | None = None,
    source_type: str | None = None,
):
    already_chunked = exists(select(CaseChunk.id).where(CaseChunk.case_id == Case.id))
    has_text = or_(
        func.length(func.trim(func.coalesce(Case.full_text, ""))) > 0,
        func.length(func.trim(func.coalesce(Case.summary, ""))) > 0,
    )
    statement = (
        select(Case)
        .where(Case.id > last_case_id, ~already_chunked, has_text)
        .order_by(Case.id)
    )
    if court:
        statement = statement.where(Case.court == court)
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    return statement


def chunk_pending_cases(
    db: Session,
    *,
    batch_size: int = 50,
    limit: int | None = None,
    court: str | None = None,
    source_type: str | None = None,
) -> tuple[int, int]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")

    cases_chunked = 0
    chunks_created = 0
    last_case_id = 0
    while limit is None or cases_chunked < limit:
        current_batch_size = min(batch_size, limit - cases_chunked) if limit else batch_size
        cases = db.scalars(
            pending_case_query(
                last_case_id=last_case_id,
                court=court,
                source_type=source_type,
            ).limit(current_batch_size)
        ).all()
        if not cases:
            break

        batch_chunks: list[CaseChunk] = []
        for case in cases:
            batch_chunks.extend(build_case_chunks(case))
        db.add_all(batch_chunks)
        db.commit()

        cases_chunked += len(cases)
        chunks_created += len(batch_chunks)
        last_case_id = cases[-1].id
        logger.info("Chunked %d cases into %d chunks", cases_chunked, chunks_created)

    return cases_chunked, chunks_created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--court", default=None)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with SessionLocal() as db:
        if args.dry_run:
            pending = db.scalars(
                pending_case_query(court=args.court, source_type=args.source_type).limit(
                    args.limit or 10
                )
            ).all()
            estimated_chunks = sum(len(split_text(case_text(case))) for case in pending)
            print(f"pending_sample={len(pending)} estimated_chunks={estimated_chunks}")
            return

        cases_chunked, chunks_created = chunk_pending_cases(
            db,
            batch_size=args.batch_size,
            limit=args.limit,
            court=args.court,
            source_type=args.source_type,
        )
        print(f"cases_chunked={cases_chunked} chunks_created={chunks_created}")


if __name__ == "__main__":
    main()