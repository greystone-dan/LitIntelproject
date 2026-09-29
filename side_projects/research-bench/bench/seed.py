"""Sample data: public decisions already cited in the project.

Summaries are one-line descriptions for demo search only. Dockets under
"tracked matters" are EXAMPLES, not real files.
"""
from datetime import date

from .models import AlertKind, Decision, DocketEntry

DECISIONS = [
    Decision("2026 FCA 140", "Wahab v. Canada (Citizenship and Immigration)", "FCA",
             date(2026, 1, 1),
             summary="non-refoulement Article 33 relevant to interpreting inadmissibility "
                     "section 34 Immigration Division reasons"),
    Decision("2023 SCC 21", "Mason v. Canada (Citizenship and Immigration)", "SCC",
             date(2023, 9, 15),
             summary="section 34(1)(e) acts of violence interpretation reasonableness "
                     "Vavilov international law non-refoulement"),
    Decision("2024 FCA 69", "Weldemariam v. Canada (Public Safety and Emergency Preparedness)",
             "FCA", date(2024, 1, 1),
             summary="section 34(1)(f) membership organization interpretation"),
]
# Decision dates for Wahab and Weldemariam are placeholders (Jan 1): confirm from the source.

DOCKETS = {
    "A-000-26": [   # EXAMPLE docket
        DocketEntry("A-000-26", date(2026, 9, 10), "Notice of appeal filed"),
        DocketEntry("A-000-26", date(2026, 9, 24), "Requisition for hearing filed"),
        DocketEntry("A-000-26", date(2026, 9, 28), "Hearing set", AlertKind.HEARING),
    ],
    "A-001-26": [   # EXAMPLE docket
        DocketEntry("A-001-26", date(2026, 9, 26), "Judgment and reasons released",
                    AlertKind.DECISION, decision_citation="2026 FCA 000 (example)"),
    ],
}
