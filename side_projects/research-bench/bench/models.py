"""Data model for the Research Bench."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum
from typing import Optional
import uuid


def new_id() -> str:
    return uuid.uuid4().hex[:12]


class Scope(str, Enum):
    PRIVATE = "private"
    TEAM = "team"


class Label(str, Enum):
    SUPPORTS = "supports"
    ADVERSE = "adverse"
    CONTEXT = "context"
    DISTINGUISH = "distinguish"


class AlertKind(str, Enum):
    NEW_ENTRY = "new_entry"
    DECISION = "decision_released"
    HEARING = "hearing_set"


@dataclass
class Decision:
    citation: str                 # e.g. "2026 FCA 140"
    style_of_cause: str
    court: str                    # FCA, FC, SCC, IRB-ID ...
    decided: date
    url: str = ""
    summary: str = ""
    source_id: str = ""           # id in the source adapter


@dataclass
class Note:
    author: str
    body: str
    paras: list[int] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.utcnow)
    id: str = field(default_factory=new_id)


@dataclass
class SavedCase:
    decision: Decision
    owner: str
    scope: Scope = Scope.PRIVATE
    tags: set[str] = field(default_factory=set)
    folder: str = "Inbox"
    notes: list[Note] = field(default_factory=list)
    id: str = field(default_factory=new_id)


@dataclass
class Annotation:
    citation: str
    para_from: int
    para_to: int
    label: Label
    comment: str
    author: str
    scope: Scope = Scope.PRIVATE
    replies: list[Note] = field(default_factory=list)
    id: str = field(default_factory=new_id)


@dataclass
class SearchQuery:
    text: str
    courts: tuple[str, ...] = ()
    date_from: Optional[date] = None
    date_to: Optional[date] = None


@dataclass
class RecentSearch:
    owner: str
    query: SearchQuery
    hits: int
    ran_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class SavedSearch:
    name: str
    owner: str
    query: SearchQuery
    last_run: Optional[datetime] = None
    last_result_ids: set[str] = field(default_factory=set)
    id: str = field(default_factory=new_id)


@dataclass
class DocketEntry:
    docket: str
    entry_date: date
    text: str
    kind: AlertKind = AlertKind.NEW_ENTRY
    decision_citation: str = ""


@dataclass
class Alert:
    docket: str
    entry: DocketEntry
    seen: bool = False


@dataclass
class TrackedMatter:
    docket: str                   # e.g. "A-123-25"
    style_of_cause: str
    analyst: str
    court: str = "FCA"
    status: str = "Open"
    last_seen: Optional[date] = None
    alerts: list[Alert] = field(default_factory=list)


@dataclass
class AuditEvent:
    actor: str
    action: str
    target_id: str
    at: datetime = field(default_factory=datetime.utcnow)
