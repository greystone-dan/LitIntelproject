"""The paragraph cited-by batch loop, written so it cannot slow the live site.

Safety rails (all on by default): lowest process priority, one database connection, short statement,
lock and idle-in-transaction limits, one tiny transaction per small batch, a rest after every batch that is
at least four times as long as the work (so it works at most 20% of the time), an optional check that
times the site and backs off when it is slow, a CPU budget, and a stop file. See docs/PARAGRAPH_CITED_BY.md.
"""

from __future__ import annotations

import argparse
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime

from sqlalchemy.exc import DBAPIError, OperationalError

from backend.batch_safety import HealthGate, stop_requested, throttle_sleep
from backend.paragraph_cited_by import ALGO_VERSION
from backend.paragraph_cited_by_db import (
    compute_source_edges,
    count_pending_sources,
    count_processed_sources,
    pending_source_ids,
    write_source_edges,
)

DESCRIPTION = """Build the paragraph "cited by" tables from stored citation occurrences.

Safe by default: with no --apply it only reports what it would do. No AI, no network (except the optional
--health-url you name). Resumable: re-run the same command to carry on.
"""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="write results (default: report only)")
    parser.add_argument("--batch-size", type=int, default=5, help="citing cases per transaction (default 5)")
    parser.add_argument("--sleep-between-batches", "--sleep", dest="sleep_between_batches", type=float, default=2.0,
                        help="minimum rest after each batch, seconds (default 2)")
    parser.add_argument("--sleep-between-cases", type=float, default=0.25, help="rest after each citing case, seconds (default 0.25)")
    parser.add_argument("--max-duty", type=float, default=0.2,
                        help="never work more than this share of the time (default 0.2 = rest at least 4x the work time)")
    parser.add_argument("--max-minutes", type=float, default=None, help="stop cleanly after this many minutes")
    parser.add_argument("--max-cpu-seconds", type=float, default=None, help="stop cleanly after this much CPU time used by this job")
    parser.add_argument("--limit", type=int, default=None, help="stop after this many citing cases")
    parser.add_argument("--after-id", type=int, default=0, help="only citing cases with an id above this")
    parser.add_argument("--case-ids", type=int, nargs="*", help="process exactly these citing case ids")
    parser.add_argument("--statement-timeout-ms", type=int, default=15000, help="per-statement limit (default 15000)")
    parser.add_argument("--lock-timeout-ms", type=int, default=2000, help="wait for a lock at most this long (default 2000)")
    parser.add_argument("--health-url", default=None,
                        help="URL of the live site to time before each batch, e.g. http://127.0.0.1:8001/health/ready")
    parser.add_argument("--health-slow-seconds", type=float, default=1.5, help="back off when the site answers slower than this (default 1.5)")
    parser.add_argument("--health-max-waits", type=int, default=12, help="give up after this many back-offs in a row (default 12)")
    parser.add_argument("--stop-file", default="stop_cited_by.txt",
                        help="stop cleanly when this file exists (default stop_cited_by.txt in the current folder)")
    parser.add_argument("--max-db-errors", type=int, default=5, help="stop after this many database errors in a row (default 5)")
    parser.add_argument("--count", action="store_true", help="also count all citing cases first (slow on a big library)")
    parser.add_argument("--report-cited", type=int, metavar="CASE_ID", help="print stored cited-by for this cited case and exit")
    args = parser.parse_args(argv)
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")
    if not 0 < args.max_duty <= 1:
        parser.error("--max-duty must be above 0 and at most 1")
    return args


@dataclass
class RunResult:
    processed: int = 0
    edges: int = 0
    occurrences: int = 0
    failed: list[int] = field(default_factory=list)
    stopped_because: str = "finished"
    health_waits: int = 0


def run(
    args: argparse.Namespace,
    session_factory: Callable,
    *,
    health: HealthGate | None = None,
    sleep: Callable[[float], None] = time.sleep,
    clock: Callable[[], float] = time.monotonic,
    cpu_clock: Callable[[], float] = time.process_time,
    log: Callable[[str], None] = print,
) -> RunResult:
    """Process pending citing cases in small, rested batches. Each batch opens, uses and closes its own session."""
    result = RunResult()
    started = clock()
    cpu_started = cpu_clock()
    deadline = started + args.max_minutes * 60 if args.max_minutes else None
    explicit = list(args.case_ids) if args.case_ids else None
    after = args.after_id
    db_errors_in_row = 0
    if health is None:
        health = HealthGate(args.health_url, slow_seconds=args.health_slow_seconds, max_waits=args.health_max_waits,
                            sleeper=sleep, log=log)

    def over_limit() -> str | None:
        if stop_requested(args.stop_file):
            return f"stop file {args.stop_file} found"
        if args.limit and result.processed >= args.limit:
            return "limit reached"
        if deadline and clock() >= deadline:
            return "time limit reached"
        if args.max_cpu_seconds and cpu_clock() - cpu_started >= args.max_cpu_seconds:
            return "CPU budget used"
        return None

    while True:
        reason = over_limit()
        if reason:
            result.stopped_because = reason
            break
        if not health.wait_until_healthy():
            result.stopped_because = "the site stayed slow or unreachable"
            break
        batch_started = clock()
        try:
            with session_factory() as db:
                if explicit is not None:
                    batch, explicit = explicit[: args.batch_size], explicit[args.batch_size:]
                else:
                    batch = pending_source_ids(db, after, args.batch_size)
                if not batch:
                    result.stopped_because = "finished"
                    break
                for source_id in batch:
                    try:
                        with db.begin_nested():  # a failure only undoes this one citing case
                            edges, used = compute_source_edges(db, source_id)
                            if args.apply:
                                write_source_edges(db, source_id, edges)
                    except (OperationalError, DBAPIError) as error:
                        # a timeout or lock wait: leave the database alone for a while, retry this case next run
                        db_errors_in_row += 1
                        result.failed.append(source_id)
                        log(f"  skipped case {source_id}: {type(error).__name__} (database busy or slow)")
                        after = max(after, source_id)
                        db.rollback()
                        sleep(min(5.0 * db_errors_in_row, 60.0))
                        break
                    except Exception as error:  # noqa: BLE001 - report and carry on with the next case
                        result.failed.append(source_id)
                        log(f"  skipped case {source_id}: {type(error).__name__}: {str(error)[:120]}")
                        after = max(after, source_id)
                        continue
                    db_errors_in_row = 0
                    result.processed += 1
                    result.edges += len(edges)
                    result.occurrences += used
                    after = max(after, source_id)
                    sleep(args.sleep_between_cases)
                    if over_limit():
                        break
                if args.apply:
                    db.commit()
                else:
                    db.rollback()
        except (OperationalError, DBAPIError) as error:
            db_errors_in_row += 1
            log(f"  database error: {type(error).__name__}; pausing")
            sleep(min(5.0 * db_errors_in_row, 60.0))
        if db_errors_in_row >= args.max_db_errors:
            result.stopped_because = f"{db_errors_in_row} database errors in a row"
            break
        log(f"  {result.processed} citing cases, {result.edges} paragraph edges, {result.occurrences} citations read "
            f"({clock() - started:.0f}s)")
        work = clock() - batch_started
        sleep(throttle_sleep(work, args.sleep_between_batches, args.max_duty))
    result.health_waits = health.waits_total
    return result


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.report_cited is not None:
        return report_cited(args.report_cited)
    from backend.batch_safety import lower_process_priority, make_limited_engine
    from backend.database import DATABASE_URL
    from sqlalchemy.orm import sessionmaker

    print(f"Paragraph cited-by, algorithm v{ALGO_VERSION}, "
          f"{'APPLY' if args.apply else 'PLAN ONLY (no --apply: nothing is written)'}, {datetime.now():%Y-%m-%d %H:%M}")
    print(f"Priority: {lower_process_priority()}. One database connection; statement limit {args.statement_timeout_ms} ms, "
          f"lock limit {args.lock_timeout_ms} ms; batches of {args.batch_size}; working at most {args.max_duty:.0%} of the time.")
    if args.health_url:
        print(f"Watching {args.health_url}: backing off when slower than {args.health_slow_seconds}s.")
    else:
        print("No --health-url given: it will not notice a slow site. Recommended: --health-url http://127.0.0.1:8001/health/ready")
    print(f"To stop at any time: create a file named {args.stop_file} in this folder (or press Ctrl+C).")
    engine = make_limited_engine(DATABASE_URL, statement_timeout_ms=args.statement_timeout_ms,
                                 lock_timeout_ms=args.lock_timeout_ms, application_name="ilit-cited-by")
    factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    with factory() as db:
        done = count_processed_sources(db)
        if args.count:
            total, _ = count_pending_sources(db)
            print(f"Citing cases with resolved citations: {total}; already processed: {done}; to do: {max(total - done, 0)}")
        else:
            print(f"Already processed at this version: {done} citing cases (add --count for the full total; it is slow).")
        db.rollback()
    try:
        result = run(args, factory)
    except KeyboardInterrupt:
        print("Interrupted; finished batches are saved. Run the same command again to resume.")
        engine.dispose()
        return 0
    engine.dispose()
    if result.failed:
        print(f"Skipped {len(result.failed)} case(s) (they stay pending): {result.failed[:20]}")
    print(f"Stopped: {result.stopped_because}. {result.processed} citing cases, {result.edges} paragraph edges, "
          f"{result.occurrences} citations read, {result.health_waits} site back-off(s).")
    if not args.apply:
        print("Nothing was written. Add --apply to store these.")
    elif result.stopped_because != "finished":
        print("Run the same command again to resume.")
    return 0


def report_cited(case_id: int) -> int:
    from backend.database import SessionLocal
    from backend.paragraph_cited_by_db import load_paragraph_cited_by

    with SessionLocal() as db:
        data = load_paragraph_cited_by(db, case_id)
    if data is None:
        print(f"Nothing stored for case {case_id} (batch not run for its citing cases, or no pinpoint citations).")
        return 0
    cov = data["coverage"]
    print(f"Case {case_id}: {cov['sources_processed']}/{cov['sources_total']} citing cases processed"
          f"{'' if cov['complete'] else ' (partial)'}")
    for item in data["paragraphs"]:
        purposes = ", ".join(f"{label} {n}" for label, n in item["purposes"].items())
        print(f"  ¶[{item['paragraph']}] cited by {item['citer_count']} case(s), {item['mention_count']} mention(s): {purposes}")
        for citer in item["citers"][:3]:
            print(f"      {citer['citation'] or citer['title']} x{citer['mentions']} {citer['purpose']}"
                  f"{' (' + citer['signal'] + ')' if citer['signal'] else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
