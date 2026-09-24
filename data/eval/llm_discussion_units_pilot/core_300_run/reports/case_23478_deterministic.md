# Discussion Units: case 23478

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **95**
- Continuity pairs: **94**
- Discussion Units: **5**
- Paragraph source hashes: **95**
- Sub-themes: **24**

## 23478:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9279e39a47206a6f25a5c3424cee0d62bac73c0b21c52212d55656ec19be99c7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23478:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, canada, claim, decision, ethnicity, hungary, immigration, reasons`
- Display key terms: `ethnicity, hungary`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: ethnicity, hungary Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c 27 (Act) for judicial review of the decision of the Refugee Protection Division (RPD) of the Immigration and Re Application context: The Applicant was refused entry to public places because of his ethnicity, and had trouble finding work. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5102759` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c 27 (Act) for judicial review of the decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated 7 May 2012 (Decision), which refused the Applicant’s application to be deemed a Convention refugee or a person in need of protection under sections 96 and 97 of the Act.
- Evidence: `reasoning_application` cue `because` at chunk `5102761` offsets `371-378`; context: The Applicant was refused entry to public places because of his ethnicity, and had trouble finding work.

#### 23478:1:subtheme:2 · paragraphs 5-23

- Raw key terms: `applicant, claim, credibility, testimony, further, hearing, hohots, found`
- Display key terms: `credibility, testimony, further, hearing, hohots`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, testimony, further, hearing, hohots Position/evidence statements: Hohots to the RPD on 22 December 2009 to explain why the Applicant’s PIF was submitted late says that “we were working to obtain the Legal Aid certificate for this family. | [16] The Applicant explained that his PIF was written on the day it was due to be submitted and that he did not know what to do, and did not know he could amend his narrative. Rule/authority context: DECISION UNDER REVIEW | [14] By Decision dated 7 May 2012, the RPD determined that, pursuant to subsection 107(2) of the Act, there was no credible basis for the Applicant’s claim, and thus he was not entitled to refugee protection. Application context: Because he was Roma, the teacher gave the Applicant a severe slap to the face. | He reported the incident to his teachers but they did nothing because he is Roma. Evidence spans paragraphs 5-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `5102763` offsets `484-492`; context: The amended PIF was translated to the Applicant before he signed it, but Question 31 of the PIF form was not read to him.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102763` offsets `376-379`; context: The Applicant inquired about adding more information, but he was advised not to do this.
- Evidence: `issue` cue `whether` at chunk `5102764` offsets `144-151`; context: He also asked him some general questions, such as whether he had any brothers or sisters.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102765` offsets `228-231`; context: Uppal asked the Applicant some questions about the reason for his claim, but did not ask for a full account of the events causing him to flee Hungary.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102766` offsets `144-152`; context: Uppal submitted into evidence was a document about country conditions in Hungary.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5102767` offsets `196-205`; context: The Affidavit of Karina Azanza lays out the details of this complaint.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5102768` offsets `346-355`; context: Hohots indicates that the Applicant himself was often not diligent and missed a number of appointments (see Exhibit K of the Affidavit of Karina Azanza).
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5102769` offsets `80-89`; context: Uppal’s response to the LSUC dated 20 August 2012 (Exhibit B of the Affidavit of Karina Azanza), he says that he met with the Applicant twice: on 27 February 2012 and on 6 March 2012, each time for an hour to prepare for the hearing.
- Evidence: `party_position` cue `submitted` at chunk `5102770` offsets `169-178`; context: Hohots to the RPD on 22 December 2009 to explain why the Applicant’s PIF was submitted late says that “we were working to obtain the Legal Aid certificate for this family.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `5102770` offsets `307-316`; context: ” The Legal Aid Certificate (page 94 of the Affidavit of Karina Azanza) says that it was issued on 24 November 2009.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102771` offsets `157-165`; context: Uppal has presented no evidence such as notes from the meetings in support of this.
- Evidence: `governing_rule` cue `UNDER` at chunk `5102771` offsets `405-410`; context: DECISION UNDER REVIEW
- Evidence: `counterargument_limitation` cue `but` at chunk `5102771` offsets `292-295`; context: Hohots says that he did advise the Applicant to obtain documentation, but the Applicant says that Mr.
- Evidence: `evidence_fact` cue `determined that` at chunk `5102772` offsets `43-58`; context: [14] By Decision dated 7 May 2012, the RPD determined that, pursuant to subsection 107(2) of the Act, there was no credible basis for the Applicant’s claim, and thus he was not entitled to refugee protection.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5102772` offsets `60-71`; context: [14] By Decision dated 7 May 2012, the RPD determined that, pursuant to subsection 107(2) of the Act, there was no credible basis for the Applicant’s claim, and thus he was not entitled to refugee protection.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102773` offsets `112-121`; context: [15] The RPD noted that throughout the hearing there was a number of discrepancies between the Applicant’s oral testimony and the information contained in his PIF.
- Evidence: `party_position` cue `submitted` at chunk `5102774` offsets `82-91`; context: [16] The Applicant explained that his PIF was written on the day it was due to be submitted and that he did not know what to do, and did not know he could amend his narrative.
- Evidence: `evidence_fact` cue `found that` at chunk `5102774` offsets `544-554`; context: The RPD found that the Applicant’s failure to mention the teachers’ racist inaction in his PIF undermined his credibility.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102775` offsets `17-26`; context: [17] In his oral testimony, the Applicant said that on one occasion at school a classmate fell in front of him and pretended that it was the Applicant who was responsible for the fall.
- Evidence: `reasoning_application` cue `Because` at chunk `5102775` offsets `185-192`; context: Because he was Roma, the teacher gave the Applicant a severe slap to the face.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102776` offsets `17-26`; context: [18] In his oral testimony, the Applicant said that he was beaten twice at school by his classmates.
- Evidence: `reasoning_application` cue `because` at chunk `5102776` offsets `163-170`; context: He reported the incident to his teachers but they did nothing because he is Roma.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102777` offsets `36-45`; context: [19] The Applicant said in his oral testimony that he was beaten a number of times for racist reasons.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102777` offsets `103-110`; context: However, in the notes the immigration officer made at the time the Applicant made his claim, the Applicant mentioned threats, humiliations and racial slurs, yet never mentioned being beaten.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102778` offsets `17-26`; context: [20] In his oral testimony, the Applicant said that he had no faith in the police in Hungary because a Roma friend of his had tried to get into a place of entertainment, and was not only refused entry but was chased away by two policemen, one of whom hit him.
- Evidence: `reasoning_application` cue `because` at chunk `5102778` offsets `93-100`; context: [20] In his oral testimony, the Applicant said that he had no faith in the police in Hungary because a Roma friend of his had tried to get into a place of entertainment, and was not only refused entry but was chased away by two policemen, one of whom hit him.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102779` offsets `29-38`; context: [21] In the Applicant’s oral testimony he said that he had never been threatened by the Hungarian Guard, and did not know anyone personally who had.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102779` offsets `149-156`; context: However, in the immigration officer’s notes it appears that the Applicant stated that he had been personally threatened by the Hungarian Guard.
- Evidence: `party_position` cue `claimed` at chunk `5102780` offsets `599-606`; context: The RPD thought it appeared the Applicant realized that he was going to be asked about corroborative documents and claimed not to have sought medical or police help as a way of avoiding the need for documents.
- Evidence: `evidence_fact` cue `testimony` at chunk `5102780` offsets `90-99`; context: [22] The RPD thought that the Applicant generally seemed vague and evasive throughout his testimony.
- Evidence: `party_position` cue `submitted` at chunk `5102781` offsets `322-331`; context: Counsel submitted that the Applicant had a slight sun tan, and that white Hungarians would not have this.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102781` offsets `630-638`; context: It was not aware of any objective evidence that white Hungarians are unable to get a sun tan.
- Evidence: `governing_rule` cue `under` at chunk `5102781` offsets `982-987`; context: As such, his claim under sections 96 and 97 of the Act failed.

#### 23478:1:subtheme:3 · paragraphs 24-24

- Raw key terms: `basis, claim, credible, decision, evidence, favourable, found, issues`
- Display key terms: `basis, credible, favourable, issues`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: basis, credible, favourable, issues Rule/authority context: [24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the cla Application context: [24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the cla Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5102782` offsets `224-230`; context: ISSUES
- Evidence: `evidence_fact` cue `found that` at chunk `5102782` offsets `18-28`; context: [24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the claim.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5102782` offsets `29-40`; context: [24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the claim.
- Evidence: `reasoning_application` cue `therefore` at chunk `5102782` offsets `172-181`; context: [24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the claim.

#### Section text

Galyas v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-03-08
Neutral citation
2013 FC 250
File numbers
IMM-5351-12
Decision Content
Date: 20130308
Docket: IMM-5351-12
Citation: 2013 FC 250
Ottawa, Ontario, March 8, 2013
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
VIKTOR GALYAS
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
INTRODUCTION

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c 27 (Act) for judicial review of the decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated 7 May 2012 (Decision), which refused the Applicant’s application to be deemed a Convention refugee or a person in need of protection under sections 96 and 97 of the Act.
BACKGROUND

[2] The Applicant is a 37-year-old man from Hungary. He fears persecution in Hungary due to his Roma ethnicity. Much of the following sequence of events is in dispute.

[3] The Applicant is from the town of Lakon. He was beaten at school for being Roma. He complained to teachers, but they did nothing. The Applicant attended vocational school where he was the only Roma student. Two skinheads in his class routinely harassed him. They assaulted him on two occasions, once in the classroom. The Applicant was refused entry to public places because of his ethnicity, and had trouble finding work. He heard about a racially-motivated murder in a town near him, and that the Hungarian Guard were planning an attack on another nearby town. The Applicant fled to Canada on 19 November 2009, and made his claim upon arrival at the airport.

[4] After arriving in Canada, the Applicant was told by a neighbour to go to the law offices of Viktor Hohots. He met with an interpreter who told him to write out the reasons for his claim and to sign the Personal Information Form (PIF) before he left. The interpreter did not tell the Applicant that what he was writing would be used as his PIF narrative; nor did he explain what should be in a PIF narrative or its relevance to the Applicant’s claim. The Applicant was not given any instructions on what to write, so he just wrote a short and general paragraph about his experiences in Hungary.

[5] Prior to the Applicant’s 9 March 2012 hearing date, the Applicant met with interpreters at Mr. Hohots’ office for the purpose of preparing amendments to his PIF. The interpreters did not ask the Applicant for more details about his claim, nor did they explain to him what should be included in the PIF or its purpose. The Applicant inquired about adding more information, but he was advised not to do this. The amended PIF was translated to the Applicant before he signed it, but Question 31 of the PIF form was not read to him. This question provides instructions for what should be included in a PIF narrative.

[6] One of the interpreters told the Applicant to obtain copies of police or medical reports. He also asked him some general questions, such as whether he had any brothers or sisters. The Applicant says he was not told to obtain any other documents in support of his claim, nor was the test for a successful refugee claim explained to him. The Applicant was also not told that he could obtain a medical report in regards to memory problems he experiences, or that Legal Aid would be able to cover the cost of such a report.

[7] The Applicant met with Vikramjit Uppal, a lawyer from Mr. Hohots’ office, a few days before his hearing. This appointment lasted about 20 minutes. Mr. Uppal asked the Applicant some questions about the reason for his claim, but did not ask for a full account of the events causing him to flee Hungary. He did not explain to the Applicant the test that must be met in order to be accepted as a refugee, nor did he inform him of things that might be asked at the hearing.

[8] The Applicant never met with Mr. Hohots himself. He was represented at his hearing by Mr. Uppal. The only document Mr. Uppal submitted into evidence was a document about country conditions in Hungary. The RPD found that there was no credible basis for the Applicant’s claim, and thus refused him refugee status.

[9] After receiving his negative decision, the Applicant decided to hire a new lawyer. He also filed a complaint with the Law Society of Upper Canada concerning both Mr. Hohots and Mr. Uppal. The Affidavit of Karina Azanza lays out the details of this complaint.

[10] Both counsel who were involved in representing the Applicant vigorously deny the Applicant’s allegations of incompetent representation. In a letter to the Law Society of Upper Canada (LSUC) dated 18 August 2012, Mr. Hohots indicates that the Applicant himself was often not diligent and missed a number of appointments (see Exhibit K of the Affidavit of Karina Azanza). Contrary to the Applicant’s assertions, Mr. Hohots says that he met with the Applicant on 19 November 2009, along with the firm’s interpreter, Mr. Sarkozi. He further says that the Applicant was advised about the refugee process in Canada, told to provide a detailed narrative containing instances of persecution, and instructed to gather or obtain documents corroborating his claim.

[11] In Mr. Uppal’s response to the LSUC dated 20 August 2012 (Exhibit B of the Affidavit of Karina Azanza), he says that he met with the Applicant twice: on 27 February 2012 and on 6 March 2012, each time for an hour to prepare for the hearing. Mr. Uppal says that he instructed the Applicant to obtain documentary evidence, that he prepared him to testify at the hearing, and that he competently represented him at the hearing.

[12] The Applicant disputes this version of events. He points out that a letter sent by Mr. Hohots to the RPD on 22 December 2009 to explain why the Applicant’s PIF was submitted late says that “we were working to obtain the Legal Aid certificate for this family.” The Legal Aid Certificate (page 94 of the Affidavit of Karina Azanza) says that it was issued on 24 November 2009. The Applicant also points out that Mr. Uppal says in his letter to the LSUC that the Applicant was initially Mr. Jozsef Sarcozi’s client. Mr. Sarcozi is an immigration consultant and translator at Mr. Hohots’ firm. The Applicant says that the evidence of Mr. Uppal and Mr. Hohots diverges with regards to who from the firm met with him.

[13] Mr. Uppal asserts that he was present at the meetings where the Applicant met with the interpreters. The Applicant says that Mr. Uppal has presented no evidence such as notes from the meetings in support of this. Mr. Hohots says that he did advise the Applicant to obtain documentation, but the Applicant says that Mr. Hohots has not provided any documentation in support of this assertion.
DECISION UNDER REVIEW

[14] By Decision dated 7 May 2012, the RPD determined that, pursuant to subsection 107(2) of the Act, there was no credible basis for the Applicant’s claim, and thus he was not entitled to refugee protection.

[15] The RPD noted that throughout the hearing there was a number of discrepancies between the Applicant’s oral testimony and the information contained in his PIF. For example, the Applicant said at his oral hearing that he was beaten at least five times as a child and that his parents complained, but the teachers said that they could do nothing. The complaints made by his parents to teachers and their being rebuffed for racist reasons was not mentioned in the PIF.

[16] The Applicant explained that his PIF was written on the day it was due to be submitted and that he did not know what to do, and did not know he could amend his narrative. The RPD did not find this explanation satisfactory. Claimants have 28 days to prepare their PIFs and the Applicant was represented by counsel. He amended his PIF just prior to the hearing on other points, so he must have known that amendments were possible. He also affirmed at the beginning of the hearing that the PIF, as amended, was complete and accurate. The RPD found that the Applicant’s failure to mention the teachers’ racist inaction in his PIF undermined his credibility.

[17] In his oral testimony, the Applicant said that on one occasion at school a classmate fell in front of him and pretended that it was the Applicant who was responsible for the fall. Because he was Roma, the teacher gave the Applicant a severe slap to the face. This incident was not mentioned in the PIF. The Applicant gave the same explanation as for the previous omission, and the RPD did not accept it for the same reasons. The RPD also thought that the Applicant obviously considered the incident significant when recounting it. The RPD found that the failure to mention this incident in the PIF further undermined the Applicant’s credibility.

[18] In his oral testimony, the Applicant said that he was beaten twice at school by his classmates. He reported the incident to his teachers but they did nothing because he is Roma. The RPD noted this was not included in his PIF. The RPD did not think this a minor incident and that if it had really happened it would have been included in his PIF. The RPD thought that this omission further undermined the Applicant’s credibility.

[19] The Applicant said in his oral testimony that he was beaten a number of times for racist reasons. However, in the notes the immigration officer made at the time the Applicant made his claim, the Applicant mentioned threats, humiliations and racial slurs, yet never mentioned being beaten. The Applicant said that at the time he made his claim he did not know where he was, he felt weird, and he was scared, surprised and startled. The RPD said that it understood that the Applicant may have been jet-lagged, but even if the Applicant could not concentrate on small details in listing problems that he experienced in his life, it would be reasonable to expect the Applicant to have mentioned multiple beatings instead of, or at least in addition to, the ones that he did mention. The RPD found that this discrepancy further undermined his credibility.

[20] In his oral testimony, the Applicant said that he had no faith in the police in Hungary because a Roma friend of his had tried to get into a place of entertainment, and was not only refused entry but was chased away by two policemen, one of whom hit him. This incident was not mentioned in the Applicant’s PIF. The RPD noted that the directions for filling out the PIF are quite clear that all attempts to obtain protection from the authorities are to be detailed, and if attempts are not made the reasons should be given. The Applicant was quite clear in his oral testimony that it was this incident that caused him not to have confidence in the police. Considering this, the RPD felt it would be reasonable to expect the incident to have been mentioned in the PIF, and the fact that it was not further undermined the Applicant’s credibility.

[21] In the Applicant’s oral testimony he said that he had never been threatened by the Hungarian Guard, and did not know anyone personally who had. However, in the immigration officer’s notes it appears that the Applicant stated that he had been personally threatened by the Hungarian Guard. The Applicant explained at the hearing that he meant that the Hungarian Guard threatened Roma people in general. The RPD did not find this explanation satisfactory. The notes of the immigration officer are fairly clear in that the Applicant fears the Hungarian Guard, and that “they threatened my life.” The RPD thought the way in which the notes are written indicates that something happened to the Applicant personally, not a general threat against Roma. It found that this discrepancy further undermined the Applicant’s credibility.

[22] The RPD thought that the Applicant generally seemed vague and evasive throughout his testimony. It said that at times he seemed to be concocting his answers to avoid further credibility concerns. For example, when the RPD noted that it seemed strange that the Applicant did not seek medical attention or police help after being beaten by racist thugs, one time for several minutes, the Applicant said he had not been seriously injured and did not think the incidents were major. The RPD thought it appeared the Applicant realized that he was going to be asked about corroborative documents and claimed not to have sought medical or police help as a way of avoiding the need for documents.

[23] The RPD found the Applicant to be generally lacking in credibility, and simply did not believe, on a balance of probabilities, what the Applicant alleged had happened to him. It also noted that the Applicant had dark hair and white skin, whereas Roma are stereotypically identified by dark skin pigmentation. Counsel submitted that the Applicant had a slight sun tan, and that white Hungarians would not have this. The Applicant said that he could be identified as Roma by his behaviour and other physical features such as his eyebrows. The RPD did not find these explanations satisfactory. It was not aware of any objective evidence that white Hungarians are unable to get a sun tan. Furthermore, while it noted that some Roma people have light or white skin, the only thing offered to establish the Applicant’s ethnicity as Roma was his own testimony, which it did not believe. The RPD found, on a balance of probabilities, that the Applicant is not Roma. As such, his claim under sections 96 and 97 of the Act failed.

[24] The RPD also found that pursuant to subsection 107(2) of the Act there was no credible or trustworthy evidence on which a favourable decision could have been made and therefore there is no credible basis for the claim.
ISSUES

## 23478:2 · paragraphs 25-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `da47c01a7dcbbac2d46838b5eaa8ad44154c1160dbb10a953d4e2197c343b684`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23478:2:subtheme:1 · paragraphs 25-26

- Raw key terms: `review, standard, adopt, analysis, applicable, applicant, breach, brunswick`
- Display key terms: `review, standard, adopt, analysis, applicable, breach, brunswick`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: review, standard, adopt, analysis, applicable, breach, brunswick Rule/authority context: STANDARD OF REVIEW | [26] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 held that a standard of review analysis need not be conducted in every instance. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5102783` offsets `40-46`; context: [25] The Applicant raises the following issues:
1) Was there a breach of natural justice due to the incompetence of the Applicant’s former counsel?
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5102783` offsets `228-246`; context: STANDARD OF REVIEW
- Evidence: `issue` cue `question` at chunk `5102784` offsets `219-227`; context: Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5102784` offsets `85-103`; context: [26] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 held that a standard of review analysis need not be conducted in every instance.

#### 23478:2:subtheme:2 · paragraphs 27-28

- Raw key terms: `appeal, canada, citizenship, court, federal, further, held, immigration`
- Display key terms: `federal, further`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: federal, further Rule/authority context: ” The standard of review applicable to the first issue is correctness. | [28] In Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (FCA) the Federal Court of Appeal held that the standard of review on a credibility finding is reasonableness. Application context: Further, in Elmi v Canada (Minister of Citizenship and Immigration), 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102785` offsets `15-20`; context: [27] The first issue goes to the Applicant’s right to fully present his case, which is an issue of procedural fairness (see Xu v Canada (Minister of Citizenship and Immigration), 2006 FC 718, Baker v Canada (Minister of Citizenship and Immigration, [1999] 2 SCR 817 [Baker] at paragraph 22).
- Evidence: `governing_rule` cue `standard of review` at chunk `5102785` offsets `909-927`; context: ” The standard of review applicable to the first issue is correctness.
- Evidence: `issue` cue `issue` at chunk `5102786` offsets `710-715`; context: The standard of review on the second issue is reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5102786` offsets `133-151`; context: [28] In Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (FCA) the Federal Court of Appeal held that the standard of review on a credibility finding is reasonableness.
- Evidence: `reasoning_application` cue `therefore` at chunk `5102786` offsets `401-410`; context: Further, in Elmi v Canada (Minister of Citizenship and Immigration), 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be evaluated on a standard of review of reasonableness.

#### 23478:2:subtheme:3 · paragraphs 29-29

- Raw key terms: `above, acceptable, analysis, another, canada, citizenship, concerned, court`
- Display key terms: `above, acceptable, analysis, another, concerned`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: above, acceptable, analysis, another, concerned Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5102787` offsets `219-226`; context: [29] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### Section text

[25] The Applicant raises the following issues:
1) Was there a breach of natural justice due to the incompetence of the Applicant’s former counsel?
2) Was the RPD’s credibility finding that the Applicant is not Roma reasonable?
STANDARD OF REVIEW

[26] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[27] The first issue goes to the Applicant’s right to fully present his case, which is an issue of procedural fairness (see Xu v Canada (Minister of Citizenship and Immigration), 2006 FC 718, Baker v Canada (Minister of Citizenship and Immigration, [1999] 2 SCR 817 [Baker] at paragraph 22). In Canadian Union of Public Employees (C.U.P.E.) v Ontario (Minister of Labour), 2003 SCC 29, the Supreme Court of Canada held at paragraph 100 that it “is for the courts, not the Minister, to provide the legal answer to procedural fairness questions.” Further, the Federal Court of Appeal in Sketchley v Canada (Attorney General), 2005 FCA 404 at paragraph 53 held that the “procedural fairness element is reviewed as a question of law. No deference is due. The decision-maker has either complied with the content of the duty of fairness appropriate for the particular circumstances, or has breached this duty.” The standard of review applicable to the first issue is correctness.

[28] In Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (FCA) the Federal Court of Appeal held that the standard of review on a credibility finding is reasonableness. Further, in Elmi v Canada (Minister of Citizenship and Immigration), 2008 FC 773, at paragraph 21, Justice Max Teitelbaum held that findings of credibility are central to the RPD’s finding of fact and are therefore to be evaluated on a standard of review of reasonableness. Finally, in Negash v Canada (Minister of Citizenship and Immigration), 2012 FC 1164, Justice David Near held at paragraph 15 that the standard of review on a credibility determination is reasonableness. The standard of review on the second issue is reasonableness.

[29] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at paragraph 47, and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at paragraph 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”
STATUTORY PROVISIONS

## 23478:3 · paragraphs 30-91

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1334f2f4f7a37f707ddd6502e63044cdd656650a062ab1e9b575bfe02749d81e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23478:3:subtheme:1 · paragraphs 30-30

- Raw key terms: `absence, accepted, adequate, against, alors, appartenance, applicable, applicant`
- Display key terms: `absence, accepted, adequate, against, alors, appartenance, applicable`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: absence, accepted, adequate, against, alors, appartenance, applicable Position/evidence statements: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5102788` offsets `1563-1568`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
No credible basis 107 (2) If the Refugee Protection Division is of the opinion, in rejecting a claim, that there was no credible or trustworthy evidence on which it could have made a favourable decision, it shall state in its reasons for the decision that there is no credible basis for the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102788` offsets `1612-1620`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
No credible basis 107 (2) If the Refugee Protection Division is of the opinion, in rejecting a claim, that there was no credible or trustworthy evidence on which it could have made a favourable decision, it shall state in its reasons for the decision that there is no credible basis for the claim.
- Evidence: `reasoning_application` cue `because` at chunk `5102788` offsets `998-1005`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
No credible basis 107 (2) If the Refugee Protection Division is of the opinion, in rejecting a claim, that there was no credible or trustworthy evidence on which it could have made a favourable decision, it shall state in its reasons for the decision that there is no credible basis for the claim.

#### 23478:3:subtheme:2 · paragraphs 31-39

- Raw key terms: `applicant, counsel, canada, immigration, because, court, citizenship, found`
- Display key terms: `because`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: because Position/evidence statements: [32] The Applicant submits that he was incompetently represented by his former counsel in the following ways: a. | [33] The Applicant points out that neither of his former counsel specifically contends that they advised the Applicant as to the definition of “refugee. Rule/authority context: Hohots’ staff advised the Applicant of the legal test he would have to meet for his refugee claim to be accepted, including that he must establish that state protection would not be forthcoming to him in Hungary; d. Application context: Failing to ask the Applicant questions at the hearing that could have helped to prove to the RPD that he is Roma, and instead submitting that the Applicant is Roma because he has a Romani name, even though this does not  | Because counsel was unaware of the errors in the narrative she failed to file an amendment correcting them. Operative outcome context: They never allowed us in to clubs and when I went into a restaurant [sic] they told me that I cant [sic] go in because I am a gypsy. Evidence spans paragraphs 31-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5102789` offsets `54-61`; context: [31] The Applicant says that the test for determining whether the incompetence of counsel amounts to a breach of procedural fairness is found at paragraph 26 of the Supreme Court of Canada’s decision in R.
- Evidence: `party_position` cue `submits` at chunk `5102790` offsets `19-26`; context: [32] The Applicant submits that he was incompetently represented by his former counsel in the following ways:
a.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102790` offsets `1373-1381`; context: Failing to ask the Applicant questions at the hearing that could have helped to prove to the RPD that he is Roma, and instead submitting that the Applicant is Roma because he has a Romani name, even though this does not appear to be supported by the evidence;
iv.
- Evidence: `governing_rule` cue `legal test` at chunk `5102790` offsets `568-578`; context: Hohots’ staff advised the Applicant of the legal test he would have to meet for his refugee claim to be accepted, including that he must establish that state protection would not be forthcoming to him in Hungary;
d.
- Evidence: `reasoning_application` cue `because` at chunk `5102790` offsets `1287-1294`; context: Failing to ask the Applicant questions at the hearing that could have helped to prove to the RPD that he is Roma, and instead submitting that the Applicant is Roma because he has a Romani name, even though this does not appear to be supported by the evidence;
iv.
- Evidence: `party_position` cue `contends` at chunk `5102791` offsets `78-86`; context: [33] The Applicant points out that neither of his former counsel specifically contends that they advised the Applicant as to the definition of “refugee.
- Evidence: `party_position` cue `submits` at chunk `5102792` offsets `19-26`; context: [34] The Applicant submits that the Court has found breaches of procedural fairness in similar cases.
- Evidence: `evidence_fact` cue `found that` at chunk `5102792` offsets `193-203`; context: In El Kaissi v Canada (Minister of Citizenship and Immigration), 2011 FC 1234 Justice Near found that there was a miscarriage of justice when counsel did not assist the applicant in filling out his PIF and instead left this to an assistant, did not meet with the applicant until two days before the hearing, and failed to produce a letter concerning an arrest that proved to be critical to the applicant’s claim.
- Evidence: `party_position` cue `submitted` at chunk `5102793` offsets `321-330`; context: The interpreter made errors in the narrative and counsel then failed to review the English version of it with the applicant before it was submitted.
- Evidence: `evidence_fact` cue `found that` at chunk `5102793` offsets `534-544`; context: The Court found that counsel’s inadequate representation “was sufficiently serious to compromise the reliability of the Board’s decision.
- Evidence: `reasoning_application` cue `Because` at chunk `5102793` offsets `332-339`; context: Because counsel was unaware of the errors in the narrative she failed to file an amendment correcting them.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102794` offsets `276-284`; context: v Canada (Minister of Citizenship and Immigration), 2011 FC 927, the Court held counsel to be incompetent due to his conduct at the applicant’s hearing, and because “when a claimant retains a representative it is his or her duty to advise the client as to what evidence will be required.
- Evidence: `reasoning_application` cue `because` at chunk `5102794` offsets `172-179`; context: v Canada (Minister of Citizenship and Immigration), 2011 FC 927, the Court held counsel to be incompetent due to his conduct at the applicant’s hearing, and because “when a claimant retains a representative it is his or her duty to advise the client as to what evidence will be required.
- Evidence: `evidence_fact` cue `found that` at chunk `5102795` offsets `173-183`; context: v Canada (Minister of Citizenship and Immigration), 2012 FC 687 found that counsel was incompetent for failing to advise the applicant that financial establishment is relevant in an H&C decision, and that a miscarriage of justice had occurred because, in refusing the application, the officer specifically referred to the lack of this evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5102795` offsets `352-359`; context: v Canada (Minister of Citizenship and Immigration), 2012 FC 687 found that counsel was incompetent for failing to advise the applicant that financial establishment is relevant in an H&C decision, and that a miscarriage of justice had occurred because, in refusing the application, the officer specifically referred to the lack of this evidence.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102796` offsets `62-71`; context: [38] The Applicant points out that he has provided a detailed affidavit in support of this application describing his interactions with his former counsel and their staff.
- Evidence: `party_position` cue `submits` at chunk `5102797` offsets `27-34`; context: [39] The Applicant further submits that it is apparent from his PIF narrative that it was prepared without competent representation.
- Evidence: `reasoning_application` cue `because` at chunk `5102797` offsets `257-264`; context: I left my country because theirs [sic] a huge racism and discrimination.
- Evidence: `disposition` cue `allowed` at chunk `5102797` offsets `900-907`; context: They never allowed us in to clubs and when I went into a restaurant [sic] they told me that I cant [sic] go in because I am a gypsy.

#### 23478:3:subtheme:3 · paragraphs 40-43

- Raw key terms: `applicant, included, counsel, former, narrative, states, cannot, competent`
- Display key terms: `included, former, narrative, states, cannot, competent`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: included, former, narrative, states, cannot, competent Position/evidence statements: [41] The Applicant submits that the content of his narrative should have alerted his former counsel to the fact that he had experienced significant events that should have been specifically referenced in the PIF. Application context: The Applicant states that it cannot be alleged that he failed to inform his counsel that these events occurred because they are set out in his PIF. Evidence spans paragraphs 40-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5102798` offsets `97-105`; context: [40] Guidance as to what should be included in a PIF narrative is set out in the instructions to question 31.
- Evidence: `issue` cue `whether` at chunk `5102799` offsets `651-658`; context: Further, competent counsel would have included some information in the narrative as to whether the Applicant sought state protection in Hungary.
- Evidence: `party_position` cue `submits` at chunk `5102799` offsets `19-26`; context: [41] The Applicant submits that the content of his narrative should have alerted his former counsel to the fact that he had experienced significant events that should have been specifically referenced in the PIF.
- Evidence: `reasoning_application` cue `because` at chunk `5102799` offsets `527-534`; context: The Applicant states that it cannot be alleged that he failed to inform his counsel that these events occurred because they are set out in his PIF.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102800` offsets `79-87`; context: [42] The Applicant recognizes that there are many contradictory allegations in evidence before this Court, particularly relating to the meetings between the Applicant and different people from Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102800` offsets `307-314`; context: However, what cannot be contested is the content of the PIF that was filed.

#### 23478:3:subtheme:4 · paragraphs 44-51

- Raw key terms: `applicant, counsel, claim, finding, because, credible, evidence, findings`
- Display key terms: `finding, because, credible, findings`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: finding, because, credible, findings Position/evidence statements: [50] While the Applicant submits that the breach of procedural fairness due to counsel’s incompetence is enough to warrant allowing this application, he further submits that the RPD’s finding that he is not Roma is unrea Application context: In the Decision, the RPD addressed each incident of persecution raised by the Applicant at his hearing, but then went on to find the Applicant not credible in relation to each incident because it was not addressed in his | [49] The Applicant further attests that had he known what documents would be helpful to his claim, he could have provided a letter from his friend who was beaten by a police officer as well as letters from family members Evidence spans paragraphs 44-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102802` offsets `587-592`; context: Counsel do not appear to challenge that they never advised the Applicant to amend his PIF to include more detail, but rather blame the Applicant for failing to raise the issue himself.
- Evidence: `evidence_fact` cue `record` at chunk `5102803` offsets `637-643`; context: ” The Applicant submits that former counsel’s failure to adequately represent him is apparent on the face of the record, and this resulted in a miscarriage of justice.
- Evidence: `counterargument_limitation` cue `fails` at chunk `5102803` offsets `391-396`; context: Counsel were retained to help the Applicant with his claim, yet the PIF narrative is deficient on the face of it and fails to provide particulars even though the narrative says that the Applicant was “humiliated, discriminated, threatened and beaten.
- Evidence: `reasoning_application` cue `because` at chunk `5102804` offsets `324-331`; context: In the Decision, the RPD addressed each incident of persecution raised by the Applicant at his hearing, but then went on to find the Applicant not credible in relation to each incident because it was not addressed in his PIF.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102804` offsets `243-246`; context: In the Decision, the RPD addressed each incident of persecution raised by the Applicant at his hearing, but then went on to find the Applicant not credible in relation to each incident because it was not addressed in his PIF.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102805` offsets `255-263`; context: At paragraph 21 of that decision the Court held that “a breach of procedural fairness inevitably occurs where the incompetence of counsel prevents a refugee claimant from presenting critical evidence to satisfy the Board and leads to negative credibility findings that permeate the entire decision.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102806` offsets `12-21`; context: [48] In his affidavit, the Applicant says that had he better understood what had to be proven in a refugee claim he could have discussed past interactions with the police in Hungary, and testified about his Roma identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102807` offsets `391-399`; context: [49] The Applicant further attests that had he known what documents would be helpful to his claim, he could have provided a letter from his friend who was beaten by a police officer as well as letters from family members confirming that he is Roma and that he was beaten at school because he is Roma as well as a psychological report addressing any difficulties he experienced in presenting evidence at his hearing.
- Evidence: `reasoning_application` cue `because` at chunk `5102807` offsets `281-288`; context: [49] The Applicant further attests that had he known what documents would be helpful to his claim, he could have provided a letter from his friend who was beaten by a police officer as well as letters from family members confirming that he is Roma and that he was beaten at school because he is Roma as well as a psychological report addressing any difficulties he experienced in presenting evidence at his hearing.
- Evidence: `party_position` cue `submits` at chunk `5102808` offsets `25-32`; context: [50] While the Applicant submits that the breach of procedural fairness due to counsel’s incompetence is enough to warrant allowing this application, he further submits that the RPD’s finding that he is not Roma is unreasonable because it relies on speculation, conjecture and racial profiling.
- Evidence: `reasoning_application` cue `because` at chunk `5102808` offsets `228-235`; context: [50] While the Applicant submits that the breach of procedural fairness due to counsel’s incompetence is enough to warrant allowing this application, he further submits that the RPD’s finding that he is not Roma is unreasonable because it relies on speculation, conjecture and racial profiling.

#### 23478:3:subtheme:5 · paragraphs 52-53

- Raw key terms: `applicant, basis, canada, cannot, citizenship, ethnicity, evidence, identity`
- Display key terms: `basis, cannot, ethnicity, identity`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: basis, cannot, ethnicity, identity Position/evidence statements: [52] The Applicant submits that the Court has quashed decisions that make negative findings about a person’s identity based on generalizations, stereotypes and racial profiling. | That is, the mere fact that a person is the exception to an ethnic profile, even on a number of factors, does not provide a sound basis for deciding that he or she is not who he or she claims to be. Application context: [53] In Vodics v Canada (Minister of Citizenship and Immigration), 2005 FC 783, at paragraph 17, Justice Douglas Campbell emphasized at paragraph 17 that an applicant’s sworn evidence as to his or her ethnicity is presum Operative outcome context: [52] The Applicant submits that the Court has quashed decisions that make negative findings about a person’s identity based on generalizations, stereotypes and racial profiling. Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102810` offsets `420-425`; context: In Szostak v Canada (Minister of Citizenship and Immigration), 2001 FCT 938, at paragraphs 20-24, the Court found that:
…when reviewing decisions of the Refugee Division in cases involving claimants who said that they were Roma and where the issue was whether they were or not and where the Refugee Division based its decision on physical appearance and other characteristics of those who were before the tribunals.
- Evidence: `party_position` cue `submits` at chunk `5102810` offsets `19-26`; context: [52] The Applicant submits that the Court has quashed decisions that make negative findings about a person’s identity based on generalizations, stereotypes and racial profiling.
- Evidence: `evidence_fact` cue `found that` at chunk `5102810` offsets `286-296`; context: In Szostak v Canada (Minister of Citizenship and Immigration), 2001 FCT 938, at paragraphs 20-24, the Court found that:
…when reviewing decisions of the Refugee Division in cases involving claimants who said that they were Roma and where the issue was whether they were or not and where the Refugee Division based its decision on physical appearance and other characteristics of those who were before the tribunals.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102810` offsets `1249-1256`; context: However, since Ms.
- Evidence: `disposition` cue `quashed` at chunk `5102810` offsets `46-53`; context: [52] The Applicant submits that the Court has quashed decisions that make negative findings about a person’s identity based on generalizations, stereotypes and racial profiling.
- Evidence: `party_position` cue `claims` at chunk `5102811` offsets `796-802`; context: That is, the mere fact that a person is the exception to an ethnic profile, even on a number of factors, does not provide a sound basis for deciding that he or she is not who he or she claims to be.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102811` offsets `175-183`; context: [53] In Vodics v Canada (Minister of Citizenship and Immigration), 2005 FC 783, at paragraph 17, Justice Douglas Campbell emphasized at paragraph 17 that an applicant’s sworn evidence as to his or her ethnicity is presumed to be truthful and cannot be rebutted by stereotypical assumptions:
…Therefore, where sworn testimony of ethnicity is presumed to be true, without the required level of certainty being attained, the failure of the person giving the evidence to meet a decision-maker’s understanding of an ethnic stereotype does not constitute reliable evidence which can be used to rebut the presumption.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5102811` offsets `292-301`; context: [53] In Vodics v Canada (Minister of Citizenship and Immigration), 2005 FC 783, at paragraph 17, Justice Douglas Campbell emphasized at paragraph 17 that an applicant’s sworn evidence as to his or her ethnicity is presumed to be truthful and cannot be rebutted by stereotypical assumptions:
…Therefore, where sworn testimony of ethnicity is presumed to be true, without the required level of certainty being attained, the failure of the person giving the evidence to meet a decision-maker’s understanding of an ethnic stereotype does not constitute reliable evidence which can be used to rebut the presumption.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5102811` offsets `242-248`; context: [53] In Vodics v Canada (Minister of Citizenship and Immigration), 2005 FC 783, at paragraph 17, Justice Douglas Campbell emphasized at paragraph 17 that an applicant’s sworn evidence as to his or her ethnicity is presumed to be truthful and cannot be rebutted by stereotypical assumptions:
…Therefore, where sworn testimony of ethnicity is presumed to be true, without the required level of certainty being attained, the failure of the person giving the evidence to meet a decision-maker’s understanding of an ethnic stereotype does not constitute reliable evidence which can be used to rebut the presumption.

#### 23478:3:subtheme:6 · paragraphs 54-54

- Raw key terms: `admis, among, analyse, apparence, appearance, applicant, aside, assumptions`
- Display key terms: `admis, among, analyse, apparence, appearance, aside, assumptions`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: admis, among, analyse, apparence, appearance, aside, assumptions Rule/authority context: In my view, comments such as these, under the circumstances, vitiate the whole decision at issue. Evidence spans paragraphs 54-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5102812` offsets `799-806`; context: Whether it is expressed consciously or not, this kind of stereotypical consideration, entirely based on the appearance of an individual, is unfortunately such that it fosters unacceptable prejudice toward Jews and cannot be used to discredit the applicant’s stated fear of being persecuted on the basis of her Jewish religion.
- Evidence: `governing_rule` cue `under` at chunk `5102812` offsets `1162-1167`; context: In my view, comments such as these, under the circumstances, vitiate the whole decision at issue.

#### 23478:3:subtheme:7 · paragraphs 55-56

- Raw key terms: `appearance, applicant, person, physical, roma, skin, white, affidavit`
- Display key terms: `appearance, person, physical, roma, skin, white, affidavit`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: appearance, person, physical, roma, skin, white, affidavit Position/evidence statements: [56] The Applicant submits that it is unfair and problematic to make factual findings concerning a claimant’s physical appearance, particularly findings that attempt to classify a claimant’s skin colour into categories s Application context: ” He also attests that “Roma people identify as Roma because we share joint origins and customs and not because we share a similar physical appearance. Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102813` offsets `95-104`; context: In his affidavit in support of this application, he disputes the RPD’s finding that he has “white skin.
- Evidence: `reasoning_application` cue `because` at chunk `5102813` offsets `244-251`; context: ” He also attests that “Roma people identify as Roma because we share joint origins and customs and not because we share a similar physical appearance.
- Evidence: `party_position` cue `submits` at chunk `5102814` offsets `19-26`; context: [56] The Applicant submits that it is unfair and problematic to make factual findings concerning a claimant’s physical appearance, particularly findings that attempt to classify a claimant’s skin colour into categories such as “white” or “dark skin pigmentation,” as occurred in the Decision.

#### 23478:3:subtheme:8 · paragraphs 57-58

- Raw key terms: `applicant, counsel, incompetence, respondent, above, actually, allegations, amend`
- Display key terms: `incompetence, above, actually, allegations, amend`
- Argument roles: `evidence_fact, party_position`
- Explanation: Observed roles: evidence_fact, party_position Display terms: incompetence, above, actually, allegations, amend Position/evidence statements: [58] The Respondent submits that the Applicant is now trying to blame his former counsel for his failed refugee claim when he was repeatedly told by his counsel to submit documents relevant to his claim, and was aware th Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102815` offsets `186-194`; context: Had the RPD not reached this erroneous finding, it would have had to consider the other evidence on the persecution the Applicant had faced in Hungary (Horvath v Canada (Minister of Citizenship and Immigration), 2011 FC 1350).
- Evidence: `party_position` cue `submits` at chunk `5102816` offsets `20-27`; context: [58] The Respondent submits that the Applicant is now trying to blame his former counsel for his failed refugee claim when he was repeatedly told by his counsel to submit documents relevant to his claim, and was aware that he could amend his PIF, having actually done so once.

#### 23478:3:subtheme:9 · paragraphs 59-67

- Raw key terms: `applicant, counsel, canada, citizenship, immigration, minister, respondent, different`
- Display key terms: `different`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position Display terms: different Position/evidence statements: [59] The Respondent also submits that an allegation of incompetent counsel is not sufficient grounds to warrant the intervention of the Court. | The Respondent submits that the Applicant has not established that his counsel was incompetent or that, but for their incompetence, the outcome of his refugee claim would have been different (Yang v Canada (Minister of C Operative outcome context: [66] Both counsel in this case have denied the Applicant’s allegations and assert that they did meet with him on different occasions, that they explained to him the refugee process, and that they instructed him to gather Evidence spans paragraphs 59-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102817` offsets `491-496`; context: In an extraordinary case, competency of counsel may give rise to a natural justice issue.
- Evidence: `party_position` cue `submits` at chunk `5102817` offsets `25-32`; context: [59] The Respondent also submits that an allegation of incompetent counsel is not sufficient grounds to warrant the intervention of the Court.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102817` offsets `498-505`; context: However there is a heavy burden on an applicant to come within this exception: see for example Sheika v.
- Evidence: `issue` cue `issues` at chunk `5102818` offsets `167-173`; context: If the Applicant had issues with the way that he was being represented and the way counsel conducted the proceedings and/or submissions made on his behalf, these matters should have been raised at the “earliest practicable opportunity” at his hearing.
- Evidence: `party_position` cue `submits` at chunk `5102820` offsets `494-501`; context: The Respondent submits that the Applicant has not established that his counsel was incompetent or that, but for their incompetence, the outcome of his refugee claim would have been different (Yang v Canada (Minister of Citizenship and Immigration), 2008 FC 269 at paragraphs 17-21).
- Evidence: `party_position` cue `submits` at chunk `5102823` offsets `20-27`; context: [65] The Respondent submits that the Applicant has not established that his former counsel were incompetent or that the result would have been different had they acted differently.
- Evidence: `party_position` cue `assert` at chunk `5102824` offsets `75-81`; context: [66] Both counsel in this case have denied the Applicant’s allegations and assert that they did meet with him on different occasions, that they explained to him the refugee process, and that they instructed him to gather documents to corroborate his claim.
- Evidence: `disposition` cue `denied` at chunk `5102824` offsets `36-42`; context: [66] Both counsel in this case have denied the Applicant’s allegations and assert that they did meet with him on different occasions, that they explained to him the refugee process, and that they instructed him to gather documents to corroborate his claim.
- Evidence: `party_position` cue `submits` at chunk `5102825` offsets `146-153`; context: [67] Given the letters from counsel instructing the Applicant to obtain documentary evidence (see the Affidavit of Karina Azanza), the Respondent submits that the Applicant must bear some responsibility for failing to provide corroborative documents which may have assisted with his claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102825` offsets `84-92`; context: [67] Given the letters from counsel instructing the Applicant to obtain documentary evidence (see the Affidavit of Karina Azanza), the Respondent submits that the Applicant must bear some responsibility for failing to provide corroborative documents which may have assisted with his claim.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102825` offsets `370-373`; context: As the Applicant himself failed to act with care, he has not demonstrated that, but for his lawyer’s actions, the result of his hearing would have been different.

#### 23478:3:subtheme:10 · paragraphs 68-69

- Raw key terms: `applicant, counsel, roma, admits, affidavit, allegations, alleged, amend`
- Display key terms: `roma, admits, affidavit, allegations, alleged, amend`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: roma, admits, affidavit, allegations, alleged, amend Application context: The Applicant therefore knew, contrary to his affidavit, that he could update/amend his PIF before the hearing. Evidence spans paragraphs 68-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5102826` offsets `542-548`; context: In fact, the transcript indicates that counsel explored the key issues that were before the RPD: credibility concerns arising from omissions in the PIF; state protection; and discrimination and/or persecution of Roma in Hungary.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102826` offsets `218-227`; context: The Applicant therefore knew, contrary to his affidavit, that he could update/amend his PIF before the hearing.
- Evidence: `reasoning_application` cue `therefore` at chunk `5102826` offsets `186-195`; context: The Applicant therefore knew, contrary to his affidavit, that he could update/amend his PIF before the hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102827` offsets `39-47`; context: [69] Furthermore, the Applicant’s oral evidence contradicted what he originally told immigration officials upon entry.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102827` offsets `191-194`; context: Thus, it is even more unclear that the result would have been different but for counsel’s alleged incompetence.

#### 23478:3:subtheme:11 · paragraphs 70-72

- Raw key terms: `apprehension, bias, canada, court, reasonable, supreme, test, board`
- Display key terms: `apprehension, bias, reasonable, supreme`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: apprehension, bias, reasonable, supreme Evidence spans paragraphs 70-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5102828` offsets `406-413`; context: v Newfoundland (Board of Commissioners of Public Utilities), [1992] 1 SCR 623, the Supreme Court of Canada stated the test for a reasonable apprehension of bias is whether a reasonably informed bystander could reasonably perceive bias on the part of the adjudicator.
- Evidence: `issue` cue `question` at chunk `5102829` offsets `546-554`; context: It is a finding that must be carefully considered since it calls into question an element of judicial integrity.
- Evidence: `counterargument_limitation` cue `however` at chunk `5102830` offsets `472-479`; context: added these words to the now classical expression of the reasonable apprehension standard:
The grounds for this apprehension must, however, be substantial, and I .

#### 23478:3:subtheme:12 · paragraphs 73-75

- Raw key terms: `applicant, counsel, respondent, canada, employment, evidence, findings, immigration`
- Display key terms: `employment, findings`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: employment, findings Position/evidence statements: [73] The Respondent submits that the RPD’s findings about the Applicant’s identity do not amount to bias or establish reliance on generalizations, stereotyping, or racial profiling. | The Respondent submits the RPD’s negative credibility findings are therefore reasonable. Application context: The Respondent submits the RPD’s negative credibility findings are therefore reasonable. | [75] The Applicant points out that in Sheikh v Canada (Minister of Employment and Immigration), [1990] FCJ No 604 the Federal Court of Appeal explicitly held that a refugee determination can be set aside because of incom Operative outcome context: ” As such, the Respondent submits that the Applicant’s argument should be dismissed. Evidence spans paragraphs 73-75. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5102831` offsets `244-251`; context: Quite simply, having found him not credible, the RPD analyzed whether the Applicant was Roma as he asserted.
- Evidence: `party_position` cue `submits` at chunk `5102831` offsets `20-27`; context: [73] The Respondent submits that the RPD’s findings about the Applicant’s identity do not amount to bias or establish reliance on generalizations, stereotyping, or racial profiling.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102831` offsets `409-417`; context: In doing so, the RPD considered counsel’s submissions and the Applicant’s explanation at the hearing as to what other evidence there was for the RPD to determine whether he was Roma, including the Applicant’s skin pigmentation, hair, facial features, and last name.
- Evidence: `disposition` cue `dismissed` at chunk `5102831` offsets `840-849`; context: ” As such, the Respondent submits that the Applicant’s argument should be dismissed.
- Evidence: `party_position` cue `submits` at chunk `5102832` offsets `510-517`; context: The Respondent submits the RPD’s negative credibility findings are therefore reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102832` offsets `57-65`; context: [74] Furthermore, questions of credibility and weight of evidence are within the jurisdiction of the RPD as the trier of fact (Brar v Canada (Minister of Employment and Immigration), [1986] FCJ No 346).
- Evidence: `reasoning_application` cue `therefore` at chunk `5102832` offsets `562-571`; context: The Respondent submits the RPD’s negative credibility findings are therefore reasonable.
- Evidence: `reasoning_application` cue `because` at chunk `5102833` offsets `204-211`; context: [75] The Applicant points out that in Sheikh v Canada (Minister of Employment and Immigration), [1990] FCJ No 604 the Federal Court of Appeal explicitly held that a refugee determination can be set aside because of incompetence of counsel.

#### 23478:3:subtheme:13 · paragraphs 76-79

- Raw key terms: `applicant, counsel, incompetence, submits, assertion, claim, court, hearing`
- Display key terms: `incompetence, submits, assertion, hearing`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: incompetence, submits, assertion, hearing Position/evidence statements: [76] The Applicant also submits that there is no requirement that he raise the issue of counsel incompetence at his hearing. | [77] In any event, the Applicant submits that the earliest practicable opportunity for him to raise his concerns about the competence of his former counsel was not at the hearing of his refugee claim. Rule/authority context: The Applicant submits that the Respondent has not cited any jurisprudence that actually supports its assertion that an applicant is required to raise the issue of the incompetence of counsel at the hearing of his or her  | The Applicant reiterates the jurisprudence he previously cited where the Court has allowed judicial review in similar circumstances (El Kaissi; Memari; K. Application context: The Applicant further submits that his case is extraordinary because there is a clear link between the RPD’s reasons for refusal and his counsel’s incompetent representation. Operative outcome context: [78] As regards the Respondent’s assertion that judicial review on the grounds of counsel incompetence will only be allowed in “extraordinary circumstances,” the Applicant submits that this is such an extraordinary circu Evidence spans paragraphs 76-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102834` offsets `79-84`; context: [76] The Applicant also submits that there is no requirement that he raise the issue of counsel incompetence at his hearing.
- Evidence: `party_position` cue `submits` at chunk `5102834` offsets `24-31`; context: [76] The Applicant also submits that there is no requirement that he raise the issue of counsel incompetence at his hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102834` offsets `279-287`; context: Dragomirov was about an applicant’s objections to evidence that was submitted to the RPD in support of his refugee hearing.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5102834` offsets `556-569`; context: The Applicant submits that the Respondent has not cited any jurisprudence that actually supports its assertion that an applicant is required to raise the issue of the incompetence of counsel at the hearing of his or her claim.
- Evidence: `party_position` cue `submits` at chunk `5102835` offsets `33-40`; context: [77] In any event, the Applicant submits that the earliest practicable opportunity for him to raise his concerns about the competence of his former counsel was not at the hearing of his refugee claim.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102835` offsets `208-217`; context: In his affidavit, the Applicant indicates that he only became aware of the extent of his former counsel’s incompetence after he met with his new counsel.
- Evidence: `party_position` cue `submits` at chunk `5102836` offsets `172-179`; context: [78] As regards the Respondent’s assertion that judicial review on the grounds of counsel incompetence will only be allowed in “extraordinary circumstances,” the Applicant submits that this is such an extraordinary circumstance.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5102836` offsets `258-271`; context: The Applicant reiterates the jurisprudence he previously cited where the Court has allowed judicial review in similar circumstances (El Kaissi; Memari; K.
- Evidence: `reasoning_application` cue `because` at chunk `5102836` offsets `451-458`; context: The Applicant further submits that his case is extraordinary because there is a clear link between the RPD’s reasons for refusal and his counsel’s incompetent representation.
- Evidence: `disposition` cue `allowed` at chunk `5102836` offsets `116-123`; context: [78] As regards the Respondent’s assertion that judicial review on the grounds of counsel incompetence will only be allowed in “extraordinary circumstances,” the Applicant submits that this is such an extraordinary circumstance.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5102837` offsets `523-536`; context: ” The jurisprudence is clear that it is only necessary to establish that the reliability of the result is compromised (K.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102837` offsets `130-133`; context: [79] In response to the Respondent’s assertion that it is not clear the result of the Applicant’s claim would have been different but for counsel’s alleged incompetence, the Applicant submits that it is not necessary for him to demonstrate that but for the incompetence the result “would have been different.

#### 23478:3:subtheme:14 · paragraphs 80-86

- Raw key terms: `applicant, counsel, respondent, finding, case, credibility, decision, findings`
- Display key terms: `finding, case, credibility, findings`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: finding, case, credibility, findings Position/evidence statements: [80] The Applicant submits that the Respondent’s argument that the RPD’s negative credibility finding was reasonable is not the relevant issue in this case. | [81] The Respondent submits that the Applicant is effectively suggesting that the RPD was biased. Rule/authority context: ” However, the Respondent has not cited any jurisprudence that says it is appropriate for the RPD to base credibility findings on a claimant’s skin colour and physical appearance in this or any other circumstance. | Incompetence will only constitute a breach of natural justice under extraordinary circumstances. Application context: [82] The Respondent submits that this aspect of the Decision was reasonable because the RPD based its finding on the evidence before it, including “the Applicant’s skin pigmentation, hair, facial features, and last name. Evidence spans paragraphs 80-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5102838` offsets `137-142`; context: [80] The Applicant submits that the Respondent’s argument that the RPD’s negative credibility finding was reasonable is not the relevant issue in this case.
- Evidence: `party_position` cue `submits` at chunk `5102838` offsets `19-26`; context: [80] The Applicant submits that the Respondent’s argument that the RPD’s negative credibility finding was reasonable is not the relevant issue in this case.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102838` offsets `348-351`; context: A finding that the Applicant’s right to natural justice was breached is sufficient to allow this application for judicial review regardless of whether the Decision would have been reasonable but for counsel’s incompetence.
- Evidence: `party_position` cue `submits` at chunk `5102839` offsets `20-27`; context: [81] The Respondent submits that the Applicant is effectively suggesting that the RPD was biased.
- Evidence: `party_position` cue `submits` at chunk `5102840` offsets `20-27`; context: [82] The Respondent submits that this aspect of the Decision was reasonable because the RPD based its finding on the evidence before it, including “the Applicant’s skin pigmentation, hair, facial features, and last name.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102840` offsets `117-125`; context: [82] The Respondent submits that this aspect of the Decision was reasonable because the RPD based its finding on the evidence before it, including “the Applicant’s skin pigmentation, hair, facial features, and last name.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5102840` offsets `264-277`; context: ” However, the Respondent has not cited any jurisprudence that says it is appropriate for the RPD to base credibility findings on a claimant’s skin colour and physical appearance in this or any other circumstance.
- Evidence: `reasoning_application` cue `because` at chunk `5102840` offsets `76-83`; context: [82] The Respondent submits that this aspect of the Decision was reasonable because the RPD based its finding on the evidence before it, including “the Applicant’s skin pigmentation, hair, facial features, and last name.
- Evidence: `counterargument_limitation` cue `However` at chunk `5102840` offsets `222-229`; context: ” However, the Respondent has not cited any jurisprudence that says it is appropriate for the RPD to base credibility findings on a claimant’s skin colour and physical appearance in this or any other circumstance.
- Evidence: `governing_rule` cue `under` at chunk `5102841` offsets `262-267`; context: Incompetence will only constitute a breach of natural justice under extraordinary circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102844` offsets `32-40`; context: [86] Former counsel dispute the evidence put forward by the Applicant but, in my view, there can be no disputing the inadequacies that appear on the face of the Applicant’s PIF narrative which clearly support his allegation that he was left to prepare this important document by himself, without guidance on what it should contain and what the RPD would be looking for in such a narrative.
- Evidence: `counterargument_limitation` cue `but` at chunk `5102844` offsets `70-73`; context: [86] Former counsel dispute the evidence put forward by the Applicant but, in my view, there can be no disputing the inadequacies that appear on the face of the Applicant’s PIF narrative which clearly support his allegation that he was left to prepare this important document by himself, without guidance on what it should contain and what the RPD would be looking for in such a narrative.

#### 23478:3:subtheme:15 · paragraphs 87-89

- Raw key terms: `applicant, claim, counsel, decision, evidence, former, inadequate, incompetent`
- Display key terms: `former, inadequate, incompetent`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: former, inadequate, incompetent Evidence spans paragraphs 87-89. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5102845` offsets `217-225`; context: [87] The evidence before me is undisputed that the Applicant was left to write his PIF on his own and that, after doing so, he was not advised that what he had written did not conform with the requirements set out in question 31 as to what should be in a PIF narrative.
- Evidence: `evidence_fact` cue `evidence` at chunk `5102845` offsets `9-17`; context: [87] The evidence before me is undisputed that the Applicant was left to write his PIF on his own and that, after doing so, he was not advised that what he had written did not conform with the requirements set out in question 31 as to what should be in a PIF narrative.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5102846` offsets `685-694`; context: Further, the Applicant has made clear in his affidavit that he could have adduced additional evidence to support his claim if he had had proper guidance from former counsel.

#### 23478:3:subtheme:16 · paragraphs 90-91

- Raw key terms: `agree, applicant, back, certification, concurs, considering, convinced, counsel`
- Display key terms: `agree, back, certification, concurs, considering, convinced`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, back, certification, concurs, considering, convinced Evidence spans paragraphs 90-91. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5102848` offsets `32-38`; context: [90] The Applicant raises other issues, but there is no point in considering them further as I am convinced this matter must be sent back for reconsideration.
- Evidence: `issue` cue `question` at chunk `5102849` offsets `31-39`; context: [91] Counsel agree there is no question for certification and the Court concurs.

#### Section text

[30] The following provisions of the Act are applicable in this proceeding:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political
opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries;
[…]
Person in Need of Protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
No credible basis 107 (2) If the Refugee Protection Division is of the opinion, in rejecting a claim, that there was no credible or trustworthy evidence on which it could have made a favourable decision, it shall state in its reasons for the decision that there is no credible basis for the claim.
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
[…]
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Preuve 107 (2) Si elle estime, en cas de rejet, qu’il n’a été présenté aucun élément de preuve crédible ou digne de foi sur lequel elle aurait pu fonder une décision favorable, la section doit faire état dans sa décision de l’absence de minimum de fondement de la demande.
ARGUMENTS
The Applicant
The Incompetence of Counsel

[31] The Applicant says that the test for determining whether the incompetence of counsel amounts to a breach of procedural fairness is found at paragraph 26 of the Supreme Court of Canada’s decision in R. v G.D.B., 2000 SCC 22. The Supreme Court of Canada said in that case that: “it must be established, first, that counsel’s acts or omissions constituted incompetence and second, that a miscarriage of justice resulted.”

[32] The Applicant submits that he was incompetently represented by his former counsel in the following ways:
a. No lawyer assisted the Applicant in preparing his PIF, and the assistant who did assist the Applicant did not explain to him what should be included in a PIF, the relevance of the contents to his claim, or translate the instructions to him;
b. No one from Mr. Hohots’ staff advised the Applicant that he should obtain documentation to corroborate his claim, such as police or medical reports;
c. No one from Mr. Hohots’ staff advised the Applicant of the legal test he would have to meet for his refugee claim to be accepted, including that he must establish that state protection would not be forthcoming to him in Hungary;
d. Neither Mr. Hohots nor his staff were adequately prepared for the Applicant’s hearing and their conduct and inaction were deficient for the following reasons:
i. Failing to arrange for the Applicant to meet with a lawyer at an earlier time than a few days before the hearing;
ii. Failing to obtain a full account of the facts behind the Applicant’s claim prior to the hearing;
iii. Failing to ask the Applicant questions at the hearing that could have helped to prove to the RPD that he is Roma, and instead submitting that the Applicant is Roma because he has a Romani name, even though this does not appear to be supported by the evidence;
iv. Failing to inform the Applicant that he might be required to answer questions concerning the form that was completed by immigration officials when he made his claim for refugee protection, and failing to prepare him accordingly;

[33] The Applicant points out that neither of his former counsel specifically contends that they advised the Applicant as to the definition of “refugee.” Mr. Uppal states that he advised the Applicant of the need to obtain documentation at their meeting on 6 March 2012, which was three days before his hearing. Mr. Hohots states that the Applicant was advised to provide documents, but does not provide specifics. Mr. Uppal also says that he did advise the Applicant that the notes from the immigration officer might be relevant, but the Applicant notes that the notes from 6 March 2012 provided by Mr. Uppal do not make any identifiable reference to the CIC notes.

[34] The Applicant submits that the Court has found breaches of procedural fairness in similar cases. In El Kaissi v Canada (Minister of Citizenship and Immigration), 2011 FC 1234 Justice Near found that there was a miscarriage of justice when counsel did not assist the applicant in filling out his PIF and instead left this to an assistant, did not meet with the applicant until two days before the hearing, and failed to produce a letter concerning an arrest that proved to be critical to the applicant’s claim.

[35] In Memari v Canada (Minister of Citizenship and Immigration), 2010 FC 1196, counsel was found to be incompetent based on the cumulative effect of her incompetent representation. The interpreter made errors in the narrative and counsel then failed to review the English version of it with the applicant before it was submitted. Because counsel was unaware of the errors in the narrative she failed to file an amendment correcting them. She also failed to procure a medical report corroborating the applicant’s injuries. The Court found that counsel’s inadequate representation “was sufficiently serious to compromise the reliability of the Board’s decision.”

[36] In T.K.M. v Canada (Minister of Citizenship and Immigration), 2011 FC 927, the Court held counsel to be incompetent due to his conduct at the applicant’s hearing, and because “when a claimant retains a representative it is his or her duty to advise the client as to what evidence will be required.”

[37] Although decided in the context of a humanitarian and compassionate (H&C) decision, the Court in K.I.K. v Canada (Minister of Citizenship and Immigration), 2012 FC 687 found that counsel was incompetent for failing to advise the applicant that financial establishment is relevant in an H&C decision, and that a miscarriage of justice had occurred because, in refusing the application, the officer specifically referred to the lack of this evidence.

[38] The Applicant points out that he has provided a detailed affidavit in support of this application describing his interactions with his former counsel and their staff. He has also provided copies of the complaint he filed with the Law Society of Upper Canada about his former counsel.

[39] The Applicant further submits that it is apparent from his PIF narrative that it was prepared without competent representation. The Applicant’s entire PIF is as follows:
Ny name is Galyos Viktor [sic] I was born on October 21st 1975. I left my country because theirs [sic] a huge racism and discrimination. Since I was a boy I struggled because I am a gypsy, I was humiliated, discriminated, threatened, and beaten. I got into problems with organizations that hated and killed gypsies. Like the Hungarian guardsmen or the skinheads, but most of the population judges the gypsies and discriminates them. I struggled to get a job [sic] I called a location if they have a job position available they told me yes and if I could come in for an interview when I did as soon as they seen [sic] my skin colour they said the position is filled and they will contact me if there is an opening. They never allowed us in to clubs and when I went into a restaurant [sic] they told me that I cant [sic] go in because I am a gypsy. I came to this country with high hopes that I wont [sic] be discriminated because of who I am.

[40] Guidance as to what should be included in a PIF narrative is set out in the instructions to question 31. The Applicant states that the instructions were never translated or explained to him. The instructions tell an applicant to set out in chronological order all significant events and reasons that led him or her to seek protection in Canada. It also tells applicants to provide details of any interactions with the authorities, and any steps that were taken to seek refuge in other parts of their home.

[41] The Applicant submits that the content of his narrative should have alerted his former counsel to the fact that he had experienced significant events that should have been specifically referenced in the PIF. He wrote “I was humiliated, discriminated, threatened, and beaten.” The narrative generally acknowledges that persecutory events occurred, but contains no information setting out the specific incidents. The Applicant states that it cannot be alleged that he failed to inform his counsel that these events occurred because they are set out in his PIF. Further, competent counsel would have included some information in the narrative as to whether the Applicant sought state protection in Hungary.

[42] The Applicant recognizes that there are many contradictory allegations in evidence before this Court, particularly relating to the meetings between the Applicant and different people from Mr. Hohots’ law office. The Applicant points out that the evidence from his two former counsels is contradictory. However, what cannot be contested is the content of the PIF that was filed. It is clear from looking at the PIF that it does not conform to expectations of what would be included in a PIF by a claimant who is represented by competent counsel. The PIF contains absolutely no particulars of the incidents of persecution suffered by the Applicant, and as a direct result the RPD found him not to be credible. The Applicant states that this is apparent on the face of the record.

[43] Further, former counsel do not appear to challenge the Applicant’s contention that he was left to write his own statement of reasons for his refugee claim, or that after doing so he was not advised that what he had written did not conform to the expectations as to what should be in a PIF narrative, or that he was not told that additional detail should be included. Counsels’ role seemed to be limited to translating the Applicant’s statement from Hungarian to English and submitting it to the RPD.

[44] Mr. Hohots admits that he left the Applicant to write his own narrative and deliver it to his office. Mr. Uppal also confirms that the Applicant wrote his own narrative, and likens the role of counsel to that of a police officer who is taking a statement from a witness. He says that the Applicant should not complain about a PIF he wrote himself, and that it was up to him to describe the events with accuracy. Counsel do not appear to challenge that they never advised the Applicant to amend his PIF to include more detail, but rather blame the Applicant for failing to raise the issue himself.

[45] Former counsel acknowledge that the Applicant’s PIF was deficient in detail and that they did not advise him of its deficiency. They also acknowledge that failing to provide the appropriate level of detail in a PIF can be detrimental to the outcome of a refugee claim. Counsel were retained to help the Applicant with his claim, yet the PIF narrative is deficient on the face of it and fails to provide particulars even though the narrative says that the Applicant was “humiliated, discriminated, threatened and beaten.” The Applicant submits that former counsel’s failure to adequately represent him is apparent on the face of the record, and this resulted in a miscarriage of justice.

[46] The Applicant points out that it was the omission of specific events in the PIF that caused the RPD to find that he was not credible. In the Decision, the RPD addressed each incident of persecution raised by the Applicant at his hearing, but then went on to find the Applicant not credible in relation to each incident because it was not addressed in his PIF. The RPD did address some other concerns, but it is apparent that its findings with regards to the omissions permeate the entire Decision. Essentially, the RPD relied on omissions to discredit each and every persecutory event referenced by the Applicant at his hearing.

[47] The present situation is very similar to El Kaissi, above. At paragraph 21 of that decision the Court held that “a breach of procedural fairness inevitably occurs where the incompetence of counsel prevents a refugee claimant from presenting critical evidence to satisfy the Board and leads to negative credibility findings that permeate the entire decision.” In the present case, it was the omissions from the Applicant’s PIF that were central to the RPD’s finding that the Applicant was not credible, and which led to the refusal of his claim.

[48] In his affidavit, the Applicant says that had he better understood what had to be proven in a refugee claim he could have discussed past interactions with the police in Hungary, and testified about his Roma identity. Had he known that the notes from the immigration officer might be relevant, he could have testified that the interpreter assisted by phone, and that the form was not read back to him before he signed it. Had his former counsel been sufficiently familiar with the background to his claim, he could have asked questions at the hearing to help elicit this evidence.

[49] The Applicant further attests that had he known what documents would be helpful to his claim, he could have provided a letter from his friend who was beaten by a police officer as well as letters from family members confirming that he is Roma and that he was beaten at school because he is Roma as well as a psychological report addressing any difficulties he experienced in presenting evidence at his hearing. The Applicant submits that had he had a meaningful opportunity to present this oral and documentary evidence to the RPD, it may not have reached the same conclusion. As such, he submits that a miscarriage of justice has occurred.
The RPD’s Finding that the Applicant is not Roma

[50] While the Applicant submits that the breach of procedural fairness due to counsel’s incompetence is enough to warrant allowing this application, he further submits that the RPD’s finding that he is not Roma is unreasonable because it relies on speculation, conjecture and racial profiling.

[51] The Federal Court of Appeal has held that it is an error for the RPD to base its findings on mere speculation or conjuncture (Canada (Minister of Employment and Immigration) v Satiacum, [1989] FCJ No 505 (FCA)). The RPD reiterates the finding that the Applicant is not credible, but also relies on its finding that the Applicant has “white skin.”

[52] The Applicant submits that the Court has quashed decisions that make negative findings about a person’s identity based on generalizations, stereotypes and racial profiling. In Szostak v Canada (Minister of Citizenship and Immigration), 2001 FCT 938, at paragraphs 20-24, the Court found that:
…when reviewing decisions of the Refugee Division in cases involving claimants who said that they were Roma and where the issue was whether they were or not and where the Refugee Division based its decision on physical appearance and other characteristics of those who were before the tribunals.
In Pluhar, supra, Justice Evans wrote this at paragraphs 10 and 11 of his decision:
In my opinion, the Refugee Division erred in law by effectively basing the decision on its assessment that Ms. Pluharova was not dark skinned, especially since it claimed no relevant “expertise”. It is inherently dangerous for Board members to base a finding on whether people in another country would regard a claimant of a particular ethnicity solely on the basis of the member’s observation of the person concerned.
There may, of course, be some situations in which it will be quite obvious from a person’s appearance that the person is not of a particular ethnicity. However, since Ms. Pluharova had black hair and a “suntanned” appearance, the panel’s “common sense” was an unsufficiently reliable basis for the panel’s assessment of such a sensitive matter. Skin tone cannot be characterized simply as either “light” or “dark”: there is a broad spectrum between these polarities. Racists may be able to identify a person as a member of a minority group by physical characteristics that would not be apparent to people in other countries.
In Mitac, supra, Justice Lutfy endorsed what Justice Evans had said in Pluhar. He then focussed on the evidence that was before the tribunal and concluded that certain of the Board’s findings were made without regard to the material before it. He was also critical of the absence of a Romany interpreter.
In my view, cases involving Romany claimants are no different than any other case which comes before the Refugee Division where identity is an issue. Panels of the Refugee Division must make their findings of identity based on the evidence adduced, whether documentary or by way of testimony. Moreover, inferences drawn must be based on the evidence and be reasonable as was made clear in Aguebor v. MEI (1993), 160 N.R. 315 (F.C.A.).
This principle ensures that generalizations, typifying, racial profiling, averaging, and preconceptions are held in check. In this case, except as to language and education, the tribunal had no documentary evidence the Court was made aware of which provided a solid basis for assessing the identity of this claimant who said he was a Roma and who testified as to the dangers of “the typical physical characteristics of the Roma in Poland” (certified record, page 541) and who expressed his concern about the dialect he spoke (certified record, page 588).

[53] In Vodics v Canada (Minister of Citizenship and Immigration), 2005 FC 783, at paragraph 17, Justice Douglas Campbell emphasized at paragraph 17 that an applicant’s sworn evidence as to his or her ethnicity is presumed to be truthful and cannot be rebutted by stereotypical assumptions:
…Therefore, where sworn testimony of ethnicity is presumed to be true, without the required level of cert

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23478:4 · paragraphs 92-93

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1212c7dbe9489fa25ba523e9668549c87c22fa319374ed8a977e402fc429d31b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23478:4:subtheme:1 · paragraphs 92-93

- Raw key terms: `allowed, application, back, cause, certification, citizenship, counsel, court`
- Display key terms: `allowed, back, certification`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allowed, back, certification No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 92-93. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application is allowed. The Decision is quashed and the matter is referred back for reconsideration.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-5351-12

STYLE OF CAUSE: VIKTOR GALYAS
- and -
MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: February 7, 2013
REASONS FOR 

## 23478:5 · paragraphs 94-94

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9f2667fb567f3c9af661a623f37a3c83c6c7f0bf2506dcc9eabf547219f31e3a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23478:5:subtheme:1 · paragraphs 94-94

- Raw key terms: `aisling, appearances, applicant, attorney, barrister, bhattacharyya, bondy, canada`
- Display key terms: `aisling, barrister, bhattacharyya, bondy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: aisling, barrister, bhattacharyya, bondy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 94-94. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: HON. MR. JUSTICE RUSSELL
DATED: March 8, 2013
APPEARANCES:
Aisling Bondy APPLICANT
Suran Bhattacharyya RESPONDENT
SOLICITORS OF RECORD:
Aisling Bondy APPLICANT
Barrister and Solicitor
Toronto, Ontario
William F. Pentney RESPONDENT
Deputy Attorney General of Canada
