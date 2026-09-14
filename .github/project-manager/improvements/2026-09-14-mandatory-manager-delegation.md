# Mandatory Manager Delegation

## Observed issue

The project-manager prompt described delegation but allowed the manager to use
direct tools first and to decide that delegation overhead exceeded the work. In
practice, multi-step citation investigations were completed directly, which
made the manager behave like an implementer rather than a coordinator.

## Evidence

The workspace contains both `project-manager.agent.md` and
`managed-worker.agent.md`, but the manager contract did not require a delegated
phase for strategic or multi-step work. The citation investigation involved
multiple probes, implementation decisions, and validation before delegation
was used consistently.

## Proposed change

Require delegation for strategic, open-ended, multi-step, or cross-surface work
when the managed worker is available. Permit direct execution only for tiny
one-step operations, manager synthesis, final acceptance validation, or bounded
worker-failure recovery. Require the exception to be recorded in task evidence.

## Expected value and risk

This makes the manager/worker boundary observable and prevents duplicated
discovery. The risk is unnecessary delegation for small tasks, bounded by the
explicit tiny-operation exception and structured worker return contract.

## Decision

Adopted on 2026-09-14 in the workspace project-manager agent, managed-task
prompt, and coding instructions.