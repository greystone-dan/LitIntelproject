"""Capped model run on the wide set (run on the PC; needs OPENAI_API_KEY in the process environment, never printed or written). Public case law only; no database.

Arms (all gpt-4.1-mini unless --model says otherwise):
  v4  the existing propositions prompt (prop_v4), unchanged: holder, kind, text, answers. Layers are NOT asked for.
  L   prop_v4 plus an explicit layer 1-6 and a verbatim quote per point (same old case header as v4).
  LF  arm L, but the old header is replaced by a frame built by code: forum, parties as styled, decision under review, how the layers nest.
Dry run (default) prints a cost ceiling per case. --send runs. --stop-file stops before the next call. --cap-usd is a hard ceiling checked against the ledger.
Only the paragraph step runs (no issue-block step).
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402

CHUNK = 20
MAX_PARA = 3000
HOLDERS = ["court", "applicant", "respondent", "earlier_decision_maker", "witness_or_document", "prior_court_or_authority", "other"]
KINDS = ["issue", "allegation_or_argument", "finding", "rule_of_law", "fact", "conclusion_or_order", "procedure"]
ROLES = ["facts", "procedural_history", "issue", "law", "analysis", "conclusion", "disposition", "other"]

SYSTEM_V4 = """You read numbered paragraphs of a Canadian court or tribunal decision. The decision-maker is always the one writing, so do not label who is "speaking". Instead, for EVERY paragraph shown, in order, return:
- para: the paragraph number exactly as shown.
- propositions: one entry for each distinct point the paragraph makes (usually 1 to 4; list every separate item when the paragraph itself lists grounds, objections or findings, one entry per item). Each entry:
  holder = whose position the point is: court (the decision-maker's own reasoning, findings, statement of law or narration), applicant (what the applicant, appellant or claimant alleges, argues or says), respondent (what the respondent, Minister or Crown says), earlier_decision_maker (what the officer, board, tribunal or lower court found or reasoned, as reported here), witness_or_document (testimony, an affidavit, a letter or a document being described), prior_court_or_authority (a case, statute or textbook being relied on), other.
  kind = issue (a question to be decided), allegation_or_argument (what a party claims or argues), finding (a conclusion on the facts or the application of law, including a reported finding), rule_of_law (a legal test, standard or principle), fact (background or procedural fact), conclusion_or_order (the outcome or order), procedure.
  text = the point in at most 22 words, naming who makes it when it is not the court.
  answers = when this point answers or rejects an earlier point in the SAME paragraph, the 1-based position of that point in this paragraph's list; otherwise 0.
- summary: ONE plain sentence, at most 25 words, saying what the paragraph says and who makes each point. Use only the paragraph text.
- role: facts, procedural_history, issue, law, analysis, conclusion, disposition or other: the job the paragraph does in the decision.
A line "[Section heading: ...]" before a paragraph is context only: do not summarize it. Ignore footnote numbers. Do not merge paragraphs and do not skip any."""

LAYER_TEXT = """  layer = which layer of the nested proceeding the point belongs to (a judicial review or appeal is nested: the writer weighs the parties' submissions to decide whether an EARLIER decision was right, and that earlier decision itself reports what a claimant, witness or the Minister said):
    1 = the writer's own evaluation, finding, narration or order in THIS decision (a dissent or concurrence is still layer 1);
    2 = a party's submission to THIS decision-maker (the judicial review applicant or respondent, the appellant, the Minister, an intervener);
    3 = the EARLIER decision-maker's own finding or reasoning, as reported (officer, RPD, RAD, board, lower court);
    4 = a first-instance party's, claimant's, witness's or Minister's position as reported INSIDE the earlier decision (what they told or argued to the earlier decision-maker);
    5 = a document, affidavit or testimony being described as evidence;
    6 = commentary on precedent or the legal framework: what a case or statute stands for, how a test works, the standard of review; it explains the law and does not decide these facts. A first-person finding on these facts, a party's argument about the test, and the earlier decision-maker's reasoning stay in layers 1, 2 and 3.
  Use the layer that fits the point itself, not the paragraph; one paragraph may hold points at several layers.
  quote = an exact, unaltered copy (at most 30 words) of the words in the paragraph that make this point, copied character for character with no ellipsis; if the point rests on several sentences, quote the most telling one."""

SYSTEM_L = SYSTEM_V4.replace("  answers = when this point", LAYER_TEXT + "\n  answers = when this point", 1)

PROP_V4 = {"type": "object", "additionalProperties": False, "required": ["holder", "kind", "text", "answers"], "properties": {
	"holder": {"type": "string", "enum": HOLDERS}, "kind": {"type": "string", "enum": KINDS}, "text": {"type": "string"}, "answers": {"type": "integer"}}}
PROP_L = {"type": "object", "additionalProperties": False, "required": ["holder", "layer", "kind", "text", "quote", "answers"], "properties": {
	"holder": {"type": "string", "enum": HOLDERS}, "layer": {"type": "integer", "enum": [1, 2, 3, 4, 5, 6]}, "kind": {"type": "string", "enum": KINDS},
	"text": {"type": "string"}, "quote": {"type": "string"}, "answers": {"type": "integer"}}}


def schema(prop):
	return {"type": "object", "additionalProperties": False, "required": ["paragraphs"], "properties": {"paragraphs": {"type": "array", "items": {
		"type": "object", "additionalProperties": False, "required": ["para", "propositions", "summary", "role"],
		"properties": {"para": {"type": "integer"}, "propositions": {"type": "array", "items": prop}, "summary": {"type": "string"}, "role": {"type": "string", "enum": ROLES}}}}}}


def old_header(doc):
	court = doc["court"]
	text = (f"case: {doc['title']}, {doc['citation']} ({court}). "
		"The style of cause lists the parties but not who is who; work out the applicant and the respondent from the first paragraphs, not from the order of the names and not from who wins. "
		"For an appeal, the appellant counts as 'applicant' and the other side as 'respondent'. The court or tribunal whose decision is under review counts as earlier_decision_maker. ")
	if court in ("RPD", "RAD"):
		text += "This is a decision of the tribunal itself: the tribunal's own reasoning is the 'court' rows, the claimant is the applicant and the Minister is the respondent."
	return text


ARMS = {
	"v4": (SYSTEM_V4, PROP_V4, lambda d: old_header(d)),
	"L": (SYSTEM_L, PROP_L, lambda d: old_header(d)),
	"LF": (SYSTEM_L, PROP_L, lambda d: f"case: {d['title']}, {d['citation']} ({d['court']}).\nFrame (built by code from the decision's own heading and opening; 'applicant' means the party that brought this proceeding or appeal, 'respondent' the other side, and the court or tribunal whose decision is under review is 'earlier_decision_maker'):\n{d['frame']}"),
}


def render(chunk, pre):
	lines = []
	for p in chunk:
		if p.get("heading_before"):
			lines.append(f"[Section heading: {p['heading_before']}]")
		lines.append(f"[{p['paragraph_index']}] {p['text'][:MAX_PARA]}")
	return pre + "\n\n".join(lines)


def run_case(client, ledger, run, arm, model, doc, send, stop_file):
	system, prop, hdr = ARMS[arm]
	pre = hdr(doc) + "\n\n"
	paras = doc["paragraphs"]
	chunks = [paras[i:i + CHUNK] for i in range(0, len(paras), CHUNK)]
	mk = lambda ch: [{"role": "system", "content": system}, {"role": "user", "content": render(ch, pre)}]  # noqa: E731
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	per = 330 if arm != "v4" else 230
	if not send:
		tin = sum(est(mk(c)) for c in chunks)
		tout = per * len(paras)
		return {"case_id": doc["case_id"], "arm": arm, "model": model, "paragraphs": len(paras), "calls": len(chunks), "est_usd_max": round(cost_usd(model, tin, tout), 4), "est_usd_typical": round(cost_usd(model, tin, int(tout * 0.7)), 4)}
	rows, dropped, usd = {}, 0, 0.0

	def ask(ch):
		nonlocal dropped, usd
		if stop_file is not None and stop_file.exists():
			raise SystemExit(3)
		msgs = mk(ch)
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="propositions", schema=schema(prop),
			max_output_tokens=min(16000, 500 + per * 2 * len(ch)), est_input_tokens=est(msgs), label=f"{arm} case {doc['case_id']}")
		usd += u["usd"]
		want = {p["paragraph_index"] for p in ch}
		for r in data["paragraphs"]:
			if r["para"] in want and r["para"] not in rows:
				rows[r["para"]] = r
			else:
				dropped += 1

	for ch in chunks:
		ask(ch)
	missing = sorted({p["paragraph_index"] for p in paras} - set(rows))
	if missing:
		ask([p for p in paras if p["paragraph_index"] in set(missing)])
	missing = sorted({p["paragraph_index"] for p in paras} - set(rows))
	return {"case_id": doc["case_id"], "arm": arm, "model": model, "usd": usd, "dropped_rows": dropped, "paragraphs_missing": missing, "paragraphs": [rows[k] for k in sorted(rows)]}


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	ap.add_argument("--arm", required=True, choices=sorted(ARMS))
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--inputs", type=Path, required=True)
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--cases", default="", help="comma list of case ids; default all in --inputs")
	ap.add_argument("--cases-file", type=Path, default=None, help="text file, one case id per line")
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--cap-usd", type=float, required=True)
	ap.add_argument("--stop-file", type=Path, default=None)
	ap.add_argument("--workers", type=int, default=4)
	args = ap.parse_args()
	ids = [int(x) for x in args.cases.split(",") if x] or ([int(x) for x in args.cases_file.read_text().split()] if args.cases_file else sorted(int(p.stem.split("_")[1]) for p in args.inputs.glob("case_*.json")))
	ledger = SpendLedger(args.ledger, args.cap_usd)
	client = make_client() if args.send else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	run = f"wide_{args.arm}"

	def one(cid):
		out_path = args.out_dir / f"case_{cid}_{args.arm}_{args.model}.json"
		if args.send and out_path.exists():
			return {"case_id": cid, "skipped": "already done"}
		doc = json.loads((args.inputs / f"case_{cid}.json").read_text(encoding="utf-8"))
		out = run_case(client, ledger, run, args.arm, args.model, doc, args.send, args.stop_file)
		if args.send:
			out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
			return {k: v for k, v in out.items() if k != "paragraphs"} | {"paragraphs_missing": len(out["paragraphs_missing"])}
		return out

	with ThreadPoolExecutor(args.workers if args.send else 1) as ex:
		results = []
		for r in ex.map(one, ids):
			print(json.dumps(r), flush=True)
			results.append(r)
	if not args.send:
		print(json.dumps({"dry_run": True, "arm": args.arm, "model": args.model, "cases": len(ids), "ceiling_usd": round(sum(r["est_usd_max"] for r in results), 3), "typical_usd": round(sum(r["est_usd_typical"] for r in results), 3), "ledger_now": round(ledger.total(), 4)}))
	else:
		print(json.dumps({"done": True, "arm": args.arm, "ledger_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
