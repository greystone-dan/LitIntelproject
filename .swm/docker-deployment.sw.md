---
title: Optional Docker deployment
---

# Optional Docker deployment

This walkthrough connects the new local container run path to the existing
application and database boundaries. It is not the production deployment
procedure.

## Flow and owners

```mermaid
flowchart LR
    Compose[docker-compose.yml] --> App[Dockerfile / backend.main:app]
    Compose --> DB[pgvector/pgvector:pg16]
    App -->|POSTGRES_* via Compose network| DB
    App --> Health[/health]
    DB --> Volume[(postgres_data)]
```

- [`Dockerfile`](../Dockerfile) builds from Python 3.12 slim, installs the
  repository's existing [`requirements.txt`](../requirements.txt), and runs
  Uvicorn as a non-root user without reload.
- [`docker-compose.yml`](../docker-compose.yml) defines the app and pgvector
  database, waits for the database health check, and retains database files in
  a named volume. The app health check uses the existing `/health` route in
  [`backend/main.py`](../backend/main.py).
- [`.dockerignore`](../.dockerignore) keeps local secrets, caches, evaluation
  data, and database dumps out of the build context.
- [`docs/DEPLOYMENT_DOCKER.md`](../docs/DEPLOYMENT_DOCKER.md) is the executable
  operator-facing guide for build, configuration, run, and teardown.
- [`.github/workflows/docker-build.yml`](../.github/workflows/docker-build.yml)
  is build-only: it does not push an image and is non-blocking.

## Invariants and failure boundaries

- The Docker build uses the existing dependency manifest unchanged. The spaCy
  model wheel comes from GitHub Releases, so image builds need outbound HTTPS
  access to GitHub.
- Database configuration is container-specific (`POSTGRES_HOST=db`) and
  preserves the existing `POSTGRES_*` configuration contract.
- `/health` is the current health endpoint; do not substitute `/health/ready`.
- The image workflow does not publish a registry artifact. Docker build and
  runtime behavior must be checked in an environment with Docker; the manager
  intentionally does not build locally for this task.
- This optional setup does not replace, migrate, or modify the live PC
  `iLitSite` scheduled-task deployment.

## Narrow validation

Run `python tests/test_dockerignore.py` to verify the key build-context
exclusion using the standard library. In the project test environment, the same
`unittest.TestCase` is also discoverable by pytest. Run
`python scripts/check_generated_docs.py` and
`git diff --check` for documentation consistency and patch formatting. Docker
builds and container startup are separate checks, not covered by these
commands.
