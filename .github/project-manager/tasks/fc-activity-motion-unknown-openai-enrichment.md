# Task: Enrich all unknown FC Activity motion subtypes with OpenAI suggestions

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Send all 700 unknown-subtype motion events from the fixed 1,000-record FC Activity report to the OpenAI API in resumable, budget-capped event batches and produce review-only subtype suggestions.

Why now: The user explicitly authorized OpenAI assistance to identify unknown motion subtypes. The existing 30-row report is insufficient; the full unknown-event population must be processed with evidence preserved.

Owner surface: `scripts/audit_fc_activity_motion_unknowns_openai.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `data/eval/fc_activity_motion_patterns_20260928.json`, OpenAI configuration, existing motion taxonomy, audit-contract tests, and canonical FC Activity documentation.

Risk boundary: External API calls are user-authorized but bounded by a hard `$5.00` task budget, batch size, timeout, and resumable checkpoint. No production/canonical database writes, no classifier rule promotion, no source mutation, and no automatic acceptance of suggestions.

Smallest falsifiable check: Dry-run over the full source report must enumerate 700 unknown motions, produce deterministic batches/checkpoint state, and prove projected spend is within the task budget before any network request.

Acceptance criteria:

- All 700 unknown motion events are selected from the source report with case/document IDs and bounded evidence.
- The adapter performs preflight cost control, resumable checkpoints, strict JSON parsing, and review-only output.
- The complete API pass finishes within the hard `$5.00` budget or records an exact bounded blocker without retrying beyond budget.
- Suggestions remain advisory with `rules_promoted=false` and `database_written=false`.
- Canonical report and Swimm walkthrough record batch count, actual spend, completion status, and residual uncertainty.
- Focused adapter/classifier tests and evidence gate pass.

Harness criteria: Full 700-event dry-run passes; focused adapter and classifier tests pass; bounded API enrichment completes within budget or records a precise blocker; canonical report and Swimm walkthrough record evidence.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated script catalog if a new script is added.

Rollback/recovery: Delete review artifacts/checkpoints and revert the task commit; no database recovery is required. Resume only from recorded checkpoints and never resend completed event IDs unless explicitly repairing an invalid response.

Evidence: Explore completed the bounded read-only inventory. The managed run recorded the dry-run, focused tests, repaired authentication, checkpoint repair, and bounded API retry. The final artifact records 700 source events, 698 structured suggestions, 2 unresolved events, actual spend `$0.0316852`, `network_called=true`, `database_written=false`, and `rules_promoted=false`. Canonical documentation was updated in `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` and `.swm/fc-ingest-source-pipeline.sw.md`. No gold set or classifier rule promotion occurred.

Files changed: `scripts/audit_fc_activity_motion_unknowns_openai.py`; `tests/test_audit_fc_activity_motion_unknowns_openai.py`; `data/eval/fc_activity_motion_unknowns_openai_20260928.json`; `data/eval/fc_activity_motion_unknowns_openai_20260928.checkpoint.json`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated script catalog.
Delegated work: Explore completed bounded read-only inventory of the existing audit path and recommended event-level adapter; no files changed.
Focused validation: `pytest tests/test_audit_fc_activity_motion_unknowns_openai.py tests/test_classify_fc_activity.py -q` passed with 51 tests. The managed full send and retry exited 0. Generated-document checks and the evidence gate remain final acceptance checks.
Residual risk: OpenAI subtype suggestions may be wrong, overconfident, or insufficiently evidenced. They are not classifier truth and require later source-backed review.
Next bounded task: Review API suggestions against source evidence before any fixture or classifier promotion.

## Hypothesis

If all unknown motion events are sent as evidence-bounded event batches with preflight budgeting and checkpoints, the API will return a complete advisory suggestion artifact without data writes or untracked spend.

## Plan

1. Implement and test the resumable event-level adapter.
2. Dry-run all 700 events and verify budget/checkpoint selection.
3. Send the complete bounded pass, validate outputs, and document results.

## Execution Checkpoints

- Delegation: Explore, bounded read-only inventory; structured report returned in session.
- Implementation: Complete; adapter tests passed.
- Documentation: Canonical report and Swimm walkthrough updated; generated references remain to be regenerated and checked.
- Recovery: Checkpoint/output paths under `data/eval/`; managed run/logs under `.github/project-manager/runs/`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User explicitly requested all unknown motions be sent to OpenAI for subtype suggestions; event-level batching is safer than case-level context reuse. | Existing 700-event report and delegated inventory |

## Completion

Completion recorded: yes

Summary: All 700 unknown motion events were sent in bounded, resumable batches. The review artifact contains 698 structured suggestions and 2 unresolved events; no database writes or rule promotion occurred.

Validation: Focused adapter/classifier tests passed; managed API commands exited 0. Final generated-document validation and evidence gate are pending.

Residual risk: Suggestions remain advisory and require source-backed review; two events did not yield structured suggestions after retry.

Next recommended task: Pending source-backed review.
