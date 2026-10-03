# Task: Verify Phase 1 statute library counts and lookup fixtures

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Audit expected statute and section counts for the seven Phase 1 laws against parser output from small fixture XML, identify whether reported counts are computed or hard-coded, and add fixture tests for importer counts and point-in-time lookup including nested provision `34(1)(f)`.

Why now: Issue #79 requests evidence-backed count reporting and date-range/nested-provision coverage for the statute reference library.

Owner surface: Statute reference-library importer, its count reporting and point-in-time lookup tests.

Commit allowed: yes

Push allowed: yes, on the current task branch only; do not alter or push source PR #29.

Dependencies: Issue #29; any live database-dependent facts must be labelled "needs DB".

Risk boundary: Do not mutate or depend on live database contents. Preserve case/statute extraction separation and importer provenance. Commit/push is allowed only for this task's current working branch; never alter or push source PR #29. Do not create/open a PR; eventual PR target is `main` and must state it depends on `greystone-dan/LitIntelproject#29`.

Smallest falsifiable check: Focused pytest fixture tests showing imported statute/section counts against parsed small XML and asserting version lookup behavior for overlaps, gaps, and nested `34(1)(f)`.

Acceptance criteria:

- Seven Phase 1 laws' expected counts are compared with fixture parser/importer output and count provenance (computed or hard-coded) is identified in applicable pages, API, docs, and reports.
- Fixture XML tests cover importer count output and point-in-time version ranges, including overlap/gap behavior and nested provision `34(1)(f)`.
- `docs/reports/statute-library-count-check.md` reports repository-verifiable facts and labels live database-dependent claims "needs DB".
- `SYSTEM_REFERENCE.md` and the relevant Swimm walkthrough are updated and linked to authoritative implementation/report details.
- Focused validation passes; task evidence records exact command and result.

Harness criteria: Focused fixture tests pass; count-check report distinguishes code-derived findings from "needs DB"; canonical and Swimm docs updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md`; `docs/reports/statute-library-count-check.md`; `scripts/import_historical_statutes.py` is the source for regenerated `docs/SCRIPT_CATALOG.generated.md`.

Rollback/recovery: Revert only this task's fixture/test and documentation changes; no database writes or migrations are planned.

Evidence: Before equivalent focused manager discovery or implementation, the managed-worker inventoried the importer, count surfaces, lookup behavior, tests, and Swimm walkthrough, then returned the required structured fields (`Files inspected`, `Files changed`, `Commands run`, `Results`, `Failures`, `Uncertainty`, `Recommendation`). Its findings: seven configured Phase 1 entries with Charter skipped by XML import; no production per-law expected section totals; computed parser/returned-list counts versus fixed registry/UI choices; API has no count field; historical authority-index counts are a different surface; importer omitted effective end dates; lookup ignored end dates; live counts/ranges are "needs DB". The final audit report separates synthetic fixture output from live facts, classifies count surfaces, and distinguishes older authority-index counts. Fixture testing exposed and fixed the namespaced XML `Section` query, effective-start/end metadata persistence, gap-aware range lookup, and explicit `as_of` API fallback behavior. The stale hard-coded “12+ versions” example was removed from its source docstring and the generated catalog was refreshed. No live DB was accessed.

Files changed: `.github/project-manager/tasks/greystone-79-statute-library-count-check.md`; `scripts/import_statutes.py`; `backend/statute_versioning.py`; `backend/routes.py`; `tests/fixtures/statute_library/phase1_sample.xml`; `tests/test_statute_library.py`; `docs/reports/statute-library-count-check.md`; `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md`; `scripts/import_historical_statutes.py`; regenerated `docs/SCRIPT_CATALOG.generated.md`.
Delegated work: `statute-count-inventory` (managed-worker) completed read-only inspection and returned the required structured report; no files changed and no tests/linters were run by the worker.
Focused validation: `python -m pytest tests/test_statute_library.py -q` — 9 passed (one Starlette deprecation warning); `python scripts/check_generated_docs.py` — all 3 generated references current; `git diff --check` — passed; local Markdown link review — passed. `python scripts/generate_script_catalog.py` regenerated the script catalog. The first pytest attempt could not collect because test/runtime dependencies were absent; after installing the minimal dependencies required to import and run this focused test, final checks passed.
Residual risk: Current database statute/version/section counts and actual persisted effective ranges remain **needs DB**. The exact requested branch ref was unavailable; work remains on the existing `copilot/claudelibrary-expansion-w61ccb` checkout. Commit/push is authorized only for that current task branch; source PR #29 remains untouched and no PR is to be opened by this task.
Next bounded task: After dependency issue #29 is resolved and read-only DB access is available, run a bounded per-instrument `statutes` / `statute_versions` / `statute_sections` count and effective-range inventory.

## Hypothesis

If the statute-library importer and point-in-time lookup are correct, small XML fixtures will produce explicit parser-derived statute/section counts and deterministic version results for overlap, gap, and nested `34(1)(f)` cases without relying on the live database.

## Plan

1. Complete the assigned bounded read-only inventory of the importer, count surfaces, lookup behavior, and nearby tests.
2. Add parser/importer and point-in-time fixture tests; correct verified date-range and parser behavior.
3. Publish the count audit report, update `SYSTEM_REFERENCE.md`, the relevant Swimm walkthrough, and generated script catalog, then record exact evidence.

## Execution Checkpoints

- Delegation: Completed read-only inventory by managed-worker `statute-count-inventory`; no tests/linters run by worker.
- Implementation: Added three-section XML fixture; covered six XML-enabled Phase 1 entries, date metadata, overlap/gap selection, API no-fallback behavior, and nested section 34 paragraph f. Focused test passed 9 cases.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `.swm/4.9nn3id9f.sw.md`, and `docs/reports/statute-library-count-check.md`; regenerated `docs/SCRIPT_CATALOG.generated.md` from `scripts/import_historical_statutes.py`.
- Recovery: No long-running operation or database writes planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created on existing checkout without switching refs | Only `copilot/claudelibrary-expansion-w61ccb` is visible; exact requested `claude/library-expansion-w61ccb` ref is unavailable | `git branch --all --list '*library-expansion*' '*greystone*'` |
| 2026-10-03 | Assign count and lookup inventory to managed-worker | Required delegated discovery completed before equivalent manager discovery; worker returned no code edits | Structured report from `statute-count-inventory`; key files and findings recorded above |

## Completion

Completion recorded: yes

Summary: Completed issue #79's repository-level count audit and fixture coverage. The report does not claim live counts; those are explicitly "needs DB". Commit/push is permitted on the current task branch only; no PR was opened.

Validation: `python -m pytest tests/test_statute_library.py -q` — 9 passed; `python scripts/check_generated_docs.py` — 3 generated references current; `git diff --check` — passed; changed-document local links resolve. `python scripts/generate_script_catalog.py` completed.

Residual risk: Live imported counts and persisted version ranges require DB access. The visible checkout branch is named `copilot/claudelibrary-expansion-w61ccb`, not the requested `claude/library-expansion-w61ccb`; source PR #29 is not to be changed or pushed.

Next recommended task: After issue #29 and approved read-only DB access, produce a bounded per-instrument live count and date-range inventory.
