import json
from datetime import date
from urllib.request import Request, urlopen

from sqlalchemy import select

from backend.database import Case, SessionLocal
from backend.models import CaseIngestRequest

API_URL = "http://127.0.0.1:8000/ingest"

CASES = [
    ("A.B.", "2023-02-15", "2023 FC TEST001", "RPD refusal involving political persecution. Court reviews credibility and risk-on-return under s.96/s.97 IRPA. Non-refoulement engaged. Application granted.", ["non-refoulement", "s.96 IRPA", "s.97 IRPA", "credibility"]),
    ("Singh", "2022-03-10", "2022 FC TEST002", "RAD decision involving political opponents. Court reviews internal flight alternatives and state protection. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "RAD review", "state protection", "IFA"]),
    ("Mohammed", "2021-06-18", "2021 FC TEST003", "RPD refusal involving torture risk. Court reviews expert evidence and country documentation. Non-refoulement obligations referenced. Application granted.", ["non-refoulement", "torture", "expert evidence", "s.97 IRPA"]),
    ("Chen", "2020-04-22", "2020 FC TEST004", "RAD decision involving religious persecution. Court reviews internal relocation and state protection. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "religious persecution", "IFA"]),
    ("Hassan", "2019-09-30", "2019 FC TEST005", "RPD refusal involving non-state actors. Court reviews systemic violence and state protection. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "non-state actors", "systemic violence"]),
    ("A.A.", "2023-05-12", "2023 FC TEST006", "PRRA refusal involving cruel treatment. Court reviews updated country reports. Explicit non-refoulement obligations referenced. Application granted.", ["non-refoulement", "PRRA", "cruel treatment"]),
    ("T.M.", "2022-07-08", "2022 FC TEST007", "PRRA refusal involving political risk. Court reviews contradictory country information. Non-refoulement central. Application dismissed.", ["non-refoulement", "PRRA", "political risk"]),
    ("Lopez", "2021-03-05", "2021 FC TEST008", "RPD refusal involving gang violence. Court reviews persecution versus criminality. Non-refoulement engaged. Application granted.", ["non-refoulement", "gang violence", "persecution"]),
    ("Ali", "2020-06-10", "2020 FC TEST009", "RAD decision involving sexual orientation risk. Court reviews credibility and country conditions. Non-refoulement implicated. Application dismissed.", ["non-refoulement", "sexual orientation", "credibility"]),
    ("J.M.", "2019-07-22", "2019 FC TEST010", "RPD refusal involving gender-based violence. Court reviews state protection. Non-refoulement engaged. Application granted.", ["non-refoulement", "gender-based violence", "state protection"]),
    ("Ibrahim", "2022-09-14", "2022 FC TEST011", "RAD decision involving armed groups. Court reviews generalized versus personalized risk. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "armed groups", "generalized risk"]),
    ("A.M.", "2021-04-28", "2021 FC TEST012", "PRRA refusal involving arbitrary detention. Court reviews human rights reports. Explicit non-refoulement obligations referenced. Application granted.", ["non-refoulement", "PRRA", "arbitrary detention"]),
    ("Sadiq", "2020-03-02", "2020 FC TEST013", "RPD refusal involving political activism. Court reviews credibility and future risk. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "political activism", "credibility"]),
    ("Khan", "2023-06-01", "2023 FC TEST014", "RAD decision involving religious conversion. Court reviews societal and state responses. Non-refoulement engaged. Application granted.", ["non-refoulement", "religious conversion", "state response"]),
    ("Li", "2022-04-05", "2022 FC TEST015", "RPD refusal involving political activity abroad. Court reviews surveillance risk. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "political activity", "surveillance"]),
    ("A.S.", "2021-07-15", "2021 FC TEST016", "PRRA refusal involving organized crime. Court reviews targeted versus generalized risk. Non-refoulement central. Application dismissed.", ["non-refoulement", "organized crime", "targeted risk"]),
    ("Hassan", "2020-05-01", "2020 FC TEST017", "RPD refusal involving ethnic minority risk. Court reviews systemic discrimination. Non-refoulement engaged. Application granted.", ["non-refoulement", "ethnic minority", "discrimination"]),
    ("Mohammed", "2019-06-18", "2019 FC TEST018", "RAD decision involving past detention. Court reviews ongoing risk. Non-refoulement engaged. Application dismissed.", ["non-refoulement", "detention", "ill-treatment"]),
    ("A.B.", "2023-09-10", "2023 FC TEST019", "PRRA refusal involving digital surveillance. Court reviews punishment likelihood. Non-refoulement central. Application granted.", ["non-refoulement", "digital surveillance", "political dissent"]),
    ("R.P.", "2024-01-12", "2024 FC TEST020", "RPD refusal involving whistleblower retaliation. Court reviews risk of reprisal and state complicity. Non-refoulement engaged. Application granted.", ["non-refoulement", "whistleblower", "reprisal", "state complicity"]),
]


def build_case(index, name, decision_date, citation, summary, issues):
    return CaseIngestRequest(
        title=f"TEST CASE - {name} v. Canada, {citation}",
        court="Federal Court",
        jurisdiction="Canada",
        date=date.fromisoformat(decision_date),
        citation=citation,
        summary=f"Synthetic {summary}",
        issues=issues,
        metadata_json={
            "synthetic": True,
            "verification_status": "synthetic_test_data",
            "verification_notes": "Fully synthetic test case.",
            "dataset": "Federal Court non-refoulement pilot",
            "dataset_index": index,
        },
        source_url=f"https://example.com/fct/test{index:03d}",
        source_name="SyntheticSource",
    )


with SessionLocal() as session:
    existing_citations = set(session.scalars(select(Case.citation)).all())

for index, values in enumerate(CASES, start=1):
    case = build_case(index, *values)
    if case.citation in existing_citations:
        print(f"{index:02d}: skipped existing citation={case.citation}")
        continue

    request = Request(
        API_URL,
        data=json.dumps(case.model_dump(mode="json")).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request) as response:
        result = json.load(response)
    print(f"{index:02d}: id={result['id']} citation={result['citation']}")
