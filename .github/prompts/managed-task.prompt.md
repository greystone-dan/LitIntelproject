---
name: "Managed Task"
description: "Start an evidence-backed AI CaseLibrary task through the project-manager workflow. Use for autonomous project work that needs an owner, acceptance criteria, validation, documentation, and handoff."
agent: "AI CaseLibrary Project Manager"
argument-hint: "Outcome, priority, constraints, and whether commit/push is allowed"
---

Start a managed AI CaseLibrary task for: ${input:outcome:Describe the desired outcome}

Priority and constraints: ${input:constraints:State priority, scope, and approval limits}

Commit allowed: ${input:commit_allowed:yes}

Push allowed: ${input:push_allowed:yes}

Follow the project-manager workflow. Create a durable task record if the work is
multi-step or may span sessions. Select one owner surface, state a falsifiable
hypothesis, implement the smallest safe slice, run its focused validation, and
record evidence before reporting completion. Do not make production, security,
Government of Canada, CBSA, destructive, unbounded, or paid-operation decisions
without explicit user approval.

Delegated returns must use exactly this schema:

```text
Files inspected:
Files changed:
Commands run:
Results:
Failures:
Uncertainty:
Recommendation:
```

Task records are manager-owned; delegated agents must not create, update, or
finalize them.
