"""
Slowly crawl CanLII case pages for a configurable set of citations.

Seed sources (choose one or both):
  --from-prototype       Pull cases_cited from the local prototype cohort in the DB,
                         ranked by citation frequency and filtered to exclude cases
                         already present in the DB.
  --citations-file FILE  CSV or JSONL file with a 'citation' column.

Citation following:
  --depth 1              Hops of citation expansion beyond seeds (0 = seeds only).
                         Expanded citations are also ranked by how often they appear.

Rate / scale limits:
  --limit 50             Max total cases to attempt (across seeds + expanded).
  --delay-ms 5000        Base milliseconds to wait between HTTP requests.
  --jitter 0.3           Fractional random jitter applied to each delay (±30% default).
  --rest-every 10        After every N fetches, pause for --rest-seconds.
  --rest-seconds 45      Duration of the periodic rest pause.

Persistence:
  --checkpoint FILE      JSON file tracking already-fetched/failed citations (for resume).
  --output FILE          JSONL output; records are appended so partial runs are safe.

Dry run:
  --dry-run              Resolve URLs and print plan without fetching anything.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import sys
import time
from collections import Counter, deque
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing dependencies. Run: pip install playwright beautifulsoup4 && playwright install chromium")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select

from backend.database import Case, SessionLocal

# ---------------------------------------------------------------------------
# Citation regex and URL construction
# ---------------------------------------------------------------------------

NEUTRAL_RE = re.compile(
    r"(?P<year>\d{4})\s+(?P<court>SCC|FCA|FCT|FC)\s+(?P<num>\d+)",
    re.IGNORECASE,
)
CANLII_RE = re.compile(
    r"(?P<year>\d{4})\s+CanLII\s+(?P<num>\d+)\s*\((?P<court>SCC|FCA|FCT|FC)\)",
    re.IGNORECASE,
)

# CanLII URL path segment per court
_URL_PATH = {"SCC": "csc-scc", "FCA": "fca", "FC": "fct", "FCT": "fct"}
_COURT_DISPLAY = {
    "SCC": "Supreme Court of Canada",
    "FCA": "Federal Court of Appeal",
    "FC": "Federal Court",
    "FCT": "Federal Court",
}
CANLII_BASE = "https://www.canlii.org"

# CanLII citation links on a case page
_CANLII_DOC_RE = re.compile(
    r"/en/ca/(?:fct|fca|csc-scc)/doc/(\d{4})/(\w+)/(\w+)\.html",
    re.IGNORECASE,
)


def _norm_court(code: str) -> str:
    return code.upper().replace("FCT", "FC")


def _url_path(court_code: str) -> str:
    return _URL_PATH.get(_norm_court(court_code), "")


def neutral_to_url(citation: str) -> str | None:
    m = NEUTRAL_RE.search(citation)
    if not m:
        return None
    year, court, num = m.group("year"), _norm_court(m.group("court")), m.group("num")
    path = _url_path(court)
    if not path:
        return None
    doc_id = f"{year}{court.lower()}{num}"
    return f"{CANLII_BASE}/en/ca/{path}/doc/{year}/{doc_id}/{doc_id}.html"


def canlii_to_url(citation: str) -> str | None:
    m = CANLII_RE.search(citation)
    if not m:
        return None
    year, num, court = m.group("year"), m.group("num"), _norm_court(m.group("court"))
    path = _url_path(court)
    if not path:
        return None
    doc_id = f"{year}canlii{num}"
    return f"{CANLII_BASE}/en/ca/{path}/doc/{year}/{doc_id}/{doc_id}.html"


def citation_to_url(citation: str) -> str | None:
    return neutral_to_url(citation) or canlii_to_url(citation)


def normalize(citation: str) -> str:
    return re.sub(r"\s+", " ", citation.strip()).upper()


def extract_neutral(text: str) -> str | None:
    m = NEUTRAL_RE.search(text)
    if not m:
        return None
    court = _norm_court(m.group("court"))
    return f"{m.group('year')} {court} {m.group('num')}"


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

def _best_full_text(soup: BeautifulSoup) -> str:
    for selector in ("#originalDocument", "#decision", ".contentBody", ".documentContent", "main"):
        for node in soup.select(selector):
            text = node.get_text("\n", strip=True)
            if len(text) > 500:
                return re.sub(r"\n{3,}", "\n\n", text).strip()
    return ""

def _best_full_html(soup: BeautifulSoup) -> str:
    selectors = ["#originalDocument", "#decision", ".contentBody", ".documentcontent", ".documentContent", "main"]
    best = None
    best_length = 0
    for selector in selectors:
        for node in soup.select(selector):
            text_length = len(node.get_text("\n", strip=True))
            if text_length > best_length:
                best = node
                best_length = text_length
    if best is None:
        return ""
    for node in best.find_all(["script", "style", "iframe", "object", "embed", "form"]):
        node.decompose()
    for node in best.find_all(True):
        for attribute in list(node.attrs):
            if attribute.lower().startswith("on"):
                del node.attrs[attribute]
        if node.name == "a":
            node.attrs = {key: value for key, value in node.attrs.items() if key.lower() in {"href", "title", "class", "id"}}
    return best.decode_contents()


def _parse_date(text: str | None) -> date | None:
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            pass
    m = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", text)
    if m:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    return None


def _labeled_value(soup: BeautifulSoup, label: str) -> str | None:
    target = f"{label.strip().lower()}:"
    for node in soup.find_all(string=True):
        if " ".join(str(node).split()).strip().lower() != target:
            continue
        parent = node.parent
        if parent is None:
            continue
        sibling = parent.find_next_sibling()
        if sibling:
            v = sibling.get_text(" ", strip=True)
            if v:
                return v
        v = parent.get_text(" ", strip=True)
        v = re.sub(rf"^{re.escape(label)}\s*:\s*", "", v, flags=re.IGNORECASE).strip()
        if v:
            return v
    return None


def _extract_cited_urls(soup: BeautifulSoup) -> list[str]:
    """Return absolute CanLII doc URLs found in the Cases Cited section."""
    urls: list[str] = []
    seen: set[str] = set()
    # CanLII wraps cited cases in a section with id="citedCases" or similar
    section = soup.find(id=re.compile(r"cited", re.IGNORECASE))
    search_root = section if section else soup
    for a in search_root.find_all("a", href=True):
        href = str(a["href"])
        if _CANLII_DOC_RE.search(href):
            url = href if href.startswith("http") else f"{CANLII_BASE}{href}"
            if url not in seen:
                seen.add(url)
                urls.append(url)
    return urls


def parse_canlii_html(html: str, source_url: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")

    h1 = soup.find("h1")
    heading = h1.get_text(" ", strip=True) if h1 else ""

    title = heading.split(",", 1)[0].strip() if "," in heading else heading
    neutral = extract_neutral(heading)
    court_source = _labeled_value(soup, "Source") or ""
    date_text = _labeled_value(soup, "Date")
    decision_date = _parse_date(date_text)

    full_text = _best_full_text(soup)
    source_html = _best_full_html(soup)
    cited_urls = _extract_cited_urls(soup)

    return {
        "title": title or "Unknown",
        "citation": neutral,
        "court": court_source or "Federal Court",
        "decision_date": decision_date,
        "full_text": full_text,
        "source_html": source_html,
        "cited_urls": cited_urls,
        "source_url": source_url,
    }


# ---------------------------------------------------------------------------
# Checkpoint helpers
# ---------------------------------------------------------------------------

def load_checkpoint(path: Path) -> dict[str, str]:
    """Return {normalized_citation: status} where status ∈ done|failed|skip."""
    if path.exists():
        try:
            return json.loads(path.read_text("utf-8"))
        except Exception:
            pass
    return {}


def save_checkpoint(path: Path, state: dict[str, str]) -> None:
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Seed loading
# ---------------------------------------------------------------------------

def load_prototype_citations() -> list[tuple[str, int]]:
    """Return (citation, frequency) sorted descending, excluding citations already crawled from CanLII."""
    proto_csv = PROJECT_ROOT / "data" / "eval" / "prototype_case_ids_v1.csv"
    if not proto_csv.exists():
        print(f"[warn] Prototype IDs CSV not found: {proto_csv}")
        return []

    ids: list[int] = []
    with proto_csv.open("r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            raw = row.get("case_id", "").strip()
            if raw.isdigit():
                ids.append(int(raw))

    if not ids:
        return []

    db = SessionLocal()
    try:
        freq: Counter[str] = Counter()
        rows = db.scalars(select(Case).where(Case.id.in_(ids)))
        for case in rows:
            for cite in (case.cases_cited or []):
                n = normalize(cite)
                if n:
                    freq[n] += 1

        if not freq:
            return []

        # Only skip citations that were already fetched from CanLII; A2AJ copies are fine to re-fetch
        already_canlii: set[str] = _already_canlii_citations(db)

        ranked = [
            (cite, count)
            for cite, count in freq.most_common()
            if cite not in already_canlii and citation_to_url(cite) is not None
        ]
        skipped = sum(1 for cite, _ in freq.most_common() if cite in already_canlii)
        print(f"[info] {len(ranked)} external citations to fetch, {skipped} already CanLII-crawled (skipped)")
        return ranked
    finally:
        db.close()


def load_prototype_self_citations() -> list[tuple[str, int]]:
    """Return the prototype cohort's own citations for direct CanLII crawling."""
    proto_csv = PROJECT_ROOT / "data" / "eval" / "prototype_case_ids_v1.csv"
    if not proto_csv.exists():
        print(f"[warn] Prototype IDs CSV not found: {proto_csv}")
        return []

    ids: list[int] = []
    with proto_csv.open("r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            raw = row.get("case_id", "").strip()
            if raw.isdigit():
                ids.append(int(raw))

    if not ids:
        return []

    db = SessionLocal()
    try:
        already_canlii = _already_canlii_citations(db)
        rows = db.scalars(select(Case).where(Case.id.in_(ids)))
        results: list[tuple[str, int]] = []
        for case in rows:
            cite = normalize(case.citation or "")
            if cite and cite not in already_canlii and citation_to_url(cite) is not None:
                results.append((cite, 1))
        skipped = sum(1 for case in db.scalars(select(Case).where(Case.id.in_(ids))) if normalize(case.citation or "") in already_canlii)
        print(f"[info] {len(results)} prototype cases to fetch from CanLII, {skipped} already done")
        return results
    finally:
        db.close()


def _already_canlii_citations(db) -> set[str]:
    """Citations/source_ids for DB entries already sourced from CanLII."""
    seen: set[str] = set()
    for (cit, src_id, src_name) in db.execute(
        select(Case.citation, Case.source_id, Case.source_name)
    ):
        if (src_name or "").lower() == "canlii":
            if cit:
                seen.add(normalize(str(cit)))
            if src_id:
                seen.add(normalize(str(src_id)))
    return seen


def load_citations_file(path: Path) -> list[str]:
    """Load from CSV (column 'citation') or JSONL (field 'citation')."""
    citations: list[str] = []
    if path.suffix.lower() in {".jsonl", ".json"}:
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        obj = json.loads(line)
                        c = (obj.get("citation") or "").strip()
                        if c:
                            citations.append(normalize(c))
                    except json.JSONDecodeError:
                        pass
    else:
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            col = next(
                (h for h in (reader.fieldnames or []) if h.lower() == "citation"),
                None,
            ) or (reader.fieldnames or [None])[0]
            for row in reader:
                c = (row.get(col) or "").strip()
                if c:
                    citations.append(normalize(c))
    return citations


# ---------------------------------------------------------------------------
# Crawler
# ---------------------------------------------------------------------------

def build_scraper() -> cloudscraper.CloudScraper:
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )
    scraper.headers.update({
        "Accept-Language": "en-CA,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    })
    return scraper


def _jittered_delay(base_ms: int, jitter: float) -> None:
    """Sleep for base_ms ± jitter fraction, randomized."""
    spread = base_ms * jitter
    actual = base_ms + random.uniform(-spread, spread)
    time.sleep(max(500, actual) / 1000)


# ---------------------------------------------------------------------------
# Browser / fetch (Playwright)
# ---------------------------------------------------------------------------

class BrowserSession:
    """Holds a Playwright browser context open for the duration of a crawl."""

    def __init__(self) -> None:
        self._pw = sync_playwright().__enter__()
        self._browser = self._pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
        )
        self._context = self._browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1366, "height": 768},
            locale="en-CA",
            timezone_id="America/Toronto",
        )
        self._context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self._page = self._context.new_page()

    def fetch(self, url: str, timeout_ms: int = 30_000) -> str:
        try:
            self._page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
        except PlaywrightTimeout as exc:
            raise RuntimeError(f"Page load timeout: {exc}") from exc
        self._page.wait_for_timeout(2500)
        html = self._page.content()
        if "cf-browser-verification" in html or "Just a moment" in html:
            self._page.wait_for_timeout(8000)
            html = self._page.content()
        if "Just a moment" in html or "Enable JavaScript" in html:
            raise RuntimeError("Cloudflare challenge not resolved")
        return html

    def close(self) -> None:
        try:
            self._browser.close()
            self._pw.__exit__(None, None, None)
        except Exception:
            pass


def fetch_url(session: BrowserSession, url: str, delay_ms: int, jitter: float, retries: int = 2) -> str:
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            return session.fetch(url)
        except Exception as exc:
            last_err = exc
            if attempt < retries:
                _jittered_delay(delay_ms * attempt, jitter)
    raise RuntimeError(f"Failed after {retries} attempts: {last_err}")


def url_to_citation(url: str) -> str | None:
    """Best-effort: extract a neutral citation from a CanLII doc URL."""
    m = _CANLII_DOC_RE.search(url)
    if not m:
        return None
    doc_id = m.group(2)  # e.g. 2019fc1234
    nm = re.match(r"(\d{4})(scc|fca|fct|fc|csc)(\d+)", doc_id, re.IGNORECASE)
    if not nm:
        return None
    year, court_raw, num = nm.group(1), nm.group(2).upper(), nm.group(3)
    court = {"FCT": "FC", "CSC": "SCC"}.get(court_raw, court_raw)
    return f"{year} {court} {num}"


def run_crawler(args: argparse.Namespace) -> None:
    # --- collect seeds ---
    seeds: list[tuple[str, int]] = []  # (citation, frequency)
    if args.prototype_self:
        self_seeds = load_prototype_self_citations()
        print(f"[info] {len(self_seeds)} prototype-self citations to fetch")
        seeds.extend(self_seeds)
    if args.from_prototype:
        proto = load_prototype_citations()
        print(f"[info] {len(proto)} prototype external citations ranked by frequency")
        # Merge, keeping higher frequency if duplicate
        existing = {normalize(c): f for c, f in seeds}
        for c, f in proto:
            n = normalize(c)
            if existing.get(n, 0) < f:
                existing[n] = f
        seeds = sorted(existing.items(), key=lambda x: x[1], reverse=True)
    if args.citations_file:
        file_seeds = load_citations_file(Path(args.citations_file))
        print(f"[info] Loaded {len(file_seeds)} citations from {args.citations_file}")
        existing = {normalize(c): f for c, f in seeds}
        for c in file_seeds:
            n = normalize(c)
            if n not in existing:
                existing[n] = 1
        seeds = sorted(existing.items(), key=lambda x: x[1], reverse=True)

    if not seeds:
        sys.exit("[error] No seed citations found. Provide --prototype-self, --from-prototype, or --citations-file.")

    print(f"[info] {len(seeds)} unique seed citations (top 5: {[c for c, _ in seeds[:5]]})") 

    checkpoint_path = Path(args.checkpoint)
    output_path = Path(args.output)
    checkpoint = load_checkpoint(checkpoint_path)

    scraper = BrowserSession() if not args.dry_run else None
    try:
        _run_loop(args, seeds, checkpoint, checkpoint_path, output_path, scraper)
    finally:
        if scraper:
            scraper.close()


def _run_loop(
    args: argparse.Namespace,
    seeds: list[tuple[str, int]],
    checkpoint: dict[str, str],
    checkpoint_path: Path,
    output_path: Path,
    scraper: "BrowserSession | None",
) -> None:

    # BFS queue: (citation_or_url, depth, frequency)
    queue: deque[tuple[str, int, int]] = deque()
    for c, freq in seeds:
        queue.append((c, 0, freq))

    fetched = 0
    attempted: set[str] = set()

    def _key(citation_or_url: str) -> str:
        return normalize(citation_or_url)

    while queue:
        if fetched >= args.limit:
            print(f"[info] Reached limit of {args.limit} cases. Stopping.")
            break

        item, depth, freq = queue.popleft()
        key = _key(item)

        if key in attempted:
            continue
        attempted.add(key)

        if checkpoint.get(key) in {"done", "skip"}:
            continue

        # Resolve URL
        if item.startswith("http"):
            url = item
            citation_label = url_to_citation(url) or item
        else:
            url = citation_to_url(item)
            citation_label = item

        if not url:
            print(f"[skip] Cannot build URL for: {item}")
            checkpoint[key] = "skip"
            save_checkpoint(checkpoint_path, checkpoint)
            continue

        if args.dry_run:
            print(f"[dry-run] depth={depth} freq={freq} {citation_label} -> {url}")
            fetched += 1
            continue

        # Periodic rest pause every N fetches
        if fetched > 0 and fetched % args.rest_every == 0:
            print(f"[rest] Pausing {args.rest_seconds}s after {fetched} fetches...")
            time.sleep(args.rest_seconds)

        print(f"[fetch] depth={depth} freq={freq} ({fetched + 1}/{args.limit}) {citation_label}")
        _jittered_delay(args.delay_ms, args.jitter)

        try:
            html = fetch_url(scraper, url, args.delay_ms, args.jitter)
        except Exception as exc:
            print(f"[fail] {citation_label}: {exc}")
            checkpoint[key] = "failed"
            save_checkpoint(checkpoint_path, checkpoint)
            continue

        try:
            parsed = parse_canlii_html(html, url)
        except Exception as exc:
            print(f"[parse-fail] {citation_label}: {exc}")
            checkpoint[key] = "failed"
            save_checkpoint(checkpoint_path, checkpoint)
            continue

        if not parsed["full_text"]:
            print(f"[skip-empty] {citation_label}: no full text extracted")
            checkpoint[key] = "skip"
            save_checkpoint(checkpoint_path, checkpoint)
            continue

        full_text: str = parsed["full_text"]
        full_text_hash = hashlib.sha256(full_text.encode("utf-8")).hexdigest()
        record: dict[str, Any] = {
            "title": parsed["title"],
            "court": parsed["court"],
            "jurisdiction": "Canada",
            "date": parsed["decision_date"].isoformat() if parsed["decision_date"] else None,
            "citation": parsed["citation"],
            "full_text": full_text,
            "source_html": parsed.get("source_html"),
            "full_text_hash": full_text_hash,
            "source_url": url,
            "source_name": "CanLII",
            "source_id": (parsed["citation"] or full_text_hash)[:255],
            "source_type": args.source_type,
            "upstream_license": "Refer to CanLII Terms of Use",
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "language": "en",
            "processing_status": "raw",
            "metadata_json": {
                "crawl_depth": depth,
                "seed_citation": citation_label,
                "crawl_date": datetime.now(timezone.utc).date().isoformat(),
            },
        }

        with output_path.open("a", encoding="utf-8") as out:
            out.write(json.dumps(record) + "\n")

        checkpoint[key] = "done"
        save_checkpoint(checkpoint_path, checkpoint)
        fetched += 1
        print(f"[ok] {parsed['citation'] or citation_label} — {len(full_text):,} chars")

        # Enqueue cited cases for next depth, ranked by frequency in this page
        if depth < args.depth:
            cited_freq: Counter[str] = Counter(parsed.get("cited_urls", []))
            for cited_url, cite_count in cited_freq.most_common():
                cited_key = _key(cited_url)
                if cited_key not in attempted and checkpoint.get(cited_key) not in {"done", "skip"}:
                    queue.append((cited_url, depth + 1, cite_count))

    print(f"\n[done] Fetched {fetched} cases. Output: {output_path}  Checkpoint: {checkpoint_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    src = parser.add_argument_group("Seed sources")
    src.add_argument("--prototype-self", action="store_true", help="Fetch the 300 core prototype cases themselves from CanLII")
    src.add_argument("--from-prototype", action="store_true", help="Seed from cases cited by the prototype cohort, ranked by frequency")
    src.add_argument("--citations-file", metavar="FILE", help="CSV or JSONL file with a 'citation' column")

    ctl = parser.add_argument_group("Crawl controls")
    ctl.add_argument("--depth", type=int, default=1, metavar="N", help="Citation-following hops (0 = seeds only, default 1)")
    ctl.add_argument("--limit", type=int, default=50, metavar="N", help="Max cases to fetch (default 50)")
    ctl.add_argument("--delay-ms", type=int, default=5000, metavar="MS", help="Base milliseconds between requests (default 5000)")
    ctl.add_argument("--jitter", type=float, default=0.3, metavar="F", help="Delay jitter fraction 0-1 (default 0.3 = ±30%%)")
    ctl.add_argument("--rest-every", type=int, default=10, metavar="N", help="Pause after every N fetches (default 10)")
    ctl.add_argument("--rest-seconds", type=int, default=45, metavar="S", help="Duration of periodic rest pause in seconds (default 45)")
    ctl.add_argument("--source-type", default="canlii_crawl", help="source_type tag written to each record")
    ctl.add_argument("--dry-run", action="store_true", help="Resolve URLs and print plan without fetching")

    out = parser.add_argument_group("Output")
    out.add_argument("--output", default="data/raw/canlii_crawl.jsonl", metavar="FILE", help="JSONL output file (appended)")
    out.add_argument("--checkpoint", default="data/raw/canlii_crawl_checkpoint.json", metavar="FILE", help="Checkpoint file for resume")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_crawler(args)
