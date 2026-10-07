"""Outcome and government-role derivation for case metadata.

These helpers inspect the operative tail of a decision (ORDER / JUDGMENT /
DISPOSITION blocks) to label the decision outcome, then combine the caption
parties with that outcome to derive the government role and result. They are
imported by `backend.metadata`; nothing else should depend on them.
"""

from __future__ import annotations

import re

OUTCOME_CLASSIFIER_VERSION = "deterministic_outcome_v2"
_GOVERNMENT_PARTY_RE = re.compile(
	r"\b(?:minister|attorney\s+general|public\s+safety|citizenship\s+and\s+immigration|canada\s+border\s+services\s+agency|\bcbsa\b|\bircc\b|government\s+of\s+canada|\bm\.?c\.?i|\bm\.?p\.?s\.?e\.?p)\b",
	re.IGNORECASE,
)

_OUTCOME_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
	(
		"dismissed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:dismissed|denied|refused)\b",
			re.IGNORECASE,
		),
	),
	(
		"allowed",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*(?:allowed|granted)\b",
			re.IGNORECASE,
		),
	),
	(
		"granted",
		re.compile(
			r"\b(?:application|appeal|judicial\s+review|motion|proceeding|claim|complaint|action)\b[^\n\.]{0,140}\b(?:is|are|be|hereby)?\s*granted\b",
			re.IGNORECASE,
		),
	),
	(
		"set_aside",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:set aside|quashed|annulled|vacated)\b", re.IGNORECASE),
	),
	(
		"remitted",
		re.compile(r"\b(?:is|are|be|hereby)?\s*(?:remitted|referred back|sent back)\b", re.IGNORECASE),
	),
)


_TAIL_CHARS = 12000
_MARKER_RE = re.compile(
	r"\b(?:ORDERS?|JUDGMENT|DISPOSITION|CONCLUSION)\b|^[ \t]*(?:Order|Judgment|Disposition|Conclusion)\b",
	re.MULTILINE,
)
_SUBJECT = (
	r"(?:applications?|appeals?|cross-appeals?|judicial\s+reviews?|petitions?|proceedings?|claims?|complaints?|actions?|"
	r"requests?|motions?|stay|leave(?:\s+to\s+\w+)?)"
)
_DISMISS_WORDS = r"(?:dismissed|denied|refused|rejected)"
_ALLOW_WORDS = r"(?:allowed|granted|upheld)"
_SUBJECT_VERB_RE = re.compile(
	rf"\b(?P<subject>{_SUBJECT})\b(?P<span>[^\n\.;]{{0,140}}?)\b(?P<verb>{_DISMISS_WORDS}|{_ALLOW_WORDS}|withdrawn|discontinued)\b",
	re.IGNORECASE,
)
_ACTOR_VERB_RE = re.compile(
	r"\b(?P<actor>court|tribunal|panel|board|division|RAD|RPD|I\s+would|we\s+would|I\s+hereby|"
	r"(?:I|we)\s+(?:will|shall)|I)(?:,?\s+(?:hereby|therefore|accordingly|now),?)?\s+"
	r"(?P<verb>allows?|dismisses|dismiss|grants?|denies|deny|refuses|refuse|rejects?)\b(?P<object>[^\n\.;]{0,100})",
	re.IGNORECASE,
)
_BARE_VERDICT_RE = re.compile(
	r"^[ \t]*(?:\d+\.[ \t]*)?(?:the[ \t]+)?(?:(?:appeal|application|motion)[ \t]+)?"
	r"(?P<verb>dismissed|allowed|granted|denied)\b[ \t]*\.?[ \t]*$",
	re.IGNORECASE | re.MULTILINE,
)
_CONSEQUENCE_RE = re.compile(
	r"\b(?:set aside|quashed|annulled|vacated|remitted|referred back|sent back)\b", re.IGNORECASE
)
# Headline dispositions printed in the headnote/judgment line, e.g. "Appeal allowed with costs, X J. dissenting."
_HEADLINE_RE = re.compile(
	r"^[ \t]*(?:Cross-)?(?:Appeals?|Applications?|Motions?|Petitions?)[ \t]+(?P<verb>allowed|dismissed|granted|denied)\b"
	r"(?:[ \t]+in[ \t]+part)?[^\n]{0,120}$",
	re.IGNORECASE | re.MULTILINE,
)
# Concluding sentences: "I would dismiss the appeal", "The appeal should therefore be allowed", "we will allow the application".
_CONCLUDING_FIRST_PERSON_RE = re.compile(
	r"\b(?:I|we)\s+(?:would|will|shall|must|propose\s+that\s+we)\s+(?:therefore\s+|accordingly\s+)?"
	r"(?P<verb>dismiss|allow|grant|deny)\b[^\n\.;]{0,60}?\b(?:appeals?|applications?|motions?|petitions?)\b",
	re.IGNORECASE,
)
_CONCLUDING_COMPOUND_RE = re.compile(
	r"\b(?:I|we)\s+(?:would|will|shall)\s+[^\n\.;]{0,60}?\band\s+(?P<verb>dismiss|allow)\s+(?:the\s+|this\s+)?(?:appeals?|applications?)\b",
	re.IGNORECASE,
)
_CONCLUDING_PASSIVE_RE = re.compile(
	r"\b(?:the\s+)?(?:appeals?|applications?|cross-appeals?|petitions?)\b[^\n\.;]{0,60}?"
	r"\b(?:should|must|will|shall)\s+(?:therefore\s+|accordingly\s+|also\s+)?be\s+(?P<verb>dismissed|allowed|granted|denied)\b",
	re.IGNORECASE,
)
# Refugee Protection/Appeal Division reasons end with a finding rather than "dismissed"/"allowed".
_TRIBUNAL_DOC_RE = re.compile(
	r"\b(?:RPD|RAD|SPR|SAR)\s+File\s+No|\bRefugee\s+(?:Protection|Appeal)\s+Division\b|\bSection\s+d[e']\s*(?:la\s+)?(?:protection|appel)",
	re.IGNORECASE,
)
_COURT_HEAD_RE = re.compile(r"\b(?:federal\s+court|cour\s+f[ée]d[ée]rale|supreme\s+court|court\s+of\s+appeal|cour\s+d'appel)\b", re.IGNORECASE)


def _is_tribunal_document(content: str) -> bool:
	"""IRB division reasons (RPD/RAD) as opposed to a court judgment that merely mentions them."""
	if _COURT_HEAD_RE.search(content[:800]):
		return False
	return bool(_TRIBUNAL_DOC_RE.search(content[:3000]))
_TRIBUNAL_FINDING_RE = re.compile(
	r"\b(?:is|are)\s+(?:neither|not)\s+(?:a\s+|an\s+)?[\"'“‘]?Convention\s+refugees?\b"
	r"|\bneither\s+of\s+you\b[^\n.]{0,120}?\bcan\s+be\s+found\s+to\s+be\s+Convention\s+refugees?\b"
	r"|\bcannot\s+be\s+found\s+to\s+be\s+(?:a\s+)?Convention\s+refugees?\b"
	r"|\b(?:is|are)\s+excluded\s+(?:from|under|by)\b|\bis\s+excludable\b|\bexcludable\s+under\b",
	re.IGNORECASE,
)
# Subsequent-history citations such as "..., leave to appeal refused, [2002] S.C.C.A. No. 505" are not dispositions.
_LEAVE_HISTORY_RE = re.compile(
	r"(?<=[;,(])\s*leave\s+to\s+appeal\s+(?:to\s+[^,;)\n]{0,40}\s+)?(?:refused|dismissed|denied|granted)\b",
	re.IGNORECASE,
)
_NEGATION_BEFORE_VERB_RE = re.compile(
	r"(?:\bnot\b|\bneither\b|\bnor\b|n't|\bcannot\b|\bnever\b|\bunless\b|\bif\b|\bwhether\b|\bshould\b|\bwould\b|\bmust\b)"
	r"\s*(?:[\w-]+\s+){0,2}$",
	re.IGNORECASE,
)
# "which had dismissed", "was refused by the officer": a past ruling being described, not the ruling made here.
_NARRATIVE_SPAN_RE = re.compile(r"\b(?:had|has|have|having|was|were|been|which|who|whose|whereby|where|when|because)\b", re.IGNORECASE)
_TRIBUNAL_CONFIRMS_RE = re.compile(r"\b(?:RAD|Appeal\s+Division)\s+(?:therefore\s+)?confirms\s+the\s+(?:decision|determination)\s+of\s+the\s+RPD\b", re.IGNORECASE)
_COMPOUND_ACTOR_RE = re.compile(
	r"\b(?:RAD|RPD|Board|Division|panel|Court)\b[^\n\.;]{0,80}?\band\s+(?P<verb>dismisses|allows)\s+(?:the\s+|this\s+)?appeals?\b", re.IGNORECASE
)
_PAST_FIRST_PERSON_RE = re.compile(
	r"\bI\s+(?P<verb>granted|allowed|dismissed|denied)\s+(?:the\s+|this\s+)?(?:application|judicial\s+review|appeal)\b", re.IGNORECASE
)
# In RAD reasons "the RPD found/determined that the appellants are not Convention refugees" describes the decision under appeal.
_RPD_NARRATIVE_RE = re.compile(r"\bRPD\b[^.\n]{0,100}\b(?:found|determined|concluded|decided|held|stated|said|made)\b|\bRPD'?s\b", re.IGNORECASE)
_CLAIM_ACCEPTED_RE = re.compile(
	r"\bclaims?\b[^\n\.;]{0,60}?\b(?:is|are)\s+accepted\b|\baccepts?\s+(?:his|her|their|the)\s+claims?\b"
	r"|\b(?:is|are)\s+(?:a\s+)?Convention\s+refugees?\s+as\s+defined\b",
	re.IGNORECASE,
)
# "I set the decision aside and refer the matter back" / "the RAD refers this matter to the RPD".
_SET_ASIDE_SPLIT_RE = re.compile(
	r"\bI\s+(?:hereby\s+)?set\s+(?:the|this|that)\s+(?:decision|determination|order|judgment)\s+aside\b"
	r"|\bthe\s+RAD\s+refers\s+(?:this|the)\s+matter\b",
	re.IGNORECASE,
)
_PARTIAL_RE = re.compile(r"\b(?:in\s+part|partly|partially)\b", re.IGNORECASE)
_SIDE_ORDER_RE = re.compile(r"\b(?:leave|stay|extension|motion|request)\b", re.IGNORECASE)
_VERB_LABELS = {
	"allowed": "allowed", "allow": "allowed", "allows": "allowed", "upheld": "allowed",
	"granted": "granted", "grant": "granted", "grants": "granted",
	"dismissed": "dismissed", "dismiss": "dismissed", "dismisses": "dismissed",
	"denied": "dismissed", "deny": "dismissed", "denies": "dismissed",
	"refused": "dismissed", "refuse": "dismissed", "refuses": "dismissed", "rejected": "dismissed",
	"reject": "dismissed", "rejects": "dismissed", "accepted": "allowed",
	"withdrawn": "withdrawn", "discontinued": "withdrawn",
}


def _sentence_bounds(text: str, start: int, end: int) -> tuple[int, int]:
	"""Expand [start, end) to the enclosing sentence/list item."""
	left = max(text.rfind("\n", 0, start), text.rfind(". ", 0, start))
	right_candidates = [i for i in (text.find("\n", end), text.find(". ", end)) if i != -1]
	right = min(right_candidates) + 1 if right_candidates else len(text)
	return left + 1, right


_STATUTE_LINE_RE = re.compile(r"\n\s*\d+\s*\(\d+\)\s+[A-ZÀ-Ý]")


def _disposition_candidates(tail: str, is_tribunal: bool = False) -> list[tuple[int, int, str, re.Match[str], str]]:
	"""Every disposition cue in `tail` as (rank, start, label, match).

	Rank 3 is a ruling on the proceeding itself, 2 is a consequence of it (set
	aside / remitted), 1 is an ancillary ruling (leave, stay, motion) or a
	"would" opinion. Negated or conditional cues are dropped.
	"""
	found: list[tuple[int, int, str, re.Match[str], str]] = []
	for match in _SUBJECT_VERB_RE.finditer(tail):
		prefix = tail[match.start("span") : match.start("verb")]
		if _NEGATION_BEFORE_VERB_RE.search(prefix) or _NARRATIVE_SPAN_RE.search(prefix):
			continue
		label = _VERB_LABELS[match.group("verb").lower()]
		subject = match.group("subject").lower()
		side = subject.startswith(("leave", "stay", "motion", "request"))
		rank = 1 if side and label in {"allowed", "granted"} else 3 if not side or label == "dismissed" else 1
		if subject.startswith(("motion", "request", "stay")) and label == "dismissed":
			rank = 1
		found.append((rank, match.start(), label, match, "subject_verb"))
	rad_text = is_tribunal and bool(re.search(r"\bthe\s+RAD\b", tail))
	for match in _ACTOR_VERB_RE.finditer(tail):
		if rad_text and match.group("actor").lower() in {"panel", "board", "division", "rpd"}:
			continue  # in RAD reasons "the panel" is the RPD being reviewed
		label = _VERB_LABELS[match.group("verb").lower()]
		conditional = match.group("actor").lower().endswith("would")
		rank = 1 if conditional or _SIDE_ORDER_RE.search(match.group("object")) else 3
		found.append((rank, match.start(), label, match, "actor"))
	for match in _HEADLINE_RE.finditer(tail):
		if _STATUTE_LINE_RE.search(tail[match.end() : match.end() + 250]):
			continue  # a heading quoted in appended legislation, e.g. "Appeal allowed / 67 (1) To allow an appeal"
		found.append((4, match.start(), _VERB_LABELS[match.group("verb").lower()], match, "headline"))
	for pattern in (_CONCLUDING_FIRST_PERSON_RE, _CONCLUDING_COMPOUND_RE, _CONCLUDING_PASSIVE_RE):
		for match in pattern.finditer(tail):
			prefix = tail[max(0, match.start() - 40) : match.start()]
			if re.search(r"\b(?:not|if|whether|unless|submits?|argues?|asks?|suggests?)\W*(?:[\w-]+\W+){0,2}$", prefix, re.IGNORECASE):
				continue
			ancillary = pattern is _CONCLUDING_FIRST_PERSON_RE and re.search(r"\bmotions?\b", match.group(0), re.IGNORECASE)
			# "Pronouncing the judgment the lower court should have given, I would dismiss..." follows the real ruling.
			consequence = re.search(r"\b(?:pronouncing|giving|rendering)\s+the\s+(?:judgments?|decisions?)\b[^.\n]{0,120}$", tail[max(0, match.start() - 160) : match.start()], re.IGNORECASE)
			rank = 1 if ancillary else 2 if consequence else 3
			found.append((rank, match.start(), _VERB_LABELS[match.group("verb").lower()], match, "concluding"))
	for match in _TRIBUNAL_FINDING_RE.finditer(tail if is_tribunal else ""):
		if _RPD_NARRATIVE_RE.search(tail[max(0, match.start() - 140) : match.start()]):
			continue
		if not _NEGATION_BEFORE_VERB_RE.search(tail[max(0, match.start() - 25) : match.start()]):
			found.append((3, match.start(), "dismissed", match, "tribunal_finding"))
	for match in _TRIBUNAL_CONFIRMS_RE.finditer(tail if is_tribunal else ""):
		found.append((3, match.start(), "dismissed", match, "tribunal_confirms"))
	for match in _COMPOUND_ACTOR_RE.finditer(tail):
		found.append((3, match.start(), _VERB_LABELS[match.group("verb").lower()], match, "actor"))
	for match in _SET_ASIDE_SPLIT_RE.finditer(tail):
		if not _NEGATION_BEFORE_VERB_RE.search(tail[max(0, match.start() - 25) : match.start()]):
			found.append((3, match.start(), "allowed", match, "actor"))
	for match in _PAST_FIRST_PERSON_RE.finditer(tail):
		found.append((3, match.start(), _VERB_LABELS[match.group("verb").lower()], match, "actor"))
	for match in _CLAIM_ACCEPTED_RE.finditer(tail):
		if not _NEGATION_BEFORE_VERB_RE.search(tail[max(0, match.start() - 20) : match.start()]):
			found.append((3, match.start(), "allowed", match, "claim_accepted"))
	for match in _BARE_VERDICT_RE.finditer(tail):
		found.append((2, match.start(), _VERB_LABELS[match.group("verb").lower()], match, "bare_verdict"))
	for match in _CONSEQUENCE_RE.finditer(tail):
		prefix = tail[max(0, match.start() - 30) : match.start()]
		if _NEGATION_BEFORE_VERB_RE.search(prefix):
			continue
		label = "set_aside" if match.group(0).lower() in {"set aside", "quashed", "annulled", "vacated"} else "remitted"
		found.append((2, match.start(), label, match, "consequence"))
	# "The appeal should be allowed, the application should be dismissed" states one ruling: keep the first.
	kept: list[tuple[int, int, str, re.Match[str], str]] = []
	last_concluding = -10**9
	for item in sorted(found, key=lambda c: c[1]):
		if item[4] in {"subject_verb", "headline", "bare_verdict"} and _STATUTE_LINE_RE.search(tail[item[3].end() : item[3].end() + 250]):
			continue  # a heading quoted in appended legislation
		if item[4] == "concluding" and item[0] >= 3:
			if item[1] - last_concluding < 400 and not re.search(r"\n|\.\s", tail[last_concluding : item[1]]):
				continue
			last_concluding = item[1]
		kept.append(item)
	return kept


def _mask_history(text: str) -> str:
	"""Blank subsequent-history "leave to appeal refused" cues, keeping offsets stable."""
	return _LEAVE_HISTORY_RE.sub(lambda m: " " * len(m.group(0)), text)


_FOOTNOTE_START_RE = re.compile(r"\n\d{1,3}\s+\S")


def _strip_footnotes(content: str) -> str:
	"""Drop the numbered footnotes IRB reasons end with (they quote statutes and case law)."""
	paragraphs = list(re.finditer(r"\n\[\d+\]", content))
	if not paragraphs:
		return content
	foot = _FOOTNOTE_START_RE.search(content, paragraphs[-1].end())
	return content[: foot.start()] if foot else content


def _assess_outcome(content: str):
	"""Score every disposition cue: (best, candidates, operative_start, offset, tail) or None."""
	if not content:
		return None
	if _is_tribunal_document(content):
		content = _strip_footnotes(content)
	offset = max(0, len(content) - _TAIL_CHARS)
	tail = content[offset:]
	is_tribunal = _is_tribunal_document(content)
	candidates = _disposition_candidates(_mask_history(tail), is_tribunal)
	if not any(c[0] >= 3 for c in candidates):
		# Long trailing annexes (statutes, footnotes) can push the ruling out of the tail.
		whole = _disposition_candidates(_mask_history(content), is_tribunal)
		if whole and (not candidates or any(c[0] >= 3 for c in whole)):
			offset, tail, candidates = 0, content, whole
	if not candidates:
		return None
	operative_start = 0
	for marker in _MARKER_RE.finditer(tail):
		if any(c[1] >= marker.start() for c in candidates):
			operative_start = marker.start()
	best = max(candidates, key=lambda item: (item[1] >= operative_start, item[0], item[1]))
	return best, candidates, operative_start, offset, tail


def _best_outcome(content: str) -> tuple[str, re.Match[str], int, str] | None:
	"""Pick the operative disposition: (label, match, tail_offset, tail_text)."""
	assessed = _assess_outcome(content)
	if assessed is None:
		return None
	best, _candidates, _operative_start, offset, tail = assessed
	return best[2], best[3], offset, tail


_PROCEDURAL_SENTENCE_RE = re.compile(
	r"\b(?:motions?|extension\s+of\s+time|stay\s+of|stay\s+pending|reinstat\w*|vacat(?:e|ion)\b|interven\w*|taxation|"
	r"assessment\s+of\s+costs|bill\s+of\s+costs|disbursements|security\s+for\s+costs|notice\s+of\s+appeal|"
	r"remov\w+\s+from\s+the\s+file|file\s+be\s+closed|adjourn\w*|objection)\b",
	re.IGNORECASE,
)
_PROCEDURAL_CAPTION_RE = re.compile(
	r"\bMOTIONS?\s+(?:DEALT\s+WITH|FOR|TO|BY|IN\s+WRITING)\b|\bASSESSMENT\s+OF\s+COSTS\b|\bTAXATION\b|"
	r"\bREASONS\s+FOR\s+ASSESSMENT\b|\bORDER\s+ON\s+MOTION\b",
)
_PROCEDURAL_TRIBUNAL_RE = re.compile(
	r"\b(?:application\s+to\s+(?:reinstate|vacate|reopen|re-open|cease|intervene|change|set\s+aside)|"
	r"extension\s+of\s+time|application\s+for\s+(?:an\s+)?extension|cessation\s+application|vacation\s+application|change\s+of\s+(?:venue|location))\b",
	re.IGNORECASE,
)
_MERITS_WORDS_RE = re.compile(
	r"\b(?:allowed|dismissed|granted|denied|rejected|refused|set\s+aside|quashed|remitted|referred\s+back|returned\s+for)\b",
	re.IGNORECASE,
)


_TRAILER_RE = re.compile(r"\n\s*(?:SOLICITORS\s+OF\s+RECORD|NAMES?\s+OF\s+COUNSEL|APPEARANCES|DOCKET\s*:)", re.IGNORECASE)


def _is_procedural(content: str, best, operative_start: int, tail: str, is_tribunal: bool) -> bool:
	"""True when the order decides a motion, extension, costs or similar, not the case itself."""
	if is_tribunal and _PROCEDURAL_TRIBUNAL_RE.search(content[:3000]):
		return True
	if not is_tribunal and (
		_PROCEDURAL_CAPTION_RE.search(content[-6000:]) or _PROCEDURAL_CAPTION_RE.search(content[:1500])
	):
		return True
	if best is None:
		return False
	left, _right = _sentence_bounds(tail, best[3].start(), best[3].end())
	if best[4] == "concluding":
		subject = tail[max(left, best[3].end() - 22) : best[3].end()]
	else:
		subject = tail[max(left, best[3].start() - 60) : best[3].end()]
	if best[4] != "headline" and _PROCEDURAL_SENTENCE_RE.search(subject):
		return True
	trailer = _TRAILER_RE.search(tail, max(0, len(tail) - 4000))
	markers = list(_MARKER_RE.finditer(tail[: trailer.start()] if trailer else tail))
	if markers:
		last = markers[-1].start()
		block = tail[last : last + 900]
		if best[1] < last and re.search(r"\bcosts\b", block, re.IGNORECASE) and not _MERITS_WORDS_RE.search(block):
			return True
	return False


_CONFLICT_WINDOW = 500


def _same_sentence_concluding(candidate, best, tail: str) -> bool:
	""""The appeal should be allowed, the application should be dismissed" is one ruling, not two."""
	if candidate[4] != "concluding" or best[4] != "concluding":
		return False
	low, high = sorted((candidate[1], best[1]))
	return not re.search(r"[\n]|\.\s", tail[low:high])


_RAD_HEAD_RE = re.compile(r"\bRAD\s+File\b|dossier\s+de\s+la\s+SAR", re.IGNORECASE)
_RAD_OPERATIVE_RE = re.compile(
	r"^[ \t]*(?:[IVX]+\.[ \t]*)?(?:REMEDY|REMEDIES|CONCLUSION|DETERMINATION|DECISION)[ \t]*(?=\[\d+\]|$)", re.MULTILINE
)
_RAD_ANNEX_RE = re.compile(r"\n[ \t]*(?:ANNEX|APPENDIX|SCHEDULE)\b")
_RAD_ACTOR = r"(?:I|(?:the\s+)?(?:RAD|Refugee\s+Appeal\s+Division))\s+(?:hereby\s+)?"
_RAD_DISMISS_RE = re.compile(
	r"\bappeals?\s+(?:of\s+[^.\n]{1,100}?\s+)?(?:is|are)\s+(?:hereby\s+)?(?:dismissed|denied)\b"
	rf"|\b{_RAD_ACTOR}(?:dismisses|dismiss|denies|deny)\s+(?:the|this|his|her|their|the\s+Minister['’]s)\s+appeals?\b"
	rf"|\b{_RAD_ACTOR}confirms?\s+the\s+(?:RPD['’]s\s+)?(?:determination|decision)\b",
	re.IGNORECASE,
)
_RAD_ALLOW_RE = re.compile(
	r"\bappeals?\s+(?:of\s+[^.\n]{1,100}?\s+)?(?:is|are)\s+(?:hereby\s+)?(?:allowed|granted)\b"
	rf"|\b{_RAD_ACTOR}(?:allows?|grants?)\s+the\s+appeals?\b"
	rf"|\b{_RAD_ACTOR}sets?\s+aside\s+the\s+(?:RPD['’]s\s+)?(?:determination|decision)\b"
	r"|\b(?:determination|decision)\s+of\s+the\s+RPD\s+is\s+set\s+aside\b"
	rf"|\b{_RAD_ACTOR}refers?\s+(?:the|this|their|his|her)\s+(?:matter|claims?)\s+(?:back\s+)?to\s+the\s+(?:RPD|Refugee\s+Protection\s+Division)\b"
	rf"|\b{_RAD_ACTOR}substitut\w+\b",
	re.IGNORECASE,
)
_RAD_PROCEDURAL_RE = re.compile(
	r"\bapplications?\s+(?:for\s+(?:an\s+)?extension\s+of\s+time|to\s+(?:reopen|re-open|reinstate|vacate|change))\b[^.\n]{0,120}?\b(?:is|are)\s+(?:therefore\s+)?(?:allowed|granted|dismissed|denied)\b",
	re.IGNORECASE,
)
_RAD_MINISTER_APPEAL_RE = re.compile(
	r"\bMinister['’]s\s+(?:Notice\s+of\s+)?appeal\b|\bNotice\s+of\s+Appeal\s+from\s+the\s+Minister\b"
	r"|\bappeals?\s+(?:filed\s+|brought\s+)?by\s+the\s+Minister\b|\bthe\s+Minister\s+(?:is\s+)?appeal(?:s|ing)\b",
	re.IGNORECASE,
)


def _is_rad_document(content: str) -> bool:
	"""Refugee Appeal Division reasons (the cover page carries the RAD file number), not a court judgment reviewing one."""
	return not _COURT_HEAD_RE.search(content[:800]) and bool(_RAD_HEAD_RE.search(content[:800]))


def _decide_rad(content: str) -> "Decision | None":
	"""Read a RAD disposition from its remedy section: confirm/dismiss, set aside/refer back, or both for different appellants.

	Returns None when the remedy section holds no recognisable ruling so the general rules still decide.
	"""
	text = _strip_footnotes(content)
	paragraphs = list(re.finditer(r"\n\s*\[\d+\]", text))
	annex = _RAD_ANNEX_RE.search(text, paragraphs[-1].end()) if paragraphs else None
	if annex:
		text = text[: annex.start()]
	markers = [m for m in _RAD_OPERATIVE_RE.finditer(text) if len(text) - m.start() <= 6000]
	start = markers[-1].start() if markers else max(0, len(text) - 2500)
	# Section 111(1) is often recited at the top of the remedy; the ruling itself is in the last paragraphs.
	start = max(start, len(text) - 1800)
	section = text[start:]
	dismiss = _RAD_DISMISS_RE.search(section)
	allow = _RAD_ALLOW_RE.search(section)
	procedural = _RAD_PROCEDURAL_RE.search(section)
	if procedural and not dismiss and not allow:
		return Decision("procedural", "procedural_order", procedural, start, section, False, 3, "rad_operative")
	if dismiss and allow:
		return Decision("mixed", "ruling", dismiss, start, section, True, 3, "rad_operative")
	if dismiss or allow:
		match = dismiss or allow
		return Decision("dismissed" if dismiss else "allowed", "ruling", match, start, section, False, 3, "rad_operative")
	return None


class Decision:
	"""The result of reading a decision's disposition."""

	__slots__ = ("label", "reason", "match", "offset", "tail", "partial", "rank", "source")

	def __init__(self, label, reason, match=None, offset=0, tail="", partial=False, rank=0, source="none"):
		self.label, self.reason, self.match, self.offset, self.tail = label, reason, match, offset, tail
		self.partial, self.rank, self.source = partial, rank, source


_CLASS = {
	"allowed": "A", "granted": "A", "set_aside": "A", "remitted": "A",
	"dismissed": "D", "withdrawn": "W",
}


_RLLR_HEAD_RE = re.compile(r"Tribunal:\s*Refugee\s+Protection\s+Division[\s\S]{0,300}?\bRPD\s+Number:", re.IGNORECASE)
_RLLR_END_RE = re.compile(r"\n[ \t]*[—–―‒-]{3,}[^\n]{0,30}$", re.MULTILINE)
_RLLR_CLASS = r"[“\"]?(?:Convention\s+refugees?|persons?\s+in\s+need\s+of\s+protection|people\s+in\s+need\s+of\s+protection|refugees?)"
_RLLR_REJECT_RE = re.compile(
	r"(?<!\bto\s)\b(?:reject(?:s|ed|ing)?|den(?:y|ies|ied|ying)|dismiss(?:es|ed|ing)?)\s+(?:all\s+of\s+|both\s+of\s+|each\s+of\s+)?(?:your|the|his|her|their)\s+(?:refugee\s+)?claims?\b"
	r"|\bclaims?\s+(?:is|are)\s*,?\s*(?:hereby\s+|therefore\s*,?\s+)?(?:rejected|denied|dismissed)\b"
	r"|\b(?:are|is)\s+(?:neither|not)\s+(?:a\s+)?[“\"]?Convention\s+refugee\b",
	re.IGNORECASE,
)
_RLLR_ACCEPT_RE = re.compile(
	r"\baccept(?:s|ed|ing)?\s+(?:all\s+of\s+|both\s+of\s+|each\s+of\s+)?(?:your|the|his|her|their)\s+(?:refugee\s+)?claims?\b"
	r"|\baccept(?:s|ed)?\s+that\s+(?:you|they|he|she|the\s+claimants?)\s+(?:are|is)\s+\w*\s*" + _RLLR_CLASS +
	r"|\bclaims?\s+(?:for\s+refugee\s+protection\s+)?(?:is|are)\s*,?\s*(?:hereby\s+|therefore\s*,?\s+)?(?:accepted|allowed|granted)\b"
	r"|\b(?:are|is|be)\s+(?:all\s+|both\s+)?(?:a\s+|an\s+)?" + _RLLR_CLASS,
	re.IGNORECASE,
)


def _is_rllr_document(content: str) -> bool:
	"""Refugee Law Lab Reporter copy of a Refugee Protection Division decision (header block with RPD Number)."""
	return bool(_RLLR_HEAD_RE.search(content[:800]))


def _decide_rllr(content: str) -> "Decision | None":
	"""Read the claim ruling from the closing paragraphs, before the footnotes and the transcript sign-off."""
	end = _RLLR_END_RE.search(content)
	text = _strip_footnotes(content[: end.start()] if end else content)
	for window in (1500, 6000):
		start = max(0, len(text) - window)
		section = text[start:]
		reject = _RLLR_REJECT_RE.search(section)
		if reject and re.match(r"[^.]{0,200}?\bbut\s+(?:is|are)\s+(?:a\s+)?persons?\s+in\s+need", section[reject.end():], re.IGNORECASE):
			reject = None  # "not a Convention refugee, but a person in need of protection" is still a granted claim
		accept = _RLLR_ACCEPT_RE.search(section)
		if reject and accept:
			return Decision("mixed", "ruling", reject, start, section, True, 3, "rllr_operative")
		if reject or accept:
			match = reject or accept
			return Decision("dismissed" if reject else "allowed", "ruling", match, start, section, False, 3, "rllr_operative")
	return None


def _decide(content: str) -> "Decision | None":
	"""Read the disposition. Labels: a ruling, "procedural", or "unclear" (the rules are not sure)."""
	if not content or not content.strip():
		return None
	if _is_rad_document(content):
		rad_decision = _decide_rad(content)
		if rad_decision is not None:
			return rad_decision
	if _is_rllr_document(content):
		rllr_decision = _decide_rllr(content)
		if rllr_decision is not None:
			return rllr_decision
	assessed = _assess_outcome(content)
	is_tribunal = _is_tribunal_document(content)
	if assessed is None:
		if _is_procedural(content, None, 0, "", is_tribunal):
			return Decision("procedural", "procedural_document")
		return Decision("unclear", "no_disposition_found")
	best, candidates, operative_start, offset, tail = assessed
	match = best[3]
	if _is_procedural(content, best, operative_start, tail, is_tribunal):
		return Decision("procedural", "procedural_order", match, offset, tail, False, best[0], best[4])
	strong = {
		_CLASS[c[2]]
		for c in candidates
		if c[0] >= 3 and c[1] >= operative_start and c[1] >= best[1] - _CONFLICT_WINDOW and not _same_sentence_concluding(c, best, tail)
		and (c[4] != "tribunal_finding" or best[4] == "tribunal_finding")
	}
	in_operative = operative_start > 0 and best[1] >= operative_start
	if best[0] < 3 and not (in_operative and best[4] in {"bare_verdict", "consequence"}):
		return Decision("unclear", "weak_cue_only", match, offset, tail, False, best[0], best[4])
	if len(strong) > 1 and best[0] < 4:
		return Decision("unclear", "conflicting_rulings", match, offset, tail, False, best[0], best[4])
	partial = _is_partial(tail, match)
	return Decision("mixed" if partial else best[2], "ruling", match, offset, tail, partial, best[0], best[4])


def _is_partial(tail: str, match: re.Match[str]) -> bool:
	left, right = _sentence_bounds(tail, match.start(), match.end())
	sentence = re.sub(r"\b(?:dissenting|concurring|dissent|concurs?)\s+in\s+part\b", " ", tail[left:right], flags=re.IGNORECASE)
	return bool(_PARTIAL_RE.search(sentence))


def _government_role(style_or_between: str) -> str | None:
	if not style_or_between:
		return None
	text = " ".join(style_or_between.split())
	# Tribunal captions list "Counsel for the Minister"; that line names a representative, not a party.
	text = re.sub(r"(?:counsel|representative)s?\s+(?:for|of)\s+the\s+minister|conseil\s+du\s+ministre", " ", text, flags=re.IGNORECASE)
	# "For the Applicant / For the Respondent" lines label counsel, not the party named just before them.
	text = re.sub(r"\bfor\s+(?:the\s+)?(?:applicants?|respondents?|appellants?)\b|\bpour\s+(?:le|la|les)\s+\w+", " ", text, flags=re.IGNORECASE)
	lower = text.lower()
	if not _GOVERNMENT_PARTY_RE.search(lower):
		return None

	applicant_matches = list(re.finditer(r"\b(?:applicants?|appellants?)\b", lower))
	respondent_matches = list(re.finditer(r"\brespondents?\b", lower))
	gov_matches = list(_GOVERNMENT_PARTY_RE.finditer(lower))
	if not gov_matches:
		return None

	def nearest_distance(a: int, positions: list[re.Match[str]]) -> int:
		if not positions:
			return 10**9
		best = 10**9
		for pos in positions:
			distance = abs(a - pos.start())
			# In captions, the role token commonly appears after the party name.
			if pos.start() < a:
				distance += 40
			if distance < best:
				best = distance
		return best

	best_role: str | None = None
	best_distance = 10**9
	for match in gov_matches:
		idx = match.start()
		d_app = nearest_distance(idx, applicant_matches)
		d_res = nearest_distance(idx, respondent_matches)
		if min(d_app, d_res) > 120:
			continue
		if d_app < d_res and d_app < best_distance:
			best_distance = d_app
			best_role = "applicant"
		elif d_res < d_app and d_res < best_distance:
			best_distance = d_res
			best_role = "respondent"

	if best_role is not None:
		return best_role

	vs_split = re.split(r"\bv\.?\b", lower, maxsplit=1)
	if len(vs_split) == 2:
		left, right = vs_split
		if _GOVERNMENT_PARTY_RE.search(left):
			return "applicant"
		if _GOVERNMENT_PARTY_RE.search(right):
			return "respondent"
	return None


def _role_from_style(style: str) -> str | None:
	"""Side of the government party in an "X v. Y" style of cause (left = applicant/appellant).

	Returns "none" when the style names two sides and neither is a government party.
	"""
	parts = re.split(r"\s+v\.?\s+", " ".join(style.split()), maxsplit=1, flags=re.IGNORECASE)
	if len(parts) != 2:
		return None
	left, right = parts
	if _GOVERNMENT_PARTY_RE.search(left):
		return "applicant"
	if _GOVERNMENT_PARTY_RE.search(right):
		return "respondent"
	return "none"


_STYLE_LINE_RE = re.compile(r"^[ \t]*(?:STYLE\s+OF\s+CAUSE|INTITUL[ÉE])\s*:?[ \t]*\n?[ \t]*([^\n]{5,250})$", re.IGNORECASE | re.MULTILINE)


_ROLE_LABEL_RE = re.compile(r"\b(applicants?|appellants?|respondents?|interveners?|intervenors?)[ \t]*(?=\n|$)", re.IGNORECASE)
_PARTY_SEPARATOR_RE = re.compile(r"\n[ \t]*(?:and|v\.?|et|[-\u2010-\u2015]+\s*and\s*[-\u2010-\u2015]+)[ \t]*\n", re.IGNORECASE)


def _role_from_labelled_parties(text: str) -> str | None:
	"""Side of the government party when the caption labels each party ("Minister ... Appellant").

	The labels say who brought the proceeding. They beat the order of the names in a title or style of cause,
	which can follow the lower court (SCC pages are titled "Gladstone v. Canada (Attorney General)" even though the
	Attorney General is the appellant) and which the Minister can appear on either side of.
	"""
	text = re.sub(r"(?:counsel|representative)s?\s+(?:for|of)\s+the\s+minister|for\s+(?:the\s+)?(?:applicants?|respondents?|appellants?)\b", " ", text, flags=re.IGNORECASE)
	found: set[str] = set()
	start = 0
	for match in _ROLE_LABEL_RE.finditer(text):
		label = match.group(1).lower()
		segment = text[start : match.start()]
		start = match.end()
		if label.startswith("interven"):
			break
		segment = _PARTY_SEPARATOR_RE.split("\n" + segment + "\n")[-1]
		segment = re.split(r"\b(?:between|entre)\s*:", segment, flags=re.IGNORECASE)[-1]
		if _GOVERNMENT_PARTY_RE.search(segment):
			found.add("respondent" if label.startswith("respondent") else "applicant")
	return found.pop() if len(found) == 1 else None


def _resolve_government_role(content: str, metadata: dict[str, object]) -> str | None:
	"""Prefer the style of cause, then the title line; fall back to caption role labels."""
	if _is_rllr_document(content):
		return None
	if _is_rad_document(content):
		# The Minister is a party to a RAD appeal only when the Minister brought it; otherwise there is no government side.
		return "applicant" if _RAD_MINISTER_APPEAL_RE.search(content[:3500]) else None
	style_text = str(metadata.get("style of cause") or "").strip()
	between_text = str(metadata.get("between") or "").strip()
	labelled = _role_from_labelled_parties("\n".join(part for part in (between_text, content[:3000]) if part))
	if labelled:
		return labelled
	candidates = [style_text] if style_text else []
	# Federal Court judgments put "STYLE OF CAUSE:" on a cover page that can sit after the reasons.
	cover = _STYLE_LINE_RE.search(content or "")
	if cover:
		candidates.append(cover.group(1).strip())
	first_line = content.lstrip()[:300].split("\n", 1)[0].strip() if content else ""
	if first_line and len(first_line) < 220:
		candidates.append(first_line)
	for text in candidates:
		role = _role_from_style(text)
		if role == "none":
			# Neither side of the style names a government party by its full name ("CUESTA v. MCI" is the common
			# abbreviation case), so let the Between block decide before giving up.
			return _government_role(between_text) if between_text else None
		if role:
			return role
	return _government_role("\n".join(part for part in (style_text, between_text, content[:1200]) if part))


_RULING_LABELS = {"allowed", "granted", "set_aside", "remitted", "dismissed", "mixed", "withdrawn"}


def _derive_outcome_fields(content: str, metadata: dict[str, object]) -> dict[str, tuple[str, float]]:
	derived: dict[str, tuple[str, float]] = {}
	decision = _decide(content)
	outcome = decision.label if decision else None
	partial = bool(decision and decision.label == "mixed")
	if outcome in {"procedural", "unclear"}:
		derived["decision outcome"] = (outcome, 0.60)
		derived["outcome status"] = ("undetermined", 0.50)
		return derived
	if outcome:
		derived["decision outcome"] = (outcome, 0.70 if partial else 0.78)

	gov_role = _resolve_government_role(content, metadata)
	if gov_role:
		derived["government role"] = (gov_role, 0.74)

	if outcome and gov_role:
		if partial:
			government_outcome = "mixed"
		elif outcome == "dismissed":
			government_outcome = "lost" if gov_role == "applicant" else "won"
		elif outcome in {"allowed", "granted", "set_aside", "remitted"}:
			government_outcome = "won" if gov_role == "applicant" else "lost"
		else:
			government_outcome = "undetermined"
		derived["government outcome"] = (government_outcome, 0.70 if partial else 0.76)
		winner = gov_role if government_outcome == "won" else "applicant" if gov_role == "respondent" else "respondent"
		loser = "respondent" if winner == "applicant" else "applicant"
		if government_outcome == "mixed":
			winner = loser = "mixed"
		derived["case winner"] = (winner, 0.70 if partial else 0.76)
		derived["case loser"] = (loser, 0.70 if partial else 0.76)
		derived["outcome status"] = (government_outcome, 0.70 if partial else 0.76)
	elif outcome:
		derived["outcome status"] = ("mixed" if partial else "undetermined", 0.60 if partial else 0.50)

	return derived


def derive_outcome_detail(content: str, metadata: dict[str, object]) -> dict[str, object]:
	"""Return structured disposition evidence without replacing legacy fields."""
	decision = _decide(content)
	if decision is None or decision.match is None:
		return {
			"status": "undetermined",
			"disposition": decision.label if decision else None,
			"evidence": None,
			"reason": decision.reason if decision else None,
		}

	match, tail_offset = decision.match, decision.offset
	evidence = {
		"text": match.group(0),
		"offset_start": tail_offset + match.start(),
		"offset_end": tail_offset + match.end(),
	}
	if decision.label not in _RULING_LABELS:
		return {"status": "undetermined", "disposition": decision.label, "evidence": evidence, "reason": decision.reason}
	label, partial = decision.label, decision.partial
	role = _resolve_government_role(content, metadata)
	status = "mixed" if partial else "undetermined"
	winner = loser = None
	if role and not partial:
		# "applicant" is the party that brought the proceeding or appeal, whoever it is (the Minister can be the
		# appellant), so who won depends only on the ruling, never on which side the government is on.
		applicant_won = label in {"allowed", "granted", "set_aside", "remitted"}
		status = "won" if applicant_won else "lost"
		winner = "applicant" if applicant_won else "respondent"
		loser = "respondent" if winner == "applicant" else "applicant"
	return {
		"status": status,
		"disposition": label,
		"winner": winner,
		"loser": loser,
		"government_role": role,
		"evidence": evidence,
		"reason": decision.reason,
	}


def build_case_outcome(content: str, metadata: dict[str, object]) -> dict[str, object]:
	"""Build the normalized dedicated outcome record for one case."""
	fields = _derive_outcome_fields(content, metadata)
	detail = derive_outcome_detail(content, metadata)
	confidence_values = [score for _value, score in fields.values()]
	evidence = detail.get("evidence") or {}
	return {
		"classifier_version": OUTCOME_CLASSIFIER_VERSION,
		"decision_outcome": fields.get("decision outcome", (None, 0.0))[0],
		"outcome_status": detail.get("status") or "undetermined",
		"winner_side": detail.get("winner") or fields.get("case winner", (None, 0.0))[0],
		"loser_side": detail.get("loser") or fields.get("case loser", (None, 0.0))[0],
		"government_role": fields.get("government role", (detail.get("government_role"), 0.0))[0],
		"government_outcome": fields.get("government outcome", (None, 0.0))[0],
		"challenged_issue": metadata.get("challenged issue"),
		"challenged_issues": [
			item for item in str(metadata.get("challenged issues") or "").split(", ") if item
		],
		"disposition_evidence": evidence.get("text"),
		"evidence_offset_start": evidence.get("offset_start"),
		"evidence_offset_end": evidence.get("offset_end"),
		"confidence": max(confidence_values, default=0.0),
		"source": "deterministic_outcome",
	}
