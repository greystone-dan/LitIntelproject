# Task: FC Activity subject coverage expansion

Status: in_progress
Created: 2026-09-27
Updated: 2026-09-27

Task: Review a large generic-institution-only sample and expand deterministic decision-subject extraction using high-frequency, source-backed program wording.

Why now: The fixed 1,000-case Activity report has 461 explicit subjects, 437 generic-institution-only cases, 8 cases with no subject evidence, and 94 cases without challenged-decision records.

Owner surface: `scripts/classify_fc_activity.py`, focused classifier tests, and bounded deterministic evaluation.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing generic subject availability model, fixed seeded evaluation, VBA-informed Activity workflow, and current subject tests.

Risk boundary: Preserve generic institution labels and do not infer legal subjects from IRCC, IRB, CBSA, visa-office, embassy, or tribunal identity alone. No schema/API change, database write, external model promotion, or canonical judgment/citation/statute modification.

Hypothesis: If high-frequency explicit program markers are extracted from the generic-only pool and validated against a reviewed sample, explicit subject coverage will increase with at least 90% precision and no regression in existing subject categories.

Smallest falsifiable check: Rank subject-like phrases across a large generic-only sample, select the highest-frequency legally specific candidates, add focused tests, and rerun the fixed 1,000-case report.

Acceptance criteria:
- Review at least 50 generic-only cases and rank recurring subject-like wording.
- Add only source-backed, legally specific deterministic patterns.
- Precision is at least 90% and recall at least 70% within the reviewed sample.
- Existing subject categories do not regress and generic labels remain generic.
- Focused tests, compilation, deterministic evaluation, canonical documentation, and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; bounded reports under `data/eval/`.

Rollback/recovery: Revert only classifier, tests, docs, task record, and new bounded evaluation artifacts. Do not modify Activity source tables or canonical judgment data.

Evidence:
