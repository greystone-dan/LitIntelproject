"""Citation-use extraction (proof of concept, report-only, open case law only).

Deterministic part: find every case citation and statute section in a decision, with its sentence id and a window of
neighbouring sentences. Model part (narrow, batched): for each citation say who cites it, what it is used for (six labels),
which listed argument it answers (or none), a one-line reason, and the evidence sentence id. The script supplies the
exact evidence text, so the model never types a quote and never produces a citation.

Six uses: applied_test, followed_or_agreed, distinguished, not_followed, reported_only, background.

Inputs: the same deterministic reports as extract_themes_v5.py; optionally the v5 themes output for the same case
(--themes-dir) to give the model a short numbered list of arguments to link to.

Dry run by default (no model call, no key needed): prints citation counts and a worst-case cost. Add --send to call the API.
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
from extract_themes_v5 import META, header, index_sentences  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "citeuse_v1"
USES = ["applied_test", "followed_or_agreed", "distinguished", "not_followed", "reported_only", "background"]
VOICES = ["judge", "applicant", "respondent", "tribunal_below", "unclear"]
BATCH = 8
WINDOW_BEFORE = 2
WINDOW_AFTER = 1
MAX_CASE_ITEMS = 32
MAX_STATUTE_ITEMS = 8
MAX_ARGS = 30

COURTS = r"(?:FC|FCA|SCC|CSC|CAF|CF|FCT|CanLII|ONCA|ONSC|BCCA|BCSC|ABCA|ABQB|QCCA|NSCA|SKCA|MBCA|NBCA|SST|RAD|RPD|IAD|SCR)"
NEUTRAL = re.compile(rf"\b(?:19|20)\d{{2}}\s+{COURTS}\s+\d{{1,5}}\b")
REPORTER = re.compile(r"\[(?:19|20)\d{2}\]\s+\d{1,3}\s+(?:S\.C\.R\.|F\.C\.|F\.C\.R\.|Imm\.\s?L\.R\.(?:\s?\(\d\w\w\))?|C\.T\.C\.)\s+\d{1,5}")
STATUTE = re.compile(r"\b(?:sections?|subsections?|paragraphs?|ss?\.)\s+\d{1,3}(?:\.\d+)?(?:\([\w.]+\))*(?:\s+(?:and|or|to)\s+\d{1,3}(?:\([\w.]+\))*)?(?:\s+of\s+(?:the\s+)?[A-Z][\w'’\- ]{2,60}?(?:Act|Regulations|Charter|Rules|Code))\b")
NAMED = re.compile(r"\b[A-Z][\w'’.\-]+(?:\s+[A-Z][\w'’.\-]*){0,3}\s+v\.\s+[A-Z][\w'’().\-]+(?:\s+[A-Za-z'’().\-]+){0,6}?\s*[,(]\s*\[?\(?(?:19|20)\d{2}\]?\)?")
NAME_BEFORE = re.compile(r"((?:[A-Z][\w'’.\-&]*\s+){0,4}(?:v\.|c\.)\s+(?:[A-Z][\w'’().,\-&]*\s*){1,6})$")
PARTY_CUE = re.compile(r"\b(submit|submits|argue|argues|argued|says|contend|contends|relies? on|relied on|counsel|according to the (?:applicant|respondent|minister))\b", re.I)
JUDGE_CUE = re.compile(r"\b(I find|I agree|I disagree|In my view|I am not persuaded|I conclude|the Court (?:finds|agrees|notes|concludes)|I accept|I reject)\b")
BELOW_CUE = re.compile(r"\b(the (?:RAD|RPD|Board|Officer|officer|Member|member|Tribunal|tribunal|Appeal Division|decision-maker) (?:found|stated|noted|concluded|held|relied on|cited|referred to))\b")

SYSTEM_CITE = (
	"You read short extracts from one Canadian immigration or refugee court or tribunal decision. Each item gives ONE citation that the script already found, "
	"the sentences around it (each with an id like 17.2) and, for context, a numbered list of arguments found in the decision. You never write or change a citation. "
	"For each item answer five things.\n"
	"voice: who is citing it. judge = the Court or tribunal speaking in its own voice. applicant or respondent = the sentence reports that party's submission ('the applicant relies on', 'counsel submits'). "
	"tribunal_below = the sentence reports the decision under review. unclear = you cannot tell.\n"
	"use: exactly one of applied_test (cited for the legal test or rule the Court itself applies), followed_or_agreed (cited as support for a point the Court adopts or agrees with), "
	"distinguished (the Court says the case differs on facts or law), not_followed (the Court declines to follow it, departs from it, doubts it or says it is overruled), "
	"reported_only (the Court only reports that a party or the tribunal relied on it, with no endorsement), background (standard of review or general background, no link to a specific argument).\n"
	"argument: the id (like A3) of the listed argument the citation is used to answer or support, or none. Choose none when no listed argument fits; do not force a match.\n"
	"why: one sentence, 25 words or fewer, in your own words, saying what the citation is used for here.\n"
	"evidence: the id of the single sentence in the extract that best shows the use (it can be the sentence with the citation).\n"
	"confidence: high if the extract plainly shows the use, low if you are guessing. Use only the extract. Return one answer per item, in the same order, using the item number given."
)

SCHEMA_CITE = {
	"type": "object", "additionalProperties": False, "required": ["answers"],
	"properties": {"answers": {"type": "array", "items": {
		"type": "object", "additionalProperties": False, "required": ["item", "voice", "use", "argument", "why", "evidence", "confidence"],
		"properties": {
			"item": {"type": "integer"},
			"voice": {"type": "string", "enum": VOICES},
			"use": {"type": "string", "enum": USES},
			"argument": {"type": "string"},
			"why": {"type": "string"},
			"evidence": {"type": "string"},
			"confidence": {"type": "string", "enum": ["high", "low"]},
		}}}},
}


def find_citations(table: dict[str, dict]) -> list[dict]:
	"""Deterministic citation finder over the sentence table."""
	found: list[dict] = []
	seen: set[tuple[str, str]] = set()
	for sid, row in table.items():
		if row["para"] == 0:  # header block (court, neutral citation of this decision)
			continue
		text = row["text"]
		spans: list[tuple[str, str, int]] = []
		for pattern, kind in ((NEUTRAL, "case"), (REPORTER, "case"), (NAMED, "case"), (STATUTE, "statute")):
			for m in pattern.finditer(text):
				spans.append((m.group(0).strip(), kind, m.start()))
		for mention, kind, start in spans:
			key = (sid, re.sub(r"\s+", " ", mention))
			if key in seen:
				continue
			seen.add(key)
			name = ""
			if kind == "case":
				m = NAME_BEFORE.search(text[:start].rstrip(" ,("))
				name = m.group(1).strip() if m else ""
			found.append({"sentence_id": sid, "para": row["para"], "mention": mention, "kind": kind, "name_hint": name})
	cases = [c for c in found if c["kind"] == "case"][:MAX_CASE_ITEMS]
	statutes = [c for c in found if c["kind"] == "statute"][:MAX_STATUTE_ITEMS]
	items = sorted(cases + statutes, key=lambda c: (int(c["sentence_id"].split(".")[0]), int(c["sentence_id"].split(".")[1])))
	for n, c in enumerate(items, 1):
		c["item"] = n
	return items


def cue(text: str) -> str:
	if JUDGE_CUE.search(text):
		return "judge"
	if BELOW_CUE.search(text):
		return "tribunal_below"
	if PARTY_CUE.search(text):
		return "party"
	return ""


def window_text(order: list[str], table: dict[str, dict], sid: str) -> tuple[str, list[str]]:
	i = order.index(sid)
	ids = order[max(0, i - WINDOW_BEFORE): i + 1 + WINDOW_AFTER]
	return "\n".join(f"{x} {table[x]['text']}" for x in ids), ids


def load_arguments(themes_dirs: list[Path] | None, case_id: int, model: str) -> list[dict]:
	for path in sorted(p for d in themes_dirs or [] for p in d.glob(f"case_{case_id}_themes_themes_v5_*.json")):
		data = json.loads(path.read_text(encoding="utf-8"))
		args = data.get("result", {}).get("arguments", [])
		return [{"id": f"A{n}", "by": a.get("made_by", ""), "claim": a.get("claim", ""), "paras": a.get("paragraphs", []), "treatment": a.get("treatment", "")} for n, a in enumerate(args[:MAX_ARGS], 1)]
	return []


def arg_list_text(args: list[dict]) -> str:
	if not args:
		return "arguments: (none supplied; answer none for argument)"
	return "arguments:\n" + "\n".join(f"{a['id']} ({a['by']}, para {','.join(str(p) for p in a['paras'][:2])}, court treatment: {a['treatment']}): {a['claim']}" for a in args)


def run_case(client, ledger, run: str, model: str, case_id: int, report: dict, args_list: list[dict], send: bool) -> dict | None:
	paragraphs = load_paragraphs(report)
	table = index_sentences(paragraphs)
	order = list(table)
	items = find_citations(table)
	head = header(case_id)
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	batches = [items[i:i + BATCH] for i in range(0, len(items), BATCH)]
	messages: list[list[dict]] = []
	for batch in batches:
		parts = []
		for c in batch:
			text, ids = window_text(order, table, c["sentence_id"])
			label = c["mention"] + (f" (name before it: {c['name_hint']})" if c["name_hint"] else "")
			parts.append(f"item {c['item']}: {label}\nextract:\n{text}")
		user = (head + "\n\n" if head else "") + arg_list_text(args_list) + "\n\n" + "\n\n".join(parts)
		messages.append([{"role": "system", "content": SYSTEM_CITE}, {"role": "user", "content": user}])
	if not send:
		worst = sum(cost_usd(model, est(m), 1800) for m in messages)
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "citations_found": len(items),
			"case_citations": sum(1 for c in items if c["kind"] == "case"), "calls": len(messages),
			"arguments_supplied": len(args_list), "est_usd_max": round(worst, 4)}))
		return None
	usd = 0.0
	answers: dict[int, dict] = {}
	for n, msgs in enumerate(messages, 1):
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="citation_use", schema=SCHEMA_CITE,
			max_output_tokens=1800, est_input_tokens=est(msgs), label=f"citeuse case {case_id} batch {n}")
		usd += u["usd"]
		for a in data["answers"]:
			answers[a["item"]] = a
	arg_ids = {a["id"] for a in args_list}
	out_items = []
	missing = bad_evidence = bad_arg = 0
	for c in items:
		a = answers.get(c["item"])
		_, window_ids = window_text(order, table, c["sentence_id"])
		row = {**c, "cue": cue(table[c["sentence_id"]]["text"]), "citing_sentence": table[c["sentence_id"]]["text"]}
		if a is None:
			missing += 1
			out_items.append({**row, "answered": False})
			continue
		ev = a["evidence"] if a["evidence"] in window_ids else ""
		if not ev:
			bad_evidence += 1
			ev = c["sentence_id"]
		arg = a["argument"] if a["argument"] in arg_ids else "none"
		if a["argument"] not in arg_ids and a["argument"] not in ("none", ""):
			bad_arg += 1
		out_items.append({**row, "answered": True, "voice": a["voice"], "use": a["use"], "argument": arg, "why": a["why"],
			"evidence_id": ev, "evidence_text": table[ev]["text"], "confidence": a["confidence"]})
	check = {"citations": len(items), "calls": len(messages), "unanswered": missing, "evidence_id_not_in_window": bad_evidence, "argument_id_invalid": bad_arg,
		"arguments_supplied": len(args_list), "use_counts": {u: sum(1 for i in out_items if i.get("use") == u) for u in USES},
		"voice_disagrees_with_cue": sum(1 for i in out_items if i.get("answered") and i["cue"] in ("judge", "tribunal_below") and i["voice"] not in (i["cue"], "unclear"))}
	return {"usd": usd, "items": out_items, "arguments": args_list, "verification": check}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	parser.add_argument("--run", required=True)
	parser.add_argument("--cases", required=True)
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True)
	parser.add_argument("--themes-dir", type=Path, action="append", help="Folder with the v5 themes outputs for the same cases (gives the argument list)")
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
		out = run_case(client, ledger, args.run, args.model, case_id, report, load_arguments(args.themes_dir, case_id, args.model), args.send)
		if out is None:
			continue
		(args.out_dir / f"case_{case_id}_citeuse_{PROMPT_VERSION}_{args.model}.json").write_text(json.dumps({
			"case_id": case_id, "model": args.model, "prompt_version": PROMPT_VERSION, "run": args.run, "usage": {"usd": out["usd"]},
			"verification": out["verification"], "arguments": out["arguments"], "items": out["items"]}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": case_id, "model": args.model, "prompt": PROMPT_VERSION, "usd": round(out["usd"], 4), **out["verification"]}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
