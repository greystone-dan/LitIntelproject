# Discussion Units: case 22283

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **29**
- Continuity pairs: **28**
- Discussion Units: **5**
- Paragraph source hashes: **29**
- Sub-themes: **10**

## 22283:1 · paragraphs 0-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a6822655f77558d7e13e6ec6789d8c2e8f1fc794e30b736e32230f539215ca6d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22283:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, decision, protection, because, board, canada, chinese, christian`
- Display key terms: `protection, because, chinese, christian`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: protection, because, chinese, christian Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated March 20, 2009 concluding that the applicant, a Chinese citizen, is n | Decision under review Application context: 27 because of his Christian religion. | On September 16, 2007 the applicant sought protection because of a well founded fear of persecution for his Christian religious beliefs. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5045748` offsets `278-289`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated March 20, 2009 concluding that the applicant, a Chinese citizen, is not a Convention refugee or a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `because` at chunk `5045748` offsets `373-380`; context: 27 because of his Christian religion.
- Evidence: `governing_rule` cue `under` at chunk `5045749` offsets `1082-1087`; context: Decision under review
- Evidence: `reasoning_application` cue `because` at chunk `5045749` offsets `908-915`; context: On September 16, 2007 the applicant sought protection because of a well founded fear of persecution for his Christian religious beliefs.

#### 22283:1:subtheme:2 · paragraphs 4-10

- Raw key terms: `applicant, board, bible, christian, held, christianity, knowledge, testimony`
- Display key terms: `bible, christian, christianity, knowledge, testimony`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: bible, christian, christianity, knowledge, testimony Application context: [8] The Board assigned little weight to a support letter from the applicant’s Church because it lacked details on the applicant’s involvement with the Church. Evidence spans paragraphs 4-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5045751` offsets `20-27`; context: [4] With respect to whether the applicant is a genuine Christian, the Board noted that according to the applicant’s testimony the applicant has been exposed to Christianity for about two years and was presently reading the Bible every day.
- Evidence: `evidence_fact` cue `testimony` at chunk `5045751` offsets `116-125`; context: [4] With respect to whether the applicant is a genuine Christian, the Board noted that according to the applicant’s testimony the applicant has been exposed to Christianity for about two years and was presently reading the Bible every day.
- Evidence: `counterargument_limitation` cue `However` at chunk `5045753` offsets `617-624`; context: However, the applicant also added “love everybody like yourself and read the bible”, which the Board held was an incorrect answer.
- Evidence: `evidence_fact` cue `testimony` at chunk `5045754` offsets `261-270`; context: The applicant’s failure to attend bible study, the internal inconsistencies in the applicant’s testimony, and the inconsistencies between his testimony and his PIF were also cited as reasons for the Board negative credibility finding.
- Evidence: `reasoning_application` cue `because` at chunk `5045755` offsets `85-92`; context: [8] The Board assigned little weight to a support letter from the applicant’s Church because it lacked details on the applicant’s involvement with the Church.
- Evidence: `evidence_fact` cue `testimony` at chunk `5045757` offsets `41-50`; context: [10] The Board held that the applicant’s testimony was not trustworthy and without credibility.

#### 22283:1:subtheme:3 · paragraphs 11-11

- Raw key terms: `applicant, aspect, based, board, claim, conceded, contradictory, decided`
- Display key terms: `aspect, based, conceded, contradictory, decided`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: aspect, based, conceded, contradictory, decided Evidence spans paragraphs 11-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5045758` offsets `307-313`; context: ISSUES
- Evidence: `evidence_fact` cue `evidence` at chunk `5045758` offsets `261-269`; context: The applicant conceded at the outset of the hearing that his latter finding was reasonably open to the Board based on the applicant’s inconsistent and contradictory evidence on this seminal aspect of his claim.

#### Section text

Wu v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-09-17
Neutral citation
2009 FC 929
File numbers
IMM-664-09
Decision Content
Federal Court
Cour fédérale
Date: 20090917
Docket: IMM-664-09
Citation: 2009 FC 929
Toronto, Ontario, September 17, 2009
PRESENT: The Honourable Mr. Justice Kelen
BETWEEN:
PENGHUI WU
Applicant
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated March 20, 2009 concluding that the applicant, a Chinese citizen, is not a Convention refugee or a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 because of his Christian religion.
FACTS

[2] The forty nine (49) year old applicant is a farmer with nine (9) years of formal education from China. The applicant is married with one child. To deal with his mother’s onset of terminal illness, the applicant allegedly converted to Christianity with the assistance of a friend who was involved with an underground Christian Church. The applicant arrived in Canada on June 29, 2007 on visitor’s visa to visit his ailing mother. During his stay, the applicant allegedly learned from his wife that on September 9, 2007 Chinese authorities, specifically the Public Safety Bureau (PSB), were looking for him and requested that the applicant’s wife contact the applicant and persuade him to return to China. The applicant allegedly learned the next day that apart from visiting his house, the PSB raided his underground church and arrested three people. On September 16, 2007 the applicant sought protection because of a well founded fear of persecution for his Christian religious beliefs. The applicant stated he has been attending the London Alliance Church since then.
Decision under review

[3] On March 20, 2009 the Board held that the applicant was not a Convention refugee or a person in need protection.

[4] With respect to whether the applicant is a genuine Christian, the Board noted that according to the applicant’s testimony the applicant has been exposed to Christianity for about two years and was presently reading the Bible every day.

[5] The Board held that the level of knowledge of Christianity the applicant possessed was not consistent with almost two years of exposure to the Bible, Christian doctrine, and practice, even when his relative lack of sophistication was considered.

[6] The Board made the following determinations with respect to the applicant’s lack of Christian knowledge at page 8 of its reasons:
1. The applicant could not state one of the three basic teachings of Jesus. Instead he recited two (2) of the Ten Commandments.
2. The applicant named the wrong book of his favourite verse which he marked in his book.
3. The applicant was unable to say anything about his favourite verse except that if you believe in Jesus you will be saved.
4. When asked about Jesus’ position on wealth, the applicant stated a partially correct answer, “take it to heaven so nobody can steal it”. However, the applicant also added “love everybody like yourself and read the bible”, which the Board held was an incorrect answer.
5. The applicant knew that Jesus’ disciples wrote the books in the New Testament, but he was unable to name a single disciple.
6. The applicant was unable to name any of the eight Teachings on the Mount.
7. Although familiar with King David, when asked what book was written by King David, the applicant erroneously stated the “New Testament”.
8. The applicant was not able to name the two special observances of the London Alliance Church until prompted or being suggested the answer.

[7] The Board appears to have drawn an adverse inference from the applicant’s quick answering to counsel’s questions where he provided the names of the four Gospels. The applicant’s failure to attend bible study, the internal inconsistencies in the applicant’s testimony, and the inconsistencies between his testimony and his PIF were also cited as reasons for the Board negative credibility finding.

[8] The Board assigned little weight to a support letter from the applicant’s Church because it lacked details on the applicant’s involvement with the Church.

[9] The Board held that the applicant’s history of attempted admission to Canada since 1995 indicates a strong desire to come and stay in Canada.

[10] The Board held that the applicant’s testimony was not trustworthy and without credibility. The Board held that the applicant is not and never was a genuine Christian believer and that any religious activities the applicant participated in and any knowledge of Christianity that the applicant displayed was acquired for the purpose of making his refugee claim.

[11] The Board also decided that the applicant’s story of being wanted by the PSB was not true. The applicant conceded at the outset of the hearing that his latter finding was reasonably open to the Board based on the applicant’s inconsistent and contradictory evidence on this seminal aspect of his claim.
ISSUES

## 22283:2 · paragraphs 12-12

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `616be144d073269138d796d7493b40ab8640839df86012a55f15122e6dd6cb31`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22283:2:subtheme:1 · paragraphs 12-12

- Raw key terms: `amount, applicant, assessment, base, capricious, cumulative, decision, effect`
- Display key terms: `amount, assessment, base, capricious, cumulative, effect`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: amount, assessment, base, capricious, cumulative, effect Evidence spans paragraphs 12-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5045759` offsets `40-46`; context: [12] The applicant raises the following issues:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `5045759` offsets `108-116`; context: err in law by ignoring or misinterpreting evidence properly before it?

#### Section text

[12] The applicant raises the following issues:
1. Did the R.P.D. err in law by ignoring or misinterpreting evidence properly before it?
2. Did the R.P.D. make patently unreasonable findings of fact or base its decision on findings of fact made in a perverse and capricious manner without regard for the material properly before it? and
3. If the R.P.D.’s errors were not reviewable errors of law, then did the cumulative effect of these errors amount to an error assessment.

## 22283:3 · paragraphs 13-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `12034d8d0852afc97eb5500050efd7ee4b4487c78dac1b10392e6aa37a27c152`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22283:3:subtheme:1 · paragraphs 13-17

- Raw key terms: `review, standard, canada, held, applicant, board, court, credibility`
- Display key terms: `review, standard, credibility`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: review, standard, credibility Rule/authority context: STANDARD OF REVIEW | 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of Evidence spans paragraphs 13-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5045760` offsets `162-180`; context: STANDARD OF REVIEW
- Evidence: `issue` cue `whether` at chunk `5045761` offsets `189-196`; context: 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question.
- Evidence: `governing_rule` cue `standard of review` at chunk `5045761` offsets `144-162`; context: 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5045762` offsets `673-681`; context: the decision was based on inferences that were not supported by the evidence; or,
4.
- Evidence: `governing_rule` cue `standard of review` at chunk `5045762` offsets `34-52`; context: [15] In the past, I held that the standard of review for credibility findings of the Board was patent unreasonableness [see Chen v.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5045764` offsets `92-105`; context: The post-Dunsmuir jurisprudence has held that the appropriate standard of review applicable to credibility and plausibility assessments is that of reasonableness with a high level of curial deference [see Saleem v.

#### 22283:3:subtheme:2 · paragraphs 18-21

- Raw key terms: `board, applicant, analysis, canada, christianity, court, credible, error`
- Display key terms: `analysis, christianity, credible, error`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: analysis, christianity, credible, error Position/evidence statements: [20] The applicant submits that the Board assessed the applicant’s knowledge of Christianity too strictly when considering that the applicant has been practicing Christianity for only two years at the time of the hearing Rule/authority context: [18] The standard of review is therefore reasonableness with a high level of deference to the Board’s findings. Application context: [18] The standard of review is therefore reasonableness with a high level of deference to the Board’s findings. | [19] The Board concluded that the applicant’s basis for seeking refugee protection was not credible – namely that the PSB in China was looking for him because he was a member of an “underground” Christian Church. Evidence spans paragraphs 18-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5045765` offsets `121-126`; context: ANALYSIS
Issue: Was the Board unreasonable in determining that the applicant was not a trustworthy and credible witness?
- Evidence: `governing_rule` cue `standard of review` at chunk `5045765` offsets `9-27`; context: [18] The standard of review is therefore reasonableness with a high level of deference to the Board’s findings.
- Evidence: `reasoning_application` cue `therefore` at chunk `5045765` offsets `31-40`; context: [18] The standard of review is therefore reasonableness with a high level of deference to the Board’s findings.
- Evidence: `evidence_fact` cue `testimony` at chunk `5045766` offsets `263-272`; context: The applicant gave inconsistent and contradictory testimony at the hearing on important aspects of this key basis of his claim.
- Evidence: `reasoning_application` cue `because` at chunk `5045766` offsets `151-158`; context: [19] The Board concluded that the applicant’s basis for seeking refugee protection was not credible – namely that the PSB in China was looking for him because he was a member of an “underground” Christian Church.
- Evidence: `party_position` cue `submits` at chunk `5045767` offsets `19-26`; context: [20] The applicant submits that the Board assessed the applicant’s knowledge of Christianity too strictly when considering that the applicant has been practicing Christianity for only two years at the time of the hearing.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5045767` offsets `287-299`; context: Nevertheless, the Court will address it for future reference.

#### 22283:3:subtheme:3 · paragraphs 22-23

- Raw key terms: `applicant, board, court, member, unreasonable, able, above, answer`
- Display key terms: `unreasonable, able, above, answer`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: unreasonable, able, above, answer Application context: This Court has often overturned a Board Member’s decision as “unfair” and “unreasonable” because the applicant could not answer detailed questions about the Bible. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5045769` offsets `333-340`; context: Determining whether one is a genuine Christian by way of “trivia” is clearly contrary to the above case law.
- Evidence: `reasoning_application` cue `because` at chunk `5045769` offsets `519-526`; context: This Court has often overturned a Board Member’s decision as “unfair” and “unreasonable” because the applicant could not answer detailed questions about the Bible.

#### 22283:3:subtheme:4 · paragraphs 24-25

- Raw key terms: `certified, question, accordingly, advised, agrees, appeal, applicant, application`
- Display key terms: `certified, question, accordingly, advised, agrees`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: certified, question, accordingly, advised, agrees Application context: Accordingly, this application for judicial review will be dismissed. Operative outcome context: Accordingly, this application for judicial review will be dismissed. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `QUESTION` at chunk `5045771` offsets `267-275`; context: CERTIFIED QUESTION
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5045771` offsets `188-199`; context: Accordingly, this application for judicial review will be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5045771` offsets `246-255`; context: Accordingly, this application for judicial review will be dismissed.
- Evidence: `issue` cue `question` at chunk `5045772` offsets `76-84`; context: [25] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal.

#### Section text

[13] I reformulated the list of questions as follows:
1. Was the Board unreasonable in determining that the applicant was not a trustworthy and credible witness?
STANDARD OF REVIEW

[14] In Dunsmuir v. New Brunswick, 2008 SCC 9, 372 N.R. 1, the Supreme Court of Canada held at paragraph 62 that the first step in conducting a standard of review analysis is to “ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question.”

[15] In the past, I held that the standard of review for credibility findings of the Board was patent unreasonableness [see Chen v. Canada (MCI), 2002 FCT 1194, 118 A.C.W.S. (3d) 700, at para. 4; Gonzalez v. Canada (MCI), 2008 FC 128, 164 A.C.W.S. (3d) 674, at para. 13]. Before a credibility finding of the Board is set aside, one of the following criteria must be established:
1. the Board did not provide valid reasons for finding that an applicant lacked credibility;
2. the inferences drawn by the Board are based on implausibility findings that in the view of the Court are simply not plausible;
3. the decision was based on inferences that were not supported by the evidence; or,
4. the credibility finding was based on a finding of fact that was perverse, capricious, or without regard to the evidence.

[16] As a result of Dunsmuir, it is clear that the standard of patent unreasonableness has been eliminated, and that reviewing courts must focus on only two standards of review, those of reasonableness and correctness.

[17] Implausibility and credibility determinations are factual in nature. The post-Dunsmuir jurisprudence has held that the appropriate standard of review applicable to credibility and plausibility assessments is that of reasonableness with a high level of curial deference [see Saleem v. Canada (MCI), [2008] F.C.J. No. 482, 2008 FC 389 at para. 13; Malveda v. Canada (MCI), [2008] F.C.J. No. 527, 2008 FC 447 at paras. 17-20; Khokhar v. Canada (MCI), [2008] F.C.J. No. 571, 2008 FC 449 at paras. 17-20].

[18] The standard of review is therefore reasonableness with a high level of deference to the Board’s findings.
ANALYSIS
Issue: Was the Board unreasonable in determining that the applicant was not a trustworthy and credible witness?

[19] The Board concluded that the applicant’s basis for seeking refugee protection was not credible – namely that the PSB in China was looking for him because he was a member of an “underground” Christian Church. The applicant gave inconsistent and contradictory testimony at the hearing on important aspects of this key basis of his claim. The Board’s finding was reasonable, which applicant’s counsel conceded at the hearing. For this reason alone, the Court must uphold the Board’s finding that the applicant is not credible with respect to the reason he seeks refugee status or protection in Canada.

[20] The applicant submits that the Board assessed the applicant’s knowledge of Christianity too strictly when considering that the applicant has been practicing Christianity for only two years at the time of the hearing. In view of my finding above, this alleged error is not material. Nevertheless, the Court will address it for future reference.

[21] In assessing a claimant’s knowledge of Christianity, the Board should not adopt an unrealistically high standard of knowledge or focus on a “few points of error or misunderstandings to a level which reached the microscopic analysis” criticized in Attakora v. Canada (Minister of Employment and Immigration) (F.C.A.), (1989), 99 N.R. 168, [1989] F.C.J. No. 444 (QL), and subsequent cases” [see Huang v. Canada (MCI), 2008 FC 346, 69 Imm. L.R. (3d) 286, per Justice Mosley at para. 10; Chen v. Canada (MCI), 2007 FC 270, 155 A.C.W.S. (3d) 929, per Justice Barnes at para 16]. The Board should not fault a poorly educated claimant for being unable to identify a passage dealing with a particular ceremony or ritual in the claimant’s holy book [see Feradov v. Canada (MCI), 2007 FC 101, 154 A.C.W.S. (3d) 1183, per Justice Barnes at para. 16].

[22] A reading of the Board’s reasons gives the impression that to be determined to be a Christian one should be able to retain at least some encyclopaedic knowledge of the Bible or Jesus’ teaching. One cannot help but have sympathy for claimant who was struggling to understand and be understood through an interpreter. Determining whether one is a genuine Christian by way of “trivia” is clearly contrary to the above case law. This Court has often overturned a Board Member’s decision as “unfair” and “unreasonable” because the applicant could not answer detailed questions about the Bible.

[23] The Court also finds that the Board Member’s dismissal of the letter from the applicant’s Church to be unreasonable. This letter simply confirmed the applicant attended the Church and was baptized in the Church.

[24] Nevertheless, while the applicant may be a genuine Christian, the Board’s finding that the applicant was not credible on the key basis for his claim was reasonably open to the Board. Accordingly, this application for judicial review will be dismissed.
CERTIFIED QUESTION

[25] Both parties advised the Court that this case does not raise a serious question of general importance which ought to be certified for an appeal. The Court agrees.


## 22283:4 · paragraphs 26-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `11c0278eda5ae9dcfa0d86ee81ff13cc03f2a27eef67220b4335020958866194`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22283:4:subtheme:1 · paragraphs 26-27

- Raw key terms: `adjudges, application, cause, citizenship, court, date, dismissed, docket`
- Display key terms: `adjudges, date, dismissed`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: adjudges, date, dismissed Operative outcome context: JUDGMENT THIS COURT ORDERS AND ADJUDGES that: This application for judicial review is dismissed. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5045772` offsets `254-263`; context: JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
This application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
This application for judicial review is dismissed.
“Michael A. Kelen”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-664-09
STYLE OF CAUSE: PENGHUI WU v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: September 15, 2009
REASONS FOR 

## 22283:5 · paragraphs 28-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a2a06d5bad7fcbfde469488b44c14cd3abbc8e9a5bb0f6c4a5924f607f7d7e92`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22283:5:subtheme:1 · paragraphs 28-28

- Raw key terms: `appearances, applicant, attorney, barrister, brookshire, canada, dated, deputy`
- Display key terms: `barrister, brookshire, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, brookshire, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: KELEN J.
DATED: September 17, 2009
APPEARANCES:
Mr. John Savaglio
FOR THE APPLICANT
Ms. Nimanthika Kaneira
FOR THE RESPONDENT
SOLICITORS OF RECORD:
John Savaglio
Barrister & Solicitor
1919 Brookshire Square
Pickering, Ontario
L1V 6L2
FOR THE APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
