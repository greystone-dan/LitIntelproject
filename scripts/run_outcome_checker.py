"""Second-opinion outcome reader for cases the rules leave "unclear" (advisory data, never overwrites).

Dry run by default: counts the cases, estimates tokens and cost, calls nothing. A real run needs --confirm-spend
and OPENAI_API_KEY, stops at --max-usd (never above 1.00), and writes JSONL files to --out. Only open case law is
sent. Use --source gold to measure the checker against the hand-read gold set (class-by-class agreement).
"""

from __future__ import annotations

import argparse
import collections
import gzip
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.metadata_outcomes import build_case_outcome
from backend import outcome_checker as oc

GOLD = PROJECT_ROOT / "tests" / "fixtures" / "outcome_gold.json.gz"
HARD_CEILING_USD = 1.00
_TRUTH = {"A": "allowed", "D": "dismissed", "M": "mixed", "P": "procedural"}


def iter_gold(only_unclear: bool):
	with gzip.open(GOLD, "rt", encoding="utf-8") as handle:
		for case in json.load(handle):
			rule = build_case_outcome(case["text"], {})["decision_outcome"]
			if only_unclear and rule != "unclear":
				continue
			yield {"id": case["id"], "citation": case["citation"], "text": case["text"], "rule": rule, "truth": _TRUTH[case["truth"]]}


def iter_db(limit: int | None):
	from sqlalchemy import select

	from backend.database import Case, SessionLocal

	with SessionLocal() as db:
		query = select(Case).order_by(Case.id)
		for case in db.scalars(query.limit(limit) if limit else query).yield_per(200):
			text = case.full_text or case.summary or ""
			rule = build_case_outcome(text, dict((case.metadata_json or {}).get("reader_extracted") or {}))["decision_outcome"]
			if rule == "unclear":
				yield {"id": case.id, "citation": case.neutral_citation if hasattr(case, "neutral_citation") else "", "text": text, "rule": rule, "truth": None}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source", choices=("db", "gold"), default="db")
	parser.add_argument("--gold-all", action="store_true", help="with --source gold, check every gold case, not just rule-unclear ones")
	parser.add_argument("--limit", type=int)
	parser.add_argument("--out", type=Path, help="directory for results.jsonl and review_queue.jsonl")
	parser.add_argument("--max-usd", type=float, default=0.40)
	parser.add_argument("--confirm-spend", action="store_true")
	args = parser.parse_args()
	if not 0 < args.max_usd <= HARD_CEILING_USD:
		parser.error(f"--max-usd must be above 0 and at most {HARD_CEILING_USD}")

	cases = list(iter_gold(not args.gold_all) if args.source == "gold" else iter_db(args.limit))
	prepared = [(case, oc.select_excerpt(case["text"])) for case in cases]
	tokens = sum(oc.estimate_tokens(excerpt) for _, excerpt in prepared)
	estimate = oc.usage_cost(tokens, 60 * len(prepared))
	print(f"cases={len(prepared)} est_input_tokens={tokens} est_cost_usd={estimate:.3f} model={oc.MODEL} cap_usd={args.max_usd}")
	if not args.confirm_spend:
		print("dry run: nothing sent. Add --confirm-spend --out DIR to run.")
		return
	if not args.out:
		parser.error("--out is required for a real run")
	if estimate > args.max_usd:
		print(f"estimate is above the cap; the run will stop at ${args.max_usd:.2f}.")
	from dotenv import load_dotenv
	from openai import OpenAI

	load_dotenv(PROJECT_ROOT / ".env")
	if not os.getenv("OPENAI_API_KEY"):
		raise SystemExit("OPENAI_API_KEY is not set")
	client = OpenAI()
	args.out.mkdir(parents=True, exist_ok=True)
	spent, prompt_total, completion_total, done = 0.0, 0, 0, 0
	tally: collections.Counter = collections.Counter()
	with (args.out / "results.jsonl").open("a", encoding="utf-8") as results, (args.out / "review_queue.jsonl").open("a", encoding="utf-8") as queue:
		for case, excerpt in prepared:
			if spent + oc.usage_cost(oc.estimate_tokens(excerpt), 60) > args.max_usd:
				print("stopped: next call would pass the spending cap")
				break
			response = client.chat.completions.create(
				model=oc.MODEL, messages=oc.build_messages(excerpt), temperature=0, max_tokens=200,
				response_format={"type": "json_object"},
			)
			usage = response.usage
			prompt_total += usage.prompt_tokens
			completion_total += usage.completion_tokens
			spent = oc.usage_cost(prompt_total, completion_total)
			answer = oc.parse_answer(response.choices[0].message.content or "", excerpt)
			relation = oc.compare(case["rule"], answer["outcome"])
			row = {"case": case["id"], "citation": case["citation"], "rule": case["rule"], "checker": answer["outcome"],
				"quote": answer["quote"], "valid": answer["valid"], "reason": answer["reason"], "relation": relation,
				"truth": case["truth"], "checker_version": oc.CHECKER_VERSION, "model": oc.MODEL}
			results.write(json.dumps(row, ensure_ascii=False) + "\n")
			if relation in {"disagree", "checker_only"} or (case["truth"] and oc.short_label(answer["outcome"]) != oc.short_label(case["truth"])):
				queue.write(json.dumps(row, ensure_ascii=False) + "\n")
			tally[(case["truth"], answer["outcome"])] += 1
			done += 1
	print(f"done={done} prompt_tokens={prompt_total} completion_tokens={completion_total} actual_cost_usd={spent:.4f}")
	if args.source == "gold":
		for (truth, got), count in sorted(tally.items(), key=str):
			print(f"hand_label={truth} checker={got} n={count}")


if __name__ == "__main__":
	main()
