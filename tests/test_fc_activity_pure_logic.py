from backend.fc_activity import derive_case_source_key, normalize_hf_case_record


def test_raw_parquet_row_becomes_one_stable_document_record():
    record = {
        "citation_fr": "2024 CF 17",
        "name_fr": "Exemple c. Canada",
        "url_fr": "https://example.test/decision",
        "document_date_fr": "2024-02-03T00:00:00Z",
        "unofficial_text_fr": "Motifs de la décision.",
    }

    normalized = normalize_hf_case_record(record)

    assert normalized["citation"] == "2024 CF 17"
    assert normalized["case_name"] == "Exemple c. Canada"
    assert normalized["date_filed"] == "2024-02-03"
    assert normalized["documents"][0]["docno"] == "raw-row"
    assert normalized["documents"][0]["recorded_entry"] == "Motifs de la décision."
    assert normalized["documents"][0]["entry_key"]
    assert normalized["documents"][0]["entry_hash"]


def test_invalid_or_empty_document_rows_are_ignored():
    normalized = normalize_hf_case_record(
        {
            "citation": "2024 FC 17",
            "documents": [
                None,
                "not a mapping",
                {},
                {"RE_NO": "2", "DOCNO": "A2", "RECORDED_ENTRY": "Order issued."},
            ],
        }
    )

    assert len(normalized["documents"]) == 1
    assert normalized["documents"][0]["docno"] == "A2"


def test_source_key_falls_back_to_canonicalized_raw_payload():
    first = {"unused": "value", "other": 2}
    reordered = {"other": 2, "unused": "value"}

    assert derive_case_source_key(first) == derive_case_source_key(reordered)
    assert derive_case_source_key(first) != derive_case_source_key({"unused": "different"})
