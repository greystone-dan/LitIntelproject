import json
import hashlib
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime

from .config import DB_PATH


def _db_path() -> str:
    return DB_PATH


@contextmanager
def get_conn():
    conn = sqlite3.connect(_db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dataset TEXT,
                citation_en TEXT,
                citation_fr TEXT,
                citation2_en TEXT,
                citation2_fr TEXT,
                name_en TEXT,
                name_fr TEXT,
                document_date_en TEXT,
                document_date_fr TEXT,
                url_en TEXT,
                url_fr TEXT,
                unofficial_text_en TEXT,
                unofficial_text_fr TEXT,
                citing_cases_count INTEGER,
                cases_cited TEXT,
                cases_citing TEXT,
                source TEXT,
                source_key TEXT,
                raw_payload TEXT,
                metadata_json TEXT
            )
            """
        )
        columns = {row[1] for row in cur.execute("PRAGMA table_info(cases)")}
        if "source_key" not in columns:
            cur.execute("ALTER TABLE cases ADD COLUMN source_key TEXT")
        cur.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS ix_cases_source_key ON cases(source_key)"
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS case_embeddings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_id INTEGER,
                model TEXT,
                vector BLOB,
                FOREIGN KEY(case_id) REFERENCES cases(id)
            )
            """
        )
        cur.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS ix_case_embeddings_case_model
            ON case_embeddings(case_id, model)
            """
        )


def _json_safe(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    return value


def _merge_lists(*values) -> list:
    merged = []
    seen = set()
    for value in values:
        for item in value or []:
            normalized = str(item).strip()
            if normalized and normalized not in seen:
                seen.add(normalized)
                merged.append(normalized)
    return merged


def _source_key(row: dict, dataset: str) -> str:
    identity = {
        "dataset": dataset,
        "citation_en": row.get("citation_en"),
        "citation_fr": row.get("citation_fr"),
        "url_en": row.get("url_en"),
        "url_fr": row.get("url_fr"),
        "document_date_en": str(row.get("document_date_en") or ""),
        "document_date_fr": str(row.get("document_date_fr") or ""),
    }
    if not any(value for key, value in identity.items() if key != "dataset"):
        identity["raw_payload"] = _json_safe(row)
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def insert_case(conn, row, dataset):
    cur = conn.cursor()
    row_dict = dict(row or {}) if isinstance(row, dict) else {}
    safe_row = _json_safe(row_dict)
    source_key = _source_key(row_dict, dataset)
    cases_cited = _merge_lists(
        row_dict.get("cases_cited"),
        row_dict.get("cases_cited_en"),
        row_dict.get("cases_cited_fr"),
    )
    cases_citing = _merge_lists(
        row_dict.get("cases_citing"),
        row_dict.get("cases_citing_en"),
        row_dict.get("cases_citing_fr"),
    )
    existing_id = cur.execute(
        "SELECT id FROM cases WHERE source_key = ?",
        (source_key,),
    ).fetchone()
    if existing_id:
        return existing_id[0]

    natural_identity = (
        row_dict.get("citation_en"),
        row_dict.get("citation_fr"),
        row_dict.get("url_en"),
        row_dict.get("url_fr"),
    )
    if any(natural_identity):
        existing_id = cur.execute(
            """
            SELECT id FROM cases
            WHERE dataset = ?
              AND COALESCE(citation_en, '') = ?
              AND COALESCE(citation_fr, '') = ?
              AND COALESCE(url_en, '') = ?
              AND COALESCE(url_fr, '') = ?
            LIMIT 1
            """,
            (dataset, *(value or "" for value in natural_identity)),
        ).fetchone()
        if existing_id:
            cur.execute(
                """
                UPDATE cases
                SET source_key = ?, cases_cited = ?, cases_citing = ?
                WHERE id = ?
                """,
                (
                    source_key,
                    json.dumps(cases_cited),
                    json.dumps(cases_citing),
                    existing_id[0],
                ),
            )
            return existing_id[0]

    cur.execute(
        """
        INSERT INTO cases (
            dataset,
            citation_en, citation_fr,
            citation2_en, citation2_fr,
            name_en, name_fr,
            document_date_en, document_date_fr,
            url_en, url_fr,
            unofficial_text_en, unofficial_text_fr,
            citing_cases_count,
            cases_cited, cases_citing,
            source,
            source_key,
            raw_payload,
            metadata_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            dataset,
            row_dict.get("citation_en"), row_dict.get("citation_fr"),
            row_dict.get("citation2_en"), row_dict.get("citation2_fr"),
            row_dict.get("name_en"), row_dict.get("name_fr"),
            str(row_dict.get("document_date_en") or ""), str(row_dict.get("document_date_fr") or ""),
            row_dict.get("url_en"), row_dict.get("url_fr"),
            row_dict.get("unofficial_text_en"), row_dict.get("unofficial_text_fr"),
            row_dict.get("citing_cases_count"),
            json.dumps(cases_cited),
            json.dumps(cases_citing),
            "huggingface",
            source_key,
            json.dumps(safe_row),
            json.dumps(
                {
                    key: _json_safe(value)
                    for key, value in safe_row.items()
                    if key not in {"unofficial_text_en", "unofficial_text_fr"}
                }
            ),
        ),
    )
    return cur.lastrowid


def insert_embedding(conn, case_id, model_name, vector_bytes):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO case_embeddings (case_id, model, vector)
        VALUES (?, ?, ?)
        ON CONFLICT(case_id, model) DO UPDATE SET vector = excluded.vector
        """,
        (case_id, model_name, vector_bytes),
    )
    return cur.lastrowid


def repair_case_metadata(batch_size: int = 100) -> int:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")

    init_db()
    repaired = 0
    last_case_id = 0
    with get_conn() as conn:
        while True:
            rows = conn.execute(
                """
                SELECT id, dataset, raw_payload
                FROM cases
                WHERE id > ? AND source_key IS NULL
                ORDER BY id
                LIMIT ?
                """,
                (last_case_id, batch_size),
            ).fetchall()
            if not rows:
                break

            for case_id, dataset, raw_payload in rows:
                row = json.loads(raw_payload)
                cases_cited = _merge_lists(
                    row.get("cases_cited"),
                    row.get("cases_cited_en"),
                    row.get("cases_cited_fr"),
                )
                cases_citing = _merge_lists(
                    row.get("cases_citing"),
                    row.get("cases_citing_en"),
                    row.get("cases_citing_fr"),
                )
                conn.execute(
                    """
                    UPDATE OR IGNORE cases
                    SET source_key = ?, cases_cited = ?, cases_citing = ?
                    WHERE id = ?
                    """,
                    (
                        _source_key(row, dataset),
                        json.dumps(cases_cited),
                        json.dumps(cases_citing),
                        case_id,
                    ),
                )
                repaired += 1
            last_case_id = rows[-1][0]
            conn.commit()

    return repaired
