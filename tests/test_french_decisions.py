"""French Federal Court / Court of Appeal decisions: judge, docket and outcome (review findings A9 and R11)."""

from backend.metadata_outcomes import build_case_outcome
from fc_ingest.document_scraper import _extract_metadata_with_quality

FC_HEADER = """Tremblay c. Canada (Procureur général)
Base de données – Cour (s)
Décisions de la Cour fédérale
Date
2026-09-16
Référence neutre
2026 CF 1165
Numéro de dossier
26-T-297
Contenu de la décision
Date : 20260916
Dossier : 26-T-297
Référence : 2026 CF 1165
Ottawa (Ontario), le 16 septembre 2026
En présence de l’honorable juge Duchesne
ENTRE :
JEAN-FRANÇOIS TREMBLAY
demandeur
et
PROCUREUR GÉNÉRAL DU CANADA
défendeur
MOTIFS ET ORDONNANCE
[1] Le demandeur a déposé une requête.
"""


def test_french_docket_stops_at_the_decision_content_heading_and_judge_loses_the_title():
	metadata = _extract_metadata_with_quality(FC_HEADER)
	assert metadata["docket"] == "26-T-297"
	assert metadata["judge"] == "Duchesne"


FCA_TEXT = """Date : 20260924
Dossier : A-127-25
Référence : 2026 CAF 160
CORAM : LE JUGE LOCKE
LA JUGE GOYETTE
LE JUGE PAMEL
ENTRE :
MAXIME FORTIN
appelant
et
SA MAJESTÉ LE ROI
intimé
MOTIFS DU JUGEMENT DE LA COUR
[13] Dans ces circonstances, l’appel sera rejeté sans dépens.
« Nathalie Goyette »
j.c.a.
COUR D’APPEL FÉDÉRALE
"""


def test_french_signature_names_the_judge_who_wrote_the_reasons():
	assert _extract_metadata_with_quality(FCA_TEXT)["judge"] == "Nathalie Goyette"


def test_french_disposition_is_read_and_the_crown_side_is_found():
	outcome = build_case_outcome(FCA_TEXT, _extract_metadata_with_quality(FCA_TEXT))
	assert outcome["decision_outcome"] == "dismissed"
	assert outcome["government_role"] == "respondent" and outcome["government_outcome"] == "won"
	assert "sera rejeté" in outcome["disposition_evidence"]


def test_french_application_allowed_and_motion_is_procedural():
	allowed = "Dossier : IMM-1-26\nENTRE :\nA B\ndemandeur\net\nLE MINISTRE DE LA CITOYENNETÉ ET DE L’IMMIGRATION\ndéfendeur\n[20] La demande de contrôle judiciaire est accueillie. Aucuns dépens."
	outcome = build_case_outcome(allowed, {})
	assert outcome["decision_outcome"] == "allowed"
	motion = "Dossier : 26-T-1\nLA COUR ORDONNE que : La requête du demandeur est rejetée, sans frais."
	assert build_case_outcome(motion, {})["decision_outcome"] == "procedural"
