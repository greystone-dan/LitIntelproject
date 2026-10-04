from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(Path(__file__).resolve().parent / ".env", override=False)
load_dotenv(PROJECT_ROOT / ".env", override=False)


def _env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    return default if value is None else value


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class AppSettings:
    @property
    def name(self) -> str:
        return _env("APP_NAME", "MyAIProject") or "MyAIProject"

    @property
    def env(self) -> str:
        return _env("APP_ENV", "development") or "development"

    @property
    def port(self) -> int:
        return _env_int("APP_PORT", 8000)

    @property
    def debug(self) -> bool:
        return _env_bool("DEBUG", False)

    @property
    def reload(self) -> bool:
        return True


@dataclass(frozen=True)
class DatabaseSettings:
    @property
    def user(self) -> str | None:
        return _env("POSTGRES_USER")

    @property
    def password(self) -> str | None:
        return _env("POSTGRES_PASSWORD")

    @property
    def host(self) -> str | None:
        return _env("POSTGRES_HOST")

    @property
    def port(self) -> str | None:
        return _env("POSTGRES_PORT")

    @property
    def database(self) -> str | None:
        return _env("POSTGRES_DB")

    @property
    def url(self) -> str | URL:
        if any([self.user, self.password, self.host, self.port, self.database]):
            return URL.create(
                drivername="postgresql+psycopg2",
                username=self.user or "postgres",
                password=self.password or "postgres",
                host=self.host or "localhost",
                port=int(self.port or "5432"),
                database=self.database or "caselibrary",
            )

        configured_url = (_env("DATABASE_URL", "") or "").strip()
        if configured_url:
            return configured_url

        return URL.create(
            drivername="postgresql+psycopg2",
            username="postgres",
            password="postgres",
            host="localhost",
            port=5432,
            database="caselibrary",
        )


@dataclass(frozen=True)
class EmbeddingSettings:
    @property
    def model(self) -> str:
        return _env("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small") or "text-embedding-3-small"

    @property
    def api_key(self) -> str | None:
        return _env("OPENAI_API_KEY")

    @property
    def organization(self) -> str | None:
        return _env("OPENAI_ORG_ID") or None

    @property
    def device(self) -> str:
        return _env("LOCAL_EMBEDDING_DEVICE", "cpu") or "cpu"

    @property
    def dimensions(self) -> int:
        return 1536


@dataclass(frozen=True)
class ChatSettings:
    @property
    def provider(self) -> str:
        return _env("TEXT_GENERATION_PROVIDER", "openai") or "openai"

    @property
    def api_key(self) -> str | None:
        return _env("OPENAI_API_KEY")

    @property
    def openai_model(self) -> str:
        return _env("OPENAI_CHAT_MODEL", "gpt-4o-mini") or "gpt-4o-mini"

    @property
    def ollama_base_url(self) -> str:
        return _env("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1") or "http://127.0.0.1:11434/v1"

    @property
    def ollama_model(self) -> str:
        return _env("OLLAMA_MODEL", "qwen3:4b") or "qwen3:4b"


@dataclass(frozen=True)
class AuditSettings:
    @property
    def log_path(self) -> str | None:
        return _env("CASELIBRARY_AUDIT_LOG")

    @property
    def raw_address(self) -> bool:
        return _env_bool("CASELIBRARY_AUDIT_LOG_RAW_ADDRESS", False)


@dataclass(frozen=True)
class AccessSettings:
    @property
    def password(self) -> str | None:
        return _env("CASELIBRARY_ACCESS_PASSWORD")

    @property
    def session_secret(self) -> str:
        return (
            _env("CASELIBRARY_SESSION_SECRET")
            or _env("SECRET_KEY")
            or self.password
            or ""
        )

    @property
    def session_seconds(self) -> int:
        raw = _env_int("CASELIBRARY_SESSION_SECONDS", 86400)
        return max(300, raw)


class Settings:
    def __init__(self) -> None:
        self.app = AppSettings()
        self.database = DatabaseSettings()
        self.embedding = EmbeddingSettings()
        self.chat = ChatSettings()
        self.audit = AuditSettings()
        self.access = AccessSettings()


settings = Settings()
