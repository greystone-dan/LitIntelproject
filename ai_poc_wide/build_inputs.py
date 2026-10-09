"""Pick a varied set of decisions from fetched public case pages and write one input file per decision (paragraphs, code-built frame).

No model, no database. Input: pool JSON files made from the public read-only pages of www.ilit.ca (id, court, date, text ...).
Usage: python build_inputs.py --pool pool.json --pool pool_scc.json --out inputs --seed wide100
"""
from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

from split_paras import resplit

MARK = re.compile(r"(?:(?<=\s)|^)\[(\d{1,3})\](?=\s)")
FORUM = {"FC": "Federal Court", "FCA": "Federal Court of Appeal", "SCC": "Supreme Court of Canada", "RPD": "Refugee Protection Division (first-instance tribunal)", "RAD": "Refugee Appeal Division (appeal tribunal)"}
NEST = {
	"FC": "The judge is the author (layer 1). The applicant and respondent in this proceeding make submissions to the judge (layer 2). The decision under review was made by an earlier decision-maker (layer 3), and that decision may itself report what a claimant, the Minister or a witness said to that decision-maker (layer 4).",
	"FCA": "The panel is the author (layer 1). The appellant and respondent make submissions to the panel (layer 2). The lower court's or tribunal's reasons are layer 3, and what a party said there, as reported in those reasons, is layer 4.",
	"SCC": "The Court is the author (layer 1); a dissent or concurrence is still the Court's judges (layer 1). The appellant, respondent and interveners make submissions (layer 2). The courts below are layer 3, and what parties said below, as reported, is layer 4.",
	"RPD": "The member of the tribunal is the author (layer 1). The claimant and the Minister make submissions to the member (layer 2). There is no earlier decision-maker unless the reasons describe a prior decision (layer 3). Testimony and documents are layer 5.",
	"RAD": "The RAD member is the author (layer 1). The appellant and the Minister make submissions to the RAD (layer 2). The RPD decision under appeal is layer 3, and what the claimant or the Minister said to the RPD, as reported, is layer 4.",
}


def numbered(text: str) -> list[dict]:
	ms, exp, seq = list(MARK.finditer(text)), 1, []
	for m in ms:
		if int(m.group(1)) == exp:
			seq.append(m)
			exp += 1
	out = []
	for k, m in enumerate(seq):
		end = seq[k + 1].start() if k + 1 < len(seq) else len(text)
		out.append({"paragraph_index": int(m.group(1)), "text": re.sub(r"\s+", " ", text[m.end():end]).strip()})
	return out


def frame(rec: dict, paras: list[dict]) -> str:
	text = rec["text"]
	court = rec["court"]
	lines = [f"Forum: {FORUM.get(court, court)}."]
	m = re.search(r"BETWEEN:\s*(.+?)\s*\n\s*(Applicants?|Appellants?|Plaintiffs?)\s*\n\s*(?:and|AND)\s*\n\s*(.+?)\s*\n\s*(Respondents?|Defendants?)\s*\n", text, re.S)
	if not m:
		m = re.search(r"Between:\s*\n\s*(.+?)\s*(Applicants?|Appellants?)\s*\n\s*(?:and|AND)\s*\n\s*(.+?)\s*(Respondents?)\s*\n", text, re.S)
	if m:
		a = re.sub(r"\s+", " ", m.group(1)).strip()[:160]
		r = re.sub(r"\s+", " ", m.group(3)).strip()[:160]
		lines.append(f"Parties as styled: {m.group(2).lower()} = {a}; {m.group(4).lower()} = {r}.")
	elif court in ("RPD", "RAD"):
		lines.append("Parties: the " + ("claimant" if court == "RPD" else "appellant") + " and the Minister; names are redacted.")
	first = " ".join(p["text"] for p in paras[:4])
	sent = None
	for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", first):
		if re.search(r"\b(judicial review|appeal|appealing|appeals|seeks leave|application)\b.{0,160}\b(decision|order|judgment|determination|reasons|ruling)\b", s, re.I):
			sent = s.strip()
			break
	if court == "RPD":
		lines.append("Decision under review: none; this is the first-instance decision.")
	elif sent:
		lines.append("Decision under review (from the opening paragraphs): " + sent[:320])
	lines.append("How the layers nest here: " + NEST.get(court, ""))
	return "\n".join(lines)


def main() -> int:
	ap = argparse.ArgumentParser()
	ap.add_argument("--pool", type=Path, action="append", required=True)
	ap.add_argument("--out", type=Path, required=True)
	ap.add_argument("--seed", default="wide100")
	ap.add_argument("--quota", default="FCimm=26,FCother=4,FCfr=7,FCA=14,SCC=10,RPD=17,RAD=22")
	args = ap.parse_args()
	pool = {}
	for p in args.pool:
		for r in json.loads(p.read_text()):
			if r.get("text"):
				pool[r["id"]] = r
	rng = random.Random(args.seed)

	def lim(r):
		hi, chars, since = (100, 140000, "2008") if r["court"] == "SCC" else (90, 100000, "2010" if r["court"] == "RPD" else "2015")
		return 12 <= r["n"] <= hi and r["chars"] <= chars and (r["date"] or "") >= since

	imm = re.compile(r"Immigration|Citizenship|Minister of Public Safety", re.I)
	groups = {
		"FCimm": [r for r in pool.values() if r["court"] == "FC" and not r["fr"] and imm.search(r["title"]) and lim(r)],
		"FCother": [r for r in pool.values() if r["court"] == "FC" and not r["fr"] and not imm.search(r["title"]) and lim(r)],
		"FCfr": [r for r in pool.values() if r["fr"] and r["court"] in ("FC", "FCA", "SCC") and lim(r)],
		"FCA": [r for r in pool.values() if r["court"] == "FCA" and not r["fr"] and lim(r)],
		"SCC": [r for r in pool.values() if r["court"] == "SCC" and not r["fr"] and lim(r) and r["n"] <= 100],
		"RPD": [r for r in pool.values() if r["court"] == "RPD" and lim(r)],
		"RAD": [r for r in pool.values() if r["court"] == "RAD" and lim(r)],
	}
	picked = []
	for part in args.quota.split(","):
		k, n = part.split("=")
		g = sorted(groups[k], key=lambda r: r["id"])
		rng.shuffle(g)
		take = [r for r in g if r["id"] not in {p["id"] for p in picked}][:int(n)]
		print(k, "available", len(g), "taking", len(take))
		picked += take
	args.out.mkdir(parents=True, exist_ok=True)
	rows = []
	for r in picked:
		paras = resplit([{"paragraph_index": p["paragraph_index"], "text": re.sub(r"^(\s*\[\d{1,3}\]\s*)+", "", p["text"]).strip()} for p in numbered(r["text"])])
		paras = [p for p in paras if p["text"]]
		dissent = bool(re.search(r"dissent|motifs dissidents|dissidents", r["text"][:6000], re.I)) if r["court"] == "SCC" else False
		doc = {"case_id": r["id"], "title": r["title"], "citation": r["citation"], "court": r["court"], "date": r["date"], "french": bool(r["fr"]), "dissent": dissent,
			"frame": frame(r, paras), "paragraphs": paras}
		(args.out / f"case_{r['id']}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
		rows.append({"case_id": r["id"], "court": r["court"], "citation": r["citation"], "date": r["date"], "title": r["title"], "french": int(bool(r["fr"])), "dissent": int(dissent), "paragraphs": len(paras), "chars": sum(len(p["text"]) for p in paras)})
	import csv
	with (args.out / "selection.csv").open("w", newline="", encoding="utf-8") as h:
		w = csv.DictWriter(h, fieldnames=list(rows[0]))
		w.writeheader()
		w.writerows(rows)
	print(json.dumps({"picked": len(rows), "paragraphs": sum(x["paragraphs"] for x in rows), "chars": sum(x["chars"] for x in rows)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
