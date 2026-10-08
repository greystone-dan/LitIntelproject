"""Citation-use extraction (proof of concept, report-only, open case law only).

Design (Daniel, 2026-10-08): do not ask a model why a judge cited a case. Identify what the judge is arguing or deciding
(the v5 themes rows: arguments, rebuttals, holdings, left-open issues), find the citations with code, and PAIR each citation
with the nearest such row by paragraph proximity, with no model call (same paragraph first, then the nearest span; ties go to the
court's own voice, then the narrower span, then the earlier row). The nearest three rows are stored as "possible" alternatives.

Model part (optional, narrow, batched; default --link proximity): a label only. For each already-paired citation the model says
who cites it (voice), what it is used for (six labels), a one-line reason and the evidence sentence id. With --link model the
model also picks the linked row from a numbered list (used only to compare against proximity). The script supplies the exact
evidence text, so the model never types a quote and never produces a citation. With --no-model nothing is sent: the output is the
deterministic pairing alone.

Six uses: applied_test, followed_or_agreed, distinguished, not_followed, reported_only, background.

Inputs: the same deterministic reports as extract_themes_v5.py; optionally the v5 themes output for the same case
(--themes-dir) to give the model a short numbered list of arguments to link to.

Dry run by default (no model call, no key needed): prints citation counts, same-paragraph pairings and a worst-case cost. Add --send to call the API (or --send --no-model to write the pairing only).
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


SCHEMA_LABEL = json.loads(json.dumps(SCHEMA_CITE))
_item = SCHEMA_LABEL["properties"]["answers"]["items"]
_item["required"] = [k for k in _item["required"] if k != "argument"]
del _item["properties"]["argument"]

SYSTEM_LABEL = (
	"You read short extracts from one Canadian immigration or refugee court or tribunal decision. Each item gives ONE citation that the script already found, "
	"the sentences around it (each with an id like 17.2) and, when known, the point the Court is arguing or deciding nearby. You never write or change a citation. "
	"For each item answer four things.\n"
	+ SYSTEM_CITE.split("voice:", 1)[1].split("argument:", 1)[0].join(["voice:", ""])
	+ "why: one sentence, 25 words or fewer, in your own words, saying what the citation is used for here.\n"
	"evidence: the id of the single sentence in the extract that best shows the use (it can be the sentence with the citation).\n"
	"confidence: high if the extract plainly shows the use, low if you are guessing. Use only the extract. Return one answer per item, in the same order, using the item number given."
)


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


UNIT_PRIORITY = {"R": 0, "H": 1, "L": 2, "A": 3}  # court's own voice first when a tie


def load_arguments(themes_dirs: list[Path] | None, case_id: int, model: str) -> list[dict]:
	"""What the Court is arguing or deciding: arguments, rebuttals, holdings, left-open issues from the v5 themes output."""
	for path in sorted(p for d in themes_dirs or [] for p in d.glob(f"case_{case_id}_themes_themes_v5_*.json")):
		res = json.loads(path.read_text(encoding="utf-8")).get("result", {})
		units: list[dict] = []
		for prefix, key, field in (("A", "arguments", "claim"), ("R", "rebuttals", "court_answer"), ("H", "holdings", "statement"), ("L", "left_open", "issue")):
			for n, row in enumerate(res.get(key, []), 1):
				paras = row.get("paragraphs", [])
				if paras:
					by = row.get("made_by", "court") if prefix in ("A", "R") else "court"
					units.append({"id": f"{prefix}{n}", "by": by, "claim": row.get(field, ""), "paras": paras, "treatment": row.get("treatment", ""), "span": [min(paras), max(paras)]})
		return units
	return []


def pair_unit(para: int, units: list[dict]) -> list[dict]:
	"""Deterministic pairing: nearest span first (0 = same paragraph); ties go to the Court's voice, then the narrower span, then the earlier row."""
	def key(u):
		lo, hi = u["span"]
		d = 0 if lo <= para <= hi else min(abs(para - lo), abs(para - hi))
		return (d, UNIT_PRIORITY.get(u["id"][0], 9), hi - lo, lo)
	ranked = sorted(units, key=key)
	return [{**u, "distance": key(u)[0]} for u in ranked[:3]]


def arg_list_text(args: list[dict]) -> str:
	if not args:
		return "arguments: (none supplied; answer none for argument)"
	return "arguments:\n" + "\n".join(f"{a['id']} ({a['by']}, para {','.join(str(p) for p in a['paras'][:2])}, court treatment: {a['treatment']}): {a['claim']}" for a in args)


def run_case(client, ledger, run: str, model: str, case_id: int, report: dict, units: list[dict], send: bool, link: str, use_model: bool) -> dict | None:
	paragraphs = load_paragraphs(report)
	table = index_sentences(paragraphs)
	order = list(table)
	items = find_citations(table)
	head = header(case_id)
	est = lambda msgs: int(sum(len(m["content"]) for m in msgs) / 3.2)  # noqa: E731
	# deterministic pairing (no model): nearest argument / rebuttal / holding / open issue by paragraph
	for c in items:
		ranked = pair_unit(c["para"], units)
		c["paired"] = ranked[0]["id"] if ranked else "none"
		c["paired_distance"] = ranked[0]["distance"] if ranked else None
		c["paired_text"] = ranked[0]["claim"] if ranked else ""
		c["possible"] = [{"id": r["id"], "distance": r["distance"]} for r in ranked]
	unit_by_id = {u["id"]: u for u in units}
	system, schema = (SYSTEM_CITE, SCHEMA_CITE) if link == "model" else (SYSTEM_LABEL, SCHEMA_LABEL)
	batches = [items[i:i + BATCH] for i in range(0, len(items), BATCH)]
	messages: list[list[dict]] = []
	for batch in batches:
		parts = []
		for c in batch:
			text, ids = window_text(order, table, c["sentence_id"])
			label = c["mention"] + (f" (name before it: {c['name_hint']})" if c["name_hint"] else "")
			near = f"\nthe point the Court is arguing or deciding nearby: {c['paired_text']}" if link == "proximity" and c["paired_text"] else ""
			parts.append(f"item {c['item']}: {label}\nextract:\n{text}{near}")
		context = arg_list_text(units) + "\n\n" if link == "model" else ""
		messages.append([{"role": "system", "content": system}, {"role": "user", "content": (head + "\n\n" if head else "") + context + "\n\n".join(parts)}])
	if not send or not use_model:
		worst = sum(cost_usd(model, est(m), 1800) for m in messages) if use_model else 0.0
		print(json.dumps({"case_id": case_id, "model": model, "prompt": PROMPT_VERSION, "citations_found": len(items),
			"case_citations": sum(1 for c in items if c["kind"] == "case"), "calls": len(messages) if use_model else 0,
			"units_supplied": len(units), "paired_same_paragraph": sum(1 for c in items if c["paired_distance"] == 0),
			"est_usd_max": round(worst, 4)}))
		if send and not use_model:
			return {"usd": 0.0, "items": items, "arguments": units, "verification": {"citations": len(items), "calls": 0, "units_supplied": len(units)}}
		return None
	usd = 0.0
	answers: dict[int, dict] = {}
	for n, msgs in enumerate(messages, 1):
		data, u = call_json(client, ledger, run=run, model=model, messages=msgs, schema_name="citation_use", schema=schema,
			max_output_tokens=1800, est_input_tokens=est(msgs), label=f"citeuse case {case_id} batch {n}")
		usd += u["usd"]
		for a in data["answers"]:
			answers[a["item"]] = a
	out_items = []
	missing = bad_evidence = bad_arg = agree = 0
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
		extra = {}
		if link == "model":
			arg = a["argument"] if a["argument"] in unit_by_id else "none"
			if a["argument"] not in unit_by_id and a["argument"] not in ("none", ""):
				bad_arg += 1
			agree += arg == c["paired"]
			extra = {"model_link": arg}
		out_items.append({**row, **extra, "answered": True, "voice": a["voice"], "use": a["use"], "why": a["why"],
			"evidence_id": ev, "evidence_text": table[ev]["text"], "confidence": a["confidence"]})
	check = {"citations": len(items), "calls": len(messages), "unanswered": missing, "evidence_id_not_in_window": bad_evidence,
		"units_supplied": len(units), "paired_same_paragraph": sum(1 for c in items if c["paired_distance"] == 0),
		"use_counts": {u: sum(1 for i in out_items if i.get("use") == u) for u in USES},
		"voice_disagrees_with_cue": sum(1 for i in out_items if i.get("answered") and i["cue"] in ("judge", "tribunal_below") and i["voice"] not in (i["cue"], "unclear"))}
	if link == "model":
		check.update({"model_link_invalid": bad_arg, "model_link_agrees_with_proximity": agree})
	return {"usd": usd, "items": out_items, "arguments": units, "verification": check}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", default="gpt-4.1-mini", choices=sorted(PRICES))
	parser.add_argument("--run", required=True)
	parser.add_argument("--cases", required=True)
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True)
	parser.add_argument("--themes-dir", type=Path, action="append", help="Folder with the v5 themes outputs for the same cases (gives the argument list)")
	parser.add_argument("--send", action="store_true", help="Call the API (and write outputs). Without it: dry run, nothing sent.")
	parser.add_argument("--link", choices=["proximity", "model"], default="proximity", help="proximity (default): the pairing is code only. model: the model also picks the linked row, to compare against proximity")
	parser.add_argument("--no-model", action="store_true", help="Pairing only: no model call at all, no key needed, writes the deterministic output")
	parser.add_argument("--reports-dir", type=Path, action="append")
	parser.add_argument("--meta-csv", type=Path, action="append")
	parser.add_argument("--cap-usd", type=float, default=None)
	args = parser.parse_args()
	for meta_path in args.meta_csv or []:
		for row in csv.DictReader(meta_path.open(encoding="utf-8-sig")):
			META[int(float(row["case_id"]))] = row
	report_dirs = args.reports_dir or [REPORTS]
	ledger = SpendLedger(args.ledger, args.cap_usd) if args.cap_usd else SpendLedger(args.ledger)
	client = make_client() if (args.send and not args.no_model) else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	for case_id in [int(x) for x in args.cases.split(",")]:
		path = next((d / f"case_{case_id}_deterministic.json" for d in report_dirs if (d / f"case_{case_id}_deterministic.json").exists()), None)
		if path is None:
			raise SystemExit(f"no report for case {case_id}")
		report = json.loads(path.read_text(encoding="utf-8"))
		out = run_case(client, ledger, args.run, args.model, case_id, report, load_arguments(args.themes_dir, case_id, args.model), args.send, args.link, not args.no_model)
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
