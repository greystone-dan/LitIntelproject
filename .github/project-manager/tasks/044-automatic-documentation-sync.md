# Task: Automatic documentation sync

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

Task: Automatically detect generated-documentation drift on repository pushes and pull requests.
Why now: API, schema, and script-catalog references can become stale when code changes, while Swimm publication is not available through repository code alone.
Owner surface: Documentation generators and repository CI.
Dependencies: Existing `scripts/generate_api_reference.py`, `scripts/generate_schema_reference.py`, and `scripts/generate_script_catalog.py`.
Risk boundary: CI checks and reports drift; it does not rewrite committed files or publish to Swimm. Workflows do not run database writers.
Smallest falsifiable check: Run `scripts/check_generated_docs.py` and confirm all generated references match after timestamp normalization.
Acceptance criteria: Push/PR workflow exists; generated API/schema/script references are checked deterministically; schema generator ordering is stable; Swimm manual boundary is documented.
Docs/generated references: `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, generated references.
Rollback/recovery: Remove the workflow/checker and revert the deterministic generator ordering; generated outputs remain source-controlled.
Evidence:
- Added `.github/workflows/documentation-sync.yml` for push and pull-request checks.
- Added `scripts/check_generated_docs.py` with temporary regeneration and timestamp normalization.
- Sorted schema unique constraints in `scripts/generate_schema_reference.py` to eliminate nondeterministic drift.
- Regenerated API, schema, and script-catalog references.
- `scripts/check_generated_docs.py` passed: 3 references current.
- Python compilation and `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
