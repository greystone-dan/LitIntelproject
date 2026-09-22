# Task: Professional Case Search

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Redesign the active Data Explorer Case Search into a professional case-finder with useful typeahead suggestions, clearer controls and states, and a more scannable result list.

Why now: The current search surface exposes the underlying controls but still feels provisional: it gives no assistance while typing, result hierarchy is weak, and loading, empty, error, keyboard, and responsive behavior are not presented as one polished workflow.

Owner surface: `backend/pages/data_explorer.py` search markup, styles, and client behavior.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `/analytics/search/cases` response contract, `tests/test_feature_tabs.py`, focused API tests, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.

Risk boundary: Preserve existing control IDs, query parameters, endpoint semantics, result-to-reader navigation, seven-tab shell, and backend-owned evidence behavior. Suggestions must be bounded, debounced, abort stale requests, and never trigger full-text search. No schema, ingestion, canonical-data, security, or production changes.

Smallest falsifiable check: `& '.\\venv\\Scripts\\python.exe' -m pytest tests/test_feature_tabs.py -q`

Acceptance criteria:

- The primary query behaves as an accessible combobox with debounced title/citation suggestions, mouse and keyboard selection, Escape dismissal, and stale-request protection.
- Suggestions use the existing bounded case-search endpoint without full-text search and do not alter API semantics.
- Search, Clear, advanced-filter state, loading, empty, error, and result-count feedback are visibly distinct and screen-reader legible.
- Results prioritize title, citation, court, and date, then separate outcome/context and citation metrics into a compact, scannable layout with a clear open-decision action.
- Desktop and mobile browser checks pass without overflow, overlap, console errors, or uncontrolled suggestion requests.
- Focused UI tests, compilation, canonical UI documentation, and the active Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; no generated references expected.

Rollback/recovery: Revert only the search markup, style, client interaction, focused tests, and documentation in this task. The API and database remain unchanged.

Evidence:

- Files changed: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and this task record.
- Delegated work: Explore agent completed a bounded read-only audit of the owner, API contract, test surface, responsive/accessibility gaps, and three suggestion approaches. It changed no files and recommended bounded client-side suggestions through the existing endpoint.
- Focused validation: `& '.\\venv\\Scripts\\python.exe' -m pytest tests/test_feature_tabs.py -q` passed 16 tests after the implementation and again after the screenshot-driven visual repair.
- Compilation: `& '.\\venv\\Scripts\\python.exe' -m py_compile backend/pages/data_explorer.py` passed.
- Browser validation: Playwright at 1280x900 and 390x844 verified one completed debounced suggestion request for rapid `Vav` input with `limit=5`, `sort_by=relevance`, and no full-text flag; five visible suggestions; ArrowDown, Enter, Escape, Ctrl+K, Clear, advanced-filter state, Mason results, and inline-reader navigation; one-column mobile cards; no overlap or horizontal overflow; and no console/page errors.
- Visual inspection: desktop and mobile screenshots were reviewed. A missing theme-token alias that made the primary Search action invisible and generic panel overflow that clipped suggestions were corrected, then rechecked. The final desktop screenshot showed a dark readable Search cases action and all five bounded suggestions.
- Runtime: `scripts/refresh_site.ps1` refreshed the local API and Cloudflare tunnel; `/health` returned HTTP 200 during browser validation.
- Canonical documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `docs/RESEARCH_UI_GUIDE.md`.
- Swimm walkthrough: `.swm/6.maiixtsw.sw.md`.

## Hypothesis

If the existing bounded title/citation search is presented as a debounced accessible combobox and its results are reorganized around legal identity and explicit interaction states, focused browser checks will show reliable keyboard selection, bounded request behavior, readable mobile layout, and unchanged reader navigation.

## Plan

1. Establish the accessible search shell, interaction states, and professional result hierarchy.
2. Add bounded debounced suggestions with cancellation and keyboard control, preserving the existing endpoint contract.
3. Run focused tests immediately, then validate desktop/mobile behavior and update required documentation.

## Execution Checkpoints

- Delegation: Explore agent audited the current owner, API contract, tests, responsive/accessibility gaps, and three suggestion approaches; no files changed.
- Implementation: Completed in `backend/pages/data_explorer.py` with contract assertions in `tests/test_feature_tabs.py`.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.
- Recovery: No long-running or data-writing operation planned.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Use the existing bounded case-search endpoint for suggestions | Delivers immediate UX value without a new API or schema surface; debounce, cancellation, minimum query length, and a five-result limit bound cost | Delegated owner/API audit |
| 2026-09-22 | Keep advanced filters subordinate to the case-finder | Known-case lookup is the dominant interaction; existing filters and semantics remain available | Current search contract and user request |

## Completion

Completion recorded: yes

Summary: Case Search now behaves as a professional case-finder with bounded accessible suggestions, explicit interaction states, a clear result hierarchy, and preserved reader/filter contracts.

Validation: Focused tests, compilation, desktop/mobile Playwright workflows, request-bound checks, screenshot review, health check, and final diff validation.

Residual risk: Suggestions reuse the existing full case-search query and response rather than a dedicated lightweight endpoint. Debounce, cancellation, minimum query length, and five-result limits bound browser use, but server-side query cost should be measured before materially increasing traffic or corpus size.

Next recommended task: Add server-side search timing and request-count observability before considering a dedicated suggestion endpoint; do not widen this UI task into backend optimization without measured evidence.
