# Task: Clarify Swimm Explorer Names

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Replace vague Swimm explorer-tree titles with consistent, human-readable names.
Why now: Several walkthrough labels are generic even though the underlying documents cover distinct architecture, workflow, and operational domains.
Owner surface: `.swm/*.sw.md` YAML frontmatter titles
Dependencies: `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
Risk boundary: Change explorer labels only; preserve Swimm filenames, document links, content, and walkthrough identity.
Smallest falsifiable check: Extract all `.swm/*.sw.md` frontmatter titles and confirm every intended label is present after editing.
Acceptance criteria: Every active Swimm walkthrough has a concise title that identifies its domain or workflow at a glance; no filenames are renamed.
Docs/generated references: Swimm walkthrough frontmatter only.
Rollback/recovery: Revert the title-only changes if Swimm displays duplicate or broken labels.
Evidence: Updated YAML `title` frontmatter for 17 Swimm walkthroughs with domain-specific, human-readable explorer labels. Filenames and document links were preserved. Title extraction confirmed all intended labels, and `git diff --check` passed.
