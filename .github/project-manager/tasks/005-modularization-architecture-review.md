# Task: Modularization Architecture Review & Centralized Router Boundary

Status: complete
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Review remaining route definitions in `backend/routes.py` and codify the boundary between the centralized FastAPI `routes.py` router and domain services (`search_service.py`, `reader_service.py`, `analytics_service.py`, `citation_map.py`, `ingestion.py`, `citations.py`, `pages/`).

Why now: With page builders, search/retrieval, reader data assembly, and analytics queries all extracted into dedicated domain modules, `backend/routes.py` has been reduced from 4,799 lines down to 2,533 lines. Retaining the lightweight 2-to-3 line endpoint decorators in `backend/routes.py` as a single authoritative FastAPI router avoids router splitting overhead and preserves 100% test monkeypatching compatibility.

Owner surface: `backend/routes.py` and architecture documentation

Dependencies: `backend/search_service.py`, `backend/reader_service.py`, `backend/analytics_service.py`, `backend/citation_map.py`, `backend/pages/`

Risk boundary:
- All 137 test suite assertions must pass.
- Public routes must remain registered and OpenAPI-discoverable.
- Domain services remain cleanly decoupled from HTTP handling.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_api.py tests\test_feature_tabs.py tests\test_citations.py tests\test_run_overnight.py -q`

Acceptance criteria:
- Clean, consistent router boundary documented.
- All 137 tests pass.
- Swimm documentation and task records synchronized.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `OVERNIGHT.md`
- `.swm/1.oi7rhqp2.sw.md`
- `.swm/blank.dudtv9pz.sw.md`

Rollback/recovery: None needed.

Evidence:
1. `backend/routes.py` successfully reduced from 4,799 lines to 2,533 lines (~2,266 lines of business logic, SQL, and HTML extracted).
2. Domain logic cleanly separated across:
   - `backend/search_service.py` (Search, vector similarity, tsvector ranking)
   - `backend/reader_service.py` (Reader data payload assembly, metadata pass, citation pass)
   - `backend/analytics_service.py` (SQL aggregations, judge profiles, FC history timelines)
   - `backend/citation_map.py` (Graph analytics,PageRank, authority lifecycles, hidden bridges)
   - `backend/pages/` (All 9 HTML client pages)
3. 137/137 tests passing in 14.29s.

## Hypothesis
Keeping `backend/routes.py` as the centralized, lightweight HTTP router delegating to domain services maximizes maintainability, keeps FastAPI route discovery simple, and maintains 100% backward compatibility.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Reaffirm centralized router + domain service architecture | Avoid sub-router fragmentation while keeping routes.py lightweight | All 137 tests pass |

## Completion
Status: complete
Summary: Modularization of backend services is complete. `backend/routes.py` is now a clean routing facade delegating to dedicated domain modules.
Validation: `pytest tests/test_*.py` -> 137 passed in 14.29s.
Residual risk: None.
Next recommended task: Address P0 items in the delivery roadmap (e.g. data quality metrics, browser smoke tests).
