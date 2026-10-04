from types import SimpleNamespace

import pytest
from sqlalchemy.dialects import postgresql

from backend import memo_authority_suggestions as suggestions


SIGNALS = {"tags": ["issue:fairness", "remedy:review"], "statutes": ["IRPA s. 112(2)(b.1)"]}
NO_LABELS = {"ids": set(), "citations": set(), "titles": set()}


def cohort(outcomes):
    return [
        {
            "id": index,
            "government_outcome": outcome,
            "shared_tags": [SIGNALS["tags"][index % 2]],
            "shared_statutes": SIGNALS["statutes"] if index == 0 else [],
        }
        for index, outcome in enumerate(outcomes)
    ]


def authority(identifier, **kwargs):
    return dict(id=identifier, title=f"Party {identifier} v Canada",
                citation=f"2020 FC {identifier}", secondary_citation=None, **kwargs)


def edges(sources, targets):
    return [
        {"source_case_id": source, "target_case_id": target}
        for source in sources for target in targets
    ]


def rank(rows, links, authorities, labels=NO_LABELS):
    return suggestions.rank_authorities(rows, links, authorities, labels, SIGNALS)


def test_duplicates_count_distinct_source_target_pairs_and_ignore_unknown_sources():
    rows = cohort(["lost"] * 5)
    links = edges(range(5), [20]) * 3 + edges([999], [20])
    result = rank(rows, links, [authority(20)])
    item = result["missing"][0]
    assert item["citing_decisions"] == item["outcomes"]["denominator"] == 5
    assert item["cohort_denominator"] == result["cohort_denominator"] == 5
    assert item["outcomes"]["lost"] == 5
    assert result["contrary"] == [item]
    assert result["coverage"]["citation_edges_checked"] == 5


@pytest.mark.parametrize(
    "outcomes, contrary, hidden",
    [
        (["lost"] * 4, False, 1),
        (["lost"] * 3 + ["mixed", None], True, 0),
        (["lost"] * 2 + ["won", "mixed", None], False, 0),
        (["lost"] * 3 + ["mixed", None, None], False, 0),
        (["lost"] * 4 + ["won", None], True, 0),
    ],
)
def test_exact_five_threshold_and_strict_majority_of_all_citing_decisions(
    outcomes, contrary, hidden,
):
    result = rank(cohort(outcomes), edges(range(len(outcomes)), [20]), [authority(20)])
    assert bool(result["contrary"]) is contrary
    assert result["contrary_hidden_below_threshold"] == hidden
    assert result["missing"][0]["outcomes"]["denominator"] == len(outcomes)


def test_unknown_stored_outcomes_are_unclassified_without_inference():
    rows = cohort(["won", "lost", "mixed", "Won", " lost ", "allowed", None, {}, []])
    for row in rows:
        row.update(outcome_status="lost", disposition="dismissed", title="Minister wins")
    item = rank(rows, edges(range(9), [20]), [authority(20)])["missing"][0]
    assert item["outcomes"] == {
        "won": 1, "lost": 1, "mixed": 1, "unclassified": 6, "denominator": 9,
    }


def test_explanations_union_only_signals_of_decisions_citing_authority():
    rows = cohort(["lost", "won", "won"])
    rows[0]["shared_tags"].append("authority:irrelevant")
    authorities = [authority(20), authority(21)]
    authorities[0]["shared_tags"] = ["authority:invented"]
    result = rank(rows, edges([0], [20]) + edges([1], [21]), authorities)
    assert result["missing"][0]["why"] == {
        "shared_tags": ["issue:fairness"], "shared_statutes": SIGNALS["statutes"],
    }
    assert result["missing"][1]["why"] == {
        "shared_tags": ["remedy:review"], "shared_statutes": [],
    }


def test_memo_resolved_id_text_secondary_fct_and_exact_full_title_exclusions():
    analysis = {"case_citations": [
        {"resolved_case_id": 20},
        {"normalized_reference": "2020 FC 21"},
        {"reference_text": "Some label, 2020 FCT 22 at para 9"},
        {"reference_text": "A reported identity"},
        {"reference_text": "  Named   Person v. Canada (Minister) "},
    ]}
    authorities = [authority(identifier) for identifier in range(20, 27)]
    authorities[2]["citation"] = " 2020   FC 22 "
    authorities[3]["secondary_citation"] = "a reported identity"
    authorities[4]["title"] = "Named Person v Canada (Minister)"
    authorities[5]["title"] = "Named Person v Canada (Other Minister)"
    authorities[6]["secondary_citation"] = "2020 FCT 21"
    result = rank(cohort(["lost"]), edges([0], range(20, 27)), authorities,
                  suggestions._memo_labels(analysis))
    assert [item["id"] for item in result["missing"]] == [25]


def test_no_fuzzy_party_fragment_or_partial_title_exclusion():
    labels = suggestions._memo_labels({"case_citations": [{"reference_text": "Party 20"}]})
    assert rank(cohort(["won"]), edges([0], [20]), [authority(20)], labels)["missing"]


def test_rank_deterministic_descending_numerator_then_id():
    rows = cohort(["won"] * 4)
    links = edges([0, 1], [25, 21]) + edges([0, 1, 2], [30]) + edges([0], [20])
    authorities = [authority(identifier) for identifier in [25, 30, 20, 21]]
    first = rank(rows, links, authorities)
    second = rank(rows[::-1], links[::-1], authorities[::-1])
    assert first == second
    assert [item["id"] for item in first["missing"]] == [30, 21, 25, 20]


def test_contrary_computed_before_missing_display_limit_and_totals():
    rows = cohort(["lost"] * 3 + ["won"] * 3)
    # Ten more frequent, non-contrary authorities hide the contrary candidates
    # from the missing display, but must not hide them from the contrary list.
    links = edges(range(6), range(20, 30)) + edges(range(5), range(40, 52))
    authorities = [authority(identifier) for identifier in list(range(20, 30)) + list(range(40, 52))]
    result = rank(rows, links, authorities)
    assert [item["id"] for item in result["missing"]] == list(range(20, 30))
    assert [item["id"] for item in result["contrary"]] == list(range(40, 50))
    assert result["coverage"]["missing_total"] == 22
    assert result["coverage"]["contrary_total"] == 12
    assert result["coverage"]["missing_truncated"]
    assert result["coverage"]["contrary_truncated"]


class Result:
    def __init__(self, rows):
        self.rows = rows

    def mappings(self):
        return iter(self.rows)


class Session:
    def __init__(self, *responses):
        self.responses = iter(responses)
        self.statements = []

    def execute(self, statement):
        self.statements.append(statement)
        return Result(next(self.responses))


def sql(statement):
    return str(statement.compile(dialect=postgresql.dialect(),
                                 compile_kwargs={"literal_binds": True}))


@pytest.fixture
def tagger(monkeypatch):
    monkeypatch.setattr(suggestions, "CoreLegalTaggerV3", lambda: SimpleNamespace(
        tag=lambda text: [
            SimpleNamespace(category="issue", value="fairness"),
            SimpleNamespace(category="remedy", value="review"),
            SimpleNamespace(category="issue", value="fairness"),
        ],
    ))


def analysis():
    return {
        "text": "invented memo",
        "statute_references": [{"normalized_reference": SIGNALS["statutes"][0]}],
    }


def selected(identifier=1, outcome="lost", **flags):
    return dict(id=identifier, government_outcome=outcome,
                signal_0=True, signal_1=False, signal_2=True, **flags)


def test_empty_and_no_session_are_complete_objects_without_queries(tagger):
    session = Session()
    empty = suggestions.build_authority_suggestions({}, session)
    unavailable = suggestions.build_authority_suggestions(analysis())
    assert empty["status"] == "no_signals"
    assert unavailable["status"] == "session_unavailable"
    assert session.statements == []
    for result in [empty, unavailable]:
        assert result["disclaimer"] == "Suggestions, not legal advice"
        assert result["missing"] == result["contrary"] == []
        assert result["cohort_denominator"] == result["contrary_hidden_below_threshold"] == 0
        assert "coverage" in result and "signals" in result


def test_empty_cohort_stops_after_one_query(tagger):
    session = Session([])
    result = suggestions.build_authority_suggestions(analysis(), session)
    assert result["status"] == "empty_cohort"
    assert len(session.statements) == 1
    assert result["cohort_denominator"] == 0


def test_cohort_sql_or_signals_same_row_and_taxonomy_exact_nested_statutes(tagger):
    session = Session([selected()], edges([1], [20]), [authority(20)])
    result = suggestions.build_authority_suggestions(analysis(), session)
    cohort_sql, edge_sql, authority_sql = map(sql, session.statements)
    assert " OR " in cohort_sql
    assert "case_tags.category = 'issue' AND case_tags.value = 'fairness'" in cohort_sql
    assert "case_tags.category = 'remedy' AND case_tags.value = 'review'" in cohort_sql
    assert f"case_tags.taxonomy_version = '{suggestions.ACTIVE_TAG_TAXONOMY_VERSION}'" in cohort_sql
    assert "statute_references.normalized_reference = 'IRPA s. 112(2)(b.1)'" in cohort_sql
    assert "provision_section" not in cohort_sql
    assert "LIMIT 501" in cohort_sql and "ORDER BY cases.id" in cohort_sql
    assert "SELECT DISTINCT citations.source_case_id, citations.target_case_id" in edge_sql
    assert "JOIN cases ON cases.id = citations.target_case_id" in edge_sql
    assert "LIMIT 10001" in edge_sql
    assert "ORDER BY citations.source_case_id, citations.target_case_id" in edge_sql
    assert "SELECT cases.id, cases.title, cases.citation, cases.secondary_citation" in authority_sql
    assert "government outcome" in cohort_sql
    for query in [cohort_sql, edge_sql, authority_sql]:
        assert "full_text" not in query and "outcome_status" not in query
        assert "summary" not in query and "source_html" not in query
    assert result["missing"][0]["why"] == {
        "shared_tags": ["issue:fairness"], "shared_statutes": SIGNALS["statutes"],
    }


@pytest.mark.parametrize("statute", ["IRPA s. 112(2)(b.1)", "IRPR s. 87(2)(a)"])
def test_statute_only_has_no_base_section_fallback(statute):
    session = Session([])
    result = suggestions.build_authority_suggestions(
        {"statute_references": [{"normalized_reference": statute}]}, session,
    )
    query = sql(session.statements[0])
    assert f"normalized_reference = '{statute}'" in query
    assert "case_tags" not in query and "pinpoint" not in query
    assert result["signals"] == {"tags": [], "statutes": [statute]}


def test_tag_only_uses_no_statute_query(tagger):
    session = Session([])
    suggestions.build_authority_suggestions({"text": "invented"}, session)
    assert "statute_references" not in sql(session.statements[0])


def test_real_deterministic_tagger_is_used_for_text(monkeypatch):
    # Supply a tiny whitelist in memory; no fixture files or external calls.
    from backend import legal_tagger_v3
    monkeypatch.setattr(legal_tagger_v3, "load_core_terms", lambda: {
        "issue": {"fairness": ("procedural fairness",)},
    })
    result = suggestions.build_authority_suggestions({"text": "Procedural fairness."})
    assert result["signals"]["tags"] == ["issue:fairness"]


def test_no_edges_skips_authority_query(tagger):
    session = Session([selected()], [])
    result = suggestions.build_authority_suggestions(analysis(), session)
    assert len(session.statements) == 2
    assert result["cohort_denominator"] == 1 and result["missing"] == []


def test_actual_cohort_cap_with_lookahead_is_explicit(tagger):
    session = Session([selected(index) for index in range(501)], [])
    result = suggestions.build_authority_suggestions(analysis(), session)
    assert result["status"] == "partial"
    assert result["cohort_denominator"] == 500
    assert result["coverage"]["partial"] and result["coverage"]["cohort_truncated"]
    assert not result["coverage"]["citation_edges_truncated"]
    assert 500 not in session.statements[1].compile().params["source_case_id_1"]


def test_actual_edge_cap_with_lookahead_is_explicit(tagger):
    links = edges([1], range(20, 10021))
    session = Session([selected()], links, [authority(20)])
    result = suggestions.build_authority_suggestions(analysis(), session)
    assert result["status"] == "partial"
    assert result["coverage"]["citation_edges_truncated"]
    assert result["coverage"]["citation_edges_checked"] == 10000
    target_ids = session.statements[2].compile().params["id_1"]
    assert len(target_ids) == 10000 and 10020 not in target_ids


def test_exact_caps_are_not_partial(tagger):
    session = Session([selected(index) for index in range(500)],
                      edges([1], range(20, 10020)), [])
    result = suggestions.build_authority_suggestions(analysis(), session)
    assert result["status"] == "complete"
    assert not result["coverage"]["partial"]
