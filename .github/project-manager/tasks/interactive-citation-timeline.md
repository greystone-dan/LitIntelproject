# Task: Make Citation Intelligence Timeline Interactive

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Let researchers click a citation timeline year and inspect the existing stored evidence table filtered to that year.

Why now: The active Citation Intelligence workflow has year-level citation counts, and the backend already supports year-filtered evidence. The next useful improvement is traceable drill-down without adding another tab or new analytics layer.

Owner surface: `backend/pages/data_explorer.py` timeline/evidence interaction.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `/api/citation-intelligence/{case_id}/timeline` and `/api/citation-intelligence/{case_id}/table` contracts.

Risk boundary: UI-only, read-only. No database writes, no citation-treatment inference, no changes to canonical citation rows or offsets.

Smallest falsifiable check: Clicking a rendered timeline year requests the existing evidence table with that year and renders the filtered evidence view without page errors.

Acceptance criteria:

- Timeline year rows are visibly actionable in the existing Timeline subtab.
- Selecting a year opens the existing evidence/table view with the year filter applied.
- The selected year can be cleared to return to the unfiltered evidence table.
- Focused UI tests and bounded desktop/mobile browser validation pass.
- Canonical documentation, Swimm, and this task record describe the traceable drill-down.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Remove the year state and row handlers; existing timeline and evidence requests remain available.

Evidence: Delegated inventory confirmed the timeline payload and table year parameter already exist. Implementation added the bounded UI drill-down and documentation checkpoint.

Hypothesis: If timeline years reuse the existing evidence-table route with a bounded `year` filter, researchers can follow temporal patterns into stored citation evidence without product surface expansion.

## Execution Checkpoints

- Delegation: Completed bounded route/UI contract inventory; no files changed by worker.
- Implementation: Completed in `backend/pages/data_explorer.py`; timeline years now open bounded year-filtered evidence using the existing route, with pagination and clear-filter behavior.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.
- Recovery: No long-running operation planned.

## Completion

Completion recorded: yes

Summary: Citation Intelligence Timeline years now drill into stored evidence without adding a new tab or backend contract.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 21 tests. Playwright at 1280x900 and 390x844 showed five year buttons, no page errors or failed responses, the expected `year=2014` table request, successful clear-filter restoration, and no horizontal overflow.

Residual risk: The timeline remains an aggregate navigation aid; it does not classify citation treatment or infer legal significance from yearly volume.

Next recommended task: Integrate the existing authority-signals response into the current Overview readout, keeping the explanation explicitly analytical and traceable.
