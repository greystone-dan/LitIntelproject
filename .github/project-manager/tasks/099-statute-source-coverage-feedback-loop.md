# Task: Rank statute source coverage for extraction feedback

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Identify the most frequently referenced statute instruments and compare their live authority-source/XML coverage to determine the smallest useful extraction feedback-loop experiment.

Why now: IRPA/IRPR authority XML is already indexed. Extending the same source-backed approach to the dominant remaining instruments may improve section recognition while keeping extraction auditable and bounded.

Owner surface: statute extraction/source coverage inventory

Commit allowed: yes

Push allowed: yes

Dependencies: `statute_references`, `legislation_documents`, `legislation_sections`, `backend/statutes.py`, `scripts/index_legislation.py`, focused extraction tests

Risk boundary: Read-only inventory first. Do not download external sources, run bulk extraction/backfill, alter extraction rules, or modify canonical records in this task.

Smallest falsifiable check: Read-only database query ranking `instrument_key` and normalized references by frequency, joined to authority-document and section counts.

Acceptance criteria:

- Produce a frequency-ranked list of dominant statute instruments from live stored references.
- Show which dominant instruments already have source documents and section text.
- Identify one bounded source-backed extraction experiment and its focused validation.
- No database writer, external acquisition, or corpus backfill runs.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md`; `ROADMAP.md`

Rollback/recovery: No data mutation is authorized. Remove or mark this task deferred if the inventory cannot be reproduced from the configured database.

Evidence: Read-only ORM inventory completed with no database writes or external acquisition. The configured database contains 751,944 statute references, 13 legislation documents, and 4,522 legislation sections. Highest uncovered priority: `canada.immigration_act` with 10,107 occurrences across 2,648 cases and no indexed document. Highest covered non-IRPA priority: `canada.criminal_code` with 50,020 occurrences across 3,708 cases, one indexed document, and 1,716 sections. The bounded Criminal Code fixture slice passed: `tests/test_citations.py -q -k "parse_legislation_citation_supports_criminal_code or extract_statute_reference_matches_returns_only_law_layer or extract_statute_references_from_text_keeps_non_irpa_instruments or resolve_legislation_reference"` -> 9 passed, 144 deselected, 1 warning. Canonical documentation: `ROADMAP.md`; Swimm walkthrough: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If dominant statute instruments are identified from stored references and paired with authoritative XML section coverage, then a bounded fixture comparison can determine whether source-backed section structure improves extraction without requiring a corpus rebuild.

## Plan

1. Delegate a bounded read-only inventory of statute frequencies and authority-source coverage.
2. Review the ranked gap and select one instrument/source-backed experiment.
3. Run focused extraction comparison only after the source and acceptance check are explicit.
4. Update canonical and Swimm documentation with the decision and evidence.

## Execution Checkpoints

- Delegation: Explore assigned a read-only inventory of dominant instruments, source files, and live authority coverage.
- Implementation: Bounded Criminal Code source-backed fixture comparison selected; no code or data changes authorized during inventory.
- Documentation: Updated `ROADMAP.md` and `.swm/4.9nn3id9f.sw.md` with live coverage results and the gated experiment.
- Recovery: No writer or external acquisition authorized.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-15 | Task created | User proposed prioritizing XML source coverage based on dominant statute usage to improve extraction through a feedback loop | Existing IRPA/IRPR XML index and extraction architecture |

## Completion

Completion recorded: yes

Summary: Completed the read-only statute demand and authority-source coverage inventory and selected the first bounded source-backed extraction experiment.

Validation: Read-only ORM coverage query completed; focused Criminal Code/statute resolution slice passed 9 tests with 144 deselected.

Residual risk: Citation frequency may reflect parser bias or existing corpus composition; it is not by itself a precision or recall measure.

Next recommended task: Build the Criminal Code fixture comparison against the indexed Justice Laws sections, with exact-span positive/negative cases and no corpus writer.
