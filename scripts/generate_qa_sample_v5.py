"""Build citation QA sample v5 from an evaluator run, balanced across court x decision-date period.

Read-only. Usage: python scripts/generate_qa_sample_v5.py
"""

import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import text

from backend.database import SessionLocal

random.seed(42)
ROWS = Path("data/eval/qa_sample_v5/rows.csv")
STRATA = json.load(open("data/eval/v5_case_strata.json"))
OUT = Path("citation-refinement/qa-sample-v5.json")
TARGETS = {"case_citations_added": 50, "case_citations_dropped": 30, "statute_citations_added": 20}


def category(r):
	if r["layer"] == "cases" and r["action"] == "added":
		return "case_citations_added"
	if r["layer"] == "cases" and r["action"] == "dropped":
		return "case_citations_dropped"
	if r["layer"] == "laws" and r["action"] == "added":
		return "statute_citations_added"
	return None


def balanced(rows, n):
	bins = defaultdict(list)
	for r in rows:
		bins[tuple(r["_stratum"])].append(r)
	for b in bins.values():
		random.shuffle(b)
	keys = sorted(bins)
	out = []
	while len(out) < n and any(bins.values()):
		for k in keys:
			if bins[k] and len(out) < n:
				out.append(bins[k].pop())
	return out


def main():
	rows = list(csv.DictReader(open(ROWS, encoding="utf-8")))
	cats = defaultdict(list)
	for r in rows:
		c = category(r)
		cid = r["source"].split(":")[-1]
		if c and cid in STRATA:
			r["_stratum"] = STRATA[cid]
			cats[c].append(r)
	s = SessionLocal()
	out = {"metadata": {"random_seed": 42, "context_chars_per_side": 300, "stratified_by": "court x decision-date period", "available": {k: len(v) for k, v in cats.items()}}, "data": {}}
	for c, n in TARGETS.items():
		out["data"][c] = []
		for r in balanced(cats[c], n):
			cid = int(r["source"].split(":")[-1])
			case = s.execute(text("select citation, docket_number, court, date, full_text from cases where id=:i"), {"i": cid}).first()
			body = case.full_text or ""
			a, b = int(r["offset_start"] or 0), int(r["offset_end"] or 0)
			out["data"][c].append({
				"case_id": cid, "case_neutral_citation": case.citation, "case_docket_number": case.docket_number,
				"case_court": case.court, "case_date": str(case.date), "period": r["_stratum"][0],
				"layer": r["layer"], "kind": r["kind"], "step": r["step"], "action": r["action"],
				"extracted_text": r["citation_text"], "normalized": r["normalized_citation"], "confidence": r["confidence"],
				"identifiers_or_instrument": r["identifiers_or_instrument"], "provision_or_pinpoints": r["provision_or_pinpoints"], "notes": r["notes"],
				"decision_context": {"before": body[max(0, a - 300):a], "cited": body[a:b], "after": body[b:b + 300]},
			})
	out["metadata"]["total_rows"] = sum(len(v) for v in out["data"].values())
	OUT.parent.mkdir(exist_ok=True)
	json.dump(out, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
	allrows = [x for v in out["data"].values() for x in v]
	print("total", len(allrows))
	print("court", dict(Counter(x["case_court"] for x in allrows)))
	print("period", dict(Counter(x["period"] for x in allrows)))
	print("court x period", dict(Counter((x["case_court"], x["period"]) for x in allrows)))
	print("years", sorted(Counter(x["case_date"][:4] for x in allrows).items()))


if __name__ == "__main__":
	main()
