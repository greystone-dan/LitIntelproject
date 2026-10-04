# Task: Compare decisions side by side

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #231's stored-data-only, rule-based decision comparison page and JSON endpoint, with additive case-reader prefill link.

Why now: CodeQL identified a polynomial regex denial-of-service risk when unbounded compare input reaches the shared citation variant parser; harden only the new compare boundary without changing the shared resolver.

Owner surface: Comparison feature: new `backend/case_compare.py` and `backend/pages/case_compare.py`, with minimal API/reader integration.

Commit allowed: yes

Push allowed: no

Dependencies: Existing case/citation resolver and stored case, outcome, tag, statute, citation data.

Risk boundary: Do not access the database, `.env`, or deploy scripts; do not alter existing reader behavior or change data semantics. Preserve issue #112's keyboard and print behavior and its existing paragraph shading, cited-paragraph counts, summary, similar paragraphs, and outline features. Comparison is deterministic and stored-data-only.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m pytest -q tests/test_case_comparison.py -k long`

Acceptance criteria:

- `GET /compare?a=...&b=...` and `GET /api/compare?a=...&b=...` resolve IDs/citations with the existing resolver and render stored facts, outcome provenance, tags, statutes, authorities, shared/unique comparisons, pinpoints, and cross-citation links.
- Unknown decisions receive a helpful 404; comparing the same decision twice is rejected politely.
- Reader exposes an additive “Compare with…” link with query parameters prefilled; no required JavaScript.
- Fixture tests cover shared/disjoint tags, cross-citation, unknown input, and duplicate decision.
- Inputs above 512 characters fail closed before trimming, numeric conversion, or citation parsing; a pathological citation fixture proves the parser is not reached.
- Required secret scan reports clean for every changed/created path.
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
CodeQL `py/polynomial-redos` at shared `backend/citations.py:2422` is mitigated
at the new comparison boundary; the shared citation resolver remains unchanged.
Blocker: `runtime-tools-secret_scanning` is unavailable in this environment
(`command -v runtime-tools-secret_scanning` returned no path), so no scan ran.
Do not commit or publish until that tool scans all changed and created paths.

Files changed: `backend/case_compare.py`, `backend/pages/case_compare.py`,
`backend/pages/data_explorer.py`, `backend/routes.py`,
`tests/test_case_comparison.py`, `docs/ARCHITECTURE.md`,
`SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`,
`docs/API_REFERENCE.generated.md`, `docs/SCHEMA_REFERENCE.generated.md`,
and this task record.
Delegated work: managed-worker owned comparison implementation and fixture
tests; its structured return reports no DB access and no task-record edits.
Focused validation: Pathological-input and route check: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m pytest -q tests/test_case_comparison.py -k 'overlong or http_route_precedence'` — 2 passed, 27 deselected. Full focused/UI/docs set: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-casecompare-venv/bin/python -m pytest -q tests/test_case_comparison.py tests/test_feature_tabs.py tests/test_documentation_contracts.py tests/test_inline_js_syntax.py` — 113 passed, 1 skipped, 1 warning. Regenerated API docs with `scripts/generate_api_reference.py`; `scripts/check_generated_docs.py` reports all 3 references current. Compilation and `git diff --check` passed. Scanner availability check: `command -v runtime-tools-secret_scanning` returned no path.
Residual risk: Required secret scan is pending. No live-database or browser run; stored evidence is not a legal-equivalence or completeness finding.
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
| 2026-10-04 | Bound compare input before parsing | CodeQL identified regex backtracking risk in the shared citation variant regex; shared resolver behavior must remain unchanged | `py/polynomial-redos` at `backend/citations.py:2422`; compare boundary will reject inputs above 512 characters |
| 2026-10-04 | Latest main requires no incorporation | Main ref remained at the recorded base | `git fetch origin main`; `origin/main` at `4735088`, ancestor of HEAD |

## Completion

Completion recorded: no

Summary: Added comparison input bound and pathological-input coverage; implementation and docs pass targeted validation, but secret scan is unavailable.

Validation: 113 focused/UI/docs/inline-JS tests passed, one skipped; generated-doc, compile, and diff checks passed. Secret scan did not run.

Residual risk: Do not commit or publish until the required secret scan runs. No live-database or browser execution; stored signals do not establish legal equivalence or completeness.

Next recommended task: Run `runtime-tools-secret_scanning` on every changed/created path; complete or publish only if clean.
