from types import SimpleNamespace

from scripts import curate_a2aj_immigration_cases as immigration_curator


class FakeBatch:
    def __init__(self, rows):
        self._rows = rows

    def to_pylist(self):
        return self._rows


class FakeParquetFile:
    def __init__(self, rows):
        self.rows = rows

    def iter_batches(self, batch_size=1024, columns=None):
        yield FakeBatch(self.rows)


def test_score_record_detects_immigration_signals():
    record = {
        "name_en": "Example v. Canada",
        "citation_en": "2024 FC 100",
        "unofficial_text_en": "This judicial review concerns IRCC and a removal order with non-refoulement risk.",
    }

    scores = immigration_curator.score_record(record)

    assert scores["agency_review"] > 0
    assert scores["removal_detention"] > 0
    assert scores["refugee_protection"] > 0
    assert immigration_curator.bucket_priority(scores) in {
        "refugee_protection",
        "removal_detention",
        "agency_review",
    }
    assert immigration_curator.immigration_anchor_score(record) > 0


def test_select_candidates_balances_buckets(monkeypatch):
    rows = [
        {
            "dataset": "FC",
            "citation_en": "2024 FC 111",
            "name_en": "Refugee Case",
            "document_date_en": "2024-01-01",
            "url_en": "https://example.com/1",
            "scraped_timestamp_en": "2024-01-02T00:00:00Z",
            "unofficial_text_en": "non-refoulement refugee protection claim",
        },
        {
            "dataset": "FC",
            "citation_en": "2024 FC 222",
            "name_en": "Detention Case",
            "document_date_en": "2024-02-01",
            "url_en": "https://example.com/2",
            "scraped_timestamp_en": "2024-02-02T00:00:00Z",
            "unofficial_text_en": "detention review and removal order and CBSA",
        },
        {
            "dataset": "FC",
            "citation_en": "2024 FC 333",
            "name_en": "Family Case",
            "document_date_en": "2024-03-01",
            "url_en": "https://example.com/3",
            "scraped_timestamp_en": "2024-03-02T00:00:00Z",
            "unofficial_text_en": "spousal sponsorship and humanitarian and compassionate relief",
        },
    ]

    monkeypatch.setattr(immigration_curator.pq, "ParquetFile", lambda path: FakeParquetFile(rows))

    selected = immigration_curator.select_candidates(immigration_curator.SOURCE, limit=2, per_bucket=1)

    assert len(selected) == 2
    assert {row["_bucket"] for row in selected} <= {
        "refugee_protection",
        "removal_detention",
        "family_status",
        "agency_review",
        "review_procedure",
    }
    assert selected[0]["_score"] > 0


def test_select_candidates_skips_non_immigration_noise(monkeypatch):
    rows = [
        {
            "dataset": "FC",
            "citation_en": "2024 FC 999",
            "name_en": "Generic Procedure Case",
            "document_date_en": "2024-04-01",
            "url_en": "https://example.com/9",
            "scraped_timestamp_en": "2024-04-02T00:00:00Z",
            "unofficial_text_en": "This case discusses procedural fairness and reasonableness in the abstract.",
        },
    ]

    monkeypatch.setattr(immigration_curator.pq, "ParquetFile", lambda path: FakeParquetFile(rows))

    selected = immigration_curator.select_candidates(immigration_curator.SOURCE, limit=5, per_bucket=2)

    assert selected == []


def test_select_candidates_applies_year_range(monkeypatch):
    rows = [
        {
            "dataset": "FC",
            "citation_en": "2019 FC 1",
            "name_en": "Older Immigration Case",
            "document_date_en": "2019-02-01",
            "url_en": "https://example.com/old",
            "scraped_timestamp_en": "2019-02-02T00:00:00Z",
            "unofficial_text_en": "IRCC review and removal order.",
        },
        {
            "dataset": "FC",
            "citation_en": "2022 FC 2",
            "name_en": "Recent Immigration Case",
            "document_date_en": "2022-03-01",
            "url_en": "https://example.com/new",
            "scraped_timestamp_en": "2022-03-02T00:00:00Z",
            "unofficial_text_en": "IRCC review and removal order.",
        },
    ]

    monkeypatch.setattr(immigration_curator.pq, "ParquetFile", lambda path: FakeParquetFile(rows))

    selected = immigration_curator.select_candidates(
        immigration_curator.SOURCE,
        limit=5,
        per_bucket=5,
        year_from=2021,
        year_to=2023,
    )

    assert len(selected) == 1
    assert selected[0]["citation_en"] == "2022 FC 2"


def test_select_candidates_respects_max_per_party(monkeypatch):
    rows = [
        {
            "dataset": "FC",
            "citation_en": "2020 FC 1",
            "name_en": "Alpha v. Canada (Citizenship and Immigration)",
            "document_date_en": "2020-01-01",
            "url_en": "https://example.com/1",
            "scraped_timestamp_en": "2020-01-02T00:00:00Z",
            "unofficial_text_en": "IRCC removal order and refugee claim.",
        },
        {
            "dataset": "FC",
            "citation_en": "2020 FC 2",
            "name_en": "Beta v. Canada (Citizenship and Immigration)",
            "document_date_en": "2020-02-01",
            "url_en": "https://example.com/2",
            "scraped_timestamp_en": "2020-02-02T00:00:00Z",
            "unofficial_text_en": "IRCC removal order and refugee claim.",
        },
        {
            "dataset": "FC",
            "citation_en": "2020 FC 3",
            "name_en": "Gamma v. Canada (Public Safety and Emergency Preparedness)",
            "document_date_en": "2020-03-01",
            "url_en": "https://example.com/3",
            "scraped_timestamp_en": "2020-03-02T00:00:00Z",
            "unofficial_text_en": "CBSA detention review and removal order.",
        },
    ]

    monkeypatch.setattr(immigration_curator.pq, "ParquetFile", lambda path: FakeParquetFile(rows))

    selected = immigration_curator.select_candidates(
        immigration_curator.SOURCE,
        limit=3,
        per_bucket=3,
        max_per_party=1,
    )

    party_patterns = [item["_party_pattern"] for item in selected]
    assert len(selected) == 2
    assert party_patterns.count("citizenship and immigration") == 1
    assert party_patterns.count("public safety and emergency preparedness") == 1
