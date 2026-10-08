"""Full-decision themes and arguments, using the deterministic discussion units as a map. Report-only; open case law only.

The model gets the whole decision as numbered paragraphs plus the rule-based unit boundaries, and returns themes and
arguments. Every argument must carry paragraph numbers and a short VERBATIM quote; the script checks each quote against
the paragraph text and marks it verified or not. Dry run by default; --send calls the model.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
for entry in (PROJECT_ROOT, PROJECT_ROOT / "scripts" / "ai_poc"):
	if str(entry) not in sys.path:
		sys.path.insert(0, str(entry))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "themes_v1"
SYSTEM = (
	"You read one Canadian immigration or refugee court or tribunal decision and extract its themes and arguments for a legal researcher. "
	"The decision is given as paragraphs [n]. The units list is a rule-based map of where the decision changes subject; use it as a guide, "
	"not as truth. Use only the decision text; never invent facts, cases or paragraph numbers.\n"
	"themes: 3 to 8 themes the reasons actually turn on, each with a short name (2 to 8 words), a one-sentence summary, and the paragraph "
	"numbers where it is discussed.\n"
	"arguments: the distinct arguments made, in the order they appear. For each: who made it (applicant, respondent, tribunal_below, court), "
	"the claim in one sentence, how the court dealt with it (accepted, rejected, not_decided), the main authority it rests on as cited in the text "
	"(or empty), the paragraph numbers, and a quote of 25 words or fewer copied exactly, character for character, from one of those paragraphs.\n"
	"overall: one or two sentences giving the result and the main reason, in plain language."
)
SCHEMA = {
	"type": "object", "additionalProperties": False, "required": ["themes", "arguments", "overall"],
	"properties": {
		"overall": {"type": "string"},
		"themes": {"type": "array", "items": {"type": "object", "additionalProperties": False,
			"required": ["name", "summary", "paragraphs"],
			"properties": {"name": {"type": "string"}, "summary": {"type": "string"}, "paragraphs": {"type": "array", "items": {"type": "integer"}}}}},
		"arguments": {"type": "array", "items": {"type": "object", "additionalProperties": False,
			"required": ["made_by", "claim", "treatment", "authority", "paragraphs", "quote"],
			"properties": {
				"made_by": {"type": "string", "enum": ["applicant", "respondent", "tribunal_below", "court"]},
				"claim": {"type": "string"},
				"treatment": {"type": "string", "enum": ["accepted", "rejected", "not_decided"]},
				"authority": {"type": "string"},
				"paragraphs": {"type": "array", "items": {"type": "integer"}},
				"quote": {"type": "string"}}}},
	},
}


def norm(text: str) -> str:
	return re.sub(r"\s+", " ", text.replace("’", "'").replace("“", '"').replace("”", '"')).strip().lower()


def verify(result: dict, paragraphs: list[dict]) -> dict:
	texts = {p["paragraph_index"]: norm(p["text"]) for p in paragraphs}
	valid = set(texts)
	verified = checked = bad_numbers = 0
	for arg in result.get("arguments", []):
		quote = norm(arg.get("quote", ""))
		nums = [n for n in arg.get("paragraphs", []) if n in valid]
		bad_numbers += len(arg.get("paragraphs", [])) - len(nums)
		arg["quote_verified"] = bool(quote) and any(quote in texts[n] for n in nums)
		checked += 1
		verified += arg["quote_verified"]
	for theme in result.get("themes", []):
		bad_numbers += sum(n not in valid for n in theme.get("paragraphs", []))
	return {"arguments": checked, "quotes_verified": verified, "paragraph_numbers_not_in_decision": bad_numbers}


def build(report: dict, paragraphs: list[dict]) -> list[dict]:
	units = [{"unit": u["discussion_unit_id"].split(":")[-1], "from": u["start_paragraph"], "to": u["end_paragraph"]} for u in report.get("discussion_units", [])]
	body = "\n\n".join(f"[{p['paragraph_index']}] {p['text']}" for p in paragraphs)
	user = f"units (rule-based, container paragraph positions): {json.dumps(units)}\n\ndecision:\n{body}"
	return [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", required=True, choices=sorted(PRICES))
	parser.add_argument("--run", required=True)
	parser.add_argument("--cases", required=True, help="Comma-separated case ids")
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True)
	parser.add_argument("--send", action="store_true")
	args = parser.parse_args()
	ledger = SpendLedger(args.ledger)
	client = make_client() if args.send else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	for case_id in [int(x) for x in args.cases.split(",")]:
		report = json.loads((REPORTS / f"case_{case_id}_deterministic.json").read_text(encoding="utf-8"))
		paragraphs = load_paragraphs(report)
		messages = build(report, paragraphs)
		est_in = int(sum(len(m["content"]) for m in messages) / 3.2)
		out_cap = 12000 if args.model.startswith(("gpt-5", "o4")) else 5000
		if not args.send:
			print(json.dumps({"case_id": case_id, "model": args.model, "est_input_tokens": est_in, "est_usd_max": round(cost_usd(args.model, est_in, out_cap), 4)}))
			continue
		data, usage = call_json(client, ledger, run=args.run, model=args.model, messages=messages, schema_name="themes_arguments",
			schema=SCHEMA, max_output_tokens=out_cap, est_input_tokens=est_in, label=f"themes case {case_id}")
		check = verify(data, paragraphs)
		(args.out_dir / f"case_{case_id}_themes_{args.model}.json").write_text(json.dumps({
			"case_id": case_id, "model": args.model, "prompt_version": PROMPT_VERSION, "run": args.run, "usage": usage,
			"verification": check, "result": data}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": case_id, "model": args.model, "usd": round(usage["usd"], 4), **check}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
