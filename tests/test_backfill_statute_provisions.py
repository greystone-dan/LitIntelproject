from scripts.backfill_statute_provisions import derive_provision_fields


def test_derive_fields_from_pinpoint():
    assert derive_provision_fields(1, "36(2)(b)") == {
        "id": 1, "section": "36", "subsection": "2", "paragraph": "b", "depth": 2, "is_list": False,
    }
    assert derive_provision_fields(2, "98.03(4)")["section"] == "98.03"
    assert derive_provision_fields(3, "96")["subsection"] is None


def test_unusable_pinpoint_is_skipped_and_lists_are_flagged():
    assert derive_provision_fields(4, "abc") is None
    assert derive_provision_fields(5, "96-97")["is_list"] is True
