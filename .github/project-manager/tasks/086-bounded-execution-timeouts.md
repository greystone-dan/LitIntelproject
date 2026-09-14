# Task: Enforce bounded execution timeouts

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Ensure managed investigations, smoke tests, diagnostics, and subprocess-backed operations cannot hang the manager session indefinitely.

Why now: Website validation and case-name diagnostics exposed inconsistent timeout enforcement. A worker review could inspect code, but a runtime probe still timed out or was cancelled without a uniform recovery boundary.

Owner surface: Project-manager execution workflow and repository-local execution harness

Commit allowed: yes

Push allowed: yes

Dependencies: `scripts/agent_harness.py`, `scripts/agent_policy.py`, managed-worker/project-manager instructions, and existing bounded operational scripts.

Risk boundary: Do not terminate unrelated user processes or database writers. Timeout changes must fail closed, preserve logs/state, and leave resumable operations recoverable.

Smallest falsifiable check: bounded harness command test proving a timed-out subprocess records evidence and returns control, plus focused manager workflow validation.

Acceptance criteria:

- Managed worker and manager instructions require hard timeouts for every command that can block.
- Long-running commands require an explicit bounded watchdog, checkpoint, and recovery command.
- Repository-local harness records timeout status and output without hanging.
- Website/browser smoke and diagnostics use bounded execution windows.
- No unrelated process is terminated by timeout handling.

Docs/generated references: `.github/agents/project-manager.agent.md`, `.github/agents/managed-worker.agent.md`, `.github/prompts/managed-task.prompt.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`

Rollback/recovery: Revert only timeout-policy/harness changes if focused tests fail. Existing run state and logs remain authoritative; do not kill or reset unrelated processes.

Evidence: Pending delegated timeout-control audit.

## Hypothesis

If timeout requirements are explicit in both manager and worker contracts and the local harness records `TimeoutExpired` as recoverable evidence, stalled diagnostics will return control without obscuring the failure.

## Plan

1. Delegate a bounded read-only timeout-control audit.
2. Implement the smallest harness/instruction changes.
3. Run focused timeout and manager tests, then update workflow documentation.

## Execution Checkpoints

- Delegation: pending bounded audit of timeout-capable code and instructions.
- Implementation: manager-owned workflow/harness changes only.
- Documentation: project-manager instructions and Swimm transition walkthrough.
- Recovery: preserve run logs/state; no process termination beyond the explicitly owned command.

## Completion

Completion recorded: no

Summary: In progress.

Validation: Pending.

Residual risk: Native tool-level cancellation may still be outside repository control; repository commands will have explicit watchdogs where possible.

Next recommended task: Pending audit findings.
