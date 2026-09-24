# Discussion Units: case 21247

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **32**
- Continuity pairs: **31**
- Discussion Units: **2**
- Paragraph source hashes: **32**
- Sub-themes: **9**

## 21247:1 · paragraphs 0-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8bf925f767ac2e7c79ee9cdc4ba5d646c37557b226f2256c613d52455cec6a56`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21247:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, canada, china, church, decision, arrested, days, february`
- Display key terms: `china, church, arrested, days, february`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position Display terms: china, church, arrested, days, february Position/evidence statements: He claimed refugee protection in Toronto three days after his arrival on the grounds that he fears persecution based on his religion. | [5] The applicant claims that the PSB continued to visit his home while he remained in hiding and it was for this reason that he fled China. Rule/authority context: The Refugee Protection Division (RPD) of the Immigration and Refugee Board, in a decision dated February 20, 2008, found that the applicant was neither a Convention refugee nor a person in need of protection under sectio | Decision Under Review Operative outcome context: For the reasons that follow, the application will be dismissed. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5000007` offsets `227-237`; context: The Refugee Protection Division (RPD) of the Immigration and Refugee Board, in a decision dated February 20, 2008, found that the applicant was neither a Convention refugee nor a person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `governing_rule` cue `under` at chunk `5000007` offsets `320-325`; context: The Refugee Protection Division (RPD) of the Immigration and Refugee Board, in a decision dated February 20, 2008, found that the applicant was neither a Convention refugee nor a person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `disposition` cue `dismissed` at chunk `5000007` offsets `546-555`; context: For the reasons that follow, the application will be dismissed.
- Evidence: `party_position` cue `claimed` at chunk `5000008` offsets `178-185`; context: He claimed refugee protection in Toronto three days after his arrival on the grounds that he fears persecution based on his religion.
- Evidence: `party_position` cue `claims` at chunk `5000011` offsets `18-24`; context: [5] The applicant claims that the PSB continued to visit his home while he remained in hiding and it was for this reason that he fled China.
- Evidence: `governing_rule` cue `Under` at chunk `5000011` offsets `352-357`; context: Decision Under Review

#### 21247:1:subtheme:2 · paragraphs 6-8

- Raw key terms: `applicant, board, christian, christianity, church, claim, faith, knowledge`
- Display key terms: `christian, christianity, church, faith, knowledge`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: christian, christianity, church, faith, knowledge Position/evidence statements: The member determined that whatever knowledge of Christianity and Pentecostalism the applicant may possess was largely obtained in Toronto and only for the purpose of supporting his invented claim. Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5000012` offsets `129-134`; context: The determinative issue in regard to Mr.
- Evidence: `party_position` cue `claim` at chunk `5000014` offsets `528-533`; context: The member determined that whatever knowledge of Christianity and Pentecostalism the applicant may possess was largely obtained in Toronto and only for the purpose of supporting his invented claim.
- Evidence: `evidence_fact` cue `determined that` at chunk `5000014` offsets `348-363`; context: The member determined that whatever knowledge of Christianity and Pentecostalism the applicant may possess was largely obtained in Toronto and only for the purpose of supporting his invented claim.

#### 21247:1:subtheme:3 · paragraphs 9-10

- Raw key terms: `christian, issues, answered, applicant, appropriate, authority, based, become`
- Display key terms: `christian, issues, answered, appropriate, authority, based, become`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: christian, issues, answered, appropriate, authority, based, become Position/evidence statements: [10] The applicant submits that the sole issue for consideration is whether the Board erred in its determination of his claim to be a Christian by ignoring the fact that the applicant had correctly answered many question Rule/authority context: I would frame the issues in the following terms: What is the appropriate standard of review? Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5000015` offsets `485-491`; context: Issues
- Evidence: `evidence_fact` cue `evidence` at chunk `5000015` offsets `475-483`; context: Cao wished to become a Christian and to practice his religion in China, he could do so without fear of persecution based on the documentary evidence.
- Evidence: `issue` cue `issue` at chunk `5000016` offsets `41-46`; context: [10] The applicant submits that the sole issue for consideration is whether the Board erred in its determination of his claim to be a Christian by ignoring the fact that the applicant had correctly answered many questions with respect to Christianity.
- Evidence: `party_position` cue `submits` at chunk `5000016` offsets `19-26`; context: [10] The applicant submits that the sole issue for consideration is whether the Board erred in its determination of his claim to be a Christian by ignoring the fact that the applicant had correctly answered many questions with respect to Christianity.
- Evidence: `governing_rule` cue `standard of review` at chunk `5000016` offsets `325-343`; context: I would frame the issues in the following terms:
What is the appropriate standard of review?

#### 21247:1:subtheme:4 · paragraphs 11-12

- Raw key terms: `applicant, board, christian, failed, genuine, whether, address, adherent`
- Display key terms: `christian, failed, genuine, whether, address, adherent`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: christian, failed, genuine, whether, address, adherent Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5000017` offsets `114-121`; context: [11] The applicant’s arguments center on his contention that the Board failed to determine in a reasonable manner whether he is a genuine Christian.
- Evidence: `issue` cue `whether` at chunk `5000018` offsets `126-133`; context: [12] The applicant relies upon decisions of this Court in which a reviewable error was found when the Board failed to address whether the applicant was a genuine adherent of the claimed faith.
- Evidence: `evidence_fact` cue `found that` at chunk `5000018` offsets `312-322`; context: 164 (Huang) the Board had found that the claimant was not a member of an underground church in China.

#### 21247:1:subtheme:5 · paragraphs 13-19

- Raw key terms: `applicant, board, christian, evidence, assessment, based, fact, religious`
- Display key terms: `christian, assessment, based, fact, religious`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: christian, assessment, based, fact, religious Position/evidence statements: [14] The applicant admits that the Board did in fact make a finding that he is not a “genuine practicing Christian”, but argues that the Board based its finding on unattainable and unreasonable requirements of knowledge  | [15] The applicant submits that the Board erred in determining that he was not a genuine Christian based on its assessment of his knowledge of the Pentecostal faith. Rule/authority context: Analysis Standard of Review Application context: While the applicant may not agree with the inferences drawn by the RPD, the respondent submits that it has not been sufficiently demonstrated that the RPD’s assessment is perverse, capricious or without regard to the evi Operative outcome context: [16] In addition, the applicant argues that the Board erred in its assessment of his religious knowledge as it asked questions of him based upon information not tendered as evidence on the record and never mentioned the  Evidence spans paragraphs 13-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5000019` offsets `188-195`; context: 338 (Li) the Court held that the Board will commit a reviewable error when it does not rule on whether an applicant is a practicing Christian, notwithstanding the fact that other adverse findings have been made against him.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5000019` offsets `236-251`; context: 338 (Li) the Court held that the Board will commit a reviewable error when it does not rule on whether an applicant is a practicing Christian, notwithstanding the fact that other adverse findings have been made against him.
- Evidence: `party_position` cue `argues` at chunk `5000020` offsets `121-127`; context: [14] The applicant admits that the Board did in fact make a finding that he is not a “genuine practicing Christian”, but argues that the Board based its finding on unattainable and unreasonable requirements of knowledge of the Christian faith and erred in its assessment of the applicant’s religious knowledge.
- Evidence: `party_position` cue `submits` at chunk `5000021` offsets `19-26`; context: [15] The applicant submits that the Board erred in determining that he was not a genuine Christian based on its assessment of his knowledge of the Pentecostal faith.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000021` offsets `604-612`; context: 135 (Feradov) wherein Justice Barnes found the Board’s criticism of the applicant’s evidence concerning his religious practices and knowledge to be unwarranted.
- Evidence: `party_position` cue `argues` at chunk `5000022` offsets `32-38`; context: [16] In addition, the applicant argues that the Board erred in its assessment of his religious knowledge as it asked questions of him based upon information not tendered as evidence on the record and never mentioned the applicant’s Certificate of Baptism, granted in Toronto, which he contends demonstrates a sufficient grasp of Christian knowledge to satisfy his church.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000022` offsets `173-181`; context: [16] In addition, the applicant argues that the Board erred in its assessment of his religious knowledge as it asked questions of him based upon information not tendered as evidence on the record and never mentioned the applicant’s Certificate of Baptism, granted in Toronto, which he contends demonstrates a sufficient grasp of Christian knowledge to satisfy his church.
- Evidence: `disposition` cue `granted` at chunk `5000022` offsets `256-263`; context: [16] In addition, the applicant argues that the Board erred in its assessment of his religious knowledge as it asked questions of him based upon information not tendered as evidence on the record and never mentioned the applicant’s Certificate of Baptism, granted in Toronto, which he contends demonstrates a sufficient grasp of Christian knowledge to satisfy his church.
- Evidence: `party_position` cue `submits` at chunk `5000023` offsets `20-27`; context: [17] The respondent submits that the applicant’s challenges to the RPD’s findings are largely unsupported by the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000023` offsets `113-121`; context: [17] The respondent submits that the applicant’s challenges to the RPD’s findings are largely unsupported by the evidence.
- Evidence: `party_position` cue `submits` at chunk `5000024` offsets `20-27`; context: [18] The respondent submits that the Board did not engage in an overly zealous or microscopic review of the evidence and even let some inconsistencies in the applicant’s testimony pass as inconsequential.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000024` offsets `108-116`; context: [18] The respondent submits that the Board did not engage in an overly zealous or microscopic review of the evidence and even let some inconsistencies in the applicant’s testimony pass as inconsequential.
- Evidence: `party_position` cue `asserts` at chunk `5000025` offsets `236-243`; context: The respondent asserts that it is not the function of this Court to substitute its view of matters of fact which the RPD has taken notice of.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000025` offsets `580-588`; context: While the applicant may not agree with the inferences drawn by the RPD, the respondent submits that it has not been sufficiently demonstrated that the RPD’s assessment is perverse, capricious or without regard to the evidence, and therefore the application should fail.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5000025` offsets `642-660`; context: Analysis
Standard of Review
- Evidence: `reasoning_application` cue `therefore` at chunk `5000025` offsets `594-603`; context: While the applicant may not agree with the inferences drawn by the RPD, the respondent submits that it has not been sufficiently demonstrated that the RPD’s assessment is perverse, capricious or without regard to the evidence, and therefore the application should fail.

#### 21247:1:subtheme:6 · paragraphs 20-24

- Raw key terms: `board, court, credibility, dunsmuir, findings, decision, fact, respect`
- Display key terms: `credibility, dunsmuir, findings, fact, respect`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: credibility, dunsmuir, findings, fact, respect Rule/authority context: The Supreme Court also held that a standard of review analysis need not be conducted in every instance. | [22] The Board’s credibility findings are findings of fact which are reviewable under section 18. Evidence spans paragraphs 20-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5000026` offsets `386-394`; context: Where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5000026` offsets `259-277`; context: The Supreme Court also held that a standard of review analysis need not be conducted in every instance.
- Evidence: `governing_rule` cue `under` at chunk `5000028` offsets `80-85`; context: [22] The Board’s credibility findings are findings of fact which are reviewable under section 18.

#### 21247:1:subtheme:7 · paragraphs 25-26

- Raw key terms: `answer, applicant, board, concerning, correctly, faith, regarding, able`
- Display key terms: `answer, concerning, correctly, faith, regarding, able`
- Argument roles: `counterargument_limitation, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, issue, party_position Display terms: answer, concerning, correctly, faith, regarding, able Position/evidence statements: [25] The applicant argues that the Board’s ultimate finding regarding the genuineness of his Christian identity was made upon unattainable and unreasonable requirements of knowledge of the Christian faith. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5000031` offsets `343-351`; context: The applicant cites Feradov, Chen and Huang, above, in support of the proposition that to require an applicant to correctly answer every question put to him concerning his religion in order to demonstrate his credibility sets far too high a standard.
- Evidence: `party_position` cue `argues` at chunk `5000031` offsets `19-25`; context: [25] The applicant argues that the Board’s ultimate finding regarding the genuineness of his Christian identity was made upon unattainable and unreasonable requirements of knowledge of the Christian faith.
- Evidence: `counterargument_limitation` cue `however` at chunk `5000032` offsets `439-446`; context: I note that the applicant did in fact struggle with certain questions, however he also successfully answered a number of others, some of which were quite specific.

#### 21247:1:subtheme:8 · paragraphs 27-30

- Raw key terms: `applicant, member, reasons, board, christian, claim, decision, faith`
- Display key terms: `christian, faith`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: christian, faith Position/evidence statements: The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value. Application context: Accordingly, I must disallow the application. Operative outcome context: JUDGMENT IT IS THE JUDGMENT OF THIS COURT that the application is dismissed. Evidence spans paragraphs 27-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5000033` offsets `158-166`; context: It is understandable that he might not be able to answer each question put to him concerning the specifics of his faith.
- Evidence: `evidence_fact` cue `testimony` at chunk `5000033` offsets `417-426`; context: But the Board’s finding regarding the applicant’s professed Christian faith was primarily based on the negative inferences the member drew from the significant inconsistencies in the applicant’s oral testimony at the hearing on issues that were material to his claim.
- Evidence: `party_position` cue `submits` at chunk `5000034` offsets `261-268`; context: The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value.
- Evidence: `evidence_fact` cue `evidence` at chunk `5000034` offsets `136-144`; context: [28] It is clear from the member’s reasons that he arrived at the conclusion that the applicant’s faith was not genuine in spite of the evidence that the applicant had been in regular attendance at a church in Toronto and had been baptized there.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5000034` offsets `573-579`; context: Taken as a whole, the decision cannot be said to be irrational or unsupported by the evidence.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5000035` offsets `189-200`; context: Accordingly, I must disallow the application.
- Evidence: `disposition` cue `dismissed` at chunk `5000035` offsets `347-356`; context: JUDGMENT
IT IS THE JUDGMENT OF THIS COURT that the application is dismissed.

#### Section text

Cao v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-10-17
Neutral citation
2008 FC 1174
File numbers
IMM-1303-08
Decision Content
Date: 20081017
Docket: IMM-1303-08
Citation: 2008 FC 1174
Ottawa, Ontario, October 17, 2008
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
WO JI CAO
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] Mr. Wo Ji Cao sought protection in Canada on the ground that he would be persecuted for his faith in China. The Refugee Protection Division (RPD) of the Immigration and Refugee Board, in a decision dated February 20, 2008, found that the applicant was neither a Convention refugee nor a person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (IRPA). Mr. Cao brought this application for judicial review of the RPD’s decision. For the reasons that follow, the application will be dismissed.
Background

[2] Mr. Cao is a 34 year old citizen of the Guangdong province in the People’s Republic of China (PRC). He fled China on November 6, 2006, and arrived in Canada the same day. He claimed refugee protection in Toronto three days after his arrival on the grounds that he fears persecution based on his religion.

[3] The applicant explained in his Personal Information Form (PIF) narrative that in November, 2005, his wife began experiencing serious joint pain as a result of many years of farming. She became debilitated and the applicant became her primary caregiver. The added burden caused the applicant to be stressed and to believe that human life was “painful and meaningless”. In mid-February, 2006, the applicant’s best friend introduced him to Christianity as a means of solving his problems and in late February took him to a service at an underground church. The applicant says that his attendance at the underground services over the following months helped improve his wife’s health as well as his own personal well-being.

[4] According to the applicant’s account, during a service at a member’s house on September 24, 2006, a lookout informed the group that the Public Security Bureau (PSB) was coming. The group dispersed, and the applicant went to his cousin’s house to hide. Two days later, while still in hiding, the applicant received a phone call from his wife informing him that PSB officers had visited his home and were looking for him. His wife said the PSB had accused him of being involved in illegal religious activities and that they had informed her that he must surrender himself to them. The PSB had also arrested two of his fellow church members.

[5] The applicant claims that the PSB continued to visit his home while he remained in hiding and it was for this reason that he fled China. After arriving in Canada, Mr. Cao says that he learned that the PSB continued to visit his home looking for him and that the two members from his church group who had been arrested were still detained.
Decision Under Review

[6] The Board concluded that the claimant was neither a Convention refugee nor a person in need of protection. The determinative issue in regard to Mr. Cao’s claim was a lack of credibility. On a balance of probabilities, the Board concluded that the applicant was not a member of an underground church, was not being pursued by the PSB, and was not a genuine practicing Christian. In short, the Board did not believe his story.

[7] The Board based its finding on the negative inferences it drew from inconsistencies in the answers provided by the applicant to questions relating to his wife’s medical documents; the exclusion of his wife from the introduction to Christianity; his knowledge of the risk inherent to attendance at an underground church prior to his first service; his knowledge regarding the procedure when a pastor is or is not present during underground services; the legal procedures utilized by the PSB to take people into custody; and his knowledge of Christianity and the Pentecostal faith.

[8] Regarding the assessment of Mr. Cao’s Christian knowledge, the Board member acknowledged that the applicant was able to answer a number of questions, but noted that he was unable to answer questions concerning the Pentecostal faith he professed to follow that, in the member’s view, any practicing Pentecostal Christian should know. The member determined that whatever knowledge of Christianity and Pentecostalism the applicant may possess was largely obtained in Toronto and only for the purpose of supporting his invented claim. The member found that the applicant’s claim was fraudulent and was made in bad faith.

[9] The member concluded that the claimant had failed to satisfy his burden of establishing a serious possibility that he would be persecuted or that he would be personally subjected to a risk to his life or a risk of cruel and unusual punishment or a risk of torture by any authority in the PRC. Moreover, the member held that if Mr. Cao wished to become a Christian and to practice his religion in China, he could do so without fear of persecution based on the documentary evidence.
Issues

[10] The applicant submits that the sole issue for consideration is whether the Board erred in its determination of his claim to be a Christian by ignoring the fact that the applicant had correctly answered many questions with respect to Christianity. I would frame the issues in the following terms:
What is the appropriate standard of review? Did the Board err in concluding that the applicant is not a genuine Christian?
Applicant’s Submissions

[11] The applicant’s arguments center on his contention that the Board failed to determine in a reasonable manner whether he is a genuine Christian.

[12] The applicant relies upon decisions of this Court in which a reviewable error was found when the Board failed to address whether the applicant was a genuine adherent of the claimed faith. In Huang v. Canada (Minister of Citizenship and Immigration), 2008 FC 132, [2008] F.C.J. No. 164 (Huang) the Board had found that the claimant was not a member of an underground church in China. The Court concluded that the Board erred in failing to address whether the applicant was a genuine Christian who would consequently face religious persecution if returned to China, regardless of whether he had previously been a member of an underground church or not.

[13] Similarly in Li v. Canada (Citizenship and Immigration), 2008 FC 266, [2008] F.C.J. No. 338 (Li) the Court held that the Board will commit a reviewable error when it does not rule on whether an applicant is a practicing Christian, notwithstanding the fact that other adverse findings have been made against him.

[14] The applicant admits that the Board did in fact make a finding that he is not a “genuine practicing Christian”, but argues that the Board based its finding on unattainable and unreasonable requirements of knowledge of the Christian faith and erred in its assessment of the applicant’s religious knowledge.

[15] The applicant submits that the Board erred in determining that he was not a genuine Christian based on its assessment of his knowledge of the Pentecostal faith. He argues that a review of the recording of the proceeding reveals that he exhibited a reasonable level of knowledge of his religion, given the fact that he had only been exposed to it for less than two years. In support of this proposition, the applicant cites Feradov v. Canada (Minister of Citizenship and Immigration), 2007 FC 101, [2007] F.C.J. No. 135 (Feradov) wherein Justice Barnes found the Board’s criticism of the applicant’s evidence concerning his religious practices and knowledge to be unwarranted. The applicant also cites Chen v. Canada (Minister of Citizenship and Immigration), 2007 FC 270, [2007] F.C.J. No. 395 and Huang, above, to support his argument.

[16] In addition, the applicant argues that the Board erred in its assessment of his religious knowledge as it asked questions of him based upon information not tendered as evidence on the record and never mentioned the applicant’s Certificate of Baptism, granted in Toronto, which he contends demonstrates a sufficient grasp of Christian knowledge to satisfy his church.
Respondent’s Submissions

[17] The respondent submits that the applicant’s challenges to the RPD’s findings are largely unsupported by the evidence. Contrary to what the applicant suggests, the respondent maintains that the Board found in clear and definitive terms that the applicant was not a genuine, practicing Christian.

[18] The respondent submits that the Board did not engage in an overly zealous or microscopic review of the evidence and even let some inconsistencies in the applicant’s testimony pass as inconsequential. The respondent asserts that the Board had the advantage of seeing and hearing the applicant testify and did not find the evidence of his religious practice in China, or the manner by which he left China convincing. The respondent maintains that these are rational reasons for rejecting the applicant’s claim.

[19] The respondent notes that credibility findings that are based on evidentiary inconsistencies, evasions and lack of detail are the heartland of the Board’s discretion as a trier or fact and are entitled to deference. The respondent asserts that it is not the function of this Court to substitute its view of matters of fact which the RPD has taken notice of. While the applicant may not agree with the inferences drawn by the RPD, the respondent submits that it has not been sufficiently demonstrated that the RPD’s assessment is perverse, capricious or without regard to the evidence, and therefore the application should fail.
Analysis
Standard of Review

[20] In Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] S.C.J. No. 9 (Dunsmuir), the Supreme Court of Canada abandoned the patent unreasonableness standard leaving only two standards of review, correctness and reasonableness. The Supreme Court also held that a standard of review analysis need not be conducted in every instance. Where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.

[21] In this case, the Board’s finding with respect to the applicant’s status as a Christian was based upon a number of negative inferences, which led to a negative credibility finding. Prior to Dunsmuir, it was settled law that the Board’s factual and credibility findings were reviewable on the patently unreasonable standard.

[22] The Board’s credibility findings are findings of fact which are reviewable under section 18.1(4)(d) of the Federal Courts Act, which provides that this Court “may grant relief under subsection (3) if it is satisfied that the federal board, commission or other tribunal based its decision or order on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it”.

[23] Several decisions of this Court have held that Dunsmuir has not changed the law in respect of factual findings subject to the limitation in paragraph 18.1(4)(d): Da Mota v. Canada (Minister of Citizenship and Immigration), 2008 FC 386, [2008] F.C.J. No. 509; Obeid v. Canada (Minister of Citizenship and Immigration), 2008 FC 503, [2008] F.C.J. No. 633; Naumets v. Canada (Minister of Citizenship and Immigration), 2008 FC 522, [2008] F.C.J. No. 655. It has also been held that a Board decision concerning questions of fact and credibility are reviewable upon the standard of reasonableness: Sukhu v. Canada (Minister of Citizenship and Immigration), 2008 FC 427, [2008] F.C.J. No. 515.

[24] The Board’s credibility analysis is central to its role as a trier of fact. As such, these findings are to be given significant deference by the reviewing Court. The Board’s credibility findings should stand unless its reasoning process was flawed and the resulting decision falls outside the range of possible, acceptable outcomes which are defensible in respect of the facts and the law, Dunsmuir, above at paragraph 47.
Did the Board err in concluding that the applicant is not a genuine Christian?

[25] The applicant argues that the Board’s ultimate finding regarding the genuineness of his Christian identity was made upon unattainable and unreasonable requirements of knowledge of the Christian faith. The applicant cites Feradov, Chen and Huang, above, in support of the proposition that to require an applicant to correctly answer every question put to him concerning his religion in order to demonstrate his credibility sets far too high a standard. Moreover, the applicant submits, the Board ignored the baptismal certificate and letter confirming membership in the Church issued by his Toronto pastor.

[26] During the hearing, the Board member asked the applicant a number of questions concerning Christianity and the Pentecostal faith. In his reasons for decision, the member notes that while he was able to correctly answer a number of questions concerning Christianity, Mr. Cao was unable to answer certain questions regarding the specifics of the Pentecostal faith. I note that the applicant did in fact struggle with certain questions, however he also successfully answered a number of others, some of which were quite specific.

[27] At the time of the Board hearing, the applicant had been a Pentecostal for only two years. It is understandable that he might not be able to answer each question put to him concerning the specifics of his faith. But the Board’s finding regarding the applicant’s professed Christian faith was primarily based on the negative inferences the member drew from the significant inconsistencies in the applicant’s oral testimony at the hearing on issues that were material to his claim.

[28] It is clear from the member’s reasons that he arrived at the conclusion that the applicant’s faith was not genuine in spite of the evidence that the applicant had been in regular attendance at a church in Toronto and had been baptized there. The applicant submits that the member should have accorded deference to the Pastor’s opinion and taken the baptismal certificate at face value. To do so would, in effect, substitute the Pastor’s assessment of the genuineness of the claim of faith for that which the member was required to make. Taken as a whole, the decision cannot be said to be irrational or unsupported by the evidence.

[29] The Board member provided extensive and transparent reasons for his finding as to the applicant’s Christian identity. The decision overall was within the range of acceptable outcomes. Accordingly, I must disallow the application. No questions were proposed for certification.
JUDGMENT
IT IS THE JUDGMENT OF THIS COURT that the application is dismissed. There are no questions to certify.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-1303-08
STYLE OF CAUSE: WO JI CAO
And
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: September 11, 2008
REASONS FOR 

## 21247:2 · paragraphs 31-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b14ecd1403c0239eb755c30d355a1e5666396cc738e1c4ba5cb9d7c884018624`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21247:2:subtheme:1 · paragraphs 31-31

- Raw key terms: `appearances, applicant, associates, attorney, campana, canada, dated, deputy`
- Display key terms: `associates, campana, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, campana, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 31-31. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: MOSLEY J.
DATED: October 17, 2008
APPEARANCES:
Vania Campana
FOR THE APPLICANT
Dupe Oluyomi
FOR THE RESPONDENT
SOLICITORS OF RECORD:
VANIA CAMPANA
Lewis & Associates
Toronto, Ontario
FOR THE APPLICANT
JOHN H. SIMS, Q.C.
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
