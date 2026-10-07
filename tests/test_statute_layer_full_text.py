from types import SimpleNamespace

from backend import case_processing


def test_statute_layer_extracts_from_full_text_not_chunks(monkeypatch):
    seen = {}

    def fake_rebuild(session, case, chunks):
        seen["chunks"] = chunks
        return 7

    monkeypatch.setattr(case_processing, "rebuild_statute_references_for_case", fake_rebuild)
    assert case_processing._run_statute_layer(object(), SimpleNamespace(id=1)) == 7
    assert seen["chunks"] == []
