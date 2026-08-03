# AI CaseLibrary Project Notes

## Status note (read first)

This file contains historical checkpoints and milestone commentary.

For live operational status and recent feature surface, prefer:

- `SYSTEM_OVERVIEW.txt`
- `CHANGELOG.md`
- `OVERNIGHT.md`
- `MASTER_IDEAS.md`

## Purpose

AI CaseLibrary is a FastAPI backend for ingesting legal case summaries and finding semantically similar cases. PostgreSQL stores the case records and pgvector stores OpenAI embeddings for similarity search.

## Latest checkpoint (2026-08-01)

First overnight result (`20260801-234642`, completed 2026-08-02):

- Completed: `35,902/35,902` cases tagged under `ca_legal_v2`.
- Completed: `35,902/35,902` cases now have chunks; `168,282` chunks total.
- Pending: citation extraction (`0` rows) and local BGE-M3 embedding (`0` rows).
- Reference verification completed with all `18` records checksum-valid.
- Citation and embedding subprocess import failures are fixed; the existing run
  passes resume preflight and will skip completed tagging/chunking work.
- Current regression baseline: `98 passed`.

- Primary PostgreSQL snapshot:
  - `35,902` cases; `35,498` remain `raw`
  - `2,682` chunks across `383` cases
  - `35,519` text-bearing cases still need chunks
  - zero local BGE-M3 chunk embeddings
  - zero cases recorded complete under `ca_legal_v2`
  - `17,240` Federal Court procedural-history records
- The separate reference library contains `18/18` validated source-native
  documents with provenance, SHA-256 checksums, and a flat inventory.
- Official Federal Court discovery has preserved `830` decision IDs in
  `data/raw/fc/fc_decisions.db`. Full text and PDFs are not yet captured from
  the source's embedded judgment endpoint; discovery must not be represented as
  completed document capture.
- `scripts/run_overnight.py` is ready for unattended sequential operation. It
  runs official FC acquisition, reference verification, `ca_legal_v2` tagging,
  corpus chunking, citation extraction, and local BGE-M3 embedding.
- Overnight execution uses no Copilot, OpenAI, Anthropic, or other hosted AI.
  BGE-M3 runs locally on CPU by default. CanLII is excluded.
- Jobs are lock-protected, logged separately, and tracked in atomic state files.
  Resume skips completed jobs and retries failed or interrupted jobs.
- Acquisition outputs remain staged in SQLite/JSONL unless an explicit import
  bridge is run. Enrichment jobs operate on canonical PostgreSQL cases.
- Current full regression baseline: `94 passed`; workspace diagnostics are clean.
- Operational commands and caveats are maintained in `OVERNIGHT.md`.

## Previous checkpoint (2026-07-31)

- Prototype productization milestone completed for immigration cohort exploration:
  - prototype set name: `immigration_334_v1`
  - cohort: `334` cases (`300` core + `34` exact seed additions)
  - cohort integrity: `334` embedded, `334` chunked
  - cohort graph artifacts: `334` nodes, `724` edges
- New prototype endpoints and UI are live:
  - `GET /prototype`
  - `GET /prototype/summary`
  - `GET /prototype/cases`
  - `GET /prototype/graph`
- Citation map is now interactive:
  - topic-aware graph filtering
  - node-limit performance controls
  - node hover details
  - node click to filter case table by citation
- Topic-keyword tagging for the full prototype cohort has been executed:
  - `scripts/tag_prototype_topics.py`
  - last run: `cases_scanned=334`, `cases_updated=334`
- Pagination robustness update:
  - out-of-range prototype pages now clamp to page `1` when filtered totals are non-zero
- Test baseline is now:
  - `pytest -q` => `52 passed`

## Project review (current)

Findings ordered by severity:

1. High: prototype graph totals are artifact-backed rather than DB-live (`/prototype/summary` and `/prototype/graph` derive edge counts from exported CSV artifacts).
   - Impact: if cohort export artifacts are stale, UI graph totals can drift from the latest database state.
   - Recommendation: either regenerate artifacts on each cohort rebuild or add a DB-backed mode with explicit source labeling.
2. Medium: runtime confusion risk when multiple uvicorn instances run on different ports (for example `8000` and `8040`) with different code vintages.
   - Impact: users can see route mismatches (e.g., one port returns `404` for newly added prototype routes).
   - Recommendation: standardize one active dev port per session or launch with `--reload` and documented restart steps.
3. Medium: documentation drift had accumulated and required manual sync (historical counts, endpoint list, and test totals).
   - Impact: handoff quality degrades and can cause wrong assumptions in later implementation.
   - Recommendation: maintain a short “latest verified snapshot” block and update it after each milestone.

Prior milestone context (pre-prototype explorer stage):

- The citation graph is now merged across local extraction and A2AJ provenance:
  - unified `citations` rows carry `provenance` (`local` or `a2aj`)
  - A2AJ provenance tables exist for `a2aj_cases`, `a2aj_citation_edges`, and `a2aj_case_map`
  - `scripts/ingest_a2aj_citation_network.py` can ingest the A2AJ parquet citation network and convert it into local edges
  - FastAPI endpoints expose both local and A2AJ graph views
- Citation-network scaffolding now exists:
  - `backend/citations.py` holds regex extraction, neutral-citation resolution, and graph metric helpers.
  - new database tables: `citations` and `citation_metrics`
  - read endpoints for outgoing, incoming, passage-level citations, and citation metrics are wired into `backend/routes.py`
  - `scripts/extract_citation_network.py` can backfill citations from cases or chunks and recompute metrics
  - search now uses citation in-degree as a small tie-break boost for case ranking
- Metadata search is now the primary `/testing` workflow, with a filter-first UI modeled on legal search patterns.
- UI search supports structured filtering across core A2AJ metadata: identifiers, citations, source metadata, date windows, noteup/citation-network filters, language, status, and citing-count bounds.
- The payload JSON editor remains available as an advanced override but is synchronized from form controls.
- A new immigration-focused seed builder exists at `scripts/curate_a2aj_immigration_cases.py`.
- That script targets a balanced core dataset of immigration cases using buckets for refugee protection, judicial review, removal/detention, family/citizenship, and agency/enforcement signals.
- The resulting dataset uses `source_type="a2aj_immigration_core"`.
- Current local corpus snapshot:
  - `3060` total cases
  - `2989` with `source_type=a2aj_parquet`
  - `25` with `source_type=a2aj_curated`
  - `46` legacy/other records with `source_type` unset
  - `553` total chunks (from earlier curated/pilot chunking)
- Search route now validates `date_from/date_to`, `scraped_from/scraped_to`, and `citing_cases_min/citing_cases_max` ranges.

## Project history

- OpenAI account and billing were configured, and an API key was created and saved locally. No key or password is stored in project documentation.
- Python 3.12, PostgreSQL, pgAdmin, pgvector, and the project virtual environment were installed.
- PowerShell activation required `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.
- The original database setup referenced `ai_caselibrary`; the working database is `caselibrary`.
- Startup debugging resolved missing environment loading, PostgreSQL authentication, and the incorrect database name.
- Database initialization and FastAPI startup are currently verified.
- Alembic migrations now manage schema evolution, including provenance fields and the HNSW cosine index.
- Search now supports court, jurisdiction, date-range filters, pagination, and a similarity score.
- Focused API tests cover ingestion, filtered search, date validation, and missing OpenAI configuration.
- A 20-record synthetic Federal Court non-refoulement dataset has been imported for safe pipeline testing. The earlier contract demo remains in the database, for 21 total records.
- The reusable importer is `scripts/ingest_synthetic_cases.py`; it validates records with Pydantic and skips existing citations when rerun.
- Raw ingestion is now supported: summary and embedding are optional, full-text hashes are automatic, provenance and A2AJ citation-network fields are stored, and raw records use `processing_status="raw"`.
- The A2AJ Parquet importer is `scripts/ingest_a2aj_parquet.py`. It supports `--dry-run`, `--limit`, Federal Court filtering, citation/hash deduplication, and does not call OpenAI.
- The A2AJ Federal Court Parquet file is stored locally at `data/raw/a2aj/FC/train.parquet`. It is approximately 805 MB and contains 35,814 records. A 25-record dry run completed successfully with zero invalid records and zero duplicate records.
- The first 25 A2AJ Federal Court records were imported, chunked into 82 chunks, and embedded. A separate 25-record curated refugee-risk group was imported as `a2aj_curated` and embedded into 471 chunks.
- Added `GET /cases/{id}` to retrieve a stored case by database ID, including raw A2AJ records. Unknown IDs return `404`.
- Processing statuses are now accurate: all 71 current case records are `embedded`.
- The 25 A2AJ pilot cases were chunked into 82 overlapping chunks and embedded with `text-embedding-3-small`. Estimated input was 105,186 tokens and estimated embedding cost was $0.0021.
- The first real A2AJ search returned embedded A2AJ cases, proving end-to-end retrieval. Synthetic cases still rank highly, so retrieval quality requires a curated benchmark and chunk-level search before scaling.
- Added a reproducible keyword-scored curated set of 25 A2AJ refugee-risk cases as `source_type="a2aj_curated"`. These cases produced 471 chunks and are embedded for evaluation.
- Added `POST /search/chunks`, which returns the matching full-text passage, parent case, citation, chunk index, and similarity score. Multiple chunks can come from one case and should later be grouped for user-facing results.
- Code-review cleanup: searches can filter by `source_type`, ingestion derives processing status from actual behavior, and full-text hashes are computed server-side.
- Search/filter expansion: added `title_contains`, `source_name_contains`, `source_url_contains`, `source_id_contains`, `citation_contains`, `secondary_citation_contains`, `dataset_version_contains`, `upstream_license_contains`, `cases_cited_contains`, `cases_citing_contains`, `language`, `processing_status`, `scraped_from`, `scraped_to`, `citing_cases_min`, and `citing_cases_max`.

## Current project structure

```text
AI CaseLibrary/
|-- backend/
|   |-- database.py   SQLAlchemy engine, sessions, ORM Case model, database startup
|   |-- main.py       FastAPI app, startup hook, router registration, health endpoint
|   |-- models.py      Pydantic request and response schemas
|   |-- routes.py      Ingest and semantic search endpoints
|   `-- .env          Local secrets and database settings; never commit
|-- .env.example      Configuration template
|-- config.yaml        Non-secret static configuration
|-- requirements.txt   Python dependencies
|-- SETUP.md           Installation and PostgreSQL/pgvector guide
|-- CHANGELOG.md       Chronological project history
|-- GUIDANCE.md        Long-term product and architecture north star
|-- AI_HANDOFF.md      Detailed continuation brief for another AI
 `-- PROJECT_NOTES.md   This durable project handoff
 ```

For forward-looking product and architecture decisions, see [GUIDANCE.md](GUIDANCE.md). For a full technical continuation brief, see [AI_HANDOFF.md](AI_HANDOFF.md). This file describes the current implementation and verified local setup; `CHANGELOG.md` records completed changes.

## Current architecture

1. `backend/main.py` creates the FastAPI application.
2. The startup hook calls `init_db()`.
3. `backend/database.py` loads environment variables, creates the SQLAlchemy engine, enables pgvector, and creates ORM tables.
4. `backend/routes.py` receives requests and calls OpenAI embeddings.
5. PostgreSQL stores the case and its 1536-dimensional vector.
6. Search orders records by pgvector cosine distance and returns five results.

## Current API

### Health check

```http
GET /
```

Expected response:

```json
{"message":"AI CaseLibrary backend is running"}
```

### Ingest a case

```http
POST /ingest
Content-Type: application/json
```

Request:

```json
{
  "title": "Example Case",
  "court": "Federal Court",
  "date": "2026-07-31",
  "summary": "This case concerns a commercial contract dispute."
}
```

The summary is embedded with `text-embedding-3-small`, then the case and vector are committed to PostgreSQL.

### Search cases

```http
POST /search
Content-Type: application/json
```

Request:

```json
{"query":"commercial contract dispute","jurisdiction":"Ontario","page":1,"page_size":5}
```

The query is embedded and the closest cases are returned using cosine similarity. Optional filters include `court`, `jurisdiction`, `date_from`, and `date_to`. Results include a normalized `similarity` value from 0 to 1.

For metadata-first workflows (`search_mode="metadata"`), the API also supports:

- `title_contains`
- `source_name_contains`, `source_url_contains`, `source_id_contains`
- `citation_contains`, `secondary_citation_contains`
- `dataset_version_contains`, `upstream_license_contains`
- `cases_cited_contains`, `cases_citing_contains`, `cited_case`
- `language`, `processing_status`
- `scraped_from`, `scraped_to`
- `citing_cases_min`, `citing_cases_max`
- `party_filters` (with alias expansion for Minister/IRCC/CBSA naming variants)

Interactive documentation is available at `http://127.0.0.1:8000/docs`.

## Local configuration

The current local database is named `caselibrary` and PostgreSQL runs on `localhost:5432`.

`backend/.env` must contain real local values, for example:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=caselibrary
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_real_postgres_password
OPENAI_API_KEY=your_real_openai_key
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

The application reads `.env` from the project root first and then `backend/.env`. Do not place real keys in `.env.example`, `config.yaml`, or tracked documentation.

## How to run

From the project root in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload
```

The backend was last verified at `http://127.0.0.1:8000` with successful PostgreSQL initialization and FastAPI startup.

## Important troubleshooting history

- A literal `DATABASE_URL=missing` caused SQLAlchemy URL parsing to fail. Clear accidental process environment variables before retrying.
- The initial default password was rejected by PostgreSQL. The actual password in `backend/.env` must match the PostgreSQL `postgres` user.
- The configured database initially did not exist. The working database is `caselibrary`.
- The VS Code message about Python environment injection being disabled was not the application blocker. `python-dotenv` loads the saved file directly.
- PostgreSQL must have the `vector` extension available. Startup runs `CREATE EXTENSION IF NOT EXISTS vector`.

## Next recommended milestones

1. Add a relevance evaluation fixture with expected citations for research questions.
2. Group chunk results by parent case and add source-type filters.
3. Review and refine the curated evaluation set.
4. Add hybrid keyword and semantic ranking with measured benchmarks.
5. Add a RAG chat endpoint only after retrieval quality is measurable.
6. Add larger ingestion jobs, deduplication, authentication, observability, and a user-facing interface.
