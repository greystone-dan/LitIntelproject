import json
import sqlite3

from fc_ingest.db import SQLiteDb


def test_insert_fc_pdf_persists_metadata_columns(tmp_path):
    db_path = tmp_path / "fc.db"
    db = SQLiteDb(db_path)

    db.insert_fc_pdf(
        {
            "fc_id": "350109",
            "pdf_url": "https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/350109/decision.pdf",
            "pdf_bytes": b"%PDF-1.7\n",
            "mime_type": "application/pdf",
            "case_title": "Doe v Canada",
            "decision_date": "2025-01-02",
            "neutral_citation": "2025 FC 123",
            "docket": "IMM-1234-24",
            "metadata": {"language": "en", "source_url": "https://decisions.fct-cf.gc.ca/..."},
        }
    )

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT fc_id, case_title, decision_date, neutral_citation, docket, metadata_json
            FROM fc_pdfs
            WHERE fc_id = ?
            """,
            ("350109",),
        ).fetchone()

    assert row is not None
    assert row[0] == "350109"
    assert row[1] == "Doe v Canada"
    assert row[2] == "2025-01-02"
    assert row[3] == "2025 FC 123"
    assert row[4] == "IMM-1234-24"
    metadata = json.loads(row[5])
    assert metadata["language"] == "en"


def test_existing_fc_pdfs_schema_is_upgraded_with_metadata_columns(tmp_path):
    db_path = tmp_path / "legacy.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE fc_pdfs (
                fc_id TEXT PRIMARY KEY,
                pdf_url TEXT,
                pdf_bytes BLOB,
                mime_type TEXT
            )
            """
        )
        conn.commit()

    SQLiteDb(db_path)

    with sqlite3.connect(db_path) as conn:
        columns = {row[1] for row in conn.execute("PRAGMA table_info(fc_pdfs)").fetchall()}

    assert "case_title" in columns
    assert "decision_date" in columns
    assert "neutral_citation" in columns
    assert "docket" in columns
    assert "metadata_json" in columns
