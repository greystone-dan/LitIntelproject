# Task: Recover case-name citation resolution

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Identify and fix the structural reason `case_name` resolution is only 5.24%, while preserving precision and preventing corpus-wide guesses.

Why now: `333,550` of `351,982` `case_name` rows remain unresolved. The exact canonical-title pass is exhausted, so repeating it cannot improve the result.

Owner surface: `scripts/resolve_citation_targets.py` and its focused citation-resolution tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Current citation inventory, canonical `Case` title/citation fields, task 082 exact-title evidence, and no database writer for the investigation phase.

Risk boundary: Read-only inventory first. Do not write target links until a deterministic candidate rule is measured and tested. Never use short-name matching as a global case-name fallback, fuzzy-match unresolved names, or alter citation extraction/offsets in this task.

Smallest falsifiable check: A bounded read-only comparison of unresolved `case_name` values against canonical title/citation aliases, followed by a focused resolver test.

Acceptance criteria:

- Name the specific structural mismatch responsible for the low recovery rate.
- Quantify recoverable candidate classes without database writes.
- Implement the smallest deterministic improvement with collision/self guards.
- Validate the improvement with focused tests and a dry-run count before any apply decision.
- Update `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md` with evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`, `data/eval/reports/`

Rollback/recovery: No database writes during investigation. Any later apply must emit a citation-id/target-id mapping artifact before bounded commits; revert only those IDs if review rejects the rule.

Evidence: Pending. Baseline: `351,982` total `case_name`, `333,550` unresolved, `18,432` resolved. Exact canonical-title candidates remaining: `0`.

## Hypothesis

The resolver is losing valid `case_name` matches because it compares one strict normalized title key, while stored citation names and canonical case identity differ through government-role designations, historical abbreviations, or extraction prefixes.

## Plan

1. Compare unresolved name groups against canonical title and citation aliases in read-only mode.
2. Implement the highest-confidence deterministic candidate class and focused tests.
3. Run a bounded dry-run report, then document results and defer database apply until evidence supports it.

## Execution Checkpoints

- Delegation: bounded read-only comparison of unresolved names and canonical identity variants; exact structured return required.
- Implementation: resolver and focused tests only after the mismatch is falsified or confirmed.
- Documentation: canonical system/operations docs and citation Swimm walkthrough.
- Recovery: mapping artifact required before any writer.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-14 | Start read-only investigation | Exact-title recovery is exhausted and the low case-name rate indicates a structural gap | Live inventory query |

## Completion

Completion recorded: no

Summary: Investigation in progress.

Validation: Pending.

Residual risk: Unresolved names may cite cases absent from the current inventory; do not treat every name-shaped row as recoverable.

Next recommended task: Pending read-only mismatch inventory.
