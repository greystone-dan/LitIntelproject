"""Quick semantic search tester over chunk embeddings.

Usage:
    python -m scripts.quick_search_engine "non-refoulement risk evidence"
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass

from openai import OpenAI
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import Case, CaseChunk, SessionLocal

EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


@dataclass
class ResultRow:
    case_id: int
    title: str
    citation: str | None
    court: str
    chunk_index: int
    similarity: float
    chunk_text: str


def _embed_query(query: str) -> list[float]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is required")

    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=query)
    return response.data[0].embedding


def search_semantic(db: Session, query: str, limit: int) -> list[ResultRow]:
    query_vector = _embed_query(query)
    distance = CaseChunk.embedding.cosine_distance(query_vector).label("distance")

    statement = (
        select(Case, CaseChunk, distance)
        .join(CaseChunk, CaseChunk.case_id == Case.id)
        .where(CaseChunk.embedding.is_not(None))
        .order_by(distance)
        .limit(limit)
    )

    rows = list(db.execute(statement))
    results: list[ResultRow] = []
    for case, chunk, distance_value in rows:
        similarity = max(0.0, min(1.0, 1.0 - float(distance_value)))
        results.append(
            ResultRow(
                case_id=case.id,
                title=case.title,
                citation=case.citation,
                court=case.court,
                chunk_index=chunk.chunk_index,
                similarity=similarity,
                chunk_text=chunk.text,
            )
        )
    return results


def _clip_text(text: str, length: int = 240) -> str:
    compact = " ".join(text.split())
    if len(compact) <= length:
        return compact
    return f"{compact[: length - 1]}..."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural-language search query")
    parser.add_argument("--limit", type=int, default=10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    with SessionLocal() as db:
        rows = search_semantic(db, args.query, limit=args.limit)

    if not rows:
        print("No results")
        return

    print(f"model={EMBEDDING_MODEL} query={args.query!r} results={len(rows)}")
    for idx, row in enumerate(rows, start=1):
        print("-" * 90)
        print(
            f"#{idx} score={row.similarity:.4f} case_id={row.case_id} "
            f"chunk={row.chunk_index} court={row.court}"
        )
        if row.citation:
            print(f"citation={row.citation}")
        print(f"title={row.title}")
        print(f"excerpt={_clip_text(row.chunk_text)}")


if __name__ == "__main__":
    main()
