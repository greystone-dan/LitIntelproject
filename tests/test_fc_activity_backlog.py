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


def test_shards_partition_the_list_without_overlap():
    from scripts.fc_activity_backlog import in_shard, parse_shard

    imms = [f"IMM-{n}-25" for n in range(1, 400)]
    first = {i for i in imms if in_shard(i, 1, 2)}
    second = {i for i in imms if in_shard(i, 2, 2)}
    assert first | second == set(imms) and not (first & second)
    assert parse_shard(None) == (1, 1) and parse_shard("2/3") == (2, 3)


def test_bad_shard_rejected():
    import pytest

    from scripts.fc_activity_backlog import parse_shard

    for bad in ("0/2", "3/2", "x", "1-2"):
        with pytest.raises(ValueError):
            parse_shard(bad)


def test_laptop_runner_fetch_and_resume(tmp_path, monkeypatch):
    import json
    import sys

    from scripts import fc_activity_laptop as lap

    body = json.dumps({"data": [{"DOC_DT": "2024-03-01", "RECORDED_ENTRY": "Notice of application", "RE_NO": "1", "DOCNO": "1",
                                 "STYLE_OF_CAUSE": "A v. B"}]})

    def fake_get(url, retries=3):
        if "IMM-3-24" in url:
            return json.dumps({"data": []})
        return body

    monkeypatch.setattr(lap, "http_get", fake_get)
    monkeypatch.setattr(lap.time, "sleep", lambda *_: None)
    lst = tmp_path / "list.txt"
    lst.write_text("IMM-1-24\tnot_in_activity\nIMM-2-24\nIMM-3-24\nbad\n", encoding="utf-8")
    data = tmp_path / "d"
    monkeypatch.setattr(sys, "argv", ["x", "--list", str(lst), "--data-dir", str(data)])
    assert lap.main() == 0
    rows = [json.loads(line) for line in (data / "results_run.jsonl").read_text().splitlines()]
    assert [r["imm"] for r in rows] == ["IMM-1-24", "IMM-2-24"]  # IMM-3-24 has no file: done but not saved
    assert rows[0]["result"]["entries_json"][0]["entry"] == "Notice of application"
    assert rows[0]["result"]["style_of_cause"] == "A v. B"
    assert (data / "done_run.txt").read_text().split() == ["IMM-1-24", "IMM-2-24", "IMM-3-24"]
    assert lap.main() == 0  # resume: nothing left, nothing duplicated
    assert len((data / "results_run.jsonl").read_text().splitlines()) == 2


def test_laptop_runner_stops_on_block(tmp_path, monkeypatch):
    import sys

    from scripts import fc_activity_laptop as lap

    def blocked(url, retries=3):
        raise lap.Blocked("HTTP 429")

    monkeypatch.setattr(lap, "http_get", blocked)
    monkeypatch.setattr(lap.time, "sleep", lambda *_: None)
    lst = tmp_path / "list.txt"
    lst.write_text("IMM-1-24\nIMM-2-24\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["x", "--list", str(lst), "--data-dir", str(tmp_path / "d")])
    assert lap.main() == 2
    assert not (tmp_path / "d" / "done_run.txt").read_text().strip()


def test_laptop_stop_file(tmp_path, monkeypatch):
    import sys

    from scripts import fc_activity_laptop as lap

    (tmp_path / "d").mkdir()
    (tmp_path / "d" / "stop.txt").write_text("")
    lst = tmp_path / "list.txt"
    lst.write_text("IMM-1-24\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["x", "--list", str(lst), "--data-dir", str(tmp_path / "d")])
    assert lap.main() == 1
