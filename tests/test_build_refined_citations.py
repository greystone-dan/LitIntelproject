from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.citation_refine import refine_document
from backend.database import Base, Case, Citation, CitationRefined, CitationRefineStatus

FRENCH = (
	"Canada (Ministre de la Citoyenneté et de l’Immigration) c Vavilov, 2019 CSC 65, [2019] 4 RCS 653, para 100. "
	"Le premier jugement (2011 CF 1169), le juge a appliqué la norme. Voir Aigbe c Canada, 2020 CF 895 au para 5."
)


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
	return "JSON"


@pytest.fixture
def session():
	engine = create_engine("sqlite://", poolclass=StaticPool, connect_args={"check_same_thread": False})
	Base.metadata.create_all(engine)
	with Session(engine) as db:
		db.add(Case(id=1, title="X c. Y", court="FC", date=date(2024, 1, 1), citation="2024 CF 1", full_text=FRENCH))
		db.add(Case(id=2, title="A v. B", court="FC", date=date(2024, 1, 1), citation="2024 FC 2", full_text="No citations here."))
		db.commit()
		yield db


def test_parenthesised_french_neutral_cites_are_found():
	identifiers = {i for row in refine_document(FRENCH).cases.rows for i in row.identifiers}
	assert {"2019 SCC 65", "2011 FC 1169", "2020 FC 895"} <= identifiers


def test_parenthesised_english_neutral_cite_is_found():
	rows = refine_document("The judge below (2004 FC 455, at para 1) erred.").cases.rows
	assert any("2004 FC 455" in row.identifiers for row in rows)


def run(session, monkeypatch, *args):
	import scripts.build_refined_citations as writer

	monkeypatch.setattr(writer, "SessionLocal", lambda: session)
	monkeypatch.setattr(session, "close", lambda: None)
	writer.main(list(args))


def test_dry_run_writes_nothing(session, monkeypatch, capsys):
	run(session, monkeypatch, "--limit", "10")
	assert session.scalar(select(CitationRefined.id)) is None
	assert "DRY RUN" in capsys.readouterr().out


def test_apply_is_resumable_and_revertable(session, monkeypatch):
	run(session, monkeypatch, "--apply", "--limit", "1")
	assert session.scalar(select(CitationRefineStatus.source_case_id)) == 1
	run(session, monkeypatch, "--apply", "--limit", "5")  # skips case 1, does case 2
	statuses = {s.source_case_id: s.case_rows for s in session.scalars(select(CitationRefineStatus))}
	assert statuses[1] >= 3 and statuses[2] == 0
	rows = list(session.scalars(select(CitationRefined)))
	assert {r.provenance for r in rows} == {"refine_v1"} and all(r.source_case_id == 1 for r in rows)
	assert session.scalar(select(Citation.id)) is None  # live table untouched
	run(session, monkeypatch, "--revert", "--yes")
	assert session.scalar(select(CitationRefined.id)) is None
	assert session.scalar(select(CitationRefineStatus.source_case_id)) is None


def test_french_paragraph_pinpoint_is_normalised_cleanly():
	text = "Voir Free World Trust c. Électro Santé Inc., 2000 CSC 66, [2000] 2 R.C.S. 1024, au paragraphe 13, et ailleurs."
	rows = refine_document(text).cases.rows
	assert rows and all(" e " not in f" {row.normalized_citation} " for row in rows)
	assert any("para. 13" in row.normalized_citation for row in rows)


def test_bare_landmark_short_forms_link_to_the_landmark_case():
	rows = refine_document("It was justified: Vavilov at para 85. See also Vavilov, au para 12 and Vavilov at paras 122, 194.").cases.rows
	assert [row.identifiers for row in rows] == [("2019 SCC 65",)] * 3
	assert rows[0].pinpoint == "at para. 85" and rows[2].pinpoint == "at paras. 122, 194"


def test_landmark_rule_stays_quiet_without_pinpoint_or_with_a_party_name():
	text = "The Vavilov framework applies. Baker v. Smith at para 3 is different. Mason was late."
	assert not [row for row in refine_document(text).cases.rows if row.step == "C4b_landmarks"]


def test_landmark_rule_does_not_double_count_a_full_citation():
	text = "Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65 at para 10."
	assert len(refine_document(text).cases.rows) == 1
