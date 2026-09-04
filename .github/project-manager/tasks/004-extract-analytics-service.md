# Task: Extract Analytics, Judge Profile, and FC History Service from Monolithic Routes

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Extract Judge Outcomes, Judge Profiles, Outcomes by Year, Data Explorer analytics, and Federal Court history/activity query logic out of `backend/routes.py` into a cohesive `backend/analytics_service.py` module while maintaining full backward compatibility.

Why now: `backend/routes.py` is ~3,085 lines long. Extracting analytics and reporting queries leaves `routes.py` as a lightweight HTTP routing layer (~1,500-2,000 lines) and creates a dedicated home for SQL aggregations, timeline builders, and profile matchers.

Owner surface: `backend/analytics_service.py` & `backend/routes.py`

Dependencies: `backend/models.py`, `backend/database.py`, `backend/fc_activity.py`, `tests/test_api.py`, `tests/test_feature_tabs.py`

Risk boundary:
- `/analytics/judge-outcomes`, `/analytics/outcomes-by-year`, `/analytics/explorer`, `/api/judge-profiles`, `/api/judge-profiles/{slug}`, `/api/fc-history`, `/api/fc-activity/*` responses must remain identical.
- Aggregation queries, percent calculations, and sorting must produce exact same outputs.
- Re-exported functions in `backend.routes` must remain backward-compatible for existing callers/tests.
- Zero breakages across the test suite.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_api.py tests\test_feature_tabs.py -q`

Acceptance criteria:
- Analytics logic cleanly extracted into `backend/analytics_service.py`.
- `backend/routes.py` delegates to `backend/analytics_service.py` while preserving all route endpoints and re-exported symbols.
- All tests in `tests/test_api.py`, `tests/test_feature_tabs.py`, `tests/test_citations.py`, and `tests/test_run_overnight.py` pass.
- Swimm documentation updated.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `.swm/blank.dudtv9pz.sw.md` (Repository Component Catalog)
- `.swm/overview.uhwv0wj2.sw.md`

Rollback/recovery: Revert changes to `backend/routes.py` and remove `backend/analytics_service.py` if regressions occur.

Evidence:
1. Created `backend/analytics_service.py` (778 lines) containing `fetch_outcomes_by_year`, `fetch_judge_outcomes`, `fetch_data_explorer_analytics`, `fetch_about_stats`, `fetch_fc_history_imm`, `fetch_fc_activity_timeline`, `fetch_fc_activity_analytics`, `fetch_judge_profiles`, `fetch_judge_profile_by_slug`, `fetch_analytics_search_cases`, `fetch_analytics_search_ministers`, `fetch_analytics_search_case_detail`, `_profile_reader_metadata`, `_government_party`, `_judge_outcome_counts`, `_analytics_case_order_sql`, `_ANALYTICS_FIELDS`, `FC_CITY_PROVINCE`, and `FC_ACTIVITY_DISPLAY_START_YEAR`.
2. Updated `backend/routes.py` to delegate all analytics, judge, and FC activity endpoints to `analytics_service`.
3. Preserved 100% backward compatibility for tests calling or monkeypatching `_analytics_case_order_sql` and other helper functions on `routes`.
4. `routes.py` reduced from 3,085 lines down to 2,533 lines (total reduction from original monolith: 4,799 -> 2,533 lines, nearly halved).
5. All 137 tests passing cleanly (`pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py`).
6. Updated Swimm Component Catalog (`.swm/blank.dudtv9pz.sw.md`).

## Hypothesis
If analytics, judge outcomes/profiles, and FC history queries are moved into `backend/analytics_service.py` and re-exported from `backend/routes.py`, all analytics endpoints, UI tabs, and test assertions will continue to function identically with zero behavioral regressions.

## Plan
1. Inventory analytics functions, helpers, and constants in `backend/routes.py`.
2. Create `backend/analytics_service.py` with clean encapsulation.
3. Update `backend/routes.py` to import and re-export symbols and delegate endpoint handlers.
4. Run `pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py -q`.
5. Update Swimm documentation and mark task complete.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Extract analytics domain from routes.py | This task record |
| 2026-09-03 | Created backend/analytics_service.py | Encapsulate SQL aggregations, judge profiles, and FC history timelines | `backend/analytics_service.py` |
| 2026-09-03 | Delegated endpoints in backend/routes.py | Maintain 100% backward compatibility with tests and callers | `backend/routes.py` |
| 2026-09-03 | Validated test suite | Confirm zero regressions across 137 tests | `pytest tests/test_*.py` 137 passed |
| 2026-09-03 | Updated Swimm Component Catalog | Keep architecture docs in sync | `.swm/blank.dudtv9pz.sw.md` |

## Completion
Status: complete
Summary: Successfully extracted analytics, judge profile, and FC history queries into `backend/analytics_service.py`, streamlined `backend/routes.py`, and validated all 137 tests pass.
Validation: `pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py -q` -> 137 passed in 16.67s.
Residual risk: None. All public API endpoints, response models, and helper symbols preserved.
Next recommended task: Modularize citation intelligence & graph route endpoints from `backend/routes.py` (which currently delegates ~40 citation-map endpoints) into a clean sub-router `backend/citation_routes.py` or similar.
