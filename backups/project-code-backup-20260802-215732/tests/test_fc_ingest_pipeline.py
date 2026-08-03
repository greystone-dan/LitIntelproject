from datetime import date

import pytest

from fc_ingest import ingest_pipeline
from fc_ingest.errors import HumanValidationRequired
from fc_ingest.ingest_pipeline import _normalize_fc_item_url, _split_by_months
from fc_ingest.item_scraper import parse_item_page


def test_split_by_months_keeps_december_bounded_to_calendar_month():
    windows = _split_by_months(date(2024, 12, 15), date(2025, 2, 10))

    assert windows == [
        (date(2024, 12, 15), date(2024, 12, 31)),
        (date(2025, 1, 1), date(2025, 1, 31)),
        (date(2025, 2, 1), date(2025, 2, 10)),
    ]


class FakeDb:
    def get_existing_fc_ids(self):
        return set()


def test_ingestion_continues_after_one_failed_month(monkeypatch):
    calls = []

    def fake_scrape(start_date, end_date, **kwargs):
        calls.append((start_date, end_date))
        if start_date.month == 1:
            raise RuntimeError("temporary source failure")
        return []

    monkeypatch.setattr(ingest_pipeline, "scrape_index_urls", fake_scrape)

    result = ingest_pipeline.run_full_ingestion(
        FakeDb(),
        start_date=date(2025, 1, 1),
        end_date=date(2025, 2, 28),
        monthly_windows=True,
    )

    assert result == []
    assert len(calls) == 2


def test_ingestion_fails_when_every_month_is_unavailable(monkeypatch):
    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_index_urls",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("unavailable")),
    )

    with pytest.raises(RuntimeError, match="All 2 Federal Court date windows failed"):
        ingest_pipeline.run_full_ingestion(
            FakeDb(),
            start_date=date(2025, 1, 1),
            end_date=date(2025, 2, 28),
            monthly_windows=True,
        )


def test_ingestion_stops_discovery_immediately_for_human_validation(monkeypatch):
    calls = []

    def fake_scrape(start_date, end_date, **kwargs):
        calls.append((start_date, end_date))
        raise HumanValidationRequired("captcha")

    monkeypatch.setattr(ingest_pipeline, "scrape_index_urls", fake_scrape)

    with pytest.raises(HumanValidationRequired, match="captcha"):
        ingest_pipeline.run_full_ingestion(
            FakeDb(),
            start_date=date(2025, 1, 1),
            end_date=date(2025, 2, 28),
            monthly_windows=True,
        )

    assert len(calls) == 1


def test_ingestion_resumes_pending_phase_two_before_discovery(monkeypatch):
    pending_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123/index.do"

    class PendingDb(FakeDb):
        def get_completed_fc_ids(self):
            return set()

        def get_pending_item_urls(self):
            return [pending_url]

    monkeypatch.setattr(
        ingest_pipeline,
        "_ingest_item_url",
        lambda *args, **kwargs: {"fc_id": "123", "item_url": pending_url},
    )
    monkeypatch.setattr(ingest_pipeline, "scrape_index_urls", lambda *args, **kwargs: [])

    result = ingest_pipeline.run_full_ingestion(
        PendingDb(),
        start_date=date(2025, 1, 1),
        end_date=date(2025, 1, 31),
        monthly_windows=True,
    )

    assert result == [{"fc_id": "123", "item_url": pending_url}]


def test_item_parser_uses_official_iframe_as_document_url():
    item_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123/index.do"
    html = '<html><body><iframe src="/fc-cf/decisions/en/item/123/index.do?iframe=true"></iframe></body></html>'

    item = parse_item_page(item_url, html)

    assert item.document_url == f"{item_url}?iframe=true"


def test_pending_phase_two_stops_immediately_for_human_validation(monkeypatch):
    pending_urls = [
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123/index.do",
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/456/index.do",
    ]
    calls = []

    class PendingDb(FakeDb):
        def get_completed_fc_ids(self):
            return set()

        def get_pending_item_urls(self):
            return pending_urls

    def blocked_ingestion(*args, **kwargs):
        calls.append(args[1])
        raise HumanValidationRequired("captcha")

    monkeypatch.setattr(ingest_pipeline, "_ingest_item_url", blocked_ingestion)

    with pytest.raises(HumanValidationRequired, match="captcha"):
        ingest_pipeline.run_full_ingestion(
            PendingDb(),
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 31),
            monthly_windows=True,
        )

    assert calls == [pending_urls[0]]


def test_normalize_fc_item_url_handles_item_document_and_pdf_urls():
    item = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/index.do"
    document = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/document.do"
    pdf = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/abc.pdf"

    assert _normalize_fc_item_url(item) == item
    assert _normalize_fc_item_url(document) == item
    assert _normalize_fc_item_url(pdf) == item
    assert _normalize_fc_item_url("https://example.com/item/350109/index.do") is None


def test_a2aj_direct_mode_uses_known_urls_and_skips_discovery(monkeypatch):
    urls = [
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/111/index.do",
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/222/index.do",
    ]
    ingested = []

    class PendingDb(FakeDb):
        def get_completed_fc_ids(self):
            return {"111"}

        def get_pending_item_urls(self):
            return []

    monkeypatch.setattr(ingest_pipeline, "load_a2aj_fc_item_urls", lambda limit=None: urls)

    def fake_ingest(*args, **kwargs):
        item_url = args[1]
        ingested.append(item_url)
        return {"fc_id": item_url.rstrip("/").split("/")[-2], "item_url": item_url}

    monkeypatch.setattr(ingest_pipeline, "_ingest_item_url", fake_ingest)
    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_index_urls",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("discovery should not run in direct mode")),
    )

    result = ingest_pipeline.run_full_ingestion(
        PendingDb(),
        a2aj_direct=True,
        a2aj_limit=10,
    )

    assert ingested == [urls[1]]
    assert result == [{"fc_id": "222", "item_url": urls[1]}]


def test_a2aj_direct_mode_respects_max_items(monkeypatch):
    urls = [
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/101/index.do",
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/102/index.do",
    ]
    ingested = []

    class PendingDb(FakeDb):
        def get_completed_fc_ids(self):
            return set()

        def get_pending_item_urls(self):
            return []

    monkeypatch.setattr(ingest_pipeline, "load_a2aj_fc_item_urls", lambda limit=None: urls)

    def fake_ingest(*args, **kwargs):
        item_url = args[1]
        ingested.append(item_url)
        return {"fc_id": item_url.rstrip("/").split("/")[-2], "item_url": item_url}

    monkeypatch.setattr(ingest_pipeline, "_ingest_item_url", fake_ingest)

    result = ingest_pipeline.run_full_ingestion(
        PendingDb(),
        a2aj_direct=True,
        max_items=1,
    )

    assert len(result) == 1
    assert len(ingested) == 1


def test_ingest_item_url_falls_back_to_pdf_when_document_is_blocked(monkeypatch):
    item_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/index.do"

    class FakeDb:
        def __init__(self):
            self.decision = None
            self.pdf = None

        def insert_fc_decision(self, record):
            self.decision = record

        def insert_fc_pdf(self, record):
            self.pdf = record

    fake_db = FakeDb()

    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_item_page",
        lambda *args, **kwargs: ingest_pipeline.ItemData(
            fc_id="350109",
            title="Doe v Canada",
            metadata={"source_url": item_url, "style of cause": "Doe v Canada", "neutral citation": "2025 FC 123"},
            document_url="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/document.do",
            pdf_url="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/decision.pdf",
        ),
    )
    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_document_page",
        lambda *args, **kwargs: (_ for _ in ()).throw(HumanValidationRequired("captcha")),
    )
    monkeypatch.setattr(
        ingest_pipeline,
        "download_pdf",
        lambda *args, **kwargs: (b"%PDF-1.7\n", "application/pdf"),
    )
    monkeypatch.setattr(ingest_pipeline.time, "sleep", lambda *_args, **_kwargs: None)

    out = ingest_pipeline._ingest_item_url(
        fake_db,
        item_url,
        timeout=5.0,
        retries=1,
        backoff_seconds=0.0,
        item_delay_seconds=0.0,
    )

    assert out["fc_id"] == "350109"
    assert out["metadata"]["document_blocked"] is True
    assert fake_db.decision is not None
    assert fake_db.pdf is not None
    assert fake_db.pdf["neutral_citation"] == "2025 FC 123"


def test_a2aj_direct_mode_skips_human_validation_and_continues(monkeypatch):
    urls = [
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/111/index.do",
        "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/222/index.do",
    ]

    class PendingDb(FakeDb):
        def get_completed_fc_ids(self):
            return set()

        def get_pending_item_urls(self):
            return []

    monkeypatch.setattr(ingest_pipeline, "load_a2aj_fc_item_urls", lambda limit=None: urls)

    def fake_ingest(*args, **kwargs):
        item_url = args[1]
        if item_url.endswith("/111/index.do"):
            raise HumanValidationRequired("captcha")
        return {"fc_id": "222", "item_url": item_url}

    monkeypatch.setattr(ingest_pipeline, "_ingest_item_url", fake_ingest)

    result = ingest_pipeline.run_full_ingestion(
        PendingDb(),
        a2aj_direct=True,
    )

    assert result == [{"fc_id": "222", "item_url": urls[1]}]


def test_ingest_item_uses_document_pdf_url_fallback(monkeypatch):
    item_url = "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/index.do"

    class FakeDb:
        def __init__(self):
            self.decision = None
            self.pdf = None

        def insert_fc_decision(self, record):
            self.decision = record

        def insert_fc_pdf(self, record):
            self.pdf = record

    fake_db = FakeDb()

    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_item_page",
        lambda *args, **kwargs: ingest_pipeline.ItemData(
            fc_id="350109",
            title="Doe v Canada",
            metadata={"source_url": item_url},
            document_url=f"{item_url}?iframe=true",
            pdf_url="",
        ),
    )
    monkeypatch.setattr(
        ingest_pipeline,
        "scrape_document_page",
        lambda *args, **kwargs: ingest_pipeline.DocumentData(
            title="Federal Court Decisions",
            full_text="Decision text",
            metadata={
                "pdf_url": "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/350109/1/document.do",
                "date": "2018-11-07",
                "neutral citation": "2018 FC 1123",
                "file numbers": "IMM-664-18",
                "style of cause": "Francis v. Canada (Citizenship and Immigration)",
            },
        ),
    )
    monkeypatch.setattr(
        ingest_pipeline,
        "download_pdf",
        lambda *args, **kwargs: (b"%PDF-1.7\n", "application/pdf"),
    )
    monkeypatch.setattr(ingest_pipeline.time, "sleep", lambda *_args, **_kwargs: None)

    out = ingest_pipeline._ingest_item_url(
        fake_db,
        item_url,
        timeout=5.0,
        retries=1,
        backoff_seconds=0.0,
        item_delay_seconds=0.0,
    )

    assert out["pdf_url"] == "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/350109/1/document.do"
    assert out["neutral_citation"] == "2018 FC 1123"
    assert out["docket"] == "IMM-664-18"
    assert fake_db.pdf is not None
    assert fake_db.pdf["neutral_citation"] == "2018 FC 1123"