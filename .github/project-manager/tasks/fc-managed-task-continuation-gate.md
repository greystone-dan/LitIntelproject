# Task: Managed-task continuation gate

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

Task: Prevent managed tasks from reporting completion after only a bounded slice when acceptance work remains.
Why now: The prompt required autonomous continuation, but the executable harness accepted empty evidence and direct planned-to-complete transitions.
Owner surface: `scripts/agent_harness.py`, `scripts/evidence_gate.py`, and managed-task workflow documentation/tests.
Commit allowed: yes
Push allowed: yes
Dependencies: Managed-task prompt, task template, project-manager README, existing harness state files.
Risk boundary: Control-plane and documentation behavior only. No application, database, production, security, paid-operation, or external-source changes.
Smallest falsifiable check: Focused harness tests must reject direct `planned -> complete` transitions and incomplete completion evidence while accepting a validated run with structured task markers.
Acceptance criteria:
- Completion requires a validating or documenting predecessor phase.
- Completion evidence requires commands, evidence, required docs, and structured task markers for files, delegation, validation, residual risk, and next bounded task.
- Prompt, task template, README, canonical transition documentation, and Swimm walkthrough describe the executable gate.
- Focused harness tests pass.
Docs/generated references: `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; `SYSTEM_REFERENCE.md`; `.swm/11.nf15c1hd.sw.md`; no generated references.
Rollback/recovery: Revert only the harness, tests, prompt/template, and documentation changes from this task; existing run state remains readable.
Evidence: Delegated Explore review inspected the managed-task prompt, project-manager agent, harness scripts, evidence gate, task template, task records 054-056, and harness tests. It identified missing enforcement for next bounded task, structured completion evidence, and phase progression. Implemented executable gates and regression tests. Focused validation passed: `pytest tests/test_evidence_gate.py tests/test_agent_harness.py -q` with 8 passed.

Files changed: `scripts/agent_harness.py`, `scripts/evidence_gate.py`, `tests/test_agent_harness.py`, `tests/test_evidence_gate.py`, `.github/prompts/managed-task.prompt.md`, `.github/project-manager/TASK_TEMPLATE.md`, `.github/project-manager/README.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `SYSTEM_REFERENCE.md`, `.swm/11.nf15c1hd.sw.md`, this task record.
Delegated work: Explore performed bounded read-only harness review; no files changed.
Focused validation: Initial focused validation `pytest tests/test_evidence_gate.py tests/test_agent_harness.py -q` passed 8 tests. Final validation `pytest tests/test_agent_harness.py tests/test_evidence_gate.py -q` passed 8 tests; `py_compile` passed for both changed scripts and `git diff --check` passed. An attempted command referenced absent `tests/test_agent_policy.py` and was corrected; no test failure occurred.
Residual risk: The gate validates required evidence labels and phase order, but does not semantically verify that every acceptance criterion is satisfied; manager review still owns product acceptance.
Next bounded task: Add structured acceptance-criterion results to run state if future managed tasks still stop with criteria pending.

Completion recorded: yes
Summary: Executable continuation and completion evidence gates now enforce the managed-task handoff contract.
Validation: 8 harness/evidence tests passed, both control-plane scripts compiled, and `git diff --check` passed.
Residual risk: Acceptance criteria remain prose and are not individually machine-evaluated.
Next recommended task: Add structured acceptance-criterion results to run state if future tasks still stop with criteria pending.
