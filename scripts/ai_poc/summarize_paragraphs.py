"""Summary-first pipeline (prompt version sum_v1): one-line summary of every paragraph, what each citation in the paragraph is used for, then the argument
structure built from the summaries alone. Public case law only; nothing is written to the database or the site.

Per decision: stage 1 = chunks of up to CHUNK paragraphs (each paragraph: speaker, one-sentence summary, and one entry per citation with a broad purpose);
stage 2 = one call that sees only the summaries and returns party points, rebuttals (answer paragraph linked to the point it answers) and left-open points.
Also computes, with code only: the share of regex-found citations that the model addressed, and a list of pinpointed case citations ("2019 SCC 65 at para 52")
for the read-only cited-paragraph export. Without --send it prints a cost ceiling per case. Stop file: if --stop-file exists the run stops before the next call.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from extract_citation_use import NEUTRAL, REPORTER, STATUTE  # noqa: E402
from extract_themes_v5 import META, header  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "sum_v1"
CHUNK = 30
PURPOSES = ["standard_of_review_or_test", "supports_court_conclusion", "party_argument_reported", "distinguished_or_rejected", "background_or_other"]

SYSTEM_SUM = """You read numbered paragraphs of a Canadian court or tribunal decision. For EVERY paragraph shown, in order, return:
- para: the paragraph number exactly as shown.
- speaker: court (the decision-maker's own reasoning or findings), party (a party's or counsel's position being reported; say who in the summary), below (a report of the decision under review, for example the RPD's findings in a RAD decision), or other (procedure, facts, quoted law, headings).
- summary: ONE plain sentence, at most 25 words, saying what the paragraph says: the point made and who makes it. If the decision-maker answers, accepts or rejects an earlier point, say so and name that point briefly. Use only the paragraph; no outside knowledge.
- ideas: "single" if the paragraph makes one main point, "multiple" if it makes two or more separate points (for example a party argument and the court's answer, or two different grounds). idea_list: when "multiple", each point in a few words; empty when "single".
- citations: one entry for EVERY citation in the paragraph (every case, statute or regulation section, rule, or textbook/report cited, including repeated mentions with a different pinpoint or job). Do not skip any. For each:
  - cite: the citation as written in the paragraph (short: name, neutral citation or section, and pinpoint if given).
  - kind: case, statute, rule, or other.
  - purpose, the broad reason the paragraph cites it:
    standard_of_review_or_test = states the standard of review, a legal test or a settled rule of law that the decision then applies;
    supports_court_conclusion = backs the decision-maker's own finding or conclusion on this case;
    party_argument_reported = the paragraph only reports that a party or counsel relies on it;
    distinguished_or_rejected = the decision-maker distinguishes it, does not follow it, or finds it does not apply;
    background_or_other = background, procedure, a quotation of the statute's wording, or anything else.
  - why: at most 15 words saying what the citation is used for here, in your own words.
Do not merge paragraphs and do not skip any. A paragraph with no citations has an empty citations list."""

SCHEMA_SUM = {"type": "object", "additionalProperties": False, "required": ["paragraphs"], "properties": {"paragraphs": {"type": "array", "items": {
	"type": "object", "additionalProperties": False, "required": ["para", "speaker", "summary", "ideas", "idea_list", "citations"],
	"properties": {
		"para": {"type": "integer"},
		"speaker": {"type": "string", "enum": ["court", "party", "below", "other"]},
		"summary": {"type": "string"},
		"ideas": {"type": "string", "enum": ["single", "multiple"]},
		"idea_list": {"type": "array", "items": {"type": "string"}},
		"citations": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["cite", "kind", "purpose", "why"], "properties": {
			"cite": {"type": "string"}, "kind": {"type": "string", "enum": ["case", "statute", "rule", "other"]},
			"purpose": {"type": "string", "enum": PURPOSES}, "why": {"type": "string"}}}}}}}}}

SYSTEM_STRUCT = """You are given the paragraph-by-paragraph summaries of a Canadian court or tribunal decision (paragraph number, speaker, one sentence). Using ONLY these summaries, return:
- overview: three sentences at most saying what the case is about, who the parties are and how it came out.
- party_points: the distinct points made by a party or counsel (including grounds of appeal and what an appellant says the lower body got wrong), one entry each: id (P1, P2, ...), para (where it is stated), by (who), text (a few words).
- rebuttals: each place the decision-maker answers a specific earlier party point: answer_para, answers (the id of the point; one entry per point if a paragraph answers several), verdict (rejects, accepts, partly, not_decided).
- left_open: points the decision-maker says it does not decide: para and text.
Use paragraph numbers exactly as given. Only use what the summaries support."""

SCHEMA_STRUCT = {"type": "object", "additionalProperties": False, "required": ["overview", "party_points", "rebuttals", "left_open"], "properties": {
	"overview": {"type": "string"},
	"party_points": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["id", "para", "by", "text"], "properties": {"id": {"type": "string"}, "para": {"type": "integer"}, "by": {"type": "string"}, "text": {"type": "string"}}}},
	"rebuttals": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["answer_para", "answers", "verdict"], "properties": {"answer_para": {"type": "integer"}, "answers": {"type": "string"}, "verdict": {"type": "string", "enum": ["rejects", "accepts", "partly", "not_decided"]}}}},
	"left_open": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["para", "text"], "properties": {"para": {"type": "integer"}, "text": {"type": "string"}}}}}}

PIN = re.compile(r"((?:19|20)\d{2}\s+(?:SCC|FCA|FC|CAF|CF)\s+\d{1,5})[^.;]{0,120}?\b(?:at\s+)?(?:paras?|paragraphs?)\.?\s*(\d{1,3})(?:\s*(?:-|–|to|and)\s*(\d{1,3}))?", re.I)


def clean(text: str) -> str:
	return re.sub(r"^(\s*\[\d{1,3}\]\s*)+", "", text.replace("\n", " ")).strip()


def run_case(client, ledger, run, model, case_id, report, send, stop_file):
	paras = [p for p in load_paragraphs(report) if p["paragraph_index"] != 0]
	head = header(case_id)
	chunks = [paras[i:i + CHUNK] for i in range(0, len(paras), CHUNK)]
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	text_cites = {p["paragraph_index"]: [m.group(0) for pat in (NEUTRAL, REPORTER, STATUTE) for m in pat.finditer(clean(p["text"]))] for p in paras}
	n_regex = sum(len(v) for v in text_cites.values())
	calls = [[{"role": "system", "content": SYSTEM_SUM}, {"role": "user", "content": (head + "\n\n" if head else "") + "\n\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in ch)}] for ch in chunks]
	if not send:
		tin = sum(est(m) for m in calls) + 2500
		tout = 125 * len(paras) + 45 * n_regex + 1200
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "paragraphs": len(paras), "regex_citations": n_regex, "calls": len(calls) + 1, "est_input_tokens": tin, "est_usd_max": round(cost_usd(model, tin, tout), 4)}))
		return None
	usd, rows, dropped = 0.0, {}, 0
	for msgs, ch in zip(calls, chunks):
		if stop_file is not None and stop_file.exists():
			print(json.dumps({"stopped": "stop file found", "case_id": case_id}), flush=True)
			raise SystemExit(3)
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="summaries", schema=SCHEMA_SUM, max_output_tokens=min(16000, 400 + 300 * len(ch)), est_input_tokens=est(msgs), label=f"sum case {case_id}")
		usd += u["usd"]
		want = {p["paragraph_index"] for p in ch}
		for r in data["paragraphs"]:
			if r["para"] in want:
				rows[r["para"]] = r
			else:
				dropped += 1
	missing = sorted({p["paragraph_index"] for p in paras} - set(rows))
	ordered = [rows[k] for k in sorted(rows)]
	listing = "\n".join(f"{r['para']}\t{r['speaker']}\t{r['summary']}" for r in ordered)
	msgs = [{"role": "system", "content": SYSTEM_STRUCT}, {"role": "user", "content": (head + "\n\n" if head else "") + listing}]
	if stop_file is not None and stop_file.exists():
		raise SystemExit(3)
	struct, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="structure", schema=SCHEMA_STRUCT, max_output_tokens=3500, est_input_tokens=est(msgs), label=f"struct case {case_id}")
	usd += u["usd"]
	# code-only checks
	addressed = 0
	for para, found in text_cites.items():
		mine = " ".join(c["cite"] for c in rows.get(para, {}).get("citations", []))
		norm = re.sub(r"\s+", "", mine).lower()
		addressed += sum(1 for f in found if re.sub(r"\s+", "", f).lower() in norm or (re.search(r"\d+", f) and re.search(r"\d+(?:\.\d+)?", f).group(0) in mine))
	pins = []
	for p in paras:
		for m in PIN.finditer(clean(p["text"])):
			pins.append({"citing_para": p["paragraph_index"], "neutral_citation": re.sub(r"\s+", " ", m.group(1)).upper(), "para_start": int(m.group(2)), "para_end": int(m.group(3) or m.group(2))})
	purposes = {k: 0 for k in PURPOSES}
	for r in ordered:
		for c in r["citations"]:
			purposes[c["purpose"]] += 1
	check = {"paragraphs": len(paras), "summaries": len(ordered), "paragraphs_missing": missing, "paragraphs_not_in_chunk_dropped": dropped, "model_citations": sum(purposes.values()), "regex_citations": n_regex, "regex_addressed": addressed, "pinpoints": len(pins), "purposes": purposes, "multi_idea_paragraphs": sum(1 for r in ordered if r["ideas"] == "multiple"),
		"party_points": len(struct["party_points"]), "rebuttals": len(struct["rebuttals"]), "left_open": len(struct["left_open"])}
	return {"usd": usd, "summaries": ordered, "structure": struct, "pinpoints": pins, "verification": check}


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	ap.add_argument("--run", required=True)
	ap.add_argument("--cases", required=True)
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--send", action="store_true")
	ap.add_argument("--reports-dir", type=Path, action="append")
	ap.add_argument("--meta-csv", type=Path, action="append")
	ap.add_argument("--cap-usd", type=float, default=None)
	ap.add_argument("--stop-file", type=Path, default=None)
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
		if path is None:
			raise SystemExit(f"no report for case {cid}")
		out = run_case(client, ledger, args.run, args.model, cid, json.loads(path.read_text(encoding="utf-8")), args.send, args.stop_file)
		if out is None:
			continue
		(args.out_dir / f"case_{cid}_summary_{PROMPT_VERSION}_{args.model}.json").write_text(json.dumps({"case_id": cid, "model": args.model, "prompt_version": PROMPT_VERSION, "run": args.run, "usage": {"usd": out["usd"]}, "verification": out["verification"], "pinpoints": out["pinpoints"], "structure": out["structure"], "summaries": out["summaries"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": cid, "model": args.model, "prompt": PROMPT_VERSION, "usd": round(out["usd"], 4), **{k: v for k, v in out["verification"].items() if k != "paragraphs_missing"}, "paragraphs_missing": len(out["verification"]["paragraphs_missing"])}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
