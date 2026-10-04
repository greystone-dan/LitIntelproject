"""Cold-session SQLite measurements and independent, complete payload oracles.

The active search statement is PostgreSQL text SQL. Its fixed SUBSTRING syntax
and empty-query label are adapted for SQLite; no pagination/ranking is changed.
The court:FC / NOT court:FC operator predicates execute without adaptation.

BEFORE (5/50 related rows), measured before editing analytics_service:
judge list 6/51; judge detail 8/53; inline detail 8/53; issue brief 2/2;
active search 1/1 (SQLite adapter); FC 3/3 then AttributeError(source_type).
AFTER budgets: 2/2, 3/3, 3/3, 2/2, 1/1, 3/3 respectively.
FC's oracle describes the intended raw-row aggregation with the missing source
column/city alias repaired; a successful legacy payload did not exist.
"""

from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path
import re
import sys

import pytest
from fastapi.encoders import jsonable_encoder
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, event
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session

from backend import analytics_service as service
from backend.database import (
    Base, Case, CaseChunk, CaseJudgeProfile, CaseTag, Citation,
    FCActivityCase, FCActivityClassification, JudgeProfile,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from performance_helpers import count_statements


@compiles(Vector, "sqlite")
def sqlite_vector(_type, _compiler, **_kw):
    return "JSON"


def wire(value):
    return json.loads(json.dumps(jsonable_encoder(value)))


def reader(row):
    metadata = row["metadata_json"]
    value = metadata.get("reader_extracted") if isinstance(metadata, dict) else None
    return value if isinstance(value, dict) else {}


def party(row):
    match = re.search(r"\bCanada\s+\(([^)]+)\)", row["title"], re.I)
    return " ".join(match[1].split()) if match else None


@pytest.fixture(params=[5, 50], ids=["5-related", "50-related"])
def cohort(request, monkeypatch):
    n = request.param
    engine = create_engine("sqlite:///:memory:")

    @event.listens_for(engine, "connect")
    def sqlite_functions(connection, _record):
        connection.create_function("test_minister", 1, lambda title: (
            re.search(r"Canada [(]([^)]*)[)]", title)[1]
            if re.search(r"Canada [(]([^)]*)[)]", title) else None))

    @event.listens_for(engine, "before_cursor_execute", retval=True)
    def postgres_substring(_conn, _cursor, sql, params, _context, _many):
        return sql.replace(
            "SUBSTRING(c.title FROM 'Canada [(]([^)]*)[)]')",
            "test_minister(c.title)",
        ), params

    Base.metadata.create_all(engine, tables=[
        model.__table__ for model in (
            Case, CaseChunk, CaseJudgeProfile, CaseTag, Citation, JudgeProfile,
            FCActivityCase, FCActivityClassification,
        )
    ])
    cases = [
        dict(id=i, title=f"Applicant {i} v. Canada ({'Immigration' if i % 2 else 'Public Safety'})",
             court="FCA" if i % 3 == 0 else "FC", date=date(2024, 1, 1 + i % 3),
             citation=f"2024 FC {i}", full_text="unused body " * 100,
             source_html="unused html " * 100, summary="unused summary",
             metadata_json={"reader_extracted": {
                 "government outcome": ["won", "lost", None][i % 3],
                 "decision outcome": ["allowed", "dismissed", None][i % 3],
                 "government role": "respondent", "case type": "JR",
                 "judge": "Judge Main",
             }} if i % 5 else {"reader_extracted": ["malformed"]})
        for i in range(1, n + 1)
    ]
    text = " ".join(f"2024 FC {i};" for i in range(1, n + 1))
    source = dict(id=1000, title="Inline v. Canada (Immigration)", court="FC",
                  citation="2025 FC 1000", date=date(2025, 1, 1),
                  full_text=text, summary=None, source_html="unused",
                  metadata_json={"reader_extracted": {"judge": "Judge Inline"}})
    cases.append(source)
    profiles = [
        dict(id=i, slug=f"judge-{i}", display_name=(
            "Judge Main" if i == 1 else ("Judge a" if i % 2 else "Judge A")),
             normalized_name=f"judge {i}", primary_court="FC",
             aliases=["Main"] if i == 1 else None)
        for i in range(1, n + 1)
    ]
    links = [(1, i) for i in range(1, n + 1)] + [(i, i) for i in range(2, n + 1)]
    citations = [
        dict(id=i, source_case_id=1000, target_case_id=i, chunk_id=1,
             citation_text=f"2024 FC {i}", normalized_citation=f"2024 FC {i}",
             offset_start=text.index(f"2024 FC {i};"),
             offset_end=text.index(f"2024 FC {i};") + len(f"2024 FC {i}"))
        for i in range(1, n + 1)
    ]
    citations += [
        dict(id=n + 1, source_case_id=1000, target_case_id=1, chunk_id=1,
             citation_text="duplicate", normalized_citation="2024 FC 1",
             offset_start=0, offset_end=9),
        dict(id=n + 2, source_case_id=1000, target_case_id=None, chunk_id=1,
             citation_text="unresolved", normalized_citation=None,
             offset_start=0, offset_end=9),
        dict(id=n + 3, source_case_id=1000, target_case_id=2, chunk_id=1,
             citation_text="invalid", normalized_citation=None,
             offset_start=-1, offset_end=2),
        dict(id=n + 4, source_case_id=1000, target_case_id=2, chunk_id=None,
             citation_text="no chunk", normalized_citation=None,
             offset_start=None, offset_end=None),
        dict(id=n + 5, source_case_id=1, target_case_id=1, chunk_id=None,
             citation_text="self", normalized_citation=None,
             offset_start=None, offset_end=None),
        dict(id=n + 6, source_case_id=3, target_case_id=1, chunk_id=None,
             citation_text="appeal", normalized_citation=None,
             offset_start=None, offset_end=None),
    ]
    fc = [
        dict(source_key=f"test-{i}", year=2023 + i % 2,
             city_filed=["Ottawa", "", "   ", None][i % 4],
             case_class=["JR", None][i % 2], track=["", "Standard"][i % 2],
             source_type=["test", None, ""][i % 3],
             classification_json={
                 key: {"status": ["resolved", None, ""][i % 3]}
                 for key in ("full_history_resolution", "closing_status", "leave_context")
             } | {"challenged_decision": {"application_type": "JR" if i % 2 else None}})
        for i in range(n)
    ]
    with Session(engine) as db:
        db.add_all(Case(**row) for row in cases)
        db.add_all(JudgeProfile(**row) for row in profiles)
        db.add_all(FCActivityCase(id=i + 1, **{
            k: v for k, v in row.items() if k != "classification_json"
        }) for i, row in enumerate(fc))
        db.flush()
        db.add(CaseChunk(id=1, case_id=1000, chunk_index=0, text=text,
                         text_hash="fixture", token_estimate=10))
        db.add_all(CaseJudgeProfile(judge_profile_id=j, case_id=c, raw_name="test")
                   for j, c in links)
        db.add_all(Citation(**row) for row in citations)
        db.add_all(FCActivityClassification(
            source_case_id=i + 1, classifier_version="test", **row)
            for i, row in enumerate(fc))
        db.add(FCActivityCase(source_key="unclassified", year=2024, source_type="test"))
        db.add_all(CaseTag(case_id=i, category="issue", value="fairness", score=1,
                           evidence="test", source="test",
                           taxonomy_version=service.ACTIVE_TAG_TAXONOMY_VERSION)
                   for i in range(1, n + 1))
        db.commit()
    monkeypatch.setattr(service, "_analytics_cache", service.TTLCache())
    original_label = service.matched_on_sql

    def sqlite_empty_label(query, **kwargs):
        # Empty-query branches are all false in PG, but SQLite cannot parse
        # the unused regex operators. Nonempty queries are NOT simulated here;
        # operator search replaces this label with its own bound value.
        return ("'Metadata'", {}) if not query else original_label(query, **kwargs)

    monkeypatch.setattr(service, "matched_on_sql", sqlite_empty_label)
    yield dict(engine=engine, n=n, cases=cases, profiles=profiles,
               links=links, citations=citations, fc=fc)
    engine.dispose()


def invoke(cohort, fn, **kwargs):
    # Never carry an identity map or fixture setup into an endpoint measurement.
    with Session(cohort["engine"]) as db:
        with count_statements(cohort["engine"]) as counter:
            result = fn(db, **kwargs)
    return wire(result), counter


def list_oracle(data, q="", limit=50):
    rows = [row for row in data["profiles"] if not q.strip() or
            q.strip().lower() in row["display_name"].lower() or
            q.strip().lower() in row["normalized_name"].lower()]
    if q.strip():
        rows.sort(key=lambda row: row["display_name"])
    counts = Counter(j for j, _ in data["links"])
    rows.sort(key=lambda row: (-counts[row["id"]], row["display_name"].lower()))
    return [dict(slug=row["slug"], display_name=row["display_name"],
                 primary_court=row["primary_court"], aliases=row["aliases"] or [],
                 decision_count=counts[row["id"]])
            for row in rows[:max(1, min(100, limit))]]


def judge_oracle(data, ministers):
    all_cases = [row for row in data["cases"] if row["id"] != 1000]
    filters = [" ".join(value.split()) for value in ministers if value.strip()]
    rows = [row for row in all_cases if not filters or
            (party(row) and party(row).casefold() in {v.casefold() for v in filters})]
    outcomes = Counter(reader(row).get("government outcome") for row in rows)
    wins, losses = outcomes["won"], outcomes["lost"]
    result = dict(
        profile={k: data["profiles"][0][k] for k in (
            "slug", "display_name", "primary_court", "aliases")},
        filter=dict(ministers=filters,
                    available_ministers=sorted({party(row) for row in all_cases if party(row)},
                                              key=str.casefold)),
        outcomes=dict(government_wins=wins, individual_wins=losses,
                      unclassified=len(rows) - wins - losses, classified=wins + losses,
                      all_linked=len(rows),
                      government_win_rate=round(wins / (wins + losses) * 100, 1)
                      if wins + losses else None),
        yearly_decisions=[dict(year=y, decisions=c) for y, c in sorted(
            Counter(str(row["date"])[:4] for row in rows if row["date"]).items())],
        decisions=[],
    )
    by_id = {row["id"]: row for row in data["cases"]}
    for row in sorted(rows, key=lambda item: item["date"] or "", reverse=True):
        citing = {c["source_case_id"] for c in data["citations"]
                  if c["target_case_id"] == row["id"] and c["source_case_id"] != row["id"]}
        result["decisions"].append(dict(
            case_id=row["id"], **{k: row[k] for k in ("title", "citation", "court", "date")},
            government_party=party(row), government_role=reader(row).get("government role"),
            government_outcome=reader(row).get("government outcome"),
            decision_outcome=reader(row).get("decision outcome"),
            case_type=reader(row).get("case type"), cited_by_cases=len(citing),
            cited_by_appeal_courts=sum(by_id[c]["court"] in ("FCA", "SCC") for c in citing),
        ))
    return wire(result)


def detail_oracle(data):
    source = data["cases"][-1]
    rows = [row for row in data["citations"] if row["source_case_id"] == 1000]
    targets = {row["id"]: row for row in data["cases"]}
    highlights = []
    for row in rows:
        start, end = row["offset_start"], row["offset_end"]
        if row["chunk_id"] is None or start is None or end is None:
            continue
        if not 0 <= start < end <= len(source["full_text"]):
            continue
        target = targets.get(row["target_case_id"], {})
        highlights.append(dict(
            text=row["citation_text"], normalized=row["normalized_citation"],
            offset_start=start, offset_end=end, target_case_id=row["target_case_id"],
            target_title=target.get("title"), target_citation=target.get("citation"),
        ))
    return wire(dict(
        case={k: source[k] for k in ("id", "title", "citation", "court", "date", "full_text")} |
             dict(judge="Judge Inline", government_outcome=None, government_role=None,
                  decision_outcome=None),
        citation_metrics=dict(citation_mentions=len(rows),
                              unique_cited_authorities=len({
                                  (row["normalized_citation"] or row["citation_text"] or "").strip()
                                  for row in rows
                                  if (row["normalized_citation"] or row["citation_text"] or "").strip()}),
                              resolved_target_cases=len({row["target_case_id"] for row in rows
                                                         if row["target_case_id"] is not None})),
        citations=highlights,
    ))


@pytest.mark.parametrize("q,limit", [("", 50), ("Judge", 3), ("Main", 0), ("absent", 100)])
def test_judge_list(cohort, q, limit):
    result, counter = invoke(cohort, service._fetch_judge_profiles_impl, q=q, limit=limit)
    assert result == list_oracle(cohort, q, limit)
    assert counter.count == (1 if not result else 2)


@pytest.mark.parametrize("ministers", [[], ["  iMmIgRaTiOn ", " "], ["Public Safety"], ["absent"]])
def test_judge_detail(cohort, ministers):
    result, counter = invoke(cohort, service.fetch_judge_profile_by_slug,
                             slug="judge-1", ministers=ministers)
    assert result == judge_oracle(cohort, ministers)
    assert counter.count == 2 + bool(result["decisions"])
    assert_narrow(counter)


def test_inline_detail(cohort):
    result, counter = invoke(cohort, service.fetch_analytics_search_case_detail, case_id=1000)
    assert result == detail_oracle(cohort)
    assert counter.count == 3
    assert_narrow(counter, allow_source_body=True)


def fc_oracle(data, x="year", group_by="full_history_resolution",
              year_from=None, year_to=None, city="", source_type=""):
    def matches(row):
        return (
            (year_from is None or row["year"] is not None and row["year"] >= year_from)
            and (year_to is None or row["year"] is not None and row["year"] <= year_to)
            and (not city.strip() or row["city_filed"] == city.strip())
            and (not source_type.strip() or row["source_type"] == source_type.strip())
        )
    rows = [row for row in data["fc"] if matches(row)]
    counts = Counter()
    sources = Counter()
    for row in rows:
        value = row["city_filed" if x == "city" else x]
        label = str(value) if value is not None and str(value).strip() else "Unknown"
        group = row["classification_json"].get(
            "challenged_decision" if group_by == "application_type" else group_by, {})
        group_value = group.get("application_type" if group_by == "application_type" else "status")
        counts[label, str(group_value or "Unknown")] += 1
        sources[row["source_type"] or "unknown"] += 1
    x_values = sorted({k[0] for k in counts},
                      key=lambda v: (0, int(v)) if v.isdigit() else (1, v))[:60]
    groups = sorted({k[1] for k in counts})
    missing = int(matches(dict(year=2024, city_filed=None, source_type="test")))
    return dict(
        x=x, x_label={"year": "Year filed", "city": "City filed",
                      "case_class": "Case class", "track": "Track"}[x],
        group_by=group_by, total=len(rows), source_type=source_type.strip() or None,
        source_counts=dict(sorted(sources.items())),
        coverage=dict(activity_cases=len(rows) + missing, classified_cases=len(rows),
                      missing_classifications=missing),
        x_values=x_values,
        groups=[dict(label=g, values=[counts[v, g] for v in x_values]) for g in groups],
    )


@pytest.mark.parametrize("x", ["year", "city", "case_class", "track"])
@pytest.mark.parametrize("group_by", [
    "full_history_resolution", "closing_status", "leave_context", "application_type",
])
@pytest.mark.parametrize("filters", [
    {}, {"year_from": 2024, "year_to": 2024},
    {"city": " Ottawa ", "source_type": " test "}, {"city": "missing"},
])
def test_fc_grouped_parity(cohort, x, group_by, filters):
    kwargs = dict(x=x, group_by=group_by, **filters)
    result, counter = invoke(cohort, service._fetch_fc_activity_analytics_impl, **kwargs)
    assert result == fc_oracle(cohort, **kwargs)
    assert counter.count == 3
    assert "GROUP BY" in counter.statements[0]
    assert "source_type" in counter.statements[0]
    assert "count(*)" in counter.statements[0].lower()
    assert "case_name" not in counter.statements[0]


def test_fc_null_year_and_missing_json(cohort):
    cohort["fc"][0]["year"] = None
    cohort["fc"][0]["classification_json"] = {}
    with Session(cohort["engine"]) as db:
        db.get(FCActivityCase, 1).year = None
        row = db.get(FCActivityClassification, 1)
        row.year = None
        row.classification_json = {}
        db.commit()
    result, counter = invoke(cohort, service._fetch_fc_activity_analytics_impl)
    assert result == fc_oracle(cohort)
    assert counter.count == 3
    assert "Unknown" in result["x_values"]


def search_oracle(data, limit, offset, *, court=None,
                  query_echo="(empty query)", matched_on="Metadata"):
    rows = [row for row in data["cases"] if court is None or row["court"] == court]
    rows.sort(key=lambda row: (row["date"], row["id"]), reverse=True)
    results = []
    for row in rows[offset:offset + limit]:
        citations = [c for c in data["citations"] if c["source_case_id"] == row["id"]]
        results.append(dict(
            case_id=row["id"], **{k: row[k] for k in ("title", "citation", "court", "date")},
            judge=reader(row).get("judge"), minister=party(row),
            decision_outcome=reader(row).get("decision outcome"),
            government_outcome=reader(row).get("government outcome"), matching_citations=0,
            citation_mentions=len(citations),
            unique_cited_authorities=len({c["normalized_citation"] or c["citation_text"]
                                          for c in citations}),
            resolved_target_cases=len({c["target_case_id"] for c in citations
                                       if c["target_case_id"] is not None}),
            cited_by_cases=len({c["source_case_id"] for c in data["citations"]
                               if c["target_case_id"] == row["id"] and
                               c["source_case_id"] != row["id"]}),
            matched_on=matched_on,
        ))
    return wire(dict(results=results, limit=limit, offset=offset, query_echo=query_echo))


@pytest.mark.parametrize("limit,offset", [(3, 1), (100, 0)])
def test_active_search_already_bounded(cohort, limit, offset):
    result, counter = invoke(cohort, service.fetch_analytics_search_cases,
                             limit=limit, offset=offset)
    assert result == search_oracle(cohort, limit, offset)
    assert counter.count == 1
    assert "LIMIT" in counter.statements[0] and "OFFSET" in counter.statements[0]
    assert_narrow(counter)


@pytest.mark.parametrize("query,court,echo", [
    ("court:FC", "FC", "filters: court: FC"),
    ("NOT court:FC", "FCA", 'meaning: NOT (court: "FC") | filters: court: FC'),
])
@pytest.mark.parametrize("limit,offset", [(3, 1), (100, 0)])
def test_active_operator_search_already_bounded(cohort, query, court, echo, limit, offset):
    result, counter = invoke(cohort, service.fetch_analytics_search_cases,
                             query=query, limit=limit, offset=offset)
    assert result == search_oracle(cohort, limit, offset, court=court,
                                  query_echo=echo, matched_on="Query operators")
    assert counter.count == 1
    assert "LIMIT" in counter.statements[0] and "OFFSET" in counter.statements[0]
    assert "UPPER(c.court) IN ('FC', 'FEDERAL COURT')" in counter.statements[0]
    assert_narrow(counter)


@pytest.mark.parametrize("endpoint", ["judge", "fc"])
def test_real_cache_cold_disabled_and_warm(cohort, endpoint):
    fn, kwargs, expected, budget = (
        (service.fetch_judge_profiles, {"q": "Judge"}, list_oracle(cohort, "Judge"), 2)
        if endpoint == "judge" else
        (service.fetch_fc_activity_analytics, {}, fc_oracle(cohort), 3)
    )
    service.set_analytics_cache_enabled(False)
    disabled, counter = invoke(cohort, fn, **kwargs)
    assert disabled == [expected, False]
    assert counter.count == budget
    service.set_analytics_cache_enabled(True)
    cold, counter = invoke(cohort, fn, **kwargs)
    assert cold == disabled
    assert counter.count == budget
    warm, counter = invoke(cohort, fn, **kwargs)
    assert warm == [expected, True]
    assert counter.count == 0


@pytest.mark.parametrize("endpoint", ["judge", "fc"])
def test_real_cache_expiry(cohort, endpoint, monkeypatch):
    now = [0]
    monkeypatch.setattr(service, "_analytics_cache",
                        service.TTLCache(ttl_seconds=10, clock=lambda: now[0]))
    fn = service.fetch_judge_profiles if endpoint == "judge" else service.fetch_fc_activity_analytics
    budget = 2 if endpoint == "judge" else 3
    cold, counter = invoke(cohort, fn)
    assert counter.count == budget
    now[0] = 9
    warm, counter = invoke(cohort, fn)
    assert warm == [cold[0], True] and counter.count == 0
    now[0] = 10
    expired, counter = invoke(cohort, fn)
    assert expired == cold and counter.count == budget


def test_missing_profile_and_case_preserve_404(cohort):
    from fastapi import HTTPException

    for fn, kwargs, detail in (
        (service.fetch_judge_profile_by_slug, {"slug": "missing"}, "Judge profile not found"),
        (service.fetch_analytics_search_case_detail, {"case_id": -1}, "Case not found"),
    ):
        with Session(cohort["engine"]) as db:
            with count_statements(cohort["engine"]) as counter:
                with pytest.raises(HTTPException) as error:
                    fn(db, **kwargs)
        assert error.value.status_code == 404
        assert error.value.detail == detail
        assert counter.count == 1


def issue_oracle(data):
    rows = sorted(data["cases"][:-1], key=lambda row: (row["date"], row["id"]))
    decisions = [
        dict(case_id=row["id"], title=row["title"], citation=row["citation"],
             date=row["date"].isoformat(), year=row["date"].year, court=row["court"],
             outcome=str(reader(row).get("decision outcome") or "unclassified").strip()
             or "unclassified", url=f"/case-reader?case_id={row['id']}")
        for row in rows
    ]
    year_rows = defaultdict(list)
    for row in decisions:
        year_rows[row["year"]].append(row)
    years = []
    for year, group in sorted(year_rows.items()):
        outcomes = Counter(row["outcome"] for row in group)
        years.append(dict(
            year=year, decision_count=len(group), unclassified_count=outcomes["unclassified"],
            outcome_splits=[dict(outcome=o, count=c, percentage=round(c / len(group) * 100, 1),
                                 unclassified_count=outcomes["unclassified"], denominator=len(group))
                            for o, c in sorted(outcomes.items())],
        ))
    ids = {row["id"] for row in rows}
    authority_mentions = Counter()
    authority_sources = defaultdict(set)
    for row in data["citations"]:
        if row["source_case_id"] in ids and row["target_case_id"] is not None:
            authority_mentions[row["target_case_id"]] += 1
            authority_sources[row["target_case_id"]].add(row["source_case_id"])
    by_id = {row["id"]: row for row in data["cases"]}
    return dict(
        tag="issue:fairness", decision_count=len(rows),
        semantics={
            "tag_matching": "Exact category:value match in the active legal-tag taxonomy; decisions are counted once.",
            "outcomes": "Decision outcome from reader_extracted metadata; missing/blank values are unclassified. Percentages use all tagged decisions in that year, including unclassified outcomes.",
            "citations": "Top authorities count stored citation occurrences with a resolved target_case_id from tagged source decisions; citing_decisions counts distinct tagged source cases. Unresolved citations and statute references are excluded.",
        },
        years=years,
        courts=[dict(court=court, decision_count=count) for court, count in sorted(
            Counter(row["court"] for row in rows).items(), key=lambda item: (-item[1], item[0]))],
        top_authorities=[
            dict(case_id=i, title=by_id[i]["title"], citation=by_id[i]["citation"],
                 citation_occurrences=authority_mentions[i],
                 citing_decisions=len(authority_sources[i]), url=f"/case-reader?case_id={i}")
            for i in sorted(authority_mentions, key=lambda i: (-authority_mentions[i], i))[:10]
        ],
        decisions=decisions,
    )


def test_issue_brief(cohort):
    result, counter = invoke(cohort, service.fetch_issue_brief, tag="issue:fairness")
    assert result == issue_oracle(cohort)
    assert counter.count == 2
    assert_narrow(counter)


def assert_narrow(counter, allow_source_body=False):
    sql = "\n".join(counter.statements).lower()
    assert "source_html" not in sql
    assert "embedding" not in sql
    if allow_source_body:
        # The inline reader needs its source body, never target case bodies.
        target_sql = next(s for s in counter.statements if "join cases" in s.lower()).lower()
        assert "full_text" not in target_sql and "summary" not in target_sql
    else:
        assert "full_text" not in sql and "summary" not in sql
