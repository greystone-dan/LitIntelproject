"""Second-pass ("step 2") refinement layers for case citations and statute references.

Pass one (``backend.citations``) is not changed. These layers take its output plus
the full decision text and return corrected rows, each tagged with the step that
produced it. See docs/CITATION_REFINEMENT.md for the merge plan.

Quick use::

    from backend.citation_refine import refine_document
    result = refine_document(case.full_text, source_citations=[case.citation])
    result.cases.rows   # RefinedCitation rows (to_raw_match() gives pass-one shape)
    result.laws.rows    # RefinedStatuteReference rows

Steps can be limited with ``steps=`` or the ``CASELIBRARY_CITATION_REFINE_STEPS``
environment variable ("all", "none", or a comma list such as "C1_gap_scan,L3_expand").
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from dataclasses import dataclass, replace

from ..citations import RawCitationMatch
from .cases import CASE_STEPS, identifier_keys, refine_case_citations
from .context import DocumentContext
from .laws import LAW_STEPS, refine_statute_references, split_provision_list
from .models import (
	ACTION_ADDED,
	ACTION_CORRECTED,
	ACTION_DROPPED,
	ACTION_EXPANDED,
	ACTION_KEPT,
	LayerResult,
	Pinpoint,
	RefinedCitation,
	RefinedStatuteReference,
)
from .pinpoints import parse_pinpoint

ALL_STEPS = CASE_STEPS + LAW_STEPS
STEPS_ENV = "CASELIBRARY_CITATION_REFINE_STEPS"


def enabled_steps(steps: Iterable[str] | None = None) -> frozenset[str]:
	"""Steps to run: the explicit argument, else the environment variable, else all."""
	if steps is not None:
		chosen = frozenset(steps)
	else:
		raw = (os.getenv(STEPS_ENV) or "all").strip()
		if raw.lower() == "all":
			chosen = frozenset(ALL_STEPS)
		elif raw.lower() in {"none", "off", ""}:
			chosen = frozenset()
		else:
			chosen = frozenset(part.strip() for part in raw.split(",") if part.strip())
	unknown = chosen - set(ALL_STEPS)
	if unknown:
		raise ValueError(f"Unknown refinement steps: {', '.join(sorted(unknown))}")
	return chosen


@dataclass
class DocumentRefinement:
	cases: LayerResult
	laws: LayerResult

	def summary(self) -> dict[str, dict[str, int]]:
		return {"cases": self.cases.counts(), "laws": self.laws.counts()}


def _resolve_cross_layer_overlaps(cases: LayerResult, laws: LayerResult) -> None:
	"""Stop a case row and a law row from claiming the same words.

	A real case citation (one with identifiers) beats a law row; a law row beats a
	bare case name (pass one's low-confidence "case_name" rows).
	"""
	drop_cases: list[RefinedCitation] = []
	drop_laws: list[RefinedStatuteReference] = []
	for case_row in cases.rows:
		for law_row in laws.rows:
			if case_row.offset_end <= law_row.offset_start or law_row.offset_end <= case_row.offset_start:
				continue
			if case_row.identifiers:
				drop_laws.append(law_row)
			elif case_row.kind == "case_name":
				drop_cases.append(case_row)
	for row in dict.fromkeys(drop_laws):
		laws.rows.remove(row)
		laws.dropped.append(replace(row, action=ACTION_DROPPED, confidence=0.0, notes=(*row.notes, "cross_layer_overlap")))
	for row in dict.fromkeys(drop_cases):
		cases.rows.remove(row)
		cases.dropped.append(replace(row, action=ACTION_DROPPED, confidence=0.0, notes=(*row.notes, "cross_layer_overlap")))


def refine_document(
	text: str | None,
	*,
	pass_one_case_rows: list[RawCitationMatch] | None = None,
	pass_one_statute_rows: list[RawCitationMatch] | None = None,
	steps: Iterable[str] | None = None,
	source_citations: Iterable[str | None] = (),
	current_year: int | None = None,
	source_dockets: Iterable[str | None] | None = None,
) -> DocumentRefinement:
	"""Run both refinement layers over one decision and reconcile them."""
	content = text or ""
	chosen = enabled_steps(steps)
	context = DocumentContext.build(content)
	cases = refine_case_citations(
		content,
		pass_one_rows=pass_one_case_rows,
		steps=[step for step in CASE_STEPS if step in chosen],
		source_citations=source_citations,
		current_year=current_year,
		source_dockets=source_dockets,
	)
	laws = refine_statute_references(
		content,
		pass_one_rows=pass_one_statute_rows,
		steps=[step for step in LAW_STEPS if step in chosen],
		context=context,
	)
	_resolve_cross_layer_overlaps(cases, laws)
	return DocumentRefinement(cases=cases, laws=laws)


__all__ = [
	"ACTION_ADDED",
	"ACTION_CORRECTED",
	"ACTION_DROPPED",
	"ACTION_EXPANDED",
	"ACTION_KEPT",
	"ALL_STEPS",
	"CASE_STEPS",
	"DocumentContext",
	"DocumentRefinement",
	"LAW_STEPS",
	"LayerResult",
	"Pinpoint",
	"RefinedCitation",
	"RefinedStatuteReference",
	"enabled_steps",
	"identifier_keys",
	"parse_pinpoint",
	"refine_case_citations",
	"refine_document",
	"refine_statute_references",
	"split_provision_list",
]
