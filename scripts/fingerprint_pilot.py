"""Read-only pilot: fingerprint a random sample of real cases and see whether the sample conclusions hold.

Reads cases.full_text (SELECT only, in a read-only transaction, one connection, lowest process priority,
throttled), computes case fingerprints in memory, and writes everything to files. It writes nothing to
the database. Output (default ``data/eval/case_fingerprints/pilot/``):

* ``fingerprints.jsonl``  one fingerprint per sampled case (terms, authorities, seconds)
* ``pilot-report.md``     timing, neighbours for the landmark cases and 20 random cases, and the
                          150 hand-labelled pairs re-scored on this library
* ``pilot-results.json``  the same numbers, machine readable

Run it from the repo folder, for example::

    ./venv/Scripts/python.exe scripts/fingerprint_pilot.py --fc 1200 --fca 500 --scc 300
"""

from __future__ import annotations

import argparse
import collections
import json
import random
import statistics
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
from sqlalchemy import func, select, text
from sqlalchemy.orm import Session

from backend.batch_safety import lower_process_priority, throttle_sleep
from backend.case_fingerprint import FINGERPRINT_VERSION, CaseFingerprint, FingerprintIndex, compute_fingerprint
from backend.database import Case

COURT_LABELS = {
    "FC": ("FC", "FEDERAL COURT"),
    "FCA": ("FCA", "FEDERAL COURT OF APPEAL"),
    "SCC": ("SCC", "SUPREME COURT OF CANADA"),
}
LANDMARKS = ["2019 SCC 65", "[1999] 2 SCR 817", "2008 SCC 9", "2009 SCC 12", "2002 SCC 1", "2015 SCC 61"]
DEFAULT_GOLD = [
    "data/eval/case_fingerprints/gold_pairs_block1.json",
    "data/eval/case_fingerprints/gold_pairs_block2.json",
]


def _court_ids(session: Session, court_key: str) -> list[int]:
    labels = COURT_LABELS[court_key]
    stmt = select(Case.id).where(Case.full_text.is_not(None)).where(func.upper(Case.court).in_(labels))
    ids = [row for row in session.scalars(stmt)]
    session.rollback()  # end the transaction: batch_safety kills ones idle over 30 s
    return ids


def _find_case(session: Session, citation: str) -> int | None:
    stmt = select(Case.id).where(Case.citation.ilike(f"%{citation}%")).order_by(Case.id).limit(1)
    found = session.scalar(stmt)
    session.rollback()
    return found


def _load_gold(paths: list[str]) -> list[dict]:
    pairs: list[dict] = []
    for path in paths:
        file = Path(path)
        if not file.is_absolute():
            file = PROJECT_ROOT / file
        if file.exists():
            pairs.extend(json.loads(file.read_text(encoding="utf-8")))
    return pairs


def _auc(scores: np.ndarray, positive: np.ndarray) -> float | None:
    """Rank-sum AUC with tied scores sharing their average rank."""
    n_pos = int(positive.sum())
    n_neg = len(positive) - n_pos
    if n_pos == 0 or n_neg == 0:
        return None
    order = np.argsort(scores, kind="stable")
    sorted_scores = scores[order]
    ranks = np.empty(len(scores))
    i = 0
    while i < len(scores):
        j = i
        while j + 1 < len(scores) and sorted_scores[j + 1] == sorted_scores[i]:
            j += 1
        ranks[order[i : j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return float((ranks[positive].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def run(session: Session, options: argparse.Namespace) -> dict:
    try:
        session.execute(text("SET TRANSACTION READ ONLY"))
    except Exception:  # noqa: BLE001 - only Postgres needs it; the script only ever SELECTs anyway
        session.rollback()
    rng = random.Random(options.seed)
    wanted: dict[int, str] = {}
    pool_sizes = {}
    for key, count in (("FC", options.fc), ("FCA", options.fca), ("SCC", options.scc)):
        ids = _court_ids(session, key)
        pool_sizes[key] = len(ids)
        for case_id in rng.sample(ids, min(count, len(ids))):
            wanted[case_id] = "sample"
    gold = _load_gold(options.gold)
    missing_gold: set[str] = set()
    forced: dict[str, int] = {}
    for citation in LANDMARKS + [c for pair in gold for c in (pair["a"], pair["b"])]:
        if citation in forced or citation in missing_gold:
            continue
        found = _find_case(session, citation)
        if found is None:
            missing_gold.add(citation)
        else:
            forced[citation] = found
            wanted.setdefault(found, "forced")

    rows: list[dict] = []
    seconds_by_court: dict[str, list[float]] = collections.defaultdict(list)
    started = time.time()
    for n, case_id in enumerate(sorted(wanted), 1):
        row = session.execute(
            select(Case.id, Case.title, Case.court, Case.citation, func.substr(Case.full_text, 1, options.max_chars))
            .where(Case.id == case_id)
        ).one_or_none()
        session.rollback()  # no open transaction while computing/sleeping (idle > 30 s gets killed)
        if row is None or not row[4]:
            continue
        work_start = time.time()
        fingerprint = compute_fingerprint(row[4], own_citation=row[3])
        work = time.time() - work_start
        seconds_by_court[(row[2] or "?").upper()].append(work)
        rows.append({
            "id": row[0], "title": row[1], "court": row[2], "citation": row[3], "seconds": round(work, 3),
            "chars": len(row[4]), "terms": fingerprint.terms, "authorities": fingerprint.authorities,
            "length": fingerprint.length, "role_chars": fingerprint.role_chars,
        })
        if n % 100 == 0:
            print(f"{n}/{len(wanted)} cases, {time.time() - started:.0f}s elapsed", flush=True)
        time.sleep(throttle_sleep(work, options.base_sleep, options.max_duty))
    session.rollback()  # read-only: nothing to commit

    out_dir = Path(options.out_dir)
    if not out_dir.is_absolute():
        out_dir = PROJECT_ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "fingerprints.jsonl").open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    index = FingerprintIndex(
        [(r["id"], CaseFingerprint(FINGERPRINT_VERSION, r["terms"], r["authorities"], r["length"], r["role_chars"])) for r in rows]
    )
    by_id = {r["id"]: r for r in rows}

    def label(case_id: int) -> str:
        r = by_id[case_id]
        return f"{(r['title'] or '')[:60]} ({r['citation']}, {r['court']})"

    report = ["# Fingerprint pilot (read-only)", "", f"Fingerprinted {len(rows)} cases ({FINGERPRINT_VERSION}); pools: {pool_sizes}; seed {options.seed}.", ""]
    timing = {}
    report += ["## Time per case", "", "| Court | n | mean s | median s | max s |", "|---|---|---|---|---|"]
    for court, values in sorted(seconds_by_court.items()):
        timing[court] = {"n": len(values), "mean": round(statistics.mean(values), 2), "median": round(statistics.median(values), 2), "max": round(max(values), 1)}
        report.append(f"| {court} | {len(values)} | {timing[court]['mean']} | {timing[court]['median']} | {timing[court]['max']} |")
    report.append(f"\nTotal compute {sum(r['seconds'] for r in rows):.0f}s; wall time {time.time() - started:.0f}s (throttled).\n")

    landmark_ids = [forced[c] for c in LANDMARKS if c in forced and forced[c] in by_id]
    others = rng.sample([r["id"] for r in rows if r["id"] not in landmark_ids], min(20, max(0, len(rows) - len(landmark_ids))))
    report.append("## Neighbours (subject = tags+statutes+roles; authorities = separate list)\n")
    neighbours = {}
    for case_id in landmark_ids + others:
        subject = index.similar_by_subject(case_id, 8)
        shared = index.shares_authorities(case_id, 8)
        neighbours[case_id] = {"subject": subject, "authorities": shared}
        report.append(f"### {label(case_id)}\n\n**Similar by subject**\n")
        for other, score in subject:
            terms = ", ".join(t.split(":", 1)[1] for t, _ in index.explain_subject(case_id, other, 3))
            report.append(f"- {label(other)} {score:.2f} (shared: {terms})")
        report.append("\n**Shares authorities**\n")
        for other, score in shared:
            report.append(f"- {label(other)} {score:.2f}")
        report.append("")

    gold_result: dict = {}
    usable = [p for p in gold if p["a"] in forced and p["b"] in forced and forced[p["a"]] in by_id and forced[p["b"]] in by_id]
    if usable:
        labels = np.array([p["label"] for p in usable])
        subject_scores = np.array([index.subject_percentile(forced[p["a"]], forced[p["b"]]) for p in usable])
        auth_scores = np.array([index.authority_percentile(forced[p["a"]], forced[p["b"]]) for p in usable])
        blend = (subject_scores + auth_scores) / 2
        report += ["## Hand-labelled pairs re-scored on this library", "", f"{len(usable)} of {len(gold)} pairs found; {sorted(missing_gold)[:10]} not found.", "", "| Ranking | AUC same-issue | AUC same-family |", "|---|---|---|"]
        for name, scores in (("Similar by subject", subject_scores), ("Shares authorities", auth_scores), ("Blend", blend)):
            same_issue, family = _auc(scores, labels == 2), _auc(scores, labels >= 1)
            gold_result[name] = {"same_issue": same_issue, "family": family}
            report.append(f"| {name} | {same_issue if same_issue is None else round(same_issue, 3)} | {family if family is None else round(family, 3)} |")
        gold_result["pairs_used"] = len(usable)
    results = {"cases": len(rows), "pools": pool_sizes, "timing": timing, "gold": gold_result, "missing_gold": sorted(missing_gold)}
    (out_dir / "pilot-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    (out_dir / "pilot-results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
    print(f"wrote {out_dir}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fc", type=int, default=1200)
    parser.add_argument("--fca", type=int, default=500)
    parser.add_argument("--scc", type=int, default=300)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--max-chars", type=int, default=250_000, help="read at most this many characters of each decision")
    parser.add_argument("--max-duty", type=float, default=0.7, help="share of time the job may spend working (0-1)")
    parser.add_argument("--base-sleep", type=float, default=0.05)
    parser.add_argument("--gold", nargs="*", default=DEFAULT_GOLD)
    parser.add_argument("--out-dir", default="data/eval/case_fingerprints/pilot")
    options = parser.parse_args()
    print("priority:", lower_process_priority())
    from backend.batch_safety import make_limited_engine
    from backend.database import engine

    limited = make_limited_engine(engine.url, statement_timeout_ms=60_000, application_name="ilit-fingerprint-pilot")
    with Session(limited) as session:
        run(session, options)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
