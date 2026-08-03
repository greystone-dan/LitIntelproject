"""Generate resumable local BGE-M3 embeddings for existing case chunks."""

from __future__ import annotations

import argparse
import logging
import os
from collections.abc import Sequence

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
    return statement


def embed_pending_chunks(
    db: Session,
    provider: SentenceTransformerEmbeddingProvider,
    *,
    batch_size: int = 4,
    limit: int | None = None,
    court: str | None = None,
    source_type: str | None = None,
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
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with SessionLocal() as db:
        if args.dry_run:
            pending = db.scalars(
                pending_chunk_query(
                    args.model,
                    court=args.court,
                    source_type=args.source_type,
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
        )
        print(f"embedded={count} model={args.model}")


if __name__ == "__main__":
    main()
