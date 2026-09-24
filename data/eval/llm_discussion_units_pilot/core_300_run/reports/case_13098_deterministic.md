# Discussion Units: case 13098

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **38**
- Continuity pairs: **37**
- Discussion Units: **2**
- Paragraph source hashes: **38**
- Sub-themes: **6**

## 13098:1 · paragraphs 0-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a81568ff4e9ca56f55f2561e721de0a449c01c2830272072f4e1073fd2be9407`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13098:1:subtheme:1 · paragraphs 0-13

- Raw key terms: `respondent, appeal, sst-gd, sst-ad, disability, pension, retirement, application`
- Display key terms: `sst-gd, sst-ad, disability, pension, retirement`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: sst-gd, sst-ad, disability, pension, retirement Rule/authority context: [1] This is an application by the Crown for judicial review of a decision of the Social Security Tribunal-Appeal Division [SST-AD] granting the Respondent leave to appeal a decision of the SST-General Division [SST-GD] u | The Department of Employment and Social Development Canada denied his application initially and also upon reconsideration on the basis that under the CPP a person in receipt of a retirement pension can only cancel it in  Application context: [5] The Respondent applied for CPP disability benefits, indicating that he ceased working due to congestive heart conditions. | [6] Accordingly, the Respondent must have established a severe and prolonged disability prior to May 31, 2012 (the Respondent’s MQP). Operative outcome context: The Department of Employment and Social Development Canada denied his application initially and also upon reconsideration on the basis that under the CPP a person in receipt of a retirement pension can only cancel it in  | On October 30, 2014, the Respondent provided written explanation as to why he should be granted an extension. Evidence spans paragraphs 0-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4647569` offsets `219-224`; context: [1] This is an application by the Crown for judicial review of a decision of the Social Security Tribunal-Appeal Division [SST-AD] granting the Respondent leave to appeal a decision of the SST-General Division [SST-GD] under section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA].
- Evidence: `governing_rule` cue `under` at chunk `4647572` offsets `266-271`; context: The Department of Employment and Social Development Canada denied his application initially and also upon reconsideration on the basis that under the CPP a person in receipt of a retirement pension can only cancel it in favour of a disability pension if the claimant is deemed to be disabled before the month in which the retirement pension became payable, referred to as the Minimum Qualifying Period [MQP] (CPP, sections 42(2), 44, 66.
- Evidence: `reasoning_application` cue `applied` at chunk `4647572` offsets `19-26`; context: [5] The Respondent applied for CPP disability benefits, indicating that he ceased working due to congestive heart conditions.
- Evidence: `disposition` cue `denied` at chunk `4647572` offsets `185-191`; context: The Department of Employment and Social Development Canada denied his application initially and also upon reconsideration on the basis that under the CPP a person in receipt of a retirement pension can only cancel it in favour of a disability pension if the claimant is deemed to be disabled before the month in which the retirement pension became payable, referred to as the Minimum Qualifying Period [MQP] (CPP, sections 42(2), 44, 66.
- Evidence: `evidence_fact` cue `found that` at chunk `4647573` offsets `176-186`; context: The initial and reconsideration decisions found that the information failed to show the Respondent was prevented from doing some type of work since May 2012 due to disability: he worked until August 2012, collected regular Employment Insurance benefits, and only first developed symptoms and received treatment for congestive heart failure in November 2012.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4647573` offsets `4-15`; context: [6] Accordingly, the Respondent must have established a severe and prolonged disability prior to May 31, 2012 (the Respondent’s MQP).
- Evidence: `disposition` cue `granted` at chunk `4647574` offsets `204-211`; context: On October 30, 2014, the Respondent provided written explanation as to why he should be granted an extension.
- Evidence: `evidence_fact` cue `found that` at chunk `4647575` offsets `498-508`; context: Nevertheless, the SST-GD found that the determinative factor precluding any success upon appeal was the lack of an arguable case.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4647575` offsets `473-485`; context: Nevertheless, the SST-GD found that the determinative factor precluding any success upon appeal was the lack of an arguable case.
- Evidence: `disposition` cue `denied` at chunk `4647575` offsets `33-39`; context: [8] On July 31, 2015, the SST-GD denied the Respondent’s request for an extension of time.
- Evidence: `disposition` cue `granted` at chunk `4647577` offsets `39-46`; context: [10] On September 28, 2015, the SST-AD granted the Respondent leave to appeal to the SST-AD, finding that the appeal fell within one of the grounds of appeal set out in section 58 of the DESDA and that it may have a reasonable chance of success.
- Evidence: `evidence_fact` cue `found that` at chunk `4647578` offsets `23-33`; context: [11] First, the SST-AD found that the Respondent’s argument that the SST-GD erred in not considering his 2012 pension contributions disclosed no ground of appeal.
- Evidence: `reasoning_application` cue `applied` at chunk `4647578` offsets `321-328`; context: The SST-GD did not err in not specifically addressing his contributions in 2011 or 2012, as the Respondent was in receipt of a CPP retirement pension when he applied for a disability pension.
- Evidence: `evidence_fact` cue `found that` at chunk `4647579` offsets `60-70`; context: [12] Second, the SST-AD concluded that the SST-GD correctly found that the Respondent’s appeal was filed late.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4647579` offsets `111-119`; context: Although the Respondent filed an appeal on March 3, 2014, the application was not complete until May 29, 2014 – over 90 days following the communication of the SST-GD Decision to the Respondent on January 16, 2014.
- Evidence: `evidence_fact` cue `determined that` at chunk `4647580` offsets `23-38`; context: [13] Third, the SST-AD determined that the SST-GD correctly articulated the applicable law for granting an extension of time to file the complete Notice of Appeal.

#### 13098:1:subtheme:2 · paragraphs 14-16

- Raw key terms: `premature, review, applicant, application, court, decision, judicial, sst-ad`
- Display key terms: `premature, review, judicial, sst-ad`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application Display terms: premature, review, judicial, sst-ad Position/evidence statements: [21] The Applicant submits that this Court’s review of the SST-AD’s Decision is final, is not interlocutory and therefore is not premature. Rule/authority context: [15] The SST-AD granted leave to appeal, concluding that “this may have been an error of law in the General Division decision”, which is a ground of appeal that may have a reasonable chance of success on appeal under sub Application context: [21] The Applicant submits that this Court’s review of the SST-AD’s Decision is final, is not interlocutory and therefore is not premature. Operative outcome context: [15] The SST-AD granted leave to appeal, concluding that “this may have been an error of law in the General Division decision”, which is a ground of appeal that may have a reasonable chance of success on appeal under sub Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4647582` offsets `255-261`; context: Issues [16] The issues are:
A.
- Evidence: `governing_rule` cue `under` at chunk `4647582` offsets `211-216`; context: [15] The SST-AD granted leave to appeal, concluding that “this may have been an error of law in the General Division decision”, which is a ground of appeal that may have a reasonable chance of success on appeal under subsection 58(1)(b) of the DESDA.
- Evidence: `disposition` cue `granted` at chunk `4647582` offsets `16-23`; context: [15] The SST-AD granted leave to appeal, concluding that “this may have been an error of law in the General Division decision”, which is a ground of appeal that may have a reasonable chance of success on appeal under subsection 58(1)(b) of the DESDA.
- Evidence: `issue` cue `issue` at chunk `4647583` offsets `224-229`; context: However, counsel for the Applicant brought the issue of prematurity to the Court’s attention.
- Evidence: `counterargument_limitation` cue `However` at chunk `4647583` offsets `177-184`; context: However, counsel for the Applicant brought the issue of prematurity to the Court’s attention.
- Evidence: `party_position` cue `submits` at chunk `4647584` offsets `19-26`; context: [21] The Applicant submits that this Court’s review of the SST-AD’s Decision is final, is not interlocutory and therefore is not premature.
- Evidence: `reasoning_application` cue `therefore` at chunk `4647584` offsets `112-121`; context: [21] The Applicant submits that this Court’s review of the SST-AD’s Decision is final, is not interlocutory and therefore is not premature.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4647584` offsets `196-208`; context: Should I find otherwise, the Applicant argues the Court nevertheless ought to exercise its discretion and hear the application.

#### 13098:1:subtheme:3 · paragraphs 17-22

- Raw key terms: `appeal, decision, granting, leave, review, court, courts, decisions`
- Display key terms: `granting, leave, review, courts, decisions`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: granting, leave, review, courts, decisions Rule/authority context: [24] However, I find that a purposive and contextual analysis of the statutory scheme governing the appeal process under the DESDA indicates the decision granting leave in this instance is final, as it is determinative a | [25] The finality of the decision is codified in section 68 of the DESDA: [t]he decision of the Tribunal on any application made under this Act is final and, except for judicial review under the Federal Courts Act, is no Application context: [24] However, I find that a purposive and contextual analysis of the statutory scheme governing the appeal process under the DESDA indicates the decision granting leave in this instance is final, as it is determinative a | [27] Further, subsection 28(g) of the Federal Courts Act, RSC 1985, c F-7 [the Act], grants the Federal Court of Appeal authority over decisions made by the SST-AD, yet the Act expressly excludes decisions made under sec Operative outcome context: Under subsection 18(1)(b) and section 26 of the Act, the Federal Court is granted exclusive original jurisdiction over decisions of federal boards, commissions or tribunals, which includes those decisions of the SST-AD e Evidence spans paragraphs 17-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4647585` offsets `9-14`; context: [22] The issue arises from several Federal Court judgments that previously characterized decisions granting leave made by the Pension Appeals Board [PAB], the predecessor to the SST-AD, as interlocutory, or as having “the look and feel of an interlocutory decision” (see Layden v Canada (Minister of Human Resources and Social Development), 2008 FC 619 at paras 24-26; Mrak v Canada (Minister of Human Resources & Skills Development), 2007 FC 672 at para 36; Canada (Attorney General) v Landry, 2008 FC 810 at para 21; McDonald v Canada (Minister of Human Resources and Skills Development), 2009 FC 1074 at para 16).
- Evidence: `governing_rule` cue `under` at chunk `4647587` offsets `115-120`; context: [24] However, I find that a purposive and contextual analysis of the statutory scheme governing the appeal process under the DESDA indicates the decision granting leave in this instance is final, as it is determinative and dispositive of rights of the parties.
- Evidence: `reasoning_application` cue `I find` at chunk `4647587` offsets `14-20`; context: [24] However, I find that a purposive and contextual analysis of the statutory scheme governing the appeal process under the DESDA indicates the decision granting leave in this instance is final, as it is determinative and dispositive of rights of the parties.
- Evidence: `governing_rule` cue `under` at chunk `4647588` offsets `129-134`; context: [25] The finality of the decision is codified in section 68 of the DESDA:
[t]he decision of the Tribunal on any application made under this Act is final and, except for judicial review under the Federal Courts Act, is not subject to appeal to or review by any court.
- Evidence: `governing_rule` cue `under` at chunk `4647589` offsets `277-282`; context: Upon granting or refusing leave, the SST-AD is functus officio with respect to their decision under section 58 of the DESDA.
- Evidence: `governing_rule` cue `under` at chunk `4647590` offsets `211-216`; context: [27] Further, subsection 28(g) of the Federal Courts Act, RSC 1985, c F-7 [the Act], grants the Federal Court of Appeal authority over decisions made by the SST-AD, yet the Act expressly excludes decisions made under sections 57(2) (granting an extension to apply for leave) and 58 (governing grounds of appeal and the granting of leave), among others.
- Evidence: `reasoning_application` cue `apply` at chunk `4647590` offsets `258-263`; context: [27] Further, subsection 28(g) of the Federal Courts Act, RSC 1985, c F-7 [the Act], grants the Federal Court of Appeal authority over decisions made by the SST-AD, yet the Act expressly excludes decisions made under sections 57(2) (granting an extension to apply for leave) and 58 (governing grounds of appeal and the granting of leave), among others.
- Evidence: `disposition` cue `granted` at chunk `4647590` offsets `427-434`; context: Under subsection 18(1)(b) and section 26 of the Act, the Federal Court is granted exclusive original jurisdiction over decisions of federal boards, commissions or tribunals, which includes those decisions of the SST-AD expressly excluded under section 28.

#### 13098:1:subtheme:4 · paragraphs 23-34

- Raw key terms: `sst-ad, leave, appeal, chance, decision, reasonable, success, desda`
- Display key terms: `sst-ad, leave, chance, reasonable, success, desda`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: sst-ad, leave, chance, reasonable, success, desda Rule/authority context: [28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory. | [32] Moreover, to refuse to hear this application on the basis of non-interference would not decrease cost and delay, but would actually run contrary to principles of efficiency and judicial economy. Application context: [30] While I understand the concern that judicial intervention in an administrative process is undesirable for a variety of reasons – including fragmentation of the administrative process, increased cost and delay, and p | Concerns over premature interference by the Court with the expertise and delegated authority of the SST-AD in making leave decisions applies equally to review of decisions denying leave, which are reviewable. Operative outcome context: Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal. | [36] Leave to appeal a decision of the SST-GD may be granted only where a claimant satisfies the SST-AD that their appeal has a “reasonable chance of success” on one of the three grounds of appeal identified in subsectio Evidence spans paragraphs 23-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4647591` offsets `645-651`; context: Further, the SST-AD’s leave decision demarcates the issues on appeal that have a reasonable chance of success (Belo-Alves v Canada (Attorney General), 2014 FC 1100 at paras 71-73).
- Evidence: `evidence_fact` cue `evidence` at chunk `4647591` offsets `407-415`; context: Unlike an appeal before the former PAB, which was de novo, an appeal to the SST-AD does not allow for new evidence and is limited to the three grounds of appeal listed in section 58.
- Evidence: `governing_rule` cue `under` at chunk `4647591` offsets `127-132`; context: [28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory.
- Evidence: `disposition` cue `granted` at chunk `4647591` offsets `528-535`; context: Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal.
- Evidence: `reasoning_application` cue `because` at chunk `4647593` offsets `238-245`; context: [30] While I understand the concern that judicial intervention in an administrative process is undesirable for a variety of reasons – including fragmentation of the administrative process, increased cost and delay, and potential mootness because of the tribunal’s ruling on another aspect of the proceedings – none of those factors are of concern in the present circumstances.
- Evidence: `governing_rule` cue `principles` at chunk `4647595` offsets `153-163`; context: [32] Moreover, to refuse to hear this application on the basis of non-interference would not decrease cost and delay, but would actually run contrary to principles of efficiency and judicial economy.
- Evidence: `reasoning_application` cue `applies` at chunk `4647596` offsets `432-439`; context: Concerns over premature interference by the Court with the expertise and delegated authority of the SST-AD in making leave decisions applies equally to review of decisions denying leave, which are reviewable.
- Evidence: `counterargument_limitation` cue `but` at chunk `4647597` offsets `335-338`; context: In a case such as this one, where the appeal has no chance of success, and where the SST-AD’s decision granting leave was not only unfounded in the facts before it, but unjustified according to section 58 the DESDA, judicial oversight is both warranted and important to serve as guidance for future leave decisions to be made in accordance with the legislation.
- Evidence: `disposition` cue `granted` at chunk `4647598` offsets `53-60`; context: [36] Leave to appeal a decision of the SST-GD may be granted only where a claimant satisfies the SST-AD that their appeal has a “reasonable chance of success” on one of the three grounds of appeal identified in subsection 58(1) of the DESDA: (a) a breach of natural justice; (b) an error of law; or (c) an erroneous finding of fact made in a perverse and capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4647600` offsets `209-217`; context: There is simply no evidence in the record before the SST-AD that the Respondent had a severe and prolonged mental or physical disability before the month in which he began to receive CPP retirement benefits that made him incapable regularly of pursuing any substantially gainful occupation.
- Evidence: `evidence_fact` cue `evidence` at chunk `4647601` offsets `190-198`; context: Again, there is no evidence of that in this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4647602` offsets `164-172`; context: [40] In determining that the Respondent’s application for leave might have a reasonable chance of success, the SST-AD must correspondingly have concluded there was evidence of the Respondent’s disability arising prior to expiry of his MQP.

#### 13098:1:subtheme:5 · paragraphs 35-36

- Raw key terms: `attorney, canada, date, general, record, abusive, acceptable, accord`
- Display key terms: `date, abusive, acceptable, accord`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: date, abusive, acceptable, accord Rule/authority context: Exception (2) Despite subsection (1), no leave is necessary in the case of an appeal brought under subsection 53(3). Application context: 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt o Operative outcome context: The application is allowed, the SST-AD’s decision is set aside, and the matter is referred to a different member of the SST-AD for reconsideration, having regard to the reasons of this decision. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4647603` offsets `3287-3294`; context: Grounds of appeal
58 (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4647603` offsets `259-267`; context: that there was some evidence suggesting the Respondent was disabled as defined by subsection 42(2) of the CPP prior to his MQP of May 31, 2012), lack the transparency, intelligibility and justification required to meet the reasonableness standard.
- Evidence: `governing_rule` cue `under` at chunk `4647603` offsets `1418-1423`; context: Exception
(2) Despite subsection (1), no leave is necessary in the case of an appeal brought under subsection 53(3).
- Evidence: `reasoning_application` cue `apply` at chunk `4647603` offsets `11048-11053`; context: 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt of a retirement pension and the applicant is deemed to have become disabled for the purposes of entitlement to the disability benefit in or after the month for which the retirement pension first became payable.
- Evidence: `counterargument_limitation` cue `but` at chunk `4647603` offsets `2237-2240`; context: Extension
(2) The Appeal Division may allow further time within which an application for leave to appeal is to be made, but in no case may an application be made more than one year after the day on which the decision is communicated to the appellant.
- Evidence: `disposition` cue `allowed` at chunk `4647603` offsets `549-556`; context: The application is allowed, the SST-AD’s decision is set aside, and the matter is referred to a different member of the SST-AD for reconsideration, having regard to the reasons of this decision.

#### Section text

Canada (Attorney General) v. O'keefe
Court (s) Database
Federal Court Decisions
Date
2016-05-04
Neutral citation
2016 FC 503
File numbers
T-1827-15
Decision Content
Date: 20160504
Docket: T-1827-15
Citation: 2016 FC 503
Ottawa, Ontario, May 4, 2016
PRESENT: The Honourable Mr. Justice Manson
BETWEEN:
ATTORNEY GENERAL OF CANADA
Applicant
and
ROBERT O'KEEFE
Respondent
JUDGMENT AND REASONS

[1] This is an application by the Crown for judicial review of a decision of the Social Security Tribunal-Appeal Division [SST-AD] granting the Respondent leave to appeal a decision of the SST-General Division [SST-GD] under section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA].
I. Background [2] Mr. Robert O’Keefe [the Respondent] began receiving Canada Pension Plan, RSC 1985, c C-8 [CPP] retirement benefits in June 2012 at the age of 60. From May until August 24 of 2012, he worked as a seasonal labourer for an auto salvage company.

[3] From September 2012 onwards, the Respondent has received regular Employment Insurance benefits.

[4] On November 13, 2012, the Respondent was admitted to hospital due to shortness of breath and swelling in his lower extremities, which had commenced approximately one week prior. He has since been diagnosed with congestive heart failure.

[5] The Respondent applied for CPP disability benefits, indicating that he ceased working due to congestive heart conditions. The Department of Employment and Social Development Canada denied his application initially and also upon reconsideration on the basis that under the CPP a person in receipt of a retirement pension can only cancel it in favour of a disability pension if the claimant is deemed to be disabled before the month in which the retirement pension became payable, referred to as the Minimum Qualifying Period [MQP] (CPP, sections 42(2), 44, 66.1(1.1)). “Disability” is defined as a physical or mental disability that is “severe” (i.e. incapable regularly of pursuing any substantial gainful occupation) and “prolonged” (i.e. the disability is likely to be long term and of indefinite duration or is likely to result in death) (CPP, subsection 42(2)(a)).

[6] Accordingly, the Respondent must have established a severe and prolonged disability prior to May 31, 2012 (the Respondent’s MQP). The initial and reconsideration decisions found that the information failed to show the Respondent was prevented from doing some type of work since May 2012 due to disability: he worked until August 2012, collected regular Employment Insurance benefits, and only first developed symptoms and received treatment for congestive heart failure in November 2012.

[7] The Respondent appealed to the SST-GD. His application was initially incomplete, and upon completion, was late. On October 30, 2014, the Respondent provided written explanation as to why he should be granted an extension.

[8] On July 31, 2015, the SST-GD denied the Respondent’s request for an extension of time. The SST-GD assessed the four factors to consider in granting an extension of time to file an appeal as set out in Canada (Minister of Human Resources Development) v Gattellaro, 2005 FC 883. Three of the four factors – intention to pursue an appeal, reasonable explanation for the delay, and no prejudice to the other party in extending the time to appeal – favoured the Respondent. Nevertheless, the SST-GD found that the determinative factor precluding any success upon appeal was the lack of an arguable case. As the Respondent’s disability commenced after he began receiving his early retirement pension, the SST-GD found he is not eligible to receive a disability pension.

[9] The Respondent sought leave to appeal this decision.

[10] On September 28, 2015, the SST-AD granted the Respondent leave to appeal to the SST-AD, finding that the appeal fell within one of the grounds of appeal set out in section 58 of the DESDA and that it may have a reasonable chance of success.

[11] First, the SST-AD found that the Respondent’s argument that the SST-GD erred in not considering his 2012 pension contributions disclosed no ground of appeal. The SST-GD did not err in not specifically addressing his contributions in 2011 or 2012, as the Respondent was in receipt of a CPP retirement pension when he applied for a disability pension.

[12] Second, the SST-AD concluded that the SST-GD correctly found that the Respondent’s appeal was filed late. Although the Respondent filed an appeal on March 3, 2014, the application was not complete until May 29, 2014 – over 90 days following the communication of the SST-GD Decision to the Respondent on January 16, 2014.

[13] Third, the SST-AD determined that the SST-GD correctly articulated the applicable law for granting an extension of time to file the complete Notice of Appeal. In finding that the Respondent had a continuing intention to appeal, a reasonable explanation for the delay and that the opposing party would not be prejudiced if the matter were to proceed, the SST-GD made no error.

[14] However, the SST-AD held the SST-GD “may” have erred in law in concluding that the Respondent failed to present an arguable case on the basis that he did not commence treatment for his condition until after he began receiving the retirement pension, which demonstrated his capacity to work at the relevant time. The SST-AD cites Stanziano v Minister of Human Resources Development, November 26, 2002, CP17926 (PAB) as standing for the principle that a disability pension claimant working after the MQP does not automatically preclude their entitlement to a disability pension.

[15] The SST-AD granted leave to appeal, concluding that “this may have been an error of law in the General Division decision”, which is a ground of appeal that may have a reasonable chance of success on appeal under subsection 58(1)(b) of the DESDA.
II. Issues [16] The issues are:
A. Is the judicial review premature?
B. Is the SST-AD Decision granting leave to appeal reasonable?
III. Standard of Review [17] The applicable standard of review when reviewing the SST-AD’s decision to grant or deny leave to appeal is reasonableness, with substantial deference to the SST-AD (Canada (Attorney General) v Hines, 2016 FC 112 at para 28 [Hines]; Canada (Attorney General) v Hoffman, 2015 FC 1348 at paras 26, 27 [Hoffman]; Tracey v Canada (Attorney General), 2015 FC 1300 at para 17 [Tracey]).
IV. Analysis [18] The relevant provisions of the governing legislation are attached as Annex A.

[19] For the reasons that follow, I am allowing this application.
A. Is the judicial review premature? [20] The Respondent made no submissions with respect to this application. However, counsel for the Applicant brought the issue of prematurity to the Court’s attention.

[21] The Applicant submits that this Court’s review of the SST-AD’s Decision is final, is not interlocutory and therefore is not premature. Should I find otherwise, the Applicant argues the Court nevertheless ought to exercise its discretion and hear the application.

[22] The issue arises from several Federal Court judgments that previously characterized decisions granting leave made by the Pension Appeals Board [PAB], the predecessor to the SST-AD, as interlocutory, or as having “the look and feel of an interlocutory decision” (see Layden v Canada (Minister of Human Resources and Social Development), 2008 FC 619 at paras 24-26; Mrak v Canada (Minister of Human Resources & Skills Development), 2007 FC 672 at para 36; Canada (Attorney General) v Landry, 2008 FC 810 at para 21; McDonald v Canada (Minister of Human Resources and Skills Development), 2009 FC 1074 at para 16). In these cases the Court nonetheless typically assumed jurisdiction to judicially review decisions of a designated member of the PAB granting or refusing leave.

[23] The general rule is that “absent exceptional circumstances, courts should not interfere with ongoing administrative processes until after they are completed, or until the available, effective remedies are exhausted” and that “very few circumstances qualify as ‘exceptional’ and the threshold for exceptionality is high” (Canada (Border Services Agency) v CB Powell Ltd, 2010 FCA 61 at paras 30-33).

[24] However, I find that a purposive and contextual analysis of the statutory scheme governing the appeal process under the DESDA indicates the decision granting leave in this instance is final, as it is determinative and dispositive of rights of the parties.

[25] The finality of the decision is codified in section 68 of the DESDA:
[t]he decision of the Tribunal on any application made under this Act is final and, except for judicial review under the Federal Courts Act, is not subject to appeal to or review by any court.

[26] The DESDA does not give statutory authority to the SST-AD to appeal or to review its own final and binding decisions regarding leave, nor is any other appeal mechanism provided. Upon granting or refusing leave, the SST-AD is functus officio with respect to their decision under section 58 of the DESDA.

[27] Further, subsection 28(g) of the Federal Courts Act, RSC 1985, c F-7 [the Act], grants the Federal Court of Appeal authority over decisions made by the SST-AD, yet the Act expressly excludes decisions made under sections 57(2) (granting an extension to apply for leave) and 58 (governing grounds of appeal and the granting of leave), among others. Under subsection 18(1)(b) and section 26 of the Act, the Federal Court is granted exclusive original jurisdiction over decisions of federal boards, commissions or tribunals, which includes those decisions of the SST-AD expressly excluded under section 28. In my view, a purposive construction of the relevant provisions mandates intervention of the Federal Court by way of judicial review.

[28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory. Under sections 55 to 58 of the DESDA, the test for obtaining leave to appeal and the nature of the appeal has changed. Unlike an appeal before the former PAB, which was de novo, an appeal to the SST-AD does not allow for new evidence and is limited to the three grounds of appeal listed in section 58. Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal. Further, the SST-AD’s leave decision demarcates the issues on appeal that have a reasonable chance of success (Belo-Alves v Canada (Attorney General), 2014 FC 1100 at paras 71-73).

[29] The DESDA makes clear that Parliament intended that the SST-AD only hear appeals properly falling within a ground of appeal and that have a reasonable chance of success. The DESDA does not grant the SST-AD broad discretion in deciding leave, and should the SST-AD grant leave to appeal in other than the instances outlined in section 58, they have improperly stepped beyond the delegated authority provided them by their governing statute.

[30] While I understand the concern that judicial intervention in an administrative process is undesirable for a variety of reasons – including fragmentation of the administrative process, increased cost and delay, and potential mootness because of the tribunal’s ruling on another aspect of the proceedings – none of those factors are of concern in the present circumstances.

[31] Concerns over fragmentation of the process are negated by the fact that the leave to appeal requirement in sections 55 to 58 of the DESDA is a discernible step in the appeal process that results in a final decision.

[32] Moreover, to refuse to hear this application on the basis of non-interference would not decrease cost and delay, but would actually run contrary to principles of efficiency and judicial economy. The undisputed facts of this case, and the very fact that an extension of time and a full hearing of the merits of the appeal would not result in a different outcome, justifies the Court’s intervention at this juncture. The same arguments would be heard at the SST-AD and then again upon subsequent judicial review, wasting both time and resources on an appeal that cannot succeed on these facts, as discussed below.

[33] This Court has exercised its jurisdiction to judicially review decisions of the SST-AD granting leave to appeal (Hoffman, above; Hines, above), and has also reviewed decisions denying leave in this context (Tracey, above; Bellefeuille v Canada (Attorney General), 2014 FC 963 at paras 11, 12). Concerns over premature interference by the Court with the expertise and delegated authority of the SST-AD in making leave decisions applies equally to review of decisions denying leave, which are reviewable.

[34] Without a judicial review mechanism, any opportunity to challenge decisions granting leave would be lost, and those decisions would be immune to judicial oversight. In a case such as this one, where the appeal has no chance of success, and where the SST-AD’s decision granting leave was not only unfounded in the facts before it, but unjustified according to section 58 the DESDA, judicial oversight is both warranted and important to serve as guidance for future leave decisions to be made in accordance with the legislation.
B. Is the SST-AD Decision granting leave to appeal reasonable? [35] Though I am sympathetic to the Respondent’s medical diagnosis, I agree with the Applicant that on the facts before the SST-AD, the Decision it came to is unreasonable.

[36] Leave to appeal a decision of the SST-GD may be granted only where a claimant satisfies the SST-AD that their appeal has a “reasonable chance of success” on one of the three grounds of appeal identified in subsection 58(1) of the DESDA: (a) a breach of natural justice; (b) an error of law; or (c) an erroneous finding of fact made in a perverse and capricious manner or without regard for the material before it. No other grounds of appeal may be considered (Belo-Alves, above, at paras 71-73).

[37] Subsection 58(2) provides that “leave to appeal is refused if the SST-AD is satisfied that the appeal has no reasonable chance of success.”

[38] An individual in receipt of a retirement pension may only cancel it in favour of a disability pension if they are deemed disabled before their MQP (CPP, sections 42(2), 44, 66.1(1.1)). There is simply no evidence in the record before the SST-AD that the Respondent had a severe and prolonged mental or physical disability before the month in which he began to receive CPP retirement benefits that made him incapable regularly of pursuing any substantially gainful occupation. The medical reports on file demonstrate that the Respondent developed symptoms related to his medical condition in November 2012, and that he presented with symptoms of congestive heart failure in November 2013. These dates fall after his effective retirement date, and he is thus statutorily barred from receiving a disability pension in these circumstances.

[39] The Decision is also unreasonable given that the case upon which the SST-AD relied in granting leave clearly requires that the claimant be disabled prior to the MQP. Again, there is no evidence of that in this case.

[40] In determining that the Respondent’s application for leave might have a reasonable chance of success, the SST-AD must correspondingly have concluded there was evidence of the Respondent’s disability arising prior to expiry of his MQP. The SST-AD Decision provides no explanation as to what basis it had for believing a disability existed, nor did it identify any evidence of disability prior to the MQP in reaching its decision. The evidence shows the Respondent’s medical condition first arose in November 2012, and the Respondent has not alleged otherwise.

[41] The SST-AD’s Decision falls outside the range of acceptable, possible outcomes in light of the facts and the law, and its reasons for granting leave to appeal on the basis that the appeal may have a reasonable chance of success (i.e. that there was some evidence suggesting the Respondent was disabled as defined by subsection 42(2) of the CPP prior to his MQP of May 31, 2012), lack the transparency, intelligibility and justification required to meet the reasonableness standard.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application is allowed, the SST-AD’s decision is set aside, and the matter is referred to a different member of the SST-AD for reconsideration, having regard to the reasons of this decision.
"Michael D. Manson"
Judge
ANNEX A
Department of Employment and Social Development Act (S.C. 2005, c. 34)
Appeal Division
Appeal
55 Any decision of the General Division may be appealed to the Appeal Division by any person who is the subject of the decision and any other prescribed person.
Division d’appel
Appel
55 Toute décision de la division générale peut être portée en appel devant la division d’appel par toute personne qui fait l’objet de la décision et toute autre personne visée par règlement.
Leave
56 (1) An appeal to the Appeal Division may only be brought if leave to appeal is granted.
Exception
(2) Despite subsection (1), no leave is necessary in the case of an appeal brought under subsection 53(3).
Autorisation du Tribunal
56 (1) Il ne peut être interjeté d’appel à la division d’appel sans permission.
Exception
(2) Toutefois, il n’est pas nécessaire d’obtenir une permission dans le cas d’un appel interjeté au titre du paragraphe 53(3).
Appeal — time limit
57 (1) An application for leave to appeal must be made to the Appeal Division in the prescribed form and manner and within,
(a) in the case of a decision made by the Employment Insurance Section, 30 days after the day on which it is communicated to the appellant; and
(b) in the case of a decision made by the Income Security Section, 90 days after the day on which the decision is communicated to the appellant.
Extension
(2) The Appeal Division may allow further time within which an application for leave to appeal is to be made, but in no case may an application be made more than one year after the day on which the decision is communicated to the appellant.
Modalités de présentation
57 (1) La demande de permission d’en appeler est présentée à la division d’appel selon les modalités prévues par règlement et dans le délai suivant :
a) dans le cas d’une décision rendue par la section de l’assurance-emploi, dans les trente jours suivant la date où l’appelant reçoit communication de la décision;
b) dans le cas d’une décision rendue par la section de la sécurité du revenu, dans les quatre-vingt-dix jours suivant la date où l’appelant reçoit communication de la décision.
Délai supplémentaire
(2) La division d’appel peut proroger d’au plus un an le délai pour présenter la demande de permission d’en appeler.
Grounds of appeal
58 (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
Criteria
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
Decision
(3) The Appeal Division must either grant or refuse leave to appeal.
Reasons
(4) The Appeal Division must give written reasons for its decision to grant or refuse leave and send copies to the appellant and any other party.
Leave granted
(5) If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed.
Moyens d’appel
58 (1) Les seuls moyens d’appel sont les suivants :
a) la division gén

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 13098:2 · paragraphs 37-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7e582f6615baa8654fb865dd2dadaa4461b1350efef4c1213fde6fa4ea15a7a7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13098:2:subtheme:1 · paragraphs 37-37

- Raw key terms: `appearances, applicant, attorney, behalf, canada, dated, deputy, gatineau`
- Display key terms: `behalf, dated, deputy, gatineau`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, dated, deputy, gatineau No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 37-37. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND reasons:
MANSON J.
DATED:
may 4, 2016
APPEARANCES:
Ms. Nancy Luitwieler
For The Applicant
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Gatineau, Quebec
For The Applicant
Robert O’Keefe
ON HIS OWN BEHALF
