"""Source adapters. Services call these; only adapters talk to outside sites.

All adapters here are STUBS. Court sites and CanLII are blocked from the cloud
environment this was written in. A real CanLII adapter needs an API key
(https://github.com/canlii/API_documentation); FCA docket data needs a source
agreed with the Registry. Keep the method signatures when replacing them.
"""
from __future__ import annotations

from datetime import date
from typing import Protocol

from .models import AlertKind, Decision, DocketEntry, SearchQuery


class SourceAdapter(Protocol):
    name: str
    def search(self, q: SearchQuery) -> list[Decision]: ...
    def fetch_decision(self, citation: str) -> Decision | None: ...


class DocketAdapter(Protocol):
    name: str
    def docket_entries(self, docket: str, since: date | None) -> list[DocketEntry]: ...


class StubCaseLawAdapter:
    """Searches a fixed in-memory corpus by keyword. Stand-in for CanLII."""
    name = "stub-caselaw"

    def __init__(self, corpus: list[Decision]):
        self.corpus = corpus

    def search(self, q: SearchQuery) -> list[Decision]:
        words = [w.lower() for w in q.text.split()]
        hits = []
        for d in self.corpus:
            hay = f"{d.citation} {d.style_of_cause} {d.summary}".lower()
            if all(w in hay for w in words) \
               and (not q.courts or d.court in q.courts) \
               and (q.date_from is None or d.decided >= q.date_from) \
               and (q.date_to is None or d.decided <= q.date_to):
                hits.append(d)
        return hits

    def fetch_decision(self, citation):
        return next((d for d in self.corpus if d.citation == citation), None)


class StubDocketAdapter:
    """Returns canned docket entries. Stand-in for the FCA docket source."""
    name = "stub-fca-dockets"

    def __init__(self, entries: dict[str, list[DocketEntry]]):
        self.entries = entries

    def docket_entries(self, docket, since):
        rows = self.entries.get(docket, [])
        return [e for e in rows if since is None or e.entry_date > since]


class CanLIIAdapter:
    """Placeholder for the real client. Not implemented."""
    name = "canlii"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, q):
        raise NotImplementedError("CanLII API client not built; see module docstring")

    def fetch_decision(self, citation):
        raise NotImplementedError


class FCADocketAdapter:
    """Placeholder for the real FCA docket client. Not implemented."""
    name = "fca-dockets"

    def docket_entries(self, docket, since):
        raise NotImplementedError("FCA docket source not agreed yet")


__all__ = ["SourceAdapter", "DocketAdapter", "StubCaseLawAdapter",
           "StubDocketAdapter", "CanLIIAdapter", "FCADocketAdapter", "AlertKind"]
