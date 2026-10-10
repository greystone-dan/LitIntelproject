# Generated API Reference

This file is generated from `backend.main:app.openapi()` by `scripts/generate_api_reference.py`. Do not edit it manually.

Generated: 2026-10-10T21:02:29.693260+00:00
OpenAPI title: FastAPI
OpenAPI version: 0.1.0
OpenAPI operations: 136 across 133 paths
Hidden operations: 100 excluded from OpenAPI

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

### `GET /analytics/cases/{case_id}/thematic-cluster`

Get Case Thematic Cluster

**Parameters**

- `case_id` (path, required; integer)
- `limit` (query, optional; integer, default `10`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/explorer`

Get Data Explorer

**Parameters**

- `group_by` (query, optional; string, default `"judge"`)
- `split_by` (query, optional; string, default `"government_outcome"`)
- `limit` (query, optional; integer, default `50`)

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
- `cites_case_id` (query, optional; integer | null)
- `tags` (query, optional; string, default `""`)
- `case_type` (query, optional; string, default `""`)
- `search_full_text` (query, optional; boolean, default `false`)
- `sort_by` (query, optional; string, default `"relevance"`)
- `limit` (query, optional; integer, default `50`)
- `offset` (query, optional; integer, default `0`)
- `cohort_id` (query, optional; string, default `""`)
- `facets` (query, optional; boolean, default `true`)
- `citation_stats` (query, optional; boolean, default `true`)

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

### `GET /analytics/search/citation-stats`

Search Analytics Citation Stats

Citation counts for the result cards on screen, loaded after the results so they never delay them.

**Parameters**

- `ids` (query, optional; string, default `""`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/cohort-assessments`

Search Cohort Assessment Records

**Parameters**

- `query` (query, optional; string, default `""`)
- `cohort_id` (query, optional; string, default `"discussion_units_core_300"`)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/cohort-assessments/compare`

Compare Cohort Assessment Records

**Parameters**

- `query` (query, optional; string, default `""`)
- `topic` (query, optional; string, default `""`)
- `role` (query, optional; string, default `""`)
- `limit` (query, optional; integer, default `25`)
- `cohort_id` (query, optional; string, default `"discussion_units_core_300"`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/facets`

Search Analytics Facets

Court, year and case-type counts for the current filters, loaded after the results so they never delay them.

**Parameters**

- `query` (query, optional; string, default `""`)
- `cites` (query, optional; string, default `""`)
- `government_outcome` (query, optional; string, default `""`)
- `decision_outcome` (query, optional; string, default `""`)
- `minister` (query, optional; string, default `""`)
- `judge` (query, optional; string, default `""`)
- `court` (query, optional; string, default `""`)
- `year` (query, optional; string, default `""`)
- `cites_case_id` (query, optional; integer | null)
- `tags` (query, optional; string, default `""`)
- `case_type` (query, optional; string, default `""`)
- `search_full_text` (query, optional; boolean, default `false`)
- `cohort_id` (query, optional; string, default `""`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/search/ministers`

Get Analytics Search Ministers

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /analytics/search/tags`

Search Analytics Tags

Stored tag values matching the typed text, with how many decisions carry each (for the Tag filter).

**Parameters**

- `q` (query, optional; string, default `""`)
- `limit` (query, optional; integer, default `12`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/statute-tag-matrix`

Get Statute Tag Matrix

**Parameters**

- `pinpoint` (query, required; string)
- `limit_tags` (query, optional; integer, default `20`)
- `limit_citations` (query, optional; integer, default `15`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /analytics/tags`

Get Tag Analytics

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /analytics/themes`

Get Analytics Themes

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /api/ai-mode`

Get Ai Mode

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /api/cases/{case_id}/summary`

Get Case Summary

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `StoredCaseSummaryResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/cases/{case_id}/summary-card`

Get Case Summary Card

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `CaseSummaryCardResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/citation-treatment/{case_id}`

Get Citation Treatment

Experimental read-only paragraph evidence, not permanent authority labels.

Counts use distinct citing decisions including unknown as their denominator.
Classes overlap for mixed evidence; unknown means no classifiable evidence.
No UI, citation metrics, stored data or source offsets are changed.

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/compare`

Compare Cases By Id Or Citation

**Parameters**

- `a` (query, required; string): Case ID or stored citation (maximum 512 characters).
- `b` (query, required; string): Case ID or stored citation (maximum 512 characters).

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/judge-profiles/{slug}/issues`

Judge Profile Issues

**Parameters**

- `slug` (path, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `404`: Unknown canonical judge slug (detail.code: unknown_judge)
- `422`: Validation Error; `application/json`: `HTTPValidationError`

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

### `GET /api/overruling-risk/{case_id}`

Get Overruling Risk

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/search-embedding-status`

Search Embedding Status

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /api/statute-library/acts`

Statute Library Acts

**Responses**

- `200`: Successful Response; `application/json`: `array`

### `GET /api/statute-library/{act}/sections`

Statute Library Toc

**Parameters**

- `act` (path, required; string)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/statute-library/{act}/sections/{section}`

Statute Library Section

**Parameters**

- `act` (path, required; string)
- `section` (path, required; string)
- `page` (query, optional; integer, default `1`)
- `page_size` (query, optional; integer, default `25`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/statutes/{act}/{section}/consideration`

Statute Consideration Analytics

Return descriptive, distinct-decision statistics for stored section references.

**Parameters**

- `act` (path, required; string)
- `section` (path, required; string)
- `page` (query, optional; integer, default `1`)
- `page_size` (query, optional; integer, default `25`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/statutes/{statute_code}`

Get Statute By Code

Get statute details, optionally as of a specific date.

**Parameters**

- `statute_code` (path, required; string)
- `as_of` (query, optional; string | null)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/statutes/{statute_code}/versions/{version_id}/sections`

Get Statute Sections

Get sections for a specific statute version.

**Parameters**

- `statute_code` (path, required; string)
- `version_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /api/version`

Api Version

Return safe application version information.

The response contains only a sanitized commit, process start time, and
interpreter version.

**Responses**

- `200`: Successful Response; `application/json`: `object`

### `GET /cases/compare`

Compare two decisions using distinct stored research signals

Returns side-by-side case facts and stored outcome assignment provenance, preserving unclassified outcomes and raw labels. Active legal tags, statute references and case authorities have distinct shared/unique counts; repeated mentions count once. Read-only; no classification or resolution is performed. Unknown IDs return 404 with detail.code=unknown_case and unknown_ids.

**Parameters**

- `a` (query, required; integer)
- `b` (query, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `404`: Unknown canonical case ID(s).
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

### `GET /cases/{case_id}/contextual-anchors`

Get Case Contextual Anchors

**Parameters**

- `case_id` (path, required; integer)
- `proximity_window` (query, optional; integer, default `250`)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/evidence-summary`

Get Case Evidence Summary

Discussion-unit evidence and case summary, loaded after the decision text so they never delay it.

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /cases/{case_id}/markup-export`

Export Case Markup Docx

Word file of the decision with the margin notes the browser sends as Word comments. Nothing is stored.

**Parameters**

- `case_id` (path, required; integer)

**Request body (required)**

- `application/json`: `MarkupExportRequest`

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/paragraph-assessments`

Get Case Paragraph Assessments

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/paragraph-positions`

Get Case Paragraph Positions

Whose-position tags and one-line summaries for a decision (preview). Stored data only; no model call.

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/paragraph-text`

Get Case Paragraph Text

Stored text of numbered paragraphs of one case; the reader's citation hover asks for what it was not sent.

**Parameters**

- `case_id` (path, required; integer)
- `paragraphs` (query, required; string): Comma-separated paragraph numbers, e.g. 45,46,47

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/paragraphs/{n}/similar`

Get Similar Paragraphs

**Parameters**

- `case_id` (path, required; integer)
- `n` (path, required; integer)
- `limit` (query, optional; integer, default `10`)

**Responses**

- `200`: Successful Response; `application/json`: `ParagraphSimilarityResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/reader-data`

Get Case Reader Data

**Parameters**

- `case_id` (path, required; integer)
- `evidence` (query, optional; boolean, default `true`)

**Responses**

- `200`: Successful Response; `application/json`: `CaseReaderDataResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/statute-references`

Get Case Statute References

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /cases/{case_id}/thematic-signature`

Get Case Thematic Signature

**Parameters**

- `case_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `object`
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
- `display_limit` (query, optional; integer | null)

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

### `GET /health/limits`

Health Limits

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`

### `GET /health/live`

Health Live

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`

### `GET /health/ready`

Health Ready

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `503`: A required dependency is unavailable

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

### `GET /issue-brief`

Build a legal issue brief for a tag

Summarizes active-taxonomy tagged decisions by year, outcome, and court, with resolved case authorities and traceable decision links. Outcome percentages use all decisions in the year as denominator and each split includes the unclassified count and denominator. An empty tag returns an empty brief.

**Parameters**

- `tag` (query, optional; string, default `""`): Exact legal tag in category:value form; empty is supported.

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /judges/compare`

Judge Comparison

Compare stored research coverage, shared issues and outcomes; not a ranking.

**Parameters**

- `a` (query, required; string): Canonical judge slug
- `b` (query, required; string): Canonical judge slug

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `404`: Unknown canonical judge slug (detail.code: unknown_judge)
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/analyze`

Live Analysis Analyze

**Parameters**

- `resolve` (query, optional; boolean, default `false`)

**Request body (required)**

- `multipart/form-data`: `Body_live_analysis_analyze_live_analysis_analyze_post`

**Responses**

- `200`: Successful Response; `application/json`: `LiveAnalysisResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/issue-matches`

Live Analysis Issue Matches

Decided issues close to one pasted argument. Keyword search only, nothing stored, no model.

**Request body (required)**

- `application/json`: `IssueMatchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/reader`

Live Analysis Reader

Reader-shaped analysis of an uploaded document for markup mode. In memory only; no model is called.

**Request body (required)**

- `multipart/form-data`: `Body_live_analysis_reader_live_analysis_reader_post`

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/reader-text`

Live Analysis Reader Text

Same as ``/live-analysis/reader`` for pasted text.

**Request body (required)**

- `application/json`: `LiveReaderTextRequest`

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /live-analysis/resolve`

Live Analysis Resolve

**Request body (required)**

- `multipart/form-data`: `Body_live_analysis_resolve_live_analysis_resolve_post`

**Responses**

- `200`: Successful Response; `application/json`: `LiveAnalysisResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /memo-citation-check`

Memo Citation Check Analyze

**Request body (required)**

- `multipart/form-data`: `Body_memo_citation_check_analyze_memo_citation_check_post`

**Responses**

- `200`: Successful Response; `application/json`: `MemoCitationCheckResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /precedent-finder`

Precedent Finder Analyze

Ephemeral V3 tag matching with bounded resolved-authority ranking.

Rank by distinct matching citing decisions, distinct matched tags, authority
date descending, then citation ascending. Statutes do not influence ranking.
All responses are no-store; no raw proposition is returned or persisted.

**Request body (required)**

- `application/json`: `object`

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `413`: Proposition or JSON body exceeds the input limit; input is never echoed.
- `422`: Invalid JSON proposition; input is never echoed.
- `500`: Research unavailable; input is never echoed.

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

### `GET /saved-searches`

List Saved Searches

**Responses**

- `200`: Successful Response; `application/json`: `array`

### `POST /saved-searches`

Create Saved Search

**Request body (required)**

- `application/json`: `SavedSearchCreateRequest`

**Responses**

- `201`: Successful Response; `application/json`: `SavedSearchResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /saved-searches/digest`

Saved Search Digest

Build a read-only digest of recorded case alerts, not live search results.

**Parameters**

- `since` (query, optional; string | null): Override last checks with an ISO timestamp

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /saved-searches/digest.html`

Saved Search Digest Html

Render the same read-only digest as self-contained inline-CSS HTML.

**Parameters**

- `since` (query, optional; string | null): Override last checks with an ISO timestamp

**Responses**

- `200`: Successful Response; `text/html`: `string`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `DELETE /saved-searches/{search_id}`

Delete Saved Search

**Parameters**

- `search_id` (path, required; integer)

**Responses**

- `204`: Successful Response
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /saved-searches/{search_id}`

Get Saved Search

**Parameters**

- `search_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `SavedSearchDetailResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `PUT /saved-searches/{search_id}`

Update Saved Search

**Parameters**

- `search_id` (path, required; integer)

**Request body (required)**

- `application/json`: `SavedSearchUpdateRequest`

**Responses**

- `200`: Successful Response; `application/json`: `SavedSearchResponse`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `POST /saved-searches/{search_id}/check`

Check Saved Search

**Parameters**

- `search_id` (path, required; integer)

**Responses**

- `200`: Successful Response; `application/json`: `SearchDigestResponse`
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

### `POST /search/chunks/paragraphs`

Search Paragraphs

**Request body (required)**

- `application/json`: `CaseSearchRequest`

**Responses**

- `200`: Successful Response; `application/json`: `array`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /search/export.csv`

Export Search Analytics Cases

**Parameters**

- `query` (query, optional; string, default `""`)
- `cites` (query, optional; string, default `""`)
- `government_outcome` (query, optional; string, default `""`)
- `decision_outcome` (query, optional; string, default `""`)
- `minister` (query, optional; string, default `""`)
- `judge` (query, optional; string, default `""`)
- `court` (query, optional; string, default `""`)
- `year` (query, optional; string, default `""`)
- `cites_case_id` (query, optional; integer | null)
- `tags` (query, optional; string, default `""`)
- `case_type` (query, optional; string, default `""`)
- `search_full_text` (query, optional; boolean, default `false`)
- `sort_by` (query, optional; string, default `"relevance"`)
- `cohort_id` (query, optional; string, default `""`)

**Responses**

- `200`: Successful Response; `text/csv`: `string`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /search/export.docx`

Export Search Docx

Export up to 200 cases using the Data Explorer search filters.

**Parameters**

- `query` (query, optional; string, default `""`)
- `cites` (query, optional; string, default `""`)
- `government_outcome` (query, optional; string, default `""`)
- `decision_outcome` (query, optional; string, default `""`)
- `minister` (query, optional; string, default `""`)
- `judge` (query, optional; string, default `""`)
- `court` (query, optional; string, default `""`)
- `year` (query, optional; string, default `""`)
- `cites_case_id` (query, optional; integer | null)
- `tags` (query, optional; string, default `""`)
- `search_full_text` (query, optional; boolean, default `false`)
- `sort_by` (query, optional; string, default `"relevance"`)
- `limit` (query, optional; integer, default `50`)

**Responses**

- `200`: Successful Response; `application/json`: `unspecified`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /search/tags/similar`

Find Similar Cases By Tags

Find cases with overlapping tags. Score by Jaccard similarity of tag (category, value) pairs.

**Parameters**

- `case_id` (query, required; integer)
- `limit` (query, optional; integer, default `10`)

**Responses**

- `200`: Successful Response; `application/json`: `object`
- `422`: Validation Error; `application/json`: `HTTPValidationError`

### `GET /themes/discovery`

Get Theme Discovery

Discover recurring legal themes across Core-300 by grouping subthemes with shared key terms.

**Responses**

- `200`: Successful Response; `application/json`: `ThemeDiscoveryResponse`

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

### `POST /access/logout`

**Hidden from OpenAPI.**

Handler: `backend.main.access_logout`

**Handler parameters**

- `request` (Request; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/about/library`

**Hidden from OpenAPI.**

Handler: `backend.routes.about_library`

**Handler parameters**

- `db` (Session; default `Depends(get_db)`)
- `response` (Response; default `None`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/about/stats`

**Hidden from OpenAPI.**

Handler: `backend.routes.about_stats`

**Handler parameters**

- `db` (Session; default `Depends(get_db)`)
- `response` (Response; default `None`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/cases/{case_id}/similar-cases`

**Hidden from OpenAPI.**

Handler: `backend.similar_cases.similar_cases`

**Handler parameters**

- `case_id` (int; required)
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

### `POST /api/deidentify`

**Hidden from OpenAPI.**

Handler: `backend.routes.deidentify_api`

**Handler parameters**

- `file` (fastapi.datastructures.UploadFile | None; default `File(None)`)
- `text` (str; default `Form()`)
- `names` (str; default `Form()`)
- `details` (str; default `Form()`)
- `categories` (str; default `Form()`)
- `auto_names` (bool; default `Form(True)`)
- `never_hide` (str; default `Form()`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /api/deidentify/docx`

**Hidden from OpenAPI.**

Handler: `backend.routes.deidentify_docx_api`

**Handler parameters**

- `text` (str; default `Form(PydanticUndefined)`)
- `filename` (str; default `Form(document.docx)`)

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
- `source_type` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)
- `response` (Response; default `None`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/breakdowns`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_breakdowns`

**Handler parameters**

- `city` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/case`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_case`

**Handler parameters**

- `imm` (str; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/counsel`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_counsel`

**Handler parameters**

- `min_files` (int; default `20`)
- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
- `decision_body` (str; default `''`)
- `city` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/dashboard`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_dashboard`

**Handler parameters**

- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
- `city` (str; default `''`)
- `decision_body` (str; default `''`)
- `application_type` (str; default `''`)
- `representation` (str; default `''`)
- `language` (str; default `''`)
- `office` (str; default `''`)
- `resolution` (str; default `''`)
- `judge` (str; default `''`)
- `counsel` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/flow`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_flow`

**Handler parameters**

- `city` (str; default `''`)
- `source_type` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/insights`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_insights`

**Handler parameters**

- `city` (str; default `''`)
- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
- `decision_body` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/judges`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_judges`

**Handler parameters**

- `min_decisions` (int; default `25`)
- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
- `decision_body` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /api/fc-activity/motions`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_activity_motions`

**Handler parameters**

- `city` (str; default `''`)
- `year_from` (int | None; default `None`)
- `year_to` (int | None; default `None`)
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
- `response` (Response; default `None`)

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

### `POST /api/reidentify`

**Hidden from OpenAPI.**

Handler: `backend.routes.reidentify_api`

**Handler parameters**

- `file` (fastapi.datastructures.UploadFile | None; default `File(None)`)
- `text` (str; default `Form()`)
- `key` (str; default `Form(PydanticUndefined)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /business-case`

**Hidden from OpenAPI.**

Handler: `backend.routes.business_case_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /case-compare`

**Hidden from OpenAPI.**

Handler: `backend.routes.case_compare_page`

**Handler parameters**

- `a` (str; default `''`)
- `b` (str; default `''`)
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

### `GET /case-reader-ui/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.routes.case_reader_ui_page`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

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

### `GET /coming-soon-demo`

**Hidden from OpenAPI.**

Handler: `backend.routes.coming_soon_demo_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /coming-soon-preview`

**Hidden from OpenAPI.**

Handler: `backend.routes.coming_soon_preview_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /coming-soon-preview/img/{name}`

**Hidden from OpenAPI.**

Handler: `backend.routes.coming_soon_preview_image`

**Handler parameters**

- `name` (str; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /coming-soon/{section}`

**Hidden from OpenAPI.**

Handler: `backend.routes.coming_soon_page`

**Handler parameters**

- `section` (str; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /compare`

**Hidden from OpenAPI.**

Handler: `backend.routes.compare_cases_page`

**Handler parameters**

- `a` (str; default `''`)
- `b` (str; default `''`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /data-explorer`

**Hidden from OpenAPI.**

Handler: `backend.routes.data_explorer_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /deidentify`

**Hidden from OpenAPI.**

Handler: `backend.routes.deidentify_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/cases/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_case`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/cases/{case_id}/activity`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_activity`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/cases/{case_id}/paragraph-assessments`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_paragraph_assessments`

**Handler parameters**

- `case_id` (int; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/cases/{case_id}/reader-data`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_reader_data`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/cases/{case_id}/statute-references`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_statute_references`

**Handler parameters**

- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /discussion-units-sandbox/search`

**Hidden from OpenAPI.**

Handler: `backend.routes.discussion_units_sandbox_search`

**Handler parameters**

- `query` (str; default `''`)
- `cites` (str; default `''`)
- `government_outcome` (str; default `''`)
- `decision_outcome` (str; default `''`)
- `minister` (str; default `''`)
- `judge` (str; default `''`)
- `court` (str; default `''`)
- `year` (str; default `''`)
- `search_full_text` (bool; default `False`)
- `sort_by` (str; default `'relevance'`)
- `limit` (int; default `50`)
- `offset` (int; default `0`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /fc-history`

**Hidden from OpenAPI.**

Handler: `backend.routes.fc_history_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /future-features`

**Hidden from OpenAPI.**

Handler: `backend.routes.future_features_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /issue-brief-ui`

**Hidden from OpenAPI.**

Handler: `backend.routes.get_issue_brief_ui`

**Handler parameters**

- `tag` (str; default `Query()`)
- `db` (Session; default `Depends(get_db)`)

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

### `GET /memo-citation-check`

**Hidden from OpenAPI.**

Handler: `backend.routes.memo_citation_check_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /precedent-finder`

**Hidden from OpenAPI.**

Handler: `backend.routes.precedent_finder_page`

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

### `GET /saved-searches-ui`

**Hidden from OpenAPI.**

Handler: `backend.routes.saved_searches_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /site-tour.css`

**Hidden from OpenAPI.**

Handler: `backend.routes.site_tour_styles`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /site-tour.js`

**Hidden from OpenAPI.**

Handler: `backend.routes.site_tour_script`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /site-tour/sample-memo.docx`

**Hidden from OpenAPI.**

Handler: `backend.routes.site_tour_sample_memo`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /statute-consideration`

**Hidden from OpenAPI.**

Handler: `backend.statute_consideration.statute_consideration_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /statute-library`

**Hidden from OpenAPI.**

Handler: `backend.routes.statute_library_page_route`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /statutes`

**Hidden from OpenAPI.**

Handler: `backend.routes.statute_viewer_page_route`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /tag-finder`

**Hidden from OpenAPI.**

Handler: `backend.routes.tag_finder_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /testing`

**Hidden from OpenAPI.**

Handler: `backend.routes.testing_interface`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /themes`

**Hidden from OpenAPI.**

Handler: `backend.routes.theme_explorer_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /unit-search`

**Hidden from OpenAPI.**

Handler: `backend.routes.get_unit_search`

**Handler parameters**

- `q` (str; default `Query(PydanticUndefined)`)
- `limit` (int; default `Query(8)`)
- `court` (str; default `Query()`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /welcome`

**Hidden from OpenAPI.**

Handler: `backend.main.welcome_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench`

**Hidden from OpenAPI.**

Handler: `backend.workbench.workbench_page`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/cases`

**Hidden from OpenAPI.**

Handler: `backend.workbench.list_cases`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/cases`

**Hidden from OpenAPI.**

Handler: `backend.workbench.add_cases`

**Handler parameters**

- `body` (AddCasesRequest; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/cases/export.csv`

**Hidden from OpenAPI.**

Handler: `backend.workbench.export_cases`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/cases/seen-all`

**Hidden from OpenAPI.**

Handler: `backend.workbench.mark_all_seen`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `DELETE /workbench/api/cases/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.delete_case`

**Handler parameters**

- `case_id` (int; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/cases/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.case_detail`

**Handler parameters**

- `case_id` (int; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `PATCH /workbench/api/cases/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.update_case`

**Handler parameters**

- `case_id` (int; required)
- `body` (ItemUpdate; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/cases/{case_id}/seen`

**Hidden from OpenAPI.**

Handler: `backend.workbench.mark_seen`

**Handler parameters**

- `case_id` (int; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/me`

**Hidden from OpenAPI.**

Handler: `backend.workbench.workbench_me`

**Handler parameters**

- `request` (Request; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/pins`

**Hidden from OpenAPI.**

Handler: `backend.workbench.list_pins`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/pins`

**Hidden from OpenAPI.**

Handler: `backend.workbench.add_pin`

**Handler parameters**

- `body` (PinRequest; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/pins/export.csv`

**Hidden from OpenAPI.**

Handler: `backend.workbench.export_pins`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/pins/state`

**Hidden from OpenAPI.**

Handler: `backend.workbench.pin_state`

**Handler parameters**

- `request` (Request; required)
- `case_id` (int; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `DELETE /workbench/api/pins/{pin_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.delete_pin`

**Handler parameters**

- `pin_id` (int; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `PATCH /workbench/api/pins/{pin_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.update_pin`

**Handler parameters**

- `pin_id` (int; required)
- `body` (ItemUpdate; required)
- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/signin`

**Hidden from OpenAPI.**

Handler: `backend.workbench.workbench_signin`

**Handler parameters**

- `body` (SignInRequest; required)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `POST /workbench/api/signout`

**Hidden from OpenAPI.**

Handler: `backend.workbench.workbench_signout`

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/api/summary`

**Hidden from OpenAPI.**

Handler: `backend.workbench.summary`

**Handler parameters**

- `owner` (str; default `Depends(current_owner)`)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/brief`

**Hidden from OpenAPI.**

Handler: `backend.workbench.brief_all`

**Handler parameters**

- `request` (Request; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.

### `GET /workbench/brief/case/{case_id}`

**Hidden from OpenAPI.**

Handler: `backend.workbench.brief_case`

**Handler parameters**

- `case_id` (int; required)
- `request` (Request; required)
- `db` (Session; default `Depends(get_db)`)

**Responses**

- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.
