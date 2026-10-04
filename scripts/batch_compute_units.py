#!/usr/bin/env python
"""
Resumable batch job CLI for computing discussion units across the case corpus.

Usage:
    python scripts/batch_compute_units.py [--start CASE_ID] [--end CASE_ID] [--clear]

Examples:
    # Compute all cases from start (default: case 1)
    python scripts/batch_compute_units.py

    # Compute specific range
    python scripts/batch_compute_units.py --start 1 --end 500

    # Clear all cached units and recompute
    python scripts/batch_compute_units.py --clear

    # Resume from case 501 after a previous run
    python scripts/batch_compute_units.py --start 501
"""

import argparse
import logging
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.database import get_db, Case
from backend.batch_jobs import batch_compute_all_units, clear_cache

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Batch compute discussion units for case corpus",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="First case ID to process (default: 1)"
    )
    parser.add_argument(
        "--end",
        type=int,
        default=None,
        help="Last case ID to process (default: max case ID in database)"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all cached units before processing"
    )

    args = parser.parse_args()

    try:
        db = next(get_db())

        if args.clear:
            logger.info("Clearing all cached discussion units...")
            deleted = clear_cache(db)
            logger.info(f"Cleared {deleted} cache entries")

        logger.info(f"Starting batch compute from case {args.start} to {args.end or 'end of corpus'}")
        stats = batch_compute_all_units(db, start_case_id=args.start, end_case_id=args.end)

        logger.info("=" * 60)
        logger.info("Batch compute complete!")
        logger.info(f"Total cases:   {stats['total_cases']}")
        logger.info(f"Processed:     {stats['processed']}")
        logger.info(f"Successful:    {stats['successful']}")
        logger.info(f"Failed:        {stats['failed']}")
        logger.info(f"Skipped:       {stats['skipped']}")
        logger.info(f"Start time:    {stats['start_time']}")
        logger.info(f"End time:      {stats['end_time']}")
        logger.info("=" * 60)

        db.close()
        return 0

    except Exception as e:
        logger.error(f"Error during batch compute: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
