# Task: Add power-user query operators to Case Search

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add safe Boolean and field operators to active Case Search, preserving the existing plain-query behavior and export contract.

Why now: Issue #119 adds transparent precision controls for legal research without sacrificing the existing default search or bounded exports.

Owner surface: `backend/query_syntax.py` and active Case Search integration in `backend/analytics_service.py` / `backend/pages/data_explorer.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing analytics search filters, active `/data-explorer` workflow, CSV/DOCX export query forwarding.

Risk boundary: No schema/data/dependency changes, DB operation, deployment, script execution, credential access, or unrelated search refactor. Keep SQL values parameterized and do not alter plain-query semantics.

Smallest falsifiable check: `python -m pytest -q tests/test_query_syntax.py`

Acceptance criteria:

- Pure parser returns a structured query and readable echo; handles quoted phrases, Boolean operators, leading minus, supported fields, unknown operators, malformed quotes, and malicious-looking values safely.
- Explicit inclusive year ranges accept the requested `year:2018..2022` syntax and retain `year:2018-2022` compatibility; the echo describes the years as inclusive.
- At least 30 table-driven parser cases plus regression tests cover operator-free queries and echo behavior.
- Active Case Search compiles supported operators into existing bounded parameterized search; no-operator queries preserve today's behavior.
- Echo is shown above results and a Search tips popover documents syntax.
- CSV and Word exports use the same parsed query and remain bounded.
- Focused API/UI checks, full pytest with known CI deselects, generated-doc check, and diff/link checks pass or are documented as blocked.

Harness criteria:

- Parser cases and injection-safety checks pass.
- Active search/API and export regression checks pass.
- Required documentation checkpoint and generated-document checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, `.swm/6.maiixtsw.sw.md`; generated API reference through `scripts/check_generated_docs.py`.

Rollback/recovery: Revert the isolated parser, UI/API integration, tests, and documentation edits; no persistent state or migration is involved.

Evidence: Delegated parser/fixture implementation to two bounded managed-worker slices; the first parser acceptance pass revealed quoted field values were split and Boolean buckets were not compile-ready. The follow-up added a Boolean AST, but manager verification still found quoted field values split; manager repaired the tokenizer, corrected corresponding fixtures, and added explicit quoted-field tests. The original focused `python -m pytest -q tests/test_query_syntax.py` passed (131 tests). A bounded follow-up corrected the missing explicit inclusive year-range syntax, retained hyphen compatibility, and added table-driven parser/echo assertions. The SQL compiler's year-range matcher now accepts both `..` and `-`; `tests/test_search_matching.py::test_operator_search_builds_parameterized_boolean_filters_and_echo` is table-driven over both spellings and checks the same year bounds are bound. The focused parser command passed after the parser correction (134 passed); its final exact result is recorded below. The echo now says `2018 through 2022 (inclusive)`. This follow-up updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, and `.swm/6.maiixtsw.sw.md`; the visible Search tips example uses the exact requested `year:2018..2022` form and notes hyphen compatibility. Compiler integration tests were not run: the existing test surface imports FastAPI, which is among the dependencies previously found missing; no installs were attempted. Prior evidence: `python -m py_compile backend/query_syntax.py backend/analytics_service.py backend/routes.py backend/pages/data_explorer.py tests/test_query_syntax.py tests/test_search_matching.py tests/test_api.py tests/test_feature_tabs.py` passed (with an existing `SyntaxWarning` at `backend/pages/data_explorer.py:8`); a no-database AST smoke check compiled court/year/judge/cites/outcome terms and hostile values as bind parameters. API/UI/export tests could not collect because `fastapi`, `httpx`, and `python-docx` are missing. Full pytest with the three documented CI deselects stopped at 91 collection errors. `python scripts/check_generated_docs.py` could not regenerate API/schema references because `fastapi` and `sqlalchemy` are missing; no dependencies were installed and no generated outputs were edited. No broad checks were repeated for this correction.

Files changed: `.github/project-manager/tasks/issue-119-search-query-operators.md`, `backend/query_syntax.py`, `tests/test_query_syntax.py`, `backend/analytics_service.py`, `backend/pages/data_explorer.py`, `tests/test_search_matching.py`, `tests/test_api.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, `.swm/6.maiixtsw.sw.md`.
Delegated work: `query-syntax-worker` implemented the initial pure parser and tests; `query-parser-repair` added AST/precedence/table-driven coverage. Manager acceptance found and repaired quoted-field tokenization and updated stale test expectations. Neither worker edited files outside `backend/query_syntax.py` and `tests/test_query_syntax.py`. The current bounded acceptance correction was manager-owned directly because it was a tiny reversible parser/doc follow-up in an existing task.
Focused validation: Final continuation run `python -m pytest -q tests/test_query_syntax.py` — 134 passed in 0.08s, including `year:2018..2022`, legacy `year:2018-2022`, and inclusive plain-language echo checks. `git diff --check` — passed after the task-record evidence update. The newly table-driven compiler regression test was not run because its test module requires unavailable FastAPI dependencies. Previously recorded py_compile and isolated AST SQL compiler smoke checks passed before this continuation; they were not rerun. Broad API/UI/export, full-suite, and generated-doc checks were not rerun.
Residual risk: Parser and compiler code now accept the explicit range, but the compiler regression test and active API/rendered UI/CSV/DOCX paths remain unverified because required packages are absent; runtime SQL was not executed against a database (prohibited). Overall task remains blocked on those dependency limitations.
Next bounded task: In an environment with the repository's existing dependencies, rerun the focused Case Search/API/export/UI checks, full pytest with CI deselects, generated-doc check, and browser validation.

## Hypothesis

If the parser maps both range spellings to inclusive bounds and the SQL compiler recognizes both spellings while binding the same values, the parser and compiler regression cases will demonstrate the explicit syntax without dropping legacy compatibility.

## Plan

1. Implement and test the pure query parser.
2. Integrate parser output with active search, echo/tips, and exports without changing default query behavior.
3. Run focused checks, full pytest with CI deselects, regenerate/check generated docs, and update canonical plus Swimm documentation.

## Execution Checkpoints

- Delegation: Managed workers implemented parser and test surface; manager verified, found a quoted-field regression, and repaired it.
- Implementation: Added the parser AST compiler to active analytics search, echo response/UI, and query tips popover; the focused parser suite passed. Follow-up accepts both inclusive year delimiters in parser and SQL compiler, adds table-driven parser/echo/compiler coverage, and passes the parser suite; compiler test remains unrun due missing dependencies.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, and `.swm/6.maiixtsw.sw.md` updated; Search tips shows the exact requested syntax and legacy compatibility.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #119 specifies a multi-surface feature with parser, API, UI, exports, and validation requirements. | User-provided issue acceptance criteria; ownership pointers in `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, and `.swm/5.b49ftjal.sw.md` / `.swm/6.maiixtsw.sw.md`. |
| 2026-10-04 | Preserve ordinary multiword query path | AST implicit AND is for operator queries only; ordinary terms must continue through the established title/citation and identity path. | `backend/analytics_service.py::_query_uses_operators`; `tests/test_search_matching.py::test_plain_query_detection_preserves_legacy_multiword_search`. |
| 2026-10-04 | Block completion pending dependency-enabled acceptance | API/UI/export tests, full pytest collection, and generated-doc regeneration require existing packages unavailable in this environment; adding/installing dependencies is outside the requested boundary. | Focused pytest collection errors; full-suite 91 collection errors; `scripts/check_generated_docs.py` failed on missing FastAPI/SQLAlchemy. |
| 2026-10-04 | Accept explicit inclusive year range delimiter | Issue acceptance requires the literal `year:2018..2022`; retain the older hyphen form and make the normalized inclusive meaning clear in echo/docs. | `python -m pytest -q tests/test_query_syntax.py` — 134 passed; canonical and Swimm docs updated. |
| 2026-10-04 | Extend SQL compiler delimiter support | AST field values preserve the raw input, so parser normalization alone did not make `..` compile to the inclusive `BETWEEN` predicate. | `backend/analytics_service.py::_query_expression_sql`; table-driven compiler regression added, but its test module cannot run with current missing FastAPI dependencies. |

## Completion

Completion recorded: no

Summary: Parser and compiler code now support the specific `year:2018..2022` acceptance syntax, preserve hyphen compatibility, and provide inclusive echo text; Search tips and canonical/Swimm documentation are updated. The overall issue task remains blocked on dependency-enabled compiler/API/UI/full/generated-doc validation.

Validation: Final follow-up parser suite `python -m pytest -q tests/test_query_syntax.py` passed (134 passed in 0.08s); `git diff --check` passed. The compiler regression is table-driven but was not run because dependencies required to import `tests/test_search_matching.py` are unavailable. Earlier Python compilation and isolated SQL compiler smoke passed. Focused integration suite, full pytest with known deselects, and generated-doc check were previously attempted and blocked by missing dependencies; no broad validation was run for this correction.

Residual risk: Search and exports have not been exercised through the API or browser; parameterized SQL was smoke-tested without database access, not executed.

Next recommended task: Re-run the documented Case Search, full-suite, and generated-doc checks in a dependency-complete environment.
