"""Generate resumable OpenAI embeddings for existing case chunks with a hard budget cap."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import math
import os
import sys
import time
import uuid
from collections.abc import Sequence
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from functools import lru_cache
from pathlib import Path
import re

from openai import APIConnectionError, APITimeoutError, InternalServerError, OpenAI, RateLimitError
from sqlalchemy import String, cast, func, select
from sqlalchemy.orm import Session

try:
    import tiktoken
except ImportError:  # pragma: no cover - the production environment includes tiktoken
    tiktoken = None

from backend.database import Case, CaseChunk, SessionLocal

logger = logging.getLogger(__name__)

DEFAULT_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
DEFAULT_COST_PER_1M = float(os.getenv("OPENAI_EMBED_COST_PER_1M", "0.02"))
DEFAULT_BATCH_SIZE = 100
DEFAULT_MAX_REQUEST_TOKENS = 100000
DEFAULT_MAX_RETRIES = 12
DEFAULT_RETRY_BASE_SECONDS = 2.0
MAX_EMBEDDING_INPUT_TOKENS = 8192


@dataclass(frozen=True)
class BudgetState:
    spent_usd: float
    budget_usd: float


def estimate_cost_usd(token_count: int, cost_per_1m: float) -> float:
    if token_count <= 0:
        return 0.0
    return (token_count / 1_000_000.0) * cost_per_1m


def count_embedding_tokens(text: str, model: str) -> int:
    return len(encode_embedding_input(text, model))


def encode_embedding_input(text: str, model: str) -> list[int]:
    if tiktoken is None:
        raise RuntimeError("tiktoken is required for exact request accounting")
    if model != "text-embedding-3-small":
        raise ValueError("Only text-embedding-3-small (1536 dimensions) is supported")
    return embedding_tokenizer(model).encode(text, disallowed_special=())


@lru_cache(maxsize=1)
def embedding_tokenizer(model: str):
    return tiktoken.encoding_for_model(model)


def split_embedding_tokens(tokens: list[int], limit: int = MAX_EMBEDDING_INPUT_TOKENS) -> list[list[int]]:
    return [tokens[index:index + limit] for index in range(0, len(tokens), limit)] or [[]]


def pool_embedding_vectors(vectors: Sequence[Sequence[float]], weights: Sequence[int] | None = None) -> list[float]:
    if not vectors:
        raise ValueError("Cannot pool an empty embedding vector list")
    if len(vectors) == 1:
        return list(vectors[0])
    weights = list(weights) if weights is not None else [1] * len(vectors)
    if len(weights) != len(vectors) or any(weight <= 0 for weight in weights):
        raise ValueError("Positive token weights are required for every vector")
    total_weight = sum(weights)
    pooled = [sum(vector[index] * weight for vector, weight in zip(vectors, weights)) / total_weight
              for index in range(1536)]
    norm = math.sqrt(sum(value * value for value in pooled))
    if not math.isfinite(norm) or norm == 0:
        raise ValueError("Cannot normalize pooled embedding vector")
    return [value / norm for value in pooled]


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


def pending_chunk_query(
    *,
    last_chunk_id: int = 0,
    source_type: str | None = None,
    case_ids: set[int] | None = None,
    worker_index: int | None = None,
    worker_count: int = 1,
    excluded_chunk_ids: set[int] | None = None,
    paragraph_only: bool = True,
):
    statement = (
        select(CaseChunk)
        .join(Case, Case.id == CaseChunk.case_id)
        .where(CaseChunk.id > last_chunk_id, CaseChunk.embedding.is_(None))
        .order_by(CaseChunk.id)
    )
    if source_type:
        statement = statement.where(Case.source_type == source_type)
    if paragraph_only:
        statement = statement.where(CaseChunk.chunk_set == "paragraph")
    if case_ids:
        statement = statement.where(Case.id.in_(sorted(case_ids)))
    if excluded_chunk_ids:
        statement = statement.where(~CaseChunk.id.in_(sorted(excluded_chunk_ids)))
    if worker_index is not None:
        if worker_count < 1 or not 0 <= worker_index < worker_count:
            raise ValueError("worker_index must be within worker_count")
        statement = statement.where(func.mod(CaseChunk.id, worker_count) == worker_index)
    return statement


def numbered_paragraph_conditions():
    return (
        CaseChunk.chunk_set == "paragraph",
        CaseChunk.paragraph_start > 0,
        CaseChunk.paragraph_start == CaseChunk.paragraph_end,
        CaseChunk.chunk_label == cast(CaseChunk.paragraph_start, String),
    )


def load_case_ids_from_csv(path: str | Path) -> set[int]:
    case_ids: set[int] = set()
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in ("case_id", "id", "local_case_id"):
                value = (row.get(key) or "").strip()
                if value.isdigit():
                    case_ids.add(int(value))
                    break
    if not case_ids:
        raise ValueError(f"No case IDs found in {path}")
    return case_ids


def emit(event: str, **fields) -> None:
    logger.info(json.dumps({"event": event, **fields}, sort_keys=True, allow_nan=False))


def acquire_writer_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+b")
    try:
        if os.name == "nt":
            import msvcrt
            if path.stat().st_size == 0:
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return handle
    except OSError as exc:
        handle.close()
        raise RuntimeError("Another hosted paragraph embedding writer holds the shared lock") from exc


class RequestLedger:
    def __init__(self, path: Path, identity: dict):
        self.path = path
        self.requests: dict[str, dict] = {}
        self.blockers: set[int] = set()
        if path.exists():
            with path.open(encoding="utf-8") as handle:
                records = [json.loads(line) for line in handle]
            if not records or records[0] != {"event": "identity", "identity": identity}:
                raise ValueError("Ledger run identity mismatch")
            for record in records[1:]:
                self._apply(record)
            if any(item["state"] in {"reserved", "usage"} for item in self.requests.values()):
                raise RuntimeError("Unreconciled request reserve/usage: inspect ledger before restart")
            for request_id, item in list(self.requests.items()):
                if item["state"] == "received":
                    self.append("superseded", request_id=request_id)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            self.append("identity", identity=identity)

    def _apply(self, record: dict) -> None:
        event = record["event"]
        if event == "reserve":
            self.requests[record["request_id"]] = {**record, "state": "reserved"}
        elif event == "committed":
            item = self.requests[record["request_id"]]
            committed = set(item.get("committed_chunk_ids", [])) | set(record["chunk_ids"])
            item.update(record, committed_chunk_ids=sorted(committed),
                        state="received" if record.get("pending_chunk_ids") else "committed")
        elif event in {"rejected", "usage", "received", "superseded"}:
            self.requests[record["request_id"]].update(record, state=event)
        elif event == "blocker":
            self.blockers.add(record["chunk_id"])

    def append(self, event: str, **fields) -> None:
        record = {"event": event, **fields}
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(record, sort_keys=True, allow_nan=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        self._apply(record)
        emit(event, **fields)

    @property
    def spent_usd(self) -> float:
        return sum(item["cost_usd"] for item in self.requests.values() if item["state"] != "rejected")

    @property
    def committed_chunks(self) -> int:
        return len({chunk_id for item in self.requests.values()
                    for chunk_id in item.get("committed_chunk_ids", [])})

    @property
    def incomplete(self) -> bool:
        return bool(self.blockers) or any(
            item["state"] in {"reserved", "usage", "received"} for item in self.requests.values()
        )


def header_delay(headers, *, wall_time=time.time) -> float:
    headers = {key.lower(): str(value) for key, value in headers.items()}
    delay = 0.0
    retry_after = headers.get("retry-after")
    if retry_after:
        try:
            delay = max(0.0, float(retry_after))
        except ValueError:
            try:
                delay = max(0.0, parsedate_to_datetime(retry_after).timestamp() - wall_time())
            except (ValueError, TypeError, OverflowError):
                pass
    for resource in ("requests", "tokens"):
        try:
            exhausted = float(headers.get(f"x-ratelimit-remaining-{resource}", "inf")) <= 0
        except ValueError:
            exhausted = False
        reset = headers.get(f"x-ratelimit-reset-{resource}", "")
        if exhausted and re.fullmatch(r"(?:\d+(?:\.\d+)?(?:ms|s|m|h))+", reset):
            seconds = sum(float(amount) * {"ms": .001, "s": 1, "m": 60, "h": 3600}[unit]
                          for amount, unit in re.findall(r"(\d+(?:\.\d+)?)(ms|s|m|h)", reset))
            delay = max(delay, seconds)
    return delay if math.isfinite(delay) else 0.0


class RequestPacer:
    def __init__(self, rpm: float = 0, tpm: float = 0, *, clock=time.monotonic, sleep=time.sleep, wall_time=time.time):
        self.rpm = rpm
        self.tpm = tpm
        self.clock = clock
        self.sleep = sleep
        self.wall_time = wall_time
        self.next_request = 0.0
        self.next_tokens = 0.0
        self.blocked_until = 0.0
        self.slowdown = 1.0

    def wait(self, tokens: int) -> None:
        wait = max(self.next_request, self.next_tokens, self.blocked_until) - self.clock()
        if wait > 0:
            self.sleep(wait)
        now = self.clock()
        self.next_request = now + 60 / self.rpm if self.rpm else now
        self.next_tokens = now + 60 * tokens / self.tpm if self.tpm else now

    def observe(self, headers, *, rate_limited: bool = False) -> float:
        delay = header_delay(headers, wall_time=self.wall_time)
        if rate_limited:
            self.blocked_until = max(self.blocked_until, self.clock() + delay)
        return delay if rate_limited else 0.0


def validate_response(response, count: int) -> dict[int, list[float]]:
    vectors = {}
    if len(response.data) != count:
        raise ValueError("Embedding response count mismatch")
    for item in response.data:
        if type(item.index) is not int or not 0 <= item.index < count or item.index in vectors:
            raise ValueError("Invalid or duplicate embedding response index")
        if len(item.embedding) != 1536 or not all(
            isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
            for value in item.embedding
        ):
            raise ValueError("Invalid embedding vector")
        vectors[item.index] = item.embedding
    return vectors


def request_batch(client, chunks, inputs, *, args, ledger, pacer):
    tokens = sum(map(len, inputs))
    if not inputs or len(inputs) > args.batch_size or tokens > args.max_request_tokens:
        raise ValueError("Request exceeds configured batch bounds")
    if any(not item or len(item) > MAX_EMBEDDING_INPUT_TOKENS for item in inputs):
        raise ValueError("Request exceeds per-input token limit")
    chunk_ids = list(dict.fromkeys(chunk.id for chunk in chunks))
    for attempt in range(1, args.max_retries + 1):
        reserve = estimate_cost_usd(tokens, args.cost_per_1m)
        if ledger.spent_usd + reserve > args.budget_usd:
            raise RuntimeError("Budget exhausted; pending coverage remains incomplete")
        pacer.wait(tokens)
        request_id = uuid.uuid4().hex
        ledger.append("reserve", request_id=request_id, chunk_ids=chunk_ids,
                      tokens=tokens, cost_usd=reserve, attempt=attempt)
        try:
            raw = client.embeddings.with_raw_response.create(model=args.model, input=inputs)
            pacer.observe(raw.headers)
            response = raw.parse()
            usage = response.usage.total_tokens
            if type(usage) is not int or usage < 1:
                raise ValueError("Invalid response token usage; reserve retained")
            ledger.append("usage", request_id=request_id, tokens=usage,
                          cost_usd=estimate_cost_usd(usage, args.cost_per_1m))
            if usage > tokens or ledger.spent_usd > args.budget_usd:
                raise RuntimeError("Response usage exceeds reservation; reconciliation required")
            vectors = validate_response(response, len(inputs))
            ledger.append("received", request_id=request_id)
            return request_id, vectors, usage
        except (APIConnectionError, APITimeoutError, InternalServerError, RateLimitError) as exc:
            headers = getattr(getattr(exc, "response", None), "headers", {})
            limited = isinstance(exc, RateLimitError)
            observed_delay = pacer.observe(headers, rate_limited=limited)
            if limited:
                ledger.append("rejected", request_id=request_id, cost_usd=0.0)
            delay = max(observed_delay, min(60.0, args.retry_base_seconds * 2 ** (attempt - 1)))
            ledger.append("retry", request_id=request_id, error_type=type(exc).__name__,
                          attempt=attempt, delay_seconds=delay, reserve_retained=not limited)
            if attempt == args.max_retries:
                raise
            pacer.blocked_until = max(pacer.blocked_until, pacer.clock() + delay)


def embed_pending_chunks(db: Session, client, *, args, ledger, pacer) -> dict:
    expire_on_commit = getattr(db, "expire_on_commit", True)
    db.expire_on_commit = False
    try:
        return _embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    finally:
        db.expire_on_commit = expire_on_commit


def _embed_pending_chunks(db: Session, client, *, args, ledger, pacer) -> dict:
    started = pacer.clock()
    scanned = 0
    embedded = 0
    last_chunk_id = 0
    states = {}
    open_requests = {}
    request_count = 0
    request_tokens = 0
    request_inputs = 0
    piece_chunks = []
    inputs = []
    tokens = 0

    def commit_batch():
        nonlocal embedded, piece_chunks, inputs, tokens, request_count, request_tokens, request_inputs
        if not inputs:
            return
        request_id, piece_vectors, usage = request_batch(
            client, piece_chunks, inputs, args=args, ledger=ledger, pacer=pacer
        )
        request_count += 1
        request_tokens += tokens
        request_inputs += len(inputs)
        open_requests[request_id] = {chunk.id for chunk in piece_chunks}
        for index, chunk in enumerate(piece_chunks):
            state = states[chunk.id]
            vector = piece_vectors[index]
            weight = len(inputs[index])
            state["received"] += 1
            if state["expected"] == 1:
                state["vector"] = list(vector)
            else:
                state["vector"] = [total + value * weight
                                   for total, value in zip(state["vector"], vector)]
        completed = [chunk_id for chunk_id in open_requests[request_id]
                     if states[chunk_id]["received"] == states[chunk_id]["expected"]]
        try:
            for chunk_id in completed:
                state = states[chunk_id]
                chunk = state["chunk"]
                if chunk.embedding is not None:
                    raise RuntimeError("Existing vector encountered; refusing overwrite")
                vector = state["vector"]
                if state["expected"] > 1:
                    norm = math.sqrt(sum(value * value for value in vector))
                    if not math.isfinite(norm) or norm == 0:
                        raise ValueError("Cannot normalize pooled embedding vector")
                    vector = [value / norm for value in vector]
                chunk.embedding = vector
                chunk.embedding_model = args.model
            if completed:
                db.commit()
        except BaseException:
            db.rollback()
            raise
        embedded += len(completed)
        completed_ids = set(completed)
        for prior_id, pending_ids in list(open_requests.items()):
            affected = bool(pending_ids & completed_ids)
            pending_ids.difference_update(completed_ids)
            if prior_id == request_id or affected:
                ledger.append("committed", request_id=prior_id,
                              chunk_ids=sorted(completed) if prior_id == request_id else [],
                              pending_chunk_ids=sorted(pending_ids),
                              run_committed_chunks=ledger.committed_chunks +
                              (len(completed) if prior_id == request_id else 0),
                              run_spent_usd=ledger.spent_usd)
            if not pending_ids:
                del open_requests[prior_id]
        for chunk_id in completed:
            del states[chunk_id]
        emit("batch_committed", request_id=request_id, batch_tokens=usage,
             embedded_chunks=embedded, run_committed_chunks=ledger.committed_chunks,
             spent_usd=ledger.spent_usd)
        piece_chunks, inputs, tokens = [], [], 0

    while args.max_chunks is None or scanned < args.max_chunks:
        limit = min(args.batch_size, args.max_chunks - scanned) if args.max_chunks else args.batch_size
        candidates = db.scalars(pending_chunk_query(last_chunk_id=last_chunk_id,
            source_type=args.source_type, case_ids=args.case_ids).limit(limit)).all()
        if not candidates:
            break
        for chunk in candidates:
            scanned += 1
            last_chunk_id = chunk.id
            if chunk.embedding is not None:
                continue
            reason = None
            encoded = []
            if not isinstance(chunk.text, str) or not chunk.text.strip():
                reason = "empty_or_malformed"
            else:
                try:
                    encoded = encode_embedding_input(chunk.text, args.model)
                except UnicodeError:
                    reason = "malformed_unicode"
                if any(0xD800 <= ord(character) <= 0xDFFF for character in chunk.text):
                    reason = "malformed_unicode"
                if not encoded:
                    reason = reason or "empty_tokens"
            if reason:
                ledger.append("blocker", chunk_id=chunk.id, case_id=chunk.case_id,
                              reason=reason, actual_tokens=len(encoded))
                continue
            pieces = split_embedding_tokens(encoded, min(MAX_EMBEDDING_INPUT_TOKENS, args.max_request_tokens))
            states[chunk.id] = {"chunk": chunk, "expected": len(pieces), "received": 0,
                                "vector": [0.0] * 1536}
            for piece in pieces:
                if inputs and (tokens + len(piece) > args.max_request_tokens or len(inputs) >= args.batch_size):
                    commit_batch()
                inputs.append(piece)
                piece_chunks.append(chunk)
                tokens += len(piece)
    commit_batch()
    elapsed = max(0.0, pacer.clock() - started)
    summary = {"embedded_chunks": embedded, "scanned_chunks": scanned,
               "run_committed_chunks": ledger.committed_chunks, "spent_usd": ledger.spent_usd,
               "elapsed_seconds": elapsed, "paragraphs_per_second": embedded / elapsed if elapsed else 0.0,
               "request_count": request_count, "request_tokens": request_tokens,
               "request_inputs": request_inputs,
               "blockers": len(ledger.blockers), "status": "blocked" if ledger.incomplete else "bounded_complete"}
    ledger.append("summary", **summary)
    return summary


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--budget-usd", type=float, default=25.0)
    parser.add_argument("--cost-per-1m", type=float, default=DEFAULT_COST_PER_1M)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    parser.add_argument("--retry-base-seconds", type=float, default=DEFAULT_RETRY_BASE_SECONDS)
    parser.add_argument("--source-type", default=None)
    parser.add_argument("--case-ids-csv", default=None)
    parser.add_argument("--max-workers", type=int, default=1)
    parser.add_argument("--progress-every", type=int, default=500)
    parser.add_argument("--max-chunks", type=int, default=None)
    parser.add_argument("--max-request-tokens", type=int, default=DEFAULT_MAX_REQUEST_TOKENS)
    parser.add_argument("--requests-per-minute", type=float, default=0, help="Optional pacing cap; 0 disables voluntary pacing.")
    parser.add_argument("--tokens-per-minute", type=float, default=0, help="Optional pacing cap; 0 disables voluntary pacing.")
    parser.add_argument("--request-timeout", type=float, default=60)
    parser.add_argument("--paragraph-only", action="store_true", default=True,
                        help="Embed canonical paragraph chunks only (the only supported mode).")
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.model != "text-embedding-3-small":
        parser.error("Only text-embedding-3-small (1536 dimensions) is supported")
    if not args.paragraph_only:
        parser.error("full-case/structural embeddings are disabled; paragraph-only mode is automatic")
    if args.max_workers != 1:
        parser.error("Paced recovery requires --max-workers 1")
    if not args.dry_run and args.run_dir is None:
        parser.error("Apply requires --run-dir for durable logs and ledger")
    for name in ("budget_usd", "cost_per_1m", "retry_base_seconds", "request_timeout"):
        value = getattr(args, name)
        if not math.isfinite(value) or value <= 0:
            parser.error(f"--{name.replace('_', '-')} must be finite and positive")
    if not 1 <= args.batch_size <= 100 or not 1 <= args.max_request_tokens <= 100000:
        parser.error("batch-size must be 1..100 and max-request-tokens 1..100000")
    if not 1 <= args.max_retries <= 12 or not 0 < args.request_timeout <= 600:
        parser.error("max-retries must be 1..12 and request-timeout must be <=600 seconds")
    for name in ("requests_per_minute", "tokens_per_minute"):
        if not math.isfinite(getattr(args, name)) or getattr(args, name) < 0:
            parser.error(f"--{name.replace('_', '-')} must be finite and nonnegative")
    if args.tokens_per_minute and args.max_request_tokens > args.tokens_per_minute:
        parser.error("max-request-tokens must not exceed tokens-per-minute")
    if args.progress_every < 1 or (args.max_chunks is not None and args.max_chunks < 1):
        parser.error("progress-every and max-chunks must be positive")
    return args


def run_identity(args) -> dict:
    cohort = json.dumps(sorted(args.case_ids) if args.case_ids else None).encode("ascii")
    return {"version": 2, "model": args.model, "paragraph_only": True,
            "long_paragraph_strategy": "token_weighted_normalized_pooling",
            "cohort_sha256": hashlib.sha256(cohort).hexdigest(), "source_type": args.source_type,
            "rpm": args.requests_per_minute, "tpm": args.tokens_per_minute,
            "batch_size": args.batch_size, "max_request_tokens": args.max_request_tokens,
            "budget_usd": args.budget_usd, "cost_per_1m": args.cost_per_1m}


def dry_run(db, args) -> int:
    sample = db.scalars(pending_chunk_query(source_type=args.source_type, case_ids=args.case_ids)
                        .limit(args.max_chunks or 20)).all()
    tokens = 0
    blockers = 0
    for chunk in sample:
        reason = None
        count = 0
        if not isinstance(chunk.text, str) or not chunk.text.strip():
            reason = "empty_or_malformed"
        elif any(0xD800 <= ord(character) <= 0xDFFF for character in chunk.text):
            reason = "malformed_unicode"
        else:
            count = count_embedding_tokens(chunk.text, args.model)
            emit("paragraph_preflight", chunk_id=chunk.id, actual_tokens=count,
                 temporary_inputs=math.ceil(count / min(MAX_EMBEDDING_INPUT_TOKENS, args.max_request_tokens)))
        if reason:
            blockers += 1
            emit("blocker", chunk_id=chunk.id, case_id=chunk.case_id, reason=reason, actual_tokens=count)
        tokens += count
    emit("dry_run", pending_sample=len(sample), exact_tokens=tokens,
         cost_usd=estimate_cost_usd(tokens, args.cost_per_1m), blockers=blockers, coverage="sample_only")
    return 1 if blockers else 0


def main(argv=None) -> int:
    args = parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(stream)
    file_handler = None
    writer_lock = None
    ledger = None
    try:
        args.case_ids = load_case_ids_from_csv(args.case_ids_csv) if args.case_ids_csv else None
        if not args.case_ids and not args.source_type:
            raise ValueError("An explicit --case-ids-csv or --source-type cohort is required")
        if args.dry_run:
            with SessionLocal() as db:
                return dry_run(db, args)
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY is required")
        writer_lock = acquire_writer_lock(
            Path(__file__).resolve().parents[1] / "data" / "overnight_runs" / "openai-paragraph-writer.lock"
        )
        args.run_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(args.run_dir / "events.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(file_handler)
        ledger = RequestLedger(args.run_dir / "requests.jsonl", run_identity(args))
        pacer = RequestPacer(args.requests_per_minute, args.tokens_per_minute)
        for name in ("OPENAI_ORG_ID", "OPENAI_ORGANIZATION", "OPENAI_PROJECT_ID"):
            os.environ.pop(name, None)
        with OpenAI(api_key=os.environ["OPENAI_API_KEY"], timeout=args.request_timeout, max_retries=0) as client:
            with SessionLocal() as db:
                summary = embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
        return 1 if summary["status"] == "blocked" else 0
    except (Exception, KeyboardInterrupt) as exc:
        fields = {"error_type": type(exc).__name__, "status": "incomplete"}
        if ledger is not None:
            ledger.append("terminal_failure", **fields, spent_usd=ledger.spent_usd,
                          run_committed_chunks=ledger.committed_chunks)
        else:
            emit("terminal_failure", **fields)
        return 1
    finally:
        if writer_lock is not None:
            writer_lock.close()
        for handler in (file_handler, stream):
            if handler is not None:
                logger.removeHandler(handler)
                handler.close()


if __name__ == "__main__":
    raise SystemExit(main())
