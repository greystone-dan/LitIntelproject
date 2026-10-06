"""Deterministic judge-name normalization (no database, no AI).

`parse_judge_name` turns a raw extracted judge string into a `JudgeName` with a
surname key, given-name tokens or initials, a role and a gender hint.
`group_judge_names` proposes same-person merge groups. Nothing here writes
data: callers apply approved groups through a reversible alias layer.
"""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field

# Leading surname particles ignored when building the surname key ("de Montigny" == "Montigny").
_PARTICLES = {"de", "du", "des", "von", "van", "der", "den", "di"}
_ROLE_PROTHONOTARY = re.compile(r"prothonotary|protonotaire", re.IGNORECASE)
_FEMALE = re.compile(r"\b(?:madam|madame|ms|mrs|mme|mademoiselle)\b", re.IGNORECASE)
# Phrases first (they contain words that are also surname particles), then single words.
_PHRASE_RE = re.compile(
	r"\b(?:l[’']?\s*honou?rable\s+juge|l[’']?\s*honou?rable|(?:le|la)\s+juge|juge\s+en\s+chef|"
	r"case\s+management\s+judge|associate\s+chief\s+justice|assistant\s+chief\s+justice|acting\s+chief\s+justice|"
	r"associate\s+judge|deputy\s+judge|chief\s+justice|the\s+honou?rable|the\s+honou?rouble)\b",
	re.IGNORECASE,
)
_WORD_RE = re.compile(
	r"\b(?:hono\w*|mister|mr|mrs|ms|madam|madame|mme|monsieur|justice|jusice|judge|juge|chief|acting|assistant|"
	r"associate|prothonotary|protonotaire|esquire|esq|maitre|me|supernumerary|the|dr|hon|deputy|assessor|registrar)\b",
	re.IGNORECASE,
)
_SUFFIX_RE = re.compile(r"[,\s]+(?:A\.?\s?C\.?\s?J|C\.?\s?J|D\.?\s?J|J\.?\s?J|J\.?\s?A|J\.?\s?F\.?\s?C\.?\s?C|J|P)\.?\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class JudgeName:
	raw: str
	surname: str  # lowercase ascii, hyphens as spaces, leading particles dropped
	given: tuple[str, ...] = ()  # lowercase given-name tokens (words or single initials)
	role: str = "judge"  # judge | prothonotary
	gender: str = ""  # "m", "f" or "" when unknown
	name_text: str = ""  # original-case name with titles/suffixes removed (accents kept)
	flags: tuple[str, ...] = field(default_factory=tuple)

	@property
	def initials(self) -> str:
		return "".join(token[0] for token in self.given)


def repair_text(raw: str) -> str:
	"""Fix common encoding damage and drop trailing docket noise."""
	text = raw
	if re.search(r"[ÂÃâ][\x80-\xbf€™œ‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜š›œžŸ]|Â", text):
		try:
			text = text.encode("cp1252").decode("utf-8")
		except (UnicodeEncodeError, UnicodeDecodeError):
			text = text.replace("Â", " ")
	text = text.replace(" ", " ").replace("‑", "-").replace("‐", "-").replace("’", "'")
	text = re.sub(r"\b(?:docket|between)\b.*$", "", text, flags=re.IGNORECASE)
	return " ".join(text.split())


def _fold(text: str) -> str:
	return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def _title_case(text: str) -> str:
	def fix(token: str, first: bool) -> str:
		if token.lower() in _PARTICLES and not first:
			return token.lower()
		match = re.fullmatch(r"(Mc|Mac)([A-Z]{2,})", token)
		if match:
			return match.group(1) + match.group(2).capitalize()
		if not token.isupper() or "." in token:
			return token
		parts = re.split(r"([\-'])", token.lower())
		return "".join(p.capitalize() if p not in "-'" else p for p in parts)
	return " ".join(fix(t, i == 0) for i, t in enumerate(text.split()))


def parse_judge_name(raw: str) -> JudgeName | None:
	"""Parse a raw judge string; return None when no personal name is left."""
	if not raw or not raw.strip():
		return None
	repaired = repair_text(raw)
	if re.search(r"\bassessor\b", repaired, re.IGNORECASE):
		return None  # "Deputy Assessor" entries are a different role: never merge them into a judge
	role = "prothonotary" if _ROLE_PROTHONOTARY.search(repaired) else "judge"
	gender = "f" if _FEMALE.search(repaired) else ("m" if re.search(r"\b(?:mr|mister|monsieur)\b", repaired, re.IGNORECASE) else "")
	flags: list[str] = []
	text = re.sub(r"[-_=]{3,}", " ", repaired)
	text = re.sub(r"(?i)justice(?=[A-Z])", "Justice ", text)
	text = re.sub(r"\s+\.", ".", text).replace("_", " ")
	text = re.sub(r"([a-z])([A-Z]\.)", r"\1 \2", text)
	text = re.sub(r",?\s*\b(?:esq(?:uire)?)\b\.?,?", " ", text, flags=re.IGNORECASE)
	previous = None
	while previous != text:
		previous, text = text, _SUFFIX_RE.sub("", text.strip())
	if text != repaired.strip():
		flags.append("suffix")
	text = _PHRASE_RE.sub(" ", text)
	text = _WORD_RE.sub(" ", text)
	text = re.sub(r"\bM\.(?=\s)", " ", text)
	text = re.sub(r"[^A-Za-zÀ-ÿ'\-,. ]+", " ", text)
	text = " ".join(text.split()).strip(" ,.")
	name_text = text
	if "," in text:  # "Surname, Given" -> "Given Surname" for display
		last, _, first = text.partition(",")
		name_text = f"{first.strip()} {last.strip()}".strip()
	folded = _fold(text)
	if "," in folded:
		surname_part, _, given_part = folded.partition(",")
		given_tokens = given_part.replace(".", " ").split()
	else:
		tokens = folded.replace(".", " ").split()
		if not tokens:
			return None
		idx = len(tokens) - 1
		while idx > 0 and tokens[idx - 1].lower() in _PARTICLES:
			idx -= 1
		surname_part, given_tokens = " ".join(tokens[idx:]), tokens[:idx]
	words = [w for w in re.split(r"[\-\s]+", surname_part.lower()) if w]
	while len(words) > 1 and words[0] in _PARTICLES:
		words.pop(0)
	surname = " ".join(words)
	surname = re.sub(r"^(mc|mac)\s+", r"\1", surname)
	given = tuple(t for t in (re.sub(r"[^a-z]", "", g.lower()) for g in given_tokens) if t)
	if len(surname) < 2 or not re.search(r"[a-z]{2}", surname):
		return None
	return JudgeName(raw, surname, given, role, gender, _title_case(name_text), tuple(flags))


def _given_compatible(a: JudgeName, b: JudgeName) -> bool:
	if not a.given or not b.given:
		return False  # surname-only never merges on its own
	for x, y in zip(a.given, b.given):
		if x[0] != y[0]:
			return False
		if len(x) > 1 and len(y) > 1 and x != y:
			return False
	return True


def same_person(a: JudgeName, b: JudgeName) -> bool:
	"""Safe merge: same surname, compatible given names/initials, no gender clash.

	Role is ignored on purpose: prothonotaries became associate judges (e.g. Tabib, Aylen).
	"""
	if a.surname != b.surname or (a.gender and b.gender and a.gender != b.gender):
		return False
	return _given_compatible(a, b)


@dataclass
class MergeGroup:
	surname: str
	members: list[str]
	canonical: str  # display name for the person
	roles: list[str] = field(default_factory=list)
	needs_review: list[str] = field(default_factory=list)


def _display(members: list[str], parsed: dict[str, JudgeName], counts: dict[str, int]) -> str:
	def rank(raw: str) -> tuple:
		p = parsed[raw]
		mixed = p.name_text != p.name_text.upper()
		return (len(p.given), mixed, counts[raw])
	return parsed[max(members, key=rank)].name_text


_FCA_SUFFIX_RE = re.compile(r"\bJ\.?\s?A\.?\s*$", re.IGNORECASE)
ELEVATION_TOLERANCE_DAYS = 366


def is_fca_string(raw: str) -> bool:
	"""True for an appeal-court style string ("NOËL J.A."): the same surname can be a different person at the FC."""
	return bool(_FCA_SUFFIX_RE.search(repair_text(raw).strip()))


def _span(members: list[str], spans: dict[str, tuple[int, int]]) -> tuple[int, int] | None:
	known = [spans[m] for m in members if m in spans]
	return (min(a for a, _ in known), max(b for _, b in known)) if known else None


def _attach_bare(bare, clusters, counts, parsed) -> list[str]:
	"""Attach surname-only strings to the person they belong to (mutates `clusters`); return the ones left for review."""
	review: list[str] = []
	if len(clusters) == 1:
		fits = [b for b in bare if not (parsed[b].gender and parsed[clusters[0][0]].gender and parsed[b].gender != parsed[clusters[0][0]].gender)]
		clusters[0].extend(fits)
		review = [b for b in bare if b not in fits]
	elif not clusters:
		female = [b for b in bare if parsed[b].gender == "f"]
		male = [b for b in bare if parsed[b].gender == "m"]
		if female and male:  # same surname, different gender titles: two people
			clusters.extend([female, male])
			review = [b for b in bare if not parsed[b].gender]  # cannot tell which one: leave alone
		else:
			clusters.append(list(bare))
	else:
		weights = [sum(counts[m] for m in c) for c in clusters]
		top = max(range(len(clusters)), key=lambda i: weights[i])
		others = sum(weights) - weights[top]
		# A clearly dominant person (others are a handful of stray decisions, usually a
		# typo'd initial) takes the surname-only strings; otherwise leave them for review.
		if others <= max(3, weights[top] // 50):
			gender = parsed[clusters[top][0]].gender
			fits = [b for b in bare if not (parsed[b].gender and gender and parsed[b].gender != gender)]
			clusters[top].extend(fits)
			review = [b for b in bare if b not in fits]
		else:
			review = list(bare)
	return review


def group_judge_names(counts: dict[str, int], spans: dict[str, tuple[int, int]] | None = None,
		courts: dict[str, set[str]] | None = None) -> list[MergeGroup]:
	"""Group raw judge strings (value -> decision count) into proposed same-person groups.

	Only groups with 2+ distinct raw strings, or ones with a review note, are returned.
	A surname-only string joins a group only when exactly one person with that surname exists;
	otherwise it is listed under `needs_review` and left alone.

	Surname-only "J.A." strings (Federal Court of Appeal) are court-scoped: they join a Federal Court
	person only when `spans` (raw string -> (first, last) decision date ordinals) shows that person's
	FC decisions ended before the appeal decisions began (a judge elevated to the FCA). Without spans,
	or when the dates overlap (Simon Noël FC vs Marc Noël FCA), they stay a separate FCA person.
	Any other surname-only string (`courts`: raw string -> courts of its profiles) joins only a person
	seen in one of its own courts, so FC "Justice Brown" never lands on SCC Russell Brown.
	"""
	parsed = {raw: parse_judge_name(raw) for raw in counts}
	by_surname: dict[str, list[str]] = defaultdict(list)
	for raw, p in parsed.items():
		if p is not None:
			by_surname[p.surname].append(raw)
	groups: list[MergeGroup] = []
	for surname, raws in by_surname.items():
		full = sorted((r for r in raws if parsed[r].given), key=lambda r: -counts[r])
		bare = sorted((r for r in raws if not parsed[r].given), key=lambda r: -counts[r])
		clusters: list[list[str]] = []
		for raw in full:
			for cluster in clusters:
				if all(same_person(parsed[raw], parsed[m]) for m in cluster):
					cluster.append(raw)
					break
			else:
				clusters.append([raw])
		review: list[str] = []
		bare_fca = [b for b in bare if is_fca_string(b)]
		bare = [b for b in bare if b not in bare_fca]
		if bare and courts and clusters:
			by_court: dict[frozenset, list[str]] = defaultdict(list)
			for b in bare:
				by_court[frozenset(courts.get(b, ()))].append(b)
			for court_set, strings in by_court.items():
				pool = [c for c in clusters if not court_set or court_set & set().union(*(courts.get(m, set()) for m in c))]
				review.extend(_attach_bare(strings, pool, counts, parsed) if pool else strings)
		elif bare:
			review.extend(_attach_bare(bare, clusters, counts, parsed))
		if bare_fca:
			fca_start = _span(bare_fca, spans or {})
			fits = []
			for cluster in clusters:
				cluster_span = _span(cluster, spans or {})
				if fca_start and cluster_span and (cluster_span[1] <= fca_start[0] + ELEVATION_TOLERANCE_DAYS
						or fca_start[1] <= cluster_span[0] + ELEVATION_TOLERANCE_DAYS):
					fits.append(cluster)
			if len(fits) == 1:
				fits[0].extend(bare_fca)
			else:
				clusters.append(list(bare_fca))
		for cluster in clusters:
			if len(cluster) > 1 or review:
				roles = sorted({parsed[m].role for m in cluster})
				groups.append(MergeGroup(surname, cluster, _display(cluster, parsed, counts), roles, review))
	return sorted(groups, key=lambda g: -sum(counts[m] for m in g.members))


def best_display_name(names: list[str]) -> str | None:
	"""Clean display name for one person from their raw strings, e.g. "Justice Simon Noël".

	Returns None when no string parses, so callers fall back to the stored name.
	"""
	parsed = [p for p in (parse_judge_name(n) for n in names) if p]
	if not parsed:
		return None
	best = max(parsed, key=lambda p: (len(p.given), p.name_text != p.name_text.upper(), len(p.name_text)))
	prefix = "Prothonotary" if all(p.role == "prothonotary" for p in parsed) else "Justice"
	return f"{prefix} {best.name_text}"


def split_panel(raw: str) -> list[str]:
	"""Split a multi-judge field ("Wagner, Richard; Abella, Rosalie; ...") into one string per judge."""
	text = raw or ""
	if ";" not in text and re.search(r"\bJJ\.?|\bC\.J\.\s+and\b", text):
		# Older style: "McLachlin C.J. and Abella, Moldaver and Rowe JJ."
		return [part.strip() for part in re.split(r",\s*|\s+and\s+", text) if part.strip()]
	return [part.strip() for part in text.split(";") if part.strip()]


_SENTENCE_WORDS = {"et", "le", "la", "les", "de", "du", "des", "nous", "que", "est", "the", "and", "was", "this", "pour", "avis"}


def _plausible_name(parsed: JudgeName) -> bool:
	"""Reject sentence fragments that landed in a panel field (French reasons text, "et nous sommes d'avis...")."""
	words = parsed.name_text.split()
	if len(words) > 6 or len(parsed.name_text) > 60:
		return False
	return not (len(words) >= 3 and sum(w.lower() in _SENTENCE_WORDS for w in words) >= 2 and "-" not in parsed.name_text)


def parse_panel(raw: str) -> list[JudgeName]:
	"""Individual judges named in a panel field; unparseable parts and duplicates are dropped."""
	seen: set[tuple[str, str]] = set()
	judges: list[JudgeName] = []
	for part in split_panel(raw):
		parsed = parse_judge_name(part)
		if parsed is None or not _plausible_name(parsed):
			continue
		key = (parsed.surname, parsed.initials[:1])
		if key not in seen:
			seen.add(key)
			judges.append(parsed)
	return judges


def is_panel_string(value: str) -> bool:
	"""True for a whole-panel string ("A; B; C" or "X C.J. and Y, Z JJ.") that is not one judge."""
	return bool(re.search(r";|\bJJ\.?|\bC\.J\.\s+and\b", value or ""))
