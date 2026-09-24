# Discussion Units: case 13382

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **25**
- Continuity pairs: **24**
- Discussion Units: **4**
- Paragraph source hashes: **25**
- Sub-themes: **9**

## 13382:1 · paragraphs 0-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e3485e9bbac489eab463258fd01b20b61e0ecf6d16551000cf48a84411e743eb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13382:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `griffin, employment, accommodations, canada, afford, already, applicant, because`
- Display key terms: `griffin, employment, accommodations, afford, already, because`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: griffin, employment, accommodations, afford, already, because Rule/authority context: Griffin’s employer stated that it would not be covering his accommodations because it was under the impression that Mr. Application context: Griffin’s employer stated that it would not be covering his accommodations because it was under the impression that Mr. | Griffin stated that he left because he could not afford to pay for his accommodations, and that he was therefore forced to leave the position when his employer refused to pay for it. Operative outcome context: In its decision dated December 22, 2015, the Appeal Division denied Mr. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4659705` offsets `784-792`; context: Although the matter was never discussed directly, Mr.
- Evidence: `disposition` cue `denied` at chunk `4659705` offsets `256-262`; context: In its decision dated December 22, 2015, the Appeal Division denied Mr.
- Evidence: `governing_rule` cue `under` at chunk `4659706` offsets `191-196`; context: Griffin’s employer stated that it would not be covering his accommodations because it was under the impression that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4659706` offsets `176-183`; context: Griffin’s employer stated that it would not be covering his accommodations because it was under the impression that Mr.
- Evidence: `evidence_fact` cue `determined that` at chunk `4659708` offsets `378-393`; context: Nevertheless, on January 29, 2015, the Commission determined that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4659708` offsets `173-180`; context: Griffin stated that he left because he could not afford to pay for his accommodations, and that he was therefore forced to leave the position when his employer refused to pay for it.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4659708` offsets `328-340`; context: Nevertheless, on January 29, 2015, the Commission determined that Mr.

#### 13382:1:subtheme:2 · paragraphs 5-8

- Raw key terms: `appeal, division, general, applicant, determined, error, evidence, leave`
- Display key terms: `division, determined, error, leave`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: division, determined, error, leave Application context: Accordingly, Mr. Operative outcome context: This request was denied on April 21, 2015. Evidence spans paragraphs 5-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4659709` offsets `1031-1038`; context: 34 [Act], allows for a decision of the General Division to be appealed only where:
a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) the General Division erred in law, whether or not the error appears on the face of the record; or
c) the General Division based its decision on erroneous findings of fact made in a perverse or capricious manner, or without regard to the evidence before it.
- Evidence: `evidence_fact` cue `determined that` at chunk `4659709` offsets `663-678`; context: Griffin’s application for leave to appeal, the Appeal Division determined that subsection 58(1) of the Department of Employment and Social Development Act, S.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4659709` offsets `132-143`; context: Accordingly, Mr.
- Evidence: `disposition` cue `denied` at chunk `4659709` offsets `106-112`; context: This request was denied on April 21, 2015.
- Evidence: `evidence_fact` cue `determined that` at chunk `4659710` offsets `32-47`; context: [8] The Appeal Division further determined that leave to appeal is to be refused if the appeal has “no reasonable chance of success.
- Evidence: `evidence_fact` cue `found that` at chunk `4659711` offsets `24-34`; context: [9] The Appeal Division found that the Applicant was essentially asking the Appeal Division to re-weigh the evidence presented to the General Division and come to a different conclusion, stating as follows:

#### 13382:1:subtheme:3 · paragraphs 9-10

- Raw key terms: `appeal, applicant, decision, division, leave, reasonable, request, acted`
- Display key terms: `division, leave, reasonable, request, acted`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: division, leave, reasonable, request, acted Position/evidence statements: He also contends that the General Division failed to observe a principle of natural justice and acted beyond or failed to exercise its jurisdiction. | [11] The Respondent submits that the main issue is whether it was reasonable for the Appeal Division to deny the Applicant’s request for leave to appeal. Application context: The Court therefore presumes that the Applicant is asserting that the Appeal Division’s decision denying his request for leave to appeal is unreasonable. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4659713` offsets `483-489`; context: Issues [10] Although the Applicant does not precisely identify any specific issues in his submissions, his application does request that his case be heard again and re-examined with additional information about why he left his job with BDC.
- Evidence: `party_position` cue `contends` at chunk `4659713` offsets `732-740`; context: He also contends that the General Division failed to observe a principle of natural justice and acted beyond or failed to exercise its jurisdiction.
- Evidence: `reasoning_application` cue `therefore` at chunk `4659713` offsets `883-892`; context: The Court therefore presumes that the Applicant is asserting that the Appeal Division’s decision denying his request for leave to appeal is unreasonable.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4659713` offsets `495-503`; context: Issues [10] Although the Applicant does not precisely identify any specific issues in his submissions, his application does request that his case be heard again and re-examined with additional information about why he left his job with BDC.
- Evidence: `issue` cue `issue` at chunk `4659714` offsets `42-47`; context: [11] The Respondent submits that the main issue is whether it was reasonable for the Appeal Division to deny the Applicant’s request for leave to appeal.
- Evidence: `party_position` cue `submits` at chunk `4659714` offsets `20-27`; context: [11] The Respondent submits that the main issue is whether it was reasonable for the Appeal Division to deny the Applicant’s request for leave to appeal.

#### 13382:1:subtheme:4 · paragraphs 11-11

- Raw key terms: `addition, additional, adduce, affidavit, applicant, attention, court, evidence`
- Display key terms: `addition, additional, adduce, affidavit, attention`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: addition, additional, adduce, affidavit, attention Evidence spans paragraphs 11-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4659715` offsets `37-42`; context: [12] In addition, there is a further issue which requires the Court’s attention, and that is the additional or new evidence which the Applicant purports to adduce in his affidavit.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659715` offsets `115-123`; context: [12] In addition, there is a further issue which requires the Court’s attention, and that is the additional or new evidence which the Applicant purports to adduce in his affidavit.

#### Section text

Griffin v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2016-07-26
Neutral citation
2016 FC 874
File numbers
T-124-16
Decision Content
Date: 20160726
Docket: T-124-16
Citation: 2016 FC 874
Ottawa, Ontario, July 26, 2016
PRESENT: The Honourable Mr. Justice Boswell
BETWEEN:
SEAN GRIFFIN
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] The Applicant, Sean Griffin, who represents himself in this proceeding, has brought this application for judicial review of a decision of the Appeal Division of the Social Security Tribunal. In its decision dated December 22, 2015, the Appeal Division denied Mr. Griffin’s request for leave to appeal a decision of the General Division of the Social Security Tribunal on the basis that the appeal did not disclose a proper ground of appeal and lacked any reasonable chance of success. The Applicant now requests, in effect, that this Court review the Appeal Division’s decision, set it aside, and return the matter to another panel of the Appeal Division for redetermination.
I. Background [2] On September 29, 2014, Mr. Griffin began working for BDC Bull Dozer Construction Ltd. Although the matter was never discussed directly, Mr. Griffin had assumed that BDC would provide him with accommodations for the duration of his employment, as BDC had done this for him in the past and he believed that BDC did so for all employees not already residing in Red Deer, Alberta (the location of the work site). After he was hired, Mr. Griffin proceeded to check into the hotel where BDC was housing a number of its other employees.

[3] On October 1, 2014, Mr. Griffin approached his employer about paying for his accommodations. Mr. Griffin’s employer stated that it would not be covering his accommodations because it was under the impression that Mr. Griffin was already residing in Red Deer with his mother. Mr. Griffin responded that he would not be able to continue working for BDC if his accommodations were not paid for since he could not afford to pay for the hotel room himself. Consequently, on October 1, 2014, Mr. Griffin voluntarily left his employment with BDC.

[4] In his October 15, 2014 report to Service Canada, Mr. Griffin did not include his employment with BDC. Consequently, Mr. Griffin continued to receive the EI benefits which he had been receiving since June of 2014.

[5] On January 8, 2015, the Canada Employment Insurance Commission contacted Mr. Griffin about the reason he ceased his employment with BDC. Mr. Griffin stated that he left because he could not afford to pay for his accommodations, and that he was therefore forced to leave the position when his employer refused to pay for it. Nevertheless, on January 29, 2015, the Commission determined that Mr. Griffin had left his employment with BDC without just cause and imposed an indefinite disqualification from receiving EI benefits, as well as a penalty for receiving ineligible benefits and not reporting his employment with BDC.

[6] In March 2015, Mr. Griffin requested a reconsideration of the Commission’s decision. This request was denied on April 21, 2015. Accordingly, Mr. Griffin appealed this denial to the General Division of the Social Security Tribunal. In a decision dated September 18, 2015, the General Division upheld the Commission’s decision, finding that Mr. Griffin had left his employment without just cause. In due course, the Applicant filed an application requesting leave to appeal the General Division’s decision to the Appeal Division.
II. The Appeal Division’s Decision [7] In its decision refusing Mr. Griffin’s application for leave to appeal, the Appeal Division determined that subsection 58(1) of the Department of Employment and Social Development Act, S.C. 2005, c. 34 [Act], allows for a decision of the General Division to be appealed only where:
a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
b) the General Division erred in law, whether or not the error appears on the face of the record; or
c) the General Division based its decision on erroneous findings of fact made in a perverse or capricious manner, or without regard to the evidence before it.

[8] The Appeal Division further determined that leave to appeal is to be refused if the appeal has “no reasonable chance of success.”

[9] The Appeal Division found that the Applicant was essentially asking the Appeal Division to re-weigh the evidence presented to the General Division and come to a different conclusion, stating as follows:

[8] The role of the Appeal Division is to determine if a reviewable error set out in ss. 58(1) of the Act has been made by the General Division and if so to provide a remedy for that error. In the absence of such a reviewable error, the law does not permit the Appeal Division to intervene. It is not our role to re-hear the case de novo.

[9] It is not sufficient for an Applicant to plead that the General Division member was mistaken in his or her conclusions and ask the Appeal Division for a different outcome. In order to have a reasonable chance of success, the Applicant must explain in some detail how, in their view, at least one reviewable error set out in the Act has been made. Having failed to do so, this application for leave to appeal does not have a reasonable chance of success and must be refused.
III. Issues [10] Although the Applicant does not precisely identify any specific issues in his submissions, his application does request that his case be heard again and re-examined with additional information about why he left his job with BDC. He also contends that the General Division failed to observe a principle of natural justice and acted beyond or failed to exercise its jurisdiction. The Court therefore presumes that the Applicant is asserting that the Appeal Division’s decision denying his request for leave to appeal is unreasonable.

[11] The Respondent submits that the main issue is whether it was reasonable for the Appeal Division to deny the Applicant’s request for leave to appeal. I agree with the Respondent that the main issue is whether the decision of the Appeal Division to deny leave to appeal was reasonable.

[12] In addition, there is a further issue which requires the Court’s attention, and that is the additional or new evidence which the Applicant purports to adduce in his affidavit.


## 13382:2 · paragraphs 12-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6098b91984c653efa4488b192511eecc27f6291ba10b2b91573e9424bd1080be`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13382:2:subtheme:1 · paragraphs 12-14

- Raw key terms: `appeal, court, decision, division, attorney, canada, considered, evidence`
- Display key terms: `division, considered`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: division, considered Position/evidence statements: Griffin’s Affidavit and Additional Arguments [15] The Respondent submits that Mr. Rule/authority context: Standard of Review [13] The applicable standard for this Court’s review of a decision of the Appeal Division granting or denying leave to appeal a decision of the General Division is that of reasonableness: see: Canada ( Application context: Griffin’s familial obligations, BDC’s health and safety practices, and his own health was not before the Appeal Division and, accordingly, cannot be and has not been considered by the Court in reviewing the reasonablenes Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4659715` offsets `185-203`; context: Standard of Review [13] The applicable standard for this Court’s review of a decision of the Appeal Division granting or denying leave to appeal a decision of the General Division is that of reasonableness: see: Canada (Attorney General) v.
- Evidence: `issue` cue `whether` at chunk `4659716` offsets `560-567`; context: Those criteria are met if “the reasons allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes”: Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16, [2011] 3 SCR 708.
- Evidence: `party_position` cue `submits` at chunk `4659716` offsets `1115-1122`; context: Griffin’s Affidavit and Additional Arguments [15] The Respondent submits that Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659716` offsets `60-68`; context: [14] This being so, the Appeal Division’s assessment of the evidence is entitled to deference (see: Dunsmuir v New Brunswick, 2008 SCC 9 at para 53, [2008] 1 SCR 190 [Dunsmuir]).
- Evidence: `evidence_fact` cue `evidence` at chunk `4659717` offsets `18-26`; context: The evidence as to Mr.
- Evidence: `reasoning_application` cue `accordingly` at chunk `4659717` offsets `163-174`; context: Griffin’s familial obligations, BDC’s health and safety practices, and his own health was not before the Appeal Division and, accordingly, cannot be and has not been considered by the Court in reviewing the reasonableness of the Appeal Division’s decision.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4659717` offsets `176-182`; context: Griffin’s familial obligations, BDC’s health and safety practices, and his own health was not before the Appeal Division and, accordingly, cannot be and has not been considered by the Court in reviewing the reasonableness of the Appeal Division’s decision.

#### 13382:2:subtheme:2 · paragraphs 15-16

- Raw key terms: `appeal, argues, decision, division, establish, failed, griffin, leave`
- Display key terms: `argues, division, establish, failed, griffin, leave`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: argues, division, establish, failed, griffin, leave Position/evidence statements: [19] The Respondent submits that, pursuant to subsection 58(1) of the Act, the Appeal Division may only grant leave to appeal a decision of the General Division where it is satisfied that an appellant has a reasonable ch Rule/authority context: [19] The Respondent submits that, pursuant to subsection 58(1) of the Act, the Appeal Division may only grant leave to appeal a decision of the General Division where it is satisfied that an appellant has a reasonable ch Application context: This issue is not properly before the Court because Mr. | Accordingly, the Respondent submits that the Appeal Division’s decision was reasonable and that this application for judicial review should be dismissed. Operative outcome context: Accordingly, the Respondent submits that the Appeal Division’s decision was reasonable and that this application for judicial review should be dismissed. Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4659718` offsets `118-123`; context: Griffin’s argument that the Court should issue a declaration that any amount he owes to the Commission should be written off.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659718` offsets `973-981`; context: Griffin also contends that the Appeal Division failed to consider all the evidence in relation to the quantum of the penalty imposed on him, and that he should not be forced to repay the benefits he received because repayment would cause him undue hardship.
- Evidence: `reasoning_application` cue `because` at chunk `4659718` offsets `247-254`; context: This issue is not properly before the Court because Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `4659718` offsets `792-795`; context: Griffin says his belief that he had no alternative but to leave his position is sufficient to establish that he had just cause for ending his employment.
- Evidence: `party_position` cue `submits` at chunk `4659719` offsets `20-27`; context: [19] The Respondent submits that, pursuant to subsection 58(1) of the Act, the Appeal Division may only grant leave to appeal a decision of the General Division where it is satisfied that an appellant has a reasonable chance of success based on one or more of the grounds of appeal listed in subsection 58(1).
- Evidence: `governing_rule` cue `pursuant to` at chunk `4659719` offsets `34-45`; context: [19] The Respondent submits that, pursuant to subsection 58(1) of the Act, the Appeal Division may only grant leave to appeal a decision of the General Division where it is satisfied that an appellant has a reasonable chance of success based on one or more of the grounds of appeal listed in subsection 58(1).
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4659719` offsets `760-771`; context: Accordingly, the Respondent submits that the Appeal Division’s decision was reasonable and that this application for judicial review should be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4659719` offsets `903-912`; context: Accordingly, the Respondent submits that the Appeal Division’s decision was reasonable and that this application for judicial review should be dismissed.

#### 13382:2:subtheme:3 · paragraphs 17-21

- Raw key terms: `appeal, decision, division, evidence, failed, general, griffin, subsection`
- Display key terms: `division, failed, griffin, subsection`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: division, failed, griffin, subsection Rule/authority context: In my view, this does not disclose a valid ground of appeal under subsection 58(1) of the Act. Application context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner. | [22] In short, because Mr. Operative outcome context: Griffin’s application for judicial review is dismissed. Evidence spans paragraphs 17-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4659720` offsets `509-516`; context: On the contrary, the Appeal Division should review the underlying record and determine whether the decision failed to properly account for any of the evidence: Karadeolian v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659720` offsets `105-113`; context: [20] It is well established that the party seeking leave to appeal bears the onus of adducing all of the evidence and arguments required to meet the requirements of subsection 58(1): see, e.
- Evidence: `reasoning_application` cue `applied` at chunk `4659720` offsets `373-380`; context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4659720` offsets `308-320`; context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659721` offsets `203-211`; context: Griffin does not identify or point to any evidence he presented that the General Division failed to consider, nor does he provide any basis on which it can be said that the General Division’s findings were capricious or perverse, or that its decision was rendered in a procedurally unfair manner.
- Evidence: `governing_rule` cue `under` at chunk `4659721` offsets `585-590`; context: In my view, this does not disclose a valid ground of appeal under subsection 58(1) of the Act.
- Evidence: `counterargument_limitation` cue `However` at chunk `4659721` offsets `148-155`; context: However, Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4659722` offsets `15-22`; context: [22] In short, because Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4659723` offsets `122-130`; context: Griffin asks this Court to perform the same task he requested of the Appeal Division: to reweigh the evidence that was before the General Division and come to a different conclusion.
- Evidence: `reasoning_application` cue `accordingly` at chunk `4659723` offsets `525-536`; context: Conclusions [24] In conclusion, the Appeal Division’s decision was reasonable and, accordingly, Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `4659723` offsets `204-211`; context: However, as noted above, that is not the proper role of this Court on judicial review – on judicial review it is not the place of this Court to reweigh the evidence that was before the Appeal Division and come to its own conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4659723` offsets `587-596`; context: Griffin’s application for judicial review is dismissed.

#### Section text

IV. Standard of Review [13] The applicable standard for this Court’s review of a decision of the Appeal Division granting or denying leave to appeal a decision of the General Division is that of reasonableness: see: Canada (Attorney General) v. Hines, 2016 FC 112 at para 28, [2016] FCJ No 84; Canada (Attorney General) v. Hoffman, 2015 FC 1348 at paras 26-27, [2015] FCJ No 1511; also see: Tracey v Canada (Attorney General), 2015 FC 1300 at para 17, [2015] FCJ No 1410 [Tracey].

[14] This being so, the Appeal Division’s assessment of the evidence is entitled to deference (see: Dunsmuir v New Brunswick, 2008 SCC 9 at para 53, [2008] 1 SCR 190 [Dunsmuir]). The Court should not interfere if the Appeal Division’s decision is intelligible, transparent, and justifiable, and falls within a range of possible, acceptable outcomes defensible in respect of the facts and the law (Dunsmuir at para 47). Those criteria are met if “the reasons allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes”: Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16, [2011] 3 SCR 708. Moreover, it is not up to this Court to reweigh the evidence that was before the Appeal Division, and it is not the function of this Court to substitute its own view of a preferable outcome: Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61, [2009] 1 SCR 339.
V. Mr. Griffin’s Affidavit and Additional Arguments [15] The Respondent submits that Mr. Griffin’s affidavit introduces new evidence that was not before the Appeal Division concerning his familial obligations, BDC’s health and safety practices, and his own health at the time he left his employment. The Respondent states, in view of Canada (Attorney General) v. Merrigan, 2004 FCA 253, 325 NR 294 , and Ochapowace First Nation v. Canada (Attorney General), 2007 FC 920, 316 FTR 19, that the record on judicial review is restricted to the material that was before the Appeal Division at the time its decision was made (also see: Association of Universities and Colleges of Canada v. Canadian Copyright Licensing Agency (Access Copyright), 2012 FCA 22 at para. 19, 428 NR 297). According to the Respondent, Mr. Griffin’s attempt to introduce new evidence is improper and should not be considered by the Court.

[16] I agree. The evidence as to Mr. Griffin’s familial obligations, BDC’s health and safety practices, and his own health was not before the Appeal Division and, accordingly, cannot be and has not been considered by the Court in reviewing the reasonableness of the Appeal Division’s decision.

[17] I also agree with the Respondent that the Court should not consider Mr. Griffin’s argument that the Court should issue a declaration that any amount he owes to the Commission should be written off. This issue is not properly before the Court because Mr. Griffin did not request such relief from the Commission and the issue does not form part of the Appeal Division’s decision.
VI. Is the Appeal Division’s Decision Reasonable? [18] Mr. Griffin contends that he had just cause to leave his employment with BDC because he had no other alternative to doing so. Specifically, Mr. Griffin argues he could not remain in his employment because he could not afford to pay for accommodations in Red Deer for the duration of his employment. Mr. Griffin says his belief that he had no alternative but to leave his position is sufficient to establish that he had just cause for ending his employment. Mr. Griffin also contends that the Appeal Division failed to consider all the evidence in relation to the quantum of the penalty imposed on him, and that he should not be forced to repay the benefits he received because repayment would cause him undue hardship.

[19] The Respondent submits that, pursuant to subsection 58(1) of the Act, the Appeal Division may only grant leave to appeal a decision of the General Division where it is satisfied that an appellant has a reasonable chance of success based on one or more of the grounds of appeal listed in subsection 58(1). According to the Respondent, it was entirely reasonable for the Appeal Division to find that Mr. Griffin failed to establish that his appeal had a reasonable chance of success on any of the three enumerated grounds of appeal. The Respondent argues that Mr. Griffin simply disagrees with the General Division’s decision which, in the Respondent’s view, is not sufficient for the Appeal Division to grant leave pursuant to subsection 58(1) of the Act. Accordingly, the Respondent submits that the Appeal Division’s decision was reasonable and that this application for judicial review should be dismissed.

[20] It is well established that the party seeking leave to appeal bears the onus of adducing all of the evidence and arguments required to meet the requirements of subsection 58(1): see, e.g., Tracey, above, at para 31; also see Auch v. Canada (Attorney General), 2016 FC 199 at para 52, [2016] FCJ No 155. Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner. On the contrary, the Appeal Division should review the underlying record and determine whether the decision failed to properly account for any of the evidence: Karadeolian v. Canada (Attorney General), 2016 FC 615 at para 10, [2016] FCJ No 615.

[21] In this case, Mr. Griffin’s sole argument for granting leave to appeal was that the General Division had erred in its assessment of the facts. However, Mr. Griffin does not identify or point to any evidence he presented that the General Division failed to consider, nor does he provide any basis on which it can be said that the General Division’s findings were capricious or perverse, or that its decision was rendered in a procedurally unfair manner. Mr. Griffin simply disagrees with the General Division’s findings. In my view, this does not disclose a valid ground of appeal under subsection 58(1) of the Act.

[22] In short, because Mr. Griffin failed to establish any of the grounds of appeal specified in subsection 58(1), the Act necessitated that his appeal be refused. As such, the Appeal Division’s decision to such effect was reasonable.

[23] In essence, Mr. Griffin asks this Court to perform the same task he requested of the Appeal Division: to reweigh the evidence that was before the General Division and come to a different conclusion. However, as noted above, that is not the proper role of this Court on judicial review – on judicial review it is not the place of this Court to reweigh the evidence that was before the Appeal Division and come to its own conclusion.
VII. Conclusions [24] In conclusion, the Appeal Division’s decision was reasonable and, accordingly, Mr. Griffin’s application for judicial review is dismissed.

[25] Having regard to all of the circumstances of this case, and the Respondent’s position that it is not seeking costs, no costs shall be awarded.


## 13382:3 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e96f41c23b3a85d49c8036bed854ae4dc7371955b9dad568bb0da72526ffc6dd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13382:3:subtheme:1 · paragraphs 22-23

- Raw key terms: `applicant, application, attorney, award, boswell, canada, cause, costs`
- Display key terms: `award, boswell, costs`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: award, boswell, costs Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that: the Applicant’s application is dismissed; and there is no award of costs. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4659724` offsets `219-228`; context: JUDGMENT
THIS COURT’S JUDGMENT is that: the Applicant’s application is dismissed; and there is no award of costs.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that: the Applicant’s application is dismissed; and there is no award of costs.
"Keith M. Boswell"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-124-16
STYLE OF CAUSE:
SEAN GRIFFIN v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
St. John’s, Newfoundland and Labrador
DATE OF HEARING:
July 7, 2016


## 13382:4 · paragraphs 24-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e776910144598ec22b94b2a4c6986429a8fbd8d92f981e3dc70a0de69e832b81`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13382:4:subtheme:1 · paragraphs 24-24

- Raw key terms: `appearances, applicant, attorney, behalf, boswell, canada, dated, deputy`
- Display key terms: `behalf, boswell, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, boswell, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
BOSWELL J.
DATED:
july 26, 2016
APPEARANCES:
Sean Griffin
For The Applicant
(ON HIS OWN BEHALF)
Stephanie Yung-Hing
For The Respondent
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Gatineau, Quebec
For The Respondent
