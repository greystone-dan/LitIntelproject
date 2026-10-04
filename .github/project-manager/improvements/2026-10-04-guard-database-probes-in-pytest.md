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
