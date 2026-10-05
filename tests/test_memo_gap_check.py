from types import SimpleNamespace
import socket

import pytest
from sqlalchemy.dialects import postgresql

from backend import memo_gap_check as gaps


TAG = "issue:fairness"
TOP_TAGS = [{"tag": TAG, "memo_mentions": 2}]
NO_LABELS = {"ids": set(), "citations": set(), "titles": set()}


def cohort(outcomes, tags=None):
    tags = tags or [[TAG] for _ in outcomes]
    return [
        {"id": index, "government_outcome": outcome, "tags": tags[index]}
        for index, outcome in enumerate(outcomes)
    ]


def authority(identifier, citation=None):
    return {
        "id": identifier,
        "title": f"Party {identifier} v Canada",
        "citation": citation or f"2020 FC {identifier}",
        "secondary_citation": None,
    }


def edges(source_ids, target_ids):
    return [
        {"source_case_id": source_id, "target_case_id": target_id}
        for source_id in source_ids
        for target_id in target_ids
    ]


def test_rank_counts_distinct_tagged_decisions_and_excludes_cited_authorities():
    rows = cohort(["won", "lost", "won", "mixed"])
    links = edges([0, 1, 2], [20]) + edges([0, 1], [21, 22, 23, 24])
    labels = {
        "ids": {22},
        "citations": {"2020 FC 23"},
        "titles": set(),
    }
    result = gaps.rank_gap_suggestions(
        rows, links, [authority(24), authority(20), authority(23),
                      authority(21), authority(22)],
        labels, TOP_TAGS,
    )

    assert [item["id"] for item in result["missing"]] == [20, 21, 24]
    assert result["missing"][0]["citing_decisions"] == 3
    assert result["missing"][0]["cohort_denominator"] == 4
    assert result["missing"][0]["tags_matched"] == [{
        "tag": TAG,
        "citing_decisions": 3,
        "tag_denominator": 4,
        "outcomes": {"won": 2, "lost": 1, "mixed": 0, "unclassified": 0},
        "baseline_outcomes": {"won": 2, "lost": 1, "mixed": 1, "unclassified": 0},
    }]
    assert "issue:fairness (3/4)" in result["missing"][0]["why"]


@pytest.mark.parametrize(
    "n, expected_contrary, expected_hidden",
    [(7, False, 1), (8, True, 0)],
)
def test_contrary_rate_is_per_tag_and_hidden_below_eight(
    n, expected_contrary, expected_hidden,
):
    outcomes = ["lost"] * 4 + ["unclassified"] * 2 + ["won"] * 6
    rows = cohort(outcomes)
    result = gaps.rank_gap_suggestions(
        rows,
        edges(range(n), [20]),
        [authority(20)],
        NO_LABELS,
        TOP_TAGS,
    )

    assert bool(result["possibly_contrary"]) is expected_contrary
    assert result["contrary_hidden_below_threshold"] == expected_hidden
    if expected_contrary:
        comparison = result["possibly_contrary"][0]["contrary_tags"][0]
        assert comparison["authority"] == {
            "against_minister": 4,
            "unclassified": 2,
            "denominator": 8,
            "rate_percent": 50.0,
        }
        assert comparison["tag_baseline"] == {
            "against_minister": 4,
            "unclassified": 2,
            "denominator": 12,
            "rate_percent": 33.3,
        }


def test_ties_do_not_count_as_contrary_and_unclassified_stays_in_denominators():
    outcomes = ["lost"] * 4 + ["unclassified"] * 2 + ["won"] * 6
    rows = cohort(outcomes)
    result = gaps.rank_gap_suggestions(
        rows,
        edges(range(12), [20]),
        [authority(20)],
        NO_LABELS,
        TOP_TAGS,
    )

    assert result["possibly_contrary"] == []
    detail = result["missing"][0]["tags_matched"][0]
    assert detail["outcomes"]["unclassified"] == 2
    assert detail["baseline_outcomes"]["unclassified"] == 2


def test_empty_memo_returns_without_tagging_or_querying(monkeypatch):
    monkeypatch.setattr(
        gaps,
        "CoreLegalTaggerV3",
        lambda: (_ for _ in ()).throw(AssertionError("empty text must not be tagged")),
    )
    session = SimpleNamespace(
        execute=lambda *_: (_ for _ in ()).throw(
            AssertionError("empty text must not query")
        )
    )

    result = gaps.build_memo_gap_suggestions({"text": ""}, session)

    assert result["status"] == "empty_memo"
    assert result["missing"] == result["possibly_contrary"] == []
    assert result["disclaimer"] == "Suggestions for review, not legal advice"


def test_tagging_without_session_makes_no_network_calls(monkeypatch):
    def no_network(*args, **kwargs):
        raise AssertionError("network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", no_network)
    monkeypatch.setattr(socket.socket, "connect", no_network)
    monkeypatch.setattr(
        gaps,
        "CoreLegalTaggerV3",
        lambda: SimpleNamespace(tag_occurrences=lambda text: [
            SimpleNamespace(category="issue", value="fairness"),
        ]),
    )

    result = gaps.build_memo_gap_suggestions({"text": "procedural fairness"})

    assert result["status"] == "session_unavailable"
    assert result["top_tags"] == [{"tag": TAG, "memo_mentions": 1}]


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
    return str(statement.compile(
        dialect=postgresql.dialect(),
        compile_kwargs={"literal_binds": True},
    ))


def test_queries_use_top_tags_and_explicit_cohort_and_edge_caps(monkeypatch):
    tag_occurrences = [
        SimpleNamespace(category="issue", value="fairness"),
        SimpleNamespace(category="issue", value="fairness"),
        SimpleNamespace(category="remedy", value="review"),
    ]
    monkeypatch.setattr(
        gaps, "CoreLegalTaggerV3",
        lambda: SimpleNamespace(
            tag_occurrences=lambda text: tag_occurrences
        ),
    )
    session = Session(
        [{"id": 1, "government_outcome": "lost", "tag_0": True, "tag_1": True}],
        [{"source_case_id": 1, "target_case_id": 20}],
        [authority(20)],
    )

    result = gaps.build_memo_gap_suggestions({"text": "memo"}, session)

    cohort_sql, edge_sql, authority_sql = map(sql, session.statements)
    assert len(session.statements) == 3
    assert result["top_tags"] == [
        {"tag": "issue:fairness", "memo_mentions": 2},
        {"tag": "remedy:review", "memo_mentions": 1},
    ]
    assert "case_tags.category = 'issue' AND case_tags.value = 'fairness'" in cohort_sql
    assert "case_tags.category = 'remedy' AND case_tags.value = 'review'" in cohort_sql
    assert (
        f"case_tags.taxonomy_version = '{gaps.ACTIVE_TAG_TAXONOMY_VERSION}'"
        in cohort_sql
    )
    assert "LIMIT 501" in cohort_sql and "ORDER BY cases.id" in cohort_sql
    assert (
        "SELECT DISTINCT citations.source_case_id, citations.target_case_id"
        in edge_sql
    )
    assert "LIMIT 10001" in edge_sql
    assert "ORDER BY citations.source_case_id, citations.target_case_id" in edge_sql
    assert (
        "SELECT cases.id, cases.title, cases.citation, cases.secondary_citation"
        in authority_sql
    )
    for query in [cohort_sql, edge_sql, authority_sql]:
        assert "full_text" not in query and "source_html" not in query
