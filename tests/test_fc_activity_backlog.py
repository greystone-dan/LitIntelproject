"""Pure-logic tests for the overnight FC Activity backlog script (no database, no network)."""

from scripts.fc_activity_backlog import estimate_hours, imm_sort_key, run_order_key, read_done, stop_requested


def test_oldest_first_orders_by_year_then_number():
    imms = ["IMM-5-23", "IMM-900-19", "IMM-7-19", "IMM-1-05"]
    assert sorted(imms, key=imm_sort_key) == ["IMM-1-05", "IMM-7-19", "IMM-900-19", "IMM-5-23"]


def test_newest_first_reverses_order():
    imms = ["IMM-5-23", "IMM-900-19", "IMM-7-19"]
    assert sorted(imms, key=lambda i: imm_sort_key(i, True)) == ["IMM-5-23", "IMM-900-19", "IMM-7-19"]


def test_read_done_reads_first_column(tmp_path):
    path = tmp_path / "done.tsv"
    path.write_text("IMM-1-20\tok:3\nIMM-2-20\tmissing\n", encoding="utf-8")
    assert read_done(path) == {"IMM-1-20", "IMM-2-20"}
    assert read_done(tmp_path / "none.tsv") == set()


def test_stop_file(tmp_path):
    stop = tmp_path / "stop.txt"
    assert not stop_requested(stop)
    stop.write_text("x")
    assert stop_requested(stop)
    assert not stop_requested(None)


def test_estimate_hours():
    assert estimate_hours(900, 4.0) == 1.0


def test_run_order_never_fetched_first_then_newest_year():
    rows = [("IMM-1-22", "open_or_unknown"), ("IMM-9-26", "open_or_unknown"), ("IMM-5-19", "no_documents"),
            ("IMM-2-24", "not_in_activity"), ("IMM-3-26", "open_or_unknown")]
    ordered = [imm for imm, _ in sorted(rows, key=run_order_key)]
    assert ordered == ["IMM-2-24", "IMM-5-19", "IMM-9-26", "IMM-3-26", "IMM-1-22"]
