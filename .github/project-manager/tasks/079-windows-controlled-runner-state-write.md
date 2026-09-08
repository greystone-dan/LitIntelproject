# Windows Controlled Runner State Write

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Make controlled citation-rebuild state checkpoints durable on Windows so a bounded dry-run and approved future canary can progress without `PermissionError` during atomic state replacement.

Why now: The all-case citation refresh remains paused after 1,295 cases because the runner failed replacing `state.json`; extraction rules are now validated, but a safe resume requires reliable checkpoint persistence.

Owner surface: `scripts/rebuild_citations_controlled.py` and `scripts/run_overnight.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing paused artifacts under `data/overnight_runs/citation-extraction-all-20260907`, runner tests or local helpers, `OVERNIGHT.md`, and the operational Swimm walkthrough.

Risk boundary: Do not modify or resume the paused run, overwrite its artifacts, write citations, resolve targets, or compute metrics. Preserve atomicity and recovery guarantees for a fresh bounded dry-run only.

Smallest falsifiable check: A fresh explicit one-case dry-run writes and replaces state checkpoints on Windows without error and leaves the database unchanged.

Acceptance criteria:

- State writes tolerate Windows file-handle behavior without replacing a valid state file with partial JSON.
- A fresh one-case dry-run reaches a terminal state with readable state/baseline/comparison artifacts.
- No citations, targets, or metrics are written.
- Operational documentation and the operations Swimm walkthrough record the validated recovery command.

Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/7.7le8istr.sw.md`; generated references are not affected.

Rollback/recovery: Revert the local state-write helper if the bounded dry-run fails. Retain the paused run directory untouched and use a new run directory for all validation.

Evidence: The all-case attempt reproduced `PermissionError: [WinError 5]` after the original three 50 ms atomic-replace attempts. The generic atomic writer now retries with capped backoff for up to 30 seconds. The controlled runner appends `case-checkpoints.jsonl` after each committed case and rewrites `state.json` only every ten cases. Resume can bootstrap the legacy stopped run from comparison evidence: `recoverable_cases=594`, `recoverable_citations=10152`, `next_case_id=641`. Focused validation: `python -m pytest tests/test_rebuild_citations_controlled.py tests/test_run_overnight.py -q` -> `13 passed`. No citation writer was started during repair. Documentation checkpoint: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If the runner closes and retries the temporary state file replacement using a Windows-compatible atomic replace path, a fresh bounded dry-run will persist valid checkpoints without changing database citation rows.

## Plan

1. Inspect the current state-write helper and focused operational tests.
2. Make the smallest Windows-compatible state-write repair and run its narrow check.
3. Run a fresh explicit one-case dry-run and document the recovery evidence.

## Execution Checkpoints

- Delegation: Read-only runner/helper inventory with structured evidence.
- Implementation: `scripts/rebuild_citations_controlled.py` and focused tests if present.
- Documentation: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/7.7le8istr.sw.md`.
- Recovery: New run directory only; the paused all-case directory remains immutable.

## Completion

Completion recorded: yes

Summary: Per-case progress is append-only, large state snapshots occur every ten cases, and transient Windows replacement locks retry for up to 30 seconds.

Validation: `13 passed`; stopped-run cursor recovered read-only at 594 cases and 10,152 citations.

Residual risk: A persistent lock beyond 30 seconds still stops fail-closed; running outside a synchronized directory remains the stronger isolation option if locks recur.

Next recommended task: Resume the stopped all-case run only after explicit approval and visible-terminal confirmation.