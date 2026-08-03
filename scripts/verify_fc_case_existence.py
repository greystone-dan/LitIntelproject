from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

COURT_FILES_ENDPOINT = "https://www.fct-cf.ca/CourtFilesAndDecisions/proceedingQueriesCourtNumberList"
DECISIONS_SEARCH_URL = "https://decisions.fct-cf.gc.ca/fc-cf/en/d/s/index.do"
USER_AGENT = "AI-CaseLibrary-FCExistenceVerifier/1.0"
CASE_NUMBER_RE = re.compile(r"^[A-Z]{1,5}-\d+-\d{2}$")


@dataclass
class VerifierConfig:
    input_path: Path
    output_jsonl: Path
    providers: list[str]
    limit: int | None
    sleep_ms: int
    timeout: float
    retries: int
    backoff_seconds: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify whether Federal Court case numbers exist across configured sources"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/raw/fc/valid_imm_numbers_from_mci.txt"),
        help="Input .txt/.json/.jsonl file with case numbers",
    )
    parser.add_argument(
        "--output-jsonl",
        type=Path,
        default=Path("data/raw/fc/case_existence_results.jsonl"),
        help="Output JSONL results path",
    )
    parser.add_argument(
        "--providers",
        default="courtfiles,decisions",
        help="Comma-separated providers: courtfiles,decisions",
    )
    parser.add_argument("--limit", type=int, default=None, help="Optional max case numbers to check")
    parser.add_argument("--sleep-ms", type=int, default=150, help="Delay between checks in milliseconds")
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTP timeout seconds")
    parser.add_argument("--retries", type=int, default=3, help="Retries per request")
    parser.add_argument("--backoff-seconds", type=float, default=0.75, help="Retry backoff base seconds")
    return parser.parse_args()


def build_config(args: argparse.Namespace) -> VerifierConfig:
    providers = [item.strip().lower() for item in args.providers.split(",") if item.strip()]
    allowed = {"courtfiles", "decisions"}
    unknown = [name for name in providers if name not in allowed]
    if unknown:
        raise ValueError(f"Unsupported providers: {', '.join(unknown)}")
    if not providers:
        raise ValueError("At least one provider is required")

    return VerifierConfig(
        input_path=args.input,
        output_jsonl=args.output_jsonl,
        providers=providers,
        limit=args.limit,
        sleep_ms=max(0, args.sleep_ms),
        timeout=max(1.0, args.timeout),
        retries=max(1, args.retries),
        backoff_seconds=max(0.0, args.backoff_seconds),
    )


def _normalize_case_number(value: str | None) -> str | None:
    text = str(value or "").strip().upper()
    if not text:
        return None
    if not CASE_NUMBER_RE.match(text):
        return None
    return text


def load_case_numbers(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    numbers: list[str] = []
    suffix = path.suffix.lower()

    if suffix == ".txt":
        for line in path.read_text(encoding="utf-8").splitlines():
            case_number = _normalize_case_number(line)
            if case_number:
                numbers.append(case_number)
    elif suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        items = payload if isinstance(payload, list) else [payload]
        for item in items:
            if isinstance(item, str):
                case_number = _normalize_case_number(item)
            elif isinstance(item, dict):
                case_number = _normalize_case_number(
                    item.get("court_number") or item.get("docket_number") or item.get("citation")
                )
            else:
                case_number = None
            if case_number:
                numbers.append(case_number)
    elif suffix == ".jsonl":
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if isinstance(row, str):
                case_number = _normalize_case_number(row)
            elif isinstance(row, dict):
                case_number = _normalize_case_number(
                    row.get("court_number") or row.get("docket_number") or row.get("citation")
                )
            else:
                case_number = None
            if case_number:
                numbers.append(case_number)
    else:
        raise ValueError(f"Unsupported input type: {suffix}")

    # Deduplicate while preserving order.
    deduped: list[str] = []
    seen: set[str] = set()
    for number in numbers:
        if number in seen:
            continue
        seen.add(number)
        deduped.append(number)
    return deduped


def request_with_retry(
    client: httpx.Client,
    url: str,
    *,
    params: dict[str, Any] | None,
    retries: int,
    backoff_seconds: float,
) -> httpx.Response:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = client.get(url, params=params)
            response.raise_for_status()
            return response
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Request failed for {url}") from last_error


def check_courtfiles(client: httpx.Client, number: str, config: VerifierConfig) -> dict[str, Any]:
    try:
        response = request_with_retry(
            client,
            COURT_FILES_ENDPOINT,
            params={"division": "t", "courtnumber": number},
            retries=config.retries,
            backoff_seconds=config.backoff_seconds,
        )
        payload = response.json() if response.text else {}
        count = int(payload.get("Count") or 0)
        return {
            "provider": "courtfiles",
            "exists": count > 0,
            "confidence": "definitive",
            "count": count,
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "provider": "courtfiles",
            "exists": None,
            "confidence": "definitive",
            "error": str(exc),
        }


def check_decisions(client: httpx.Client, number: str, config: VerifierConfig) -> dict[str, Any]:
    try:
        response = request_with_retry(
            client,
            DECISIONS_SEARCH_URL,
            params={"cont": number},
            retries=config.retries,
            backoff_seconds=config.backoff_seconds,
        )
        # This endpoint does not expose a reliable server-side hit count in the static HTML.
        # We still record that the external lookup executed and whether the query token appears.
        body_upper = response.text.upper()
        return {
            "provider": "decisions",
            "exists": None,
            "confidence": "signal_only",
            "token_seen": number in body_upper,
            "status_code": response.status_code,
            "url": str(response.url),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "provider": "decisions",
            "exists": None,
            "confidence": "signal_only",
            "error": str(exc),
        }


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def run_verification(config: VerifierConfig) -> dict[str, int]:
    numbers = load_case_numbers(config.input_path)
    if config.limit is not None:
        if config.limit <= 0:
            raise ValueError("--limit must be greater than zero")
        numbers = numbers[: config.limit]

    if config.output_jsonl.exists():
        config.output_jsonl.unlink()

    checked = exists_yes = exists_no = errors = 0

    headers = {"User-Agent": USER_AGENT}
    with httpx.Client(timeout=config.timeout, headers=headers, follow_redirects=True) as client:
        for number in numbers:
            checks: list[dict[str, Any]] = []
            if "courtfiles" in config.providers:
                checks.append(check_courtfiles(client, number, config))
            if "decisions" in config.providers:
                checks.append(check_decisions(client, number, config))

            definitive = [item for item in checks if item.get("confidence") == "definitive"]
            definitive_exists = [item.get("exists") for item in definitive if item.get("exists") is not None]

            if True in definitive_exists:
                aggregate_exists: bool | None = True
                exists_yes += 1
            elif definitive_exists and all(value is False for value in definitive_exists):
                aggregate_exists = False
                exists_no += 1
            else:
                aggregate_exists = None
                errors += 1

            row = {
                "court_number": number,
                "exists": aggregate_exists,
                "providers": checks,
            }
            append_jsonl(config.output_jsonl, row)
            checked += 1

            if config.sleep_ms > 0:
                time.sleep(config.sleep_ms / 1000)

    return {
        "checked": checked,
        "exists_yes": exists_yes,
        "exists_no": exists_no,
        "unknown_or_error": errors,
    }


def main() -> None:
    args = parse_args()
    config = build_config(args)
    summary = run_verification(config)
    print(
        "Checked={checked} Exists={exists_yes} Missing={exists_no} Unknown={unknown_or_error} Output={output}".format(
            checked=summary["checked"],
            exists_yes=summary["exists_yes"],
            exists_no=summary["exists_no"],
            unknown_or_error=summary["unknown_or_error"],
            output=config.output_jsonl,
        )
    )


if __name__ == "__main__":
    main()
