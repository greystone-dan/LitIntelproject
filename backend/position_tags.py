"""Whose-position tags for the reader (preview).

Each paragraph of a decision can carry a tag for whose position it reports (applicant, respondent, earlier
decision maker, the Court's own finding, prior authority, witness or document) and a one-line summary.

Two sources, one response shape, so the screens never care which one answered:

* stored decisions: read from ``data/position_preview/case_<id>.json`` (built offline from the propositions
  run by ``scripts/build_position_preview.py``). A later database table only needs a new source class with
  the same ``paragraphs_for`` method; the route and the screens stay as they are.
* Live Analysis documents: fixed cue-phrase rules over the text, in memory, nothing stored.

No model is called when a page loads. Every paragraph carries an empty ``citations`` list: the reserved place
where citation use will attach later.
"""

from __future__ import annotations

import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Protocol

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "position_preview"
LAYERS_DIR = Path(__file__).resolve().parents[1] / "data" / "position_layers"  # rules output: level per paragraph
LEARNED_DIR = Path(os.environ.get("ILIT_POSITION_LEARNED_DIR") or Path(__file__).resolve().parents[1] / "data" / "position_learned")  # rules + learned tagger output (holder only)
LEARNED_FLAG = "ILIT_LEARNED_POSITIONS"  # "1" lets a decision with no stored preview read LEARNED_DIR; default off

# key -> label shown on the tag. The keys match the stored holder names.
POSITION_LABELS: dict[str, str] = {
	"applicant": "Applicant",
	"respondent": "Respondent",
	"earlier_decision_maker": "Earlier decision-maker",
	"court": "The judge",
	"prior_court_or_authority": "Earlier case or law",
	"witness_or_document": "Witness or document",
	"other": "Other",
}

# One plain sentence per tag, for the legend. Written for a reader who has never seen a decision laid out this way.
POSITION_HELP: dict[str, str] = {
	"applicant": "The person who brought the case (or appealed). Their side of the argument.",
	"respondent": "The other side, usually the Minister or the government. Their side of the argument.",
	"earlier_decision_maker": "The officer, board or tribunal whose decision is being reviewed.",
	"court": "The judge writing this decision: facts found, reasoning and the ruling.",
	"prior_court_or_authority": "A past court decision or rule of law that the paragraph leans on.",
	"witness_or_document": "What a witness said or a document or report shows.",
	"other": "Not clearly any one voice.",
}

# Nesting. A judicial review is nested: the judge (level 0) evaluates whether an earlier decision maker's decision
# (level 1) was reasonable, and that decision itself reports what two other parties argued (level 2). ``depth`` drives
# the indent. Holder labels alone cannot say which level an applicant or respondent paragraph sits at, so those stay
# "not yet detected" until a layer is supplied (stored rows may carry an explicit ``layer``; rules may set one later).
LAYERS: dict[str, dict[str, Any]] = {
	"judge": {"label": "Judge\u2019s evaluation", "depth": 0, "detected": True},
	"jr_party": {"label": "Argument to the Court", "depth": 1, "detected": True},
	"earlier_decision": {"label": "Earlier decision", "depth": 1, "detected": True},
	"first_instance": {"label": "Position reported in the earlier decision", "depth": 2, "detected": True},
	"framework": {"label": "Law and tests", "depth": 1, "detected": True},
	"source": {"label": "Authority or document", "depth": 1, "detected": True},
	"unknown": {"label": "Level not yet detected", "depth": None, "detected": False},
}
_LAYER_BY_HOLDER = {
	"court": "judge",
	"earlier_decision_maker": "earlier_decision",
	"prior_court_or_authority": "source",
	"witness_or_document": "source",
}

LEGEND_NOTE = (
	"A judicial review is nested. The judge (first level) decides whether an earlier decision maker\u2019s decision was "
	"reasonable. That earlier decision (second level) itself reports what two other parties argued (third level, "
	"indented furthest). Where the level of a paragraph is not known yet, it says so."
)

FRAMEWORK_LABEL = "Law and tests"
FRAMEWORK_NOTE = (
	"Law and tests marks passages that comment on other decisions or on the law itself (what a case stands for, how a "
	"test works). It sits beside the tag in grey and is not linked to the cited cases yet."
)

KIND_LABELS: dict[str, str] = {
	"fact": "Fact",
	"finding": "Finding",
	"rule_of_law": "Legal rule",
	"allegation_or_argument": "Argument",
	"conclusion_or_order": "Conclusion or order",
	"issue": "Issue",
	"procedure": "Procedure",
}

RELIABILITY_STORED = (
	"How reliable are these tags? They were read ahead of time by an AI model and have not been checked by a lawyer. "
	"In our checks, about 8 in 10 tags named the right voice. Summaries can miss nuance, and a paragraph that mixes "
	"voices may carry two tags. Read the paragraph itself before relying on a tag."
)
RELIABILITY_RULES = (
	"How reliable are these tags? They come from fixed cue phrases such as “the applicant submits”, with no AI. "
	"A tag shows only that the phrase appears, not that the paragraph is entirely that voice, and paragraphs "
	"without a cue phrase are left untagged. Not checked by a lawyer."
)
EMPTY_NOTE = (
	"Not tagged yet. “Whose position” shows who is speaking in each paragraph (the judge, each side, the earlier "
	"decision-maker). It is prepared ahead of time for a growing set of decisions ({count} so far) and is never "
	"worked out when you open a page. This decision is not in that set yet."
)
EMPTY_NOTE_RULES = (
	"No clear cue phrases found. For pasted documents the tags come from fixed phrases such as “the applicant "
	"submits” or “I am not persuaded”. This text has none, so nothing is tagged."
)

RELIABILITY_LEARNED = (
	"How reliable are these tags? They were worked out ahead of time by fixed cue phrases plus a small statistical "
	"model trained on labelled decisions, with no summary. Against a second reader they named the same voice for "
	"about 3 paragraphs in 4, and about 5 in 6 when the judge, authorities and documents are counted as one group. "
	"Not checked by a lawyer."
)
PREVIEW_NOTICE_LEARNED = (
	"Preview. Machine-generated from the decision text and not yet checked by a lawyer. Some tags will be wrong, "
	"so check the paragraph itself before relying on one."
)

PREVIEW_NOTICE_STORED = (
	"Preview. Machine-generated from the decision text and not yet checked by a lawyer. "
	"Some tags will be wrong, so check the paragraph itself before relying on one."
)
PREVIEW_NOTICE_RULES = (
	"Rule-based preview. Tags come from fixed cue phrases in the text (for example “the applicant submits”), "
	"with no AI and nothing stored. Paragraphs without a clear cue are left untagged. Not checked by a lawyer."
)


class PositionSource(Protocol):
	def paragraphs_for(self, case_id: int) -> dict[str, dict[str, Any]] | None:
		"""Paragraph number (as text) -> tag row, or ``None`` when this source has nothing for the decision."""


def _layer(holder: str, explicit: str | None) -> dict[str, Any]:
	key = explicit if explicit in LAYERS else _LAYER_BY_HOLDER.get(holder, "unknown")
	return {"key": key, **LAYERS[key]}


def _row(
	holders: list[str],
	summary: str,
	kinds: list[str],
	role: str | None,
	cue: str | None = None,
	layer: str | None = None,
	framework: str = "unknown",
) -> dict[str, Any]:
	keys = [h for h in holders if h in POSITION_LABELS] or ["other"]
	return {
		"positions": [{"key": k, "label": POSITION_LABELS[k]} for k in keys],
		"layer": _layer(keys[0], layer),
		"framework": framework,  # "yes", "no", or "unknown" when the data cannot tell
		"summary": summary,
		"kinds": [KIND_LABELS.get(k, k.replace("_", " ").capitalize()) for k in kinds],
		"role": role,
		"cue": cue,
		"citations": [],  # reserved: citation use attaches here later
	}


_RULE_LAYER = {1: "judge", 2: "jr_party", 3: "earlier_decision", 4: "first_instance", 5: "source", 6: "framework"}


def _rule_layers(directory: Path, case_id: int) -> dict[str, dict[str, Any]] | None:
	"""Per-paragraph level from the rules export. Rows decided only by default are left out: the level is not detected."""
	path = directory / f"case_{int(case_id)}.json"
	try:
		stored = json.loads(path.read_text(encoding="utf-8"))
	except (OSError, ValueError):
		return None
	return {n: r for n, r in stored.get("paragraphs", {}).items() if r.get("c") != "default" and r.get("l") in _RULE_LAYER}


def _framework(kinds: list[str], role: str | None) -> str:
	"""Stored labels say it directly: a legal-rule statement, or a paragraph whose role is "law"."""
	return "yes" if role == "law" or (kinds and kinds[0] == "rule_of_law") else "no"


class FilePositionSource:
	"""Compact per-decision files built from the propositions run."""

	def __init__(self, directory: Path = DATA_DIR, layers_directory: Path | None = LAYERS_DIR, learned_directory: Path = LEARNED_DIR) -> None:
		self.directory = directory
		self.layers_directory = layers_directory
		self.learned_directory = learned_directory

	def kind_for(self, case_id: int) -> str:
		"""``stored`` (propositions run) or ``learned`` (rules + learned tagger, only when the flag is on)."""
		if (self.directory / f"case_{int(case_id)}.json").is_file():
			return "stored"
		return "learned" if self._learned_path(case_id) else "stored"

	def _learned_path(self, case_id: int) -> Path | None:
		if os.environ.get(LEARNED_FLAG) != "1":
			return None
		path = self.learned_directory / f"case_{int(case_id)}.json"
		return path if path.is_file() else None

	def _learned_rows(self, path: Path) -> dict[str, dict[str, Any]] | None:
		try:
			stored = json.loads(path.read_text(encoding="utf-8"))
		except (OSError, ValueError):
			return None
		return {n: _row([r["h"]], "", [], r.get("r")) for n, r in stored.get("paragraphs", {}).items()} or None

	def paragraphs_for(self, case_id: int) -> dict[str, dict[str, Any]] | None:
		path = self.directory / f"case_{int(case_id)}.json"
		if not path.is_file():
			learned = self._learned_path(case_id)
			return self._learned_rows(learned) if learned else None
		try:
			stored = json.loads(path.read_text(encoding="utf-8"))
		except (OSError, ValueError):
			return None
		rules = _rule_layers(self.layers_directory, case_id) if self.layers_directory else None
		out = {}
		for number, row in stored.get("paragraphs", {}).items():
			rule = rules.get(number) if rules is not None else None
			framework = _framework(row.get("k", []), row.get("r"))
			if rule and rule.get("law"):
				framework = "yes"
			# With a rules export for this decision, a paragraph it only defaulted stays "not detected".
			layer = row.get("l") or (_RULE_LAYER[rule["l"]] if rule else ("unknown" if rules is not None else None))
			out[number] = _row(row.get("h", []), row.get("s", ""), row.get("k", []), row.get("r"), layer=layer, framework=framework)
		return out or None


_SOURCE: PositionSource = FilePositionSource()


def get_position_source() -> PositionSource:
	return _SOURCE


_DECIDED = re.compile(r"\b(dismiss|allows?|allowed|sets? aside|quash|remit|refus|denies|deny)", re.I)


def _lead(row: dict[str, Any]) -> str:
	return row["positions"][0]["key"]


def _first(rows: dict[str, dict[str, Any]], key: str) -> tuple[str, dict[str, Any]] | None:
	"""First paragraph (document order) where ``key`` is the lead voice and the paragraph argues something."""
	ordered = sorted(rows.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 10**9)
	for number, row in ordered:
		if _lead(row) == key and row["summary"] and any(k in ("Argument", "Issue") for k in row["kinds"]):
			return number, row
	return None


def stored_overview(rows: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
	"""One line per side from the stored summaries: what each side argued and what the judge decided.

	Chosen by fixed rules (the first argument paragraph of each side; the last ruling that dismisses, allows,
	sets aside or refuses), so the same data always gives the same lines. A side with no argument tagged is
	simply left out rather than guessed.
	"""
	out: list[dict[str, Any]] = []
	for key, label in (("applicant", "Applicant argued"), ("respondent", "Respondent argued")):
		hit = _first(rows, key)
		if hit:
			out.append({"key": key, "label": label, "para": hit[0], "text": hit[1]["summary"]})
	ordered = sorted(rows.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else -1, reverse=True)
	for number, row in ordered:
		if _lead(row) == "court" and "Conclusion or order" in row["kinds"] and _DECIDED.search(row["summary"]):
			out.append({"key": "court", "label": "The judge decided", "para": number, "text": row["summary"]})
			break
	return out


def _common(mode: str) -> dict[str, Any]:
	return {
		"mode": mode,
		"preview": True,
		"reliability": RELIABILITY_STORED if mode == "stored" else RELIABILITY_RULES,
		"legend_items": [{"key": k, "label": POSITION_LABELS[k], "help": POSITION_HELP[k]} for k in POSITION_LABELS],
		"framework_label": FRAMEWORK_LABEL,
	}


def case_positions(case_id: int, source: PositionSource | None = None) -> dict[str, Any]:
	"""The response for one stored decision."""
	source = source or _SOURCE
	rows = source.paragraphs_for(case_id)
	learned = rows is not None and getattr(source, "kind_for", lambda _c: "stored")(case_id) == "learned"
	return {
		**_common("stored"),
		**({"reliability": RELIABILITY_LEARNED, "source": "learned"} if learned else {}),
		"case_id": case_id,
		"available": rows is not None,
		"overview": stored_overview(rows) if rows else [],
		"empty_note": EMPTY_NOTE.format(count=len(stored_case_ids())),
		"notice": PREVIEW_NOTICE_LEARNED if learned else PREVIEW_NOTICE_STORED,
		"legend": LEGEND_NOTE,
		"framework_note": FRAMEWORK_NOTE,
		"layers": LAYERS,
		"paragraphs": rows or {},
	}


# ---------------------------------------------------------------- rules-only version (Live Analysis)

_VERBS_EN = (
	r"submits?|submitted|argues?|argued|contends?|contended|asserts?|asserted|alleges?|alleged|claims?|claimed|"
	r"maintains?|maintained|says|said|states?|stated|relies|relied|takes the position|position is|"
	r"further submits?|also submits?|points? out|acknowledges?|concedes?|admits?|agrees?"
)
_PARTY = {
	"applicant": r"(?:applicants?|appellants?|plaintiffs?|claimants?|moving party|petitioners?)",
	"respondent": r"(?:respondents?|ministers?|defendants?|crown|attorney general|minister’s counsel|minister's counsel)",
}
_DECIDERS = (
	r"(?:officer|visa officer|immigration officer|board|rpd|rad|iad|tribunal|member|panel|decision[- ]maker|"
	r"delegate|immigration division|adjudicator|judge|commissioner)"
)

# (key, compiled pattern). Order does not matter; the earliest match in the paragraph sorts first.
_RULES: list[tuple[str, re.Pattern[str]]] = [
	(
		"applicant",
		re.compile(
			rf"\b(?:the\s+)?{_PARTY['applicant']}(?:[’']s\s+(?:counsel|position|submissions?|argument))?\s+(?:also\s+|further\s+|now\s+)?(?:{_VERBS_EN})\b"
			rf"|\bcounsel\s+for\s+the\s+{_PARTY['applicant']}\b|\baccording\s+to\s+the\s+{_PARTY['applicant']}\b"
			rf"|\bthe\s+{_PARTY['applicant']}[’']s\s+(?:position|submissions?|argument|case)\b"
			r"|\ble\s+demandeur\s+(?:soutient|prétend|affirme|allègue|fait\s+valoir|invoque)|\bla\s+demanderesse\s+(?:soutient|prétend|affirme|allègue|fait\s+valoir|invoque)",
			re.I,
		),
	),
	(
		"respondent",
		re.compile(
			rf"\b(?:the\s+)?{_PARTY['respondent']}(?:[’']s\s+(?:counsel|position|submissions?|argument))?\s+(?:also\s+|further\s+|now\s+)?(?:{_VERBS_EN})\b"
			rf"|\bcounsel\s+for\s+the\s+{_PARTY['respondent']}\b|\baccording\s+to\s+the\s+{_PARTY['respondent']}\b"
			rf"|\bthe\s+{_PARTY['respondent']}[’']s\s+(?:position|submissions?|argument|case)\b"
			r"|\ble\s+(?:défendeur|ministre)\s+(?:soutient|prétend|affirme|allègue|fait\s+valoir|invoque)",
			re.I,
		),
	),
	(
		"earlier_decision_maker",
		re.compile(
			rf"\b(?:the\s+)?{_DECIDERS}\s+(?:also\s+|then\s+|further\s+|therefore\s+)?(?:found|concluded|determined|held|noted|stated|rejected|"
			r"was\s+(?:not\s+)?satisfied|accepted|reasoned|considered|decided|refused|gave\s+(?:little|no)\s+weight|"
			r"did\s+not\s+(?:believe|accept)|drew\s+a\s+negative|said)\b"
			r"|\bthe\s+decision\s+under\s+review\b|\bthe\s+impugned\s+decision\b"
			r"|\b(?:la\s+SPR|la\s+SAR|l[’']agent|le\s+commissaire|la\s+section)\s+a\s+(?:conclu|estimé|jugé|déterminé|statué|noté|rejeté)",
			re.I,
		),
	),
	(
		"court",
		re.compile(
			r"\bI\s+(?:am\s+(?:not\s+)?(?:persuaded|satisfied|convinced)|find|conclude|agree|disagree|accept|reject|would|do\s+not\s+accept|"
			r"am\s+of\s+the\s+(?:view|opinion)|cannot\s+accept|see\s+no)\b"
			r"|\b[Ii]n\s+my\s+(?:view|opinion|respectful\s+view)\b|\bthis\s+Court\s+(?:finds?|concludes?|held|has\s+held|agrees?)\b"
			r"|\bthe\s+Court\s+(?:finds?|concludes?|is\s+(?:not\s+)?satisfied|agrees?|accepts?|rejects?)\b"
			r"|\bthe\s+(?:application|appeal)(?:\s+for\s+judicial\s+review)?\s+(?:is|will\s+be)\s+(?:allowed|dismissed|granted)\b"
			r"|\bno\s+question\s+(?:is|will\s+be)\s+certified\b"
			r"|\bje\s+(?:suis\s+d[’']avis|conclus|ne\s+suis\s+pas\s+convaincu|rejette)|\bà\s+mon\s+avis\b",
			re.I,
		),
	),
	(
		"prior_court_or_authority",
		re.compile(
			r"\b(?:the\s+)?(?:Supreme\s+Court(?:\s+of\s+Canada)?|Federal\s+Court\s+of\s+Appeal|Court\s+of\s+Appeal|SCC|FCA)\s+"
			r"(?:has\s+)?(?:held|stated|explained|confirmed|observed|noted|found|concluded|said|wrote|recognized)\b"
			r"|\b(?:In|in|See|see)\s+[A-Z][\w’'.\-]+(?:\s+[A-Za-z’'.\-]+){0,6}\s+v\.\s+[A-Z][^,.;]{2,60},?\s+(?:\[?\d{4}\]?|\d{4}\s+(?:SCC|FCA|FC)|\d+\s+[A-Z]+)"
			r"|\bVavilov\b.{0,60}\b(?:held|stated|explained|confirmed)\b"
			r"|\bla\s+Cour\s+suprême\s+a\s+(?:conclu|statué|affirmé|expliqué)",
			re.I,
		),
	),
	(
		"witness_or_document",
		re.compile(
			r"\b(?:testified|testimony|affidavit|declaration|in\s+(?:his|her|their)\s+(?:narrative|BOC|statement|evidence)|"
			r"stated\s+in\s+(?:his|her|their)|country\s+(?:condition|documentation)|documentary\s+evidence\s+(?:states|indicates|shows)|"
			r"the\s+(?:report|document|letter)\s+(?:states|indicates|says|notes))\b"
			r"|\ba\s+témoigné\b|\bselon\s+(?:l[’']affidavit|le\s+témoignage)",
			re.I,
		),
	),
]

_MAX_CUE = 70


def rules_positions(text: str, blocks: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
	"""Fixed-rule tags for the numbered paragraphs of a document. Untagged paragraphs are simply absent.

	Each tagged paragraph names the phrase that triggered it (``cue``) so the reader can show why. There is no
	summary in this version: a one-line summary needs a model, which a pasted document never gets.
	"""
	out: dict[str, dict[str, Any]] = {}
	for block in blocks:
		if block.get("type") != "para" or block.get("num") is None:
			continue
		segment = text[block["start"] : block["end"]]
		hits: list[tuple[int, str, str]] = []
		for key, pattern in _RULES:
			match = pattern.search(segment)
			if match:
				hits.append((match.start(), key, " ".join(match.group(0).split())[:_MAX_CUE]))
		if not hits:
			continue
		hits.sort()
		out[str(block["num"])] = _row([key for _, key, _ in hits[:2]], "", [], None, cue=hits[0][2])
	return out


def live_positions(text: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
	"""The response block that rides in the Live Analysis reader payload."""
	rows = rules_positions(text, blocks)
	overview = []
	for key, label in (("applicant", "Applicant argued"), ("respondent", "Respondent argued"), ("court", "The judge wrote")):
		hit = next(((n, r) for n, r in sorted(rows.items(), key=lambda kv: int(kv[0])) if _lead(r) == key), None)
		if hit:
			overview.append({"key": key, "label": label, "para": hit[0], "text": "First cue: \u201c" + (hit[1]["cue"] or "") + "\u201d"})
	return {
		**_common("rules"),
		"available": bool(rows),
		"overview": overview,
		"empty_note": EMPTY_NOTE_RULES,
		"notice": PREVIEW_NOTICE_RULES,
		"legend": LEGEND_NOTE,
		"framework_note": FRAMEWORK_NOTE,
		"layers": LAYERS,
		"paragraphs": rows,
	}


@lru_cache(maxsize=1)
def stored_case_ids() -> frozenset[int]:
	"""Decisions the stored source covers (for tests and a quick coverage check)."""
	return frozenset(int(p.stem.split("_")[1]) for p in DATA_DIR.glob("case_*.json"))
