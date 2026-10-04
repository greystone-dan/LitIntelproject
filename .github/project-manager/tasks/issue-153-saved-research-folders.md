# Task: Saved research folders

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add browser-local saved research folders, case notes, JSON backup/restore,
and stateless CSV/DOCX exports for selected folder cases.

Why now: A lightweight research workbench supports saving and organizing
authorities without creating server-side user state; downloadable exports make
the saved work portable.

Owner surface: New `backend/research_folders.py` and `backend/pages/research_folders.py`
modules, with minimal route/application registration and additive Data Explorer
controls.

Commit allowed: yes

Push allowed: yes, only via the approved `report_progress` workflow

Dependencies: Existing Data Explorer search/reader builders, filtered-search
DOCX helper, FastAPI route conventions, and the selected active UI walkthrough.
Issue #112 Rules block is currently inaccessible (GitHub CLI lacks auth; public
API returned HTTP 403); do not infer additional issue-specific rules.

Risk boundary: No database access, server persistence, new logging, `.env`
access, changes to existing search/reader contracts, or unbounded exports.
Export accepts at most 500 selected cases and emits only citation, name, court,
date, outcome (including `unclassified`), and note.

Smallest falsifiable check: Focused API tests prove valid selected IDs and notes
produce CSV/DOCX exports capped at 500 and reject invalid/oversized requests;
static UI tests prove storage failure is visible and additive folder controls
exist on search and reader surfaces, including JavaScript syntax validation.

Acceptance criteria:

- Browser `localStorage` is the only folder persistence; denied/unavailable
  storage is visibly reported without breaking the page.
- Users can create, rename, and confirm deletion of folders, add cases from
  Case Search and the reader, and edit per-case notes.
- JSON backup export/import works with validation and no server storage.
- `POST /api/research-folders/export` returns bounded CSV or DOCX via existing
  filtered-search DOCX helpers and includes citation/name/court/date/outcome,
  `unclassified`, and note fields.
- Focused server and static-analysis JavaScript tests, repository validation,
  canonical docs, and the relevant Swimm walkthrough are updated and recorded.

Harness criteria:
- focused export and UI static-analysis tests pass
- generated-doc check and documentation link/diff checks pass
- documented full-suite run completes or exact unrelated blockers are recorded

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`,
`docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; generated API reference
must be refreshed from its generator.

Rollback/recovery: Revert the new modules, tests, and additive UI hooks; no
database state or migration exists. Keep unrelated worktree changes intact.

Evidence: The `folder-export` managed worker added the API module/router and
focused API tests; its test commands were blocked because pytest and FastAPI
are not installed. Manager added the browser-local UI module, route/page
integration, static tests, and docs. Python compilation, `git diff --check`, and
Node `--check` for the JavaScript passed. Issue #112 Rules block inspection was
attempted using `gh issue view 112` and the public GitHub API, but failed due
missing authentication/HTTP 403. No database or `.env` access.

Files changed: `.github/project-manager/tasks/issue-153-saved-research-folders.md`,
`backend/pages/research_folders.py`, `backend/research_folders.py`,
`backend/routes.py`, `tests/test_research_folders_api.py`,
`tests/test_research_folders_static.py`, `SYSTEM_REFERENCE.md`,
`CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/1.oi7rhqp2.sw.md`, and
`.swm/6.maiixtsw.sw.md`.
Delegated work: `issue153-inventory` (managed-worker), read-only issue/rules and
convention inventory; and `folder-export` (managed-worker), backend export
module/router/tests; both returned the required structured reports.
Focused validation: `python -m compileall -q backend/research_folders.py
backend/pages/research_folders.py backend/routes.py
tests/test_research_folders_api.py tests/test_research_folders_static.py`
passed with one pre-existing `backend/pages/data_explorer.py` invalid-escape
SyntaxWarning. `node --check -` passed for the injected JavaScript; direct
static UI assertions passed 10/10; new Swimm links resolve; `git diff --check`
passed. `python -m pytest -q tests/test_research_folders_static.py
tests/test_research_folders_api.py` and the documented full suite with its
three deselects both stopped because pytest is not installed.
`python scripts/generate_api_reference.py` stopped because FastAPI is absent;
`python scripts/check_generated_docs.py` reported generator failures for
missing FastAPI and SQLAlchemy. The changed-Markdown local-link scan found two
pre-existing broken links in `SYSTEM_REFERENCE.md` (`ANALYST_QUICK_START.md`
and `reports/test-coverage.md`), confirmed present in HEAD; all new Swimm links
resolve. Common secret-pattern scan found no matches.
Residual risk: Issue #112 Rules block contents remain unknown; Python tests,
generated-doc regeneration/check, and live browser validation remain blocked.
The requested `report_progress` and `parallel_validation` integrations are not
exposed in this session; independent validations were run with the available
parallel tool, but no publish was performed.
Next bounded task: In a dependency-equipped, authenticated session, inspect the
issue #112 Rules block, run focused/full/documentation validation, then publish
using the approved `report_progress` workflow.

## Hypothesis

If the export logic is isolated from request registration, focused API tests
will demonstrate that selected folder cases can be exported without persistence
and with a strict 500-case ceiling.

## Plan

1. Implement the stateless export endpoint and test its CSV/DOCX contract.
2. Add browser-local folder management and additive search/reader controls with
   static-analysis coverage.
3. Run focused then repository validation; update canonical docs and Swimm.

## Execution Checkpoints

- Delegation: `issue153-inventory` (managed-worker), read-only repository
  conventions and issue #112 access; structured report received.
- Implementation: Pending; backend export is the first slice.
- Documentation: Pending; update canonical sources and
  `.swm/6.maiixtsw.sw.md` in the same checkpoint.
- Recovery: No persistent server state; local browser backup is JSON.

## Decision Log

Product outcome: Analysts can collect and annotate authorities in a browser,
move that work through JSON backup, and export selected evidence without
creating server-side folder state.

Alternatives considered:

| Approach | Accuracy/traceability | Cost and maintenance | Scale/fit |
| --- | --- | --- | --- |
| `localStorage` + JSON backup + stateless API export (selected) | Browser retains explicit case IDs/notes; API re-reads canonical case metadata for export | Smallest implementation; browser quota and per-profile scope are disclosed | Fits the requested client-only ownership and 500-case export cap |
| IndexedDB + JSON backup | Same canonical export source; local folder records remain inspectable | More async lifecycle, migration, and test complexity | Better for very large client datasets than the scoped folder feature needs |
| Server-backed folders | Easier cross-device sharing, but introduces account and persistence semantics | Requires identity, schema, authorization, retention, and logging decisions | Conflicts with the explicit no-server-folder-storage boundary |

The selected approach is disconfirmed if its visible storage-failure path cannot
preserve/export in-memory data, or if selected metadata exports exceed the
500-case bound; focused static/API tests are the smallest current experiment.

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use localStorage for folder state, JSON for portable backup, and a stateless API for selected exports | Matches the requested privacy/persistence boundary while reusing the existing filtered-search DOCX path | User acceptance criteria and existing Data Explorer/export contracts |
| 2026-10-04 | Keep implementation in new page/API modules with minimal registration hooks | Limits coupling to the large route and page-builder modules | Repository ownership map and issue request |
| 2026-10-04 | Prefer browser localStorage to IndexedDB or server-backed storage | IndexedDB adds asynchronous state/migration complexity for a browser-only collection; server persistence violates the no-server-folder-state requirement | Explicit issue outcome; no schema or migration requirement |

## Completion

Completion recorded: no

Summary: Implementation and documentation are present; the task is blocked on
the inaccessible issue #112 Rules block and missing executable Python/document
validation dependencies.

Validation: See focused validation evidence above; repository-wide checks remain
to be attempted.

Residual risk: Issue #112 Rules block is inaccessible in this session.

Next recommended task: Execute the documented test and generated-reference
checks in a dependency-equipped environment, then use the approved publish
workflow.
