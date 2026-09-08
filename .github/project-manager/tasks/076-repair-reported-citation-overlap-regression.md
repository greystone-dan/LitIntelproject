# Repair Reported Citation Overlap Regression

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Restore complete identifier-bearing reported citations that are downgraded or truncated in full-document extraction, while preserving valid same-name short-form occurrences at distinct offsets.

Why now: The paused total citation refresh exposed valid external reported citations in canonical full text that are extracted completely in isolation but reduced to `case_name` or `case_short` forms in full-document context. Missing full anchors can suppress legitimate short forms.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/case_processing.py`, focused citation tests, paused state/baseline under `data/overnight_runs/citation-extraction-all-20260907`, and the later controlled runner recovery.

Risk boundary: Preserve case/statute separation, exact source offsets, direct identifier-bearing same-decision anchors, and separate target resolution. Do not resume the all-case writer or modify persisted citations in this task.

Smallest falsifiable check: Full-document extraction returns complete `case` rows for the reported citations found in cases 37, 53, 62, and 65, and preserves repeated `case_short` forms at different offsets with direct anchors.

Acceptance criteria:

- Longer identifier-bearing full citation candidates always win over overlapping `case_name` or `case_short` candidates.
- A full-document fixture retains the complete reported spans for David Bull, Turpin, Suresh, and Kaberuka.
- Valid repeated short-form occurrences at distinct spans remain separate rows with direct full anchors.
- Bare names and prior short forms remain ineligible as anchors.
- Focused citation tests pass.
- Canonical documentation and Swimm record the repaired selection rule and validation evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: Revert the localized candidate-selection change. The total rebuild remains paused; preserve its baseline/comparison artifacts and do not resume until a repaired bounded cohort comparison is accepted.

Evidence: Paused-cohort audit found `12,446 -> 12,455` full/name/neutral rows and `27,455 -> 10,880` short rows. In full-document extraction, complete external reported citations were reduced or absent despite being in canonical text and extracting correctly as standalone strings: David Bull (`case 37`), Turpin (`case 53`), Suresh (`case 62`), and Kaberuka (`case 65`). They are not source-case self citations. The live rebuild is stopped at 1,295 completed cases; no resolution or metrics ran. Repair: allow closing parenthetical/bracket citation boundaries; support digit-bearing party names in candidate/normalization paths; promote an immediately adjacent reported-plus-neutral citation to one longest full anchor; and reject malformed case candidates that begin in a preceding neutral citation. Real corpus checks restored complete full anchors for cases 37, 53, 62, 65, and 627. In a ten-case highest-loss audit, repaired extraction increased anchored short rows versus the paused result by 290 in case 601, 57 in case 615, and 107 in case 765. The successor recovery task repaired direct CanLII short anchoring and rejects generic bare aliases; reporter-only historical anchors remain separate. Final focused validation: `python -m pytest tests\\test_citations.py -q` -> `137 passed, 1 warning`. Canonical documentation updated: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`; Swimm walkthrough updated: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If complete reported candidates are retained through candidate assembly and ranked above overlapping name/short candidates, the full-document fixtures will produce complete `case` anchors and preserve subsequent legitimate short-form rows without enabling short-to-short anchors.

## Plan

1. Trace candidate construction and overlap selection for the failing full-document contexts.
2. Add minimal exact-span regression fixtures and repair the localized selection rule.
3. Run focused citation tests and update authoritative documentation/Swimm before planning a repaired cohort.

## Execution Checkpoints

- Delegation: None; the extractor/fixture interaction needs direct local diagnosis.
- Implementation: `backend/citations.py` and `tests/test_citations.py` repaired and validated.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`; system-map change is not required because the ownership boundary did not change.
- Recovery: `data/overnight_runs/citation-extraction-all-20260907` remains the paused-run authority.

## Completion

Completion recorded: yes

Summary: Reported-citation candidate selection is repaired; the follow-on CanLII short-anchor recovery is complete in task 077.

Validation: `python -m pytest tests\\test_citations.py -q` -> `137 passed, 1 warning`.

Residual risk: The paused cases have regenerated citation rows; restoration/rebuild is a separate approved recovery step after extractor acceptance.

Next recommended task: Repair the Windows atomic state-write failure and run a fresh bounded controlled rebuild cohort before considering the paused all-case run.