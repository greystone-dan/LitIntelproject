#!/usr/bin/env python3
"""
Populate case_chunk_embeddings table with local sentence-transformer embeddings.

Run this on the PC where the database is accessible.
Generates embeddings for all case chunks using BAAI/bge-m3 (1024 dims).

Usage:
    python3 scripts/populate_embeddings.py [--model MODEL_NAME] [--batch-size N] [--skip-existing]
"""

import os
import sys
from pathlib import Path
from typing import Generator

# Add backend to path
backend_path = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db, CaseChunk, CaseChunkEmbedding
from embedding_providers import SentenceTransformerEmbeddingProvider

# Load environment
project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env", override=True)

DEFAULT_MODEL = "BAAI/bge-m3"
DEFAULT_DIMENSIONS = 1024
DEFAULT_BATCH_SIZE = 32


def get_embedding_provider(model_name: str, dimensions: int) -> SentenceTransformerEmbeddingProvider:
    """Initialize the embedding provider."""
    return SentenceTransformerEmbeddingProvider(
        model_name=model_name,
        dimensions=dimensions,
        device=os.getenv("LOCAL_EMBEDDING_DEVICE", "cpu"),
    )


def get_chunks_needing_embeddings(
    session: Session, model_name: str, skip_existing: bool = False
) -> Generator[CaseChunk, None, None]:
    """Yield chunks that need embeddings for the given model."""
    if skip_existing:
        # Only get chunks without embeddings for this model
        subquery = select(CaseChunkEmbedding.chunk_id).where(
            CaseChunkEmbedding.model_name == model_name
        )
        query = select(CaseChunk).where(~CaseChunk.id.in_(subquery))
    else:
        # Get all chunks
        query = select(CaseChunk)

    for chunk in session.stream(query):
        yield chunk[0]  # Unpack tuple from stream


def populate_embeddings(
    model_name: str = DEFAULT_MODEL,
    dimensions: int = DEFAULT_DIMENSIONS,
    batch_size: int = DEFAULT_BATCH_SIZE,
    skip_existing: bool = False,
) -> None:
    """Generate and store embeddings for all case chunks."""

    print(f"Connecting to database...")
    session_generator = get_db()
    session = next(session_generator)

    try:
        # Count total chunks needing embeddings BEFORE loading model
        print(f"Scanning database for chunks needing embeddings...")
        chunks_iter = get_chunks_needing_embeddings(session, model_name, skip_existing)
        chunks_list = list(chunks_iter)
        total = len(chunks_list)

        if total == 0:
            print("No chunks need embeddings. Use --skip-existing=false to re-embed all.")
            return

        # Estimate time BEFORE loading the expensive model
        print(f"\n{'='*70}")
        print(f"CHUNK COUNT & TIME ESTIMATE")
        print(f"{'='*70}")
        print(f"Total chunks to embed: {total:,}")

        num_batches = (total + batch_size - 1) // batch_size
        ms_per_batch = 125  # Typical: 100-150ms per batch on Windows CPU
        estimated_seconds = (num_batches * ms_per_batch) / 1000
        estimated_hours = estimated_seconds / 3600

        print(f"Batches: {num_batches:,} × {batch_size} chunks")
        print(f"Estimated time: {estimated_hours:.1f}–{estimated_hours * 1.2:.1f} hours on Windows CPU")
        print(f"  - With GPU (CUDA): {estimated_hours / 4:.1f} hours")
        print(f"  - Resumable: Use --skip-existing to continue if interrupted")
        print(f"{'='*70}\n")

        print(f"Initializing embedding model: {model_name} ({dimensions} dims)...")
        provider = get_embedding_provider(model_name, dimensions)

        # Process in batches
        for batch_start in range(0, total, batch_size):
            batch_end = min(batch_start + batch_size, total)
            batch = chunks_list[batch_start:batch_end]

            # Get text to embed
            texts = [chunk.text for chunk in batch]

            # Generate embeddings
            print(
                f"Embedding batch {batch_start // batch_size + 1}/{(total + batch_size - 1) // batch_size} "
                f"(chunks {batch_start}-{batch_end})...",
                end="",
                flush=True,
            )
            embeddings = provider.embed_documents(texts)

            # Store in database
            for chunk, embedding in zip(batch, embeddings):
                existing = session.query(CaseChunkEmbedding).filter(
                    CaseChunkEmbedding.chunk_id == chunk.id,
                    CaseChunkEmbedding.model_name == model_name,
                ).first()

                if existing:
                    existing.embedding = embedding
                    existing.dimensions = dimensions
                else:
                    new_embedding = CaseChunkEmbedding(
                        chunk_id=chunk.id,
                        model_name=model_name,
                        dimensions=dimensions,
                        embedding=embedding,
                    )
                    session.add(new_embedding)

            session.commit()
            print(" ✓")

        print(f"\n✓ Successfully embedded {total} chunks")

    except Exception as e:
        session.rollback()
        print(f"\n✗ Error: {e}", file=sys.stderr)
        raise
    finally:
        session.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Populate case_chunk_embeddings with local sentence-transformer embeddings",
        epilog="""
SCALE: ~150K paragraphs from 61K decisions. Supports resumable runs with --skip-existing.

PERFORMANCE ESTIMATES (Windows CPU):
  • First run: 2-4 hours on CPU (100-150ms per 32-chunk batch)
  • If GPU available: <1 hour with CUDA
  • Memory: ~1GB for model + batch buffer
  • Resumable: Use --skip-existing to continue interrupted runs

USAGE:
  python3 scripts\\populate_embeddings.py                   # Full run
  python3 scripts\\populate_embeddings.py --skip-existing   # Resume (skip completed)
  python3 scripts\\populate_embeddings.py --batch-size=64   # Larger batches (faster)
        """,
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Embedding model name (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--dimensions",
        type=int,
        default=DEFAULT_DIMENSIONS,
        help=f"Expected embedding dimensions (default: {DEFAULT_DIMENSIONS})",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Batch size for processing (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip chunks that already have embeddings for this model",
    )

    args = parser.parse_args()

    populate_embeddings(
        model_name=args.model,
        dimensions=args.dimensions,
        batch_size=args.batch_size,
        skip_existing=args.skip_existing,
    )


if __name__ == "__main__":
    main()
