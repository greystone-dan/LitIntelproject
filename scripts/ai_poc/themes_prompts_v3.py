"""Prompt versions themes_v3 and themes_v4 for extract_themes.py. Report-only; open case law only.

v3 = v2 plus the prompt-only recommendations of argument-structure-research.md: a hard "who is speaking" rule, quote written
before the claim, single-paragraph pinpoints, separate partial-outcome fields, a "what the party did not do" field,
explicit holding kinds, and one short worked example that is NOT taken from any of the five test cases (126, 1046, 1147, 1292, 1540).
v4 = v3 plus a first pass that lists the issues the Court itself decides (with disposition), then the v3 extraction told to cover every issue.
Not built: the per-row quote repair call and the quote-supports-claim check (see the research file, recs 5 and 11).
"""

from __future__ import annotations

SPEAKER_RULES = (
	"WHO IS SPEAKING. Decide who is speaking before you classify any row. Text introduced by 'the applicant submits / argues / says', 'counsel submits', "
	"'the respondent relies on', 'the Minister says' or 'the Board / RAD / Appeal Division found' reports someone else's position: it is an argument or the decision below, "
	"never a holding. Text where the judge speaks in their own voice ('I am not persuaded', 'In my view', 'I agree', 'I find', 'the Court finds', 'this application is dismissed') "
	"is a holding or a rebuttal. A holding must be something the Court itself says. If the Court only recites the decision below without endorsing it, record it as an argument with made_by tribunal_below, not a holding. "
	"If the Court adopts a party's position, record the party's argument with treatment accepted AND the Court's adoption as a holding.\n"
	"The case header names the parties. In a judicial review the applicant is whoever brought the application (the Minister or the Attorney General in some cases), the respondent is the other side. "
	"Use the header; do not infer sides from who won. Use intervener only for a named intervener.\n"
)

EXAMPLE = (
	"EXAMPLE (an invented passage, only to show the row types; do not copy it). Passage: [3] The applicant says the officer ignored his brother's letter. [4] I disagree. "
	"The letter is two lines long and repeats what the applicant said in his own affidavit. [5] The applicant also says he was not told about the officer's concerns. I agree the officer should have raised them. "
	"However, the applicant had a full chance to respond in his later submissions, so the error did not matter. [6] I need not decide whether the officer applied the wrong version of the Guidelines, because the result would be the same.\n"
	"Rows: arguments: applicant / 'the officer ignored his brother's letter' / rejected, paragraph 3. "
	"arguments: applicant / 'he was not told about the officer's concerns' / partly_accepted, outcome_note 'right that the officer should have raised them, but harmless', changed_result false, paragraph 5. "
	"rebuttals: point 'ignored the letter' / court_answer 'the letter was short and repeated his affidavit', paragraph 4. "
	"holdings: conclusion / 'any unfairness did not matter because he could respond later', paragraph 5. "
	"left_open: issue 'whether the wrong version of the Guidelines was applied' / reason 'result would be the same', paragraph 6.\n"
)

SYSTEM_V3 = (
	"You read one Canadian immigration or refugee court or tribunal decision and extract what a litigator needs from it. "
	"The decision is given as paragraphs [n]. The units list is a rule-based map of where the decision changes subject; use it as a guide, not as truth. "
	"Use only the decision text; never invent facts, cases or paragraph numbers.\n"
	+ SPEAKER_RULES +
	"EVERY ROW: write the quote FIRST, then the rest. The quote is one continuous sentence or part of a sentence of 25 words or fewer, copied exactly, character for character, "
	"from the paragraph it points to. Never join two passages and never use '...'. paragraphs = the single paragraph where the point is first made, plus at most two more. "
	"If a point spans more than three paragraphs, split it into separate rows, each with its own quote.\n"
	"Fill each list separately and do not leave out an item because it overlaps another list.\n"
	"themes: 3 to 8 themes the reasons turn on: a short name (2 to 8 words), a one-sentence summary, and the key paragraph numbers.\n"
	"arguments: only what a PARTY (applicant, respondent, intervener) or the tribunal below argued or decided, one row per distinct point, in order; never the judge's own reasoning. "
	"For tribunal_below, give one row for each distinct finding the Court recites or relies on, including findings about the claimant's background or experience that the Court treats as important. treatment is what the Court did with it: accepted, partly_accepted (accepted in part, or the Court agrees the party is right on the point but holds it does not change the result: harmless, no prejudice, forward-looking analysis), "
	"rejected, or not_decided (expressly declined). outcome_note = one sentence saying what part was accepted or why it did not matter (empty if plainly accepted or rejected). "
	"changed_result = true only if accepting it changed the outcome. gap = what the party failed to do that the Court relies on (did not raise the point, filed no evidence, made no submissions on a step, did not ask for more time, filed no affidavit), or empty. Also use gap for what the Court says a party did not do in the earlier hearing.\n"
	"holdings: what the COURT itself decides or states: kind conclusion (its answer on an issue), legal_test (a rule or test it states or applies, e.g. a reasonableness test or a framework for corroboration), "
	"standard_of_review, procedural_point (a preliminary or procedural ruling), court_declined_to_decide (an issue it expressly does not decide), remedy (the order, costs, certified question), or other. "
	"reason (a separate reason the Court gives for a conclusion: each 'in my view', 'moreover', 'I note', 'there is no evidence' step). "
	"Also record as holdings: a limit the Court puts on its own role (for example, that it will not reweigh the evidence), and how it resolves a conflict between two lines of case law. "
	"One row for each separate step the Court takes to reach its result. When the Court states a rule and then applies it to several findings or pieces of evidence, "
	"give one holding for the rule and one reason or rebuttal for each application; do not merge them.\n"
	"rebuttals: one row per specific party point the Court answers separately, reason by reason: do not merge them. Give the point, who made it, and how the Court answered.\n"
	"authorities: the main cases or provisions the Court relies on, with how it treated each: followed, applied, distinguished, rejected, or mentioned, and why in one line.\n"
	"left_open: issues the Court expressly says it does not decide or assumes without deciding, with the reason. This includes a ground a party raised that the Court does not reach "
	"because it decides on another ground, a standard of review it says it need not choose, and a question it sends back to the decision-maker.\n"
	"overall: one or two sentences giving the result and the main reason, in plain language.\n"
	+ EXAMPLE
)

_PARA = {"type": "array", "items": {"type": "integer"}}


def _obj(props: dict) -> dict:
	return {"type": "object", "additionalProperties": False, "required": list(props), "properties": props}


_BY = {"type": "string", "enum": ["applicant", "respondent", "tribunal_below", "intervener"]}

SCHEMA_V3 = {
	"type": "object", "additionalProperties": False,
	"required": ["overall", "themes", "arguments", "holdings", "rebuttals", "authorities", "left_open"],
	"properties": {
		"overall": {"type": "string"},
		"themes": {"type": "array", "items": _obj({"name": {"type": "string"}, "summary": {"type": "string"}, "paragraphs": _PARA})},
		"arguments": {"type": "array", "items": _obj({
			"quote": {"type": "string"}, "paragraphs": _PARA, "made_by": _BY, "claim": {"type": "string"},
			"treatment": {"type": "string", "enum": ["accepted", "partly_accepted", "rejected", "not_decided"]},
			"outcome_note": {"type": "string"}, "changed_result": {"type": "boolean"}, "gap": {"type": "string"}, "authority": {"type": "string"}})},
		"holdings": {"type": "array", "items": _obj({
			"quote": {"type": "string"}, "paragraphs": _PARA,
			"kind": {"type": "string", "enum": ["conclusion", "legal_test", "standard_of_review", "procedural_point", "court_declined_to_decide", "reason", "remedy", "other"]},
			"statement": {"type": "string"}})},
		"rebuttals": {"type": "array", "items": _obj({
			"quote": {"type": "string"}, "paragraphs": _PARA, "point": {"type": "string"}, "made_by": _BY, "court_answer": {"type": "string"}})},
		"authorities": {"type": "array", "items": _obj({
			"quote": {"type": "string"}, "paragraphs": _PARA, "authority": {"type": "string"},
			"treatment": {"type": "string", "enum": ["followed", "applied", "distinguished", "rejected", "mentioned"]}, "why": {"type": "string"}})},
		"left_open": {"type": "array", "items": _obj({"quote": {"type": "string"}, "paragraphs": _PARA, "issue": {"type": "string"}, "reason": {"type": "string"}})},
	},
}

# v4 pass A: the issue map. Short, no quotes needed.
SYSTEM_V4_ISSUES = (
	"You read one Canadian immigration or refugee court decision. The decision is given as paragraphs [n]. "
	"List every issue the Court itself deals with, in the order it deals with them, including the standard of review, any preliminary or procedural point, "
	"any issue it expressly declines to decide or assumes without deciding, and the remedy or certified question. For each: a short label; the paragraph(s) where the Court states its conclusion on it "
	"(1 to 3 numbers); and disposition = one of allowed, dismissed, partly_allowed, found_harmless, not_decided, assumed_without_deciding, other. "
	"Do not add issues the Court does not discuss. Do not list a party's argument as an issue unless the Court addresses it separately. Use only the decision text."
)
SCHEMA_V4_ISSUES = {
	"type": "object", "additionalProperties": False, "required": ["issues"],
	"properties": {"issues": {"type": "array", "items": _obj({
		"label": {"type": "string"}, "paragraphs": _PARA,
		"disposition": {"type": "string", "enum": ["allowed", "dismissed", "partly_allowed", "found_harmless", "not_decided", "assumed_without_deciding", "other"]}})}},
}
V4_EXTRA = (
	"ISSUE MAP. A first pass listed the issues the Court itself decides (below, in order). Cover every one of them: each issue must have at least one row in holdings, left_open or rebuttals "
	"(a standard-of-review or remedy issue goes in holdings), and each party argument tied to it must be in arguments. Do not add rows for things the Court does not discuss. "
	"The issue map is a guide, not truth: fix it if the decision shows otherwise.\n"
)
