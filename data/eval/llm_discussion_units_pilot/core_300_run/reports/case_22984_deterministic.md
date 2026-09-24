# Discussion Units: case 22984

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **70**
- Continuity pairs: **69**
- Discussion Units: **1**
- Paragraph source hashes: **70**
- Sub-themes: **16**

## 22984:1 · paragraphs 0-69

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0d04cd30046860e93ee494cd764542850547217511fca1cd30026b8219f8c59c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22984:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, application, attorney, canada, decision, duncan, federal, general`
- Display key terms: `duncan, federal`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: duncan, federal Rule/authority context: Pursuant to subsections 303(1) and (2) of the Federal Courts Rules, SOR/98-106, the Attorney General of Canada is the properly named Respondent in this matter, and shall replace the Minister of Human Resources and Skills Application context: [2] For the reasons that follow, I find that the application for judicial review should be granted. Operative outcome context: [2] For the reasons that follow, I find that the application for judicial review should be granted. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5077438` offsets `256-263`; context: Duncan (the “Applicant”) to be ineligible for an Old Age Security (OAS) pension, whether full or partial.
- Evidence: `reasoning_application` cue `I find` at chunk `5077439` offsets `33-39`; context: [2] For the reasons that follow, I find that the application for judicial review should be granted.
- Evidence: `disposition` cue `granted` at chunk `5077439` offsets `91-98`; context: [2] For the reasons that follow, I find that the application for judicial review should be granted.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5077440` offsets `126-137`; context: Pursuant to subsections 303(1) and (2) of the Federal Courts Rules, SOR/98-106, the Attorney General of Canada is the properly named Respondent in this matter, and shall replace the Minister of Human Resources and Skills Development (the “Minister”) in that capacity.

#### 22984:1:subtheme:2 · paragraphs 4-5

- Raw key terms: `applicant, canada, england, full-time, home, part-time, pension, accept`
- Display key terms: `england, full-time, home, part-time, pension, accept`
- Argument roles: `party_position, reasoning_application`
- Explanation: Observed roles: party_position, reasoning_application Display terms: england, full-time, home, part-time, pension, accept Position/evidence statements: In 2002, the Applicant resigned his law partnership in England and claims to have left his London home in order to accept a full-time consultancy position with a Vancouver-based law firm. Application context: [5] The Applicant applied for an OAS pension on September 6, 2007. Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5077441` offsets `408-414`; context: In 2002, the Applicant resigned his law partnership in England and claims to have left his London home in order to accept a full-time consultancy position with a Vancouver-based law firm.
- Evidence: `reasoning_application` cue `applied` at chunk `5077442` offsets `18-25`; context: [5] The Applicant applied for an OAS pension on September 6, 2007.

#### 22984:1:subtheme:3 · paragraphs 6-8

- Raw key terms: `applicant, canada, dated, letter, claimed, country, february, indicated`
- Display key terms: `dated, letter, claimed, country, february, indicated`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: dated, letter, claimed, country, february, indicated Position/evidence statements: In a question addressing CPP contributions between the years 2002 and 2004, the Applicant responded as follows: “Not paid but claimed by CRA. | In a letter to the Client Services Division, International Tax Services, dated 11/7/06, the Applicant claimed: “I am not at present ‘living’ or ‘resident’ in any country. Application context: […] Accordingly, I did not again become a ‘resident’ of Canada, factual or otherwise, in 2002 merely by my 9 months’ consultancy stay, but was only a visitor […]” (Respondent’s Record, Volume 1, Tab 2, p. Operative outcome context: For these reasons, his application was denied. Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5077443` offsets `189-197`; context: In a question addressing CPP contributions between the years 2002 and 2004, the Applicant responded as follows: “Not paid but claimed by CRA.
- Evidence: `party_position` cue `claimed` at chunk `5077443` offsets `310-317`; context: In a question addressing CPP contributions between the years 2002 and 2004, the Applicant responded as follows: “Not paid but claimed by CRA.
- Evidence: `evidence_fact` cue `Record` at chunk `5077443` offsets `430-436`; context: As above I was not ‘living’ in Canada 02-Date but was a part-time non-resident sojourner” (Respondent’s Record, Volume 1, Tab 2, p.
- Evidence: `party_position` cue `claimed` at chunk `5077444` offsets `760-767`; context: In a letter to the Client Services Division, International Tax Services, dated 11/7/06, the Applicant claimed: “I am not at present ‘living’ or ‘resident’ in any country.
- Evidence: `evidence_fact` cue `Record` at chunk `5077444` offsets `621-627`; context: In his CRA Determination of Residency Status form, dated 12/5/06, the Applicant indicated that he “sojourn[ed] in Canada as a Canadian citizen staying for short stays as a non-resident and also in England and Spain”, was “not resident in Canada full-time or England or Spain, but [would] travel/sojourn to each”, and was involved in “part-time legal [handwriting unclear] work occasionally when in BC when & if I get any” (Respondent’s Record, Volume 1, Tab 2, pp.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5077444` offsets `833-844`; context: […] Accordingly, I did not again become a ‘resident’ of Canada, factual or otherwise, in 2002 merely by my 9 months’ consultancy stay, but was only a visitor […]” (Respondent’s Record, Volume 1, Tab 2, p.
- Evidence: `disposition` cue `denied` at chunk `5077445` offsets `369-375`; context: For these reasons, his application was denied.

#### 22984:1:subtheme:4 · paragraphs 9-16

- Raw key terms: `applicant, dated, decision, letter, review, appeal, tribunal, canadian`
- Display key terms: `dated, letter, review, canadian`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: dated, letter, review, canadian Position/evidence statements: In his request for reconsideration to the Regional Director of Human Resources and Social Development, the Applicant submitted that he made a number of errors in his initial application, including: (i) listing his Englis | The hearing was adjourned to allow the Applicant additional time to submit further documentation. Rule/authority context: [12] By letter dated October 20, 2011, and marked “without prejudice”, HRSDC informed the Applicant that, following a review of the additional information provided since June 2011, it had determined that he did meet the  | Decision under review Operative outcome context: On February 1, 2012, the Review Tribunal dismissed the Applicant’s appeal. Evidence spans paragraphs 9-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5077446` offsets `1037-1045`; context: With respect to the residence questionnaire (dated January 25, 2008), he submits that he correctly stated his ‘part-time non-(full-time) resident sojourner’ status in response to question 10.
- Evidence: `party_position` cue `submitted` at chunk `5077446` offsets `237-246`; context: In his request for reconsideration to the Regional Director of Human Resources and Social Development, the Applicant submitted that he made a number of errors in his initial application, including: (i) listing his English address instead of his Vancouver address; (ii) listing that he was a part-time resident of England instead of a part-time resident of Vancouver from 2002 to the date of application (September 6, 2007), having allegedly missed a note instructing him to disregard ‘periods when you were outside Canada for less than six months at a time’; and (iii) listing that he ‘live[d] permanently outside Canada’, when he claims to have in fact lived part-time in British Columbia and part-time (but not permanently) in England.
- Evidence: `counterargument_limitation` cue `but` at chunk `5077446` offsets `825-828`; context: In his request for reconsideration to the Regional Director of Human Resources and Social Development, the Applicant submitted that he made a number of errors in his initial application, including: (i) listing his English address instead of his Vancouver address; (ii) listing that he was a part-time resident of England instead of a part-time resident of Vancouver from 2002 to the date of application (September 6, 2007), having allegedly missed a note instructing him to disregard ‘periods when you were outside Canada for less than six months at a time’; and (iii) listing that he ‘live[d] permanently outside Canada’, when he claims to have in fact lived part-time in British Columbia and part-time (but not permanently) in England.
- Evidence: `party_position` cue `submit` at chunk `5077448` offsets `143-149`; context: The hearing was adjourned to allow the Applicant additional time to submit further documentation.
- Evidence: `evidence_fact` cue `determined that` at chunk `5077449` offsets `188-203`; context: [12] By letter dated October 20, 2011, and marked “without prejudice”, HRSDC informed the Applicant that, following a review of the additional information provided since June 2011, it had determined that he did meet the residence requirements under the OASA.
- Evidence: `governing_rule` cue `under` at chunk `5077449` offsets `243-248`; context: [12] By letter dated October 20, 2011, and marked “without prejudice”, HRSDC informed the Applicant that, following a review of the additional information provided since June 2011, it had determined that he did meet the residence requirements under the OASA.
- Evidence: `counterargument_limitation` cue `although` at chunk `5077449` offsets `291-299`; context: The Applicant was informed that although his passports confirm several absences from Canada from May 16, 2006 onwards, HRSDC calculated his Canadian residence from April 3, 2002 to September 10, 2007.
- Evidence: `evidence_fact` cue `Record` at chunk `5077450` offsets `319-325`; context: The Applicant requested that the Respondent reconsider its decision and amend the offer to reflect a full OAS pension (Respondent’s Record, Volume III, p.
- Evidence: `governing_rule` cue `under` at chunk `5077451` offsets `232-237`; context: Decision under review
- Evidence: `disposition` cue `dismissed` at chunk `5077451` offsets `119-128`; context: On February 1, 2012, the Review Tribunal dismissed the Applicant’s appeal.
- Evidence: `party_position` cue `submit` at chunk `5077452` offsets `289-295`; context: The decision notes that the appeal hearing was adjourned at the Applicant’s request on June 14, 2011, in order to permit him to submit further documentary evidence regarding his Canadian residency.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077452` offsets `316-324`; context: The decision notes that the appeal hearing was adjourned at the Applicant’s request on June 14, 2011, in order to permit him to submit further documentary evidence regarding his Canadian residency.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5077452` offsets `126-137`; context: [15] As noted above, the Review Tribunal found the Applicant to be ineligible to receive either a full or partial OAS pension pursuant to section 3 of the OASA.

#### 22984:1:subtheme:5 · paragraphs 17-21

- Raw key terms: `canada, review, tribunal, applicant, relevant, during, evidence, full`
- Display key terms: `review, relevant, during, full`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: review, relevant, during, full Rule/authority context: [19] The Review Tribunal considered the parties’ submissions and the eligibility requirements for full and partial OAS benefits under subsections 3(1) and (2) of the OASA, as well as under subsection 21(1) of the Old Age | [20] Ultimately, the Review Tribunal found that, upon weighing all of the evidence and examining the whole context of the individual, the Applicant did not intend to reside and did not reside in Canada as required under  Evidence spans paragraphs 17-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077454` offsets `14-19`; context: [17] The only issue on appeal before the Review Tribunal was a determination of the Applicant’s duration and periods of residency in Canada for the purposes of determining whether he should be entitled to receive a full or partial OAS pension or no pension at all.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077455` offsets `225-233`; context: [18] The Review Tribunal surveyed a number of statements suggesting that the Applicant was not resident and did not consider himself to be resident in Canada during the Relevant Period, as well as the documentation and other evidence put forward by the Applicant in support of what he now alleges to be “part-time residence in Canada from 2002 to 2008”.
- Evidence: `governing_rule` cue `under` at chunk `5077456` offsets `128-133`; context: [19] The Review Tribunal considered the parties’ submissions and the eligibility requirements for full and partial OAS benefits under subsections 3(1) and (2) of the OASA, as well as under subsection 21(1) of the Old Age Security Regulations, CRC, c 1246 (the “OAS Regulations”), finding that the two periods of time relevant to determining the Appellant’s residency in Canada are: (i) April 4, 2002 to March 19, 2007; and (ii) March 20, 2007 to March 19, 2008.
- Evidence: `evidence_fact` cue `found that` at chunk `5077457` offsets `37-47`; context: [20] Ultimately, the Review Tribunal found that, upon weighing all of the evidence and examining the whole context of the individual, the Applicant did not intend to reside and did not reside in Canada as required under the OASA and the OAS Regulations during the two relevant time periods.
- Evidence: `governing_rule` cue `under` at chunk `5077457` offsets `214-219`; context: [20] Ultimately, the Review Tribunal found that, upon weighing all of the evidence and examining the whole context of the individual, the Applicant did not intend to reside and did not reside in Canada as required under the OASA and the OAS Regulations during the two relevant time periods.
- Evidence: `evidence_fact` cue `found that` at chunk `5077458` offsets `190-200`; context: [21] The Review Tribunal placed significant weight on the statements in the Applicant’s OAS application suggesting that he did not consider himself a resident during the Relevant Period and found that “[w]hile the [Applicant] has testified that in fact he filled in the OAS Application incorrectly, it does not follow that he can retroactively revise or amend that application at the time of the appeal hearing” (Review Tribunal Decision, para 57).

#### 22984:1:subtheme:6 · paragraphs 22-22

- Raw key terms: `absence, account, applicant, assisting, basis, bills, canada, decision`
- Display key terms: `absence, account, assisting, basis, bills`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: absence, account, assisting, basis, bills Evidence spans paragraphs 22-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5077459` offsets `501-507`; context: Issues
- Evidence: `evidence_fact` cue `evidence` at chunk `5077459` offsets `80-88`; context: [22] The Review Tribunal also emphasized the insufficiency of the “patchwork of evidence filed” by the Applicant for the Relevant Period, and noted that a “pattern of late and over due payments of invoices since 2002” suggested absence, rather than assisting in establishing residency.

#### 22984:1:subtheme:7 · paragraphs 23-27

- Raw key terms: `canada, person, regulations, residence, period, sente, sidence, subsection`
- Display key terms: `person, regulations, residence, period, sente, sidence, subsection`
- Argument roles: `counterargument_limitation, governing_rule`
- Explanation: Observed roles: counterargument_limitation, governing_rule Display terms: person, regulations, residence, period, sente, sidence, subsection Rule/authority context: [23] Having reviewed the materials and submissions of both parties, I am of the view that the following questions must be determined: i) What is the applicable standard of review? | [25] If an individual cannot qualify for a full OAS pension, he or she may qualify for a partial pension under subsection 3(2) of the OASA. Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `standard of review` at chunk `5077460` offsets `160-178`; context: [23] Having reviewed the materials and submissions of both parties, I am of the view that the following questions must be determined:
i) What is the applicable standard of review?
- Evidence: `counterargument_limitation` cue `However` at chunk `5077461` offsets `172-179`; context: However, paragraph 3(1)(b) of the OASA sets out the criteria to be met in order for an individual to qualify for a full OAS pension without having 40 years of residence.
- Evidence: `governing_rule` cue `under` at chunk `5077462` offsets `105-110`; context: [25] If an individual cannot qualify for a full OAS pension, he or she may qualify for a partial pension under subsection 3(2) of the OASA.
- Evidence: `governing_rule` cue `standard of review` at chunk `5077464` offsets `719-737`; context: …
i) What is the applicable standard of review?

#### 22984:1:subtheme:8 · paragraphs 28-29

- Raw key terms: `acceptable, attorney, canada, court, decided, decision, dunsmuir, general`
- Display key terms: `acceptable, decided, dunsmuir`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: acceptable, decided, dunsmuir Rule/authority context: [28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reaso Application context: [28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reaso | [29] With respect to allegations of breach of procedural fairness, the Court will apply a standard of correctness. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077465` offsets `84-89`; context: [28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reasonableness standard, save and except where the critical issue is the proper legal test to be applied for determining residency (which is not the case here): see Canada (Minister of Human Resources Development) v Ding, 2005 FC 76 [Ding] at paras 58-60; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24; Kiefer v Canada (Attorney General), 2008 FC 786 at paras 20-21; de Bustamante v Canada (Attorney General), 2008 FC 1111 at paras 33-34; Singer v Canada (Attorney General), 2010 FC 607 at para 18.
- Evidence: `governing_rule` cue `legal test` at chunk `5077465` offsets `295-305`; context: [28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reasonableness standard, save and except where the critical issue is the proper legal test to be applied for determining residency (which is not the case here): see Canada (Minister of Human Resources Development) v Ding, 2005 FC 76 [Ding] at paras 58-60; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24; Kiefer v Canada (Attorney General), 2008 FC 786 at paras 20-21; de Bustamante v Canada (Attorney General), 2008 FC 1111 at paras 33-34; Singer v Canada (Attorney General), 2010 FC 607 at para 18.
- Evidence: `reasoning_application` cue `therefore` at chunk `5077465` offsets `189-198`; context: [28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reasonableness standard, save and except where the critical issue is the proper legal test to be applied for determining residency (which is not the case here): see Canada (Minister of Human Resources Development) v Ding, 2005 FC 76 [Ding] at paras 58-60; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24; Kiefer v Canada (Attorney General), 2008 FC 786 at paras 20-21; de Bustamante v Canada (Attorney General), 2008 FC 1111 at paras 33-34; Singer v Canada (Attorney General), 2010 FC 607 at para 18.
- Evidence: `issue` cue `question` at chunk `5077466` offsets `201-209`; context: As a result, no deference is owed to the decision-maker in such matters, and the only question to be decided is whether the procedure followed was fair: Attorney General of Canada v Sketchley, 2005 FCA 404, [2006] 3 FCR 392 at para 52-55; Canadian Union of Public Employees (CUPE) v Ontario (Minister of Labour), 2003 SCC 29, [2003] 1 SCR 539 at para 100-103.
- Evidence: `reasoning_application` cue `apply` at chunk `5077466` offsets `82-87`; context: [29] With respect to allegations of breach of procedural fairness, the Court will apply a standard of correctness.

#### 22984:1:subtheme:9 · paragraphs 30-34

- Raw key terms: `settlement, applicant, canada, cannot, documents, hearing, pension, privilege`
- Display key terms: `settlement, cannot, documents, hearing, pension, privilege`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: settlement, cannot, documents, hearing, pension, privilege Position/evidence statements: The Applicant claims that the exclusion of these letters resulted in a breach of procedural fairness and unfairly deprived him of the opportunity to make full submissions. | The Applicant contends, however, that the privilege was waived in the case at hand when the Review Tribunal decided to include these documents in the hearing file. Application context: [34] In addition, the Applicant cannot seriously contend that he was prevented from making full submissions because he relied on the October 20, 2011 letter to establish residency from 2002 to 2007. Evidence spans paragraphs 30-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077467` offsets `695-700`; context: The letter of settlement and reply were both marked as “without prejudice” and the Review Tribunal decided, “[a]fter receiving oral submissions from the parties and after careful consideration,” that their inclusion would be inappropriate and that the documents were “not relevant to the primary issue on appeal, that is, the establishment, or lack thereof, of the Appellant’s Canadian residency” from 2002 to 2008.
- Evidence: `party_position` cue `claims` at chunk `5077467` offsets `829-835`; context: The Applicant claims that the exclusion of these letters resulted in a breach of procedural fairness and unfairly deprived him of the opportunity to make full submissions.
- Evidence: `evidence_fact` cue `Record` at chunk `5077467` offsets `102-108`; context: [30] In a letter of settlement dated October 20, 2011, and reproduced at page 691 of the Respondent’s Record, a Service Canada Benefits Officer accepted that the Applicant had resumed residence in Canada in 2002 and offered him a partial (23/40ths) pension.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5077468` offsets `546-554`; context: As Wigmore stated, “[…] admissions made in the course of settlement negotiations may not be concessions of wrongs done, but merely an expression of a desire to purchase peace, and as such irrelevant and inadmissible”: see Wigmore on Evidence (Chadbourn rev.
- Evidence: `party_position` cue `contends` at chunk `5077469` offsets `256-264`; context: The Applicant contends, however, that the privilege was waived in the case at hand when the Review Tribunal decided to include these documents in the hearing file.
- Evidence: `counterargument_limitation` cue `however` at chunk `5077469` offsets `266-273`; context: The Applicant contends, however, that the privilege was waived in the case at hand when the Review Tribunal decided to include these documents in the hearing file.
- Evidence: `party_position` cue `contend` at chunk `5077471` offsets `49-56`; context: [34] In addition, the Applicant cannot seriously contend that he was prevented from making full submissions because he relied on the October 20, 2011 letter to establish residency from 2002 to 2007.
- Evidence: `reasoning_application` cue `because` at chunk `5077471` offsets `108-115`; context: [34] In addition, the Applicant cannot seriously contend that he was prevented from making full submissions because he relied on the October 20, 2011 letter to establish residency from 2002 to 2007.

#### 22984:1:subtheme:10 · paragraphs 35-43

- Raw key terms: `applicant, residence, residency, canada, position, review, tribunal, considered`
- Display key terms: `residence, residency, position, review, considered`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: residence, residency, position, review, considered Position/evidence statements: While the Applicant claims to have been informed on the telephone prior to the hearing that such letters are not privileged in administrative proceedings, there does not appear to be any evidence on the record of this co | [36] Finally, the Applicant submits that the position taken by the Review Tribunal is inconsistent, given that it made no findings with respect to other documents marked “without prejudice”. Rule/authority context: [42] The Applicant argued forcefully that the concept of residence under the Income Tax Act, RSC, 1985, c 1 (5th Supp) (ITA), is the not the same and should not be interpreted in the same way as the concept of residence  | [43] The Respondent counters that the concept of residence under the ITA is the same as residence under the OASA, pointing to case law under the ITA that suggests that the material factors to be considered in determining Application context: [37] For all of these reasons, I find that the Review Tribunal did not err in excluding the settlement documents. | He alleges that one may be considered a non-resident for tax purposes while still qualifying as a resident for OAS purposes and, therefore, that the Review Tribunal should have accepted his corrected statements and evide Evidence spans paragraphs 35-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5077472` offsets `658-666`; context: While the Applicant claims to have been informed on the telephone prior to the hearing that such letters are not privileged in administrative proceedings, there does not appear to be any evidence on the record of this conversation, and the Applicant did not claim to have relied on this information once informed at the hearing that the admissibility of the documents was in question.
- Evidence: `party_position` cue `claims` at chunk `5077472` offsets `303-309`; context: While the Applicant claims to have been informed on the telephone prior to the hearing that such letters are not privileged in administrative proceedings, there does not appear to be any evidence on the record of this conversation, and the Applicant did not claim to have relied on this information once informed at the hearing that the admissibility of the documents was in question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077472` offsets `470-478`; context: While the Applicant claims to have been informed on the telephone prior to the hearing that such letters are not privileged in administrative proceedings, there does not appear to be any evidence on the record of this conversation, and the Applicant did not claim to have relied on this information once informed at the hearing that the admissibility of the documents was in question.
- Evidence: `party_position` cue `submits` at chunk `5077473` offsets `28-35`; context: [36] Finally, the Applicant submits that the position taken by the Review Tribunal is inconsistent, given that it made no findings with respect to other documents marked “without prejudice”.
- Evidence: `evidence_fact` cue `found that` at chunk `5077474` offsets `255-265`; context: Had it not found that the settlement offer was privileged, the Review Tribunal would not have been bound to adopt the position expressed in the October 20, 2011 letter, but it would at least have been required to assess and explain why it has come to a different conclusion.
- Evidence: `reasoning_application` cue `I find` at chunk `5077474` offsets `31-37`; context: [37] For all of these reasons, I find that the Review Tribunal did not err in excluding the settlement documents.
- Evidence: `counterargument_limitation` cue `but` at chunk `5077474` offsets `413-416`; context: Had it not found that the settlement offer was privileged, the Review Tribunal would not have been bound to adopt the position expressed in the October 20, 2011 letter, but it would at least have been required to assess and explain why it has come to a different conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5077475` offsets `193-200`; context: In his OAS application, the Applicant claimed not to be a resident between 2002 and the date of his application in 2007, but later explained that these assertions were made in order to protect his more valuable non-resident income tax status.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077475` offsets `613-621`; context: He alleges that one may be considered a non-resident for tax purposes while still qualifying as a resident for OAS purposes and, therefore, that the Review Tribunal should have accepted his corrected statements and evidence demonstrating that he was in fact resident in Canada between 2002 and 2007.
- Evidence: `reasoning_application` cue `therefore` at chunk `5077475` offsets `527-536`; context: He alleges that one may be considered a non-resident for tax purposes while still qualifying as a resident for OAS purposes and, therefore, that the Review Tribunal should have accepted his corrected statements and evidence demonstrating that he was in fact resident in Canada between 2002 and 2007.
- Evidence: `reasoning_application` cue `applied` at chunk `5077476` offsets `93-100`; context: [39] There is generally no dispute between the parties as to the residency requirement to be applied.
- Evidence: `party_position` cue `submitted` at chunk `5077478` offsets `19-28`; context: [41] The Applicant submitted that the Review Tribunal should also have considered subsection 21(4), according to which short absences (less than a year) should be deemed not to interrupt a person’s residency.
- Evidence: `reasoning_application` cue `applies` at chunk `5077478` offsets `357-364`; context: This argument is without merit in light of the position taken by the Review Tribunal, as it is obvious from a plain reading of that section that it applies only where residency has already been established.
- Evidence: `party_position` cue `argued` at chunk `5077479` offsets `19-25`; context: [42] The Applicant argued forcefully that the concept of residence under the Income Tax Act, RSC, 1985, c 1 (5th Supp) (ITA), is the not the same and should not be interpreted in the same way as the concept of residence under the OASA.
- Evidence: `governing_rule` cue `under` at chunk `5077479` offsets `67-72`; context: [42] The Applicant argued forcefully that the concept of residence under the Income Tax Act, RSC, 1985, c 1 (5th Supp) (ITA), is the not the same and should not be interpreted in the same way as the concept of residence under the OASA.
- Evidence: `party_position` cue `argues` at chunk `5077480` offsets `417-423`; context: The Respondent argues that the Applicant cannot have it both ways as an individual cannot be a non-resident of Canada for fiscal purposes, yet be a resident for OAS purposes.
- Evidence: `governing_rule` cue `under` at chunk `5077480` offsets `59-64`; context: [43] The Respondent counters that the concept of residence under the ITA is the same as residence under the OASA, pointing to case law under the ITA that suggests that the material factors to be considered in determining “residence” are the same under both acts (Thomson v Canada (Minister of National Revenue), [1946] SCR 209, [1946] CTC 51 [Thomson]; The Queen v Reeder, 75 DTC 5160 at 5163 (FCTD)).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5077480` offsets `443-449`; context: The Respondent argues that the Applicant cannot have it both ways as an individual cannot be a non-resident of Canada for fiscal purposes, yet be a resident for OAS purposes.

#### 22984:1:subtheme:11 · paragraphs 44-57

- Raw key terms: `canada, residence, justice, canadian, case, described, factors, minister`
- Display key terms: `residence, justice, canadian, case, described, factors`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: residence, justice, canadian, case, described, factors Rule/authority context: In Vegh v R, 2012 TCC 95 at paras 24-29, Justice Boyle considered the law of residence in relation to the ITA, noting the foundational nature of the Thomson decision and beginning his analysis with the following comments | [24] “The legal test of residence has a substantial factual component”: per Sharlow J. Application context: It should therefore be construed liberally, and persons should not be lightly disentitled to OAS benefits. | [31] [The definition in paragraph 21(1)(a)] has been applied to a variety of circumstances. Evidence spans paragraphs 44-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5077481` offsets `1055-1063`; context: The CRA’s Interpretation Bulletin IT-221R3 (Consolidated), “Determination of individual’s residence status” (2002), provides as follows (at para 2):
The term “resident” is not defined in the Income Tax Act (the “Act”), however, the Courts have held “residence” to be “a matter of the degree to which a person in mind and fact settles into or maintains or centralizes his ordinary mode of living with its accessories in social relations, interests and conveniences at or in the place in question.
- Evidence: `governing_rule` cue `legal test` at chunk `5077482` offsets `619-629`; context: In Vegh v R, 2012 TCC 95 at paras 24-29, Justice Boyle considered the law of residence in relation to the ITA, noting the foundational nature of the Thomson decision and beginning his analysis with the following comments regarding the factual nature of legal test:
- Evidence: `governing_rule` cue `legal test` at chunk `5077483` offsets `10-20`; context: [24] “The legal test of residence has a substantial factual component”: per Sharlow J.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5077485` offsets `104-115`; context: [23] The object of the Act and of various reciprocal agreements entered into by the Canadian Government pursuant to section 40 of the Act were ably described by Justice Judith A.
- Evidence: `reasoning_application` cue `therefore` at chunk `5077486` offsets `401-410`; context: It should therefore be construed liberally, and persons should not be lightly disentitled to OAS benefits.
- Evidence: `governing_rule` cue `principles` at chunk `5077489` offsets `15-25`; context: [25] Thus, new principles were introduced in the Act.
- Evidence: `governing_rule` cue `legal test` at chunk `5077490` offsets `9-19`; context: [47] The legal test for residency is described at paragraphs 30-37 of Singer, which include the following key excerpts:
- Evidence: `reasoning_application` cue `applied` at chunk `5077491` offsets `53-60`; context: [31] [The definition in paragraph 21(1)(a)] has been applied to a variety of circumstances.
- Evidence: `evidence_fact` cue `determined that` at chunk `5077493` offsets `529-544`; context: Minister of Human Resources Development (December 19, 2003), the RT determined that the appellant's Canadian residence began on the day she formalized her intention by applying for permanent residence.
- Evidence: `reasoning_application` cue `applied` at chunk `5077494` offsets `241-248`; context: Sometime the fact that a person has obtained or applied for a permanent status will be relevant while in others it will not.

#### 22984:1:subtheme:12 · paragraphs 58-59

- Raw key terms: `above, claimant, context, factual, residence, acts, always, analysis`
- Display key terms: `above, context, factual, residence, acts, always, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: above, context, factual, residence, acts, always, analysis Position/evidence statements: [48] In the final analysis, I think that the common law definition of residence is relevant to consideration of the term under both the OASA and the ITA and, thus, that the Respondent is correct to assert that the materi Rule/authority context: [48] In the final analysis, I think that the common law definition of residence is relevant to consideration of the term under both the OASA and the ITA and, thus, that the Respondent is correct to assert that the materi Evidence spans paragraphs 58-59. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5077495` offsets `562-570`; context: That said, as stressed in Thomson and Singer, above, the meaning of the term may vary not only in the contexts of different matters, but also in different aspects of the same matter, and one must be wary of precedent, such that the context of the act in question as well as a claimant’s specific factual circumstances must always be kept in mind.
- Evidence: `party_position` cue `assert` at chunk `5077495` offsets `198-204`; context: [48] In the final analysis, I think that the common law definition of residence is relevant to consideration of the term under both the OASA and the ITA and, thus, that the Respondent is correct to assert that the material factors to be considered in determining “residence” may be the same under both acts.
- Evidence: `governing_rule` cue `under` at chunk `5077495` offsets `121-126`; context: [48] In the final analysis, I think that the common law definition of residence is relevant to consideration of the term under both the OASA and the ITA and, thus, that the Respondent is correct to assert that the material factors to be considered in determining “residence” may be the same under both acts.
- Evidence: `issue` cue `issues` at chunk `5077496` offsets `434-440`; context: In that regard, Justice Russell found that “considerable care has been taken to distinguish between a change of “domicile” (which depends upon the will of the individual) and a change of “residence” which depends upon factual issues that are external to the individual[’]s intentions” (para 57).
- Evidence: `evidence_fact` cue `found that` at chunk `5077496` offsets `240-250`; context: In that regard, Justice Russell found that “considerable care has been taken to distinguish between a change of “domicile” (which depends upon the will of the individual) and a change of “residence” which depends upon factual issues that are external to the individual[’]s intentions” (para 57).

#### 22984:1:subtheme:13 · paragraphs 60-61

- Raw key terms: `canada, domicile, establish, even, factual, individual, ordinarily, paragraph`
- Display key terms: `domicile, establish, even, factual, individual, ordinarily, paragraph`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: domicile, establish, even, factual, individual, ordinarily, paragraph Rule/authority context: The wording of paragraph 21(1)(a) of the OAS Regulations makes the factual component of the definition of residence under the OASA even clearer. Application context: [50] Justice Russell goes on to conclude that residency is a factual issue that requires an examination of the whole context of the individual and that it constitutes a reviewable error to focus on a claimant’s “obvious  Evidence spans paragraphs 60-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077497` offsets `69-74`; context: [50] Justice Russell goes on to conclude that residency is a factual issue that requires an examination of the whole context of the individual and that it constitutes a reviewable error to focus on a claimant’s “obvious intentions” to the exclusion of other factors in a case that could lead to a contrary conclusion.
- Evidence: `reasoning_application` cue `conclude` at chunk `5077497` offsets `32-40`; context: [50] Justice Russell goes on to conclude that residency is a factual issue that requires an examination of the whole context of the individual and that it constitutes a reviewable error to focus on a claimant’s “obvious intentions” to the exclusion of other factors in a case that could lead to a contrary conclusion.
- Evidence: `counterargument_limitation` cue `although` at chunk `5077497` offsets `1071-1079`; context: The length of stay or the time present within the jurisdiction, although an element, is not always conclusive.
- Evidence: `governing_rule` cue `under` at chunk `5077498` offsets `284-289`; context: The wording of paragraph 21(1)(a) of the OAS Regulations makes the factual component of the definition of residence under the OASA even clearer.

#### 22984:1:subtheme:14 · paragraphs 62-64

- Raw key terms: `applicant, application, canada, decision, residency, resident, review, stated`
- Display key terms: `residency, resident, review, stated`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: residency, resident, review, stated Position/evidence statements: [53] Although the Review Tribunal lists various documents and pieces of evidence submitted by the Applicant in support of his claim, it in no way engages with that evidence in its decision. Rule/authority context: A careful review of the decision reveals that, while citing the proper test and even noting that the Applicant’s intention to resume his residency in Canada in 2002 cannot be considered determinative of residency under t Operative outcome context: It is not to be denied that the Review Tribunal placed significant weight on the Applicant’s OAS application as probative evidence of the Applicant’s mindset that he was not a resident of Canada at the time of applicatio | Lone comments regarding a “pattern of late and over due payments of invoices since 2002” and the fact that the Applicant spends time in each of England, Spain and Canada constitute the only references to the “patchwork o Evidence spans paragraphs 62-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077499` offsets `701-706`; context: In particular, it stated that in Ding this Court “found that the determination of residency is a factual issue that requires an examination of the whole context of the individual” (Review Tribunal decision, para 43).
- Evidence: `evidence_fact` cue `evidence` at chunk `5077499` offsets `370-378`; context: It is not to be denied that the Review Tribunal placed significant weight on the Applicant’s OAS application as probative evidence of the Applicant’s mindset that he was not a resident of Canada at the time of application.
- Evidence: `counterargument_limitation` cue `however` at chunk `5077499` offsets `501-508`; context: It is clear from the reasons, however, that the Review Tribunal was aware of the relevant case law and the appropriate test.
- Evidence: `disposition` cue `denied` at chunk `5077499` offsets `264-270`; context: It is not to be denied that the Review Tribunal placed significant weight on the Applicant’s OAS application as probative evidence of the Applicant’s mindset that he was not a resident of Canada at the time of application.
- Evidence: `party_position` cue `submitted` at chunk `5077500` offsets `81-90`; context: [53] Although the Review Tribunal lists various documents and pieces of evidence submitted by the Applicant in support of his claim, it in no way engages with that evidence in its decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077500` offsets `72-80`; context: [53] Although the Review Tribunal lists various documents and pieces of evidence submitted by the Applicant in support of his claim, it in no way engages with that evidence in its decision.
- Evidence: `governing_rule` cue `under` at chunk `5077500` offsets `690-695`; context: A careful review of the decision reveals that, while citing the proper test and even noting that the Applicant’s intention to resume his residency in Canada in 2002 cannot be considered determinative of residency under the OASA (Decision, para 46), the Review Tribunal goes on to rely entirely on the Applicant’s (allegedly erroneous) statements that he did not intend to become a resident, as stated in his OAS application and various other communications with government.
- Evidence: `disposition` cue `dismissed` at chunk `5077500` offsets `1183-1192`; context: Lone comments regarding a “pattern of late and over due payments of invoices since 2002” and the fact that the Applicant spends time in each of England, Spain and Canada constitute the only references to the “patchwork of evidence” dismissed by the Review Tribunal, apart from the annotated but non-exhaustive lists of the evidence reviewed.
- Evidence: `evidence_fact` cue `record` at chunk `5077501` offsets `849-855`; context: In addition, their statement that the application sets out indicia showing not only that he did not intend to reside but that he didn’t reside in Canada is unsupported in the reasons and cryptic in light of the evidentiary record.
- Evidence: `counterargument_limitation` cue `but` at chunk `5077501` offsets `743-746`; context: In addition, their statement that the application sets out indicia showing not only that he did not intend to reside but that he didn’t reside in Canada is unsupported in the reasons and cryptic in light of the evidentiary record.

#### 22984:1:subtheme:15 · paragraphs 65-66

- Raw key terms: `applicant, conclusion, considered, context, contrary, despite, ding, error`
- Display key terms: `conclusion, considered, context, contrary, despite, ding, error`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: conclusion, considered, context, contrary, despite, ding, error Position/evidence statements: [55] The Review Tribunal’s statement at paragraph 56 of its reasons that the excerpts from the OAS application represent “an admission of the Appellant himself that he did not intend, nor did he submit that he was a resi Application context: While this was considered a reviewable error in Ding, the Review Tribunal properly cites and states that it is aware of the test to be applied. Evidence spans paragraphs 65-66. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5077502` offsets `781-786`; context: Secondly, as accepted by the Review Tribunal itself, the Applicant’s intention or mindset is not determinative of the issue of residency and, despite claiming that it has examined the whole context of the Applicant by applying Ding, the Review Tribunal risks committing the exact error described in that case by focusing its reasons on the “obvious intentions” of the Applicant to the exclusion of other factors in the case that, if considered, could arguably lead to a contrary conclusion.
- Evidence: `party_position` cue `submit` at chunk `5077502` offsets `195-201`; context: [55] The Review Tribunal’s statement at paragraph 56 of its reasons that the excerpts from the OAS application represent “an admission of the Appellant himself that he did not intend, nor did he submit that he was a resident of Canada from April 4, 2002 onwards” is problematic in two respects.
- Evidence: `evidence_fact` cue `determined that` at chunk `5077502` offsets `537-552`; context: According to the Applicant, once he determined that he did not need to protect his tax status, he has consistently submitted that he was a resident from 2002 on.
- Evidence: `issue` cue `whether` at chunk `5077503` offsets `690-697`; context: Nevertheless, even if it is assumed that the Review Tribunal properly applied the test for determining residency, its reasons are insufficient to permit this Court, not to mention the Applicant, to understand why it made its decision or to determine whether its conclusion is within the range of acceptable outcomes.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077503` offsets `245-253`; context: [56] Despite the Review Tribunal’s assertions that it has examined the whole context of the Applicant, its reasons suggest that it has based its decision on the Applicant’s “obvious intentions” to the potential exclusion of other factors in the evidence that could lead to a contrary conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5077503` offsets `431-438`; context: While this was considered a reviewable error in Ding, the Review Tribunal properly cites and states that it is aware of the test to be applied.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5077503` offsets `440-452`; context: Nevertheless, even if it is assumed that the Review Tribunal properly applied the test for determining residency, its reasons are insufficient to permit this Court, not to mention the Applicant, to understand why it made its decision or to determine whether its conclusion is within the range of acceptable outcomes.

#### 22984:1:subtheme:16 · paragraphs 67-69

- Raw key terms: `allowed, applicant, application, canada, contribute, economy, establish, evidence`
- Display key terms: `allowed, contribute, economy, establish`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: allowed, contribute, economy, establish Position/evidence statements: Had proper reasons been provided, the Review Tribunal’s conclusion might be justifiable, as it is far from clear that the voluminous documentary evidence submitted by the Applicant should be considered sufficient or of t Rule/authority context: [58] Despite this finding, I agree with the Respondent that the Applicant likely cannot have it both ways and, given the similarities in the tests for residency under the ITA and the OASA, in the event that he were succe Application context: Without prejudging the ultimate outcome, however, I find that the reasons provided are insufficient to permit me to assess whether the Review Tribunal’s conclusion falls within the range of acceptable outcomes which are  Operative outcome context: For this reason, I find that the application for judicial review should be allowed. | JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is allowed, without costs. Evidence spans paragraphs 67-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5077504` offsets `535-542`; context: Without prejudging the ultimate outcome, however, I find that the reasons provided are insufficient to permit me to assess whether the Review Tribunal’s conclusion falls within the range of acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `party_position` cue `submitted` at chunk `5077504` offsets `301-310`; context: Had proper reasons been provided, the Review Tribunal’s conclusion might be justifiable, as it is far from clear that the voluminous documentary evidence submitted by the Applicant should be considered sufficient or of the quality necessary to establish residence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5077504` offsets `292-300`; context: Had proper reasons been provided, the Review Tribunal’s conclusion might be justifiable, as it is far from clear that the voluminous documentary evidence submitted by the Applicant should be considered sufficient or of the quality necessary to establish residence.
- Evidence: `reasoning_application` cue `I find` at chunk `5077504` offsets `462-468`; context: Without prejudging the ultimate outcome, however, I find that the reasons provided are insufficient to permit me to assess whether the Review Tribunal’s conclusion falls within the range of acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `counterargument_limitation` cue `however` at chunk `5077504` offsets `453-460`; context: Without prejudging the ultimate outcome, however, I find that the reasons provided are insufficient to permit me to assess whether the Review Tribunal’s conclusion falls within the range of acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `disposition` cue `allowed` at chunk `5077504` offsets `751-758`; context: For this reason, I find that the application for judicial review should be allowed.
- Evidence: `evidence_fact` cue `RECORD` at chunk `5077505` offsets `1092-1098`; context: "Yves de Montigny"
Judge
FEDERAL COURT
SOLICITORS OF RECORD
DOCKET: T-453-12
STYLE OF CAUSE: ROGER J.
- Evidence: `governing_rule` cue `under` at chunk `5077505` offsets `161-166`; context: [58] Despite this finding, I agree with the Respondent that the Applicant likely cannot have it both ways and, given the similarities in the tests for residency under the ITA and the OASA, in the event that he were successful in establishing residency before the Review Tribunal, he may put at risk what he has described as his more valuable tax position.
- Evidence: `disposition` cue `allowed` at chunk `5077505` offsets `1015-1022`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is allowed, without costs.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5077506` offsets `83-91`; context: [1] Footnote 8 of Singer here provides as follows: “See Minutes of Proceedings and Evidence of the Standing Committee on Health, Welfare and Social Affairs, No.

#### Section text

Duncan v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2013-03-27
Neutral citation
2013 FC 319
File numbers
T-453-12
Notes
Digest
Decision Content
Date: 20130327
Docket: T-453-12
Citation: 2013 FC 319
Ottawa, Ontario, March 27, 2013
PRESENT: The Honourable Mr. Justice de Montigny
BETWEEN:
ROGER J. DUNCAN
Applicant
and
THE ATTORNEY GENERAL OF CANADA
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision by the Office of the Commissioner of Review Tribunals (the “Review Tribunal” or the “OCRT”), finding Mr. Roger J. Duncan (the “Applicant”) to be ineligible for an Old Age Security (OAS) pension, whether full or partial.

[2] For the reasons that follow, I find that the application for judicial review should be granted.

[3] As a preliminary matter, it is to be noted that the Applicant, who was self-represented, improperly named the Respondent. Pursuant to subsections 303(1) and (2) of the Federal Courts Rules, SOR/98-106, the Attorney General of Canada is the properly named Respondent in this matter, and shall replace the Minister of Human Resources and Skills Development (the “Minister”) in that capacity.
1. Background

[4] The Applicant was born in England on March 19, 1943, and is now 70 years of age. He immigrated to Canada in 1966 and was admitted as a lawyer in the province of British Columbia in 1969, becoming a Canadian citizen in 1972. From 1984 until 2002, the Applicant returned to England in order to practice law, having lost his job in Canada. In 2002, the Applicant resigned his law partnership in England and claims to have left his London home in order to accept a full-time consultancy position with a Vancouver-based law firm. After a one-year period working as a consultant, the Applicant started his own law practice in 2003 (splitting his time between England and British Columbia on an approximately quarterly basis) and ultimately retired in 2007. The Applicant owns part-time residences in each of Canada, England, France and Spain. Since retiring, he has travelled and intends to travel extensively, splitting his time between the four part-time homes. Mr. Duncan claims to be in need of his OAS pension, despite appearing to have significant worldwide investments, and affirms that he would not be subject to the OAS recovery tax.

[5] The Applicant applied for an OAS pension on September 6, 2007. In the section of the application addressing “residence history”, the Applicant indicated that he lived in Canada from December 30, 1966 to August 20, 1984, that he was a full-time resident of England from August 21, 1984 until February 22, 2002, and that he was a part-time resident of England from April 4, 2002 until the date of his application. In the section of the application requesting the Applicant’s “home address”, he provided an English address. The Applicant signed his OAS application and declared the information to be true and complete.

[6] In a letter received by Human Resources and Social Development (“HRSDC”) on February 6, 2008, the Applicant attached a completed “residence questionnaire”, dated January 25, 2008. In a question addressing CPP contributions between the years 2002 and 2004, the Applicant responded as follows: “Not paid but claimed by CRA. As above I was not ‘living’ in Canada 02-Date but was a part-time non-resident sojourner” (Respondent’s Record, Volume 1, Tab 2, p. 86).

[7] Similar affirmations were made in two other submissions to the government, both dated 2006, asserting that the Applicant was not a resident of Canada from 2002 until at least 2006. In his CRA Determination of Residency Status form, dated 12/5/06, the Applicant indicated that he “sojourn[ed] in Canada as a Canadian citizen staying for short stays as a non-resident and also in England and Spain”, was “not resident in Canada full-time or England or Spain, but [would] travel/sojourn to each”, and was involved in “part-time legal [handwriting unclear] work occasionally when in BC when & if I get any” (Respondent’s Record, Volume 1, Tab 2, pp. 78-81). In a letter to the Client Services Division, International Tax Services, dated 11/7/06, the Applicant claimed: “I am not at present ‘living’ or ‘resident’ in any country. […] Accordingly, I did not again become a ‘resident’ of Canada, factual or otherwise, in 2002 merely by my 9 months’ consultancy stay, but was only a visitor […]” (Respondent’s Record, Volume 1, Tab 2, p. 82).

[8] By letter dated February 12, 2008, the Applicant was informed that the information provided in his application indicated that he had resided in Canada for 17 years and 235 days. To qualify for a pension he would need to change his principal country of residence to Canada, taking all steps to establish a permanent residence. For these reasons, his application was denied.

[9] By letter dated August 6, 2008, the Applicant requested a reconsideration of the decision to deny him OAS benefits. In his request for reconsideration to the Regional Director of Human Resources and Social Development, the Applicant submitted that he made a number of errors in his initial application, including: (i) listing his English address instead of his Vancouver address; (ii) listing that he was a part-time resident of England instead of a part-time resident of Vancouver from 2002 to the date of application (September 6, 2007), having allegedly missed a note instructing him to disregard ‘periods when you were outside Canada for less than six months at a time’; and (iii) listing that he ‘live[d] permanently outside Canada’, when he claims to have in fact lived part-time in British Columbia and part-time (but not permanently) in England. With respect to the residence questionnaire (dated January 25, 2008), he submits that he correctly stated his ‘part-time non-(full-time) resident sojourner’ status in response to question 10.

[10] After several requests for further information, which the Applicant provided, he was informed by letter dated September 29, 2009 that the initial decision to deny his application for OAS benefits had been maintained, as he did not fully meet the residence requirements of the Old Age Security Act, RSC 1985, c O-9 (the “OASA” or the “Act”). By letter dated November 12, 2009, the Applicant advised the OCRT that he wished to appeal the Minister’s decision of September 29, 2009.

[11] A Review Tribunal hearing was convened on June 14, 2011 in Vancouver. The hearing was adjourned to allow the Applicant additional time to submit further documentation.

[12] By letter dated October 20, 2011, and marked “without prejudice”, HRSDC informed the Applicant that, following a review of the additional information provided since June 2011, it had determined that he did meet the residence requirements under the OASA. The Applicant was informed that although his passports confirm several absences from Canada from May 16, 2006 onwards, HRSDC calculated his Canadian residence from April 3, 2002 to September 10, 2007. As a result he was entitled to a partial pension of 23/40ths, effective April 2008 (Respondent’s Record, Volume II, p. 691).

[13] By letter dated October 26, 2011, and marked “without prejudice”, the Applicant informed the Respondent that he did not wish to accept the settlement offer of a partial OAS pension. The Applicant requested that the Respondent reconsider its decision and amend the offer to reflect a full OAS pension (Respondent’s Record, Volume III, p. 687).

[14] A second Review Tribunal was convened on November 9, 2011, in Vancouver. On February 1, 2012, the Review Tribunal dismissed the Applicant’s appeal. It is this decision that is the subject matter of this proceeding.
2. Decision under review

[15] As noted above, the Review Tribunal found the Applicant to be ineligible to receive either a full or partial OAS pension pursuant to section 3 of the OASA. The decision notes that the appeal hearing was adjourned at the Applicant’s request on June 14, 2011, in order to permit him to submit further documentary evidence regarding his Canadian residency.

[16] The Review Tribunal dealt with two preliminary matters: (i) finding, after receiving oral submissions from the parties and upon careful consideration, that a “without prejudice” settlement letter from the Minister to the Applicant, dated October 20, 2011, and reply dated October 26, 2011, are not relevant to the establishment of the Applicant’s Canadian residency for the period of April 4, 2002 to March 19, 2008 (the “Relevant Period”); and (ii) accepting as admissible certain insurance records filed by the Applicant after the close of his appeal hearing.

[17] The only issue on appeal before the Review Tribunal was a determination of the Applicant’s duration and periods of residency in Canada for the purposes of determining whether he should be entitled to receive a full or partial OAS pension or no pension at all.

[18] The Review Tribunal surveyed a number of statements suggesting that the Applicant was not resident and did not consider himself to be resident in Canada during the Relevant Period, as well as the documentation and other evidence put forward by the Applicant in support of what he now alleges to be “part-time residence in Canada from 2002 to 2008”.

[19] The Review Tribunal considered the parties’ submissions and the eligibility requirements for full and partial OAS benefits under subsections 3(1) and (2) of the OASA, as well as under subsection 21(1) of the Old Age Security Regulations, CRC, c 1246 (the “OAS Regulations”), finding that the two periods of time relevant to determining the Appellant’s residency in Canada are: (i) April 4, 2002 to March 19, 2007; and (ii) March 20, 2007 to March 19, 2008.

[20] Ultimately, the Review Tribunal found that, upon weighing all of the evidence and examining the whole context of the individual, the Applicant did not intend to reside and did not reside in Canada as required under the OASA and the OAS Regulations during the two relevant time periods. On a balance of probabilities, the Review Tribunal concluded that the Applicant was last a resident of Canada for the purposes of OAS benefits eligibility on August 20, 1984. Accepting that the Applicant had been resident in Canada for a total of 17 years and 235 days between 1966 and 1984, this was insufficient to meet the requirements for either full or partial OAS benefits.

[21] The Review Tribunal placed significant weight on the statements in the Applicant’s OAS application suggesting that he did not consider himself a resident during the Relevant Period and found that “[w]hile the [Applicant] has testified that in fact he filled in the OAS Application incorrectly, it does not follow that he can retroactively revise or amend that application at the time of the appeal hearing” (Review Tribunal Decision, para 57). The Review Tribunal emphasized the probative value of the application, finding that it “evidence[d] the [Applicant’s] mindset at the time of the OAS Application submission, that he was visitor, a part-time sojourner, to Canada from April 4, 2002 onwards” (Review Tribunal Decision, para 58).

[22] The Review Tribunal also emphasized the insufficiency of the “patchwork of evidence filed” by the Applicant for the Relevant Period, and noted that a “pattern of late and over due payments of invoices since 2002” suggested absence, rather than assisting in establishing residency. The Review Tribunal wrote: “If one makes their home and ordinarily lives in Canada one would be reasonably expected to pay bills and statements of account on a regular basis” (Review Tribunal Decision, para 62).
3. Issues

[23] Having reviewed the materials and submissions of both parties, I am of the view that the following questions must be determined:
i) What is the applicable standard of review?
ii) Did the exclusion of the settlement letter and reply between the Minister and the Applicant constitute a breach of procedural fairness?
iii) Was the Review Tribunal’s decision reasonable?
4. Analysis
- The legislative framework

[24] The general requirement for a full OAS pension as set out in paragraph 3(1)(c) of the OASA is to have accumulated 40 years of residence in Canada after the age of 18. However, paragraph 3(1)(b) of the OASA sets out the criteria to be met in order for an individual to qualify for a full OAS pension without having 40 years of residence. It provides as follows:
MONTHLY PENSION
Pension Payable Payment of full pension 3. (1) Subject to this Act and the regulations, a full monthly pension may be paid to
[…]
(b) every person who
(i) on July 1, 1977 was not a pensioner but had attained twenty-five years of age and resided in Canada or, if that person did not reside in Canada, had resided in Canada for any period after attaining eighteen years of age or possessed a valid immigration visa,
(ii) has attained sixty-five years of age, and
(iii) has resided in Canada for the ten years immediately preceding the day on which that person’s application is approved or, if that person has not so resided, has, after attaining eighteen years of age, been present in Canada prior to those ten years for an aggregate period at least equal to three times the aggregate periods of absence from Canada during those ten years, and has resided in Canada for at least one year immediately preceding the day on which that person’s application is approved; and
[…]
PENSIONS
Ayants droit Pleine pension 3. (1) Sous réserve des autres dispositions de la présente loi et de ses règlements, la pleine pension est payable aux personnes suivantes :
…
b) celles qui, à la fois :
(i) sans être pensionnées au 1er juillet 1977, avaient alors au moins vingt-cinq ans et résidaient au Canada ou y avaient déjà résidé après l’âge de dix-huit ans, ou encore étaient titulaires d’un visa d’immigrant valide,
(ii) ont au moins soixante-cinq ans,
(iii) ont résidé au Canada pendant les dix ans précédant la date d’agrément de leur demande, ou ont, après l’âge de dix-huit ans, été présentes au Canada, avant ces dix ans, pendant au moins le triple des périodes d’absence du Canada au cours de ces dix ans tout en résidant au Canada pendant au moins l’année qui précède la date d’agrément de leur demande;
…

[25] If an individual cannot qualify for a full OAS pension, he or she may qualify for a partial pension under subsection 3(2) of the OASA. For a partial pension, the individual must have resided in Canada for at least 10 years and must have been a resident on the day preceding the day on which the application is approved. If the individual did not reside in Canada on the day preceding the day on which the application is approved, the individual must have resided in Canada for at least 20 years. Subsections 3(2) to 3(5) provide as follows:
MONTHLY PENSION
Pension Payable Payment of partial pension 3. (2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person’s application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person’s application is approved.
Amount of partial pension
(3) The amount of a partial monthly pension, for any month, shall bear the same relation to the full monthly pension for that month as the aggregate period that the applicant has resided in Canada after attaining eighteen years of age and prior to the day on which the application is approved, determined in accordance with subsection (4), bears to forty years.
Rounding of aggregate period
(4) For the purpose of calculating the amount of a partial monthly pension under subsection (3), the aggregate period described in that subsection shall be rounded to the lower multiple of a year when it is not a multiple of a year.
Additional residence irrelevant for partial pensioner
(5) Once a person’s application for a partial monthly pension has been approved, the amount of monthly pension payable to that person under this Part may not be increased on the basis of subsequent periods of residence in Canada.
PENSIONS
Ayants droit Pension partielle 3. (2) Sous réserve des autres dispositions de la présente loi et de ses règlements, une pension partielle est payable aux personnes qui ne peuvent bénéficier de la pleine pension et qui, à la fois :
a) ont au moins soixante-cinq ans;
b) ont, après l’âge de dix-huit ans, résidé en tout au Canada pendant au moins dix ans mais moins de quarante ans avant la date d’agrément de leur demande et, si la période totale de résidence est inférieure à vingt ans, résidaient au Canada le jour précédant la date d’agrément de leur demande.
Montant
(3) Pour un mois donné, le montant de la pension partielle correspond aux n/40 de la pension complète, n étant le nombre total — arrondi conformément au paragraphe (4) — d’années de résidence au Canada depuis le dix-huitième anniversaire de naissance jusqu’à la date d’agrément de la demande.
Arrondissement
(4) Le nombre total d’années de résidence au Canada est arrondi au chiffre inférieur.
Résidence ultérieure
(5) Les années de résidence postérieures à l’agrément d’une demande de pension partielle ne peuvent influer sur le montant de celle-ci.

[26] For individuals who have already established residence in Canada, subsection 21(4) of the OAS Regulations protects their residence by ensuring that temporary absences from the country do not interrupt their period of residence:
Residence
21. (4) Any interval of absence from Canada of a person resident in Canada that is
(a) of a temporary nature and does not exceed one year,
(b) for the purpose of attending a school or university, or
(c) specified in subsection (5)
shall be deemed not to have interrupted that person’s residence or presence in Canada.
Résidence
21. (4) Lorsqu’une personne qui réside au Canada s’absente du Canada et que son absence
a) est temporaire et ne dépasse pas un an,
b) a pour motif la fréquentation d’une école ou d’une université, ou
c) compte parmi les absences mentionnées au paragraphe (5),
cette absence est réputée n’avoir pas interrompu la résidence ou la présence de cette personne au Canada.

[27] Finally, subsection 21(1) of the OAS Regulations explains the difference between “residence” and “presence” for purposes of OAS eligibility. It states:
Residence
21. (1) For the purposes of the Act and these Regulations,
(a) a person resides in Canada if he makes his home and ordinarily lives in any part of Canada; and
(b) a person is present in Canada when he is physically present in any part of Canada.
[…]
Résidence
21. (1) Aux fins de la Loi et du présent règlement,
a) une personne réside au Canada si elle établit sa demeure et vit ordinairement dans une région du Canada; et
b) une personne est présente au Canada lorsqu’elle se trouve physiquement dans une région du Canada.
…
i) What is the applicable standard of review?

[28] It has been decided on several occasions, both pre- and post-Dunsmuir that the issue of residence is a question of mixed fact and law that is more factually than legally driven and is therefore reviewable on a reasonableness standard, save and except where the critical issue is the proper legal test to be applied for determining residency (which is not the case here): see Canada (Minister of Human Resources Development) v Ding, 2005 FC 76 [Ding] at paras 58-60; Canada (Minister of Human Resources Development) v Chhabu, 2005 FC 1277 at paras 23-24; Kiefer v Canada (Attorney General), 2008 FC 786 at paras 20-21; de Bustamante v Canada (Attorney General), 2008 FC 1111 at paras 33-34; Singer v Canada (Attorney General), 2010 FC 607 at para

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]

