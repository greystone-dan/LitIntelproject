# Task: Opt-in local query embeddings

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add opt-in local query embeddings with a dimension guard and a read-only
provider-status endpoint.

Why now: Researchers need a transparent local retrieval option without
silently changing hosted defaults or implying that generation and retrieval
share a provider.

Owner surface: `backend` query embedding selection and its API contract.

Commit allowed: yes

Push allowed: no

Dependencies: Existing OpenAI query embeddings, local SentenceTransformer
provider, local model configuration, current search API.

Risk boundary: Preserve OpenAI as the default; do not access the database,
deploy, read/edit `.env`, download models in tests, or alter stored vectors or
retrieval semantics. Reject incompatible query vector dimensions.

Smallest falsifiable check: `python -m pytest -q tests/test_api.py -k
search_embedding_status` with provider construction mocked.

Acceptance criteria:

- Local query embeddings are opt-in, and the default remains OpenAI.
- Query vectors are dimension-checked before use against the retrieval vector
  contract; incompatible vectors fail in a controlled way.
- `GET /api/search-embedding-status` reports query provider, model, dimensions,
  whether query data leaves the machine, and `TEXT_GENERATION_PROVIDER`.
- Focused tests mock providers and require no model downloads or database.
- Update canonical docs, the Search and Retrieval Swimm walkthrough, and add
  `docs/reports/local-query-embeddings.md`.

Harness criteria: Status route exposes configured retrieval and generation
provider metadata without constructing an embedding model. Local mode selects
the mocked local provider and rejects a dimension mismatch. Existing OpenAI
default remains unchanged.

Docs/generated references: `SYSTEM_REFERENCE.md`,
`.swm/5.b49ftjal.sw.md`, `docs/reports/local-query-embeddings.md`, generated API
reference via `scripts/check_generated_docs.py`.

Rollback/recovery: Revert the additive provider selection, route, tests, and
documentation; no data or schema changes are made.

Evidence: Implemented opt-in query provider and status route; manager's isolated
provider smoke check passed without database or model access. Focused/full
pytest checks could not start because `pytest` is not installed. The generated
documentation check could not regenerate API/schema references because
`fastapi` and `sqlalchemy` are not installed. No database, deploy, `.env` file,
or model download was accessed. Canonical documentation updated:
`SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `DOCS_INDEX.md`, and
`docs/reports/local-query-embeddings.md`; Swimm walkthrough updated:
`.swm/5.b49ftjal.sw.md`.

Files changed: `.env.example`, `.swm/5.b49ftjal.sw.md`, `DOCS_INDEX.md`,
`SYSTEM_REFERENCE.md`, `backend/query_embedding_providers.py`,
`backend/routes.py`, `backend/search_service.py`,
`docs/CONFIGURATION_REFERENCE.md`,
`docs/reports/local-query-embeddings.md`, `tests/test_api.py`, and this task
record.
Implementation was completed by the project-manager agent, which added the
provider module, route, search integration, and mocked tests. Compilation and
diff checks passed; pytest and runtime API checks were unavailable because
dependencies were absent.
Focused validation: Passed `python -m compileall -q
backend/search_service.py backend/query_embedding_providers.py
backend/routes.py tests/test_api.py`, `git diff --check`, targeted added-link
resolution, and an isolated fake-provider smoke test covering OpenAI default,
local provider/status, and rejection of 1024 dimensions against the 1536
indexed contract. Focused and full pytest commands exited before collection with
`No module named pytest`. `python scripts/check_generated_docs.py` failed
because `fastapi` and `sqlalchemy` are unavailable to its generators.
Residual risk: Pytest/API route tests and generated-reference consistency remain
unverified in this dependency-free environment. The default BGE-M3 query vector
is 1024-dimensional and is incompatible with the current 1536-dimensional
standard semantic index; the guard rejects it. Equal dimensions alone do not
prove embedding-model compatibility. A broader local-vector retrieval change is
not part of this issue.
Next bounded task: Run the focused API tests and generated-doc check in a
dependency-equipped, DB-isolated CI environment before treating the task as
complete.

## Hypothesis

If query-provider selection is additive and validates the returned vector
dimension, mocked API tests will demonstrate the local opt-in and status
transparency while the default stays OpenAI.

## Plan

1. Implement isolated query-provider selection, dimension guard, and status API. Done.
2. Add no-download mocked tests and the requested report. Done.
3. Update canonical and Swimm docs; run focused tests and required checks. Tests
   and generated-doc check are blocked by unavailable dependencies.

## Execution Checkpoints

- Implementation: Added provider selection, route, search integration, and
  mocked API tests; compilation and diff checks passed, but pytest was
  unavailable because dependencies were absent.
- Implementation: `backend/query_embedding_providers.py`,
  `backend/search_service.py`, and `backend/routes.py`; provider smoke check
  confirms the default/local selection and dimension guard without model or DB.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`,
  `DOCS_INDEX.md`, `.env.example`, `docs/reports/local-query-embeddings.md`,
  and `.swm/5.b49ftjal.sw.md` updated.
- Recovery: No persistent state or database operation. Latest `origin/main`
  (`fc90009`) was fetched and verified as an ancestor of current `HEAD`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use the current merged-main feature branch as the start point | User confirms latest main was just merged by parent; working tree was clean | `git status --short --branch`; HEAD is merge commit `a93abdb` |
| 2026-10-04 | Keep OpenAI default and separate retrieval from generation | Preserve existing behavior and make local-query data flow explicit | Provider settings/status implementation and mocked tests |

## Completion

Completion recorded: no

Summary: Implementation and documentation are present, but acceptance is
blocked until pytest/API and generated-reference validation run in an
environment with dependencies and no database access.

Validation: `compileall`, `git diff --check`, targeted documentation-link check,
and isolated mocked provider/dimension smoke test passed. Focused/full pytest
and `scripts/check_generated_docs.py` did not run successfully because
dependencies are missing.

Residual risk: Same-dimension but semantically incompatible model spaces are not
detectable from dimensions alone; local BGE-M3 is not compatible with the
current hosted semantic index.

Next recommended task: Run focused API tests and generated-doc check in a
dependency-equipped, DB-isolated CI environment.
