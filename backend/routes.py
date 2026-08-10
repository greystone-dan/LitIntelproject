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
from fastapi.responses import HTMLResponse
from openai import OpenAI, OpenAIError
from sqlalchemy import Text, func, or_, select
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
from .metadata import extract_metadata_matches
from .database import (
	Case,
	CaseChunk,
	CaseChunkEmbedding,
	CaseSource,
	CaseTag,
	Citation,
	CitationMetrics,
	IngestionRun,
	StatuteReference,
	get_db,
)
from .embedding_providers import SentenceTransformerEmbeddingProvider
from .database import A2AJCase, A2AJCaseMap, A2AJCitationEdge
from .ingestion import merge_case_record
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
	if isinstance(metadata.get("topic_keywords"), list):
		values = [str(value) for value in metadata["topic_keywords"] if value]
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
			value = maybe_callable() if callable(maybe_callable) else maybe_callable
		if not value and hasattr(citation, "matched_text"):
			maybe_callable = getattr(citation, "matched_text")
			value = maybe_callable() if callable(maybe_callable) else maybe_callable
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
		("forum", "rad", r"\bRAD\b"),
		("forum", "rpd", r"\bRPD\b"),
		("forum", "irb", r"\bIRB\b"),
		("statute", "irpa", r"\bIRPA\b"),
		("statute", "irpr", r"\bIRPR\b"),
		("analysis", "ifa", r"\bIFA\b"),
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

	for match in re.finditer(r"\[(\d+)\]", content):
		add_row("paragraph_marker", match.group(1), evidence=match.group(0), source="reader_structure")
		if len([row for row in rows if row.key == "paragraph_marker"]) >= 12:
			break

	return rows


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
		source_breakdown=source_breakdown,
		cases=cases,
	)


@router.get("/cases/{case_id}", response_model=CaseResponse)
def get_case(case_id: int, db: Session = Depends(get_db)) -> Case:
	case = db.scalar(select(Case).where(Case.id == case_id))
	if case is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
	return case


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
			.where(CaseChunk.case_id == case_id, CaseChunk.chunk_set.in_(["section", "legacy"]))
			.order_by(CaseChunk.chunk_index)
		)
	)
	if chunks:
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
				if raw.kind not in {"case", "case_short", "case_name", "neutral", "statute", "instrument"}:
					continue
				normalized_key = str(raw.normalized_citation or raw.citation_text or "").strip().lower()
				key = (chunk.id, raw.offset_start, raw.offset_end, normalized_key)
				if key in seen_live:
					continue
				seen_live.add(key)
				citation_responses.append(
					CaseReaderCitationResponse(
						id=next_live_id,
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


def _citation_pass_page_html() -> str:
	return """<!doctype html>
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
		function highlightText(text,ranges){let out='';let cursor=0;for(const range of ranges){if(range.start<cursor||range.start>=text.length)continue;const end=Math.min(range.end,text.length);if(end<=cursor)continue;out+=esc(text.slice(cursor,range.start));const active=state.activeRowKey&&range.rowKey===state.activeRowKey?' active-hit':'';const layerClass=range.layer==='law'?'cite-law':range.layer==='metadata'?'cite-metadata':'cite-case';out+=`<mark class=\"${layerClass}${active}\" data-row-key=\"${esc(range.rowKey)}\" title=\"Click for details: ${esc(range.label)}\">${esc(text.slice(range.start,end))}</mark>`;cursor=end;}out+=esc(text.slice(cursor));return out;}
		function renderHighlights(){if(!state.payload)return;const text=(state.payload.case.full_text||state.payload.case.summary||'').toString();if(!text){document.getElementById('annotatedText').textContent='No case text available.';return;}const ranges=findRanges(text,rowsForView(state.payload));document.getElementById('annotatedText').innerHTML=highlightText(text,ranges);document.querySelectorAll('mark[data-row-key]').forEach(mark=>{mark.onclick=()=>selectReference(String(mark.dataset.rowKey||''));});if(state.activeRowKey){const mark=document.querySelector('mark.active-hit');if(mark)mark.scrollIntoView({behavior:'smooth',block:'center'});}}
		function pinpointFromText(value){const text=String(value||'');const m=text.match(/\bat\s+para(?:s|graph(?:s)?)?\.?\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*\b/i);return m?m[0].replace(/\s+/g,' ').trim():'';}
		function pinpointBadge(row){if(String(row.__layer||'')!=='Case')return '<span class=\"badge\" style=\"opacity:.58\">N/A</span>';const pinpoint=pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text);if(pinpoint){return `<span class=\"badge\" style=\"background:#edf7ed;border-color:#78b27b;color:#1f5c26\" title=\"${esc(pinpoint)}\">Pinpoint</span>`;}return '<span class=\"badge\" style=\"background:#fff4e8;border-color:#d8aa78;color:#8b4e11\" title=\"No at para/paras marker detected\">Missing</span>';}
		function renderRows(cases,laws,metadata){document.getElementById('liveCount').textContent=String(cases.length);document.getElementById('lawCount').textContent=String(laws.length);document.getElementById('metadataCount').textContent=String(metadata.length);document.getElementById('selectedCount').textContent=state.activeRowKey?'1':'0';const casePinpointCount=cases.filter(row=>pinpointFromText(row.normalized_citation)||pinpointFromText(row.citation_text)).length;document.getElementById('tableSummary').textContent=`${cases.length} case citation${cases.length===1?'':'s'} · ${laws.length} statute/law reference${laws.length===1?'':'s'} · ${metadata.length} metadata field${metadata.length===1?'':'s'} · ${casePinpointCount}/${cases.length} case cites with pinpoint.`;const rows=[...cases.map((row,index)=>({...row,__rowKey:`case:${index}`,__layer:'Case'})),...laws.map((row,index)=>({...row,__rowKey:`law:${index}`,__layer:'Law'})),...metadata.map((row,index)=>({...row,kind:row.field,citation_text:row.text,normalized_citation:row.value,__rowKey:`metadata:${index}`,__layer:'Metadata'}))];if(!rows.length)return '<div class=\"empty\">No references extracted.</div>';return `<table><thead><tr><th>#</th><th>Layer</th><th>Kind</th><th>Reference text</th><th>Pinpoint</th><th>Normalized</th><th>Where</th><th>Context</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class=\"clickable ${state.activeRowKey===r.__rowKey?'active-row':''}\" data-row-key=\"${r.__rowKey}\"><td>${i+1}</td><td>${esc(r.__layer)}</td><td>${esc(r.kind||'')}</td><td>${esc(r.citation_text||'')}</td><td>${pinpointBadge(r)}</td><td>${esc(r.normalized_citation||'')}</td><td>${esc(`${r.offset_start??''}-${r.offset_end??''}`)}</td><td>${esc(r.context||'')}</td></tr>`).join('')}</tbody></table>`;}
		function detailField(label,value){return `<div class=\"detail-field\"><small>${esc(label)}</small><strong>${esc(shown(value))}</strong></div>`;}
		function renderDetail(detail){const panel=document.getElementById('detailPanel');if(!detail){panel.innerHTML='<div class=\"empty\">Select a reference to inspect its exact text, document position, chunks, and stored records.</div>';return;}const location=detail.location||{},passage=detail.passage||{},metadata=detail.metadata||null;const chunks=(detail.chunks||[]).map(chunk=>`<details class=\"chunk-detail\"><summary>${esc(chunk.chunk_set)} #${esc(chunk.chunk_index)} · ${esc(shown(chunk.chunk_label))} · chunk id ${esc(chunk.chunk_id)}</summary><div class=\"detail-grid\">${detailField('Paragraph range',chunk.paragraph_start===null?'Not stored':chunk.paragraph_start===chunk.paragraph_end?chunk.paragraph_start:`${chunk.paragraph_start}-${chunk.paragraph_end}`)}${detailField('Chunk offsets',`${chunk.offset_start}-${chunk.offset_end}`)}${detailField('Document offsets',`${chunk.document_start}-${chunk.document_end}`)}${detailField('Text length',chunk.text_length)}${detailField('Token estimate',chunk.token_estimate)}${detailField('Exact chunk match',chunk.citation_text)}</div><pre class=\"detail-text\">${esc(chunk.text)}</pre></details>`).join('')||'<div class=\"record-row\">No stored chunk contains this exact document span.</div>';const records=(detail.stored_records||[]).map(record=>{const target=record.target;const targetHtml=record.target===undefined?'':target?` · resolved to <a href=\"/case-reader?case_id=${encodeURIComponent(target.case_id)}\">${esc(target.title||target.citation||`Case ${target.case_id}`)}</a> (${esc(shown(target.citation))})`:' · no resolved target';return `<div class=\"record-row\"><strong>Record ${esc(record.record_id)}</strong> · ${esc(shown(record.citation_kind))} · chunk ${esc(shown(record.chunk_id))} · offsets ${esc(shown(record.offset_start))}-${esc(shown(record.offset_end))}${record.provenance!==undefined?` · provenance ${esc(shown(record.provenance))}`:''}${record.unresolved!==undefined?` · ${record.unresolved?'unresolved':'resolved flag clear'}`:''}${targetHtml}</div>`;}).join('')||'<div class=\"record-row\">No matching stored record for this extracted occurrence.</div>';panel.innerHTML=`<div class=\"detail-title\"><h2>${esc(detail.citation_text)}</h2><span>${esc(detail.layer)} · ${esc(detail.kind)}</span></div><div class=\"detail-grid\">${detailField('Normalized value',detail.normalized_value)}${detailField('Document offsets',`${detail.offset_start}-${detail.offset_end}`)}${detailField('Span length',detail.span_length)}${detailField('Line / column',`${location.line_number} / ${location.column_number}`)}${detailField('Paragraph',location.paragraph_number)}${detailField('Document position',`${location.position_percent}%`)}${metadata?detailField('Confidence',metadata.confidence)+detailField('Source',metadata.source):''}</div><div class=\"detail-section\"><h3>Line-aligned passage · offsets ${esc(passage.offset_start)}-${esc(passage.offset_end)}</h3><pre class=\"detail-text\">${esc(passage.text)}</pre></div><div class=\"detail-section\"><h3>Containing chunks (${detail.chunks.length})</h3>${chunks}</div><div class=\"detail-section\"><h3>Stored records (${detail.stored_records.length})</h3>${records}</div>`;}
		async function loadDetail(rowKey){const selectedRow=rowsForView(state.payload).find(row=>row.__rowKey===rowKey);if(!selectedRow)return;document.getElementById('detailPanel').innerHTML='<div class=\"empty\">Loading citation details...</div>';const query=new URLSearchParams({layer:selectedRow.__layer,offset_start:String(selectedRow.offset_start),offset_end:String(selectedRow.offset_end)});try{const detail=await json(`/cases/${state.selected}/citation-pass/detail?${query}`);if(state.activeRowKey!==rowKey)return;state.detail=detail;renderDetail(detail);}catch(error){if(state.activeRowKey===rowKey)document.getElementById('detailPanel').innerHTML=`<div class=\"empty\">${esc(error.message)}</div>`;}}
		function selectReference(rowKey){if(!rowKey)return;state.activeRowKey=rowKey;state.detail=null;renderPayload(state.payload);loadDetail(rowKey);}
		function bindRowClicks(){document.querySelectorAll('tr[data-row-key]').forEach(row=>{row.onclick=()=>selectReference(String(row.getAttribute('data-row-key')||''));});}
		function renderPayload(payload){state.payload=payload;const c=payload.case;const s=payload.summary||{};document.getElementById('caseCard').innerHTML=`<div class=\"card-head\"><div><h2 class=\"case-title\">${esc(c.title)}</h2><div class=\"case-meta\">${esc(c.citation||'No citation')} · ${esc(c.court)} · ${esc(c.date)} · id ${c.id}</div></div><div class=\"badges\"><span class=\"badge\"><strong>${s.live_total||0}</strong> case citations</span><span class=\"badge\"><strong>${s.statute_total||0}</strong> statutes/laws</span><span class=\"badge\"><strong>${s.metadata_total||0}</strong> metadata fields</span><span class=\"badge\"><strong>${c.full_text?'Yes':'No'}</strong> full text</span></div></div><div class=\"badges\" style=\"margin-top:14px\"><span class=\"badge\">Orange: cases</span><span class=\"badge\">Green: statutes/laws</span><span class=\"badge\">Blue: metadata</span></div>`;const cases=(payload.live_extracted||[]).map(row=>({...row,context:row.context||''}));const laws=(payload.live_statutes||[]).map(row=>({...row,context:row.context||''}));const metadata=(payload.live_metadata||[]).map(row=>({...row,context:row.context||''}));document.getElementById('citationTables').innerHTML=renderRows(cases,laws,metadata);bindRowClicks();renderHighlights();}
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
	metadata_rows = extract_metadata_matches(full_text)
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
			"context": full_text[max(0, match.offset_start - 40):min(len(full_text), match.offset_end + 40)].replace("\n", " ").strip(),
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
					}
				)
				break
			search_start = chunk_start + 1
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
		matches = extract_metadata_matches(full_text)
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

	citation_text = selected.text if layer == "metadata" else selected.citation_text
	normalized = selected.value if layer == "metadata" else selected.normalized_citation
	kind = selected.field if layer == "metadata" else selected.kind
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
		"stored_records": stored_records,
		"metadata": {
			"confidence": selected.confidence,
			"source": selected.source,
		} if layer == "metadata" else None,
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
	search: CaseSearchRequest, db: Session = Depends(get_db), response: Response = None
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
		prepared_rows.append((case, semantic_similarity, lexical_score, int(graph_in_degree_value or 0)))

	weighted_rows: list[tuple[Case, float, float]] = []
	for case, semantic_similarity, lexical_score, graph_in_degree_value in prepared_rows:
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

	if response is not None:
		response.headers["X-Search-Total"] = str(total_matches)
		response.headers["X-Search-Page"] = str(search.page)
		response.headers["X-Search-Page-Size"] = str(search.page_size)
		response.headers["X-Search-Total-Pages"] = str(max(1, -(-total_matches // search.page_size)))
		response.headers["X-Search-Effective-Mode"] = effective_mode
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
