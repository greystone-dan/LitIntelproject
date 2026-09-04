# Task: Preserve Repeated Inferred Tag Occurrences

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Preserve repeated reader-inferred tag occurrences so the Case Reader does not imply that a repeated term occurred only once.
Why now: `Ou v. Canada` contains 18 standalone `ID` mentions while the reader payload exposed one `forum:id` row because inferred tags were deduplicated by category/value.
Owner surface: `backend/reader_service.py` inferred reader-tag generation
Dependencies: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, reader-data contract
Risk boundary: Keep persisted tags, deterministic extraction layers, source provenance, and backend-owned offsets unchanged; apply a bounded occurrence limit to live inferred tags.
Smallest falsifiable check: Fetch OU v. Canada reader data and confirm multiple `forum:id` inferred rows with distinct evidence excerpts.
Acceptance criteria: Repeated inferred matches are represented as separate bounded tag occurrences; UI grouping still presents one unique tag with an occurrence count; existing reader and extraction tests remain green.
Docs/generated references: Swimm active UI walkthrough and `docs/RESEARCH_UI_GUIDE.md`.
Rollback/recovery: Revert the inferred-tag occurrence change if payload size or reader rendering becomes excessive.
Evidence: Confirmed OU v. Canada had 18 standalone `ID` tokens but one inferred tag because reader inference deduplicated category/value. Updated inference to use one canonical full-text representation and retain repeated matches up to 50 per inferred tag. Live payload now reports 27 `forum: id` matches, including the rule's `Immigration Division` phrase matches, with 79 total tag rows. Browser validation showed 11 unique groups and 27 expandable `forum: id` occurrences with no page errors. Added `tests/test_reader_tag_occurrences.py`; focused tests passed (14), API/UI tests passed (55), and full suite passed (312). `git diff --check` passed.
