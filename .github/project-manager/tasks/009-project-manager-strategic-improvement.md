# Task: Strengthen Project Manager Strategic Reasoning

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Extend the AI CaseLibrary project-manager agent from disciplined task execution toward technical product management and continuous improvement.
Why now: The current agent protects implementation quality but does not consistently connect work to product mission, compare architectural options, or surface high-leverage improvement opportunities.
Owner surface: `.github/agents/project-manager.agent.md`
Dependencies: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
Risk boundary: Strategic analysis must remain proportional to task complexity and must not override existing safety, ownership, validation, provenance, or escalation rules.
Smallest falsifiable check: Verify the edited agent file contains the new strategic sections and all existing required safety and task-record sections.
Acceptance criteria: The agent has mission alignment, goal translation, solution evaluation, continuous improvement review, cost-aware execution, and self-improvement guidance; routine work remains lightweight; multi-step work remains evidence-backed.
Docs/generated references: `.github/agents/project-manager.agent.md`; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
Rollback/recovery: Revert only the agent instruction change and this task record if the new workflow causes unnecessary analysis or conflicts with repository guardrails.
Evidence: Updated `.github/agents/project-manager.agent.md` with mission alignment, goal translation, proportional continuous-improvement review, major-change solution evaluation, cost-aware execution, daily review triggers, and a non-automatic self-improvement loop. Added the improvements record convention and documented it in `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`. Prompt structure validation found all 11 required headings; `git diff --check` passed.
