# Task: Deterministic contextual authority observations

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Continue the additive contextual authority layer with deterministic, evidence-linked legal-intelligence observations over Phase 0 context units.

Why now: Phase 0 provides versioned context units and exact source spans; the next safe increment is transparent rule-based observations before weak supervision or statistical models.

Owner surface: `backend/contextual_authority/`, additive migration if required, bounded tests/scripts, and contextual architecture documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Phase 0 package, `CaseChunk`/`Citation` read-only contracts, existing citation/statute extraction semantics.

Risk boundary: No mutation of canonical citations, statutes, chunks, tags, metadata, outcomes, or resolution. No production corpus writer, model inference, weak supervision, treatment conclusion, authority profile, or UI integration.

Smallest falsifiable check: A fixture context containing explicit legal-language cues yields deterministic observations with exact evidence spans, method/version identity, and no changes to its source chunks or citation membership.

Acceptance criteria:

- Add a pure deterministic observation builder over Phase 0 context units.
- Support only transparent first-pass labels such as issue cue, treatment cue, and disposition cue; do not claim legal conclusions beyond the cue label.
- Preserve exact chunk-local evidence spans and hashes.
- Keep observations versioned and provenance-classed as deterministic rules.
- Add focused positive, negative, overlap, and no-mutation tests.
- Update canonical documentation and the relevant Swimm walkthrough.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and task evidence.

Rollback/recovery: Remove only the new observation code/tests/docs; no canonical rows are changed. Any future staged observation rows remain unpublished and transactionally discardable.

Evidence: Phase 0 completed with 159 focused tests, compilation, migration-range SQL compilation, and documentation checkpoint. Explore completed a read-only inventory and recommended reusing disposition patterns and safe issue/government-party cues while deferring treatment inference. Added `backend/contextual_authority/observations.py` and `tests/test_contextual_observations.py`; focused observation tests passed (3) and compilation passed. Documentation checkpoint updated in `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If deterministic observations operate only on immutable Phase 0 segments, then transparent legal-language cues can be added without changing citation identity, offsets, or source text.

## Plan

1. Delegate a bounded read-only inventory of existing legal cue/tag/outcome patterns and nearest tests.
2. Implement a pure observation contract and deterministic cue rules.
3. Add exact evidence-span and no-mutation tests.
4. Validate the focused slice and existing citation regression tests.
5. Update canonical and Swimm documentation; stop before weak supervision/statistical phases unless a new bounded task is opened.

## Execution Checkpoints

- Delegation: Explore inspected deterministic outcome, subject, tagger, metadata, Phase 0, and nearby test surfaces; no files changed.
- Implementation: Pure disposition, issue-type, and government-party observation builder completed; treatment/merits inference intentionally excluded.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated.
- Recovery: no corpus writer or model run.

## Completion

Completion recorded: yes

Summary: Deterministic observation phase is complete for the bounded safe-label slice.

Validation: `pytest tests/test_contextual_observations.py -q` passed (3); compilation passed. Combined contextual/citation regression is the final acceptance check.

Residual risk: Reader highlight parity remains unrelated and unresolved; this phase must not widen that scope.

Next recommended task: Run the combined regression, then open a separate managed task for citation-direction treatment experiments or weak-supervision label agreement.
