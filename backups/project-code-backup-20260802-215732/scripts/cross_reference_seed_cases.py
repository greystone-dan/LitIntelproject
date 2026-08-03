from __future__ import annotations

import argparse
import re
from pathlib import Path
import sys

import pandas as pd
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cross-reference seed cases against core set and local DB.")
    parser.add_argument("--seed-csv", type=Path, default=Path("data/eval/seed_cases_extracted.csv"))
    parser.add_argument("--core-csv", type=Path, default=Path("data/eval/core_immigration_cases.csv"))
    parser.add_argument("--out-csv", type=Path, default=Path("data/eval/reports/seed_case_cross_reference_100.csv"))
    return parser.parse_args()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_name(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"\s*\([^)]*\)", "", lowered)
    lowered = lowered.replace("\u2019", "'").replace("\u2011", "-")
    lowered = re.sub(r"[^a-z0-9\s\-]", " ", lowered)
    lowered = normalize_space(lowered)
    return lowered


def extract_neutral_citation(listed_citation: str) -> str:
    patterns = [
        r"\b\d{4}\s+SCC\s+\d+\b",
        r"\b\d{4}\s+FCA\s+\d+\b",
        r"\b\d{4}\s+FC\s+\d+\b",
        r"\b\d{4}\s+FCT\s+\d+\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, listed_citation, flags=re.IGNORECASE)
        if match:
            return normalize_space(match.group(0).upper())
    return ""


def first_party_token(name: str) -> str:
    # Use first word before "v." as a lightweight identity token.
    base = name.split(" v.")[0].split(" v ")[0].strip().lower()
    base = re.sub(r"\s*\([^)]*\)", "", base)
    base = re.sub(r"[^a-z0-9\s\-]", " ", base)
    base = normalize_space(base)
    if not base:
        return ""
    tokens = [token for token in base.split(" ") if token]
    long_tokens = [token for token in tokens if len(token) >= 4]
    if long_tokens:
        return max(long_tokens, key=len)
    return tokens[0] if tokens else ""


def main() -> None:
    args = parse_args()
    if not args.seed_csv.exists():
        raise SystemExit(f"Seed file not found: {args.seed_csv}")
    if not args.core_csv.exists():
        raise SystemExit(f"Core file not found: {args.core_csv}")

    seeds = pd.read_csv(args.seed_csv)
    core = pd.read_csv(args.core_csv)
    core_citations = set(core["neutral_citation"].astype(str).str.upper().str.strip())

    with SessionLocal() as session:
        db_rows = list(session.execute(select(Case.id, Case.title, Case.citation)))

    db_citations = {
        str(citation).upper().strip(): (int(case_id), str(title or ""))
        for case_id, title, citation in db_rows
        if citation
    }

    db_title_rows: list[tuple[int, str, str]] = []
    for case_id, title, citation in db_rows:
        if not title:
            continue
        db_title_rows.append((int(case_id), normalize_name(str(title)), str(citation or "")))

    results: list[dict[str, object]] = []
    for _, row in seeds.iterrows():
        name = str(row.get("name", "")).strip()
        listed_citation = str(row.get("listed_citation", "")).strip()
        neutral = extract_neutral_citation(listed_citation)
        normalized_seed_name = normalize_name(name)

        status = "not_found"
        matched_case_id: int | None = None
        matched_case_citation = ""
        matched_case_title = ""
        matched_by = "none"
        name_match = False
        seed_party = first_party_token(name)

        if neutral:
            in_core = neutral in core_citations
            in_db = neutral in db_citations
            if in_core:
                status = "in_core_exact"
                matched_case_id, matched_case_title = db_citations.get(neutral, (None, ""))
                matched_case_citation = neutral
                matched_by = "neutral_citation"
                name_match = bool(seed_party and seed_party in normalize_name(matched_case_title))
                if not name_match:
                    status = "in_core_citation_only"
            elif in_db:
                status = "in_db_exact"
                matched_case_id, matched_case_title = db_citations.get(neutral, (None, ""))
                matched_case_citation = neutral
                matched_by = "neutral_citation"
                name_match = bool(seed_party and seed_party in normalize_name(matched_case_title))
                if not name_match:
                    status = "in_db_citation_only"
            else:
                status = "missing_exact"
        else:
            matches = [
                (case_id, db_title, citation)
                for case_id, db_title, citation in db_title_rows
                if normalized_seed_name and normalized_seed_name in db_title
            ]
            if matches:
                case_id, _db_title, citation = matches[0]
                matched_case_id = case_id
                matched_case_citation = citation
                matched_case_title = _db_title
                matched_by = "title_contains"
                name_match = True
                if citation and citation.upper().strip() in core_citations:
                    status = "in_core_title_candidate"
                else:
                    status = "in_db_title_candidate"
            else:
                status = "missing_exact"

        results.append(
            {
                "name": name,
                "listed_citation": listed_citation,
                "neutral_citation": neutral,
                "status": status,
                "matched_by": matched_by,
                "matched_case_id": matched_case_id,
                "matched_case_citation": matched_case_citation,
                "matched_case_title": matched_case_title,
                "name_match": name_match,
            }
        )

    output = pd.DataFrame(results)
    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.out_csv, index=False)

    print(f"seed_cases={len(output)}")
    for key, value in output["status"].value_counts().to_dict().items():
        print(f"{key}={value}")
    print(f"out_csv={args.out_csv}")


if __name__ == "__main__":
    main()
