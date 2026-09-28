# Task: Review FC Activity pipeline before scale-up

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Review the FC Activity extraction and evaluation process for ambiguity, unsafe assumptions, weak evidence linkage, denominator errors, and scale-up blockers before testing a wider case sample.

Why now: The fixed IMM-15 sample has stable deterministic fields and a read-only evaluator; a wider run should not proceed until the pipeline contract and reporting boundaries are clear.

Owner surface: FC Activity deterministic extraction/evaluation pipeline under `scripts/`.

Commit allowed: yes

Push allowed: yes

Dependencies: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, latest fixed evaluation artifact, focused tests, FC Activity comparison documentation, and Swimm walkthrough.

Risk boundary: Review and bounded validation only; no database writes, no external AI calls, no unbounded corpus run, and no changes to unrelated extraction systems.

Smallest falsifiable check: Run a read-only pipeline contract audit that verifies sample selection, evidence retention, field denominators, output serialization, and `database_written=false` on the fixed evaluation.

Acceptance criteria:

- Pipeline stages and ownership are clear enough for a wider bounded run.
- Any ambiguous field semantics, denominator/reporting defects, or safety gaps are identified with evidence.
- High-risk defects are fixed or explicitly marked as blockers before scale-up.
- Focused tests and a bounded evaluation pass after any fixes.
- Canonical documentation and the FC Activity Swimm walkthrough record the readiness decision.

Harness criteria: The readiness check uses a bounded sample and confirms no database writes or network calls.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `OVERNIGHT.md`.

Rollback/recovery: Revert only review-driven pipeline/documentation edits; preserve existing evaluation artifacts and do not delete user data.

Evidence: Read-only review identified missing evaluator ordering, an unreported cross-field validator, an unparenthesized French final-decision marker gap, and false JR outcomes from rejected underlying decisions. Fixed these issues. Focused tests passed (70). Fixed evaluation validated 1,000/1,000 cases with zero issues, `network_called=false`, and `database_written=false`. A repeat run selected identical case IDs and produced identical metrics. Canonical documentation: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`. Swimm walkthrough: `.swm/fc-ingest-source-pipeline.sw.md`.

Files changed: `scripts/classify_fc_activity.py`; `scripts/evaluate_fc_activity_deterministic.py`; `tests/test_classify_fc_activity.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `data/eval/fc_activity_imm_suffix_15_readiness_20260928.json`.
Delegated work: Explore, bounded read-only pipeline review; no files changed.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py -q` (70 passed); fixed evaluator and repeat rerun (1,000 cases each, zero validation issues, no network/database writes, identical case IDs).
Residual risk: Wider-sample runtime, artifact size, and unseen text patterns remain untested; detailed motion subtype/result quality remains limited by design.
Next bounded task: Run a wider read-only sample with a new output artifact and explicit runtime/output-size monitoring.

## Hypothesis

If the FC Activity classifier, evaluator, evidence contract, and operational controls are coherent, a bounded audit plus fixed-sample rerun will expose no unresolved blocker to a larger read-only sample.

## Plan

1. Inventory the pipeline and identify scale-up blockers.
2. Fix only high-risk contract or validation defects.
3. Rerun focused tests and the fixed evaluation, then record the wider-run boundary.

## Execution Checkpoints

- Delegation: Pending Explore review and structured result.
- Implementation: Pending review findings.
- Documentation: Pending canonical document and Swimm walkthrough updates.
- Recovery: No database or bulk-write operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested a pipeline/process cleanup review before a wider test sample. | Current fixed-sample artifacts and FC Activity documentation |

## Completion

Completion recorded: yes

Summary: FC Activity pipeline is clean for a wider bounded read-only sample after ordering, validation, and JR semantic fixes.

Validation: 70 focused tests passed; fixed and repeat evaluations selected identical samples, validated all cases, and made no network or database writes.

Residual risk: Wider-sample operational behavior and unseen parser patterns remain to be measured.

Next recommended task: Run the wider bounded read-only FC Activity sample.