"""Themes, arguments, holdings and left-open issues, built for a small model (gpt-4.1-mini). Report-only; open case law only.

Differences from extract_themes.py (v2 to v4), each aimed at a failure seen with mini:
- Evidence by sentence id. The decision is shown one sentence per line with an id such as 17.2 (paragraph 17, sentence 2). The model returns ids; the script
  supplies the exact sentence text as the quote and derives the paragraph numbers. A quote can no longer be paraphrased or mis-numbered.
- One small schema: a single list of rows (kind, by, text, result, note, evidence) instead of seven lists.
- Issue map first (one call), then one short call per issue with only that issue's paragraphs, so the model has less to hold at once and
  every part of the decision is read in turn.
- One batched repair call per case for rows whose evidence ids are missing or invalid.
- Two short invented worked examples in the system prompt.
Output files use the same field names as v2 to v4 (arguments, holdings, rebuttals, authorities, left_open, themes, quote, paragraphs) so the earlier scoring tools work.
Dry run by default; --send calls the model.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
for entry in (PROJECT_ROOT, PROJECT_ROOT / "scripts" / "ai_poc"):
	if str(entry) not in sys.path:
		sys.path.insert(0, str(entry))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "themes_v5c"  # v5b + rebuttal / left_open rules with an "answers" link to the party sentence
META: dict[int, dict] = {}
CHUNK_TRIGGER = 14  # an issue range longer than this many paragraphs is split (v5 used 25)
CHUNK = 10  # paragraphs per call when split (v5 used 20)
GAP_MIN_RUN = 3  # an uncovered run of at least this many paragraphs gets a second look
GAP_MAX_RUNS = 4  # per case, to keep cost bounded
LEFT_OPEN_CUES = re.compile(r"\b(need not|does not need to|do not need to|need not decide|will not (?:consider|decide|assess|address)|declin\w+ to (?:decide|consider|rule|address)|without deciding|not necessary to decide|unnecessary to decide|leaves? (?:open|for)|is not (?:necessary|required) to)\b", re.I)

PARTIES = {
	126: "Espinosa v. Canada (Minister of Citizenship and Immigration). Applicant = Mr Espinosa (the refugee claimant). Respondent = the Minister. Below = the Immigration and Refugee Board.",
	1046: "Canada (Minister of Human Resources Development) v. Gattellaro. Applicant = the Minister. Respondent = Ms Gattellaro (the CPP claimant). Below = a member of the Pension Appeal Board.",
	1147: "Ambroise v. Canada (Citizenship and Immigration). Applicant = Ms Ambroise (the refugee claimant). Respondent = the Minister. Below = the Refugee Appeal Division (RAD), and before it the RPD.",
	1292: "Senadheerage v. Canada (Citizenship and Immigration), 2020 FC 968. Applicant = Mr Senadheerage (the refugee claimant). Respondent = the Minister. Below = the Refugee Appeal Division (RAD).",
	1540: "Canada (Attorney General) v. Angell. Applicant = the Attorney General of Canada (AGC). Respondent = Ms Angell (the CPP claimant, no lawyer). Below = the Appeal Division of the Social Security Tribunal.",
}


def header(case_id: int) -> str:
	if case_id in PARTIES:
		return f"case: {PARTIES[case_id]}"
	meta = META.get(case_id)
	if not meta:
		return ""
	court = (meta.get("court") or "").strip()
	tribunal = court.upper() in {"RPD", "RAD", "IAD", "ID"} or "refugee" in court.lower()
	text = (
		f"case: {meta.get('title', '')}, {meta.get('citation', '')} ({court}). "
		"The style of cause lists the parties but not who is who; work out the applicant and the respondent from the first paragraphs, not from the order of the names and not from who wins. "
		"For an appeal, the appellant counts as 'applicant' and the other side as 'respondent'. The court or tribunal whose decision is under review counts as tribunal_below. "
	)
	if tribunal:
		text += "This is a decision of the tribunal itself: the tribunal's own reasoning is the 'court' rows, the claimant is the applicant and the Minister is the respondent."
	return text


# ---------- sentences ----------
ABBREV = {"v", "s", "ss", "para", "paras", "no", "nos", "inc", "ltd", "c", "doc", "fc", "fca", "scc", "scr", "fct", "fcj", "nr", "cf", "re", "ex", "st", "mr", "mrs", "ms", "dr", "hon", "j", "ja", "cj", "sub", "subs", "reg", "art", "ch", "vol", "at", "p", "pp", "etc", "al", "cr", "cs", "d", "r", "a", "b"}
_SPLIT = re.compile(r"(?<=[.?!])([\"”')\]]*)\s+(?=[A-Z\"“(\[‘])")


def split_sentences(text: str) -> list[str]:
	text = re.sub(r"\s+", " ", text).strip()
	if not text:
		return []
	pieces: list[str] = []
	last = 0
	for match in _SPLIT.finditer(text):
		cut = match.start() + len(match.group(1))
		pieces.append(text[last:cut].strip())
		last = match.end()
	pieces.append(text[last:].strip())
	merged: list[str] = []
	for piece in pieces:
		if merged:
			prev = merged[-1]
			tail = re.findall(r"([A-Za-z]+)\.[\"”')\]]*$", prev)
			ends_abbrev = bool(tail) and (tail[-1].lower() in ABBREV or (len(tail[-1]) == 1 and tail[-1].isupper()))
			digits = bool(re.search(r"\b\d+\.$", prev)) and len(prev.split()) <= 2
			if ends_abbrev or digits or len(prev.split()) < 3:
				merged[-1] = prev + " " + piece
				continue
		merged.append(piece)
	out: list[str] = []
	for sentence in merged:  # very long block: also cut at semicolons so one id is not a whole page
		if len(sentence.split()) > 90 and ";" in sentence:
			parts = [x.strip() for x in re.split(r"(?<=;)\s+", sentence) if x.strip()]
			buf = ""
			for part in parts:
				if buf and len((buf + " " + part).split()) > 60:
					out.append(buf)
					buf = part
				else:
					buf = (buf + " " + part).strip()
			if buf:
				out.append(buf)
		else:
			out.append(sentence)
	return out


def index_sentences(paragraphs: list[dict]) -> dict[str, dict]:
	"""id like '17.2' -> {para, text}. The leading '[n]' markers in the stored text are dropped."""
	table: dict[str, dict] = {}
	for p in paragraphs:
		n = p["paragraph_index"]
		text = re.sub(r"^(\s*\[\d{1,3}\]\s*)+", "", p["text"].replace("\n", " "))
		for i, sentence in enumerate(split_sentences(text), 1):
			table[f"{n}.{i}"] = {"para": n, "text": sentence}
	return table


def render(table: dict[str, dict], paras: set[int] | None = None) -> str:
	lines: list[str] = []
	last = None
	for sid, row in table.items():
		if paras is not None and row["para"] not in paras:
			continue
		if last is not None and row["para"] != last:
			lines.append("")
		lines.append(f"{sid} {row['text']}")
		last = row["para"]
	return "\n".join(lines)


# ---------- prompts and schemas ----------
EXAMPLE = (
	"EXAMPLES (invented, to show the row types; never copy them).\n"
	"Text:\n3.1 The applicant says the officer ignored his brother's letter.\n3.2 He also says nobody told him about the officer's concerns.\n\n"
	"4.1 I disagree about the letter.\n4.2 It is two lines long and repeats what the applicant said in his own affidavit.\n\n"
	"5.1 I agree the officer should have raised the concerns.\n5.2 However, the applicant answered them fully in his later submissions, so the error did not matter.\n\n"
	"6.1 I need not decide whether the officer used the wrong version of the Guidelines.\n6.2 The result would be the same.\n"
	"Rows: "
	"{kind party_argument, by applicant, text 'The officer ignored his brother's letter', result rejected, evidence [3.1]}; "
	"{kind rebuttal, by court, text 'The letter was short and repeated his affidavit', result none, evidence [4.2], answers '3.1'}; "
	"{kind party_argument, by applicant, text 'He was not told about the officer's concerns', result partly_accepted, note 'right that they should have been raised, but harmless', evidence [3.2]}; "
	"{kind court_holding, by court, text 'The failure to raise the concerns did not matter because he answered them later', result none, evidence [5.2]}; "
	"{kind left_open, by court, text 'Whether the wrong version of the Guidelines was used', result not_decided, note 'the result would be the same', evidence [6.1, 6.2]}.\n"
)

SPEAKER = (
	"WHO IS SPEAKING. 'the applicant says / argues / submits', 'counsel submits', 'the respondent relies on' report a party: kind party_argument, by that party. "
	"'The Board / RAD / RPD / Appeal Division found' reports the decision below: kind finding_below, by tribunal_below. "
	"The judge's own voice ('I am not persuaded', 'In my view', 'I agree', 'I find', 'the Court', 'this application is dismissed') is the Court: kind court_holding, legal_test, standard_of_review, rebuttal, authority, left_open or remedy, by court. "
	"A holding is something the Court itself says; never record the Court's reasoning as a party's argument. Sides come from the case header, not from who wins: the header says who the applicant is, so use it exactly, even when the applicant is the Minister or the Attorney General (their arguments are then by applicant, and the other party's are by respondent). "
	"If the Court says 'I agree with X that ... but ...', record X's argument with result partly_accepted and say what part in note.\n"
)

SYSTEM_MAP = (
	"You read one Canadian immigration or refugee decision, shown as numbered paragraphs. Use only the text. "
	"1) List every issue the decision itself deals with, in the order it deals with them, including the standard of review, any preliminary or procedural point, any issue it expressly declines to decide or assumes without deciding, and the remedy or costs. "
	"For each: a short label; first_paragraph and last_paragraph (the paragraph numbers where the decision starts and finishes dealing with it); disposition = allowed, dismissed, partly_allowed, found_harmless, not_decided, assumed_without_deciding or other. "
	"Do not add issues the decision does not discuss. "
	"2) themes: 3 to 6 themes the reasons turn on, each a short name (2 to 8 words), a one-sentence summary and the paragraph numbers where it is discussed (at most 4). "
	"3) overall: one or two sentences giving the result and the main reason in plain language."
)
SCHEMA_MAP = {
	"type": "object", "additionalProperties": False, "required": ["issues", "themes", "overall"],
	"properties": {
		"overall": {"type": "string"},
		"issues": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["label", "first_paragraph", "last_paragraph", "disposition"], "properties": {
			"label": {"type": "string"}, "first_paragraph": {"type": "integer"}, "last_paragraph": {"type": "integer"},
			"disposition": {"type": "string", "enum": ["allowed", "dismissed", "partly_allowed", "found_harmless", "not_decided", "assumed_without_deciding", "other"]}}}},
		"themes": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["name", "summary", "paragraphs"], "properties": {
			"name": {"type": "string"}, "summary": {"type": "string"}, "paragraphs": {"type": "array", "items": {"type": "integer"}}}}},
	},
}

KINDS = ["party_argument", "finding_below", "court_holding", "legal_test", "standard_of_review", "rebuttal", "authority", "left_open", "remedy", "party_gap", "background_fact"]
SYSTEM_ISSUE = (
	"You extract what a litigator needs from ONE part of a Canadian immigration or refugee decision. The part is shown one sentence per line, each with an id such as 17.2 "
	"(paragraph 17, sentence 2). Use only these sentences; never invent facts, cases or ids.\n"
	+ SPEAKER +
	"Return rows. Each row has: kind (" + ", ".join(KINDS) + "); by (applicant, respondent, tribunal_below, intervener, court); text (one plain-language sentence in your own words); "
	"result (for a party_argument or finding_below: what the Court did with it: accepted, partly_accepted, rejected or not_decided; otherwise none); "
	"note (one short sentence, only for partly_accepted, not_decided or left_open: what part or why; else an empty string); "
	"evidence (1 or 2 sentence ids from the text below that say it, copied exactly; the text is shown to the reader as the quote).\n"
	"Row types: party_argument = one distinct point a party makes. finding_below = a distinct finding of the decision below. court_holding = a conclusion the Court reaches on an issue. "
	"legal_test = a rule, test or framework the Court states or applies, or a limit the Court puts on its own role. standard_of_review. "
	"rebuttal = the Court answering one specific party point (one row per point). authority = a case or provision the Court relies on; text says how it is treated (followed, applied, distinguished, rejected) and why. "
	"left_open = an issue the Court does not decide or assumes without deciding. remedy = the order, costs, certified question. "
	"party_gap = something a party failed to do or file that the Court relies on. background_fact = a fact about the claimant that the Court treats as important to the result.\n"
	"REBUTTAL vs COURT_HOLDING. Use rebuttal (not court_holding) for every sentence where the Court responds to something a party or the decision below said: 'I disagree', 'I am not persuaded', 'I cannot accept', 'does not assist', 'without merit', 'the Minister has not persuaded me', 'fails because'. "
	"For a rebuttal, set answers to the id of the sentence in this text where that party point is made (a party_argument row's evidence id), or an empty string if the point is not in this text. For all other rows answers is an empty string. "
	"Use court_holding only for the Court's own final answer on an issue, with no party point being answered. "
	"LEFT_OPEN. Use left_open (not court_holding) whenever the Court says it does not decide, need not decide, does not have to decide, assumes without deciding, declines to consider, or leaves something for the decision-maker or another day; put the reason in note.\n"
	"Give one row for each separate point, reason or step; do not merge them. Include every row type that the text contains, and no row the text does not support. "
	"If the part states a rule and then applies it to several findings, give one legal_test row and one row for each application.\n"
	+ EXAMPLE
)
SCHEMA_ROWS = {
	"type": "object", "additionalProperties": False, "required": ["rows"],
	"properties": {"rows": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["kind", "by", "text", "result", "note", "evidence", "answers"], "properties": {
		"kind": {"type": "string", "enum": KINDS},
		"by": {"type": "string", "enum": ["applicant", "respondent", "tribunal_below", "intervener", "court"]},
		"text": {"type": "string"},
		"result": {"type": "string", "enum": ["accepted", "partly_accepted", "rejected", "not_decided", "none"]},
		"note": {"type": "string"},
		"evidence": {"type": "array", "items": {"type": "string"}},
		"answers": {"type": "string"}}}}},
}
SYSTEM_REPAIR = (
	"Some rows from an extraction have no valid evidence ids. For each row, choose 1 or 2 sentence ids from the candidate sentences that best support the row's text. "
	"If no candidate supports it, return an empty list for that row. Use only ids that appear in the candidates."
)
SCHEMA_REPAIR = {
	"type": "object", "additionalProperties": False, "required": ["fixes"],
	"properties": {"fixes": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["row", "evidence"], "properties": {
		"row": {"type": "integer"}, "evidence": {"type": "array", "items": {"type": "string"}}}}}},
}


def partition(issues: list[dict], paragraph_numbers: list[int]) -> list[dict]:
	"""Turn the issue map into ranges that cover every paragraph, in order (no gaps); the first range starts at the first paragraph."""
	if not paragraph_numbers:
		return []
	lo, hi = min(paragraph_numbers), max(paragraph_numbers)
	valid = sorted({i["first_paragraph"] for i in issues if lo <= i["first_paragraph"] <= hi})
	ordered = sorted((i for i in issues if lo <= i["first_paragraph"] <= hi), key=lambda i: (i["first_paragraph"], i["last_paragraph"]))
	if not ordered:
		return [{"label": "whole decision", "disposition": "other", "start": lo, "end": hi}]
	ranges = []
	starts = [lo if k == 0 else issue["first_paragraph"] for k, issue in enumerate(ordered)]
	for k, issue in enumerate(ordered):
		end = (starts[k + 1] - 1) if k + 1 < len(ordered) else hi
		if end < starts[k]:
			end = starts[k]
		ranges.append({"label": issue["label"], "disposition": issue["disposition"], "start": starts[k], "end": max(end, starts[k])})
	# a long range is split so one call does not carry a whole long analysis
	out = []
	for r in ranges:
		span = [n for n in paragraph_numbers if r["start"] <= n <= r["end"]]
		if len(span) > CHUNK_TRIGGER:
			for j in range(0, len(span), CHUNK):
				chunk = span[j:j + CHUNK]
				out.append({**r, "start": chunk[0], "end": chunk[-1]})
		else:
			out.append(r)
	return out


def build_result(map_result: dict, rows: list[dict], table: dict[str, dict]) -> dict[str, Any]:
	"""Convert rows into the v2 to v4 list layout, with the exact sentence text as the quote."""
	result: dict[str, Any] = {"overall": map_result.get("overall", ""), "themes": map_result.get("themes", []), "issue_map": map_result.get("issues", []),
		"arguments": [], "holdings": [], "rebuttals": [], "authorities": [], "left_open": [], "rows_without_evidence": []}
	for row in rows:
		ids = [e for e in row.get("evidence", []) if e in table]
		if not ids:
			result["rows_without_evidence"].append(row)
			continue
		paras = sorted({table[e]["para"] for e in ids})
		quote = " ".join(table[e]["text"] for e in ids)
		common = {"quote": quote, "paragraphs": paras, "evidence_ids": ids, "quote_verified": True, "quote_loose_verified": True, "quote_found_in": paras}
		kind, by = row["kind"], row["by"]
		if kind in ("court_holding", "legal_test") and by == "court" and LEFT_OPEN_CUES.search(row["text"]):
			row = {**row, "relabelled_from": kind}
			kind = "left_open"
		if kind in ("party_argument", "finding_below"):
			result["arguments"].append({**common, "made_by": by if by != "court" else "tribunal_below", "claim": row["text"], "treatment": row["result"] if row["result"] != "none" else "accepted",
				"outcome_note": row["note"], "kind": kind})
		elif kind == "rebuttal":
			ans = row.get("answers", "")
			result["rebuttals"].append({**common, "point": "", "made_by": by, "court_answer": row["text"],
				"answers_evidence_id": ans if ans in table else "", "answers_paragraph": table[ans]["para"] if ans in table else None})
		elif kind == "authority":
			result["authorities"].append({**common, "authority": row["text"], "treatment": "", "why": row["note"]})
		elif kind == "left_open":
			result["left_open"].append({**common, "issue": row["text"], "reason": row["note"]})
		else:
			hk = {"court_holding": "conclusion", "legal_test": "legal_test", "standard_of_review": "standard_of_review", "remedy": "remedy", "party_gap": "party_gap", "background_fact": "background_fact"}[kind]
			result["holdings"].append({**common, "kind": hk, "statement": row["text"]})
	return result


def run_case(client, ledger, run: str, model: str, case_id: int, report: dict, send: bool) -> dict | None:
	paragraphs = load_paragraphs(report)
	table = index_sentences(paragraphs)
	numbers = [p["paragraph_index"] for p in paragraphs]
	head = header(case_id)
	full_text = "\n\n".join(f"[{p['paragraph_index']}] " + re.sub(r"^(\s*\[\d{1,3}\]\s*)+", "", p["text"].replace("\n", " ")) for p in paragraphs)
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	map_msgs = [{"role": "system", "content": SYSTEM_MAP}, {"role": "user", "content": (head + "\n\n" if head else "") + "decision:\n" + full_text}]
	if not send:
		n_issues = max(6, -(-len(numbers) // 9) + 2)
		est_in = est(map_msgs) + est([{"role": "system", "content": SYSTEM_ISSUE}] * n_issues) + int(len(full_text) / 3.2) * 1.1
		worst = cost_usd(model, int(est_in), 2500 + n_issues * 3000)
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "sentences": len(table), "est_input_tokens": int(est_in), "est_usd_max": round(worst, 4)}))
		return None
	usd = 0.0
	map_result, u = call_json(client, ledger, run=run, model=model, messages=map_msgs, schema_name="issue_map", schema=SCHEMA_MAP, max_output_tokens=2500, est_input_tokens=est(map_msgs), label=f"map case {case_id}")
	usd += u["usd"]
	ranges = partition(map_result["issues"], numbers)
	labels = "; ".join(r["label"] for r in ranges)
	rows: list[dict] = []
	for r in ranges:
		paras = {n for n in numbers if r["start"] <= n <= r["end"]}
		body = render(table, paras)
		if not body:
			continue
		user = (head + "\n\n" if head else "") + f"All parts of the decision, for context: {labels}\nThis part: {r['label']} (disposition: {r['disposition']}; paragraphs {r['start']} to {r['end']}).\n\ntext:\n{body}"
		msgs = [{"role": "system", "content": SYSTEM_ISSUE}, {"role": "user", "content": user}]
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="rows", schema=SCHEMA_ROWS, max_output_tokens=3000, est_input_tokens=est(msgs), label=f"issue case {case_id} {r['start']}-{r['end']}")
		usd += u["usd"]
		for row in data["rows"]:
			row["_range"] = [r["start"], r["end"]]
			rows.append(row)
	covered = {table[e]["para"] for row in rows for e in row.get("evidence", []) if e in table}
	runs, cur = [], []
	for n in [x for x in numbers if x != 0]:
		if n in covered:
			if len(cur) >= GAP_MIN_RUN:
				runs.append(cur)
			cur = []
		else:
			cur.append(n)
	if len(cur) >= GAP_MIN_RUN:
		runs.append(cur)
	gap_calls = 0
	for run_paras in runs[:GAP_MAX_RUNS]:
		run_paras = run_paras[:CHUNK]
		body = render(table, set(run_paras))
		user = (head + "\n\n" if head else "") + f"All parts of the decision, for context: {labels}\nThis part: paragraphs {run_paras[0]} to {run_paras[-1]}, which the first pass produced no rows for. Check whether any argument, finding, holding, test or other row type is stated here; if the paragraphs only describe background with nothing a litigator needs, return no rows.\n\ntext:\n{body}"
		msgs = [{"role": "system", "content": SYSTEM_ISSUE}, {"role": "user", "content": user}]
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="rows", schema=SCHEMA_ROWS, max_output_tokens=2000, est_input_tokens=est(msgs), label=f"gap case {case_id} {run_paras[0]}-{run_paras[-1]}")
		usd += u["usd"]
		gap_calls += 1
		for row in data["rows"]:
			row["_range"] = [run_paras[0], run_paras[-1]]
			row["_gap_pass"] = True
			rows.append(row)
	bad = [(i, row) for i, row in enumerate(rows) if not [e for e in row.get("evidence", []) if e in table]]
	repaired = 0
	if bad:
		cand = {}
		for i, row in bad:
			lo, hi = row["_range"]
			cand[i] = render(table, {n for n in numbers if lo <= n <= hi})
		listing = "\n\n".join(f"row {i}: {row['text']}\ncandidates:\n{cand[i]}" for i, row in bad[:12])
		msgs = [{"role": "system", "content": SYSTEM_REPAIR}, {"role": "user", "content": listing}]
		fixes, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="repair", schema=SCHEMA_REPAIR, max_output_tokens=1500, est_input_tokens=est(msgs), label=f"repair case {case_id}")
		usd += u["usd"]
		for fx in fixes["fixes"]:
			if 0 <= fx["row"] < len(rows) and [e for e in fx["evidence"] if e in table]:
				rows[fx["row"]]["evidence"] = fx["evidence"]
				repaired += 1
	result = build_result(map_result, rows, table)
	cited = {p for key in ("arguments", "holdings", "rebuttals", "authorities", "left_open") for item in result[key] for p in item["paragraphs"]}
	check = {"items": sum(len(result[k]) for k in ("arguments", "holdings", "rebuttals", "authorities", "left_open")),
		"quote_exact_in_cited": sum(len(result[k]) for k in ("arguments", "holdings", "rebuttals", "authorities", "left_open")),
		"quote_loose_in_cited": 0, "quote_found_elsewhere": 0, "quote_not_found": 0, "quote_has_ellipsis": 0, "paragraph_numbers_not_in_decision": 0,
		"rows_without_evidence_after_repair": len(result["rows_without_evidence"]), "evidence_repaired": repaired, "issues": len(ranges), "calls": 1 + len(ranges) + gap_calls + (1 if bad else 0), "gap_pass_calls": gap_calls,
		"paragraph_coverage": round(len(cited & set(numbers)) / len(numbers), 3) if numbers else 0.0,
		"rows": {k: len(result[k]) for k in ("themes", "arguments", "holdings", "rebuttals", "authorities", "left_open")}}
	return {"usd": usd, "result": result, "verification": check}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	parser.add_argument("--run", required=True)
	parser.add_argument("--cases", required=True)
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True)
	parser.add_argument("--send", action="store_true")
	parser.add_argument("--reports-dir", type=Path, action="append")
	parser.add_argument("--meta-csv", type=Path, action="append")
	parser.add_argument("--cap-usd", type=float, default=None)
	args = parser.parse_args()
	for meta_path in args.meta_csv or []:
		for row in csv.DictReader(meta_path.open(encoding="utf-8-sig")):
			META[int(float(row["case_id"]))] = row
	report_dirs = args.reports_dir or [REPORTS]
	ledger = SpendLedger(args.ledger, args.cap_usd) if args.cap_usd else SpendLedger(args.ledger)
	client = make_client() if args.send else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	for case_id in [int(x) for x in args.cases.split(",")]:
		path = next((d / f"case_{case_id}_deterministic.json" for d in report_dirs if (d / f"case_{case_id}_deterministic.json").exists()), None)
		if path is None:
			raise SystemExit(f"no report for case {case_id}")
		report = json.loads(path.read_text(encoding="utf-8"))
		out = run_case(client, ledger, args.run, args.model, case_id, report, args.send)
		if out is None:
			continue
		(args.out_dir / f"case_{case_id}_themes_{PROMPT_VERSION}_{args.model}.json").write_text(json.dumps({
			"case_id": case_id, "model": args.model, "prompt_version": PROMPT_VERSION, "run": args.run, "usage": {"usd": out["usd"]},
			"verification": out["verification"], "result": out["result"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": case_id, "model": args.model, "prompt": PROMPT_VERSION, "usd": round(out["usd"], 4), **out["verification"]}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
