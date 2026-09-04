# Task: Strengthen Cost-Aware Delegation Policy

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Make the project-manager agent a coordinator by routing eligible grunt work to the lowest-cost capable delegated agent.
Why now: The manager prompt describes cost awareness but does not clearly make delegation the default for bounded discovery, inventory, mechanical analysis, or routine validation.
Owner surface: `.github/agents/project-manager.agent.md`
Dependencies: Available agent/delegation tools and repository ownership boundaries
Risk boundary: Delegation must not transfer accountability for product decisions, security, secrets, irreversible operations, evidence interpretation, or final acceptance. Platform model availability remains external.
Smallest falsifiable check: Verify the prompt contains an explicit delegation hierarchy, coordinator responsibilities, and exceptions for direct execution.
Acceptance criteria: The manager routes eligible grunt work to the cheapest capable agent, requests structured evidence, synthesizes results, and performs final validation; it does not pretend to control unavailable platform model routing.
Docs/generated references: `.github/agents/project-manager.agent.md`, `.github/project-manager/improvements/README.md`
Rollback/recovery: Revert the prompt-only policy addition if delegation adds overhead or weakens evidence quality.
Evidence: Added `Delegation And Coordination` to `.github/agents/project-manager.agent.md` with a three-level routing hierarchy: direct tools for tiny work, the lowest-cost capable delegate for bounded grunt work, and stronger delegation only for difficult synthesis. The policy requires structured delegated returns, bounded scope, manager-owned decisions and final validation, and honest reporting of platform model availability. Prompt marker validation and `git diff --check` passed.
