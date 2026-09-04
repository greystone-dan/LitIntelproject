"""Contextual Tag, Statute, and Citation Intelligence Service for AI CaseLibrary.

Correlates stored legal tags (ca_legal_v2 taxonomy), statutory provisions (IRPA/IRPR),
and case citations using character offset proximity, co-occurrence matrices, and
composite thematic signatures to cluster similar cases and surface legal themes.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from datetime import date
from typing import Any

from sqlalchemy import func, or_, select, text as sql_text
from sqlalchemy.orm import Session

from .database import (
	Case,
	CaseChunk,
	CaseSource,
	CaseTag,
	Citation,
	CitationMetrics,
	StatuteReference,
)
from .legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION


# --- Core Thematic Category Definitions ---

THEME_CATEGORIES: dict[str, dict[str, Any]] = {
	"security_inadmissibility": {
		"label": "Security & Terrorism Inadmissibility",
		"description": "National security, terrorism, espionage, and membership in organizations under IRPA s. 34",
		"tag_categories": ["security"],
		"statute_pinpoints": ["34", "34(1)(a)", "34(1)(b)", "34(1)(c)", "34(1)(d)", "34(1)(e)", "34(1)(f)", "34(1)(f)", "77", "77(1)", "81"],
		"landmark_citations": ["Suresh v. Canada", "Harkat", "Charkaoui", "Almrei", "2002 SCC 1", "2014 SCC 37"],
	},
	"human_rights_war_crimes": {
		"label": "Human Rights Violations & War Crimes",
		"description": "Crimes against humanity, war crimes, genocide, and complicity under IRPA s. 35",
		"tag_categories": ["human_rights"],
		"statute_pinpoints": ["35", "35(1)(a)", "35(1)(b)", "35(1)(c)", "98"],
		"landmark_citations": ["Mugesera v. Canada", "Ezokola", "2013 SCC 40", "2005 SCC 40"],
	},
	"criminal_inadmissibility": {
		"label": "Criminality & Organized Crime",
		"description": "Serious criminality, convictions, and organized criminality under IRPA ss. 36 and 37",
		"tag_categories": ["criminality"],
		"statute_pinpoints": ["36", "36(1)(a)", "36(1)(b)", "36(2)(a)", "37", "37(1)(a)", "37(1)(b)"],
		"landmark_citations": ["Tran v. Canada", "Medovarski", "2017 SCC 50", "2005 SCC 51"],
	},
	"misrepresentation_identity": {
		"label": "Misrepresentation & Identity Verification",
		"description": "False statements, undisclosed information, identity fraud, and 5-year bar under IRPA s. 40",
		"tag_categories": ["misrepresentation_identity"],
		"statute_pinpoints": ["40", "40(1)(a)", "40(1)(b)", "40(1)(c)", "40(2)(a)", "127"],
		"landmark_citations": ["Bellido v. Canada", "Jiang v. Canada", "2005 FC 452"],
	},
	"refugee_credibility_risk": {
		"label": "Refugee Protection & Credibility Assessment",
		"description": "Convention refugee and person in need of protection claims, credibility findings, and internal flight alternatives under IRPA ss. 96 & 97",
		"tag_categories": ["evidence_credibility", "risk_country_conditions"],
		"statute_pinpoints": ["96", "97", "97(1)", "97(1)(a)", "97(1)(b)", "100", "101", "107", "110", "110(4)", "111", "112", "113(a)"],
		"landmark_citations": ["Ward", "Maldonado", "Vavilov", "Pushpanathan", "1993 2 SCR 689", "2019 SCC 65"],
	},
	"humanitarian_compassionate": {
		"label": "Humanitarian & Compassionate (H&C) Applications",
		"description": "H&C relief, Best Interests of the Child (BIOC), establishment, and hardship under IRPA s. 25(1)",
		"tag_categories": ["humanitarian_family"],
		"statute_pinpoints": ["25", "25(1)", "25(1.1)", "25(1.2)", "25.1", "25.2"],
		"landmark_citations": ["Kanthasamy v. Canada", "Baker v. Canada", "2015 SCC 61", "[1999] 2 S.C.R. 817"],
	},
	"procedural_fairness_review": {
		"label": "Procedural Fairness & Standard of Review",
		"description": "Natural justice, right to be heard, bias, adequacy of reasons, and reasonableness review under IRPA s. 72(1)",
		"tag_categories": ["procedural_fairness", "constitutional_international"],
		"statute_pinpoints": ["72", "72(1)", "74", "74(d)", "18.1"],
		"landmark_citations": ["Vavilov", "Dunsmuir", "Baker", "2019 SCC 65", "2008 SCC 9"],
	},
	"detention_enforcement": {
		"label": "Detention Reviews & Enforcement",
		"description": "Immigration detention, flight risk, danger to the public, release conditions, and removal enforcement under IRPA ss. 48-58",
		"tag_categories": ["detention", "removal_enforcement"],
		"statute_pinpoints": ["48", "49", "55", "55(1)", "55(2)", "56", "57", "57(1)", "57(2)", "58", "58(1)"],
		"landmark_citations": ["Charkaoui v. Canada", "Sahin v. Canada", "2007 SCC 9"],
	},
}


# --- Data Structures ---


@dataclass
class ProximityCluster:
	"""Represents a co-occurring cluster of tags, statutes, and citations within a text window."""
	case_id: int
	chunk_id: int | None
	window_start: int
	window_end: int
	tags: list[dict[str, Any]]
	statutes: list[dict[str, Any]]
	citations: list[dict[str, Any]]
	thematic_label: str


@dataclass
class CaseThematicSignature:
	"""Deterministic composite legal signature for a case."""
	case_id: int
	title: str
	citation: str | None
	court: str | None
	date: str | None
	primary_theme: str
	theme_scores: dict[str, float]
	top_statutes: list[str]
	top_tags: list[str]
	top_citations: list[str]
	government_outcome: str | None = None
	decision_outcome: str | None = None


# --- Service Functions ---


def fetch_theme_catalog() -> list[dict[str, Any]]:
	"""Return the structured legal theme definitions with associated categories and key statutes."""
	catalog = []
	for key, theme in THEME_CATEGORIES.items():
		catalog.append(
			{
				"theme_key": key,
				"label": theme["label"],
				"description": theme["description"],
				"tag_categories": theme["tag_categories"],
				"statute_pinpoints": theme["statute_pinpoints"],
				"landmark_authorities": theme["landmark_citations"],
			}
		)
	return catalog


def fetch_theme_breakdown(db: Session) -> dict[str, Any]:
	"""Aggregate corpus-wide case distribution across defined legal themes."""
	total_cases = int(db.scalar(select(func.count(Case.id))) or 0)

	# Aggregate tag categories
	tag_cat_rows = db.execute(
		sql_text(
			"""
			SELECT category, COUNT(*) as tag_count, COUNT(DISTINCT case_id) as case_count
			FROM case_tags
			GROUP BY category
			ORDER BY tag_count DESC
			"""
		)
	).mappings().all()

	tag_categories = [
		{
			"category": str(r["category"]),
			"tag_count": int(r["tag_count"]),
			"case_count": int(r["case_count"]),
			"case_pct": round(int(r["case_count"]) / total_cases * 100, 2) if total_cases else 0.0,
		}
		for r in tag_cat_rows
	]

	# Aggregate top statutory provisions
	statute_rows = db.execute(
		sql_text(
			"""
			SELECT pinpoint, COUNT(*) as ref_count, COUNT(DISTINCT source_case_id) as case_count
			FROM statute_references
			WHERE pinpoint IS NOT NULL AND pinpoint <> ''
			GROUP BY pinpoint
			ORDER BY ref_count DESC
			LIMIT 30
			"""
		)
	).mappings().all()

	top_statutes = [
		{
			"pinpoint": str(r["pinpoint"]),
			"reference_count": int(r["ref_count"]),
			"case_count": int(r["case_count"]),
		}
		for r in statute_rows
	]

	return {
		"total_cases": total_cases,
		"themes": fetch_theme_catalog(),
		"tag_categories": tag_categories,
		"top_statutory_pinpoints": top_statutes,
	}


def fetch_statute_tag_affinity(
	db: Session,
	pinpoint: str,
	*,
	limit_tags: int = 20,
	limit_citations: int = 15,
) -> dict[str, Any]:
	"""Compute tag affinities and co-cited authorities for cases citing a specific statutory provision."""
	norm_pinpoint = pinpoint.strip()
	if not norm_pinpoint:
		raise ValueError("pinpoint parameter is required")

	# Find all cases citing this statutory pinpoint
	case_ids = list(
		db.scalars(
			select(StatuteReference.source_case_id)
			.where(StatuteReference.pinpoint == norm_pinpoint)
			.distinct()
		)
	)
	total_citing_cases = len(case_ids)

	if not case_ids:
		return {
			"pinpoint": norm_pinpoint,
			"citing_cases_count": 0,
			"top_tag_categories": [],
			"top_tag_values": [],
			"top_cited_authorities": [],
			"outcome_summary": {"won": 0, "lost": 0, "unclassified": 0, "relief_rate": None},
		}

	# 1. Enriched Tag Categories
	tag_cat_rows = db.execute(
		sql_text(
			"""
			SELECT category, COUNT(*) as occurrences, COUNT(DISTINCT case_id) as case_count
			FROM case_tags
			WHERE case_id IN :case_ids
			  AND taxonomy_version = :taxonomy_version
			GROUP BY category
			ORDER BY case_count DESC, occurrences DESC
			LIMIT 15
			"""
		),
		{"case_ids": tuple(case_ids), "taxonomy_version": ACTIVE_TAG_TAXONOMY_VERSION},
	).mappings().all()

	tag_categories = [
		{
			"category": str(r["category"]),
			"occurrences": int(r["occurrences"]),
			"case_count": int(r["case_count"]),
			"case_prevalence_pct": round(int(r["case_count"]) / total_citing_cases * 100, 1),
		}
		for r in tag_cat_rows
	]

	# 2. Top Tag Values (Specific legal issues)
	tag_val_rows = db.execute(
		sql_text(
			"""
			SELECT category, value, COUNT(*) as occurrences, COUNT(DISTINCT case_id) as case_count
			FROM case_tags
			WHERE case_id IN :case_ids
			  AND taxonomy_version = :taxonomy_version
			GROUP BY category, value
			ORDER BY case_count DESC, occurrences DESC
			LIMIT :limit_tags
			"""
		),
		{
			"case_ids": tuple(case_ids),
			"limit_tags": limit_tags,
			"taxonomy_version": ACTIVE_TAG_TAXONOMY_VERSION,
		},
	).mappings().all()

	tag_values = [
		{
			"category": str(r["category"]),
			"value": str(r["value"]),
			"occurrences": int(r["occurrences"]),
			"case_count": int(r["case_count"]),
			"case_prevalence_pct": round(int(r["case_count"]) / total_citing_cases * 100, 1),
		}
		for r in tag_val_rows
	]

	# 3. Top Co-Cited Authorities for this statute
	cit_rows = db.execute(
		sql_text(
			"""
			SELECT
				COALESCE(target.title, c.normalized_citation, c.citation_text) AS authority_title,
				COALESCE(target.citation, c.normalized_citation) AS authority_citation,
				c.target_case_id,
				COUNT(*) AS mention_count,
				COUNT(DISTINCT c.source_case_id) AS case_count
			FROM citations c
			LEFT JOIN cases target ON target.id = c.target_case_id
			WHERE c.source_case_id IN :case_ids
			  AND COALESCE(c.normalized_citation, c.citation_text, '') <> ''
			GROUP BY authority_title, authority_citation, c.target_case_id
			ORDER BY case_count DESC, mention_count DESC
			LIMIT :limit_citations
			"""
		),
		{"case_ids": tuple(case_ids), "limit_citations": limit_citations},
	).mappings().all()

	cited_authorities = [
		{
			"title": str(r["authority_title"]),
			"citation": str(r["authority_citation"] or ""),
			"target_case_id": r["target_case_id"],
			"mention_count": int(r["mention_count"]),
			"case_count": int(r["case_count"]),
			"co_citation_pct": round(int(r["case_count"]) / total_citing_cases * 100, 1),
		}
		for r in cit_rows
	]

	# 4. Outcome distribution for cases citing this statute
	outcome_rows = db.execute(
		sql_text(
			"""
			SELECT
				metadata_json->'reader_extracted'->>'government outcome' AS gov_outcome,
				metadata_json->'reader_extracted'->>'decision outcome' AS dec_outcome,
				COUNT(*) AS count
			FROM cases
			WHERE id IN :case_ids
			GROUP BY gov_outcome, dec_outcome
			"""
		),
		{"case_ids": tuple(case_ids)},
	).mappings().all()

	gov_wins = sum(int(r["count"]) for r in outcome_rows if r["gov_outcome"] == "won")
	gov_losses = sum(int(r["count"]) for r in outcome_rows if r["gov_outcome"] == "lost")
	classified = gov_wins + gov_losses
	relief_rate = round(gov_losses / classified * 100, 1) if classified else None

	return {
		"pinpoint": norm_pinpoint,
		"citing_cases_count": total_citing_cases,
		"top_tag_categories": tag_categories,
		"top_tag_values": tag_values,
		"top_cited_authorities": cited_authorities,
		"outcomes": {
			"government_wins": gov_wins,
			"individual_relief_wins": gov_losses,
			"classified_cases": classified,
			"applicant_relief_rate_pct": relief_rate,
		},
	}


def fetch_case_contextual_anchors(
	db: Session,
	case_id: int,
	*,
	proximity_window: int = 250,
) -> list[dict[str, Any]]:
	"""Extract character-offset proximity anchors where tags, statutes, and citations co-occur in a case."""
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise ValueError(f"Case {case_id} not found")

	full_text = case.full_text or case.summary or ""

	# Load tags with offsets
	tags = list(
		db.scalars(
			select(CaseTag)
			.where(
				CaseTag.case_id == case_id,
				CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
				CaseTag.offset_start.is_not(None),
				CaseTag.offset_end.is_not(None),
			)
			.order_by(CaseTag.offset_start)
		)
	)

	# Load statutes with offsets
	statutes = list(
		db.scalars(
			select(StatuteReference)
			.where(
				StatuteReference.source_case_id == case_id,
				StatuteReference.offset_start.is_not(None),
				StatuteReference.offset_end.is_not(None),
			)
			.order_by(StatuteReference.offset_start)
		)
	)

	# Load citations with offsets
	citations = list(
		db.scalars(
			select(Citation)
			.where(
				Citation.source_case_id == case_id,
				Citation.offset_start.is_not(None),
				Citation.offset_end.is_not(None),
			)
			.order_by(Citation.offset_start)
		)
	)

	anchors: list[dict[str, Any]] = []

	# Iterate over each statute reference and find tags/citations within proximity_window
	for statute in statutes:
		stat_start = statute.offset_start or 0
		stat_end = statute.offset_end or stat_start
		win_start = max(0, stat_start - proximity_window)
		win_end = min(len(full_text), stat_end + proximity_window)

		nearby_tags = [
			{
				"category": t.category,
				"value": t.value,
				"offset_start": t.offset_start,
				"offset_end": t.offset_end,
			}
			for t in tags
			if t.offset_start is not None and t.offset_end is not None
			and not (t.offset_end < win_start or t.offset_start > win_end)
		]

		nearby_cites = [
			{
				"citation_text": c.citation_text,
				"normalized_citation": c.normalized_citation,
				"target_case_id": c.target_case_id,
				"offset_start": c.offset_start,
				"offset_end": c.offset_end,
			}
			for c in citations
			if c.offset_start is not None and c.offset_end is not None
			and not (c.offset_end < win_start or c.offset_start > win_end)
		]

		if nearby_tags or nearby_cites:
			# Determine snippet
			snippet = full_text[win_start:win_end].replace("\n", " ").strip()
			anchors.append(
				{
					"statute": {
						"normalized_reference": statute.normalized_reference,
						"pinpoint": statute.pinpoint,
						"offset_start": stat_start,
						"offset_end": stat_end,
					},
					"window_start": win_start,
					"window_end": win_end,
					"snippet": snippet,
					"co_occurring_tags": nearby_tags,
					"co_occurring_citations": nearby_cites,
				}
			)

	return anchors


def compute_case_thematic_signature(db: Session, case_id: int) -> CaseThematicSignature:
	"""Compute deterministic thematic signature combining tag counts, statutes, and citations."""
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise ValueError(f"Case {case_id} not found")

	tags = list(
		db.scalars(
			select(CaseTag).where(
				CaseTag.case_id == case_id,
				CaseTag.taxonomy_version == ACTIVE_TAG_TAXONOMY_VERSION,
			)
		)
	)
	statutes = list(
		db.scalars(select(StatuteReference).where(StatuteReference.source_case_id == case_id))
	)
	citations = list(
		db.scalars(select(Citation).where(Citation.source_case_id == case_id))
	)

	metadata = case.metadata_json or {}
	reader_extracted = metadata.get("reader_extracted", {}) if isinstance(metadata, dict) else {}

	# Count tag categories and values
	tag_categories = {t.category for t in tags}
	tag_values = {f"{t.category}:{t.value}" for t in tags}

	# Extract statutory pinpoints
	statute_pinpoints = {s.pinpoint for s in statutes if s.pinpoint}

	# Extract cited authorities
	cited_names = {
		(c.normalized_citation or c.citation_text or "").strip()
		for c in citations
		if (c.normalized_citation or c.citation_text)
	}

	# Compute score across defined legal themes
	theme_scores: dict[str, float] = {}
	for theme_key, theme_def in THEME_CATEGORIES.items():
		score = 0.0

		# Tag match score
		matched_tags = sum(1 for cat in theme_def["tag_categories"] if cat in tag_categories)
		score += matched_tags * 2.0

		# Statute pinpoint match score
		matched_statutes = sum(
			1 for pp in theme_def["statute_pinpoints"] if pp in statute_pinpoints
		)
		score += matched_statutes * 3.5

		# Landmark authority match score
		matched_cites = sum(
			1 for lm in theme_def["landmark_citations"]
			if any(lm.lower() in cite.lower() for cite in cited_names)
		)
		score += matched_cites * 2.5

		if score > 0:
			theme_scores[theme_key] = round(score, 2)

	# Identify dominant theme
	if theme_scores:
		primary_theme = max(theme_scores.items(), key=lambda item: item[1])[0]
	else:
		primary_theme = "general_immigration"

	top_stats = sorted(list(statute_pinpoints))[:10]
	top_t = sorted(list(tag_values))[:15]
	top_c = sorted(list(cited_names))[:10]

	return CaseThematicSignature(
		case_id=case.id,
		title=case.title or "Untitled",
		citation=case.citation,
		court=case.court,
		date=case.date.isoformat() if case.date else None,
		primary_theme=primary_theme,
		theme_scores=theme_scores,
		top_statutes=top_stats,
		top_tags=top_t,
		top_citations=top_c,
		government_outcome=reader_extracted.get("government outcome"),
		decision_outcome=reader_extracted.get("decision outcome"),
	)


def find_thematically_similar_cases(
	db: Session,
	case_id: int,
	*,
	limit: int = 10,
) -> dict[str, Any]:
	"""Find cases with the highest composite thematic similarity (statute + tag + citation overlap)."""
	source_sig = compute_case_thematic_signature(db, case_id)

	# Query candidate cases sharing at least one top statute or top tag
	source_statutes = source_sig.top_statutes
	source_tags = [t.split(":")[-1] for t in source_sig.top_tags if ":" in t]

	if not source_statutes and not source_tags:
		return {
			"source_case": source_sig.__dict__,
			"matched_cluster_count": 0,
			"similar_cases": [],
		}

	candidate_ids_stmt = (
		select(Case.id)
		.where(
			Case.id != case_id,
			or_(
				Case.id.in_(
					select(StatuteReference.source_case_id).where(
						StatuteReference.pinpoint.in_(source_statutes)
					)
				)
				if source_statutes
				else sql_text("FALSE"),
				Case.id.in_(
					select(CaseTag.case_id).where(
						CaseTag.value.in_(source_tags)
					)
				)
				if source_tags
				else sql_text("FALSE"),
			),
		)
		.limit(100)
	)

	candidate_ids = list(db.scalars(candidate_ids_stmt))

	scored_candidates = []
	for cid in candidate_ids:
		cand_sig = compute_case_thematic_signature(db, cid)

		# 1. Jaccard similarity on statutes
		s_set1, s_set2 = set(source_sig.top_statutes), set(cand_sig.top_statutes)
		s_sim = len(s_set1 & s_set2) / len(s_set1 | s_set2) if (s_set1 | s_set2) else 0.0

		# 2. Jaccard similarity on tags
		t_set1, t_set2 = set(source_sig.top_tags), set(cand_sig.top_tags)
		t_sim = len(t_set1 & t_set2) / len(t_set1 | t_set2) if (t_set1 | t_set2) else 0.0

		# 3. Jaccard similarity on citations
		c_set1, c_set2 = set(source_sig.top_citations), set(cand_sig.top_citations)
		c_sim = len(c_set1 & c_set2) / len(c_set1 | c_set2) if (c_set1 | c_set2) else 0.0

		# 4. Theme alignment bonus
		theme_bonus = 0.15 if source_sig.primary_theme == cand_sig.primary_theme else 0.0

		composite_similarity = round(
			(0.40 * s_sim) + (0.35 * t_sim) + (0.15 * c_sim) + theme_bonus, 4
		)

		if composite_similarity > 0.05:
			scored_candidates.append(
				{
					"case_id": cand_sig.case_id,
					"title": cand_sig.title,
					"citation": cand_sig.citation,
					"court": cand_sig.court,
					"date": cand_sig.date,
					"primary_theme": cand_sig.primary_theme,
					"composite_similarity": composite_similarity,
					"shared_statutes": sorted(list(s_set1 & s_set2)),
					"shared_tags": sorted(list(t_set1 & t_set2)),
					"shared_citations": sorted(list(c_set1 & c_set2)),
					"government_outcome": cand_sig.government_outcome,
					"decision_outcome": cand_sig.decision_outcome,
				}
			)

	scored_candidates.sort(key=lambda item: item["composite_similarity"], reverse=True)
	top_matches = scored_candidates[:limit]

	return {
		"source_case": source_sig.__dict__,
		"matched_cluster_count": len(scored_candidates),
		"similar_cases": top_matches,
	}
