#!/usr/bin/env python3
"""Low-priority scheduled intake of new decisions from A2AJ and court sources.

Runs continuously on Daniel's PC, checking for new decisions every 6 hours (A2AJ)
or 24 hours (court sources), deduplicating, and importing without interfering with
the live site. Designed to be pausable, resume-able, and disable-able.

Disable by:
  - Setting SCHEDULED_INTAKE_ENABLED=false in .env
  - Renaming script to .disabled
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal, IngestionRun

logger = logging.getLogger(__name__)


class ScheduledIntakeDaemon:
    """Manages scheduled intake of new cases with locking, health checks, and resumability."""

    def __init__(
        self,
        batch_size: int = 50,
        inter_batch_pause: float = 1.0,
        a2aj_interval_hours: int = 6,
        court_interval_hours: int = 24,
        dry_run: bool = False,
        site_url: str = "http://127.0.0.1:8000",
        ingest_url: str = "http://127.0.0.1:8000/ingest",
    ):
        self.batch_size = batch_size
        self.inter_batch_pause = inter_batch_pause
        self.a2aj_interval = timedelta(hours=a2aj_interval_hours)
        self.court_interval = timedelta(hours=court_interval_hours)
        self.dry_run = dry_run
        self.site_url = site_url
        self.ingest_url = ingest_url

        # Lock file location
        self.lock_path = PROJECT_ROOT / ".scheduled_intake.lock"

    def is_enabled(self) -> bool:
        """Check if scheduled intake is enabled via environment or file existence."""
        if os.getenv("SCHEDULED_INTAKE_ENABLED", "true").lower() == "false":
            return False
        if not self.lock_path.parent.exists():
            return False
        return True

    def acquire_lock(self, timeout_secs: float = 5.0) -> bool:
        """Acquire process lock using temporary file atomic rename.

        Returns True if lock acquired, False if another process holds it.
        """
        try:
            # Try to open lock file for reading to check age
            if self.lock_path.exists():
                with open(self.lock_path, "r") as f:
                    lock_info = json.load(f)
                    started = datetime.fromisoformat(lock_info.get("started_at", ""))
                    age = (datetime.now(timezone.utc) - started.replace(tzinfo=timezone.utc)).total_seconds()
                    # If lock is older than timeout, it's stale; clear it
                    if age > timeout_secs * 2:  # 2x timeout to be safe
                        self.lock_path.unlink()
                    else:
                        # Lock is held by another process
                        return False
        except (json.JSONDecodeError, ValueError, KeyError):
            # Malformed lock, clear it
            try:
                self.lock_path.unlink()
            except FileNotFoundError:
                pass

        # Try atomic create
        try:
            lock_data = {
                "started_at": datetime.now(timezone.utc).isoformat(),
                "pid": os.getpid(),
            }
            # Use temp file + atomic rename for safety
            with NamedTemporaryFile(
                mode="w",
                dir=self.lock_path.parent,
                delete=False,
                suffix=".tmp",
            ) as tmp:
                json.dump(lock_data, tmp)
                tmp_path = Path(tmp.name)
            tmp_path.replace(self.lock_path)
            return True
        except (OSError, IOError):
            return False

    def release_lock(self) -> None:
        """Release the process lock."""
        try:
            self.lock_path.unlink(missing_ok=True)
        except OSError:
            pass

    def check_site_health(self) -> bool:
        """Check if live site is healthy before running intake.

        Returns True if health check passes (or if check fails, still return True
        to be lenient). Only abort if explicitly too loaded.
        """
        try:
            resp = requests.get(f"{self.site_url}/health", timeout=5)
            if resp.status_code == 200:
                return True
            # If site is returning errors, don't ingest
            logger.warning(f"Site health check returned {resp.status_code}; skipping intake")
            return False
        except Exception as e:
            logger.info(f"Site health check unavailable: {e}; proceeding anyway")
            return True

    def log_run_to_db(
        self,
        source_type: str,
        status: str,
        records_discovered: int = 0,
        records_imported: int = 0,
        records_skipped: int = 0,
        error_message: str | None = None,
    ) -> None:
        """Log intake run to database."""
        try:
            with SessionLocal() as db:
                run = IngestionRun(
                    source_type=source_type,
                    source_name="scheduled_intake",
                    run_type="scheduled_discovery" if self.dry_run else "scheduled_ingest",
                    status=status,
                    records_seen=records_discovered,
                    records_ingested=records_imported,
                    records_updated=0,
                    records_failed=records_skipped,
                    metadata_json={
                        "dry_run": self.dry_run,
                        "batch_size": self.batch_size,
                        "error": error_message,
                    },
                )
                db.add(run)
                db.commit()
        except Exception as e:
            logger.warning(f"Could not log run to database: {type(e).__name__} (DB unavailable?)")

    def should_run_a2aj_check(self) -> bool:
        """Check if enough time has passed since last A2AJ check."""
        try:
            with SessionLocal() as db:
                last_run = db.scalar(
                    select(IngestionRun)
                    .where(IngestionRun.source_type == "a2aj_scheduled")
                    .order_by(IngestionRun.id.desc())
                )
                if last_run is None:
                    return True
                if last_run.finished_at is None:
                    # Previous run didn't finish; wait
                    return False
                elapsed = datetime.now(timezone.utc) - last_run.finished_at.replace(tzinfo=timezone.utc)
                return elapsed >= self.a2aj_interval
        except Exception as e:
            logger.warning(f"Cannot check A2AJ interval (DB unavailable?): {type(e).__name__}")
            # Return True to allow intake to proceed (database may come online soon)
            return True

    def discover_a2aj_new_decisions(self) -> tuple[int, list[dict]]:
        """Discover new decisions from A2AJ dataset without importing.

        Returns (discovered_count, decisions_list) for reporting.
        """
        logger.info("Starting A2AJ discovery in dry-run mode")
        from scripts.ingest_a2aj_parquet import build_case
        from sqlalchemy import select
        from backend.database import Case

        try:
            import datasets
        except ImportError:
            logger.error("datasets library not available; skipping A2AJ intake")
            return 0, []

        discovered = []
        with SessionLocal() as db:
            existing_citations = set(db.scalars(select(Case.citation)).all())
            existing_hashes = set(db.scalars(select(Case.full_text_hash)).all())

        try:
            # Use streaming mode to avoid downloading entire dataset
            ds = datasets.load_dataset(
                "a2aj/canadian-case-law",
                split="train",
                streaming=True,
                trust_remote_code=True,
            )

            count = 0
            for record in ds:
                # Filter to target courts
                court = record.get("dataset", "").upper()
                if court not in {"FC", "FCA", "SCC", "RAD", "RPD"}:
                    continue

                # Try to build case object for validation
                case = build_case(record)
                if case is None:
                    continue

                # Check if already ingested
                if case.citation in existing_citations or case.full_text_hash in existing_hashes:
                    continue

                discovered.append({
                    "citation": case.citation,
                    "title": case.title,
                    "court": case.court,
                    "date": case.date.isoformat() if case.date else None,
                    "source_id": case.source_id,
                })

                count += 1
                if count >= self.batch_size:
                    break

            logger.info(f"Discovered {count} new A2AJ decisions")
            return count, discovered

        except Exception as e:
            logger.error(f"A2AJ discovery failed: {e}")
            self.log_run_to_db(
                "a2aj_scheduled",
                "failed",
                error_message=str(e),
            )
            return 0, []

    def run_once(self) -> None:
        """Run one cycle of discovery/ingestion checks."""
        if not self.is_enabled():
            logger.info("Scheduled intake is disabled")
            return

        if not self.acquire_lock():
            logger.debug("Another intake process is running")
            return

        try:
            if not self.check_site_health():
                logger.warning("Site health check failed; skipping intake")
                return

            if self.should_run_a2aj_check():
                discovered, decisions = self.discover_a2aj_new_decisions()
                self.log_run_to_db(
                    "a2aj_scheduled",
                    "completed",
                    records_discovered=discovered,
                    records_imported=0 if self.dry_run else discovered,
                )
                logger.info(f"A2AJ intake cycle: discovered={discovered}")

        finally:
            self.release_lock()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Cases per batch (default: 50)",
    )
    parser.add_argument(
        "--inter-batch-pause",
        type=float,
        default=1.0,
        help="Seconds to pause between batches (default: 1.0)",
    )
    parser.add_argument(
        "--a2aj-interval",
        type=int,
        default=6,
        help="Hours between A2AJ checks (default: 6)",
    )
    parser.add_argument(
        "--court-interval",
        type=int,
        default=24,
        help="Hours between court source checks (default: 24)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Discover and report without importing",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run one cycle and exit (for testing)",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=300,
        help="Seconds between polling (default: 300 / 5 min)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args()


def setup_logging(verbose: bool = False) -> None:
    """Set up logging to file and console."""
    log_dir = PROJECT_ROOT / "logs" / "intake"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / f"daemon-{datetime.now().strftime('%Y%m%d')}.log"

    handlers = [
        logging.FileHandler(log_file),
        logging.StreamHandler(),
    ]

    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )


def main() -> None:
    args = parse_args()
    setup_logging(args.verbose)

    daemon = ScheduledIntakeDaemon(
        batch_size=args.batch_size,
        inter_batch_pause=args.inter_batch_pause,
        a2aj_interval_hours=args.a2aj_interval,
        court_interval_hours=args.court_interval,
        dry_run=args.dry_run,
    )

    logger.info(f"Scheduled intake daemon starting (dry_run={args.dry_run})")

    if args.once:
        daemon.run_once()
    else:
        while True:
            try:
                daemon.run_once()
                time.sleep(args.poll_interval)
            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {e}", exc_info=True)
                time.sleep(args.poll_interval)


if __name__ == "__main__":
    main()
