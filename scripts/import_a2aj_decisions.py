#!/usr/bin/env python3
"""
Dry-run importer for A2AJ Canadian case law decisions.

Demonstrates mapping from A2AJ HuggingFace dataset to iLit decision schema.
Supports: RPD (Refugee Protection Division), RAD (Refugee Appeal Division),
FC (Federal Court), FCA (Federal Court of Appeal), and other Canadian courts.

Note: This is a dry-run proof-of-concept. Actual import would require:
1. Database write permissions
2. Deduplication against existing iLit decisions
3. Citation linking setup
4. Embedding generation
"""

import json
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# A2AJ dataset columns → iLit decision schema
FIELD_MAPPING = {
    "citation_en": "citation",
    "name_en": "title",
    "document_date_en": "date",
    "url_en": "source_url",
    "dataset": "court",  # or source_name
    "unofficial_text_en": "full_text",
    "cases_cited_en": "cases_cited_raw",
    "upstream_license": "upstream_license",
}


def parse_a2aj_decision(row: dict) -> dict | None:
    """
    Convert A2AJ dataset row to iLit decision format.

    Args:
        row: Row from a2aj/canadian-case-law dataset

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
                # Format: "2013-06-06 00:00:00+00:00"
                date_obj = datetime.fromisoformat(date_str.replace("+00:00", "")).date()
            else:
                date_obj = None
        except:
            logger.warning(f"Could not parse date for {citation}")
            date_obj = None

        # Parse cases cited (semicolon-separated)
        cases_cited_str = to_string(row.get("cases_cited_en", ""))
        cases_cited = (
            [c.strip() for c in cases_cited_str.split(";") if c.strip()]
            if cases_cited_str
            else []
        )

        # Build decision dict
        decision = {
            "citation": citation,
            "title": to_string(row.get("name_en", "")) or citation,
            "court": to_string(row.get("dataset", "Unknown")),
            "jurisdiction": "Federal",  # A2AJ is federal decisions
            "date": date_obj,
            "full_text": full_text,
            "source_url": to_string(row.get("url_en", "")),
            "source_name": "A2AJ Canadian Case Law",
            "source_type": "academic_dataset",
            "dataset_version": "a2aj-2026-09-27",
            "upstream_license": to_string(row.get("upstream_license", "")),
            "cases_cited": cases_cited,
            "language": "en",  # Assuming English for _en columns
            "processing_status": "ready",  # Already text, no OCR needed
            "scraped_at": datetime.fromisoformat(
                to_string(row.get("scraped_timestamp_en", datetime.now().isoformat())).replace(
                    "+00:00", ""
                )
            ),
        }

        return decision

    except Exception as e:
        logger.error(f"Error parsing A2AJ decision: {e}")
        return None


def dry_run_a2aj_import(sample_size: int = 100) -> None:
    """
    Dry-run import of A2AJ decisions: load sample, parse, show stats.

    Args:
        sample_size: Number of decisions to sample (default 100)
    """
    try:
        from datasets import load_dataset

        logger.info(f"Loading A2AJ Canadian Case Law dataset (sample: {sample_size})...")
        ds = load_dataset("a2aj/canadian-case-law", split="train")
        logger.info(f"✓ Dataset loaded: {len(ds)} total decisions")

        # Count by court
        from collections import Counter

        court_counts = Counter(ds["dataset"])
        logger.info(f"✓ Courts represented:")
        for court, count in court_counts.most_common(10):
            logger.info(f"    {court}: {count}")

        # Parse sample decisions
        parsed_count = 0
        parsed_by_court = Counter()
        text_sizes = []

        for i in range(min(sample_size, len(ds))):
            row = ds[i]
            decision = parse_a2aj_decision(row)

            if decision:
                parsed_count += 1
                parsed_by_court[decision["court"]] += 1
                text_sizes.append(len(decision["full_text"]))

                # Show first parsed decision as sample
                if parsed_count == 1:
                    logger.info(f"\n✓ Sample parsed decision:")
                    logger.info(f"    Citation: {decision['citation']}")
                    logger.info(f"    Court: {decision['court']}")
                    logger.info(f"    Date: {decision['date']}")
                    logger.info(f"    Text length: {len(decision['full_text'])} chars")
                    logger.info(
                        f"    Cases cited: {len(decision['cases_cited'])} references"
                    )

        logger.info(f"\n✓ Parsing results (from {sample_size} samples):")
        logger.info(f"    Valid decisions parsed: {parsed_count}/{sample_size}")
        logger.info(f"    Success rate: {100*parsed_count/sample_size:.1f}%")
        logger.info(f"    By court:")
        for court, count in parsed_by_court.most_common():
            logger.info(f"      {court}: {count}")

        if text_sizes:
            logger.info(f"\n✓ Text statistics:")
            logger.info(f"    Min: {min(text_sizes)} chars")
            logger.info(f"    Max: {max(text_sizes)} chars")
            logger.info(f"    Avg: {sum(text_sizes)/len(text_sizes):.0f} chars")

        # Estimate full import scope
        if parsed_count > 0:
            success_rate = parsed_count / sample_size
            estimated_valid = int(len(ds) * success_rate)
            logger.info(f"\n✓ Estimated scope for full import:")
            logger.info(f"    Total dataset size: {len(ds)}")
            logger.info(f"    Est. valid decisions: ~{estimated_valid}")
            logger.info(f"    Estimated data size: ~{sum(text_sizes)*len(ds)/len(text_sizes)/1024/1024:.1f} MB")

        logger.info("\n✓ Next steps:")
        logger.info("    1. Dedup against existing iLit decisions (by citation + date)")
        logger.info("    2. Run full import with database inserts")
        logger.info("    3. Link to statute references")
        logger.info("    4. Generate embeddings for vector search")

    except ImportError:
        logger.error("datasets library not found. Install: pip install datasets")
    except Exception as e:
        logger.error(f"Error during dry-run: {e}")


if __name__ == "__main__":
    import sys

    sample_size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    dry_run_a2aj_import(sample_size)
