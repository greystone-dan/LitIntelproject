# Task: Add statute consideration analytics

Status: planned
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add descriptive decision-level statistics and a research page for cases that reference an act section.

Why now: Issue #151 adds a traceable way to assess how an identified statutory provision appears in reported decisions without presenting the counts as legal advice.

Owner surface: Statute consideration analytics and its dedicated API/UI entry points.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing statute canonicalization/versioning, statute reference rows, case outcomes, reader routes, and statute viewer.

Risk boundary: Read-only descriptive analytics only; no schema/database/deployment changes, no external calls, preserve statute/case-reference separation, and keep route registration minimal.

Smallest falsifiable check: `python -m pytest -q tests/test_statute_consideration.py`

Acceptance criteria:

- The API reports distinct decisions referencing a provision, court/year counts, outcome counts with unclassified and denominator, and a paginated relevance-ranked list capped at 50 per page.
- Unknown sections return a clear 404 with a useful hint; the dedicated page accepts act and section and links results to the reader.
- The statute viewer links to consideration; fixture tests and concise feature documentation cover the behavior.
- Focused tests, generated-document check, and the CI-configured full test suite pass; generated API references are regenerated where needed.

Harness criteria: API analytics and pagination fixtures pass; UI/form/link fixtures pass; generated docs are current; CI-configured full suite passes.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md` (statute evidence layer) and `.swm/1.oi7rhqp2.sw.md` (API/UI ownership); generated API/schema/script references via documented generators.

Rollback/recovery: Revert the isolated new service/page and minimal route/viewer registrations; no persisted data or schema changes require recovery.

Evidence: Pending. Record delegated work, commands, observed results, artifacts, known failures, canonical documentation path, and Swimm walkthrough paths.

Files changed: None yet.
Delegated work: Pending assignment to managed-worker for bounded feature implementation, fixture tests, and feature documentation; manager retains task record, decision, and final validation.
Focused validation: Pending.
Residual risk: Existing reference/outcome data completeness may constrain descriptive counts.
Next bounded task: None until focused implementation check.

## Hypothesis

If decision-level aggregation is correctly derived from stored statute references and canonical cases, fixture/API tests will show correct distinct decision, court/year, outcome-denominator, stable ranking, pagination, and unknown-section behavior without schema changes.

## Plan

1. Assign the bounded implementation and focused fixture checks to a managed worker.
2. Review the returned change against the API/UI and descriptive-statistics requirements.
3. Regenerate generated references, run focused and CI-configured full tests, and update canonical and Swimm documentation.

## Execution Checkpoints

- Delegation: Pending managed-worker assignment and structured return.
- Implementation: Pending worker changes and focused check.
- Documentation: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md` and `.swm/1.oi7rhqp2.sw.md`.
- Recovery: No database or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Scope to read-only statute-reference analytics with no schema change | Issue requires descriptive statistics and existing statute storage | User request; `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md` |

## Completion

Completion recorded: no

Summary: Pending implementation.

Validation: Not run.

Residual risk: Pending.

Next recommended task: Pending.
