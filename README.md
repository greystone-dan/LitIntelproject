# AI CaseLibrary

AI CaseLibrary is a Canadian legal research system focused on immigration litigation workflows.
It collects court decisions and legal reference materials, preserves source provenance, and adds searchable structure (metadata, chunks, citations, tags, and embeddings).

This project is a research aid, not legal advice.

## What This Repo Provides

- FastAPI backend for case ingestion, search, retrieval, and citation exploration
- PostgreSQL + pgvector canonical case store
- Source staging pipelines for A2AJ and Federal Court collection workflows
- Case chunking and semantic embeddings
- Legal tag extraction and citation network processing
- Quick semantic search UI for manual testing

## Current Status

- Canonical case store is populated and searchable
- Citation graph analytics are live, including authority, path, missing-authority, lifecycle, and surprise surfaces
- Chunk embeddings are populated for semantic chunk search
- Semantic and hybrid search rollout flags are enabled
- Quick search page is available in-app

Current live scale is large enough for serious QA and graph analysis: 35,902 cases, 168,282 chunks, 303,816 citations, 770,395 tags, 5,808 chunk embeddings, and 429 case embeddings.

## Citation Stabilization Scope (Current)

- Active extraction hardening is focused on case-to-case citations.
- Citation-pass review should be driven by live extraction output from case citations, not statute or convention filtering overlays.
- Statute/instrument extraction remains available as a separate layer and should not be mixed into case-only QA decisions.
- Do not start a broad 300-case re-ingest/rebuild until citation-pass reliability gates are satisfied.

## Main Workflow (Canonical)

Use this sequence as the default operating path before touching side scripts or broader reprocessing.

1. Run the API locally.
2. Open Citation Pass and review layered extraction output for the selected cohort case.
3. Validate exact text spans and offsets first, then normalized citation quality.
4. Add or update deterministic extractor rules and tests.
5. Re-run focused tests, then cohort checks, then update docs/changelog.
6. Commit and push only after the extraction/UI pass is reproducible.

### Day-To-Day Commands

Start API:

~~~powershell
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8070
~~~

Open UI:

- http://127.0.0.1:8070/citation-pass

Focused citation tests:

~~~powershell
./venv/Scripts/python.exe -m pytest tests/test_citations.py -q
~~~

Optional full test sweep:

~~~powershell
./venv/Scripts/python.exe -m pytest -q
~~~

Primary success criteria for this phase:

- Case citations are captured with exact source spans.
- Paragraph pinpoints (for example, "at para. 10" / "at paras. 37 and 44") are preserved with the citation context.
- Statute/instrument and metadata layers remain separate from case-citation QA decisions.

## Legacy Separation

To keep the project less scattered, legacy materials are explicitly separated:

- `legacy/` for archived artifacts and legacy workflow references
- `backend/legacy/` for modules intentionally excluded from active runtime paths
- `docs/history/` for historical implementation notes

Default active path remains Citation Pass and deterministic extraction hardening.

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL + pgvector
- OpenAI embeddings and local embedding support
- Pytest test suite

See [requirements.txt](requirements.txt) for pinned dependency versions.

## Repository Layout

- [backend](backend): API routes, models, database layer, retrieval logic
- [scripts](scripts): ingestion, chunking, embeddings, evaluation, and operational scripts
- [fc_ingest](fc_ingest): Federal Court source-specific staging pipeline
- [alembic](alembic): schema migrations
- [tests](tests): automated tests
- [data](data): evaluation artifacts, staging outputs, and runtime data folders
- [canlaw](canlaw): source staging helpers and related tooling

## Quick Start

1. Clone and enter the project

~~~bash
git clone https://github.com/greystone-dan/LitIntelproject.git
cd LitIntelproject
~~~

2. Create and activate virtual environment

~~~powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
~~~

3. Install dependencies

~~~powershell
pip install -r requirements.txt
~~~

4. Configure environment

- Copy [.env.example](.env.example) to .env
- Fill database and API credentials

5. Run migrations (if needed)

~~~powershell
alembic upgrade head
~~~

6. Start API

~~~powershell
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
~~~

## Quick Search Testing

### Browser UI

## Azure Hosting

This project is set up to run as one web app. See [docs/AZURE_DEPLOYMENT.md](docs/AZURE_DEPLOYMENT.md) for the Docker-based Azure path using Azure Container Apps or Azure App Service plus Azure PostgreSQL.

For the proof of concept, keep the site to one UI and continue citation verification on the existing metadata and chunking base. Do not re-ingest the 300-case review list yet.

After server startup, open:

- http://127.0.0.1:8000/quick-search

If port 8000 is already in use, run on another port and open the matching URL.

### Terminal Semantic Search

~~~powershell
python -m scripts.quick_search_engine "non-refoulement risk on return" --limit 10
~~~

## Useful Endpoints

- GET / : backend health message
- GET /quick-search : lightweight semantic/hybrid search page
- POST /search : case-level search
- POST /search/chunks : chunk-level search
- POST /search/chunks/grouped : grouped passage retrieval by case
- GET /testing : API testing page
- GET /research : research interface page

## Data and Provenance Notes

- Preserve source first, enrich second
- Canonical data lives in PostgreSQL
- Staging data may exist in SQLite/Parquet/JSON artifacts
- Reference library documents are stored separately from canonical cases
- Citation rows are stored as chunk-backed `Citation` records with offsets and normalized text; the citation record itself does not carry a dedicated timestamp column, so timing is inferred from the owning case and chunk timestamps.

## GitHub and Large Files

This repository excludes oversized local backup archives from tracking.
If you generate large local archives in [backups](backups), keep them out of Git history.

## Core Documentation

- [SYSTEM_OVERVIEW.txt](SYSTEM_OVERVIEW.txt): plain-language system state
- [SETUP.md](SETUP.md): environment and workstation setup
- [OVERNIGHT.md](OVERNIGHT.md): unattended operation guide
- [DOCS_INDEX.md](DOCS_INDEX.md): document authority map
- [CHANGELOG.md](CHANGELOG.md): milestone and feature changes
- [ROADMAP.md](ROADMAP.md): forward plan for missing features and QA

## Historical Notes

Historical AI handoff documents were moved to [docs/history](docs/history) to keep the repository root focused on active operational docs.

## License and Usage

Use according to upstream data source licenses and your organizational policy.
Always verify critical legal findings against authoritative records.
