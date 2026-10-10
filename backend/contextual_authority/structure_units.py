"""Discussion units cut along the decision's skeleton (no AI).

The live units come from paragraph-to-paragraph similarity. These come from ``case_structure``: every paragraph gets a
role (header, overview, facts, issues, analysis, disposition) in skeleton order, a unit is a run of one role, and the
analysis is also cut at each major heading. On hand-labelled decisions this found the true unit starts far more often
(63.7% exact on two hold-outs, against 22.9% for the similarity units) and was right more often when it cut (62% against 18%).

``structure_report`` takes a report from ``scripts.inspect_discussion_units.inspect_case`` and returns a copy whose
``discussion_units`` are the structure units, in the same shape, so the reader, party arguments and markup need no change.
The original sub-themes are kept: each goes to the structure unit that holds its first paragraph.
"""

from __future__ import annotations

from typing import Any

from .case_structure import label_paragraph_roles, structural_unit_starts

STRUCTURE_UNITS_METHOD = "case_structure_units_v1"


def structure_report(report: dict[str, Any]) -> dict[str, Any]:
	"""Copy of ``report`` with structure-based discussion units; the report is returned unchanged when it has no text."""
	paragraphs = sorted(report.get("paragraphs", []), key=lambda paragraph: paragraph["paragraph_index"])
	if not paragraphs or not report.get("discussion_units"):
		return report
	texts = [paragraph.get("text") or "" for paragraph in paragraphs]
	indexes = [paragraph["paragraph_index"] for paragraph in paragraphs]
	roles = label_paragraph_roles(texts)
	starts = structural_unit_starts(texts, roles, split_analysis_headings=True)
	bounds = starts + [len(texts)]
	prefix = report["discussion_units"][0]["discussion_unit_id"].rsplit(":", 1)[0]
	units: list[dict[str, Any]] = []
	for position, (a, b) in enumerate(zip(bounds, bounds[1:])):
		units.append(
			{
				"discussion_unit_id": f"{prefix}:{position}",
				"start_paragraph": indexes[a],
				"end_paragraph": indexes[b - 1],
				"paragraph_count": b - a,
				"structure_role": roles[a],
				"generation_method": STRUCTURE_UNITS_METHOD,
				"subthemes": [],
			}
		)
	if not units:
		return report
	for original in report["discussion_units"]:
		for subtheme in original.get("subthemes", []):
			first = min(subtheme.get("paragraph_indices") or [original["start_paragraph"]])
			target = next((u for u in units if u["start_paragraph"] <= first <= u["end_paragraph"]), units[-1])
			target["subthemes"].append(subtheme)
	return {**report, "discussion_units": units, "discussion_unit_count": len(units), "unit_source": STRUCTURE_UNITS_METHOD}
