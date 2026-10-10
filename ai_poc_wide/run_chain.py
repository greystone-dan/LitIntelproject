"""Full chain on drafts (PC run, OpenAI key in the process only, public law and fictional drafts, no database).
 1. extract the draft's arguments (run_draft SYSTEM/SCHEMA, frame arm F)  2. word-match 20 candidate decided issues from the library (match_library; the draft's own source case is left out)
 3. model picks the best candidate (run_rerank SYSTEM/SCHEMA)  4. attach the candidate's result and the quoted paragraph that states it (read from the stored decision text)
Dry run prints a cost ceiling. --send runs. --cap-usd is a hard ledger ceiling."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
import run_draft as RD, run_rerank as RR  # noqa: E402
from match_library import Index  # noqa: E402
HERE = Path(__file__).resolve().parent


def load_library():
	lib, paras = [], {}
	for iss_dir, inp_dir in (("out_stage2/issues", "inputs"), ("out_wave2/issues", "inputs_wave2")):
		for f in sorted((HERE / iss_dir).glob("case_*_issues_gpt-4.1-mini.json")):
			x = json.loads(f.read_text(encoding="utf-8"))
			cid = x["case_id"]
			doc = json.loads((HERE / inp_dir / f"case_{cid}.json").read_text(encoding="utf-8"))
			paras[cid] = {p["paragraph_index"]: p["text"] for p in doc["paragraphs"]}
			for i in x["result"]["issues"]:
				lib.append({"case_id": cid, "citation": doc["citation"], "issue": i["issue"], "applicant_position": i["applicant_position"], "result": i["result"], "result_text": i["result_text"], "result_para": i["result_para"], "text": i["issue"] + " " + i["applicant_position"]})
	return lib, paras


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--drafts", type=Path, required=True)
	ap.add_argument("--model", default="gpt-4.1", choices=sorted(PRICES))
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--cap-usd", type=float, required=True)
	ap.add_argument("--stop-file", type=Path, default=None)
	a = ap.parse_args()
	lib, paras = load_library()
	idx = Index(lib)
	ledger = SpendLedger(a.ledger, a.cap_usd)
	client = make_client() if a.send else None
	a.out_dir.mkdir(parents=True, exist_ok=True)
	ceiling = 0.0
	for f in sorted(a.drafts.glob("*.json")):
		d = json.loads(f.read_text(encoding="utf-8"))
		path = a.out_dir / f"{d['draft_id']}_chain.json"
		if a.send and path.exists():
			print(json.dumps({"draft": d["draft_id"], "skipped": True}), flush=True)
			continue
		body = "\n".join(f"[{p['n']}] {p['text']}" for p in d["paragraphs"])
		msgs = [{"role": "system", "content": RD.SYSTEM}, {"role": "user", "content": RD.frame(d) + "\n\nDraft:\n" + body}]
		tin = int(sum(len(m["content"]) for m in msgs) / 3.2)
		if not a.send:
			ceiling += cost_usd(a.model, tin, 2500) + 8 * cost_usd(a.model, 3200, 200)
			continue
		if a.stop_file is not None and a.stop_file.exists():
			raise SystemExit(3)
		data, u = call_json(client, ledger, run="chain_extract", model=a.model, messages=msgs, schema_name="draft_args", schema=RD.SCHEMA, max_output_tokens=6000, est_input_tokens=tin, label=f"extract {d['draft_id']}")
		usd = u["usd"]
		out = []
		for j, arg in enumerate(data["arguments"]):
			cands = [x for s, x in idx.top(arg["issue"] + " " + arg["claim"], 40) if x["case_id"] != d.get("case_id")][:20]
			lines = "\n".join(f"{i}. {c['issue']} | applicant said: {c['applicant_position']} | result: {c['result']}" for i, c in enumerate(cands))
			m2 = [{"role": "system", "content": RR.SYSTEM}, {"role": "user", "content": f"Argument issue: {arg['issue']}\nArgument: {arg['claim']}\n\nCandidates:\n{lines}"}]
			r, u2 = call_json(client, ledger, run="chain_rerank", model=a.model, messages=m2, schema_name="rerank", schema=RR.SCHEMA, max_output_tokens=600, est_input_tokens=int(sum(len(m["content"]) for m in m2) / 3.2), label=f"rerank {d['draft_id']}#{j}")
			usd += u2["usd"]
			b = r["best"]
			best = None
			if 0 <= b < len(cands) and r["labels"][b] != "different":
				c = cands[b]
				best = {"label": r["labels"][b], "citation": c["citation"], "case_id": c["case_id"], "issue": c["issue"], "result": c["result"], "result_para": c["result_para"], "quoted_paragraph": paras[c["case_id"]].get(c["result_para"], "")[:600]}
			out.append({"argument": arg, "best_match": best})
		path.write_text(json.dumps({"draft_id": d["draft_id"], "model": a.model, "usd": round(usd, 4), "results": out}, ensure_ascii=False, indent=1), encoding="utf-8")
		print(json.dumps({"draft": d["draft_id"], "usd": round(usd, 4), "arguments": len(out)}), flush=True)
	print(json.dumps({"done": True, "ledger_total_usd": round(ledger.total(), 4)} if a.send else {"dry_run": True, "model": a.model, "library_issues": len(lib), "ceiling_usd": round(ceiling, 3)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
