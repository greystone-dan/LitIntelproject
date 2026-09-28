# Task: FC Activity OpenAI feedback loop

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

Task: Use bounded OpenAI review batches across diverse real FC Activity samples to identify deterministic extraction gaps, then convert verified feedback into tested rules.
Why now: Deterministic Activity coverage has improved, but subject, hearing, judge-stage, and delay fields still need broad-sample feedback before further rule expansion.
Owner surface: `scripts/evaluate_fc_activity_deterministic.py`, existing OpenAI audit/review tooling, `scripts/classify_fc_activity.py`, focused Activity tests, and bounded evaluation artifacts.
Commit allowed: yes
Push allowed: yes
Dependencies: Existing real Activity inventory, deterministic classifier, OpenAI credentials/configuration, bounded audit path, and no-write review contract.
Risk boundary: OpenAI calls are review-only and bounded to approved sample batches. No production fact writes, no canonical ingestion, no database mutation, no secrets in logs, and no automatic promotion of model output. Deterministic extraction remains authoritative.
Smallest falsifiable check: Run one bounded 100-record diverse review batch, verify evidence-linked JSON output and measured disagreements, then implement only a high-confidence deterministic rule supported by multiple examples.
Acceptance criteria:
- Batch sampling spans distinct years and procedural/source patterns rather than repeating the seeded sample.
- Each model response is evidence-linked, schema-validated, and stored as review feedback only.
- Review feedback produces a measured list of deterministic candidate rules with positive/negative examples.
- At least one high-confidence rule is implemented with focused tests, or the evidence shows no safe rule should be added.
- No production/database writes or automatic LLM fact promotion occur.
- Focused tests, real-data evaluation, canonical documentation, and Swimm checkpoint are updated.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; bounded artifacts under `data/eval/`; no generated references.
Rollback/recovery: Delete only new review artifacts and revert classifier/tests/docs/task changes from this task. Do not touch raw Activity tables or canonical records.
Evidence: Audit-path tests passed 3, then 12 after source-evidence support; focused Activity suite passed 42. Prepared and sent four 100-record batches. Batch 1 cost $0.0069954 with 3 findings; batch 2 cost $0.0070014 but overlapped batch 1 100/100 because both used a 100-case artifact; batch 3 from a 1,000-case corpus had zero overlap with batch 1 and cost $0.0083156; batch 4 used the corrected source-backed corpus and cost $0.0150174 with 3 findings. All completed artifacts report `database_written: false`; no model fact was promoted automatically. One source-supported `appearance_filed` rule was implemented and tested. Updated [SYSTEM_REFERENCE.md](../../SYSTEM_REFERENCE.md), [docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md](../../docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md), and [.swm/fc-ingest-source-pipeline.sw.md](../../.swm/fc-ingest-source-pipeline.sw.md).
Files changed: `scripts/audit_fc_activity_openai.py`, `scripts/evaluate_fc_activity_deterministic.py`, `scripts/classify_fc_activity.py`, focused tests, canonical docs, Swimm walkthrough, and bounded artifacts under `data/eval/`.
Delegated work: Explore completed a read-only audit-path review; the manager retained implementation, API calls, rule acceptance, documentation, and final validation.
Focused validation: `\.\venv\Scripts\python.exe -m pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py tests/test_review_fc_activity_local.py -q` passed 42 tests. Audit/evaluator focused tests passed 12 tests before the final classifier suite.
Residual risk: External model feedback may be incomplete or wrong; no rule is accepted without source evidence and deterministic tests. Actual API cost must remain bounded and recorded.
Next bounded task: Run another source-backed, non-overlapping 100-record batch only when a new extraction hypothesis is defined; retain human review for ambiguous procedural semantics.
