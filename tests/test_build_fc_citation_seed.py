from __future__ import annotations

from scripts.build_fc_citation_seed import (
    InputEntry,
    _normalize_entry,
    build_seed,
)


def test_normalize_entry_accepts_fc_item_url() -> None:
    entry = InputEntry(
        raw_value="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123456/index.do",
        raw_url="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/123456/index.do",
        source_row=1,
    )
    accept, reject = _normalize_entry(entry)
    assert reject is None
    assert accept is not None
    assert accept.item_id == "123456"
    assert accept.normalized_url.endswith("/item/123456/index.do")


def test_normalize_entry_rejects_non_fc_domain() -> None:
    entry = InputEntry(
        raw_value="https://example.com/fc-cf/decisions/en/item/999/index.do",
        raw_url="https://example.com/fc-cf/decisions/en/item/999/index.do",
        source_row=1,
    )
    accept, reject = _normalize_entry(entry)
    assert accept is None
    assert reject is not None
    assert reject.reason == "not_supported_domain"


def test_normalize_entry_accepts_canlii_doc_url() -> None:
    entry = InputEntry(
        raw_value="https://www.canlii.org/en/ca/fc/doc/2024/2024fc123/2024fc123.html",
        raw_url="https://www.canlii.org/en/ca/fc/doc/2024/2024fc123/2024fc123.html?resultIndex=1",
        source_row=1,
    )
    accept, reject = _normalize_entry(entry)
    assert reject is None
    assert accept is not None
    assert accept.source_system == "canlii"
    assert accept.item_id == "2024fc123"
    assert accept.normalized_url == "https://www.canlii.org/en/ca/fc/doc/2024/2024fc123/2024fc123.html"


def test_build_seed_rejects_duplicate_item_id() -> None:
    entries = [
        InputEntry(
            raw_value="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/100/index.do",
            raw_url="https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/100/index.do",
            source_row=1,
        ),
        InputEntry(
            raw_value="https://decisions.fct-cf.gc.ca/fc-cf/decisions/fr/item/100/index.do",
            raw_url="https://decisions.fct-cf.gc.ca/fc-cf/decisions/fr/item/100/index.do",
            source_row=2,
        ),
    ]

    accepts, rejects, stats = build_seed(entries)
    assert len(accepts) == 1
    assert len(rejects) == 1
    assert rejects[0].reason in {"duplicate_item_id", "duplicate_normalized_url"}
    assert stats["accepted"] == 1
    assert stats["rejected"] == 1
