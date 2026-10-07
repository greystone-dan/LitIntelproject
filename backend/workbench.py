"""Workbench: a demo analyst's own space (case list with activity flags, pinned decisions, notes).

Demo sign-in only: a name picks a per-person bucket kept in a cookie. There is no password and no real
account, and the page says so. Everything here reads stored data (``fc_procedural_history``,
``fc_activity_classifications``, ``cases``); no model is called and nothing a user types is sent anywhere.
Uploaded documents (Live Analysis, De-identify) never touch these tables.
"""

from __future__ import annotations

import csv
import io
import re
from datetime import date, datetime, timedelta, timezone
from urllib.parse import quote, unquote
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import (
	Case,
	Citation,
	FCActivityClassification,
	FCProceduralHistory,
	WorkbenchCase,
	WorkbenchPin,
	get_db,
)

router = APIRouter()

COOKIE = "ilit_wb_user"
DISPLAY_COOKIE = "ilit_wb_name"
_NO_STORE = {"Cache-Control": "no-store"}
_IMM = re.compile(r"\bIMM\s*-?\s*(\d{1,6})\s*-\s*(\d{2,4})\b", re.IGNORECASE)
_BARE = re.compile(r"(?<![\w-])(\d{1,6})\s*-\s*(\d{2})(?![\w-])")
MAX_CASES = 500
MAX_TAGS = 12


def normalize_imm(value: str) -> str | None:
	match = _IMM.search(value or "")
	if not match:
		return None
	number, year = match.group(1), match.group(2)
	if len(year) == 4:
		year = year[2:]
	return f"IMM-{int(number)}-{year}"


def parse_imm_numbers(raw: str) -> list[str]:
	"""Every IMM number in free text ("IMM-1234-19", "imm 1234-19", or a bare "1234-19"), de-duplicated in order."""
	found: list[str] = []
	text = raw or ""
	for match in _IMM.finditer(text):
		found.append(normalize_imm(match.group(0)) or "")
	stripped = _IMM.sub(" ", text)
	for match in _BARE.finditer(stripped):
		found.append(f"IMM-{int(match.group(1))}-{match.group(2)}")
	seen: set[str] = set()
	return [item for item in found if item and not (item in seen or seen.add(item))]


def _cells(line: str) -> list[str]:
	delimiter = next((d for d in ("\t", "|", ";") if d in line), ",")
	try:
		return [c.strip() for c in next(csv.reader([line], delimiter=delimiter))]
	except (csv.Error, StopIteration):
		return [line.strip()]


def parse_import_rows(raw: str) -> list[tuple[str, str | None]]:
	"""IMM numbers with an optional label, from pasted lists or table rows (Excel/CSV: "IMM-1-24<TAB>Lopez v MCI").

	A row with exactly one IMM number and other text uses the first other cell as the label. Rows holding several
	IMM numbers (a plain list) get no label.
	"""
	rows: list[tuple[str, str | None]] = []
	seen: set[str] = set()
	for line in (raw or "").splitlines():
		numbers = parse_imm_numbers(line)
		if not numbers:
			continue
		label = None
		if len(numbers) == 1:
			others = [c for c in _cells(line) if c and not parse_imm_numbers(c)]
			if others and len(line) > 12:
				label = others[0][:255]
		for imm in numbers:
			if imm not in seen:
				seen.add(imm)
				rows.append((imm, label))
	return rows


def slugify_owner(name: str) -> str:
	slug = re.sub(r"[^a-z0-9]+", "-", (name or "").strip().lower()).strip("-")[:60]
	return f"demo-{slug}" if slug else ""


def display_name(request: Request, owner: str) -> str:
	"""The name as typed at sign-in (kept in a cookie); falls back to the title-cased bucket name."""
	typed = " ".join(unquote(request.cookies.get(DISPLAY_COOKIE, "")).split())[:60]
	return typed if typed and slugify_owner(typed) == owner else owner[5:].replace("-", " ").title()


def current_owner(request: Request) -> str:
	owner = request.cookies.get(COOKIE, "")
	if not re.fullmatch(r"demo-[a-z0-9-]{1,60}", owner):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sign in to the Workbench first.")
	return owner


def _clean_tags(tags: list[str] | None) -> list[str]:
	out: list[str] = []
	for tag in tags or []:
		text = " ".join(str(tag).split())[:40]
		if text and text.lower() not in {t.lower() for t in out}:
			out.append(text)
	return out[:MAX_TAGS]


# ---------------------------------------------------------------- FC activity state


def _entry_date(entry: dict[str, Any]) -> str:
	return str(entry.get("date") or "")


def _sorted_entries(entries: list[Any] | None) -> list[dict[str, Any]]:
	rows = [e for e in (entries or []) if isinstance(e, dict)]
	return sorted(rows, key=_entry_date)


def _parse_date(value: Any) -> date | None:
	if isinstance(value, date):
		return value
	try:
		return date.fromisoformat(str(value)[:10])
	except (TypeError, ValueError):
		return None


def fc_state(db: Session, imm: str) -> dict[str, Any]:
	"""What the stored FC data says about one IMM file right now (read only, no network)."""
	history = db.scalar(select(FCProceduralHistory).where(FCProceduralHistory.imm_number == imm))
	if history is not None:
		entries = _sorted_entries(history.entries_json)
		latest = history.latest_activity_date or (_parse_date(entries[-1].get("date")) if entries else None)
		return {
			"known": True,
			"source": "docket",
			"style_of_cause": history.style_of_cause,
			"status": history.case_status,
			"leave": history.leave_decision,
			"judicial_review": history.jr_decision,
			"judge": history.judge,
			"entries": len(entries),
			"latest_activity": latest,
			"fetched_at": history.fetched_at,
			"_entries": entries,
		}
	classified = db.scalar(select(FCActivityClassification).where(FCActivityClassification.imm_number == imm))
	if classified is not None:
		data = classified.classification_json or {}
		timeline = data.get("timeline") if isinstance(data.get("timeline"), list) else []
		return {
			"known": True,
			"source": "classified",
			"style_of_cause": classified.case_name,
			"status": data.get("lifecycle_status"),
			"leave": data.get("leave_decision") if isinstance(data.get("leave_decision"), str) else None,
			"judicial_review": data.get("judicial_review_result") if isinstance(data.get("judicial_review_result"), str) else None,
			"judge": None,
			"entries": len(timeline),
			"latest_activity": None,
			"fetched_at": classified.updated_at,
			"_entries": [],
		}
	return {
		"known": False, "source": None, "style_of_cause": None, "status": None, "leave": None,
		"judicial_review": None, "judge": None, "entries": 0, "latest_activity": None, "fetched_at": None, "_entries": [],
	}


_MILESTONES = (
	("Filed", re.compile(r"notice of application|application for leave|leave application|filed", re.I), True),
	("Leave granted", re.compile(r"leave\b.{0,40}\bgranted|granting leave|application for leave.{0,40}granted", re.I), False),
	("Leave dismissed", re.compile(r"leave\b.{0,40}\bdismissed|dismissing.{0,30}leave|leave\b.{0,40}\bdenied", re.I), False),
	("Hearing", re.compile(r"\bhearing\b|oral hearing|hearing scheduled", re.I), False),
	("Stay", re.compile(r"\bstay\b|stay of removal", re.I), False),
	("Judgment", re.compile(r"judgment|reasons for (?:order|judgment)|application.{0,30}(?:allowed|dismissed)", re.I), False),
	("Discontinued", re.compile(r"discontinu|withdraw", re.I), False),
)


def milestones(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
	"""Key docket events found by fixed text rules (first Filed, then every other kind in date order)."""
	found: list[dict[str, Any]] = []
	filed_done = False
	for entry in entries:
		text = str(entry.get("entry") or "")
		for label, pattern, first_only in _MILESTONES:
			if first_only and filed_done:
				continue
			if pattern.search(text):
				if first_only:
					filed_done = True
				found.append({"label": label, "date": entry.get("date"), "entry": text[:160]})
				break
	return found[-12:]


def _snapshot(row: WorkbenchCase, state: dict[str, Any]) -> None:
	row.last_seen_entries = int(state["entries"] or 0)
	row.last_seen_activity_date = state["latest_activity"]
	row.last_seen_status = state["status"]
	row.last_viewed_at = datetime.now(timezone.utc)


def case_payload(row: WorkbenchCase, state: dict[str, Any], *, detail: bool = False) -> dict[str, Any]:
	new_count = max(0, int(state["entries"] or 0) - int(row.last_seen_entries or 0))
	status_changed = bool(row.last_seen_status) and bool(state["status"]) and row.last_seen_status != state["status"]
	flagged = new_count > 0 or status_changed
	reasons: list[str] = []
	if new_count:
		reasons.append(f"{new_count} new docket {'entry' if new_count == 1 else 'entries'}")
	if status_changed:
		reasons.append(f"status changed from {row.last_seen_status} to {state['status']}")
	new_entries = state["_entries"][-new_count:] if new_count and state["_entries"] else []
	payload: dict[str, Any] = {
		"id": row.id,
		"imm_number": row.imm_number,
		"label": row.label,
		"notes": row.notes or "",
		"tags": row.tags or [],
		"folder": row.folder or "",
		"deadline": row.deadline.isoformat() if row.deadline else None,
		"deadline_label": row.deadline_label or "",
		"added_at": row.added_at.isoformat() if row.added_at else None,
		"last_viewed_at": row.last_viewed_at.isoformat() if row.last_viewed_at else None,
		"known": state["known"],
		"style_of_cause": state["style_of_cause"],
		"status": state["status"],
		"leave": state["leave"],
		"judicial_review": state["judicial_review"],
		"judge": state["judge"],
		"entries": state["entries"],
		"latest_activity": state["latest_activity"].isoformat() if state["latest_activity"] else None,
		"data_as_of": state["fetched_at"].isoformat() if state["fetched_at"] else None,
		"flagged": flagged,
		"new_entries": new_count,
		"flag_reasons": reasons,
		"new_entry_preview": [
			{"date": e.get("date"), "entry": str(e.get("entry") or "")[:400]} for e in new_entries[-5:]
		],
	}
	if detail:
		payload["timeline"] = [
			{"date": e.get("date"), "entry": str(e.get("entry") or "")[:1200], "re_no": e.get("re_no"), "new": i >= len(state["_entries"]) - new_count and new_count > 0}
			for i, e in enumerate(state["_entries"])
		][-80:]
		payload["milestones"] = milestones(state["_entries"])
	return payload


def live_cited_by(db: Session, case_ids: list[int]) -> dict[int, int]:
	"""Distinct citing decisions per case, counted live from citations (the same count the case reader shows)."""
	if not case_ids:
		return {}
	rows = db.execute(
		select(Citation.target_case_id, func.count(func.distinct(Citation.source_case_id)))
		.where(Citation.target_case_id.in_(case_ids))
		.group_by(Citation.target_case_id)
	).all()
	return {int(target): int(count) for target, count in rows}


def pin_payload(pin: WorkbenchPin, case: Case | None, cited_by: int | None = None) -> dict[str, Any]:
	return {
		"id": pin.id,
		"case_id": pin.case_id,
		"title": case.title if case else "(decision no longer in the library)",
		"citation": case.citation if case else None,
		"court": case.court if case else None,
		"date": case.date.isoformat() if case and case.date else None,
		"docket": case.docket_number if case else None,
		"cited_by": cited_by if case else None,
		"notes": pin.notes or "",
		"tags": pin.tags or [],
		"folder": pin.folder or "",
		"pinned_at": pin.pinned_at.isoformat() if pin.pinned_at else None,
	}


# ---------------------------------------------------------------- request models


class SignInRequest(BaseModel):
	name: str = Field(min_length=1, max_length=60)


class AddCasesRequest(BaseModel):
	text: str = Field(min_length=1, max_length=20000)
	folder: str | None = Field(default=None, max_length=80)


class ItemUpdate(BaseModel):
	label: str | None = Field(default=None, max_length=255)
	notes: str | None = Field(default=None, max_length=20000)
	tags: list[str] | None = None
	folder: str | None = Field(default=None, max_length=80)
	deadline: str | None = None
	deadline_label: str | None = Field(default=None, max_length=120)


class PinRequest(BaseModel):
	case_id: int
	folder: str | None = Field(default=None, max_length=80)


def _apply_update(row: WorkbenchCase | WorkbenchPin, body: ItemUpdate) -> None:
	fields = body.model_fields_set
	if "notes" in fields:
		row.notes = (body.notes or "").strip() or None
	if "tags" in fields:
		row.tags = _clean_tags(body.tags)
	if "folder" in fields:
		row.folder = " ".join((body.folder or "").split())[:80] or None
	if isinstance(row, WorkbenchCase):
		if "label" in fields:
			row.label = " ".join((body.label or "").split())[:255] or None
		if "deadline" in fields:
			if body.deadline:
				parsed = _parse_date(body.deadline)
				if parsed is None:
					raise HTTPException(status_code=422, detail="Deadline must be a date like 2026-11-30.")
				row.deadline = parsed
			else:
				row.deadline = None
				row.deadline_label = None
		if "deadline_label" in fields and row.deadline:
			row.deadline_label = " ".join((body.deadline_label or "").split())[:120] or None


def _owned_case(db: Session, owner: str, case_id: int) -> WorkbenchCase:
	row = db.scalar(select(WorkbenchCase).where(WorkbenchCase.id == case_id, WorkbenchCase.owner == owner))
	if row is None:
		raise HTTPException(status_code=404, detail="That case is not on your list.")
	return row


def _owned_pin(db: Session, owner: str, pin_id: int) -> WorkbenchPin:
	row = db.scalar(select(WorkbenchPin).where(WorkbenchPin.id == pin_id, WorkbenchPin.owner == owner))
	if row is None:
		raise HTTPException(status_code=404, detail="That pinned case was not found.")
	return row


def _json(payload: Any, code: int = 200) -> JSONResponse:
	return JSONResponse(payload, status_code=code, headers=_NO_STORE)


# ---------------------------------------------------------------- sign-in (demo)


@router.get("/workbench/api/me", include_in_schema=False)
def workbench_me(request: Request) -> JSONResponse:
	owner = request.cookies.get(COOKIE, "")
	if not re.fullmatch(r"demo-[a-z0-9-]{1,60}", owner):
		return _json({"signed_in": False, "demo": True})
	return _json({"signed_in": True, "demo": True, "owner": owner, "display": display_name(request, owner)})


@router.post("/workbench/api/signin", include_in_schema=False)
def workbench_signin(body: SignInRequest) -> JSONResponse:
	owner = slugify_owner(body.name)
	if not owner:
		raise HTTPException(status_code=422, detail="Enter a name with at least one letter or number.")
	typed = " ".join(body.name.split())[:60]
	response = _json({"signed_in": True, "demo": True, "owner": owner, "display": typed})
	response.set_cookie(COOKIE, owner, max_age=60 * 60 * 24 * 365, httponly=True, samesite="lax", path="/")
	response.set_cookie(DISPLAY_COOKIE, quote(typed), max_age=60 * 60 * 24 * 365, samesite="lax", path="/")
	return response


@router.post("/workbench/api/signout", include_in_schema=False)
def workbench_signout() -> JSONResponse:
	response = _json({"signed_in": False, "demo": True})
	response.delete_cookie(COOKIE, path="/")
	response.delete_cookie(DISPLAY_COOKIE, path="/")
	return response


# ---------------------------------------------------------------- case list


@router.get("/workbench/api/cases", include_in_schema=False)
def list_cases(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	rows = db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner).order_by(WorkbenchCase.added_at.desc())).all()
	items = [case_payload(row, fc_state(db, row.imm_number)) for row in rows]
	items.sort(key=lambda item: (not item["flagged"], item["deadline"] or "9999", item["imm_number"]))
	return _json({"cases": items, "flagged": sum(1 for item in items if item["flagged"]), "total": len(items)})


@router.post("/workbench/api/cases", include_in_schema=False)
def add_cases(body: AddCasesRequest, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	import_rows = parse_import_rows(body.text)
	numbers = [imm for imm, _ in import_rows]
	labels = {imm: label for imm, label in import_rows}
	if not numbers:
		raise HTTPException(status_code=422, detail="No IMM numbers found. Use the form IMM-1234-19, one per line or separated by commas.")
	existing = {row.imm_number for row in db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner)).all()}
	if len(existing) + len([n for n in numbers if n not in existing]) > MAX_CASES:
		raise HTTPException(status_code=422, detail=f"A Workbench list holds up to {MAX_CASES} cases.")
	added, skipped = [], []
	folder = " ".join((body.folder or "").split())[:80] or None
	for imm in numbers:
		if imm in existing:
			skipped.append(imm)
			continue
		row = WorkbenchCase(owner=owner, imm_number=imm, folder=folder, tags=[], label=labels.get(imm))
		_snapshot(row, fc_state(db, imm))
		db.add(row)
		added.append(imm)
	db.commit()
	return _json({"added": added, "already_on_list": skipped})


@router.get("/workbench/api/cases/export.csv", include_in_schema=False)
def export_cases(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> Response:
	rows = db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner).order_by(WorkbenchCase.imm_number)).all()
	buffer = io.StringIO()
	writer = csv.writer(buffer)
	writer.writerow(["IMM number", "Style of cause", "Status", "Leave", "Judicial review", "Entries", "Latest activity", "New since last viewed", "Folder", "Tags", "Deadline", "Deadline note", "Notes"])
	for row in rows:
		item = case_payload(row, fc_state(db, row.imm_number))
		writer.writerow([_csv_safe(v) for v in [
			item["imm_number"], item["style_of_cause"] or "", item["status"] or "", item["leave"] or "", item["judicial_review"] or "",
			item["entries"], item["latest_activity"] or "", item["new_entries"], item["folder"], "; ".join(item["tags"]),
			item["deadline"] or "", item["deadline_label"], item["notes"],
		]])
	return Response(buffer.getvalue(), media_type="text/csv", headers={**_NO_STORE, "Content-Disposition": 'attachment; filename="workbench-case-list.csv"'})


@router.post("/workbench/api/cases/seen-all", include_in_schema=False)
def mark_all_seen(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	rows = db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner)).all()
	for row in rows:
		_snapshot(row, fc_state(db, row.imm_number))
	db.commit()
	return _json({"marked": len(rows)})


@router.get("/workbench/api/cases/{case_id}", include_in_schema=False)
def case_detail(case_id: int, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	row = _owned_case(db, owner, case_id)
	return _json(case_payload(row, fc_state(db, row.imm_number), detail=True))


@router.patch("/workbench/api/cases/{case_id}", include_in_schema=False)
def update_case(case_id: int, body: ItemUpdate, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	row = _owned_case(db, owner, case_id)
	_apply_update(row, body)
	db.commit()
	return _json(case_payload(row, fc_state(db, row.imm_number)))


@router.post("/workbench/api/cases/{case_id}/seen", include_in_schema=False)
def mark_seen(case_id: int, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	row = _owned_case(db, owner, case_id)
	_snapshot(row, fc_state(db, row.imm_number))
	db.commit()
	return _json(case_payload(row, fc_state(db, row.imm_number)))


@router.delete("/workbench/api/cases/{case_id}", include_in_schema=False)
def delete_case(case_id: int, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	db.delete(_owned_case(db, owner, case_id))
	db.commit()
	return _json({"deleted": case_id})


# ---------------------------------------------------------------- pinned decisions


@router.get("/workbench/api/pins", include_in_schema=False)
def list_pins(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	pins = db.scalars(select(WorkbenchPin).where(WorkbenchPin.owner == owner).order_by(WorkbenchPin.pinned_at.desc())).all()
	cases = {c.id: c for c in db.scalars(select(Case).where(Case.id.in_([p.case_id for p in pins] or [0]))).all()}
	counts = live_cited_by(db, [p.case_id for p in pins])
	return _json({"pins": [pin_payload(p, cases.get(p.case_id), counts.get(p.case_id, 0)) for p in pins]})


@router.get("/workbench/api/pins/state", include_in_schema=False)
def pin_state(request: Request, case_id: int, db: Session = Depends(get_db)) -> JSONResponse:
	"""For the reader's Save button: signed out is a normal answer, not an error."""
	owner = request.cookies.get(COOKIE, "")
	if not re.fullmatch(r"demo-[a-z0-9-]{1,60}", owner):
		return _json({"signed_in": False, "pinned": False})
	pin = db.scalar(select(WorkbenchPin).where(WorkbenchPin.owner == owner, WorkbenchPin.case_id == case_id))
	return _json({"signed_in": True, "pinned": pin is not None, "pin_id": pin.id if pin else None})


@router.post("/workbench/api/pins", include_in_schema=False)
def add_pin(body: PinRequest, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	case = db.get(Case, body.case_id)
	if case is None:
		raise HTTPException(status_code=404, detail="That decision is not in the library.")
	pin = db.scalar(select(WorkbenchPin).where(WorkbenchPin.owner == owner, WorkbenchPin.case_id == body.case_id))
	created = pin is None
	if pin is None:
		pin = WorkbenchPin(owner=owner, case_id=body.case_id, tags=[], folder=" ".join((body.folder or "").split())[:80] or None)
		db.add(pin)
		db.commit()
	return _json({**pin_payload(pin, case, live_cited_by(db, [pin.case_id]).get(pin.case_id, 0)), "created": created})


@router.get("/workbench/api/pins/export.csv", include_in_schema=False)
def export_pins(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> Response:
	pins = db.scalars(select(WorkbenchPin).where(WorkbenchPin.owner == owner).order_by(WorkbenchPin.pinned_at.desc())).all()
	cases = {c.id: c for c in db.scalars(select(Case).where(Case.id.in_([p.case_id for p in pins] or [0]))).all()}
	buffer = io.StringIO()
	writer = csv.writer(buffer)
	writer.writerow(["Title", "Citation", "Court", "Date", "Docket", "Folder", "Tags", "Notes", "Case ID"])
	for pin in pins:
		item = pin_payload(pin, cases.get(pin.case_id))
		writer.writerow([_csv_safe(v) for v in [item["title"], item["citation"] or "", item["court"] or "", item["date"] or "", item["docket"] or "", item["folder"], "; ".join(item["tags"]), item["notes"], item["case_id"]]])
	return Response(buffer.getvalue(), media_type="text/csv", headers={**_NO_STORE, "Content-Disposition": 'attachment; filename="workbench-pinned-cases.csv"'})


@router.patch("/workbench/api/pins/{pin_id}", include_in_schema=False)
def update_pin(pin_id: int, body: ItemUpdate, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	pin = _owned_pin(db, owner, pin_id)
	_apply_update(pin, body)
	db.commit()
	return _json(pin_payload(pin, db.get(Case, pin.case_id), live_cited_by(db, [pin.case_id]).get(pin.case_id, 0)))


@router.delete("/workbench/api/pins/{pin_id}", include_in_schema=False)
def delete_pin(pin_id: int, owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	db.delete(_owned_pin(db, owner, pin_id))
	db.commit()
	return _json({"deleted": pin_id})


# ---------------------------------------------------------------- summary


@router.get("/workbench/api/summary", include_in_schema=False)
def summary(owner: str = Depends(current_owner), db: Session = Depends(get_db)) -> JSONResponse:
	"""Home page numbers: list size, flagged files, pins, and deadlines in the next 30 days (or overdue)."""
	today = date.today()
	soon = today + timedelta(days=30)
	cases = db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner)).all()
	pins = db.scalars(select(WorkbenchPin).where(WorkbenchPin.owner == owner)).all()
	flagged = 0
	deadlines: list[dict[str, Any]] = []
	for row in cases:
		item = case_payload(row, fc_state(db, row.imm_number))
		flagged += 1 if item["flagged"] else 0
		if row.deadline and row.deadline <= soon:
			deadlines.append({"id": row.id, "imm_number": row.imm_number, "deadline": row.deadline.isoformat(), "label": row.deadline_label or "Deadline", "days": (row.deadline - today).days})
	deadlines.sort(key=lambda d: d["deadline"])
	return _json({"cases": len(cases), "flagged": flagged, "pins": len(pins), "deadlines": deadlines})


def _csv_safe(value: Any) -> Any:
	"""Spreadsheet formula guard for text a user typed or a source supplied."""
	if isinstance(value, str) and value[:1] in ("=", "+", "-", "@", "\t", "\r"):
		return "'" + value
	return value


# ---------------------------------------------------------------- printable briefs


def _owner_or_message(request: Request) -> str | None:
	owner = request.cookies.get(COOKIE, "")
	return owner if re.fullmatch(r"demo-[a-z0-9-]{1,60}", owner) else None


def _signin_needed() -> HTMLResponse:
	return HTMLResponse('<!doctype html><meta charset="utf-8"><p style="font:16px sans-serif;margin:30px">Sign in on the <a href="/workbench">Workbench</a> first.</p>', status_code=401)


def _case_section(item: dict[str, Any]) -> str:
	from .pages.workbench_brief import esc

	flag = f'<p class="flag">New since last viewed: {esc("; ".join(item["flag_reasons"]))}.</p>' if item["flagged"] else ""
	miles = "".join(f"<tr><td>{esc(m['date'])}</td><td>{esc(m['label'])}</td><td>{esc(m['entry'])}</td></tr>" for m in item.get("milestones", []))
	rows = "".join(
		f'<tr class="{"new" if e["new"] else ""}"><td>{esc(e["date"])}</td><td>{esc(e["entry"])}</td></tr>' for e in item.get("timeline", [])
	)
	dl = f"<p><strong>Deadline:</strong> {esc(item['deadline'])} {esc(item['deadline_label'])}</p>" if item["deadline"] else ""
	return (
		f"<h2>{esc(item['imm_number'])} {esc(item['label'] or item['style_of_cause'] or '')}</h2>{flag}"
		f"<p class=\"muted\">Status: {esc(item['status'] or 'not stored')} &middot; Leave: {esc(item['leave'] or '-')} &middot; Judicial review: {esc(item['judicial_review'] or '-')} &middot; Judge: {esc(item['judge'] or '-')} &middot; {esc(item['entries'])} docket entries"
		f"{(' &middot; folder ' + esc(item['folder'])) if item['folder'] else ''}{(' &middot; tags ' + esc(', '.join(item['tags']))) if item['tags'] else ''}</p>{dl}"
		+ (f"<p><strong>Notes</strong></p><div class=\"notes\">{esc(item['notes'])}</div>" if item["notes"] else "")
		+ (f"<p><strong>Milestones</strong></p><table><tr><th>Date</th><th>Event</th><th>Docket text</th></tr>{miles}</table>" if miles else "")
		+ (f"<p><strong>Docket</strong></p><table><tr><th style=\"width:92px\">Date</th><th>Entry</th></tr>{rows}</table>" if rows else "<p class=\"muted\">No docket entries are stored for this file yet.</p>")
	)


@router.get("/workbench/brief/case/{case_id}", response_class=HTMLResponse, include_in_schema=False)
def brief_case(case_id: int, request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
	from .pages.workbench_brief import brief_page

	owner = _owner_or_message(request)
	if owner is None:
		return _signin_needed()
	row = _owned_case(db, owner, case_id)
	item = case_payload(row, fc_state(db, row.imm_number), detail=True)
	return HTMLResponse(brief_page(f"Case brief: {row.imm_number}", "Workbench", _case_section(item)), headers=_NO_STORE)


@router.get("/workbench/brief", response_class=HTMLResponse, include_in_schema=False)
def brief_all(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
	"""Morning brief: what moved since you last looked, deadlines, then the whole case list and pinned decisions."""
	from .pages.workbench_brief import brief_page, esc

	owner = _owner_or_message(request)
	if owner is None:
		return _signin_needed()
	rows = db.scalars(select(WorkbenchCase).where(WorkbenchCase.owner == owner).order_by(WorkbenchCase.imm_number)).all()
	items = [case_payload(r, fc_state(db, r.imm_number), detail=True) for r in rows]
	flagged = [i for i in items if i["flagged"]]
	today = date.today()
	due = sorted((i for i in items if i["deadline"]), key=lambda i: i["deadline"])
	html = f"<h2>New activity ({len(flagged)})</h2>"
	html += "".join(_case_section(i) for i in flagged) if flagged else '<p class="muted">Nothing has moved on your tracked files since you last viewed them.</p>'
	html += f"<h2>Deadlines ({len(due)})</h2>"
	html += (
		"<table><tr><th>Date</th><th>File</th><th>Note</th><th>Days</th></tr>"
		+ "".join(f"<tr><td>{esc(i['deadline'])}</td><td>{esc(i['imm_number'])} {esc(i['label'] or i['style_of_cause'] or '')}</td><td>{esc(i['deadline_label'])}</td><td>{(date.fromisoformat(i['deadline']) - today).days}</td></tr>" for i in due)
		+ "</table>"
	) if due else '<p class="muted">No deadlines set.</p>'
	html += f"<h2>All tracked files ({len(items)})</h2><table><tr><th>IMM</th><th>Name</th><th>Status</th><th>Latest activity</th><th>Folder</th></tr>"
	html += "".join(f"<tr><td>{esc(i['imm_number'])}</td><td>{esc(i['label'] or i['style_of_cause'] or '')}</td><td>{esc(i['status'] or '')}</td><td>{esc(i['latest_activity'] or '')}</td><td>{esc(i['folder'])}</td></tr>" for i in items) + "</table>"
	pins = db.scalars(select(WorkbenchPin).where(WorkbenchPin.owner == owner).order_by(WorkbenchPin.pinned_at.desc())).all()
	cases = {c.id: c for c in db.scalars(select(Case).where(Case.id.in_([p.case_id for p in pins] or [0]))).all()}
	html += f"<h2>Pinned decisions ({len(pins)})</h2>"
	if pins:
		html += "<table><tr><th>Decision</th><th>Citation</th><th>Notes</th></tr>"
		for pin in pins:
			p = pin_payload(pin, cases.get(pin.case_id))
			html += f"<tr><td>{esc(p['title'])}<div class=\"muted\">{esc(p['court'])} {esc(p['date'])}</div></td><td>{esc(p['citation'])}</td><td>{esc(p['notes'])}</td></tr>"
		html += "</table>"
	else:
		html += '<p class="muted">Nothing pinned yet.</p>'
	return HTMLResponse(brief_page(f"Morning brief, {today.strftime('%B %d, %Y').replace(' 0', ' ')}", "Workbench", html), headers=_NO_STORE)


# ---------------------------------------------------------------- page


@router.get("/workbench", response_class=HTMLResponse, include_in_schema=False)
def workbench_page() -> HTMLResponse:
	from .pages.workbench import workbench_page_html

	return HTMLResponse(content=workbench_page_html(), headers=_NO_STORE)
