# Task: Integrate smart citation intelligence into the active research tabs

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Incorporate the highest-value existing citation intelligence into the active `/data-explorer` tabs without creating one tab per feature, centered on case fingerprints, similar-authority patterns, and where a case is cited across later decisions.

Why now: The backend already exposes citation-network analytics, but the primary site workflow still makes researchers leave the core search/reader path to discover those signals. The user wants a more intelligent site without interface bloat.

Owner surface: `backend/pages/data_explorer.py` active Data Explorer integration, with read-only supporting calls to existing citation analytics routes.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing citation-map analytics routes and serializers, canonical citation/target data, active Data Explorer tabs, focused API/UI tests, and browser smoke validation.

Risk boundary: Read-only presentation only. Do not infer citation treatment, legal authority, or controlling status; do not mutate citation/statute rows; preserve backend-owned offsets, provenance, unresolved states, and separate evidence layers; do not add a new top-level tab for each feature.

Smallest falsifiable check: A bounded browser run can open one case, render a compact fingerprint and citation-pattern view from existing routes, and expose at least one linked related-case or citing-decision path without page errors.

Acceptance criteria:

- Case Search or the inline reader exposes a compact case fingerprint using existing evidence layers.
- Citation Intelligence presents similar-authority/citation-cluster signals in an existing tab or subview.
- A selected case can show where it is cited in other decisions, with traceable case links and bounded results.
- The UI labels analytical signals as research aids and distinguishes stored evidence from derived pattern summaries.
- Focused backend/UI tests and a bounded desktop/mobile browser check pass.
- Canonical documentation and the relevant Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, generated API references only if route contracts change.

Rollback/recovery: Remove the new Data Explorer presentation and fetch calls; retain existing citation analytics routes and canonical data unchanged.

Evidence: Pending. Record delegated work, commands, observed results, artifacts, known failures, canonical documentation path, and Swimm walkthrough path.

## Hypothesis

If existing citation-network analytics are presented as a compact case fingerprint and authority-pattern view inside the current reader/Citation Intelligence workflow, then a researcher can move from a case to its related authorities and citing decisions without adding navigation bloat or making unsupported legal-treatment claims.

## Plan

1. Delegate a bounded contract/inventory check for existing routes and the smallest viable UI insertion points.
2. Implement one coherent citation-intelligence slice in the active Data Explorer tabs.
3. Run focused tests immediately, then validate the browser path at desktop and mobile sizes.
4. Update canonical documentation, Swimm, and this task record with evidence and residual risk.

## Execution Checkpoints

- Delegation: Completed bounded route/UI contract inventory; existing overview, evidence table, and similar-by-authority routes were selected.
- Implementation: Completed in `backend/pages/data_explorer.py`; added the retired Judge panel startup guard and direct Citation Intelligence initialization for URL-selected cases.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.
- Recovery: Remove the fingerprint wrapper/fetches and retain the existing analytics routes; no canonical data changed.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Keep the work inside existing tabs | The product goal is intelligence without interface bloat; the roadmap prioritizes discovery-to-reader-to-authority continuity. | `ROADMAP.md`, `docs/RESEARCH_UI_GUIDE.md` |

## Completion

Completion recorded: yes

Summary: The active Citation Intelligence Overview now exposes a bounded case fingerprint, stored citing decisions, and shared-authority navigation without adding a top-level tab.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 20 tests. Playwright at 1280x900 and 390x844 returned HTTP 200 with zero page errors, zero failed responses, one fingerprint, eight citing rows, six cluster rows, and no horizontal overflow. Clicking a citing row loaded a non-empty decision title in the inline reader.

Residual risk: The fingerprint is intentionally bounded to eight citing rows and six related cases; it does not classify citation treatment or provide a full graph. The shared-authority result depends on resolved canonical citation rows.

Next recommended task: Add a bounded visual timeline interaction inside the existing Timeline subtab using stored year-level citation evidence.
