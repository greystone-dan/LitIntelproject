"""Small, bounded probes used by the public health endpoints."""

from __future__ import annotations

import os
from typing import Any

import httpx


PROBE_TIMEOUT_SECONDS = 2.0
_OK = "ok"
_ERROR = "error"
_NOT_CHECKED = "not_checked"
_NOT_CONFIGURED = "not_configured"


def _database_probe() -> dict[str, Any]:
    """Check connectivity, pgvector, and all ORM-managed tables independently."""
    probe_engine = None
    try:
        from sqlalchemy import bindparam, create_engine, text
        from sqlalchemy.pool import NullPool

        from .database import Base, engine as application_engine

        probe_engine = create_engine(
            application_engine.url,
            connect_args={"connect_timeout": int(PROBE_TIMEOUT_SECONDS)},
            poolclass=NullPool,
        )
        with probe_engine.connect() as connection:
            connection.execute(
                text("SELECT set_config('statement_timeout', :timeout, false)"),
                {"timeout": str(int(PROBE_TIMEOUT_SECONDS * 1000))},
            )
            connection.execute(text("SELECT 1"))
            vector_available = bool(
                connection.execute(
                    text("SELECT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'vector')")
                ).scalar()
            )
            required_tables = sorted(Base.metadata.tables)
            present_tables = set(
                connection.execute(
                    text(
                        "SELECT table_name FROM information_schema.tables "
                        "WHERE table_schema = current_schema() "
                        "AND table_type = 'BASE TABLE' AND table_name IN :required"
                    ).bindparams(bindparam("required", expanding=True)),
                    {"required": required_tables},
                ).scalars()
            )
        missing_tables = sorted(set(required_tables) - present_tables)
        return {
            "database": {"status": _OK},
            "vector_extension": {
                "status": _OK if vector_available else _ERROR
            },
            "required_tables": {
                "status": _OK if not missing_tables else _ERROR,
                "missing": missing_tables,
            },
        }
    except Exception:
        return {
            "database": {"status": _ERROR},
            "vector_extension": {"status": _NOT_CHECKED},
            "required_tables": {"status": _NOT_CHECKED, "missing": []},
        }
    finally:
        if probe_engine is not None:
            probe_engine.dispose()


def _model_endpoint_probe() -> dict[str, Any]:
    """Check configured generation and embedding services without model inference."""
    configured_provider = os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower()
    provider = (
        configured_provider
        if configured_provider in {"openai", "local"}
        else "unconfigured"
    )
    generation_status = _ERROR if provider == "unconfigured" else _NOT_CONFIGURED
    generation = {"provider": provider, "status": generation_status}
    embeddings = {"provider": "openai", "status": _NOT_CONFIGURED}

    if provider == "local":
        try:
            base_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1").strip()
            if not base_url:
                raise ValueError("Local model endpoint is not configured")
            url = base_url.rstrip("/").removesuffix("/v1") + "/api/tags"
            response = httpx.get(url, timeout=PROBE_TIMEOUT_SECONDS)
            response.raise_for_status()
            generation["status"] = _OK
        except Exception:
            # Never include exception text: it may contain a URL or credential.
            generation["status"] = _ERROR

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").strip()
            if not base_url:
                raise ValueError("OpenAI endpoint is not configured")
            response = httpx.get(
                base_url.rstrip("/") + "/models",
                headers={"Authorization": "Bearer " + api_key},
                timeout=PROBE_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            embeddings["status"] = _OK
        except Exception:
            # Never include exception text: it may contain a URL or credential.
            embeddings["status"] = _ERROR

        if provider == "openai":
            generation["status"] = embeddings["status"]

    endpoint_statuses = (generation["status"], embeddings["status"])
    return {
        "status": (
            _OK
            if all(status in {_OK, _NOT_CONFIGURED} for status in endpoint_statuses)
            else _ERROR
        ),
        "checks": {
            "text_generation": generation,
            "embeddings": embeddings,
        },
    }


def readiness() -> tuple[dict[str, Any], bool]:
    """Return a safe readiness document and whether every required probe passed."""
    checks = _database_probe()
    checks["model_endpoints"] = _model_endpoint_probe()
    ready = all(
        check["status"] == _OK
        for check in checks.values()
    )
    return {"status": _OK if ready else _ERROR, "checks": checks}, ready


def liveness() -> dict[str, str]:
    """Report that the application process can serve requests."""
    return {"status": _OK}
