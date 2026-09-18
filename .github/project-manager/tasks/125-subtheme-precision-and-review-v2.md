# Task: Sub-theme precision and review packet V2

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Implement the external review findings for deterministic Discussion Unit sub-themes and produce a fresh multi-case review packet.

Why now: The first three-case review found strong provenance and usable boundaries, but recurring false positives from metadata/headings, over-broad party-position and counterargument cues, noisy display terms, and explanations that only list labels.

Owner surface: `backend/contextual_authority/` plus the read-only Discussion Unit inspector and focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Discussion Unit/SubTheme contracts, paragraph chunk fixtures, read-only inspector, and three-case evaluation artifacts.

Risk boundary: Preserve source text, chunk IDs, hashes, local offsets, contiguous paragraph boundaries, read-only behavior, separate canonical evidence layers, and offline execution. No database writes, migrations, UI/runtime activation, embeddings, clustering, or opaque labels.

Smallest falsifiable check: `PYTHONPATH=. .\\venv\\Scripts\\python.exe -m pytest tests/test_subthemes_v1.py tests/test_discussion_unit_inspector.py -q`

Acceptance criteria:

- Metadata-only headings, captions, certification, record, and solicitor sections do not produce substantive role observations unless supported by substantive text.
- `party_position`, `disposition`, and `counterargument_limitation` precision rules are tightened with adversarial tests.
- Display key terms filter obvious party/administrative noise while raw terms remain preserved.
- Explanations identify observed topic, actor, assertion/evidence, authority, and treatment without inventing legal conclusions.
- Existing provenance, offset, containment, determinism, and zero-write checks remain passing.
- Fresh bounded review artifacts are generated for additional cases.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/8.upryk5h6.sw.md`; `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`; no generated references.

Rollback/recovery: Revert only the task-owned code/tests/docs/artifacts if needed; all analysis remains read-only and staged under `data/eval/`. Do not alter canonical database rows.

Evidence: Pending delegated inventory, implementation checks, cross-case artifact validation, and documentation checkpoint.

## Hypothesis

If metadata/context filters and actor-aware role rules are applied before sub-theme aggregation, then the focused adversarial tests and a fresh multi-case rerun will show fewer metadata/party-position/counterargument false positives while preserving exact offsets, hashes, containment, and deterministic output.

## Plan

1. Delegate a bounded read-only inventory of the extraction, inspector, tests, and available case fixtures.
2. Implement the smallest deterministic precision and display-term changes in the owning package.
3. Run focused tests immediately, repair local failures, and rerun.
4. Generate a fresh bounded multi-case review set and validate cross-case invariants.
5. Update canonical documentation and the contextual-authority Swimm walkthrough.

## Execution Checkpoints

- Delegation: Explore read-only inventory completed; structured report identified `subthemes.py`, inspector, and focused tests as the owning slice.
- Implementation: `subthemes.py`, inspector, and focused tests updated; focused check passed with 13 tests.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated in this checkpoint.
- Recovery: No long-running writer; staged artifacts only.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-18 | Keep contiguous paragraph boundaries and improve local precision rules first | External review found boundaries broadly coherent and defects deterministic/local | Pasted external review feedback, sections B-K |

## Completion

Completion recorded: yes

Summary: V1.1 precision improvements implemented and fresh four-case review artifacts generated.

Validation: Focused tests: 13 passed before artifact generation; final focused suite: 18 passed. `py_compile` passed. `git diff --check` passed with Windows LF-to-CRLF warnings only. Fresh artifacts: cases 677, 1093, 1171, and 18674. Cross-case determinism, offsets, hashes, containment, display-term subset, and zero-write checks passed.

Residual risk: Implicit legal moves remain out of scope; sub-theme coherence and explanation usefulness still require external human review. Case 18674 is a heterogeneity check, not corpus-wide evidence.

Next recommended task: External human review of the four V1.1 packets before any further role taxonomy or semantic expansion.
