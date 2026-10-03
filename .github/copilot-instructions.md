# AI CaseLibrary Coding Instructions

## Project Context

AI CaseLibrary is a Canadian legal research system focused on immigration litigation. It uses FastAPI, SQLAlchemy, PostgreSQL/pgvector, deterministic extraction, source staging, and generated research UI pages.

Read `SYSTEM_REFERENCE.md` for current architecture, `DOCS_INDEX.md` for documentation authority, and the relevant Swimm walkthrough under `.swm/` before changing an owned subsystem.

## Working Rules

- Make one small pull request per issue. Keep the change focused and preserve unrelated worktree changes.
- Use plain language in pull request descriptions. Start with:

  ```text
  Before: <what happened before>
  After: <what changes>
  ```

- Never delete a working feature unless the issue explicitly requires it; preserve existing behavior and compatibility.
- For requests asking for analysis, provide a report file rather than implementing code unless implementation is explicitly requested.
- Agents must not access or operate on the database, deploy or restart the live site, or read or modify `.env` files.

## Tests And Documentation

- Run tests with `python -m pytest -q`. CI deselects three tests:
  - `tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence`
  - `tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes`
  - `tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint`
- `python scripts/check_generated_docs.py` must pass.
- Run the narrowest relevant check first, and report test failures or checks that were not run honestly.
- Do not manually edit generated references; regenerate them from their source.

## Ownership Boundaries

- `backend/main.py`: FastAPI application lifecycle, startup, health, access helpers, and router inclusion.
- `backend/routes.py`: API contracts, request orchestration, database queries, analytics delegation, and generated UI integration.
- `backend/models.py`: Pydantic request and response contracts.
- `backend/database.py`: SQLAlchemy engine, sessions, ORM models, and database configuration precedence.
- `backend/ingestion.py`: provenance-aware canonical create/merge policy.
- `backend/case_processing.py`: ordered metadata, chunk, citation, and statute processing stages.
- `backend/citations.py`: deterministic case/statute extraction, offsets, resolution, and citation metrics.
- `backend/pages/`: page-specific HTML builders used by the active interfaces.
- `alembic/`: deployable schema migrations.
- `scripts/`: acquisition, enrichment, evaluation, operations, and documentation generators.

## Non-Negotiable Invariants

- Keep case citations, statute/instrument references, metadata, tags, and embeddings as separate layers.
- Preserve backend-owned source/chunk offsets; browser code must not invent replacement offsets.
- Keep case-to-case target resolution as a separate local pass after extraction.
- Preserve source identity, provenance, hashes, licence/terms, and merge conflicts.
- Keep IRPA/IRPR nested provisions such as `34(1)(f)` covered by positive, negative, and exact-span tests.
- Treat `/data-explorer` as the active research workflow; `/case-reader` is a compatibility redirect.
- Keep staged, discovered, activity, synthetic, reference-library, and side-project data distinct from canonical judgment records.
- Treat no-index headers as indexing controls, not authentication.

## Validation Rules

Run the narrowest check that can disprove the change before broad validation:

- Citation or statute rule: focused `tests/test_citations.py` tests with exact spans.
- API/search/reader change: relevant `tests/test_api.py` tests and contract validation.
- UI change: `tests/test_feature_tabs.py`, Python compilation, and a browser check.
- Ingestion change: `tests/test_ingestion_merge.py`, importer tests, and a bounded dry run.
- Schema change: affected tests, migration inspection, and schema regeneration.
- Operational change: `--help`, orchestration tests, and preflight/dry-run.
- Documentation change: generated-source check, local-link review, and `git diff --check`.

Never claim the full suite, browser checks, a migration, or a bulk run succeeded unless it actually ran. Record known failures and residual risk honestly.

## Generated And Operational Safety

- Do not manually edit `docs/API_REFERENCE.generated.md`, `docs/SCHEMA_REFERENCE.generated.md`, `docs/SCRIPT_CATALOG.generated.md`, or generated work-history files.
- Do not run competing bulk PostgreSQL writers.
- Use bounded limits, dry-run, preflight, checkpoints, state, logs, and resume support where available.
- Update the relevant canonical documentation and Swimm walkthrough in the same coherent checkpoint.
- Treat Swimm as the source of truth for connected explanation, architecture
	rationale, ownership, and workflow context. Every agent or delegated task must
	update its relevant Swimm walkthrough and canonical repository document before
	the task is marked complete. Code, migrations, generated references, and
	executable runbooks remain authoritative for exact implementation details.
- Prefer small reversible refactors that preserve imports and public contracts until callers and tests have moved.
