"""Generate resumable OpenAI embeddings for existing case chunks with a hard budget cap."""

from __future__ import annotations

import argparse
import logging
import os
import random
import sys
import time
from collections.abc import Sequence
from dataclasses import dataclass

from openai import APIConnectionError, APITimeoutError, InternalServerError, OpenAI, RateLimitError
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import Case, CaseChunk, SessionLocal

logger = logging.getLogger(__name__)

DEFAULT_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
DEFAULT_COST_PER_1M = float(os.getenv("OPENAI_EMBED_COST_PER_1M", "0.02"))
DEFAULT_BATCH_SIZE = 100
DEFAULT_MAX_RETRIES = 12
DEFAULT_RETRY_BASE_SECONDS = 2.0


@dataclass(frozen=True)
class BudgetState:
    spent_usd: float
    budget_usd: float


def estimate_cost_usd(token_count: int, cost_per_1m: float) -> float:
    if token_count <= 0:
        return 0.0
    return (token_count / 1_000_000.0) * cost_per_1m


def fit_batch_to_budget(
    chunks: Sequence[CaseChunk],
    budget: BudgetState,
    cost_per_1m: float,
) -> list[CaseChunk]:
    selected: list[CaseChunk] = []
    running_tokens = 0
    for chunk in chunks:
        tokens = int(getattr(chunk, "token_estimate", 0) or 0)
        projected_cost = estimate_cost_usd(running_tokens + tokens, cost_per_1m)
        if budget.spent_usd + projected_cost > budget.budget_usd and selected:
            break
        if budget.spent_usd + projected_cost > budget.budget_usd and not selected:
            return []
        selected.append(chunk)
        running_tokens += tokens
    return selected


def pending_chunk_query(*, last_chunk_id: int = 0, source_type: str | None = None):
    statement = (
        select(CaseChunk)
        .join(Case, Case.id == CaseChunk.case_id)
        .where(CaseChunk.id > last_chunk_id, CaseChunk.embedding.is_(None))
        .order_by(CaseChunk.id)
    )
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    return statement


def _create_embeddings_with_retry(
    client: OpenAI,
    *,
    model: str,
    input_texts: list[str],
    max_retries: int,
    retry_base_seconds: float,
):
    if max_retries < 1:
        raise ValueError("max_retries must be at least 1")
    if retry_base_seconds <= 0:
        raise ValueError("retry_base_seconds must be positive")

    delay = retry_base_seconds
    for attempt in range(1, max_retries + 1):
        try:
            return client.embeddings.create(model=model, input=input_texts)
        except (APIConnectionError, APITimeoutError, InternalServerError, RateLimitError) as exc:
            if attempt >= max_retries:
                raise
            jitter = random.uniform(0.0, min(1.0, delay * 0.25))
            sleep_seconds = min(60.0, delay + jitter)
            logger.warning(
                "Embedding request failed (%s), retry %d/%d in %.1fs",
                type(exc).__name__,
                attempt,
                max_retries,
                sleep_seconds,
            )
            time.sleep(sleep_seconds)
            delay = min(60.0, delay * 1.8)


def embed_pending_chunks(
    db: Session,
    client: OpenAI,
    *,
    model: str,
    budget_usd: float,
    cost_per_1m: float,
    batch_size: int,
    max_retries: int,
    retry_base_seconds: float,
    source_type: str | None = None,
    max_chunks: int | None = None,
) -> tuple[int, int, float]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    if budget_usd <= 0:
        raise ValueError("budget_usd must be positive")

    embedded = 0
    embedded_tokens = 0
    spent_usd = 0.0
    last_chunk_id = 0

    while max_chunks is None or embedded < max_chunks:
        target_batch_size = min(batch_size, max_chunks - embedded) if max_chunks else batch_size
        candidates = db.scalars(
            pending_chunk_query(last_chunk_id=last_chunk_id, source_type=source_type).limit(target_batch_size)
        ).all()
        if not candidates:
            break

        budgeted = fit_batch_to_budget(candidates, BudgetState(spent_usd, budget_usd), cost_per_1m)
        if not budgeted:
            logger.info("Budget cap reached: spent=$%.4f cap=$%.4f", spent_usd, budget_usd)
            break

        response = _create_embeddings_with_retry(
            client,
            model=model,
            input_texts=[chunk.text for chunk in budgeted],
            max_retries=max_retries,
            retry_base_seconds=retry_base_seconds,
        )
        for chunk, item in zip(budgeted, response.data, strict=True):
            chunk.embedding = item.embedding
            chunk.embedding_model = model
            embedded += 1
            tokens = int(chunk.token_estimate or 0)
            embedded_tokens += tokens
            spent_usd += estimate_cost_usd(tokens, cost_per_1m)
            last_chunk_id = chunk.id

        touched_case_ids = sorted({int(chunk.case_id) for chunk in budgeted})
        cases = list(db.scalars(select(Case).where(Case.id.in_(touched_case_ids))))
        for case in cases:
            if case.processing_status != "embedded":
                case.processing_status = "embedded"

        db.commit()
        logger.info(
            "Embedded chunks=%d tokens=%d est_spend=$%.4f/%0.4f model=%s",
            embedded,
            embedded_tokens,
            spent_usd,
            budget_usd,
            model,
        )

    return embedded, embedded_tokens, spent_usd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--budget-usd", type=float, default=25.0)
    parser.add_argument("--cost-per-1m", type=float, default=DEFAULT_COST_PER_1M)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    parser.add_argument("--retry-base-seconds", type=float, default=DEFAULT_RETRY_BASE_SECONDS)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--max-chunks", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s", stream=sys.stdout)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        raise SystemExit("OPENAI_API_KEY is required")

    with SessionLocal() as db:
        if args.dry_run:
            sample = db.scalars(
                pending_chunk_query(source_type=args.source_type).limit(args.max_chunks or 20)
            ).all()
            tokens = sum(int(chunk.token_estimate or 0) for chunk in sample)
            estimated = estimate_cost_usd(tokens, args.cost_per_1m)
            print(
                f"pending_sample={len(sample)} sample_tokens={tokens} "
                f"sample_est_cost=${estimated:.4f} model={args.model}"
            )
            return

        client = OpenAI(api_key=api_key)
        embedded, embedded_tokens, spent = embed_pending_chunks(
            db,
            client,
            model=args.model,
            budget_usd=args.budget_usd,
            cost_per_1m=args.cost_per_1m,
            batch_size=args.batch_size,
            max_retries=args.max_retries,
            retry_base_seconds=args.retry_base_seconds,
            source_type=args.source_type,
            max_chunks=args.max_chunks,
        )
        print(
            f"embedded_chunks={embedded} embedded_tokens={embedded_tokens} "
            f"estimated_spend_usd={spent:.4f} budget_usd={args.budget_usd:.4f} model={args.model}"
        )


if __name__ == "__main__":
    main()
