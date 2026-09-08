# Anchor-Aware Short-Form Recovery Audit

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Recover legitimate historical short-form case-citation occurrences only when the current source decision contains a direct, identifier-bearing full anchor for the same alias.

Why now: The repaired extractor restores many legitimate short forms, but the paused refresh still loses some historical rows. The user requires recovery with valid anchors, not silent suppression or short-to-short chaining.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Current canonical case text, preserved baseline/comparison artifacts under `data/overnight_runs/citation-extraction-all-20260907`, focused citation tests, and the later controlled rebuild.

Risk boundary: Do not write citations, resume the all-case rebuild, resolve targets, or compute metrics. Preserve each occurrence's source text and offsets. Reject generic/ambiguous aliases and never create an anchor from a bare name, prior short form, or historical anchor alone.

Smallest falsifiable check: A read-only audit of cases 549, 615, 502, and 493 identifies historical short occurrences whose exact source spans are present and whose aliases match a current direct identifier-bearing anchor; it rejects `Agency` and other generic aliases.

Acceptance criteria:

- The recovery matcher accepts only direct current `case` anchors, or compatibility `case_name` anchors containing a reported citation.
- A recovered occurrence preserves its current canonical source span and is associated with a direct same-document full anchor.
- Generic or ambiguous aliases are rejected rather than treated as recovered case citations.
- No target-resolution, metric, or citation-table writes occur.
- Exact-span focused citation tests pass.
- `SYSTEM_REFERENCE.md` and `.swm/4.9nn3id9f.sw.md` document the recovery gate and evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`. Generated references are not affected.

Rollback/recovery: The initial audit is read-only. Revert the localized recovery matcher if its focused tests fail; retain the paused-run baseline and comparison artifacts unchanged. A future writer requires separate approval and a bounded cohort.

Evidence: Delegated bounded read-only inventory compared preserved baseline rows, current extraction, source text, and chunks for cases 549, 615, 502, and 493. All 1,134 missing historical short occurrences were textually present, but only four had a qualifying current full anchor: three `Miele` and one generic `hospital` occurrence in case 549. The local diagnosis showed that `Miele v Humber River Regional Hospital, 2007 CanLII 27757 (ONSC)` was a current full `case` row, but its CanLII suffix was not eligible for alias derivation. The repair permits only a full `case` row with a parsed CanLII identifier to derive aliases, retaining direct source offsets and anchor span. It also rejects generic bare aliases `Agency`, `Canadian`, and `hospital`. Read-only post-repair audit: case 549 `short_count=97`, `Miele=3`; case 615 `short_count=51`, no `Canadian`; case 502 `short_count=8`; case 493 `short_count=4`, no `Agency`. No citations, targets, metrics, run state, or baseline artifacts were written. Focused regression: `python -m pytest tests\\test_citations.py -k canlii_case_as_short_form_anchor -q` -> `1 passed, 136 deselected, 1 warning`. Final focused suite: `python -m pytest tests\\test_citations.py -q` -> `137 passed, 1 warning`. Editor diagnostics for `backend/citations.py` and `tests/test_citations.py` found no errors; `git diff --check` found no whitespace errors. Canonical documentation updated: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`; Swimm walkthrough updated: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If a historic short occurrence remains at an exact canonical source span and its alias has exactly one current same-document identifier-bearing full anchor, a conservative matcher can recover it without accepting generic aliases or short-to-short provenance.

## Plan

1. Audit representative historical occurrences against current text and current full anchors without writes.
2. Add a small pure recovery-matcher helper with positive, negative, and exact-span tests.
3. Re-run the audit using the helper and update the citation documentation/Swimm checkpoint.

## Execution Checkpoints

- Delegation: Bounded read-only representative-case inventory; no manager records or source edits by delegate.
- Implementation: `backend/citations.py` and `tests/test_citations.py`; focused `python -m pytest tests/test_citations.py -q`.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: Read-only report only; `data/overnight_runs/citation-extraction-all-20260907` remains paused-run authority.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Start read-only recovery audit | Legitimate historical occurrences must gain valid current full anchors before any rebuild resumes. | Task 076 cohort comparison and user direction. |

## Completion

Completion recorded: yes

Summary: Identifier-bearing full CanLII cases can now directly anchor conservative same-document short forms; generic bare aliases are rejected.

Validation: `python -m pytest tests\\test_citations.py -q` -> `137 passed, 1 warning`.

Residual risk: Reporter-only styles such as Markevich/Morneault remain unanchored and require a separately tested full-anchor recognizer; this task does not promote bare `case_name` spans.

Next recommended task: Repair the Windows atomic state-write failure and run a fresh bounded controlled rebuild cohort before considering the paused all-case run.