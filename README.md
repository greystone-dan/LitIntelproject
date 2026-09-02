# AI CaseLibrary

AI CaseLibrary is a Canadian legal research system focused on immigration litigation workflows.
It collects court decisions and legal reference materials, preserves source provenance, and adds searchable structure (metadata, chunks, citations, tags, and embeddings).

This project is a research aid, not legal advice.

For the complete, current architecture, system behavior, data model, operational
workflows, API map, limitations, and code-review posture, read
[SYSTEM_REFERENCE.md](SYSTEM_REFERENCE.md). It is the canonical system document.

## What This Repo Provides

- FastAPI backend for case ingestion, search, retrieval, case reading, analytics, and citation exploration
- PostgreSQL + pgvector canonical case store
- Source staging pipelines for A2AJ and Federal Court collection workflows
- Paragraph chunking and citation-network processing
- Search and reader UIs for decisions, analytics, and citation QA
- Isolated side-project utilities that can store separate datasets without entering the canonical case workflow

## Current Status

- Canonical case store is populated and searchable
- Advanced search UI is live at `/data-explorer` with filters, minister dropdown, result metrics, and a full-decision modal reader
- Unified case detail is live at `/case-reader`
- Citation graph analytics are live under `/citation-map/*`
- Citation extraction and local target resolution are both populated in the database
- Citation Pass remains available as the deterministic QA surface for extraction debugging
- The isolated Luck of the Draw III utility lives under `side_projects/luck_of_the_draw_iii` and writes only to schema `lotd`

Current live scale in the main case library database:

- 35,902 canonical cases
- 35,856 cases with full text
- 1,390,886 paragraph chunks
- 1,492,628 stored citation rows
- 760,197 citations linked to a target case
- 31,944 unique linked target cases
- Reader metadata coverage: 31,340 judges, 31,449 decision outcomes, 27,230 government outcomes

## Current Workflow

Use the repo in three distinct modes:

1. Research workflow: `/data-explorer` for advanced search, filters, analytics tabs, and full-decision reading.
2. Case inspection workflow: `/case-reader` for unified case detail, stored citations, chunks, sources, and metrics.
3. Extractor QA workflow: `/citation-pass` when validating citation extraction offsets or layered extractor behavior.

Core research-facing capabilities now available:

1. Search cases by text, cited authority, minister/government party, judge, court, year, government outcome, and decision outcome.
2. Sort search results by citation relevance, date, or minister.
3. Open full decisions in a modal reader with stored citation highlights.
4. See per-case citation metrics such as total citation mentions, unique cited authorities, and linked target cases.
5. Review judge-outcome summaries and flexible two-field analytics in the same `/data-explorer` surface.
6. Explore citation graph, authority flow, lifecycle, surprises, hidden bridges, and contextual exports under `/citation-map/*`.
7. Run deterministic extraction QA in `/citation-pass` without mixing statute/instrument and case-citation decisions.

### Day-To-Day Commands

Start API:

~~~powershell
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8070
~~~

Open UI:

- http://127.0.0.1:8070/data-explorer

Focused citation tests:

~~~powershell
./venv/Scripts/python.exe -m pytest tests/test_citations.py -q
~~~

Optional full test sweep:

~~~powershell
./venv/Scripts/python.exe -m pytest -q
~~~

Primary success criteria for this phase:

- Advanced search returns stored case-level citation evidence quickly enough to open heavily cited decisions interactively.
- Stored citation rows retain chunk location and offset integrity.
- Case-to-case target resolution remains a separate local pass after extraction.
- Statute/instrument and metadata layers remain separate from case-citation QA decisions.

## Legacy Separation

To keep the project less scattered, legacy materials are explicitly separated:

- `legacy/` for archived artifacts and legacy workflow references
- `backend/legacy/` for modules intentionally excluded from active runtime paths
- `docs/history/` for historical implementation notes

Default active path for research is `/data-explorer` plus `/case-reader`; Citation Pass is the verification path.

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
- [side_projects](side_projects): isolated non-core dataset utilities and outputs
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

## Primary Interfaces

- `GET /data-explorer`: single-page research interface with About, Case Search,
  Citation Intelligence, Judge Outcomes, Judge Profile, and Data Explorer tabs
- `GET /about`: compatibility redirect to the About tab
- `GET /citation-intelligence`: compatibility redirect to Citation Intelligence
- `GET /judges`: compatibility redirect to Judge Profile
- `GET /case-reader`: unified case detail reader
- `GET /citation-pass`: extractor QA surface
- `GET /citation-map`: citation graph workbench
- `GET /quick-search`: lightweight lexical/semantic search page

## Quick Search Testing

### Browser UI

For the proof of concept, keep the site to one UI and continue citation verification on the existing metadata and chunking base. Do not re-ingest the 300-case review list yet.

After server startup, open:

- http://127.0.0.1:8000/quick-search

If port 8000 is already in use, run on another port and open the matching URL.

### Terminal Semantic Search

~~~powershell
python -m scripts.quick_search_engine "non-refoulement risk on return" --limit 10
~~~

## Local Domain Hosting (Cloudflare Tunnel)

If you want to expose your local app through your own domain while it runs on your machine:

1. One-time setup:

~~~powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup_cloudflare_tunnel.ps1 -Hostname your.domain.com -TunnelName aicaselibrary-local -LocalPort 8070
~~~

2. Start app + tunnel:

~~~powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_local_with_tunnel.ps1
~~~

See [docs/CLOUDFLARE_TUNNEL_SETUP.md](docs/CLOUDFLARE_TUNNEL_SETUP.md) for details.

## Useful Endpoints

- GET / : backend health message
- GET /data-explorer : six-tab immigration litigation intelligence UI
- GET /api/about/stats : live About-page library statistics
- GET /api/citation-intelligence/{case_id}/overview : citation overview metrics
- GET /api/citation-intelligence/{case_id}/table : citation evidence table
- GET /api/judge-profiles : canonical judge profile list
- GET /api/judge-profiles/{slug} : selected judge profile and linked cases
- GET /analytics/search/cases : filtered case search API
- GET /analytics/search/ministers : minister dropdown source API
- GET /analytics/search/cases/{case_id} : full-decision reader payload with citation highlights and metrics
- GET /case-reader : unified case detail UI
- GET /quick-search : lightweight semantic/hybrid search page
- GET /citation-pass : citation QA UI
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
- The Luck of the Draw III side project stores its imported tables in PostgreSQL schema `lotd`, not in the canonical case tables.

## GitHub and Large Files

This repository excludes oversized local backup archives from tracking.
If you generate large local archives in [backups](backups), keep them out of Git history.

## Core Documentation

- [SYSTEM_REFERENCE.md](SYSTEM_REFERENCE.md): canonical current architecture, functionality, data model, operations, and limitations
- [SYSTEM_OVERVIEW.txt](SYSTEM_OVERVIEW.txt): plain-language system state
- [SETUP.md](SETUP.md): environment and workstation setup
- [OVERNIGHT.md](OVERNIGHT.md): unattended operation guide
- [DOCS_INDEX.md](DOCS_INDEX.md): document authority map
- [CHANGELOG.md](CHANGELOG.md): milestone and feature changes
- [ROADMAP.md](ROADMAP.md): forward plan for missing features and QA
- [side_projects/luck_of_the_draw_iii/README.md](side_projects/luck_of_the_draw_iii/README.md): isolated LotD dataset utility

## Historical Notes

Historical AI handoff documents were moved to [docs/history](docs/history) to keep the repository root focused on active operational docs.

## License and Usage

Use according to upstream data source licenses and your organizational policy.
Always verify critical legal findings against authoritative records.
