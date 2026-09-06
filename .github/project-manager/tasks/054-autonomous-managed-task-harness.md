# Task: Autonomous managed-task harness

Status: complete
Created: 2026-09-05
Updated: 2026-09-05

Task: Make the project-manager workflow execute multi-step tasks through delegation, implementation, validation, documentation, recovery, and completion without routine confirmation requests.
Why now: The agent was stopping after plans, partial tests, or intermediate milestones instead of carrying the user-approved task through its full acceptance loop.
Owner surface: `.github/prompts/managed-task.prompt.md`, `.github/project-manager/README.md`, `.github/project-manager/TASK_TEMPLATE.md`, and Swimm transition guidance.
Dependencies: Existing project-manager agent, task records, delegated structured-return contract, canonical/Swimm documentation rule.
Risk boundary: Autonomy does not authorize destructive, paid, production, security, Government of Canada/CBSA, or unbounded operations. Those remain approval boundaries.
Smallest falsifiable check: Inspect the managed-task prompt for the execute-through-completion contract and validate customization/documentation whitespace.
Acceptance criteria: Managed tasks explicitly plan, delegate, implement, test, repair, document, recover, and complete; routine confirmation is not required; completion evidence names canonical and Swimm paths.
Docs/generated references: `.github/prompts/managed-task.prompt.md`, `.github/project-manager/README.md`, `.github/project-manager/TASK_TEMPLATE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`.
Rollback/recovery: Revert the workflow instruction/template changes; task records remain ordinary Markdown.
Evidence:
- Updated managed-task prompt with autonomous execution phases, no-routine-confirmation rule, watchdog/recovery expectations, and completion gate.
- Updated project-manager README with autonomous invocation behavior.
- Extended task template with execution checkpoints.
- Updated Swimm transition guidance with the same execution contract.
- `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
