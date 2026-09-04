# Task: Design Reversible Self-Citation Cleanup Plan

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Add a dry-run planner for candidate self-citation cleanup based on the bounded audit classifications.
Why now: Existing self-citation rows block the quality gate, while future rebuilds now prevent exact source-case citations from being persisted.
Owner surface: `scripts/plan_self_citation_cleanup.py`
Dependencies: `scripts/audit_self_citations.py`, `backend/database.py`, citation rows and source case text
Risk boundary: Dry-run only; no deletes, updates, commits, migrations, or automatic cleanup. Candidate classifications are not deletion authorization.
Smallest falsifiable check: Run the planner with `--limit 100` and confirm it emits a candidate report with `write_performed: false`.
Acceptance criteria: Produce bounded candidate IDs, classifications, counts, and a proposed review order suitable for a later reversible canary.
Docs/generated references: Swimm Technical Debt Register and Improvement Queue; Swimm Evaluation Framework and Quality Metrics; generated script catalog.
Rollback/recovery: Remove the planner and report documentation; no data rollback is needed.
Evidence: Added `scripts/plan_self_citation_cleanup.py`, a bounded read-only planner with a hard 1,000-row limit, classification counts, safe context excerpts, review order, `write_performed=False`, and `cleanup_authorized=False`. Live `--limit 100` output matched the audit split: 40 source-header citations, 36 source-header artifacts, and 24 review candidates. Added a non-destructive planner test (`1 passed`), regenerated the script catalog, and ran the full suite (`319 passed`). `git diff --check` passed.
