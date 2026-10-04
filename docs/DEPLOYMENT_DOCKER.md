# Docker deployment guide

This optional Docker Compose setup runs the existing FastAPI application with a
local PostgreSQL 16 database containing pgvector. It does not change application
behavior or initialize a production deployment.

## Prerequisites and build

Install Docker Engine and the Docker Compose plugin. Build from the repository
root:

```sh
docker compose build
```

The multi-stage `Dockerfile` installs the existing `requirements.txt` in its
builder stage and runs the app as an unprivileged user in the runtime stage. The
requirements include the `en_core_web_md` spaCy wheel hosted on GitHub Releases.
The machine or build runner therefore needs outbound HTTPS access to GitHub
during the image build so pip can download that wheel. This setup does not mirror
or replace the dependency.

## Run

Set `POSTGRES_PASSWORD` to a local-only password in the shell or a root `.env`
file, then start the services:

```sh
docker compose up -d
docker compose ps
docker compose logs -f app
```

Compose waits for PostgreSQL's `pg_isready` health check before starting the
app. The app health check requests its existing `/health` endpoint. Open
`http://localhost:${APP_PORT:-8000}`. Stop the services with
`docker compose down`; the named `postgres_data` volume keeps database files
across container recreation. `docker compose down -v` removes that volume and
its database contents.

## Configuration

Compose reads variables from the invoking environment and the root `.env` file
for interpolation. `.env` is excluded from the image build context and should
never contain committed credentials. The Compose file passes the supported
settings explicitly to the app:

| Variable | Default | Purpose |
| --- | --- | --- |
| `POSTGRES_USER` | `postgres` | Database user |
| `POSTGRES_PASSWORD` | required | Database password; set a strong value |
| `POSTGRES_DB` | `caselibrary` | Database name |
| `POSTGRES_PORT` | `5432` | Host port for PostgreSQL |
| `PORT` | `8000` | App's listening port inside its container |
| `APP_PORT` | `8000` | Host port mapped to the app |
| `CASELIBRARY_ACCESS_PASSWORD` | empty | Optional app access password |
| `CASELIBRARY_SESSION_SECRET` | empty | Optional session-signing secret |
| `CASELIBRARY_SESSION_SECONDS` | `86400` | Access-session lifetime |
| `OPENAI_API_KEY`, `OPENAI_ORG_ID` | empty | Optional OpenAI credentials |
| `OPENAI_MODEL` | `gpt-4o` | OpenAI model setting |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` | Embedding model setting |
| `ANTHROPIC_API_KEY` | empty | Optional Anthropic credential |
| `ANTHROPIC_MODEL` | `claude-3-5-sonnet-20241022` | Anthropic model setting |
| `CANLII_API_KEY` | empty | Optional CanLII credential |
| `LOG_LEVEL` | `INFO` | Application logging level |

The app connects to the Compose database using `POSTGRES_HOST=db` and port
`5432` on the internal network. `POSTGRES_PORT` controls the published host
port, which is bound to loopback only. Defaults are for local use, not a public
or production deployment.

## Scope and deployment boundary

This container setup is an optional reproducible run path. **It does not replace
or alter the live PC `iLitSite` scheduled-task deployment.** Existing scheduled
tasks, production data, ingestion, and the live deployment remain outside this
Compose stack.

The GitHub Actions workflow at
`.github/workflows/docker-build.yml` performs a build-only check with image
push disabled. It is configured with `continue-on-error: true`. No Docker image
build or container startup is claimed as a local validation for this change.
