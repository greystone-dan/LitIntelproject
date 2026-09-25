# Task: Stabilize Citation Intelligence UI

Status: complete
Updated: 2026-09-25
Evidence: Delegated read-only Explore audit inspected `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`; it identified chained Citation Intelligence loader wrappers and generic error handling as the likely reliability risks and changed no files. Implementation changed `backend/pages/data_explorer.py` to compose the selected-authority Overview, expose Timeline/Neighborhood/Evidence paths, isolate enrichment with explicit loading/error states, and prevent duplicate neighborhood binding; `tests/test_feature_tabs.py` now covers the paths and states. Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 24 tests; `git diff --check` passed. Refreshed local app with `scripts\\refresh_site.ps1`; bounded Playwright checks at 1280x900 and 390x844 returned HTTP 200, no page errors, no responses >=400, no horizontal overflow, Timeline 5 years, Neighborhood 20 rows, Evidence 25 rows; after a bounded 20-second settle wait, mobile Overview showed fingerprint 1, authority-signals section 1, signal rows 4, and actions 3. Canonical documentation updated at `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated at `.swm/8.upryk5h6.sw.md`.
- Delegation: Explore completed a read-only bounded audit; no files changed. It returned the required structured report and recommended consolidating the wrapper chain.
- Delegated report:
	- Files inspected: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`
	- Files changed: None
	- Commands run: None; live browser execution was unavailable to the delegate
	- Results: Chained Citation Intelligence view wrappers and generic error handling were the main local reliability risks.
	- Failures: No runtime audit was run by the delegate because server availability was unknown.
	- Uncertainty: Case `24696` availability and live neighborhood/signal timing were not verified by the delegate.
	- Recommendation: Consolidate view orchestration and add explicit error/empty states.
- Implementation: Completed in `backend/pages/data_explorer.py`; regression coverage added in `tests/test_feature_tabs.py`.
- Documentation: Completed in `docs/RESEARCH_UI_GUIDE.md` and `.swm/8.upryk5h6.sw.md`.
Completion recorded: yes
Summary: Citation Intelligence now presents one selected-authority Overview with explicit research paths, stable partial-result handling, and the existing evidence-backed subviews remain navigable and traceable.
Validation: `24 passed`; `git diff --check` passed; refreshed-app Playwright checks passed at desktop and mobile sizes with clean requests, no page errors, no overflow, and settled Overview enrichment.
Residual risk: The generated page remains a large single-file HTML/JavaScript surface, and enrichment latency can leave the explicit loading state visible for several seconds on a cold local API. No API or database contract was changed.
Next recommended task: Add a small browser smoke test to the repository so the selected-case Overview settlement and subview transitions run automatically rather than only through bounded local Playwright checks.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Citation Intelligence APIs in `backend/citation_map.py` and `backend/routes.py`; live local app on port 8001 for bounded browser verification.

Risk boundary: UI-only refinement. Preserve backend-owned citation provenance, offsets, chunk IDs, target IDs, unresolved states, analytical-signal labels, existing routes, and the separation between stored evidence and derived analytics. No database writes, migration, production, security, or paid operations.

Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q`, followed by a bounded Playwright check of `/data-explorer?tab=citation-intelligence&case_id=24696` at desktop and mobile sizes.

Acceptance criteria:

- The selected case context and the current Citation Intelligence purpose are visible without relying on hidden or stale content.
- Overview presents the existing footprint, timeline, neighborhood, authority signals, and evidence paths in a clear hierarchy, with stored evidence versus derived research signals labeled.
- Loading, empty, and API failure states are explicit and cannot be overwritten by stale placeholders or duplicate loader races.
- Existing subtabs and reader click-through continue to expose their results once, including timeline filtering, neighborhood rows, authority signals, and evidence.
- Focused tests and bounded browser checks pass without page errors, failed requests, or mobile horizontal overflow.
- Canonical UI guidance and the relevant Swimm walkthrough describe the stabilized Citation Intelligence workflow.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`; generated API/schema references unchanged unless source contracts change.

Rollback/recovery: Revert only the task-scoped UI, test, and documentation edits. No database or long-running state is changed. If browser validation finds an initialization regression, restore the prior loader path and rerun the focused test.

Evidence: Pending. Record delegated audit, files changed, commands actually run, focused results, canonical documentation path, Swimm walkthrough path, known failures, and residual risk.

## Hypothesis

If Citation Intelligence uses one explicit selected-case context, a stable overview hierarchy, and centralized result-state handling, then the focused UI contract plus bounded desktop/mobile browser check will show each intended result exactly once without initialization errors or hidden stale placeholders.

## Plan

1. Delegate a bounded audit of the current renderer, loader orchestration, tests, and live page behavior.
2. Implement the smallest coherent UI/state refinement in the owning page builder and add regression assertions.
3. Run focused validation immediately, repair local failures, then update canonical UI guidance and the Swimm walkthrough.
4. Run final focused tests, diff hygiene, and bounded desktop/mobile browser validation.

## Execution Checkpoints

- Delegation: Pending bounded audit by Explore; required structured return recorded below.
- Implementation: Pending; owner is `backend/pages/data_explorer.py` with `tests/test_feature_tabs.py`.
- Documentation: Pending; update `docs/RESEARCH_UI_GUIDE.md` and `.swm/8.upryk5h6.sw.md`.
- Recovery: No long-running operation or database state involved.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Task created | User reports unclear, awkward, partially missing Citation Intelligence results; current implementation is concentrated in one page builder and has focused tests. | `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, `tests/test_feature_tabs.py` |

## Completion

Completion recorded: no

Summary: Pending implementation and validation.

Validation: Pending.

Residual risk: Pending live browser audit and implementation.

Next recommended task: Pending final acceptance; likely follow-up is a separate accessibility or performance pass if residual issues remain.
