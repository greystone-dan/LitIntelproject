"""Paragraph tagging v2 (topic + role) for the 300 Core cases. Report-only; no database; open case law only.

Dry run by default (counts, token and cost estimate, no network). --send calls the model.
Fixes from the 2026-09-24 gpt-4.1-nano run: whole case in one call with json_object mode and max_tokens=6000 (long
cases were truncated -> broken JSON, ~17% of paragraphs missing). Here: windows of <=WINDOW paragraphs, strict JSON
schema, controlled role list, retries with backoff, missing-paragraph retry by splitting the window, spend ledger with a cap.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
for entry in (PROJECT_ROOT, PROJECT_ROOT / "scripts" / "ai_poc"):
	if str(entry) not in sys.path:
		sys.path.insert(0, str(entry))

from common import CapReached, PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402

REPORTS = PROJECT_ROOT / "data" / "eval" / "llm_discussion_units_pilot" / "core_300_run" / "reports"
PROMPT_VERSION = "tag_v2"
WINDOW = 40
MAX_PARAGRAPH_CHARS = 2500
ROLES = [
	"procedural_history", "background_facts", "issue_framing", "legal_test", "party_position",
	"evidence_assessment", "reasoning_application", "disposition", "other",
]

SYSTEM_V2 = (
	"You label the paragraphs of a Canadian immigration or refugee court or tribunal decision for a legal researcher. "
	"Return exactly one assessment for every supplied paragraph, in the same order, copying paragraph_index exactly. "
	"Judge each paragraph from its own text; the earlier-topic hint is only for keeping topic wording consistent.\n"
	"topic: 2 to 8 plain words naming the specific point of the paragraph (for example 'RAD credibility finding on identity "
	"documents' or 'standard of review: reasonableness'), not a generic word like 'Analysis'. Reuse the identical wording for "
	"adjacent paragraphs that continue the same point; change it only when the point changes.\n"
	"role, exactly one of: procedural_history (how the matter got here: prior decisions, hearings, appeal steps); "
	"background_facts (the claimant's or applicant's story and facts); issue_framing (the question(s) the court must decide, "
	"including standard of review labels); legal_test (law, statutes, cases and tests stated as the governing rule); "
	"party_position (what the applicant, respondent or decision-maker argued or found, reported not decided); "
	"evidence_assessment (the court weighing or describing evidence or the record); reasoning_application (the court applying the law "
	"to the facts and reaching a conclusion on a point); disposition (the final order, result, costs, certified question); "
	"other (headings, style of cause, counsel lists, page furniture, blank or unreadable text).\n"
	"explanation: one sentence of 25 words or fewer saying what the paragraph does, using only the paragraph text. "
	"Do not invent facts, citations, names or paragraph numbers.\n"
	"confidence: 0 to 1; use 0.5 or lower for headings, fragments, block quotations or paragraphs whose role is genuinely ambiguous."
)

SCHEMA = {
	"type": "object",
	"additionalProperties": False,
	"required": ["assessments"],
	"properties": {
		"assessments": {
			"type": "array",
			"items": {
				"type": "object",
				"additionalProperties": False,
				"required": ["paragraph_index", "topic", "role", "explanation", "confidence"],
				"properties": {
					"paragraph_index": {"type": "integer"},
					"topic": {"type": "string"},
					"role": {"type": "string", "enum": ROLES},
					"explanation": {"type": "string"},
					"confidence": {"type": "number"},
				},
			},
		}
	},
}


def load_paragraphs(report: dict) -> list[dict]:
	"""Same selection rule as the 2026-09-24 run (numbered [n] paragraphs when the decision has them), so results compare."""
	from scripts.package_discussion_units_llm import _legal_paragraphs

	rows = _legal_paragraphs(report.get("paragraphs", []))
	return [{"paragraph_index": int(r["paragraph_index"]), "text": str(r["text"])[:MAX_PARAGRAPH_CHARS]} for r in rows if str(r["text"]).strip()]


def windows(paragraphs: list[dict], size: int = WINDOW) -> list[list[dict]]:
	return [paragraphs[i:i + size] for i in range(0, len(paragraphs), size)]


def build_messages(case_id: int, chunk: list[dict], previous_topic: str | None) -> list[dict]:
	payload = {
		"case_id": case_id,
		"earlier_topic_hint": previous_topic or "",
		"paragraphs": [{"paragraph_index": p["paragraph_index"], "text": p["text"]} for p in chunk],
	}
	return [{"role": "system", "content": SYSTEM_V2}, {"role": "user", "content": json.dumps(payload, ensure_ascii=True)}]


def estimate_tokens(chunk: list[dict]) -> int:
	return int(len(SYSTEM_V2) / 3.5 + sum(len(p["text"]) for p in chunk) / 3.0 + 40 * len(chunk))


def tag_chunk(client, ledger, model, run, case_id, chunk, previous_topic, usage_total):
	"""Tag one window; paragraphs missing or invalid are retried by splitting the window; leftovers are marked missing."""
	want = [p["paragraph_index"] for p in chunk]
	label = f"case {case_id} paras {want[0]}-{want[-1]}"
	data, usage = call_json(
		client, ledger, run=run, model=model, messages=build_messages(case_id, chunk, previous_topic),
		schema_name="paragraph_assessments", schema=SCHEMA,
		max_output_tokens=max(1500, 130 * len(chunk)), est_input_tokens=estimate_tokens(chunk), label=label,
	)
	for key in ("prompt_tokens", "completion_tokens", "usd"):
		usage_total[key] = usage_total.get(key, 0) + usage[key]
	got = {}
	for item in data.get("assessments", []):
		index = item.get("paragraph_index")
		if index in want and index not in got and item.get("role") in ROLES and str(item.get("topic", "")).strip():
			got[index] = {**item, "confidence": max(0.0, min(1.0, float(item.get("confidence") or 0)))}
	missing = [i for i in want if i not in got]
	if missing and len(chunk) > 1:
		retry_chunk = [p for p in chunk if p["paragraph_index"] in missing]
		half = max(1, len(retry_chunk) // 2)
		for part in (retry_chunk[:half], retry_chunk[half:]):
			if part:
				try:
					got.update(tag_chunk(client, ledger, model, run, case_id, part, previous_topic, usage_total))
				except CapReached:
					raise
				except RuntimeError:
					pass
	return got


def tag_case(client, ledger, model, run, case_id, out_dir, force):
	target = out_dir / f"case_{case_id}_tags.json"
	if target.exists() and not force:
		return {"case_id": case_id, "status": "skipped"}
	report = json.loads((REPORTS / f"case_{case_id}_deterministic.json").read_text(encoding="utf-8"))
	paragraphs = load_paragraphs(report)
	assessments: dict[int, dict] = {}
	usage_total: dict = {}
	previous_topic = None
	errors = []
	for chunk in windows(paragraphs):
		try:
			got = tag_chunk(client, ledger, model, run, case_id, chunk, previous_topic, usage_total)
		except CapReached:
			raise
		except RuntimeError as exc:
			errors.append(str(exc))
			continue
		assessments.update(got)
		last = [got[p["paragraph_index"]] for p in chunk if p["paragraph_index"] in got]
		previous_topic = last[-1]["topic"] if last else previous_topic
	ordered = [assessments[p["paragraph_index"]] for p in paragraphs if p["paragraph_index"] in assessments]
	missing = [p["paragraph_index"] for p in paragraphs if p["paragraph_index"] not in assessments]
	result = {
		"case_id": case_id, "model": model, "prompt_version": PROMPT_VERSION, "run": run,
		"paragraph_count": len(paragraphs), "tagged_count": len(ordered), "missing_paragraph_indices": missing,
		"errors": errors, "usage": usage_total, "assessments": ordered,
		"status": "complete" if not missing else ("partial" if ordered else "failed"),
	}
	out_dir.mkdir(parents=True, exist_ok=True)
	target.write_text(json.dumps(result, indent=1), encoding="utf-8")
	return {"case_id": case_id, "status": result["status"], "tagged": len(ordered), "of": len(paragraphs), "usd": usage_total.get("usd", 0)}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", default="gpt-4.1-nano", choices=sorted(PRICES))
	parser.add_argument("--run", required=True, help="Run name, e.g. nano_v2_all300")
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True, help="Shared spend ledger (JSON lines), same file for every run")
	parser.add_argument("--cases", help="Comma-separated case ids; default all 300")
	parser.add_argument("--limit", type=int, help="Use only the first N case ids (sorted)")
	parser.add_argument("--workers", type=int, default=4)
	parser.add_argument("--force", action="store_true")
	parser.add_argument("--send", action="store_true", help="Call the model; otherwise dry run")
	args = parser.parse_args()
	ids = sorted(int(m.group(1)) for f in REPORTS.glob("case_*_deterministic.json") if (m := re.match(r"case_(\d+)_", f.name)))
	if args.cases:
		ids = [int(x) for x in args.cases.split(",")]
	if args.limit:
		ids = ids[:args.limit]
	ledger = SpendLedger(args.ledger)
	if not args.send:
		total_in = total_par = 0
		for case_id in ids:
			paragraphs = load_paragraphs(json.loads((REPORTS / f"case_{case_id}_deterministic.json").read_text(encoding="utf-8")))
			total_par += len(paragraphs)
			total_in += sum(estimate_tokens(c) for c in windows(paragraphs))
		out_tokens = total_par * 80
		print(json.dumps({"status": "dry_run", "cases": len(ids), "paragraphs": total_par, "est_input_tokens": total_in,
			"est_output_tokens": out_tokens, "est_usd": round(cost_usd(args.model, total_in, out_tokens), 4),
			"spent_so_far_usd": round(ledger.total(), 4)}))
		return 0
	client = make_client()
	args.out_dir.mkdir(parents=True, exist_ok=True)
	results = []
	try:
		with ThreadPoolExecutor(max_workers=args.workers) as pool:
			for outcome in pool.map(lambda cid: tag_case(client, ledger, args.model, args.run, cid, args.out_dir, args.force), ids):
				results.append(outcome)
				print(json.dumps(outcome), flush=True)
	except CapReached as exc:
		print(json.dumps({"status": "stopped_at_cap", "detail": str(exc)}))
	summary = {"run": args.run, "model": args.model, "cases": len(results), "spent_total_usd": round(ledger.total(), 4),
		"statuses": {s: sum(1 for r in results if r["status"] == s) for s in {r["status"] for r in results}}}
	(args.out_dir / "run_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
	print(json.dumps(summary))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
