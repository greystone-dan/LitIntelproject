from datetime import date
import importlib.util
from pathlib import Path
import re
import os
import shutil
import signal
import subprocess
import tempfile

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from backend.database import Case, CaseChunk, CaseTag, Citation, get_db
from backend.legal_tagger_v3 import ACTIVE_TAG_TAXONOMY_VERSION
from backend import paragraph_similarity as service


@pytest.fixture
def db():
    engine = create_engine("sqlite://")

    @event.listens_for(engine, "connect")
    def functions(connection, _):
        connection.create_function("strpos", 2, lambda text, needle: (text.find(needle) + 1)
                                   if text is not None and needle is not None else None)

    for model in (Case, CaseChunk, CaseTag, Citation):
        model.__table__.create(engine)
    with Session(engine) as session:
        yield session


def case(db, owner, text, number=7, chunk_index=999):
    db.add(Case(id=owner, title=f"Case {owner}", court="FC", date=date(2025, 1, 1),
                citation=f"2025 FC {owner}", full_text=text))
    db.add(CaseChunk(id=owner, case_id=owner, chunk_set="paragraph", chunk_index=chunk_index,
                     paragraph_start=number, paragraph_end=number, text=text,
                     text_hash=str(owner), token_estimate=10))
    db.flush()


def tag(db, owner, text, *, start=None, evidence=None, taxonomy=ACTIVE_TAG_TAXONOMY_VERSION):
    full_text = db.scalar(service.select(Case.full_text).where(Case.id == owner))
    start = full_text.index(text) if start is None else start
    db.add(CaseTag(case_id=owner, chunk_id=None, category="issue", value=text,
                   score=1, evidence=text if evidence is None else evidence,
                   offset_start=start, offset_end=start + len(text),
                   source="core_whitelist", taxonomy_version=taxonomy))
    db.flush()


def cite(db, owner, label="2020 FC 8", *, target=88, chunk=True, kind="neutral", **kwargs):
    text = db.scalar(service.select(Case.full_text).where(Case.id == owner))
    start = text.index(label)
    db.add(Citation(source_case_id=owner, chunk_id=owner if chunk else None,
                    citation_kind=kind, citation_text=label, normalized_citation=label,
                    offset_start=start, offset_end=start + len(label),
                    target_case_id=target, target_paragraph=400, **kwargs))
    db.flush()


def test_exact_tags_without_chunk_and_deterministic_score_ties(db):
    for owner in (1, 3, 2):
        case(db, owner, "[7] 😀 fairness and 2020 FC 8.")
        tag(db, owner, "fairness")
        cite(db, owner)
    # A second stored occurrence must not increase the score.
    tag(db, 2, "fairness", taxonomy="old")
    result = service.similar_paragraphs(1, 7, 10, db)
    assert [(row.case_id, row.paragraph_number, row.score) for row in result.results] == [(2, 7, 3), (3, 7, 3)]
    assert result.results[0].shared_tags == ["issue:fairness"]
    assert result.results[0].shared_authorities == ["case:88"]
    assert "3 points" in result.results[0].why_matched
    assert not result.coverage.partial


def test_canonical_prefix_and_local_citation_offsets(db):
    for owner in (1, 2):
        case(db, owner, "[7] fairness and 2020 FC 8.")
        tag(db, owner, "fairness", start=len("Header\n[7] "))
        cite(db, owner)
        db.get(Case, owner).full_text = "Header\n" + db.get(Case, owner).full_text
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results[0].score == 3


def test_citation_only_and_no_evidence(db):
    for owner in (1, 2):
        case(db, owner, "[7] See 2020 FC 8.")
        cite(db, owner, chunk=False)
    assert service.similar_paragraphs(1, 7, 10, db).results[0].score == 2
    db.query(Citation).delete()
    assert service.similar_paragraphs(1, 7, 10, db).results == []


@pytest.mark.parametrize("fault", ["offset", "evidence", "taxonomy", "paragraph", "canonical", "repeat", "chunk-index"])
def test_unverified_rows_never_guess(db, fault):
    for owner in (1, 2):
        case(db, owner, "[7] fairness.")
        tag(db, owner, "fairness")
    candidate = db.get(CaseChunk, 2)
    candidate_tag = db.query(CaseTag).filter_by(case_id=2).one()
    if fault == "offset":
        candidate_tag.offset_end = 9999
    elif fault == "evidence":
        candidate_tag.evidence = "something else"
    elif fault == "taxonomy":
        candidate_tag.taxonomy_version = "old"
    elif fault == "paragraph":
        candidate.paragraph_start = candidate.paragraph_end = 99
    elif fault == "canonical":
        db.get(Case, 2).full_text = "[7] different."
    elif fault == "repeat":
        db.get(Case, 2).full_text += "\n[7] fairness."
    else:
        candidate.paragraph_start = candidate.paragraph_end = None
        candidate.chunk_index = 7
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results == []


def test_unresolved_formal_authority_and_short_form_anchor(db):
    for owner in (1, 2):
        case(db, owner, "[7] 2020 FC 8 is called Smith. Smith applies.")
        cite(db, owner, target=None)
    assert service.similar_paragraphs(1, 7, 10, db).results[0].shared_authorities == ["citation:2020 FC 8"]
    db.query(Citation).delete()
    for owner in (1, 2):
        text = db.get(Case, owner).full_text
        start = text.rindex("Smith")
        db.add(Citation(source_case_id=owner, chunk_id=owner, citation_kind="case_short",
                        citation_text="Smith", normalized_citation="Smith", target_case_id=88,
                        offset_start=start, offset_end=start + 5,
                        anchor_citation_text="2020 FC 8", anchor_offset_start=4, anchor_offset_end=13))
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results[0].score == 2
    db.query(Citation).filter_by(source_case_id=2).one().anchor_offset_start = 0
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results == []


def test_statutes_and_cited_pinpoints_not_source_paragraphs(db):
    for owner in (1, 2):
        case(db, owner, "[7] IRPA and 2020 FC 8.")
        cite(db, owner, kind="statute")
    assert service.similar_paragraphs(1, 7, 10, db).results == []
    with pytest.raises(Exception) as error:
        service.similar_paragraphs(1, 400, 10, db)
    assert error.value.status_code == 404
    with pytest.raises(Exception) as missing:
        service.similar_paragraphs(999, 7, 10, db)
    assert missing.value.status_code == 404


def earlier_chunk_anchor(db, owner, target):
    """Explicit rows in rebuild_citations_for_case's canonical stored format."""
    paragraph = "[7] Smith applies."
    anchor = "Smith v Jones, 2020 FC 8"
    prefix = f"Decision header\n[6] See {anchor} (Smith).\n"
    case(db, owner, paragraph)
    db.get(Case, owner).full_text = prefix + paragraph
    db.add(CaseChunk(id=owner + 100, case_id=owner, chunk_set="paragraph",
                     chunk_index=998, paragraph_start=6, paragraph_end=6,
                     text=prefix.split("\n")[1], text_hash=f"earlier-{owner}",
                     token_estimate=10))
    # Only the occurrence subtracts the containing chunk's document base.
    # The earlier full citation's anchor span is not rebased.
    start = paragraph.index("Smith")
    anchor_start = prefix.index(anchor)
    row = Citation(source_case_id=owner, chunk_id=owner, citation_kind="case_short",
                   citation_text="Smith", normalized_citation="Smith",
                   offset_start=start, offset_end=start + len("Smith"),
                   anchor_citation_text=anchor, anchor_offset_start=anchor_start,
                   anchor_offset_end=anchor_start + len(anchor),
                   target_case_id=target, unresolved=target is None)
    db.add(row)
    db.flush()
    assert row.anchor_offset_end > row.offset_start
    return row


@pytest.mark.parametrize("target,identity", [(88, "case:88"), (None, "citation:2020 FC 8")])
def test_document_relative_anchor_in_earlier_paragraph_chunk(db, target, identity):
    for owner in (1, 2):
        earlier_chunk_anchor(db, owner, target)
    result = service.similar_paragraphs(1, 7, 10, db)
    assert [(row.case_id, row.paragraph_number, row.score) for row in result.results] == [(2, 7, 2)]
    assert result.results[0].shared_authorities == [identity]
    assert not result.coverage.partial


@pytest.mark.parametrize("owner", [1, 2])
@pytest.mark.parametrize("fault", [
    "negative", "empty", "reversed", "outside", "after-occurrence", "chunk-relative", "text",
])
def test_corrupt_document_relative_short_anchor_rejected(db, owner, fault):
    rows = {number: earlier_chunk_anchor(db, number, 88) for number in (1, 2)}
    row = rows[owner]
    full_text = db.get(Case, owner).full_text
    if fault == "negative":
        row.anchor_offset_start = -1
    elif fault == "empty":
        row.anchor_offset_end = row.anchor_offset_start
    elif fault == "reversed":
        row.anchor_offset_end = row.anchor_offset_start - 1
    elif fault == "outside":
        row.anchor_offset_end = len(full_text) + 1
    elif fault == "after-occurrence":
        row.anchor_offset_start = full_text.rindex("Smith")
        row.anchor_offset_end = row.anchor_offset_start + 5
        row.anchor_citation_text = "Smith"
    elif fault == "chunk-relative":
        row.anchor_offset_start -= len("Decision header\n")
        row.anchor_offset_end -= len("Decision header\n")
    else:
        row.anchor_citation_text = "2020 FC 9"
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results == []


def test_budgets_and_all_queries_have_sql_limits(db, monkeypatch):
    for owner in range(1, 8):
        case(db, owner, "[7] fairness.")
        tag(db, owner, "fairness")
    monkeypatch.setattr(service, "POSTINGS", 3)
    monkeypatch.setattr(service, "CANDIDATE_CASES", 2)
    statements = []

    @event.listens_for(db.bind, "before_cursor_execute")
    def capture(_, __, statement, ___, ____, _____):
        statements.append(statement)

    result = service.similar_paragraphs(1, 7, 10, db)
    assert [row.case_id for row in result.results] == [2, 3]
    assert result.coverage.partial
    assert result.coverage.candidate_cases_checked == 2
    assert all("LIMIT" in statement for statement in statements if statement.startswith("SELECT"))
    assert not any(re.search(r"(?:SELECT |, )cases\.full_text(?: AS |,\s|\sFROM)", statement)
                   for statement in statements)


def test_paragraph_ties_and_duplicate_numbers(db):
    case(db, 1, "[7] fairness.")
    tag(db, 1, "fairness")
    case(db, 2, "[7] fairness.")
    tag(db, 2, "fairness")
    db.get(Case, 2).full_text += "\n[8] fairness."
    db.add(CaseChunk(id=22, case_id=2, chunk_set="paragraph", chunk_index=0,
                     paragraph_start=8, paragraph_end=8, text="[8] fairness.",
                     text_hash="22", token_estimate=10))
    tag(db, 2, "fairness", start=len("[7] fairness.\n[8] "))
    rows = service.similar_paragraphs(1, 7, 10, db).results
    assert [(row.case_id, row.paragraph_number) for row in rows] == [(2, 7), (2, 8)]
    db.get(CaseChunk, 22).paragraph_start = db.get(CaseChunk, 22).paragraph_end = 7
    db.flush()
    assert service.similar_paragraphs(1, 7, 10, db).results == []


def test_source_and_paragraph_budgets(db, monkeypatch):
    case(db, 1, "[7] fairness.")
    case(db, 2, "[7] fairness.")
    tag(db, 1, "fairness")
    tag(db, 2, "fairness")
    monkeypatch.setattr(service, "SOURCE_ROWS", 0)
    assert service.similar_paragraphs(1, 7, 10, db).coverage.partial
    monkeypatch.setattr(service, "SOURCE_ROWS", 256)
    monkeypatch.setattr(service, "PARAGRAPHS_TOTAL", 0)
    result = service.similar_paragraphs(1, 7, 10, db)
    assert result.results == [] and result.coverage.partial
    monkeypatch.setattr(service, "PARAGRAPHS_TOTAL", 1)
    result = service.similar_paragraphs(1, 7, 10, db)
    assert [row.case_id for row in result.results] == [2]
    assert result.coverage.partial


def test_source_signal_cap_disclosed(db, monkeypatch):
    for owner in (1, 2):
        case(db, owner, "[7] fairness and 2020 FC 8.")
        tag(db, owner, "fairness")
        cite(db, owner)
    monkeypatch.setattr(service, "SIGNALS", 1)
    result = service.similar_paragraphs(1, 7, 10, db)
    assert result.results[0].score == 1
    assert result.coverage.partial


def bare_scc_case(db, owner):
    paragraph = "3 😀 fairness and 2020 SCC 8 apply."
    prefix = "Supreme Court of Canada\nDecision Content\n1 Background.\n2 Prior reasons.\n"
    case(db, owner, paragraph, number=3)
    db.get(Case, owner).court = "SCC"
    cite(db, owner, "2020 SCC 8")
    db.get(Case, owner).full_text = prefix + paragraph
    db.flush()
    tag(db, owner, "fairness")
    return prefix, paragraph


def test_bounded_bare_scc_actual_context_and_offsets(db, monkeypatch):
    contexts = {owner: bare_scc_case(db, owner) for owner in (1, 2)}
    formatted = []
    formatter = service.format_decision

    def capture(text):
        formatted.append(text)
        return formatter(text)

    monkeypatch.setattr(service, "format_decision", capture)
    # A large suffix must not be fetched/formatted as candidate context.
    db.get(Case, 2).full_text += "\nUnrelated suffix " + "x" * service.TEXT_CHARS
    db.flush()
    paragraphs, capped, consumed = service._located_chunks(db, 2)
    assert not capped and consumed == 1
    paragraph = paragraphs[0]
    prefix, text = contexts[2]
    assert paragraph.pos - 1 == len(prefix)
    assert paragraph.text == text and paragraph.prefix == prefix
    stored_tag = db.query(CaseTag).filter_by(case_id=2).one()
    stored_cite = db.query(Citation).filter_by(source_case_id=2).one()
    assert stored_tag.offset_start == len(prefix) + text.index("fairness")
    assert stored_cite.offset_start == text.index("2020 SCC 8")
    verified_cite = db.execute(service._citation_query().where(Citation.id == stored_cite.id)).one()
    assert verified_cite.start == len(prefix) + stored_cite.offset_start
    assert verified_cite.exact == "2020 SCC 8"
    result = service.similar_paragraphs(1, 3, 10, db)
    assert [(row.case_id, row.paragraph_number, row.score) for row in result.results] == [(2, 3, 3)]
    assert not result.coverage.partial
    assert formatted and all(text == prefix + contexts[2][1] for text in formatted)
    assert all(len(text) <= service.TEXT_CHARS for text in formatted)
    # Canonical tags must not be silently interpreted as chunk-relative offsets.
    stored_tag.offset_start -= len(prefix)
    stored_tag.offset_end -= len(prefix)
    db.flush()
    assert service.similar_paragraphs(1, 3, 10, db).results[0].score == 2


@pytest.mark.parametrize("owner", [1, 2])
@pytest.mark.parametrize("fault", [
    "missing-marker", "broken-sequence", "broken-before-valid", "oversized-context",
    "repeat", "duplicate", "ambiguous-marker",
])
def test_bounded_bare_scc_rejects_unverified_context(db, owner, fault):
    contexts = {number: bare_scc_case(db, number) for number in (1, 2)}
    prefix, paragraph = contexts[owner]
    decision = db.get(Case, owner)
    if fault == "missing-marker":
        decision.full_text = prefix.replace("Decision Content", "Reasons") + paragraph
    elif fault == "broken-sequence":
        decision.full_text = prefix.replace("2 Prior reasons.", "4 Prior reasons.") + paragraph
    elif fault == "broken-before-valid":
        decision.full_text = prefix.replace("2 Prior reasons.", "4 Skipped number.\n2 Prior reasons.") + paragraph
    elif fault == "ambiguous-marker":
        decision.full_text = "Decision Content\n" + prefix + paragraph
    elif fault == "oversized-context":
        decision.full_text = "x" * service.TEXT_CHARS + "\n" + prefix + paragraph
    elif fault == "repeat":
        decision.full_text += "\n" + paragraph
    else:
        db.add(CaseChunk(id=100 + owner, case_id=owner, chunk_set="paragraph",
                         chunk_index=0, paragraph_start=3, paragraph_end=3,
                         text=paragraph, text_hash=f"duplicate-{owner}", token_estimate=10))
    db.flush()
    assert service._located_chunks(db, owner, paragraph=3)[0] == []
    if owner == 1:
        with pytest.raises(Exception) as error:
            service.similar_paragraphs(1, 3, 10, db)
        assert error.value.status_code == 404
    else:
        assert service.similar_paragraphs(1, 3, 10, db).results == []


def test_bounded_bare_scc_context_cap_boundary(db, monkeypatch):
    prefix, paragraph = bare_scc_case(db, 1)
    monkeypatch.setattr(service, "TEXT_CHARS", len(prefix + paragraph))
    assert len(service._located_chunks(db, 1)[0]) == 1
    monkeypatch.setattr(service, "TEXT_CHARS", len(prefix + paragraph) - 1)
    assert service._located_chunks(db, 1)[0] == []


@pytest.mark.parametrize("budget,expected,partial,limits", [
    (0, [], True, [1]),
    (1, [4], True, [2]),
    (3, [2, 3, 4], True, [4, 3]),
    (6, [2, 3, 4, 5, 6], False, [7, 6]),
])
def test_bounded_unresolved_labels_equality_and_shared_postings_budget(
        db, monkeypatch, budget, expected, partial, limits):
    labels = ["2020 FC 8", "2020 FCT 8"]
    case(db, 1, "[7] " + " and ".join(labels) + ".")
    for label in reversed(labels):
        cite(db, 1, label, target=None)
    for owner, label in [(6, labels[1]), (4, labels[0]), (3, labels[1]),
                         (5, labels[1]), (2, labels[1])]:
        case(db, owner, f"[7] See {label}.")
        cite(db, owner, label, target=None)
    monkeypatch.setattr(service, "POSTINGS", budget)
    statements = []

    @event.listens_for(db.bind, "before_cursor_execute")
    def capture(_, __, statement, parameters, ___, ____):
        statements.append((statement, parameters))

    for _ in range(2):
        statements.clear()
        result = service.similar_paragraphs(1, 7, 10, db)
        assert [row.case_id for row in result.results] == expected
        assert all(row.score == 2 for row in result.results)
        assert result.coverage.partial is partial
        seeks = [(sql, params) for sql, params in statements
                 if sql.startswith("SELECT citations.id, citations.source_case_id AS owner")]
        assert len(seeks) == len(limits)
        assert [params[-2] for _, params in seeks] == limits
        assert [params[0] for _, params in seeks] == labels[:len(limits)]
        assert all("citations.normalized_citation = ?" in sql for sql, _ in seeks)
        assert all("ORDER BY citations.source_case_id, citations.id" in sql for sql, _ in seeks)
        assert all("LIMIT" in sql for sql, _ in seeks)
        assert not any("citations.normalized_citation IN" in sql for sql, _ in statements)
        # Known eligible row counts prove all label seeks share one lookahead.
        fetched = sum(min(count, cap) for count, cap in zip([1, 4], limits))
        assert fetched <= budget + 1
        assert not any(re.search(r"(?:SELECT |, )cases\.full_text(?: AS |,\s|\sFROM)", sql)
                       for sql, _ in statements)


def test_api_validation_and_payload(monkeypatch):
    from backend.routes import router
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[get_db] = lambda: object()
    monkeypatch.setattr("backend.routes.similar_paragraphs", lambda *args: {
        "results": [], "coverage": {"partial": False, "candidate_cases_checked": 0,
        "source_row_budget": 256, "signal_budget": 24, "postings_per_signal": 128,
        "candidate_case_budget": 32, "paragraph_row_budget": 512, "note": "Bounded"}
    })
    with TestClient(app) as client:
        assert client.get("/cases/1/paragraphs/7/similar").json()["coverage"]["note"] == "Bounded"
        for path in ("/cases/0/paragraphs/7/similar", "/cases/1/paragraphs/0/similar",
                     "/cases/1/paragraphs/7/similar?limit=0", "/cases/1/paragraphs/7/similar?limit=51",
                     "/cases/1/paragraphs/no/similar"):
            assert client.get(path).status_code == 422


def test_index_migration_mirrors_orm_and_reverses(monkeypatch):
    path = Path("alembic/versions/0031_paragraph_similarity_postings.py")
    spec = importlib.util.spec_from_file_location("similarity_migration", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    created, dropped = [], []
    monkeypatch.setattr(module.op, "create_index", lambda name, table, cols: created.append((name, table, cols)))
    monkeypatch.setattr(module.op, "drop_index", lambda name, table_name: dropped.append(name))
    module.upgrade()
    module.downgrade()
    assert dropped == [name for name, _, _ in reversed(created)]
    for name, table, columns in created:
        index = next(index for index in Case.metadata.tables[table].indexes if index.name == name)
        assert [column.name for column in index.columns] == columns


def test_active_reader_feature_and_mock_browser():
    from backend.degraded_mode import panel_helpers_script
    from backend.pages.data_explorer import data_explorer_page_html
    html = data_explorer_page_html()
    panel_queue = "const panelRequests=" + html.split("const panelRequests=", 1)[1].split(
        "function readerPanelCurrent", 1
    )[0]
    feature = html.split("let paragraphSimilarityRequest=0;", 1)[1].split("const initialCaseId=", 1)[0]
    assert "/paragraphs/${n}/similar?limit=10" in feature
    assert "panel.isConnected" in feature
    assert "&paragraph=${Number(row.paragraph_number)}" in feature
    browser = shutil.which("chromium")
    if not browser:
        pytest.skip("Chromium not installed; static feature assertions passed")
    document = """<html><body><div id="decisionBody"><p class="fmt-para" data-para="7">Text</p></div>
""" + panel_helpers_script() + "<script>" + panel_queue + """
let readerState={caseId:1};let openDecision=async id=>{readerState.caseId=id;};
const esc=s=>String(s);let pending=[];
window.fetch=()=>new Promise(resolve=>pending.push(resolve));
const tick=()=>new Promise(resolve=>setTimeout(resolve,0));
let paragraphSimilarityRequest=0;
""" + feature + """
(async ()=>{
const para=document.querySelector('.fmt-para');
const first=showSimilarParagraphs(para);await tick();
const second=showSimilarParagraphs(para);await tick();
const loading=document.getElementById('paragraphSimilarity').textContent.includes('Loading');
pending[1]({ok:true,json:async()=>({results:[{case_id:2,paragraph_number:9,title:'Target',excerpt:'Match',why_matched:'1 shared tag',shared_tags:['issue:fairness'],shared_authorities:[]}],coverage:{note:'Bounded'}})});
await second;
pending[0]({ok:true,json:async()=>({results:[],coverage:{note:'STALE'}})});
await first;
const panel=document.getElementById('paragraphSimilarity');
const linked=panel.textContent.includes('Bounded')&&!panel.textContent.includes('STALE')&&panel.querySelector('a').getAttribute('href').endsWith('case_id=2&paragraph=9');
const empty=showSimilarParagraphs(para);await tick();pending[2]({ok:true,json:async()=>({results:[],coverage:{note:'Bounded'}})});await empty;
const emptyShown=document.getElementById('paragraphSimilarity').textContent.includes('No matches found');
const failed=showSimilarParagraphs(para);await tick();pending[3]({ok:false,status:500});await failed;
const errorShown=document.getElementById('paragraphSimilarity').textContent.includes('This section could not load.');
document.querySelector('#paragraphSimilarity button').click();await tick();
pending[4]({ok:true,json:async()=>({results:[],coverage:{note:'Recovered'}})});await tick();
const recovered=document.getElementById('paragraphSimilarity').textContent.includes('Recovered');
history.replaceState(null,'','?case_id=2&paragraph=9');
const target=document.createElement('p');target.className='fmt-para';target.dataset.para='9';document.getElementById('decisionBody').append(target);
await openDecision(2);
const opened=target.classList.contains('is-cited');
if(loading&&linked&&emptyShown&&errorShown&&recovered&&opened){
document.body.dataset.browserCheck='passed';
}
})();
</script></body></html>"""
    # ignore_cleanup_errors: Chromium helper processes can still be flushing the
    # profile directory for a moment after the main process exits.
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
        path = Path(directory) / "mock-reader.html"
        path.write_text(document)
        # Same isolation flags as the other headless-Chromium tests: private profile
        # (no shared default profile between parallel workers), no /dev/shm use, no
        # session D-Bus lookup (the stall seen in CI stderr).
        # Own process group: Chromium leaves helper processes that inherit the output
        # pipes, so a plain subprocess.run() can wait on them until its timeout even
        # though the page finished. Kill the whole group once the browser is done.
        process = subprocess.Popen(
            [browser, "--headless", "--no-sandbox", "--disable-gpu",
             "--disable-dev-shm-usage", "--disable-background-networking",
             "--disable-extensions", "--no-first-run", "--no-default-browser-check",
             f"--user-data-dir={Path(directory) / 'profile'}",
             "--dump-dom", "--virtual-time-budget=1000", path.as_uri()],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            env={**os.environ, "DBUS_SESSION_BUS_ADDRESS": "disabled:"},
            start_new_session=True,
        )
        try:
            stdout, stderr = process.communicate(timeout=30)
        finally:
            try:
                if hasattr(os, "killpg"):
                    os.killpg(process.pid, signal.SIGKILL)
                else:
                    process.kill()
            except ProcessLookupError:
                pass
            process.wait()
    result = subprocess.CompletedProcess(process.args, process.returncode, stdout, stderr)
    assert result.returncode == 0, result.stderr
    assert 'data-browser-check="passed"' in result.stdout, result.stdout
