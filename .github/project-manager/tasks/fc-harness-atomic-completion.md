# Task: Atomic managed-task completion gates

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

Task: Make managed-task completion atomic, evidence-gated, and validation-aware.
Why now: The current harness enforces phase order but can mark a run complete before the separate evidence gate is run, and it permits failed validation evidence.
Owner surface: `scripts/agent_harness.py`, `scripts/evidence_gate.py`, focused harness tests, and managed-task documentation.
Commit allowed: yes
Push allowed: yes
Dependencies: Existing harness state format, evidence gate, task records, and manager workflow.
Risk boundary: Control-plane only. No application, database, production, security, external, paid, destructive, or source-data operations.
Smallest falsifiable check: A completion transition with missing task evidence, missing docs, or failed validation must fail without changing state; a fully evidenced validating run must complete.
Acceptance criteria:
- Completion invokes evidence validation before writing terminal state.
- Task record and required documentation paths are stored with the run.
- Failed validation commands cannot support completion.
- Terminal runs cannot transition into repair phases under the same run ID.
- Focused tests and documentation pass.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; `.swm/11.nf15c1hd.sw.md`; no generated references.
Rollback/recovery: Revert only harness, tests, task template/prompt, and documentation changes from this task. Existing run state remains readable.
Evidence: Explore completed a bounded read-only compatibility review. Implemented
atomic prospective-state completion validation, persisted task-record and
required-document configuration, phase-aware command evidence, and failed
validation blocking. The completion path validates before writing terminal
state; failed completion leaves the run in its prior phase. Updated the managed
task prompt, project-manager README, canonical transition documentation,
system reference, and Swimm walkthrough.

Files changed: `scripts/agent_harness.py`, `scripts/evidence_gate.py`,
`tests/test_agent_harness.py`, `tests/test_evidence_gate.py`,
`.github/prompts/managed-task.prompt.md`, `.github/project-manager/README.md`,
`docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `SYSTEM_REFERENCE.md`,
`.swm/11.nf15c1hd.sw.md`, this task record.
Delegated work: Explore reviewed the completion API/state design; no files changed.
Focused validation: `pytest tests/test_agent_harness.py tests/test_evidence_gate.py -q` passed 10 tests; both control-plane scripts compiled; `git diff --check` passed.
Residual risk: Acceptance criteria remain prose and are not individually machine-evaluated; old runs without persisted task-record paths require migration or a new run to use automatic completion validation.
Next bounded task: Add structured acceptance-criterion results to run state.

Completion recorded: yes
Summary: Managed-task completion is now atomic, evidence-gated, and validation-aware.
Validation: 10 focused tests passed, compilation passed, and diff whitespace check passed.
Residual risk: Acceptance criteria still need structured per-criterion results for full machine enforcement.
Next recommended task: Add structured acceptance-criterion results to run state.
