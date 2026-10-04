# Task: Add issue-brief DOCX export

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Complete issue #158 by preserving the existing brief, adding yearly Minister-win statistics and a parity DOCX export, and reusing the case-search DOCX bootstrap helper.

Why now: The full issue body is now available; the initial implementation omitted Minister win rates and needs completion against the full acceptance criteria.

Owner surface: Issue brief analytics and rendering, with one shared DOCX helper used by the existing search export.

Commit allowed: no

Push allowed: no

Dependencies: Existing `fetch_issue_brief`, active `reader_extracted` government-outcome semantics, filtered-search DOCX helper pattern, and latest `origin/main` merged at `e0c3dca`.

Risk boundary: Preserve all existing brief payload fields and rendered content; only append yearly Minister-win fields. Keep source facts deterministic with no generated prose. Preserve tag bounds, taxonomy/outcome/citation semantics, route no-store behavior, and `/search/export.docx` behavior. Do not access a database outside isolated tests; do not touch db/deploy/.env.

Smallest falsifiable check: `python -m pytest tests/test_issue_brief.py -q`

Acceptance criteria:

- `fetch_issue_brief` keeps all current fields/values and appends yearly Minister-win rate, wins, total n, classified n, and unclassified count.
- The issue page and DOCX display yearly decision counts, outcome splits, and Minister-win statistics with denominator disclosures.
- `GET /issue-brief.docx` calls the same fetcher as the page; its DOCX opens and contains expected headings, numbers, authorities, links, and the exact dated descriptive-statistics footer.
- Existing JSON/page behavior and `/search/export.docx` output remain compatible.
- Update `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and the relevant Swimm walkthrough; regenerate/check generated docs from source.
- Run focused tests and the full pytest suite with the three configured CI deselections; record any actual limitations.

Harness criteria: Issue-brief and shared DOCX export tests pass; full CI-deselected pytest suite result is recorded; generated-doc check passes or is blocked with evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `docs/API_REFERENCE.generated.md` via `scripts/generate_api_reference.py`.

Rollback/recovery: Revert only the issue-brief additions and shared DOCX-helper refactor; no schema or persisted data changes. Restore `/search/export.docx`'s existing inline bootstrap/serialization if reverting the shared helper.

Evidence: Latest `origin/main` was merged in `e0c3dca`; initial implementation is `b3f342a`. Added yearly Minister-win summaries using stored `government outcome` categories; preserved prior outcome fields, authorities, and links. Page and DOCX share the additive facts; both DOCX routes now use `backend/docx_export.py`. `python -m pytest tests/test_issue_brief.py tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages -q` passed (7 tests). `python scripts/generate_api_reference.py` and `python scripts/check_generated_docs.py` passed; Python compilation and `git diff --check` passed. Full suite with CI deselections ran 1,265 passed, 3 failed, 2 skipped, 1 xfailed, and 3 deselected: one failure needs the unavailable `sentence-transformers` package and two fail to download the tiktoken vocabulary because network DNS is unavailable. The requested `report_progress`/`parallel_validation` integrations are not exposed here; progress checklist was sent in conversation and equivalent parallel focused checks were run locally. Secret-pattern scan found no matches. No database, deployment, commit, or push operation occurred.

Files changed: `.github/project-manager/tasks/issue-158-issue-brief-docx-export.md`, `.swm/1.oi7rhqp2.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `docs/API_REFERENCE.generated.md`, `backend/analytics_service.py`, `backend/docx_export.py`, `backend/issue_brief_analytics.py`, `backend/issue_brief_docx.py`, `backend/pages/issue_brief.py`, `backend/routes.py`, `tests/test_issue_brief.py`.
Delegated work: `managed-worker` previously implemented the base DOCX route/render/tests and returned a structured inventory; manager inspected full issue requirements, added the missing yearly statistics, extracted/reused DOCX helpers, and independently validated.
Focused validation: `/tmp/issue158-venv/bin/python -m pytest -q tests/test_issue_brief.py tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages` passed (7); `/tmp/issue158-venv/bin/python scripts/check_generated_docs.py` passed (3 references); `/tmp/issue158-venv/bin/python -m py_compile ...` and `git diff --check` passed.
Residual risk: The full CI-deselected suite is not clean due one missing local-embedding dependency and two unavailable external tokenizer downloads; these failures are unrelated to the issue-brief changes. No browser check was performed.
Next bounded task: In a dependency/network-enabled CI environment, rerun the exact full suite and commit/publish this change through the available progress integration.

## Hypothesis

If the brief appends yearly Minister-win rates while retaining all previous fields, and both exporters share the existing text-to-DOCX bootstrap/serialization convention, focused tests will verify denominator transparency, page/DOCX parity, valid document structure, and unchanged search-export behavior.

## Plan

1. Add Minister-win summaries as an additive analytics field.
2. Extract DOCX serializers and shared helpers into new modules; keep route edits minimal.
3. Test page/DOCX content, denominators, links, headers, footer, and search-export compatibility.
4. Update canonical/Swimm docs, regenerate references, and run focused/full checks.

## Execution Checkpoints

- Delegation: `managed-worker` handled only the issue brief route, renderer, and tests; files and results are recorded above.
- Implementation: Added yearly Minister-win rate/count/denominator fields, matching page/DOCX table facts, shared DOCX helpers, and the exact requested footer suffix.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and regenerated `docs/API_REFERENCE.generated.md`; generated-doc consistency passed.
- Recovery: Not applicable; no long-running job or persistent state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use classified government outcomes for Minister-win rate; disclose total n, classified n, and unclassified count | Align with stored outcome categories and established rate semantics; unknown outcomes must not be treated as losses | `backend/judge_issue_record.py`; `backend/analytics_service.py::_judge_outcome_counts` |

## Completion

Completion recorded: no

Summary: Issue #158 feature acceptance checks and docs pass; task is blocked from clean completion by three unrelated full-suite dependency/network failures and unavailable report-progress integration.

Validation: Focused tests passed (7), generated docs passed (3 references), py_compile and `git diff --check` passed. Full suite: 1,265 passed, 3 failed, 2 skipped, 1 xfailed, 3 deselected.

Residual risk: Full suite retains one sentence-transformers dependency failure and two offline tiktoken vocabulary-download failures. No browser validation or commit/push was performed.

Next recommended task: Rerun full CI in a dependency/network-enabled environment, then commit and publish via the project progress integration.
