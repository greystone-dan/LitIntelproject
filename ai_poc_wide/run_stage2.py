"""Stage 2 on the wide set (PC run, OpenAI key in the process only, public law, no database). Works from the arm-LF points already produced; no paragraph text is resent except the order paragraphs.
  --task issues   issue map: issues the decision deals with, each with paragraph range, each side's position, the court's result on that issue (enum) and the paragraph that says it.
  --task answers  for every party point (holder applicant/respondent, plus earlier-decision-maker points that a party attacks), the point(s) that answer it and whether the court accepted or rejected it.
Dry run prints a cost ceiling. --send runs. --cap-usd is a hard ceiling in the ledger. --stop-file stops before the next call."""
from __future__ import annotations
import argparse, json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402

RESULTS = ["allowed_for_applicant", "dismissed_for_applicant", "partly_allowed", "not_decided", "moot_or_procedural"]
SYSTEM_I = """You are given, for a Canadian court or tribunal decision, a frame (forum, parties, decision under review) and the points found in each numbered paragraph as lines "para | holder | kind | point". The decision-maker is the author; "applicant" means the party that brought this proceeding or appeal. Return the issues the decision actually decides, in order. For each issue: issue (the question in plain words), paras (the paragraph range where it is dealt with, e.g. "12-20"), applicant_position and respondent_position (at most 25 words each, 'not stated' if the points do not show it), result (one of: allowed_for_applicant = the court agrees with the applicant on this issue; dismissed_for_applicant = the court rejects the applicant on this issue; partly_allowed; not_decided = the court says it need not decide it; moot_or_procedural), result_para (the single paragraph number where the court states its result on this issue, 0 if none), result_text (at most 25 words). Also return overall: order_para (the paragraph number that states the final order, 0 if none) and overall_result (one of the same values, for the whole application or appeal). Use only the points given; do not invent."""
SCHEMA_I = {"type": "object", "additionalProperties": False, "required": ["issues", "order_para", "overall_result"], "properties": {
	"order_para": {"type": "integer"}, "overall_result": {"type": "string", "enum": RESULTS},
	"issues": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["issue", "paras", "applicant_position", "respondent_position", "result", "result_para", "result_text"], "properties": {
		"issue": {"type": "string"}, "paras": {"type": "string"}, "applicant_position": {"type": "string"}, "respondent_position": {"type": "string"},
		"result": {"type": "string", "enum": RESULTS}, "result_para": {"type": "integer"}, "result_text": {"type": "string"}}}}}}
SYSTEM_A = """You are given, for a Canadian court or tribunal decision, a frame and numbered points as lines "id | para | holder | kind | point". The decision-maker is the author. For EVERY point whose holder is applicant or respondent (a party's argument or position, to this decision-maker or reported inside the earlier decision), return: id (exactly as given); answered_by (the ids of the points where the decision-maker answers, accepts or rejects it, empty if none; use only ids from the list); outcome (accepted = the decision-maker agrees with this point; rejected = it disagrees; partly; not_addressed = no answer in the points given). Do not invent ids; do not answer for points you cannot see an answer to: use not_addressed."""
SCHEMA_A = {"type": "object", "additionalProperties": False, "required": ["answers"], "properties": {"answers": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["id", "answered_by", "outcome"], "properties": {
	"id": {"type": "integer"}, "answered_by": {"type": "array", "items": {"type": "integer"}}, "outcome": {"type": "string", "enum": ["accepted", "rejected", "partly", "not_addressed"]}}}}}}

def listing(lf, task):
	lines, ids = [], {}
	k = 0
	for r in lf["paragraphs"]:
		for p in r["propositions"]:
			k += 1
			ids[k] = (r["para"], p)
			lines.append(f"{k} | {r['para']} | {p['holder']} | {p['kind']} | {p['text']}" if task == "answers" else f"{r['para']} | {p['holder']} | {p['kind']} | {p['text']}")
	return "\n".join(lines), ids

def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--task", required=True, choices=["issues", "answers"])
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--inputs", type=Path, required=True)
	ap.add_argument("--lf-dir", type=Path, required=True, help="folder with the arm-LF outputs (out/LF)")
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--cases-file", type=Path, default=None)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--cap-usd", type=float, required=True)
	ap.add_argument("--stop-file", type=Path, default=None)
	ap.add_argument("--workers", type=int, default=4)
	a = ap.parse_args()
	ids = [int(x) for x in a.cases_file.read_text().split()] if a.cases_file else sorted(int(p.stem.split("_")[1]) for p in a.inputs.glob("case_*.json"))
	ledger = SpendLedger(a.ledger, a.cap_usd)
	client = make_client() if a.send else None
	a.out_dir.mkdir(parents=True, exist_ok=True)
	system, schema = (SYSTEM_I, SCHEMA_I) if a.task == "issues" else (SYSTEM_A, SCHEMA_A)

	def one(cid):
		path = a.out_dir / f"case_{cid}_{a.task}_{a.model}.json"
		if a.send and path.exists():
			return {"case_id": cid, "skipped": True}
		doc = json.loads((a.inputs / f"case_{cid}.json").read_text(encoding="utf-8"))
		lf_files = list(a.lf_dir.glob(f"case_{cid}_*.json"))
		if not lf_files:
			return {"case_id": cid, "skipped": True, "reason": "no LF output for this case"}
		lf = json.loads(lf_files[0].read_text(encoding="utf-8"))
		text, idmap = listing(lf, a.task)
		user = f"case: {doc['title']}, {doc['citation']} ({doc['court']}).\nFrame:\n{doc['frame']}\n\nPoints:\n{text}"
		msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
		tin = int(sum(len(m["content"]) for m in msgs) / 3.2)
		nparty = sum(1 for _, p in idmap.values() if p["holder"] in ("applicant", "respondent"))
		tout = 2500 if a.task == "issues" else 40 * max(nparty, 1) + 200
		if not a.send:
			return {"case_id": cid, "task": a.task, "model": a.model, "est_usd_max": round(cost_usd(a.model, tin, tout), 4)}
		if a.stop_file is not None and a.stop_file.exists():
			raise SystemExit(3)
		data, u = call_json(client, ledger, run=f"stage2_{a.task}", model=a.model, messages=msgs, schema_name=a.task, schema=schema, max_output_tokens=min(16000, tout * 2), est_input_tokens=tin, label=f"{a.task} case {cid}")
		out = {"case_id": cid, "task": a.task, "model": a.model, "usd": u["usd"], "points": {str(k): v[0] for k, v in idmap.items()}, "result": data}
		path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
		return {"case_id": cid, "usd": round(u["usd"], 4)}

	with ThreadPoolExecutor(a.workers if a.send else 1) as ex:
		res = []
		for r in ex.map(one, ids):
			print(json.dumps(r), flush=True)
			res.append(r)
	if a.send:
		print(json.dumps({"done": True, "task": a.task, "ledger_total_usd": round(ledger.total(), 4)}))
	else:
		print(json.dumps({"dry_run": True, "task": a.task, "model": a.model, "cases": len(ids), "ceiling_usd": round(sum(r.get("est_usd_max", 0) for r in res), 3), "skipped_no_lf": sum(1 for r in res if r.get("reason"))}))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
