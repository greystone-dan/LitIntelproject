# Task: Isolate Discussion Unit search and reader sandbox

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Add a read-only experimental search and reader limited to the Discussion Unit core 300 cohort.

Why now: The paragraph and grouped experiments need a safe research surface without changing the active reader or full inventory search.

Owner surface: `backend/discussion_units_sandbox.py`, `backend/pages/discussion_units_sandbox.py`, and sandbox routes in `backend/routes.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: The read-only `discussion_unit_core_300.csv` manifest and existing `build_case_reader_data` service.

Risk boundary: Do not modify `/data-explorer`, `/case-reader`, production analytics search routes, database schema, or the active paragraph assessment run.

Smallest falsifiable check: `venv\\Scripts\\python.exe -m py_compile backend/discussion_units_sandbox.py backend/pages/discussion_units_sandbox.py backend/routes.py`.

Acceptance criteria:

- Sandbox search uses the same advanced controls, suggestions, sorting, and reader workflow as the main case surface.
- Sandbox search returns only manifest case IDs.
- Non-cohort reader requests return 404.
- Reader highlighting, modes, subtabs, evidence controls, linked context, and activity/statute views use the same renderer and sandbox endpoints.
- Existing production routes remain unchanged.
- Focused API and browser checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`; generated API references must be regenerated if the route is included.

Rollback/recovery: Remove the sandbox module, page, imports, routes, tests, and this task record; no data rollback is required.

Evidence: Delegated read-only comparison completed. The sandbox now reuses the production Data Explorer HTML/JavaScript renderer with sandbox endpoint substitutions and cohort-scoped SQL search. Validation: 48 tests passed, compilation passed, route registration passed, and git diff check passed. The active paragraph assessment run was not touched.

## Hypothesis

If the cohort manifest is enforced before search and reader assembly, the sandbox can reuse source-preserving reader data while preventing access outside the 300-case experiment.

## Plan

1. Add manifest validation and read-only cohort search helper.
2. Reuse the full production search/reader renderer with sandbox endpoint configuration.
3. Add focused parity tests, documentation, and route validation.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager, read-only route and ownership exploration.
- Implementation: `backend/discussion_units_sandbox.py`, cohort-aware search in `backend/analytics_service.py`, shared renderer wiring in `backend/routes.py`, and Sandbox navigation in `backend/pages/data_explorer.py`; focused checks passed.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md` updated.
- Recovery: no long-running operation; active paragraph run remains outside this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-24 | Use separate sandbox routes and page | Preserve production search and reader behavior while experimenting | User request and delegated route inspection |

## Completion

Completion recorded: yes

Summary: Added a full-parity read-only search and reader sandbox limited to the Discussion Unit core 300 cohort. Production search and reader contracts remain unchanged; the main shell gains only a Sandbox navigation link.

Validation: `py_compile` passed; `tests/test_discussion_units_sandbox.py tests/test_api.py` passed with 48 tests; route table check passed; `git diff --check` passed.

Residual risk: The Sandbox includes the full production Case Search/reader surface, but unrelated top-level analytics tabs remain visually present in the shared renderer and are not part of the cohort experiment contract.

Next recommended task: Review the 300-case reader behavior and decide which Discussion Unit overlays should be added without changing the parity baseline.
