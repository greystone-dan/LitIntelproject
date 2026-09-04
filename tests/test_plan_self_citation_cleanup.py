from scripts import plan_self_citation_cleanup


class FakeResult:
    def mappings(self):
        return self

    def all(self):
        return [
            {
                "id": 1,
                "source_case_id": 7,
                "citation_text": "2024 FC 7",
                "normalized_citation": "2024 FC 7",
                "offset_start": 100,
                "offset_end": 109,
                "source_title": "Example v. Canada",
                "source_citation": "2024 FC 7",
                "full_text": "Neutral citation 2024 FC 7",
            }
        ]


class FakeSession:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def execute(self, statement, params):
        return FakeResult()


def test_cleanup_plan_is_explicitly_non_destructive(monkeypatch):
    monkeypatch.setattr(plan_self_citation_cleanup, "SessionLocal", FakeSession)

    report = plan_self_citation_cleanup.plan_cleanup(5000)

    assert report["sample_limit"] == 1000
    assert report["write_performed"] is False
    assert report["cleanup_authorized"] is False
    assert report["classification_counts"] == {"source_header_citation": 1}
    assert report["candidates"][0]["review_priority"] == "first"
