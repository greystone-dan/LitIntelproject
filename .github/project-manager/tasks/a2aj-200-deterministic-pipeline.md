# Task: Run deterministic pipeline on 200 A2AJ cases

Status: in-progress
Created: 2026-09-30
Updated: 2026-09-30

Task: Process exactly the 200 A2AJ cases imported after 2026-07-24 through chunks, metadata, outcomes, case citations, statutes, and V3 tags.

Why now: The 200 new FC/FCA/SCC records are present in canonical storage and need deterministic derived layers before embedding work.

Owner surface: `scripts/run_v2_pipeline.py` cohort selection and deterministic case-processing stages.

Commit allowed: yes
Push allowed: yes

Dependencies: Canonical A2AJ records, current chunk-heading fix, citation/statute extraction, outcome classifier, and V3 tagger.

Risk boundary: Exactly 200 cases with `source_type=a2aj_parquet` and `date > 2026-07-24`; exclude source HTML acquisition and embeddings; include SCC explicitly; no other cases, no source replacement, no bulk corpus rebuild.

Smallest falsifiable check: A dry-run over the selected cohort must report exactly 200 cases and plan only chunks, metadata, outcomes, citations, statutes, and tags_v3.

Acceptance criteria:

- Source HTML stage is skipped entirely.
- Chunks, metadata, outcomes, citations, statutes, and tags_v3 complete for all 200 cases or are quarantined with explicit errors.
- No embeddings are produced.
- Durable run state and post-run counts are recorded.
- Canonical source documentation and the processing Swimm walkthrough are updated.

Docs/generated references: `docs/TESTING_MATRIX.md`, `.swm/4.9nn3id9f.sw.md`, `OVERNIGHT.md`.

Rollback/recovery: Resume the same run directory for quarantined stages; do not rerun completed stages blindly. Derived layers are case-scoped and replace only their own versioned rows.

Evidence: Pending dry-run and deterministic pipeline execution.

Files changed: This task record so far.
Delegated work: None; bounded pipeline execution is manager-owned.
Focused validation: Pipeline dry-run with the exact 200 case IDs and stage exclusion.
Residual risk: Existing embeddings remain absent; source HTML and any HTML-dependent structural mapping remain deferred.
Next bounded task: Measure chunk/citation/statute/tag outputs and review quarantined cases before any embedding cohort.
