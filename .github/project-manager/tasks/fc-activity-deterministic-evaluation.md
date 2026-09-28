# Task: FC Activity deterministic evaluation

Status: complete
Created: 2026-09-25
Updated: 2026-09-26

## Task Record

Task: Measure and improve deterministic extraction of Federal Court Activity procedural records, using bounded recent-year samples and up to $5 of OpenAI API review.

Why now: The Activity inventory is intended to represent every IMM matter filed in Federal Court, including matters without a published judgment. We need trustworthy procedural statistics before adding LLM-assisted insights.

Owner surface: `scripts/classify_fc_activity.py` and focused Activity evaluation tests/reports

Commit allowed: yes

Push allowed: yes

Dependencies: `fc_activity_cases` and `fc_activity_documents`; existing deterministic classifier; representative Activity records across years; explicit OpenAI API budget approval from the user.

Risk boundary: Keep Activity records separate from canonical cases, citations, statutes, judgment text, embeddings, and ingestion tables. Do not interrupt or modify the active/resumable collector. OpenAI use is limited to a bounded audit sample and $5 maximum; do not send secrets or unrestricted data.

Smallest falsifiable check: Run deterministic extraction on a fixed cross-year sample, verify every emitted event retains source document evidence, and compare a recent-year weighted audit sample against an OpenAI review within the approved budget.

Acceptance criteria:

- Deterministic event taxonomy covers filing/perfection, leave, judge, motions, stays, hearings, decisions, and procedural closure signals without changing raw Activity rows.
- Cross-year sample report measures extraction coverage, unknowns, ambiguities, and evidence completeness, with heavier representation from the last 6-7 years.
- OpenAI audit uses a frozen, redacted/limited sample, records model, prompt version, token usage, estimated spend, and disagreements, and stays at or below $5.
- Focused tests cover positive, negative, ambiguous, repeated-motion, judge-name, bilingual, and source-date semantics.
- Canonical repository documentation and the relevant Swimm walkthrough describe the Activity-only deterministic boundary and evaluation checkpoint.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated references only if source/schema contracts change.

Rollback/recovery: Revert only the classifier/test/report changes from this task; delete generated evaluation artifacts if needed. Resume the collector using `data/raw/fc/Resume activity extraction command.ps1`; do not rerun or alter its existing checkpoints.

Evidence: Delegated review completed on the Activity schema, classifier, tests, taxonomy, and evaluation design; the structured review required a retry and returned the required files/commands/results/failures/uncertainty/recommendation fields. The classifier/test slice changed only `scripts/classify_fc_activity.py` and `tests/test_classify_fc_activity.py`. Focused validation passed: `21 passed` from `tests/test_classify_fc_activity.py`, `tests/test_evaluate_fc_activity_deterministic.py`, and `tests/test_audit_fc_activity_openai.py`. The read-only deterministic report was regenerated at `data/eval/fc_activity_deterministic_evaluation_20260925.json` for 100 records with seven-year weighting; it reported 119 application-filed, 70 perfected, 77 leave-decision, 68 judge, 104 motion-filed, 10 motion-decision, 23 stay, 31 hearing, and 66 decision events. The bounded OpenAI audit was regenerated at `data/eval/fc_activity_openai_audit_20260925.json` with `gpt-4.1-nano`, 12 records, 75% recent-year weighting, no database writes, and estimated cost `$0.001548`, below the approved `$5` ceiling. Documentation was updated in `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.

## Hypothesis

If deterministic Activity extraction is structured as evidence-backed repeatable events, then a fixed cross-year sample will expose measurable coverage and ambiguity patterns that can be reviewed with a bounded recent-year OpenAI audit without writing canonical data.

## Plan

1. Freeze a bounded cross-year sample and define event coverage metrics.
2. Extend deterministic extraction and fixtures for event/date/judge/motion semantics.
3. Run focused tests and generate a read-only evaluation report.
4. Send only the approved bounded recent-year audit sample to OpenAI and record disagreements/cost.
5. Update canonical documentation and the Activity Swimm walkthrough.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager; bounded read-only review of Activity schema, classifier, tests, taxonomy, and evaluation design. A structured retry is required if the first return does not follow the exact delegated schema.
- Implementation: classifier and focused tests; no collector or canonical ingestion changes.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/fc-ingest-source-pipeline.sw.md` must be updated before completion.
- Recovery: collector resume script is `data/raw/fc/Resume activity extraction command.ps1`; evaluation artifacts must be bounded and rerunnable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Keep raw Activity records separate and add derived deterministic events | User wants management statistics over all FC IMM matters, including matters without published judgments | User request; `SYSTEM_REFERENCE.md`; Activity runbook |
| 2026-09-25 | Weight the last 6-7 years more heavily in the OpenAI audit | User requested recent-year emphasis while retaining cross-year coverage | User request |

## Completion

Completion recorded: 2026-09-26

Summary: Complete for the bounded deterministic evaluation and audit checkpoint. Raw Activity rows and the collector were not modified.

Validation: Focused suite passed with 21 tests. Deterministic report and OpenAI audit both completed read-only; documentation consistency was checked with `git diff --check`.

Residual risk: Registry wording variability, semantic date ambiguity, final-decision marker clarity, and incomplete linkage between Activity records and published judgments may produce unknown or conflicting signals. No derived event table or API/UI presentation was added.

Next recommended task: Expand the deterministic taxonomy and metrics for settlements, stays of removal, procedural closure, hearing outcomes, and delay intervals before exposing Activity statistics in the API/UI.
