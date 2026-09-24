# Discussion Units: case 25572

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **76**
- Continuity pairs: **75**
- Discussion Units: **5**
- Paragraph source hashes: **76**
- Sub-themes: **19**

## 25572:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `929b0b4f1706bb72bc3b6a1f042a3d91bf52b31a3af493293efb0d54520af667`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25572:1:subtheme:1 · paragraphs 0-13

- Raw key terms: `applicant, officer, canada, because, grenada, omar, application, april`
- Display key terms: `officer, because, grenada, omar, april`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: officer, because, grenada, omar, april Position/evidence statements: On 25 November 2004, the Applicant came to Canada a third time and claimed refugee status, basing her claim on the abuse she would suffer at the hands of her husband, Phillip. Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c. | She applied for an H&C exemption on 12 March 2007, which resulted in the Decision under review. Application context: Although Omar is a Canadian citizen, because of his age he will go where his mother goes. | She applied for judicial review of that decision, but her application was dismissed on 3 April 2006 because she failed to file an application record. Operative outcome context: [3] On 12 December 2005, the RPD denied the Applicant’s claim for refugee protection. | She noted that, because he lived with her in Grenada, Omar was denied access to services that other Canadians enjoy in Canada. Evidence spans paragraphs 0-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5203300` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c.
- Evidence: `party_position` cue `claimed` at chunk `5203301` offsets `499-506`; context: On 25 November 2004, the Applicant came to Canada a third time and claimed refugee status, basing her claim on the abuse she would suffer at the hands of her husband, Phillip.
- Evidence: `reasoning_application` cue `because` at chunk `5203301` offsets `235-242`; context: Although Omar is a Canadian citizen, because of his age he will go where his mother goes.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5203301` offsets `198-206`; context: Although Omar is a Canadian citizen, because of his age he will go where his mother goes.
- Evidence: `evidence_fact` cue `record` at chunk `5203302` offsets `228-234`; context: She applied for judicial review of that decision, but her application was dismissed on 3 April 2006 because she failed to file an application record.
- Evidence: `governing_rule` cue `under` at chunk `5203302` offsets `439-444`; context: She applied for an H&C exemption on 12 March 2007, which resulted in the Decision under review.
- Evidence: `reasoning_application` cue `applied` at chunk `5203302` offsets `90-97`; context: She applied for judicial review of that decision, but her application was dismissed on 3 April 2006 because she failed to file an application record.
- Evidence: `counterargument_limitation` cue `but` at chunk `5203302` offsets `136-139`; context: She applied for judicial review of that decision, but her application was dismissed on 3 April 2006 because she failed to file an application record.
- Evidence: `disposition` cue `denied` at chunk `5203302` offsets `33-39`; context: [3] On 12 December 2005, the RPD denied the Applicant’s claim for refugee protection.
- Evidence: `reasoning_application` cue `because` at chunk `5203303` offsets `102-109`; context: [4] The Applicant based her application for an H&C exemption primarily on the hardship she would face because of Phillip’s abuse and Grenada’s inability to protect her from him.
- Evidence: `reasoning_application` cue `because` at chunk `5203304` offsets `1036-1043`; context: She noted that, because he lived with her in Grenada, Omar was denied access to services that other Canadians enjoy in Canada.
- Evidence: `disposition` cue `denied` at chunk `5203304` offsets `1083-1089`; context: She noted that, because he lived with her in Grenada, Omar was denied access to services that other Canadians enjoy in Canada.
- Evidence: `governing_rule` cue `UNDER` at chunk `5203305` offsets `161-166`; context: DECISION UNDER REVIEW
- Evidence: `reasoning_application` cue `because` at chunk `5203307` offsets `92-99`; context: [8] The Officer rejected the Applicant’s application for permanent residence on H&C grounds because he was not satisfied that she or Omar would suffer unusual and undeserved or disproportionate hardship if her application was not granted.
- Evidence: `disposition` cue `granted` at chunk `5203307` offsets `230-237`; context: [8] The Officer rejected the Applicant’s application for permanent residence on H&C grounds because he was not satisfied that she or Omar would suffer unusual and undeserved or disproportionate hardship if her application was not granted.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203309` offsets `43-51`; context: [10] The Officer then considered the other evidence before him.
- Evidence: `reasoning_application` cue `because` at chunk `5203309` offsets `174-181`; context: He found that, because she was unemployed and collecting social assistance while she was living in Canada, the Applicant’s level of establishment was not sufficient to make it worth considering.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5203309` offsets `354-362`; context: Although Omar had made friends in Canada, the Officer found that removing him from Canada would not have a negative impact on him which would amount to unusual and undeserved or disproportionate hardship.
- Evidence: `evidence_fact` cue `found that` at chunk `5203310` offsets `72-82`; context: He found that she had decided to return to Grenada even though she had nothing and no one to return to.
- Evidence: `counterargument_limitation` cue `although` at chunk `5203310` offsets `438-446`; context: The Officer found that, although the Applicant was currently unemployed and had limited education, there was insufficient evidence that she could not find work or benefit from the assistance of family and friends in the future.
- Evidence: `evidence_fact` cue `found that` at chunk `5203311` offsets `22-32`; context: [12] The Officer also found that the Applicant did not face a risk of abuse from Phillip because she had not returned to him when she went back to Grenada.
- Evidence: `reasoning_application` cue `because` at chunk `5203311` offsets `89-96`; context: [12] The Officer also found that the Applicant did not face a risk of abuse from Phillip because she had not returned to him when she went back to Grenada.
- Evidence: `evidence_fact` cue `found that` at chunk `5203312` offsets `58-68`; context: He found that Omar’s interests were being met by the Applicant with the help of her family.

#### 25572:1:subtheme:2 · paragraphs 14-14

- Raw key terms: `abuser, accordingly, applicant, appropriate, care, concluded, degree, denied`
- Display key terms: `abuser, accordingly, appropriate, care, concluded, degree, denied`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: abuser, accordingly, appropriate, care, concluded, degree, denied Application context: Accordingly, he denied the Applicant’s request for permanent residence on H&C grounds. Operative outcome context: Accordingly, he denied the Applicant’s request for permanent residence on H&C grounds. Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5203313` offsets `497-503`; context: ISSUES
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5203313` offsets `410-421`; context: Accordingly, he denied the Applicant’s request for permanent residence on H&C grounds.
- Evidence: `disposition` cue `denied` at chunk `5203313` offsets `426-432`; context: Accordingly, he denied the Applicant’s request for permanent residence on H&C grounds.

#### Section text

Williams v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-02-07
Neutral citation
2012 FC 166
File numbers
IMM-2949-11
Decision Content
Federal Court
Cour fédérale
Date: 20120207
Docket: IMM-2949-11
Citation: 2012 FC 166
Ottawa, Ontario, February 7, 2012
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
ERLINA MARY WILLIAMS
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
INTRODUCTION

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c. 27 (Act) for judicial review of the decision an Immigration Officer (Officer) of Citizenship and Immigration Canada (CIC), dated 19 April 2011 (Decision), which refused the Applicant’s application for permanent residence on Humanitarian and Compassionate (H&C) grounds under subsection 25(1) of the Act.
BACKGROUND

[2] The Applicant is a citizen of Grenada. She currently lives in Grenada with her 8-year-old son, Omar. Omar is a Canadian citizen who was born in August 2002 while his mother was visiting Canada. Although Omar is a Canadian citizen, because of his age he will go where his mother goes. The Applicant first visited Canada in March 2001, and returned in July 2002. After the second visit, the Applicant returned to Grenada in 2003. On 25 November 2004, the Applicant came to Canada a third time and claimed refugee status, basing her claim on the abuse she would suffer at the hands of her husband, Phillip.

[3] On 12 December 2005, the RPD denied the Applicant’s claim for refugee protection. She applied for judicial review of that decision, but her application was dismissed on 3 April 2006 because she failed to file an application record. The Applicant applied for a pre-removal risk assessment on 9 March 2007 and received a negative decision on 3 July 2007. She applied for an H&C exemption on 12 March 2007, which resulted in the Decision under review.

[4] The Applicant based her application for an H&C exemption primarily on the hardship she would face because of Phillip’s abuse and Grenada’s inability to protect her from him. She also said that the abuse would have a negative impact on Omar. Further, she noted that Omar has severe asthma and requires ongoing medical treatment, which she would be unable to afford in Grenada because the medications are costly and she has limited resources. She also said that Omar had built up a support network in Canada and would suffer hardship if his mother was removed to Grenada.

[5] On 1 August 2007, the Applicant voluntarily executed the removal order which was in place against her. She bought tickets for her and Omar to travel to Grenada. On 17 July 2008 and 18 December 2008, she made additional submissions to CIC to support her H&C application. In these submissions, she drew attention to Omar’s asthma, the link between his asthma and the Grenadian climate, and her financial situation in Grenada. She also made submissions to CIC on 23 April 2010 in which she noted a letter from her sister, Arlene Williams, which indicated Arlene’s concern about Omar’s situation in Grenada. With these submissions, the Applicant included a letter from Omar’s doctor in Grenada – Dr. W. W. Thomas – attesting to Omar’s medical condition. On 5 April 2011, the Applicant made her final submissions to CIC on her application in which she reviewed her concerns about Omar’s asthma in the Grenadian climate, their living situation, and case law from the United Kingdom (UK) on the best interests of children. She noted that, because he lived with her in Grenada, Omar was denied access to services that other Canadians enjoy in Canada.

[6] The Officer considered the Applicant’s submissions and came to his Decision on 19 April 2011. He notified the Applicant by letter on 20 April 2011.
DECISION UNDER REVIEW

[7] The Decision in this case consists of both the Officer’s letter of 20 April 2011 and the Application for Permanent Residence Narrative Form, dated 19 April 2011.

[8] The Officer rejected the Applicant’s application for permanent residence on H&C grounds because he was not satisfied that she or Omar would suffer unusual and undeserved or disproportionate hardship if her application was not granted.

[9] The Officer began his analysis with a review of the Applicant’s immigration history. He noted that she had visited Canada twice prior to her rejected refugee claim. The Officer also reviewed the Applicant’s submissions in support of her H&C claim: that her financial situation in Grenada was poor; that Omar’s medical condition deteriorated while they were in Grenada; and that it was in Omar’s best interests to be in Canada. The Officer noted that the Applicant was presently being supported by her friends in Grenada.

[10] The Officer then considered the other evidence before him. He noted the Applicant’s eight years of education, volunteer services, and employment history. He found that, because she was unemployed and collecting social assistance while she was living in Canada, the Applicant’s level of establishment was not sufficient to make it worth considering. Although Omar had made friends in Canada, the Officer found that removing him from Canada would not have a negative impact on him which would amount to unusual and undeserved or disproportionate hardship.

[11] The Officer also looked at the Applicant’s financial situation. He found that she had decided to return to Grenada even though she had nothing and no one to return to. He assigned little weight to the Applicant’s claim of poverty, saying that her travel history, her choice to purchase her own tickets to Grenada, and the financial support she received from her friends and family did not support this claim. The Officer found that, although the Applicant was currently unemployed and had limited education, there was insufficient evidence that she could not find work or benefit from the assistance of family and friends in the future.

[12] The Officer also found that the Applicant did not face a risk of abuse from Phillip because she had not returned to him when she went back to Grenada.

[13] Finally, the Officer considered Omar’s interests. He found that Omar’s interests were being met by the Applicant with the help of her family. He also found that the letter from Dr. Thomas did not show that Omar had a severe medical condition. The Officer said that asthma is a common condition and found that it was being treated in spite of the Applicant’s financial hardship. He found that the Applicant was overstating Omar’s condition for her own gain and that she had twice returned to Grenada without appearing to give Omar’s condition the attention it deserved. Based on the Applicant’s submissions that her family would be willing to cover airfare for her and Omar to return to Canada, the Officer found that her family would be willing to assist with Omar’s medication. The Officer was not satisfied that the Applicant had been unable to provide for Omar’s medical condition.

[14] The Officer found­­ that the fears the Applicant had for her son before she returned to Grenada had not materialized; Omar was not in the presence of his mother’s abuser and was not deprived of an education or appropriate medical care. He concluded that neither the Applicant nor Omar were suffering undue and undeserved or disproportionate hardship in Grenada to the degree required to grant H&C relief. Accordingly, he denied the Applicant’s request for permanent residence on H&C grounds.
ISSUES

## 25572:2 · paragraphs 15-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0598a5f4fda4779137986f39f2f4330062e6476b766585fcdc0ea5ee8eec6690`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25572:2:subtheme:1 · paragraphs 15-17

- Raw key terms: `canada, case, child, court, factors, held, officer, review`
- Display key terms: `case, child, factors, officer, review`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: case, child, factors, officer, review Rule/authority context: ­ STANDARD OF REVIEW | [16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Application context: [15] The Applicant raises the following issues in this case: a) Whether the Officer failed to appropriately assess Omar’s best interests; b) Whether the Officer’s conclusions were unreasonable; c) Whether the Officer app Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5203314` offsets `40-46`; context: [15] The Applicant raises the following issues in this case:
a) Whether the Officer failed to appropriately assess Omar’s best interests;
b) Whether the Officer’s conclusions were unreasonable;
c) Whether the Officer applied the wrong test for the best interests of the child;
d) Whether the Officer provided adequate reasons.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5203314` offsets `329-347`; context: ­
STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `applied` at chunk `5203314` offsets `217-224`; context: [15] The Applicant raises the following issues in this case:
a) Whether the Officer failed to appropriately assess Omar’s best interests;
b) Whether the Officer’s conclusions were unreasonable;
c) Whether the Officer applied the wrong test for the best interests of the child;
d) Whether the Officer provided adequate reasons.
- Evidence: `issue` cue `question` at chunk `5203315` offsets `220-228`; context: Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5203315` offsets `86-104`; context: [16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance.

#### 25572:2:subtheme:2 · paragraphs 18-19

- Raw key terms: `canada, citizenship, court, fact, given, held, immigration, issue`
- Display key terms: `fact, given`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: fact, given Rule/authority context: The standard of review on the first issue is reasonableness. | The standard of review on the second issue is reasonableness. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5203317` offsets `358-366`; context: Where the best interests of a child lie is a question of fact which, following Dunsmuir, above, at paragraph 53, will attract a standard of reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5203317` offsets `473-491`; context: The standard of review on the first issue is reasonableness.
- Evidence: `issue` cue `issue` at chunk `5203318` offsets `684-689`; context: The standard of review on the second issue is reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5203318` offsets `651-669`; context: The standard of review on the second issue is reasonableness.

#### 25572:2:subtheme:3 · paragraphs 20-21

- Raw key terms: `canada, court, decision, falls, outcomes, paragraph, possible, range`
- Display key terms: `falls, outcomes, paragraph, possible, range`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: falls, outcomes, paragraph, possible, range Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5203319` offsets `329-336`; context: Rather, “the reasons must be read together with the outcome and serve the purpose of showing whether the result falls within a range of possible outcomes.
- Evidence: `issue` cue `whether` at chunk `5203320` offsets `219-226`; context: [21] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### 25572:2:subtheme:4 · paragraphs 22-22

- Raw key terms: `above, agrees, analysis, answer, application, applying, bring, canada`
- Display key terms: `above, agrees, analysis, answer, applying, bring`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: above, agrees, analysis, answer, applying, bring Rule/authority context: [22] In Sahota v Canada (Minister of Citizenship and Immigration) 2011 FC 739, Justice Phelan held at paragraph 7 that the application of the proper legal test is reviewable on the correctness standard. Evidence spans paragraphs 22-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5203321` offsets `437-442`; context: The standard of review with respect to the third issue is correctness.
- Evidence: `governing_rule` cue `legal test` at chunk `5203321` offsets `149-159`; context: [22] In Sahota v Canada (Minister of Citizenship and Immigration) 2011 FC 739, Justice Phelan held at paragraph 7 that the application of the proper legal test is reviewable on the correctness standard.

#### Section text

[15] The Applicant raises the following issues in this case:
a) Whether the Officer failed to appropriately assess Omar’s best interests;
b) Whether the Officer’s conclusions were unreasonable;
c) Whether the Officer applied the wrong test for the best interests of the child;
d) Whether the Officer provided adequate reasons.
­
STANDARD OF REVIEW

[16] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[17] In Hawthorne v Canada (Minister of Citizenship and Immigration) 2002 FCA 475, the Federal Court of Appeal held at paragraph 6 that
the officer’s task [in an H&C determination] is to determine, in the circumstances of each case, the likely degree of hardship to the child caused by the removal of the parent and to weigh this degree of hardship together with other factors, including public policy considerations, that militate in favour of or against the removal of the parent.

[18] Further, the Federal Court of Appeal held in Legault v Canada (Minister of Citizenship and Immigration) 2002 FCA 125 at paragraph 12 that, once an officer has identified and defined the best interests of the child, it is up to him to determine what weight those interests must be given in the circumstances. Where the best interests of a child lie is a question of fact which, following Dunsmuir, above, at paragraph 53, will attract a standard of reasonableness. The standard of review on the first issue is reasonableness.

[19] In Baker v Canada (Minister of Citizenship and Immigration), [1999] SCJ No 39, the Supreme Court of Canada held that, when reviewing an H&C decision, “considerable deference should be accorded to immigration Officers exercising the powers conferred by the legislation, given the fact-specific nature of the inquiry, its role within the statutory scheme as an exception, the fact that the decision-maker is the Minister, and the considerable discretion evidenced by the statutory language” (paragraph 62). Justice Michael Phelan followed this approach in Thandal v Canada (Minister of Citizenship and Immigration) 2008 FC 489, at paragraph 7. The standard of review on the second issue is reasonableness.

[20] In Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board) 2011 SCC 62, the Supreme Court of Canada held at paragraph 14 that the adequacy of reasons is not a stand-alone basis for quashing a decision. Rather, “the reasons must be read together with the outcome and serve the purpose of showing whether the result falls within a range of possible outcomes.” The fourth issue in this case, whether the Officer provided adequate reasons, is to be analysed along with the reasonableness of the Decision as a whole.

[21] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at paragraph 47, and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at paragraph 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”

[22] In Sahota v Canada (Minister of Citizenship and Immigration) 2011 FC 739, Justice Phelan held at paragraph 7 that the application of the proper legal test is reviewable on the correctness standard. See also Garcia v Canada (Minister of Citizenship and Immigration) 2010 FC 677 at paragraph 7 and Markis v Canada (Minister of Citizenship and Immigration) 2008 FC 428 at paragraph 19. The standard of review with respect to the third issue is correctness. As the Supreme Court of Canada held in Dunsmuir, above, at paragraph 50,
When applying the correctness standard, a reviewing court will not show deference to the decision maker’s reasoning process; it will rather undertake its own analysis of the question. The analysis will bring the court to decide whether it agrees with the determination of the decision maker; if not, the court will substitute its own view and provide the correct answer. From the outset, the court must ask whether the tribunal’s decision was correct.
STATUTORY PROVISIONS

## 25572:3 · paragraphs 23-72

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6f0426eec834bd2741869a0129c1d5da61f7622d2844a6e3b3367598662e040d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25572:3:subtheme:1 · paragraphs 23-33

- Raw key terms: `applicant, officer, omar, canada, unreasonable, asthma, evidence, says`
- Display key terms: `officer, omar, unreasonable, asthma, says`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: officer, omar, unreasonable, asthma, says Position/evidence statements: [24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada. | [25] The Applicant also points to the letter she submitted to the Officer from Dr. Rule/authority context: [26] In this case, the Officer was under a duty to address the totality of the evidence which was before him, including the factors the Applicant felt were important. Application context: [24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada. | Because the Officer did not address these submissions, the Decision is unreasonable and must be returned for reconsideration. Evidence spans paragraphs 23-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5203322` offsets `1237-1245`; context: ARGUMENTS
The Applicant
The Officer Ignored Evidence
- Evidence: `party_position` cue `argues` at chunk `5203323` offsets `19-25`; context: [24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203323` offsets `88-96`; context: [24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada.
- Evidence: `reasoning_application` cue `because` at chunk `5203323` offsets `60-67`; context: [24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada.
- Evidence: `counterargument_limitation` cue `but` at chunk `5203323` offsets `263-266`; context: She notes that the Officer mentioned Omar’s asthma at page 3 of the Decision, but the Officer did not acknowledge or address her submission that the climate in Grenada makes Omar’s asthma worse than it was in Canada.
- Evidence: `party_position` cue `submitted` at chunk `5203324` offsets `49-58`; context: [25] The Applicant also points to the letter she submitted to the Officer from Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203325` offsets `79-87`; context: [26] In this case, the Officer was under a duty to address the totality of the evidence which was before him, including the factors the Applicant felt were important.
- Evidence: `governing_rule` cue `under` at chunk `5203325` offsets `35-40`; context: [26] In this case, the Officer was under a duty to address the totality of the evidence which was before him, including the factors the Applicant felt were important.
- Evidence: `evidence_fact` cue `found that` at chunk `5203327` offsets `23-33`; context: [28] Here, the Officer found that Omar’s asthma was not severe, but did not compare his condition in Grenada with his condition in Canada.
- Evidence: `reasoning_application` cue `Because` at chunk `5203327` offsets `401-408`; context: Because the Officer did not address these submissions, the Decision is unreasonable and must be returned for reconsideration.
- Evidence: `counterargument_limitation` cue `but` at chunk `5203327` offsets `64-67`; context: [28] Here, the Officer found that Omar’s asthma was not severe, but did not compare his condition in Grenada with his condition in Canada.
- Evidence: `party_position` cue `argues` at chunk `5203328` offsets `24-30`; context: [29] The Applicant also argues that the Officer’s findings that her family would assist in purchasing Omar’s medications, that she is overstating his condition for her own gain, and that Omar’s condition is not severe are all unreasonable.
- Evidence: `party_position` cue `argues` at chunk `5203329` offsets `316-322`; context: The Applicant argues that it is against public policy to hold an enforced removal against an H&C claimant.
- Evidence: `reasoning_application` cue `because` at chunk `5203329` offsets `84-91`; context: [30] The Applicant says that the Officer found she was overstating Omar’s condition because she returned to Grenada without regard to his condition.
- Evidence: `counterargument_limitation` cue `but` at chunk `5203329` offsets `236-239`; context: This finding is unreasonable because she returned to Grenada, not by her own decision, but because she was required to leave by the Canadian government.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203330` offsets `251-259`; context: She points to evidence that Omar has been treated in hospital several times and has to use inhalers daily to control his symptoms.
- Evidence: `reasoning_application` cue `applied` at chunk `5203330` offsets `638-645`; context: It is also unclear what test the Officer applied to establish that Omar’s asthma is not severe.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203331` offsets `204-212`; context: The Officer based this conclusion in part on evidence that the Applicant’s family in Canada would be willing to assist with the cost of a ticket for Omar to Canada if her H&C application was successful.
- Evidence: `reasoning_application` cue `Applied` at chunk `5203331` offsets `870-877`; context: The Officer Applied the Incorrect Test for the Best Interests of the Child
- Evidence: `party_position` cue `argues` at chunk `5203332` offsets `27-33`; context: [33] The Applicant further argues that the Officer applied the wrong test when he analysed Omar’s interest in her H&C application.
- Evidence: `reasoning_application` cue `applied` at chunk `5203332` offsets `51-58`; context: [33] The Applicant further argues that the Officer applied the wrong test when he analysed Omar’s interest in her H&C application.

#### 25572:3:subtheme:2 · paragraphs 34-36

- Raw key terms: `best, canada, interests, above, affected, analysis, applicant, baker`
- Display key terms: `best, interests, above, affected, analysis, baker`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: best, interests, above, affected, analysis, baker Rule/authority context: [34] The jurisprudence clearly establishes that officers considering H&C applications are required to analyse the best interests of children affected by their decisions separately from the hardship analysis. Application context: The Applicant says that, when the Officer said that he was not “satisfied that a removal from [Canada] at this early stage of the child’s life will have a negative impact on the child to the extent where he would suffer  Operative outcome context: In this case, the Officer incorrectly looked at the hardship Omar would suffer if his mother were not granted permanent residence (see Mangru v Canada (Minister of Citizenship and Immigration) 2011 FC 779 at paragraph 24 Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5203333` offsets `9-22`; context: [34] The jurisprudence clearly establishes that officers considering H&C applications are required to analyse the best interests of children affected by their decisions separately from the hardship analysis.
- Evidence: `disposition` cue `granted` at chunk `5203333` offsets `476-483`; context: In this case, the Officer incorrectly looked at the hardship Omar would suffer if his mother were not granted permanent residence (see Mangru v Canada (Minister of Citizenship and Immigration) 2011 FC 779 at paragraph 24).
- Evidence: `reasoning_application` cue `applied` at chunk `5203334` offsets `532-539`; context: The Applicant says that, when the Officer said that he was not “satisfied that a removal from [Canada] at this early stage of the child’s life will have a negative impact on the child to the extent where he would suffer undue and undeserved or disproportionate hardship,” the Officer applied the incorrect test in assessing Omar’s best interests.

#### 25572:3:subtheme:3 · paragraphs 37-41

- Raw key terms: `best, interests, officer, above, applicant, applications, canada, omar`
- Display key terms: `best, interests, officer, above, applications, omar`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: best, interests, officer, above, applications, omar Rule/authority context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ Application context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ Operative outcome context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ | The Officer addressed the Applicant’s concerns that Omar would be in Phillip’s presence, would be denied access to education, and would not have access to medical care. Evidence spans paragraphs 37-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5203336` offsets `197-204`; context: In this case, the Officer was required to consider whether Omar’s best interests were served by allowing him to come to Canada with his mother or by forcing him to remain with her in Grenada; the Officer was not required to decide whether Omar was suffering in Grenada or that he would suffer less in Canada.
- Evidence: `counterargument_limitation` cue `However` at chunk `5203337` offsets `120-127`; context: However, she also notes that in Baker, above, Justice Claire L’Heureux-Dubé held at paragraph 75 that
[…]where the interests of children are minimized, in a manner inconsistent with Canada’s humanitarian and compassionate tradition and the Minister’s guidelines, the decision will be unreasonable.
- Evidence: `governing_rule` cue `under` at chunk `5203339` offsets `328-333`; context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ No 1906 at paragraph 12).
- Evidence: `reasoning_application` cue `Because` at chunk `5203339` offsets `284-291`; context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ No 1906 at paragraph 12).
- Evidence: `disposition` cue `granted` at chunk `5203339` offsets `390-397`; context: Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ No 1906 at paragraph 12).
- Evidence: `evidence_fact` cue `found that` at chunk `5203340` offsets `644-654`; context: Although the Applicant feared these risks, the Officer reasonably found that they had not materialized in Grenada.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5203340` offsets `578-586`; context: Although the Applicant feared these risks, the Officer reasonably found that they had not materialized in Grenada.
- Evidence: `disposition` cue `denied` at chunk `5203340` offsets `507-513`; context: The Officer addressed the Applicant’s concerns that Omar would be in Phillip’s presence, would be denied access to education, and would not have access to medical care.

#### 25572:3:subtheme:4 · paragraphs 42-45

- Raw key terms: `officer, omar, although, applicant, condition, canada, climate, considered`
- Display key terms: `officer, omar, although, condition, climate, considered`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: officer, omar, although, condition, climate, considered Position/evidence statements: [45] Although the Respondent has argued that the Officer considered the Applicant’s submissions on the impact of the Grenadian climate on Omar’s condition, the Applicant says that he merely mentioned her concerns without Application context: Though this may suggest that he applied the incorrect test, the Respondent notes that Justice Russel Zinn held in Segura v Canada (Minister of Citizenship and Immigration) 2009 FC 894 that using the language of hardship  Evidence spans paragraphs 42-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5203341` offsets `47-53`; context: [42] The Officer also adequately canvassed the issues surrounding Omar’s medical condition.
- Evidence: `evidence_fact` cue `found that` at chunk `5203341` offsets `198-208`; context: Although the climate in Grenada makes Omar’s condition worse and his medication is expensive, the Officer found that the evidence showed his asthma is being treated.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5203341` offsets `92-100`; context: Although the climate in Grenada makes Omar’s condition worse and his medication is expensive, the Officer found that the evidence showed his asthma is being treated.
- Evidence: `issue` cue `whether` at chunk `5203342` offsets `410-417`; context: What matters is “whether it can be said on a reading of the decision as a whole that the Officer applied the correct test and conducted a proper analysis.
- Evidence: `reasoning_application` cue `applied` at chunk `5203342` offsets `152-159`; context: Though this may suggest that he applied the incorrect test, the Respondent notes that Justice Russel Zinn held in Segura v Canada (Minister of Citizenship and Immigration) 2009 FC 894 that using the language of hardship does not automatically result in a reviewable error.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203343` offsets `94-102`; context: Given the evidence before him the Officer reasonably found that the Applicant’s situation did not warrant granting permanent residence on H&C grounds.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5203343` offsets `235-243`; context: Although Omar would have easier access to the medicine he needs and better education in Canada, these factors alone do not mean that the Decision was unreasonable.
- Evidence: `party_position` cue `argued` at chunk `5203344` offsets `33-39`; context: [45] Although the Respondent has argued that the Officer considered the Applicant’s submissions on the impact of the Grenadian climate on Omar’s condition, the Applicant says that he merely mentioned her concerns without actually addressing them.

#### 25572:3:subtheme:5 · paragraphs 46-48

- Raw key terms: `applicant, omar, says, affected, best, children, exemptions, interests`
- Display key terms: `omar, says, affected, best, children, exemptions, interests`
- Argument roles: `counterargument_limitation, disposition, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, reasoning_application Display terms: omar, says, affected, best, children, exemptions, interests Application context: In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history. Operative outcome context: In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history. Evidence spans paragraphs 46-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5203345` offsets `133-140`; context: Whether asthma is common or not has no bearing on how Omar’s asthma is affected by the Grenadian climate, which was a key feature of the Applicant’s H&C application.
- Evidence: `reasoning_application` cue `because` at chunk `5203347` offsets `685-692`; context: In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5203347` offsets `747-762`; context: In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history.
- Evidence: `disposition` cue `allowed` at chunk `5203347` offsets `657-664`; context: In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history.

#### 25572:3:subtheme:6 · paragraphs 49-51

- Raw key terms: `above, best, interests, officer, affected, applicant, application, canada`
- Display key terms: `above, best, interests, officer, affected`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: above, best, interests, officer, affected Application context: Further, Segura is distinguishable because Omar faces challenges related to his asthma that are not typically faced by children who are removed from Canada with their parents. | Rather, she has asserted that the Officer ignored her submissions and applied the wrong test for the best interests of a child directly affected by the Decision, which are reviewable errors. Operative outcome context: Here, the Officer summarily dismissed Omar’s condition without considering its seriousness and how it was affected by the climate in Grenada. Evidence spans paragraphs 49-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5203348` offsets `447-454`; context: The Officer also ignored the Applicant’s submissions and made no finding on whether the change in environment had jeopardized Omar’s health and well-being.
- Evidence: `disposition` cue `dismissed` at chunk `5203348` offsets `257-266`; context: Here, the Officer summarily dismissed Omar’s condition without considering its seriousness and how it was affected by the climate in Grenada.
- Evidence: `issue` cue `whether` at chunk `5203349` offsets `245-252`; context: However, the Officer’s analysis of Omar’s situation explicitly considered whether denying the H&C application would cause Omar unusual and undeserved or disproportionate hardship without looking at what was in his best interests.
- Evidence: `reasoning_application` cue `because` at chunk `5203349` offsets `436-443`; context: Further, Segura is distinguishable because Omar faces challenges related to his asthma that are not typically faced by children who are removed from Canada with their parents.
- Evidence: `counterargument_limitation` cue `However` at chunk `5203349` offsets `171-178`; context: However, the Officer’s analysis of Omar’s situation explicitly considered whether denying the H&C application would cause Omar unusual and undeserved or disproportionate hardship without looking at what was in his best interests.
- Evidence: `evidence_fact` cue `evidence` at chunk `5203350` offsets `115-123`; context: [51] The Applicant also says that her application for judicial review does not amount to a request to re-weigh the evidence already considered.
- Evidence: `reasoning_application` cue `applied` at chunk `5203350` offsets `214-221`; context: Rather, she has asserted that the Officer ignored her submissions and applied the wrong test for the best interests of a child directly affected by the Decision, which are reviewable errors.

#### 25572:3:subtheme:7 · paragraphs 52-53

- Raw key terms: `applicant, climate, condition, consider, considered, grenadian, impact, officer`
- Display key terms: `climate, condition, consider, considered, grenadian, impact, officer`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: climate, condition, consider, considered, grenadian, impact, officer Application context: [52] The Applicant takes issue with the Respondent’s argument that the Decision was reasonable because Omar has access to schooling and medical care in Grenada. Operative outcome context: She says that the Officer summarily dismissed Omar’s condition as common without appreciating the impact of the Grenadian climate. Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5203351` offsets `25-30`; context: [52] The Applicant takes issue with the Respondent’s argument that the Decision was reasonable because Omar has access to schooling and medical care in Grenada.
- Evidence: `reasoning_application` cue `because` at chunk `5203351` offsets `95-102`; context: [52] The Applicant takes issue with the Respondent’s argument that the Decision was reasonable because Omar has access to schooling and medical care in Grenada.
- Evidence: `disposition` cue `dismissed` at chunk `5203352` offsets `165-174`; context: She says that the Officer summarily dismissed Omar’s condition as common without appreciating the impact of the Grenadian climate.

#### 25572:3:subtheme:8 · paragraphs 54-63

- Raw key terms: `best, interests, officer, decision, child, disproportionate, hardship, undeserved`
- Display key terms: `best, interests, officer, child, disproportionate, hardship, undeserved`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: best, interests, officer, child, disproportionate, hardship, undeserved Rule/authority context: If the Decision is read as a whole, it seems to me that the Officer was not really aware of what a best interest analysis requires or of the legal principles that must be applied. | [56] I agree with the Applicant that the Officer in the present matter has committed the very error contemplated in the jurisprudence from this Court I have quoted above and the Decision of the Federal Court of Appeal in Application context: If the Decision is read as a whole, it seems to me that the Officer was not really aware of what a best interest analysis requires or of the legal principles that must be applied. | [55] It is clear on the face of the Decision that the Officer has applied the wrong test in assessing the best interests of the child. Evidence spans paragraphs 54-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5203353` offsets `34-40`; context: [54] The Applicant raises several issues but there is a fundamental problem with this Decision that requires it be returned for reconsideration.
- Evidence: `governing_rule` cue `principles` at chunk `5203353` offsets `292-302`; context: If the Decision is read as a whole, it seems to me that the Officer was not really aware of what a best interest analysis requires or of the legal principles that must be applied.
- Evidence: `reasoning_application` cue `applied` at chunk `5203353` offsets `316-323`; context: If the Decision is read as a whole, it seems to me that the Officer was not really aware of what a best interest analysis requires or of the legal principles that must be applied.
- Evidence: `reasoning_application` cue `applied` at chunk `5203354` offsets `66-73`; context: [55] It is clear on the face of the Decision that the Officer has applied the wrong test in assessing the best interests of the child.
- Evidence: `counterargument_limitation` cue `however` at chunk `5203354` offsets `299-306`; context: He makes the following statements that constitute the basis of his analysis:
Her child, a four-year-old Canadian citizen had just started JK and making new friends however I am not satisfied that a removal from this setting at this early stage in the child’s life will have a negative impact on the child to the extend (sic) where he would suffer undue and undeserved or disproportionate hardship.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5203355` offsets `120-133`; context: [56] I agree with the Applicant that the Officer in the present matter has committed the very error contemplated in the jurisprudence from this Court I have quoted above and the Decision of the Federal Court of Appeal in Hawthorne.
- Evidence: `reasoning_application` cue `applied` at chunk `5203355` offsets `874-881`; context: ” It may not be an error to use the language of hardship, but the Officer here went one step further and applied hardship as the test for Omar’s interests.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5203356` offsets `99-112`; context: [57] I agree with the Applicant’s characterization of the problem and her account of the governing jurisprudence and adopt them for purposes of these reasons.
- Evidence: `reasoning_application` cue `applied` at chunk `5203358` offsets `530-537`; context: This standard is only to be applied to the assessment of hardship experienced by an applicant from having to apply for admission to Canada from overseas; it does not apply to the assessment of the best interests of a child affected by the removal of a parent.
- Evidence: `reasoning_application` cue `apply` at chunk `5203359` offsets `270-275`; context: [60] Similarly, this Court stated in Arulraj, above, at paragraph 14 that
[…] terms found in the IP5 Guidelines of “unusual”, “undeserved” or “disproportionate” are used in the context of considering an applicant’s H & C interests in staying in Canada and not having to apply for landing from abroad.
- Evidence: `evidence_fact` cue `found that` at chunk `5203361` offsets `26-36`; context: [62] In Mangru, the Court found that, in addition to incorrectly describing the test involved in determining the best interest of the children impacted by the decision, the officer had minimized the impact on the children of being forced to leave Canada to accompany their parents to Guyana.

#### 25572:3:subtheme:9 · paragraphs 64-69

- Raw key terms: `interests, alive, best, child, sensitive, alert, consideration, court`
- Display key terms: `interests, alive, best, child, sensitive, alert, consideration`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: interests, alive, best, child, sensitive, alert, consideration Rule/authority context: [68] In Baker, above, the Supreme Court of Canada held that for the exercise of discretion under subsection 25(1) of the Act to fall within the standard of reasonableness, the decision-maker must consider the child’s bes Application context: As a result, a threshold test of undeserved or undue hardship or a threshold “basic needs” approach to a best interests analysis, like that applied by the Officer in this case, does not adequately determine – in a way th | I conclude that because the reasons for this decision do not indicate that it was made in a manner which was alive, attentive, or sensitive to the interests of Ms. Operative outcome context: [65] For example, officers should not discontinue their consideration of what is in a child’s best interests after determining that the child is not being beaten or malnourished, or, as in the present decision, is not be Evidence spans paragraphs 64-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5203363` offsets `344-352`; context: The question is not: “is the child suffering enough that his “best interests” are not being “met”?
- Evidence: `disposition` cue `denied` at chunk `5203364` offsets `233-239`; context: [65] For example, officers should not discontinue their consideration of what is in a child’s best interests after determining that the child is not being beaten or malnourished, or, as in the present decision, is not being outright denied medical care.
- Evidence: `reasoning_application` cue `applied` at chunk `5203365` offsets `320-327`; context: As a result, a threshold test of undeserved or undue hardship or a threshold “basic needs” approach to a best interests analysis, like that applied by the Officer in this case, does not adequately determine – in a way that is “alert, alive and sensitive” – what is in the child’s best interest.
- Evidence: `governing_rule` cue `under` at chunk `5203367` offsets `91-96`; context: [68] In Baker, above, the Supreme Court of Canada held that for the exercise of discretion under subsection 25(1) of the Act to fall within the standard of reasonableness, the decision-maker must consider the child’s best interests as an important factor, give them substantial weight, and be alert, alive and sensitive to them.
- Evidence: `counterargument_limitation` cue `However` at chunk `5203367` offsets `841-848`; context: However, where the interests of children are minimized, in a manner inconsistent with Canada's humanitarian and compassionate tradition and the Minister's guidelines, the decision will be unreasonable.
- Evidence: `reasoning_application` cue `conclude` at chunk `5203368` offsets `364-372`; context: I conclude that because the reasons for this decision do not indicate that it was made in a manner which was alive, attentive, or sensitive to the interests of Ms.

#### 25572:3:subtheme:10 · paragraphs 70-71

- Raw key terms: `above, decision, officer, able, accordance, added, articulate, best`
- Display key terms: `above, officer, able, accordance, added, articulate, best`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: above, officer, able, accordance, added, articulate, best Rule/authority context: [71] The Decision is therefore returned for a new officer to consider in accordance with the above principles. Application context: [71] The Decision is therefore returned for a new officer to consider in accordance with the above principles. Evidence spans paragraphs 70-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5203369` offsets `522-529`; context: To demonstrate sensitivity, the officer must be able to clearly articulate the suffering of a child that will result from a negative decision, and then say whether, together with a consideration of other factors, the suffering warrants humanitarian and compassionate relief.
- Evidence: `governing_rule` cue `principles` at chunk `5203370` offsets `99-109`; context: [71] The Decision is therefore returned for a new officer to consider in accordance with the above principles.
- Evidence: `reasoning_application` cue `therefore` at chunk `5203370` offsets `21-30`; context: [71] The Decision is therefore returned for a new officer to consider in accordance with the above principles.

#### 25572:3:subtheme:11 · paragraphs 72-72

- Raw key terms: `agree, certification, concurs, counsel, court, issue`
- Display key terms: `agree, certification, concurs`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, certification, concurs Evidence spans paragraphs 72-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5203371` offsets `31-36`; context: [72] Counsel agree there is no issue for certification and the Court concurs.

#### Section text

[23] The following provision of the Act is applicable in this proceeding:
25. (1) The Minister must, on request of a foreign national in Canada who is inadmissible
or who does not meet the requirements of this Act, and may, on request of a foreign national outside Canada, examine the circumstances
concerning the foreign national and may grant the foreign national permanent resident status or an exemption from any applicable criteria or
obligations of this Act if the Minister is of the opinion that it is justified by humanitarian and compassionate considerations relating to the
foreign national, taking into account the best interests of a child directly affected
25. (1) Le ministre doit, sur demande d’un étranger se trouvant au Canada qui est interdit de territoire ou qui ne se conforme pas à la présente
loi, et peut, sur demande d’un étranger se trouvant hors du Canada, étudier le cas de cet
étranger; il peut lui octroyer le statut de résident permanent ou lever tout ou partie des critères
et obligations applicables, s’il estime que des considérations d’ordre humanitaire relatives
à l’étranger le justifient, compte tenu de l’intérêt supérieur de l’enfant directement touché.
ARGUMENTS
The Applicant
The Officer Ignored Evidence

[24] The Applicant argues that the Decision is unreasonable because the Officer ignored evidence before him that the severity of Omar’s asthma is exacerbated by the climate in Grenada. She notes that the Officer mentioned Omar’s asthma at page 3 of the Decision, but the Officer did not acknowledge or address her submission that the climate in Grenada makes Omar’s asthma worse than it was in Canada. The Applicant points to her written submissions of 5 April 2011 in which she wrote that
Omar has been hospitalized several times due to his severe asthma attacks […] Living in Grenada has not only increased the severity of Omar’s asthma attacks, but has also put his life at risk for not being able to access the inhalers he needs.

[25] The Applicant also points to the letter she submitted to the Officer from Dr. Thomas which shows that Omar has been treated regularly in hospital for his asthma.

[26] In this case, the Officer was under a duty to address the totality of the evidence which was before him, including the factors the Applicant felt were important. The Applicant points to Citizen and Immigration Canada’s (CIC) IP5 Manual – Immigrant Applications in Canada made on Humanitarian and Compassionate Grounds – which says at page 69 that
An officer should consider and weigh all the relevant evidence and information, including what the applicant and the officer consider to be important. Officers must not ignore evidence or place too much emphasis on one factor to the exclusion of all other factors.
They must look at the whole picture.

[27] The Applicant says that in Curry v Canada (Minister of Citizenship and Immigration) 2006 FC 1350, Justice Douglas Campbell held at paragraph 10 that it was not fair or proper for an officer to act contrary to the IP5 Manual and not consider all the factors before him or her.

[28] Here, the Officer found that Omar’s asthma was not severe, but did not compare his condition in Grenada with his condition in Canada. The submissions the Applicant made on the worsening of Omar’s symptoms were so important that the Officer was required to address them directly in the Decision (see Ozdemir v Canada (Minister of Citizenship and Immigration) 2001 FCA 331 at paragraphs 9 and 10). Because the Officer did not address these submissions, the Decision is unreasonable and must be returned for reconsideration.
The Officer’s Findings Were Unreasonable

[29] The Applicant also argues that the Officer’s findings that her family would assist in purchasing Omar’s medications, that she is overstating his condition for her own gain, and that Omar’s condition is not severe are all unreasonable.

[30] The Applicant says that the Officer found she was overstating Omar’s condition because she returned to Grenada without regard to his condition. This finding is unreasonable because she returned to Grenada, not by her own decision, but because she was required to leave by the Canadian government. The Applicant argues that it is against public policy to hold an enforced removal against an H&C claimant. To do so would encourage people with pending H&C applications who are also subject to removal orders to do all they can to avoid removal because removal would negatively impact their H&C applications. The Applicant also notes that her return to Grenada in 2003 occurred before Omar first experienced asthma symptoms. Further, she could not have foreseen the impact that the Grenadian climate would have on Omar when they returned to Grenada in 2007.

[31] The Officer also made an unreasonable finding when he concluded that Omar’s asthma is not severe and that asthma is a common condition; the Applicant says that this is an improper basis for finding that Omar’s asthma is not severe. She points to evidence that Omar has been treated in hospital several times and has to use inhalers daily to control his symptoms. The Officer’s reasons do not show that he considered these facts or how they affected the Decision. Omar’s medical condition was an important aspect of the application, so the Officer should have thoroughly canvassed this point. It is also unclear what test the Officer applied to establish that Omar’s asthma is not severe.

[32] The Applicant also challenges the Officer’s finding that she will be able to afford Omar’s medication if she gives it the priority it appears to deserve. The Officer based this conclusion in part on evidence that the Applicant’s family in Canada would be willing to assist with the cost of a ticket for Omar to Canada if her H&C application was successful. He found this showed that they would also be willing to assist with the cost of Omar’s medication if the H&C application was not successful. The Applicant says that it was unreasonable for the Officer to equate her family’s willingness to assist with a return airfare to Canada with a continuing ability and willingness to help her buy medicine for Omar. She notes that her family members in Canada have children of their own, so they may not be able to continue to help with Omar’s medications.
The Officer Applied the Incorrect Test for the Best Interests of the Child

[33] The Applicant further argues that the Officer applied the wrong test when he analysed Omar’s interest in her H&C application. She notes that in Shchegolevich v Canada (Minister of Citizenship and Immigration) 2008 FC 527, Justice Robert Barnes wrote at paragraph 12 that
It is clear that the Officer erred by requiring that Mr. Schegolevich establish that the adverse effects of his removal upon his spouse and his stepson would be unusual, undeserved, or disproportionate. This standard is only to be applied to the assessment of hardship experienced by an applicant from having to apply for admission to Canada from overseas; it does not apply to the assessment of the best interests of a child affected by the removal of a parent.

[34] The jurisprudence clearly establishes that officers considering H&C applications are required to analyse the best interests of children affected by their decisions separately from the hardship analysis. Officers must also be alert, alive, and sensitive to those interests (see Baker, above, and Kolosovs v Canada (Minister of Citizenship and Immigration) 2008 FC 165). In this case, the Officer incorrectly looked at the hardship Omar would suffer if his mother were not granted permanent residence (see Mangru v Canada (Minister of Citizenship and Immigration) 2011 FC 779 at paragraph 24).

[35] As in Mangru, “the application of the unusual and undeserved or disproportionate hardship threshold permeates [the Officer’s] analysis of the best interests of the [child] and results in an inappropriate conclusion” (Mangru, at paragraph 27). The Applicant says that, when the Officer said that he was not “satisfied that a removal from [Canada] at this early stage of the child’s life will have a negative impact on the child to the extent where he would suffer undue and undeserved or disproportionate hardship,” the Officer applied the incorrect test in assessing Omar’s best interests.

[36] The Applicant relies on Kolosovs, Baker, and Shchegolevich, all above, Owusu v Canada (Minister of Citizenship and Immigration) 2004 FCA 38, Arulraj v Canada (Minister of Citizenship and Immigration) 2006 FC 529, and Hawthorne, above, and says that, when officers assess the best interests of children affected by H&C decisions, they must
a. Establish what is in the best interests of the children;
b. Assess the degree to which those interests are compromised by all the decisions contemplated; and
c. Determine the weight the best interests of the children will play in the H&C assessment.

[37] The Applicant also says that there is no minimum level of suffering a child must experience in order to ground a positive H&C determination. In this case, the Officer was required to consider whether Omar’s best interests were served by allowing him to come to Canada with his mother or by forcing him to remain with her in Grenada; the Officer was not required to decide whether Omar was suffering in Grenada or that he would suffer less in Canada. The Officer did not consider the right question.

[38] The Applicant acknowledges that the best interests of a child directly affected are not necessarily determinative. However, she also notes that in Baker, above, Justice Claire L’Heureux-Dubé held at paragraph 75 that
[…]where the interests of children are minimized, in a manner inconsistent with Canada’s humanitarian and compassionate tradition and the Minister’s guidelines, the decision will be unreasonable.

[39] The Officer committed the error Justice L’Heureux-Dubé identified in Baker, so the Decision must be returned for reconsideration.
The Respondent
H&C Applications are Exceptional and Discretionary

[40] The Respondent draws the Court’s attention to the principle that H&C exemptions are not designed to eliminate all hardship arising out of the requirements of the Act. Rather, section 25 of the Act is aimed at eliminating only unusual and undeserved or disproportionate hardship. Because of the exceptional nature of relief under section 25, applicants must meet a high threshold to be granted an exemption under that section (see Irimie v Canada (Minister of Citizenship and Immigration), [2000] FCJ No 1906 at paragraph 12). Applicants must also demonstrate all of the positive ingredients in their applications (see Owusu, above).
The Officer Adequately Considered Omar’s Best Interests

[41] In Hawthorne, above, the Federal Court of Appeal held at paragraph 6 that the task faced by an H&C officer is to weigh the hardship faced by the applicants along with all the other positive and negative ingredients in their applications. In this case, the Officer thoroughly considered where Omar’s best interests lay and weighed these against the other positive and negative factors in the application. The Officer addressed the Applicant’s concerns that Omar would be in Phillip’s presence, would be denied access to education, and would not have access to medical care. Although the Applicant feared these risks, the Officer reasonably found that they had not materialized in Grenada.

[42] The Officer also adequately canvassed the issues surrounding Omar’s medical condition. Although the climate in Grenada makes Omar’s condition worse and his medication is expensive, the Officer found that the evidence showed his asthma is being treated. This finding was reasonable. Further, the Applicant did not provide objective evidence to prove that Omar’s medication is expensive or that his condition is severe.

[43] The Officer said that removal to Grenada would not cause Omar unusual and undeserved or disproportionate hardship. Though this may suggest that he applied the incorrect test, the Respondent notes that Justice Russel Zinn held in Segura v Canada (Minister of Citizenship and Immigration) 2009 FC 894 that using the language of hardship does not automatically result in a reviewable error. What matters is “whether it can be said on a reading of the decision as a whole that the Officer applied the correct test and conducted a proper analysis.” (see paragraph 29).

[44] In this case, the Decision shows that the Officer considered Omar’s condition. Given the evidence before him the Officer reasonably found that the Applicant’s situation did not warrant granting permanent residence on H&C grounds. Although Omar would have easier access to the medicine he needs and better education in Canada, these factors alone do not mean that the Decision was unreasonable. The Applicant’s submissions in this case amount only to an invitation to the Court to re-weigh the factors that the Officer considered which is improper on judicial review.
The Applicant’s Reply

[45] Although the Respondent has argued that the Officer considered the Applicant’s submissions on the impact of the Grenadian climate on Omar’s condition, the Applicant says that he merely mentioned her concerns without actually addressing them. This failure to consider her submissions is a reviewable error.

[46] The Applicant also says that the Officer’s statement that asthma is a common condition was irrelevant to the H&C determination. Whether asthma is common or not has no bearing on how Omar’s asthma is affected by the Grenadian climate, which was a key feature of the Applicant’s H&C application. The Officer made this statement without addressing the severity of Omar’s condition and how it was affected by the climate in Grenada. This is a reviewable error.

[47] The Respondent has said that H&C exemptions are exceptional and discretionary. The Applicant agrees and says that, in exercising this discretion, officers must give a great deal of attention to the best interests of children affected by their decisions (see Legault, above, at paragraph 11). The Officer here did not pay sufficient attention to Omar’s interests.

[48] As the Respondent has noted, H&C exemptions are intended to relieve unusual and undeserved or disproportionate hardship; the Applicant says that hers is a case where unusual and undeserved or disproportionate hardship will arise out of the operation of the Act. While it is true that leaving a job or family in Canada do not necessarily constitute unusual and undeserved or disproportionate hardship, applying this reasoning would cause Omar to suffer. The Applicant points to ZH (Tanzania) (FC) v Secretary of State for the Home Department, [2011] UKSC 4, a decision from the UK Supreme Court. In that case, the UK Supreme Court held that a parent be allowed to remain in the UK because her children’s best interests lay in remaining there, notwithstanding the parent’s “appalling immigration history.” The Applicant says her case should be similarly decided.
Best Interests of the Child

[49] Although Hawthorne, above, teaches that there is no set formula for considering the best interests of children affected by H&C decisions, it is still an error for officers to summarily dismiss concerns relating to children. Here, the Officer summarily dismissed Omar’s condition without considering its seriousness and how it was affected by the climate in Grenada. The Officer also ignored the Applicant’s submissions and made no finding on whether the change in environment had jeopardized Omar’s health and well-being.

[50] As the Respondent has noted, Segura, above, teaches that the use of hardship in describing the impact of a decision on children is not a reviewable error on its own. However, the Officer’s analysis of Omar’s situation explicitly considered whether denying the H&C application would cause Omar unusual and undeserved or disproportionate hardship without looking at what was in his best interests. Further, Segura is distinguishable because Omar faces challenges related to his asthma that are not typically faced by children who are removed from Canada with their parents. The Officer’s summary dismissal of Omar’s condition shows that his analysis of Omar’s best interests was deficient in both form and substance. Though he mentioned the impact of the Grenadian climate on Omar’s asthma, the Officer did not weigh this factor as he was bound to do.

[51] The Applicant also says that her application for judicial review does not amount to a request to re-weigh the evidence already considered. Rather, she has asserted that the Officer ignored her submissions and applied the wrong test for the best interests of a child directly affected by the Decision, which are reviewable errors. She notes that in Kisana v Canada (Minister of Citizenship and Immigration) 2009 FCA 189, the Federal Court of Appeal quoted from Legault, above, and held at paragraph 24 that
It is not for the courts to reweigh the factors considered by an H&C officer. On the other hand, an officer is required to examine the best interests of the child "with care" and weigh them against other factors. Mere mention that the best interests of the child has been considered will not be sufficient
The Applicant’s Further Memorandum

[52] The Applicant takes issue with the Respondent’s argument that the Decision was reasonable because Omar has access to schooling and medical care in Grenada. She says that the Respondent has not addressed the fact that Omar’s need for medical care would be reduced if he were removed from the Grenadian climate to Canada. She also says that the Respondent’s argument that the Officer considered Omar’s condition is incorrect; he did not consider the impact of the Grenadian climate on Omar’s condition. The Officer only noted her submissions without considering them. He did not engage with those submissions.

[53] The Applicant also disagrees with the Respondent’s contention that the Officer adequately considered Omar’s best interests. She says that the Officer summarily dismissed Omar’s condition as common without appreciating the impact of the Grenadian climate. He also did not consider the impact the Applicant’s financial difficulties had on Omar’s condition.
ANALYSIS

[54] The Applicant raises several issues but there is a fundamental problem with this Decision that requires it be returned for reconsideration. If the Decision is read as a whole, it seems to me that the Officer was not really aware of what a best interest analysis requires or of the legal principles that must be applied. The Respondent says that this is merely a matter of form and not substance, and that I should not be swayed by the Officer’s misstatements. I disagree.

[55] It is clear on the face of the Decision that the Officer has applied the wrong test in assessing the best interests of the child. He makes the following statements that constitute the basis of his analysis:
Her child, a four-year-old Canadian citizen had just started JK and making new friends however I am not satisfied that a removal from this setting at this early stage in the child’s life will have a negative impact on the child to the extend (sic) where he would suffer undue and undeserved or disproportionate hardship. [Emphasis added]
…
Considering all the submissions and history of this case, I am not satisfied that subject nor her son, are suffering undue and undeserved nor disproportionate hardship in Granada to the degree that this application should be considered favorably. [Emphasis added]

[56] I agree with the Applicant that the Officer in the present matter has committed the very error contemplated in the jurisprudence from this Court I have quoted above and the Decision of the Federal Court of Appeal in Hawthorne. Rather than being alert, alive and sensitive to Omar’s circumstances and viewing the situation from his perspective, as the jurisprudence requires, the Officer has instead concluded that: “I a

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 25572:4 · paragraphs 73-74

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f3359d1d7099355405f259c941a7c286bbdffef184cde7b77044311c1f259301`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25572:4:subtheme:1 · paragraphs 73-74

- Raw key terms: `allowed, applicant, application, cause, certification, citizenship, counsel, court`
- Display key terms: `allowed, certification`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allowed, certification No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 73-74. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application is allowed, the Decision is quashed and the matter is returned for reconsideration by a different officer.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-2949-11

STYLE OF CAUSE: ERLINA MARY WILLIAMS
Applicant
- and -
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: January 10, 2012
REASONS FOR 

## 25572:5 · paragraphs 75-75

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6c975f66444f9ff33e2bd6d165dfbbe5dd98253cdef13a012d38ede76c2d258d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25572:5:subtheme:1 · paragraphs 75-75

- Raw key terms: `appearances, applicant, attorney, barrister, canada, cham, dated, deputy`
- Display key terms: `barrister, cham, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, cham, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 75-75. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: HON. MR. JUSTICE RUSSELL
DATED: February 7, 2012
APPEARANCES:
Geraldine Sadoway APPLICANT
Veronica Cham RESPONDENT
SOLICITORS OF RECORD:
Geraldine Sadoway APPLICANT
Barrister & Solicitor
Toronto, Ontario
Myles J. Kirvan RESPONDENT
Deputy Attorney General of Canada
