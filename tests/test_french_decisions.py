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


def test_crown_as_appelant_wins_when_the_appeal_is_allowed_and_loses_when_dismissed():
	base = "Dossier : A-1-26\nENTRE :\nSA MAJESTÉ LE ROI\nappelant\net\nJEAN TREMBLAY\nintimé\nMOTIFS DU JUGEMENT\n[40] "
	allowed = build_case_outcome(base + "L’appel est accueilli, avec dépens.", {})
	assert (allowed["decision_outcome"], allowed["government_role"], allowed["government_outcome"]) == ("allowed", "applicant", "won")
	dismissed = build_case_outcome(base + "L’appel est rejeté, avec dépens.", {})
	assert (dismissed["decision_outcome"], dismissed["government_outcome"]) == ("dismissed", "lost")


def test_conflicting_french_rulings_are_unclear_not_the_last_one():
	text = "ENTRE :\nA B\nappelant\net\nLE MINISTRE\nintimé\n[50] L’appel est accueilli. La demande de contrôle judiciaire est rejetée, avec dépens."
	assert build_case_outcome(text, {})["decision_outcome"] in (None, "unclear")
	same = text.replace("est rejetée", "est accueillie")
	assert build_case_outcome(same, {})["decision_outcome"] == "allowed"


def _outcome(text):
	return build_case_outcome(text, {})["decision_outcome"]


FR_PAD = " Le demandeur est un citoyen et les motifs de la décision sont dans le dossier pour la Cour." * 12


def test_english_statute_text_quoted_in_a_french_decision_does_not_decide_the_outcome():
	text = (
		"Dossier : IMM-2-26\nENTRE :\nA B\ndemandeur\net\nLE MINISTRE\ndéfendeur\nMOTIFS ET JUGEMENT\n" + FR_PAD +
		"\nLa disposition prévoit que « the application is allowed if the officer erred ».\n"
		"[40] La demande de contrôle judiciaire est rejetée. Aucuns dépens."
	)
	assert _outcome(text) == "dismissed"


def test_subjunctive_order_after_the_cour_ordonne_marker_beats_earlier_history():
	text = (
		"Dossier : IMM-3-26\nENTRE :\nA B\ndemandeur\net\nLE MINISTRE\ndéfendeur\nMOTIFS\n" + FR_PAD +
		"\n[3] La demande d’autorisation est accueillie. Plus tard, l'affaire a été entendue.\n"
		"JUGEMENT\nLA COUR ORDONNE que la demande de contrôle judiciaire soit rejetée, sans frais."
	)
	assert _outcome(text) == "dismissed"


def test_conditional_first_person_ruling_in_appeal_reasons():
	base = "Dossier : A-9-26\nENTRE :\nA B\nappelant\net\nLE MINISTRE\nintimé\nMOTIFS DU JUGEMENT\n" + FR_PAD + "\n[60] "
	assert _outcome(base + "Je rejetterais l’appel, avec dépens.") == "dismissed"
	assert _outcome(base + "J’accueillerais l’appel, avec dépens.") == "allowed"


def test_allowed_for_one_party_and_dismissed_in_all_other_respects_is_in_part():
	text = (
		"Dossier : A-10-26\nENTRE :\nA B\nappelant\net\nLE MINISTRE\nintimé\nMOTIFS DU JUGEMENT\n" + FR_PAD +
		"\n[70] L’appel est accueilli à l’égard de M. B. et, à tous les autres égards, il est rejeté, sans dépens."
	)
	assert _outcome(text) == "mixed"


def test_french_signature_is_found_when_an_annex_follows():
	annex = "\nANNEXE\n" + "Disposition applicable du règlement et son texte complet.\n" * 400
	assert _extract_metadata_with_quality(FCA_TEXT + annex)["judge"] == "Nathalie Goyette"


def test_present_demande_fait_droit_and_en_partie_forms():
	head = "Dossier : IMM-4-26\nENTRE :\nA B\ndemandeur\net\nLE MINISTRE\ndéfendeur\nMOTIFS\n" + FR_PAD + "\n"
	assert _outcome(head + "LA COUR ORDONNE que la présente demande de contrôle judiciaire soit rejetée.") == "dismissed"
	assert _outcome(head + "LA COUR STATUE :\nIl est fait droit à la demande de contrôle judiciaire. La décision est annulée.") == "allowed"
	assert _outcome(head + "LA COUR STATUE que :\n1. Les demandes sont en partie accueillies;") == "mixed"


def test_a_condition_or_an_annex_after_the_order_is_not_the_ruling():
	head = "Dossier : A-11-26\nENTRE :\nA B\nappelant\net\nLE MINISTRE\nintimé\nMOTIFS\n" + FR_PAD + "\n"
	conditional = head + "[90] La requête sera rejetée, avec dépens. À défaut de quoi, ses appels seront rejetés."
	assert _outcome(conditional) == "procedural"
	annex = head + "LA COUR ORDONNE que la demande soit accueillie.\n« A B »\nJuge\nANNEXE\nLa demande est rejetée si l’agent est d’avis que..."
	assert _outcome(annex) == "allowed"
