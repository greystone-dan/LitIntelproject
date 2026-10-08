"""Full-decision themes, arguments, court holdings, rebuttals, authorities and left-open issues (prompt themes_v2; v1 had only themes and arguments), using the deterministic discussion units as a map. Report-only; open case law only.

The model gets the whole decision as numbered paragraphs plus the rule-based unit boundaries, and returns themes and
arguments. Every argument must carry paragraph numbers and a short VERBATIM quote; the script checks each quote against
the paragraph text and marks it verified or not. Dry run by default; --send calls the model.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
for entry in (PROJECT_ROOT, PROJECT_ROOT / "scripts" / "ai_poc"):
	if str(entry) not in sys.path:
		sys.path.insert(0, str(entry))

from common import PRICES, SpendLedger, call_json, cost_usd, make_client  # noqa: E402
from tag_paragraphs import REPORTS, load_paragraphs  # noqa: E402

PROMPT_VERSION = "themes_v2"
SYSTEM = (
	"You read one Canadian immigration or refugee court or tribunal decision and extract what a litigator needs from it. "
	"The decision is given as paragraphs [n]. The units list is a rule-based map of where the decision changes subject; use it as a guide, "
	"not as truth. Use only the decision text; never invent facts, cases or paragraph numbers. The case header says who is the applicant and who is the respondent on this "
	"application; use it. Every item needs 1 to 3 paragraph numbers (the paragraphs that actually say it, never a long range) and a quote of 25 words or fewer "
	"copied exactly, character for character, from one of those paragraphs. Do not stitch two passages together with '...'.\n"
	"Fill each list separately and do not leave out an item because it overlaps another list.\n"
	"themes: 3 to 8 themes the reasons turn on: a short name (2 to 8 words), a one-sentence summary, and the key paragraph numbers.\n"
	"arguments: only what a PARTY (applicant, respondent) or the tribunal below argued or decided, one row per distinct point, in order. "
	"made_by is applicant, respondent or tribunal_below. Never put the judge's own reasoning here. "
	"treatment is what the court did with it: accepted, partly_accepted (accepted in part or accepted but found harmless), rejected, or not_decided "
	"(the court expressly declined to decide it).\n"
	"holdings: what the COURT itself decides and the legal tests and rules it states or applies, one row each: a conclusion on an issue, a test, a safeguard, a "
	"standard of review, or the remedy. kind is one of conclusion, legal_test, standard_of_review, remedy, other. Include each separate point the court makes in order to reach its result.\n"
	"rebuttals: where the court answers a party's point specifically, one row per point: what the point was, how the court answered it, and who made the point.\n"
	"authorities: the main cases or provisions the court relies on, with how it treated each: followed, applied, distinguished, rejected, or mentioned.\n"
	"left_open: issues the court expressly says it does not decide, with the reason.\n"
	"overall: one or two sentences giving the result and the main reason, in plain language."
)
_QP = {"paragraphs": {"type": "array", "items": {"type": "integer"}}, "quote": {"type": "string"}}


def _obj(props: dict) -> dict:
	return {"type": "object", "additionalProperties": False, "required": list(props), "properties": props}


SCHEMA = {
	"type": "object", "additionalProperties": False,
	"required": ["overall", "themes", "arguments", "holdings", "rebuttals", "authorities", "left_open"],
	"properties": {
		"overall": {"type": "string"},
		"themes": {"type": "array", "items": _obj({"name": {"type": "string"}, "summary": {"type": "string"}, "paragraphs": _QP["paragraphs"]})},
		"arguments": {"type": "array", "items": _obj({
			"made_by": {"type": "string", "enum": ["applicant", "respondent", "tribunal_below"]},
			"claim": {"type": "string"},
			"treatment": {"type": "string", "enum": ["accepted", "partly_accepted", "rejected", "not_decided"]},
			"authority": {"type": "string"}, **_QP})},
		"holdings": {"type": "array", "items": _obj({
			"kind": {"type": "string", "enum": ["conclusion", "legal_test", "standard_of_review", "remedy", "other"]},
			"statement": {"type": "string"}, **_QP})},
		"rebuttals": {"type": "array", "items": _obj({
			"point": {"type": "string"}, "made_by": {"type": "string", "enum": ["applicant", "respondent", "tribunal_below"]},
			"court_answer": {"type": "string"}, **_QP})},
		"authorities": {"type": "array", "items": _obj({
			"authority": {"type": "string"},
			"treatment": {"type": "string", "enum": ["followed", "applied", "distinguished", "rejected", "mentioned"]},
			"why": {"type": "string"}, **_QP})},
		"left_open": {"type": "array", "items": _obj({"issue": {"type": "string"}, "reason": {"type": "string"}, **_QP})},
	},
}
ITEM_LISTS = ("arguments", "holdings", "rebuttals", "authorities", "left_open")


def norm(text: str) -> str:
	return re.sub(r"\s+", " ", text.replace("’", "'").replace("“", '"').replace("”", '"')).strip().lower()


def _loose(text: str) -> str:
	"""Compare without quotation marks or end punctuation, which models often change."""
	return re.sub(r"[\"'`]", "", norm(text)).strip(" .,;:")


def _snap(quote: str, nums: list[int], paragraphs: list[dict]) -> str:
	"""No model call: for a quote that is not in the decision, return the real sentence in the cited paragraphs that shares most of its words (at least half), else ''."""
	words = {w for w in re.findall(r"[a-z0-9]+", quote.lower()) if len(w) > 2}
	if len(words) < 3:
		return ""
	best, best_score = "", 0.0
	for p in paragraphs:
		if p["paragraph_index"] not in nums:
			continue
		for sentence in re.split(r"(?<=[.;?!])\s+", p["text"].replace("\n", " ")):
			sw = {w for w in re.findall(r"[a-z0-9]+", sentence.lower()) if len(w) > 2}
			score = len(words & sw) / len(words) if words else 0.0
			if score > best_score:
				best, best_score = sentence.strip(), score
	return best if best_score >= 0.5 else ""


def verify(result: dict, paragraphs: list[dict]) -> dict:
	"""Strict check (exact, in a cited paragraph), loose check (ignores quote marks/end punctuation), and where the quote really is."""
	texts = {p["paragraph_index"]: norm(p["text"]) for p in paragraphs}
	loose = {n: _loose(t) for n, t in texts.items()}
	valid = set(texts)
	counts = {"items": 0, "quote_exact_in_cited": 0, "quote_loose_in_cited": 0, "quote_found_elsewhere": 0, "quote_not_found": 0, "quote_has_ellipsis": 0}
	bad_numbers = 0
	for key in ITEM_LISTS:
		for item in result.get(key, []):
			nums = [n for n in item.get("paragraphs", []) if n in valid]
			bad_numbers += len(item.get("paragraphs", [])) - len(nums)
			quote = norm(item.get("quote", ""))
			lq = _loose(item.get("quote", ""))
			counts["items"] += 1
			if "..." in quote or "\u2026" in quote:
				counts["quote_has_ellipsis"] += 1
			item["quote_verified"] = bool(quote) and any(quote in texts[n] for n in nums)
			item["quote_loose_verified"] = bool(lq) and any(lq in loose[n] for n in nums)
			if not item["quote_loose_verified"] and ("..." in quote or "\u2026" in quote):
				# a quote stitched with "..." counts as loosely verified only if every piece (3+ words) is in one cited paragraph
				pieces = [_loose(x) for x in re.split(r"\.\.\.|\u2026", item.get("quote", "")) if len(x.split()) >= 3]
				item["quote_loose_verified"] = bool(pieces) and any(all(x in loose[n] for x in pieces) for n in nums)
			item["quote_found_in"] = [n for n in sorted(valid) if lq and lq in loose[n]]
			if item["quote_verified"]:
				counts["quote_exact_in_cited"] += 1
			elif item["quote_loose_verified"]:
				counts["quote_loose_in_cited"] += 1
			elif item["quote_found_in"]:
				counts["quote_found_elsewhere"] += 1
			else:
				counts["quote_not_found"] += 1
			if not (item["quote_verified"] or item["quote_loose_verified"] or item["quote_found_in"]):
				fix = _snap(item.get("quote", ""), nums, paragraphs)
				if fix:
					item["quote_snapped"] = fix
					counts["quote_snapped_to_real_sentence"] = counts.get("quote_snapped_to_real_sentence", 0) + 1
	for theme in result.get("themes", []):
		bad_numbers += sum(n not in valid for n in theme.get("paragraphs", []))
	counts["paragraph_numbers_not_in_decision"] = bad_numbers
	counts["rows"] = {k: len(result.get(k, [])) for k in ("themes",) + ITEM_LISTS}
	return counts


# Who is who on the application, so the model does not guess sides (the five review cases).
PARTIES = {
	126: "Espinosa v. Canada (Minister of Citizenship and Immigration). Applicant = Mr Espinosa (the refugee claimant). Respondent = the Minister. Below = the Immigration and Refugee Board.",
	1046: "Canada (Minister of Human Resources Development) v. Gattellaro. Applicant = the Minister. Respondent = Ms Gattellaro (the CPP claimant). Below = a member of the Pension Appeal Board.",
	1147: "Ambroise v. Canada (Citizenship and Immigration). Applicant = Ms Ambroise (the refugee claimant). Respondent = the Minister. Below = the Refugee Appeal Division (RAD), and before it the RPD.",
	1292: "Senadheerage v. Canada (Citizenship and Immigration), 2020 FC 968. Applicant = Mr Senadheerage (the refugee claimant). Respondent = the Minister. Below = the Refugee Appeal Division (RAD).",
	1540: "Canada (Attorney General) v. Angell. Applicant = the Attorney General of Canada (AGC). Respondent = Ms Angell (the CPP claimant, no lawyer). Below = the Appeal Division of the Social Security Tribunal.",
}


META: dict[int, dict] = {}


def generic_header(meta: dict) -> str:
	"""For cases not in PARTIES: the style of cause, and a rule for working out the sides from the text (no hard-coded names)."""
	court = (meta.get("court") or "").strip()
	tribunal = court.upper() in {"RPD", "RAD", "IAD", "ID"} or "refugee" in court.lower()
	text = (
		f"case: {meta.get('title', '')}, {meta.get('citation', '')} ({court}). "
		"The style of cause lists the parties but not who is who; work out the applicant and the respondent from the first paragraphs of the decision, "
		"not from the order of the names and not from who wins. For an appeal, the appellant counts as 'applicant' and the other side as 'respondent'. "
		"The court or tribunal whose decision is under review counts as tribunal_below. "
	)
	if tribunal:
		text += ("This is a decision of the tribunal itself, not a court reviewing another body: the tribunal's own reasoning and findings are the 'court' rows "
			"(holdings, rebuttals), the claimant is the applicant and the Minister is the respondent.")
	return text


def build(report: dict, paragraphs: list[dict], system: str | None = None) -> list[dict]:
	units = [{"unit": u["discussion_unit_id"].split(":")[-1], "from": u["start_paragraph"], "to": u["end_paragraph"]} for u in report.get("discussion_units", [])]
	body = "\n\n".join(f"[{p['paragraph_index']}] {p['text']}" for p in paragraphs)
	cid = report.get("case_id")
	header = f"case: {PARTIES[cid]}\n\n" if cid in PARTIES else (generic_header(META[cid]) + "\n\n" if cid in META else "")
	user = f"{header}units (rule-based, container paragraph positions): {json.dumps(units)}\n\ndecision:\n{body}"
	return [{"role": "system", "content": system or SYSTEM}, {"role": "user", "content": user}]


def coverage(result: dict, paragraphs: list[dict]) -> float:
	"""Share of the decision's paragraphs cited by any non-theme row (a rough completeness signal, not accuracy)."""
	cited = {n for key in ITEM_LISTS for item in result.get(key, []) for n in item.get("paragraphs", [])}
	valid = {p["paragraph_index"] for p in paragraphs}
	return round(len(cited & valid) / len(valid), 3) if valid else 0.0


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--model", required=True, choices=sorted(PRICES))
	parser.add_argument("--run", required=True)
	parser.add_argument("--cases", required=True, help="Comma-separated case ids")
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--ledger", type=Path, required=True)
	parser.add_argument("--send", action="store_true")
	parser.add_argument("--reports-dir", type=Path, action="append", help="Folder(s) with case_<id>_deterministic.json (default: the 300-case run reports)")
	parser.add_argument("--meta-csv", type=Path, action="append", help="CSV(s) with case_id,title,citation,court for the sides header of cases not hard-coded")
	parser.add_argument("--prompt", choices=["v2", "v3", "v4"], default="v2", help="Prompt version (v4 = issue map pass, then v3 extraction)")
	parser.add_argument("--cap-usd", type=float, default=None, help="Stop when the ledger total would pass this (the ledger already holds earlier spend)")
	args = parser.parse_args()
	version = f"themes_{args.prompt}"
	import csv as _csv
	for meta_path in args.meta_csv or []:
		for row in _csv.DictReader(meta_path.open(encoding="utf-8-sig")):
			META[int(float(row["case_id"]))] = row
	report_dirs = args.reports_dir or [REPORTS]
	system, schema = SYSTEM, SCHEMA
	if args.prompt in ("v3", "v4"):
		import themes_prompts_v3 as v3
		system, schema = v3.SYSTEM_V3, v3.SCHEMA_V3
	ledger = SpendLedger(args.ledger, args.cap_usd) if args.cap_usd else SpendLedger(args.ledger)
	client = make_client() if args.send else None
	args.out_dir.mkdir(parents=True, exist_ok=True)
	for case_id in [int(x) for x in args.cases.split(",")]:
		report_path = next((d / f"case_{case_id}_deterministic.json" for d in report_dirs if (d / f"case_{case_id}_deterministic.json").exists()), None)
		if report_path is None:
			raise SystemExit(f"no report for case {case_id} in {[str(d) for d in report_dirs]}")
		report = json.loads(report_path.read_text(encoding="utf-8"))
		paragraphs = load_paragraphs(report)
		out_cap = 12000 if args.model.startswith(("gpt-5", "o4")) else 9000
		issues = None
		usd_a = 0.0
		if args.prompt == "v4":
			msgs_a = build(report, paragraphs, v3.SYSTEM_V4_ISSUES)
			est_a = int(sum(len(m["content"]) for m in msgs_a) / 3.2)
			if args.send:
				issues, usage_a = call_json(client, ledger, run=args.run, model=args.model, messages=msgs_a, schema_name="issue_map",
					schema=v3.SCHEMA_V4_ISSUES, max_output_tokens=2500, est_input_tokens=est_a, label=f"issues case {case_id}")
				usd_a = usage_a["usd"]
				system_b = system + v3.V4_PATCH + v3.V4_EXTRA + "ISSUES: " + json.dumps(issues["issues"])
			else:
				system_b = system + v3.V4_PATCH + v3.V4_EXTRA
			messages = build(report, paragraphs, system_b)
			est_dry = est_a + int(sum(len(m["content"]) for m in messages) / 3.2)
		else:
			messages = build(report, paragraphs, system)
			est_dry = int(sum(len(m["content"]) for m in messages) / 3.2)
		est_in = int(sum(len(m["content"]) for m in messages) / 3.2)
		if not args.send:
			worst = cost_usd(args.model, est_dry, out_cap + (2500 if args.prompt == "v4" else 0))
			print(json.dumps({"case_id": case_id, "model": args.model, "prompt": version, "est_input_tokens": est_dry, "est_usd_max": round(worst, 4)}))
			continue
		data, usage = call_json(client, ledger, run=args.run, model=args.model, messages=messages, schema_name="themes_arguments",
			schema=schema, max_output_tokens=out_cap, est_input_tokens=est_in, label=f"themes case {case_id}")
		check = verify(data, paragraphs)
		check["paragraph_coverage"] = coverage(data, paragraphs)
		total_usd = usage["usd"] + usd_a
		(args.out_dir / f"case_{case_id}_themes_{version}_{args.model}.json").write_text(json.dumps({
			"case_id": case_id, "model": args.model, "prompt_version": version, "run": args.run, "usage": {**usage, "usd": total_usd},
			"issue_map": issues, "verification": check, "result": data}, indent=1), encoding="utf-8")
		print(json.dumps({"case_id": case_id, "model": args.model, "prompt": version, "usd": round(total_usd, 4), **check}), flush=True)
	print(json.dumps({"spent_total_usd": round(ledger.total(), 4)}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
