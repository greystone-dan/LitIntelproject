# Reporter-Only Short-Form Anchors

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Recognize complete reporter-only case citations as direct same-document anchors for legitimate later short forms.

Why now: The rebuild gate still has a known precision-preserving coverage gap: historical Markevich and Morneault short forms are present in source text but their reporter-only full citations remain compatibility `case_name` rows and cannot legally seed anchors.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Canonical source text for case 615, existing citation extraction tests, and the paused-run artifacts. Target resolution and the controlled runner are downstream and out of scope.

Risk boundary: Preserve direct identifier-bearing anchor provenance, exact source offsets, and generic-alias rejection. Do not promote bare names, write citation rows, resolve targets, or run/resume the rebuild.

Smallest falsifiable check: A full reporter-only citation in the observed source style produces a complete eligible anchor and a later `Markevich`/`Morneault` short form with exact occurrence and anchor spans.

Acceptance criteria:

- Reporter-only full citations are eligible only when they contain a verified volume, recognized reporter, optional series, and page identifier.
- Legitimate later short forms retain direct full anchor text and exact spans.
- Bare case names and generic aliases remain ineligible.
- Focused citation tests pass.
- `SYSTEM_REFERENCE.md` and `.swm/4.9nn3id9f.sw.md` record the updated anchor rule.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`; generated references are not affected.

Rollback/recovery: Revert the isolated reporter-only candidate rule if tests or the real-case audit expose an overmatch. Preserve paused baseline/comparison artifacts; no database state changes occur in this task.

Evidence: Delegated read-only audit of canonical case 615 found Markevich and Morneault as bare `case_name` rows despite complete reporter citations, and found a separate `Revenue` short false positive. The repair recognizes only plausible party names followed by a complete FTR/DLR reporter sequence with volume, optional series, and page; it consumes adjacent court, CanLII, and quoted declared-alias suffixes only in that reporter-only branch. It excludes parenthesized-year reporter forms from this rule so their existing compatibility classification remains unchanged, and adds `Revenue` to the generic bare-alias rejection set. Focused fixtures: `python -m pytest tests\\test_citations.py -k 'reporter_only_case_as_short_form_anchor or generic_revenue_alias or parenthesized_year_reporter' -q` -> `4 passed, 136 deselected, 1 warning`. Read-only case 615 audit -> two Markevich and three Morneault short rows, each anchored to an exact complete source span; zero `Revenue` short rows. Final focused suite: `python -m pytest tests\\test_citations.py -q` -> `140 passed, 1 warning`. Canonical documentation updated: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`; Swimm walkthrough updated: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If a case-name span is immediately followed by a complete recognized reporter citation, classifying that composite span as an identifier-bearing full anchor will recover later matching short forms without enabling bare-name or short-to-short anchors.

## Plan

1. Inspect the exact case 615 reporter-only citations and candidate classification.
2. Add the smallest reporter-composite recognition rule and exact-span positive/negative tests.
3. Run focused tests and a read-only representative audit, then update documentation.

## Execution Checkpoints

- Delegation: Read-only case 615 reporter-citation inventory with structured evidence.
- Implementation: `backend/citations.py`, `tests/test_citations.py`; focused `python -m pytest tests\\test_citations.py -q`.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: The paused rebuild remains stopped; no writer runs in this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Start reporter-only anchor repair | The bounded recovery audit found no qualifying Markevich/Morneault anchor despite verified historical occurrences. | Task 077 evidence. |

## Completion

Completion recorded: yes

Summary: Complete FTR/DLR reporter-only citations now provide direct same-document anchors for later short forms.

Validation: `python -m pytest tests\\test_citations.py -q` -> `140 passed, 1 warning`.

Residual risk: The narrow FTR/DLR rule does not cover every reporter series; additions require a separate exact-span evidence set.

Next recommended task: Repair the Windows controlled-runner state-write failure after this citation slice passes.