# Case-Citation Rebuild Anchor Invariant

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Prepare the case-to-case citation extractor for a clean citation-layer rebuild by requiring every persisted short-form anchor to reference a full same-decision case citation with an identifier.

Why now: Historical citation rows mix earlier extraction behavior with the current parser. A clean rebuild must preserve every detected short-form occurrence while preventing short-to-short anchor chains and bare case-name anchors.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Canonical case text, citation-layer rebuild runner, focused extraction tests, and a pre-rebuild citation audit.

Risk boundary: Do not run a database delete or rebuild. Do not alter statutes, metadata, tags, chunks, case records, source text, citation occurrence text, occurrence offsets, or pinpoint values. Target resolution remains separate. Do not broaden normalization beyond the extractor's current canonical form.

Smallest falsifiable check: A text containing one full citation followed by two short mentions must produce two `case_short` occurrences whose anchor text and offsets both equal the full citation span; a bare case name followed by a short mention must not produce an anchored short citation.

Acceptance criteria:

- A short-form anchor originates only from a full `case` match containing a legal identifier.
- Multiple short-form occurrences retain their individual source offsets and pinpoints.
- Every short-form occurrence anchors directly to the full citation, never to another short-form occurrence.
- Focused citation tests pass.
- No database writer, delete, or rebuild runs in this task.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: Source-only change. Revert the anchor-admission rule and rerun focused tests. A later rebuild requires a citation export, bounded cohort, checkpoint/resume state, and post-run audit before any wider delete.

Evidence: The Vavilov regression was traced to an oversized parser `case_name` span being included in V2 overlap selection and blocking later aliases. Restoring the existing V2 case-name boundary retained full neutral promotion while leaving bare names non-anchor evidence. `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q -k rebuild_style_extraction` passed (`1 passed, 127 deselected, 1 warning`); it uses an in-memory recording session with `resolve_targets=False` and proves two Zazai short rows persist with distinct source offsets, shared direct full-anchor fields, and no targets. Final `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q` passed (`128 passed, 1 warning`). Documentation checkpoint: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/system-map.ovnldklv.sw.md` updated.

## Hypothesis

If bare `case_name` matches cannot seed anchor entries, then all emitted `case_short` matches will retain their own occurrences while directly referencing a full same-decision citation span with a legal identifier.

## Plan

1. Verify the anchor admission path and current duplicate-short coverage.
2. Tighten anchor admission and add direct-anchor and bare-name regression tests.
3. Run focused citation validation and document the rebuild gate. Complete.

## Execution Checkpoints

- Delegation: None; the parser invariant and test are a single local slice.
- Implementation: Complete in `backend/citations.py` and `tests/test_citations.py`.
- Documentation: Complete in `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/system-map.ovnldklv.sw.md`.
- Recovery: No database operation is authorized in this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Require full-case anchors for short forms | A historical bare case-name anchor can mask a missed legal identifier, producing inconsistent anchor provenance | Zazai source text contains a full dotted neutral citation while the historical stored anchor ends at the bare case name |

## Completion

Completion recorded: yes.

Summary: Short forms now anchor only to direct identifier-bearing same-decision full citations. Bare names and short forms cannot seed anchors; full neutral and reported forms retain compatibility behavior.

Validation: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q -k rebuild_style_extraction` - `1 passed, 127 deselected, 1 warning`; `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q` - `128 passed, 1 warning`. No destructive database command or rebuild ran.

Residual risk: The in-memory test proves the extractor and persistence helper contract only. A real citation-layer rebuild still requires explicit approval, a baseline export, bounded cohort behavior, checkpoints/resume, and post-run comparison before any wider delete.

Next recommended task: Run a bounded clean citation-layer rebuild only after the invariant and cohort audit pass.
