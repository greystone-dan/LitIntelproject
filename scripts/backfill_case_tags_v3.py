#!/usr/bin/env python3
"""Backfill all cases with V3 legal tags. Resumable and idempotent."""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path

from sqlalchemy import delete, func, select

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseTag, CaseTaggingStatus, SessionLocal
from backend.legal_tagger_v3 import TAXONOMY_VERSION
from scripts.tag_cases_v3 import tag_pending_cases

logger = logging.getLogger(__name__)


def count_existing_tags(db) -> int:
    """Count tags for the current taxonomy version before backfill."""
    return db.scalar(
        select(func.count(CaseTag.id)).where(CaseTag.taxonomy_version == TAXONOMY_VERSION)
    ) or 0


def count_all_cases(db) -> int:
    """Count total cases in database."""
    return db.scalar(select(func.count(Case.id))) or 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retag", action="store_true", help="Delete existing tags and start fresh")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with SessionLocal() as db:
        total_cases = count_all_cases(db)
        tags_before = count_existing_tags(db)

        logger.info(f"Starting backfill: total_cases={total_cases} tags_before={tags_before} taxonomy={TAXONOMY_VERSION}")

        if args.dry_run:
            logger.info("DRY RUN: no changes will be made")
            return

        if args.retag:
            logger.info("Deleting existing tags and tagging status for retag")
            db.execute(delete(CaseTag).where(CaseTag.taxonomy_version == TAXONOMY_VERSION))
            db.execute(delete(CaseTaggingStatus).where(CaseTaggingStatus.taxonomy_version == TAXONOMY_VERSION))
            db.commit()

        # Backfill in batches of 100 with 1-second pause between batches
        logger.info("Starting tag backfill with batch_size=100 and pause=1.0s")
        start_time = time.time()
        cases_tagged = tags_created = skipped_cases = 0

        while True:
            cases_tagged_batch, tags_created_batch, skipped_batch = tag_pending_cases(
                db,
                batch_size=100,
                batch_timeout=300,
                limit=100,
            )

            cases_tagged += cases_tagged_batch
            tags_created += tags_created_batch
            skipped_cases += skipped_batch

            if cases_tagged_batch == 0:
                break

            logger.info(f"Batch complete: cases_tagged={cases_tagged} tags_created={tags_created} skipped={skipped_cases}")
            time.sleep(1.0)

        elapsed = time.time() - start_time
        tags_after = count_existing_tags(db)

        result = {
            "status": "complete",
            "taxonomy_version": TAXONOMY_VERSION,
            "cases_tagged": cases_tagged,
            "tags_created": tags_created,
            "tags_skipped": skipped_cases,
            "tags_before": tags_before,
            "tags_after": tags_after,
            "elapsed_seconds": round(elapsed, 1),
        }

        logger.info(json.dumps(result))
        print(json.dumps(result))


if __name__ == "__main__":
    main()
