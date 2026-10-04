"""Load versioned prompt text from the adjacent prompts directory."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import re


_PROMPT_DIR = Path(__file__).with_name("prompts")
_PROMPT_NAME = re.compile(r"[a-z0-9_]+")
_VERSION_HEADER = re.compile(r"# prompt_version: (v[0-9]+)\n\n")


@lru_cache(maxsize=None)
def get_prompt(name: str) -> tuple[str, str]:
    """Return an immutable prompt body and its header-declared version."""
    if not _PROMPT_NAME.fullmatch(name):
        raise ValueError(f"invalid prompt name: {name!r}")
    path = _PROMPT_DIR / f"{name}.txt"
    raw_text = path.read_text(encoding="utf-8")
    match = _VERSION_HEADER.match(raw_text)
    if match is None:
        raise ValueError(f"prompt {name!r} has no valid version header")
    text = raw_text[match.end() :]
    if text.endswith("\n"):
        text = text[:-1]
    return text, match.group(1)
