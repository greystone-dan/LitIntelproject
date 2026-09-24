# Discussion Units: case 20779

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **39**
- Continuity pairs: **38**
- Discussion Units: **1**
- Paragraph source hashes: **39**
- Sub-themes: **14**

## 20779:1 · paragraphs 0-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5c9c1b2e16020d37e13fa3913dc2a9e83152399e0a2c0be3dad7bfa107a4961d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20779:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, evidence, ferguson, application, jamaica, risk, assessment, country`
- Display key terms: `ferguson, jamaica, risk, assessment, country`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: ferguson, jamaica, risk, assessment, country Position/evidence statements: Ferguson is very openly lesbian, counsel respectfully submits that there is a very serious possibility that the Applicant would be at risk should she return to her country of nationality. Rule/authority context: [4] On the PRRA application form under the heading “Reasons for Applying For Pre-Removal Risk Assessment (PRRA)” Ms. Application context: [1] The Applicant says that the Pre-removal Risk Assessment (PRRA) Officer rejected her application because he did not believe that she was lesbian. Operative outcome context: The officer nonetheless dismissed the application on the basis that there was insufficient evidence to establish that Ms. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982117` offsets `247-255`; context: The Respondent says that the PRRA officer rejected the application because there was insufficient evidence presented to prove, on the balance of probabilities, that the Applicant is lesbian.
- Evidence: `reasoning_application` cue `because` at chunk `4982117` offsets `100-107`; context: [1] The Applicant says that the Pre-removal Risk Assessment (PRRA) Officer rejected her application because he did not believe that she was lesbian.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982118` offsets `136-144`; context: [2] For the reasons that follow, I am of the opinion that no hearing was required as the decision was based solely on the weight of the evidence presented and did not rest on the Applicant’s credibility.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4982120` offsets `187-195`; context: Under the heading “Supporting Evidence” where she is asked to provide a list of the written documents included with the application that will “clearly act as evidence in support of your application for a Pre-removal Risk Assessment", two types of documents were listed, news articles and affidavits, which she indicated would support her requests for protection by providing “objective proof of risk".
- Evidence: `governing_rule` cue `under` at chunk `4982120` offsets `33-38`; context: [4] On the PRRA application form under the heading “Reasons for Applying For Pre-Removal Risk Assessment (PRRA)” Ms.
- Evidence: `party_position` cue `submits` at chunk `4982121` offsets `1017-1024`; context: Ferguson is very openly lesbian, counsel respectfully submits that there is a very serious possibility that the Applicant would be at risk should she return to her country of nationality.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982121` offsets `106-114`; context: Ferguson's former counsel wrote to the PRRA officer enclosing “the evidence being relied upon by the Applicant and submissions in support of her application".
- Evidence: `evidence_fact` cue `evidence` at chunk `4982122` offsets `118-126`; context: Ferguson's claim agreed, without reservation, on the basis of documentary evidence, that lesbians in Jamaica are at risk of severe physical abuse on account of their sexual orientation.
- Evidence: `disposition` cue `dismissed` at chunk `4982122` offsets `254-263`; context: The officer nonetheless dismissed the application on the basis that there was insufficient evidence to establish that Ms.

#### 20779:1:subtheme:2 · paragraphs 7-8

- Raw key terms: `applicant's, application, credibility, decision, evidence, ferguson, hearing, held`
- Display key terms: `applicant's, credibility, ferguson, hearing`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: applicant's, credibility, ferguson, hearing Rule/authority context: Ferguson submits that the basis for the PRRA officer’s determination rejecting the application was her credibility and accordingly, pursuant to section 113 of the Immigration and Refugee Protection Act, S. Application context: Ferguson submits that the basis for the PRRA officer’s determination rejecting the application was her credibility and accordingly, pursuant to section 113 of the Immigration and Refugee Protection Act, S. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4982123` offsets `462-469`; context: The prescribed factors for determining whether a hearing is to be held are set out in section 167 of the Immigration and Refugee Protection Regulations, SOR/2002-227:
167.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982123` offsets `743-751`; context: For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
(a) whether there is evidence that raises a serious issue of the applicant's credibility and is related to the factors set out in sections 96 and 97 of the Act;
(b) whether the evidence is central to the decision with respect to the application for protection; and
(c) whether the evidence, if accepted, would justify allowing the application for protection.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4982123` offsets `140-151`; context: Ferguson submits that the basis for the PRRA officer’s determination rejecting the application was her credibility and accordingly, pursuant to section 113 of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `accordingly` at chunk `4982123` offsets `127-138`; context: Ferguson submits that the basis for the PRRA officer’s determination rejecting the application was her credibility and accordingly, pursuant to section 113 of the Immigration and Refugee Protection Act, S.
- Evidence: `issue` cue `issue` at chunk `4982124` offsets `275-280`; context: The issue is whether the requirements set out in subsection 167(a) were met.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982124` offsets `469-477`; context: The Applicant's position is that they were; the officer's rejection of her application was based on the rejection of her evidence that she was openly lesbian, and thus the decision rested on her credibility.
- Evidence: `counterargument_limitation` cue `but` at chunk `4982124` offsets `638-641`; context: The Respondent takes the position that the decision was not based on credibility, but rather on a finding that there was insufficient evidence presented to establish, on the balance of probabilities, that Ms.

#### 20779:1:subtheme:3 · paragraphs 9-10

- Raw key terms: `applicant, hearing, issue, officer, oral, view, accepted, alleged`
- Display key terms: `hearing, officer, oral, view, accepted, alleged`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: hearing, officer, oral, view, accepted, alleged Rule/authority context: For the reasons that follow, I am of the view that the officer made no error and an oral hearing was not required under the Act or Regulations. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4982125` offsets `17-22`; context: [9] There was an issue raised by the Applicant in the pleadings regarding an alleged breach of the Canadian Bill of Rights, S.
- Evidence: `counterargument_limitation` cue `however` at chunk `4982125` offsets `142-149`; context: 44; however, it was not pursued in oral argument and, in my view, was without merit.
- Evidence: `issue` cue `issue` at chunk `4982126` offsets `60-65`; context: [10] If the officer’s determination was based on a “serious issue of the applicant’s credibility” it is accepted that in Ms.
- Evidence: `governing_rule` cue `under` at chunk `4982126` offsets `344-349`; context: For the reasons that follow, I am of the view that the officer made no error and an oral hearing was not required under the Act or Regulations.

#### 20779:1:subtheme:4 · paragraphs 11-15

- Raw key terms: `applicant, counsel, evidence, officer, submitted, support, application, canada`
- Display key terms: `officer, submitted, support`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: officer, submitted, support Position/evidence statements: [11] The Applicant submitted that while the officer did not explicitly state that the decision was one of credibility, it could not be anything other than credibility. | [12] The Respondent submits that the legislative scheme makes it clear that applicants who submit a PRRA application or any other application governed by the Act must present evidence to support that application. Rule/authority context: This, it is submitted, is essentially a finding of credibility that attracts the requirement to hold a hearing under section 167 of the Regulations. Application context: Her counsel writes in the memorandum of argument: “Whether because the Applicant had failed to produce sufficient evidence on the balance of probabilities, or for any other reason, the PRRA officer has not believed the s | Ferguson of her right to apply for a Pre-removal Risk Assessment states that information in written submissions will be considered by the PRRA officer. Evidence spans paragraphs 11-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4982127` offsets `331-338`; context: Her counsel writes in the memorandum of argument: “Whether because the Applicant had failed to produce sufficient evidence on the balance of probabilities, or for any other reason, the PRRA officer has not believed the statement that the Applicant is a lesbian”.
- Evidence: `party_position` cue `submitted` at chunk `4982127` offsets `19-28`; context: [11] The Applicant submitted that while the officer did not explicitly state that the decision was one of credibility, it could not be anything other than credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982127` offsets `394-402`; context: Her counsel writes in the memorandum of argument: “Whether because the Applicant had failed to produce sufficient evidence on the balance of probabilities, or for any other reason, the PRRA officer has not believed the statement that the Applicant is a lesbian”.
- Evidence: `governing_rule` cue `under` at chunk `4982127` offsets `654-659`; context: This, it is submitted, is essentially a finding of credibility that attracts the requirement to hold a hearing under section 167 of the Regulations.
- Evidence: `reasoning_application` cue `because` at chunk `4982127` offsets `339-346`; context: Her counsel writes in the memorandum of argument: “Whether because the Applicant had failed to produce sufficient evidence on the balance of probabilities, or for any other reason, the PRRA officer has not believed the statement that the Applicant is a lesbian”.
- Evidence: `party_position` cue `submits` at chunk `4982128` offsets `20-27`; context: [12] The Respondent submits that the legislative scheme makes it clear that applicants who submit a PRRA application or any other application governed by the Act must present evidence to support that application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982128` offsets `175-183`; context: [12] The Respondent submits that the legislative scheme makes it clear that applicants who submit a PRRA application or any other application governed by the Act must present evidence to support that application.
- Evidence: `party_position` cue `submitted` at chunk `4982129` offsets `32-41`; context: [13] In response, the Applicant submitted that it is common practice for immigration counsel to file written submissions on behalf of clients which include statements of evidence, and that there is nothing in either the Act or Regulations or in the policy and procedures of the Respondent that would indicate that such evidence is not to be considered.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982129` offsets `170-178`; context: [13] In response, the Applicant submitted that it is common practice for immigration counsel to file written submissions on behalf of clients which include statements of evidence, and that there is nothing in either the Act or Regulations or in the policy and procedures of the Respondent that would indicate that such evidence is not to be considered.
- Evidence: `reasoning_application` cue `apply` at chunk `4982129` offsets `471-476`; context: Ferguson of her right to apply for a Pre-removal Risk Assessment states that information in written submissions will be considered by the PRRA officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982130` offsets `129-137`; context: [14] With respect, in my view, that form letter makes it clear that the submissions are to set out reasons and explanations –not evidence.
- Evidence: `party_position` cue `submitted` at chunk `4982131` offsets `18-27`; context: [15] Both parties submitted numerous authorities to the Court in support of their respective positions.

#### 20779:1:subtheme:5 · paragraphs 16-17

- Raw key terms: `approach, court, officer, review, view, accept, appeal, appeared`
- Display key terms: `approach, officer, review, view, accept, appeared`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: approach, officer, review, view, accept, appeared Rule/authority context: Most of the cases to which the Court was referred were determined on the particular facts of the decision under review. | [17] In my view, the approach to be taken by both the officer and this Court, sitting in review, is to be guided by the principles set out by the Federal Court of Appeal in Carrillo v. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4982132` offsets `143-148`; context: [16] Counsel for both parties appeared to be of the same mind that, in the words of Respondent counsel, there is no principled approach to the issue of credibility versus sufficiency of evidence to be gleaned from these authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982132` offsets `186-194`; context: [16] Counsel for both parties appeared to be of the same mind that, in the words of Respondent counsel, there is no principled approach to the issue of credibility versus sufficiency of evidence to be gleaned from these authorities.
- Evidence: `governing_rule` cue `under` at chunk `4982132` offsets `365-370`; context: Most of the cases to which the Court was referred were determined on the particular facts of the decision under review.
- Evidence: `governing_rule` cue `principles` at chunk `4982133` offsets `120-130`; context: [17] In my view, the approach to be taken by both the officer and this Court, sitting in review, is to be guided by the principles set out by the Federal Court of Appeal in Carrillo v.

#### 20779:1:subtheme:6 · paragraphs 18-19

- Raw key terms: `appeal, court, evidence, find, proof, standard, abused, allowed`
- Display key terms: `find, proof, standard, abused, allowed`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: find, proof, standard, abused, allowed Position/evidence statements: She claimed that she had been abused by her common-law spouse and that her spouse's brother, a police officer, had helped her spouse find her when she hid after the beating. Application context: [19] The Court of Appeal, in the course of its reasons, engaged in a detailed and informative discussion of the concepts of burden of proof, standard of proof, and quality of the evidence necessary to meet the burden of  Operative outcome context: Her refugee claim was dismissed by the Board. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4982134` offsets `270-275`; context: The principal issue before the Immigration and Refugee Protection Board was whether state protection was available to Ms.
- Evidence: `party_position` cue `claimed` at chunk `4982134` offsets `86-93`; context: She claimed that she had been abused by her common-law spouse and that her spouse's brother, a police officer, had helped her spouse find her when she hid after the beating.
- Evidence: `evidence_fact` cue `found that` at chunk `4982134` offsets `447-457`; context: It found that she was not a credible or trustworthy witness with respect to her efforts to seek state protection in Mexico.
- Evidence: `disposition` cue `dismissed` at chunk `4982134` offsets `420-429`; context: Her refugee claim was dismissed by the Board.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982135` offsets `179-187`; context: [19] The Court of Appeal, in the course of its reasons, engaged in a detailed and informative discussion of the concepts of burden of proof, standard of proof, and quality of the evidence necessary to meet the burden of proof, all of which I find to be very useful in the present case and which, in my view, ought to be kept in mind by PRRA officers when considering applications.
- Evidence: `reasoning_application` cue `I find` at chunk `4982135` offsets `240-246`; context: [19] The Court of Appeal, in the course of its reasons, engaged in a detailed and informative discussion of the concepts of burden of proof, standard of proof, and quality of the evidence necessary to meet the burden of proof, all of which I find to be very useful in the present case and which, in my view, ought to be kept in mind by PRRA officers when considering applications.

#### 20779:1:subtheme:7 · paragraphs 20-21

- Raw key terms: `bears, burden, proof, administrative, applicant, applications, asking, bayavuge`
- Display key terms: `bears, burden, proof, administrative, applications, asking, bayavuge`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: bears, burden, proof, administrative, applications, asking, bayavuge Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4982136` offsets `26-33`; context: [20] In every proceeding, whether judicial or administrative, one party has the burden of proof.

#### 20779:1:subtheme:8 · paragraphs 22-23

- Raw key terms: `applicant, balance, burden, each, evidence, evidentiary, fact, facts`
- Display key terms: `balance, burden, each, evidentiary, fact, facts`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: balance, burden, each, evidentiary, fact, facts Application context: Accordingly, while an applicant may have met the evidentiary burden because evidence of each essential fact has been presented, he may not have met the legal burden because the evidence presented does not prove the facts Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4982138` offsets `816-821`; context: As will be discussed below, I hold that she did present some evidence of her sexual orientation and thus can be said to have met her evidentiary burden – she presented evidence of each material fact in issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982138` offsets `379-387`; context: That is proved by presenting evidence to the officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982139` offsets `60-68`; context: [23] As the Court of Appeal pointed out in Carrillo not all evidence is of the same quality.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4982139` offsets `93-104`; context: Accordingly, while an applicant may have met the evidentiary burden because evidence of each essential fact has been presented, he may not have met the legal burden because the evidence presented does not prove the facts required on the balance of probabilities.

#### 20779:1:subtheme:9 · paragraphs 24-25

- Raw key terms: `evidence, legal, weight, whether, above, applicant, assess, assessments`
- Display key terms: `legal, weight, whether, above, assess, assessments`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: legal, weight, whether, above, assess, assessments Application context: Findings of credibility may be made on the basis that previous statements of the witness contradict or are inconsistent with the evidence now being offered (see for example Karimi, above), or because the witness failed t Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4982140` offsets `26-33`; context: [24] The determination of whether the evidence presented meets the legal burden will depend very much on the weight given to the evidence that has been presented.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982140` offsets `38-46`; context: [24] The determination of whether the evidence presented meets the legal burden will depend very much on the weight given to the evidence that has been presented.
- Evidence: `issue` cue `whether` at chunk `4982141` offsets `170-177`; context: First, he may assess whether the evidence is credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982141` offsets `34-42`; context: [25] When a PRRA applicant offers evidence, in either oral or documentary form, the officer may engage in two separate assessments of that evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4982141` offsets `529-536`; context: Findings of credibility may be made on the basis that previous statements of the witness contradict or are inconsistent with the evidence now being offered (see for example Karimi, above), or because the witness failed to tender this important evidence at an earlier opportunity, thus bringing into question whether it is a recent fabrication (see for example Sidhu v.

#### 20779:1:subtheme:10 · paragraphs 26-28

- Raw key terms: `assessment, evidence, probative, because, considering, credibility, fact, found`
- Display key terms: `assessment, probative, because, considering, credibility, fact`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: assessment, probative, because, considering, credibility, fact Application context: Invariably this occurs when the trier of fact is of the view that the answer to the first question is irrelevant because the evidence is to be given little or no weight, even if it is found to be reliable evidence. | [27] Evidence tendered by a witness with a personal interest in the matter may also be examined for its weight before considering its credibility because typically this sort of evidence requires corroboration if it is to Evidence spans paragraphs 26-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4982142` offsets `384-391`; context: It is open to the trier of fact, in considering the evidence, to move immediately to an assessment of weight or probative value without considering whether it is credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982142` offsets `41-49`; context: [26] If the trier of fact finds that the evidence is credible, then an assessment must be made as to the weight that is to be given to it.
- Evidence: `reasoning_application` cue `because` at chunk `4982142` offsets `521-528`; context: Invariably this occurs when the trier of fact is of the view that the answer to the first question is irrelevant because the evidence is to be given little or no weight, even if it is found to be reliable evidence.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4982143` offsets `5-13`; context: [27] Evidence tendered by a witness with a personal interest in the matter may also be examined for its weight before considering its credibility because typically this sort of evidence requires corroboration if it is to have probative value.
- Evidence: `reasoning_application` cue `because` at chunk `4982143` offsets `146-153`; context: [27] Evidence tendered by a witness with a personal interest in the matter may also be examined for its weight before considering its credibility because typically this sort of evidence requires corroboration if it is to have probative value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982144` offsets `14-22`; context: [28] The only evidence presented concerning Ms.

#### 20779:1:subtheme:11 · paragraphs 29-30

- Raw key terms: `client, counsel, evidence, informal, prra, ability, administrative, admit`
- Display key terms: `client, informal, prra, ability, administrative, admit`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: client, informal, prra, ability, administrative, admit Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4982145` offsets `12-17`; context: [29] I take issue with the position of the Respondent in its memorandum of argument that a statement made by counsel can never be evidence and thus, presumably, can never be found to have any probative value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982145` offsets `130-138`; context: [29] I take issue with the position of the Respondent in its memorandum of argument that a statement made by counsel can never be evidence and thus, presumably, can never be found to have any probative value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982146` offsets `28-36`; context: [30] If the strict rules of evidence were imposed on informal administrative processes, such as the PRRA determination process, their ability to function effectively and promptly would be impaired.

#### 20779:1:subtheme:12 · paragraphs 31-33

- Raw key terms: `evidence, fact, given, prra, statement, weight, applicant, counsel`
- Display key terms: `fact, given, prra, statement, weight`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: fact, given, prra, statement, weight Position/evidence statements: [31] Accepting that counsel may submit evidence directly to the PRRA officer, the question will always remain, as it does for all tendered evidence, as to the degree of weight to be given to that evidence. | Had the statement been affirmed by the Applicant in a sworn affidavit submitted with her application, it would have been deserving of somewhat greater weight than it was given. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4982147` offsets `82-90`; context: [31] Accepting that counsel may submit evidence directly to the PRRA officer, the question will always remain, as it does for all tendered evidence, as to the degree of weight to be given to that evidence.
- Evidence: `party_position` cue `submit` at chunk `4982147` offsets `32-38`; context: [31] Accepting that counsel may submit evidence directly to the PRRA officer, the question will always remain, as it does for all tendered evidence, as to the degree of weight to be given to that evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982147` offsets `39-47`; context: [31] Accepting that counsel may submit evidence directly to the PRRA officer, the question will always remain, as it does for all tendered evidence, as to the degree of weight to be given to that evidence.
- Evidence: `party_position` cue `submitted` at chunk `4982148` offsets `226-235`; context: Had the statement been affirmed by the Applicant in a sworn affidavit submitted with her application, it would have been deserving of somewhat greater weight than it was given.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982148` offsets `118-126`; context: [32] When, as here, the fact asserted is critical to the PRRA application, it was open to the officer to require more evidence to satisfy the legal burden.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982149` offsets `40-48`; context: [33] The weight the trier of fact gives evidence tendered in a proceeding is not a science.
- Evidence: `counterargument_limitation` cue `but` at chunk `4982149` offsets `131-134`; context: Persons may weigh evidence differently but there is a reasonable range of weight within which the assessment of the evidence’s weight should fall.

#### 20779:1:subtheme:13 · paragraphs 34-36

- Raw key terms: `applicant, application, based, counsel, decision, evidence, lesbian, officer`
- Display key terms: `based, lesbian, officer`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue Display terms: based, lesbian, officer Rule/authority context: [34] It is also my view that there is nothing in the officer's decision under review which would indicate that any part of it was based on the Applicant's credibility. Operative outcome context: [36] For these reasons, this application is dismissed. Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4982150` offsets `585-593`; context: In my view, that determination does not bring into question the Applicant’s credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982150` offsets `311-319`; context: He states that there is insufficient objective evidence to establish that she is lesbian.
- Evidence: `governing_rule` cue `under` at chunk `4982150` offsets `72-77`; context: [34] It is also my view that there is nothing in the officer's decision under review which would indicate that any part of it was based on the Applicant's credibility.
- Evidence: `counterargument_limitation` cue `but` at chunk `4982150` offsets `431-434`; context: In short, he found that there was some evidence – the statement of counsel – but that it was insufficient to prove, on the balance of probabilities, that Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4982151` offsets `327-335`; context: However, every applicant for a Pre-removal Risk Assessment, and their counsel, must take responsibility to ensure that all of the relevant evidence is before the officer and, of equal importance, that they present the best evidence in support of the application.
- Evidence: `counterargument_limitation` cue `However` at chunk `4982151` offsets `188-195`; context: However, every applicant for a Pre-removal Risk Assessment, and their counsel, must take responsibility to ensure that all of the relevant evidence is before the officer and, of equal importance, that they present the best evidence in support of the application.
- Evidence: `disposition` cue `dismissed` at chunk `4982152` offsets `44-53`; context: [36] For these reasons, this application is dismissed.

#### 20779:1:subtheme:14 · paragraphs 37-38

- Raw key terms: `hearing, judgment, ontario, reasons, september, zinn, accordingly, advised`
- Display key terms: `hearing, ontario, september, zinn, accordingly, advised`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: hearing, ontario, september, zinn, accordingly, advised Position/evidence statements: Accordingly, within 15 days of the issue of these Reasons, either or both counsel may submit a draft of any question proposed to be certified. Application context: Accordingly, within 15 days of the issue of these Reasons, either or both counsel may submit a draft of any question proposed to be certified. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4982153` offsets `134-142`; context: [37] At the hearing the parties requested an opportunity to consider their positions and, if advised, make submissions on a certified question.
- Evidence: `party_position` cue `submit` at chunk `4982153` offsets `230-236`; context: Accordingly, within 15 days of the issue of these Reasons, either or both counsel may submit a draft of any question proposed to be certified.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4982153` offsets `144-155`; context: Accordingly, within 15 days of the issue of these Reasons, either or both counsel may submit a draft of any question proposed to be certified.

#### Section text

Ferguson v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-09-23
Neutral citation
2008 FC 1067
File numbers
IMM-1356-08
Notes
Digest
Decision Content
Date: 20080923
Docket: IMM-1356-08
Citation: 2008 FC 1067
BETWEEN:
MITCHELL MARIE FERGUSON
(A.K.A. MICHELLE MARIE FERGUSON)
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT
ZINN J.

[1] The Applicant says that the Pre-removal Risk Assessment (PRRA) Officer rejected her application because he did not believe that she was lesbian. The Respondent says that the PRRA officer rejected the application because there was insufficient evidence presented to prove, on the balance of probabilities, that the Applicant is lesbian. If the Applicant is correct, then the PRRA officer ought to have held a hearing to determine her sexual orientation. If the Respondent is correct then no hearing was required.

[2] For the reasons that follow, I am of the opinion that no hearing was required as the decision was based solely on the weight of the evidence presented and did not rest on the Applicant’s credibility.
BACKGROUND

[3] Ms. Ferguson has been in Canada since 1987. She lost her status as a permanent resident of Canada and was ordered deported to Jamaica, her country of nationality, after a criminal conviction for drug trafficking.

[4] On the PRRA application form under the heading “Reasons for Applying For Pre-Removal Risk Assessment (PRRA)” Ms. Ferguson wrote “submissions to follow". Under the heading “Supporting Evidence” where she is asked to provide a list of the written documents included with the application that will “clearly act as evidence in support of your application for a Pre-removal Risk Assessment", two types of documents were listed, news articles and affidavits, which she indicated would support her requests for protection by providing “objective proof of risk". In fact, no affidavits were ever provided in support of the application. The news articles that were provided dealt with the treatment of lesbians in Jamaica but none specifically referenced Ms. Ferguson.

[5] By letter dated July 25, 2007, Ms. Ferguson's former counsel wrote to the PRRA officer enclosing “the evidence being relied upon by the Applicant and submissions in support of her application". In addition to enclosing news articles, counsel provided a six-page document which appears to be the submissions referenced in the covering letter. Counsel writes:
Ms. Ferguson is lesbian and is very open about her sexual orientation. She believes that if removed to Jamaica, her life would be at risk, as a result of well-known incidences of homophobia and hate-crime violence in that country against members of her particular social group.
The only other reference to Ms. Ferguson’s sexual orientation is found at the end of her former counsel’s submissions where she writes:
Respecting the fact that the objective documentary evidence reveals the persecution of members of the Applicant's particular social group is commonplace in Jamaica, and the fact that Ms. Ferguson is very openly lesbian, counsel respectfully submits that there is a very serious possibility that the Applicant would be at risk should she return to her country of nationality.

[6] The officer charged with evaluating Ms. Ferguson's claim agreed, without reservation, on the basis of documentary evidence, that lesbians in Jamaica are at risk of severe physical abuse on account of their sexual orientation. The officer nonetheless dismissed the application on the basis that there was insufficient evidence to establish that Ms. Ferguson is lesbian. The officer wrote as follows:
Aside from the brief statement that the applicant is a “lesbian and is very open about her sexual orientation", I have not been provided with supporting evidence that establishes, on the balance of probabilities that, the applicant is a homosexual. Without sufficient evidence that the applicant is a lesbian, an assessment of current country conditions does not establish that she is personally at risk in Jamaica.
Thus, while independent research confirms violence against homosexuals in Jamaica, there is insufficient objective evidence before me to establish that the applicant is, on the balance of probabilities, a lesbian.

[7] Ms. Ferguson submits that the basis for the PRRA officer’s determination rejecting the application was her credibility and accordingly, pursuant to section 113 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27, an oral hearing should have been held. Subsection 113(a) provides that “a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required”. The prescribed factors for determining whether a hearing is to be held are set out in section 167 of the Immigration and Refugee Protection Regulations, SOR/2002-227:
167. For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
(a) whether there is evidence that raises a serious issue of the applicant's credibility and is related to the factors set out in sections 96 and 97 of the Act;
(b) whether the evidence is central to the decision with respect to the application for protection; and
(c) whether the evidence, if accepted, would justify allowing the application for protection.
167. Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
c) la question de savoir si ces éléments de preuve, à supposer qu’ils soient admis, justifieraient que soit accordée la protection.

[8] It is common ground between the parties that if all of the requirements of that section are met, then a hearing should be held by the officer. It is also common ground that the officer’s decision establishes that the requirements in subsections (b) and (c) were met. The issue is whether the requirements set out in subsection 167(a) were met. The Applicant's position is that they were; the officer's rejection of her application was based on the rejection of her evidence that she was openly lesbian, and thus the decision rested on her credibility. The Respondent takes the position that the decision was not based on credibility, but rather on a finding that there was insufficient evidence presented to establish, on the balance of probabilities, that Ms. Ferguson was openly lesbian. In fact, in her written submission, the Respondent’s counsel takes the position that there was no evidence before the PRRA officer regarding Ms. Ferguson’s sexual orientation to doubt or believe, as her counsel’s submission in this regard was not evidence.
ISSUE

[9] There was an issue raised by the Applicant in the pleadings regarding an alleged breach of the Canadian Bill of Rights, S.C. 1960, c. 44; however, it was not pursued in oral argument and, in my view, was without merit. The sole issue in this proceeding is whether the PRRA officer erred in failing to consider conducting or in failing to conduct an oral hearing.

[10] If the officer’s determination was based on a “serious issue of the applicant’s credibility” it is accepted that in Ms. Ferguson’s circumstances, as otherwise found by the officer, he ought to have conducted an oral hearing. For the reasons that follow, I am of the view that the officer made no error and an oral hearing was not required under the Act or Regulations.
ANALYSIS

[11] The Applicant submitted that while the officer did not explicitly state that the decision was one of credibility, it could not be anything other than credibility. In the Applicant’s submission, the officer did not believe her counsel’s statement that she is an open lesbian. Her counsel writes in the memorandum of argument: “Whether because the Applicant had failed to produce sufficient evidence on the balance of probabilities, or for any other reason, the PRRA officer has not believed the statement that the Applicant is a lesbian”. This, it is submitted, is essentially a finding of credibility that attracts the requirement to hold a hearing under section 167 of the Regulations. The Applicant further submits that the PRRA officer did not explain why the statement provided by the Applicant’s former counsel was insufficient evidence or what evidence the officer did rely on to refute the statement that she was lesbian.

[12] The Respondent submits that the legislative scheme makes it clear that applicants who submit a PRRA application or any other application governed by the Act must present evidence to support that application. It is submitted that bald assertions in written submissions do not constitute evidence and ought not to be given any weight. It is submitted that the officer, quite properly, gave no weight to counsel’s submissions that his client was lesbian. In support of this proposition the Respondent relies on Buio v. Canada (Minister of Citizenship and Immigration), 2007 FC 157 at para 32; Canada (Minister of Citizenship and Immigration)v. Sittampalam, 2004 FC 1756 at para 32; and Bressette v. Keetle and Stony Point First Nations Band Council (1997), 137 F.T.R. 189.

[13] In response, the Applicant submitted that it is common practice for immigration counsel to file written submissions on behalf of clients which include statements of evidence, and that there is nothing in either the Act or Regulations or in the policy and procedures of the Respondent that would indicate that such evidence is not to be considered. It is further submitted that the letter from Citizenship and Immigration Canada advising Ms. Ferguson of her right to apply for a Pre-removal Risk Assessment states that information in written submissions will be considered by the PRRA officer. That form letter contains the following paragraph:
You may send us written submissions to support your application for protection. You may explain, in the submissions, the reasons why you think your removal to your country of nationality or habitual residence would put you at risk.

[14] With respect, in my view, that form letter makes it clear that the submissions are to set out reasons and explanations –not evidence. Evidence to support the application ought to be contained in or referenced in the application. In this instance, the Applicant’s statement on the face of her application that submissions were to follow may have been sufficient to alert the officer that those submissions might also contain evidence in addition to reasons and explanations. As will be discussed later, it is my view that there may be instances when statements from counsel may be considered to be evidence.

[15] Both parties submitted numerous authorities to the Court in support of their respective positions. The Applicant referred to Karimi v. Canada (Minister of Citizenship and Immigration), 2007 FC 1010; Latifi v. Canada (Minister of Citizenship and Immigration), 2006 FC 1388; Lewis v. Canada (Minister of Citizenship and Immigration), 2007 FC 778; Rizvi v. Canada (Minister of Citizenship and Immigration), 2008 FC 717; Shafi v. Canada (Minister of Citizenship and Immigration), 2005 FC 714; Suresh v. Canada (Minister of Citizenship and Immigration), [2002] SCC 1; Tekei v. Canada (Minister of Citizenship and Immigration), 2005 FC 27; and Zokai v. Canada (Minister of Citizenship and Immigration), 2005 FC 1103. The Respondent directed the Court’s attention to further authorities, including Demirovic v. Canada (Minister of Citizenship and Immigration), 2005 FC 1284; Gong v. Canada (Minister of Citizenship and Immigration), 2008 FC 600; Iboude v. Canada (Minister of Citizenship and Immigration), [2005] F.C.J. No. 1595; Kim v. Canada (Minister of Citizenship and Immigration), [2003] F.C.J. No. 452; Lake v. Canada (Minister of Citizenship and Immigration), [2008] S.C.J. No. 23; Li v. Canada (Minister of Citizenship and Immigration), [2005] F.C.J. No. 1; Ortiz Juarez v. Canada (Minister of Citizenship and Immigration), [2006] F.C.J. No. 365; Owusu v. Canada (Minister of Citizenship and Immigration), [2004] F.C.J. No. 158; Ray v. Canada (Minister of Citizenship and Immigration), [2006] F.C.J. No. 927; Saadatkhani v. Canada (Minister of Citizenship and Immigration), [2006] F.C.J. No. 769; Sen v. Canada (Minister of Citizenship and Immigration), [2006] F.C.J. No. 1804; and Yousef v. Canada (Minister of Citizenship and Immigration), [2006] F.C.J. No. 1101.

[16] Counsel for both parties appeared to be of the same mind that, in the words of Respondent counsel, there is no principled approach to the issue of credibility versus sufficiency of evidence to be gleaned from these authorities. I do not share that view. Most of the cases to which the Court was referred were determined on the particular facts of the decision under review. In each instance the Court was required to make a determination as to whether, in the decision under review, “there is evidence that raises a serious issue of the applicant’s credibility”, to use the words of section 167 of the Regulations. That, in turn, required an examination of the evidence before the officer and the officer’s assessment of that evidence. I accept the submission of Applicant’s counsel that the Court must look beyond the express wording of the officer’s decision to determine whether, in fact, the applicant’s credibility was in issue.

[17] In my view, the approach to be taken by both the officer and this Court, sitting in review, is to be guided by the principles set out by the Federal Court of Appeal in Carrillo v. Canada (Minister of Citizenship and Immigration), [2008] F.C.J. No. 399.

[18] Ms. Carrillo is a citizen of Mexico who sought refugee protection in Canada. She claimed that she had been abused by her common-law spouse and that her spouse's brother, a police officer, had helped her spouse find her when she hid after the beating. The principal issue before the Immigration and Refugee Protection Board was whether state protection was available to Ms. Carrillo in Mexico. Her refugee claim was dismissed by the Board. It found that she was not a credible or trustworthy witness with respect to her efforts to seek state protection in Mexico. Further, the Board held that had it found her to be credible, she had nonetheless failed to rebut the presumption of state protection with clear and convincing evidence. The Federal Court set aside that decision on the basis that the Board imposed too high a standard of proof on Ms. Carrillo regarding the lack of state protection. An appeal to the Federal Court of Appeal was allowed.

[19] The Court of Appeal, in the course of its reasons, engaged in a detailed and informative discussion of the concepts of burden of proof, standard of proof, and quality of the evidence necessary to meet the burden of proof, all of which I find to be very useful in the present case and which, in my view, ought to be kept in mind by PRRA officers when considering applications.

[20] In every proceeding, whether judicial or administrative, one party has the burden of proof. Where the existence of a particular fact is at issue, uncertainty is resolved by asking whether or not the burden has been discharged with respect to that fact . This was eloquently stated by Lord Hoffmann in In re B (Children) (FC), [2008] UKHL 35 at paragraph 2:
If a legal rule requires a fact to be proved (a “fact in issue”), a judge or jury must decide whether or not it happened. There is no room for a finding that it might have happened. The law operates a binary system in which the only values are 0 and 1. The fact either happened or it did not. If the tribunal is left in doubt, the doubt is resolved by a rule that one party or the other carries the burden of proof. If the party who bears the burden of proof fails to discharge it, a value of 0 is returned and the fact is treated as not having happened. If he does discharge it, a value of 1 is returned and the fact is treated as having happened.

[21] In PRRA applications, it is the applicant who bears the burden of proof: Bayavuge v. Canada (Minister of Citizenship and Immigration), [2007] F.C.J. No. 111.

[22] The standard of proof in civil matters and in administrative processes is the balance of probabilities. In this PRRA application the Applicant must prove, on a balance of probabilities, that she would be subject to risk of persecution, danger of torture, risk to life or risk of cruel and unusual treatment or punishment if returned to Jamaica. That is proved by presenting evidence to the officer. In this respect the Applicant also has an evidentiary burden. The Applicant has the burden of presenting evidence of each of the facts that has to be proved. One of those facts involves her sexual orientation. As will be discussed below, I hold that she did present some evidence of her sexual orientation and thus can be said to have met her evidentiary burden – she presented evidence of each material fact in issue.

[23] As the Court of Appeal pointed out in Carrillo not all evidence is of the same quality. Accordingly, while an applicant may have met the evidentiary burden because evidence of each essential fact has been presented, he may not have met the legal burden because the evidence presented does not prove the facts required on the balance of probabilities. The legal burden of proof is met, in this case, when the Applicant proves to the officer, on the balance of probabilities, that she is lesbian.

[24] The determination of whether the evidence presented meets the legal burden will depend very much on the weight given to the evidence that has been presented.

[25] When a PRRA applicant offers evidence, in either oral or documentary form, the officer may engage in two separate assessments of that evidence. First, he may assess whether the evidence is credible. When there is a finding that the evidence is not credible, it is in truth a finding that the source of the evidence is not reliable. Findings of credibility may be made on the basis that previous statements of the witness contradict or are inconsistent with the evidence now being offered (see for example Karimi, above), or because the witness failed to tender this important evidence at an earlier opportunity, thus bringing into question whether it is a recent fabrication (see for example Sidhu v. Canada 2004 FC 39). Documentary evidence may also be found to be unreliable because its author is not credible. Self-serving reports may fall into this category. In either case, the trier of fact may assign little or no weight to the evidence offered based on its reliability, and hold that the legal standard has not been met.

[26] If the trier of fact finds that the evidence is credible, then an assessment must be made as to the weight that is to be given to it. It is not only evidence that has passed the test of reliability that may be assessed for weight. It is open to the trier of fact, in considering the evidence, to move immediately to an assessment of weight or probative value without considering whether it is credible. Invariably this occurs when the trier of fact is of the view that the answer to the first question is irrelevant because the evidence is to be given little or no weight, even if it is found to be reliable evidence. For example, evidence of third parties who have no means of independently verifying the facts to which they testify is likely to be ascribed little weight, whether it is credible or not.

[27] Evidence tendered by a witness with a personal interest in the matter may also be examined for its weight before considering its credibility because typically this sort of evidence requires corrob

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]

