# Versioned Legislation Future-Proofing

Status: backlog

Problem: Laws and regulations change after they are first indexed. The authority
library must preserve historical text and identity rather than silently replacing
an older instrument with the current version.

Required design questions:

- How are effective dates, in-force dates, repeal dates, and amendment dates
  represented for instruments and individual provisions?
- How are source snapshots, XML/PDF hashes, retrieval timestamps, and official
  publication versions linked to one authority version?
- When a case cites a provision, can resolution identify the version in force on
  the decision date, while still showing the current version for research?
- How are renumbered, repealed, or moved provisions mapped without changing the
  original extracted reference or historical target?
- How are bilingual versions kept aligned across amendments?
- How does the UI distinguish current law, historical law, and an unresolved
  version mismatch?
- What is the refresh process, including change detection, staged parsing,
  regression evaluation, approval, and rollback?

Acceptance direction: authority documents and provisions become immutable
versioned snapshots with explicit validity intervals and supersession links.
Existing statute occurrences retain their raw text, offsets, source hash, and
resolved version; refreshes create a new version rather than overwriting the old
one. Historical and current resolution must be separately queryable.

Trigger: before the authority library expands into recurring automated refreshes or
before provision-target foreign keys are added to a large corpus. Until then,
current-version resolution may be used as an explicitly provisional mode, but a
new source refresh must never silently re-resolve existing historical case
occurrences to the newest text.

Owner: statute authority library and resolver workstream, linked to
`.github/project-manager/tasks/041-statute-authority-resolution-strategy.md`.
