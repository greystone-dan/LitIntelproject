---
name: "Managed Task"
description: "Start an evidence-backed AI CaseLibrary task through the project-manager workflow. Use for autonomous project work that needs an owner, acceptance criteria, validation, documentation, and handoff."
agent: "AI CaseLibrary Project Manager"
argument-hint: "Outcome, priority, constraints, and whether commit/push is allowed"
---

Start a managed AI CaseLibrary task for: ${input:outcome:Describe the desired outcome}

Priority and constraints: ${input:constraints:State priority, scope, approval limits, and whether commit or push is allowed}

Follow the project-manager workflow. Create a durable task record if the work is
multi-step or may span sessions. Select one owner surface, state a falsifiable
hypothesis, implement the smallest safe slice, run its focused validation, and
record evidence before reporting completion. Do not make production, security,
Government of Canada, CBSA, destructive, unbounded, or paid-operation decisions
without explicit user approval.
