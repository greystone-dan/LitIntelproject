# Generated API Reference

This file is generated from `backend.main:app.openapi()` by `scripts/generate_api_reference.py`. Do not edit it manually.

Generated: 2026-09-04T00:57:32.282168+00:00
OpenAPI title: FastAPI
OpenAPI version: 0.1.0
OpenAPI operations: 80 across 80 paths
Hidden operations: 35 excluded from OpenAPI

The live OpenAPI UI is available at `/docs`. This appendix records the route contract present when it was generated. Request/response component definitions remain available in the live schema. Routes deliberately hidden from OpenAPI are appended with their handler signature.

## Operations

### `GET /`

Root

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`

### `GET /a2aj/cases/{a2aj_case_id}`

Get A2Aj Case

**Parameters**

- `a2aj_case_id` (path, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `A2AJCaseResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /a2aj/cases/{a2aj_case_id}/edges`

Get A2Aj Case Edges

**Parameters**

- `a2aj_case_id` (path, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /a2aj/cases/{a2aj_case_id}/map`

Get A2Aj Case Map

**Parameters**

- `a2aj_case_id` (path, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `A2AJCaseMapResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /a2aj/citation-network/build-map`

Build A2Aj Case Map Endpoint

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `POST /a2aj/citation-network/convert`

Convert A2Aj Edges Endpoint

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /analytics/explorer`

Get Data Explorer

**Parameters**

- `group_by` (query, optional; string, default `"judge"`)
- `split_by` (query, optional; string, default `"government_outcome"`)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/judge-outcomes`

Get Judge Outcomes

**Parameters**

- `limit` (query, optional; integer, default `50`)
- `min_decisions` (query, optional; integer, default `0`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/outcomes-by-year`

Get Outcomes By Year

**Responses**

- `200`: Successful Response; `application/json`: `array`

### `GET /analytics/search/cases`

Search Analytics Cases

**Parameters**

- `query` (query, optional; string, default `""`)
- `cites` (query, optional; string, default `""`)
- `government_outcome` (query, optional; string, default `""`)
- `decision_outcome` (query, optional; string, default `""`)
- `minister` (query, optional; string, default `""`)
- `judge` (query, optional; string, default `""`)
- `court` (query, optional; string, default `""`)
- `year` (query, optional; string, default `""`)
- `search_full_text` (query, optional; boolean, default `false`)
- `sort_by` (query, optional; string, default `"relevance"`)
- `limit` (query, optional; integer, default `50`)
- `offset` (query, optional; integer, default `0`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/cases/{case_id}`

Get Analytics Search Case

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/ministers`

Get Analytics Search Ministers

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /api/legislation/cases`

Get Legislation Cases

Find every case that cites one canonical legislation provision.

**Parameters**

- `instrument_key` (query, required; string)
- `pinpoint` (query, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/legislation/section`

Get Legislation Section

Return local authoritative section text and cases citing the pinpoint.

**Parameters**

- `instrument_key` (query, required; string)
- `pinpoint` (query, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `LegislationSectionLookupResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}`

Get Case

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `CaseResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citation-metrics`

Get Case Citation Metrics

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMetricsResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citation-pass`

Get Case Citation Pass

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citation-pass/detail`

Get Case Citation Pass Detail

**Parameters**

- `case_id` (path, required; integer)
- `layer` (query, required; string)
- `offset_start` (query, required; integer)
- `offset_end` (query, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citations/incoming`

Get Case Incoming Citations

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citations/outgoing`

Get Case Outgoing Citations

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/citations/passages`

Get Case Citation Passages

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/reader-data`

Get Case Reader Data

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `CaseReaderDataResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map`

Citation Map Page

**Responses**

- `200`: Successful Response; `text/html`: `string`

### `GET /citation-map/authorities`

Get Citation Map Authorities

**Parameters**

- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/landmarks`

Get Citation Landmark Candidates

**Parameters**

- `limit` (query, optional; integer, default `20`)
- `recent_years` (query, optional; integer, default `3`)
- `baseline_years` (query, optional; integer, default `5`)
- `min_recent` (query, optional; integer, default `20`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/landmarks.csv`

Export Citation Landmark Candidates

**Parameters**

- `limit` (query, optional; integer, default `20`)
- `recent_years` (query, optional; integer, default `3`)
- `baseline_years` (query, optional; integer, default `5`)
- `min_recent` (query, optional; integer, default `20`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/lifecycle`

Get Citation Authority Lifecycle

**Parameters**

- `category` (query, optional; string | null)
- `value` (query, optional; string | null)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `25`)
- `recent_years` (query, optional; integer, default `3`)
- `prior_years` (query, optional; integer, default `3`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/lifecycle.csv`

Export Citation Authority Lifecycle

**Parameters**

- `category` (query, optional; string | null)
- `value` (query, optional; string | null)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `25`)
- `recent_years` (query, optional; integer, default `3`)
- `prior_years` (query, optional; integer, default `3`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/replacement`

Get Citation Replacement Trend

**Parameters**

- `old_case_id` (query, required; integer)
- `new_case_id` (query, required; integer)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapReplacementResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/{case_id}/co-cited`

Get Citation Map Co Cited Authorities

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `30`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/{case_id}/inheritance`

Get Citation Inheritance Chains

**Parameters**

- `case_id` (path, required; integer)
- `max_depth` (query, optional; integer, default `3`)
- `limit` (query, optional; integer, default `20`)
- `per_node_limit` (query, optional; integer, default `20`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/authorities/{case_id}/inheritance.csv`

Export Citation Inheritance Chains

**Parameters**

- `case_id` (path, required; integer)
- `max_depth` (query, optional; integer, default `3`)
- `limit` (query, optional; integer, default `20`)
- `per_node_limit` (query, optional; integer, default `20`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases`

Search Citation Map Cases

**Parameters**

- `q` (query, required; string)
- `limit` (query, optional; integer, default `12`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/review/fc-priority`

Review Fc Priority Cases

**Parameters**

- `limit` (query, optional; integer, default `300`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/authority-map`

Get Case Authority Map

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `5`)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapNeighborhoodResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/authority-signals`

Get Citation Authority Signals

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `20`)
- `context_limit` (query, optional; integer, default `3`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/authority-signals.csv`

Export Citation Authority Signals

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `20`)
- `context_limit` (query, optional; integer, default `3`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/completion-suggestions`

Get Citation Completion Suggestions

**Parameters**

- `case_id` (path, required; integer)
- `peer_limit` (query, optional; integer, default `40`)
- `limit` (query, optional; integer, default `20`)
- `min_peer_share` (query, optional; number, default `0.2`)
- `min_peer_citations` (query, optional; integer, default `2`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/completion-suggestions.csv`

Export Citation Completion Suggestions

**Parameters**

- `case_id` (path, required; integer)
- `peer_limit` (query, optional; integer, default `40`)
- `limit` (query, optional; integer, default `20`)
- `min_peer_share` (query, optional; number, default `0.2`)
- `min_peer_citations` (query, optional; integer, default `2`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/missing-authorities`

Get Citation Missing Authorities

**Parameters**

- `case_id` (path, required; integer)
- `peer_limit` (query, optional; integer, default `40`)
- `limit` (query, optional; integer, default `20`)
- `min_peer_share` (query, optional; number, default `0.2`)
- `min_peer_citations` (query, optional; integer, default `2`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/missing-authorities.csv`

Export Citation Missing Authorities

**Parameters**

- `case_id` (path, required; integer)
- `peer_limit` (query, optional; integer, default `40`)
- `limit` (query, optional; integer, default `20`)
- `min_peer_share` (query, optional; number, default `0.2`)
- `min_peer_citations` (query, optional; integer, default `2`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/neighborhood`

Get Citation Map Neighborhood

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `100`)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapNeighborhoodResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/position-profiles`

Get Citation Position Profiles

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `30`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/position-profiles.csv`

Export Citation Position Profiles

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `30`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/similar`

Get Citation Map Similar Cases

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `20`)
- `min_shared` (query, optional; integer, default `2`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{case_id}/tags`

Get Citation Map Case Tags

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `100`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts`

Get Citation Contexts

**Parameters**

- `source_case_id` (path, required; integer)
- `target_case_id` (path, required; integer)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts.csv`

Export Citation Contexts

**Parameters**

- `source_case_id` (path, required; integer)
- `target_case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/cases/{source_case_id}/citations/{target_case_id}/summary`

Get Citation Edge Summary

**Parameters**

- `source_case_id` (path, required; integer)
- `target_case_id` (path, required; integer)
- `context_limit` (query, optional; integer, default `3`)
- `variant_limit` (query, optional; integer, default `5`)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapEdgeSummaryResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/common-citers`

Get Common Citing Cases

**Parameters**

- `case_ids` (query, required; string)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/courts/flow`

Get Citation Cross Court Flow

**Parameters**

- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `40`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/courts/flow.csv`

Export Citation Cross Court Flow

**Parameters**

- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `40`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/issues/dashboard`

Get Citation Shift Dashboard

**Parameters**

- `category` (query, required; string)
- `value` (query, required; string)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `replacement_limit` (query, optional; integer, default `8`)
- `lifecycle_limit` (query, optional; integer, default `40`)
- `surprise_limit` (query, optional; integer, default `25`)

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapShiftDashboardResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/issues/dashboard.csv`

Export Citation Shift Dashboard

**Parameters**

- `category` (query, required; string)
- `value` (query, required; string)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `replacement_limit` (query, optional; integer, default `8`)
- `lifecycle_limit` (query, optional; integer, default `40`)
- `surprise_limit` (query, optional; integer, default `25`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/issues/graph`

Get Citation Issue Map

**Parameters**

- `category` (query, required; string)
- `value` (query, required; string)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `CitationIssueMapResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/issues/shifts`

Get Citation Doctrine Shifts

**Parameters**

- `category` (query, required; string)
- `value` (query, required; string)
- `limit` (query, optional; integer, default `10`)
- `candidate_limit` (query, optional; integer, default `12`)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/issues/shifts.csv`

Export Citation Doctrine Shifts

**Parameters**

- `category` (query, required; string)
- `value` (query, required; string)
- `limit` (query, optional; integer, default `10`)
- `candidate_limit` (query, optional; integer, default `12`)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/paths`

Get Citation Paths

**Parameters**

- `source_case_id` (query, required; integer)
- `target_case_id` (query, required; integer)
- `max_hops` (query, optional; integer, default `3`)
- `limit` (query, optional; integer, default `5`)
- `per_node_limit` (query, optional; integer, default `40`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/paths/contextual`

Get Contextual Citation Paths

**Parameters**

- `source_case_id` (query, required; integer)
- `target_case_id` (query, required; integer)
- `max_hops` (query, optional; integer, default `3`)
- `limit` (query, optional; integer, default `5`)
- `per_node_limit` (query, optional; integer, default `40`)
- `hop_context_limit` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/paths/hidden`

Get Hidden Citation Bridges

**Parameters**

- `source_case_id` (query, required; integer)
- `target_case_id` (query, required; integer)
- `max_hops` (query, optional; integer, default `4`)
- `path_limit` (query, optional; integer, default `20`)
- `per_node_limit` (query, optional; integer, default `60`)
- `limit` (query, optional; integer, default `15`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/paths/hidden.csv`

Export Hidden Citation Bridges

**Parameters**

- `source_case_id` (query, required; integer)
- `target_case_id` (query, required; integer)
- `max_hops` (query, optional; integer, default `4`)
- `path_limit` (query, optional; integer, default `20`)
- `per_node_limit` (query, optional; integer, default `60`)
- `limit` (query, optional; integer, default `15`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/summary`

Get Citation Map Summary

**Responses**

- `200`: Successful Response; `application/json`: `CitationMapSummaryResponse`

### `GET /citation-map/surprises`

Get Citation Surprises

**Parameters**

- `category` (query, optional; string | null)
- `value` (query, optional; string | null)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `50`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/surprises.csv`

Export Citation Surprises

**Parameters**

- `category` (query, optional; string | null)
- `value` (query, optional; string | null)
- `start_year` (query, optional; integer | null)
- `end_year` (query, optional; integer | null)
- `limit` (query, optional; integer, default `50`)
- `min_occurrences` (query, optional; integer, default `1`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /citation-map/topics`

Get Citation Map Topics

**Parameters**

- `q` (query, optional; string, default `""`)
- `limit` (query, optional; integer, default `100`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /citation-metrics/recompute`

Recompute Citation Metrics

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /health`

Health

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`

### `POST /ingest`

Ingest Case

**Request body (required)**

- `application/json`: `CaseIngestRequest`

**Responses**

- `201`: Successful Response; `application/json`: `CaseResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /ingest/merge`

Merge Ingest Case

**Request body (required)**

- `application/json`: `CaseIngestRequest`

**Responses**

- `200`: Successful Response; `application/json`: `CaseMergeResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /inventory`

Get Inventory

**Responses**

- `200`: Successful Response; `application/json`: `InventoryResponse`

### `POST /live-analysis/analyze`

Live Analysis Analyze

**Parameters**

- `resolve` (query, optional; boolean, default `false`)

**Request body (required)**

- `multipart/form-data`: `Body_live_analysis_analyze_live_analysis_analyze_post`

**Responses**

- `200`: Successful Response; `application/json`: `LiveAnalysisResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/resolve`

Live Analysis Resolve

**Request body (required)**

- `multipart/form-data`: `Body_live_analysis_resolve_live_analysis_resolve_post`

**Responses**

- `200`: Successful Response; `application/json`: `LiveAnalysisResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /prototype/cases`

Prototype Cases

**Parameters**

- `q` (query, optional; string | null)
- `topic` (query, optional; string | null)
- `page` (query, optional; integer, default `1`)
- `page_size` (query, optional; integer, default `20`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /prototype/graph`

Prototype Graph

**Parameters**

- `max_nodes` (query, optional; integer, default `160`)
- `topic` (query, optional; string | null)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /prototype/summary`

Prototype Summary

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `POST /research`

Research

**Request body (required)**

- `application/json`: `ResearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `ResearchResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /search`

Search Cases

**Request body (required)**

- `application/json`: `CaseSearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /search/chunks`

Search Chunks

**Request body (required)**

- `application/json`: `CaseSearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /search/chunks/grouped`

Search Chunks Grouped

**Request body (required)**

- `application/json`: `ChunkGroupSearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `GroupedChunkSearchResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /search/chunks/local`

Search Chunks Local

**Request body (required)**

- `application/json`: `LocalChunkSearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

## Hidden Operations

### `GET /about`

**Hidden from OpenAPI.**

Handler: `backend.routes.about_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /access`

**Hidden from OpenAPI.**

Handler: `backend.main.access_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /access/login`

**Hidden from OpenAPI.**

Handler: `backend.main.access_login`

**Handler parameters**

- `request` (Request; required)
- `password` (str; default `Form(PydanticUndefined)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/about/stats`

**Hidden from OpenAPI.**

Handler: `backend.routes.about_stats`

**Handler parameters**

- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/cases`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_cases`

**Handler parameters**

- `title` (str; default `''`)
- `limit` (int; default `12`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/search`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_search`

**Handler parameters**

- `q` (str; default `''`)
- `limit` (int; default `12`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/companions`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_companions`

**Handler parameters**

- `case_id` (int; required)
- `limit` (int; default `20`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/courts`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_courts`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/judges`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_judges`

**Handler parameters**

- `case_id` (int; required)
- `limit` (int; default `30`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/outcomes`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_outcomes`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/overview`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_overview`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/statutes`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_statutes`

**Handler parameters**

- `case_id` (int; required)
- `limit` (int; default `25`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/table`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_table`

**Handler parameters**

- `case_id` (int; required)
- `page` (int; default `1`)
- `page_size` (int; default `50`)
- `year` (int | None; default `None`)
- `court` (str | None; default `None`)
- `judge` (str | None; default `None`)
- `gov_outcome` (str | None; default `None`)
- `min_mentions` (int; default `1`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/citation-intelligence/{case_id}/timeline`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_timeline`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/analytics`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_analytics`

**Handler parameters**

- `x` (str; default `'year'`)
- `group_by` (str; default `'full_history_resolution'`)
- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
- `city` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/timeline`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_timeline`

**Handler parameters**

- `city` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-history`

**Hidden from OpenAPI.**

Handler: `backend.routes.fetch_fc_history`

**Handler parameters**

- `imm` (str; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/judge-profiles`

**Hidden from OpenAPI.**

Handler: `backend.routes.judge_profiles`

**Handler parameters**

- `q` (str; default `''`)
- `limit` (int; default `50`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/judge-profiles/{slug}`

**Hidden from OpenAPI.**

Handler: `backend.routes.judge_profile`

**Handler parameters**

- `slug` (str; required)
- `minister` (list[str] | None; default `Query(None)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /case-reader`

**Hidden from OpenAPI.**

Handler: `backend.routes.case_reader_page`

**Handler parameters**

- `case_id` (int | None; default `None`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /case-reader/cases`

**Hidden from OpenAPI.**

Handler: `backend.routes.case_reader_cases`

**Handler parameters**

- `limit` (int; default `300`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /cases/{case_id}/activity`

**Hidden from OpenAPI.**

Handler: `backend.routes.get_case_activity`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /citation-intelligence`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_intelligence_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /citation-pass`

**Hidden from OpenAPI.**

Handler: `backend.routes.citation_pass_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /data-explorer`

**Hidden from OpenAPI.**

Handler: `backend.routes.data_explorer_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /fc-history`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_history_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /judge-outcomes`

**Hidden from OpenAPI.**

Handler: `backend.routes.judge_outcomes_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /judges`

**Hidden from OpenAPI.**

Handler: `backend.routes.judges_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /judges/{slug}`

**Hidden from OpenAPI.**

Handler: `backend.routes.judge_profile_page`

**Handler parameters**

- `slug` (str; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /live-analysis`

**Hidden from OpenAPI.**

Handler: `backend.routes.live_analysis_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /prototype`

**Hidden from OpenAPI.**

Handler: `backend.routes.prototype_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /quick-search`

**Hidden from OpenAPI.**

Handler: `backend.routes.quick_search_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /research`

**Hidden from OpenAPI.**

Handler: `backend.routes.research_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /robots.txt`

**Hidden from OpenAPI.**

Handler: `backend.main.robots`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /testing`

**Hidden from OpenAPI.**

Handler: `backend.routes.testing_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.
