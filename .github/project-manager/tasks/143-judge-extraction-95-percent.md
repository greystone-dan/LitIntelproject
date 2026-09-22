# Task: Reach 95 percent post-2005 judge identification

Status: in-progress
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Make judge extraction reliably identify the judge for at least 95% of cases dated 2006 onward, with one canonical profile per exact normalized judge name; defer spelling-variation merging until a later task.

Why now: Judge identity is a core research dimension, but current stored metadata contains false positives and many valid judge values have no profile link. The product needs a measurable extraction-coverage gate before rerunning judge extraction and writing to the database.

Owner surface: Judge metadata extraction and profileability evaluation.

Commit allowed: yes

Push allowed: yes

Dependencies: `fc_ingest/document_scraper.py`, `backend/metadata.py`, `scripts/backfill_judge_profiles.py`, `scripts/judge_reconciliation_report.py`, source-preserved case records, judge tests, and the active database.

Risk boundary: No production database writes, destructive cleanup, spelling-variation merges, external acquisition, or live-pipeline rollout until the 95% gate and source-review evidence pass. Cases dated before 2006 are out of scope for the success metric.

Smallest falsifiable check: A read-only post-2005 evaluation reports the denominator, profileable extracted judges, invalid values, missing values, and a manually reviewable sample of cases where extraction is absent or suspect.

Acceptance criteria:

- Define the post-2005 denominator as cases with a valid decision date in 2006 or later.
- Measure judge-identification coverage using source-preserved evidence, not merely non-empty metadata.
- Reach at least 95% reliable judge identification on the post-2005 denominator, with the metric and sample review recorded.
- Preserve exact normalized-name uniqueness; do not merge possible spelling variations in this task.
- Add regression fixtures for reviewed extraction patterns and future-pipeline behavior.
- Prepare a bounded rerun/write plan, but do not execute database writes without a separate approval checkpoint.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, this task record, and any focused evaluation artifact. Do not hand-edit generated references.

Rollback/recovery: Revert extraction/test/report changes before any write. Future writes must use a checkpoint, dry-run output, row-level audit, and reversible backup or transaction plan.

Evidence: Parser now includes inline `CORAM` and `REASONS FOR ORDER` /
`ASSESSMENT` fallbacks. Focused judge tests passed (`31 passed`) and
`py_compile` passed. The read-only stored post-2005 baseline is 41,123 cases,
with 34,471 nonempty judge values, 31,582 profileable values, 2,889 invalid
values, 31,334 profileable values at confidence 0.92-0.98, and 7,199 valid
values without profile links. A bounded fresh sample reached 93/100
profileable and zero invalid. The full fresh evaluation timed out at 120
seconds and remains pending. No database writes, backfill, or live-pipeline
rollout occurred.

## Hypothesis

If judge extraction uses multiple source-grounded fallbacks with shared junk rejection and is measured against source-preserved decision evidence, then post-2005 cases can reach at least 95% reliable judge identification without spelling-variation merging.

## Plan

1. Establish the post-2005 denominator, current coverage, and source evidence available for evaluation.
2. Delegate a bounded review of extraction ownership and candidate source fields.
3. Improve the smallest controlling extraction path and add reviewed fixtures.
4. Run the focused evaluation and document whether the 95% gate passes.
5. If the gate passes, prepare but do not execute a separate rerun/write task for approval.

## Execution Checkpoints

- Delegation: Completed as a bounded documentation handoff.
- Baseline: Stored post-2005 baseline recorded; full fresh evaluation pending
	after a 120-second timeout.
- Implementation: Parser fallbacks added for inline `CORAM` and `REASONS FOR
	ORDER` / `ASSESSMENT`; focused tests passed.
- Documentation: Update SYSTEM_REFERENCE.md and the relevant Swimm walkthrough
	with current evidence and the no-write boundary.
- Recovery: No database writes permitted in this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | User set a measurable post-2005 judge-identification goal and deferred spelling-variation merging | Current tasks 139-142 and live reconciliation report |
| 2026-09-22 | Current evaluation state recorded | Parser fallbacks and focused validation are complete, but the bounded fresh sample is 93% and the full fresh evaluation timed out; no 95% claim or write authorization follows | Read-only stored baseline, bounded fresh sample, focused tests, and `py_compile` |

## Completion

Completion recorded: no

Summary: Parser improvements and focused validation are complete. The 95% gate
remains unproven because the bounded fresh sample reached 93/100 and the full
fresh evaluation timed out.

Validation: Focused judge tests: 31 passed. `py_compile`: passed. Full fresh
evaluation: timed out at 120 seconds.

Residual risk: Reliability cannot be claimed from the stored baseline or the
93/100 bounded sample alone; the full fresh evaluation and source-grounded
review remain outstanding.

TODO / next task: Run a batched read-only fresh post-2005 evaluation with
checkpointed progress and bounded batches, then review its denominator,
profileable rate, invalid values, and source-grounded sample. Only after that
result is accepted should a separate approval be requested for a dry-run or
database write/backfill.
