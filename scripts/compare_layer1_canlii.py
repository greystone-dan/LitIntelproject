"""Compare local layer-1 metadata against CanLII API metadata for the master 300 cohort.

This script reuses the existing CanLII client wiring and the current local
metadata extractor. It reports which metadata-like fields appear in the CanLII
API payload but are missing locally.

Output:
- data/eval/reports/layer1_canlii_gap_report.json
- data/eval/reports/layer1_canlii_gap_report.csv
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env", override=True)
load_dotenv(PROJECT_ROOT / "backend" / ".env", override=True)

from backend.citation_pipeline.canlii import CanLiiApiClient
from backend.database import Case, SessionLocal
from backend.routes import _build_reader_extracted_metadata, _review_fc_priority_cases


DEFAULT_JSON = PROJECT_ROOT / "data" / "eval" / "reports" / "layer1_canlii_gap_report.json"
DEFAULT_CSV = PROJECT_ROOT / "data" / "eval" / "reports" / "layer1_canlii_gap_report.csv"

SKIP_KEY_RE = re.compile(
	r"^(?:"
	r"body|full_text|fulltext|html|markup|text|reasons|summary|result|decision|judgment|opinion|headnotes?"
	r"|citation|neutralcitation|neutral_citation|canliiurl|url|href|documenturl|pdfurl"
	r")$",
	re.IGNORECASE,
)

KEY_ALIASES: dict[str, str] = {
	"neutralcitation": "neutral_citation_text",
	"neutral_citation": "neutral_citation_text",
	"citation": "neutral_citation_text",
	"decisiondate": "decision_date_text",
	"date": "decision_date_text",
	"decision_date": "decision_date_text",
	"docket": "docket",
	"title": "style_of_cause_text",
	"case_name": "style_of_cause_text",
	"styleofcause": "style_of_cause_text",
	"style_of_cause": "style_of_cause_text",
	"coram": "panel_or_coram",
	"panel": "panel_or_coram",
	"judge": "judge",
	"judges": "judge_names_all",
	"language": "language_of_decision",
	"court": "court_level",
	"appellants": "applicants_all",
	"applicant": "applicants_all",
	"respondents": "respondents_all",
	"respondent": "respondents_all",
	"party": "applicants_all",
	"parties": "applicants_all",
	"hearingdate": "date_of_hearing",
	"placeofhearing": "place_of_hearing",
	"place_of_hearing": "place_of_hearing",
	"date_of_hearing": "date_of_hearing",
	"counsel": "counsel_for_applicant",
	"counsel_for_appellant": "counsel_for_applicant",
	"counsel_for_applicant": "counsel_for_applicant",
	"counsel_for_respondent": "counsel_for_respondent",
}


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--limit", type=int, default=300, help="Number of review cases to compare")
	parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
	parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
	parser.add_argument("--max-api-requests-per-second", type=int, default=2)
	return parser.parse_args()


def _normalize_key(value: str) -> str:
	return re.sub(r"[^a-z0-9]+", "", value.strip().lower())


def _flatten_metadata(payload: Any, *, prefix: str = "", depth: int = 0, max_depth: int = 2) -> dict[str, str]:
	items: dict[str, str] = {}
	if depth > max_depth:
		return items
	if isinstance(payload, dict):
		for key, value in payload.items():
			key_text = str(key)
			if SKIP_KEY_RE.search(key_text):
				continue
			path = f"{prefix}.{key_text}" if prefix else key_text
			if isinstance(value, (dict, list)):
				items.update(_flatten_metadata(value, prefix=path, depth=depth + 1, max_depth=max_depth))
			elif value is not None:
				items[path] = str(value)
	elif isinstance(payload, list):
		for index, value in enumerate(payload[:20]):
			path = f"{prefix}[{index}]" if prefix else f"[{index}]"
			if isinstance(value, (dict, list)):
				items.update(_flatten_metadata(value, prefix=path, depth=depth + 1, max_depth=max_depth))
			elif value is not None:
				items[path] = str(value)
	return items


def _api_field_names(payload: dict[str, Any] | None) -> dict[str, str]:
	if not payload:
		return {}
	selected: dict[str, str] = {}
	for path, value in _flatten_metadata(payload).items():
		parts = [part for part in re.split(r"[.\[\]]+", path) if part]
		if not parts:
			continue
		terminal = _normalize_key(parts[-1])
		if not terminal or SKIP_KEY_RE.search(terminal):
			continue
		selected[path] = value
	return selected


def _local_field_names(case: Case) -> dict[str, str]:
	rows = _build_reader_extracted_metadata(case, [], include_canonical_fields=False)
	fields: dict[str, str] = {}
	for row in rows:
		if not row.value:
			continue
		fields[row.key] = row.value
	return fields


def _mapped_api_keys(api_fields: dict[str, str]) -> dict[str, list[str]]:
	mapped: dict[str, list[str]] = defaultdict(list)
	for path, value in api_fields.items():
		terminal = _normalize_key(path.split(".")[-1].split("[")[0])
		canonical = KEY_ALIASES.get(terminal)
		if canonical:
			mapped[canonical].append(f"{path} = {value}")
	return mapped


def main() -> None:
	args = parse_args()
	client = CanLiiApiClient.from_env()
	if client is None:
		raise SystemExit(
			"CANLII_API_KEY is not available in the current environment. "
			"Set it in .env or the shell, then rerun this script."
		)

	with SessionLocal() as session:
		case_rows = _review_fc_priority_cases(session, limit=max(1, min(500, args.limit)))
		case_ids = [int(row["case_id"]) for row in case_rows if row.get("case_id") is not None]
		cases = list(session.scalars(select(Case).where(Case.id.in_(case_ids))))
		cases_by_id = {case.id: case for case in cases}

	results: list[dict[str, Any]] = []
	aggregate_api_only: Counter[str] = Counter()
	aggregate_local_only: Counter[str] = Counter()
	api_hits = 0
	api_misses = 0

	for case_id in case_ids:
		case = cases_by_id.get(case_id)
		if case is None:
			continue

		local_fields = _local_field_names(case)
		neutral = case.citation or case.secondary_citation or ""
		api_payload = client.lookup_by_neutral(neutral)
		api_fields = _api_field_names(api_payload if isinstance(api_payload, dict) else None)
		mapped_api = _mapped_api_keys(api_fields)

		local_keys = set(local_fields)
		api_keys = set(mapped_api)
		common_keys = local_keys & api_keys
		missing_local = sorted(api_keys - local_keys)
		missing_api = sorted(local_keys - api_keys)

		if api_fields:
			api_hits += 1
			for key in missing_local:
				aggregate_api_only[key] += 1
		for key in missing_api:
			aggregate_local_only[key] += 1
		if not api_fields:
			api_misses += 1

		results.append(
			{
				"case_id": case.id,
				"title": case.title,
				"citation": case.citation,
				"local_keys": sorted(local_keys),
				"api_keys": sorted(api_keys),
				"common_keys": sorted(common_keys),
				"missing_local_keys": missing_local,
				"missing_api_keys": missing_api,
				"api_field_paths": api_fields,
				"mapped_api_fields": mapped_api,
			}
		)

	args.json_out.parent.mkdir(parents=True, exist_ok=True)
	args.csv_out.parent.mkdir(parents=True, exist_ok=True)
	args.json_out.write_text(
		json.dumps(
			{
				"total_cases": len(results),
				"api_hits": api_hits,
				"api_misses": api_misses,
				"top_api_only_fields": aggregate_api_only.most_common(50),
				"top_local_only_fields": aggregate_local_only.most_common(50),
				"cases": results,
			},
			indent=2,
			default=str,
		),
		encoding="utf-8",
	)

	with args.csv_out.open("w", encoding="utf-8", newline="") as handle:
		import csv

		writer = csv.DictWriter(
			handle,
			fieldnames=[
				"case_id",
				"title",
				"citation",
				"api_keys",
				"local_keys",
				"missing_local_keys",
				"missing_api_keys",
			],
		)
		writer.writeheader()
		for row in results:
			writer.writerow(
				{
					"case_id": row["case_id"],
					"title": row["title"],
					"citation": row["citation"],
					"api_keys": "; ".join(row["api_keys"]),
					"local_keys": "; ".join(row["local_keys"]),
					"missing_local_keys": "; ".join(row["missing_local_keys"]),
					"missing_api_keys": "; ".join(row["missing_api_keys"]),
				}
			)

	print(
		json.dumps(
			{
				"total_cases": len(results),
				"api_hits": api_hits,
				"api_misses": api_misses,
				"json_out": str(args.json_out),
				"csv_out": str(args.csv_out),
			},
			indent=2,
		)
	)


if __name__ == "__main__":
	main()