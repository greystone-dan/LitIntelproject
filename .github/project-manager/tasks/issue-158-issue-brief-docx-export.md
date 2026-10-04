# Task: Add issue-brief DOCX export

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add `GET /issue-brief.docx` for the same tag-filtered facts exposed on the printable issue-brief page.

Why now: Issue #158 requests a portable, traceable DOCX version of the existing legal issue brief.

Owner surface: Issue brief route and renderer (`backend/routes.py`, `backend/pages/issue_brief.py`).

Commit allowed: no

Push allowed: no

Dependencies: Existing `fetch_issue_brief` payload and filtered-search DOCX construction conventions; issue text could not be fetched (GitHub returned 403).

Risk boundary: Read-only export only; preserve current `tag` bounds, page/JSON behavior, taxonomy/outcome/citation semantics, and no-store response behavior. Do not access a database outside isolated tests.

Smallest falsifiable check: `python -m pytest tests/test_issue_brief.py -q`

Acceptance criteria:

- `GET /issue-brief.docx` accepts the same `tag` parameter and calls the same `fetch_issue_brief` data source as the page.
- DOCX includes the facts and traceable links displayed by the page, including empty-state behavior, plus a footer beginning `Generated from iLit data on` and a generated date.
- Focused route tests inspect generated DOCX contents, headers, and parameter handling.
- Update `SYSTEM_REFERENCE.md` and the relevant Swimm walkthrough; generated API reference is refreshed from its generator.

Harness criteria: Focused issue-brief tests pass; documentation generation check passes.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/1.oi7rhqp2.sw.md`, generated API reference via its source generator.

Rollback/recovery: Revert the route and page renderer additions; no schema or persisted data changes.

Evidence: The supplied issue description ends after the required footer prefix; GitHub API access returned 403, so a UTC ISO date follows the prefix without adding other undocumented requirements. The API route and DOCX renderer reuse `fetch_issue_brief`; the DOCX includes the page's displayed summaries, disclosures, trace links, empty state, and dated footer. Canonical docs updated: `SYSTEM_REFERENCE.md` and `CHANGELOG.md`. Swimm walkthrough updated: `.swm/1.oi7rhqp2.sw.md`. `python -m py_compile backend/pages/issue_brief.py backend/routes.py tests/test_issue_brief.py` passed; `git diff --check` passed. `python -m pytest tests/test_issue_brief.py -q` could not run (`No module named pytest`). `python scripts/check_generated_docs.py` failed because FastAPI and SQLAlchemy are unavailable, so generated references could not be refreshed. No database, deploy, commit, or push operation was performed.

Files changed: `.github/project-manager/tasks/issue-158-issue-brief-docx-export.md`, `.swm/1.oi7rhqp2.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `backend/pages/issue_brief.py`, `backend/routes.py`, `tests/test_issue_brief.py`.
Delegated work: `managed-worker` implemented the route, DOCX renderer, and focused tests; it returned the required structured summary. Worker-reported pytest attempts were blocked by absent test/runtime dependencies; manager independently reviewed the diff and reran focused validation.
Focused validation: `python -m py_compile backend/pages/issue_brief.py backend/routes.py tests/test_issue_brief.py` passed; `git diff --check` passed. `python -m pytest tests/test_issue_brief.py -q` blocked: `No module named pytest`.
Residual risk: Behavioral tests and generated API/schema documentation checks remain unverified because pytest, FastAPI, and SQLAlchemy are absent. The rest of issue #158's truncated description is unavailable.
Next bounded task: Install/activate the repository test dependencies, rerun focused issue-brief tests, and regenerate/check the API reference.

## Hypothesis

If the DOCX export calls the existing issue-brief fetcher and serializes each displayed aggregate/list with the same labels and link targets, the focused test will verify parity with the page data and the requested dated footer.

## Plan

1. Add the DOCX renderer and route using the existing issue-brief query.
2. Add populated and empty brief route tests and verify DOCX structure, date footer, and download headers.
3. Update canonical/Swimm docs and attempt focused and generated-document checks.

## Execution Checkpoints

- Delegation: `managed-worker` handled only the issue brief route, renderer, and tests; files and results are recorded above.
- Implementation: Added `GET /issue-brief.docx`, page-fact DOCX serialization, generated UTC-date footer, and focused route tests.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `.swm/1.oi7rhqp2.sw.md`; generated-reference regeneration is blocked by missing dependencies.
- Recovery: Not applicable; no long-running job or persistent state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use ISO date after requested footer prefix | Issue body is truncated after “Generated from iLit data on”; no additional formatting requirements available | Supplied task description; GitHub issue API returned 403 |

## Completion

Completion recorded: no

Summary: Implementation and source documentation are present; task remains blocked pending behavioral tests and generated-reference refresh.

Validation: Python compilation and `git diff --check` passed. Focused pytest could not start because pytest is missing; generated-doc check could not import FastAPI or SQLAlchemy.

Residual risk: DOCX route behavior and generated API contract have not been verified in this environment; remainder of issue description unavailable.

Next recommended task: Restore test/document-generation dependencies and rerun the focused pytest and generated-doc check.
