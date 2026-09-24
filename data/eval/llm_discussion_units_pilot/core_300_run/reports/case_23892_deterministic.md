# Discussion Units: case 23892

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **39**
- Continuity pairs: **38**
- Discussion Units: **3**
- Paragraph source hashes: **39**
- Sub-themes: **6**

## 23892:1 · paragraphs 0-35

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `33a86f63a6d4d3d571b550cf2a8ce3f36d819a5cbf58867f9368e1544b7aec5e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23892:1:subtheme:1 · paragraphs 0-19

- Raw key terms: `applicant, record, respondent, italy, canada, stated, allegedly, lived`
- Display key terms: `italy, stated, allegedly, lived`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: italy, stated, allegedly, lived Position/evidence statements: [8] In May 2003, the applicant submitted an application for Old Age Security benefits, and the application was approved. Rule/authority context: [1] This is an application for judicial review under section 18. | A letter dated January 12, 2009, stated that the applicant did not qualify for an Old Age Security pension under the Agreement on Social Security between Canada and Italy (Respondent’s Record, Vol 1, pp 45-46). Application context: He said that he was ineligible for an Italian pension because he was no longer registered in that country’s records. | He stated that the information on file was false because he was trying to cover up the fact that he was in a relationship in Canada with Ms. Operative outcome context: The Tribunal dismissed Mr. | The applicant was granted Canadian citizenship on March 27, 1984 (Applicant’s Record, p 53). Evidence spans paragraphs 0-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5122116` offsets `47-52`; context: [1] This is an application for judicial review under section 18.
- Evidence: `disposition` cue `dismissed` at chunk `5122116` offsets `335-344`; context: The Tribunal dismissed Mr.
- Evidence: `evidence_fact` cue `Record` at chunk `5122117` offsets `365-371`; context: The applicant came back to Canada on March 8, 1978, on visa valid until March 1979 (Respondent’s Record, Vol 1, pp 75 and 80-81).
- Evidence: `counterargument_limitation` cue `However` at chunk `5122117` offsets `653-660`; context: However, the applicant’s spouse, their three (3) children and their seven (7) grandchildren are still living in Italy.
- Evidence: `disposition` cue `granted` at chunk `5122117` offsets `790-797`; context: The applicant was granted Canadian citizenship on March 27, 1984 (Applicant’s Record, p 53).
- Evidence: `evidence_fact` cue `Record` at chunk `5122118` offsets `292-298`; context: [3] The applicant allegedly lived with Michèle Breton from 1986 to 1999 at three (3) different addresses in Quebec: 1646 Bergerac Street in Vimont, Laval (1986–1993); 2747 Benjamin-Sulte Street in Montréal (1993–1995); and 103–2215 Des Laurentides Boulevard in Laval (1995–1999) (Applicant’s Record, Applicant’s Affidavit, p 29).
- Evidence: `evidence_fact` cue `Record` at chunk `5122119` offsets `97-103`; context: [4] The applicant used the address 1410 Stanley Street, in Montréal, several times (Respondent’s Record, Vol 1, pp 43, 60, 174).
- Evidence: `evidence_fact` cue `Record` at chunk `5122120` offsets `240-246`; context: Mannucci, is its sole director (Respondent’s Record, Vol 1, pp 35-37; Applicant’s Record, Applicant’s Affidavit, p 30).
- Evidence: `evidence_fact` cue `Record` at chunk `5122121` offsets `265-271`; context: [6] The applicant made mandatory contributions to the Instituto Nazionale Providenza Sociale (national social security institute) in Italy until January 1, 1979, and then continued making contributions on a voluntary basis in 1996, 1997, 1999 and 2000 (Applicant’s Record, Applicant’s Affidavit, p 30; Respondent’s Record, Vol 1, pp 23-24).
- Evidence: `evidence_fact` cue `Record` at chunk `5122122` offsets `104-110`; context: [7] A Canadian passport in the applicant’s name was issued by the Rome office in May 2002 (Respondent’s Record, Vol 1, p 74).
- Evidence: `party_position` cue `submitted` at chunk `5122123` offsets `31-40`; context: [8] In May 2003, the applicant submitted an application for Old Age Security benefits, and the application was approved.
- Evidence: `evidence_fact` cue `Record` at chunk `5122123` offsets `175-181`; context: He received benefits until December 2008 (Applicant’s Record, Applicant’s Affidavit, p 28; Respondent’s Record, Vol 1, pp 60-63).
- Evidence: `evidence_fact` cue `Record` at chunk `5122124` offsets `93-99`; context: [9] An investigation into the applicant’s residency was requested in June 2007 (Respondent’s Record, Vol 1, p 85).
- Evidence: `evidence_fact` cue `Record` at chunk `5122125` offsets `303-309`; context: Breton allegedly stated that the applicant was a very close friend but had never lived with her: the applicant was her landlord until he sold the condominium on Des Laurentides Boulevard in 2003 (Respondent’s Record, pp 95 and 114).
- Evidence: `evidence_fact` cue `Record` at chunk `5122126` offsets `750-756`; context: The applicant further stated that he had not kept any old invoices (Respondent’s Record, Vol 1, p 109).
- Evidence: `reasoning_application` cue `because` at chunk `5122126` offsets `606-613`; context: He said that he was ineligible for an Italian pension because he was no longer registered in that country’s records.
- Evidence: `evidence_fact` cue `Record` at chunk `5122127` offsets `539-545`; context: [12] After the interview, the applicant provided a list of addresses where he had allegedly lived but did not indicate the dates when he supposedly lived at these locations: (i) Berlioz Street, Nun’s Island, Montréal; (ii) two (2) different addresses on De l’Île-des-Sœurs Boulevard, Montréal; (iii) Sherbrooke Street West, Montréal; (iv) St-Marc Street, Montréal; (v) Des Laurentides Boulevard, Laval; (vi) Mariecourt Avenue, Québec; (vii) Benjamin [Sulte] Street, Montréal; (viii) current address: Du Parc Road, Mandeville (Respondent’s Record, Vol 1, p 162).
- Evidence: `evidence_fact` cue `Record` at chunk `5122128` offsets `87-93`; context: [13] The investigating officer’s report was signed on September 19, 2008 (Respondent’s Record, Vol 1, pp 150-53).
- Evidence: `evidence_fact` cue `Record` at chunk `5122129` offsets `262-268`; context: [14] Further to this investigation, a letter dated December 1, 2008, was sent to the applicant to inform him that the investigation had revealed that his principal residence was in Italy and that he had received an overpayment of more than $44,000 (Respondent’s Record, Vol 1, pp 43-44).
- Evidence: `governing_rule` cue `under` at chunk `5122129` offsets `471-476`; context: A letter dated January 12, 2009, stated that the applicant did not qualify for an Old Age Security pension under the Agreement on Social Security between Canada and Italy (Respondent’s Record, Vol 1, pp 45-46).
- Evidence: `evidence_fact` cue `Record` at chunk `5122130` offsets `146-152`; context: The request was denied by letter dated February 22, 2010 (Applicant’s Record, pp 33-35).
- Evidence: `disposition` cue `denied` at chunk `5122130` offsets `92-98`; context: The request was denied by letter dated February 22, 2010 (Applicant’s Record, pp 33-35).
- Evidence: `disposition` cue `dismissed` at chunk `5122131` offsets `187-196`; context: The Tribunal dismissed the applicant’s appeal.
- Evidence: `evidence_fact` cue `Record` at chunk `5122132` offsets `798-804`; context: Breton allegedly told the investigator on the telephone that the applicant had not lived with her because she did not want to discuss her personal business with strangers (Respondent’s Record, Vol 1, p 54; Applicant’s Record, Affidavit of Michèle Breton, p 86).
- Evidence: `reasoning_application` cue `because` at chunk `5122132` offsets `268-275`; context: He stated that the information on file was false because he was trying to cover up the fact that he was in a relationship in Canada with Ms.
- Evidence: `disposition` cue `denied` at chunk `5122132` offsets `481-487`; context: Breton, who had denied living with the applicant.
- Evidence: `evidence_fact` cue `testimony` at chunk `5122134` offsets `35-44`; context: [19] The Tribunal took note of the testimony of Ms.

#### 23892:1:subtheme:2 · paragraphs 20-24

- Raw key terms: `canada, applicant, application, person, regulations, security, approved, autres`
- Display key terms: `person, regulations, security, approved, autres`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: person, regulations, security, approved, autres Rule/authority context: (2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and (a) has attain | Standard of review Application context: (1) The Minister, at any time before or after approval of an application or after the requirement for an application is waived, may require the applicant, the person who applied on the applicant’s behalf, the beneficiary Evidence spans paragraphs 20-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5122135` offsets `264-269`; context: Issue
- Evidence: `evidence_fact` cue `evidence` at chunk `5122135` offsets `59-67`; context: [20] The Tribunal was of the opinion that, in light of the evidence on record, the applicant had arrived in Canada in 1976 but had not been a resident of Canada since that date.
- Evidence: `counterargument_limitation` cue `but` at chunk `5122135` offsets `123-126`; context: [20] The Tribunal was of the opinion that, in light of the evidence on record, the applicant had arrived in Canada in 1976 but had not been a resident of Canada since that date.
- Evidence: `issue` cue `issue` at chunk `5122136` offsets `53-58`; context: [21] This application for judicial review raises the issue of whether it was reasonable for the Tribunal, having found that the applicant had not established his residence in Canada and that he must reimburse the overpayment, to dismiss his appeal.
- Evidence: `evidence_fact` cue `found that` at chunk `5122136` offsets `113-123`; context: [21] This application for judicial review raises the issue of whether it was reasonable for the Tribunal, having found that the applicant had not established his residence in Canada and that he must reimburse the overpayment, to dismiss his appeal.
- Evidence: `governing_rule` cue `under` at chunk `5122137` offsets `403-408`; context: (2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person’s application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person’s application is approved.
- Evidence: `evidence_fact` cue `evidence` at chunk `5122139` offsets `701-709`; context: (1) The Minister, at any time before or after approval of an application or after the requirement for an application is waived, may require the applicant, the person who applied on the applicant’s behalf, the beneficiary or the person who receives payment on the applicant’s behalf, as the case may be, to make available or allow to be made available further information or evidence regarding the eligibility of the applicant or the beneficiary for a benefit.
- Evidence: `governing_rule` cue `Standard of review` at chunk `5122139` offsets `1690-1708`; context: Standard of review
- Evidence: `reasoning_application` cue `applied` at chunk `5122139` offsets `497-504`; context: (1) The Minister, at any time before or after approval of an application or after the requirement for an application is waived, may require the applicant, the person who applied on the applicant’s behalf, the beneficiary or the person who receives payment on the applicant’s behalf, as the case may be, to make available or allow to be made available further information or evidence regarding the eligibility of the applicant or the beneficiary for a benefit.

#### 23892:1:subtheme:3 · paragraphs 25-27

- Raw key terms: `applicant, tribunal, attorney, canada, considered, court, decision, evidence`
- Display key terms: `considered`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: considered Position/evidence statements: [26] As a preliminary argument, the respondent submitted that this Court should not consider a power of attorney attached to the applicant’s affidavit, since it is new evidence. | [27] The applicant submits that he provided the evidence required to prove that he is a Canadian resident and that the Tribunal made a palpable error in its decision. Rule/authority context: [25] The standard of review applicable to questions of mixed fact and law that have been considered by the Review Tribunal—that is, the determination of the applicant’s residence—is reasonableness (Dunsmuir v New Brunswi Application context: The Court’s analysis will therefore be limited to “the existence of justification, transparency and intelligibility within the decision-making process. Evidence spans paragraphs 25-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5122140` offsets `749-756`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para 47).
- Evidence: `governing_rule` cue `standard of review` at chunk `5122140` offsets `9-27`; context: [25] The standard of review applicable to questions of mixed fact and law that have been considered by the Review Tribunal—that is, the determination of the applicant’s residence—is reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 [Dunsmuir]; Singer v Canada (Attorney General), 2010 FC 607 at para 18, 370 FTR 121 [Singer]; De Bustamante v Canada (Attorney General), 2008 FC 1111 at para 34, [2008] FCJ no 1389 (QL) [De Bustamante]; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24, 280 FTR 296 [Chhabu]).
- Evidence: `reasoning_application` cue `therefore` at chunk `5122140` offsets `593-602`; context: The Court’s analysis will therefore be limited to “the existence of justification, transparency and intelligibility within the decision-making process.
- Evidence: `counterargument_limitation` cue `But` at chunk `5122140` offsets `719-722`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para 47).
- Evidence: `party_position` cue `submitted` at chunk `5122141` offsets `47-56`; context: [26] As a preliminary argument, the respondent submitted that this Court should not consider a power of attorney attached to the applicant’s affidavit, since it is new evidence.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5122141` offsets `141-150`; context: [26] As a preliminary argument, the respondent submitted that this Court should not consider a power of attorney attached to the applicant’s affidavit, since it is new evidence.
- Evidence: `party_position` cue `submits` at chunk `5122142` offsets `19-26`; context: [27] The applicant submits that he provided the evidence required to prove that he is a Canadian resident and that the Tribunal made a palpable error in its decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5122142` offsets `48-56`; context: [27] The applicant submits that he provided the evidence required to prove that he is a Canadian resident and that the Tribunal made a palpable error in its decision.

#### 23892:1:subtheme:4 · paragraphs 28-35

- Raw key terms: `court, canada, applicant, evidence, residence, tribunal, record, cannot`
- Display key terms: `residence, cannot`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: residence, cannot Position/evidence statements: Contrary to what the applicant submits, the Court notes that the burden of proof before the Tribunal rests on the applicant (Saraffian v Canada (Minister of Human Resources and Skills Development) 2012 FC 1532 at para 20 Rule/authority context: The respondent states that in De Bustamante, above at para 37, the Court pointed out that residence is a factual issue that requires an examination of the whole context of the individual under scrutiny. Application context: The Court is therefore of the opinion that, in light of all the evidence on record, the Court cannot conclude that this omission is fatal (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Boa | Given the evidence on record in this case, the Court is of the opinion that it was open to the Tribunal to conclude that the applicant has not established residence in Canada. Evidence spans paragraphs 28-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5122143` offsets `313-318`; context: The respondent states that in De Bustamante, above at para 37, the Court pointed out that residence is a factual issue that requires an examination of the whole context of the individual under scrutiny.
- Evidence: `governing_rule` cue `under` at chunk `5122143` offsets `387-392`; context: The respondent states that in De Bustamante, above at para 37, the Court pointed out that residence is a factual issue that requires an examination of the whole context of the individual under scrutiny.
- Evidence: `evidence_fact` cue `testimony` at chunk `5122144` offsets `128-137`; context: Diamant, the Tribunal states that it doubts the applicant’s testimony on the places where he allegedly lived during the periods he was not in a relationship with Ms.
- Evidence: `evidence_fact` cue `testimony` at chunk `5122145` offsets `109-118`; context: [30] The Court takes note of the applicant’s argument to the effect that the Tribunal failed to consider the testimony of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5122146` offsets `91-99`; context: [31] However, it is trite law that the Tribunal is not required to refer to every piece of evidence placed before it (Kombargi v Canada (Minister of Social Development), 2006 FC 1511 at para 12, 306 FTR 202).
- Evidence: `reasoning_application` cue `therefore` at chunk `5122146` offsets `436-445`; context: The Court is therefore of the opinion that, in light of all the evidence on record, the Court cannot conclude that this omission is fatal (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at paras 11-17, [2011] 3 SCR 708 [Newfoundland and Labrador Nurses]).
- Evidence: `party_position` cue `submits` at chunk `5122147` offsets `761-768`; context: Contrary to what the applicant submits, the Court notes that the burden of proof before the Tribunal rests on the applicant (Saraffian v Canada (Minister of Human Resources and Skills Development) 2012 FC 1532 at para 20, [2012] FCJ no 1620 (QL) [Saraffian]).
- Evidence: `evidence_fact` cue `evidence` at chunk `5122147` offsets `515-523`; context: The Court cannot help but note that the applicant gave the Tribunal only patchy evidence that he truly resided in Canada for a period of ten (10) years.
- Evidence: `evidence_fact` cue `evidence` at chunk `5122148` offsets `9-17`; context: [33] The evidence on record shows that the applicant filed tax returns in Canada, owned real estate, carried out business activities and contributed to the Quebec Pension Plan.
- Evidence: `counterargument_limitation` cue `However` at chunk `5122148` offsets `177-184`; context: However, the evidence also shows that there were long and frequent absences, as demonstrated by the stamps in his passport, that he had family ties and business interests in Italy, and that by his own admission, his lifestyle was such that he travelled a lot and had no furniture, just some clothes, in his residence in Canada (Respondent’s Record, Vol 1, p 109).
- Evidence: `evidence_fact` cue `evidence` at chunk `5122149` offsets `99-107`; context: [34] The courts have consistently held that it is up to the Tribunal, not this Court, to weigh the evidence presented to it.
- Evidence: `reasoning_application` cue `conclude` at chunk `5122149` offsets `232-240`; context: Given the evidence on record in this case, the Court is of the opinion that it was open to the Tribunal to conclude that the applicant has not established residence in Canada.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5122149` offsets `611-617`; context: The applicant is essentially asking this Court to assess the evidence in a manner that would be more favourable to him, which is something that this Court cannot do on judicial review.

#### Section text

De Carolis v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2013-04-12
Neutral citation
2013 FC 366
File numbers
T-2088-11
Decision Content
Date: 20130412
Docket: T-2088-11
Citation: 2013 FC 366
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, April 12, 2013
PRESENT: The Honourable Mr. Justice Boivin
BETWEEN:
FRANCO DE CAROLIS
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review under section 18.1 of the Federal Courts Act, RSC 1985, c F-7, of a decision of the Review Tribunal (the Tribunal) dated November 25, 2011, dismissing the applicant’s appeal concerning an application for a partial Old Age Security pension and a Guaranteed Income Supplement. The Tribunal dismissed Mr. De Carolis’ appeal, finding that he had never resided in Canada.
Factual background

[2] Franco De Carolis (the applicant) was born on September 7, 1937, in Italy. The applicant came to Canada for the first time on November 29, 1976, on a visa valid until December 29, 1976. He then returned to Rome and came back to Canada two (2) other times in 1977. The applicant came back to Canada on March 8, 1978, on visa valid until March 1979 (Respondent’s Record, Vol 1, pp 75 and 80-81). The date of the applicant’s official entry to Canada is May 17, 1979. At that time, he stated on his immigration entry card that his spouse, Olga Mannucci, and their three (3) children would be following him to Canada (Respondent’s Record, pp 62 and 71). However, the applicant’s spouse, their three (3) children and their seven (7) grandchildren are still living in Italy. The applicant was granted Canadian citizenship on March 27, 1984 (Applicant’s Record, p 53).

[3] The applicant allegedly lived with Michèle Breton from 1986 to 1999 at three (3) different addresses in Quebec: 1646 Bergerac Street in Vimont, Laval (1986–1993); 2747 Benjamin-Sulte Street in Montréal (1993–1995); and 103–2215 Des Laurentides Boulevard in Laval (1995–1999) (Applicant’s Record, Applicant’s Affidavit, p 29). The applicant then allegedly lived in Montréal from 1999 to 2003 (Applicant’s Record, Affidavit of Michèle Breton, p 85), and with Jacqueline Diamant from 2003 to 2007, in Québec City.

[4] The applicant used the address 1410 Stanley Street, in Montréal, several times (Respondent’s Record, Vol 1, pp 43, 60, 174). This is the address of his company, Decatour International Inc, a travel agency. The applicant is identified as the director, president and majority shareholder of Decatour.

[5] As regards the applicant’s business interests, he is a minority shareholder in Società Scambi Internazionali, a legal entity doing business as Neo Tours, in Rome. The applicant’s spouse, Ms. Mannucci, is its sole director (Respondent’s Record, Vol 1, pp 35-37; Applicant’s Record, Applicant’s Affidavit, p 30). The applicant’s spouse is also manager of the Hotel Iris Carillon in Fiuggi, Italy, which is owned by Società Costruzioni Italia. Ms. Mannucci was appointed chief executive officer of Società Costruzioni Italia (Respondent’s Record, Vol 1, pp 101-06).

[6] The applicant made mandatory contributions to the Instituto Nazionale Providenza Sociale (national social security institute) in Italy until January 1, 1979, and then continued making contributions on a voluntary basis in 1996, 1997, 1999 and 2000 (Applicant’s Record, Applicant’s Affidavit, p 30; Respondent’s Record, Vol 1, pp 23-24).

[7] A Canadian passport in the applicant’s name was issued by the Rome office in May 2002 (Respondent’s Record, Vol 1, p 74).

[8] In May 2003, the applicant submitted an application for Old Age Security benefits, and the application was approved. He received benefits until December 2008 (Applicant’s Record, Applicant’s Affidavit, p 28; Respondent’s Record, Vol 1, pp 60-63). In the application form, the applicant gave the address of his Montréal business, Decatour, as his mailing address, but he did not indicate a home address (Respondent’s Record, Vol 1, p 60).

[9] An investigation into the applicant’s residency was requested in June 2007 (Respondent’s Record, Vol 1, p 85). The investigator visited Decatour’s offices on December 11, 2007, where he was told that the applicant was in Italy (Respondent’s Record, p 94). When the applicant telephoned the investigator from Italy on December 12, 2007, he said that he was not planning to leave his wife, that he owned a hotel in Italy with four (4) other members of his family, that he had a house in Italy and that he was not receiving a pension in Italy. The applicant allegedly stated that he owned a condominium in Pierrefonds, Quebec, which he was renting out to third parties (Respondent’s Record, Vol 1, p 95).

[10] During a telephone call between Ms. Breton and the investigator on January 11, 2008, Ms. Breton allegedly stated that the applicant was a very close friend but had never lived with her: the applicant was her landlord until he sold the condominium on Des Laurentides Boulevard in 2003 (Respondent’s Record, pp 95 and 114).

[11] During an interview in May 2008, the applicant declared that he did not have any other passports besides his Canadian one. He presented a Quebec driver’s licence issued in 1995 and expired since August 2001 that indicated an address on Benjamin-Sulte Street in Montréal, an address allegedly matching that of Ms. Breton. The applicant declared that he was currently living on Du Parc Road in Mandeville, Quebec. He also stated that he kept nothing but some clothes at his Canadian residence, did not have any furniture and travelled a great deal. He said that he was ineligible for an Italian pension because he was no longer registered in that country’s records. The applicant further stated that he had not kept any old invoices (Respondent’s Record, Vol 1, p 109).

[12] After the interview, the applicant provided a list of addresses where he had allegedly lived but did not indicate the dates when he supposedly lived at these locations: (i) Berlioz Street, Nun’s Island, Montréal; (ii) two (2) different addresses on De l’Île-des-Sœurs Boulevard, Montréal; (iii) Sherbrooke Street West, Montréal; (iv) St-Marc Street, Montréal; (v) Des Laurentides Boulevard, Laval; (vi) Mariecourt Avenue, Québec; (vii) Benjamin [Sulte] Street, Montréal; (viii) current address: Du Parc Road, Mandeville (Respondent’s Record, Vol 1, p 162).

[13] The investigating officer’s report was signed on September 19, 2008 (Respondent’s Record, Vol 1, pp 150-53). The report sets out the following facts, among others:
- the applicant was unable to provide the dates when he lived at the indicated addresses, nor could he produce any documentary evidence of his residence;
- the address given in the pension application is a commercial building where Decatour was located, and there was no residential space in that building;
- the applicant’s Canadian passport, issued in Rome in 2002, contains numerous stamps from around the world but none for Canada;
- the applicant’s spouse owns Neo Tours, a business located in Rome, and he is its president;
- the applicant has no residence in his name in Canada, but his spouse has a house in Italy where the applicant lives when he goes there;
- the applicant has not established his place of residence in Canada, given his significant ties abroad (his family and a business interest), and he does not appear to have cut his ties with his country of origin and only puts in token appearances in Canada;
- the applicant does not use any public services in Canada, but it should be noted that he made contributions to the Quebec Pension Plan from 1978 to 1985 inclusively, and later from 1993 to 1997, with his last contribution being made in 2000, and that he filed income tax returns from 1979 to 1987, from 1994 to 2000, and from 2002 to 2007.

[14] Further to this investigation, a letter dated December 1, 2008, was sent to the applicant to inform him that the investigation had revealed that his principal residence was in Italy and that he had received an overpayment of more than $44,000 (Respondent’s Record, Vol 1, pp 43-44). His file was then transferred to International Operations in December 2008. A letter dated January 12, 2009, stated that the applicant did not qualify for an Old Age Security pension under the Agreement on Social Security between Canada and Italy (Respondent’s Record, Vol 1, pp 45-46).

[15] The applicant requested a review of that decision on January 30, 2009. The request was denied by letter dated February 22, 2010 (Applicant’s Record, pp 33-35). The applicant appealed against that appeal decision on May 19, 2010 (Applicant’s Record, pp 37-41). The Tribunal dismissed the applicant’s appeal on November 25, 2011. That decision is the subject of this judicial review.
The impugned decision

[16] The Tribunal hearing was held on September 14, 2011. The applicant testified, as did three (3) other witnesses: Michelle Breton, Jacqueline Diamant and Paolo Fogagnolo. The Tribunal dismissed the applicant’s appeal.

[17] Before the Tribunal, the applicant maintained that he had proved his residence in Canada since 1976. He explained that he left Canada for business trips and to visit his wife and children, who still live in Italy. He stated that the information on file was false because he was trying to cover up the fact that he was in a relationship in Canada with Ms. Breton while he was still married. The file contained business office addresses and the addresses of Ms. Breton, who had denied living with the applicant. Ms. Breton testified before the Tribunal that the applicant lived with her from 1986 to 1999. Ms. Breton allegedly told the investigator on the telephone that the applicant had not lived with her because she did not want to discuss her personal business with strangers (Respondent’s Record, Vol 1, p 54; Applicant’s Record, Affidavit of Michèle Breton, p 86).

[18] The Tribunal noted that the applicant and his wife never separated, that they continued to operate the Hotel Iris Carillon in Italy, that his doctor was mainly in Italy, and that he had an interest in a travel agency in Rome, Neo Tours, of which he was president and manager.

[19] The Tribunal took note of the testimony of Ms. Diamant, who states that the applicant lived with her between 2003 and 2007 in Québec City, and that he would bring a bag with him and had no furniture or any other possessions at her place. The Tribunal also noted the testimony of the applicant himself, who stated that his businesses were in Canada, and that he has resided and had a bank account here for at least twenty (20) years.

[20] The Tribunal was of the opinion that, in light of the evidence on record, the applicant had arrived in Canada in 1976 but had not been a resident of Canada since that date. According to the Tribunal, the applicant is present, rather than resident, in Canada.
Issue

[21] This application for judicial review raises the issue of whether it was reasonable for the Tribunal, having found that the applicant had not established his residence in Canada and that he must reimburse the overpayment, to dismiss his appeal.
Legislative provisions

[22] Subsection 3(2) of the Old Age Security Act, RSC 1985, c O-9, sets out the following requirements to be met to qualify for a partial pension:
PART I
MONTHLY PENSION
Pension Payable
. . .
Payment of partial pension
3. (2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person’s application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person’s application is approved.
. . .
PARTIE I
PENSIONS
Ayants droit
[…]
Pension partielle
3. (2) Sous réserve des autres dispositions de la présente loi et de ses règlements, une pension partielle est payable aux personnes qui ne peuvent bénéficier de la pleine pension et qui, à la fois :
a) ont au moins soixante-cinq ans;
b) ont, après l’âge de dix-huit ans, résidé en tout au Canada pendant au moins dix ans mais moins de quarante ans avant la date d’agrément de leur demande et, si la période totale de résidence est inférieure à vingt ans, résidaient au Canada le jour précédant la date d’agrément de leur demande.
[…]

[23] Subsection 21(1) of the Old Age Security Regulations, CRC, c 1246, defines residence as distinct from presence:
Residence
. . .
21. (1) For the purposes of the Act and these Regulations,
(a) a person resides in Canada if he makes his home and ordinarily lives in any part of Canada; and
(b) a person is present in Canada when he is physically present in any part of Canada.
. . .
Résidence
[…]
21. (1) Aux fins de la Loi et du présent règlement,
a) une personne réside au Canada si elle établit sa demeure et vit ordinairement dans une région du Canada; et
b) une personne est présente au Canada lorsqu’elle se trouve physiquement dans une région du Canada.
[…]

[24] Finally, section 23 of the Old Age Security Regulations, above, provides that the Minister may conduct an investigation before or after an application has been approved:
Further Information and Investigation Before or After the Approval of an Application or Before or After the Requirement of an Application Is Waived
23. (1) The Minister, at any time before or after approval of an application or after the requirement for an application is waived, may require the applicant, the person who applied on the applicant’s behalf, the beneficiary or the person who receives payment on the applicant’s behalf, as the case may be, to make available or allow to be made available further information or evidence regarding the eligibility of the applicant or the beneficiary for a benefit.
(2) The Minister may at any time make an investigation into the eligibility of a person to receive a benefit including the capacity of a beneficiary to manage his own affairs.
Autres renseignements et enquêtes avant ou après l’agrément de la demande ou l’octroi de la dispense
23. (1) Le ministre peut, avant ou après l’agrément d’une demande ou après l’octroi d’une dispense, exiger que le requérant, la personne qui a fait la demande en son nom, le prestataire ou la personne qui touche la pension pour le compte de ce dernier, selon le cas, permette l’accès à des renseignements ou des éléments de preuve additionnels concernant l’admissibilité du requérant ou du prestataire à une prestation.
(2) Le ministre peut, en tout temps, faire enquête sur l’admissibilité d’une personne à une prestation, y compris sur la capacité du prestataire pour ce qui est de l’administration de ses propres affaires.
Standard of review

[25] The standard of review applicable to questions of mixed fact and law that have been considered by the Review Tribunal—that is, the determination of the applicant’s residence—is reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 [Dunsmuir]; Singer v Canada (Attorney General), 2010 FC 607 at para 18, 370 FTR 121 [Singer]; De Bustamante v Canada (Attorney General), 2008 FC 1111 at para 34, [2008] FCJ no 1389 (QL) [De Bustamante]; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24, 280 FTR 296 [Chhabu]). The Court’s analysis will therefore be limited to “the existence of justification, transparency and intelligibility within the decision-making process. But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para 47).
Analysis

[26] As a preliminary argument, the respondent submitted that this Court should not consider a power of attorney attached to the applicant’s affidavit, since it is new evidence. As this evidence was not before the Tribunal, it should not be considered on judicial review (Swain v Canada (Attorney General), 2003 FCA 434 at para 2, [2003] FCJ no 1719 (QL)). Indeed, the Court finds that this power of attorney authorizing the applicant’s lawyer to sell his condominium in Pierrefonds was not before the Tribunal (Applicant’s Record, pp 69-72). The Court will disregard this document.

[27] The applicant submits that he provided the evidence required to prove that he is a Canadian resident and that the Tribunal made a palpable error in its decision. He also argues that the burden of proof has been reversed such that the onus is on the respondent to prove that he is not a resident.

[28] The respondent, meanwhile, points out that to meet the residency requirement, a person must make his or her home and ordinarily live in Canada (Old Age Security Regulations, paragraph 21(1)(a)). The respondent states that in De Bustamante, above at para 37, the Court pointed out that residence is a factual issue that requires an examination of the whole context of the individual under scrutiny.

[29] Regarding the content of the testimonies of Ms. Breton and Ms. Diamant, the Tribunal states that it doubts the applicant’s testimony on the places where he allegedly lived during the periods he was not in a relationship with Ms. Breton. The Court is of the opinion that the Tribunal did not disregard the testimonies of Ms. Breton and Ms. Diamant but rather found that it disagrees that the applicant was resident in Canada. As the respondent notes, evidence of a relationship is not necessarily evidence of residence, which must be distinguished from physical presence in Canada within the meaning of the Old Age Security Act and its Regulations.

[30] The Court takes note of the applicant’s argument to the effect that the Tribunal failed to consider the testimony of Mr. Fogagnolo in its decision. According to Mr. Fogagnolo’s affidavit, he testified before the Tribunal that he knew the applicant and had personal knowledge that the applicant resided in the areas of Montréal and Laval from 1976 to 2003 before moving to Québec City and living with Ms. Diamant until 2007 (Applicant’s Record, p 90).

[31] However, it is trite law that the Tribunal is not required to refer to every piece of evidence placed before it (Kombargi v Canada (Minister of Social Development), 2006 FC 1511 at para 12, 306 FTR 202). Although it would no doubt be preferable that the Tribunal mention Mr. Fogagnolo’s testimony, it appears from his affidavit that he simply repeated, in general terms, the testimonies of Ms. Breton and Ms. Diamant. The Court is therefore of the opinion that, in light of all the evidence on record, the Court cannot conclude that this omission is fatal (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at paras 11-17, [2011] 3 SCR 708 [Newfoundland and Labrador Nurses]). Moreover, the Tribunal is presumed to have considered and weighed all the evidence before it, unless it is proved otherwise (Florea v Canada (Minister of Employment and Immigration) (FCA), [1993] FCJ no 598 (QL)).

[32] The case law has laid down a non-exhaustive list of factors to consider when establishing residence, for example, in Ding, above, and De Bustamante, above at para 38. These factors are personal property, social and fiscal ties in Canada, ties in another country, regularity and length of visits to Canada, as well as the frequency and length of absences from Canada, the lifestyle of the person and his or her establishment here. The Court cannot help but note that the applicant gave the Tribunal only patchy evidence that he truly resided in Canada for a period of ten (10) years. The applicant did not provide any leases, utility bills, bank statements or any other evidence that he had a residence in 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23892:2 · paragraphs 36-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `239db85b18e26a17640882ae6380ae322f3cd4a256192d93c74fcb7e3e6ac4be`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23892:2:subtheme:1 · paragraphs 36-37

- Raw key terms: `adjudges, application, attorney, boivin, canada, carolis, cause, certified`
- Display key terms: `adjudges, boivin, carolis, certified`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adjudges, boivin, carolis, certified No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that the application for judicial review be dismissed. Without costs.
“Richard Boivin”
Judge
Certified true translation
Michael Palles
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: T-2088-11
STYLE OF CAUSE: Franco De Carolis
v Attorney General of Canada
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: March 26, 2013
REASONS FOR 

## 23892:3 · paragraphs 38-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8622f93dbc976f1785781bfdf87444e6265908895dfa7fd8e1fb7e0f0d86b0cf`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23892:3:subtheme:1 · paragraphs 38-38

- Raw key terms: `appearances, applicant, april, attorney, boivin, canada, cerundolo, dated`
- Display key terms: `april, boivin, cerundolo, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, boivin, cerundolo, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 38-38. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: BOIVIN J.
DATED: April 12, 2013
APPEARANCES:
Denis Maiorino
FOR THE APPLICANT
Vanessa Luna
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Cerundolo & Maiorino
Montréal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General Canada
FOR THE RESPONDENT
