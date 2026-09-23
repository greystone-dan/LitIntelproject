# Resumable Discussion Unit runner

Status: complete
Created: 2026-09-23
Updated: 2026-09-23

Task: Make bounded Discussion Unit cohort runs resumable and visually reviewable without resending completed cases. Preserve per-case request, result, Markdown, and raw-response artifacts while adding a durable case ledger and explicit retry behavior.

Why now: Prior experiments had malformed responses and manual reruns. The existing single-case package preserves some artifacts but has no durable skip state, so completed cases could be resent and charged again.

Owner surface: `scripts/discussion_units_ledger.py`, `scripts/package_discussion_units_llm.py`, and `scripts/run_discussion_units_cohort.py`.

Dependencies: existing per-case deterministic report JSON, the 300/2,500 cohort CSVs, OpenAI configuration only when `--send` is explicitly used, and existing Markdown rendering.

Risk boundary: No database writes, no canonical publication, no automatic retry of failed cases, and no external calls during tests or dry-run. Terminal completed rows are never resent unless the ledger is deliberately removed or a future force option is added.

Smallest falsifiable check: A completed ledger row causes a second runner invocation to skip the case; a failed/malformed row remains checkpointed and is retried only with an explicit retry flag; Markdown and raw response paths remain available.

Acceptance criteria: atomic ledger writes; per-case started/completed/failed states; skip terminal cases; explicit retry-failed behavior; cohort runner with bounded case count; tests for skip/retry and malformed-response checkpointing; documentation and next-step note.

Docs/generated references: `SYSTEM_REFERENCE.md`, relevant `.swm/` walkthrough, and `docs/NEXT_STEPS.md`.

Rollback/recovery: Remove the new runner/ledger and ledger artifact; existing per-case JSON/Markdown/raw artifacts remain readable. No database rollback is needed.

Commit allowed: yes

Push allowed: yes

Evidence: Delegated audit confirmed that prior Discussion Unit artifacts preserved
raw responses and Markdown but had no durable per-case skip ledger. Added
`scripts/discussion_units_ledger.py`, integrated ledger checkpointing into
`scripts/package_discussion_units_llm.py`, and added the bounded manifest runner
`scripts/run_discussion_units_cohort.py`. Added
`tests/test_discussion_units_ledger.py`. The ledger atomically records
`started`, `complete`, and `failed`; completed rows are skipped by default and
failed rows require `--retry-failed`. Network, replay, and malformed-response
failures are checkpointed.

Validation passed: `venv\Scripts\python.exe -m pytest
tests/test_discussion_units_ledger.py tests/test_package_discussion_units_llm.py
tests/test_build_discussion_unit_priority_lists.py -q` (`9 passed`), direct
`--help` for both new/updated CLIs, `py_compile`, and `git diff --check`.
Updated `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and created
`docs/NEXT_STEPS.md`. No external model call or database write occurred.

Residual risk: the 300-case manifest and model run have not been launched. The
next bounded task is to generate/verify that manifest, run a no-network prepare
pass, then execute the 300-case hybrid run with a fresh ledger and review its
Markdown/error artifacts before expanding.
