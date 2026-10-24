"""Pass 1 of the argument breakdown: a plain "what is this case" frame, built before any paragraph is classified.

``case_frame.build_frame`` answers the court, the kind of proceeding, the earlier decision maker and which side the
Minister is on. This adds what a reader needs to follow the arguments: the parties as people, the levels the case
has been through and their dates and outcomes, what the case is about, the issues the court says it will decide
and the arguments each side is reported as making. Regular expressions only: no model, no network, no database.

Every item carries the paragraph number it came from so a reader (or a grader) can check it against the text.
Nothing is guessed: an item that cannot be found is left out or ``unknown``.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any, Sequence

from backend.case_frame import CaseFrame, UNKNOWN, build_frame

FRAME_PLUS_VERSION = "frame_plus_v1"

_TITLE_PREFIX = re.compile(r"^(?:mr|ms|mrs|miss|mme|madam|dr)\.?\s+", re.I)
_MONTH = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
_DATE = rf"(?:{_MONTH}\s+\d{{1,2}},?\s+\d{{4}}|\d{{4}}-\d{{2}}-\d{{2}})"

# level key -> (pattern for a mention of that decision, label)
_LEVELS = (
	("officer", r"(?:visa |immigration |senior immigration |PRRA |H&C |senior |processing |pre-removal risk assessment |enforcement )?"
		r"(?:officer|officers)\b|\bvisa office\b|\bdelegate\b|\bCitizenship Judge\b", "officer or delegate"),
	("id", r"\bImmigration Division\b|\bID\b(?= member| decision)", "Immigration Division"),
	("rpd", r"\bRefugee Protection Division\b|\bRPD\b", "Refugee Protection Division"),
	("iad", r"\bImmigration Appeal Division\b|\bIAD\b", "Immigration Appeal Division"),
	("rad", r"\bRefugee Appeal Division\b|\bRAD\b", "Refugee Appeal Division"),
	("fc", r"\bFederal Court\b(?! of Appeal)", "Federal Court"),
	("fca", r"\bFederal Court of Appeal\b", "Federal Court of Appeal"),
	("tribunal", r"\b(?:Tribunal|Board|Commission|Chairperson|Adjudicator)\b", "other tribunal"),
	("lower_court", r"\b(?:trial judge|application judge|motions? judge|Prothonotary|Superior Court|Court of (?:King|Queen)['’]s Bench|Provincial Court|Tax Court|Trial Division|Court of Justice|Cour (?:sup[ée]rieure|du Qu[ée]bec))\b", "lower court"),
	("provincial_ca", r"\b(?:Court of Appeal for [A-Z]\w+(?: [A-Z]\w+)?|(?:Ontario|British Columbia|Alberta|Quebec|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland and Labrador) Court of Appeal|Cour d['’]appel(?: du Qu[ée]bec)?|(?<!Federal )Court of Appeal)\b", "provincial court of appeal"),
)
_LEVEL_RX = tuple((k, re.compile(p), lab) for k, p, lab in _LEVELS)
_RANK = {"officer": 0, "id": 0, "rpd": 0, "tribunal": 0, "iad": 1, "rad": 1, "fc": 2, "lower_court": 2, "fca": 3, "provincial_ca": 3, "scc": 4}

_DECIDED = re.compile(
	r"(?:decision|determination|refusal|reasons|order|judgment)s?\s+(?:of|by|from)\s+(?:the\s+|a\s+|an\s+)?(?P<who>[^.,;()]{3,80}?)"
	rf"(?:\s*\([^)]{{1,30}}\))?(?:,?\s+(?:dated|made|rendered|issued|on)\s+(?P<date>{_DATE}))?", re.I)
_POSS = re.compile(
	rf"(?P<who>(?:the\s+)?(?:\w+\s+){{0,2}}(?:officer|RPD|RAD|IAD|ID|Board|Member|Panel|Tribunal|Commission|delegate|Citizenship Judge|Federal Court|Court of Appeal)['’]s)"
	rf"\s+(?:decision|refusal|determination|reasons|finding)(?:[^.]{{0,40}}?(?:dated|of)\s+(?P<date>{_DATE}))?", re.I)
_OUTCOME = re.compile(
	r"\b(rejected|refused|dismissed|allowed|granted|confirmed|upheld|set aside|found|determined|concluded|denied|approved|issued|ordered)\b"
	r"(?:\s+(?:the|her|his|their|an?)\s+)?(?P<what>[^.;]{0,100})", re.I)

_SUBJECTS = (
	("refugee protection claim", r"\bsections? 96\b|\bs\.? 96\b|\bConvention refugee\b|\bperson in need of protection\b|refugee protection|claim for refugee|refugee claim"),
	("humanitarian and compassionate application", r"humanitarian and compassionate|\bH&C\b|\bs\.? 25(?:\(1\))?\b|section 25"),
	("pre-removal risk assessment", r"pre-removal risk assessment|\bPRRA\b"),
	("misrepresentation finding", r"misrepresentation|\bs\.? 40\b|section 40 of"),
	("criminal inadmissibility", r"criminality|\bs\.? 36\b|section 36 of|serious criminality"),
	("security or human-rights inadmissibility", r"\bs\.? 34\b|section 34 of|\bs\.? 35\b|section 35 of|crimes against humanity|\bs\.? 37\b|organized crime"),
	("spousal or family sponsorship", r"sponsor|common-law partner|conjugal|family class|genuine(?:ness)? of the (?:marriage|relationship)|spousal"),
	("study permit", r"study permit|student permit|permis d['’]études"),
	("work permit", r"work permit|\bLMIA\b|labour market impact|permis de travail|\bIEC\b|post-graduation work"),
	("temporary resident visa", r"temporary resident visa|\bTRV\b|visitor visa|visa de r[ée]sident temporaire"),
	("permanent residence application", r"permanent residen(?:ce|t) (?:application|visa)|express entry|skilled worker|provincial nominee|\bPNP\b|\bCEC\b|Canadian Experience Class"),
	("citizenship", r"Citizenship Act|citizenship (?:application|judge)|revocation of citizenship"),
	("removal or stay of removal", r"stay of (?:the )?removal|removal order|deportation order|exclusion order|departure order|removal from Canada"),
	("detention review", r"detention review|\bdetention\b|release from detention"),
	("residency obligation appeal", r"residency obligation|section 28 of"),
	("cessation or vacation of refugee status", r"cessation|vacat(?:ion|e) of (?:the )?(?:refugee|protected)|ceased to be a (?:Convention )?refugee"),
	("immigration appeal (visa refusal, removal order)", r"\bsponsorship appeal\b|appeal from a refusal of a sponsorship|appeal.{0,40}removal order"),
)
_SUBJECT_RX = tuple((k, re.compile(p, re.I)) for k, p in _SUBJECTS)

_ISSUE_HEAD = re.compile(r"\b(?:issues?|questions?)\b[^.]{0,80}?\b(?:are|is|raised|follow|arise|arises|to be decided|for determination)\b|"
	r"\bI would frame the\b|\bthe following (?:issues?|questions?)\b|\bdeterminative issue\b|\bdispositive issue\b", re.I)
_ISSUE_ITEM = re.compile(r"^\s*(?:\(?[a-z0-9ivx]{1,4}[.)]|[•\-–])\s+\S")
_ARG = re.compile(
	r"(?P<who>\b(?:the\s+)?(?:applicants?|appellants?|claimants?|respondents?|ministers?|minister['’]s counsel|counsel for the \w+|plaintiffs?|"
	r"defendants?|interveners?|Mr\.\s+\w+|Ms\.\s+\w+|Mrs\.\s+\w+|Mme\s+\w+|M\.\s+\w+)\b)[^.]{0,50}?\b"
	r"(?:argues?|argued|submits?|submitted|contends?|contended|says|alleges?|alleged|asserts?|asserted|maintains?|"
	r"claims?|claimed|raises?|raised|takes issue|challenges?|challenged|relies on|disagrees?|states|stated|requests|seeks)\b", re.I)
_RESP = re.compile(r"respondent|minister|attorney general|crown|defendant|intim[ée]", re.I)
_CITIZEN_OF = re.compile(r"\b(?:a |an )?(?:citizen|national|native|resident) of (?P<c>[A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)?)")


@dataclass
class Level:
	level: str  # rpd, rad, officer, fc, ...
	label: str
	date: str = ""
	outcome: str = ""
	para: int = 0  # printed paragraph number the mention came from (0 = header)


@dataclass
class Argument:
	side: str  # applicant | respondent | court
	text: str
	para: int


_CHALLENGE = re.compile(
	r"\b(?:erred|err(?:s|ed)? in|made (?:a |an )?(?:reviewable )?error|unreasonabl[ey]|fail(?:ed|s|ure) to|breach(?:ed)? (?:of )?(?:the )?(?:procedural )?fairness|"
	r"(?:was|were|is|are) (?:not )?(?:procedurally )?(?:unfair|unreasonable|incorrect|wrong)|ignored|misapprehended|misconstrued|misinterpreted|"
	r"challenges?|challenged|takes issue|contests?|seeks? (?:judicial review|to set aside)|appeals?\b)", re.I)
_FINDING_TOPICS = (
	("credibility", r"credib|implausib|inconsisten|contradict"),
	("internal flight alternative", r"internal flight|\bIFA\b"),
	("state protection", r"state protection|adequa(?:te|cy) of (?:state )?protection"),
	("procedural fairness", r"procedural fairness|natural justice|duty of fairness|reasonable apprehension of bias|\bbias\b|right to be heard"),
	("humanitarian factors (establishment, best interests of the child, hardship)", r"best interests|establishment|hardship|humanitarian"),
	("risk assessment", r"\brisk\b|persecution|well-founded fear|section 97|\bs\.? 97\b"),
	("genuineness of relationship", r"genuine|bona fide|marriage of convenience|relationship"),
	("inadmissibility finding", r"inadmissib|misrepresent|criminal|security"),
	("evidence assessment", r"\bevidence\b|document|affidavit|new evidence"),
	("legal test or statutory interpretation", r"interpret|legal test|statutory|\bsection \d+|\bs\.? \d+"),
	("sufficiency of reasons", r"adequa(?:te|cy) of (?:the )?reasons|insufficient reasons|inadequate reasons|failed to explain"),
	("admissibility of new evidence on appeal", r"new evidence|subsection 110\(4\)|\bs\.? 110\(4\)"),
	("oral hearing request", r"oral hearing"),
	("residence or presence requirement", r"residen|physical presence"),
)
_FINDING_RX = tuple((k, re.compile(p, re.I)) for k, p in _FINDING_TOPICS)
_NEUTRAL = re.compile(r"\b(\d{4})\s+(FC|FCA|SCC|CanLII|IRB|RPD|RAD|SAR)\s+(\d+)\b")


@dataclass
class Challenge:
	target: str  # level key of the decision being challenged
	topics: list[str]
	text: str
	para: int


@dataclass
class FramePlus:
	version: str = FRAME_PLUS_VERSION
	base: dict[str, Any] = field(default_factory=dict)  # the case_frame.CaseFrame as a dict
	forum: str = UNKNOWN
	proceeding: str = UNKNOWN
	applicant: str = ""  # the person or party who brings the case, as named in the decision
	applicant_role: str = UNKNOWN  # individual | minister | other
	respondent: str = ""
	respondent_role: str = UNKNOWN
	origin_country: str = ""
	subject: str = UNKNOWN
	levels: list[Level] = field(default_factory=list)  # lowest first, ending with this decision
	disposition: str = UNKNOWN
	issues: list[Argument] = field(default_factory=list)
	arguments: list[Argument] = field(default_factory=list)
	determinative: str = ""
	challenged: list[Challenge] = field(default_factory=list)  # which part of the earlier decision is attacked
	challenged_decision: str = ""  # neutral citation of the decision under challenge, when the text gives one

	def to_dict(self) -> dict[str, Any]:
		return asdict(self)

	def text(self) -> str:
		out = []
		if self.applicant and self.respondent:
			out.append(f"{self.applicant} ({self.applicant_role}) v. {self.respondent} ({self.respondent_role}).")
		if self.subject != UNKNOWN:
			out.append(f"About: {self.subject}.")
		if self.levels:
			out.append("Levels: " + " -> ".join(l.label + (f" ({', '.join(x for x in (l.date, l.outcome) if x)})" if (l.date or l.outcome) else "") for l in self.levels) + ".")
		if self.challenged:
			target = next((l.label for l in self.levels if l.level == self.challenged[0].target), "the earlier decision")
			out.append(f"Challenges the {target}" + (f" ({self.challenged_decision})" if self.challenged_decision else "")
				+ ": " + "; ".join(sorted({t for c in self.challenged for t in c.topics})) + ".")
			for c in self.challenged[:3]:
				out.append(f"  challenged [{c.para}]: {c.text}")
		for i in self.issues:
			out.append(f"Issue [{i.para}]: {i.text}")
		for a in self.arguments:
			out.append(f"{a.side.title()} [{a.para}]: {a.text}")
		return "\n".join(out)


def _clean_name(name: str) -> str:
	name = re.sub(r"\s+", " ", name or "").strip(" ,.;")
	name = re.sub(r"\b(?:et al\.?|and others)$", "", name, flags=re.I).strip(" ,")
	return name


def _role(name: str) -> str:
	if re.search(r"minister|attorney general|his majesty|the king|the queen|canada\s*\(|public safety|border services|procureur|ministre", name, re.I):
		return "minister"
	if re.search(r"\b(?:inc|ltd|limited|corp|corporation|company|commission|society|union|association|city|board|bank|canada|council|college|authority|syndicat|soci[ée]t[ée]|ville)\b\.?", name, re.I):
		return "organization"
	return "individual" if name else UNKNOWN


def _sentences(text: str) -> list[str]:
	return [s.strip() for s in re.split(r"(?<=[.?!;])\s+(?=[A-Z“\"(])", text) if s.strip()]


def _level_of(who: str) -> tuple[str, str] | None:
	for key, rx, label in _LEVEL_RX:
		if rx.search(who):
			return key, label
	return None


_OUTCOME_WORDS = (
	("rejected", r"reject(?:ed|ing|s)?|not a (?:convention )?refugee|neither a convention refugee"),
	("refused", r"refus(?:ed|ing|al|es)"),
	("dismissed", r"dismiss(?:ed|ing|es)"),
	("denied", r"den(?:ied|ying|ies)"),
	("allowed", r"allow(?:ed|ing|s)"),
	("granted", r"grant(?:ed|ing|s)"),
	("accepted", r"accept(?:ed|ing)|is a convention refugee"),
	("confirmed", r"confirm(?:ed|ing|s)|upheld|upholding"),
	("set aside", r"set aside|quash(?:ed|ing)|overturn(?:ed|ing)"),
	("found inadmissible", r"inadmissible|inadmissib"),
	("approved", r"approv(?:ed|ing)"),
)
_OUTCOME_RX = tuple((k, re.compile(r"\b(?:%s)\b" % p, re.I)) for k, p in _OUTCOME_WORDS)
_DATE_RX = re.compile(_DATE)
_DATE_NEAR = re.compile(rf"(?:dated|of|on|made|rendered|issued)\s+({_DATE})|\(({_DATE})\)|,\s*({_DATE})")


def _short_outcome(text: str) -> str:
	best = None
	for key, rx in _OUTCOME_RX:
		m = rx.search(text)
		if m and (best is None or m.start() < best[0]):
			best = (m.start(), key, text[m.start():m.start() + 70])
	if not best:
		return ""
	return re.sub(r"\s+", " ", best[2]).strip(" ,;.")


def _mentions(sentence: str):
	"""(level key, label, position after the mention) for each earlier-decision mention in a sentence."""
	for key, rx, label in _LEVEL_RX:
		for m in rx.finditer(sentence):
			before = sentence[max(0, m.start() - 70):m.start()]
			after = sentence[m.end():m.end() + 160]
			if re.search(r"decision|determination|refusal|reasons|judgment|order|finding|appeal(?:ed|ing|s)? (?:to|from|of)|review of|rejected|refused|dismissed|confirmed|found|concluded|held|denied", before + after[:60], re.I):
				yield key, label, m.end()


def _extract_levels(paragraphs: Sequence[str], numbers: Sequence[int], frame: CaseFrame, forum: str, this_date: str, disposition: str, header: str = "") -> list[Level]:
	found: dict[str, Level] = {}
	limit = min(len(paragraphs), 14)
	for idx in range(limit):
		for sentence in _sentences(paragraphs[idx][:3000]):
			for key, label, end in _mentions(sentence):
				if key == forum:
					continue
				after = sentence[end:end + 200]
				dm = _DATE_NEAR.search(after[:110])
				date = next((g for g in dm.groups() if g), "") if dm else ""
				rest = after[dm.end():] if dm else after
				outcome = _short_outcome(rest[:45]) if re.match(r"[\s,;]*(?:and\s+)?(?:which\s+|that\s+)?(?:reject|refus|dismiss|den|allow|grant|confirm|found|conclud|determin|approv|upheld|set aside|quash)", rest, re.I) else ""
				cur = found.get(key)
				if cur is None:
					found[key] = Level(key, label, date, outcome, numbers[idx])
				else:
					cur.date = cur.date or date
					cur.outcome = cur.outcome or outcome
	m = re.search(r"On appeal from ([^\n.]{5,120})", header or "", re.I)
	if m:
		for key, label, _ in _mentions("the decision of " + m.group(1)):
			if key != forum and key not in found:
				found[key] = Level(key, label, "", "", 0)
	edm = frame.earlier_decision_maker.value
	if edm != UNKNOWN and edm not in found and edm not in ("judge",):
		found[edm] = Level(edm, next((lab for k, _, lab in _LEVELS if k == edm), edm), "", "", 0)
	levels = sorted(found.values(), key=lambda l: (_RANK.get(l.level, 0), l.para))
	levels.append(Level(forum, {"fc": "Federal Court", "fca": "Federal Court of Appeal", "scc": "Supreme Court of Canada",
		"rpd": "Refugee Protection Division", "rad": "Refugee Appeal Division", "iad": "Immigration Appeal Division",
		"id": "Immigration Division"}.get(forum, forum), this_date, disposition, 0))
	return levels


def _subject(intro: str) -> str:
	if not re.search(r"Immigration and Refugee Protection Act|IRPA|Citizenship Act|Immigration Act|Convention refugee|refugee protection|\bIRCC\b|Citizenship and Immigration|immigration|Refugee", intro):
		return "not an immigration matter"
	scores = []
	for key, rx in _SUBJECT_RX:
		hits = rx.findall(intro)
		if hits:
			first = rx.search(intro).start()
			scores.append((-len(hits), first, key))
	if not scores:
		return UNKNOWN
	scores.sort()
	return scores[0][2]


_HEADING = re.compile(r"^\s*(?:[IVX]+\.|[A-Z]\.|\d+\.)?\s*(?:the\s+)?(?:issues?|questions? (?:in issue|at issue|to be decided)|grounds? of (?:appeal|review)|the issue)\b[:.]?\s*", re.I)
_KIND = r"(?:determinative|dispositive|decisive|central|main|key)\s+(?:issue|question)s?"
_DETERMINATIVE = re.compile(
	rf"(?:\b{_KIND}\b(?:\s+(?:in|on|for|of) (?:this|the) (?:appeal|case|claim|application|matter|motion))?(?:,?\s*(?:which\s+)?(?:is|are|being|was|were)|:|\s+is)\s+(?P<a>[^.;]{{5,170}}))|"
	rf"(?:(?P<b>[A-Z][^.;]{{4,140}}?)\s+(?:is|are|was|were)\s+(?:the|a)\s+{_KIND}\b)", re.I)
_SKIP_ISSUE = re.compile(r"^(?:again|however|therefore|here|thus|in my view|i (?:find|note|will)|the (?:panel|rpd|rad|officer) (?:finds?|notes?|did))\b|\bno issues?\b|\bhas not (?:raised|made)\b", re.I)


def _clip(text: str, n: int = 230) -> str:
	return re.sub(r"^\[\d+\]\s*", "", re.sub(r"\s+", " ", text)).strip()[:n]


def _issues(paragraphs: Sequence[str], numbers: Sequence[int]) -> list[Argument]:
	out: list[Argument] = []
	n = len(paragraphs)
	head = min(n, max(10, n // 3))
	# 1. a paragraph that introduces the issues, with the issues listed in it or in the short paragraphs after it
	for i in range(head):
		text = paragraphs[i]
		m = _HEADING.match(text) or (ISSUE_INLINE.search(text) if len(text) < 1800 else None)
		if not m:
			continue
		body = text[m.end():] if _HEADING.match(text) else text[m.start():]
		parts = [x.strip() for x in re.split(r"\n+|(?<=[.?;:])\s+(?=\(?(?:[a-z]|\d{1,2}|[ivx]{1,4})[.)]\s)|\s(?=\((?:[a-z]|\d{1,2}|[ivx]{1,4})\)\s)", body) if len(x.strip()) > 25]
		items = [x for x in parts if not _SKIP_ISSUE.search(x)][:5]
		for j in range(i + 1, min(n, i + 6)):
			t = paragraphs[j]
			if len(t) < 320 and (t.rstrip().endswith("?") or re.match(r"\s*(?:\(?[a-z0-9ivx]{1,4}[.)]\s|Whether|Was|Did|Is|Does|Should|Were|Are|Can|Has|Do)\b", t)):
				items.append(t)
			elif len(t) >= 320:
				break
		for it in items[:6]:
			out.append(Argument("court", _clip(it), numbers[i]))
		if out:
			return out[:6]
	# 2. a sentence naming the determinative issue
	for i in range(min(n, 30)):
		m = _DETERMINATIVE.search(paragraphs[i][:2500])
		if m:
			out.append(Argument("court", _clip(m.group("a") or m.group("b")), numbers[i]))
			break
	return out


ISSUE_INLINE = re.compile(r"\b(?:the (?:following |two |three |four |main )?(?:issues?|questions?) (?:raised |on this (?:application|appeal) |in this (?:application|appeal) )?(?:are|is|arises?|arise)|raises? the (?:following )?(?:issues?|questions?)|I would frame the)\b", re.I)

_ARG_VERB = (r"(?:argues?|argued|submits?|submitted|contends?|contended|asserts?|asserted|maintains?|maintained|alleges?|alleged|"
	r"takes? the position|is of the view|position is that|says that|raises? (?:the following|\w+ (?:arguments?|grounds?|issues?))|"
	r"relies on the (?:argument|submission)|disagrees? (?:with|that)|takes issue with|challenges?|challenged|requests? that|asks? (?:this|the) (?:Court|Division))")
_ARG_SUBJECT = (r"(?P<who>(?:the\s+)?(?:applicants?|appellants?|claimants?|respondents?|ministers?|minister['’]s counsel|intervener|plaintiffs?|defendants?|"
	r"counsel for (?:the )?\w+|(?:Mr|Ms|Mrs|Mme|M)\.?\s+[A-Z]\w+|[A-Z]\w+(?: [A-Z]\w+){0,3})(?:['’]s (?:counsel|position|submissions?|argument))?)")
_ARG_RE = re.compile(_ARG_SUBJECT + r"\s+(?:also |further |first |next |now |essentially |primarily |mainly |generally |additionally )?" + _ARG_VERB, re.I)
_POSITION_RE = re.compile(r"(?P<who>(?:the\s+)?(?:applicants?|appellants?|claimants?|respondents?|ministers?))['’]s\s+(?:position|submissions?|argument|case|contention)", re.I)
_COURT_SUBJECT = re.compile(r"^\W*(?:the )?(?:panel|court|tribunal|board|member|officer|rpd|rad|iad|judge|commission)\b|^\W*i\b|^\W*we\b", re.I)
_FACTS_ONLY = re.compile(r"seeks? judicial review|applies? for judicial review|is (?:a )?(?:citizen|national) of|alleged the following|following (?:allegations|events|facts)|arrived in Canada|was born", re.I)
_ARG_SECTION = re.compile(r"\b(?:positions? of the parties|parties[’'] (?:positions?|submissions)|submissions|arguments?|applicant[’']s (?:position|submissions)|appellant[’']s (?:position|submissions))\b", re.I)


def _side_of(who: str, applicant: str, forum: str) -> str:
	w = who.lower()
	if re.search(r"respondent|minister|attorney general|crown|defendant|intim", w):
		return "respondent"
	if re.search(r"applicant|appellant|claimant|plaintiff|counsel for (?:the )?(?:applicant|appellant)", w):
		return "applicant"
	if applicant and any(t in w for t in {x.lower() for x in re.findall(r"[A-Za-z]{4,}", applicant)}):
		return "applicant"
	return ""


def _arguments(paragraphs: Sequence[str], numbers: Sequence[int], frame: CaseFrame, applicant: str) -> list[Argument]:
	out: list[Argument] = []
	counts = {"applicant": 0, "respondent": 0}
	forum = frame.court.value
	for i, text in enumerate(paragraphs):
		if len(text) > 4000:
			text = text[:4000]
		for sentence in _sentences(text):
			if len(sentence) < 70 or _FACTS_ONLY.search(sentence) or sentence.lstrip("[]0123456789 ").startswith(("\"", "“", "In ")):
				continue
			sentence = re.sub(r"^\W*\[\d+\]\s*", "", sentence)
			m = _ARG_RE.search(sentence) or _POSITION_RE.search(sentence)
			if not m or m.start() > 12:
				continue
			if _COURT_SUBJECT.match(sentence[m.start():]):
				continue
			side = _side_of(m.group("who"), applicant, forum)
			if not side or counts[side] >= 5:
				continue
			# the sentence must say what is argued: a "that" clause, a colon, or an error/relief claim
			tail = sentence[m.end():]
			if not re.search(r"\bthat\b|:|\berr|unreasonabl|\bfail|\bbreach|\bshould|\bmust|\bwas not|\bwere not|\bis not|\bno basis|\bmisappre|\bignor|\bwithout\b|\bcorrect", tail, re.I):
				continue
			counts[side] += 1
			out.append(Argument(side, _clip(sentence, 260), numbers[i]))
	return sorted(out, key=lambda a: a.para)


_ERR = re.compile(r"\berr|unreasonabl|\bfail|\bbreach|unfair|\bmisappre|\bmisconstru|\bignor|\bflaw|\bwrong|incorrect|\bunsupported|no basis|\bwithout (?:regard|considering|explain)|\binadequate|\bperverse|\bcapricious", re.I)
_LOWER_CITE = re.compile(r"(?:decision|judgment|order|reasons|ruling)[^.()]{0,60}?(?:\(|, |of the [A-Z][^.()]{0,40}\s+)?(?:\(|\[)?(\d{4}\s+(?:FC|FCA|ONCA|BCCA|ABCA|QCCA|CanLII|SCC)\s+\d+)", re.I)


def _challenged(paragraphs: Sequence[str], numbers: Sequence[int], levels: list[Level], forum: str, arguments: list[Argument],
		applicant_role: str) -> tuple[list[Challenge], str]:
	"""Which part of the decision below the challenging side attacks, from that side's argued errors."""
	earlier = [l for l in levels if l.level != forum]
	if not earlier:
		return [], ""
	target = earlier[-1].level
	challenger = "respondent" if applicant_role == "minister" else "applicant"
	out: list[Challenge] = []
	for a in arguments:
		if a.side != challenger or not _ERR.search(a.text):
			continue
		topics = [k for k, rx in _FINDING_RX if rx.search(a.text)]
		out.append(Challenge(target, topics[:3] or ["general"], a.text, a.para))
	cite = ""
	for text in paragraphs[:6]:
		for sentence in _sentences(text[:3000]):
			if re.search(r"appeal|judicial review|Federal Court|Court of Appeal", sentence, re.I):
				m = _LOWER_CITE.search(sentence)
				if m:
					cite = re.sub(r"\s+", " ", m.group(1))
					break
		if cite:
			break
	return out[:5], cite


_DISP_PATTERNS = (
	(re.compile(r"\bI\s+(?:hereby\s+)?(dismiss|allow|reject|refuse|grant|accept|confirm|set aside)\b|\bwe\s+(?:would\s+)?(dismiss|allow)\b|\bI would (dismiss|allow)\b", re.I), None),
	(re.compile(r"\b(?:application|appeal|motion|claim|request|stay)\b[^.]{0,50}?\b(?:is|are|will be|must be|shall be|should be|be)\s+(dismissed|allowed|granted|refused|rejected|denied)(\s+in part)?", re.I), None),
	(re.compile(r"\b(?:is|am|are)\s+(not\s+)?a\s+Convention refugee|\b(?:is|am)\s+(not\s+)?a person in need of protection", re.I), "refugee"),
)
_VERB_FORM = {"dismiss": "dismissed", "allow": "allowed", "reject": "rejected", "refuse": "refused", "grant": "granted", "accept": "accepted",
	"confirm": "confirmed", "set aside": "set aside"}


def _disposition(paragraphs: Sequence[str]) -> str:
	zones = list(paragraphs[:4]) + list(paragraphs[-7:])
	for text in zones:
		for rx, kind in _DISP_PATTERNS:
			m = rx.search(text)
			if not m:
				continue
			if kind == "refugee":
				return "rejected (not a Convention refugee)" if m.group(1) else "accepted (Convention refugee or person in need of protection)"
			word = next(g for g in m.groups() if g and g.strip().lower() not in ("in part",))
			word = _VERB_FORM.get(word.lower(), word.lower())
			return word + (" in part" if re.search(r"in part", m.group(0), re.I) else "")
	return ""


def _this_date(header: str) -> str:
	m = re.search(r"Date of [Dd]ecision\s*\n?\s*(" + _DATE + ")", header or "") or re.search(r"\nDate\s*\n\s*(\d{4}-\d{2}-\d{2})", header or "") or re.search(r"Date:\s*(\d{8})", header or "")
	return m.group(1) if m else ""


def build_frame_plus(header: str, body: str, paragraphs: Sequence[str], numbers: Sequence[int], *, case_type: str | None = None) -> FramePlus:
	"""The pass-1 frame. ``paragraphs``/``numbers`` are the printed paragraphs and their numbers."""
	base = build_frame(header, body, case_type=case_type)
	fp = FramePlus(base=base.to_dict())
	fp.forum = base.court.value
	fp.proceeding = base.proceeding.value
	intro = "\n".join(paragraphs[:12])[:6000] if paragraphs else (body or "")[:6000]

	a, r = _clean_name(base.applicant_name), _clean_name(base.respondent_name)
	if a:
		fp.applicant, fp.respondent = a, r
		fp.applicant_role, fp.respondent_role = _role(a), _role(r)
	elif fp.forum in ("rpd", "rad", "iad", "id"):
		# anonymised tribunal decisions: the person is the claimant or appellant; the Minister may intervene
		role = {"rpd": "claimant", "rad": "appellant", "iad": "appellant", "id": "person concerned"}[fp.forum]
		fp.applicant, fp.applicant_role = f"the {role}", "individual"
		fp.respondent, fp.respondent_role = ("the Minister", "minister") if fp.forum in ("rad", "iad", "id") else ("", UNKNOWN)
	m = _CITIZEN_OF.search(intro[:2500])
	if m:
		fp.origin_country = m.group("c")
	fp.subject = base.subject.value if base.subject.known else _subject(intro[:3500])
	fp.levels = _extract_levels(paragraphs, numbers, base, fp.forum, _this_date(header), _disposition(paragraphs), header)
	fp.disposition = _disposition(paragraphs) or (base.disposition if base.disposition not in ("stated", UNKNOWN) else "")
	fp.issues = _issues(paragraphs, numbers)
	fp.arguments = _arguments(paragraphs, numbers, base, fp.applicant)
	fp.challenged, fp.challenged_decision = _challenged(paragraphs, numbers, fp.levels, fp.forum, fp.arguments, fp.applicant_role)
	return fp


def frame_matches_text(frame: dict[str, Any], full_text: str) -> bool:
	"""Guard for model-written frames: false when the frame looks like it was written for a different decision.

	A swapped frame (one extractor call writing another decision's frame) names parties and dates that never
	appear in the text. Checks that most of the frame's party-name words, quoted dates and paragraph numbers
	are found in the decision. Anonymised names (XXXX) are skipped; with nothing checkable the frame passes.
	"""
	text = (full_text or "").lower()
	parties = frame.get("parties") or {}
	# Notes in brackets ("(anonymized appellant, citizen of China)") are the writer's words, not names.
	names = [re.sub(r"\([^)]*\)", " ", str(parties.get(key) or "")) for key in ("applicant", "respondent")]
	words = {w.lower() for name in names for w in re.findall(r"[A-Za-z]{5,}", name)}
	words -= {"anonymized", "anonymised", "counsel", "appeared", "submissions", "reported", "minister", "citizenship", "immigration", "canada", "applicant", "respondent", "appellant", "claimant", "individual", "organization", "redacted", "refugee"}
	checks = [w in text for w in words]
	for level in frame.get("levels") or []:
		date = str(level.get("date") or "")
		year = re.search(r"\b(?:19|20)\d{2}\b", date)
		if year:
			checks.append(year.group(0) in text)
	paras = [p.get("para") for key in ("arguments", "issues", "challenged") for p in (frame.get(key) or []) if isinstance(p.get("para"), int)]
	max_para = max((int(m) for m in re.findall(r"\[(\d{1,3})\]", full_text or "")), default=0)
	if paras and max_para:
		checks.append(max(paras) <= max_para + 1)
	return not checks or sum(checks) / len(checks) >= 0.6
