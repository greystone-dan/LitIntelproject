"""Fill an empty local database with a test library for checking the site tour (scripts/check_site_tour.py).

The real library's result lists run to thousands of pixels, so a tour checked on a handful of cases misses what goes
wrong on long lists. This adds the 9 example decisions the tour opens (Vavilov, Baker, Dunsmuir, Khosa and five
made-up Federal Court files) and --bulk more made-up Federal Court files (default 300) that the tour's searches find:
best interests of the child, non-refoulement statutory interpretation, and cessation involving India won by the
Minister. Every decision says it is a TEST FIXTURE. Then it runs the same processing, case types, judge profiles
and pinpoint linking the real library has.

Local only: it refuses any base URL other than localhost, and needs --yes.

    python scripts/seed_tour_fixture.py --base-url http://localhost:8001 --yes
    python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --sizes 1440x900,1920x1080
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = "TEST FIXTURE: placeholder text used only to check the site tour locally. This is not the real decision."
VAVILOV = ("Reasonableness is the presumptive standard of review on an application under section 72 of the Immigration and "
           "Refugee Protection Act. See Dunsmuir v. New Brunswick, 2008 SCC 9 and Baker v. Canada (Minister of Citizenship "
           "and Immigration), [1999] 2 SCR 817.")
LONG = " A reviewing court must consider the outcome of the administrative decision in light of its underlying rationale. " \
       "This fixture sentence only makes the paragraph as long as a real one." * 6
EXAMPLES = [
    ("Canada (Minister of Citizenship and Immigration) v. Vavilov", "Supreme Court of Canada", "2019-12-19", "2019 SCC 65", "[2019] 4 SCR 653", VAVILOV + LONG),
    ("Baker v. Canada (Minister of Citizenship and Immigration)", "Supreme Court of Canada", "1999-07-09", "[1999] 2 SCR 817", "1999 CanLII 699 (SCC)",
     "The interests of children are an important factor in a humanitarian and compassionate decision under the Immigration Act. Duty of procedural fairness."),
    ("Dunsmuir v. New Brunswick", "Supreme Court of Canada", "2008-03-07", "2008 SCC 9", "[2008] 1 SCR 190",
     "Two standards of review: correctness and reasonableness. Section 18.1 of the Federal Courts Act."),
    ("Canada (Citizenship and Immigration) v. Khosa", "Supreme Court of Canada", "2009-03-06", "2009 SCC 12", "[2009] 1 SCR 339",
     "Judicial review of an Immigration and Refugee Board decision under section 18.1 of the Federal Courts Act; see Dunsmuir v. New Brunswick, 2008 SCC 9."),
    ("Sample Applicant v. Canada (Citizenship and Immigration)", "Federal Court", "2023-05-11", "2023 FC 685", "IMM-1234-22",
     "Judicial review of a visa officer's refusal. The standard is reasonableness per Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65. "
     "Procedural fairness. Application for a temporary resident visa under section 11 of the Immigration and Refugee Protection Act and section 179 of the "
     "Immigration and Refugee Protection Regulations; leave under section 72 of the Act. The application is dismissed."),
    ("Another Applicant v. Canada (Citizenship and Immigration)", "Federal Court", "2024-02-02", "2024 FC 100", "IMM-555-23",
     "Judicial review of a refusal of an application for permanent residence on humanitarian and compassionate grounds under section 25 of the Immigration "
     "and Refugee Protection Act. Baker v. Canada, [1999] 2 SCR 817. The officer did not consider the best interests of the child. Reasonableness applies "
     "per Vavilov, 2019 SCC 65 at para 5. The application is allowed."),
    ("Sample Minister v. Third Applicant", "Federal Court of Appeal", "2022-03-03", "2022 FCA 30", "A-100-21",
     "Appeal from the Federal Court. Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65 sets the standard. The appeal is dismissed."),
    ("Gurpreet Singh Sandhu and Harpreet Kaur Sandhu v. Canada (Minister of Citizenship and Immigration and Minister of Public Safety and Emergency Preparedness)",
     "Federal Court", "2025-03-04", "2025 FC 321", "IMM-777-24",
     "Judicial review of a decision of the Refugee Protection Division allowing the Minister's application for cessation of refugee protection under "
     "section 108 of the Immigration and Refugee Protection Act. The applicant, a citizen of India, renewed his Indian passport and travelled to India, "
     "and so reavailed himself of the protection of that country. Reasonableness applies per Vavilov, 2019 SCC 65 at para 5. The application for "
     "judicial review is dismissed."),
    ("Second Applicant v. Canada (Citizenship and Immigration)", "Federal Court", "2024-09-09", "2024 FC 900", "IMM-888-23",
     "Judicial review of a cessation decision under section 108 of the Immigration and Refugee Protection Act. The applicant is a citizen of India who "
     "returned to India voluntarily and obtained a new passport. Cessation of refugee protection under paragraph 108(1)(a). The application for judicial "
     "review is dismissed."),
]
BULK = [
    ("Best Interests of the Child Applicant {n} v. Canada (Citizenship and Immigration)",
     "Judicial review of a humanitarian and compassionate refusal under section 25 of the Immigration and Refugee Protection Act. The officer failed to "
     "weigh the best interests of the child. Reasonableness applies per Vavilov, 2019 SCC 65 at para 5. The application is allowed."),
    ("Non-refoulement Statutory Interpretation Applicant {n} v. Canada (Citizenship and Immigration)",
     "Statutory interpretation of section 115 of the Immigration and Refugee Protection Act and the principle of non-refoulement. Reasonableness "
     "applies per Vavilov, 2019 SCC 65. The application is dismissed."),
    ("Cessation Applicant {n} v. Canada (Citizenship and Immigration)",
     "Judicial review of a cessation decision under section 108 of the Immigration and Refugee Protection Act. The applicant, a citizen of India, "
     "renewed an Indian passport and travelled to India, and so reavailed himself of the protection of India. Reasonableness applies per Vavilov, "
     "2019 SCC 65 at para 5. The application for judicial review is dismissed."),
]


def decision(title: str, court: str, date: str, citation: str, judge: str, body: str, paragraphs: int) -> str:
    paras = [NOTE, "Judgment", "Reasons for judgment"] + [body] * paragraphs + ["Conclusion", body]
    head = f"{title}\n{court}\nDate: {date.replace('-', '')}\nJudge: {judge}\nCitation: {citation}\nDecision Content\n"
    return head + "\n".join(f"[{k + 1}] {p}" for k, p in enumerate(paras))


def ingest(base: str, case: dict) -> int:
    request = urllib.request.Request(base + "/ingest", json.dumps(case).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return int(json.load(response)["id"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-url", default="http://localhost:8001")
    parser.add_argument("--bulk", type=int, default=300, help="how many made-up Federal Court files to add for long result lists")
    parser.add_argument("--yes", action="store_true", help="write the test library into the local database")
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    if urllib.parse.urlparse(base).hostname not in {"localhost", "127.0.0.1"}:
        print("refusing: the tour fixture is for a local test database only")
        return 1
    if not args.yes:
        print(f"would add {len(EXAMPLES)} example decisions and {args.bulk} made-up files to the database behind {base}; add --yes")
        return 0
    ids = []
    for title, court, date, citation, second, body in EXAMPLES:
        judge = "Justice Rowe" if "SCC" in citation else ("Justice Stratas" if "FCA" in citation else "Justice Smith")
        ids.append(ingest(base, dict(title=title, court=court, date=date, citation=citation, secondary_citation=second,
                                     docket_number=second if second.startswith(("IMM", "A-")) else None,
                                     full_text=decision(title, court, date, citation, judge, body, 12), summary=body)))
    for k in range(args.bulk):
        title, body = BULK[k % len(BULK)]
        title, citation, date = title.format(n=k + 1), f"2023 FC {1000 + k}", f"2023-{1 + k % 12:02d}-{1 + k % 27:02d}"
        ids.append(ingest(base, dict(title=title, court="Federal Court", date=date, citation=citation, docket_number=f"IMM-{2000 + k}-22",
                                     full_text=decision(title, "Federal Court", date, citation, f"Justice Brown{k % 7}", body, 6), summary=body)))
    sys.path.insert(0, str(ROOT))
    from backend.case_processing import process_case_in_five_layers
    from backend.database import SessionLocal
    from sqlalchemy import text

    db = SessionLocal()
    try:
        for case_id in ids:
            process_case_in_five_layers(db, case_id)
            db.commit()
        db.execute(text("UPDATE citations SET target_case_id = (SELECT id FROM cases WHERE citation = '2019 SCC 65' LIMIT 1) "
                        "WHERE citation_text ILIKE '%2019 SCC 65%' AND target_case_id IS NULL AND source_case_id = ANY(:ids)"), {"ids": ids})
        db.commit()
    finally:
        db.close()
    for script in ("classify_case_types.py --apply", "backfill_judge_profiles.py", "link_citation_pinpoints.py --apply"):
        subprocess.run([sys.executable, str(ROOT / "scripts" / script.split()[0]), *script.split()[1:]], cwd=ROOT, check=False,
                       env={**os.environ, "PYTHONPATH": str(ROOT)})
    print(f"added {len(ids)} test decisions (ids {ids[0]} to {ids[-1]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
