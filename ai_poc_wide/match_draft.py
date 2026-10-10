"""No-AI matching of a draft's extracted arguments to decided issues, shaped for the Live Analysis screen.
For each argument: the single most similar decided issue (word match on issue + applicant position, as tested), its result, the quoted paragraph that states the result,
the next two alternatives, a soften flag when the no-AI checks distrust the stored result.
Library = every issue map under out_stage2, out_wave2 and out_wave3_* (whatever exists). Standard library only; no database, no model.
Usage: python match_draft.py --args out_drafts/F41/C4420_F41_gpt-4.1.json [--exclude-case 4420]   (the argument file is a run_draft output)"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from match_library import Index
HERE = Path(__file__).resolve().parent
SOURCES = [("out_stage2/issues", "inputs"), ("out_wave2/issues", "inputs_wave2")] + [(f"out_wave3_{n}/issues", "inputs_wave3") for n in ("300", "594")]
WOULD = re.compile(r"\bI would (allow|dismiss)\b", re.I)
ORDER = re.compile(r"\bappeals?\s+(allowed|dismissed)\b", re.I)
PLAIN = {"allowed_for_applicant": "the applicant won on this issue", "dismissed_for_applicant": "the applicant lost on this issue", "partly_allowed": "partly allowed", "not_decided": "the court did not decide it", "moot_or_procedural": "moot or procedural"}


def load_library():
	lib, paras = [], {}
	for iss_dir, inp_dir in SOURCES:
		for f in sorted((HERE / iss_dir).glob("case_*_issues_*.json")):
			x = json.loads(f.read_text(encoding="utf-8"))
			cid = x["case_id"]
			p = HERE / inp_dir / f"case_{cid}.json"
			if not p.exists():
				continue
			doc = json.loads(p.read_text(encoding="utf-8"))
			paras[cid] = {q["paragraph_index"]: q["text"] for q in doc["paragraphs"]}
			tail = " ".join(paras[cid][k] for k in sorted(paras[cid])[-3:])
			split = bool(ORDER.search(tail) and re.search(r"dissent", tail, re.I))
			for i in x["result"]["issues"]:
				soften = ""
				if split:
					w = WOULD.search(paras[cid].get(i["result_para"], ""))
					if w and w.group(1).lower()[:5] != ORDER.search(tail).group(1).lower()[:5]:
						soften = "This result may come from a dissent; check the Court's final order."
				if i["result_para"] == 0 or i["result"] == "not_decided":
					soften = soften or "No paragraph states a result for this issue."
				lib.append({"case_id": cid, "citation": doc["citation"], "court": doc["court"], "issue": i["issue"], "result": i["result"], "result_para": i["result_para"], "soften": soften, "text": i["issue"] + " " + i["applicant_position"]})
	return lib, paras


def match_argument(idx, paras, arg, exclude=None):
	c = [(s, x) for s, x in idx.top(arg["issue"] + " " + arg["claim"], 40) if x["case_id"] != exclude][:3]
	if not c:
		return None
	def card(s, x):
		return {"score": s, "citation": x["citation"], "court": x["court"], "issue": x["issue"], "result": PLAIN[x["result"]], "paragraph_number": x["result_para"], "quoted_paragraph": paras[x["case_id"]].get(x["result_para"], "")[:600], "soften": x["soften"]}
	return {"basis": "similar wording only; the score did not predict usefulness in the 32-argument test, so no confidence tier is shown", "best": card(*c[0]), "also": [card(s, x) for s, x in c[1:]]}


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--args", type=Path, required=True)
	ap.add_argument("--exclude-case", type=int, default=None)
	a = ap.parse_args()
	lib, paras = load_library()
	idx = Index(lib)
	data = json.loads(a.args.read_text(encoding="utf-8"))
	out = [{"argument": x, "match": match_argument(idx, paras, x, a.exclude_case)} for x in data["result"]["arguments"]]
	print(json.dumps({"library_issues": len(lib), "results": out}, ensure_ascii=False, indent=1))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
