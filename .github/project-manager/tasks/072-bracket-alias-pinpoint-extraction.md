# Bracket Alias And Pinpoint Extraction

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Verify and repair, if necessary, deterministic extraction of full case citations that include bracket aliases and trailing pinpoints before preparing a clean citation-layer rebuild.

Why now: A rebuild must preserve full citation spans, declared aliases, and pinpoints. Reported live-extraction cases may be truncating a full authority before a bracket alias or later pinpoint, which would weaken short-form anchoring and citation evidence.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `tests/test_citations.py`, citation persistence helper, and the citation evidence Swimm walkthrough.

Risk boundary: No database writer, deletion, rebuild, target resolution, metric recomputation, or external lookup. Do not change statutes, metadata, tags, chunks, or source records.

Smallest falsifiable check: A full citation with a bracket alias and a trailing pinpoint produces one full `case` match whose source slice includes the alias and pinpoint, whose `declared_alias` is populated, and whose `pinpoint` is populated; a later alias short form retains its own pinpoint and anchors to that full span.

Acceptance criteria:

- Bracket aliases are retained as part of their identifier-bearing full citation span.
- Trailing pinpoints after full citations and alias forms are preserved in citation text and normalized citation.
- Later short forms retain their own pinpoints and direct full-anchor provenance.
- Relevant focused citation tests pass.
- No data mutation runs.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md` or the active citation walkthrough.

Rollback/recovery: Source-only parser/test change. Revert the local rule and rerun focused tests. The citation rebuild remains unapproved until a separate bounded runner is implemented and validated.

Evidence: Read-only audit confirmed extension order is base match -> trailing reporter -> pinpoint -> bracket alias -> pinpoint after alias. The added Albert regression passed: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_citations.py -q -k "preserves_bracket_alias_and_trailing_pinpoints"` -> `1 passed, 128 deselected, 1 warning`. It proves full text `Albert v. Canada (MCI), 2020 FC 100 [Albert] at para. 30`, declared alias `Albert`, full pinpoint `at para. 30`, later short pinpoint `at para. 40`, and direct anchor provenance. Documentation checkpoint: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If the full citation extension runs before declared-alias extraction and pinpoint capture, then a citation such as `Albert v. Canada (MCI), 2020 FC 100 [Albert] at para. 30` will remain one full case occurrence and later `Albert at para. 40` will anchor directly to that full span.

## Plan

1. Inspect full-citation extension order and nearby alias/pinpoint tests.
2. Add the Albert regression and repair the local parser only if it fails.
3. Run focused citation validation and document the verified behavior. Complete.

## Execution Checkpoints

- Delegation: Completed read-only pinpoint/alias path audit.
- Implementation: Added focused Albert regression; no parser repair was needed.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: No database operation is authorized.

## Completion

Completion recorded: yes.

Summary: Bracket aliases and pinpoints after aliases are retained in full citation spans; later short forms preserve their own pinpoints and direct anchors.

Validation: `1 passed, 128 deselected, 1 warning`. No database mutation ran.

Residual risk: This proves the default V2 extractor behavior. The controlled citation-only runner remains a separate operational prerequisite.

Next recommended task: Implement and validate the bounded citation-only rebuild runner before seeking approval for a cohort execution.
