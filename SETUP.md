# Local Development Setup

This guide covers a minimal local developer setup. It does not provision or
protect a hosted service. See [README.md](README.md) for the short quick start,
[docs/CONFIGURATION_REFERENCE.md](docs/CONFIGURATION_REFERENCE.md) for runtime
settings, and [OVERNIGHT.md](OVERNIGHT.md) for bounded operational runs.

## Requirements

- Python 3.12 (the CI test job uses Python 3.12).
- PostgreSQL with the `pgvector` extension, configured through the local
  environment.
- Git.

Keep credentials in local environment configuration; never copy them into
tracked files. Do not read or share `.env` values as part of routine setup.

## Create an environment and install dependencies

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows, activate with `.\.venv\Scripts\Activate.ps1`. Configure a local
database URL using the documented environment-variable precedence in the
[configuration reference](docs/CONFIGURATION_REFERENCE.md); do not put a
password in a command, source file, or issue report.

## Start the application

With the local database configured and PostgreSQL running:

```bash
python -m alembic upgrade head
python -m uvicorn backend.main:app --port 8000
```

Open `http://127.0.0.1:8000/data-explorer`. The main workflow is the
Data Explorer search and inline reader. See the [research UI guide](docs/RESEARCH_UI_GUIDE.md)
for workflow details.

## Verify the setup

Run the focused local checks documented in [README.md](README.md). Generated
API, schema, and script-catalog documentation is checked with:

```bash
python scripts/check_generated_docs.py
```

Use `python -m pytest -q` for the full suite, noting the CI deselections and
known environment-specific failures described in the README and
[testing matrix](docs/TESTING_MATRIX.md). Do not claim a database integration
check passed unless it ran against an explicitly configured disposable local
database.

## Optional Request Audit Log

Request-audit settings, record contents, privacy limits, rotation, and operator
permissions are maintained in
[docs/CONFIGURATION_REFERENCE.md#optional-request-audit-log](docs/CONFIGURATION_REFERENCE.md#optional-request-audit-log).
It is disabled by default. Review the separate proxy/server access logs as well;
this optional application log is not an access-control mechanism.

## Operational runs

Do not start an overnight or bulk operation as part of workstation setup.
Read [OVERNIGHT.md](OVERNIGHT.md), inspect the command's help and preflight
requirements, and ensure no other database writer is active before a separately
approved bounded run.
