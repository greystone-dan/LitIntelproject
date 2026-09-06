# Task: Repo-local agent control plane

Status: complete
Created: 2026-09-05
Updated: 2026-09-05

Task: Implement the first durable control-plane slice for autonomous managed tasks.
Why now: Prose-only autonomy did not reliably carry tasks through delegation, implementation, validation, documentation, and recovery.
Owner surface: `scripts/agent_harness.py`, `scripts/agent_policy.py`, managed-task documentation, and harness tests.
Dependencies: Existing managed-task prompt, project-manager task records, Swimm documentation checkpoint.
Risk boundary: This slice does not intercept VS Code tools or authorize destructive/production operations. Policy returns `allow`, `ask`, or `deny`; native hook/AHP integration remains a later adapter.
Smallest falsifiable check: Harness tests create atomic state/events, record command evidence, protect manager state, require approval for Git push, and reject terminal-state transitions.
Acceptance criteria: Run state, events, heartbeat, phase transitions, command logs/hashes, repair budget, and fail-closed policy surface exist; focused tests pass; canonical and Swimm docs explain authority boundaries.
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.github/prompts/managed-task.prompt.md`, `.github/project-manager/TASK_TEMPLATE.md`.
Rollback/recovery: Remove the new scripts/tests and revert documentation additions; no runtime or database changes.
Evidence:
- Added `scripts/agent_harness.py` with atomic state, events, heartbeat, transitions, command evidence, and terminal-state guards.
- Added `scripts/agent_policy.py` with worker manager-state denial and privileged Git approval decisions.
- Added `tests/test_agent_harness.py`.
- Harness tests passed: `5 passed`.
- Updated managed-task prompt, project-manager README, task template, Swimm transition guidance, and system reference.
- Python compilation and `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
