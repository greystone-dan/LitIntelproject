"""Cold-session, offline citation endpoint budgets and complete legacy parity.

Fixtures scale citing decisions and outgoing authorities independently (5/50
edges in each direction), not just repeated occurrences of one authority.
No application startup, application engine, cache, or PostgreSQL emulation.
"""

from collections import Counter
from datetime import date
from functools import lru_cache
from math import log1p

import pytest
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, distinct, func, or_, select
from sqlalchemy.orm import Session, aliased
from sqlalchemy.pool import StaticPool

from backend import citation_map as cm, routes
from backend.database import (
    Base, Case, CaseChunk, CaseTag, Citation, CitationMetrics, StatuteReference,
    get_db,
)
from performance_helpers import count_statements


@pytest.fixture(params=[5, 50], ids=["5", "50"])
def graph(request, monkeypatch):
    monkeypatch.setenv("CASELIBRARY_FOCUS_MASTER_300", "false")
    cm._focused_case_ids.cache_clear()
    engine = create_engine(
        "sqlite:///:memory:", poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine, tables=[
        Case.__table__, CaseChunk.__table__, CaseTag.__table__,
        Citation.__table__, CitationMetrics.__table__, StatuteReference.__table__,
    ])
    n = request.param
    with Session(engine) as db:
        for case_id in [1, 2] + list(range(10, 10 + n)) + list(range(100, 100 + n)):
            db.add(Case(
                id=case_id, title=f"Fixture decision {case_id}",
                citation=f"2020 FC {case_id}", court="FC" if case_id % 3 else "FCA",
                date=date(2020 + case_id % 3, 1, 1),
                full_text="UNUSED FULL TEXT " * 100, source_html="UNUSED HTML " * 100,
                metadata_json={"reader_extracted": {
                    "judge": "Judge A" if case_id % 3 else "",
                    "government outcome": ["won", "lost", "mixed", None][case_id % 4],
                }},
            ))
            # Missing and null metrics must remain distinct from actual zero.
            if case_id % 3:
                db.add(CitationMetrics(
                    case_id=case_id, in_degree=case_id % 4,
                    out_degree=None, pagerank=0.0 if case_id % 2 else 0.125,
                ))
        db.flush()
        citation_id = 1
        for i in range(n):
            source, target = 10 + i, 100 + i
            for owner in [source, 2]:
                chunk_id = owner * 1000 + i
                db.add(CaseChunk(
                    id=chunk_id, case_id=owner, chunk_index=i,
                    text=f"standard of review\n2020 FC {target}\ncontext {i}",
                    text_hash=f"hash-{chunk_id}", token_estimate=20,
                ))
            db.flush()
            for owner, authority, chunk_id in [
                (source, 1, source * 1000 + i), (2, target, 2000 + i),
            ]:
                # Duplicate identical contexts exercise pre-dedup limits and ties.
                for repetition in range(1 + i % 3):
                    db.add(Citation(
                        id=citation_id, source_case_id=owner, target_case_id=authority,
                        chunk_id=chunk_id if i % 4 else None,
                        citation_text=f"2020 FC {authority}",
                        normalized_citation=f"2020 FC {authority}",
                        offset_start=19 if repetition != 2 else None,
                        offset_end=30 if repetition != 2 else None,
                    ))
                    citation_id += 1
            db.add(StatuteReference(
                source_case_id=source, reference_kind="statute",
                normalized_reference="IRPA s. 34" if i % 2 else None,
            ))
            db.add(CaseTag(
                case_id=2, category="issue", value=f"issue-{i}",
                score=0.5, evidence=f"evidence-{i}", source="fixture",
                taxonomy_version=cm.ACTIVE_TAG_TAXONOMY_VERSION,
            ))
            if i % 3 == 0:
                db.add(CaseTag(
                    case_id=2, category="issue", value=f"issue-{i}",
                    score=0.3, evidence=f"second mention-{i}", source="fixture",
                    offset_start=50, offset_end=60,
                    taxonomy_version=cm.ACTIVE_TAG_TAXONOMY_VERSION,
                ))
            if i % 2:
                db.add(CaseTag(
                    case_id=source, category="issue", value=f"issue-{i}",
                    score=0.4, evidence="common", source="fixture",
                    taxonomy_version=cm.ACTIVE_TAG_TAXONOMY_VERSION,
                ))
            db.add(CaseTag(
                case_id=source, category="issue", value="old",
                score=0.1, evidence="old taxonomy", source="fixture",
                taxonomy_version="old",
            ))
        db.commit()
    app = FastAPI()
    app.include_router(routes.router)

    def isolated_db():
        with Session(engine) as db:
            yield db

    app.dependency_overrides[get_db] = isolated_db
    with TestClient(app) as client:
        yield engine, client, n
    engine.dispose()
    cm._focused_case_ids.cache_clear()


# Exact statement counts, including route-level existence checks. Deliberately
# request enough rows to exercise all 50 authorities rather than the default 20.
ENDPOINTS = [
    ("/api/citation-intelligence/search?q=Fixture&limit=50", 1),
    ("/api/citation-intelligence/cases?title=Fixture&limit=50", 1),
    ("/api/citation-intelligence/1/overview", 9),
    ("/api/citation-intelligence/1/timeline", 2),
    ("/api/citation-intelligence/1/outcomes", 2),
    ("/api/citation-intelligence/1/courts", 2),
    ("/api/citation-intelligence/1/judges", 2),
    ("/api/citation-intelligence/1/statutes", 2),
    ("/api/citation-intelligence/1/companions", 2),
    ("/api/citation-intelligence/1/table?page_size=200", 3),
    ("/citation-map/summary", 6),
    ("/citation-map/cases?q=Fixture&limit=30", 1),
    ("/citation-map/cases/1/neighborhood?limit=500", 3),
    ("/citation-map/cases/2/authority-signals?limit=80&context_limit=3", 4),
    ("/citation-map/surprises?limit=250", 2),
    ("/citation-map/cases/2/tags?limit=250&display_limit=3", 4),
]


@pytest.mark.parametrize("path,ceiling", ENDPOINTS, ids=[x[0] for x in ENDPOINTS])
def test_cold_endpoint_statement_budget(graph, path, ceiling):
    engine, client, n = graph
    with count_statements(engine) as counter:
        response = client.get(path)
    assert response.status_code == 200, (path, n, response.text)
    assert counter.count == ceiling, (path, n, counter.count, ceiling)


def legacy_surprises(db, **kwargs):
    """Pre-optimization query/ranking oracle, including candidate cap and ties."""
    limit = kwargs.get("limit", 50)
    edges = cm._aggregated_edges()
    src, tgt = aliased(Case), aliased(Case)
    frequency = select(
        edges.c.target_case_id,
        func.count(edges.c.source_case_id).label("global_citing_cases"),
    ).group_by(edges.c.target_case_id).cte()
    totals = select(
        edges.c.source_case_id,
        func.sum(edges.c.occurrence_count).label("source_occurrences"),
    ).group_by(edges.c.source_case_id).cte()
    statement = select(
        src, tgt, edges.c.occurrence_count, frequency.c.global_citing_cases,
        func.coalesce(totals.c.source_occurrences, edges.c.occurrence_count),
    ).join(src, src.id == edges.c.source_case_id).join(
        tgt, tgt.id == edges.c.target_case_id,
    ).join(frequency, frequency.c.target_case_id == edges.c.target_case_id).outerjoin(
        totals, totals.c.source_case_id == edges.c.source_case_id,
    ).where(edges.c.occurrence_count >= kwargs.get("min_occurrences", 1))
    if kwargs.get("category") and kwargs.get("value"):
        statement = statement.join(
            CaseTag, (CaseTag.case_id == src.id)
            & (CaseTag.category == kwargs["category"])
            & (CaseTag.value == kwargs["value"])
            & (CaseTag.taxonomy_version == cm.ACTIVE_TAG_TAXONOMY_VERSION),
        )
    for key, operator in [("start_year", "__ge__"), ("end_year", "__le__")]:
        if kwargs.get(key) is not None:
            statement = statement.where(
                getattr(func.extract("year", src.date), operator)(kwargs[key])
            )
    rows = list(db.execute(statement.order_by(
        edges.c.occurrence_count.desc(), frequency.c.global_citing_cases, src.id,
    ).limit(max(limit * 5, 200))))
    result = []
    for source, authority, count, global_count, source_total in rows:
        count, global_count = int(count or 0), int(global_count or 0)
        result.append({
            "source_case": cm._case_node(source, db.get(CitationMetrics, source.id)),
            "authority": cm._case_node(authority, db.get(CitationMetrics, authority.id)),
            "occurrence_count": count, "global_citing_cases": global_count,
            "gravity_share": count / max(1, int(source_total or 0)),
            "surprise_score": float(log1p(count) / (1 + log1p(max(1, global_count)))),
        })
    result.sort(key=lambda item: (item["surprise_score"], item["occurrence_count"]), reverse=True)
    return result[:limit]


def legacy_tags(db, case_id=2, limit=250, display_limit=3):
    """Original rarity algorithm; repair only its missing distinct import."""
    tags = list(db.scalars(select(CaseTag).where(
        CaseTag.case_id == case_id,
        CaseTag.taxonomy_version == cm.ACTIVE_TAG_TAXONOMY_VERSION,
    ).order_by(CaseTag.score.desc(), CaseTag.category, CaseTag.value).limit(
        max(limit, display_limit or limit),
    )))
    total = db.scalar(select(func.count(distinct(CaseTag.case_id)))) or 1
    mentions = Counter((tag.category, tag.value) for tag in tags)

    @lru_cache(maxsize=10000)
    def fire_rate(category, value):
        count = db.scalar(select(func.count(distinct(CaseTag.case_id))).where(
            CaseTag.category == category, CaseTag.value == value,
            CaseTag.taxonomy_version == cm.ACTIVE_TAG_TAXONOMY_VERSION,
        )) or 0
        return count / max(total, 1)

    scored = []
    for tag in tags:
        rarity = 1.0 / (fire_rate(tag.category, tag.value) + 0.01)
        scored.append((tag, rarity * mentions[(tag.category, tag.value)]))
    seen, ranked = set(), []
    for tag, _ in sorted(scored, key=lambda item: -item[1]):
        key = tag.category, tag.value
        if key not in seen:
            seen.add(key)
            ranked.append(tag)
    return [{
        "category": tag.category, "value": tag.value, "score": tag.score,
        "evidence": tag.evidence, "source": tag.source,
        "taxonomy_version": tag.taxonomy_version, "display": i < (display_limit or limit),
    } for i, tag in enumerate(ranked[:limit])]


@pytest.mark.parametrize("kwargs", [
    {"limit": 250}, {"limit": 3}, {"limit": 50, "min_occurrences": 2},
    {"limit": 50, "start_year": 2021, "end_year": 2022},
    {"limit": 50, "category": "issue", "value": "issue-1"},
    {"limit": 50, "category": "issue", "value": "absent"},
])
def test_surprises_complete_json_matches_legacy(graph, kwargs):
    engine, client, _ = graph
    with Session(engine) as db:
        expected = jsonable_encoder(legacy_surprises(db, **kwargs))
    with Session(engine) as db:
        actual = jsonable_encoder(cm.citation_surprise_feed(db, **kwargs))
    assert actual == expected
    assert client.get("/citation-map/surprises", params=kwargs).json() == expected


def test_tags_complete_json_matches_repaired_legacy(graph):
    engine, client, _ = graph
    with Session(engine) as db:
        expected = jsonable_encoder(legacy_tags(db))
    with Session(engine) as db:
        actual = jsonable_encoder(cm.case_legal_tags(db, 2, limit=250, display_limit=3))
    assert actual == expected
    # Existing response model omits the helper-only display flag.
    expected_http = [{key: value for key, value in tag.items() if key != "display"}
                     for tag in expected]
    assert client.get("/citation-map/cases/2/tags",
                      params={"limit": 250, "display_limit": 3}).json() == expected_http


def legacy_contexts(db, source_id, target_id, limit=50):
    target = aliased(Case)
    rows = db.execute(select(Citation, CaseChunk, Case, target)
        .join(CaseChunk, CaseChunk.id == Citation.chunk_id)
        .join(Case, Case.id == Citation.source_case_id)
        .join(target, target.id == Citation.target_case_id)
        .where(Citation.source_case_id == source_id, Citation.target_case_id == target_id,
               Citation.offset_start.is_not(None), Citation.offset_end.is_not(None))
        .order_by(CaseChunk.chunk_index, Citation.offset_start, Citation.id).limit(limit))
    result, seen = [], set()
    for citation, chunk, source, authority in rows:
        start = int(citation.offset_start or 0)
        end = int(citation.offset_end or start)
        context, context_start, context_end = cm._citation_context(chunk.text, start, end)
        key = citation.normalized_citation or "", " ".join(context.split())
        if key in seen:
            continue
        seen.add(key)
        result.append({
            "citation_id": citation.id, "source_case_id": source.id,
            "source_title": source.title, "source_citation": source.citation,
            "target_case_id": authority.id, "target_title": authority.title,
            "target_citation": authority.citation, "chunk_id": chunk.id,
            "chunk_index": chunk.chunk_index, "citation_text": citation.citation_text,
            "normalized_citation": citation.normalized_citation,
            "offset_start": start, "offset_end": end, "context_start": context_start,
            "context_end": context_end, "context": context,
        })
    return result


def legacy_signals(db, case_id=2, limit=80, context_limit=3):
    edges = cm._aggregated_edges()
    frequency = select(
        edges.c.target_case_id,
        func.count(edges.c.source_case_id).label("citing_cases"),
    ).group_by(edges.c.target_case_id).cte()
    rows = list(db.execute(select(
        Case, CitationMetrics, edges.c.occurrence_count, frequency.c.citing_cases,
    ).join(edges, edges.c.target_case_id == Case.id)
        .join(frequency, frequency.c.target_case_id == Case.id)
        .outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
        .where(edges.c.source_case_id == case_id, edges.c.target_case_id != case_id)
        .order_by(edges.c.occurrence_count.desc(), frequency.c.citing_cases, Case.id)
        .limit(limit)))
    total = max(1, sum(int(row[2]) for row in rows))
    results = []
    for authority, metrics, occurrence_count, global_count in rows:
        stats = db.execute(select(
            func.count(Citation.id), func.count(func.distinct(Citation.chunk_id)),
            func.min(CaseChunk.chunk_index), func.max(CaseChunk.chunk_index),
        ).outerjoin(CaseChunk, CaseChunk.id == Citation.chunk_id).where(
            Citation.source_case_id == case_id, Citation.target_case_id == authority.id,
        )).first()
        occurrences = int(stats[0] or 0) if stats else int(occurrence_count)
        chunks = int(stats[1] or 0) if stats else 0
        contexts = legacy_contexts(db, case_id, authority.id, max(1, context_limit))
        score = log1p(occurrences) / (1 + log1p(max(1, int(global_count or 0))))
        results.append({
            "authority": cm._case_node(authority, metrics),
            "occurrence_count": occurrences, "distinct_chunks": chunks,
            "gravity_share": occurrences / total, "global_citing_cases": int(global_count or 0),
            "surprise_score": float(score),
            "originality_score": float(score * (chunks / max(1, occurrences))),
            "boilerplate_hits": sum(
                any(phrase in context["context"].lower() for phrase in cm._STANDARD_TEST_PHRASES)
                for context in contexts
            ),
            "first_chunk_index": int(stats[2]) if stats and stats[2] is not None else None,
            "last_chunk_index": int(stats[3]) if stats and stats[3] is not None else None,
            "sample_contexts": contexts,
        })
    return sorted(results, key=lambda row: (row["surprise_score"], row["occurrence_count"]), reverse=True)


@pytest.mark.parametrize("limit,context_limit", [(80, 3), (3, 1), (80, 10), (1, 0)])
def test_signals_complete_json_matches_legacy(graph, limit, context_limit):
    engine, client, _ = graph
    with Session(engine) as db:
        expected = jsonable_encoder(legacy_signals(db, limit=limit, context_limit=context_limit))
    with Session(engine) as db:
        actual = jsonable_encoder(cm.citation_authority_signals(
            db, 2, limit=limit, context_limit=context_limit,
        ))
    assert actual == expected
    assert client.get("/citation-map/cases/2/authority-signals", params={
        "limit": limit, "context_limit": max(1, context_limit),
    }).json() == expected


def legacy_table(db, case_id=1, **kwargs):
    page, size = kwargs.get("page", 1), kwargs.get("page_size", 50)
    counts = select(
        Citation.source_case_id, func.count(Citation.id).label("mention_count"),
    ).where(Citation.target_case_id == case_id).group_by(Citation.source_case_id).having(
        func.count(Citation.id) >= kwargs.get("min_mentions", 1),
    ).cte()
    base = select(Citation, Case, CaseChunk, counts.c.mention_count).join(
        Case, Case.id == Citation.source_case_id,
    ).outerjoin(CaseChunk, CaseChunk.id == Citation.chunk_id).join(
        counts, counts.c.source_case_id == Citation.source_case_id,
    ).where(Citation.target_case_id == case_id)
    if kwargs.get("year"):
        base = base.where(func.extract("year", Case.date) == kwargs["year"])
    if kwargs.get("court"):
        base = base.where(Case.court.ilike(f"%{kwargs['court']}%"))
    if kwargs.get("judge"):
        base = base.where(Case.metadata_json["reader_extracted"]["judge"].as_string().ilike(
            f"%{kwargs['judge']}%",
        ))
    if kwargs.get("gov_outcome"):
        base = base.where(func.lower(
            Case.metadata_json["reader_extracted"]["government outcome"].as_string(),
        ) == kwargs["gov_outcome"].lower())
    total = db.scalar(select(func.count()).select_from(base.subquery())) or 0
    rows = db.execute(base.order_by(
        Case.date.desc(), Citation.source_case_id, Citation.id,
    ).offset((page - 1) * size).limit(size))
    result = []
    for citation, case, chunk, count in rows:
        metadata = (case.metadata_json or {}).get("reader_extracted", {})
        result.append({
            "citation_id": citation.id, "case_id": case.id, "case_title": case.title,
            "case_citation": case.citation, "court": case.court,
            "date": str(case.date) if case.date else None,
            "judge": metadata.get("judge"), "gov_outcome": metadata.get("government outcome"),
            "mention_count": int(count or 0), "chunk_id": chunk.id if chunk else None,
            "chunk_index": chunk.chunk_index if chunk else None,
            "citation_text": citation.citation_text, "chunk_text": chunk.text if chunk else None,
        })
    return {"total": int(total), "page": page, "page_size": size,
            "total_pages": max(1, -(-int(total) // size)), "rows": result}


@pytest.mark.parametrize("kwargs", [
    {"page_size": 200}, {"page": 2, "page_size": 3}, {"court": "FC"},
    {"year": 2021}, {"judge": "Judge A"}, {"gov_outcome": "WON"},
    {"min_mentions": 2}, {"court": "absent"},
])
def test_table_complete_json_matches_legacy(graph, kwargs):
    engine, client, _ = graph
    with Session(engine) as db:
        expected = jsonable_encoder(legacy_table(db, **kwargs))
    with Session(engine) as db:
        actual = jsonable_encoder(cm.citation_intelligence_table(db, 1, **kwargs))
    assert actual == expected
    assert client.get("/api/citation-intelligence/1/table", params=kwargs).json() == expected


@pytest.mark.parametrize("term", ["Fixture", "2020 FC 1", "absent", ""])
def test_search_and_cases_complete_json_matches_legacy(graph, term):
    engine, client, _ = graph
    with Session(engine) as db:
        search_rows = [] if not term else db.execute(select(Case, CitationMetrics)
            .outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
            .where(or_(Case.citation.ilike(f"%{term}%"), Case.title.ilike(f"%{term}%")))
            .order_by((Case.citation == term).desc(), Case.date.desc(), Case.id.desc()).limit(50))
        expected_search = jsonable_encoder([cm._case_node(case, metrics) for case, metrics in search_rows])
        cases = [] if not term else db.scalars(select(Case)
            .where(Case.title.ilike(f"%{term}%"))
            .order_by(Case.date.desc(), Case.id.desc()).limit(50))
        expected_cases = jsonable_encoder([{
            "case_id": case.id, "title": case.title, "citation": case.citation,
            "court": case.court, "date": case.date,
        } for case in cases])
    assert client.get("/api/citation-intelligence/search", params={"q": term, "limit": 50}).json() == expected_search
    assert client.get("/api/citation-intelligence/cases", params={"title": term, "limit": 50}).json() == expected_cases


@pytest.mark.parametrize("limit", [1, 3, 50])
def test_context_complete_json_matches_legacy(graph, limit):
    engine, _, _ = graph
    with Session(engine) as db:
        expected = jsonable_encoder(legacy_contexts(db, 2, 101, limit))
    with Session(engine) as db:
        actual = jsonable_encoder(cm.citation_contexts(db, 2, 101, limit))
    assert actual == expected


@pytest.mark.parametrize("path,expected_count", [
    ("/api/citation-intelligence/search?q=Fixture", 1),
    ("/api/citation-intelligence/cases?title=Fixture", 1),
    ("/api/citation-intelligence/1/table?page_size=200", 3),
])
def test_unused_large_fields_are_not_selected(graph, path, expected_count):
    engine, client, _ = graph
    with count_statements(engine) as counter:
        response = client.get(path)
    assert response.status_code == 200
    assert counter.count == expected_count
    # Table's unchanged route existence check still reads a full Case; inspect
    # the count/data statements, not that out-of-scope route-level lookup.
    statements = counter.statements[1:] if "/table" in path else counter.statements
    for statement in statements:
        assert "full_text" not in statement
        assert "source_html" not in statement
        assert "embedding" not in statement
    if "/table" in path:
        assert "case_chunks.text" not in statements[0]
        assert "case_chunks.text" in statements[1]


def test_context_projection_and_limit_before_dedup(graph):
    engine, _, n = graph
    with Session(engine) as db:
        db.add(CaseChunk(
            id=99999, case_id=2, chunk_index=n + 1,
            text="A later distinct context", text_hash="later", token_estimate=10,
        ))
        db.flush()
        db.add(Citation(
            source_case_id=2, target_case_id=101, chunk_id=99999,
            citation_text="2020 FC 101", normalized_citation="2020 FC 101",
            offset_start=2, offset_end=8,
        ))
        db.commit()
    for limit in [1, 2, 3, 10]:
        with Session(engine) as db:
            expected = legacy_contexts(db, 2, 101, limit)
        with Session(engine) as db, count_statements(engine) as counter:
            actual = cm.citation_contexts(db, 2, 101, limit)
        assert actual == expected
        assert counter.count == 1
        assert all(field not in counter.statements[0]
                   for field in ["full_text", "source_html", "embedding"])
        with Session(engine) as db:
            expected_signals = legacy_signals(db, context_limit=limit)
        with Session(engine) as db, count_statements(engine) as counter:
            actual_signals = cm.citation_authority_signals(db, 2, limit=80, context_limit=limit)
        assert actual_signals == expected_signals
        assert counter.count == 3
        assert all(field not in counter.statements[-1]
                   for field in ["full_text", "source_html", "embedding"])
    # The first two occurrences are duplicates. Do not fill the context limit
    # with the later distinct row, which would change boilerplate/scores/JSON.
    with Session(engine) as db:
        assert len(cm.citation_contexts(db, 2, 101, 2)) == 1
        assert len(cm.citation_contexts(db, 2, 101, 3)) == 2


@pytest.mark.parametrize("focus_ids", [(), (1, 2, 11, 101)])
def test_optimized_graph_reads_preserve_focus_scope(graph, monkeypatch, focus_ids):
    engine, _, _ = graph
    monkeypatch.setenv("CASELIBRARY_FOCUS_MASTER_300", "true")
    monkeypatch.setattr(cm, "_focused_case_ids", lru_cache(maxsize=1)(lambda: focus_ids))
    with Session(engine) as db:
        expected_surprises = legacy_surprises(db, limit=250)
        expected_signals = legacy_signals(db)
    with Session(engine) as db:
        assert cm.citation_surprise_feed(db, limit=250) == expected_surprises
    with Session(engine) as db:
        assert cm.citation_authority_signals(db, 2, limit=80) == expected_signals


def test_empty_and_missing_routes_do_not_fetch_extra_rows(graph):
    engine, client, _ = graph
    for path in [
        "/api/citation-intelligence/search", "/api/citation-intelligence/cases",
    ]:
        with count_statements(engine) as counter:
            response = client.get(path)
        assert response.json() == []
        assert counter.count == 0
    for suffix in ["overview", "timeline", "outcomes", "courts", "judges",
                   "statutes", "companions", "table"]:
        with count_statements(engine) as counter:
            response = client.get(f"/api/citation-intelligence/999999/{suffix}")
        assert response.status_code == 404
        assert counter.count == 1
    with Session(engine) as db, count_statements(engine) as counter:
        assert cm.citation_surprise_feed(db, category="issue", value="absent") == []
    assert counter.count == 1
    with Session(engine) as db, count_statements(engine) as counter:
        assert cm.citation_authority_signals(db, 1) == []
    assert counter.count == 1


def test_repaired_legacy_tag_oracle_documents_growth(graph, monkeypatch):
    """Diagnostic oracle only: actual baseline raised NameError after two SQLs."""
    engine, client, n = graph
    monkeypatch.setattr(routes, "_case_legal_tags", legacy_tags)
    with count_statements(engine) as counter:
        response = client.get("/citation-map/cases/2/tags?limit=250&display_limit=3")
    assert response.status_code == 200
    assert counter.count == n + 3
