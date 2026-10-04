"""Native SQLite contracts for the FC timeline, breakdowns, and flow services.

Issue138 follow-up: application source is unchanged. "Before" and "after" here
are two measurements of the SAME current implementation in fresh Sessions, not
a historical optimization comparison. At both 5/50 rows the statement budgets
are timeline 2/2, breakdowns 3/3, and flow 1/1.

No SQL rewrites, database-function shims, or application database are used.
SQLite's native JSON extraction supports these three queries. PostgreSQL-only
functions elsewhere remain unsupported: these counts are not PostgreSQL plans,
latency measurements, runtime speedup claims, or HTTP/router coverage.
"""

from collections import Counter
import json

import pytest
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend import analytics_service as service
from backend.database import FCActivityCase, FCActivityClassification
from performance_helpers import count_statements


# Independently fixed response metadata, not imported from the implementation.
CITY_PROVINCES = {
    "Calgary": "Alberta",
    "Edmonton": "Alberta",
    "Charlottetown": "Prince Edward Island",
    "Fredericton": "New Brunswick",
    "Saint John": "New Brunswick",
    "Halifax": "Nova Scotia",
    "Montréal": "Quebec",
    "Québec": "Quebec",
    "Ottawa": "Ontario",
    "Toronto": "Ontario",
    "Regina": "Saskatchewan",
    "Saskatoon": "Saskatchewan",
    "St. John's": "Newfoundland and Labrador",
    "Vancouver": "British Columbia",
    "Whitehorse": "Yukon",
    "Winnipeg": "Manitoba",
    "Yellowknife": "Northwest Territories",
}


# Each specimen declares its expected branch independently of SQL/Python branch
# evaluation. Conflicting lower-priority evidence deliberately tests precedence.
FLOW_SPECIMENS = [
    ("direct_jr_granted", {
        "challenged_decision": {"application_type": "direct_judicial_review"},
        "judicial_review_result": {"result": "granted"},
        "leave_decision": {"result": "refused"},
        "lifecycle_status": {"status": "active"},
    }),
    ("direct_jr_dismissed", {
        "challenged_decision": {"application_type": "direct_judicial_review"},
        "judicial_review_result": {"result": "dismissed"},
        "leave_decision": {"result": "granted"},
    }),
    ("direct_jr_pending", {
        "challenged_decision": {"application_type": "direct_judicial_review"},
        "judicial_review_result": {"result": None},
        "leave_decision": {"result": "refused"},
    }),
    ("leave_refused", {
        "leave_decision": {"result": "refused"},
        "judicial_review_result": {"result": "granted"},
        "lifecycle_status": {"status": "active"},
    }),
    ("leave_jr_granted", {
        "leave_decision": {"result": "granted"},
        "judicial_review_result": {"result": "granted"},
        "lifecycle_status": {"status_kind": "withdrawn"},
    }),
    ("leave_jr_dismissed", {
        "leave_decision": {"result": "granted"},
        "judicial_review_result": {"result": "dismissed"},
    }),
    ("leave_granted_pending_jr", {
        "leave_decision": {"result": "granted"},
        "judicial_review_result": {"result": ""},
        "lifecycle_status": {"status": "active"},
    }),
    ("active", {
        "lifecycle_status": {"status": "abeyance", "status_kind": "withdrawn"},
    }),
    ("closed_before_leave", {
        "lifecycle_status": {"status_kind": "administratively_terminated"},
    }),
    ("unresolved", {}),
]


@pytest.fixture(params=[5, 50], ids=["5-rows", "50-rows"])
def corpus(request):
    """Exactly n case rows and n classification rows, setup outside counting."""
    engine = create_engine("sqlite:///:memory:")
    for model in (FCActivityCase, FCActivityClassification):
        model.__table__.create(engine)
    cases, classifications = [], []
    for index in range(request.param):
        kind = index % 10
        branch, payload = FLOW_SPECIMENS[kind]
        cases.append(dict(
            id=index + 1, source_key=f"summary-{index}",
            year=[2002, 2003, 2024, None, 2024, 2025, 2024, 2003, 2025, 2024][kind],
            city_filed=["Old registry", "Ottawa", None, "Toronto", "",
                        "Montréal", "   ", "Ottawa", "Vancouver", "Remote"][kind],
            case_class=[None, "", "JR", "   ", "Appeal"][index % 5],
            track=f"Track {index % 15:02d}" if index % 5 else None,
            raw_payload={"unused": "x" * 10000},
        ))
        # Classification locations/years intentionally differ from case fields:
        # summaries read cases, while flow reads classifications, with no year cut.
        classifications.append(dict(
            source_case_id=index + 1, source_key=f"summary-{index}",
            year=1999, city_filed=["Ottawa", "Toronto", None, "", "Montréal"][index % 5],
            source_type=["portal", "archive", None, ""][index % 4],
            classifier_version="offline", classification_json=payload,
            expected_branch=branch,
        ))
    try:
        with Session(engine) as db:
            db.add_all(FCActivityCase(**row) for row in cases)
            db.flush()
            db.add_all(FCActivityClassification(**{
                key: value for key, value in row.items() if key != "expected_branch"
            }) for row in classifications)
            db.commit()
        yield dict(engine=engine, n=request.param, cases=cases,
                   classifications=classifications)
    finally:
        engine.dispose()


def wire(value):
    return json.loads(json.dumps(jsonable_encoder(value)))


def measure_current_twice(data, endpoint, kwargs, expected, ceiling):
    """Before == after, same source, fresh identity map for EVERY invocation."""
    counts = []
    for phase in ("before-current", "after-current"):
        with Session(data["engine"]) as db:
            assert not db.identity_map
            with count_statements(data["engine"]) as counter:
                result = getattr(service, f"fetch_fc_activity_{endpoint}")(db, **kwargs)
        assert wire(result) == wire(expected)
        assert counter.count <= ceiling
        # These queries are uncached; exact counts make the recorded measurements
        # reproducible and prevent a warmed result from masquerading as cold SQL.
        assert counter.count == ceiling
        assert all(sql.lstrip().upper().startswith("SELECT")
                   for sql in counter.statements)
        assert all("raw_payload" not in sql for sql in counter.statements)
        if endpoint != "flow":
            assert all("classification_json" not in sql for sql in counter.statements)
        counts.append(counter.count)
        print(f"{data['n']} rows {endpoint} {kwargs} {phase}: {counter.count}")
    assert counts[0] == counts[1]


def timeline_oracle(data, city):
    selected = city.strip()
    eligible = [row for row in data["cases"]
                if row["year"] is not None and row["year"] >= 2003]
    totals = Counter(row["year"] for row in eligible)
    scoped = Counter(row["year"] for row in eligible
                     if (row["city_filed"] or "Unknown") == selected)
    years = sorted(totals)
    if selected == "Unknown":
        # Preserve CURRENT JSON, not an intended repair: NULL and "" are separate
        # SQL groups but share the response alias. An empty-city group replaces
        # the NULL-city group for the same year (rather than adding to it).
        # The fixture has no literal "Unknown" city. Totals still include both.
        null_cities = Counter(row["year"] for row in eligible
                              if row["city_filed"] is None)
        empty_cities = Counter(row["year"] for row in eligible
                               if row["city_filed"] == "")
        scoped = Counter({year: empty_cities[year] if year in empty_cities
                          else null_cities[year] for year in years})
    counts = scoped if selected else totals
    return dict(
        city=selected or None,
        cities=sorted({row["city_filed"] for row in data["cases"]
                       if row["city_filed"] not in (None, "")}),
        city_provinces=dict(CITY_PROVINCES),
        total=sum(counts.values()),
        rows=[dict(year=year, count=counts[year]) for year in years],
        total_rows=[dict(year=year, count=totals[year]) for year in years],
        province_rows=[],
    )


@pytest.mark.parametrize("city", ["", " Ottawa ", "missing", "Unknown", "   ", "Montréal"])
def test_timeline_complete_json_and_constant_statements(corpus, city):
    measure_current_twice(corpus, "timeline", dict(city=city),
                          timeline_oracle(corpus, city), 2)


def breakdowns_oracle(data, city, limit):
    selected = city.strip()
    rows = [row for row in data["cases"]
            if row["year"] is not None and row["year"] >= 2003
            and (not selected or row["city_filed"] == selected)]
    result = dict(city=selected or None)
    for output, field in (("registry_locations", "city_filed"),
                          ("case_classes", "case_class"), ("tracks", "track")):
        counts = Counter(row[field] if row[field] not in (None, "") else "Unknown"
                         for row in rows)
        ordered = sorted(counts, key=lambda label: (-counts[label], label))
        result[output] = [dict(label=label, count=counts[label])
                          for label in ordered[:max(1, min(limit, 12))]]
    return result


@pytest.mark.parametrize("city,limit", [
    ("", 8), (" Ottawa ", 8), ("missing", 8), ("", 0), ("", -5),
    ("", 1), ("", 12), ("", 99), ("   ", 8), ("Montréal", 2),
])
def test_breakdowns_complete_json_and_constant_statements(corpus, city, limit):
    measure_current_twice(corpus, "breakdowns", dict(city=city, limit=limit),
                          breakdowns_oracle(corpus, city, limit), 3)


def flow_oracle(data, city, source_type):
    selected_city, selected_source = city.strip(), source_type.strip()
    counts = Counter(row["expected_branch"] for row in data["classifications"]
                     if (not selected_city or row["city_filed"] == selected_city)
                     and (not selected_source or row["source_type"] == selected_source))
    values = dict(counts)
    values["total"] = sum(counts.values())
    values["leave_granted"] = sum(counts[key] for key in (
        "leave_jr_granted", "leave_jr_dismissed", "leave_granted_pending_jr"))
    values["direct_jr"] = sum(counts[key] for key in (
        "direct_jr_granted", "direct_jr_dismissed", "direct_jr_pending"))
    labels = [
        ("total", "Classified activity cases"), ("active", "Active / live"),
        ("leave_refused", "Leave dismissed"), ("leave_granted", "Leave granted"),
        ("direct_jr", "Direct JR"), ("closed_before_leave", "Closed before leave"),
        ("unresolved", "Unresolved evidence"), ("leave_jr_granted", "JR granted"),
        ("leave_jr_dismissed", "JR dismissed"),
        ("leave_granted_pending_jr", "JR pending / not observed"),
        ("direct_jr_granted", "JR granted"), ("direct_jr_dismissed", "JR dismissed"),
        ("direct_jr_pending", "JR pending / not observed"),
    ]
    edges = [
        ("total", "active"), ("total", "leave_refused"),
        ("total", "closed_before_leave"), ("total", "unresolved"),
        ("total", "leave_granted"), ("total", "direct_jr"),
        ("leave_granted", "leave_jr_granted"), ("leave_granted", "leave_jr_dismissed"),
        ("leave_granted", "leave_granted_pending_jr"),
        ("direct_jr", "direct_jr_granted"), ("direct_jr", "direct_jr_dismissed"),
        ("direct_jr", "direct_jr_pending"),
    ]
    return dict(
        city=selected_city or None, source_type=selected_source or None,
        total=values["total"],
        nodes=[dict(key=key, label=label, value=values.get(key, 0))
               for key, label in labels],
        links=[dict(source=source, target=target, value=values.get(target, 0))
               for source, target in edges],
        semantics="exclusive_procedural_branches",
        note="Each case is assigned one branch using lifecycle and outcome precedence. "
             "Leave, judicial-review, and applicability fields otherwise overlap and "
             "are not represented as a cross-field Sankey.",
    )


@pytest.mark.parametrize("city,source_type", [
    ("", ""), (" Ottawa ", ""), ("", " portal "), ("Toronto", "archive"),
    ("missing", ""), ("", "missing"), ("Montréal", "portal"), ("   ", "   "),
])
def test_flow_complete_json_and_constant_statements(corpus, city, source_type):
    measure_current_twice(corpus, "flow", dict(city=city, source_type=source_type),
                          flow_oracle(corpus, city, source_type), 1)
