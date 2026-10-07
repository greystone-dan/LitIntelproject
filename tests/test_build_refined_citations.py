from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.citation_refine import CASE_STEPS, refine_document
from backend.citation_refine.cases import refine_case_citations
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


def test_random_seed_and_language_filters(session, monkeypatch, capsys):
	session.get(Case, 1).language = "fr"
	session.commit()
	run(session, monkeypatch, "--language", "fr", "--random-seed", "3", "--limit", "5")
	assert "decisions=1 " in capsys.readouterr().out
	run(session, monkeypatch, "--random-seed", "3", "--limit", "1")
	assert "decisions=1 " in capsys.readouterr().out


def test_weak_pass_one_short_forms_are_rejected_and_real_ones_kept():
	from backend.citation_refine.models import RefinedCitation
	from backend.citation_refine.short_forms import is_weak_short_form

	def short(text, anchor, alias=None, step="pass1"):
		return RefinedCitation(kind="case_short", citation_text=text, normalized_citation=anchor, offset_start=0, offset_end=1,
			step=step, action="kept", confidence=0.8, declared_alias=alias)

	weak = [
		("Nation", "Standingready v. Ocean Man First Nation, 2021 FC 434"),
		("Bank", "Royal Bank of Canada v. Radius Credit Union Ltd., 2010 SCC 48"),
		("connection", "Venngo Inc v. Concierge Connection Inc, 2017 FCA 96"),
		("actuellement disponible seulement en anglais", "Dunn v. Canada (Attorney General), 2025 FC 652"),
		("Estate", "Jones Estate v. Canada (Attorney General), 2009 FC 646"),
	]
	real = [
		("Jordan", "R. v. Jordan, 2016 SCC 27"),
		("(Caraan at para 44)", "Caraan v. Canada (Public Safety and Emergency Preparedness), 2013 FC 3"),
		("Dunsmuir, para. 53", "Dunsmuir v. New Brunswick, 2008 SCC 9, at para. 53"),
		("Kanthasamy FCA", "Kanthasamy v. Canada (Citizenship and Immigration), 2014 FCA 113"),
		("WINNING COMBINATION", "Canada (Health) v. The Winning Combination Inc., 2017 FCA 101"),
	]
	assert all(is_weak_short_form(short(text, anchor)) for text, anchor in weak)
	assert not any(is_weak_short_form(short(text, anchor)) for text, anchor in real)
	assert not is_weak_short_form(short("Nation", "Standingready v. Ocean Man First Nation, 2021 FC 434", alias="Nation"))
	assert not is_weak_short_form(short("Nation", "Standingready v. Ocean Man First Nation, 2021 FC 434", step="C2_backrefs"))


def test_title_block_and_footnote_name_only_rows_are_rejected():
	from backend.citation_refine.models import RefinedCitation
	from backend.citation_refine.short_forms import is_weak_short_form

	def name_only(text):
		return RefinedCitation(kind="case_name", citation_text=text, normalized_citation=text, offset_start=0, offset_end=1,
			step="pass1", action="kept", confidence=0.4)

	assert all(is_weak_short_form(name_only(t)) for t in ["JUNIOR HERMAN v. THE", "MAHIR YAHYA SHARIF v. MCI", "Hall v. Hill[3"])
	assert not any(is_weak_short_form(name_only(t)) for t in ["Drummond v. Baylis", "R. v. Jack", "Canada (Attorney General) v. Singh"])


_DEFINED_NAMES_TEXT = (
	"The Respondent relies on Lozano Caceres v Canada (Citizenship and Immigration), 2022 FC 179 [Lozano] as support. "
	"As stated at paragraph 34 of Lozano: the test is met. "
	"See Canadian Council for Refugees v Canada (Citizenship and Immigration), 2023 SCC 17 [CCR] at para 158 and "
	"B010 v Canada (Citizenship and Immigration), 2015 SCC 58. This is the trilogy (Suresh, Febles, B010). "
	"In light of Mason and CCR, there was a matter to be resolved."
)


def test_defined_names_pinpoint_first_and_bare_acronyms() -> None:
	rows = refine_document(_DEFINED_NAMES_TEXT).cases.rows
	step_rows = [row for row in rows if row.step == "C4c_defined_names"]
	pinpoint_first = [row for row in step_rows if "pinpoint_first" in row.notes]
	assert [row.citation_text for row in pinpoint_first] == ["at paragraph 34 of Lozano"]
	assert pinpoint_first[0].pinpoint == "at para. 34"
	assert "2022 FC 179" in pinpoint_first[0].normalized_citation
	bare = {row.citation_text: row for row in step_rows if "defined_name" in row.notes}
	assert list(row.citation_text for row in step_rows if row.citation_text == "B010") == ["B010"]
	assert "CCR" in bare and "2023 SCC 17" in bare["CCR"].normalized_citation
	# the bracketed definition itself is never a second row
	assert not [row for row in rows if row.citation_text == "[CCR]"]


def test_defined_names_step_can_be_switched_off() -> None:
	steps = [step for step in CASE_STEPS if step != "C4c_defined_names"]
	rows = refine_case_citations(_DEFINED_NAMES_TEXT, steps=steps).rows
	assert not [row for row in rows if row.step == "C4c_defined_names"]


_NOISE_TEXT = (
	"Canada (Attorney General) v. Kostic, 2025 FC 125 was cited. Later, Ms. Kostic wrote to the Court and Kostic argued the point. "
	"The Court said in Kostic that the rule applies. Kostic at para 12 is clear. Arbour J. stated in Biniaris, at para. 37.\\n"
)


def test_party_mentions_are_dropped_but_real_short_forms_kept() -> None:
	text = _NOISE_TEXT.replace("\\\\n", "\\n")
	result = refine_case_citations(text, steps=CASE_STEPS)
	kept = [row.citation_text for row in result.rows if row.kind == "case_short"]
	assert [row.citation_text for row in result.rows if row.kind == "case_short" and row.citation_text == "Kostic"] == ["Kostic"]
	assert not any(row.citation_text == "Kostic" and text[row.offset_end : row.offset_end + 8] == " argued " for row in result.rows)
	assert any(text[row.offset_start - 3 : row.offset_start] == "in " and row.citation_text == "Kostic" for row in result.rows)
	assert any(row.citation_text.startswith("Kostic at para 12") for row in result.rows)
	assert not [row for row in result.rows if row.kind == "neutral" and "Biniaris" in row.citation_text]


def test_ibid_in_a_numbered_note_needs_the_citation_in_the_note_before() -> None:
	filler = "Exhibit R-1, National Documentation Package, item 2.1, a long description of a report on human rights. " * 3
	text = "9 See Nesbitt v. Canada, 2003 FCT 785.\n10 " + filler + "\n11 Ibid., and item 10.1.\n12 Nesbitt v. Canada, 2003 FCT 785.\n13 Ibid."
	rows = [row for row in refine_case_citations(text.replace("\\n", "\n"), steps=CASE_STEPS).rows if row.citation_text.startswith("Ibid")]
	assert [row.citation_text for row in rows] == ["Ibid."]
