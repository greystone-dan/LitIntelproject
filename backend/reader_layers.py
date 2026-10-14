"""Stored layers for one decision in the reader: decided issues and one-line paragraph notes.

Both are written ahead of time from the decision text (see scripts/load_core150_layers.py) and read from the
database; no model runs when a page loads. The reader shows them only with Experimental on, and only for
decisions that have them (the 150 core Federal Court decisions to start with).
"""

from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session, aliased

from .database import Case, IssueMap, ParagraphNote, ParagraphNoteLink
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


LINKS_LABEL = "Related paragraphs in other decisions (automatic, may differ)"
LINKS_NOTE = (
	"Found ahead of time by an AI model comparing the one-line notes, not the decisions themselves. In a blind check about 60% "
	"were the same point and about 92 to 98% were the same or a related point; some are generic. Read both paragraphs before relying on one."
)
LINKS_PER_NOTE = 2


def case_note_links(case_id: int, db: Session) -> dict[str, Any]:
	"""Stored links from this decision's paragraph notes to notes in other decisions. Stored rows only; no model call."""
	other_note = aliased(ParagraphNote)
	mine = aliased(ParagraphNote)
	rows = db.execute(
		select(
			ParagraphNoteLink.para, mine.note, ParagraphNoteLink.score, ParagraphNoteLink.other_case_id, ParagraphNoteLink.other_para,
			other_note.note, Case.title, Case.citation,
		)
		.join(mine, (mine.case_id == ParagraphNoteLink.case_id) & (mine.para == ParagraphNoteLink.para) & (mine.version == 1))
		.join(other_note, (other_note.case_id == ParagraphNoteLink.other_case_id) & (other_note.para == ParagraphNoteLink.other_para) & (other_note.version == 1))
		.join(Case, Case.id == ParagraphNoteLink.other_case_id)
		.where(ParagraphNoteLink.case_id == case_id)
		.order_by(ParagraphNoteLink.para, ParagraphNoteLink.score.desc(), ParagraphNoteLink.other_case_id, ParagraphNoteLink.other_para)
	).all()
	items: dict[int, dict[str, Any]] = {}
	for para, note, score, other_id, other_para, other_text, title, citation in rows:
		item = items.setdefault(para, {"para": para, "note": note, "links": []})
		if len(item["links"]) < LINKS_PER_NOTE:
			item["links"].append(
				{"case_id": other_id, "title": title, "citation": citation, "para": other_para, "note": other_text, "score": score}
			)
	if not items:
		return {"available": False}
	return {"available": True, "label": LINKS_LABEL, "note": LINKS_NOTE, "items": list(items.values())}
