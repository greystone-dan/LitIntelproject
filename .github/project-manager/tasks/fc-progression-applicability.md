# Task: Model FC field applicability by case progression

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Distinguish known, pending, not-applicable, and not-observed FC Activity fields using deterministic case progression.

Why now: Current coverage treats structurally unreachable fields as missing. For example, judicial review cannot occur after leave is refused, but the current output leaves downstream fields looking unknown.

Owner surface: `scripts/classify_fc_activity.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing leave context, judicial review result, closing status, lifecycle status, milestone rollups, and evaluator report.

Risk boundary: Preserve existing evidence and public values; add applicability metadata without inventing events or treating inference as source fact. Motions remain paused.

Smallest falsifiable check: Add fixtures for leave refused, leave pending, leave granted with JR result, direct JR, and discontinuance; assert downstream field applicability states.

Acceptance criteria:

- `judicial_review_result` and `judicial_review_final_decision` are explicitly `not_applicable` after confirmed leave refusal.
- Pending and not-observed states remain distinct from structural non-applicability.
- Final decision markers are not confused with judicial-review final decisions; a leave dismissal may be the final decision observed for that case.
- Existing raw evidence values and focused classifier tests remain compatible.

Harness criteria: Progression fixtures pass; evaluator reports applicability counts; documentation explains the state model.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`

Rollback/recovery: Revert the applicability-only code/test/docs commit; no database migration or bulk write is required.

Evidence: Existing classifier inspection showed `leave_context.status` already distinguished `refused`, `pending`, direct judicial review, and inferred grant, while downstream final-decision applicability remained ambiguous. The implementation now emits `field_applicability` with explicit leave N/A reasons and explanations plus application-perfection and hearing applicability. The bounded 1,000-case evaluation recorded leave known=466, pending=252, not applicable=278; application perfection known=529, pending=309, not applicable=162; hearing known=516, pending=220, not observed=6, not applicable=258; judicial-review result known=52, pending=20, not applicable=672; judicial-review final known=50, pending=22, not applicable=672; `database_written=false`. A read-only stratification of all pending perfection and hearing cases found no safe inference rule: pending perfection concentrated in leave-refused (110), unknown/unresolved leave (85), and leave-pending (79); pending hearing concentrated in unknown/unresolved leave (89), leave-pending (79), and perfected subsets (28 and 24). No rule was promoted.

Files changed: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, `tests/test_classify_fc_activity.py`, `tests/test_evaluate_fc_activity_deterministic.py`, `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`, `.swm/fc-ingest-source-pipeline.sw.md`, this task record, and the read-only evaluation artifact.
Delegated work: Explore agent reviewed classifier, tests, docs, schema, and the existing 1,000-case artifact; no files changed.
Focused validation: `pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py -q` (70 passed); Python compilation, generated-doc check, and `git diff --check` passed; bounded evaluation completed with no database write. Pending-case stratification was read-only and promoted no rules.
Residual risk: Some terminal states remain uncertain when source history is incomplete or contradictory; production-order inference is supporting evidence, not a direct leave decision.
Next bounded task: Revalidate source completeness for a small pending-perfection and pending-hearing sample before considering additional deterministic rules.

## Hypothesis

If applicability is derived from confirmed progression states, the evaluator will stop counting unreachable judicial-review fields as missing while preserving genuinely pending and unobserved cases.

## Plan

1. Define the progression state matrix and field-status contract.
2. Implement leave/JR applicability metadata with focused fixtures.
3. Measure known, pending, not-applicable, and not-observed counts on the existing bounded report.
4. Update canonical and Swimm documentation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Add applicability metadata before expanding extraction rules | Coverage must distinguish impossible fields from missing evidence before rule improvements can be measured | Existing classifier already emits `not_reached`, `pending`, direct-JR, and terminal statuses |

## Completion

Completion recorded: yes

Summary: Added progression-aware applicability metadata and reporting for leave, judicial-review, application-perfection, and hearing fields without changing raw evidence values. A bounded pending-case review found no safe additional inference rule.

Validation: Focused classifier/evaluator tests and bounded read-only evaluation passed; final documentation checks pending.

Residual risk: Applicability coverage is not an accuracy estimate and does not yet cover every field.

Next recommended task: Revalidate a bounded source sample; keep pending states unchanged unless source evidence supports a precise rule.
