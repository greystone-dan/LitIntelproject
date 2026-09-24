# Task: Redesign About system map as a visual architecture canvas

Status: in-progress
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Replace the current disclosure-list system map with a visual, animated, audience-friendly architecture canvas inspired by high-level system architecture diagrams.

Why now: The current map explains the system but does not provide the visual overview or interactive sense of movement the About page needs.

Owner surface: `backend/pages/data_explorer.py` and focused UI/browser tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing About panel, current system-map content, shared generated CSS/JavaScript, feature-tab tests, and local browser validation.

Risk boundary: UI-only. Preserve live inventory metrics, Data Explorer tab behavior, routes, backend-owned evidence/provenance language, and unrelated worktree changes. No database, API, or production access changes.

Smallest falsifiable check: Browser-rendered About contains a visual node canvas with visible connections, animated flow state, clickable nodes that update an accessible detail panel, and no horizontal overflow on mobile.

Acceptance criteria:

- The map reads visually like a high-level architecture diagram rather than a stacked list.
- Major stages are represented by visually distinct nodes and directional connections.
- A subtle animated flow communicates movement through the system without distracting from reading.
- Clicking a node highlights it and updates a detail panel with plain-language explanation.
- A general audience can understand the site function without knowing repository terminology.
- Keyboard access, reduced-motion behavior, responsive layout, existing metrics, and other tabs remain intact.
- Focused tests, diagnostics, whitespace validation, and browser interaction checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`

Rollback/recovery: Restore the prior system-map markup/styles/scripts and focused assertions; no data rollback is needed.

Evidence: Existing map implementation and focused tests inspected. Explore delegation reviewed `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, and `docs/RESEARCH_UI_GUIDE.md`; it recommended a connected SVG/canvas treatment with mobile layout and animation. No files were changed by delegation.

## Hypothesis

If the About map uses a connected visual canvas with selectable nodes, a moving flow indicator, and a persistent plain-language detail panel, then general visitors will understand the system's purpose faster than they do from sequential disclosures while the existing architecture detail remains available on interaction.

## Plan

1. Delegate a bounded inspection of the current visual surface, script insertion points, and browser test approach.
2. Implement the visual canvas, animated flow, node selection state, detail panel, and accessible fallback.
3. Run focused tests immediately, then browser-check desktop/mobile interaction and reduced-motion behavior.
4. Update canonical UI documentation and the Active UI Swimm walkthrough.
5. Finalize evidence and commit/push the completed checkpoint.

## Execution Checkpoints

- Authority review: prior task documentation and active UI ownership reviewed.
- Delegation: Complete; bounded Explore report consumed.
- Implementation: Complete; visual SVG route, six selectable stations, shared detail panel, responsive layout, and reduced-motion CSS added in `backend/pages/data_explorer.py`; focused assertions updated in `tests/test_feature_tabs.py`.
- Documentation: Complete; updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.
- Recovery: No long-running or destructive operation planned.

## Completion

Completion recorded: yes

Summary: Replaced the disclosure-list system map with a connected visual architecture canvas while preserving live metrics, tab behavior, provenance language, and Site Architecture depth.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests; `get_errors` reported no errors for touched Python files; `git diff --check` passed. Playwright checks against the reloaded local API passed at 1280x900 and 390x844 for HTTP 200, six stage buttons, SVG routes, initial selection, enrichment interaction/detail update, and no horizontal overflow. Reduced-motion Playwright check passed with route animation duration `0s`.

Residual risk: A visual architecture canvas can become decorative rather than explanatory; node labels, plain-language detail, and the existing Site Architecture tab must remain the source of depth.

Next recommended task: Review the visual hierarchy with a general visitor and refine the most confusing node or connection.
