#!/usr/bin/env python3
"""
Importer for historical point-in-time statute versions from justice.gc.ca.

Fetches statute versions from PITIndex.html and extracts text from
point-in-time HTML pages. Stores multiple versions with their in-force dates
to enable decision-date matching (core of Phase 1 requirement).

Available versions depend on the Justice Laws PIT index at import time; this
script does not guarantee a fixed version count or prove current library coverage.
"""

import logging
import re
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class PITIndexParser:
    """Parse point-in-time version info from justice.gc.ca PITIndex.html pages."""

    JUSTICE_BASE = "https://laws-lois.justice.gc.ca"

    @staticmethod
    def get_statute_code_from_url(statute_url: str) -> str:
        """Extract statute code from URL (e.g., 'i-2.5' from '/eng/acts/i-2.5/')."""
        match = re.search(r"/(?:acts|regulations)/([^/]+)", statute_url)
        return match.group(1) if match else None

    @classmethod
    def fetch_pitindex(cls, statute_url: str) -> list[dict] | None:
        """
        Fetch PITIndex.html for a statute and extract version date ranges.

        Returns list of dicts with 'start_date', 'end_date', 'pit_date', 'url'
        """
        try:
            code = cls.get_statute_code_from_url(statute_url)
            if not code:
                logger.warning(f"Could not extract code from {statute_url}")
                return None

            # Determine if Acts or Regulations
            statute_type = "acts" if "/acts/" in statute_url else "regulations"
            pitindex_url = f"{cls.JUSTICE_BASE}/eng/{statute_type}/{code}/PITIndex.html"

            logger.info(f"Fetching PITIndex from {pitindex_url}...")
            response = httpx.get(pitindex_url, timeout=30)
            if response.status_code != 200:
                logger.warning(f"Could not fetch PITIndex (status {response.status_code})")
                return None

            versions = cls._parse_pitindex_html(response.text, code, statute_type)
            logger.info(f"✓ Found {len(versions)} versions in PITIndex")
            return versions

        except Exception as e:
            logger.error(f"Error fetching PITIndex: {e}")
            return None

    @staticmethod
    def _parse_pitindex_html(html: str, code: str, statute_type: str) -> list[dict]:
        """Parse version entries from PITIndex HTML."""
        versions = []

        # Look for entries like:
        # <li><a href='20260326/P1TT3xt3.html'>From 2026-03-26 to 2026-09-21</a></li>
        pattern = r'<li><a href=[\'"](\d{8})/P1TT3xt3\.html[\'"]>From (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})</a></li>'

        for match in re.finditer(pattern, html):
            pit_date_str = match.group(1)
            start_str = match.group(2)
            end_str = match.group(3)

            try:
                pit_date = datetime.strptime(pit_date_str, "%Y%m%d").date()
                start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_str, "%Y-%m-%d").date()

                # The PIT date represents when this version was consolidated
                # Use start_date as the in_force_date for matching
                version_url = (
                    f"https://laws-lois.justice.gc.ca/eng/{statute_type}/{code}/"
                    f"{pit_date_str}/P1TT3xt3.html"
                )

                versions.append(
                    {
                        "pit_date": pit_date,
                        "in_force_date": start_date,
                        "end_date": end_date,
                        "url": version_url,
                        "date_range": f"{start_date} to {end_date}",
                    }
                )
            except Exception as e:
                logger.warning(f"Could not parse version entry: {e}")

        return versions


def dry_run_historical_versions() -> None:
    """Dry-run: fetch and analyze historical versions for IRPA and IRPR."""
    statutes = {
        "IRPA": "https://laws-lois.justice.gc.ca/eng/acts/i-2.5/",
        "IRPR": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
    }

    for name, url in statutes.items():
        logger.info(f"\n{'='*60}")
        logger.info(f"Analyzing {name}")
        logger.info("=" * 60)

        versions = PITIndexParser.fetch_pitindex(url)
        if not versions:
            logger.warning(f"Could not fetch versions for {name}")
            continue

        logger.info(f"\n✓ {name} has {len(versions)} historical versions:")
        for i, v in enumerate(versions[:5]):  # Show first 5
            logger.info(
                f"  [{i+1}] In-force: {v['in_force_date']} (PIT: {v['pit_date']}) "
                f"Range: {v['date_range']}"
            )

        if len(versions) > 5:
            logger.info(f"  ... and {len(versions) - 5} more")

        # Show statistics
        dates = [v["in_force_date"] for v in versions]
        logger.info(f"\n✓ Version history span: {min(dates)} to {max(dates)}")
        logger.info(f"  Total period: {(max(dates) - min(dates)).days} days")

        # Estimate scope
        logger.info(f"\n✓ Estimated database impact:")
        logger.info(f"  Versions to store: {len(versions)}")
        logger.info(f"  Estimated metadata per version: ~500 bytes")
        logger.info(f"  Total metadata: ~{len(versions)*500/1024:.1f} KB")
        logger.info(f"  Plus full_text or text_compressed per version")


if __name__ == "__main__":
    dry_run_historical_versions()
