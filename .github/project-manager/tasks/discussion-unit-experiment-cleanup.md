# Task: Clean up Discussion Unit experiment artifacts

Status: planned
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Inventory and clean up historical Discussion Unit experiment outputs while preserving the evidence needed for comparison.

Why now: The 20-case and future 300-case runs generate many local request, response, review, and ledger files. They are useful during analysis but should not become permanent GitHub project structure or expose unnecessary source text in repository history.

Owner surface: `data/eval/llm_discussion_units_pilot/` and repository evaluation-artifact policy

Commit allowed: yes

Push allowed: yes

Dependencies: Complete paragraph-level and span-based comparison summaries; user approval before deleting or archiving any artifacts

Risk boundary: Do not delete source reports, completed run evidence, ledgers, or raw responses until a comparison summary and recovery/archive location have been verified. Do not alter application code, canonical case data, or database records.

Smallest falsifiable check: `git status --short --untracked-files=all -- data/eval/llm_discussion_units_pilot` shows generated run directories ignored, while intentionally retained summaries remain visible.

Acceptance criteria:

- A complete inventory identifies each experiment, its purpose, case count, status, and total cost.
- Detailed generated files are either archived outside the working tree or removed only after verification and approval.
- A small comparison summary preserves the conclusions and key metrics for the span-based and paragraph-level methods.
- `git status` does not expose routine generated run files, and `git diff --check` passes.

Docs/generated references: `docs/TESTING_MATRIX.md`; relevant Discussion Unit task records; no generated documentation files

Rollback/recovery: Restore archived run directories from the recorded archive path or Git history; do not use destructive deletion before the archive manifest is checked.

Evidence: Pending. Current evidence includes the 12 completed paragraph-level comparisons and the repository ignore rule added on 2026-09-24.

## Hypothesis

If generated experiment directories are ignored and their conclusions are reduced to verified summaries before cleanup, the project will remain easy to navigate without losing the evidence needed to choose between span-based and paragraph-level Discussion Unit methods.

## Plan

1. Inventory all existing Discussion Unit experiments, artifacts, ledgers, and generated file counts.
2. Produce and verify aggregate comparison summaries for the 20-case and 300-case runs.
3. Archive or remove detailed artifacts with explicit approval and recheck repository status.

## Execution Checkpoints

- Delegation: None yet; use a bounded read-only inventory before cleanup.
- Implementation: Added the targeted `.gitignore` rule for `data/eval/llm_discussion_units_pilot/*_run/`.
- Documentation: Update the comparison summary and relevant task record; no generated reference edits.
- Recovery: Record archive path and manifest before any deletion.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-24 | Ignore generated evaluation run directories | Prevent local experiment outputs from entering GitHub accidentally | Current `git status` showed generated run files as untracked |
| 2026-09-24 | Defer cleanup until comparison is complete | Preserve evidence while the two methods are being evaluated | 12 paragraph-level reviews are available and the 300-case run is planned |

## Completion

Completion recorded: no

Summary: Planned cleanup task only; no generated artifacts were deleted.

Validation: Targeted ignore rule applied. Full cleanup validation is pending.

Residual risk: Existing untracked artifacts remain on disk and may need archiving or deletion after comparison.

Next recommended task: Complete the 300-case comparison, generate the aggregate report, then execute this cleanup task.
