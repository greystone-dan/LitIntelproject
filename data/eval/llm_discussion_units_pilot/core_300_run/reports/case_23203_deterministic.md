# Discussion Units: case 23203

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **25**
- Continuity pairs: **24**
- Discussion Units: **3**
- Paragraph source hashes: **25**
- Sub-themes: **7**

## 23203:1 · paragraphs 0-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c18660097e56c877b4a21f5ff0b7955310793c6bd6518b311a7545c2ce34490f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23203:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, family, canada, marry, obeefack, protection, raised, refugee`
- Display key terms: `family, marry, obeefack, protection, raised, refugee`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: family, marry, obeefack, protection, raised, refugee Position/evidence statements: The applicant claims that in 2011, following her repeated refusals to marry Obeefack, her uncle tried to force her to reimburse her would-be husband. | [6] The applicant arrived in Canada on April 3, 2013, and claimed refugee protection on May 16, 2013. Rule/authority context: Introduction [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision dated November 5, 2013, by a member of the Refugee Appe Application context: The applicant alleges that her uncle sold her because she was no longer capable of supporting the family in which she had been raised. | Because of this relationship, she refused to marry Mr. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5089155` offsets `841-856`; context: Introduction [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision dated November 5, 2013, by a member of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board [IRB] of Canada, upholding a decision of the Refugee Protection Division [RPD] whereby it was determined that the applicant is neither a “Convention refugee” under section 96 of the IRPA nor a “person in need of protection” within the meaning of section 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5089155` offsets `532-537`; context: Introduction [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision dated November 5, 2013, by a member of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board [IRB] of Canada, upholding a decision of the Refugee Protection Division [RPD] whereby it was determined that the applicant is neither a “Convention refugee” under section 96 of the IRPA nor a “person in need of protection” within the meaning of section 97 of the IRPA.
- Evidence: `reasoning_application` cue `because` at chunk `5089156` offsets `121-128`; context: The applicant alleges that her uncle sold her because she was no longer capable of supporting the family in which she had been raised.
- Evidence: `party_position` cue `claims` at chunk `5089157` offsets `222-228`; context: The applicant claims that in 2011, following her repeated refusals to marry Obeefack, her uncle tried to force her to reimburse her would-be husband.
- Evidence: `reasoning_application` cue `Because` at chunk `5089157` offsets `143-150`; context: Because of this relationship, she refused to marry Mr.
- Evidence: `party_position` cue `claimed` at chunk `5089159` offsets `58-65`; context: [6] The applicant arrived in Canada on April 3, 2013, and claimed refugee protection on May 16, 2013.
- Evidence: `evidence_fact` cue `evidence` at chunk `5089161` offsets `791-799`; context: Indeed, she provided no evidence of his existence.

#### 23203:1:subtheme:2 · paragraphs 7-8

- Raw key terms: `fact, acknowledge, affected, analysis, appeal, applicant, applied, arguing`
- Display key terms: `fact, acknowledge, affected, analysis, applied, arguing`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: fact, acknowledge, affected, analysis, applied, arguing Rule/authority context: [11] After conducting an analysis as to the standard of review to be applied, the RAD concluded that the principles developed in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 applied here, and included an excerp Application context: Obeefack because she wanted nothing to do with him. | [11] After conducting an analysis as to the standard of review to be applied, the RAD concluded that the principles developed in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 applied here, and included an excerp Operative outcome context: Impugned decision [10] The RAD dismissed the applicant’s appeal, thereby reaffirming that the RPD’s findings in its decision were reasonable. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5089162` offsets `142-150`; context: That the RPD erred in interpreting the case as a question of forced marriage rather than as a question of money.
- Evidence: `reasoning_application` cue `because` at chunk `5089162` offsets `625-632`; context: Obeefack because she wanted nothing to do with him.
- Evidence: `disposition` cue `dismissed` at chunk `5089162` offsets `1066-1075`; context: Impugned decision [10] The RAD dismissed the applicant’s appeal, thereby reaffirming that the RPD’s findings in its decision were reasonable.
- Evidence: `issue` cue `issues` at chunk `5089163` offsets `353-359`; context: As we will now demonstrate, questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5089163` offsets `44-62`; context: [11] After conducting an analysis as to the standard of review to be applied, the RAD concluded that the principles developed in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 applied here, and included an excerpt from paragraph 51:
.
- Evidence: `reasoning_application` cue `applied` at chunk `5089163` offsets `69-76`; context: [11] After conducting an analysis as to the standard of review to be applied, the RAD concluded that the principles developed in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 applied here, and included an excerpt from paragraph 51:
.

#### 23203:1:subtheme:3 · paragraphs 9-13

- Raw key terms: `huruglica, conclusion, decision, determination, justice, phelan, review, above`
- Display key terms: `huruglica, conclusion, determination, justice, phelan, review, above`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: huruglica, conclusion, determination, justice, phelan, review, above Rule/authority context: Did the RAD err in its determination of the standard of review to be applied to the RPD’s decision? | The RAD’s determination with respect to standard of review is owed little deference from this Court (Dunsmuir, above, at para 50). Application context: Did the RAD err in its determination of the standard of review to be applied to the RPD’s decision? Evidence spans paragraphs 9-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5089164` offsets `253-259`; context: Issues [13] The issues are:
a.
- Evidence: `evidence_fact` cue `found that` at chunk `5089164` offsets `783-793`; context: In that decision, Justice Phelan found that the RAD’s determination of the standard of review to be applied to an RPD decision is itself reviewable on a correctness standard, given that it is a question of law that is of general interest to the legal system and that it is well beyond the scope of the RAD’s expertise (see paras 25 to 34).
- Evidence: `governing_rule` cue `standard of review` at chunk `5089164` offsets `383-401`; context: Did the RAD err in its determination of the standard of review to be applied to the RPD’s decision?
- Evidence: `reasoning_application` cue `applied` at chunk `5089164` offsets `408-415`; context: Did the RAD err in its determination of the standard of review to be applied to the RPD’s decision?
- Evidence: `governing_rule` cue `standard of review` at chunk `5089165` offsets `89-107`; context: The RAD’s determination with respect to standard of review is owed little deference from this Court (Dunsmuir, above, at para 50).
- Evidence: `evidence_fact` cue `evidence` at chunk `5089166` offsets `240-248`; context: [17] Save for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference to the RPD’s assessment of the evidence: see Huruglica, at paras 37 and 55.
- Evidence: `evidence_fact` cue `evidence` at chunk `5089167` offsets `204-212`; context: Thus, the RAD must proceed with an independent review of the evidence in order to arrive at its own conclusion.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5089167` offsets `5-16`; context: [18] Pursuant to subsection 111(1) of the IRPA, the RAD is entitled to substitute a determination that, in its opinion, should have been made.

#### 23203:1:subtheme:4 · paragraphs 14-18

- Raw key terms: `advantage, applicant, assessment, testimony, above, analysis, conclusion, credibility`
- Display key terms: `advantage, assessment, testimony, above, analysis, conclusion, credibility`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: advantage, assessment, testimony, above, analysis, conclusion, credibility Position/evidence statements: Balotoken was false and the numerous documents she provided indicating that she is single, the RPD found that it was difficult to assign much weight to the documents submitted. Rule/authority context: [20] With respect, I agree with Justice Phelan’s analysis at paragraphs 35 to 56 in Huruglica, above, regarding the standard of review to be applied to RPD decisions. Application context: [20] With respect, I agree with Justice Phelan’s analysis at paragraphs 35 to 56 in Huruglica, above, regarding the standard of review to be applied to RPD decisions. | Conclusion [26] For the foregoing reasons, I find that the RAD’s analysis of the evidence and of the parties’ submissions was insufficient, and that this application must be allowed. Operative outcome context: Conclusion [26] For the foregoing reasons, I find that the RAD’s analysis of the evidence and of the parties’ submissions was insufficient, and that this application must be allowed. Evidence spans paragraphs 14-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5089169` offsets `299-306`; context: It must review all aspects of the RPD’s decision and come to an independent assessment of whether the claimant is a Convention refugee or a person in need of protection.
- Evidence: `issue` cue `issues` at chunk `5089170` offsets `98-104`; context: [55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”.
- Evidence: `evidence_fact` cue `testimony` at chunk `5089171` offsets `370-379`; context: But two of the findings were not based exclusively on the testimony of the applicant.
- Evidence: `governing_rule` cue `standard of review` at chunk `5089171` offsets `116-134`; context: [20] With respect, I agree with Justice Phelan’s analysis at paragraphs 35 to 56 in Huruglica, above, regarding the standard of review to be applied to RPD decisions.
- Evidence: `reasoning_application` cue `applied` at chunk `5089171` offsets `141-148`; context: [20] With respect, I agree with Justice Phelan’s analysis at paragraphs 35 to 56 in Huruglica, above, regarding the standard of review to be applied to RPD decisions.
- Evidence: `party_position` cue `submitted` at chunk `5089172` offsets `444-453`; context: Balotoken was false and the numerous documents she provided indicating that she is single, the RPD found that it was difficult to assign much weight to the documents submitted.
- Evidence: `evidence_fact` cue `evidence` at chunk `5089172` offsets `72-80`; context: [23] In my view, the RAD should have reconsidered the assessment of the evidence in that regard.
- Evidence: `evidence_fact` cue `testimony` at chunk `5089173` offsets `81-90`; context: [25] Given that this finding was not made solely on the basis of the applicant’s testimony, and given that the RPD enjoyed no particular advantage in analyzing the documents, I am of the view that the RAD ought to have reconsidered the evidence in that regard.
- Evidence: `reasoning_application` cue `I find` at chunk `5089173` offsets `310-316`; context: Conclusion [26] For the foregoing reasons, I find that the RAD’s analysis of the evidence and of the parties’ submissions was insufficient, and that this application must be allowed.
- Evidence: `disposition` cue `allowed` at chunk `5089173` offsets `441-448`; context: Conclusion [26] For the foregoing reasons, I find that the RAD’s analysis of the evidence and of the parties’ submissions was insufficient, and that this application must be allowed.

#### 23203:1:subtheme:5 · paragraphs 19-21

- Raw key terms: `certification, parties, questions, reasons, regard, above, case, court`
- Display key terms: `certification, questions, regard, above, case`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: certification, questions, regard, above, case Application context: [29] The parties will therefore have thirty (30) days from the date of these reasons to make submissions with regard to the wording of any questions for certification. Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5089174` offsets `58-64`; context: [27] As Justice Phelan noted in Huruglica, above, similar issues have been raised in matters that are currently before the Court and there are very few precedents for it to use as guidance.
- Evidence: `reasoning_application` cue `therefore` at chunk `5089176` offsets `22-31`; context: [29] The parties will therefore have thirty (30) days from the date of these reasons to make submissions with regard to the wording of any questions for certification.

#### Section text

Yetna v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-09-10
Neutral citation
2014 FC 858
File numbers
IMM-7567-13
Decision Content
Date: 20140910
Docket: IMM-7567-13
Citation: 2014 FC 858
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, September 10, 2014
PRESENT: The Honourable Mr. Justice Locke
BETWEEN:
FIDELE NGO YETNA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] of a decision dated November 5, 2013, by a member of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board [IRB] of Canada, upholding a decision of the Refugee Protection Division [RPD] whereby it was determined that the applicant is neither a “Convention refugee” under section 96 of the IRPA nor a “person in need of protection” within the meaning of section 97 of the IRPA.
II. Facts [2] The applicant is a 40 year-old woman from Cameroon who was working as a nurse and who was independent of the family in which she had been raised. She had supported the family until 2010, the year she was injured and forced to stop working.

[3] As the applicant’s father was deceased, her uncle had taken his place. The applicant alleges that her uncle sold her because she was no longer capable of supporting the family in which she had been raised. In fact, the uncle had accepted a sum of money from an 82 year-old man named Obeefack in return for consent to marry the applicant.

[4] The applicant had apparently been dating a man named Balotoken for several years and had become the adoptive mother of his three children. Because of this relationship, she refused to marry Mr. Obeefack. The applicant claims that in 2011, following her repeated refusals to marry Obeefack, her uncle tried to force her to reimburse her would-be husband. Her uncle also reportedly threatened Balotoken, who, following these threats, left the applicant.

[5] In December 2012, the applicant was purportedly physically abused by the family in which she had been raised.

[6] The applicant arrived in Canada on April 3, 2013, and claimed refugee protection on May 16, 2013.

[7] The hearing before the RPD was held on July 11, 2013, and its decision was delivered on July 31, 2013.

[8] The RPD concluded that the applicant lacked credibility. More specifically, the RPD had doubts about the following:
a. The uncle, who was father figure to the applicant, apparently respected her independence until she was 40 years old, but suddenly changed his attitude. The RPD also noted that most arranged marriages occur at a young age. The RPD further noted that no arranged marriages had been planned for the applicant’s sisters.
b. The applicant was forced to stop working in 2010, but continued her studies in 2011 with the intention of later finding employment.
c. Although attempts to force her to marry Obeefack were made for several years, the applicant was unable to provide details about him with respect to his family and the source of his wealth. Indeed, she provided no evidence of his existence.
d. Between 2009 and 2013, the applicant travelled to Benin and Gabon on several occasions. The fact that she returned to Cameroon after these trips indicates that the applicant did not fear returning to her country of origin.
e. Documents provided by the applicant to obtain a visa to travel to Canada indicate that she married Mr. Balotoken in 2011. The applicant disputed the veracity of those documents and provided other documents that indicated that she was single. The RPD noted that one of the documents provided for the visa bore the applicant’s signature. The RPD stated that it was impossible to determine which documents were genuine, those provided for the visa or those provided for the refugee protection claim.

[9] The applicant filed an appeal of that decision before the RAD, arguing the following:
a. That the RPD erred in interpreting the case as a question of forced marriage rather than as a question of money.
b. That the RPD did not acknowledge that the uncle who arranged the marriage was not the applicant’s father.
c. That the RPD failed to consider other reasons that would explain the arranged marriage, such as (i) the fact that she was the next daughter to be married, and (ii) the fact that her family disapproved of her and Mr. Balotoken being Jehovah’s Witnesses.
d. That the applicant knew nothing about Mr. Obeefack because she wanted nothing to do with him.
e. That numerous documents contradict the false documents submitted to obtain a visa. Thus, the RPD erred in questioning the applicant’s credibility.
f. That the applicant’s trips outside the country, after which she would return to Cameroon, occurred prior to the problems she later encountered. Therefore, those trips should not have affected her credibility.
III. Impugned decision [10] The RAD dismissed the applicant’s appeal, thereby reaffirming that the RPD’s findings in its decision were reasonable.

[11] After conducting an analysis as to the standard of review to be applied, the RAD concluded that the principles developed in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 applied here, and included an excerpt from paragraph 51:
. . . As we will now demonstrate, questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness.

[12] The RAD analyzed all of the RPD’s findings with the exception of that regarding the trips outside Cameroon. Apart from this exception (which the RAD considered to be secondary), the RAD concluded that all of the RPD’s findings were reasonable.
IV. Issues [13] The issues are:
a. On which standard is the RAD’s decision reviewable?
b. Did the RAD err in its determination of the standard of review to be applied to the RPD’s decision?
c. Did the RAD err in upholding the RPD’s conclusion that the applicant lacked credibility?
V. Standard of review applicable to RAD’s decision [14] My colleague, Justice Phelan, was called upon to decide a similar matter in Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica]. In that decision, Justice Phelan found that the RAD’s determination of the standard of review to be applied to an RPD decision is itself reviewable on a correctness standard, given that it is a question of law that is of general interest to the legal system and that it is well beyond the scope of the RAD’s expertise (see paras 25 to 34).

[15] With respect, I concur with Justice Phelan. The RAD’s determination with respect to standard of review is owed little deference from this Court (Dunsmuir, above, at para 50). Such a finding is consistent with that of the Alberta Court of Appeal in Newton v Criminal Trial Lawyers’ Assn., 2010 ABCA 399, 493 AR 89, at para 39.
VI. Standard of review applicable to RPD’s decision [16] Taking into consideration once more Justice Phelan’s decision in Huruglica, above, I am of the view that the RAD erred in concluding that the RPD decision was reviewable on a reasonableness standard.

[17] Save for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference to the RPD’s assessment of the evidence: see Huruglica, at paras 37 and 55. The RAD has as much expertise as the RPD, and perhaps more in terms of analyzing relevant documents and parties’ submissions.

[18] Pursuant to subsection 111(1) of the IRPA, the RAD is entitled to substitute a determination that, in its opinion, should have been made. Thus, the RAD must proceed with an independent review of the evidence in order to arrive at its own conclusion.

[19] At paragraphs 54 and 55 of his decision in Huruglica, above, Justice Phelan stated the following:

[54] Having concluded that the RAD erred in reviewing the RPD’s decision on the standard of reasonableness, I have further concluded that for the reasons above, the RAD is required to conduct a hybrid appeal. It must review all aspects of the RPD’s decision and come to an independent assessment of whether the claimant is a Convention refugee or a person in need of protection. Where its assessment departs from that of the RPD, the RAD must substitute its own decision.

[55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”.

[20] With respect, I agree with Justice Phelan’s analysis at paragraphs 35 to 56 in Huruglica, above, regarding the standard of review to be applied to RPD decisions.
VII. RPD’s finding on the applicant’s credibility [21] The significant findings of the RPD in this matter centre on the applicant’s credibility. But two of the findings were not based exclusively on the testimony of the applicant. Thus, the RPD enjoyed no advantage over the RAD when it made its findings.
A. The father is in fact the uncle [22] A reading of the RPD’s decision shows that the panel perhaps failed to grasp that the uncle who had been acting as father to the applicant since 2005 was not her real father. I am of the opinion that the panel may have had a better understanding as to why the father suddenly changed his attitude towards his daughter had it properly interpreted that fact.

[23] In my view, the RAD should have reconsidered the assessment of the evidence in that regard.
B. The authenticity of the contract of marriage between the applicant and Mr. Balotoken [24] In light of the applicant’s testimony to the effect that her marriage contract with Mr. Balotoken was false and the numerous documents she provided indicating that she is single, the RPD found that it was difficult to assign much weight to the documents submitted.

[25] Given that this finding was not made solely on the basis of the applicant’s testimony, and given that the RPD enjoyed no particular advantage in analyzing the documents, I am of the view that the RAD ought to have reconsidered the evidence in that regard.
VIII. Conclusion [26] For the foregoing reasons, I find that the RAD’s analysis of the evidence and of the parties’ submissions was insufficient, and that this application must be allowed.

[27] As Justice Phelan noted in Huruglica, above, similar issues have been raised in matters that are currently before the Court and there are very few precedents for it to use as guidance. In that regard, this case is one in which a question for certification is warranted.

[28] None of the parties has proposed any serious questions of general importance for certification but I am of the view that, in light of these reasons, the possibility for such questions to be proposed should remain open.

[29] The parties will therefore have thirty (30) days from the date of these reasons to make submissions with regard to the wording of any questions for certification.


## 23203:2 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fc5680bed0f3b8b985305abd5f1b55b8a3957e4affdaca19cb01569ab1b4181f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23203:2:subtheme:1 · paragraphs 22-23

- Raw key terms: `date, adjudges, allowed, applicant, application, aside, back, cause`
- Display key terms: `date, adjudges, allowed, aside, back`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, adjudges, allowed, aside, back No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS AND ADJUDGES that:
1. This application for judicial review is allowed.
2. The RAD’s decision, dated November 5, 2013, is set aside and the matter referred back for full reconsideration, by a newly constituted RAD, of the RPD’s decision refusing the applicant’s claim for refugee protection.
3. The parties will have thirty (30) days from the date of these reasons to make submissions with regard to the wording of any questions for certification.
George R. Locke
Judge
Certified true translation
Sebastian Desbarats, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-7567-13
STYLE OF CAUSE:
FIDELE GNO YETNA v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
montréal, QUEBEC
DATE OF HEARING:
JULY 16, 2014


## 23203:3 · paragraphs 24-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3b154250f1e26c605b846ab889dd83b80c3f7dfdde9a31299e56f8ddb3d71513`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23203:3:subtheme:1 · paragraphs 24-24

- Raw key terms: `appearances, applicant, attorney, canada, counsel, dated, deputy, general`
- Display key terms: `dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
LOCKE J.
DATED:
SEPTEMBER 10, 2014
APPEARANCES:
Stéphanie Valois
FOR THE APPLICANT
Simone Truong
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Stéphanie Valois
Counsel
Montreal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Montreal, Quebec
FOR THE RESPONDENT
