# Task: FC Activity leave-decision coverage

Status: complete
Created: 2026-09-27
Updated: 2026-09-27
Task: Improve deterministic leave-decision discernibility using VBA-derived registry wording while preserving pending and not-applicable states.

Why now: Leave decisions are explicit in 582/1,000 sampled classifications; recent cases may be pending, but unresolved leave records need a clear pending label rather than an undifferentiated unknown.

Owner surface: `scripts/classify_fc_activity.py`, focused classifier tests, and bounded deterministic evaluation.

Commit allowed: yes

Push allowed: yes

Dependencies: VBA-aligned logic in `scripts/fetch_fc_procedural_history.py`, FC Activity evaluator, existing leave-decision tests.

Risk boundary: Do not infer a granted/refused leave decision from a generic final decision. Preserve explicit outcomes, later-review inferred grants, discontinuance/withdrawal/termination not-applicable states, raw evidence, and source separation.

Hypothesis: If registry shorthand and French leave-outcome wording are added to the existing explicit rules, and unresolved leave applications are labeled `pending` in context, leave status will become discernible without converting pending cases into outcomes.

Smallest falsifiable check: Add focused tests for English shorthand, French outcome wording, and a filed-but-unresolved application; run the focused classifier suite and compare the fixed 1,000-case report.

Acceptance criteria:
- Explicit English shorthand and French leave outcomes classify with source evidence.
- Filed but unresolved leave applications expose `leave_context.status = pending`.
- Discontinued, withdrawn, terminated, direct-review, and later-review inference behavior does not regress.
- Focused tests, compilation, deterministic evaluation, canonical documentation, and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; bounded reports under `data/eval/`.

Rollback/recovery: Revert only the classifier, focused tests, docs, task record, and new bounded report. Do not modify raw Activity tables or canonical judgment data.

Evidence: Focused classifier suite passed 49 tests after the rule and pending-state changes. The broader Activity suite passed 65 tests. The fixed 1,000-case comparison changed 14 prior unknown leave results to explicit outcomes (7 granted and 7 refused), with no event-count changes; the new report contains 104 pending leave applications. Python compilation, editor diagnostics, and `git diff --check` passed. `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md` were updated. Managed run `fc-activity-leave-decision-coverage-20260927-20260927-193906-c82d2f4d` passed all four criteria and the evidence gate.

Files changed: `scripts/classify_fc_activity.py`, `tests/test_classify_fc_activity.py`, `data/eval/fc_activity_real_evaluation_20261001_1000_leave_coverage_v1.json`, `data/eval/fc_activity_real_evaluation_20261001_1000_leave_coverage_harness.json`, `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, `.swm/fc-ingest-source-pipeline.sw.md`, and this task record.

Delegated work: Explore performed a bounded read-only inventory of the classifier, tests, evaluator, VBA-aligned procedural-history port, and Excel reference availability. No delegated files were changed.

Focused validation: `pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py tests/test_review_fc_activity_local.py tests/test_audit_fc_activity_openai.py -q` passed 65 tests; the fixed 1,000-case evaluation passed read-only; `py_compile`, editor diagnostics, and `git diff --check` passed.

Residual risk: A pending label means no leave outcome was observed in the captured Activity history; it does not prove the matter is currently pending in the Court registry. The remaining 82 `unknown` leave contexts in the fixed sample have no challenged-decision record, so they are a separate source-coverage gap rather than unresolved leave decisions. Explicit outcome precision still needs a reviewed gold set.

Next bounded task: Build a reviewed leave-decision gold set spanning recent pending cases, shorthand outcomes, French entries, discontinuance, withdrawal, termination, and later-review inference, then measure precision and recall.
