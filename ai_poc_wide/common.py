"""Shared helpers for the AI proof-of-concept scripts: spend ledger with a hard cap, retrying model calls.

Report-only. Reads case JSON, writes JSON files, never touches the database. Only open case law is sent.
"""

from __future__ import annotations

import json
import os
import random
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# USD per million tokens (input, output). Taken from OpenAI list prices as last recorded; verify before a big run.
PRICES = {
	"gpt-4.1-nano": (0.10, 0.40),
	"gpt-4.1-mini": (0.40, 1.60),
	"gpt-4.1": (2.00, 8.00),
	"gpt-5-nano": (0.05, 0.40),
	"gpt-5-mini": (0.25, 2.00),
	"gpt-5": (1.25, 10.00),
	"o4-mini": (1.10, 4.40),
}
HARD_CAP_USD = 9.50  # the approved budget is US$10 in total; stop before it


def cost_usd(model: str, prompt_tokens: int, completion_tokens: int) -> float:
	price_in, price_out = PRICES[model]
	return prompt_tokens * price_in / 1e6 + completion_tokens * price_out / 1e6


class CapReached(RuntimeError):
	pass


class SpendLedger:
	"""Append-only JSON-lines ledger shared by every run; refuses a call that could pass the cap."""

	def __init__(self, path: Path, cap_usd: float = HARD_CAP_USD):
		self.path = Path(path)
		self.cap = min(cap_usd, HARD_CAP_USD)
		self.lock = threading.Lock()
		self.path.parent.mkdir(parents=True, exist_ok=True)

	def total(self) -> float:
		if not self.path.exists():
			return 0.0
		total = 0.0
		for line in self.path.read_text(encoding="utf-8").splitlines():
			if line.strip():
				total += float(json.loads(line).get("usd", 0.0))
		return total

	def reserve_check(self, estimate_usd: float) -> None:
		with self.lock:
			if self.total() + estimate_usd > self.cap:
				raise CapReached(f"spend {self.total():.4f} + estimate {estimate_usd:.4f} would pass cap {self.cap:.2f}")

	def record(self, **entry: Any) -> None:
		entry["ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
		with self.lock:
			with self.path.open("a", encoding="utf-8") as handle:
				handle.write(json.dumps(entry, sort_keys=True) + "\n")


def make_client():
	from openai import OpenAI

	os.environ.pop("OPENAI_ORG_ID", None)
	os.environ.pop("OPENAI_ORGANIZATION", None)
	return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), timeout=240.0, max_retries=0)


def call_json(
	client: Any,
	ledger: SpendLedger,
	*,
	run: str,
	model: str,
	messages: list[dict[str, str]],
	schema_name: str,
	schema: dict[str, Any],
	max_output_tokens: int,
	est_input_tokens: int,
	label: str,
	attempts: int = 4,
) -> tuple[dict[str, Any], dict[str, Any]]:
	"""One strict-schema call with retries and backoff. Returns (parsed_json, usage). Every attempt that bills is recorded."""
	last_error = "unknown"
	reasoning = model.startswith(("gpt-5", "o4", "o3"))
	for attempt in range(1, attempts + 1):
		ledger.reserve_check(cost_usd(model, est_input_tokens, max_output_tokens))
		kwargs: dict[str, Any] = {
			"model": model,
			"messages": messages,
			"response_format": {"type": "json_schema", "json_schema": {"name": schema_name, "strict": True, "schema": schema}},
		}
		if reasoning:
			kwargs["max_completion_tokens"] = max_output_tokens
		else:
			kwargs["max_tokens"] = max_output_tokens
			kwargs["temperature"] = 0
		try:
			response = client.chat.completions.create(**kwargs)
		except Exception as exc:  # network, 429, 5xx: back off and retry
			last_error = f"{type(exc).__name__}: {exc}"[:300]
			time.sleep(min(60, 2 ** attempt) + random.random())
			continue
		usage = {
			"prompt_tokens": int(getattr(response.usage, "prompt_tokens", 0) or 0),
			"completion_tokens": int(getattr(response.usage, "completion_tokens", 0) or 0),
		}
		usage["usd"] = cost_usd(model, usage["prompt_tokens"], usage["completion_tokens"])
		ledger.record(run=run, model=model, label=label, attempt=attempt, **usage)
		choice = response.choices[0]
		content = choice.message.content or ""
		if choice.finish_reason == "length":
			last_error = "output truncated (finish_reason=length)"
			continue
		try:
			return json.loads(content), usage
		except json.JSONDecodeError as exc:
			last_error = f"invalid JSON: {exc}"
			time.sleep(1)
	raise RuntimeError(f"{label}: failed after {attempts} attempts: {last_error}")
