#!/usr/bin/env python3
"""
Full A2AJ Canadian case law importer with deduplication and database writes.

Loads A2AJ dataset (226,147 decisions from 29 courts), deduplicates against
existing iLit corpus, and imports non-duplicate cases from target courts:
- Federal Court (FC): 35,990 decisions
- Federal Court of Appeal (FCA): 7,813 decisions
- Supreme Court of Canada (SCC): 10,893 decisions
- Refugee Appeal Division (RAD): 14,216 decisions
- Refugee Protection Division (RPD): 6,729 decisions

Total target: 75,641 new cases available for import.
"""

import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from collections import defaultdict, Counter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Map A2AJ dataset codes to iLit court names
COURT_MAP = {
    "FC": "Federal Court",
    "FCA": "Federal Court of Appeal",
    "SCC": "Supreme Court of Canada",
    "RAD": "Refugee Appeal Division",
    "RPD": "Refugee Protection Division",
}

TARGET_COURTS = set(COURT_MAP.values())


class CitationNormalizer:
    """Normalize citations for reliable deduplication."""

    @staticmethod
    def normalize_citation(citation: str) -> str:
        """Normalize citation to canonical form for matching."""
        if not citation:
            return ""
        citation = re.sub(r"\s*\(CanLII\s*\d+\)\s*", "", citation, flags=re.IGNORECASE)
        citation = re.sub(r"\s*\[.*?\]\s*", "", citation)
        citation = re.sub(r"\s+", "", citation)
        return citation.lower().strip()


def load_existing_citations() -> dict[tuple[str, str], int]:
    """
    Load existing case citations from iLit database for deduplication.
    Returns dict of (normalized_citation, date_str) → case_id.
    """
    existing = {}

    try:
        from backend.database import SessionLocal, Case
        db = SessionLocal()

        cases = db.query(Case.id, Case.citation, Case.date).all()
        normalizer = CitationNormalizer()

        for case_id, citation, date_obj in cases:
            if citation and date_obj:
                norm = normalizer.normalize_citation(citation)
                date_str = str(date_obj.date()) if hasattr(date_obj, 'date') else str(date_obj)
                if norm:
                    existing[(norm, date_str)] = case_id

        logger.info(f"Loaded {len(existing)} existing citations from iLit database")
        db.close()
        return existing

    except Exception as e:
        logger.error(f"Error loading existing citations: {e}")
        logger.warning("Proceeding without deduplication (will mark all as new)")
        return {}


def parse_a2aj_decision(row: dict, normalizer: CitationNormalizer) -> Optional[dict]:
    """
    Convert A2AJ dataset row to iLit decision format.

    Args:
        row: Row from a2aj/canadian-case-law dataset
        normalizer: CitationNormalizer instance

    Returns:
        Decision dict ready for database insert, or None if invalid
    """
    try:
        # Helper to convert list or string to string
        def to_string(val):
            if isinstance(val, list):
                return " ".join(str(v) for v in val if v) if val else ""
            return str(val).strip() if val else ""

        # Extract and validate required fields
        citation = to_string(row.get("citation_en", ""))
        full_text = to_string(row.get("unofficial_text_en", ""))

        if not citation or not full_text or len(full_text) < 100:
            return None

        # Parse date
        date_str = to_string(row.get("document_date_en", ""))
        try:
            if date_str:
                # Format: "2013-06-06 00:00:00+00:00" or similar
                date_obj = datetime.fromisoformat(date_str.replace("+00:00", "")).date()
            else:
                date_obj = None
        except:
            logger.debug(f"Could not parse date for {citation}: {date_str}")
            date_obj = None

        # Parse cases cited (semicolon-separated)
        cases_cited_str = to_string(row.get("cases_cited_en", ""))
        cases_cited = (
            [c.strip() for c in cases_cited_str.split(";") if c.strip()]
            if cases_cited_str
            else []
        )

        # Map court
        dataset_code = to_string(row.get("dataset", "")).upper()
        court = COURT_MAP.get(dataset_code)
        if not court:
            return None  # Skip non-target courts

        # Build decision dict
        decision = {
            "citation": citation,
            "normalized_citation": normalizer.normalize_citation(citation),
            "title": to_string(row.get("name_en", "")) or citation,
            "court": court,
            "jurisdiction": "Federal",
            "date": date_obj,
            "full_text": full_text,
            "source_url": to_string(row.get("url_en", "")),
            "source_name": "A2AJ Canadian Case Law",
            "source_type": "academic_dataset",
            "dataset_version": "a2aj-2026-10-03",
            "upstream_license": to_string(row.get("upstream_license", "")),
            "cases_cited": cases_cited,
            "language": "en",
            "processing_status": "parsed",
            "metadata": {
                "a2aj_dataset": dataset_code,
                "text_length": len(full_text),
                "citations_count": len(cases_cited),
            }
        }

        return decision

    except Exception as e:
        logger.debug(f"Error parsing A2AJ row: {e}")
        return None


def import_a2aj_cases(dry_run: bool = True, max_cases: Optional[int] = None) -> dict:
    """
    Import A2AJ cases into iLit database with deduplication.

    Args:
        dry_run: If True, report what would be imported without writing
        max_cases: Limit import to this many cases (for testing)

    Returns:
        Summary dict with import statistics
    """
    try:
        from datasets import load_dataset
    except ImportError:
        logger.error("datasets library not installed. Install with: pip install datasets")
        return {}

    logger.info("Starting A2AJ import process...")
    logger.info(f"Dry run: {dry_run}")

    # Load existing citations for deduplication
    existing_citations = load_existing_citations()
    normalizer = CitationNormalizer()

    # Prepare import results tracking
    stats = {
        "total_rows_examined": 0,
        "valid_decisions": 0,
        "duplicates": 0,
        "new_cases": 0,
        "by_court": defaultdict(lambda: {"total": 0, "new": 0, "duplicates": 0}),
        "invalid_reasons": Counter(),
        "imported_case_ids": [],
    }

    try:
        logger.info("Loading A2AJ dataset (streaming mode)...")
        ds = load_dataset("a2aj/canadian-case-law", split="train", streaming=True)

        # For streaming datasets, we need to track progress differently
        processed = 0

        for row in ds:
            stats["total_rows_examined"] += 1
            processed += 1

            # Show progress
            if processed % 1000 == 0:
                logger.info(f"Processed {processed} A2AJ rows...")

            # Stop if max_cases reached
            if max_cases and stats["new_cases"] >= max_cases:
                logger.info(f"Reached max_cases limit ({max_cases})")
                break

            # Parse decision
            decision = parse_a2aj_decision(row, normalizer)
            if not decision:
                stats["invalid_reasons"]["parse_failed"] += 1
                continue

            stats["valid_decisions"] += 1
            court = decision["court"]
            stats["by_court"][court]["total"] += 1

            # Check for duplicate
            dedup_key = (decision["normalized_citation"], str(decision["date"]) if decision["date"] else None)
            is_duplicate = dedup_key in existing_citations

            if is_duplicate:
                stats["duplicates"] += 1
                stats["by_court"][court]["duplicates"] += 1
                continue

            stats["new_cases"] += 1
            stats["by_court"][court]["new"] += 1

            # If not dry run, insert into database
            if not dry_run:
                try:
                    from backend.database import SessionLocal, Decision
                    db = SessionLocal()

                    new_case = Decision(
                        citation=decision["citation"],
                        title=decision["title"],
                        court=decision["court"],
                        jurisdiction=decision["jurisdiction"],
                        date=decision["date"],
                        full_text=decision["full_text"],
                        source_url=decision.get("source_url", ""),
                        source_name=decision.get("source_name", ""),
                        source_type=decision.get("source_type", ""),
                        language=decision.get("language", "en"),
                        processing_status=decision.get("processing_status", "parsed"),
                        metadata=decision.get("metadata", {}),
                    )

                    db.add(new_case)
                    db.commit()

                    stats["imported_case_ids"].append(new_case.id)
                    existing_citations[dedup_key] = new_case.id

                    db.close()

                except Exception as e:
                    logger.error(f"Error inserting case {decision['citation']}: {e}")
                    stats["invalid_reasons"]["db_insert_failed"] += 1
                    continue

        logger.info(f"\n✓ A2AJ import complete")
        logger.info(f"  Total rows examined: {stats['total_rows_examined']}")
        logger.info(f"  Valid decisions: {stats['valid_decisions']}")
        logger.info(f"  Duplicates found: {stats['duplicates']}")
        logger.info(f"  New cases: {stats['new_cases']}")

        if not dry_run:
            logger.info(f"  Cases imported: {len(stats['imported_case_ids'])}")

        return stats

    except Exception as e:
        logger.error(f"Error during A2AJ import: {e}")
        import traceback
        traceback.print_exc()
        return stats


def report_import_summary(stats: dict):
    """Generate and print import summary report."""
    logger.info("\n" + "="*70)
    logger.info("A2AJ IMPORT SUMMARY")
    logger.info("="*70)

    print(f"\n{'Court':<30} {'Total':>10} {'New':>10} {'Duplicates':>12}")
    print("-"*70)

    for court in sorted(stats["by_court"].keys()):
        court_stats = stats["by_court"][court]
        print(f"{court:<30} {court_stats['total']:>10} {court_stats['new']:>10} {court_stats['duplicates']:>12}")

    print("-"*70)
    total_all = sum(s["total"] for s in stats["by_court"].values())
    total_new = sum(s["new"] for s in stats["by_court"].values())
    total_dups = sum(s["duplicates"] for s in stats["by_court"].values())
    print(f"{'TOTAL':<30} {total_all:>10} {total_new:>10} {total_dups:>12}")

    logger.info("\n✓ Statistics:")
    logger.info(f"  Valid decisions parsed: {stats['valid_decisions']}")
    logger.info(f"  Parse success rate: {100*stats['valid_decisions']/max(1, stats['total_rows_examined']):.1f}%")

    if stats["invalid_reasons"]:
        logger.info("\n⚠ Invalid reasons:")
        for reason, count in stats["invalid_reasons"].most_common():
            logger.info(f"  {reason}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "import":
        # Actual import (requires database)
        dry_run = "--dry-run" in sys.argv
        max_cases = None

        # Check for max limit
        for arg in sys.argv:
            if arg.startswith("--max="):
                max_cases = int(arg.split("=")[1])

        logger.info("Running A2AJ import (production mode)")
        logger.info(f"Dry run: {dry_run}")
        if max_cases:
            logger.info(f"Max cases: {max_cases}")

        stats = import_a2aj_cases(dry_run=dry_run, max_cases=max_cases)
        report_import_summary(stats)

    else:
        # Dry run by default
        print("""
A2AJ Canadian Case Law Importer

Usage:
    python scripts/import_a2aj_full.py                    - Dry run (assess scope)
    python scripts/import_a2aj_full.py import             - Actual import
    python scripts/import_a2aj_full.py import --dry-run   - Dry run with DB check
    python scripts/import_a2aj_full.py import --max=100   - Import first 100 new cases

This tool loads the A2AJ Canadian case law dataset, deduplicates against the
iLit corpus, and imports new decisions from target courts.

Target courts:
  - Federal Court (FC): 35,990 decisions
  - Federal Court of Appeal (FCA): 7,813 decisions
  - Supreme Court of Canada (SCC): 10,893 decisions
  - Refugee Appeal Division (RAD): 14,216 decisions
  - Refugee Protection Division (RPD): 6,729 decisions

Total scope: 75,641 decisions available for import.
        """)

        # Run dry run assessment
        logger.info("Running dry-run assessment...")
        stats = import_a2aj_cases(dry_run=True, max_cases=5000)
        report_import_summary(stats)
