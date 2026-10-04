from backend import text_generation_providers as providers


def test_openai_provider_uses_configured_chat_model(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OPENAI_CHAT_MODEL", "gpt-test")
    monkeypatch.delenv("TEXT_GENERATION_PROVIDER", raising=False)

    provider = providers.get_text_generation_provider()

    assert provider.model_name == "gpt-test"
