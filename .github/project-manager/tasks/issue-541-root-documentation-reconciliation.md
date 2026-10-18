# Task: Reconcile root documentation with current main

Status: complete
Created: 2026-10-17
Updated: 2026-10-17

## Task Record

Task: Reconcile issue #541's named root documentation with current implementation; archive or remove stale material and correct the documentation index.

Why now: Stale operating claims, historical root documents, and unclear document status undermine trust in the current system reference and repository entrypoint.

Owner surface: Root documentation and documentation authority (`DOCS_INDEX.md`).

Commit allowed: yes

Push allowed: yes

Dependencies: Current implementation and generated API/schema/script references; relevant Swimm governance walkthrough.

Risk boundary: Documentation-only. Do not modify `CLAUDE.md`, generated docs manually, `backend/`, code, database, or `.env`; preserve unrelated worktree changes and source-history links.

Smallest falsifiable check: Verify the 11 replacement links resolve, preserve all pre-marker SYSTEM_REFERENCE content, and pass `git diff --check`.

Acceptance criteria:

- The named root documents are audited against current implementation and evidence; stale claims are corrected, archived, or removed with incoming links handled.
- README current focus and any corpus counts are accurately scoped and evidence-backed rather than presented as timeless inventory.
- `DOCS_INDEX.md` lists and classifies every remaining audited root document; links resolve.
- The root statute test is moved under `tests/` only if it is a genuine runnable test; otherwise it is deleted with evidence.
- Relevant canonical repository documentation and Swimm walkthrough are updated in the same checkpoint.
- Generated documentation check, local-link review, `git diff --check`, changed-file secret scan, and `parallel_validation` are run and results recorded.

Harness criteria:
- All audited root docs have an evidence-backed current/historical/obsolete disposition and index status.
- No forbidden implementation/generated/secrets files are changed.
- Focused documentation validation passes, with any broader validation limitation stated.

Docs/generated references: `DOCS_INDEX.md`; `SYSTEM_REFERENCE.md`; `.swm/11.nf15c1hd.sw.md`; generated docs are sources for live route/table/script facts and must not be edited.

Rollback/recovery: Revert only this task's documentation and archive moves if validation or link review fails; preserve unrelated worktree changes.

Evidence: Initial authority review completed: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.github/project-manager/TASK_TEMPLATE.md`, `.github/project-manager/README.md`, and `.swm/11.nf15c1hd.sw.md` read. In the parent session, `engine-tools-report_progress` was called before edits; it returned no changes to commit and posted the checklist. A managed worker returned the required structured audit. The parent session independently fetched and compared main: `origin/main=e06c35b` (PR #545), this branch is based on `4e70169`, and the only main delta is `backend/pages/coming_soon_examples.json` plus `backend/pages/roadmap_page.py`. README includes the issue-provided approximate, date-scoped figure and FC/SCC/FCA focus without claiming database verification. SYSTEM_REFERENCE's 11 appendix bodies were replaced with source links while preserving all pre-marker material except the handbook pointer wording; size fell from 553,191 to 169,642 bytes. The user explicitly authorized this output-only trim and accepted the helper overwrite risk. Parent-session validation is recorded below.

Files changed: `.swm/11.nf15c1hd.sw.md`, `.swm/future-state.north-star.sw.md`, `CHANGELOG.md`, `DOCS_INDEX.md`, `LEGAL_TAGGING.md`, `MASTER_IDEAS.md`, `OVERNIGHT.md`, `README.md`, `ROADMAP.md`, `SETUP.md`, `SYSTEM_REFERENCE.md`, `docs/history/README.md`, `docs/history/PROJECT_NOTES.md`; moved `GUIDANCE.md`, `STYLING_REFERENCE.md`, `SYSTEM_FOCUS_MODE.md`, `TAGGING_IMPROVEMENTS.md`, and `gold-set-expansion-findings.md` to `docs/history/`; deleted the non-genuine root `test_statute_integration.py`; task record.
Delegated work: Managed worker audited the named root docs and current source, reconciled the docs/index and archives, and returned structured findings. Manager acceptance found stale incoming links to moved `GUIDANCE.md` and an outdated archive inventory; manager fixed those in `.swm/future-state.north-star.sw.md`, `docs/history/PROJECT_NOTES.md`, and `docs/history/README.md`.
Focused validation: Earlier `python scripts/check_generated_docs.py` failed because its API/schema generators could not import `fastapi` and `sqlalchemy`; per user direction it was not rerun. Focused pytest could not start because `pytest` is absent. The stdlib README route check passed (16 paths covered by 239 checked-in generated routes). Current local-link review and `git diff --check` passed; all 11 replacement links resolve, and the preservation check confirms all pre-marker System Reference content is unchanged except the handbook pointer wording. Per user report, parent-session `parallel_validation` ran; code review reported no findings but its review backend was unavailable, CodeQL was skipped as trivial, and the secret scan passed. No further tests were run, per user direction.
Residual risk: Running the unchanged `scripts/embed_documentation_appendices.py` will restore the full appendix bodies; this output-only overwrite risk is accepted as requested. Generated API/schema/script freshness was not established because the earlier check lacked dependencies. The V3 activation contradiction remains documented and unchanged.
Next bounded task: If desired, create a separate scoped change to make the appendix helper emit links instead of full copies.

## Hypothesis

If copied appendix bodies are replaced by links, the pre-marker system reference remains intact, every source link resolves, and the hand-written reference becomes materially smaller without touching generated outputs.

## Plan

1. Verify the documentation authority and existing worktree boundary.
2. Delegate the bounded root-doc audit, archive/test disposition, and same-checkpoint canonical/Swimm edits.
3. Validate links and diff integrity; record parent-session review evidence and the accepted helper overwrite risk.

## Execution Checkpoints

- Delegation: Managed worker completed the bounded documentation audit; manager performed final link/archive corrections.
- Implementation: Root docs reconciled; five historical files moved, one invalid root test deleted, README clarified, and the 11 duplicated SYSTEM_REFERENCE appendices replaced by source links; no code or generated outputs changed.
- Documentation: Updated `DOCS_INDEX.md`, `SYSTEM_REFERENCE.md`, `docs/history/README.md`, `.swm/11.nf15c1hd.sw.md`, and the `.swm/future-state` link to the moved authority.
- Recovery: No data or runtime operation. The helper overwrite risk is documented; the helper was not run or modified.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-17 | Keep scope to documentation governance and named audited files | User explicitly restricts changes to documentation/test-file disposition and prohibits code/generated-doc edits | Issue #541 request and repository guardrails |
| 2026-10-17 | Report checklist before edits through parent-session progress tool | The parent-session call returned no changes to commit but posted the checklist | Parent-session report_progress result |
| 2026-10-17 | Use an output-only SYSTEM_REFERENCE appendix trim; leave helper unchanged | User explicitly chose the docs-only result and accepted that the helper can restore copied appendices | User follow-up; `scripts/embed_documentation_appendices.py:8-20,43-57` |
| 2026-10-17 | Record latest-main comparison as independently verified in parent session | Parent session fetched `origin/main=e06c35b`, confirmed branch base `4e70169` and the two-file main delta; manager did not merge | Parent-session Git/fetch comparison |

## Completion

Completion recorded: yes

Summary: README now has the requested issue-provided corpus snapshot and focus. SYSTEM_REFERENCE retains its unique pre-marker content and links to the 11 canonical/generated companion sources instead of duplicating their bodies.

Validation: `git diff --check`, changed-Markdown local-link review, README route-coverage assertion, and preservation check for all pre-marker System Reference content passed. All 11 replacement links resolve. The earlier generated-doc check and pytest limitations remain recorded; the checker was not rerun per user direction. Parent session: `parallel_validation` ran; code review reported no findings but its review backend was unavailable; CodeQL was skipped as trivial; secret scan passed.

Residual risk: Running the unchanged appendix helper will re-embed full copies. Generated-reference freshness was not independently confirmed; main comparison is complete per user-provided refs/delta; V3 profile activation conflict remains unresolved.

Next recommended task: Consider a separate scoped update to make the appendix helper generate links rather than full copies.
