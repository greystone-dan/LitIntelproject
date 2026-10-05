"""Check saved case searches and optionally persist previously unseen matches."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

SEARCH_FILTER_KEYS = (
	"cites",
	"government_outcome",
	"decision_outcome",
	"minister",
	"judge",
	"court",
	"year",
	"sort_by",
)


def _as_bool(value: Any) -> bool:
	if isinstance(value, bool):
		return value
	return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def _fetch_analytics_search_cases(db: Any, **kwargs: Any) -> dict[str, Any]:
	from backend.analytics_service import fetch_analytics_search_cases

	return fetch_analytics_search_cases(db, **kwargs)


def build_search_arguments(search: SavedSearch, result_limit: int) -> dict[str, Any]:
	filters = search.filters if isinstance(search.filters, dict) else {}
	return {
		"query": search.query or "",
		**{key: filters.get(key, "") for key in SEARCH_FILTER_KEYS},
		"search_full_text": _as_bool(filters.get("search_full_text")),
		"limit": max(1, min(result_limit, 100)),
		"offset": 0,
	}


def check_saved_search(
	db: Any,
	search: SavedSearch,
	*,
	result_limit: int = 100,
	apply: bool = False,
) -> dict[str, int]:
	"""Return bounded match counts; optionally save newly matching case alerts."""
	from backend.database import SearchAlert

	results = _fetch_analytics_search_cases(
		db, **build_search_arguments(search, result_limit)
	).get("results", [])
	existing = {
		alert.case_id
		for alert in db.query(SearchAlert)
		.filter(SearchAlert.search_id == search.id)
		.all()
	}
	new_case_ids = []
	for result in results:
		case_id = int(result["case_id"])
		if case_id in existing:
			continue
		existing.add(case_id)
		new_case_ids.append(case_id)
		if apply:
			db.add(
				SearchAlert(
					search_id=search.id,
					case_id=case_id,
					match_type="case_search",
				)
			)
	if apply:
		search.last_alert_check = datetime.now(timezone.utc)
		db.commit()
	return {
		"search_id": int(search.id),
		"matched_cases": len(results),
		"new_alerts": len(new_case_ids),
	}


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		description=(
			"Check saved case searches. The default is read-only; use --apply "
			"to record newly matching cases as alerts."
		)
	)
	parser.add_argument("--search-id", type=int, help="Check one saved search only")
	parser.add_argument(
		"--max-searches",
		type=int,
		default=25,
		help="Maximum saved searches to check (1-100; default: 25)",
	)
	parser.add_argument(
		"--max-results",
		type=int,
		default=100,
		help="Maximum matching cases evaluated per search (1-100; default: 100)",
	)
	parser.add_argument(
		"--apply",
		action="store_true",
		help="Persist new alert rows and last-check timestamps",
	)
	return parser


def main(argv: list[str] | None = None) -> int:
	args = build_parser().parse_args(argv)
	if not 1 <= args.max_searches <= 100:
		raise SystemExit("--max-searches must be between 1 and 100")
	if not 1 <= args.max_results <= 100:
		raise SystemExit("--max-results must be between 1 and 100")
	if args.search_id is not None and args.search_id <= 0:
		raise SystemExit("--search-id must be positive")

	from backend.database import SavedSearch, SessionLocal

	db = SessionLocal()
	try:
		query = db.query(SavedSearch).order_by(SavedSearch.id.asc())
		if args.search_id is not None:
			query = query.filter(SavedSearch.id == args.search_id)
		searches = query.limit(args.max_searches).all()
		results = [
			check_saved_search(
				db,
				search,
				result_limit=args.max_results,
				apply=args.apply,
			)
			for search in searches
		]
		print(
			json.dumps(
				{
					"mode": "apply" if args.apply else "dry-run",
					"checked_searches": len(results),
					"results": results,
				},
				sort_keys=True,
			)
		)
		return 0
	except Exception:
		db.rollback()
		raise
	finally:
		db.close()


if __name__ == "__main__":
	raise SystemExit(main())
