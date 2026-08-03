import json
from pathlib import Path

from scripts.verify_fc_case_existence import (
    VerifierConfig,
    check_courtfiles,
    load_case_numbers,
)


class _FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload
        self.text = json.dumps(payload)

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


class _FakeClient:
    def __init__(self, payload: dict):
        self.payload = payload

    def get(self, url, params=None):
        _ = url, params
        return _FakeResponse(self.payload)


def test_load_case_numbers_from_txt(tmp_path: Path):
    path = tmp_path / "numbers.txt"
    path.write_text("IMM-1-24\nimm-1-24\nBAD\nT-10-23\n", encoding="utf-8")

    values = load_case_numbers(path)

    assert values == ["IMM-1-24", "T-10-23"]


def test_load_case_numbers_from_json_objects(tmp_path: Path):
    path = tmp_path / "numbers.json"
    path.write_text(
        json.dumps(
            [
                {"court_number": "imm-123-24"},
                {"docket_number": "IMM-123-24"},
                {"citation": "A-9-22"},
            ]
        ),
        encoding="utf-8",
    )

    values = load_case_numbers(path)

    assert values == ["IMM-123-24", "A-9-22"]


def test_check_courtfiles_parses_count_as_exists():
    config = VerifierConfig(
        input_path=Path("dummy.txt"),
        output_jsonl=Path("out.jsonl"),
        providers=["courtfiles"],
        limit=None,
        sleep_ms=0,
        timeout=5.0,
        retries=1,
        backoff_seconds=0.0,
    )
    result = check_courtfiles(_FakeClient({"Count": 2}), "IMM-123-24", config)

    assert result["provider"] == "courtfiles"
    assert result["exists"] is True
    assert result["confidence"] == "definitive"
    assert result["count"] == 2
