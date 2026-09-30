# Task: Add bounded FC Activity panel charts

Status: complete
Created: 2026-09-29
Updated: 2026-09-29

## Task Record

Task: Retain the FC cases filed-per-year chart and add registry-location, case-class, and filing-track charts to the active `/data-explorer` FC History panel without restoring the overlapping procedural Sankey.

Why now: The FC History panel needs useful, interpretable activity context after the Sankey removal, using data already normalized in the active activity-case layer.

Owner surface: `backend/analytics_service.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/routes.py`, `backend/pages/data_explorer.py`, `fc_activity_cases`, FC History feature tests, `SYSTEM_REFERENCE.md`, `.swm/7.7le8istr.sw.md`, and `docs/RESEARCH_UI_GUIDE.md`.

Risk boundary: Preserve the annual filing chart and unrelated worktree changes. Do not query `raw_payload` or `classification_json`, add a full JSON scan, alter activity records, or imply that activity context is a captured judgment or a procedural outcome.

Smallest falsifiable check: `./venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -k "fc_activity" -q`.

Acceptance criteria:

- The FC History panel presents four coherent activity charts: yearly filings, registry locations, case classes, and filing tracks.
- The new metrics come from bounded SQL `GROUP BY` queries over structured `fc_activity_cases` columns and honor the existing city filter.
- No FC Activity Sankey is rendered or reintroduced.
- Focused FC Activity feature tests pass.

Harness criteria: Focused FC Activity feature tests pass after the chart service and UI changes.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/7.7le8istr.sw.md`, and this task record. No generated reference requires manual editing.

Rollback/recovery: Revert the bounded service, route, page, test, and documentation changes; no data migration or write is involved.

Evidence: Added `/api/fc-activity/breakdowns` backed by three bounded SQL `GROUP BY` queries over `fc_activity_cases.city_filed`, `fc_activity_cases.case_class`, and `fc_activity_cases.track`. The FC History panel retains the annual filed-case SVG and adds responsive top-$8$ registry-location, case-class, and filing-track bar charts. Focused validation passed: `./venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -k "fc_activity" -q` (`4 passed, 26 deselected`). Documentation checkpoint: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/7.7le8istr.sw.md` updated.

Files changed: `backend/analytics_service.py`, `backend/routes.py`, `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/7.7le8istr.sw.md`, and this task record.
Delegated work: Direct bounded worker slice; task-record and documentation checkpoint required by project instructions.
Focused validation: `./venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -k "fc_activity" -q` passed (`4 passed, 26 deselected`).
Residual risk: Top-$8$ distributions are descriptive inventory measures and may reflect source coverage or missing structured fields.
Next bounded task: Browser-check the FC History panel at desktop and mobile sizes against a running local API.

## Hypothesis

If the new charts aggregate `city_filed` and `case_class` directly in SQL from `fc_activity_cases`, then the panel can add useful non-overlapping activity context without scanning raw JSON or representing procedural outcomes as flow.

## Plan

1. Add a city-filtered, top-$8$ activity-case breakdown service and route.
2. Render the two compact SVG bar charts alongside the retained yearly chart.
3. Add focused contract/UI tests and update the FC activity documentation checkpoint.

## Execution Checkpoints

- Delegation: Direct bounded worker slice; no separate worker capability was available in this session.
- Implementation: Pending.
- Documentation: Pending `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/7.7le8istr.sw.md`.
- Recovery: No long operation or persisted state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Use annual filings, registry location, case-class, and filing-track distributions | These are directly structured activity-case fields, avoid classification overlap, and do not require JSON scans | `backend/database.py`, `backend/analytics_service.py`, and the FC Activity Swimm walkthrough |

## Completion

Completion recorded: yes

Summary: Added two bounded FC Activity inventory charts beside the retained annual filing timeline without restoring the overlapping procedural Sankey.

Validation: `./venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -k "fc_activity" -q` passed (`4 passed, 26 deselected`).

Residual risk: The distributions depend on current source coverage and structured-field completeness; a browser layout check against the live database remains useful.

Next recommended task: Browser-check the FC History panel at desktop and mobile sizes against a running local API.