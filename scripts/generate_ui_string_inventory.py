"""Generate a bounded inventory of literal UI text in application source."""

from __future__ import annotations

import argparse
import html
import io
import json
import re
import sys
import tokenize
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
JSON_OUTPUT = PROJECT_ROOT / "docs" / "UI_STRING_INVENTORY.generated.json"
REPORT_OUTPUT = PROJECT_ROOT / "docs" / "UI_STRING_INVENTORY.generated.md"

TEXT_NODE = re.compile(r">([^<>]+)<")
ATTRIBUTE = re.compile(
    r"\b(aria-label|alt|placeholder|title|value)\s*=\s*(['\"])(.*?)\2",
    re.IGNORECASE | re.DOTALL,
)
NON_UI_BLOCK = re.compile(
    r"<!--.*?-->|<style\b[^>]*>.*?</style\s*>|<script\b[^>]*>.*?</script\s*>",
    re.IGNORECASE | re.DOTALL,
)
CODE_MARKERS = re.compile(
    r"(?:=>|===|!==|&&|\|\||\b(?:const|function|return|let|var)\s+[$A-Za-z_][\w$]*|"
    r"document\.(?:querySelector|getElementById)\s*\(|"
    r"\.(?:addEventListener|classList)\b|\bfetch\s*\(|\basync\s+function\b|"
    r"\bawait\s+[$A-Za-z_][\w$]*[.(])"
)

SOURCE_FILES = [
    PROJECT_ROOT / "backend" / "main.py",
    PROJECT_ROOT / "backend" / "routes.py",
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.py")),
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.html")),
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.js")),
]


def _clean_candidate(value: str) -> str | None:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    if not value or not any(character.isalpha() for character in value):
        return None
    if len(value) > 500 or CODE_MARKERS.search(value):
        return None
    if re.search(r"\{[^}]*\}", value) or any(marker in value for marker in ("${", "{{", "}}", "={")):
        return None
    return value


def _python_string_fragments(source_text: str) -> list[tuple[str, int]]:
    """Return string-token contents and starting lines, excluding surrounding code."""
    fragments = []
    for token in tokenize.generate_tokens(io.StringIO(source_text).readline):
        if token.type != tokenize.STRING:
            continue
        raw = token.string
        prefix_match = re.match(r"(?i)[rubf]*", raw)
        prefix_length = prefix_match.end() if prefix_match else 0
        quoted = raw[prefix_length:]
        quote = quoted[:3] if quoted.startswith(("'''", '"""')) else quoted[:1]
        if len(quote) not in (1, 3) or not quoted.endswith(quote):
            continue
        fragments.append((quoted[len(quote):-len(quote)], token.start[0]))
    return fragments


def _remove_non_ui_blocks(source_text: str) -> str:
    return NON_UI_BLOCK.sub(
        lambda match: "\n" * match.group(0).count("\n"),
        source_text,
    )


def extract_source_strings(source_path: Path, source_text: str) -> list[dict[str, str | int]]:
    """Extract visible HTML text nodes and selected literal UI attributes."""
    source = source_path.resolve().relative_to(PROJECT_ROOT).as_posix()
    results: set[tuple[str, int, str, str]] = set()

    if source_path.suffix == ".py":
        fragments = _python_string_fragments(source_text)
    else:
        fragments = [(source_text, 1)]

    for fragment, first_line in fragments:
        searchable = _remove_non_ui_blocks(fragment)
        for match in TEXT_NODE.finditer(searchable):
            value = _clean_candidate(match.group(1))
            if value:
                line = first_line + searchable.count("\n", 0, match.start())
                results.add((value, line, "text", source))

        for match in ATTRIBUTE.finditer(searchable):
            value = _clean_candidate(match.group(3))
            if value:
                line = first_line + searchable.count("\n", 0, match.start())
                results.add((value, line, match.group(1).lower(), source))

    return [
        {"text": text, "line": line, "kind": kind, "source": path}
        for text, line, kind, path in sorted(results, key=lambda row: (row[3], row[1], row[2], row[0]))
    ]


def build_inventory() -> dict[str, object]:
    sources = [path for path in SOURCE_FILES if path.is_file()]
    items: list[dict[str, str | int]] = []
    for path in sources:
        items.extend(extract_source_strings(path, path.read_text(encoding="utf-8")))
    items.sort(key=lambda item: (str(item["source"]), int(item["line"]), str(item["kind"]), str(item["text"])))
    return {
        "title": "Static UI string inventory",
        "coverage": (
            "Literal HTML text nodes and selected literal attributes (aria-label, alt, placeholder, "
            "title, value) found in backend/main.py, backend/routes.py, and backend/pages/*.py, "
            "*.html, and *.js. This is source coverage, not a runtime-complete or deduplicated "
            "catalog. Dynamically generated JavaScript text, data/API-derived labels, strings "
            "assembled from runtime values, and content outside these UI source files are excluded. "
            "Source markup that is conditional or superseded at runtime may still be represented."
        ),
        "sources": [path.relative_to(PROJECT_ROOT).as_posix() for path in sources],
        "item_count": len(items),
        "items": items,
    }


def render_report(inventory: dict[str, object]) -> str:
    items = inventory["items"]
    assert isinstance(items, list)
    lines = [
        "# Static UI string inventory",
        "",
        "Generated by `python scripts/generate_ui_string_inventory.py`. Do not edit this report by hand.",
        "",
        f"- **Extracted occurrences:** {len(items)}",
        f"- **Scanned source files:** {len(inventory['sources'])}",
        f"- **Coverage:** {inventory['coverage']}",
        f"- **Machine-readable output:** [`UI_STRING_INVENTORY.generated.json`](UI_STRING_INVENTORY.generated.json)",
        "",
        "| Source | Line | Kind | Literal |",
        "| --- | ---: | --- | --- |",
    ]
    for item in items:
        source = str(item["source"]).replace("|", "\\|")
        text = str(item["text"]).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| `{source}` | {item['line']} | {item['kind']} | {text} |")
    return "\n".join(lines) + "\n"


def generated_outputs() -> dict[Path, str]:
    inventory = build_inventory()
    return {
        JSON_OUTPUT: json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        REPORT_OUTPUT: render_report(inventory),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated outputs are stale")
    args = parser.parse_args()
    outputs = generated_outputs()
    if args.check:
        stale = [str(path.relative_to(PROJECT_ROOT)) for path, content in outputs.items()
                 if not path.is_file() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("Stale or missing generated UI inventory: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"UI inventory is current ({len(build_inventory()['items'])} extracted occurrences).")
        return 0
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
