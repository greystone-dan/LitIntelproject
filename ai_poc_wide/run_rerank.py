"""Rerank test (PC run, OpenAI key in the process only, public law, no database). For each draft argument, judge its 5 closest decided issues from OTHER cases (candidates built in code by match_library.py).
Returns per candidate: same_question | related | different, and the index of the best match (or -1). Dry run prints a ceiling. --send runs under a hard ledger cap."""
from __future__ import annotations
import argparse, json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
SYSTEM = """You compare one argument from a draft with a numbered list of issues already decided in other Canadian cases. For each candidate (by its number) say: same_question (the decided issue asks the same legal question, so its result is a useful precedent for the argument), related (same topic, different question) or different. Also give best (the index of the single most useful candidate, or -1 if none is at least related). Judge from the wording only."""
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["labels", "best"], "properties": {"labels": {"type": "array", "items": {"type": "string", "enum": ["same_question", "related", "different"]}}, "best": {"type": "integer"}}}

def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--candidates", type=Path, required=True)
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--out", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--cap-usd", type=float, required=True)
	ap.add_argument("--stop-file", type=Path, default=None)
	a = ap.parse_args()
	items = json.loads(a.candidates.read_text(encoding="utf-8"))
	ledger = SpendLedger(a.ledger, a.cap_usd)
	client = make_client() if a.send else None
	done = json.loads(a.out.read_text(encoding="utf-8")) if a.send and a.out.exists() else {}

	def one(it):
		if it["key"] in done:
			return None
		cands = "\n".join(f"{i}. {c['issue']} | applicant said: {c['applicant_position']} | result: {c['result']}" for i, c in enumerate(it["candidates"]))
		msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": f"Argument issue: {it['issue']}\nArgument: {it['claim']}\n\nCandidates:\n{cands}"}]
		tin = int(sum(len(m["content"]) for m in msgs) / 3.2)
		if not a.send:
			return it["key"], cost_usd(a.model, tin, 200), None
		if a.stop_file is not None and a.stop_file.exists():
			raise SystemExit(3)
		data, u = call_json(client, ledger, run="rerank", model=a.model, messages=msgs, schema_name="rerank", schema=SCHEMA, max_output_tokens=600, est_input_tokens=tin, label=it["key"])
		return it["key"], u["usd"], data

	res = []
	with ThreadPoolExecutor(4 if a.send else 1) as ex:
		for r in ex.map(one, items):
			if r:
				res.append(r)
				if a.send:
					done[r[0]] = r[2]
					a.out.write_text(json.dumps(done, ensure_ascii=False, indent=1), encoding="utf-8")
	print(json.dumps({"done" if a.send else "dry_run": True, "model": a.model, "items": len(res), "usd" if a.send else "ceiling_usd": round(sum(r[1] for r in res), 4), "ledger_total_usd": round(ledger.total(), 4) if a.send else None}))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
