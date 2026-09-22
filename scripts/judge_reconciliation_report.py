"""Report stored judge metadata and canonical profile-link mismatches without writes."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.database import Case, CaseJudgeProfile, JudgeProfile, SessionLocal
from backend.metadata import extract_case_metadata
from fc_ingest.document_scraper import _is_judge_junk
from scripts.backfill_judge_profiles import extracted_judge, is_profileable_judge, normalize_judge_name


def _case_sample(case: Case, raw_judge: str, status: str) -> dict[str, Any]:
	metadata = _metadata_evidence(case)
	confidence = metadata.get("_field_confidence", {})
	return {
		"case_id": case.id,
		"title": case.title,
		"citation": case.citation,
		"date": getattr(case, "date", None),
		"source_name": getattr(case, "source_name", None),
		"source_type": getattr(case, "source_type", None),
		"raw_judge": raw_judge or None,
		"confidence": confidence.get("judge") if isinstance(confidence, dict) else None,
		"quality_flags": metadata.get("_quality_flags", []),
		"source_excerpt": (getattr(case, "full_text", None) or "")[:200],
		"status": status,
	}


def _metadata_evidence(case: Case) -> dict[str, Any]:
	metadata_value = getattr(case, "metadata_json", None)
	if not isinstance(metadata_value, dict):
		return {}
	reader = metadata_value.get("reader_extracted")
	if not isinstance(reader, dict):
		return metadata_value
	evidence = dict(metadata_value)
	evidence.update(reader)
	return evidence


def _fresh_judge_evidence(case: Case) -> tuple[str, dict[str, Any]]:
	payload = extract_case_metadata(getattr(case, "full_text", None))
	return str(payload.get("judge") or "").strip(), payload


def _append_sample(samples: dict[str, list[dict[str, Any]]], key: str, value: dict[str, Any], limit: int) -> None:
	if len(samples[key]) < limit:
		samples[key].append(value)


def build_report(
	cases: Iterable[Case],
	links: Iterable[CaseJudgeProfile],
	profiles: Iterable[JudgeProfile],
	*,
	sample_limit: int = 10,
	min_date: date | None = None,
	fresh_extraction: bool = False,
) -> dict[str, Any]:
	case_rows = [case for case in cases if min_date is None or (getattr(case, "date", None) and case.date >= min_date)]
	link_rows = list(links)
	profile_rows = list(profiles)
	linked_case_ids = {link.case_id for link in link_rows}
	linked_raw_by_case: dict[int, list[str]] = defaultdict(list)
	for link in link_rows:
		linked_raw_by_case[link.case_id].append(link.raw_name)

	samples: dict[str, list[dict[str, Any]]] = defaultdict(list)
	value_counts: Counter[str] = Counter()
	invalid_counts: Counter[str] = Counter()
	profileable_count = 0
	nonempty_count = 0
	valid_unlinked_count = 0
	invalid_linked_count = 0
	linked_without_valid_raw_count = 0
	confidence_bins: Counter[str] = Counter()
	fresh_counts: Counter[str] = Counter()
	fresh_confidence_bins: Counter[str] = Counter()
	fresh_mismatch_count = 0
	for case in case_rows:
		raw_judge = extracted_judge(case)
		if fresh_extraction:
			fresh_judge, fresh_metadata = _fresh_judge_evidence(case)
			if fresh_judge != raw_judge:
				fresh_mismatch_count += 1
			if not fresh_judge:
				fresh_counts["missing"] += 1
			elif is_profileable_judge(fresh_judge):
				fresh_counts["profileable"] += 1
				fresh_confidence = fresh_metadata.get("_field_confidence", {}).get("judge")
				if fresh_confidence is None:
					fresh_confidence_bins["missing"] += 1
				elif fresh_confidence < 0.78:
					fresh_confidence_bins["<0.78"] += 1
				elif fresh_confidence < 0.92:
					fresh_confidence_bins["0.78-0.91"] += 1
				elif fresh_confidence < 0.99:
					fresh_confidence_bins["0.92-0.98"] += 1
				else:
					fresh_confidence_bins["0.99+"] += 1
			else:
				fresh_counts["invalid"] += 1
		if not raw_judge:
			if case.id in linked_case_ids:
				linked_without_valid_raw_count += 1
				_append_sample(samples, "linked_without_valid_raw_judge", _case_sample(case, raw_judge, "missing"), sample_limit)
			continue
		nonempty_count += 1
		value_counts[raw_judge] += 1
		if is_profileable_judge(raw_judge):
			profileable_count += 1
			metadata = _metadata_evidence(case)
			confidence = metadata.get("_field_confidence", {}).get("judge") if isinstance(metadata.get("_field_confidence"), dict) else None
			if confidence is None:
				confidence_bins["missing"] += 1
			elif confidence < 0.78:
				confidence_bins["<0.78"] += 1
			elif confidence < 0.92:
				confidence_bins["0.78-0.91"] += 1
			elif confidence < 0.99:
				confidence_bins["0.92-0.98"] += 1
			else:
				confidence_bins["0.99+"] += 1
			if case.id not in linked_case_ids:
				valid_unlinked_count += 1
				_append_sample(samples, "valid_raw_without_profile_link", _case_sample(case, raw_judge, "valid_unlinked"), sample_limit)
			continue
		invalid_kind = "junk_pattern" if _is_judge_junk(raw_judge) else "malformed_profile_name"
		invalid_counts[invalid_kind] += 1
		if case.id in linked_case_ids:
			invalid_linked_count += 1
			_append_sample(samples, "invalid_raw_with_profile_link", _case_sample(case, raw_judge, invalid_kind), sample_limit)
		else:
			_append_sample(samples, "invalid_raw_without_profile_link", _case_sample(case, raw_judge, invalid_kind), sample_limit)

	profile_name_counts = Counter(profile.normalized_name for profile in profile_rows)
	mismatched_links = 0
	for case in case_rows:
		raw_judge = extracted_judge(case)
		for linked_raw in linked_raw_by_case.get(case.id, []):
			if linked_raw != raw_judge:
				mismatched_links += 1
				_append_sample(
					samples,
					"profile_link_raw_name_mismatch",
					_case_sample(case, raw_judge, "link_raw_name_mismatch") | {"linked_raw_name": linked_raw},
					sample_limit,
				)

	return {
		"read_only": True,
		"sample_limit": sample_limit,
		"min_date": min_date,
		"counts": {
			"total_cases": len(case_rows),
			"cases_with_nonempty_raw_judge": nonempty_count,
			"cases_with_profileable_raw_judge": profileable_count,
			"cases_with_invalid_raw_judge": nonempty_count - profileable_count,
			"cases_with_valid_raw_judge_without_profile_link": valid_unlinked_count,
			"cases_with_invalid_raw_judge_with_profile_link": invalid_linked_count,
			"linked_cases_without_valid_raw_judge": linked_without_valid_raw_count,
			"case_judge_profile_links": len(link_rows),
			"judge_profiles": len(profile_rows),
			"duplicate_normalized_profiles": sum(count - 1 for count in profile_name_counts.values() if count > 1),
			"profile_link_raw_name_mismatches": mismatched_links,
		},
		"invalid_raw_judge_kinds": dict(invalid_counts),
		"confidence_bins_for_profileable_judges": dict(confidence_bins),
		"fresh_extraction": {
			"enabled": fresh_extraction,
			"counts": dict(fresh_counts),
			"confidence_bins_for_profileable_judges": dict(fresh_confidence_bins),
			"cases_different_from_stored_judge": fresh_mismatch_count,
		},
		"top_raw_judge_values": [
			{"value": value, "case_count": count} for value, count in value_counts.most_common(25)
		],
		"samples": dict(samples),
		"normalization_note": "Profileability reuses scripts.backfill_judge_profiles.is_profileable_judge; this report performs no writes.",
	}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--sample-limit", type=int, default=10, help="Maximum samples per mismatch category.")
	parser.add_argument("--min-date", type=date.fromisoformat, help="Only include cases on or after YYYY-MM-DD.")
	parser.add_argument("--fresh-extraction", action="store_true", help="Re-extract judges from full_text for a read-only comparison.")
	parser.add_argument("--output", type=Path, help="Optional JSON output path; stdout is always written.")
	args = parser.parse_args()
	if args.sample_limit < 1 or args.sample_limit > 100:
		parser.error("--sample-limit must be between 1 and 100")
	with SessionLocal() as session:
		report = build_report(
			session.scalars(select(Case).order_by(Case.id)),
			session.scalars(select(CaseJudgeProfile).order_by(CaseJudgeProfile.id)),
			session.scalars(select(JudgeProfile).order_by(JudgeProfile.id)),
			sample_limit=args.sample_limit,
			min_date=args.min_date,
			fresh_extraction=args.fresh_extraction,
		)
	payload = json.dumps(report, ensure_ascii=False, indent=2, default=str)
	print(payload)
	if args.output:
		args.output.parent.mkdir(parents=True, exist_ok=True)
		args.output.write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
