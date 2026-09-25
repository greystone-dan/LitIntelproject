# Task: Add case-level pipeline graphic to About

Status: in-progress
Created: 2026-09-25
Updated: 2026-09-25

Task: Add a second interactive graphic directly below the architecture graph explaining what happens to one case, including ordered processing stages, distinct derived layers, separate citation resolution, and unfinished work.

Why now: The architecture graph explains the site broadly, but users need a case-level view of the pipeline and visible honesty about incomplete quality gates.

Owner surface: `backend/pages/data_explorer.py` and focused UI/browser tests.

Commit allowed: yes
Push allowed: yes

Dependencies: `backend/case_processing.py`, `SYSTEM_REFERENCE.md`, relevant Swimm pipeline walkthroughs, current About graph, feature-tab tests.

Risk boundary: UI-only. Preserve existing architecture graph, live inventory, APIs, routes, offsets, provenance, and unrelated worktree changes.

Smallest falsifiable check: Browser renders the second pipeline graphic below the architecture graph; all ordered stages, distinct layers, and unfinished gates are visible; clicking a stage expands its details inside the pipeline graphic without horizontal overflow.

Acceptance criteria:
- Second graphic appears directly below the architecture graph.
- Shows input, full_case/heading/paragraph chunking, metadata, outcome, citations, statutes, tags_v3, distinct output layers, and separate target resolution.
- Clearly marks unfinished/deferred work, including short-form anchor quality, statute source indexing, and experimental discussion units.
- Stage selection expands detail within the pipeline canvas, not in a separate page section.
- Responsive, keyboard-accessible, reduced-motion aware, and covered by focused tests/browser validation.

Hypothesis: A case-level pipeline graphic with ordered stages, parallel evidence layers, and explicit unfinished gates will make the system's per-case behavior and current limits understandable without requiring users to read architecture documentation.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/overview.uhwv0wj2.sw.md`.

Rollback/recovery: Remove the second pipeline markup/styles/scripts/tests/docs; no data rollback required.

Evidence: Delegated Explore inspection found the canonical seven-stage order and deferred work from `backend/case_processing.py`, `SYSTEM_REFERENCE.md`, and the Swimm pipeline walkthroughs. No files changed by delegation.
