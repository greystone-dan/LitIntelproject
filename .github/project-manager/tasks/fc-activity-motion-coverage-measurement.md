# Task: Measure FC Activity motion coverage on fixed 100-record sample

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Add a reproducible motion subtype/result coverage summary to the seeded 100-record FC Activity evaluator and record the measured result.

Why now: The Beta-informed taxonomy is implemented and tested; the next bounded signal is coverage on a fixed cohort before expanding rules or fixtures.

Owner surface: `scripts/evaluate_fc_activity_deterministic.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity database/evaluator, motion classifier, canonical Beta report, and FC ingestion Swimm walkthrough.

Risk boundary: Read-only evaluation only. Do not write database rows, alter raw Activity data, run network collection, or promote uncertain categories. Preserve the fixed seed/sample contract.

Smallest falsifiable check: `venv\\Scripts\\python.exe scripts\\evaluate_fc_activity_deterministic.py --sample-size 100 --seed 20260925 --recent-years 7 --recent-share 0.7 --output data\\eval\\fc_activity_motion_coverage_20260928.json`

Acceptance criteria:

- The evaluator emits deterministic motion subtype/result distributions and coverage counts for the fixed 100-record sample.
- The report records the sample parameters and confirms no database writes or network calls.
- The measured result is documented in the canonical Beta report and FC ingestion Swimm walkthrough.
- Focused evaluator/classifier tests pass.

Harness criteria: The fixed 100-record evaluator passes; focused evaluator/classifier tests pass; canonical report and Swimm walkthrough record the measured result.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; no generated reference changes expected.

Rollback/recovery: Remove the new evaluation artifact and revert the evaluator/report/docs commit; no database or raw-data recovery is required.

Evidence: Managed run `fc-activity-motion-coverage-measurement-20260928-070601-4f768fd9` recorded the fixed cohort and focused validation. The 100-record report found 8 motion cases, 22 motion events, 22/22 complete evidence, 22.73% subtype coverage, and 18.18% result coverage; unknowns remained visible. `network_called=false` and `database_written=false`.

Files changed: `scripts/evaluate_fc_activity_deterministic.py`; `tests/test_evaluate_fc_activity_deterministic.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; this task record. Evaluation artifact: `data/eval/fc_activity_motion_coverage_20260928.json`.
Delegated work: Explore completed a bounded read-only inventory of evaluator, classifier, tests, docs, and data surfaces; no files changed.
Focused validation: `python -m pytest tests/test_evaluate_fc_activity_deterministic.py tests/test_classify_fc_activity.py -q` passed 59 tests; the fixed evaluator passed with 100 actual records; `git diff --check` and generated-doc validation passed.
Residual risk: Coverage is observed extraction coverage, not gold-set accuracy. Unknowns remain high (17/22 subtype, 18/22 result), and the cohort is not a population estimate.
Next bounded task: Expand the fixed fixture/gold-set matrix only if the measured cohort reveals a material taxonomy gap.

## Hypothesis

If the evaluator aggregates the existing promoted motion events correctly, the fixed seeded cohort will produce a deterministic subtype/result distribution while preserving the existing 100-record sample and read-only contract.

## Plan

1. Add the smallest pure aggregation helper and focused tests.
2. Run the fixed 100-record evaluator with a new output artifact.
3. Update canonical documentation and Swimm with measured evidence, then pass the evidence gate.

## Execution Checkpoints

- Delegation: Explore, bounded read-only inventory; structured result returned in session.
- Implementation: Pending evaluator/reporting change and focused check.
- Documentation: Pending canonical report and Swimm walkthrough updates.
- Recovery: Evaluation artifact path will be `data/eval/fc_activity_motion_coverage_20260928.json`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | Existing seeded evaluator is the safest bounded measurement surface; only motion aggregation is missing. | Explore inventory; evaluator source review |

## Completion

Completion recorded: yes

Summary: Added deterministic motion coverage aggregation and measured the fixed seeded 100-record cohort without database or network writes.

Validation: Managed criteria 0, 1, and 2 passed; `scripts/evidence_gate.py` passed with 5 recorded commands.

Residual risk: Coverage is not accuracy; broader source-text fixtures and gold-set validation remain.

Next recommended task: Pending measurement.
