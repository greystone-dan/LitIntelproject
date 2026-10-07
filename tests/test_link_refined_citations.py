from datetime import date

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.citation_refine.linking import build_case_key_index, resolve_refined_row
from backend.citation_source import citations_source, incoming_citations, outgoing_citations
from backend.database import Base, Case, Citation, CitationRefined, CitationRefineStatus


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
	return "JSON"


@pytest.fixture
def session():
	engine = create_engine("sqlite://", poolclass=StaticPool, connect_args={"check_same_thread": False})
	Base.metadata.create_all(engine)
	with Session(engine) as db:
		for case_id, title, cite in [
			(1, "Source v. A", "2026 FC 1"),
			(2, "Canada (Minister of Citizenship and Immigration) v. Vavilov", "2019 SCC 65"),
			(3, "Other v. B", "2020 FC 5"),
			(4, "Twin one", "2020 FC 9"),
			(5, "Twin two", "2020 FC 9"),
		]:
			db.add(Case(id=case_id, title=title, citation=cite, court="FC", date=date(2020, 1, 1), full_text="x"))
		db.commit()
		yield db


def _index(db):
	return build_case_key_index(db.execute(select(Case.id, Case.citation, Case.secondary_citation)))


def test_resolve_neutral_french_and_short_rows(session) -> None:
	index = _index(session)
	assert resolve_refined_row("case", "Vavilov, 2019 SCC 65 at para 85", "Canada v. Vavilov, 2019 SCC 65, at para. 85", 1, index) == 2
	assert resolve_refined_row("neutral", "2019 CSC 65 au para 5", "2019 CSC 65", 1, index) == 2
	assert resolve_refined_row("case_short", "Vavilov at para 85", "Canada v. Vavilov, 2019 SCC 65, at para. 85", 1, index) == 2


def test_no_link_for_ambiguous_missing_selfcite_or_name_only(session) -> None:
	index = _index(session)
	assert resolve_refined_row("neutral", "2020 FC 9", "2020 FC 9", 1, index) is None  # two cases share it
	assert resolve_refined_row("neutral", "2031 FC 99", "2031 FC 99", 1, index) is None  # not in library
	assert resolve_refined_row("neutral", "2019 SCC 65", "2019 SCC 65", 2, index) is None  # self-citation
	assert resolve_refined_row("case_name", "Vavilov", "Vavilov", 1, index) is None


def test_citations_source_default_and_validation(monkeypatch) -> None:
	monkeypatch.delenv("CITATIONS_SOURCE", raising=False)
	assert citations_source() == "legacy"
	monkeypatch.setenv("CITATIONS_SOURCE", "refined")
	assert citations_source() == "refined"
	monkeypatch.setenv("CITATIONS_SOURCE", "bogus")
	with pytest.raises(ValueError):
		citations_source()


def test_read_paths_fall_back_per_source_case(session, monkeypatch) -> None:
	session.add_all(
		[
			Citation(source_case_id=1, target_case_id=2, citation_kind="neutral", citation_text="legacy-1"),
			Citation(source_case_id=3, target_case_id=2, citation_kind="neutral", citation_text="legacy-3"),
			CitationRefined(source_case_id=1, target_case_id=2, citation_kind="neutral", citation_text="refined-1", refine_version=1),
			CitationRefined(source_case_id=1, target_case_id=None, citation_kind="case_short", citation_text="refined-1b", refine_version=1),
			CitationRefineStatus(source_case_id=1, refine_version=1, status="done", case_rows=2, statute_rows=0),
		]
	)
	session.commit()
	monkeypatch.delenv("CITATIONS_SOURCE", raising=False)
	assert [c.citation_text for c in outgoing_citations(session, 1)] == ["legacy-1"]
	assert [c.citation_text for c in incoming_citations(session, 2)] == ["legacy-1", "legacy-3"]
	monkeypatch.setenv("CITATIONS_SOURCE", "refined")
	assert [c.citation_text for c in outgoing_citations(session, 1)] == ["refined-1", "refined-1b"]
	assert [c.citation_text for c in outgoing_citations(session, 3)] == ["legacy-3"]  # not refined yet: live rows
	assert [c.citation_text for c in incoming_citations(session, 2)] == ["refined-1", "legacy-3"]


def _run(session, monkeypatch, *args):
	import scripts.link_refined_citations as script

	monkeypatch.setattr(script, "SessionLocal", lambda: session)
	monkeypatch.setattr(session, "close", lambda: None)
	script.main(list(args))


def _links(session):
	session.expire_all()
	return {r.citation_text: (r.target_case_id, r.unresolved) for r in session.scalars(select(CitationRefined))}


def test_link_script_dry_run_apply_and_revert(session, monkeypatch, capsys) -> None:
	session.add_all(
		[
			CitationRefined(source_case_id=1, citation_kind="neutral", citation_text="2019 SCC 65", normalized_citation="2019 SCC 65", refine_version=1, unresolved=True),
			CitationRefined(source_case_id=1, citation_kind="neutral", citation_text="2031 FC 99", normalized_citation="2031 FC 99", refine_version=1, unresolved=True),
			CitationRefined(source_case_id=1, citation_kind="case_name", citation_text="Vavilov", normalized_citation="Vavilov", refine_version=1, unresolved=True),
		]
	)
	session.commit()
	_run(session, monkeypatch)
	assert "DRY RUN" in capsys.readouterr().out
	assert _links(session)["2019 SCC 65"] == (None, True)
	_run(session, monkeypatch, "--apply")
	assert "[neutral: linked=1]" in capsys.readouterr().out
	assert _links(session) == {"2019 SCC 65": (2, False), "2031 FC 99": (None, True), "Vavilov": (None, True)}
	with pytest.raises(SystemExit):
		_run(session, monkeypatch, "--revert")  # refuses without --yes
	_run(session, monkeypatch, "--revert", "--yes")
	assert _links(session)["2019 SCC 65"] == (None, True)


def test_citation_routes_default_to_live_rows_and_flip_with_the_flag(session, monkeypatch) -> None:
	from backend.routes import get_case_incoming_citations, get_case_outgoing_citations

	session.add_all(
		[
			Citation(source_case_id=1, target_case_id=2, citation_kind="neutral", citation_text="legacy-1"),
			CitationRefined(source_case_id=1, target_case_id=2, citation_kind="neutral", citation_text="refined-1", refine_version=1),
			CitationRefineStatus(source_case_id=1, refine_version=1, status="done", case_rows=1, statute_rows=0),
		]
	)
	session.commit()
	monkeypatch.delenv("CITATIONS_SOURCE", raising=False)
	assert [c.citation_text for c in get_case_outgoing_citations(1, session)] == ["legacy-1"]
	assert [c.citation_text for c in get_case_incoming_citations(2, session)] == ["legacy-1"]
	monkeypatch.setenv("CITATIONS_SOURCE", "refined")
	assert [c.citation_text for c in get_case_outgoing_citations(1, session)] == ["refined-1"]
	assert [c.citation_text for c in get_case_incoming_citations(2, session)] == ["refined-1"]
