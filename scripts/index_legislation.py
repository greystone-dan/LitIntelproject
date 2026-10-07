"""Index authoritative legal sources into section-addressable references."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup

from sqlalchemy import delete, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import LegislationDocument, LegislationSection, SessionLocal

@dataclass(frozen=True)
class SourceDefinition:
	title: str
	citation: str
	relative_path: str
	source_format: str
	source_url: str


XML_SOURCES = {
	"canada.irpa": SourceDefinition(
		title="Immigration and Refugee Protection Act",
		citation="I-2.5",
		relative_path="IRPA DATA/IRPA.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/I-2.5/",
	),
	"canada.irpr": SourceDefinition(
		title="Immigration and Refugee Protection Regulations",
		citation="SOR/2002-227",
		relative_path="IRPA DATA/IRPA-R.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/",
	),
	"canada.criminal_code": SourceDefinition(
		title="Criminal Code",
		citation="R.S.C. 1985, c. C-46",
		relative_path="legislation_xml/C-46.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-46/",
	),
	"canada.citizenship_act": SourceDefinition(
		title="Citizenship Act",
		citation="R.S.C. 1985, c. C-29",
		relative_path="legislation_xml/C-29.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-29/",
	),
	"canada.federal_courts_act": SourceDefinition(
		title="Federal Courts Act",
		citation="R.S.C. 1985, c. F-7",
		relative_path="legislation_xml/F-7.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/F-7/",
	),
	"canada.federal_courts_rules": SourceDefinition(
		title="Federal Courts Rules",
		citation="SOR/98-106",
		relative_path="legislation_xml/SOR-98-106.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/regulations/SOR-98-106/",
	),
	"canada.income_tax_act": SourceDefinition(
		title="Income Tax Act",
		citation="R.S.C. 1985, c. 1 (5th Supp.)",
		relative_path="legislation_xml/I-3.3.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/I-3.3/",
	),
	"canada.marine_liability_act": SourceDefinition(
		title="Marine Liability Act",
		citation="S.C. 2001, c. 6",
		relative_path="legislation_xml/M-0.7.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/M-0.7/",
	),
	"canada.commercial_arbitration_act": SourceDefinition(
		title="Commercial Arbitration Act",
		citation="R.S.C. 1985, c. C-34.6",
		relative_path="legislation_xml/C-34.6.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-34.6/",
	),
	"canada.coastal_fisheries_protection_act": SourceDefinition(
		title="Coastal Fisheries Protection Act",
		citation="R.S.C. 1985, c. C-33",
		relative_path="legislation_xml/C-33.xml",
		source_format="xml",
		source_url="https://laws-lois.justice.gc.ca/eng/acts/C-33/",
	),
}

# Justice Laws XML snapshots added for statute coverage (Open Government Licence - Canada).
# Each row: instrument key, title the XML must carry, citation, file in data/reference_library/legislation_xml/, Justice Laws path.
_JUSTICE_LAWS = (
	("canada.customs_act", "Customs Act", "R.S.C. 1985, c. 1 (2nd Supp.)", "C-52.6.xml", "acts/C-52.6"),
	("canada.cbsa_act", "Canada Border Services Agency Act", "S.C. 2005, c. 38", "C-1.4.xml", "acts/C-1.4"),
	("canada.customs_tariff", "Customs Tariff", "S.C. 1997, c. 36", "C-54.011.xml", "acts/C-54.011"),
	("canada.excise_tax_act", "Excise Tax Act", "R.S.C. 1985, c. E-15", "E-15.xml", "acts/E-15"),
	("canada.excise_act", "Excise Act", "R.S.C. 1985, c. E-14", "E-14.xml", "acts/E-14"),
	("canada.excise_act_2001", "Excise Act, 2001", "S.C. 2002, c. 22", "E-14.1.xml", "acts/E-14.1"),
	("canada.patent_act", "Patent Act", "R.S.C. 1985, c. P-4", "P-4.xml", "acts/P-4"),
	("canada.competition_act", "Competition Act", "R.S.C. 1985, c. C-34", "C-34.xml", "acts/C-34"),
	("canada.bankruptcy_insolvency_act", "Bankruptcy and Insolvency Act", "R.S.C. 1985, c. B-3", "B-3.xml", "acts/B-3"),
	("canada.food_and_drugs_act", "Food and Drugs Act", "R.S.C. 1985, c. F-27", "F-27.xml", "acts/F-27"),
	("canada.controlled_drugs_substances_act", "Controlled Drugs and Substances Act", "S.C. 1996, c. 19", "C-38.8.xml", "acts/C-38.8"),
	("canada.evidence_act", "Canada Evidence Act", "R.S.C. 1985, c. C-5", "C-5.xml", "acts/C-5"),
	("canada.access_to_information_act", "Access to Information Act", "R.S.C. 1985, c. A-1", "A-1.xml", "acts/A-1"),
	("canada.interpretation_act", "Interpretation Act", "R.S.C. 1985, c. I-21", "I-21.xml", "acts/I-21"),
	("canada.supreme_court_act", "Supreme Court Act", "R.S.C. 1985, c. S-26", "S-26.xml", "acts/S-26"),
	("canada.fisheries_act", "Fisheries Act", "R.S.C. 1985, c. F-14", "F-14.xml", "acts/F-14"),
	("canada.labour_code", "Canada Labour Code", "R.S.C. 1985, c. L-2", "L-2.xml", "acts/L-2"),
	("canada.criminal_records_act", "Criminal Records Act", "R.S.C. 1985, c. C-47", "C-47.xml", "acts/C-47"),
	("canada.csis_act", "Canadian Security Intelligence Service Act", "R.S.C. 1985, c. C-23", "C-23.xml", "acts/C-23"),
	("canada.extradition_act", "Extradition Act", "S.C. 1999, c. 18", "E-23.01.xml", "acts/E-23.01"),
	("canada.security_of_information_act", "Security of Information Act", "R.S.C. 1985, c. O-5", "O-5.xml", "acts/O-5"),
	("canada.marine_act", "Canada Marine Act", "S.C. 1998, c. 10", "C-6.7.xml", "acts/C-6.7"),
	("canada.employment_insurance_act", "Employment Insurance Act", "S.C. 1996, c. 23", "E-5.6.xml", "acts/E-5.6"),
	("canada.railway_safety_act", "Railway Safety Act", "R.S.C. 1985, c. 32 (4th Supp.)", "R-4.2.xml", "acts/R-4.2"),
	("canada.crown_liability_proceedings_act", "Crown Liability and Proceedings Act", "R.S.C. 1985, c. C-50", "C-50.xml", "acts/C-50"),
	("canada.shipping_act_2001", "Canada Shipping Act, 2001", "S.C. 2001, c. 26", "C-10.15.xml", "acts/C-10.15"),
	("canada.fpslra", "Federal Public Sector Labour Relations Act", "S.C. 2003, c. 22, s. 2", "P-33.3.xml", "acts/P-33.3"),
	("canada.pcmltfa", "Proceeds of Crime (Money Laundering) and Terrorist Financing Act", "S.C. 2000, c. 17", "P-24.501.xml", "acts/P-24.501"),
	("canada.corrections_conditional_release_act", "Corrections and Conditional Release Act", "S.C. 1992, c. 20", "C-44.6.xml", "acts/C-44.6"),
	("canada.youth_criminal_justice_act", "Youth Criminal Justice Act", "S.C. 2002, c. 1", "Y-1.5.xml", "acts/Y-1.5"),
	("canada.indian_act", "Indian Act", "R.S.C. 1985, c. I-5", "indian_act_I-5.xml", "acts/I-5"),
	("canada.privacy_act", "Privacy Act", "R.S.C. 1985, c. P-21", "privacy_act_P-21.xml", "acts/P-21"),
	("canada.human_rights_act", "Canadian Human Rights Act", "R.S.C. 1985, c. H-6", "canadian_human_rights_act_H-6.xml", "acts/H-6"),
	("canada.rpd_rules", "Refugee Protection Division Rules", "SOR/2012-256", "SOR-2012-256.xml", "regulations/SOR-2012-256"),
	("canada.rad_rules", "Refugee Appeal Division Rules", "SOR/2012-257", "SOR-2012-257.xml", "regulations/SOR-2012-257"),
	("canada.id_rules", "Immigration Division Rules", "SOR/2002-229", "SOR-2002-229.xml", "regulations/SOR-2002-229"),
	("canada.iad_rules", "Immigration Appeal Division Rules, 2022", "SOR/2022-277", "SOR-2022-277.xml", "regulations/SOR-2022-277"),
	("canada.fc_cirp_rules", "Federal Courts Citizenship, Immigration and Refugee Protection Rules", "SOR/93-22", "SOR-93-22.xml", "regulations/SOR-93-22"),
	("canada.citizenship_regulations", "Citizenship Regulations", "SOR/93-246", "SOR-93-246.xml", "regulations/SOR-93-246"),
	("canada.noc_regulations", "Patented Medicines (Notice of Compliance) Regulations", "SOR/93-133", "SOR-93-133.xml", "regulations/SOR-93-133"),
	("canada.food_and_drug_regulations", "Food and Drug Regulations", "C.R.C., c. 870", "CRC-c-870.xml", "regulations/C.R.C.,_c._870"),
	("canada.cpp", "Canada Pension Plan", "R.S.C. 1985, c. C-8", "C-8.xml", "acts/C-8"),
	("canada.oas_act", "Old Age Security Act", "R.S.C. 1985, c. O-9", "O-9.xml", "acts/O-9"),
	("canada.official_languages_act", "Official Languages Act", "R.S.C. 1985, c. 31 (4th Supp.)", "O-3.01.xml", "acts/O-3.01"),
	("canada.cra_act", "Canada Revenue Agency Act", "S.C. 1999, c. 17", "C-10.11.xml", "acts/C-10.11"),
	("canada.cbca", "Canada Business Corporations Act", "R.S.C. 1985, c. C-44", "C-44.xml", "acts/C-44"),
	("canada.copyright_act", "Copyright Act", "R.S.C. 1985, c. C-42", "C-42.xml", "acts/C-42"),
	("canada.trademarks_act", "Trademarks Act", "R.S.C. 1985, c. T-13", "T-13.xml", "acts/T-13"),
	("canada.telecommunications_act", "Telecommunications Act", "S.C. 1993, c. 38", "T-3.4.xml", "acts/T-3.4"),
	("canada.transportation_act", "Canada Transportation Act", "S.C. 1996, c. 10", "C-10.4.xml", "acts/C-10.4"),
	("canada.elections_act", "Canada Elections Act", "S.C. 2000, c. 9", "E-2.01.xml", "acts/E-2.01"),
	("canada.national_defence_act", "National Defence Act", "R.S.C. 1985, c. N-5", "N-5.xml", "acts/N-5"),
	("canada.cepa_1999", "Canadian Environmental Protection Act, 1999", "S.C. 1999, c. 33", "C-15.31.xml", "acts/C-15.31"),
	("canada.judges_act", "Judges Act", "R.S.C. 1985, c. J-1", "J-1.xml", "acts/J-1"),
	("canada.rcmp_act", "Royal Canadian Mounted Police Act", "R.S.C. 1985, c. R-10", "R-10.xml", "acts/R-10"),
	("canada.public_service_employment_act", "Public Service Employment Act", "S.C. 2003, c. 22, ss. 12, 13", "P-33.01.xml", "acts/P-33.01"),
	("canada.employment_equity_act", "Employment Equity Act", "S.C. 1995, c. 44", "E-5.401.xml", "acts/E-5.401"),
	("canada.multiculturalism_act", "Canadian Multiculturalism Act", "R.S.C. 1985, c. 24 (4th Supp.)", "C-18.7.xml", "acts/C-18.7"),
	("canada.divorce_act", "Divorce Act", "R.S.C. 1985, c. 3 (2nd Supp.)", "D-3.4.xml", "acts/D-3.4"),
	("canada.sema", "Special Economic Measures Act", "S.C. 1992, c. 17", "S-14.5.xml", "acts/S-14.5"),
	("canada.magnitsky_act", "Justice for Victims of Corrupt Foreign Officials Act (Sergei Magnitsky Law)", "S.C. 2017, c. 21", "J-2.3.xml", "acts/J-2.3"),
	("canada.scida", "Security of Canada Information Disclosure Act", "S.C. 2015, c. 20, s. 2", "S-6.9.xml", "acts/S-6.9"),
	("canada.tax_court_act", "Tax Court of Canada Act", "R.S.C. 1985, c. T-2", "T-2.xml", "acts/T-2"),
	("canada.sima", "Special Import Measures Act", "R.S.C. 1985, c. S-15", "S-15.xml", "acts/S-15"),
	("canada.export_import_permits_act", "Export and Import Permits Act", "R.S.C. 1985, c. E-19", "E-19.xml", "acts/E-19"),
	("canada.firearms_act", "Firearms Act", "S.C. 1995, c. 39", "F-11.6.xml", "acts/F-11.6"),
	("canada.health_of_animals_act", "Health of Animals Act", "S.C. 1990, c. 21", "H-3.3.xml", "acts/H-3.3"),
	("canada.plant_protection_act", "Plant Protection Act", "S.C. 1990, c. 22", "P-14.8.xml", "acts/P-14.8"),
	("canada.quarantine_act", "Quarantine Act", "S.C. 2005, c. 20", "Q-1.1.xml", "acts/Q-1.1"),
	("canada.wappriita", "Wild Animal and Plant Protection and Regulation of International and Interprovincial Trade Act", "S.C. 1992, c. 52", "W-8.5.xml", "acts/W-8.5"),
	("canada.cultural_property_act", "Cultural Property Export and Import Act", "R.S.C. 1985, c. C-51", "C-51.xml", "acts/C-51"),
	("canada.seized_property_act", "Seized Property Management Act", "S.C. 1993, c. 37", "S-8.3.xml", "acts/S-8.3"),
	("canada.gec_act", "Government Employees Compensation Act", "R.S.C. 1985, c. G-5", "G-5.xml", "acts/G-5"),
	("canada.citt_act", "Canadian International Trade Tribunal Act", "R.S.C. 1985, c. 47 (4th Supp.)", "C-18.3.xml", "acts/C-18.3"),
	("canada.ei_regulations", "Employment Insurance Regulations", "SOR/96-332", "SOR-96-332.xml", "regulations/SOR-96-332"),
	("canada.ccr_regulations", "Corrections and Conditional Release Regulations", "SOR/92-620", "SOR-92-620.xml", "regulations/SOR-92-620"),
	("canada.presentation_of_persons_regs", "Presentation of Persons (2003) Regulations", "SOR/2003-323", "SOR-2003-323.xml", "regulations/SOR-2003-323"),
	("canada.reporting_imported_goods_regs", "Reporting of Imported Goods Regulations", "SOR/86-873", "SOR-86-873.xml", "regulations/SOR-86-873"),
	("canada.tax_court_rules_general", "Tax Court of Canada Rules (General Procedure)", "SOR/90-688a", "SOR-90-688A.xml", "regulations/SOR-90-688A"),
	("canada.financial_administration_act", "Financial Administration Act", "R.S.C. 1985, c. F-11", "F-11.xml", "acts/F-11"),
	("canada.statutory_instruments_act", "Statutory Instruments Act", "R.S.C. 1985, c. S-22", "S-22.xml", "acts/S-22"),
	("canada.department_cic_act", "Department of Citizenship and Immigration Act", "S.C. 1994, c. 31", "C-29.4.xml", "acts/C-29.4"),
	("canada.prisons_reformatories_act", "Prisons and Reformatories Act", "R.S.C. 1985, c. P-20", "P-20.xml", "acts/P-20"),
	("canada.transfer_of_offenders_act", "Transfer of Offenders Act", "S.C. 2004, c. 21", "T-15.xml", "acts/T-15"),
	("canada.mutual_legal_assistance_act", "Mutual Legal Assistance in Criminal Matters Act", "R.S.C. 1985, c. 30 (4th Supp.)", "M-13.6.xml", "acts/M-13.6"),
	("canada.identification_of_criminals_act", "Identification of Criminals Act", "R.S.C. 1985, c. I-1", "I-1.xml", "acts/I-1"),
	("canada.bill_of_rights", "Canadian Bill of Rights", "S.C. 1960, c. 44", "C-12.3.xml", "acts/C-12.3"),
	("canada.pipeda", "Personal Information Protection and Electronic Documents Act", "S.C. 2000, c. 5", "P-8.6.xml", "acts/P-8.6"),
	("canada.carriage_by_air_act", "Carriage by Air Act", "R.S.C. 1985, c. C-26", "C-26.xml", "acts/C-26"),
	("canada.income_tax_regulations", "Income Tax Regulations", "C.R.C., c. 945", "CRC-c-945.xml", "regulations/C.R.C.,_c._945"),
	("canada.pension_act", "Pension Act", "R.S.C. 1985, c. P-6", "P-6.xml", "acts/P-6"),
	("canada.bank_act", "Bank Act", "S.C. 1991, c. 46", "B-1.01.xml", "acts/B-1.01"),
	("canada.broadcasting_act", "Broadcasting Act", "S.C. 1991, c. 11", "B-9.01.xml", "acts/B-9.01"),
	("canada.aeronautics_act", "Aeronautics Act", "R.S.C. 1985, c. A-2", "A-2.xml", "acts/A-2"),
	("canada.vrab_act", "Veterans Review and Appeal Board Act", "S.C. 1995, c. 18", "V-1.6.xml", "acts/V-1.6"),
	("canada.crba", "Canada Recovery Benefits Act", "S.C. 2020, c. 12, s. 2", "C-10.10.xml", "acts/C-10.10"),
	("canada.cerba", "Canada Emergency Response Benefit Act", "S.C. 2020, c. 5, s. 8", "C-3.7.xml", "acts/C-3.7"),
	("canada.statistics_act", "Statistics Act", "R.S.C. 1985, c. S-19", "S-19.xml", "acts/S-19"),
	("canada.interest_act", "Interest Act", "R.S.C. 1985, c. I-15", "I-15.xml", "acts/I-15"),
	("canada.bills_of_exchange_act", "Bills of Exchange Act", "R.S.C. 1985, c. B-4", "B-4.xml", "acts/B-4"),
	("canada.state_immunity_act", "State Immunity Act", "R.S.C. 1985, c. S-18", "S-18.xml", "acts/S-18"),
	("canada.parliament_act", "Parliament of Canada Act", "R.S.C. 1985, c. P-1", "P-1.xml", "acts/P-1"),
	("canada.pssa", "Public Service Superannuation Act", "R.S.C. 1985, c. P-36", "P-36.xml", "acts/P-36"),
	("canada.cfsa", "Canadian Forces Superannuation Act", "R.S.C. 1985, c. C-17", "C-17.xml", "acts/C-17"),
	("canada.impact_assessment_act", "Impact Assessment Act", "S.C. 2019, c. 28, s. 1", "I-2.75.xml", "acts/I-2.75"),
	("canada.radiocommunication_act", "Radiocommunication Act", "R.S.C. 1985, c. R-2", "R-2.xml", "acts/R-2"),
	("canada.emergencies_act", "Emergencies Act", "R.S.C. 1985, c. 22 (4th Supp.)", "E-4.5.xml", "acts/E-4.5"),
	("canada.post_corporation_act", "Canada Post Corporation Act", "R.S.C. 1985, c. C-10", "C-10.xml", "acts/C-10"),
	("canada.cicc_act", "College of Immigration and Citizenship Consultants Act", "S.C. 2019, c. 29, s. 292", "C-33.6.xml", "acts/C-33.6"),
	("canada.cahwca", "Crimes Against Humanity and War Crimes Act", "S.C. 2000, c. 24", "C-45.9.xml", "acts/C-45.9"),
	("canada.esdc_act", "Department of Employment and Social Development Act", "S.C. 2005, c. 34", "H-5.7.xml", "acts/H-5.7"),
	("canada.csfaa", "Canada Student Financial Assistance Act", "S.C. 1994, c. 28", "S-22.7.xml", "acts/S-22.7"),
	("canada.security_offences_act", "Security Offences Act", "R.S.C. 1985, c. S-7", "S-7.xml", "acts/S-7"),
	("canada.pser", "Public Service Employment Regulations", "SOR/2005-334", "SOR-2005-334.xml", "regulations/SOR-2005-334"),
	("canada.patent_rules", "Patent Rules", "SOR/2019-251", "SOR-2019-251.xml", "regulations/SOR-2019-251"),
)

for _key, _title, _citation, _file, _path in _JUSTICE_LAWS:
	XML_SOURCES.setdefault(
		_key,
		SourceDefinition(
			title=_title,
			citation=_citation,
			relative_path=f"data/reference_library/legislation_xml/{_file}",
			source_format="xml",
			source_url=f"https://laws-lois.justice.gc.ca/eng/{_path}/",
		),
	)
JUSTICE_LAWS_KEYS = tuple(row[0] for row in _JUSTICE_LAWS)

NON_XML_SOURCES = {
	"canada.charter": SourceDefinition(
		title="Canadian Charter of Rights and Freedoms",
		citation="Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982",
		relative_path="data/reference_library/non_xml_authorities/constitution_act_1982_page_12.html",
		source_format="html",
		source_url="https://laws-lois.justice.gc.ca/eng/const/page-12.html",
	),
	"canada.constitution_act_1867": SourceDefinition(
		title="Constitution Act, 1867",
		citation="Constitution Act, 1867, 30 & 31 Vict., c. 3 (U.K.)",
		relative_path="data/reference_library/non_xml_authorities/constitution_acts_1867_to_1982.html",
		source_format="html_constitution_1867",
		source_url="https://laws-lois.justice.gc.ca/eng/const/FullText.html",
	),
	"canada.constitution_act_1982": SourceDefinition(
		title="Constitution Act, 1982",
		citation="Constitution Act, 1982, Schedule B to the Canada Act 1982 (U.K.), 1982, c. 11",
		relative_path="data/reference_library/non_xml_authorities/constitution_acts_1867_to_1982.html",
		source_format="html_constitution_1982",
		source_url="https://laws-lois.justice.gc.ca/eng/const/FullText.html",
	),
	# Provincial acts cut from the A2AJ canadian-laws dataset by scripts/extract_a2aj_provincial_acts.py (open tier only).
	"ontario.immigration_act_2015": SourceDefinition(
		title="Ontario Immigration Act, 2015",
		citation="Ontario Immigration Act, 2015, S.O. 2015, c. 8",
		relative_path="data/reference_library/provincial_json/ontario_immigration_act_2015.json",
		source_format="json_sections",
		source_url="https://www.ontario.ca/laws/statute/15o08",
	),
	"alberta.immigration_oversight_act": SourceDefinition(
		title="Immigration Oversight Act",
		citation="Immigration Oversight Act, S.A. 2026, c. I-0.3",
		relative_path="data/reference_library/provincial_json/alberta_immigration_oversight_act.json",
		source_format="json_sections",
		source_url="https://kings-printer.alberta.ca/",
	),
	"manitoba.worker_recruitment_protection_act": SourceDefinition(
		title="The Worker Recruitment and Protection Act",
		citation="The Worker Recruitment and Protection Act, C.C.S.M. c. W197",
		relative_path="data/reference_library/provincial_json/manitoba_worker_recruitment_protection_act.json",
		source_format="json_sections",
		source_url="https://web2.gov.mb.ca/laws/statutes/ccsm/w197.php",
	),
	"international.refugee_convention": SourceDefinition(
		title="Convention Relating to the Status of Refugees",
		citation="Convention Relating to the Status of Refugees",
		relative_path="data/reference_library/non_xml_authorities/refugee_convention_1951_unts_189.txt",
		source_format="text",
		source_url="https://treaties.un.org/doc/Publication/UNTS/Volume%20189/volume-189-I-2545-English.pdf",
	),
	"international.refugee_protocol": SourceDefinition(
		title="Protocol Relating to the Status of Refugees",
		citation="Protocol Relating to the Status of Refugees",
		relative_path="data/reference_library/non_xml_authorities/refugee_protocol_1967_unts_606.txt",
		source_format="text",
		source_url="https://treaties.un.org/doc/Publication/UNTS/Volume%20606/volume-606-I-8791-English.pdf",
	),
}

SOURCE_DEFINITIONS = {**XML_SOURCES, **NON_XML_SOURCES}


def parse_sections(path: Path) -> list[tuple[str, str | None, str]]:
	root = ET.parse(path).getroot()
	sections = []
	seen_numbers: set[str] = set()
	# Only the enacted text: sections quoted inside amending bills, "not in force" notes and schedules are
	# not addressable provisions and used to push look-alike numbers into the library.
	body = root.find("Body")
	for section in (body if body is not None else root).iter("Section"):
		label = section.findtext("Label")
		if not label:
			continue
		number = label.strip()
		if number in seen_numbers:
			continue
		text = " ".join(" ".join(section.itertext()).split())
		seen_numbers.add(number)
		sections.append((number, section.findtext("MarginalNote"), text))
	return sections


def _heading_unit(text: str) -> tuple[str, str | None] | None:
	match = re.match(r"(?:Section|Article|Art\.)\s+([0-9]+[A-Za-z]?(?:\.[0-9]+)?|[IVXLCDM]+)(?:\s*[-:]?\s*(.*))?$", text)
	if match is None:
		return None
	return match.group(1), (match.group(2) or None)


def parse_html_sections(path: Path) -> list[tuple[str, str | None, str]]:
	soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
	charter_part = next(
		(
			element
			for element in soup.find_all("h2", class_="Part")
			if "Canadian Charter of Rights and Freedoms" in element.get_text(" ", strip=True)
		),
		None,
	)
	justice_sections = soup.select("p.Section, p.Subsection")
	if justice_sections and (charter_part is not None or soup.select_one("a.sectionLabel") is not None):
		sections: list[tuple[str, str | None, str]] = []
		seen_numbers: set[str] = set()
		current_label: str | None = None
		elements = soup.find_all(["h2", "h3", "p", "ul", "ol"])
		if charter_part is not None:
			start = elements.index(charter_part)
			elements = elements[start:]
		for element in elements:
			if element is not charter_part and element.name == "h2" and "Part" in (element.get("class") or []):
				break
			if element.name == "h3" and "Subheading" in (element.get("class") or []):
				current_label = element.get_text(" ", strip=True)
				continue
			if element.name == "p" and element.select_one("a.sectionLabel") is not None:
				anchor = element.select_one("a.sectionLabel")
				number = anchor.get_text(" ", strip=True)
				if not number or number in seen_numbers:
					continue
				body = element.get_text(" ", strip=True)
				body = re.sub(rf"^{re.escape(number)}\s*", "", body)
				sections.append((number, current_label, body))
				seen_numbers.add(number)
			elif sections and element.name in {"ul", "ol"}:
				text = element.get_text(" ", strip=True)
				if text:
					number, label, body = sections[-1]
					sections[-1] = (number, label, f"{body} {text}".strip())
		return sections
	blocks = [element.get_text(" ", strip=True) for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"])]
	sections: list[tuple[str, str | None, str]] = []
	current: tuple[str, str | None, list[str]] | None = None
	seen_numbers: set[str] = set()
	for block in blocks:
		unit = _heading_unit(block)
		if unit is not None:
			if current is not None:
				number, label, text = current
				if number not in seen_numbers and text:
					sections.append((number, label, " ".join(text)))
					seen_numbers.add(number)
			number, label = unit
			current = (number, label, [])
		elif current is not None:
			current[2].append(block)
	if current is not None:
		number, label, text = current
		if number not in seen_numbers and text:
			sections.append((number, label, " ".join(text)))
	return sections


def parse_text_sections(path: Path) -> list[tuple[str, str | None, str]]:
	sections: list[tuple[str, str | None, str]] = []
	current: tuple[str, str | None, list[str]] | None = None
	seen_numbers: set[str] = set()
	for raw_line in path.read_text(encoding="utf-8").splitlines():
		line = " ".join(raw_line.split())
		if not line:
			continue
		unit = _heading_unit(line)
		if unit is not None:
			if current is not None:
				number, label, text = current
				if number not in seen_numbers and text:
					sections.append((number, label, " ".join(text)))
					seen_numbers.add(number)
			number, label = unit
			current = (number, label, [])
		elif current is not None:
			current[2].append(line)
	if current is not None:
		number, label, text = current
		if number not in seen_numbers and text:
			sections.append((number, label, " ".join(text)))
	return sections


_CONSTITUTION_ACTS = {
	"html_constitution_1867": ("CONSTITUTION ACT, 1867", "CANADA ACT 1982"),
	"html_constitution_1982": ("CONSTITUTION ACT, 1982", "ENDNOTES"),
}


def parse_constitution_sections(path: Path, source_format: str) -> list[tuple[str, str | None, str]]:
	"""Split one Act out of the combined Justice Laws page "The Constitution Acts 1867 to 1982"."""
	start_title, end_title = _CONSTITUTION_ACTS[source_format]
	soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
	for junk in soup.select("span.wb-invisible, a[href^='#end']"):
		junk.decompose()
	headings = soup.find_all("h2")
	start = next((h for h in headings if h.get_text(" ", strip=True).upper().startswith(start_title)), None)
	if start is None:
		return []
	sections: list[tuple[str, str | None, str]] = []
	seen_numbers: set[str] = set()
	label: str | None = None
	current: list | None = None

	def flush() -> None:
		if current is not None:
			number, part_label, parts = current
			text = " ".join(" ".join(parts).split())
			if text:
				sections.append((number, part_label, text))

	for element in start.find_all_next(["h2", "h3", "p", "ul", "ol"]):
		if element.name == "h2":
			title = element.get_text(" ", strip=True)
			if title.upper().startswith(end_title) or title.upper().startswith("ENDNOTES"):
				break
			flush()
			current = None
			label = title
		elif element.name == "h3":
			label = element.get_text(" ", strip=True)
		elif element.name == "p" and element.select_one("a.sectionLabel") is not None:
			flush()
			number = element.select_one("a.sectionLabel").get_text(" ", strip=True)
			if not number or number in seen_numbers:
				current = None
				continue
			seen_numbers.add(number)
			body = re.sub(rf"^{re.escape(number)}\s*", "", element.get_text(" ", strip=True))
			current = [number, label, [body]]
		elif current is not None and not any(c.startswith("MarginalNote") for c in (element.get("class") or [])):
			current[2].append(element.get_text(" ", strip=True))
	flush()
	return sections


def parse_json_sections(path: Path) -> list[tuple[str, str | None, str]]:
	"""Sections from an A2AJ snapshot: {"sections": [[number, text], ...]} (see extract_a2aj_provincial_acts.py)."""
	data = json.loads(path.read_text(encoding="utf-8"))
	sections: list[tuple[str, str | None, str]] = []
	seen_numbers: set[str] = set()
	for number, text in data.get("sections", []):
		number = str(number).strip()
		if not number or number in seen_numbers or not str(text).strip():
			continue
		seen_numbers.add(number)
		sections.append((number, None, str(text)))
	return sections


def parse_source_sections(path: Path, source_format: str) -> list[tuple[str, str | None, str]]:
	if source_format == "xml":
		return parse_sections(path)
	if source_format == "html":
		return parse_html_sections(path)
	if source_format == "text":
		return parse_text_sections(path)
	if source_format in _CONSTITUTION_ACTS:
		return parse_constitution_sections(path, source_format)
	if source_format == "json_sections":
		return parse_json_sections(path)
	raise ValueError(f"unsupported source format: {source_format}")


def index_source(session, instrument_key: str, source: SourceDefinition) -> int:
	path = PROJECT_ROOT / source.relative_path
	document = session.scalar(select(LegislationDocument).where(LegislationDocument.instrument_key == instrument_key))
	if document is None:
		document = LegislationDocument(instrument_key=instrument_key, title=source.title)
		session.add(document)
		session.flush()
	document.title = source.title
	document.citation = source.citation
	document.source_url = source.source_url
	document.local_path = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
	document.source_hash = hashlib.sha256(path.read_bytes()).hexdigest()
	session.execute(delete(LegislationSection).where(LegislationSection.document_id == document.id))
	rows = [
		LegislationSection(document_id=document.id, section_number=number, label=label, text=text, display_order=index)
		for index, (number, label, text) in enumerate(parse_source_sections(path, source.source_format))
	]
	session.add_all(rows)
	return len(rows)


def verify_identity(path: Path, title: str) -> bool:
	"""True when the XML's own short or long title carries the expected title (a wrong snapshot is rejected)."""
	root = ET.parse(path).getroot()
	wanted = re.sub(r"\W+", " ", title).strip().lower()
	for tag in ("ShortTitle", "LongTitle"):
		found = root.findtext(f".//{tag}")
		if found and wanted in re.sub(r"\W+", " ", found).strip().lower():
			return True
	return False


def dry_run(keys) -> None:
	"""Parse each snapshot and print its section counts; touches no database."""
	total = 0
	for key in keys:
		source = SOURCE_DEFINITIONS[key]
		path = PROJECT_ROOT / source.relative_path
		if not path.exists():
			print(f"{key}: file not found at {source.relative_path}")
			continue
		sections = parse_source_sections(path, source.source_format)
		ok = verify_identity(path, source.title) if source.source_format == "xml" and key in JUSTICE_LAWS_KEYS else None
		numbers = [number for number, _, _ in sections]
		empty = sum(1 for _, _, text in sections if not text.strip())
		total += len(sections)
		print(f"{key}: sections={len(sections)} empty_text={empty} first={numbers[:1]} last={numbers[-1:]} identity_ok={ok}")
	print(f"total sections: {total}")


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--instrument", choices=[*SOURCE_DEFINITIONS, "all"], default="all")
	parser.add_argument("--dry-run", action="store_true", help="parse and count only; no database access")
	parser.add_argument(
		"--only-missing",
		action="store_true",
		help="skip instruments that already have a document, so existing text is left untouched",
	)
	args = parser.parse_args()
	keys = SOURCE_DEFINITIONS if args.instrument == "all" else {args.instrument: SOURCE_DEFINITIONS[args.instrument]}
	if args.dry_run:
		dry_run(keys)
		return
	with SessionLocal() as session:
		existing = set(session.scalars(select(LegislationDocument.instrument_key))) if args.only_missing else set()
		for key, source in keys.items():
			if key in existing:
				print(f"{key}: skipped (already indexed)", flush=True)
				continue
			if key in JUSTICE_LAWS_KEYS and not verify_identity(PROJECT_ROOT / source.relative_path, source.title):
				print(f"{key}: REJECTED, the snapshot's title does not match {source.title!r}", flush=True)
				continue
			count = index_source(session, key, source)
			print(f"{key}: sections={count}", flush=True)
		session.commit()


if __name__ == "__main__":
	main()
