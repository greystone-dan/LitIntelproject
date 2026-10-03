#!/usr/bin/env python3
"""
Diagnostic tool to understand why A2AJ parsing is failing.
Samples rows and reports what's missing/invalid.
"""

import logging
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Map A2AJ dataset codes to iLit court names
COURT_MAP = {
    "FC": "Federal Court",
    "FCA": "Federal Court of Appeal",
    "SCC": "Supreme Court of Canada",
    "RAD": "Refugee Appeal Division",
    "RPD": "Refugee Protection Division",
}

TARGET_COURTS = set(COURT_MAP.values())


def diagnose_a2aj():
    """Sample A2AJ dataset and report failure reasons."""
    try:
        from datasets import load_dataset
    except ImportError:
        logger.error("datasets library not installed")
        return

    logger.info("Loading A2AJ dataset for diagnosis...")

    failure_reasons = Counter()
    valid_count = 0
    court_distribution = Counter()
    sample_failures = []

    try:
        ds = load_dataset("a2aj/canadian-case-law", split="train", streaming=True)

        processed = 0
        for row in ds:
            processed += 1

            # Check fields
            citation = row.get("citation_en", "")
            full_text = row.get("unofficial_text_en", "")
            dataset_code = (row.get("dataset", "") or "").upper()

            if not citation:
                failure_reasons["missing_citation"] += 1
                if len(sample_failures) < 5:
                    sample_failures.append({
                        "reason": "missing_citation",
                        "dataset": dataset_code,
                        "has_text": bool(full_text),
                    })
                continue

            if not full_text:
                failure_reasons["missing_text"] += 1
                if len(sample_failures) < 5:
                    sample_failures.append({
                        "reason": "missing_text",
                        "citation": citation[:50],
                        "dataset": dataset_code,
                    })
                continue

            if isinstance(full_text, list):
                full_text_str = " ".join(str(t) for t in full_text)
            else:
                full_text_str = str(full_text)

            if len(full_text_str) < 100:
                failure_reasons["text_too_short"] += 1
                if len(sample_failures) < 5:
                    sample_failures.append({
                        "reason": "text_too_short",
                        "citation": citation[:50],
                        "text_len": len(full_text_str),
                        "dataset": dataset_code,
                    })
                continue

            court = COURT_MAP.get(dataset_code)
            if not court:
                failure_reasons["unmapped_court"] += 1
                court_distribution[dataset_code] += 1
                if len(sample_failures) < 5:
                    sample_failures.append({
                        "reason": "unmapped_court",
                        "dataset": dataset_code,
                    })
                continue

            # Valid!
            valid_count += 1
            court_distribution[court] += 1

            # Show progress
            if processed % 10000 == 0:
                logger.info(f"Processed {processed}, valid so far: {valid_count}")

            # Stop at sample size
            if processed >= 100000:
                break

        logger.info(f"\n{'='*70}")
        logger.info("A2AJ DIAGNOSTIC RESULTS")
        logger.info(f"{'='*70}\n")

        logger.info(f"Processed: {processed} rows")
        logger.info(f"Valid: {valid_count} ({100*valid_count/processed:.1f}%)")
        logger.info(f"\nFailure reasons:")
        for reason, count in failure_reasons.most_common():
            logger.info(f"  {reason}: {count} ({100*count/processed:.1f}%)")

        logger.info(f"\nCourt distribution (valid cases):")
        for court, count in court_distribution.most_common():
            logger.info(f"  {court}: {count}")

        logger.info(f"\nSample failures:")
        for sample in sample_failures:
            logger.info(f"  {sample}")

    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    diagnose_a2aj()
