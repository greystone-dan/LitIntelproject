from backend.fc_activity import normalize_fc_activity, normalize_hf_case_record


def test_normalize_fc_activity_deduplicates_cases_and_documents():
    rows = [
        {
            "citation": "2023 FC 101",
            "name": "Example v. Minister",
            "year": 2023,
            "date_filed": "2023-02-01",
            "city_filed": "Toronto",
            "nature": "Judicial Review",
            "class": "Immigration",
            "track": "FC",
            "source_url": "https://example.test/case/1",
            "scraped_timestamp": "2023-02-10T12:00:00Z",
            "documents": [
                {"RE_NO": 1, "DOCNO": "A1", "DOC_DT": "2023-02-02", "RECORDED_ENTRY": "Application filed."},
                {"RE_NO": 2, "DOCNO": "A2", "DOC_DT": "2023-02-03", "RECORDED_ENTRY": "Order issued."},
            ],
        },
        {
            "citation": "2023 FC 101",
            "name": "Example v. Minister",
            "year": 2023,
            "date_filed": "2023-02-01",
            "city_filed": "Toronto",
            "nature": "Judicial Review",
            "class": "Immigration",
            "track": "FC",
            "source_url": "https://example.test/case/1",
            "scraped_timestamp": "2023-02-10T12:00:00Z",
            "documents": [
                {"RE_NO": 1, "DOCNO": "A1", "DOC_DT": "2023-02-02", "RECORDED_ENTRY": "Application filed."},
                {"RE_NO": 3, "DOCNO": "A3", "DOC_DT": "2023-02-04", "RECORDED_ENTRY": "Decision rendered."},
            ],
        },
    ]

    result = normalize_fc_activity(rows)

    assert len(result["cases"]) == 1
    assert len(result["documents"]) == 3
    assert result["duplicates_removed"] == 2
    assert result["cases"][0]["citation"] == "2023 FC 101"
    assert result["documents"][0]["case_key"] == result["cases"][0]["case_key"]


def test_normalize_hf_case_record_preserves_case_and_docket_details():
    record = {
        "citation": "IMM-1234-19",
        "year": 2019,
        "name": "A v Minister of Citizenship and Immigration",
        "date_filed": "2019-01-15",
        "city_filed": "Toronto",
        "nature": "Judicial review",
        "class": "Immigration",
        "track": "FC",
        "source_url": "https://example.test/case/123",
        "scraped_timestamp": "2024-01-01T12:00:00Z",
        "documents": [
            {
                "RE_NO": "1",
                "DOCNO": "A-001",
                "DOC_DT": "2019-01-16",
                "RECORDED_ENTRY": "Filed application for judicial review.",
            },
            {
                "RE_NO": "2",
                "DOCNO": "A-002",
                "DOC_DT": "2019-01-18",
                "RECORDED_ENTRY": "Response filed by the Minister.",
            },
        ],
    }

    canonical = normalize_hf_case_record(record)

    assert canonical["citation"] == "IMM-1234-19"
    assert canonical["case_name"] == "A v Minister of Citizenship and Immigration"
    assert canonical["source_url"] == "https://example.test/case/123"
    assert canonical["documents"][0]["doc_dt"] == "2019-01-16"
    assert canonical["documents"][0]["recorded_entry"] == "Filed application for judicial review."
    assert canonical["documents"][1]["recorded_entry"] == "Response filed by the Minister."


def test_normalize_hf_case_record_handles_missing_document_list():
    record = {
        "citation": "IMM-4321-20",
        "year": 2020,
        "name": "B v Minister",
    }

    canonical = normalize_hf_case_record(record)

    assert canonical["citation"] == "IMM-4321-20"
    assert canonical["documents"] == []
    assert canonical["case_name"] == "B v Minister"
    assert canonical["source_key"]


def test_normalize_hf_case_record_produces_stable_source_key_without_citation():
    record = {
        "name": "No Citation v. Minister",
        "source_url": "https://example.test/case/no-citation",
        "date_filed": "2024-01-15",
        "year": 2024,
        "documents": [{"RE_NO": "5", "DOCNO": "B-5", "DOC_DT": "2024-01-16", "RECORDED_ENTRY": "Filed."}],
    }

    canonical = normalize_hf_case_record(record)

    assert canonical["citation"] is None
    assert canonical["source_key"]
    assert canonical["documents"][0]["recorded_entry"] == "Filed."
    assert canonical["documents"][0]["entry_key"]


def test_normalize_hf_case_record_coerces_true_dataset_timestamps():
    record = {
        "citation": "2024 FC 100",
        "name": "Example v. Minister",
        "date_filed": "2024-01-15T00:00:00Z",
        "scraped_timestamp": "2024-01-16T12:30:45Z",
        "documents": [{"RE_NO": 1, "DOCNO": "X1", "DOC_DT": "2024-01-16T00:00:00Z", "RECORDED_ENTRY": "Application filed."}],
    }

    canonical = normalize_hf_case_record(record)

    assert canonical["date_filed"] == "2024-01-15T00:00:00Z"
    assert canonical["documents"][0]["doc_dt"] == "2024-01-16"
