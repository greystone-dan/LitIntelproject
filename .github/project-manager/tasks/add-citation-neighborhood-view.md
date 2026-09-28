# Task: Add Citation Neighborhood View

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: Expose the selected case's direct citing and cited relationships inside Citation Intelligence.

Why now: The active workflow shows aggregates, evidence, clusters, and authority signals, but lacks a compact case-centered view of the immediate citation neighborhood.

Owner surface: `backend/pages/data_explorer.py` Citation Intelligence subview integration.

Commit allowed: yes
Push allowed: yes

Dependencies: Existing `/api/citation-intelligence/{case_id}/neighborhood` route and response contract.

Risk boundary: Read-only presentation. Preserve resolved/unresolved citation boundaries; do not infer treatment, legal similarity, or controlling status.

Smallest falsifiable check: A selected case can open the neighborhood subview, render direct related nodes, and open a related case in the active reader without page errors.

Acceptance criteria:
- Existing Citation Intelligence navigation exposes a compact Neighborhood view.
- Focus case, relationship direction, occurrence count, and linked case identity remain visible.
- Related-case click-through uses the active reader.
- Focused tests, browser validation, and canonical/Swimm documentation pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Remove the subview renderer and route call; preserve the existing citation routes and other views.

Evidence: Delegated inventory confirmed the neighborhood endpoint and response model are implemented and compatible with the active UI. The bounded subview now renders direct relationships and preserves related case click-through.

Hypothesis: A bounded direct-neighborhood view will make citation relationships inspectable without requiring a separate graph page or legal-treatment inference.

## Execution Checkpoints

- Delegation: Completed bounded contract inventory; no files changed by worker.
- Implementation: Completed in `backend/pages/data_explorer.py`; added the Neighborhood subview, bounded route call, direction/occurrence labels, reader links, and resilient asynchronous tab binding.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.

## Completion

Completion recorded: yes
Summary: Citation Intelligence now exposes a compact direct citation neighborhood without adding a top-level tab or changing backend data.
Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 23 tests. Playwright at 1280x900 and 390x844 returned HTTP 200 with no page errors, no failed responses, 20 neighborhood rows, active Neighborhood state, and no horizontal overflow. Desktop related-row click-through produced a non-empty decision title.
Residual risk: The view is bounded to 20 edges and depends on resolved citation graph rows; it does not classify legal similarity or treatment.
Next recommended task: Pause for human review before selecting the next citation-intelligence slice.
