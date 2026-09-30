# Task: Show FC Activity outcomes as procedural branches

Status: active
Created: 2026-09-29
Updated: 2026-09-29

## Task Record

Task: Replace the disconnected, hard-coded FC Activity flow summary with live procedural branches for active cases, leave outcomes, and judicial-review outcomes.

Why now: The active `/data-explorer` visualization presents hard-coded, disconnected outcome counts beside a milestone Sankey, which can imply mutually exclusive transitions despite overlapping classifier dimensions.

Owner surface: `backend/analytics_service.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `FCActivityClassification.classification_json`, `scripts/classify_fc_activity.py`, FC History renderer, focused feature tests.

Risk boundary: Do not modify classifications, source activity rows, canonical judgments, or run a bulk classifier. Do not claim a Sankey transition where classification dimensions overlap.

Smallest falsifiable check: A focused aggregation test with synthetic classification JSON verifies that active, leave granted/refused, and JR granted/dismissed records produce one exclusive branch each and live totals.

Acceptance criteria:

- `/api/fc-activity/flow` derives values from the filtered current `FCActivityClassification` inventory rather than constants.
- The visualization shows active, leave granted/refused, and JR granted/dismissed as connected procedural branches.
- Every rendered link is an exclusive lifecycle transition; applicability/overlap limits are disclosed rather than encoded as a Sankey.
- Focused FC visualization test passes.

Harness criteria: Live aggregation and exclusive-branch fixture pass; renderer identifies the output as procedural branches.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`; `.swm/fc-ingest-source-pipeline.sw.md`; no generated reference changes expected.

Rollback/recovery: Revert the read-only analytics, renderer, test, and documentation changes. No database data or schema is changed.

Evidence: Pending.

Files changed: Pending.
Delegated work: Exception: no capable managed-worker tool is available in this session; the bounded owner slice is being completed directly.
Focused validation: Pending.
Residual risk: Pending.
Next bounded task: None.

## Hypothesis

If each classified case is assigned one lifecycle branch using classifier precedence and applicability, the focused aggregation test will show connected, non-overlapping active/leave/JR flows whose branch sum equals the filtered classification count.

## Plan

1. Aggregate current classification JSON into exclusive procedural branches.
2. Render connected branches and disclose their evidence boundary.
3. Add focused regression coverage and update the UI/Swimm documentation.

## Execution Checkpoints

- Delegation: Direct bounded execution; managed-worker capability unavailable.
- Implementation: Pending.
- Documentation: Pending.
- Recovery: No long-running operation or data mutation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Use exclusive lifecycle branches, not a full cross-field Sankey | Leave, JR, closure, and applicability are separate classifier dimensions and may overlap | `scripts/classify_fc_activity.py` field-applicability contract |

## Completion

Completion recorded: no

Summary: Active work.

Validation: Pending.

Residual risk: Pending.

Next recommended task: None.