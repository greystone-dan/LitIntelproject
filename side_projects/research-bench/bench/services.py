"""Services: the Research Bench functions. UI and API call these only."""
from __future__ import annotations

from datetime import datetime

from .adapters import DocketAdapter, SourceAdapter
from .models import (Alert, Annotation, AuditEvent, Decision, Label, Note,
                     RecentSearch, SavedCase, SavedSearch, Scope, SearchQuery,
                     TrackedMatter)
from .store import Store


class PublishBlocked(Exception):
    pass


class LibraryService:
    """My Bench (private) and the Team Library (shared)."""

    def __init__(self, store: Store):
        self.store = store

    def save(self, user: str, decision: Decision, folder="Inbox", tags=()) -> SavedCase:
        case = SavedCase(decision=decision, owner=user, folder=folder, tags=set(tags))
        self.store.put_case(case)
        self.store.audit(AuditEvent(user, "save", case.id))
        return case

    def add_note(self, user: str, case: SavedCase, body: str, paras=()) -> Note:
        if case.scope == Scope.PRIVATE and case.owner != user:
            raise PermissionError("private case")
        note = Note(author=user, body=body, paras=list(paras))
        case.notes.append(note)
        self.store.audit(AuditEvent(user, "note", case.id))
        return note

    def publish_to_team(self, user: str, case: SavedCase) -> SavedCase:
        self._publish_guard(case)
        case.scope = Scope.TEAM
        self.store.audit(AuditEvent(user, "publish", case.id))
        return case

    def my_bench(self, user: str) -> list[SavedCase]:
        return self.store.cases(owner=user, scope=Scope.PRIVATE)

    def team_library(self, tag: str | None = None) -> list[SavedCase]:
        rows = self.store.cases(scope=Scope.TEAM)
        return [c for c in rows if tag is None or tag in c.tags]

    @staticmethod
    def _publish_guard(case: SavedCase) -> None:
        """Block material that must never enter the shared library.

        TODO: replace the tag check with a real classification field once the
        source systems expose one.
        """
        blocked = {"protected-b", "internal", "private-id-decision"}
        if blocked & {t.lower() for t in case.tags}:
            raise PublishBlocked(f"{case.decision.citation}: tagged {blocked & case.tags}")


class AnnotationService:
    def __init__(self, store: Store):
        self.store = store

    def annotate(self, user, citation, para_from, para_to, label: Label, comment,
                 scope=Scope.PRIVATE) -> Annotation:
        if para_to < para_from:
            raise ValueError("para_to before para_from")
        ann = Annotation(citation, para_from, para_to, label, comment, user, scope)
        self.store.put_annotation(ann)
        return ann

    def reply(self, user, ann: Annotation, body) -> Note:
        n = Note(author=user, body=body)
        ann.replies.append(n)
        return n

    def for_decision(self, citation, viewer) -> list[Annotation]:
        return self.store.annotations(citation, viewer)


class SearchService:
    def __init__(self, store: Store, source: SourceAdapter):
        self.store, self.source = store, source

    def run(self, user, q: SearchQuery) -> list[Decision]:
        hits = self.source.search(q)
        self.store.add_recent(RecentSearch(user, q, len(hits)))
        return hits

    def create_alert(self, user, q: SearchQuery, name: str | None = None) -> SavedSearch:
        """A search alert: a saved query re-run to flag decisions released since last look."""
        s = SavedSearch(name=name or q.text, owner=user, query=q)
        self.store.put_saved_search(s)
        return s

    def rerun(self, s: SavedSearch) -> tuple[list[Decision], list[Decision]]:
        """Return (all hits, hits that are new since the last run)."""
        hits = self.source.search(s.query)
        ids = {d.citation for d in hits}
        new = [d for d in hits if d.citation not in s.last_result_ids] if s.last_run else []
        s.last_result_ids, s.last_run = ids, datetime.utcnow()
        return hits, new

    def recent(self, user):
        return self.store.recent(user)


class CaseTrackerService:
    """Live case tracker: an analyst's tracked files and update checks."""

    def __init__(self, store: Store, dockets: DocketAdapter):
        self.store, self.dockets = store, dockets

    def track(self, analyst, docket, style_of_cause, court="FCA") -> TrackedMatter:
        m = TrackedMatter(docket=docket, style_of_cause=style_of_cause,
                          analyst=analyst, court=court)
        self.store.put_matter(m)
        return m

    def check(self, analyst) -> list[Alert]:
        """Query the docket source for every tracked matter; return new alerts."""
        fresh: list[Alert] = []
        for m in self.store.matters(analyst):
            entries = self.dockets.docket_entries(m.docket, m.last_seen)
            for e in sorted(entries, key=lambda e: e.entry_date):
                alert = Alert(m.docket, e)
                m.alerts.append(alert)
                fresh.append(alert)
                m.last_seen = e.entry_date
                if e.decision_citation:
                    m.status = f"Decided ({e.decision_citation})"
        return fresh

    def my_list(self, analyst):
        return self.store.matters(analyst)


class AnalysisService:
    """Live analysis: run a decision against a provision.

    STUB. A real version would send the decision text, the provision, the
    user's question and the team's annotations on that decision to a language
    model, and return structured output. Nothing leaves the environment today.
    """

    def __init__(self, store: Store, source: SourceAdapter):
        self.store, self.source = store, source

    def analyse(self, user, citation: str, provision: str, question: str = "") -> dict:
        context = self.store.annotations(citation, user)
        return {
            "citation": citation,
            "provision": provision,
            "key_paragraphs": [],        # [(para_ref, why)]
            "bearing": "",               # how it bears on the Minister's reading
            "passages_to_watch": [],     # [(para_ref, why)]
            "context_annotations": len(context),
            "stub": True,
        }
