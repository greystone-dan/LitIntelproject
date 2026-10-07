"""Case fingerprints: deterministic terms, roles, subject vs authority rankings, and storage."""

import pytest
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend.case_fingerprint import (
    FINGERPRINT_VERSION,
    CaseFingerprint,
    FingerprintIndex,
    authority_key,
    compute_fingerprint,
    paragraph_role_spans,
    statute_key,
)
from backend.case_fingerprint_store import load_index, rebuild_case_fingerprint, rebuild_missing
from backend.database import Base, Case, CaseFingerprintRecord


@compiles(Vector, "sqlite")
def _sqlite_vector_type(_type, _compiler, **_kw):
    return "JSON"


HC = """Decision Content

[1] This is an application for judicial review of a decision refusing an application for permanent residence on humanitarian and compassionate grounds under subsection 25(1) of the Immigration and Refugee Protection Act, SC 2001, c 27.
[2] The applicant arrived in Canada in 2012 and claimed refugee protection. The officer found that the best interests of the child did not justify an exemption.
[3] The standard of review is reasonableness. See Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65.
[4] In my view, the officer's treatment of the best interests of the child was unreasonable. Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 requires the interests of children to be well identified and defined.
[5] For these reasons, the application is allowed and the matter is returned for redetermination by a different officer.
"""

HC2 = HC.replace("2012", "2015").replace("best interests of the child", "hardship the applicant would face")
CITIZENSHIP = """Decision Content

[1] This is an appeal under subsection 14(5) of the Citizenship Act, RSC 1985, c C-29 from the decision of a citizenship judge denying the application for citizenship because the residence requirement in paragraph 5(1)(c) was not met.
[2] The appellant was absent from Canada for long periods. The judge applied the Koo test, Re Koo, [1993] 1 FC 286.
[3] In my view the decision was reasonable. The appeal is dismissed.
"""


def test_keys_normalise_authorities_and_statutes():
    assert authority_key("Canada v Vavilov, 2019 SCC 65, [2019] 4 SCR 653") == "2019 scc 65"
    assert authority_key("2015 FCT 12") == "2015 fc 12"
    assert authority_key("Vavilov, supra") is None
    assert statute_key("Immigration and Refugee Protection Act, S.C. 2001, c. 27, s. 25(1)") == "Immigration and Refugee Protection Act s25"


def test_fingerprint_is_deterministic_and_role_tagged():
    first = compute_fingerprint(HC, own_citation="2020 FC 100")
    second = compute_fingerprint(HC, own_citation="2020 FC 100")
    assert first == second
    assert first.version == FINGERPRINT_VERSION
    assert first.terms, "tags or statutes should be found"
    assert all(key.startswith(("t:", "s:")) and "@" in key for key in first.terms)
    roles = {key.rsplit("@", 1)[1] for key in first.terms}
    assert roles <= {"metadata", "overview", "facts", "issues", "analysis", "disposition"}
    assert sum(first.plain_terms().values()) == sum(first.terms.values())
    assert first.role_chars and sum(first.role_chars.values()) <= len(HC)


def test_authorities_exclude_self_and_aliases():
    fingerprint = compute_fingerprint(HC, own_citation="2019 SCC 65")
    assert "2019 scc 65" not in fingerprint.authorities
    assert "1999 2 scr 817" in fingerprint.authorities


def test_empty_text_gives_empty_fingerprint():
    fingerprint = compute_fingerprint("")
    assert fingerprint.terms == {} and fingerprint.authorities == {}
    assert paragraph_role_spans("") == []


def _index():
    items = [(1, compute_fingerprint(HC)), (2, compute_fingerprint(HC2)), (3, compute_fingerprint(CITIZENSHIP))]
    return FingerprintIndex(items, min_df_plain=1, min_df_role=1, min_df_authority=1)


def test_similar_by_subject_prefers_same_subject():
    ranked = _index().similar_by_subject(1, k=2)
    assert [case_id for case_id, _ in ranked][0] == 2
    assert ranked[0][1] > 0.5
    assert all(case_id != 1 for case_id, _ in ranked)


def test_shares_authorities_is_a_separate_ranking():
    index = _index()
    shared = index.shares_authorities(1, k=2)
    assert shared[0][0] == 2  # same two authorities
    assert index.shares_authorities(3, k=2) == []  # cites nothing the others cite
    assert index.explain_subject(1, 2)


def test_unknown_case_returns_nothing():
    assert _index().similar_by_subject(99) == []


@pytest.fixture()
def session():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        yield db


def _case(case_id, title, text, citation=None):
    from datetime import date

    return Case(id=case_id, title=title, court="FC", date=date(2020, 1, 1), citation=citation, full_text=text)


def test_store_roundtrip_and_index(session):
    session.add_all([_case(1, "A", HC, "2020 FC 1"), _case(2, "B", HC2, "2020 FC 2"), _case(3, "C", CITIZENSHIP, "2020 FC 3"), _case(4, "D", None)])
    session.commit()
    assert rebuild_missing(session, batch_size=2) == 3  # case 4 has no text
    assert rebuild_missing(session) == 0  # idempotent
    stored = session.get(CaseFingerprintRecord, 1)
    assert stored.version == FINGERPRINT_VERSION and stored.terms
    index = load_index(session)
    assert index.case_ids == [1, 2, 3]
    index = FingerprintIndex(
        [(r.case_id, CaseFingerprint(r.version, r.terms, r.authorities)) for r in session.query(CaseFingerprintRecord)],
        min_df_plain=1, min_df_role=1, min_df_authority=1,
    )
    assert index.similar_by_subject(1, k=1)[0][0] == 2


def test_rebuild_replaces_old_version(session):
    session.add(_case(1, "A", HC, "2020 FC 1"))
    session.commit()
    rebuild_case_fingerprint(session, session.get(Case, 1))
    session.commit()
    session.get(CaseFingerprintRecord, 1).version = "cfp-0"
    session.commit()
    assert rebuild_missing(session) == 1
    assert session.get(CaseFingerprintRecord, 1).version == FINGERPRINT_VERSION


def test_statute_scan_is_windowed_and_offsets_survive():
    filler = "[9] The officer considered the evidence and the submissions of counsel at length.\n" * 600
    text = HC + filler + "[900] Section 25(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 applies.\n"
    assert len(text) > 30000
    fingerprint = compute_fingerprint(text)
    assert any(key.startswith("s:Immigration and Refugee Protection Act s25") for key in fingerprint.terms)


def test_rebuild_missing_filters_court_and_ends_transactions(session):
    session.add_all([_case(1, "A", HC, "2020 FC 1"), _case(2, "B", HC2, "2020 FC 2")])
    session.get(Case, 2).court = "Federal Court of Appeal"
    session.commit()
    assert rebuild_missing(session, court="FCA") == 1
    assert session.get(CaseFingerprintRecord, 2) is not None and session.get(CaseFingerprintRecord, 1) is None
    assert rebuild_missing(session, court="FC", max_duty=0.99) == 1


def test_rebuild_missing_with_workers_matches_single_process(session):
    session.add_all([_case(1, "A", HC, "2020 FC 1"), _case(2, "B", HC2, "2020 FC 2")])
    session.commit()
    assert rebuild_missing(session, workers=2) == 2
    parallel = {r.case_id: dict(r.terms) for r in session.query(CaseFingerprintRecord)}
    session.query(CaseFingerprintRecord).delete()
    session.commit()
    assert rebuild_missing(session, workers=1) == 2
    assert parallel == {r.case_id: dict(r.terms) for r in session.query(CaseFingerprintRecord)}


def test_similar_cases_payload_and_empty_state(session):
    from backend import similar_cases

    similar_cases.reset_cache()
    assert similar_cases.build_similar_cases(session, 1)["available"] is False  # nothing stored yet: panel stays hidden
    session.add_all([_case(1, "A", HC, "2020 FC 1"), _case(2, "B", HC2, "2020 FC 2"), _case(3, "C", CITIZENSHIP, "2020 FC 3")])
    session.commit()
    rebuild_missing(session)
    index = FingerprintIndex(
        [(r.case_id, CaseFingerprint(r.version, r.terms, r.authorities, r.text_length or 0, r.role_chars or {})) for r in session.query(CaseFingerprintRecord)],
        min_df_plain=1, min_df_role=1, min_df_authority=1,
    )
    payload = similar_cases.build_similar_cases(session, 1, index=index)
    assert payload["available"] is True
    assert payload["similar"][0]["case_id"] == 2 and payload["similar"][0]["shared"]
    assert all(row["case_id"] != 1 for row in payload["similar"] + payload["shares_authorities"])
    assert payload["shares_authorities"][0]["case_id"] == 2
    assert similar_cases.build_similar_cases(session, 999, index=index)["available"] is False


def test_similar_cases_route_is_registered_and_answers(session):
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from backend import similar_cases
    from backend.database import get_db
    from backend.routes import router

    similar_cases.reset_cache()
    app = FastAPI()
    app.include_router(router)  # the real route table, so a missing registration fails here
    app.dependency_overrides[get_db] = lambda: session
    body = TestClient(app).get("/api/cases/1/similar-cases").json()
    assert body == {"available": False, "case_id": 1, "similar": [], "shares_authorities": []}
