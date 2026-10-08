"""Rebuttal-only pass over the party points a themes run already found (prompt version rebut_v1).

Input: a themes v5/v5c output (the party and finding-below rows with their sentence ids) and the deterministic paragraph report.
Code builds a window for each party point: its own paragraphs plus the next WINDOW_AFTER paragraphs. The model gets a few party points and the window's
numbered sentences, and for each point says whether the court answers it in the window, the answering sentence ids, and the verdict.
Quotes are copied from the sentence table by id (never written by the model). Public case law only; nothing is written to the database or the site.
Without --send it prints a cost ceiling per case.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from extract_themes_v5 import META, header, index_sentences, render  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

# Optional context arms (A/B test of our own data): H = nearest section heading above the window, I = the fixed list of refugee claim issues,
# K = court sentences that carry a disagreement cue are marked with "*" (code-found, not model-found).
CUE_RE = re.compile(r"\b(I do not agree|I disagree|do(es)? not agree|cannot agree|not persuaded|I reject|cannot accept|do not accept|with respect|without merit|no merit|misconstrue|misread|mischaracteri[sz]|is not correct|is not persuasive|I am not satisfied|failed to (show|establish|demonstrate)|has not (shown|established|demonstrated))\b", re.I)


def issue_list() -> str:
	from backend.case_types.claim_issues import ISSUE_CUES

	return ", ".join(k.replace("_", " ") for k in ISSUE_CUES)


def heading_above(report: dict, para: int) -> str:
	best = ""
	for p in sorted(report.get("paragraphs", []), key=lambda x: x["paragraph_index"]):
		if p["paragraph_index"] > para:
			break
		if p.get("is_heading") and str(p.get("text", "")).strip():
			best = str(p["text"]).strip()[:120]
	return best

PROMPT_VERSION = "rebut_v1"
WINDOW_AFTER = 2
MAX_POINTS = 6
MAX_GAP = 3

SYSTEM = """You read a few sentences of a Canadian immigration decision. Each numbered party point below was made by a party (or is a finding of the decision under review) and the decision is now answering it.
For EACH party point decide whether the court (or the reviewing panel) answers THAT point in the text shown. An answer is a sentence or run of sentences that responds to the point: accepts it, rejects it, qualifies it, or says it need not be decided.
Rules:
- Answer only from the text shown. Do not use outside knowledge.
- answer_ids are sentence ids from the text shown (like "17.2"), written by the court, never the sentences that state the party point itself. Use the fewest ids that carry the answer (usually 1 to 3).
- If the text shown only states the point or the facts and never responds to it, answered is false and answer_ids is empty.
- A general statement of law is not an answer unless it is applied to this point.
- verdict: rejects (the point fails), accepts (the point succeeds), partly, not_decided (the court says it need not or will not decide it), or none when answered is false.
- why: one short plain sentence naming how the court answers, in your own words (under 30 words)."""

SCHEMA = {
	"type": "object", "additionalProperties": False, "required": ["results"],
	"properties": {"results": {"type": "array", "items": {
		"type": "object", "additionalProperties": False, "required": ["point", "answered", "answer_ids", "verdict", "why"],
		"properties": {
			"point": {"type": "string"},
			"answered": {"type": "boolean"},
			"answer_ids": {"type": "array", "items": {"type": "string"}},
			"verdict": {"type": "string", "enum": ["rejects", "accepts", "partly", "not_decided", "none"]},
			"why": {"type": "string"},
		}}}},
}


def points_from(result: dict, table: dict) -> list[dict]:
	out = []
	for i, row in enumerate(result.get("arguments", [])):
		if row.get("kind") not in ("party_argument", "finding_below"):
			continue
		ids = [e for e in row.get("evidence_ids", []) if e in table]
		if not ids:
			continue
		paras = sorted({table[e]["para"] for e in ids})
		out.append({"pid": f"P{len(out) + 1}", "row": i, "by": row.get("made_by", ""), "text": row.get("claim", ""), "ids": ids, "lo": paras[0], "hi": paras[-1]})
	return sorted(out, key=lambda p: (p["lo"], p["hi"]))


def groups(points: list[dict]) -> list[list[dict]]:
	out: list[list[dict]] = []
	for p in points:
		if out and len(out[-1]) < MAX_POINTS and p["lo"] - max(q["hi"] for q in out[-1]) <= MAX_GAP:
			out[-1].append(p)
		else:
			out.append([p])
	return out


def run_case(client, ledger, run, model, case_id, report, themes, send, context="", stop_file=None):
	paragraphs = load_paragraphs(report)
	table = index_sentences(paragraphs)
	numbers = sorted({p["paragraph_index"] for p in paragraphs})
	points = points_from(themes["result"], table)
	head = header(case_id)
	calls = []
	for g in groups(points):
		lo, hi = min(p["lo"] for p in g), max(p["hi"] for p in g)
		paras = {n for n in numbers if lo <= n <= hi + WINDOW_AFTER}
		listing = "\n".join(f"{p['pid']} ({p['by']}; stated at {', '.join(p['ids'])}): {p['text']}" for p in g)
		body = render(table, paras)
		if "K" in context:
			body = "\n".join(("* " if CUE_RE.search(ln) and not any(ln.startswith(i + " ") for p in g for i in p["ids"]) else "") + ln for ln in body.split("\n"))
		extra = ""
		if "H" in context and heading_above(report, lo):
			extra += f"Section heading above this text: {heading_above(report, lo)}\n"
		if "I" in context:
			extra += f"Typical issues in refugee decisions (for orientation only): {issue_list()}\n"
		if "K" in context:
			extra += "Sentences marked * contain a disagreement or rejection cue found by a word list; they may or may not answer a point.\n"
		user = (head + "\n\n" if head else "") + extra + f"Party points:\n{listing}\n\ntext:\n{body}"
		calls.append((g, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]))
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	if not send:
		tin = sum(est(m) for _, m in calls)
		tout = sum(300 + 110 * len(g) for g, _ in calls)
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "context": context, "points": len(points), "calls": len(calls), "est_input_tokens": tin, "est_usd_max": round(cost_usd(model, tin, tout), 4)}))
		return None
	usd, out_rows, bad_ids = 0.0, [], 0
	dropped_own = dropped_missing = dropped_on_unanswered = 0
	for g, msgs in calls:
		if stop_file is not None and stop_file.exists():
			print(json.dumps({"stopped": "stop file found", "case_id": case_id}), flush=True)
			raise SystemExit(3)
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="rebuttal_pass", schema=SCHEMA, max_output_tokens=300 + 150 * len(g), est_input_tokens=est(msgs), label=f"rebut case {case_id} {g[0]['pid']}")
		usd += u["usd"]
		by_pid = {p["pid"]: p for p in g}
		for r in data["results"]:
			p = by_pid.get(r["point"].split()[0] if r["point"] else "")
			if p is None:
				continue
			ids = [x for x in r["answer_ids"] if x in table and x not in p["ids"]]
			bad_ids += len(r["answer_ids"]) - len(ids)
			dropped_own += sum(1 for x in r["answer_ids"] if x in p["ids"])
			dropped_missing += sum(1 for x in r["answer_ids"] if x not in table)
			dropped_on_unanswered += (len(r["answer_ids"]) - len(ids)) if not r["answered"] else 0
			if r["answered"] and not ids:
				r = {**r, "answered": False, "verdict": "none"}
			out_rows.append({"pid": p["pid"], "party_by": p["by"], "party_text": p["text"], "party_ids": p["ids"], "answered": r["answered"], "verdict": r["verdict"],
				"answer_ids": ids, "answer_paragraphs": sorted({table[x]["para"] for x in ids}), "answer_quote": " ".join(table[x]["text"] for x in ids), "why": r["why"]})
	check = {"points": len(points), "calls": len(calls), "answered": sum(r["answered"] for r in out_rows), "points_returned": len(out_rows), "answer_ids_dropped": bad_ids, "dropped_own_sentence": dropped_own, "dropped_not_in_text": dropped_missing, "dropped_on_unanswered_rows": dropped_on_unanswered}
	return {"usd": usd, "result": out_rows, "verification": check}


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--run", required=True)
	ap.add_argument("--cases", required=True)
	ap.add_argument("--themes-dir", type=Path, required=True)
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--reports-dir", type=Path, action="append")
	ap.add_argument("--meta-csv", type=Path, action="append")
	ap.add_argument("--cap-usd", type=float, default=None)
	ap.add_argument("--context", default="", help="letters from H, I, K (see top of file); empty = control")
	ap.add_argument("--stop-file", type=Path, default=None, help="if this file exists the run stops before the next call")
	args = ap.parse_args()
	for m in args.meta_csv or []:
		for row in csv.DictReader(m.open(encoding="utf-8-sig")):
			META[int(float(row["case_id"]))] = row
	dirs = args.reports_dir or [REPORTS]
	ledger = SpendLedger(args.ledger, args.cap_usd) if args.cap_usd else SpendLedger(args.ledger)
	client = make_client() if args.send else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	for cid in [int(x) for x in args.cases.split(",")]:
		path = next((d / f"case_{cid}_deterministic.json" for d in dirs if (d / f"case_{cid}_deterministic.json").exists()), None)
		hits = sorted(glob.glob(str(args.themes_dir / f"case_{cid}_themes_*.json")))
		if path is None or not hits:
			raise SystemExit(f"missing report or themes file for case {cid}")
		out = run_case(client, ledger, args.run, args.model, cid, json.loads(path.read_text(encoding="utf-8")), json.loads(Path(hits[-1]).read_text(encoding="utf-8")), args.send, args.context, args.stop_file)
		if out is None:
			continue
		(args.out_dir / f"case_{cid}_rebut_{PROMPT_VERSION}_{args.model}.json").write_text(json.dumps({"case_id": cid, "model": args.model, "prompt_version": PROMPT_VERSION, "context": args.context, "run": args.run, "usage": {"usd": out["usd"]}, "verification": out["verification"], "result": out["result"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": cid, "model": args.model, "prompt": PROMPT_VERSION, "context": args.context, "usd": round(out["usd"], 4), **out["verification"]}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
