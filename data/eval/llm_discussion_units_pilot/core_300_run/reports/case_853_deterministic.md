# Discussion Units: case 853

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **29**
- Continuity pairs: **28**
- Discussion Units: **2**
- Paragraph source hashes: **29**
- Sub-themes: **10**

## 853:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `57aeb680d82289477db820226883ff995a0a6a4578e32f8e6bd8d9438e042630`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 853:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, board, immigration, canada, identity, rasheed, sohail, alleges`
- Display key terms: `identity, rasheed, sohail, alleges`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: identity, rasheed, sohail, alleges Position/evidence statements: The applicant further submitted a four page photocopy of a Pakistani passport showing a picture of him under the name Sohail Rasheed. Rule/authority context: [1] The applicant seeks judicial review of the decision of the Immigration and Refugee Board, Refugee Protection Division (the Board), dated February 21, 2003, wherein it was decided that the applicant was not a "Convent | [3] The applicant entered Canada with a British passport under the name Mohammad Rafiq Sharif. Application context: Accordingly, the Board concluded that the applicant's story, including allegations of persecution, was not credible. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4115884` offsets `269-280`; context: [1] The applicant seeks judicial review of the decision of the Immigration and Refugee Board, Refugee Protection Division (the Board), dated February 21, 2003, wherein it was decided that the applicant was not a "Convention refugee" or a "person in need of protection" pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `governing_rule` cue `under` at chunk `4115886` offsets `57-62`; context: [3] The applicant entered Canada with a British passport under the name Mohammad Rafiq Sharif.
- Evidence: `party_position` cue `submitted` at chunk `4115887` offsets `171-180`; context: The applicant further submitted a four page photocopy of a Pakistani passport showing a picture of him under the name Sohail Rasheed.
- Evidence: `governing_rule` cue `under` at chunk `4115887` offsets `118-123`; context: [4] The applicant provided the Board with identification papers, including a birth certificate and school certificate under the name Sohail Rasheed.
- Evidence: `governing_rule` cue `under` at chunk `4115888` offsets `561-566`; context: Reference was also made to an official warrant of arrest issued under the seal of the Court of Najid Nughal, which was produced before the Board.
- Evidence: `evidence_fact` cue `found that` at chunk `4115889` offsets `55-65`; context: [6] The applicant's claim did not succeed as the Board found that he had not met his burden of establishing his identity.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4115889` offsets `122-133`; context: Accordingly, the Board concluded that the applicant's story, including allegations of persecution, was not credible.

#### 853:1:subtheme:2 · paragraphs 7-8

- Raw key terms: `board, canada, establishing, identity, question, acceptable, accordingly, adopted`
- Display key terms: `establishing, identity, question, acceptable, accordingly, adopted`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: establishing, identity, question, acceptable, accordingly, adopted Rule/authority context: [8] The standard of review in credibility cases of the Board is patent unreasonableness (R. Application context: Accordingly, the respondent suggests that it is logical to conclude that the question of whether a claimant possesses acceptable documentation establishing his or her identity is to be reviewed by this Court only if the  Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115890` offsets `368-376`; context: [7] The reasons given by the Board for dismissing the documentary evidence establishing the applicant's identity are as follows:
1) There is no reasonable explanation for the applicant misleading the authorities upon his arrival in Canada;
2) The applicant only obtained a duplicate of the NIC approximately two months before his refugee hearing, leading the Board to question how the card was obtained, since the documentary evidence shows NICs are delivered only in person to male applicants;
3) With respect to the birth certificate and school certificate, the documentary evidence shows that false or forged documents are easily obtained upon payment of money; and
4) The photocopy of four pages of a Pakistani passport showing the applicant's picture and the name of Sohail Rasheed should not be given any probative value, since it is not an original and it is incomplete.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115890` offsets `66-74`; context: [7] The reasons given by the Board for dismissing the documentary evidence establishing the applicant's identity are as follows:
1) There is no reasonable explanation for the applicant misleading the authorities upon his arrival in Canada;
2) The applicant only obtained a duplicate of the NIC approximately two months before his refugee hearing, leading the Board to question how the card was obtained, since the documentary evidence shows NICs are delivered only in person to male applicants;
3) With respect to the birth certificate and school certificate, the documentary evidence shows that false or forged documents are easily obtained upon payment of money; and
4) The photocopy of four pages of a Pakistani passport showing the applicant's picture and the name of Sohail Rasheed should not be given any probative value, since it is not an original and it is incomplete.
- Evidence: `issue` cue `question` at chunk `4115891` offsets `414-422`; context: Accordingly, the respondent suggests that it is logical to conclude that the question of whether a claimant possesses acceptable documentation establishing his or her identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding.
- Evidence: `governing_rule` cue `standard of review` at chunk `4115891` offsets `8-26`; context: [8] The standard of review in credibility cases of the Board is patent unreasonableness (R.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4115891` offsets `337-348`; context: Accordingly, the respondent suggests that it is logical to conclude that the question of whether a claimant possesses acceptable documentation establishing his or her identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding.

#### 853:1:subtheme:3 · paragraphs 9-11

- Raw key terms: `applicant, identity, reasons, respect, standard, submits, absence, accept`
- Display key terms: `identity, respect, standard, submits, absence, accept`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: identity, respect, standard, submits, absence, accept Position/evidence statements: [9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible | [10] The applicant submits that the failure of the Board to accept identification papers for improper reasons constitutes an error of law. Rule/authority context: [9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible | Hence, the standard of review with respect to such a decision is correctness. Application context: )), I conclude that the determination with respect to the applicant's identity should be reviewed on a standard of reasonableness simpliciter. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115892` offsets `48-56`; context: [9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible under Canadian law (in this case the matter was heard in the province of Quebec).
- Evidence: `party_position` cue `submits` at chunk `4115892` offsets `31-38`; context: [9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible under Canadian law (in this case the matter was heard in the province of Quebec).
- Evidence: `evidence_fact` cue `Evidence` at chunk `4115892` offsets `1304-1312`; context: b) Section 23 of the Canada Evidence Act, R.
- Evidence: `governing_rule` cue `under` at chunk `4115892` offsets `221-226`; context: [9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible under Canadian law (in this case the matter was heard in the province of Quebec).
- Evidence: `party_position` cue `submits` at chunk `4115893` offsets `19-26`; context: [10] The applicant submits that the failure of the Board to accept identification papers for improper reasons constitutes an error of law.
- Evidence: `governing_rule` cue `standard of review` at chunk `4115893` offsets `150-168`; context: Hence, the standard of review with respect to such a decision is correctness.
- Evidence: `reasoning_application` cue `conclude` at chunk `4115894` offsets `193-201`; context: )), I conclude that the determination with respect to the applicant's identity should be reviewed on a standard of reasonableness simpliciter.

#### 853:1:subtheme:4 · paragraphs 12-13

- Raw key terms: `board, documents, establishing, identity, acceptable, acceptance, assessment, available`
- Display key terms: `documents, establishing, identity, acceptable, acceptance, assessment, available`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: documents, establishing, identity, acceptable, acceptance, assessment, available Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115895` offsets `347-355`; context: That being said, in the present case, the acceptance or rejection by the Board of official foreign documents establishing identity raises a mixed question of fact and law.
- Evidence: `issue` cue `whether` at chunk `4115896` offsets `225-232`; context: If not available, the Board is nevertheless obliged to decide whether the claimant has provided a reasonable explanation for the lack of documentation, or has taken reasonable steps to obtain it.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4115896` offsets `194-206`; context: If not available, the Board is nevertheless obliged to decide whether the claimant has provided a reasonable explanation for the lack of documentation, or has taken reasonable steps to obtain it.

#### 853:1:subtheme:5 · paragraphs 14-17

- Raw key terms: `applicant, board, examined, given, identity, made, respect, taken`
- Display key terms: `examined, given, identity, made, respect, taken`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: examined, given, identity, made, respect, taken Application context: Overall, I find the Board's decision unreasonable. | Yes, she said that, but I wasn't sure because the agent had told me that act on my instruction, whatever I am saying you do accordingly. Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4115897` offsets `157-164`; context: The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.
- Evidence: `issue` cue `question` at chunk `4115898` offsets `68-76`; context: [15] Considering all relevant criteria, including the nature of the question, the expertise of the Board relative to that of this Court on the issue, the purpose of the Act, sections 96, 97 and 106 of the Act, I am of the view that the determination made by the Board with respect to the identity of the applicant should be examined on a reasonableness simpliciter standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115899` offsets `111-119`; context: [16] Having carefully examined the transcripts of the hearing held before the Board as well as the documentary evidence submitted by the applicant, I have concluded that the finding of the Board is not tenable.
- Evidence: `reasoning_application` cue `I find` at chunk `4115899` offsets `432-438`; context: Overall, I find the Board's decision unreasonable.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4115899` offsets `284-290`; context: Taken either as a whole or independently, the reasons given by the Board cannot stand up to "a somewhat probing examination" (Law Society of New Brunswick v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4115900` offsets `60-69`; context: [17] The applicant did in fact explain in the course of his testimony why he had lied to the immigration authorities upon his arrival.
- Evidence: `reasoning_application` cue `because` at chunk `4115900` offsets `1444-1451`; context: Yes, she said that, but I wasn't sure because the agent had told me that act on my instruction, whatever I am saying you do accordingly.

#### 853:1:subtheme:6 · paragraphs 18-19

- Raw key terms: `claimant, documents, whether, accept, accepted, accordance, agent, agent's`
- Display key terms: `documents, whether, accept, accepted, accordance, agent, agent's`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: documents, whether, accept, accepted, accordance, agent, agent's Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4115901` offsets `502-509`; context: Second, whether a person has told the truth about his or her travel documents has little direct bearing on whether the person is indeed a refugee (Attakora v.
- Evidence: `issue` cue `whether` at chunk `4115902` offsets `336-343`; context: In this regard, I am ready to accept that the basic rule in Canadian law is that foreign documents (whether they establish the identity or not of a claimant) purporting to be issued by a competent foreign public officer should be accepted as evidence of their content unless the Board has some valid reason to doubt of their authenticity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115902` offsets `478-486`; context: In this regard, I am ready to accept that the basic rule in Canadian law is that foreign documents (whether they establish the identity or not of a claimant) purporting to be issued by a competent foreign public officer should be accepted as evidence of their content unless the Board has some valid reason to doubt of their authenticity.

#### 853:1:subtheme:7 · paragraphs 20-21

- Raw key terms: `board, certificate, documents, evidence, foreign, particular, validity, acta`
- Display key terms: `certificate, documents, foreign, particular, validity, acta`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: certificate, documents, foreign, particular, validity, acta Rule/authority context: He provided the right answer at page 392, as follows: Although there is almost no jurisprudence to be found bearing directly on the point, it must be held that an act of state - a passport or a certificate of identity -  Application context: The maxim omnia praesumuntur rite et solemniter esse acta applies with particular force here, establishing a rebuttable presumption of validity. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115903` offsets `407-415`; context: In that Immigration Appeal Board decision, the Chairman asked the following question at page 391:
The question here is, who can question the validity of an act of state and who, having questioned it, has the burden of proof as to its validity, and what proof is required?
- Evidence: `evidence_fact` cue `evidence` at chunk `4115903` offsets `240-248`; context: ) Moreover, identity documents issued by a foreign government are presumed to be valid unless evidence is produced to prove otherwise: see Gur, Jorge P.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4115903` offsets `685-698`; context: He provided the right answer at page 392, as follows:
Although there is almost no jurisprudence to be found bearing directly on the point, it must be held that an act of state - a passport or a certificate of identity - is prima facie valid.
- Evidence: `reasoning_application` cue `applies` at chunk `4115903` offsets `1048-1055`; context: The maxim omnia praesumuntur rite et solemniter esse acta applies with particular force here, establishing a rebuttable presumption of validity.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4115903` offsets `657-665`; context: He provided the right answer at page 392, as follows:
Although there is almost no jurisprudence to be found bearing directly on the point, it must be held that an act of state - a passport or a certificate of identity - is prima facie valid.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115904` offsets `102-110`; context: [6] In this instance, the Board challenged the validity of the birth certificate without adducing any evidence in support of its contention and, clearly, the matter of foreign documents it is not an area where the Board can claim particular knowledge.

#### 853:1:subtheme:8 · paragraphs 22-25

- Raw key terms: `board, evidence, applicant, documentary, made, accordingly, apparently, authentic`
- Display key terms: `documentary, made, accordingly, apparently, authentic`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: documentary, made, accordingly, apparently, authentic Position/evidence statements: [24] In conclusion, I note that this is not a case where the Board has closely examined a claimant's testimony and has determined that in light of the numerous contradictions and inconsistencies in said testimony, no pro Application context: Indeed, the latter document was sent for verification and the expert report concludes that the document in question is probably authentic. | Accordingly, the Board has manifestly failed to consider that relevant part of the documentary evidence. Evidence spans paragraphs 22-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115905` offsets `281-289`; context: Indeed, the latter document was sent for verification and the expert report concludes that the document in question is probably authentic.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115905` offsets `358-366`; context: Accordingly, it should have been accepted as evidence of the applicant's identity.
- Evidence: `reasoning_application` cue `concludes` at chunk `4115905` offsets `250-259`; context: Indeed, the latter document was sent for verification and the expert report concludes that the document in question is probably authentic.
- Evidence: `issue` cue `Question` at chunk `4115906` offsets `809-817`; context: 192-195, Government of Pakistan, Ministry of Interior, Directorate General of Registration, Question number 16).
- Evidence: `evidence_fact` cue `evidence` at chunk `4115906` offsets `390-398`; context: Furthermore, the documentary evidence referred to by the Board in its decision does not establish conclusively that duplicate NICs are only delivered in person to male applicants.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4115906` offsets `830-841`; context: Accordingly, the Board has manifestly failed to consider that relevant part of the documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4115907` offsets `115-123`; context: The reasons of the Board for discarding the other documentary evidence submitted by the applicant do not reside on strong grounds.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4115907` offsets `39-45`; context: [23] As a whole, the impugned decision cannot stand.
- Evidence: `party_position` cue `submitted` at chunk `4115908` offsets `280-289`; context: [24] In conclusion, I note that this is not a case where the Board has closely examined a claimant's testimony and has determined that in light of the numerous contradictions and inconsistencies in said testimony, no probative value should be afforded to the documentary evidence submitted by the claimant (Ramalingam v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4115908` offsets `101-110`; context: [24] In conclusion, I note that this is not a case where the Board has closely examined a claimant's testimony and has determined that in light of the numerous contradictions and inconsistencies in said testimony, no probative value should be afforded to the documentary evidence submitted by the claimant (Ramalingam v.

#### 853:1:subtheme:9 · paragraphs 26-27

- Raw key terms: `immigration, allowed, application, april, back, board, cause, certified`
- Display key terms: `allowed, april, back, certified`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: allowed, april, back, certified Operative outcome context: Consequently, the present application should be allowed and the matter sent back for redetermination by a differently constituted panel. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4115909` offsets `193-201`; context: No question of general importance has been raised by counsel and none will be certified.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4115909` offsets `627-633`; context: "Luc Martineau"
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-1956-03
- Evidence: `disposition` cue `allowed` at chunk `4115909` offsets `101-108`; context: Consequently, the present application should be allowed and the matter sent back for redetermination by a differently constituted panel.

#### Section text

Rasheed v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-04-21
Neutral citation
2004 FC 587
File numbers
IMM-1956-03
Decision Content
Date: 20040421
Docket: IMM-1956-03
Citation: 2004 FC 587
OTTAWA, ONTARIO, THIS 21st DAY OF APRIL 2004
Present: THE HONOURABLE MR. JUSTICE MARTINEAU
BETWEEN:
SOHAIL RASHEED
Applicant
- and -
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] The applicant seeks judicial review of the decision of the Immigration and Refugee Board, Refugee Protection Division (the Board), dated February 21, 2003, wherein it was decided that the applicant was not a "Convention refugee" or a "person in need of protection" pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act).

[2] The applicant is a citizen of Pakistan. He alleges a well-founded fear of persecution by reason of his political opinions. Central to the applicant's claim was his identity.

[3] The applicant entered Canada with a British passport under the name Mohammad Rafiq Sharif. Upon his arrival in Canada on January 19, 2001, the authorities identified his passport as being false. The applicant indicated to an immigration officer that he was Mohammad Khalid. The applicant subsequently completed his Personal Information Form (PIF) under the name Sohail Rasheed. At the hearing, the applicant indicated that Sohail Rasheed is his correct name.

[4] The applicant provided the Board with identification papers, including a birth certificate and school certificate under the name Sohail Rasheed. The applicant further submitted a four page photocopy of a Pakistani passport showing a picture of him under the name Sohail Rasheed. At the hearing, the applicant explained that he was unable to contact his friend, who had his passport, and all he could find was the photocopy provided. The applicant could not find his original National Identity Card (NIC), but did provide the Board with a duplicate copy of his NIC, which was issued by the Pakistani authorities. The latter was found to be probably authentic by Citizenship and Immigration Canada.

[5] The applicant alleges that he was involved for the past fifteen years in most of the important political events in Karachi and the province of Sindh. He presented to the Board several pictures of himself reproduced in the newspapers where he is seen with leaders for the Pakistan People's Party. He was a bodyguard to many top members of the party. Moreover, the applicant presented his party membership card (also with a picture of himself) and several letters of support from party members. Reference was also made to an official warrant of arrest issued under the seal of the Court of Najid Nughal, which was produced before the Board.

[6] The applicant's claim did not succeed as the Board found that he had not met his burden of establishing his identity. Accordingly, the Board concluded that the applicant's story, including allegations of persecution, was not credible.

[7] The reasons given by the Board for dismissing the documentary evidence establishing the applicant's identity are as follows:
1) There is no reasonable explanation for the applicant misleading the authorities upon his arrival in Canada;
2) The applicant only obtained a duplicate of the NIC approximately two months before his refugee hearing, leading the Board to question how the card was obtained, since the documentary evidence shows NICs are delivered only in person to male applicants;
3) With respect to the birth certificate and school certificate, the documentary evidence shows that false or forged documents are easily obtained upon payment of money; and
4) The photocopy of four pages of a Pakistani passport showing the applicant's picture and the name of Sohail Rasheed should not be given any probative value, since it is not an original and it is incomplete.

[8] The standard of review in credibility cases of the Board is patent unreasonableness (R.K.L. v. Canada (Minister of Citizenship and Immigration), [2003] F.C.J. No. 162 (T.D.) (QL)). As long as the inferences drawn by the tribunal are not patently unreasonable as to warrant intervention, its findings are not open to judicial review. Accordingly, the respondent suggests that it is logical to conclude that the question of whether a claimant possesses acceptable documentation establishing his or her identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding. That is indeed the view adopted by some judges of this Court (Najam v. Canada (Minister of Citizenship and Immigration, [2004] F.C.J. No. 516 at para. 14 (F.C.) (QL); and Gasparyan v. Canada (Minister of Citizenship and Immigration), [2003] F.C.J. No. 1103 at para. 6 (F.C.) (QL)).

[9] To contrast, the applicant submits that the question in issue does not strictly relate to credibility since foreign documents presented by a claimant in order to establish his or her identity are generally admissible under Canadian law (in this case the matter was heard in the province of Quebec). In this regard, counsel for the applicant has referred this Court to the following provisions:
a) Article 2822 of the Civil Code of Quebec:
Art. 2822. An act purporting to be issued by a competent foreign public officer makes proof of its content against all persons and neither the quality nor the signature of the officer need be proved.
Similarly, a copy of a document in the custody of the foreign public officer makes proof of its conformity to the original against all persons, and replaces the original if it purports to be issued by the officer
Art. 2822. L'acte qui émane apparemment d'un officier public étranger compétent fait preuve, à l'égard de tous, de son contenu, sans qu'il soit nécessaire de prouver la qualité ni la signature de cet officier.
De même, la copie d'un document dont l'officier public étranger est dépositaire fait preuve, à l'égard de tous, de sa conformité à l'original et supplée à ce dernier, si elle émane apparemment de cet officier.
b) Section 23 of the Canada Evidence Act, R.S.C. 1985, c. C-5:
23. (1) Evidence of any proceeding or record whatever of, in or before any court in Great Britain, the Supreme Court, the Federal Court of Appeal,
the Federal Court or the Tax Court of Canada, any court in a province, any court in a British colony or possession or any court of record of the United States, of a state of the United States or of any other foreign country, or before any justice of the peace or coroner in a province, may be given in any action or proceeding by an exemplification or certified copy of the proceeding or record, purporting to be under the seal of the court or under the hand or seal of the justice, coroner or court stenographer, as the case may be, without any proof of the authenticity of the seal or of the signature of the justice, coroner or court stenographer or other proof whatever.
(2) Where any court, justice or coroner or court stenographer referred to in subsection (1) has no seal, or so certifies, the evidence may be given by a copy purporting to be certified under the signature of a judge or presiding provincial court judge or of the justice or coroner or court stenographer, without any proof of the authenticity of the signature or other proof whatever.
23. (1) La preuve d'une procédure ou pièce d'un tribunal de la Grande-Bretagne, ou de la Cour suprême, ou de la Cour d'appel fédérale, ou de la Cour fédérale, ou de la Cour canadienne de l'impôt, ou d'un tribunal d'une province, ou de tout tribunal d'une colonie ou possession britannique, ou d'un tribunal d'archives des États-Unis, ou de tout État des États-Unis, ou d'un autre pays étranger, ou d'un juge de paix ou d'un coroner dans une province, peut se faire, dans toute action ou procédure, au moyen d'une ampliation ou copie certifiée de la procédure ou pièce, donnée comme portant le sceau du tribunal, ou la signature ou le sceau du juge de paix, du coroner ou du sténographe judiciaire, selon le cas, sans aucune preuve de l'authenticité de ce sceau ou de la signature du juge de paix, du coroner ou du sténographe judiciaire, ni autre preuve.
(2) Si un de ces tribunaux, ce juge de paix, ce coroner ou ce sténographe judiciaire n'a pas de sceau, ou certifie qu'il n'en a pas, la preuve peut se faire au moyen d'une copie donnée comme certifiée sous la signature d'un juge ou du juge de la cour provinciale présidant ce tribunal, ou de ce juge de paix, de ce coroner ou de ce sténographe judiciaire, sans aucune preuve de l'authenticité de cette signature, ni autre preuve.
c) Paragraph 25(1) of the Interpretation Act, R.S.C. 1985, c. I-21:
25(1) Where an enactment provides that a document is evidence of a fact without anything in the context to indicate that the document is conclusive evidence, then, in any judicial proceedings, the document is admissible in evidence and the fact is deemed to be established in the absence of any evidence to the contrary.
25(1) Fait foi de son contenu en justice sauf preuve contraire le document dont un texte prévoit qu'il établit l'existence d'un fait sans toutefois préciser qu'il l'établit de façon concluante.

[10] The applicant submits that the failure of the Board to accept identification papers for improper reasons constitutes an error of law. Hence, the standard of review with respect to such a decision is correctness.

[11] For the reasons that follow, applying the pragmatic and functional approach (Dr. Q. v. College of Physicians and Surgeons of British-Columbia, [2003] 1 S.C.R. 226 at para. 21 (S.C.C.)), I conclude that the determination with respect to the applicant's identity should be reviewed on a standard of reasonableness simpliciter.

[12] It is true that questions of law are generally reviewable on a standard of correctness (Pushpanathan v. Canada (Minister of Citizenship and Immigration, [1998] 1 S.C.R. 982 at para. 50 (S.C.C.)). That being said, in the present case, the acceptance or rejection by the Board of official foreign documents establishing identity raises a mixed question of fact and law.

[13] A claimant bears the onus of establishing his or her identity. Parliament has placed particular emphasis on the importance of providing acceptable documents. If not available, the Board is nevertheless obliged to decide whether the claimant has provided a reasonable explanation for the lack of documentation, or has taken reasonable steps to obtain it. That being said, it is within the purview of the Board to consider the failure to establish identity in its assessment of the overall credibility of a claimant.

[14] Section 106 of the Act provides as follows:
106. The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.
106. La Section de la protection des réfugiés prend en compte, s'agissant de crédibilité, le fait que, n'étant pas muni de papiers d'identité acceptables, le demandeur ne peut raisonnablement en justifier la raison et n'a pas pris les mesures voulues pour s'en procurer.

[15] Considering all relevant criteria, including the nature of the question, the expertise of the Board relative to that of this Court on the issue, the purpose of the Act, sections 96, 97 and 106 of the Act, I am of the view that the determination made by the Board with respect to the identity of the applicant should be examined on a reasonableness simpliciter standard. This conclusion is consistent with the reasoning and the result I have reached in Umba v. Canada (Ministre de la Citoyenneté et de l'Immigration), [2004] A.C.F. no 17 (F.C.) (QL).

[16] Having carefully examined the transcripts of the hearing held before the Board as well as the documentary evidence submitted by the applicant, I have concluded that the finding of the Board is not tenable. Taken either as a whole or independently, the reasons given by the Board cannot stand up to "a somewhat probing examination" (Law Society of New Brunswick v. Ryan, [2003] 1 S.C.R. 247 at paras. 48, 55 (S.C.C.)). Overall, I find the Board's decision unreasonable.

[17] The applicant did in fact explain in the course of his testimony why he had lied to the immigration authorities upon his arrival. He testified that he was following his agent's instructions. Indeed, when asked to explain the inconsistencies given to Canadian authorities, the applicant gave the following explanations:
Q. Now, this is where it gets a little bit strange for me anyway. Here you are, you're in the room with a Canadian Immigration officer. You've established some sort of relationship with the officer where the officer has grained your confidence and you have gained the confidence of the officer. Okay. Why don't you give her your real name?
A. The agent told me that if you are caught, then don't give your real name give another name. And he said that I was doing according to what he had said. He said if you act whatever I have told you, then it will be okay. Otherwise you will have problems. He said don't give my name and don't give your name, the real name.
Q. But at that point what did you think you were gonna achieve by giving her another false name?
A. I was afraid, I wasn't sure that I will be given asylum here, since I was locked in the room talking with them.
Q. But did they not say that they were gonna help you? Did they not say that you had problems, that they understood that Pakistan is a problematic country and that you may have had problems in Pakistan?
A. Yes, she said that, but I wasn't sure because the agent had told me that act on my instruction, whatever I am saying you do accordingly. And I was very nervous at that time, and I was in a position that I had run away, fled from there and came here, I had come here to save my life.
-. Okay.
Q. I mean, from what I understand, you decided to act on the instructions of your agent over the understanding that a CIC immigration officer demonstrated to you?
A. Yes, because before this, the immigration officer had made me scared saying that we'll send you back so that I could not trust her.

[18] Where a claimant travels on false documents, destroys travel documents or lies about them upon arrival following an agent's instructions, it has been held to be peripheral and of very limited value as a determination of general credibility. First, it is not uncommon for those who are fleeing from persecution not to have regular travel documents and, as a result of their fears and vulnerability, simply to act in accordance with the instructions of the agent who organized their escape. Second, whether a person has told the truth about his or her travel documents has little direct bearing on whether the person is indeed a refugee (Attakora v. Canada (Minister of Employment and Immigration, [1989] F.C.J. No. 444 (C.A) (QL); and Takhar v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 240 at para. 14 (T.D.) (QL).

[19] Despite the fact that the applicant lied in failing to give his real name to the Canadian authorities at the port of entry, it remains that the applicant subsequently provided numerous documents in order to establish his identity. In this regard, I am ready to accept that the basic rule in Canadian law is that foreign documents (whether they establish the identity or not of a claimant) purporting to be issued by a competent foreign public officer should be accepted as evidence of their content unless the Board has some valid reason to doubt of their authenticity.

[20] In Ramalingam v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No.10 (T.D.) (QL), Dubé J. notes at paragraphs 5 and 6:
(...) Moreover, identity documents issued by a foreign government are presumed to be valid unless evidence is produced to prove otherwise: see Gur, Jorge P. (1971), 1 I.A.C. 384 (I.A.B.)1. In that Immigration Appeal Board decision, the Chairman asked the following question at page 391:
The question here is, who can question the validity of an act of state and who, having questioned it, has the burden of proof as to its validity, and what proof is required?
He provided the right answer at page 392, as follows:
Although there is almost no jurisprudence to be found bearing directly on the point, it must be held that an act of state - a passport or a certificate of identity - is prima facie valid. The recognition of the sovereignty of a foreign state over its citizens or nationals and the comity of nations make any other finding untenable. The maxim omnia praesumuntur rite et solemniter esse acta applies with particular force here, establishing a rebuttable presumption of validity.

[6] In this instance, the Board challenged the validity of the birth certificate without adducing any evidence in support of its contention and, clearly, the matter of foreign documents it is not an area where the Board can claim particular knowledge. That, in my view, constitutes a reviewable error on the part of the Board.

[21] Unquestionably, there was no valid reason for the Board to discard the duplicate of the applicant's NIC, which constituted conclusive proof of the applicant's identity. Indeed, the latter document was sent for verification and the expert report concludes that the document in question is probably authentic. Accordingly, it should have been accepted as evidence of the applicant's identity.

[22] Moreover, the Board's reasoning for dismissing this apparently authentic document is arbitrary and capricious. Contrary to the suggestion made by the Board, the inscriptions on the document tend to prove that the duplicate has been issued in 1995 (while the original would have been issued in 1991), that is, many years before the applicant left Pakistan. Furthermore, the documentary evidence referred to by the Board in its decision does not establish conclusively that duplicate NICs are only delivered in person to male applicants. As appears from more recent documentary evidence, any bona fide family member can obtain prepared NICs of his family with written authorization from them (Tribunal Record, pp. 192-195, Government of Pakistan, Ministry of Interior, Directorate General of Registration, Question number 16). Accordingly, the Board has manifestly failed to consider that relevant part of the documentary evidence.

[23] As a whole, the impugned decision cannot stand. The reasons of the Board for discarding the other documentary evidence submitted by the applicant do not reside on strong grounds. Despite the fact that false or forged documents may be obtained in Pakistan upon payment for money, it remains that both the birth certificate and the high school leaving certificate have apparently been issued by the Government of Pakistan. The suggestion made by the Board that the latter documents may be forged is purely speculative when one considers in its entirety the documentary evidence submitted by the applicant.

[24] In conclusion, I note that this is not a case where the Board has closely examined a claimant's testimony and has determined that in light of the numerous contradictions and inconsistencies in said testimony, no probative value should be afforded to the documentary evidence submitted by the claimant (Ramalingam v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 10 (T.D.) (QL); and Ibnmogdad v. Canada (Minister of Citizenship and Immigration), [2004] F.C.J. No. 327 (F.C.) (QL)). Here, the credibility finding made by the Board is based on the initial lie made by the applicant to the immigration authorities.

[25] The errors made by the Board are determinative. Consequently, the present application should be allowed and the matter sent back for redetermin

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 853:2 · paragraphs 28-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f89f818f5fd0f88106e20d956542d5668a6e632bf0ab24cf33fb325f1eae62ad`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 853:2:subtheme:1 · paragraphs 28-28

- Raw key terms: `appearances, applicant, april, attorney, canada, daniel, dated, deputy`
- Display key terms: `april, daniel, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, daniel, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER: THE HONOURABLE MR. JUSTICE MARTINEAU
DATED: APRIL 21, 2004
APPEARANCES:
MR. STEWART ISTVANFFY FOR APPLICANT
MR. DANIEL LATULIPPE FOR RESPONDENT
SOLICITORS OF RECORD:
MR. STEWART ISTVANFFY FOR THE APPLICANT
MONTREAL, QUEBEC
MR. MORRIS ROSENBERG FOR THE RESPONDENT
DEPUTY ATTORNEY GENERAL OF CANADA
