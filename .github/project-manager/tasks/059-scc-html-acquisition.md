# SCC HTML acquisition

Status: blocked
Created: 2026-09-06

Task: Acquire and validate source HTML for SCC cases as a separate bounded source-refresh workstream.
Why now: The completed V2 text-only run deliberately excluded SCC HTML; 10,889 SCC cases have full text and source URLs, but only 27 have stored HTML.
Owner surface: `scripts/acquire_case_html.py` and SCC source provenance.
Dependencies: Existing SCC source URLs, `decision_content_url`, response citation validation, host limiter, and quarantine output.
Risk boundary: SCC-only, bounded, dry-run first; no V2 enrichment writer, no concurrent PostgreSQL enrichment, no source deletion, and no aggressive request rate.
Smallest falsifiable check: A five-case dry run reports validated/quarantined dispositions without changing canonical database rows.
Acceptance criteria: Establish SCC fetch success/failure rate and reasons, then decide whether a bounded write batch is safe; preserve source identity, hashes, retrieval metadata, and quarantine evidence.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Dry-run has no database writes; acquisition writes can be resumed or reviewed by quarantine record without deleting prior HTML.
Evidence: Initial inventory: SCC total 10,889; full text 10,889; source URLs 10,889; stored source HTML 27. Initial five-case dry run returned 5 ready, 0 quarantined, and 0 applied. The first 25-case write batch refreshed existing records: 25 ready, 25 applied, 0 quarantined, with coverage remaining 27. After adding `--missing-html-only`, a five-case missing-HTML probe returned 1 ready and 4 quarantined. Raw inspection showed valid decision HTML for one URL and `login.openathens.net` redirects without decision content for four older SCC URLs. Bulk acquisition is blocked pending an approved alternate source or URL mapping; no further bulk writes should run.
Commit allowed: yes
Push allowed: yes
