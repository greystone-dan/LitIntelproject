"""Repository interface plus an in-memory implementation.

Swap InMemoryStore for a SQLite/Postgres store later; services depend only on Store.
"""
from __future__ import annotations

from typing import Protocol

from .models import (Annotation, AuditEvent, RecentSearch, SavedCase,
                     SavedSearch, Scope, TrackedMatter)

RECENT_LIMIT = 25


class Store(Protocol):
    def put_case(self, case: SavedCase) -> None: ...
    def cases(self, owner: str | None = None, scope: Scope | None = None) -> list[SavedCase]: ...
    def put_annotation(self, ann: Annotation) -> None: ...
    def annotations(self, citation: str, viewer: str) -> list[Annotation]: ...
    def add_recent(self, r: RecentSearch) -> None: ...
    def recent(self, owner: str) -> list[RecentSearch]: ...
    def put_saved_search(self, s: SavedSearch) -> None: ...
    def saved_searches(self, owner: str) -> list[SavedSearch]: ...
    def put_matter(self, m: TrackedMatter) -> None: ...
    def matters(self, analyst: str) -> list[TrackedMatter]: ...
    def audit(self, e: AuditEvent) -> None: ...


class InMemoryStore:
    def __init__(self) -> None:
        self._cases: dict[str, SavedCase] = {}
        self._anns: dict[str, Annotation] = {}
        self._recent: list[RecentSearch] = []
        self._saved: dict[str, SavedSearch] = {}
        self._matters: dict[tuple[str, str], TrackedMatter] = {}
        self.audit_log: list[AuditEvent] = []

    def put_case(self, case):
        self._cases[case.id] = case

    def cases(self, owner=None, scope=None):
        return [c for c in self._cases.values()
                if (owner is None or c.owner == owner) and (scope is None or c.scope == scope)]

    def put_annotation(self, ann):
        self._anns[ann.id] = ann

    def annotations(self, citation, viewer):
        return sorted((a for a in self._anns.values() if a.citation == citation
                       and (a.scope == Scope.TEAM or a.author == viewer)),
                      key=lambda a: a.para_from)

    def add_recent(self, r):
        self._recent.insert(0, r)
        mine = [x for x in self._recent if x.owner == r.owner]
        for stale in mine[RECENT_LIMIT:]:
            self._recent.remove(stale)

    def recent(self, owner):
        return [r for r in self._recent if r.owner == owner]

    def put_saved_search(self, s):
        self._saved[s.id] = s

    def saved_searches(self, owner):
        return [s for s in self._saved.values() if s.owner == owner]

    def put_matter(self, m):
        self._matters[(m.analyst, m.docket)] = m

    def matters(self, analyst):
        return [m for (a, _), m in self._matters.items() if a == analyst]

    def audit(self, e):
        self.audit_log.append(e)
