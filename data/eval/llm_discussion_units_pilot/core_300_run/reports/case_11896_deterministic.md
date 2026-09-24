# Discussion Units: case 11896

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **3**
- Paragraph source hashes: **26**
- Sub-themes: **8**

## 11896:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3670f0d6b205703f21cf8051000f9f7f5e2c9a291f0650bf439ed72ebdd21273`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11896:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, application, court, decision, officer, protection, reasons, refugee`
- Display key terms: `officer, protection, refugee`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: officer, protection, refugee Rule/authority context: Introduction [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by an inland enforcement officer [the Off Operative outcome context: [3] For the reasons that follow, the application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4597053` offsets `531-542`; context: Introduction [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by an inland enforcement officer [the Officer] refusing the applicant’s Pre-Removal Risk Assessment application [PRRA].
- Evidence: `disposition` cue `dismissed` at chunk `4597055` offsets `52-61`; context: [3] For the reasons that follow, the application is dismissed.

#### Section text

El Bouni v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-06-02
Neutral citation
2015 FC 700
File numbers
IMM-7627-14
Notes
A correction was made on November 30, 2015
Decision Content
Date: 20150602
Docket: IMM-7627-14
Citation: 2015 FC 700
Ottawa, Ontario, June 2, 2015
PRESENT: The Honourable Mr. Justice Annis
BETWEEN:
HAIDAR EL BOUNI
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by an inland enforcement officer [the Officer] refusing the applicant’s Pre-Removal Risk Assessment application [PRRA].

[2] The applicant is seeking an order quashing the Officer’s decision and referring the matter back for re-determination. The applicant also asks the Court for two declaratory orders: (1) that the officer must make a new evaluation of the danger facing the applicants rather than following the Refugee Protection Division’s credibility findings, and (2) that the situation in Libya and Article 3 of the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, 1465 UNTS 85 [the Convention Against Torture] must be addressed for this type of decision to be valid.

[3] For the reasons that follow, the application is dismissed.


## 11896:2 · paragraphs 3-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e9f675cb39bc74cf280fd63b459f90a97159ee25c05409c8ab89a38850e220e8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11896:2:subtheme:1 · paragraphs 3-11

- Raw key terms: `applicant, ellafi, application, decision, divorce, family, found, protection`
- Display key terms: `ellafi, divorce, family, protection`
- Argument roles: `disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, party_position, reasoning_application Display terms: ellafi, divorce, family, protection Position/evidence statements: He claims that these people have close ties to Muammar Khadafi and the Libyan government. | He claims that the doctor told them that the mental illness in Ms. Application context: [9] The applicant applied for permanent residence in the spouse or common-law partner category on May 22, 2013. | Ellafi and this was not relevant because he was not arguing that he was at risk by reason of this divorce. Operative outcome context: [8] On March 5, 2012, the Refugee Protection Division [RPD] denied his refugee claim on the basis that his story lacked credibility. | This application was denied and this Court dismissed his application for leave and judicial review of this decision because he had failed to perfect the application. Evidence spans paragraphs 3-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4597055` offsets `202-208`; context: He claims that these people have close ties to Muammar Khadafi and the Libyan government.
- Evidence: `party_position` cue `claims` at chunk `4597056` offsets `375-381`; context: He claims that the doctor told them that the mental illness in Ms.
- Evidence: `disposition` cue `denied` at chunk `4597059` offsets `60-66`; context: [8] On March 5, 2012, the Refugee Protection Division [RPD] denied his refugee claim on the basis that his story lacked credibility.
- Evidence: `reasoning_application` cue `applied` at chunk `4597060` offsets `18-25`; context: [9] The applicant applied for permanent residence in the spouse or common-law partner category on May 22, 2013.
- Evidence: `disposition` cue `denied` at chunk `4597060` offsets `133-139`; context: This application was denied and this Court dismissed his application for leave and judicial review of this decision because he had failed to perfect the application.
- Evidence: `party_position` cue `submitted` at chunk `4597062` offsets `59-68`; context: [11] The applicant was offered a PRRA on July 29, 2013 and submitted his application on August 28, 2013.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4597062` offsets `256-265`; context: He included the following documentation in support of his claim that he would face a high risk of threats, death, and torture if he returned to Libya:
Affidavit of Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4597063` offsets `153-160`; context: Ellafi and this was not relevant because he was not arguing that he was at risk by reason of this divorce.

#### 11896:2:subtheme:2 · paragraphs 12-13

- Raw key terms: `applicant, assessment, concluded, country, evidence, including, issues, judicial`
- Display key terms: `assessment, concluded, country, including, issues, judicial`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: assessment, concluded, country, including, issues, judicial Position/evidence statements: Consideration of an application for protection shall be as follows: (a) an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably  Rule/authority context: Standard of Review [18] With the withdrawal of issues by the applicant, the remaining two entail the Officer’s assessment of the evidence in a PRRA. Application context: (1) A person in Canada, other than a person referred to in subsection 115(1), may, in accordance with the regulations, apply to the Minister for protection if they are subject to a removal order that is in force or are n Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4597064` offsets `53-59`; context: [14] The Officer acknowledged that there are ongoing issues in Libya including violent armed clashes, a deficient judicial system and “serious weakness in the areas of women’s rights and freedom of expression.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597064` offsets `371-379`; context: ” However, the Officer concluded that the problems raised in the country condition documentation were generalized and that the applicant had failed to adduce any evidence to cause the Officer to contradict the RPD’s assessment of risk.
- Evidence: `counterargument_limitation` cue `However` at chunk `4597064` offsets `211-218`; context: ” However, the Officer concluded that the problems raised in the country condition documentation were generalized and that the applicant had failed to adduce any evidence to cause the Officer to contradict the RPD’s assessment of risk.
- Evidence: `issue` cue `Issues` at chunk `4597065` offsets `1841-1847`; context: Issues [17] The applicant raised the following issues in his application for leave and for judicial review, but indicated at the hearing that he is only proceeding on the first two issues:
1.
- Evidence: `party_position` cue `claim` at chunk `4597065` offsets `1179-1184`; context: Consideration of an application for protection shall be as follows:
(a) an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably available, or that the applicant could not reasonably have been expected in the circumstances to have presented, at the time of the rejection;
…
113.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597065` offsets `1246-1254`; context: Consideration of an application for protection shall be as follows:
(a) an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably available, or that the applicant could not reasonably have been expected in the circumstances to have presented, at the time of the rejection;
…
113.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4597065` offsets `2628-2646`; context: Standard of Review [18] With the withdrawal of issues by the applicant, the remaining two entail the Officer’s assessment of the evidence in a PRRA.
- Evidence: `reasoning_application` cue `apply` at chunk `4597065` offsets `658-663`; context: (1) A person in Canada, other than a person referred to in subsection 115(1), may, in accordance with the regulations, apply to the Minister for protection if they are subject to a removal order that is in force or are named in a certificate described in subsection 77(1).

#### 11896:2:subtheme:3 · paragraphs 14-17

- Raw key terms: `applicant, evidence, prra, officer, allegations, application, canada, court`
- Display key terms: `prra, officer, allegations`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: prra, officer, allegations Position/evidence statements: [22] The applicant is challenging the Officer’s conclusion that the evidence he submitted was not new evidence within the meaning of section 113 of the Act. | [23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicia Application context: Moreover, I find that the quality of much of this evidence is wanting. Operative outcome context: [23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicia Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4597066` offsets `311-317`; context: While a PRRA application may require consideration of the same factual and legal issues as in the refugee claim, the PRRA process is not intended to be an appeal or opportunity for the applicant to have the same allegations and facts reassessed (Raza at para 12, Figurado v Canada (Solicitor General), 2005 FC 347 at para 52).
- Evidence: `evidence_fact` cue `evidence` at chunk `4597066` offsets `69-77`; context: [20] The Court further noted that a PRRA officer may properly reject evidence if it cannot prove that the relevant facts as of the date of the PRRA application are materially different from the facts of the RPD (Raza at para 17).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4597066` offsets `84-90`; context: [20] The Court further noted that a PRRA officer may properly reject evidence if it cannot prove that the relevant facts as of the date of the PRRA application are materially different from the facts of the RPD (Raza at para 17).
- Evidence: `evidence_fact` cue `evidence` at chunk `4597067` offsets `128-136`; context: [21] The RPD’s finding that the applicant is not credible would preclude a positive finding in a PRRA unless he shows, with new evidence, that a “material change in circumstances has occurred since the prior determination by the RPD” (Barrios Silva v Canada (Citizenship and Immigration), 2012 FC 1294 at para 20).
- Evidence: `party_position` cue `submitted` at chunk `4597068` offsets `80-89`; context: [22] The applicant is challenging the Officer’s conclusion that the evidence he submitted was not new evidence within the meaning of section 113 of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597068` offsets `68-76`; context: [22] The applicant is challenging the Officer’s conclusion that the evidence he submitted was not new evidence within the meaning of section 113 of the Act.
- Evidence: `party_position` cue `submits` at chunk `4597069` offsets `25-32`; context: [23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicial review of the RPD decision.
- Evidence: `evidence_fact` cue `determined that` at chunk `4597069` offsets `106-121`; context: [23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicial review of the RPD decision.
- Evidence: `reasoning_application` cue `I find` at chunk `4597069` offsets `260-266`; context: Moreover, I find that the quality of much of this evidence is wanting.
- Evidence: `disposition` cue `denied` at chunk `4597069` offsets `196-202`; context: [23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicial review of the RPD decision.

#### 11896:2:subtheme:4 · paragraphs 18-20

- Raw key terms: `evidence, based, canada, citizenship, credible, decision, family, highly`
- Display key terms: `based, credible, family, highly`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: based, credible, family, highly Position/evidence statements: [24] The applicant also claims that the Officer rejected this evidence on the basis that it came from family members and other interested parties, which he submits is an error of law (Gonzalez Perea v Canada (Citizenship Application context: If the evidence is highly probative of the case and is credible evidence, then the officer should generally exercise his or her discretion in favour of receiving the evidence because of the importance of the issues at st | [25] However, I find that confirmatory evidence of family members and friends, which is not subject to cross-examination, is not highly probative or credible evidence. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4597070` offsets `975-981`; context: If the evidence is highly probative of the case and is credible evidence, then the officer should generally exercise his or her discretion in favour of receiving the evidence because of the importance of the issues at stake…
- Evidence: `party_position` cue `claims` at chunk `4597070` offsets `24-30`; context: [24] The applicant also claims that the Officer rejected this evidence on the basis that it came from family members and other interested parties, which he submits is an error of law (Gonzalez Perea v Canada (Citizenship and Immigration), 2008 FC 432).
- Evidence: `evidence_fact` cue `evidence` at chunk `4597070` offsets `62-70`; context: [24] The applicant also claims that the Officer rejected this evidence on the basis that it came from family members and other interested parties, which he submits is an error of law (Gonzalez Perea v Canada (Citizenship and Immigration), 2008 FC 432).
- Evidence: `reasoning_application` cue `because` at chunk `4597070` offsets `942-949`; context: If the evidence is highly probative of the case and is credible evidence, then the officer should generally exercise his or her discretion in favour of receiving the evidence because of the importance of the issues at stake…
- Evidence: `counterargument_limitation` cue `but` at chunk `4597070` offsets `319-322`; context: I disagree that the Officer based his decision on this reasoning, but even had this been the case, it would have been justified.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597071` offsets `39-47`; context: [25] However, I find that confirmatory evidence of family members and friends, which is not subject to cross-examination, is not highly probative or credible evidence.
- Evidence: `reasoning_application` cue `I find` at chunk `4597071` offsets `14-20`; context: [25] However, I find that confirmatory evidence of family members and friends, which is not subject to cross-examination, is not highly probative or credible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597072` offsets `57-65`; context: [26] In any event, the respondent notes that there is no evidence indicating that the Officer based this decision on who the letters and affidavits were from – the Officer examined each piece of evidence and concluded that they all referred to incidents that occurred prior to the RPD hearing.

#### 11896:2:subtheme:5 · paragraphs 21-22

- Raw key terms: `applicant, evidence, officer, risk, acceptable, acknowledged, advised, agree`
- Display key terms: `officer, risk, acceptable, acknowledged, advised, agree`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: officer, risk, acceptable, acknowledged, advised, agree Application context: [28] The applicant’s evidence in this application is that he did not obtain these documents at the time of the RPD hearing because he was poorly advised by his former counsel. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4597073` offsets `33-41`; context: [27] It is acknowledged that the question of weight to be given to evidence in risk assessments is within the purview of the Officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597073` offsets `67-75`; context: [27] It is acknowledged that the question of weight to be given to evidence in risk assessments is within the purview of the Officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4597074` offsets `21-29`; context: [28] The applicant’s evidence in this application is that he did not obtain these documents at the time of the RPD hearing because he was poorly advised by his former counsel.
- Evidence: `reasoning_application` cue `because` at chunk `4597074` offsets `123-130`; context: [28] The applicant’s evidence in this application is that he did not obtain these documents at the time of the RPD hearing because he was poorly advised by his former counsel.

#### 11896:2:subtheme:6 · paragraphs 23-24

- Raw key terms: `citizenship, immigration, accordingly, annis, appeal, applicant, application, arising`
- Display key terms: `accordingly, annis, arising`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: accordingly, annis, arising Application context: [30] I find that the country condition documentation did not raise any new risk or new information that had come up since the RPD decision (Selliah v Canada (Citizenship and Immigration), 2004 FC 872 at para 38, 256 FTR  Operative outcome context: Conclusion [31] The application is dismissed. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4597075` offsets `634-640`; context: Accordingly, I find no reviewable error in the Officer’s treatment of state protection issues.
- Evidence: `reasoning_application` cue `I find` at chunk `4597075` offsets `5-11`; context: [30] I find that the country condition documentation did not raise any new risk or new information that had come up since the RPD decision (Selliah v Canada (Citizenship and Immigration), 2004 FC 872 at para 38, 256 FTR 53).
- Evidence: `disposition` cue `dismissed` at chunk `4597075` offsets `683-692`; context: Conclusion [31] The application is dismissed.

#### Section text

II. Background [4] The applicant, a Libyan citizen, sought refugee protection on the basis of his alleged fear of his in-laws in Libya. He claims that these people have close ties to Muammar Khadafi and the Libyan government.

[5] The applicant married his former wife, Ms, Imam Ellafi, in December 2007 after only meeting her and her family on one prior occasion. He alleges that he later found out that Ms. Ellafi’s maternal grandfather and brother were suffering from a mental illness. Worried that this would affect their future children, he and his wife consulted a doctor in May or June 2008. He claims that the doctor told them that the mental illness in Ms. Ellafi’s family is hereditary and there was a “great risk” that their children would have it.

[6] The applicant alleges that, based on this information from the doctor, he refused to have a child with his wife and began using contraception. She was upset by this and her family began indirectly threatening him in July 2008. The situation worsened when a family meeting was held in her family’s village on November 13, 2008, where the applicant alleges that his father-in-law pointed a handgun at him and threatened to kill him if he continued to refuse to have a child by December 1, 2009 or if he divorced her. He returned to their apartment in Tripoli and allegedly received several more threats in-person and over the phone from Ms. Ellafi’s family. He alleges that her family is closely connected to the Libyan army and security forces. He filed a police complaint and allegedly found a dismembered dog outside his apartment door the next day. After this incident, the applicant left the apartment. He alleges that his neighbours told him that Ms. Ellafi’s uncle and several armed men were looking for him and that people in vehicles were watching for him at the apartment. He sought refuge with a friend outside Tripoli.

[7] The applicant decided to seek refugee protection in Canada since his mother lives in Montreal. He obtained a United States visa and fled to Tunisia in January 2010. He then travelled to the United States before crossing the border into Canada on January 12, 2010. A conditional departure order was issued against him at that time.

[8] On March 5, 2012, the Refugee Protection Division [RPD] denied his refugee claim on the basis that his story lacked credibility. His application for leave and for judicial review of the RPD decision was refused on August 10, 2012.

[9] The applicant applied for permanent residence in the spouse or common-law partner category on May 22, 2013. This application was denied and this Court dismissed his application for leave and judicial review of this decision because he had failed to perfect the application.

[10] Meanwhile, he sought and obtained a divorce from Ms. Ellafi in Canada.

[11] The applicant was offered a PRRA on July 29, 2013 and submitted his application on August 28, 2013. He included the following documentation in support of his claim that he would face a high risk of threats, death, and torture if he returned to Libya:
Affidavit of Mr. Tarek Taggazi (applicant’s friend), dated August 23, 2013; Medical report detailing the risk of mental illness in Ms. Ellafi’s family, dated July 16, 2008; Certificate of divorce from Ms. Ellafi, dated August 14, 2013; Affidavit of Ms. Gertila Zehra Mohamed (applicant’s mother), dated August 15, 2013; Letter from Mr. Haidar Abderaheem Ali El Bouni (applicant’s father), dated August 14, 2013; Letter from the regional council attesting to the incidents of November 2009, dated August 21, 2013; Letter from the mayor’s office attesting that the applicant received threats in July 2010; Letter from Mr. Jamal El Haraty (applicant’s neighbour), dated July 21, 2013; and Letter from Mr. Farag Mohamed Frag and Mr. Husni Abdulla Mohamed Ben Aun (applicant’s neighbours), dated August 18, 2013.
III. Impugned Decision [12] The Officer refused the PRRA on May 8, 2014, concluding that the evidence submitted did not meet the criteria to be considered new evidence. The Officer found that the affidavits and letters from the applicant’s friends, parents and neighbours all referred to past events that arose before the RPD refused the claim, even though they were written after that point in time. The medical report and the mayor’s letter both pre-dated the RPD decision, so the Officer found that it was reasonable to assume that they could have been presented at the time of the RPD hearing and the applicant had provided no explanation for why this would not have been possible.

[13] In the Officer’s estimation, the only new fact raised in the PRRA application was the applicant’s divorce from Ms. Ellafi and this was not relevant because he was not arguing that he was at risk by reason of this divorce.

[14] The Officer acknowledged that there are ongoing issues in Libya including violent armed clashes, a deficient judicial system and “serious weakness in the areas of women’s rights and freedom of expression.” However, the Officer concluded that the problems raised in the country condition documentation were generalized and that the applicant had failed to adduce any evidence to cause the Officer to contradict the RPD’s assessment of risk.

[15] Overall, the Officer concluded that the applicant had not demonstrated that he would face more than a mere possibility of persecution or that there are serious reasons to believe he would be subjected to torture or a risk to his life or of cruel and unusual treatment or punishment if returned to Libya.
IV. Statutory Provisions [16] The following provisions of the Act are applicable in these proceedings:
Immigration and Refugee Protection Act, SC 2001, c 27
Loi sur l’immigration et la protection des réfugiés, LC 2001, ch 27
112. (1) A person in Canada, other than a person referred to in subsection 115(1), may, in accordance with the regulations, apply to the Minister for protection if they are subject to a removal order that is in force or are named in a certificate described in subsection 77(1).
…
112. (1) La personne se trouvant au Canada et qui n’est pas visée au paragraphe 115(1) peut, conformément aux règlements, demander la protection au ministre si elle est visée par une mesure de renvoi ayant pris effet ou nommée au certificat visé au paragraphe 77(1).
…
113. Consideration of an application for protection shall be as follows:
(a) an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably available, or that the applicant could not reasonably have been expected in the circumstances to have presented, at the time of the rejection;
…
113. Il est disposé de la demande comme il suit :
a) le demandeur d’asile débouté ne peut présenter que des éléments de preuve survenus depuis le rejet ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’il n’était pas raisonnable, dans les circonstances, de s’attendre à ce qu’il les ait présentés au moment du rejet;
…
[Emphasis added.]
[Soulignement ajouté.]
V. Issues [17] The applicant raised the following issues in his application for leave and for judicial review, but indicated at the hearing that he is only proceeding on the first two issues:
1. Did the Officer err in concluding that the documents submitted by the applicant did not constitute new evidence within the meaning of section 113(a) of the Act?
2. Did the Officer err in concluding that the applicant did not demonstrate that he would be personally at risk if he were to return to Libya?
3. Does the PRRA process raise issues of institutional bias or lack of independence?
4. Is paragraph 113(a) of the IRPA consistent with the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 [Charter]?
VI. Standard of Review [18] With the withdrawal of issues by the applicant, the remaining two entail the Officer’s assessment of the evidence in a PRRA. This is fundamentally a fact-finding exercise. His or her determination of what constitutes new evidence is a question of mixed fact and law reviewed on a basis of reasonableness (Wang v Canada (Citizenship and Immigration), 2010 FC 799 at para 11, 191 ACWS (3d) 574, Negm v Canada (Citizenship and Immigration), 2015 FC 272, 250 ACWS (3d) 317).
VII. Analysis A. Did the Officer err in concluding that the documents submitted by the applicant did not constitute new evidence within the meaning of section 113(a)? [19] In Raza v Canada (Citizenship and Immigration), 2007 FCA 385, 289 DLR (4th) 675, the Federal Court of Appeal held that a PRRA officer must respect the RPD’s negative refugee determination “unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD.” The Court in Raza summarized the following questions to be asked about the evidence in a PRRA application:
1. Credibility: Is the evidence credible, considering its source and the circumstances in which it came into existence? If not, the evidence need not be considered.
2. Relevance: Is the evidence relevant to the PRRA application, in the sense that it is capable of proving or disproving a fact that is relevant to the claim for protection? If not, the evidence need not be considered.
3. Newness: Is the evidence new in the sense that it is capable of:
(a) proving the current state of affairs in the country of removal or an event that occurred or a circumstance that arose after the hearing in the RPD, or
(b) proving a fact that was unknown to the refugee claimant at the time of the RPD hearing, or
(c) contradicting a finding of fact by the RPD (including a credibility finding)?
If not, the evidence need not be considered.
4. Materiality: Is the evidence material, in the sense that the refugee claim probably would have succeeded if the evidence had been made available to the RPD? If not, the evidence need not be considered.
5. Express statutory conditions:
(a) If the evidence is capable of proving only an event that occurred or circumstances that arose prior to the RPD hearing, then has the applicant established either that the evidence was not reasonably available to him or her for presentation at the RPD hearing, or that he or she could not reasonably have been expected in the circumstances to have presented the evidence at the RPD hearing? If not, the evidence need not be considered.
(b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

[20] The Court further noted that a PRRA officer may properly reject evidence if it cannot prove that the relevant facts as of the date of the PRRA application are materially different from the facts of the RPD (Raza at para 17). While a PRRA application may require consideration of the same factual and legal issues as in the refugee claim, the PRRA process is not intended to be an appeal or opportunity for the applicant to have the same allegations and facts reassessed (Raza at para 12, Figurado v Canada (Solicitor General), 2005 FC 347 at para 52). It is common ground that the applicant must put his or her best foot forward before the RPD.

[21] The RPD’s finding that the applicant is not credible would preclude a positive finding in a PRRA unless he shows, with new evidence, that a “material change in circumstances has occurred since the prior determination by the RPD” (Barrios Silva v Canada (Citizenship and Immigration), 2012 FC 1294 at para 20).

[22] The applicant is challenging the Officer’s conclusion that the evidence he submitted was not new evidence within the meaning of section 113 of the Act. The applicant claims that the Officer erred by ignoring the documents referring to an ongoing search for him and threats made since the RPD decision. I disagree. Most of the evidence introduced before the PRRA Officer contravenes the express statutory limitations since it was reasonably available to the applicant for his presentation at the RPD.

[23] The respondent also submits that the PRRA officer could not ignore the fact that the RPD had already determined that the applicant’s allegations of risk were not credible and that this Court denied leave for judicial review of the RPD decision. Moreover, I find that the quality of much of this evidence is wanting. The father’s letter, mother’s affidavit, and Mr. El Haraty’s letter contain vague and overly broad allegations about an ongoing search and threats after the applicant’s departure, without any details about when these occurred. They also reiterate the allegations that were before the RPD and do not rebut the RPD’s credibility findings in the sense of establishing that the relevant facts at the date of the PRRA application were materially different from the facts as found by the RPD.

[24] The applicant also claims that the Officer rejected this evidence on the basis that it came from family members and other interested parties, which he submits is an error of law (Gonzalez Perea v Canada (Citizenship and Immigration), 2008 FC 432). I disagree that the Officer based his decision on this reasoning, but even had this been the case, it would have been justified. The applicant referred to the case of Elezi v Canada (Citizenship and Immigration), 2007 FC 240, [2008] 1 FCR 365 [Elezi]. At paragraph 45 of Elezi, Justice de Montigny cites with approval a passage from section 4.999 of, Immigration Law and Practice (2nd ed., loose-leaf) by Lorne Waldman that:
Finally, I would argue that the nature of the evidence itself should also be considered. If the evidence is highly probative of the case and is credible evidence, then the officer should generally exercise his or her discretion in favour of receiving the evidence because of the importance of the issues at stake…

[25] However, I find that confirmatory evidence of family members and friends, which is not subject to cross-examination, is not highly probative or credible evidence. Highly probative evidence is intrinsically well-presented evidence from independent sources confirming a material fact in the matter.

[26] In any event, the respondent notes that there is no evidence indicating that the Officer based this decision on who the letters and affidavits were from – the Officer examined each piece of evidence and concluded that they all referred to incidents that occurred prior to the RPD hearing. The respondent refers the Court to Kaybaki v Canada (Citizenship and Immigration), 2004 FC 32, 128 ACWS (3d) 784, where Justice Kelen concluded that the officer did not err in rejecting similar evidence, which I agree supports its position.

[27] It is acknowledged that the question of weight to be given to evidence in risk assessments is within the purview of the Officer. The Officer is charged with determining if the applicant is subject to risks that have arisen since the RPD decision, and in this case, the Officer’s conclusion that the only new risk evidence related to the divorce was correct (Doumbouya v Canada (Citizenship and Immigration), 2007 FC 1187 at paras 36-38,325 FTR 14).

[28] The applicant’s evidence in this application is that he did not obtain these documents at the time of the RPD hearing because he was poorly advised by his former counsel. I agree with the respondent’s submission that the Court should not consider this because the applicant has not followed the requisite steps before pleading the incompetence of his former counsel. The onus remained on the applicant to provide the relevant acceptable documentation to establish his claim.
B. Did the Officer err in concluding that the applicant did not demonstrate that he would be personally at risk if he were to return to Libya? [29] The applicant submits that the Officer erred in assessing the documentary evidence concerning the current situation in Libya and his risk upon return. It is his position that all of the documents referred to by the Officer show that there is an appalling human rights situation in Libya with a complete breakdown of state authority.

[30] I find that the country condition documentation did not raise any new risk or new information that had come up since the RPD decision (Selliah v Canada (Citizenship and Immigration), 2004 FC 872 at para 38, 256 FTR 53). There is also the problem arising from the applicant’s failure to demonstrate a connection between the generalized country conditions and his personal situation, so it was reasonable for the Officer to reject the application (Jarada v Canada (Citizenship and Immigration), 2005 FC 409 at para 28, [2005] FCJ No 506 (QL)). Accordingly, I find no reviewable error in the Officer’s treatment of state protection issues.
VIII. Conclusion [31] The application is dismissed. There were no questions suggested for certification and none are certified.
JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed without any questions being certified for appeal.
"Peter Annis"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-7627-14
STYLE OF CAUSE:
HAIDAR EL BOUNI v MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, Quebec
DATE OF HEARING:
May 20, 2015


## 11896:3 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4f089f85e3728552d9b3db7000388fecbfb6ad85ae3ade3e769dc93093984985`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11896:3:subtheme:1 · paragraphs 25-25

- Raw key terms: `annis, appearances, applicant, attorney, barrister, bouni, canada, citizenship`
- Display key terms: `annis, barrister, bouni`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: annis, barrister, bouni No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
ANNIS J.
DATED:
June 2, 2015
APPEARANCES:
Stewart Istvanffy
For The Applicant
HAIDAR EL BOUNI
Suzanne Trudel
For The Respondent
MINISTER OF CITIZENSHIP AND IMMIGRATION
SOLICITORS OF RECORD:
Stewart Istvanffy
Barrister and Solicitor
Montréal, Quebec
For The Applicant
HAIDAR EL BOUNI
William F. Pentney
Deputy Attorney General of Canada
Ottawa, Ontario
For The Respondent
MINISTER OF CITIZENSHIP AND IMMIGRATION
