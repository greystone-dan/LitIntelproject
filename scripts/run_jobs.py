"""Run opt-in interval jobs in a separate process, without database or dotenv imports."""

from __future__ import annotations

import argparse
import signal
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.job_runner import Runner, install_signal_handlers, load_jobs, log_event


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Exit codes: 0 success/no enabled jobs; 1 job/lock failure or timeout; "
               "2 invalid configuration/arguments; 130 SIGINT; 143 SIGTERM.",
    )
    parser.add_argument("--config", type=Path, default=ROOT / "config/jobs.example.json")
    parser.add_argument("--lock-dir", type=Path, default=ROOT / "data/job_runner_locks")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--once", action="store_true", help="Run each enabled job once, then exit")
    modes.add_argument("--dry-run", action="store_true", help="Log due enabled jobs without commands or lock writes, then exit")
    modes.add_argument("--list", action="store_true", help="List validated jobs without commands or lock writes, then exit")
    args = parser.parse_args(argv)
    try:
        jobs = load_jobs(args.config)
    except (OSError, ValueError, OverflowError):
        log_event("config_error", reason="unreadable_or_invalid_config")
        return 2
    if args.list:
        for job in jobs:
            log_event("job_config", job=job.name, enabled=job.enabled,
                      interval_seconds=job.interval_seconds,
                      max_runtime_seconds=job.max_runtime_seconds,
                      overlap_policy=job.overlap_policy)
        return 0
    stop = threading.Event()
    previous, received = install_signal_handlers(stop)
    try:
        code = Runner(jobs, args.lock_dir, ROOT, stop=stop).run(once=args.once, dry_run=args.dry_run)
        if received:
            log_event("runner_stopped", signal=received[0])
            return 128 + received[0]
        return code
    finally:
        for signum, handler in previous.items():
            signal.signal(signum, handler)


if __name__ == "__main__":
    raise SystemExit(main())
