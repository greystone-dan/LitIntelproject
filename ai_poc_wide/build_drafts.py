"""Build the draft-analysis test set (no model, no database): 3 fictional Word memoranda plus 17 one-sided drafts made from decided cases.
A built draft is the verbatim paragraphs of a decision that the stage-1 labels give wholly to the applicant (the party's own submissions as recited), renumbered [1]..[n].
The decision's issues and results (stage 2) are written to a SEPARATE hidden file that is never sent to a model.
Usage: python build_drafts.py --docs <folder with the Word memoranda> --out drafts_test"""
from __future__ import annotations
import argparse, glob, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
PICK = [4420, 27943, 5224, 2697, 29918, 29590, 62989, 75040, 74590, 65838, 68330, 61469, 43929, 50451, 48335, 48372, 47083]
FORUM = {"FC": "Federal Court", "FCA": "Federal Court of Appeal", "SCC": "Supreme Court of Canada", "RPD": "Refugee Protection Division", "RAD": "Refugee Appeal Division"}

def main() -> int:
	ap = argparse.ArgumentParser()
	ap.add_argument("--docs", type=Path, required=True)
	ap.add_argument("--out", type=Path, default=HERE / "drafts_test")
	a = ap.parse_args()
	(a.out / "drafts").mkdir(parents=True, exist_ok=True)
	hidden = {}
	import docx
	for f, forum, side in (("03-fake-individual-moa-prra.docx", "FC", "applicant"), ("04-fake-individual-moa-study-permit.docx", "FC", "applicant"), ("05-fake-minister-moa-cessation.docx", "FC", "the Minister")):
		paras = [p.text.strip() for p in docx.Document(a.docs / f).paragraphs if p.text.strip()]
		body = [t for t in paras[1:]]
		did = "W" + f[:2]
		doc = {"draft_id": did, "forum": forum, "side": side, "source": "fictional Word memorandum", "paragraphs": [{"n": i, "text": t} for i, t in enumerate(body, 1)]}
		(a.out / "drafts" / f"{did}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
	for cid in PICK:
		d = json.loads((HERE / "inputs" / f"case_{cid}.json").read_text(encoding="utf-8"))
		lf = json.loads(next((HERE / "out" / "LF").glob(f"case_{cid}_*.json")).read_text(encoding="utf-8"))
		keep = {r["para"] for r in lf["paragraphs"] if r["propositions"] and all(p["holder"] == "applicant" for p in r["propositions"])}
		texts = [p["text"] for p in d["paragraphs"] if p["paragraph_index"] in keep]
		out, n = [], 0
		for t in texts:
			if n + len(t) > 14000:
				break
			n += len(t)
			out.append(t)
		did = f"C{cid}"
		doc = {"draft_id": did, "forum": d["court"], "side": "applicant", "source": f"verbatim applicant-side paragraphs of case {cid}", "paragraphs": [{"n": i, "text": t} for i, t in enumerate(out, 1)]}
		(a.out / "drafts" / f"{did}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
		iss = json.loads(next((HERE / "out_stage2" / "issues").glob(f"case_{cid}_issues_gpt-4.1-mini.json")).read_text(encoding="utf-8"))["result"]
		hidden[did] = {"case_id": cid, "citation": d["citation"], "overall_result": iss["overall_result"], "issues": [{"issue": i["issue"], "result": i["result"]} for i in iss["issues"]]}
	(a.out / "HIDDEN_answers.json").write_text(json.dumps(hidden, ensure_ascii=False, indent=1), encoding="utf-8")
	print(len(list((a.out / "drafts").glob("*.json"))), "drafts")
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
