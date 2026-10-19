from types import SimpleNamespace

from scripts.fill_fca_headline_outcomes import classify, summarise
from scripts.resplit_paragraph_chunks import carry_over_embeddings, locate_rows, row_for_paragraph, row_for_position, row_signature


def _row(label, start, end, text, text_hash="h"):
    return SimpleNamespace(id=None, chunk_label=label, paragraph_start=start, paragraph_end=end, text=text, text_hash=text_hash)


def test_locate_rows_and_position_lookup_follow_the_text():
    text = "intro\n[1] first\n[2] second"
    rows = [_row("intro", None, None, "intro"), _row("1", 1, 1, "[1] first"), _row("2", 2, 2, "[2] second")]
    located = locate_rows(text, rows)

    row, start = row_for_position(located, text.index("second"))

    assert row.chunk_label == "2"
    assert start == text.index("[2]")
    assert row_for_position(located, len(text) + 5) == (None, 0)


def test_row_for_paragraph_needs_exactly_one_match():
    rows = [_row("1", 1, 1, "a"), _row("2", 2, 3, "b"), _row("3", 3, 3, "c")]

    assert row_for_paragraph(rows, 1).chunk_label == "1"
    assert row_for_paragraph(rows, 2).chunk_label == "2"
    assert row_for_paragraph(rows, 3) is None
    assert row_for_paragraph(rows, None) is None


def test_row_signature_detects_identical_splits():
    a = [_row("1", 1, 1, "x", "h1")]
    assert row_signature(a) == row_signature([_row("1", 1, 1, "x", "h1")])
    assert row_signature(a) != row_signature([_row("1", 1, 1, "x", "h2")])


def test_fca_fill_only_touches_blank_headlines_with_clear_v2_results():
    assert classify("", "allowed") == "fill"
    assert classify(None, "mixed") == "fill"
    assert classify(None, "dismissed") == "fill"
    assert classify(None, "unclear") == "left_blank"
    assert classify(None, "procedural") == "left_blank"
    assert classify(None, None) == "left_blank"
    assert classify("dismissed", "allowed") == "kept_existing"


def test_fca_fill_summary_counts_before_and_after():
    rows = [(1, None, "allowed"), (2, "", "unclear"), (3, "dismissed", "allowed"), (4, None, "dismissed")]

    summary = summarise(rows)

    assert summary["blank_before"] == 3
    assert summary["blank_after"] == 1
    assert summary["fill"] == 2
    assert summary["kept_existing"] == 1
    assert summary["filled_by_value"] == {"allowed": 1, "dismissed": 1}


def _embedded(label, text, text_hash, embedding):
    row = _row(label, None, None, text, text_hash)
    row.embedding = embedding
    row.embedding_model = "m" if embedding is not None else None
    return row


def test_embeddings_carry_to_new_rows_with_identical_text_only():
    old = [_embedded("1", "same", "a", [0.1]), _embedded("2", "old split", "b", [0.2]), _embedded("3", "plain", "c", None)]
    new = [_embedded("1", "same", "a", None), _embedded("2", "new split", "d", None)]

    carried, lost = carry_over_embeddings(old, new)

    assert (carried, lost) == (1, 1)
    assert new[0].embedding == [0.1]
    assert new[0].embedding_model == "m"
    assert new[1].embedding is None


class _Result:
    def __init__(self, value=None, rows=()):
        self.value, self.rows = value, rows

    def scalar(self):
        return self.value

    def __iter__(self):
        return iter(self.rows)


class _RecordingSession:
    """Stands in for a SQLAlchemy session: records every statement and answers the few reads apply_case makes."""

    def __init__(self, index_exists=True, indexed=(1, 2)):
        self.index_exists, self.indexed, self.statements, self.added = index_exists, list(indexed), [], []

    def scalars(self, _statement):
        return []

    def add_all(self, rows):
        self.added.extend(rows)

    def flush(self):
        pass

    def execute(self, statement, params=None):
        sql = str(statement)
        self.statements.append((sql, params))
        if "to_regclass" in sql:
            return _Result(self.index_exists)
        if "SELECT chunk_id FROM paragraph_search" in sql:
            return _Result(rows=[(chunk_id,) for chunk_id in self.indexed])
        return _Result()


def _full_row(row_id, label, text):
    return SimpleNamespace(
        id=row_id, case_id=7, chunk_set="paragraph", chunk_index=0, chunk_label=label, paragraph_start=None,
        paragraph_end=None, text=text, text_hash=text, token_estimate=1, embedding_model=None, embedding=None,
    )


def test_apply_case_keeps_the_paragraph_search_index_in_step(tmp_path):
    from scripts.resplit_paragraph_chunks import apply_case

    session = _RecordingSession()
    case = SimpleNamespace(id=7, full_text="[1] a [2] b", summary=None)
    plan = {"old_rows": [_full_row(1, "1", "[1] a"), _full_row(2, "2", "[2] b")], "new_rows": [_full_row(10, "1", "[1] a")]}

    apply_case(session, case, plan, tmp_path)

    sql = [statement for statement, _ in session.statements]
    delete_at = next(i for i, text in enumerate(sql) if "DELETE FROM paragraph_search" in text)
    insert_at = next(i for i, text in enumerate(sql) if "INSERT INTO paragraph_search" in text)
    assert delete_at < insert_at
    assert session.statements[delete_at][1] == {"case_id": 7}
    assert session.statements[insert_at][1] == {"ids": [10]}
    undo = __import__("json").loads((tmp_path / "case_7.json").read_text(encoding="utf-8"))
    assert undo["search"] == [1, 2]


def test_apply_case_skips_the_index_when_the_table_is_missing(tmp_path):
    from scripts.resplit_paragraph_chunks import apply_case

    session = _RecordingSession(index_exists=False)
    case = SimpleNamespace(id=7, full_text="[1] a", summary=None)
    plan = {"old_rows": [_full_row(1, "1", "[1] a")], "new_rows": [_full_row(10, "1", "[1] a")]}

    apply_case(session, case, plan, tmp_path)

    assert not any("paragraph_search" in statement and "to_regclass" not in statement for statement, _ in session.statements)


def test_renumbered_paragraphs_counts_numbers_that_point_at_different_text():
    from scripts.resplit_paragraph_chunks import renumbered_paragraphs

    old = [_row("1", 1, 1, "[1] First"), _row("2", 2, 2, "[2] Second\nIssue Estoppel"), _row("3", 3, 3, "[3] Third")]
    same_numbers = [_row("1", 1, 1, "[1] First"), _row("2", 2, 2, "[2] Second"), _row("heading", None, None, "Issue Estoppel"), _row("3", 3, 3, "[3] Third")]
    shifted = [_row("1", 1, 1, "[1] First"), _row("2", 2, 2, "[2] Third"), _row("3", 3, 3, "[3] Fourth")]

    assert renumbered_paragraphs(old, same_numbers) == 0
    assert renumbered_paragraphs(old, shifted) == 2


def test_renumbered_paragraphs_ignores_a_heading_glued_before_the_marker():
    from scripts.resplit_paragraph_chunks import renumbered_paragraphs

    old = [_row("1", 1, 1, "I. Overview [1] The Applicant is a citizen"), _row("2", 2, 2, "[2] Second")]
    new = [_row("heading", None, None, "I. Overview"), _row("1", 1, 1, "[1] The Applicant is a citizen"), _row("2", 2, 2, "[2] Second")]

    assert renumbered_paragraphs(old, new) == 0
