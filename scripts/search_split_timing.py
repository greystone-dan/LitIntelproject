"""Read-only timing of the two requests a search makes, separately: the results list and the facet counts.

The data-explorer page first asks /analytics/search/cases (facets and citation stats off) and, once the results are
shown, /analytics/search/facets with the same filters. This sends exactly those two requests to a running site and
prints how long each takes, twice per query. Only GET requests; it reads no keys and writes nothing.
Note: the site keeps facet answers for 10 minutes, so run 2 of the facets request is normally a cache hit.

    python scripts/search_split_timing.py --base http://127.0.0.1:8001 --out search_split_timing.txt
"""

from __future__ import annotations

import argparse
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

QUERIES = ["reasonableness", "Baker"]


def get(url: str) -> tuple[float, int, int]:
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=120) as response:
            body = response.read()
            status = response.status
    except urllib.error.HTTPError as error:
        body, status = error.read(), error.code
    return time.perf_counter() - started, status, len(body)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", default="http://127.0.0.1:8001")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--queries", nargs="*", default=QUERIES)
    args = parser.parse_args()
    lines = [f"base={args.base}  (seconds; status; response bytes)"]
    for query in args.queries:
        results = urllib.parse.urlencode(
            {"query": query, "sort_by": "relevance", "limit": 50, "facets": 0, "citation_stats": 0}
        )
        facets = urllib.parse.urlencode({"query": query})
        for run in (1, 2):
            r_time, r_status, r_size = get(f"{args.base}/analytics/search/cases?{results}")
            f_time, f_status, f_size = get(f"{args.base}/analytics/search/facets?{facets}")
            lines.append(
                f"{query!r} run {run}: results {r_time:.2f} s ({r_status}, {r_size} B) | "
                f"facets {f_time:.2f} s ({f_status}, {f_size} B) | page shows results after {r_time:.2f} s"
            )
            print(lines[-1])
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
