"""Statement instrumentation for isolated offline performance fixtures."""

from contextlib import contextmanager
from dataclasses import dataclass, field

from sqlalchemy import event


@dataclass
class StatementCounter:
    statements: list[str] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.statements)


@contextmanager
def count_statements(engine):
    """Count executed SQL, excluding setup outside the context; always detach."""
    counter = StatementCounter()

    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        counter.statements.append(statement)

    event.listen(engine, "before_cursor_execute", before_cursor_execute)
    try:
        yield counter
    finally:
        event.remove(engine, "before_cursor_execute", before_cursor_execute)
