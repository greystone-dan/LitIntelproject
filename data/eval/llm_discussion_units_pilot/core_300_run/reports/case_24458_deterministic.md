# Discussion Units: case 24458

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **59**
- Continuity pairs: **58**
- Discussion Units: **4**
- Paragraph source hashes: **59**
- Sub-themes: **18**

## 24458:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8812355cb058d78777d65b79786503ce3fa440929a13a11acf0ba08a02316e64`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24458:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, september, canada, citizenship, december, immigration, ivis, permit`
- Display key terms: `september, december, ivis, permit`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: september, december, ivis, permit Rule/authority context: [1] This is an application for judicial review of a decision of an officer of Citizenship and Immigration Canada (the Officer) denying the Applicant’s application for a temporary resident visa and determining that the Ap Application context: [6] The Applicant applied for, and on June 1, 2012 was issued, a work permit valid to June 1, 2014, permitting the Applicant to work at IVIS Inc. Operative outcome context: He was granted a study permit for the period December 24, 2006 to January 31, 2008. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5150316` offsets `274-285`; context: [1] This is an application for judicial review of a decision of an officer of Citizenship and Immigration Canada (the Officer) denying the Applicant’s application for a temporary resident visa and determining that the Applicant engaged in misrepresentation with the result, pursuant to subsection 40(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA), that he is inadmissible to Canada for a period of two years.
- Evidence: `disposition` cue `granted` at chunk `5150317` offsets `52-59`; context: He was granted a study permit for the period December 24, 2006 to January 31, 2008.
- Evidence: `reasoning_application` cue `applied` at chunk `5150321` offsets `18-25`; context: [6] The Applicant applied for, and on June 1, 2012 was issued, a work permit valid to June 1, 2014, permitting the Applicant to work at IVIS Inc.

#### 24458:1:subtheme:2 · paragraphs 7-8

- Raw key terms: `angeles, applicant, application, canada, disclose, october, office, refusal`
- Display key terms: `angeles, disclose, october, office, refusal`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: angeles, disclose, october, office, refusal Application context: [7] The Applicant again applied for a temporary residency visa on October 11, 2012 at the CIC Seattle office. | Your failure to disclose the refusal of your application in that office, therefore, could have induced an error in the administration of the Act and regulations. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5150322` offsets `147-155`; context: In that application, in reply to the question “Have you ever been refused any kind of visa, admission, or been ordered to leave Canada or any other country.
- Evidence: `reasoning_application` cue `applied` at chunk `5150322` offsets `24-31`; context: [7] The Applicant again applied for a temporary residency visa on October 11, 2012 at the CIC Seattle office.
- Evidence: `evidence_fact` cue `evidence` at chunk `5150323` offsets `510-518`; context: Immigration records in Canada together with the information and evidence submitted in your application indicate that you engaged in unauthorized full-time employment whilst you were the holder of an off-campus work permit.
- Evidence: `reasoning_application` cue `therefore` at chunk `5150323` offsets `922-931`; context: Your failure to disclose the refusal of your application in that office, therefore, could have induced an error in the administration of the Act and regulations.
- Evidence: `counterargument_limitation` cue `but` at chunk `5150323` offsets `736-739`; context: The record shows that you were requested to surrender the document but failed to comply.

#### 24458:1:subtheme:3 · paragraphs 9-11

- Raw key terms: `applicant, error, application, clerical, consultant, declaration, immigration, made`
- Display key terms: `error, clerical, consultant, declaration, made`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: error, clerical, consultant, declaration, made Position/evidence statements: [10] In response, the Applicant submitted a Statutory Declaration in which he stated that a clerical error had been made by the immigration consultant who helped him with his application with the result that he had answe | [11] The Applicant also submitted a statutory declaration by Mr. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5150324` offsets `434-439`; context: The Applicant was given an opportunity to provide an explanation or documentary evidence to address this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5150324` offsets `409-417`; context: The Applicant was given an opportunity to provide an explanation or documentary evidence to address this issue.
- Evidence: `issue` cue `question` at chunk `5150325` offsets `236-244`; context: [10] In response, the Applicant submitted a Statutory Declaration in which he stated that a clerical error had been made by the immigration consultant who helped him with his application with the result that he had answered “no” to the question, “Have you ever been refused any kind of visa, admission, or been ordered to leave Canada or any other country?
- Evidence: `party_position` cue `submitted` at chunk `5150325` offsets `32-41`; context: [10] In response, the Applicant submitted a Statutory Declaration in which he stated that a clerical error had been made by the immigration consultant who helped him with his application with the result that he had answered “no” to the question, “Have you ever been refused any kind of visa, admission, or been ordered to leave Canada or any other country?
- Evidence: `party_position` cue `submitted` at chunk `5150326` offsets `24-33`; context: [11] The Applicant also submitted a statutory declaration by Mr.

#### 24458:1:subtheme:4 · paragraphs 12-14

- Raw key terms: `applicant, letter, officer, application, irpa, january, requirements, resident`
- Display key terms: `letter, officer, irpa, january, requirements, resident`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: letter, officer, irpa, january, requirements, resident Rule/authority context: Decision Under Review | As it had been determined that the Applicant had engaged in misrepresentation pursuant to subsection 40(1)(a) of the IPRA, the Applicant was inadmissible to Canada for a period of two years. Application context: [13] In the January 8, 2013 letter, the Officer stated that he was not satisfied that the Applicant met the requirements of the IRPA and the Immigration and Refugee Protection Regulations, SOR/2002-22 (the IRPA Regulatio Operative outcome context: Specifically, the Applicant had denied previously being refused a visa when, in fact, he had been refused by the CIC Los Angeles office. Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Under` at chunk `5150327` offsets `150-155`; context: Decision Under Review
- Evidence: `reasoning_application` cue `therefore` at chunk `5150328` offsets `250-259`; context: [13] In the January 8, 2013 letter, the Officer stated that he was not satisfied that the Applicant met the requirements of the IRPA and the Immigration and Refugee Protection Regulations, SOR/2002-22 (the IRPA Regulations) and that the Officer was, therefore, refusing his application.
- Evidence: `evidence_fact` cue `record` at chunk `5150329` offsets `581-587`; context: Further, that the Applicant had denied engaging in unauthorized employment whereas the record and his own application indicated otherwise.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5150329` offsets `822-833`; context: As it had been determined that the Applicant had engaged in misrepresentation pursuant to subsection 40(1)(a) of the IPRA, the Applicant was inadmissible to Canada for a period of two years.
- Evidence: `disposition` cue `denied` at chunk `5150329` offsets `389-395`; context: Specifically, the Applicant had denied previously being refused a visa when, in fact, he had been refused by the CIC Los Angeles office.

#### Section text

Goburdhun v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-09-23
Neutral citation
2013 FC 971
File numbers
IMM-674-13
Notes
A correction was made on February 6, 2017.
Decision Content
Federal Court
Cour fédérale
Date: 20130923
Docket: IMM-674-13
Citation: 2013 FC 971
Ottawa, Ontario, September 23, 2013
PRESENT: The Honourable Madam Justice Strickland
BETWEEN:
LOCHANDATH GOBURDHUN
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of an officer of Citizenship and Immigration Canada (the Officer) denying the Applicant’s application for a temporary resident visa and determining that the Applicant engaged in misrepresentation with the result, pursuant to subsection 40(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA), that he is inadmissible to Canada for a period of two years. The application is brought pursuant to subsection 72(1) of the IRPA.
Background

[2] The Applicant is a citizen of Mauritius. He was granted a study permit for the period December 24, 2006 to January 31, 2008. This was renewed for the period January 4, 2008 to September 27, 2008 and he was issued a work permit on April 4, 2008, also valid to September 27, 2008 which permitted him to work up to 20 hours a week during regular academic sessions and full time during scheduled breaks. The work permit is referred to by Citizenship and Immigration Canada (CIC) as an off-campus work permit (OCWP). His study permit was again renewed for the period September 15, 2008 to April 30, 2009 and an OCWP on the same terms was issued on October 15, 2008 also valid to April 30, 2009. A final study permit and OCWP were issued on April 24, 2009 valid to May 16, 2012.

[3] From January 2010 to December 2010, the Applicant attended the Northern Alberta Institute of Technology (NAIT) and successfully completed a full-time, one year Water and Waste Technician Program. While attending the NAIT, he held a part time practicum position at IVIS Inc., from May 2010 to September 2010, as permitted by the OCWP.

[4] Upon graduation, the Applicant commenced full time employment with IVIS Inc., as of December 20, 2010 and continuing to September 2012. He was no longer a student and did not obtain an alternate work permit until June 1, 2012.

[5] On November 3, 2011, the Applicant was refused a temporary resident visa by the CIC office in Los Angeles.

[6] The Applicant applied for, and on June 1, 2012 was issued, a work permit valid to June 1, 2014, permitting the Applicant to work at IVIS Inc.

[7] The Applicant again applied for a temporary residency visa on October 11, 2012 at the CIC Seattle office. In that application, in reply to the question “Have you ever been refused any kind of visa, admission, or been ordered to leave Canada or any other country.” He responded “no” and did not disclose the November 3, 2011 temporary residency visa refusal in Los Angeles.

[8] On October 31, 2012, the Officer sent the Applicant a “fairness letter” pointing out that the Applicant had failed to disclose the prior temporary residency visa refusal in Los Angeles. This stated, in part:
It is difficult to escape the conclusion that your failure to disclose the previous refused TRV application in your application to this office was a deliberate attempt to conceal both the refusals themselves and the reasons for them. Immigration records in Canada together with the information and evidence submitted in your application indicate that you engaged in unauthorized full-time employment whilst you were the holder of an off-campus work permit. The record shows that you were requested to surrender the document but failed to comply. This was the primary reason for the refusal of your application by the Los Angeles office. Your failure to disclose the refusal of your application in that office, therefore, could have induced an error in the administration of the Act and regulations.

[9] The letter also referred to subsection 40(1)(a) of the IRPA which states that a foreign national is inadmissible due to misrepresentation as a result of directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of the IRPA. The Applicant was given an opportunity to provide an explanation or documentary evidence to address this issue.

[10] In response, the Applicant submitted a Statutory Declaration in which he stated that a clerical error had been made by the immigration consultant who helped him with his application with the result that he had answered “no” to the question, “Have you ever been refused any kind of visa, admission, or been ordered to leave Canada or any other country?” when the correct answer was “yes”. He stated that this was not an intentional mistake, and, that he had never engaged in any unauthorized full-time employment while he was the holder of an OCWP and had never received any request from any immigration office to surrender any document. He attached all of the study and work permits he had received.

[11] The Applicant also submitted a statutory declaration by Mr. Randy McDonald who identified himself as an administrative assistant at Canwrx Group Ltd., the immigration consultant that had acted as the Applicant’s representative in making the October 2012 temporary residency visa application. Mr. McDonald confirmed that he had made the clerical error described above.

[12] By letter dated January 8, 2013, the Officer advised the Applicant that he did not meet the requirements for a temporary resident visa.
Decision Under Review

[13] In the January 8, 2013 letter, the Officer stated that he was not satisfied that the Applicant met the requirements of the IRPA and the Immigration and Refugee Protection Regulations, SOR/2002-22 (the IRPA Regulations) and that the Officer was, therefore, refusing his application.

[13] The basis for the refusal was that the Officer was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary resident as he had contravened the conditions of admission on a previous stay in Canada and as he had not answered all of the questions in his application truthfully as required by subsection 16(1) of the IRPA. Specifically, the Applicant had denied previously being refused a visa when, in fact, he had been refused by the CIC Los Angeles office. Further, that the Applicant had denied engaging in unauthorized employment whereas the record and his own application indicated otherwise. The letter also stated that the Applicant had no authority to work after he completed his studies at the NAIT. As it had been determined that the Applicant had engaged in misrepresentation pursuant to subsection 40(1)(a) of the IPRA, the Applicant was inadmissible to Canada for a period of two years.
Applicable Law and Policy

## 24458:2 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ed33185947b32e179dadc94c662379811612ee7e64746b3074845d549506830b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24458:2:subtheme:1 · paragraphs 15-15

- Raw key terms: `administration, agent, alablement, answer, application, appliquent, apply, auteur`
- Display key terms: `administration, agent, alablement, answer, appliquent, apply, auteur`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: administration, agent, alablement, answer, appliquent, apply, auteur Rule/authority context: (1) A permanent resident or a foreign national is inadmissible for misrepresentation (a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce Application context: (1) A foreign national must, before entering Canada, apply to an officer for a visa or for any other document required by the regulations. Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5150330` offsets `658-666`; context: (1) A person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.
- Evidence: `governing_rule` cue `under` at chunk `5150330` offsets `1293-1298`; context: (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
[…]
(2) The following provisions govern subsection (1):
(a) the permanent resident or the foreign national continues to be inadmissible for misrepresentation for a period of two years following, in the case of a determination outside Canada, a final determination of inadmissibility under subsection (1) or, in the case of a determination in Canada, the date the removal order is enforced; and
[…]
PARTIE 1
IMMIGRATION AU CANADA
SECTION 1
FORMALITÉS ET SÉLECTION
Formalités
11.
- Evidence: `reasoning_application` cue `apply` at chunk `5150330` offsets `194-199`; context: (1) A foreign national must, before entering Canada, apply to an officer for a visa or for any other document required by the regulations.

#### Section text

[14] The relevant provisions of the IRPA are as follows:
PART 1
IMMIGRATION TO CANADA
DIVISION 1 REQUIREMENTS AND SELECTION
Requirements
11. (1) A foreign national must, before entering Canada, apply to an officer for a visa or for any other document required by the regulations. The visa or document may be issued if, following an examination, the officer is satisfied that the foreign national is not inadmissible and meets the requirements of this Act.
[…]
Obligation — answer
Truthfully
16. (1) A person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.
[…]
Misrepresentation
40. (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
[…]
(2) The following provisions govern subsection (1):
(a) the permanent resident or the foreign national continues to be inadmissible for misrepresentation for a period of two years following, in the case of a determination outside Canada, a final determination of inadmissibility under subsection (1) or, in the case of a determination in Canada, the date the removal order is enforced; and
[…]
PARTIE 1
IMMIGRATION AU CANADA
SECTION 1
FORMALITÉS ET SÉLECTION
Formalités
11. (1) L’étranger doit, préalablement à son entrée au Canada, demander à l’agent les visa et autres documents requis par règlement. L’agent peut les délivrer sur preuve, à la suite d’un contrôle, que l’étranger n’est pas interdit de territoire et se conforme à la présente loi.
[…]
Obligation du
Demandeur
16. (1) L’auteur d’une demande au titre de la présente loi doit répondre véridiquement aux
questions qui lui sont posées lors du contrôle,
[…]
Fausses déclarations
40. (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une
présentation erronée sur un fait important quant à un objet pertinent, ou une réticence
sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente
loi;
[…]
(2) Les dispositions suivantes s’appliquent au paragraphe (1):
(a) l’interdiction de territoire court pour les deux ans suivant la décision la constatant en dernier ressort, si le résident permanent ou l’étranger n’est pas au pays, ou suivant l’exécution de la mesure de renvoi;
[…]

## 24458:3 · paragraphs 16-57

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7f1517b0f8ed32b62449fa933d17a3f88189fd4cab3b2e0f7a32a93242e4d1ef`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24458:3:subtheme:1 · paragraphs 16-17

- Raw key terms: `canada, document, visa, accordance, agent, agraira, another, applicable`
- Display key terms: `document, visa, accordance, agent, agraira, another, applicable`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: document, visa, accordance, agent, agraira, another, applicable Position/evidence statements: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national (a) has applied in accordance with these Regulations for a temporary reside Rule/authority context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national (a) has applied in accordance with these Regulations for a temporary reside Application context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national (a) has applied in accordance with these Regulations for a temporary reside Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5150331` offsets `144-149`; context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national
(a) has applied in accordance with these Regulations for a temporary resident visa as a member of the visitor, worker or student class;
(b) will leave Canada by the end of the period authorized for their stay under Division 2;
(c) holds a passport or other document that they may use to enter the country that issued it or another country;
(d) meets the requirements applicable to that class;
(e) is not inadmissible; and
(f) meets the requirements of subsections 30(2) and (3), if they must submit to a medical examination under paragraph 16(2)(b) of the Act.
- Evidence: `party_position` cue `submit` at chunk `5150331` offsets `764-770`; context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national
(a) has applied in accordance with these Regulations for a temporary resident visa as a member of the visitor, worker or student class;
(b) will leave Canada by the end of the period authorized for their stay under Division 2;
(c) holds a passport or other document that they may use to enter the country that issued it or another country;
(d) meets the requirements applicable to that class;
(e) is not inadmissible; and
(f) meets the requirements of subsections 30(2) and (3), if they must submit to a medical examination under paragraph 16(2)(b) of the Act.
- Evidence: `governing_rule` cue `under` at chunk `5150331` offsets `481-486`; context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national
(a) has applied in accordance with these Regulations for a temporary resident visa as a member of the visitor, worker or student class;
(b) will leave Canada by the end of the period authorized for their stay under Division 2;
(c) holds a passport or other document that they may use to enter the country that issued it or another country;
(d) meets the requirements applicable to that class;
(e) is not inadmissible; and
(f) meets the requirements of subsections 30(2) and (3), if they must submit to a medical examination under paragraph 16(2)(b) of the Act.
- Evidence: `reasoning_application` cue `applied` at chunk `5150331` offsets `280-287`; context: An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national
(a) has applied in accordance with these Regulations for a temporary resident visa as a member of the visitor, worker or student class;
(b) will leave Canada by the end of the period authorized for their stay under Division 2;
(c) holds a passport or other document that they may use to enter the country that issued it or another country;
(d) meets the requirements applicable to that class;
(e) is not inadmissible; and
(f) meets the requirements of subsections 30(2) and (3), if they must submit to a medical examination under paragraph 16(2)(b) of the Act.

#### 24458:3:subtheme:2 · paragraphs 18-19

- Raw key terms: `material, matter, misrepresentation, addresses, administration, applicable, applicants, applying`
- Display key terms: `material, matter, misrepresentation, addresses, administration, applicable, applying`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: material, matter, misrepresentation, addresses, administration, applicable, applying Rule/authority context: 1) and that persons who misrepresent or withhold material facts, either directly or indirectly, relating to a relevant matter that induces or could induce an error in the administration of the Act are inadmissible to Can | Standard of Review Application context: [18] I would frame the issue in this matter as being whether it was reasonable for the Officer to conclude that there was a material misrepresentation. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5150333` offsets `794-800`; context: Issues
- Evidence: `governing_rule` cue `pursuant to` at chunk `5150333` offsets `437-448`; context: 1) and that persons who misrepresent or withhold material facts, either directly or indirectly, relating to a relevant matter that induces or could induce an error in the administration of the Act are inadmissible to Canada pursuant to subsection 40(1)(a) of the IRPA.
- Evidence: `issue` cue `issue` at chunk `5150334` offsets `23-28`; context: [18] I would frame the issue in this matter as being whether it was reasonable for the Officer to conclude that there was a material misrepresentation.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5150334` offsets `152-170`; context: Standard of Review
- Evidence: `reasoning_application` cue `conclude` at chunk `5150334` offsets `98-106`; context: [18] I would frame the issue in this matter as being whether it was reasonable for the Officer to conclude that there was a material misrepresentation.

#### 24458:3:subtheme:3 · paragraphs 20-21

- Raw key terms: `canada, citizenship, court, held, immigration, para, review, standard`
- Display key terms: `para, review, standard`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: para, review, standard Rule/authority context: [18] The majority of the Supreme Court has held that “[a]n exhaustive analysis is not required in every case to determine the proper standard of review. | [19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation purs Application context: [19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation purs Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5150335` offsets `182-189`; context: ” Courts must first ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of deference to be accorded to a decision-maker with regard to a particular category of question (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at paras 57 and 62 [Dunsmuir]; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12, [2009] 1 SCR 339 at para 53 [Khosa]).
- Evidence: `governing_rule` cue `standard of review` at chunk `5150335` offsets `133-151`; context: [18] The majority of the Supreme Court has held that “[a]n exhaustive analysis is not required in every case to determine the proper standard of review.
- Evidence: `issue` cue `whether` at chunk `5150336` offsets `95-102`; context: [19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation pursuant to subsection 40(1)(a) of the IRPA is reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5150336` offsets `45-63`; context: [19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation pursuant to subsection 40(1)(a) of the IRPA is reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `5150336` offsets `70-77`; context: [19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation pursuant to subsection 40(1)(a) of the IRPA is reasonableness.

#### 24458:3:subtheme:4 · paragraphs 22-24

- Raw key terms: `applicant, above, facts, material, acceptable, analysis, application, assisting`
- Display key terms: `above, facts, material, acceptable, analysis, assisting`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: above, facts, material, acceptable, analysis, assisting Position/evidence statements: [22] The Applicant submits that he brought the error to the attention of the immigration consultant who was assisting him and that he believed that the error would be corrected before the consultant submitted the applica Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5150337` offsets `213-220`; context: [20] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility of the decision-making process and also with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law” (Dunsmuir, above, at para 47; Khosa, above at para 59).
- Evidence: `party_position` cue `submits` at chunk `5150339` offsets `19-26`; context: [22] The Applicant submits that he brought the error to the attention of the immigration consultant who was assisting him and that he believed that the error would be corrected before the consultant submitted the application.

#### 24458:3:subtheme:5 · paragraphs 25-29

- Raw key terms: `applicant, application, respondent, accordingly, decision, immigration, information, submits`
- Display key terms: `accordingly, information, submits`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: accordingly, information, submits Position/evidence statements: [23] Further, the Applicant submits that only if information affects the process undertaken or the final decision will it be considered to be material (ENF 2; Ali v Canada (Minister of Citizenship and Immigration), 2008  | [24] The Respondent submits that the Applicant’s failure to disclose the previous temporary resident visa application constituted a material misrepresentation. Application context: Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided. | [25] The Respondent refers to the requirements of the IRPA, the IRPA Regulations as well as ENF 2 and concludes that the Officer properly applied these provisions which required the Applicant to provide complete and trut Operative outcome context: Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided. Evidence spans paragraphs 25-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5150340` offsets `258-266`; context: Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided.
- Evidence: `party_position` cue `submits` at chunk `5150340` offsets `28-35`; context: [23] Further, the Applicant submits that only if information affects the process undertaken or the final decision will it be considered to be material (ENF 2; Ali v Canada (Minister of Citizenship and Immigration), 2008 FC 166 [Ali]).
- Evidence: `reasoning_application` cue `because` at chunk `5150340` offsets `347-354`; context: Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided.
- Evidence: `disposition` cue `denied` at chunk `5150340` offsets `301-307`; context: Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided.
- Evidence: `party_position` cue `submits` at chunk `5150341` offsets `20-27`; context: [24] The Respondent submits that the Applicant’s failure to disclose the previous temporary resident visa application constituted a material misrepresentation.
- Evidence: `reasoning_application` cue `concludes` at chunk `5150342` offsets `102-111`; context: [25] The Respondent refers to the requirements of the IRPA, the IRPA Regulations as well as ENF 2 and concludes that the Officer properly applied these provisions which required the Applicant to provide complete and truthful information.
- Evidence: `party_position` cue `submits` at chunk `5150343` offsets `20-27`; context: [26] The Respondent submits that the Applicant was aware of the error in his application and, while he may have brought this to the attention of his immigration consultant, he himself signed and declared the application to contain truthful answers.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5150343` offsets `249-260`; context: Accordingly, this error was not beyond his control, he was alive to it and could and should have reviewed the application prior to signing it to ensure that the error had been rectified and that the application was accurate.
- Evidence: `evidence_fact` cue `determined that` at chunk `5150344` offsets `324-339`; context: The Officer examined the file and determined that this contradicted the Applicant’s own application, the CIC record and other evidence.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5150344` offsets `426-437`; context: Accordingly, it was open for the Officer to conclude that the Applicant had continued to be dishonest.

#### 24458:3:subtheme:6 · paragraphs 30-38

- Raw key terms: `applicant, application, above, canada, court, immigration, information, justice`
- Display key terms: `above, information, justice`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: above, information, justice Position/evidence statements: [29] Here, the Applicant submits that he had no knowledge of the misrepresentation which was caused by his immigration consultant’s failure to correct a clerical error. | Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. Rule/authority context: [28] In Oloumi, above, Justice Tremblay-Lamer describes general principles arising from this Court’s treatment of section 40 of the IRPA which are summarized below together with other such principles arising from the jur Application context: [28] In Oloumi, above, Justice Tremblay-Lamer describes general principles arising from this Court’s treatment of section 40 of the IRPA which are summarized below together with other such principles arising from the jur | Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. Operative outcome context: that she had been “granted landing… by reason of any fraudulent or improper means”. Evidence spans paragraphs 30-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5150345` offsets `2087-2094`; context: To accomplish this, the onus is placed on the applicant to ensure the completeness and accuracy of their application (Jiang, above, at para 35;Wang, above, at paras 55-56);
- An applicant has a duty of candour to provide complete, honest and truthful information in every manner when applying for entry into Canada (Bodine v Canada (Minister of Citizenship and Immigration), 2008 FC 848 at para 41; Baro v Canada (Minister of Citizenship and Immigration), 2007 FC 1299 at para 15);
- As the applicant is responsible for the content of an application which they sign, the applicant’s belief that he or she was not misrepresenting a material fact is not reasonable where they fail to review their application and ensure the completeness and veracity of the document before signing it (Haque, above, at para 16; Cao v Canada (Minister of Citizenship and Immigration), 2010 FC 450 at para 31 [Cao]);
- In determining whether a misrepresentation is material, regard must be had for the wording of the provision and its underlying purpose (Oloumi, above, at para 22);
- A misrepresentation need not be decisive or determinative.
- Evidence: `governing_rule` cue `principles` at chunk `5150345` offsets `64-74`; context: [28] In Oloumi, above, Justice Tremblay-Lamer describes general principles arising from this Court’s treatment of section 40 of the IRPA which are summarized below together with other such principles arising from the jurisprudence:
- Section 40 is to be given a broad interpretation in order to promote its underlying purpose (Khan v Canada (Minister of Citizenship and Immigration), 2008 FC 512 at para 25 [Khan]);
- Section 40 is broadly worded to encompasses misrepresentations even if made by another party, including an immigration consultant, without the knowledge of the applicant (Jiang v Canada (Minister of Citizenship and Immigration), 2011 FC 942 at para 35 [Jiang]; Wang v Canada (Minister of Citizenship and Immigration), 2005 FC 1059 at paras 55-56 [Wang]);
- The exception to this rule is narrow and applies only to truly extraordinary circumstances where an applicant honestly and reasonably believed that they were not misrepresenting a material fact and knowledge of the misrepresentation was beyond the applicant’s control (Medel, above);
- The objective of section 40 is to deter misrepresentation and maintain the integrity of the immigration process.
- Evidence: `reasoning_application` cue `applies` at chunk `5150345` offsets `816-823`; context: [28] In Oloumi, above, Justice Tremblay-Lamer describes general principles arising from this Court’s treatment of section 40 of the IRPA which are summarized below together with other such principles arising from the jurisprudence:
- Section 40 is to be given a broad interpretation in order to promote its underlying purpose (Khan v Canada (Minister of Citizenship and Immigration), 2008 FC 512 at para 25 [Khan]);
- Section 40 is broadly worded to encompasses misrepresentations even if made by another party, including an immigration consultant, without the knowledge of the applicant (Jiang v Canada (Minister of Citizenship and Immigration), 2011 FC 942 at para 35 [Jiang]; Wang v Canada (Minister of Citizenship and Immigration), 2005 FC 1059 at paras 55-56 [Wang]);
- The exception to this rule is narrow and applies only to truly extraordinary circumstances where an applicant honestly and reasonably believed that they were not misrepresenting a material fact and knowledge of the misrepresentation was beyond the applicant’s control (Medel, above);
- The objective of section 40 is to deter misrepresentation and maintain the integrity of the immigration process.
- Evidence: `issue` cue `question` at chunk `5150346` offsets `283-291`; context: The Applicants submits that he instructed the consultant to change the answer of “no” to “yes” in response to the question “Have you ever been refused any kind of visa, admission or been ordered to leave Canada or another country?
- Evidence: `party_position` cue `submits` at chunk `5150346` offsets `25-32`; context: [29] Here, the Applicant submits that he had no knowledge of the misrepresentation which was caused by his immigration consultant’s failure to correct a clerical error.
- Evidence: `counterargument_limitation` cue `However` at chunk `5150346` offsets `401-408`; context: ” However, that the consultant failed to do so before submitting the application.
- Evidence: `party_position` cue `claimed` at chunk `5150349` offsets `387-394`; context: Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error.
- Evidence: `reasoning_application` cue `because` at chunk `5150349` offsets `374-381`; context: Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error.
- Evidence: `disposition` cue `granted` at chunk `5150349` offsets `808-815`; context: that she had been “granted landing… by reason of any fraudulent or improper means”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5150350` offsets `49-58`; context: [36] When considered within its factual context, therefore, the exception in Medel is relatively narrow.
- Evidence: `party_position` cue `argued` at chunk `5150351` offsets `55-61`; context: [32] In Haque, above, the applicants therein similarly argued that the misrepresentations were not intentional and that it was their consultant who erred in filling out the application.
- Evidence: `evidence_fact` cue `found that` at chunk `5150353` offsets `679-689`; context: Justice Rennie found that the applicant had not persuaded the Court that it was unreasonable for the officer to find this to be a material misrepresentation.
- Evidence: `reasoning_application` cue `applied` at chunk `5150353` offsets `221-228`; context: The applicant therein indicated on his application form that he had never applied for, or been refused, immigration status in Canada.

#### 24458:3:subtheme:7 · paragraphs 39-41

- Raw key terms: `material, misrepresentation, applicant, disclose, error, irpa, situation, subsection`
- Display key terms: `material, misrepresentation, disclose, error, irpa, situation, subsection`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: material, misrepresentation, disclose, error, irpa, situation, subsection Position/evidence statements: He was aware of the error in his application and was responsible for ensuring that, when submitted, his application was accurate and truthful. Application context: The Applicant therefore failed to demonstrate that he honestly and reasonably believed that he was not withholding potentially material information. | ENF 2 gives as an example of a situation constituting misrepresentation, one where an applicant fails to disclose that they recently applied for a visa to Canada. Evidence spans paragraphs 39-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5150354` offsets `137-142`; context: [34] In my view, the Applicant in this case clearly made a misrepresentation by failing to disclose the prior CIC Los Angeles refusal to issue a temporary residency visa in his October 2012 application.
- Evidence: `party_position` cue `submitted` at chunk `5150354` offsets `292-301`; context: He was aware of the error in his application and was responsible for ensuring that, when submitted, his application was accurate and truthful.
- Evidence: `reasoning_application` cue `therefore` at chunk `5150354` offsets `611-620`; context: The Applicant therefore failed to demonstrate that he honestly and reasonably believed that he was not withholding potentially material information.
- Evidence: `counterargument_limitation` cue `However` at chunk `5150354` offsets `346-353`; context: However, he failed to review the application before it was submitted.
- Evidence: `issue` cue `question` at chunk `5150355` offsets `26-34`; context: [35] This leaves only the question of whether the misrepresentation was material.
- Evidence: `reasoning_application` cue `applied` at chunk `5150356` offsets `415-422`; context: ENF 2 gives as an example of a situation constituting misrepresentation, one where an applicant fails to disclose that they recently applied for a visa to Canada.

#### 24458:3:subtheme:8 · paragraphs 42-47

- Raw key terms: `irpa, material, applicant, error, misrepresentation, above, administration, application`
- Display key terms: `irpa, material, error, misrepresentation, above, administration`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: irpa, material, error, misrepresentation, above, administration Position/evidence statements: [40] In the present case, the Respondent submits that the Officer could have been prevented from undertaking an appropriate investigation and verification process and, therefore, could have erroneously determined that th Application context: This Court held that the misrepresented fact was material because federal skilled workers must demonstrate language proficiency to be accepted. | [40] In the present case, the Respondent submits that the Officer could have been prevented from undertaking an appropriate investigation and verification process and, therefore, could have erroneously determined that th Evidence spans paragraphs 42-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5150357` offsets `36-43`; context: [37] As noted above, in determining whether a misrepresentation is material, regard must be had for the wording of the provision and its underlying purpose.
- Evidence: `reasoning_application` cue `because` at chunk `5150359` offsets `208-215`; context: This Court held that the misrepresented fact was material because federal skilled workers must demonstrate language proficiency to be accepted.
- Evidence: `party_position` cue `submits` at chunk `5150360` offsets `41-48`; context: [40] In the present case, the Respondent submits that the Officer could have been prevented from undertaking an appropriate investigation and verification process and, therefore, could have erroneously determined that the Applicant met all the requirements of the IRPA had the Officer relied on the Applicants denial of a prior visa refusal.
- Evidence: `evidence_fact` cue `determined that` at chunk `5150360` offsets `202-217`; context: [40] In the present case, the Respondent submits that the Officer could have been prevented from undertaking an appropriate investigation and verification process and, therefore, could have erroneously determined that the Applicant met all the requirements of the IRPA had the Officer relied on the Applicants denial of a prior visa refusal.
- Evidence: `reasoning_application` cue `therefore` at chunk `5150360` offsets `168-177`; context: [40] In the present case, the Respondent submits that the Officer could have been prevented from undertaking an appropriate investigation and verification process and, therefore, could have erroneously determined that the Applicant met all the requirements of the IRPA had the Officer relied on the Applicants denial of a prior visa refusal.
- Evidence: `counterargument_limitation` cue `However` at chunk `5150362` offsets `153-160`; context: However, section 9.

#### 24458:3:subtheme:9 · paragraphs 48-49

- Raw key terms: `applicant, canada, immigration, misrepresentation, ability, above, accept, access`
- Display key terms: `misrepresentation, ability, above, accept, access`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: misrepresentation, ability, above, accept, access Application context: [43] I also cannot accept the Applicant’s submission made when appearing before me that, because CIC has access to the whole of his immigration history, an incorrect answer in his application is not material. Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5150363` offsets `803-810`; context: What matters is whether the misrepresentation induced or could have induced such an error.
- Evidence: `reasoning_application` cue `because` at chunk `5150363` offsets `89-96`; context: [43] I also cannot accept the Applicant’s submission made when appearing before me that, because CIC has access to the whole of his immigration history, an incorrect answer in his application is not material.

#### 24458:3:subtheme:10 · paragraphs 50-53

- Raw key terms: `applicant, application, issued, ocwp, permit, refusal, time, work`
- Display key terms: `issued, ocwp, permit, refusal, time, work`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: issued, ocwp, permit, refusal, time, work Position/evidence statements: [45] At the hearing before me the Applicant also submitted that because, between the time when the temporary residency visa was refused in Los Angeles and the time of the refusal in Seattle he was issued a work permit, t Application context: [45] At the hearing before me the Applicant also submitted that because, between the time when the temporary residency visa was refused in Los Angeles and the time of the refusal in Seattle he was issued a work permit, t | Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary residence based on the prior contravention was reasonable. Evidence spans paragraphs 50-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5150365` offsets `731-739`; context: And finally, the question asked on the temporary visa application was whether the Applicant had ever been refused any kind of visa, thus it was incumbent upon him to disclose the prior refusal regardless of the subsequent issuance of the work permit.
- Evidence: `party_position` cue `submitted` at chunk `5150365` offsets `49-58`; context: [45] At the hearing before me the Applicant also submitted that because, between the time when the temporary residency visa was refused in Los Angeles and the time of the refusal in Seattle he was issued a work permit, this rendered the first refusal immaterial as the immigration authorities were clearly satisfied with his subsequent application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5150365` offsets `690-698`; context: Secondly, it is not known if the Applicant was requested to or did disclose the refused temporary residency when he applied for the work permit as neither the Applicant nor the Respondent led evidence on this point.
- Evidence: `reasoning_application` cue `because` at chunk `5150365` offsets `64-71`; context: [45] At the hearing before me the Applicant also submitted that because, between the time when the temporary residency visa was refused in Los Angeles and the time of the refusal in Seattle he was issued a work permit, this rendered the first refusal immaterial as the immigration authorities were clearly satisfied with his subsequent application.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5150366` offsets `735-746`; context: Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary residence based on the prior contravention was reasonable.
- Evidence: `counterargument_limitation` cue `However` at chunk `5150366` offsets `242-249`; context: However, this is contradicted by Attachment A of his October 11, 2012 application and the September 7, 2012 letter from IVIS Inc.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5150368` offsets `29-38`; context: [48] The Respondent filed an affidavit of Ms.

#### 24458:3:subtheme:11 · paragraphs 54-55

- Raw key terms: `above, applicant, full, nait, ocwp, officer, record, refused`
- Display key terms: `above, full, nait, ocwp, officer, refused`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: above, full, nait, ocwp, officer, refused Evidence spans paragraphs 54-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5150369` offsets `743-749`; context: Moreover, it is trite law that new evidence is only admissible on judicial review to resolve issues of procedural fairness or jurisdiction which exceptions have no application in this case (Oloumi, above, at para 10; Alabadleh v Canada (Minister of Citizenship and Immigration), 2006 FC 716 at para 6; Albajjali v Canada (Minister of Citizenship and Immigration), 2013 FC 660 at para 12).
- Evidence: `evidence_fact` cue `affidavit` at chunk `5150369` offsets `40-49`; context: [49] It appears that the purpose of the affidavit was to bolster the CTR which contains no record supporting the finding by the Officer that the Applicant was actually asked, but refused, to surrender his OCWP nor explaining why he was not in compliance with the OCWP at some time before a February 1, 2012 GMCS entry which stated this to be the case but at which time the Applicant was enrolled full time at NAIT.
- Evidence: `evidence_fact` cue `record` at chunk `5150370` offsets `279-285`; context: [50] However, even in the absence of an evidentiary basis for the assertion that the Applicant was requested to and refused to surrender the OCWP and that this was the primary reason for the Los Angeles refusal, there was, as set out above, a sufficient evidentiary basis in the record before the Officer to support the fact that the Applicant worked full time while holding only a OCWP, after graduation from NAIT, from December 20, 2010 to June 1, 2012.

#### 24458:3:subtheme:12 · paragraphs 56-57

- Raw key terms: `accordingly, admission, alberta, applicant, application, arises, august, authorized`
- Display key terms: `accordingly, admission, alberta, arises, august, authorized`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: accordingly, admission, alberta, arises, august, authorized Rule/authority context: Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary resident and that he had made material misrepresentations pursuant to subsection 40 Application context: Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary resident and that he had made material misrepresentations pursuant to subsection 40 Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is dismissed. Evidence spans paragraphs 56-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5150371` offsets `715-723`; context: No question of general importance for certification was proposed and none arises.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5150371` offsets `512-523`; context: Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary resident and that he had made material misrepresentations pursuant to subsection 40(1)(a) of the IRPA was reasonable and defensible in respect to the facts and the law.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5150371` offsets `317-328`; context: Accordingly, the Officer’s finding that he was not satisfied that the Applicant would leave Canada at the end of his stay as a temporary resident and that he had made material misrepresentations pursuant to subsection 40(1)(a) of the IRPA was reasonable and defensible in respect to the facts and the law.
- Evidence: `disposition` cue `dismissed` at chunk `5150371` offsets `701-710`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed.

#### Section text

[15] The relevant provisions of the IRPA Regulations state:
PART 9
TEMPORARY RESIDENTS
DIVISION 1
TEMPORARY RESIDENT VISA
179. An officer shall issue a temporary resident visa to a foreign national if, following an examination, it is established that the foreign national
(a) has applied in accordance with these Regulations for a temporary resident visa as a member of the visitor, worker or student class;
(b) will leave Canada by the end of the period authorized for their stay under Division 2;
(c) holds a passport or other document that they may use to enter the country that issued it or another country;
(d) meets the requirements applicable to that class;
(e) is not inadmissible; and
(f) meets the requirements of subsections 30(2) and (3), if they must submit to a medical examination under paragraph 16(2)(b) of the Act.
PARTIE 9
RÉSIDENTS TEMPORAIRES
SECTION 1
VISA DE RÉSIDENT TEMPORAIRE
179. L’agent délivre un visa de résident temporaire à l’étranger si, à l’issue d’un contrôle, les éléments suivants sont établis:
a) l’étranger en a fait, conformément au présent règlement, la demande au titre de la catégorie des visiteurs, des travailleurs ou des étudiants;
b) il quittera le Canada à la fin de la période de séjour autorisée qui lui est applicable au titre de la section 2;
c) il est titulaire d’un passeport ou autre document qui lui permet d’entrer dans le pays qui l’a délivré ou dans un autre pays;
d) il se conforme aux exigences applicables à cette catégorie;
e) il n’est pas interdit de territoire;
f) s’il est tenu de se soumettre à une visite médicale en application du paragraphe 16(2) de la Loi, il satisfait aux exigences prévues aux paragraphes 30(2) et (3).

[16] CIC has also produced a policy document entitled ENF 2 – Evaluating Inadmissibility (ENF 2) which is intended to assist visa offices in assessing misrepresentation. While such guidelines or operational manuals do not have the force of law, they have been recognized by this Court as valuable guidelines to immigration officers in carrying out their duties (Canada (Minister of Public Safety and Emergency Preparedness) v Martinez-Brito, 2012 FC 438 at para 46; Baker v Canada (Minister of Citizenship and Immigration), [1991] 2 SCR 817 [Baker]; Agraira v Canada (Minister of Public Safety and Emergency Preparedness), 2013 SCC 36 at para 85).

[17] ENF 2 states that the purpose of the misrepresentation provisions is to ensure that applicants provide complete, honest and truthful information in every manner when applying for entry into Canada (section 9.1) and that persons who misrepresent or withhold material facts, either directly or indirectly, relating to a relevant matter that induces or could induce an error in the administration of the Act are inadmissible to Canada pursuant to subsection 40(1)(a) of the IRPA. Misrepresentation and withholding are defined as direct and indirect misrepresentation (section 9.2). The document also describes the principles applicable to relevancy as well as materiality and provides examples of these (section 9.4). It also addresses errors in the administration of the IRPA (section 9.5).
Issues

[18] I would frame the issue in this matter as being whether it was reasonable for the Officer to conclude that there was a material misrepresentation.
Standard of Review

[18] The majority of the Supreme Court has held that “[a]n exhaustive analysis is not required in every case to determine the proper standard of review.” Courts must first ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of deference to be accorded to a decision-maker with regard to a particular category of question (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at paras 57 and 62 [Dunsmuir]; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12, [2009] 1 SCR 339 at para 53 [Khosa]).

[19] This Court has previously held that the standard of review to be applied when determining whether an immigration officer made a reviewable error in concluding that an applicant made a material misrepresentation pursuant to subsection 40(1)(a) of the IRPA is reasonableness. Misrepresentation is an issue of mixed fact and law and is therefore reviewable on the reasonableness standard (Oloumi v Canada (Minister of Citizenship and Immigration), 2012 FC 428 at para 12 [Oloumi]; Karami v Canada (Minister of Citizenship and Immigration), 2009 FC 788 at para 14).

[20] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility of the decision-making process and also with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law” (Dunsmuir, above, at para 47; Khosa, above at para 59).
Positions of the Parties
The Applicant

[21] The Applicant’s position is that there was no misrepresentation but, even if there was, it was not material.

[22] The Applicant submits that he brought the error to the attention of the immigration consultant who was assisting him and that he believed that the error would be corrected before the consultant submitted the application. He was not dishonest and did not knowingly misrepresent his immigration history. He reasonably and honestly believed at the time the application was made that he was not withholding material information. In this regard he relies on Medel v Canada, [1990] FCJ No 318 (CA)(QL) [Medel] and distinguishes Oloumi, above, and Haque v Canada (Minister of Citizenship and Immigration), 2011 FC 315 [Haque] on their facts. He also submits that he responded to the fairness letter in an effort to explain the error and provided copies of his study visas and his work permits.

[23] Further, the Applicant submits that only if information affects the process undertaken or the final decision will it be considered to be material (ENF 2; Ali v Canada (Minister of Citizenship and Immigration), 2008 FC 166 [Ali]). Here the answer to the question of whether he had previously been denied a visa was not material to the process because the application was complete and could be processed regardless of the answer provided. Nor did his answer put into doubt other important information about himself.
The Respondent

[24] The Respondent submits that the Applicant’s failure to disclose the previous temporary resident visa application constituted a material misrepresentation.

[25] The Respondent refers to the requirements of the IRPA, the IRPA Regulations as well as ENF 2 and concludes that the Officer properly applied these provisions which required the Applicant to provide complete and truthful information. The failure to disclose the previous temporary residency visa refusal was a relevant matter to weigh when considering the Applicant’s subsequent application and could have induced an error in the administration of the IRPA. Accordingly, the failure to disclose this matter renders the Applicant inadmissible by virtue of section 40 of the IRPA and the Decision is therefore, reasonable. The Respondent relies on Oloumi and Haque, both above, in support of its position.

[26] The Respondent submits that the Applicant was aware of the error in his application and, while he may have brought this to the attention of his immigration consultant, he himself signed and declared the application to contain truthful answers. Accordingly, this error was not beyond his control, he was alive to it and could and should have reviewed the application prior to signing it to ensure that the error had been rectified and that the application was accurate. Therefore, the Applicant cannot now claim that he honestly and reasonably believed in the veracity of the answers (Oloumi, above, Khorasgani v Canada (Minister of Citizenship and Immigration), 2012 FC 1177 at paras 14-18). The Respondent submits that the Applicant’s reliance on Medel, above is misplaced in the circumstances of this case.

[27] Further, in response to the fairness letter, the Applicant provided a statutory declaration stating that he had never engaged in any unauthorized full time employment while a holder of an OCWP and that he had never received a request from an immigration officer to surrender his OCWP. The Officer examined the file and determined that this contradicted the Applicant’s own application, the CIC record and other evidence. Accordingly, it was open for the Officer to conclude that the Applicant had continued to be dishonest. This indicated a pattern of providing untruthful information in breach of the Applicant’s statutory duty of candour and therefore justified the Officer’s decision.
Analysis

[28] In Oloumi, above, Justice Tremblay-Lamer describes general principles arising from this Court’s treatment of section 40 of the IRPA which are summarized below together with other such principles arising from the jurisprudence:
- Section 40 is to be given a broad interpretation in order to promote its underlying purpose (Khan v Canada (Minister of Citizenship and Immigration), 2008 FC 512 at para 25 [Khan]);
- Section 40 is broadly worded to encompasses misrepresentations even if made by another party, including an immigration consultant, without the knowledge of the applicant (Jiang v Canada (Minister of Citizenship and Immigration), 2011 FC 942 at para 35 [Jiang]; Wang v Canada (Minister of Citizenship and Immigration), 2005 FC 1059 at paras 55-56 [Wang]);
- The exception to this rule is narrow and applies only to truly extraordinary circumstances where an applicant honestly and reasonably believed that they were not misrepresenting a material fact and knowledge of the misrepresentation was beyond the applicant’s control (Medel, above);
- The objective of section 40 is to deter misrepresentation and maintain the integrity of the immigration process. To accomplish this, the onus is placed on the applicant to ensure the completeness and accuracy of their application (Jiang, above, at para 35;Wang, above, at paras 55-56);
- An applicant has a duty of candour to provide complete, honest and truthful information in every manner when applying for entry into Canada (Bodine v Canada (Minister of Citizenship and Immigration), 2008 FC 848 at para 41; Baro v Canada (Minister of Citizenship and Immigration), 2007 FC 1299 at para 15);
- As the applicant is responsible for the content of an application which they sign, the applicant’s belief that he or she was not misrepresenting a material fact is not reasonable where they fail to review their application and ensure the completeness and veracity of the document before signing it (Haque, above, at para 16; Cao v Canada (Minister of Citizenship and Immigration), 2010 FC 450 at para 31 [Cao]);
- In determining whether a misrepresentation is material, regard must be had for the wording of the provision and its underlying purpose (Oloumi, above, at para 22);
- A misrepresentation need not be decisive or determinative. It is material if it is important enough to affect the process (Oloumi, above, at para 25);
- An applicant may not take advantage of the fact that the misrepresentation is caught by the immigration authorities before the final assessment of the application. The materiality analysis is not limited to a particular point in time in the processing of the application. (Haque, above, at paras 12 and 17; Khan, above, at paras 25, 27 and 29; Shahin v Canada (Minister of Citizenship and Immigration), 2012 FC 423 at para 29 [Shahin]);

[29] Here, the Applicant submits that he had no knowledge of the misrepresentation which was caused by his immigration consultant’s failure to correct a clerical error. The Applicants submits that he instructed the consultant to change the answer of “no” to “yes” in response to the question “Have you ever been refused any kind of visa, admission or been ordered to leave Canada or another country?” However, that the consultant failed to do so before submitting the application.

[30] As noted above, subsection 40(1)(a) is broadly worded as to include misrepresentations even if made by another party without the knowledge of the applicant, the general rule being that a misrepresentation can occur without the applicant’s knowledge (Jiang, above, at para 35; Cao; above, at para 31; Haque, above, at para 15;Wang, above, at paras 55-56; Shahin, above, at para 26).

[31] While an exception to this principle arises where an applicant can show that he or she honestly and reasonably believed that they were not withholding material information (Medel, above), this exception is narrow. As the court stated in Oloumi, above:

[35] Despite being frequently cited, the “exception” referred to in this passage has received limited application. Its originating case, Medel, above, involved an unusual set of facts: the applicant was being sponsored by her husband, but unbeknownst to her the husband withdrew his sponsorship. Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. They implied it would be returned to her, corrected. The applicant had English-speaking relatives inspect the visa and, after they assured her that nothing was wrong with it, she used it to enter Canada. The Immigration Appeal Board found her to be a person described in section 27(1)(e) of the former Immigration Act, 1976, SC 1976-77, c 52 [now RSC 1985, c I-2)], i.e. that she had been “granted landing… by reason of any fraudulent or improper means”. This finding was set aside by the Federal Court of Appeal because the applicant had “reasonably believed” that she was not withholding information relevant to her admission.

[36] When considered within its factual context, therefore, the exception in Medel is relatively narrow. As Justice MacKay noted while distinguishing the case before him in Mohammed v Canada (Minister of Citizenship & Immigration), 1997 CanLII 5084 (FC), [1997] 3 FC 299:
41 The present circumstances may also be distinguished from those in Medel on the basis that the information which the applicant failed to disclose was not information regarding which he was truly subjectively unaware. The applicant in the present case was not unaware that he was married. Nor was it information, as in Medel, the knowledge of which was beyond his control. This was not information which had been concealed from him or about which he had been misled by Embassy officials. The applicant's alleged ignorance regarding the requirement to report such a material change in his marital status and his inability to communicate this information to an immigration officer upon arrival does not, in my opinion, constitute “subjective unawareness” of the material information as contemplated in Medel.
Furthermore, I emphasize that a determinative factor in the Medel case was that the applicant had reasonably believed that she was not withholding information from Canadian authorities. In contrast, in the case before this Court the applicants did not act reasonably—the principal applicant failed to review his application to ensure its accuracy.

[32] In Haque, above, the applicants therein similarly argued that the misrepresentations were not intentional and that it was their consultant who erred in filling out the application. Justice Mosley rejected this argument and stated the following:

[15] […] Nonetheless, he signed the application and so cannot be absolved of his personal duty to ensure the information he provided was true and complete. This was expressed succinctly by Justice Robert Mainville at para 31 of Cao, supra:
The Applicant signed her temporary residence application and consequently must be held personally accountable for the information provided in that application. It is as simple as that.

[33] The present case is also factually very similar to Diwalpitiye v Canada (Minister of Citizenship and Immigration), 2012 FC 885 [Diwalpitiye]. The applicant therein indicated on his application form that he had never applied for, or been refused, immigration status in Canada. When the officer raised this as a concern in a fairness letter, the applicant responded by explaining that he had previously applied for a temporary resident visa, which was refused, but a subsequent application was successful. While he admitted this error in completing the application form, he requested that his application be processed because the error was merely an oversight. Justice Rennie found that the applicant had not persuaded the Court that it was unreasonable for the officer to find this to be a material misrepresentation.

[34] In my view, the Applicant in this case clearly made a misrepresentation by failing to disclose the prior CIC Los Angeles refusal to issue a temporary residency visa in his October 2012 application. He was aware of the error in his application and was responsible for ensuring that, when submitted, his application was accurate and truthful. However, he failed to review the application before it was submitted. Further, the fact of the prior refusal and of the identified clerical error in his application and whether or not it had been corrected was information that was within his control. The Applicant therefore failed to demonstrate that he honestly and reasonably believed that he was not withholding potentially material information. This situation does not, therefore, fall within the narrow exception found in Medel, above. It was reasonable for the Officer to conclude that the Applicant had not answered all of the questions in his application truthfully as required by subsection 16(1) of the IRPA and had misrepresented that fact.

[35] This leaves only the question of whether the misrepresentation was material.

[36] Subsection 40(1)(a) of the IRPA states that a foreign national is inadmissible for misrepresentation for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of the IRPA. ENF 2 gives as an example of a situation constituting misrepresentation, one where an applicant fails to disclose that they recently applied for a visa to Canada.

[37] As noted above, in determining whether a misrepresentation is material, regard must be had for the wording of the provision and its underlying purpose. To be material, a misrepresentation need not be decisive or determinative. It will be material if it is important enough to affect the process. The wording of section 40 confirms that a misrepresentation does not actually have to induce an error, it is enough that it could do so (IRPA, subsection 40(1)(a); Oloumi, above, at paras 22 and 25; Haque, above, at para 11; Mai v Canada (Minister of Public Safety and Emergency Preparedness), 2011 FC 101 at para 18; Nazim v Canada (Minister of Citizenship and Immigration), 2009 FC 471)).

[38] In Haque, above, the applicant failed to disclose that he had formerly lived and studied in the United States and omitted or misrepresented details with respect to his place of residence, education and employment history. The deciding officer discovered the omission upon a review of CIC’s records. This Court held that the withheld information was material to the application as, without it, a visa could have been issued to the applicant without the required police and conduct certificates from the United States, thereby precluding a necessary investigation and inducing an error in the administration of the IRPA.

[39] In Oloumi, above, a fraudulent English test was submitted as part of an application for permanent residence in the Federal Skilled Worker class. This Court held that the misrepresented fact was material because federal skilled workers must demonstrate language proficiency to be accepted. The false document could have induced an error in the administration of the IRPA because it could have been relied upon by a decision-maker to conclude that the applica

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 24458:4 · paragraphs 58-58

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `715b22ab5184624096db6e9e39258fae57be8954953ffdd3f2ac225e93a56460`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24458:4:subtheme:1 · paragraphs 58-58

- Raw key terms: `alberta, anna, appearances, applicant, associates, attorney, canada, dated`
- Display key terms: `alberta, anna, associates, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, anna, associates, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 58-58. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT BY: STRICKLAND J.
DATED: September 23, 2013
APPEARANCES:
Ranbir S. Thind
FOR THE APPLICANT
Anna Kuranicheva
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Ranbir Thind & Associates
Edmonton, Alberta
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Edmonton, Alberta
FOR THE RESPONDENT
