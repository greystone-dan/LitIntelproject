# Change Management Rules

Last reviewed: 2026-09-01

These rules keep AI CaseLibrary changes traceable, testable, and recoverable. They apply to code, schema, extraction, data acquisition, UI, documentation, operational jobs, and release checkpoints.

## Universal Change Loop

1. Identify the owning module and a falsifiable local behavior expectation.
2. Inspect the smallest relevant test, call site, schema, or live route.
3. Make the smallest coherent change.
4. Run the narrowest validation that can disprove the change.
5. Repair the same slice if validation fails; do not expand scope until it passes or is classified.
6. Run broader validation proportionate to blast radius.
7. Update generated/human documentation, changelog, and runbooks as needed.
8. Review `git diff --check`, preserve unrelated worktree changes, and create a coherent checkpoint.

## Schema Or Migration Change

1. Update ORM model and Pydantic/API contracts together where the field is exposed.
2. Create an Alembic migration with forward and rollback behavior appropriate to the data.
3. Consider existing data, indexes, nullability, uniqueness, foreign keys, and delete behavior.
4. Run `alembic current`, `alembic heads`, and a controlled upgrade in the intended environment.
5. Regenerate `docs/SCHEMA_REFERENCE.generated.md`.
6. Test affected ingestion, query, reader, and migration paths.
7. Document backfill plan, expected duration, lock/write contention, and recovery strategy before corpus-scale execution.

## New Or Changed Data Source

1. Add the source to `docs/DATA_SOURCE_REGISTER.md` before broad import.
2. Define source class, licence/terms, official/secondary/staging status, stable identity, source URL, and retrieval timestamp.
3. Define source type, merge priority, deduplication key, raw/staging storage, canonical bridge, and failure behavior.
4. Preserve provenance and source conflicts; do not silently overwrite superior source data.
5. Add mock/fixture tests and a bounded dry run.
6. Do not bypass court/site access controls or mislabel discovered/staged data as captured official material.

## Extractor Or Classifier Change

1. State which layer changes: case citations, statutes/instruments, metadata, tags, or FC activity classification.
2. Add a positive fixture, a negative/near-miss fixture, and exact offset assertions where text spans are stored.
3. Keep case citations and statute references separate.
4. For IRPA/IRPR work, test nested forms such as `34(1)(f)` with punctuation and heading/running-text variants.
5. Run focused tests, then a bounded real-case/sample audit before corpus-wide rebuild.
6. Record expected/matched/missing/unexpected rows and span errors; do not treat higher row count as automatic improvement.
7. Version taxonomy/classifier output where its semantics change.

## Search, API, Or Analytics Change

1. Update Pydantic request/response models and route validation when the external contract changes.
2. Bound limits, pagination, candidate pools, date ranges, and expensive graph traversals.
3. Preserve source/provenance and distinguish occurrence counts from unique entities.
4. Add route tests for happy path, invalid input, and upper-bound behavior.
5. Regenerate `docs/API_REFERENCE.generated.md` when FastAPI route/schema output changes.
6. Add CSV/export coverage when an analytical JSON route has a paired export contract.

## UI Or Reader Change

1. Treat `backend/routes.py` generated HTML/CSS/JavaScript as a coupled frontend artifact.
2. Preserve backend-owned citation/statute offsets; never use browser-only calculations to replace stored evidence locations.
3. For JavaScript regex/string changes inside Python strings, use correct raw/double escaping.
4. Run `py_compile`, `test_feature_tabs.py`, affected route tests, and manual browser checks.
5. Check desktop and mobile layout, long decision scrolling, hover clipping, linked authority navigation, empty states, and text overflow.
6. Do not refactor duplicate renderer/wrapper chains without browser regression coverage.

## Operational Script Or Bulk Data Change

1. Update the script catalog and recovery guide if invocation/risk/recovery changes.
2. Provide or preserve `--help`, bounded limit, dry-run, resume, and/or preflight behavior where appropriate.
3. Use keyset pagination, bounded batches, commits, state/log output, and idempotent keys for large writes.
4. Never run a competing PostgreSQL writer while `run_overnight.py` or another bulk writer may be active.
5. Record before/after counts, command, scope, timestamp, run ID, errors, and sampled verification.
6. Resume interrupted work where supported; do not restart blindly.

## Configuration Or Security Change

1. Update `docs/CONFIGURATION_REFERENCE.md` and `.env.example` with placeholders only.
2. Test environment precedence, missing/invalid values, and secure defaults.
3. Never commit secrets. Revoke/rotate any credential accidentally written to tracked history or shared output.
4. Treat no-index/robots headers as indexing controls, not authentication.
5. For access control changes, test anonymous denial, valid login/cookie access, expiration, local behavior, HTTPS cookie flags, and reverse-proxy/tunnel paths.

## Documentation Change

1. Put current system architecture/functionality in `SYSTEM_REFERENCE.md` or its linked canonical appendices.
2. Keep `CHANGELOG.md` chronological and test-backed; keep `WORK_HISTORY.md` as generated activity/delivery record.
3. Regenerate API, schema, script, or work-history documents after their sources change.
4. Validate local links and run `git diff --check`.
5. Move superseded snapshots to `docs/history/` and label them historical rather than editing history into a false current state.

## Large Artifacts And Git Checkpoints

1. Do not add raw corpora, backups, logs, or secrets to ordinary Git history.
2. Use Git LFS only for deliberate large tracked artifacts; confirm the LFS object transfers before calling GitHub synchronized.
3. Inspect `git status`, staged diff, and file sizes before committing.
4. Keep commits coherent by feature or release checkpoint.
5. Never reset/revert unrelated user work to make a commit or push convenient.
6. After a failed LFS push, retain the local commit, report remote divergence, and resume only when the transfer is intended.

## Release Checkpoint

Before declaring a change stable:

1. Focused tests pass for every touched behavior.
2. Touched Python modules compile and diagnostics are clean.
3. Relevant generated documentation is refreshed.
4. Browser/API smoke checks pass for user-facing changes.
5. Full-suite result is recorded honestly, including known failures.
6. Migrations have an applied/rollback/backfill plan if schema changed.
7. Source, security, configuration, large-file, and deployment implications are documented.
8. `git diff --check` is clean and the local/remote Git state is known.