"""Offline contracts for ephemeral proposition research (SQLite fixtures only)."""

from datetime import date
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from backend import precedent_finder as service
from backend.database import Case, CaseChunk, CaseTag, Citation, get_db
from backend.legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION


@pytest.fixture
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    @event.listens_for(engine, "connect")
    def functions(connection, _):
        connection.create_function("strpos", 2, lambda text, needle: text.find(needle) + 1
                                   if text is not None and needle is not None else None)

    for model in (Case, CaseChunk, CaseTag, Citation):
        model.__table__.create(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


def case(db, number, *, day=date(2020, 1, 1), outcome=None, **kwargs):
    metadata = {"reader_extracted": {"government outcome": outcome}} if outcome else {}
    db.add(Case(id=number, title=f"Decision {number}", court="FC", date=day,
                citation=f"2020 FC {number}", metadata_json=metadata, **kwargs))
    db.flush()


def tag(db, owner, value="fairness", *, taxonomy=ACTIVE_TAG_TAXONOMY_VERSION, offset=0):
    db.add(CaseTag(case_id=owner, category="issue", value=value, score=1,
                   evidence=value, offset_start=offset, offset_end=offset + len(value),
                   source="core_whitelist", taxonomy_version=taxonomy))
    db.flush()


def cite(db, source, target, kind="neutral"):
    db.add(Citation(source_case_id=source, target_case_id=target,
                    citation_kind=kind, normalized_citation="2020 FC 100"))
    db.flush()


@pytest.fixture
def fixed_tagger(monkeypatch):
    class Tagger:
        def tag(self, text):
            return [SimpleNamespace(category="issue", value=value)
                    for value in ("fairness", "reasons") if value in text]
    monkeypatch.setattr(service, "CoreLegalTaggerV3", Tagger)


def source_paragraphs(db, owner, paragraphs, *, prefix="Source header\n", label=None):
    """Stored canonical paragraphs; chunk indices intentionally are not numbers."""
    case(db, owner, full_text=prefix + "\n".join(text for _, text in paragraphs))
    if label is not None:
        db.get(Case, owner).citation = label
    chunks = []
    for index, (number, text) in enumerate(paragraphs):
        chunk = CaseChunk(case_id=owner, chunk_set="paragraph", chunk_index=900 + index,
                          paragraph_start=number, paragraph_end=number, text=text,
                          text_hash=f"{owner}-{index}", token_estimate=10)
        db.add(chunk)
        chunks.append(chunk)
    db.flush()
    return chunks


def stored_citation(db, owner, target, text, *, chunk=None, **kwargs):
    full = db.get(Case, owner).full_text
    start = (chunk.text if chunk else full).index(text)
    row = Citation(source_case_id=owner, target_case_id=target,
                   chunk_id=chunk.id if chunk else None,
                   citation_kind="neutral", citation_text=text, normalized_citation=text,
                   offset_start=start, offset_end=start + len(text),
                   target_paragraph=400, **kwargs)
    db.add(row)
    db.flush()
    return row


@pytest.mark.parametrize("local", [False, True])
def test_verified_source_paragraph_not_authority_header_or_target_pinpoint(db, fixed_tagger, local):
    paragraph = "[7] 😀 See 2020 FC 100 for the applicable test."
    chunks = source_paragraphs(db, 1, [(6, "[6] Background."), (7, paragraph)])
    tag(db, 1)  # Decision-level retrieval, not evidence that this paragraph is tagged.
    case(db, 100, full_text="TARGET HEADER\n[400] Target pinpoint is not the source.")
    citation = stored_citation(db, 1, 100, "2020 FC 100", chunk=chunks[1] if local else None)
    payload = service.find_precedents("fairness", db)
    row = payload["authorities"][0]
    assert row["excerpt"] == paragraph
    assert row["excerpt_source"] == {
        "source_case_id": 1, "source_citation": "2020 FC 1",
        "paragraph_number": 7, "citation_row_id": citation.id,
        "matched_tags": ["issue:fairness"], "matched_tag_count": 1,
        "basis": row["excerpt_source"]["basis"],
    }
    assert "decision-level, not paragraph tag evidence" in row["excerpt_source"]["basis"]
    assert payload["coverage"]["paragraph_rows_checked"] == 2
    assert not payload["coverage"]["partial"]
    assert "TARGET" not in row["excerpt"]
    assert not db.new and not db.dirty and not db.deleted


@pytest.mark.parametrize("fault", [
    "no-chunk", "no-span", "negative", "empty", "outside", "text",
    "canonical-mismatch", "duplicate-paragraph", "repeat", "number",
    "grouped", "unnumbered", "oversized", "wrong-owner", "ambiguous-citation-chunk",
    "missing-citation-chunk", "chunk-index", "header-citation",
])
def test_unverifiable_source_excerpt_is_omitted_not_guessed(db, fixed_tagger, fault):
    paragraph = "[7] See 2020 FC 100."
    chunks = source_paragraphs(db, 1, [(7, paragraph)])
    tag(db, 1)
    case(db, 100, full_text="A tempting target header fallback")
    citation = stored_citation(db, 1, 100, "2020 FC 100", chunk=chunks[0])
    chunk = chunks[0]
    if fault == "no-chunk":
        citation.chunk_id = None
        chunk.chunk_set = "legacy"  # No paragraph rows, without ORM delete cascades.
    elif fault == "no-span":
        citation.offset_start = citation.offset_end = None
    elif fault == "negative":
        citation.offset_start = -1
    elif fault == "empty":
        citation.offset_end = citation.offset_start
    elif fault == "outside":
        citation.offset_end = 100000
    elif fault == "text":
        citation.citation_text = "different text"
    elif fault == "canonical-mismatch":
        db.get(Case, 1).full_text = "[7] A different canonical paragraph."
    elif fault == "duplicate-paragraph":
        db.add(CaseChunk(case_id=1, chunk_set="paragraph", chunk_index=901,
                         paragraph_start=7, paragraph_end=7, text="[7] Other.",
                         text_hash="duplicate", token_estimate=2))
    elif fault == "repeat":
        db.get(Case, 1).full_text += "\n" + paragraph
    elif fault == "number":
        chunk.paragraph_start = chunk.paragraph_end = 400
    elif fault == "grouped":
        chunk.text += "\n[8] Another paragraph."
        chunk.paragraph_end = 8
        db.get(Case, 1).full_text = "Header\n" + chunk.text
    elif fault == "unnumbered":
        chunk.text = "See 2020 FC 100."
        db.get(Case, 1).full_text = chunk.text
        citation.offset_start = chunk.text.index("2020 FC 100")
        citation.offset_end = citation.offset_start + len("2020 FC 100")
    elif fault == "oversized":
        chunk.text += "x" * service.TEXT_CHARS
        db.get(Case, 1).full_text = chunk.text
    elif fault == "wrong-owner":
        other = source_paragraphs(db, 2, [(7, paragraph)])[0]
        citation.chunk_id = other.id
    elif fault == "missing-citation-chunk":
        citation.chunk_id = 99999
    elif fault == "chunk-index":
        chunk.chunk_index = 7
        chunk.paragraph_start = chunk.paragraph_end = None
    elif fault == "header-citation":
        db.get(Case, 1).full_text = "Header cites 2020 FC 100\n" + paragraph
        citation.chunk_id = None
        citation.offset_start = len("Header cites ")
        citation.offset_end = citation.offset_start + len("2020 FC 100")
    else:
        # Ambiguous local base, even though the numbered paragraph itself is unique.
        other = CaseChunk(case_id=1, chunk_set="legacy", chunk_index=902,
                          text="2020 FC 100", text_hash="ambiguous", token_estimate=2)
        db.add(other)
        db.flush()
        citation.chunk_id = other.id
        citation.offset_start = 0
        citation.offset_end = len(other.text)
        db.get(Case, 1).full_text += "\nUnnumbered 2020 FC 100."
    db.flush()
    row = service.find_precedents("fairness", db)["authorities"][0]
    assert row["excerpt"] is None and row["excerpt_source"] is None
    assert row["matching_citing_decisions"] == 1  # Discovery/ranking unchanged.


def test_deterministic_source_choice_all_tie_breakers(db, fixed_tagger):
    case(db, 100)
    citations = {}
    for owner, label, tags in (
        (1, "A", ["fairness"]), (2, "B", ["fairness", "reasons"]),
        (4, "A", ["fairness", "reasons"]), (3, "A", ["fairness", "reasons"]),
    ):
        chunks = source_paragraphs(db, owner, [
            (7, "[7] See 2020 FC 100 and again 2020 FC 100."),
            (8, "[8] Also see 2020 FC 100."),
        ], label=label)
        for value in tags:
            tag(db, owner, value)
        tag(db, owner, offset=50)  # Duplicate tag does not increase distinct count.
        stored_citation(db, owner, 100, "2020 FC 100", chunk=chunks[1])
        citations[owner] = stored_citation(db, owner, 100, "2020 FC 100", chunk=chunks[0])
        stored_citation(db, owner, 100, "2020 FC 100", chunk=chunks[0])
    first = service.find_precedents("fairness reasons", db)
    second = service.find_precedents("fairness reasons", db)
    assert first == second
    source = first["authorities"][0]["excerpt_source"]
    assert (source["source_case_id"], source["source_citation"], source["paragraph_number"],
            source["citation_row_id"], source["matched_tag_count"]) == (3, "A", 7, citations[3].id, 2)
    # An invalid best source must not suppress a valid lower-ranked source.
    for citation in db.query(Citation).filter_by(source_case_id=3):
        citation.citation_text = "invalid"
    db.flush()
    assert service.find_precedents("fairness reasons", db)["authorities"][0]["excerpt_source"]["source_case_id"] == 4


@pytest.mark.parametrize("invalid_anchor", [False, True])
def test_short_citation_local_occurrence_document_anchor(db, fixed_tagger, invalid_anchor):
    chunks = source_paragraphs(db, 1, [
        (6, "[6] See 2020 FC 100 (Smith)."), (7, "[7] Smith applies."),
    ])
    tag(db, 1)
    case(db, 100)
    citation = stored_citation(db, 1, 100, "Smith", chunk=chunks[1])
    citation.citation_kind = "case_short"
    citation.anchor_citation_text = "2020 FC 100"
    start = db.get(Case, 1).full_text.index(citation.anchor_citation_text)
    citation.anchor_offset_start = start if not invalid_anchor else 0
    citation.anchor_offset_end = start + len(citation.anchor_citation_text)
    db.flush()
    row = service.find_precedents("fairness", db)["authorities"][0]
    if invalid_anchor:
        assert row["excerpt"] is None
    else:
        assert row["excerpt"] == "[7] Smith applies."
        assert row["excerpt_source"]["paragraph_number"] == 7


@pytest.mark.parametrize("prefix,available", [
    ("Court header\nDecision Content\n1 Background.\n", True),
    ("Court header\n", False),
    ("Court header\nDecision Content\n1 Background.\n4 Gap.\n", False),
])
def test_bare_numbered_paragraph_requires_real_formatter_context(db, fixed_tagger, prefix, available):
    chunk = source_paragraphs(db, 1, [(2, "2 See 2020 FC 100.")], prefix=prefix)[0]
    tag(db, 1)
    case(db, 100)
    stored_citation(db, 1, 100, "2020 FC 100", chunk=chunk)
    row = service.find_precedents("fairness", db)["authorities"][0]
    assert bool(row["excerpt"]) is available


@pytest.mark.parametrize("local", [False, True])
@pytest.mark.parametrize("bare", [False, True])
@pytest.mark.parametrize("tail", [
    "SOLICITORS OF RECORD\n2020 FC 100",
    "I. Authorities including 2020 FC 100",
    "[1] (2020) See 2020 FC 100.",
    '"Justice Smith"\nSee 2020 FC 100.',
    "Judgment delivered at Ottawa\nSee 2020 FC 100.",
])
def test_structured_tail_citation_is_not_source_paragraph(db, fixed_tagger, tail, bare, local):
    paragraph = ("2" if bare else "[7]") + " Background.\n" + tail
    prefix = "Court header\nDecision Content\n1 Background.\n" if bare else "Source header\n"
    chunk = source_paragraphs(db, 1, [(2 if bare else 7, paragraph)], prefix=prefix)[0]
    tag(db, 1)
    case(db, 100)
    stored_citation(db, 1, 100, "2020 FC 100", chunk=chunk if local else None)
    payload = service.find_precedents("fairness", db)
    row = payload["authorities"][0]
    assert row["excerpt"] is None and row["excerpt_source"] is None
    assert row["matching_citing_decisions"] == 1
    assert payload["coverage"]["paragraph_rows_checked"] == 1
    assert not payload["coverage"]["partial"]


@pytest.mark.parametrize("bare", [False, True])
@pytest.mark.parametrize("tail", [
    "The applicable test is set out in 2020 FC 100.",
    "(a) Apply the test in 2020 FC 100.",
    ("“The applicable test is set out in 2020 FC 100, and must be applied "
     "in light of all the circumstances of the particular case.”"),
])
def test_paragraph_continuation_list_and_quote_remain_eligible(db, fixed_tagger, tail, bare):
    paragraph = ("2" if bare else "[7]") + " Background.\n" + tail
    prefix = "Court header\nDecision Content\n1 Background.\n" if bare else "Source header\n"
    chunk = source_paragraphs(db, 1, [(2 if bare else 7, paragraph)], prefix=prefix)[0]
    tag(db, 1)
    case(db, 100)
    stored_citation(db, 1, 100, "2020 FC 100", chunk=chunk)
    row = service.find_precedents("fairness", db)["authorities"][0]
    assert row["excerpt"] == paragraph
    assert row["excerpt_source"]["paragraph_number"] == (2 if bare else 7)


def test_global_paragraph_budget_charges_invalid_rows_and_bounds_projections(db, fixed_tagger, monkeypatch):
    monkeypatch.setattr(service, "PARAGRAPHS_TOTAL", 2)
    monkeypatch.setattr(service, "PARAGRAPHS_PER_DECISION", 1)
    case(db, 100, full_text="Never project this target text")
    for owner in (1, 2, 3):
        chunk = source_paragraphs(db, owner, [(7, "[7] See 2020 FC 100.")])[0]
        tag(db, owner)
        stored_citation(db, owner, 100, "2020 FC 100", chunk=chunk)
        chunk.paragraph_start = chunk.paragraph_end = 99  # Charged although rejected.
    db.flush()
    statements = []
    event.listen(db.bind, "before_cursor_execute",
                 lambda conn, cursor, sql, params, context, many: statements.append(sql))
    payload = service.find_precedents("fairness", db)
    assert payload["coverage"]["partial"]
    assert payload["coverage"]["paragraph_row_budget"] == 2
    assert payload["coverage"]["paragraph_rows_checked"] == 2
    assert payload["authorities"][0]["excerpt"] is None
    selects = [sql for sql in statements if sql.lstrip().startswith("SELECT")]
    assert all("LIMIT" in sql for sql in selects)
    assert not any("embedding" in sql for sql in selects)
    assert not any(sql.lstrip().startswith(("INSERT", "UPDATE", "DELETE")) for sql in statements)
    for sql in selects:
        # Every full_text use is a server-side bounded span/location expression;
        # no ORM Case or CaseChunk projection can sneak in.
        projection = sql.split("\nFROM")[0]
        assert "SELECT cases.full_text" not in projection
        assert ", cases.full_text" not in projection
        assert "SELECT case_chunks.text" not in projection
        assert ", case_chunks.text AS" not in projection
    target_query = next(sql for sql in selects if "cases.court" in sql)
    assert "full_text" not in target_query


def test_complete_citing_paragraph_not_header_or_truncated_before_citation(db, fixed_tagger):
    paragraph = "[7] " + "Background. " * 40 + "See 2020 FC 100."
    chunk = source_paragraphs(db, 1, [(7, paragraph)])[0]
    tag(db, 1)
    case(db, 100)
    stored_citation(db, 1, 100, "2020 FC 100", chunk=chunk)
    assert service.find_precedents("fairness", db)["authorities"][0]["excerpt"] == paragraph


def test_paragraph_budget_is_shared_across_authorities_in_source_preference_order(db, fixed_tagger, monkeypatch):
    monkeypatch.setattr(service, "PARAGRAPHS_TOTAL", 2)
    for owner, target, label in ((1, 100, "A"), (2, 101, "B"), (3, 102, "A")):
        case(db, target)
        chunk = source_paragraphs(db, owner, [(7, f"[7] See 2020 FC {target}.")], label=label)[0]
        tag(db, owner)
        if owner != 1:
            tag(db, owner, "reasons")
        stored_citation(db, owner, target, f"2020 FC {target}", chunk=chunk)
    payload = service.find_precedents("fairness reasons", db)
    by_target = {row["case_id"]: row for row in payload["authorities"]}
    assert payload["coverage"]["paragraph_rows_checked"] == 2
    assert payload["coverage"]["partial"]
    assert by_target[102]["excerpt_source"]["source_case_id"] == 3
    assert by_target[101]["excerpt_source"]["source_case_id"] == 2
    assert by_target[100]["excerpt"] is None


@pytest.mark.parametrize("budget", ["PARAGRAPHS_PER_DECISION", "CITATIONS_PER_DECISION"])
def test_excerpt_verification_cannot_expand_discovery_or_paragraph_budget(db, fixed_tagger, monkeypatch, budget):
    monkeypatch.setattr(service, budget, 1)
    case(db, 100)
    chunks = source_paragraphs(db, 1, [
        (6, "[6] Not a citation paragraph."), (7, "[7] See 2020 FC 100."),
    ])
    tag(db, 1)
    # First discovery row is invalid. A valid lookahead occurrence is not eligible.
    cite(db, 1, 100)
    stored_citation(db, 1, 100, "2020 FC 100", chunk=chunks[1])
    payload = service.find_precedents("fairness", db)
    assert payload["coverage"]["partial"]
    assert payload["authorities"][0]["excerpt"] is None
    if budget == "PARAGRAPHS_PER_DECISION":
        assert payload["coverage"]["paragraph_rows_checked"] == 1


def test_lexicographic_counts_duplicates_and_outcome_denominator(db, fixed_tagger):
    for number, outcome in ((1, "won"), (2, "lost"), (3, None), (4, "mixed")):
        case(db, number, outcome=outcome)
        tag(db, number)
    tag(db, 2, offset=20)  # A second occurrence is not a second decision/tag.
    tag(db, 3, "reasons")
    tag(db, 4, "reasons")
    for number, day in ((100, date(2000, 1, 1)), (101, date(2025, 1, 1)),
                        (102, date(2024, 1, 2)), (103, date(2024, 1, 1)),
                        (104, date(2024, 1, 1))):
        case(db, number, day=day, full_text="Authority source excerpt.")
    for owner in (1, 2, 3):
        cite(db, owner, 100)
    cite(db, 1, 100)  # Occurrence duplication must not inflate denominator.
    cite(db, 1, 101)
    cite(db, 2, 101)
    for target in (104, 103, 102):
        cite(db, 3, target)
        cite(db, 4, target)
    payload = service.find_precedents("fairness reasons fairness", db)
    rows = payload["authorities"]
    assert [row["case_id"] for row in rows] == [100, 102, 103, 104, 101]
    assert rows[0]["rank_numbers"] == [3, 2, 20000101]
    assert rows[0]["matched_tags"] == ["issue:fairness", "issue:reasons"]
    assert rows[0]["matching_citing_decisions"] == 3
    assert rows[0]["outcome_mix"] == {
        "government_won": 1, "government_lost": 1, "mixed": 0, "unclassified": 1,
        "denominator": 3,
        "basis": "Stored reader_extracted government outcomes of matching "
                 "citing decisions; not outcomes of the authority.",
    }
    assert rows[1]["outcome_mix"]["mixed"] == 1
    assert rows[0]["excerpt"] is None  # Never fall back to the target's header.
    assert rows[0]["excerpt_source"] is None
    assert rows[0]["court"] == "FC"
    assert rows[0]["date"] == "2000-01-01"
    assert not payload["coverage"]["partial"]
    assert "proposition" not in payload
    assert not db.new and not db.dirty and not db.deleted


def test_citation_tie_and_missing_excerpt(db, fixed_tagger):
    case(db, 1)
    tag(db, 1)
    for number, citation in ((100, "2020 FC Z"), (101, "2020 FC A")):
        case(db, number)
        db.get(Case, number).citation = citation
        cite(db, 1, number)
    db.flush()
    rows = service.find_precedents("fairness", db)["authorities"]
    assert [row["case_id"] for row in rows] == [101, 100]
    assert rows[0]["excerpt"] is None
    assert rows[0]["outcome_mix"]["unclassified"] == 1


@pytest.mark.parametrize("source", ["synthetic", "staged", "discovered", "activity",
                                   "reference_library", "side_project"])
def test_noncanonical_sources_and_targets_excluded(db, fixed_tagger, source):
    case(db, 1)
    case(db, 2, source_type=source)
    case(db, 100)
    case(db, 101, source_type=source)
    tag(db, 1)
    tag(db, 2)
    cite(db, 1, 100)
    cite(db, 2, 100)
    cite(db, 1, 101)
    rows = service.find_precedents("fairness", db)["authorities"]
    assert [row["case_id"] for row in rows] == [100]
    assert rows[0]["matching_citing_decisions"] == 1


def test_old_tags_statutes_unresolved_self_and_noncanonical_datasets(db, fixed_tagger):
    for number in (1, 2, 100, 101, 102, 103):
        case(db, number)
    case(db, 3, dataset_version="synthetic-fixture")
    case(db, 104, dataset_version="reference-library-v1")
    tag(db, 1)
    tag(db, 2, taxonomy="old")
    tag(db, 3)
    cite(db, 1, 100)
    cite(db, 2, 101)
    cite(db, 3, 102)
    cite(db, 1, 103, kind="statute")
    cite(db, 1, 104)
    cite(db, 1, None)
    cite(db, 1, 1)
    assert [row["case_id"] for row in service.find_precedents("fairness", db)["authorities"]] == [100]


def test_posting_budget_charges_duplicates_and_every_query_bounded(db, fixed_tagger, monkeypatch):
    monkeypatch.setattr(service, "POSTINGS_PER_TAG", 2)
    for number in (1, 2, 100):
        case(db, number)
    tag(db, 1)
    tag(db, 1, offset=20)
    tag(db, 2)
    cite(db, 1, 100)
    cite(db, 2, 100)
    statements = []
    event.listen(db.bind, "before_cursor_execute",
                 lambda conn, cursor, statement, params, context, many: statements.append(statement))
    payload = service.find_precedents("fairness", db)
    assert payload["coverage"]["partial"]
    assert payload["authorities"][0]["matching_citing_decisions"] == 1
    assert all("LIMIT" in sql for sql in statements if sql.lstrip().startswith("SELECT"))
    assert not any("SELECT cases.full_text" in sql for sql in statements)
    assert "ORDER BY case_tags.case_id, case_tags.id" in statements[0]
    assert not any(sql.lstrip().startswith(("INSERT", "UPDATE", "DELETE")) for sql in statements)


@pytest.mark.parametrize("budget", ["CITING_DECISIONS", "CITATIONS_PER_DECISION", "AUTHORITIES"])
def test_each_discovery_budget_reports_partial(db, fixed_tagger, monkeypatch, budget):
    monkeypatch.setattr(service, budget, 1)
    for number in (1, 2, 100, 101):
        case(db, number)
    for owner in (1, 2):
        tag(db, owner)
        cite(db, owner, 100)
        cite(db, owner, 101)
    assert service.find_precedents("fairness", db)["coverage"]["partial"]


def test_empty_tagless_and_real_extractors():
    class NoDatabase:
        def execute(self, *_):
            raise AssertionError("Tagless inputs must not query the database")
    assert "Enter" in service.find_precedents("", NoDatabase())["message"]
    payload = service.find_precedents("hello", NoDatabase())
    assert payload["authorities"] == []
    assert "No V3 legal tags" in payload["message"]
    # Use the real V3 engine, but empty postings for the real recognized phrase.
    class EmptyDatabase:
        def execute(self, *_):
            return []
    payload = service.find_precedents("IRPA s. 34(1)(f)", EmptyDatabase())
    assert payload["statutes"]
    assert "34(1)(f)" in " ".join(payload["statutes"])
    payload = service.find_precedents("procedural fairness", EmptyDatabase())
    assert payload["tags"]
    assert "No resolved canonical authorities" in payload["message"]


@pytest.fixture
def client(monkeypatch):
    from backend import routes
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[get_db] = lambda: object()
    monkeypatch.setattr(routes, "find_precedents", lambda proposition, db: {
        "tags": [], "statutes": [], "authorities": [], "message": "No matches",
        "coverage": {"partial": False, "note": "Bounded"},
    })
    return TestClient(app)


@pytest.mark.parametrize("body", [
    {}, {"proposition": 12}, {"proposition": None}, {"proposition": ["private-secret"]},
    {"proposition": {"private-secret": "value"}}, ["private-secret"],
    {"other": "private-secret"}, {"proposition": "ok", "other": "private-secret"},
])
def test_validation_never_echoes_input(client, body, caplog):
    response = client.post("/precedent-finder", json=body)
    assert response.status_code == 422
    assert "private-secret" not in response.text
    assert "private-secret" not in caplog.text
    assert response.headers["cache-control"] == "no-store"


def test_malformed_json_and_body_byte_limit(client, caplog):
    for body, status in ((b'{"proposition":"private-secret"', 422),
                         (b"\xffprivate-secret", 422),
                         (b"private-secret" * 4000, 413)):
        response = client.post("/precedent-finder", content=body,
                               headers={"Content-Type": "application/json"})
        assert response.status_code == status
        assert "private-secret" not in response.text
        assert response.headers["cache-control"] == "no-store"
    assert "private-secret" not in caplog.text


def test_character_limit_and_json_unicode(client, monkeypatch, caplog):
    from backend import routes
    calls = []
    def analyze(proposition, db):
        calls.append(len(proposition))
        return {"authorities": []}
    monkeypatch.setattr(routes, "find_precedents", analyze)
    for text in ("x" * 3000, "😀" * 3000):
        assert client.post("/precedent-finder", json={"proposition": text}).status_code == 200
    rejected = "private-secret" + "x" * 3000
    response = client.post("/precedent-finder", json={"proposition": rejected})
    assert response.status_code == 413
    assert "private-secret" not in response.text + caplog.text
    assert calls == [3000, 3000]
    with pytest.raises(ValueError, match="at most 3000"):
        service.find_precedents(rejected, object())


def test_success_failure_and_media_type_privacy(client, monkeypatch, caplog):
    from backend import routes
    response = client.post("/precedent-finder", json={"proposition": "private-secret"})
    assert response.status_code == 200
    assert "private-secret" not in response.text + caplog.text
    assert response.headers["pragma"] == "no-cache"
    def fail(proposition, db):
        raise ValueError(proposition)
    monkeypatch.setattr(routes, "find_precedents", fail)
    response = client.post("/precedent-finder", json={"proposition": "private-secret"})
    assert response.status_code == 500
    assert "private-secret" not in response.text + caplog.text
    response = client.post("/precedent-finder", content="private-secret")
    assert response.status_code == 422
    assert "private-secret" not in response.text + caplog.text


def test_page_contract_preserves_existing_research_links(client):
    response = client.get("/precedent-finder")
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    html = response.text
    for expected in ('maxlength="3000"', 'method:\'POST\'', "JSON.stringify({proposition:input.value})",
                     "textContent=value", 'href="/data-explorer"', "rank", "unclassified",
                     "denominator", "recency", "pagehide", "No embeddings",
                     "Citing source paragraph:", "row.excerpt_source", "source.basis",
                     "/data-explorer?tab=search&case_id=",
                     "encodeURIComponent(source.source_case_id)+'&paragraph='",
                     "encodeURIComponent(source.paragraph_number)"):
        assert expected in html
    assert "localStorage" not in html and "sessionStorage" not in html
    assert "innerHTML" not in html and "console." not in html
    assert "alert(" not in html


def test_real_endpoint_fixture_and_audit_never_record_proposition(db, fixed_tagger, caplog):
    from backend import routes
    from backend.audit import RequestAuditMiddleware
    case(db, 1)
    case(db, 100)
    tag(db, 1)
    cite(db, 1, 100)
    app = FastAPI()
    app.include_router(routes.router)
    app.dependency_overrides[get_db] = lambda: db
    records = []
    audit = RequestAuditMiddleware.__new__(RequestAuditMiddleware)
    audit.app = app
    audit.address_key = b"fixture-only"
    audit.raw_address = False
    audit.handler = SimpleNamespace(handle=lambda record: records.append(record.getMessage()))
    client = TestClient(audit)
    proposition = "private-secret fairness"
    response = client.post("/precedent-finder", json={"proposition": proposition})
    assert response.status_code == 200
    row = response.json()["authorities"][0]
    assert row["case_id"] == 100
    assert row["rank_numbers"] == [1, 1, 20200101]
    assert row["outcome_mix"]["denominator"] == 1
    response = client.post("/precedent-finder", json={"proposition": [proposition]})
    assert response.status_code == 422
    assert len(records) == 2
    assert all('"path": "/precedent-finder"' in record for record in records)
    assert "private-secret" not in response.text + caplog.text + "".join(records)
    assert not db.new and not db.dirty and not db.deleted


def test_deep_invalid_json_and_openapi_contract(client):
    response = client.post("/precedent-finder", content="[" * 2000 + "private-secret",
                           headers={"Content-Type": "application/json"})
    assert response.status_code == 422
    assert "private-secret" not in response.text
    operation = client.app.openapi()["paths"]["/precedent-finder"]["post"]
    schema = operation["requestBody"]["content"]["application/json"]["schema"]
    assert schema["properties"]["proposition"]["maxLength"] == 3000
    assert schema["required"] == ["proposition"]
    assert schema["additionalProperties"] is False
    assert {"200", "413", "422", "500"} <= set(operation["responses"])
