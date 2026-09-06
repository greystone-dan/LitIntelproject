# Task: Reader evidence organization

Status: complete
Created: 2026-09-05
Updated: 2026-09-05

Task: Improve the active Data Explorer reader organization without removing search, reader, citation, statute, tag, or source-link functionality.
Why now: The backend already exposes distinct evidence layers and exact offsets, but the reader's legend and evidence inspection affordance were difficult to discover.
Owner surface: `backend/pages/data_explorer.py` and feature-tab coverage.
Dependencies: Existing reader HTML/data attributes and read-only citation/tag/statute contracts.
Risk boundary: Front-end-only additive change; no API, database, extraction, or live V2 pipeline changes.
Smallest falsifiable check: Rendered Data Explorer shell contains the evidence-details control and existing layer highlights remain present.
Acceptance criteria: Reader exposes Tags/Laws/Citations legend plus an accessible evidence-details toggle and inline inspector for existing highlights; case search and reader behavior remain intact.
Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, relevant Swimm active-UI walkthrough.
Rollback/recovery: Revert the page-builder CSS/HTML/JS and focused test; no data recovery required.
Evidence:
- Added persistent `Show evidence details` control and delegated highlight inspector to the active reader.
- Existing citation/statute/tag color classes remain unchanged.
- Focused feature-tab tests passed: `2 passed`.
- Python compilation and `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
