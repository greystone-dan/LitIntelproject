"""Read-only aggregation of judge-linked recorded issues and their outcomes."""

from __future__ import annotations

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import Case, CaseJudgeProfile, JudgeProfile

_JUDGE_ISSUE_MINIMUM_DECISIONS = 10
_FEDERAL_COURT_NAMES = {"fc", "federal court", "federal court of canada"}
_ISSUE_OUTCOME_CATEGORIES = ("minister_win", "applicant_win", "other", "unclassified")


def _stored_issue_labels(value: Any) -> set[str]:
	if not isinstance(value, list):
		return set()
	return {
		" ".join(label.split()).casefold()
		for label in value
		if isinstance(label, str) and label.strip()
	}


def _issue_outcome_category(metadata_json: Any) -> str:
	metadata = metadata_json if isinstance(metadata_json, dict) else {}
	reader = metadata.get("reader_extracted")
	reader = reader if isinstance(reader, dict) else {}
	outcome = reader.get("government outcome")
	if not isinstance(outcome, str) or not outcome.strip():
		return "unclassified"
	normalized = outcome.strip().casefold()
	if normalized == "won":
		return "minister_win"
	if normalized == "lost":
		return "applicant_win"
	if normalized == "mixed":
		return "other"
	return "unclassified"


def _issue_outcome_summary(cases: list[Any]) -> dict[str, Any]:
	denominator = len(cases)
	counts = {category: 0 for category in _ISSUE_OUTCOME_CATEGORIES}
	for case in cases:
		counts[_issue_outcome_category(case.metadata_json)] += 1
	return {
		category: {
			"count": count,
			"denominator": denominator,
			"percent": round(count / denominator * 100, 1) if denominator else None,
		}
		for category, count in counts.items()
	}


def fetch_judge_profile_issues(db: Session, slug: str) -> dict[str, Any]:
	"""Aggregate stored issue outcomes for one exact canonical judge profile.

	Issue labels come only from ``cases.issues`` and outcome ownership only from
	``reader_extracted.government outcome``. ``won`` is a Minister win, ``lost``
	is an applicant win, and ``mixed`` is other. Missing, blank, undetermined,
	and unrecognized values are unclassified. Outcome percentages use each
	issue's full decision count.
	"""
	with db.no_autoflush:
		profile = db.execute(
			select(JudgeProfile.id, JudgeProfile.slug, JudgeProfile.display_name)
			.where(JudgeProfile.slug == slug.strip())
		).first()
		if profile is None:
			return {"status": "unknown_judge"}

		linked_ids = select(CaseJudgeProfile.case_id).where(
			CaseJudgeProfile.judge_profile_id == profile.id
		)
		judge_cases = list(db.execute(
			select(Case.id, Case.issues, Case.metadata_json)
			.where(Case.id.in_(linked_ids))
			.order_by(Case.id)
		))
		judge_by_issue: dict[str, list[Any]] = {}
		for case in judge_cases:
			for issue in _stored_issue_labels(case.issues):
				judge_by_issue.setdefault(issue, []).append(case)

		visible_issues = {
			issue for issue, cases in judge_by_issue.items()
			if len(cases) >= _JUDGE_ISSUE_MINIMUM_DECISIONS
		}
		federal_court_cases = list(db.execute(
			select(Case.id, Case.issues, Case.metadata_json, Case.court)
			.where(func.lower(func.trim(Case.court)).in_(tuple(_FEDERAL_COURT_NAMES)))
			.order_by(Case.id)
		))
		baseline_by_issue: dict[str, list[Any]] = {issue: [] for issue in visible_issues}
		federal_court_decisions = len(federal_court_cases)
		for case in federal_court_cases:
			for issue in _stored_issue_labels(case.issues) & visible_issues:
				baseline_by_issue[issue].append(case)

		issues = []
		for issue in sorted(visible_issues):
			judge_issue_cases = judge_by_issue[issue]
			baseline_issue_cases = baseline_by_issue[issue]
			issues.append({
				"issue": issue,
				"judge": {
					"decisions": {
						"count": len(judge_issue_cases),
						"denominator": len(judge_cases),
					},
					"outcomes": _issue_outcome_summary(judge_issue_cases),
				},
				"federal_court_baseline": {
					"decisions": {
						"count": len(baseline_issue_cases),
						"denominator": federal_court_decisions,
					},
					"outcomes": _issue_outcome_summary(baseline_issue_cases),
				},
			})

		return {
			"status": "ok",
			"profile": {"slug": profile.slug, "display_name": profile.display_name},
			"issues": issues,
			"hidden_issue_count": sum(
				len(cases) < _JUDGE_ISSUE_MINIMUM_DECISIONS for cases in judge_by_issue.values()
			),
			"metadata": {
				"issue_source": "cases.issues; whitespace collapsed and casefolded; distinct per decision; no fallback",
				"outcome_source": "cases.metadata_json.reader_extracted.government outcome",
				"outcome_mapping": {
					"won": "minister_win",
					"lost": "applicant_win",
					"mixed": "other",
					"missing_blank_undetermined_or_unrecognized_values": "unclassified",
				},
				"minimum_decisions_per_visible_issue": _JUDGE_ISSUE_MINIMUM_DECISIONS,
				"hidden_issue_count": "number of distinct judge-linked stored issues below the minimum; labels are not returned",
				"count_unit": "distinct decisions",
				"denominators": {
					"judge_decisions": "all decisions linked to the canonical judge profile",
					"federal_court_baseline_decisions": "all decisions whose stored court is FC, Federal Court, or Federal Court of Canada",
					"outcome_counts_and_percentages": "all decisions for that issue and cohort, including unclassified",
				},
				"interpretation": "Recorded coverage only; not a ranking, harshness measure, or finding that an issue determined the outcome.",
			},
		}
