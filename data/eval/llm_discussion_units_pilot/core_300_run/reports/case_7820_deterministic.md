# Discussion Units: case 7820

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **36**
- Continuity pairs: **35**
- Discussion Units: **3**
- Paragraph source hashes: **36**
- Sub-themes: **6**

## 7820:1 · paragraphs 0-9

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `95a7f05604ff55a224860ac86c8da16129a804977d522c2a51123c5b53887ee3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7820:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `applicants, argentina, decision, applicant, canada, immigration, judicial, principal`
- Display key terms: `argentina, judicial, principal`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: argentina, judicial, principal Position/evidence statements: [8] In December 2003, the Applicants submitted a Humanitarian and Compassionate (H & C) Application. Rule/authority context: [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: The decision was to the effect that there were insufficient grounds to allow the Applicants' request to apply for permanent residence from within Canada. | Following the crackdown on illegal immigrants after September 11, 2001, they left for Canada in June 2002 and decided to seek refugee status because they feared being deported back to Argentina. Operative outcome context: [6] The refugee claims of the Applicants were denied on June 10, 2003, by the Refugee Protection Division (RPD) of the Immigration and Refugee Protection Board. | [7] The Applicants applied for a PRRA on January 5, 2004, and it was denied on February 25, 2005. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4412390` offsets `47-58`; context: [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `apply` at chunk `4412390` offsets `346-351`; context: The decision was to the effect that there were insufficient grounds to allow the Applicants' request to apply for permanent residence from within Canada.
- Evidence: `reasoning_application` cue `because` at chunk `4412394` offsets `364-371`; context: Following the crackdown on illegal immigrants after September 11, 2001, they left for Canada in June 2002 and decided to seek refugee status because they feared being deported back to Argentina.
- Evidence: `evidence_fact` cue `found that` at chunk `4412395` offsets `185-195`; context: In its reasons, the RPD found that the Applicants' failure to claim refugee status in the United States created negative credibility inferences, and that they had a viable internal flight alternative in Argentina.
- Evidence: `disposition` cue `denied` at chunk `4412395` offsets `46-52`; context: [6] The refugee claims of the Applicants were denied on June 10, 2003, by the Refugee Protection Division (RPD) of the Immigration and Refugee Protection Board.
- Evidence: `reasoning_application` cue `applied` at chunk `4412396` offsets `19-26`; context: [7] The Applicants applied for a PRRA on January 5, 2004, and it was denied on February 25, 2005.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4412396` offsets `174-182`; context: Although represented by counsel, the Applicants did not seek judicial review of that decision either.
- Evidence: `disposition` cue `denied` at chunk `4412396` offsets `69-75`; context: [7] The Applicants applied for a PRRA on January 5, 2004, and it was denied on February 25, 2005.
- Evidence: `party_position` cue `submitted` at chunk `4412397` offsets `37-46`; context: [8] In December 2003, the Applicants submitted a Humanitarian and Compassionate (H & C) Application.
- Evidence: `reasoning_application` cue `because` at chunk `4412397` offsets `439-446`; context: The Applicants alleged essentially the same risks as presented on the RPD and PRRA applications, hardship for the family because of economic, education and criminal conditions in Argentina, and possible separation of the family if removed to the United States.
- Evidence: `disposition` cue `denied` at chunk `4412397` offsets `600-606`; context: This application was denied on July 20, 2005.

#### 7820:1:subtheme:2 · paragraphs 9-9

- Raw key terms: `abandonment, abide, addressed, affected, allegations, alleged, alternative, amount`
- Display key terms: `abandonment, abide, addressed, affected, allegations, alleged, alternative, amount`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: abandonment, abide, addressed, affected, allegations, alleged, alternative, amount Rule/authority context: She addressed documentary evidence relating to the consequences of abandonment of the Canadian-born children to the Child Welfare system by their parents so that they may have better lives in Canada, but found that such  Application context: However, she placed "little weight" on this factor, "because it has resulted form the Applicants' refusal to abide by removal orders which came into effect in summer 2003, approximately 1yr after the family's arrival. Evidence spans paragraphs 9-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4412398` offsets `3780-3786`; context: ISSUES
- Evidence: `evidence_fact` cue `evidence` at chunk `4412398` offsets `67-75`; context: [9] In her reasons, the Officer stated that there was insufficient evidence of unusual and undeserved or disproportionate hardship to warrant an exemption from the requirements of the Act.
- Evidence: `governing_rule` cue `under` at chunk `4412398` offsets `3026-3031`; context: She addressed documentary evidence relating to the consequences of abandonment of the Canadian-born children to the Child Welfare system by their parents so that they may have better lives in Canada, but found that such a situation would result from a parental choice entirely under the Applicants' control, and would therefore not constitute hardship that is unusual and undeserved or disproportionate.
- Evidence: `reasoning_application` cue `because` at chunk `4412398` offsets `680-687`; context: However, she placed "little weight" on this factor, "because it has resulted form the Applicants' refusal to abide by removal orders which came into effect in summer 2003, approximately 1yr after the family's arrival.
- Evidence: `counterargument_limitation` cue `However` at chunk `4412398` offsets `627-634`; context: However, she placed "little weight" on this factor, "because it has resulted form the Applicants' refusal to abide by removal orders which came into effect in summer 2003, approximately 1yr after the family's arrival.

#### Section text

Serda v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2006-03-17
Neutral citation
2006 FC 356
File numbers
IMM-4687-05
Decision Content
Date: 20060317
Docket: IMM-4687-05
Citation: 2006 FC 356
Ottawa, Ontario, March 17, 2006
PRESENT: The Honourable Justice de Montigny
BETWEEN:
RAUL GERARDO SERDA
SILVANA GABRIELA ZAMORA DE SERDA
MARIA PAULA SERDA
MARIO GUSTAVO ZAMORA
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act) of a decision of Immigration Officer Vanessa Bissonnette (the Officer) dated July 20, 2005. The decision was to the effect that there were insufficient grounds to allow the Applicants' request to apply for permanent residence from within Canada.
BACKGROUND

[2] Raul Gerardo Serda (the principal Applicant) is a citizen of Argentina. He was born on March 25, 1972. He came to Canada via the United States on June 25, 2002, with his wife Silvana Gabriella Zamora and daughter Maria Paula, who are also citizens of Argentina. Since their arrival in Canada, the Applicants have had three daughters who are Canadian citizens: Melisa Sabrina, born on January 8, 2003, Cynthia Elisa and Vanessa Carolina, born on May 28, 2004.

[3] The principal applicant began working part-time as a "remis" driver in Buenos Aires in 1996. Remises are a form of unlicensed taxi current in Argentina, and the fact that their owners do not pay taxes gives them a competitive advantage over regular taxis. Taxi drivers complained about the unfair competition, but obtained no assistance from the police or the government. Between 1996 and 2000, tensions between taxi and remis drivers escalated from peaceful demonstrations to outright violent attacks on remis drivers and threats against their families.

[4] The principal Applicant and his family began receiving threats in 1997. These threats escalated until 1998, when shots were fired at the principal Applicant's mother's house from outside, an hour after the Applicant had been eating dinner there. The principal Applicant's brother was also assaulted and threatened by a group of men who pulled a gun on him while he was driving them in his remis.

[5] As a result, the principal Applicant decided to relocate to the United Statesin 2000 for security reasons. The Applicants spent a little more than two years in the United Stateswithout ever applying for refugee status. Following the crackdown on illegal immigrants after September 11, 2001, they left for Canada in June 2002 and decided to seek refugee status because they feared being deported back to Argentina.

[6] The refugee claims of the Applicants were denied on June 10, 2003, by the Refugee Protection Division (RPD) of the Immigration and Refugee Protection Board. In its reasons, the RPD found that the Applicants' failure to claim refugee status in the United States created negative credibility inferences, and that they had a viable internal flight alternative in Argentina. The Applicants did not seek judicial review of the RPD's decision regarding their claims.

[7] The Applicants applied for a PRRA on January 5, 2004, and it was denied on February 25, 2005. The Applicants were apparently informed of the PRRA decision in April 2005. Although represented by counsel, the Applicants did not seek judicial review of that decision either.

[8] In December 2003, the Applicants submitted a Humanitarian and Compassionate (H & C) Application. Further submissions were requested and received from the Applicants in July 2004, which mentioned the two youngest children. Additional submissions were also received in May 2005, and were considered in the decision. The Applicants alleged essentially the same risks as presented on the RPD and PRRA applications, hardship for the family because of economic, education and criminal conditions in Argentina, and possible separation of the family if removed to the United States. This application was denied on July 20, 2005. The Applicants applied for leave and judicial review of that decision before this Court on August 3, 2005.
DECISION OF THE IMMIGRATION OFFICER

[9] In her reasons, the Officer stated that there was insufficient evidence of unusual and undeserved or disproportionate hardship to warrant an exemption from the requirements of the Act. After having considered factors weighing positively and negatively in making her decision, the Immigration officer came to the following conclusions:
The Applicants' establishment in Canada: The Officer noted that despite a long period of unemployment in Canada, the fact that the principal Applicant was now gainfully employed and that the family was integrated in the community indicated that the Applicants were established in Canada. However, she placed "little weight" on this factor, "because it has resulted form the Applicants' refusal to abide by removal orders which came into effect in summer 2003, approximately 1yr after the family's arrival. The settlement that resulted and the hardship of now uprooting the family were entirely within the Applicants' control and does not constitute undue and undeserved hardship". She further considered that "the hardship caused by voluntarily establishment to be disproportionate; all foreigners must weigh the pros and the cons of lengthy settlement in a country in which they do not benefit from permanent status".
Personalized risk facing the Applicants in Argentina: The Officer found that the alleged risk represented only a small portion of the Applicants' reasons for applying for H & C considerations, and that their allegations were identical to those made before the RPD. Considering that the RPD found that the Applicants had an internal flight alternative in Argentina, the Officer gave little weight to this factor.
Emotional hardship on the parents: The Officer mentioned documentary evidence regarding the parents' feelings of stress and insecurity at the prospect of returning to Argentina, but stated that she was not satisfied that their legitimate parental concerns would translate into dysfunctional parenting. While she recognized that relocation would constitute a hardship for the parents, she noted that the Applicants had demonstrated that they could be extremely resourceful, that economic conditions in Argentina had improved since their departure, and that they could benefit from the support of their families. The Officer concluded that the Applicants' legitimate parental concerns at the prospect of relocation to Argentina did not amount to unusual and undeserved or disproportionate hardship, and did not warrant an exemption from the requirements of the Act.
Best interests of the children affected by the outcome of the H & C decision: The Officer wrote that she considered "most extensively the impact of a negative decision on the four children affected by the outcome". She addressed documentary evidence relating to the consequences of abandonment of the Canadian-born children to the Child Welfare system by their parents so that they may have better lives in Canada, but found that such a situation would result from a parental choice entirely under the Applicants' control, and would therefore not constitute hardship that is unusual and undeserved or disproportionate. The Officer then considered the eventuality of relocation to Argentina as a family unit, which she considered a more likely outcome. She stated that her analysis was guided by Citizenship and Immigration Canada's Internal Processing Manual (IP5), specifically subsection 5.19, which pertains to the best interest of the children. After considering the Applicants' submissions regarding the poor quality of education, the children's exposure to poverty and violence and other factors relating to the conditions in Argentina, she concluded that they did not amount to hardship that is undeserved and unusual or disproportionate.
ISSUES

## 7820:2 · paragraphs 10-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a963184c02c1a284559d7f4d3a336239f7943ad17f780bb0ec893bb77f0ca0d8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7820:2:subtheme:1 · paragraphs 10-17

- Raw key terms: `officer, applicants, application, canada, decision, discretion, immigration, best`
- Display key terms: `officer, discretion, best`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: officer, discretion, best Position/evidence statements: [16] The Applicants also submitted that the Immigration Officer has fettered her discretion in refusing to place any weight on the Applicants' establishment in Canada because they had failed to abide by removal Orders is Rule/authority context: ANALYSIS Standard of review | 817, that the applicable standard of review regarding a decision on an H & C application was reasonableness simpliciter. Application context: [12] Accordingly, the task of this Court is to determine if there is any reason to support the conclusion reached by the Immigration Officer. | [15] I agree with the Respondent that the Officer doesn't have to be an expert in the law, as long as she applies the relevant principles. Operative outcome context: Finally, they contended that if the Immigration Officer's reasoning is allowed to stand, no application made pursuant to section 25 will ever receive a positive consideration in regard to establishment in Canada. Evidence spans paragraphs 10-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4412399` offsets `46-52`; context: [10] The Applicants have raised the following issues:
a) Did the Officer fetter her discretion?
- Evidence: `evidence_fact` cue `evidence` at chunk `4412399` offsets `169-177`; context: b) Did the Officer violate the duty of fairness by considering extrinsic evidence without first providing the Applicants with an opportunity to review this evidence and respond to it?
- Evidence: `governing_rule` cue `Standard of review` at chunk `4412399` offsets `389-407`; context: ANALYSIS
Standard of review
- Evidence: `governing_rule` cue `standard of review` at chunk `4412400` offsets `153-171`; context: 817, that the applicable standard of review regarding a decision on an H & C application was reasonableness simpliciter.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4412401` offsets `5-16`; context: [12] Accordingly, the task of this Court is to determine if there is any reason to support the conclusion reached by the Immigration Officer.
- Evidence: `governing_rule` cue `under` at chunk `4412403` offsets `795-800`; context: I am guided in my duty by the Internal Processing Manual - IP5 and, pertaining to the best interest of the children, all specific content found under subsection 5.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412404` offsets `457-465`; context: As discussed below, the Officer assessed the evidence presented by the Applicants fairly and with a view to all the circumstances of the case, and she did not fetter her discretion in declining to address the Australian decision.
- Evidence: `governing_rule` cue `principles` at chunk `4412404` offsets `127-137`; context: [15] I agree with the Respondent that the Officer doesn't have to be an expert in the law, as long as she applies the relevant principles.
- Evidence: `reasoning_application` cue `applies` at chunk `4412404` offsets `106-113`; context: [15] I agree with the Respondent that the Officer doesn't have to be an expert in the law, as long as she applies the relevant principles.
- Evidence: `party_position` cue `submitted` at chunk `4412405` offsets `25-34`; context: [16] The Applicants also submitted that the Immigration Officer has fettered her discretion in refusing to place any weight on the Applicants' establishment in Canada because they had failed to abide by removal Orders issued in the summer 2003.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4412405` offsets `701-712`; context: Finally, they contended that if the Immigration Officer's reasoning is allowed to stand, no application made pursuant to section 25 will ever receive a positive consideration in regard to establishment in Canada.
- Evidence: `reasoning_application` cue `because` at chunk `4412405` offsets `167-174`; context: [16] The Applicants also submitted that the Immigration Officer has fettered her discretion in refusing to place any weight on the Applicants' establishment in Canada because they had failed to abide by removal Orders issued in the summer 2003.
- Evidence: `disposition` cue `allowed` at chunk `4412405` offsets `663-670`; context: Finally, they contended that if the Immigration Officer's reasoning is allowed to stand, no application made pursuant to section 25 will ever receive a positive consideration in regard to establishment in Canada.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4412406` offsets `441-452`; context: It was statutorily stayed when the Applicants were notified that they could make a PRRA application, which they did in January of 2004, pursuant to section 232 of the Immigration and Refugee Protection Regulations.
- Evidence: `reasoning_application` cue `applies` at chunk `4412406` offsets `1600-1607`; context: A removal order is stayed when a person is notified by the Department under subsection 160(3) that they may make an application under subsection 112(1) of the Act, and the stay is effective until the earliest of the following events occurs:
(a) the Department receives confirmation in writing from the person that they do not intend to make an application;
(b) the person does not make an application within the period provided under section 162;
(c) the application for protection is rejected;
(d) if a decision to allow the application for protection is made under paragraph 114(1)(a) of the Act and the person has not made an application within the period provided under subsection 175(1) to remain in Canada as a permanent resident, the expiry of that period;
(e) if a decision to allow the application for protection is made under paragraph 114(1)(a) of the Act, the decision with respect to the person's application to remain in Canada as a permanent resident is made; and
(f) in the case of a person to whom subsection 112(3) of the Act applies, the stay is cancelled under subsection 114(2) of the Act.

#### 7820:2:subtheme:2 · paragraphs 18-21

- Raw key terms: `canada, applicants, officer, applicant, application, considered, fact, immigration`
- Display key terms: `officer, considered, fact`
- Argument roles: `disposition, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, party_position, reasoning_application Display terms: officer, considered, fact Position/evidence statements: [18] Now, counsel for the Applicants contends that it was unreasonable for the Immigration Officer to find that the Applicants could have effected their own removal from Canada in the summer of 2003. Rule/authority context: This cannot be equated to a "prolonged inability to leave Canada", which is one of the situations where the Applicant's degree of establishment may be a factor to be considered pursuant to section 11. | In assessing an application for landing from within Canada on Humanitarian and Compassionate grounds made pursuant to section 25, the Immigration Officer is provided with Ministerial guidelines. Application context: 7 Unusual and undeserved hardship Unusual and undeserved hardship is: • the hardship (of having to apply for a permanent resident visa from outside of Canada) that the applicant would have to face should be, in most case Operative outcome context: [21] It would obviously defeat the purpose of the Act if the longer an applicant was to live illegally in Canada, the better his or her chances were to be allowed to stay permanently, even though he or she would not othe Evidence spans paragraphs 18-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `contends` at chunk `4412407` offsets `37-45`; context: [18] Now, counsel for the Applicants contends that it was unreasonable for the Immigration Officer to find that the Applicants could have effected their own removal from Canada in the summer of 2003.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4412408` offsets `578-589`; context: This cannot be equated to a "prolonged inability to leave Canada", which is one of the situations where the Applicant's degree of establishment may be a factor to be considered pursuant to section 11.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4412409` offsets `1686-1697`; context: In assessing an application for landing from within Canada on Humanitarian and Compassionate grounds made pursuant to section 25, the Immigration Officer is provided with Ministerial guidelines.
- Evidence: `reasoning_application` cue `apply` at chunk `4412409` offsets `3008-3013`; context: 7 Unusual and undeserved hardship
Unusual and undeserved hardship is:
• the hardship (of having to apply for a permanent resident visa from outside of Canada) that the applicant would have to face should be, in most cases, unusual, in other words, a hardship not anticipated by the Act or Regulations; and
• the hardship (of having to apply for a permanent resident visa from outside of Canada) that the applicant would face should be, in most cases, the result of circumstances beyond the person's control
6.
- Evidence: `disposition` cue `allowed` at chunk `4412410` offsets `155-162`; context: [21] It would obviously defeat the purpose of the Act if the longer an applicant was to live illegally in Canada, the better his or her chances were to be allowed to stay permanently, even though he or she would not otherwise qualify as a refugee or permanent resident.

#### 7820:2:subtheme:3 · paragraphs 22-34

- Raw key terms: `applicants, canada, officer, application, argentina, reasons, review, consideration`
- Display key terms: `officer, argentina, review, consideration`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: officer, argentina, review, consideration Position/evidence statements: [27] The Applicants argued that the Officer's consideration of the best interest of the children was perverse, capricious and without any basis. | As for the documentary evidence, there is a presumption that she has considered what was submitted to her by the parties, even though she did not specifically address each and every one of the country reports in her reas Application context: It cannot be said, therefore, that she fettered her discretion; quite to the contrary, she looked at all the circumstances before concluding as she did, and therefore exercised her discretion. Operative outcome context: ), 2005 FC 1239); if it were otherwise, the huge majority of people living illegally in Canada would have to be granted permanent resident status for Humanitarian and Compassionate reasons. | [32] For all of the above reasons this application for judicial review is dismissed. Evidence spans paragraphs 22-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4412411` offsets `554-561`; context: It was submitted that without a proper and reasonable consideration of establishment, the Immigration Officer could not make a reasonable assessment of whether the family would suffer undue, undeserved or disproportionate hardship if returned to Argentina.
- Evidence: `reasoning_application` cue `therefore` at chunk `4412413` offsets `183-192`; context: It cannot be said, therefore, that she fettered her discretion; quite to the contrary, she looked at all the circumstances before concluding as she did, and therefore exercised her discretion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412414` offsets `262-270`; context: [25] The Applicants alleged that the Officer violated the duty of fairness by relying on the Pre-Removal Risk Assessment conducted in February 2005, despite submissions made by counsel that this risk assessment should be disregarded since it relied on extrinsic evidence which had not been provided to the Applicants for review and comment.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412415` offsets `291-299`; context: If the Applicants had a problem with the documentary evidence considered by the PRRA Officer, they should have raised it in the context of an application for leave and judicial review of the PRRA decision.
- Evidence: `party_position` cue `argued` at chunk `4412416` offsets `20-26`; context: [27] The Applicants argued that the Officer's consideration of the best interest of the children was perverse, capricious and without any basis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412416` offsets `247-255`; context: While they recognized that the Officer was not bound to explicitly address every piece of documentary evidence submitted to her, they nevertheless contended that she erred in failing to address documentary evidence that directly contradicted her conclusions.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4412416` offsets `279-291`; context: While they recognized that the Officer was not bound to explicitly address every piece of documentary evidence submitted to her, they nevertheless contended that she erred in failing to address documentary evidence that directly contradicted her conclusions.
- Evidence: `evidence_fact` cue `found that` at chunk `4412417` offsets `706-716`; context: She considered the allegations of risk and the family's history, and found that the hardships faced by the family fell within the normal range of hardship faced by any family being deported, and were not undue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412418` offsets `70-78`; context: [29] As for the alleged failure of the Officer to mention documentary evidence contradicting her conclusions, a review of the Cepeda-Gutierrez decision shows that Justice Evans was referring to evidence directly related to the personal situation of an applicant, and not to the documentary evidence.
- Evidence: `party_position` cue `submitted` at chunk `4412419` offsets `238-247`; context: As for the documentary evidence, there is a presumption that she has considered what was submitted to her by the parties, even though she did not specifically address each and every one of the country reports in her reasons.
- Evidence: `evidence_fact` cue `evidence` at chunk `4412419` offsets `172-180`; context: As for the documentary evidence, there is a presumption that she has considered what was submitted to her by the parties, even though she did not specifically address each and every one of the country reports in her reasons.
- Evidence: `party_position` cue `argued` at chunk `4412420` offsets `34-40`; context: [31] Finally, the Applicants have argued that conditions in Argentina are dismal and not good for raising children.
- Evidence: `disposition` cue `granted` at chunk `4412420` offsets `557-564`; context: ), 2005 FC 1239); if it were otherwise, the huge majority of people living illegally in Canada would have to be granted permanent resident status for Humanitarian and Compassionate reasons.
- Evidence: `disposition` cue `dismissed` at chunk `4412421` offsets `74-83`; context: [32] For all of the above reasons this application for judicial review is dismissed.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4412422` offsets `558-564`; context: "Yves de Montigny"
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-4687-05
- Evidence: `disposition` cue `dismissed` at chunk `4412422` offsets `473-482`; context: JUDGMENT
THIS COURT ORDERS THAT:
- This application for judicial review is dismissed.

#### Section text

[10] The Applicants have raised the following issues:
a) Did the Officer fetter her discretion?
b) Did the Officer violate the duty of fairness by considering extrinsic evidence without first providing the Applicants with an opportunity to review this evidence and respond to it?
c) Did the Officer err in law in failing to consider the best interest of the Applicants' children?
ANALYSIS
Standard of review

[11] The Supreme Court of Canada has made it clear in Baker v. Canada(Minister of Citizenship and Immigration), [1999] 2 S.C.R. 817, that the applicable standard of review regarding a decision on an H & C application was reasonableness simpliciter. That decision has consistently been followed by this Court: see, for example, Adviento v. Canada(M.C.I.), 2003 FC 1430 [2003] F.C.J. No. 1837 (QL); Li v. Canada (M.C.I.), 2004 FC 1695 [2004] F.C.J. No. 2055 (QL); Malekzai v. Canada (M.C.I.), 2004 FC 1099 [2004] F.C.J. No. 1329 (QL); Lee v. Canada (M.C.I.), 2005 FC 413.

[12] Accordingly, the task of this Court is to determine if there is any reason to support the conclusion reached by the Immigration Officer. The decision must be able to withstand a somewhat probing examination. On the other hand, this Court will not intervene on judicial review simply because it would have weighed the relevant factors differently and could have arrived at a different result.
Did the Officer fetter her discretion?

[13] Turning to the first argument submitted by the Applicants, they contended that the Officer erred in fettering her discretion based upon unreasonable interpretations of law and policy and erroneous findings of facts. More specifically, the Applicants urged that the Officer fettered her discretion in failing to consider their establishment in Canada, and in not considering relevant case law with respect to the best interests of the children.

[14] The second point can be disposed of summarily. In submissions made by counsel in May 2005, specific reference was made to the Federal Court's reasoning in Hawthorne v. Canada (M.C.I.), [2003] 2 F.C. 555, as well as to a decision rendered by an Australian Appeals Tribunal (Cabrera and Minister for Immigration and Multicultural and Indigenous Affairs, [2004] AATA 1353). In response to these submissions, the Immigration Officer stated: "While I remain cognizant of some of what has been debated in front of the Canadian Federal Court; I am not a legal counsel and my only concern is the fair and impartial review of this particular application. I am guided in my duty by the Internal Processing Manual - IP5 and, pertaining to the best interest of the children, all specific content found under subsection 5.19 of the said manual."

[15] I agree with the Respondent that the Officer doesn't have to be an expert in the law, as long as she applies the relevant principles. The Officer's reasons show that she clearly considered the best interests of the children according to the requirements of Canadian law, and as interesting as it may be, the Australian decision was of little legal value in the determination of the Applicants' application. As discussed below, the Officer assessed the evidence presented by the Applicants fairly and with a view to all the circumstances of the case, and she did not fetter her discretion in declining to address the Australian decision.

[16] The Applicants also submitted that the Immigration Officer has fettered her discretion in refusing to place any weight on the Applicants' establishment in Canada because they had failed to abide by removal Orders issued in the summer 2003. According to the Applicants, section 25 clearly applies to any individuals in Canada that are inadmissible to Canada, as they were deemed to be from the moment they declared their intention to make a refugee claim in Canada. They also relied on immigration policy, which states that establishment in Canada is one of the factors to be considered. Finally, they contended that if the Immigration Officer's reasoning is allowed to stand, no application made pursuant to section 25 will ever receive a positive consideration in regard to establishment in Canada. This would be in direct contradiction to the purpose of section 25 of the IRPA, which was to allow persons in violation of Canadian immigration law to apply for permanent residence.

[17] Despite the apparent attractiveness of this argument, I have come to the conclusion that it must be rejected. There is no doubt that the removal order against the Applicants did come into effect in the summer of 2003, following the decision of the RPD to dismiss the refugee claim of the Applicants. It was statutorily stayed when the Applicants were notified that they could make a PRRA application, which they did in January of 2004, pursuant to section 232 of the Immigration and Refugee Protection Regulations. This section reads as follows:
232. A removal order is stayed when a person is notified by the Department under subsection 160(3) that they may make an application under subsection 112(1) of the Act, and the stay is effective until the earliest of the following events occurs:
(a) the Department receives confirmation in writing from the person that they do not intend to make an application;
(b) the person does not make an application within the period provided under section 162;
(c) the application for protection is rejected;
(d) if a decision to allow the application for protection is made under paragraph 114(1)(a) of the Act and the person has not made an application within the period provided under subsection 175(1) to remain in Canada as a permanent resident, the expiry of that period;
(e) if a decision to allow the application for protection is made under paragraph 114(1)(a) of the Act, the decision with respect to the person's application to remain in Canada as a permanent resident is made; and
(f) in the case of a person to whom subsection 112(3) of the Act applies, the stay is cancelled under subsection 114(2) of the Act.
232. Il est sursis à la mesure de renvoi dès le moment où le ministère avise l'intéressé aux termes du paragraphe 160(3) qu'il peut faire une demande de protection au titre du paragraphe 112(1) de la Loi. Le sursis s'applique jusqu'au premier en date des événements suivants :
a) le ministère reçoit de l'intéressé confirmation écrite qu'il n'a pas l'intention de se prévaloir de son droit;
b) le délai prévu à l'article 162 expire sans que l'intéressé fasse la demande qui y est prévue;
c) la demande de protection est rejetée;
d) s'agissant d'une personne à qui l'asile a été conféré aux termes du paragraphe 114(1) de la Loi et qui n'a pas fait sa demande de séjour au Canada à titre de résident permanent dans le délai prévu au paragraphe 175(1), l'expiration du délai;
e) s'agissant d'une personne à qui l'asile a été conféré aux termes du paragraphe 114(1) de la Loi, la décision quant à sa demande de séjour au Canada à titre de résident permanent;
f) s'agissant d'une personne visée au paragraphe 112(3) de la Loi, la révocation du sursis prévue au paragraphe 114(2) de la Loi.

[18] Now, counsel for the Applicants contends that it was unreasonable for the Immigration Officer to find that the Applicants could have effected their own removal from Canada in the summer of 2003. Since they had a statutory right to seek Pre-removal Risk Assessment before being removed from Canada, the exercise of that legally available remedy should not be a fact from which the Immigration Officer can draw a negative inference.

[19] On the other hand, the fact that a removal order is stayed pending a PRRA application does not affect the validity of the removal order. The Applicants, knowing that further time in Canada waiting for their legal processes to be completed would mean more alleged difficulty in returning to their home country, and knowing that they had been ordered to be removed, made the choice to stay anyway. This cannot be equated to a "prolonged inability to leave Canada", which is one of the situations where the Applicant's degree of establishment may be a factor to be considered pursuant to section 11.2 of the IP5 Manual.

[20] One of the cornerstones of the Immigration and Refugee Protection Act is the requirement that persons who wish to live permanently in Canada must, prior to their arrival in Canada, submit their application outside Canada and qualify for, and obtain, a permanent resident visa. Section 25 of the Act gives to the Minister the flexibility to approve deserving cases for processing within Canada. This is clearly meant to be an exceptional remedy, as is made clear by the wording of that provision:
25. (1) The Minister shall, upon request of a foreign national who is inadmissible or who does not meet the requirements of this Act, and may, on the Minister's own initiative, examine the circumstances concerning the foreign national and may grant the foreign national permanent resident status or an exemption from any applicable criteria or obligation of this Act if the Minister is of the opinion that it is justified by humanitarian and compassionate considerations relating to them, taking into account the best interests of a child directly affected, or by public policy considerations.
25. (1) Le ministre doit, sur demande d'un étranger interdit de territoire ou qui ne se conforme pas à la présente loi, et peut, de sa propre initiative, étudier le cas de cet étranger et peut lui octroyer le statut de résident permanent ou lever tout ou partie des critères et obligations applicables, s'il estime que des circonstances d'ordre humanitaire relatives à l'étranger - compte tenu de l'intérêt supérieur de l'enfant directement touché - ou l'intérêt public le justifient.
In assessing an application for landing from within Canada on Humanitarian and Compassionate grounds made pursuant to section 25, the Immigration Officer is provided with Ministerial guidelines. Immigration Manual IP5 - Immigration Applications in Canada made on Humanitarian or compassionate Grounds, a manual put out by the Minister of Citizenship and Immigration Canada, provides guidelines on what is meant by Humanitarian and Compassionate grounds. It states, at paragraph 5.1:
5.1 Humanitarian and Compassionate Grounds
Applicants bear the onus of satisfying the decision-maker that their personal circumstances are such that the hardship of having to obtain a permanent resident visa from outside of Canada would be:
(i) unusual and undeserved or
(ii) disproportionate.
Applicants may present whatever facts they believe are relevant.
5.1 Motifs d'ordre humanitaire
Il incombe au demandeur de prouver au décideur que son cas particulier est tel que la difficulté de devoir obtenir un visa de resident permanent de l'extérieur du Canada serait
(i) soit inhabituelle et injustifiée;
(ii) soit excessive.
Le demandeur peut exposer les faits qu'il juge pertinents, quels qu'ils soient.
The IP5 Manual goes on to define "unusual and undeserved" hardship and "disproportionate" hardship. It states, at paragraphs 6.7 and 6.8:
6.7 Unusual and undeserved hardship
Unusual and undeserved hardship is:
• the hardship (of having to apply for a permanent resident visa from outside of Canada) that the applicant would have to face should be, in most cases, unusual, in other words, a hardship not anticipated by the Act or Regulations; and
• the hardship (of having to apply for a permanent resident visa from outside of Canada) that the applicant would face should be, in most cases, the result of circumstances beyond the person's control
6.8 Disproportionate hardship
Humanitarian and compassionate grounds may exist in cases that would not meet the "unusual and undeserved" criteria but where the hardship (of having to apply for a permanent resident visa from outside of Canada) would have a disproportionate impact on the applicant due to their personal circumstances
6.7 Difficulté inhabituelle et injustifiée
On appelle difficulté inhabituelle et injustifée :
• la difficulté (de devoir demander un visa de résident permanent hors du Canada) à laquelle le demandeur s'exposerait serait, dans la plupart des cas, inhabituelle ou, en d'autres termes, une difficulté non prévue à la Loi ou à son Règlement; et
• la difficulté (de devoir demander un visa de résident hors du Canada) à laquelle le demandeur s'exposerait serait, dans la pluparts des cas, le résultat de circonstances échappant au contrôle de cette personne.
6.8 Difficultés démesurées
Des motifs d'ordre humanitaire peuvent exister dans des cas n'étant pas considérés comme « inusités ou injustifiés » , mais dont la difficulté (de présenter une demande de visa de résident permanent à l'extérieur de Canada) aurait des répercussions disproportionnées pour le demandeur, compte tenu des circonstances qui lui sont propres.

[21] It would obviously defeat the purpose of the Act if the longer an applicant was to live illegally in Canada, the better his or her chances were to be allowed to stay permanently, even though he or she would not otherwise qualify as a refugee or permanent resident. This circular argument was indeed considered by the H & C officer, but not accepted; it doesn't strike me as being an unreasonable conclusion.

[22] The Applicants relied on section 11.2 of the IP5 Manual, according to which an applicant's degree of establishment in Canada "may be a factor to consider in certain situations", one of which is when the "prolonged inability to leave Canada has led to establishment". A note to that section further adds that "establishment of the applicant up to the time of the H & C decision may be considered". It was submitted that without a proper and reasonable consideration of establishment, the Immigration Officer could not make a reasonable assessment of whether the family would suffer undue, undeserved or disproportionate hardship if returned to Argentina.

[23] There are a number of answers to that submission. First of all, the public policy considerations outlined in the Immigration Manual do not bind the Minister and his agents (see Maple Lodge Farms Limited v. Government of Canada, [1982] 2 S.C.R. 2). More importantly, it cannot be said that the exercise of all the legal recourses provided by the IRPA are circumstances beyond the control of the Applicant. A failed refugee claimant is certainly entitled to use all the legal remedies at his or her disposal, but he or she must do so knowing full well that the removal will be more painful if it eventually comes to it. As Décary J.A. stated in Legault v. M.C.I., 2002 FCA 125, at para. 19:
The Minister, who is responsible for the application of the policy and the Act, is definitely authorized to refuse the exception requested by a person who has established the existence of humanitarian and compassionate grounds, if he believes, for example, that the circumstances surrounding his entry and stay in Canada discredit him or create a precedent susceptible of encouraging illegal entry in Canada. In this sense, the Minister is at liberty to take into consideration the fact that the humanitarian and compassionate grounds that a person claims are the result of his own actions.

[24] In any event, the Immigration Officer did not refuse to consider the establishment of the Applicants in Canada, but decided to give this factor little weight. It cannot be said, therefore, that she fettered her discretion; quite to the contrary, she looked at all the circumstances before concluding as she did, and therefore exercised her discretion. Before turning to the Applicants' other arguments, I need only add that even if the Officer erred in this respect, it would not in and of itself make her decision as a whole unreasonable, since establishment is only one of the factors that can be taken into consideration to determine if an applicant would suffer undue, undeserved or disproportionate hardship if returned to his or her country of origin. I have not been persuaded that her decision with respect to this factor tainted her assessment of all the other factors to which she turned her mind.
Did the Officer violate the duty of fairness?

[25] The Applicants alleged that the Officer violated the duty of fairness by relying on the Pre-Removal Risk Assessment conducted in February 2005, despite submissions made by counsel that this risk assessment should be disregarded since it relied on extrinsic evidence which had not been provided to the Applicants for review and comment. This extrinsic evidence consisted of a report on Argentina prepared by Latin Focus, according to which Argentina's economy was improving.

[26] Despite the Applicants' arguments to the contrary, and in light of the fact that they neither sought nor obtained judicial review of the PRRA decision, it was legally valid and it was not unreasonable for the Officer to consider it. If the Applicants had a problem with the documentary evidence considered by the PRRA Officer, they should have raised it in the context of an application for leave and judicial review of the PRRA decision. The present application is not the proper forum to seek review of the manner in which evidence was considered by the PRRA Officer.
Did the Officer err in failing to consider the best interest of the Applicants' children?

[27] The Applicants argued that the Officer's consideration of the best interest of the children was perverse, capricious and without any basis. While they recognized that the Officer was not bound to explicitly address every piece of documentary evidence submitted to her, they nevertheless contended that she erred in failing to address documentary evidence that directly contradicted her conclusions. They relied for that proposition on the decision of this Court in Cepeda-Guiterrez v. Canada(M.C.I.), [1998] F.C.J. No. 1425, where Justice Evans wrote at para. 17: "...the more important the evidence that is not mentioned specifically and analyzed in the agency's reasons, the more willing a court may be to infer from the silence that the agency made an erroneous finding of fact 'without regard to the evidence'". The Applicants gave the example of excerpts of a U.S. Department of State Report on Human Rights Practices in Argentina, which was cited by the Officer as a factor weighing negatively on the H & C application. They submitted that she failed to consider other reports that detailed evidence of high dropout rates and child labour in Argentina.

[28] Having carefully read the Immigration Officer's reasons, I am of the view that she was alert, alive and sensitive to the best interests of the Applicants' children, as required by the Supreme Court of Canada in Baker v. Canada (M.C.I.), [1999] 2 S.C.R. 817, at para. 74. She considered the children's young ages, socialization of the family, that they primarily spoke Spanish and had not started school in Canada, and the opportunities and challenges faced by the children and the family if returned to Argentina, as well as the general country conditions and the requirements for undue hardship not anticipated by the legislation. She considered the allegations of risk and the family's history, and found that the hardships faced by the family fell within the normal range of hardship faced by any family being deported, and were not undue. This finding, and the explanations on which it is based, do not strike me as being unreasonable.

[29] As for the alleged failure of the Officer to mention documentary evidence contradicting her conclusions, a review of the Cepeda-Gutierrez decision shows that Justice Evans was referring to evidence directly related to the personal situation of an applicant, and not to the documentary evidence. As my colleague Justice Snider noted recently in Gavoci v. Canada (M.C.I.), [2005] F.C.J. No. 249, at para. 9:
A review of Cepeda-Gutierrez shows that it must be read in context. I note that the reviewable error of the tribunal in Cepeda-Gutierrez was its failure to refer to a personal psychological re

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 7820:3 · paragraphs 35-35

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `352feda4f12744b28b8f0d1a17d1e428e1e645bb37b99e81c4f5e7de1d86f0ac`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7820:3:subtheme:1 · paragraphs 35-35

- Raw key terms: `alberta, appearances, applicants, attorney, barristers, calgary, canada, caron`
- Display key terms: `alberta, barristers, calgary, caron`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, barristers, calgary, caron No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 35-35. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: Justice de Montigny
DATED: March 17, 2006
APPEARANCES:
Ms. D. Jean Munn &
Ms. Rishma N. Shariff FOR THE APPLICANTS
Mr. Rick Garvin FOR THE RESPONDENT
SOLICITORS OF RECORD:
Caron & Partners LLP FOR THE APPLICANTS
Barristers & Solicitors
Calgary, Alberta
John H. Sims, Q.C. FOR THE RESPONDENT
Deputy Attorney General of Canada
