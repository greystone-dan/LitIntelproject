"""Resolve refined citation rows to library cases (side tables only).

The index is built from ``cases.citation`` / ``cases.secondary_citation`` with the same ``identifier_keys`` the refinement
puts on its rows, so keys match on both sides (French court codes map to the English ones). A key that belongs to more than
one case is ambiguous and never links. Name-only rows are not linked here: they carry no citation to look up.
"""

from __future__ import annotations

from collections.abc import Iterable

from .cases import identifier_keys

LINKABLE_KINDS = frozenset({"neutral", "case", "case_short"})


def build_case_key_index(rows: Iterable[tuple[int, str | None, str | None]]) -> dict[str, int | None]:
	"""key -> case id, or None when two cases share the key. ``rows`` are (case id, citation, secondary citation)."""
	index: dict[str, int | None] = {}
	for case_id, citation, secondary in rows:
		for value in (citation, secondary):
			for key in identifier_keys(value):
				if key not in index:
					index[key] = case_id
				elif index[key] != case_id:
					index[key] = None
	return index


def resolve_refined_row(
	kind: str,
	citation_text: str | None,
	normalized_citation: str | None,
	source_case_id: int,
	index: dict[str, int | None],
) -> int | None:
	"""Case id this refined row cites, or None (not in the library, ambiguous, name-only or a self-citation)."""
	if kind not in LINKABLE_KINDS:
		return None
	hits: set[int] = set()
	for value in (normalized_citation, citation_text):
		for key in identifier_keys(value):
			target = index.get(key)
			if target is not None:
				hits.add(target)
		if hits:
			break
	if len(hits) != 1:
		return None
	target = next(iter(hits))
	return None if target == source_case_id else target
