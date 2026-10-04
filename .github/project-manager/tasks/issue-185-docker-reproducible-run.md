# Task: Issue #185 reproducible Docker run

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add a Dockerfile, Compose setup, build-only CI workflow, deployment guide, and focused dockerignore test for a reproducible local run.

Why now: Provide an isolated, repeatable container run path without changing application behavior or the existing live PC deployment.

Owner surface: New Docker packaging and local container deployment documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `requirements.txt`, `/health`, and `POSTGRES_*` configuration; no database operation or local image build.

Risk boundary: New files only. Do not change application code, dependencies, `.env`, database state, deploy scripts, or existing documentation/workflows/tests. The live PC `iLitSite` scheduled-task deployment remains unchanged. Do not build Docker locally.

Smallest falsifiable check: `python tests/test_dockerignore.py`

Acceptance criteria:

- A multi-stage Python 3.12 slim image installs `requirements.txt`, runs Uvicorn without reload on `0.0.0.0:$PORT`, and uses a non-root runtime user.
- Compose defines the app and `pgvector/pgvector:pg16`, waits for database health, uses environment-driven configuration, checks app `/health`, and persists database files.
- `.dockerignore` excludes the requested secrets, data, dump, venv, and cache paths; a focused test confirms `.env`.
- New deployment documentation covers build/run, environment variables, the spaCy wheel's outbound GitHub requirement, and the existing live deployment boundary.
- A new build-only GitHub Actions workflow does not push and uses `continue-on-error: true`.
- Focused checks pass; Docker is not run locally.

Harness criteria: Focused dockerignore test passes; generated-doc check is attempted and any environment blocker is recorded; `git diff --check` passes.

Docs/generated references: New `docs/DEPLOYMENT_DOCKER.md` and new `.swm/docker-deployment.sw.md`; no generated references should change.

Rollback/recovery: Remove only the new files from this task; no image, container, volume, database, or production state is created.

Evidence: Delegated worker created the requested six owner-surface files; manager review corrected the runtime port handling, health-check utility, and documentation accuracy. Added new Swimm walkthrough `.swm/docker-deployment.sw.md` and canonical guide `docs/DEPLOYMENT_DOCKER.md`; no existing repository files were changed. `python tests/test_dockerignore.py` passed (1 test), static acceptance-marker check passed (12 checks), and `git diff --check` passed. `python scripts/check_generated_docs.py` was attempted but could not run its API/schema generators because this environment lacks `fastapi` and `sqlalchemy`; generated-reference status remains unverified. `python -m pytest -q tests/test_dockerignore.py` was also attempted but pytest is not installed. No Docker build or container run was performed.

Files changed: `.dockerignore`, `.github/project-manager/tasks/issue-185-docker-reproducible-run.md`, `.github/workflows/docker-build.yml`, `.swm/docker-deployment.sw.md`, `Dockerfile`, `docker-compose.yml`, `docs/DEPLOYMENT_DOCKER.md`, `tests/test_dockerignore.py`.
Delegated work: `managed-worker` created Dockerfile, Compose, dockerignore, build-only workflow, deployment guide, and focused test; it returned the required structured report. Manager reviewed all deliverables, made local owner-surface corrections, added the Swimm walkthrough, and owns final acceptance.
Focused validation: `python tests/test_dockerignore.py` passed (1 test); static Docker acceptance-marker check passed (12 checks); `git diff --check` passed.
Residual risk: The generated-doc check is blocked by missing `fastapi` and `sqlalchemy`; its generators could not assess drift. Docker image build and container startup remain unverified by instruction.
Next bounded task: Review the non-blocking GitHub Docker build result after CI runs.

## Hypothesis

If the new packaging files preserve the current `/health` and `POSTGRES_*` contracts, the focused `.dockerignore` test will pass without modifying existing files.

## Plan

1. Delegate creation of the new packaging, workflow, documentation, and test files.
2. Add a new Swimm walkthrough and review the delivered artifacts.
3. Run the focused test, attempt the generated-doc check, run whitespace validation, and record evidence.

## Execution Checkpoints

- Delegation: Managed worker returned the required structured report and created six new implementation files.
- Implementation: Manager review corrected Docker port binding and health checks; static requirements check passed.
- Documentation: `docs/DEPLOYMENT_DOCKER.md` and `.swm/docker-deployment.sw.md` added as new files.
- Recovery: No runtime state created.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #185 requests a bounded, new-files-only Docker run path. | Existing `/health`, database configuration, dependency source, and Swimm map inventory inspected. |

## Completion

Completion recorded: yes

Summary: Added the new Docker/Compose local run path, build-only non-blocking workflow, focused build-context test, deployment guide, and Swimm walkthrough. All changes are new files; application code, dependencies, existing documentation, and deployment scripts were not altered.

Validation: `python tests/test_dockerignore.py` passed (1 test); 12 static acceptance checks passed; `git diff --check` passed. `python scripts/check_generated_docs.py` was attempted but failed to import unavailable `fastapi` and `sqlalchemy`; pytest is also unavailable. Docker was not run.

Residual risk: Generated references could not be checked in this environment; Docker build/runtime remain unverified as requested.

Next recommended task: Review the non-blocking GitHub Docker build result after CI runs.
