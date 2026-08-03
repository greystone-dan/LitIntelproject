# AI CaseLibrary - AI Handoff

## Status note (read first)

This file is historical context and may not contain the latest endpoint surface,
test totals, or overnight outcomes.

Use these files as the current operational source of truth:

- `SYSTEM_OVERVIEW.txt` for plain-language system state.
- `CHANGELOG.md` for milestone-level implementation updates.
- `OVERNIGHT.md` for current overnight run operations.
- `MASTER_IDEAS.md` for the staged feature roadmap.

## Purpose of this document

This is the detailed continuation brief for another AI assistant or developer. It describes the verified project state as of 2026-08-01, what has been implemented, what the data means, what was tested, and what should happen next. It intentionally contains no passwords or API keys.

## AI stage summary (current)

Stage: full-corpus operational enrichment with resumable local processing.

Verified canonical PostgreSQL state:

- `35,902` cases; `35,498` remain `raw`.
- `2,682` chunks across `383` cases.
- `35,519` text-bearing cases are pending chunk creation.
- Zero local BGE-M3 chunk embeddings have been written yet.
- Zero cases are recorded complete under the current `ca_legal_v2` taxonomy.
- `17,240` Federal Court procedural histories are stored.

Legal tagging update:

- `backend/legal_tagger.py` defines evidence-bearing `ca_legal_v2` deterministic tags.
- Migration `0010_case_legal_tags` is applied; it adds indexed `case_tags` and
  taxonomy-aware `case_tagging_status` tables.
- `scripts/tag_cases.py` supports dry runs, bounded batches, resume, filters, and retagging.
- PRRA, CBSA/MPSEP removal procedure, inadmissibility, detention, IRPA/IRPR,
  remedies, international law, countries, and organizations are first-class dimensions.
- See `LEGAL_TAGGING.md` for source hierarchy, cautions, taxonomy coverage, and commands.
- The full `ca_legal_v2` bulk run has not started; the overnight job is ready.

Overnight operations:

- `scripts/run_overnight.py` runs official Federal Court acquisition, reference
  verification, tagging, chunking, citation extraction, and local embeddings in
  a single sequential writer pipeline.
- The runner uses an exclusive lock, timestamped run directory, atomic
  `state.json`, separate combined-output logs, preflight, and resumable job state.
- `scripts/chunk_cases.py` uses 6,000-character chunks with 600-character overlap,
  keyset pagination, and commits every 50 cases.
- `scripts/embed_local_chunks.py` uses local BGE-M3, writes 1,024-dimensional
  vectors, defaults to CPU, and commits every four chunks.
- CanLII and all paid Copilot/OpenAI/Anthropic jobs are excluded from the safe
  overnight profile. The first BGE-M3 run may download model files.
- Run and resume instructions are authoritative in `OVERNIGHT.md`.

Separate source state:

- The reference library contains `18/18` validated source-native PDF/HTML
  documents with retrieval metadata and SHA-256 checksums.
- `data/raw/fc/fc_decisions.db` preserves `830` discovered official Federal Court
  decision IDs. It currently has zero captured full texts and PDFs because the
  embedded judgment endpoint rejects the automated payload stage.
- Portal and official-decision acquisition output is staged in JSONL/SQLite and
  is not automatically merged into canonical PostgreSQL cases.
- `canlaw.db` remains a separate `61,217`-record A2AJ staging archive.

Verified quality state:

- `pytest -q` => `94 passed`.
- Workspace diagnostics are clean.
- Both `safe` and `pull` overnight profiles pass live preflight.

Recommended launch:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --continue-on-error
```

## Earlier update (2026-07-31)

- Citation graph update:
  - local and A2AJ citation edges now share the unified `citations` table, tagged by `provenance`
  - A2AJ provenance tables are present: `a2aj_cases`, `a2aj_citation_edges`, `a2aj_case_map`
  - `scripts/ingest_a2aj_citation_network.py` reads the A2AJ parquet network, builds the map, and converts edges into local citations
  - endpoints now include local citation lookups plus A2AJ case/edge/map views and conversion triggers
  - citation metrics still recompute from the unified graph, so A2AJ and local edges both count
- Citation-network scaffolding is now present:
  - `backend/citations.py` implements neutral, case, and statute citation extraction plus neutral-citation resolution.
  - `citations` and `citation_metrics` tables were added in Alembic and the ORM.
  - backend endpoints now expose outgoing, incoming, and passage-level citation rows plus per-case metrics.
  - `scripts/extract_citation_network.py` can backfill the graph from cases or chunks and recompute metrics.
  - case search applies a small in-degree tie-breaker to surface more-cited cases a bit higher.
- Expanded metadata search and tester UX significantly:
  - Added structured filters for title, source metadata, citation variants, language, processing status, scrape date range, and citing-case bounds.
  - Added relationship filters for `cases_cited` and `cases_citing` text matching.
  - Added range validation for decision date, scrape date, and citing-case min/max bounds.
  - Reworked `/testing` into a metadata-first legal search panel with advanced filters, agency presets, synchronized payload preview, and active-filter summary.
  - Adopted CanLII-inspired wording for document-text, identifier, and noteup-style fields.
- Project health pass completed:
  - `pytest -q` => `52 passed`
  - no workspace diagnostics from `get_errors`
  - live `/search` smoke check on port `8031` returned HTTP `200` with pagination headers.

Example safe smoke run:

```powershell
& "c:/Users/danny/OneDrive/Desktop/AI CaseLibrary/venv/Scripts/python.exe" scripts/fc_portal_collector.py `
  --prefixes IMM `
  --max-pages 1 `
  --max-records 25 `
  --delay-ms 1500
```

## Product vision

AI CaseLibrary is intended to become a litigation-focused Canadian legal knowledge system. It should preserve judicial decisions and related source metadata, support reliable semantic and keyword retrieval, expose citation relationships, and eventually provide citation-grounded RAG research assistance.

The central design principle is:

> Preserve source records first, enrich them second, and make every derived result traceable to its source.

The system is a research aid, not a substitute for legal advice. A2AJ records are unofficial copies and must be verified against authoritative sources when accuracy is important.

## Verified local environment

- Workspace: `C:\Users\danny\OneDrive\Desktop\AI CaseLibrary`
- Python: 3.12.1 in `venv`
- PostgreSQL: local service on `localhost:5432`
- Database: `caselibrary`
- pgvector: enabled
- OpenAI embedding model: `text-embedding-3-small`
- FastAPI development command:

```powershell
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload
```

The default API URL is `http://127.0.0.1:8000` and the OpenAPI UI is `/docs`.

The application loads secrets from the project-root `.env` or `backend/.env`. The local file must not be committed.

## Repository structure

```text
AI CaseLibrary/
|-- backend/
|   |-- database.py       SQLAlchemy engine, ORM Case and CaseChunk models
|   |-- main.py           FastAPI app and startup initialization
|   |-- models.py         Pydantic request and response models
|   |-- routes.py         Ingest, retrieval, and embedding calls
|   `-- .env              Local secrets; do not commit
|-- alembic/
|   |-- env.py            Migration environment using the application engine
|   `-- versions/
|       |-- 0001_case_metadata.py
|       |-- 0002_raw_ingestion.py
|       |-- 0003_backfill_processing_status.py
|       `-- 0004_case_chunks.py
|-- scripts/
|   |-- ingest_synthetic_cases.py
|   |-- ingest_a2aj_parquet.py
|   |-- curate_a2aj_cases.py
|   `-- embed_a2aj_cases.py
|-- tests/test_api.py      Focused API behavior tests
|-- data/raw/a2aj/FC/      Local ignored A2AJ Parquet source
|-- CHANGELOG.md           Chronological history
|-- PROJECT_NOTES.md       Current compact handoff
|-- GUIDANCE.md            Long-term product and architecture direction
|-- AI_HANDOFF.md          This detailed continuation brief
|-- requirements.txt       Python dependencies
|-- alembic.ini            Alembic configuration
|-- config.yaml            Static non-secret configuration
`-- SETUP.md               Original environment setup guide
```

## Current database state

Verified current totals:

```text
35,902 case records
35,498 raw case records
2,682 case chunks across 383 cases
35,519 text-bearing cases pending chunk creation
0 local BGE-M3 chunk embeddings
0 ca_legal_v2 tagging completion records
17,240 Federal Court procedural histories
```

The existing chunks represent curated, pilot, and prototype subsets. The
overnight chunker will expand coverage without replacing existing chunks, after
which local BGE-M3 embedding processes all pending chunks resumably.

The local A2AJ source file is:

```text
data/raw/a2aj/FC/train.parquet
```

It is approximately 805 MB and contains 35,814 Federal Court records. It is ignored by version control.

The canonical PostgreSQL corpus is now substantially loaded, but broad local
chunking and embedding have not yet run.

## Data model

### `cases`

The main case record includes:

- `id`
- `title`
- `court`
- `jurisdiction`
- `date`
- `citation`
- `secondary_citation`
- `summary`, nullable during raw ingestion
- `full_text`
- `issues`
- `metadata_json`
- `source_url`
- `source_name`
- `source_id`
- `source_type`
- `dataset_version`
- `upstream_license`
- `scraped_at`
- `language`
- `full_text_hash`
- `processing_status`
- `cases_cited`
- `cases_citing`
- `citing_cases_count`
- `embedding`, nullable until enrichment
- `created_at`

### `case_chunks`

Full-text chunks include:

- `id`
- `case_id`
- `chunk_index`
- `text`
- `text_hash`
- `token_estimate`
- `embedding`
- `embedding_model`
- `created_at`

There is currently no database foreign-key constraint from `case_chunks.case_id` to `cases.id`. Add that in a future migration after deciding the desired delete behavior, preferably `ON DELETE CASCADE`.

## API behavior

### `GET /`

Health check returning:

```json
{"message":"AI CaseLibrary backend is running"}
```

### `POST /ingest`

Accepts structured metadata and either a summary, full text, or both.

- If `summary` is provided, the route calls OpenAI and stores an embedding.
- If only `full_text` is provided, the route performs raw ingestion without OpenAI.
- The server computes `full_text_hash` from the supplied full text and does not trust a client-provided hash.
- `processing_status` is derived by the route: `embedded` when summary embedding is created, otherwise `raw`.
- A request must contain at least one of `summary` or `full_text`.

The endpoint currently does not implement citation-based idempotency itself. Batch importers handle duplicate detection before calling it.

### `GET /cases/{case_id}`

Returns a stored case by ID, including raw A2AJ metadata and full text. Returns HTTP 404 for an unknown ID. This endpoint currently returns the complete full text, which may be large; a future response mode should support metadata-only and text-preview responses.

### `POST /search`

Performs case-level cosine similarity search against non-null case embeddings. Supports:

- `title_contains`
- `court`
- `jurisdiction`
- `source_name_contains`
- `source_url_contains`
- `source_id_contains`
- `source_type`
- `citation_contains`
- `secondary_citation_contains`
- `dataset_version_contains`
- `upstream_license_contains`
- `cases_cited_contains`
- `cases_citing_contains`
- `party_filters`
- `date_from`
- `date_to`
- `scraped_from`
- `scraped_to`
- `language`
- `processing_status`
- `citing_cases_min`
- `citing_cases_max`
- `page`
- `page_size`

Results include a normalized similarity value, but this value is a ranking signal, not legal confidence or truth.

### `POST /search/chunks`

Performs cosine similarity search over embedded chunks and returns:

- Parent case metadata
- `chunk_index`
- Matching `chunk_text`
- Similarity

The endpoint can return multiple chunks from the same case. This is useful for RAG prototyping but should be grouped by parent case before becoming a polished user-facing search result.

## Ingestion and embedding scripts

### `scripts/ingest_a2aj_parquet.py`

Reads A2AJ Parquet records and sends raw records through `/ingest`.

Features:

- Federal Court selection with `--court FC`
- `--limit`
- `--dry-run`
- Citation and full-text-hash duplicate detection
- A2AJ provenance and citation-network mapping
- No OpenAI calls

Example:

```powershell
$env:PYTHONPATH = (Get-Location).Path
$env:CASELIBRARY_INGEST_URL = "http://127.0.0.1:8001/ingest"
.\venv\Scripts\python.exe scripts/ingest_a2aj_parquet.py `
  data/raw/a2aj/FC/train.parquet `
  --court FC --limit 25 --dry-run
```

### `scripts/curate_a2aj_cases.py`

Scans the full local A2AJ Federal Court Parquet file using transparent keyword scoring for:

- Non-refoulement
- Torture
- Persecution
- Removal/deportation
- State protection
- Internal flight alternatives

It imports the top 25 as `source_type=a2aj_curated` with selection scores in `metadata_json`. This is a reproducible evaluation set, not a substitute for legal expert curation.

### `scripts/embed_a2aj_cases.py`

Chunks raw cases into approximately 6,000-character chunks with 600-character overlap, estimates tokens at roughly four characters per token, batches OpenAI embedding requests, stores chunk vectors, averages chunk vectors into the case-level vector, and marks cases embedded.

Environment variables:

- `A2AJ_EMBED_LIMIT`, default `25`
- `A2AJ_EMBED_SOURCE_TYPE`, default `a2aj_curated`
- `OPENAI_EMBEDDING_MODEL`, default `text-embedding-3-small`

The script prints an estimated cost before the API call. The two completed runs were approximately:

- Pilot: 82 chunks, 105,186 estimated tokens, approximately `$0.0021`
- Curated: 471 chunks, 687,537 estimated tokens, approximately `$0.0138`

The script is not yet resumable at chunk granularity and does not delete/reconcile stale chunks if chunking parameters change. Fix this before large-scale reprocessing.

## Migrations

Current head:

```text
0010_case_legal_tags
```

Migration history:

- `0001_case_metadata`: metadata fields and HNSW cosine index
- `0002_raw_ingestion`: nullable summary/embedding, provenance, hashes, processing status, citation fields
- `0003_backfill_processing_status`: labels existing vector records as embedded
- `0004_case_chunks`: chunk storage
- `0005_citation_network`: local citation graph and metrics
- `0006_a2aj_citation_network`: A2AJ citation provenance and mapping
- `0007_fc_procedural_history`: Federal Court IMM history storage
- `0008_case_provenance_tables`: canonical source provenance
- `0009_local_chunk_embeddings`: model-specific local chunk vectors
- `0010_case_legal_tags`: versioned deterministic legal tags and completion state

Run:

```powershell
.\venv\Scripts\python.exe -m alembic upgrade head
```

The application startup still calls `Base.metadata.create_all()`. That is convenient for local development, but migrations should become the authoritative schema mechanism before deployment or shared environments.

## Code review findings addressed in the pause checkpoint

- Added source-type filtering so synthetic data can be excluded from searches.
- Server now computes full-text hashes instead of trusting client values.
- Processing status is derived from actual ingestion behavior rather than caller input.
- Added source-type filtering coverage and hash/status regression coverage.
- Confirmed Pylance diagnostics are clean for touched modules.
- Full focused suite currently passes with 8 tests.

## Known limitations and risks

1. Search quality is not yet benchmarked against human-labeled expected citations.
2. Synthetic records and real A2AJ records coexist in the same database; source filters must be used for meaningful evaluation.
3. Chunk search returns repeated parent cases rather than grouped case results.
4. Local BGE-M3 retrieval has not yet been benchmarked or fully populated.
5. Cases that already own chunks are intentionally skipped; changed source text
  requires an explicit future chunk reconciliation policy.
6. Official Federal Court decision discovery works, but embedded judgment text
  and PDF capture is currently blocked by the source endpoint.
7. Acquisition outputs are staged and require an explicit provenance-preserving
  merge before they become canonical cases.
8. A2AJ texts are unofficial copies with source-specific licensing and possible extraction errors.
9. Text normalization is not yet stored separately from preserved raw text.
10. The API returns full text in case responses, which is inefficient for large judgments.
11. PostgreSQL integration and retrieval-quality tests should be expanded beyond current focused coverage.
12. No grounded RAG generation has been implemented for the broad corpus.

## Recommended next steps

### Phase 1: Complete and observe overnight enrichment

1. Start the safe overnight profile with `--continue-on-error`.
2. Monitor each job log and `state.json`; resume rather than restarting completed jobs.
3. Measure resulting tag, chunk, citation, and local-embedding coverage.
4. Do not run another PostgreSQL writer concurrently.
5. Keep paid OpenAI embedding jobs out of this run.

### Phase 2: Search correctness

1. Benchmark local BGE-M3 retrieval against checked-in expected citations.
2. Group chunk results by parent case, retaining the best passages.
3. Add keyword/full-text search and hybrid ranking.
4. Add explicit chunk reconciliation for changed source text.
5. Expand PostgreSQL integration tests.

### Phase 3: Multi-source identity

1. Use the existing provenance tables and define canonical merge rules for staged FC records.
2. Match official and A2AJ records by citation, title, date, docket, and source ID.
3. Preserve source disagreement instead of silently overwriting values.
4. Import staged records only after validating required text and dates.
5. Keep source-native files and retrieval metadata separate from canonical cases.

### Phase 4: Scale carefully

1. Let resumable chunking and embedding advance as far as the overnight window permits.
2. Re-run retrieval benchmarks at measured coverage checkpoints.
3. Tune local embedding batch size only from observed memory and throughput.
4. Track model version and dimensions for every vector.
5. Avoid paid full-corpus embedding unless explicitly approved and costed.

### Phase 5: RAG

Only after retrieval is measurable:

1. Retrieve grouped case passages.
2. Build citation-preserving context.
3. Generate cautious answers.
4. Return cited cases and source URLs.
5. Test against questions where the expected authorities are known.

## Useful continuation commands

```powershell
# Run tests
.\venv\Scripts\python.exe -m pytest -q

# Check migration state
.\venv\Scripts\python.exe -m alembic current

# Compile project Python
.\venv\Scripts\python.exe -m py_compile backend/*.py scripts/*.py tests/*.py

# Start local API
.\venv\Scripts\python.exe -m uvicorn backend.main:app --reload
```

## Important continuation instruction

Do not delete the synthetic or pilot records without an explicit decision. Do not import the full A2AJ corpus or add RAG next. The project is paused at a useful checkpoint where retrieval evaluation, source filtering, chunk grouping, and multi-source identity should be addressed first.
