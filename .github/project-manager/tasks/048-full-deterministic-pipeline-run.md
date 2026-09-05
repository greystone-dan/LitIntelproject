# Task: Full deterministic pipeline run

Status: deferred
Created: 2026-09-04
Updated: 2026-09-04

Task: Run the V2 Pipeline across the 60K+ canonical case cohort using tracked, resumable jobs.
Why now: Today’s completed redesign covers source-HTML recovery, HTML-aware chunks, metadata, citations/statutes/metrics, active tags, and dedicated outcomes; the existing overnight profile does not represent this pipeline.
Owner surface: V2 Pipeline orchestration: source HTML reacquisition, rechunking, metadata, citations/statutes, outcomes, and active tags.
Dependencies: PostgreSQL availability, migration head `0022_case_outcomes`, sufficient disk, no competing bulk writer, canonical source links, and existing case text.
Risk boundary: Do not run legacy V1 or comparison-only V2 tagging as the active pipeline. No source/citation/tag deletion outside each job’s documented versioned/rebuild scope. Use one lock-protected orchestrator run with logs and resumable state.
Smallest falsifiable check: Orchestrator preflight passes for `chunk_cases`, `citations`, `case_outcomes`, `tag_cases_v3`, and `local_embeddings`; each job exposes bounded/resumable controls and writes its own run log.
Acceptance criteria: A tracked profile runs validated source-HTML reacquisition first, then HTML-aware rechunking, metadata refresh, citation/statute/metrics rebuild, dedicated outcomes, and active tags; no embeddings; state/logs are created; failures are resumable; documentation and Swimm runbook identify the V2 Pipeline stages.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `LEGAL_TAGGING.md`, `docs/EXTRACTION_35K_RUNBOOK.md`, relevant `.swm/` operational/system walkthrough.
Rollback/recovery: Stop and resume by run ID; inspect per-job logs/state; rerun only incomplete jobs. Preserve V1/V2 rows and versioned V3/outcome rows.
Evidence:
- Initial launch attempt was stopped before completing the first generic chunk
	job after clarifying that the requested run requires HTML-aware rechunking and
	full metadata/citation/statute/tag/outcome refresh.
- No embeddings run was started or completed.
- The active overnight orchestrator was not changed to claim this pipeline;
	a future run needs a dedicated, reviewed orchestration design first.
- Corrected scope: source-link HTML reacquisition and validation is an explicit
	first stage, before HTML-aware rechunking. Original source identity, URL,
	retrieval time, hash, and parser/provenance metadata must be preserved.
- One-case V2 Pipeline smoke test completed for case `22` (`2005 FC 1037`):
	HTML reacquisition applied, 12 replacement chunks created (`full_case=1`,
	`section=3`, `paragraph=8`), citations rebuilt (`1`), statutes rebuilt (`1`),
	dedicated outcome replaced (`won`, `set_aside`, applicant winner, exact
	evidence span), and 35 V3 tag occurrences/status rows replaced. No
	embeddings or cohort run was started.
- Medium-long case test completed for case `9237` (`2006 FC 443`, 179,883
	characters): HTML applied; replacement chunks were `full_case=1`,
	`section=5`, `paragraph=135`; citations rebuilt to `66` from `424` prior
	rows; statutes rebuilt to `44` from `99` prior rows; outcome was explicitly
	`undetermined` with no disposition evidence; and 5 V3 tag occurrences were
	persisted. This confirms overwrite behavior but blocks cohort rollout until
	the citation/statute count delta is adjudicated.
- A 731,236-character case (`13681`) was intentionally not completed because
	the current HTML-to-canonical-text `SequenceMatcher` alignment became
	computationally prohibitive and was interrupted before chunk rows committed.
Status: deferred
Commit allowed: yes
Push allowed: yes
