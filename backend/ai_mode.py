"""Central configuration for optional AI-backed features."""

from __future__ import annotations

import os


VALID_ENHANCED_AI_MODES = frozenset({"off", "local", "hosted"})
AI_DISABLED_MESSAGE = "AI answers are disabled in this deployment"


def enhanced_mode() -> str:
	"""Return the configured mode, rejecting unsupported values."""
	mode = os.getenv("ENHANCED_AI_MODE", "off").strip().lower()
	if mode not in VALID_ENHANCED_AI_MODES:
		raise ValueError("ENHANCED_AI_MODE must be one of: off, local, hosted")
	return mode


def mode_status() -> dict[str, str]:
	return {"enhanced_ai_mode": enhanced_mode()}


def search_downgrade_reason(requested_mode: str, effective_mode: str) -> str | None:
	if requested_mode not in {"semantic", "hybrid"} or effective_mode == requested_mode:
		return None
	mode = enhanced_mode()
	if mode == "off":
		return "Enhanced AI mode is off; lexical search was used."
	if mode == "local":
		return "Hosted semantic search is unavailable in local mode; lexical search was used."
	return None
