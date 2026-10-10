"""Deterministic "case frame": what kind of proceeding this decision is, before any paragraph is read.

Example frame: "Judicial review in the Federal Court of a Refugee Protection Division decision about
cessation. The applicant is the protected person; the respondent is the Minister. The question is whether the
RPD's decision was reasonable."

Built from the header, the parties block, the opening paragraphs and (optionally) the stored case-type label.
Nothing here calls a model, a network service or a database. Every field records where it came from
(``header``, ``text``, ``case_type``, ``default``) and a confidence (``high``, ``medium``, ``low``); a field
that cannot be found is ``unknown`` and is never guessed.

Layer names follow the plan: L0 the judge, L1 the parties before the court, L2 the earlier decision maker,
L3 the first-instance parties as reported in that decision.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any

FRAME_VERSION = "frame_v1"
UNKNOWN = "unknown"

_GOV = re.compile(r"minister|attorney general|canada\s*\(|public safety|border services|his majesty|the king|the queen|"
	r"ministre|procureur", re.I)

# earlier decision makers: key -> (pattern, label)
_EARLIER = (
	("rpd", r"refugee protection division|\bRPD\b|\bSPR\b", "Refugee Protection Division"),
	("rad", r"refugee appeal division|\bRAD\b|\bSAR\b", "Refugee Appeal Division"),
	("iad", r"immigration appeal division|\bIAD\b|\bSAI\b", "Immigration Appeal Division"),
	("id", r"immigration division\b|\bID\b member", "Immigration Division"),
	("delegate", r"minister['’]s delegate|delegate of the minister", "Minister's delegate"),
	("officer", r"(?:visa |immigration |senior immigration |pra?r?a |h&c |case |reviewing |biometrics )?officer\b|"
		r"\bvisa office\b|agent des visas|agent", "officer"),
	("judge", r"(?:application|motions?|trial|reviewing|federal court) judge|federal court\b(?=[^.]{0,30}(?:judgment|decision|order))|"
		r"tax court|superior court|court of appeal|trial judge", "lower court judge"),
	("agency", r"canada revenue agency|\bCRA\b|minister of national revenue|\bCBSA\b|\bIRCC\b", "agency"),
	("tribunal", r"human rights (?:tribunal|commission)|social security tribunal|labour board|"
		r"canadian human rights|public service|commission\b|tribunal\b|board\b|arbitrator|adjudicator", "tribunal"),
)
_EARLIER_RE = tuple((k, re.compile(p, re.I if k not in ("rpd", "rad", "iad") else 0), lab) for k, p, lab in _EARLIER)

_JR_LEAD = re.compile(
	r"(?:application|motion|demande)[^.]{0,60}?(?:for\s+)?judicial review[^.]{0,80}?(?:of|against)\s+(?:a|an|the)?\s*"
	r"(?:decision|determination|refusal|dismissal|order|finding)s?\s+(?:of|by|made by|rendered by)\s+(?P<who>[^.]{3,120}?)(?:[.,;]|\s+dated|\s+made|\s+refusing|\s+rejecting|\s+on\b|$)",
	re.I)
_POSS_DECISION = re.compile(
	r"\b((?:the |an? )?(?:visa |immigration |senior immigration |pra?r?a |h&c |case )?(?:officer|RPD|RAD|IAD|SPR|SAR|Board|Member|"
	r"delegate|Minister['’]s delegate|Commission|Tribunal|CRA|Canada Revenue Agency|Judge|Chair|Division)['’]s?)\s+"
	r"(?:decision|refusal|reasons|determination|finding|conclusion|notes)|"
	r"\b(?:decision|refusal|determination|reasons) (?:of|by) ((?:the |an? )?(?:visa |senior immigration |immigration )?(?:officer|RPD|RAD|IAD|Board|Member|"
	r"delegate|Commission|Tribunal|CRA|Canada Revenue Agency|Judge|Chair|Division))", re.I)
_JR_ANY = re.compile(r"judicial review|section 72|s\. 72|contr[ôo]le judiciaire|18\.1", re.I)
_APPEAL_ANY = re.compile(r"\bnotice of appeal\b|\bappeal from\b|\bappeal of\b|\bleave to appeal\b|\bthis appeal\b|\bthe appeal\b|\bappellants?\b", re.I)
_MOTION_ANY = re.compile(r"\bmotion (?:to strike|for a stay|for|to)\b|\bstay of (?:removal|the)\b|\binjunction\b|\bcertified question\b", re.I)
_BETWEEN = re.compile(
	r"BETWEEN:?\s*(?P<a>.{2,300}?)\s*\b(?P<arole>Applicants?|Appellants?|Plaintiffs?|Petitioners?|Moving Party)\b"
	r"\s*(?:\(.{0,40}?\))?\s*(?:-\s*and\s*-|and|et)\s*(?P<b>.{2,300}?)\s*\b(?P<brole>Respondents?|Defendants?|Intim[ée]s?)\b",
	re.I | re.S)
_STANDARD_STATED = re.compile(
	r"standard of review[^.]{0,120}?\b(reasonableness|correctness|procedural fairness|palpable and overriding)\b|"
	r"\b(reasonableness|correctness|palpable and overriding error)\b[^.]{0,60}standard", re.I)
_FAIRNESS = re.compile(r"procedural fairness|natural justice|duty of fairness|breach of fairness", re.I)
_DISPOSITION = re.compile(
	r"(?:application|appeal|motion)[^.]{0,40}?(?:is|are|will be|must be|shall be)\s+(allowed|dismissed|granted|refused)|"
	r"(?:allow|dismiss)(?:s|ed|ing)? the (?:application|appeal|motion)|THIS COURT['’]S JUDGMENT is that", re.I)


@dataclass
class FrameField:
	value: str
	source: str = "default"
	confidence: str = "low"

	@property
	def known(self) -> bool:
		return self.value != UNKNOWN


@dataclass
class CaseFrame:
	version: str = FRAME_VERSION
	court: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	proceeding: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	earlier_decision_maker: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	subject: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	applicant_name: str = ""
	respondent_name: str = ""
	applicant_is_minister: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	standard_of_review: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	layers_present: list[str] = field(default_factory=list)
	question: str = ""
	disposition: str = UNKNOWN
	# What kind of document this is and whose voice is the default. A decision is written by the court or tribunal;
	# a memorandum of argument, factum or written submissions is written by one side, so every untagged sentence
	# in it is that side's position, not the Court's.
	document_kind: FrameField = field(default_factory=lambda: FrameField(UNKNOWN))
	author: FrameField = field(default_factory=lambda: FrameField("court"))

	def to_dict(self) -> dict[str, Any]:
		return asdict(self)

	@property
	def has_earlier_decision(self) -> bool:
		return self.earlier_decision_maker.known

	@property
	def confident(self) -> bool:
		"""Court, proceeding and sides are known; and an earlier decision maker when the proceeding needs one."""
		need_earlier = self.proceeding.value in ("judicial_review", "appeal")
		return (self.court.known and self.proceeding.known and self.applicant_is_minister.known
			and (self.earlier_decision_maker.known or not need_earlier))

	def text(self) -> str:
		"""Short plain-language frame, built only from known fields."""
		court = {"fc": "the Federal Court", "fca": "the Federal Court of Appeal", "scc": "the Supreme Court of Canada",
			"rpd": "the Refugee Protection Division", "rad": "the Refugee Appeal Division",
			"iad": "the Immigration Appeal Division", "id": "the Immigration Division"}.get(self.court.value, "")
		kind = {"judicial_review": "judicial review", "appeal": "appeal", "motion": "motion", "direct": "hearing"}.get(
			self.proceeding.value, "")
		parts = []
		if kind and court:
			earlier = self.earlier_decision_maker.value
			if self.proceeding.value in ("judicial_review", "appeal") and earlier != UNKNOWN:
				parts.append(f"This is {_a(kind)} {kind} in {court} of a decision of the {_label(earlier)}"
					+ (f" about {self.subject.value}" if self.subject.known else "") + ".")
			else:
				parts.append(f"This is {_a(kind)} {kind} in {court}.")
		if self.applicant_is_minister.known:
			parts.append("The Minister is the applicant." if self.applicant_is_minister.value == "yes"
				else "The applicant is the individual (the Minister or the Crown is the respondent).")
		if self.document_kind.known and self.document_kind.value != "decision":
			who = {"applicant": "the applicant", "respondent": "the respondent"}.get(self.author.value, "one side")
			parts.append(f"This document is {_a(self.document_kind.value)} {self.document_kind.value} written by {who}, so its untagged statements are that side's position.")
		if self.question:
			parts.append(self.question)
		return " ".join(parts)


_DOC_KIND = (
	("memorandum", r"memorandum of (?:argument|fact and law)|m[ée]moire (?:des faits et du droit|de l['’]?(?:appelant|intim[ée]|demandeur|d[ée]fendeur))"),
	("factum", r"\bfactum\b"),
	("submissions", r"written (?:submissions|representations)|further (?:written )?submissions|reply submissions|submissions of the (?:applicant|respondent|appellant|minister)"),
	("decision", r"judgment and reasons|reasons for (?:judgment|decision|order)|reasons and decision|order and reasons|"
		r"notice of decision|reasons for judgment and judgment|motifs (?:du jugement|de la d[ée]cision|et d[ée]cision)|jugement et motifs"),
)
_DOC_AUTHOR = re.compile(
	r"\b(?P<side>applicant|appellant|respondent|minister|moving party|intervener|plaintiff|defendant|demandeur|demanderesse|d[ée]fendeur|intim[ée]e?|appelante?)"
	r"['’]?s?\s+(?:memorandum|factum|written submissions|submissions|m[ée]moire)|"
	r"(?:memorandum|factum|submissions|m[ée]moire)\s+(?:of|de|du|for|on behalf of)\s+(?:the\s+|la\s+|l['’]|le\s+)?(?P<side2>applicant|appellant|respondent|minister|moving party|intervener|plaintiff|defendant|demandeur|demanderesse|d[ée]fendeur|intim[ée]e?|appelante?)|"
	r"prepared by counsel for the (?P<side3>applicant|appellant|respondent|minister)", re.I)


def _document_kind(head: str) -> tuple[FrameField, str | None]:
	"""Kind of document from its first lines, and the side that wrote it when the heading says so."""
	for key, pat in _DOC_KIND:
		m = re.search(pat, head, re.I)
		if not m:
			continue
		# a heading ("RESPONDENT'S MEMORANDUM OF ARGUMENT", "Applicant's written submissions"), not a passing
		# mention in a sentence ("the submissions of the applicant were...")
		before = head[head.rfind("\n", 0, m.start()) + 1:m.start()]
		if m.group(0).isupper() or re.fullmatch(r"\s*(?:(?:the\s+)?[\w’']+\s+){0,3}", before, re.I):
			kind = FrameField(key, "header", "high")
			break
	else:
		return FrameField(UNKNOWN), None
	if key == "decision":
		return kind, None
	m = _DOC_AUTHOR.search(head)
	side = (m.group("side") or m.group("side2") or m.group("side3")).lower() if m else None
	return kind, side


def _a(word: str) -> str:
	return "an" if word[:1] in "aeiou" else "a"


def _label(key: str) -> str:
	for k, _, lab in _EARLIER_RE:
		if k == key:
			return lab
	return key


def _detect_court(header: str, docket: str) -> FrameField:
	h = header[:700]
	for key, pat in (("fca", r"Federal Court of Appeal"), ("fc", r"Federal Court Decisions"), ("scc", r"Supreme Court"),
			("rpd", r"\bRPD File|dossier de la SPR"), ("rad", r"\bRAD File|dossier de la SAR"),
			("iad", r"\bIAD File|dossier de la SAI"), ("id", r"\bID File|dossier de la SI\b")):
		if re.search(pat, h):
			return FrameField(key, "header", "high")
	# a tribunal decision whose header names the division (pasted or uploaded documents have no file label)
	for key, pat in (("rpd", r"Refugee Protection Division|Section de la protection des r[ée]fugi[ée]s"),
			("rad", r"Refugee Appeal Division|Section d['’]appel des r[ée]fugi[ée]s"),
			("iad", r"Immigration Appeal Division|Section d['’]appel de l['’]immigration"),
			("id", r"Immigration Division|Section de l['’]immigration")):
		if re.search(pat, h, re.I):
			return FrameField(key, "header", "medium")
	if re.search(r"\bA-\d+-\d+\b", docket or h):
		return FrameField("fca", "header", "medium")
	if re.search(r"\b(?:IMM|T)-\d+-\d+\b", docket or h):
		return FrameField("fc", "header", "medium")
	return FrameField(UNKNOWN)


def _earlier_from(who: str) -> str:
	for key, rx, _ in _EARLIER_RE:
		if rx.search(who):
			return key
	return UNKNOWN


def build_frame(header_text: str, body_text: str = "", *, case_type: str | None = None, case_type_court: str | None = None) -> CaseFrame:
	"""Build the frame. ``header_text`` is the stored header (title, database, court, docket, BETWEEN block);
	``body_text`` the decision text (the first ~4,000 characters matter). ``case_type`` is the deterministic
	case-type label when one exists (used only for the subject)."""
	f = CaseFrame()
	header = header_text or ""
	intro = (body_text or "")[:4000]
	allhead = header + "\n" + intro
	docket = ""
	dm = re.search(r"\b((?:IMM|[A-Z]{1,2})-\d+-\d+)\b", allhead)
	if dm:
		docket = dm.group(1)
	f.court = _detect_court(header, docket)
	f.document_kind, author_side = _document_kind((header + "\n" + intro[:600]))
	if f.court.value in ("rpd", "rad", "iad", "id") and not f.document_kind.known:
		f.document_kind = FrameField("decision", "header", "medium")

	# parties and who is the Minister
	bm = _BETWEEN.search(allhead)
	title = header.strip().splitlines()[0] if header.strip() else ""
	tparts = re.split(r"\s+(?:v\.?|c\.|vs\.?)\s+", title, maxsplit=1)
	crown = re.compile(r"his majesty|the king|the queen|^\s*r\.?\s*$|\bregina\b|\brex\b|^\s*r\.?\s+v\.?", re.I)
	if bm:
		a, b = re.sub(r"\s+", " ", bm.group("a")).strip(), re.sub(r"\s+", " ", bm.group("b")).strip()
		f.applicant_name, f.respondent_name = a, b
		a_gov, b_gov = bool(_GOV.search(a)), bool(_GOV.search(b))
		if crown.search(a) or crown.search(b) or crown.search(title):
			f.applicant_is_minister = FrameField("crown", "header", "high")  # criminal side: keep literal roles
		elif a_gov and not b_gov:
			f.applicant_is_minister = FrameField("yes", "header", "high")
		elif b_gov and not a_gov:
			f.applicant_is_minister = FrameField("no", "header", "high")
		elif not a_gov and not b_gov:
			f.applicant_is_minister = FrameField("no", "header", "medium")  # private parties
	elif len(tparts) == 2:
		f.applicant_name, f.respondent_name = tparts
		if crown.search(title):
			f.applicant_is_minister = FrameField("crown", "header", "medium")
		elif _GOV.search(tparts[0]) and not _GOV.search(tparts[1]):
			f.applicant_is_minister = FrameField("yes", "header", "medium")
		elif _GOV.search(tparts[1]) or not _GOV.search(tparts[0]):
			f.applicant_is_minister = FrameField("no", "header", "medium")
	if f.court.value in ("rpd", "rad", "iad", "id") and not f.applicant_is_minister.known:
		# tribunal decisions have no style of cause; the claimant/appellant is the individual unless the Minister applies
		minister_applies = re.search(r"minister['’]s application|application by the minister|minister applied|the minister is the applicant|"
			r"cessation|vacation|demande du ministre", intro, re.I)
		f.applicant_is_minister = FrameField("yes" if minister_applies else "no", "text", "low" if minister_applies else "medium")

	# proceeding
	if f.court.value in ("rpd", "rad", "iad", "id"):
		f.proceeding = FrameField("appeal" if f.court.value in ("rad", "iad") else "direct", "header", "high")
	elif re.search(r"\bmoves? (?:for|to)\b|\bmotion (?:to strike|for a stay|by)|\bis a motion\b", intro[:900], re.I) and not re.search(
			r"seeks? judicial review|application for judicial review of", intro[:900], re.I):
		f.proceeding = FrameField("motion", "text", "medium")
	elif _JR_ANY.search(intro):
		f.proceeding = FrameField("judicial_review", "text", "high" if f.court.value == "fc" else "medium")
	elif _APPEAL_ANY.search(intro) or (f.court.value in ("fca", "scc") and _APPEAL_ANY.search(allhead)):
		f.proceeding = FrameField("appeal", "text", "medium")
	elif _MOTION_ANY.search(intro):
		f.proceeding = FrameField("motion", "text", "medium")
	elif f.document_kind.value in ("memorandum", "factum", "submissions") and f.court.value in ("fc", "fca"):
		# a memorandum in the Federal Courts about a refusal or decision is almost always a judicial review
		if _POSS_DECISION.search(intro) or re.search(r"\brefus(?:ed|al)\b|\bdecision\b", intro, re.I):
			f.proceeding = FrameField("judicial_review" if f.court.value == "fc" else "appeal", "default", "low")

	if f.court.value == "fca" and re.search(
			r"appeal (?:from|of) (?:a |the )?(?:judgment|decision|order|reasons)[^.]{0,40}Federal Court|"
			r"from the (?:judgment|decision|order|reasons) of the Federal Court|Federal Court (?:judge|allowed|dismissed|granted)|"
			r"the Federal Court['’]s (?:judgment|decision)|\bFederal Court judge\b|the application judge", intro, re.I):
		f.proceeding = FrameField("appeal", "text", "high")
		f.earlier_decision_maker = FrameField("judge", "text", "high")
	# earlier decision maker
	jm = _JR_LEAD.search(intro)
	if f.earlier_decision_maker.known:
		pass
	elif f.court.value == "rad":
		f.earlier_decision_maker = FrameField("rpd", "header", "high")
	elif f.court.value in ("rpd", "id"):
		pass  # first instance: no earlier decision
	elif jm:
		key = _earlier_from(jm.group("who"))
		if key != UNKNOWN:
			f.earlier_decision_maker = FrameField(key, "text", "high")
	if not f.earlier_decision_maker.known and f.proceeding.value in ("judicial_review", "appeal") and f.court.value != "rpd":
		if f.court.value in ("fca", "scc") and f.proceeding.value == "appeal":
			f.earlier_decision_maker = FrameField("judge", "default", "low")
		else:
			m = re.search(r"decision of (?:a |an |the )?([^.]{3,100}?)(?:[.,;]| dated| on )", intro, re.I)
			if m:
				key = _earlier_from(m.group(1))
				if key != UNKNOWN:
					f.earlier_decision_maker = FrameField(key, "text", "medium")
	if not f.earlier_decision_maker.known and f.proceeding.value == "judicial_review" and f.court.value in ("fc", "fca"):
		m = re.search(r"judicial review\s+(?:of|from)(.{0,220})", intro, re.I | re.S)
		if m:
			best = None
			for key, rx, _ in _EARLIER_RE:
				if key in ("judge",):
					continue
				mm = rx.search(m.group(1))
				if mm and (best is None or mm.start() < best[0]):
					best = (mm.start(), key)
			if best:
				f.earlier_decision_maker = FrameField(best[1], "text", "high")
	if not f.earlier_decision_maker.known and f.proceeding.value in ("judicial_review", "appeal") and f.court.value != "rpd":
		# fallback: the most-named decision maker whose "decision/reasons" is discussed in the opening
		counts: dict[str, int] = {}
		for m in _POSS_DECISION.finditer(intro):
			key = _earlier_from(m.group(1) or m.group(2))
			if key != UNKNOWN:
				counts[key] = counts.get(key, 0) + 1
		if counts:
			key = max(counts, key=lambda k: counts[k])
			f.earlier_decision_maker = FrameField(key, "text", "medium" if counts[key] >= 2 else "low")
	if case_type:
		f.subject = FrameField(case_type, "case_type", "medium")

	# who wrote this document: the court (a decision) or one side (a memorandum, factum or submissions)
	if f.document_kind.known and f.document_kind.value != "decision":
		if author_side in ("applicant", "appellant", "moving party", "plaintiff", "demandeur", "demanderesse", "appelant", "appelante"):
			f.author = FrameField("applicant", "header", "high")
		elif author_side in ("respondent", "defendant", "intime", "intimé", "intimée", "défendeur", "defendeur"):
			f.author = FrameField("respondent", "header", "high")
		elif author_side == "minister":
			f.author = FrameField("applicant" if f.applicant_is_minister.value == "yes" else "respondent", "header", "medium")
		else:
			f.author = FrameField(UNKNOWN, "default", "low")  # one side wrote it, but the heading does not say which
	elif f.document_kind.known:
		f.author = FrameField("court", "header", "high")

	# standard of review
	sm = _STANDARD_STATED.search(body_text or "")
	if sm:
		word = (sm.group(1) or sm.group(2) or "").lower()
		f.standard_of_review = FrameField(word, "text", "medium")
	elif f.proceeding.value in ("judicial_review",):
		f.standard_of_review = FrameField("reasonableness", "default", "low")

	# layers (plan names L0..L3)
	layers = ["L0 judge"]
	if f.proceeding.value in ("judicial_review", "appeal", "motion"):
		layers.append("L1 parties before the court")
	if f.earlier_decision_maker.known:
		layers.append("L2 earlier decision maker")
		layers.append("L3 first-instance parties as reported")
	elif f.proceeding.value == "direct":
		layers.append("L1 parties before this tribunal")
	f.layers_present = layers

	if f.earlier_decision_maker.known and f.proceeding.value in ("judicial_review", "appeal"):
		who = _label(f.earlier_decision_maker.value)
		how = "procedurally fair" if _FAIRNESS.search(intro) and f.standard_of_review.value != "reasonableness" else (
			"correct" if f.standard_of_review.value == "correctness" else "reasonable")
		about = f" about {f.subject.value}" if f.subject.known else ""
		f.question = f"The question is whether the {who}'s decision{about} was {how}."
	dm2 = _DISPOSITION.search(body_text[-3000:] if body_text else "")
	if dm2:
		f.disposition = (dm2.group(1) or "stated").lower()
	return f
