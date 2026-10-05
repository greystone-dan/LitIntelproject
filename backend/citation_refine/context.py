"""Whole-document context shared by the refinement layers.

Built once per decision so later steps can ask:
- what does "the Act" / "the Regulations" / "[IRPA]" mean at this point?
- where does the sentence containing this offset start?
"""

from __future__ import annotations

import re
from bisect import bisect_right
from dataclasses import dataclass, field

from .instruments import INSTRUMENT_ALIAS_RE, REGISTRY, lookup_alias

# Abbreviations that end in a period but do not end a sentence.
_NON_TERMINAL_ABBREVIATIONS = {
	"s", "ss", "v", "c", "no", "nos", "para", "paras", "p", "pp", "art", "arts", "r", "rr",
	"sc", "rsc", "sor", "cf", "eg", "e.g", "ie", "i.e", "j", "ja", "jj", "mr", "mrs", "ms", "dr",
	"inc", "ltd", "co", "corp", "supp", "ed", "vol", "ch", "subs", "al", "id", "ibid", "n",
	"fc", "fca", "scr", "dlr", "imm", "lr", "fcj", "qb", "ca", "u", "st", "ste", "re", "vs",
}
_SENTENCE_END_RE = re.compile(r"[.!?](?=\s+[\"“(\[]?[A-Z0-9])|\n\s*\n")

# A defined term placed right after an instrument's name:
#   Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA]
#   ... Regulations, SOR/2002-227 (the "Regulations")
_DEFINITION_RE = re.compile(
	r"^[^\[\(\n]{0,110}?[\[(]\s*(?:hereinafter\s+(?:referred\s+to\s+as\s+)?)?(?:the\s+|la\s+|le\s+|les\s+)?"
	r"[\"“”'‘’]?(?P<term>[A-Z][A-Za-z'’ .]{0,40}?)[\"“”'‘’]?\s*[\])]"
)
_REJECT_TERMS = {"canlii", "ql", "lexis", "fc", "fca", "scc", "en", "fr", "eng", "fra"}

# Generic short forms that a decision may use without defining them.
GENERIC_TERMS = ("act", "regulations", "rules", "loi", "règlement", "règles", "convention", "charter")


def normalize_term(term: str) -> str:
	value = " ".join(term.replace("’", "'").split()).casefold().strip(" .\"“”'")
	value = re.sub(r"^(?:the|la|le|les|l')\s*", "", value)
	return value


@dataclass(frozen=True)
class Definition:
	offset: int
	term: str
	instrument_key: str
	explicit: bool


@dataclass
class DocumentContext:
	text: str
	sentence_starts: list[int] = field(default_factory=list)
	definitions: list[Definition] = field(default_factory=list)
	mentioned_instruments: dict[str, int] = field(default_factory=dict)
	first_mentions: dict[str, int] = field(default_factory=dict)

	@classmethod
	def build(cls, text: str) -> "DocumentContext":
		context = cls(text=text)
		context.sentence_starts = _sentence_starts(text)
		context._collect_instruments()
		return context

	# -- sentences ---------------------------------------------------------
	def sentence_start(self, offset: int) -> int:
		index = bisect_right(self.sentence_starts, offset) - 1
		return self.sentence_starts[index] if index >= 0 else 0

	def previous_sentence_start(self, offset: int) -> int:
		index = bisect_right(self.sentence_starts, offset) - 2
		return self.sentence_starts[index] if index >= 0 else 0

	# -- definitions -------------------------------------------------------
	def _collect_instruments(self) -> None:
		for match in INSTRUMENT_ALIAS_RE.finditer(self.text):
			found = lookup_alias(match.group(0))
			if found is None:
				continue
			key, _language = found
			self.mentioned_instruments[key] = self.mentioned_instruments.get(key, 0) + 1
			self.first_mentions.setdefault(key, match.start())
			definition = _DEFINITION_RE.match(self.text, match.end())
			if definition is None:
				continue
			term = normalize_term(definition.group("term"))
			if not term or term in _REJECT_TERMS or re.search(r"\d", term) or len(term.split()) > 4:
				continue
			self.definitions.append(Definition(match.start(), term, key, explicit=True))
		self.definitions.sort(key=lambda item: item.offset)

	@property
	def is_immigration_context(self) -> bool:
		return any(
			key in self.mentioned_instruments
			for key in ("canada.irpa", "canada.irpr", "canada.immigration_act", "international.refugee_convention")
		)

	def resolve_term(self, term: str, offset: int) -> tuple[str, bool] | None:
		"""Return (instrument_key, explicit) for a short form like "the Act" used at ``offset``.

		Explicit definitions before the offset win, then any explicit definition,
		then defaults (IRPA / IRPR in immigration decisions, or the only Act named).
		"""
		normalized = normalize_term(term)
		if not normalized:
			return None
		alias = lookup_alias(normalized)
		if alias is not None and normalized not in GENERIC_TERMS:
			return alias[0], True
		preceding = [item for item in self.definitions if item.term == normalized and item.offset <= offset]
		if preceding:
			return preceding[-1].instrument_key, True
		anywhere = [item for item in self.definitions if item.term == normalized]
		if anywhere:
			return anywhere[0].instrument_key, True
		return self._default_for(normalized, offset)

	def _default_for(self, term: str, offset: int | None = None) -> tuple[str, bool] | None:
		mentioned = self.mentioned_instruments
		if term in {"act", "loi"}:
			if "canada.irpa" in mentioned or (self.is_immigration_context and "canada.immigration_act" not in mentioned):
				return "canada.irpa", False
			# "The only Act named" is a guess, so it needs the Act to have been named before this use and to be one a
			# decision is likely to mean by "the Act". Court-procedure Acts are cited in passing (judicial review
			# jurisdiction), so a decision about another statute must not have its "the Act" read as one of those.
			acts = [
				key
				for key in mentioned
				if REGISTRY[key].kind == "statute"
				and _is_act(key)
				and key not in _INCIDENTAL_ACTS
				and (offset is None or self.first_mentions.get(key, 0) <= offset)
			]
			return (acts[0], False) if len(acts) == 1 else None
		if term in {"regulations", "règlement"}:
			if "canada.irpr" in mentioned or self.is_immigration_context:
				return "canada.irpr", False
			return None
		if term in {"rules", "règles"}:
			rules = [key for key in mentioned if REGISTRY[key].provision_label == "r." or key == "canada.federal_courts_rules"]
			return (rules[0], False) if len(rules) == 1 else None
		if term == "convention":
			treaties = [key for key in mentioned if REGISTRY[key].kind == "instrument"]
			if len(treaties) == 1:
				return treaties[0], False
			if self.is_immigration_context and not treaties:
				return "international.refugee_convention", False
			return None
		if term == "charter":
			return "canada.charter", False
		return None


# Acts decisions cite in passing for procedure; never the answer to a bare "the Act" by elimination.
_INCIDENTAL_ACTS = frozenset({"canada.federal_courts_act", "canada.interpretation_act", "canada.canada_evidence_act"})


def _is_act(key: str) -> bool:
	citation = REGISTRY[key].citation
	return bool(re.search(r"\bAct\b", citation.split(",")[0]))


def _sentence_starts(text: str) -> list[int]:
	starts = [0]
	for match in _SENTENCE_END_RE.finditer(text):
		position = match.start()
		if text[position] == ".":
			word = re.search(r"([A-Za-z.]+)$", text[max(0, position - 12) : position])
			if word:
				token = word.group(1).strip(".").casefold()
				if token in _NON_TERMINAL_ABBREVIATIONS or len(token) == 1:
					continue
		start = match.end()
		while start < len(text) and text[start].isspace():
			start += 1
		starts.append(start)
	return starts
