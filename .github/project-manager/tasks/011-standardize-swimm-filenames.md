# Task: Standardize Swimm Filenames

Status: deferred
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Rename opaque `.swm` walkthrough filenames to consistent lowercase kebab-case names and update repository references.
Why now: Human-readable titles improved the explorer labels, but opaque filenames still make links and maintenance harder to understand.
Owner surface: `.swm/*.sw.md` filenames and repository references
Dependencies: Swimm walkthrough links, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, repository-local references
Risk boundary: Preserve document content, YAML titles, Swimm metadata, and walkthrough identity as far as the repository format permits; do not rename unrelated files.
Smallest falsifiable check: Confirm every old filename has no remaining repository reference and every new filename exists with valid Swimm frontmatter.
Acceptance criteria: All selected Swimm filenames use lowercase kebab-case descriptive names; all tracked repository references are updated; no old filenames remain in repository text.
Docs/generated references: `.swm/*.sw.md`, repository Markdown references.
Rollback/recovery: Use the recorded old-to-new rename map in Git to restore filenames and references if Swimm link resolution regresses.
Evidence: Filename search and rename execution were deferred at the user's request before any filenames or repository references were changed.
