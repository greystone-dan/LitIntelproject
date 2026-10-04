"""Additive issue-brief summaries derived from stored outcome metadata."""

from __future__ import annotations

from typing import Any

from .judge_issue_record import _issue_outcome_category


def minister_win_rates_by_year(cases: list[Any]) -> dict[int | None, dict[str, Any]]:
	"""Return Minister-win rates by year with explicit total/classified n values.

	The rate is Minister wins divided by classified government outcomes (won,
	lost, or mixed). ``n`` is all tagged decisions in the year; unclassified
	outcomes are disclosed and are not silently treated as losses.
	"""
	grouped: dict[int | None, dict[str, int]] = {}
	for case in cases:
		year = case.date.year if case.date else None
		group = grouped.setdefault(
			year, {"n": 0, "minister_wins": 0, "unclassified_count": 0}
		)
		group["n"] += 1
		category = _issue_outcome_category(case.metadata_json)
		if category == "minister_win":
			group["minister_wins"] += 1
		elif category == "unclassified":
			group["unclassified_count"] += 1

	result: dict[int | None, dict[str, Any]] = {}
	for year, counts in grouped.items():
		classified_n = counts["n"] - counts["unclassified_count"]
		result[year] = {
			"minister_wins": counts["minister_wins"],
			"rate": (
				round(counts["minister_wins"] / classified_n * 100, 1)
				if classified_n
				else None
			),
			"n": counts["n"],
			"classified_n": classified_n,
			"unclassified_count": counts["unclassified_count"],
		}
	return result


def minister_win_rate_label(summary: dict[str, Any] | None) -> str:
	"""Format the auditable Minister-win statistic for page and DOCX tables."""
	if not summary:
		return "—"
	rate = "n/a" if summary.get("rate") is None else f"{summary['rate']:.1f}%"
	return (
		f"{rate} (wins {int(summary.get('minister_wins') or 0)} / classified n "
		f"{int(summary.get('classified_n') or 0)}; n {int(summary.get('n') or 0)}, "
		f"unclassified {int(summary.get('unclassified_count') or 0)})"
	)
