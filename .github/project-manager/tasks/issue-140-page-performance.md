# Task: Improve page delivery performance and resilience

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #140's focused page-delivery, caching/compression, page-weight measurement, and loading/error/retry improvements.

Why now: User confirmed issue #140's exact targets: case search, case reader, Citation Intelligence, and FC dashboard; the previously unresolved target list no longer blocks completion.

Owner surface: FastAPI page delivery and the four specified research-page states, with focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing route response/cache contracts and installed runtime dependencies; exact page list confirmed by the user.

Risk boundary: Do not touch database, deployment, or `.env`; preserve download/stream response bodies and headers, existing no-store routes, page behavior, and unrelated worktree changes.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py`

Acceptance criteria:

- Add GZipMiddleware with explicit exceptions for downloads and streams.
- Apply public `max-age=3600` and ETag/If-None-Match to non-personalized static page shells without caching dynamic or no-store responses; no standalone static-file mount currently exists.
- Add a page-weight script and checked-in baseline report.
- Add loading/error/retry states to case search, case reader, Citation Intelligence, and FC dashboard; prevent duplicate searches and preserve filters; make FC dashboard status `aria-live="polite"`.
- Add relevant tests; generated-doc checks pass; update Swimm and canonical documentation.
- Record validation, blockers, and the requested Before/After PR description.

Harness criteria:

- Focused relevant tests pass.
- Generated documentation check and `git diff --check` pass.
- Canonical repository document and relevant Swimm walkthrough are both updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; active UI Swimm walkthrough under `.swm/`; generated documentation checked with `python scripts/check_generated_docs.py`.

Rollback/recovery: Revert only the issue #140 changes; no database or deployment actions are in scope.

Evidence: The continuation completed all four confirmed page-state targets, public one-hour shell caching with conditional ETags, focused regression tests, canonical docs, and Swimm updates. Validation commands and residual browser limitation are recorded below.

Files changed: `.github/project-manager/tasks/issue-140-page-performance.md`; `.swm/1.oi7rhqp2.sw.md`; `.swm/6.maiixtsw.sw.md`; `CHANGELOG.md`; `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `backend/cache_headers.py`; `backend/gzip_middleware.py`; `backend/main.py`; `backend/routes.py`; `backend/pages/data_explorer.py`; `backend/pages/fc_analytics.py`; `backend/pages/research.py`; `scripts/measure_page_weight.py`; `docs/page_weight_baseline.json`; `tests/test_feature_tabs.py`; `tests/test_gzip_middleware.py`; `tests/test_page_weight.py`; generated `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`.
Delegated work: Managed worker `issue-140-ui-states` inspected `backend/routes.py`, `backend/pages/data_explorer.py`, `backend/pages/fc_analytics.py`, and focused tests; changed the two page builders and `tests/test_feature_tabs.py`. It reported four focused UI tests passed, Python compilation and `git diff --check` passed, and no database/browser run. Manager reviewed the diff, added retry for the partial supporting-reader-data failure, adjusted static-shell cache policy, and performed final acceptance.
Focused validation: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py` — 72 passed, 1 skipped. `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` — all 3 references current. `python -m py_compile backend/cache_headers.py backend/pages/data_explorer.py backend/pages/fc_analytics.py tests/test_gzip_middleware.py tests/test_feature_tabs.py` — passed. `node --check -` on the generated Data Explorer wrapper and FC dashboard script — passed. `git diff --check` — passed.
Residual risk: No browser interaction or database-backed suite was run; Playwright and Selenium are not installed, and this task explicitly forbids database access. No deployment or `.env` access occurred.
Next bounded task: Add browser smoke coverage for the four page-state transitions when a DB-independent browser fixture is available.

## Hypothesis

If the delivery changes cache only static non-personalized shells and preserve route-specific behavior, focused API/UI tests will demonstrate conditional one-hour responses, no-store preservation, and stable loading/error/retry states on all four selected pages.

## Plan

1. Delegate the four-page UI state and focused-test implementation.
2. Review the worker diff and complete the public static-shell cache policy.
3. Update canonical repository docs and relevant Swimm walkthroughs, then run focused tests and generated-doc checks.

## Execution Checkpoints

- Delegation: Managed worker returned a structured report for case reader, duplicate search submit, and FC dashboard states; manager validated Citation Intelligence's embedded page and retry behavior.
- Implementation: Static page shells now use public one-hour caching with ETag/If-None-Match and Cookie variance. Search disables duplicates and preserves filters; reader covers full and partial failure retry; Citation Intelligence retains selected-case loading/error/retry states; FC dashboard has polite live status and retry. Explorer CSS/JS are served from the `/static/` mount with cache validators.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md` updated. Generated references checked, not hand-edited.
- Recovery: No long operation, database writes, or deployment involved.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #140 requirements supplied in prompt; GitHub issue body inaccessible in this environment. | `gh issue view 140` failed because `GH_TOKEN` is not configured; worktree initially clean. |
| 2026-10-04 | Clarify the page-state target list | Continue only on the user's specified case search, case reader, Citation Intelligence, and FC dashboard surfaces. | User continuation prompt. |
| 2026-10-04 | Apply public caching to static HTML shells and Explorer assets, not dynamic APIs | Cache only non-personalized shells and static assets; keep explicit no-store paths unchanged. | Route-helper and mounted-asset tests for public max-age, ETag/304, and no-store response behavior. |

## Completion

Completion recorded: yes

Summary: Issue #140's confirmed page-state targets and cache policy are implemented and focused checks pass.

Validation: 72 focused tests passed, 1 skipped; generated-doc check, Python compilation, targeted Node syntax checks, and diff hygiene passed. See Final Evidence for exact commands and documentation paths.

Residual risk: Browser interaction and database-backed suites were not run; Playwright and Selenium are unavailable in the environment. The pytest command used `--noconftest` to avoid the repository conftest's PostgreSQL availability probe.

Next recommended task: Add browser smoke coverage for all four page-state transitions using a DB-independent fixture.

## Final Evidence

- Focused tests: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py` — 72 passed, 1 skipped.
- Page baseline: `PYTHON_DOTENV_DISABLED=1 python scripts/measure_page_weight.py` measured all 25 current HTML builders with deterministic fixtures and wrote `docs/reports/page-weight-baseline.md`.
- Generated references: `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` — passed; all three generated references current.
- Python compile: `python -m py_compile backend/cache_headers.py backend/pages/data_explorer.py backend/pages/fc_analytics.py tests/test_gzip_middleware.py tests/test_feature_tabs.py` — passed.
- UI JavaScript: script-only `node --check -` for the appended Data Explorer wrapper and FC dashboard — passed. Playwright/Selenium browser checks were not available.
- Documentation checkpoint: canonical `SYSTEM_REFERENCE.md`, detailed UI guide `docs/RESEARCH_UI_GUIDE.md`, and Swimm walkthroughs `.swm/1.oi7rhqp2.sw.md` and `.swm/6.maiixtsw.sw.md` updated.
- Diff check: `git diff --check` — passed.
- Before: Reader and FC dashboard failures had no retry; search submits could overlap; static shells revalidated privately; Citation Intelligence and FC states lacked finalized coverage.
- After: Four requested surfaces expose their defined loading/error/retry behavior, search suppresses duplicate submits while retaining filters, FC status is announced politely, and non-personalized static shells and Explorer assets use public one-hour caching with validators. Dynamic APIs and existing no-store responses remain outside those cache policies.

## Main merge follow-up

Merged refreshed `main` after commit `fc90009`. Kept both branches' changelog,
system-reference, and Swimm documentation; regenerated the API, schema, and
script references. Added `backend/cache_headers.py`, `backend/gzip_middleware.py`,
and the moved Explorer static assets to `docs/ARCHITECTURE.md`. The merged main
branch adds the standalone case-comparison page builder, so the offline baseline
now measures 25 builders rather than the original 24. The main-added lazy-loaded
Judge Profile UI remains in the external Explorer asset and its tests now inspect
that asset as well as the HTML shell.

Merge validation: 284 focused, database-independent tests passed and 1 skipped.
`scripts/check_generated_docs.py`, Python compilation, `git diff --check`, and
the architecture inventory contract passed. The full suite remains unrun
because `tests/conftest.py` probes PostgreSQL (`SELECT 1`), prohibited by the
task's no-database boundary.
