"""Draft analysis test (PC run, OpenAI key in the process only, public law and fictional drafts, no database).
Reads a one-sided draft (numbered paragraphs) and returns its arguments: issue, claim, supporting paragraphs, a word-for-word quote, the layer of each piece of support (derived later in code from `support.kind`), and weak spots.
  --arm F   adds a code-built frame (forum, which side wrote it, how layers nest); --arm N sends the draft with no frame.
Dry run prints a cost ceiling. --send runs. --cap-usd is a hard ceiling in the ledger. The answers file HIDDEN_answers.json is never read here."""
from __future__ import annotations
import argparse, json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402

FORUMS = {"FC": "Federal Court", "FCA": "Federal Court of Appeal", "SCC": "Supreme Court of Canada", "RPD": "Refugee Protection Division", "RAD": "Refugee Appeal Division"}
KINDS = ["statute_or_regulation", "case_law", "record_evidence", "decision_under_review", "policy_or_guideline", "other"]
SYSTEM = """You read a one-sided draft written for one party in a Canadian immigration or refugee proceeding. The text is numbered paragraphs. Find the arguments the draft actually makes. Group them under the issue each one answers. For each argument return: issue (the legal question in plain words, same wording for arguments on the same issue); claim (what the draft says, at most 30 words); paras (the paragraph numbers); quote (one sentence copied word for word from those paragraphs, at most 40 words); support (a list of what the draft relies on: kind, one of %s, and ref, at most 15 words); weak_spot (one sentence on what the other side would most likely answer, or 'none'). Only use what is in the draft. Do not add arguments the draft does not make.""" % ", ".join(KINDS)
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["arguments"], "properties": {"arguments": {"type": "array", "items": {"type": "object", "additionalProperties": False,
	"required": ["issue", "claim", "paras", "quote", "support", "weak_spot"], "properties": {"issue": {"type": "string"}, "claim": {"type": "string"}, "paras": {"type": "array", "items": {"type": "integer"}}, "quote": {"type": "string"},
	"support": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["kind", "ref"], "properties": {"kind": {"type": "string", "enum": KINDS}, "ref": {"type": "string"}}}}, "weak_spot": {"type": "string"}}}}}}

def frame(d):
	side = d["side"]
	return (f"Forum: {FORUMS.get(d['forum'], d['forum'])}. The draft was written for the {side}. "
		"Everything the draft says is that party's own submission to the decision-maker (layer 2). "
		"Where it describes the decision under review it is reporting an earlier decision-maker (layer 3); where it cites a case or statute it is relying on law (layer 6); where it points to testimony or documents it is relying on the record (layer 5).")

def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--drafts", type=Path, required=True)
	ap.add_argument("--arm", required=True, choices=["F", "N"])
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--cap-usd", type=float, required=True)
	ap.add_argument("--stop-file", type=Path, default=None)
	ap.add_argument("--workers", type=int, default=4)
	a = ap.parse_args()
	files = sorted(a.drafts.glob("*.json"))
	files = [f for f in files if not f.name.startswith("HIDDEN")]
	ledger = SpendLedger(a.ledger, a.cap_usd)
	client = make_client() if a.send else None
	a.out_dir.mkdir(parents=True, exist_ok=True)

	def one(f):
		d = json.loads(f.read_text(encoding="utf-8"))
		path = a.out_dir / f"{d['draft_id']}_{a.arm}_{a.model}.json"
		if a.send and path.exists():
			return {"draft": d["draft_id"], "skipped": True}
		body = "\n".join(f"[{p['n']}] {p['text']}" for p in d["paragraphs"])
		user = (frame(d) + "\n\n" if a.arm == "F" else "") + "Draft:\n" + body
		msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
		tin = int(sum(len(m["content"]) for m in msgs) / 3.2)
		tout = 2500
		if not a.send:
			return {"draft": d["draft_id"], "est_usd_max": round(cost_usd(a.model, tin, tout), 4)}
		if a.stop_file is not None and a.stop_file.exists():
			raise SystemExit(3)
		data, u = call_json(client, ledger, run=f"draft_{a.arm}", model=a.model, messages=msgs, schema_name="draft_args", schema=SCHEMA, max_output_tokens=6000, est_input_tokens=tin, label=f"draft {d['draft_id']}")
		path.write_text(json.dumps({"draft_id": d["draft_id"], "arm": a.arm, "model": a.model, "usd": u["usd"], "result": data}, ensure_ascii=False, indent=1), encoding="utf-8")
		return {"draft": d["draft_id"], "usd": round(u["usd"], 4)}

	with ThreadPoolExecutor(a.workers if a.send else 1) as ex:
		res = []
		for r in ex.map(one, files):
			print(json.dumps(r), flush=True)
			res.append(r)
	if a.send:
		print(json.dumps({"done": True, "arm": a.arm, "model": a.model, "ledger_total_usd": round(ledger.total(), 4)}))
	else:
		print(json.dumps({"dry_run": True, "arm": a.arm, "model": a.model, "drafts": len(files), "ceiling_usd": round(sum(r["est_usd_max"] for r in res), 3)}))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
