"""Shared skip-to-content behavior for standalone generated pages."""

import re
from functools import wraps
from typing import Callable, TypeVar


Builder = TypeVar("Builder", bound=Callable[..., str])

_SKIP_LINK_STYLE = """
<style>
.skip-link{position:absolute;left:1rem;top:-5rem;z-index:10000;padding:.65rem 1rem;
background:#fff;color:#111;border:2px solid #111;font:inherit}
.skip-link:focus{top:1rem}
</style>
"""


def ensure_skip_link(html: str) -> str:
    """Add one visible-on-focus link and its keyboard-focusable destination."""
    if re.search(
        r'<a\b[^>]*\bclass\s*=\s*["\'][^"\']*\bskip-link\b[^"\']*["\']',
        html,
        re.IGNORECASE,
    ):
        return html

    body_match = re.search(r"<body\b[^>]*>", html, re.IGNORECASE)
    if body_match is None:
        raise ValueError("Standalone page builder output is missing a body element")

    target_match = re.search(r"<main\b[^>]*>", html, re.IGNORECASE)
    if target_match is None:
        target_match = re.search(r"<h1\b[^>]*>", html, re.IGNORECASE)
    if target_match is None:
        raise ValueError("Standalone page builder output has no main or h1 target")

    target_tag = target_match.group(0)
    id_match = re.search(r"(?<![\w:-])id\s*=\s*(['\"])(.*?)\1", target_tag, re.IGNORECASE)
    target_id = id_match.group(2) if id_match else "main-content"
    if id_match is None:
        target_tag = target_tag[:-1] + f' id="{target_id}">'
    if not re.search(r"\btabindex\s*=", target_tag, re.IGNORECASE):
        target_tag = target_tag[:-1] + ' tabindex="-1">'
    html = html[: target_match.start()] + target_tag + html[target_match.end() :]

    link = f'<a class="skip-link" href="#{target_id}">Skip to main content</a>'
    body_match = re.search(r"<body\b[^>]*>", html, re.IGNORECASE)
    html = html[: body_match.end()] + "\n" + link + html[body_match.end() :]

    head_close = re.search(r"</head\s*>", html, re.IGNORECASE)
    if head_close:
        html = html[: head_close.start()] + _SKIP_LINK_STYLE + html[head_close.start() :]
    return html


def with_skip_link(builder: Builder) -> Builder:
    """Decorate a complete page builder with the shared skip-link primitive."""

    @wraps(builder)
    def wrapped(*args, **kwargs):
        return ensure_skip_link(builder(*args, **kwargs))

    return wrapped  # type: ignore[return-value]
