# Improvement: Prevent implicit PostgreSQL probes during pytest startup

Observed issue: `tests/conftest.py` calls `SessionLocal().execute("SELECT 1")`
at import time to discover PostgreSQL availability. This can contact a live
database merely by collecting tests, which conflicts with tasks that prohibit
database access.

Evidence: During issue #204's follow-up validation, the CI workflow's
CI-deselected suite was run with a process-local SQLAlchemy guard. Earlier
focused pytest invocations occurred before this behavior was discovered and
therefore invoked the fixture's read-only localhost probe; the connection
outcome was not captured. See
`.github/project-manager/tasks/issue-204-openai-compatible-chat-provider.md`.

Recommendation: In a separate reviewed test-infrastructure task, move the
availability check behind an explicit fixture/opt-in or add a standard
database-blocked test launcher so collection never makes an implicit network
connection. Preserve intentional SQLite in-memory tests and keep any
PostgreSQL integration check explicitly opt-in.

Expected value and risk: Makes no-DB validation reliable and prevents hidden
test-time access. Changing skip semantics could expose assumptions in tests
that currently rely on the import-time probe; cover both local and CI flows.

Decision and date: Deferred on 2026-10-04; this issue does not change test
infrastructure or database behavior.

## Repeat Evidence (2026-10-05)

During PR comment 5990921329 integration, a focused and an initial full pytest
run set `PYTHON_DOTENV_DISABLED=1` but did not block the conftest probe.
`SessionLocal().execute("SELECT 1")` was therefore attempted during collection;
the connection outcome was not captured and no writes were intended. Later
validation used a temporary startup guard that blocked the project engine's
`connect` and `raw_connection` methods before pytest collection; the focused
run confirmed the probe was intercepted. This repeats the risk above and shows
that an environment flag alone is insufficient.

Recommendation: Prioritize a repository-owned, documented no-project-database
pytest launcher/guard before further managed full-suite runs. It must install
the block before `tests/conftest.py` import, preserve explicit in-memory SQLite
tests, and leave PostgreSQL integration opt-in. Until then, use the bounded
temporary engine guard and record it with every pytest result.
