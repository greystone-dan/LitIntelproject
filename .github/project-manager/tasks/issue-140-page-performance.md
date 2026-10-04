# Task: Improve page delivery performance and resilience

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #140's focused page-delivery, caching/compression, page-weight measurement, and loading/error/retry improvements.

Why now: Improve research-page responsiveness and resilience while retaining download, stream, and no-store behavior.

Owner surface: FastAPI middleware and generated research pages under `backend/`, with page-delivery tests and a bounded page-weight tool/report.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing route response/cache contracts and installed runtime dependencies; issue requirements are limited to the user-provided prompt because GitHub issue lookup is unavailable.

Risk boundary: Do not touch database, deployment, or `.env`; preserve download/stream response bodies and headers, existing no-store routes, page behavior, and unrelated worktree changes.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py`

Acceptance criteria:

- Add GZipMiddleware with explicit exceptions for downloads and streams.
- Apply cache headers and static ETags where appropriate without weakening no-store routes.
- Add a page-weight script and checked-in baseline report.
- Make only safe lightweight page changes; add loading, error, and retry states to the specified pages. Current scoped changes cover Data Explorer case search and the Research Bench `/research` prototype.
- Add relevant tests; generated-doc checks pass; update Swimm and canonical documentation.
- Record validation, blockers, and the requested Before/After PR description.

Harness criteria:

- Focused relevant tests pass.
- Generated documentation check and `git diff --check` pass.
- Canonical repository document and relevant Swimm walkthrough are both updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; active UI Swimm walkthrough under `.swm/`; generated documentation checked with `python scripts/check_generated_docs.py`.

Rollback/recovery: Revert only the issue #140 changes; no database or deployment actions are in scope.

Evidence: Implementation, documentation, and focused checks are complete for the prompt-confirmed requirements. Full task remains blocked because no page list was supplied and the issue body could not be retrieved; see the blocker below.

Files changed: `backend/main.py`; `backend/gzip_middleware.py`; `backend/cache_headers.py`; `backend/routes.py`; `backend/pages/data_explorer.py`; `backend/pages/research.py`; `scripts/measure_page_weight.py`; `docs/page_weight_baseline.json`; `tests/test_gzip_middleware.py`; `tests/test_page_weight.py`; generated `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`; `SYSTEM_REFERENCE.md`; `CHANGELOG.md`; `.swm/1.oi7rhqp2.sw.md`; `.swm/6.maiixtsw.sw.md`; this task record.
Delegated work: Managed worker `issue-140-implementation` returned a structured report for its runtime/UI slice. Manager review found its original response-header exclusion ineffective and cache helpers unwired; manager repaired the middleware, wired route ETags, added Data Explorer search retry, strengthened tests, and retained the offline-only report scope.
Focused validation: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py` — 71 passed, 1 skipped; generated-doc check passed; changed Python sources compiled; tracked and new-file whitespace checks passed.
Residual risk: Exact target pages in issue #140 could not be confirmed; browser interaction and database-backed suites were not run. A whole-page Node syntax scan found one pre-existing Tag Analytics script syntax error, while both modified scripts pass targeted syntax checks. No database, deployment, or `.env` access was performed.
Next bounded task: Confirm the exact page list for issue #140, then add or adjust loading/error/retry states only on those pages.

## Hypothesis

If the delivery changes preserve route-specific behavior, focused API/UI tests will demonstrate compression and caching only for eligible responses and stable loading/error/retry states on the selected pages.

## Plan

1. Delegate implementation and focused test discovery within the backend delivery/UI surface.
2. Review the diff and worker evidence; repair or narrow the same slice if needed.
3. Update the system reference and active UI/API Swimm walkthroughs, then run focused and documentation checks.

## Execution Checkpoints

- Delegation: Managed worker returned a structured report; manager corrected an ineffective gzip bypass and unwired caching helpers.
- Implementation: Compression, download/stream/no-store bypass, static shell ETags, offline baseline, and two page-state scopes implemented.
- Documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md` updated; generated references regenerated from source.
- Recovery: No long operation, database writes, or deployment involved.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #140 requirements supplied in prompt; GitHub issue body inaccessible in this environment. | `gh issue view 140` failed because `GH_TOKEN` is not configured; worktree initially clean. |
| 2026-10-04 | Keep work blocked on unlisted page targets | Active `/data-explorer` is the primary surface; `/research` is the Research Bench prototype. Do not infer a broader page list. | `SYSTEM_REFERENCE.md` UI ownership; `gh` issue lookup failed for missing token and local issue API returned HTTP 410. |

## Completion

Completion recorded: yes (blocked pending target-page clarification)

Summary: Prompt-confirmed runtime, cache, measurement, page-state, tests, and documentation work is implemented. The precise issue page list remains unverified.

Validation: Focused tests passed: 71 passed, 1 skipped. `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` passed (3 generated references current). `python -m py_compile` passed for modified Python files; `git diff --check` and a new-file whitespace check passed. `node --check` passed for the changed Research and Data Explorer scripts.

Residual risk: No browser test or database-backed suite was run. Tests used `--noconftest` to avoid the repository conftest's PostgreSQL availability probe.

Next recommended task: Confirm issue #140's exact loading/error/retry page targets.

## Blocker

The prompt says “specified pages” but does not name them. `gh issue view 140` could not authenticate (`GH_TOKEN` unavailable), and the configured local issue API returned HTTP 410. The implemented page-state work covers `/data-explorer` case search and the `/research` prototype based on repository UI ownership. Required decision: confirm those are the intended targets or provide the exact route list.

## Final Evidence

- Focused tests: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_gzip_middleware.py tests/test_page_weight.py tests/test_feature_tabs.py` — 71 passed, 1 skipped, 2 dependency deprecation warnings.
- Page baseline: `python scripts/measure_page_weight.py` — passed; offline HTML-only measurements written to `docs/page_weight_baseline.json`.
- Generated references: `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` — passed; all three generated references current.
- Documentation checkpoint: canonical `SYSTEM_REFERENCE.md` and Swimm walkthroughs `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md` updated.
- Changed UI JavaScript: targeted `node --check` — 2 scripts passed. A whole-page check found one unrelated pre-existing Tag Analytics syntax error, also documented by the existing UI walkthrough.
- Diff check: `git diff --check` — passed after whitespace cleanup.
