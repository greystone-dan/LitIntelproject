"""Propositions layer (prompt version prop_v4): after a code-only split of glued paragraphs and headings (split_paras.py), for EVERY paragraph: a short list of
propositions (who holds it, what kind of statement, the point), a one-sentence summary and a role; then, from the propositions alone, a case overview and
issue blocks (issue, each side's position, the court's conclusion, paragraph ranges). The court is always the writer; 'holder' says whose position is reported.
Public case law only; nothing is written to the database. Without --send it prints a cost ceiling per case. --stop-file stops before the next call.
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
from extract_themes_v5 import META, header  # noqa: E402
from opinion_parts import describe, opinion_parts, part_of  # noqa: E402
from split_paras import resplit  # noqa: E402
from summarize_paragraphs import clean  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "prop_v6"  # prop_v5 plus QA prompt fixes: court evaluations of the tribunal, agreement with a party, sides, headings
CHUNK = 20
REUSE_PROPS: Path | None = None  # --reuse-props DIR: reuse the stored propositions of the same prompt version and rerun only the blocks call
HOLDERS = ["court", "applicant", "respondent", "earlier_decision_maker", "witness_or_document", "prior_court_or_authority", "other"]
KINDS = ["issue", "allegation_or_argument", "finding", "rule_of_law", "fact", "conclusion_or_order", "procedure"]
ROLES = ["facts", "procedural_history", "issue", "law", "analysis", "conclusion", "disposition", "other"]

SYSTEM_P = """You read numbered paragraphs of a Canadian court or tribunal decision. The decision-maker is always the one writing, so do not label who is "speaking". Instead, for EVERY paragraph shown, in order, return:
- para: the paragraph number exactly as shown.
- propositions: one entry for each distinct point the paragraph makes (usually 1 to 4; list every separate item when the paragraph itself lists grounds, objections or findings, one entry per item). Each entry:
  holder = whose position the point is: court (the decision-maker's own reasoning, findings, statement of law or narration), applicant (what the applicant, appellant or claimant alleges, argues or says), respondent (what the respondent, Minister or Crown says), earlier_decision_maker (what the officer, board, tribunal or lower court found or reasoned, as reported here), witness_or_document (testimony, an affidavit, a letter or a document being described), prior_court_or_authority (a case, statute or textbook being relied on), other.
  kind = issue (a question to be decided), allegation_or_argument (what a party claims or argues), finding (a conclusion on the facts or the application of law, including a reported finding), rule_of_law (a legal test, standard or principle), fact (background or procedural fact), conclusion_or_order (the outcome or order), procedure.
  text = the point in at most 22 words, naming who makes it when it is not the court.
  answers = when this point answers or rejects an earlier point in the SAME paragraph, the 1-based position of that point in this paragraph's list; otherwise 0.
- summary: ONE plain sentence, at most 25 words, saying what the paragraph says and who makes each point. Use only the paragraph text.
- role: facts, procedural_history, issue, law, analysis, conclusion, disposition or other: the job the paragraph does in the decision.
Rules learned from grading:
- When the decision-maker evaluates an earlier decision ("the RAD did not err", "the officer reasonably found", "it is clear from the decision that", "failed to consider", "the analysis was unreasonable"), the evaluation is the COURT's point (holder court, kind finding). Only the earlier decision-maker's own reported finding or reasoning is holder earlier_decision_maker; write the two as separate propositions.
- "I agree with the Respondent that X", "the Minister is correct that X", "I accept the Applicant's submission that X": X is the court's finding (holder court) AND the party's argument (holder respondent or applicant, kind allegation_or_argument), as two propositions, the second naming who argued it. Never reduce it to only the party's submission.
- Sides come from who brings the proceeding, not from the order of the names. When the Minister, the Crown or a public body is the appellant or applicant, it is 'applicant'; the individual is then 'respondent'. 'Counsel' or 'counsel for the appellants' is the appellants' side. When a party says it told an earlier decision-maker something ("in his PRRA submissions", "before the RAD the applicant argued"), keep the party as holder and say in the text that it was said to the earlier decision-maker.
- Do not reconstruct an argument from the court's numbered rebuttals ("First... Second..."). Report only what the paragraph states, and mark the court's rebuttal as the court's.
- "[Section heading: ...]" lines and issue questions in a decision are the court's structure, not any party's position.
A line "[Section heading: ...]" before a paragraph is context only: do not summarize it. Ignore footnote numbers. Do not merge paragraphs and do not skip any."""

SCHEMA_P = {"type": "object", "additionalProperties": False, "required": ["paragraphs"], "properties": {"paragraphs": {"type": "array", "items": {
	"type": "object", "additionalProperties": False, "required": ["para", "propositions", "summary", "role"],
	"properties": {
		"para": {"type": "integer"},
		"propositions": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["holder", "kind", "text", "answers"], "properties": {
			"holder": {"type": "string", "enum": HOLDERS}, "kind": {"type": "string", "enum": KINDS}, "text": {"type": "string"}, "answers": {"type": "integer"}}}},
		"summary": {"type": "string"},
		"role": {"type": "string", "enum": ROLES}}}}}}

SYSTEM_B = """You are given, for a Canadian court or tribunal decision, the propositions found in each paragraph (paragraph number, holder, kind, point). Using ONLY these, return:
- overview: three sentences at most saying what the case is about, who the parties are and how it came out.
- background_paras and disposition_paras: paragraph ranges as text (for example "1-5, 14-18"; empty when none).
- The propositions of dissenting reasons, when there are any, are listed after a line "=== DISSENT (not the Court's) ===". The overview, positions, court_conclusion, conclusion_paras and paras of every block come from the majority and concurring propositions ONLY. Never use a dissent paragraph in paras or conclusion_paras. Put what the dissent said on the same issue in that block's dissent_view (at most 30 words, with its paragraph numbers; empty text when the dissent does not address the issue).
- blocks: one block per issue the decision actually deals with, in order. Each block: issue (the question in plain words), paras (the range where it is dealt with), positions (each side's or earlier decision-maker's position: holder, text of at most 25 words, paras; write 'not stated' as the text when the propositions do not give that side's position), court_conclusion (at most 30 words, 'not stated' if none), conclusion_paras.
Do not invent anything the propositions do not support. When a party's position is stated in the propositions only as an agreement by the court ("agree with the Respondent"), still give that party's position from the matching proposition instead of 'not stated'."""

SCHEMA_B = {"type": "object", "additionalProperties": False, "required": ["overview", "background_paras", "disposition_paras", "blocks"], "properties": {
	"overview": {"type": "string"}, "background_paras": {"type": "string"}, "disposition_paras": {"type": "string"},
	"blocks": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["issue", "paras", "positions", "court_conclusion", "conclusion_paras", "dissent_view"], "properties": {
		"issue": {"type": "string"}, "dissent_view": {"type": "string"}, "paras": {"type": "string"}, "court_conclusion": {"type": "string"}, "conclusion_paras": {"type": "string"},
		"positions": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["holder", "text", "paras"], "properties": {
			"holder": {"type": "string", "enum": HOLDERS}, "text": {"type": "string"}, "paras": {"type": "string"}}}}}}}}}


def _paras_of(text: str) -> list[int]:
	out: list[int] = []
	for a, b in re.findall(r"(\d+)(?:\s*[-–]\s*(\d+))?", text or ""):
		lo, hi = int(a), int(b) if b else int(a)
		if hi - lo < 400:
			out.extend(range(lo, hi + 1))
	return out


def _ranges(nums: list[int]) -> str:
	out, i = [], 0
	nums = sorted(set(nums))
	while i < len(nums):
		j = i
		while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
			j += 1
		out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
		i = j + 1
	return ", ".join(out)


def keep_dissent_out(blocks: dict, parts: list[dict]) -> dict:
	"""Code check after the blocks call: dissent paragraphs never stay in a block's paras or conclusion_paras, and a court
	conclusion left with no majority or concurring paragraph is replaced by 'not stated' (the dissent's view is in dissent_view)."""
	dissent = {n for p in parts if p["kind"] == "dissenting" for n in range(p["start"], p["end"] + 1)}
	if not dissent:
		return blocks
	for b in blocks["blocks"]:
		had = _paras_of(b["conclusion_paras"])
		b["paras"] = _ranges([n for n in _paras_of(b["paras"]) if n not in dissent])
		b["conclusion_paras"] = _ranges([n for n in had if n not in dissent])
		for pos in b["positions"]:
			pos["paras"] = _ranges([n for n in _paras_of(pos["paras"]) if n not in dissent])
		if had and not b["conclusion_paras"]:
			b["court_conclusion"] = "not stated (only the dissent reaches this issue)"
	return blocks


def render(ch, pre, parts=None):
	lines = []
	last_part = None
	for p in ch:
		part = part_of(parts or [], p["paragraph_index"])
		if parts and part != last_part:
			# the chunk crosses into (or starts inside) a concurrence or dissent: say so once
			lines.append(f"[Opinion part: {part} reasons from here]")
			last_part = part
		if p.get("heading_before"):
			lines.append(f"[Section heading: {p['heading_before']}]")
		lines.append(f"[{p['paragraph_index']}] {p['text']}")
	return pre + "\n\n".join(lines)


def run_case(client, ledger, run, model, case_id, report, send, stop_file):
	paras = resplit([{"paragraph_index": p["paragraph_index"], "text": clean(p["text"])} for p in load_paragraphs(report) if p["paragraph_index"] != 0])
	head = header(case_id).replace("tribunal_below", "earlier_decision_maker")
	parts_info = opinion_parts("\n".join(str(p.get("text", "")) for p in report.get("paragraphs", [])))
	parts_line = describe(parts_info)
	pre = (head + "\n\n") if head else ""
	if parts_line:
		pre += parts_line + "\n\n"
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	chunks = [paras[i:i + CHUNK] for i in range(0, len(paras), CHUNK)]
	mk = lambda ch: [{"role": "system", "content": SYSTEM_P}, {"role": "user", "content": render(ch, pre, parts_info["parts"])}]  # noqa: E731
	if not send:
		tin = sum(est(mk(c)) for c in chunks) + 3000
		tout = 220 * len(paras) + 1500
		if REUSE_PROPS and (REUSE_PROPS / f"case_{case_id}_prop_{PROMPT_VERSION}_{model}.json").exists():
			tin, tout = 40000, 2000  # blocks call only
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "paragraphs": len(paras), "calls": len(chunks) + 1, "est_input_tokens": tin, "est_usd_max": round(cost_usd(model, tin, tout), 4)}))
		return None

	def stop():
		if stop_file is not None and stop_file.exists():
			print(json.dumps({"stopped": "stop file found", "case_id": case_id}), flush=True)
			raise SystemExit(3)

	usd, rows, dropped = 0.0, {}, 0
	why = {"duplicate": 0, "not_in_chunk": 0}

	def ask(ch):
		nonlocal usd, dropped
		stop()
		msgs = mk(ch)
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="propositions", schema=SCHEMA_P, max_output_tokens=min(16000, 500 + 420 * len(ch)), est_input_tokens=est(msgs), label=f"prop case {case_id}")
		usd += u["usd"]
		want = {p["paragraph_index"] for p in ch}
		for r in data["paragraphs"]:
			if r["para"] in want and r["para"] not in rows:
				rows[r["para"]] = r
			else:
				dropped += 1
				why["duplicate" if r["para"] in rows else "not_in_chunk"] += 1

	stored = REUSE_PROPS / f"case_{case_id}_prop_{PROMPT_VERSION}_{model}.json" if REUSE_PROPS else None
	if stored is not None and stored.exists():
		for r in json.loads(stored.read_text(encoding="utf-8"))["paragraphs"]:
			rows[r["para"]] = {k: r[k] for k in ("para", "propositions", "summary", "role")}
	else:
		for ch in chunks:
			ask(ch)
	retried = sorted({p["paragraph_index"] for p in paras} - set(rows))
	if retried:
		ask([p for p in paras if p["paragraph_index"] in set(retried)])
	missing = sorted({p["paragraph_index"] for p in paras} - set(rows))
	ordered = [rows[k] for k in sorted(rows)]
	for r in ordered:
		r["part"] = part_of(parts_info["parts"], r["para"])  # majority / concurring / dissenting, from the text's own markers
	row = lambda r: [f"{r['para']}\t{pp['holder']}/{pp['kind']}\t{pp['text']}" for pp in r["propositions"]]  # noqa: E731
	listing_lines = [ln for r in ordered if r["part"] != "dissenting" for ln in row(r)]
	dissent_lines = [ln for r in ordered if r["part"] == "dissenting" for ln in row(r)]
	if dissent_lines:
		listing_lines += ["", "=== DISSENT (not the Court's) ==="] + dissent_lines
	listing = "\n".join(listing_lines)
	msgs = [{"role": "system", "content": SYSTEM_B}, {"role": "user", "content": pre + listing}]
	stop()
	blocks, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="blocks", schema=SCHEMA_B, max_output_tokens=4000, est_input_tokens=est(msgs), label=f"blocks case {case_id}")
	usd += u["usd"]
	blocks = keep_dissent_out(blocks, parts_info["parts"])
	hold = {}
	for r in ordered:
		for pp in r["propositions"]:
			hold[pp["holder"]] = hold.get(pp["holder"], 0) + 1
	check = {"paragraphs": len(paras), "rows": len(ordered), "paragraphs_missing": missing, "retried": len(retried), "dropped_rows": dropped, "dropped_why": why, "propositions": sum(len(r["propositions"]) for r in ordered), "holders": hold,
		"empty_proposition_rows": sum(1 for r in ordered if not r["propositions"]), "blocks": len(blocks["blocks"]), "split_paragraphs": sum(1 for p in paras if "split_from" in p), "headings_before": sum(1 for p in paras if "heading_before" in p)}
	return {"usd": usd, "paragraphs": ordered, "blocks": blocks, "verification": check, "opinion_parts": parts_info, "headings": {p["paragraph_index"]: p["heading_before"] for p in paras if "heading_before" in p}, "split_from": {p["paragraph_index"]: p["split_from"] for p in paras if "split_from" in p}}


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
	ap.add_argument("--reuse-props", type=Path, default=None)
	args = ap.parse_args()
	global REUSE_PROPS
	REUSE_PROPS = args.reuse_props
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
		(args.out_dir / f"case_{cid}_prop_{PROMPT_VERSION}_{args.model}.json").write_text(json.dumps({"case_id": cid, "model": args.model, "prompt_version": PROMPT_VERSION, "run": args.run, "usage": {"usd": out["usd"]}, "verification": out["verification"], "opinion_parts": out["opinion_parts"], "headings": out["headings"], "split_from": out["split_from"], "blocks": out["blocks"], "paragraphs": out["paragraphs"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": cid, "model": args.model, "prompt": PROMPT_VERSION, "usd": round(out["usd"], 4), **{k: v for k, v in out["verification"].items() if k != "paragraphs_missing"}, "paragraphs_missing": len(out["verification"]["paragraphs_missing"])}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
