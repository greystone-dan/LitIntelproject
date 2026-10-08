"""Paragraph layer (prompt version para_v2): speaker, one-sentence summary and single/multiple idea flag for EVERY paragraph, then a case overview and
broad issue sections built from the summaries alone. No citations, no rebuttals (they are tied in later). Public case law only; nothing is written to the database.

Changes from sum_v1: evidence/testimony is its own speaker ('evidence'); footnote numbers and footnote text are ignored; paragraphs the model skipped
are re-asked once (missing-paragraph retry); stage 2 returns overview + issue sections (paragraph ranges) instead of party points and rebuttals.
Without --send it prints a cost ceiling per case. Stop file: if --stop-file exists the run stops before the next call.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from extract_themes_v5 import META, header  # noqa: E402
from summarize_paragraphs import clean  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "para_v2"
VARIANTS = ("base", "brief", "role", "g3", "ctx3")  # g3 = one summary per group of 3 consecutive paragraphs; ctx3 = per-paragraph summaries with the neighbouring paragraphs shown as context only; base = fixes only; brief = case brief (parties, issues) read first and shown with every chunk; role = adds a one-word paragraph role
CHUNK = 30

SYSTEM_SUM = """You read numbered paragraphs of a Canadian court or tribunal decision. For EVERY paragraph shown, in order, return:
- para: the paragraph number exactly as shown.
- speaker, who is speaking in the paragraph:
  court = the decision-maker's own reasoning, findings, conclusions, or its statement of the law it applies (including the court narrating background);
  party = a party's or counsel's position, argument or concession being reported (name who in the summary);
  below = a report of the decision under review (for example the RPD's or an officer's findings in a later decision);
  evidence = a witness's testimony, an affidavit, a document or an expert report being described;
  other = procedure, headings, quoted statute wording, or anything that fits none of the above.
- summary: ONE plain sentence, at most 25 words, saying what the paragraph says: the point made and who makes it. If the decision-maker answers, accepts or rejects an earlier point, say so and name that point briefly. Include key facts (dates, amounts, outcome) when the paragraph is mainly factual. Use only the paragraph text; no outside knowledge.
- ideas: "single" if the paragraph makes one main point, "multiple" if it makes two or more separate points (for example a party argument and the court's answer, or two grounds). idea_list: when "multiple", each point in a few words; empty when "single".
Ignore footnote numbers and footnote text that run into a paragraph. Do not merge paragraphs and do not skip any."""

SCHEMA_SUM = {"type": "object", "additionalProperties": False, "required": ["paragraphs"], "properties": {"paragraphs": {"type": "array", "items": {
	"type": "object", "additionalProperties": False, "required": ["para", "speaker", "summary", "ideas", "idea_list"],
	"properties": {
		"para": {"type": "integer"},
		"speaker": {"type": "string", "enum": ["court", "party", "below", "evidence", "other"]},
		"summary": {"type": "string"},
		"ideas": {"type": "string", "enum": ["single", "multiple"]},
		"idea_list": {"type": "array", "items": {"type": "string"}}}}}}}

SYSTEM_G3 = """You read numbered paragraphs of a Canadian court or tribunal decision, already split into groups of three consecutive paragraphs (the last group of a chunk may have fewer). For EVERY group shown, in order, return:
- para: the first paragraph number of the group; last: the last paragraph number of the group.
- speaker: court (the decision-maker's own reasoning, findings or statement of the law), party (a party's or counsel's position or concession being reported), below (a report of the decision under review), evidence (testimony, affidavit, document or expert report being described), other (procedure, headings, quoted statute wording), or mixed if the group clearly has more than one speaker.
- summary: ONE plain sentence, at most 40 words, saying what the group says: the points made and who makes them. If the decision-maker answers, accepts or rejects an earlier point, say so. Use only the text shown.
- ideas: "single" if the group develops one main point, "multiple" if two or more separate points; idea_list: when "multiple", each point in a few words.
Ignore footnote numbers and footnote text that run into a paragraph. Do not skip any group."""
SCHEMA_G3 = {"type": "object", "additionalProperties": False, "required": ["groups"], "properties": {"groups": {"type": "array", "items": {
	"type": "object", "additionalProperties": False, "required": ["para", "last", "speaker", "summary", "ideas", "idea_list"],
	"properties": {"para": {"type": "integer"}, "last": {"type": "integer"}, "speaker": {"type": "string", "enum": ["court", "party", "below", "evidence", "other", "mixed"]},
		"summary": {"type": "string"}, "ideas": {"type": "string", "enum": ["single", "multiple"]}, "idea_list": {"type": "array", "items": {"type": "string"}}}}}}}

SYSTEM_BRIEF = """Read this Canadian court or tribunal decision and return a case brief for a reader who will summarize it paragraph by paragraph: who the parties are (and who is the applicant/appellant), what is being challenged, and the 2 to 5 issues the decision-maker deals with, in plain words. At most 120 words in total. Use only the text."""
SCHEMA_BRIEF = {"type": "object", "additionalProperties": False, "required": ["brief"], "properties": {"brief": {"type": "string"}}}
ROLE_TEXT = "\n- role: facts, procedural_history, issue, law, analysis, conclusion, disposition or other: the job the paragraph does in the decision."

SYSTEM_STRUCT = """You are given the paragraph-by-paragraph summaries of a Canadian court or tribunal decision (paragraph number, speaker, one sentence). Using ONLY these summaries, return:
- overview: three sentences at most saying what the case is about, who the parties are and how it came out.
- sections: the broad parts of the decision in order, covering every paragraph once with no gaps: first (first paragraph), last (last paragraph), label (a few plain words, for example "Background", "Issue: procedural fairness", "Standard of review", "Disposition"), kind (background, issue, standard_of_review, analysis, disposition, other).
Use paragraph numbers exactly as given."""

SCHEMA_STRUCT = {"type": "object", "additionalProperties": False, "required": ["overview", "sections"], "properties": {
	"overview": {"type": "string"},
	"sections": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["first", "last", "label", "kind"], "properties": {
		"first": {"type": "integer"}, "last": {"type": "integer"}, "label": {"type": "string"},
		"kind": {"type": "string", "enum": ["background", "issue", "standard_of_review", "analysis", "disposition", "other"]}}}}}}


def run_case(client, ledger, run, model, case_id, report, send, stop_file, variant="base"):
	paras = [p for p in load_paragraphs(report) if p["paragraph_index"] != 0]
	head = header(case_id)
	pre = (head + "\n\n") if head else ""
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	sysmsg = SYSTEM_SUM.replace("\nIgnore footnote", ROLE_TEXT + "\nIgnore footnote") if variant == "role" else SYSTEM_SUM
	schema = json.loads(json.dumps(SCHEMA_SUM))
	if variant == "role":
		it = schema["properties"]["paragraphs"]["items"]
		it["required"].append("role")
		it["properties"]["role"] = {"type": "string", "enum": ["facts", "procedural_history", "issue", "law", "analysis", "conclusion", "disposition", "other"]}
	state = {"brief": ""}
	idx = {p["paragraph_index"]: i for i, p in enumerate(paras)}

	def ctx_block(ch):
		i0, i1 = idx[ch[0]["paragraph_index"]], idx[ch[-1]["paragraph_index"]]
		before = paras[max(0, i0 - 1):i0]
		after = paras[i1 + 1:i1 + 2]
		return before, after
	render = lambda ch: [{"role": "system", "content": sysmsg + (("\n\nCase brief (for orientation only; summarize each paragraph from its own text):\n" + state["brief"]) if state["brief"] else "")}, {"role": "user", "content": pre + (("CONTEXT ONLY, do not summarize (previous paragraph):\n" + "\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in ctx_block(ch)[0]) + "\n\nPARAGRAPHS TO SUMMARIZE:\n") if variant == "ctx3" and ctx_block(ch)[0] else "") + "\n\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in ch) + (("\n\nCONTEXT ONLY, do not summarize (next paragraph):\n" + "\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in ctx_block(ch)[1])) if variant == "ctx3" and ctx_block(ch)[1] else "")}]  # noqa: E731
	chunks = [paras[i:i + CHUNK] for i in range(0, len(paras), CHUNK)]
	if variant == "g3":
		render = lambda ch: [{"role": "system", "content": SYSTEM_G3}, {"role": "user", "content": pre + "\n\n".join(  # noqa: E731
			f"GROUP {g[0]['paragraph_index']}-{g[-1]['paragraph_index']}:\n" + "\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in g) for g in (ch[i:i + 3] for i in range(0, len(ch), 3)))}]
	if not send:
		tin = sum(est(render(c)) for c in chunks) + 2500 + (sum(len(p["text"]) for p in paras) // 3 + 400 + 250 * len(chunks) if variant == "brief" else 0)
		tout = 90 * len(paras) * (1.1 if variant == "role" else 0.5 if variant == "g3" else 1) + 1200 + (250 if variant == "brief" else 0)
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "paragraphs": len(paras), "calls": len(chunks) + 1, "est_input_tokens": tin, "est_usd_max": round(cost_usd(model, tin, tout), 4)}))
		return None

	def stop():
		if stop_file is not None and stop_file.exists():
			print(json.dumps({"stopped": "stop file found", "case_id": case_id}), flush=True)
			raise SystemExit(3)

	usd, rows, dropped = 0.0, {}, 0
	covered_by_group = set()

	def ask(ch):
		nonlocal usd, dropped
		stop()
		msgs = render(ch)
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="summaries", schema=(SCHEMA_G3 if variant == "g3" else schema), max_output_tokens=min(16000, 400 + 200 * len(ch)), est_input_tokens=est(msgs), label=f"para case {case_id}")
		usd += u["usd"]
		want = {p["paragraph_index"] for p in ch}
		if variant == "g3":
			for r in data["groups"]:
				if r["para"] in want and r["para"] not in rows:
					rows[r["para"]] = r
					covered_by_group.update(range(r["para"], r["last"] + 1))
				else:
					dropped += 1
			return
		for r in data["paragraphs"]:
			if r["para"] in want and r["para"] not in rows:
				rows[r["para"]] = r
			else:
				dropped += 1

	if variant == "brief":
		stop()
		fulltext = [{"role": "system", "content": SYSTEM_BRIEF}, {"role": "user", "content": pre + "\n\n".join(f"[{p['paragraph_index']}] {clean(p['text'])}" for p in paras)}]
		b, u = call_json(client, ledger, run=run, model=model, messages=fulltext, schema_name="brief", schema=SCHEMA_BRIEF, max_output_tokens=400, est_input_tokens=est(fulltext), label=f"brief case {case_id}")
		usd += u["usd"]
		state["brief"] = b["brief"]
	for ch in chunks:
		ask(ch)
	have = lambda: set(rows) | covered_by_group  # noqa: E731
	retried = sorted({p["paragraph_index"] for p in paras} - have())
	if retried:
		ask([p for p in paras if p["paragraph_index"] in set(retried)])
	missing = sorted({p["paragraph_index"] for p in paras} - have())
	ordered = [rows[k] for k in sorted(rows)]
	listing = "\n".join(f"{r['para']}{('-' + str(r['last'])) if variant == 'g3' else ''}\t{r['speaker']}\t{r['summary']}" for r in ordered)
	msgs = [{"role": "system", "content": SYSTEM_STRUCT}, {"role": "user", "content": pre + listing}]
	stop()
	struct, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="structure", schema=SCHEMA_STRUCT, max_output_tokens=2500, est_input_tokens=est(msgs), label=f"struct case {case_id}")
	usd += u["usd"]
	covered = set()
	for s in struct["sections"]:
		covered |= set(range(s["first"], s["last"] + 1))
	gaps = sorted({p["paragraph_index"] for p in paras} - covered)
	speakers = {}
	for r in ordered:
		speakers[r["speaker"]] = speakers.get(r["speaker"], 0) + 1
	check = {"paragraphs": len(paras), "summaries": len(ordered), "paragraphs_missing": missing, "retried": len(retried), "dropped_rows": dropped, "speakers": speakers,
		"multi_idea_paragraphs": sum(1 for r in ordered if r["ideas"] == "multiple"), "sections": len(struct["sections"]), "section_gap_paragraphs": len(gaps)}
	return {"brief": state["brief"], "usd": usd, "summaries": ordered, "structure": struct, "verification": check}


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
	ap.add_argument("--variant", default="base", choices=VARIANTS)
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
		out = run_case(client, ledger, args.run, args.model, cid, json.loads(path.read_text(encoding="utf-8")), args.send, args.stop_file, args.variant)
		if out is None:
			continue
		(args.out_dir / f"case_{cid}_para_{PROMPT_VERSION}_{args.variant}_{args.model}.json").write_text(json.dumps({"case_id": cid, "model": args.model, "prompt_version": PROMPT_VERSION, "variant": args.variant, "run": args.run, "usage": {"usd": out["usd"]}, "verification": out["verification"], "structure": out["structure"], "brief": out.get("brief", ""), "summaries": out["summaries"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": cid, "model": args.model, "prompt": PROMPT_VERSION, "usd": round(out["usd"], 4), **{k: v for k, v in out["verification"].items() if k != "paragraphs_missing"}, "paragraphs_missing": len(out["verification"]["paragraphs_missing"])}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
