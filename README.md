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
- Chunk embeddings are populated for semantic chunk search
- Semantic and hybrid search rollout flags are enabled
- Quick search page is available in-app

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
