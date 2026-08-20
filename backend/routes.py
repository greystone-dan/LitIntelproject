import os
import math
import csv
import io
import re
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from openai import OpenAI, OpenAIError
from sqlalchemy import Text, func, or_, select, text as sql_text
from sqlalchemy.sql import Select
from sqlalchemy.orm import Session

try:
	import yaml
except Exception:  # pragma: no cover
	yaml = None

from .citation_map import (
	case_authority_map as _case_authority_map,
	citation_authority_signals as _citation_authority_signals,
	citation_completion_suggestions as _citation_completion_suggestions,
	citation_doctrine_shifts as _citation_doctrine_shifts,
	citation_edge_summary as _citation_edge_summary,
	citation_cross_court_flow as _citation_cross_court_flow,
	citation_hidden_bridges as _citation_hidden_bridges,
	citation_authority_lifecycle as _citation_authority_lifecycle,
	citation_inheritance_chains as _citation_inheritance_chains,
	citation_missing_authorities as _citation_missing_authorities,
	citation_position_profiles as _citation_position_profiles,
	citation_shift_dashboard as _citation_shift_dashboard,
	citation_contextual_paths as _citation_contextual_paths,
	case_legal_tags as _case_legal_tags,
	citation_contexts as _citation_contexts,
	citation_issue_map as _citation_issue_map,
	citation_landmark_candidates as _citation_landmark_candidates,
	citation_paths as _citation_paths,
	citation_map_summary as _citation_map_summary,
	citation_map_topics as _citation_map_topics,
	citation_intelligence_overview as _ci_overview,
	citation_intelligence_timeline as _ci_timeline,
	citation_intelligence_outcomes as _ci_outcomes,
	citation_intelligence_courts as _ci_courts,
	citation_intelligence_judges as _ci_judges,
	citation_intelligence_statutes as _ci_statutes,
	citation_intelligence_table as _ci_table,
	citation_neighborhood as _citation_neighborhood,
	citation_replacement_trend as _citation_replacement_trend,
	citation_surprise_feed as _citation_surprise_feed,
	common_citing_cases as _common_citing_cases,
	co_cited_authorities as _co_cited_authorities,
	search_citation_cases as _search_citation_cases,
	similar_cases_by_authority as _similar_cases_by_authority,
	top_authorities as _top_authorities,
)
from .citation_map_workbench_v2 import citation_map_html
from .case_reader import case_reader_html
from .citations import build_a2aj_case_map as _build_a2aj_case_map
from .citations import compute_citation_metrics as _compute_citation_metrics
from .citations import convert_a2aj_edges_to_local as _convert_a2aj_edges_to_local
from .citations import extract_case_citation_matches
from .citations import extract_statute_reference_matches
from .citations import extract_raw_citation_matches
from .citations import is_self_case_name_match
from .citations import RawCitationMatch
from .metadata import extract_metadata_observations
from .database import (
	Case,
	CaseChunk,
	CaseChunkEmbedding,
	CaseSource,
	CaseTag,
	JudgeProfile,
	CaseJudgeProfile,
	Citation,
	CitationMetrics,
	FCProceduralHistory,
	FCActivityCase,
	FCActivityDocument,
	IngestionRun,
	StatuteReference,
	get_db,
)
from .embedding_providers import SentenceTransformerEmbeddingProvider
from .database import A2AJCase, A2AJCaseMap, A2AJCitationEdge
from .ingestion import merge_case_record
from scripts.fetch_fc_procedural_history import HEADERS, process_imm, upsert_result
from .models import (
	CaseIngestRequest,
	CaseMergeResponse,
	CaseReaderChunkResponse,
	CaseReaderCitationResponse,
	CaseReaderDataResponse,
	CaseReaderMetadataFieldResponse,
	CaseReaderTagResponse,
	CaseResponse,
	CaseSearchRequest,
	CaseSearchResponse,
	CaseSourceResponse,
	InventoryResponse,
	InventorySourceSummary,
	InventoryCaseResponse,
	LocalChunkSearchRequest,
	A2AJCaseMapResponse,
	A2AJCaseResponse,
	A2AJCitationEdgeResponse,
	CitationMapAuthorityResponse,
	CitationMapAuthoritySignalResponse,
	CitationMapAuthorityLifecycleResponse,
	CitationMapCaseNode,
	CitationMapCompletionSuggestionResponse,
	CitationMapCoCitationResponse,
	CitationMapCommonCiterResponse,
	CitationMapContextualPathResponse,
	CitationMapContextResponse,
	CitationMapCourtFlowResponse,
	CitationMapEdgeSummaryResponse,
	CitationMapHiddenBridgeResponse,
	CitationMapInheritanceChainResponse,
	CitationMapLandmarkCandidateResponse,
	CitationMapLegalTagResponse,
	CitationMapMissingAuthorityResponse,
	CitationMapPathResponse,
	CitationMapPositionProfileResponse,
	CitationMapReplacementResponse,
	CitationMapShiftDashboardResponse,
	CitationMapSurpriseResponse,
	CitationMapTopicResponse,
	CitationIssueMapResponse,
	CitationMapNeighborhoodResponse,
	CitationMapSimilarCaseResponse,
	CitationMapSummaryResponse,
	CitationMetricsResponse,
	CitationResponse,
	ChunkGroupSearchRequest,
	ChunkPassage,
	ChunkSearchResponse,
	GroupedChunkCaseResponse,
	GroupedChunkSearchResponse,
	ResearchRequest,
	ResearchResponse,
	ResearchSource,
)

router = APIRouter(tags=["cases"])
EMBEDDING_DIMENSIONS = 1536
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
PROTOTYPE_SET_NAME = "immigration_334_v1"

_STATUTE_LIKE_RE = re.compile(r"\b(IRPA|IRPR|Charter|Act|Code|Regulations?|Convention|art\.)\b", re.IGNORECASE)


def _is_statute_like_label(value: str | None) -> bool:
	text = (value or "").strip()
	return bool(_STATUTE_LIKE_RE.search(text))
PROTOTYPE_IDS_CSV = Path(__file__).resolve().parent.parent / "data" / "eval" / "prototype_case_ids_v1.csv"
PROTOTYPE_EDGES_CSV = Path(__file__).resolve().parent.parent / "data" / "eval" / "reports" / "prototype_v1_citation_edges.csv"
FC_PRIORITY_CASE_MAP_CSV = Path(__file__).resolve().parent.parent / "data" / "eval" / "fc_priority_seed_case_map.csv"
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


def _is_irpa_irpr_reference(value: str | None) -> bool:
	return bool(
		re.search(
			r"\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b",
			value or "",
			re.IGNORECASE,
		)
	)


@lru_cache(maxsize=4)
def _load_review_case_ids(csv_path: str) -> list[int]:
	path = Path(csv_path)
	if not path.exists():
		return []
	case_ids: list[int] = []
	seen_ids: set[int] = set()
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		reader = csv.DictReader(handle)
		for row in reader:
			if str(row.get("status") or "") != "matched":
				continue
			raw = str(row.get("local_case_id") or "").strip()
			if raw.isdigit():
				case_id = int(raw)
				if case_id in seen_ids:
					continue
				seen_ids.add(case_id)
				case_ids.append(case_id)
	return case_ids


def _review_fc_priority_cases(db: Session, limit: int) -> list[dict[str, Any]]:
	case_ids = _load_review_case_ids(str(FC_PRIORITY_CASE_MAP_CSV))
	if not case_ids:
		return []
	rows = list(db.scalars(select(Case).where(Case.id.in_(case_ids))))
	rows_by_id = {row.id: row for row in rows}
	ordered_rows = [rows_by_id[case_id] for case_id in case_ids if case_id in rows_by_id]
	if limit > 0:
		ordered_rows = ordered_rows[:limit]
	metrics_by_case = {
		row.case_id: row
		for row in db.scalars(select(CitationMetrics).where(CitationMetrics.case_id.in_([case.id for case in ordered_rows])))
	}
	return [
		{
			"case_id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
			"in_degree": int(getattr(metrics_by_case.get(case.id), "in_degree", 0) or 0),
			"out_degree": int(getattr(metrics_by_case.get(case.id), "out_degree", 0) or 0),
			"pagerank": getattr(metrics_by_case.get(case.id), "pagerank", None),
		}
		for case in ordered_rows
	]


def _env_bool(name: str) -> bool | None:
	value = os.getenv(name)
	if value is None:
		return None
	return value.strip().lower() in {"1", "true", "yes", "on"}


def _load_ai_rollout_flags() -> dict[str, bool]:
	flags = {
		"semantic_enabled": True,
		"hybrid_enabled": True,
		"local_semantic_enabled": True,
		"embed_on_ingest_enabled": True,
	}

	config_path = Path(__file__).resolve().parent.parent / "config.yaml"
	if yaml is not None and config_path.exists():
		try:
			payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
			rollout = ((payload.get("ai") or {}).get("rollout") or {})
			for key in flags:
				if key in rollout:
					flags[key] = bool(rollout.get(key))
		except Exception:
			pass

	overrides = {
		"semantic_enabled": _env_bool("CASELIBRARY_SEMANTIC_ENABLED"),
		"hybrid_enabled": _env_bool("CASELIBRARY_HYBRID_ENABLED"),
		"local_semantic_enabled": _env_bool("CASELIBRARY_LOCAL_SEMANTIC_ENABLED"),
		"embed_on_ingest_enabled": _env_bool("CASELIBRARY_EMBED_ON_INGEST_ENABLED"),
	}
	for key, value in overrides.items():
		if value is not None:
			flags[key] = value
	return flags


AI_ROLLOUT = _load_ai_rollout_flags()


def _effective_search_mode(requested_mode: str) -> str:
	if requested_mode == "semantic" and not AI_ROLLOUT["semantic_enabled"]:
		return "metadata"
	if requested_mode == "hybrid" and (
		not AI_ROLLOUT["hybrid_enabled"] or not AI_ROLLOUT["semantic_enabled"]
	):
		return "metadata"
	return requested_mode

PROTOTYPE_TOPIC_PATTERNS: dict[str, tuple[str, ...]] = {
	"refugee_protection": (
		r"\brefugee\b",
		r"\basylum\b",
		r"\bconvention refugee\b",
		r"\bprotected person\b",
		r"\bnon[- ]?refoulement\b",
		r"\bRPD\b",
		r"\bRAD\b",
	),
	"removal_detention": (
		r"\bremoval order\b",
		r"\bstay of removal\b",
		r"\bdeport\w*\b",
		r"\bdetention\b",
		r"\bPRRA\b",
		r"\bpre[- ]?removal risk assessment\b",
	),
	"inadmissibility_security": (
		r"\binadmissib\w*\b",
		r"\bsecurity\b",
		r"\bserious criminality\b",
		r"\bmisrepresentation\b",
		r"\borganized criminality\b",
		r"\bIRPA s\.?\s*34\b",
	),
	"family_hc": (
		r"\bfamily class\b",
		r"\bsponsorship\b",
		r"\bspouse\b",
		r"\bcommon[- ]law\b",
		r"\bhumanitarian and compassionate\b",
		r"\bH&?C\b",
		r"\bbest interests of the child\b",
	),
	"citizenship_status": (
		r"\bcitizenship\b",
		r"\bpermanent resident\b",
		r"\bresidency obligation\b",
		r"\bcertificate of citizenship\b",
	),
	"judicial_review_procedure": (
		r"\bjudicial review\b",
		r"\bprocedural fairness\b",
		r"\bnatural justice\b",
		r"\breasonableness\b",
		r"\bcorrectness\b",
		r"\bVavilov\b",
	),
}

try:
	from eyecite import get_citations
except Exception:  # pragma: no cover
	get_citations = None


def _testing_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>AI CaseLibrary API Tester</title>
	<style>
		:root {
			--bg: #f5f3ef;
			--panel: #fffdf9;
			--ink: #1f1d1a;
			--muted: #5d5952;
			--accent: #0f6e6a;
			--accent-2: #d7682f;
			--border: #d9d2c7;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			background:
				radial-gradient(circle at 15% 10%, #ece3d7 0, transparent 32%),
				radial-gradient(circle at 85% 90%, #d6ebe8 0, transparent 35%),
				var(--bg);
			color: var(--ink);
			min-height: 100vh;
		}
		.wrap {
			max-width: 1100px;
			margin: 0 auto;
			padding: 24px;
		}
		h1 {
			margin: 0 0 12px;
			font-size: clamp(1.5rem, 2.5vw, 2.2rem);
			letter-spacing: 0.01em;
		}
		p.lead {
			margin: 0 0 20px;
			color: var(--muted);
		}
		.grid {
			display: grid;
			gap: 16px;
			grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		}
		.search-card {
			grid-column: 1 / -1;
		}
		.search-layout {
			display: grid;
			gap: 14px;
			grid-template-columns: minmax(0, 1.45fr) minmax(300px, 0.85fr);
			align-items: start;
		}
		.search-panel,
		.preview-panel {
			border: 1px solid var(--border);
			border-radius: 14px;
			background: #fffefb;
			padding: 12px;
		}
		.section-head {
			display: flex;
			justify-content: space-between;
			gap: 10px;
			align-items: center;
			margin-bottom: 10px;
		}
		.section-head h2 {
			margin: 0;
		}
		.section-subtitle {
			margin: 0;
			color: var(--muted);
			font-size: 0.84rem;
		}
		.filter-group {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 10px 10px 2px;
			margin-top: 12px;
			background: rgba(255, 255, 255, 0.72);
		}
		.filter-group summary {
			cursor: pointer;
			font-size: 0.9rem;
			font-weight: 600;
			color: var(--ink);
			margin-bottom: 8px;
		}
		.filter-group summary::marker {
			color: var(--accent);
		}
		.filter-grid {
			display: grid;
			gap: 8px;
		}
		.filter-actions {
			display: flex;
			flex-wrap: wrap;
			gap: 8px;
			margin-top: 12px;
		}
		.filter-actions button {
			width: auto;
			margin-top: 0;
			min-width: 144px;
		}
		.preview-panel textarea {
			min-height: 540px;
		}
		.helper-text {
			margin-top: 8px;
			font-size: 0.82rem;
			color: var(--muted);
			line-height: 1.45;
		}
		@media (max-width: 900px) {
			.search-layout {
				grid-template-columns: 1fr;
			}
			.preview-panel textarea {
				min-height: 260px;
			}
		}
		.card {
			background: var(--panel);
			border: 1px solid var(--border);
			border-radius: 14px;
			padding: 14px;
			box-shadow: 0 6px 20px rgba(35, 24, 13, 0.06);
		}
		h2 {
			margin: 0 0 8px;
			font-size: 1rem;
		}
		label {
			display: block;
			margin: 8px 0 4px;
			font-size: 0.86rem;
			color: var(--muted);
		}
		.controls {
			display: grid;
			grid-template-columns: 1fr 1fr;
			gap: 8px;
			align-items: end;
			margin-top: 8px;
		}
		.toggle {
			display: flex;
			align-items: center;
			gap: 8px;
			font-size: 0.86rem;
			color: var(--muted);
		}
		.toggle input {
			width: auto;
		}
		input, textarea, button {
			width: 100%;
			border-radius: 10px;
			border: 1px solid var(--border);
			padding: 9px 10px;
			font: inherit;
		}
		textarea {
			min-height: 130px;
			resize: vertical;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.86rem;
		}
		button {
			margin-top: 10px;
			background: linear-gradient(135deg, var(--accent), #0b5753);
			color: white;
			border: none;
			font-weight: 600;
			cursor: pointer;
			transition: transform 0.12s ease;
		}
		button:hover {
			transform: translateY(-1px);
		}
		.secondary {
			background: linear-gradient(135deg, var(--accent-2), #b95626);
		}
		.result {
			margin-top: 10px;
			background: #fffdf9;
			color: var(--ink);
			border-radius: 10px;
			padding: 10px;
			min-height: 120px;
			white-space: normal;
			overflow-x: auto;
			font-family: inherit;
			font-size: 0.9rem;
			line-height: 1.45;
			border: 1px solid var(--border);
		}
		.result pre {
			margin: 0;
			white-space: pre-wrap;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.82rem;
			line-height: 1.45;
			color: var(--ink);
		}
		.result .case-card {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 10px 12px;
			margin-bottom: 10px;
			background: #ffffff;
		}
		.result .case-card.compact {
			padding: 8px 12px;
		}
		.result .hit-title {
			display: block;
			font-weight: 700;
			color: #0b5753;
			text-decoration: none;
			margin-bottom: 2px;
		}
		.result .hit-title:hover {
			text-decoration: underline;
		}
		.result .hit-meta {
			font-size: 0.78rem;
			color: var(--muted);
			margin-bottom: 4px;
		}
		.result .case-summary {
			margin-top: 6px;
			color: var(--muted);
			font-size: 0.84rem;
			line-height: 1.4;
		}
		.result .case-detail {
			display: none;
			margin-top: 8px;
			padding-top: 8px;
			border-top: 1px solid var(--border);
		}
		.result .case-detail.open {
			display: block;
		}
		.result .case-text {
			margin-top: 10px;
			white-space: pre-wrap;
			font-family: Consolas, "Courier New", monospace;
			font-size: 0.85rem;
			line-height: 1.5;
		}
		.pill {
			display: inline-block;
			padding: 2px 8px;
			border-radius: 999px;
			border: 1px solid var(--border);
			font-size: 0.78rem;
			color: var(--muted);
			margin-right: 6px;
		}
	</style>
</head>
<body>
	<div class="wrap">
		<h1>AI CaseLibrary API Tester</h1>
		<p class="lead">Manual testing interface for ingest and retrieval endpoints. Edit payloads, send requests, and inspect live JSON responses.</p>
		<div class="pill">Base URL: current host</div>
		<div class="pill">No auth required</div>
		<div class="grid">
			<section class="card">
				<h2>POST /ingest</h2>
				<label for="ingest">JSON payload</label>
				<textarea id="ingest">{
	"title": "Example v. Jones",
	"court": "Federal Court",
	"jurisdiction": "Canada",
	"date": "2026-07-31",
	"citation": "2026 FC 100",
	"summary": "The applicant challenges a removal order based on risk evidence.",
	"source_type": "manual_test"
}</textarea>
				<button onclick="sendJson('POST', '/ingest', 'ingest', 'ingestResult')">Run ingest</button>
				<div id="ingestResult" class="result"></div>
			</section>

			<section class="card search-card">
				<div class="section-head">
					<div>
						<h2>POST /search</h2>
						<p class="section-subtitle">Search A2AJ by query, citation, court, source metadata, scrape date, and relationship filters.</p>
					</div>
					<div class="pill">Metadata-first search</div>
				</div>
				<div class="search-layout">
					<div class="search-panel">
						<div class="controls" style="grid-template-columns: 1.2fr 1fr 1fr;">
							<div>
								<label for="searchQuery">Document text query</label>
								<input id="searchQuery" type="text" placeholder="non-refoulement risk review" />
							</div>
							<div>
								<label for="metaTitle">Case name / title (identifier)</label>
								<input id="metaTitle" type="text" placeholder="Doe v. Canada" />
							</div>
							<div>
								<label for="metaCaseNumber">File number / source ID (identifier)</label>
								<input id="metaCaseNumber" type="text" placeholder="IMM-1234-24" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="metaCitation">Citation (identifier)</label>
								<input id="metaCitation" type="text" placeholder="2024 FC 100" />
							</div>
							<div>
								<label for="secondaryCitationFilter">Secondary citation</label>
								<input id="secondaryCitationFilter" type="text" placeholder="2024 FCA 1" />
							</div>
							<div>
								<label for="sourceNameFilter">Source name</label>
								<input id="sourceNameFilter" type="text" placeholder="A2AJ Canadian Legal Data" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="sourceUrlFilter">Source URL contains</label>
								<input id="sourceUrlFilter" type="text" placeholder="canlii.org" />
							</div>
							<div>
								<label for="datasetVersionFilter">Dataset version contains</label>
								<input id="datasetVersionFilter" type="text" placeholder="2024-" />
							</div>
							<div>
								<label for="upstreamLicenseFilter">Upstream license contains</label>
								<input id="upstreamLicenseFilter" type="text" placeholder="Open Government" />
							</div>
						</div>
						<div class="controls" style="grid-template-columns: 1fr 1fr 1fr 1fr; margin-top: 8px;">
							<div>
								<label for="courtType">Court type</label>
								<select id="courtType">
									<option value="">All courts</option>
									<option value="FC">FC</option>
									<option value="Federal Court">Federal Court</option>
									<option value="Federal Court of Appeal">Federal Court of Appeal</option>
									<option value="Ontario Court of Appeal">Ontario Court of Appeal</option>
								</select>
							</div>
							<div>
								<label for="jurisdictionFilter">Jurisdiction</label>
								<input id="jurisdictionFilter" type="text" placeholder="Canada" />
							</div>
							<div>
								<label for="sourceTypeFilter">Source type</label>
								<input id="sourceTypeFilter" type="text" placeholder="a2aj_curated" list="sourceTypeOptions" />
								<datalist id="sourceTypeOptions">
									<option value="a2aj_curated"></option>
									<option value="a2aj_parquet"></option>
									<option value="federal_court"></option>
									<option value="manual_test"></option>
								</datalist>
							</div>
							<div>
								<label for="languageFilter">Language</label>
								<select id="languageFilter">
									<option value="">Any</option>
									<option value="en">English</option>
									<option value="fr">French</option>
								</select>
							</div>
						</div>
						<details class="filter-group" open>
							<summary>Advanced metadata filters</summary>
							<div class="filter-grid">
								<div class="controls" style="grid-template-columns: 1fr 1fr 1fr 1fr; margin-top: 0;">
									<div>
										<label class="toggle" for="yearToggle"><input id="yearToggle" type="checkbox" /> Year filter</label>
										<input id="decisionYear" type="number" min="1900" max="2100" placeholder="2020" disabled />
									</div>
									<div>
										<label for="scrapedFrom">Scraped from</label>
										<input id="scrapedFrom" type="date" />
									</div>
									<div>
										<label for="scrapedTo">Scraped to</label>
										<input id="scrapedTo" type="date" />
									</div>
									<div>
										<label for="processingStatusFilter">Processing status</label>
										<select id="processingStatusFilter">
											<option value="">Any</option>
											<option value="raw">raw</option>
											<option value="embedded">embedded</option>
										</select>
									</div>
								</div>
								<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
									<div>
										<label for="citedCaseFilter">Noteup cited case</label>
										<input id="citedCaseFilter" type="text" placeholder="2007 FC 1262" />
									</div>
									<div>
										<label for="casesCitedFilter">Cases cited contains</label>
										<input id="casesCitedFilter" type="text" placeholder="2007 FC 1262" />
									</div>
									<div>
										<label for="casesCitingFilter">Cases citing contains</label>
										<input id="casesCitingFilter" type="text" placeholder="2026 FC 1" />
									</div>
								</div>
								<div class="controls" style="grid-template-columns: 1fr 1fr; margin-top: 8px;">
									<div>
										<label for="citingCasesMin">Citing cases min</label>
										<input id="citingCasesMin" type="number" min="0" placeholder="0" />
									</div>
									<div>
										<label for="citingCasesMax">Citing cases max</label>
										<input id="citingCasesMax" type="number" min="0" placeholder="100" />
									</div>
								</div>
								<div class="controls" style="grid-template-columns: repeat(3, 1fr); margin-top: 8px;">
									<label class="toggle" for="partyMinister"><input id="partyMinister" type="checkbox" checked /> Minister</label>
									<label class="toggle" for="partyIRCC"><input id="partyIRCC" type="checkbox" /> IRCC</label>
									<label class="toggle" for="partyCBSA"><input id="partyCBSA" type="checkbox" /> CBSA</label>
								</div>
							</div>
						</details>
						<div class="filter-actions">
							<button class="secondary" onclick="applyAgencyPreset('minister')">Minister preset</button>
							<button class="secondary" onclick="applyAgencyPreset('ircc')">IRCC preset</button>
							<button class="secondary" onclick="applyAgencyPreset('cbsa')">CBSA preset</button>
							<button class="secondary" onclick="applyAgencyPreset('all')">All agencies</button>
							<button class="secondary" onclick="clearSearchFilters()">Reset your search</button>
							<button onclick="runCaseSearch()">Start a search</button>
						</div>
						<div id="searchPageInfo" class="pill" style="margin-top: 12px;">No search run yet.</div>
						<div id="activeFilterSummary" class="helper-text">Active filters: Minister party preset</div>
					</div>
					<div class="preview-panel">
						<label for="search">Payload preview / advanced override</label>
						<textarea id="search">{
	"query": "non-refoulement risk review",
	"search_mode": "metadata",
	"semantic_weight": 0.7,
	"lexical_weight": 0.3,
	"source_type": "a2aj_curated",
	"party_filters": ["Minister"],
	"cited_case": "2007 FC 1262",
	"page": 1,
	"page_size": 15
}</textarea>
						<div class="helper-text">The form drives the search. The JSON preview stays in sync so you can inspect or fine-tune the payload if needed.</div>
					</div>
				</div>
				<div class="controls" style="grid-template-columns: 120px 120px 1fr; align-items:end; margin-top: 12px;">
					<div>
						<label for="searchPage">Page</label>
						<input id="searchPage" type="number" min="1" value="1" />
					</div>
					<div>
						<label for="searchPageSize">Per page</label>
						<input id="searchPageSize" type="number" min="1" max="50" value="15" />
					</div>
					<div>
						<div class="pill">Use the filters above, then search.</div>
					</div>
				</div>
				<div class="controls" style="grid-template-columns: 1fr 1fr; margin-top:10px;">
					<button class="secondary" onclick="changeSearchPage(-1)">Previous page</button>
					<button onclick="changeSearchPage(1)">Next page</button>
				</div>
				<div id="searchResult" class="result"></div>
				<div id="caseTextResult" class="result"></div>
			</section>

			<section class="card">
				<h2>POST /search/chunks</h2>
				<label for="chunks">JSON payload</label>
				<textarea id="chunks">{
	"query": "torture evidence and internal flight alternative",
	"source_type": "a2aj_curated",
	"cited_case": "2007 FC 1262",
	"page": 1,
	"page_size": 5
}</textarea>
				<div class="controls">
					<label class="toggle" for="groupChunks"><input id="groupChunks" type="checkbox" checked /> Group by case</label>
					<div>
						<label for="maxChunksPerCase">Top chunks per case</label>
						<input id="maxChunksPerCase" type="number" min="1" max="10" value="2" />
					</div>
				</div>
				<button onclick="runChunkSearch()">Run grouped chunk search</button>
				<button class="secondary" onclick="sendJson('POST', '/search/chunks', 'chunks', 'chunksResult')">Run raw chunk search</button>
				<div id="chunksResult" class="result"></div>
			</section>

			<section class="card">
				<h2>GET /cases/{id}</h2>
				<label for="caseId">Case ID</label>
				<input id="caseId" type="number" value="1" min="1" />
				<button class="secondary" onclick="getCaseById()">Fetch case</button>
				<div id="caseResult" class="result"></div>
			</section>
		</div>
	</div>

	<script>
		function pretty(data) {
			return JSON.stringify(data, null, 2);
		}

		function escapeHtml(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function previewText(value, maxLength = 180) {
			const normalized = String(value ?? "").replace(/\\s+/g, " ").trim();
			if (!normalized) {
				return "Click to open full text.";
			}
			if (normalized.length <= maxLength) {
				return normalized;
			}
			return `${normalized.slice(0, maxLength).trimEnd()}...`;
		}

		function renderCaseResultPane(caseRecord) {
			const output = document.getElementById("caseTextResult");
			const text = caseRecord.full_text || caseRecord.summary || "No text available.";
			output.innerHTML = `
				<strong>${escapeHtml(caseRecord.title || "Untitled case")}</strong><br />
				<span class="pill">${escapeHtml(caseRecord.citation || "No citation")}</span>
				<span class="pill">Case ID ${escapeHtml(caseRecord.id)}</span>
				<div class="case-text">${escapeHtml(text)}</div>
			`;
		}

		function updateSearchPageInfo(text) {
			const info = document.getElementById("searchPageInfo");
			if (info) {
				info.textContent = text;
			}
		}

		function updateActiveFilterSummary(payload) {
			const summary = document.getElementById("activeFilterSummary");
			if (!summary) {
				return;
			}
			const labels = [];
			if (payload.title_contains) labels.push(`title:${payload.title_contains}`);
			if (payload.citation_contains) labels.push(`citation:${payload.citation_contains}`);
			if (payload.secondary_citation_contains) labels.push(`secondary:${payload.secondary_citation_contains}`);
			if (payload.court) labels.push(`court:${payload.court}`);
			if (payload.jurisdiction) labels.push(`jurisdiction:${payload.jurisdiction}`);
			if (payload.source_type) labels.push(`source_type:${payload.source_type}`);
			if (payload.language) labels.push(`language:${payload.language}`);
			if (Array.isArray(payload.party_filters) && payload.party_filters.length) labels.push(`party:${payload.party_filters.join(",")}`);
			if (payload.date_from || payload.date_to) labels.push(`decision_date:${payload.date_from || "?"}..${payload.date_to || "?"}`);
			if (payload.scraped_from || payload.scraped_to) labels.push(`scraped:${payload.scraped_from || "?"}..${payload.scraped_to || "?"}`);
			if (payload.processing_status) labels.push(`status:${payload.processing_status}`);
			if (payload.cited_case) labels.push(`cited_case:${payload.cited_case}`);
			if (payload.cases_cited_contains) labels.push(`cases_cited:${payload.cases_cited_contains}`);
			if (payload.cases_citing_contains) labels.push(`cases_citing:${payload.cases_citing_contains}`);
			if (payload.citing_cases_min !== undefined || payload.citing_cases_max !== undefined) {
				labels.push(`citing_count:${payload.citing_cases_min ?? "?"}..${payload.citing_cases_max ?? "?"}`);
			}
			summary.textContent = labels.length ? `Active filters: ${labels.join(" | ")}` : "Active filters: none";
		}

		function getSearchPayload() {
			return JSON.parse(document.getElementById("search").value);
		}

		function setFieldValue(id, value) {
			const field = document.getElementById(id);
			if (field) {
				field.value = value ?? "";
			}
		}

		function setFieldChecked(id, value) {
			const field = document.getElementById(id);
			if (field) {
				field.checked = Boolean(value);
			}
		}

		function setSearchPayload(payload) {
			document.getElementById("search").value = JSON.stringify(payload, null, 2);
			document.getElementById("searchPage").value = String(payload.page ?? 1);
			document.getElementById("searchPageSize").value = String(payload.page_size ?? 15);
			setFieldValue("searchQuery", payload.query);
			setFieldValue("metaTitle", payload.title_contains);
			setFieldValue("metaCaseNumber", payload.source_id_contains);
			setFieldValue("metaCitation", payload.citation_contains);
			setFieldValue("secondaryCitationFilter", payload.secondary_citation_contains);
			setFieldValue("sourceNameFilter", payload.source_name_contains);
			setFieldValue("sourceUrlFilter", payload.source_url_contains);
			setFieldValue("datasetVersionFilter", payload.dataset_version_contains);
			setFieldValue("upstreamLicenseFilter", payload.upstream_license_contains);
			document.getElementById("courtType").value = payload.court ?? "";
			setFieldValue("jurisdictionFilter", payload.jurisdiction);
			setFieldValue("sourceTypeFilter", payload.source_type);
			document.getElementById("languageFilter").value = payload.language ?? "";
			const hasYearFilter = Boolean(payload.date_from || payload.date_to);
			document.getElementById("yearToggle").checked = hasYearFilter;
			document.getElementById("decisionYear").disabled = !hasYearFilter;
			document.getElementById("decisionYear").value = hasYearFilter && payload.date_from ? String(new Date(payload.date_from).getFullYear()) : "";
			setFieldValue("scrapedFrom", payload.scraped_from);
			setFieldValue("scrapedTo", payload.scraped_to);
			document.getElementById("processingStatusFilter").value = payload.processing_status ?? "";
			setFieldValue("citedCaseFilter", payload.cited_case);
			setFieldValue("casesCitedFilter", payload.cases_cited_contains);
			setFieldValue("casesCitingFilter", payload.cases_citing_contains);
			setFieldValue("citingCasesMin", payload.citing_cases_min);
			setFieldValue("citingCasesMax", payload.citing_cases_max);
			setFieldChecked("partyMinister", Array.isArray(payload.party_filters) ? payload.party_filters.includes("Minister") : false);
			setFieldChecked("partyIRCC", Array.isArray(payload.party_filters) ? payload.party_filters.includes("IRCC") : false);
			setFieldChecked("partyCBSA", Array.isArray(payload.party_filters) ? payload.party_filters.includes("CBSA") : false);
			updateActiveFilterSummary(payload);
		}

		function syncSearchControlsToPayload(payload) {
			payload.page = Math.max(1, Number(document.getElementById("searchPage").value || payload.page || 1));
			payload.page_size = Math.max(1, Math.min(50, Number(document.getElementById("searchPageSize").value || payload.page_size || 15)));
			const queryText = document.getElementById("searchQuery").value.trim();
			if (queryText) {
				payload.query = queryText;
			}
			const titleContains = document.getElementById("metaTitle").value.trim();
			if (titleContains) {
				payload.title_contains = titleContains;
			} else {
				delete payload.title_contains;
			}
			const sourceId = document.getElementById("metaCaseNumber").value.trim();
			if (sourceId) {
				payload.source_id_contains = sourceId;
			} else {
				delete payload.source_id_contains;
			}
			const citation = document.getElementById("metaCitation").value.trim();
			if (citation) {
				payload.citation_contains = citation;
			} else {
				delete payload.citation_contains;
			}
			const secondaryCitation = document.getElementById("secondaryCitationFilter").value.trim();
			if (secondaryCitation) {
				payload.secondary_citation_contains = secondaryCitation;
			} else {
				delete payload.secondary_citation_contains;
			}
			const sourceName = document.getElementById("sourceNameFilter").value.trim();
			if (sourceName) {
				payload.source_name_contains = sourceName;
			} else {
				delete payload.source_name_contains;
			}
			const sourceUrl = document.getElementById("sourceUrlFilter").value.trim();
			if (sourceUrl) {
				payload.source_url_contains = sourceUrl;
			} else {
				delete payload.source_url_contains;
			}
			const datasetVersion = document.getElementById("datasetVersionFilter").value.trim();
			if (datasetVersion) {
				payload.dataset_version_contains = datasetVersion;
			} else {
				delete payload.dataset_version_contains;
			}
			const upstreamLicense = document.getElementById("upstreamLicenseFilter").value.trim();
			if (upstreamLicense) {
				payload.upstream_license_contains = upstreamLicense;
			} else {
				delete payload.upstream_license_contains;
			}
			const courtType = document.getElementById("courtType").value.trim();
			if (courtType) {
				payload.court = courtType;
			} else {
				delete payload.court;
			}
			const jurisdiction = document.getElementById("jurisdictionFilter").value.trim();
			if (jurisdiction) {
				payload.jurisdiction = jurisdiction;
			} else {
				delete payload.jurisdiction;
			}
			const sourceType = document.getElementById("sourceTypeFilter").value.trim();
			if (sourceType) {
				payload.source_type = sourceType;
			} else {
				delete payload.source_type;
			}
			const language = document.getElementById("languageFilter").value.trim();
			if (language) {
				payload.language = language;
			} else {
				delete payload.language;
			}
			const yearToggle = document.getElementById("yearToggle").checked;
			document.getElementById("decisionYear").disabled = !yearToggle;
			const yearValue = Number(document.getElementById("decisionYear").value);
			if (yearToggle && Number.isFinite(yearValue) && yearValue >= 1900) {
				payload.date_from = `${yearValue}-01-01`;
				payload.date_to = `${yearValue}-12-31`;
			} else {
				delete payload.date_from;
				delete payload.date_to;
				if (!yearToggle) {
					document.getElementById("decisionYear").value = "";
				}
			}
			const scrapedFrom = document.getElementById("scrapedFrom").value;
			if (scrapedFrom) {
				payload.scraped_from = scrapedFrom;
			} else {
				delete payload.scraped_from;
			}
			const scrapedTo = document.getElementById("scrapedTo").value;
			if (scrapedTo) {
				payload.scraped_to = scrapedTo;
			} else {
				delete payload.scraped_to;
			}
			const processingStatus = document.getElementById("processingStatusFilter").value.trim();
			if (processingStatus) {
				payload.processing_status = processingStatus;
			} else {
				delete payload.processing_status;
			}
			const citedCase = document.getElementById("citedCaseFilter").value.trim();
			if (citedCase) {
				payload.cited_case = citedCase;
			} else {
				delete payload.cited_case;
			}
			const casesCited = document.getElementById("casesCitedFilter").value.trim();
			if (casesCited) {
				payload.cases_cited_contains = casesCited;
			} else {
				delete payload.cases_cited_contains;
			}
			const casesCiting = document.getElementById("casesCitingFilter").value.trim();
			if (casesCiting) {
				payload.cases_citing_contains = casesCiting;
			} else {
				delete payload.cases_citing_contains;
			}
			const citingCasesMin = document.getElementById("citingCasesMin").value.trim();
			if (citingCasesMin !== "") {
				payload.citing_cases_min = Math.max(0, Number(citingCasesMin));
			} else {
				delete payload.citing_cases_min;
			}
			const citingCasesMax = document.getElementById("citingCasesMax").value.trim();
			if (citingCasesMax !== "") {
				payload.citing_cases_max = Math.max(0, Number(citingCasesMax));
			} else {
				delete payload.citing_cases_max;
			}
			const partyFilters = [];
			if (document.getElementById("partyMinister").checked) {
				partyFilters.push("Minister");
			}
			if (document.getElementById("partyIRCC").checked) {
				partyFilters.push("IRCC");
			}
			if (document.getElementById("partyCBSA").checked) {
				partyFilters.push("CBSA");
			}
			if (partyFilters.length > 0) {
				payload.party_filters = partyFilters;
			} else {
				delete payload.party_filters;
			}
			setSearchPayload(payload);
			return payload;
		}

		function clearSearchFilters() {
			const payload = getSearchPayload();
			setSearchPayload({
				query: payload.query || document.getElementById("searchQuery").value.trim() || "",
				search_mode: payload.search_mode || "metadata",
				semantic_weight: payload.semantic_weight ?? 0.7,
				lexical_weight: payload.lexical_weight ?? 0.3,
				page: 1,
				page_size: Number(document.getElementById("searchPageSize").value || payload.page_size || 15),
			});
		}

		function applyAgencyPreset(preset) {
			const payload = getSearchPayload();
			if (preset === "minister") {
				payload.party_filters = ["Minister"];
			} else if (preset === "ircc") {
				payload.party_filters = ["IRCC"];
			} else if (preset === "cbsa") {
				payload.party_filters = ["CBSA"];
			} else {
				payload.party_filters = ["Minister", "IRCC", "CBSA"];
			}
			setSearchPayload(payload);
		}

		document.addEventListener("keydown", (event) => {
			if (event.key !== "Enter") {
				return;
			}
			if (event.target && event.target.tagName === "TEXTAREA") {
				return;
			}
			event.preventDefault();
			runCaseSearch();
		});

		function searchPageCount(total, pageSize) {
			if (!total || !pageSize) {
				return 0;
			}
			return Math.max(1, Math.ceil(total / pageSize));
		}

		function renderSearchPageInfo(total, page, pageSize, shown) {
			const totalPages = searchPageCount(total, pageSize);
			const start = total === 0 ? 0 : ((page - 1) * pageSize) + 1;
			const end = total === 0 ? 0 : Math.min(total, (page - 1) * pageSize + shown);
			updateSearchPageInfo(`Showing ${start}-${end} of ${total} results${totalPages ? ` · page ${page}/${totalPages}` : ""}`);
		}

		function getSearchHeaders(response) {
			return {
				total: Number(response.headers.get("x-search-total") || 0),
				page: Number(response.headers.get("x-search-page") || 1),
				pageSize: Number(response.headers.get("x-search-page-size") || 15),
			};
		}

		function getResultMatchSource(item) {
			if (item.match_source) {
				return item.match_source;
			}
			return "Unknown";
		}

		const caseTextCache = {};

		async function toggleCaseText(caseId) {
			const detail = document.getElementById(`case-detail-${caseId}`);
			if (!detail) {
				return;
			}
			if (detail.classList.contains("open")) {
				detail.classList.remove("open");
				return;
			}
			detail.classList.add("open");
			if (caseTextCache[caseId]) {
				detail.innerHTML = caseTextCache[caseId];
				return;
			}
			detail.innerHTML = "Loading case text...";
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				if (!response.ok) {
					detail.innerHTML = `<span style=\"color:#8c3b2f;\">${escapeHtml(body.detail || 'Failed to load case text.')}</span>`;
					return;
				}
				const text = body.full_text || body.summary || "No text available.";
				const html = `
					<strong>${escapeHtml(body.title || "Untitled case")}</strong><br />
					<span class="pill">${escapeHtml(body.citation || "No citation")}</span>
					<span class="pill">Case ID ${escapeHtml(body.id)}</span>
					<div class="case-text">${escapeHtml(text)}</div>
				`;
				caseTextCache[caseId] = html;
				detail.innerHTML = html;
			} catch (error) {
				detail.innerHTML = `<span style=\"color:#8c3b2f;\">Request error: ${escapeHtml(error.message)}</span>`;
			}
		}

		function renderSearchResults(results) {
			const output = document.getElementById("searchResult");
			if (!Array.isArray(results) || results.length === 0) {
				output.innerHTML = "No results.";
				return;
			}

			const rows = results.map((item) => `
				<div class="case-card compact">
					<a href="#" class="hit-title" onclick="toggleCaseText(${Number(item.id)}); return false;">
						${escapeHtml(item.title || "Untitled case")}
					</a>
					<div class="hit-meta">
						${escapeHtml(item.citation || "No citation")}${item.court ? ` · ${escapeHtml(item.court)}` : ""} · score ${Number(item.similarity ?? 0).toFixed(3)} · ${escapeHtml(getResultMatchSource(item))}
					</div>
					<div class="case-summary">${escapeHtml(previewText(item.summary || ""))}</div>
					<div style="margin-top:6px;">
						<button class="secondary" style="width:auto; margin-top:0; padding:6px 10px; font-size:0.82rem;" onclick="toggleCaseText(${Number(item.id)}); return false;">Open text</button>
					</div>
					<div id="case-detail-${Number(item.id)}" class="case-detail"></div>
				</div>
			`).join("");

			output.innerHTML = rows;
		}

		async function changeSearchPage(delta) {
			let payload;
			try {
				payload = getSearchPayload();
			} catch (error) {
				updateSearchPageInfo(`Invalid JSON: ${error.message}`);
				return;
			}
			payload = syncSearchControlsToPayload(payload);
			payload.page = Math.max(1, (Number(payload.page) || 1) + delta);
			setSearchPayload(payload);
			await runCaseSearch();
		}

		async function runCaseSearch() {
			const output = document.getElementById("searchResult");
			let payload;
			try {
				payload = syncSearchControlsToPayload(getSearchPayload());
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			document.getElementById("caseTextResult").textContent = "";
			const start = performance.now();
			try {
				const response = await fetch("/search", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.innerHTML = `<div style="margin-bottom:10px;">[${response.status}] ${escapeHtml(response.statusText)} (${elapsed} ms)</div>`;
				if (Array.isArray(body)) {
					const headers = getSearchHeaders(response);
					renderSearchPageInfo(headers.total, headers.page, headers.pageSize, body.length);
					renderSearchResults(body);
				} else {
					output.innerHTML += `<pre style="margin:0; white-space:pre-wrap;">${escapeHtml(pretty(body))}</pre>`;
				}
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function fetchCaseText(caseId) {
			const output = document.getElementById("caseTextResult");
			if (!caseId || caseId < 1) {
				output.textContent = "Enter a valid positive case ID.";
				return;
			}
			output.textContent = "Loading case text...";
			const start = performance.now();
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.innerHTML = `<div style="margin-bottom:10px;">[${response.status}] ${escapeHtml(response.statusText)} (${elapsed} ms)</div>`;
				if (response.ok) {
					renderCaseResultPane(body);
				} else {
					output.innerHTML += `<pre style="margin:0; white-space:pre-wrap;">${escapeHtml(pretty(body))}</pre>`;
				}
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		function groupChunkResults(rows, maxChunksPerCase) {
			const grouped = new Map();
			for (const row of rows) {
				if (!grouped.has(row.id)) {
					grouped.set(row.id, {
						id: row.id,
						title: row.title,
						citation: row.citation,
						court: row.court,
						jurisdiction: row.jurisdiction,
						best_similarity: row.similarity,
						chunks: [],
					});
				}
				const entry = grouped.get(row.id);
				entry.best_similarity = Math.max(entry.best_similarity, row.similarity ?? 0);
				entry.chunks.push({
					chunk_index: row.chunk_index,
					similarity: row.similarity,
					chunk_text: row.chunk_text,
				});
			}

			const cases = Array.from(grouped.values());
			for (const item of cases) {
				item.chunks.sort((a, b) => (b.similarity ?? 0) - (a.similarity ?? 0));
				item.chunks = item.chunks.slice(0, maxChunksPerCase);
			}
			cases.sort((a, b) => (b.best_similarity ?? 0) - (a.best_similarity ?? 0));
			return {
				result_type: "grouped_by_case",
				total_cases: cases.length,
				total_chunks: rows.length,
				max_chunks_per_case: maxChunksPerCase,
				cases,
			};
		}

		async function sendJson(method, url, inputId, outputId) {
			const output = document.getElementById(outputId);
			let payload;
			try {
				payload = JSON.parse(document.getElementById(inputId).value);
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const response = await fetch(url, {
					method,
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function runChunkSearch() {
			const output = document.getElementById("chunksResult");
			const groupByCase = document.getElementById("groupChunks").checked;
			const maxChunksValue = Number(document.getElementById("maxChunksPerCase").value);
			const maxChunksPerCase = Number.isFinite(maxChunksValue) && maxChunksValue > 0 ? maxChunksValue : 2;

			let payload;
			try {
				payload = JSON.parse(document.getElementById("chunks").value);
			} catch (error) {
				output.textContent = `Invalid JSON: ${error.message}`;
				return;
			}

			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const url = groupByCase ? "/search/chunks/grouped" : "/search/chunks";
				const groupedPayload = groupByCase ? { ...payload, max_chunks_per_case: maxChunksPerCase } : payload;
				const response = await fetch(url, {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(groupedPayload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}

		async function getCaseById() {
			const caseId = Number(document.getElementById("caseId").value);
			const output = document.getElementById("caseResult");
			if (!caseId || caseId < 1) {
				output.textContent = "Enter a valid positive case ID.";
				return;
			}
			output.textContent = "Sending request...";
			const start = performance.now();
			try {
				const response = await fetch(`/cases/${caseId}`);
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));
				const elapsed = (performance.now() - start).toFixed(0);
				output.textContent = `[${response.status}] ${response.statusText} (${elapsed} ms)\n\n${pretty(body)}`;
			} catch (error) {
				output.textContent = `Request error: ${error.message}`;
			}
		}
	</script>
</body>
</html>
"""


def _prototype_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>Prototype Explorer</title>
	<style>
		:root {
			--bg: #f4efe6;
			--panel: #fffaf0;
			--ink: #1e1b16;
			--muted: #5d5547;
			--accent: #0d6a5f;
			--accent-2: #b65d2e;
			--line: #d8cebf;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 10% 8%, #f0e5d4 0, transparent 34%),
				radial-gradient(circle at 90% 88%, #d9ece8 0, transparent 35%),
				var(--bg);
		}
		.wrap { max-width: 1150px; margin: 0 auto; padding: 22px; }
		h1 { margin: 0 0 6px; font-size: clamp(1.55rem, 2.4vw, 2.2rem); }
		.lead { margin: 0 0 14px; color: var(--muted); }
		.grid { display: grid; gap: 14px; grid-template-columns: 1fr 1fr 1fr; }
		.card {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 12px;
			padding: 14px;
		}
		.card h2 { margin: 0 0 8px; font-size: 1rem; }
		.stat { font-size: 1.8rem; font-weight: 700; line-height: 1.1; }
		.stat-note { color: var(--muted); font-size: 0.86rem; }
		.controls { display: grid; gap: 10px; grid-template-columns: 1.2fr 0.8fr 0.6fr; margin-top: 12px; }
		label { display: block; font-size: 0.82rem; color: var(--muted); margin-bottom: 4px; }
		input, select, button {
			width: 100%; border: 1px solid var(--line); border-radius: 8px;
			padding: 9px 10px; font-size: 0.92rem; background: #fff;
		}
		button {
			background: linear-gradient(135deg, var(--accent), #14867a);
			color: #fff; font-weight: 600; border: none; cursor: pointer;
		}
		button.secondary { background: linear-gradient(135deg, var(--accent-2), #cf7d49); }
		.pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
		.pill {
			border: 1px solid var(--line); border-radius: 999px;
			padding: 3px 9px; font-size: 0.78rem; color: var(--muted);
		}
		.graph-canvas {
			width: 100%;
			height: 620px;
			border: 1px solid var(--line);
			border-radius: 10px;
			background:
				radial-gradient(circle at 20% 20%, #fffdf8 0, #f4ecdf 100%);
		}
		.graph-meta {
			display: flex;
			justify-content: space-between;
			gap: 10px;
			flex-wrap: wrap;
			margin-top: 8px;
		}
		table {
			width: 100%; border-collapse: collapse; margin-top: 12px; background: var(--panel);
			border: 1px solid var(--line); border-radius: 10px; overflow: hidden;
		}
		th, td { text-align: left; padding: 8px 9px; border-bottom: 1px solid #eee3d3; vertical-align: top; }
		th { background: #f9f0e2; font-size: 0.81rem; text-transform: uppercase; letter-spacing: 0.03em; color: #6d614f; }
		tr:last-child td { border-bottom: none; }
		.small { color: var(--muted); font-size: 0.82rem; }
		@media (max-width: 960px) {
			.grid { grid-template-columns: 1fr 1fr; }
			.controls { grid-template-columns: 1fr; }
		}
		@media (max-width: 620px) {
			.grid { grid-template-columns: 1fr; }
		}
	</style>
</head>
<body>
	<div class="wrap">
		<nav style="display:flex;gap:14px;margin-bottom:16px;font-size:0.88rem;">
			<a href="/research" style="color:#0d6a5f;text-decoration:none;">Research</a>
			<a href="/testing" style="color:#0d6a5f;text-decoration:none;">API Tester</a>
		</nav>
		<h1>Prototype Explorer</h1>
		<p class="lead">Inspect the immigration prototype cohort, topic tags, and citation-map readiness.</p>
		<div class="pills">
			<div class="pill">Prototype set: immigration_334_v1</div>
			<div class="pill">Scope: embedded + chunked cohort only</div>
		</div>

		<div class="grid" id="statsGrid">
			<div class="card"><h2>Total Cases</h2><div class="stat" id="statTotal">-</div><div class="stat-note">Cases in cohort</div></div>
			<div class="card"><h2>Embedded</h2><div class="stat" id="statEmbedded">-</div><div class="stat-note">Cases with vector</div></div>
			<div class="card"><h2>Chunked</h2><div class="stat" id="statChunked">-</div><div class="stat-note">Cases with chunks</div></div>
			<div class="card"><h2>Citation Nodes</h2><div class="stat" id="statNodes">-</div><div class="stat-note">Internal graph nodes</div></div>
			<div class="card"><h2>Citation Edges</h2><div class="stat" id="statEdges">-</div><div class="stat-note">Internal graph edges</div></div>
			<div class="card"><h2>Unique Topics</h2><div class="stat" id="statTopics">-</div><div class="stat-note">Keyword topic taxonomy</div></div>
		</div>

		<div class="card" style="margin-top:14px;">
			<h2>Citation Map</h2>
			<div class="controls" style="grid-template-columns: 1fr 0.8fr 0.6fr; margin-top: 0;">
				<div>
					<label for="graphTopic">Focus topic</label>
					<select id="graphTopic"><option value="">All topics</option></select>
				</div>
				<div>
					<label for="graphNodes">Max nodes</label>
					<input id="graphNodes" type="number" min="30" max="280" value="160" />
				</div>
				<div>
					<label>&nbsp;</label>
					<button onclick="loadGraph()">Render map</button>
				</div>
			</div>
			<svg id="graphSvg" class="graph-canvas" viewBox="0 0 980 620" preserveAspectRatio="xMidYMid meet"></svg>
			<div class="graph-meta">
				<div class="small" id="graphInfo">Graph not loaded.</div>
				<div class="small" id="graphHover">Hover a node for details.</div>
			</div>
		</div>

		<div class="card" style="margin-top:14px;">
			<h2>Browse Cases</h2>
			<div class="controls">
				<div>
					<label for="q">Query</label>
					<input id="q" type="text" placeholder="vavilov, irpa s.34, humanitarian and compassionate" />
				</div>
				<div>
					<label for="topic">Topic</label>
					<select id="topic"><option value="">All topics</option></select>
				</div>
				<div>
					<label for="pageSize">Per page</label>
					<input id="pageSize" type="number" min="5" max="100" value="20" />
				</div>
			</div>
			<div class="controls" style="grid-template-columns: 1fr 1fr 1fr; margin-top: 8px;">
				<button onclick="runSearch(1)">Search</button>
				<button class="secondary" onclick="prevPage()">Previous</button>
				<button onclick="nextPage()">Next</button>
			</div>
			<div class="small" id="pageInfo" style="margin-top:10px;">No search yet.</div>
			<div id="tableWrap"></div>
		</div>
	</div>

	<script>
		let currentPage = 1;
		let total = 0;

		function esc(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function parseList(value) {
			if (!Array.isArray(value)) return "";
			return value.join(", ");
		}

		function topicColor(topic) {
			const palette = {
				refugee_protection: '#176f67',
				removal_detention: '#b65d2e',
				inadmissibility_security: '#8b3f62',
				family_hc: '#3f6db0',
				citizenship_status: '#8b6c10',
				judicial_review_procedure: '#4f4a9c',
			};
			return palette[topic] || '#6f6456';
		}

		async function loadSummary() {
			const res = await fetch('/prototype/summary');
			const body = await res.json();
			document.getElementById('statTotal').textContent = body.total_cases ?? 0;
			document.getElementById('statEmbedded').textContent = body.embedded_cases ?? 0;
			document.getElementById('statChunked').textContent = body.chunked_cases ?? 0;
			document.getElementById('statNodes').textContent = body.citation_nodes ?? 0;
			document.getElementById('statEdges').textContent = body.citation_edges ?? 0;
			document.getElementById('statTopics').textContent = Object.keys(body.topic_distribution || {}).length;

			const topicSelect = document.getElementById('topic');
			const graphTopicSelect = document.getElementById('graphTopic');
			for (const key of Object.keys(body.topic_distribution || {})) {
				const opt = document.createElement('option');
				opt.value = key;
				opt.textContent = `${key} (${body.topic_distribution[key]})`;
				topicSelect.appendChild(opt);
				graphTopicSelect.appendChild(opt.cloneNode(true));
			}
		}

		function createInitialLayout(nodes, width, height) {
			const centerX = width / 2;
			const centerY = height / 2;
			const radius = Math.min(width, height) * 0.36;
			return nodes.map((node, index) => {
				const angle = (Math.PI * 2 * index) / Math.max(nodes.length, 1);
				return {
					...node,
					x: centerX + (Math.cos(angle) * radius),
					y: centerY + (Math.sin(angle) * radius),
					vx: 0,
					vy: 0,
				};
			});
		}

		function forceLayout(nodes, edges, width, height) {
			const byId = new Map(nodes.map((n) => [n.id, n]));
			const edgePairs = edges
				.map((e) => [byId.get(e.source), byId.get(e.target)])
				.filter((pair) => pair[0] && pair[1]);
			const repulsion = 14000;
			const springLength = 85;
			const springStrength = 0.015;
			const damping = 0.86;
			const pad = 20;

			for (let step = 0; step < 170; step += 1) {
				for (let i = 0; i < nodes.length; i += 1) {
					for (let j = i + 1; j < nodes.length; j += 1) {
						const a = nodes[i];
						const b = nodes[j];
						let dx = a.x - b.x;
						let dy = a.y - b.y;
						const distSq = Math.max(20, (dx * dx) + (dy * dy));
						const force = repulsion / distSq;
						const dist = Math.sqrt(distSq);
						dx /= dist;
						dy /= dist;
						a.vx += dx * force;
						a.vy += dy * force;
						b.vx -= dx * force;
						b.vy -= dy * force;
					}
				}

				for (const [a, b] of edgePairs) {
					let dx = b.x - a.x;
					let dy = b.y - a.y;
					const dist = Math.max(1, Math.sqrt((dx * dx) + (dy * dy)));
					const stretch = dist - springLength;
					dx /= dist;
					dy /= dist;
					const fx = dx * stretch * springStrength;
					const fy = dy * stretch * springStrength;
					a.vx += fx;
					a.vy += fy;
					b.vx -= fx;
					b.vy -= fy;
				}

				for (const node of nodes) {
					node.vx *= damping;
					node.vy *= damping;
					node.x = Math.min(width - pad, Math.max(pad, node.x + node.vx));
					node.y = Math.min(height - pad, Math.max(pad, node.y + node.vy));
				}
			}
			return nodes;
		}

		function renderGraph(payload) {
			const svg = document.getElementById('graphSvg');
			svg.innerHTML = '';
			const width = 980;
			const height = 620;
			const nodes = forceLayout(createInitialLayout(payload.nodes || [], width, height), payload.edges || [], width, height);
			const byId = new Map(nodes.map((n) => [n.id, n]));

			const selectNode = (node) => {
				const citation = (node.citation || '').trim();
				if (!citation) {
					document.getElementById('graphHover').textContent = 'Selected node has no citation to filter.';
					return;
				}
				document.getElementById('q').value = citation;
				document.getElementById('graphHover').textContent = `Selected ${citation}; table filtered by citation.`;
				runSearch(1);
			};

			for (const edge of payload.edges || []) {
				const source = byId.get(edge.source);
				const target = byId.get(edge.target);
				if (!source || !target) continue;
				const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
				line.setAttribute('x1', String(source.x));
				line.setAttribute('y1', String(source.y));
				line.setAttribute('x2', String(target.x));
				line.setAttribute('y2', String(target.y));
				line.setAttribute('stroke', '#ccbca4');
				line.setAttribute('stroke-width', '1');
				line.setAttribute('stroke-opacity', '0.65');
				svg.appendChild(line);
			}

			for (const node of nodes) {
				const topic = Array.isArray(node.topics) && node.topics.length ? node.topics[0] : '';
				const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
				circle.setAttribute('cx', String(node.x));
				circle.setAttribute('cy', String(node.y));
				circle.setAttribute('r', String(Math.min(11, 3 + Math.sqrt(Math.max(1, Number(node.degree || 1))))));
				circle.setAttribute('fill', topicColor(topic));
				circle.setAttribute('fill-opacity', '0.88');
				circle.setAttribute('stroke', '#ffffff');
				circle.setAttribute('stroke-width', '1.3');
				circle.setAttribute('data-case-id', String(node.id || ''));
				circle.setAttribute('data-citation', String(node.citation || ''));
				circle.setAttribute('data-title', String(node.title || ''));
				circle.style.cursor = 'pointer';
				circle.addEventListener('mouseenter', () => {
					document.getElementById('graphHover').textContent = `${node.citation || 'No citation'} | ${node.title || 'Untitled'} | degree=${node.degree || 0}`;
				});
				circle.addEventListener('click', () => {
					selectNode(node);
				});
				svg.appendChild(circle);

				if ((node.degree || 0) >= 10) {
					const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
					text.setAttribute('x', String(node.x + 6));
					text.setAttribute('y', String(node.y - 6));
					text.setAttribute('font-size', '10');
					text.setAttribute('fill', '#3f362a');
					text.style.cursor = 'pointer';
					text.textContent = (node.citation || '').slice(0, 20);
					text.addEventListener('click', () => selectNode(node));
					svg.appendChild(text);
				}
			}

			const meta = payload.meta || {};
			document.getElementById('graphInfo').textContent = `Showing ${meta.returned_nodes || 0} of ${meta.total_nodes || 0} nodes and ${meta.returned_edges || 0} of ${meta.total_edges || 0} edges.`;
		}

		async function loadGraph() {
			const topic = document.getElementById('graphTopic').value.trim();
			const maxNodes = Math.max(30, Math.min(280, Number(document.getElementById('graphNodes').value || 160)));
			const params = new URLSearchParams({ max_nodes: String(maxNodes) });
			if (topic) params.set('topic', topic);
			document.getElementById('graphInfo').textContent = 'Rendering graph...';
			try {
				const response = await fetch(`/prototype/graph?${params.toString()}`);
				const payload = await response.json();
				renderGraph(payload);
			} catch (error) {
				document.getElementById('graphInfo').textContent = `Unable to load graph: ${error.message}`;
			}
		}

		function renderRows(items) {
			if (!Array.isArray(items) || items.length === 0) {
				document.getElementById('tableWrap').innerHTML = '<div class="small" style="margin-top:12px;">No cases matched.</div>';
				return;
			}
			const rows = items.map((item) => `
				<tr>
					<td>${esc(item.case_id)}</td>
					<td>${esc(item.citation || '')}</td>
					<td>${esc(item.title || '')}</td>
					<td>${esc(item.court || '')}</td>
					<td>${esc(item.date || '')}</td>
					<td>${esc(parseList(item.topic_keywords))}</td>
					<td>${esc(item.chunk_count)}</td>
				</tr>
			`).join('');
			document.getElementById('tableWrap').innerHTML = `
				<table>
					<thead>
						<tr>
							<th>ID</th><th>Citation</th><th>Title</th><th>Court</th><th>Date</th><th>Topics</th><th>Chunks</th>
						</tr>
					</thead>
					<tbody>${rows}</tbody>
				</table>
			`;
		}

		async function runSearch(page) {
			currentPage = page;
			const q = document.getElementById('q').value.trim();
			const topic = document.getElementById('topic').value.trim();
			const pageSize = Math.max(5, Math.min(100, Number(document.getElementById('pageSize').value || 20)));
			const params = new URLSearchParams({ page: String(currentPage), page_size: String(pageSize) });
			if (q) params.set('q', q);
			if (topic) params.set('topic', topic);
			const res = await fetch(`/prototype/cases?${params.toString()}`);
			const body = await res.json();
			total = Number(body.total || 0);
			renderRows(body.items || []);
			const shownFrom = total === 0 ? 0 : ((currentPage - 1) * pageSize) + 1;
			const shownTo = total === 0 ? 0 : Math.min(total, (currentPage - 1) * pageSize + (body.items || []).length);
			document.getElementById('pageInfo').textContent = `Showing ${shownFrom}-${shownTo} of ${total} (page ${currentPage})`;
		}

		function prevPage() { if (currentPage > 1) runSearch(currentPage - 1); }
		function nextPage() {
			const pageSize = Math.max(5, Math.min(100, Number(document.getElementById('pageSize').value || 20)));
			if (currentPage * pageSize < total) runSearch(currentPage + 1);
		}

		loadSummary().then(() => {
			runSearch(1);
			loadGraph();
		});
	</script>
</body>
</html>
"""


def _prototype_case_ids() -> list[int]:
	if not PROTOTYPE_IDS_CSV.exists():
		return []
	ids: list[int] = []
	with PROTOTYPE_IDS_CSV.open("r", encoding="utf-8", newline="") as file_obj:
		reader = csv.DictReader(file_obj)
		for row in reader:
			raw = row.get("case_id")
			if not raw:
				continue
			try:
				ids.append(int(raw))
			except ValueError:
				continue
	return ids


def _prototype_edges_count() -> int:
	if not PROTOTYPE_EDGES_CSV.exists():
		return 0
	with PROTOTYPE_EDGES_CSV.open("r", encoding="utf-8", newline="") as file_obj:
		row_count = sum(1 for _ in file_obj)
	# subtract header
	return max(0, row_count - 1)


def _prototype_edges() -> list[tuple[int, int, str]]:
	if not PROTOTYPE_EDGES_CSV.exists():
		return []
	edges: list[tuple[int, int, str]] = []
	with PROTOTYPE_EDGES_CSV.open("r", encoding="utf-8", newline="") as file_obj:
		reader = csv.DictReader(file_obj)
		for row in reader:
			try:
				source_case_id = int(row.get("source_case_id", ""))
				target_case_id = int(row.get("target_case_id", ""))
			except ValueError:
				continue
			edges.append((source_case_id, target_case_id, row.get("normalized_citation", "") or ""))
	return edges


def _prototype_topic_scores(text: str) -> dict[str, int]:
	scores: dict[str, int] = {}
	for topic, patterns in PROTOTYPE_TOPIC_PATTERNS.items():
		score = 0
		for pattern in patterns:
			score += len(re.findall(pattern, text, flags=re.IGNORECASE))
		scores[topic] = score
	return scores


def _case_topic_keywords(case: Case) -> list[str]:
	metadata = case.metadata_json or {}
	if isinstance(metadata, dict):
		topic_keywords = metadata.get("topic_keywords")
		if isinstance(topic_keywords, list):
			values = [str(value) for value in topic_keywords if value]
			if values:
				return values
	text = " ".join(
		[
			case.title or "",
			case.summary or "",
			case.full_text or "",
			" ".join(case.cases_cited or []),
		]
	)
	scores = _prototype_topic_scores(text)
	return [topic for topic, score in scores.items() if score > 0]


def _embed(text: str) -> list[float]:
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="OPENAI_API_KEY is not configured",
		)

	try:
		client = OpenAI(api_key=api_key)
		response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
	except OpenAIError as exc:
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY,
			detail="The embedding service is unavailable",
		) from exc

	embedding = response.data[0].embedding
	if len(embedding) != EMBEDDING_DIMENSIONS:
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY,
			detail="The embedding service returned an unexpected vector size",
		)
	return embedding


def _normalize_whitespace(value: str) -> str:
	return " ".join((value or "").split()).strip()


def _extract_legal_citations(text: str | None) -> list[str]:
	if not text or get_citations is None:
		return []

	results: list[str] = []
	seen: set[str] = set()
	for citation in get_citations(text):
		value: str | None = None
		if hasattr(citation, "corrected_citation"):
			maybe_callable = getattr(citation, "corrected_citation")
			result = maybe_callable() if callable(maybe_callable) else maybe_callable
			value = str(result) if result is not None else None
		if not value and hasattr(citation, "matched_text"):
			maybe_callable = getattr(citation, "matched_text")
			result = maybe_callable() if callable(maybe_callable) else maybe_callable
			value = str(result) if result is not None else None
		if not value:
			value = str(citation)

		normalized = " ".join(str(value).split())
		if normalized and normalized not in seen:
			seen.add(normalized)
			results.append(normalized)
	return results


def _build_reader_inferred_tags(case: Case, chunks: list[CaseChunk]) -> list[CaseReaderTagResponse]:
	text_parts: list[str] = []
	if case.full_text:
		text_parts.append(case.full_text)
	if case.summary:
		text_parts.append(case.summary)
	for chunk in chunks:
		if chunk.text:
			text_parts.append(chunk.text)
	content = "\n".join(text_parts)
	if not content.strip():
		return []

	catalog: list[tuple[str, str, str]] = [
		("forum", "federal_court", r"\bFederal Court\b|\bFC\b"),
		("forum", "rad", r"\bRAD\b|Refugee Appeal Division"),
		("forum", "rpd", r"\bRPD\b|Refugee Protection Division"),
		("forum", "iad", r"\bIAD\b|Immigration Appeal Division"),
		("forum", "id", r"\bID\b|Immigration Division"),
		("forum", "irb", r"\bIRB\b|Immigration and Refugee Board"),
		("statute", "irpa", r"\b(?:IRPA|Immigration and Refugee Protection Act)\b"),
		("statute", "irpr", r"\b(?:IRPR|Immigration and Refugee Protection Regulations?)\b"),
		("issue", "procedural_fairness", r"procedural fairness|natural justice|right to be heard|fair hearing"),
		("issue", "reasonableness", r"\breasonableness\b|unreasonable decision|reasonable decision"),
		("issue", "standard_of_review", r"standard of review|palpable and overriding error|correctness standard"),
		("issue", "credibility", r"\bcredibility\b|credible evidence|credibility finding"),
		("issue", "jurisdiction", r"\bjurisdiction\b|jurisdictional error"),
		("issue", "delay", r"\bdelay\b|unreasonable delay|mandamus"),
		("issue", "detention", r"\bdetention\b|detained|detention review"),
		("issue", "removal", r"\bremoval\b|removal order|pre-removal risk assessment|\bPRRA\b"),
		("issue", "inadmissibility", r"inadmissib|security certificate|organized criminality|misrepresentation"),
		("issue", "refugee_protection", r"refugee protection|Convention refugee|person in need of protection|\bclaimant\b"),
		("issue", "humanitarian_compassionate", r"humanitarian and compassionate|\bH&C\b|\bH[.]\s*&\s*C[.]\b"),
		("issue", "family_reunification", r"family reunification|family class|spousal sponsorship|sponsorship application"),
		("issue", "temporary_residence", r"temporary resident|study permit|work permit|visitor visa|temporary foreign worker"),
		("issue", "citizenship", r"\bcitizenship\b|citizenship application|citizenship revocation"),
		("analysis", "ifa", r"\bIFA\b|internal flight alternative|alternative of internal flight"),
		("analysis", "charter", r"\bCharter\b|Canadian Charter of Rights and Freedoms|section 7 of the Charter"),
		("analysis", "statutory_interpretation", r"statutory interpretation|purposive interpretation|modern principle of interpretation"),
		("analysis", "adr", r"\bADR\b|\bAdministrative\s+Deferral\s+of\s+Removal\b"),
	]

	tags: list[CaseReaderTagResponse] = []
	seen_values: set[str] = set()
	for category, value, pattern in catalog:
		match = re.search(pattern, content, flags=re.IGNORECASE)
		if match is None:
			continue
		key = f"{category}:{value}"
		if key in seen_values:
			continue
		seen_values.add(key)
		evidence = content[max(0, match.start() - 80): min(len(content), match.end() + 80)].strip()
		tags.append(
			CaseReaderTagResponse(
				category=category,
				value=value,
				score=0.9,
				evidence=evidence,
				source="reader_keyword",
				taxonomy_version="reader_v1",
			)
		)

	section_hits: dict[str, str] = {}

	def add_section_tag(tag_value: str, evidence: str) -> None:
		if not tag_value or tag_value in section_hits:
			return
		section_hits[tag_value] = evidence

	for match in re.finditer(r"\b(?:IRPA|IRPR)\s+(?:s\.|section)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)", content, flags=re.IGNORECASE):
		section = _normalize_whitespace(match.group(1))
		prefix = "irpr" if re.search(r"\bIRPR\b", match.group(0), flags=re.IGNORECASE) else "irpa"
		add_section_tag(f"{prefix}_s_{section}", content[max(0, match.start() - 80): min(len(content), match.end() + 80)].strip())
		if len(section_hits) >= 20:
			break

	for match in re.finditer(r"\b(?:ss?\.|sections?|subsections?|paragraphs?)\s*(\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*(?:\s*(?:to|-|and|or)\s*\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*)*)\s+of\s+(?:the\s+)?(IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations|Canadian Charter of Rights and Freedoms|Charter|Criminal Code)\b", content, flags=re.IGNORECASE):
		sections = match.group(1)
		law = match.group(2)
		prefix = "irpr" if re.search(r"\bIRPR\b", law, flags=re.IGNORECASE) else "charter" if re.search(r"\bCharter\b", law, flags=re.IGNORECASE) else "criminal_code" if re.search(r"\bCriminal Code\b", law, flags=re.IGNORECASE) else "irpa"
		for section_match in re.finditer(r"\d{1,3}[A-Za-z]?(?:\s*\(\s*[A-Za-z0-9]+\s*\))*", sections):
			section = _normalize_whitespace(section_match.group(0))
			add_section_tag(f"{prefix}_s_{section}", content[max(0, match.start() - 80): min(len(content), match.end() + 80)].strip())
		if len(section_hits) >= 20:
			break

	for section, evidence in section_hits.items():
		tags.append(
			CaseReaderTagResponse(
				category="statute_section",
				value=section,
				score=0.85,
				evidence=evidence,
				source="reader_keyword",
				taxonomy_version="reader_v1",
			)
		)

	return tags


def _build_reader_extracted_metadata(case: Case, chunks: list[CaseChunk]) -> list[CaseReaderMetadataFieldResponse]:
	text_parts: list[str] = []
	if case.full_text:
		text_parts.append(case.full_text)
	if case.summary:
		text_parts.append(case.summary)
	for chunk in chunks[:2]:
		if chunk.text:
			text_parts.append(chunk.text)
	content = "\n".join(text_parts)

	rows: list[CaseReaderMetadataFieldResponse] = []
	seen: set[tuple[str, str]] = set()

	def add_row(key: str, value: str | None, evidence: str | None = None, source: str = "reader_extracted") -> None:
		if value is None:
			return
		clean = _normalize_whitespace(value)
		if not clean:
			return
		pair = (key, clean)
		if pair in seen:
			return
		seen.add(pair)
		rows.append(CaseReaderMetadataFieldResponse(key=key, value=clean, source=source, evidence=evidence))

	add_row("decision_date", str(case.date), source="canonical_case")
	if hasattr(case.date, "day") and hasattr(case.date, "strftime"):
		add_row("decision_date_written", f"{case.date.strftime('%B')} {case.date.day}, {case.date.strftime('%Y')}", source="canonical_case")

	for match in re.finditer(r"\bIMM[- ]?\d{1,6}-\d{2}\b", content, flags=re.IGNORECASE):
		add_row("imm_number", match.group(0).upper().replace(" ", "-"), evidence=match.group(0))

	match = re.search(r"\b([A-Z][a-z]+,\s+[A-Z][A-Za-z ]+),\s+[A-Z][a-z]+\s+\d{1,2},\s+\d{4}\b", content)
	if match is not None:
		add_row("location", match.group(1), evidence=match.group(0))

	match = re.search(
		r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(?:19|20)\d{2}\b",
		content,
		flags=re.IGNORECASE,
	)
	if match is not None:
		add_row("decision_date_written", match.group(0), evidence=match.group(0))

	match = re.search(r"\bDate\s*[:\-]?\s*((?:19|20)\d{2}[-/](?:0[1-9]|1[0-2])[-/](?:0[1-9]|[12]\d|3[01]))", content, flags=re.IGNORECASE)
	if match is not None:
		add_row("decision_date_text", match.group(1).replace("/", "-"), evidence=match.group(0))

	match = re.search(r"(The\s+Honourable[^\n\r]{0,100}?Justice\s+[A-Z][A-Za-z'\-]+)", content, flags=re.IGNORECASE)
	if match is not None:
		add_row("judge", match.group(1), evidence=match.group(0))

	match = re.search(r"\bApplicants\s+and\s+(.{8,180}?)\s+Respondent\b", content, flags=re.IGNORECASE | re.DOTALL)
	if match is None:
		match = re.search(r"\band\s+(.{8,180}?)\s+Respondent\b", content, flags=re.IGNORECASE | re.DOTALL)
	if match is not None:
		candidate = _normalize_whitespace(match.group(1))
		candidate = re.sub(r"^[^A-Za-z]+", "", candidate)
		candidate = re.sub(r"[^A-Za-z)\]'.\- ]+$", "", candidate)
		if candidate.isupper():
			candidate = candidate.title()
		add_row("respondent", candidate, evidence=_normalize_whitespace(match.group(0)))

	minister_match = re.search(
		r"\bThe\s+Minister\s+of\s+Citizenship\s+and\s+Immigration\b",
		content,
		flags=re.IGNORECASE,
	)
	if minister_match is not None:
		add_row(
			"respondent",
			"The Minister of Citizenship and Immigration",
			evidence=minister_match.group(0),
		)

	match = re.search(r"\bcitizens\s+of\s+([A-Z][A-Za-z'\- ]{2,60})\b", content, flags=re.IGNORECASE)
	if match is not None:
		add_row("country", match.group(1).title(), evidence=match.group(0))

	preferred_order = {"imm_number": 0, "decision_date": 1, "decision_date_written": 2, "decision_date_text": 3, "location": 4, "judge": 5, "respondent": 6, "country": 7}
	return sorted(rows, key=lambda row: (preferred_order.get(row.key, 99), row.key, row.value))


def _party_filter_terms(filters: list[str]) -> list[str]:
	aliases = {
		"Minister": [
			"Minister",
			"MPSEP",
			"Minister of Public Safety",
			"Minister of Public Safety and Emergency Preparedness",
		],
		"IRCC": [
			"IRCC",
			"Immigration, Refugees and Citizenship Canada",
			"Citizenship and Immigration Canada",
		],
		"CBSA": [
			"CBSA",
			"Canada Border Services Agency",
			"Border Services Agency",
		],
	}

	terms: list[str] = []
	seen: set[str] = set()
	for filter_name in filters:
		for term in aliases.get(filter_name, [filter_name]):
			normalized = term.strip()
			if normalized and normalized.lower() not in seen:
				seen.add(normalized.lower())
				terms.append(normalized)
	return terms


def _apply_case_filters(statement: Select, search: CaseSearchRequest) -> Select:
	if search.title_contains:
		statement = statement.where(Case.title.ilike(f"%{search.title_contains}%"))
	if search.court:
		statement = statement.where(Case.court == search.court)
	if search.jurisdiction:
		statement = statement.where(Case.jurisdiction == search.jurisdiction)
	if search.source_name_contains:
		statement = statement.where(Case.source_name.ilike(f"%{search.source_name_contains}%"))
	if search.source_url_contains:
		statement = statement.where(Case.source_url.ilike(f"%{search.source_url_contains}%"))
	if search.source_id_contains:
		statement = statement.where(Case.source_id.ilike(f"%{search.source_id_contains}%"))
	if search.dataset_version_contains:
		statement = statement.where(Case.dataset_version.ilike(f"%{search.dataset_version_contains}%"))
	if search.upstream_license_contains:
		statement = statement.where(Case.upstream_license.ilike(f"%{search.upstream_license_contains}%"))
	if search.secondary_citation_contains:
		statement = statement.where(Case.secondary_citation.ilike(f"%{search.secondary_citation_contains}%"))
	if search.party_filters:
		searchable_document = _case_search_document()
		party_terms = _party_filter_terms([party for party in search.party_filters if party])
		party_clauses = [searchable_document.ilike(f"%{party}%") for party in party_terms]
		if party_clauses:
			statement = statement.where(or_(*party_clauses))
	if search.source_type:
		statement = statement.where(Case.source_type == search.source_type)
	if search.language:
		statement = statement.where(Case.language == search.language)
	if search.processing_status:
		statement = statement.where(Case.processing_status == search.processing_status)
	for tag_filter in search.tag_filters or []:
		category, _, value = tag_filter.partition(":")
		statement = statement.where(
			select(CaseTag.id)
			.where(
				CaseTag.case_id == Case.id,
				CaseTag.category == category.strip(),
				CaseTag.value == value.strip(),
			)
			.exists()
		)
	if search.date_from:
		statement = statement.where(Case.date >= search.date_from)
	if search.date_to:
		statement = statement.where(Case.date <= search.date_to)
	if search.scraped_from:
		statement = statement.where(func.date(Case.scraped_at) >= search.scraped_from)
	if search.scraped_to:
		statement = statement.where(func.date(Case.scraped_at) <= search.scraped_to)
	if search.citing_cases_min is not None:
		statement = statement.where(func.coalesce(Case.citing_cases_count, 0) >= search.citing_cases_min)
	if search.citing_cases_max is not None:
		statement = statement.where(func.coalesce(Case.citing_cases_count, 0) <= search.citing_cases_max)
	if search.cited_case:
		cited_case_text = func.coalesce(func.cast(Case.cases_cited, Text), "")
		statement = statement.where(cited_case_text.ilike(f"%{search.cited_case}%"))
	if search.citation_contains:
		needle = f"%{search.citation_contains}%"
		statement = statement.where(
			or_(
				Case.citation.ilike(needle),
				Case.secondary_citation.ilike(needle),
			)
		)
	if search.cases_cited_contains:
		cited_text = func.coalesce(func.cast(Case.cases_cited, Text), "")
		statement = statement.where(cited_text.ilike(f"%{search.cases_cited_contains}%"))
	if search.cases_citing_contains:
		citing_text = func.coalesce(func.cast(Case.cases_citing, Text), "")
		statement = statement.where(citing_text.ilike(f"%{search.cases_citing_contains}%"))
	return statement


def _validate_search_ranges(search: CaseSearchRequest) -> None:
	if search.date_from and search.date_to and search.date_from > search.date_to:
		raise HTTPException(status_code=422, detail="date_from must be on or before date_to")
	if search.scraped_from and search.scraped_to and search.scraped_from > search.scraped_to:
		raise HTTPException(status_code=422, detail="scraped_from must be on or before scraped_to")
	if (
		search.citing_cases_min is not None
		and search.citing_cases_max is not None
		and search.citing_cases_min > search.citing_cases_max
	):
		raise HTTPException(status_code=422, detail="citing_cases_min must be less than or equal to citing_cases_max")


def _case_search_document() -> Any:
	return func.concat_ws(
		" ",
		func.coalesce(Case.title, ""),
		func.coalesce(Case.citation, ""),
		func.coalesce(Case.secondary_citation, ""),
		func.coalesce(Case.source_name, ""),
		func.coalesce(Case.source_id, ""),
		func.coalesce(Case.court, ""),
		func.coalesce(Case.jurisdiction, ""),
		func.coalesce(Case.summary, ""),
		func.coalesce(Case.full_text, ""),
		func.coalesce(func.cast(Case.cases_cited, Text), ""),
		func.coalesce(func.cast(Case.cases_citing, Text), ""),
		func.coalesce(func.cast(Case.metadata_json, Text), ""),
	)


def _case_match_source(case: Case, query: str, search_mode: str) -> str:
	query_text = " ".join(query.lower().split())
	if not query_text:
		return "Metadata" if search_mode == "metadata" else "Mixed"

	metadata_parts = [
		getattr(case, "title", None),
		getattr(case, "citation", None),
		getattr(case, "secondary_citation", None),
		getattr(case, "source_name", None),
		getattr(case, "source_id", None),
		getattr(case, "court", None),
		getattr(case, "jurisdiction", None),
		str(getattr(case, "metadata_json", None) or ""),
		str(getattr(case, "cases_cited", None) or ""),
		str(getattr(case, "cases_citing", None) or ""),
	]
	metadata_text = " ".join(part for part in metadata_parts if part).lower()
	body_text = f"{getattr(case, 'summary', '') or ''} {getattr(case, 'full_text', '') or ''}".lower()

	metadata_hits = sum(1 for token in query_text.split() if token in metadata_text)
	body_hits = sum(1 for token in query_text.split() if token in body_text)
	if metadata_hits > body_hits:
		return "Metadata"
	if body_hits > metadata_hits:
		return "Full text"
	if search_mode == "metadata":
		return "Metadata"
	if search_mode == "semantic":
		return "Full text"
	return "Mixed"


def _chunk_search_document() -> Any:
	return func.concat_ws(
		" ",
		func.coalesce(Case.title, ""),
		func.coalesce(Case.citation, ""),
		func.coalesce(Case.secondary_citation, ""),
		func.coalesce(Case.source_name, ""),
		func.coalesce(Case.source_id, ""),
		func.coalesce(Case.court, ""),
		func.coalesce(Case.jurisdiction, ""),
		func.coalesce(Case.summary, ""),
		func.coalesce(Case.full_text, ""),
		func.coalesce(func.cast(Case.cases_cited, Text), ""),
		func.coalesce(func.cast(Case.cases_citing, Text), ""),
		func.coalesce(func.cast(Case.metadata_json, Text), ""),
		func.coalesce(CaseChunk.text, ""),
	)


def _case_lexical_rank_expr(query: str):
	# Prefer structured metadata first, then summaries/full text, using the simple parser for identifiers.
	document = _case_search_document()
	return func.ts_rank_cd(func.to_tsvector("simple", document), func.plainto_tsquery("simple", query))


def _chunk_lexical_rank_expr(query: str):
	document = _chunk_search_document()
	return func.ts_rank_cd(func.to_tsvector("simple", document), func.plainto_tsquery("simple", query))


def _build_case_source(case_data: CaseIngestRequest, case_id: int, *, is_primary: bool = True) -> CaseSource:
	return CaseSource(
		case_id=case_id,
		source_type=(case_data.source_type or "unknown").strip() or "unknown",
		source_name=case_data.source_name,
		source_id=case_data.source_id,
		source_url=case_data.source_url,
		dataset_version=case_data.dataset_version,
		upstream_license=case_data.upstream_license,
		scraped_at=case_data.scraped_at,
		is_primary=is_primary,
		metadata_json=case_data.metadata_json or None,
	)


def _build_ingestion_run(case_data: CaseIngestRequest, *, records_seen: int = 1, records_ingested: int = 1) -> IngestionRun:
	return IngestionRun(
		source_type=(case_data.source_type or "unknown").strip() or "unknown",
		source_name=case_data.source_name,
		run_type="single_ingest",
		status="completed",
		records_seen=records_seen,
		records_ingested=records_ingested,
		records_updated=0,
		records_failed=0,
		metadata_json={
			"court": case_data.court,
			"citation": case_data.citation,
			"source_id": case_data.source_id,
		},
	)


@router.post("/ingest", response_model=CaseResponse, status_code=status.HTTP_201_CREATED)
def ingest_case(case_data: CaseIngestRequest, db: Session = Depends(get_db)) -> Case:
	metadata: dict[str, Any] = dict(case_data.metadata_json or {})
	extracted_citations = _extract_legal_citations(case_data.full_text or case_data.summary)
	if extracted_citations:
		metadata["extracted_citations"] = extracted_citations

	case = Case(
		title=case_data.title,
		court=case_data.court,
		jurisdiction=case_data.jurisdiction,
		date=case_data.date,
		citation=case_data.citation,
		docket_number=case_data.docket_number,
		summary=case_data.summary,
		full_text=case_data.full_text,
		issues=case_data.issues,
		metadata_json=metadata or None,
		source_url=case_data.source_url,
		source_name=case_data.source_name,
		secondary_citation=case_data.secondary_citation,
		source_id=case_data.source_id,
		source_type=case_data.source_type,
		dataset_version=case_data.dataset_version,
		upstream_license=case_data.upstream_license,
		scraped_at=case_data.scraped_at,
		language=case_data.language,
		full_text_hash=(sha256(case_data.full_text.encode("utf-8")).hexdigest() if case_data.full_text else None),
		processing_status=(
			"embedded" if (case_data.summary and AI_ROLLOUT["embed_on_ingest_enabled"]) else "raw"
		),
		cases_cited=case_data.cases_cited or (extracted_citations or None),
		cases_citing=case_data.cases_citing,
		citing_cases_count=case_data.citing_cases_count,
		embedding=(
			_embed(case_data.summary)
			if (case_data.summary and AI_ROLLOUT["embed_on_ingest_enabled"])
			else None
		),
	)
	db.add(case)
	try:
		db.commit()
	except Exception:
		db.rollback()
		raise
	db.refresh(case)

	source_row = _build_case_source(case_data, case.id)
	run_row = _build_ingestion_run(case_data)
	db.add(source_row)
	db.add(run_row)
	db.commit()
	db.refresh(source_row)
	db.refresh(run_row)
	return case


@router.post("/ingest/merge", response_model=CaseMergeResponse)
def merge_ingest_case(
	case_data: CaseIngestRequest,
	db: Session = Depends(get_db),
) -> CaseMergeResponse:
	if not case_data.cases_cited:
		extracted_citations = _extract_legal_citations(case_data.full_text or case_data.summary)
		if extracted_citations:
			case_data = case_data.model_copy(update={"cases_cited": extracted_citations})

	try:
		case, action, changed_fields = merge_case_record(db, case_data)
	except Exception:
		db.rollback()
		raise
	return CaseMergeResponse(
		action=action,
		changed_fields=sorted(changed_fields),
		case=CaseResponse.model_validate(case),
	)


@router.get("/inventory", response_model=InventoryResponse)
def get_inventory(db: Session = Depends(get_db)) -> InventoryResponse:
	total_cases = db.scalar(select(func.count(Case.id))) or 0
	total_sources = db.scalar(select(func.count(CaseSource.id))) or 0
	source_breakdown = [
		{"source_type": source_type or "unknown", "case_count": count}
		for source_type, count in db.execute(
			select(CaseSource.source_type, func.count(CaseSource.id))
			.group_by(CaseSource.source_type)
			.order_by(CaseSource.source_type)
		).all()
	]

	case_rows = db.execute(
		select(Case.id, Case.title, Case.court, Case.date, Case.citation, Case.source_type, Case.source_name, Case.source_id)
		.order_by(Case.id)
	).all()
	cases: list[dict[str, Any]] = []
	for case_id, title, court, decision_date, citation, source_type, source_name, source_id in case_rows:
		sources = db.scalars(
			select(CaseSource)
			.where(CaseSource.case_id == case_id)
			.order_by(CaseSource.is_primary.desc(), CaseSource.created_at.asc(), CaseSource.id.asc())
		).all()
		cases.append(
			{
				"id": case_id,
				"title": title,
				"court": court,
				"date": decision_date,
				"citation": citation,
				"source_type": source_type,
				"source_name": source_name,
				"source_id": source_id,
				"source_count": len(sources),
				"sources": [
					{
						"id": source_row.id,
						"source_type": source_row.source_type,
						"source_name": source_row.source_name,
						"source_id": source_row.source_id,
						"source_url": source_row.source_url,
						"dataset_version": source_row.dataset_version,
						"upstream_license": source_row.upstream_license,
						"scraped_at": source_row.scraped_at,
						"is_primary": source_row.is_primary,
						"metadata_json": source_row.metadata_json,
						"created_at": source_row.created_at,
					}
					for source_row in sources
				],
			}
		)

	return InventoryResponse(
		total_cases=int(total_cases),
		total_sources=int(total_sources),
		source_breakdown=[InventorySourceSummary.model_validate(item) for item in source_breakdown],
		cases=[InventoryCaseResponse.model_validate(item) for item in cases],
	)


@router.get("/cases/{case_id}", response_model=CaseResponse)
def get_case(case_id: int, db: Session = Depends(get_db)) -> Case:
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	return case


@router.get("/cases/{case_id}/activity", response_model=dict[str, Any], include_in_schema=False)
def get_case_activity(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)
	metadata_text = str(case.metadata_json or {})
	imm_numbers = sorted(
		{
			match.upper().replace(" ", "-")
			for match in re.findall(r"IMM[- ]\d{1,6}[- ]\d{2,4}", " ".join((case.docket_number or "", case.source_id or "", metadata_text)), re.IGNORECASE)
		}
	)
	procedural_rows = list(
		db.scalars(
			select(FCProceduralHistory)
			.where(FCProceduralHistory.imm_number.in_(imm_numbers))
			.order_by(FCProceduralHistory.latest_activity_date.desc().nullslast(), FCProceduralHistory.imm_number)
		)
	) if imm_numbers else []
	activity_cases = list(
		db.scalars(
			select(FCActivityCase)
			.where(FCActivityCase.citation.in_(imm_numbers))
			.order_by(FCActivityCase.date_filed.desc().nullslast(), FCActivityCase.id)
		)
	) if imm_numbers else []
	activity_case_ids = [row.id for row in activity_cases]
	documents = list(
		db.scalars(
			select(FCActivityDocument)
			.where(FCActivityDocument.case_id.in_(activity_case_ids))
			.order_by(FCActivityDocument.doc_dt.desc().nullslast(), FCActivityDocument.id)
		)
	) if activity_case_ids else []
	documents_by_case: dict[int, list[dict[str, Any]]] = {}
	for document in documents:
		documents_by_case.setdefault(document.case_id, []).append({
			"id": document.id,
			"re_no": document.re_no,
			"docno": document.docno,
			"doc_dt": document.doc_dt,
			"recorded_entry": document.recorded_entry,
		})
	return {
		"case_id": case_id,
		"imm_numbers": imm_numbers,
		"procedural_history": [
			{
				"imm_number": row.imm_number,
				"style_of_cause": row.style_of_cause,
				"judge": row.judge,
				"leave_decision": row.leave_decision,
				"leave_date": row.leave_date,
				"jr_decision": row.jr_decision,
				"jr_decision_date": row.jr_decision_date,
				"case_status": row.case_status,
				"latest_activity_date": row.latest_activity_date,
				"entries": row.entries_json or [],
			}
			for row in procedural_rows
		],
		"activity_cases": [
			{
				"id": row.id,
				"citation": row.citation,
				"year": row.year,
				"case_name": row.case_name,
				"date_filed": row.date_filed,
				"city_filed": row.city_filed,
				"nature": row.nature,
				"case_class": row.case_class,
				"track": row.track,
				"source_url": row.source_url,
				"documents": documents_by_case.get(row.id, []),
			}
			for row in activity_cases
		],
	}


@router.get("/cases/{case_id}/reader-data", response_model=CaseReaderDataResponse)
def get_case_reader_data(case_id: int, db: Session = Depends(get_db)) -> CaseReaderDataResponse:
	case = _get_case_or_404(case_id, db)

	sources = list(
		db.scalars(
			select(CaseSource)
			.where(CaseSource.case_id == case_id)
			.order_by(CaseSource.is_primary.desc(), CaseSource.id)
		)
	)
	chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(CaseChunk.case_id == case_id, CaseChunk.chunk_set.in_(["paragraph", "section", "legacy"]))
			.order_by(CaseChunk.chunk_index)
		)
	)
	if any((chunk.chunk_set or "") == "paragraph" for chunk in chunks):
		chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "paragraph"]
	elif chunks:
		if any((chunk.chunk_set or "") == "section" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "section"]
		elif any((chunk.chunk_set or "") == "legacy" for chunk in chunks):
			chunks = [chunk for chunk in chunks if (chunk.chunk_set or "") == "legacy"]
	tags = list(
		db.scalars(
			select(CaseTag)
			.where(CaseTag.case_id == case_id)
			.order_by(CaseTag.category, CaseTag.value)
		)
	)
	inferred_tags = _build_reader_inferred_tags(case, chunks)
	extracted_metadata = _build_reader_extracted_metadata(case, chunks)

	target_case = Case.__table__.alias("target_case")
	citation_rows = db.execute(
		select(
			Citation,
			target_case.c.id,
			target_case.c.title,
			target_case.c.citation,
		)
		.outerjoin(target_case, target_case.c.id == Citation.target_case_id)
		.where(Citation.source_case_id == case_id)
		.order_by(Citation.chunk_id, Citation.offset_start, Citation.id)
	)

	citation_responses = [
		CaseReaderCitationResponse(
			id=citation.id,
			citation_kind=citation.citation_kind,
			chunk_id=citation.chunk_id,
			offset_start=citation.offset_start,
			offset_end=citation.offset_end,
			citation_text=citation.citation_text,
			normalized_citation=citation.normalized_citation,
			target_case_id=target_case_id,
			target_title=target_title,
			target_citation=target_citation,
			provenance=citation.provenance,
			unresolved=citation.unresolved,
		)
		for citation, target_case_id, target_title, target_citation in citation_rows
	]
	citation_responses = [
		row
		for row in citation_responses
		if not is_self_case_name_match(
			case.title,
			RawCitationMatch(
				kind=row.citation_kind,
				citation_text=row.citation_text or "",
				normalized_citation=row.normalized_citation or "",
				offset_start=row.offset_start or 0,
				offset_end=row.offset_end or 0,
			),
		)
	]

	statute_rows = list(
		db.scalars(
			select(StatuteReference)
			.where(StatuteReference.source_case_id == case_id)
			.order_by(StatuteReference.chunk_id, StatuteReference.offset_start, StatuteReference.id)
		)
	)
	statute_responses = [
		CaseReaderCitationResponse(
			id=-1000000 - reference.id,
			citation_kind=reference.reference_kind,
			chunk_id=reference.chunk_id,
			offset_start=reference.offset_start,
			offset_end=reference.offset_end,
			citation_text=reference.reference_text,
			normalized_citation=reference.normalized_reference,
			provenance="statute_references",
			unresolved=False,
		)
		for reference in statute_rows
		if _is_irpa_irpr_reference(reference.reference_text)
		or _is_irpa_irpr_reference(reference.normalized_reference)
	]
	citation_responses.extend(statute_responses)

	selected_chunk_ids = {chunk.id for chunk in chunks if chunk.id is not None}
	if selected_chunk_ids:
		citation_responses = [
			row
			for row in citation_responses
			if row.chunk_id is None or row.chunk_id in selected_chunk_ids
		]

	has_statute_like = any(
		_is_statute_like_label(row.target_citation)
		or _is_statute_like_label(row.normalized_citation)
		or _is_statute_like_label(row.citation_text)
		for row in citation_responses
	)

	chunk_ids_with_rows = {row.chunk_id for row in citation_responses if row.chunk_id in selected_chunk_ids}
	if selected_chunk_ids:
		seen_live: set[tuple[int, int, int, str]] = set()
		for row in citation_responses:
			if row.chunk_id is None or row.offset_start is None or row.offset_end is None:
				continue
			seen_live.add(
				(
					row.chunk_id,
					int(row.offset_start),
					int(row.offset_end),
					str(row.normalized_citation or row.citation_text or "").strip().lower(),
				)
			)

		next_live_id = -1
		process_all_chunks = (not chunk_ids_with_rows) or (not has_statute_like)
		for chunk in chunks:
			if chunk.id is None:
				continue
			if not process_all_chunks and chunk.id in chunk_ids_with_rows:
				# Existing rows are present for this chunk, but we still run extraction
				# and only append rows that are truly missing from payload spans.
				pass
			chunk_text = chunk.text or ""
			if not chunk_text.strip():
				continue
			for raw in extract_raw_citation_matches(chunk_text):
				if raw.kind not in {"case", "case_short", "case_name", "neutral"}:
					continue
				if is_self_case_name_match(case.title, raw):
					continue
				normalized_key = str(raw.normalized_citation or raw.citation_text or "").strip().lower()
				key = (chunk.id, raw.offset_start, raw.offset_end, normalized_key)
				if key in seen_live:
					continue
				seen_live.add(key)
				citation_responses.append(
					CaseReaderCitationResponse(
						id=next_live_id,
						citation_kind=raw.kind,
						chunk_id=chunk.id,
						offset_start=raw.offset_start,
						offset_end=raw.offset_end,
						citation_text=raw.citation_text,
						normalized_citation=raw.normalized_citation,
						target_case_id=None,
						target_title=None,
						target_citation=None,
						provenance="reader_live_extract",
						unresolved=True,
					)
				)
				next_live_id -= 1
			for raw in extract_statute_reference_matches(chunk_text):
				if not _is_irpa_irpr_reference(raw.citation_text) and not _is_irpa_irpr_reference(raw.normalized_citation):
					continue
				normalized_key = str(raw.normalized_citation or raw.citation_text or "").strip().lower()
				key = (chunk.id, raw.offset_start, raw.offset_end, normalized_key)
				if key in seen_live:
					continue
				seen_live.add(key)
				citation_responses.append(
					CaseReaderCitationResponse(
						id=next_live_id,
						citation_kind=raw.kind,
						chunk_id=chunk.id,
						offset_start=raw.offset_start,
						offset_end=raw.offset_end,
						citation_text=raw.citation_text,
						normalized_citation=raw.normalized_citation,
						provenance="reader_live_statute_extract",
						unresolved=False,
					)
				)
				next_live_id -= 1

	metrics = db.scalar(select(CitationMetrics).where(CitationMetrics.case_id == case_id))

	return CaseReaderDataResponse(
		case=CaseResponse.model_validate(case, from_attributes=True),
		sources=[CaseSourceResponse.model_validate(row, from_attributes=True) for row in sources],
		chunks=[
			CaseReaderChunkResponse(
				id=chunk.id,
				chunk_set=chunk.chunk_set,
				chunk_index=chunk.chunk_index,
				chunk_label=chunk.chunk_label,
				paragraph_start=chunk.paragraph_start,
				paragraph_end=chunk.paragraph_end,
				text=chunk.text or "",
				text_length=len(chunk.text or ""),
				token_estimate=int(chunk.token_estimate or 0),
				created_at=chunk.created_at,
			)
			for chunk in chunks
		],
		citations=citation_responses,
		tags=[CaseReaderTagResponse.model_validate(tag, from_attributes=True) for tag in tags] + inferred_tags,
		extracted_metadata=extracted_metadata,
		metrics=CitationMetricsResponse.model_validate(metrics, from_attributes=True) if metrics is not None else None,
	)


def _get_case_or_404(case_id: int, db: Session) -> Case:
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	return case


@router.get("/cases/{case_id}/citations/outgoing", response_model=list[CitationResponse])
def get_case_outgoing_citations(case_id: int, db: Session = Depends(get_db)) -> list[CitationResponse]:
	_get_case_or_404(case_id, db)
	rows = list(
		db.execute(
			select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id)
		)
	)
	return [CitationResponse.model_validate(citation, from_attributes=True) for citation, in rows]


@router.get("/cases/{case_id}/citations/incoming", response_model=list[CitationResponse])
def get_case_incoming_citations(case_id: int, db: Session = Depends(get_db)) -> list[CitationResponse]:
	_get_case_or_404(case_id, db)
	rows = list(
		db.execute(
			select(Citation).where(Citation.target_case_id == case_id).order_by(Citation.id)
		)
	)
	return [CitationResponse.model_validate(citation, from_attributes=True) for citation, in rows]


@router.get("/cases/{case_id}/citations/passages", response_model=list[CitationResponse])
def get_case_citation_passages(case_id: int, db: Session = Depends(get_db)) -> list[CitationResponse]:
	_get_case_or_404(case_id, db)
	rows = list(
		db.execute(
			select(Citation).where(Citation.source_case_id == case_id, Citation.chunk_id.is_not(None)).order_by(Citation.chunk_id, Citation.offset_start)
		)
	)
	return [CitationResponse.model_validate(citation, from_attributes=True) for citation, in rows]


@router.get("/cases/{case_id}/citation-metrics", response_model=CitationMetricsResponse)
def get_case_citation_metrics(case_id: int, db: Session = Depends(get_db)) -> CitationMetricsResponse:
	_get_case_or_404(case_id, db)
	metrics = db.scalar(select(CitationMetrics).where(CitationMetrics.case_id == case_id))
	if metrics is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Citation metrics not found")
	return CitationMetricsResponse.model_validate(metrics, from_attributes=True)


@router.post("/citation-metrics/recompute", response_model=dict[str, int])
def recompute_citation_metrics(db: Session = Depends(get_db)) -> dict[str, int]:
	updated = _compute_citation_metrics(db)
	return {"cases_updated": updated}


@router.get("/citation-map/summary", response_model=CitationMapSummaryResponse)
def get_citation_map_summary(db: Session = Depends(get_db)) -> dict[str, int]:
	return _citation_map_summary(db)


@router.get("/citation-map", response_class=HTMLResponse)
def citation_map_page() -> str:
	return citation_map_html()


@router.get("/case-reader", response_class=HTMLResponse)
def case_reader_page() -> str:
	return case_reader_html()


@router.get("/case-reader/cases", response_model=list[dict[str, Any]], include_in_schema=False)
def case_reader_cases(limit: int = 300, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	rows = db.scalars(
		select(Case)
		.where(Case.title.is_not(None))
		.order_by(Case.date.desc().nullslast(), Case.id.desc())
		.limit(max(1, min(500, limit)))
	)
	return [
		{
			"case_id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
		}
		for case in rows
	]


def _judge_outcomes_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Judge Outcomes | AI CaseLibrary</title>
	<style>
		:root{--ink:#14212b;--muted:#63707a;--paper:#f6f4ee;--panel:#fffdfa;--line:#d9d5ca;--gov:#285d75;--ind:#b65a34;--unknown:#b8b3a8;}
		*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif}.shell{max-width:1280px;margin:auto;padding:32px 24px 56px}.masthead{display:flex;justify-content:space-between;gap:24px;align-items:end;border-bottom:3px solid var(--ink);padding-bottom:20px}.eyebrow{font:700 12px/1.2 Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:var(--gov)}h1{font-size:34px;font-weight:normal;margin:7px 0 0;letter-spacing:0}.subhead{max-width:620px;margin:0;color:var(--muted);font-size:16px;line-height:1.45}.summary{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-bottom:1px solid var(--line);margin:25px 0 18px}.metric{padding:13px 16px 14px 0}.metric+.metric{border-left:1px solid var(--line);padding-left:16px}.metric small{display:block;font:700 11px Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}.metric strong{font-size:27px;font-weight:normal}.legend{display:flex;gap:16px;align-items:center;font:12px Arial,sans-serif;color:var(--muted);margin:12px 0}.key{display:inline-flex;align-items:center;gap:6px}.dot{width:10px;height:10px;display:inline-block}.table-wrap{overflow:auto;background:var(--panel);border:1px solid var(--line)}table{border-collapse:collapse;width:100%;min-width:820px}th{text-align:left;padding:12px 10px;font:700 11px Arial,sans-serif;letter-spacing:.7px;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);white-space:nowrap}td{padding:13px 10px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:middle}.rank{font:700 13px Arial,sans-serif;color:var(--muted)}.judge{min-width:250px}.count{font-variant-numeric:tabular-nums;text-align:right}.bar{height:13px;display:flex;min-width:180px;background:#eeeae1}.gov{background:var(--gov)}.individual{background:var(--ind)}.unknown{background:var(--unknown)}.rate{font:700 13px Arial,sans-serif}.note{color:var(--muted);font-size:13px;line-height:1.45;margin:16px 0 0}.empty{padding:30px;color:var(--muted)}@media(max-width:680px){.shell{padding:22px 14px}.masthead{display:block}.subhead{margin-top:15px}.summary{grid-template-columns:1fr}.metric+.metric{border-left:0;border-top:1px solid var(--line);padding-left:0}h1{font-size:29px}}
	</style>
</head>
<body>
	<main class="shell">
		<header class="masthead"><div><div class="eyebrow">Decision Analytics</div><h1>How Top Judges Rule</h1></div><p class="subhead">The 50 judges with the most decisions, showing outcomes where the government and individual sides can be determined from the decision record.</p></header>
		<section class="summary" id="summary"><div class="metric"><small>Loading</small><strong>...</strong></div></section>
		<div class="legend"><span class="key"><i class="dot" style="background:var(--gov)"></i>Government wins</span><span class="key"><i class="dot" style="background:var(--ind)"></i>Individual wins</span><span class="key"><i class="dot" style="background:var(--unknown)"></i>Unclassified</span></div>
		<div class="table-wrap"><table><thead><tr><th>#</th><th>Judge</th><th>Decisions</th><th>Outcome split</th><th>Government wins</th><th>Individual wins</th><th>Unclassified</th><th>Gov. win rate</th></tr></thead><tbody id="rows"><tr><td colspan="8" class="empty">Loading analytics...</td></tr></tbody></table></div>
		<p class="note">Win rate uses only classified decisions. Unclassified decisions are included in the decision total but excluded from the rate.</p>
	</main>
	<script>
		const number=value=>new Intl.NumberFormat().format(Number(value||0));
		const escape=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
		function metric(label,value){return `<div class="metric"><small>${escape(label)}</small><strong>${escape(value)}</strong></div>`;}
		function row(item,index){const classified=item.government_wins+item.individual_wins;const govWidth=classified?item.government_wins/classified*100:0;const individualWidth=classified?item.individual_wins/classified*100:0;const unknownWidth=item.decisions?item.unclassified/item.decisions*100:0;const rate=classified?`${(govWidth).toFixed(1)}%`:'--';return `<tr><td class="rank">${index+1}</td><td class="judge">${escape(item.judge)}</td><td class="count">${number(item.decisions)}</td><td><div class="bar" title="Government: ${number(item.government_wins)} | Individual: ${number(item.individual_wins)} | Unclassified: ${number(item.unclassified)}"><span class="gov" style="width:${govWidth}%"></span><span class="individual" style="width:${individualWidth}%"></span><span class="unknown" style="width:${unknownWidth}%"></span></div></td><td class="count">${number(item.government_wins)}</td><td class="count">${number(item.individual_wins)}</td><td class="count">${number(item.unclassified)}</td><td class="rate">${rate}</td></tr>`;}
		async function load(){try{const response=await fetch('/analytics/judge-outcomes?limit=50');if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();document.getElementById('summary').innerHTML=metric('Judges ranked',data.judges.length)+metric('Decisions shown',number(data.totals.decisions))+metric('Classified outcomes',number(data.totals.classified));document.getElementById('rows').innerHTML=data.judges.map(row).join('')||'<tr><td colspan="8" class="empty">No judge outcome data is available.</td></tr>';}catch(error){document.getElementById('rows').innerHTML=`<tr><td colspan="8" class="empty">${escape(error.message)}</td></tr>`;}}
		load();
	</script>
</body>
</html>"""


@router.get("/judge-outcomes", response_class=HTMLResponse, include_in_schema=False)
def judge_outcomes_page() -> HTMLResponse:
	return HTMLResponse(content=_judge_outcomes_page_html(), status_code=status.HTTP_200_OK)


@router.get("/analytics/judge-outcomes", response_model=dict[str, Any])
def get_judge_outcomes(
	limit: int = 50,
	min_decisions: int = 0,
	db: Session = Depends(get_db),
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


_ANALYTICS_FIELDS = {
	"judge": ("Judge", "metadata_json->'reader_extracted'->>'judge'"),
	"court": ("Court", "court"),
	"decision_year": ("Decision year", "SUBSTRING(COALESCE(metadata_json->'reader_extracted'->>'date', '') FROM 1 FOR 4)"),
	"decision_outcome": ("Decision outcome", "metadata_json->'reader_extracted'->>'decision outcome'"),
	"government_role": ("Government role", "metadata_json->'reader_extracted'->>'government role'"),
	"government_outcome": ("Government outcome", "metadata_json->'reader_extracted'->>'government outcome'"),
}


def _data_explorer_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Immigration Litigation Intelligence Tool | iLIT</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
<style>
:root {
--bg: #f5f7fb;
--surface: #ffffff;
--surface-alt: #f1f5f9;
--border: #e2e8f0;
--text: #102038;
--muted: #5b6d83;
--muted-2: #8ca0b6;
--navy: #1e3a8a;
--blue: #2563eb;
--blue-soft: #dbeafe;
--green: #16a34a;
--green-soft: #dcfce7;
--amber: #f59e0b;
--amber-soft: #fef3c7;
--red: #dc2626;
--red-soft: #fee2e2;
--purple: #7c3aed;
--purple-soft: #ede9fe;
--shadow: 0 16px 40px rgba(15,23,42,0.06);
--shadow-soft: 0 8px 20px rgba(37,99,235,0.08);
}
*{box-sizing:border-box}html,body{margin:0;height:100%}body{background:var(--bg);color:var(--text);font-family:Inter,"Segoe UI",Arial,sans-serif;line-height:1.5}
button,input,select{font:inherit}
.app-shell{display:flex;flex-direction:column;min-height:100vh;background:var(--bg)}
.topbar{display:flex;align-items:center;height:64px;padding:0 28px;background:var(--surface);border-bottom:1px solid var(--border)}
.brand{display:flex;align-items:center;gap:12px}
.logo-mark{display:grid;place-items:center;width:36px;height:36px;border-radius:12px;background:linear-gradient(135deg,var(--navy),var(--blue));color:#fff;font-weight:800;font-size:16px;box-shadow:var(--shadow-soft);position:relative}
.logo-mark::after{content:"";position:absolute;top:6px;right:6px;width:9px;height:9px;border-radius:50%;background:#f5d88d;box-shadow:0 0 0 2px rgba(255,255,255,0.7)}
.brand-name{font-size:16px;font-weight:800;letter-spacing:-0.03em}.brand-sub{font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted)}
.global-search{justify-self:center;display:flex;align-items:center;gap:10px;max-width:560px;width:100%;padding:10px 14px;border:1px solid var(--border);border-radius:14px;background:var(--surface-alt)}
.global-search input{flex:1;border:0;outline:none;background:transparent;color:var(--text);font-size:14px}
.global-search input::placeholder{color:var(--muted-2)}
.header-actions{display:flex;align-items:center;justify-content:flex-end;gap:12px}
.icon-button{display:grid;place-items:center;width:34px;height:34px;border:1px solid var(--border);background:var(--surface);border-radius:10px;color:var(--muted);font-size:15px}
.user-pill{display:flex;align-items:center;gap:10px;padding:7px 10px 7px 7px;background:var(--surface);border:1px solid var(--border);border-radius:12px}
.avatar{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#dbeafe,#bfdbfe);color:var(--navy);font-size:12px;font-weight:700;border:1px solid rgba(37,99,235,0.15)}
.workspace{display:block;min-height:calc(100vh - 64px);flex:1 0 auto}
.sidebar{padding:16px 14px 12px;border-right:1px solid var(--border);background:rgba(255,255,255,0.5);overflow:auto}
.section-label{margin:14px 8px 8px;color:var(--muted-2);font-size:11px;letter-spacing:.12em;text-transform:uppercase;font-weight:700}
.nav-card{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:12px;margin-bottom:6px;color:var(--muted);font-size:14px;font-weight:600;transition:all .15s ease}
.nav-card:hover{background:var(--surface);border:1px solid var(--border);box-shadow:var(--shadow-soft)}
.nav-card.active{background:var(--blue-soft);color:var(--navy);border:1px solid rgba(37,99,235,0.18)}
.nav-icon{width:28px;height:28px;border-radius:10px;display:grid;place-items:center;border:1px solid var(--border);background:rgba(255,255,255,0.7);font-size:12px}
.quick-grid,.folder-list{display:grid;gap:8px;margin-top:8px}
.quick-card{display:flex;justify-content:space-between;align-items:center;padding:10px 10px 10px 12px;background:var(--surface);border:1px solid var(--border);border-radius:12px;box-shadow:var(--shadow)}
.quick-label{display:flex;flex-direction:column;gap:2px}.quick-label strong{font-size:13px;color:var(--text)}.quick-label span{font-size:11px;color:var(--muted-2)}
.badge-count{min-width:28px;height:22px;display:inline-flex;align-items:center;justify-content:center;padding:0 8px;border-radius:999px;background:var(--blue-soft);color:var(--navy);font-size:11px;font-weight:700}
.folder-item{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;border:1px solid var(--border);background:rgba(255,255,255,0.8);border-radius:10px;font-size:13px;color:var(--muted)}
.folder-item span{font-weight:600;color:var(--text)}
.folder-item small{color:var(--muted-2);font-size:11px}
.center-pane{display:flex;flex-direction:column;min-width:0;max-width:1200px;margin:0 auto;padding:32px 28px 48px;gap:16px;overflow:auto;
}
.page-header{padding:4px 4px 2px}
.eyebrow{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--navy);font-weight:700}
.page-header h1{margin:8px 0 0;font-size:28px;letter-spacing:-0.04em;font-weight:700}
.page-header p{margin:6px 0 0;color:var(--muted);font-size:13px}
.view-tabs{display:flex;gap:8px;margin-top:14px}
.tab{border:1px solid var(--border);border-radius:9px;background:var(--surface);color:var(--muted);padding:8px 12px;font-size:12px;font-weight:700;cursor:pointer}
.tab.active{background:var(--navy);border-color:var(--navy);color:#fff}
.panel-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;box-shadow:var(--shadow);overflow:hidden}
.search-layout{padding:14px 14px 12px}
.search-form{display:grid;grid-template-columns:repeat(4,minmax(180px,1fr));gap:12px}
.search-form .wide{grid-column:span 2}
.search-form label{display:block;margin-bottom:7px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:700}
.search-form input,.search-form select{width:100%;height:42px;padding:0 12px;border:1px solid var(--border);border-radius:10px;background:var(--surface);color:var(--text)}
.search-form input:focus,.search-form select:focus{outline:2px solid rgba(37,99,235,.12);border-color:var(--blue)}
.search-actions{display:flex;align-items:flex-end;gap:10px}.search-actions button{height:42px;padding:0 16px;border:0;border-radius:10px;background:var(--navy);color:#fff;font-weight:700;letter-spacing:.08em;text-transform:uppercase;cursor:pointer}.search-actions button.secondary{background:#eef2ff;color:var(--navy)}
.advanced-actions{grid-column:1/-1;display:flex;justify-content:flex-start;margin-top:12px}.advanced-search{grid-column:1/-1;margin-top:2px;padding:14px 0 2px;border-top:1px solid var(--border);min-width:0}.advanced-search[hidden]{display:none}.advanced-search::before{content:'Refine the result set';display:block;color:var(--text);font-size:12px;font-weight:700;letter-spacing:.04em}.advanced-search::after{content:'Use these filters to narrow by authority, outcome, court, judge, year, or full decision text.';display:block;margin-top:3px;color:var(--muted);font-size:11px}.advanced-search .search-form{grid-template-columns:repeat(3,minmax(0,1fr));margin-top:12px;min-width:0}.advanced-search .search-form>div,.advanced-search .check-field{min-width:0}.advanced-search input,.advanced-search select{min-width:0;max-width:100%}.check-field{display:flex;align-items:center;gap:8px;min-height:42px;color:var(--muted);font-size:12px;font-weight:600}.check-field input{width:16px;height:16px;accent-color:var(--blue)}
.search-meta{margin-top:12px;padding-top:10px;border-top:1px solid var(--border);color:var(--muted);font-size:12px}
.results-wrap{display:grid;gap:10px;margin-top:12px}
.case-result{display:block;width:100%;padding:14px 16px;background:var(--surface);border:1px solid var(--border);border-radius:14px;text-align:left;cursor:pointer;transition:all .15s ease}
.case-result:hover{border-color:var(--blue);background:linear-gradient(180deg,#ffffff 0%,#eff6ff 100%);box-shadow:var(--shadow-soft)}
.result-title{font-size:16px;font-weight:700;letter-spacing:-0.02em;color:var(--text)}
.result-meta{margin-top:6px;color:var(--muted);font-size:12px;line-height:1.6}
.result-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.tag{display:inline-flex;align-items:center;padding:5px 8px;border-radius:999px;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.tag.win{background:var(--green-soft);color:var(--green)}
.tag.loss{background:var(--red-soft);color:var(--red)}
.tag.neutral{background:var(--surface-alt);color:var(--muted)}
.summaryRows,.legend{display:flex;flex-wrap:wrap;gap:16px;padding:14px 16px 0;color:var(--muted);font-size:12px}
.summaryRows span strong{display:block;color:var(--text);font-size:20px;letter-spacing:-0.04em ;}
.legend .key{display:inline-flex;align-items:center;gap:6px}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%}
.table-wrap{overflow:auto;margin-top:12px;padding:0 10px 10px}
table{width:100%;border-collapse:collapse;min-width:720px}
thead th{padding:10px 12px;background:#f8fafc;border-bottom:1px solid var(--border);text-align:left;color:var(--muted);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
tbody td{padding:10px 12px;border-bottom:1px solid var(--border);font-size:13px;color:var(--text)}
tbody tr:hover{background:#fafcff}.number{text-align:right}.rank{color:var(--muted)}.group{font-weight:600}
.bar{display:flex;align-items:center;height:10px;border-radius:999px;overflow:hidden;background:#edf2f7;min-width:120px}
.bar span{display:block;height:100%}
.empty{padding:20px;color:var(--muted);font-size:14px}
.right-panel{display:flex;flex-direction:column;padding:18px 18px 12px 0;gap:12px;border-left:1px solid var(--border);background:rgba(255,255,255,0.32)}
.side-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}
.side-card .header{padding:12px 14px;border-bottom:1px solid var(--border);background:rgba(248,250,252,0.8);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:700}
.side-card .body{padding:12px 14px}
.tags-cloud{display:flex;flex-wrap:wrap;gap:8px}
.cloud-tag{display:inline-flex;align-items:center;padding:6px 10px;border-radius:999px;background:var(--surface-alt);border:1px solid var(--border);color:var(--muted);font-size:11px;font-weight:600}
.issue-row{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:8px 0;border-bottom:1px solid var(--border)}
.issue-row:last-child{border-bottom:0}
.issue-row small{display:block;color:var(--muted-2);font-size:10px;letter-spacing:.08em;text-transform:uppercase}
.score-badge{display:inline-flex;align-items:center;justify-content:center;padding:4px 8px;border-radius:999px;font-size:11px;font-weight:700}
.score-badge.red{background:var(--red-soft);color:var(--red)}
.score-badge.amber{background:var(--amber-soft);color:#b45309}
.score-badge.green{background:var(--green-soft);color:var(--green)}
.note-box{padding:10px 12px;border:1px solid var(--border);border-radius:10px;background:linear-gradient(180deg,#fff,#f8fafc);margin-bottom:10px}
.note-box:last-child{margin-bottom:0}
.note-box strong{display:block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.note-box span{display:block;color:var(--muted);font-size:12px;line-height:1.6}
.ci-header{padding:14px 16px 0}.ci-header h3{margin:0;color:var(--text);font-size:17px;letter-spacing:-.02em}.ci-header p{margin:4px 0 0;color:var(--muted);font-size:12px}.ci-table{margin-top:12px}.ci-evidence{padding:14px 16px;border-bottom:1px solid var(--border)}.ci-evidence:last-child{border-bottom:0}.ci-evidence h3{margin:0;color:var(--text);font-size:14px}.ci-evidence p{margin:7px 0 0;color:var(--muted);font-size:12px;line-height:1.55}.ci-quote{padding:10px 12px;border-left:3px solid var(--blue);background:var(--blue-soft);color:var(--text)!important;white-space:pre-wrap}.ci-pager{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:14px 16px}.ci-pager button{padding:7px 10px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text);font-size:12px;font-weight:700}.ci-pager button:disabled{opacity:.45;cursor:not-allowed}
.ci-chart{display:block;width:100%;height:auto;margin-top:12px;border-top:1px solid var(--border);border-bottom:1px solid var(--border);background:linear-gradient(180deg,#fff,#f8fafc)}.ci-chart-label{fill:var(--muted);font-size:11px}.ci-chart-grid{stroke:var(--border);stroke-width:1}.ci-chart-line{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:3}.ci-chart-dot{stroke:#fff;stroke-width:2}.ci-chart-legend{display:flex;gap:14px;padding:10px 16px 0;color:var(--muted);font-size:12px}.ci-chart-legend i{display:inline-block;width:10px;height:10px;margin-right:5px;border-radius:50%}
.fc-activity-block{margin-top:18px;padding-top:16px;border-top:1px solid var(--border)}.fc-activity-filter{grid-template-columns:minmax(220px,320px);margin:12px 16px 0}.fc-activity-block .ci-header{padding-top:0}.fc-activity-chart{padding:0 16px 16px}
.fc-activity-block .ci-chart-legend{flex-wrap:wrap;line-height:1.5}
@media(max-width:920px){.view-tabs{max-width:100%;overflow-x:auto;flex-wrap:nowrap;padding-bottom:2px}.view-tabs .tab{flex:0 0 auto}.about-dashboard{grid-template-columns:1fr}.about-coverage-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.about-coverage-row:nth-child(3n){border-right:1px solid var(--border)}.about-coverage-row:nth-child(2n){border-right:0}.about-status-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.about-story{display:grid;gap:0;margin-top:18px;border-top:1px solid var(--border)}.about-section{padding:20px 16px;border-bottom:1px solid var(--border)}.about-section:last-child{border-bottom:0}.about-section h3{margin:0;color:var(--text);font:600 21px/1.15 "Newsreader",serif}.about-section p{max-width:880px;margin:8px 0 0;color:var(--muted);font-size:13px;line-height:1.7}.about-kicker{margin-bottom:7px;color:var(--rust);font-size:10px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}.about-fields,.about-flow{display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin-top:13px}.about-fields span,.about-flow span{padding:6px 8px;border:1px solid var(--border);border-radius:4px;background:var(--surface-alt);color:var(--muted);font-size:11px;font-weight:600}.about-flow b{color:var(--rust);font-size:14px}.about-note{font-size:12px!important}.about-status-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:14px}.about-status-grid div{padding:11px 12px;border:1px solid var(--border);background:var(--surface-alt)}.about-status-grid strong{display:block;color:var(--text);font-size:18px}.about-status-grid span{display:block;margin-top:3px;color:var(--muted);font-size:11px;line-height:1.4}
.about-dashboard{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px}.about-dashboard-group{padding:12px;border:1px solid var(--border);background:var(--surface-alt)}.about-dashboard-label,.about-coverage-head span{color:var(--muted);font-size:10px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}.about-metric-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:10px}.about-metric-grid div{min-width:0}.about-metric-grid strong{display:block;color:var(--text);font-size:19px;line-height:1.1}.about-metric-grid span{display:block;margin-top:4px;color:var(--muted);font-size:10px;line-height:1.25}.about-coverage{margin-top:10px;border:1px solid var(--border)}.about-coverage-head{display:flex;justify-content:space-between;gap:12px;padding:11px 12px;border-bottom:1px solid var(--border);background:var(--surface-alt)}.about-coverage-head strong{font-size:12px}.about-coverage-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}.about-coverage-row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 8px;padding:10px 12px;border-bottom:1px solid var(--border);border-right:1px solid var(--border)}.about-coverage-row:nth-child(3n){border-right:0}.about-coverage-row strong{font-size:11px;color:var(--text)}.about-coverage-row span{grid-column:1;color:var(--muted-2);font:10px/1.2 "IBM Plex Mono",monospace}.about-coverage-row b{grid-column:2;grid-row:1 / span 2;align-self:center;color:var(--text);font-size:15px}.about-coverage-row em{grid-column:1;color:var(--green);font-size:9px;font-style:normal;text-transform:uppercase;letter-spacing:.05em}.about-coverage-row b:has(+ em){ }
.judge-profile-summary{padding:0 16px 16px}.judge-profile-summary .bar{margin:12px 0}.judge-profile-aliases{padding:0 16px 8px}.judge-profile-aliases .result-tags{margin-top:4px}.judge-decisions{padding:0 16px 16px}.judge-decisions h3{margin:16px 0 4px;font-size:16px;letter-spacing:-.02em}.judge-decisions p{margin:0;color:var(--muted);font-size:12px}.judge-open{padding:6px 9px;border:1px solid var(--border);border-radius:7px;background:var(--surface);color:var(--blue);font-size:11px;font-weight:700;cursor:pointer}
.bottom-tray{display:grid;grid-template-columns:repeat(5,minmax(180px,1fr));gap:12px;padding:12px 16px 16px;border-top:1px solid var(--border);background:rgba(255,255,255,0.72)}
.tray-panel{display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--border);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}
.tray-head{padding:10px 12px;border-bottom:1px solid var(--border);background:rgba(248,250,252,0.8);font-size:11px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--muted)}
.tray-body{padding:10px 12px 12px;display:flex;flex-direction:column;gap:8px;overflow:auto}
.excerpt-card{padding:10px;border-radius:10px;border:1px solid var(--border);background:linear-gradient(180deg,#fff,#f8fafc)}
.excerpt-card p{margin:0 0 6px;color:var(--muted);font-size:12px;line-height:1.5}
.excerpt-card small{display:block;color:var(--muted-2);font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:700}
.reader-shell{display:flex;flex-direction:column;height:100%}
.reader-head{position:relative;padding:18px 54px 14px 20px;border-bottom:2px solid var(--text);background:var(--surface)}
.reader-head h2{margin:0 0 6px;font-size:1.5rem;letter-spacing:-0.03em}
.reader-meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px;color:var(--muted);font-size:12px}
.reader-meta .meta-pill{display:inline-flex;align-items:center;padding:5px 8px;border:1px solid var(--border);border-radius:4px;background:var(--surface);color:var(--muted)}
.reader-source-link{display:inline-flex;align-items:center;padding:5px 8px;border:1px solid var(--border);border-radius:4px;background:var(--surface);color:var(--blue);font-size:10px;font-weight:700;text-decoration:none}
.reader-toolbar{position:absolute;right:14px;top:18px;display:flex;justify-content:flex-end}
.reader-view-toggle{display:inline-flex;padding:3px;border:1px solid var(--border);border-radius:999px;background:var(--surface);gap:3px}
.reader-view-button{padding:6px 10px;border:0;border-radius:999px;background:transparent;color:var(--muted);font-size:10px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;cursor:pointer}
.reader-view-button.active{background:var(--ink);color:#fff}
.close-reader{position:absolute;right:14px;top:12px;border:0;background:transparent;color:var(--text);font-size:2rem;line-height:1;cursor:pointer}
.reader-layout{display:grid;grid-template-columns:minmax(240px,.72fr) minmax(0,1.8fr) minmax(240px,.72fr);height:calc(100% - 92px)}
.chunk-panel{margin:0 0 14px;border:1px solid var(--border);border-radius:10px;background:var(--surface);overflow:hidden}
.chunk-header{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 12px;border-bottom:1px solid var(--border);background:rgba(248,250,252,0.75);font-size:10px;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}
.chunk-header strong{color:var(--text);font-size:10px}
.chunk-body{padding:16px 18px;font-family:Georgia,"Times New Roman",serif;font-size:16px;line-height:1.8;white-space:pre-wrap}
.chunk-citation{display:inline;padding:1px 6px;border-radius:6px;background:var(--blue-soft);color:var(--navy);font-size:11px;font-weight:700;border:1px solid rgba(49,93,141,.18)}.chunk-statute{display:inline;padding:1px 6px;border-radius:6px;background:#eee4f7;color:#4b2868;font-size:11px;font-weight:700;border:1px solid rgba(107,70,145,.28);box-shadow:inset 0 -1.5px 0 #7b4fa3}#decisionBody .chunk-statute{background:#eee4f7!important;color:#4b2868!important;border-color:rgba(107,70,145,.28)!important;box-shadow:inset 0 -1.5px 0 #7b4fa3!important}
.reader-pane{overflow:auto;border-right:1px solid var(--border);background:linear-gradient(180deg,#fff,#f8fafc)}
.reader-pane.linked{border-right:0;background:#f8f6ef}.reader-pane.linked .reader-status{padding:18px;color:var(--muted);font-size:12px;line-height:1.5}
.reader-pane.target{border-right:0;background:#f8fafc}
.inline-case-reader{min-height:calc(100vh - 190px);overflow:hidden}.inline-case-reader .reader-shell{min-height:calc(100vh - 190px)}.inline-case-reader .reader-layout{flex:1;height:auto;min-height:0}.inline-case-reader .reader-head{padding-left:20px}.return-to-results{display:inline-flex;align-items:center;margin:0 0 9px;padding:5px 7px;border:1px solid var(--border);border-radius:5px;background:var(--surface);color:var(--text);font-size:10px;font-weight:700;cursor:pointer}
.reader-pane-header{padding:14px 18px 10px;border-bottom:1px solid var(--border);color:var(--muted);font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:700}
.reader-text{padding:18px 22px 28px;font-family:Georgia,"Times New Roman",serif;font-size:16px;line-height:1.8;white-space:pre-wrap}
.reader-text mark{background:#f8e6a7;padding:0 2px;border-radius:4px}
.reader-text mark.primary{background:#f0c29b}
.reader-text .citation-link{display:inline;padding:1px 6px;border-radius:6px;background:var(--blue-soft);color:var(--navy);font-size:11px;font-weight:700;cursor:pointer;border:0}
.reader-target-body{padding:18px}.reader-target-body h3{margin:0 0 8px;font-size:1.2rem;letter-spacing:-0.02em}.reader-target-meta{margin-bottom:14px;color:var(--muted);font-size:12px}.quote{padding:14px 16px;border:1px solid var(--border);border-radius:10px;background:#fff;white-space:pre-wrap;font-family:Georgia,"Times New Roman",serif;font-size:15px;line-height:1.7}
.reader-status{padding:22px;color:var(--muted);font-size:14px}
.reader-intel{padding:14px}.reader-intel-section{margin-bottom:16px}.reader-intel-section:last-child{margin-bottom:0}.reader-intel-section h3{margin:0 0 4px;font-size:13px;letter-spacing:-.01em}.reader-intel-section p{margin:0 0 8px;color:var(--muted);font-size:11px;line-height:1.45}.reader-intel-row{padding:10px 0;border-top:1px solid var(--border)}.reader-intel-row strong{display:block;font-size:12px;line-height:1.35}.reader-intel-row small{display:block;margin-top:3px;color:var(--muted);font-size:10px;line-height:1.45}.reader-intel-row a{display:inline-block;margin-top:5px;color:var(--blue);font-size:10px;font-weight:700;text-decoration:none}.reader-intel-action{display:inline-flex;align-items:center;margin:0 0 12px;padding:7px 9px;border:1px solid var(--border);border-radius:7px;background:var(--surface);color:var(--navy);font-size:11px;font-weight:700;text-decoration:none}.reader-intel-context{margin-top:5px;padding:7px 8px;border-left:2px solid var(--blue);background:var(--blue-soft);color:var(--text);font-size:10px;line-height:1.45}
.reader-info-tabs{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));border-bottom:1px solid var(--border);background:#f8f6ef}.reader-info-tabs button{padding:9px 2px;border:0;background:transparent;color:var(--muted);font-size:9px;letter-spacing:.04em;text-transform:uppercase;cursor:pointer}.reader-info-tabs button.active{color:var(--text);box-shadow:inset 0 -2px var(--rust)}.reader-info-content{min-height:0}.reader-info{padding:14px}.reader-info-section{margin-bottom:16px}.reader-info-section:last-child{margin-bottom:0}.reader-info-section h3{margin:0 0 7px;font-size:12px;letter-spacing:.05em;text-transform:uppercase}.reader-info-row{padding:9px 0;border-top:1px solid var(--border)}.reader-info-row:first-of-type{border-top:0}.reader-info-row strong{display:block;font-size:12px;line-height:1.35}.reader-info-row small{display:block;margin-top:3px;color:var(--muted);font-size:10px;line-height:1.45}.reader-info-row a{display:inline-block;margin-top:5px;color:var(--blue);font-size:10px;font-weight:700;text-decoration:none}.reader-info-metrics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}.reader-info-metric{padding:8px;border:1px solid var(--border);border-radius:5px;background:var(--surface)}.reader-info-metric strong{display:block;font-size:14px}.reader-info-metric span{display:block;margin-top:2px;color:var(--muted);font-size:9px}.reader-info-tags{display:flex;flex-wrap:wrap;gap:5px}.reader-info-tags span{padding:4px 6px;border:1px solid var(--border);border-radius:4px;background:#f4f3ed;color:var(--muted);font-size:9px}.reader-info-preview{padding:14px}.reader-info-preview h3{margin:0 0 8px;font-size:16px}.reader-info-preview-meta{margin-bottom:12px;color:var(--muted);font-size:11px}
.reader-info{display:block}.reader-info-table{width:100%;min-width:0;margin:0 0 16px;border-collapse:collapse}.reader-info-table th,.reader-info-table td{padding:8px 9px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top;font-size:10px;line-height:1.4}.reader-info-table th{width:38%;color:var(--muted);font-size:9px;letter-spacing:.06em;text-transform:uppercase;font-weight:700}.reader-info-table td{color:var(--text);word-break:break-word}.reader-info-table tr:last-child th,.reader-info-table tr:last-child td{border-bottom:0}.reader-citation-group{border-top:1px solid var(--border);padding:8px 0}.reader-citation-group summary{display:flex;justify-content:space-between;gap:10px;cursor:pointer;list-style:none;font-size:11px}.reader-citation-group summary::-webkit-details-marker{display:none}.reader-citation-group summary span{color:var(--muted);white-space:nowrap}.reader-citation-occurrences{padding-left:10px}.reader-citation-occurrences .reader-info-row{padding:8px 0;border-top:1px solid var(--border)}
.global-search,.header-actions,.sidebar,.right-panel,.bottom-tray{display:none}
@media(max-width:1100px){.reader-layout{grid-template-columns:minmax(210px,.72fr) minmax(0,1.6fr) minmax(210px,.72fr)}}
@media(max-width:760px){.reader-layout{display:flex;flex-direction:column;height:auto}.reader-pane.target{order:1;max-height:none}.reader-pane.source{order:2;min-height:520px}.reader-pane.linked{order:3;min-height:180px}.reader-info-tabs{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* Citation Map visual language: shared research-workbench foundation. */
:root{--bg:#f1efe8;--surface:#fffef9;--surface-alt:#f8f6ef;--border:#d8d5ca;--text:#202522;--muted:#69726d;--muted-2:#8b928d;--navy:#202522;--blue:#315d8d;--blue-soft:#e7eef6;--green:#176c68;--green-soft:#edf5f3;--amber:#c28e2d;--amber-soft:#f8f0dc;--red:#a4412b;--red-soft:#f7e8e3;--purple:#62754d;--purple-soft:#edf1e7;--shadow:0 10px 28px rgba(32,37,34,.07);--shadow-soft:0 8px 20px rgba(32,37,34,.08)}
html,body{height:auto;min-height:100%;background:var(--bg)}body{font-family:"IBM Plex Sans",sans-serif;letter-spacing:0;background-image:linear-gradient(rgba(32,37,34,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(32,37,34,.035) 1px,transparent 1px);background-size:26px 26px}
.app-shell{background:transparent}.topbar{height:68px;justify-content:space-between;padding:0 24px;border-bottom:1px solid var(--border);background:rgba(255,254,249,.96)}.topbar .brand{align-items:baseline;gap:13px}.logo-mark{display:none}.brand-name{font:700 28px/1 "Newsreader",serif;letter-spacing:0}.brand-sub{font-size:12px;letter-spacing:0;text-transform:none;color:var(--muted)}.research-nav{display:flex;align-items:center;gap:5px}.research-nav a{display:flex;align-items:center;gap:5px;padding:7px 9px;border-radius:5px;color:var(--muted);font-size:10px;text-decoration:none}.research-nav a.active{background:var(--ink);color:#fff}.research-nav a:hover{color:var(--teal)}
.workspace{min-height:calc(100vh - 68px)}.center-pane{max-width:1320px;padding:25px 24px 40px;gap:14px;overflow:visible}.page-header{padding:4px 0 2px}.eyebrow{color:var(--rust);letter-spacing:.08em}.page-header h1{font:700 31px/1.1 "Newsreader",serif;letter-spacing:0}.page-header p{font-size:12px;color:var(--muted)}.view-tabs{gap:0;margin-top:17px;border-bottom:1px solid var(--border)}.tab{border:0;border-radius:0;background:transparent;padding:10px 12px;color:var(--muted);font-size:10px;letter-spacing:.04em;text-transform:uppercase}.tab.active{background:transparent;color:var(--text);box-shadow:inset 0 -2px var(--rust)}
.panel-card{border:1px solid var(--border);border-radius:5px;box-shadow:none;background:rgba(255,254,249,.94)}.search-layout{padding:17px}.search-form{gap:10px}.search-form label{font-size:10px;letter-spacing:.08em;color:var(--muted)}.search-form input,.search-form select{height:39px;border-color:var(--border);border-radius:5px;background:var(--surface);font-size:12px}.search-form input:focus,.search-form select:focus{outline:0;border-color:var(--teal)}.search-actions{gap:7px}.search-actions button{height:39px;border-radius:5px;background:var(--ink);font-size:10px;letter-spacing:.04em}.search-actions button.secondary{border:1px solid var(--border);background:var(--surface);color:var(--ink)}.advanced-actions{margin-top:10px}.advanced-search{border-color:var(--border)}.search-meta{border-color:var(--border);font-size:11px}.case-result{padding:12px 14px;border-color:var(--border);border-radius:5px;background:var(--surface)}.case-result:hover{border-color:var(--teal);background:#edf3f0;box-shadow:none}.result-title{font-size:14px;letter-spacing:0}.result-meta{font-size:11px;line-height:1.45}.tag{padding:4px 6px;border:1px solid var(--border);border-radius:4px;letter-spacing:.04em}.tag.win{background:var(--green-soft);color:var(--green)}.tag.loss{background:var(--red-soft);color:var(--red)}.tag.neutral{background:#f4f3ed;color:var(--muted)}
.summaryRows,.legend{gap:14px;padding:13px 14px 0;font-size:11px}.summaryRows span strong{font-size:19px;letter-spacing:0}.table-wrap{padding:0;margin-top:12px}thead th{padding:10px 12px;background:#f8f6ef;border-color:var(--border);font-size:10px}tbody td{padding:10px 12px;border-color:#e9e6dd;font-size:12px}tbody tr:hover{background:#edf3f0}.bar{background:#ebe9df;border-radius:0}.note-box{padding:10px 12px;border-color:var(--border);border-radius:5px;background:var(--surface)}.ci-header h3{font:600 19px/1.15 "Newsreader",serif}.ci-chart{border-color:var(--border);background:rgba(255,254,249,.6)}.ci-evidence{border-color:var(--border)}.ci-quote,.reader-intel-context{border-left-color:var(--teal);background:#edf5f3}.ci-pager button,.judge-open{border-color:var(--border);border-radius:5px;background:var(--surface);color:var(--ink)}
.reader-head{border-bottom-color:var(--ink);background:var(--surface)}.reader-head h2{font-family:"Newsreader",serif}.reader-pane{border-color:var(--border);background:var(--surface)}.reader-pane.target{background:#f8f6ef}.reader-pane-header{border-color:var(--border)}.reader-text{font-family:"Newsreader",serif;font-size:17px;line-height:1.75}.reader-text .citation-link{border-radius:3px;background:#e7eef6;color:var(--blue)}.quote{border-color:var(--border);border-radius:5px;background:var(--surface)}
@media(max-width:1180px){.topbar{grid-template-columns:240px minmax(0,1fr) 200px}.workspace{grid-template-columns:240px minmax(0,1fr) 320px}.bottom-tray{grid-template-columns:repeat(2,minmax(180px,1fr))}.search-form{grid-template-columns:repeat(2,minmax(180px,1fr))}.search-form .wide{grid-column:span 2}}
@media(max-width:920px){.topbar{grid-template-columns:1fr;height:auto;padding:14px 16px;gap:12px}.workspace{display:block;min-height:0;flex:none}.sidebar,.right-panel{display:none}.center-pane{padding:12px}.search-form{grid-template-columns:1fr}.search-form .wide{grid-column:span 1}.bottom-tray{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="app-shell">
<header class="topbar">
<div class="brand">
<div>
<div class="brand-name">ILIT</div>
<div class="brand-sub">Immigration Litigation Intelligence System</div>
</div>
</div>
<nav class="research-nav" aria-label="Primary navigation"><a class="active" href="/data-explorer">Research</a><a href="/citation-map">Citation Map</a><a href="/case-reader">Case Reader</a></nav>
</header>
<div class="workspace">
<aside class="sidebar">
<div class="section-label">Research desk</div>
<div class="nav-card active"><span class="nav-icon">?</span>Dashboard</div>
<div class="nav-card"><span class="nav-icon">?</span>Research Projects</div>
<div class="nav-card"><span class="nav-icon">?</span>Active Files</div>
<div class="nav-card"><span class="nav-icon">?</span>Case Collections</div>
<div class="nav-card"><span class="nav-icon">?</span>Authorities</div>
<div class="nav-card"><span class="nav-icon">?</span>Notes</div>
<div class="nav-card"><span class="nav-icon">?</span>Bookmarks</div>
<div class="nav-card"><span class="nav-icon">?</span>Timeline</div>
<div class="nav-card"><span class="nav-icon">?</span>Workspaces</div>
<div class="section-label">Quick access</div>
<div class="quick-grid">
<div class="quick-card"><div class="quick-label"><strong>IRPA</strong><span>Immigration law</span></div><div class="badge-count">12</div></div>
<div class="quick-card"><div class="quick-label"><strong>PRRA</strong><span>Return risk</span></div><div class="badge-count">7</div></div>
<div class="quick-card"><div class="quick-label"><strong>ENFIP</strong><span>Manuals</span></div><div class="badge-count">18</div></div>
</div>
<div class="section-label">Folders</div>
<div class="folder-list">
<div class="folder-item"><span>Leave Applications</span><small>24</small></div>
<div class="folder-item"><span>Judicial Reviews</span><small>86</small></div>
<div class="folder-item"><span>Inadmissibility</span><small>41</small></div>
<div class="folder-item"><span>Refugee Protection</span><small>63</small></div>
<div class="folder-item"><span>Humanitarian &amp; Compassionate</span><small>29</small></div>
</div>
</aside>
<main class="center-pane">
<div class="page-header">
<div class="eyebrow">Immigration litigation intelligence</div>
<h1>Immigration Litigation Intelligence Tool</h1>
<p>Search decisions, inspect authorities, and compare outcomes across the case library.</p>
<div class="view-tabs" role="tablist" aria-label="Research views">
<button class="tab" type="button" data-tab="about">About</button>
<button class="tab active" type="button" data-tab="search">Case search</button>
<button class="tab" type="button" data-tab="citation-intelligence">Citation Intelligence</button>
<button class="tab" type="button" data-tab="judge">Judge outcomes</button>
<button class="tab" type="button" data-tab="judge-profile">Judge Profile</button>
<button class="tab" type="button" data-tab="explorer">Data explorer</button>
<button class="tab" type="button" data-tab="fc-history">FC History</button>
</div>
</div>
<section id="aboutPanel" class="panel-card search-layout" hidden>
<div class="page-header"><div class="eyebrow">About the tool</div><h2>Immigration Litigation Intelligence Tool</h2><p>Evidence-focused research across Canadian immigration decisions, authorities, and outcomes.</p></div>
<div class="summaryRows" id="aboutSummary"><span>Loading library statistics...</span></div>
<div class="about-dashboard" id="aboutDashboard"><div class="about-dashboard-group"><div class="about-dashboard-label">Core library</div><div class="about-metric-grid"><div><strong id="aboutCaseCountTop">--</strong><span>decision cases</span></div><div><strong id="aboutChunkCountTop">--</strong><span>searchable chunks</span></div><div><strong id="aboutCitationCountTop">--</strong><span>citation records</span></div><div><strong id="aboutLinkedCitationCountTop">--</strong><span>resolved citations</span></div></div></div><div class="about-dashboard-group"><div class="about-dashboard-label">Federal Court activity</div><div class="about-metric-grid"><div><strong id="aboutFcCaseCountTop">--</strong><span>IMM case records</span></div><div><strong id="aboutFcDocumentCountTop">--</strong><span>docket entries</span></div><div><strong id="aboutJudgeCountTop">--</strong><span>judge profiles</span></div><div><strong id="aboutCaseJudgeCountTop">--</strong><span>case-judge links</span></div></div></div></div>
<div class="about-coverage"><div class="about-coverage-head"><strong>Data layer coverage</strong><span>Live row counts from the current database</span></div><div class="about-coverage-grid"><div class="about-coverage-row"><strong>Decision records</strong><span>cases</span><b id="aboutCaseCountLayer">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Search index</strong><span>case_chunks</span><b id="aboutChunkCountLayer">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Sources</strong><span>case_sources</span><b id="aboutSourceCount">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Ingestion history</strong><span>ingestion_runs</span><b id="aboutIngestionCount">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Citations</strong><span>citations</span><b id="aboutCitationCountLayer">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Citation metrics</strong><span>citation_metrics</span><b id="aboutCitationMetricsCount">--</b><em>empty</em></div><div class="about-coverage-row"><strong>Statute references</strong><span>statute_references</span><b id="aboutStatuteCount">--</b><em>empty</em></div><div class="about-coverage-row"><strong>Case tags</strong><span>case_tags</span><b id="aboutTagCount">--</b><em>empty</em></div><div class="about-coverage-row"><strong>Embeddings</strong><span>case_chunk_embeddings</span><b id="aboutEmbeddingCount">--</b><em>empty</em></div><div class="about-coverage-row"><strong>FC activity cases</strong><span>fc_activity_cases</span><b id="aboutFcCaseCountLayer">--</b><em>populated</em></div><div class="about-coverage-row"><strong>FC docket entries</strong><span>fc_activity_documents</span><b id="aboutFcDocumentCountLayer">--</b><em>populated</em></div><div class="about-coverage-row"><strong>Procedural staging</strong><span>fc_procedural_history</span><b id="aboutProceduralCountLayer">--</b><em>small staging set</em></div></div></div>
<div class="about-story">
<section class="about-section"><div class="about-kicker">01 / Case records</div><h3>Each case is more than a title and citation.</h3><p>A case record can include the case name, neutral citation, court, jurisdiction, decision date, docket number, source URL, source identity, full decision text, processing state, and extracted metadata. The original source relationship is retained so research can move from a result back to the underlying decision.</p><div class="about-fields"><span>Case identity</span><span>Court and jurisdiction</span><span>Date and docket</span><span>Source provenance</span><span>Full text</span><span>Extracted metadata</span></div></section>
<section class="about-section"><div class="about-kicker">02 / Searchable text</div><h3>Decisions are divided into evidence-sized text chunks.</h3><p>The library currently contains <strong id="aboutChunkCount">--</strong> searchable chunks. Each chunk belongs to a case and records its chunk set, position, label, paragraph range, text, text hash, and token estimate. Chunks are the units used for full-text search, semantic retrieval, citation evidence, and passage-level reading.</p></section>
<section class="about-section"><div class="about-kicker">03 / Citation records</div><h3>Citations remain tied to where they appear.</h3><p>Each citation record preserves the raw citation text as it appeared, a normalized citation form, the case that made the citation, and the cited case when the reference was resolved. When available, it also stores the source chunk and character offsets so a researcher can locate the citation in its surrounding passage.</p><div class="about-flow"><span>Source case</span><b>→</b><span>Raw citation text</span><b>→</b><span>Chunk + offsets</span><b>→</b><span>Resolved target case</span></div><p class="about-note"><strong id="aboutCitationCount">--</strong> citation records are stored; <strong id="aboutLinkedCitationCount">--</strong> currently resolve to another case in the library. Unresolved references remain available for review rather than being discarded.</p></section>
<section class="about-section"><div class="about-kicker">04 / Citation intelligence</div><h3>The citation layer supports relationship research.</h3><p>Because citation records connect source cases to cited authorities, the site can expose incoming and outgoing citation relationships, authority use over time, citation evidence, related decisions, and unresolved-reference quality checks. The graph is built from the underlying records, not from a manually curated list.</p></section>
<section class="about-section"><div class="about-kicker">05 / Federal Court activity</div><h3>Federal Court history is a separate activity layer.</h3><p>The FC activity collection currently contains <strong id="aboutFcCaseCount">--</strong> case-level records and <strong id="aboutFcDocumentCount">--</strong> linked docket entries. Case records include IMM citation, year, case name, filing date, registry location, nature, class, track, source URL, and scrape timestamp. Each linked activity entry preserves its record number, document number, date, and the original <code>RECORDED_ENTRY</code> text.</p><p>This layer is designed for timelines, location filters, and later extraction of procedural events such as filings, orders, hearings, decisions, leave outcomes, and judicial-review outcomes. Its coverage is useful but not a complete Federal Court archive.</p></section>
<section class="about-section"><div class="about-kicker">06 / Coverage and status</div><h3>What is available now, and what is still being built.</h3><div class="about-status-grid"><div><strong id="aboutCaseCount">--</strong><span>decision case records</span></div><div><strong id="aboutJudgeCount">--</strong><span>judge profiles</span></div><div><strong id="aboutProceduralCount">--</strong><span>procedural-history staging records</span></div><div><strong>Review first</strong><span>automated extraction remains research assistance, not a substitute for checking the source record</span></div></div><p class="about-note">Counts update from the current database. Empty or incomplete extraction layers are labeled plainly so the scope of the evidence stays visible.</p></section>
</div>
</section>
<section id="searchPanel" class="panel-card search-layout">
<form class="search-form" id="caseSearch">
<div class="wide"><label for="searchQuery">Case name or citation</label><input id="searchQuery" placeholder="e.g. Vavilov or 2019 SCC 65" autocomplete="off"></div>
<div class="search-actions"><button type="submit">Search cases</button><button type="button" class="secondary" id="clearSearch">Clear</button></div>
<div class="advanced-search" id="advancedSearchOptions" hidden><div class="search-form">
<div><label for="cites">Cases citing</label><input id="cites" placeholder="e.g. Vavilov"></div>
<div><label for="governmentOutcome">Government outcome</label><select id="governmentOutcome"><option value="">Any outcome</option><option value="won">Government won</option><option value="lost">Individual won</option></select></div>
<div><label for="decisionOutcome">Decision outcome</label><select id="decisionOutcome"><option value="">Any result</option><option value="dismissed">Dismissed</option><option value="allowed">Allowed</option><option value="granted">Granted</option></select></div>
<div><label for="ministerFilter">Minister / government party</label><select id="ministerFilter"><option value="">Any minister or government party</option></select></div>
<div><label for="judgeFilter">Judge contains</label><input id="judgeFilter" placeholder="e.g. Zinn"></div>
<div><label for="courtFilter">Court contains</label><input id="courtFilter" placeholder="e.g. FC"></div>
<div><label for="yearFilter">Decision year</label><input id="yearFilter" inputmode="numeric" maxlength="4" placeholder="e.g. 2024"></div>
<div><label for="searchSort">Sort results</label><select id="searchSort"><option value="newest" selected>Newest decision</option><option value="relevance">Most cited / newest</option><option value="oldest">Oldest decision</option><option value="minister">Minister / government party (A-Z)</option></select></div>
<div><label for="searchLimit">Results</label><select id="searchLimit"><option>10</option><option>25</option><option selected>50</option><option>100</option></select></div>
<label class="check-field"><input id="searchFullText" type="checkbox">Search full decision text</label>
</div></div>
</form>
<div class="search-actions advanced-actions"><button type="button" class="secondary" id="toggleAdvancedSearch" aria-expanded="false" aria-controls="advancedSearchOptions">Advanced options</button></div>
<div class="search-meta" id="searchMeta">Search by case name or citation. Open Advanced options for filters or full-decision text.</div>
<div class="results-wrap" id="searchResults"></div>
</section>
<section id="caseReaderPanel" class="panel-card inline-case-reader" hidden>
<div class="reader-shell">
<div class="reader-head">
<button class="return-to-results" type="button" onclick="closeDecisionReader()">Return to case results</button>
<h2 id="decisionTitle">Decision</h2>
<div class="reader-meta" id="decisionMeta"></div>
<div class="reader-toolbar">
  <div class="reader-view-toggle" role="tablist" aria-label="Reader view mode">
    <button type="button" class="reader-view-button active" data-reader-view="normalized">Normalized text</button>
    <button type="button" class="reader-view-button" data-reader-view="chunks">Chunks</button>
  </div>
</div>
</div>
<div class="reader-layout">
<aside class="reader-pane target"><div class="reader-pane-header" id="decisionTargetHeading">Case information</div><div id="decisionTarget"><div class="reader-status">Open a decision to review its information and citation intelligence.</div></div></aside>
<article class="reader-pane source"><div class="reader-pane-header">Source decision</div><div class="reader-text" id="decisionBody"></div></article>
<aside class="reader-pane linked"><div class="reader-pane-header">Case context</div><div class="reader-status">Linked cases and related authorities will appear here.</div></aside>
</div>
</div>
</section>
<section id="citationIntelligencePanel" class="panel-card search-layout" hidden>
<div class="page-header"><div class="eyebrow">Authority analysis</div><h2>Citation Intelligence</h2><p>Trace how authorities are used, where they travel, and what outcomes follow.</p></div>
<form class="search-form" id="citationIntelligenceSearch"><div class="wide"><label for="citationCaseQuery">Find a case by title</label><input id="citationCaseQuery" placeholder="e.g. Vavilov v. Canada" autocomplete="off"></div><div class="search-actions"><button type="submit">Find case</button></div></form>
<div class="search-meta" id="citationSearchMeta">Search by case title to open Citation Intelligence.</div>
<div class="results-wrap" id="citationSearchResults"></div>
<div class="view-tabs citation-subtabs" role="tablist" aria-label="Citation Intelligence views"><button class="tab active" type="button" data-ci-tab="overview">Overview</button><button class="tab" type="button" data-ci-tab="timeline">Timeline</button><button class="tab" type="button" data-ci-tab="outcomes">Outcomes</button><button class="tab" type="button" data-ci-tab="courts">Courts</button><button class="tab" type="button" data-ci-tab="judges">Judges</button><button class="tab" type="button" data-ci-tab="companions">Companions</button><button class="tab" type="button" data-ci-tab="statutes">Statutes</button><button class="tab" type="button" data-ci-tab="table">Evidence</button></div>
<div id="citationIntelligenceContent" class="search-meta">Select a case from Case Search to inspect its citation intelligence.</div>
</section>
<section id="judgePanel" class="panel-card search-layout" hidden>
<div class="summaryRows" id="judgeSummary"><span>Loading judge outcomes...</span></div>
<div class="legend"><span class="key"><i class="dot" style="background:var(--blue)"></i>Government wins</span><span class="key"><i class="dot" style="background:var(--red)"></i>Individual wins</span><span class="key"><i class="dot" style="background:#cbd5e1"></i>Unclassified</span></div>
<div class="table-wrap"><table><thead><tr><th>#</th><th>Judge</th><th class="number">Decisions</th><th>Outcome split</th><th class="number">Government wins</th><th class="number">Individual wins</th><th class="number">Unclassified</th><th class="number">Government win rate</th></tr></thead><tbody id="judgeRows"><tr><td colspan="8" class="empty">Loading judge outcomes...</td></tr></tbody></table></div>
<p class="search-meta">Includes every judge with more than 100 decisions. Win rate uses classified government-versus-individual outcomes only.</p>
</section>
<section id="judgeProfilePanel" class="panel-card search-layout" hidden>
<div class="page-header"><div class="eyebrow">Judicial profiles</div><h2>Judge Profile</h2><p>Explore normalized judge records and the decisions associated with each profile.</p></div>
<form class="search-form" id="judgeProfileSearch"><div class="wide"><label for="judgeProfileQuery">Find a judge by name</label><input id="judgeProfileQuery" placeholder="e.g. Zinn" autocomplete="off"></div><div class="search-actions"><button type="submit">Find judge</button></div></form>
<div class="search-meta" id="judgeProfileSearchMeta">Search by judge name to open a profile.</div>
<div id="judgeProfileContent" class="search-meta">Loading judge profiles...</div>
</section>
<section id="explorerPanel" class="panel-card search-layout" hidden>
<div class="search-form" style="grid-template-columns:repeat(3,minmax(180px,1fr));margin-bottom:8px;">
<div><label for="groupBy">Field A: rank by</label><select id="groupBy"></select></div>
<div><label for="splitBy">Field B: break down by</label><select id="splitBy"></select></div>
<div><label for="limit">Results to show</label><select id="limit"><option>10</option><option>25</option><option selected>50</option><option>75</option><option>100</option></select></div>
</div>
<div class="summaryRows" id="summary"><span>Loading results...</span></div>
<div class="legend" id="legend"></div>
<div class="table-wrap"><table><thead id="head"></thead><tbody id="rows"><tr><td class="empty">Loading analytics...</td></tr></tbody></table></div>
<p class="search-meta">Missing values are shown as ?Unknown.? Counts use the metadata extracted from each decision and update from the current database state.</p>
</section>
<section id="fcHistoryPanel" class="panel-card search-layout" hidden>
<div class="page-header"><div class="eyebrow">Federal Court procedural history</div><h2>FC History</h2><p>Lookup an IMM number and pull the latest Federal Court leave/JR activity from the official FC site.</p></div>
<form class="search-form" id="fcHistoryForm">
<div class="wide"><label for="fcImmInput">IMM number</label><input id="fcImmInput" data-fc-docket="" placeholder="IMM-1234-19" autocomplete="off"></div>
<div class="search-actions"><button type="submit">Fetch history</button></div>
</form>
<div class="search-meta" id="fcHistoryMeta">Enter an IMM number to fetch procedural history.</div>
<div class="results-wrap" id="fcHistoryResults"><div class="empty">No Federal Court history loaded yet.</div></div>
<section class="fc-activity-block" aria-labelledby="fcActivityHeading">
<div class="ci-header"><h3 id="fcActivityHeading">Federal Court cases filed over time</h3><p>Annual count of FC activity cases, filterable by registry location.</p></div>
<div class="search-form fc-activity-filter"><div><label for="fcActivityCity">Location filed</label><select id="fcActivityCity"><option value="">All locations</option></select></div></div>
<div class="search-meta" id="fcActivityMeta">Loading FC activity totals...</div>
<div id="fcActivityChart" class="fc-activity-chart"><div class="empty">Loading chart...</div></div>
</section>
</section>
</main>
<aside class="right-panel">
<div class="side-card">
<div class="header">Research notebook</div>
<div class="body">
<div class="tags-cloud">
<span class="cloud-tag">Procedural Fairness</span><span class="cloud-tag">Bias</span><span class="cloud-tag">Country Conditions</span><span class="cloud-tag">Credibility</span><span class="cloud-tag">Risk on Return</span><span class="cloud-tag">Alternative Internal Flight</span>
</div>
</div>
</div>
<div class="side-card">
<div class="header">Analyst notes</div>
<div class="body">
<div class="note-box"><strong>Key note</strong><span>RAD failed to engage with probative country evidence.</span></div>
<div class="note-box"><strong>Litigation theme</strong><span>Reasonableness review and fairness of evidence assessment.</span></div>
</div>
</div>
<div class="side-card">
<div class="header">Issues identified</div>
<div class="body">
<div class="issue-row"><div><strong>Procedural fairness</strong><small>Issue</small></div><div class="score-badge red">High</div><div class="score-badge red">92%</div></div>
<div class="issue-row"><div><strong>Reasonableness review</strong><small>Issue</small></div><div class="score-badge amber">Medium</div><div class="score-badge amber">72%</div></div>
<div class="issue-row"><div><strong>Country conditions</strong><small>Issue</small></div><div class="score-badge green">Low</div><div class="score-badge green">64%</div></div>
</div>
</div>
<div class="side-card">
<div class="header">Draft arguments</div>
<div class="body">
<div class="note-box"><strong>Argument 01</strong><span>Status: Drafting ? Last modified: 2h ago ? 14 authorities</span></div>
<div class="note-box"><strong>Argument 02</strong><span>Status: In review ? Last modified: 1d ago ? 8 authorities</span></div>
</div>
</div>
</aside>
</div>
<section class="bottom-tray">
<div class="tray-panel"><div class="tray-head">Saved excerpts</div><div class="tray-body"><div class="excerpt-card"><p>?The board must provide a clear account of why it rejects expert evidence and country conditions material.?</p><small>Raza v Canada ? ?18</small></div></div></div>
<div class="tray-panel"><div class="tray-head">Citation clipboard</div><div class="tray-body"><div class="excerpt-card"><p>Baker v Canada</p><small>Authority</small></div><div class="excerpt-card"><p>Vavilov</p><small>Authority</small></div><div class="excerpt-card"><p>Kanthasamy</p><small>Authority</small></div></div></div>
<div class="tray-panel"><div class="tray-head">Recently viewed</div><div class="tray-body"><div class="excerpt-card"><p>Singh v Canada</p><small>2 hours ago ? 14 views</small></div><div class="excerpt-card"><p>Chieu v Canada</p><small>1 day ago ? 9 views</small></div></div></div>
<div class="tray-panel"><div class="tray-head">Bookmarked passages</div><div class="tray-body"><div class="excerpt-card"><p>Accountability of tribunal reasoning</p><small>Case: Raza ? Topic: fairness</small></div><div class="excerpt-card"><p>Evidence-based review</p><small>Case: Chieu ? Topic: nexus</small></div></div></div>
<div class="tray-panel"><div class="tray-head">Active file context</div><div class="tray-body"><div class="excerpt-card"><p>Court: Federal Court</p><small>Registry: Ottawa</small></div><div class="excerpt-card"><p>Deadline: 15 November 2026</p><small>Status: Active ? Project: RPD Review</small></div></div></div>
</section>
</div>
<script>
const palette=['var(--blue)','var(--red)','var(--amber)','var(--green)','var(--purple)'];
const esc=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const num=value=>new Intl.NumberFormat().format(Number(value||0));
let fields=[];
function searchValues(){return {query:document.getElementById('searchQuery').value,cites:document.getElementById('cites').value,government_outcome:document.getElementById('governmentOutcome').value,decision_outcome:document.getElementById('decisionOutcome').value,minister:document.getElementById('ministerFilter').value,judge:document.getElementById('judgeFilter').value,court:document.getElementById('courtFilter').value,year:document.getElementById('yearFilter').value,search_full_text:document.getElementById('searchFullText').checked?'true':'',sort_by:document.getElementById('searchSort').value,limit:document.getElementById('searchLimit').value};}
function resultCard(item){const tags=[item.citation,item.court,item.date,item.minister,item.judge,item.decision_outcome,item.government_outcome==='won'?'Government won':item.government_outcome==='lost'?'Individual won':''].filter(Boolean),citationInfo=`${num(item.citation_mentions)} citation mention${item.citation_mentions===1?'':'s'} ? ${num(item.unique_cited_authorities)} unique cited ${item.unique_cited_authorities===1?'authority':'authorities'}${item.resolved_target_cases?` ? ${num(item.resolved_target_cases)} linked case${item.resolved_target_cases===1?'':'s'}`:''}`;return `<button class="case-result" data-case-id="${item.case_id}"><div class="result-title">${esc(item.title||'Untitled decision')}</div><div class="result-meta">${tags.map(value=>esc(value)).join(' ? ')}${item.matching_citations?` ? ${num(item.matching_citations)} matching citation${item.matching_citations===1?'':'s'}`:''}</div><div class="result-meta">${citationInfo}</div><div class="result-tags">${tags.slice(-2).map(value=>`<span class="tag ${value==='Government won'?'win':value==='Individual won'?'loss':'neutral'}">${esc(value)}</span>`).join('')}</div></button>`;}
async function loadSearch(event){if(event)event.preventDefault();const values=searchValues(),params=new URLSearchParams();Object.entries(values).forEach(([key,value])=>{if(value)params.set(key,value)});document.getElementById('searchMeta').textContent=values.search_full_text?'Searching names, citations, and full decision text...':'Searching case names and citations...';document.getElementById('searchResults').innerHTML='';try{const response=await fetch(`/analytics/search/cases?${params}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();document.getElementById('searchMeta').textContent=`Showing ${num(data.results.length)} matching decision${data.results.length===1?'':'s'}.`;document.getElementById('searchResults').innerHTML=data.results.map(resultCard).join('')||'<div class="empty">No cases matched these filters.</div>';document.querySelectorAll('.case-result').forEach(button=>button.onclick=()=>openDecision(Number(button.dataset.caseId)));}catch(error){document.getElementById('searchMeta').textContent=String(error);}}
function highlightCitationTarget(item, query){if (!item.target_case_id) return `<mark class="${query ? 'primary' : ''}" title="${esc(item.normalized || item.text)}">${esc(String(item.text || ''))}</mark>`;return `<button class="citation-link" type="button" data-target-case-id="${item.target_case_id}" data-target-title="${esc(item.target_title || 'Linked case')}" data-normalized="${esc(item.normalized || item.text || '')}" title="Open linked case: ${esc(item.target_title || 'Linked case')}">${esc(String(item.text || ''))}</button>`;}
function highlightedDecision(text,citations){const chars=Array.from(text||'');const needle=document.getElementById('cites').value.trim().toLocaleLowerCase();const ranges=(citations||[]).map(item=>({...item,start:Number(item.offset_start),end:Number(item.offset_end),text:item.text || item.normalized || item.citation_text || '',target_case_id:item.target_case_id || null,target_title:item.target_title || null})).filter(item => Number.isInteger(item.start) && Number.isInteger(item.end) && item.end > item.start && item.start >=0 && item.end <= chars.length).sort((a,b)=>a.start-b.start||b.end-a.end);let cursor=0, html='';for (const item of ranges){if (item.start < cursor) continue; html += esc(chars.slice(cursor,item.start).join('')); const primary = needle && String(item.text || '').toLowerCase().includes(needle); const statute = /\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b/i.test(String(item.normalized || item.text || '')); if (item.target_case_id){ html += `<button class="citation-link" type="button" data-target-case-id="${item.target_case_id}" data-target-title="${esc(item.target_title || 'Linked case')}" data-normalized="${esc(item.normalized || item.text || '')}" title="Open linked case: ${esc(item.target_title || 'Linked case')}">${esc(chars.slice(item.start,item.end).join(''))}</button>`;} else { html += `<mark class="${statute ? 'chunk-statute' : primary ? 'primary' : ''}" title="${esc(item.normalized || item.text)}">${esc(chars.slice(item.start,item.end).join(''))}</mark>`; } cursor = item.end;}return html + esc(chars.slice(cursor).join(''));}
async function openLinkedCase(caseId,label='Linked case'){const targetPane=document.getElementById('decisionTarget');targetPane.innerHTML='<div class="reader-status">Loading linked case...</div>';try{const response=await fetch(`/analytics/search/cases/${caseId}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();const item=data.case||{};const targetText=item.full_text||'';const snippet=targetText.length>2000?`${targetText.slice(0,2000).trim()}?`:targetText;targetPane.innerHTML=`<div class="reader-target-body"><h3>${esc(item.title||label)}</h3><div class="reader-target-meta">${esc(item.citation||'No citation')} ? ${esc(item.court||'Unknown court')} ? ${esc(item.date||'')}</div><div class="quote">${esc(snippet||'No text available')}</div></div>`;}catch(error){targetPane.innerHTML=`<div class="reader-status">${esc(error.message)}</div>`;}}
function extractDocketFromPayload(item){const values=[];const push=(candidate)=>{if(candidate===null||candidate===undefined) return; if(typeof candidate==='string'){const trimmed=candidate.trim(); if(trimmed) values.push(trimmed);} else if(typeof candidate==='number'){values.push(String(candidate));} else if(Array.isArray(candidate)){candidate.forEach(push);} else if(typeof candidate==='object'){for (const value of Object.values(candidate)) push(value);}};push(item);const patterns=[/IMM-\d{1,6}-\d{2,4}/i,/\b\d{1,6}-\d{2,4}\b/,/\b[A-Z]{2,6}-\d{1,6}-\d{2,4}\b/i];for (const value of values){for(const pattern of patterns){const match=value.match(pattern);if(match){return match[0].toUpperCase();}}}return ''}
function intelligenceRows(rows,render){return (rows||[]).map(render).join('')||'<div class="reader-status">No evidence available for this case.</div>'}
function renderCaseReaderPane(data,activeTab='details'){const box=document.getElementById('decisionTarget');const caseData=data.case||{},metrics=data.metrics||{},citations=data.citations||[],sources=data.sources||[],tags=data.tags||[],metadata=data.extracted_metadata||[];const infoRow=(title,detail,link='')=>`<div class="reader-info-row"><strong>${esc(title)}</strong><small>${esc(detail||'Not recorded')}</small>${link}</div>`;const metricsHtml=`<div class="reader-info-metrics"><div class="reader-info-metric"><strong>${num(metrics.in_degree)}</strong><span>incoming citations</span></div><div class="reader-info-metric"><strong>${num(metrics.out_degree)}</strong><span>outgoing citations</span></div><div class="reader-info-metric"><strong>${metrics.pagerank===null||metrics.pagerank===undefined?'--':Number(metrics.pagerank).toFixed(5)}</strong><span>PageRank</span></div><div class="reader-info-metric"><strong>${num(citations.length)}</strong><span>citation rows</span></div></div>`;const sourceLink=caseData.source_url?`<div class="reader-info-row"><strong>Original source</strong><small>${esc(caseData.source_name||caseData.source_type||'Source')}</small><a href="${esc(caseData.source_url)}" target="_blank" rel="noopener noreferrer">Open source</a></div>`:'';const details=`<div class="reader-info"><section class="reader-info-section"><h3>Case details</h3>${metricsHtml}${sourceLink||''}</section><section class="reader-info-section"><h3>Extracted metadata</h3>${metadata.slice(0,16).map(row=>infoRow(String(row.key||'').replaceAll('_',' '),`${row.value||''}${row.source?` / ${row.source}`:''}`)).join('')||'<div class="reader-status">No extracted metadata.</div>'}</section><section class="reader-info-section"><h3>Tags</h3><div class="reader-info-tags">${tags.map(tag=>`<span>${esc(`${tag.category}: ${tag.value}`)}</span>`).join('')||'<span>No tags available.</span>'}</div></section></div>`;const citationsHtml=`<div class="reader-info"><section class="reader-info-section"><h3>Stored citations</h3><p>Resolved and unresolved citation rows from this decision.</p>${citations.slice(0,80).map(row=>{const title=row.target_title||row.citation_text||row.normalized_citation||'Citation';const detail=[row.target_citation||row.normalized_citation,row.provenance,row.unresolved?'unresolved':'resolved'].filter(Boolean).join(' / ');const link=row.target_case_id?`<a href="/case-reader?case_id=${row.target_case_id}">Open authority</a>`:'';return infoRow(title,detail,link)}).join('')||'<div class="reader-status">No citation rows stored.</div>'}</section></div>`;const sourcesHtml=`<div class="reader-info"><section class="reader-info-section"><h3>Sources</h3>${sources.map(source=>infoRow(source.source_name||source.source_type||'Source',`${source.source_type||'unknown'} / ${source.source_id||'no source ID'}`,source.source_url?`<a href="${esc(source.source_url)}" target="_blank" rel="noreferrer">Open source</a>`:'')).join('')||'<div class="reader-status">No source records available.</div>'}</section></div>`;const unresolved=citations.filter(row=>row.unresolved);const qaHtml=`<div class="reader-info"><section class="reader-info-section"><h3>Quality snapshot</h3><div class="reader-info-metrics"><div class="reader-info-metric"><strong>${num(citations.length)}</strong><span>total rows</span></div><div class="reader-info-metric"><strong>${num(unresolved.length)}</strong><span>unresolved</span></div><div class="reader-info-metric"><strong>${citations.length?Math.round((citations.length-unresolved.length)/citations.length*100):0}%</strong><span>resolution rate</span></div><div class="reader-info-metric"><strong>${num(metadata.length)}</strong><span>metadata fields</span></div></div></section><section class="reader-info-section"><h3>Unresolved citations</h3>${unresolved.slice(0,20).map(row=>infoRow(row.citation_text||row.normalized_citation||'Citation',row.normalized_citation||'No normalized form')).join('')||'<div class="reader-status">No unresolved citation rows.</div>'}</section></div>`;const views={details,citations:citationsHtml,sources:sourcesHtml,qa:qaHtml};box.innerHTML=`<div class="reader-info-tabs"><button data-reader-tab="details">Details</button><button data-reader-tab="citations">Citations</button><button data-reader-tab="sources">Sources</button><button data-reader-tab="qa">QA</button><button data-reader-tab="intelligence">Intel</button></div><div id="decisionInfoContent" class="reader-info-content">${views[activeTab]||details}</div>`;box.querySelectorAll('[data-reader-tab]').forEach(button=>{button.classList.toggle('active',button.dataset.readerTab===activeTab);button.onclick=()=>{const tab=button.dataset.readerTab;if(tab==='intelligence'){loadCaseIntelligence(data.case.id);return}renderCaseReaderPane(data,tab)}})}
async function loadCaseIntelligence(caseId){const box=document.getElementById('decisionInfoContent');box.innerHTML='<div class="reader-status">Loading citation intelligence...</div>';try{const [signals,related,missing,suggestions]=await Promise.all([fetch(`/citation-map/cases/${caseId}/authority-signals?limit=4&context_limit=1`).then(response=>response.ok?response.json():[]),fetch(`/citation-map/cases/${caseId}/similar?limit=4&min_shared=2`).then(response=>response.ok?response.json():[]),fetch(`/citation-map/cases/${caseId}/missing-authorities?limit=4`).then(response=>response.ok?response.json():[]),fetch(`/citation-map/cases/${caseId}/completion-suggestions?limit=4`).then(response=>response.ok?response.json():[])]);const authorityRow=item=>{const authority=item.authority||{},context=(item.sample_contexts||[])[0]?.context||'';return `<div class="reader-intel-row"><strong>${esc(authority.title||authority.citation||'Authority')}</strong><small>${esc(authority.citation||'No citation')} / ${num(item.occurrence_count)} mentions across ${num(item.distinct_chunks)} sections</small>${context?`<div class="reader-intel-context">${esc(context.slice(0,260))}</div>`:''}<a href="/case-reader?case_id=${authority.case_id}">Open authority</a></div>`};const recommendationRow=item=>{const authority=item.authority||{};return `<div class="reader-intel-row"><strong>${esc(authority.title||authority.citation||'Authority')}</strong><small>${esc(authority.citation||'No citation')} / cited by ${num(item.peer_citing_cases)} peer decisions / ${Math.round(Number(item.peer_coverage||0)*100)}% peer coverage</small><a href="/case-reader?case_id=${authority.case_id}">Open authority</a></div>`};const relatedRow=item=>{const relatedCase=item.case||{};return `<div class="reader-intel-row"><strong>${esc(relatedCase.title||relatedCase.citation||'Related case')}</strong><small>${esc(relatedCase.citation||'No citation')} / ${num(item.shared_authority_count)} shared authorities</small><a href="/case-reader?case_id=${relatedCase.case_id}">Open related case</a></div>`};box.innerHTML=`<div class="reader-intel"><a class="reader-intel-action" href="/citation-map?case_id=${caseId}">Open Citation Map</a><section class="reader-intel-section"><h3>Influential Authorities</h3><p>Authorities used most distinctively in this decision.</p>${intelligenceRows(signals,authorityRow)}</section><section class="reader-intel-section"><h3>Related Cases</h3><p>Decisions sharing this case's authority pattern.</p>${intelligenceRows(related,relatedRow)}</section><section class="reader-intel-section"><h3>Peer Authority Gaps</h3><p>Authorities common among comparable decisions but absent here.</p>${intelligenceRows(missing,recommendationRow)}</section><section class="reader-intel-section"><h3>Research Suggestions</h3><p>Ranked peer-derived authorities for review, not legal recommendations.</p>${intelligenceRows(suggestions,recommendationRow)}</section></div>`}catch(error){box.innerHTML=`<div class="reader-status">${esc(error.message)}</div>`}}
function renderCaseReaderPane(data,activeTab='details'){const box=document.getElementById('decisionTarget'),caseData=data.case||{},metrics=data.metrics||{},citations=data.citations||[],sources=data.sources||[],chunks=data.chunks||[],tags=data.tags||[],metadata=data.extracted_metadata||[];const table=(heading,rows)=>`<section class="reader-info-section"><h3>${heading}</h3><table class="reader-info-table"><tbody>${rows.filter(([,value])=>value!==null&&value!==undefined&&value!=='').map(([key,value])=>`<tr><th>${esc(String(key).replaceAll('_',' '))}</th><td>${esc(Array.isArray(value)?value.join(', '):String(value))}</td></tr>`).join('')||'<tr><td colspan="2">Not recorded</td></tr>'}</tbody></table></section>`;const extracted=metadata.filter(row=>row.key!=='paragraph_marker').map(row=>[row.key,`${row.value||''}${row.source?` (${row.source})`:''}`]);const header=[['citation',caseData.citation],['court',caseData.court],['date',caseData.date],['jurisdiction',caseData.jurisdiction],['language',caseData.language],['source',caseData.source_name],['citation_rows',citations.length],['incoming_citations',metrics.in_degree],['outgoing_citations',metrics.out_degree],['pagerank',metrics.pagerank===null||metrics.pagerank===undefined?null:Number(metrics.pagerank).toFixed(5)]];const details=`<div class="reader-info">${table('Extracted metadata',extracted)}${table('Header metadata',header)}</div>`;const tagsHtml=`<div class="reader-info"><section class="reader-info-section"><h3>Tags</h3><div class="reader-info-tags">${tags.map(tag=>`<span>${esc(`${tag.category}: ${tag.value}`)}</span>`).join('')||'<span>No tags available.</span>'}</div></section></div>`;const citationsHtml=`<div class="reader-info">${citations.map(row=>`<div class="reader-info-row"><strong>${esc(row.target_title||row.citation_text||row.target_citation||'Citation')}</strong><small>${esc(row.target_citation||row.normalized_citation||'No normalized citation')} · chunk ${row.chunk_id??'-'} · ${row.offset_start??'-'}-${row.offset_end??'-'}</small></div>`).join('')||'<div class="reader-status">No citation rows stored.</div>'}</div>`;const evidenceChunks=chunks.filter(chunk=>chunk.text_length||chunk.text);const caseCitations=citations.filter(row=>row.citation_kind!=='statute');const statuteCitations=citations.filter(row=>row.citation_kind==='statute'||/\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b/i.test(String(row.normalized_citation||row.citation_text||'')));const citedChunkIds=new Set(caseCitations.concat(statuteCitations).map(row=>row.chunk_id).filter(Boolean));const evidenceHtml=`<div class="reader-info">${table('Evidence coverage',[['text_chunks',evidenceChunks.length],['text_characters',evidenceChunks.reduce((total,chunk)=>total+Number(chunk.text_length||String(chunk.text||'').length),0)],['chunks_with_citations',citedChunkIds.size],['case_citation_occurrences',caseCitations.length],['statute_citation_occurrences',statuteCitations.length],['source_records',sources.length]])}<section class="reader-info-section"><h3>Provenance records</h3>${sources.map(source=>`<div class="reader-info-row"><strong>${esc(source.source_name||source.source_type||'Source')}</strong><small>${esc(source.source_type||'')} · ${esc(source.source_id||'no source id')}</small></div>`).join('')||'<div class="reader-status">No provenance records available.</div>'}</section></div>`;const unresolved=citations.filter(row=>row.unresolved);const qaHtml=`<div class="reader-info">${table('Quality snapshot',[['citation_rows',citations.length],['unresolved_rows',unresolved.length],['metadata_fields',metadata.length]])}</div>`;const views={details,citations,evidence:evidenceHtml,qa:qaHtml,tags:tagsHtml};box.innerHTML=`<div class="reader-info-tabs"><button data-reader-tab="details">Metadata</button><button data-reader-tab="citations">Citations</button><button data-reader-tab="evidence">Evidence</button><button data-reader-tab="qa">QA</button><button data-reader-tab="intelligence">Intel</button></div><div id="decisionInfoContent" class="reader-info-content">${views[activeTab]||details}</div>`;box.querySelectorAll('[data-reader-tab]').forEach(button=>{button.classList.toggle('active',button.dataset.readerTab===activeTab);button.onclick=()=>{if(button.dataset.readerTab==='intelligence'){loadCaseIntelligence(data.case.id);return}renderCaseReaderPane(data,button.dataset.readerTab)}})}
function groupedCitationHtml(citations){const groups=new Map();(citations||[]).filter(row=>row.citation_kind!=='statute').forEach(row=>{const label=String(row.target_title||row.target_citation||row.normalized_citation||row.citation_text||'Unresolved citation').trim();const key=label.toLocaleLowerCase();const group=groups.get(key)||{label,rows:[]};group.rows.push(row);groups.set(key,group)});if(!groups.size)return '<div class="reader-status">No case-to-case citations stored for this case.</div>';return [...groups.values()].sort((a,b)=>b.rows.length-a.rows.length||a.label.localeCompare(b.label)).map(group=>`<details class="reader-citation-group"><summary><strong>${esc(group.label)}</strong><span>${num(group.rows.length)} occurrence${group.rows.length===1?'':'s'}</span></summary><div class="reader-citation-occurrences">${group.rows.map(row=>`<div class="reader-info-row"><strong>${esc(row.citation_text||row.normalized_citation||'Citation')}</strong><small>${esc(row.normalized_citation||'No normalized citation')} · chunk ${row.chunk_id??'-'} · ${row.offset_start??'-'}-${row.offset_end??'-'}${row.unresolved?' · unresolved':''}</small></div>`).join('')}</div></details>`).join('')}
const originalRenderCaseReaderPane=renderCaseReaderPane;renderCaseReaderPane=function(data,activeTab='details'){originalRenderCaseReaderPane(data,activeTab);if(activeTab==='details'){document.querySelectorAll('#decisionInfoContent .reader-info-table:first-of-type td').forEach(cell=>{cell.textContent=cell.textContent.replace(/\s+\([^)]*\)$/,'')})}if(activeTab==='citations'){const content=document.getElementById('decisionInfoContent');if(content)content.innerHTML=groupedCitationHtml(data.citations||[])}};
const legacyReaderRender=renderCaseReaderPane;renderCaseReaderPane=function(data,activeTab='details'){legacyReaderRender(data,activeTab);const tabs=document.querySelector('#decisionTarget .reader-info-tabs'),content=document.getElementById('decisionInfoContent');if(!tabs||!content)return;if(!tabs.querySelector('[data-reader-tab="activity"]')){tabs.insertAdjacentHTML('beforeend','<button data-reader-tab="activity">Activity</button>');tabs.querySelector('[data-reader-tab="activity"]').onclick=()=>renderCaseReaderPane(data,'activity')}if(activeTab!=='activity')return;content.innerHTML='<div class="reader-status">Loading FC activity...</div>';fetch(`/cases/${data.case?.id}/activity`).then(response=>response.ok?response.json():response.json().then(body=>Promise.reject(new Error(body.detail||`Request failed (${response.status})`)))).then(activity=>{const escValue=value=>esc(value??'');const formatDate=value=>value?new Date(value).toLocaleDateString('en-CA'):'Date unavailable';const rows=[];(activity.procedural_history||[]).forEach(history=>(history.entries||[]).forEach(entry=>rows.push(`<div class="reader-info-row"><strong>${escValue(entry.date||'Activity entry')}</strong><small>${escValue(entry.entry||'No activity text')} · ${escValue(history.imm_number)}</small></div>`)));(activity.activity_cases||[]).forEach(item=>(item.documents||[]).forEach(document=>rows.push(`<div class="reader-info-row"><strong>${escValue(formatDate(document.doc_dt))}</strong><small>${escValue(document.recorded_entry||'No recorded entry')} · ${escValue(item.citation||'FC activity')} · ${escValue(document.docno||document.re_no||'document')}</small></div>`)));if(!activity.imm_numbers?.length){content.innerHTML='<div class="reader-status">No IMM link is recorded for this case, so no FC activity is shown.</div>';return}content.innerHTML=`<div class="reader-info"><section class="reader-info-section"><h3>Linked Federal Court activity</h3><div class="reader-info-row"><strong>IMM link</strong><small>${escValue(activity.imm_numbers.join(', '))}</small></div>${rows.join('')||'<div class="reader-status">No stored FC activity entries for this linked case.</div>'}</section></div>`}).catch(error=>{content.innerHTML=`<div class="reader-status">Unable to load FC activity: ${esc(error.message)}</div>`})};
const infoReaderRender=renderCaseReaderPane;renderCaseReaderPane=function(data,activeTab='details'){const mappedTab=activeTab==='info'?'evidence':activeTab;infoReaderRender(data,mappedTab);const tabs=document.querySelector('#decisionTarget .reader-info-tabs'),content=document.getElementById('decisionInfoContent');if(!tabs||!content)return;const evidenceTab=tabs.querySelector('[data-reader-tab="evidence"]'),qaTab=tabs.querySelector('[data-reader-tab="qa"]');if(evidenceTab){evidenceTab.dataset.readerTab='info';evidenceTab.textContent='Info';evidenceTab.classList.toggle('active',activeTab==='info');evidenceTab.onclick=()=>renderCaseReaderPane(data,'info')}if(qaTab)qaTab.remove();
if(activeTab==='info'){const caseData=data.case||{},sourceLink=caseData.source_url?`<a href="${esc(caseData.source_url)}" target="_blank" rel="noopener noreferrer">Open original source</a>`:'No source URL recorded';content.insertAdjacentHTML('afterbegin',`<section class="reader-info-section"><h3>Record context</h3><table class="reader-info-table"><tbody><tr><th>processing status</th><td>${esc(caseData.processing_status||'Not recorded')}</td></tr><tr><th>source</th><td>${esc(caseData.source_name||caseData.source_type||'Not recorded')}<br>${sourceLink}</td></tr><tr><th>jurisdiction</th><td>${esc(caseData.jurisdiction||'Not recorded')}</td></tr><tr><th>tags</th><td>${num((data.tags||[]).length)}</td></tr></tbody></table></section>`)}}
const tagActReaderRender=renderCaseReaderPane;renderCaseReaderPane=function(data,activeTab='details'){const mappedTab=activeTab==='tags'||activeTab==='acts'? 'details':activeTab;tagActReaderRender(data,mappedTab);const tabs=document.querySelector('#decisionTarget .reader-info-tabs'),content=document.getElementById('decisionInfoContent');if(!tabs||!content)return;[['tags','Tags'],['acts','Acts / Regs']].forEach(([key,label])=>{if(tabs.querySelector(`[data-reader-tab="${key}"]`))return;tabs.insertAdjacentHTML('beforeend',`<button data-reader-tab="${key}">${label}</button>`);tabs.querySelector(`[data-reader-tab="${key}"]`).onclick=()=>renderCaseReaderPane(data,key)});if(activeTab==='tags'){const tags=data.tags||[];content.innerHTML=`<div class="reader-info"><section class="reader-info-section"><h3>Live tag candidates</h3><p class="reader-status">Generated at read time; not written to the inventory.</p>${tags.map(tag=>`<div class="reader-info-row"><strong>${esc(tag.category||'other')}: ${esc(tag.value)}</strong><small>${esc(tag.evidence||'No evidence excerpt')} · ${Math.round(Number(tag.score||0)*100)}% · ${esc(tag.source||'reader')}</small></div>`).join('')||'<div class="reader-status">No live tag candidates generated.</div>'}</section></div>`}if(activeTab==='acts'){const rows=(data.citations||[]).filter(row=>row.citation_kind==='statute'||/\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\b/i.test(String(row.normalized_citation||row.citation_text||'')));content.innerHTML=`<div class="reader-info"><section class="reader-info-section"><h3 style="color:#6b3f91">Acts / Regulations</h3><p class="reader-status">IRPA and IRPR references from stored and live statute extraction.</p>${rows.map(row=>`<div class="reader-info-row" style="border-left:3px solid #8b5bb2;padding-left:8px"><strong>${esc(row.normalized_citation||row.citation_text||'IRPA / IRPR reference')}</strong><small>${esc(row.citation_text||'')} · chunk ${row.chunk_id??'-'} · ${row.offset_start??'-'}-${row.offset_end??'-'} · ${esc(row.provenance||'reader')}</small></div>`).join('')||'<div class="reader-status">No IRPA or IRPR references found.</div>'}</section></div>`}}
const preciseReaderRender=renderCaseReaderPane;renderCaseReaderPane=function(data,activeTab='details'){preciseReaderRender(data,activeTab==='tags'||activeTab==='acts'?'details':activeTab);const tabs=document.querySelector('#decisionTarget .reader-info-tabs'),content=document.getElementById('decisionInfoContent');if(!tabs||!content)return;[['tags','Tags'],['acts','Acts / Regs']].forEach(([key,label])=>{const button=tabs.querySelector(`[data-reader-tab="${key}"]`);if(button){button.textContent=label;button.classList.toggle('active',activeTab===key);button.onclick=()=>renderCaseReaderPane(data,key)}});if(activeTab==='tags'){const tags=(data.tags||[]).filter(tag=>tag.source==='reader_keyword');content.innerHTML=`<div class="reader-info"><section class="reader-info-section"><h3>Live tag candidates</h3><p class="reader-status">Generated at read time; not written to the inventory.</p>${tags.map(tag=>`<div class="reader-info-row"><strong>${esc(tag.category||'other')}: ${esc(tag.value)}</strong><small>${esc(tag.evidence||'No evidence excerpt')} · ${Math.round(Number(tag.score||0)*100)}% · live generated</small></div>`).join('')||'<div class="reader-status">No live tag candidates generated.</div>'}</section></div>`}if(activeTab==='acts'){const rows=(data.citations||[]).filter(row=>row.provenance==='statute_references');content.innerHTML=`<div class="reader-info"><section class="reader-info-section"><h3 style="color:#6b3f91">Acts / Regulations</h3><p class="reader-status">Persisted statute-reference table rows only; live extraction is excluded.</p>${rows.map(row=>`<div class="reader-info-row" style="border-left:3px solid #8b5bb2;padding-left:8px"><strong>${esc(row.normalized_citation||row.citation_text||'IRPA / IRPR reference')}</strong><small>${esc(row.citation_text||'')} · chunk ${row.chunk_id??'-'} · ${row.offset_start??'-'}-${row.offset_end??'-'} · statute table</small></div>`).join('')||'<div class="reader-status">No persisted IRPA or IRPR references found.</div>'}</section></div>`}}
const readerState={mode:'normalized',caseId:null,payload:null};
const readerInfoObserver=new MutationObserver(()=>{const info=document.querySelector('#decisionTarget .reader-info');if(!info)return;const metadata=Array.from(info.children).find(section=>section.querySelector('h3')?.textContent==='Extracted metadata');if(metadata&&info.firstElementChild!==metadata)info.prepend(metadata)});readerInfoObserver.observe(document.body,{subtree:true,childList:true});
function renderChunkedDecision(readerData){const chunks=Array.isArray(readerData?.chunks)?readerData.chunks:[];const citations=Array.isArray(readerData?.citations)?readerData.citations:[];const byChunk=new Map();citations.forEach((row)=>{if(!row.chunk_id)return;const list=byChunk.get(row.chunk_id)||[];list.push(row);byChunk.set(row.chunk_id,list)});if(!chunks.length){return '<div class="reader-status">No chunked text is available for this case.</div>';}return chunks.map((chunk,index)=>{const text=chunk.text||'';const rows=(byChunk.get(chunk.id)||[]).map((row)=>{const start=Number(row.offset_start);const end=Number(row.offset_end);if(!Number.isFinite(start)||!Number.isFinite(end)||end<=start||start<0||end>text.length)return null;const label=row.target_citation||row.normalized_citation||row.citation_text||'Citation';return {start,end,label,statute:/\\b(?:IRPA|IRPR|Immigration and Refugee Protection Act|Immigration and Refugee Protection Regulations?)\\b/i.test(String(label))};}).filter(Boolean).sort((a,b)=>a.start-b.start||(a.statute? -1:1)||(b.statute?1:-1)||b.end-a.end);let output='';let cursor=0;rows.forEach((range)=>{if(range.start<cursor) return;output+=esc(text.slice(cursor,range.start));output+=`<mark class="${range.statute?'chunk-statute':'chunk-citation'}" title="${esc(range.label)}">${esc(text.slice(range.start,range.end))}</mark>`;cursor=range.end;});output+=esc(text.slice(cursor));return `<article class="chunk-panel"><div class="chunk-header"><strong>${esc(chunk.chunk_label||`Chunk ${index+1}`)}</strong><span>${esc(chunk.chunk_set||'Decision text')} · ${num(text.length)} chars</span></div><div class="chunk-body">${output || '<span class="reader-status">No text available.</span>'}</div></article>`;}).join('');}
function setReaderMode(mode){const nextMode=mode==='chunks'||(mode==='normalized'&&readerState.payload?.readerData)?'chunks':'normalized';readerState.mode=nextMode;document.querySelectorAll('.reader-view-button').forEach((button)=>button.classList.toggle('active',button.dataset.readerView===nextMode));const body=document.getElementById('decisionBody');if(!body||!readerState.payload)return;const {item,citations,readerData}=readerState.payload;if(nextMode==='chunks'){body.innerHTML=renderChunkedDecision(readerData||{});}else{body.innerHTML=highlightedDecision(item.full_text,citations||[]);}body.querySelectorAll('.citation-link').forEach((button)=>button.addEventListener('click',()=>{document.getElementById('decisionTargetHeading').textContent='Linked case';openLinkedCase(Number(button.dataset.targetCaseId),button.dataset.targetTitle||'Linked case')}));}
function closeDecisionReader(){document.getElementById('caseReaderPanel').hidden=true;document.getElementById('searchPanel').hidden=false;document.getElementById('searchQuery').focus();readerState.caseId=null;readerState.payload=null;readerState.mode='normalized';document.querySelectorAll('.reader-view-button').forEach((button)=>button.classList.toggle('active',button.dataset.readerView==='normalized'));}
async function openDecision(caseId){const readerPanel=document.getElementById('caseReaderPanel');const body=document.getElementById('decisionBody');document.getElementById('searchPanel').hidden=true;readerPanel.hidden=false;readerPanel.scrollIntoView({behavior:'smooth',block:'start'});body.innerHTML='<div class="reader-status">Loading full decision...</div>';document.getElementById('decisionTargetHeading').textContent='Case information';try{const [response,readerResponse]=await Promise.all([fetch(`/analytics/search/cases/${caseId}`),fetch(`/cases/${caseId}/reader-data`)]);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json(),readerData=readerResponse.ok?await readerResponse.json():null,item=data.case,metrics=data.citation_metrics;readerState.caseId=caseId;readerState.payload={item,citations:data.citations||[],readerData};document.getElementById('decisionTitle').textContent=item.title||'Untitled decision';const metaParts=[item.citation,item.court,item.date,item.judge,item.government_outcome==='won'?'Government won':item.government_outcome==='lost'?'Individual won':`${num(metrics.citation_mentions)} citation mentions`].filter(Boolean);const docket=extractDocketFromPayload(item);const fcHistoryMeta=docket?`<a class="reader-source-link" data-fc-docket="${esc(docket)}" href="/data-explorer?tab=fc-history&imm=${encodeURIComponent(docket)}">Open FC History</a>`:'';const sourceMeta=item.source_url?`<a class="reader-source-link" href="${esc(item.source_url)}" target="_blank" rel="noopener noreferrer">Case source</a>`:'';document.getElementById('decisionMeta').innerHTML=[...metaParts.map(value=>`<span class="meta-pill">${esc(value)}</span>`),sourceMeta,fcHistoryMeta].filter(Boolean).join('');if(docket){const fcInput=document.getElementById('fcImmInput');if(fcInput){fcInput.value=docket;fcInput.dataset.fcDocket=docket;}}if(readerData)renderCaseReaderPane(readerData);else document.getElementById('decisionTarget').innerHTML='<div class="reader-status">Case information is unavailable.</div>';setReaderMode(readerState.mode);}catch(error){body.innerHTML=`<div class="reader-status">${esc(error.message)}</div>`;}}
function renderJudge(data){document.getElementById('judgeSummary').innerHTML=`<span><strong>${num(data.judges.length)}</strong><br>judges with more than 100 decisions</span><span><strong>${num(data.totals.decisions)}</strong><br>decisions counted</span><span><strong>${num(data.totals.classified)}</strong><br>classified outcomes</span>`;document.getElementById('judgeRows').innerHTML=data.judges.map((item,index)=>{const classified=item.government_wins+item.individual_wins;const govWidth=classified?item.government_wins/classified*100:0;const individualWidth=classified?item.individual_wins/classified*100:0;const unknownWidth=item.decisions?item.unclassified/item.decisions*100:0;return `<tr><td class="rank">${index+1}</td><td class="group">${esc(item.judge)}</td><td class="number">${num(item.decisions)}</td><td><div class="bar"><span style="width:${govWidth}%;background:var(--blue)"></span><span style="width:${individualWidth}%;background:var(--red)"></span><span style="width:${unknownWidth}%;background:#cbd5e1"></span></div></td><td class="number">${num(item.government_wins)}</td><td class="number">${num(item.individual_wins)}</td><td class="number">${num(item.unclassified)}</td><td class="number">${classified?`${govWidth.toFixed(1)}%`:'--'}</td></tr>`}).join('')};
async function loadJudge(){try{const response=await fetch('/analytics/judge-outcomes?min_decisions=100');if(!response.ok)throw new Error(`Request failed (${response.status})`);renderJudge(await response.json())}catch(error){document.getElementById('judgeRows').innerHTML=`<tr><td colspan="8" class="empty">${esc(error.message)}</td></tr>`}}
function options(selected){return fields.map(field=>`<option value="${field.key}" ${field.key===selected?'selected':''}>${esc(field.label)}</option>`).join('')};
function paintFields(){document.getElementById('groupBy').innerHTML=options('judge');document.getElementById('splitBy').innerHTML=options('government_outcome')}
async function loadMinisters(){const response=await fetch('/analytics/search/ministers');if(!response.ok)throw new Error('Unable to load minister options');const data=await response.json();document.getElementById('ministerFilter').innerHTML=`<option value="">Any minister or government party</option>${data.ministers.map(value=>`<option value="${esc(value)}">${esc(value)}</option>`).join('')}`;}
async function loadAbout(){const response=await fetch('/api/about/stats');if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();document.getElementById('aboutSummary').innerHTML=`<span><strong>${num(data.cases)}</strong><br>decision cases</span><span><strong>${num(data.case_chunks)}</strong><br>searchable chunks</span><span><strong>${num(data.citations)}</strong><br>citation records</span><span><strong>${num(data.fc_activity_cases)}</strong><br>FC activity cases</span>`;const fields={aboutCaseCount:data.cases,aboutCaseCountTop:data.cases,aboutCaseCountLayer:data.cases,aboutChunkCount:data.case_chunks,aboutChunkCountTop:data.case_chunks,aboutChunkCountLayer:data.case_chunks,aboutCitationCount:data.citations,aboutCitationCountTop:data.citations,aboutCitationCountLayer:data.citations,aboutLinkedCitationCount:data.linked_citations,aboutLinkedCitationCountTop:data.linked_citations,aboutJudgeCount:data.judge_profiles,aboutJudgeCountTop:data.judge_profiles,aboutCaseJudgeCountTop:data.case_judge_profiles,aboutFcCaseCount:data.fc_activity_cases,aboutFcCaseCountTop:data.fc_activity_cases,aboutFcCaseCountLayer:data.fc_activity_cases,aboutFcDocumentCount:data.fc_activity_documents,aboutFcDocumentCountTop:data.fc_activity_documents,aboutFcDocumentCountLayer:data.fc_activity_documents,aboutProceduralCount:data.fc_procedural_history,aboutProceduralCountLayer:data.fc_procedural_history,aboutSourceCount:data.case_sources,aboutIngestionCount:data.ingestion_runs,aboutCitationMetricsCount:data.citation_metrics,aboutStatuteCount:data.statute_references,aboutTagCount:data.case_tags,aboutEmbeddingCount:data.case_chunk_embeddings};Object.entries(fields).forEach(([id,value])=>{const element=document.getElementById(id);if(element)element.textContent=num(value)});}
async function loadCitationIntelligence(){const box=document.getElementById('citationIntelligenceContent'),caseId=new URLSearchParams(location.search).get('case_id');if(!caseId){box.textContent='Select a case from Case Search to inspect its citation intelligence.';return}box.textContent='Loading citation intelligence...';try{const [overview,outcomes,courts,judges,statutes]=await Promise.all([fetch(`/api/citation-intelligence/${caseId}/overview`).then(response=>response.json()),fetch(`/api/citation-intelligence/${caseId}/outcomes`).then(response=>response.json()),fetch(`/api/citation-intelligence/${caseId}/courts`).then(response=>response.json()),fetch(`/api/citation-intelligence/${caseId}/judges?limit=8`).then(response=>response.json()),fetch(`/api/citation-intelligence/${caseId}/statutes?limit=8`).then(response=>response.json())]);const metrics=overview.metrics||overview;const cards=Object.entries(metrics).filter(([,value])=>typeof value==='number').slice(0,6).map(([key,value])=>`<span><strong>${num(value)}</strong><br>${esc(key.replaceAll('_',' '))}</span>`).join('');const courtRows=(courts||[]).slice(0,8).map(item=>`<div class="note-box"><strong>${esc(item.court||item.label||'Court')}</strong><span>${num(item.count||item.citations||item.decisions||0)} records</span></div>`).join('');const judgeRows=(judges||[]).slice(0,8).map(item=>`<div class="note-box"><strong>${esc(item.judge||item.name||'Judge')}</strong><span>${num(item.count||item.citations||item.decisions||0)} records</span></div>`).join('');const statuteRows=(statutes||[]).slice(0,8).map(item=>`<span class="tag neutral">${esc(item.label||item.value||item.statute||'Statute')}</span>`).join('');box.innerHTML=`<div class="summaryRows">${cards||'<span>No citation metrics available.</span>'}</div><div class="search-meta">Outcome breakdown: ${esc(JSON.stringify(outcomes))}</div><div class="bottom-tray" style="padding:12px 0 0;background:transparent;border:0"><div class="tray-panel"><div class="tray-head">Citing courts</div><div class="tray-body">${courtRows||'<span class="empty">No court data.</span>'}</div></div><div class="tray-panel"><div class="tray-head">Citing judges</div><div class="tray-body">${judgeRows||'<span class="empty">No judge data.</span>'}</div></div></div><div class="search-meta">Statute and regulation references</div><div class="result-tags">${statuteRows||'<span class="tag neutral">No statute references.</span>'}</div>`}catch(error){box.textContent=String(error)}}
async function loadJudgeProfiles(){const box=document.getElementById('judgeProfileContent');try{const response=await fetch('/api/judge-profiles?limit=100');if(!response.ok)throw new Error(`Request failed (${response.status})`);const profiles=await response.json();if(!profiles.length){box.innerHTML='<span>No canonical judge profiles are available yet. Apply migration 0014 and run the judge profile backfill.</span>';return}box.innerHTML=`<div class="results-wrap">${profiles.map(profile=>`<button class="case-result judge-profile-result" data-slug="${esc(profile.slug)}"><div class="result-title">${esc(profile.display_name)}</div><div class="result-meta">${esc(profile.primary_court||'Court not recorded')} · ${num(profile.decision_count)} decisions</div></button>`).join('')}</div>`;box.querySelectorAll('.judge-profile-result').forEach(button=>button.onclick=()=>loadJudgeProfile(button.dataset.slug))}catch(error){box.textContent=String(error)}}
async function loadJudgeProfile(slug){const box=document.getElementById('judgeProfileContent');try{const response=await fetch(`/api/judge-profiles/${encodeURIComponent(slug)}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json(),profile=data.profile,outcomes=data.outcomes||{},classified=Number(outcomes.classified||0),rate=outcomes.government_win_rate,aliases=(profile.aliases||[]).filter(alias=>alias!==profile.display_name),yearRows=(data.yearly_decisions||[]).map(item=>`<tr><td class="group">${esc(item.year)}</td><td class="number">${num(item.decisions)}</td></tr>`).join(''),decisionRows=(data.decisions||[]).slice(0,50).map(item=>`<tr><td class="group">${esc(item.title||'Untitled decision')}</td><td>${esc(item.citation||'No citation')}</td><td>${esc(item.court||'')}</td><td>${esc(item.date||'')}</td><td class="number"><button class="judge-open" type="button" data-case-id="${item.case_id}">Open</button></td></tr>`).join('');const url=new URL(location.href);url.searchParams.set('tab','judge-profile');url.searchParams.set('judge',slug);history.replaceState(null,'',url);box.innerHTML=`<div class="ci-header"><h3>${esc(profile.display_name)}</h3><p>${esc(profile.primary_court||'Court not recorded')} / ${num(data.decisions.length)} canonical linked decisions</p></div><div class="judge-profile-aliases">${aliases.length?`<div class="search-meta">Known name variants</div><div class="result-tags">${aliases.map(alias=>`<span class="tag neutral">${esc(alias)}</span>`).join('')}</div>`:''}</div><div class="judge-profile-summary"><div class="summaryRows"><span><strong>${num(data.decisions.length)}</strong><br>linked decisions</span><span><strong>${num(outcomes.government_wins)}</strong><br>government wins</span><span><strong>${num(outcomes.individual_wins)}</strong><br>individual wins</span><span><strong>${rate===null||rate===undefined?'--':`${Number(rate).toFixed(1)}%`}</strong><br>government win rate</span></div><div class="bar" title="Government wins: ${num(outcomes.government_wins)} | Individual wins: ${num(outcomes.individual_wins)} | Unclassified: ${num(outcomes.unclassified)}"><span style="width:${classified?Number(outcomes.government_wins||0)/classified*100:0}%;background:var(--blue)"></span><span style="width:${classified?Number(outcomes.individual_wins||0)/classified*100:0}%;background:var(--red)"></span><span style="width:${data.decisions.length?Number(outcomes.unclassified||0)/data.decisions.length*100:0}%;background:#cbd5e1"></span></div><div class="search-meta">Outcome rate excludes ${num(outcomes.unclassified)} unclassified decision${Number(outcomes.unclassified)===1?'':'s'}.</div></div><div class="judge-decisions"><h3>Decision volume by year</h3><p>Annual volume across the canonical profile.</p>${ciTable(['Year','Decisions'],yearRows)}<h3>Recent linked decisions</h3><p>Showing the 50 most recent of ${num(data.decisions.length)} decisions.</p>${ciTable(['Decision','Citation','Court','Date',''],decisionRows)}<button type="button" class="tab" id="backToJudgeProfiles">Back to judge profiles</button></div>`;box.querySelectorAll('.judge-open').forEach(button=>button.onclick=()=>openDecision(Number(button.dataset.caseId)));document.getElementById('backToJudgeProfiles').onclick=loadJudgeProfiles}catch(error){box.textContent=String(error)}}
async function searchCitationCases(event){event.preventDefault();const query=document.getElementById('citationCaseQuery').value.trim(),meta=document.getElementById('citationSearchMeta'),results=document.getElementById('citationSearchResults');if(!query){meta.textContent='Enter a case title.';results.innerHTML='';return}meta.textContent='Searching case titles...';try{const response=await fetch(`/api/citation-intelligence/cases?title=${encodeURIComponent(query)}&limit=12`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const cases=await response.json();meta.textContent=`Found ${num(cases.length)} matching case${cases.length===1?'':'s'}.`;results.innerHTML=cases.map(item=>`<button class="case-result citation-case-result" data-case-id="${item.case_id}"><div class="result-title">${esc(item.title)}</div><div class="result-meta">${esc(item.citation||'No citation')} · ${esc(item.court)} · ${esc(item.date)}</div></button>`).join('')||'<div class="empty">No case titles matched.</div>';results.querySelectorAll('.citation-case-result').forEach(button=>button.onclick=()=>{const url=new URL(location.href);url.searchParams.set('tab','citation-intelligence');url.searchParams.set('case_id',button.dataset.caseId);history.pushState(null,'',url);loadCitationIntelligence()})}catch(error){meta.textContent=String(error);results.innerHTML=''}}
async function searchJudgeProfiles(event){event.preventDefault();const query=document.getElementById('judgeProfileQuery').value.trim(),meta=document.getElementById('judgeProfileSearchMeta'),box=document.getElementById('judgeProfileContent');if(!query){meta.textContent='Enter a judge name.';loadJudgeProfiles();return}meta.textContent='Searching judge names...';try{const response=await fetch(`/api/judge-profiles?q=${encodeURIComponent(query)}&limit=50`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const profiles=await response.json();meta.textContent=`Found ${num(profiles.length)} matching judge${profiles.length===1?'':'s'}.`;box.innerHTML=profiles.map(profile=>`<button class="case-result judge-profile-result" data-slug="${esc(profile.slug)}"><div class="result-title">${esc(profile.display_name)}</div><div class="result-meta">${esc(profile.primary_court||'Court not recorded')} · ${num(profile.decision_count)} decisions</div></button>`).join('')||'<div class="empty">No judge profiles matched.</div>';box.querySelectorAll('.judge-profile-result').forEach(button=>button.onclick=()=>{const url=new URL(location.href);url.searchParams.set('tab','judge-profile');url.searchParams.set('judge',button.dataset.slug);history.pushState(null,'',url);loadJudgeProfile(button.dataset.slug)})}catch(error){meta.textContent=String(error)}}
const ciState={caseId:null,active:'overview',page:1};
const ciLabel=key=>({case_id:'case ID',in_degree:'incoming links',unique_citing_cases:'citing decisions',total_occurrences:'citation mentions',avg_mentions_per_case:'average mentions per decision',max_mentions_in_single_case:'most mentions in one decision'}[key]||key.replaceAll('_',' '));
const ciTable=(headers,rows)=>`<div class="table-wrap ci-table"><table><thead><tr>${headers.map(header=>`<th>${esc(header)}</th>`).join('')}</tr></thead><tbody>${rows||'<tr><td colspan="8" class="empty">No data available.</td></tr>'}</tbody></table></div>`;
const ciOutcomeLabel=key=>({government_win:'Government won',government_loss:'Individual won',mixed:'Mixed outcome',unknown:'Outcome not classified'}[key]||ciLabel(key));
function ciEvidence(data){const rows=data.rows||[];const evidence=rows.map(item=>`<article class="ci-evidence"><h3>${esc(item.case_title||'Untitled decision')}</h3><div class="result-meta">${esc(item.case_citation||'No citation')} / ${esc(item.court||'Unknown court')} / ${esc(item.date||'Date unavailable')} / ${esc(item.judge||'Judge unavailable')}</div><div class="result-tags"><span class="tag ${item.gov_outcome==='won'?'win':item.gov_outcome==='lost'?'loss':'neutral'}">${esc(item.gov_outcome==='won'?'Government won':item.gov_outcome==='lost'?'Individual won':'Outcome unclassified')}</span><span class="tag neutral">${num(item.mention_count)} mentions in decision</span></div><p><strong>Matched citation:</strong> ${esc(item.citation_text||'Stored citation text unavailable')}</p><p class="ci-quote">${esc(item.chunk_text||'No surrounding passage stored.')}</p></article>`).join('')||'<div class="empty">No citation evidence matched these filters.</div>';return `<div class="ci-header"><h3>Citation evidence</h3><p>${num(data.total)} stored citation occurrence${data.total===1?'':'s'}; showing page ${num(data.page)} of ${num(data.total_pages)}.</p></div>${evidence}<div class="ci-pager"><button type="button" id="ciPrevious" ${data.page<=1?'disabled':''}>Previous page</button><span>Page ${num(data.page)} of ${num(data.total_pages)}</span><button type="button" id="ciNext" ${data.page>=data.total_pages?'disabled':''}>Next page</button></div>`}
async function loadCitationIntelligenceView(view,page=1){const box=document.getElementById('citationIntelligenceContent');if(!ciState.caseId){box.textContent='Search for a case title above to open Citation Intelligence.';return}ciState.active=view;ciState.page=page;document.querySelectorAll('[data-ci-tab]').forEach(tab=>tab.classList.toggle('active',tab.dataset.ciTab===view));box.textContent='Loading citation intelligence...';try{const query=view==='table'?`?page=${page}&page_size=25`:'';const response=await fetch(`/api/citation-intelligence/${ciState.caseId}/${view}${query}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();if(view==='overview'){const metrics=data.metrics||data;const metricKeys=['unique_citing_cases','total_occurrences','avg_mentions_per_case','max_mentions_in_single_case'];box.innerHTML=`<div class="ci-header"><h3>${esc(data.title||'Selected authority')}</h3><p>${esc(data.citation||'No neutral citation')} / ${esc(data.court||'Court unavailable')} / cited from ${esc(data.first_citation_date||'unknown')} to ${esc(data.most_recent_citation_date||'unknown')}</p></div><div class="summaryRows">${metricKeys.filter(key=>metrics[key]!==undefined).map(key=>`<span><strong>${num(metrics[key])}</strong><br>${esc(ciLabel(key))}</span>`).join('')}</div>`}else if(view==='timeline'){box.innerHTML=`<div class="ci-header"><h3>Use over time</h3><p>Distinct citing decisions and total citation mentions by year.</p></div>${ciTable(['Year','Citing decisions','Citation mentions'],data.map(item=>`<tr><td class="group">${esc(item.year)}</td><td class="number">${num(item.citing_cases)}</td><td class="number">${num(item.occurrences)}</td></tr>`).join(''))}` }else if(view==='outcomes'){const keys=['government_win','government_loss','mixed','unknown'];const total=data.total_cases||0;box.innerHTML=`<div class="ci-header"><h3>Outcomes in citing decisions</h3><p>Outcome coding for ${num(total)} decisions that cite this authority.</p></div><div class="summaryRows">${keys.map(key=>`<span><strong>${num(data[key])}</strong><br>${esc(ciOutcomeLabel(key))} (${Number(data[`${key}_pct`]||0).toFixed(1)}%)</span>`).join('')}</div><div class="table-wrap ci-table"><div class="bar">${keys.map((key,index)=>`<span style="width:${Number(data[`${key}_pct`]||0)}%;background:${['var(--blue)','var(--red)','var(--amber)','#cbd5e1'][index]}"></span>`).join('')}</div></div>`}else if(view==='courts'){box.innerHTML=`<div class="ci-header"><h3>Courts citing this authority</h3><p>Where this authority appears across the decision set.</p></div>${ciTable(['Court','Citing decisions','Mentions','Share of decisions'],data.map(item=>`<tr><td class="group">${esc(item.court||'Unknown')}</td><td class="number">${num(item.case_count)}</td><td class="number">${num(item.occurrences)}</td><td class="number">${Number(item.pct||0).toFixed(1)}%</td></tr>`).join(''))}` }else if(view==='judges'){box.innerHTML=`<div class="ci-header"><h3>Judges citing this authority</h3><p>Leading judges by distinct decisions, with first and latest recorded use.</p></div>${ciTable(['Judge','Decisions','Mentions','First use','Latest use'],data.map(item=>`<tr><td class="group">${esc(item.judge||'Unknown')}</td><td class="number">${num(item.case_count)}</td><td class="number">${num(item.occurrences)}</td><td>${esc(item.first_use||'-')}</td><td>${esc(item.latest_use||'-')}</td></tr>`).join(''))}` }else if(view==='companions'){box.innerHTML=`<div class="ci-header"><h3>Frequently co-cited authorities</h3><p>Authorities that appear in the same citing decisions.</p></div>${ciTable(['Authority','Citation','Shared citing decisions'],data.map(item=>`<tr><td class="group">${esc(item.authority_title||'Unknown')}</td><td>${esc(item.authority_citation||'No citation')}</td><td class="number">${num(item.shared_citing_cases)}</td></tr>`).join(''))}` }else if(view==='statutes'){box.innerHTML=`<div class="ci-header"><h3>Statutes and regulations</h3><p>Extracted legislative references from decisions citing this authority.</p></div>${ciTable(['Provision','Citing decisions','Mentions'],data.map(item=>`<tr><td class="group">${esc(item.label||'Unknown')}</td><td class="number">${num(item.case_count)}</td><td class="number">${num(item.occurrences)}</td></tr>`).join(''))}` }else{box.innerHTML=ciEvidence(data);document.getElementById('ciPrevious')?.addEventListener('click',()=>loadCitationIntelligenceView('table',data.page-1));document.getElementById('ciNext')?.addEventListener('click',()=>loadCitationIntelligenceView('table',data.page+1));}}catch(error){box.textContent=String(error)}}
async function loadCitationTimeline(){const box=document.getElementById('citationIntelligenceContent');ciState.active='timeline';document.querySelectorAll('[data-ci-tab]').forEach(tab=>tab.classList.toggle('active',tab.dataset.ciTab==='timeline'));box.textContent='Loading citation timeline...';try{const response=await fetch(`/api/citation-intelligence/${ciState.caseId}/timeline`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();if(!data.length){box.innerHTML='<div class="empty">No timeline data available.</div>';return}const width=760,height=270,left=54,right=54,top=24,bottom=42,plotWidth=width-left-right,plotHeight=height-top-bottom,maxCases=Math.max(...data.map(item=>Number(item.citing_cases)||0),1),maxOccurrences=Math.max(...data.map(item=>Number(item.occurrences)||0),1),x=index=>left+(data.length===1?plotWidth/2:index*plotWidth/(data.length-1)),y=(value,max)=>top+plotHeight-(Number(value)||0)/max*plotHeight,casePath=data.map((item,index)=>`${index?'L':'M'}${x(index).toFixed(1)},${y(item.citing_cases,maxCases).toFixed(1)}`).join(' '),occurrencePath=data.map((item,index)=>`${index?'L':'M'}${x(index).toFixed(1)},${y(item.occurrences,maxOccurrences).toFixed(1)}`).join(' '),grid=[0,.25,.5,.75,1].map(step=>{const yy=top+plotHeight*(1-step);return `<line class="ci-chart-grid" x1="${left}" y1="${yy}" x2="${width-right}" y2="${yy}"/><text class="ci-chart-label" x="${left-8}" y="${yy+4}" text-anchor="end">${num(Math.round(maxCases*step))}</text><text class="ci-chart-label" x="${width-right+8}" y="${yy+4}">${num(Math.round(maxOccurrences*step))}</text>`}).join(''),years=data.map((item,index)=>`<text class="ci-chart-label" x="${x(index)}" y="${height-16}" text-anchor="middle">${esc(item.year)}</text>`).join(''),dots=(key,max,color)=>data.map((item,index)=>`<circle class="ci-chart-dot" cx="${x(index)}" cy="${y(item[key],max)}" r="4" fill="${color}"><title>${esc(item.year)}: ${num(item[key])}</title></circle>`).join('');box.innerHTML=`<div class="ci-header"><h3>Use over time</h3><p>Trends in distinct citing decisions and total mentions. Hover a point for its exact value.</p></div><div class="ci-chart-legend"><span><i style="background:var(--blue)"></i>Citing decisions (left axis)</span><span><i style="background:var(--green)"></i>Citation mentions (right axis)</span></div><svg class="ci-chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="Citation trend over time">${grid}<path class="ci-chart-line" d="${casePath}" stroke="var(--blue)"/><path class="ci-chart-line" d="${occurrencePath}" stroke="var(--green)"/>${dots('citing_cases',maxCases,'var(--blue)')}${dots('occurrences',maxOccurrences,'var(--green)')}${years}</svg>${ciTable(['Year','Citing decisions','Citation mentions'],data.map(item=>`<tr><td class="group">${esc(item.year)}</td><td class="number">${num(item.citing_cases)}</td><td class="number">${num(item.occurrences)}</td></tr>`).join(''))}` }catch(error){box.textContent=String(error)}}
async function loadCitationIntelligence(){const caseId=new URLSearchParams(location.search).get('case_id');ciState.caseId=caseId;document.querySelectorAll('[data-ci-tab]').forEach(tab=>tab.onclick=()=>tab.dataset.ciTab==='timeline'?loadCitationTimeline():loadCitationIntelligenceView(tab.dataset.ciTab));if(ciState.active==='timeline')await loadCitationTimeline();else await loadCitationIntelligenceView(ciState.active)}
function renderFcActivityTimeline(data){const totalRows=data.total_rows||data.rows||[],selectedCity=data.city||'',provinceRows=data.province_rows||[],series=selectedCity?[{label:selectedCity,rows:data.rows||[],color:'var(--green)'}].concat([{label:'All locations',rows:totalRows,color:'var(--text)'}]):provinceRows.map((item,index)=>({label:item.province,rows:item.rows,color:['var(--blue)','var(--green)','var(--amber)','var(--red)','var(--purple)'][index%5]})).concat([{label:'All locations',rows:totalRows,color:'var(--text)'}]),box=document.getElementById('fcActivityChart');if(!totalRows.length){box.innerHTML='<div class="empty">No FC activity cases match this location.</div>';return}const width=900,height=340,left=62,right=18,top=28,bottom=58,plotWidth=width-left-right,plotHeight=height-top-bottom,maxCount=Math.max(...series.flatMap(item=>item.rows.map(row=>Number(row.count)||0)),1),years=totalRows.map(item=>item.year),x=index=>left+(years.length===1?plotWidth/2:index*plotWidth/(years.length-1)),y=value=>top+plotHeight-(Number(value)||0)/maxCount*plotHeight,grid=[0,.25,.5,.75,1].map(step=>{const yy=top+plotHeight*(1-step);return `<line class="ci-chart-grid" x1="${left}" y1="${yy}" x2="${width-right}" y2="${yy}"/><text class="ci-chart-label" x="${left-8}" y="${yy+4}" text-anchor="end">${num(Math.round(maxCount*step))}</text>`}).join(''),axisLabels=years.map((year,index)=>index%3===0||index===years.length-1?`<text class="ci-chart-label" x="${x(index)}" y="${height-20}" text-anchor="middle">${esc(year)}</text>`:'').join(''),lineFor=(item,index)=>{const path=item.rows.map((row,rowIndex)=>`${rowIndex?'L':'M'}${x(rowIndex).toFixed(1)},${y(row.count).toFixed(1)}`).join(' ');const dots=item.rows.map((row,rowIndex)=>`<circle class="ci-chart-dot" cx="${x(rowIndex)}" cy="${y(row.count)}" r="${item.label==='All locations'?5:3}" fill="${item.color}"><title>${esc(item.label)} / ${esc(row.year)}: ${num(row.count)} cases</title></circle>`).join('');return `<path class="ci-chart-line" d="${path}" stroke="${item.color}" stroke-width="${item.label==='All locations'?4:2}" opacity="${item.label==='All locations'?1:.72}"/>${dots}`};const legend=series.map(item=>`<span class="key"><i class="dot" style="background:${item.color}"></i>${esc(item.label)}</span>`).join('');const tableRows=totalRows.map((item,index)=>`<tr><td class="group">${esc(item.year)}</td>${series.map(seriesItem=>`<td class="number">${num(seriesItem.rows[index]?.count||0)}</td>`).join('')}</tr>`).join('');box.innerHTML=`<div class="ci-chart-legend">${legend}</div><svg class="ci-chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="Federal Court cases filed by province and total">${grid}${series.map(lineFor).join('')}${axisLabels}</svg>${ciTable(['Year',...series.map(item=>item.label)],tableRows)}`}
async function loadFcActivityTimeline(){const city=document.getElementById('fcActivityCity').value,params=city?`?city=${encodeURIComponent(city)}`:'';const meta=document.getElementById('fcActivityMeta');meta.textContent='Loading FC activity totals...';try{const response=await fetch(`/api/fc-activity/timeline${params}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);const data=await response.json();const select=document.getElementById('fcActivityCity');if(!select.dataset.loaded){const groups={};data.cities.forEach(value=>{const province=data.city_provinces[value]||'Other';(groups[province] ||= []).push(value)});select.innerHTML='<option value="">All locations / provinces</option>'+Object.keys(groups).sort().map(province=>`<optgroup label="${esc(province)}">${groups[province].sort().map(value=>`<option value="${esc(value)}">${esc(value)}</option>`).join('')}</optgroup>`).join('');select.dataset.loaded='true';}meta.textContent=`${num(data.total)} cases across ${city||'all provinces'}.`;renderFcActivityTimeline(data)}catch(error){meta.textContent=String(error);document.getElementById('fcActivityChart').innerHTML='<div class="empty">Unable to load FC activity totals.</div>'}}
document.getElementById('fcActivityCity')?.addEventListener('change',loadFcActivityTimeline);loadFcActivityTimeline();
function render(data){const splitLabel=data.split_by.label;const colors=Object.fromEntries(data.split_values.map((value,index)=>[value,palette[index%palette.length]]));document.getElementById('summary').innerHTML=`<span><strong>${num(data.totals.decisions)}</strong><br>decisions counted</span><span><strong>${num(data.groups.length)}</strong><br>${esc(data.group_by.label.toLowerCase())} results shown</span>`;document.getElementById('legend').innerHTML=data.split_values.map(value=>`<span class="key"><i class="dot" style="background:${colors[value]}"></i>${esc(value)}</span>`).join('');document.getElementById('head').innerHTML=`<tr><th>#</th><th>${esc(data.group_by.label)}</th><th>Decisions</th><th>${esc(splitLabel)} split</th>${data.split_values.map(value=>`<th class="number">${esc(value)}</th>`).join('')}</tr>`;document.getElementById('rows').innerHTML=data.groups.map((item,index)=>{const bar=data.split_values.map(value=>{const count=item.breakdown[value]||0;return `<span style="width:${item.decisions?count/item.decisions*100:0}%;background:${colors[value]}" title="${esc(value)}: ${num(count)}"></span>`}).join('');return `<tr><td class="rank">${index+1}</td><td class="group">${esc(item.value)}</td><td class="number">${num(item.decisions)}</td><td><div class="bar">${bar}</div></td>${data.split_values.map(value=>`<td class="number">${num(item.breakdown[value]||0)}</td>`).join('')}</tr>`}).join('')||'<tr><td class="empty">No matching decision data.</td></tr>'};
async function load(){const groupBy=document.getElementById('groupBy').value,splitBy=document.getElementById('splitBy').value,limit=document.getElementById('limit').value;document.getElementById('rows').innerHTML='<tr><td class="empty">Loading analytics...</td></tr>';try{const response=await fetch(`/analytics/explorer?group_by=${encodeURIComponent(groupBy)}&split_by=${encodeURIComponent(splitBy)}&limit=${encodeURIComponent(limit)}`);if(!response.ok)throw new Error(`Request failed (${response.status})`);render(await response.json())}catch(error){document.getElementById('rows').innerHTML=`<tr><td class="empty">${esc(error.message)}</td></tr>`}}
(async()=>{const response=await fetch('/analytics/explorer?limit=1');if(!response.ok)throw new Error('Unable to load available fields');const data=await response.json();fields=data.fields;paintFields();await loadMinisters();document.getElementById('apply')?.addEventListener('click', load);document.getElementById('caseSearch').onsubmit=loadSearch;document.getElementById('searchSort').value='newest';loadSearch();const advancedButton=document.getElementById('toggleAdvancedSearch'),advancedOptions=document.getElementById('advancedSearchOptions');advancedButton.onclick=()=>{const expanded=advancedOptions.hidden;advancedOptions.hidden=!expanded;advancedButton.setAttribute('aria-expanded',String(expanded));advancedButton.textContent=expanded?'Hide advanced options':'Advanced options';};document.getElementById('clearSearch').onclick=()=>{document.getElementById('caseSearch').reset();advancedOptions.hidden=true;advancedButton.setAttribute('aria-expanded','false');advancedButton.textContent='Advanced options';document.getElementById('searchMeta').textContent='Search by case name or citation. Open Advanced options for filters or full-decision text.';document.getElementById('searchResults').innerHTML='';};const selectTab=active=>{const panels={about:'aboutPanel',search:'searchPanel','citation-intelligence':'citationIntelligencePanel',judge:'judgePanel','judge-profile':'judgeProfilePanel',explorer:'explorerPanel','fc-history':'fcHistoryPanel'};const normalized=active==='data-explorer'?'explorer':active==='judge-outcomes'?'judge':active;const selected=panels[normalized]?normalized:'search';Object.entries(panels).forEach(([key,id])=>{const panel=document.getElementById(id);if(panel)panel.hidden=key!==selected});document.getElementById('judgePanel').hidden=selected!=='judge';document.querySelectorAll('[data-tab]').forEach(item=>item.classList.toggle('active',item.dataset.tab===selected));history.replaceState(null,'',`/data-explorer?tab=${encodeURIComponent(selected)}${new URLSearchParams(location.search).get('case_id')?`&case_id=${encodeURIComponent(new URLSearchParams(location.search).get('case_id'))}`:''}`);if(selected==='about')loadAbout();if(selected==='citation-intelligence')loadCitationIntelligence();if(selected==='judge')loadJudge();if(selected==='judge-profile')loadJudgeProfiles();if(selected==='explorer')load();};document.querySelectorAll('[data-tab]').forEach(tab=>tab.onclick=()=>selectTab(tab.dataset.tab));const initialTab=new URLSearchParams(location.search).get('tab')||'search';selectTab(initialTab);})().catch(error=>document.getElementById('searchMeta').textContent=String(error));
</script>
<script>
const requestedTab=new URLSearchParams(location.search).get('tab');const requestedImm=new URLSearchParams(location.search).get('imm');const fcImmInput=document.getElementById('fcImmInput');const setFcHistoryInput=(docket)=>{if(!fcImmInput) return false;const normalized=(docket||'').trim();if(!normalized)return false;fcImmInput.value=normalized;fcImmInput.dataset.fcDocket=normalized;return true;};if(requestedTab==='judge-profile'){history.replaceState(null,'',`/data-explorer?tab=judge-profile${new URLSearchParams(location.search).get('judge')?`&judge=${encodeURIComponent(new URLSearchParams(location.search).get('judge'))}`:''}`);document.getElementById('searchPanel').hidden=true;document.getElementById('judgeProfilePanel').hidden=false;loadJudgeProfiles().then(()=>{const judge=new URLSearchParams(location.search).get('judge');if(judge)loadJudgeProfile(judge)});}if(requestedTab==='fc-history'){document.querySelectorAll('[data-tab]').forEach(tab=>tab.classList.toggle('active',tab.dataset.tab==='fc-history'));const panels={about:'aboutPanel',search:'searchPanel','citation-intelligence':'citationIntelligencePanel',judge:'judgePanel','judge-profile':'judgeProfilePanel',explorer:'explorerPanel','fc-history':'fcHistoryPanel'};Object.entries(panels).forEach(([key,id])=>{const panel=document.getElementById(id);if(panel)panel.hidden=key!=='fc-history'});if(requestedImm){setFcHistoryInput(requestedImm);document.getElementById('fcHistoryForm').dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));}}document.querySelectorAll('[data-tab]').forEach(tab=>tab.addEventListener('click',()=>{const active=tab.dataset.tab;const panels={about:'aboutPanel',search:'searchPanel','citation-intelligence':'citationIntelligencePanel',judge:'judgePanel','judge-profile':'judgeProfilePanel',explorer:'explorerPanel','fc-history':'fcHistoryPanel'};const selected=panels[active]?active:'search';Object.entries(panels).forEach(([key,id])=>{const panel=document.getElementById(id);if(panel)panel.hidden=key!==selected});if(selected==='judge')document.getElementById('judgePanel').hidden=false;if(selected==='judge-profile')loadJudgeProfiles();if(selected==='fc-history'&& fcImmInput){const docket=fcImmInput.dataset.fcDocket||fcImmInput.value.trim();if(docket){fcImmInput.value=docket;fcImmInput.dataset.fcDocket=docket;}}}));document.getElementById('citationIntelligenceSearch').onsubmit=searchCitationCases;document.getElementById('judgeProfileSearch').onsubmit=searchJudgeProfiles;document.getElementById('fcHistoryForm').onsubmit=async (event)=>{event.preventDefault();const imm=document.getElementById('fcImmInput').value.trim();const meta=document.getElementById('fcHistoryMeta');const results=document.getElementById('fcHistoryResults');if(!imm){meta.textContent='Enter an IMM number first.';return;}meta.textContent='Fetching Federal Court history...';results.innerHTML='<div class="empty">Loading...</div>';try{const response=await fetch(`/api/fc-history?imm=${encodeURIComponent(imm)}`);if(!response.ok){throw new Error((await response.json()).detail || `Request failed (${response.status})`);}const data=await response.json();const entries=(data.entries_json||[]).map((item,index)=>`<div class="note-box"><strong>${esc(item.date||`Entry ${index+1}`)}</strong><span>${esc(item.entry||'No entry text')}</span></div>`).join('') || '<div class="empty">No recorded activity entries.</div>';results.innerHTML=`<div class="summaryRows"><span><strong>${esc(data.imm_number||imm)}</strong><br>IMM number</span><span><strong>${esc(data.case_status||'Unknown')}</strong><br>status</span><span><strong>${esc(data.leave_decision||'N/A')}</strong><br>leave decision</span><span><strong>${esc(data.jr_decision||'N/A')}</strong><br>JR decision</span></div><div class="search-meta">Judge: ${esc(data.judge||'Not recorded')} · Style of cause: ${esc(data.style_of_cause||'Not recorded')}</div><div class="results-wrap">${entries}</div>`;meta.textContent=`Fetched Federal Court history for ${esc(data.imm_number||imm)}.`;}catch(error){meta.textContent=String(error);results.innerHTML='<div class="empty">Unable to fetch FC history.</div>';}};const initialTab=new URLSearchParams(location.search).get('tab');if(initialTab==='judge-profile'){document.getElementById('searchPanel').hidden=true;document.getElementById('judgeProfilePanel').hidden=false;loadJudgeProfiles();}else if(initialTab==='judge-outcomes'){document.getElementById('searchPanel').hidden=true;document.getElementById('judgePanel').hidden=false;loadJudge();}else if(initialTab==='fc-history'){document.getElementById('searchPanel').hidden=true;document.getElementById('fcHistoryPanel').hidden=false;}
document.querySelectorAll('[data-tab]').forEach(tab=>tab.addEventListener('click',()=>{document.getElementById('caseReaderPanel').hidden=true;}));
document.querySelectorAll('[data-reader-info-tab]').forEach((button)=>button.addEventListener('click',()=>{if(!readerState.payload)return;renderCaseReaderPane(readerState.payload,button.dataset.readerInfoTab);}));
document.querySelectorAll('.reader-view-button').forEach((button)=>button.addEventListener('click',()=>setReaderMode(button.dataset.readerView)));
</script>
</body>
</html>
"""



@router.get("/data-explorer", response_class=HTMLResponse, include_in_schema=False)
def data_explorer_page() -> HTMLResponse:
	return HTMLResponse(content=_data_explorer_page_html(), status_code=status.HTTP_200_OK)


@router.get("/analytics/explorer", response_model=dict[str, Any])
def get_data_explorer(
	group_by: str = "judge",
	split_by: str = "government_outcome",
	limit: int = 50,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	if group_by not in _ANALYTICS_FIELDS or split_by not in _ANALYTICS_FIELDS:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported analytics field")
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


@router.get("/api/about/stats", response_model=dict[str, int], include_in_schema=False)
def about_stats(db: Session = Depends(get_db)) -> dict[str, int]:
	return {
		"cases": int(db.scalar(select(func.count(Case.id))) or 0),
		"case_chunks": int(db.scalar(select(func.count(CaseChunk.id))) or 0),
		"case_sources": int(db.scalar(select(func.count(CaseSource.id))) or 0),
		"ingestion_runs": int(db.scalar(select(func.count(IngestionRun.id))) or 0),
		"citations": int(db.scalar(select(func.count(Citation.id))) or 0),
		"linked_citations": int(
			db.scalar(select(func.count(Citation.id)).where(Citation.target_case_id.is_not(None))) or 0
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


@router.get("/api/fc-history", response_model=dict[str, Any], include_in_schema=False)
def fetch_fc_history(imm: str, db: Session = Depends(get_db)) -> dict[str, Any]:
	normalized = (imm or "").strip().upper()
	if not normalized or not re.fullmatch(r"IMM-\d{1,6}-\d{2,4}", normalized, flags=re.IGNORECASE):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Provide an IMM number like IMM-1234-19.")
	try:
		with httpx.Client(headers=HEADERS, follow_redirects=True) as client:
			result = process_imm(client, normalized)
		upsert_result(db, result)
		return result
	except Exception as exc:  # pragma: no cover - network-limited runtime path
		raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Could not fetch FC history: {exc}")


@router.get("/api/fc-activity/timeline", response_model=dict[str, Any], include_in_schema=False)
def fc_activity_timeline(city: str = "", db: Session = Depends(get_db)) -> dict[str, Any]:
	"""Return yearly FC activity counts by province and total, optionally focused on a city."""
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
		province_counts.setdefault(province, {})[year] = province_counts.setdefault(province, {}).get(year, 0) + int(row.count)
		total_counts[year] = total_counts.get(year, 0) + int(row.count)
	years = sorted(total_counts)
	def timeline(counts: dict[int, int]) -> list[dict[str, int]]:
		return [{"year": year, "count": counts.get(year, 0)} for year in years]
	province_rows = [
		{"province": province, "rows": timeline(province_counts[province])}
		for province in sorted(province_counts)
	]
	selected_rows = timeline(city_counts.get(selected_city, {})) if selected_city else timeline(total_counts)
	return {
		"city": selected_city or None,
		"cities": list(cities),
		"city_provinces": FC_CITY_PROVINCE,
		"total": sum(total_counts.values()) if not selected_city else sum(row["count"] for row in selected_rows),
		"rows": selected_rows,
		"total_rows": timeline(total_counts),
		"province_rows": province_rows,
	}


@router.get("/api/citation-intelligence/search", response_model=list[dict[str, Any]], include_in_schema=False)
def citation_intelligence_search(
	q: str = "",
	limit: int = 12,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _search_citation_cases(db, q, limit=max(1, min(50, limit)))


@router.get("/api/citation-intelligence/cases", response_model=list[dict[str, Any]], include_in_schema=False)
def citation_intelligence_cases(
	title: str = "",
	limit: int = 12,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	term = title.strip()
	if not term:
		return []
	rows = db.scalars(
		select(Case)
		.where(Case.title.ilike(f"%{term}%"))
		.order_by(Case.date.desc(), Case.id.desc())
		.limit(max(1, min(50, limit)))
	)
	return [
		{
			"case_id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
		}
		for case in rows
	]


@router.get("/api/citation-intelligence/{case_id}/overview", include_in_schema=False)
def citation_intelligence_overview(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	_get_case_or_404(case_id, db)
	return _ci_overview(db, case_id)


@router.get("/api/citation-intelligence/{case_id}/timeline", include_in_schema=False)
def citation_intelligence_timeline(case_id: int, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _ci_timeline(db, case_id)


@router.get("/api/citation-intelligence/{case_id}/outcomes", include_in_schema=False)
def citation_intelligence_outcomes(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	_get_case_or_404(case_id, db)
	return _ci_outcomes(db, case_id)


@router.get("/api/citation-intelligence/{case_id}/courts", include_in_schema=False)
def citation_intelligence_courts(case_id: int, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _ci_courts(db, case_id)


@router.get("/api/citation-intelligence/{case_id}/judges", include_in_schema=False)
def citation_intelligence_judges(case_id: int, limit: int = 30, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _ci_judges(db, case_id, max(1, min(100, limit)))


@router.get("/api/citation-intelligence/{case_id}/statutes", include_in_schema=False)
def citation_intelligence_statutes(case_id: int, limit: int = 25, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _ci_statutes(db, case_id, max(1, min(100, limit)))


@router.get("/api/citation-intelligence/{case_id}/companions", include_in_schema=False)
def citation_intelligence_companions(case_id: int, limit: int = 20, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _co_cited_authorities(db, case_id, max(1, min(100, limit)))


@router.get("/api/citation-intelligence/{case_id}/table", include_in_schema=False)
def citation_intelligence_table(
	case_id: int,
	page: int = 1,
	page_size: int = 50,
	year: int | None = None,
	court: str | None = None,
	judge: str | None = None,
	gov_outcome: str | None = None,
	min_mentions: int = 1,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	_get_case_or_404(case_id, db)
	return _ci_table(
		db,
		case_id,
		page=max(1, page),
		page_size=max(1, min(200, page_size)),
		year=year,
		court=court,
		judge=judge,
		gov_outcome=gov_outcome,
		min_mentions=max(1, min_mentions),
	)


@router.get("/api/judge-profiles", response_model=list[dict[str, Any]], include_in_schema=False)
def judge_profiles(q: str = "", limit: int = 50, db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	term = q.strip()
	if term:
		pattern = f"%{term}%"
		statement = select(JudgeProfile).where(
			or_(JudgeProfile.display_name.ilike(pattern), JudgeProfile.normalized_name.ilike(pattern))
		).order_by(JudgeProfile.display_name)
		rows = list(db.scalars(statement))
		ordered = sorted(rows, key=lambda row: (-len(row.case_links), row.display_name.lower()))[: max(1, min(100, limit))]
	else:
		rows = list(db.scalars(select(JudgeProfile)))
		ordered = sorted(rows, key=lambda row: (-len(row.case_links), row.display_name.lower()))[: max(1, min(100, limit))]
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


@router.get("/api/judge-profiles/{slug}", response_model=dict[str, Any], include_in_schema=False)
def judge_profile(slug: str, db: Session = Depends(get_db)) -> dict[str, Any]:
	profile = db.scalar(select(JudgeProfile).where(JudgeProfile.slug == slug))
	if profile is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Judge profile not found")
	cases = [link.case for link in profile.case_links]
	government_wins = 0
	individual_wins = 0
	unclassified = 0
	years: dict[str, int] = {}
	for case in cases:
		raw_metadata = case.metadata_json
		metadata: dict[str, Any] = raw_metadata if isinstance(raw_metadata, dict) else {}
		reader_value = metadata.get("reader_extracted")
		reader: dict[str, Any] = reader_value if isinstance(reader_value, dict) else {}
		outcome = reader.get("government outcome")
		if outcome == "won":
			government_wins += 1
		elif outcome == "lost":
			individual_wins += 1
		else:
			unclassified += 1
		if case.date:
			year = str(case.date)[:4]
			years[year] = years.get(year, 0) + 1
	classified = government_wins + individual_wins
	outcomes = {
		"government_wins": government_wins,
		"individual_wins": individual_wins,
		"unclassified": unclassified,
		"classified": classified,
		"government_win_rate": (
			round(government_wins / classified * 100, 1)
			if classified
			else None
		),
	}
	return {
		"profile": {
			"slug": profile.slug,
			"display_name": profile.display_name,
			"primary_court": profile.primary_court,
			"aliases": profile.aliases or [],
		},
		"outcomes": outcomes,
		"yearly_decisions": [
			{"year": year, "decisions": decisions}
			for year, decisions in sorted(years.items())
		],
		"decisions": [
			{"case_id": case.id, "title": case.title, "citation": case.citation, "court": case.court, "date": case.date}
			for case in sorted(cases, key=lambda item: item.date, reverse=True)
		],
	}


@router.get("/about", include_in_schema=False)
def about_page() -> RedirectResponse:
	return RedirectResponse(url="/data-explorer?tab=about", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/citation-intelligence", include_in_schema=False)
def citation_intelligence_page() -> RedirectResponse:
	return RedirectResponse(url="/data-explorer?tab=citation-intelligence", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/judges", include_in_schema=False)
def judges_page() -> RedirectResponse:
	return RedirectResponse(url="/data-explorer?tab=judge-profile", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/fc-history", include_in_schema=False)
def fc_history_page() -> RedirectResponse:
	return RedirectResponse(url="/data-explorer?tab=fc-history", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/judges/{slug}", include_in_schema=False)
def judge_profile_page(slug: str) -> RedirectResponse:
	return RedirectResponse(url=f"/data-explorer?tab=judge-profile&judge={slug}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


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
		return (f"COALESCE({minister_expression}, 'Unknown') ASC, c.date DESC NULLS LAST, c.id DESC", params)
	return ("c.date DESC NULLS LAST, c.id DESC", params)


@router.get("/analytics/search/cases", response_model=dict[str, Any])
def search_analytics_cases(
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
	db: Session = Depends(get_db),
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
		if cites else "0"
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


@router.get("/analytics/search/ministers", response_model=dict[str, list[str]])
def get_analytics_search_ministers(db: Session = Depends(get_db)) -> dict[str, list[str]]:
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


@router.get("/analytics/search/cases/{case_id}", response_model=dict[str, Any])
def get_analytics_search_case(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)
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
	chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(CaseChunk.id.in_(chunk_ids))
			.order_by(CaseChunk.chunk_index, CaseChunk.id)
		)
	) if chunk_ids else []
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
	resolved_target_cases = {citation.target_case_id for citation in citation_rows if citation.target_case_id is not None}
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


def _citation_pass_page_html() -> str:
	return r"""<!doctype html>
<html lang=\"en\">
<head>
	<meta charset=\"utf-8\">
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
	<title>Citation Pass | AI CaseLibrary</title>
	<style>
		:root{
			--bg:#eef2f6;
			--panel:#ffffff;
			--panel-2:#f8fafc;
			--text:#16202a;
			--muted:#5f6b78;
			--line:#d7dfe8;
			--accent:#2457d6;
			--accent-2:#6a7dff;
			--accent-soft:#e8efff;
			--gold:#f5b942;
			--shadow:0 18px 50px rgba(22,32,42,.08);
		}
		*{box-sizing:border-box}
		body{margin:0;color:var(--text);background:
			radial-gradient(circle at top left, rgba(36,87,214,.12), transparent 34%),
			radial-gradient(circle at top right, rgba(106,125,255,.10), transparent 26%),
			linear-gradient(180deg,#f4f7fb 0%, #eef2f6 34%, #edf1f6 100%);
			font-family:"Trebuchet MS","Segoe UI",sans-serif}
		.shell{display:grid;grid-template-rows:auto 1fr;min-height:100vh}
		.hero{position:relative;overflow:hidden;padding:22px 28px 18px;border-bottom:1px solid rgba(215,223,232,.85);background:rgba(255,255,255,.76);backdrop-filter:blur(12px)}
		.hero::after{content:"";position:absolute;inset:auto -40px -90px auto;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle, rgba(36,87,214,.14), transparent 70%);pointer-events:none}
		.hero-top{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}
		.kicker{text-transform:uppercase;letter-spacing:.14em;font-size:11px;font-weight:700;color:var(--accent);margin:0 0 8px}
		h1{margin:0;font-size:30px;line-height:1.05;font-family:Georgia,serif;letter-spacing:-.02em}
		.hero-copy{max-width:760px;margin-top:10px;color:var(--muted);font-size:13px;line-height:1.5}
		.hero-stats{display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end}
		.stat{min-width:140px;padding:12px 14px;border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.8);box-shadow:var(--shadow)}
		.stat strong{display:block;font-size:20px;line-height:1;color:var(--text)}
		.stat span{display:block;margin-top:4px;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
		.main-grid{display:grid;grid-template-columns:340px 1fr;min-height:0;gap:16px;padding:16px 16px 18px}
		.sidebar,.content{min-height:0}
		.sidebar{display:flex;flex-direction:column;overflow:hidden;border:1px solid var(--line);border-radius:20px;background:rgba(255,255,255,.75);box-shadow:var(--shadow)}
		.sidebar-head{padding:14px 14px 12px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,250,252,.92))}
		.sidebar-head strong{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
		.sidebar-head .sub{margin-top:6px;font-size:12px;color:var(--muted);line-height:1.45}
		#cases{overflow:auto;min-height:0}
		button.case{display:block;width:100%;text-align:left;padding:13px 14px;border:0;border-bottom:1px solid rgba(215,223,232,.75);background:transparent;cursor:pointer;transition:background .15s ease,transform .15s ease}
		button.case:hover{background:#f4f8ff;transform:translateX(2px)}
		button.case.active{background:linear-gradient(90deg,rgba(36,87,214,.10),rgba(106,125,255,.04));box-shadow:inset 3px 0 0 var(--accent)}
		button.case strong{display:block;font-size:13px;line-height:1.35}
		button.case small{display:block;color:var(--muted);font-size:11px;margin-top:4px;line-height:1.35}
		.content{display:grid;grid-template-rows:auto auto auto 1fr;gap:16px;min-height:0}
		.card{background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:20px;padding:16px 18px;box-shadow:var(--shadow)}
		.card-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap}
		.case-title{font-family:Georgia,serif;font-size:21px;line-height:1.15;margin:0 0 8px}
		.case-meta{font-size:12px;color:var(--muted);line-height:1.5}
		.badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
		.badge{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:var(--panel-2);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
		.badge strong{color:var(--text);font-size:12px;letter-spacing:0;text-transform:none}
		.detail-panel{background:rgba(255,255,255,.88);border:1px solid var(--line);border-left:4px solid var(--accent);padding:15px 18px;box-shadow:var(--shadow)}
		.detail-title{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:12px}
		.detail-title h2{margin:0;font:700 17px/1.25 Georgia,serif}
		.detail-title span{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}
		.detail-grid{display:grid;grid-template-columns:repeat(6,minmax(100px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}
		.detail-field{min-width:0;padding:9px 10px;background:#fff}
		.detail-field small{display:block;margin-bottom:4px;color:var(--muted);font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.08em}
		.detail-field strong{display:block;overflow-wrap:anywhere;font-size:12px;line-height:1.35}
		.detail-section{margin-top:12px}
		.detail-section h3{margin:0 0 6px;color:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:.08em}
		.detail-text{margin:0;padding:10px 12px;overflow:auto;white-space:pre-wrap;border:1px solid var(--line);background:#f8fafc;font:12px/1.55 "Cascadia Mono",Consolas,monospace}
		.chunk-detail{margin-top:6px;border:1px solid var(--line);background:#fff}
		.chunk-detail summary{padding:9px 11px;cursor:pointer;font-size:11px;font-weight:700}
		.chunk-detail .detail-text{border-width:1px 0 0}
		.record-row{padding:9px 11px;border:1px solid var(--line);background:#fff;font-size:12px;line-height:1.5}
		.record-row+.record-row{border-top:0}
		.record-row a{color:var(--accent);font-weight:700}
		.citation-panel{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(320px,.95fr);gap:16px;min-height:0}
		.text-card,.table-card{min-height:0;background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}
		.text-card{display:flex;flex-direction:column;overflow:hidden}
		.table-card{display:flex;flex-direction:column;overflow:hidden}
		.panel-head{padding:14px 16px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,250,252,.92))}
		.panel-head strong{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
		.panel-head .sub{margin-top:6px;font-size:12px;color:var(--muted);line-height:1.45}
		.case-text{flex:1;min-height:0;white-space:pre-wrap;background:linear-gradient(180deg,#fff,#fcfdff);padding:18px 18px 20px;overflow:auto;font-family:"Cascadia Mono","SFMono-Regular",Consolas,monospace;font-size:12px;line-height:1.62}
		table{width:100%;border-collapse:collapse;background:transparent}
		thead th{position:sticky;top:0;background:#f7f9fc;z-index:1}
		th,td{padding:10px 11px;border-bottom:1px solid #e7edf4;vertical-align:top;text-align:left;font-size:12px}
		th{font-weight:700;color:#334155;text-transform:uppercase;letter-spacing:.05em;font-size:10px}
		tr.clickable{cursor:pointer}
		tr.clickable:hover{background:#f4f8ff}
		tr.active-row{background:rgba(36,87,214,.08)}
		.empty{padding:18px;color:var(--muted)}
		.list-wrap{overflow:auto;min-height:0}
		.mark-help{font-size:12px;color:var(--muted);margin:0}
		.mark-help strong{color:var(--text)}
		mark.cite-case{background:rgba(245,185,66,.32);box-shadow:inset 0 -2px rgba(245,185,66,.9);padding:0 1px;border-radius:2px}
		mark.cite-law{background:rgba(45,166,108,.22);box-shadow:inset 0 -2px rgba(35,139,89,.9);padding:0 1px;border-radius:2px}
		mark.cite-metadata{background:rgba(64,120,220,.20);box-shadow:inset 0 -2px rgba(53,109,204,.92);padding:0 1px;border-radius:2px}
		mark[data-row-key]{cursor:pointer}
		mark[data-row-key]:hover{outline:2px solid rgba(36,87,214,.55)}
		mark.active-hit{outline:2px solid var(--accent);background:rgba(36,87,214,.18)!important}
		@media (max-width: 1100px){
			.main-grid{grid-template-columns:1fr}
			.citation-panel{grid-template-columns:1fr}
			.detail-grid{grid-template-columns:repeat(3,minmax(100px,1fr))}
			.sidebar{max-height:360px}
		}
		@media (max-width: 760px){
			.hero{padding:18px 14px}
			h1{font-size:24px}
			.main-grid{padding:12px}
			.card,.sidebar,.text-card,.table-card{border-radius:16px}
			.detail-grid{grid-template-columns:repeat(2,minmax(100px,1fr))}
		}
	</style>
</head>
<body>
	<div class=\"shell\">
		<div class=\"hero\">
			<div class=\"hero-top\">
				<div>
					<p class=\"kicker\">AI CaseLibrary</p>
					<h1>Citation Pass</h1>
					<div class=\"hero-copy\">Layered extraction review. Case citations are orange, statutes and legal instruments are green, and extracted metadata is blue. Each layer keeps its own extraction process and exact offsets.</div>
				</div>
				<div class=\"hero-stats\">
					<div class=\"stat\"><strong id=\"liveCount\">0</strong><span>Live citations</span></div>
					<div class=\"stat\"><strong id=\"lawCount\">0</strong><span>Statutes / laws</span></div>
					<div class=\"stat\"><strong id=\"metadataCount\">0</strong><span>Metadata fields</span></div>
					<div class=\"stat\"><strong id=\"selectedCount\">0</strong><span>Selected row</span></div>
					<div class=\"stat\"><strong id=\"caseCount\">0</strong><span>Cases in list</span></div>
				</div>
			</div>
		</div>
		<div class=\"main-grid\">
			<aside class=\"sidebar\">
				<div class=\"sidebar-head\">
					<strong>Review Cohort</strong>
					<div class=\"sub\">Choose a case to inspect the extraction output. The list stays focused on the current proof-of-concept set.</div>
				</div>
				<div id=\"cases\" class=\"list-wrap\"><div class=\"empty\">Loading cases...</div></div>
			</aside>
			<section class=\"content\">
				<div id=\"caseCard\" class=\"card\">Select a case.</div>
				<section id=\"detailPanel\" class=\"detail-panel\"><div class=\"empty\">Select a reference to inspect its exact text, document position, chunks, and stored records.</div></section>
				<div class=\"citation-panel\">
					<div class=\"text-card\">
						<div class=\"panel-head\">
							<strong>Highlighted Text</strong>
							<div class=\"sub\">Case citations are orange. Statutes and legal instruments are green. Metadata is blue.</div>
						</div>
						<div id=\"annotatedText\" class=\"case-text\">No case loaded.</div>
					</div>
					<div class=\"table-card\">
						<div class=\"panel-head\">
							<strong>Extracted References</strong>
							<div class=\"sub\" id=\"tableSummary\">Waiting for a case selection.</div>
						</div>
						<div id=\"citationTables\" class=\"list-wrap empty\">No citation pass loaded yet.</div>
					</div>
				</div>
			</section>
		</div>
	</div>
	<script>
		const state={selected:null,payload:null,activeRowKey:null,detail:null};
		const esc=v=>String(v??'').replace(/[&<>\'\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','\"':'&quot;'}[c]));
		async function json(url){const r=await fetch(url);if(!r.ok){throw new Error('Request failed: '+r.status)}return r.json();}
		const shown=v=>v===null||v===undefined||v===''?'Not stored':String(v);
		function renderCaseList(rows){document.getElementById('caseCount').textContent=String(rows.length);const box=document.getElementById('cases');box.innerHTML=rows.map(row=>`<button class=\"case ${state.selected===row.case_id?'active':''}\" data-id=\"${row.case_id}\"><strong>${esc(row.title)}</strong><small>${esc(row.citation||'No citation')} · ${esc(row.court)} · ${esc(row.date)}</small></button>`).join('')||'<div class="empty">No cases in review list.</div>';box.querySelectorAll('button.case').forEach(b=>b.onclick=()=>openCase(Number(b.dataset.id)));}
		function rowsForView(payload){const cases=(payload.live_extracted||[]).map((row,index)=>({...row,__rowKey:`case:${index}`,__layer:'case'}));const laws=(payload.live_statutes||[]).map((row,index)=>({...row,__rowKey:`law:${index}`,__layer:'law'}));const metadata=(payload.live_metadata||[]).map((row,index)=>({...row,citation_text:row.text,normalized_citation:`${row.field}: ${row.value}`,__rowKey:`metadata:${index}`,__layer:'metadata'}));return [...cases,...laws,...metadata];}
		function findRanges(text,rows){const candidates=[];const codePointToCodeUnit=[0];let codeUnits=0;for(const char of text){codeUnits+=char.length;codePointToCodeUnit.push(codeUnits);}for(const row of rows){const codePointStart=Number(row.offset_start),codePointEnd=Number(row.offset_end);if(!Number.isInteger(codePointStart)||!Number.isInteger(codePointEnd)||codePointStart<0||codePointEnd<=codePointStart||codePointEnd>=codePointToCodeUnit.length)continue;const start=codePointToCodeUnit[codePointStart],end=codePointToCodeUnit[codePointEnd];const citationText=String(row.citation_text||'');if(!citationText||text.slice(start,end)!==citationText)continue;candidates.push({start,end,label:String(row.normalized_citation||citationText),rowKey:String(row.__rowKey||''),layer:String(row.__layer||'case')});}const ranges=[];for(const candidate of candidates.sort((a,b)=>(a.end-a.start)-(b.end-b.start)||a.start-b.start)){if(ranges.some(range=>candidate.start<range.end&&candidate.end>range.start))continue;ranges.push(candidate);}return ranges.sort((a,b)=>a.start-b.start||b.end-a.end);}
		function paragraphBreaks(segment,allowLeadingBreak){const value=String(segment||'');return value.replace(/\[(\d+)\]/g,(m,n,idx)=>{if(idx===0&&!allowLeadingBreak)return`[${n}]`;return`\n\n[${n}]`;});}
		function highlightText(text,ranges){let out='';let cursor=0;for(const range of ranges){if(range.start<cursor||range.start>=text.length)continue;const end=Math.min(range.end,text.length);if(end<=cursor)continue;out+=esc(paragraphBreaks(text.slice(cursor,range.start),cursor>0));const active=state.activeRowKey&&range.rowKey===state.activeRowKey?' active-hit':'';const layerClass=range.layer==='law'?'cite-law':range.layer==='metadata'?'cite-metadata':'cite-case';out+=`<mark class=\"${layerClass}${active}\" data-row-key=\"${esc(range.rowKey)}\" title=\"Click for details: ${esc(range.label)}\">${esc(paragraphBreaks(text.slice(range.start,end),cursor>0||range.start>0))}</mark>`;cursor=end;}out+=esc(paragraphBreaks(text.slice(cursor),cursor>0));return out;}
		function renderHighlights(){if(!state.payload)return;const text=(state.payload.case.full_text||state.payload.case.summary||'').toString();if(!text){document.getElementById('annotatedText').textContent='No case text available.';return;}const ranges=findRanges(text,rowsForView(state.payload));document.getElementById('annotatedText').innerHTML=highlightText(text,ranges);document.querySelectorAll('mark[data-row-key]').forEach(mark=>{mark.onclick=()=>selectReference(String(mark.dataset.rowKey||''));});if(state.activeRowKey){const mark=document.querySelector('mark.active-hit');if(mark)mark.scrollIntoView({behavior:'smooth',block:'center'});}}
		function pinpointFromText(value){const text=String(value||'');const m=text.match(/\bat\s+para(?:s|graph(?:s)?)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*\b/i);return m?m[0].replace(/\s+/g,' ').trim():'';}
		function codePointSlice(value,start,end){const chars=Array.from(String(value||''));const safeStart=Math.max(0,Math.min(start,chars.length));const safeEnd=Math.max(safeStart,Math.min(end,chars.length));return chars.slice(safeStart,safeEnd).join('');}
		function trailingPinpoint(row){if(String(row.__layer||'')!=='Case'||!state.payload)return '';const text=(state.payload.case.full_text||state.payload.case.summary||'').toString();const end=Number(row.offset_end);if(!Number.isInteger(end)||end<0)return '';const tail=codePointSlice(text,end,end+140);const m=tail.match(/^\s*[)\],;:\-]*\s*(?:\[\s*)?(?:at\s+)?para(?:s|graph(?:s)?)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*(?:\s*\])?\b/i);return m?m[0].replace(/\s+/g,' ').trim():'';}
		function pinpointBadge(row){const layer=String(row.__layer||'');if(layer==='Metadata'){const confidence=Number(row.confidence);const confidenceText=Number.isFinite(confidence)?confidence.toFixed(2):'n/a';if(row.span_matched){return `<span class=\"badge\" style=\"background:#edf7ed;border-color:#78b27b;color:#1f5c26\" title=\"Exact text span matched (source: ${esc(String(row.source||'unknown'))}, confidence: ${esc(confidenceText)})\">Matched span</span>`;}return `<span class=\"badge\" style=\"background:#fff4e8;border-color:#d8aa78;color:#8b4e11\" title=\"Extracted metadata without exact text span (source: ${esc(String(row.source||'unknown'))}, confidence: ${esc(confidenceText)})\">Extracted only</span>`;}if(layer!=='Case')return '<span class=\"badge\" style=\"opacity:.58\">N/A</span>';const pinpoint=pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text);if(pinpoint){return `<span class=\"badge\" style=\"background:#edf7ed;border-color:#78b27b;color:#1f5c26\" title=\"${esc(pinpoint)}\">Pinpoint</span>`;}const missed=trailingPinpoint(row);if(missed){return `<span class=\"badge\" style=\"background:#ffe8e8;border-color:#d89494;color:#7f1d1d\" title=\"Trailing pinpoint in source text not captured: ${esc(missed)}\">Missed</span>`;}return '<span class=\"badge\" style=\"background:#f7f7f7;border-color:#c9c9c9;color:#4b5563\" title=\"This citation has no para/paras marker in the source text.\">None cited</span>';}
		function renderRows(cases,laws,metadata){document.getElementById('liveCount').textContent=String(cases.length);document.getElementById('lawCount').textContent=String(laws.length);document.getElementById('metadataCount').textContent=String(metadata.length);document.getElementById('selectedCount').textContent=state.activeRowKey?'1':'0';const casePinpointCount=cases.filter(row=>pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text)).length;const metadataSpanCount=metadata.filter(row=>Boolean(row.span_matched)).length;document.getElementById('tableSummary').textContent=`${cases.length} case citation${cases.length===1?'':'s'} · ${laws.length} statute/law reference${laws.length===1?'':'s'} · ${metadata.length} metadata field${metadata.length===1?'':'s'} · ${casePinpointCount}/${cases.length} case cites with pinpoint · ${metadataSpanCount}/${metadata.length} metadata spans matched.`;const rows=[...cases.map((row,index)=>({...row,__rowKey:`case:${index}`,__layer:'Case'})),...laws.map((row,index)=>({...row,__rowKey:`law:${index}`,__layer:'Law'})),...metadata.map((row,index)=>({...row,kind:row.field,citation_text:row.text,normalized_citation:row.value,__rowKey:`metadata:${index}`,__layer:'Metadata'}))];if(!rows.length)return '<div class=\"empty\">No references extracted.</div>';return `<table><thead><tr><th>#</th><th>Layer</th><th>Kind</th><th>Reference text</th><th>Status</th><th>Normalized</th><th>Where</th><th>Context</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class=\"clickable ${state.activeRowKey===r.__rowKey?'active-row':''}\" data-row-key=\"${r.__rowKey}\"><td>${i+1}</td><td>${esc(r.__layer)}</td><td>${esc(r.kind||'')}</td><td>${esc(r.citation_text||'')}</td><td>${pinpointBadge(r)}</td><td>${esc(r.normalized_citation||'')}</td><td>${esc(`${r.offset_start??''}-${r.offset_end??''}`)}</td><td>${esc(r.context||'')}</td></tr>`).join('')}</tbody></table>`;}
		function detailField(label,value){return `<div class=\"detail-field\"><small>${esc(label)}</small><strong>${esc(shown(value))}</strong></div>`;}
		function renderDetail(detail){const panel=document.getElementById('detailPanel');if(!detail){panel.innerHTML='<div class=\"empty\">Select a reference to inspect its exact text, document position, chunks, and stored records.</div>';return;}const location=detail.location||{},passage=detail.passage||{},metadata=detail.metadata||null;const chunks=(detail.chunks||[]).map(chunk=>`<details class=\"chunk-detail\"><summary>${esc(chunk.chunk_set)} #${esc(chunk.chunk_index)} · ${esc(shown(chunk.chunk_label))} · chunk id ${esc(chunk.chunk_id)}</summary><div class=\"detail-grid\">${detailField('Paragraph range',chunk.paragraph_start===null?'Not stored':chunk.paragraph_start===chunk.paragraph_end?chunk.paragraph_start:`${chunk.paragraph_start}-${chunk.paragraph_end}`)}${detailField('Chunk offsets',`${chunk.offset_start}-${chunk.offset_end}`)}${detailField('Document offsets',`${chunk.document_start}-${chunk.document_end}`)}${detailField('Text length',chunk.text_length)}${detailField('Token estimate',chunk.token_estimate)}${detailField('Exact chunk match',chunk.citation_text)}</div><pre class=\"detail-text\">${esc(chunk.text)}</pre></details>`).join('')||'<div class=\"record-row\">No stored chunk contains this exact document span.</div>';const records=(detail.stored_records||[]).map(record=>{const target=record.target;const targetHtml=record.target===undefined?'':target?` · resolved to <a href=\"/case-reader?case_id=${encodeURIComponent(target.case_id)}\">${esc(target.title||target.citation||`Case ${target.case_id}`)}</a> (${esc(shown(target.citation))})`:' · no resolved target';return `<div class=\"record-row\"><strong>Record ${esc(record.record_id)}</strong> · ${esc(shown(record.citation_kind))} · chunk ${esc(shown(record.chunk_id))} · offsets ${esc(shown(record.offset_start))}-${esc(shown(record.offset_end))}${record.provenance!==undefined?` · provenance ${esc(shown(record.provenance))}`:''}${record.unresolved!==undefined?` · ${record.unresolved?'unresolved':'resolved flag clear'}`:''}${targetHtml}</div>`;}).join('')||'<div class=\"record-row\">No matching stored record for this extracted occurrence.</div>';panel.innerHTML=`<div class=\"detail-title\"><h2>${esc(detail.citation_text)}</h2><span>${esc(detail.layer)} · ${esc(detail.kind)}</span></div><div class=\"detail-grid\">${detailField('Normalized value',detail.normalized_value)}${detailField('Document offsets',`${detail.offset_start}-${detail.offset_end}`)}${detailField('Span length',detail.span_length)}${detailField('Line / column',`${location.line_number} / ${location.column_number}`)}${detailField('Paragraph',location.paragraph_number)}${detailField('Document position',`${location.position_percent}%`)}${metadata?detailField('Confidence',metadata.confidence)+detailField('Source',metadata.source):''}</div><div class=\"detail-section\"><h3>Line-aligned passage · offsets ${esc(passage.offset_start)}-${esc(passage.offset_end)}</h3><pre class=\"detail-text\">${esc(passage.text)}</pre></div><div class=\"detail-section\"><h3>Containing chunks (${detail.chunks.length})</h3>${chunks}</div><div class=\"detail-section\"><h3>Stored records (${detail.stored_records.length})</h3>${records}</div>`;}
		async function loadDetail(rowKey){const selectedRow=rowsForView(state.payload).find(row=>row.__rowKey===rowKey);if(!selectedRow)return;const start=Number(selectedRow.offset_start),end=Number(selectedRow.offset_end);if(!Number.isInteger(start)||!Number.isInteger(end)||end<=start){document.getElementById('detailPanel').innerHTML='<div class=\"empty\">No exact source span is available for this extracted metadata field.</div>';return;}document.getElementById('detailPanel').innerHTML='<div class=\"empty\">Loading citation details...</div>';const query=new URLSearchParams({layer:selectedRow.__layer,offset_start:String(start),offset_end:String(end)});try{const detail=await json(`/cases/${state.selected}/citation-pass/detail?${query}`);if(state.activeRowKey!==rowKey)return;state.detail=detail;renderDetail(detail);}catch(error){if(state.activeRowKey===rowKey)document.getElementById('detailPanel').innerHTML=`<div class=\"empty\">${esc(error.message)}</div>`;}}
		function selectReference(rowKey){if(!rowKey)return;state.activeRowKey=rowKey;state.detail=null;renderPayload(state.payload);loadDetail(rowKey);}
		function bindRowClicks(){document.querySelectorAll('tr[data-row-key]').forEach(row=>{row.onclick=()=>selectReference(String(row.getAttribute('data-row-key')||''));});}
		function metadataFieldValue(rows,name){const target=String(name||'').toLowerCase();const row=(rows||[]).find(r=>String(r.field||'').toLowerCase()===target);return row?String(row.value||'').trim():'';}
		function aljrSummaryText(metadataRows){const role=metadataFieldValue(metadataRows,'government role').toLowerCase();const outcomeRaw=metadataFieldValue(metadataRows,'decision outcome').toLowerCase();const filedBy=role==='applicant'?'Minister':role==='respondent'?'Individual':'Unknown';let result='Unknown';if(outcomeRaw==='dismissed'){result='Dismissed';}else if(outcomeRaw==='allowed'||outcomeRaw==='granted'){result='Granted';}return `ALJR Filed by ${filedBy}, result: ${result}`;}
		function renderPayload(payload){state.payload=payload;const c=payload.case;const s=payload.summary||{};const cases=(payload.live_extracted||[]).map(row=>({...row,context:row.context||''}));const laws=(payload.live_statutes||[]).map(row=>({...row,context:row.context||''}));const metadata=(payload.live_metadata||[]).map(row=>({...row,context:row.context||''}));const aljrSummary=aljrSummaryText(metadata);document.getElementById('caseCard').innerHTML=`<div class=\"card-head\"><div><h2 class=\"case-title\">${esc(c.title)}</h2><div class=\"case-meta\">${esc(c.citation||'No citation')} · ${esc(c.court)} · ${esc(c.date)} · id ${c.id}</div><div class=\"case-meta\" style=\"margin-top:6px\"><strong>${esc(aljrSummary)}</strong></div></div><div class=\"badges\"><span class=\"badge\"><strong>${s.live_total||0}</strong> case citations</span><span class=\"badge\"><strong>${s.statute_total||0}</strong> statutes/laws</span><span class=\"badge\"><strong>${s.metadata_total||0}</strong> metadata fields</span><span class=\"badge\"><strong>${c.full_text?'Yes':'No'}</strong> full text</span></div></div><div class=\"badges\" style=\"margin-top:14px\"><span class=\"badge\">Orange: cases</span><span class=\"badge\">Green: statutes/laws</span><span class=\"badge\">Blue: metadata</span></div>`;document.getElementById('citationTables').innerHTML=renderRows(cases,laws,metadata);bindRowClicks();renderHighlights();}
		async function openCase(caseId){state.selected=caseId;state.activeRowKey=null;state.detail=null;renderDetail(null);const payload=await json(`/cases/${caseId}/citation-pass`);renderPayload(payload);const list=await json('/citation-map/cases/review/fc-priority?limit=300');renderCaseList(list);}
		async function load(){const list=await json('/citation-map/cases/review/fc-priority?limit=300');renderCaseList(list);if(list.length){await openCase(list[0].case_id);}}
		load().catch(e=>{document.getElementById('cases').innerHTML=`<div class=\"empty\">${esc(e.message)}</div>`;});
	</script>
</body>
</html>"""


@router.get("/citation-pass", response_class=HTMLResponse, include_in_schema=False)
def citation_pass_page() -> str:
	return _citation_pass_page_html()


@router.get("/cases/{case_id}/citation-pass", response_model=dict[str, Any])
def get_case_citation_pass(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)

	full_text = case.full_text or case.summary or ""
	live_rows = extract_case_citation_matches(full_text)
	statute_rows = extract_statute_reference_matches(full_text)
	metadata_rows = extract_metadata_observations(full_text)
	live_payload = [
		{
			"kind": match.kind,
			"citation_text": match.citation_text,
			"normalized_citation": match.normalized_citation,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"context": full_text[max(0, (match.offset_start or 0) - 40):min(len(full_text), (match.offset_end or 0) + 40)].replace("\n", " ").strip(),
		}
		for match in live_rows
	]
	statute_payload = [
		{
			"kind": match.kind,
			"citation_text": match.citation_text,
			"normalized_citation": match.normalized_citation,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"context": full_text[max(0, match.offset_start - 40):min(len(full_text), match.offset_end + 40)].replace("\n", " ").strip(),
		}
		for match in statute_rows
	]
	metadata_payload = [
		{
			"field": match.field,
			"text": match.text,
			"value": match.value,
			"offset_start": match.offset_start,
			"offset_end": match.offset_end,
			"confidence": match.confidence,
			"source": match.source,
			"span_matched": match.span_matched,
			"context": (
				full_text[max(0, match.offset_start - 40):min(len(full_text), match.offset_end + 40)].replace("\n", " ").strip()
				if match.span_matched and match.offset_start is not None and match.offset_end is not None
				else ""
			),
		}
		for match in metadata_rows
	]

	return {
		"case": {
			"id": case.id,
			"title": case.title,
			"citation": case.citation,
			"court": case.court,
			"date": case.date,
			"summary": case.summary,
			"full_text": case.full_text,
		},
		"summary": {
			"live_total": len(live_payload),
			"statute_total": len(statute_payload),
			"metadata_total": len(metadata_payload),
		},
		"live_extracted": live_payload,
		"live_statutes": statute_payload,
		"live_metadata": metadata_payload,
	}


def _citation_pass_chunks(
	db: Session,
	case_id: int,
	full_text: str,
	offset_start: int,
	offset_end: int,
) -> list[dict[str, Any]]:
	def _is_paragraph_chunk(chunk_set: str | None) -> bool:
		value = (chunk_set or "").strip().lower()
		return value == "paragraph" or value.startswith("paragraph_")

	chunks = list(
		db.scalars(
			select(CaseChunk)
			.where(CaseChunk.case_id == case_id)
			.order_by(CaseChunk.chunk_set, CaseChunk.chunk_index, CaseChunk.id)
		)
	)
	locations: list[dict[str, Any]] = []
	for chunk in chunks:
		chunk_text = chunk.text or ""
		search_start = 0
		while chunk_text:
			chunk_start = full_text.find(chunk_text, search_start)
			if chunk_start < 0:
				break
			chunk_end = chunk_start + len(chunk_text)
			if chunk_start <= offset_start and offset_end <= chunk_end:
				relative_start = offset_start - chunk_start
				relative_end = offset_end - chunk_start
				locations.append(
					{
						"chunk_id": chunk.id,
						"chunk_set": chunk.chunk_set,
						"chunk_index": chunk.chunk_index,
						"chunk_label": chunk.chunk_label,
						"paragraph_start": chunk.paragraph_start,
						"paragraph_end": chunk.paragraph_end,
						"document_start": chunk_start,
						"document_end": chunk_end,
						"offset_start": relative_start,
						"offset_end": relative_end,
						"citation_text": chunk_text[relative_start:relative_end],
						"text": chunk_text,
						"text_length": len(chunk_text),
						"token_estimate": chunk.token_estimate,
						"is_paragraph_chunk": _is_paragraph_chunk(chunk.chunk_set),
					}
				)
				break
			search_start = chunk_start + 1
	locations.sort(
		key=lambda row: (
			0 if row.get("is_paragraph_chunk") else 1,
			abs((row.get("text_length") or 0) - (offset_end - offset_start)),
			str(row.get("chunk_set") or ""),
			int(row.get("chunk_index") or 0),
		)
	)
	return locations


def _stored_case_citation_details(
	db: Session,
	case_id: int,
	selected: Any,
	chunks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
	chunk_locations = {int(chunk["chunk_id"]): chunk for chunk in chunks}
	rows = list(db.scalars(select(Citation).where(Citation.source_case_id == case_id).order_by(Citation.id)))
	details: list[dict[str, Any]] = []
	for citation in rows:
		chunk = chunk_locations.get(citation.chunk_id) if citation.chunk_id is not None else None
		identity_matches = (
			citation.normalized_citation == selected.normalized_citation
			or citation.citation_text == selected.citation_text
		)
		if citation.chunk_id is None:
			location_matches = (
				citation.offset_start == selected.offset_start
				and citation.offset_end == selected.offset_end
			)
		else:
			location_matches = chunk is not None and (
				citation.offset_start is None
				or (
					citation.offset_start == chunk["offset_start"]
					and citation.offset_end == chunk["offset_end"]
				)
			)
		if not identity_matches or not location_matches:
			continue
		target = db.get(Case, citation.target_case_id) if citation.target_case_id is not None else None
		details.append(
			{
				"record_id": citation.id,
				"citation_kind": getattr(citation, "citation_kind", "unknown"),
				"chunk_id": citation.chunk_id,
				"offset_start": citation.offset_start,
				"offset_end": citation.offset_end,
				"citation_text": citation.citation_text,
				"normalized_citation": citation.normalized_citation,
				"provenance": citation.provenance,
				"unresolved": citation.unresolved,
				"target": {
					"case_id": target.id,
					"title": target.title,
					"citation": target.citation,
					"court": target.court,
					"date": target.date,
				} if target is not None else None,
			}
		)
	return details


def _stored_statute_reference_details(
	db: Session,
	case_id: int,
	selected: Any,
	chunks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
	chunk_locations = {int(chunk["chunk_id"]): chunk for chunk in chunks}
	rows = list(db.scalars(select(StatuteReference).where(StatuteReference.source_case_id == case_id).order_by(StatuteReference.id)))
	details: list[dict[str, Any]] = []
	for reference in rows:
		chunk = chunk_locations.get(reference.chunk_id) if reference.chunk_id is not None else None
		identity_matches = (
			reference.normalized_reference == selected.normalized_citation
			or reference.reference_text == selected.citation_text
		)
		if reference.chunk_id is None:
			location_matches = (
				reference.offset_start == selected.offset_start
				and reference.offset_end == selected.offset_end
			)
		else:
			location_matches = chunk is not None and (
				reference.offset_start is None
				or (
					reference.offset_start == chunk["offset_start"]
					and reference.offset_end == chunk["offset_end"]
				)
			)
		if identity_matches and location_matches:
			details.append(
				{
					"record_id": reference.id,
					"chunk_id": reference.chunk_id,
					"offset_start": reference.offset_start,
					"offset_end": reference.offset_end,
					"reference_text": reference.reference_text,
					"normalized_reference": reference.normalized_reference,
					"reference_kind": reference.reference_kind,
				}
			)
	return details


@router.get("/cases/{case_id}/citation-pass/detail", response_model=dict[str, Any])
def get_case_citation_pass_detail(
	case_id: int,
	layer: str,
	offset_start: int,
	offset_end: int,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)
	full_text = case.full_text or case.summary or ""
	if layer not in {"case", "law", "metadata"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported citation layer")
	if offset_start < 0 or offset_end <= offset_start or offset_end > len(full_text):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid citation offsets")

	if layer == "case":
		matches = extract_case_citation_matches(full_text)
	elif layer == "law":
		matches = extract_statute_reference_matches(full_text)
	else:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metadata layer not supported in this endpoint")
	selected = next(
		(match for match in matches if match.offset_start == offset_start and match.offset_end == offset_end),
		None,
	)
	if selected is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Extracted reference not found")

	line_start = full_text.rfind("\n", 0, offset_start) + 1
	line_end = full_text.find("\n", offset_end)
	if line_end < 0:
		line_end = len(full_text)
	line_text = full_text[line_start:line_end]
	paragraph_match = re.match(r"\s*\[(\d+)\]", line_text)
	chunks = _citation_pass_chunks(db, case_id, full_text, offset_start, offset_end)
	stored_records: list[dict[str, Any]] = []
	if layer == "case":
		stored_records = _stored_case_citation_details(db, case_id, selected, chunks)
	elif layer == "law":
		stored_records = _stored_statute_reference_details(db, case_id, selected, chunks)
	primary_paragraph_chunk = next((chunk for chunk in chunks if chunk.get("is_paragraph_chunk")), None)

	citation_text = selected.citation_text
	normalized = selected.normalized_citation
	kind = selected.kind
	return {
		"layer": layer,
		"kind": kind,
		"citation_text": citation_text,
		"normalized_value": normalized,
		"offset_start": offset_start,
		"offset_end": offset_end,
		"span_length": offset_end - offset_start,
		"location": {
			"line_number": full_text.count("\n", 0, offset_start) + 1,
			"column_number": offset_start - line_start + 1,
			"paragraph_number": int(paragraph_match.group(1)) if paragraph_match else None,
			"document_length": len(full_text),
			"position_percent": round((offset_start / len(full_text)) * 100, 2) if full_text else 0.0,
		},
		"passage": {
			"text": line_text,
			"offset_start": line_start,
			"offset_end": line_end,
		},
		"chunks": chunks,
		"primary_paragraph_chunk": primary_paragraph_chunk,
		"stored_records": stored_records,
	}


@router.get("/citation-map/authorities", response_model=list[CitationMapAuthorityResponse])
def get_citation_map_authorities(
	limit: int = 50,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _top_authorities(db, limit=max(1, min(200, limit)))


@router.get("/citation-map/cases", response_model=list[CitationMapCaseNode])
def search_citation_map_cases(
	q: str,
	limit: int = 12,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _search_citation_cases(db, q, limit=max(1, min(30, limit)))


@router.get("/citation-map/cases/review/fc-priority", response_model=list[CitationMapCaseNode])
def review_fc_priority_cases(
	limit: int = 300,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _review_fc_priority_cases(db, limit=max(1, min(500, limit)))


@router.get("/citation-map/topics", response_model=list[CitationMapTopicResponse])
def get_citation_map_topics(
	q: str = "",
	limit: int = 100,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _citation_map_topics(db, q, limit=max(1, min(250, limit)))


@router.get("/citation-map/issues/graph", response_model=CitationIssueMapResponse)
def get_citation_issue_map(
	category: str,
	value: str,
	limit: int = 50,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	if category not in {"issue", "statute", "legal_area"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported tag category")
	return _citation_issue_map(db, category, value, limit=max(10, min(200, limit)))


@router.get("/citation-map/cases/{case_id}/authority-map", response_model=CitationMapNeighborhoodResponse)
def get_case_authority_map(
	case_id: int,
	limit: int = 5,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)
	return _case_authority_map(db, case, limit=max(1, min(12, limit)))


@router.get("/citation-map/cases/{case_id}/tags", response_model=list[CitationMapLegalTagResponse])
def get_citation_map_case_tags(
	case_id: int,
	limit: int = 100,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _case_legal_tags(db, case_id, limit=max(1, min(250, limit)))


@router.get("/citation-map/common-citers", response_model=list[CitationMapCommonCiterResponse])
def get_common_citing_cases(
	case_ids: str,
	limit: int = 50,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	try:
		selected_ids = list(dict.fromkeys(int(value.strip()) for value in case_ids.split(",") if value.strip()))
	except ValueError as exc:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="case_ids must be integers") from exc
	if len(selected_ids) < 2 or len(selected_ids) > 3:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Select two or three distinct cases")
	return _common_citing_cases(db, selected_ids, limit=max(1, min(200, limit)))


@router.get("/citation-map/paths", response_model=list[CitationMapPathResponse])
def get_citation_paths(
	source_case_id: int,
	target_case_id: int,
	max_hops: int = 3,
	limit: int = 5,
	per_node_limit: int = 40,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	return _citation_paths(
		db,
		source_case_id,
		target_case_id,
		max_hops=max(1, min(6, max_hops)),
		limit=max(1, min(25, limit)),
		per_node_limit=max(5, min(120, per_node_limit)),
	)


@router.get("/citation-map/paths/contextual", response_model=list[CitationMapContextualPathResponse])
def get_contextual_citation_paths(
	source_case_id: int,
	target_case_id: int,
	max_hops: int = 3,
	limit: int = 5,
	per_node_limit: int = 40,
	hop_context_limit: int = 1,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	return _citation_contextual_paths(
		db,
		source_case_id,
		target_case_id,
		max_hops=max(1, min(6, max_hops)),
		limit=max(1, min(25, limit)),
		per_node_limit=max(5, min(120, per_node_limit)),
		hop_context_limit=max(1, min(5, hop_context_limit)),
	)


@router.get("/citation-map/paths/hidden", response_model=list[CitationMapHiddenBridgeResponse])
def get_hidden_citation_bridges(
	source_case_id: int,
	target_case_id: int,
	max_hops: int = 4,
	path_limit: int = 20,
	per_node_limit: int = 60,
	limit: int = 15,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if source_case_id == target_case_id:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="source_case_id and target_case_id must be different",
		)
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	return _citation_hidden_bridges(
		db,
		source_case_id,
		target_case_id,
		max_hops=max(2, min(8, max_hops)),
		path_limit=max(1, min(40, path_limit)),
		per_node_limit=max(5, min(150, per_node_limit)),
		bridge_limit=max(1, min(60, limit)),
	)


@router.get("/citation-map/paths/hidden.csv")
def export_hidden_citation_bridges(
	source_case_id: int,
	target_case_id: int,
	max_hops: int = 4,
	path_limit: int = 20,
	per_node_limit: int = 60,
	limit: int = 15,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_hidden_citation_bridges(
		source_case_id=source_case_id,
		target_case_id=target_case_id,
		max_hops=max_hops,
		path_limit=path_limit,
		per_node_limit=per_node_limit,
		limit=limit,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"bridge_case_id",
		"bridge_title",
		"bridge_citation",
		"path_count",
		"weighted_support",
		"average_relative_position",
		"average_path_hops",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		bridge = row.get("bridge_case") or {}
		writer.writerow(
			{
				"bridge_case_id": bridge.get("case_id"),
				"bridge_title": bridge.get("title"),
				"bridge_citation": bridge.get("citation"),
				"path_count": row.get("path_count"),
				"weighted_support": row.get("weighted_support"),
				"average_relative_position": row.get("average_relative_position"),
				"average_path_hops": row.get("average_path_hops"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="hidden-bridges-{source_case_id}-to-{target_case_id}.csv"'},
	)


@router.get(
	"/citation-map/cases/{case_id}/authority-signals",
	response_model=list[CitationMapAuthoritySignalResponse],
)
def get_citation_authority_signals(
	case_id: int,
	limit: int = 20,
	context_limit: int = 3,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _citation_authority_signals(
		db,
		case_id,
		limit=max(1, min(80, limit)),
		context_limit=max(1, min(10, context_limit)),
	)


@router.get("/citation-map/cases/{case_id}/authority-signals.csv")
def export_citation_authority_signals(
	case_id: int,
	limit: int = 20,
	context_limit: int = 3,
	db: Session = Depends(get_db),
) -> Response:
	_get_case_or_404(case_id, db)
	rows = _citation_authority_signals(
		db,
		case_id,
		limit=max(1, min(80, limit)),
		context_limit=max(1, min(10, context_limit)),
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"occurrence_count",
		"distinct_chunks",
		"gravity_share",
		"global_citing_cases",
		"surprise_score",
		"originality_score",
		"boilerplate_hits",
		"first_chunk_index",
		"last_chunk_index",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"occurrence_count": row.get("occurrence_count"),
				"distinct_chunks": row.get("distinct_chunks"),
				"gravity_share": row.get("gravity_share"),
				"global_citing_cases": row.get("global_citing_cases"),
				"surprise_score": row.get("surprise_score"),
				"originality_score": row.get("originality_score"),
				"boilerplate_hits": row.get("boilerplate_hits"),
				"first_chunk_index": row.get("first_chunk_index"),
				"last_chunk_index": row.get("last_chunk_index"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="authority-signals-{case_id}.csv"'},
	)


@router.get(
	"/citation-map/cases/{case_id}/missing-authorities",
	response_model=list[CitationMapMissingAuthorityResponse],
)
def get_citation_missing_authorities(
	case_id: int,
	peer_limit: int = 40,
	limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if not (0.0 <= min_peer_share <= 1.0):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="min_peer_share must be between 0 and 1")
	_get_case_or_404(case_id, db)
	return _citation_missing_authorities(
		db,
		case_id,
		peer_limit=max(5, min(200, peer_limit)),
		result_limit=max(1, min(100, limit)),
		min_peer_share=min_peer_share,
		min_peer_citations=max(1, min(30, min_peer_citations)),
	)


@router.get("/citation-map/cases/{case_id}/missing-authorities.csv")
def export_citation_missing_authorities(
	case_id: int,
	peer_limit: int = 40,
	limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_missing_authorities(
		case_id=case_id,
		peer_limit=peer_limit,
		limit=limit,
		min_peer_share=min_peer_share,
		min_peer_citations=min_peer_citations,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"peer_citing_cases",
		"peer_coverage",
		"peer_occurrences",
		"rarity_boost",
		"priority_score",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"peer_citing_cases": row.get("peer_citing_cases"),
				"peer_coverage": row.get("peer_coverage"),
				"peer_occurrences": row.get("peer_occurrences"),
				"rarity_boost": row.get("rarity_boost"),
				"priority_score": row.get("priority_score"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="missing-authorities-{case_id}.csv"'},
	)


@router.get(
	"/citation-map/cases/{case_id}/position-profiles",
	response_model=list[CitationMapPositionProfileResponse],
)
def get_citation_position_profiles(
	case_id: int,
	limit: int = 30,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _citation_position_profiles(
		db,
		case_id,
		limit=max(1, min(120, limit)),
		min_occurrences=max(1, min(50, min_occurrences)),
	)


@router.get("/citation-map/cases/{case_id}/position-profiles.csv")
def export_citation_position_profiles(
	case_id: int,
	limit: int = 30,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_position_profiles(
		case_id=case_id,
		limit=limit,
		min_occurrences=min_occurrences,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"occurrence_count",
		"avg_chunk_index",
		"first_chunk_index",
		"last_chunk_index",
		"first_half_hits",
		"second_half_hits",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"occurrence_count": row.get("occurrence_count"),
				"avg_chunk_index": row.get("avg_chunk_index"),
				"first_chunk_index": row.get("first_chunk_index"),
				"last_chunk_index": row.get("last_chunk_index"),
				"first_half_hits": row.get("first_half_hits"),
				"second_half_hits": row.get("second_half_hits"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="position-profiles-{case_id}.csv"'},
	)


@router.get(
	"/citation-map/cases/{case_id}/completion-suggestions",
	response_model=list[CitationMapCompletionSuggestionResponse],
)
def get_citation_completion_suggestions(
	case_id: int,
	peer_limit: int = 40,
	limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if not (0.0 <= min_peer_share <= 1.0):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="min_peer_share must be between 0 and 1")
	_get_case_or_404(case_id, db)
	return _citation_completion_suggestions(
		db,
		case_id,
		peer_limit=max(5, min(200, peer_limit)),
		limit=max(1, min(100, limit)),
		min_peer_share=min_peer_share,
		min_peer_citations=max(1, min(30, min_peer_citations)),
	)


@router.get("/citation-map/cases/{case_id}/completion-suggestions.csv")
def export_citation_completion_suggestions(
	case_id: int,
	peer_limit: int = 40,
	limit: int = 20,
	min_peer_share: float = 0.2,
	min_peer_citations: int = 2,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_completion_suggestions(
		case_id=case_id,
		peer_limit=peer_limit,
		limit=limit,
		min_peer_share=min_peer_share,
		min_peer_citations=min_peer_citations,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"peer_citing_cases",
		"peer_coverage",
		"rarity_boost",
		"expected_occurrences",
		"recommendation_score",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"peer_citing_cases": row.get("peer_citing_cases"),
				"peer_coverage": row.get("peer_coverage"),
				"rarity_boost": row.get("rarity_boost"),
				"expected_occurrences": row.get("expected_occurrences"),
				"recommendation_score": row.get("recommendation_score"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="completion-suggestions-{case_id}.csv"'},
	)


@router.get("/citation-map/surprises", response_model=list[CitationMapSurpriseResponse])
def get_citation_surprises(
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 50,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if bool(category) != bool(value):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="category and value must be provided together")
	if category and category not in {"issue", "statute", "legal_area", "outcome"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported tag category")
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="start_year cannot be greater than end_year")
	return _citation_surprise_feed(
		db,
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=max(1, min(250, limit)),
		min_occurrences=max(1, min(50, min_occurrences)),
	)


@router.get("/citation-map/surprises.csv")
def export_citation_surprises(
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 50,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_surprises(
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=limit,
		min_occurrences=min_occurrences,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"source_case_id",
		"source_title",
		"source_citation",
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"occurrence_count",
		"global_citing_cases",
		"gravity_share",
		"surprise_score",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		source_case = row.get("source_case") or {}
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"source_case_id": source_case.get("case_id"),
				"source_title": source_case.get("title"),
				"source_citation": source_case.get("citation"),
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"occurrence_count": row.get("occurrence_count"),
				"global_citing_cases": row.get("global_citing_cases"),
				"gravity_share": row.get("gravity_share"),
				"surprise_score": row.get("surprise_score"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="citation-surprises.csv"'},
	)


@router.get("/citation-map/authorities/replacement", response_model=CitationMapReplacementResponse)
def get_citation_replacement_trend(
	old_case_id: int,
	new_case_id: int,
	start_year: int | None = None,
	end_year: int | None = None,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	if old_case_id == new_case_id:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="old_case_id and new_case_id must be different",
		)
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="start_year cannot be greater than end_year",
		)
	_get_case_or_404(old_case_id, db)
	_get_case_or_404(new_case_id, db)
	return _citation_replacement_trend(
		db,
		old_case_id,
		new_case_id,
		start_year=start_year,
		end_year=end_year,
	)


@router.get("/citation-map/authorities/lifecycle", response_model=list[CitationMapAuthorityLifecycleResponse])
def get_citation_authority_lifecycle(
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 25,
	recent_years: int = 3,
	prior_years: int = 3,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if bool(category) != bool(value):
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="category and value must be provided together")
	if category and category not in {"issue", "statute", "legal_area", "outcome"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported tag category")
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="start_year cannot be greater than end_year")
	return _citation_authority_lifecycle(
		db,
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=max(1, min(120, limit)),
		recent_years=max(1, min(10, recent_years)),
		prior_years=max(1, min(10, prior_years)),
	)


@router.get("/citation-map/authorities/lifecycle.csv")
def export_citation_authority_lifecycle(
	category: str | None = None,
	value: str | None = None,
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 25,
	recent_years: int = 3,
	prior_years: int = 3,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_authority_lifecycle(
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		limit=limit,
		recent_years=recent_years,
		prior_years=prior_years,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"authority_case_id",
		"authority_title",
		"authority_citation",
		"recent_citing_cases",
		"prior_citing_cases",
		"total_citing_cases",
		"velocity",
		"decay",
		"lifecycle_stage",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"authority_case_id": authority.get("case_id"),
				"authority_title": authority.get("title"),
				"authority_citation": authority.get("citation"),
				"recent_citing_cases": row.get("recent_citing_cases"),
				"prior_citing_cases": row.get("prior_citing_cases"),
				"total_citing_cases": row.get("total_citing_cases"),
				"velocity": row.get("velocity"),
				"decay": row.get("decay"),
				"lifecycle_stage": row.get("lifecycle_stage"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="authority-lifecycle.csv"'},
	)


@router.get("/citation-map/courts/flow", response_model=list[CitationMapCourtFlowResponse])
def get_citation_cross_court_flow(
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 40,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="start_year cannot be greater than end_year")
	return _citation_cross_court_flow(
		db,
		start_year=start_year,
		end_year=end_year,
		limit=max(1, min(200, limit)),
	)


@router.get("/citation-map/courts/flow.csv")
def export_citation_cross_court_flow(
	start_year: int | None = None,
	end_year: int | None = None,
	limit: int = 40,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_cross_court_flow(
		start_year=start_year,
		end_year=end_year,
		limit=limit,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = ["source_court", "target_court", "citing_case_count", "citation_occurrences"]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		writer.writerow(
			{
				"source_court": row.get("source_court"),
				"target_court": row.get("target_court"),
				"citing_case_count": row.get("citing_case_count"),
				"citation_occurrences": row.get("citation_occurrences"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="cross-court-flow.csv"'},
	)


@router.get("/citation-map/authorities/landmarks", response_model=list[CitationMapLandmarkCandidateResponse])
def get_citation_landmark_candidates(
	limit: int = 20,
	recent_years: int = 3,
	baseline_years: int = 5,
	min_recent: int = 20,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	return _citation_landmark_candidates(
		db,
		limit=max(1, min(100, limit)),
		recent_years=max(1, min(10, recent_years)),
		baseline_years=max(1, min(20, baseline_years)),
		min_recent=max(1, min(200, min_recent)),
	)


@router.get("/citation-map/authorities/landmarks.csv")
def export_citation_landmark_candidates(
	limit: int = 20,
	recent_years: int = 3,
	baseline_years: int = 5,
	min_recent: int = 20,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_landmark_candidates(
		limit=limit,
		recent_years=recent_years,
		baseline_years=baseline_years,
		min_recent=min_recent,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"case_id",
		"title",
		"citation",
		"recent_citing_cases",
		"baseline_citing_cases",
		"emergence_score",
		"lift_ratio",
		"recent_start_year",
		"recent_end_year",
		"baseline_start_year",
		"baseline_end_year",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		case_node = row.get("case") or {}
		writer.writerow(
			{
				"case_id": case_node.get("case_id"),
				"title": case_node.get("title"),
				"citation": case_node.get("citation"),
				"recent_citing_cases": row.get("recent_citing_cases"),
				"baseline_citing_cases": row.get("baseline_citing_cases"),
				"emergence_score": row.get("emergence_score"),
				"lift_ratio": row.get("lift_ratio"),
				"recent_start_year": (row.get("recent_window") or {}).get("start_year"),
				"recent_end_year": (row.get("recent_window") or {}).get("end_year"),
				"baseline_start_year": (row.get("baseline_window") or {}).get("start_year"),
				"baseline_end_year": (row.get("baseline_window") or {}).get("end_year"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="landmark-candidates.csv"'},
	)


@router.get("/citation-map/issues/shifts", response_model=list[CitationMapReplacementResponse])
def get_citation_doctrine_shifts(
	category: str,
	value: str,
	limit: int = 10,
	candidate_limit: int = 12,
	start_year: int | None = None,
	end_year: int | None = None,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	if category not in {"issue", "statute", "legal_area"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported tag category")
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="start_year cannot be greater than end_year")
	return _citation_doctrine_shifts(
		db,
		category=category,
		value=value,
		limit=max(1, min(50, limit)),
		candidate_limit=max(4, min(40, candidate_limit)),
		start_year=start_year,
		end_year=end_year,
	)


@router.get("/citation-map/issues/dashboard", response_model=CitationMapShiftDashboardResponse)
def get_citation_shift_dashboard(
	category: str,
	value: str,
	start_year: int | None = None,
	end_year: int | None = None,
	replacement_limit: int = 8,
	lifecycle_limit: int = 40,
	surprise_limit: int = 25,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	if category not in {"issue", "statute", "legal_area"}:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unsupported tag category")
	if start_year is not None and end_year is not None and start_year > end_year:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="start_year cannot be greater than end_year")
	return _citation_shift_dashboard(
		db,
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		replacement_limit=max(1, min(30, replacement_limit)),
		lifecycle_limit=max(5, min(200, lifecycle_limit)),
		surprise_limit=max(1, min(200, surprise_limit)),
	)


@router.get("/citation-map/issues/dashboard.csv")
def export_citation_shift_dashboard(
	category: str,
	value: str,
	start_year: int | None = None,
	end_year: int | None = None,
	replacement_limit: int = 8,
	lifecycle_limit: int = 40,
	surprise_limit: int = 25,
	db: Session = Depends(get_db),
) -> Response:
	payload = get_citation_shift_dashboard(
		category=category,
		value=value,
		start_year=start_year,
		end_year=end_year,
		replacement_limit=replacement_limit,
		lifecycle_limit=lifecycle_limit,
		surprise_limit=surprise_limit,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = ["section", "case_id", "title", "citation", "score", "status", "meta"]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in payload.get("replacement_candidates", []):
		old_node = row.get("old_authority") or {}
		new_node = row.get("new_authority") or {}
		writer.writerow(
			{
				"section": "replacement_candidate",
				"case_id": f'{old_node.get("case_id")}->{new_node.get("case_id")}',
				"title": f'{old_node.get("title")} -> {new_node.get("title")}',
				"citation": f'{old_node.get("citation")} -> {new_node.get("citation")}',
				"score": row.get("replacement_score"),
				"status": row.get("status"),
				"meta": "",
			}
		)
	for row in payload.get("emerging_authorities", []):
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"section": "emerging_authority",
				"case_id": authority.get("case_id"),
				"title": authority.get("title"),
				"citation": authority.get("citation"),
				"score": row.get("velocity"),
				"status": row.get("lifecycle_stage"),
				"meta": f'recent={row.get("recent_citing_cases")};prior={row.get("prior_citing_cases")}',
			}
		)
	for row in payload.get("declining_authorities", []):
		authority = row.get("authority") or {}
		writer.writerow(
			{
				"section": "declining_authority",
				"case_id": authority.get("case_id"),
				"title": authority.get("title"),
				"citation": authority.get("citation"),
				"score": row.get("decay"),
				"status": row.get("lifecycle_stage"),
				"meta": f'recent={row.get("recent_citing_cases")};prior={row.get("prior_citing_cases")}',
			}
		)
	for row in payload.get("surprises", []):
		authority = row.get("authority") or {}
		source_case = row.get("source_case") or {}
		writer.writerow(
			{
				"section": "surprise",
				"case_id": authority.get("case_id"),
				"title": authority.get("title"),
				"citation": authority.get("citation"),
				"score": row.get("surprise_score"),
				"status": "",
				"meta": f'source={source_case.get("case_id")};occurrences={row.get("occurrence_count")}',
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="shift-dashboard.csv"'},
	)


@router.get("/citation-map/issues/shifts.csv")
def export_citation_doctrine_shifts(
	category: str,
	value: str,
	limit: int = 10,
	candidate_limit: int = 12,
	start_year: int | None = None,
	end_year: int | None = None,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_doctrine_shifts(
		category=category,
		value=value,
		limit=limit,
		candidate_limit=candidate_limit,
		start_year=start_year,
		end_year=end_year,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"old_case_id",
		"old_title",
		"old_citation",
		"new_case_id",
		"new_title",
		"new_citation",
		"replacement_score",
		"status",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		old_node = row.get("old_authority") or {}
		new_node = row.get("new_authority") or {}
		writer.writerow(
			{
				"old_case_id": old_node.get("case_id"),
				"old_title": old_node.get("title"),
				"old_citation": old_node.get("citation"),
				"new_case_id": new_node.get("case_id"),
				"new_title": new_node.get("title"),
				"new_citation": new_node.get("citation"),
				"replacement_score": row.get("replacement_score"),
				"status": row.get("status"),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": 'attachment; filename="doctrine-shifts.csv"'},
	)


@router.get("/citation-map/authorities/{case_id}/inheritance", response_model=list[CitationMapInheritanceChainResponse])
def get_citation_inheritance_chains(
	case_id: int,
	max_depth: int = 3,
	limit: int = 20,
	per_node_limit: int = 20,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _citation_inheritance_chains(
		db,
		case_id,
		max_depth=max(1, min(6, max_depth)),
		limit=max(1, min(60, limit)),
		per_node_limit=max(1, min(100, per_node_limit)),
		min_occurrences=max(1, min(50, min_occurrences)),
	)


@router.get("/citation-map/authorities/{case_id}/inheritance.csv")
def export_citation_inheritance_chains(
	case_id: int,
	max_depth: int = 3,
	limit: int = 20,
	per_node_limit: int = 20,
	min_occurrences: int = 1,
	db: Session = Depends(get_db),
) -> Response:
	rows = get_citation_inheritance_chains(
		case_id=case_id,
		max_depth=max_depth,
		limit=limit,
		per_node_limit=per_node_limit,
		min_occurrences=min_occurrences,
		db=db,
	)
	buffer = io.StringIO(newline="")
	fieldnames = [
		"chain_case_ids",
		"depth",
		"total_occurrences",
		"edge_occurrences",
	]
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	for row in rows:
		writer.writerow(
			{
				"chain_case_ids": ",".join(str(case_id_value) for case_id_value in row.get("chain_case_ids") or []),
				"depth": row.get("depth"),
				"total_occurrences": row.get("total_occurrences"),
				"edge_occurrences": ",".join(str(value) for value in row.get("edge_occurrences") or []),
			}
		)
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="inheritance-chains-{case_id}.csv"'},
	)


@router.get(
	"/citation-map/cases/{source_case_id}/citations/{target_case_id}/summary",
	response_model=CitationMapEdgeSummaryResponse,
)
def get_citation_edge_summary(
	source_case_id: int,
	target_case_id: int,
	context_limit: int = 3,
	variant_limit: int = 5,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	return _citation_edge_summary(
		db,
		source_case_id,
		target_case_id,
		context_limit=max(1, min(20, context_limit)),
		variant_limit=max(1, min(20, variant_limit)),
	)


@router.get(
	"/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts",
	response_model=list[CitationMapContextResponse],
)
def get_citation_contexts(
	source_case_id: int,
	target_case_id: int,
	limit: int = 50,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	return _citation_contexts(db, source_case_id, target_case_id, limit=max(1, min(200, limit)))


@router.get("/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts.csv")
def export_citation_contexts(
	source_case_id: int,
	target_case_id: int,
	db: Session = Depends(get_db),
) -> Response:
	_get_case_or_404(source_case_id, db)
	_get_case_or_404(target_case_id, db)
	rows = _citation_contexts(db, source_case_id, target_case_id, limit=200)
	buffer = io.StringIO(newline="")
	fieldnames = list(CitationMapContextResponse.model_fields)
	writer = csv.DictWriter(buffer, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(rows)
	filename = f"citation-context-{source_case_id}-to-{target_case_id}.csv"
	return Response(
		content="\ufeff" + buffer.getvalue(),
		media_type="text/csv; charset=utf-8",
		headers={"Content-Disposition": f'attachment; filename="{filename}"'},
	)


@router.get("/citation-map/cases/{case_id}/neighborhood", response_model=CitationMapNeighborhoodResponse)
def get_citation_map_neighborhood(
	case_id: int,
	limit: int = 100,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	case = _get_case_or_404(case_id, db)
	return _citation_neighborhood(db, case, limit=max(1, min(500, limit)))


@router.get("/citation-map/cases/{case_id}/similar", response_model=list[CitationMapSimilarCaseResponse])
def get_citation_map_similar_cases(
	case_id: int,
	limit: int = 20,
	min_shared: int = 2,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _similar_cases_by_authority(
		db,
		case_id,
		limit=max(1, min(100, limit)),
		min_shared=max(1, min(50, min_shared)),
	)


@router.get("/citation-map/authorities/{case_id}/co-cited", response_model=list[CitationMapCoCitationResponse])
def get_citation_map_co_cited_authorities(
	case_id: int,
	limit: int = 30,
	db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
	_get_case_or_404(case_id, db)
	return _co_cited_authorities(db, case_id, limit=max(1, min(100, limit)))


@router.get("/a2aj/cases/{a2aj_case_id}", response_model=A2AJCaseResponse)
def get_a2aj_case(a2aj_case_id: str, db: Session = Depends(get_db)) -> A2AJCase:
	a2aj_case = db.scalar(select(A2AJCase).where(A2AJCase.a2aj_case_id == a2aj_case_id))
	if a2aj_case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="A2AJ case not found")
	return a2aj_case


@router.get("/a2aj/cases/{a2aj_case_id}/edges", response_model=list[A2AJCitationEdgeResponse])
def get_a2aj_case_edges(a2aj_case_id: str, db: Session = Depends(get_db)) -> list[A2AJCitationEdgeResponse]:
	rows = list(
		db.execute(
			select(A2AJCitationEdge).where(A2AJCitationEdge.source_a2aj_case_id == a2aj_case_id).order_by(A2AJCitationEdge.id)
		)
	)
	return [A2AJCitationEdgeResponse.model_validate(edge, from_attributes=True) for edge, in rows]


@router.get("/a2aj/cases/{a2aj_case_id}/map", response_model=A2AJCaseMapResponse)
def get_a2aj_case_map(a2aj_case_id: str, db: Session = Depends(get_db)) -> A2AJCaseMap:
	mapping = db.scalar(select(A2AJCaseMap).where(A2AJCaseMap.a2aj_case_id == a2aj_case_id))
	if mapping is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="A2AJ case map not found")
	return mapping


@router.post("/a2aj/citation-network/build-map", response_model=dict[str, int])
def build_a2aj_case_map_endpoint(db: Session = Depends(get_db)) -> dict[str, int]:
	updated = _build_a2aj_case_map(db)
	return {"a2aj_case_map_updated": updated}


@router.post("/a2aj/citation-network/convert", response_model=dict[str, int])
def convert_a2aj_edges_endpoint(db: Session = Depends(get_db)) -> dict[str, int]:
	inserted = _convert_a2aj_edges_to_local(db)
	return {"citations_inserted": inserted}


def _quick_search_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>Quick Semantic Search</title>
	<style>
		:root {
			--bg: #f2f5f7;
			--card: #ffffff;
			--ink: #1e2a33;
			--muted: #5f6f7a;
			--accent: #0a7a73;
			--accent-2: #0c5eaf;
			--border: #d6e0e6;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 12% 10%, #e6f4f2 0, transparent 30%),
				radial-gradient(circle at 82% 88%, #e7eef8 0, transparent 34%),
				var(--bg);
			min-height: 100vh;
		}
		.wrap {
			max-width: 1080px;
			margin: 0 auto;
			padding: 22px;
		}
		h1 {
			margin: 0 0 8px;
			font-size: clamp(1.5rem, 2.4vw, 2.2rem);
		}
		.sub {
			margin: 0 0 18px;
			color: var(--muted);
		}
		.grid {
			display: grid;
			grid-template-columns: minmax(0, 1fr);
			gap: 14px;
		}
		.card {
			background: var(--card);
			border: 1px solid var(--border);
			border-radius: 14px;
			padding: 14px;
			box-shadow: 0 8px 24px rgba(13, 33, 48, 0.08);
		}
		.row {
			display: grid;
			grid-template-columns: 1fr 180px 170px;
			gap: 10px;
		}
		.filters {
			display: grid;
			grid-template-columns: 1fr 1fr 1fr;
			gap: 10px;
			margin-top: 10px;
		}
		label {
			display: block;
			margin: 4px 0;
			font-size: 0.85rem;
			color: var(--muted);
		}
		input, select, button {
			width: 100%;
			border: 1px solid var(--border);
			border-radius: 10px;
			padding: 10px;
			font: inherit;
		}
		button {
			cursor: pointer;
			border: none;
			color: #fff;
			font-weight: 700;
			background: linear-gradient(135deg, var(--accent), var(--accent-2));
		}
		.status {
			margin-top: 10px;
			font-size: 0.88rem;
			color: var(--muted);
		}
		.result {
			border: 1px solid var(--border);
			border-radius: 12px;
			padding: 12px;
			margin-top: 12px;
			background: #fcfeff;
		}
		.result h3 {
			margin: 0;
			font-size: 1rem;
		}
		.meta {
			margin-top: 3px;
			font-size: 0.82rem;
			color: var(--muted);
		}
		.chunks {
			margin-top: 8px;
			display: grid;
			gap: 8px;
		}
		.chunk {
			padding: 10px;
			border: 1px solid var(--border);
			border-radius: 10px;
			background: #fff;
			font-size: 0.88rem;
			line-height: 1.45;
		}
		.chunk-head {
			font-size: 0.78rem;
			font-weight: 700;
			color: #2f4b5f;
			margin-bottom: 4px;
		}
		@media (max-width: 860px) {
			.row,
			.filters {
				grid-template-columns: 1fr;
			}
		}
	</style>
</head>
<body>
	<div class="wrap">
		<h1>Quick Semantic Search</h1>
		<p class="sub">Chunk-level semantic and hybrid retrieval over the current case library.</p>

		<section class="card">
			<div class="row">
				<div>
					<label for="query">Query</label>
					<input id="query" type="text" value="non-refoulement risk on return" />
				</div>
				<div>
					<label for="mode">Mode</label>
					<select id="mode">
						<option value="semantic" selected>semantic</option>
						<option value="hybrid">hybrid</option>
						<option value="lexical">lexical</option>
						<option value="metadata">metadata</option>
					</select>
				</div>
				<div>
					<label for="pageSize">Cases</label>
					<input id="pageSize" type="number" min="1" max="20" value="8" />
				</div>
			</div>

			<div class="filters">
				<div>
					<label for="court">Court contains</label>
					<input id="court" type="text" placeholder="Federal Court" />
				</div>
				<div>
					<label for="sourceType">Source type</label>
					<input id="sourceType" type="text" placeholder="a2aj_curated" />
				</div>
				<div>
					<label for="citationContains">Citation contains</label>
					<input id="citationContains" type="text" placeholder="FC" />
				</div>
			</div>

			<button id="searchBtn">Search</button>
			<div id="status" class="status">Ready.</div>
		</section>

		<section id="results"></section>
	</div>

	<script>
		function clip(text, maxLen) {
			const compact = (text || "").replace(/\\s+/g, " ").trim();
			if (compact.length <= maxLen) return compact;
			return compact.slice(0, maxLen - 1) + "...";
		}

		function renderResults(payload) {
			const results = document.getElementById("results");
			results.innerHTML = "";
			const cases = payload.cases || [];
			if (!cases.length) {
				results.innerHTML = '<section class="card"><div class="status">No results found.</div></section>';
				return;
			}

			for (const item of cases) {
				const card = document.createElement("section");
				card.className = "card result";
				const citation = item.citation ? ` | ${item.citation}` : "";
				card.innerHTML = `
					<h3>${item.title}</h3>
					<div class="meta">score=${item.best_similarity.toFixed(4)} | ${item.court}${citation}</div>
					<div class="chunks"></div>
				`;
				const chunksEl = card.querySelector(".chunks");
				for (const chunk of item.chunks || []) {
					const node = document.createElement("div");
					node.className = "chunk";
					node.innerHTML = `
						<div class="chunk-head">chunk ${chunk.chunk_index} | score=${chunk.similarity.toFixed(4)}</div>
						<div>${clip(chunk.chunk_text, 420)}</div>
					`;
					chunksEl.appendChild(node);
				}
				results.appendChild(card);
			}
		}

		async function runSearch() {
			const statusEl = document.getElementById("status");
			const query = document.getElementById("query").value.trim();
			if (!query) {
				statusEl.textContent = "Enter a query first.";
				return;
			}

			const payload = {
				query,
				search_mode: document.getElementById("mode").value,
				page: 1,
				page_size: Number(document.getElementById("pageSize").value || 8),
				max_chunks_per_case: 2,
				candidate_pool: 150,
				court: document.getElementById("court").value || null,
				source_type: document.getElementById("sourceType").value || null,
				citation_contains: document.getElementById("citationContains").value || null,
			};

			statusEl.textContent = "Searching...";
			try {
				const response = await fetch("/search/chunks/grouped", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				if (!response.ok) {
					const body = await response.text();
					throw new Error(`Search failed (${response.status}): ${body}`);
				}
				const result = await response.json();
				statusEl.textContent = `Found ${result.total_cases} case matches from ${result.total_chunks} candidate chunks.`;
				renderResults(result);
			} catch (error) {
				statusEl.textContent = String(error);
			}
		}

		document.getElementById("searchBtn").addEventListener("click", runSearch);
		document.getElementById("query").addEventListener("keydown", (event) => {
			if (event.key === "Enter") {
				event.preventDefault();
				runSearch();
			}
		});
	</script>
</body>
</html>
"""


@router.get("/quick-search", response_class=HTMLResponse, include_in_schema=False)
def quick_search_interface() -> HTMLResponse:
	return HTMLResponse(content=_quick_search_page_html(), status_code=status.HTTP_200_OK)


@router.get("/testing", response_class=HTMLResponse, include_in_schema=False)
def testing_interface() -> HTMLResponse:
	return HTMLResponse(content=_testing_page_html(), status_code=status.HTTP_200_OK)


@router.get("/prototype", response_class=HTMLResponse, include_in_schema=False)
def prototype_interface() -> HTMLResponse:
	return HTMLResponse(content=_prototype_page_html(), status_code=status.HTTP_200_OK)


@router.get("/prototype/summary", response_model=dict[str, Any])
def prototype_summary(db: Session = Depends(get_db)) -> dict[str, Any]:
	ids = _prototype_case_ids()
	if not ids:
		return {
			"prototype_set": PROTOTYPE_SET_NAME,
			"total_cases": 0,
			"embedded_cases": 0,
			"chunked_cases": 0,
			"citation_nodes": 0,
			"citation_edges": 0,
			"topic_distribution": {},
		}

	cases = list(db.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.id)))
	case_ids = [case.id for case in cases]
	embedded = sum(1 for case in cases if case.processing_status == "embedded" and case.embedding is not None)
	chunked = db.scalar(select(func.count(func.distinct(CaseChunk.case_id))).where(CaseChunk.case_id.in_(case_ids))) or 0

	citation_edges = _prototype_edges_count()

	topic_distribution: dict[str, int] = {}
	for case in cases:
		for topic in _case_topic_keywords(case):
			topic_distribution[topic] = topic_distribution.get(topic, 0) + 1

	return {
		"prototype_set": PROTOTYPE_SET_NAME,
		"total_cases": len(cases),
		"embedded_cases": embedded,
		"chunked_cases": int(chunked),
		"citation_nodes": len(cases),
		"citation_edges": int(citation_edges),
		"topic_distribution": dict(sorted(topic_distribution.items(), key=lambda item: item[0])),
	}


@router.get("/prototype/cases", response_model=dict[str, Any])
def prototype_cases(
	q: str | None = None,
	topic: str | None = None,
	page: int = 1,
	page_size: int = 20,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	if page < 1:
		page = 1
	page_size = max(5, min(100, page_size))

	ids = _prototype_case_ids()
	if not ids:
		return {"total": 0, "page": page, "page_size": page_size, "items": []}

	rows = list(db.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.date.desc(), Case.id.desc())))
	chunks = list(db.execute(
		select(CaseChunk.case_id, func.count(CaseChunk.id))
		.where(CaseChunk.case_id.in_(ids))
		.group_by(CaseChunk.case_id)
	))
	chunk_counts = {case_id: int(count) for case_id, count in chunks}

	query = (q or "").strip().lower()
	topic_filter = (topic or "").strip()

	filtered: list[Case] = []
	for case in rows:
		topics = _case_topic_keywords(case)
		if topic_filter and topic_filter not in topics:
			continue
		if query:
			document = " ".join(
				[
					(case.title or ""),
					(case.citation or ""),
					(case.summary or ""),
					(case.full_text or ""),
				]
			).lower()
			if query not in document:
				continue
		filtered.append(case)

	total = len(filtered)
	if total > 0 and (page - 1) * page_size >= total:
		page = 1
	start = (page - 1) * page_size
	end = start + page_size
	slice_rows = filtered[start:end]

	items = [
		{
			"case_id": case.id,
			"citation": case.citation,
			"title": case.title,
			"court": case.court,
			"date": case.date.isoformat() if case.date else None,
			"processing_status": case.processing_status,
			"topic_keywords": _case_topic_keywords(case),
			"chunk_count": chunk_counts.get(case.id, 0),
		}
		for case in slice_rows
	]

	return {
		"total": total,
		"page": page,
		"page_size": page_size,
		"items": items,
	}


@router.get("/prototype/graph", response_model=dict[str, Any])
def prototype_graph(
	max_nodes: int = 160,
	topic: str | None = None,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	max_nodes = max(30, min(280, max_nodes))

	ids = _prototype_case_ids()
	if not ids:
		return {"nodes": [], "edges": [], "meta": {"total_nodes": 0, "total_edges": 0, "returned_nodes": 0, "returned_edges": 0}}

	case_rows = list(db.scalars(select(Case).where(Case.id.in_(ids)).order_by(Case.id)))
	if not case_rows:
		return {"nodes": [], "edges": [], "meta": {"total_nodes": 0, "total_edges": 0, "returned_nodes": 0, "returned_edges": 0}}

	case_by_id = {case.id: case for case in case_rows}
	case_id_set = set(case_by_id.keys())
	edges = [edge for edge in _prototype_edges() if edge[0] in case_id_set and edge[1] in case_id_set]

	in_degree: dict[int, int] = {}
	out_degree: dict[int, int] = {}
	neighbors: dict[int, set[int]] = {}
	for source_case_id, target_case_id, _ in edges:
		out_degree[source_case_id] = out_degree.get(source_case_id, 0) + 1
		in_degree[target_case_id] = in_degree.get(target_case_id, 0) + 1
		neighbors.setdefault(source_case_id, set()).add(target_case_id)
		neighbors.setdefault(target_case_id, set()).add(source_case_id)

	topic_filter = (topic or "").strip()
	base_ids = list(case_id_set)
	if topic_filter:
		base_ids = [
			case_id
			for case_id, case in case_by_id.items()
			if topic_filter in _case_topic_keywords(case)
		]

	if not base_ids:
		return {
			"nodes": [],
			"edges": [],
			"meta": {
				"total_nodes": len(case_rows),
				"total_edges": len(edges),
				"returned_nodes": 0,
				"returned_edges": 0,
			},
		}

	selected: set[int] = set()
	for case_id in sorted(base_ids, key=lambda cid: (-(in_degree.get(cid, 0) + out_degree.get(cid, 0)), cid)):
		if len(selected) >= max_nodes:
			break
		selected.add(case_id)

	if len(selected) < max_nodes:
		for case_id in sorted(base_ids, key=lambda cid: (-(in_degree.get(cid, 0) + out_degree.get(cid, 0)), cid)):
			if len(selected) >= max_nodes:
				break
			for neighbor in neighbors.get(case_id, set()):
				if len(selected) >= max_nodes:
					break
				selected.add(neighbor)

	if len(selected) < max_nodes:
		for case_id in sorted(case_id_set, key=lambda cid: (-(in_degree.get(cid, 0) + out_degree.get(cid, 0)), cid)):
			if len(selected) >= max_nodes:
				break
			selected.add(case_id)

	nodes_payload = []
	for case_id in sorted(selected):
		case = case_by_id.get(case_id)
		if case is None:
			continue
		topics = _case_topic_keywords(case)
		nodes_payload.append(
			{
				"id": case.id,
				"citation": case.citation,
				"title": case.title,
				"court": case.court,
				"date": case.date.isoformat() if case.date else None,
				"topics": topics,
				"in_degree": in_degree.get(case.id, 0),
				"out_degree": out_degree.get(case.id, 0),
				"degree": in_degree.get(case.id, 0) + out_degree.get(case.id, 0),
			}
		)

	selected_edges = [
		{
			"source": source_case_id,
			"target": target_case_id,
			"citation": normalized_citation,
		}
		for source_case_id, target_case_id, normalized_citation in edges
		if source_case_id in selected and target_case_id in selected
	]

	return {
		"nodes": nodes_payload,
		"edges": selected_edges,
		"meta": {
			"prototype_set": PROTOTYPE_SET_NAME,
			"topic": topic_filter or None,
			"max_nodes": max_nodes,
			"total_nodes": len(case_rows),
			"total_edges": len(edges),
			"returned_nodes": len(nodes_payload),
			"returned_edges": len(selected_edges),
		},
	}


@router.post("/search", response_model=list[CaseSearchResponse])
def search_cases(
	search: CaseSearchRequest, db: Session = Depends(get_db)
) -> list[CaseSearchResponse]:
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode)

	query_vector = _embed(search.query) if effective_mode in {"semantic", "hybrid"} else None
	semantic_distance = (
		Case.embedding.cosine_distance(query_vector).label("semantic_distance")
		if query_vector is not None
		else None
	)
	lexical_rank = _case_lexical_rank_expr(search.query).label("lexical_rank")
	graph_in_degree = func.coalesce(CitationMetrics.in_degree, 0).label("graph_in_degree")

	statement = (
		select(Case, semantic_distance, lexical_rank, graph_in_degree)
		if semantic_distance is not None
		else select(Case, lexical_rank, graph_in_degree)
	)
	statement = statement.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
	if effective_mode in {"semantic", "hybrid"}:
		statement = statement.where(Case.embedding.is_not(None))
	statement = _apply_case_filters(statement, search)

	count_statement = statement.order_by(None).limit(None).offset(None)
	if effective_mode in {"lexical", "metadata"}:
		statement = statement.order_by(lexical_rank.desc())
	else:
		statement = statement.order_by(semantic_distance)

	total_matches = db.scalar(select(func.count()).select_from(count_statement.subquery())) or 0
	raw_rows = list(db.execute(statement))
	prepared_rows: list[tuple[Case, float, float]] = []
	max_lexical = 0.0

	for row in raw_rows:
		if effective_mode in {"semantic", "hybrid"}:
			if len(row) == 4:
				case, semantic_distance_value, lexical_rank_value, graph_in_degree_value = row
			else:
				case, semantic_distance_value, lexical_rank_value = row
				graph_in_degree_value = 0
		else:
			if len(row) == 3:
				case, lexical_rank_value, graph_in_degree_value = row
			else:
				case, lexical_rank_value = row
				graph_in_degree_value = 0
			semantic_distance_value = None

		semantic_similarity = (
			max(0.0, min(1.0, 1.0 - float(semantic_distance_value)))
			if semantic_distance_value is not None
			else 0.0
		)
		lexical_score = max(0.0, float(lexical_rank_value or 0.0))
		max_lexical = max(max_lexical, lexical_score)
		prepared_rows.append((case, semantic_similarity, lexical_score))

	weighted_rows: list[tuple[Case, float, float]] = []
	for case, semantic_similarity, lexical_score in prepared_rows:
		lexical_similarity = lexical_score / max_lexical if max_lexical > 0 else 0.0
		if effective_mode == "semantic":
			final_score = semantic_similarity
		elif effective_mode in {"lexical", "metadata"}:
			final_score = lexical_similarity
		else:
			denominator = search.semantic_weight + search.lexical_weight
			final_score = (
				(search.semantic_weight * semantic_similarity) + (search.lexical_weight * lexical_similarity)
			) / denominator
		graph_boost = min(0.05, math.log1p(max(0, graph_in_degree_value)) / 100.0)
		weighted_rows.append((case, final_score, final_score + graph_boost))

	weighted_rows.sort(key=lambda item: item[2], reverse=True)
	start = (search.page - 1) * search.page_size
	end = start + search.page_size
	page_rows = weighted_rows[start:end]

	return [
		CaseSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			similarity=score,
			match_source=_case_match_source(case, search.query, effective_mode),
		)
		for case, score, _ in page_rows
	]


@router.post("/search/chunks", response_model=list[ChunkSearchResponse])
def search_chunks(
	search: CaseSearchRequest, db: Session = Depends(get_db)
) -> list[ChunkSearchResponse]:
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode)

	if effective_mode in {"lexical", "metadata"}:
		lexical_rank = _chunk_lexical_rank_expr(search.query).label("lexical_rank")
		statement = (
			select(Case, CaseChunk, lexical_rank)
			.join(CaseChunk, CaseChunk.case_id == Case.id)
			.order_by(lexical_rank.desc())
			.offset((search.page - 1) * search.page_size)
			.limit(search.page_size)
		)
	else:
		distance = CaseChunk.embedding.cosine_distance(_embed(search.query)).label("distance")
		statement = (
			select(Case, CaseChunk, distance)
			.join(CaseChunk, CaseChunk.case_id == Case.id)
			.where(CaseChunk.embedding.is_not(None))
			.order_by(distance)
			.offset((search.page - 1) * search.page_size)
			.limit(search.page_size)
		)
	statement = _apply_case_filters(statement, search)

	rows = list(db.execute(statement))
	if effective_mode in {"lexical", "metadata"}:
		max_lexical = max((float(rank or 0.0) for _, _, rank in rows), default=0.0)
		return [
			ChunkSearchResponse(
				**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
				chunk_index=chunk.chunk_index,
				chunk_text=chunk.text,
				similarity=(max(0.0, float(rank or 0.0)) / max_lexical if max_lexical > 0 else 0.0),
			)
			for case, chunk, rank in rows
		]

	return [
		ChunkSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			chunk_index=chunk.chunk_index,
			chunk_text=chunk.text,
			similarity=max(0.0, min(1.0, 1.0 - float(distance_value))),
		)
		for case, chunk, distance_value in rows
	]


@lru_cache(maxsize=2)
def _local_embedding_provider(model_name: str) -> SentenceTransformerEmbeddingProvider:
	return SentenceTransformerEmbeddingProvider(model_name=model_name)


@router.post("/search/chunks/local", response_model=list[ChunkSearchResponse])
def search_chunks_local(
	search: LocalChunkSearchRequest,
	db: Session = Depends(get_db),
) -> list[ChunkSearchResponse]:
	if not AI_ROLLOUT["local_semantic_enabled"]:
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="Local semantic search is disabled by rollout configuration",
		)
	_validate_search_ranges(search)
	query_vector = _local_embedding_provider(search.model_name).embed_query(search.query)
	distance = CaseChunkEmbedding.embedding.cosine_distance(query_vector).label("distance")
	statement = (
		select(Case, CaseChunk, distance)
		.join(CaseChunk, CaseChunk.case_id == Case.id)
		.join(CaseChunkEmbedding, CaseChunkEmbedding.chunk_id == CaseChunk.id)
		.where(CaseChunkEmbedding.model_name == search.model_name)
		.order_by(distance)
		.offset((search.page - 1) * search.page_size)
		.limit(search.page_size)
	)
	statement = _apply_case_filters(statement, search)
	rows = list(db.execute(statement))
	return [
		ChunkSearchResponse(
			**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
			chunk_index=chunk.chunk_index,
			chunk_text=chunk.text,
			similarity=max(0.0, min(1.0, 1.0 - float(distance_value))),
		)
		for case, chunk, distance_value in rows
	]


def _grouped_chunk_search(
	search: ChunkGroupSearchRequest, db: Session
) -> GroupedChunkSearchResponse:
	"""Inner retrieval shared by /search/chunks/grouped and /research."""
	_validate_search_ranges(search)
	effective_mode = _effective_search_mode(search.search_mode)

	query_vector = _embed(search.query) if effective_mode in {"semantic", "hybrid"} else None
	semantic_distance = (
		CaseChunk.embedding.cosine_distance(query_vector).label("semantic_distance")
		if query_vector is not None
		else None
	)
	lexical_rank = _chunk_lexical_rank_expr(search.query).label("lexical_rank")

	statement = (
		select(Case, CaseChunk, semantic_distance, lexical_rank)
		if semantic_distance is not None
		else select(Case, CaseChunk, lexical_rank)
	)
	statement = statement.join(CaseChunk, CaseChunk.case_id == Case.id)
	if effective_mode in {"semantic", "hybrid"}:
		statement = statement.where(CaseChunk.embedding.is_not(None))
	statement = _apply_case_filters(statement, search)

	chunk_scan_limit = min(
		500,
		max(search.candidate_pool, search.page_size * search.max_chunks_per_case * 5),
	)
	if effective_mode in {"lexical", "metadata"}:
		statement = statement.order_by(lexical_rank.desc()).limit(chunk_scan_limit)
	else:
		statement = statement.order_by(semantic_distance).limit(chunk_scan_limit)

	raw_rows = list(db.execute(statement))
	prepared_rows: list[tuple[Case, CaseChunk, float, float]] = []
	max_lexical = 0.0

	for row in raw_rows:
		if effective_mode in {"semantic", "hybrid"}:
			case, chunk, semantic_distance_value, lexical_rank_value = row
		else:
			case, chunk, lexical_rank_value = row
			semantic_distance_value = None

		semantic_similarity = (
			max(0.0, min(1.0, 1.0 - float(semantic_distance_value)))
			if semantic_distance_value is not None
			else 0.0
		)
		lexical_score = max(0.0, float(lexical_rank_value or 0.0))
		max_lexical = max(max_lexical, lexical_score)
		prepared_rows.append((case, chunk, semantic_similarity, lexical_score))

	grouped: dict[int, GroupedChunkCaseResponse] = {}
	for case, chunk, semantic_similarity, lexical_score in prepared_rows:
		lexical_similarity = lexical_score / max_lexical if max_lexical > 0 else 0.0
		if effective_mode == "semantic":
			final_similarity = semantic_similarity
		elif effective_mode in {"lexical", "metadata"}:
			final_similarity = lexical_similarity
		else:
			denominator = search.semantic_weight + search.lexical_weight
			final_similarity = (
				(search.semantic_weight * semantic_similarity) + (search.lexical_weight * lexical_similarity)
			) / denominator

		case_id = case.id
		entry = grouped.get(case_id)
		if entry is None:
			entry = GroupedChunkCaseResponse(
				**CaseResponse.model_validate(case, from_attributes=True).model_dump(),
				best_similarity=final_similarity,
				chunks=[],
			)
			grouped[case_id] = entry
		entry.best_similarity = max(entry.best_similarity, final_similarity)
		entry.chunks.append(
			ChunkPassage(
				chunk_index=chunk.chunk_index,
				chunk_text=chunk.text,
				similarity=final_similarity,
			)
		)

	grouped_cases = list(grouped.values())
	for item in grouped_cases:
		item.chunks.sort(key=lambda c: c.similarity, reverse=True)
		item.chunks = item.chunks[: search.max_chunks_per_case]
	grouped_cases.sort(key=lambda c: c.best_similarity, reverse=True)

	start = (search.page - 1) * search.page_size
	end = start + search.page_size
	paged_cases = grouped_cases[start:end]

	return GroupedChunkSearchResponse(
		total_cases=len(grouped_cases),
		total_chunks=len(raw_rows),
		max_chunks_per_case=search.max_chunks_per_case,
		cases=paged_cases,
	)


@router.post("/search/chunks/grouped", response_model=GroupedChunkSearchResponse)
def search_chunks_grouped(
	search: ChunkGroupSearchRequest, db: Session = Depends(get_db)
) -> GroupedChunkSearchResponse:
	return _grouped_chunk_search(search, db)


_CONTEXT_CHAR_LIMIT = 12_000
_RESEARCH_DISCLAIMER = (
	"Research aid only — not legal advice. "
	"Sources are unofficial copies; verify against authoritative records."
)


def _research_page_html() -> str:
	return """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<title>Legal Research</title>
	<style>
		:root {
			--bg: #f4efe6;
			--panel: #fffaf0;
			--ink: #1e1b16;
			--muted: #5d5547;
			--accent: #0d6a5f;
			--accent-2: #b65d2e;
			--line: #d8cebf;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", "Source Sans 3", sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 10% 8%, #f0e5d4 0, transparent 34%),
				radial-gradient(circle at 90% 88%, #d9ece8 0, transparent 35%),
				var(--bg);
		}
		.wrap { max-width: 980px; margin: 0 auto; padding: 22px; }
		nav { display: flex; gap: 14px; margin-bottom: 18px; font-size: 0.88rem; }
		nav a { color: var(--accent); text-decoration: none; }
		nav a:hover { text-decoration: underline; }
		h1 { margin: 0 0 6px; font-size: clamp(1.55rem, 2.4vw, 2.1rem); }
		.lead { margin: 0 0 18px; color: var(--muted); font-size: 0.93rem; }
		.card {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 12px;
			padding: 16px;
			margin-bottom: 14px;
		}
		.card h2 { margin: 0 0 10px; font-size: 1rem; }
		label { display: block; font-size: 0.82rem; color: var(--muted); margin-bottom: 4px; }
		textarea, input, select {
			width: 100%; border: 1px solid var(--line); border-radius: 8px;
			padding: 9px 10px; font-size: 0.92rem; background: #fff; font-family: inherit;
		}
		textarea { resize: vertical; min-height: 80px; }
		button {
			width: 100%; border: none; border-radius: 8px;
			padding: 10px; font-size: 0.94rem; font-weight: 600; cursor: pointer;
			background: linear-gradient(135deg, var(--accent), #14867a); color: #fff;
		}
		button:disabled { opacity: 0.55; cursor: not-allowed; }
		.grid2 { display: grid; gap: 12px; grid-template-columns: 1fr 1fr; }
		.grid3 { display: grid; gap: 12px; grid-template-columns: 1fr 1fr 1fr; }
		.answer-box {
			white-space: pre-wrap;
			background: #fff;
			border: 1px solid var(--line);
			border-radius: 8px;
			padding: 14px;
			font-size: 0.93rem;
			line-height: 1.65;
			min-height: 60px;
		}
		.source-card {
			background: #fff;
			border: 1px solid var(--line);
			border-radius: 8px;
			padding: 12px;
			margin-top: 10px;
		}
		.source-title { font-weight: 600; font-size: 0.95rem; }
		.source-meta { color: var(--muted); font-size: 0.81rem; margin: 3px 0 8px; }
		.excerpt {
			background: #f9f0e2;
			border-left: 3px solid var(--accent);
			padding: 8px 10px;
			font-size: 0.86rem;
			line-height: 1.55;
			margin-top: 6px;
			border-radius: 0 6px 6px 0;
			white-space: pre-wrap;
		}
		summary { cursor: pointer; font-size: 0.83rem; color: var(--accent); margin-top: 6px; }
		.disclaimer {
			font-size: 0.78rem;
			color: var(--muted);
			margin-top: 18px;
			padding: 10px 12px;
			border: 1px solid var(--line);
			border-radius: 8px;
			background: #f9f2e8;
		}
		.token-info { font-size: 0.78rem; color: var(--muted); margin-top: 6px; }
		@media (max-width: 640px) {
			.grid2, .grid3 { grid-template-columns: 1fr; }
		}
	</style>
</head>
<body>
	<div class="wrap">
		<nav>
			<a href="/prototype">Prototype Explorer</a>
			<a href="/testing">API Tester</a>
		</nav>
		<h1>Legal Research</h1>
		<p class="lead">Ask a research question. Answers are grounded in the prototype immigration cohort.</p>

		<div class="card">
			<h2>Research Question</h2>
			<div style="margin-bottom:10px;">
				<label for="question">Question</label>
				<textarea id="question" placeholder="e.g. What is the legal test for refugee protection under section 96 of the IRPA?"></textarea>
			</div>
			<div class="grid3" style="margin-bottom:12px;">
				<div>
					<label for="sourceType">Cohort (source_type)</label>
					<input id="sourceType" type="text" value="a2aj_immigration_core" />
				</div>
				<div>
					<label for="maxCases">Max source cases (1–10)</label>
					<input id="maxCases" type="number" min="1" max="10" value="5" />
				</div>
				<div>
					<label for="searchMode">Search mode</label>
					<select id="searchMode">
						<option value="semantic">Semantic</option>
						<option value="hybrid" selected>Hybrid</option>
						<option value="lexical">Lexical</option>
					</select>
				</div>
			</div>
			<button id="submitBtn" onclick="runResearch()">Run Research</button>
		</div>

		<div id="resultSection" style="display:none;">
			<div class="card">
				<h2>Answer</h2>
				<div id="answerBox" class="answer-box"></div>
				<div id="tokenInfo" class="token-info"></div>
			</div>
			<div class="card">
				<h2>Sources</h2>
				<div id="sourcesBox"></div>
			</div>
		</div>

		<div class="disclaimer">
			Research aid only — not legal advice. Sources are unofficial copies; verify against authoritative records.
		</div>
	</div>

	<script>
		function esc(value) {
			return String(value ?? "")
				.replace(/&/g, "&amp;")
				.replace(/</g, "&lt;")
				.replace(/>/g, "&gt;")
				.replace(/\"/g, "&quot;")
				.replace(/'/g, "&#39;");
		}

		function renderSources(sources) {
			if (!Array.isArray(sources) || sources.length === 0) {
				document.getElementById("sourcesBox").innerHTML = "<p style='color:var(--muted);'>No sources returned.</p>";
				return;
			}
			const cards = sources.map((src, i) => {
				const excerptHtml = (src.excerpts || []).map((ex, j) => `
					<div class="excerpt">${esc(ex)}</div>
				`).join("");
				const sourceLink = src.source_url
					? `<a href="${esc(src.source_url)}" target="_blank" rel="noopener noreferrer">${esc(src.source_url)}</a>`
					: "";
				return `
					<div class="source-card">
						<div class="source-title">${esc(src.title || "Untitled")}</div>
						<div class="source-meta">
							${esc(src.citation || "No citation")}
							${src.court ? ` &middot; ${esc(src.court)}` : ""}
							${src.date ? ` &middot; ${esc(src.date)}` : ""}
							${src.source_url ? ` &middot; ${sourceLink}` : ""}
							&middot; Case ID ${esc(src.case_id)}
						</div>
						<details>
							<summary>${(src.excerpts || []).length} excerpt(s) used in context</summary>
							${excerptHtml}
						</details>
					</div>
				`;
			}).join("");
			document.getElementById("sourcesBox").innerHTML = cards;
		}

		async function runResearch() {
			const question = document.getElementById("question").value.trim();
			if (!question) {
				alert("Please enter a research question.");
				return;
			}

			const btn = document.getElementById("submitBtn");
			btn.disabled = true;
			btn.textContent = "Researching…";
			document.getElementById("resultSection").style.display = "none";

			const payload = {
				query: question,
				max_cases: Math.max(1, Math.min(10, Number(document.getElementById("maxCases").value) || 5)),
				search_mode: document.getElementById("searchMode").value,
			};
			const sourceType = document.getElementById("sourceType").value.trim();
			if (sourceType) {
				payload.source_type = sourceType;
			}

			try {
				const response = await fetch("/research", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify(payload),
				});
				const body = await response.json().catch(() => ({ detail: "No JSON response body" }));

				if (!response.ok) {
					document.getElementById("answerBox").textContent =
						`Error ${response.status}: ${body.detail || response.statusText}`;
					document.getElementById("sourcesBox").innerHTML = "";
					document.getElementById("tokenInfo").textContent = "";
					document.getElementById("resultSection").style.display = "block";
					return;
				}

				document.getElementById("answerBox").textContent = body.answer || "(No answer returned)";
				document.getElementById("tokenInfo").textContent =
					`Model: ${body.model_used} · Prompt tokens: ${body.prompt_tokens} · Completion tokens: ${body.completion_tokens}`;
				renderSources(body.sources || []);
				document.getElementById("resultSection").style.display = "block";
			} catch (err) {
				document.getElementById("answerBox").textContent = `Request error: ${err.message}`;
				document.getElementById("sourcesBox").innerHTML = "";
				document.getElementById("resultSection").style.display = "block";
			} finally {
				btn.disabled = false;
				btn.textContent = "Run Research";
			}
		}

		document.addEventListener("keydown", (e) => {
			if (e.key === "Enter" && e.ctrlKey) {
				runResearch();
			}
		});
	</script>
</body>
</html>
"""


@router.get("/research", response_class=HTMLResponse, include_in_schema=False)
def research_interface() -> HTMLResponse:
	return HTMLResponse(content=_research_page_html(), status_code=status.HTTP_200_OK)


@router.post("/research", response_model=ResearchResponse)
def research(search: ResearchRequest, db: Session = Depends(get_db)) -> ResearchResponse:
	result = _grouped_chunk_search(search, db)

	top_cases = result.cases[: search.max_cases]
	if not top_cases:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="No embedded cases matched the query",
		)

	context_parts: list[str] = []
	for group in top_cases:
		header = f"Case: {group.title} [{group.citation or 'No citation'}] ({group.date or 'Unknown date'})"
		body = "\n".join(chunk.chunk_text for chunk in group.chunks)
		context_parts.append(f"{header}\n{body}")

	context = "\n\n---\n\n".join(context_parts)
	if len(context) > _CONTEXT_CHAR_LIMIT:
		context = context[:_CONTEXT_CHAR_LIMIT] + "\n[Context truncated]"

	system_prompt = (
		"You are a Canadian legal research assistant helping lawyers and researchers find relevant case law. "
		"Base your answer ONLY on the case excerpts provided below. "
		"CRITICAL: Only cite cases that are explicitly named in the provided excerpts. "
		"Do NOT draw on your training knowledge to add cases, statutes, or legal tests that are not in the excerpts. "
		"If the excerpts discuss a different but related legal provision (e.g., s. 96 when s. 34 was asked), "
		"say so explicitly and describe only what those cases actually say. "
		"If the excerpts are genuinely insufficient to address the question, say so and suggest the user try a broader or rephrased query. "
		f"{_RESEARCH_DISCLAIMER}"
	)

	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="OPENAI_API_KEY is not configured",
		)

	chat_model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
	try:
		client = OpenAI(api_key=api_key)
		completion = client.chat.completions.create(
			model=chat_model,
			temperature=search.temperature,
			messages=[
				{"role": "system", "content": system_prompt},
				{"role": "user", "content": f"Question: {search.query}\n\nCase excerpts:\n{context}"},
			],
		)
	except OpenAIError as exc:
		raise HTTPException(
			status_code=status.HTTP_502_BAD_GATEWAY,
			detail="The generation service is unavailable",
		) from exc

	answer = completion.choices[0].message.content or ""
	usage = completion.usage

	sources = [
		ResearchSource(
			case_id=group.id,
			title=group.title,
			citation=group.citation,
			court=group.court,
			date=group.date,
			source_url=group.source_url,
			excerpts=[chunk.chunk_text for chunk in group.chunks],
		)
		for group in top_cases
	]

	return ResearchResponse(
		question=search.query,
		answer=answer,
		sources=sources,
		model_used=chat_model,
		prompt_tokens=usage.prompt_tokens if usage else 0,
		completion_tokens=usage.completion_tokens if usage else 0,
	)
