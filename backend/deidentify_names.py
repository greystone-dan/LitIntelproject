"""Find people's names automatically for the de-identify tool.

Runs entirely on this machine: a spaCy language model (no internet calls once
installed) plus a few rules that suit immigration files ("Ms. X", "my brother
X", the "BETWEEN: ... Applicant" block). Names of parties in cited cases
("Vavilov", "Baker v Canada, [1999] 2 SCR 817") and decision-makers
("Justice X", "Member X") are kept, because they are public and the legal
analysis needs them, unless the same name is also used for a person in the file.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from functools import lru_cache
import logging
import os
import re
from typing import Iterable

from .citations import extract_case_citation_matches
from .deidentify import NAME_PARTICLES

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "en_core_web_md"
CHUNK_CHARS = 20000

_NAME_WORD = r"[A-ZÀ-ÖØ-Þ][\w'’À-ÖØ-öø-ÿ-]*"
_HONORIFIC = r"(?:Mr|Mrs|Ms|Miss|Mx|Dr|Madam|Mme|Mlle|Monsieur|Madame|Señor|Señora|Sra|Sr)\.?"
_RELATION = (
	r"(?:brother|sister|mother|father|son|daughter|wife|husband|spouse|partner|uncle|aunt|cousin|"
	r"nephew|niece|grandmother|grandfather|grandson|granddaughter|friend|neighbou?r|sponsor|"
	r"boyfriend|girlfriend|fianc[ée]e?|brother-in-law|sister-in-law|mother-in-law|father-in-law|"
	r"stepfather|stepmother|child|children|colleague|employer|landlord|pastor|imam|priest)"
)
_HONORIFIC_NAME = re.compile(
	r"\b" + _HONORIFIC + r"\s+(?!(?:Justice|Chief|Associate|Judge|Member|Commissioner)\b)(" + _NAME_WORD + r"(?:\s+" + _NAME_WORD + r"){0,3})"
)
_RELATION_NAME = re.compile(
	r"\b(?:my|his|her|their|our|the claimant's|the applicant's)(?:\s+\w+['’]s)?\s+" + _RELATION
	+ r",?\s+(" + _NAME_WORD + r"(?:\s+" + _NAME_WORD + r"){0,3})"
)
_DOCUMENT_OF = re.compile(
	r"\b(?:AFFIDAVIT|STATUTORY DECLARATION|DECLARATION|STATEMENT|TESTIMONY|EVIDENCE|LETTER|NARRATIVE)\s+OF\s+"
	r"([A-ZÀ-ÖØ-Þ][A-ZÀ-ÖØ-Þ'’ -]{1,80}?)\s*$",
	re.MULTILINE,
)
_I_NAME = re.compile(r"(?:^|\n)\s*I,\s+(" + _NAME_WORD + r"(?:\s+" + _NAME_WORD + r"){0,5}),")
_PARTY_BLOCK = re.compile(
	r"\bBETWEEN\s*:\s*\n(.{2,400}?)\n\s*(?:Applicants?|Claimants?|Appellants?|Plaintiffs?|Petitioners?)\b",
	re.DOTALL,
)
_DECISION_MAKER = re.compile(
	r"\b(?:Justice|Juge|Judge|Member|Commissioner|Chief Justice|Associate Chief Justice|"
	r"Prothonotary|Associate Judge|Adjudicator)\s+((?:" + _NAME_WORD + r"\.?\s+){0,2}" + _NAME_WORD + r")"
	r"|\b(" + _NAME_WORD + r")\s+J\.?A?\.?(?=[\s,;)]|$)"
)

# Words that are never a person's name on their own, even when a model tags them.
_NOT_NAMES = {
	"applicant", "applicants", "claimant", "claimants", "appellant", "respondent", "officer", "member",
	"minister", "court", "justice", "judge", "board", "division", "panel", "tribunal", "counsel",
	"canada", "canadian", "government", "immigration", "citizenship", "refugee", "refugees",
	"protection", "act", "regulations", "section", "paragraph", "para", "decision", "reasons",
	"judgment", "order", "affidavit", "exhibit", "page", "tab", "the", "and", "of", "in", "on",
	"mr", "mrs", "ms", "dr", "madam", "sir", "honourable", "hon", "present", "between", "date",
	"docket", "citation", "file", "agent", "persecution", "aop", "god",
	"interpreter", "witness", "visa", "officer's", "irb", "rpd", "rad", "ircc", "cbsa", "mci", "minor", "spouse",
	"psep", "irpa", "irpr", "boc", "pif", "gcms", "h&c", "pra", "prra", "id",
	"appellants", "respondents", "et", "claimant's", "applicant's", "dated", "ibid", "etc", "supra",
	"conseil", "conseils", "motifs", "me", "commissaire", "membre", "demandeur", "demanderesse",
	"ministre", "juge", "imm", "lr", "scr", "fc", "fca", "fct", "ftr", "dlr", "acws", "nr", "cf", "caf",
	"j", "ja", "cj", "acj", "sgd", "signed", "judgment", "jugement", "per", "re",
	"v", "vs", "for", "place", "hearing", "style", "cause", "solicitors", "record", "appearances", "al",
	"barrister", "solicitor", "following", "see", "per", "also", "according", "pursuant", "unlike",
}
# Movements and faiths a model tends to read as people; hiding them would gut a claim's facts.
_GROUP_NAMES = {"falun gong", "falun dafa", "zhuan falun", "ahmadiyya", "ahmadi"}
_INITIAL = re.compile(r"[A-ZÀ-Þ]\.?")
_ABBREVIATION = re.compile(r"(?:[A-Za-z]\.){2,}[A-Za-z]?\.?|[A-Z]\.[A-Z]+")


@dataclass
class NameDetection:
	names: list[str] = field(default_factory=list)  # to hide
	kept: list[dict[str, str]] = field(default_factory=list)  # public names left in, with the reason
	available: bool = True
	message: str = ""


@lru_cache(maxsize=1)
def _load_model():
	import spacy

	name = os.getenv("DEIDENTIFY_SPACY_MODEL", DEFAULT_MODEL)
	nlp = spacy.load(name, exclude=["lemmatizer", "parser", "tagger", "attribute_ruler", "senter"])
	nlp.max_length = max(nlp.max_length, CHUNK_CHARS * 2)
	return nlp


def model_status() -> tuple[bool, str]:
	try:
		_load_model()
		return True, ""
	except Exception as exc:  # pragma: no cover - depends on the machine
		logger.warning("De-identify name model unavailable: %s", exc)
		return False, (
			"Automatic name detection is not available on this server (the spaCy language model is not "
			"installed). Only the names you type in will be hidden."
		)


def _chunks(text: str) -> Iterable[tuple[int, str]]:
	"""Split on paragraph breaks into pieces small enough for the model, keeping offsets."""
	start = 0
	while start < len(text):
		end = min(len(text), start + CHUNK_CHARS)
		if end < len(text):
			cut = text.rfind("\n", start + CHUNK_CHARS // 2, end)
			end = cut + 1 if cut > start else end
		yield start, text[start:end]
		start = end


def _model_view(chunk: str) -> str:
	"""Title-case ALL-CAPS lines so the model can read headings like 'AFFIDAVIT OF MARIA LOPEZ'."""
	def fix(line: str) -> str:
		letters = [c for c in line if c.isalpha()]
		if len(letters) >= 4 and all(c.isupper() for c in letters):
			titled = line.title()
			return titled if len(titled) == len(line) else line
		return line
	return "".join(fix(line) for line in chunk.splitlines(keepends=True))


def _junk_word(word: str, places: set[str]) -> bool:
	bare = word.strip(".,;:()").casefold()
	return bare in _NOT_NAMES or bare in places or bool(_ABBREVIATION.fullmatch(word.strip(",;:()")))


def _clean(name: str, places: set[str] = frozenset()) -> str:
	name = re.sub(r"[’']s$", "", name.strip())
	name = re.sub(r"^\W+|[^\w.)]+$", "", name)
	words = [w for w in name.split() if not re.fullmatch(_HONORIFIC, w, re.IGNORECASE)]
	while words and _junk_word(words[-1], places):
		words.pop()
	while words and _junk_word(words[0], places):
		words.pop(0)
	unique: list[str] = []
	for word in words:  # "Normand Leduc Normand" from table cells read across
		if word.casefold() not in {u.casefold() for u in unique}:
			unique.append(word)
	return re.sub(r"\.$", "", " ".join(unique)) if unique and not _INITIAL.fullmatch(unique[-1]) else " ".join(unique)


def _plausible(name: str, lowercase_words: set[str] = frozenset(), strict_caps: bool = True) -> bool:
	if not name or len(name) < 2 or re.search(r"\d|[\[\]@/\\(]", name) or "XXX" in name.upper():
		return False
	words = name.split()
	full_words = [w for w in words if not _INITIAL.fullmatch(w)]
	if not full_words:
		return False
	if all(w.casefold() in lowercase_words for w in full_words):
		return False  # "Reasonableness", "Motifs": ordinary words that happen to be capitalised here
	if len(words) > 7 or strict_caps and not all(w[0].isupper() for w in words if w.casefold() not in NAME_PARTICLES):
		return False
	return not all(w.casefold() in _NOT_NAMES for w in words)


def _case_citation_words(text: str) -> tuple[set[str], list[tuple[int, int]]]:
	"""Words used as party names in cited cases, and the spans of those citations."""
	words: set[str] = set()
	spans: list[tuple[int, int]] = []
	try:
		matches = extract_case_citation_matches(text)
	except Exception:  # pragma: no cover - defensive: citation parsing must never block redaction
		return words, spans
	for match in matches:
		if match.kind not in {"case", "case_short"}:
			continue  # a bare "X v. Canada" title may be the client's own case
		spans.append((match.offset_start, match.offset_end))
		parties = re.split(r",\s*(?:\[|\(|\d{4})", text[match.offset_start : match.offset_end])[0]
		words.update(w.casefold() for w in re.findall(r"[\w'’-]+", parties) if w[:1].isupper())
	return words, spans


def _extend_entity(text: str, start: int, end: int) -> tuple[int, int]:
	"""Widen a model hit to neighbouring capitalised words ("Harjinder" + "Singh Sandhu")."""
	word = re.compile(_NAME_WORD + r"$")
	while True:
		before = re.search(r"(" + _NAME_WORD + r") $", text[max(0, start - 40) : start])
		if not before or before.group(1).casefold() in _NOT_NAMES or re.fullmatch(_HONORIFIC, before.group(1)):
			break
		prev_start = start - len(before.group(0))
		lead = text[max(0, prev_start - 2) : prev_start]
		if not lead or lead.endswith("\n") or re.search(r"[.!?:]\s?$", lead):
			break  # the word starts a sentence or line, so its capital proves nothing
		start = prev_start
	while True:
		after = re.match(r" (" + _NAME_WORD + r")(?![\w'’-])", text[end : end + 40])
		if not after or after.group(1).casefold() in _NOT_NAMES or not word.match(after.group(1)):
			break
		end += len(after.group(0))
	return start, end


def detect_names(text: str, typed_names: Iterable[str] = (), never_hide: Iterable[str] = ()) -> NameDetection:
	available, message = model_status()
	raw: list[tuple[str, str]] = []  # (text as found, how it was found)
	personal_context: set[str] = set()  # words seen as a person in the file itself
	person_votes: Counter[str] = Counter()
	other_votes: Counter[str] = Counter()  # read as a place, group or organisation

	if available:
		nlp = _load_model()
		for offset, chunk in _chunks(text):
			doc = nlp(_model_view(chunk))
			for ent in doc.ents:
				start, end = offset + ent.start_char, offset + ent.end_char
				label_text = text[start:end].casefold()
				if ent.label_ == "PERSON":
					person_votes[label_text] += 1
					person_votes.update(label_text.split())
					start, end = _extend_entity(text, start, end)
					# A hit that runs over a line break is usually two people listed one per line.
					raw.extend((line, "model") for line in text[start:end].splitlines() if line.strip())
				elif ent.label_ in {"GPE", "LOC", "FAC", "NORP", "ORG"}:
					other_votes[label_text] += 1
					if ent.label_ != "ORG":
						other_votes.update(label_text.split())
	places = {w for w, n in other_votes.items() if n > person_votes[w]}

	for pattern, how in (
		(_HONORIFIC_NAME, "title"), (_RELATION_NAME, "relation"), (_DOCUMENT_OF, "party"), (_I_NAME, "party"),
	):
		for match in pattern.finditer(text):
			value = match.group(1)
			raw.append((value.title() if value.isupper() else value, how))
	for block in _PARTY_BLOCK.finditer(text):
		for part in re.split(
			r"\s*\n\s*|\s*,\s*|\s+(?:AND|and|et|ET)\s+|\s+(?:a\.?k\.?a\.?|A\.?K\.?A\.?|also known as|alias|n[ée]e?)\s+",
			re.sub(r"\s+et\s+al\.?|\([^)]*\)", "", block.group(1)),
		):
			part = re.sub(r"^(?:and|AND|et|ET)\s+", "", part.strip())
			raw.append((part.title() if part.isupper() else part, "party"))

	lowercase_words = set(re.findall(r"(?<![\w.])[a-zà-ÿ][\w'’-]*", text))
	found: dict[str, str] = {}
	for value, how in raw:
		if how == "model":
			name = _clean(value, places)
			if not _plausible(name, lowercase_words):
				continue
		else:
			# Found by a rule about people ("Ms. X", "BETWEEN: X Applicant"): trust it more.
			name = _clean(value)
			if not _plausible(name, strict_caps=False):
				continue
		if how == "model":
			if name.casefold() in places or name.casefold() in _GROUP_NAMES:
				continue  # read more often as a place, group or organisation ("Falun Gong")
			found.setdefault(name, how)
		else:
			found[name] = how
			personal_context.update(w.casefold() for w in name.split() if not _INITIAL.fullmatch(w))

	# A found surname drags in the capitalised words right before it: "by Harjinder Singh Sandhu".
	for name in [n for n in found if " " not in n and len(n) >= 3]:
		lead = re.compile(r"(?<=[a-z,;] )((?:" + _NAME_WORD + r" ){1,3})" + re.escape(name) + r"(?![\w'’-])")
		for match in lead.finditer(text):
			fuller = _clean(match.group(1) + name)
			if fuller != name and _plausible(fuller, lowercase_words):
				found.setdefault(fuller, found[name])

	decision_makers: set[str] = set()
	for match in _DECISION_MAKER.finditer(text):
		value = match.group(1) or match.group(2)
		decision_makers.update(w.casefold().rstrip(".") for w in value.split())

	citation_words, _ = _case_citation_words(text)
	typed_words = {w.casefold() for name in typed_names for w in name.split()}
	never = {_clean(n).casefold() for n in never_hide if n.strip()}

	result = NameDetection(available=available, message=message)
	for name, how in found.items():
		words = [w.casefold() for w in name.split() if not _INITIAL.fullmatch(w)]
		if name.casefold() in never:
			result.kept.append({"name": name, "reason": "On your never-hide list"})
			continue
		if not (set(words) & (typed_words | personal_context)):
			if all(w in citation_words for w in words):
				result.kept.append({"name": name, "reason": "Party in a cited case"})
				continue
			if words and words[-1] in decision_makers:
				result.kept.append({"name": name, "reason": "Judge or decision-maker"})
				continue
		result.names.append(name)

	# One entry per name whatever its case: prefer "Maria Lopez" over "MARIA LOPEZ".
	by_case: dict[str, str] = {}
	for name in result.names:
		key = name.casefold()
		if key not in by_case or (by_case[key].isupper() and not name.isupper()):
			by_case[key] = name
	# Drop names already covered by a longer name (its parts are hidden with it).
	longer = sorted(by_case.values(), key=lambda n: -len(n.split()))
	covered: list[str] = []
	for name in longer:
		words = set(name.casefold().split())
		if any(words < set(other.casefold().split()) for other in covered):
			continue
		covered.append(name)
	result.names = sorted(covered, key=str.casefold)
	result.kept = sorted({k["name"]: k for k in result.kept}.values(), key=lambda k: k["name"].casefold())
	return result
