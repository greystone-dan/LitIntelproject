"""Stored layers for one decision in the reader: decided issues and one-line paragraph notes.

Both are written ahead of time from the decision text (see scripts/load_core150_layers.py) and read from the
database; no model runs when a page loads. The reader shows them only with Experimental on, and only for
decisions that have them (the 150 core Federal Court decisions to start with).
"""

from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import IssueMap, ParagraphNote
from .issue_match import RESULT_LABELS, review_items

ISSUES_NOTE = (
	"Written ahead of time by a small AI model that read the decision, then checked against it on a sample "
	"(about 95% of results matched). It can be wrong: read the paragraph before relying on it."
)
NOTES_NOTE = (
	"One-line notes written ahead of time by an AI model, one paragraph at a time. About 85% were judged faithful "
	"to the paragraph on a blind sample, and some qualifiers (\"partly\", \"at most\") are dropped. Names are still in the notes. "
	"Check the paragraph itself before relying on a note."
)


def case_issue_map(case_id: int, db: Session) -> dict[str, Any]:
	rows = list(
		db.execute(select(IssueMap).where(IssueMap.case_id == case_id).order_by(IssueMap.source_key, IssueMap.issue_no)).scalars()
	)
	if not rows:
		return {"available": False}
	issues = []
	for row in rows:
		flags = [f for f in (row.review_flags or []) if isinstance(f, str)]
		issues.append(
			{
				"issue": row.issue,
				"applicant_position": row.applicant_position or "",
				"respondent_position": row.respondent_position or "",
				"result": row.result,
				"result_label": RESULT_LABELS.get(row.result, row.result.replace("_", " ")),
				"result_para": row.result_para or None,
				"quote": row.result_paragraph or "",
				"checks": review_items(flags),
			}
		)
	return {"available": True, "note": ISSUES_NOTE, "issues": issues}


def case_paragraph_notes(case_id: int, db: Session) -> dict[str, Any]:
	row_version = db.execute(
		select(ParagraphNote.version).where(ParagraphNote.case_id == case_id).order_by(ParagraphNote.version.desc()).limit(1)
	).scalar_one_or_none()
	if row_version is None:
		return {"available": False}
	rows = db.execute(
		select(ParagraphNote.para, ParagraphNote.note).where(ParagraphNote.case_id == case_id, ParagraphNote.version == row_version)
	).all()
	return {"available": True, "note": NOTES_NOTE, "version": row_version, "paragraphs": {str(p): n for p, n in rows}}
