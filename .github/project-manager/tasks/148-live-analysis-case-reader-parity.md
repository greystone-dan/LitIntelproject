# Task: Integrate current Case Reader capabilities into Live Analysis

Status: complete
Created: 2026-09-29
Updated: 2026-09-30

## Task Record

Task: Bring the active inline Case Reader's applicable current evidence, navigation, and reading improvements into the ephemeral `/live-analysis` workflow.

Why now: Live Analysis is an active prototype for uploaded DOCX/text-PDF review, but its reader experience has not received the improvements made to the active Case Reader since its last pass.

Owner surface: `backend/pages/live_analysis.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/live_analysis.py`, live-analysis routes, `backend/pages/data_explorer.py`, existing live-analysis tests, browser evidence, `SYSTEM_REFERENCE.md`, and the relevant research-UI Swimm walkthrough.

Risk boundary: Uploaded material remains in memory only: no upload, case, chunk, citation, statute, metadata, or source write. Preserve backend-issued offsets and the separate case-citation/statute layers. Do not represent ephemeral local resolution as canonical database evidence or inferred citation treatment.

Smallest falsifiable check: Upload a supported fixture and verify that every newly reused reader control renders only from the live-analysis response and preserves citation/statute span alignment without an API or browser error.

Acceptance criteria:

- A documented parity matrix distinguishes applicable Case Reader improvements from inapplicable canonical-case features.
- Live Analysis receives every applicable, source-safe Case Reader reading and evidence interaction identified by the inventory, without persistence or invented offsets.
- Existing Live Analysis upload, citation, statute, and local-resolution behavior remains usable.
- Focused live-analysis tests, relevant feature-tab/UI checks, Python compilation, and a browser upload/read check pass.
- The canonical research UI documentation and relevant Swimm walkthrough describe the parity boundary and ephemeral-data constraints.

Harness criteria:

- Parity matrix and implemented boundary distinguish applicable reader features from canonical-only features.
- Live Analysis remains ephemeral and preserves backend-issued evidence offsets.
- Focused tests and browser validation pass.
- Canonical research UI documentation and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and the relevant `.swm/` research-UI walkthrough to be identified during the delegated inventory.

Rollback/recovery: Revert only the Live Analysis page and direct supporting contract changes. No stored data or migration is involved; uploaded bytes remain in memory for the request lifecycle.

Evidence: The read-only Explore inventory classified portable features as evidence tabs, counts, grouping, legend, hover previews, and offset scroll-back; canonical-only features remain excluded. Implemented the page-local parity slice using existing response fields. Updated `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, and `.swm/1.oi7rhqp2.sw.md` with the parity boundary and ephemeral constraints.

Files changed: `backend/pages/live_analysis.py`, `tests/test_live_analysis.py`, `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, `.swm/1.oi7rhqp2.sw.md`, plus the existing worktree changes included in the requested repository commit.
Delegated work: `Explore` completed a read-only inventory with no file changes. It returned the required feature matrix, identified existing backend-issued offsets and response fields, and recommended evidence tabs/grouping/legend as the smallest safe slice.
Focused validation: `pytest tests/test_live_analysis.py -q` passed with 7 tests; `pytest tests/test_feature_tabs.py -q` passed with 30 tests; the combined focused repository regression set passed with 117 tests; `python -m py_compile backend/pages/live_analysis.py` passed; Playwright upload/read validation against `http://127.0.0.1:8001/live-analysis` passed after verifying both tabs, statute grouping, counts, and one backend `data-start` row.
Residual risk: Live Analysis remains an ephemeral prototype and does not inherit canonical-only metadata, chunk mode, linked authority panes, assessment overlays, or graph analytics. Browser validation is bounded to the local refreshed server.
Next bounded task: None for this parity slice; next product work should be selected from `docs/STILL_TO_DO.md`.

## Hypothesis

If Live Analysis reuses only the Case Reader interactions supported by its existing ephemeral evidence payload, then an uploaded document can receive the current reader improvements without persistence, offset drift, or a claim of canonical authority.

## Plan

1. Delegate a read-only Live Analysis versus Case Reader feature and contract inventory.
2. Implement the smallest parity slice on the Live Analysis page and direct supporting contract only if required.
3. Run focused tests and browser upload/read validation, then update documentation and the Swimm walkthrough.

## Execution Checkpoints

- Delegation: `Explore` read-only parity inventory completed; no files changed by the worker.
- Implementation: `backend/pages/live_analysis.py` now provides separate evidence tabs, counts, response-field grouping, source links, and backend-offset scroll-back.
- Documentation: `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, and `.swm/1.oi7rhqp2.sw.md` updated in the same checkpoint.
- Recovery: No durable state. Revert page/contract changes; restart the local server only if browser validation requires it.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Start with the Live Analysis page as the single owner surface | It directly controls the ephemeral reader UI, while canonical case data must remain out of scope | `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, user request |

## Completion

Completion recorded: yes

Summary: Applied the applicable current Case Reader evidence interactions to the ephemeral Live Analysis reader without changing routes, schemas, persistence, or offset ownership.

Validation: Focused Live Analysis tests, shared feature-tab tests, Python compilation, local page contract, and final Playwright upload/read check passed.

Residual risk: Canonical-only Case Reader features remain intentionally unavailable for uploaded documents.

Next recommended task: Select the next bounded item from `docs/STILL_TO_DO.md`.