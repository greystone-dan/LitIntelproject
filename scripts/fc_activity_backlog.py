#!/usr/bin/env python3
"""Overnight FC Activity backlog: fetch docket activity for IMM files that are not resolved yet.

"Known" IMM numbers are the union of: fc_activity_cases (citation or raw_payload.imm_number),
fc_procedural_history rows with a style of cause, and IMM docket numbers on FC decisions in `cases`.

A known number is "resolved" when its fc_activity file has docket entries AND the stored
classification says lifecycle_status.status = 'closed'. Everything else is unresolved:
  not_in_activity   known only from decisions / procedural history, no fc_activity file
  no_documents      fc_activity file exists but holds zero docket entries
  open_or_unknown   has entries, lifecycle not 'closed' (or not classified yet)

Subcommands (all read-only except `run` without --dry-run):
  counts              totals and a by-year breakdown, plus a runtime estimate
  run --dry-run       fetch and parse the first N unresolved numbers (default 20), write nothing
  run                 the real run: additive writes only, resumable, stop file, progress file
  undo                list (default) or remove (--yes) the rows a run added, from its ledger

Writes are additive: new fc_activity_cases / fc_activity_documents rows only. Existing files only
gain missing docket entries (and a blank case name/date is filled); nothing is overwritten or deleted.
No AI calls. Two requests per file at the polite 2 s delay plus jitter.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from backend.database import FCActivityCase, FCActivityDocument, SessionLocal  # noqa: E402

IMM_RE = re.compile(r"^IMM-(\d+)-(\d{2})$")
ADVISORY_LOCK_KEY = 74_100_262
CATEGORIES = ("not_in_activity", "no_documents", "open_or_unknown")
SECONDS_PER_FILE = 4.0  # 2.0 s delay + ~0.25 s mean jitter + two requests; refined by the dry run
DEFAULT_RUN_DIR = PROJECT_ROOT / "data" / "fc_activity_overnight"

UNRESOLVED_SQL = """
WITH acase AS (
    SELECT c.id,
           upper(COALESCE(NULLIF(c.citation, ''), c.raw_payload->>'imm_number')) AS imm
    FROM fc_activity_cases c
),
acase_imm AS (
    SELECT a.imm,
           bool_or(EXISTS (SELECT 1 FROM fc_activity_documents d WHERE d.case_id = a.id)) AS has_docs,
           bool_or(k.classification_json::jsonb #>> '{lifecycle_status,status}' = 'closed') AS closed
    FROM acase a
    LEFT JOIN fc_activity_classifications k ON k.source_case_id = a.id
    WHERE a.imm ~ '^IMM-[0-9]+-[0-9]{2}$'
    GROUP BY a.imm
),
known AS (
    SELECT imm FROM acase_imm
    UNION
    SELECT upper(imm_number) FROM fc_procedural_history
      WHERE coalesce(style_of_cause, '') <> '' AND upper(imm_number) ~ '^IMM-[0-9]+-[0-9]{2}$'
    UNION
    SELECT m[1] FROM cases cs,
      LATERAL regexp_matches(upper(coalesce(cs.docket_number, '') || ' ' || coalesce(cs.source_id, '')),
                             '(IMM-[0-9]+-[0-9]{2})', 'g') AS m
      WHERE cs.court = 'FC'
)
SELECT k.imm,
       CASE WHEN a.imm IS NULL THEN 'not_in_activity'
            WHEN NOT coalesce(a.has_docs, false) THEN 'no_documents'
            WHEN coalesce(a.closed, false) THEN 'resolved'
            ELSE 'open_or_unknown' END AS category
FROM known k LEFT JOIN acase_imm a ON a.imm = k.imm
"""


def imm_sort_key(imm: str, newest_first: bool = False) -> tuple[int, int]:
    """Year then sequence; two-digit years 00-50 are 2000s. Oldest first unless newest_first."""
    match = IMM_RE.match(imm)
    if not match:
        return (9999, 0)
    seq, yy = int(match.group(1)), int(match.group(2))
    year = 2000 + yy if yy <= 50 else 1900 + yy
    return (-year, -seq) if newest_first else (year, seq)


def load_unresolved(db, categories: tuple[str, ...] = CATEGORIES) -> list[tuple[str, str]]:
    rows = db.execute(text(UNRESOLVED_SQL)).all()
    return [(imm, cat) for imm, cat in rows if cat in categories and IMM_RE.match(imm)]


def read_done(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.split("\t", 1)[0].strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def stop_requested(stop_file: Path | None) -> bool:
    return bool(stop_file and stop_file.exists())


def estimate_hours(count: int, seconds_per_file: float = SECONDS_PER_FILE) -> float:
    return count * seconds_per_file / 3600


class Logger:
    def __init__(self, path: Path | None) -> None:
        self.handle = path.open("a", encoding="utf-8", buffering=1) if path else None

    def __call__(self, message: str) -> None:
        line = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}Z {message}"
        print(line, flush=True)
        if self.handle:
            self.handle.write(line + "\n")


def cmd_counts(args: argparse.Namespace) -> int:
    with SessionLocal() as db:
        rows = db.execute(text(UNRESOLVED_SQL)).all()
    by_cat: dict[str, int] = {}
    by_year: dict[str, dict[str, int]] = {}
    for imm, cat in rows:
        by_cat[cat] = by_cat.get(cat, 0) + 1
        year = imm_sort_key(imm)[0]
        by_year.setdefault(str(year), {}).setdefault(cat, 0)
        by_year[str(year)][cat] += 1
    total = len(rows)
    unresolved = sum(by_cat.get(c, 0) for c in CATEGORIES)
    print(f"Total known IMM numbers: {total:,}")
    print(f"Resolved (closed): {by_cat.get('resolved', 0):,}")
    print(f"Unresolved: {unresolved:,}")
    for cat in CATEGORIES:
        print(f"  {cat}: {by_cat.get(cat, 0):,}")
    print("\nBy year (resolved / not_in_activity / no_documents / open_or_unknown):")
    for year in sorted(by_year):
        c = by_year[year]
        print(f"  {year}: {c.get('resolved', 0):,} / {c.get('not_in_activity', 0):,} / "
              f"{c.get('no_documents', 0):,} / {c.get('open_or_unknown', 0):,}")
    print(f"\nEstimate at ~{SECONDS_PER_FILE:.0f} s per file: {estimate_hours(unresolved):.1f} hours "
          f"for all unresolved ({estimate_hours(unresolved) / 10:.1f} ten-hour nights).")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps({"total": total, "by_category": by_cat, "by_year": by_year}, indent=2), encoding="utf-8")
    return 0


def store_additive(db, imm: str, result: dict[str, Any], run_label: str) -> tuple[int, bool, list[int]]:
    """Add the file/entries that are missing. Never overwrites or deletes. Returns (case_id, case_created, new_doc_ids)."""
    from scripts.fetch_fc_procedural_history import _activity_hash, _activity_year, _json_safe, _parse_date

    case = db.query(FCActivityCase).filter(FCActivityCase.citation == imm).first()
    if case is None:
        case = db.query(FCActivityCase).filter(
            FCActivityCase.source_key.in_([_activity_hash("fc-procedural-endpoint", imm), _activity_hash("fc-daily-intake", imm)])
        ).first()
    entry_dates = [d for d in (_parse_date(str(e.get("date") or "")) for e in result.get("entries_json") or []) if d]
    created = False
    if case is None:
        case = FCActivityCase(
            source_key=_activity_hash("fc-overnight-backlog", imm),
            citation=imm,
            year=_activity_year(imm),
            case_name=result.get("style_of_cause"),
            date_filed=min(entry_dates) if entry_dates else None,
            source_type="fc_registry_overnight",
            source_name=run_label,
            source_id=imm,
            scraped_timestamp=result.get("fetched_at"),
            raw_payload=_json_safe({**result, "imm_number": imm}),
        )
        db.add(case)
        db.flush()
        created = True
    else:
        if not case.case_name and result.get("style_of_cause"):
            case.case_name = result["style_of_cause"]
        if case.date_filed is None and entry_dates:
            case.date_filed = min(entry_dates)

    new_ids: list[int] = []
    seen: set[tuple[str, str]] = set()
    for entry in result.get("entries_json") or []:
        entry_text = str(entry.get("entry") or "").strip()
        entry_date = entry.get("date") or None
        re_no = str(entry.get("re_no") or "").strip() or None
        docno = str(entry.get("docno") or "").strip() or None
        if not entry_text and not entry_date:
            continue
        entry_hash = _activity_hash(imm, re_no, docno, entry_date, entry_text)
        if re_no is not None and docno is not None:
            if (re_no, docno) in seen:
                continue
            seen.add((re_no, docno))
            if db.query(FCActivityDocument.id).filter(
                FCActivityDocument.case_id == case.id, FCActivityDocument.re_no == re_no, FCActivityDocument.docno == docno
            ).first():
                continue
        if db.query(FCActivityDocument.id).filter(
            FCActivityDocument.case_id == case.id, FCActivityDocument.entry_hash == entry_hash
        ).first():
            continue
        doc = FCActivityDocument(
            case_id=case.id, re_no=re_no, docno=docno,
            doc_dt=_parse_date(str(entry_date)) if entry_date else None,
            recorded_entry=entry_text or None, entry_hash=entry_hash,
            raw_document={"imm_number": imm, **entry},
        )
        db.add(doc)
        db.flush()
        new_ids.append(doc.id)
    db.commit()
    return case.id, created, new_ids


def cmd_run(args: argparse.Namespace) -> int:
    from scripts.daily_intake import build_fc_client, is_missing_file
    from scripts.fetch_fc_procedural_history import RequestBudget, process_imm, validate_delay_ms
    import random

    validate_delay_ms(args.delay_ms)
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    stop_file = Path(args.stop_file) if args.stop_file else run_dir / "stop.txt"
    done_path = run_dir / "done.tsv"          # IMM <tab> outcome; the resume list
    ledger_path = run_dir / "ledger.jsonl"    # what was added, for undo
    progress_path = run_dir / "progress.json"
    log = Logger(None if args.dry_run else run_dir / "run.log")
    run_label = f"FC Activity overnight backlog {datetime.now(timezone.utc):%Y-%m-%d}"

    if stop_requested(stop_file) and not args.dry_run:
        log(f"Stop file exists ({stop_file}); delete it to run. Nothing done.")
        return 1

    lock_db = SessionLocal()  # held open for the whole run: the advisory lock lives on this connection
    with SessionLocal() as db:
        candidates = load_unresolved(db, tuple(args.categories.split(",")))
    if not args.dry_run:
        if not lock_db.execute(text("SELECT pg_try_advisory_lock(:k)"), {"k": ADVISORY_LOCK_KEY}).scalar():
            log("Another backlog run holds the lock; exiting.")
            lock_db.close()
            return 1
    candidates.sort(key=lambda row: imm_sort_key(row[0], args.newest_first))
    done = set() if args.dry_run or args.ignore_done else read_done(done_path)
    todo = [imm for imm, _cat in candidates if imm not in done]
    limit = 20 if args.dry_run and not args.limit else args.limit
    if limit:
        todo = todo[:limit]
    log(f"{'DRY RUN: ' if args.dry_run else ''}{len(candidates):,} unresolved, {len(done):,} already done, "
        f"{len(todo):,} to process (~{estimate_hours(len(todo)):.1f} h)")

    started = time.monotonic()
    request_budget = RequestBudget(max(args.max_requests, 2 * len(todo) * 3))
    stats = {"processed": 0, "files_added": 0, "docs_added": 0, "missing": 0, "failed": 0}
    consecutive_failures = 0
    pause_s = args.issue_pause_s
    stopped_by = "finished"
    done_handle = None if args.dry_run else done_path.open("a", encoding="utf-8", buffering=1)
    ledger_handle = None if args.dry_run else ledger_path.open("a", encoding="utf-8", buffering=1)

    def write_progress() -> None:
        if args.dry_run:
            return
        progress_path.write_text(json.dumps({
            **stats, "remaining": len(todo) - stats["processed"], "stopped_by": stopped_by,
            "elapsed_minutes": round((time.monotonic() - started) / 60, 1),
            "updated": datetime.now(timezone.utc).isoformat(),
        }, indent=2), encoding="utf-8")

    try:
        with build_fc_client() as client:
            for i, imm in enumerate(todo, 1):
                if stop_requested(stop_file):
                    stopped_by = "stop file"
                    break
                if args.max_minutes and (time.monotonic() - started) > args.max_minutes * 60:
                    stopped_by = "time limit"
                    break
                if i > 1:
                    time.sleep((args.delay_ms + random.randint(0, args.jitter_ms)) / 1000)
                try:
                    result = process_imm(client, imm, request_budget=request_budget)
                except Exception as exc:  # budget or unexpected
                    result = {"error": str(exc)}
                if result.get("error"):
                    stats["failed"] += 1
                    consecutive_failures += 1
                    log(f"[fail] {imm}: {result['error']} (consecutive={consecutive_failures}, pausing {pause_s:.0f}s)")
                    time.sleep(pause_s)
                    pause_s = min(pause_s * 2, 300)
                    if consecutive_failures >= args.max_consecutive_failures:
                        stopped_by = f"{consecutive_failures} failures in a row (source may be blocking)"
                        break
                    continue
                consecutive_failures, pause_s = 0, args.issue_pause_s
                stats["processed"] += 1
                if is_missing_file(result):
                    stats["missing"] += 1
                    outcome = "missing"
                    log(f"[{i}/{len(todo)}] {imm}: no file at registry")
                elif args.dry_run:
                    outcome = "dry"
                    log(f"[{i}/{len(todo)}] {imm}: {len(result.get('entries_json') or [])} entries, "
                        f"status={result.get('case_status')}, would write")
                else:
                    with SessionLocal() as db:
                        case_id, created, new_ids = store_additive(db, imm, result, run_label)
                    stats["files_added"] += int(created)
                    stats["docs_added"] += len(new_ids)
                    outcome = f"ok:{len(new_ids)}"
                    if created or new_ids:
                        ledger_handle.write(json.dumps({"imm": imm, "case_id": case_id, "case_created": created, "doc_ids": new_ids}) + "\n")
                    log(f"[{i}/{len(todo)}] {imm}: {'new file, ' if created else ''}{len(new_ids)} new entries")
                if done_handle:
                    done_handle.write(f"{imm}\t{outcome}\n")
                if i % 25 == 0:
                    write_progress()
    finally:
        write_progress()
        lock_db.close()
        for handle in (done_handle, ledger_handle):
            if handle:
                handle.close()
    log(f"Stopped: {stopped_by}. {stats}")
    return 0 if stopped_by in ("finished", "stop file", "time limit") else 2


def cmd_undo(args: argparse.Namespace) -> int:
    ledger = Path(args.run_dir) / "ledger.jsonl"
    if not ledger.exists():
        print("No ledger; nothing to undo.")
        return 0
    entries = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line.strip()]
    doc_ids = [d for e in entries for d in e["doc_ids"]]
    case_ids = [e["case_id"] for e in entries if e["case_created"]]
    print(f"Ledger: {len(case_ids):,} files created, {len(doc_ids):,} docket entries added.")
    if not args.yes:
        print("Dry run. Re-run with --yes to delete exactly these rows.")
        return 0
    with SessionLocal() as db:
        db.execute(text("DELETE FROM fc_activity_documents WHERE id = ANY(:ids)"), {"ids": doc_ids})
        db.execute(text("DELETE FROM fc_activity_cases WHERE id = ANY(:ids) AND source_type = 'fc_registry_overnight'"), {"ids": case_ids})
        db.commit()
    ledger.rename(ledger.with_suffix(".undone.jsonl"))
    print("Removed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    counts = sub.add_parser("counts", help="read-only counts and runtime estimate")
    counts.add_argument("--json-out")
    counts.set_defaults(func=cmd_counts)
    run = sub.add_parser("run", help="fetch unresolved IMM files")
    run.add_argument("--dry-run", action="store_true", help="fetch and parse 20 numbers (or --limit), write nothing")
    run.add_argument("--limit", type=int)
    run.add_argument("--max-minutes", type=float, help="stop after this long (e.g. 600 for ten hours)")
    run.add_argument("--categories", default=",".join(CATEGORIES))
    run.add_argument("--newest-first", action="store_true", help="default is oldest year first")
    run.add_argument("--ignore-done", action="store_true", help="re-fetch numbers already in done.tsv")
    run.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    run.add_argument("--stop-file", help="default: <run-dir>/stop.txt")
    run.add_argument("--delay-ms", type=int, default=2000, help="minimum 2000")
    run.add_argument("--jitter-ms", type=int, default=500)
    run.add_argument("--issue-pause-s", type=float, default=10, help="pause after a failed fetch; doubles up to 300")
    run.add_argument("--max-consecutive-failures", type=int, default=10)
    run.add_argument("--max-requests", type=int, default=100000)
    run.set_defaults(func=cmd_run)
    undo = sub.add_parser("undo", help="remove the rows a run added (dry run unless --yes)")
    undo.add_argument("--run-dir", default=str(DEFAULT_RUN_DIR))
    undo.add_argument("--yes", action="store_true")
    undo.set_defaults(func=cmd_undo)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
