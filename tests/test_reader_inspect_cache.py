from types import SimpleNamespace

from backend import reader_service


def test_discussion_unit_segmentation_is_cached_until_chunks_change(monkeypatch):
    calls = []
    monkeypatch.setattr(reader_service, "inspect_case", lambda *args: calls.append(args) or {"discussion_units": []})
    reader_service._INSPECT_CACHE.clear()
    chunks = [SimpleNamespace(id=1, text_hash="a", chunk_set="paragraph")]
    reader_service._cached_inspect_case(None, 7, chunks)
    reader_service._cached_inspect_case(None, 7, chunks)
    assert len(calls) == 1
    chunks[0].text_hash = "b"
    reader_service._cached_inspect_case(None, 7, chunks)
    assert len(calls) == 2
