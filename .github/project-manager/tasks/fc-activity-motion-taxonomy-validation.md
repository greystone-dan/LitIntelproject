# Task: FC Activity motion taxonomy and validation slice

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Add a bounded Beta-informed motion taxonomy and pure cross-field validation slice to FC Activity classification.

Why now: The verified Beta workbook identifies motion categories and integrity checks that are useful for FC Activity review, while the current classifier only preserves generic motion events and outcomes.

Owner surface: `scripts/classify_fc_activity.py` and focused classifier tests

Commit allowed: yes

Push allowed: yes

Dependencies: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; raw Activity documents; existing `ActivityEvent` and `classify_events` contracts.

Risk boundary: Do not modify raw Activity rows, canonical cases, database schemas, remote collection behavior, or paid/LLM review. Unknown motion types and contradictory fields must remain visible.

Smallest falsifiable check: Focused tests prove Beta-derived motion subtypes/results and structured validation findings while preserving source document evidence.

Acceptance criteria:

- Motion events expose a stable subtype for the highest-value Beta categories and preserve unknowns with source evidence.
- Motion results distinguish granted, granted in part, refused, abandoned, and discontinued where explicit wording exists.
- A pure validation function reports Beta-derived cross-field contradictions without writing data.

Harness criteria:

- Focused motion and validation tests pass.
- Existing FC Activity classifier regression tests pass.
- Canonical report and Swimm walkthrough are updated with measured evidence.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `DOCS_INDEX.md`.

Rollback/recovery: Revert only the classifier, focused tests, task record, and documentation checkpoint; raw Activity and canonical case data remain untouched.

Evidence: Managed run `fc-activity-motion-taxonomy-validation-20260928-065731-621f81dc` recorded focused motion tests (4 passed) and the existing classifier regression suite (49 passed). Motion subtypes/results and the pure validator were added without raw Activity or canonical writes. The canonical comparison report and Swimm walkthrough now record the measured checkpoint.

Files changed: `scripts/classify_fc_activity.py`; `tests/test_motion_taxonomy.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; this task record.
Delegated work: Explore performed a bounded read-only inventory of current motion extraction, tests, Beta-derived categories, and safe insertion points. No files changed. The structured result identified the fixture matrix and validator contract.
Focused validation: `python -m pytest tests/test_motion_taxonomy.py -q` passed 4 tests; `python -m pytest tests/test_classify_fc_activity.py -q` passed 49 tests.
Residual risk: Beta phrases are a starting point; subtype precedence and French wording require broader source-text coverage. The validator is not yet applied to a fixed production-sized evaluation.
Next bounded task: Measure motion subtype coverage on a fixed 100-record evaluation after the fixture slice.

## Hypothesis

If Beta's explicit motion categories and result phrases are added as evidence-backed rules, then focused fixtures will produce more useful motion labels without changing event counts or losing unknowns.

## Plan

1. Delegate a bounded inventory of current motion rules, fixtures, and safe insertion points.
2. Add the smallest subtype/result and pure validation implementation with focused tests.
3. Run focused tests, record harness criteria, update documentation, and run the evidence gate.

## Execution Checkpoints

- Delegation: Explore completed the bounded read-only inventory.
- Implementation: Motion subtype/result normalization and pure validation added; focused tests passed.
- Documentation: Canonical Beta comparison and FC ingestion Swimm walkthrough updated.
- Recovery: No long-running operation; managed run state and events provide recovery evidence.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | Continue the Beta workbook comparison with a bounded implementation slice. | `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` |

## Completion

Completion recorded: yes

Summary: Added the first Beta-informed motion taxonomy/result layer and a pure cross-field validator with focused fixtures.

Validation: Managed run criteria 0, 1, and 2 passed; `scripts/evidence_gate.py` passed with 4 recorded commands.

Residual risk: Broader motion coverage and fixed-cohort measurement remain.

Next recommended task: Measure motion subtype/result coverage on a fixed 100-record evaluation.
