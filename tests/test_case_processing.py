from types import SimpleNamespace

from backend import case_processing


class FakeSession:
    def __init__(self):
        self.added = []

    def execute(self, statement):
        return None

    def add_all(self, rows):
        self.added.extend(rows)


def test_full_case_stage_creates_one_complete_chunk():
    session = FakeSession()
    case = SimpleNamespace(id=7, full_text="Full case text", summary="Fallback summary")

    count = case_processing._run_full_case_chunk_layer(session, case)

    assert count == 1
    assert len(session.added) == 1
    assert session.added[0].chunk_set == "full_case"
    assert session.added[0].chunk_label == "Full case"
    assert session.added[0].text == "Full case text"
    assert session.added[0].paragraph_start is None
    assert session.added[0].paragraph_end is None


def test_stage_order_exposes_chunking_before_metadata_and_citation_layers():
    assert case_processing.STAGE_ORDER[:3] == ("full_case", "heading_chunks", "metadata")
    assert case_processing.STAGE_ORDER[3:] == ("case_citations", "statutes", "tags_v3")


def test_v3_tag_stage_replaces_only_v3_rows_and_records_occurrence_count(monkeypatch):
    class TagSession(FakeSession):
        def __init__(self):
            super().__init__()
            self.statuses = []

        def add(self, row):
            self.statuses.append(row)

    rows = [
        {
            "category": "agency",
            "value": "ircc",
            "score": 1.0,
            "evidence": "IRCC",
            "offset_start": 0,
            "offset_end": 4,
            "rule_id": "agency.ircc",
            "language": "unknown",
            "evidence_role": "mention",
            "chunk_id": None,
            "source": "core_whitelist",
            "taxonomy_version": "ca_legal_v3_core",
        },
        {
            "category": "agency",
            "value": "ircc",
            "score": 1.0,
            "evidence": "IRCC",
            "offset_start": 10,
            "offset_end": 14,
            "rule_id": "agency.ircc",
            "language": "unknown",
            "evidence_role": "mention",
            "chunk_id": None,
            "source": "core_whitelist",
            "taxonomy_version": "ca_legal_v3_core",
        },
    ]
    monkeypatch.setattr(case_processing, "build_case_tag_rows", lambda text: rows)
    session = TagSession()

    count = case_processing._run_v3_tag_layer(
        session,
        SimpleNamespace(id=7, full_text="IRCC and IRCC", summary=""),
    )

    assert count == 2
    assert len(session.added) == 2
    assert session.statuses[-1].tags_count == 2
