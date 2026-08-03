"""Create a QA report for the immigration-core A2AJ selector output."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from scripts import curate_a2aj_immigration_cases as selector


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("source_file", type=Path, nargs="?", default=selector.SOURCE)
	parser.add_argument("--limit", type=int, default=selector.DEFAULT_LIMIT)
	parser.add_argument("--per-bucket", type=int, default=selector.DEFAULT_PER_BUCKET)
	parser.add_argument("--min-anchor-score", type=int, default=selector.DEFAULT_MIN_ANCHOR_SCORE)
	parser.add_argument("--min-total-score", type=int, default=selector.DEFAULT_MIN_TOTAL_SCORE)
	parser.add_argument("--year-from", type=int, default=None)
	parser.add_argument("--year-to", type=int, default=None)
	parser.add_argument("--tracks", nargs="*", choices=selector.BUCKET_ORDER, default=None)
	parser.add_argument("--max-per-party", type=int, default=None)
	parser.add_argument(
		"--report-json",
		type=Path,
		default=Path("data/eval/reports/immigration-core-selection-report.json"),
		help="Path to write machine-readable selection QA report",
	)
	return parser.parse_args()


def _anchor_bin(score: int) -> str:
	if score <= 5:
		return "0-5"
	if score <= 20:
		return "6-20"
	if score <= 100:
		return "21-100"
	if score <= 300:
		return "101-300"
	return "301+"


def main() -> None:
	args = parse_args()
	tracks = set(args.tracks) if args.tracks else None
	selected = selector.select_candidates(
		args.source_file,
		limit=args.limit,
		per_bucket=args.per_bucket,
		min_anchor_score=args.min_anchor_score,
		min_total_score=args.min_total_score,
		year_from=args.year_from,
		year_to=args.year_to,
		tracks=tracks,
		max_per_party=args.max_per_party,
	)

	bucket_counts = Counter(item.get("_bucket") for item in selected)
	party_counts = Counter(item.get("_party_pattern") for item in selected)
	year_counts = Counter()
	anchor_bins = Counter()
	top_records: list[dict[str, object]] = []

	for item in selected:
		decision_date = selector.parse_date(selector.value(item, "document_date_en", "document_date_fr"))
		if decision_date is not None:
			year_counts[str(decision_date.year)] += 1
		anchor_score = int(item.get("_anchor_score") or 0)
		anchor_bins[_anchor_bin(anchor_score)] += 1
		top_records.append(
			{
				"citation": item.get("citation_en"),
				"title": item.get("name_en"),
				"bucket": item.get("_bucket"),
				"party_pattern": item.get("_party_pattern"),
				"anchor_score": anchor_score,
				"score": int(item.get("_score") or 0),
			}
		)

	top_records.sort(key=lambda row: (-int(row["anchor_score"]), -int(row["score"]), str(row["citation"] or "")))

	report = {
		"summary": {
			"selected_cases": len(selected),
			"source_file": str(args.source_file),
			"limit": args.limit,
			"per_bucket": args.per_bucket,
			"min_anchor_score": args.min_anchor_score,
			"min_total_score": args.min_total_score,
			"year_from": args.year_from,
			"year_to": args.year_to,
			"tracks": sorted(tracks) if tracks else None,
			"max_per_party": args.max_per_party,
		},
		"distribution": {
			"by_bucket": dict(sorted(bucket_counts.items())),
			"by_party_pattern_top10": dict(party_counts.most_common(10)),
			"by_year": dict(sorted(year_counts.items())),
			"anchor_bins": dict(anchor_bins),
		},
		"top_records": top_records[:25],
	}

	args.report_json.parent.mkdir(parents=True, exist_ok=True)
	args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")

	print(f"selected_cases={len(selected)}")
	print(f"report_json={args.report_json}")
	print("bucket_distribution=")
	for bucket, count in sorted(bucket_counts.items()):
		print(f"  {bucket}: {count}")
	print("top_party_patterns=")
	for party, count in party_counts.most_common(10):
		print(f"  {party}: {count}")


if __name__ == "__main__":
	main()