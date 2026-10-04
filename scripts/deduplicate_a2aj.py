#!/usr/bin/env python3
"""
Deduplication logic for A2AJ decisions against existing iLit corpus.

Matches A2AJ decisions to existing decisions using:
1. Neutral citation (normalized) + decision date
2. Case name + date (fallback)

This prevents duplicate storage and enables citation linking.

Note: This is a dry-run proof-of-concept showing dedup logic.
Actual implementation requires database access and citation normalization rules.
"""

import logging
import re
from datetime import date, datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CitationNormalizer:
    """Normalize neutral citations for dedup matching."""

    @staticmethod
    def normalize_citation(citation: str) -> str:
        """
        Normalize neutral citation to canonical form for matching.

        Examples:
        - "2007 BCCA 315" -> "2007BCCA315"
        - "2007 BCCA 315 (CanLII)" -> "2007BCCA315"
        - "TB2-06788" -> "TB206788" (IRB decisions)
        """
        if not citation:
            return ""

        # Remove common suffixes
        citation = re.sub(r"\s*\(CanLII\)\s*", "", citation, flags=re.IGNORECASE)
        citation = re.sub(r"\s*\[.*?\]\s*", "", citation)  # Remove [brackets]

        # Normalize whitespace
        citation = re.sub(r"\s+", "", citation)

        return citation.lower()

    @staticmethod
    def extract_year(citation: str) -> int | None:
        """Extract decision year from citation."""
        match = re.search(r"\b(19|20)\d{2}\b", citation)
        return int(match.group(0)) if match else None


class DecisionDeduplicator:
    """Dry-run dedup logic for A2AJ decisions against iLit corpus."""

    def __init__(self, existing_decisions: dict | None = None):
        """
        Initialize deduplicator with existing decisions.

        existing_decisions: dict mapping normalized_citation -> decision dict
        """
        self.existing_decisions = existing_decisions or {}
        self.normalizer = CitationNormalizer()

    def add_existing_decision(self, citation: str, date_str: str):
        """Add an existing decision to the dedup index."""
        norm_citation = self.normalizer.normalize_citation(citation)
        key = (norm_citation, date_str)
        self.existing_decisions[key] = True

    def is_duplicate(
        self, a2aj_citation: str, a2aj_date: date | str, tolerance_days: int = 1
    ) -> bool:
        """
        Check if A2AJ decision is a duplicate.

        Args:
            a2aj_citation: Citation from A2AJ dataset
            a2aj_date: Decision date from A2AJ
            tolerance_days: Allow date matches within N days (for date parsing differences)

        Returns:
            True if decision is likely a duplicate
        """
        if isinstance(a2aj_date, str):
            try:
                a2aj_date = datetime.fromisoformat(a2aj_date.replace("+00:00", "")).date()
            except:
                return False

        norm_citation = self.normalizer.normalize_citation(a2aj_citation)

        # Exact match
        if (norm_citation, str(a2aj_date)) in self.existing_decisions:
            return True

        # Check within tolerance window
        for i in range(-tolerance_days, tolerance_days + 1):
            check_date = a2aj_date + timedelta(days=i)
            if (norm_citation, str(check_date)) in self.existing_decisions:
                return True

        return False

    def assess_batch(self, a2aj_decisions: list[dict], sample_size: int = 100) -> dict:
        """
        Assess dedup rate for a batch of A2AJ decisions.

        Args:
            a2aj_decisions: List of decision dicts from A2AJ
            sample_size: Number to analyze (default 100)

        Returns:
            Stats dict with duplicate_count, new_count, etc.
        """
        duplicates = 0
        new_decisions = 0
        errors = 0

        for i, decision in enumerate(a2aj_decisions[:sample_size]):
            try:
                if self.is_duplicate(
                    decision.get("citation", ""), decision.get("date", "")
                ):
                    duplicates += 1
                else:
                    new_decisions += 1
            except Exception as e:
                logger.warning(f"Error checking decision {i}: {e}")
                errors += 1

        return {
            "total_checked": min(len(a2aj_decisions), sample_size),
            "duplicates": duplicates,
            "new": new_decisions,
            "errors": errors,
            "duplicate_rate": (
                duplicates / (duplicates + new_decisions) * 100
                if duplicates + new_decisions > 0
                else 0
            ),
        }


def dry_run_dedup():
    """Dry-run: simulate dedup against mock iLit corpus."""
    logger.info("Dry-run A2AJ deduplication against simulated iLit corpus\n")

    # Simulate existing iLit decisions (small sample)
    dedup = DecisionDeduplicator()

    # Add some "existing" decisions from iLit
    existing = [
        ("2007 BCCA 315", "2007-06-01"),
        ("2015 FC 123", "2015-02-14"),
        ("2019 FCA 456", "2019-11-22"),
        ("TB2-06788", "2013-06-06"),  # RPD decision
        ("2020 RAD 789", "2020-03-15"),  # RAD decision
    ]

    logger.info(f"✓ Simulated iLit corpus: {len(existing)} decisions")
    for citation, date_str in existing:
        dedup.add_existing_decision(citation, date_str)

    # Test dedup on a2aj decisions (some duplicates, some new)
    a2aj_test = [
        {"citation": "2007 BCCA 315", "date": "2007-06-01"},  # Exact duplicate
        {"citation": "2007 BCCA 315 (CanLII)", "date": "2007-06-01"},  # Same, different format
        {"citation": "2015 FC 123", "date": "2015-02-15"},  # Different date (tolerance test)
        {"citation": "2021 BCCA 999", "date": "2021-09-10"},  # New decision
        {"citation": "TB2-06788", "date": "2013-06-06"},  # IRB duplicate
        {"citation": "2022 FCA 111", "date": "2022-05-20"},  # New FCA decision
    ]

    logger.info(f"✓ Testing against {len(a2aj_test)} A2AJ decisions:\n")

    duplicates = 0
    new = 0

    for i, decision in enumerate(a2aj_test):
        is_dup = dedup.is_duplicate(decision["citation"], decision["date"])
        status = "DUPLICATE" if is_dup else "NEW"
        duplicates += is_dup
        new += not is_dup
        logger.info(f"  [{i+1}] {decision['citation']:20} ({decision['date']}) → {status}")

    logger.info(f"\n✓ Dedup results:")
    logger.info(f"  Duplicates found: {duplicates}/{len(a2aj_test)}")
    logger.info(f"  New decisions: {new}/{len(a2aj_test)}")
    logger.info(f"  Duplicate rate: {duplicates/len(a2aj_test)*100:.1f}%")

    # Scale estimate
    total_a2aj = 226147
    estimated_dupes = int(total_a2aj * (duplicates / len(a2aj_test)))
    estimated_new = total_a2aj - estimated_dupes

    logger.info(f"\n✓ Scaled to full A2AJ dataset (~226K decisions):")
    logger.info(f"  Est. duplicates: ~{estimated_dupes:,}")
    logger.info(f"  Est. new decisions to add: ~{estimated_new:,}")

    logger.info(f"\n✓ Court breakdown for CBSA relevance:")
    courts_priority = {
        "FC": "Primary (Federal Court)",
        "FCA": "Primary (Federal Court of Appeal)",
        "RAD": "Primary (Refugee Appeal Division)",
        "RPD": "Secondary (Refugee Protection Division context)",
        "SCC": "Reference (Supreme Court)",
        "BCCA": "Out of scope (Provincial Appeals)",
        "ONCA": "Out of scope (Provincial Appeals)",
    }
    for court, relevance in courts_priority.items():
        logger.info(f"  {court:8} → {relevance}")


if __name__ == "__main__":
    dry_run_dedup()
