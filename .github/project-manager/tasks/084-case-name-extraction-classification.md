# Task: Repair case-name extraction and classification

Status: deferred
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Repair citation extraction so full reported case citations are classified as `case`, genuine name-only references as `case_name`, and truncated/noisy `X v Y` spans are rejected or completed before target resolution.

Why now: The live unresolved `case_name` backlog is `333,550` rows. Bounded inspection found full reported citations such as `R. v. Backhouse, (2005), 195 O.A.C. 80` stored as `case_name`, alongside truncated spans such as `Anderson v. The`, `Hardy v. Motor`, and `Echostar Corporation v. Service`. These malformed or misclassified rows cannot be resolved reliably by the current title resolver.

Owner surface: `backend/citations.py` and the controlled citation rebuild path

Commit allowed: yes

Push allowed: yes

Dependencies: Citation extractor tests, controlled rebuild runner, a bounded affected-case cohort, and no competing PostgreSQL writer.

Risk boundary: Do not run a corpus-wide extraction replacement or target-resolution writer in this deferred task. Preserve source offsets, short-form anchor invariants, and existing citation identity until extractor fixtures and a bounded canary pass.

Smallest falsifiable check: Add focused extractor fixtures proving parenthesized reported citations classify as `case`, complete standalone names remain `case_name`, and truncated weak-party spans are rejected; run `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q`.

Acceptance criteria:

- Parenthesized-year reported citations no longer enter `case_name`.
- Standalone case-name extraction does not emit weak or truncated party spans without strong evidence.
- Existing neutral, reported, short-form anchor, offset, and overlap tests remain green.
- A bounded canary quantifies affected rows before any full replacement.
- The main pipeline uses the corrected extractor before another resolution pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`, and `docs/EXTRACTION_35K_RUNBOOK.md`

Rollback/recovery: Keep changes extraction-only until the bounded canary passes. Use the controlled runner's baseline/comparison/checkpoint artifacts for any affected-case rebuild; do not reuse the full-corpus run directory.

Evidence: Read-only live probes completed without database writes. `R. v. Backhouse, (2005), 195 O.A.C. 80` is classified as `case_name` by both legacy and V2 extractors because the current branch uses `case_name if reported.startswith("(") else "case"`. The broad standalone regex also emits truncated forms. One bounded 5-row reader sample completed in `0.92` seconds; the earlier diagnostic timeout was caused by loading and repeatedly normalizing the entire Case inventory in Python, not by a database writer.

## Hypothesis

If reported-citation classification and standalone-name span selection are corrected in the extractor, a bounded affected-case rebuild will convert obvious full authorities to formal `case` rows and remove impossible truncated names before resolution, materially improving downstream matching.

## Plan

1. Add failing focused fixtures for classification and truncated-span behavior.
2. Correct extractor branch ordering/classification and standalone span boundaries.
3. Run the focused suite and a bounded read-only inventory of affected stored rows.
4. Execute a controlled canary only after explicit approval, then update the main pipeline checkpoint.

## Execution Checkpoints

- Delegation: none; live investigation was bounded and read-only.
- Implementation: deferred; no source or database edits in this task.
- Documentation: this task records the issue; canonical docs should be updated when implementation begins.
- Recovery: use a fresh controlled rebuild directory and preserve baseline/comparison/checkpoint artifacts.

## Completion

Completion recorded: no

Summary: Deferred backlog item recorded. No database writes or extractor changes were made.

Validation: Read-only extractor probes and bounded live queries completed; no implementation validation run because the task is deferred.

Residual risk: The current `case_name` population mixes name-only, full reported, and truncated/noisy spans, so resolution metrics remain understated until extraction is repaired.

Next recommended task: Implement focused extractor fixtures and correction, then run a bounded canary before any corpus-wide rebuild.
