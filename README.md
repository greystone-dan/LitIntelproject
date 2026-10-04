# iLit (AI CaseLibrary)

iLit is a research tool for Canadian immigration case law. It stores decisions
and their source history, then makes the text searchable and lets researchers
inspect citations, legislation references, extracted case information, and
related analytics. It supports research; it is not legal advice.

This page is a contributor and reviewer entry point. The detailed architecture,
all backend modules, data boundaries, and schema summary are in
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Current behavior is documented in
[SYSTEM_REFERENCE.md](SYSTEM_REFERENCE.md).

## What is available

- **Data Explorer** — the primary interface for About, Case Search, Site
  Architecture, Citation Intelligence, Judge Profile, FC History, and Legal
  Themes & Statutes. Search results open a full-decision reader with stored
  citation, statute, and other evidence.
- **Case and passage search** — text and structured filters, lexical or
  embedding-backed retrieval where vectors exist, and grouped passage results.
- **Citation Map** — explore citation relationships, authorities, paths, and
  related graph analytics.
- **Citation Pass** — inspect deterministic citation and statute extraction
  and source offsets; this is a QA tool, not the normal research workflow.
- **Live Analysis** — inspect DOCX or text-based PDF content in memory and
  optionally resolve extracted citations against local case records. Uploaded
  documents are not saved to the case database.
- **Supporting tools** — saved searches, de-identification, memo citation
  checks, and experimental research or cohort-analysis pages.
- **Source-aware ingestion** — add or merge case records while preserving
  provenance and source identity.

Selected routes are listed below. Their presence and current API contracts are
checked against the generated [API reference](docs/API_REFERENCE.generated.md).

| Route | Purpose |
| --- | --- |
| `GET /data-explorer` | Primary research interface and case reader |
| `GET /case-reader` | Compatibility redirect into Data Explorer |
| `GET /citation-map` | Citation graph workbench |
| `GET /citation-pass` | Extraction and offset QA |
| `GET /live-analysis` | In-memory document review |
| `POST /live-analysis/analyze` | Analyze a supplied document |
| `POST /live-analysis/resolve` | Resolve extracted references locally |
| `GET /quick-search` | Lightweight search interface |
| `POST /search` | Case-level search |
| `POST /search/chunks` | Passage-level search |
| `POST /ingest` | Create a case through the ingestion contract |
| `POST /ingest/merge` | Merge a source record into a case |
| `GET /saved-searches` | List saved searches |
| `POST /research` | Experimental retrieval and answer workflow |

## Run locally

You need Python, PostgreSQL with the `pgvector` extension, and a local database
configured through environment variables. No database credentials are included
in the repository. Optional provider credentials are only needed for workflows
that use those providers; deterministic extraction and most local reads do not
require an AI API key.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m alembic upgrade head
python -m uvicorn backend.main:app --port 8000
```

On Windows, activate the environment with
`.\.venv\Scripts\Activate.ps1`. Configure the database before starting the
application. The server starts locally; open the `/data-explorer` route in a
browser.

## Run tests

The CI test job uses Python 3.12 and installs `requirements-dev.txt`. Run the
same test selection locally:

```bash
pip install -r requirements-dev.txt
python -m pytest -q \
  --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence \
  --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes \
  --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint
```

Those three tests are deliberately deselected in CI: two require a local
PostgreSQL service, and one depends on an Ollama-compatible client setup.
Generated API, schema, and script documentation is checked with:

```bash
python scripts/check_generated_docs.py
```

## Data flow and hosting

Source-specific collectors and staging tools prepare records; validated case
records enter the canonical ingestion and merge policy. PostgreSQL stores the
canonical cases and separate derived layers. Processing extracts chunks,
metadata, citations, statutes, tags, outcomes, and optional embeddings. Search
and analytics services read those layers through the API, and the API serves
the research pages.

The live application and its PostgreSQL/pgvector database run together on one
workstation. The database is not hosted in the cloud. GitHub holds source code
and runs CI; cloud sessions do not connect to the live database.

## Defaults and boundaries

- The password gate is **off by default**. Setting `CASELIBRARY_ACCESS_PASSWORD`
  enables the application gate; it is not a substitute for a separately
  configured network perimeter when one is required.
- The request audit log is **off by default**. Set `CASELIBRARY_AUDIT_LOG` to
  a file path to opt in. Raw client addresses are not logged unless the separate
  raw-address option is explicitly enabled.
- Document size and parsing limits are **on by default**. The
  `LITINTEL_MAX_*` environment variables override limits; they do not turn
  validation off.
- Case citations, legislation references, metadata, tags, and embeddings are
  separate data layers. Staging data, activity data, reference documents,
  synthetic examples, and side-project datasets are not interchangeable with
  canonical case records.

## Repository map

| Location | What it contains |
| --- | --- |
| `backend/` | FastAPI application, routes, data models, database access, processing, search, and pages |
| `alembic/` | Database schema migrations |
| `scripts/` | Ingestion, acquisition, evaluation, documentation, and operations commands |
| `fc_ingest/` | Federal Court source collection and staging |
| `canlaw/` | Local legal-data staging archive and command-line tools |
| `data/` | Local source, reference-library, evaluation, and runtime artifacts; much is not tracked |
| `docs/` | Architecture, source governance, setup, research guidance, and generated references |
| `tests/` | Automated tests |
| `side_projects/` | Independent data utilities outside the canonical case workflow |
| `legacy/` | Archived or reference-only materials |
| `.swm/` | Connected architecture and workflow walkthroughs |
| `.github/` | CI workflows and repository automation |
| `SYSTEM_REFERENCE.md` | Detailed current system and operations reference |

## Further reading

- [Architecture, schema, and source boundaries](docs/ARCHITECTURE.md)
- [Data source and licence register](docs/DATA_SOURCE_REGISTER.md)
- [Generated API reference](docs/API_REFERENCE.generated.md)
- [Generated schema reference](docs/SCHEMA_REFERENCE.generated.md)
- [Current system reference](SYSTEM_REFERENCE.md)
- [Setup guide](SETUP.md)
