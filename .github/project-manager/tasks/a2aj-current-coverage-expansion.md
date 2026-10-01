# Task: Assess A2AJ current-coverage expansion

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Determine whether AI CaseLibrary can safely acquire and ingest additional Canadian Legal Data from A2AJ through the present day.

Why now: The canonical case corpus is substantial but incomplete, and A2AJ may provide newer or missing Canadian decisions.

Owner surface: A2AJ acquisition, curation, and canonical-ingestion boundary under `scripts/` and `backend/ingestion.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: A2AJ source coverage and terms/licence, existing A2AJ scripts/manifests, canonical identity/merge policy, database capacity, and approval for any external acquisition or bulk write.

Risk boundary: Read-only inventory and source-contract assessment only in this phase. No bulk download, paid API, credential use, source-term decision, production write, canonical merge, or unbounded operation without explicit approval.

Smallest falsifiable check: Identify the existing A2AJ acquisition/curation/import path and run its narrowest non-mutating help/preflight or fixture test; establish whether a bounded date/ID probe is possible without writing canonical data.

Acceptance criteria:

- Establish current A2AJ corpus coverage, date/identifier strategy, and likely present-day gap from repository evidence.
- Map source terms/provenance, staging, deduplication, and canonical merge protections.
- Define the smallest safe next experiment for a bounded recent-case probe or fixture-only import.
- Record focused validation and all external-operation approval boundaries.
- Update one canonical source/operations document and the relevant Swimm walkthrough.

Harness criteria: A2AJ path and current coverage are evidenced; Provenance/licence/merge boundaries are documented; Bounded next experiment is defined; Focused validation result is recorded; Canonical document and Swimm walkthrough are named and updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/DATA_SOURCE_REGISTER.md`, relevant A2AJ runbook, and relevant `.swm/` walkthrough.

Rollback/recovery: No acquisition or write in discovery. Revert documentation/task changes only; preserve any read-only reports and do not delete source data.

Evidence: Read-only inventory, live canonical date/count query, staging-file metadata check, one bounded public API probe, focused fixture tests, documentation checkpoint, and managed-run evidence are recorded below. Managed run: `.github/project-manager/runs/a2aj-current-coverage-expansion-20260930-124102-6d97a2ff`. The live API probe returned HTTP 400 for the attempted search shape; this is treated as an unresolved contract, not as proof that A2AJ has no current data.

Files changed: `.github/project-manager/tasks/a2aj-current-coverage-expansion.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`
Delegated work: Explore agent performed a read-only inventory and returned exactly: `Files inspected:` SYSTEM_REFERENCE.md, DOCS_INDEX.md, OVERNIGHT.md, docs/DATA_SOURCE_REGISTER.md, docs/CONFIGURATION_REFERENCE.md, A2AJ scripts, canlaw helpers, backend/ingestion.py, relevant tests, CHANGELOG.md, and docs/STILL_TO_DO.md; `Files changed:` none; `Commands run:` none; `Results:` A2AJ/Hugging Face staging covers 61,217 in the documented 2026-08-01 snapshot, paginated API and staging bridges exist, provenance and source-priority safeguards are present; `Failures:` none; `Uncertainty:` current A2AJ refresh date, API availability/shape, incremental schedule, court coverage, and scale limits; `Recommendation:` perform a bounded read-only freshness/API probe, then a dry-run delta and seek explicit approval before canonical writes.
Focused validation: `& .\venv\Scripts\python.exe -m pytest tests/test_ingest_a2aj_parquet.py tests/test_a2aj_citation_network.py -q` passed: 3 passed. `ingest_a2aj_api.py --help` passed. Canonical read-only query found `a2aj_parquet=60849`, newest `2026-07-24`; `canlaw.db` exists at approximately 6.7 GB with an August modification time. One public request to `https://api.a2aj.ca/search?query=2026&doc_type=cases&output_language=en` returned `400 Bad Request`, so no current API records were imported.
Residual risk: The current public API contract and present-day coverage remain unverified; A2AJ terms/licence, endpoint limits, refreshed staging contents, provincial/tribunal coverage, duplicate deltas, storage cost, and canonical merge behavior for a new batch require follow-up. No download, paid call, or database write was performed.
Next bounded task: Reconcile the current A2AJ API documentation/response contract or obtain a refreshed public dataset manifest, then run a one-page read-only freshness probe and a 50-100-record dry-run delta comparison without canonical writes.

## Hypothesis

If A2AJ exposes a current, provenance-preserving dataset or endpoint compatible with the existing staging/import path, then a bounded recent-case probe can measure corpus gaps without changing canonical records.

## Plan

1. Read authoritative source, operations, and ingestion documentation and consume the delegated inventory.
2. Select one acquisition/curation owner surface and define a non-mutating probe.
3. Run focused validation, update canonical and Swimm documentation, and leave any bulk acquisition/write as an explicit next approval.

## Execution Checkpoints

- Delegation: Explore agent, read-only A2AJ inventory; structured result consumed before implementation.
- Implementation: No acquisition or canonical write; recorded current date coverage and an explicit API-contract blocker.
- Documentation: `docs/DATA_SOURCE_REGISTER.md` and `.swm/canlaw-staging-and-models.sw.md` updated.
- Recovery: No long-running operation planned; no external paid or bulk operation allowed.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-30 | Task created | User asked whether A2AJ can extend the corpus toward present-day coverage. | Managed-task request and A2AJ source link |

## Completion

Completion recorded: yes

Summary: A2AJ expansion is technically supported by existing staging/import paths, but current present-day coverage is not yet confirmed. The canonical A2AJ parquet population ends at 2026-07-24, and the first public API probe returned HTTP 400.

Validation: Focused A2AJ ingestion/citation tests passed 3 tests; importer help passed; live counts and staging metadata were read without writes.

Residual risk: Current API shape and refreshed source availability remain unresolved; no bulk operation was attempted.

Next recommended task: Run the bounded API-contract/freshness probe and dry-run delta comparison described above.
