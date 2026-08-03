"""Generate resumable local BGE-M3 embeddings for existing case chunks."""

from __future__ import annotations

import argparse
import csv
import logging
import os
from collections.abc import Sequence
from pathlib import Path

from sqlalchemy import exists, select
from sqlalchemy.orm import Session

from backend.database import Case, CaseChunk, CaseChunkEmbedding, SessionLocal
from backend.embedding_providers import (
    DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    SentenceTransformerEmbeddingProvider,
)

logger = logging.getLogger(__name__)


def encode_chunk_batch(
    chunks: Sequence[CaseChunk],
    provider: SentenceTransformerEmbeddingProvider,
) -> list[CaseChunkEmbedding]:
    vectors = provider.embed_documents([chunk.text for chunk in chunks])
    return [
        CaseChunkEmbedding(
            chunk_id=chunk.id,
            model_name=provider.model_name,
            dimensions=provider.dimensions,
            embedding=vector,
        )
        for chunk, vector in zip(chunks, vectors, strict=True)
    ]


def pending_chunk_query(
    model_name: str,
    *,
    last_chunk_id: int = 0,
    court: str | None = None,
    source_type: str | None = None,
    case_ids: set[int] | None = None,
):
    already_embedded = exists(
        select(CaseChunkEmbedding.id).where(
            CaseChunkEmbedding.chunk_id == CaseChunk.id,
            CaseChunkEmbedding.model_name == model_name,
        )
    )
    statement = (
        select(CaseChunk)
        .join(Case, Case.id == CaseChunk.case_id)
        .where(CaseChunk.id > last_chunk_id, ~already_embedded)
        .order_by(CaseChunk.id)
    )
    if court:
        statement = statement.where(Case.court == court)
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    if case_ids:
        statement = statement.where(Case.id.in_(sorted(case_ids)))
    return statement


def load_case_ids_from_csv(path: str | Path) -> set[int]:
    case_ids: set[int] = set()
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in ("local_case_id", "case_id", "id"):
                value = (row.get(key) or "").strip()
                if value.isdigit():
                    case_ids.add(int(value))
                    break
    return case_ids


def embed_pending_chunks(
    db: Session,
    provider: SentenceTransformerEmbeddingProvider,
    *,
    batch_size: int = 4,
    limit: int | None = None,
    court: str | None = None,
    source_type: str | None = None,
    case_ids: set[int] | None = None,
) -> int:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if limit is not None and limit < 1:
        raise ValueError("limit must be at least 1")

    embedded = 0
    last_chunk_id = 0
    while limit is None or embedded < limit:
        current_batch_size = min(batch_size, limit - embedded) if limit else batch_size
        chunks = db.scalars(
            pending_chunk_query(
                provider.model_name,
                last_chunk_id=last_chunk_id,
                court=court,
                source_type=source_type,
                case_ids=case_ids,
            ).limit(current_batch_size)
        ).all()
        if not chunks:
            break

        rows = encode_chunk_batch(chunks, provider)
        db.add_all(rows)
        db.commit()
        embedded += len(rows)
        last_chunk_id = chunks[-1].id
        logger.info("Embedded %d chunks with %s", embedded, provider.model_name)

    return embedded


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model",
        default=os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL),
    )
    parser.add_argument("--dimensions", type=int, default=DEFAULT_LOCAL_EMBEDDING_DIMENSIONS)
    parser.add_argument("--device", default=os.getenv("LOCAL_EMBEDDING_DEVICE", "cpu"))
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--court", default=None)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--case-ids-csv", default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    case_ids = load_case_ids_from_csv(args.case_ids_csv) if args.case_ids_csv else None
    if args.case_ids_csv:
        logger.info("Loaded %d scoped case IDs from %s", len(case_ids or set()), args.case_ids_csv)

    with SessionLocal() as db:
        if args.dry_run:
            pending = db.scalars(
                pending_chunk_query(
                    args.model,
                    court=args.court,
                    source_type=args.source_type,
                    case_ids=case_ids,
                ).limit(args.limit or 10)
            ).all()
            print(f"pending_sample={len(pending)} model={args.model} dimensions={args.dimensions}")
            return

        provider = SentenceTransformerEmbeddingProvider(
            args.model,
            dimensions=args.dimensions,
            device=args.device,
        )
        count = embed_pending_chunks(
            db,
            provider,
            batch_size=args.batch_size,
            limit=args.limit,
            court=args.court,
            source_type=args.source_type,
            case_ids=case_ids,
        )
        print(f"embedded={count} model={args.model}")


if __name__ == "__main__":
    main()
