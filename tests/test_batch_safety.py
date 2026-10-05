"""Safety rails for batch jobs that share a machine with the live site (no network, no real database)."""

from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, func, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import batch_safety
from backend.batch_safety import HealthGate, make_limited_engine, postgres_options, stop_requested, throttle_sleep
from backend.database import (
    Base,
    Case,
    CaseChunk,
    Citation,
    ParagraphCitationEdge,
    ParagraphCitationStatus,
)
from backend.paragraph_cited_by_runner import parse_args, run


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


def test_throttle_sleep_keeps_work_share_at_or_below_duty():
    assert throttle_sleep(1.0, 2.0, 0.2) == 4.0  # 1s of work, 4s rest = 20% duty
    assert throttle_sleep(0.1, 2.0, 0.2) == 2.0  # never below the base rest
    assert throttle_sleep(5.0, 0.0, 0.5) == 5.0
    assert throttle_sleep(3.0, 1.0, 1.0) == 1.0  # a duty of 1 means "no extra throttle"


def test_postgres_options_hold_for_the_whole_connection_and_are_safe():
    options = postgres_options(statement_timeout_ms=15000, lock_timeout_ms=2000, idle_in_transaction_ms=30000,
                               application_name="bad name; DROP")
    assert "-c statement_timeout=15000" in options
    assert "-c lock_timeout=2000" in options
    assert "-c idle_in_transaction_session_timeout=30000" in options
    assert "application_name=badnameDROP" in options


def test_limited_postgres_engine_is_capped_at_one_connection():
    engine = make_limited_engine("postgresql+psycopg2://u:p@localhost:5432/x", statement_timeout_ms=1234)
    assert engine.pool.size() == 1
    assert engine.pool._max_overflow == 0
    engine.dispose()


def test_limited_engine_other_backends_still_build():
    engine = make_limited_engine("sqlite://")
    assert engine.dialect.name == "sqlite"
    engine.dispose()


def test_lower_priority_never_raises(monkeypatch):
    monkeypatch.setattr(batch_safety.os, "nice", lambda n: (_ for _ in ()).throw(OSError("no")), raising=False)
    monkeypatch.setattr(batch_safety.sys, "platform", "linux")
    assert "unchanged" in batch_safety.lower_process_priority()
    monkeypatch.setattr(batch_safety.os, "nice", lambda n: 19, raising=False)
    assert batch_safety.lower_process_priority() == "nice 19"


def test_fetch_seconds_refuses_non_http_urls():
    with pytest.raises(ValueError):
        batch_safety.fetch_seconds("file:///etc/passwd")


def _gate(times, **kw):
    pauses, logs = [], []
    seq = iter(times)

    def fetch(_url):
        value = next(seq)
        if isinstance(value, Exception):
            raise value
        return value

    gate = HealthGate("http://x/health", fetch=fetch, sleeper=pauses.append, log=logs.append, **kw)
    return gate, pauses, logs


def test_health_gate_without_url_is_always_healthy():
    assert HealthGate(None).wait_until_healthy() is True


def test_health_gate_backs_off_with_doubling_waits_then_recovers():
    gate, pauses, _ = _gate([4.0, OSError("down"), 0.2], base_wait=10, max_wait=25)
    assert gate.wait_until_healthy() is True
    assert pauses == [10, 20]
    assert gate.waits_total == 2


def test_health_gate_gives_up_when_the_site_never_recovers():
    gate, pauses, _ = _gate([9.0] * 4, max_waits=3, base_wait=1, max_wait=2)
    assert gate.wait_until_healthy() is False
    assert pauses == [1, 2, 2]


def test_stop_file(tmp_path):
    flag = tmp_path / "stop.txt"
    assert stop_requested(str(flag)) is False
    flag.write_text("x")
    assert stop_requested(str(flag)) is True
    assert stop_requested(None) is False


# ---- the runner, against SQLite ----

@pytest.fixture
def factory():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine, tables=[m.__table__ for m in (
        Case, CaseChunk, Citation, ParagraphCitationEdge, ParagraphCitationStatus)])
    with Session(engine) as session:
        session.add(Case(id=1, title="Authority", citation="2019 SCC 65", court="SCC", date=date(2019, 1, 1), full_text="x"))
        for cid in range(2, 8):
            full = f"Reasons. See also Authority, 2019 SCC 65 at para 12. End {cid}."
            start = full.index("Authority")
            session.add(Case(id=cid, title=f"Citer {cid}", citation=f"2020 FC {cid}", court="FC", date=date(2020, 1, cid), full_text=full))
            session.add(Citation(source_case_id=cid, target_case_id=1, citation_kind="neutral",
                                 citation_text="Authority, 2019 SCC 65 at para 12", normalized_citation="2019 SCC 65",
                                 target_paragraph=12, offset_start=start, offset_end=start + 34))
        session.commit()
    return lambda: Session(engine)


def _args(tmp_path, *extra):
    return parse_args(["--stop-file", str(tmp_path / "stop.txt"), *extra])


def _count(factory, model):
    with factory() as db:
        return db.scalar(select(func.count()).select_from(model))


def test_defaults_are_gentle():
    args = parse_args([])
    assert args.apply is False and args.batch_size <= 5 and args.sleep_between_batches >= 2 and args.limit is None
    assert args.statement_timeout_ms <= 15000 and args.lock_timeout_ms <= 2000 and args.max_duty <= 0.2


def test_incremental_defaults_to_bounded_limit_and_rejects_nonpositive_limit():
    assert parse_args(["--incremental"]).limit == 50
    with pytest.raises(SystemExit):
        parse_args(["--incremental", "--limit", "0"])
    with pytest.raises(SystemExit):
        parse_args(["--incremental", "--limit", "-1"])


def test_incremental_rejects_health_url():
    with pytest.raises(SystemExit):
        parse_args(["--incremental", "--health-url", "http://127.0.0.1:8001/health/ready"])


def test_plan_mode_writes_nothing(factory, tmp_path):
    result = run(_args(tmp_path), factory, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 6 and result.stopped_because == "finished"
    assert _count(factory, ParagraphCitationStatus) == 0


def test_apply_writes_in_small_batches_and_sleeps_between(factory, tmp_path):
    pauses = []
    result = run(_args(tmp_path, "--apply", "--batch-size", "2"), factory, sleep=pauses.append, log=lambda m: None)
    assert result.processed == 6
    assert _count(factory, ParagraphCitationStatus) == 6
    assert _count(factory, ParagraphCitationEdge) == 6
    assert len([p for p in pauses if p >= 2.0]) >= 3  # a real rest after each batch


def test_limit_and_resume(factory, tmp_path):
    first = run(_args(tmp_path, "--apply", "--limit", "2", "--batch-size", "1"), factory, sleep=lambda s: None, log=lambda m: None)
    assert first.processed == 2 and first.stopped_because == "limit reached"
    second = run(_args(tmp_path, "--apply"), factory, sleep=lambda s: None, log=lambda m: None)
    assert second.processed == 4 and second.stopped_because == "finished"
    assert _count(factory, ParagraphCitationStatus) == 6


def test_stop_file_stops_before_any_work(factory, tmp_path):
    (tmp_path / "stop.txt").write_text("stop")
    result = run(_args(tmp_path, "--apply"), factory, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 0 and "stop file" in result.stopped_because
    assert _count(factory, ParagraphCitationStatus) == 0


def test_slow_site_aborts_without_touching_the_database(factory, tmp_path):
    gate = HealthGate("http://x", fetch=lambda u: 99.0, sleeper=lambda s: None, log=lambda m: None, max_waits=2)
    result = run(_args(tmp_path, "--apply"), factory, health=gate, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 0 and "slow" in result.stopped_because
    assert _count(factory, ParagraphCitationStatus) == 0


def test_cpu_budget_and_time_limit(factory, tmp_path):
    ticks = iter(range(0, 1000))
    result = run(_args(tmp_path, "--apply", "--max-cpu-seconds", "1", "--batch-size", "1"), factory,
                 sleep=lambda s: None, cpu_clock=lambda: float(next(ticks)), log=lambda m: None)
    assert result.stopped_because == "CPU budget used" and result.processed < 6
    clock = iter(x * 100.0 for x in range(0, 1000))
    result = run(_args(tmp_path, "--apply", "--max-minutes", "1", "--batch-size", "1"), factory,
                 sleep=lambda s: None, clock=lambda: next(clock), log=lambda m: None)
    assert result.stopped_because == "time limit reached"


def test_explicit_case_ids(factory, tmp_path):
    result = run(_args(tmp_path, "--apply", "--case-ids", "3", "5"), factory, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 2
    with factory() as db:
        done = set(db.scalars(select(ParagraphCitationStatus.source_case_id)))
    assert done == {3, 5}


def test_incremental_mode_commits_case_by_case_and_covers_no_citation_cases(factory, tmp_path):
    class FailingGate:
        def wait_until_healthy(self):
            raise AssertionError("health gate should be disabled in incremental mode")

    args = _args(tmp_path, "--apply", "--incremental", "--limit", "7", "--batch-size", "3")
    before = run(args, factory, health=FailingGate(), sleep=lambda s: None, log=lambda m: None)
    assert before.processed == 7 and before.stopped_because == "limit reached"
    with factory() as db:
        statuses = db.execute(
            select(ParagraphCitationStatus.source_case_id, ParagraphCitationStatus.edges, ParagraphCitationStatus.computed_at)
            .order_by(ParagraphCitationStatus.source_case_id)
        ).all()
        target = db.execute(
            select(ParagraphCitationStatus.edges).where(ParagraphCitationStatus.source_case_id == 1)
        ).scalar_one()
        assert target == 0
        assert [row.source_case_id for row in statuses] == [1, 2, 3, 4, 5, 6, 7]
        cited_by = db.execute(
            select(ParagraphCitationStatus.source_case_id).where(ParagraphCitationStatus.source_case_id == 1)
        ).scalar_one()
        assert cited_by == 1
        target_view = db.execute(select(ParagraphCitationStatus).where(ParagraphCitationStatus.source_case_id == 1)).scalar_one()
        assert target_view.edges == 0
        from backend.paragraph_cited_by_db import load_target_cited_by

        cited = load_target_cited_by(db, [(1, 12)])
        assert cited[(1, 12)]["citer_count"] == 6
        before_statuses = [(row.source_case_id, row.edges, row.computed_at) for row in statuses]
        before_edges = db.execute(
            select(ParagraphCitationEdge.id, ParagraphCitationEdge.source_case_id, ParagraphCitationEdge.target_case_id, ParagraphCitationEdge.target_paragraph)
            .order_by(ParagraphCitationEdge.id)
        ).all()
    after = run(args, factory, health=FailingGate(), sleep=lambda s: None, log=lambda m: None)
    assert after.processed == 0 and after.stopped_because == "finished"
    with factory() as db:
        after_statuses = db.execute(
            select(ParagraphCitationStatus.source_case_id, ParagraphCitationStatus.edges, ParagraphCitationStatus.computed_at)
            .order_by(ParagraphCitationStatus.source_case_id)
        ).all()
        after_edges = db.execute(
            select(ParagraphCitationEdge.id, ParagraphCitationEdge.source_case_id, ParagraphCitationEdge.target_case_id, ParagraphCitationEdge.target_paragraph)
            .order_by(ParagraphCitationEdge.id)
        ).all()
    assert before_statuses == [(row.source_case_id, row.edges, row.computed_at) for row in after_statuses]
    assert before_edges == after_edges


def test_bulk_operational_error_rolls_back_before_sleep(factory, tmp_path, monkeypatch):
    from backend import paragraph_cited_by_runner as runner

    real_compute = runner.compute_source_edges
    events: list[str] = []

    def flaky_compute(db, source_id):
        if source_id == 2:
            raise OperationalError("statement", {}, Exception("boom"))
        return real_compute(db, source_id)

    def spy_factory():
        db = factory()
        original_rollback = db.rollback

        def rollback():
            events.append("rollback")
            return original_rollback()

        db.rollback = rollback
        return db

    monkeypatch.setattr(runner, "compute_source_edges", flaky_compute)
    result = run(
        _args(tmp_path, "--apply", "--batch-size", "3"),
        spy_factory,
        sleep=lambda seconds: events.append(f"sleep:{seconds}"),
        log=lambda m: None,
    )

    assert result.failed == [2]
    assert events[0] == "rollback"
    assert events[1].startswith("sleep")


def test_incremental_mode_rolls_back_only_the_failed_case(factory, tmp_path, monkeypatch):
    from backend import paragraph_cited_by_runner as runner

    real_compute = runner.compute_source_edges

    def flaky_compute(db, source_id):
        if source_id == 3:
            raise RuntimeError("boom")
        return real_compute(db, source_id)

    monkeypatch.setattr(runner, "compute_source_edges", flaky_compute)
    result = run(_args(tmp_path, "--apply", "--incremental", "--limit", "3", "--batch-size", "3"),
                 factory, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 2
    assert result.attempts == 3
    assert result.failed == [3]
    assert result.stopped_because == "limit reached"
    with factory() as db:
        done = set(db.scalars(select(ParagraphCitationStatus.source_case_id)))
    assert {1, 2}.issubset(done) and 3 not in done


def test_incremental_limit_counts_current_explicit_ids(factory, tmp_path):
    with factory() as db:
        from backend.paragraph_cited_by_db import compute_source_edges, write_source_edges

        edges, _ = compute_source_edges(db, 2)
        write_source_edges(db, 2, edges)
        db.commit()

    result = run(_args(tmp_path, "--apply", "--incremental", "--limit", "2", "--case-ids", "2", "3", "4", "--batch-size", "5"),
                 factory, sleep=lambda s: None, log=lambda m: None)
    assert result.processed == 1
    assert result.attempts == 2
    assert result.failed == []
    assert result.stopped_because == "limit reached"
    with factory() as db:
        done = set(db.scalars(select(ParagraphCitationStatus.source_case_id)))
    assert {2, 3}.issubset(done) and 4 not in done
