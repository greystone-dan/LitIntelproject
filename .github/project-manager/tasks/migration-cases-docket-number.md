# Task: Add idempotent docket-number schema migration

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add a safe Alembic migration for `cases.docket_number` and verify fresh-schema parity with the `Case` ORM model.

Why now: Issue #223 reports PostgreSQL fresh-migration tests fail because the ORM declares the docket field and index but the migration graph does not create them.

Owner surface: Schema evolution (`alembic/` and its focused migration tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Current Alembic head; `backend/database.py` model metadata; disposable PostgreSQL with pgvector for the gated migration test.

Risk boundary: Only create the missing nullable `String(255)` column and declared index. Never drop or alter existing columns or data. Do not access any live database, `.env`, or deploy scripts; do not weaken or hide PostgreSQL tests.

Smallest falsifiable check: Run the inspector-mocked idempotency test without pytest DB fixtures; PostgreSQL parity test requires an explicit disposable-service opt-in and skips if PostgreSQL is unavailable.

Acceptance criteria:

- A new revision on the actual current head idempotently adds only the missing column and index and has a safe downgrade.
- A PostgreSQL-gated migration-from-zero test compares migrated `cases` columns and indexes against `Case` metadata.
- A cheap SQLite/inspector-free idempotency test covers existing/missing column and index states.
- Regenerate schema docs and update the schema canonical documentation and database walkthrough.
- Focused checks, full pytest suite, generated-doc check, final parallel validation, and modified-file secret scan are run or recorded as unavailable/failing.

Harness criteria:

- Focused migration/idempotency tests pass; PostgreSQL case runs or skips cleanly.
- Generated schema reference is current.
- Canonical documentation and database walkthrough are updated.
- Full suite and generated-doc check results are recorded honestly.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/2.40nypbay.sw.md`, and generated `docs/SCHEMA_REFERENCE.generated.md` via `scripts/generate_schema_reference.py`.

Rollback/recovery: Before deployment, revert this new migration and accompanying test/docs changes. Downgrade is intentionally a no-op because the migration cannot distinguish pre-existing objects; after deployment, do not expect downgrade to remove the column/index.

Evidence: Issue #223 and issue #112 constraints were read. Managed worker returned the new migration/test files. Manager review added explicit test opt-in/dotenv guards, corrected a failing SQLAlchemy type assertion, advanced the graph test, and wired the PostgreSQL test into the existing disposable pgvector workflow with skip rejection. Final parallel validation: the inspector-mocked test passed (1, no DB); `py_compile` passed; Alembic reported `0037_cases_docket_number (head)`; workflow YAML parsed; whitespace and high-confidence credential scans were clean. `python scripts/generate_schema_reference.py` passed and refreshed `docs/SCHEMA_REFERENCE.generated.md`. `python scripts/check_generated_docs.py` was attempted but failed because `fastapi` is not installed. Full pytest and the PostgreSQL migration test were not run: user prohibited database use, and pytest's `tests/conftest.py` probes a configured database at import. No throwaway PostgreSQL was started or probed; no database or `.env` contents were accessed, and no deploy script was accessed or modified.

Files changed: `.github/project-manager/tasks/migration-cases-docket-number.md`, `.github/workflows/pgvector-tests.yml`, `.swm/2.40nypbay.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `alembic/versions/0037_cases_docket_number.py`, `docs/SCHEMA_REFERENCE.generated.md`, `tests/test_cases_docket_number_migration.py`, `tests/test_migrations.py`.
Delegated work: Managed worker implemented only the new migration/test files and reported static compile/whitespace success; its initial mocked test could not import because SQLAlchemy was unavailable. Manager installed dependencies only under `/tmp`, reviewed and repaired the assertion, and reran the DB-free test successfully.
Focused validation: Inspector-mocked test passed (1); migration/test compilation passed; Alembic reports one head `0037_cases_docket_number`; workflow YAML parsed; schema generation, `git diff --check`, whitespace scan, and credential scan passed. Full generated-doc check failed on missing FastAPI; no database tests were run by instruction.
Residual risk: The PostgreSQL migration-from-zero test and full suite remain unexecuted; CI's disposable pgvector workflow now runs the migration test and rejects silent skips.
Next bounded task: Run the pgvector workflow on its disposable Postgres service and address any migration/model parity failure.

## Hypothesis

If the migration and guard helper are correct, running the migration from zero produces the exact `Case`-declared docket column/index without changing pre-existing schema objects, and the targeted tests demonstrate both paths.

## Plan

1. Delegate the bounded migration and focused test implementation after confirming actual revision/test conventions.
2. Independently accept the schema behavior, refresh generated schema and required documentation.
3. Run focused and requested broad validation, secret scan modified files, and parallel validation.

## Execution Checkpoints

- Delegation: Managed worker assigned only the Alembic migration and focused migration tests; structured return required.
- Implementation: Added `0037_cases_docket_number`; focused mocked check passes.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/2.40nypbay.sw.md`; generated schema reference refreshed.
- Recovery: No database operation; no long-running job state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created; owner is schema evolution | Issue #223 requires one additive, idempotent migration and migration-from-zero coverage | Issue #223; `backend/database.py` owner documented in system reference and database walkthrough |
| 2026-10-04 | Require explicit disposable PostgreSQL opt-in before migration test can connect | Existing test infrastructure probes configured DBs; isolate the new integration test and ensure CI rejects a skip | Reviewed `tests/conftest.py`, `.github/workflows/pgvector-tests.yml`, and project database walkthrough |
| 2026-10-04 | Run gated test in existing disposable pgvector workflow | Standard pytest suite does not set the integration opt-in; CI must exercise and reject skips for this test | `.github/workflows/pgvector-tests.yml` sets `CASELIBRARY_PGVECTOR_TESTS=1` and checks two test results |

## Completion

Completion recorded: yes

Summary: Added the idempotent schema revision, direct tests, disposable-workflow coverage, and required generated/canonical/Swimm documentation.

Validation: The database-free mocked idempotency test, compilation, graph-head inspection, schema generation, diff check, and credential scan passed. The full generated-doc check lacked FastAPI; database tests/full pytest were not run under the no-DB boundary.

Residual risk: PostgreSQL migration-from-zero parity is CI-only and has not run in this environment.

Next recommended task: Run the pgvector workflow against disposable PostgreSQL and confirm the fresh-migration comparison plus existing PostgreSQL tests pass.
