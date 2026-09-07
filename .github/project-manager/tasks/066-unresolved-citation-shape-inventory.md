# Unresolved Citation Shape Inventory

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Build a read-only worklist of unresolved citation shapes and use the highest-volume precision-safe family to guide the next bounded recovery.

Why now: The previous deterministic passes reduced unresolved rows to 747,051, but the remaining population is large enough that source coverage, alternate formatting, and extraction-shape evidence may reveal additional exact recoveries.

Owner surface: `scripts/resolve_citation_targets.py`, `scripts/resolve_short_citation_targets.py`, and citation-resolution QA/reporting.

Commit allowed: yes

Push allowed: yes

Dependencies: Live PostgreSQL citation and case rows; existing citation normalization and local case indexes.

Risk boundary: Read-only inventory first. Do not alter citation text, offsets, provenance, statutes, or target links without a unique local target and a focused precision test. Do not use broad fuzzy matching, surname-only matching, or external paid services without explicit approval.

Smallest falsifiable check: Run a bounded read-only database report grouping unresolved rows by citation kind and normalized citation shape, then measure whether the largest groups have a unique exact local citation/title candidate.

Acceptance criteria:

- The unresolved population is grouped into an actionable list by citation kind and shape.
- Candidate recoveries are ranked by count, uniqueness, and evidence strength.
- One precision-safe rule is either tested and applied in a bounded batch, or explicitly deferred with evidence.
- Focused citation tests, compilation, and final live counts are recorded.
- Canonical documentation and the relevant Swimm walkthrough describe the result and next bounded task.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/blank.dudtv9pz.sw.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: Inventory artifact is read-only. The title-year writer inspected citation IDs through `6,424,840` and updated only previously unresolved target links in bounded commits; recover by clearing only the recorded title-year batch links if needed, leaving citation rows and source evidence intact.

Evidence: Read-only inventory artifact, focused tests, bounded dry run, full title-year recovery writer, live count query, representative target spot check, generated catalog refresh, and documentation checkpoint recorded below.

## Hypothesis

If unresolved rows are grouped by normalized citation shape and checked against exact local citation/title indexes, then duplicate canonical titles with an exact cited decision year will yield a unique-target rule that improves recall without reducing precision.

## Plan

1. Run a read-only unresolved-shape inventory and save its output as evidence.
2. Test the highest-ranked candidate against existing fixtures and a bounded live sample.
3. Apply only a unique-target rule, rerun focused tests, and update live counts.
4. Update canonical and Swimm documentation with evidence and residual risk.

## Execution Checkpoints

- Delegation: none; direct bounded database inventory keeps production data read-only.
- Implementation: `scripts/report_unresolved_citation_shapes.py`, `scripts/resolve_citation_targets.py`, and `tests/test_citations.py`; focused suite passed after title-year rule.
- Documentation: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/blank.dudtv9pz.sw.md`, `.swm/system-map.ovnldklv.sw.md`, and generated `docs/SCRIPT_CATALOG.generated.md` updated.
- Recovery: read-only inventory saved at `data/eval/reports/unresolved_citation_shapes_20260907.json`; writer completed through citation ID `6424840` with bounded commits.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Task created | Remaining unresolved rows warrant a shape-level worklist before another resolver rule | Final checkpoint recorded 747,051 unresolved rows |
| 2026-09-07 | Title-year rule applied | Duplicate title families such as Baker and RJR-Macdonald had unique cited decision years; ambiguous year sets remained rejected | Inventory found 2,341 candidates; writer linked 2,343 and Baker spot check resolved to case 35899 |

## Completion

Completion recorded: yes

Summary: Built a ranked unresolved-shape worklist and applied exact title-plus-decision-year disambiguation for duplicate canonical titles.

Validation: `tests\\test_citations.py` passed `120`; bounded dry run inspected `100,000` rows and found `2` candidates; full writer inspected `747,051` rows and linked `2,343`; live count query returned `2,152,332` total, `1,407,624` resolved, `744,708` unresolved, broken down as `444,007` `case_short`, `251,906` `case_name`, `44,364` `case`, and `4,431` `neutral`; Python compilation, diagnostics, generated-doc check, and `git diff --check` passed.

Residual risk: `692,870` unresolved rows had no exact local signal in the inventory; `623` title-year candidates remained ambiguous. The remaining population is dominated by absent authorities, anonymized/truncated names, extraction noise, and ambiguous aliases. No fuzzy matching or external API adjudication was used.

Next recommended task: Build a read-only source-coverage report for the largest absent-authority families, beginning with historical Federal Court and pre-CanLII reporter citations.
