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
    assert case_processing.STAGE_ORDER[3:] == ("case_citations", "statutes")
