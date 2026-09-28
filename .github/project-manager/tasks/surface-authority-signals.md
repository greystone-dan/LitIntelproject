# Task: Surface Authority Signals in Citation Intelligence

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: Add a compact derived authority-signals summary to the existing Citation Intelligence Overview.

Why now: The backend already ranks authorities by occurrence, spread, surprise, and originality, but the active Overview only exposes broader fingerprint and cluster signals.

Owner surface: `backend/pages/data_explorer.py` Citation Intelligence Overview integration.

Dependencies: Existing `/citation-map/cases/{case_id}/authority-signals` route and response contract.

Risk boundary: Read-only presentation. Preserve backend-owned scores and contexts; do not infer legal treatment or mutate citation data.

Smallest falsifiable check: A selected case Overview renders a bounded authority-signals section and an authority link opens the inline reader without page errors.

Acceptance criteria:
- Existing Overview includes a compact authority-signals section.
- Derived metrics are explicitly labeled as analytical research aids.
- Authority links preserve case IDs and open the active reader.
- Focused tests, desktop/mobile browser validation, and documentation pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Remove the additional authority-signals fetch/render block; retain existing route and reader behavior.

Evidence: Delegated inventory confirmed the route is bounded and the reader already has a compatible authority-row rendering pattern. The Overview now renders four bounded signal rows from the existing route.

Hypothesis: A small ranked authority-signals card in the existing fingerprint will expose where a case's citation use is concentrated or distinctive without adding navigation bloat.

## Execution Checkpoints

- Delegation: Completed bounded contract inventory; no files changed by worker.
- Implementation: Completed in `backend/pages/data_explorer.py`; added a compact authority-signals section to the existing Overview and removed a redundant startup loader that could duplicate enrichment.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.

## Completion

Completion recorded: yes
Summary: Citation Intelligence Overview now exposes bounded distinctive-authority signals without adding a tab or changing citation data.
Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 22 tests. Playwright at 1280x900 and 390x844 rendered one authority-signals section with four rows, one fingerprint, and six cluster rows; no page errors, failed responses, or horizontal overflow. A deterministic loader check confirmed signal-row click-through to a decision title.
Residual risk: Surprise/originality scores are derived navigation signals and must not be presented as legal importance. The card is bounded to four authorities and depends on resolved citation data.
Next recommended task: Pause for human review; the next product slice can be selected after connectivity returns.
