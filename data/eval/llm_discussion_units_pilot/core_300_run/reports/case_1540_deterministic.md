# Discussion Units: case 1540

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **65**
- Continuity pairs: **64**
- Discussion Units: **8**
- Paragraph source hashes: **65**
- Sub-themes: **21**

## 1540:1 · paragraphs 0-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dbc9a7bff4b58da6ba44be9e5fef4d1860018074a418a36a7d239e5b8b51e6f5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `decision, angell, application, canada, division, general, made, appeal`
- Display key terms: `angell, division, made`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: angell, division, made Rule/authority context: Angel’s application for disability pension benefits under the Canada Pension Plan, RSC 1985, c C-8 (the “CPP”). Operative outcome context: The Appeal Division granted the respondent, Ms Angell, leave to appeal from a decision of the SST General Division dated March 26, 2018. | [2] The General Division denied Ms. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `4145812` offsets `187-194`; context: The Appeal Division granted the respondent, Ms Angell, leave to appeal from a decision of the SST General Division dated March 26, 2018.
- Evidence: `governing_rule` cue `under` at chunk `4145813` offsets `88-93`; context: Angel’s application for disability pension benefits under the Canada Pension Plan, RSC 1985, c C-8 (the “CPP”).
- Evidence: `disposition` cue `denied` at chunk `4145813` offsets `25-31`; context: [2] The General Division denied Ms.
- Evidence: `disposition` cue `allowed` at chunk `4145814` offsets `52-59`; context: [3] For the reasons that follow, the application is allowed.

#### 1540:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `angell, appeal, benefits, decision, denied, disability, division, general`
- Display key terms: `angell, benefits, denied, disability, division`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: angell, benefits, denied, disability, division Rule/authority context: [6] The Court’s role right now is not to decide whether or not Ms Angell is entitled to disability benefits under the CPP. Operative outcome context: Angell permission, or “leave”, to appeal the decision of the General Division that denied her disability benefits. | Angell must obtain permission from the Appeal Division before she can appeal the decision of the General Division that denied her disability benefits. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145817` offsets `48-55`; context: [6] The Court’s role right now is not to decide whether or not Ms Angell is entitled to disability benefits under the CPP.
- Evidence: `governing_rule` cue `under` at chunk `4145817` offsets `108-113`; context: [6] The Court’s role right now is not to decide whether or not Ms Angell is entitled to disability benefits under the CPP.
- Evidence: `disposition` cue `denied` at chunk `4145817` offsets `275-281`; context: Angell permission, or “leave”, to appeal the decision of the General Division that denied her disability benefits.
- Evidence: `disposition` cue `denied` at chunk `4145818` offsets `135-141`; context: Angell must obtain permission from the Appeal Division before she can appeal the decision of the General Division that denied her disability benefits.

#### 1540:1:subtheme:3 · paragraphs 8-13

- Raw key terms: `angell, appeal, decision, division, permission, application, aside, decided`
- Display key terms: `angell, division, permission, aside, decided`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: angell, division, permission, aside, decided Rule/authority context: [12] Ms Angell applied for a disability pension under the CPP. Application context: [11] The AGC therefore succeeds on this application. | [12] Ms Angell applied for a disability pension under the CPP. Operative outcome context: That is also the job of the Appeal Division, if Ms Angell is granted permission to appeal in the decision to come. Evidence spans paragraphs 8-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145819` offsets `137-144`; context: My task is to decide whether to do so.
- Evidence: `issue` cue `whether` at chunk `4145820` offsets `147-154`; context: I have not made a new decision on whether to grant leave to appeal.
- Evidence: `disposition` cue `granted` at chunk `4145821` offsets `125-132`; context: That is also the job of the Appeal Division, if Ms Angell is granted permission to appeal in the decision to come.
- Evidence: `reasoning_application` cue `therefore` at chunk `4145822` offsets `13-22`; context: [11] The AGC therefore succeeds on this application.
- Evidence: `governing_rule` cue `under` at chunk `4145823` offsets `48-53`; context: [12] Ms Angell applied for a disability pension under the CPP.
- Evidence: `reasoning_application` cue `applied` at chunk `4145823` offsets `15-22`; context: [12] Ms Angell applied for a disability pension under the CPP.

#### 1540:1:subtheme:4 · paragraphs 14-19

- Raw key terms: `angell, disability, division, general, medical, december, defined, disabled`
- Display key terms: `angell, disability, division, medical, december, defined, disabled`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue Display terms: angell, disability, division, medical, december, defined, disabled Rule/authority context: [16] In order to be eligible for a disability pension under the CPP, Ms Angell must meet the requirements set out in that legislation. Operative outcome context: [17] Initially, the Minister of Employment and Social Development denied Ms Angell’s claim. Evidence spans paragraphs 14-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4145825` offsets `141-147`; context: She advises that she cannot stand now and cannot work as a result of her knee issues, which include a Baker’s cyst behind one knee.
- Evidence: `governing_rule` cue `under` at chunk `4145827` offsets `54-59`; context: [16] In order to be eligible for a disability pension under the CPP, Ms Angell must meet the requirements set out in that legislation.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145828` offsets `382-390`; context: In a decision dated March 26, 2018, the General Division concluded that Ms Angell had provided insufficient objective medical evidence of a severe disability existing on or before the MQP.
- Evidence: `disposition` cue `denied` at chunk `4145828` offsets `66-72`; context: [17] Initially, the Minister of Employment and Social Development denied Ms Angell’s claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4145829` offsets `26-36`; context: [18] The General Division found that Ms Angell must prove, on a balance of probabilities, that she was disabled as defined in the CPP on or before the end of the MQP, i.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145830` offsets `87-95`; context: [19] According to the General Division, a claimant must provide some objective medical evidence of her disability, which must relate to the date of the MQP and show that the disability has been occurring continuously since that date.
- Evidence: `counterargument_limitation` cue `but` at chunk `4145830` offsets `324-327`; context: The General Division found that the claimant must provide not only credible oral evidence but also some objective medical evidence to satisfy the burden of proof to show the disability.

#### 1540:1:subtheme:5 · paragraphs 20-21

- Raw key terms: `angell, appeal, concluded, division, general, benefits, case, corroborate`
- Display key terms: `angell, concluded, division, benefits, case, corroborate`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: angell, concluded, division, benefits, case, corroborate Application context: It therefore did not make a finding on whether disability was prolonged. Operative outcome context: The General Division dismissed her appeal, thereby upholding the denial of her disability benefits. | By decision dated November 22, 2018, a member of the Appeal Division granted leave to appeal. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145831` offsets `242-249`; context: It therefore did not make a finding on whether disability was prolonged.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145831` offsets `104-112`; context: [20] The General Division concluded in this case that Ms Angell failed to provide any objective medical evidence to corroborate her oral evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `4145831` offsets `206-215`; context: It therefore did not make a finding on whether disability was prolonged.
- Evidence: `disposition` cue `dismissed` at chunk `4145831` offsets `297-306`; context: The General Division dismissed her appeal, thereby upholding the denial of her disability benefits.
- Evidence: `disposition` cue `granted` at chunk `4145832` offsets `145-152`; context: By decision dated November 22, 2018, a member of the Appeal Division granted leave to appeal.

#### 1540:1:subtheme:6 · paragraphs 22-26

- Raw key terms: `division, general, appeal, decision, based, claimant, condition, erred`
- Display key terms: `division, based, condition, erred`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, based, condition, erred Rule/authority context: The Appeal Division noted that under subs. | [8] The General Division correctly states that a disability pension claimant must prove that they have a disability that is both severe and prolonged under the Canada Pension Plan. Application context: [24] The AGC has applied for judicial review of this decision. Evidence spans paragraphs 22-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145833` offsets `231-238`; context: [22] In its decision granting leave to appeal, the Appeal Division noted that the Department Of Employment And Social Development Act, SC 2005, c 34, contemplates only three grounds of appeal that the Appeal Division may consider: whether the General Division failed to observe a principle of natural justice or made a jurisdictional error; made an error in law; or based its decision on an erroneous finding of fact that it made in a perverse or capricious manner for without regard for the material before it.
- Evidence: `governing_rule` cue `under` at chunk `4145833` offsets `543-548`; context: The Appeal Division noted that under subs.
- Evidence: `issue` cue `Issue` at chunk `4145834` offsets `301-306`; context: The Appeal Division’s analysis is set out below in its entirety, including its internal heading and paragraphs 8-9 of its reasons:
Issue 2: Error in law
- Evidence: `evidence_fact` cue `evidence` at chunk `4145835` offsets `248-256`; context: It also states that a claimant must provide some objective medical evidence of their disability.
- Evidence: `governing_rule` cue `under` at chunk `4145835` offsets `150-155`; context: [8] The General Division correctly states that a disability pension claimant must prove that they have a disability that is both severe and prolonged under the Canada Pension Plan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145836` offsets `56-64`; context: [9] However, the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter.
- Evidence: `reasoning_application` cue `applied` at chunk `4145837` offsets `17-24`; context: [24] The AGC has applied for judicial review of this decision.

#### Section text

Canada (Attorney General) v. Angell
Court (s) Database
Federal Court Decisions
Date
2020-11-26
Neutral citation
2020 FC 1093
File numbers
T-2176-18
Notes
A correction was made on January 28, 2021
Decision Content
Date: 20201126
Docket: T-2176-18
Citation: 2020 FC 1093
Toronto, Ontario, November 26, 2020
PRESENT: Mr. Justice A.D. Little
BETWEEN:
ATTORNEY GENERAL OF CANADA
Applicant
and
CAROL ANGELL
Respondent
JUDGMENT AND REASONS

[1] The Attorney General of Canada (“AGC”) seeks judicial review of a decision of the Appeal Division of the Social Security Tribunal (“SST”) dated November 22, 2018. The Appeal Division granted the respondent, Ms Angell, leave to appeal from a decision of the SST General Division dated March 26, 2018.

[2] The General Division denied Ms. Angel’s application for disability pension benefits under the Canada Pension Plan, RSC 1985, c C-8 (the “CPP”).

[3] For the reasons that follow, the application is allowed. The decision of the Appeal Division will be set aside and the matter remitted back to the Appeal Division for a new decision on leave to appeal made by a different member.
I. Summary

[4] Before I begin the analysis, I will summarize my decision. I will try to do so with minimal legal jargon.

[5] I heard this application by videoconference. Ms Angell did not have a lawyer to represent her. I listened carefully to what she had to say. I asked her some questions and she answered very helpfully and capably to explain her situation. I thank her for what she said. I also listened carefully to the points made by the lawyer for the AGC. I thank him too, and commend the sensitivity displayed during his submissions.

[6] The Court’s role right now is not to decide whether or not Ms Angell is entitled to disability benefits under the CPP. I am concerned only with the Appeal Division’s decision to grant Ms. Angell permission, or “leave”, to appeal the decision of the General Division that denied her disability benefits.

[7] In law, Ms. Angell must obtain permission from the Appeal Division before she can appeal the decision of the General Division that denied her disability benefits. Permission to appeal can only be granted by the Appeal Division in some circumstances, which are defined by Parliament in a law called the Department of Employment and Social Development Act. The Appeal Division gave Ms. Angell permission to appeal the General Division’s decision.

[8] The AGC has requested that I set aside the Appeal Division’s decision that gave Ms Angell permission to appeal. My task is to decide whether to do so. If I do, the Appeal Division must decide over again whether Ms Angell should be given permission to appeal. If I decide not to set aside the Appeal Division’s decision, Ms Angell can proceed with her appeal at the Appeal Division.

[9] I have decided that I must set aside the Appeal Division’s decision to grant Ms Angell permission to appeal. I have not made a new decision on whether to grant leave to appeal. A member of the Appeal Division, someone other than the person who made it already, will have to make a new decision on that point.

[10] I have also not decided the appeal itself “on its merits”. That is also the job of the Appeal Division, if Ms Angell is granted permission to appeal in the decision to come.

[11] The AGC therefore succeeds on this application.
II. Events Leading to this Application

[12] Ms Angell applied for a disability pension under the CPP. The basis for Ms. Angel’s disability benefit application was sleep apnea, arthritis in her left knee and right hip, and hyperthyroidism/Hashimoto’s disease.

[13] Ms Angell worked for Canada Post for more than 20 years in Nova Scotia, before moving west to Alberta to work in construction. She then returned to Nova Scotia.

[14] Ms Angell had a knee replacement operation in March 2015. She advises that she cannot stand now and cannot work as a result of her knee issues, which include a Baker’s cyst behind one knee.

[15] It took a long time for Ms Angell’s medical records to be sent to her. From her submissions at the hearing, I understand she has them all now and they have been filed for the purposes of her disability benefits application.

[16] In order to be eligible for a disability pension under the CPP, Ms Angell must meet the requirements set out in that legislation. Specifically, under paragraph 44(1)(b) of the CPP, an applicant must be disabled as defined in the CPP on or before the end of a minimum qualifying period or “MQP”. The determination of the MQP is based on the applicant’s contributions to the CPP. In this case, the MQP ended on December 31, 2013.

[17] Initially, the Minister of Employment and Social Development denied Ms Angell’s claim. The Minister denied the claim again on reconsideration. Ms Angell appealed to the General Division of the SST. The General Division upheld the Minister’s decision. In a decision dated March 26, 2018, the General Division concluded that Ms Angell had provided insufficient objective medical evidence of a severe disability existing on or before the MQP.

[18] The General Division found that Ms Angell must prove, on a balance of probabilities, that she was disabled as defined in the CPP on or before the end of the MQP, i.e. by December 31, 2013. It noted that paragraph 42(2)(a) of the CPP defines a “disability” as a physical or mental disability that is severe and prolonged. The General Division held that a person is considered to have a severe disability if a person is incapable regularly of pursuing any substantially gainful occupation. The General Division also held that a disability is prolonged if it is likely to be long, continued and of indefinite duration or is likely to result in death.

[19] According to the General Division, a claimant must provide some objective medical evidence of her disability, which must relate to the date of the MQP and show that the disability has been occurring continuously since that date. The General Division found that the claimant must provide not only credible oral evidence but also some objective medical evidence to satisfy the burden of proof to show the disability.

[20] The General Division concluded in this case that Ms Angell failed to provide any objective medical evidence to corroborate her oral evidence. It found the disability she experienced was not severe. It therefore did not make a finding on whether disability was prolonged. The General Division dismissed her appeal, thereby upholding the denial of her disability benefits.

[21] Ms Angell requested leave to appeal to the Appeal Division of the SST. By decision dated November 22, 2018, a member of the Appeal Division granted leave to appeal. The Appeal Division concluded that the General Division may have erred in law.

[22] In its decision granting leave to appeal, the Appeal Division noted that the Department Of Employment And Social Development Act, SC 2005, c 34, contemplates only three grounds of appeal that the Appeal Division may consider: whether the General Division failed to observe a principle of natural justice or made a jurisdictional error; made an error in law; or based its decision on an erroneous finding of fact that it made in a perverse or capricious manner for without regard for the material before it. The Appeal Division noted that under subs. 58(2) of the Act, leave to appeal may also be refused if the appeal has no reasonable chance of success.

[23] In granting leave to appeal, the Appeal Division concluded that the General Division “may have erred in law, and this requires intervention by the Appeal Division”. The Appeal Division’s analysis is set out below in its entirety, including its internal heading and paragraphs 8-9 of its reasons:
Issue 2: Error in law

[8] The General Division correctly states that a disability pension claimant must prove that they have a disability that is both severe and prolonged under the Canada Pension Plan. It also states that a claimant must provide some objective medical evidence of their disability. The General Division decision states that the medical evidence must relate to the date of the MQP and continuously thereafter. It based its decision that the claimant was not disabled, at least in part, on her failure to provide medical evidence of a disabling condition at the MQP.

[9] However, the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter. As a result, the General Division may have erred in law, and this requires intervention by Appeal Division.

[24] The AGC has applied for judicial review of this decision.


## 1540:2 · paragraphs 27-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fc642f2826792ecd7fb0d6c15d1670186b029779359ff197bad3e642e1a09684`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:2:subtheme:1 · paragraphs 27-29

- Raw key terms: `review, standard, application, boswell, dean, reasonableness, vavilov, administrative`
- Display key terms: `review, standard, boswell, dean, reasonableness, vavilov, administrative`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: review, standard, boswell, dean, reasonableness, vavilov, administrative Rule/authority context: [25] The standard of review on this application is reasonableness: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65; Canada (Attorney General) v Dean, 2020 FC 206 (Boswell, J), at para 18. | [26] As Justice Boswell noted earlier this year in Dean, the standard of review of the Appeal Division was also reasonableness prior to Vavilov. Application context: This presumption of reasonableness review applies to all aspects of the decision: Vavilov, at paras 16, 23 and 25. Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `standard of review` at chunk `4145838` offsets `9-27`; context: [25] The standard of review on this application is reasonableness: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65; Canada (Attorney General) v Dean, 2020 FC 206 (Boswell, J), at para 18.
- Evidence: `reasoning_application` cue `applies` at chunk `4145838` offsets `353-360`; context: This presumption of reasonableness review applies to all aspects of the decision: Vavilov, at paras 16, 23 and 25.
- Evidence: `governing_rule` cue `standard of review` at chunk `4145839` offsets `61-79`; context: [26] As Justice Boswell noted earlier this year in Dean, the standard of review of the Appeal Division was also reasonableness prior to Vavilov.

#### Section text

III. Standard of Review

[25] The standard of review on this application is reasonableness: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65; Canada (Attorney General) v Dean, 2020 FC 206 (Boswell, J), at para 18. Reasonableness is the presumed standard applicable to judicial review of administrative decisions. This presumption of reasonableness review applies to all aspects of the decision: Vavilov, at paras 16, 23 and 25. The presumption may be rebutted by legislative intent, or if the rule of law requires a different standard: Vavilov, para 17, 23 and 69. The presumption is not rebutted in this case.

[26] As Justice Boswell noted earlier this year in Dean, the standard of review of the Appeal Division was also reasonableness prior to Vavilov. As will become clear, my conclusion on this application is consistent with the helpful reasons of Justice Boswell in Dean.

## 1540:3 · paragraphs 30-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dd0ae846b239536cc23204750340733dc472a12c8de848bb5a43cdf5e0ac1d75`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:3:subtheme:1 · paragraphs 30-33

- Raw key terms: `decision, para, vavilov, court, justified, maker, point, reasonableness`
- Display key terms: `para, vavilov, justified, maker, point, reasonableness`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: para, vavilov, justified, maker, point, reasonableness Rule/authority context: [30] With these principles in mind, I turn to the Appeal Division’s decision in this case. Evidence spans paragraphs 30-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145841` offsets `56-63`; context: [28] When reviewing for reasonableness, the court asks “whether the decision bears the hallmarks of reasonableness – justification, transparency and intelligibility – and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision”: Vavilov, at para 99.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4145841` offsets `434-440`; context: To intervene, the reviewing court must be satisfied that there are “sufficiently serious shortcomings” in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency.
- Evidence: `evidence_fact` cue `record` at chunk `4145842` offsets `84-90`; context: [29] A decision will not be reasonable if the reasons, read in conjunction with the record, do not make it possible to understand the decision maker’s reasoning on a critical point: Vavilov, at para 103; Patel v Canada (Citizenship and Immigration), 2020 FC 77 (Diner, J.
- Evidence: `governing_rule` cue `principles` at chunk `4145843` offsets `16-26`; context: [30] With these principles in mind, I turn to the Appeal Division’s decision in this case.

#### Section text

[27] In conducting a reasonableness review, a court must consider the outcome of the administrative decision in light of its underlying rationale, in order to ensure that the decision as a whole is transparent, intelligible and justified: Vavilov, at para 15. The focus of reasonableness review is on the decision made by the decision maker, including both the reasoning process (i.e. the rationale) that led to the decision and the outcome: Vavilov, at paras 83, 86; Delta Air Lines Inc. v. Lukács, 2018 SCC 2, [2018] 1 SCR 6, at para 12. The starting point is the reasons provided by the decision maker: Vavilov, at para 84.

[28] When reviewing for reasonableness, the court asks “whether the decision bears the hallmarks of reasonableness – justification, transparency and intelligibility – and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision”: Vavilov, at para 99. To intervene, the reviewing court must be satisfied that there are “sufficiently serious shortcomings” in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency. Flaws or shortcomings must be more than superficial or peripheral to the merits of the decision, or a “minor misstep”. The problem must be sufficiently central or significant to render the decision unreasonable: Vavilov, at para 100.

[29] A decision will not be reasonable if the reasons, read in conjunction with the record, do not make it possible to understand the decision maker’s reasoning on a critical point: Vavilov, at para 103; Patel v Canada (Citizenship and Immigration), 2020 FC 77 (Diner, J.), at para 9.

[30] With these principles in mind, I turn to the Appeal Division’s decision in this case.


## 1540:4 · paragraphs 34-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `352544169bca278d12e0fd5583f2a918017ccabb4094a30ea5711e8be81d0e69`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:4:subtheme:1 · paragraphs 34-35

- Raw key terms: `appeal, leave, analysis, appealed, brought, decision, department, development`
- Display key terms: `leave, analysis, appealed, brought, department, development`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: leave, analysis, appealed, brought, department, development Rule/authority context: Under subs. Operative outcome context: 56(1), an appeal to the Appeal Division may only be brought if leave to appeal is granted. Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Under` at chunk `4145844` offsets `215-220`; context: Under subs.
- Evidence: `disposition` cue `granted` at chunk `4145844` offsets `309-316`; context: 56(1), an appeal to the Appeal Division may only be brought if leave to appeal is granted.

#### 1540:4:subtheme:2 · paragraphs 36-37

- Raw key terms: `appeal, division, refused, acted, appears, based, beyond, capricious`
- Display key terms: `division, refused, acted, appears, based, beyond, capricious`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: division, refused, acted, appears, based, beyond, capricious Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145845` offsets `30-37`; context: [32] Two provisions constrain whether the Appeal Division may grant leave to appeal.
- Evidence: `evidence_fact` cue `record` at chunk `4145845` offsets `440-446`; context: First, the “only” grounds of appeal are set out in paragraphs 58(1)(a), (b) and (c), which provide:
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner without regard for the material before it.

#### Section text

IV. Analysis
The Requirement for Leave to Appeal

[31] Section 55 of the Department of Employment And Social Development Act provides that any decision of the General Division may be appealed to the Appeal Division by any person who is the subject of the decision. Under subs. 56(1), an appeal to the Appeal Division may only be brought if leave to appeal is granted.

[32] Two provisions constrain whether the Appeal Division may grant leave to appeal. First, the “only” grounds of appeal are set out in paragraphs 58(1)(a), (b) and (c), which provide:
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner without regard for the material before it.

[33] Second, subs. 58(2) provides that “[l]eave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.”

## 1540:5 · paragraphs 38-54

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ec55fb7ae594c7f436525820fb7bc2646b5c70803cd046851dc24a1aeee2a087`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:5:subtheme:1 · paragraphs 38-41

- Raw key terms: `appeal, decision, division, leave, application, grant, added, appellant`
- Display key terms: `division, leave, grant, added, appellant`
- Argument roles: `disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, reasoning_application Display terms: division, leave, grant, added, appellant Application context: The AGC submits that the General Division made no error and that the Appeal Division was incorrect to conclude, at paragraph 9 of its decision, that “the courts do not require that the medical evidence relate directly to Operative outcome context: [35] If leave is granted, the application for leave to appeal become the notice of appeal: subs. Evidence spans paragraphs 38-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `4145848` offsets `17-24`; context: [35] If leave is granted, the application for leave to appeal become the notice of appeal: subs.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145850` offsets `316-324`; context: The AGC submits that the General Division made no error and that the Appeal Division was incorrect to conclude, at paragraph 9 of its decision, that “the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter” [emphasis added].
- Evidence: `reasoning_application` cue `conclude` at chunk `4145850` offsets `225-233`; context: The AGC submits that the General Division made no error and that the Appeal Division was incorrect to conclude, at paragraph 9 of its decision, that “the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter” [emphasis added].

#### 1540:5:subtheme:2 · paragraphs 42-45

- Raw key terms: `appeal, attorney, benefits, canada, claimant, disability, division, evidence`
- Display key terms: `benefits, disability, division`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: benefits, disability, division Position/evidence statements: Further, paragraph 68(1)(a) of the Canada Pension Plan Regulations, CRC, c 385, provides that if an applicant claims to be disabled within the meaning of the CPP, the applicant “shall supply” a “report of any physical or Rule/authority context: Therefore, the AGC maintained that the Appeal Division erred (implicitly) in finding that her appeal had a reasonable chance of success under subs. | [40] I agree with the AGC that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to qualify for disability benefits under the CPP. Application context: The Appeal Division was incorrect to conclude that the General Division erred in law on this issue. | Therefore, the AGC maintained that the Appeal Division erred (implicitly) in finding that her appeal had a reasonable chance of success under subs. Evidence spans paragraphs 42-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4145851` offsets `411-416`; context: The Appeal Division was incorrect to conclude that the General Division erred in law on this issue.
- Evidence: `reasoning_application` cue `conclude` at chunk `4145851` offsets `355-363`; context: The Appeal Division was incorrect to conclude that the General Division erred in law on this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145852` offsets `76-84`; context: [39] Second, the AGC submits that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to obtain disability benefits: Gholipour v Canada (Attorney General), 2017 FCA 99, at para 6.
- Evidence: `governing_rule` cue `under` at chunk `4145852` offsets `597-602`; context: Therefore, the AGC maintained that the Appeal Division erred (implicitly) in finding that her appeal had a reasonable chance of success under subs.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4145852` offsets `461-470`; context: Therefore, the AGC maintained that the Appeal Division erred (implicitly) in finding that her appeal had a reasonable chance of success under subs.
- Evidence: `party_position` cue `claims` at chunk `4145853` offsets `451-457`; context: Further, paragraph 68(1)(a) of the Canada Pension Plan Regulations, CRC, c 385, provides that if an applicant claims to be disabled within the meaning of the CPP, the applicant “shall supply” a “report of any physical or mental disability”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145853` offsets `73-81`; context: [40] I agree with the AGC that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to qualify for disability benefits under the CPP.
- Evidence: `governing_rule` cue `under` at chunk `4145853` offsets `182-187`; context: [40] I agree with the AGC that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to qualify for disability benefits under the CPP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145854` offsets `124-132`; context: [41] Thus, to the extent that the Appeal Division concluded in its reasons at paragraphs 7-8 that no such objective medical evidence is required, the Appeal Division was incorrect in law.

#### 1540:5:subtheme:3 · paragraphs 46-47

- Raw key terms: `appeal, division, reasons, additional, address, already, angell, beyond`
- Display key terms: `division, additional, address, already, angell, beyond`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: division, additional, address, already, angell, beyond Rule/authority context: [42] The AGC also submitted that Ms Angell did not have a reasonable chance of success on the merits of the appeal, such that leave to appeal must be refused under subs. Evidence spans paragraphs 46-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4145855` offsets `260-265`; context: I will not address that issue in these reasons, as it is a question for the Appeal Division.
- Evidence: `governing_rule` cue `under` at chunk `4145855` offsets `158-163`; context: [42] The AGC also submitted that Ms Angell did not have a reasonable chance of success on the merits of the appeal, such that leave to appeal must be refused under subs.

#### 1540:5:subtheme:4 · paragraphs 48-49

- Raw key terms: `ability, addressed, administrative, authority, decision, held, justice, paragraph`
- Display key terms: `ability, addressed, administrative, authority, justice, paragraph`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: ability, addressed, administrative, authority, justice, paragraph Rule/authority context: There were years of further delay in Canada before an Authority to Proceed was issued under the Extradition Act, SC 1999, c. Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4145857` offsets `488-494`; context: Those issues have been addressed above.
- Evidence: `issue` cue `whether` at chunk `4145858` offsets `1119-1126`; context: It also deprives this court of the ability to gauge the reasonableness of the Minister’s decision in terms of whether his officials could have advanced this file more expeditiously and what efforts were made, if any, to encourage Romanian officials to act with diligence in responding to requests from its Canadian counterparts.
- Evidence: `governing_rule` cue `under` at chunk `4145858` offsets `418-423`; context: There were years of further delay in Canada before an Authority to Proceed was issued under the Extradition Act, SC 1999, c.

#### 1540:5:subtheme:5 · paragraphs 50-53

- Raw key terms: `decision, reasons, required, added, administrative, appeal, application, boros`
- Display key terms: `required, added, administrative, boros`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: required, added, administrative, boros Rule/authority context: [47] In my view, in a decision granting leave to appeal under s. | In my view, when viewed independently or with paragraph 7 of the Appeal Division’s reasons, this statement in paragraph 9 does not exhibit the transparency required for administrative decisions under Vavilov and does not Operative outcome context: 58(5)), they will understand why leave to appeal was granted. Evidence spans paragraphs 50-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145859` offsets `309-316`; context: On the existing record, we are unable to determine whether the decision to order Ms.
- Evidence: `evidence_fact` cue `record` at chunk `4145859` offsets `274-280`; context: On the existing record, we are unable to determine whether the decision to order Ms.
- Evidence: `issue` cue `whether` at chunk `4145860` offsets `602-609`; context: As Boros and Vancouver Airport Authority suggest, transparency ensures that the person(s) affected by a decision understand why the decision was made; it ensures that a reviewing court has the ability to understand the basis for the decision on an application for judicial review – in other words, the ability to determine whether the decision was reasonable; and it ensures that others affected by the decision are provided with satisfactorily guidance.
- Evidence: `evidence_fact` cue `record` at chunk `4145860` offsets `206-212`; context: [46] The requirement for transparency in administrative decision-making ensures that the decision-maker discloses the reasoning process that led to its decision, in the reasons provided and in light of the record that was before the decision-maker (see Vavilov, at paras 91-96).
- Evidence: `governing_rule` cue `under` at chunk `4145861` offsets `56-61`; context: [47] In my view, in a decision granting leave to appeal under s.
- Evidence: `disposition` cue `granted` at chunk `4145861` offsets `795-802`; context: 58(5)), they will understand why leave to appeal was granted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145862` offsets `149-157`; context: [48] In this case, the Appeal Division sought to identify an error of law and stated at paragraph 9 that “the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter” [emphasis added].
- Evidence: `governing_rule` cue `under` at chunk `4145862` offsets `439-444`; context: In my view, when viewed independently or with paragraph 7 of the Appeal Division’s reasons, this statement in paragraph 9 does not exhibit the transparency required for administrative decisions under Vavilov and does not achieve one of the purposes of a decision to grant leave to appeal – identifying and describing with clarity a legal error that meets the test under s.

#### 1540:5:subtheme:6 · paragraphs 54-54

- Raw key terms: `above, addition, analysis, angell, anything, appeal, appear, attorney`
- Display key terms: `above, addition, analysis, angell, anything, appear`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, addition, analysis, angell, anything, appear Rule/authority context: However, neither of those paragraphs contained a discussion of court decisions or a legal issue concerning direct versus indirect evidence to support a claim for disability benefits under the CPP. Application context: The Appeal Division’s reasoning therefore does not appear to respond or refer to anything in its own reasons, in the only court decision it cited, or to any specific legal reasoning in the General Division’s decision. Evidence spans paragraphs 54-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4145863` offsets `977-982`; context: However, neither of those paragraphs contained a discussion of court decisions or a legal issue concerning direct versus indirect evidence to support a claim for disability benefits under the CPP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4145863` offsets `159-167`; context: [49] The Appeal Division’s reasons in paragraph 9 did not explain or elaborate on what it meant when it stated that the courts do not require that the medical evidence “relate directly to” a claimant’s condition at the MQP and thereafter.
- Evidence: `governing_rule` cue `under` at chunk `4145863` offsets `1069-1074`; context: However, neither of those paragraphs contained a discussion of court decisions or a legal issue concerning direct versus indirect evidence to support a claim for disability benefits under the CPP.
- Evidence: `reasoning_application` cue `therefore` at chunk `4145863` offsets `1668-1677`; context: The Appeal Division’s reasoning therefore does not appear to respond or refer to anything in its own reasons, in the only court decision it cited, or to any specific legal reasoning in the General Division’s decision.
- Evidence: `counterargument_limitation` cue `However` at chunk `4145863` offsets `597-604`; context: However, Justice Décary’s reasons in Warren did not discuss objective medical evidence that directly or indirectly relates to a claimant’s condition.

#### Section text

[34] Subsection 58(4) provides that the Appeal Division “must give written reasons for its decision to grant or refuse leave” and send copies to the appellant and any other party.

[35] If leave is granted, the application for leave to appeal become the notice of appeal: subs. 58(5).
The Appeal Division’s Decision Must Be Set Aside

[36] On this application for judicial review, the AGC makes a number of arguments to support its submission that the Appeal Division’s decision to grant leave was unreasonable.

[37] First, the AGC submits that the Appeal Division’s decision incorrectly found an error of law by the General Division. The AGC submits that the General Division made no error and that the Appeal Division was incorrect to conclude, at paragraph 9 of its decision, that “the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter” [emphasis added].

[38] I agree with the AGC. The Federal Court of Appeal has held that a claimant must demonstrate an entitlement to disability benefits by reason of a severe and prolonged disability that existed prior to the expiry of the MQP and continuously thereafter: Brennan v Attorney General of Canada, 2011 FCA 318, at para 8. The Appeal Division was incorrect to conclude that the General Division erred in law on this issue. There was therefore no ground of appeal on that basis in paragraph 58(1)(b) of the Department of Employment and Social Development Act.

[39] Second, the AGC submits that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to obtain disability benefits: Gholipour v Canada (Attorney General), 2017 FCA 99, at para 6. The AGC contends that in this case, with reference to paragraphs 25 and 26 of the General Division’s reasons, there is no arguable case on which Ms Angell’s appeal can succeed based on the objective medical evidence. Therefore, the AGC maintained that the Appeal Division erred (implicitly) in finding that her appeal had a reasonable chance of success under subs. 58(2) of the Department of Employment and Social Development Act. For that reason, the AGC submits, the appeal decision did not fall within the range of possible, acceptable outcomes that are defensible by the facts and law, as required by Vavilov.

[40] I agree with the AGC that a claimant must provide objective medical evidence to support a finding of disability on or before the MQP in order to qualify for disability benefits under the CPP. In addition to Gholipour, see also Warren v Canada (Attorney General), 2008 FCA 377, at para 4 and the cases cited there; and Dean, at para 24. Further, paragraph 68(1)(a) of the Canada Pension Plan Regulations, CRC, c 385, provides that if an applicant claims to be disabled within the meaning of the CPP, the applicant “shall supply” a “report of any physical or mental disability”. The regulation states that the report is to include the nature, extent and prognosis of the disability; the findings upon which the diagnosis and prognosis were made; limitations resulting from the disability; and any other pertinent information, including recommendations for further diagnostic work or treatment, that may be relevant.

[41] Thus, to the extent that the Appeal Division concluded in its reasons at paragraphs 7-8 that no such objective medical evidence is required, the Appeal Division was incorrect in law.

[42] The AGC also submitted that Ms Angell did not have a reasonable chance of success on the merits of the appeal, such that leave to appeal must be refused under subs. 58(2) of the Department of Employment and Social Development Act. I will not address that issue in these reasons, as it is a question for the Appeal Division.

[43] However, I have an additional concern related to the transparency of the Appeal Division’s reasons, beyond the errors of law already identified.

[44] Transparency is one of the three hallmarks of administrative decision-making, along with justification and intelligibility: Vavilov, at para 15; Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at para 47. In Vancouver Airport Authority v PSAC, 2010 FCA 158, [2011] 4 FCR 425, Stratas JA held that justification and intelligibility are present when “the basis for a decision has been given and the basis is understandable, with some discernible rationality and logic”. Those issues have been addressed above. Justice Stratas also stated that transparency “speaks to the ability of observers to scrutinize and understand what an administrative decision maker has decided and why”: at paragraph 16(d).

[45] The Court of Appeal for Ontario recently set aside an administrative decision owing to concerns about transparency in Romania v Boros, 2020 ONCA 216. A little background is needed to understand the decision. Ms Boros was convicted in absentia of offences in Romania. Years later, Romania requested the extradition of Ms Boros. There were years of further delay in Canada before an Authority to Proceed was issued under the Extradition Act, SC 1999, c. 18. Ms Boros requested that the Minister of Justice exercise his discretion not to surrender her. The Minister rejected that request, with reasons set out in a lengthy letter. The Court of Appeal held that the Minister’s letter did not address the delays transparently. At paragraph 29, the Court concluded that the Minister’s letter covered a long period of time but shed “very little light on what happened”. The Court explained, at paragraphs 29-30:
This general approach denies Ms. Boros the opportunity to understand why the process took so long. It also deprives this court of the ability to gauge the reasonableness of the Minister’s decision in terms of whether his officials could have advanced this file more expeditiously and what efforts were made, if any, to encourage Romanian officials to act with diligence in responding to requests from its Canadian counterparts. Moreover, the 18-month delay between the issuance of the ATP and the summons is not explained. The combined Canadian delay of nearly 8 years is not addressed beyond an implicit general claim that these matters take a long time. In our view, this is inadequate.

[30] The delay between Ms. Ioan’s statement of September 23, 1998 and the issuance of the summons on November 15, 2016 – more than 18 years – has not been properly investigated, nor properly explained. In the circumstances, the surrender order cannot stand. On the existing record, we are unable to determine whether the decision to order Ms. Boros’ surrender was reasonable. More information is required before we can properly conduct this analysis.
[Emphasis added.]

[46] The requirement for transparency in administrative decision-making ensures that the decision-maker discloses the reasoning process that led to its decision, in the reasons provided and in light of the record that was before the decision-maker (see Vavilov, at paras 91-96). As Boros and Vancouver Airport Authority suggest, transparency ensures that the person(s) affected by a decision understand why the decision was made; it ensures that a reviewing court has the ability to understand the basis for the decision on an application for judicial review – in other words, the ability to determine whether the decision was reasonable; and it ensures that others affected by the decision are provided with satisfactorily guidance. See also Vancouver Airport Authority, at paras 13-14.

[47] In my view, in a decision granting leave to appeal under s. 56 of the Department Of Employment and Social Development Act, and providing its required reasons under subs. 58(4), the Appeal Division should not only identify a ground of appeal that falls within the available grounds in paragraphs 58(1)(a), (b) or (c). It should also communicate with clarity what that successful ground(s) of appeal is (are). Providing a clear description, even if briefly, assists both the parties to the appeal and the panel of the Appeal Division that will eventually hear the appeal on its merits. When they read the written reasons for granting leave, together with the application for leave to appeal (which becomes the notice of appeal under subs. 58(5)), they will understand why leave to appeal was granted.

[48] In this case, the Appeal Division sought to identify an error of law and stated at paragraph 9 that “the courts do not require that the medical evidence relate directly to a claimant’s condition at the MQP and thereafter” [emphasis added]. In my view, when viewed independently or with paragraph 7 of the Appeal Division’s reasons, this statement in paragraph 9 does not exhibit the transparency required for administrative decisions under Vavilov and does not achieve one of the purposes of a decision to grant leave to appeal – identifying and describing with clarity a legal error that meets the test under s. 58 and will be addressed on its merits on the appeal.

[49] The Appeal Division’s reasons in paragraph 9 did not explain or elaborate on what it meant when it stated that the courts do not require that the medical evidence “relate directly to” a claimant’s condition at the MQP and thereafter. In addition to that gap in communicating what the Appeal Division decided and why, neither the phrase “relate directly to” nor the sentence as a whole related to anything in paragraph 7 of the Appeal Division’s reasons. The only reference to a court decision in paragraph 7 is through a footnote referring to Warren v Canada (Attorney General), cited above. However, Justice Décary’s reasons in Warren did not discuss objective medical evidence that directly or indirectly relates to a claimant’s condition. Paragraph 7 of the Appeal Division’s reasons referred, via two other footnotes, to paragraphs 22 and 25 of the General Division’s decision. However, neither of those paragraphs contained a discussion of court decisions or a legal issue concerning direct versus indirect evidence to support a claim for disability benefits under the CPP. The General Division’s reasoning recognized that a medical report may be dated after the MQP but refer to findings in respect of a disability that existed before or at the MQP. Its reasons also discussed what may constitute “objective” evidence and discussed whether Ms Angell provided any objective medical evidence to corroborate her oral evidence. However, I am unable to detect any analysis or reference to a court decision or a legal issue related to “indirect” (as opposed to “direct”) evidence to support a disability at the MQP and thereafter. The Appeal Division’s reasoning therefore does not appear to respond or refer to anything in its own reasons, in the only court decision it cited, or to any specific legal reasoning in the General Division’s decision.

## 1540:6 · paragraphs 55-61

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1094ba090457fd09ceb2d0d860e68b9c056503d29728b1e94a169644aea6f5ae`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:6:subtheme:1 · paragraphs 55-57

- Raw key terms: `vavilov, appeal, cannot, court, decision, division, para, paras`
- Display key terms: `vavilov, cannot, division, para, paras`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: vavilov, cannot, division, para, paras Evidence spans paragraphs 55-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4145864` offsets `359-364`; context: [50] Bearing in mind the objectives of a transparent decision, the Appeal Division’s reasons did not sufficiently communicate what it decided and why, did not identify for the parties a permitted ground for appeal on the merits, and will not enable the panel of the Appeal Division hearing the merits of the appeal to identify the legal error that will be at issue (something that may have greater importance when the proposed appellant is not represented by legal counsel).
- Evidence: `issue` cue `whether` at chunk `4145865` offsets `241-248`; context: A reviewing court cannot build its own bridge across an apparent gap in a decision-maker’s reasoning, nor determine whether that court-constructed conduit would have been correct in law.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4145866` offsets `217-223`; context: [52] In order for a decision to be set aside on the basis that it is unreasonable, Vavilov requires that the reviewing court be satisfied that there are “sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency”: at para 100.

#### 1540:6:subtheme:2 · paragraphs 58-59

- Raw key terms: `appeal, decision, division, leave, accordingly, addition, application, aside`
- Display key terms: `division, leave, accordingly, addition, aside`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: division, leave, accordingly, addition, aside Application context: [53] In this case, having paid close attention to its reasons, I conclude that the shortcomings in the Appeal Division’s decision are sufficiently serious to undermine both the reasoning and the outcome reached by the Ap | [54] Accordingly, the decision of the Appeal Division granting leave to appeal must be set aside. Evidence spans paragraphs 58-59. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4145867` offsets `323-328`; context: The shortcomings include one or more errors of law on the very issue at stake on the application for leave to appeal, namely, whether there was an error of law made by the General Division.
- Evidence: `reasoning_application` cue `conclude` at chunk `4145867` offsets `65-73`; context: [53] In this case, having paid close attention to its reasons, I conclude that the shortcomings in the Appeal Division’s decision are sufficiently serious to undermine both the reasoning and the outcome reached by the Appeal Division to grant leave to appeal.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4145868` offsets `5-16`; context: [54] Accordingly, the decision of the Appeal Division granting leave to appeal must be set aside.

#### 1540:6:subtheme:3 · paragraphs 60-61

- Raw key terms: `above, addressed, agree, analysis, angell, appeal, application, assess`
- Display key terms: `above, addressed, agree, analysis, angell, assess`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: above, addressed, agree, analysis, angell, assess Rule/authority context: I will also not consider the AGC’s submission that, in the circumstances here, Ms Angell did not have a reasonable chance of success on the appeal under subs. Operative outcome context: [56] The AGC requested that the application be granted without costs. Evidence spans paragraphs 60-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4145869` offsets `49-56`; context: [55] Given the analysis above, I need not assess whether the Appeal Division’s reasons for granting leave to appeal sufficiently addressed subs.
- Evidence: `governing_rule` cue `under` at chunk `4145869` offsets `358-363`; context: I will also not consider the AGC’s submission that, in the circumstances here, Ms Angell did not have a reasonable chance of success on the appeal under subs.
- Evidence: `disposition` cue `granted` at chunk `4145870` offsets `47-54`; context: [56] The AGC requested that the application be granted without costs.

#### Section text

[50] Bearing in mind the objectives of a transparent decision, the Appeal Division’s reasons did not sufficiently communicate what it decided and why, did not identify for the parties a permitted ground for appeal on the merits, and will not enable the panel of the Appeal Division hearing the merits of the appeal to identify the legal error that will be at issue (something that may have greater importance when the proposed appellant is not represented by legal counsel). See Vavilov, at paras 86, 94-100, 102-103; Vancouver Airport Authority, at paras 13-14 and 16(d).

[51] While it is possible to hypothesize about what the Appeal Division meant in paragraph 9, to do so would be speculative. A reviewing court cannot build its own bridge across an apparent gap in a decision-maker’s reasoning, nor determine whether that court-constructed conduit would have been correct in law. Doing so would re-write the decision-maker’s reasons. See Vavilov, at paras 83, 96-98; Komolafe v Canada (Citizenship and Immigration), 2013 FC 431 (Rennie, J), at para 11 (quoted with approval in Vavilov, at para 97); and Rezaei v Canada (Immigration, Refugees and Citizenship), 2020 FC 444 (LeBlanc, J), at para 28.
V. Conclusion

[52] In order for a decision to be set aside on the basis that it is unreasonable, Vavilov requires that the reviewing court be satisfied that there are “sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency”: at para 100.

[53] In this case, having paid close attention to its reasons, I conclude that the shortcomings in the Appeal Division’s decision are sufficiently serious to undermine both the reasoning and the outcome reached by the Appeal Division to grant leave to appeal. The shortcomings include one or more errors of law on the very issue at stake on the application for leave to appeal, namely, whether there was an error of law made by the General Division. In addition, the Appeal Division’s reasons do not contain a transparent explanation of how it reached its conclusion on that central issue of whether to grant leave to appeal: Vavilov, at paras 86, 96, 100, 102-103; Senadheerage v. Canada (Citizenship and Immigration), 2020 FC 968 (Grammond, J.), at paras 36-42. These shortcomings cause me to lose confidence in the outcome reached by the Appeal Division: Vavilov, at para 106.

[54] Accordingly, the decision of the Appeal Division granting leave to appeal must be set aside.

[55] Given the analysis above, I need not assess whether the Appeal Division’s reasons for granting leave to appeal sufficiently addressed subs. 58(2) of the Department of Employment and Social Development Act. I will also not consider the AGC’s submission that, in the circumstances here, Ms Angell did not have a reasonable chance of success on the appeal under subs. 58(2). It will be for the Appeal Division on redetermination to deal with the latter issue.

[56] The AGC requested that the application be granted without costs. I agree.


## 1540:7 · paragraphs 62-63

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `976aabfe925aca33364e2079e9c7f4929e79fd6069481f2ce13b667867e9a13c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:7:subtheme:1 · paragraphs 62-63

- Raw key terms: `angell, t-2176-18, appeal, aside, attorney, august, canda, carol`
- Display key terms: `angell, t-2176-18, aside, august, canda, carol`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: angell, t-2176-18, aside, august, canda, carol No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT in T-2176-18
THIS COURT’S JUDGMENT is that:
The decision of the Appeal Division of the Social Security Tribunal dated November 22, 2018 is set aside. Ms Angell’s request for leave to appeal is remitted to the Appeal Division for determination by a different member.
There is no order as to costs.
"A.D. Little"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-2176-18
STYLE OF CAUSE:
ATTORNEY GENERAL OF CANDA and CAROL ANGELL
PLACE OF HEARING:
TORONTO, ONTARIO
DATE OF HEARING:
AUGUST 12, 2020


## 1540:8 · paragraphs 64-64

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `972377b8af22b54e5de998fe2ba087fe8a1c2c410dac90b3c1a494ca28dde1d2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1540:8:subtheme:1 · paragraphs 64-64

- Raw key terms: `angell, appearances, applicant, attorney, canada, carol, dated, general`
- Display key terms: `angell, carol, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: angell, carol, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 64-64. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
little J.
DATED:
november 26, 2020
APPEARANCES:
Matthew Vens
For The APPLICANT
Carol Angell
SELF-REPRESENTED
SOLICITORS OF RECORD:
Matthew Vens
Attorney General of Canada
For The APPLICANT
Carol Angell
SELF-REPRESENTED
