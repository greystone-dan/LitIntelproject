# Task: Compare decisions side by side

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #231's stored-data-only, rule-based decision comparison page and JSON endpoint, with additive case-reader prefill link.

Why now: Analysts need a traceable side-by-side view of stored facts and shared or distinct legal signals without AI-generated conclusions; follow-up checks preserve route contracts and distinguish citation target pinpoints from source occurrence paragraphs.

Owner surface: Comparison feature: new `backend/case_compare.py` and `backend/pages/case_compare.py`, with minimal API/reader integration.

Commit allowed: yes

Push allowed: no

Dependencies: Existing case/citation resolver and stored case, outcome, tag, statute, citation data.

Risk boundary: Do not access the database, `.env`, or deploy scripts; do not alter existing reader behavior or change data semantics. Preserve issue #112's keyboard and print behavior and its existing paragraph shading, cited-paragraph counts, summary, similar paragraphs, and outline features. Comparison is deterministic and stored-data-only.

Smallest falsifiable check: `python -m pytest -q tests/test_case_comparison.py`

Acceptance criteria:

- `GET /compare?a=...&b=...` and `GET /api/compare?a=...&b=...` resolve IDs/citations with the existing resolver and render stored facts, outcome provenance, tags, statutes, authorities, shared/unique comparisons, pinpoints, and cross-citation links.
- Unknown decisions receive a helpful 404; comparing the same decision twice is rejected politely.
- Reader exposes an additive “Compare with…” link with query parameters prefilled; no required JavaScript.
- Fixture tests cover shared/disjoint tags, cross-citation, unknown input, and duplicate decision.
- Backend inventory and canonical docs are updated; generated references are regenerated and checked.
- Issue #112 reader behavior remains compatible.

Harness criteria: Comparison fixtures pass; generated documentation check passes; task and code docs both identify updated canonical and Swimm references.

Docs/generated references: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, relevant active UI/reader Swimm walkthrough, API reference via generators.

Rollback/recovery: Revert only the comparison feature files and minimal route/reader integration; no schema or data changes.

Evidence: Read issue #231's full public body and issue #112's full body; its
comments list was empty. Issue #112 requires keyboard j/k or n/p navigation,
visible current paragraph, ? help, shortcuts ignored while typing, print
navigation/side-panel/button suppression, numbered paragraphs, no paragraph
splitting, citation/title print header, and preservation of shading, cited
counts, summary, similar paragraphs and outline features. The implementation
only adds a reader link and hides that link in print; fixture assertions retain
the keyboard, print, and reader-feature markers. The first focused test run
exposed a missing `CaseChunk.token_estimate` in the new fixture and an absent
`requests` test dependency; both were repaired without project dependency
changes. A temporary environment under `/tmp/litintel-casecompare-venv` enabled
validation without modifying repository dependencies. Test and generator
commands set `PYTHON_DOTENV_DISABLED=1`; tests used in-memory SQLite only.
Canonical docs updated: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, and
`CHANGELOG.md`. Swimm walkthrough updated:
`.swm/6.maiixtsw.sw.md`. Generated API/schema/script references regenerated.
Follow-up compatibility clarification preserves the legacy page form action at
`/case-compare` and sets `/compare` only on the new page.
Citation evidence now labels `Citation.target_paragraph` as the cited decision's
pinpoint, while source occurrence paragraphs come from the citing chunk; only an
exact stored `Citation.target_case_id` match produces a cross-citation. An
unresolved citation mentioning the compared decision is included in the fixture
and does not create a cross-citation or target pinpoint.

Files changed: `backend/case_compare.py`, `backend/pages/case_compare.py`,
`backend/pages/data_explorer.py`, `backend/routes.py`,
`tests/test_case_comparison.py`, `docs/ARCHITECTURE.md`,
`SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`,
`docs/API_REFERENCE.generated.md`, `docs/SCHEMA_REFERENCE.generated.md`,
and this task record.
Delegated work: managed-worker owned comparison implementation and fixture
tests; its structured return reports no DB access and no task-record edits.
Focused validation: Follow-up pinpoint/target check: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m pytest -q tests/test_case_comparison.py` — 28 passed, 1 deprecation warning. Full focused/UI/docs set: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m pytest -q tests/test_case_comparison.py tests/test_feature_tabs.py tests/test_documentation_contracts.py tests/test_inline_js_syntax.py` — 112 passed, 1 skipped, 1 deprecation warning. Regenerated with `scripts/generate_api_reference.py`, `scripts/generate_schema_reference.py`, and `scripts/generate_script_catalog.py` using the same isolated Python and `PYTHON_DOTENV_DISABLED=1`; `scripts/check_generated_docs.py` — all 3 references current. `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m compileall -q backend/case_compare.py backend/pages/case_compare.py backend/pages/data_explorer.py backend/routes.py tests/test_case_comparison.py && git diff --check` — passed.
Residual risk: No live-database or browser run; stored evidence is not a legal-equivalence or completeness finding.
Next bounded task: None.

## Hypothesis

If the comparison service and page consume only persisted case, outcome, tag, statute, and citation evidence through the existing resolver, fixture tests will demonstrate accurate shared/unique signals and safe handling of unresolved and identical inputs without reader regressions.

## Plan

1. Implement the comparison logic, JSON/page routes, and additive reader link in a narrow feature slice.
2. Add fixture tests for comparison evidence and request edge cases.
3. Update the architecture inventory, canonical references, and relevant Swimm walkthrough; regenerate generated documentation and validate.

## Execution Checkpoints

- Delegation: managed-worker returned the required structured report and code/test files. Manager recovery repaired a required fixture token count and installed `requests` only in the temporary environment to complete validation.
- Implementation: comparison code, route integration, reader prefill and SQLite fixture cases added; follow-up keeps old/new page form actions distinct.
- Documentation: `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and generated references updated, with explicit old/new route contracts and the issue-driven reader-link rationale.
- Recovery: Not applicable; no database or bulk operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created; commit and push prohibited | User explicitly requested no Git push and implementation is for review | Issue #231 public body and issue #112 body; issue #112 comments list was empty |
| 2026-10-04 | Keep citation resolution local and preserve existing route contracts | Stored-data-only, no external lookup, and additive compatibility | Existing local resolution index and passing route fixtures |
| 2026-10-04 | Keep the legacy compare form action separate from the new route | Avoid changing the pre-existing `/case-compare` workflow while adding `/compare` | Fixture verifies old form posts to `/case-compare` and new form posts to `/compare` |
| 2026-10-04 | Label target and source paragraph evidence separately | `Citation.target_paragraph` is the cited decision's pinpoint, not the citation occurrence paragraph | Fixture verifies explicit UI labels and ignores matching unresolved text without exact target ID |
| 2026-10-04 | Latest main requires no incorporation | Main ref remained at the recorded base | `git fetch origin main`; `origin/main` at `4735088`, ancestor of HEAD |

## Completion

Completion recorded: yes

Summary: Added stored-data comparison API/page and reader prefill; preserved the existing comparison service/API and legacy page action, and documented the issue-driven reader-link addition. Target pinpoints and source occurrence locations are explicitly distinct.

Validation: 112 focused/UI/docs/inline-JS tests passed, one skipped; 28 focused compatibility fixtures passed; generated-doc, compile, and diff checks passed.

Residual risk: No live-database or browser execution; stored signals do not establish legal equivalence or completeness.

Next recommended task: None; live-corpus evaluation requires a separate authorized task.
