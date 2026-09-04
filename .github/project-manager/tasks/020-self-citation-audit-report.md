# Task: Add Self-Citation Audit Report

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Create a bounded read-only audit report that classifies existing self-citation rows before any cleanup decision.
Why now: The quality gate found 241,272 self-citation rows, and a sample identified source-header citation artifacts, but the full population needs measured classification.
Owner surface: `scripts/audit_self_citations.py`
Dependencies: `backend/database.py`, existing `citations` and `cases` data, Swimm quality/debt walkthroughs
Risk boundary: Read-only only; no deletes, updates, commits, migrations, or automatic cleanup. Sample limits are mandatory and output must not expose secrets.
Smallest falsifiable check: Run the classifier tests and `--help`; with a live database, run a bounded `--limit 100` report.
Acceptance criteria: Report total sampled rows, classifications, representative safe metadata/context, and a recommendation input for reversible cleanup design.
Docs/generated references: Swimm Technical Debt Register and Improvement Queue; Swimm Evaluation Framework and Quality Metrics; generated script catalog.
Rollback/recovery: Remove the audit script and report documentation; no data rollback is needed.
Evidence: Added `scripts/audit_self_citations.py`, a bounded read-only classifier with a hard 1,000-row maximum, safe context samples, JSON output, and explicit `write_performed: false`. Unit tests passed (`3 passed`); CLI compile/help passed; the live `--limit 100` audit found 241,272 total self-citations and classified the sample as 40 exact source-citation headers, 36 source-header caption artifacts, and 24 remaining candidates. No data was modified.
