import importlib
import sqlite3


def test_ingest_courts_to_db_inserts_rows_for_multiple_courts(tmp_path, monkeypatch):
    db_path = tmp_path / "canlaw.db"
    monkeypatch.setenv("CANLAW_DB_PATH", str(db_path))

    import canlaw.config as config
    import canlaw.db as db
    import canlaw.hf_loader as loader

    importlib.reload(config)
    importlib.reload(db)
    importlib.reload(loader)

    db.init_db()

    fake_rows = {
        "FC": [{"citation_en": "FC 1"}],
        "RPD": [{"citation_en": "RPD 1"}],
        "FCA": [{"citation_en": "FCA 1"}],
        "SCC": [{"citation_en": "SCC 1"}],
    }

    def fake_load_court_dataset(court):
        return fake_rows[court]

    monkeypatch.setattr(loader, "load_court_dataset", fake_load_court_dataset)

    loader.ingest_courts_to_db(courts=["FC", "RPD", "FCA", "SCC"])

    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT dataset FROM cases ORDER BY id").fetchall()

    assert [row[0] for row in rows] == ["FC", "RPD", "FCA", "SCC"]
