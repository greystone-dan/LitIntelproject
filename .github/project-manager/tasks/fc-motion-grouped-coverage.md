# Task: Add grouped motion coverage metrics

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Add a more useful unique-motion coverage metric that groups document-level motion events by stable case and motion identifiers while preserving existing document-level metrics.

Why now: The current 952-event denominator counts multiple documents from the same motion separately and understates useful subtype coverage. The user reports the prior Excel tool produced a more meaningful measure.

Owner surface: `scripts/evaluate_fc_activity_deterministic.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Seeded FC Activity evaluation, classifier fields `activity_case_id`, `re_no`, `docno`, subtype, outcome, source evidence, and existing evaluation tests/docs.

Risk boundary: Read-only evaluation only. Do not alter classifier events, raw Activity data, database rows, gold sets, or OpenAI artifacts. Preserve existing metrics for backward comparison.

Smallest falsifiable check: The seeded evaluation must emit document-level metrics unchanged and grouped unique-motion metrics with explicit group counts, ambiguity counts, and subtype/result coverage.

Acceptance criteria:

- Existing document-level motion metrics remain unchanged and clearly labeled.
- Grouped unique-motion metrics use case plus stable motion identifier, with a documented fallback and ambiguity count.
- Grouped subtype and outcome rates are computed from one representative aggregate per group, not document count.
- The seeded evaluation demonstrates the difference between document-level and grouped denominators without network or database writes.
- Focused tests, documentation checks, and evidence gate pass.

Harness criteria:

- Group construction and aggregation tests pass for shared, missing, and conflicting identifiers.
- Seeded evaluation emits grouped metrics and preserves existing raw metrics.
- Canonical documentation and Swimm walkthrough explain the two denominators and limitations.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; evaluation tests and generated references if affected.

Rollback/recovery: Revert the task commit. Evaluation artifacts are read-only outputs; no database recovery is required.

Evidence: Explore completed the bounded inventory. Final focused tests passed, and the seeded 1,000-case read-only evaluation emitted both unchanged document-level metrics and grouped metrics: 952 document events, 917 grouped candidates, 44 explicit Motion Doc reference groups, 873 re_no groups, grouped subtype coverage 28.68%, and grouped outcome coverage 13.85%. The evaluation recorded no network or database writes. Generated-document validation passed.

Files changed: `scripts/evaluate_fc_activity_deterministic.py`; `tests/test_evaluate_fc_activity_deterministic.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `data/eval/fc_activity_motion_grouped_20260928.json`.
Delegated work: Explore completed a bounded read-only inventory. It confirmed `(activity_case_id, re_no)` as the safest fallback key, recommended singleton fallback for missing `re_no`, and advised explicit conflict/unknown states without majority voting. The manager then verified explicit Motion Doc references as the stronger source-text bridge. No files were changed by the worker.
Focused validation: `pytest tests/test_evaluate_fc_activity_deterministic.py tests/test_motion_taxonomy.py tests/test_audit_fc_activity_motion_unknowns_openai.py -q` passed. Seeded evaluation exited 0 with `network_called=false` and `database_written=false`. `scripts/check_generated_docs.py` exited 0.
Residual risk: Grouping quality depends on source identifier consistency; unresolved or conflicting identifiers must remain visible.
Next bounded task: Compare grouped metrics against the prior Excel workbook review queue.

## Hypothesis

If document events are grouped by case and stable motion identifiers before coverage is calculated, the grouped denominator will better represent unique motions and produce a materially higher, more useful subtype coverage rate without changing extraction.

## Plan

1. Delegate a bounded inventory of evaluator and identifier semantics.
2. Implement pure grouping and aggregation helpers with tests.
3. Run the seeded evaluation, update docs, and pass the evidence gate.

## Execution Checkpoints

- Delegation: Explore inventory completed; structured report returned in the managed session output.
- Implementation: Grouped coverage helper and tests complete; document-level metrics remain backward-compatible.
- Documentation: Canonical FC Activity comparison and Swimm source-pipeline walkthrough updated with grouping method, denominator counts, and limitations.
- Recovery: No external operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested a more useful grouped motion coverage number because document-level metrics appear to understate the Excel-style result. | Current seeded evaluation and classifier identifier fields |

## Completion

Completion recorded: yes

Summary: Added explicit Motion Doc/Requête Doc grouping with re_no fallback, singleton handling, and conflict-visible subtype/outcome aggregation. The useful grouped denominator is 917 motion candidates from 952 document events.

Validation: Focused tests, seeded evaluation, and generated-document validation passed.

Residual risk: Source records without explicit motion-document references remain conservative singleton groups; grouped coverage is not accuracy and does not reconstruct every legal motion.

Next recommended task: Compare grouped metrics to Excel-style motion counts.
