from io import BytesIO

import pytest
from docx import Document
from fastapi.testclient import TestClient

from backend import routes
from backend.main import app
from backend.table_of_authorities import (
    CaseMetadata,
    InputLineLimitError,
    ParsedCitation,
    build_docx,
    case_id_lookup_values,
    citation_lookup_values,
    court_order_key,
    parse_submission,
    resolve_case_ids,
    resolve_authorities,
)


CASES = [
    CaseMetadata(
        case_id=1,
        title="Vavilov",
        court="Supreme Court of Canada",
        citation="2019 SCC 65",
        source_url="https://www.canlii.org/en/ca/scc/doc/2019/2019scc65/2019scc65.html",
    ),
    CaseMetadata(
        case_id=2,
        title="Alpha v Canada",
        court="Federal Court",
        citation="2020 FC 10",
        source_url="https://example.org/not-canlii",
    ),
    CaseMetadata(
        case_id=3,
        title="Beta v Canada",
        court="Federal Court",
        citation="2021 FC 20",
        source_url="https://www.canlii.org.evil.example/en/ca/fc/doc/2021/2021fc20/2021fc20.html",
    ),
    CaseMetadata(
        case_id=4,
        title="Federal appeal",
        court="Federal Court of Appeal",
        citation="2022 FCA 30",
    ),
]


def _document_text(content: bytes) -> tuple[list[str], list[str]]:
    document = Document(BytesIO(content))
    paragraphs = [paragraph.text for paragraph in document.paragraphs]
    links = [
        rel.target_ref
        for rel in document.part.rels.values()
        if rel.reltype.endswith("/hyperlink")
    ]
    return paragraphs, links


def test_parser_captures_case_citations_and_paragraph_references():
    parsed = parse_submission(
        "Vavilov, 2019 SCC 65 at paras 23, 25-26\n"
        "2020 FC 10, at para. 7"
    )

    assert len(parsed) == 2
    assert any("2019 SCC 65" in row.citation for row in parsed)
    assert parsed[0].paragraph_refs == ("23", "25–26")
    assert parsed[1].paragraph_refs == ("7",)


def test_unrecognized_nonblank_lines_are_retained_in_docx_not_found_section():
    parsed = parse_submission("\n \t\nUnparseable authority text\n \n")
    assert [item.citation for item in parsed] == ["Unparseable authority text"]

    groups, not_found = resolve_authorities(parsed, CASES)
    paragraphs, _ = _document_text(build_docx(groups, not_found))
    assert paragraphs.index("Not found in local case metadata") < paragraphs.index(
        "Unparseable authority text"
    )

    assert parse_submission("\n \t \n") == []


def test_nonblank_line_limit_includes_200_and_rejects_201():
    accepted = "\n\n".join(f"2020 SCC {index + 1}" for index in range(200))
    assert len(parse_submission(accepted)) == 200

    with pytest.raises(InputLineLimitError, match="200 nonblank lines"):
        parse_submission(accepted + "\n2026 SCC 999")


def test_positive_numeric_lines_are_case_ids_and_nonpositive_lines_are_retained():
    text = "1\n001\n0\n-2\n2020 FC 10"

    assert case_id_lookup_values(text) == [1]
    assert [item.citation for item in parse_submission(text)] == [
        "0",
        "-2",
        "2020 FC 10",
    ]


def test_citation_lookup_values_are_normalized_and_support_fc_aliases():
    parsed = [
        ParsedCitation("2020 FCT 10", ()),
        ParsedCitation("Vavilov v Canada, [2019] 2 S.C.R. 100", ()),
    ]

    assert citation_lookup_values(parsed) == [
        "2019 2 S.C.R. 100",
        "2019 2 SCR 100",
        "2020 FC 10",
        "2020 FCT 10",
    ]


def test_local_metadata_query_is_filtered_to_parsed_citations():
    class FakeSession:
        statement = None

        def execute(self, statement):
            self.statement = statement
            return self

        def all(self):
            return []

    session = FakeSession()
    parsed = parse_submission("2020 FC 10")

    assert routes._table_of_authorities_case_metadata(session, parsed) == []
    sql = str(session.statement.compile(compile_kwargs={"literal_binds": True}))
    assert "WHERE" in sql
    assert "'2020 FC 10'" in sql


def test_local_case_id_metadata_query_is_filtered_to_requested_ids():
    class FakeSession:
        statement = None

        def execute(self, statement):
            self.statement = statement
            return self

        def all(self):
            return []

    session = FakeSession()
    assert routes._table_of_authorities_case_metadata_by_ids(session, [1, 8]) == []
    sql = str(session.statement.compile(compile_kwargs={"literal_binds": True}))

    assert "WHERE" in sql
    assert "cases.id IN (1, 8)" in sql
    assert routes._table_of_authorities_case_metadata_by_ids(session, []) == []


def test_case_id_resolution_handles_known_and_unknown_ids():
    groups, not_found = resolve_case_ids([1, 999], CASES)

    assert [row.title for _, rows in groups for row in rows] == ["Vavilov"]
    assert [row.citation for row in not_found] == ["Case ID 999"]


def test_resolution_groups_in_deterministic_court_order_and_alphabetizes():
    parsed = parse_submission(
        "2021 FC 20\n2020 FC 10\n2022 FCA 30\n2019 SCC 65"
    )
    groups, not_found = resolve_authorities(parsed, CASES)

    assert [court for court, _ in groups] == [
        "Supreme Court of Canada",
        "Federal Court of Appeal",
        "Federal Court",
    ]
    assert [row.title for row in groups[-1][1]] == ["Alpha v Canada", "Beta v Canada"]
    assert not not_found
    assert court_order_key("Federal Court of Appeal") < court_order_key("Federal Court")


def test_unmatched_authorities_appear_in_docx_not_found_section():
    parsed = parse_submission("2099 SCC 777 at para 4")
    groups, not_found = resolve_authorities(parsed, CASES)
    paragraphs, links = _document_text(build_docx(groups, not_found))

    assert any("Not found in local case metadata" in item for item in paragraphs)
    assert any("2099 SCC 777" in item and "paras 4" in item for item in paragraphs)
    assert links == []


def test_docx_contains_resolved_authorities_paragraph_refs_and_only_trusted_local_links():
    parsed = parse_submission("2019 SCC 65, at paras 23, 25-26\n2020 FC 10\n2021 FC 20")
    groups, not_found = resolve_authorities(parsed, CASES)
    paragraphs, links = _document_text(build_docx(groups, not_found))
    text = "\n".join(paragraphs)

    assert "Vavilov" in text
    assert "2019 SCC 65" in text
    assert "paras 23, 25–26" in text
    assert "Alpha v Canada" in text
    assert len(links) == 1
    assert links[0] == CASES[0].source_url
    assert "evil.example" not in "\n".join(links)
    assert "example.org" not in "\n".join(links)


def test_duplicate_local_citation_is_not_arbitrarily_resolved():
    ambiguous = CASES + [
        CaseMetadata(
            case_id=5,
            title="Conflicting local record",
            court="Supreme Court of Canada",
            citation="2019 SCC 65",
        )
    ]
    groups, not_found = resolve_authorities(parse_submission("2019 SCC 65"), ambiguous)

    assert groups == []
    assert [row.citation for row in not_found] == ["2019 SCC 65"]


def test_page_and_post_are_stateless_no_store_and_do_not_log_submission(monkeypatch, caplog):
    sentinel = "PRIVATE_SUBMISSION_SENTINEL"
    monkeypatch.setattr(
        routes, "_table_of_authorities_case_metadata", lambda _db, _parsed: CASES
    )
    app.dependency_overrides[routes.get_db] = lambda: iter([object()])
    client = TestClient(app)
    try:
        page = client.get("/table-of-authorities")
        response = client.post(
            "/table-of-authorities/build",
            data={"text": f"{sentinel} 2099 SCC 777"},
        )
        json_response = client.post(
            "/table-of-authorities",
            json={"text": f"{sentinel} 2099 SCC 777"},
        )
    finally:
        app.dependency_overrides.pop(routes.get_db, None)

    assert page.status_code == 200
    assert "200 nonblank lines" in page.text
    assert page.headers["cache-control"] == "no-store"
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    assert response.content[:2] == b"PK"
    assert json_response.status_code == 200
    assert json_response.headers["cache-control"] == "no-store"
    assert json_response.content[:2] == b"PK"
    output_text, _ = _document_text(response.content)
    json_output_text, _ = _document_text(json_response.content)
    assert sentinel not in "\n".join(output_text)
    assert sentinel not in "\n".join(json_output_text)
    assert sentinel not in caplog.text


def test_json_post_contract_and_mixed_citation_and_id_input(monkeypatch):
    operation = app.openapi()["paths"]["/table-of-authorities"]["post"]
    request_schema = app.openapi()["components"]["schemas"]["TableOfAuthoritiesRequest"]
    assert "one citation or positive local case ID per line" in request_schema["properties"][
        "text"
    ]["description"]
    assert list(operation["requestBody"]["content"]) == ["application/json"]
    assert list(operation["responses"]["200"]["content"]) == [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    monkeypatch.setattr(
        routes, "_table_of_authorities_case_metadata", lambda _db, _parsed: CASES
    )
    monkeypatch.setattr(
        routes,
        "_table_of_authorities_case_metadata_by_ids",
        lambda _db, case_ids: [case for case in CASES if case.case_id in case_ids],
    )
    app.dependency_overrides[routes.get_db] = lambda: iter([object()])
    try:
        response = TestClient(app).post(
            "/table-of-authorities",
            json={"text": "1\n2019 SCC 65\n999"},
        )
        invalid_body = TestClient(app).post("/table-of-authorities", json={})
    finally:
        app.dependency_overrides.pop(routes.get_db, None)

    assert response.status_code == 200
    assert response.headers["content-type"].startswith(
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    assert 'filename="table-of-authorities.docx"' in response.headers["content-disposition"]
    paragraphs, _ = _document_text(response.content)
    text = "\n".join(paragraphs)
    assert text.count("Vavilov") == 1
    assert "Case ID 999" in text
    assert invalid_body.status_code == 422


def test_existing_form_post_still_returns_a_docx_with_case_id_lines(monkeypatch):
    monkeypatch.setattr(
        routes, "_table_of_authorities_case_metadata", lambda _db, _parsed: []
    )
    monkeypatch.setattr(
        routes,
        "_table_of_authorities_case_metadata_by_ids",
        lambda _db, case_ids: [case for case in CASES if case.case_id in case_ids],
    )
    app.dependency_overrides[routes.get_db] = lambda: iter([object()])
    try:
        response = TestClient(app).post(
            "/table-of-authorities/build", data={"text": "1\n999"}
        )
    finally:
        app.dependency_overrides.pop(routes.get_db, None)

    assert response.status_code == 200
    paragraphs, _ = _document_text(response.content)
    text = "\n".join(paragraphs)
    assert "Vavilov" in text
    assert "Case ID 999" in text


@pytest.mark.parametrize("use_json", [False, True])
def test_post_returns_clear_422_for_more_than_200_nonblank_lines(monkeypatch, use_json):
    metadata_calls = []
    monkeypatch.setattr(
        routes, "_table_of_authorities_case_metadata",
        lambda _db, _parsed: metadata_calls.append(True) or CASES,
    )
    monkeypatch.setattr(routes, "_table_of_authorities_case_metadata_by_ids", lambda *_: [])
    app.dependency_overrides[routes.get_db] = lambda: iter([object()])
    try:
        client = TestClient(app)
        text = "\n".join(f"2020 SCC {i + 1}" for i in range(201))
        response = (
            client.post("/table-of-authorities", json={"text": text})
            if use_json
            else client.post("/table-of-authorities/build", data={"text": text})
        )
    finally:
        app.dependency_overrides.pop(routes.get_db, None)

    assert response.status_code == 422
    assert "200 nonblank lines" in response.json()["detail"]
    assert metadata_calls == []
