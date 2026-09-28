# Task: Structured managed-task acceptance criteria

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

Task: Require explicit per-criterion results before managed-task completion.
Why now: The harness now gates evidence and validation, but acceptance criteria remain prose and a manager can mark a task complete without machine-readable proof that each criterion passed.
Owner surface: `scripts/agent_harness.py`, `scripts/evidence_gate.py`, focused harness tests, and managed-task documentation.
Commit allowed: yes
Push allowed: yes
Dependencies: Existing run state, completion gate, task template, managed-task prompt, and project-manager documentation.
Risk boundary: Control-plane only. No application, database, production, security, external, paid, destructive, or source-data operations.
Smallest falsifiable check: Completion must fail when any declared acceptance criterion is missing or false, and pass only when every declared criterion is true.
Acceptance criteria:
- New runs can persist named acceptance criteria and their results.
- Completion rejects missing, false, or extra criterion results.
- Existing completion evidence and validation gates remain enforced.
- Focused harness tests and documentation pass.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; `.swm/11.nf15c1hd.sw.md`; no generated references.
Rollback/recovery: Revert only harness, tests, prompt/template, and documentation changes from this task. Existing run state remains readable.
Evidence: Explore completed a bounded read-only state-schema review and
recommended ordered criteria with result objects, preserving empty criteria for
legacy runs. Implemented `criteria` and `criterion_results` in run state,
criterion recording through Python API and CLI, and completion validation for
missing, false, extra, duplicate, and invalidly linked results. Updated the
task template, managed-task prompt, project-manager README, canonical
transition documentation, system reference, and Swimm walkthrough.

Files changed: `scripts/agent_harness.py`, `scripts/evidence_gate.py`,
`tests/test_agent_harness.py`, `tests/test_evidence_gate.py`,
`.github/project-manager/TASK_TEMPLATE.md`, `.github/prompts/managed-task.prompt.md`,
`.github/project-manager/README.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`,
`SYSTEM_REFERENCE.md`, `.swm/11.nf15c1hd.sw.md`, this task record.
Delegated work: Explore reviewed the compatible state/API shape; no files changed.
Focused validation: `pytest tests/test_agent_harness.py tests/test_evidence_gate.py -q` passed 12 tests; both control-plane scripts compiled; `git diff --check` passed.
Residual risk: Criterion truth is asserted by the manager; the harness verifies completeness, booleans, indexes, and optional command references, not semantic truth. Legacy runs with no declared criteria remain compatible.
Next bounded task: Add criterion evidence references or command-to-criterion linkage beyond the optional command index.

Completion recorded: yes
Summary: Managed-task acceptance criteria are now machine-complete before terminal completion.
Validation: 12 focused tests passed, compilation passed, and diff whitespace check passed.
Residual risk: Semantic criterion truth remains manager-owned.
Next recommended task: Add richer criterion evidence references if auditability requires them.
