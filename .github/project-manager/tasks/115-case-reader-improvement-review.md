# Task: Case reader improvement review

Status: deferred
Created: 2026-09-18
Updated: 2026-09-18

Task: Deep-dive the active Data Explorer case reader and implement the highest-value bounded improvement that makes its information easier to understand and use.
Why now: The reader contains metadata, evidence, intelligence, activity, tags, statutes, precedents, and linked authorities, but the information hierarchy and repeated interaction layers may obscure the primary research workflow.
Owner surface: Active case-reader presentation in `backend/pages/data_explorer.py`, with focused UI tests and browser validation.
Dependencies: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, relevant Swimm reader walkthrough, `tests/test_feature_tabs.py`, `scripts/browser_smoke.py`.
Risk boundary: Reader presentation and navigation only. Preserve extraction, stored evidence rows, offsets, API payloads, provenance, highlight semantics, and legacy routes.
Smallest falsifiable check: A focused browser check demonstrates the primary evidence workflow is easier to scan or navigate without changing rendered evidence counts or stored payload contracts.
Acceptance criteria:
- Review identifies and ranks concrete reader usability improvements by value, cost, risk, and maintainability.
- One bounded high-value improvement is implemented in the active reader.
- Existing evidence and reader behavior remain intact.
- Focused tests and browser validation pass.
- Canonical documentation and relevant Swimm walkthrough record the change.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert only task-owned reader source, tests, documentation, and task record changes.
Commit allowed: yes
Push allowed: yes
Evidence:
Hypothesis: The active reader can become more useful through a presentation-layer improvement that clarifies the primary evidence workflow without changing backend evidence contracts.
Evidence: User requested rollback because the accessibility step did not improve the reader experience. Removed the task-owned tab roles/navigation, browser assertions, and documentation additions. Earlier Acts / Regs and Tags grouping work remains intact. Focused rollback validation is pending.
