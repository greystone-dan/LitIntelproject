from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable


class SQLiteDb:
    def __init__(self, db_path: str | Path = "fc_decisions.db") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS fc_decisions (
                    fc_id TEXT PRIMARY KEY,
                    neutral_citation TEXT,
                    docket TEXT,
                    decision_date TEXT,
                    judge TEXT,
                    style_of_cause TEXT,
                    item_url TEXT,
                    document_url TEXT,
                    pdf_url TEXT,
                    full_text TEXT,
                    metadata_json TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS fc_pdfs (
                    fc_id TEXT PRIMARY KEY,
                    pdf_url TEXT,
                    pdf_bytes BLOB,
                    mime_type TEXT,
                    case_title TEXT,
                    decision_date TEXT,
                    neutral_citation TEXT,
                    docket TEXT,
                    metadata_json TEXT
                )
                """
            )
            columns = {row[1] for row in conn.execute("PRAGMA table_info(fc_pdfs)").fetchall()}
            if "case_title" not in columns:
                conn.execute("ALTER TABLE fc_pdfs ADD COLUMN case_title TEXT")
            if "decision_date" not in columns:
                conn.execute("ALTER TABLE fc_pdfs ADD COLUMN decision_date TEXT")
            if "neutral_citation" not in columns:
                conn.execute("ALTER TABLE fc_pdfs ADD COLUMN neutral_citation TEXT")
            if "docket" not in columns:
                conn.execute("ALTER TABLE fc_pdfs ADD COLUMN docket TEXT")
            if "metadata_json" not in columns:
                conn.execute("ALTER TABLE fc_pdfs ADD COLUMN metadata_json TEXT")
            conn.commit()

    def _coerce_mapping(self, record: Any) -> dict[str, Any]:
        if isinstance(record, dict):
            return record
        if hasattr(record, "__dict__"):
            return {key: value for key, value in vars(record).items() if not key.startswith("_")}
        return {}

    def get_existing_fc_ids(self) -> set[str]:
        with self._connect() as conn:
            rows = conn.execute("SELECT fc_id FROM fc_decisions").fetchall()
        return {str(row["fc_id"]) for row in rows if row["fc_id"]}

    def get_completed_fc_ids(self) -> set[str]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT decision.fc_id
                FROM fc_decisions AS decision
                LEFT JOIN fc_pdfs AS pdf ON pdf.fc_id = decision.fc_id
                WHERE length(trim(coalesce(decision.full_text, ''))) > 0
                   OR length(coalesce(pdf.pdf_bytes, X'')) > 0
                """
            ).fetchall()
        return {str(row["fc_id"]) for row in rows if row["fc_id"]}

    def get_pending_item_urls(self) -> list[str]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT decision.item_url
                FROM fc_decisions AS decision
                LEFT JOIN fc_pdfs AS pdf ON pdf.fc_id = decision.fc_id
                WHERE length(trim(coalesce(decision.item_url, ''))) > 0
                  AND length(trim(coalesce(decision.full_text, ''))) = 0
                  AND length(coalesce(pdf.pdf_bytes, X'')) = 0
                ORDER BY decision.fc_id
                """
            ).fetchall()
        return [str(row["item_url"]) for row in rows]

    def insert_fc_decision(self, record: Any) -> dict[str, Any]:
        payload = self._coerce_mapping(record)
        normalized = {
            "fc_id": payload.get("fc_id"),
            "neutral_citation": payload.get("neutral_citation"),
            "docket": payload.get("docket"),
            "decision_date": payload.get("decision_date"),
            "judge": payload.get("judge"),
            "style_of_cause": payload.get("style_of_cause"),
            "item_url": payload.get("item_url"),
            "document_url": payload.get("document_url"),
            "pdf_url": payload.get("pdf_url"),
            "full_text": payload.get("full_text"),
            "metadata_json": json.dumps(payload.get("metadata") or payload.get("metadata_json") or {}, ensure_ascii=False),
        }
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO fc_decisions (
                    fc_id,
                    neutral_citation,
                    docket,
                    decision_date,
                    judge,
                    style_of_cause,
                    item_url,
                    document_url,
                    pdf_url,
                    full_text,
                    metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    normalized["fc_id"],
                    normalized["neutral_citation"],
                    normalized["docket"],
                    normalized["decision_date"],
                    normalized["judge"],
                    normalized["style_of_cause"],
                    normalized["item_url"],
                    normalized["document_url"],
                    normalized["pdf_url"],
                    normalized["full_text"],
                    normalized["metadata_json"],
                ),
            )
            conn.commit()
        return normalized

    def insert_fc_pdf(self, record: Any) -> dict[str, Any]:
        payload = self._coerce_mapping(record)
        normalized = {
            "fc_id": payload.get("fc_id"),
            "pdf_url": payload.get("pdf_url"),
            "pdf_bytes": payload.get("pdf_bytes"),
            "mime_type": payload.get("mime_type"),
            "case_title": payload.get("case_title"),
            "decision_date": payload.get("decision_date"),
            "neutral_citation": payload.get("neutral_citation"),
            "docket": payload.get("docket"),
            "metadata_json": json.dumps(payload.get("metadata") or payload.get("metadata_json") or {}, ensure_ascii=False),
        }
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO fc_pdfs (
                    fc_id,
                    pdf_url,
                    pdf_bytes,
                    mime_type,
                    case_title,
                    decision_date,
                    neutral_citation,
                    docket,
                    metadata_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    normalized["fc_id"],
                    normalized["pdf_url"],
                    normalized["pdf_bytes"],
                    normalized["mime_type"],
                    normalized["case_title"],
                    normalized["decision_date"],
                    normalized["neutral_citation"],
                    normalized["docket"],
                    normalized["metadata_json"],
                ),
            )
            conn.commit()
        return normalized
