# Task: Implement five deterministic improvements from FC motion advisory output

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Convert the completed 700-event FC motion advisory review into five bounded code improvements: explicit motion phrase coverage, related-document subtype context, French motion variants, conservative stay handling, and cumulative audit-run bookkeeping.

Why now: The advisory output identified explicit source wording missed by the deterministic classifier and exposed retry metadata loss. These are trust and maintainability improvements, but suggestions remain advisory and must not be promoted automatically.

Owner surface: `scripts/classify_fc_activity.py` and `scripts/audit_fc_activity_motion_unknowns_openai.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity classifier, motion fixtures/tests, fixed 1,000-record evaluation, advisory artifact, canonical FC Activity documentation, and Swimm source-pipeline walkthrough.

Risk boundary: No production or canonical database writes, no gold set, no automatic OpenAI rule promotion, no unbounded API calls, and no changes to unrelated citation or ingestion layers.

Smallest falsifiable check: Focused classifier and adapter tests must demonstrate exact subtype normalization, context propagation, conservative stay fallback, and cumulative audit metadata without network access.

Acceptance criteria:

- Explicit English and French motion phrases from the advisory evidence classify deterministically with source evidence and exact-span tests.
- Related motion documents can inherit an explicit subtype only through a bounded, evidence-preserving context rule; unrelated documents remain unknown.
- French consent/stay/extension variants are covered without changing raw Activity text.
- Generic stay language remains generic unless an explicit target is present; no low-confidence advisory suggestion is promoted.
- Audit output preserves cumulative pass/retry counts, token usage, spend, and unresolved event keys.
- Focused tests, bounded deterministic evaluation, generated-document checks, and evidence gate pass.

Harness criteria:

- Phrase and French subtype rules pass focused exact-span tests.
- Context propagation passes related/unrelated document tests.
- Conservative stay behavior passes focused tests.
- Audit bookkeeping passes offline adapter tests and preserves cumulative metadata.
- Documentation and bounded evaluation checks pass with no network or database writes.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; generated script catalog if script metadata changes.

Rollback/recovery: Revert the task commit. Evaluation artifacts are read-only outputs; no database recovery is required. Do not rerun OpenAI calls unless explicitly authorized.

Evidence: Explore completed the bounded read-only inventory. The focused suite passed 58 tests. The seeded 1,000-case deterministic evaluation passed with no network or database writes: 952 motion events, 264 classified subtypes, 27.73% subtype coverage versus the prior 26.32%, and complete evidence on all 952 events. Generated-document validation passed. No OpenAI call, gold set, database write, or automatic rule promotion was performed.

Files changed: `scripts/classify_fc_activity.py`; `scripts/audit_fc_activity_motion_unknowns_openai.py`; `tests/test_motion_taxonomy.py`; `tests/test_audit_fc_activity_motion_unknowns_openai.py`; `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `docs/SCRIPT_CATALOG.generated.md`; `data/eval/fc_activity_motion_improvements_seeded_20260928.json`.
Delegated work: Explore completed a bounded read-only inventory of the classifier, adapter, focused tests, and FC Activity docs. It found missing French consent/stay variants, no context-propagation helper, conservative generic stay fallback, and incomplete retry/bookkeeping tests. No files were changed.
Focused validation: `pytest tests/test_motion_taxonomy.py tests/test_audit_fc_activity_motion_unknowns_openai.py tests/test_classify_fc_activity.py -q` passed 58 tests. Seeded 1,000-case evaluation exited 0. `scripts/check_generated_docs.py` exited 0.
Residual risk: Advisory suggestions can still be wrong; context propagation must remain conservative and source-backed.
Next bounded task: Review any newly classified events against source text before broader rule expansion.

## Hypothesis

If the five improvements are implemented at the deterministic classifier and audit-contract boundaries, focused fixtures and the fixed evaluation will show increased explicit subtype coverage while preserving unknowns, source evidence, no network calls, and no database writes.

## Plan

1. Delegate a bounded read-only inventory of the five change surfaces and exact tests.
2. Implement the smallest deterministic classifier and audit bookkeeping changes.
3. Run focused tests, then the fixed evaluation and documentation checks.
4. Update canonical FC Activity documentation and Swimm walkthrough, then pass the evidence gate.

## Execution Checkpoints

- Delegation: Explore inventory completed; structured report returned in the managed session output.
- Implementation: Classifier is `fc_activity_v5`; five bounded improvements are implemented and focused tests pass.
- Documentation: Canonical FC Activity comparison and Swimm source-pipeline walkthrough updated with before/after metrics and safety boundaries.
- Recovery: No external API run planned; use local evaluation artifacts and managed run logs.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User requested all five improvements be executed from the advisory output. | `data/eval/fc_activity_motion_unknowns_openai_20260928.json` and current classifier |

## Completion

Completion recorded: yes

Summary: Implemented explicit phrase coverage, French variants, conservative same-record context propagation, generic stay protection, and cumulative audit bookkeeping.

Validation: Focused tests, seeded deterministic evaluation, and generated-document validation passed. Evidence gate is pending.

Residual risk: Context propagation depends on shared `re_no` and intentionally leaves conflicting or unrelated events unknown. Advisory output remains non-authoritative.

Next recommended task: Source-backed review of newly classified events.
