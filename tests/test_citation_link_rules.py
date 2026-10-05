from backend.citation_link_rules import (
	build_index,
	classify_unresolved,
	cited_name_key,
	keys_for,
	names_compatible,
	resolve_row,
	title_counts_for,
)

CASES = [
	(1, "Baker v. Canada (Minister of Citizenship and Immigration)", "1999 CanLII 699 (SCC)", "[1999] 2 SCR 817"),
	(2, "Nicholson v. Haldimand-Norfolk Regional Board of Commissioners of Police", "[1979] 1 SCR 311", None),
	(3, "R. v. Smith", "[1972] SCR 100", None),
	(4, "Singh v. Canada", "2012 FC 437", None),
	(5, "Singh v. Canada", "2012 FCA 100", None),
	(6, "Maarouf v. Canada (Minister of Employment and Immigration)", "[1994] 1 F.C. 723", None),
	(7, "Twin v. One", "[1990] 2 SCR 50", None),
	(8, "Twin v. Two", "[1990] 2 SCR 50", None),
	(9, "Kamel v. Canada", "(1985), 17 D.L.R. (4th) 422", None),
]
INDEX = build_index(CASES)


def target(text, source=99):
	return resolve_row(text, source, INDEX)


def test_keys_cover_spelling_variants():
	assert [k.value for k in keys_for("[1985] 1 R.C.S. 177")] == ["1985 1 SCR 177"]
	assert [k.value for k in keys_for("[1994] 1 F.C.R. 723")] == ["1994 1 FC 723"]
	assert [k.value for k in keys_for("[1972] S.C.R. 1073")] == ["1972 SCR 1073"]
	assert [k.value for k in keys_for("(1993), 157 N.R. 225 (F.C.A.)")] == ["1993 157 NR 225"]
	assert [k.value for k in keys_for("2012 CAF 196")] == ["2012 FCA 196"]
	assert keys_for("64 ACWS (3d) 844") == []


def test_year_only_scr_is_limited_to_old_reports():
	assert keys_for("[2005] SCR 12") == []


def test_french_neutral_cite_links_by_exact_key():
	assert target("Singh c. Canada, 2012 CF 437").target_case_id == 4
	assert target("Singh c. Canada, 2012 CAF 100").target_case_id == 5


def test_french_neutral_cite_rejects_unrelated_name():
	result = target("Zhang c. Ministre, 2012 CF 437")
	assert result.target_case_id is None and result.reason == "name_mismatch"


def test_year_only_scr_cite_links_when_library_case_has_same_cite():
	result = target("R. v. Smith, [1972] S.C.R. 100")
	assert (result.target_case_id, result.rule) == (3, "reporter_year_only")


def test_reporter_spelling_variants_link():
	assert target("Baker v. Canada, [1999] 2 S.C.R. 817").target_case_id == 1
	assert target("Baker c. Canada, [1999] 2 R.C.S. 817").target_case_id == 1
	assert target("Maarouf v. Canada, [1994] 1 F.C.R. 723").target_case_id == 6


def test_paren_year_series_cite_links():
	assert target("Kamel v. Canada, (1985), 17 D.L.R. (4th) 422").target_case_id == 9


def test_neutral_cite_to_other_court_is_not_linked():
	result = target("Somebody v. Other, 2015 BCSC 435")
	assert result.target_case_id is None and result.reason == "no_hit"


def test_self_cite_is_not_linked():
	assert target("R. v. Smith, [1972] SCR 100", source=3).reason == "self"


def test_shared_key_needs_title_confirmation():
	assert target("Whatever, [1990] 2 SCR 50").reason == "ambiguous"
	assert target("Twin v. Two, [1990] 2 SCR 50").target_case_id == 8
	assert target("Twin v. Three, [1990] 2 SCR 50").reason == "ambiguous"


def test_cited_name_and_compatibility():
	assert cited_name_key("Baker v. Canada (Minister of Citizenship and Immigration), [1999] 2 S.C.R. 817") == (
		"baker v canada minister of citizenship and immigration"
	)
	assert cited_name_key("[1999] 2 S.C.R. 817") == ""
	assert names_compatible("", "anything")
	assert names_compatible("baker v canada", "baker v canada minister")
	assert not names_compatible("zhang v ministre", "singh v canada")


def test_classify_buckets():
	counts = title_counts_for(INDEX)

	def bucket(text, kind="case"):
		return classify_unresolved(text, kind, 99, INDEX, counts)

	assert bucket("Singh c. Canada, 2012 CF 437")[0] == "would_link:neutral_fr"
	assert bucket("X v. Y, 2015 BCSC 435") == ("neutral_other_court", "BCSC")
	assert bucket("X v. Y, 2013 FC 99") == ("neutral_library_court_not_in_library", "FC")
	assert bucket("X v. Y, 2013 CanLII 99 (SCC)")[0] == "canlii_cite_not_in_library"
	assert bucket("X v. Y, [2000] 3 SCR 99")[0] == "reporter_cite_not_in_library"
	assert bucket("Ibid. at para 4")[0] == "back_reference"
	assert bucket("Rajudeen v. M.E.I. (F.C.A., no. A-1779-83)")[0] == "docket_only"
	assert bucket("Foo v. Bar, 64 ACWS (3d) 844")[0] == "reporter_unkeyable"
	assert bucket("Baker v. Canada (Minister of Citizenship and Immigration)", "case_name")[0] == "name_only_title_unique"
	assert bucket("Singh v. Canada", "case_name")[0] == "name_only_ambiguous"
	assert bucket("Nobody v. Nothing", "case_name")[0] == "name_only_not_in_library"


# --- database-backed checks (in-memory SQLite, no network) ---

from datetime import date  # noqa: E402

import pytest  # noqa: E402
from pgvector.sqlalchemy import Vector  # noqa: E402
from sqlalchemy import create_engine, select  # noqa: E402
from sqlalchemy.ext.compiler import compiles  # noqa: E402
from sqlalchemy.orm import Session  # noqa: E402
from sqlalchemy.pool import StaticPool  # noqa: E402

from backend.database import Base, Case, Citation  # noqa: E402


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
	return "JSON"


@pytest.fixture
def session():
	engine = create_engine("sqlite://", poolclass=StaticPool, connect_args={"check_same_thread": False})
	Base.metadata.create_all(engine)
	with Session(engine) as db:
		for case_id, title, citation, secondary in CASES + [(50, "Source v. Case", "2020 FC 1", None)]:
			db.add(Case(id=case_id, title=title, court="SCC" if "SCR" in (citation or "") else "FC", date=date(1999, 1, 1),
				citation=citation, secondary_citation=secondary, full_text="x"))
		db.flush()
		for text, kind in [
			("R. v. Smith, [1972] S.C.R. 100", "case"),
			("Singh c. Canada, 2012 CF 437", "neutral"),
			("X v. Y, 2015 BCSC 435", "neutral"),
			("Ibid. at para 4", "case_short"),
		]:
			db.add(Citation(source_case_id=50, citation_kind=kind, citation_text=text, normalized_citation=text, unresolved=True))
		db.commit()
		yield db


def test_analysis_reports_buckets(session):
	from scripts.analyze_citation_link_coverage import analyze

	report = analyze(session, None, 100, 50)
	assert report["inspected"] == 4
	assert report["buckets"]["would_link:reporter_year_only"] == 1
	assert report["buckets"]["would_link:neutral_fr"] == 1
	assert report["buckets"]["neutral_other_court"] == 1
	assert report["buckets"]["back_reference"] == 1
	assert report["extended_rules_gain"] == 2
	assert report["probe_case"]["id"] == 50


def test_resolver_extended_rules_are_opt_in(session, monkeypatch):
	import scripts.resolve_citation_targets as resolver

	monkeypatch.setattr(resolver, "SessionLocal", lambda: session)
	monkeypatch.setattr(session, "close", lambda: None)

	def linked():
		session.expire_all()
		return sorted(session.scalars(select(Citation.target_case_id).where(Citation.target_case_id.is_not(None))))

	monkeypatch.setattr("sys.argv", ["resolve_citation_targets.py"])
	resolver.main()
	assert linked() == []  # standard rules link none of these
	monkeypatch.setattr("sys.argv", ["resolve_citation_targets.py", "--extended-rules"])
	resolver.main()
	assert linked() == [3, 4]
