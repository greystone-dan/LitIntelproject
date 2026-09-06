"""Fail-closed policy for ProjectManagerGAME operations."""

from __future__ import annotations

import re
from pathlib import Path

GAME_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_EXECUTABLES = {"python", "python.exe", "node", "node.exe"}
DENIED_TOKENS = {
    "git",
    "powershell",
    "pwsh",
    "cmd",
    "bash",
    "sh",
    "curl",
    "wget",
    "invoke-webrequest",
    "invoke-restmethod",
    "start-process",
}
SHELL_TOKENS = re.compile(r"[;&|<>`$]|\\r|\\n")


def confined_path(path: str | Path) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = GAME_ROOT / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(GAME_ROOT)
    except ValueError as error:
        raise PermissionError(f"path outside browser_game boundary: {path}") from error
    return resolved


def validate_command(command: list[str], cwd: str | Path = GAME_ROOT) -> list[str]:
    if not command:
        raise PermissionError("empty command denied")
    confined_path(cwd)
    executable = Path(command[0]).name.lower()
    if executable not in ALLOWED_EXECUTABLES:
        raise PermissionError(f"executable not allowed: {executable}")
    for argument in command:
        lowered = argument.lower()
        if SHELL_TOKENS.search(argument):
            raise PermissionError("shell syntax denied")
        if lowered in DENIED_TOKENS:
            raise PermissionError(f"command token denied: {argument}")
        if ".." in Path(argument).parts or argument.startswith(("/", "\\")):
            raise PermissionError(f"path argument denied: {argument}")
    return command


def validate_write(path: str | Path) -> Path:
    return confined_path(path)
