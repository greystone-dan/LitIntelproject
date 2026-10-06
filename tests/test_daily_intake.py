"""Tests for the daily intake job (scripts/daily_intake.py).

Offline tests cover the pure logic and the HTTP handling with a mock transport.
The database tests use a throwaway court/IMM-year so they never touch real rows,
and are skipped when Postgres is not reachable.
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from scripts import daily_intake


def test_imm_year_number_parses_and_rejects():
    assert daily_intake.imm_year_number("IMM-1234-26") == (26, 1234)
    assert daily_intake.imm_year_number(" imm-5-09 ") == (9, 5)
    assert daily_intake.imm_year_number("IMM-1234-2026") is None
    assert daily_intake.imm_year_number(None) is None


def test_is_missing_file_needs_no_rows_and_no_style():
    assert daily_intake.is_missing_file({"entries_json": [], "style_of_cause": None})
    assert not daily_intake.is_missing_file({"entries_json": [], "style_of_cause": "A v. B"})
    assert not daily_intake.is_missing_file({"entries_json": [{"entry": "x"}], "style_of_cause": None})


def test_parse_args_defaults_and_guards():
    args = daily_intake.parse_args([])
    assert args.courts == ["FC", "FCA", "SCC"]
    assert args.max_cases == 200 and args.dry_run is False
    assert args.fc_delay_ms >= 2000
    with pytest.raises(SystemExit):
        daily_intake.parse_args(["--fc-delay-ms", "500"])
    with pytest.raises(SystemExit):
        daily_intake.parse_args(["--max-cases", "0"])


def test_budget_expires():
    budget = daily_intake.Budget(max_minutes=0)
    with pytest.raises(daily_intake.BudgetExceeded):
        budget.check()


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


def test_probe_partition_reads_linked_headers():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "HEAD"
        return httpx.Response(
            302,
            headers={"x-linked-etag": '"abc123"', "x-linked-size": "42", "x-repo-commit": "deadbeef"},
        )

    info = daily_intake.probe_partition(_client(handler), "FC")
    assert info == {"etag": "abc123", "size": 42, "commit": "deadbeef"}


def test_probe_partition_errors_on_bad_status_or_missing_etag():
    with pytest.raises(RuntimeError):
        daily_intake.probe_partition(_client(lambda r: httpx.Response(404)), "FC")
    with pytest.raises(RuntimeError):
        daily_intake.probe_partition(_client(lambda r: httpx.Response(302)), "FC")


def test_download_partition_verifies_hash_and_reuses_file(tmp_path: Path):
    body = b"parquet-bytes" * 100
    etag = hashlib.sha256(body).hexdigest()
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(200, content=body)

    info = {"etag": etag, "size": len(body), "commit": None}
    budget = daily_intake.Budget(5)
    first = daily_intake.download_partition(_client(handler), "FC", info, tmp_path, budget)
    assert first.read_bytes() == body and calls["n"] == 1
    again = daily_intake.download_partition(_client(handler), "FC", info, tmp_path, budget)
    assert again == first and calls["n"] == 1  # reused, no second download

    bad = {"etag": "0" * 64, "size": len(body), "commit": None}
    with pytest.raises(RuntimeError, match="SHA-256"):
        daily_intake.download_partition(_client(handler), "FCA", bad, tmp_path, budget)
    assert not list(tmp_path.glob("FCA-*"))  # no partial or bad file left behind


def test_download_partition_removes_older_partition_for_same_court(tmp_path: Path):
    old = tmp_path / "FC-11111111.parquet"
    old.write_bytes(b"old")
    body = b"new"
    info = {"etag": hashlib.sha256(body).hexdigest(), "size": None, "commit": None}
    daily_intake.download_partition(
        _client(lambda r: httpx.Response(200, content=body)), "FC", info, tmp_path, daily_intake.Budget(5)
    )
    assert not old.exists()


def _write_parquet(path: Path, rows: list[dict]) -> None:
    pq.write_table(pa.Table.from_pylist(rows), path)


def test_iter_candidate_records_filters_court_and_cutoff(tmp_path: Path):
    path = tmp_path / "x.parquet"
    _write_parquet(
        path,
        [
            {"dataset": "FC", "citation_en": "2026 FC 1", "document_date_en": "2026-01-10", "document_date_fr": None, "unofficial_text_en": "a"},
            {"dataset": "FC", "citation_en": "2026 FC 2", "document_date_en": "2026-03-10", "document_date_fr": None, "unofficial_text_en": "b"},
            {"dataset": "FCA", "citation_en": "2026 FCA 1", "document_date_en": "2026-03-11", "document_date_fr": None, "unofficial_text_en": "c"},
            {"dataset": "FC", "citation_en": None, "document_date_en": None, "document_date_fr": "2026-03-12", "unofficial_text_en": "d"},
            {"dataset": "FC", "citation_en": "no date", "document_date_en": None, "document_date_fr": None, "unofficial_text_en": "e"},
        ],
    )
    got = [r["unofficial_text_en"] for r in daily_intake.iter_candidate_records(path, "FC", date(2026, 2, 1))]
    assert got == ["b", "d"]
    everything = [r["unofficial_text_en"] for r in daily_intake.iter_candidate_records(path, "FC", None)]
    assert everything == ["a", "b", "d", "e"]


# ---------------------------------------------------------------------------
# Database-backed tests (skipped without Postgres)
# ---------------------------------------------------------------------------

TEST_COURT = "ZZTEST"
TEST_YEAR = 97  # a two-digit year no real IMM file uses


@pytest.fixture
def clean_db(requires_postgres):
    from sqlalchemy import delete

    from backend.database import (
        Case,
        CaseSource,
        FCActivityCase,
        IngestionRun,
        SessionLocal,
        init_db,
    )

    init_db()

    def wipe() -> None:
        with SessionLocal() as db:
            ids = [row for row in db.scalars(Case.__table__.select().with_only_columns(Case.id).where(Case.court == TEST_COURT))]
            if ids:
                db.execute(delete(CaseSource).where(CaseSource.case_id.in_(ids)))
                db.execute(delete(Case).where(Case.id.in_(ids)))
            db.execute(
                delete(FCActivityCase).where(
                    FCActivityCase.citation.like(f"IMM-%-{TEST_YEAR}") | FCActivityCase.source_key.like("t-%")
                )
            )
            db.execute(delete(IngestionRun).where(IngestionRun.source_name == "daily_intake_test"))
            db.commit()

    wipe()
    yield
    wipe()


def _record(n: int, day: str) -> dict:
    return {
        "dataset": TEST_COURT,
        "citation_en": f"2026 {TEST_COURT} {n}",
        "name_en": f"Test v. Test {n}",
        "document_date_en": day,
        "unofficial_text_en": f"Reasons for judgment number {n}. The application is dismissed.",
    }


def test_import_new_cases_creates_once_and_skips_existing(clean_db, tmp_path: Path):
    from sqlalchemy import func, select

    from backend.database import Case, SessionLocal

    path = tmp_path / "p.parquet"
    _write_parquet(path, [_record(1, "2026-05-01"), _record(2, "2026-05-02"), _record(3, "2026-05-03")])
    budget = daily_intake.Budget(5)

    dry = daily_intake.import_new_cases(TEST_COURT, path, cutoff=None, remaining=10, dry_run=True, budget=budget)
    assert dry["created"] == 3 and dry["case_ids"] == []
    with SessionLocal() as db:
        assert db.scalar(select(func.count()).select_from(Case).where(Case.court == TEST_COURT)) == 0

    real = daily_intake.import_new_cases(TEST_COURT, path, cutoff=None, remaining=2, dry_run=False, budget=budget)
    assert real["created"] == 2 and real["capped"] is True and len(real["case_ids"]) == 2

    again = daily_intake.import_new_cases(TEST_COURT, path, cutoff=None, remaining=10, dry_run=False, budget=budget)
    assert again["created"] == 1 and again["already_present"] == 2  # idempotent; the capped one arrives now

    with SessionLocal() as db:
        assert db.scalar(select(func.count()).select_from(Case).where(Case.court == TEST_COURT)) == 3
        assert db.scalar(select(func.max(Case.date)).where(Case.court == TEST_COURT)) is not None


def test_process_new_cases_runs_deterministic_layers(clean_db, tmp_path: Path):
    from sqlalchemy import select

    from backend.database import Case, CaseChunk, SessionLocal

    path = tmp_path / "p.parquet"
    _write_parquet(path, [_record(7, "2026-05-01")])
    budget = daily_intake.Budget(5)
    counts = daily_intake.import_new_cases(TEST_COURT, path, cutoff=None, remaining=5, dry_run=False, budget=budget)
    result = daily_intake.process_new_cases(counts["case_ids"], budget)
    assert result == {"processed": 1, "failed": 0}
    with SessionLocal() as db:
        case = db.get(Case, counts["case_ids"][0])
        assert case.processing_status == "parsed"
        assert db.scalars(select(CaseChunk).where(CaseChunk.case_id == case.id)).first() is not None


def _fake_result(imm: str, entries: list[tuple[str, str, str]]) -> dict:
    return {
        "imm_number": imm,
        "style_of_cause": "DOE v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION",
        "fetched_at": datetime.now(timezone.utc),
        "entries_json": [
            {"re_no": str(i), "docno": str(i), "date": d, "entry": text} for i, (d, text, _x) in enumerate(entries, 1)
        ],
    }


def test_store_activity_is_idempotent_and_adds_only_new_entries(clean_db):
    from sqlalchemy import func, select

    from backend.database import FCActivityDocument, SessionLocal

    imm = f"IMM-1-{TEST_YEAR}"
    first = _fake_result(imm, [("2026-01-12", "Application for leave and judicial review filed", "")])
    with SessionLocal() as db:
        case, added = daily_intake.store_activity(db, imm, first)
        case_id = case.id
    assert added == 1

    with SessionLocal() as db:
        _, added_again = daily_intake.store_activity(db, imm, first)
    assert added_again == 0

    grown = _fake_result(
        imm,
        [
            ("2026-01-12", "Application for leave and judicial review filed", ""),
            ("2026-02-01", "Respondent's record filed", ""),
        ],
    )
    with SessionLocal() as db:
        same_case, added_new = daily_intake.store_activity(db, imm, grown)
        assert same_case.id == case_id and same_case.citation == imm
    assert added_new == 1
    with SessionLocal() as db:
        total = db.scalar(select(func.count()).select_from(FCActivityDocument).where(FCActivityDocument.case_id == case_id))
        assert total == 2


def test_highest_known_imm_reads_citation_and_payload(clean_db):
    from backend.database import FCActivityCase, SessionLocal

    with SessionLocal() as db:
        db.add(FCActivityCase(source_key="t-a", citation=f"IMM-40-{TEST_YEAR}", year=1997))
        db.add(FCActivityCase(source_key="t-b", citation=None, year=1997, raw_payload={"imm_number": f"IMM-55-{TEST_YEAR}"}))
        db.commit()
        assert daily_intake.highest_known_imm(db, TEST_YEAR) == 55
        assert daily_intake.highest_known_imm(db, 96) == 0


def test_run_log_writes_started_then_finished(clean_db):
    from backend.database import IngestionRun, SessionLocal

    log = daily_intake.RunLog(enabled=True, dry_run=False)
    log.start({"x": 1})
    with SessionLocal() as db:
        row = db.get(IngestionRun, log.run_id)
        assert row.status == "started" and row.finished_at is None
        row.source_name = "daily_intake_test"  # lets the fixture clean it up
        db.commit()
    log.finish("completed", 5, 2, 1, 0, {"ok": True})
    with SessionLocal() as db:
        row = db.get(IngestionRun, log.run_id)
        assert row.status == "completed" and row.finished_at is not None
        assert (row.records_seen, row.records_ingested, row.records_updated, row.records_failed) == (5, 2, 1, 0)


def test_dry_run_writes_no_run_row():
    log = daily_intake.RunLog(enabled=False, dry_run=True)
    log.start({})
    assert log.run_id is None
    log.finish("completed", 0, 0, 0, 0, {})  # must be a no-op, not an error


def _activity_args(**overrides):
    args = daily_intake.parse_args(["--skip-cases", "--fc-delay-ms", "2000"])
    args.today = date(1997, 5, 1)  # suffix 97: never touches real IMM years
    args.refresh_cap = 0
    for key, value in overrides.items():
        setattr(args, key, value)
    return args


def _patch_registry(monkeypatch, existing: set[str], calls: list[str]):
    import scripts.fetch_fc_procedural_history as fetcher

    def fake_process_imm(client, imm, request_budget=None):
        calls.append(imm)
        if request_budget is not None:
            request_budget.spend()
            request_budget.spend()
        if imm not in existing:
            return {"imm_number": imm, "style_of_cause": None, "entries_json": [], "error": "no_re_data",
                    "fetched_at": datetime.now(timezone.utc)}
        return {
            "imm_number": imm,
            "style_of_cause": "DOE v. MCI",
            "fetched_at": datetime.now(timezone.utc),
            "entries_json": [
                {"re_no": "1", "docno": "1", "date": "1997-04-20", "entry": "Application for leave and judicial review filed"},
                {"re_no": "2", "docno": "2", "date": "1997-04-21", "entry": "Notice of appearance filed"},
            ],
        }

    monkeypatch.setattr(fetcher, "process_imm", fake_process_imm)
    monkeypatch.setattr(daily_intake, "polite_pause", lambda *_a: None)
    monkeypatch.setattr(daily_intake, "build_fc_client", lambda: httpx.Client())


def _seed_known(number: int) -> None:
    from backend.database import FCActivityCase, SessionLocal

    with SessionLocal() as db:
        db.add(FCActivityCase(source_key=f"t-seed-{number}", citation=f"IMM-{number}-{TEST_YEAR}", year=1997))
        db.commit()


def test_activity_stage_walks_forward_stores_and_classifies(clean_db, monkeypatch):
    from sqlalchemy import select

    from backend.database import FCActivityCase, FCActivitySummary, SessionLocal

    _seed_known(40)
    calls: list[str] = []
    _patch_registry(monkeypatch, {f"IMM-41-{TEST_YEAR}", f"IMM-42-{TEST_YEAR}", f"IMM-47-{TEST_YEAR}"}, calls)

    result = daily_intake.run_activity_stage(_activity_args(miss_streak=3), daily_intake.Budget(5))

    # 41, 42 found; 43-45 are three misses in a row, so 47 is never reached.
    assert result["new_files"] == [f"IMM-41-{TEST_YEAR}", f"IMM-42-{TEST_YEAR}"]
    assert calls == [f"IMM-{n}-{TEST_YEAR}" for n in (41, 42, 43, 44, 45)]
    assert result["new_documents"] == 4 and result["classified"] == 2 and result["errors"] == []
    with SessionLocal() as db:
        stored = db.scalar(select(FCActivityCase).where(FCActivityCase.citation == f"IMM-41-{TEST_YEAR}"))
        assert stored.case_name == "DOE v. MCI" and str(stored.date_filed) == "1997-04-20"
        assert db.get(FCActivitySummary, stored.id) is not None

    # A second run starts after 42, finds nothing new and adds nothing.
    calls.clear()
    again = daily_intake.run_activity_stage(_activity_args(miss_streak=2), daily_intake.Budget(5))
    assert calls == [f"IMM-43-{TEST_YEAR}", f"IMM-44-{TEST_YEAR}"]
    assert again["new_files"] == [] and again["new_documents"] == 0


def test_activity_stage_stops_cleanly_at_request_cap(clean_db, monkeypatch):
    _seed_known(10)
    calls: list[str] = []
    existing = {f"IMM-{n}-{TEST_YEAR}" for n in range(11, 30)}
    _patch_registry(monkeypatch, existing, calls)
    result = daily_intake.run_activity_stage(_activity_args(max_fc_requests=6), daily_intake.Budget(5))
    assert len(calls) == 3 and len(result["new_files"]) == 3  # 6 requests = 3 files
    assert result["errors"] == [] and "request cap" in result["stopped_by"]


def test_activity_stage_dry_run_and_empty_year_guard(clean_db, monkeypatch):
    from sqlalchemy import select

    from backend.database import FCActivityCase, SessionLocal

    calls: list[str] = []
    _patch_registry(monkeypatch, {f"IMM-1-{TEST_YEAR}"}, calls)
    guarded = daily_intake.run_activity_stage(_activity_args(), daily_intake.Budget(5))
    assert calls == [] and "refusing to sweep" in guarded["errors"][0]

    _seed_known(5)
    _patch_registry(monkeypatch, {f"IMM-6-{TEST_YEAR}"}, calls)
    dry = daily_intake.run_activity_stage(_activity_args(dry_run=True, miss_streak=2), daily_intake.Budget(5))
    assert dry["new_files"] == [f"IMM-6-{TEST_YEAR}"]
    with SessionLocal() as db:
        assert db.scalar(select(FCActivityCase).where(FCActivityCase.citation == f"IMM-6-{TEST_YEAR}")) is None
