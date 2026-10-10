"""Live Analysis issue matches: find decided issues close to one argument from a user's draft.

Plain keyword search (BM25) over each stored issue's wording, the applicant's position on it and the
plain-language questions written for it at ingest. No model runs here, and the argument text is only
used for this request: it is never stored or logged. Behind CASELIBRARY_ISSUE_MATCHES_ENABLED=1.

Measured on 20 arguments from topics the library was never grown for, this search put a useful
precedent in its top three for 15 (about 75%); a decided issue is only a keyword match to check, not a
confirmed precedent (see ai_poc_wide/rerank_test/stage2).
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import math
import os
import re
import threading
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import IssueMap, IssueMapQuestion

ENABLED_ENV = "CASELIBRARY_ISSUE_MATCHES_ENABLED"
MAX_QUERY_CHARS = 4000
MIN_QUERY_CHARS = 20
TOP_N = 3
K1 = 1.4
B = 0.75
STOP = frozenset(
	"the a an of to in and or is are was were be by for on at with as that this did does do whether it its his her their court err erred unreasonable reasonable".split()
)
RESULT_LABELS = {
	"allowed_for_applicant": "The applicant won on this issue.",
	"dismissed_for_applicant": "The respondent won on this issue (the applicant lost).",
	"partly_allowed": "The applicant partly won on this issue.",
	"not_decided": "The court said it did not need to decide this issue.",
	"moot_or_procedural": "The issue was moot or dealt with as a procedural point.",
}
BASIS = (
	"Keyword match to check, not a confirmed precedent. The search compares wording only (no AI is used) and "
	"covers the decisions in the issue-map library; read the paragraph before relying on it."
)


def is_enabled() -> bool:
	return os.getenv(ENABLED_ENV) == "1"


def tokens(value: str) -> list[str]:
	return [w for w in re.findall(r"[a-zà-ÿ0-9]{3,}", (value or "").lower()) if w not in STOP]


@dataclass(frozen=True)
class IssueRow:
	id: int
	case_id: int | None
	citation: str | None
	court: str | None
	issue: str
	result: str
	result_para: int | None
	soften: str | None
	result_paragraph: str | None


class IssueIndex:
	"""In-memory BM25 over a few thousand rows; built once from the database and reused."""

	def __init__(self, rows: list[IssueRow], texts: list[str]) -> None:
		self.rows = rows
		self.docs = [Counter(tokens(t)) for t in texts]
		self.lengths = [sum(c.values()) for c in self.docs]
		n = len(self.docs)
		self.avg = (sum(self.lengths) / n) if n else 0.0
		df: Counter[str] = Counter()
		for c in self.docs:
			df.update(c.keys())
		self.idf = {w: math.log(1 + (n - v + 0.5) / (v + 0.5)) for w, v in df.items()}

	def top(self, query: str, k: int = TOP_N) -> list[tuple[float, IssueRow]]:
		q = set(tokens(query))
		if not q or not self.rows:
			return []
		scored: list[tuple[float, int]] = []
		for i, c in enumerate(self.docs):
			s = 0.0
			norm = K1 * (1 - B + B * self.lengths[i] / self.avg) if self.avg else K1
			for w in q:
				tf = c.get(w)
				if tf:
					s += self.idf[w] * tf * (K1 + 1) / (tf + norm)
			if s > 0:
				scored.append((s, i))
		scored.sort(key=lambda t: (-t[0], t[1]))
		return [(s, self.rows[i]) for s, i in scored[:k]]


_lock = threading.Lock()
_cache: dict[str, Any] = {"count": None, "index": None}


def reset_index() -> None:
	with _lock:
		_cache["count"] = None
		_cache["index"] = None


def _build_index(db: Session) -> IssueIndex:
	questions: dict[int, list[str]] = {}
	for issue_map_id, question in db.execute(
		select(IssueMapQuestion.issue_map_id, IssueMapQuestion.question).order_by(IssueMapQuestion.issue_map_id, IssueMapQuestion.position)
	):
		questions.setdefault(issue_map_id, []).append(question)
	rows: list[IssueRow] = []
	texts: list[str] = []
	for m in db.execute(select(IssueMap).order_by(IssueMap.id)).scalars():
		rows.append(
			IssueRow(m.id, m.case_id, m.citation, m.court, m.issue, m.result, m.result_para, m.soften, m.result_paragraph)
		)
		texts.append(" ".join([m.text, *questions.get(m.id, [])]))
	return IssueIndex(rows, texts)


def get_index(db: Session) -> IssueIndex:
	count = db.execute(select(func.count()).select_from(IssueMap)).scalar_one()
	with _lock:
		if _cache["index"] is None or _cache["count"] != count:
			_cache["index"] = _build_index(db)
			_cache["count"] = count
		return _cache["index"]


def _card(row: IssueRow) -> dict[str, Any]:
	note = row.soften
	if not note and (not row.result_para or row.result == "not_decided"):
		note = "No paragraph states a result for this issue."
	return {
		"case_id": row.case_id,
		"citation": row.citation,
		"court": row.court,
		"issue": row.issue,
		"result": row.result,
		"result_label": RESULT_LABELS.get(row.result, row.result.replace("_", " ")),
		"result_paragraph_number": row.result_para or None,
		"result_paragraph": row.result_paragraph,
		"note": note,
		"case_url": f"/data-explorer?case_id={row.case_id}" if row.case_id else None,
	}


def find_issue_matches(db: Session, argument: str) -> dict[str, Any]:
	text = (argument or "").strip()[:MAX_QUERY_CHARS]
	index = get_index(db)
	hits = index.top(text, TOP_N)
	return {
		"basis": BASIS,
		"library_issues": len(index.rows),
		"library_decisions": len({r.case_id or r.citation for r in index.rows}),
		"matches": [_card(r) for _, r in hits],
	}
