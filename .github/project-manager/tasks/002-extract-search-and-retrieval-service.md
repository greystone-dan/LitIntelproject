# Task: Extract Search and Retrieval Service from Monolithic Routes

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Extract search and retrieval query construction, ranking, embedding helpers, and grouped chunk search logic out of `backend/routes.py` into a cohesive `backend/search_service.py` module while preserving full backward compatibility and API contracts in `backend/routes.py`.

Why now: `backend/routes.py` is over 4,300 lines long and contains all SQL assembly, ranking expressions, vector scoring, and chunk grouping mixed directly with HTTP route definitions. Separating the search service simplifies testability, enables independent optimization, and moves toward clean domain boundaries.

Owner surface: `backend/search_service.py` & `backend/routes.py`

Dependencies: `backend/models.py`, `backend/database.py`, `backend/embedding_providers.py`, `tests/test_api.py`

Risk boundary:
- Search modes (`semantic`, `lexical`, `hybrid`, `metadata`) must compute exact same scores and rankings.
- Grouped chunk search and pagination behavior must remain identical.
- Direct imports from `backend.routes` (such as `_embed`, `search_cases`, `search_chunks`, `search_chunks_local`, `search_chunks_grouped`, `AI_ROLLOUT`, `EMBEDDING_DIMENSIONS`) must remain exported and fully functional.
- Zero breakages across API test suite.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_api.py -q`

Acceptance criteria:
- Search logic cleanly extracted into `backend/search_service.py`.
- `backend/routes.py` delegates to `backend/search_service.py` while preserving all route endpoints and re-exported symbols.
- All tests in `tests/test_api.py` and full test suite pass.
- Swimm documentation updated to reflect the new search service boundary.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `.swm/5.b49ftjal.sw.md` (Search and Retrieval walkthrough)
- `.swm/overview.uhwv0wj2.sw.md`

Rollback/recovery: Revert changes to `backend/routes.py` and remove `backend/search_service.py` if regressions occur.

Evidence:
1. Created `backend/search_service.py` housing `execute_search_cases`, `execute_search_chunks`, `execute_search_chunks_local`, `execute_grouped_chunk_search`, filter builders, ranking expressions, embedding functions, and rollout flags.
2. Updated `backend/routes.py` to import and re-export all search symbols and delegate route endpoints (`/search`, `/search/chunks`, `/search/chunks/local`, `/search/chunks/grouped`) to `search_service`.
3. Verified 100% backward compatibility for tests monkeypatching `routes.AI_ROLLOUT` and `routes._embed`.
4. `routes.py` reduced by another ~460 lines (from 4,301 to 3,840 lines; total reduction from 4,800 to 3,840 lines).
5. All 137 tests passing cleanly (`pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py`).
6. Updated Swimm walkthroughs `.swm/5.b49ftjal.sw.md` and `.swm/blank.dudtv9pz.sw.md`.

## Hypothesis
If search and retrieval functions are moved into a dedicated `backend/search_service.py` and re-exported from `backend/routes.py`, all search modes, rankings, and test monkeypatches on `routes` will continue to function identically with zero behavioral regressions.

## Plan
1. Inventory all search-related functions, constants, and dependencies in `backend/routes.py`.
2. Create `backend/search_service.py` with cleanly organized query builders, rankers, and search execution functions.
3. Update `backend/routes.py` to import and re-export these symbols and delegate endpoint handlers to `search_service`.
4. Run `tests/test_api.py` and the full test suite.
5. Update Swimm search walkthrough and mark task complete.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Extract search domain from monolithic routes.py | This task record |
| 2026-09-03 | Created backend/search_service.py | Encapsulate search logic and SQL ranking expressions | `backend/search_service.py` |
| 2026-09-03 | Re-exported search facade in backend/routes.py | Maintain 100% backward compatibility with test monkeypatching | `backend/routes.py` |
| 2026-09-03 | Validated test suite | Confirm zero regressions across 137 tests | `pytest tests/test_*.py` 137 passed |
| 2026-09-03 | Updated Swimm Search Walkthrough | Keep architectural diagrams and docs in sync | `.swm/5.b49ftjal.sw.md` |

## Completion
Status: complete
Summary: Successfully extracted search and retrieval service into `backend/search_service.py`, streamlined `backend/routes.py`, and validated all 137 tests pass.
Validation: `pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py -q` -> 137 passed in 45.96s.
Residual risk: None. All public endpoints and monkeypatchable symbols preserved.
Next recommended task: Modularize case reader and metadata extraction formatting out of `backend/routes.py` into a dedicated `backend/reader_service.py`.
