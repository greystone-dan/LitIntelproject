# Task: Align Acts / Regs with Citations

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

Task: Restyle and refine the Acts / Regs reader tab so its drill-down matches the Citations tab's grouping, disclosure, and occurrence presentation.
Why now: The current Acts / Regs tab is functionally nested but visually distinct and less coherent than the established Citations evidence pattern.
Owner surface: `backend/pages/data_explorer.py` grouped reader evidence rendering and styles.
Dependencies: Existing `groupedCitationHtml()`, `groupedStatuteHtml()`, `tests/test_feature_tabs.py`, browser smoke/live B010 reader validation.
Risk boundary: Acts / Regs reader presentation only. Preserve statute rows, source/section grouping semantics, offsets, provenance, citations, tags, and highlighting.
Smallest falsifiable check: B010 shows Acts / Regs source and section disclosures with the same visual classes/summary structure as Citations while retaining all 41 stored occurrences.
Acceptance criteria:
- Acts / Regs group summaries use the Citations visual language and occurrence-row structure.
- Source -> section -> occurrence drill-down remains intact.
- No stored statute rows or occurrence metadata are filtered or rewritten.
- Focused tests and browser validation pass.
- Canonical documentation and relevant Swimm walkthrough record the alignment.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert only task-owned Acts / Regs renderer/style, tests, documentation, and task record changes.
Commit allowed: yes
Push allowed: yes
Evidence:
Hypothesis: Reusing the Citations tab's disclosure and occurrence classes for statute groups will improve scanability without changing the statute evidence contract.
Delegated work: Explore compared `groupedCitationHtml()`, `groupedStatuteHtml()`, and the inline reader CSS; it identified the six statute classes as unstyled and recommended citation-parity rules.
Implementation: Added citation-matched CSS for statute summaries, source/section disclosures, nested containers, and occurrence rows. Grouping logic and all evidence fields remain unchanged.
Focused validation: `py_compile backend/pages/data_explorer.py` passed with the existing `\s` SyntaxWarning; `pytest tests/test_feature_tabs.py -q` passed (14 tests); direct Playwright validation against refreshed `http://127.0.0.1:8000/data-explorer?case_id=53516` confirmed 7 sources, 7 sections, 41 occurrences, matching 8px spacing, 16px group typography, 10px occurrence typography, and matching border colors between Acts / Regs and Citations. Final `git diff --check` pending.
Canonical documentation updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`. Swimm walkthrough updated: `.swm/8.upryk5h6.sw.md`.
Residual risk: This is a presentation-only parity change; visual behavior was checked on the B010 fixture, not every corpus variation.
Next bounded task: Review whether statute source labels should display instrument citations separately from document titles on cases with multiple source aliases.
