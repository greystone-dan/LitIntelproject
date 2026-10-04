#!/usr/bin/env python3
"""Measure generated research-page HTML size without a server or database."""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "page_weight_baseline.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.pages.citation_map import citation_map_html
from backend.pages.data_explorer import data_explorer_page_html
from backend.pages.research import research_page_html


def measure_page(
    name: str, build_html: Callable[[], str]
) -> dict[str, Any]:
    """Measure UTF-8 HTML and its gzip representation."""
    html = build_html()
    html_bytes = html.encode("utf-8")
    gzip_bytes = gzip.compress(html_bytes, compresslevel=6)
    return {
        "name": name,
        "status": "ok",
        "size_bytes": len(html_bytes),
        "size_gzip_bytes": len(gzip_bytes),
        "compression_ratio": round(len(gzip_bytes) / len(html_bytes) * 100, 1),
        "line_count": len(html.splitlines()),
        "script_count": html.count("<script"),
        "style_count": html.count("<style"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="JSON baseline path (default: docs/page_weight_baseline.json)",
    )
    output = parser.parse_args().output

    pages = [
        ("research", research_page_html),
        ("citation_map", citation_map_html),
        ("data_explorer", data_explorer_page_html),
    ]
    measurements = [measure_page(name, build_html) for name, build_html in pages]
    total_html = sum(page["size_bytes"] for page in measurements)
    total_gzip = sum(page["size_gzip_bytes"] for page in measurements)

    print("Page Weight Baseline Report")
    print("=" * 70)
    for page in measurements:
        print(
            f"{page['name']:25} {page['size_bytes']:>8,} bytes"
            f" | gzip: {page['size_gzip_bytes']:>8,} bytes"
            f" | ratio: {page['compression_ratio']:>5}%"
        )
    print("-" * 70)
    ratio = round(total_gzip / total_html * 100, 1) if total_html else 0
    print(f"{'Total':25} {total_html:>8,} bytes | gzip: {total_gzip:>8,} bytes | ratio: {ratio}%")
    print("Methodology: offline generated HTML; UTF-8 bytes; gzip level 6.")
    print("Not measured: browser assets, rendering, runtime, or network latency.")

    report = {
        "version": "1.0",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "methodology": (
            "offline HTML-only measurement; UTF-8 bytes; gzip compression level 6"
        ),
        "pages": measurements,
        "summary": {
            "total_html_bytes": total_html,
            "total_gzip_bytes": total_gzip,
            "average_compression": ratio,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Baseline written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
