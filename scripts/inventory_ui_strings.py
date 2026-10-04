"""Generate a static inventory of literal UI text and route error messages."""

from __future__ import annotations

import argparse
import ast
import io
import json
import re
import sys
import tokenize
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
JSON_OUTPUT = PROJECT_ROOT / "docs" / "reports" / "ui-strings.json"
REPORT_OUTPUT = PROJECT_ROOT / "docs" / "reports" / "french-ui-inventory.md"
PLACEHOLDER = re.compile(r"\{[^{}\s]+\}|\$\{[^}]+\}|%\([^)]+\)[sd]|%[sd]")
TEMPLATE_KEY = re.compile(r"\{\{\s*[a-z][a-z0-9_.-]*\s*\}\}")
CODE_MARKERS = re.compile(
    r"(?:=>|===|!==|&&|\|\||\b(?:const|function|return|let|var)\s+[$A-Za-z_][\w$]*|"
    r"document\.(?:querySelector|getElementById)\s*\(|"
    r"\.(?:addEventListener|classList)\b|\bfetch\s*\(|"
    r"\b(?:async|await)\s+[$A-Za-z_][\w$]*[.(])"
)
JS_UI_ASSIGNMENT = re.compile(
    r"""\b(?:textContent|innerHTML|ariaLabel|title|placeholder)\s*=\s*(['"`])"""
)

SOURCE_FILES = [
    PROJECT_ROOT / "backend" / "routes.py",
    PROJECT_ROOT / "backend" / "i18n.py",
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.py")),
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.html")),
    *sorted((PROJECT_ROOT / "backend" / "pages").glob("*.js")),
]


def _clean_candidate(value: str) -> str | None:
    value = unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    if not value or TEMPLATE_KEY.fullmatch(value):
        return None
    if not any(character.isalpha() for character in value):
        return None
    if len(value) > 1000 or CODE_MARKERS.search(value):
        return None
    return value


def _python_string_fragments(source_text: str) -> list[tuple[str, int]]:
    fragments = []
    for token in tokenize.generate_tokens(io.StringIO(source_text).readline):
        if token.type != tokenize.STRING:
            continue
        raw = token.string
        prefix_match = re.match(r"(?i)[rubf]*", raw)
        prefix_length = prefix_match.end() if prefix_match else 0
        quoted = raw[prefix_length:]
        quote = quoted[:3] if quoted.startswith(("'''", '"""')) else quoted[:1]
        if len(quote) in (1, 3) and quoted.endswith(quote):
            fragments.append((quoted[len(quote):-len(quote)], token.start[0]))
    return fragments


class _UIHTMLParser(HTMLParser):
    def __init__(self, source: str, first_line: int, source_file: str):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.first_line = first_line
        self.source_file = source_file
        self.stack: list[str] = []
        self.hidden_depth = 0
        self.items: list[dict[str, str | int | bool]] = []

    def _add(self, value: str, kind: str, line: int) -> None:
        text = _clean_candidate(value)
        if text:
            self.items.append({
                "file": self.source_file,
                "line": self.first_line + line - 1,
                "string": text,
                "context_kind": kind,
                "contains_placeholders": bool(PLACEHOLDER.search(text)),
            })

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        line = self.getpos()[0]
        if tag in ("script", "style"):
            self.hidden_depth += 1
        if not tag.endswith("/"):
            self.stack.append(tag)
        for name, value in attrs:
            if value is None:
                continue
            if name == "aria-label":
                kind = "aria-label"
            elif name == "title":
                kind = "tooltip"
            elif name in ("alt", "placeholder", "value"):
                kind = "button" if tag == "button" or (
                    tag == "input" and dict(attrs).get("type") in ("button", "submit")
                ) else "label"
            else:
                continue
            self._add(value, kind, line)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self.hidden_depth:
            self.hidden_depth -= 1
        if tag in self.stack:
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[index:]

    def handle_data(self, data: str) -> None:
        if self.hidden_depth:
            return
        line = self.getpos()[0]
        if "title" in self.stack:
            kind = "tooltip"
        elif self.stack and re.fullmatch(r"h[1-6]", self.stack[-1]):
            kind = "heading"
        elif "button" in self.stack:
            kind = "button"
        elif "label" in self.stack:
            kind = "label"
        else:
            kind = "label"
        self._add(data, kind, line)


def _relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def _js_assigned_text(fragment: str, first_line: int) -> list[tuple[str, int]]:
    found = []
    cursor = 0
    while match := JS_UI_ASSIGNMENT.search(fragment, cursor):
        quote = match.group(1)
        start = match.end()
        index = start
        value = []
        while index < len(fragment):
            character = fragment[index]
            if character == "\\" and index + 1 < len(fragment):
                value.extend((character, fragment[index + 1]))
                index += 2
            elif character == quote:
                break
            else:
                value.append(character)
                index += 1
        if index >= len(fragment):
            cursor = start
            continue
        found.append(("".join(value), first_line + fragment.count("\n", 0, match.start())))
        cursor = index + 1
    return found


def _route_errors(source_path: Path, source_text: str, root: Path) -> list[dict[str, str | int | bool]]:
    if source_path.name != "routes.py":
        return []
    tree = ast.parse(source_text, filename=str(source_path))
    source_file = _relative_path(source_path, root)
    items = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if node.func.id != "HTTPException":
            continue
        detail = next((keyword.value for keyword in node.keywords if keyword.arg == "detail"), None)
        if detail is None:
            continue
        if isinstance(detail, ast.Dict):
            visible_values = [
                value for key, value in zip(detail.keys, detail.values)
                if isinstance(key, ast.Constant) and key.value in ("message", "error", "detail")
            ]
        else:
            visible_values = [detail]
        for child in (node for value in visible_values for node in ast.walk(value)):
            if isinstance(child, ast.Constant) and isinstance(child.value, str):
                text = _clean_candidate(child.value)
                if text:
                    items.append({
                        "file": source_file,
                        "line": child.lineno,
                        "string": text,
                        "context_kind": "error",
                        "contains_placeholders": bool(PLACEHOLDER.search(text)),
                    })
    return items


def _english_catalog_strings(
    source_path: Path, source_text: str, root: Path
) -> list[dict[str, str | int | bool]]:
    if source_path.name != "i18n.py":
        return []
    tree = ast.parse(source_text, filename=str(source_path))
    messages = next(
        (
            node.value
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "MESSAGES" for target in node.targets)
        ),
        None,
    )
    if not isinstance(messages, ast.Dict):
        return []
    english_catalog = next(
        (
            value
            for key, value in zip(messages.keys, messages.values)
            if isinstance(key, ast.Constant) and key.value == "en"
        ),
        None,
    )
    if not isinstance(english_catalog, ast.Dict):
        return []
    source_file = _relative_path(source_path, root)
    items = []
    for key, value in zip(english_catalog.keys, english_catalog.values):
        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
            continue
        if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
            continue
        text = _clean_candidate(value.value)
        if text:
            items.append({
                "file": source_file,
                "line": value.lineno,
                "string": text,
                "context_kind": "heading" if key.value == "about.title" else "label",
                "contains_placeholders": bool(PLACEHOLDER.search(text)),
            })
    return items


def extract_source_strings(
    source_path: Path,
    source_text: str,
    root: Path = PROJECT_ROOT,
) -> list[dict[str, str | int | bool]]:
    """Extract visible literal text and selected runtime UI/error messages."""
    source_file = _relative_path(source_path, root)
    suffix = source_path.suffix.lower()
    fragments = _python_string_fragments(source_text) if suffix == ".py" else [(source_text, 1)]
    results: set[tuple[str, int, str, str, bool]] = set()

    for fragment, first_line in fragments:
        if suffix != ".py" or "<" in fragment:
            parser = _UIHTMLParser(fragment, first_line, source_file)
            parser.feed(fragment)
            for item in parser.items:
                results.add((
                    str(item["file"]), int(item["line"]), str(item["string"]),
                    str(item["context_kind"]), bool(item["contains_placeholders"]),
                ))
        for assigned_text, line in _js_assigned_text(fragment, first_line):
            text = _clean_candidate(assigned_text)
            if text:
                results.add((
                    source_file, line, text, "label", bool(PLACEHOLDER.search(text)),
                ))

    extracted = [
        {
            "file": file,
            "line": line,
            "string": text,
            "context_kind": kind,
            "contains_placeholders": placeholders,
        }
        for file, line, text, kind, placeholders in results
    ]
    extracted.extend(_route_errors(source_path, source_text, root))
    extracted.extend(_english_catalog_strings(source_path, source_text, root))
    return sorted(
        extracted,
        key=lambda item: (
            str(item["file"]), int(item["line"]), str(item["context_kind"]), str(item["string"])
        ),
    )


def find_concatenations(source_paths: list[Path], root: Path = PROJECT_ROOT) -> list[dict[str, str | int]]:
    """Find source-level Python string concatenations that complicate localization."""
    found: set[tuple[str, int, str]] = set()
    for path in source_paths:
        if path.suffix != ".py" or path.parent.name != "pages":
            continue
        text = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(text, filename=str(path))
        except SyntaxError:
            continue
        parents = {
            child: parent
            for parent in ast.walk(tree)
            for child in ast.iter_child_nodes(parent)
        }
        for node in ast.walk(tree):
            if not isinstance(node, ast.BinOp) or not isinstance(node.op, ast.Add):
                continue
            parent = parents.get(node)
            if isinstance(parent, ast.BinOp) and isinstance(parent.op, ast.Add):
                continue
            if not any(isinstance(child, ast.Constant) and isinstance(child.value, str)
                       for child in ast.walk(node)):
                continue
            expression = ast.get_source_segment(text, node)
            if not expression or not any(char.isalpha() for char in expression):
                continue
            expression = re.sub(r"\s+", " ", expression).strip()
            if len(expression) > 180:
                expression = expression[:177] + "..."
            found.add((_relative_path(path, root), node.lineno, expression))
    return [
        {"file": file, "line": line, "expression": expression}
        for file, line, expression in sorted(found)
    ]


def build_inventory(source_paths: list[Path] | None = None, root: Path = PROJECT_ROOT) -> dict[str, object]:
    paths = source_paths if source_paths is not None else [path for path in SOURCE_FILES if path.is_file()]
    items: list[dict[str, str | int | bool]] = []
    for path in paths:
        items.extend(extract_source_strings(path, path.read_text(encoding="utf-8"), root))
    items.sort(key=lambda item: (
        str(item["file"]), int(item["line"]), str(item["context_kind"]), str(item["string"])
    ))
    return {
        "coverage": (
            "Static source inventory of literal HTML text, selected accessibility/form attributes, "
            "JavaScript DOM text assignments, literal English catalog messages, and literal "
            "FastAPI HTTPException details in backend/pages/*, backend/i18n.py, and "
            "backend/routes.py. Runtime-generated/API-derived text and "
            "messages assembled entirely from variables require manual review."
        ),
        "item_count": len(items),
        "items": items,
        "concatenations": find_concatenations(paths, root),
        "sources": [_relative_path(path, root) for path in paths],
    }


def render_report(inventory: dict[str, object]) -> str:
    items = inventory["items"]
    concatenations = inventory["concatenations"]
    assert isinstance(items, list) and isinstance(concatenations, list)
    counts = Counter(str(item["file"]) for item in items)
    lines = [
        "# French-language UI string inventory",
        "",
        "Generated by `python scripts/inventory_ui_strings.py`. Do not edit by hand.",
        "",
        f"- **Extracted occurrences:** {len(items)}",
        f"- **Scanned files:** {len(inventory['sources'])}",
        f"- **Coverage:** {inventory['coverage']}",
        "- **Machine-readable output:** [`ui-strings.json`](ui-strings.json)",
        "",
        (
            "This is a reproducible static-source inventory, not a claim that runtime-generated "
            "or API-provided content has been exhaustively translated. Review the listed sources "
            "and test rendered pages before extending localization."
        ),
        "",
        "## Occurrences by page/source",
        "",
        "| Page/source | Occurrences |",
        "| --- | ---: |",
    ]
    lines.extend(f"| `{file}` | {count} |" for file, count in sorted(counts.items()))
    lines.extend([
        "",
        "## Strings assembled by concatenation",
        "",
        (
            f"Found **{len(concatenations)}** Python string-concatenation expression(s) in scanned "
            "page/route sources. These require review because translators cannot safely reorder "
            "fragments or adjust grammar across English-only code boundaries."
        ),
        "",
        "| File | Line | Expression |",
        "| --- | ---: | --- |",
    ])
    for item in concatenations:
        expression = str(item["expression"]).replace("|", "\\|").replace("`", "'")
        lines.append(f"| `{item['file']}` | {item['line']} | `{expression}` |")
    lines.extend([
        "",
        "## Recommended implementation approach",
        "",
        (
            "Use a message catalog keyed by stable IDs, with English as the source language and "
            "French values reviewed by a fluent Canadian French speaker. Resolve locale in this "
            "order: an explicit `?lang=fr` URL override, then `Accept-Language`, then English; "
            "include an accessible language toggle in the shared header. Keep placeholders named "
            "and consistent between locales, escape inserted text, and test catalog parity and "
            "English output compatibility."
        ),
        "",
        (
            "The About-page proof of concept is intentionally limited. Its French values are "
            "machine-drafted and require fluent-speaker review; no legal terminology is represented "
            "as final."
        ),
        "",
        "## Terminology glossary for human review",
        "",
        "| English term | Draft French / question for reviewer |",
        "| --- | --- |",
        "| outcome | Résultat / issue? Confirm preferred case-outcome term in context. |",
        "| Minister | ministre / ministre de la Sécurité publique? Confirm the intended party and capitalization. |",
        "| judicial review | contrôle judiciaire; confirm against current Canadian immigration-law usage. |",
        "| leave (to appeal / judicial review) | autorisation; distinguish procedural leave from ordinary permission. |",
        "| stay (of removal / proceedings) | sursis; confirm the specific legal context. |",
        "| Federal Court | Cour fédérale; verify official institutional naming in each context. |",
        "",
        "## Full string inventory",
        "",
        "| File | Line | Context | Placeholders | String |",
        "| --- | ---: | --- | --- | --- |",
    ])
    for item in items:
        text = str(item["string"]).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| `{item['file']}` | {item['line']} | {item['context_kind']} | "
            f"{'yes' if item['contains_placeholders'] else 'no'} | {text} |"
        )
    return "\n".join(lines) + "\n"


def generated_outputs() -> dict[Path, str]:
    inventory = build_inventory()
    return {
        JSON_OUTPUT: json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        REPORT_OUTPUT: render_report(inventory),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated reports are stale")
    args = parser.parse_args()
    outputs = generated_outputs()
    if args.check:
        stale = [str(path.relative_to(PROJECT_ROOT)) for path, content in outputs.items()
                 if not path.is_file() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("Stale or missing UI inventory reports: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"UI inventory is current ({build_inventory()['item_count']} occurrences).")
        return 0
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
