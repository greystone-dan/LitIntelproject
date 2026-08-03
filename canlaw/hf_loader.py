import logging
from collections.abc import Iterable, Mapping

from .config import DEFAULT_COURTS, HF_COURT_DATA_DIRS, HF_DATASET
from .db import get_conn, init_db, insert_case

logger = logging.getLogger(__name__)


def load_court_dataset(court: str):
    try:
        from datasets import load_dataset
    except ImportError as exc:  # pragma: no cover - import guard
        raise RuntimeError("The 'datasets' package is required to download Hugging Face data") from exc

    data_dir = HF_COURT_DATA_DIRS.get(court)
    if not data_dir:
        raise ValueError(f"No Hugging Face data directory configured for court {court}")

    return load_dataset(HF_DATASET, data_dir=data_dir, split="train")


def normalize_courts(courts: Iterable[str] | None) -> list[str]:
    requested = courts or DEFAULT_COURTS
    normalized = list(dict.fromkeys(court.strip().upper() for court in requested if court.strip()))
    unsupported = [court for court in normalized if court not in HF_COURT_DATA_DIRS]
    if unsupported:
        supported = ", ".join(sorted(HF_COURT_DATA_DIRS))
        raise ValueError(f"Unsupported court codes: {', '.join(unsupported)}. Supported: {supported}")
    return normalized


def ingest_courts_to_db(courts: Iterable[str] | None = None) -> dict[str, int]:
    init_db()
    court_names = normalize_courts(courts)
    counts = {}

    for court in court_names:
        logger.info("Ingesting court %s from Hugging Face", court)
        rows = load_court_dataset(court)
        count = 0
        with get_conn() as conn:
            for row in rows:
                if not isinstance(row, Mapping):
                    raise TypeError(f"Expected a mapping for {court}, got {type(row).__name__}")
                insert_case(conn, dict(row), court)
                count += 1
        counts[court] = count
        logger.info("Processed %d %s records", count, court)

    return counts
