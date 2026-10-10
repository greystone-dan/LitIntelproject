"""No-AI checks over stage-2 outputs. They flag items for softer display; they never rewrite a label.
  direction_cue   the answer paragraph says the decision-maker agrees/disagrees with a named side, and that side is the holder of the point, but the label says the opposite
  dissent_suspect (issues) the result paragraph says "I would allow/dismiss" while the closing order says the opposite and mentions a dissent
  partial_cue     the answer paragraph says "in part"/"partly"/"partially" but the label is a flat accepted/rejected
Usage: python stage2_checks.py --inputs inputs --lf-dir out/LF --stage2 out_stage2 [--model gpt-4.1-mini]"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

SIDE = r"(appellants?|respondents?|applicants?|claimants?|minister|attorney general|crown|commission)"
AGREE = re.compile(r"\b(?:i|we|the (?:rad|rpd|panel|court|tribunal|member))\s+(?:also\s+)?(?:agrees?|accepts?|finds? merit in)\s+(?:with|the)\s+(?:the\s+)?" + SIDE, re.I)
DISAGREE = re.compile(r"\b(?:i|we|the (?:rad|rpd|panel|court|tribunal|member))\s+(?:respectfully\s+)?(?:disagrees?|rejects?|does not accept|do not accept)\b[^.]{0,40}?\b(?:with\s+)?(?:the\s+)?" + SIDE, re.I)
PART = re.compile(r"\b(in part|partly|partially|to some extent)\b", re.I)
WOULD = re.compile(r"\bI would (allow|dismiss)\b", re.I)
ORDER = re.compile(r"\bappeals?\s+(allowed|dismissed)\b", re.I)


def side_of(holder_text: str) -> str:
	return re.sub(r"s$", "", holder_text.lower())


def check_answers(doc, lf, ans, partial=False):
	"""Return flags for party points whose label contradicts a direction cue in the answering paragraph."""
	paras = {p["paragraph_index"]: p["text"] for p in doc["paragraphs"]}
	pts = {}
	k = 0
	for r in lf["paragraphs"]:
		for p in r["propositions"]:
			k += 1
			pts[k] = (r["para"], p)
	flags = []
	for a in ans["result"]["answers"]:
		para, p = pts[a["id"]]
		holder = p["holder"]  # applicant | respondent
		for sid in a["answered_by"]:
			if sid not in pts:
				continue
			ap, _ = pts[sid]
			text = paras.get(ap, "")
			m = AGREE.search(text)
			if m and a["outcome"] == "rejected":
				s = side_of(m.group(1))
				if (s in ("applicant", "appellant", "claimant") and holder == "applicant") or (s not in ("applicant", "appellant", "claimant") and holder == "respondent"):
					flags.append({"id": a["id"], "flag": "direction_cue", "para": ap, "cue": m.group(0)})
					break
			if partial and PART.search(text) and a["outcome"] in ("accepted", "rejected"):
				flags.append({"id": a["id"], "flag": "partial_cue", "para": ap, "cue": PART.search(text).group(0)})
				break
	return flags


def check_issues(doc, iss):
	paras = {p["paragraph_index"]: p["text"] for p in doc["paragraphs"]}
	tail = " ".join(paras[k] for k in sorted(paras)[-3:])
	om = ORDER.search(tail)
	flags = []
	if om and re.search(r"dissent", tail, re.I):
		majority = om.group(1).lower()
		for i, it in enumerate(iss["result"]["issues"], 1):
			w = WOULD.search(paras.get(it["result_para"], ""))
			if w and w.group(1).lower()[:5] != majority[:5]:
				flags.append({"n": i, "flag": "dissent_suspect", "para": it["result_para"], "cue": w.group(0) + " vs order " + om.group(0)})
	return flags


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--inputs", type=Path, required=True)
	ap.add_argument("--lf-dir", type=Path, required=True)
	ap.add_argument("--stage2", type=Path, required=True)
	ap.add_argument("--model", default="gpt-4.1-mini")
	ap.add_argument("--with-partial", action="store_true", help="also flag the noisy in-part cue (38 flags on 100 cases, mostly right labels)")
	a = ap.parse_args()
	tot = {}
	for f in sorted((a.stage2 / "answers").glob(f"case_*_answers_{a.model}.json")):
		ans = json.loads(f.read_text(encoding="utf-8"))
		cid = ans["case_id"]
		doc = json.loads((a.inputs / f"case_{cid}.json").read_text(encoding="utf-8"))
		lf = json.loads(next(a.lf_dir.glob(f"case_{cid}_*.json")).read_text(encoding="utf-8"))
		for fl in check_answers(doc, lf, ans, a.with_partial):
			print(json.dumps({"case_id": cid, **fl}, ensure_ascii=False))
			tot[fl["flag"]] = tot.get(fl["flag"], 0) + 1
	for f in sorted((a.stage2 / "issues").glob(f"case_*_issues_{a.model}.json")):
		iss = json.loads(f.read_text(encoding="utf-8"))
		cid = iss["case_id"]
		doc = json.loads((a.inputs / f"case_{cid}.json").read_text(encoding="utf-8"))
		for fl in check_issues(doc, iss):
			print(json.dumps({"case_id": cid, **fl}, ensure_ascii=False))
			tot[fl["flag"]] = tot.get(fl["flag"], 0) + 1
	print(json.dumps({"flag_totals": tot}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
