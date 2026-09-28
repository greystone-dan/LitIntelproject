# Task: Discover FC Activity motion patterns at corpus scale

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Use the 318k-record FC Activity corpus to measure motion/procedural patterns and run a bounded OpenAI review batch for rule suggestions without changing source or canonical data.

Why now: The fixed 100-record measurement shows 22.73% motion subtype coverage and 18.18% result coverage, with unknowns dominating. The broader corpus can identify recurring evidence patterns before taxonomy changes.

Owner surface: FC Activity evaluation and review-only audit scripts

Commit allowed: yes

Push allowed: yes

Dependencies: `scripts/evaluate_fc_activity_deterministic.py`, `scripts/audit_fc_activity_openai.py`, existing FC Activity database, OpenAI API key/configuration, Beta comparison report, and FC ingestion Swimm walkthrough.

Risk boundary: Read-only database access and filesystem evaluation artifacts only. OpenAI use is explicitly user-authorized but capped at a 10-case batch and $0.01 estimated budget. No production/canonical writes, source collection, destructive actions, or automatic rule promotion.

Smallest falsifiable check: `venv\\Scripts\\python.exe scripts\\evaluate_fc_activity_deterministic.py --sample-size 1000 --seed 20260925 --recent-years 7 --recent-share 0.7 --output data\\eval\\fc_activity_motion_patterns_20260928.json`

Acceptance criteria:

- A seeded 1,000-record corpus baseline is produced with motion coverage and unknown distributions.
- A bounded OpenAI review batch runs only if the configured key is available and the $0.01 estimate is within budget; its output remains review-only.
- Findings are summarized without automatically changing classifier rules.
- Canonical report and Swimm walkthrough record commands, artifact paths, observed patterns, API budget/status, and residual uncertainty.
- Focused evaluator/audit tests and evidence gate pass.

Harness criteria: The 1,000-record deterministic baseline passes; the bounded OpenAI audit is prepared or completed within its explicit budget and review-only contract; focused tests pass; canonical report and Swimm walkthrough record evidence.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; no generated reference changes expected.

Rollback/recovery: Delete only new evaluation/audit artifacts if needed and revert the task commit; no database or canonical recovery is required. Do not retry API calls outside the recorded budget.

Evidence: Managed run `fc-activity-motion-pattern-discovery-20260928-072507-94d5d481` recorded the seeded 1,000-record baseline, a prepared 10-case sample, a completed OpenAI audit, 62 focused tests, and documentation checks. The baseline found 139 motion cases and 950 motion events; subtype coverage was 26.32% and result coverage 13.37%, with unknowns preserved. The OpenAI audit estimated cost `$0.0014555`, returned 3 advisory findings, and recorded `database_written=false`.

Files changed: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; this task record. Evaluation and audit artifacts: `data/eval/fc_activity_motion_patterns_20260928.json`; `data/eval/fc_activity_openai_motion_review_20260928.json`.
Delegated work: Explore completed a bounded read-only inventory of corpus, evaluator, OpenAI audit path, tests, and operational docs; no files changed.
Focused validation: The seeded evaluator completed; OpenAI audit completed within the $0.01 cap; `python -m pytest tests/test_evaluate_fc_activity_deterministic.py tests/test_audit_fc_activity_openai.py tests/test_classify_fc_activity.py -q` passed 62 tests; `git diff --check` and generated-doc validation passed.
Residual risk: A 1,000-record sample is not population truth; OpenAI suggestions are advisory and may be incomplete, inconsistent, or wrong. The audit sample contained only one case with motion events, so the findings are not a motion-specific accuracy estimate.
Next bounded task: Convert recurring, source-supported unknown patterns into a reviewed fixture/gold-set matrix before changing classifier rules.

## Hypothesis

If the existing evaluator and audit path are applied to a seeded corpus baseline and a small budget-capped review batch, recurring unknown motion evidence patterns will become measurable and produce reviewable rule suggestions without writes.

## Plan

1. Run the seeded 1,000-record deterministic baseline.
2. Send one 10-case, $0.01-capped OpenAI review batch if configuration permits.
3. Validate artifacts, summarize patterns, update canonical documentation and Swimm, and pass the evidence gate.

## Execution Checkpoints

- Delegation: Explore, bounded read-only inventory; structured result returned in session.
- Implementation: Pending corpus baseline and bounded audit execution.
- Documentation: Pending canonical report and Swimm walkthrough updates.
- Recovery: Run state/logs under `.github/project-manager/runs/`; evaluation artifacts under `data/eval/`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested continued corpus breakdown and explicitly authorized bounded OpenAI assistance. | Explore inventory; existing audit budget/send gate |

## Completion

Completion recorded: yes

Summary: Measured recurring motion/procedural patterns across a seeded 1,000-record corpus sample and completed one budget-capped OpenAI review batch without production or canonical writes.

Validation: Managed criteria 0, 1, 2, and 3 passed; `scripts/evidence_gate.py` passed with 7 recorded commands.

Residual risk: High unknown rates and the general-purpose audit sample require source-backed fixture/gold-set review before classifier changes.

Next recommended task: Select recurring unknown motion phrases from the 1,000-record artifact and build a reviewed fixture/gold-set matrix.
