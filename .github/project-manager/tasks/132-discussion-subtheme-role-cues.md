# Task: Refine weak Discussion Unit role cues

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Improve deterministic role-cue and governing-rule context quality for the exact weak sub-themes identified by the expanded external review.

Why now: The 16-case V1.2 review confirmed boundary and provenance quality but identified weak or missing role cues in `677:3`, `1093:1`, `1171:2`, and `18674:72`.

Owner surface: `backend/contextual_authority/subthemes.py` and focused sub-theme tests

Commit allowed: yes

Push allowed: yes

Dependencies: V1.4 sub-theme rules, V1.2 Discussion Unit packets, `tests/test_subthemes_v1.py`.

Risk boundary: Deterministic evidence and explanation quality only. Preserve source text, offsets, hashes, role taxonomy, procedural-claim filtering, local contrast gating, and read-only behavior. Do not activate runtime output or add embeddings/clustering.

Smallest falsifiable check: Reproduce the four cited sub-theme outputs and determine whether each weakness is a missing cue, a false-positive cue, or explanation/context compression before editing rules.

Acceptance criteria:

- Inspect exact cited sub-themes and their source evidence.
- Add the smallest rule/test change only if a repeated deterministic defect is demonstrated.
- Preserve explicit advocacy/disposition recall and existing negative filters.
- Validate focused sub-theme tests plus the Discussion Unit inspector contract.
- Update `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` with the result.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, `data/eval/discussion_units_external_review_v1_2_api_response.md`.

Rollback/recovery: Revert only this task's sub-theme/test/documentation edits; preserve V1.2 segmentation and all evaluation packets.

Evidence: Delegated inspection confirmed that `677:3` and `1171:2` are cue-free heading/appearance spans, not missed role extractions; `1093:1` contains valid `pursuant to` governing-rule evidence; and `18674:72` contains valid evidence, issue, and governing-rule cues. No repeated extraction defect justified a new rule. The smallest safe change appends a deterministic cue-free diagnostic to explanations when `argument_evidence` is empty and bumps `SUBTHEME_VERSION` to `1.4`. The 16 cohort packets and four baseline review packets were regenerated as dry runs with zero canonical/contextual writes and unchanged Discussion Unit counts. `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` document the V1.4 behavior.

## Hypothesis

If the cited weaknesses reflect deterministic cue or explanation gaps, a focused rule/test adjustment will improve explicit role visibility without changing source spans, offsets, hashes, or existing V1.3 precision tests.

## Completion

Completion recorded: yes

Summary: Completed the bounded role-cue review. The implementation labels cue-free spans as metadata or cue-free text without inventing roles, while preserving extraction rules and source evidence.

Validation: `python -m pytest tests/test_discussion_units_v1.py tests/test_subthemes_v1.py tests/test_discussion_unit_inspector.py -q` passed with 24 tests; bounded cohort assertions passed for all 16 cases; `git diff --check` passed with warnings only.

Residual risk: External review used sampled evidence and may have overgeneralized from weak examples. Cue-free spans remain intentionally unresolved hypotheses for human review, not legal conclusions.

Next recommended task: Continue bounded cohort review only if new evidence shows a repeated extraction false positive or false negative; otherwise keep the V1.4 layer offline and additive.