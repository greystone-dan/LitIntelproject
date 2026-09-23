# Task: Mason citation-event external AI framework

Status: complete
Created: 2026-09-23
Updated: 2026-09-23

## Task Record

Task: Establish a reusable, reasonably fast and cheap framework that takes Mason citation events, sends them to an external AI in a reliable method, and returns source-backed argument-level citation events for review.

Why now: The first 97-event runs exposed poor bulk-response reliability. A one-event isolation experiment was needed before scaling beyond Mason.

Owner surface: `scripts/run_treatment_teacher_batch.py` and the Mason evaluation workflow under `data/eval/llm_discussion_units_pilot/`.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing deterministic citation rows, Mason Discussion Units, OpenAI-compatible teacher contract, and the current fixture/request artifacts.

Risk boundary: Report-only evaluation. Do not alter deterministic citation extraction, write canonical database rows, publish runtime treatment labels, run unbounded or concurrent paid operations, or expose secrets.

Smallest falsifiable check: Inspect all 10 completed Mason batches and compare submitted examples, returned labels, omissions, malformed responses, and source-span validation failures against the fixture.

Acceptance criteria:

- A bounded framework can process Mason citation events with explicit cost, checkpoint, retry/recovery, and output validation controls.
- The execution method is selected from evidence and keeps a 100-event test within the user-approved $3 budget.
- Accepted output preserves deterministic citation identity and exact source-backed spans, including argument-level context where available.
- Focused tests and a bounded Mason validation run pass, with quality and residual failure rates recorded.
- The canonical repository document and relevant Swimm walkthrough describe the framework and its boundaries.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/8.upryk5h6.sw.md`; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; generated references are not hand-edited.

Rollback/recovery: Preserve existing artifacts; use a new request/result/run identifier for each paid experiment. Revert only the new runner/framework changes if needed. No database rollback is applicable.

Evidence: Explore performed bounded reviews of the batch failure and one-event method. The original compact run processed all 97 events in 33 three-event batches for `$0.0315425`; 12 labels passed validation and its complete ledger records 42 malformed-response rows. The isolated rerun processed all 97 events in 97 one-event calls for `$0.0366286`; 31 labels passed, 65 were rejected by source validation, and one response was malformed. Two accepted labels populated argument context. Both complete ledgers preserve source-backed rows; focused tests and compilation passed, and canonical and Swimm documentation were updated.

## Hypothesis

If the Mason events are sent with a smaller response unit and stricter per-event contract, the focused audit will show that most current failures are caused by batch omissions or malformed model output rather than incorrect deterministic source anchors.

## Plan

1. Audit the completed 97-event run and identify the dominant failure mode.
2. Implement the smallest bounded execution improvement within the existing teacher contract.
3. Run focused tests and a paid Mason canary within the $3 approval.
4. Update canonical and Swimm documentation with observed quality, cost, and recovery behavior.

## Execution Checkpoints

- Delegation: Explore reviewed the original result, identifying large-response truncation and offset failures; the returned count discrepancy was independently resolved against the saved result, which contained 1 valid and 40 invalid labels.
- Implementation: Added bounded `--paragraph-context` fixture windows, the complete ledger, and a default `--batch-size 1` in the treatment runner; retained explicit batch-size control, checkpointing, budget, and exact-span validation.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` with the compact Mason framework, measured cost, quality limits, and runtime-disabled boundary.
- Recovery: Existing full run remains at `data/eval/llm_discussion_units_pilot/mason_argument_citation_all_result.json`; new experiments must use distinct artifacts.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-23 | Use Mason as the bounded proving ground | User requested a framework focused on Mason with a $3 test budget | Existing 97-event result and request artifacts |
| 2026-09-23 | Keep semantic treatment report-only | Deterministic citation records remain authoritative | `SYSTEM_REFERENCE.md` and current teacher contract |

## Completion

Completion recorded: yes

Summary: Mason now has a reusable report-only external-AI evaluation path and a complete 97-row review ledger that preserves deterministic citation provenance even when AI responses fail.

Validation: `23 passed` for `tests/test_teacher_contract.py` and `tests/test_package_discussion_units_llm.py`; Python compilation passed for the touched modules; isolated Mason run completed with 97 one-event calls and `$0.0366286` spend; the complete ledger passed assertions for 97 rows, complete coverage, valid status totals, and source-backed citation spans; `git diff --check` passed.

Residual risk: Only 31 of 97 isolated labels passed and most accepted labels still require human review; 65 were rejected by span/context validation and one response remained malformed. Argument-level context remains sparse, with two populated labels. No output is runtime-published.

Next recommended task: Review the 31 isolated accepted labels, then improve the contract by separating treatment classification from argument-context extraction and compare held-out semantic accuracy.
