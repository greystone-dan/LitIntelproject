# Repository Atlas And Overnight Operations

Last updated: 2026-09-03

## Purpose And Authority

This is the repository atlas and the canonical operational guide for bounded overnight work. It explains what each meaningful repository family does, how data moves between families, which boundaries are active or isolated, and how to validate changes. It is paired with these authorities:

- `SYSTEM_REFERENCE.md`: current architecture, contracts, data model, routes, limitations, and review posture.
- `DOCS_INDEX.md`: documentation authority and active-versus-historical rules.
- `CHANGELOG.md`: chronological implementation and verification record.
- `docs/CONFIGURATION_REFERENCE.md`: environment variables, precedence, and security configuration.
- `docs/DATA_SOURCE_REGISTER.md`: source identity, provenance, and storage policy.
- `docs/SCRIPT_CATALOG.generated.md`: generated script inventory. Do not edit it manually.
- `docs/SCHEMA_REFERENCE.generated.md` and `docs/API_REFERENCE.generated.md`: generated schema and route appendices. Do not edit them manually.

When this atlas conflicts with a generated reference, regenerate the reference and treat the generated output as authoritative for its subject. When a live count conflicts with prose, query `/api/about/stats` or the database.

## System In One View

```mermaid
flowchart LR
    Sources[Official courts / A2AJ / CanLII / local files] --> Staging[fc_ingest / canlaw / scripts]
    Staging --> Canonical[backend/ingestion.py]
    Canonical --> DB[(PostgreSQL + pgvector)]
    DB --> Process[backend/case_processing.py]
    Process --> Derived[metadata / chunks / citations / statutes / tags / embeddings]
    Derived --> APIs[backend/main.py + routes.py]
    APIs --> Explorer[/data-explorer active research workflow]
    APIs --> Graph[/citation-map authority analytics]
    APIs --> QA[/citation-pass extraction QA]
    Uploads[DOCX / text PDF] --> Live[/live-analysis in-memory workflow]
    Eval[data/eval + tests] --> Quality[focused checks and benchmarks]
    Ops[scripts/run_overnight.py] --> Staging
    Ops --> Process
    Ops --> Quality
```

The central invariant is additive traceability: acquire and preserve source records first, enrich them in separate layers, and expose the evidence without inventing browser-side offsets or legal conclusions.

## Ownership Map

| Surface | Owner and purpose | Inputs -> outputs | Persistence and dependencies | Focused validation |
| --- | --- | --- | --- | --- |
| Application startup | `backend/main.py`; creates FastAPI app, startup, health, access/no-index helpers, router inclusion | Environment + app modules -> running ASGI app | PostgreSQL initialization; FastAPI | `python -m py_compile backend/main.py`; health request |
| API and active UI | `backend/routes.py`; HTTP contracts, orchestration, generated HTML/CSS/JS, reader payloads | Requests + DB rows -> JSON/HTML responses | Reads/writes through database and processing helpers; inline frontend is coupled to routes | `pytest tests/test_api.py -q`; feature-tab tests; browser check |
| Contracts | `backend/models.py`; Pydantic request/response types | HTTP payloads -> validated models/OpenAPI schemas | Used by routes and generated API reference | API contract tests and OpenAPI regeneration |
| Database | `backend/database.py`; settings precedence, sessions, ORM declarations | Environment + ORM operations -> PostgreSQL/pgvector state | Alembic migrations are deployment authority | migration inspection; affected tests |
| Canonical ingestion | `backend/ingestion.py`; identity, source merge, sanitization, provenance | Source records -> canonical cases and case sources | Writes `cases`, `case_sources`, `ingestion_runs` | `pytest tests/test_ingestion_merge.py -q` |
| Ordered processing | `backend/case_processing.py`; metadata, chunk, citation, statute stage contract | Canonical case text -> derived layers | Writes selected derived tables; stage order is a contract | processing tests and bounded case run |
| Extraction | `backend/citations.py`; case/statute rules, spans, normalization, metrics helpers | Plain text/chunks -> occurrence rows and metrics inputs | Case citations and statutes remain separate | focused `tests/test_citations.py -q` |
| Citation analytics | `backend/citation_map.py`; read-only graph and authority calculations | Resolved citation edges + metadata -> bounded analytics/CSV | Reads citations, metrics, tags, outcomes | citation-map API tests |
| Metadata | `backend/metadata.py`; fields, outcomes, evidence, confidence | Source text/HTML -> structured observations | Case metadata JSON and review flags | metadata tests and gold-set audit |
| Tagging | `backend/legal_tagger.py`, `legal_tagger_v2.py`; deterministic taxonomy | Case text/metadata -> evidence-backed tags/status | `case_tags`, `case_tagging_status`; v2 whitelist in `config/` | tagging tests and bounded dry run |
| Embeddings | `backend/embedding_providers.py`; provider selection and vector wiring | Cases/chunks -> model-versioned vectors | pgvector case/chunk embedding tables; optional local/hosted providers | provider tests; bounded embedding run |
| Live analysis | `backend/live_analysis.py`; temporary DOCX/text-PDF extraction and local resolution | Uploaded bytes -> in-memory text, spans, resolution results | No upload/case/chunk/citation persistence | live-analysis tests and API check |
| Federal Court activity | `backend/fc_activity.py`; activity normalization/classification support | Staged activity records -> normalized activity data | Separate activity/procedural tables; not proof of captured judgment | FC activity tests and bounded import |
| Page builders | `backend/pages/`; page-specific HTML builders where separated from routes | Data/config -> rendered page fragments | No canonical writes during rendering | feature-tab tests and browser check |

## Repository Families

### `backend/`

The active runtime package. `main.py`, `routes.py`, `models.py`, `database.py`, `ingestion.py`, `case_processing.py`, `citations.py`, `citation_map.py`, `metadata.py`, tagging, embeddings, Federal Court activity, and live analysis form the current application boundary. `citation_pipeline/` contains reusable citation-pipeline support and must preserve extraction/resolution separation. `pages/` contains page-specific rendering helpers. `legacy/`, when present, is parked code and is not an active ownership target.

### `fc_ingest/`

Federal Court source-specific acquisition and SQLite staging. The package is entered through `__main__.py` and coordinates `index_scraper.py`, `document_scraper.py`, `item_scraper.py`, and `pdf_downloader.py`, with `ingest_pipeline.py` and `db.py` managing orchestration and storage. `models.py` defines staged records and `errors.py` defines source failures. Discovery, download, and document completeness are separate states; an identifier is not proof that a judgment body or PDF was captured. Validate parser/database changes with `tests/test_fc_ingest_db.py` and bounded collector checks.

### `canlaw/`

Source-specific CanLII/legal-data helpers and staging support. `config.py` holds source configuration, `db.py` owns local staging access, `embeddings.py` and `hf_loader.py` support optional model workflows, and `cli.py` is the local entry point. This family must preserve source-native identity and provenance when records cross into canonical ingestion. Direct CanLII access may receive anti-bot responses; use the documented fallback/import paths rather than silently treating a blocked response as a missing case.

### `alembic/`

Deployable schema history. `env.py` connects migration configuration to application metadata, `script.py.mako` templates revisions, and `versions/` contains ordered revisions. Apply with `alembic upgrade head`; do not use `Base.metadata.create_all()` as a deployment substitute. After model or migration changes, inspect the migration and regenerate the schema appendix.

### `scripts/`

Operational tools are separate bounded programs, not one implicit pipeline.

| Family | Representative responsibilities |
| --- | --- |
| Acquisition and staging | A2AJ, CanLII, Federal Court, CanLaw, synthetic/reference imports |
| Federal Court activity | Portal collection, procedural history, activity ingestion/classification, metadata backfill |
| Enrichment | Chunking, tagging, citation/statute extraction, target resolution, judge profiles |
| Retrieval and embeddings | Local/OpenAI embeddings, quick search, retrieval evaluation |
| QA and adjudication | Citation verification/evaluation, metadata audits, gold-set review, candidate cleanup |
| Cohort and fixture builders | Immigration cohorts, FC seeds, activity/citation/metadata gold templates |
| Documentation | API/schema/script/work-history generation |
| Operations | `run_overnight.py`, local server/tunnel refresh and setup scripts |

The generated script catalog is the file-by-file command reference. Before a large writer, inspect `--help`, use a dry-run or bounded limit where available, confirm no competing writer owns PostgreSQL, and record output paths.

### `data/`

Runtime and research artifacts, not a second source of truth for code:

| Path | Meaning and safety boundary |
| --- | --- |
| `data/raw/` | Source-native downloads and SQLite/JSONL staging; usually local/untracked |
| `data/eval/` | Fixtures, cohorts, gold templates, benchmark inputs, reports; inspect before publishing large files |
| `data/reference_library/` | Separate official/reference corpus; `manifest.json` is authoritative and `inventory.csv` is generated |
| `data/overnight_runs/` | Per-run state and logs; never treat logs as canonical case data |
| `data/static/` | Static application/support artifacts |
| `data/copilot_exports/` | Reviewable local-session exports used by work-history generation |
| `data/` other artifacts | Check the producing script and provenance before reuse or deletion |

Reference documents must not enter canonical case tables without an explicit, documented bridge. Raw, staged, synthetic, activity, and canonical judgment records remain distinct.

### `tests/`

Tests are the contract map as well as the regression suite. Route/API and feature-tab tests protect public workflows; citation tests protect exact spans, short forms, and IRPA/IRPR nested provisions; ingestion/source tests protect provenance and merge policy; metadata/tagging/chunk tests protect enrichment; FC, retrieval, analytics, security, and overnight tests protect operational boundaries. A new subsystem should add a focused test before it is moved or modularized.

### `side_projects/`

Isolated utilities and datasets. The Luck of the Draw III project documents its own imports/exports and writes to schema `lotd`; it must not enter canonical case tables or research routes. Other side projects require the same explicit scope, storage, and validation note before being treated as active product code.

### `legacy/` and `docs/history/`

Reference-only material. It explains lineage and prior decisions but may contain old counts, endpoints, tests, or architecture. Never use it to infer current runtime behavior. When an old document is useful to an agent, link it from a current authority and label the historical boundary rather than silently rewriting history.

### Root configuration and documentation

`requirements.txt` defines Python dependencies; `config.yaml` holds project configuration that may be partly legacy or aspirational; `.env` and local environment files hold secrets and must stay ignored. `README.md` is the short entry point. `SYSTEM_REFERENCE.md` is the detailed current handbook. `GUIDANCE.md`, `ROADMAP.md`, and `MASTER_IDEAS.md` describe future direction. `CHANGELOG.md` records verified milestones. `DOCS_INDEX.md` controls authority. `AI_HANDOFF.md` is a detailed working handoff and can be time-sensitive.

Generated API, schema, script, and work-history documents are outputs of their generators. Change the source code or generator, then regenerate; never patch generated output by hand.

## Change Routing Guide

| Change | Read first | Update or validate |
| --- | --- | --- |
| API, search, reader, or analytics | `SYSTEM_REFERENCE.md`, route walkthrough | `tests/test_api.py`, feature tabs, API reference regeneration |
| Citation/statute rule or offset | citation walkthrough and extractor tests | exact-span tests, including `34(1)(f)` positive/negative/exact cases |
| Source adapter or merge policy | source register and ingestion tests | provenance/merge tests and bounded dry run |
| Schema/model | migration history and generated schema rules | migration inspection, affected tests, schema regeneration |
| Overnight job | this document and `scripts/run_overnight.py` | `tests/test_run_overnight.py`, `--help`, preflight |
| UI/page builder | research UI guide and route/page owner | Python compilation, feature-tab tests, browser request/check |
| Evaluation/gold data | data-source register and producing script | bounded generation, fixture/evaluation tests, provenance review |
| Documentation/Swimm | `DOCS_INDEX.md` and owning walkthrough | link review, structural check, `git diff --check` |

## Overnight Runner

The runner in `scripts/run_overnight.py` executes selected jobs sequentially, holds an exclusive lock, writes one combined log per job, and atomically writes `state.json` after transitions. It deliberately excludes CanLII and hosted-AI embedding jobs from the safe profile. Never run another PostgreSQL writer beside an active run.

### Profiles And Order

| Profile | Jobs |
| --- | --- |
| `pull` | `fc_decisions`, `fc_portal`, `fc_history` |
| `enrich` | `reference_verify`, `tag_cases`, `chunk_cases`, `citations`, `local_embeddings` |
| `safe` | pull jobs followed by the enrich jobs |
| `verify` | `regression_tests` |

The safe ordering is significant: acquisition precedes canonical enrichment; chunking precedes citation extraction and local chunk embeddings. Citation extraction writes case citations and separate statute references, then metrics. Use the explicit job option only when the dependency order remains valid.

### Commands

Run from the repository root:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --preflight
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --continue-on-error
.\venv\Scripts\python.exe scripts\run_overnight.py --profile pull --continue-on-error
.\venv\Scripts\python.exe scripts\run_overnight.py --resume --continue-on-error
.\venv\Scripts\python.exe scripts\run_overnight.py --resume 20260801-234642 --continue-on-error
```

Preflight checks the interpreter, scripts, disk space, and PostgreSQL when needed; it does not create a run or contact remote sources. `--help` is the first check for any changed operational interface.

### Recovery And Evidence

Runs are stored under `data/overnight_runs/<run-id>/`:

- `state.json`: durable run status and per-job attempts/results.
- `<job>.log`: combined stdout/stderr for that job.
- `overnight.lock`: active-run ownership marker.

Completed jobs are skipped on resume. Failed and interrupted jobs are retried; collectors may also retain source-specific checkpoints. Use `--force-unlock` only after confirming that no overnight Python process is active. Preserve the run ID, failed job, exit code, log path, and recovery command in the handoff or changelog. Use `docs/OPERATIONAL_RECOVERY_GUIDE.md` for failure-specific steps.

### Focused Overnight Check

```powershell
.\venv\Scripts\python.exe -m pytest tests\test_run_overnight.py -q
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --preflight
```

Do not claim a bulk run succeeded from a preflight result. A successful preflight only establishes readiness; job logs and `state.json` establish the actual outcome.

## Documentation And Modularization Rules

Before changing an owned surface, record the task, reason, owner, dependencies, risk boundary, smallest falsifiable check, acceptance criteria, documentation references, rollback, and evidence. Keep one owning surface and one focused validation command until that check passes. Preserve public imports, route paths, response shapes, provenance, offsets, and separate derived layers while modularizing.

When a subsystem changes, update this atlas only for ownership/lifecycle facts; update `SYSTEM_REFERENCE.md` for current behavior; update the relevant Swimm walkthrough for the traced code path; and update `CHANGELOG.md` with tested milestones. Keep future goals in `GUIDANCE.md`, `ROADMAP.md`, `MASTER_IDEAS.md`, and `.swm/future-state.north-star.sw.md`.

## Current Gaps And Next Atlas Pass

This atlas closes the previous repository-wide coverage gap, but it is not a substitute for file-level API/schema catalogs or route-level walkthroughs. Dedicated Swimm walkthroughs now cover `fc_ingest/` and `canlaw/`. The next useful documentation increments are:

1. Add route/page ownership links for each active generated UI surface.
2. Add a test-to-owner matrix as new subsystem tests are introduced.
3. Replace stale static inventory prose with dated API/database evidence.
4. Tie each future-state capability to a current owner, migration, route, and acceptance test before implementation begins.
