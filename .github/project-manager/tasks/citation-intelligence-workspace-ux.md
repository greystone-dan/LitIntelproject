# Task: Citation Intelligence workspace UX

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Make Citation Intelligence a clear case-focused workspace with preserved navigation, a visual overview, and no orphaned search results when opening a case.

Why now: Users must scroll past stale Citation Intelligence search results after opening a case, and the current bottom subtab strip does not present the available evidence as a coherent page.

Owner surface: backend/pages/data_explorer.py

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Citation Intelligence APIs and active Data Explorer reader flow; no schema or database changes.

Risk boundary: Preserve backend-owned citation evidence, offsets, unresolved states, API contracts, read-only behavior, and the active /data-explorer workflow. Do not present derived signals as legal treatment or controlling status.

Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` plus a bounded browser check that opens Citation Intelligence, selects a case, and verifies the workspace header, overview visual, and cleared search results.

Acceptance criteria:

- Opening a Citation Intelligence result removes the stale search-results block from the visible reader path and leaves a clear return path.
- Citation Intelligence presents a page-like case workspace with persistent selected-authority context and secondary research navigation.
- Overview includes an accessible visual summary built only from stored counts, dates, and derived network metrics, with clear evidence/derived labeling.
- Existing Timeline, Neighborhood, and Evidence paths remain reachable and functional.
- Focused tests, browser validation, and documentation pass.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`; generated references unchanged.

Rollback/recovery: Revert the scoped UI/test/documentation commit; no data or migration rollback is required.

Evidence: Explore completed a read-only audit of the active Data Explorer shell and identified stale `#citationSearchResults` content as the scroll cause. Implemented the workspace hierarchy, stale-result clearing, and citation-footprint visual in `backend/pages/data_explorer.py`; added focused UI contract coverage in `tests/test_feature_tabs.py`. Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 25 tests; `git diff --check` passed. Website refresh started the local API on port 8001 and connected the Cloudflare tunnel. Bounded Playwright checks passed at 1280x900 and 390x844: HTTP 200, one overview visual, three research actions, correct navigation order, no page errors, no responses >=400, and no horizontal overflow. Canonical documentation updated at `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated at `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If the result container is cleared on case open and Citation Intelligence gains a persistent case workspace header with a visual overview, a focused browser check will show the reader without orphaned results and expose the available citation evidence without requiring a long scroll through unrelated content.

## Plan

1. Inspect the active shell, case-open flow, existing Citation Intelligence renderers, and nearby contract tests.
2. Implement the scoped navigation and overview visual changes in the active generated UI and add focused assertions.
3. Run focused tests and a bounded browser check, then update the canonical guide and Swimm walkthrough.

## Execution Checkpoints

- Delegation: Explore audit of the active UI and APIs; read-only, no files changed.
- Implementation: Pending; owner is `backend/pages/data_explorer.py` with focused tests.
- Documentation: Pending; update `docs/RESEARCH_UI_GUIDE.md` and `.swm/8.upryk5h6.sw.md`.
- Recovery: No long-running operation or database write.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Task created | User feedback identifies reader scroll friction, weak page hierarchy, and an unhelpful overview presentation. | Explore audit and active Data Explorer shell |

## Completion

Completion recorded: yes

Summary: Citation Intelligence now behaves as a case-focused workspace with secondary navigation above its results/content, clears stale Citation Intelligence results when opening the reader, and presents a source-grounded footprint visual with explicit derived-metric labeling.

Validation: 25 focused tests passed; diff check passed; bounded desktop/mobile browser validation passed after website refresh.

Residual risk: The generated HTML/JavaScript surface remains large and contains legacy compatibility wrappers. The visual uses existing overview API data and remains a derived navigation aid, not legal treatment or controlling-authority status.

Next recommended task: Consolidate the legacy Citation Intelligence loader wrappers after a separate regression plan and browser baseline are approved.
