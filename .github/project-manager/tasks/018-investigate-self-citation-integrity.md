# Task: Investigate Self-Citation Integrity

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Characterize the corpus quality gate's self-citation failure using a bounded read-only sample.
Why now: The live quality gate found 241,272 citation rows whose source and target case IDs match, blocking the integrity gate.
Owner surface: Citation extraction and target resolution
Dependencies: `scripts/evaluate_data_quality.py`, `backend/citations.py`, citation database rows
Risk boundary: Read-only sample only; do not delete, rewrite, resolve, or bulk-update citation rows until the failure mode and policy are established.
Smallest falsifiable check: Inspect a bounded sample of self-citation rows with source/target metadata and citation text to classify likely true references versus false self-matches.
Acceptance criteria: Produce a measured classification of sampled self-citations, identify the controlling code/data failure mode, and define the smallest safe follow-up check.
Docs/generated references: Swimm Technical Debt Register and Improvement Queue; Swimm Evaluation Framework and Quality Metrics.
Rollback/recovery: No data changes; discard the read-only sample output if the query is inconclusive.
Evidence: A read-only sample of 20 self-citation rows showed repeated extraction of each source decision's own neutral citation from header fields such as `Neutral citation` and `Citation:`. Added exact source-case citation filtering to rebuild paths and regression coverage; 80 citation tests pass. Existing rows remain unchanged. Next task is an audited, reversible bounded cleanup/rebuild plan before any data mutation.
