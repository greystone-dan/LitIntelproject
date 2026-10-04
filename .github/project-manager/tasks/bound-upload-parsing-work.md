# Task: Bound upload size and parsing work

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Bound upload reads and parser work for memo check, Live Analysis, and de-identification.

Why now: Unbounded upload reads and expanded-document parsing can consume excessive memory or CPU in ephemeral document workflows.

Owner surface: Backend ephemeral upload parsing and its focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: FastAPI upload routes, DOCX/PDF parsers; no database or deployment work.

Risk boundary: Preserve normal document behavior and ephemeral/no-write semantics; do not access the database, deploy, inspect `.env`, or modify unrelated working-tree content.

Smallest falsifiable check: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py tests/test_memo_citation_check.py`

Acceptance criteria:

- Centralized upload/parser limits support environment overrides.
- Upload bytes are read incrementally and requests exceeding the configured limit return HTTP 413 across memo check, Live Analysis, and de-identification.
- DOCX expanded size and archive entry count, PDF page count, and extracted text length are bounded with clear errors.
- Focused tests cover oversized uploads, a generated zip-bomb-like DOCX, a many-page PDF, and normal behavior.
- Canonical documentation and the relevant Swimm walkthrough describe the new limits; generated references are regenerated if `backend/routes.py` changes.
- Run focused checks, `python -m pytest -q`, and `python scripts/check_generated_docs.py`; record failures honestly.

Harness criteria:
- Focused upload/parser tests pass.
- Full pytest and generated-document checks are recorded.
- Canonical and Swimm documentation paths are included in evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/reports/privacy-security-review.md`, `.swm/1.oi7rhqp2.sw.md`, and regenerated API reference.

Rollback/recovery: Revert only the upload-limit implementation/tests/docs; no persistent data is changed.

Evidence: Delegated implementation completed and reviewed. Canonical behavior is documented in `SYSTEM_REFERENCE.md` and `docs/reports/privacy-security-review.md`; the relevant Swimm route walkthrough is `.swm/1.oi7rhqp2.sw.md`. Focused and full pytest commands were attempted but could not start because pytest is not installed. API-reference generation and the generated-doc check were attempted but could not run because FastAPI and SQLAlchemy are not installed. `git diff --check`, Python compilation, and the changed-file high-confidence secret scan passed.

Files changed: `.github/project-manager/tasks/bound-upload-parsing-work.md`, `backend/resource_limits.py`, `backend/routes.py`, `backend/live_analysis.py`, `backend/deidentify.py`, `tests/test_live_analysis.py`, `tests/test_deidentify.py`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/reports/privacy-security-review.md`, `.swm/1.oi7rhqp2.sw.md`. Generated API reference was not regenerated because its generator could not import FastAPI.
Delegated work: `managed-worker` implemented the backend limits and tests; its structured result is recorded in the work session. Manager reviewed the changes and added the de-identification DOCX-output text cap plus route test.
Focused validation: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py tests/test_memo_citation_check.py` — blocked: `/usr/bin/python: No module named pytest`. `python -m py_compile backend/resource_limits.py backend/routes.py backend/live_analysis.py backend/deidentify.py tests/test_live_analysis.py tests/test_deidentify.py` — passed. `git diff --check` — passed.
Residual risk: Runtime tests are unverified; generated API reference and generated-doc consistency remain unverified due missing dependencies. Multipart parsing may spool request bytes before route-level bounded reads, and parser CPU/memory isolation is not implemented.
Next bounded task: In the repository's CI/dependency environment, run focused and full pytest, regenerate `docs/API_REFERENCE.generated.md`, run `python scripts/check_generated_docs.py`, then update this task record based on observed results.

## Hypothesis

If all three upload workflows share centralized bounded reads and parser guards, focused tests will demonstrate HTTP 413 at the byte cap, rejection of oversized expanded DOCX/PDF work, and unchanged normal parsing.

## Plan

1. Delegate the bounded backend implementation and focused tests.
2. Review the resulting behavior and regenerate generated references if route changes require it.
3. Update the canonical system reference and relevant Swimm walkthrough.
4. Run focused validation, full pytest, generated-doc check, and final safety checks.

## Execution Checkpoints

- Delegation: `managed-worker` changed upload/parser implementation and focused tests; structured result reports limits, behavior, commands, and pytest unavailability.
- Implementation: Route, parser, and test changes reviewed; Python compilation and whitespace checks passed.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `docs/reports/privacy-security-review.md`, and `.swm/1.oi7rhqp2.sw.md`.
- Recovery: None; no long-running or persistent operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created with upload/parser handling as one backend owner surface | Requirements span shared route-level upload enforcement and format-specific parser limits | User request; `SYSTEM_REFERENCE.md` Live Analysis section; `.swm/1.oi7rhqp2.sw.md` Live Analysis boundary |

## Completion

Completion recorded: no

Summary: Implementation and documentation are present, but acceptance is blocked pending runtime tests and generated API-documentation validation in an environment with the repository dependencies installed.

Validation: Focused pytest and `python -m pytest -q` both stopped because pytest is unavailable. `python scripts/generate_api_reference.py` and `python scripts/check_generated_docs.py` stopped because FastAPI and SQLAlchemy are unavailable. `git diff --check`, `python -m py_compile ...`, and high-confidence secret scanning passed.

Residual risk: Parser route behavior and generated-reference consistency require CI-environment validation; upstream multipart spooling and parser CPU/memory limits remain outside this change.

Next recommended task: Run the listed focused/full test and generation commands in the dependency-complete CI environment; do not mark this task complete until those results are recorded.
