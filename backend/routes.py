import os
import math
import csv
import io
import re
import httpx
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, File, HTTPException, Query, Response, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from openai import OpenAI, OpenAIError
from bs4 import BeautifulSoup, NavigableString
from sqlalchemy import Text, func, or_, select, text as sql_text
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

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
from .pages.citation_map import citation_map_html
from .pages.citation_pass import citation_pass_page_html
from .pages.data_explorer import data_explorer_page_html
from .pages.judge_outcomes import judge_outcomes_page_html
from .pages.live_analysis import live_analysis_page_html
from .pages.prototype import prototype_page_html
from .pages.quick_search import quick_search_page_html
from .pages.research import research_page_html
from .live_analysis import MAX_DOCX_BYTES, analyze_document
from .pages.testing import testing_page_html
from .citations import build_a2aj_case_map as _build_a2aj_case_map
from .citations import compute_citation_metrics as _compute_citation_metrics
from .citations import convert_a2aj_edges_to_local as _convert_a2aj_edges_to_local
from .citations import extract_case_citation_matches
from .citations import extract_statute_reference_matches
from .citations import parse_legislation_citation
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
	FCActivityClassification,
	FCActivityDocument,
	IngestionRun,
	LegislationDocument,
	LegislationSection,
	StatuteReference,
	get_db,
)
from .embedding_providers import SentenceTransformerEmbeddingProvider
from .database import A2AJCase, A2AJCaseMap, A2AJCitationEdge
from .ingestion import merge_case_record
from .analytics_service import (
	FC_ACTIVITY_DISPLAY_START_YEAR,
	FC_CITY_PROVINCE,
	_ANALYTICS_FIELDS,
	_analytics_case_order_sql,
	_government_party,
	_judge_outcome_counts,
	_profile_reader_metadata,
	fetch_about_stats,
	fetch_analytics_search_case_detail,
	fetch_analytics_search_cases,
	fetch_analytics_search_ministers,
	fetch_data_explorer_analytics,
	fetch_fc_activity_analytics,
	fetch_fc_activity_timeline,
	fetch_fc_history_imm,
	fetch_judge_outcomes,
	fetch_judge_profile_by_slug,
	fetch_judge_profiles,
	fetch_outcomes_by_year,
)
from .reader_service import (
	build_case_citation_pass,
	build_case_citation_pass_detail,
	build_case_reader_data,
	get_case_metadata_pass as _get_case_metadata_pass_impl,
	_build_metadata_pass_normalized_rows,
	_build_reader_extracted_metadata,
	_build_reader_inferred_tags,
	_citation_pass_chunks,
	_format_reader_html,
	_is_irpa_irpr_reference,
	_is_statute_like_label,
	_legislation_url_for_reference,
	_stored_case_citation_details,
	_stored_statute_reference_details,
)
from .search_service import (
	AI_ROLLOUT,
	EMBEDDING_DIMENSIONS,
	EMBEDDING_MODEL,
	execute_grouped_chunk_search,
	execute_search_cases,
	execute_search_chunks,
	execute_search_chunks_local,
	_apply_case_filters,
	_case_lexical_rank_expr,
	_case_match_source,
	_case_search_document,
	_chunk_lexical_rank_expr,
	_chunk_search_document,
	_effective_search_mode,
	_embed,
	_env_bool,
	_load_ai_rollout_flags,
	_local_embedding_provider,
	_party_filter_terms,
	_validate_search_ranges,
)
from .models import (
	CaseIngestRequest,
	CaseMergeResponse,
	CaseReaderChunkResponse,
	CaseReaderCitationResponse,
	LegislationCaseOccurrenceResponse,
	LegislationSectionCaseResponse,
	LegislationSectionLookupResponse,
	LegislationSectionResponse,
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
	LiveAnalysisResponse,
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

_data_explorer_page_html = data_explorer_page_html

router = APIRouter(tags=["cases"])
PROTOTYPE_SET_NAME = "immigration_334_v1"

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


@router.get("/analytics/outcomes-by-year", response_model=list[dict[str, Any]])
def get_outcomes_by_year(db: Session = Depends(get_db)) -> list[dict[str, Any]]:
	return fetch_outcomes_by_year(db)

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
	return build_case_reader_data(case_id, db)


@router.get("/api/legislation/cases", response_model=list[LegislationCaseOccurrenceResponse])
def get_legislation_cases(
	instrument_key: str,
	pinpoint: str,
	db: Session = Depends(get_db),
) -> list[LegislationCaseOccurrenceResponse]:
	"""Find every case that cites one canonical legislation provision."""
	requested_key = instrument_key.strip().lower()
	requested_pinpoint = re.sub(r"\s+", "", pinpoint).strip(".")
	rows = db.execute(
		select(StatuteReference, Case.id, Case.title, Case.citation)
		.join(Case, Case.id == StatuteReference.source_case_id)
		.where(
			or_(
				StatuteReference.instrument_key == requested_key,
				StatuteReference.normalized_reference.ilike(f"%{requested_pinpoint}%"),
			)
		)
		.order_by(Case.id, StatuteReference.offset_start, StatuteReference.id)
	)
	results: list[LegislationCaseOccurrenceResponse] = []
	for reference, case_id, title, citation in rows:
		parsed = parse_legislation_citation(reference.normalized_reference or reference.reference_text)
		if parsed is None or parsed.instrument_key != requested_key:
			continue
		pinpoints = {part.strip() for part in parsed.pinpoint.split(",")}
		if requested_pinpoint not in pinpoints and parsed.pinpoint != requested_pinpoint:
			continue
		results.append(
			LegislationCaseOccurrenceResponse(
				case_id=case_id,
				title=title,
				citation=citation,
				reference_id=reference.id,
				reference_text=reference.reference_text,
				instrument_key=parsed.instrument_key,
				pinpoint=requested_pinpoint,
				legislation_url=reference.legislation_url or parsed.legislation_url,
				chunk_id=reference.chunk_id,
				offset_start=reference.offset_start,
				offset_end=reference.offset_end,
			)
		)
	return results


@router.get("/api/legislation/section", response_model=LegislationSectionLookupResponse)
def get_legislation_section(
	instrument_key: str,
	pinpoint: str,
	db: Session = Depends(get_db),
) -> LegislationSectionLookupResponse:
	"""Return local authoritative section text and cases citing the pinpoint."""
	requested_key = instrument_key.strip().lower()
	requested_pinpoint = re.sub(r"\s+", "", pinpoint).strip(".")
	section_match = re.match(r"(\d{1,3}(?:\.\d+)?[A-Za-z]?)", requested_pinpoint)
	if section_match is None:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid legislation pinpoint")
	document = db.scalar(select(LegislationDocument).where(LegislationDocument.instrument_key == requested_key))
	if document is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legislation document not indexed")
	section = db.scalar(
		select(LegislationSection).where(
			LegislationSection.document_id == document.id,
			LegislationSection.section_number == section_match.group(1),
		)
	)
	if section is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legislation section not indexed")
	case_rows = db.execute(
		select(StatuteReference, Case.id, Case.title, Case.citation)
		.join(Case, Case.id == StatuteReference.source_case_id)
		.where(
			or_(
				StatuteReference.instrument_key == requested_key,
				StatuteReference.normalized_reference.ilike(f"%{requested_pinpoint}%"),
			)
		)
		.order_by(Case.id, StatuteReference.offset_start, StatuteReference.id)
	)
	cases: list[LegislationSectionCaseResponse] = []
	seen_cases: set[int] = set()
	for reference, case_id, title, citation in case_rows:
		parsed = parse_legislation_citation(reference.normalized_reference or reference.reference_text)
		if parsed is None or parsed.instrument_key != requested_key:
			continue
		if requested_pinpoint not in {part.strip() for part in parsed.pinpoint.split(",")} and parsed.pinpoint != requested_pinpoint:
			continue
		if case_id in seen_cases:
			continue
		seen_cases.add(case_id)
		cases.append(LegislationSectionCaseResponse(case_id=case_id, title=title, citation=citation, pinpoint=requested_pinpoint))
	return LegislationSectionLookupResponse(
		section=LegislationSectionResponse(
			instrument_key=document.instrument_key,
			title=document.title,
			citation=document.citation,
			section_number=section.section_number,
			label=section.label,
			text=section.text,
			source_url=_legislation_url_for_reference(f"{document.title} s. {section.section_number}"),
		),
		cases=cases,
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


@router.get("/live-analysis", response_class=HTMLResponse, include_in_schema=False)
def live_analysis_page() -> HTMLResponse:
	return HTMLResponse(content=live_analysis_page_html(), status_code=status.HTTP_200_OK)


@router.post("/live-analysis/analyze", response_model=LiveAnalysisResponse)
async def live_analysis_analyze(
	file: UploadFile = File(...),
	resolve: bool = Query(False),
	db: Session = Depends(get_db),
) -> LiveAnalysisResponse:
	content = await file.read()
	try:
		payload = analyze_document(content, file.filename or "document.docx", file.content_type, db if resolve else None)
	except ValueError as exc:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
	except Exception as exc:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="The document could not be parsed as DOCX") from exc
	return LiveAnalysisResponse.model_validate(payload)


@router.post("/live-analysis/resolve", response_model=LiveAnalysisResponse)
async def live_analysis_resolve(
	file: UploadFile = File(...),
	db: Session = Depends(get_db),
) -> LiveAnalysisResponse:
	content = await file.read()
	try:
		payload = analyze_document(content, file.filename or "document.docx", file.content_type, db)
	except ValueError as exc:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
	except Exception as exc:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="The document could not be resolved") from exc
	return LiveAnalysisResponse.model_validate(payload)


@router.get("/case-reader", response_class=HTMLResponse, include_in_schema=False)
def case_reader_page(case_id: int | None = None) -> RedirectResponse:
	target = "/data-explorer"
	if case_id is not None:
		target += f"?case_id={case_id}"
	return RedirectResponse(url=target, status_code=status.HTTP_307_TEMPORARY_REDIRECT)


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


@router.get("/judge-outcomes", response_class=HTMLResponse, include_in_schema=False)
def judge_outcomes_page() -> HTMLResponse:
	return HTMLResponse(content=judge_outcomes_page_html(), status_code=status.HTTP_200_OK)


@router.get("/analytics/judge-outcomes", response_model=dict[str, Any])
def get_judge_outcomes(
	limit: int = 50,
	min_decisions: int = 0,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	return fetch_judge_outcomes(db, limit=limit, min_decisions=min_decisions)


@router.get("/data-explorer", response_class=HTMLResponse, include_in_schema=False)
def data_explorer_page() -> HTMLResponse:
	return HTMLResponse(content=data_explorer_page_html(), status_code=status.HTTP_200_OK)


@router.get("/analytics/explorer", response_model=dict[str, Any])
def get_data_explorer(
	group_by: str = "judge",
	split_by: str = "government_outcome",
	limit: int = 50,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	return fetch_data_explorer_analytics(db, group_by=group_by, split_by=split_by, limit=limit)


@router.get("/api/about/stats", response_model=dict[str, int], include_in_schema=False)
def about_stats(db: Session = Depends(get_db)) -> dict[str, int]:
	return fetch_about_stats(db)


@router.get("/api/fc-history", response_model=dict[str, Any], include_in_schema=False)
def fetch_fc_history(imm: str, db: Session = Depends(get_db)) -> dict[str, Any]:
	return fetch_fc_history_imm(db, imm)


@router.get("/api/fc-activity/timeline", response_model=dict[str, Any], include_in_schema=False)
def fc_activity_timeline(city: str = "", db: Session = Depends(get_db)) -> dict[str, Any]:
	"""Return yearly FC activity counts by province and total, optionally focused on a city."""
	return fetch_fc_activity_timeline(db, city=city)


@router.get("/api/fc-activity/analytics", response_model=dict[str, Any], include_in_schema=False)
def fc_activity_analytics(
	x: str = "year",
	group_by: str = "full_history_resolution",
	year_from: int | None = None,
	year_to: int | None = None,
	city: str = "",
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	return fetch_fc_activity_analytics(
		db,
		x=x,
		group_by=group_by,
		year_from=year_from,
		year_to=year_to,
		city=city,
	)


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
	return fetch_judge_profiles(db, q=q, limit=limit)


@router.get("/api/judge-profiles/{slug}", response_model=dict[str, Any], include_in_schema=False)
def judge_profile(
	slug: str,
	minister: list[str] | None = Query(default=None),
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	return fetch_judge_profile_by_slug(db, slug, ministers=minister)


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
	return fetch_analytics_search_cases(
		db,
		query=query,
		cites=cites,
		government_outcome=government_outcome,
		decision_outcome=decision_outcome,
		minister=minister,
		judge=judge,
		court=court,
		year=year,
		search_full_text=search_full_text,
		sort_by=sort_by,
		limit=limit,
		offset=offset,
	)


@router.get("/analytics/search/ministers", response_model=dict[str, list[str]])
def get_analytics_search_ministers(db: Session = Depends(get_db)) -> dict[str, list[str]]:
	return fetch_analytics_search_ministers(db)


@router.get("/analytics/search/cases/{case_id}", response_model=dict[str, Any])
def get_analytics_search_case(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	return fetch_analytics_search_case_detail(db, case_id)


def get_case_metadata_pass(case_id: int, db: Session) -> dict[str, object]:
	return _get_case_metadata_pass_impl(
		case_id,
		db,
		get_case_fn=_get_case_or_404,
		build_extracted_fn=_build_reader_extracted_metadata,
		build_normalized_fn=_build_metadata_pass_normalized_rows,
	)


@router.get("/citation-pass", response_class=HTMLResponse, include_in_schema=False)
def citation_pass_page() -> str:
	return citation_pass_page_html()


@router.get("/cases/{case_id}/citation-pass", response_model=dict[str, Any])
def get_case_citation_pass(case_id: int, db: Session = Depends(get_db)) -> dict[str, Any]:
	return build_case_citation_pass(
		case_id,
		db,
		get_case_fn=_get_case_or_404,
		extract_case_fn=extract_case_citation_matches,
		extract_statute_fn=extract_statute_reference_matches,
		extract_metadata_fn=extract_metadata_observations,
	)


@router.get("/cases/{case_id}/citation-pass/detail", response_model=dict[str, Any])
def get_case_citation_pass_detail(
	case_id: int,
	layer: str,
	offset_start: int,
	offset_end: int,
	db: Session = Depends(get_db),
) -> dict[str, Any]:
	return build_case_citation_pass_detail(
		case_id,
		layer,
		offset_start,
		offset_end,
		db,
		get_case_fn=_get_case_or_404,
		extract_case_fn=extract_case_citation_matches,
		extract_statute_fn=extract_statute_reference_matches,
		stored_case_fn=_stored_case_citation_details,
		stored_statute_fn=_stored_statute_reference_details,
	)


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
	return quick_search_page_html()


@router.get("/quick-search", response_class=HTMLResponse, include_in_schema=False)
def quick_search_interface() -> HTMLResponse:
	return HTMLResponse(content=quick_search_page_html(), status_code=status.HTTP_200_OK)


@router.get("/testing", response_class=HTMLResponse, include_in_schema=False)
def testing_interface() -> HTMLResponse:
	return HTMLResponse(content=testing_page_html(), status_code=status.HTTP_200_OK)


@router.get("/prototype", response_class=HTMLResponse, include_in_schema=False)
def prototype_interface() -> HTMLResponse:
	return HTMLResponse(content=prototype_page_html(), status_code=status.HTTP_200_OK)


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
	return execute_search_cases(search, db, embed_fn=_embed, rollout=AI_ROLLOUT)


@router.post("/search/chunks", response_model=list[ChunkSearchResponse])
def search_chunks(
	search: CaseSearchRequest, db: Session = Depends(get_db)
) -> list[ChunkSearchResponse]:
	return execute_search_chunks(search, db, embed_fn=_embed, rollout=AI_ROLLOUT)


@router.post("/search/chunks/local", response_model=list[ChunkSearchResponse])
def search_chunks_local(
	search: LocalChunkSearchRequest,
	db: Session = Depends(get_db),
) -> list[ChunkSearchResponse]:
	return execute_search_chunks_local(search, db, rollout=AI_ROLLOUT)


def _grouped_chunk_search(
	search: ChunkGroupSearchRequest, db: Session
) -> GroupedChunkSearchResponse:
	"""Inner retrieval shared by /search/chunks/grouped and /research."""
	return execute_grouped_chunk_search(search, db, embed_fn=_embed, rollout=AI_ROLLOUT)


@router.post("/search/chunks/grouped", response_model=GroupedChunkSearchResponse)
def search_chunks_grouped(
	search: ChunkGroupSearchRequest, db: Session = Depends(get_db)
) -> GroupedChunkSearchResponse:
	return _grouped_chunk_search(search, db)


_CONTEXT_CHAR_LIMIT = 12_000
_RESEARCH_DISCLAIMER = (
	"Research aid only � not legal advice. "
	"Sources are unofficial copies; verify against authoritative records."
)


def _research_page_html() -> str:
	return research_page_html()


@router.get("/research", response_class=HTMLResponse, include_in_schema=False)
def research_interface() -> HTMLResponse:
	return HTMLResponse(content=research_page_html(), status_code=status.HTTP_200_OK)


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
