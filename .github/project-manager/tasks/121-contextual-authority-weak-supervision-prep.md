# Task: Weak-supervision agreement substrate

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Add a bounded weak-supervision preparation layer that compares deterministic rule votes without training a model or writing corpus labels.

Why now: Deterministic observations now provide transparent cue rules; the next safe step is measuring agreement, conflict, and abstention before statistical intelligence.

Owner surface: `backend/contextual_authority/`, bounded tests, and contextual architecture documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Phase 0 context units and Phase 1 deterministic observations.

Risk boundary: No model training, pseudo-label publication, corpus-scale labeling, canonical mutation, treatment inference, or UI integration.

Smallest falsifiable check: A fixture with two rule votes produces a stable agreement/conflict/abstention report while source observations remain unchanged.

Acceptance criteria:

- Define immutable rule-vote and agreement-report contracts.
- Support positive, negative, conflict, and abstention outcomes.
- Preserve observation provenance and exact evidence identity in reports.
- Keep output suitable for later weak-supervision tooling but do not emit labels for production use.
- Add focused tests and documentation.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and task evidence.

Rollback/recovery: Remove only the agreement module/tests/docs; no database or corpus writes occur.

Evidence: Phase 1 deterministic observations accepted with 162 combined tests passing, compilation passing, and `git diff --check` passing. Explore completed a read-only inventory of citation rule confidence, abstention, provenance, and evaluation conventions. Added `backend/contextual_authority/voting.py` and `tests/test_contextual_voting.py`; focused voting tests passed (4), combined contextual/citation regression passed (166), explicit compilation passed, and `git diff --check` passed. Documentation checkpoint updated in `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If deterministic observations are compared as abstaining rule votes, then disagreement can be measured explicitly before any pseudo-label or statistical model is introduced.

## Plan

1. Delegate a bounded inventory of existing evaluation/label-agreement conventions.
2. Implement pure vote normalization and agreement reporting.
3. Add focused conflict, abstention, provenance, and no-mutation tests.
4. Validate with contextual and citation regressions.
5. Update canonical and Swimm documentation; stop before model training.

## Execution Checkpoints

- Delegation: Explore inspected contextual observations, citation pipeline rules, AI triage suggestions, FC existence aggregation, and evaluation tests; no files changed.
- Implementation: Frozen `RuleVote` and `RuleAgreementReport` contracts with threshold-based abstention, conflict retention, deterministic provenance hashes, and no label publication.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated.
- Recovery: no model run, corpus labeling, or database writer.

## Completion

Completion recorded: yes

Summary: Weak-supervision preparation is complete as an in-memory agreement substrate.

Validation: `pytest tests/test_contextual_voting.py -q` passed (4); combined contextual/citation regression passed (166); explicit compilation and `git diff --check` passed. The suite emitted one existing `CryptographyDeprecationWarning` for ARC4; no new failure was observed.

Residual risk: Treatment labels and model-based confidence remain intentionally unsupported.

Next recommended task: Choose and approve the statistical intelligence model family and bounded calibration/labeled fixture before any model training or pseudo-label publication.
