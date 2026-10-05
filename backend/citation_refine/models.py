"""Data shapes shared by the case and law refinement layers.

Every refined row records which step produced it (``step``), what the step did
to the pass-one result (``action``) and a confidence score, so the layers can be
run in shadow mode and compared against the first pass before being merged.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..citations import RawCitationMatch

# What a refinement step did relative to the first pass.
ACTION_KEPT = "kept"  # pass-one row unchanged (possibly enriched with metadata)
ACTION_CORRECTED = "corrected"  # pass-one row replaced by a better span or normalization
ACTION_ADDED = "added"  # new row the first pass missed
ACTION_EXPANDED = "expanded"  # one row produced by splitting a pass-one list/range
ACTION_DROPPED = "dropped"  # pass-one row judged to be noise

PINPOINT_PARAGRAPH = "paragraph"
PINPOINT_PAGE = "page"
PINPOINT_FOOTNOTE = "footnote"


@dataclass(frozen=True)
class Pinpoint:
	"""A structured pinpoint: which paragraphs or pages of the target are cited."""

	kind: str
	raw: str
	values: tuple[int, ...]
	is_range_or_list: bool = False
	truncated: bool = False
	# "para 45 ff" / "et seq": the author means 45 and an unstated number of following paragraphs.
	# ``values`` holds only the stated numbers; the extent is never guessed.
	open_ended: bool = False

	def display(self) -> str:
		label = {"paragraph": "para", "page": "p.", "footnote": "n."}.get(self.kind, self.kind)
		if len(self.values) == 1:
			return f"{label} {self.values[0]}" + (" ff" if self.open_ended else "")
		return f"{label} {self.values[0]}-{self.values[-1]}" if self._is_contiguous() else f"{label} " + ", ".join(
			str(value) for value in self.values
		)

	def _is_contiguous(self) -> bool:
		return all(b - a == 1 for a, b in zip(self.values, self.values[1:]))


@dataclass(frozen=True)
class RefinedCitation:
	"""A case-layer row after the second pass."""

	kind: str
	citation_text: str
	normalized_citation: str
	offset_start: int
	offset_end: int
	step: str
	action: str
	confidence: float
	pinpoint: str | None = None
	pinpoints: tuple[Pinpoint, ...] = ()
	anchor_citation_text: str | None = None
	anchor_offset_start: int | None = None
	anchor_offset_end: int | None = None
	declared_alias: str | None = None
	case_name: str | None = None
	identifiers: tuple[str, ...] = ()
	language: str = "en"
	notes: tuple[str, ...] = ()
	replaces: tuple[tuple[int, int, str], ...] = ()

	def to_raw_match(self) -> RawCitationMatch:
		"""Return the pass-one compatible shape used by the existing writers."""
		return RawCitationMatch(
			kind=self.kind,
			citation_text=self.citation_text,
			normalized_citation=self.normalized_citation,
			offset_start=self.offset_start,
			offset_end=self.offset_end,
			pinpoint=self.pinpoint,
			anchor_citation_text=self.anchor_citation_text,
			anchor_offset_start=self.anchor_offset_start,
			anchor_offset_end=self.anchor_offset_end,
			declared_alias=self.declared_alias,
		)


@dataclass(frozen=True)
class RefinedStatuteReference:
	"""A law-layer row after the second pass.

	Rows produced by expanding a list ("ss. 96, 97") share ``group_start`` /
	``group_end`` (the original span) and carry their position in ``group_index``.
	"""

	kind: str
	citation_text: str
	normalized_citation: str
	offset_start: int
	offset_end: int
	step: str
	action: str
	confidence: float
	instrument_key: str | None = None
	instrument_citation: str | None = None
	provision: str | None = None
	section: str | None = None
	subsection: str | None = None
	paragraph: str | None = None
	subparagraph: str | None = None
	nested_depth: int | None = None
	legislation_url: str | None = None
	group_start: int | None = None
	group_end: int | None = None
	group_index: int | None = None
	group_size: int | None = None
	language: str = "en"
	notes: tuple[str, ...] = ()
	replaces: tuple[tuple[int, int, str], ...] = ()

	@property
	def provision_path(self) -> tuple[str, ...]:
		return tuple(part for part in (self.section, self.subsection, self.paragraph, self.subparagraph) if part)

	def to_raw_match(self) -> RawCitationMatch:
		return RawCitationMatch(
			kind=self.kind,
			citation_text=self.citation_text,
			normalized_citation=self.normalized_citation,
			offset_start=self.offset_start,
			offset_end=self.offset_end,
		)


@dataclass
class LayerResult:
	"""Output of one refinement layer."""

	rows: list
	dropped: list = field(default_factory=list)
	steps_run: tuple[str, ...] = ()

	def counts(self) -> dict[str, int]:
		summary: dict[str, int] = {}
		for row in [*self.rows, *self.dropped]:
			key = f"{row.step}:{row.action}"
			summary[key] = summary.get(key, 0) + 1
		return dict(sorted(summary.items()))
