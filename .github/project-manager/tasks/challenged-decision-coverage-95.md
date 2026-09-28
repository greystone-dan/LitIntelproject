# Task: Raise challenged-decision coverage toward 95 percent

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Improve deterministic analysis of the decision challenged by an originating ALJR, anchored to the first ALJR row while allowing later activity to enrich the result, and measure the same IMM-15 1,000-case slice.

Why now: The fixed slice has nearly universal originating ALJR rows and filing dates, but first-row decision type coverage is only 42.3%. The user wants substantially higher decision-information coverage, targeting the 95% range without losing source traceability or later evidence.

Owner surface: `scripts/classify_fc_activity.py` challenged-decision extraction and its focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity event extraction, IMM-15 evaluation artifact, evaluator report, canonical FC Activity comparison, and Swimm source-pipeline walkthrough.

Risk boundary: Preserve raw activity text, document identity, first-row anchor fields, and existing later-history enrichment. No database writes, external APIs, LLM classification, production changes, or broad corpus runs.

Smallest falsifiable check: `pytest tests/test_classify_fc_activity.py -q` plus a bounded IMM-15 evaluator rerun; the decision-information metric must be explicitly defined and reported.

Acceptance criteria:

- First originating ALJR evidence remains the anchor for filing date and challenged-decision facts; later rows may enrich separately.
- Decision maker/type and decision type/date extraction reaches the agreed 95% target for the defined combined decision-information metric on the fixed 1,000-case IMM-15 slice, or records the exact limiting evidence and a justified blocked status.
- Source document IDs and text remain attached to promoted decision fields.
- Focused classifier/evaluator tests, compilation, generated-doc check, and whitespace validation pass.
- Canonical FC Activity documentation and the Swimm walkthrough record the metric, evidence, and residual risk.

Harness criteria:

- Focused classifier tests pass.
- Focused evaluator tests pass.
- IMM-15 bounded decision-information metric reaches target or is explicitly documented as blocked with evidence.
- Canonical and Swimm documentation are updated and validation checks pass.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated documentation check.

Rollback/recovery: Revert the classifier/test/documentation commit. Evaluation artifacts are read-only and can be regenerated with the fixed IMM-15 suffix command. Do not resume any unbounded run.

Evidence: Delegated gap analysis was completed after a focused retry. The bounded evaluator selected 1,000 cases through indexed `FCActivityClassification.imm_number` suffix `15`, classified only the selected cases, made no database writes, and wrote `data/eval/fc_activity_imm_suffix_15_decision_analysis_20260928.json`. Results: 999 originating rows, 999 filing dates, 937 originating maker types, 423 decision types, 507 decision dates, and 963 cases with combined originating decision information (96.3%). Focused classifier/evaluator tests passed 75 tests. Canonical documentation: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`. Swimm walkthrough: `.swm/fc-ingest-source-pipeline.sw.md`.

Files changed: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, `tests/test_classify_fc_activity.py`, `tests/test_evaluate_fc_activity_deterministic.py`, this task record, `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.
Delegated work: Completed bounded exploration of decision-information gaps and safe fallback rules; the first invalid motion-field analysis was retried with the correct `classification.challenged_decision` scope.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py -q` -> 75 passed; bounded IMM-15 evaluator -> 963/1,000 (96.3%).
Residual risk: Sparse or malformed originating rows may lack explicit decision type/date; fallback inference must remain evidence-backed and distinguish anchor facts from later enrichment.
Next bounded task: Review the 37 remaining combined-metric gaps by source pattern, with no broad evaluation or subject fabrication.

## Hypothesis

If originating ALJR text is parsed with explicit decision-maker and decision-type fallback families while preserving first-row anchoring and later evidence separately, the defined decision-information coverage will move into the 95% range without inventing unsupported legal facts.

## Plan

1. Create a managed harness run with explicit acceptance criteria.
2. Delegate a bounded inventory of remaining IMM-15 decision-information gaps.
3. Implement the smallest high-precision fallback slice with tests.
4. Rerun the fixed IMM-15 sample, record coverage, and update canonical/Swimm documentation.
5. Run the evidence gate before completion.

## Execution Checkpoints

- Delegation: Complete.
- Implementation: Complete.
- Documentation: Complete.
- Recovery: No long-running operation; all evaluation runs must remain database-side filtered and sample-first.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested substantial improvement toward 95% coverage on the fixed IMM-15 slice | Existing report: 999 originating rows, 999 filing dates, 901 originating maker types, 423 originating decision types |

## Completion

Completion recorded: yes

Summary: The first originating ALJR row remains the anchor, later activity remains enrichment, and the combined originating decision-information metric reached 96.3% on the fixed 1,000-case IMM-15 slice.

Validation: 75 focused classifier/evaluator tests passed; bounded evaluator completed with `database_written=false`; final compilation, generated-doc, whitespace, harness, and evidence-gate checks remain.

Residual risk: Decision type remains explicit in only 42.3% of originating rows, decision dates in 50.7%, and 37 cases lack any combined decision-information signal. This metric measures extraction coverage, not gold-set accuracy.

Next recommended task: Delegate and inspect decision-information gaps before editing extraction rules.
