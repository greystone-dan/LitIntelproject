from copy import deepcopy

from fastapi.testclient import TestClient

from backend import health
from backend.main import app


def _database_checks(*, database="ok", vector="ok", tables="ok", missing=None):
    return {
        "database": {"status": database},
        "vector_extension": {"status": vector},
        "required_tables": {
            "status": tables,
            "missing": missing or [],
        },
    }


def _install_probes(monkeypatch, *, db=None, endpoint="ok"):
    monkeypatch.setattr(
        health,
        "_database_probe",
        lambda: deepcopy(db or _database_checks()),
    )
    monkeypatch.setattr(
        health,
        "_model_endpoint_probe",
        lambda: {
            "status": endpoint,
            "checks": {
                "text_generation": {"provider": "local", "status": endpoint},
                "embeddings": {"provider": "openai", "status": "ok"},
            },
        },
    )


def test_readiness_is_healthy_when_all_mocked_probes_pass(monkeypatch):
    _install_probes(monkeypatch)

    document, ready = health.readiness()

    assert ready is True
    assert document["status"] == "ok"
    assert document["checks"]["database"]["status"] == "ok"
    assert document["checks"]["vector_extension"]["status"] == "ok"
    assert document["checks"]["required_tables"] == {"status": "ok", "missing": []}
    assert document["checks"]["model_endpoints"]["status"] == "ok"
    assert document["checks"]["model_endpoints"]["checks"]["text_generation"]["status"] == "ok"
    assert document["checks"]["model_endpoints"]["checks"]["embeddings"]["status"] == "ok"


def test_readiness_fails_when_database_is_down(monkeypatch):
    _install_probes(
        monkeypatch,
        db=_database_checks(database="error", vector="not_checked", tables="not_checked"),
    )

    document, ready = health.readiness()

    assert ready is False
    assert document["status"] == "error"
    assert document["checks"]["database"]["status"] == "error"
    assert document["checks"]["vector_extension"]["status"] == "not_checked"
    assert document["checks"]["required_tables"]["status"] == "not_checked"


def test_readiness_fails_when_vector_extension_is_missing(monkeypatch):
    _install_probes(monkeypatch, db=_database_checks(vector="error"))

    document, ready = health.readiness()

    assert ready is False
    assert document["checks"]["database"]["status"] == "ok"
    assert document["checks"]["vector_extension"]["status"] == "error"


def test_readiness_fails_when_required_tables_are_missing(monkeypatch):
    _install_probes(
        monkeypatch,
        db=_database_checks(tables="error", missing=["cases"]),
    )

    document, ready = health.readiness()

    assert ready is False
    assert document["checks"]["required_tables"] == {
        "status": "error",
        "missing": ["cases"],
    }


def test_readiness_fails_when_configured_model_endpoint_is_down(monkeypatch):
    _install_probes(monkeypatch, endpoint="error")

    document, ready = health.readiness()

    assert ready is False
    assert document["checks"]["model_endpoints"]["status"] == "error"
    assert document["checks"]["model_endpoints"]["checks"]["text_generation"] == {
        "provider": "local",
        "status": "error",
    }


def test_model_endpoint_probe_uses_short_timeout_and_hides_endpoint(monkeypatch):
    calls = []

    def fake_get(url, *, timeout):
        calls.append((url, timeout))
        raise RuntimeError("connection failed: private-host.invalid")

    monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://private-host.invalid:11434/v1")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(health.httpx, "get", fake_get)

    result = health._model_endpoint_probe()

    assert result == {
        "status": "error",
        "checks": {
            "text_generation": {"provider": "local", "status": "error"},
            "embeddings": {"provider": "openai", "status": "not_configured"},
        },
    }
    assert calls == [
        ("http://private-host.invalid:11434/api/tags", health.PROBE_TIMEOUT_SECONDS)
    ]
    assert "private-host.invalid" not in str(result)


def test_model_endpoint_probe_checks_selected_and_embedding_endpoints(monkeypatch):
    calls = []

    class SuccessfulResponse:
        @staticmethod
        def raise_for_status():
            return None

    def fake_get(url, *, timeout, headers=None):
        calls.append((url, timeout, headers))
        return SuccessfulResponse()

    monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://local-model.invalid:11434/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://embedding.invalid/v1")
    monkeypatch.setattr(health.httpx, "get", fake_get)

    result = health._model_endpoint_probe()

    assert result == {
        "status": "ok",
        "checks": {
            "text_generation": {"provider": "local", "status": "ok"},
            "embeddings": {"provider": "openai", "status": "ok"},
        },
    }
    assert [call[:2] for call in calls] == [
        ("http://local-model.invalid:11434/api/tags", health.PROBE_TIMEOUT_SECONDS),
        ("https://embedding.invalid/v1/models", health.PROBE_TIMEOUT_SECONDS),
    ]
    assert calls[1][2] == {"Authorization": "Bearer " + "test-key"}


def test_model_endpoint_probe_is_healthy_when_no_remote_endpoints_are_configured(
    monkeypatch,
):
    monkeypatch.delenv("TEXT_GENERATION_PROVIDER", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(health, "_database_probe", _database_checks)
    monkeypatch.setattr(
        health.httpx,
        "get",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("unexpected probe")),
    )

    document, ready = health.readiness()

    assert ready is True
    assert document["status"] == "ok"
    assert document["checks"]["model_endpoints"] == {
        "status": "ok",
        "checks": {
            "text_generation": {"provider": "openai", "status": "not_configured"},
            "embeddings": {"provider": "openai", "status": "not_configured"},
        },
    }


def test_model_endpoint_probe_local_generation_does_not_require_openai_key(monkeypatch):
    calls = []

    class SuccessfulResponse:
        @staticmethod
        def raise_for_status():
            return None

    def fake_get(url, *, timeout, headers=None):
        calls.append((url, timeout, headers))
        return SuccessfulResponse()

    monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://local-model.invalid:11434/v1")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(health, "_database_probe", _database_checks)
    monkeypatch.setattr(health.httpx, "get", fake_get)

    document, ready = health.readiness()

    assert ready is True
    assert document["checks"]["model_endpoints"] == {
        "status": "ok",
        "checks": {
            "text_generation": {"provider": "local", "status": "ok"},
            "embeddings": {"provider": "openai", "status": "not_configured"},
        },
    }
    assert calls == [
        ("http://local-model.invalid:11434/api/tags", health.PROBE_TIMEOUT_SECONDS, None)
    ]


def test_model_endpoint_probe_reports_configured_openai_outage(monkeypatch):
    calls = []

    def fake_get(url, *, timeout, headers=None):
        calls.append((url, timeout, headers))
        raise RuntimeError("connection failed: private-host.invalid")

    monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://private-host.invalid/v1")
    monkeypatch.setattr(health.httpx, "get", fake_get)

    result = health._model_endpoint_probe()

    assert result == {
        "status": "error",
        "checks": {
            "text_generation": {"provider": "openai", "status": "error"},
            "embeddings": {"provider": "openai", "status": "error"},
        },
    }
    assert calls == [
        (
            "https://private-host.invalid/v1/models",
            health.PROBE_TIMEOUT_SECONDS,
            {"Authorization": "Bearer " + "test-key"},
        )
    ]
    assert "private-host.invalid" not in str(result)


def test_health_routes_remain_public_with_password_gate_and_legacy_health_exact(
    monkeypatch,
):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    _install_probes(monkeypatch)
    client = TestClient(app)

    legacy = client.get("/health")
    live = client.get("/health/live")
    ready = client.get("/health/ready")

    assert legacy.status_code == 200
    assert legacy.json() == {"message": "AI CaseLibrary backend is running"}
    assert live.status_code == 200
    assert live.json() == {"status": "ok"}
    assert ready.status_code == 200


def test_public_readiness_route_returns_503_when_a_required_probe_fails(monkeypatch):
    monkeypatch.setenv("CASELIBRARY_ACCESS_PASSWORD", "test-password")
    _install_probes(monkeypatch, endpoint="error")

    response = TestClient(app).get("/health/ready")

    assert response.status_code == 503
    assert response.json()["status"] == "error"
