"""Analytics, judge profile, and Federal Court activity service for AI CaseLibrary.

Owns SQL aggregation queries for judge outcomes, yearly trends, data explorer cross-tabulations,
judge profile resolution and filtering, and Federal Court activity timelines.
"""

from __future__ import annotations

import re
from typing import Any

import httpx
from fastapi import HTTPException, status
from sqlalchemy import func, or_, select, text as sql_text
from sqlalchemy.orm import Session

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
	if query:
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
		return ranking, params
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


def fetch_judge_outcomes(
	db: Session,
	*,
	limit: int = 50,
	min_decisions: int = 0,
) -> dict[str, Any]:
	limit = max(1, min(limit, 100))
	min_decisions = max(0, min(min_decisions, 10_000))
	limit_clause = "" if min_decisions else "LIMIT :limit"
	rows = db.execute(
		sql_text(
			f"""
			SELECT
				metadata_json->'reader_extracted'->>'judge' AS judge,
				COUNT(*) AS decisions,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'government outcome' = 'won') AS government_wins,
				COUNT(*) FILTER (WHERE metadata_json->'reader_extracted'->>'government outcome' = 'lost') AS individual_wins
			FROM cases
			WHERE COALESCE(metadata_json->'reader_extracted'->>'judge', '') <> ''
			GROUP BY judge
			HAVING COUNT(*) > :min_decisions
			ORDER BY decisions DESC, judge ASC
			{limit_clause}
			"""
		),
		{"limit": limit, "min_decisions": min_decisions},
	).mappings().all()
	judges = []
	for row in rows:
		decisions = int(row["decisions"] or 0)
		government_wins = int(row["government_wins"] or 0)
		individual_wins = int(row["individual_wins"] or 0)
		judges.append(
			{
				"judge": str(row["judge"]),
				"decisions": decisions,
				"government_wins": government_wins,
				"individual_wins": individual_wins,
				"unclassified": decisions - government_wins - individual_wins,
			}
		)
	return {
		"judges": judges,
		"totals": {
			"decisions": sum(row["decisions"] for row in judges),
			"classified": sum(row["government_wins"] + row["individual_wins"] for row in judges),
		},
	}


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
		"case_tags": int(db.scalar(select(func.count(CaseTag.id))) or 0),
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
		"province_rows": province_rows,
	}


def fetch_fc_activity_analytics(
	db: Session,
	*,
	x: str = "year",
	group_by: str = "full_history_resolution",
	year_from: int | None = None,
	year_to: int | None = None,
	city: str = "",
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
	rows = db.execute(statement).all()
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
	return {
		"x": x,
		"x_label": labels[x],
		"group_by": group_by,
		"total": sum(counts.values()),
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
) -> dict[str, Any]:
	limit = max(1, min(limit, 100))
	offset = max(0, offset)
	filters = ["TRUE"]
	params: dict[str, Any] = {"limit": limit, "offset": offset}
	query = " ".join(query.split())
	cites = " ".join(cites.split())
	minister = " ".join(minister.split())
	judge = " ".join(judge.split())
	court = " ".join(court.split())
	year = "".join(character for character in year if character.isdigit())[:4]
	minister_expression = "SUBSTRING(c.title FROM 'Canada [(]([^)]*)[)]')"
	if query:
		params["query"] = f"%{query}%"
		query_fields = "c.title ILIKE :query OR c.citation ILIKE :query"
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
	rows = db.execute(
		sql_text(
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
			FROM cases c
			WHERE {where_clause}
			ORDER BY {sort_order}
			LIMIT :limit OFFSET :offset
			"""
		),
		params,
	).mappings().all()
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
