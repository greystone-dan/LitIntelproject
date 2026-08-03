import json
import sqlite3

import importlib


def test_insert_case_preserves_full_payload_and_metadata(tmp_path, monkeypatch):
    db_path = tmp_path / "canlaw.db"
    monkeypatch.setenv("CANLAW_DB_PATH", str(db_path))

    import canlaw.config as config
    import canlaw.db as db

    importlib.reload(config)
    importlib.reload(db)

    db.init_db()

    row = {
        "dataset": "FC",
        "citation_en": "FC 123",
        "citation_fr": "FC 123 FR",
        "cases_cited_en": ["A v B", "C v D"],
        "cases_cited_fr": ["A c B"],
        "cases_citing_en": ["E v F"],
        "custom_meta": {"judge": "Smith", "year": 2024},
        "notes": "rich payload",
    }

    with sqlite3.connect(db_path) as conn:
        case_id = db.insert_case(conn, row, "FC")
        stored = conn.execute(
            "SELECT raw_payload, metadata_json, cases_cited, cases_citing FROM cases WHERE id = ?",
            (case_id,),
        ).fetchone()

    assert json.loads(stored[0])["custom_meta"]["judge"] == "Smith"
    assert json.loads(stored[1])["custom_meta"]["judge"] == "Smith"
    assert json.loads(stored[0])["notes"] == "rich payload"
    assert json.loads(stored[2]) == ["A v B", "C v D", "A c B"]
    assert json.loads(stored[3]) == ["E v F"]


def test_insert_case_is_idempotent_by_source_record(tmp_path, monkeypatch):
    db_path = tmp_path / "canlaw.db"
    monkeypatch.setenv("CANLAW_DB_PATH", str(db_path))

    import canlaw.config as config
    import canlaw.db as db

    importlib.reload(config)
    importlib.reload(db)
    db.init_db()

    row = {
        "citation_en": "2024 FC 123",
        "url_en": "https://example.test/case/123",
        "unofficial_text_en": "Reasons for decision.",
    }

    with db.get_conn() as conn:
        first_id = db.insert_case(conn, row, "FC")
        second_id = db.insert_case(conn, row, "FC")
        count = conn.execute("SELECT COUNT(*) FROM cases").fetchone()[0]

    assert second_id == first_id
    assert count == 1


def test_insert_case_recognizes_rows_created_before_source_keys(tmp_path, monkeypatch):
    db_path = tmp_path / "canlaw.db"
    monkeypatch.setenv("CANLAW_DB_PATH", str(db_path))

    import canlaw.config as config
    import canlaw.db as db

    importlib.reload(config)
    importlib.reload(db)
    db.init_db()
    row = {
        "citation_en": "2024 FC 456",
        "url_en": "https://example.test/case/456",
        "cases_cited_en": ["2020 SCC 1"],
    }

    with db.get_conn() as conn:
        case_id = db.insert_case(conn, row, "FC")
        conn.execute("UPDATE cases SET source_key = NULL, cases_cited = '[]' WHERE id = ?", (case_id,))
        rerun_id = db.insert_case(conn, row, "FC")
        stored = conn.execute(
            "SELECT source_key, cases_cited FROM cases WHERE id = ?", (case_id,)
        ).fetchone()

    assert rerun_id == case_id
    assert stored[0]
    assert json.loads(stored[1]) == ["2020 SCC 1"]


def test_repair_case_metadata_backfills_legacy_rows(tmp_path, monkeypatch):
    db_path = tmp_path / "canlaw.db"
    monkeypatch.setenv("CANLAW_DB_PATH", str(db_path))

    import canlaw.config as config
    import canlaw.db as db

    importlib.reload(config)
    importlib.reload(db)
    db.init_db()
    row = {
        "citation_en": "2024 SCC 10",
        "cases_cited_en": ["2020 SCC 1"],
        "cases_citing_fr": ["2025 CSC 2"],
    }
    with db.get_conn() as conn:
        case_id = db.insert_case(conn, row, "SCC")
        conn.execute(
            "UPDATE cases SET source_key = NULL, cases_cited = '[]', cases_citing = '[]' WHERE id = ?",
            (case_id,),
        )

    assert db.repair_case_metadata(batch_size=1) == 1
    with db.get_conn() as conn:
        stored = conn.execute(
            "SELECT source_key, cases_cited, cases_citing FROM cases WHERE id = ?",
            (case_id,),
        ).fetchone()

    assert stored[0]
    assert json.loads(stored[1]) == ["2020 SCC 1"]
    assert json.loads(stored[2]) == ["2025 CSC 2"]
