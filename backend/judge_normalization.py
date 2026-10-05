"""Deterministic judge-name normalization (no database, no AI).

`parse_judge_name` turns a raw extracted judge string into a `JudgeName` with a
surname, given-name tokens or initials, and an honorific/role flag. `same_person`
and `group_judge_names` use those parts to propose merge groups. Nothing here
writes data: callers apply approved groups through a reversible alias layer.
"""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field

_TITLE_WORDS = (
	r"the\s+honou?rable|l[’']?\s*honorable|honou?rable|hon\.?|madam(?:e)?\s+justice|mr\.?\s+justice|mrs\.?\s+justice|"
	r"chief\s+justice|associate\s+chief\s+justice|associate\s+judge|deputy\s+judge|supernumerary|"
	r"justice|judge|juge\s+en\s+chef|juge|madame|madam|monsieur|mr\.?|mrs\.?|ms\.?|prothonotary|protonotaire|"
	r"member|commissioner|dr\.?"
)
_TITLE_RE = re.compile(rf"\b(?:{_TITLE_WORDS})\b", re.IGNORECASE)
_SUFFIX_RE = re.compile(r"[,\s]+(?:A\.?C\.?J\.?|C\.?J\.?|J\.?A\.?|J\.?F\.?C\.?C\.?|P\.?|J\.?)\s*$", re.IGNORECASE)
_PARTICLES = {"de", "du", "des", "la", "le", "van", "von", "der", "den", "st", "ste", "mc", "mac"}


@dataclass(frozen=True)
class JudgeName:
	raw: str
	surname: str  # lowercased ascii, spaces collapsed, hyphens kept as space
	given: tuple[str, ...] = ()  # lowercased given-name tokens (full words or single letters)
	role: str = "judge"  # judge | prothonotary
	flags: tuple[str, ...] = field(default_factory=tuple)

	@property
	def initials(self) -> str:
		return "".join(token[0] for token in self.given)

	@property
	def key(self) -> str:
		"""Stable grouping key: surname plus first initial (surname only when no given name)."""
		return f"{self.surname}|{self.initials[:1]}"


def _fold(text: str) -> str:
	text = text.replace("’", "'")
	return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def parse_judge_name(raw: str) -> JudgeName | None:
	"""Parse a raw judge string; return None when nothing name-like is left."""
	if not raw or not raw.strip():
		return None
	text = " ".join(_fold(raw).split())
	flags: list[str] = []
	role = "prothonotary" if re.search(r"prothonotary|protonotaire", text, re.IGNORECASE) else "judge"
	# "Gleason, J." / "Gleason J." -> strip trailing role suffix, remember it.
	stripped = _SUFFIX_RE.sub("", text)
	if stripped != text:
		flags.append("suffix")
	text = _TITLE_RE.sub(" ", stripped)
	text = re.sub(r"[^A-Za-z'\-,\. ]+", " ", text)
	text = " ".join(text.split()).strip(" ,.")
	if not text:
		return None
	if "," in text:  # "Surname, Given" form
		surname_part, _, given_part = text.partition(",")
		given_tokens = given_part.replace(".", " ").split()
		flags.append("comma-order")
	else:
		tokens = text.replace(".", " ").split()
		if len(tokens) == 1:
			surname_part, given_tokens = tokens[0], []
		else:
			# Trailing token(s) are the surname; leading single letters / words are given names.
			idx = len(tokens) - 1
			while idx > 0 and tokens[idx - 1].lower() in _PARTICLES:
				idx -= 1
			surname_part, given_tokens = " ".join(tokens[idx:]), tokens[:idx]
	surname = re.sub(r"[\-\s]+", " ", surname_part.lower()).strip()
	surname = re.sub(r"^(mc|mac)\s+", r"\1", surname)
	given = tuple(re.sub(r"[^a-z]", "", t.lower()) for t in given_tokens)
	given = tuple(t for t in given if t)
	if len(surname) < 2 or not re.search(r"[a-z]{2}", surname):
		return None
	return JudgeName(raw=raw, surname=surname, given=given, role=role, flags=tuple(flags))


def _given_compatible(a: JudgeName, b: JudgeName) -> bool:
	if not a.given or not b.given:
		return False  # surname-only never merges on its own; needs review
	for x, y in zip(a.given, b.given):
		if x[0] != y[0]:
			return False
		if len(x) > 1 and len(y) > 1 and x != y:
			return False
	return True


def same_person(a: JudgeName, b: JudgeName) -> bool:
	"""True only for a safe merge: same surname, same role, compatible given names/initials."""
	return a.surname == b.surname and a.role == b.role and _given_compatible(a, b)


@dataclass
class MergeGroup:
	surname: str
	members: list[str]  # raw strings, most frequent first
	canonical: str
	needs_review: list[str] = field(default_factory=list)  # surname-only strings with several candidates


def group_judge_names(counts: dict[str, int]) -> list[MergeGroup]:
	"""Group raw judge strings (value -> decision count) into proposed same-person groups.

	Only groups with 2+ distinct raw strings are returned. Surname-only strings attach to
	a group only when exactly one candidate person has that surname; otherwise they are
	listed under `needs_review`.
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
		if bare:
			if len(clusters) == 1:
				clusters[0].extend(bare)
			elif len(clusters) == 0 and len(bare) > 1:
				clusters.append(list(bare))  # all surname-only variants of one name
			else:
				review = bare
		for cluster in clusters:
			if len(cluster) > 1 or review:
				groups.append(MergeGroup(surname, cluster, max(cluster, key=lambda r: (len(parsed[r].given), counts[r])), review if len(clusters) > 1 or review else []))
	return sorted(groups, key=lambda g: -sum(counts[m] for m in g.members))
