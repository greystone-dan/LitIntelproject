# Task: Synchronize About and Site Architecture current-state pages

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Update the active About and Site Architecture pages so live inventory status and feature wording reflect the current product shell.

Why now: The visible Data explorer tab was removed, but page prose still names it and About coverage labels do not reflect populated live layers.

Owner surface: `backend/pages/data_explorer.py` plus the active UI documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: `/api/about/stats`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`.

Risk boundary: No database writes, schema changes, extraction changes, or changes to hidden compatibility routes.

Smallest falsifiable check: Load `/api/about/stats` and the page HTML, then verify all About coverage statuses are populated from live values and no visible Data explorer tab is present.

Acceptance criteria:

- About coverage status labels are derived from live counts.
- About and Site Architecture prose describe the current seven-tab shell.
- The guide and UI walkthrough no longer claim Data explorer is a visible top-level tab.
- Focused page and documentation validation passes.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`. No generated references are hand-edited.

Rollback/recovery: Revert only the focused page/documentation changes if the navigation contract is restored.

Evidence: Live `/api/about/stats` reports populated citation metrics, statute references, and case tags. The refreshed browser path requested `/api/about/stats` with HTTP 200 and rendered citation metrics `61,241`, statute references `751,944`, case tags `896,159`, and embeddings `0`; no visible Data explorer button remained. `py_compile` passed. Updated `docs/RESEARCH_UI_GUIDE.md` and `.swm/6.maiixtsw.sw.md` was verified to contain no stale Data explorer tab wording.

## Hypothesis

If About status labels are computed from the same live inventory payload used for counts, the page will no longer contradict the current database when displayed during a demo.

## Completion

Completion recorded: yes

Validation: `python -m py_compile backend/pages/data_explorer.py` passed; `/api/about/stats` returned HTTP 200; Playwright user-path validation loaded the About tab, confirmed live metric values, and found zero visible Data explorer buttons; `git diff --check` passed.

Residual risk: Final browser validation still reports the pre-existing `/analytics/judge-outcomes?min_decisions=100` 404 and a null-element page error in the broader initializer; neither affected the About stats request, live coverage values, or visible tab validation.

TODO / next task: Add a visible judge-coverage limitation and complete the separate post-2005 95% judge evaluation before making reliability claims in a management demo.
