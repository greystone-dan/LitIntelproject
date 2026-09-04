# Task: FastAPI Lifespan Modernization, IRPA/IRPR Extraction Hardening, and Data Quality Reporting

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task:
1. Modernize `backend/main.py` startup event to the modern FastAPI `lifespan` context manager, eliminating deprecation warnings.
2. Harden IRPA/IRPR statute extraction tests with comprehensive positive, negative, and exact-offset fixtures for complex nested provisions (e.g., `34(1)(f)`, `72(1)`, `112`, `ss. 96 and 97(1)`).
3. Implement an automated data-quality report tool (`scripts/evaluate_data_quality.py`) to systematically audit orphan edges, null metadata fields, and extraction coverage as specified in P0 roadmap milestones.

Why now:
- User priority: Keep statute extraction narrow and precise; prioritize clean IRPA and IRPR extraction with reliable capture of nested forms like `34(1)(f)`.
- System reference limitation 7 specifies migrating FastAPI startup hook to lifespan handler.
- Swimm Improvement Queue P0 milestone requires deterministic data-quality measurement (orphan links, duplicate edges, null metadata).

Owner surface: `backend/main.py`, `backend/citations.py`, `tests/test_citations.py`, `scripts/evaluate_data_quality.py`

Dependencies: `backend/database.py`, `backend/citations.py`, `backend/models.py`

Risk boundary:
- Extraction precision must not regress; positive, negative, and exact offset fixtures must pass.
- Case citations and statute references must remain strictly separate layers.
- Application startup and database initialization must remain 100% reliable.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_citations.py tests\test_api.py -q`

Acceptance criteria:
- FastAPI lifespan handler active with zero deprecation warnings on startup.
- Nested IRPA/IRPR fixtures tested with exact character offsets.
- `scripts/evaluate_data_quality.py` can run against database or dry-run and emit structured JSON/markdown health report.
- Full regression suite passes cleanly.
- Swimm documentation updated.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `.swm/4.9nn3id9f.sw.md` (Citation, Statute, and Tag Extraction)
- `.swm/untitled-doc.vt0ykcns.sw.md` (Data Quality and Metrics)

Rollback/recovery: Revert modified files if tests fail.

Evidence:
1. Migrated `backend/main.py` startup event to the modern FastAPI `lifespan` context manager via `asynccontextmanager`. Verified zero deprecation warnings on application startup.
2. Hardened IRPA/IRPR nested provision extraction in `tests/test_citations.py` with exact-span character slicing, positive fixtures (`34(1)(f)`, `245(1)(c)`, `228(1)(a)`, `72(1)`), and negative rejection tests for non-statute transcript/exhibit text. All 79 citation tests passing cleanly.
3. Created `scripts/evaluate_data_quality.py` which executes deterministic SQL audits over canonical cases, chunks, citations, statutes, and metadata completeness, outputting JSON and markdown summaries. Verified execution on database (61,241 cases, 1.88M citations, 0 invalid offset spans, 0 orphan targets).
4. Added unit tests in `tests/test_evaluate_data_quality.py` and regenerated `docs/SCRIPT_CATALOG.generated.md`.
5. Updated Swimm documentation (`.swm/untitled-doc.vt0ykcns.sw.md` and `.swm/blank.dudtv9pz.sw.md`).
6. Full test suite: 304 passed in 17.02s.

## Hypothesis
Replacing `@app.on_event("startup")` with `lifespan` will eliminate deprecation warnings while preserving startup database initialization, and comprehensive nested IRPA fixtures will verify extractor precision for section forms like `34(1)(f)`.

## Plan
1. Update `backend/main.py` to use `lifespan=lifespan` with `asynccontextmanager`.
2. Add nested IRPA/IRPR exact-span and negative regression tests in `tests/test_citations.py`.
3. Create `scripts/evaluate_data_quality.py` for deterministic database/corpus health audits.
4. Run full pytest suite and compile checks.
5. Update Swimm documentation and mark task complete.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Modernize lifespan, harden nested IRPA tests, and add data quality audit | This task file |
| 2026-09-03 | Migrated main.py to lifespan context manager | Eliminate FastAPI startup deprecation warnings | `backend/main.py` |
| 2026-09-03 | Added nested IRPA/IRPR exact-span and negative fixtures | Guarantee precision on section-form citations | `tests/test_citations.py` |
| 2026-09-03 | Implemented scripts/evaluate_data_quality.py | Satisfy P0 data-quality measurement milestone | `scripts/evaluate_data_quality.py`, `tests/test_evaluate_data_quality.py` |
| 2026-09-03 | Validated full test suite | Confirm 304 passing tests | `pytest -q` -> 304 passed |

## Completion
Status: complete
Summary: Successfully modernized FastAPI lifespan handler, hardened nested IRPA/IRPR extraction fixtures with exact character offsets, and built the automated data-quality evaluation tool.
Validation: `pytest -q` -> 304 passed in 17.02s.
Residual risk: None.
Next recommended task: Add browser smoke test suite (Playwright) to complete the remaining P0 roadmap items.
