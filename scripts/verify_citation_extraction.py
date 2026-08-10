from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from openai import OpenAI, OpenAIError
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import RawCitationMatch, extract_raw_citation_matches
from backend.database import Case, CaseChunk, Citation, SessionLocal

DEFAULT_AUDIT_MODEL = os.getenv("OPENAI_AUDIT_MODEL", "gpt-4.1-nano")
DEFAULT_AUDIT_BUDGET_USD = float(os.getenv("OPENAI_AUDIT_BUDGET_USD", "0.10"))
DEFAULT_AUDIT_INPUT_COST_PER_1M = float(os.getenv("OPENAI_AUDIT_INPUT_COST_PER_1M", "0.10"))
DEFAULT_AUDIT_OUTPUT_COST_PER_1M = float(os.getenv("OPENAI_AUDIT_OUTPUT_COST_PER_1M", "0.40"))
DEFAULT_AUDIT_MAX_OUTPUT_TOKENS = int(os.getenv("OPENAI_AUDIT_MAX_OUTPUT_TOKENS", "300"))
DEFAULT_AUDIT_MAX_CHARS = int(os.getenv("OPENAI_AUDIT_MAX_CHARS", "5000"))


def load_fixtures(path: Path) -> list[dict[str, Any]]:
	if not path.exists():
		raise FileNotFoundError(f"Fixture file does not exist: {path}")
	fixtures: list[dict[str, Any]] = []
	if path.suffix.lower() == ".jsonl":
		for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
			if not line.strip():
				continue
			fixtures.append(_validate_fixture_item(json.loads(line), index))
		return fixtures

	payload = json.loads(path.read_text(encoding="utf-8"))
	if not isinstance(payload, list):
		raise ValueError("Fixture file must contain a top-level JSON array")
	for index, item in enumerate(payload, start=1):
		fixtures.append(_validate_fixture_item(item, index))
	return fixtures


def _validate_fixture_item(item: Any, index: int) -> dict[str, Any]:
	if not isinstance(item, dict):
		raise ValueError(f"Fixture #{index} must be an object")
	text = item.get("text")
	expected = item.get("expected")
	if not isinstance(text, str) or not text.strip():
		raise ValueError(f"Fixture #{index} requires non-empty text")
	if not isinstance(expected, list):
		raise ValueError(f"Fixture #{index} requires an expected list")
	return item


def _match_key(match: dict[str, Any]) -> tuple[str, str, int, int]:
	return (
		str(match.get("kind") or ""),
		str(match.get("normalized_citation") or ""),
		int(match.get("offset_start") or 0),
		int(match.get("offset_end") or 0),
	)


def _context_snippet(text: str, offset_start: int, offset_end: int, radius: int = 80) -> str:
	start = max(0, offset_start - radius)
	end = min(len(text), offset_end + radius)
	return text[start:end]


def estimate_tokens(text: str) -> int:
	return max(1, len(text) // 4)


def estimate_chat_cost_usd(
	*,
	input_tokens: int,
	output_tokens: int,
	input_cost_per_1m: float,
	output_cost_per_1m: float,
) -> float:
	return ((max(0, input_tokens) / 1_000_000.0) * input_cost_per_1m) + (
		(max(0, output_tokens) / 1_000_000.0) * output_cost_per_1m
	)


def _raw_match_to_dict(match: RawCitationMatch, *, text: str | None = None) -> dict[str, Any]:
	payload = {
		"kind": match.kind,
		"citation_text": match.citation_text,
		"normalized_citation": match.normalized_citation,
		"offset_start": match.offset_start,
		"offset_end": match.offset_end,
	}
	if text is not None:
		payload["context_snippet"] = _context_snippet(text, match.offset_start, match.offset_end)
		payload["trailing_text"] = text[match.offset_end:match.offset_end + 16]
		payload["leading_text"] = text[max(0, match.offset_start - 16):match.offset_start]
	return payload


def _kind_matches(kind_filter: str | None, kind: str | None) -> bool:
	if not kind_filter or kind_filter == "all":
		return True
	return str(kind or "").lower() == kind_filter.lower()


def _stored_citation_to_dict(citation: Citation, *, text: str) -> dict[str, Any]:
	offset_start = int(citation.offset_start or 0)
	offset_end = int(citation.offset_end or offset_start)
	payload = {
		"kind": "case",
		"citation_text": citation.citation_text or text[offset_start:offset_end],
		"normalized_citation": citation.normalized_citation,
		"offset_start": offset_start,
		"offset_end": offset_end,
		"citation_id": citation.id,
		"target_case_id": citation.target_case_id,
		"unresolved": citation.unresolved,
	}
	if text:
		payload["context_snippet"] = _context_snippet(text, offset_start, offset_end)
		payload["trailing_text"] = text[offset_end:offset_end + 16]
		payload["leading_text"] = text[max(0, offset_start - 16):offset_start]
	return payload


def _dict_to_raw_match(row: dict[str, Any]) -> RawCitationMatch:
	return RawCitationMatch(
		kind=str(row.get("kind") or "unknown"),
		citation_text=str(row.get("citation_text") or ""),
		normalized_citation=str(row.get("normalized_citation") or ""),
		offset_start=int(row.get("offset_start") or 0),
		offset_end=int(row.get("offset_end") or 0),
	)


def validate_actual_spans(text: str, matches: list[RawCitationMatch]) -> list[dict[str, Any]]:
	errors: list[dict[str, Any]] = []
	for match in matches:
		span_text = text[match.offset_start:match.offset_end]
		if span_text != match.citation_text:
			errors.append(
				{
					"kind": match.kind,
					"expected_text": match.citation_text,
					"span_text": span_text,
					"offset_start": match.offset_start,
					"offset_end": match.offset_end,
				}
			)
	return errors


def evaluate_fixtures(fixtures: list[dict[str, Any]]) -> dict[str, Any]:
	totals = {
		"fixtures": len(fixtures),
		"expected": 0,
		"actual": 0,
		"matched": 0,
		"missing": 0,
		"unexpected": 0,
		"span_errors": 0,
	}
	by_kind: dict[str, Counter[str]] = defaultdict(Counter)
	results: list[dict[str, Any]] = []

	for index, fixture in enumerate(fixtures, start=1):
		fixture_id = str(fixture.get("id") or f"fixture_{index}")
		text = str(fixture["text"])
		expected_rows = [row for row in fixture["expected"] if isinstance(row, dict)]
		actual_matches = extract_raw_citation_matches(text)
		span_errors = validate_actual_spans(text, actual_matches)

		expected_map = {_match_key(row): row for row in expected_rows}
		actual_rows = [_raw_match_to_dict(row, text=text) for row in actual_matches]
		actual_map = {_match_key(row): row for row in actual_rows}

		missing_keys = sorted(set(expected_map) - set(actual_map))
		unexpected_keys = sorted(set(actual_map) - set(expected_map))
		matched_keys = sorted(set(expected_map) & set(actual_map))

		totals["expected"] += len(expected_rows)
		totals["actual"] += len(actual_rows)
		totals["matched"] += len(matched_keys)
		totals["missing"] += len(missing_keys)
		totals["unexpected"] += len(unexpected_keys)
		totals["span_errors"] += len(span_errors)

		for row in expected_rows:
			by_kind[str(row.get("kind") or "unknown")]["expected"] += 1
		for row in actual_rows:
			by_kind[str(row.get("kind") or "unknown")]["actual"] += 1
		for key in matched_keys:
			by_kind[key[0]]["matched"] += 1
		for key in missing_keys:
			by_kind[key[0]]["missing"] += 1
		for key in unexpected_keys:
			by_kind[key[0]]["unexpected"] += 1

		results.append(
			{
				"id": fixture_id,
				"matched": len(matched_keys),
				"missing": [expected_map[key] for key in missing_keys],
				"unexpected": [actual_map[key] for key in unexpected_keys],
				"span_errors": span_errors,
			}
		)

	precision = (totals["matched"] / totals["actual"]) if totals["actual"] else 1.0
	recall = (totals["matched"] / totals["expected"]) if totals["expected"] else 1.0

	return {
		"summary": {
			**totals,
			"precision": precision,
			"recall": recall,
		},
		"by_kind": {
			kind: {
				**counts,
				"precision": (counts["matched"] / counts["actual"]) if counts["actual"] else 1.0,
				"recall": (counts["matched"] / counts["expected"]) if counts["expected"] else 1.0,
			}
			for kind, counts in sorted(by_kind.items())
		},
		"results": results,
	}


def build_sample_report(
	samples: list[dict[str, Any]],
	*,
	source: str,
	rows_scanned: int,
	kind_filter: str | None = None,
) -> dict[str, Any]:
	total_citations = 0
	span_errors_total = 0
	results: list[dict[str, Any]] = []

	for index, sample in enumerate(samples, start=1):
		text = str(sample["text"])
		provided_actual = [row for row in sample.get("actual", []) if isinstance(row, dict)]
		if provided_actual:
			actual_rows = provided_actual
			actual_matches = [_dict_to_raw_match(row) for row in actual_rows]
			span_errors = []
		else:
			actual_matches = [
				match if isinstance(match, RawCitationMatch) else RawCitationMatch(**match)
				for match in sample.get("matches", [])
			]
			if not actual_matches:
				actual_matches = extract_raw_citation_matches(text)
			actual_rows = [_raw_match_to_dict(match, text=text) for match in actual_matches]
			span_errors = validate_actual_spans(text, actual_matches)
		if kind_filter:
			actual_rows = [row for row in actual_rows if _kind_matches(kind_filter, row.get("kind"))]
			actual_matches = [match for match in actual_matches if _kind_matches(kind_filter, match.kind)]
		total_citations += len(actual_rows)
		span_errors_total += len(span_errors)
		results.append(
			{
				"id": str(sample.get("id") or f"sample_{index}"),
				**{key: value for key, value in sample.items() if key not in {"id", "text", "matches"}},
				"text_length": len(text),
				"actual": actual_rows,
				"span_errors": span_errors,
			}
		)

	return {
		"summary": {
			"mode": "sample_canonical",
			"source": source,
			"rows_scanned": rows_scanned,
			"sampled": len(results),
			"citations": total_citations,
			"span_errors": span_errors_total,
		},
		"results": results,
	}


def _sample_text_for_audit(text: str, max_chars: int) -> str:
	if max_chars == 0:
		return text
	if max_chars < 200:
		raise ValueError("max_chars must be at least 200")
	if len(text) <= max_chars:
		return text
	head = max_chars // 2
	tail = max_chars - head
	return text[:head] + "\n[...truncated for audit...]\n" + text[-tail:]


def build_openai_audit_messages(sample: dict[str, Any], *, max_chars: int) -> list[dict[str, str]]:
	text = _sample_text_for_audit(str(sample.get("text") or ""), max_chars)
	actual = sample.get("actual") or []
	actual_slim = [
		{
			"kind": row.get("kind"),
			"citation_text": row.get("citation_text"),
			"normalized_citation": row.get("normalized_citation"),
			"unresolved": row.get("unresolved"),
		}
		for row in actual
	]
	metadata = {
		"id": sample.get("id"),
		"case_id": sample.get("case_id"),
		"title": sample.get("title"),
		"citation": sample.get("citation"),
		"court": sample.get("court"),
		"date": sample.get("date"),
	}
	system_prompt = (
		"You are auditing legal citation extraction. "
		"Review only the text and extracted citations provided. "
		"Return plain text lines only, no markdown and no JSON. "
		"Use exactly these prefixes: SUMMARY|, MISS|, BAD|. "
		"Format: SUMMARY|<confidence>|<notes>. "
		"Format: MISS|<kind>|<citation_text>|<reason>. "
		"Format: BAD|<suggested_kind>|<extracted_citation>|<issue>|<reason>. "
		"Return at most 12 missing_citations and at most 12 mischaracterized_citations, prioritizing the highest-confidence issues. "
		"Never use the pipe character inside a field value. "
		"Keep each reason under 20 words and avoid quoting long passages. "
		"Keep notes to one short sentence. Confidence must be one of high, medium, low. "
		"Do not include markdown fences or any text before or after the lines. "
		"Do not infer authorities that are not actually present in the text. "
		"Flag truncation when an extracted citation looks cut off, especially statutes with subsections. "
		"If trailing_text begins with characters like '(' or continues a subsection immediately after the extracted citation, treat that as truncation or mischaracterization. "
		"If an extracted citation is only a prefix of a longer citation visible in context, report it in mischaracterized_citations."
	)
	user_prompt = json.dumps(
		{
			"metadata": metadata,
			"extracted_citations": actual_slim,
			"text": text,
		},
		ensure_ascii=True,
	)
	return [
		{"role": "system", "content": system_prompt},
		{"role": "user", "content": user_prompt},
	]


def _parse_audit_payload(content: str) -> dict[str, Any]:
	text = content.strip()
	if "SUMMARY|" in text or "MISS|" in text or "BAD|" in text:
		payload: dict[str, Any] = {
			"missing_citations": [],
			"mischaracterized_citations": [],
			"notes": "",
			"confidence": "low",
		}
		for raw_line in text.splitlines():
			line = raw_line.strip()
			if not line:
				continue
			parts = [part.strip() for part in line.split("|")]
			if not parts:
				continue
			kind = parts[0].upper()
			if kind == "SUMMARY" and len(parts) >= 3:
				payload["confidence"] = parts[1] or "low"
				payload["notes"] = "|".join(parts[2:]).strip()
			elif kind == "MISS" and len(parts) >= 4:
				payload["missing_citations"].append(
					{
						"kind": parts[1],
						"citation_text": parts[2],
						"reason": "|".join(parts[3:]).strip(),
					}
				)
			elif kind == "BAD" and len(parts) >= 5:
				payload["mischaracterized_citations"].append(
					{
						"suggested_kind": parts[1],
						"extracted_citation": parts[2],
						"issue": parts[3],
						"reason": "|".join(parts[4:]).strip(),
					}
				)
		return payload
	if text.startswith("```"):
		text = re.sub(r"^```(?:json)?\s*", "", text)
		text = re.sub(r"\s*```$", "", text)
	if not text.startswith("{"):
		start = text.find("{")
		end = text.rfind("}")
		if start != -1 and end != -1 and end > start:
			text = text[start:end + 1]
	payload = json.loads(text)
	if not isinstance(payload, dict):
		raise ValueError("Audit response must be a JSON object")
	payload.setdefault("missing_citations", [])
	payload.setdefault("mischaracterized_citations", [])
	payload.setdefault("notes", "")
	payload.setdefault("confidence", "low")
	return payload


def run_openai_audit(
	report: dict[str, Any],
	*,
	client: Any,
	model: str,
	budget_usd: float,
	input_cost_per_1m: float,
	output_cost_per_1m: float,
	max_output_tokens: int,
	max_chars: int,
) -> dict[str, Any]:
	if budget_usd <= 0:
		raise ValueError("budget_usd must be positive")
	if max_output_tokens < 1:
		raise ValueError("max_output_tokens must be at least 1")

	spent_usd = 0.0
	processed = 0
	failed = 0
	results: list[dict[str, Any]] = []
	flagged_missing = 0
	flagged_mischaracterized = 0

	for sample in report.get("results", []):
		messages = build_openai_audit_messages(sample, max_chars=max_chars)
		estimated_input_tokens = sum(estimate_tokens(message["content"]) for message in messages)
		estimated_cost = estimate_chat_cost_usd(
			input_tokens=estimated_input_tokens,
			output_tokens=max_output_tokens,
			input_cost_per_1m=input_cost_per_1m,
			output_cost_per_1m=output_cost_per_1m,
		)
		if spent_usd + estimated_cost > budget_usd:
			break

		try:
			completion = client.chat.completions.create(
				model=model,
				temperature=0,
				max_tokens=max_output_tokens,
				messages=messages,
			)
			content = completion.choices[0].message.content or "{}"
			audit = _parse_audit_payload(content)
			usage = completion.usage
			input_tokens = int(getattr(usage, "prompt_tokens", estimated_input_tokens) or estimated_input_tokens)
			output_tokens = int(getattr(usage, "completion_tokens", max_output_tokens) or max_output_tokens)
			cost_usd = estimate_chat_cost_usd(
				input_tokens=input_tokens,
				output_tokens=output_tokens,
				input_cost_per_1m=input_cost_per_1m,
				output_cost_per_1m=output_cost_per_1m,
			)
			spent_usd += cost_usd
			processed += 1
			flagged_missing += len(audit.get("missing_citations", []))
			flagged_mischaracterized += len(audit.get("mischaracterized_citations", []))
			results.append(
				{
					"id": sample.get("id"),
					"model": model,
					"usage": {
						"prompt_tokens": input_tokens,
						"completion_tokens": output_tokens,
						"estimated_cost_usd": cost_usd,
					},
					"audit": audit,
				}
			)
		except (OpenAIError, ValueError, json.JSONDecodeError) as exc:
			failed += 1
			spent_usd += estimated_cost
			results.append(
				{
					"id": sample.get("id"),
					"model": model,
					"usage": {
						"prompt_tokens": estimated_input_tokens,
						"completion_tokens": max_output_tokens,
						"estimated_cost_usd": estimated_cost,
					},
					"error": str(exc),
				}
			)

	return {
		"summary": {
			"model": model,
			"budget_usd": budget_usd,
			"spent_usd": spent_usd,
			"processed": processed,
			"failed": failed,
			"flagged_missing": flagged_missing,
			"flagged_mischaracterized": flagged_mischaracterized,
		},
		"results": results,
	}


def _case_text(case: Case) -> str:
	full_text = case.full_text or ""
	if full_text.strip():
		return full_text
	return case.summary or ""


def load_case_ids_from_csv(path: Path) -> set[int]:
	if not path.exists():
		raise FileNotFoundError(f"Case ID CSV does not exist: {path}")
	case_ids: set[int] = set()
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		reader = csv.DictReader(handle)
		for row in reader:
			for key in ("local_case_id", "case_id", "id"):
				value = str(row.get(key) or "").strip()
				if value.isdigit():
					case_ids.add(int(value))
					break
	return case_ids


def sample_case_rows(limit: int, *, court: str | None = None, case_ids: set[int] | None = None) -> tuple[int, list[dict[str, Any]]]:
	batch_size = max(limit * 5, 50)
	rows_scanned = 0
	samples: list[dict[str, Any]] = []
	last_case_id = 0

	with SessionLocal() as session:
		while len(samples) < limit:
			statement = select(Case).where(Case.id > last_case_id).order_by(Case.id).limit(batch_size)
			if court:
				statement = statement.where(Case.court == court)
			if case_ids:
				statement = statement.where(Case.id.in_(sorted(case_ids)))
			cases = session.scalars(statement).all()
			if not cases:
				break
			for case in cases:
				last_case_id = case.id
				text = _case_text(case)
				if not text.strip():
					continue
				rows_scanned += 1
				matches = extract_raw_citation_matches(text)
				if not matches:
					continue
				samples.append(
					{
						"id": f"case:{case.id}",
						"case_id": case.id,
						"title": case.title,
						"citation": case.citation,
						"court": case.court,
						"date": case.date.isoformat(),
						"text": text,
						"matches": matches,
					}
				)
				if len(samples) >= limit:
					break

	return rows_scanned, samples


def sample_chunk_rows(limit: int) -> tuple[int, list[dict[str, Any]]]:
	batch_size = max(limit * 10, 100)
	rows_scanned = 0
	samples: list[dict[str, Any]] = []
	offset = 0

	with SessionLocal() as session:
		while len(samples) < limit:
			chunks = session.scalars(
				select(CaseChunk).order_by(CaseChunk.case_id, CaseChunk.chunk_index).offset(offset).limit(batch_size)
			).all()
			if not chunks:
				break
			offset += len(chunks)
			for chunk in chunks:
				text = chunk.text or ""
				if not text.strip():
					continue
				rows_scanned += 1
				matches = extract_raw_citation_matches(text)
				if not matches:
					continue
				samples.append(
					{
						"id": f"chunk:{chunk.case_id}:{chunk.chunk_index}",
						"case_id": chunk.case_id,
						"chunk_id": chunk.id,
						"chunk_index": chunk.chunk_index,
						"title": chunk.case.title if chunk.case is not None else None,
						"citation": chunk.case.citation if chunk.case is not None else None,
						"text": text,
						"matches": matches,
					}
				)
				if len(samples) >= limit:
					break

	return rows_scanned, samples


def _case_text_for_citation(case: Case | None) -> str:
	if case is None:
		return ""
	return _case_text(case)


def sample_existing_citation_groups(limit: int, *, source: str) -> tuple[int, list[dict[str, Any]]]:
	if source not in {"cases", "chunks"}:
		raise ValueError("source must be 'cases' or 'chunks'")
	rows_scanned = 0
	samples: list[dict[str, Any]] = []
	group_count = 0
	with SessionLocal() as session:
		if source == "chunks":
			chunk_ids = session.scalars(
				select(Citation.chunk_id)
				.where(Citation.chunk_id.is_not(None), Citation.target_case_id.is_not(None))
				.distinct()
				.order_by(Citation.chunk_id)
				.limit(limit)
			).all()
			for chunk_id in chunk_ids:
				chunk = session.get(CaseChunk, chunk_id)
				if chunk is None or not (chunk.text or "").strip():
					continue
				citation_rows = session.scalars(
					select(Citation)
					.where(Citation.chunk_id == chunk_id, Citation.target_case_id.is_not(None))
					.order_by(Citation.offset_start, Citation.id)
				).all()
				if not citation_rows:
					continue
				rows_scanned += len(citation_rows)
				samples.append(
					{
						"id": f"stored-chunk:{chunk.case_id}:{chunk.chunk_index}",
						"case_id": chunk.case_id,
						"chunk_id": chunk.id,
						"chunk_index": chunk.chunk_index,
						"title": chunk.case.title if chunk.case is not None else None,
						"citation": chunk.case.citation if chunk.case is not None else None,
						"text": chunk.text,
						"actual": [_stored_citation_to_dict(citation, text=chunk.text) for citation in citation_rows],
					}
				)
				group_count += 1
				if group_count >= limit:
					break
		else:
			case_ids = session.scalars(
				select(Citation.source_case_id)
				.where(Citation.target_case_id.is_not(None))
				.distinct()
				.order_by(Citation.source_case_id)
				.limit(limit)
			).all()
			for case_id in case_ids:
				case = session.get(Case, case_id)
				text = _case_text_for_citation(case)
				if not text.strip():
					continue
				citation_rows = session.scalars(
					select(Citation)
					.where(Citation.source_case_id == case_id, Citation.target_case_id.is_not(None))
					.order_by(Citation.chunk_id, Citation.offset_start, Citation.id)
				).all()
				if not citation_rows:
					continue
				rows_scanned += len(citation_rows)
				samples.append(
					{
						"id": f"stored-case:{case.id}",
						"case_id": case.id,
						"title": case.title,
						"citation": case.citation,
						"court": case.court,
						"date": case.date.isoformat(),
						"text": text,
						"actual": [
							_stored_citation_to_dict(citation, text=(citation.chunk.text if citation.chunk is not None else text))
							for citation in citation_rows
						],
					}
				)
				group_count += 1
				if group_count >= limit:
					break

	return rows_scanned, samples


def write_report(path: Path, report: dict[str, Any]) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Verify raw citation extraction against labeled fixtures")
	parser.add_argument("fixture_file", nargs="?", type=Path, help="Path to JSON or JSONL fixture file")
	parser.add_argument("--report-json", type=Path, default=None, help="Optional path to write full JSON report")
	parser.add_argument("--limit", type=int, default=None, help="Optional max number of fixtures to evaluate")
	parser.add_argument(
		"--sample-canonical",
		action="store_true",
		help="Sample stored cases or chunks and write extracted citations for manual audit",
	)
	parser.add_argument("--case-ids-csv", type=Path, default=None, help="Optional CSV restricting sampled case audit to listed case IDs")
	parser.add_argument(
		"--sample-source",
		choices=("cases", "chunks"),
		default="cases",
		help="Storage surface to sample when --sample-canonical is set",
	)
	parser.add_argument("--court", default=None, help="Optional court filter for case sampling")
	parser.add_argument(
		"--sample-existing-citations",
		action="store_true",
		help="Sample already stored citation rows from the database for external audit",
	)
	parser.add_argument("--openai-audit", action="store_true", help="Run a cheap OpenAI audit over sampled rows")
	parser.add_argument("--audit-model", default=DEFAULT_AUDIT_MODEL)
	parser.add_argument("--audit-budget-usd", type=float, default=DEFAULT_AUDIT_BUDGET_USD)
	parser.add_argument("--audit-input-cost-per-1m", type=float, default=DEFAULT_AUDIT_INPUT_COST_PER_1M)
	parser.add_argument("--audit-output-cost-per-1m", type=float, default=DEFAULT_AUDIT_OUTPUT_COST_PER_1M)
	parser.add_argument("--audit-max-output-tokens", type=int, default=DEFAULT_AUDIT_MAX_OUTPUT_TOKENS)
	parser.add_argument("--audit-max-chars", type=int, default=DEFAULT_AUDIT_MAX_CHARS, help="Max chars of case text to send to audit model; use 0 for full text")
	parser.add_argument("--kind-filter", default=None, choices=(None, "all", "neutral", "case", "statute", "instrument", "secondary"), help="Optional citation kind filter for sampled audits")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	if args.sample_canonical or args.sample_existing_citations:
		if args.fixture_file is not None:
			raise SystemExit("fixture_file is not used with sampling modes")
		if (args.sample_canonical or args.sample_existing_citations) and args.sample_source == "chunks" and args.court:
			raise SystemExit("--court is only supported with --sample-source cases")
		if args.report_json is None:
			raise SystemExit("--report-json is required with sampling modes")
		limit = args.limit or 25
		if limit < 1:
			raise SystemExit("--limit must be at least 1")
		case_ids = load_case_ids_from_csv(args.case_ids_csv) if args.case_ids_csv else None
		if args.sample_existing_citations:
			rows_scanned, samples = sample_existing_citation_groups(limit, source=args.sample_source)
			report = build_sample_report(samples, source=f"stored_{args.sample_source}", rows_scanned=rows_scanned, kind_filter=args.kind_filter)
		else:
			rows_scanned, samples = (
				sample_case_rows(limit, court=args.court, case_ids=case_ids)
				if args.sample_source == "cases"
				else sample_chunk_rows(limit)
			)
			report = build_sample_report(samples, source=args.sample_source, rows_scanned=rows_scanned, kind_filter=args.kind_filter)
		if args.openai_audit:
			api_key = os.getenv("OPENAI_API_KEY")
			if not api_key:
				raise SystemExit("OPENAI_API_KEY is required for --openai-audit")
			try:
				client = OpenAI(api_key=api_key)
				report["openai_audit"] = run_openai_audit(
					report,
					client=client,
					model=args.audit_model,
					budget_usd=args.audit_budget_usd,
					input_cost_per_1m=args.audit_input_cost_per_1m,
					output_cost_per_1m=args.audit_output_cost_per_1m,
					max_output_tokens=args.audit_max_output_tokens,
					max_chars=args.audit_max_chars,
				)
			except (OpenAIError, ValueError, json.JSONDecodeError) as exc:
				raise SystemExit(f"OpenAI audit failed: {exc}") from exc
		print(json.dumps(report["summary"], sort_keys=True))
		if "openai_audit" in report:
			print(json.dumps(report["openai_audit"]["summary"], sort_keys=True))
		write_report(args.report_json, report)
		return

	if args.fixture_file is None:
		raise SystemExit("fixture_file is required unless --sample-canonical is set")
	fixtures = load_fixtures(args.fixture_file)
	if args.limit is not None:
		if args.limit < 1:
			raise SystemExit("--limit must be at least 1")
		fixtures = fixtures[:args.limit]

	report = evaluate_fixtures(fixtures)
	summary = report["summary"]
	print(json.dumps(summary, sort_keys=True))

	if args.report_json:
		write_report(args.report_json, report)

	if summary["missing"] or summary["unexpected"] or summary["span_errors"]:
		raise SystemExit(1)


if __name__ == "__main__":
	main()