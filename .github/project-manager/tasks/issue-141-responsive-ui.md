# Task: Issue #141 responsive research UI

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Make every generated research UI page usable at 360, 768, and 1280 CSS pixels and document the page-by-page audit.

Why now: Narrow viewports currently lack systematic validation across generated page builders; regressions undermine research access and usability.

Owner surface: `backend/pages/` generated page markup and styles, with a browser-independent test contract.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/case_formatter.py`, `scripts/browser_smoke.py`, UI guide, and active UI Swimm walkthrough were inspected for generated page behavior and test/documentation ownership. Existing UI guide appendix in `SYSTEM_REFERENCE.md` is synchronized by `scripts/embed_documentation_appendices.py`.

Risk boundary: Change only responsive CSS/layout and focused tests/docs. Preserve print styles, page features, desktop appearance, viewport-specific usability, table behavior, and all data/API contracts. No database, migration, deployment, dependency, credential, or generated-document hand edits.

Smallest falsifiable check: focused responsive page-builder tests assert viewport metadata, responsive layout rules, non-table min-width limits, and scroll wrappers for every table.

Acceptance criteria:

- Every page builder is assessed against 360, 768, and 1280 widths; only relevant CSS is changed.
- Browser-independent CSS extraction tests enforce the requested viewport/layout/table constraints.
- Optional browser screenshots are created only if `/opt/pw-browsers` Chromium is available; otherwise browser validation skips cleanly.
- A page-by-page audit report, canonical research UI guide, and relevant Swimm walkthrough are updated together.
- Focused tests pass, followed by the requested full pytest command with exactly the three CI deselects and `python scripts/check_generated_docs.py`; results are recorded honestly.

Harness criteria:
- Focused responsive tests pass.
- Required documentation and Swimm walkthrough are updated and checked.
- Full requested pytest command and generated-doc check results are recorded.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `docs/reports/responsive-audit.md`, active UI walkthrough `.swm/6.maiixtsw.sw.md`, and regenerated `SYSTEM_REFERENCE.md` appendix via its generator.

Rollback/recovery: Revert only responsive CSS/test/doc hunks if they regress established behavior; use audit findings to narrow any failed page-specific fix. No persistent state is touched.

Evidence: The managed worker reviewed all `backend/pages/*.py` builders and changed only page CSS/markup plus `tests/test_responsive_generated_pages.py`; direct assertions, page-builder compilation, and diff checks passed. After merging `main`, `python -m pytest -q tests/test_responsive_generated_pages.py tests/test_documentation_contracts.py` passed (4 passed, 1 optional browser test skipped); the alias for `testing_page_html` prevents pytest from collecting the builder as a test. `python scripts/check_generated_docs.py` passed after running the API, schema, and script-catalog generators and re-embedding appendices. `docs/ARCHITECTURE.md` lists all 94 backend files; the documentation contract test passes. The requested full CI suite command ran with its exact three deselects: 1,534 passed, 2 skipped, 1 xfailed, 3 deselected, and 3 failed. The failures are environment-related network resolution failures in `tests/test_api.py::test_local_chunk_search_uses_requested_model` (Hugging Face) and two tokenizer-count tests in `tests/test_openai_chunk_embeddings.py` (OpenAI tokenizer blob DNS). `python -m py_compile` passed for all changed page builders and the responsive test, with existing invalid-escape `SyntaxWarning`s in `data_explorer.py` and `theme_explorer.py`. `/opt/pw-browsers` and Playwright are absent, so the optional browser test skipped and no screenshots were generated. The UI guide and Swimm walkthrough preserve both main's updates and the responsive notes; `scripts/embed_documentation_appendices.py` regenerated `SYSTEM_REFERENCE.md` from the merged references and guide.

Files changed: `.swm/6.maiixtsw.sw.md`, `SYSTEM_REFERENCE.md` (regenerated appendices), `backend/pages/citation_map.py`, `backend/pages/citation_pass.py`, `backend/pages/data_explorer.py`, `backend/pages/deidentify.py`, `backend/pages/fc_analytics.py`, `backend/pages/issue_brief.py`, `backend/pages/judge_outcomes.py`, `backend/pages/prototype.py`, `backend/pages/quick_search.py`, `backend/pages/tag_analytics.py`, `backend/pages/theme_explorer.py`, `docs/RESEARCH_UI_GUIDE.md`, `docs/reports/responsive-audit.md`, `tests/test_responsive_generated_pages.py`, and this task record.
Delegated work: managed-worker handled the bounded generated page/CSS and responsive-test slice; structured return recorded in manager turn. Manager owns reports, canonical/Swimm docs, generated appendix, final acceptance.
Focused validation: `python -m pytest -q tests/test_responsive_generated_pages.py tests/test_documentation_contracts.py` — 4 passed, 1 optional browser test skipped. `python scripts/check_generated_docs.py` — passed. `python -m py_compile backend/pages/citation_map.py backend/pages/citation_pass.py backend/pages/data_explorer.py backend/pages/deidentify.py backend/pages/fc_analytics.py backend/pages/issue_brief.py backend/pages/judge_outcomes.py backend/pages/prototype.py backend/pages/quick_search.py backend/pages/tag_analytics.py backend/pages/theme_explorer.py tests/test_responsive_generated_pages.py` — passed with existing warnings noted above.
Residual risk: Full suite has three tests that require network access unavailable in this environment; browser geometry and 360/768/1280 visual appearance remain unverified without Chromium/Playwright. Main introduced unrelated trailing whitespace in `backend/query_syntax.py` and `tests/test_query_syntax.py`; the responsive branch delta against main is whitespace-clean.
Next bounded task: Rerun only the three network-dependent tests and optional screenshots in an environment with the required network/browser; review rendered page geometry.

## Hypothesis

If generated pages include usable mobile viewport/layout rules and horizontally scrollable table wrappers, the browser-independent responsive contract will pass while existing desktop behavior and print rules remain intact.

## Plan

1. Review the canonical UI behavior, page builders, formatter, smoke checks, tests, and active UI walkthrough.
2. Inventory generated pages and add focused CSS contract checks; repair only responsive layout defects.
3. Produce the page-by-page audit and update canonical and Swimm guidance.
4. Run focused validation, the exact requested full suite command, generated-doc check, and optional browser smoke/screenshots if supported.

## Execution Checkpoints

- Delegation: managed-worker reviewed all `backend/pages/*.py` and updated scoped page/CSS and test files; structured return is summarized above.
- Implementation: 11 page/fragment modules plus focused responsive contract and optional screenshot test.
- Documentation: updated `docs/RESEARCH_UI_GUIDE.md`, `docs/reports/responsive-audit.md`, `.swm/6.maiixtsw.sw.md`; regenerated `SYSTEM_REFERENCE.md` appendices.
- Recovery: none required.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Created task with page-builder/CSS-test owner surface | User requested full issue #141 implementation with explicit constraints and validations | Issue request |
| 2026-10-04 | Assigned page/CSS and browser-independent contract test to managed worker; manager retained docs and acceptance | Bounded code surface can be implemented independently while preserving manager ownership of documentation and final validation | Worker inspected every Python page builder and returned structured findings |

## Completion

Completion recorded: no

Summary: Responsive CSS/test and documentation slice merged with current main; acceptance remains blocked on three network-dependent suite failures and unavailable browser rendering.

Validation: Focused responsive/documentation tests passed (4 passed, 1 skipped); generated-doc check passed; the full CI suite had 1,534 passes and 3 network-dependent failures. All four generator steps (API, schema, script catalog, appendix embedding) were run after merge.

Residual risk: Three full-suite tests could not access Hugging Face/OpenAI tokenizer assets, and rendered browser geometry/print layout remain unverified.

Next recommended task: Rerun the three network-dependent tests with DNS access and capture optional screenshots where Chromium and Playwright are available.
