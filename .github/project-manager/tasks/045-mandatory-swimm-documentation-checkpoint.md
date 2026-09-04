# Task: Mandatory Swimm documentation checkpoint

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

Task: Require every agent or delegated task to update the relevant Swimm walkthrough and canonical repository document before completion.
Why now: Generated-document CI catches repository drift, but task completion also needs durable architecture and workflow context in Swimm.
Owner surface: Project-manager instructions and Swimm transition contract.
Dependencies: `.github/agents/project-manager.agent.md`, `.github/copilot-instructions.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`.
Risk boundary: Swimm is authoritative for explanation, rationale, ownership, and workflow context; code, migrations, generated references, and executable runbooks remain authoritative for exact implementation and reproducibility.
Smallest falsifiable check: Inspect the customization and transition files for the mandatory checkpoint language and run `git diff --check`.
Acceptance criteria: Completion requires both documentation paths in task evidence; missing walkthrough coverage blocks completion; delegated work follows the same rule.
Docs/generated references: Custom project-manager agent, repository instructions, Swimm transition document.
Rollback/recovery: Revert only the instruction and transition-document additions; no runtime or database changes.
Evidence:
- Updated `.github/agents/project-manager.agent.md` with mandatory Swimm and canonical-document checkpoint rules.
- Updated `.github/copilot-instructions.md` with the same repository guardrail.
- Updated `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md` to define Swimm authority and completion evidence.
- Updated `.swm/system-map.ovnldklv.sw.md` with the active V3 processing stage,
  occurrence-preservation contract, and legacy V1/V2 boundaries.
- `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
