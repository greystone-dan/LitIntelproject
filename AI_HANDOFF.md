# AI CaseLibrary Handoff

Last updated: 2026-09-02

This document is a detailed working handoff and may contain time-bound implementation context. For the canonical current architecture, functionality, data model, operations, limitations, and code-review posture, see `SYSTEM_REFERENCE.md`.

## 0. Active Delivery Focus (2026-08-12)

Current delivery focus is user-facing advanced search and linked citation reading,
with deterministic extractor QA retained as a supporting workflow.

The standalone Live Analysis prototype is available at `/live-analysis` for
ephemeral document review. It accepts DOCX and text-based PDF uploads, preserves
source offsets and PDF page locations, and never persists the uploaded document.
Extraction and citation resolution are separate actions; `/live-analysis/resolve`
can match neutral, named, and short-form references against local case metadata.

Primary workflow for this phase:

1. Use `/data-explorer` as the primary research-facing surface.
2. Use `/case-reader` for unified case detail and linked citation inspection.
3. Preserve exact citation spans and offsets as backend-owned truth.
4. Keep extraction, target resolution, and reader UX as separate concerns.
5. Use `/citation-pass` only when validating extraction behavior.
6. Update explainer docs in the same change set before push.

Hard scope constraints currently in force:

1. Keep case citations, statutes/instruments, and metadata as separate extractor
	and API payload layers.
2. Runtime extraction must remain deterministic and must not require AI/API calls.
3. Preserve exact backend-owned source spans; the UI must not infer or reparse them.
4. Keep case-to-case target resolution as a separate local pass after extraction.
5. Keep side-project datasets isolated from canonical case tables and routes.
6. Keep Live Analysis uploads in memory; optional local resolution may read case
	metadata but must not write database records or call external resolution services.

Current live user-facing capabilities in this phase:

1. `/data-explorer` now includes advanced search, judge outcomes, and case data explorer tabs.
2. Advanced search supports cited-authority filtering, minister dropdown selection, date and outcome filters, and result sorting.
3. The decision modal uses stored citation rows and returns exact highlight spans quickly even for heavily cited cases.
4. Citation result cards and reader payloads expose citation counts, unique cited authorities, and linked target-case counts.
5. Local target resolution is populated in the database and no longer just planned.

Layered extraction work completed in this pass:

1. Case-only extraction supports full anchors, grounded aliases, parenthetical
	span expansion, and Unicode-safe UI offset conversion.
2. `extract_statute_reference_matches()` independently selects only statute and
	instrument candidates.
3. Law matching covers Acts, Codes, Regulations, Rules, Orders, SOR/SI
	citations, international instruments, plural provisions, and bounded anchored
	short forms in paragraph text and headings.
4. `extract_metadata_matches()` converts canonical deterministic FC metadata
	into exact source spans with confidence and provenance.
5. `/cases/{case_id}/citation-pass` returns `live_extracted`, `live_statutes`,
	and `live_metadata`; the UI uses orange, green, and blue respectively.

Targeted verification on this pass:

1. Dedicated statute-layer regressions: `6 passed`.
2. Citation-pass API separation contract: `1 passed`.
3. Metadata exact-span contract: `1 passed`.
4. Live Febles payload: `168` case citations, `442` law references, zero law
	span errors, including `9` standalone Article 31/32 headings.
5. Live Hasani payload: `48` case citations, `62` law references, `10` metadata
	fields, and zero span errors across all layers.
6. Updated review server: `http://127.0.0.1:8060/citation-pass`.

Known caution:

1. The repository is in a large dirty state with many parallel changes beyond the citation-pass track.
2. Full `pytest -q` currently stops during collection at
	`tests/test_fc_document_scraper.py:58` because of a pre-existing syntax error.
	Do not represent the focused green tests as a full-suite baseline.
3. Anchored short-form law propagation is deliberately bounded to avoid turning
	ordinary prose or judgment paragraph numbers into statute references.

Immediate entry point for the next agent:

1. Run a deterministic cohort audit for statute/instrument false negatives and
	false positives, grouped by format, before broad persistence/reprocessing.
2. Add real-case regressions for remaining uncovered instruments, French statute
	forms, Parts/Schedules, and provision references beyond the current anchor window.
3. Repair or reconcile the unrelated FC document-scraper test syntax error, then
	run the full suite and record a new baseline.

### 0.1 Docket Number Field Backfill (2026-08-19)

A new `docket_number` column was added to the canonical `cases` table to capture Federal Court docket and file identifiers separately from citation semantics.

Backfill results across the 35,902-case corpus:

1. **Coverage**: 35,451 of 35,902 cases (98.74%)
2. **IMM pattern** (IMM-XXXX-YY): 22,140 cases
3. **T pattern** (T-XXXX): 13,308 cases
4. **Other**: 3 cases
5. **Not found**: 451 cases (likely non-Federal-Court or missing docket in text)

Extraction method: Scanned title, summary, and first chunk text for `T-\d+` and `IMM-\d{1,6}-\d{2,4}` patterns. This is a read-only backfill; the field is nullable and does not affect existing citation pipelines.

### 0.2 Pickup Estimate And Statute Scope Guardrail (2026-08-10)

Current rough citation pickup estimate for deterministic extraction:

1. Fresh cohort audit (`data/eval/reports/case_citation_coverage_fresh.json`) over 294 matched FC-priority cases reports 18,623 extracted citations.
2. Miss proxies in that audit are 156 anchored-alias misses and 88 parenthetical misses.
3. Rough extraction pickup estimate is approximately 98.7% for this cohort.
4. A more conservative case-level cleanliness read from the 480-case postpatch external audit remains about 93.1% (`33/480` cases flagged with missing citations).

Statute work priority for the current phase:

1. Do not expand broad statute/instrument scope right now beyond high-value fixes.
2. Keep IRPA and IRPR extraction quality as a hard requirement.
3. Ensure section-pattern references such as `34(1)(f)` (and similar nested subsection/paragraph forms) are consistently detected and normalized when cited in running text, parentheticals, and headings.
4. Treat IRPA/IRPR section-format misses as release blockers for the citation-pass/statute layer even when non-IRPA statute coverage remains unchanged.

## 1. What This System Is

AI CaseLibrary is a Canadian legal research system focused on immigration litigation workflows. The system ingests case law and supporting materials, normalizes them into a PostgreSQL canonical store, chunks and embeds text for retrieval, tags cases with structured legal metadata, and exposes citation-graph and search tooling for research workflows.

The project is not just a search app. It is a layered legal research platform with:

1. Canonical case storage.
2. Chunk-level retrieval and embeddings.
3. Citation graph construction and analytics.
4. Topic/issue/legal-area tagging.
5. API routes and UI surfaces for case review, citation map exploration, and research workflows.
6. QA harnesses for deterministic extraction, route coverage, and budget-bounded external audit.

## 2. System Layers

### Layer 1: Source Acquisition And Staging

This layer brings raw source data into the ecosystem. The code is split across source-specific ingestion and staging scripts.

Key areas:

1. `fc_ingest/` for Federal Court collection and staging.
2. `canlaw/` for source helpers and local embedding tooling.
3. `scripts/ingest_*`, `scripts/import_*`, and `scripts/crawl_*` for bringing source artifacts into the local workflow.
4. `scripts/download_reference_library.py` and related scripts for reference documents.

Practical role:

1. Pull source records from APIs, parquet, HTML, or local files.
2. Normalize case metadata, text, and provenance.
3. Persist staging artifacts before canonical ingestion.

### Layer 2: Canonical Database

The canonical schema lives in `backend/database.py`. This is the system of record for cases, chunks, citations, tags, embeddings, metrics, and several A2AJ-related staging tables.

Core entities:

1. `Case`
2. `CaseChunk`
3. `Citation`
4. `CitationMetrics`
5. `CaseTag`
6. `CaseTaggingStatus`
7. `CaseChunkEmbedding`
8. `A2AJCase`
9. `A2AJCitationEdge`
10. `A2AJCaseMap`

### Layer 3: Extraction, Enrichment, And Graph Construction

This is where raw text becomes structured research data.

Main modules:

1. `backend/citations.py` for citation extraction and resolution.
2. `backend/legal_tagger.py` for legal tagging.
3. `backend/embedding_providers.py` for embedding provider wiring.
4. `backend/citation_map.py` for graph analytics and citation-map computations.
5. `backend/case_reader.py` for case reading / UI helper surfaces.

This layer computes:

1. Citation rows with offsets and normalized text.
2. Graph edges between citing cases and cited authorities.
3. Authority metrics such as in-degree, out-degree, and pagerank.
4. Higher-order analytics like missing authorities, completion suggestions, lifecycle trends, hidden bridges, and doctrine shifts.

### Layer 4: API And UI Surfaces

`backend/routes.py` exposes the primary FastAPI surface.

Primary routes include:

1. Search and retrieval.
2. Citation map summary and graph analytics.
3. CSV export variants for most citation-map endpoints.
4. Research assistant and quick-search views.

### Layer 5: QA, Evaluation, And External Audit

The QA layer is not just unit tests. It includes:

1. Pytest coverage for extractors, routes, and helper logic.
2. Deterministic citation extraction verification.
3. Stored-citation external audit with a cheap OpenAI model.
4. Retrieval evaluation scripts and benchmark-style checks.

Relevant files:

1. `tests/`
2. `scripts/verify_citation_extraction.py`
3. `scripts/evaluate_retrieval.py`
4. `scripts/embed_openai_chunks.py`

## 3. Live Scale Snapshot

These counts came from the live database at the time of this handoff.

| Object | Count |
| --- | ---: |
| Cases | 35,902 |
| Cases with chunks | 35,902 |
| Text-bearing cases | 35,856 |
| Cases with docket_number | 35,451 |
| Case chunks | 1,390,886 |
| Citations | 1,492,628 |
| Linked citations | 760,197 |
| Unresolved citations | 732,431 |
| Unique linked target cases | 31,944 |
| Citation rows with chunk_id | 1,492,628 |
| Citation rows without chunk_id | 0 |
| Case tags | 0 |
| Chunk embeddings | 0 |
| LotD side-project cases (`lotd.cases`) | 218,639 |
| LotD side-project dockets (`lotd.dockets`) | 2,610,399 |

### Citation Graph Summary

The graph summary computed by `backend/citation_map.py` is:

| Metric | Count |
| --- | ---: |
| Total cases | 35,902 |
| Resolved citation occurrences | 217,339 |
| Unresolved citation occurrences | 86,477 |
| Aggregated case-to-case edges | 166,328 |
| Connected cases | 32,112 |
| Cases with citation metrics | 35,902 |

Interpretation:

1. The system has broad citation coverage and a substantial linked graph.
2. The active database is currently centered on text, paragraph chunks, metadata, and citations rather than populated tags or embeddings.
3. The separate `lotd` schema is present for side-project work and does not feed the main application.

## 4. Tags And Embeddings

### Case Tags

`CaseTag` stores structured labels with the following fields:

1. `id`
2. `case_id`
3. `category`
4. `value`
5. `score`
6. `evidence`
7. `source`
8. `taxonomy_version`
9. `created_at`

Observed tag breakdown:

| Category | Count |
| --- | ---: |
| statute | 129,369 |
| proceeding | 57,454 |
| citation_network | 55,929 |
| issue | 54,977 |
| legal_area | 40,338 |
| convention_ground | 39,657 |
| source | 35,907 |
| court | 35,907 |
| decision_year | 35,907 |
| language | 35,856 |
| regulation | 34,763 |
| standard_of_review | 30,931 |
| minister | 28,683 |
| remedy | 26,842 |
| risk | 22,401 |
| country | 18,690 |
| tribunal | 18,058 |
| evidence | 12,162 |
| outcome | 9,444 |
| authority | 7,430 |
| agency | 7,211 |
| program_impact | 7,077 |
| inadmissibility | 6,186 |
| enforcement_action | 5,043 |
| international_instrument | 3,618 |
| enforcement_impediment | 3,578 |
| cbsa_program | 2,308 |
| organization | 2,059 |
| legacy_topic | 1,296 |
| detention_ground | 874 |
| guideline | 239 |
| release_mechanism | 176 |
| docket_type | 25 |

Observed tag source breakdown:

| Source | Count |
| --- | ---: |
| text_rule | 569,568 |
| structured_metadata | 164,971 |
| metadata | 35,856 |

Observed taxonomy versions:

| Taxonomy | Count |
| --- | ---: |
| ca_legal_v2 | 770,357 |
| ca_legal_v1 | 38 |

Takeaway:

1. Tag coverage is effectively universal across the case set.
2. Most tags are rule-derived.
3. `ca_legal_v2` is the active taxonomy in production-scale use.

### Embeddings

Observed chunk embedding model:

| Model | Count |
| --- | ---: |
| BAAI/bge-m3 | 5,808 |

Observed case embeddings:

1. `Case.embedding` is present for 429 cases.
2. Most retrieval work is chunk-based rather than case-vector based.

## 5. Citation Record Model

The canonical citation row is `Citation` in `backend/database.py`.

### Fields Tracked On Each Citation

1. `id`
2. `source_case_id`
3. `target_case_id`
4. `citation_text`
5. `normalized_citation`
6. `provenance`
7. `chunk_id`
8. `offset_start`
9. `offset_end`
10. `unresolved`
11. `created_at` is not present on `Citation` in the current schema; timing is inferred from the owning case and chunk timestamps.

### What Each Field Means

1. `source_case_id` is the citing case.
2. `target_case_id` is the cited authority when the link is resolved.
3. `citation_text` is the literal text span extracted from the source.
4. `normalized_citation` is the normalized form used for matching, grouping, and graph analytics.
5. `provenance` records the origin of the row. Current live data is entirely `local`.
6. `chunk_id` points to the source chunk that contained the citation.
7. `offset_start` and `offset_end` give the character span within the chunk text.
8. `unresolved` flags citations that did not resolve to a target case.
9. There is no dedicated citation timestamp column today. Use `Case.created_at` and `CaseChunk.created_at` when you need source timing metadata.

### Current Citation Storage Shape

1. Every stored citation row currently has `chunk_id` populated.
2. Every stored citation row currently has `provenance = local`.
3. There are no citation rows stored without a chunk reference in the current database snapshot.
4. Roughly 71.5% of citation rows are resolved to a target case, and the rest remain unresolved.
5. Citation rows do not currently carry their own explicit timestamp field.

### Citation Metrics

`CitationMetrics` stores per-case graph metrics:

1. `case_id`
2. `in_degree`
3. `out_degree`
4. `pagerank`

These metrics are used to rank authorities and make the graph surface more interpretable.

## 6. Citation Map Capabilities

The citation-map system is the strongest analytical surface in the repo. It is exposed through many API routes in `backend/routes.py` and computed in `backend/citation_map.py`.

### Core Discovery And Graph Summary

1. `/citation-map/summary`
2. `/citation-map/authorities`
3. `/citation-map/cases`
4. `/citation-map/topics`
5. `/citation-map/issues/graph`
6. `/citation-map/cases/{case_id}/authority-map`
7. `/citation-map/cases/{case_id}/tags`
8. `/citation-map/common-citers`

What these do:

1. Summarize the graph and graph coverage.
2. List the top cited authorities.
3. Search cases by title or citation.
4. Surface topic-like label groups.
5. Build a local issue graph from tags and citations.
6. Show the authority neighborhood of a specific case.
7. Return structured legal tags for a case.
8. Find cases that cite the same authorities.

### Path And Context Tools

1. `/citation-map/paths`
2. `/citation-map/paths/contextual`
3. `/citation-map/paths/hidden`
4. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/summary`
5. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts`
6. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts.csv`

These are the evidence-heavy surfaces.

Tracked context fields include:

1. `citation_id`
2. `source_case_id`
3. `source_title`
4. `source_citation`
5. `target_case_id`
6. `target_title`
7. `target_citation`
8. `chunk_id`
9. `chunk_index`
10. `citation_text`
11. `normalized_citation`
12. `offset_start`
13. `offset_end`
14. `context_start`
15. `context_end`
16. `context`

What the path tools do:

1. Show shortest or bounded citation paths between cases.
2. Add context to each hop so the path is evidence-backed.
3. Reveal hidden bridge cases that connect two authorities through intermediate citation chains.
4. Export contexts to CSV for audit and research workflows.

### Authority Intensity And Surprise Tools

1. `/citation-map/cases/{case_id}/authority-signals`
2. `/citation-map/cases/{case_id}/authority-signals.csv`
3. `/citation-map/surprises`
4. `/citation-map/surprises.csv`
5. `/citation-map/authorities/landmarks`
6. `/citation-map/authorities/landmarks.csv`

Fields exposed in authority-signal views:

1. `authority`
2. `occurrence_count`
3. `distinct_chunks`
4. `gravity_share`
5. `global_citing_cases`
6. `surprise_score`
7. `originality_score`
8. `boilerplate_hits`
9. `first_chunk_index`
10. `last_chunk_index`
11. `sample_contexts`

Fields exposed in surprise views:

1. `source_case`
2. `authority`
3. `occurrence_count`
4. `global_citing_cases`
5. `gravity_share`
6. `surprise_score`

### Missing Authority And Completion Tools

1. `/citation-map/cases/{case_id}/missing-authorities`
2. `/citation-map/cases/{case_id}/missing-authorities.csv`
3. `/citation-map/cases/{case_id}/position-profiles`
4. `/citation-map/cases/{case_id}/position-profiles.csv`
5. `/citation-map/cases/{case_id}/completion-suggestions`
6. `/citation-map/cases/{case_id}/completion-suggestions.csv`

Tracked fields in these views:

1. `authority`
2. `peer_citing_cases`
3. `peer_coverage`
4. `peer_occurrences`
5. `rarity_boost`
6. `priority_score`
7. `occurrence_count`
8. `avg_chunk_index`
9. `first_chunk_index`
10. `last_chunk_index`
11. `first_half_hits`
12. `second_half_hits`
13. `expected_occurrences`
14. `recommendation_score`

What these are for:

1. Detect likely missing authorities in a case compared with peer cases.
2. Measure where an authority tends to appear in a case.
3. Suggest likely completion opportunities when an authority cluster looks incomplete.

### Doctrine Shift, Replacement, Lifecycle, And Cross-Court Flow

1. `/citation-map/authorities/replacement`
2. `/citation-map/authorities/lifecycle`
3. `/citation-map/authorities/lifecycle.csv`
4. `/citation-map/courts/flow`
5. `/citation-map/courts/flow.csv`
6. `/citation-map/issues/shifts`
7. `/citation-map/issues/dashboard`
8. `/citation-map/issues/dashboard.csv`
9. `/citation-map/issues/shifts.csv`

Tracked fields in these views:

1. `old_authority`
2. `new_authority`
3. `replacement_score`
4. `status`
5. `series`
6. `authority`
7. `recent_citing_cases`
8. `prior_citing_cases`
9. `total_citing_cases`
10. `velocity`
11. `decay`
12. `lifecycle_stage`
13. `source_court`
14. `target_court`
15. `citing_case_count`
16. `citation_occurrences`
17. `replacement_candidates`
18. `emerging_authorities`
19. `declining_authorities`
20. `surprises`

What these are for:

1. Track authority replacement over time.
2. Show whether an authority is rising, plateauing, or declining.
3. Measure cross-court authority flow.
4. Surface doctrine shifts within a given issue, statute, or legal area.

### Inheritance And Co-Citation Tools

1. `/citation-map/authorities/{case_id}/inheritance`
2. `/citation-map/authorities/{case_id}/inheritance.csv`
3. `/citation-map/authorities/{case_id}/co-cited`
4. `/citation-map/cases/{case_id}/similar`

Tracked fields:

1. `chain_case_ids`
2. `depth`
3. `total_occurrences`
4. `nodes`
5. `edge_occurrences`
6. `shared_authority_count`
7. `rarity_weighted_score`
8. `shared_authorities`
9. `shared_citing_cases`
10. `citation_occurrences`

What these do:

1. Show inheritance chains for authorities.
2. Surface co-cited authorities.
3. Find similar cases based on shared authorities.

### Citation Edge Evidence Tools

1. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/summary`
2. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts`
3. `/citation-map/cases/{source_case_id}/citations/{target_case_id}/contexts.csv`

These are the core evidence export surfaces for a specific Case A cites Case B relationship.

Tracked fields in edge summaries:

1. `source_case`
2. `target_case`
3. `occurrence_count`
4. `distinct_chunks`
5. `first_chunk_index`
6. `last_chunk_index`
7. `top_normalized_citations`
8. `sample_contexts`

### Citation Map Topics And Issue Graph

1. `/citation-map/topics`
2. `/citation-map/issues/graph`

These route families connect tags to citation analytics so the system can move between issue categories and citation evidence.

Tracked fields:

1. `category`
2. `value`
3. `case_count`
4. `available_cases`
5. `nodes`
6. `edges`

## 7. API and UI Surface Summary

The user-facing surfaces currently include:

1. `GET /quick-search`
2. `GET /case-reader`
3. `GET /citation-map`
4. `GET /research`
5. `GET /testing`

The main API areas are:

1. Search and retrieval.
2. Citation map analytics.
3. Research assistant responses.
4. CSV exports for analysis and offline review.

The app also includes OpenAI-backed features in selected routes, but the current external-audit work intentionally uses a narrow budget and should not be treated as a production inference layer for citation truth.

## 8. QA Status And 1000-Case External Audit

The recent QA work introduced a two-part citation audit strategy:

1. Deterministic fixture-based citation extraction checks.
2. A cheap external OpenAI audit over already stored citation rows.

### Deterministic QA Baseline

The deterministic citation verification harness and focused tests are currently green.

### 1000-Case Stored Citation Audit

This was a real audit of stored litigation citations, meaning Case A to Case B links already in the database. It did not re-run extraction forward from raw text.

Run details:

1. Sample size: 1,000 source cases.
2. Stored citation rows audited: 5,683 case-to-case citations.
3. Budget cap: $0.15.
4. Model: `gpt-4.1-nano`.
5. Actual spend: about $0.136624.
6. Processed cases: 462.
7. Failed responses: 538.
8. Flagged missing citations: 36.
9. Flagged mischaracterized citations: 133.

Important caveat:

1. The cheap model produced malformed JSON very often at this scale.
2. Many of the returned mischaracterizations were duplicate/redundancy noise rather than true extraction defects.
3. The audit is still useful as a triage signal, but not as an automatic source of truth.

### Most Useful Audit Findings

The audit surfaced a few likely real extraction issues:

1. A citation like `IRPA s.40(1)` is present where the surrounding text shows `IRPA s.40(1)(c)`. That suggests the stored citation text may be truncated.
2. Party-style case citations sometimes appear only partially captured, especially where a reporter citation is present in context but the row is incomplete.
3. One example flagged a citation like `[2005] F.C.J. No. 1290` as incomplete, which is exactly the type of reporter-style truncation that should be fixed deterministically.

### Most Common Noisy Audit Patterns

1. Duplicate citation mentions being treated as suspicious.
2. Same authority repeated across a case being called a mischaracterization.
3. Context snippets causing the model to infer truncation when the citation text itself is correct.

### Practical Interpretation

The audit says the current citation graph is broadly useful, but the stored citation text should be reviewed for truncation and partial party-style capture. The next fix should be deterministic extraction improvements, not more broad AI labeling.

## 9. What The System Does Well

1. It has a large, populated canonical corpus.
2. It has a dense citation graph with over 217k resolved citation occurrences.
3. It has broad tag coverage for issues, statutes, legal areas, proceedings, and other legal dimensions.
4. It exposes strong citation-map utilities for navigation, evidence review, and trend analysis.
5. It has a working deterministic QA layer and a budget-bounded external audit process.

## 10. Current Gaps

1. Citation extraction still needs better handling of truncated party-style and reporter-style citations.
2. The cheap OpenAI audit model is useful as a reviewer, but not as a primary validator.
3. Some advanced roadmap items remain not fully implemented end to end, especially around deeper context extraction and explainability UX.
4. Performance baselines and nightly data-quality gates are still thinner than the breadth of the product surface would ideally require.

## 11. Recommended Next Moves

1. Fix the deterministic citation extractor for the real false-negative patterns found in the 1000-case audit.
2. Convert the 1000-case audit findings into a filtered issue shortlist so duplicate-only flags are excluded.
3. Add a regression fixture set for partial reporter citations and party-style citations.
4. Keep the cheap OpenAI pass as an external audit layer only, with a hard budget cap and failure tolerance.
5. Expand performance and data-quality gates once the citation extraction defects are reduced.

## 12. Key Files To Know

1. [backend/database.py](backend/database.py)
2. [backend/citations.py](backend/citations.py)
3. [backend/citation_map.py](backend/citation_map.py)
4. [backend/routes.py](backend/routes.py)
5. [backend/models.py](backend/models.py)
6. [scripts/verify_citation_extraction.py](scripts/verify_citation_extraction.py)
7. [tests/test_verify_citation_extraction.py](tests/test_verify_citation_extraction.py)
8. [ROADMAP.md](ROADMAP.md)
9. [README.md](README.md)

## 13. Bottom Line

This system is already a substantial legal citation analysis platform, not just a search tool. The canonical store is populated, the citation graph is dense, and the citation-map surface is broad. The main immediate quality issue is citation extraction fidelity for certain citation patterns, which the 1000-case external audit helped reveal.

Use the deterministic extractor and the citation graph as the core. Use the cheap OpenAI audit only as a triage layer. Fix extraction defects deterministically before widening any AI-assisted automation.