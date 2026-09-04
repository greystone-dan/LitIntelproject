# Task: Add Data Explorer Browser Smoke Coverage

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Add a bounded Playwright smoke command for the active Data Explorer and inline Case Reader journeys.
Why now: Route tests and static HTML checks cannot detect asynchronous reader rendering, stale script behavior, layer-tab failures, or mobile layout regressions.
Owner surface: `scripts/browser_smoke.py`
Dependencies: Running site from `scripts/refresh_site.ps1`, installed Playwright browser, active `/data-explorer` workflow
Risk boundary: Read-only browser validation; do not start servers, modify data, or treat a smoke pass as comprehensive legal or accessibility QA.
Smallest falsifiable check: Run the smoke command against `http://127.0.0.1:8000` and verify search, reader tabs, tag groups, layer legend, and mobile Themes loading.
Acceptance criteria: A bounded command validates desktop search-to-reader behavior, all evidence-layer tabs, grouped tag output, and mobile Themes loading.
Docs/generated references: `OVERNIGHT.md`, Swimm active UI walkthrough, `docs/RESEARCH_UI_GUIDE.md`.
Rollback/recovery: Remove the smoke script and documentation command if the harness becomes unreliable or conflicts with the supported environment.
Evidence: Browser smoke passed against `http://127.0.0.1:8000` using query `Vavilov`: reader tabs detected, 16 tag groups and 317 occurrences rendered, Tags/Laws/Citations legend detected, and mobile Themes loaded. The initial attempt exposed an asynchronous wait defect and was repaired by waiting for the reader tab container.
