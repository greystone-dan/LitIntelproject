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

## Autonomous execution contract

Treat this as an execution handoff, not a request for a plan-only response.
After recording the task, continue through the full loop without asking for
routine confirmation or status approval:

1. Read the required authority docs and local owner/test surface.
2. Write the hypothesis, acceptance criteria, rollback, and focused check into
	the task record.
	Declare the same acceptance criteria when creating the harness run and record
	each result with the harness `criterion` action; completion requires every
	declared criterion to be explicitly passed.
3. For every multi-step, strategic, open-ended, or cross-surface task, enter a
	delegated phase before manager implementation. Assign the smallest bounded
	worker slice and require the exact structured delegated return below. Skip
	delegation only for a genuinely tiny one-step operation and record that
	exception in the task evidence.
4. Implement the smallest safe slice and immediately run the focused check.
5. Repair local failures and rerun the same check before widening scope.
6. Update the canonical repository document and relevant Swimm walkthrough in
	the same checkpoint.
7. Continue to adjacent acceptance criteria, tests, and documentation until the
	task is complete, blocked, or explicitly deferred.

Do not stop after planning, a proposal, a first edit, a dry run, or a partial
delegated report when the task can continue safely. Do not send progress questions
between phases. Send concise progress updates only at meaningful checkpoints or
when a real approval boundary/blocker is reached. Long-running commands may run
under bounded watchdogs, but they must leave state, logs, and a recovery command.

Completion is forbidden until the task record names: files changed, delegated
work, commands actually run, focused validation results, canonical documentation
path, Swimm walkthrough path, residual risk, and the next bounded task.
Use the task-record labels `Files changed:`, `Delegated work:`,
`Focused validation:`, `Residual risk:`, and `Next bounded task:` so the
repository evidence gate can verify the completion contract. Before reporting
completion, run `scripts/evidence_gate.py` against the terminal run state and
task record; if it fails, repair the same task and rerun the gate. New runs
must be created with the task record and required documentation paths so the
harness performs this check automatically before changing state to `complete`.
A managed run must not transition directly from planning to `complete`.
Declare criteria with repeated `--criterion` options and record each result with
`scripts/agent_harness.py criterion RUN_DIR INDEX true`; missing, false, extra,
or invalidly linked results block completion.

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
