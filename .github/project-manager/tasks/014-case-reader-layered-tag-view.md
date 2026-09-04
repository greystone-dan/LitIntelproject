# Task: Improve Case Reader Layered Evidence View

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Make tags, statutes, and case citations distinct and usable in the active inline Case Reader.
Why now: The reader already highlights the three evidence layers, but the Tags panel exposed only live keyword candidates instead of all stored/inferred tags and their individual occurrences.
Owner surface: `backend/pages/data_explorer.py`
Dependencies: `backend/reader_service.py`, `tests/test_feature_tabs.py`, active `/data-explorer` reader workflow
Risk boundary: Preserve backend-owned offsets and separate citation/statute/tag layers; keep existing reader, linked authority, and tab behavior intact.
Smallest falsifiable check: Search a known case in the browser, open the reader, and verify green/purple/yellow highlights plus grouped Tags with occurrence details.
Acceptance criteria: All tags are visible; tags are grouped by unique category/value; each occurrence exposes evidence, source, score, taxonomy, and offsets when available; citations remain yellow, laws purple, and tags green.
Docs/generated references: Swimm active UI walkthrough and `docs/RESEARCH_UI_GUIDE.md`.
Rollback/recovery: Revert the focused page/test/docs changes if browser interaction or reader layer rendering regresses.
Evidence: Added grouped unique-tag and occurrence rendering to the active Case Reader, preserving backend-owned evidence fields. Browser validation through a Vavilov search confirmed 19 unique tags across 111 occurrences, 71 green tag highlights, 40 purple statute highlights, and 33 yellow citation highlights; citations, Acts / Regs, and Precedents tabs remained usable with no browser page errors. `py_compile` passed, focused feature tests passed (13), focused combined tests passed (20), full suite passed (311), and `git diff --check` passed.
