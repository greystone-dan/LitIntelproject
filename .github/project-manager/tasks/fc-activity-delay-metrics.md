# Task: FC Activity delay metrics

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Add deterministic report-level filing-to-removal and motion-to-removal delay metrics with explicit missing and ambiguous states.

Why now: The Activity classifier now preserves explicit scheduled-removal dates, but management statistics need bounded intervals without treating source document dates as procedural dates.

Owner surface: `scripts/evaluate_fc_activity_deterministic.py` and focused evaluator tests

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `procedural_events`, explicit filing dates, `removal_scheduled_date`, and read-only deterministic report generation.

Risk boundary: Additive report output only. No raw Activity, canonical case, citation, statute, schema, collector, API/UI, network, or paid-operation changes.

Smallest falsifiable check: Synthetic procedural events with explicit application/motion filing and scheduled-removal dates produce correct day intervals; missing removal dates and non-chronological pairs remain classified rather than coerced.

Acceptance criteria:

- Report filing-to-removal and motion-to-removal metrics.
- Preserve complete, missing, and ambiguous status categories.
- Include count and quartile summaries for valid intervals.
- Keep source-document and semantic date distinctions visible.
- Update canonical documentation and the relevant Swimm walkthrough.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `data/eval/fc_activity_deterministic_evaluation_20260925.json`.

Rollback/recovery: Revert only evaluator/tests/documentation changes from this task; delete the regenerated evaluation artifact if required. Do not touch collector checkpoints or source tables.

Evidence: Delegated read-only review confirmed the smallest safe implementation is additive evaluator logic over existing derived event fields. New evaluator tests passed 4/4; the full Activity-focused suite passed 25 tests. The deterministic report regenerated read-only for 100 records with seven-year weighting and `database_written: false`: filing-to-removal had 3 complete, 1 ambiguous, and 96 missing-removal-date cases; motion-to-removal had the same status counts. Valid intervals had min/p25/p50/p75/max of 2/2/3/3/8 days for filing-to-removal and 2/2/3/3/5 days for motion-to-removal. Both metrics expose 100 cases, 3 valid cases, and 3% coverage. Documentation was updated in `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.

## Hypothesis

If delay intervals are computed only from explicit semantic anchors and scheduled-removal dates, then management statistics can show useful timing distributions while preserving uncertainty instead of inventing dates.

## Completion

Completion recorded: 2026-09-25

Summary: Complete for additive deterministic delay metrics over the bounded evaluation sample.

Validation: `python -m pytest tests/test_evaluate_fc_activity_deterministic.py -q` passed with 4 tests; the full Activity-focused suite passed with 25 tests; the deterministic report command completed without database writes.

Residual risk: The sample has only three valid intervals per metric and one ambiguous date-order case; these are evaluation signals, not population estimates. Multiple stay motions and administrative rescheduling may require case-level temporal association before broader reporting.

Next recommended task: Validate temporal association across multiple stay motions and rescheduled removals before any API/UI exposure; the current 3% coverage is not a population estimate.
