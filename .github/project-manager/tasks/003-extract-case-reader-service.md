# Task: Extract Case Reader and Metadata Service from Monolithic Routes

Status: in-progress
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Extract case-reader payload construction (`/cases/{case_id}/reader-data`), metadata extraction formatting, citation detail resolution, tag inference, and HTML reader formatting out of `backend/routes.py` into a dedicated `backend/reader_service.py` module while preserving full backward compatibility.

Why now: `backend/routes.py` is still over 3,800 lines long and contains complex payload formatting for the inline reader and metadata pass mixed with route definitions. Extracting this domain reduces monolith complexity and isolates reader evidence formatting.

Owner surface: `backend/reader_service.py` & `backend/routes.py`

Dependencies: `backend/models.py`, `backend/database.py`, `backend/citations.py`, `tests/test_api.py`

Risk boundary:
- `/cases/{case_id}/reader-data` and `/cases/{case_id}/citation-pass` responses must remain identical.
- Extracted metadata fields, normalized display rows, and citation details must retain exact shapes.
- Direct symbol imports/accesses on `backend.routes` (e.g., `_stored_case_citation_details`, `get_case_metadata_pass`, `_build_reader_extracted_metadata`) must remain exported and backward-compatible.
- Zero breakages across the test suite.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_api.py tests\test_feature_tabs.py -q`

Acceptance criteria:
- Reader payload and metadata pass logic cleanly extracted into `backend/reader_service.py`.
- `backend/routes.py` delegates to `backend/reader_service.py` while preserving all route endpoints and re-exported symbols.
- All tests in `tests/test_api.py`, `tests/test_feature_tabs.py`, and `tests/test_citations.py` pass.
- Swimm documentation updated.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `.swm/blank.dudtv9pz.sw.md` (Repository Component Catalog)
- `.swm/overview.uhwv0wj2.sw.md`

Rollback/recovery: Revert changes to `backend/routes.py` and remove `backend/reader_service.py` if regressions occur.

Evidence:
1. Created `backend/reader_service.py` (1,032 lines) containing `build_case_reader_data`, `build_case_citation_pass`, `build_case_citation_pass_detail`, `get_case_metadata_pass`, `_build_reader_inferred_tags`, `_build_reader_extracted_metadata`, `_build_metadata_pass_normalized_rows`, `_format_reader_html`, `_stored_case_citation_details`, `_stored_statute_reference_details`, and `_citation_pass_chunks`.
2. Updated `backend/routes.py` to import and re-export all reader/citation-pass symbols and delegate route handlers directly to `reader_service`.
3. Preserved 100% backward compatibility for test monkeypatching of extraction and DB retrieval functions on `routes`.
4. `routes.py` reduced from 3,840 to 3,085 lines (total modularization progress: 4,800 -> 3,085 lines, ~1,715 lines eliminated from the monolith).
5. All 137 tests passing cleanly (`pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py`).
6. Updated Swimm documentation (`.swm/blank.dudtv9pz.sw.md`).

## Hypothesis
If case reader payload assembly and metadata formatting functions are moved into `backend/reader_service.py` and re-exported from `backend/routes.py`, all reader endpoints, citation-pass details, and test calls on `routes` will continue to function identically with zero behavioral regressions.

## Plan
1. Inventory reader-data, metadata pass, and citation detail functions in `backend/routes.py`.
2. Create `backend/reader_service.py` with clean encapsulation.
3. Update `backend/routes.py` to import and re-export symbols and delegate endpoint handlers.
4. Run `pytest tests/test_api.py tests/test_feature_tabs.py -q`.
5. Update Swimm documentation and mark task complete.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Extract reader domain from monolithic routes.py | This task record |
| 2026-09-03 | Created backend/reader_service.py | Encapsulate reader data, metadata pass, citation pass details, and HTML citation wrapping | `backend/reader_service.py` |
| 2026-09-03 | Re-exported reader facade in backend/routes.py | Maintain 100% backward compatibility with test monkeypatching | `backend/routes.py` |
| 2026-09-03 | Validated test suite | Confirm zero regressions across 137 tests | `pytest tests/test_*.py` 137 passed |
| 2026-09-03 | Updated Swimm Component Catalog | Keep architectural catalog in sync with new module | `.swm/blank.dudtv9pz.sw.md` |

## Completion
Status: complete
Summary: Successfully extracted case-reader, metadata pass, and citation-pass service into `backend/reader_service.py`, streamlined `backend/routes.py`, and validated all 137 tests pass.
Validation: `pytest tests/test_api.py tests/test_feature_tabs.py tests/test_citations.py tests/test_run_overnight.py -q` -> 137 passed in 17.68s.
Residual risk: None. All public endpoints, models, and monkeypatchable symbols preserved.
Next recommended task: Modularize judge profile, judge outcomes, and FC history analytics endpoints from `backend/routes.py` into a dedicated `backend/analytics_service.py`.
