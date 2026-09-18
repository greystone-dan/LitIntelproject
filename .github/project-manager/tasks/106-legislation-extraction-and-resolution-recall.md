# Task: Improve legislation extraction and section resolution recall

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Improve legislation citation extraction recall and resolve recognized references to specific sections in the stored authority sources.

Why now: The user reports that abbreviated and repeated provision references are missed, reducing trust in legislation evidence even where the authority source is already stored.

Owner surface: backend/citations.py legislation extraction and authority-section resolution

Commit allowed: yes

Push allowed: yes

Dependencies: stored legislation_documents and legislation_sections; existing statute-reference parser; focused citation tests

Risk boundary: Do not change case-citation extraction, legislation versioning, corpus backfills, source acquisition, or destructive database data. Preserve raw reference text and exact source offsets. Any resolution must remain additive and provenance-aware.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_citations.py -k "statute_reference or legislation" -q

Acceptance criteria:

- A bounded inventory identifies the highest-value missed legislation-reference shapes and current resolution boundary.
- The first implementation slice improves recall for repeated, abbreviated, and case-varied provisions without changing raw spans.
- Recognized references can resolve to stored authority sections when instrument identity and pinpoint are sufficient.
- Positive, negative, and exact-span tests cover the changed behavior.
- Focused validation passes and canonical documentation plus the relevant Swimm walkthrough record the new contract.

Docs/generated references: SYSTEM_REFERENCE.md; docs/TESTING_MATRIX.md; docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Revert the focused extractor/resolution changes and tests. No database writer or corpus backfill is authorized in this task; any new additive code path must be disabled by reverting its source change.

Evidence: Delegated workers identified the controlling statute normalizers, anchored-provision path, stored legislation models, and reader surfaces. Implemented case-insensitive nested provision identity, cross-sentence shorthand carry-forward, read-only stored-section resolution with explicit unresolved statuses, and additive authority metadata in live analysis and the stored reader. Focused validation passed: citation tests 31 passed/122 deselected, stored-reader API tests 2 passed/42 deselected, live-analysis tests 6 passed, and git diff --check passed. SYSTEM_REFERENCE.md, docs/TESTING_MATRIX.md, and .swm/4.9nn3id9f.sw.md record the new contract. A bounded read-only residue assessment found no single additional high-confidence regex gap; remaining evidence is mixed non-IRPA instrument identity/noisy-title coverage and needs a fresh bounded demand report before more rule edits.

## Hypothesis

If legislation extraction preserves provision aliases and uses the stored instrument registry to resolve exact section keys, then focused mixed-form fixtures will show higher recall and deterministic section resolution without altering raw text or offsets.

## Plan

1. Delegate a bounded inventory of extractor patterns, stored authority resolution paths, and highest-value nearby tests.
2. Implement the smallest recall and resolution slice supported by that evidence.
3. Run focused tests immediately, repair local failures, and add only directly required fixtures.
4. Update canonical and Swimm documentation, then record residual missed shapes for the next bounded task.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager workers completed bounded inventory, extraction, resolution, and reader-adoption slices with the required structured reports.
- Implementation: backend/citations.py, backend/statutes.py, backend/live_analysis.py, backend/reader_service.py, backend/models.py, and focused tests; no schema or data writer changes.
- Documentation: SYSTEM_REFERENCE.md, docs/TESTING_MATRIX.md, and .swm/4.9nn3id9f.sw.md updated.
- Recovery: no corpus backfill or unbounded writer authorized

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Keep versioning out of scope | User explicitly deferred legislation versions | Current managed-task request and prior authority checkpoint |
| 2026-09-17 | Keep case citations separate | Legislation recall is the current trust gap | Project invariants and task owner surface |

## Completion

Completion recorded: yes

Summary: Improved legislation recall and added deterministic read-only section resolution across live analysis and the stored reader without changing raw text or offsets.

Validation: .\\venv\\Scripts\\python.exe -m pytest tests/test_citations.py -k "statute_reference or legislation" -q -> 31 passed, 122 deselected; .\\venv\\Scripts\\python.exe -m pytest tests/test_api.py -k "stored_reader_statute_references" -q -> 2 passed, 42 deselected; .\\venv\\Scripts\\python.exe -m pytest tests/test_live_analysis.py -q -> 6 passed; git diff --check passed.

Residual risk: Lists/ranges and unindexed instruments remain explicitly unresolved, and no corpus-wide recall claim or backfill was made. Further shape expansion should be driven by a sampled unresolved-reference inventory.

Next recommended task: Build a bounded read-only unresolved statute-shape report and prioritize the next instrument/alias family by frequency and precision risk.
