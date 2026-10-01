from types import SimpleNamespace

import math
import pytest
import httpx
from openai import RateLimitError
from sqlalchemy import create_engine, event, select, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from scripts import embed_openai_chunks as runner

from scripts.embed_openai_chunks import (
    BudgetState,
    count_embedding_tokens,
    estimate_cost_usd,
    fit_batch_to_budget,
    parse_args,
)


def test_count_embedding_tokens_uses_model_tokenizer():
    assert count_embedding_tokens("immigration judicial review", "text-embedding-3-small") > 0


def test_count_embedding_tokens_treats_special_token_text_as_literal():
    assert count_embedding_tokens("case text includes <|endoftext|>", "text-embedding-3-small") > 0


def test_estimate_cost_usd_scales_linearly():
    assert estimate_cost_usd(0, 0.02) == 0.0
    assert estimate_cost_usd(1_000_000, 0.02) == 0.02
    assert estimate_cost_usd(500_000, 0.02) == 0.01


def test_fit_batch_to_budget_truncates_before_exceeding_cap():
    chunks = [
        SimpleNamespace(token_estimate=250_000),
        SimpleNamespace(token_estimate=250_000),
        SimpleNamespace(token_estimate=250_000),
    ]
    budget = BudgetState(spent_usd=0.0, budget_usd=0.01)

    selected = fit_batch_to_budget(chunks, budget, cost_per_1m=0.02)

    assert len(selected) == 2


def test_fit_batch_to_budget_returns_empty_when_first_chunk_exceeds_cap():
    chunks = [SimpleNamespace(token_estimate=600_000)]
    budget = BudgetState(spent_usd=0.0, budget_usd=0.01)

    selected = fit_batch_to_budget(chunks, budget, cost_per_1m=0.02)

    assert selected == []


def test_runner_defaults_to_paragraph_only_and_larger_request_window():
    args = parse_args([
        "--case-ids-csv", "cohort.csv",
        "--dry-run",
    ])

    assert args.paragraph_only is True
    assert args.max_workers == 1
    assert args.max_request_tokens == 100000
    assert args.requests_per_minute == 0
    assert args.tokens_per_minute == 0


def make_chunk(chunk_id, text):
    return SimpleNamespace(id=chunk_id, case_id=10, text=text, embedding=None, embedding_model=None)


class FakeSession:
    def __init__(self, chunks, fail_commit=False):
        self.chunks = chunks
        self.fail_commit = fail_commit
        self.commits = 0
        self.rollbacks = 0
        self.queries = []
        self.expire_on_commit = True
        self.persisted = {chunk.id: (chunk.embedding, chunk.embedding_model) for chunk in chunks}

    def scalars(self, statement):
        self.queries.append(statement)
        params = statement.compile().params
        last_id = params["id_1"]
        limit = statement._limit_clause.value
        selected = [chunk for chunk in self.chunks if chunk.id > last_id and chunk.embedding is None][:limit]
        return SimpleNamespace(all=lambda: selected)

    def commit(self):
        if self.fail_commit:
            raise RuntimeError("simulated database failure")
        self.commits += 1
        self.persisted = {chunk.id: (chunk.embedding, chunk.embedding_model) for chunk in self.chunks}

    def rollback(self):
        self.rollbacks += 1
        for chunk in self.chunks:
            chunk.embedding, chunk.embedding_model = self.persisted[chunk.id]


class FakeClient:
    def __init__(self, rate_limit_once=False):
        self.requests = []
        self.rate_limit_once = rate_limit_once
        self.embeddings = SimpleNamespace(with_raw_response=SimpleNamespace(create=self.create))

    def create(self, *, model, input):
        if self.rate_limit_once:
            self.rate_limit_once = False
            response = httpx.Response(429, headers={"retry-after": "3"},
                                      request=httpx.Request("POST", "https://example.test/embeddings"))
            raise RateLimitError("simulated rate limit", response=response, body=None)
        self.requests.append(input)
        data = []
        for index, tokens in enumerate(input):
            vector = [0.0] * 1536
            vector[tokens[0] % 2] = 1.0
            data.append(SimpleNamespace(index=index, embedding=vector))
        response = SimpleNamespace(data=list(reversed(data)), usage=SimpleNamespace(total_tokens=sum(map(len, input))))
        return SimpleNamespace(headers={}, parse=lambda: response)


def run_fake(monkeypatch, tmp_path, chunks, *, token_map, request_cap=100000, batch_size=100,
             budget=1, rate_limit_once=False, fail_commit=False):
    monkeypatch.setattr(runner, "encode_embedding_input", lambda text, model: token_map[text])
    args = runner.parse_args(["--run-dir", str(tmp_path), "--max-request-tokens", str(request_cap),
                              "--batch-size", str(batch_size), "--budget-usd", str(budget)])
    args.case_ids = {10}
    db = FakeSession(chunks, fail_commit=fail_commit)
    client = FakeClient(rate_limit_once=rate_limit_once)
    ledger = runner.RequestLedger(tmp_path / "requests.jsonl", runner.run_identity(args))
    now = [0.0]
    sleeps = []

    def sleep(delay):
        sleeps.append(delay)
        now[0] += delay

    pacer = runner.RequestPacer(clock=lambda: now[0], sleep=sleep)
    return args, db, client, ledger, pacer, sleeps


def test_short_paragraph_batch_uses_response_indices_without_sleep(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "first"), make_chunk(2, "second")]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks, token_map={"first": [0, 0], "second": [1, 1]})
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert result["embedded_chunks"] == 2
    assert chunks[0].embedding == [1.0] + [0.0] * 1535
    assert chunks[1].embedding == [0.0, 1.0] + [0.0] * 1534
    assert len(client.requests) == 1
    assert sleeps == []
    assert db.commits == 1
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert reloaded.committed_chunks == 2
    result = runner.embed_pending_chunks(db, client, args=args, ledger=reloaded, pacer=pacer)
    assert result["embedded_chunks"] == 0
    assert len(client.requests) == 1


def test_large_paragraph_spans_bounded_requests_and_pools_token_weights(monkeypatch, tmp_path):
    chunk = make_chunk(1, "long")
    encoded = [0] * 16384 + [1] * 1000
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [chunk], token_map={"long": encoded}, request_cap=9000)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    sent = [piece for request in client.requests for piece in request]
    assert [token for piece in sent for token in piece] == encoded
    assert all(len(piece) <= 8192 for piece in sent)
    assert all(sum(map(len, request)) <= 9000 for request in client.requests)
    assert len(client.requests) == 3
    assert db.commits == 1
    assert result["run_committed_chunks"] == 1
    assert chunk.text == "long"
    assert chunk.embedding[0] / chunk.embedding[1] == pytest.approx(16.384)
    assert math.sqrt(sum(value ** 2 for value in chunk.embedding)) == pytest.approx(1)
    assert sleeps == []
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert reloaded.spent_usd == pytest.approx(runner.estimate_cost_usd(len(encoded), args.cost_per_1m))
    assert reloaded.committed_chunks == 1


def test_many_windows_respect_input_count_limit(monkeypatch, tmp_path):
    chunk = make_chunk(1, "long")
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [chunk], token_map={"long": [0] * 20000}, batch_size=1)
    runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert len(client.requests) == 3
    assert all(len(request) == 1 for request in client.requests)


def test_budget_exhaustion_does_not_commit_partial_paragraph(monkeypatch, tmp_path):
    chunk = make_chunk(1, "long")
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [chunk], token_map={"long": [0] * 20000}, request_cap=8192, budget=0.0002)
    with pytest.raises(RuntimeError, match="Budget exhausted"):
        runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert len(client.requests) == 1
    assert chunk.embedding is None
    assert db.commits == 0
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert reloaded.spent_usd > 0
    assert not reloaded.incomplete


def test_retry_after_waits_only_on_actual_rate_limit(monkeypatch, tmp_path):
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [make_chunk(1, "text")], token_map={"text": [0]}, rate_limit_once=True)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert result["embedded_chunks"] == 1
    assert sleeps == [3]
    assert ledger.spent_usd == pytest.approx(runner.estimate_cost_usd(1, args.cost_per_1m))


def test_commit_failure_keeps_received_cost_for_safe_restart(monkeypatch, tmp_path):
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [make_chunk(1, "text")], token_map={"text": [0]}, fail_commit=True)
    with pytest.raises(RuntimeError, match="simulated database failure"):
        runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert db.rollbacks == 1
    assert ledger.committed_chunks == 0
    assert ledger.spent_usd > 0
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert not reloaded.incomplete
    assert reloaded.spent_usd == ledger.spent_usd
    assert db.chunks[0].embedding is None
    assert db.expire_on_commit is True


def test_paragraph_query_is_scoped_keyset_without_grouping():
    statement = runner.pending_chunk_query(last_chunk_id=20, case_ids={10}).limit(100)
    sql = str(statement.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
    assert "case_chunks.chunk_set = 'paragraph'" in sql
    assert "case_chunks.embedding IS NULL" in sql
    assert "case_chunks.id > 20" in sql
    assert "cases.id IN (10)" in sql
    assert "LIMIT 100" in sql
    assert "GROUP BY" not in sql
    assert "paragraph_start =" not in sql


def test_empty_paragraph_reports_blocker_without_request(monkeypatch, tmp_path):
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [make_chunk(1, "")], token_map={})
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert result["status"] == "blocked"
    assert client.requests == []


def test_unreconciled_reservation_blocks_restart(tmp_path):
    ledger = runner.RequestLedger(tmp_path / "ledger.jsonl", {"test": True})
    ledger.append("reserve", request_id="ambiguous", chunk_ids=[1], cost_usd=0.01)
    with pytest.raises(RuntimeError, match="Unreconciled"):
        runner.RequestLedger(ledger.path, {"test": True})


def test_shared_writer_lock_prevents_overlap_and_releases_on_close(tmp_path):
    path = tmp_path / "writer.lock"
    handle = runner.acquire_writer_lock(path)
    try:
        with pytest.raises(RuntimeError, match="shared lock"):
            runner.acquire_writer_lock(path)
    finally:
        handle.close()
    with runner.acquire_writer_lock(path):
        assert path.exists()


def test_received_restart_reembeds_only_null_row_without_resetting_spend(monkeypatch, tmp_path):
    chunk = make_chunk(1, "long")
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [chunk], token_map={"long": [0] * 20000}, request_cap=8192, budget=0.0002)
    with pytest.raises(RuntimeError, match="Budget exhausted"):
        runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    prior_cost = ledger.spent_usd
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    with pytest.raises(RuntimeError, match="Budget exhausted"):
        runner.embed_pending_chunks(db, client, args=args, ledger=reloaded, pacer=pacer)
    assert reloaded.spent_usd == prior_cost
    assert chunk.embedding is None
    assert len(client.requests) == 1


def test_dry_run_accepts_long_paragraph_without_api_or_db_mutation(monkeypatch, tmp_path):
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [make_chunk(1, "long")], token_map={"long": [0] * 30000}, request_cap=9000)
    assert runner.dry_run(db, args) == 0
    assert db.commits == 0
    assert client.requests == []


def test_long_paragraph_does_not_disrupt_neighbor_short_batches(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "before"), make_chunk(2, "long"), make_chunk(3, "after")]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks, token_map={"before": [0], "long": [1] * 10000, "after": [0]}, request_cap=8192)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert result["embedded_chunks"] == 3
    assert all(chunk.embedding is not None for chunk in chunks)
    assert ledger.committed_chunks == 3
    assert sum(sum(map(len, request)) for request in client.requests) == 10002
    assert sleeps == []


def test_short_and_long_paragraphs_share_one_indexed_request(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "before"), make_chunk(2, "long"), make_chunk(3, "after")]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks,
        token_map={"before": [0], "long": [1] * 10000, "after": [0]})
    original_create = client.create

    def create(**kwargs):
        raw = original_create(**kwargs)
        response = raw.parse()
        for item in response.data:
            item.embedding = [value * 2 for value in item.embedding]
        return raw

    client.embeddings.with_raw_response.create = create
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert len(client.requests) == 1
    assert list(map(len, client.requests[0])) == [1, 8192, 1808, 1]
    assert chunks[0].embedding == chunks[2].embedding == [2.0] + [0.0] * 1535
    assert chunks[1].embedding == [0.0, 1.0] + [0.0] * 1534
    assert result["run_committed_chunks"] == 3
    assert result["request_count"] == 1
    assert sleeps == []


def test_request_tail_carries_across_keyset_fetch_pages(monkeypatch, tmp_path):
    chunks = [make_chunk(chunk_id, str(chunk_id)) for chunk_id in range(1, 7)]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks,
        token_map={chunk.text: [chunk.id % 2] * 6 for chunk in chunks},
        request_cap=10, batch_size=2)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert len(client.requests) == 6
    assert result["embedded_chunks"] == 6
    assert len(db.queries) == 4
    assert db.expire_on_commit is True
    assert sleeps == []


def test_mixed_windows_carry_tail_across_fetches_and_reduce_requests(monkeypatch, tmp_path):
    chunks = [make_chunk(chunk_id, "long" if chunk_id % 2 else "short")
              for chunk_id in range(1, 11)]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks, token_map={"long": [1] * 9000, "short": [0]}, batch_size=4)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert list(map(len, client.requests)) == [4, 4, 4, 3]
    assert len(db.queries) == 4
    assert result["request_count"] == 4
    assert result["request_inputs"] == 15
    assert result["request_tokens"] == 45005
    assert result["embedded_chunks"] == ledger.committed_chunks == 10
    assert all(chunk.embedding is not None for chunk in chunks)
    assert sleeps == []


def test_huge_paragraph_shares_requests_and_never_commits_partial_vector(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "short"), make_chunk(2, "huge"), make_chunk(3, "after")]
    encoded = [0] * (8192 * 25) + [1] * 1000
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks,
        token_map={"short": [1], "huge": encoded, "after": [0]})
    original_create = client.create
    observations = []

    def create(**kwargs):
        observations.append((chunks[0].embedding is not None, chunks[1].embedding is not None))
        return original_create(**kwargs)

    client.embeddings.with_raw_response.create = create
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert observations == [(False, False), (True, False), (True, False)]
    assert list(map(len, client.requests)) == [13, 12, 3]
    assert all(sum(map(len, request)) <= 100000 and len(request) <= 100 for request in client.requests)
    assert all(len(piece) <= 8192 for request in client.requests for piece in request)
    assert chunks[1].embedding[0] / chunks[1].embedding[1] == pytest.approx(204.8)
    assert db.commits == 2
    assert result["run_committed_chunks"] == 3
    assert not ledger.incomplete
    assert sleeps == []


def test_mixed_request_retains_cost_and_committed_count_after_failure_and_restart(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "short"), make_chunk(2, "long"), make_chunk(3, "after")]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks,
        token_map={"short": [0], "long": [1] * 17384, "after": [0]}, request_cap=9000)
    original_commit = db.commit

    def commit():
        db.fail_commit = db.commits == 1
        original_commit()

    monkeypatch.setattr(db, "commit", commit)
    with pytest.raises(RuntimeError, match="simulated database failure"):
        runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    prior_cost = ledger.spent_usd
    assert ledger.committed_chunks == 1
    assert chunks[0].embedding is not None
    assert chunks[1].embedding is chunks[2].embedding is None
    assert all(item["state"] == "received" for item in ledger.requests.values())
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert reloaded.spent_usd == prior_cost
    assert reloaded.committed_chunks == 1
    assert not reloaded.incomplete
    monkeypatch.setattr(db, "commit", original_commit)
    db.fail_commit = False
    result = runner.embed_pending_chunks(db, client, args=args, ledger=reloaded, pacer=pacer)
    assert result["embedded_chunks"] == 2
    assert result["run_committed_chunks"] == 3
    assert result["spent_usd"] == pytest.approx(
        prior_cost + runner.estimate_cost_usd(17385, args.cost_per_1m))
    again = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert again.committed_chunks == 3
    assert not again.incomplete
    assert sleeps == []


def test_mixed_partial_request_budget_failure_keeps_completed_neighbor(monkeypatch, tmp_path):
    chunks = [make_chunk(1, "short"), make_chunk(2, "long")]
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, chunks,
        token_map={"short": [0], "long": [1] * 20000}, request_cap=9000, budget=0.0002)
    with pytest.raises(RuntimeError, match="Budget exhausted"):
        runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert len(client.requests) == db.commits == 1
    assert chunks[0].embedding is not None and chunks[1].embedding is None
    reloaded = runner.RequestLedger(ledger.path, runner.run_identity(args))
    assert reloaded.committed_chunks == 1
    assert reloaded.spent_usd == pytest.approx(runner.estimate_cost_usd(8193, args.cost_per_1m))
    assert not reloaded.incomplete


def test_ambiguous_usage_blocks_restart_even_with_committed_neighbor(tmp_path):
    ledger = runner.RequestLedger(tmp_path / "ledger.jsonl", {"test": True})
    ledger.append("reserve", request_id="mixed", chunk_ids=[1, 2], cost_usd=0.01)
    ledger.append("received", request_id="mixed")
    ledger.append("committed", request_id="mixed", chunk_ids=[1], pending_chunk_ids=[2])
    ledger.append("reserve", request_id="ambiguous", chunk_ids=[2], cost_usd=0.01)
    ledger.append("usage", request_id="ambiguous", cost_usd=0.01)
    with pytest.raises(RuntimeError, match="Unreconciled"):
        runner.RequestLedger(ledger.path, {"test": True})


def test_summary_reports_elapsed_and_paragraph_throughput(monkeypatch, tmp_path):
    args, db, client, ledger, pacer, sleeps = run_fake(
        monkeypatch, tmp_path, [make_chunk(1, "short")], token_map={"short": [0]})
    times = iter([10.0, 10.0, 10.0, 12.0])
    pacer.clock = lambda: next(times)
    result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
    assert result["elapsed_seconds"] == 2.0
    assert result["paragraphs_per_second"] == 0.5
    assert result["request_count"] == result["request_inputs"] == result["request_tokens"] == 1
    assert sleeps == []


def test_real_orm_commit_does_not_reload_buffered_paragraphs(monkeypatch, tmp_path):
    class Base(DeclarativeBase):
        pass

    class Paragraph(Base):
        __tablename__ = "paragraphs"
        id: Mapped[int] = mapped_column(primary_key=True)
        case_id: Mapped[int]
        text: Mapped[str]
        embedding: Mapped[str | None] = mapped_column(String, nullable=True)
        embedding_model: Mapped[str | None] = mapped_column(nullable=True)

    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        db.add_all([Paragraph(id=chunk_id, case_id=10, text=str(chunk_id)) for chunk_id in range(1, 7)])
        db.commit()
        args, fake_db, client, ledger, pacer, sleeps = run_fake(
            monkeypatch, tmp_path, [], token_map={str(chunk_id): [0] * 6 for chunk_id in range(1, 7)},
            request_cap=10, batch_size=2)
        monkeypatch.setattr(runner, "pending_chunk_query", lambda *, last_chunk_id=0, **kwargs:
                            select(Paragraph).where(Paragraph.id > last_chunk_id,
                                                    Paragraph.embedding.is_(None)).order_by(Paragraph.id))
        statements = []

        def observe(connection, cursor, statement, parameters, context, executemany):
            statements.append(statement)

        def serialize_vectors(session, flush_context, instances):
            for paragraph in session.dirty:
                if isinstance(paragraph.embedding, list):
                    paragraph.embedding = str(paragraph.embedding)

        event.listen(engine, "before_cursor_execute", observe)
        event.listen(db, "before_flush", serialize_vectors)
        result = runner.embed_pending_chunks(db, client, args=args, ledger=ledger, pacer=pacer)
        assert result["embedded_chunks"] == 6
        assert len([statement for statement in statements if statement.startswith("SELECT")]) == 4
        assert db.expire_on_commit is True
        assert sleeps == []
    engine.dispose()
