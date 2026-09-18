# Task: High-return tagging-system improvements

Status: in-progress
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Review the current deterministic legal-tagging system, identify high-return precision/recall gaps, and implement the safest bounded improvements with focused regression coverage.

Why now: The tagging system is a core research signal, but its current quality and rule coverage need an evidence-backed pass before broader corpus use.

Owner surface: backend/legal_tagger.py and adjacent tagging tests

Commit allowed: yes

Push allowed: yes

Dependencies: legal taxonomy definitions, tagging v2/v3 compatibility paths, focused tests and fixtures

Risk boundary: Do not rewrite taxonomy identifiers, run corpus-wide tagging/backfills, alter case text, change statute/citation extraction, or make production/semantic decisions. Preserve existing public output contracts and source provenance.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_legal_tagger.py -q

Acceptance criteria:

- A bounded inventory identifies the highest-value tagging defects and current coverage gaps.
- Implemented changes improve measured precision or recall with positive and negative fixtures.
- Existing tag payload shape and compatibility paths remain intact.
- Focused tagging tests and relevant static validation pass.
- Canonical documentation and the relevant Swimm walkthrough record the changes and residual risk.

Docs/generated references: SYSTEM_REFERENCE.md; docs/TESTING_MATRIX.md; LEGAL_TAGGING.md; relevant .swm/ walkthrough

Rollback/recovery: Revert only the focused tagging rule/test/documentation changes. No corpus backfill or destructive data operation is authorized.

Evidence: Pending delegated inventory, implementation, focused validation, and documentation checkpoint.

## Hypothesis

If current tagging rules are compared against their focused fixtures and taxonomy contract, then one or more high-frequency deterministic gaps can be fixed with additive rules without changing output shape or unrelated extraction layers.

## Plan

1. Delegate a bounded inventory of tagging implementations, tests, taxonomy sources, and recent known gaps.
2. Implement the highest-return local tagging slice supported by evidence.
3. Run focused tests immediately, repair local failures, and iterate on adjacent high-return fixes only when validated.
4. Update canonical and Swimm documentation and record remaining gaps before completion.

## Execution Checkpoints

- Delegation: pending tagging inventory and bounded recommendation
- Implementation: pending
- Documentation: pending SYSTEM_REFERENCE.md, docs/TESTING_MATRIX.md, LEGAL_TAGGING.md, and relevant Swimm walkthrough
- Recovery: no corpus tagging/backfill authorized

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Keep work deterministic and bounded | User requested high-return improvements without scope for corpus rewrite | Current managed-task request |

## Completion

Completion recorded: no

Summary: In progress.

Validation: Pending.

Residual risk: Real-corpus tagging quality remains unmeasured until a bounded evaluation sample is run.

Next recommended task: Run a fixed-sample tagging evaluation after the focused rule checkpoint.
