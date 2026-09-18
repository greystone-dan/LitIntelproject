# Repository Atlas And Overnight Operations

Last updated: 2026-09-07

## SCC 1970-present run status

Status: complete

The SCC text-only enrichment run for cases dated 1970-01-01 through the present reached a terminal completion checkpoint. Verified terminal output from the resumed runner was:

- `status=completed`
- `processed=3703`
- `completed=4920`
- `quarantined=8`
- `elapsed_seconds=26363.0`

This was the bounded 1970-present cohort under `data/overnight_runs/scc-text-only-1970-present-20260906`, with no HTML acquisition, no embeddings, and target resolution deferred by design.

## Case Citation Rebuild Gate

The case-citation extractor is ready for an extraction-only rebuild: `case_short` rows preserve their own source offsets and pinpoints, and each may point only to a direct, identifier-bearing full citation span from the same decision. Full CanLII and complete FTR/DLR reporter-only case citations are eligible anchors; bare case names and earlier short forms cannot become anchors. Generic bare aliases such as `Agency`, `Canadian`, `hospital`, and `Revenue` are rejected even when a full case citation exists. The reporter-only branch retains an adjacent court, declared alias, and pinpoint in its full anchor; other full citation forms retain trailing reporters, bracket aliases, and pinpoints in order. Pinpoints persist in citation text and normalized citation; a chunk-linked occurrence uses chunk-relative offsets while its anchor span remains document-relative. The focused in-memory rebuild-style check invokes `extract_citations_from_text(..., resolve_targets=False)` and confirms that two Zazai short forms persist with a shared direct full anchor while no target resolution occurs.

The existing bulk writers are not approved for the rebuild: they either combine citation work with other layers or lack the required explicit cohort, dry run, baseline export, durable checkpoint, exclusive-writer lock, and post-run comparator. The prepared replacement is `scripts/rebuild_citations_controlled.py`, which is intentionally excluded from the standard overnight profile. First create and inspect a bounded baseline without mutation:

```powershell
.\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --case-id <id> --limit 1 --run-dir data/overnight_runs/citation-rebuild-<run-id>
```

Only after reviewing its baseline/state files and receiving explicit approval may an operator add `--apply --confirm-citation-rebuild` to the same explicit cohort. A run directory with an existing `state.json` must not be silently overwritten; either resume the matching run with `--resume` or choose a fresh run directory. The runner replaces only `case_citations`, flushes before recording a pre-commit comparison, and rolls back a nonempty-to-empty result or invalid short-form anchor before commit. It defers generic resolution, short-form resolution, and citation metrics to separate later commands.

The `2026-09-07` corrected one-case canary and five-case cohort completed cleanly. The current database has `61,216` text-bearing cases. A fresh 500-case live-progress gate then completed through `scripts/run_citation_rebuild_progress.py` with fifty ten-case batches: `500` cases processed, `7,700` citations extracted, and zero failed batches under `data/overnight_runs/citation-progress-500-case-retry-20260907`. No citation runner is currently active.

The earlier partial run under `data/overnight_runs/citation-extraction-all-20260907` completed `1,295` cases before its checkpoint write failure. Its state is explicitly `stopped`, with `59,921` cases pending; baseline, comparison, and state artifacts are preserved for recovery and must not be resumed blindly. Target resolution and metrics remain deferred.

The single-directory all-case run resumed past its first pause and later stalled again at case `53722`, whose process burned roughly two hours of continuous CPU with no new checkpoint row; a soft interrupt did not reach the child process, so the worker was force-terminated. Case `53722`'s citations exactly matched its pre-run baseline afterward, confirming a clean rollback, and it is recorded as explicitly `skipped` with its stall evidence. A second recovery defect was found and fixed: the resume walk previously stopped at the first case with no comparison/checkpoint row, even when that case had an operator-recorded terminal status (such as `skipped`) and later cases already had journal evidence; it now treats a recorded terminal status as a pass-through and keeps recovering later cases. The verified cursor after both fixes is case `53757` committed, with case `53758` next; two cases (`24480`, `53722`) are recorded `skipped` with reasons, and no writer outside the current resumed run is active. The runner rewrites the larger `state.json` snapshot every ten cases, retries transient Windows replacements for up to 30 seconds, and records an operator interrupt as stopped. The resume command, after explicit approval, is:

```powershell
.\venv\Scripts\python.exe -u scripts\rebuild_citations_controlled.py --all --limit 61216 --run-dir data/overnight_runs/citation-extraction-all-live-20260907 --apply --confirm-citation-rebuild --progress-every 10 --resume
```

Do not run it until the output terminal is visibly confirmed and no other PostgreSQL writer is active. This command creates no per-batch directories, does not resolve targets or compute metrics, and keeps those as separate post-extraction phases.

The command above has since completed: `61,212` cases committed and four were
explicitly skipped (`24480`, `53722`, `56686`, and `56973`). Do not rerun that
completed directory. Future runs require a fresh directory and newly counted
frozen cohort, and must retain separate target-resolution and metrics phases.

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

Generated documentation is checked automatically by
`.github/workflows/documentation-sync.yml` using
`scripts/check_generated_docs.py` on pushes and pull requests. Swimm walkthrough
updates remain a manual repository checkpoint; the workflow does not publish to
Swimm.

The active deterministic enrichment profile is `enrich`. It runs chunking,
case/statute extraction and metrics, the dedicated `case_outcomes` backfill,
the overnight `tag_cases` job through `scripts/tag_cases_v3.py`, and local
embeddings. The explicit `pipeline` profile runs the complete resumable V2
sequence through `scripts/run_v2_pipeline.py`: source HTML, chunks, metadata,
outcome, case citations, statutes, and V3 tags. It is separate from `enrich`
because the V2 runner has its own per-case quarantine and durable state. The
legacy `scripts/tag_cases.py`, `scripts/tag_cases_v2.py`, and combined citation
job remain outside the active V2 path.

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
| API routing | `backend/routes.py`; HTTP contracts, route dispatch, interface registration, facade re-exports | Requests + DB rows -> JSON/HTML responses | Dispatches to dedicated domain services; lightweight routing | `pytest tests/test_api.py -q`; feature-tab tests; browser check |
| Search & retrieval | `backend/search_service.py`; case/chunk search, lexical tsvector rank, cosine distance semantic scoring, hybrid search, chunk grouping | `CaseSearchRequest` -> Search response models | Executes PostgreSQL ranking and vector similarity | `pytest tests/test_api.py -k search -q` |
| Reader & metadata pass | `backend/reader_service.py`; reader data assembly (`/cases/{id}/reader-data`), metadata pass formatting, HTML citation wrapping | `case_id` -> Reader & citation pass response models | Formats multi-layer evidence payloads without mutating DB | `pytest tests/test_api.py -k reader -q` |
| Analytics & reporting | `backend/analytics_service.py`; SQL aggregations for judge outcomes, yearly trends, data explorer cross-tabs, judge profiles, and FC history | Query params -> Aggregated metrics & distributions | Executes complex reporting and outcome ratio queries | `pytest tests/test_api.py -k analytics -q` |
| Contracts | `backend/models.py`; Pydantic request/response types | HTTP payloads -> validated models/OpenAPI schemas | Used by routes and generated API reference | API contract tests and OpenAPI regeneration |
| Database | `backend/database.py`; settings precedence, sessions, ORM declarations | Environment + ORM operations -> PostgreSQL/pgvector state | Alembic migrations are deployment authority | migration inspection; affected tests |
| Canonical ingestion | `backend/ingestion.py`; identity, source merge, sanitization, provenance | Source records -> canonical cases and case sources | Writes `cases`, `case_sources`, `ingestion_runs` | `pytest tests/test_ingestion_merge.py -q` |
| Ordered processing | `backend/case_processing.py`; metadata, outcome, chunk, citation, statute, and V3 tag stage contract | Canonical case text -> derived layers | Writes selected derived tables; stage order is a contract | processing tests and bounded case run |
| Extraction | `backend/citations.py`; case/statute rules, spans, normalization, metrics helpers | Plain text/chunks -> occurrence rows and metrics inputs | Case citations and statutes remain separate | focused `tests/test_citations.py -q` |
| Citation analytics | `backend/citation_map.py`; read-only graph and authority calculations | Resolved citation edges + metadata -> bounded analytics/CSV | Reads citations, metrics, tags, outcomes | citation-map API tests |
| Metadata | `backend/metadata.py`; fields, outcomes, evidence, confidence | Source text/HTML -> structured observations | Case metadata JSON and review flags | metadata tests and gold-set audit |
| Tagging | `backend/legal_tagger_v3.py`, `backend/case_processing.py`; active deterministic core, with V1/V2 retained for comparison | Case text -> repeated evidence-backed V3 occurrences/status | `case_tags`, `case_tagging_status`; V3 proposal in `data/eval/reports/` | focused V3 tests and bounded canary |
| Embeddings | `backend/embedding_providers.py`; provider selection and vector wiring | Cases/chunks -> model-versioned vectors | pgvector case/chunk embedding tables; optional local/hosted providers | provider tests; bounded embedding run |
| Live analysis | `backend/live_analysis.py`; temporary DOCX/text-PDF extraction and local resolution | Uploaded bytes -> in-memory text, spans, resolution results | No upload/case/chunk/citation persistence | live-analysis tests and API check |
| Federal Court activity | `backend/fc_activity.py`; activity normalization/classification support | Staged activity records -> normalized activity data | Separate activity/procedural tables; not proof of captured judgment | FC activity tests and bounded import |
| Page builders | `backend/pages/`; page-specific HTML builders (`data_explorer.py`, `quick_search.py`, `research.py`, etc.) | Data/config -> rendered page fragments | No canonical writes during rendering | feature-tab tests and browser check |

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

The automatic `safe` and `enrich` profiles intentionally exclude the legacy
combined `citations` job. Any full pipeline or citation backfill must use
`scripts/rebuild_citations_controlled.py`, as validated by the 2026-09-07
all-case replacement. The operator must supply a frozen text-bearing case
count, a fresh run directory, `--apply`, and `--confirm-citation-rebuild`.
Target resolution, statute extraction, and metric recomputation remain separate
post-extraction checkpoints; do not substitute the legacy combined command.

Citation target resolution is intentionally split into exact and conservative
short/name passes. `scripts/resolve_citation_targets.py` handles local citation
variants, unique canonical-title recovery, and duplicate-title disambiguation
when the cited decision year identifies one canonical case. The rule covers
parenthesized reporter years and CanLII/reporter/neutral forms without changing
stored offsets. `scripts/resolve_short_citation_targets.py` uses same-source
composite anchors and repeated globally resolved aliases, with collision and
self-case gates. For `case_short`, formal identifiers preserved in
`normalized_citation` constrain candidate cases; a short name may select one
authority inside a compound anchor, but it must never trigger a corpus-wide
short-name lookup. These scripts must run alone as PostgreSQL writers with
bounded commits and progress logs. After the full replacement and formal/neutral
pass, the live database contained `1,444,546` rows: `919,781` linked and
`524,765` unresolved. The read-only
[post-resolution shape report](data/eval/reports/unresolved_citation_shapes_post_resolution_20260907.json)
attributes `477,627` unresolved rows (`91.02%`) to no exact local signal;
`16,656` have a unique alias signal and `1,258` have an ambiguous title/year
signal. Broad fuzzy matching is not approved.

A cancelled short/name pass committed `3,019` bounded updates before
termination. The accepted remaining short-form inventory gap contains `117,074`
anchored unresolved occurrences across `10,889` source cases and `16,495`
distinct exact anchors; their stored identifiers have no candidate in the local
case inventory. A separate `330` unresolved short rows lack anchors and remain
provenance defects.

The exact case-name pass subsequently linked `14,051` rows using one unique
non-self canonical-title match. The current unresolved total is `507,695`.
Excluding all short forms leaves `390,291`: `333,550 case_name`, `53,078 case`,
and `3,663 neutral`. See
[the non-short unresolved report](data/eval/reports/unresolved_citation_shapes_excluding_short_20260907.json)
for exact shapes and candidate signals.

The extraction layer treats recognized full reported citations, including
`[2004] 3 F.C.R. 323`, as eligible same-document anchors for later short-form
mentions. Historical rows created before this rule may require a separate
bounded extraction backfill; target resolution remains a later pass.

The current anchor-provenance inventory contains `1,408,402` `case_short` rows:
`1,330,030` have anchor fields and `78,372` are missing anchor text or offsets.
Under V2, the latter are backfill defects, not legitimate unanchored rows. The
anchor gap includes `60,399` unresolved rows, compared with `744,708` unresolved
citation rows overall; repair provenance without changing target resolution.

The bounded 2026-09-07 read-only inventory separately inspected the `383,608`
unresolved rows that already have anchor text and offsets. All stored spans
matched their source text. It found `9,130` pure right-edge extension
candidates, `14,235` start-correction candidates requiring review, and
`360,243` rows with no local extension evidence. The last category is not proof
of semantic completeness. The inventory excluded the `78,372` no-anchor rows,
did not run full-document extraction, and made no database writes. A later
anchor-only writer must update only anchor text and anchor offsets; target
resolution remains a separate pass. This is a second, distinct anchor backfill
from task 068: task 069 covers all `383,608` unresolved rows with existing
anchor fields, while its `9,130` pure right-edge rows are only one direct
recovery class inside that backfill.

### Refresh The Website

Use the repository refresh script for the local API and configured Cloudflare
tunnel:

```powershell
.\scripts\refresh_site.ps1
```

It stops stale local Uvicorn and `cloudflared` processes before starting the
site on `http://127.0.0.1:8000`. Keep the terminal open because it owns the
local API and tunnel. The public site is normally available at
`https://www.ilit.ca`.

After a UI change, run the bounded browser smoke check while the refreshed site
is running:

```powershell
.\venv\Scripts\python.exe scripts\browser_smoke.py --base-url http://127.0.0.1:8000 --query Vavilov
```

This checks Data Explorer search, the inline reader tabs, grouped tag output,
the Tags/Laws/Citations legend, and mobile Themes loading. It is a smoke check,
not a substitute for legal-content review or full accessibility testing.

Before any self-citation cleanup, generate a read-only candidate plan:

```powershell
.\venv\Scripts\python.exe scripts\plan_self_citation_cleanup.py --limit 100
```

The planner classifies a bounded sample and always reports
`write_performed=False` and `cleanup_authorized=False`. Do not delete or rewrite
citation rows from its output without a separate reviewed canary plan.

Run the exact-span statute baseline after citation/statute rule changes:

```powershell
.\venv\Scripts\python.exe scripts\evaluate_statute_extraction.py
```

This fixture check measures extraction precision and recall; it does not measure
whole-corpus coverage.

For a bounded sample chunk rebuild, use a case-specific command:

```powershell
.\venv\Scripts\python.exe scripts\chunk_cases.py --case-id 32097 --replace-existing
```

The canonical output has `full_case`, `section`, and `paragraph` layers. Compare
generated text to `Case.full_text` before treating HTML-derived boundaries as
production evidence; preserved HTML and canonical text may not have identical
metadata representations yet.

The curated core subset is `data/eval/core_immigration_cases.csv` with 300
canonical case IDs and source URLs. Use `scripts/reacquire_source_html.py
--limit 5` for a bounded HTML acquisition preflight. The tool rejects Federal
Court public-site shells that do not contain the expected decision citation. For
these item pages, the actual decision may be in the same-origin `?iframe=true`
content URL; preserve the original item URL as source identity and validate the
iframe response before storing a snapshot.

For source-structure testing, use one representative FC, FCA, and SCC case.
Compare decision-body containers, heading patterns, metadata blocks, mapping
confidence, and exact canonical-text containment before expanding the rebuild
population. Court HTML wrappers are not interchangeable.

For SCC canaries, expect `.documentcontent` and nested `SectionN` containers.
The decision body begins at numbered paragraph elements; front-matter summaries,
navigation, and metadata must not be treated as decision paragraphs. Use the SCC
source-specific confidence gate and verify exact canonical-text containment.

Run the fixed Data Explorer retrieval benchmark after ranking changes:

```powershell
.\venv\Scripts\python.exe scripts\evaluate_retrieval_benchmark.py --base-url http://127.0.0.1:8000
```

It reports MRR, precision@k, and recall@k for the bounded benchmark set in
`data/eval/retrieval_benchmark.json`.

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

The compact pre-run baseline for all 61,241 cases is
`data/eval/reports/v2-pipeline-before-all.jsonl`. It records source HTML state,
text/metadata hashes, chunk counts, citation/statute counts, V3 tag count, and
outcome summary without serializing every row. Optimized runs should compare
this baseline and retain detailed snapshots only for the QA sample and flagged
cases.

After removing per-occurrence target resolution from extraction, a fresh 50-case
benchmark completed in 27.3 seconds, approximately 659 cases/hour, with
five-case checkpoints, zero quarantines, and embeddings excluded. Resolution
remains a separate later pass.

The corrected extraction-only rerun is the authoritative speed baseline: 50
cases completed in 23.0 seconds, with zero target resolutions, 1,139 local
short-form anchors, zero quarantines, and embeddings excluded. The prior slow
behavior was the N+1 target-resolution lookup and must not return to extraction.

The full optimized non-SCC text-only run launched under
`data/overnight_runs/v2-text-only-full-20260905` with batch size 50 and no HTML
acquisition, embeddings, or detailed snapshots. SCC remains excluded. Start the
separate slow SCC HTML acquisition only after this PostgreSQL writer completes;
do not run both writers concurrently.

### Completed V2 run review (2026-09-06)

The optimized run completed with `50,327` processed records: `43,598` cases
completed all seven stages, `6,729` were excluded because their source URL had
no parseable allowed host, and `0` were quarantined. The completed cohort was
`86.63%` of processed records. The run state is authoritative at
`data/overnight_runs/v2-text-only-full-20260905/state.json`.

Against the matching completed-cohort rows in
`data/eval/reports/v2-pipeline-before-all.jsonl`, derived rows changed by:

- chunks: `1,634,480 -> 1,822,752` (`+12%`);
- case citations: `1,183,971 -> 1,544,076` (`+30%`);
- statute references: `278,998 -> 459,441` (`+65%`);
- V3 tag occurrences: `38,137 -> 880,795` (`23.1x`).

The read-only integrity audit found no malformed citation/statute offsets and no
V3 tag rows missing offsets. This is an extraction-quality result, not a
reader-complete or graph-complete result: all `1,544,076` new citation rows
remain explicitly unresolved and have no `chunk_id` until the separate local
target-resolution and layer-association pass. Only `17` completed-cohort cases
currently have stored source HTML, so text-only output must not be presented as
HTML-provenance-complete. Stage zero-yield rates were metadata `7.61%`, case
citations `0.69%`, statutes `14.10%`, and tags `37.51%`; these represent cases
with no newly emitted rows for that layer, not quarantined failures.

The next source-refresh workstream is SCC HTML. The current inventory has
`10,889` SCC cases with full text and source URLs but only `27` stored HTML
snapshots. A bounded five-case dry-run probe on 2026-09-06 returned `5 ready`,
`0 quarantined`, and `0 applied`, confirming the SCC URL/content validator path
without writing to PostgreSQL. Use the existing host limiter and quarantine
output for the next bounded write batch; do not combine source acquisition with
another enrichment writer.

The first 25-case SCC write batch refreshed existing snapshots rather than
expanding coverage because the original selector did not exclude cases that
already had HTML; coverage remained `27`. The selector now supports
`--missing-html-only`. A five-case missing-HTML probe returned `1 ready` and
`4 quarantined`; raw inspection showed the four failures redirected to
`login.openathens.net` without decision content. Stop bulk SCC acquisition until
an approved alternate source or URL mapping is available. Do not bypass access
controls or treat the redirect page as a judgment snapshot.

SCC enrichment is prepared as a separate text-only path in
`scripts/run_scc_text_only.py`. It does not require source HTML or a parseable
source host, selects only SCC cases with canonical full text, and runs the same
seven stages as the optimized V2 runner without embeddings. The SCC-specific
chunk fallback recognizes old `1 The Court` paragraphs, modern `[1]` paragraphs,
Roman-numeral sections, and unnumbered older decisions whose canonical text
preserves one body paragraph per line. A five-case dry run completed with zero
writes and zero quarantines; the stored 27-case SCC sample had exact
canonical-text containment for every generated chunk.

The 1980-present SCC canary then ran exactly 50 representative cases through
all seven stages in `530.3` seconds: `50` completed and `0` quarantined. It
created `2,545` chunks, `16,329` extraction-only case citations, `8,117`
statute references, and `351` V3 tag occurrences. The read-only audit found
zero malformed citation/statute offsets and zero missing tag offsets. All
citations remain unresolved and unassociated with chunks until the separate
resolution/layer-association pass. Eight metadata reports were zero-change and
27 cases had no V3 matches; neither is a processing failure. This canary is the
readiness gate for the remaining SCC cases, subject to the same batch size,
checkpoint, and quarantine controls.

SCC performance profiling found short-form citation candidate generation, not
target resolution, to be the dominant cost on very large decisions. The safe
optimization now indexes prior anchors for nearest lookup and avoids copying the
full text prefix during metadata checks. It preserves the 680k-character
benchmark output count (`3,684` citations) and passed the full citation suite
(`109 passed`). A more aggressive combined-regex experiment changed output
counts and was rejected; no accuracy-risking optimization is retained.

The requested SCC production-boundary run launched on 2026-09-06 for the
`4,928` full-text cases dated `1970-01-01` or later. It uses
`data/overnight_runs/scc-text-only-1970-present-20260906`, batch size `25`, no
HTML, no embeddings, and extraction-only citations. Resume with the same run
directory and `--resume` if interrupted; do not start a competing PostgreSQL
writer.

Each SCC case now runs in an isolated process/session with a default
`600`-second watchdog. Exceptions and timeouts are recorded as quarantines, the
child transaction is discarded on termination, and the parent continues to the
next case. This protects the resume after case `53722` demonstrated that
exception-only quarantine could not catch a CPU-bound hang.

The corrected extraction-only rerun completed 50 cases in 23.0 seconds: 1,688
citation occurrences, zero resolved targets, 1,139 same-document anchors, 452
statutes, 1,569 V3 tags, and 50 outcomes. This is the valid benchmark for the
current extraction contract.

HTML-free chunk parity is under active evaluation. The current text-only rules
pass the sample for several FC/FCA/SCC cases, including token/content parity,
but two cases still show paragraph-count divergence. Do not replace the
HTML-enabled reference as the quality gate until the parity report passes or
the remaining family-specific differences are explicitly accepted.

### Profiles And Order

| Profile | Jobs |
| --- | --- |
| `pull` | `fc_decisions`, `fc_portal`, `fc_history` |
| `enrich` | `reference_verify`, `tag_cases`, `chunk_cases`, `citations`, `local_embeddings` |
| `safe` | pull jobs followed by the enrich jobs |
| `pipeline` | `v2_pipeline` |
| `verify` | `regression_tests` |

The safe ordering is significant: acquisition precedes canonical enrichment;
chunking creates `full_case`, `section`, and `paragraph` layers before citation
extraction and local chunk embeddings. Citation extraction writes case citations
and separate statute references, then metrics. Use the explicit job option only
when the dependency order remains valid.

### V2 Pipeline launch gate

The redesigned V2 Pipeline is not the current `safe` profile. Before a cohort
run, use a dedicated tracked runner for:

1. validated source-link HTML reacquisition with host/source disposition;
2. HTML-aware replacement rechunking;
3. metadata refresh;
4. case citations, statute references, and metrics;
5. dedicated outcomes;
6. V3 tags.

Embeddings are excluded. Launch requires bounded timeouts/retries, per-case
failure quarantine, checkpoints, before/after snapshots, and a stratified delta
gate. The current input audit found 61,241 cases and URLs but only 42 stored HTML
snapshots; 6,729 URLs have no parseable hostname and 25 use an unsupported host.
Those source dispositions must be resolved before cohort execution.

The prepared runner is `scripts/run_v2_pipeline.py`. It executes the seven
stages with per-case state and quarantine, and prints `embeddings=False` by
design. The overnight coordinator exposes it as the dedicated `v2_pipeline`
job inside the `pipeline` profile, and the job calls the runner without adding
an `--apply` mode. `scripts/acquire_case_html.py` is its bounded source-refresh helper.
Each local stage runs in an isolated worker with `--stage-timeout` (default 900
seconds); a timeout terminates that worker, records quarantine, and preserves
the run for resume.
The runner is ready for a bounded stratified trial, not an unrestricted cohort
launch, until malformed/unsupported source links and delta gates are resolved.

Source acquisition is configured separately through `scripts/acquire_case_html.py`.
Its default policy is only 2 concurrent workers and a 2-second minimum delay
between requests to the same host, with retries/backoff, request timeouts, host
validation, response/citation validation, and quarantine. Reuse stored
`source_html` before making a network request; do not increase these limits
without reviewing source terms and host response.

The initial six-case trial completed five cases and quarantined one SCC source
whose fetched page did not contain the expected citation. One completed case
had a major citation delta (`407->45`), confirming that the gate is necessary;
no cohort execution should proceed until those cases are adjudicated.

The approved overnight run launched as
`data/overnight_runs/v2-pipeline-20260904` with batch size 25, source timeout 30
seconds, 3 retries, 900-second stage watchdogs, quarantine, and embeddings
excluded. Its state file was `running` with 3 cases checkpointed at the latest
documentation checkpoint. Resume or inspect the same run directory; do not start
a competing writer.

That run was paused for an efficiency redesign after checkpointing 1,786 cases
in roughly 12 hours. The bottleneck is architectural: seven worker-process
launches per case, serial source acquisition, per-case stage commits, and full
comparison-file serialization. The next runner must benchmark a persistent or
batched worker design, concurrent bounded source acquisition, batched commits,
sampled detailed snapshots, and a separate slow queue for very-large cases.

The primary measured bottleneck is now citation resolution: extraction performs
a database lookup for each neutral citation occurrence. This N+1 resolver must
be replaced with a per-case or batch cache before another cohort run; otherwise
citation-heavy decisions can appear idle while queries accumulate.

The main V2 Pipeline policy now excludes SCC by default and forces canonical-
text section and paragraph chunking for non-SCC cases, even when HTML exists.
SCC HTML acquisition is a separate slow calibration path. Bulk mode disables
detailed per-case snapshots; use the compact baseline and sampled/flagged-case
reports after the run.

The V2 Pipeline citation stage is extraction-only. It does not resolve targets
against the database while extracting; all extracted occurrences remain
explicitly unresolved until the separately scheduled local resolution pass runs
after the canonical case corpus is loaded.
Short forms may point to their extracted anchor citation within the same case;
no database lookup is used to create that relationship.

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

Before cohort rollout, create a before snapshot for each bounded test case with
`scripts/compare_pipeline_case.py --snapshot`, run the V2 Pipeline case, create
the after snapshot, and compare them with `--compare`. Block rollout when large
citation/statute deltas, missing evidence offsets, alignment aborts, or outcome
changes lack adjudication. Very large documents use bounded block lookup rather
than global alignment; unmapped blocks remain explicit for review.

The deferred V2 Pipeline rollout requires case-level comparison before cohort
execution. The automated harness now produces before/after reports. A fresh
178K-character case produced chunks `237->247`, citations `36->40`, statutes
`115->114`, and V3 tags `0->10`. The bounded large-document path also
completed a 731K-character case with 709 chunks, 133 citations, 93 statutes,
and 483 V3 tags. Count deltas still require adjudication before cohort rollout.

## Documentation And Modularization Rules

Before changing an owned surface, record the task, reason, owner, dependencies, risk boundary, smallest falsifiable check, acceptance criteria, documentation references, rollback, and evidence. Keep one owning surface and one focused validation command until that check passes. Preserve public imports, route paths, response shapes, provenance, offsets, and separate derived layers while modularizing.

When a subsystem changes, update this atlas only for ownership/lifecycle facts; update `SYSTEM_REFERENCE.md` for current behavior; update the relevant Swimm walkthrough for the traced code path; and update `CHANGELOG.md` with tested milestones. Keep future goals in `GUIDANCE.md`, `ROADMAP.md`, `MASTER_IDEAS.md`, and `.swm/future-state.north-star.sw.md`.

## Current Gaps And Next Atlas Pass

This atlas closes the previous repository-wide coverage gap, but it is not a substitute for file-level API/schema catalogs or route-level walkthroughs. Dedicated Swimm walkthroughs now cover `fc_ingest/` and `canlaw/`. The next useful documentation increments are:

1. Add route/page ownership links for each active generated UI surface.
2. Add a test-to-owner matrix as new subsystem tests are introduced.
3. Replace stale static inventory prose with dated API/database evidence.
4. Tie each future-state capability to a current owner, migration, route, and acceptance test before implementation begins.
