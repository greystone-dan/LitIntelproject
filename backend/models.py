from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CaseIngestRequest(BaseModel):
	title: str = Field(min_length=1, max_length=255)
	court: str = Field(min_length=1, max_length=255)
	jurisdiction: str | None = Field(default=None, max_length=100)
	date: date
	citation: str | None = Field(default=None, max_length=255)
	docket_number: str | None = Field(default=None, max_length=255)
	summary: str | None = Field(default=None, min_length=1)
	full_text: str | None = None
	source_html: str | None = None
	issues: list[str] | None = None
	metadata_json: dict[str, Any] | None = None
	source_url: str | None = Field(default=None, max_length=2048)
	source_name: str | None = Field(default=None, max_length=255)
	secondary_citation: str | None = Field(default=None, max_length=255)
	source_id: str | None = Field(default=None, max_length=255)
	source_type: str | None = Field(default=None, max_length=100)
	dataset_version: str | None = Field(default=None, max_length=100)
	upstream_license: str | None = None
	scraped_at: datetime | None = None
	language: str | None = Field(default=None, max_length=10)
	full_text_hash: str | None = Field(default=None, min_length=64, max_length=64)
	processing_status: Literal["raw", "embedded"] = "raw"
	cases_cited: list[str] | None = None
	cases_citing: list[str] | None = None
	citing_cases_count: int | None = Field(default=None, ge=0)

	@model_validator(mode="after")
	def require_text(self) -> "CaseIngestRequest":
		if not self.summary and not self.full_text:
			raise ValueError("summary or full_text is required")
		return self


class LiveAnalysisReferenceResponse(BaseModel):
	kind: str
	reference_text: str
	normalized_reference: str
	offset_start: int
	offset_end: int
	paragraph_index: int | None = None
	paragraph_text: str | None = None
	page_number: int | None = None
	context: str
	resolved_case_id: int | None = None
	resolved_case_title: str | None = None
	resolved_case_citation: str | None = None
	instrument_key: str | None = None
	pinpoint: str | None = None
	legislation_url: str | None = None
	source_title: str | None = None
	source_text: str | None = None
	source_url: str | None = None


class LiveAnalysisSummaryResponse(BaseModel):
	case_citations: int
	resolved_case_citations: int
	unresolved_case_citations: int
	statute_references: int


class LiveAnalysisResponse(BaseModel):
	filename: str = Field(min_length=1)
	text: str
	text_length: int
	paragraph_count: int
	case_citations: list[LiveAnalysisReferenceResponse]
	statute_references: list[LiveAnalysisReferenceResponse]
	summary: LiveAnalysisSummaryResponse


class CaseSearchRequest(BaseModel):
	query: str = Field(min_length=1)
	search_mode: Literal["semantic", "lexical", "hybrid", "metadata"] = "semantic"
	semantic_weight: float = Field(default=0.7, ge=0.0, le=1.0)
	lexical_weight: float = Field(default=0.3, ge=0.0, le=1.0)
	candidate_pool: int = Field(default=100, ge=10, le=500)
	title_contains: str | None = Field(default=None, max_length=255)
	court: str | None = Field(default=None, max_length=255)
	jurisdiction: str | None = Field(default=None, max_length=100)
	source_name_contains: str | None = Field(default=None, max_length=255)
	source_url_contains: str | None = Field(default=None, max_length=2048)
	source_id_contains: str | None = Field(default=None, max_length=255)
	dataset_version_contains: str | None = Field(default=None, max_length=100)
	upstream_license_contains: str | None = None
	secondary_citation_contains: str | None = Field(default=None, max_length=255)
	party_filters: list[str] | None = None
	cited_case: str | None = Field(default=None, max_length=255)
	citation_contains: str | None = Field(default=None, max_length=255)
	cases_cited_contains: str | None = Field(default=None, max_length=255)
	cases_citing_contains: str | None = Field(default=None, max_length=255)
	date_from: date | None = None
	date_to: date | None = None
	scraped_from: date | None = None
	scraped_to: date | None = None
	source_type: str | None = Field(default=None, max_length=100)
	language: str | None = Field(default=None, max_length=10)
	processing_status: str | None = Field(default=None, max_length=30)
	tag_filters: list[str] | None = Field(default=None, max_length=20)
	citing_cases_min: int | None = Field(default=None, ge=0)
	citing_cases_max: int | None = Field(default=None, ge=0)
	page: int = Field(default=1, ge=1)
	page_size: int = Field(default=15, ge=1, le=50)

	@model_validator(mode="after")
	def validate_hybrid_weights(self) -> "CaseSearchRequest":
		if self.search_mode == "hybrid" and (self.semantic_weight + self.lexical_weight) <= 0:
			raise ValueError("hybrid search requires semantic_weight + lexical_weight > 0")
		for tag_filter in self.tag_filters or []:
			category, separator, value = tag_filter.partition(":")
			if not separator or not category.strip() or not value.strip():
				raise ValueError("tag_filters must use category:value")
		return self


class CaseResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	title: str
	court: str
	jurisdiction: str | None = None
	date: date
	citation: str | None = None
	docket_number: str | None = None
	summary: str | None = None
	full_text: str | None = None
	issues: list[str] | None = None
	metadata_json: dict[str, Any] | None = None
	source_url: str | None = None
	source_name: str | None = None
	secondary_citation: str | None = None
	source_id: str | None = None
	source_type: str | None = None
	dataset_version: str | None = None
	upstream_license: str | None = None
	scraped_at: Any = None
	language: str | None = None
	full_text_hash: str | None = None
	processing_status: str = "raw"
	cases_cited: list[str] | None = None
	cases_citing: list[str] | None = None
	citing_cases_count: int | None = None


class CaseMergeResponse(BaseModel):
	action: Literal["created", "merged"]
	changed_fields: list[str]
	case: CaseResponse


class CaseSourceResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	source_type: str
	source_name: str | None = None
	source_id: str | None = None
	source_url: str | None = None
	dataset_version: str | None = None
	upstream_license: str | None = None
	scraped_at: datetime | None = None
	is_primary: bool
	metadata_json: dict[str, Any] | None = None
	created_at: datetime


class CaseReaderChunkResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	chunk_set: str = "legacy"
	chunk_index: int
	chunk_label: str | None = None
	paragraph_start: int | None = None
	paragraph_end: int | None = None
	text: str
	text_length: int
	token_estimate: int
	created_at: datetime


class CaseReaderCitationResponse(BaseModel):
	id: int
	citation_kind: str = "unknown"
	chunk_id: int | None = None
	offset_start: int | None = None
	offset_end: int | None = None
	citation_text: str | None = None
	normalized_citation: str | None = None
	instrument_key: str | None = None
	pinpoint: str | None = None
	target_case_id: int | None = None
	target_title: str | None = None
	target_citation: str | None = None
	target_paragraph: int | None = None
	target_chunk_text: str | None = None
	legislation_url: str | None = None
	provenance: str = "local"
	unresolved: bool = False
	layer_spans: dict[str, dict[str, int | None]] | None = None


class LegislationCaseOccurrenceResponse(BaseModel):
	case_id: int
	title: str | None = None
	citation: str | None = None
	reference_id: int
	reference_text: str | None = None
	instrument_key: str
	pinpoint: str
	legislation_url: str | None = None
	chunk_id: int | None = None
	offset_start: int | None = None
	offset_end: int | None = None


class LegislationSectionResponse(BaseModel):
	instrument_key: str
	title: str
	citation: str | None = None
	section_number: str
	label: str | None = None
	text: str
	source_url: str | None = None


class LegislationSectionCaseResponse(BaseModel):
	case_id: int
	title: str | None = None
	citation: str | None = None
	pinpoint: str


class LegislationSectionLookupResponse(BaseModel):
	section: LegislationSectionResponse
	cases: list[LegislationSectionCaseResponse]


class CaseReaderTagResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int | None = None
	category: str
	value: str
	score: float
	evidence: str
	offset_start: int | None = None
	offset_end: int | None = None
	source: str
	taxonomy_version: str
	created_at: datetime | None = None


class CaseReaderMetadataFieldResponse(BaseModel):
	key: str
	value: str
	source: str = "reader_extracted"
	evidence: str | None = None


class CaseReaderDataResponse(BaseModel):
	case: CaseResponse
	sources: list[CaseSourceResponse]
	chunks: list[CaseReaderChunkResponse]
	citations: list[CaseReaderCitationResponse]
	tags: list[CaseReaderTagResponse]
	extracted_metadata: list[CaseReaderMetadataFieldResponse] = []
	metrics: "CitationMetricsResponse | None" = None
	formatted_html: str | None = None


class InventoryCaseResponse(BaseModel):
	id: int
	title: str
	court: str
	date: date
	citation: str | None = None
	source_type: str | None = None
	source_name: str | None = None
	source_id: str | None = None
	source_count: int
	sources: list[CaseSourceResponse]


class InventorySourceSummary(BaseModel):
	source_type: str
	case_count: int


class InventoryResponse(BaseModel):
	total_cases: int
	total_sources: int
	source_breakdown: list[InventorySourceSummary]
	cases: list[InventoryCaseResponse]


class CaseSearchResponse(CaseResponse):
	similarity: float
	match_source: str | None = None


class ChunkSearchResponse(CaseResponse):
	chunk_index: int
	chunk_text: str
	similarity: float


class LocalChunkSearchRequest(CaseSearchRequest):
	model_config = ConfigDict(protected_namespaces=())

	model_name: str = Field(default="BAAI/bge-m3", min_length=1, max_length=255)


class ChunkGroupSearchRequest(CaseSearchRequest):
	max_chunks_per_case: int = Field(default=2, ge=1, le=10)


class ChunkPassage(BaseModel):
	chunk_index: int
	chunk_text: str
	similarity: float


class GroupedChunkCaseResponse(CaseResponse):
	best_similarity: float
	chunks: list[ChunkPassage]


class GroupedChunkSearchResponse(BaseModel):
	result_type: Literal["grouped_by_case"] = "grouped_by_case"
	total_cases: int
	total_chunks: int
	max_chunks_per_case: int
	cases: list[GroupedChunkCaseResponse]


class CitationResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	source_case_id: int
	target_case_id: int | None = None
	citation_kind: str = "unknown"
	citation_text: str | None = None
	normalized_citation: str | None = None
	provenance: str = "local"
	chunk_id: int | None = None
	offset_start: int | None = None
	offset_end: int | None = None
	unresolved: bool = False


class CitationMetricsResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	case_id: int
	in_degree: int | None = None
	out_degree: int | None = None
	pagerank: float | None = None


class CitationMapSummaryResponse(BaseModel):
	total_cases: int
	resolved_occurrences: int
	unresolved_occurrences: int
	aggregated_edges: int
	connected_cases: int
	metrics_cases: int


class CitationMapCaseNode(BaseModel):
	case_id: int
	title: str
	citation: str | None = None
	court: str
	date: date
	in_degree: int = 0
	out_degree: int = 0
	pagerank: float | None = None


class CitationMapAuthorityResponse(CitationMapCaseNode):
	citing_cases: int
	citation_occurrences: int


class CitationMapEdgeResponse(BaseModel):
	source_case_id: int
	target_case_id: int
	occurrence_count: int


class CitationMapNeighborhoodResponse(BaseModel):
	focus: CitationMapCaseNode
	nodes: list[CitationMapCaseNode]
	edges: list[CitationMapEdgeResponse]


class CitationMapSharedAuthority(BaseModel):
	case_id: int
	title: str
	citation: str | None = None
	citing_cases: int


class CitationMapSimilarCaseResponse(BaseModel):
	case: CitationMapCaseNode
	shared_authority_count: int
	rarity_weighted_score: float
	shared_authorities: list[CitationMapSharedAuthority]


class CitationMapCoCitationResponse(BaseModel):
	authority: CitationMapCaseNode
	shared_citing_cases: int
	citation_occurrences: int


class CitationMapCommonCiterResponse(BaseModel):
	case: CitationMapCaseNode
	matched_authority_count: int
	citation_occurrences: int


class CitationMapPathResponse(BaseModel):
	path_case_ids: list[int]
	hop_count: int
	total_occurrences: int
	nodes: list[CitationMapCaseNode]
	edge_occurrences: list[int]


class CitationMapPathHopResponse(BaseModel):
	source_case_id: int
	target_case_id: int
	occurrence_count: int
	contexts: list["CitationMapContextResponse"]


class CitationMapContextualPathResponse(CitationMapPathResponse):
	hops: list[CitationMapPathHopResponse]


class CitationMapContextResponse(BaseModel):
	citation_id: int
	source_case_id: int
	source_title: str
	source_citation: str | None = None
	target_case_id: int
	target_title: str
	target_citation: str | None = None
	chunk_id: int
	chunk_index: int
	citation_text: str | None = None
	normalized_citation: str | None = None
	offset_start: int
	offset_end: int
	context_start: int
	context_end: int
	context: str


class CitationMapEdgeVariantResponse(BaseModel):
	normalized_citation: str | None = None
	occurrences: int


class CitationMapEdgeSummaryResponse(BaseModel):
	source_case: CitationMapCaseNode
	target_case: CitationMapCaseNode
	occurrence_count: int
	distinct_chunks: int
	first_chunk_index: int | None = None
	last_chunk_index: int | None = None
	top_normalized_citations: list[CitationMapEdgeVariantResponse]
	sample_contexts: list[CitationMapContextResponse]


class CitationMapAuthoritySignalResponse(BaseModel):
	authority: CitationMapCaseNode
	occurrence_count: int
	distinct_chunks: int
	gravity_share: float
	global_citing_cases: int
	surprise_score: float
	originality_score: float
	boilerplate_hits: int
	first_chunk_index: int | None = None
	last_chunk_index: int | None = None
	sample_contexts: list[CitationMapContextResponse]


class CitationMapReplacementYearResponse(BaseModel):
	year: int
	old_citing_cases: int
	new_citing_cases: int
	new_share: float


class CitationMapReplacementResponse(BaseModel):
	old_authority: CitationMapCaseNode
	new_authority: CitationMapCaseNode
	replacement_score: float
	status: str
	series: list[CitationMapReplacementYearResponse]


class CitationMapLandmarkWindow(BaseModel):
	start_year: int
	end_year: int


class CitationMapLandmarkCandidateResponse(BaseModel):
	case: CitationMapCaseNode
	recent_citing_cases: int
	baseline_citing_cases: int
	emergence_score: float
	lift_ratio: float
	recent_window: CitationMapLandmarkWindow
	baseline_window: CitationMapLandmarkWindow


class CitationMapSurpriseResponse(BaseModel):
	source_case: CitationMapCaseNode
	authority: CitationMapCaseNode
	occurrence_count: int
	global_citing_cases: int
	gravity_share: float
	surprise_score: float


class CitationMapHiddenBridgeResponse(BaseModel):
	bridge_case: CitationMapCaseNode
	path_count: int
	weighted_support: float
	average_relative_position: float
	average_path_hops: float


class CitationMapInheritanceChainResponse(BaseModel):
	chain_case_ids: list[int]
	depth: int
	total_occurrences: int
	nodes: list[CitationMapCaseNode]
	edge_occurrences: list[int]


class CitationMapMissingAuthorityResponse(BaseModel):
	authority: CitationMapCaseNode
	peer_citing_cases: int
	peer_coverage: float
	peer_occurrences: int
	rarity_boost: float
	priority_score: float


class CitationMapAuthorityLifecycleResponse(BaseModel):
	authority: CitationMapCaseNode
	recent_citing_cases: int
	prior_citing_cases: int
	total_citing_cases: int
	velocity: float
	decay: float
	lifecycle_stage: str


class CitationMapCourtFlowResponse(BaseModel):
	source_court: str
	target_court: str
	citing_case_count: int
	citation_occurrences: int


class CitationMapPositionProfileResponse(BaseModel):
	authority: CitationMapCaseNode
	occurrence_count: int
	avg_chunk_index: float
	first_chunk_index: int | None = None
	last_chunk_index: int | None = None
	first_half_hits: int
	second_half_hits: int


class CitationMapCompletionSuggestionResponse(BaseModel):
	authority: CitationMapCaseNode
	peer_citing_cases: int
	peer_coverage: float
	rarity_boost: float
	expected_occurrences: int
	recommendation_score: float


class CitationMapShiftDashboardResponse(BaseModel):
	category: str
	value: str
	replacement_candidates: list[CitationMapReplacementResponse]
	emerging_authorities: list[CitationMapAuthorityLifecycleResponse]
	declining_authorities: list[CitationMapAuthorityLifecycleResponse]
	surprises: list[CitationMapSurpriseResponse]


class CitationMapLegalTagResponse(BaseModel):
	category: str
	value: str
	score: float
	evidence: str
	source: str
	taxonomy_version: str


class CitationMapTopicResponse(BaseModel):
	category: str
	value: str
	case_count: int


class CitationIssueMapResponse(BaseModel):
	category: str
	value: str
	available_cases: int
	nodes: list[CitationMapCaseNode]
	edges: list[CitationMapEdgeResponse]


class A2AJCaseResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	a2aj_case_id: str
	neutral_citation: str | None = None
	court: str | None = None
	decision_date: date | None = None
	cases_cited: list[str] | None = None
	cases_citing: list[str] | None = None
	citing_cases_count: int | None = None


class A2AJCitationEdgeResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	source_a2aj_case_id: str
	target_a2aj_case_id: str | None = None
	normalized_citation: str | None = None


class A2AJCaseMapResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	a2aj_case_id: str
	local_case_id: int


class ResearchRequest(ChunkGroupSearchRequest):
	max_cases: int = Field(default=5, ge=1, le=10)
	temperature: float = Field(default=0.3, ge=0.0, le=1.0)
	# override ChunkGroupSearchRequest defaults for richer context
	max_chunks_per_case: int = Field(default=3, ge=1, le=10)
	page_size: int = Field(default=20, ge=1, le=50)


class ResearchSource(BaseModel):
	case_id: int
	title: str
	citation: str | None
	court: str | None
	date: date | None
	source_url: str | None
	excerpts: list[str]


class ResearchResponse(BaseModel):
	model_config = ConfigDict(protected_namespaces=())

	question: str
	answer: str
	sources: list[ResearchSource]
	model_used: str
	prompt_tokens: int
	completion_tokens: int
