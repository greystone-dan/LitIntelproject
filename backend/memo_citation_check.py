"""Memo citation check: analyze uploaded documents for citation completeness.

Extends live document analysis to provide:
- Treatment flags (negative/later treatment status)
- Commonly cited authorities on same issues
- Missing authority identification
"""

from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy import func, select, and_

from .database import Case, Citation
from .memo_authority_suggestions import build_authority_suggestions
from .memo_gap_check import build_memo_gap_suggestions
from .live_analysis import (
	analyze_document,
	LiveParagraph,
	_citation_variants,
	_case_alias_terms,
	_paragraph_for_offset,
	_context,
)


def _get_treatment_status(session: Session, target_case_id: int) -> dict[str, Any]:
	"""Get treatment status of a case (whether it's been overruled, applied, etc.)."""
	if not target_case_id:
		return {}

	# Get all citations to this case
	citations = session.query(Citation).filter(
		Citation.target_case_id == target_case_id
	).all()

	if not citations:
		return {
			"has_treatment": False,
			"treatment_flags": [],
			"citing_cases_count": 0,
		}

	# Analyze citation kinds to determine treatment
	treatment_flags = []
	citation_kinds = [c.citation_kind for c in citations if c.citation_kind]

	# Detect treatment based on citation kind values
	if any(k and k.lower() in {"overruled", "reversed", "quashed"} for k in citation_kinds):
		treatment_flags.append("negative_treatment")
	elif any(k and k.lower() in {"applied", "followed", "applied_with_modification"} for k in citation_kinds):
		treatment_flags.append("positive_treatment")

	return {
		"has_treatment": len(treatment_flags) > 0,
		"treatment_flags": treatment_flags,
		"citing_cases_count": len(citations),
	}


def _find_related_authorities(
	session: Session,
	case_id: int,
	limit: int = 5,
) -> list[dict[str, Any]]:
	"""Find commonly cited authorities that share issues with the given case."""
	if not case_id:
		return []

	case = session.query(Case).filter(Case.id == case_id).first()
	if not case or not case.issues:
		return []

	# Find other high-citation cases with shared issues (in-app filtering)
	related_cases_query = (
		session.query(Case)
		.filter(Case.id != case_id)
		.order_by(Case.citing_cases_count.desc().nulls_last())
		.limit(limit * 3)
		.all()
	)

	result = []
	for related_case in related_cases_query:
		if not related_case.issues:
			continue
		# Check if there's overlap between issues
		overlap = bool(set(case.issues) & set(related_case.issues))
		if overlap:
			result.append({
				"id": related_case.id,
				"title": related_case.title,
				"citation": related_case.citation,
				"court": related_case.court,
				"date": related_case.date.isoformat() if related_case.date else None,
				"citing_count": related_case.citing_cases_count or 0,
				"issues": related_case.issues or [],
			})
			if len(result) >= limit:
				break

	return result


def analyze_memo_citations(
	content: bytes,
	filename: str,
	content_type: str | None = None,
	session: Session | None = None,
) -> dict[str, Any]:
	"""Analyze a memo/draft document for citation completeness and treatment.

	Returns:
	- All cited authorities with resolution status
	- Treatment flags (negative/later treatment) where available
	- Commonly cited authorities on same issues that are missing from the draft
	"""
	# First, do the standard live analysis
	analysis = analyze_document(content, filename, content_type, session)
	analysis = {
		**analysis,
		"suggestions": build_authority_suggestions(analysis, session),
		"gap_suggestions": build_memo_gap_suggestions(analysis, session),
	}

	if not session:
		return analysis

	# Enhance case citations with treatment info
	enhanced_case_citations = []
	for citation_row in analysis["case_citations"]:
		case_id = citation_row.get("resolved_case_id")
		treatment = _get_treatment_status(session, case_id) if case_id else {}
		related = _find_related_authorities(session, case_id) if case_id else []

		enhanced_case_citations.append({
			**citation_row,
			"treatment": treatment,
			"related_authorities": related,
		})

	# Analyze what authorities are missing
	cited_case_ids = {
		c.get("resolved_case_id")
		for c in enhanced_case_citations
		if c.get("resolved_case_id")
	}

	# Find all commonly discussed issues in cited cases
	all_issues = set()
	for case_id in cited_case_ids:
		if case_id:
			case = session.query(Case).filter(Case.id == case_id).first()
			if case and case.issues:
				all_issues.update(case.issues)

	# Find authorities on these issues that weren't cited
	missing_authorities = []
	if all_issues:
		# Get uncited cases with shared issues
		uncited_cases = (
			session.query(Case)
			.filter(~Case.id.in_(cited_case_ids))
			.order_by(Case.citing_cases_count.desc().nulls_last())
			.limit(20)
			.all()
		)

		for case in uncited_cases:
			if case.issues and any(issue in all_issues for issue in case.issues):
				missing_authorities.append({
					"id": case.id,
					"title": case.title,
					"citation": case.citation,
					"court": case.court,
					"date": case.date.isoformat() if case.date else None,
					"citing_count": case.citing_cases_count or 0,
					"issues": case.issues or [],
					"reason": "Commonly cited on issues present in draft but not cited",
				})
			if len(missing_authorities) >= 10:
				break

	return {
		**analysis,
		"case_citations": enhanced_case_citations,
		"missing_authorities": missing_authorities,
		"memo_analysis": {
			"total_authorities_cited": len(enhanced_case_citations),
			"resolved_authorities": sum(1 for c in enhanced_case_citations if c.get("resolved_case_id")),
			"authorities_with_treatment": sum(1 for c in enhanced_case_citations if c.get("treatment", {}).get("has_treatment")),
			"missing_authorities_found": len(missing_authorities),
		},
	}
