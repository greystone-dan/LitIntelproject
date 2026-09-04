# Task: Codebase Organization and Initial Modularization

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Analyze code structure hotspots, design a clean modular architecture preserving all contracts, and execute the first safe modularization slice.

Why now: The backend code is heavily concentrated in monolithic files (especially `backend/routes.py`, `backend/citations.py`, `backend/database.py`), making autonomous feature development and testing slower and riskier.

Owner surface: `backend/` and architecture documentation

Dependencies: Existing test suite (`tests/test_api.py`, `tests/test_citations.py`, `tests/test_feature_tabs.py`, `tests/test_run_overnight.py`)

Risk boundary:
- Public API routes and request/response models must remain identical.
- Inlined HTML/JS research UI at `/data-explorer` must function without regression.
- Deterministic extraction offsets and table separation must remain intact.
- Backward-compatible imports must be preserved during module refactoring.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_api.py tests\test_feature_tabs.py tests\test_citations.py -q`

Acceptance criteria:
- Hotspots identified and classified into clean ownership domains.
- First modularization slice completed with zero contract breaks.
- All relevant tests pass.
- Architecture docs / Swimm maps updated to reflect new module boundaries.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `OVERNIGHT.md`
- `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
- `.swm/overview.uhwv0wj2.sw.md`
- `.swm/system-map.ovnldklv.sw.md`

Rollback/recovery: Reversible Git branch/commit or file restores if tests fail.

Evidence:
1. Converted `.swm/blank.dudtv9pz.sw.md` into comprehensive Swimm walkthrough: `Repository Component Catalog and Directory Map` detailing all directories, module boundaries, script families, data isolation rules, and testing pyramids.
2. Extracted inlined HTML page builders from `backend/routes.py` (`_quick_search_page_html` -> `backend/pages/quick_search.py`, `_research_page_html` -> `backend/pages/research.py`), completing modularization of all UI page builders into `backend/pages/`.
3. Added clean `__all__` exports to `backend/pages/__init__.py`.
4. Validated 137 tests passing with 0 errors (`tests/test_api.py`, `tests/test_feature_tabs.py`, `tests/test_citations.py`, `tests/test_run_overnight.py`).
5. Resolved syntax warning on escaped regex literals in page modules.

## Hypothesis
If monolithic route/query/page logic or database configurations are modularized into dedicated domain packages with backward-compatible facade exports, all API and feature tab tests will pass without behavioral regressions while reducing complexity.

## Plan
1. Audit size, imports, and responsibilities across `backend/` (`routes.py`, `database.py`, `citations.py`, etc.).
2. Design candidate module boundaries (e.g. `backend/routes/` or extracting page builders into `backend/pages/`, query services, config).
3. Execute the first safe, high-impact slice (e.g., separating UI page rendering from API routing or separating query/analytics services).
4. Run focused validation and verify zero regression.
5. Update docs and task record with evidence.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | User requested project reorganization and modularization | This task file |
| 2026-09-03 | Replaced blank Swimm doc with comprehensive component catalog | Maximize context and eliminate token waste reading raw code | `.swm/blank.dudtv9pz.sw.md` |
| 2026-09-03 | Modularized quick_search and research page builders out of routes.py | Reduce monolithic routes.py by ~500 lines while preserving all API/UI contracts | `backend/pages/quick_search.py`, `backend/pages/research.py` |
| 2026-09-03 | Validated test suite | Confirm zero regressions across 137 tests | `pytest tests/test_*.py` 137 passed |

## Completion
Status: complete
Summary: Successfully created Swimm Component Catalog, modularized remaining inlined page builders from routes.py into backend/pages/, and verified all 137 focused tests pass.
Validation: `pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py -q` -> 137 passed in 3.68s.
Residual risk: None. All public import paths and HTTP endpoints preserved.
Next recommended task: Modularize search/retrieval query helpers or citation intelligence calculation services out of routes.py into dedicated backend services.
