# Task: Add opt-in response security headers

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #170's opt-in response security headers and explain operation.

Why now: Add defense-in-depth headers without changing existing access, no-index, caching, audit, or response-body behavior.

Owner surface: Backend response middleware (`backend/security_headers.py`, minimal registration in `backend/main.py`, and focused tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Starlette/FastAPI runtime and issue #112 findings; no new dependencies.

Risk boundary: Preserve existing route-set headers, access/password gate, no-index, no-cache, audit behavior, and streaming responses. Headers default off. Never read `.env`, access a database, or deploy.

Smallest falsifiable check: `python -m pytest -q tests/test_security_headers.py` (Python 3.12.3 is available; Starlette, FastAPI, and pytest are not installed in the default interpreter at task start).

Acceptance criteria:

- An opt-in pure-ASGI middleware applies the requested headers and safe HSTS/CSP configuration without replacing existing headers or consuming streaming bodies.
- Middleware registration order is tested alongside access/no-index and audit middleware.
- Focused tests cover default passthrough, enabled headers, HTTPS and forwarded-proto HSTS, preservation, streaming, and registration/order.
- Activation, report-only review, CSP origin derivation, and untested enforcement mode are documented.
- Canonical and Swimm documentation are updated and documentation checks pass.

Harness criteria:

- Backend middleware behavior and ordering are covered by focused tests.
- Required configuration and CSP operations are documented.
- Canonical and Swimm documentation are updated.

Docs/generated references: `docs/SECURITY_HEADERS.md`, `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, and `.swm/1.oi7rhqp2.sw.md`.

Rollback/recovery: Remove the middleware registration and new middleware/test/docs changes; default-off configuration means deployments remain unchanged unless explicitly enabled.

Evidence: Managed worker added the backend middleware, registration, and focused tests; manager reviewed them and added no-cache/password-gate assertions. Updated `docs/SECURITY_HEADERS.md`, `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, and `.swm/1.oi7rhqp2.sw.md`. `python -m py_compile backend/main.py backend/security_headers.py tests/test_security_headers.py`, `git diff --check`, a standalone ASGI smoke check for passthrough/headers/HSTS/header preservation/streaming, and checks of the newly added local links passed. Final `python -m pytest -q tests/test_security_headers.py` could not run because pytest is absent. `python scripts/check_generated_docs.py` exited 1 because its API/schema generators cannot import missing FastAPI and SQLAlchemy; no dependency installation or generated-file edits were made. `git fetch origin main` refreshed origin/main at `95dd903`; it is already an ancestor of HEAD, so no merge was needed. No `.env`, database, or deployment access.

Files changed: `backend/security_headers.py`, `backend/main.py`, `tests/test_security_headers.py`, `docs/SECURITY_HEADERS.md`, `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `.swm/1.oi7rhqp2.sw.md`, and this task record.
Delegated work: Managed worker implemented middleware, minimal registration, and tests. Structured return reported files inspected/changed, commands, results, missing runtime test dependencies, and recommendation to validate in a provisioned environment.
Focused validation: Syntax, whitespace, standalone ASGI smoke, and added-link checks passed. Focused pytest and generated-doc checks remain blocked by missing Python packages.
Residual risk: Committed pytest cases, integration middleware order, and generated API/schema doc synchronization have not executed. CSP enforcement mode is intentionally documented as untested.
Next bounded task: In an environment with the project's existing FastAPI, Starlette, SQLAlchemy, and pytest dependencies, run the focused test and generated-document checks; make no policy changes unless those checks expose a defect.

## Hypothesis

If middleware applies headers only when opted in and runs outside existing access/no-index and audit handling, focused ASGI tests will show that it preserves route headers, streams, and HTTPS-aware policy while default requests pass through unchanged.

## Plan

1. Delegate the backend middleware, minimal registration, and focused tests as one bounded implementation slice.
2. Independently review the implementation, then document configuration and CSP report review in the requested canonical and Swimm documents.
3. Run focused tests, generated-document checks, link review, and `git diff --check`; refresh origin/main near completion.

## Execution Checkpoints

- Delegation: Managed worker completed the backend middleware, registration, and tests; manager reviewed the slice.
- Implementation: `backend/security_headers.py`, `backend/main.py`, and `tests/test_security_headers.py`; syntax passed, but pytest was unavailable.
- Documentation: Updated `docs/SECURITY_HEADERS.md`, `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, and `.swm/1.oi7rhqp2.sw.md`; new local links resolve.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue requires coordinated implementation, focused tests, and multiple documentation updates. | Read `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, transition guide, and the specified Swimm walkthrough. |
| 2026-10-04 | Marked blocked after implementation | Code and documentation are ready, but required test and generated-doc checks cannot run without project dependencies. | `python -m pytest -q tests/test_security_headers.py` reports no pytest; `python scripts/check_generated_docs.py` cannot import FastAPI and SQLAlchemy. |

## Completion

Completion recorded: no

Summary: Middleware, tests, and documentation are implemented. Acceptance remains blocked on running focused tests and generated documentation checks with existing project dependencies.

Validation: `python -m py_compile backend/main.py backend/security_headers.py tests/test_security_headers.py`, `git diff --check`, standalone ASGI smoke, and added local-link checks passed. Focused pytest and `scripts/check_generated_docs.py` were attempted and blocked by missing dependencies.

Residual risk: No pytest integration result or successful generated-doc check; CSP enforcement remains explicitly untested.

Next recommended task: Run focused pytest and generated-doc checks in a provisioned project environment.
