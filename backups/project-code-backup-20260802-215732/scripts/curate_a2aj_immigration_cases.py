"""Select and import a core A2AJ immigration dataset.

This script builds a balanced immigration-focused seed set from the full A2AJ
Federal Court parquet source. It prioritizes cases with immigration-party
signals, immigration issue keywords, and case patterns commonly seen in Federal
Court immigration review work.
"""
import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import date, datetime
from hashlib import sha256
from pathlib import Path

import pyarrow.parquet as pq
from sqlalchemy import select

from backend.database import Case, SessionLocal

SOURCE = Path("data/raw/a2aj/FC/train.parquet")
DEFAULT_LIMIT = 60
DEFAULT_PER_BUCKET = 10
SOURCE_TYPE = "a2aj_immigration_core"
DEFAULT_MIN_ANCHOR_SCORE = 1
DEFAULT_MIN_TOTAL_SCORE = 1

BUCKET_PATTERNS: dict[str, tuple[str, ...]] = {
	"refugee_protection": (
		r"(?i)non[- ]?refoulement",
		r"(?i)refugee protection division|\bRPD\b",
		r"(?i)refugee appeal division|\bRAD\b",
		r"(?i)refugee claim|protected person|convention refugee|asylum",
		r"(?i)torture|cruel and unusual|ill[- ]?treatment|risk on return",
		r"(?i)safe third country|safe-third-country",
	),
	"review_procedure": (
		r"(?i)judicial review|application for judicial review|reasonableness",
		r"(?i)procedural fairness|duty of fairness|natural justice",
		r"(?i)certiorari|mandamus|prohibition",
		r"(?i)board decision|tribunal decision|decision maker",
	),
	"removal_detention": (
		r"(?i)removal order|stay of removal|deportation|deport",
		r"(?i)detention review|detained|detention",
		r"(?i)inadmissib|security inadmissib|criminal inadmissib|misrepresentation",
		r"(?i)PRRA|pre[- ]?removal risk assessment",
	),
	"family_status": (
		r"(?i)sponsorship|spousal sponsorship|family class|spouse|common[- ]law partner",
		r"(?i)humanitarian and compassionate|\bH&C\b",
		r"(?i)best interests of the child|child|children|minor",
		r"(?i)citizenship|permanent resident|PR card|residency obligation",
	),
	"agency_review": (
		r"(?i)\bIMM[- ]?\d",
		r"(?i)\bIRCC\b|Immigration, Refugees and Citizenship Canada|Citizenship and Immigration Canada",
		r"(?i)\bCBSA\b|Canada Border Services Agency|Border Services Agency",
		r"(?i)\bMinister\b|Minister of Public Safety|MPSEP|Minister of Public Safety and Emergency Preparedness",
	),
}

BUCKET_ORDER = [
	"refugee_protection",
	"review_procedure",
	"removal_detention",
	"family_status",
	"agency_review",
]

IMMIGRATION_ANCHORS: tuple[str, ...] = (
	r"(?i)\bIMM[- ]?\d",
	r"(?i)\bIRCC\b|Immigration, Refugees and Citizenship Canada|Citizenship and Immigration Canada",
	r"(?i)\bCBSA\b|Canada Border Services Agency|Border Services Agency",
	r"(?i)\bMinister\b|Minister of Public Safety|MPSEP|Minister of Public Safety and Emergency Preparedness",
	r"(?i)non[- ]?refoulement|refugee claim|protected person|convention refugee|asylum",
	r"(?i)removal order|stay of removal|deportation|detention review|PRRA|pre[- ]?removal risk assessment",
	r"(?i)spousal sponsorship|family class|common[- ]law partner|humanitarian and compassionate|\bH&C\b",
)


def clamp_text(value, max_length: int) -> str | None:
	if value is None:
		return None
	normalized = " ".join(str(value).split()).strip()
	if not normalized:
		return None
	if len(normalized) <= max_length:
		return normalized
	return normalized[:max_length].rstrip()


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("source_file", type=Path, nargs="?", default=SOURCE)
	parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Maximum cases to import")
	parser.add_argument("--per-bucket", type=int, default=DEFAULT_PER_BUCKET, help="Max cases to take from each bucket before fallback filling")
	parser.add_argument("--min-anchor-score", type=int, default=DEFAULT_MIN_ANCHOR_SCORE, help="Require at least this many immigration anchor hits")
	parser.add_argument("--min-total-score", type=int, default=DEFAULT_MIN_TOTAL_SCORE, help="Require at least this keyword total score")
	parser.add_argument("--year-from", type=int, default=None, help="Optional earliest decision year to keep")
	parser.add_argument("--year-to", type=int, default=None, help="Optional latest decision year to keep")
	parser.add_argument("--tracks", nargs="*", choices=BUCKET_ORDER, default=None, help="Optional subset of immigration tracks to keep")
	parser.add_argument("--max-per-party", type=int, default=None, help="Optional cap per inferred party pattern")
	parser.add_argument("--export-json", type=Path, default=None, help="Optional path for deterministic selected-record export")
	parser.add_argument("--export-csv", type=Path, default=None, help="Optional path for deterministic selected-record CSV export")
	parser.add_argument("--dry-run", action="store_true")
	return parser.parse_args()


def value(record: dict, *names: str):
	for name in names:
		result = record.get(name)
		if result is not None and result != "":
			return result
	return None


def parse_date(value_to_parse) -> date | None:
	if isinstance(value_to_parse, datetime):
		return value_to_parse.date()
	if isinstance(value_to_parse, date):
		return value_to_parse
	if value_to_parse:
		return date.fromisoformat(str(value_to_parse)[:10])
	return None


def parse_datetime(value_to_parse) -> datetime | None:
	if isinstance(value_to_parse, datetime):
		return value_to_parse
	if value_to_parse:
		return datetime.fromisoformat(str(value_to_parse).replace("Z", "+00:00"))
	return None


def parse_version(value_to_parse) -> str | None:
	parsed = parse_datetime(value_to_parse)
	return parsed.isoformat() if parsed else None


def score_record(record: dict) -> dict[str, int]:
	title = str(value(record, "name_en", "name_fr") or "")
	text = str(value(record, "unofficial_text_en", "unofficial_text_fr") or "")
	citation = str(value(record, "citation_en", "citation_fr") or "")
	full = f"{title}\n{citation}\n{text}"
	return {
		bucket: sum(len(re.findall(pattern, full)) for pattern in patterns)
		for bucket, patterns in BUCKET_PATTERNS.items()
	}


def immigration_anchor_score(record: dict) -> int:
	title = str(value(record, "name_en", "name_fr") or "")
	text = str(value(record, "unofficial_text_en", "unofficial_text_fr") or "")
	citation = str(value(record, "citation_en", "citation_fr") or "")
	full = f"{title}\n{citation}\n{text}"
	return sum(len(re.findall(pattern, full)) for pattern in IMMIGRATION_ANCHORS)


def bucket_priority(bucket_scores: dict[str, int]) -> str | None:
	best_bucket = None
	best_score = 0
	for bucket in BUCKET_ORDER:
		score = bucket_scores.get(bucket, 0)
		if score > best_score:
			best_bucket = bucket
			best_score = score
	return best_bucket


def compute_total_score(bucket_scores: dict[str, int]) -> int:
	return sum(min(score, 5) for score in bucket_scores.values())


def infer_party_pattern(record: dict) -> str:
	title = str(value(record, "name_en", "name_fr") or "")
	match = re.search(r"\(([^\)]{3,80})\)", title)
	if match:
		return " ".join(match.group(1).split()).lower()
	compact = " ".join(title.split()).lower()
	if "citizenship and immigration" in compact:
		return "citizenship and immigration"
	if "public safety and emergency preparedness" in compact:
		return "public safety and emergency preparedness"
	if "attorney general" in compact:
		return "attorney general"
	if "minister" in compact:
		return "minister"
	return "other"


def select_candidates(
	source_file: Path,
	limit: int,
	per_bucket: int,
	min_anchor_score: int = DEFAULT_MIN_ANCHOR_SCORE,
	min_total_score: int = DEFAULT_MIN_TOTAL_SCORE,
	year_from: int | None = None,
	year_to: int | None = None,
	tracks: set[str] | None = None,
	max_per_party: int | None = None,
) -> list[dict]:
	rows: list[dict] = []
	for batch in pq.ParquetFile(source_file).iter_batches(
		batch_size=1024,
		columns=[
			"dataset",
			"citation_en",
			"citation2_en",
			"name_en",
			"document_date_en",
			"url_en",
			"scraped_timestamp_en",
			"unofficial_text_en",
			"cases_cited_en",
			"cases_citing_en",
			"citing_cases_count",
			"upstream_license",
		],
	):
		for record in batch.to_pylist():
			if value(record, "dataset") != "FC":
				continue
			decision_date = parse_date(value(record, "document_date_en", "document_date_fr"))
			if year_from is not None and decision_date and decision_date.year < year_from:
				continue
			if year_to is not None and decision_date and decision_date.year > year_to:
				continue
			anchor_score = immigration_anchor_score(record)
			bucket_scores = score_record(record)
			bucket = bucket_priority(bucket_scores)
			total_score = compute_total_score(bucket_scores)
			if not bucket:
				continue
			if tracks and bucket not in tracks:
				continue
			if total_score < min_total_score:
				continue
			if anchor_score < min_anchor_score:
				continue
			record["_bucket"] = bucket
			record["_bucket_scores"] = bucket_scores
			record["_anchor_score"] = anchor_score
			record["_score"] = total_score
			record["_party_pattern"] = infer_party_pattern(record)
			rows.append(record)

	rows.sort(
		key=lambda record: (
			-record["_anchor_score"],
			-record["_score"],
			BUCKET_ORDER.index(record["_bucket"]),
			record.get("citation_en") or "",
		)
	)

	selected: list[dict] = []
	selected_keys: set[str] = set()
	per_bucket_counts: dict[str, int] = defaultdict(int)
	party_counts: dict[str, int] = defaultdict(int)

	def row_key(record: dict) -> str:
		citation = str(record.get("citation_en") or "").strip().lower()
		if citation:
			return citation
		title = str(record.get("name_en") or "").strip().lower()
		return title or sha256(str(record.get("unofficial_text_en") or "").encode("utf-8")).hexdigest()

	for bucket in BUCKET_ORDER:
		for record in rows:
			if record["_bucket"] != bucket:
				continue
			if per_bucket_counts[bucket] >= per_bucket:
				break
			party = str(record.get("_party_pattern") or "other")
			if max_per_party is not None and party_counts[party] >= max_per_party:
				continue
			key = row_key(record)
			if key in selected_keys:
				continue
			selected.append(record)
			selected_keys.add(key)
			per_bucket_counts[bucket] += 1
			party_counts[party] += 1
			if len(selected) >= limit:
				return selected

	for record in rows:
		if len(selected) >= limit:
			break
		party = str(record.get("_party_pattern") or "other")
		if max_per_party is not None and party_counts[party] >= max_per_party:
			continue
		key = row_key(record)
		if key in selected_keys:
			continue
		selected.append(record)
		selected_keys.add(key)
		party_counts[party] += 1

	return selected


def export_selected_records(selected: list[dict], export_json: Path | None, export_csv: Path | None) -> None:
	if export_json is not None:
		export_json.parent.mkdir(parents=True, exist_ok=True)
		payload = [
			{
				"citation": record.get("citation_en"),
				"title": record.get("name_en"),
				"decision_date": str(record.get("document_date_en") or ""),
				"bucket": record.get("_bucket"),
				"anchor_score": record.get("_anchor_score"),
				"score": record.get("_score"),
				"party_pattern": record.get("_party_pattern"),
				"bucket_scores": record.get("_bucket_scores"),
				"source_url": record.get("url_en"),
			}
			for record in selected
		]
		export_json.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")

	if export_csv is not None:
		export_csv.parent.mkdir(parents=True, exist_ok=True)
		with export_csv.open("w", encoding="utf-8", newline="") as handle:
			writer = csv.DictWriter(
				handle,
				fieldnames=[
					"citation",
					"title",
					"decision_date",
					"bucket",
					"anchor_score",
					"score",
					"party_pattern",
					"source_url",
				],
			)
			writer.writeheader()
			for record in selected:
				writer.writerow(
					{
						"citation": record.get("citation_en"),
						"title": record.get("name_en"),
						"decision_date": str(record.get("document_date_en") or ""),
						"bucket": record.get("_bucket"),
						"anchor_score": record.get("_anchor_score"),
						"score": record.get("_score"),
						"party_pattern": record.get("_party_pattern"),
						"source_url": record.get("url_en"),
					}
				)


def build_case(record: dict) -> Case | None:
	title = clamp_text(value(record, "name_en", "name_fr"), 255)
	decision_date = parse_date(value(record, "document_date_en", "document_date_fr"))
	full_text = value(record, "unofficial_text_en", "unofficial_text_fr")
	citation = clamp_text(value(record, "citation_en", "citation_fr"), 255)
	if not title or not decision_date or not full_text:
		return None

	full_text_hash = sha256(full_text.encode("utf-8")).hexdigest()
	bucket_scores = record.get("_bucket_scores") or {}
	return Case(
		title=title,
		court="FC",
		jurisdiction="Canada",
		date=decision_date,
		citation=citation,
		secondary_citation=clamp_text(value(record, "citation2_en", "citation2_fr"), 255),
		full_text=full_text,
		source_url=clamp_text(value(record, "url_en", "url_fr"), 2048),
		source_name="A2AJ Canadian Legal Data",
		source_id=clamp_text(citation or full_text_hash, 255),
		source_type=SOURCE_TYPE,
		dataset_version=clamp_text(parse_version(value(record, "scraped_timestamp_en", "scraped_timestamp_fr")), 100),
		upstream_license=value(record, "upstream_license"),
		scraped_at=parse_datetime(value(record, "scraped_timestamp_en", "scraped_timestamp_fr")),
		language="en" if record.get("unofficial_text_en") else "fr",
		full_text_hash=full_text_hash,
		processing_status="raw",
		cases_cited=value(record, "cases_cited_en", "cases_cited_fr"),
		cases_citing=value(record, "cases_citing_en", "cases_citing_fr"),
		citing_cases_count=record.get("citing_cases_count"),
		metadata_json={
			"evaluation_group": "immigration_core",
			"selection_method": "balanced_keyword_score",
			"primary_bucket": record.get("_bucket"),
			"bucket_scores": bucket_scores,
			"verification_status": "a2aj_unverified",
		},
	)


def main() -> None:
	args = parse_args()
	if args.limit < 1:
		raise SystemExit("--limit must be at least 1")
	if args.per_bucket < 1:
		raise SystemExit("--per-bucket must be at least 1")
	if args.min_anchor_score < 0:
		raise SystemExit("--min-anchor-score must be zero or greater")
	if args.min_total_score < 1:
		raise SystemExit("--min-total-score must be at least 1")
	if args.year_from is not None and args.year_from < 1900:
		raise SystemExit("--year-from must be 1900 or greater")
	if args.year_to is not None and args.year_to < 1900:
		raise SystemExit("--year-to must be 1900 or greater")
	if args.year_from is not None and args.year_to is not None and args.year_from > args.year_to:
		raise SystemExit("--year-from must be less than or equal to --year-to")
	if args.max_per_party is not None and args.max_per_party < 1:
		raise SystemExit("--max-per-party must be at least 1")
	if not args.source_file.exists():
		raise SystemExit(f"Source file does not exist: {args.source_file}")
	tracks = set(args.tracks) if args.tracks else None

	selected = select_candidates(
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
	export_selected_records(selected, args.export_json, args.export_csv)
	with SessionLocal() as session:
		existing = set(session.scalars(select(Case.citation)).all())
		imported = 0
		for record in selected:
			citation = record.get("citation_en")
			if citation in existing:
				continue
			case = build_case(record)
			if case is None:
				continue
			if args.dry_run:
				print(f"would import: {case.citation or case.title} [{record.get('_bucket')}] score={record.get('_score')}")
			else:
				session.add(case)
			existing.add(citation)
			imported += 1
		if not args.dry_run:
			session.commit()

	print(f"selected={len(selected)} imported={imported} source_type={SOURCE_TYPE}")
	if args.export_json:
		print(f"export_json={args.export_json}")
	if args.export_csv:
		print(f"export_csv={args.export_csv}")
	for record in selected:
		print(
			f"{record.get('citation_en')} | {record.get('name_en')} | bucket={record.get('_bucket')} "
			f"| party={record.get('_party_pattern')} | anchors={record.get('_anchor_score')} | score={record.get('_score')}"
		)


if __name__ == "__main__":
	main()