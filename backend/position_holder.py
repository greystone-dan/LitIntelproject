"""Deterministic "whose position is this paragraph reporting" rules.

The judge or member is always the author. What this module tags is *whose view* a
sentence reports: the applicant/claimant, the respondent/Minister, the earlier decision
maker (officer, RPD, RAD, IAD, a lower-court judge), the court or tribunal itself, a
prior court or other authority (case law, statute), or a witness/document.

Everything is plain regular expressions. Nothing here calls a model, a network service
or a database. A case header reader (``parse_parties``) keeps the sides straight when the
Minister is the applicant/appellant (for example ``Minister of Citizenship and
Immigration v. X``).

Each hit is a ``Cue`` with the holder, the matched phrase and a confidence of
``explicit`` (a named cue was found) or ``carried`` (the sentence has no cue of its own and
continues a run of submissions) or ``default`` (nothing found, so the court's own voice).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable

APPLICANT = "applicant"
RESPONDENT = "respondent"
EARLIER = "earlier_decision_maker"
COURT = "court"
AUTHORITY = "prior_court_or_authority"
WITNESS = "witness_or_document"

HOLDERS = (APPLICANT, RESPONDENT, EARLIER, COURT, AUTHORITY, WITNESS)

# ---------------------------------------------------------------------------
# Case header
# ---------------------------------------------------------------------------

_GOV_FIRST = re.compile(
	r"^\s*(?:the\s+)?(?:minister\b|canada\s*\((?:minister|public safety|attorney|citizenship|immigration|"
	r"national revenue|border services)|attorney general|his majesty|the king|the queen|ministre|"
	r"public safety|canada border services|canada \(c\.?b\.?s\.?a)", re.I)
_GOV_ANY = re.compile(
	r"minister|attorney general|canada\s*\(|public safety|border services|his majesty|the king|the queen", re.I)
_CORP_WORDS = re.compile(r"\b(?:inc|ltd|ltée|co|corp|corporation|limited|llc|lp|s\.?e\.?n\.?c\.?)\.?$", re.I)


@dataclass
class Parties:
	"""Who is who in the header. ``first`` and ``second`` are the title sides."""
	first: str = ""
	second: str = ""
	minister_first: bool = False
	aliases_first: tuple[str, ...] = ()
	aliases_second: tuple[str, ...] = ()
	# True (default): "applicant" always means the individual/private party and "respondent" the
	# Minister/government, even when the title puts the Minister first. False: use the literal words.
	normalize: bool = True


def _aliases(name: str) -> tuple[str, ...]:
	"""Short names the decision may use for a party ("Lemay Co Inc." -> "Lemay")."""
	name = re.sub(r"\([^)]*\)", " ", name)
	name = re.sub(r"\s+", " ", name).strip(" ,.")
	if not name or _GOV_ANY.search(name):
		return ()
	out = {name}
	tokens = [t for t in re.split(r"[\s,]+", name) if t]
	while tokens and _CORP_WORDS.search(tokens[-1]):
		tokens = tokens[:-1]
	if tokens:
		out.add(" ".join(tokens))
		out.add(tokens[0] if len(tokens[0]) > 2 else " ".join(tokens))
		if len(tokens) > 1:
			out.add(tokens[-1])
	return tuple(sorted((a for a in out if len(a) > 2 and a.lower() not in {"the", "and", "his", "her"}),
		key=len, reverse=True))


def parse_parties(title: str) -> Parties:
	"""Read ``A v. B`` from the first header line (or the first line of the text)."""
	line = (title or "").strip().splitlines()[0] if (title or "").strip() else ""
	m = re.split(r"\s+(?:v\.?|c\.|vs\.?)\s+", line, maxsplit=1)
	if len(m) != 2:
		return Parties()
	first, second = m[0].strip(), m[1].strip()
	return Parties(first=first, second=second, minister_first=bool(_GOV_FIRST.match(first)),
		aliases_first=_aliases(first), aliases_second=_aliases(second))


# ---------------------------------------------------------------------------
# Cue vocabulary
# ---------------------------------------------------------------------------

_ARGUE = (r"(?:submit|argu(?:e)?|contend|say|state|allege|claim|assert|maintain|emphasi[sz]e|stress|point out|"
	r"suggest|dispute|object|respond|reply|insist|plead|urge|add|reassert|seek|opine|make the point|makes the point|"
	r"take the position|takes the position|"
	r"concede|acknowledge|admit|also submit|further submit|contest|complain|testif|swear|swore|rely|relies)")
_ARGUE_RE = re.compile(r"(?!submit(?:s|ted)?\s+(?:an?|his|her|their|the|its|three|two|four|\d+)\s+(?:\w+\s+)?"
	r"(?:application|request|grievance|claim|appeal|document|evidence|form|letter|response|motion|notice|"
	r"complaint|affidavit|package|submissions?\s+to)\b)(?:%s)(?:s|es|ed|d|ted|ting|ied|ies|ing)?\b" % _ARGUE, re.I)

_APPL_NOUN = (r"(?:the\s+|an?\s+)?(?:(?:principal|co-|co|main|lead)\s+)?"
	r"(?:applicants?|appellants?|claimants?|plaintiffs?|petitioners?|complainants?|"
	r"(?:person|individual) concerned|permanent resident|foreign national|protected person)")
_RESP_NOUN = (r"(?:the\s+)?(?:respondents?|defendants?|minister(?:\s+of\s+[A-Z][\w ,&-]+?)?|minister['’]s\s+(?:counsel|representative|delegate's counsel)|"
	r"attorney general(?:\s+of\s+canada)?|crown|government(?:\s+of\s+canada)?|"
	r"canada border services agency|cbsa|ircc|mci|mpsep|mcpi|ministre|crown counsel|"
	r"minister['’]s representative|public safety)")
_COUNSEL = r"(?:(?:counsel|lawyer|representative|agent)\s+(?:for|of)\s+(?:the\s+)?)"
_POSS = r"['’]s?"

_EARLIER_NOUN = (r"(?:the\s+)?(?:officer|visa officer|immigration officer|senior immigration officer|pra?r?a officer|"
	r"prra officer|h&c officer|h&c|decision[- ]?makers?|delegate|member|panel|board|tribunal|"
	r"rpd|rad|iad|id|ird|sst|rpd member|rad member|iad member|division|"
	r"commissioner|adjudicator|immigration division|refugee protection division|refugee appeal division|"
	r"immigration appeal division|appeal division|(?:application|motions?|reviewing) judge|"
	r"trial judge|federal court judge|the judge|judge|arbitrator|visa office|case officer|reviewing officer|"
	r"program manager|ircc officer|biometrics officer|decision letter|refusal letter|letter of refusal|"
	r"gcms notes|officer['’]s notes|reasons for decision|reasons for refusal|notes to file)")
_EARLIER_VERB = re.compile(
	r"(?:found|finds|concluded|concludes|determined|determines|decided|decides|held|holds|noted|notes|stated|states|"
	r"wrote|writes|reasoned|reasons|accepted|accepts|rejected|rejects|considered|considers|assessed|assesses|"
	r"gave|gives|was not satisfied|was satisfied|were not satisfied|did not believe|drew|draws|"
	r"ruled|rules|observed|observes|indicated|indicates|acknowledged|acknowledges|"
	r"said|says|explained|explains|erred|failed to|believed|disbelieved|doubted|questioned|"
	r"was of the (?:view|opinion)|is of the (?:view|opinion)|was concerned|had concerns|"
	r"gives|give|sets out|set out|lists|listed|reads|read|relied on|relies on|attributed|weighed|did not accept|did not find|did not consider|"
	r"was not persuaded|was persuaded|had difficulty|saw no|sees no)\b", re.I)

# Words that mark the reasons or record of the earlier decision.
_EARLIER_POSS = re.compile(
	r"\b(?:the\s+)?(?:officer|rpd|rad|iad|id|board|tribunal|member|panel|decision[- ]?maker|delegate|judge)"
	r"(?:['’]s)\s+(?:reasons|decision|notes|finding|findings|conclusion|conclusions|assessment|analysis|"
	r"determination|treatment|reading|interpretation|approach|credibility|view)\b", re.I)
_DECISION_UNDER_REVIEW = re.compile(
	r"\b(?:the\s+)?(?:decision under review|impugned decision|decision (?:of|by) the (?:officer|rpd|rad|iad|board)|"
	r"decision (?:being|under) (?:reviewed|appeal)|refusal letter|negative decision|the decision)\b"
	r"(?=[^.]{0,40}\b(?:states?|stated|reads?|found|finds?|concluded?|noted|rejected|was based)\b)", re.I)

_COURT_FIRST_PERSON = re.compile(
	r"\bI\s+(?:find|found|conclude|concluded|agree|disagree|am|am not|would|will|do not|don['’]t|did not|"
	r"see no|see nothing|accept|reject|note|noted|have considered|have concluded|have found|decline|share|cannot|"
	r"can't|must|should|need|do|also|therefore|thus|therefore find|prefer|read|take|turn|begin|start|"
	r"now|first|next|further|consider|considered|think|believe|believe that|have|had|would not|"
	r"was not|was|dismiss|allow|certif|grant|order|direct|observe|add|emphasi[sz]e)\b|"
	r"\b(?:in|to) my (?:view|opinion|respectful view|respectful opinion|assessment|judgment)\b|"
	r"\bmy (?:conclusion|finding|view|analysis|reasons|decision)\b|"
	r"\b(?:the court|this court|the tribunal|the panel|the division|the board|the member)\s+"
	r"(?:finds|found|concludes|concluded|agrees|disagrees|is satisfied|notes|noted|must|will|should|"
	r"is not persuaded|was not persuaded|is of the view|accepts|rejects|observes|cannot|would|has considered|"
	r"does not|do not|is unable|sees no|saw no|read|reads|turns|now turns|begins|considers|reviewed)\b|"
	r"\b(?:application|appeal|motion|request|judicial review)\s+(?:for judicial review\s+)?"
	r"(?:is|are|will be|must be|should be|shall be)\s+(?:allowed|dismissed|granted|refused|rejected)\b|"
	r"\bthere is no (?:question|serious question)\b|\bno (?:costs|question)s?\b|"
	r"\bthis (?:court['’]s )?judgment\b|\bjudgment (?:in|is)\b|"
	r"\bi am (?:not )?persuaded\b|\bnot persuaded\b|\bnot convinced\b|\bunpersuasive\b", re.I)

_AUTH_CITE = r"(?:\b(?:19|20)\d{2}\s+(?:SCC|FCA|FC|CAF|CF|ONCA|BCCA|ABCA|QCCA|CanLII|RAD|RPD|IAD|SST)\s+\d+|\[(?:19|20)\d{2}\]\s+\d+\s+(?:SCR|FCR|F\.C\.|S\.C\.R\.|FC|FCR|C\.F\.))"
_AUTH_ACT = (r"(?:held|holds|found|finds|stated|states|said|says|explained|explains|observed|observes|"
	r"noted|notes|concluded|concludes|wrote|writes|confirmed|confirms|reaffirmed|recognized|recognised|clarified|"
	r"ruled|rules|emphasi[sz]ed|determined|decided|reasoned|cautioned|affirmed|set out|sets out|"
	r"established|established that|expressed|described|defined|requires|required|provides|provided|"
	r"means|mean|reads|read|directs|directed|applied|applies|adopted|adopts|rejected|distinguished|"
	r"outlined|outlines|summari[sz]ed|reiterated|reiterates|elaborated)")
_AUTH_VERB = (r"(?:held|holds|found|finds|stated|states|said|says|explained|explains|observed|observes|"
	r"noted|notes|concluded|concludes|wrote|writes|confirmed|confirms|reaffirmed|recognized|recognised|clarified|"
	r"ruled|emphasi[sz]ed|determined|decided|reasoned|cautioned|affirmed|set out|sets out|"
	r"established|expressed|described|defined|reiterated|elaborated|outlined|summari[sz]ed)")
_STATUTE_VERB = r"(?:provides?|states?|requires?|defines?|says?|allows?|permits?|prohibits?|stipulates?|mandates?|directs?|sets out)"
_AUTHORITY_SUBJ = re.compile(
	r"(?:\b(?i:(?:the\s+)?(?:supreme court(?: of canada)?|federal court of appeal|court of appeal|"
	r"case law|jurisprudence|caselaw|authorities))\b|"
	r"\b(?i:chief justice|madam justice|mr\.? justice|justice|mme? justice|justices)\s*[A-Z][\w'’-]*|"
	r"\b[A-Z][\w'’-]+,?\s+(?:C\.J\.|J\.A\.|J\.|JJ\.A\.|C\.J\.C\.)(?=\s)|"
	r"\b[A-Z][\w.'’&-]*(?:\s+[A-Za-z][\w.'’&-]*){0,5}\s+v\.?\s+[A-Z][\w.'’&()-]*(?:\s+[A-Za-z][\w.'’&()-]*){0,5}?)"
	r"[^.;]{0,50}?\b%s\b" % _AUTH_VERB)
_STATUTE_SUBJ = re.compile(
	r"(?:\bparliament\b|\bthe\s+(?:act|regulations?|irpa|irpr|statute|legislation|convention|charter|guidelines|manual|"
	r"operational manual|policy|instructions|ministerial instructions)\b|"
	r"\b(?:section|subsection|paragraph|article|rule|s\.|ss\.)\s*\d+[\w.()]*(?:\s+of\s+the\s+[A-Z][\w ]*)?)"
	r"[^.;]{0,40}?\b%s\b" % _STATUTE_VERB, re.I)
_AUTHORITY_LEAD = re.compile(
	r"^(?:\[\d+\]\s*)?(?:in|see|see also|as (?:stated|held|explained|noted|observed|set out|confirmed|mentioned) in|"
	r"per|citing|cited in|following|applying|compare|cf\.?|contrast)\s+(?:the\s+)?[A-Z][\w.'’& ,()-]{2,80}?"
	r"(?:\s+v\.?\s+|\s+c\.\s+|,\s*(?:19|20)\d{2}\s)", re.I)
_CITES = re.compile(_AUTH_CITE + r"|\b[A-Z][\w'’-]+\s+v\.?\s+[A-Z]|\bat\s+paras?\.?\s+\d+|\bibid\b")
_AUTH_CITE_TAIL = re.compile(_AUTH_CITE + r"|\bat\s+paras?\.?\s+\d+", re.I)

_WITNESS = re.compile(
	r"\b(?:testif(?:y|ied|ies|ying)|testimony|swore|sworn|(?:gave|gives|giving) evidence|oral evidence|"
	r"(?:in|from|during)\s+(?:his|her|their|the applicant['’]s|the claimant['’]s)\s+(?:affidavit|statement|"
	r"narrative|boc|basis of claim|declaration|interview|oral testimony|evidence|hearing|letter|submission|"
	r"testimony|application|form|forms|written statement|poe notes|port of entry notes|affidavit evidence)|"
	r"according to (?:the|his|her|their)\s+(?:ndp|national documentation package|documentary evidence|"
	r"country conditions?|country documentation|documents?|affidavit|letter|report|record|evidence|medical|"
	r"psychological|police|doctor|expert|translator|interpreter|witness|certificate)|"
	r"(?:the|a|an|his|her|their|x{3,}['’]?s?)\s+(?:affidavit|affidavits|letter|letters|report|reports|document|documents|"
	r"passport|ndp|national documentation package|country condition (?:documents|evidence|reports?)|"
	r"medical (?:report|certificate)|psychological (?:report|assessment)|psychologist|doctor|physician|"
	r"expert|certificate|photo|photograph|photographs|video|email|emails|message|messages|text messages?|"
	r"record|records|boc|basis of claim|narrative|poe notes|transcript|summons|warrant|police report|"
	r"newspaper article|article|articles|news report|medical|evidence|witness|witnesses|"
	r"hearing transcript|ircc notes|gcms notes|cams notes|fosss notes|notes|statement|statements|form|forms|"
	r"application|supporting documents?)\s+(?:states?|stated|says?|said|indicates?|indicated|shows?|showed|"
	r"confirms?|confirmed|reveals?|revealed|notes?|noted|reports?|reported|reads?|provides?|provided|mentions?|"
	r"mentioned|describes?|described|alleges?|alleged|demonstrates?|"
	r"demonstrated|explains?|explained|asserts?|asserted|claims?|claimed|attests?|attested)\b)|"
	r"\bwitness(?:es)?\s+(?:said|stated|testified|gave|described|explained)\b|"
	r"\b(?:dr|mr|ms|mrs)\.?\s+[A-Z][\w'’-]+\s+(?:opined|opines|testified|reported|concluded|wrote)\b|"
	r"\bshe\s+(?:testified|swore)\b|\bhe\s+(?:testified|swore)\b", re.I)

_PRONOUN_PARTY = re.compile(r"^(?:he|she|they|his|her|their|mr\.?|ms\.?|mrs\.?|mx\.?)\b", re.I)


@dataclass
class Cue:
	holder: str
	phrase: str
	sentence: int
	confidence: str = "explicit"


@dataclass
class Result:
	"""Tagging of one paragraph."""
	cues: list[Cue] = field(default_factory=list)
	holders: list[str] = field(default_factory=list)
	primary: str = COURT
	sentence_holders: list[str] = field(default_factory=list)
	sentence_holders_extra: list[str] = field(default_factory=list)  # paragraph-level only (citations)


# ---------------------------------------------------------------------------
# Sentences
# ---------------------------------------------------------------------------

_ABBREV = re.compile(
	r"\b(?:v|vs|s|ss|para|paras|no|nos|mr|ms|mrs|dr|st|inc|ltd|co|corp|cf|et al|e\.g|i\.e|etc|c|art|"
	r"sec|subs|pp|p|vol|ed|eds|cl|al|j|jj|ja|cj|f\.c|f\.c\.a|s\.c\.c|supp|rev|ch|cir|dept|jan|feb|mar|apr|"
	r"jun|jul|aug|sep|sept|oct|nov|dec|approx|prof|hon|esq|jr|sr|ca|can|ont|que|bc|alta|man|sask)\.\s*$", re.I)


def split_sentences(text: str) -> list[str]:
	text = re.sub(r"^\s*\[\d+\]\s*", "", text or "")
	text = re.sub(r"\s+", " ", text).strip()
	if not text:
		return []
	out: list[str] = []
	start = 0
	for m in re.finditer(r"[.!?;:](?=[\"”’')\]]*\s+(?:[A-Z“\"(\[]|\d))", text):
		end = m.end()
		while end < len(text) and text[end] in "\"”’')]":
			end += 1
		chunk = text[start:end].strip()
		if m.group(0) in ".:" and _ABBREV.search(text[start:m.end()]):
			continue
		if m.group(0) == ":":
			continue
		if chunk:
			out.append(chunk)
		start = end
	tail = text[start:].strip()
	if tail:
		out.append(tail)
	return out


# ---------------------------------------------------------------------------
# Cue finding
# ---------------------------------------------------------------------------

def _party_regexes(parties: Parties) -> tuple[re.Pattern | None, re.Pattern | None]:
	def build(names: Iterable[str]) -> re.Pattern | None:
		names = [re.escape(n) for n in names if n]
		if not names:
			return None
		return re.compile(r"(?:\b(?:mr\.?|ms\.?|mrs\.?|mx\.?)\s+)?\b(?:%s)\b" % "|".join(names))
	return build(parties.aliases_first), build(parties.aliases_second)


def _subject_re(noun: str) -> re.Pattern:
	return re.compile(r"(?:^|[\s,(\"“])(%s)(?:%s)?(?=[\s,])" % (noun, _POSS), re.I)


_APPL_RE = _subject_re(_APPL_NOUN)
_RESP_RE = _subject_re(_RESP_NOUN)
_COUNSEL_APPL = re.compile(r"\b%s%s\b" % (_COUNSEL, _APPL_NOUN), re.I)
_COUNSEL_RESP = re.compile(r"\b%s%s\b" % (_COUNSEL, _RESP_NOUN), re.I)
_EARLIER_RE = re.compile(r"(?:^|[\s,(\"“])(%s)(?:%s)?(?=[\s,])" % (_EARLIER_NOUN, _POSS), re.I)

_ACCORDING = re.compile(r"\baccording to\s+(.{1,60}?)(?:,|\s+(?:the|it|he|she|they|a|an)\s)", re.I)
_IN_VIEW = re.compile(r"\b(?:in|to)\s+(.{1,60}?)['’]s?\s+(?:view|opinion|submission|position|argument|estimation|mind|submissions)\b", re.I)
_VIEW_OF = re.compile(r"\b(?:in|to) the (?:view|opinion|submission) of (.{1,60}?)(?:,|\s)", re.I)
_POSITION_OF = re.compile(r"(?:^|\s)(%s|%s)['’]s?\s+(?:position|argument|arguments|submissions?|"
	r"claim|allegation|allegations|contention|view|theory|case|evidence|reply|response|counsel)\b" % (_APPL_NOUN, _RESP_NOUN), re.I)


def _side_of_noun(noun: str, parties: Parties) -> str | None:
	"""Map the literal word to a holder; the literal word is what a reader sees."""
	n = noun.lower()
	swap = parties.minister_first and parties.normalize
	if re.search(r"minister|attorney|crown|government|cbsa|border services|ircc|mci|mpsep|mcpi|ministre|public safety", n):
		return RESPONDENT
	if re.search(r"applicant|appellant|claimant|plaintiff|petitioner|complainant|permanent resident|"
		r"foreign national|protected person|person concerned|individual concerned", n):
		return RESPONDENT if swap and re.search(r"applicant|appellant|petitioner|plaintiff", n) else APPLICANT
	if re.search(r"respondent|defendant", n):
		return APPLICANT if swap else RESPONDENT
	return None


def _first_alias_hit(sentence: str, rx: re.Pattern | None) -> re.Match | None:
	return rx.search(sentence) if rx else None


def sentence_cue(sentence: str, parties: Parties | None = None, *, index: int = 0) -> Cue | None:
	"""The first explicit cue in a sentence, or None."""
	parties = parties or Parties()
	rx_first, rx_second = _party_regexes(parties)
	s = sentence
	hits: list[tuple[int, int, str, str]] = []  # (position, priority, holder, phrase)

	def add(pos: int, prio: int, holder: str, phrase: str) -> None:
		hits.append((pos, prio, holder, phrase.strip()))

	# first person / the court's own voice
	m = _COURT_FIRST_PERSON.search(s)
	if m:
		add(m.start(), 1, COURT, m.group(0))

	# witness or document
	m = _WITNESS.search(s)
	if m:
		own = re.match(r"(?:testif|testimony|swore|sworn|(?:gave|gives|giving) evidence|oral evidence|"
			r"(?:in|from|during)\s+(?:his|her|their|the applicant|the claimant)|she\s|he\s|they\s)", m.group(0), re.I)
		# the party's own testimony or sworn statement is the party's position; keep WITNESS for other people and papers
		add(m.start(), 3, APPLICANT if own else WITNESS, m.group(0))

	# prior authority: citation + verb, or an "In X v. Y" lead
	m = _AUTHORITY_SUBJ.search(s)
	if m:
		add(m.start(), 4, AUTHORITY, m.group(0)[:60])
	m = _STATUTE_SUBJ.search(s)
	if m:
		add(m.start(), 4, AUTHORITY, m.group(0)[:60])
	m = _AUTHORITY_LEAD.search(s)
	if m:
		add(m.start(), 2, AUTHORITY, m.group(0)[:60])

	# earlier decision maker
	for m in _EARLIER_RE.finditer(s):
		tail = s[m.end(): m.end() + 80]
		vm = _EARLIER_VERB.match(tail.lstrip(" ,"))
		noun = m.group(1).lower()
		if not vm:
			continue
		if vm:
			add(m.start(1), 5, EARLIER, s[m.start(1): m.end() + len(vm.group(0)) + 1 if vm else m.end()])
			break
	m = _EARLIER_POSS.search(s)
	if m:
		add(m.start(), 5, EARLIER, m.group(0))
	m = _DECISION_UNDER_REVIEW.search(s)
	if m:
		add(m.start(), 6, EARLIER, m.group(0))

	# parties: "<party> <argue verb>", "according to <party>", "in <party>'s view"
	for m in list(_APPL_RE.finditer(s)) + list(_RESP_RE.finditer(s)):
		after = s[m.end():]
		window = after[:60]
		am = re.match(r"[\s,]*(?:(?:also|further|then|now|again|however|first|instead|likewise|therefore|thus|"
			r"as well|only|simply|never|not|has|have|had|did|does|do|will|would|can|could|may|might|must|should|"
			r"strongly|vigorously|consistently|repeatedly|expressly|essentially)\s+)*" + _ARGUE_RE.pattern, window, re.I) or \
			re.match(r"[\s,]*(?:therefore |thus |then |also )?(?:brought|filed|made|bring|file|make)\b[^.;]{0,60}?,\s*"
			+ _ARGUE_RE.pattern, window + after[60:140], re.I)
		if am:
			holder = _side_of_noun(m.group(1), parties)
			if holder:
				add(m.start(1), 5, holder, s[m.start(1): m.end() + am.end()])
	for rx, holder in ((_COUNSEL_APPL, APPLICANT), (_COUNSEL_RESP, RESPONDENT)):
		m = rx.search(s)
		if m and _ARGUE_RE.search(s[m.end(): m.end() + 60]):
			add(m.start(), 5, holder, m.group(0))
	m = _POSITION_OF.search(s)
	if m:
		holder = _side_of_noun(m.group(1), parties)
		if holder:
			add(m.start(1), 5, holder, m.group(0))
	for rx_alias, holder in ((rx_first, APPLICANT), (rx_second, RESPONDENT)):
		if not rx_alias:
			continue
		if parties.minister_first:
			# the Minister has no short name; only the second side (the individual) has aliases
			if holder == APPLICANT:
				continue
			holder = APPLICANT if parties.normalize else RESPONDENT
		for m in rx_alias.finditer(s):
			window = s[m.end(): m.end() + 60]
			am = re.match(r"[\s,]*(?:(?:also|further|then|now|again|however|first|instead|likewise|has|have|had|did|"
				r"does|do|will|would|can|could|strongly|consistently|repeatedly)\s+)*" + _ARGUE_RE.pattern, window, re.I)
			if am:
				add(m.start(), 5, holder, s[m.start(): m.end() + am.end()])
				break
		m = rx_alias.search(s)
		if m and re.search(r"according to\s*$|in\s*$|to\s*$", s[:m.start()], re.I) and re.match(
				r"['’]s?\s+(?:view|opinion|submission|position|argument|estimation|mind)", s[m.end():], re.I):
			add(m.start(), 5, holder, s[max(0, m.start() - 20): m.end() + 12])
		m = rx_alias.search(s)
		if m and re.search(r"according to\s*$", s[:m.start()], re.I):
			add(m.start(), 5, holder, s[max(0, m.start() - 16): m.end()])
	m = _ACCORDING.search(s)
	if m:
		who = m.group(1)
		holder = _side_of_noun(who, parties)
		if holder is None:
			if rx_first and rx_first.search(who) and not parties.minister_first:
				holder = APPLICANT
			elif rx_second and rx_second.search(who):
				holder = APPLICANT if (parties.minister_first and parties.normalize) else RESPONDENT
		if holder:
			add(m.start(), 5, holder, m.group(0))
	for rx in (_IN_VIEW, _VIEW_OF):
		m = rx.search(s)
		if m:
			who = m.group(1)
			holder = _side_of_noun(who, parties)
			if holder is None and rx_first and rx_first.search(who) and not parties.minister_first:
				holder = APPLICANT
			if holder is None and rx_second and rx_second.search(who):
				holder = APPLICANT if (parties.minister_first and parties.normalize) else RESPONDENT
			if holder:
				add(m.start(), 5, holder, m.group(0))

	if not hits:
		# a citation tail with no other cue is the authority speaking
		m = _AUTH_CITE_TAIL.search(s)
		if m and re.search(r"\bv\.?\s", s):
			return Cue(AUTHORITY, m.group(0), index, "explicit")
		return None
	# earliest cue wins; a tie goes to the higher priority number (more specific)
	hits.sort(key=lambda h: (h[0], -h[1]))
	pos, _, holder, phrase = hits[0]
	# first-person text anywhere in a sentence about a party view ("I note that the applicant submits") stays
	# with the party when the party cue sits inside the same clause
	if holder == COURT and len(hits) > 1:
		for h in hits[1:]:
			if h[2] in (APPLICANT, RESPONDENT, EARLIER, WITNESS) and re.match(
					r"I\s+(?:note|noted|observe|observed|accept|understand|recognize|recognise|acknowledge|"
					r"see|read|have read|have considered|am aware)\b", s[pos:pos + 40], re.I):
				return Cue(h[2], h[3], index, "explicit")
	return Cue(holder, phrase, index, "explicit")


_CONTINUES = re.compile(
	r"^(?:\[\d+\]\s*)?(?:further(?:more)?|also|moreover|in addition|additionally|lastly|finally|specifically|"
	r"similarly|likewise|they|he|she|it|that|this|these|those|first|second|third|as such|accordingly|"
	r"in particular|according to|as a result|therefore|thus|consequently|for example|for instance)\b", re.I)
_DATE = re.compile(r"\b(?:19|20)\d{2}\b|\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b", re.I)
_COURT_RESET = re.compile(
	r"^(?:\[\d+\]\s*)?(?:I\b|In my\b|My\b|The Court\b|Having\b|For\b|Accordingly\b|Therefore\b|As a result\b|"
	r"This application\b|The application\b|The appeal\b|Turning\b|On the\b|Thus\b|However, I\b|"
	r"Consequently\b|In conclusion\b|There is no\b|Neither\b|Neither party\b|Both parties\b|The parties\b|"
	r"The standard of review\b|The issue\b|The issues\b|The question\b)", re.I)


def tag_paragraph(text: str, parties: Parties | None = None, *, previous: str | None = None) -> Result:
	"""Tag one paragraph. ``previous`` is the holder of the paragraph before it (for run carry-over)."""
	parties = parties or Parties()
	sentences = split_sentences(text)
	res = Result()
	last = previous
	for i, s in enumerate(sentences):
		cue = sentence_cue(s, parties, index=i)
		if cue:
			res.cues.append(cue)
			res.sentence_holders.append(cue.holder)
			last = cue.holder
			continue
		# no cue: carry a submission/finding run, but not past a first-person reset
		if last in (APPLICANT, RESPONDENT) and _CONTINUES.match(s) and not _COURT_RESET.match(s) \
				and not _DATE.search(s):
			carried = Cue(last, "", i, "carried")
			res.cues.append(carried)
			res.sentence_holders.append(last)
		else:
			res.cues.append(Cue(COURT, "", i, "default"))
			res.sentence_holders.append(COURT)
			last = COURT if last in (None, COURT, AUTHORITY) else last
	if AUTHORITY not in res.sentence_holders and _CITES.search(text or ""):
		res.sentence_holders_extra = [AUTHORITY]
	order: list[str] = []
	for h in res.sentence_holders + list(res.sentence_holders_extra):
		if h not in order:
			order.append(h)
	res.holders = order
	explicit = [c.holder for c in res.cues if c.confidence == "explicit"]
	if explicit:
		res.primary = max(set(explicit), key=lambda h: (explicit.count(h), -explicit.index(h)))
	elif res.sentence_holders:
		res.primary = res.sentence_holders[0]
	return res


_PARA_NUM = re.compile(r"(?:(?<=\n)|(?<=\s)|^)\[(\d{1,4})\]\s")


def split_numbered_paragraphs(text: str) -> dict[int, str]:
	"""Split text on its own ``[n]`` markers. Markers must climb by small steps so that a
	bracketed number inside a quotation does not start a paragraph."""
	marks = [(m.start(), int(m.group(1))) for m in _PARA_NUM.finditer(text or "")]
	keep: list[tuple[int, int]] = []
	prev = 0
	for pos, n in marks:
		at_line_start = pos == 0 or text[pos - 1] == "\n"
		if n > prev and (n - prev == 1 or (n - prev <= 3 and at_line_start)):
			keep.append((pos, n))
			prev = n
	out: dict[int, str] = {}
	for i, (pos, n) in enumerate(keep):
		end = keep[i + 1][0] if i + 1 < len(keep) else len(text)
		out[n] = text[pos:end].strip()
	return out


def tag_decision(paragraphs: list[str], title: str = "") -> list[Result]:
	"""Tag a whole decision in order, carrying submission runs from one paragraph to the next."""
	parties = parse_parties(title)
	results: list[Result] = []
	prev: str | None = None
	for p in paragraphs:
		r = tag_paragraph(p, parties, previous=prev)
		results.append(r)
		last_explicit = [c.holder for c in r.cues if c.confidence == "explicit"]
		last_any = r.sentence_holders[-1] if r.sentence_holders else None
		if last_any in (COURT, None) or re.match(r"^\s*(?:\[\d+\]\s*)?(?:I\b|In my\b)", p):
			prev = None
		else:
			prev = last_any if last_explicit or last_any in (APPLICANT, RESPONDENT, EARLIER, WITNESS) else prev
	return results
