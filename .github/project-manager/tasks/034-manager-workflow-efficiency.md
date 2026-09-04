# Task: Improve manager workflow reliability and token efficiency

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Add delegated-agent recovery rules, manager-only task-record ownership,
explicit commit/push permissions, fresh-evidence requirements, and remove
avoidable prompt duplication while preserving repository safety boundaries.

Why now: A delegated audit returned no output, created duplicate task state,
and required recovery. The instruction stack repeats substantial content and
has ambiguous status/commit handling, increasing token burn and interruption risk.

Owner surface: `.github/agents/project-manager.agent.md`,
`.github/prompts/managed-task.prompt.md`, `.github/project-manager/TASK_TEMPLATE.md`.

Commit allowed: yes

Push allowed: yes

Dependencies: `.github/copilot-instructions.md`, project-manager README, active
managed-task workflow.

Risk boundary: Workflow-only changes. Do not alter application code, data,
security posture, generated references, or existing task history.

Smallest falsifiable check: Parse prompt frontmatter and grep for required
recovery, ownership, permission, and fresh-evidence rules; run `git diff --check`.

Acceptance criteria:

- Delegated no-output recovery and structured-return requirements are explicit
- Subagents cannot own task-record completion or commit/push decisions
- Commit and push permissions are distinct and require fresh validation
- Task template has one canonical status field
- Prompt duplication is reduced without removing repository invariants

Docs/generated references: `.github/project-manager/README.md`; no generated docs.

Rollback/recovery: Revert only the three workflow files if validation fails.

Evidence: Delegated agent edited only the three authorized workflow files. Independent `git diff --check` passed. UTF-8 contract check confirmed the exact delegated return schema, explicit commit/push permissions, and one template `Status:` field. Agent and managed-task prompt frontmatter remains present; TASK_TEMPLATE is correctly a plain Markdown template without frontmatter. No application files or Git history changed.

## Hypothesis

If workflow ownership, recovery, and permission rules are explicit and repeated
text is reduced, managed tasks will recover predictably with less context cost.

## Plan

1. Delegate bounded edits to the agent and prompt files; manager keeps task state.
2. Update the task template status and commit/push fields.
3. Validate frontmatter, required rules, diff, and prompt references.

## Completion

Status: complete

Summary: Added delegated-agent recovery and structured-return rules; made task records, final acceptance, and commit/push decisions manager-owned; added separate commit/push permissions and fresh-validation requirements; added a compact token-efficiency section; and removed duplicate task-template status ambiguity.

Validation: `git diff --check` passed. UTF-8 content assertions passed for required schema, permissions, and single canonical template status. Scope review confirmed exactly three workflow files changed by the delegated edit.

Residual risk: Prompt behavior remains instruction-guided rather than mechanically enforced; a future hook could enforce prohibited task-file or Git operations if this remains a recurring failure mode.

Next recommended task: Resume citation extraction with one delegated bounded corpus audit and manager-owned evidence consolidation.
