from __future__ import annotations

from pathlib import Path

from scripts import run_case_intelligence_request as runner


def test_build_client_uses_ollama_openai_compatible_endpoint(monkeypatch):
    captured = {}

    class FakeOpenAI:
        def __init__(self, **kwargs):
            captured.update(kwargs)

    monkeypatch.setattr(runner, "OpenAI", FakeOpenAI)

    runner.build_client(
        "local",
        ollama_base_url="http://localhost:11434/v1",
        ollama_model="qwen2.5:7b",
    )

    assert captured == {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama-local",
    }


def test_local_run_preserves_json_output_contract(tmp_path: Path):
    class FakeUsage:
        prompt_tokens = 12
        completion_tokens = 8

    class FakeMessage:
        content = '{"answer": "local"}'

    class FakeChoice:
        message = FakeMessage()

    class FakeCompletions:
        def create(self, **kwargs):
            assert kwargs["model"] == "qwen2.5:7b"
            assert kwargs["response_format"] == {"type": "json_object"}
            return type("Completion", (), {"choices": [FakeChoice()], "usage": FakeUsage()})()

    client = type("Client", (), {"chat": type("Chat", (), {"completions": FakeCompletions()})()})()
    output_path = tmp_path / "result.json"
    result = runner.run_request(
        {
            "request_id": "local-test",
            "model": "qwen2.5:7b",
            "budget_usd": 0,
            "messages": [{"role": "user", "content": "Return JSON."}],
        },
        client=client,
        output_path=output_path,
        max_output_tokens=50,
        input_rate=0,
        output_rate=0,
    )

    assert result["status"] == "case_intelligence_run_complete"
    assert result["model"] == "qwen2.5:7b"
    assert '"answer": "local"' in output_path.read_text(encoding="utf-8")