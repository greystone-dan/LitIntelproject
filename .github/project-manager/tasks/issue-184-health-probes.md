# Task: Add public health probes

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add public `GET /health/live` and dependency-reporting `GET /health/ready` endpoints while preserving `GET /health` exactly.

Why now: Issue #184 requires explicit liveness/readiness signals for operators without leaking deployment or credential details.

Owner surface: `backend/health.py` plus minimal health registration/access exemptions in `backend/main.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FastAPI startup, database schema, and configured model-provider settings; all external dependencies must be mocked in tests.

Risk boundary: Preserve the existing `/health` response exactly; do not access the database or `.env`, deploy, touch deploy scripts, remove features, add dependencies, or enable the password gate. Probes must use short timeouts, disclose no secrets/hostnames/connection strings, and readiness must return 503 when any required dependency is unhealthy.

Smallest falsifiable check: Focused health-probe tests in `tests/test_api.py` (or a dedicated health test module) with mocked database/model endpoints.

Acceptance criteria:

- `GET /health/live` and `GET /health/ready` are public even when the password gate is enabled; existing `GET /health` behavior is unchanged.
- Readiness independently reports database connectivity, vector extension, required tables, and configured model endpoints; any required dependency failure yields HTTP 503 and safe output.
- Tests cover all healthy, database down, missing vector extension, and model endpoint down without contacting real services.
- Generated API docs are regenerated and `scripts/check_generated_docs.py` passes.
- Canonical documentation and the connected Swimm system-map walkthrough describe the probe behavior.

Harness criteria:

1. Focused mocked health tests pass for healthy and required failure cases.
2. Generated-doc check passes after API route regeneration.
3. Documentation names both the canonical repository document and Swimm walkthrough, and `git diff --check` passes.

Docs/generated references: `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/system-map.ovnldklv.sw.md`; regenerate API reference with its generator and verify using `scripts/check_generated_docs.py`.

Rollback/recovery: Revert the additive probe module and its route/access registration while retaining the original `/health`; regenerate the API reference from current routes.

Evidence: Managed-worker implemented the probe module, minimal route/access registration, and tests; manager reviewed the exact code and added the explicit OpenAPI 503 response. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, and `CHANGELOG.md`. Swimm walkthrough updated: `.swm/system-map.ovnldklv.sw.md`. Focused validation passed: `PYTHONPATH=/tmp/health-sitecustomize /tmp/litintel-health-venv/bin/python -m pytest -q tests/test_health.py tests/test_documentation_contracts.py` (14 passed); the sitecustomize shim disables dotenv loading, and tests mock all DB/model calls. API reference was regenerated with `PYTHONPATH=/tmp/health-sitecustomize /tmp/litintel-health-venv/bin/python scripts/generate_api_reference.py`; `PYTHONPATH=/tmp/health-sitecustomize /tmp/litintel-health-venv/bin/python scripts/check_generated_docs.py` passed (3 references current); `git diff --check` and `python -m py_compile backend/main.py backend/health.py tests/test_health.py` passed. No DB or `.env` was accessed.

Files changed: `backend/health.py`, `backend/main.py`, `tests/test_health.py`, `docs/API_REFERENCE.generated.md`, `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/system-map.ovnldklv.sw.md`, `CHANGELOG.md`, `.github/project-manager/tasks/issue-184-health-probes.md`.
Delegated work: `managed-worker` implemented the backend health probe slice and focused tests, then corrected optional model-endpoint readiness semantics after manager review. Both returns were structured; worker could not run pytest in the base interpreter, so manager prepared an isolated environment with existing project dependency versions and disabled dotenv loading.
Focused validation: 14 tests passed; API reference generation succeeded; generated-doc check passed (3 references); `git diff --check` and Python syntax compilation passed.
Residual risk: Database SQL/readiness behavior has not been exercised against a real database; all dependency calls were mocked, as required.
Next bounded task: Commit and publish the validated branch after the final fresh validation.

## Hypothesis

If the new probes report dependency health using bounded mockable checks and the access exemption includes both route paths, focused tests will demonstrate correct healthy/degraded status, redaction, and public access without changing `/health`.

## Plan

1. Run the existing focused API/health baseline and inspect current route/access behavior.
2. Implement `backend/health.py`, minimal `backend/main.py` integration, and mocked tests.
3. Regenerate API docs; update canonical docs and the Swimm system map.
4. Re-run focused tests, generated-doc validation, and diff checks; refresh `origin/main` and publish the validated task branch.

## Execution Checkpoints

- Delegation: Pending bounded managed-worker implementation and baseline-test run.
- Implementation: Pending.
- Documentation: `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, and `.swm/system-map.ovnldklv.sw.md`.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created; assign backend implementation and tests to managed-worker | Multi-step runtime change; keep manager responsible for documentation, acceptance, Git, and final validation | Issue #184 requirements and current ownership references |

## Completion

Completion recorded: yes

Summary: Added public liveness and dependency-readiness endpoints, tests, regenerated API docs, and updated canonical/Swimm documentation.

Validation: 14 focused health/documentation tests passed; generated API reference was regenerated; `scripts/check_generated_docs.py`, `git diff --check`, and Python compilation passed. `git fetch origin main` refreshed main at `3720556` (`#180`); main is an ancestor of this branch, so no merge was required.

Residual risk: No live database or model endpoint validation was performed.

Next recommended task: Commit/publish this branch; no related follow-up is required.
