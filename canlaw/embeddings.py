import logging

import numpy as np

from .config import EMBEDDING_MODEL_NAME
from .db import get_conn, insert_embedding

logger = logging.getLogger(__name__)

_embed_model = None


def get_embed_model():
    global _embed_model
    if _embed_model is None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:  # pragma: no cover - import guard
            raise RuntimeError("The 'sentence-transformers' package is required for embeddings") from exc
        _embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _embed_model


def embed_all_court_cases(courts=None, batch_size: int = 16) -> int:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")

    model = get_embed_model()
    court_names = [court.strip().upper() for court in (courts or [])]
    params = list(court_names)
    court_filter = f"AND c.dataset IN ({','.join('?' for _ in court_names)})" if court_names else ""
    embedded = 0
    last_case_id = 0

    with get_conn() as conn:
        while True:
            rows = conn.execute(
                f"""
                SELECT c.id, COALESCE(c.unofficial_text_en, c.unofficial_text_fr)
                FROM cases AS c
                WHERE c.id > ?
                  AND COALESCE(c.unofficial_text_en, c.unofficial_text_fr) IS NOT NULL
                  {court_filter}
                  AND NOT EXISTS (
                      SELECT 1 FROM case_embeddings AS e
                      WHERE e.case_id = c.id AND e.model = ?
                  )
                ORDER BY c.id
                LIMIT ?
                """,
                [last_case_id, *params, EMBEDDING_MODEL_NAME, batch_size],
            ).fetchall()
            if not rows:
                break

            vectors = model.encode(
                [text for _, text in rows],
                batch_size=batch_size,
                show_progress_bar=False,
            )
            for (case_id, _), vector in zip(rows, vectors):
                insert_embedding(
                    conn,
                    case_id,
                    EMBEDDING_MODEL_NAME,
                    np.asarray(vector, dtype=np.float32).tobytes(),
                )
            embedded += len(rows)
            last_case_id = rows[-1][0]
            conn.commit()
            logger.info("Embedded %d cases", embedded)

    return embedded
