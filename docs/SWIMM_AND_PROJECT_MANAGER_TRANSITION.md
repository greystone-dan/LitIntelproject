# Swimm Documentation And Project Manager Transition

Last reviewed: 2026-09-03

## Purpose

This document is the bridge between the current hand-maintained documentation
set and a future Swimm workspace plus project-manager agent workflow.

Swimm should document and connect the implementation that exists. It should
not become a second source of truth for live counts, API contracts, database
schema, or operational commands. Those remain owned by the documents and
generators listed in `DOCS_INDEX.md`.

## Recommended Swimm Pass

Create or import the following walkthroughs in this order. Keep each walkthrough
small enough that a future code change can update it without rewriting the
whole project map.

| Walkthrough | Starting point | What it should explain | Owner |
| --- | --- | --- | --- |
| System map | `backend/main.py` | Application startup, route registration, and health surface | Backend/runtime |
| Research request | `backend/routes.py` | Search request to query, reader payload, and UI response | API/research UI |
| Processing pipeline | `backend/case_processing.py` | Metadata, chunks, citations, and statutes as separate stages | Data quality |
| Source-to-canonical flow | `backend/ingestion.py` | Staging, provenance, merge priority, and canonical writes | Ingestion |
| Citation evidence | `backend/citations.py` | Extraction, offsets, resolution, metrics, and QA boundaries | Citation QA |
| Database map | `backend/database.py` and `alembic/` | ORM entities, migrations, and pgvector responsibilities | Data/platform |
| Operational run | `scripts/run_overnight.py` and `OVERNIGHT.md` | Locks, bounded jobs, resume behavior, and recovery | Operations |
| Active UI | `backend/routes.py` and `docs/RESEARCH_UI_GUIDE.md` | Data Explorer, inline reader, Citation Map, and legacy boundaries | Research UI |

For every walkthrough, include: entry point, important files, data passed
between steps, invariants, failure modes, and the narrowest validation command.
Prefer links to source files and generated references over copied code blocks.

## Repository Map

```mermaid
flowchart TD
    Sources[Official, A2AJ, CanLII, local sources] --> Staging[fc_ingest, canlaw, scripts]
    Staging --> Ingest[backend/ingestion.py]
    Ingest --> DB[(PostgreSQL + pgvector)]
    DB --> Process[backend/case_processing.py]
    Process --> Metadata[metadata and legal tags]
    Process --> Chunks[chunks and embeddings]
    Process --> Cases[citation extraction]
    Process --> Statutes[IRPA/IRPR and statute references]
    Cases --> Resolve[target resolution and graph metrics]
    DB --> API[backend/main.py + routes.py]
    Resolve --> API
    Statutes --> API
    API --> Explorer[/data-explorer/]
    API --> QA[/citation-pass/]
    API --> Map[/citation-map/]
    API --> Live[/live-analysis/]
```

### Ownership Boundaries

| Concern | Owning surface | Must remain true |
| --- | --- | --- |
| Application startup | `backend/main.py` | Startup and route behavior are validated independently of UI markup |
| API and generated UI | `backend/routes.py` | Browser-owned offsets are never substituted for backend evidence offsets |
| Case citations | `backend/citations.py` | Case citations stay separate from statutes and metadata |
| Statutes/instruments | `backend/citations.py` | IRPA/IRPR nested forms such as `34(1)(f)` remain release-sensitive |
| Canonical data | `backend/database.py`, `backend/ingestion.py` | Provenance, source priority, and hashes are preserved |
| Schema evolution | `alembic/` | Migrations are authoritative for deployment changes |
| Operational jobs | `scripts/run_overnight.py`, `OVERNIGHT.md` | Bulk work is bounded, resumable, and lock-protected |
| Active research workflow | `/data-explorer` | `/case-reader` is a compatibility redirect; QA pages are not the primary product |
| Isolated data | `side_projects/` | Side-project tables and routes do not enter canonical case workflows |

## Improvement Queue Before Agent Handoff

Use this queue as the initial Swimm-linked improvement board. Do not broaden
scope until each item has an owner, a test, and a documented acceptance check.

| Priority | Improvement | Evidence of completion |
| --- | --- | --- |
| P0 | Repair or reconcile the known FC document-scraper test collection error | Full suite collects and the result is recorded honestly |
| P0 | Add browser smoke coverage for Data Explorer and inline reader | Playwright checks load, search, reader open/close, highlights, and mobile layout |
| P0 | Establish a deterministic data-quality report | Orphans, malformed citations, duplicate edges, and null metadata are measured |
| P0 | Keep IRPA/IRPR extraction precise | Nested section forms, including `34(1)(f)`, have positive, negative, and offset fixtures |
| P1 | Add retrieval and endpoint performance baselines | Fixed corpus/sample reports p50/p95 and bounded query behavior |
| P1 | Add citation context evidence | Context windows are persisted, exposed, and covered by exact-span tests |
| P1 | Reduce documentation drift | Generated references are refreshed by a documented checkpoint command |
| P2 | Build a research workbench | Save/resume, notes, pinned authorities, and evidence exports have route and UI contracts |

## Handoff Contract For A Future Project Manager Agent

The future manager agent should coordinate work, not silently redefine domain
truth. Every proposed task should carry this compact record:

```text
Task:
Why now:
Owner surface:
Dependencies:
Risk boundary:
Smallest falsifiable check:
Acceptance criteria:
Docs or generated references to refresh:
Rollback or recovery:
Evidence:
```

The manager loop is:

1. Read `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`,
   this document, and the relevant Swimm walkthrough before assigning work.
2. Choose one owning surface and state one falsifiable behavior expectation.
3. Assign the smallest implementation slice and its focused validation command.
4. Require evidence before marking the task complete: test output, generated
   documentation, or a bounded browser/API check as appropriate.
5. Update the relevant canonical document and Swimm walkthrough in the same
   checkpoint.
6. Keep unrelated worktree changes intact and record blockers rather than
   disguising them as completed work.

### Manager Guardrails

- Never treat generated API/schema/script documents as hand-edit targets.
- Never run competing bulk database writers.
- Never call staged, discovered, or activity data an official captured judgment.
- Never merge statute extraction into case-citation extraction.
- Never claim a full-suite or browser result that was not actually run.
- Never let an agent expand a task beyond its stated owner surface without a
  new acceptance check.

## Swimm Maintenance Rule

When a change crosses one of the ownership boundaries above, update the linked
walkthrough and the canonical repository document in the same change set. If a
walkthrough becomes stale, label the gap and point to the authoritative source;
do not preserve a visually complete but inaccurate diagram.

The first practical Swimm session should produce the eight walkthroughs above,
link them to the named source files, and then use the P0 queue to drive the
project cleanup. Only after that map is reviewed should an operational
project-manager agent scaffold be introduced.