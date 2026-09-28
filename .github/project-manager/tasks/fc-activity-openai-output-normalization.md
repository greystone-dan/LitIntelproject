# Task: Normalize open-ended FC Activity model outputs

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Normalize alternate nano and mini loose JSON structures into comparable FC Activity coverage fields without changing raw artifacts.
Why now: The mini run contains richer nested information than the strict comparator counted, but model-specific key drift prevents fair comparison.
Owner surface: New read-only output normalization/evaluation script under `scripts/`.
Dependencies: Completed nano loose and mini loose artifacts, deterministic IMM-15 report.
Risk boundary: No API calls, no database writes, raw artifacts immutable, normalization is evaluation-only and advisory.
Smallest falsifiable check: Run the normalizer on both artifacts and verify it recovers known alternate filing, judge, and motion structures while reporting review flags.
Acceptance criteria:
- Preserve raw model records and write separate normalized artifacts.
- Normalize common filing-date, decision-date/type, judge, motion, and identity variants.
- Report per-model coverage and review flags; do not silently claim accuracy.
- Validate output against a small set of expected alternate structures.
Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; normalized artifacts under `data/eval/`.
Rollback/recovery: Delete only normalized artifacts and script; raw model and deterministic artifacts remain untouched.
Commit allowed: yes
Push allowed: yes
Evidence: Read-only inventory found recurring alternate filing keys, nested decision structures, judge strings, and 5+ motion row shapes across both completed pilots. Added and ran the evaluation-only normalizer on both artifacts. Normalized coverage was nano: filing date 95/100, decision date 100/100, decision type 38/100, judges 85/100, motions 82/100 with 119 rows; mini: filing date 100/100, decision date 98/100, decision type 3/100, judges 92/100, motions 46/100 with 61 rows. The normalizer preserves source paths and emits missing-field flags; no API or database access occurred.
Files changed: `scripts/normalize_fc_activity_openai_outputs.py`, this task record, generated script catalog, and normalized artifact under `data/eval/`.
Focused validation: normalizer compilation and execution passed on both artifacts; nested challenged-decision handling was rerun; generated-doc check and `git diff --check` passed.
Residual risk: Key normalization improves comparability but does not establish factual precision. Mini decision-type recovery remains low because many responses describe decisions narratively without a discrete type; manual source review remains required.
Next bounded task: Manually review a stratified set of normalized model/deterministic disagreements.
