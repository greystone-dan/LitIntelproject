# Testing Matrix

Last reviewed: 2026-09-01

This matrix maps current automated coverage to active system surfaces. It distinguishes deterministic unit-style tests from route, source-pipeline, and operational tests. It does not claim browser end-to-end coverage where none exists.

## Current Baseline

Latest broad run: `268 passed, 2 failed`.

The two failures are stale expectation mismatches, not known active-path defects:

1. A test expects IRPA statute data in `citations`, while the current architecture correctly stores it in `statute_references`.
2. A test expects retired wording from the standalone reader instead of the active inline research reader.

Focused active UI/citation regression checks most recently passed with `18 passed`. Always rerun the relevant slice after a change; do not treat this historical count as a substitute for current validation.

## Coverage Matrix

| System surface | Primary tests | Coverage focus | Main gaps |
| --- | --- | --- | --- |
| Core API, ingest, search, reader payloads | `test_api.py` | Request validation, filtering, ranking, reader/citation-pass responses, metadata compatibility | No live PostgreSQL/pgvector performance suite |
| Active Data Explorer UI contract | `test_feature_tabs.py` | Tab presence, hidden route behavior, live stats contract, search controls, panel markup | No browser interaction/screenshot test |
| Citation extraction and resolution | `test_citations.py`, `test_citation_pipeline.py` | Case forms, aliases, pinpoints, offsets, statutes/instruments, rebuild semantics, graph bounds | Real-corpus precision/recall remains sampled rather than continuous |
| Citation audit tooling | `test_verify_citation_extraction.py`, `test_build_fc_citation_seed.py`, `test_map_fc_seed_to_local_cases.py` | Fixtures, spans, audit reports, seed normalization/mapping | External model audit calls are not run in normal tests |
| Metadata/outcomes/dockets | `test_metadata.py`, `test_api.py`, `test_fc_document_scraper.py` | Exact spans, outcome derivation, reader fields, scraper metadata | Limited real-world multilingual/format gold coverage |
| Legal tags | `test_legal_tagger.py` | Immigration/refugee, CBSA, IRPA/IRPR, French rules, metadata tags | Taxonomy recall/precision not continuously benchmarked by humans |
| Chunking | `test_chunk_cases.py` | Overlap, progress safety, section/paragraph chunks, fallback text | Large corpus timing and reconciliation tests absent |
| Ingestion/provenance merge | `test_ingestion_merge.py`, `test_ingest_a2aj_parquet.py`, `test_import_fc_decisions.py` | Source priority, conflicts, hashes, rich source metadata, import mapping | No concurrent-writer integration test |
| A2AJ/Canlaw staging | `test_a2aj_citation_network.py`, `test_canlaw_*.py`, `test_import_canlaw_staging.py`, `test_curate_a2aj_immigration_cases.py` | Staging identity, multi-court handling, embeddings, bridge/resume, curation | Live upstream API/dataset availability intentionally not tested |
| Federal Court ingestion | `test_fc_ingest_db.py`, `test_fc_ingest_pipeline.py`, `test_fc_portal_collector.py`, `test_fetch_fc_procedural_history_cli.py` | Page parsing, month bounds, resumability, direct mode, CLI no-op | Live anti-bot/source behavior intentionally excluded |
| FC activity intelligence | `test_hf_fc_activity_ingest.py`, `test_classify_fc_activity.py` | Normalization, stable keys, document dedupe, English/French activity classification | Human-adjudicated classification quality set remains limited |
| Embeddings/retrieval evaluation | `test_local_embeddings.py`, `test_openai_chunk_embeddings.py`, `test_evaluate_retrieval.py` | Dimension checks, batching, budgets, metric summaries | No production latency/SLO or provider integration test |
| Overnight operations | `test_run_overnight.py` | Profile composition, module-safe invocation, locks, stale-lock cleanup, resume state | No destructive full-run integration test |
| Reference library | `test_download_reference_library.py` | MIME/signature validation, checksum/provenance, failure cleanup | Live download availability intentionally excluded |
| Security helpers | `test_security.py`, relevant API tests | Cookie signature/expiry, robots headers | Access middleware enforcement is not implemented and therefore not tested as enforced |

## Test Types And Boundaries

### Deterministic Unit Tests

Most tests use fake sessions, temporary files, or mocked HTTP/model clients. They should be fast, repeatable, and safe to run without live network/API credentials. Use them for extractor rules, text offsets, normalizers, classifiers, data merge policy, and argument validation.

### Route/Contract Tests

Route tests verify response shape, validation, parameter bounds, helper delegation, and generated UI contract markers. They do not prove browser JavaScript executes or that PostgreSQL query plans meet performance goals.

### Source-Pipeline Tests

Source collectors and importers are tested against controlled HTML, mock responses, temporary SQLite databases, and fixtures. They intentionally do not bypass access controls or depend on a live court/CanLII page remaining stable.

### Operational Tests

The overnight runner tests locks, job selection, state transitions, and command construction. They do not run full corpus writes. A full operational run needs preflight, bounded canary, state/log review, before/after counts, and sampled QA.

## Required Validation By Change Type

| Change | Minimum test/check |
| --- | --- |
| Citation/statute rule | Relevant `test_citations.py` slice plus exact-span fixture; verify IRPA/IRPR nested forms when touched |
| Reader/UI markup or behavior | `test_feature_tabs.py`, route/compile check, and manual browser interaction |
| Search/ranking/filter | Relevant `test_api.py` slice; inspect query semantics and result ordering |
| Metadata/outcome/docket logic | `test_metadata.py` plus relevant `test_api.py` cases |
| Tag taxonomy | `test_legal_tagger.py` with focused new rule fixture |
| Migration/ORM model | Schema generator, migration check, affected route/model tests, test database inspection |
| Ingestion/source merge | `test_ingestion_merge.py` and importer-specific tests |
| FC activity classifier | `test_classify_fc_activity.py` with English/French and negative example when applicable |
| Script/orchestration | Script `--help`, relevant test module, dry-run/preflight for writers |
| Documentation generator | Run generator, check output, local-link validation, `git diff --check` |

## Browser And Performance Gap

The most important missing layer is browser end-to-end coverage for the active Data Explorer. The generated UI is embedded in `backend/routes.py`; a Python route returning HTML does not prove the JavaScript initializes, tabs switch, searches render, linked citations open, scroll/tooltip behavior works, or mobile stacking is readable.

Add a Playwright-based smoke suite for:

1. `/data-explorer` load and top-level tab switching.
2. Case search to reader opening.
3. Reader mode toggle, citation hover, linked-authority pane, and close/return behavior.
4. Citation Intelligence case selection and subtab load.
5. Mobile-width layout screenshot/no-overlap check.

Performance coverage should add representative PostgreSQL-backed timing and query-plan checks for active search, reader data, citation intelligence, and FC history routes. Keep fixed test datasets/scope and record p50/p95 targets before enforcing a release budget.

## Test Hygiene Rules

1. Tests must express the active data model, not obsolete UI copy or pre-separation statute behavior.
2. Add a regression fixture for every fixed extraction false positive/negative.
3. Keep source/network tests mocked unless an explicitly bounded manual integration run is requested.
4. Do not put real API keys, passwords, source credentials, or personal data into fixtures.
5. Use direct test paths after local changes; run the full suite before a release checkpoint.
6. Record known failures with reason and owner; do not call the suite green while failures remain.