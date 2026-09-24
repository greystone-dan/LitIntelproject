# Task: Redesign About as an interactive architecture graph

Status: in-progress
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Replace the simplified six-category About map with an interactive graph that explains the real site architecture, pipeline, citation intelligence, live functions, research workflow, and evidence controls.

Why now: The current map reads as a simple line of six square categories and does not explain the actual system or reveal connected detail when users click.

Owner surface: `backend/pages/data_explorer.py` and focused UI/browser tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Current About canvas, authoritative Swimm architecture maps, live inventory endpoint, feature-tab tests, local browser validation.

Risk boundary: UI-only. Preserve live metrics, tab behavior, APIs, provenance and offset invariants, and unrelated worktree changes. No database or backend contract changes.

Smallest falsifiable check: Browser-rendered About shows a layered graph with branching and loop connections; clicking a graph node expands connected sub-panels with relevant detail and metrics without horizontal overflow.

Acceptance criteria:

- Graph nodes represent actual site concepts rather than arbitrary six categories.
- Central graph explains sources/staging, canonical library, seven processing stages, citation resolution, services, research surfaces, and evidence controls.
- Clicking nodes expands connected panels with plain-language explanations, inputs/outputs, metrics, routes or verification rules as appropriate.
- Citation extraction and target resolution remain visibly separate; citations, statutes, metadata, tags, chunks, and embeddings remain separate layers.
- Existing live inventory and About tab behavior remain intact.
- Keyboard access, responsive layout, reduced motion, focused tests, diagnostics, and browser interaction checks pass.

Hypothesis: If the About surface presents the actual architecture as a layered graph with expandable connected panels, visitors will understand how the site works and why its evidence is trustworthy better than they do from a six-category linear map.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, relevant `.swm/` walkthroughs.

Rollback/recovery: Restore the prior About graph markup, styles, scripts, tests, and documentation; no data rollback is needed.

Evidence: Delegated Explore inspection found the real flow in `.swm/system-map.ovnldklv.sw.md`, `.swm/overview.uhwv0wj2.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, and `.swm/fc-ingest-source-pipeline.sw.md`. No files changed by delegation.

Evidence: Explore delegation inspected the current page and authoritative runtime/chart walkthroughs and recommended a layered graph with source, processing, resolution, service, and research subgraphs. Implemented 11 real architecture nodes, SVG branch/loop routes, connected-node highlighting, expandable detail panels, live inputs/outputs/signals, responsive positioning, and reduced-motion behavior in `backend/pages/data_explorer.py`. Updated `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/overview.uhwv0wj2.sw.md`, and `.swm/6.maiixtsw.sw.md`. An unrelated untracked task file `.github/project-manager/tasks/upgrade-about-system-map-interactive-graph.md` was preserved and not staged.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests; `get_errors` reported no errors for touched Python files; `git diff --check` passed. Playwright against the refreshed local API passed at 1280x900 and 390x844 for HTTP 200, 11 nodes, branch routes, Sources and Pipeline expansion, connected states, visible expansion panels, and no horizontal overflow. Reduced-motion Playwright check passed with graph route animation duration `0s`.

Residual risk: The graph is intentionally explanatory and uses live inventory counters already owned by the About shell; it does not make the underlying backend pipeline itself interactive. The canonical Site Architecture tab remains the deeper reference.

Status: complete
