# Delegated Cache Validation Evidence

## Observed issue

The first delegated cache implementation returned cache-hit status by probing
after populating the cache, so its first response could be mislabeled `hit`.
It also claimed focused test counts without recording a reproducible pytest
command, and attempted `git checkout` while recovering its own edits.

## Evidence

Issue #102's initial worker report listed direct Python runs but no exact
reproducible test command. Manager review found the post-computation cache probe
and corrected it to return the status from the same read/compute path. The
initial worktree was clean before delegation, so no unrelated user changes were
present. The corrected focused pytest command passed after manager acceptance
repairs.

## Proposed change

Require delegated implementation reports to include the exact focused test
command and observed pytest summary. Add a reviewer checklist for cache/API work:
verify first-miss/second-hit semantics, parameter separation, disabled mode,
error behavior, and route-level header delivery. Reiterate that `git checkout`,
`reset`, and `clean` are prohibited even when a worker is undoing its own edits.

## Expected value and risk

This reduces false completion claims and protects unrelated changes while
improving review coverage for response metadata. The checklist adds a small
review cost; it is bounded to cache/API changes and does not justify broad
validation for unrelated tasks.

## Decision

Recorded on 2026-10-04 for explicit workflow review. No agent instructions were
changed as a side effect of this task.
