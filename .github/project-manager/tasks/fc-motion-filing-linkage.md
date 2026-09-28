# Task: Link motion filings to later activity entries

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Use motion filing descriptions to enrich later hearing and decision entries without treating row identity as motion identity.

Why now: The current grouped metric still treats the FC Activity row/document identity as a logical motion boundary, leaving decision entries without the filing description that names the motion.

Owner surface: `scripts/classify_fc_activity.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity `recorded_entry`, `docno`, `re_no`, and deterministic classifier tests.

Risk boundary: Preserve every source activity entry and its evidence; do not merge or rewrite FC Activity database rows; do not infer a motion link without a source motion reference or bounded fallback.

Smallest falsifiable check: `pytest tests/test_classify_fc_activity.py -k motion -q`

Acceptance criteria:

- A filing entry with a substantive motion description can supply subtype context to a later motion entry referencing the same motion document number.
- Row/document identity is not used as the logical motion identity.
- Existing source evidence and unrelated motion references remain separate.

Harness criteria: Focused classifier motion-linkage tests pass; existing evaluator tests pass; docs explain the identity distinction.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`

Rollback/recovery: Revert the classifier/test/docs commit; no database writes are part of this task.

Evidence: Explore inspection confirmed `recorded_entry` contains motion substance and that row identity is not a logical motion. The seeded read-only evaluation produced 952 motion events, 568 groups, 202 explicit motion-reference groups, 366 `re_no` fallbacks, 521/952 (54.83%) event subtype coverage, and 218/568 (38.38%) grouped subtype coverage; `database_written=false`.

Files changed: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, `tests/test_classify_fc_activity.py`, `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`, `.swm/fc-ingest-source-pipeline.sw.md`, this task record, and the read-only evaluation artifact.
Delegated work: Explore agent traced schema, classifier, evaluator, and representative reports; no files changed.
Focused validation: `pytest tests/test_classify_fc_activity.py -q` (50 passed); `pytest tests/test_evaluate_fc_activity_deterministic.py -q` (11 passed); `py_compile` passed; bounded evaluation completed with no database write.
Residual risk: Some filings may lack a recoverable motion reference and remain unresolved; grouped coverage is not an accuracy estimate.
Next bounded task: Review the 10 grouped subtype conflicts and unresolved motion-reference families.

## Hypothesis

If motion references are matched from filing text and source `docno` before falling back to `re_no`, a later motion decision will inherit the filing subtype while retaining separate source document evidence.

## Plan

1. Add a narrow motion-reference key to classifier propagation.
2. Add focused tests for filing-to-decision linkage and reference isolation.
3. Validate, then update the canonical FC Activity comparison and Swimm walkthrough.

## Execution Checkpoints

- Delegation: Explore agent inspected the bounded FC Activity surface and returned a structured report.
- Implementation: Classifier and evaluator now use explicit motion references before `re_no` fallback.
- Documentation: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` and `.swm/fc-ingest-source-pipeline.sw.md` updated.
- Recovery: No long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Treat row identity as ingestion identity, not logical motion identity | User clarified that the identity is only the FC Activity entry number; motion substance is in the filing description | Existing schema/evaluator inspection and representative report rows |

## Completion

Completion recorded: yes

Summary: Motion filing descriptions now enrich later referenced activity entries without treating FC Activity row identity as logical motion identity.

Validation: Focused classifier/evaluator tests, Python compilation, bounded seeded evaluation, and documentation updates completed.

Residual risk: Text-independent or ambiguous entries remain conservative.

Next recommended task: Review the 10 grouped subtype conflicts and unresolved motion-reference families.
