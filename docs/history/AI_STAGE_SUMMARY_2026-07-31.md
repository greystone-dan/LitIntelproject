# AI CaseLibrary - Current Stage Summary (2026-07-31)

## Status note (historical snapshot)

This file captures project state on 2026-07-31 and is not a live status
document.

For current status, use:

- `SYSTEM_OVERVIEW.txt`
- `CHANGELOG.md`
- `OVERNIGHT.md`
- `DOCS_INDEX.md`

## 1. Project purpose

AI CaseLibrary is a litigation-focused legal retrieval backend. It ingests case records, stores metadata and vectors in PostgreSQL + pgvector, and supports semantic retrieval at case and passage level. It is positioned as a research aid with traceability to source records.

## 2. Current implementation stage

The project is past foundational setup and into retrieval-quality iteration.

Completed platform capabilities:

- Raw or embedded ingestion through `POST /ingest`.
- Case retrieval by id through `GET /cases/{case_id}`.
- Case-level semantic search through `POST /search` with metadata filters and pagination.
- Case-level multi-mode search through `POST /search` with `semantic`, `lexical`, and `hybrid` ranking modes.
- Chunk-level semantic search through `POST /search/chunks`.
- Server-side grouped chunk retrieval through `POST /search/chunks/grouped`.
- Built-in manual API testing UI through `GET /testing`.
- Citation-aware filters in search requests (`cited_case`, `citation_contains`).
- Free legal citation extraction during ingest using `eyecite`.
- Retrieval evaluator supports per-topic metrics and quality gates.
- Federal Court source adapter script supports JSON/JSONL/CSV import into `/ingest`.
- Federal Court portal collector now supports staged listing/detail collection and importer-ready output rows.

## 3. Notable recent upgrades in this session

1. Added a first-party testing UI endpoint (`/testing`) with request editors and live JSON outputs.
2. Added grouped chunk controls in UI and backend endpoint for grouped passage retrieval.
3. Added runtime config hardening in database config:
- Explicit `POSTGRES_*` settings now take precedence over `DATABASE_URL`.
- This avoids stale shell `DATABASE_URL` values breaking startup.
4. Added citation extraction fallback behavior and citation-aware search filtering.
5. Added retrieval evaluation harness script and sample fixture file.
6. Added weighted hybrid ranking controls (`search_mode`, `semantic_weight`, `lexical_weight`, `candidate_pool`) and lexical-only no-embedding path.
7. Added benchmark quality-gate options and JSON reporting in `scripts/evaluate_retrieval.py`.
8. Added a 25-query starter benchmark fixture with topic labels.
9. Expanded tests from earlier 8 to current 19 passing tests.
10. Added FC portal staged collector enhancements:
- `--emit-import-ready` writes records directly mappable by `scripts/import_fc_decisions.py`.
- `--incremental-prefix-window` rotates prefix subsets across runs using checkpoint state.
- Added mocked end-to-end collector test to validate listing + detail -> import-ready mapping.

## 4. Current API surface

- `GET /`
- `POST /ingest`
- `GET /cases/{case_id}`
- `POST /search`
- `POST /search/chunks`
- `POST /search/chunks/grouped`
- `GET /testing`

New search request filter fields:

- `cited_case`: exact citation token expected in `cases_cited`.
- `citation_contains`: substring match over `citation` and `secondary_citation`.

New ranking controls:

- `search_mode`: `semantic` | `lexical` | `hybrid`
- `semantic_weight`: hybrid semantic contribution
- `lexical_weight`: hybrid lexical contribution
- `candidate_pool`: pre-pagination candidate set size for weighted reranking

## 5. Data and environment snapshot

- Python: 3.12.1 (`venv`)
- PostgreSQL: localhost:5432
- Database: `caselibrary`
- pgvector enabled
- Embedding model: `text-embedding-3-small`
- Alembic head: `0004_case_chunks`
- Known local dataset baseline from prior handoff: 71 cases, 553 chunks

## 6. Testing status

Automated test status verified in this session:

- `12 passed` in `pytest -q`

Coverage focus:

- ingestion and embedding behavior
- date validation
- hash/status derivation safeguards
- source filtering behavior via SQL parameter assertions
- UI endpoint availability
- grouped chunk search grouping behavior
- DB URL precedence logic

## 7. Key technical decisions currently in force

1. Ingestion derives `processing_status` from behavior; client cannot force incorrect status.
2. Server computes `full_text_hash` from submitted text.
3. Grouped chunk search is now a backend concern, not only frontend post-processing.
4. Project-local Postgres settings can override stale inherited `DATABASE_URL` when `POSTGRES_*` is set.

## 8. Risks and known gaps

1. Retrieval quality still needs formal benchmark fixtures (query -> expected citations/cases).
2. No reranking stage yet (cross-encoder or citation-aware rerank).
3. No RAG answer endpoint yet.
4. Case chunk table still lacks explicit FK constraint to cases.
5. Retrieval evaluation currently depends on external fixture quality and should be expanded with more expected-citation examples.

## 9. Next recommended build order

1. Add retrieval evaluation fixtures and benchmark tests.
2. Add free citation extraction/normalization component in ingestion pipeline.
3. Add hybrid ranking (keyword + semantic) behind explicit configuration/parameters.
4. Add reranking stage for top-k results.
5. Add grounded RAG endpoint after measurable retrieval quality thresholds.

Current artifact for step 1:

- `scripts/evaluate_retrieval.py`
- `data/eval/research_questions.sample.json`
- `data/eval/research_questions.starter25.json`

Evaluator gate flags now available:

- `--min-hit-rate`
- `--min-mrr`
- `--min-topic-hit-rate`
- `--min-topic-fixtures`
- `--report-json`
- `--limit`
- `--verbose`

## 10. Files to read first for a new AI

1. `GUIDANCE.md` (north star)
2. `AI_HANDOFF.md` (deep historical handoff)
3. `backend/routes.py` (active endpoint logic)
4. `backend/models.py` (request/response contracts)
5. `backend/database.py` (connection + schema models)
6. `tests/test_api.py` and `tests/test_database_config.py` (behavioral expectations)
