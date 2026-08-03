import json
import sqlite3

from scripts.import_canlaw_staging import iter_staging_records


def test_iter_staging_records_filters_courts_and_resumes(tmp_path):
    database_path = tmp_path / "canlaw.db"
    with sqlite3.connect(database_path) as connection:
        connection.execute(
            "CREATE TABLE cases (id INTEGER PRIMARY KEY, dataset TEXT, raw_payload TEXT)"
        )
        connection.executemany(
            "INSERT INTO cases (id, dataset, raw_payload) VALUES (?, ?, ?)",
            [
                (1, "FC", json.dumps({"citation_en": "2024 FC 1"})),
                (2, "RPD", json.dumps({"citation_en": "2024 RPD 1"})),
                (3, "SCC", json.dumps({"citation_en": "2024 SCC 1"})),
            ],
        )

    records = list(iter_staging_records(database_path, ["FC", "SCC"], start_after_id=1))

    assert records == [(3, {"citation_en": "2024 SCC 1"})]
