import importlib
import os

from sqlalchemy import URL


def test_database_url_prefers_postgres_parts(monkeypatch):
    import dotenv

    monkeypatch.setattr(dotenv, "load_dotenv", lambda *args, **kwargs: True)
    monkeypatch.setenv("DATABASE_URL", "******localhost:5432/ai_caselibrary")
    monkeypatch.setenv("POSTGRES_USER", "real_user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "real_password")
    monkeypatch.setenv("POSTGRES_HOST", "dbhost")
    monkeypatch.setenv("POSTGRES_PORT", "5433")
    monkeypatch.setenv("POSTGRES_DB", "caselibrary")

    import backend.database as database
    import backend.settings as settings_module

    importlib.reload(settings_module)
    importlib.reload(database)

    url = database._database_url()

    assert isinstance(url, URL)
    assert str(url).startswith("postgresql+psycopg2://real_user")
    assert url.database == "caselibrary"


def test_database_url_falls_back_to_database_url(monkeypatch):
    import dotenv

    monkeypatch.setattr(dotenv, "load_dotenv", lambda *args, **kwargs: True)
    monkeypatch.setenv("DATABASE_URL", "sqlite:///demo_db.sqlite3")
    for key in [
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
    ]:
        monkeypatch.delenv(key, raising=False)

    import backend.database as database
    import backend.settings as settings_module

    importlib.reload(settings_module)
    importlib.reload(database)

    url = database._database_url()

    assert isinstance(url, str)
    assert url == "sqlite:///demo_db.sqlite3"


def test_exported_env_beats_dotenv(monkeypatch):
    imported = []

    def fake_load_dotenv(path, override=False):
        imported.append(("backend" if path.parent.name == "backend" else "root", override))
        file_values = {
            "POSTGRES_USER": "file_user",
            "POSTGRES_PASSWORD": "file_password",
            "POSTGRES_HOST": "file_host",
            "POSTGRES_PORT": "6543",
            "POSTGRES_DB": "file_db",
            "OPENAI_CHAT_MODEL": "file-model",
        }
        for key, value in file_values.items():
            if override or key not in os.environ:
                os.environ[key] = value
        return True

    monkeypatch.setenv("POSTGRES_USER", "exported_user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "exported_password")
    monkeypatch.setenv("POSTGRES_HOST", "exported_host")
    monkeypatch.setenv("POSTGRES_PORT", "5434")
    monkeypatch.setenv("POSTGRES_DB", "exported_db")
    monkeypatch.setenv("OPENAI_CHAT_MODEL", "exported-model")

    import dotenv
    import backend.settings as settings_module

    monkeypatch.setattr(dotenv, "load_dotenv", fake_load_dotenv)
    importlib.reload(settings_module)

    assert settings_module.settings.database.user == "exported_user"
    assert settings_module.settings.database.password == "exported_password"
    assert settings_module.settings.chat.openai_model == "exported-model"
    assert imported == [("backend", False), ("root", False)]
    assert all(override is False for _, override in imported)


def test_backend_dotenv_wins_over_root_dotenv(monkeypatch):
    imported = []

    def fake_load_dotenv(path, override=False):
        key = "backend" if path.parent.name == "backend" else "root"
        imported.append((key, override))
        file_values = {
            "root": {"POSTGRES_USER": "root_user", "OPENAI_CHAT_MODEL": "root-model"},
            "backend": {"POSTGRES_USER": "backend_user", "OPENAI_CHAT_MODEL": "backend-model"},
        }[key]
        for key, value in file_values.items():
            if override or key not in os.environ:
                os.environ[key] = value
        return True

    for key in ["POSTGRES_USER", "OPENAI_CHAT_MODEL"]:
        monkeypatch.delenv(key, raising=False)

    import dotenv
    import backend.settings as settings_module

    monkeypatch.setattr(dotenv, "load_dotenv", fake_load_dotenv)
    importlib.reload(settings_module)

    assert settings_module.settings.database.user == "backend_user"
    assert settings_module.settings.chat.openai_model == "backend-model"
    assert imported == [("backend", False), ("root", False)]
