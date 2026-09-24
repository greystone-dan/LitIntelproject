# Discussion Units: case 2788

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **5**
- Paragraph source hashes: **30**
- Sub-themes: **12**

## 2788:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c32b23a44e9fb12a47ea6a5c3e6bca77e5c0ef0c39cae44a54e1795e5472ad42`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2788:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `abiodun, applicants, bukola, decision, immigration, judicial, reasons, review`
- Display key terms: `abiodun, bukola, judicial, review`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: abiodun, bukola, judicial, review Rule/authority context: They seek judicial review of the decision of the Refugee Appeal Division [RAD] dated January 18, 2019 confirming the decision of the Refugee Protection Division [RPD] dated September 26, 2018 that the Applicants are neit Operative outcome context: [2] For the reasons that follow, the application for judicial review is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4194463` offsets `463-474`; context: They seek judicial review of the decision of the Refugee Appeal Division [RAD] dated January 18, 2019 confirming the decision of the Refugee Protection Division [RPD] dated September 26, 2018 that the Applicants are neither Convention refugees nor persons in need of protection pursuant to paragraph 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
- Evidence: `disposition` cue `dismissed` at chunk `4194464` offsets `72-81`; context: [2] For the reasons that follow, the application for judicial review is dismissed.

#### Section text

Tiodunmo v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2019-11-22
Neutral citation
2019 FC 1489
File numbers
IMM-1227-19
Decision Content
Date: 20191122
Docket: IMM-1227-19
Citation: 2019 FC 1489
Ottawa, Ontario, November 22, 2019
PRESENT: The Honourable Mr. Justice Lafrenière
BETWEEN:
TITILAYO BUKOLA TIODUNMO, OLUWAFERANMI MARY TIODUNMO, OLUWAPAMILERINAYO LYDIA TIODUNMO,
SAHEED ABIODUN TIODUNMO
Applicants
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondents
JUDGMENT AND REASONS
I. Overview

[1] The Applicants are Nigerian citizens. The Principal Applicant is Titilayo Bukola Tiodunmo. The other Applicants are her husband, Saheed Abiodun Tiodunmo, and their minor daughters. They seek judicial review of the decision of the Refugee Appeal Division [RAD] dated January 18, 2019 confirming the decision of the Refugee Protection Division [RPD] dated September 26, 2018 that the Applicants are neither Convention refugees nor persons in need of protection pursuant to paragraph 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

[2] For the reasons that follow, the application for judicial review is dismissed.


## 2788:2 · paragraphs 3-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ac227f2eec40d71575b198b17eda0d335a140c80f70084b5cbb98b0fe538ded3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2788:2:subtheme:1 · paragraphs 3-4

- Raw key terms: `afraid, applicants, back, background, born, canada, claim, claimed`
- Display key terms: `afraid, back, background, born, claimed`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: afraid, back, background, born, claimed No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.

#### 2788:2:subtheme:2 · paragraphs 5-7

- Raw key terms: `applicants, nigeria, continued, family, harcourt, port, actually, agents`
- Display key terms: `nigeria, continued, family, harcourt, port, actually, agents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: nigeria, continued, family, harcourt, port, actually, agents Rule/authority context: [5] In assessing the Applicants’ claims pursuant to both sections 96 and 97 of the IRPA, the RPD noted that the Applicants’ extended family made their threats when Oluwapamilerinayo was born in 2012; however, the extende Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4194466` offsets `22-27`; context: [4] The determinative issue before the RPD was the existence of an internal flight alternative [IFA].
- Evidence: `governing_rule` cue `pursuant to` at chunk `4194467` offsets `40-51`; context: [5] In assessing the Applicants’ claims pursuant to both sections 96 and 97 of the IRPA, the RPD noted that the Applicants’ extended family made their threats when Oluwapamilerinayo was born in 2012; however, the extended family did not take any steps to carry out their threats for the next ﬁve years.
- Evidence: `counterargument_limitation` cue `however` at chunk `4194467` offsets `200-207`; context: [5] In assessing the Applicants’ claims pursuant to both sections 96 and 97 of the IRPA, the RPD noted that the Applicants’ extended family made their threats when Oluwapamilerinayo was born in 2012; however, the extended family did not take any steps to carry out their threats for the next ﬁve years.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194468` offsets `31-39`; context: [6] The RPD found there was no evidence that the agents of persecution had continued to search for the Applicants after they left Nigeria.
- Evidence: `counterargument_limitation` cue `but` at chunk `4194468` offsets `231-234`; context: The Applicants did not indicate that the secret cult as a whole was actually pursuing them, but rather just Saheed’s family members who were part of the cult.

#### 2788:2:subtheme:3 · paragraphs 8-11

- Raw key terms: `applicants, analysis, available, evidence, family, found, friends, harcourt`
- Display key terms: `analysis, available, family, friends, harcourt`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: analysis, available, family, friends, harcourt Position/evidence statements: [9] Before the RAD, the Applicants submitted that the RPD erred by failing to consider the relevant Jurisprudential Guide, using the wrong legal test in conducting its IFA analysis, failing to have regard to the pervasiv Rule/authority context: [9] Before the RAD, the Applicants submitted that the RPD erred by failing to consider the relevant Jurisprudential Guide, using the wrong legal test in conducting its IFA analysis, failing to have regard to the pervasiv Application context: It also considered the Applicants’ arguments that they would face difficulty because they lack friends and family there. Evidence spans paragraphs 8-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4194469` offsets `108-115`; context: The RPD considered whether it would be unduly harsh to expect the Applicants to relocate to Port Harcourt.
- Evidence: `evidence_fact` cue `found that` at chunk `4194469` offsets `455-465`; context: It ultimately found that the Applicants has not established it would be unreasonable for them to relocate to Port Harcourt.
- Evidence: `reasoning_application` cue `because` at chunk `4194469` offsets `273-280`; context: It also considered the Applicants’ arguments that they would face difficulty because they lack friends and family there.
- Evidence: `issue` cue `whether` at chunk `4194470` offsets `646-653`; context: The RAD refused to accept the three articles into evidence, stating: “[i]n the absence of those specific submissions, I do not know how that evidence relates to the Appellants or whether it meets the requirements for admissibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194470` offsets `66-74`; context: [8] On appeal to the RAD, the Applicants sought to adduce further evidence in the form of three emails containing news articles about cults in Nigeria, two of which pre-dated the RPD’s decision.
- Evidence: `party_position` cue `submitted` at chunk `4194471` offsets `35-44`; context: [9] Before the RAD, the Applicants submitted that the RPD erred by failing to consider the relevant Jurisprudential Guide, using the wrong legal test in conducting its IFA analysis, failing to have regard to the pervasive nature of traditional beliefs in Nigeria and failing to consider the hardship from cutting off contact with all family members and friends.
- Evidence: `governing_rule` cue `legal test` at chunk `4194471` offsets `139-149`; context: [9] Before the RAD, the Applicants submitted that the RPD erred by failing to consider the relevant Jurisprudential Guide, using the wrong legal test in conducting its IFA analysis, failing to have regard to the pervasive nature of traditional beliefs in Nigeria and failing to consider the hardship from cutting off contact with all family members and friends.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194472` offsets `47-55`; context: [10] The RAD conducted its own analysis of the evidence and agreed with the RPD that the Applicants had a viable IFA available to them in Port Harcourt.

#### Section text

II. Background Facts

[3] Titilayo and Saheed are the parents of two daughters, Oluwapamilerinayo (born in 2012) and Oluwaferanmi (born in 2014). In 2017, they left Nigeria and made a claim for refugee protection in Canada, claiming that Saheed’s extended family intended to mutilate their daughters as a form of traditional rites, and had threatened to kill the family unless they convert back to Islam. At the hearing at their refugee claim, the Applicants also claimed to be afraid of a secret cult into which Saheed had been inducted in 2004.

[4] The determinative issue before the RPD was the existence of an internal flight alternative [IFA]. At the outset of the hearing, the Applicants were notified of Port Harcourt, Nigeria as a potential IFA.

[5] In assessing the Applicants’ claims pursuant to both sections 96 and 97 of the IRPA, the RPD noted that the Applicants’ extended family made their threats when Oluwapamilerinayo was born in 2012; however, the extended family did not take any steps to carry out their threats for the next ﬁve years. The RPD also observed that the Applicants did not feel that the threats of violence were imminent, and they continued to live and work in the same place, and travel to and from Nigeria for work and pleasure without incident.

[6] The RPD found there was no evidence that the agents of persecution had continued to search for the Applicants after they left Nigeria. The Applicants did not indicate that the secret cult as a whole was actually pursuing them, but rather just Saheed’s family members who were part of the cult. The RPD found it was unlikely that, even if Saheed’s family could motivate the secret cult to look for the Applicants, it had the means to locate the Applicants in Port Harcourt given objective evidence that showed the cult did not have a national reach and did not operate in the south-east part of the country where Port Harcourt is located.

[7] The RPD concluded that the Applicants had an IFA available to them in Port Harcourt. The RPD considered whether it would be unduly harsh to expect the Applicants to relocate to Port Harcourt. It also considered the Applicants’ arguments that they would face difficulty because they lack friends and family there. The RPD also considered religious, economic and cultural factors and whether and how those factors affect women in the IFA. It ultimately found that the Applicants has not established it would be unreasonable for them to relocate to Port Harcourt.

[8] On appeal to the RAD, the Applicants sought to adduce further evidence in the form of three emails containing news articles about cults in Nigeria, two of which pre-dated the RPD’s decision. The RAD found that the Applicants failed to comply with Rule 3(3)(g)(iii) of the Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules] which requires appellants to make full and detailed submissions showing how the new evidence meets the requirements for admissibility. The RAD refused to accept the three articles into evidence, stating: “[i]n the absence of those specific submissions, I do not know how that evidence relates to the Appellants or whether it meets the requirements for admissibility.”

[9] Before the RAD, the Applicants submitted that the RPD erred by failing to consider the relevant Jurisprudential Guide, using the wrong legal test in conducting its IFA analysis, failing to have regard to the pervasive nature of traditional beliefs in Nigeria and failing to consider the hardship from cutting off contact with all family members and friends.

[10] The RAD conducted its own analysis of the evidence and agreed with the RPD that the Applicants had a viable IFA available to them in Port Harcourt.


## 2788:3 · paragraphs 12-12

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `549b4dc51139285cb38a3244e1d4b6c914e886326d8379dda9a39e291ad51eb3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2788:3:subtheme:1 · paragraphs 12-12

- Raw key terms: `determined, issues`
- Display key terms: `determined, issues`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: determined, issues No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 12-12. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

III. Issues to be Determined

## 2788:4 · paragraphs 13-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c0a44e51acbe8bf90c5bc47d3524107994254df04c3f7419dbfb2075a7821a98`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2788:4:subtheme:1 · paragraphs 13-14

- Raw key terms: `evidence, issues, review, standard, admissibility, admit, admitted, appeal`
- Display key terms: `issues, review, standard, admissibility, admit, admitted`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: issues, review, standard, admissibility, admit, admitted Position/evidence statements: [11] The Applicants submit that the issues before this Court are as follows: A. Rule/authority context: Standard of Review | [12] The standard of review to be applied in this case is not in dispute. Application context: [12] The standard of review to be applied in this case is not in dispute. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4194473` offsets `36-42`; context: [11] The Applicants submit that the issues before this Court are as follows:
A.
- Evidence: `party_position` cue `submit` at chunk `4194473` offsets `20-26`; context: [11] The Applicants submit that the issues before this Court are as follows:
A.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194473` offsets `132-140`; context: “Did the Refugee Appeal Division fail to admit into evidence documentation which should have been admitted into evidence?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4194473` offsets `290-308`; context: Standard of Review
- Evidence: `issue` cue `issues` at chunk `4194474` offsets `110-116`; context: The RAD’s determinations of factual issues and issues of mixed fact and law are reviewable on a reasonableness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194474` offsets `406-414`; context: This standard applies to the RAD’s determination as to the availability of an IFA (see Tariq v Canada (Citizenship and Immigration), 2017 FC 1017 at para 14) and the RAD’s assessment of the admissibility of new evidence (see Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 29 [Singh]).
- Evidence: `governing_rule` cue `standard of review` at chunk `4194474` offsets `9-27`; context: [12] The standard of review to be applied in this case is not in dispute.
- Evidence: `reasoning_application` cue `applied` at chunk `4194474` offsets `34-41`; context: [12] The standard of review to be applied in this case is not in dispute.

#### 2788:4:subtheme:2 · paragraphs 15-18

- Raw key terms: `evidence, applicants, admit, articles, decision, documents, failed, meets`
- Display key terms: `admit, articles, documents, failed, meets`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: admit, articles, documents, failed, meets Position/evidence statements: [14] The Applicants submit that the refusal by the RAD to admit into evidence the three articles, and more particularly the article dated October 12, 2018, was unreasonable. Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4194475` offsets `38-45`; context: [13] The Court’s role is to determine whether the RAD’s decision is justifiable, transparent and intelligible and whether it falls within a range of possible outcomes, defensible in respect of the evidence before the RAD and law (see Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).
- Evidence: `evidence_fact` cue `evidence` at chunk `4194475` offsets `197-205`; context: [13] The Court’s role is to determine whether the RAD’s decision is justifiable, transparent and intelligible and whether it falls within a range of possible outcomes, defensible in respect of the evidence before the RAD and law (see Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).
- Evidence: `party_position` cue `submit` at chunk `4194476` offsets `20-26`; context: [14] The Applicants submit that the refusal by the RAD to admit into evidence the three articles, and more particularly the article dated October 12, 2018, was unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194476` offsets `69-77`; context: [14] The Applicants submit that the refusal by the RAD to admit into evidence the three articles, and more particularly the article dated October 12, 2018, was unreasonable.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4194476` offsets `382-388`; context: Relevance cannot be determined in a vacuum.
- Evidence: `evidence_fact` cue `evidence` at chunk `4194477` offsets `159-167`; context: [15] It is now firmly established that an appellant’s memorandum on appeal to the RAD must include full and detailed submissions regarding how any documentary evidence the appellant wishes to rely on not only meets the requirements of subsection 110(4), but also how that evidence relates to the appellant: Singh at para 45.
- Evidence: `counterargument_limitation` cue `but` at chunk `4194477` offsets `254-257`; context: [15] It is now firmly established that an appellant’s memorandum on appeal to the RAD must include full and detailed submissions regarding how any documentary evidence the appellant wishes to rely on not only meets the requirements of subsection 110(4), but also how that evidence relates to the appellant: Singh at para 45.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4194478` offsets `69-77`; context: [16] At paragraphs 2 and 3 of their Written Statement Concerning New Evidence submitted to the RAD, the Applicants simply state that they are presenting evidence referred to in section 110(4) of the IRPA consisting of “[n]ews articles that came out subsequent to the decision about cults in Nigeria.

#### 2788:4:subtheme:3 · paragraphs 19-20

- Raw key terms: `articles, circumstances, evidence, whether, accepting, applicants, arose, available`
- Display key terms: `articles, circumstances, whether, accepting, arose, available`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: articles, circumstances, whether, accepting, arose, available Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4194479` offsets `367-374`; context: It was not the RAD’s role to sift through the articles to figure out by itself whether the evidence met the requirements of subsection 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4194479` offsets `62-70`; context: [17] It was incumbent on the Applicants to establish that the evidence arose after the rejection of their claim or was not reasonably available to them, or that they could not reasonably have been expected in the circumstances to have presented the evidence at the time of the rejection.
- Evidence: `issue` cue `Whether` at chunk `4194480` offsets `136-143`; context: Whether the RPD and RAD confused two different cults
- Evidence: `evidence_fact` cue `evidence` at chunk `4194480` offsets `123-131`; context: [18] In the circumstances, I am not satisfied that the RAD committed a reviewable error in not accepting the articles into evidence.

#### 2788:4:subtheme:4 · paragraphs 21-22

- Raw key terms: `applicants, awo-opa, cult, cults, imole, relevant, addressing, agents`
- Display key terms: `awo-opa, cult, cults, imole, relevant, addressing, agents`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: awo-opa, cult, cults, imole, relevant, addressing, agents Position/evidence statements: The Applicants submit that the fact that the two divisions identify two different cults as the feared agents of persecution means that they are not addressing the same issue. Application context: For the following reasons, I conclude that there is no merit to the Applicants’ position that the RAD was confused about which cult was at issue. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4194481` offsets `320-325`; context: The Applicants submit that the fact that the two divisions identify two different cults as the feared agents of persecution means that they are not addressing the same issue.
- Evidence: `party_position` cue `submit` at chunk `4194481` offsets `167-173`; context: The Applicants submit that the fact that the two divisions identify two different cults as the feared agents of persecution means that they are not addressing the same issue.
- Evidence: `reasoning_application` cue `conclude` at chunk `4194481` offsets `356-364`; context: For the following reasons, I conclude that there is no merit to the Applicants’ position that the RAD was confused about which cult was at issue.
- Evidence: `evidence_fact` cue `testimony` at chunk `4194482` offsets `94-103`; context: [20] Saheed consistently and singularly referred to the relevant cult as Imole throughout his testimony.

#### 2788:4:subtheme:5 · paragraphs 23-23

- Raw key terms: `analysis, cannot, circumstances, cult, decision, engaged, faulted, name`
- Display key terms: `analysis, cannot, circumstances, cult, engaged, faulted, name`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: analysis, cannot, circumstances, cult, engaged, faulted, name Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4194483` offsets `131-138`; context: Whether the RAD engaged in a truncated IFA analysis

#### 2788:4:subtheme:6 · paragraphs 24-27

- Raw key terms: `agents, applicants, considered, decision, failed, find, likelihood, motivation`
- Display key terms: `agents, considered, failed, find, likelihood, motivation`
- Argument roles: `counterargument_limitation, disposition, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, party_position, reasoning_application Display terms: agents, considered, failed, find, likelihood, motivation Position/evidence statements: They submit the RAD failed however to consider the likelihood the agents of persecution would find the Applicants in the IFA. Application context: I find no reviewable error by the RAD in this component of its decision. | [24] Being substantially in agreement with the Respondent’s written submissions, I conclude that the application for judicial review should be dismissed. Operative outcome context: [24] Being substantially in agreement with the Respondent’s written submissions, I conclude that the application for judicial review should be dismissed. Evidence spans paragraphs 24-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4194484` offsets `169-175`; context: They submit the RAD failed however to consider the likelihood the agents of persecution would find the Applicants in the IFA.
- Evidence: `counterargument_limitation` cue `however` at chunk `4194484` offsets `191-198`; context: They submit the RAD failed however to consider the likelihood the agents of persecution would find the Applicants in the IFA.
- Evidence: `reasoning_application` cue `I find` at chunk `4194485` offsets `451-457`; context: I find no reviewable error by the RAD in this component of its decision.
- Evidence: `reasoning_application` cue `conclude` at chunk `4194486` offsets `83-91`; context: [24] Being substantially in agreement with the Respondent’s written submissions, I conclude that the application for judicial review should be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4194486` offsets `143-152`; context: [24] Being substantially in agreement with the Respondent’s written submissions, I conclude that the application for judicial review should be dismissed.

#### Section text

[11] The Applicants submit that the issues before this Court are as follows:
A. “Did the Refugee Appeal Division fail to admit into evidence documentation which should have been admitted into evidence?”
B. “Does the reasoning of the Refugee Appeal Division suffer from cult confusion?”
IV. Standard of Review

[12] The standard of review to be applied in this case is not in dispute. The RAD’s determinations of factual issues and issues of mixed fact and law are reviewable on a reasonableness standard. This standard applies to the RAD’s determination as to the availability of an IFA (see Tariq v Canada (Citizenship and Immigration), 2017 FC 1017 at para 14) and the RAD’s assessment of the admissibility of new evidence (see Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 29 [Singh]).

[13] The Court’s role is to determine whether the RAD’s decision is justifiable, transparent and intelligible and whether it falls within a range of possible outcomes, defensible in respect of the evidence before the RAD and law (see Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).
V. Analysis
A. Whether the RAD failed to admit documents which should have been admitted

[14] The Applicants submit that the refusal by the RAD to admit into evidence the three articles, and more particularly the article dated October 12, 2018, was unreasonable. They argue “[s]ometimes documents speak for themselves” and that the relevance of the documents provided should have been apparent to the RAD without specific submissions on the matter. I disagree. Relevance cannot be determined in a vacuum.

[15] It is now firmly established that an appellant’s memorandum on appeal to the RAD must include full and detailed submissions regarding how any documentary evidence the appellant wishes to rely on not only meets the requirements of subsection 110(4), but also how that evidence relates to the appellant: Singh at para 45. In the present case, the Applicants failed to provide any substantive submissions to the RAD.

[16] At paragraphs 2 and 3 of their Written Statement Concerning New Evidence submitted to the RAD, the Applicants simply state that they are presenting evidence referred to in section 110(4) of the IRPA consisting of “[n]ews articles that came out subsequent to the decision about cults in Nigeria.” At paragraph 5 of the form, they leave blank a space for the page number in their appellants’ memorandum where they were meant to explain how the new evidence meets the requirements of section 110(4) and how it relates to them. No mention is made of the three articles in the appellants’ memorandum.

[17] It was incumbent on the Applicants to establish that the evidence arose after the rejection of their claim or was not reasonably available to them, or that they could not reasonably have been expected in the circumstances to have presented the evidence at the time of the rejection. It was not the RAD’s role to sift through the articles to figure out by itself whether the evidence met the requirements of subsection 110(4).

[18] In the circumstances, I am not satisfied that the RAD committed a reviewable error in not accepting the articles into evidence.
B. Whether the RPD and RAD confused two different cults

[19] The RPD refers to the “Awo-Opa” cult as relevant to the feared agents of persecution in its decision while the RAD only mentions the “Imole” cult. The Applicants submit that the fact that the two divisions identify two different cults as the feared agents of persecution means that they are not addressing the same issue. For the following reasons, I conclude that there is no merit to the Applicants’ position that the RAD was confused about which cult was at issue.

[20] Saheed consistently and singularly referred to the relevant cult as Imole throughout his testimony. The only reference to the Awo-Opa cult was raised by the Applicants’ counsel in an exchange with Saheed regarding a photograph showing a cult-initiation with a caption referring to a number of cults, including the Awo-Opa. Counsel asked Saheed why there was no documentary evidence about the Imole cult. Saheed replied that the cults identiﬁed on the photograph’s caption, including the Awo-Opa cult, were “all the same” as the Imole cult.

[21] In the circumstances, the RAD cannot be faulted for referring in its decision to the cult by the very name used by Saheed.
C. Whether the RAD engaged in a truncated IFA analysis

[22] The Applicants acknowledge that the RAD considered the motivation of the agents of persecution to find the Applicants in the IFA and their ability to do that. They submit the RAD failed however to consider the likelihood the agents of persecution would find the Applicants in the IFA. According to the Applicants, as long as there is a likelihood of being discovered by the feared agents of persecution in any manner at any time, the identified IFA location is not viable. In my view, any assertion that the RAD failed to consider the likelihood of discovery is semantic at best, and demonstrably false when one considers the RAD’s decision in context.

[23] The RAD concluded the Applicants would be safe from Imole cultists in Port Harcourt, that the Imole cult’s reach did not extend to Port Harcourt, and that the Applicants failed to establish “the alleged agent of harm would have the motivation or capacity to harm or persecute this family in Port Harcourt”. It is implicit in this that the RAD considered the likelihood the cult and the agents of persecution would find the Applicants in the IFA. I find no reviewable error by the RAD in this component of its decision.
VI. Conclusion

[24] Being substantially in agreement with the Respondent’s written submissions, I conclude that the application for judicial review should be dismissed.

[25] There are no questions for certification.


## 2788:5 · paragraphs 28-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b3cd4b35c1bf13efa19bd7919782fa95592a5f3363a51bee5058d83ef09a45e0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2788:5:subtheme:1 · paragraphs 28-29

- Raw key terms: `imm-1227-19, judgment, lafreni, abiodun, appearances, applicants, application, attorney`
- Display key terms: `imm-1227-19, lafreni, abiodun`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: imm-1227-19, lafreni, abiodun Operative outcome context: JUDGMENT IN IMM-1227-19 THIS COURT’S JUDGMENT is that: The application for judicial review is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4194487` offsets `141-150`; context: JUDGMENT IN IMM-1227-19
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.

#### Section text

JUDGMENT IN IMM-1227-19
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.
"Roger R. Lafrenière"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-1227-19
STYLE OF CAUSE:
TITILAYO BUKOLA TIODUNMO, OLUWAFERANMI MARY TIODUNMO, OLUWAPAMILERINAYO LYDIA TIODUNMO, SAHEED ABIODUN TIODUNMO v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Winnipeg, Manitoba
DATE OF HEARING:
November 13, 2019
JUDGMENT AND REASONS:
LAFRENIÈRE J.
DATED:
November 22, 2019
APPEARANCES:
David Matas
For The Applicants
Brendan Friesen
FOR THE RESPONDENT
SOLICITORS OF RECORD:
David Matas
Barrister and Solicitor
Winnipeg, Manitoba
FOR THE APPLICANTS
Attorney General of Canada
Winnipeg, Manitoba
FOR THE RESPONDENT
