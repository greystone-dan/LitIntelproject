# Task: Managed worker and evidence gate

Status: complete
Created: 2026-09-05
Updated: 2026-09-05

Task: Complete the next harness slice with a restricted managed worker and deterministic completion evidence gate.
Why now: The manager harness had durable state and policy decisions but lacked a worker role definition and executable completion gate.
Owner surface: `.github/agents/managed-worker.agent.md`, `scripts/evidence_gate.py`, focused harness tests, and documentation.
Dependencies: `scripts/agent_harness.py`, managed-task prompt, task records, Swimm checkpoint.
Risk boundary: Worker cannot edit task records, commit, push, or run destructive/production operations. The evidence gate validates records but does not itself authorize external or destructive operations.
Smallest falsifiable check: End-to-end harness run creates state/events, records a command, transitions complete, and the evidence gate accepts required canonical/Swimm paths.
Acceptance criteria: Restricted worker agent exists; evidence gate rejects incomplete state and accepts fresh complete evidence; docs identify both; no live pipeline process is interrupted.
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.github/agents/managed-worker.agent.md`.
Rollback/recovery: Remove worker/evidence-gate scripts and revert documentation; no runtime or database changes.
Evidence:
- Added `.github/agents/managed-worker.agent.md` with bounded owner-surface, no-task-state, no-Git-authority rules.
- Added `scripts/evidence_gate.py` and `tests/test_evidence_gate.py`.
- Harness/evidence tests passed: `7 passed`.
- End-to-end run lifecycle passed with one recorded command and evidence gate `ok=true`.
- No live extraction pipeline process was interrupted.
- Updated canonical system and Swimm transition docs.
Status: complete
Commit allowed: yes
Push allowed: yes
