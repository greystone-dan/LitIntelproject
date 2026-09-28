# Task: Audit challenged-decision date coverage

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Audit and improve deterministic extraction of the date of the underlying decision being challenged.

Why now: This field is present in only 507/1,000 cases in the fixed evaluation and is the clearest remaining coverage gap among core challenged-decision fields.

Owner surface: `scripts/classify_fc_activity.py` and its focused regression tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Fixed seeded 1,000-case evaluation and existing FC Activity fixtures.

Risk boundary: Read-only evaluation only; do not infer dates from unrelated procedural events, alter leave/final decision semantics, or write database records.

Smallest falsifiable check: Inventory missing `challenged_decision.decision_date` cases and classify whether the source text contains an unhandled explicit date signal.

Acceptance criteria:

- Missing-date cases are classified into parser gaps, alternate source locations, genuinely absent dates, or ambiguous dates.
- Any parser change is evidence-linked and covered by focused regression tests.
- The fixed evaluation is rerun and reports changed coverage without changing leave/final decision semantics.
- Relevant canonical documentation and the FC Activity Swimm walkthrough record the result.

Harness criteria: The missing-date audit is bounded to the fixed 1,000-case sample and performs no database writes.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`.

Rollback/recovery: Revert only the focused parser/test/documentation edits; evaluation artifacts are disposable and read-only.

Evidence: Delegated read-only inventory identified explicit semicolon, space-separated, and French date forms. Focused tests passed (65). Fixed 1,000-case evaluation rerun produced 695/1,000 challenged-decision dates (69.5%), up from 507/1,000 (50.7%), and 973/1,000 combined decision information (97.3%), up from 963/1,000 (96.3%). Applicability coverage for application perfection, leave, hearing, judicial-review result, judicial-review final decision, and generic final decision was unchanged. Canonical documentation: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`. Swimm walkthrough: `.swm/fc-ingest-source-pipeline.sw.md`.

Files changed: `scripts/classify_fc_activity.py`; `tests/test_classify_fc_activity.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `data/eval/fc_activity_imm_suffix_15_after_date_patterns_20260928.json`.
Delegated work: Explore, bounded read-only inventory of the fixed evaluation artifact; no files changed.
Focused validation: `python -m pytest tests/test_classify_fc_activity.py -q` (65 passed); fixed evaluator rerun (1,000 cases, `database_written=false`).
Residual risk: 305 cases still lack an explicit challenged-decision date; some may be genuinely unavailable or ambiguous. Returned date strings are not normalized to ISO format.
Next bounded task: Audit the remaining 305 missing dates for additional explicit, non-ambiguous formats before considering date normalization.

## Hypothesis

If the missing dates are primarily alternate explicit date phrasings or available in nearby originating-application text, a bounded audit will identify a small evidence-backed parser improvement without requiring inference from later procedural events.

## Plan

1. Inventory missing-date cases in the fixed evaluation sample.
2. Implement only evidence-backed date parsing gaps and add fixtures.
3. Rerun focused tests and the bounded evaluation, then update documentation.

## Execution Checkpoints

- Delegation: Pending Explore inventory and structured report.
- Implementation: Pending audit result.
- Documentation: Pending canonical document and Swimm walkthrough updates.
- Recovery: No database or bulk-write operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested the next step after identifying 50.7% challenged-decision date coverage. | Fixed evaluation artifact and current classifier metrics |

## Completion

Completion recorded: yes

Summary: Added evidence-backed challenged-decision date patterns and measured the coverage increase.

Validation: Focused classifier suite passed 65/65; bounded fixed evaluation passed with 1,000 cases and no database writes.

Residual risk: Remaining missing dates require source-level classification; no date inference was added.

Next recommended task: Perform a bounded audit of the remaining 305 missing dates.