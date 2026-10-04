"""Analytics, judge profile, and Federal Court activity service for AI CaseLibrary.

Owns SQL aggregation queries for judge outcomes, yearly trends, data explorer cross-tabulations,
judge profile resolution and filtering, and Federal Court activity timelines.
"""

from __future__ import annotations

import re
from typing import Any

import httpx
from fastapi import HTTPException, status
from sqlalchemy import bindparam, case, func, or_, select, text as sql_text
from sqlalchemy.orm import Session

from fc_ingest.document_scraper import _JUDGE_JUNK_PATTERN
from scripts.fetch_fc_procedural_history import HEADERS, process_imm, upsert_result
from .database import (
	Case,
	CaseChunk,
	CaseChunkEmbedding,
	CaseJudgeProfile,
	CaseSource,
	CaseTag,
	Citation,
	CitationMetrics,
	FCActivityCase,
	FCActivityClassification,
	FCActivityDocument,
	FCProceduralHistory,
	IngestionRun,
	JudgeProfile,
	StatuteReference,
)
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from .search_matching import identity_sql, matched_on_sql

FC_ACTIVITY_DISPLAY_START_YEAR = 2003

FC_CITY_PROVINCE = {
	"Calgary": "Alberta",
	"Edmonton": "Alberta",
	"Charlottetown": "Prince Edward Island",
	"Fredericton": "New Brunswick",
	"Saint John": "New Brunswick",
	"Halifax": "Nova Scotia",
	"Montréal": "Quebec",
	"Québec": "Quebec",
	"Ottawa": "Ontario",
	"Toronto": "Ontario",
	"Regina": "Saskatchewan",
	"Saskatoon": "Saskatchewan",
	"St. John's": "Newfoundland and Labrador",
	"Vancouver": "British Columbia",
	"Whitehorse": "Yukon",
	"Winnipeg": "Manitoba",
	"Yellowknife": "Northwest Territories",
}

_ANALYTICS_FIELDS = {
	"judge": ("Judge", "metadata_json->'reader_extracted'->>'judge'"),
	"court": ("Court", "court"),
	"decision_year": (
		"Decision year",
		"SUBSTRING(COALESCE(metadata_json->'reader_extracted'->>'date', '') FROM 1 FOR 4)",
	),
	"decision_outcome": (
		"Decision outcome",
		"metadata_json->'reader_extracted'->>'decision outcome'",
	),
	"government_role": (
		"Government role",
		"metadata_json->'reader_extracted'->>'government role'",
	),
	"government_outcome": (
		"Government outcome",
		"metadata_json->'reader_extracted'->>'government outcome'",
	),
}


def _profile_reader_metadata(case: Case) -> dict[str, Any]:
	raw_metadata = case.metadata_json
	metadata: dict[str, Any] = raw_metadata if isinstance(raw_metadata, dict) else {}
	reader_value = metadata.get("reader_extracted")
	return reader_value if isinstance(reader_value, dict) else {}


def _government_party(case: Case) -> str | None:
	match = re.search(r"\bCanada\s+\(([^)]+)\)", case.title or "", flags=re.IGNORECASE)
	return " ".join(match.group(1).split()) if match else None


def _judge_outcome_counts(cases: list[Case]) -> dict[str, int | float | None]:
	counts = {"government_wins": 0, "individual_wins": 0, "unclassified": 0}
	for case in cases:
		outcome = _profile_reader_metadata(case).get("government outcome")
		if outcome == "won":
			counts["government_wins"] += 1
		elif outcome == "lost":
			counts["individual_wins"] += 1
		else:
			counts["unclassified"] += 1
	classified = counts["government_wins"] + counts["individual_wins"]
	counts["classified"] = classified
	counts["all_linked"] = len(cases)
	counts["government_win_rate"] = (
		round(counts["government_wins"] / classified * 100, 1) if classified else None
	)
	return counts


def _analytics_case_order_sql(
	query: str,
	sort_by: str,
	*,
	minister_expression: str = "SUBSTRING(c.title FROM 'Canada [(]([^)]*)[)]')",
	search_full_text: bool = False,
) -> tuple[str, dict[str, Any]]:
	query = " ".join(query.split())
	params: dict[str, Any] = {}
	if query and sort_by == "relevance":
		params["query_exact"] = query
		params["query_like"] = f"%{query}%"
		params["query_exact_like"] = f"%{query}%"
		ranking = """
			CASE
				WHEN LOWER(COALESCE(c.title, '')) LIKE LOWER(:query_exact_like) THEN 1000
				WHEN LOWER(COALESCE(c.citation, '')) LIKE LOWER(:query_exact_like) THEN 900
				WHEN LOWER(COALESCE(c.title, '')) = LOWER(:query_exact) THEN 850
				WHEN LOWER(COALESCE(c.citation, '')) = LOWER(:query_exact) THEN 800
		"""
		if search_full_text:
			ranking += """
				WHEN LOWER(COALESCE(c.full_text, '')) LIKE LOWER(:query_like) THEN 700
				WHEN LOWER(COALESCE(c.summary, '')) LIKE LOWER(:query_like) THEN 600
			"""
		ranking += """
				ELSE 0
			END DESC,
			c.date DESC NULLS LAST,
			c.id DESC
			"""
		citation, party, match_params = identity_sql(query)
		params.update(match_params)
		return f"CASE WHEN {citation} THEN 2 WHEN {party} THEN 1 ELSE 0 END DESC, " + ranking, params
	if sort_by == "newest":
		return ("c.date DESC NULLS LAST, c.id DESC", params)
	if sort_by == "oldest":
		return ("c.date ASC NULLS LAST, c.id ASC", params)
	if sort_by == "minister":
		return (
			f"COALESCE({minister_expression}, 'Unknown') ASC, c.date DESC NULLS LAST, c.id DESC",
			params,
		)
	return ("c.date DESC NULLS LAST, c.id DESC", params)


def fetch_outcomes_by_year(db: Session) -> list[dict[str, Any]]:
	rows = db.execute(
		sql_text(
			"""
			SELECT
				EXTRACT(YEAR FROM date)::int AS year,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'government outcome' = 'won') AS government_wins,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'government outcome' = 'lost') AS individual_wins,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'decision outcome' IN ('allowed', 'granted', 'set_aside', 'remitted')) AS relief_decisions,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'decision outcome' IN ('dismissed', 'denied', 'refused')) AS dismissed_decisions
			FROM cases
			WHERE date IS NOT NULL
			GROUP BY year
			HAVING COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'government outcome' IN ('won', 'lost')) > 0
			ORDER BY year
			"""
		)
	).mappings().all()
	result: list[dict[str, Any]] = []
	for row in rows:
		government_wins = int(row["government_wins"] or 0)
		individual_wins = int(row["individual_wins"] or 0)
		relief_decisions = int(row["relief_decisions"] or 0)
		dismissed_decisions = int(row["dismissed_decisions"] or 0)
		classified = government_wins + individual_wins
		result.append(
			{
				"year": int(row["year"]),
				"government_wins": government_wins,
				"individual_wins": individual_wins,
				"classified": classified,
				"relief_decisions": relief_decisions,
				"dismissed_decisions": dismissed_decisions,
				"government_win_rate": round(government_wins / classified * 100, 1),
				"individual_win_rate": round(individual_wins / classified * 100, 1),
			}
		)
	return result


def fetch_data_explorer_analytics(
	db: Session,
	*,
	group_by: str = "judge",
	split_by: str = "government_outcome",
	limit: int = 50,
) -> dict[str, Any]:
	if group_by not in _ANALYTICS_FIELDS or split_by not in _ANALYTICS_FIELDS:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported analytics field"
		)
	limit = max(1, min(limit, 100))
	group_label, group_expression = _ANALYTICS_FIELDS[group_by]
	split_label, split_expression = _ANALYTICS_FIELDS[split_by]
	query = sql_text(
		f"""
		WITH grouped AS (
			SELECT
				COALESCE(NULLIF({group_expression}, ''), 'Unknown') AS group_value,
				COALESCE(NULLIF({split_expression}, ''), 'Unknown') AS split_value,
				COUNT(*) AS decisions
			FROM cases
			GROUP BY group_value, split_value
		), totals AS (
			SELECT group_value, SUM(decisions) AS total_decisions
			FROM grouped
			GROUP BY group_value
			ORDER BY total_decisions DESC, group_value ASC
			LIMIT :limit
		)
		SELECT grouped.group_value, grouped.split_value, grouped.decisions, totals.total_decisions
		FROM grouped JOIN totals USING (group_value)
		ORDER BY totals.total_decisions DESC, grouped.group_value ASC, grouped.decisions DESC, grouped.split_value ASC
		"""
	)
	rows = db.execute(query, {"limit": limit}).mappings().all()
	groups: dict[str, dict[str, Any]] = {}
	split_values: list[str] = []
	for row in rows:
		group_value = str(row["group_value"])
		split_value = str(row["split_value"])
		if split_value not in split_values:
			split_values.append(split_value)
		group = groups.setdefault(
			group_value,
			{"value": group_value, "decisions": int(row["total_decisions"]), "breakdown": {}},
		)
		group["breakdown"][split_value] = int(row["decisions"])
	result_groups = list(groups.values())
	return {
		"fields": [{"key": key, "label": label} for key, (label, _) in _ANALYTICS_FIELDS.items()],
		"group_by": {"key": group_by, "label": group_label},
		"split_by": {"key": split_by, "label": split_label},
		"split_values": split_values,
		"groups": result_groups,
		"totals": {"decisions": sum(group["decisions"] for group in result_groups)},
	}


def fetch_about_stats(db: Session) -> dict[str, int]:
	return {
		"cases": int(db.scalar(select(func.count(Case.id))) or 0),
		"case_chunks": int(db.scalar(select(func.count(CaseChunk.id))) or 0),
		"case_sources": int(db.scalar(select(func.count(CaseSource.id))) or 0),
		"ingestion_runs": int(db.scalar(select(func.count(IngestionRun.id))) or 0),
		"citations": int(db.scalar(select(func.count(Citation.id))) or 0),
		"linked_citations": int(
			db.scalar(select(func.count(Citation.id)).where(Citation.target_case_id.is_not(None)))
			or 0
		),
		"judge_profiles": int(db.scalar(select(func.count(JudgeProfile.id))) or 0),
		"case_judge_profiles": int(db.scalar(select(func.count(CaseJudgeProfile.id))) or 0),
		"citation_metrics": int(db.scalar(select(func.count(CitationMetrics.case_id))) or 0),
		"statute_references": int(db.scalar(select(func.count(StatuteReference.id))) or 0),
		"case_tags": int(
			db.scalar(
				select(func.count(CaseTag.id)).where(
					CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
				)
			)
			or 0
		),
		"case_chunk_embeddings": int(db.scalar(select(func.count(CaseChunkEmbedding.id))) or 0),
		"fc_activity_cases": int(db.scalar(select(func.count(FCActivityCase.id))) or 0),
		"fc_activity_documents": int(db.scalar(select(func.count(FCActivityDocument.id))) or 0),
		"fc_procedural_history": int(db.scalar(select(func.count(FCProceduralHistory.id))) or 0),
	}


def fetch_fc_history_imm(db: Session, imm: str) -> dict[str, Any]:
	normalized = (imm or "").strip().upper()
	if not normalized or not re.fullmatch(r"IMM-\d{1,6}-\d{2,4}", normalized, flags=re.IGNORECASE):
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="Provide an IMM number like IMM-1234-19.",
		)
	try:
		with httpx.Client(headers=HEADERS, follow_redirects=True) as client:
			result = process_imm(client, normalized)
		upsert_result(db, result)
		return result
	except Exception as exc:  # pragma: no cover - network-limited runtime path
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Could not fetch FC history: {exc}"
		)


def fetch_fc_activity_timeline(db: Session, *, city: str = "") -> dict[str, Any]:
	selected_city = city.strip()
	rows = db.execute(
		select(
			FCActivityCase.year.label("year"),
			FCActivityCase.city_filed.label("city"),
			func.count(FCActivityCase.id).label("count"),
		)
		.where(
			FCActivityCase.year.is_not(None),
			FCActivityCase.year >= FC_ACTIVITY_DISPLAY_START_YEAR,
		)
		.group_by(FCActivityCase.year, FCActivityCase.city_filed)
		.order_by(FCActivityCase.year, FCActivityCase.city_filed)
	).all()
	cities = db.scalars(
		select(FCActivityCase.city_filed)
		.where(FCActivityCase.city_filed.is_not(None), FCActivityCase.city_filed != "")
		.distinct()
		.order_by(FCActivityCase.city_filed)
	).all()
	city_counts: dict[str, dict[int, int]] = {}
	province_counts: dict[str, dict[int, int]] = {}
	total_counts: dict[int, int] = {}
	for row in rows:
		year = int(row.year)
		location = str(row.city or "Unknown")
		province = FC_CITY_PROVINCE.get(location, "Unknown")
		city_counts.setdefault(location, {})[year] = int(row.count)
		province_counts.setdefault(province, {})[year] = (
			province_counts.setdefault(province, {}).get(year, 0) + int(row.count)
		)
		total_counts[year] = total_counts.get(year, 0) + int(row.count)
	years = sorted(total_counts)

	def timeline(counts: dict[int, int]) -> list[dict[str, int]]:
		return [{"year": year, "count": counts.get(year, 0)} for year in years]

	province_rows = [
		{"province": province, "rows": timeline(province_counts[province])}
		for province in sorted(province_counts)
	]
	selected_rows = (
		timeline(city_counts.get(selected_city, {})) if selected_city else timeline(total_counts)
	)
	return {
		"city": selected_city or None,
		"cities": list(cities),
		"city_provinces": FC_CITY_PROVINCE,
		"total": (
			sum(total_counts.values())
			if not selected_city
			else sum(row["count"] for row in selected_rows)
		),
		"rows": selected_rows,
		"total_rows": timeline(total_counts),
		"province_rows": [],
	}


def fetch_fc_activity_breakdowns(
	db: Session,
	*,
	city: str = "",
	limit: int = 8,
) -> dict[str, Any]:
	"""Return bounded, structured distributions for the FC History panel."""
	selected_city = city.strip()
	chart_limit = max(1, min(limit, 12))
	filters = [FCActivityCase.year.is_not(None), FCActivityCase.year >= FC_ACTIVITY_DISPLAY_START_YEAR]
	if selected_city:
		filters.append(FCActivityCase.city_filed == selected_city)

	def distribution(column: Any) -> list[dict[str, Any]]:
		label = func.coalesce(func.nullif(column, ""), "Unknown").label("label")
		rows = db.execute(
			select(label, func.count(FCActivityCase.id).label("count"))
			.where(*filters)
			.group_by(label)
			.order_by(func.count(FCActivityCase.id).desc(), label)
			.limit(chart_limit)
		).all()
		return [{"label": str(row.label), "count": int(row.count)} for row in rows]

	return {
		"city": selected_city or None,
		"registry_locations": distribution(FCActivityCase.city_filed),
		"case_classes": distribution(FCActivityCase.case_class),
		"tracks": distribution(FCActivityCase.track),
	}


def fetch_fc_activity_flow(
	db: Session,
	*,
	city: str = "",
	source_type: str = "",
) -> dict[str, Any]:
	"""Return a live, exclusive procedural branch flow for classified activity."""
	classification = FCActivityClassification.classification_json
	direct_review = classification["challenged_decision"]["application_type"].as_string()
	leave_result = classification["leave_decision"]["result"].as_string()
	jr_result = classification["judicial_review_result"]["result"].as_string()
	lifecycle_status = classification["lifecycle_status"]["status"].as_string()
	lifecycle_kind = classification["lifecycle_status"]["status_kind"].as_string()
	branch = case(
		(direct_review == "direct_judicial_review", case(
			(jr_result == "granted", "direct_jr_granted"),
			(jr_result == "dismissed", "direct_jr_dismissed"),
			else_="direct_jr_pending",
		)),
		(leave_result == "refused", "leave_refused"),
		(leave_result == "granted", case(
			(jr_result == "granted", "leave_jr_granted"),
			(jr_result == "dismissed", "leave_jr_dismissed"),
			else_="leave_granted_pending_jr",
		)),
		(lifecycle_status.in_(("active", "abeyance")), "active"),
		(lifecycle_kind.in_(("discontinued", "withdrawn", "administratively_terminated")), "closed_before_leave"),
		else_="unresolved",
	).label("branch")
	statement = select(branch, func.count(FCActivityClassification.id).label("count")).select_from(FCActivityClassification)
	if city.strip():
		statement = statement.where(FCActivityClassification.city_filed == city.strip())
	if source_type.strip():
		statement = statement.where(FCActivityClassification.source_type == source_type.strip())
	counts = {str(row.branch): int(row.count) for row in db.execute(statement.group_by(branch)).all()}
	leaf_keys = (
		"active", "leave_refused", "leave_jr_granted", "leave_jr_dismissed",
		"leave_granted_pending_jr", "direct_jr_granted", "direct_jr_dismissed",
		"direct_jr_pending", "closed_before_leave", "unresolved",
	)
	total = sum(counts.get(key, 0) for key in leaf_keys)
	leave_granted = sum(counts.get(key, 0) for key in ("leave_jr_granted", "leave_jr_dismissed", "leave_granted_pending_jr"))
	direct_jr = sum(counts.get(key, 0) for key in ("direct_jr_granted", "direct_jr_dismissed", "direct_jr_pending"))
	nodes = [
		{"key": "total", "label": "Classified activity cases", "value": total},
		{"key": "active", "label": "Active / live", "value": counts.get("active", 0)},
		{"key": "leave_refused", "label": "Leave dismissed", "value": counts.get("leave_refused", 0)},
		{"key": "leave_granted", "label": "Leave granted", "value": leave_granted},
		{"key": "direct_jr", "label": "Direct JR", "value": direct_jr},
		{"key": "closed_before_leave", "label": "Closed before leave", "value": counts.get("closed_before_leave", 0)},
		{"key": "unresolved", "label": "Unresolved evidence", "value": counts.get("unresolved", 0)},
		{"key": "leave_jr_granted", "label": "JR granted", "value": counts.get("leave_jr_granted", 0)},
		{"key": "leave_jr_dismissed", "label": "JR dismissed", "value": counts.get("leave_jr_dismissed", 0)},
		{"key": "leave_granted_pending_jr", "label": "JR pending / not observed", "value": counts.get("leave_granted_pending_jr", 0)},
		{"key": "direct_jr_granted", "label": "JR granted", "value": counts.get("direct_jr_granted", 0)},
		{"key": "direct_jr_dismissed", "label": "JR dismissed", "value": counts.get("direct_jr_dismissed", 0)},
		{"key": "direct_jr_pending", "label": "JR pending / not observed", "value": counts.get("direct_jr_pending", 0)},
	]
	links = [
		{"source": "total", "target": key, "value": counts.get(key, 0)}
		for key in ("active", "leave_refused", "closed_before_leave", "unresolved")
	]
	links.extend(
		[
			{"source": "total", "target": "leave_granted", "value": leave_granted},
			{"source": "total", "target": "direct_jr", "value": direct_jr},
		]
	)
	links.extend(
		{"source": "leave_granted", "target": key, "value": counts.get(key, 0)}
		for key in ("leave_jr_granted", "leave_jr_dismissed", "leave_granted_pending_jr")
	)
	links.extend(
		{"source": "direct_jr", "target": key, "value": counts.get(key, 0)}
		for key in ("direct_jr_granted", "direct_jr_dismissed", "direct_jr_pending")
	)
	return {
		"city": city.strip() or None,
		"source_type": source_type.strip() or None,
		"total": total,
		"nodes": nodes,
		"links": links,
		"semantics": "exclusive_procedural_branches",
		"note": "Each case is assigned one branch using lifecycle and outcome precedence. Leave, judicial-review, and applicability fields otherwise overlap and are not represented as a cross-field Sankey.",
	}


def fetch_fc_activity_analytics(
	db: Session,
	*,
	x: str = "year",
	group_by: str = "full_history_resolution",
	year_from: int | None = None,
	year_to: int | None = None,
	city: str = "",
	source_type: str = "",
) -> dict[str, Any]:
	allowed_x = {"year", "city", "case_class", "track"}
	allowed_groups = {
		"full_history_resolution",
		"closing_status",
		"leave_context",
		"application_type",
	}
	if x not in allowed_x or group_by not in allowed_groups:
		raise HTTPException(status_code=422, detail="Unsupported FC analytics dimension")
	group_expression = (
		FCActivityClassification.classification_json["challenged_decision"][
			"application_type"
		]
		if group_by == "application_type"
		else FCActivityClassification.classification_json[group_by]["status"]
	).as_string()
	statement = select(
		FCActivityClassification.year,
		FCActivityClassification.city_filed,
		FCActivityClassification.case_class,
		FCActivityClassification.track,
		group_expression.label("group_value"),
	).select_from(FCActivityClassification)
	if year_from is not None:
		statement = statement.where(FCActivityClassification.year >= year_from)
	if year_to is not None:
		statement = statement.where(FCActivityClassification.year <= year_to)
	if city.strip():
		statement = statement.where(FCActivityClassification.city_filed == city.strip())
	if source_type.strip():
		statement = statement.where(
			FCActivityClassification.source_type == source_type.strip()
		)
	rows = db.execute(statement).all()
	def coverage_statement(model: Any):
		statement = select(func.count()).select_from(model)
		if year_from is not None:
			statement = statement.where(model.year >= year_from)
		if year_to is not None:
			statement = statement.where(model.year <= year_to)
		if city.strip():
			statement = statement.where(model.city_filed == city.strip())
		if source_type.strip():
			statement = statement.where(model.source_type == source_type.strip())
		return statement

	case_coverage = coverage_statement(FCActivityCase)
	classification_coverage = coverage_statement(FCActivityClassification)
	activity_case_count = db.scalar(case_coverage) or 0
	classified_case_count = db.scalar(classification_coverage) or 0
	labels: dict[str, str] = {
		"year": "Year filed",
		"city": "City filed",
		"case_class": "Case class",
		"track": "Track",
	}
	counts: dict[tuple[str, str], int] = {}
	for row in rows:
		value = getattr(row, x) if x != "year" else row.year
		x_value = str(value if value is not None and str(value).strip() else "Unknown")
		group_value = str(row.group_value or "Unknown")
		counts[(x_value, group_value)] = counts.get((x_value, group_value), 0) + 1
	x_values = sorted(
		{key[0] for key in counts},
		key=lambda value: (int(value) if value.isdigit() else value),
	)[:60]
	group_values = sorted({key[1] for key in counts})
	source_counts: dict[str, int] = {}
	for row in rows:
		value = row.source_type or "unknown"
		source_counts[value] = source_counts.get(value, 0) + 1
	return {
		"x": x,
		"x_label": labels[x],
		"group_by": group_by,
		"total": sum(counts.values()),
		"source_type": source_type.strip() or None,
		"source_counts": dict(sorted(source_counts.items())),
		"coverage": {
			"activity_cases": activity_case_count,
			"classified_cases": classified_case_count,
			"missing_classifications": max(activity_case_count - classified_case_count, 0),
		},
		"x_values": x_values,
		"groups": [
			{
				"label": group,
				"values": [counts.get((x_value, group), 0) for x_value in x_values],
			}
			for group in group_values
		],
	}


def fetch_judge_profiles(
	db: Session,
	*,
	q: str = "",
	limit: int = 50,
) -> list[dict[str, Any]]:
	term = q.strip()
	if term:
		pattern = f"%{term}%"
		statement = (
			select(JudgeProfile)
			.where(
				or_(
					JudgeProfile.display_name.ilike(pattern),
					JudgeProfile.normalized_name.ilike(pattern),
				)
			)
			.order_by(JudgeProfile.display_name)
		)
		rows = list(db.scalars(statement))
		ordered = sorted(
			rows, key=lambda row: (-len(row.case_links), row.display_name.lower())
		)[: max(1, min(100, limit))]
	else:
		rows = list(db.scalars(select(JudgeProfile)))
		ordered = sorted(
			rows, key=lambda row: (-len(row.case_links), row.display_name.lower())
		)[: max(1, min(100, limit))]
	return [
		{
			"slug": row.slug,
			"display_name": row.display_name,
			"primary_court": row.primary_court,
			"aliases": row.aliases or [],
			"decision_count": len(row.case_links),
		}
		for row in ordered
	]


def _case_influence(case_ids: list[int], db: Session) -> dict[int, tuple[int, int]]:
	"""Per case: distinct citing decisions, and how many of those are FCA or SCC decisions."""
	if not case_ids:
		return {}
	statement = sql_text(
		"SELECT cit.target_case_id AS case_id, "
		"COUNT(DISTINCT cit.source_case_id) AS cited_by, "
		"COUNT(DISTINCT cit.source_case_id) FILTER ("
		"WHERE UPPER(src.court) IN ('FCA', 'SCC', 'FEDERAL COURT OF APPEAL', 'SUPREME COURT OF CANADA')"
		") AS appeal_cited_by "
		"FROM citations cit JOIN cases src ON src.id = cit.source_case_id "
		"WHERE cit.target_case_id IN :case_ids AND cit.source_case_id <> cit.target_case_id "
		"GROUP BY cit.target_case_id"
	).bindparams(bindparam("case_ids", expanding=True))
	rows = db.execute(statement, {"case_ids": case_ids}).all()
	return {int(row.case_id): (int(row.cited_by or 0), int(row.appeal_cited_by or 0)) for row in rows}


def fetch_judge_profile_by_slug(
	db: Session,
	slug: str,
	*,
	ministers: list[str] | None = None,
) -> dict[str, Any]:
	profile = db.scalar(select(JudgeProfile).where(JudgeProfile.slug == slug))
	if profile is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Judge profile not found")
	all_cases = list(
		{case.id: case for link in profile.case_links if (case := link.case) is not None}.values()
	)
	minister_filters = [" ".join(value.split()) for value in (ministers or []) if value.strip()]
	minister_filter_keys = {value.casefold() for value in minister_filters}
	if minister_filter_keys:
		filtered_cases = [
			case
			for case in all_cases
			if _government_party(case) and _government_party(case).casefold() in minister_filter_keys
		]
	else:
		filtered_cases = all_cases
	outcomes = _judge_outcome_counts(filtered_cases)
	years: dict[str, int] = {}
	for case in filtered_cases:
		if case.date:
			year = str(case.date)[:4]
			years[year] = years.get(year, 0) + 1
	influence = _case_influence([case.id for case in filtered_cases], db)
	return {
		"profile": {
			"slug": profile.slug,
			"display_name": profile.display_name,
			"primary_court": profile.primary_court,
			"aliases": profile.aliases or [],
		},
		"filter": {
			"ministers": minister_filters,
			"available_ministers": sorted(
				{_government_party(case) for case in all_cases if _government_party(case)},
				key=str.casefold,
			),
		},
		"outcomes": outcomes,
		"yearly_decisions": [
			{"year": year, "decisions": decisions} for year, decisions in sorted(years.items())
		],
		"decisions": [
			{
				"case_id": case.id,
				"title": case.title,
				"citation": case.citation,
				"court": case.court,
				"date": case.date,
				"government_party": _government_party(case),
				"government_role": _profile_reader_metadata(case).get("government role"),
				"government_outcome": _profile_reader_metadata(case).get("government outcome"),
				"decision_outcome": _profile_reader_metadata(case).get("decision outcome"),
				"case_type": _profile_reader_metadata(case).get("case type"),
				"cited_by_cases": influence.get(case.id, (0, 0))[0],
				"cited_by_appeal_courts": influence.get(case.id, (0, 0))[1],
			}
			for case in sorted(filtered_cases, key=lambda item: item.date or "", reverse=True)
		],
	}


def fetch_analytics_search_cases(
	db: Session,
	*,
	query: str = "",
	cites: str = "",
	government_outcome: str = "",
	decision_outcome: str = "",
	minister: str = "",
	judge: str = "",
	court: str = "",
	year: str = "",
	search_full_text: bool = False,
	sort_by: str = "relevance",
	limit: int = 50,
	offset: int = 0,
	cohort_ids: list[int] | None = None,
) -> dict[str, Any]:
	limit = max(1, min(limit, 100))
	offset = max(0, offset)
	filters = ["TRUE"]
	params: dict[str, Any] = {"limit": limit, "offset": offset}
	if cohort_ids is not None:
		filters.append("c.id IN :cohort_ids")
		params["cohort_ids"] = cohort_ids
	query = " ".join(query.split())
	cites = " ".join(cites.split())
	minister = " ".join(minister.split())
	judge = " ".join(judge.split())
	court = " ".join(court.split())
	year = "".join(character for character in year if character.isdigit())[:4]
	minister_expression = "SUBSTRING(c.title FROM 'Canada [(]([^)]*)[)]')"
	citation_match, party_match, match_params = identity_sql(query)
	params.update(match_params)
	match_label, label_params = matched_on_sql(query, search_full_text=search_full_text)
	params.update(label_params)
	if query:
		params["query"] = f"%{query}%"
		query_fields = f"c.title ILIKE :query OR c.citation ILIKE :query OR {citation_match} OR {party_match}"
		if search_full_text:
			query_fields += " OR c.full_text ILIKE :query OR c.summary ILIKE :query"
		filters.append(f"({query_fields})")
	if cites:
		params["cites"] = f"%{cites}%"
		filters.append(
			"EXISTS (SELECT 1 FROM citations cited WHERE cited.source_case_id = c.id "
			"AND (cited.citation_text ILIKE :cites OR cited.normalized_citation ILIKE :cites))"
		)
	if government_outcome in {"won", "lost"}:
		params["government_outcome"] = government_outcome
		filters.append("c.metadata_json->'reader_extracted'->>'government outcome' = :government_outcome")
	if decision_outcome in {"dismissed", "allowed", "granted"}:
		params["decision_outcome"] = decision_outcome
		filters.append("c.metadata_json->'reader_extracted'->>'decision outcome' = :decision_outcome")
	if minister:
		params["minister"] = f"%{minister}%"
		filters.append(f"{minister_expression} ILIKE :minister")
	if judge:
		params["judge"] = f"%{judge}%"
		filters.append("c.metadata_json->'reader_extracted'->>'judge' ILIKE :judge")
	if court:
		if court.strip().upper() == "FC":
			# Exact match so "FC" does not also match "FCA" or "Federal Court of Appeal".
			filters.append("UPPER(c.court) IN ('FC', 'FEDERAL COURT')")
		else:
			params["court"] = f"%{court}%"
			filters.append("c.court ILIKE :court")
	if year:
		params["year"] = f"{year}%"
		filters.append("COALESCE(c.metadata_json->'reader_extracted'->>'date', '') ILIKE :year")
	where_clause = " AND ".join(filters)
	citation_count = (
		"(SELECT COUNT(*) FROM citations cited WHERE cited.source_case_id = c.id "
		"AND (cited.citation_text ILIKE :cites OR cited.normalized_citation ILIKE :cites))"
		if cites
		else "0"
	)
	citation_mentions = "(SELECT COUNT(*) FROM citations cited WHERE cited.source_case_id = c.id)"
	unique_cited_authorities = (
		"(SELECT COUNT(DISTINCT COALESCE(NULLIF(cited.normalized_citation, ''), cited.citation_text)) "
		"FROM citations cited WHERE cited.source_case_id = c.id)"
	)
	resolved_target_cases = (
		"(SELECT COUNT(DISTINCT cited.target_case_id) FROM citations cited "
		"WHERE cited.source_case_id = c.id AND cited.target_case_id IS NOT NULL)"
	)
	cited_by_cases = (
		"(SELECT COUNT(DISTINCT cited.source_case_id) FROM citations cited "
		"WHERE cited.target_case_id = c.id AND cited.source_case_id <> c.id)"
	)
	default_sort = (
		"matching_citations DESC, c.date DESC NULLS LAST, c.id DESC"
		if cites
		else "c.date DESC NULLS LAST, c.id DESC"
	)
	sort_order = {
		"newest": "c.date DESC NULLS LAST, c.id DESC",
		"oldest": "c.date ASC NULLS LAST, c.id ASC",
		"minister": f"COALESCE({minister_expression}, 'Unknown') ASC, c.date DESC NULLS LAST, c.id DESC",
	}.get(sort_by, default_sort)
	if query and sort_by == "relevance":
		sort_order_sql, ranking_params = _analytics_case_order_sql(
			query,
			sort_by,
			minister_expression=minister_expression,
			search_full_text=search_full_text,
		)
		params.update(ranking_params)
		sort_order = sort_order_sql
	statement = sql_text(
			f"""
			SELECT
				c.id, c.title, c.citation, c.court, c.date,
				c.metadata_json->'reader_extracted'->>'judge' AS judge,
				c.metadata_json->'reader_extracted'->>'decision outcome' AS decision_outcome,
				c.metadata_json->'reader_extracted'->>'government outcome' AS government_outcome,
				{minister_expression} AS minister,
				{citation_count} AS matching_citations
				,{citation_mentions} AS citation_mentions
				,{unique_cited_authorities} AS unique_cited_authorities
				,{resolved_target_cases} AS resolved_target_cases
				,{cited_by_cases} AS cited_by_cases
				,{match_label} AS matched_on
			FROM cases c
			WHERE {where_clause}
			ORDER BY {sort_order}
			LIMIT :limit OFFSET :offset
			"""
		)
	if cohort_ids is not None:
		statement = statement.bindparams(bindparam("cohort_ids", expanding=True))
	rows = db.execute(statement, params).mappings().all()
	return {
		"results": [
			{
				"case_id": int(row["id"]),
				"title": row["title"],
				"citation": row["citation"],
				"court": row["court"],
				"date": row["date"],
				"judge": row["judge"],
				"minister": row["minister"],
				"decision_outcome": row["decision_outcome"],
				"government_outcome": row["government_outcome"],
				"matching_citations": int(row["matching_citations"] or 0),
				"citation_mentions": int(row["citation_mentions"] or 0),
				"unique_cited_authorities": int(row["unique_cited_authorities"] or 0),
				"resolved_target_cases": int(row["resolved_target_cases"] or 0),
				"cited_by_cases": int(row["cited_by_cases"] or 0),
				"matched_on": row.get("matched_on", "Metadata"),
			}
			for row in rows
		],
		"limit": limit,
		"offset": offset,
	}


def fetch_analytics_search_ministers(db: Session) -> dict[str, list[str]]:
	rows = db.execute(
		sql_text(
			"""
			SELECT DISTINCT TRIM(SUBSTRING(title FROM 'Canada [(]([^)]*)[)]')) AS minister
			FROM cases
			WHERE SUBSTRING(title FROM 'Canada [(]([^)]*)[)]') IS NOT NULL
			ORDER BY minister
			"""
		)
	).scalars().all()
	return {"ministers": [str(value) for value in rows if value]}


def fetch_analytics_search_case_detail(db: Session, case_id: int) -> dict[str, Any]:
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	full_text = case.full_text or case.summary or ""
	reader_extracted = (case.metadata_json or {}).get("reader_extracted")
	metadata: dict[str, Any] = reader_extracted if isinstance(reader_extracted, dict) else {}
	citation_rows = list(
		db.scalars(
			select(Citation)
			.where(Citation.source_case_id == case.id)
			.order_by(Citation.id)
		)
	)
	chunk_ids = {citation.chunk_id for citation in citation_rows if citation.chunk_id is not None}
	chunks = (
		list(
			db.scalars(
				select(CaseChunk)
				.where(CaseChunk.id.in_(chunk_ids))
				.order_by(CaseChunk.chunk_index, CaseChunk.id)
			)
		)
		if chunk_ids
		else []
	)
	chunk_starts: dict[int, int] = {}
	search_start = 0
	for chunk in chunks:
		chunk_text = chunk.text or ""
		chunk_start = full_text.find(chunk_text, search_start)
		if chunk_start < 0:
			chunk_start = full_text.find(chunk_text)
		if chunk_start < 0:
			continue
		chunk_starts[chunk.id] = chunk_start
		search_start = max(search_start, chunk_start + len(chunk_text))
	highlights = []
	for citation in citation_rows:
		if citation.chunk_id is None:
			continue
		chunk_start = chunk_starts.get(citation.chunk_id)
		if chunk_start is None or citation.offset_start is None or citation.offset_end is None:
			continue
		start = chunk_start + citation.offset_start
		end = chunk_start + citation.offset_end
		if start < 0 or end <= start or end > len(full_text):
			continue
		highlights.append(
			{
				"text": citation.citation_text,
				"normalized": citation.normalized_citation,
				"offset_start": start,
				"offset_end": end,
				"target_case_id": citation.target_case_id,
				"target_title": citation.target_case.title if citation.target_case else None,
				"target_citation": citation.target_case.citation if citation.target_case else None,
			}
		)
	unique_cited_authorities = {
		(citation.normalized_citation or citation.citation_text or "").strip()
		for citation in citation_rows
		if (citation.normalized_citation or citation.citation_text or "").strip()
	}
	resolved_target_cases = {
		citation.target_case_id
		for citation in citation_rows
		if citation.target_case_id is not None
	}
	return {
		"case": {
			"id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
			"judge": metadata.get("judge"),
			"decision_outcome": metadata.get("decision outcome"),
			"government_outcome": metadata.get("government outcome"),
			"government_role": metadata.get("government role"),
			"full_text": full_text,
		},
		"citation_metrics": {
			"citation_mentions": len(citation_rows),
			"unique_cited_authorities": len(unique_cited_authorities),
			"resolved_target_cases": len(resolved_target_cases),
		},
		"citations": highlights,
	}


def fetch_tag_trends_by_year(db: Session) -> dict[str, Any]:
	"""Tag frequency trends by year: top tags over time."""
	query = select(
		func.extract('year', Case.date).label('year'),
		CaseTag.category,
		CaseTag.value,
		func.count(func.distinct(CaseTag.case_id)).label('case_count'),
		func.count(CaseTag.id).label('tag_mentions'),
	).join(
		Case, CaseTag.case_id == Case.id
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
	).group_by(
		'year', CaseTag.category, CaseTag.value
	).order_by(
		'year desc', 'case_count desc'
	)
	rows = db.execute(query).all()
	trends = {}
	for year, category, value, case_count, tag_mentions in rows:
		year_str = str(int(year)) if year else 'Unknown'
		if year_str not in trends:
			trends[year_str] = []
		trends[year_str].append({
			'category': category,
			'value': value,
			'case_count': case_count,
			'tag_mentions': tag_mentions,
		})
	return trends


def fetch_tag_by_judge(db: Session) -> dict[str, Any]:
	"""Judge specialization: most common tags per judge."""
	query = select(
		Case.judge,
		CaseTag.category,
		CaseTag.value,
		func.count(func.distinct(CaseTag.case_id)).label('case_count'),
	).join(
		Case, CaseTag.case_id == Case.id
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
		Case.judge.isnot(None),
	).group_by(
		Case.judge, CaseTag.category, CaseTag.value
	).having(
		func.count(func.distinct(CaseTag.case_id)) >= 2
	).order_by(
		Case.judge, 'case_count desc'
	)
	rows = db.execute(query).all()
	judge_tags = {}
	for judge, category, value, case_count in rows:
		if judge not in judge_tags:
			judge_tags[judge] = []
		judge_tags[judge].append({
			'category': category,
			'value': value,
			'case_count': case_count,
		})
	return judge_tags


def fetch_tag_frequency(db: Session) -> list[dict[str, Any]]:
	"""Overall tag frequency across corpus."""
	query = select(
		CaseTag.category,
		CaseTag.value,
		func.count(func.distinct(CaseTag.case_id)).label('case_count'),
		func.count(CaseTag.id).label('tag_mentions'),
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
	).group_by(
		CaseTag.category, CaseTag.value
	).order_by(
		'case_count desc'
	).limit(100)
	rows = db.execute(query).all()
	return [
		{
			'category': category,
			'value': value,
			'case_count': case_count,
			'tag_mentions': tag_mentions,
		}
		for category, value, case_count, tag_mentions in rows
	]


def fetch_all_tag_analytics(db: Session) -> dict[str, Any]:
	"""Aggregate all tag analytics data."""
	trends = fetch_tag_trends_by_year(db)
	judge_tags = fetch_tag_by_judge(db)
	frequency = fetch_tag_frequency(db)

	# Summary stats
	total_tags_query = select(
		func.count(func.distinct(CaseTag.category + ':' + CaseTag.value))
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
	)
	total_tags = db.execute(total_tags_query).scalar() or 0

	unique_cases_query = select(
		func.count(func.distinct(CaseTag.case_id))
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
	)
	unique_cases_tagged = db.execute(unique_cases_query).scalar() or 0

	unique_categories_query = select(
		func.count(func.distinct(CaseTag.category))
	).where(
		CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION
	)
	unique_categories = db.execute(unique_categories_query).scalar() or 0

	return {
		'trends': trends,
		'judge_tags': judge_tags,
		'frequency': frequency,
		'summary': {
			'total_tags': total_tags,
			'unique_cases_tagged': unique_cases_tagged,
			'unique_categories': unique_categories,
		}
	}


def fetch_issue_brief(db: Session, tag: str) -> dict[str, Any]:
	"""Build an issue brief from active-taxonomy tags and stored case outcomes/citations."""
	category, separator, value = tag.partition(":")
	if not separator or not category.strip() or not value.strip():
		return _empty_issue_brief(tag)

	tagged_case_ids = (
		select(CaseTag.case_id)
		.where(
			CaseTag.category == category.strip(),
			CaseTag.value == value.strip(),
			CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
		)
		.distinct()
		.subquery()
	)
	cases = db.scalars(
		select(Case)
		.where(Case.id.in_(select(tagged_case_ids.c.case_id)))
		.order_by(Case.date, Case.id)
	).all()

	year_data: dict[int | None, dict[str, Any]] = {}
	court_counts: dict[str, int] = {}
	decision_links: list[dict[str, Any]] = []
	for case in cases:
		year = case.date.year if case.date else None
		group = year_data.setdefault(year, {"decision_count": 0, "outcomes": {}})
		group["decision_count"] += 1
		metadata = case.metadata_json if isinstance(case.metadata_json, dict) else {}
		reader_metadata = metadata.get("reader_extracted")
		reader_metadata = reader_metadata if isinstance(reader_metadata, dict) else {}
		outcome = reader_metadata.get("decision outcome")
		outcome = str(outcome).strip() if outcome else "unclassified"
		if not outcome:
			outcome = "unclassified"
		group["outcomes"][outcome] = group["outcomes"].get(outcome, 0) + 1
		court = (case.court or "").strip() or "Unspecified"
		court_counts[court] = court_counts.get(court, 0) + 1
		decision_links.append(
			{
				"case_id": case.id,
				"title": case.title,
				"citation": case.citation,
				"date": case.date.isoformat() if case.date else None,
				"year": year,
				"court": court,
				"outcome": outcome,
				"url": f"/case-reader?case_id={case.id}",
			}
		)

	years: list[dict[str, Any]] = []
	for year in sorted(year_data, key=lambda item: (item is None, item or 0)):
		group = year_data[year]
		denominator = group["decision_count"]
		unclassified = group["outcomes"].get("unclassified", 0)
		outcomes = [
			{
				"outcome": outcome,
				"count": count,
				"percentage": round(count / denominator * 100, 1) if denominator else 0.0,
				"unclassified_count": unclassified,
				"denominator": denominator,
			}
			for outcome, count in sorted(group["outcomes"].items())
		]
		years.append(
			{
				"year": year,
				"decision_count": denominator,
				"unclassified_count": unclassified,
				"outcome_splits": outcomes,
			}
		)

	authority_rows = db.execute(
		select(
			Case.id,
			Case.title,
			Case.citation,
			func.count(Citation.id).label("citation_occurrences"),
			func.count(func.distinct(Citation.source_case_id)).label("citing_decisions"),
		)
		.join(Citation, Citation.target_case_id == Case.id)
		.where(
			Citation.source_case_id.in_(select(tagged_case_ids.c.case_id)),
			Citation.target_case_id.is_not(None),
		)
		.group_by(Case.id, Case.title, Case.citation)
		.order_by(func.count(Citation.id).desc(), Case.id)
		.limit(10)
	).all()
	return {
		"tag": tag,
		"decision_count": len(cases),
		"semantics": {
			"tag_matching": "Exact category:value match in the active legal-tag taxonomy; decisions are counted once.",
			"outcomes": "Decision outcome from reader_extracted metadata; missing/blank values are unclassified. Percentages use all tagged decisions in that year, including unclassified outcomes.",
			"citations": "Top authorities count stored citation occurrences with a resolved target_case_id from tagged source decisions; citing_decisions counts distinct tagged source cases. Unresolved citations and statute references are excluded.",
		},
		"years": years,
		"courts": [
			{"court": court, "decision_count": count}
			for court, count in sorted(court_counts.items(), key=lambda item: (-item[1], item[0]))
		],
		"top_authorities": [
			{
				"case_id": row.id,
				"title": row.title,
				"citation": row.citation,
				"citation_occurrences": int(row.citation_occurrences),
				"citing_decisions": int(row.citing_decisions),
				"url": f"/case-reader?case_id={row.id}",
			}
			for row in authority_rows
		],
		"decisions": decision_links,
	}


def _empty_issue_brief(tag: str) -> dict[str, Any]:
	return {
		"tag": tag,
		"decision_count": 0,
		"semantics": {
			"tag_matching": "Exact category:value match in the active legal-tag taxonomy; decisions are counted once.",
			"outcomes": "Decision outcome from reader_extracted metadata; missing/blank values are unclassified. Percentages use all tagged decisions in that year, including unclassified outcomes.",
			"citations": "Top authorities count stored citation occurrences with a resolved target_case_id from tagged source decisions; citing_decisions counts distinct tagged source cases. Unresolved citations and statute references are excluded.",
		},
		"years": [],
		"courts": [],
		"top_authorities": [],
		"decisions": [],
	}
