# Discussion Units: case 10319

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **34**
- Continuity pairs: **33**
- Discussion Units: **2**
- Paragraph source hashes: **34**
- Sub-themes: **8**

## 10319:1 · paragraphs 0-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `869cca513db2b95497e7d89b0972a036a9233e96e15df66e814a056095950460`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10319:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `general, miter, appeal, benefits, decision, disability, division, found`
- Display key terms: `miter, benefits, disability, division`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: miter, benefits, disability, division Position/evidence statements: In her reconsideration application, she claimed that her disability commenced in 2003. | [4] Her application was denied in November 2013, and again denied after reconsideration in February 2014, based on the fact that she did not meet the contributory requirements for the time she claimed a disability. Rule/authority context: The Appeal Division dismissed her appeal of the decision of the General Division of the Social Security Tribunal [General Division] pursuant to section 58 of the Department of Employment and Social Development Act, SC 20 | The Appeal Division Decision under Review [7] The Appeal Division found that Ms. Application context: Miter applied for CPP disability benefits in 2013. | [8] The Appeal Division found that the General Division had correctly stated the test for summary dismissal, had correctly applied that test and had correctly concluded that the appeal had no reasonable chance of success Operative outcome context: The Appeal Division dismissed her appeal of the decision of the General Division of the Social Security Tribunal [General Division] pursuant to section 58 of the Department of Employment and Social Development Act, SC 20 | [4] Her application was denied in November 2013, and again denied after reconsideration in February 2014, based on the fact that she did not meet the contributory requirements for the time she claimed a disability. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4518550` offsets `450-460`; context: The General Division had found that Ms.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4518550` offsets `317-328`; context: The Appeal Division dismissed her appeal of the decision of the General Division of the Social Security Tribunal [General Division] pursuant to section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [the Act].
- Evidence: `disposition` cue `dismissed` at chunk `4518550` offsets `205-214`; context: The Appeal Division dismissed her appeal of the decision of the General Division of the Social Security Tribunal [General Division] pursuant to section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [the Act].
- Evidence: `party_position` cue `claimed` at chunk `4518551` offsets `276-283`; context: In her reconsideration application, she claimed that her disability commenced in 2003.
- Evidence: `reasoning_application` cue `applied` at chunk `4518551` offsets `14-21`; context: Miter applied for CPP disability benefits in 2013.
- Evidence: `party_position` cue `claimed` at chunk `4518552` offsets `193-200`; context: [4] Her application was denied in November 2013, and again denied after reconsideration in February 2014, based on the fact that she did not meet the contributory requirements for the time she claimed a disability.
- Evidence: `disposition` cue `denied` at chunk `4518552` offsets `24-30`; context: [4] Her application was denied in November 2013, and again denied after reconsideration in February 2014, based on the fact that she did not meet the contributory requirements for the time she claimed a disability.
- Evidence: `evidence_fact` cue `found that` at chunk `4518553` offsets `214-224`; context: The General Division found that the Applicant’s contributory period was 2004-2010, but she had made contributions only in 2007 and 2010, which did not meet the requirement to have made contributions in four out of the six years in the relevant contributory period, which is the period preceding the claim for benefits, or to have made valid contributions for at least 25 years including three of the last six years.
- Evidence: `counterargument_limitation` cue `but` at chunk `4518553` offsets `276-279`; context: The General Division found that the Applicant’s contributory period was 2004-2010, but she had made contributions only in 2007 and 2010, which did not meet the requirement to have made contributions in four out of the six years in the relevant contributory period, which is the period preceding the claim for benefits, or to have made valid contributions for at least 25 years including three of the last six years.
- Evidence: `disposition` cue `dismissed` at chunk `4518553` offsets `92-101`; context: The General Division summarily dismissed the appeal on August 18, 2015 finding that the appeal had no reasonable chance of success.
- Evidence: `party_position` cue `argued` at chunk `4518554` offsets `93-99`; context: She argued that the General Division had failed to meet a principle of natural justice and had made factual errors.
- Evidence: `evidence_fact` cue `found that` at chunk `4518554` offsets `416-426`; context: The Appeal Division Decision under Review [7] The Appeal Division found that Ms.
- Evidence: `governing_rule` cue `under` at chunk `4518554` offsets `379-384`; context: The Appeal Division Decision under Review [7] The Appeal Division found that Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `4518555` offsets `24-34`; context: [8] The Appeal Division found that the General Division had correctly stated the test for summary dismissal, had correctly applied that test and had correctly concluded that the appeal had no reasonable chance of success on the evidence before it.
- Evidence: `reasoning_application` cue `applied` at chunk `4518555` offsets `123-130`; context: [8] The Appeal Division found that the General Division had correctly stated the test for summary dismissal, had correctly applied that test and had correctly concluded that the appeal had no reasonable chance of success on the evidence before it.

#### 10319:1:subtheme:2 · paragraphs 7-8

- Raw key terms: `appeal, division, general, review, standard, arguments, assess, atkinson`
- Display key terms: `division, review, standard, arguments, assess, atkinson`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, review, standard, arguments, assess, atkinson Rule/authority context: The Standard of Review [10] The sole issue in this judicial review is whether the Appeal Division’s decision to dismiss Ms. | [11] The standard of review for decisions of the Appeal Division to grant or to deny leave to appeal is reasonableness (Reinhardt v Canada (Attorney General), 2016 FCA 158 at para 15; Atkinson v Canada (Attorney General) Application context: It was, therefore, unnecessary to consider the medical information to assess whether it established a prolonged disability. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4518556` offsets `457-464`; context: It was, therefore, unnecessary to consider the medical information to assess whether it established a prolonged disability.
- Evidence: `evidence_fact` cue `found that` at chunk `4518556` offsets `160-170`; context: The Appeal Division found that establishing a disability is only one part of the eligibility requirements for CPP disability benefits.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4518556` offsets `513-531`; context: The Standard of Review [10] The sole issue in this judicial review is whether the Appeal Division’s decision to dismiss Ms.
- Evidence: `reasoning_application` cue `therefore` at chunk `4518556` offsets `388-397`; context: It was, therefore, unnecessary to consider the medical information to assess whether it established a prolonged disability.
- Evidence: `governing_rule` cue `standard of review` at chunk `4518557` offsets `9-27`; context: [11] The standard of review for decisions of the Appeal Division to grant or to deny leave to appeal is reasonableness (Reinhardt v Canada (Attorney General), 2016 FCA 158 at para 15; Atkinson v Canada (Attorney General), 2014 FCA 187 at paras 22-33.

#### 10319:1:subtheme:3 · paragraphs 9-10

- Raw key terms: `considers, reasonable, acceptable, acknowledged, applicant, application, began, benefits`
- Display key terms: `considers, reasonable, acceptable, acknowledged, began, benefits`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: considers, reasonable, acceptable, acknowledged, began, benefits Rule/authority context: [13] As explained at the hearing, the standard of reasonableness is a legal concept which has been interpreted in the jurisprudence. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4518558` offsets `18-25`; context: [12] To determine whether a decision is reasonable, the Court looks for “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4518559` offsets `118-131`; context: [13] As explained at the hearing, the standard of reasonableness is a legal concept which has been interpreted in the jurisprudence.

#### 10319:1:subtheme:4 · paragraphs 11-13

- Raw key terms: `miter, acknowledges, benefits, contributions, health, made, past, period`
- Display key terms: `miter, acknowledges, benefits, contributions, health, made, past, period`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: miter, acknowledges, benefits, contributions, health, made, past, period Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4518560` offsets `106-112`; context: Miter submitted a written account describing her health issues in detail, a chronology of her pursuit of a diagnosis and treatment with several doctors, copies of correspondence from several doctors that had been submitted to the General Division and Appeal Division and a copy of the April 29, 2016 decision of the Ontario Health Professions Appeal and Review Board which considered the results of an investigation into Ms.

#### 10319:1:subtheme:5 · paragraphs 14-15

- Raw key terms: `benefits, contributions, disability, miter, respondent, ability, appeal, applied`
- Display key terms: `benefits, contributions, disability, miter, ability, applied`
- Argument roles: `counterargument_limitation, disposition, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, party_position, reasoning_application Display terms: benefits, contributions, disability, miter, ability, applied Position/evidence statements: Miter did not meet the eligibility requirements for a CPP disability pension, whether her disability arose in 2003, at the time of her surgery, or in 2011, as she stated in her first benefits claim. | [20] The Respondent submits that the Appeal Division did not err in finding that the General Division properly summarily dismissed the appeal as it did not have a reasonable chance of success. Application context: Miter applied for benefits in 2013. | She now submits that she is in need of the CPP disability benefits because she remains disabled, cannot work and has medical and drug expenses. Operative outcome context: [20] The Respondent submits that the Appeal Division did not err in finding that the General Division properly summarily dismissed the appeal as it did not have a reasonable chance of success. Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4518563` offsets `123-130`; context: Miter did not meet the eligibility requirements for a CPP disability pension, whether her disability arose in 2003, at the time of her surgery, or in 2011, as she stated in her first benefits claim.
- Evidence: `party_position` cue `claim` at chunk `4518563` offsets `237-242`; context: Miter did not meet the eligibility requirements for a CPP disability pension, whether her disability arose in 2003, at the time of her surgery, or in 2011, as she stated in her first benefits claim.
- Evidence: `reasoning_application` cue `applied` at chunk `4518563` offsets `254-261`; context: Miter applied for benefits in 2013.
- Evidence: `issue` cue `issues` at chunk `4518564` offsets `315-321`; context: She describes long-standing health issues that interfered with her ability to work and to make contributions to the CPP.
- Evidence: `party_position` cue `submits` at chunk `4518564` offsets `20-27`; context: [20] The Respondent submits that the Appeal Division did not err in finding that the General Division properly summarily dismissed the appeal as it did not have a reasonable chance of success.
- Evidence: `reasoning_application` cue `because` at chunk `4518564` offsets `468-475`; context: She now submits that she is in need of the CPP disability benefits because she remains disabled, cannot work and has medical and drug expenses.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4518564` offsets `498-504`; context: She now submits that she is in need of the CPP disability benefits because she remains disabled, cannot work and has medical and drug expenses.
- Evidence: `disposition` cue `dismissed` at chunk `4518564` offsets `121-130`; context: [20] The Respondent submits that the Appeal Division did not err in finding that the General Division properly summarily dismissed the appeal as it did not have a reasonable chance of success.

#### 10319:1:subtheme:6 · paragraphs 16-21

- Raw key terms: `appeal, division, benefits, contributions, made, miter, period, years`
- Display key terms: `division, benefits, contributions, made, miter, period, years`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, benefits, contributions, made, miter, period, years Rule/authority context: [24] The Appeal Division noted the requirements for CPP disability benefits, which are: to be under 65 years of age; to not be in receipt of the CPP retirement pension; to be disabled; and to have made valid contribution Application context: [23] I find that the Appeal Division did not err; it properly applied the law to the facts before it. Evidence spans paragraphs 16-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4518565` offsets `82-87`; context: Miter’s health conditions, the issue before the Court is whether the Appeal Division erred in applying the law that governs Appeals from denials of benefits.
- Evidence: `reasoning_application` cue `I find` at chunk `4518566` offsets `5-11`; context: [23] I find that the Appeal Division did not err; it properly applied the law to the facts before it.
- Evidence: `governing_rule` cue `under` at chunk `4518567` offsets `94-99`; context: [24] The Appeal Division noted the requirements for CPP disability benefits, which are: to be under 65 years of age; to not be in receipt of the CPP retirement pension; to be disabled; and to have made valid contributions to the CPP for not less than the Minimum Qualifying Period [MQP].
- Evidence: `evidence_fact` cue `found that` at chunk `4518570` offsets `82-92`; context: Miter and found that they did not reflect any of the grounds for appeal set out in section 58 of the Act, which are the only grounds for an appeal, and which further provides that leave to appeal will be refused if the Appeal Division “is satisfied that the appeal has no reasonable chance of success.

#### 10319:1:subtheme:7 · paragraphs 22-32

- Raw key terms: `appeal, general, court, decision, applicant, benefits, attorney, based`
- Display key terms: `benefits, based`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: benefits, based Rule/authority context: [28] Under subsection 58(1) of Act, the only grounds of appeal are that: 58 (1) The only grounds of appeal are that 58 (1) Les seuls moyens d’appel sont les suivants : (a) the General Division failed to observe a princip | [29] To simplify the above, the grounds of appeal are limited to: (a) a breach of procedural fairness, which focusses on the process before the decision maker(s), such as whether an applicant had an opportunity to make s Application context: Like the Board, this Court is bound to apply the provisions of the Plan and cannot disregard those provisions so as to remedy what might be considered or perceived as an unfair and/or unjust result. | [32] The same finding applies in the present case. Operative outcome context: [3] I am unable to find any error with the Board’s decision which would have allowed us to intervene. | JUDGMENT THIS COURT’S JUDGMENT is that: The application for judicial review is dismissed. Evidence spans paragraphs 22-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4518571` offsets `501-508`; context: [28] Under subsection 58(1) of Act, the only grounds of appeal are that:
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4518571` offsets `553-559`; context: [28] Under subsection 58(1) of Act, the only grounds of appeal are that:
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `Under` at chunk `4518571` offsets `5-10`; context: [28] Under subsection 58(1) of Act, the only grounds of appeal are that:
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `issue` cue `whether` at chunk `4518572` offsets `171-178`; context: [29] To simplify the above, the grounds of appeal are limited to: (a) a breach of procedural fairness, which focusses on the process before the decision maker(s), such as whether an applicant had an opportunity to make submissions; (b) an error of law, such as the application of incorrect statutory provisions or principles of the jurisprudence; and (c) an error of fact, such as ignoring a relevant fact or misunderstanding a fact.
- Evidence: `governing_rule` cue `principles` at chunk `4518572` offsets `314-324`; context: [29] To simplify the above, the grounds of appeal are limited to: (a) a breach of procedural fairness, which focusses on the process before the decision maker(s), such as whether an applicant had an opportunity to make submissions; (b) an error of law, such as the application of incorrect statutory provisions or principles of the jurisprudence; and (c) an error of fact, such as ignoring a relevant fact or misunderstanding a fact.
- Evidence: `reasoning_application` cue `apply` at chunk `4518576` offsets `141-146`; context: Like the Board, this Court is bound to apply the provisions of the Plan and cannot disregard those provisions so as to remedy what might be considered or perceived as an unfair and/or unjust result.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4518576` offsets `178-184`; context: Like the Board, this Court is bound to apply the provisions of the Plan and cannot disregard those provisions so as to remedy what might be considered or perceived as an unfair and/or unjust result.
- Evidence: `disposition` cue `allowed` at chunk `4518576` offsets `77-84`; context: [3] I am unable to find any error with the Board’s decision which would have allowed us to intervene.
- Evidence: `reasoning_application` cue `applies` at chunk `4518577` offsets `22-29`; context: [32] The same finding applies in the present case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4518579` offsets `104-112`; context: [34] The Appeal Division’s decision to dismiss the appeal is based on the provisions of the law and the evidence before it.
- Evidence: `reasoning_application` cue `apply` at chunk `4518580` offsets `339-344`; context: The Court must apply the law and cannot bend the requirements of this complex contributory social benefits scheme.
- Evidence: `disposition` cue `dismissed` at chunk `4518580` offsets `664-673`; context: JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.

#### Section text

Miter v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-03-03
Neutral citation
2017 FC 262
File numbers
T-1080-16
Decision Content
Date: 20170303
Docket: T-1080-16
Citation: 2017 FC 262
Ottawa, Ontario, March 3, 2017
PRESENT: The Honourable Madam Justice Kane
BETWEEN:
RODICA MITER
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] The Applicant, Ms. Rodica Miter, seeks judicial review of the decision of the Appeal Division of the Social Security Tribunal Appeal Division [Appeal Division], dated May 30, 2016. The Appeal Division dismissed her appeal of the decision of the General Division of the Social Security Tribunal [General Division] pursuant to section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [the Act]. The General Division had found that Ms. Miter’s appeal of the denial of disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] had no reasonable chance of success.
I. Background [2] Ms. Miter recounts that she had surgery in 2003 and since that time has experienced a wide range of medical symptoms that have had a severe impact on her health and ability to work. She recounts that doctors repeatedly dismissed and/or misdiagnosed her medical conditions.

[3] Ms. Miter applied for CPP disability benefits in 2013. In the application for benefits, she stated that she had not been able to work in her custom drapery and interiors business since 2011 due to her debilitating health condition. In her reconsideration application, she claimed that her disability commenced in 2003.

[4] Her application was denied in November 2013, and again denied after reconsideration in February 2014, based on the fact that she did not meet the contributory requirements for the time she claimed a disability.

[5] Ms. Miter appealed the decision to the General Division. The General Division summarily dismissed the appeal on August 18, 2015 finding that the appeal had no reasonable chance of success. The General Division found that the Applicant’s contributory period was 2004-2010, but she had made contributions only in 2007 and 2010, which did not meet the requirement to have made contributions in four out of the six years in the relevant contributory period, which is the period preceding the claim for benefits, or to have made valid contributions for at least 25 years including three of the last six years.

[6] Ms. Miter then appealed the decision of the General Division to the Appeal Division. She argued that the General Division had failed to meet a principle of natural justice and had made factual errors. She argued that she was unable to work due to her medical condition and that the Appeal Division should consider additional medical records.
II. The Appeal Division Decision under Review [7] The Appeal Division found that Ms. Miter had not made the required contributions in the relevant period and that she did not dispute this fact. As she did not meet one of the two statutory requirements for disability benefits (which are valid contributions and the establishment of a disability in the relevant period), the appeal could not succeed. The Appeal Division found that the General Division had not made any factual errors and that Ms. Miter’s allegation of a breach of natural justice appeared to be based on her claims regarding medical malpractice and was not related to the process in the General Division.

[8] The Appeal Division found that the General Division had correctly stated the test for summary dismissal, had correctly applied that test and had correctly concluded that the appeal had no reasonable chance of success on the evidence before it.

[9] The Appeal Division considered Ms. Miter’s arguments that the General Division should have considered her medical records and opinions. The Appeal Division found that establishing a disability is only one part of the eligibility requirements for CPP disability benefits. The other requirement is to meet the minimum qualifying period contributions. Ms. Miter had not done so. It was, therefore, unnecessary to consider the medical information to assess whether it established a prolonged disability.
III. The Standard of Review [10] The sole issue in this judicial review is whether the Appeal Division’s decision to dismiss Ms. Miter’s appeal is reasonable.

[11] The standard of review for decisions of the Appeal Division to grant or to deny leave to appeal is reasonableness (Reinhardt v Canada (Attorney General), 2016 FCA 158 at para 15; Atkinson v Canada (Attorney General), 2014 FCA 187 at paras 22-33.

[12] To determine whether a decision is reasonable, the Court looks for “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190).

[13] As explained at the hearing, the standard of reasonableness is a legal concept which has been interpreted in the jurisprudence. It may not reflect what Ms. Miter considers to be reasonable from her perspective, as that term is used in every-day language.
IV. The Applicant’s Submissions [14] Ms. Miter submits that her disability, which began with surgery in 2003, prevented her from working continuously and, as a result, from making contributions to the CPP in subsequent years. She explains that if she had received proper treatment and diagnosis, her health would not have deteriorated and she could have continued to work and to make contributions to the CPP. She also explains that if the doctors she consulted had acknowledged their misdiagnosis and/or had provided her with the necessary supporting medical documents she could have pursued her application for benefits earlier. Ms. Miter suggests that she could not obtain medical records from doctors who were concealing their misdiagnosis of her health conditions.

[15] On this application for judicial review, Ms. Miter submitted a written account describing her health issues in detail, a chronology of her pursuit of a diagnosis and treatment with several doctors, copies of correspondence from several doctors that had been submitted to the General Division and Appeal Division and a copy of the April 29, 2016 decision of the Ontario Health Professions Appeal and Review Board which considered the results of an investigation into Ms. Miter’s allegations against doctors who had treated her, primarily in the period around 2011-2013.

[16] Ms. Miter notes that she made contributions to the CPP throughout her working life, but could not do so more recently due to her deteriorating health. She questions why a broader examination of her contributions in the past cannot be relied on to provide her with the benefits she now needs, including to pay for her medication.
V. The Respondent’s Submissions [17] The Respondent acknowledges and sympathizes with Ms. Miter’s description of her serious health conditions.

[18] The Respondent explains that the CPP is a contributory plan to provide benefits where the eligibility criteria are met. The eligibility criteria in the CPP are strict and inflexible; an applicant must be both disabled as defined in the CPP and meet the contribution requirements for the relevant period. The Respondent acknowledges that Ms. Miter made contributions to the CPP in the past. The Respondent’s records note that contributions were made in 1979-1982, 1985-1988, 2000-2001, 2007 and 2010.

[19] The Respondent notes, however, that Ms. Miter did not meet the eligibility requirements for a CPP disability pension, whether her disability arose in 2003, at the time of her surgery, or in 2011, as she stated in her first benefits claim. Ms. Miter applied for benefits in 2013. The relevant six year period to assess her contributions is 2007- 2013. Ms. Miter made contributions for only two years (2007 and 2010), rather than the four years required in the relevant six year period.

[20] The Respondent submits that the Appeal Division did not err in finding that the General Division properly summarily dismissed the appeal as it did not have a reasonable chance of success.
VI. The Appeal Division Did Not Err [21] Ms. Miter is in a very unfortunate situation. She describes long-standing health issues that interfered with her ability to work and to make contributions to the CPP. She now submits that she is in need of the CPP disability benefits because she remains disabled, cannot work and has medical and drug expenses.

[22] Although the Court is very sympathetic to Ms. Miter’s health conditions, the issue before the Court is whether the Appeal Division erred in applying the law that governs Appeals from denials of benefits.

[23] I find that the Appeal Division did not err; it properly applied the law to the facts before it.

[24] The Appeal Division noted the requirements for CPP disability benefits, which are: to be under 65 years of age; to not be in receipt of the CPP retirement pension; to be disabled; and to have made valid contributions to the CPP for not less than the Minimum Qualifying Period [MQP].

[25] The MQP is set out in subsection 44(2) of the CPP and, at its simplest explanation, provides that an applicant has made contributions in four of the last six years within the relevant contributory period or has made valid contributions for at least 25 years including three of the last six years.

[26] Ms. Miter made contributions in 2007 and 2010. In her 2013 claim for benefits she stated that her disability began in 2011 and she stopped working at that time. Clearly she had not made contributions in four of the six years in her contributory period. She did not dispute this at the General Division, at the Appeal Division or before this Court.

[27] The Appeal Division addressed the grounds for appeal argued by Ms. Miter and found that they did not reflect any of the grounds for appeal set out in section 58 of the Act, which are the only grounds for an appeal, and which further provides that leave to appeal will be refused if the Appeal Division “is satisfied that the appeal has no reasonable chance of success.”

[28] Under subsection 58(1) of Act, the only grounds of appeal are that:
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.

[29] To simplify the above, the grounds of appeal are limited to: (a) a breach of procedural fairness, which focusses on the process before the decision maker(s), such as whether an applicant had an opportunity to make submissions; (b) an error of law, such as the application of incorrect statutory provisions or principles of the jurisprudence; and (c) an error of fact, such as ignoring a relevant fact or misunderstanding a fact.

[30] As noted by Justice Manson in Canada (Attorney General) v O’Keefe, 2016 FC 503:

[29] The DESDA makes clear that Parliament intended that the SST-AD only hear appeals properly falling within a ground of appeal and that have a reasonable chance of success. The DESDA does not grant the SST-AD broad discretion in deciding leave, and should the SST-AD grant leave to appeal in other than the instances outlined in section 58, they have improperly stepped beyond the delegated authority provided them by their governing statute.

[31] In Pleasant-Joseph v Canada (Attorney General), 2009 FCA 173, the Court of Appeal considered the appeal of a denial of CPP disability benefits based on the applicant’s failure to satisfy the contribution requirements. The Court of Appeal found, at paragraph 3:

[3] I am unable to find any error with the Board’s decision which would have allowed us to intervene. Like the Board, this Court is bound to apply the provisions of the Plan and cannot disregard those provisions so as to remedy what might be considered or perceived as an unfair and/or unjust result.

[32] The same finding applies in the present case. The role of the Court is not to determine an applicant’s eligibility for disability benefits. Even if that were the role of the Court, it could not ignore the clear eligibility requirements of the Act.

[33] The existence of a severe health condition on its own is not sufficient to be awarded CPP disability benefits. An applicant must also demonstrate that he or she made contributions for not less than the MQP as required by subsection 44(2) of the CPP.

[34] The Appeal Division’s decision to dismiss the appeal is based on the provisions of the law and the evidence before it. The role of the Court is to determine if the Appeal Division made a reasonable decision based on the facts and the law. The Appeal Division’s decision to affirm the General Division’s decision that Ms. Miter’s appeal had no reasonable chance of success is a reasonable decision. Moreover, it is the only decision the Appeal Division could have reached.

[35] The Court understands Ms. Miter’s frustration in pursuing several levels of appeals with respect to the denial of her benefits, which likely gave her some false hope that benefits could be provided. She asks why the CPP cannot be interpreted more liberally to better meet her needs and the needs of other contributors. The Court must apply the law and cannot bend the requirements of this complex contributory social benefits scheme. The same applies to the Appeal Division, the General Division and the decision makers within the Department of Employment and Social Development.
JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.
No costs are ordered.
"Catherine M. Kane"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1080-16
STYLE OF CAUSE:
RODICA MITER v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
February 7, 2017


## 10319:2 · paragraphs 33-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5dca8dc5316d97a144b8a2d28158ba512bf77fe69fad4b757cf2400d9b52ebbe`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10319:2:subtheme:1 · paragraphs 33-33

- Raw key terms: `appearances, applicant, attorney, canada, dated, deputy, doucette, general`
- Display key terms: `dated, deputy, doucette`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy, doucette No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 33-33. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT and reasons:
KANE J.
DATED:
march 3, 2017
APPEARANCES:
Rodica Miter
For The Applicant
RODICA MITER
Sandra Doucette
For The Respondent
ATTORNEY GENERAL OF CANADA
SOLICITORS OF RECORD:
None
For The Applicant
RODICA MITER
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
ATTORNEY GENERAL OF CANADA
