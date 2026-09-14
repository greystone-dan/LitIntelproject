# Task: Review and stabilize the iLIT website after V2 pipeline changes

Status: complete
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Verify the active iLIT Data Explorer website loads current case data and reader content after the V2 backend changes, then produce a bounded improvement recommendation before statutes/tag work resumes.

Why now: Backend extraction, resolution, and pipeline behavior changed substantially. The website must be checked against current API contracts and live data before downstream statute and tag workflows are prioritized.

Owner surface: `backend/pages/data_explorer.py`, `backend/routes.py`, and the active Data Explorer API/reader contract

Commit allowed: yes

Push allowed: yes

Dependencies: Local FastAPI server, PostgreSQL, current database counts, `tests/test_feature_tabs.py`, `tests/test_api.py`, and browser smoke coverage.

Risk boundary: Review and bounded UI/API compatibility only. Do not alter citation, statute, tag, or canonical database data. Do not redesign unrelated legacy pages. Any write remains limited to website code/tests/docs after a failing check identifies the need.

Smallest falsifiable check: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_feature_tabs.py tests\\test_api.py -q` plus the bounded browser smoke check against the refreshed local server.

Acceptance criteria:

- Active `/data-explorer` loads and its search-to-reader path opens a case.
- Reader API responses and displayed counts represent the current database, not stale hard-coded checkpoint prose.
- Basic mobile/themes and reader tabs remain functional.
- Review findings are ranked by severity and a bounded improvement backlog is recorded.
- Any implementation change has focused tests and updated canonical/Swimm documentation.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Keep website edits isolated to the active page/API/test surface; revert only the bounded UI change if focused validation fails. No database rollback is authorized.

Evidence: Delegated read-only static review found the expected Data Explorer/search/reader/tab contract but could not execute the browser. Manager acceptance initially failed because `/cases/35874/reader-data` timed out while `/analytics/search/cases/35874` returned normally. A watchdog traced the delay to request-time V2 citation extraction in `build_case_reader_data`; profiling showed `_format_reader_html` consumed `88.96s` of a `92.73s` profiled build by rescanning stored HTML once per citation. The reader was incorrectly doing extraction and HTML rewriting despite being a reader.

Manager fix: removed all live citation/statute extraction from the reader request path, removed request-time stored-HTML citation formatting, and removed the stale route import. The reader now returns persisted case text/chunks/citations/statute rows/tags/metadata only. Direct Vavilov reader build completed in `3.59s`, returned `4` chunks and `975` citation rows, with `formatted_html=False`. Focused reader API tests passed (`3 passed`). Final browser smoke passed: Vavilov search opened the case, reader tabs were `Metadata`, `Citations`, `Info`, `Intel`, `Activity`, `Tags`, `Acts / Regs`, `Precedents`, tag groups/occurrences rendered, the layer legend rendered, and mobile Themes loaded.

## Hypothesis

If the active Data Explorer frontend still matches its backend contracts, a bounded API plus browser smoke run will load search results, a selected case, reader tabs, and the mobile Themes view; failures will identify the smallest compatibility fix.

## Plan

1. Read authoritative UI/operations docs and delegate a bounded read-only website smoke/review.
2. Consume the worker report, decide the smallest website correction or document-only backlog.
3. Implement only directly required fixes, then rerun focused tests/browser smoke.
4. Update canonical/Swimm documentation and record ranked follow-up improvements.

## Execution Checkpoints

- Delegation: pending bounded read-only browser/API/UI review; worker may not edit task records or commit.
- Implementation: manager-owned active Data Explorer page/API/test changes only.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: local server/tunnel state only; no database writer.

## Completion

Completion recorded: yes

Summary: Repaired the V2 website regression that made case opening execute citation extraction and rescan stored HTML. The active reader is now persisted-evidence-only and the end-to-end browser smoke passes.

Validation: `pytest tests/test_api.py -k "reader or case_detail" -q` -> `3 passed`; direct reader build -> `3.59s`; browser smoke -> passed.

Residual risk: The reader payload remains large for citation-heavy decisions (`975` rows / about 3 MB for Vavilov). Next improvements should paginate or lazy-load secondary panels and linked-authority context without reintroducing extraction. The full repository suite was not rerun in this UI checkpoint.

Next recommended task: Add reader payload timing/size telemetry and lazy-load secondary panels (`Intel`, `Activity`, linked context) after the basic case view is visible.
