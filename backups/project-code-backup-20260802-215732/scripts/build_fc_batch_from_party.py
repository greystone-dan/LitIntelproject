from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

import httpx


def parse_ms_date(raw: str | None) -> str | None:
    text = str(raw or "")
    match = re.search(r"/Date\((\d+)", text)
    if not match:
        return None
    return dt.datetime.utcfromtimestamp(int(match.group(1)) / 1000).date().isoformat()


def main() -> None:
    url = "https://www.fct-cf.ca/CourtFilesAndDecisions/ProceedingsQueriesPartyInfo"
    params = {"division": "t", "name": "MCI"}

    with httpx.Client(timeout=45, follow_redirects=True, headers={"User-Agent": "Mozilla/5.0"}) as client:
        response = client.get(url, params=params)
        response.raise_for_status()
        rows = (response.json().get("data") or [])[:25]

    out: list[dict] = []
    for row in rows:
        decision_date = parse_ms_date(row.get("FILE_DT"))
        title = (row.get("STYLE_OF_CAUSE") or "").strip() or "Untitled Federal Court file"
        court_no = (row.get("COURT_NO") or "").strip()
        nature = (row.get("ENGLISH_NATURE_DESC") or "").strip()
        city = (row.get("ENGLISH_CITY_NAME") or "").strip()

        summary = "Federal Court court-file record from official portal. "
        if nature:
            summary += f"Nature: {nature}. "
        if city:
            summary += f"Registry city: {city}. "
        if court_no:
            summary += f"Court file number: {court_no}."

        out.append(
            {
                "style_of_cause": title,
                "decision_date": decision_date,
                "docket_number": court_no or None,
                "summary": summary,
                "citation": court_no or None,
                "url": "https://www.fct-cf.ca/en/court-files-and-decisions/court-files",
                "court": "Federal Court",
                "jurisdiction": "Canada",
                "language": "en",
                "dataset": "fc_portal",
                "source_id": row.get("COURT_SEQ") or court_no,
                "metadata_json": {
                    "source_endpoint": "ProceedingsQueriesPartyInfo",
                    "query_name": "MCI",
                    "division": row.get("DIVISION"),
                    "nature_code": row.get("NATURE_CD"),
                    "nature_desc": nature or None,
                    "city": city or None,
                    "court_seq": row.get("COURT_SEQ"),
                    "party": row.get("Party"),
                },
            }
        )

    target = Path("data/raw/fc/portal_party_mci_25.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, ensure_ascii=True, indent=2), encoding="utf-8")
    dated = sum(1 for row in out if row.get("decision_date"))
    print(f"wrote={target} count={len(out)} with_date={dated}")


if __name__ == "__main__":
    main()
