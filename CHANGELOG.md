# Change History

Document role: milestone and implementation delta log.
For current operating picture, pair this with `SYSTEM_OVERVIEW.txt` and `OVERNIGHT.md`.

## Unreleased - Optimized V2 text-only enrichment review

- Completed the optimized non-SCC V2 run: 50,327 records processed, 43,598
	completed, 6,729 excluded for missing parseable allowed hosts, and 0
	quarantined.
- Compared the completed cohort with the compact baseline: chunks increased
	12%, case citations 30%, statute references 65%, and V3 tag occurrences
	23.1x.
- Read-only evidence auditing found no malformed citation/statute offsets and
	no V3 tag rows missing offsets.
- Recorded the remaining boundary: citation rows are extraction-only and remain
	explicitly unresolved without chunk association until the separate local
	target-resolution pass; HTML coverage was intentionally not expanded by this
	run.
- Verification: focused V2/citation suite passed 116 tests; generated API,
	schema, and script references are current.

## 2026-09-03 - Thematic intelligence in Data Explorer

- Added the ninth Data Explorer tab, Legal Themes & Statutes, with live theme
	definitions and statute-tag affinity exploration for provisions such as
	`34(1)(f)`.
- Added inline reader Precedents support backed by composite thematic clustering
	across stored tags, statute references, and case citations.
- Verification: contextual intelligence tests passed (7), feature/API tests
	passed (55), and the full suite passed (311).

## Unreleased - Standalone Live Analysis prototype

- Added an ephemeral `.docx` analysis surface at `/live-analysis` with in-memory
	paragraph offsets, deterministic case-citation and statute-reference evidence,
	and optional read-only local case resolution.
- Added upload validation, focused API/service tests, and navigation links while
	keeping analysis results out of the canonical database and ingestion pipeline.
- Added text-based PDF support with page-aware evidence and `pypdf`; scanned-PDF
	OCR remains outside the prototype scope.
- Optimized optional local citation resolution into one batched database read and
	removed the external CanLII fallback from the Live Analysis path.
- Split citation resolution into a distinct second request and broadened local
	matching to named and short-form references using case metadata.
- Verification: `81 passed` for the focused Live Analysis/citation test slice;
	touched modules compile cleanly.

## 2026-08-19 - Docket Number Field Backfill and FC Activity Cross-Reference

- Added dedicated `docket_number` column to the canonical `cases` table to
	capture Federal Court docket and file identifiers separately from legal
	citation semantics.
- Backfilled docket numbers across 35,902 decisions by scanning title, summary,
	and first chunk text for T-XXXX and IMM-XXXX-YY patterns: 35,451 cases
	populated (98.74% coverage), with 22,140 IMM-pattern and 13,308 T-pattern
	docket numbers recovered.
- Updated schema in `backend/database.py`, `backend/models.py`,
	`backend/ingestion.py`, and `backend/routes.py` to persist the field through
	create and merge workflows.
- Cross-referenced canonical docket_number values against FC Activity dataset
	citations: 18,911 exact matches (53.85% of canonical dockets with activity
	correlation), confirming reliable linkage for immigration cases up to 2022.
- Documented root causes of 16,204 non-matches: 13,308 T-pattern cases
	(non-immigration; activity dataset is 100% immigration-focused), 2,838
	IMM-cases dated >2022 (activity dataset ends 2022), and 55 coverage gaps
	within date range.
- Verified backward compatibility: all Federal Court import tests pass (9
	passed), ingest/metadata tests pass (10 passed).
- Updated `AI_HANDOFF.md` with docket field documentation and coverage metrics.

## 2026-08-17 - Six-tab intelligence interface

- Restored the primary one-page product shell with About, Case Search,
	Citation Intelligence, Judge Outcomes, Judge Profile, and Data Explorer tabs.
- Restored database-backed About statistics and Citation Intelligence API
	surfaces without changing citation extraction or resolution behavior.
- Added Judge Profile list/detail APIs using the existing canonical profile
	schema and preserved compatibility redirects for `/about`,
	`/citation-intelligence`, and `/judges`.

Note: entries on the same date may be grouped by feature theme rather than
strict execution order.

## 2026-08-12 - Advanced search, citation resolution, and isolated LotD import

- Promoted `/data-explorer` into the main research-facing UI with three tabs:
	advanced search, judge outcomes, and case data explorer.
- Added advanced search filters for cited authority, government outcome,
	decision outcome, judge, court, year, and minister/government party.
- Added minister dropdown sourcing through `/analytics/search/ministers` and
	sort controls for relevance, newest, oldest, and minister A-Z.
- Added a full-decision modal reader backed by stored citation rows rather than
	live re-extraction, preserving highlight spans while reducing open time for
	heavily cited decisions.
- Added per-case citation metrics in search results and reader payloads:
	total citation mentions, unique cited authorities, and linked target cases.
- Added local batch target-resolution scripts:
	`scripts/resolve_citation_targets.py` and
	`scripts/resolve_short_citation_targets.py`.
- Completed local target resolution for the current citation inventory:
	`1,492,628` citation rows total, `760,197` linked rows, and `31,944` unique
	linked target cases.
- Added isolated side-project dataset utility under
	`side_projects/luck_of_the_draw_iii/`, including cached Hugging Face parquet
	download, import into schema `lotd`, and workbook export.
- Built the LotD dataset successfully: `218,639` cases, `2,610,399` dockets,
	and workbook output at
	`side_projects/luck_of_the_draw_iii/output/luck_of_the_draw_iii.xlsx`.
- Verification performed through live database counts, focused API timing, and
	targeted importer validation rather than a new full `pytest -q` baseline.

## 2026-08-10 - Workflow consolidation and explainer alignment

- Declared Citation Pass as the canonical day-to-day workflow for current
	extraction stabilization work.
- Updated `README.md` with a single operating sequence (run API, review
	`/citation-pass`, fix deterministic extraction, validate, then push).
- Updated `DOCS_INDEX.md` so explainer-document authority and update order are
	explicit for patch cycles.
- Updated `AI_HANDOFF.md` to foreground the same primary workflow and reduce
	context switching across parallel notes.
- Repository checkpoint prepared for push from `main` to keep all work up to
	this point synchronized on GitHub.

## 2026-08-10 - Legacy system folder consolidation

- Added a top-level `legacy/` archive zone to reduce root-level clutter and
	make active-vs-legacy boundaries explicit.
- Moved `Case Law Bookmarks - August 2026.docx` into
	`legacy/artifacts/Case Law Bookmarks - August 2026.docx`.
- Added `legacy/README.md` with rules for what belongs in legacy paths.
- Updated `README.md` and `DOCS_INDEX.md` to point active work to Citation Pass
	and classify legacy paths as reference-only.

## 2026-08-10 - Legacy helper script archive

- Moved non-runtime, non-test-bound helper scripts from `scripts/` to
	`legacy/scripts/` to keep the active scripts surface focused.
- Added `legacy/scripts/README.md` documenting archived script intent and scope.

## 2026-08-07 - Deterministic layered extraction review

- Hardened the case-only citation layer for full case anchors, grounded
	short-form aliases, complete parenthetical spans, and exact Unicode-safe
	source offsets.
- Added independent deterministic statute/instrument extraction through
	`extract_statute_reference_matches()`; statute rows no longer depend on case
	extraction or participate in case-layer overlap selection.
- Expanded law coverage for Canadian Acts, Codes, Regulations, Rules, Orders,
	SOR/SI citations, international instruments, plural provisions, and bounded
	short-form section/article propagation from a named authority.
- Added precision guards against ordinary prose such as `In order` and bare
	judgment paragraph numbers inheriting a statute anchor.
- Added a deterministic metadata span layer backed by the Federal Court
	metadata extractor. Canonical text-derived fields retain exact offsets,
	confidence, and source provenance.
- Extended `GET /cases/{case_id}/citation-pass` with separate
	`live_extracted`, `live_statutes`, and `live_metadata` arrays and independent
	counts. The review UI renders case citations in orange, laws in green, and
	metadata in blue without reparsing backend spans.
- Added focused extractor and API regressions. Verified live code-point span
	integrity with zero errors: Febles has `168` case citations and `442` law
	references; Hasani has `48` case citations, `62` law references, and `10`
	metadata fields.
- Focused validation passes: `6` statute-layer tests, `1` citation-pass API
	test, and `1` metadata-layer test. The full suite currently stops during test
	collection on a pre-existing syntax error in
	`tests/test_fc_document_scraper.py:58`; no full-suite pass count is claimed.
- No AI/API extraction calls or broad cohort reprocessing were performed.

## 2026-08-02 - Direct A2AJ FC PDF ingestion with metadata tagging

- Added direct Federal Court ingestion mode in `fc_ingest` (`--a2aj-direct`)
	that bypasses discovery windows and pulls known FC item URLs from the
	A2AJ-backed canonical corpus.
- Added FC URL normalization so `item`, `document`, and PDF links resolve to a
	canonical Lexum item URL before ingestion.
- Extended SQLite staging `fc_pdfs` records to store searchable metadata beside
	the PDF blob: case title, decision date, neutral citation, docket, and
	`metadata_json`.
- Added in-place schema upgrade logic for existing `fc_pdfs` tables so old
	databases gain new metadata columns automatically.
- Added regression tests for direct mode behavior and PDF metadata persistence;
	focused FC ingest test baseline is now `12 passed`.

## 2026-08-03 - Citation intelligence expansion

- Added a global citation surprise feed at `/citation-map/surprises` with
	optional tag and year filters, balancing local citation intensity against
	global authority ubiquity.
- Added doctrine-shift analytics at `/citation-map/issues/shifts` to surface
	likely authority replacement patterns within issue/statute/legal-area slices.
- Added CSV exports for high-value analytics surfaces:
	`/citation-map/cases/{case_id}/authority-signals.csv`,
	`/citation-map/surprises.csv`,
	`/citation-map/authorities/landmarks.csv`, and
	`/citation-map/issues/shifts.csv`.
- Added route-level regression tests for new endpoint bounds, validation rules,
	and export headers; full suite baseline is now `110 passed`.

## 2026-08-03 - Citation hidden paths and inheritance chains

- Added hidden-bridge analytics at `/citation-map/paths/hidden` to rank
	intermediate cases that repeatedly connect source-target citation paths.
- Added authority inheritance chain analytics at
	`/citation-map/authorities/{case_id}/inheritance` to trace downstream
	citation adoption depth and edge strength.
- Added CSV exports for both new surfaces:
	`/citation-map/paths/hidden.csv` and
	`/citation-map/authorities/{case_id}/inheritance.csv`.
- Expanded citation route tests and raised full regression baseline to
	`111 passed`.

## 2026-08-03 - Position profiles, completion suggestions, and shift dashboard

- Added citation position profiles at
	`/citation-map/cases/{case_id}/position-profiles` with early-vs-late
	citation placement features and CSV export.
- Added citation completion suggestions at
	`/citation-map/cases/{case_id}/completion-suggestions` to recommend likely
	missing authorities, plus CSV export.
- Added jurisprudential shift dashboard at `/citation-map/issues/dashboard`
	combining replacement candidates, lifecycle-stage signals, and surprise
	authorities into one issue-level intelligence payload, plus CSV export.
- Expanded route-level test coverage and raised full regression baseline to
	`113 passed`.

## 2026-08-03 - Missing authorities, lifecycle, and court flow

- Added missing-authority detection at
	`/citation-map/cases/{case_id}/missing-authorities` to surface authorities
	peer-similar cases cite that the focus case does not.
- Added authority lifecycle tracking at
	`/citation-map/authorities/lifecycle` with stage classification
	(emerging, dominant, declining, foundational, transitional).
- Added cross-court authority flow analytics at `/citation-map/courts/flow`
	to quantify citation movement between courts.
- Added CSV exports for all three new analytics surfaces.
- Saved the user master roadmap into `MASTER_IDEAS.md` for future staged
	implementation planning.
- Expanded citation route tests and raised full regression baseline to
	`112 passed`.

## 2026-08-03 - Case reader and branch-focused exploration

- Added `/case-reader`, a searchable, responsive decision reader backed by each
	case's canonical stored full text, with source and citation-map deep links.
- Changed map, search, comparison, and evidence surfaces to show case names as
	the primary visual label and neutral citations as secondary metadata.
- Kept first-level authorities radial while placing expanded descendants near
	their clicked parent and bringing off-screen branches into the map viewport.
- Added opt-in HTTP Basic authentication for temporary private deployments;
	local access remains unchanged unless private-access environment variables are
	set.

## 2026-08-03 - Case Explorer and Issue Map workbench

- Added a dual-mode citation workbench with focused case exploration and broad
	issue, statute, and legal-area maps.
- Added force-directed issue graphs with 20-150 case controls, all internal
	citation links, and node sizes scaled by distinct citing-case counts.
- Added two/three-authority common-citer comparison, exact chunk-backed citation
	contexts with CSV export, evidence-bearing legal tags, and branch expansion.
- Kept dynamic IRPA section tags visibly identified as machine-extracted
	evidence candidates rather than authoritative legal classifications.
- Validated dense desktop and narrow-screen rendering without page overflow.

## 2026-08-02 - Citation map baseline

- Added whole-corpus citation analytics for graph summary, leading authorities,
	weighted case neighborhoods, co-cited authorities, and explainable
	shared-authority similarity.
- Aggregated repeated citation occurrences into weighted case-to-case edges
	while retaining the underlying occurrence rows as evidence.
- Added typed read-only APIs under `/citation-map/*` with bounded result sizes.
- Redesigned `/citation-map` around arbitrary case search and a focused radial
	map of the five most influential authorities cited by the selected case.
- Added clickable node inspection, authority mention counts, one-click map
	recentering, related cases with shared-authority explanations, and co-citation
	drill-down.
- Excluded document self-citations from focused authority maps and verified
	responsive rendering without horizontal overflow in narrow and desktop views.
- Validated all analytics queries against the live `35,902`-case PostgreSQL
	corpus without starting embeddings or modifying Hugging Face staging.
- Full regression baseline: `104 passed`.

## 2026-08-02 - First overnight result and resume-path repair

- Executed overnight run `20260801-234642` with `--continue-on-error`.
- Completed `ca_legal_v2` tagging for all `35,902` cases, creating `770,357`
	tags in approximately 59 minutes.
- Chunked all `35,519` previously unchunked text-bearing cases into `165,600`
	new chunks in approximately 87 seconds. PostgreSQL now contains `168,282`
	chunks across all `35,902` cases.
- Verified the separate reference library without downloads (`18` skipped as
	checksum-valid). The FC portal completed with zero new rows.
- Diagnosed citation and local-embedding failures as direct-script Python import
	path errors. Changed both overnight commands to module-mode invocation and
	added regression coverage.
- Changed an empty prototype procedural-history candidate set into a successful
	no-op rather than a failed job.
- Isolated official FC discovery failures by monthly window while retaining a
	non-zero exit when every source window is unavailable.
- Verified the existing failed-job run can resume without repeating completed
	tagging or chunking. Local BGE-M3 dry run sees pending chunks.
- Current remaining backlog: zero extracted citations and zero local BGE-M3
	vectors across `168,282` chunks.
- Full regression baseline after repair: `98 passed`.

## 2026-08-01 - Resumable overnight enrichment and local embeddings

- Added `scripts/run_overnight.py`, a sequential overnight orchestrator with an
	exclusive process lock, atomic JSON state, timestamped run directories,
	per-job logs, preflight checks, failure policy, and completed-job skipping on
	resume.
- Added official Federal Court-only acquisition jobs for IMM decision discovery,
	portal records, and procedural histories. CanLII and paid hosted-AI jobs are
	intentionally excluded from the overnight profiles.
- Added `scripts/chunk_cases.py` to create 6,000-character chunks with
	600-character overlap for canonical cases that do not already own chunks.
	Chunking uses keyset pagination and commits every 50 cases without changing
	`processing_status` or calling an AI service.
- Added resumable local BGE-M3 embedding through `scripts/embed_local_chunks.py`.
	It creates 1,024-dimensional vectors in `case_chunk_embeddings`, runs on CPU
	by default, commits every four chunks, and makes no OpenAI or Copilot calls.
- Hardened citation backfill with keyset pagination. Chunk citation extraction
	now processes all chunks for a case together so a later partial batch cannot
	erase earlier citations.
- Fixed Federal Court monthly ingestion windows across December/year boundaries.
- Added a separate 18-document reference library with strict content validation,
	source-native PDF/HTML storage, checksums, atomic writes, resume, and inventory.
- Advanced deterministic legal tagging to `ca_legal_v2`, including deeper PRRA,
	CBSA removal, inadmissibility, detention, and enforcement concepts.
- Verified pre-run PostgreSQL state: `35,902` cases, `35,498` raw cases, `2,682`
	chunks across `383` cases, `35,519` text-bearing cases pending chunking, zero
	local BGE-M3 embeddings, and zero `ca_legal_v2` completion records.
- Verified source state: `17,240` FC procedural histories, `830` discovered
	official FC decision IDs, and `18/18` reference documents downloaded.
- Added `OVERNIGHT.md` with launch, pull-only, preflight, resume, lock, state, and
	log operations. Full regression baseline: `94 passed`; workspace diagnostics
	are clean.

## 2026-08-01 - Versioned Canadian immigration and CBSA legal tags

- Added deterministic, evidence-bearing `ca_legal_v1` tagging across immigration,
	refugee protection, IRPA/IRPR, international law, countries, organizations,
	judicial review, remedies, and general legal concepts.
- Added first-class CBSA/MPSEP dimensions for section 44 reports, inadmissibility,
	detention, removal orders, stays/deferrals, warrants, and program consequences.
- Added indexed `case_tags` and resumable `case_tagging_status` tables in migration
	`0010_case_legal_tags` without changing source records or existing embeddings.
- Added `scripts/tag_cases.py` with dry-run, batching, limits, court/source filters,
	taxonomy-aware resume, and explicit retag support.
- Added `LEGAL_TAGGING.md` with authoritative source hierarchy, secondary reference
	works, interpretation cautions, taxonomy coverage, and operational commands.
- Verified focused taxonomy coverage (`5 passed`) and a five-case PostgreSQL dry-run
	(`38` preview tags).

## 2026-08-01 - Multi-court Hugging Face staging and project health review

- Downloaded and verified `61,217` A2AJ decisions in a local SQLite staging archive:
	- FC: `35,814`
	- RPD: `6,729`
	- FCA: `7,785`
	- SCC: `10,889`
- Preserved complete source rows in `raw_payload` plus query-friendly normalized columns and metadata-only JSON.
- Fixed bilingual citation normalization for `cases_cited_en/fr` and `cases_citing_en/fr`.
- Added stable source keys and compatibility matching so ingestion reruns do not duplicate pre-key staging rows.
- Added a bounded `repair_staging` command to backfill normalized citation columns and source keys after active data pulls finish.
- Added unique case/model embedding storage and bounded-memory embedding batches that skip completed vectors.
- Added `scripts/import_canlaw_staging.py`, a streaming, resumable, dry-run-capable bridge into the primary PostgreSQL ingestion API.
- Expanded `scripts/ingest_a2aj_parquet.py` to preserve all non-text A2AJ source metadata, including bilingual fields.
- Added Hugging Face/Xet dependencies, ignored the multi-gigabyte staging database, and removed duplicate dependency declarations.
- Added focused regression tests for multi-court ingestion, rich metadata, idempotency, embeddings, and the staging bridge.
- Verified the complete project suite: `60 passed`.
- Operational safety: left the active FC procedural-history pull running and did not execute the PostgreSQL bridge.

## 2026-07-31 - Prototype explorer, citation map, and topic-keyword visibility

- Added prototype cohort explorer endpoints:
	- `GET /prototype`
	- `GET /prototype/summary`
	- `GET /prototype/cases`
	- `GET /prototype/graph`
- Added an interactive citation map in the prototype UI:
	- topic-aware graph filtering
	- node-cap control for performance
	- degree-based node sizing and topic color encoding
	- hover metadata and node-click table filtering
- Added robust prototype pagination behavior:
	- out-of-range page requests now clamp to page `1` when filtered totals are non-zero
- Added cohort topic tagging workflow:
	- `scripts/tag_prototype_topics.py`
	- executed successfully for full cohort (`334` scanned/updated)
- Added prototype graph and pagination regression tests in `tests/test_api.py`.
- Updated health baseline:
	- `pytest -q` => `52 passed`

## 2026-07-31 - Merged local and A2AJ citation graph

- Extended the citation graph to carry a `provenance` flag so local regex extraction and A2AJ-derived edges can coexist in the unified `citations` table.
- Added A2AJ provenance tables and mappings:
	- `a2aj_cases`
	- `a2aj_citation_edges`
	- `a2aj_case_map`
- Added `scripts/ingest_a2aj_citation_network.py` to read the A2AJ parquet source, populate A2AJ citation tables, build the local case map, and convert A2AJ edges into local citations.
- Added FastAPI endpoints for A2AJ cases, A2AJ edges, A2AJ mapping, and A2AJ graph conversion.
- Kept local citation extraction and citation-metric recomputation in `backend/citations.py` and `scripts/extract_citation_network.py`.

## 2026-07-31 - Citation network scaffold added

- Added citation-graph ORM models and migration for `citations` and `citation_metrics`.
- Added reusable citation extraction helpers in `backend/citations.py` with Canadian neutral, case, and statute citation regexes.
- Added read-only backend endpoints for outgoing, incoming, and passage-level citations plus per-case citation metrics.
- Added `scripts/extract_citation_network.py` to backfill citations from cases or chunks and recompute graph metrics.
- Added a small citation-in-degree tie-breaker to case search so heavily cited cases can surface higher without changing the reported similarity score.

## 2026-07-31 - Immigration core dataset curation added

- Added `scripts/curate_a2aj_immigration_cases.py` to build a balanced immigration-focused seed set from the full A2AJ Federal Court parquet source.
- The selector now groups cases by immigration-relevant buckets:
	- refugee protection / non-refoulement
	- judicial review / procedure
	- removal / detention / inadmissibility
	- family status / citizenship / H&C
	- agency review and enforcement (`IMM`, `IRCC`, `CBSA`, `Minister`, `MPSEP`)
- Added balanced sampling controls:
	- default limit of 60 cases
	- per-bucket selection cap before fallback filling
- Stored the resulting records as `source_type="a2aj_immigration_core"` with bucket metadata in `metadata_json`.
- Added tests covering immigration signal scoring and bucket-balanced selection.

## 2026-07-31 - Metadata search UX overhaul, broader filters, and project health pass

- Expanded `CaseSearchRequest` metadata filters in `backend/models.py` with:
	- `title_contains`
	- `source_name_contains`, `source_url_contains`, `source_id_contains`
	- `citation_contains`, `secondary_citation_contains`
	- `dataset_version_contains`, `upstream_license_contains`
	- `cases_cited_contains`, `cases_citing_contains`
	- `language`, `processing_status`
	- `scraped_from`, `scraped_to`
	- `citing_cases_min`, `citing_cases_max`
- Extended `_apply_case_filters` in `backend/routes.py` so all of the above fields are enforced in SQL filtering.
- Added shared request validation guardrails for:
	- reversed decision date ranges
	- reversed scraped date ranges
	- invalid citing count bounds (`min > max`)
- Reworked the `/testing` UI into a metadata-first legal search interface:
	- core fields for document text, identifiers, citation, court, source, and language
	- advanced metadata panel for noteup/citation-network, scrape windows, status, and citing-count bounds
	- optional year toggle filter
	- agency presets (`Minister`, `IRCC`, `CBSA`, `All agencies`)
	- active-filter summary line and `Enter` key to run search
	- JSON payload moved to synchronized preview/advanced override mode
- Applied CanLII-style wording and flow cues (`Document text query`, identifier labels, `Start a search`, `Reset your search`).
- Confirmed runtime API behavior via live smoke check on `POST /search` (status `200` with pagination headers).
- Project health pass completed:
	- `python -m py_compile backend/routes.py backend/models.py tests/test_api.py`
	- `pytest -q` => `38 passed`
	- `get_errors` => no workspace diagnostics
- Added and updated regression coverage in `tests/test_api.py` for the new filter fields, UI labels, and validation behavior.

## 2026-07-31 - Retrieval foundation extended

- Added Alembic configuration and an initial migration for controlled schema evolution.
- Added jurisdiction, citation, full text, issues, flexible metadata, source URL, and source name fields.
- Added B-tree metadata indexes and an HNSW cosine vector index.
- Added search filters for court, jurisdiction, and date ranges.
- Added pagination and normalized similarity scores to search responses.
- Added four focused API tests covering ingestion, filtered search, date validation, and missing OpenAI configuration.

## 2026-07-31 - FC import adapter and low-noise evaluation controls

- Added `scripts/import_fc_decisions.py` to import Federal Court records from `.json`, `.jsonl`, or `.csv` through the existing `/ingest` API.
- Added field normalization for common FC dataset keys (`style_of_cause`, `neutral_citation`, `decision_date`, `docket_number`, `full_text`).
- Added lightweight deduplication and record-skipping rules for missing required content/date during batch import.
- Added evaluator controls in `scripts/evaluate_retrieval.py`:
	- `--limit` to run a bounded fixture subset for faster iteration.
	- `--verbose` to opt in to per-query output instead of printing it by default.
- Added unit tests for importer mapping/deduplication and evaluator summary/gate behavior.

## 2026-07-31 - Federal Court portal collector (stage 1 and optional stage 2)

- Added `scripts/fc_portal_collector.py` for polite FC portal collection with:
	- prefix-based paging (`IMM`, `T`, `A`, etc.)
	- retry/backoff and configurable request pacing
	- checkpoint/resume support
	- incremental JSONL output
	- deduplication across runs from existing output
	- optional detail-page expansion (`--expand-details`)
- Added parser tests for listing and detail extraction in `tests/test_fc_portal_collector.py`.
- Added `beautifulsoup4` dependency for robust HTML parsing.
- Added optional importer-contract emission (`--emit-import-ready`) that writes staged rows mapped to `style_of_cause`, `neutral_citation`, `decision_date`, `full_text`, `docket_number`, and `url`.
- Added incremental prefix-rotation mode (`--incremental-prefix-window`, checkpoint-backed `rotation_run`) for scheduled runs without crawling all prefixes each execution.
- Added importer normalization for staged collector output so `scripts/import_fc_decisions.py` ignores listing/detail rows and consumes `stage=import_ready` rows directly.

## 2026-07-31 - Multi-site case existence verifier (run-later ready)

- Added `scripts/verify_fc_case_existence.py` to verify whether docket/court numbers exist across configured sources.
- Supports `.txt`, `.json`, and `.jsonl` input formats and writes JSONL verification output.
- Added provider framework with:
	- `courtfiles` (definitive check via official `/CourtFilesAndDecisions/proceedingQueriesCourtNumberList` endpoint)
	- `decisions` (signal-only probe to decisions site search endpoint)
- Added focused unit tests in `tests/test_verify_fc_case_existence.py`.

## 2026-07-31 - Synthetic dataset imported

- Added a reusable importer for 20 clearly labeled synthetic Federal Court non-refoulement cases.
- Imported the dataset through the live `/ingest` API, generating and storing OpenAI embeddings for each record.
- Confirmed the database contains 20 synthetic cases plus the earlier demo case.
- Verified broad semantic search and jurisdiction-filtered search against the dataset.
- Made the importer skip existing citations so it can be rerun safely.

## 2026-07-31 - Raw A2AJ ingestion foundation

- Made summaries and embeddings optional so source documents can be preserved before enrichment.
- Added A2AJ provenance, licensing, source, hash, processing-status, and citation-network fields.
- Added migration `0002_raw_ingestion` and applied it to the local database.
- Added `scripts/ingest_a2aj_parquet.py` with dry-run, limit, Federal Court filtering, and duplicate detection.
- Added a regression test proving raw ingestion does not call OpenAI.
- Installed `pyarrow` for Parquet reading; no A2AJ data has been imported yet.

## 2026-07-31 - First A2AJ embedding test

- Added `case_chunks` storage and migration `0004_case_chunks`.
- Chunked the 25 A2AJ pilot cases into 82 overlapping chunks.
- Embedded the chunks with `text-embedding-3-small` at an estimated cost of $0.0021.
- Stored chunk embeddings and case-level average vectors, marking all 25 A2AJ records as `embedded`.
- Verified real A2AJ records appear in semantic search.
- Observed that synthetic records still rank highly, confirming the need for curated relevance benchmarks and chunk-level retrieval evaluation.

## 2026-07-31 - Curated evaluation and chunk search

- Added a transparent keyword-scored selector for 25 A2AJ refugee-risk cases.
- Imported the curated cases separately as `a2aj_curated` raw records, preserving the original pilot set.
- Embedded 471 curated text chunks at an estimated cost of $0.0138.
- Added `POST /search/chunks` to return source passages with parent-case citations.
- Verified chunk retrieval returns relevant passages about torture evidence, state protection, and refoulement.

## 2026-07-31 - A2AJ source and retrieval state

- Downloaded the A2AJ Federal Court Parquet source locally at `data/raw/a2aj/FC/train.parquet`.
- Verified the file contains 35,814 records and completed a 25-record dry run with zero invalid records or duplicates.
- Imported 25 A2AJ pilot records as raw full-text records, then chunked and embedded them into 82 chunks.
- Added `GET /cases/{id}` for direct case retrieval with a clear `404` response for missing IDs.
- Added migration `0003_backfill_processing_status` so existing vector records are labeled `embedded` instead of `raw`.

## 2026-07-31 - Paused evaluation checkpoint

Current database state:

- 21 synthetic/demo prototype cases, embedded.
- 25 A2AJ pilot cases, embedded in 82 chunks.
- 25 curated A2AJ refugee-risk evaluation cases, embedded in 471 chunks.
- 71 total case records and 553 total stored chunks.
- Alembic revision `0004_case_chunks` is at head.
- Seven automated tests pass.

The project is intentionally paused before larger ingestion. The current retrieval result is a technical success, not yet a validated legal-relevance benchmark: synthetic cases can rank highly, and chunk results can repeat the same parent case. No summaries or RAG generation have been added.

Recommended next path:

1. Add a relevance evaluation fixture with research questions and expected case citations.
2. Group chunk results by parent case and return the best passages per case.
3. Add source-type filters so evaluation can exclude synthetic records.
4. Review curated results manually and adjust selection rules.
5. Run the benchmark before importing more records or generating summaries.
6. Add RAG only after retrieval quality is measurable.

## 2026-07-31 - Long-term guidance added

- Added `GUIDANCE.md` as the project north star for litigation-focused ingestion, retrieval, RAG, data modeling, operations, and future product decisions.
- Kept current implementation notes, historical changes, and future direction in separate documents.

## Earlier project history - Accounts, setup, and resolution

This section records the supplied project history without storing passwords, API keys, or other secret values.

### Phase 1 - Accounts and API setup

- An OpenAI account was created.
- OpenAI billing was funded with $25 in credits.
- A new OpenAI API key was generated, verified in the OpenAI dashboard, and saved locally in the project environment file.
- Secret values are intentionally omitted from this history.

### Phase 2 - Local development environment

- Python 3.12 and pip were installed and verified.
- The project was created at `C:\Users\danny\OneDrive\Desktop\AI CaseLibrary`.
- A project virtual environment was created in `venv`.
- PowerShell activation required:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

- Backend dependencies were installed, including FastAPI, Uvicorn, SQLAlchemy, psycopg2, pgvector, Pydantic, and the OpenAI client.

### Phase 3 - PostgreSQL and pgvector

- PostgreSQL and pgAdmin were installed.
- pgvector was enabled and verified.
- The working local database is `caselibrary`.
- The `cases` table contains `id`, `title`, `court`, `date`, `summary`, `embedding`, and `created_at`.

### Phase 4 - FastAPI backend

- `main.py` provides the FastAPI application, startup hook, router registration, and health check.
- `database.py` provides SQLAlchemy configuration, sessions, the ORM `Case` model, pgvector setup, and table creation.
- `models.py` provides the Pydantic request and response models.
- `routes.py` provides embedding calls, ingestion, and vector similarity search.
- The current implementation keeps these responsibilities in the four modules above rather than separate `schemas.py`, `openai_client.py`, or `search.py` files.

### Phase 5 - Project-local environment

- A local `.env` file was created under `backend/.env`.
- It contains local OpenAI and PostgreSQL configuration, but its secret values are not recorded here.
- The application loads `.env` from the project root or `backend/.env` using `python-dotenv`.
- It supports either `DATABASE_URL` or separate `POSTGRES_*` variables.

### Phase 6 - Debugging and resolution

- Initial startup failed because the environment file was missing or empty and the fallback PostgreSQL credentials were incorrect.
- PostgreSQL was reachable, but authentication initially failed for the `postgres` user.
- After the correct local environment values were saved, the remaining error showed that `ai_caselibrary` did not exist.
- The configuration was corrected to use the existing `caselibrary` database.
- Database initialization then succeeded, including pgvector setup and table creation.
- Uvicorn completed startup with `Application startup complete.`

### Phase 7 - Current system state

- The health endpoint has been verified successfully.
- The `/ingest` and `/search` routes are registered and ready for live OpenAI testing.
- API documentation is available at `/docs`.
- Full live ingestion and semantic-search requests still require a valid OpenAI API key and should be tested with non-sensitive sample cases.

## 2026-07-31 - Backend foundation completed

### Added

- FastAPI application wiring in `backend/main.py`.
- SQLAlchemy PostgreSQL engine and session management.
- ORM `Case` model with title, court, date, summary, timestamp, and a 1536-dimensional pgvector embedding.
- Automatic `vector` extension setup and table creation at application startup.
- Pydantic request and response schemas.
- `POST /ingest` for OpenAI summary embeddings and case storage.
- `POST /search` for OpenAI query embeddings and cosine similarity search.
- Environment loading from the project root `.env` or `backend/.env`.
- Support for either `DATABASE_URL` or separate `POSTGRES_*` settings.
- Safe SQLAlchemy URL construction for passwords containing special characters.

### Configuration fixes

- Identified that PostgreSQL was running on port 5432.
- Corrected the database name from `ai_caselibrary` to `caselibrary`.
- Confirmed PostgreSQL authentication and pgvector initialization.

### Verification

- Backend modules compile successfully.
- Pylance reports no errors in the database module.
- Database initialization succeeded.
- FastAPI startup completed successfully.
- `GET /` returned `AI CaseLibrary backend is running`.

### Remaining work

- Add Alembic migrations.
- Add automated API and database tests.
- Test `/ingest` and `/search` with a valid OpenAI API key.
- Add the AI chat/RAG endpoint.
- Add authentication, CORS configuration, logging, and production deployment settings.

## 2026-07-31 - Code review and pause checkpoint

- Reviewed backend, migrations, importers, tests, and live database state.
- Added source-type filtering to case and chunk search so synthetic data can be excluded from evaluation.
- Made ingestion derive `processing_status` from actual behavior instead of trusting caller input.
- Made the server compute full-text hashes instead of accepting a potentially false client-provided hash.
- Added regression coverage for source filtering, hash integrity, and derived processing status; the suite now has 8 passing tests.
- Added `AI_HANDOFF.md`, a detailed technical continuation brief for another AI or developer.
- Confirmed the paused database state: 71 cases, 553 chunks, migration `0004_case_chunks` at head.
- Documented remaining risks: unbenchmarked retrieval quality, repeated parent cases in chunk results, no CanLII adapter, no canonical multi-source table, and no RAG layer.

The recommended next step is retrieval evaluation with expected citations, not full-corpus ingestion or RAG generation.
