"""Scheduled job to check saved searches and generate alerts for new matches.

Run this script periodically (e.g., hourly) on the PC to discover new case law
and FC docket entries matching saved searches.

Usage:
    python scripts/check_saved_searches.py

To schedule on Windows, add to Task Scheduler:
    - Program: python
    - Arguments: scripts/check_saved_searches.py
    - Frequency: hourly or daily
"""

import sys
import os
from datetime import datetime
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.database import (
    SessionLocal,
    SavedSearch,
    SearchAlert,
    FCActivityAlert,
    Case,
    CaseChunk,
    FCActivityCase,
)
from backend.saved_searches_service import (
    get_saved_search,
    find_new_matches,
    record_alert,
    update_last_check,
    get_recent_alerts,
)
from backend.search_service import perform_search
from backend.models import CaseSearchRequest


def check_all_searches():
    """Check all saved searches and record new alerts."""
    db = SessionLocal()
    try:
        searches = db.query(SavedSearch).all()

        if not searches:
            print("No saved searches found.")
            return

        print(f"Checking {len(searches)} saved search(es)...\n")

        total_new_alerts = 0

        for search in searches:
            print(f"Processing: '{search.name}'")
            print(f"  Query: {search.query}")
            print(f"  Last checked: {search.last_alert_check}")

            # Construct search request
            search_req = CaseSearchRequest(
                query=search.query,
                search_mode=search.search_mode,
                page=1,
                page_size=100,
                **search.filters,
            )

            # Perform search
            try:
                result = perform_search(db, search_req)

                # Filter for new cases since last check
                since = search.last_alert_check or datetime.min
                new_cases_found = 0

                for case in result.results:
                    if case.scraped_at and case.scraped_at > since:
                        # Record alert for this case
                        try:
                            alert = record_alert(
                                db=db,
                                search_id=search.id,
                                case_id=case.id,
                                chunk_id=None,
                                match_type="full_case",
                                relevance_score=None,
                            )
                            new_cases_found += 1
                            total_new_alerts += 1
                            print(f"    ✓ New: {case.title} [{case.citation or 'No citation'}]")
                        except Exception as e:
                            print(f"    ✗ Error recording alert for case {case.id}: {e}")

                # Check for FC Activity matches if search filters include any
                if search.filters.get("court", "").lower().find("federal") >= 0 or not search.filters.get("court"):
                    fc_activity_alerts = check_fc_activity(db, search)
                    print(f"    FC Activity: {fc_activity_alerts} new entries")
                    total_new_alerts += fc_activity_alerts

                # Update last check time
                update_last_check(db, search.id)
                print(f"  Result: Found {new_cases_found} new case(s)\n")

            except Exception as e:
                print(f"  Error performing search: {e}\n")
                continue

        print(f"\n{'='*50}")
        print(f"Summary: {total_new_alerts} total new results across all searches")
        print(f"Time: {datetime.now().isoformat()}")
        print(f"{'='*50}")

    finally:
        db.close()


def check_fc_activity(db: SessionLocal, search: SavedSearch) -> int:
    """Check FC activity for matches to saved search."""
    try:
        # Extract court filter
        court = search.filters.get("court", "")
        judge = search.filters.get("judge_name")

        # Query FC activity cases matching filters
        query = db.query(FCActivityCase)

        if court and court.lower() != "federal court":
            return 0

        # Simple filter: check if case number or title contains search query
        search_query = search.query.lower()
        matching_cases = [
            case for case in query.all()
            if search_query in (case.case_number or "").lower()
            or search_query in (case.case_name or "").lower()
        ]

        since = search.last_alert_check or datetime.min
        new_alerts = 0

        for case in matching_cases:
            # Check for new documents since last check
            recent_docs = [
                doc for doc in case.documents
                if doc.created_at > since
            ]

            for doc in recent_docs:
                try:
                    alert = FCActivityAlert(
                        search_id=search.id,
                        case_id=case.id,
                        entry_type=doc.entry_type or "document",
                    )
                    db.add(alert)
                    new_alerts += 1
                except Exception as e:
                    print(f"      Error recording FC activity alert: {e}")

        if new_alerts > 0:
            db.commit()

        return new_alerts

    except Exception as e:
        print(f"    Error checking FC activity: {e}")
        return 0


def main():
    """Main entry point."""
    print("Saved Searches Alert Check")
    print(f"Started at: {datetime.now().isoformat()}\n")

    try:
        check_all_searches()
        print("\n✓ Check completed successfully")
        return 0
    except Exception as e:
        print(f"\n✗ Check failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
