#!/usr/bin/env python3
"""
A2AJ case law importer for Federal courts (FC, FCA, SCC, RAD, RPD).

Loads A2AJ Canadian case law dataset, deduplicates against existing iLit cases,
and reports how many new decisions per court would be added.

This enables expansion of case database with 100k+ academic dataset cases.
"""

import logging
import re
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Target courts for import
TARGET_COURTS = {"Federal Court", "Federal Court of Appeal", "SCC", "RAD", "RPD"}

class CitationNormalizer:
    """Normalize citations for deduplication."""

    @staticmethod
    def normalize_citation(citation: str) -> str:
        """Normalize citation to canonical form."""
        if not citation:
            return ""
        citation = re.sub(r"\s*\(CanLII\)\s*", "", citation, flags=re.IGNORECASE)
        citation = re.sub(r"\s*\[.*?\]\s*", "", citation)
        citation = re.sub(r"\s+", "", citation)
        return citation.lower()


def load_existing_citations(db=None) -> set[tuple[str, str]]:
    """
    Load existing case citations from iLit database.
    Returns set of (normalized_citation, date_str) tuples.
    """
    existing = set()

    if db is None:
        try:
            from backend.database import SessionLocal, Case
            db = SessionLocal()
        except Exception as e:
            logger.warning(f"Could not load existing citations from DB: {e}")
            logger.warning("Proceeding without dedup (will report all A2AJ cases as new)")
            return existing

    try:
        from backend.database import Case
        cases = db.query(Case.citation, Case.date).all()
        normalizer = CitationNormalizer()

        for citation, date_obj in cases:
            if citation:
                norm = normalizer.normalize_citation(citation)
                date_str = str(date_obj) if date_obj else None
                if date_str:
                    existing.add((norm, date_str))

        logger.info(f"Loaded {len(existing)} existing citations from iLit")
        return existing
    except Exception as e:
        logger.error(f"Error loading existing citations: {e}")
        return set()
    finally:
        if db:
            db.close()


def assess_a2aj_imports() -> dict[str, dict]:
    """
    Load A2AJ dataset and assess how many new cases per court would be added.
    Uses chunked loading to avoid memory issues.
    """
    try:
        from datasets import load_dataset
    except ImportError:
        logger.error("datasets library not installed. Install with: pip install datasets")
        return {}

    logger.info("Loading A2AJ dataset...")
    existing_citations = load_existing_citations()
    normalizer = CitationNormalizer()

    results = {
        "Federal Court": {"total": 0, "new": 0, "duplicates": 0, "invalid": 0},
        "Federal Court of Appeal": {"total": 0, "new": 0, "duplicates": 0, "invalid": 0},
        "SCC": {"total": 0, "new": 0, "duplicates": 0, "invalid": 0},
        "RAD": {"total": 0, "new": 0, "duplicates": 0, "invalid": 0},
        "RPD": {"total": 0, "new": 0, "duplicates": 0, "invalid": 0},
    }

    try:
        # Load dataset with streaming to avoid memory issues
        ds = load_dataset("a2aj/canadian-case-law", split="train", streaming=True)
        logger.info(f"A2AJ dataset loaded (streaming mode)")

        processed = 0
        for row in ds:
            try:
                # Map A2AJ dataset field to court
                dataset_name = row.get("dataset", "")
                court_map = {
                    "Federal Court": "Federal Court",
                    "Federal Court of Appeal": "Federal Court of Appeal",
                    "Supreme Court of Canada": "SCC",
                    "Refugee Appeal Division": "RAD",
                    "Refugee Protection Division": "RPD",
                }

                court = None
                for key, mapped_court in court_map.items():
                    if key.lower() in dataset_name.lower():
                        court = mapped_court
                        break

                if not court:
                    continue

                results[court]["total"] += 1

                # Check if it's a valid case
                citation = row.get("citation_en", "")
                full_text = row.get("unofficial_text_en", "")
                date_str = row.get("document_date_en", "")

                if not citation or not full_text or len(full_text) < 100:
                    results[court]["invalid"] += 1
                    continue

                # Parse date
                try:
                    if date_str:
                        date_obj = datetime.fromisoformat(date_str.replace("+00:00", "")).date()
                        date_key = str(date_obj)
                    else:
                        date_key = None
                except:
                    results[court]["invalid"] += 1
                    continue

                # Check for duplicate
                norm_citation = normalizer.normalize_citation(citation)
                if date_key and (norm_citation, date_key) in existing_citations:
                    results[court]["duplicates"] += 1
                else:
                    results[court]["new"] += 1

                processed += 1
                if processed % 1000 == 0:
                    logger.info(f"Processed {processed} A2AJ decisions...")

            except Exception as e:
                logger.warning(f"Error processing row: {e}")
                continue

        logger.info(f"\nProcessed {processed} A2AJ decisions total")
        return results

    except Exception as e:
        logger.error(f"Error loading A2AJ dataset: {e}")
        return {}


def report_a2aj_import_forecast():
    """Generate and print import forecast."""
    logger.info("="*60)
    logger.info("A2AJ Case Law Import Forecast")
    logger.info("="*60)

    results = assess_a2aj_imports()

    if not results:
        logger.error("Could not assess A2AJ imports")
        return

    total_new = 0
    total_cases = 0

    print("\n" + "="*60)
    print("A2AJ Import Summary")
    print("="*60)
    print(f"{'Court':<30} {'Total':>10} {'New':>10} {'Duplicates':>12}")
    print("-"*60)

    for court in ["Federal Court", "Federal Court of Appeal", "SCC", "RAD", "RPD"]:
        data = results[court]
        total = data["total"]
        new = data["new"]
        dups = data["duplicates"]

        if total > 0:
            print(f"{court:<30} {total:>10} {new:>10} {dups:>12}")
            total_new += new
            total_cases += total

    print("-"*60)
    print(f"{'TOTAL':<30} {total_cases:>10} {total_new:>10}")
    print("="*60)

    if total_cases > 0:
        dedup_rate = (sum(r["duplicates"] for r in results.values()) / total_cases * 100)
        print(f"\nDuplication rate: {dedup_rate:.1f}%")
        print(f"New cases to import: {total_new}")
        print(f"\nImport command: python scripts/import_a2aj_decisions.py --courts FC FCA SCC RAD RPD")
    else:
        logger.error("No A2AJ cases found for target courts")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "assess":
        report_a2aj_import_forecast()
    else:
        print("""
A2AJ Case Law Importer

Usage:
    python scripts/a2aj_case_importer.py assess    - Report import forecast
    python scripts/a2aj_case_importer.py import    - Actually import cases (requires DB)

This tool loads the A2AJ Canadian case law dataset and reports how many new
decisions from Federal Court, FCA, SCC, RAD, and RPD can be imported.
        """)
