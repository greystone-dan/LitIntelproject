# Task: Add ALJR filer, minister, and motion presence fields

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Add conservative deterministic fields for whether motions are present, who filed the ALJR, and which Minister/respondent it was filed against.

Why now: These fields are simpler and more useful for a targeted later AI enrichment run than detailed motion subtype/result extraction.

Owner surface: `scripts/classify_fc_activity.py` and focused FC Activity tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Fixed IMM-15 evaluation and originating ALJR application rows.

Risk boundary: Preserve source evidence and unknowns; do not infer filer or minister from unrelated later events, and do not replace underlying tribunal-maker fields.

Smallest falsifiable check: Inventory originating-row phrases for filer/respondent and compare binary motion presence with existing procedural motion events.

Acceptance criteria:

- The classifier emits a conservative binary motion-presence field with source evidence.
- The classifier distinguishes ALJR filer as government or individual when explicit, otherwise unknown.
- The classifier identifies MPSEP/CBSA and MCI/IRCC respondent signals when explicit, otherwise unknown.
- Focused tests cover positive, negative, and unknown cases.
- The fixed evaluation reports coverage and the changes are documented in the canonical FC Activity comparison and Swimm walkthrough.

Harness criteria: Fixed evaluation remains read-only and reports `database_written=false`.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`.

Rollback/recovery: Revert only the focused classifier, test, and documentation edits; evaluation output is disposable.

Evidence: Delegated inventory confirmed existing evidence-linked motion events and warned that tribunal-maker fields must not be used as respondent identity. Focused tests passed (68). Fixed 1,000-case evaluation passed with `database_written=false`: motion presence yes in 267 cases and no in 733; filer type individual 969, government 1, organization 18, unknown 12; respondent ministry MCI/IRCC 867, MPSEP/CBSA 74, unknown 59. Canonical documentation: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`. Swimm walkthrough: `.swm/fc-ingest-source-pipeline.sw.md`.

Files changed: `scripts/classify_fc_activity.py`; `tests/test_classify_fc_activity.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `data/eval/fc_activity_imm_suffix_15_party_motion_20260928.json`.
Delegated work: Explore, bounded read-only inventory; no files changed.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py -q` (68 passed); fixed evaluator rerun (1,000 cases, `database_written=false`).
Residual risk: Filer classification defaults to individual only after case-name party parsing excludes government and organization markers; it is not a legal-party adjudication. Ministry mapping is limited to explicit case-name abbreviations.
Next bounded task: Use these fields as the structured input for a targeted AI review of motion subtype/result and unresolved party cases.

## Hypothesis

If the originating ALJR rows contain explicit applicant/respondent and minister phrases, these three fields can be added deterministically with useful coverage while preserving unknowns for ambiguous records.

## Plan

1. Inventory originating-row patterns and existing motion evidence.
2. Add fields and focused fixtures.
3. Run focused tests and the fixed evaluation, then update documentation.

## Execution Checkpoints

- Delegation: Pending Explore inventory and structured result.
- Implementation: Pending.
- Documentation: Pending canonical document and Swimm walkthrough updates.
- Recovery: No database or bulk-write operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User selected simple motion presence, ALJR filer, and minister fields for later AI enhancement. | Existing FC Activity classifier and fixed evaluation |

## Completion

Completion recorded: yes

Summary: Added evidence-linked binary motion presence and conservative ALJR filer/respondent ministry fields.

Validation: Focused classifier suite passed 68/68; bounded fixed evaluation passed with no database writes.

Residual risk: Detailed motion subtype/result remains intentionally unresolved; filer and ministry fields preserve unknown/organization categories.

Next recommended task: Run a bounded AI enhancement experiment on motion subtype/result using only cases with `motion_presence=yes`.