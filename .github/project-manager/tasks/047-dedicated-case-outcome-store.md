# Task: Dedicated case outcome store

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

Task: Make outcome intelligence its own persisted source of truth while retaining metadata mirrors for compatibility.
Why now: Outcome logic is currently derived in its own module but stored only inside `metadata_json.reader_extracted`, which limits queryability, versioning, and auditability.
Owner surface: `backend/metadata_outcomes.py`, `backend/database.py`, `backend/case_processing.py`, outcome migration/backfill, outcome tests, and outcome Swimm documentation.
Dependencies: Canonical case text, caption/party metadata, existing deterministic outcome derivation, Alembic, metadata compatibility payload.
Risk boundary: Additive schema and writes only. Do not delete existing metadata fields or rewrite source/citation/statute/tag rows. Dedicated outcome rows must retain explicit unknown/mixed states and evidence offsets.
Smallest falsifiable check: A processed case writes one versioned `case_outcomes` row with the same winner/disposition/evidence as the compatibility metadata mirror; rerunning replaces only that version's row.
Acceptance criteria: Dedicated ORM table and migration exist; ordered processing writes versioned outcome rows; bounded backfill script exists; active outcome consumers can migrate later; existing metadata/API behavior remains compatible; focused tests pass.
Alternatives considered: Keep metadata-only (cheapest but not independent); dedicated current outcome row plus mirror (recommended); append-only outcome history (stronger provenance but premature complexity).
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/METRICS_DICTIONARY.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, relevant `.swm/` outcome/evaluation walkthrough, generated schema reference.
Rollback/recovery: Drop only the new outcome version/table after backup or stop the outcome stage; metadata mirror remains available.
Evidence:
- Added `CaseOutcome` ORM model and additive Alembic migration `0022_case_outcomes`
	with versioned normalized outcome fields, challenged issues, confidence, and
	evidence offsets.
- Added the ordered `outcome` processing stage and bounded resumable
	`scripts/backfill_case_outcomes.py` writer.
- Applied migration `0022_case_outcomes` to the configured database.
- Dry-run previewed 25 pending cases with 25 outcome records and no writes.
- Bounded canary wrote 25 `deterministic_outcome_v1` rows; statuses were 8 won,
	11 lost, and 6 undetermined. Twenty-four rows had valid positive evidence
	spans; one undetermined row had no disposition span as expected.
- Updated `SYSTEM_REFERENCE.md`, `LEGAL_TAGGING.md`, `OVERNIGHT.md`,
	`docs/METRICS_DICTIONARY.md`, and the Swimm evaluation walkthrough.
- Generated schema and script references are current; focused tests passed
	(`26 passed`) and `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
