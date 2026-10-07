#!/usr/bin/env python3
"""Daily intake: new decisions from A2AJ, then new Federal Court (IMM) activity records.

One run does, in order:

1. Cases. For each court (default FC, FCA, SCC) it asks Hugging Face whether the
   A2AJ partition has changed since the last completed run (one HEAD request,
   no download). Only if it changed does it download the partition, import
   decisions newer than what the library holds (minus a small overlap), skip
   anything already present, and run the deterministic processing layers
   (chunks, metadata, outcome, citations, statutes, tags) on each new case.
2. FC activity. New IMM files are found by walking forward from the highest
   IMM number already stored for the current year, fetching each from the
   Federal Court registry until several numbers in a row do not exist. A few
   recently active files are also re-fetched so their newest docket entries
   arrive. Touched files are re-classified with the existing rule classifier.

Everything is deterministic: no AI or model calls. Each run writes one row to
ingestion_runs (started, then finished with finished_at and counts). Caps keep
a run small: --max-cases, --max-fc-requests, --max-minutes. Re-running is safe:
existing cases and docket entries are never duplicated.

Usage:
  python scripts/daily_intake.py --dry-run          # report only, writes nothing
  python scripts/daily_intake.py                    # the real daily run
  python scripts/daily_intake.py --skip-activity    # cases only
  python scripts/daily_intake.py --skip-cases       # FC activity only
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import httpx  # noqa: E402
from sqlalchemy import func, select, text  # noqa: E402

from backend.database import (  # noqa: E402
    Case,
    FCActivityCase,
    FCActivityDocument,
    IngestionRun,
    SessionLocal,
)

logger = logging.getLogger("daily_intake")

RUN_SOURCE_TYPE = "daily_intake"
RUN_SOURCE_NAME = "scheduled_daily"
ADVISORY_LOCK_KEY = 74_100_261  # arbitrary constant; one daily run at a time

A2AJ_PARTITION_URL = "https://huggingface.co/datasets/a2aj/canadian-case-law/resolve/main/{court}/train.parquet"
DEFAULT_COURTS = ("FC", "FCA", "SCC")
DEFAULT_DOWNLOAD_DIR = PROJECT_ROOT / "data" / "raw" / "a2aj" / "daily"
USER_AGENT = "iLit-daily-intake/1.0 (+https://www.ilit.ca; research use)"
IMM_PATTERN = re.compile(r"^IMM-(\d+)-(\d{2})$")


class BudgetExceeded(RuntimeError):
    """Raised when a run reaches its time cap."""


class RequestCapReached(BudgetExceeded):
    """Raised when the per-run registry request cap is reached."""


@dataclass
class Budget:
    """Wall-clock deadline for one run."""

    max_minutes: float
    started: float = field(default_factory=time.monotonic)

    def expired(self) -> bool:
        return (time.monotonic() - self.started) > self.max_minutes * 60

    def check(self) -> None:
        if self.expired():
            raise BudgetExceeded(f"time budget of {self.max_minutes} minutes used up")


# ---------------------------------------------------------------------------
# Run log (ingestion_runs)
# ---------------------------------------------------------------------------


class RunLog:
    """One ingestion_runs row per run: created as 'started', closed with finished_at."""

    def __init__(self, enabled: bool, dry_run: bool) -> None:
        self.enabled = enabled
        self.run_id: int | None = None
        self.dry_run = dry_run

    def start(self, metadata: dict[str, Any]) -> None:
        if not self.enabled:
            return
        with SessionLocal() as db:
            row = IngestionRun(
                source_type=RUN_SOURCE_TYPE,
                source_name=RUN_SOURCE_NAME,
                run_type="daily_intake",
                status="started",
                metadata_json=metadata,
            )
            db.add(row)
            db.commit()
            self.run_id = row.id

    def finish(self, status: str, seen: int, ingested: int, updated: int, failed: int, metadata: dict[str, Any]) -> None:
        if not self.enabled or self.run_id is None:
            return
        with SessionLocal() as db:
            row = db.get(IngestionRun, self.run_id)
            if row is None:
                return
            row.status = status
            row.finished_at = datetime.now(timezone.utc)
            row.records_seen = seen
            row.records_ingested = ingested
            row.records_updated = updated
            row.records_failed = failed
            row.metadata_json = metadata
            db.commit()


def last_completed_run(db) -> IngestionRun | None:
    return db.scalar(
        select(IngestionRun)
        .where(
            IngestionRun.source_type == RUN_SOURCE_TYPE,
            IngestionRun.run_type == "daily_intake",
            IngestionRun.status.in_(("completed", "completed_with_errors")),
            IngestionRun.finished_at.is_not(None),
        )
        .order_by(IngestionRun.id.desc())
        .limit(1)
    )


def previous_partition_state(db, court: str, lookback: int = 60) -> dict[str, Any] | None:
    """The partition fingerprint from the latest run that fully consumed this court."""
    runs = db.scalars(
        select(IngestionRun)
        .where(
            IngestionRun.source_type == RUN_SOURCE_TYPE,
            IngestionRun.status.in_(("completed", "completed_with_errors")),
        )
        .order_by(IngestionRun.id.desc())
        .limit(lookback)
    )
    for run in runs:
        state = ((run.metadata_json or {}).get("cases") or {}).get("courts", {}).get(court)
        if state and state.get("fully_consumed") and state.get("etag"):
            return state
    return None


# ---------------------------------------------------------------------------
# Stage 1: new decisions from A2AJ
# ---------------------------------------------------------------------------


def probe_partition(client: httpx.Client, court: str) -> dict[str, Any]:
    """HEAD the Hugging Face partition. Returns etag/size/commit without downloading."""
    response = client.head(A2AJ_PARTITION_URL.format(court=court), follow_redirects=False, timeout=30)
    if response.status_code not in (200, 302):
        raise RuntimeError(f"HTTP {response.status_code} probing {court} partition")
    etag = (response.headers.get("x-linked-etag") or response.headers.get("etag") or "").strip('"')
    size = response.headers.get("x-linked-size") or response.headers.get("content-length")
    if not etag:
        raise RuntimeError(f"no etag returned for {court} partition")
    return {
        "etag": etag,
        "size": int(size) if size and size.isdigit() else None,
        "commit": response.headers.get("x-repo-commit"),
    }


def download_partition(client: httpx.Client, court: str, info: dict[str, Any], download_dir: Path, budget: Budget) -> Path:
    """Download one partition to <dir>/<court>-<etag8>.parquet, reusing a complete earlier download."""
    download_dir.mkdir(parents=True, exist_ok=True)
    target = download_dir / f"{court}-{info['etag'][:8]}.parquet"
    if target.exists() and (info["size"] is None or target.stat().st_size == info["size"]):
        logger.info("%s: reusing earlier download %s", court, target.name)
        return target
    partial = target.with_suffix(".part")
    digest = hashlib.sha256()
    with client.stream("GET", A2AJ_PARTITION_URL.format(court=court), follow_redirects=True, timeout=120) as response:
        response.raise_for_status()
        with partial.open("wb") as handle:
            for chunk in response.iter_bytes(1024 * 1024):
                handle.write(chunk)
                digest.update(chunk)
                budget.check()
    if info["size"] is not None and partial.stat().st_size != info["size"]:
        partial.unlink(missing_ok=True)
        raise RuntimeError(f"{court}: downloaded size does not match upstream size")
    if re.fullmatch(r"[0-9a-f]{64}", info["etag"]) and digest.hexdigest() != info["etag"]:
        partial.unlink(missing_ok=True)
        raise RuntimeError(f"{court}: SHA-256 of download does not match upstream")
    partial.replace(target)
    for older in download_dir.glob(f"{court}-*.parquet"):
        if older != target:
            older.unlink(missing_ok=True)
    return target


def court_cutoff(db, court: str, overlap_days: int) -> date | None:
    """Only decisions after (latest stored decision - overlap) are candidates."""
    latest = db.scalar(select(func.max(Case.date)).where(Case.court == court))
    if latest is None:
        return None
    latest_day = latest.date() if isinstance(latest, datetime) else latest
    return latest_day - timedelta(days=overlap_days)


def iter_candidate_records(path: Path, court: str, cutoff: date | None) -> Iterator[dict[str, Any]]:
    """Yield parquet rows for `court` dated after `cutoff`, reading dates before text."""
    import pyarrow.parquet as pq

    from scripts.ingest_a2aj_parquet import parse_date

    parquet = pq.ParquetFile(path)
    for batch in parquet.iter_batches(batch_size=256):
        names = set(batch.schema.names)
        keep: list[int] = []
        datasets = batch.column("dataset").to_pylist() if "dataset" in names else [court] * batch.num_rows
        dates_en = batch.column("document_date_en").to_pylist() if "document_date_en" in names else [None] * batch.num_rows
        dates_fr = batch.column("document_date_fr").to_pylist() if "document_date_fr" in names else [None] * batch.num_rows
        for index in range(batch.num_rows):
            if datasets[index] != court:
                continue
            try:
                decided = parse_date(dates_en[index] or dates_fr[index])
            except ValueError:
                decided = None
            if cutoff is not None and (decided is None or decided <= cutoff):
                continue
            keep.append(index)
        if keep:
            yield from batch.take(keep).to_pylist()


def import_new_cases(
    court: str,
    path: Path,
    *,
    cutoff: date | None,
    remaining: int,
    dry_run: bool,
    budget: Budget,
) -> dict[str, Any]:
    """Create decisions not yet in the library. Existing cases are skipped, never enriched."""
    from backend.ingestion import _find_existing_case, merge_case_record
    from scripts.ingest_a2aj_parquet import build_case

    counts = {"candidates": 0, "invalid": 0, "already_present": 0, "created": 0, "failed": 0, "capped": False}
    created_ids: list[int] = []
    sample: list[str] = []
    with SessionLocal() as db:
        for record in iter_candidate_records(path, court, cutoff):
            budget.check()
            counts["candidates"] += 1
            case = build_case(record)
            if case is None:
                counts["invalid"] += 1
                continue
            if _find_existing_case(db, case) is not None:
                counts["already_present"] += 1
                continue
            if counts["created"] >= remaining:
                counts["capped"] = True
                break
            if len(sample) < 10:
                sample.append(case.citation or case.title)
            if dry_run:
                counts["created"] += 1
                continue
            try:
                stored, action, _changed = merge_case_record(db, case)
            except Exception as exc:  # one bad record must not stop the run
                db.rollback()
                counts["failed"] += 1
                logger.warning("%s: could not import %s: %s", court, case.citation, exc)
                continue
            if action == "created":
                counts["created"] += 1
                created_ids.append(stored.id)
            else:
                counts["already_present"] += 1
    counts["sample"] = sample
    counts["case_ids"] = created_ids
    return counts


def process_new_cases(case_ids: list[int], budget: Budget) -> dict[str, int]:
    """Run the deterministic processing layers on each new case, isolating failures."""
    from backend.case_processing import STAGE_ORDER, process_case_in_five_layers

    done = failed = 0
    with SessionLocal() as db:
        for case_id in case_ids:
            budget.check()
            try:
                process_case_in_five_layers(db, case_id, stage_order=list(STAGE_ORDER))
                case = db.get(Case, case_id)
                if case is not None and case.processing_status == "raw":
                    case.processing_status = "parsed"
                db.commit()
                done += 1
            except Exception as exc:
                db.rollback()
                failed += 1
                logger.warning("processing case %s failed: %s", case_id, exc)
    return {"processed": done, "failed": failed}


def run_cases_stage(args: argparse.Namespace, budget: Budget) -> dict[str, Any]:
    result: dict[str, Any] = {"courts": {}, "created": 0, "failed": 0, "seen": 0, "errors": []}
    remaining = args.max_cases
    headers = {"User-Agent": USER_AGENT}
    with httpx.Client(headers=headers) as client:
        for court in args.courts:
            summary: dict[str, Any] = {}
            result["courts"][court] = summary
            try:
                budget.check()
                info = probe_partition(client, court)
                summary.update(info)
                with SessionLocal() as db:
                    previous = previous_partition_state(db, court)
                    cutoff = court_cutoff(db, court, args.overlap_days)
                summary["cutoff"] = cutoff.isoformat() if cutoff else None
                if previous and previous.get("etag") == info["etag"] and not args.force_check:
                    summary["action"] = "unchanged_upstream"
                    summary["fully_consumed"] = True
                    logger.info("%s: upstream partition unchanged since last run; nothing to do", court)
                    continue
                if remaining <= 0:
                    summary["action"] = "skipped_cap_reached"
                    summary["fully_consumed"] = False
                    continue
                if args.dry_run and not args.download_in_dry_run:
                    summary["action"] = "would_download"
                    summary["fully_consumed"] = False
                    logger.info("%s: upstream changed (%s bytes); dry run does not download", court, info["size"])
                    continue
                path = download_partition(client, court, info, args.download_dir, budget)
                counts = import_new_cases(
                    court, path, cutoff=cutoff, remaining=remaining, dry_run=args.dry_run, budget=budget
                )
                summary.update({key: counts[key] for key in ("candidates", "invalid", "already_present", "created", "failed", "capped", "sample")})
                result["seen"] += counts["candidates"]
                result["created"] += counts["created"]
                result["failed"] += counts["failed"]
                remaining -= counts["created"]
                summary["action"] = "dry_run" if args.dry_run else "imported"
                summary["fully_consumed"] = (not counts["capped"]) and counts["failed"] == 0 and not args.dry_run
                if counts["case_ids"]:
                    summary["processing"] = process_new_cases(counts["case_ids"], budget)
                    result["failed"] += summary["processing"]["failed"]
                if summary["fully_consumed"] and not args.keep_downloads:
                    path.unlink(missing_ok=True)
                logger.info("%s: %s", court, {k: v for k, v in summary.items() if k != "sample"})
            except BudgetExceeded as exc:
                summary["action"] = "stopped_budget"
                summary["fully_consumed"] = False
                result["errors"].append(f"{court}: {exc}")
                break
            except Exception as exc:
                summary["action"] = "error"
                summary["fully_consumed"] = False
                result["errors"].append(f"{court}: {exc}")
                logger.exception("%s: cases stage failed", court)
    return result


# ---------------------------------------------------------------------------
# Stage 2: FC activity records for newly filed IMM files
# ---------------------------------------------------------------------------


def imm_year_number(imm: str | None) -> tuple[int, int] | None:
    match = IMM_PATTERN.match((imm or "").strip().upper())
    if not match:
        return None
    return int(match.group(2)), int(match.group(1))


def highest_known_imm(db, year_suffix: int) -> int:
    """Highest IMM sequence number already stored for a two-digit year suffix.

    Files from 2023 on keep the docket number only in raw_payload ('imm_number'); the citation
    column is blank, and date_filed is the latest activity date, so the docket-year suffix is
    the only reliable filing year. The year column is used just to narrow the scan.
    """
    suffix = f"{year_suffix:02d}"
    pattern = rf"^IMM-[0-9]+-{suffix}$"
    full_year = 2000 + year_suffix if year_suffix <= 50 else 1900 + year_suffix
    best = 0
    queries = (
        "SELECT max(split_part(citation, '-', 2)::int) FROM fc_activity_cases "
        "WHERE year IN (:y, :y1) AND citation ~ :p",
        "SELECT max(split_part(raw_payload->>'imm_number', '-', 2)::int) FROM fc_activity_cases "
        "WHERE year IN (:y, :y1) AND raw_payload->>'imm_number' ~ :p",
        # Empty probe rows (no style of cause) exist in fc_procedural_history; they are not real files.
        "SELECT max(split_part(imm_number, '-', 2)::int) FROM fc_procedural_history "
        "WHERE imm_number ~ :p AND coalesce(style_of_cause, '') <> ''",
    )
    for query in queries:
        value = db.execute(text(query), {"p": pattern, "y": full_year, "y1": full_year + 1}).scalar()
        if value:
            best = max(best, int(value))
    return best


def is_missing_file(result: dict[str, Any]) -> bool:
    """A number the registry has no file for: no docket rows and no style of cause."""
    return not (result.get("entries_json") or []) and not result.get("style_of_cause")


def build_fc_client() -> httpx.Client:
    import os

    from scripts.fetch_fc_procedural_history import HEADERS

    headers = dict(HEADERS)
    # Identify ourselves by default. If the registry rejects that, the operator can set
    # FC_ACTIVITY_USER_AGENT in .env; the choice stays visible and deliberate.
    headers["User-Agent"] = os.getenv("FC_ACTIVITY_USER_AGENT") or USER_AGENT
    return httpx.Client(headers=headers, follow_redirects=True)


def polite_pause(delay_ms: int, jitter_ms: int) -> None:
    import random

    time.sleep((delay_ms + random.randint(0, jitter_ms)) / 1000)


def store_activity(db, imm: str, result: dict[str, Any]) -> tuple[FCActivityCase, int]:
    """Create or update the fc_activity case for this IMM number and add only new docket entries."""
    from scripts.fetch_fc_procedural_history import _activity_hash, _activity_year, _json_safe, _parse_date

    legacy_key = _activity_hash("fc-procedural-endpoint", imm)
    case = db.scalar(select(FCActivityCase).where(FCActivityCase.citation == imm))
    if case is None:
        case = db.scalar(select(FCActivityCase).where(FCActivityCase.source_key == legacy_key))
        if case is not None and case.citation is None:
            case.citation = imm
    entry_dates = [d for d in (_parse_date(str(e.get("date") or "")) for e in result.get("entries_json") or []) if d]
    if case is None:
        case = FCActivityCase(
            source_key=_activity_hash("fc-daily-intake", imm),
            citation=imm,
            year=_activity_year(imm),
            case_name=result.get("style_of_cause"),
            date_filed=min(entry_dates) if entry_dates else None,
            source_type="fc_registry_live",
            source_name="Federal Court registry (daily intake)",
            source_id=imm,
            scraped_timestamp=result.get("fetched_at"),
            raw_payload=_json_safe({**result, "imm_number": imm}),
        )
        db.add(case)
        db.flush()
    else:
        case.case_name = result.get("style_of_cause") or case.case_name
        case.scraped_timestamp = result.get("fetched_at")
        case.raw_payload = _json_safe({**result, "imm_number": imm})
        if case.date_filed is None and entry_dates:
            case.date_filed = min(entry_dates)

    added = 0
    seen_identities: set[tuple[str, str]] = set()
    for entry in result.get("entries_json") or []:
        entry_text = str(entry.get("entry") or "").strip()
        entry_date = entry.get("date") or None
        re_no = str(entry.get("re_no") or "").strip() or None
        docno = str(entry.get("docno") or "").strip() or None
        if not entry_text and not entry_date:
            continue
        entry_hash = _activity_hash(imm, re_no, docno, entry_date, entry_text)
        if re_no is not None and docno is not None:
            if (re_no, docno) in seen_identities:
                continue
            seen_identities.add((re_no, docno))
            if db.scalar(
                select(FCActivityDocument.id).where(
                    FCActivityDocument.case_id == case.id,
                    FCActivityDocument.re_no == re_no,
                    FCActivityDocument.docno == docno,
                )
            ):
                continue
        if db.scalar(
            select(FCActivityDocument.id).where(
                FCActivityDocument.case_id == case.id, FCActivityDocument.entry_hash == entry_hash
            )
        ):
            continue
        db.add(
            FCActivityDocument(
                case_id=case.id,
                re_no=re_no,
                docno=docno,
                doc_dt=_parse_date(str(entry_date)) if entry_date else None,
                recorded_entry=entry_text or None,
                entry_hash=entry_hash,
                raw_document={"imm_number": imm, **entry},
            )
        )
        added += 1
    db.commit()
    return case, added


def refresh_candidates(db, limit: int, min_age_days: int, active_within_days: int, today: date) -> list[str]:
    """Recently active files not fetched for a while, oldest fetch first, as IMM numbers."""
    if limit <= 0:
        return []
    # Pick candidate cases first from cheap columns (year, scrape time), then test each for a recent
    # docket entry with an indexed EXISTS, stopping at the limit. Never aggregate the whole documents
    # table (3.6M rows) and never read raw_payload for more than the chosen few.
    params = {
        "active_since": today - timedelta(days=active_within_days),
        "stale_before": datetime.now(timezone.utc) - timedelta(days=min_age_days),
        "limit": limit,
        "min_year": today.year - 1,
    }
    chosen = [
        row[0]
        for row in db.execute(
            text(
                """
                SELECT c.id
                FROM fc_activity_cases c
                WHERE c.year >= :min_year
                  AND (c.scraped_timestamp IS NULL OR c.scraped_timestamp < :stale_before)
                  AND EXISTS (
                      SELECT 1 FROM fc_activity_documents d
                      WHERE d.case_id = c.id AND d.doc_dt >= :active_since
                  )
                ORDER BY c.scraped_timestamp NULLS FIRST, c.id
                LIMIT :limit
                """
            ),
            params,
        )
    ]
    if not chosen:
        return []
    rows = db.execute(
        text(
            "SELECT COALESCE(citation, raw_payload->>'imm_number') FROM fc_activity_cases "
            "WHERE id = ANY(:ids) ORDER BY scraped_timestamp NULLS FIRST, id"
        ),
        {"ids": chosen},
    )
    return [row[0] for row in rows if row[0] and IMM_PATTERN.match(row[0].strip().upper())]


def classify_touched(case_ids: list[int]) -> int:
    """Re-run the existing rule classifier on files whose docket changed."""
    if not case_ids:
        return 0
    from scripts.classify_fc_activity import classify_cases, persist_report

    with SessionLocal() as db:
        cases = list(db.scalars(select(FCActivityCase).where(FCActivityCase.id.in_(case_ids))))
        documents: dict[int, list[FCActivityDocument]] = {case.id: [] for case in cases}
        for document in db.scalars(
            select(FCActivityDocument)
            .where(FCActivityDocument.case_id.in_(case_ids))
            .order_by(FCActivityDocument.case_id, FCActivityDocument.doc_dt, FCActivityDocument.id)
        ):
            documents[document.case_id].append(document)
        report = classify_cases(cases, documents)
    return persist_report(report, force=True)


def run_activity_stage(args: argparse.Namespace, budget: Budget) -> dict[str, Any]:
    from scripts.fetch_fc_procedural_history import RequestBudget, process_imm

    today = getattr(args, "today", None) or datetime.now(timezone.utc).date()  # tests pin the date
    result: dict[str, Any] = {
        "new_files": [],
        "refreshed": [],
        "new_documents": 0,
        "requests_used": 0,
        "classified": 0,
        "seen": 0,
        "failed": 0,
        "errors": [],
    }
    years = [today.year % 100]
    if today.month == 1:
        years.append((today.year - 1) % 100)  # early-January stragglers from last year

    request_budget = RequestBudget(args.max_fc_requests)
    touched: list[int] = []
    try:
        with build_fc_client() as client:
            fetched_any = False

            def fetch(imm: str) -> dict[str, Any] | None:
                nonlocal fetched_any
                budget.check()
                if request_budget.used + 2 > request_budget.maximum:  # each file costs two requests
                    raise RequestCapReached(f"request cap of {request_budget.maximum} reached")
                if fetched_any:
                    polite_pause(args.fc_delay_ms, args.fc_jitter_ms)
                fetched_any = True
                return process_imm(client, imm, request_budget=request_budget)

            # New files: walk forward from the highest known number.
            for suffix in years:
                with SessionLocal() as db:
                    start = highest_known_imm(db, suffix)
                if start == 0 and not args.allow_sweep_from_one:
                    with SessionLocal() as db:
                        prior_year_known = highest_known_imm(db, (suffix - 1) % 100)
                    if prior_year_known == 0:
                        result["errors"].append(
                            f"No IMM files stored for 20{suffix:02d} or the year before; refusing to sweep from IMM-1. "
                            "Load the FC activity data first, or pass --allow-sweep-from-one."
                        )
                        continue
                misses = 0
                number = start
                while misses < args.miss_streak and len(result["new_files"]) < args.max_new_files:
                    number += 1
                    imm = f"IMM-{number}-{suffix:02d}"
                    outcome = fetch(imm)
                    result["seen"] += 1
                    if outcome is None or is_missing_file(outcome):
                        misses += 1
                        continue
                    misses = 0
                    if args.dry_run:
                        result["new_files"].append(imm)
                        continue
                    with SessionLocal() as db:
                        stored, added = store_activity(db, imm, outcome)
                        touched.append(stored.id)
                    result["new_files"].append(imm)
                    result["new_documents"] += added
                logger.info("FC activity: year %02d walked from IMM-%d, %d new file(s)", suffix, start + 1, len(result["new_files"]))

            # Refresh a few recently active files so new docket entries arrive.
            with SessionLocal() as db:
                refresh = refresh_candidates(db, args.refresh_cap, args.refresh_min_age_days, args.refresh_active_days, today)
            for imm in refresh:
                outcome = fetch(imm)
                result["seen"] += 1
                if outcome is None or is_missing_file(outcome):
                    continue
                if args.dry_run:
                    result["refreshed"].append(imm)
                    continue
                with SessionLocal() as db:
                    stored, added = store_activity(db, imm, outcome)
                if added:
                    touched.append(stored.id)
                    result["new_documents"] += added
                result["refreshed"].append(imm)
    except RequestCapReached as exc:
        result["stopped_by"] = str(exc)  # a normal stop, picked up again tomorrow
    except BudgetExceeded as exc:
        result["stopped_by"] = str(exc)
    except Exception as exc:
        result["failed"] += 1
        result["errors"].append(f"FC activity fetch failed: {exc}")
        logger.exception("FC activity stage failed")
    result["requests_used"] = request_budget.used
    if touched and not args.dry_run:
        try:
            result["classified"] = classify_touched(sorted(set(touched)))
        except Exception as exc:
            result["failed"] += 1
            result["errors"].append(f"classification failed: {exc}")
            logger.exception("FC activity classification failed")
    return result


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def acquire_run_lock(connection) -> bool:
    return bool(connection.execute(text("SELECT pg_try_advisory_lock(:k)"), {"k": ADVISORY_LOCK_KEY}).scalar())


def release_run_lock(connection) -> None:
    connection.execute(text("SELECT pg_advisory_unlock(:k)"), {"k": ADVISORY_LOCK_KEY})


def hours_since_last_run() -> float | None:
    with SessionLocal() as db:
        last = last_completed_run(db)
        if last is None or last.finished_at is None:
            return None
        finished = last.finished_at if last.finished_at.tzinfo else last.finished_at.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - finished).total_seconds() / 3600


def run(args: argparse.Namespace) -> int:
    budget = Budget(args.max_minutes)
    log = RunLog(enabled=not args.dry_run, dry_run=args.dry_run)

    from backend.database import engine

    with engine.connect() as lock_connection:
        if not acquire_run_lock(lock_connection):
            logger.warning("Another daily intake run is in progress; exiting")
            return 0
        try:
            elapsed = hours_since_last_run()
            if elapsed is not None and elapsed < args.min_hours_between_runs and not args.force and not args.dry_run:
                logger.info("Last completed run was %.1f hours ago (< %s); nothing to do. Use --force to override.", elapsed, args.min_hours_between_runs)
                return 0

            log.start({"dry_run": args.dry_run, "courts": list(args.courts), "max_cases": args.max_cases})
            summary: dict[str, Any] = {"dry_run": args.dry_run}
            seen = ingested = updated = failed = 0
            errors: list[str] = []
            try:
                if not args.skip_cases:
                    cases = run_cases_stage(args, budget)
                    summary["cases"] = cases
                    seen += cases["seen"]
                    ingested += cases["created"]
                    failed += cases["failed"]
                    errors += cases["errors"]
                if not args.skip_activity:
                    activity = run_activity_stage(args, budget)
                    summary["fc_activity"] = activity
                    seen += activity["seen"]
                    ingested += len(activity["new_files"])
                    updated += len(activity["refreshed"])
                    failed += activity["failed"]
                    errors += activity["errors"]
                status = "completed_with_errors" if (errors or failed) else "completed"
            except Exception as exc:
                logger.exception("Daily intake failed")
                errors.append(str(exc))
                status = "failed"
            summary["errors"] = errors
            summary["minutes"] = round((time.monotonic() - budget.started) / 60, 2)
            log.finish(status, seen, ingested, updated, failed, summary)
            logger.info("Daily intake %s: %s", status, {k: v for k, v in summary.items() if k not in ("cases", "fc_activity")})
            _print_report(summary)
            return 0 if status != "failed" else 1
        finally:
            release_run_lock(lock_connection)


def _print_report(summary: dict[str, Any]) -> None:
    prefix = "DRY RUN " if summary.get("dry_run") else ""
    for court, info in (summary.get("cases") or {}).get("courts", {}).items():
        print(
            f"{prefix}cases {court}: {info.get('action')} "
            f"candidates={info.get('candidates', 0)} new={info.get('created', 0)} "
            f"already_present={info.get('already_present', 0)} failed={info.get('failed', 0)}"
        )
        for citation in info.get("sample") or []:
            print(f"    {citation}")
    activity = summary.get("fc_activity")
    if activity is not None:
        print(
            f"{prefix}fc activity: new_files={len(activity['new_files'])} refreshed={len(activity['refreshed'])} "
            f"new_documents={activity['new_documents']} requests={activity['requests_used']} classified={activity['classified']}"
            + (f" (stopped: {activity['stopped_by']})" if activity.get("stopped_by") else "")
        )
        for imm in activity["new_files"][:20]:
            print(f"    {imm}")
    for error in summary.get("errors") or []:
        print(f"{prefix}error: {error}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Report what would happen; write nothing to the database")
    parser.add_argument("--force", action="store_true", help="Run even if a run completed recently")
    parser.add_argument("--min-hours-between-runs", type=float, default=20.0)
    parser.add_argument("--skip-cases", action="store_true")
    parser.add_argument("--skip-activity", action="store_true")
    parser.add_argument("--verbose", action="store_true")

    cases = parser.add_argument_group("cases")
    cases.add_argument("--courts", nargs="+", default=list(DEFAULT_COURTS), help="A2AJ court codes (default FC FCA SCC)")
    cases.add_argument("--max-cases", type=int, default=200, help="Cap on new cases per run")
    cases.add_argument("--overlap-days", type=int, default=30, help="Re-check this many days before the newest stored decision")
    cases.add_argument("--download-dir", type=Path, default=DEFAULT_DOWNLOAD_DIR)
    cases.add_argument("--keep-downloads", action="store_true")
    cases.add_argument("--force-check", action="store_true", help="Download and compare even if upstream looks unchanged")
    cases.add_argument("--download-in-dry-run", action="store_true", help="Let --dry-run download changed partitions (large) and list new cases")

    activity = parser.add_argument_group("fc activity")
    activity.add_argument("--max-fc-requests", type=int, default=400, help="Cap on registry HTTP requests per run (2 per file)")
    activity.add_argument("--max-new-files", type=int, default=150, help="Cap on new IMM files per run")
    activity.add_argument("--miss-streak", type=int, default=5, help="Stop walking after this many missing numbers in a row")
    activity.add_argument("--refresh-cap", type=int, default=20, help="Recently active files to re-fetch per run (0 disables)")
    activity.add_argument("--refresh-min-age-days", type=int, default=7)
    activity.add_argument("--refresh-active-days", type=int, default=120)
    activity.add_argument("--allow-sweep-from-one", action="store_true", help="Allow walking from IMM-1 when nothing is stored (new library only)")
    activity.add_argument("--fc-delay-ms", type=int, default=2000, help="Pause between files (minimum 2000)")
    activity.add_argument("--fc-jitter-ms", type=int, default=500)

    parser.add_argument("--max-minutes", type=float, default=120.0, help="Stop the run after this long")
    args = parser.parse_args(argv)
    if args.fc_delay_ms < 2000:
        parser.error("--fc-delay-ms must be at least 2000")
    if args.max_cases < 1 or args.max_fc_requests < 1 or args.miss_streak < 1:
        parser.error("caps must be at least 1")
    args.courts = [court.upper() for court in args.courts]
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
