"""Workbench: demo sign-in, case list with new-activity flags, pinned decisions, exports."""

from datetime import date, timedelta

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend import workbench
from backend.database import (
	Base,
	Case,
	Citation,
	FCActivityCase,
	FCActivityClassification,
	FCProceduralHistory,
	WorkbenchCase,
	WorkbenchPin,
	get_db,
)


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
	return "JSON"


@pytest.fixture()
def env():
	engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
	Base.metadata.create_all(
		engine,
		tables=[t.__table__ for t in (Case, Citation, FCActivityCase, FCActivityClassification, FCProceduralHistory, WorkbenchCase, WorkbenchPin)],
	)
	Session = sessionmaker(bind=engine)
	app = FastAPI()
	app.include_router(workbench.router)

	def override():
		db = Session()
		try:
			yield db
		finally:
			db.close()

	app.dependency_overrides[get_db] = override
	return TestClient(app), Session


def _docket(Session, imm, entries, status="Awaiting Leave Decision"):
	with Session() as db:
		row = db.query(FCProceduralHistory).filter_by(imm_number=imm).one_or_none()
		if row is None:
			row = FCProceduralHistory(imm_number=imm, style_of_cause="DOE v. MCI")
			db.add(row)
		row.entries_json = entries
		row.case_status = status
		row.latest_activity_date = date.fromisoformat(entries[-1]["date"]) if entries else None
		db.commit()


def _entry(day, text="Filed"):
	return {"date": f"2026-09-{day:02d}", "entry": text, "re_no": "1", "docno": ""}


def _sign_in(client, name="Demo analyst"):
	assert client.post("/workbench/api/signin", json={"name": name}).status_code == 200


def test_parse_imm_numbers_accepts_common_spellings():
	assert workbench.parse_imm_numbers("IMM-1234-19, imm 55-2024\n 777-21 and IMM-1234-19") == ["IMM-1234-19", "IMM-55-24", "IMM-777-21"]
	assert workbench.parse_imm_numbers("no numbers here") == []
	assert workbench.parse_imm_numbers("2026-10-07") == []  # a date is not an IMM number


def test_api_requires_demo_sign_in_and_signin_sets_cookie(env):
	client, _ = env
	assert client.get("/workbench/api/cases").status_code == 401
	assert client.get("/workbench/api/me").json()["signed_in"] is False
	_sign_in(client, "Pat Lee")
	me = client.get("/workbench/api/me").json()
	assert me["signed_in"] and me["demo"] and me["display"] == "Pat Lee"
	_sign_in(client, "QA check")
	assert client.get("/workbench/api/me").json()["display"] == "QA check"  # shown as typed
	assert client.post("/workbench/api/signin", json={"name": "!!!"}).status_code == 422
	client.post("/workbench/api/signout")
	assert client.get("/workbench/api/cases").status_code == 401


def test_new_fc_activity_is_flagged_until_marked_viewed(env):
	client, Session = env
	_docket(Session, "IMM-1234-19", [_entry(1), _entry(2)])
	_sign_in(client)
	added = client.post("/workbench/api/cases", json={"text": "IMM-1234-19, IMM-9-24"}).json()
	assert added["added"] == ["IMM-1234-19", "IMM-9-24"]
	listing = client.get("/workbench/api/cases").json()
	by_imm = {c["imm_number"]: c for c in listing["cases"]}
	assert not by_imm["IMM-1234-19"]["flagged"] and by_imm["IMM-1234-19"]["entries"] == 2
	assert by_imm["IMM-9-24"]["known"] is False and not by_imm["IMM-9-24"]["flagged"]
	_docket(Session, "IMM-1234-19", [_entry(1), _entry(2), _entry(5, "Order granting leave")], status="Leave Granted")
	_docket(Session, "IMM-9-24", [_entry(3, "Notice of application")])
	listing = client.get("/workbench/api/cases").json()
	by_imm = {c["imm_number"]: c for c in listing["cases"]}
	assert listing["flagged"] == 2
	flagged = by_imm["IMM-1234-19"]
	assert flagged["flagged"] and flagged["new_entries"] == 1
	assert flagged["new_entry_preview"][0]["entry"] == "Order granting leave"
	assert any("Leave Granted" in r for r in flagged["flag_reasons"])
	case_id = flagged["id"]
	detail = client.get(f"/workbench/api/cases/{case_id}").json()
	assert detail["timeline"][-1]["new"] is True and detail["timeline"][0]["new"] is False
	seen = client.post(f"/workbench/api/cases/{case_id}/seen").json()
	assert not seen["flagged"]
	assert client.post("/workbench/api/cases/seen-all").json()["marked"] == 2
	assert client.get("/workbench/api/cases").json()["flagged"] == 0


def test_notes_tags_folder_deadline_and_summary(env):
	client, _ = env
	_sign_in(client)
	client.post("/workbench/api/cases", json={"text": "IMM-1-24"})
	case_id = client.get("/workbench/api/cases").json()["cases"][0]["id"]
	soon = (date.today() + timedelta(days=3)).isoformat()
	updated = client.patch(
		f"/workbench/api/cases/{case_id}",
		json={"notes": "Call counsel", "tags": ["urgent", "Urgent", " H&C "], "folder": "Week 41", "deadline": soon, "deadline_label": "Record due"},
	).json()
	assert updated["notes"] == "Call counsel" and updated["tags"] == ["urgent", "H&C"] and updated["folder"] == "Week 41"
	assert updated["deadline"] == soon
	assert client.patch(f"/workbench/api/cases/{case_id}", json={"deadline": "someday"}).status_code == 422
	summary = client.get("/workbench/api/summary").json()
	assert summary["cases"] == 1 and summary["deadlines"][0]["days"] == 3
	cleared = client.patch(f"/workbench/api/cases/{case_id}", json={"deadline": ""}).json()
	assert cleared["deadline"] is None and cleared["deadline_label"] == ""
	assert client.delete(f"/workbench/api/cases/{case_id}").status_code == 200
	assert client.get("/workbench/api/cases").json()["total"] == 0


def test_lists_are_private_to_each_demo_user(env):
	client, _ = env
	_sign_in(client, "Alex")
	client.post("/workbench/api/cases", json={"text": "IMM-1-24"})
	case_id = client.get("/workbench/api/cases").json()["cases"][0]["id"]
	_sign_in(client, "Blair")
	assert client.get("/workbench/api/cases").json()["total"] == 0
	assert client.patch(f"/workbench/api/cases/{case_id}", json={"notes": "mine"}).status_code == 404
	assert client.delete(f"/workbench/api/cases/{case_id}").status_code == 404


def test_case_list_csv_guards_spreadsheet_formulas(env):
	client, _ = env
	_sign_in(client)
	client.post("/workbench/api/cases", json={"text": "IMM-1-24"})
	case_id = client.get("/workbench/api/cases").json()["cases"][0]["id"]
	client.patch(f"/workbench/api/cases/{case_id}", json={"notes": "=HYPERLINK(\"x\")"})
	response = client.get("/workbench/api/cases/export.csv")
	assert response.headers["content-type"].startswith("text/csv")
	assert "IMM-1-24" in response.text and "'=HYPERLINK" in response.text


def test_pins_save_from_reader_and_state_endpoint(env):
	client, Session = env
	with Session() as db:
		db.add(Case(id=7, title="Doe v. Canada", court="FC", date=date(2024, 1, 2), citation="2024 FC 1", docket_number="IMM-1-23"))
		db.commit()
	state = client.get("/workbench/api/pins/state", params={"case_id": 7}).json()
	assert state == {"signed_in": False, "pinned": False}
	assert client.post("/workbench/api/pins", json={"case_id": 7}).status_code == 401
	_sign_in(client)
	assert client.post("/workbench/api/pins", json={"case_id": 999}).status_code == 404
	first = client.post("/workbench/api/pins", json={"case_id": 7}).json()
	again = client.post("/workbench/api/pins", json={"case_id": 7}).json()
	assert first["created"] and not again["created"] and first["id"] == again["id"]
	assert client.get("/workbench/api/pins/state", params={"case_id": 7}).json()["pinned"] is True
	pin = client.patch(f"/workbench/api/pins/{first['id']}", json={"notes": "Key on reasonableness", "tags": ["vavilov"], "folder": "Core"}).json()
	assert pin["title"] == "Doe v. Canada" and pin["tags"] == ["vavilov"] and pin["folder"] == "Core"
	listed = client.get("/workbench/api/pins").json()["pins"]
	assert len(listed) == 1 and listed[0]["citation"] == "2024 FC 1"
	assert "Doe v. Canada" in client.get("/workbench/api/pins/export.csv").text
	assert client.delete(f"/workbench/api/pins/{first['id']}").status_code == 200
	assert client.get("/workbench/api/pins").json()["pins"] == []


def test_page_marks_itself_demo_and_has_the_three_views(env):
	client, _ = env
	html = client.get("/workbench").text
	assert "Demo sign-in only" in html
	for view in ("Analyst home", "Live analysis", "De-identifier"):
		assert view in html
	assert 'data-src="/live-analysis?embed=1"' in html and 'data-src="/deidentify?embed=1"' in html


def test_import_rows_read_pasted_tables_with_labels():
	rows = workbench.parse_import_rows("IMM-1-24\tLopez v MCI\nIMM-2-24,IMM-3-24\n\"IMM-4-24\",\"Singh, Raj\"\nnothing here\nIMM-1-24\tduplicate")
	assert rows == [("IMM-1-24", "Lopez v MCI"), ("IMM-2-24", None), ("IMM-3-24", None), ("IMM-4-24", "Singh, Raj")]


def test_import_label_is_stored_and_milestones_come_from_docket_text(env):
	client, Session = env
	_docket(Session, "IMM-1-24", [
		_entry(1, "Notice of application filed"),
		_entry(9, "Order granting leave and setting hearing"),
		_entry(20, "Hearing scheduled for 2026-11-18"),
	])
	_sign_in(client)
	client.post("/workbench/api/cases", json={"text": "IMM-1-24\tLopez v MCI"})
	case = client.get("/workbench/api/cases").json()["cases"][0]
	assert case["label"] == "Lopez v MCI"
	detail = client.get(f"/workbench/api/cases/{case['id']}").json()
	labels = [m["label"] for m in detail["milestones"]]
	assert labels[0] == "Filed" and "Leave granted" in labels and "Hearing" in labels


def test_printable_briefs_need_sign_in_and_escape_user_text(env):
	client, Session = env
	assert client.get("/workbench/brief").status_code == 401
	_docket(Session, "IMM-1-24", [_entry(1, "Notice of application filed"), _entry(2, "Reply <script>alert(1)</script>")])
	_sign_in(client)
	client.post("/workbench/api/cases", json={"text": "IMM-1-24"})
	case_id = client.get("/workbench/api/cases").json()["cases"][0]["id"]
	client.patch(f"/workbench/api/cases/{case_id}", json={"notes": "<b>call</b> counsel"})
	one = client.get(f"/workbench/brief/case/{case_id}")
	assert one.status_code == 200 and "<script>alert" not in one.text and "&lt;b&gt;call&lt;/b&gt;" in one.text
	allbrief = client.get("/workbench/brief")
	assert allbrief.status_code == 200 and "Morning brief" in allbrief.text and "IMM-1-24" in allbrief.text
	client.post("/workbench/api/signout")
	assert client.get(f"/workbench/brief/case/{case_id}").status_code == 401


def test_pin_cited_by_is_counted_live_not_from_the_stored_column(env):
	client, Session = env
	with Session() as db:
		db.add_all([
			Case(id=7, title="Target", court="FC", date=date(2024, 1, 2), citation="2024 FC 1", citing_cases_count=8797),
			Case(id=8, title="A", court="FC", date=date(2024, 1, 3)),
			Case(id=9, title="B", court="FC", date=date(2024, 1, 4)),
		])
		db.flush()
		for source in (8, 8, 9):  # two mentions from one decision still count once
			db.add(Citation(source_case_id=source, target_case_id=7, citation_text="x", normalized_citation="x"))
		db.commit()
	_sign_in(client)
	client.post("/workbench/api/pins", json={"case_id": 7})
	assert client.get("/workbench/api/pins").json()["pins"][0]["cited_by"] == 2
