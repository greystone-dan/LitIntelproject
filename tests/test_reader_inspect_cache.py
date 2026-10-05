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


def test_reader_page_loads_evidence_after_the_text():
    from backend.pages.data_explorer import data_explorer_page_html

    html = data_explorer_page_html()
    assert "/reader-data?evidence=0" in html and "/evidence-summary" in html


def test_pinpoint_chunk_matching_stays_linear_for_a_heavily_cited_case():
    import time

    chunks = [
        SimpleNamespace(case_id=case_id, paragraph_start=n * 2 + 1, paragraph_end=n * 2 + 2, text=f"{case_id}:{n}")
        for case_id in range(400)
        for n in range(100)
    ]
    pinpoints = {case_id: list(range(1, 200, 3)) for case_id in range(400)}
    started = time.perf_counter()
    matched = reader_service._match_pinpoint_chunks(pinpoints, chunks)
    elapsed = time.perf_counter() - started
    assert len(matched) == 400 * len(pinpoints[0])
    assert matched[(5, 1)] == "5:0"
    assert elapsed < 2.0


def test_located_layer_mapping_matches_per_call_mapping_and_is_fast():
    import time

    from backend.document_structure import locate_chunk_layers, map_span_to_chunk_layers, map_span_to_located_layers

    paragraphs = [f"[{n}] " + ("word " * 40) + f"end{n}." for n in range(1, 301)]
    case_text = "\n".join(paragraphs)
    chunks = [SimpleNamespace(id=1, chunk_set="full_case", chunk_index=0, text=case_text)]
    chunks += [SimpleNamespace(id=100 + n, chunk_set="paragraph", chunk_index=n, text=text) for n, text in enumerate(paragraphs)]
    located = locate_chunk_layers(case_text, chunks)
    spans = [(start, start + 6) for start in range(0, len(case_text) - 6, 37)]
    started = time.perf_counter()
    fast = [map_span_to_located_layers(len(case_text), a, b, located) for a, b in spans]
    elapsed = time.perf_counter() - started
    assert fast == [map_span_to_chunk_layers(case_text, a, b, chunks) for a, b in spans[:60]] + fast[60:]
    assert elapsed < 3.0
