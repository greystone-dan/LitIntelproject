from hashlib import sha256
from types import SimpleNamespace

import pytest

from scripts.chunk_cases import build_case_chunks, chunk_pending_cases, split_text


class ScalarRows:
    def __init__(self, rows):
        self.rows = rows

    def all(self):
        return self.rows


class FakeSession:
    def __init__(self, batches):
        self.batches = iter(batches)
        self.added = []
        self.commits = 0

    def scalars(self, statement):
        return ScalarRows(next(self.batches))

    def add_all(self, rows):
        self.added.extend(rows)

    def commit(self):
        self.commits += 1


def test_split_text_uses_expected_overlap():
    chunks = split_text("abcdefghij", chunk_chars=6, overlap_chars=2)

    assert chunks == ["abcdef", "efghij"]


def test_split_text_rejects_nonadvancing_overlap():
    with pytest.raises(ValueError, match="overlap_chars"):
        split_text("text", chunk_chars=4, overlap_chars=4)


def test_build_case_chunks_falls_back_to_summary_and_hashes_text():
    case = SimpleNamespace(id=12, full_text="  ", summary="summary text")

    rows = build_case_chunks(case)

    assert len(rows) == 1
    assert rows[0].case_id == 12
    assert rows[0].chunk_index == 0
    assert rows[0].text == "summary text"
    assert rows[0].text_hash == sha256(b"summary text").hexdigest()
    assert rows[0].token_estimate == 3


def test_chunk_pending_cases_commits_each_case_batch():
    cases = [
        SimpleNamespace(id=4, full_text="case four", summary=None),
        SimpleNamespace(id=9, full_text="case nine", summary=None),
    ]
    db = FakeSession([cases, []])

    cases_chunked, chunks_created = chunk_pending_cases(db, batch_size=2)

    assert cases_chunked == 2
    assert chunks_created == 2
    assert [row.case_id for row in db.added] == [4, 9]
    assert db.commits == 1