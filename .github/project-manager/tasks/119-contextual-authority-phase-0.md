# Task: Build contextual authority Phase 0 foundation

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Construct the additive contextual/analysis layer beginning with immutable snapshots, contextual units, deterministic context variants, and evidence invariants.

Why now: The research specification requires citation-context intelligence without mutating canonical citations, statutes, metadata, tags, chunks, or resolutions.

Owner surface: `backend/contextual_authority/`, `alembic/`, bounded context-generation scripts, and focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `Case`, `CaseChunk`, `Citation`, target-resolution fields, Alembic migration workflow, canonical processing documentation.

Risk boundary: No writes or updates to canonical citation/statute/metadata/tag rows; no production or unbounded corpus run; no treatment, weak-supervision, student-model, theme, profile, or temporal claims in Phase 0.

Smallest falsifiable check: A bounded fixture generates versioned sentence/paragraph/window/burst contextual units whose segments reconstruct exact canonical chunk text and whose snapshot remains unpublished until invariants pass.

Acceptance criteria:

- Additive schema supports immutable snapshots, context units, segment membership, citation membership, observations/evidence placeholders, and active-snapshot publication control without changing canonical tables.
- Deterministic Phase 0 generation supports sentence, paragraph, fixed-window, and citation-burst variants with method/version/config hashes.
- Every generated segment preserves source case/chunk identity, offsets, text hash, and reconstructability evidence.
- Bounded dry-run/inspection path exists; no unbounded writer is invoked.
- Focused tests cover snapshot state, offset/hash invariants, repeated citation membership, and no canonical mutation.
- Canonical documentation and the relevant Swimm walkthrough describe the boundary and validation command.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md` only if UI changes occur; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; relevant `.swm/` architecture/processing walkthrough.

Rollback/recovery: Remove only the new migration/package/script/test changes before publication; if a bounded snapshot is created, mark it failed or discard its unpublished rows transactionally. Never delete or rewrite canonical evidence.

Evidence: Delegated read-only inventory completed by Explore. It confirmed `CaseChunk` stores chunk text/hash and `Citation` stores chunk-relative occurrence offsets plus separate anchor offsets; latest migration is `0025_structured_statute_prov`; citation stages must remain unchanged. Added `backend/contextual_authority/`, migration `0026_contextual_authority_phase0`, focused invariant tests, and read-only `scripts/inspect_context_variants.py`. `pytest tests/test_contextual_authority_phase0.py tests/test_citations.py -q` passed with 159 tests; compilation passed; `alembic upgrade 0025_structured_statute_prov:0026_contextual_authority_p0 --sql` passed without applying migrations; `git diff --check` passed. Full-base offline SQL remains blocked by the pre-existing `0001_case_metadata` MockConnection inspection failure. Documentation checkpoint updated in `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If Phase 0 reads canonical chunks and citations without mutating them, then a bounded fixture can produce multiple versioned context variants with exact segment reconstruction and a non-active snapshot while existing citation tests remain unchanged.

## Plan

1. Inventory existing ORM, migration, processing, citation-offset, and script conventions through a bounded delegated read-only review.
2. Implement the smallest additive schema/contracts and deterministic context generators.
3. Add bounded invariant tests and a dry-run inspection command.
4. Run focused validation, inspect migration/schema output, and document the architecture boundary.
5. Only after Phase 0 passes, plan the next deterministic legal-intelligence slice.

## Execution Checkpoints

- Delegation: Explore inspected `backend/database.py`, `alembic/versions/0025_structured_statute_provisions.py`, `backend/case_processing.py`, `scripts/rebuild_citations_controlled.py`, and `tests/test_citations.py`; no files changed.
- Implementation: package/contracts, deterministic generators, additive migration, tests, and bounded inspector completed.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated.
- Recovery: no bulk run; bounded fixture/dry-run artifacts only.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-18 | Start with immutable additive Phase 0 | Both supplied specifications prohibit simultaneous implementation and canonical mutation | User-provided contextual authority specifications |

## Completion

Completion recorded: yes

Summary: Phase 0 additive foundation is complete; no canonical evidence rows were changed.

Validation: Focused contextual and citation tests passed (now 4 contextual tests plus the existing citation suite); `py_compile` passed for the new package, migration, and inspector; the new migration range compiled to offline SQL; `git diff --check` passed.

Residual risk: Existing reader highlight parity remains unrelated and unresolved. Full-base Alembic offline generation still fails in pre-existing migration `0001_case_metadata`; the new `0025 -> 0026` range compiles successfully. No database migration or corpus run was performed.

Next recommended task: Run a bounded database-backed inspector against an approved fixture, then implement deterministic actor/intent/treatment observations as a separate phase.
