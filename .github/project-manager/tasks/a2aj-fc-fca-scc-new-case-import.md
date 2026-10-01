# Task: Import new A2AJ FC/FCA/SCC cases

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

Task: Import only the refreshed A2AJ FC, FCA, and SCC records dated after 2026-07-24.

Why now: The bounded refresh identified 200 post-baseline cases that are not present by citation or full-text hash in the canonical database.

Owner surface: `scripts/ingest_a2aj_parquet.py` and the local `/ingest` API path.

Commit allowed: yes
Push allowed: yes

Dependencies: Refreshed Parquet files under `data/raw/a2aj/refresh-20260930/`, local FastAPI service, PostgreSQL configuration, and existing A2AJ source/provenance fields.

Risk boundary: Only FC, FCA, and SCC; decision date strictly after 2026-07-24; no enrichment of existing cases, no RPD, no replacement, no deletion, no embeddings, and no unrelated source writes.

Smallest falsifiable check: A date-filtered dry-run must select exactly 200 records with zero invalid records before the API write begins.

Acceptance criteria:

- The importer supports an explicit date cutoff.
- The focused dry-run selects FC 168, FCA 28, and SCC 4.
- The write imports exactly those 200 records through the existing API contract.
- Imported records retain A2AJ source metadata, URLs, hashes, licence, and citation relationships.
- Post-import counts and task documentation are recorded.

Docs/generated references: `.github/project-manager/tasks/a2aj-fc-fca-scc-refresh-acquisition.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`.

Rollback/recovery: Stop before import if dry-run differs. If the write fails, record the exact partial count and use source IDs/citations for bounded recovery; do not delete unrelated records.

Evidence: Date-filtered dry-run selected FC 168, FCA 28, and SCC 4 with zero invalid records. The local API write completed with `selected=168 imported=168 skipped=0 invalid=0`, `selected=28 imported=28 skipped=0 invalid=0`, and `selected=4 imported=4 skipped=0 invalid=0`. Post-import verification found 61,049 canonical `a2aj_parquet` cases, 200 more than the 60,849 baseline.

Files changed: `.github/project-manager/tasks/a2aj-fc-fca-scc-new-case-import.md`, `scripts/ingest_a2aj_parquet.py`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`.
Delegated work: None; bounded implementation and validation are manager-owned.
Focused validation: Date-filtered dry-run passed; write summaries passed; post-import database query confirmed FC 35,657 total / 168 post-baseline, FCA 7,795 / 28, and SCC 10,868 / 4, with latest dates 2026-09-25, 2026-09-24, and 2026-09-18. The temporary API was stopped after the write.
Residual risk: This task intentionally did not enrich existing cases with refreshed citation-network metadata or HTML snapshots. Those remain a separate later task.
Next bounded task: Design and dry-run a provenance-preserving enrichment pass for existing A2AJ-matched cases.

Status details: Import only new post-baseline records; existing case enrichment is explicitly deferred.
