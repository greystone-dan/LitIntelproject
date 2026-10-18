# Task: Issue #548 Cleanup 7

Status: blocked
Created: 2026-10-17
Updated: 2026-10-17

## Task Record

Task: Remove only evidence-backed dead/duplicate backend code and packages that are not consumed or intentionally installed.

Why now: Issue #548 requests a final cleanup pass while preserving all live routes, runtime imports, and explicitly required dependencies.

Owner surface: Backend dead-code and dependency cleanup.

Commit allowed: yes

Push allowed: yes, through the requested progress workflow if available.

Dependencies: Current import/use evidence across application code, scripts, ingestion, tests, image builds, and workflows.

Risk boundary: Do not remove runtime startup imports, routes, dynamic/plugin imports, dependencies installed for an explicit workflow, or alter behavior. Do not access a database, deploy, or touch environment files.

Smallest falsifiable check: Repository-wide reference/import evidence for each proposed removal, followed by focused tests and generated-document validation.

Acceptance criteria:

- Every deleted backend file/symbol and removed requirement has exact use/import evidence across the scoped repository surfaces.
- Live route behavior, startup imports, and explicitly justified package installs remain unchanged.
- Targeted tests, full pytest, generated-doc check, secret scan, and parallel validation are run or their unavailability/blocker is recorded honestly.
- Canonical documentation and the relevant Swimm walkthrough are updated; generated references are regenerated where required.

Harness criteria: Not used; repository `parallel_validation` integration is not exposed in this session.

Docs/generated references: `docs/ARCHITECTURE.md` or `SYSTEM_REFERENCE.md` as applicable, `.swm/system-map.ovnldklv.sw.md`, generated API/schema/script references via `scripts/check_generated_docs.py`.

Rollback/recovery: Restore only the narrowly removed symbol/module/requirement from the diff; no data migration or runtime operation is involved.

Evidence: Starting worktree was clean on `copilot/cleanup-dead-and-duplicate-modules` at `a9a65d8`, parent `09b901d`. Two managed-worker returns established the implementation and candidate dispositions. Scoped `git grep` and import-name checks found no package imports in `backend/`, `scripts/`, `fc_ingest/`, `canlaw/`, or `tests/`; the removal evidence is summarized in the pull request description. Live route, comparison, tagger, startup, and explicitly justified packages were retained. No database, deployment, or environment file was accessed.

Files changed: `.github/project-manager/tasks/issue-548-cleanup-7.md`; `.swm/system-map.ovnldklv.sw.md`; `docs/ARCHITECTURE.md`; `backend/contextual_intelligence.py`; `backend/routes.py`; deleted `backend/unit_search.py` and `backend/vector_tables.py`; `requirements.txt`; deleted `tests/test_unit_search_e2e.py`, `tests/test_unit_search_model.py`, and `tests/test_vector_tables.py`.
Delegated work: the route-local unused whitespace helper, `ProximityCluster`, and 14 unused `requirements.txt` entries were removed after reviewing use and install surfaces. The deprecated `backend/unit_search.py`, unused `backend/vector_tables.py`, and only their direct tests were removed; both case-comparison modules and all tagger versions with live consumers were retained.
Focused validation: `python -m py_compile backend/contextual_intelligence.py backend/routes.py` passed. `python -c 'from scripts.regenerate_docs import sync_inventory; ...'` reported no added/removed backend inventory rows. `git diff --check`, Swimm local-link/trailing-whitespace checks, and the changed-file high-confidence secret scan passed (7 files scanned, no matches). `PYTHON_DOTENV_DISABLED=1 python -m pytest tests/test_unit_keyword_search.py -q` and `PYTHON_DOTENV_DISABLED=1 python -m pytest -q` both stopped before collection with `No module named pytest`. `PYTHON_DOTENV_DISABLED=1 python scripts/regenerate_docs.py` stopped at `No module named fastapi`; `python scripts/check_generated_docs.py` failed because `fastapi` and `sqlalchemy` are absent. `ruff --select F401,F841` and vulture were unavailable. No database access was made.
Residual risk: Full/focused pytest, API/schema/script reference regeneration and generated-doc check, dependency audit, and Ruff/vulture checks remain unvalidated because required packages/tools are absent. The Anthropic Compose/deployment-guide environment settings remain as a separate stale-config question; no Python provider consumes them. Static searches cannot rule out undocumented external consumers. Commit/push and `report_progress` were not run.
Next bounded task: In an approved isolated Python environment with pytest and the repository’s runtime dependencies, guard PostgreSQL access, run the focused and full pytest suite plus `scripts/regenerate_docs.py`/`check_generated_docs.py`, then resolve this validation blocker.

## Hypothesis

If only private backend symbols and packages with no repository/runtime-install consumer are removed, the application’s route/startup contracts remain intact and the targeted plus full pytest and generated-doc checks pass.

## Plan

1. Inventory issue-named candidate modules and requirements across application, scripts, ingestion, tests, Docker, workflows, and iLitSite startup; inspect dynamic imports and explicit install reasons.
2. Remove only candidates whose lack of use is established, preserving all ambiguous or live items. (Complete.)
3. Run the narrowest affected tests, then requested full pytest and documentation/security validation; update canonical and Swimm documentation. (Documentation/security/static checks passed; pytest and generated-doc checks blocked by missing dependencies.)

## Execution Checkpoints

- Delegation: Two managed workers returned structured findings for dependency/helper removals and issue-named backend candidates; removal evidence is summarized in the pull request description.
- Implementation: Removed only the unreferenced code/modules/tests and 14 unused base requirements; no routes or startup imports changed.
- Documentation: Updated `docs/ARCHITECTURE.md` and Swimm `.swm/system-map.ovnldklv.sw.md`. `scripts/regenerate_docs.py` and `scripts/check_generated_docs.py` were attempted but blocked by missing FastAPI/SQLAlchemy.
- Recovery: Not applicable; no database or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-17 | Created a bounded cleanup task; defer candidate selection to repository-wide evidence | Existing report covers only prior backend symbols, while issue scope also includes explicit modules, requirements, and install surfaces | Clean worktree; existing inventory, ownership docs, and public issue body reviewed |
| 2026-10-17 | Keep the issue base; do not merge the fetched later main commit | Latest remote main was committed four minutes after the supplied task time | Shared base `09b901d`; `origin/main` `b731411f` timestamp `17:37Z`; task time `17:33Z` |
| 2026-10-17 | Mark task blocked after implementation and docs | Required tests and generated-doc checks cannot start without missing runtime/test packages; pytest collection would otherwise probe PostgreSQL | Focused/full pytest and both docs commands attempted; failure evidence recorded above |

## Completion

Completion recorded: no

Summary: Evidence-backed code/dependency cleanup and documentation are complete. Task status is blocked because focused/full pytest and generated reference validation could not run in this environment.

Validation: Python compilation, architecture inventory synchronization, whitespace/link checks, and changed-file secret scan passed. Pytest commands failed before collection because pytest is absent. Docs generator/check failed because FastAPI and SQLAlchemy are absent.

Residual risk: No pytest or generated-doc pass is claimed; no database, deployment, or environment files were accessed.

Next recommended task: Run the blocked test and documentation checks in an isolated dependency-complete environment with PostgreSQL connections prohibited.
