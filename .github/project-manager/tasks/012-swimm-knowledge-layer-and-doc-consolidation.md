# Task: Establish Swimm Knowledge Layer and Consolidate Docs

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Populate the three new Swimm knowledge documents and then reduce Markdown duplication through explicit authority boundaries.
Why now: The project has strong documentation but too many overlapping sources, while strategic debt, design rationale, and evaluation decisions are not yet centralized.
Owner surface: `.swm/` knowledge layer and documentation authority map
Dependencies: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `ROADMAP.md`, `MASTER_IDEAS.md`, existing Swimm walkthroughs
Risk boundary: Do not delete or broadly rewrite documents in the first pass; preserve generated references, operational runbooks, repository instructions, and historical records.
Smallest falsifiable check: Each new Swimm document contains a clear scope, authority boundary, and links to the existing source material it consolidates.
Acceptance criteria: Three Swimm docs are populated; consolidation rules are documented; later cleanup can identify canonical, pointer, generated, operational, and historical Markdown without ambiguity.
Docs/generated references: Three new `.swm` docs, `DOCS_INDEX.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`.
Rollback/recovery: Revert only the new Swimm content and authority-map edits; preserve existing source documents until replacement coverage is verified.
Evidence: Populated the Swimm technical-debt register, architecture-decision index, and evaluation/quality-metrics framework. Updated `DOCS_INDEX.md` with explicit documentation ownership and consolidation rules, corrected the stale eight-tab workflow wording, and updated the Swimm transition map. Structural content checks and `git diff --check` passed. No existing Markdown files were deleted or renamed.
