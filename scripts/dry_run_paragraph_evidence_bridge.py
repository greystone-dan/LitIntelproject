from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

from backend.database import CaseChunk, Citation, SessionLocal, StatuteReference
from backend.discussion_units_sandbox import load_discussion_unit_cohort, load_paragraph_assessments


DEFAULT_OUTPUT = Path("data/eval/llm_discussion_units_pilot/paragraph_evidence_bridge_dry_run.json")


def _chunk_integrity(chunk: CaseChunk) -> str:
	actual_hash = hashlib.sha256((chunk.text or "").encode("utf-8")).hexdigest()
	return "match" if actual_hash == chunk.text_hash else "mismatch"


def _evidence_rows(session: Any, case_id: int, chunk_ids: list[int]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
	if not chunk_ids:
		return [], []
	citations = session.scalars(
		select(Citation).where(Citation.source_case_id == case_id, Citation.chunk_id.in_(chunk_ids))
	).all()
	statutes = session.scalars(
		select(StatuteReference).where(
			StatuteReference.source_case_id == case_id,
			StatuteReference.chunk_id.in_(chunk_ids),
		)
	).all()
	citation_rows = [
		{
			"id": item.id,
			"chunk_id": item.chunk_id,
			"offset_start": item.offset_start,
			"offset_end": item.offset_end,
			"citation_kind": item.citation_kind,
			"normalized_citation": item.normalized_citation,
			"target_case_id": item.target_case_id,
		}
		for item in citations
	]
	statute_rows = [
		{
			"id": item.id,
			"chunk_id": item.chunk_id,
			"offset_start": item.offset_start,
			"offset_end": item.offset_end,
			"instrument_key": item.instrument_key,
			"normalized_reference": item.normalized_reference,
			"provision_section": item.provision_section,
			"provision_subsection": item.provision_subsection,
			"provision_paragraph": item.provision_paragraph,
		}
		for item in statutes
	]
	return citation_rows, statute_rows


def map_case(session: Any, case_id: int) -> list[dict[str, Any]]:
	assessment_payload = load_paragraph_assessments(case_id, enforce_cohort=False)
	assessments = assessment_payload["assessments"]
	chunks = session.scalars(
		select(CaseChunk)
		.where(CaseChunk.case_id == case_id, CaseChunk.chunk_set == "paragraph")
		.order_by(CaseChunk.chunk_index, CaseChunk.id)
	).all()
	chunks_by_paragraph: dict[str, list[CaseChunk]] = {}
	for chunk in chunks:
		if chunk.paragraph_start is not None:
			chunks_by_paragraph.setdefault(str(chunk.paragraph_start), []).append(chunk)

	all_chunk_ids = [chunk.id for chunk in chunks]
	citations, statutes = _evidence_rows(session, case_id, all_chunk_ids)
	citations_by_chunk: dict[int, list[dict[str, Any]]] = {}
	statutes_by_chunk: dict[int, list[dict[str, Any]]] = {}
	for citation in citations:
		citations_by_chunk.setdefault(citation["chunk_id"], []).append(citation)
	for statute in statutes:
		statutes_by_chunk.setdefault(statute["chunk_id"], []).append(statute)

	records: list[dict[str, Any]] = []
	for paragraph, assessment in sorted(assessments.items(), key=lambda item: int(item[0])):
		matches = chunks_by_paragraph.get(paragraph, [])
		if len(matches) != 1:
			records.append(
				{
					"case_id": case_id,
					"status": "unmatched" if not matches else "ambiguous",
					"paragraph": paragraph,
					"matching_chunk_ids": [chunk.id for chunk in matches],
					"reason": "no canonical paragraph chunk" if not matches else "multiple canonical chunks share paragraph_start",
					"assessment": assessment,
				}
			)
			continue
		chunk = matches[0]
		records.append(
			{
				"case_id": case_id,
				"status": "exact",
				"paragraph": paragraph,
				"chunk_id": chunk.id,
				"paragraph_start": chunk.paragraph_start,
				"paragraph_end": chunk.paragraph_end,
				"text_hash": chunk.text_hash,
				"hash_check": _chunk_integrity(chunk),
				"assessment": assessment,
				"citations": citations_by_chunk.get(chunk.id, []),
				"statute_references": statutes_by_chunk.get(chunk.id, []),
			}
		)

	for paragraph, matches in sorted(chunks_by_paragraph.items(), key=lambda item: int(item[0])):
		if paragraph in assessments:
			continue
		for chunk in matches:
			records.append(
				{
					"case_id": case_id,
					"status": "missing_assessment",
					"paragraph": paragraph,
					"chunk_id": chunk.id,
					"paragraph_start": chunk.paragraph_start,
					"paragraph_end": chunk.paragraph_end,
					"text_hash": chunk.text_hash,
					"hash_check": _chunk_integrity(chunk),
					"citations": citations_by_chunk.get(chunk.id, []),
					"statute_references": statutes_by_chunk.get(chunk.id, []),
				}
			)
	return records


def build_report(session: Any, case_ids: Iterable[int]) -> dict[str, Any]:
	records = [record for case_id in case_ids for record in map_case(session, case_id)]
	counts: dict[str, int] = {}
	for record in records:
		counts[record["status"]] = counts.get(record["status"], 0) + 1
	return {
		"mode": "read_only",
		"cohort": "discussion_unit_core_300",
		"case_count": len(list(case_ids)) if not isinstance(case_ids, list) else len(case_ids),
		"record_count": len(records),
		"counts": counts,
		"records": records,
	}


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Read-only paragraph assessment evidence mapper")
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	parser.add_argument("--limit", type=int, default=300)
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	if args.limit < 1 or args.limit > 300:
		raise SystemExit("--limit must be between 1 and 300")
	case_ids = list(load_discussion_unit_cohort())[: args.limit]
	with SessionLocal() as session:
		report = build_report(session, case_ids)
	report["case_ids"] = case_ids
	args.output.parent.mkdir(parents=True, exist_ok=True)
	args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
	print(json.dumps({key: report[key] for key in ("mode", "case_count", "record_count", "counts")}))
	print(f"report={args.output}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())