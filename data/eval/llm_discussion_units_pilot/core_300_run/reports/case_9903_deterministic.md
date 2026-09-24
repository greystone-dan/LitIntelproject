# Discussion Units: case 9903

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **25**
- Continuity pairs: **24**
- Discussion Units: **4**
- Paragraph source hashes: **25**
- Sub-themes: **6**

## 9903:1 · paragraphs 0-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f8c66057f00f2e745bce4561cd8d4f6236e3c1b22d7042b4d4b74da79e371c8b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9903:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `parchment, division, general, appeal, work, decision, disability, another`
- Display key terms: `parchment, division, work, disability, another`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: parchment, division, work, disability, another Position/evidence statements: He argues that the Appeal Division ignored medical reports that, according to Mr. Rule/authority context: Parchment, a self-represented Applicant, seeks judicial review of the decision upholding a denial of his claim to a disability pension under the provisions of the Canada Pension Plan, RSC 1985, c. | Accordingly, his disability did not meet the definition of “severe and prolonged” pursuant to the CPP legislation. Application context: Parchment’s arguments, medical evidence was not overlooked, and I conclude that the decision of the Appeal Division is reasonable. | Parchment applied for CPP disability benefits, describing his disabilities as neck, back and shoulder pain. Operative outcome context: Therefore, this application for judicial review is dismissed. | His application for disability coverage through his private insurer was denied. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4500479` offsets `561-566`; context: Parchment, a self-represented Applicant, seeks judicial review of the decision upholding a denial of his claim to a disability pension under the provisions of the Canada Pension Plan, RSC 1985, c.
- Evidence: `party_position` cue `argues` at chunk `4500480` offsets `144-150`; context: He argues that the Appeal Division ignored medical reports that, according to Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500480` offsets `293-301`; context: There is medical evidence that states he cannot return to his pre-accident work as a Chef.
- Evidence: `reasoning_application` cue `conclude` at chunk `4500480` offsets `596-604`; context: Parchment’s arguments, medical evidence was not overlooked, and I conclude that the decision of the Appeal Division is reasonable.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4500480` offsets `317-323`; context: There is medical evidence that states he cannot return to his pre-accident work as a Chef.
- Evidence: `disposition` cue `dismissed` at chunk `4500480` offsets `712-721`; context: Therefore, this application for judicial review is dismissed.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4500481` offsets `835-846`; context: Accordingly, his disability did not meet the definition of “severe and prolonged” pursuant to the CPP legislation.
- Evidence: `reasoning_application` cue `applied` at chunk `4500481` offsets `510-517`; context: Parchment applied for CPP disability benefits, describing his disabilities as neck, back and shoulder pain.
- Evidence: `counterargument_limitation` cue `although` at chunk `4500481` offsets `667-675`; context: In June 2012, his application was denied on the basis that although he may not be able to do his usual work, he was capable of doing other work.
- Evidence: `disposition` cue `denied` at chunk `4500481` offsets `435-441`; context: His application for disability coverage through his private insurer was denied.
- Evidence: `governing_rule` cue `under` at chunk `4500482` offsets `230-235`; context: The General Division also concluded that he was not eligible for a disability pension under the CPP, concluding that his disability was not “severe” prior to the minimum qualifying period [MQP] of December 31, 2013.
- Evidence: `evidence_fact` cue `found that` at chunk `4500484` offsets `25-35`; context: [8] The General Division found that although Mr.
- Evidence: `evidence_fact` cue `found that` at chunk `4500485` offsets `359-369`; context: Second, he argued that the General Division should not have found that his work experience gave him transferable skills.
- Evidence: `evidence_fact` cue `found that` at chunk `4500486` offsets `216-226`; context: The Appeal Division also found that the General Division considered the evidence, including Mr.
- Evidence: `evidence_fact` cue `determined that` at chunk `4500487` offsets `120-135`; context: The Appeal division determined that he did not raise a ground of appeal which had a reasonable chance of success.

#### Section text

Parchment v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-04-10
Neutral citation
2017 FC 354
File numbers
T-1219-16
Decision Content
Date: 20170410
Docket: T-1219-16
Citation: 2017 FC 354
Ottawa, Ontario, April 10, 2017
PRESENT: The Honourable Madam Justice McDonald
BETWEEN:
STERLING PARCHMENT
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Introduction [1] Mr. Parchment, a self-represented Applicant, seeks judicial review of the decision upholding a denial of his claim to a disability pension under the provisions of the Canada Pension Plan, RSC 1985, c. C-8 [CPP]. The Appeal Division of the Social Security Tribunal of Canada refused Mr. Parchment’s appeal from the General Division who confirmed the denial of his claim for CPP disability benefits.

[2] In 2010, Mr. Parchment was injured in a motor vehicle accident, and, other than for a brief period of time, he has not returned to work. He argues that the Appeal Division ignored medical reports that, according to Mr. Parchment, confirm that he is disabled from working. There is medical evidence that states he cannot return to his pre-accident work as a Chef. However, as both the General Division and the Appeal Division noted, there is also medical evidence that he is capable of working in another capacity. Despite Mr. Parchment’s arguments, medical evidence was not overlooked, and I conclude that the decision of the Appeal Division is reasonable. Therefore, this application for judicial review is dismissed. No costs are awarded.
II. Background [3] On June 1, 2010, Mr. Parchment was involved in a motor vehicle accident and sustained injuries to his neck, back, and left shoulder. He has ongoing complaints of pain and limitation of movement as a result of these injuries.

[4] Between December 2010 and September 2011, Mr. Parchment received disability benefits through his private insurer. When these benefits ceased in September 2011, he attempted to return to his job as a Chef. He struggled in his job, and also struggled in another position. These struggles ultimately led him to permanently leave his employment in November 2011. His application for disability coverage through his private insurer was denied.
III. Application for CPP benefits [5] In April 2012, Mr. Parchment applied for CPP disability benefits, describing his disabilities as neck, back and shoulder pain. In June 2012, his application was denied on the basis that although he may not be able to do his usual work, he was capable of doing other work. Accordingly, his disability did not meet the definition of “severe and prolonged” pursuant to the CPP legislation.

[6] Mr. Parchment requested a reconsideration of this decision, and on January 26, 2016, the General Division held a hearing by teleconference. The General Division also concluded that he was not eligible for a disability pension under the CPP, concluding that his disability was not “severe” prior to the minimum qualifying period [MQP] of December 31, 2013.

[7] The MQP is the date by which Mr. Parchment had to establish severe and prolonged disability within the meaning of the CPP scheme.

[8] The General Division found that although Mr. Parchment may not be able to return to his pre-accident employment, he did not prove that he was regularly incapable of pursuing any substantially gainful occupation within his work restrictions. Additionally, his medical evidence failed to show that he could not do another job. The General Division found that he was capable of performing lighter duties, as compared to his work as a Chef, and noted that he had no significant barriers to undergo retraining.

[9] Mr. Parchment appealed this decision.
IV. CPP Appeal Division Decision [10] Before the Appeal Division, Mr. Parchment argued that the General Division committed two errors. First, he argued that the hearing before the General Division should have been conducted in person or by videoconference. Second, he argued that the General Division should not have found that his work experience gave him transferable skills. He argued that his work experience only qualifies him for physical work.

[11] The Appeal Division concluded that the General Division did not breach any of Mr. Parchment’s procedural fairness rights by holding the hearing by teleconference, rather than in person. The Appeal Division also found that the General Division considered the evidence, including Mr. Parchment’s age, education and work history in relation to his capacity to regularly pursue other substantially gainful employment.

[12] On July 11, 2016, the Appeal Division refused Mr. Parchment’s application for leave to appeal. The Appeal division determined that he did not raise a ground of appeal which had a reasonable chance of success.


## 9903:2 · paragraphs 9-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a4da5f57d68e545c2ee945ea0d401a85b090cfe920051b7450a8fceeced30598`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9903:2:subtheme:1 · paragraphs 9-10

- Raw key terms: `appeal, division, para, paras, applicable, attorney, board, brunswick`
- Display key terms: `division, para, paras, applicable, brunswick`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: division, para, paras, applicable, brunswick Rule/authority context: Standard of review [14] The applicable standard of review of an Appeal Division decision is reasonableness (Tracey v Canada (Attorney General), 2015 FC 1300, at paras 18-23, confirmed by Karadeolian v Canada (Attorney Ge Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4500487` offsets `217-223`; context: Issues [13] There are 2 issues for determination:
Should Mr.
- Evidence: `governing_rule` cue `Standard of review` at chunk `4500487` offsets `379-397`; context: Standard of review [14] The applicable standard of review of an Appeal Division decision is reasonableness (Tracey v Canada (Attorney General), 2015 FC 1300, at paras 18-23, confirmed by Karadeolian v Canada (Attorney General), 2016 FC 615, at para 7).
- Evidence: `issue` cue `whether` at chunk `4500488` offsets `56-63`; context: [15] As a result, this Court is tasked with determining whether the Appeal Division’s conclusions are defensible in respect to the facts and the law.

#### 9903:2:subtheme:2 · paragraphs 11-14

- Raw key terms: `appeal, division, parchment, general, hearing, argues, considered, decide`
- Display key terms: `division, parchment, hearing, argues, considered, decide`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: division, parchment, hearing, argues, considered, decide Rule/authority context: Given this, and the fact that the General Division has the discretion to decide how to hold hearings, I agree with the Appeal Division that this does not constitute a valid ground of appeal under section 58 of the Depart Application context: [20] Therefore, I conclude that this argument is without merit. Operative outcome context: Parchment argues that the General Division should have granted him an in person hearing. Evidence spans paragraphs 11-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4500489` offsets `5-11`; context: [16] Issues of procedural fairness are considered on the standard of correctness (Moodie v Canada (Attorney General), 2015 FCA 87 at para 50; Mission Institution v Khela, 2014 SCC 24 at para 79 and Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43).
- Evidence: `disposition` cue `granted` at chunk `4500489` offsets `407-414`; context: Parchment argues that the General Division should have granted him an in person hearing.
- Evidence: `issue` cue `issue` at chunk `4500490` offsets `41-46`; context: [18] The Appeal Division considered this issue, but determined that Mr.
- Evidence: `evidence_fact` cue `determined that` at chunk `4500490` offsets `52-67`; context: [18] The Appeal Division considered this issue, but determined that Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500491` offsets `37-45`; context: Parchment does not point to evidence that was overlooked by the General division.
- Evidence: `governing_rule` cue `under` at chunk `4500491` offsets `386-391`; context: Given this, and the fact that the General Division has the discretion to decide how to hold hearings, I agree with the Appeal Division that this does not constitute a valid ground of appeal under section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA].
- Evidence: `reasoning_application` cue `Therefore` at chunk `4500492` offsets `5-14`; context: [20] Therefore, I conclude that this argument is without merit.

#### 9903:2:subtheme:3 · paragraphs 15-21

- Raw key terms: `appeal, division, general, chance, reasonable, success, error, evidence`
- Display key terms: `division, chance, reasonable, success, error`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: division, chance, reasonable, success, error Application context: [25] The Appeal Division applied the correct test in refusing leave and reasonably found that the Applicant had failed to raise a ground of appeal that had a reasonable chance of success. | Chan’s report, because it was consistent and in keeping with the other medical evidence. Operative outcome context: Therefore, this judicial review is dismissed without costs. Evidence spans paragraphs 15-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4500493` offsets `578-585`; context: [22] On an appeal, the Appeal Division considers the following as outlined in subsection 58(1) and (2) of the DESDA:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that:
58 (1) Les seuls moyens d’appel sont les suivants:
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4500493` offsets `630-636`; context: [22] On an appeal, the Appeal Division considers the following as outlined in subsection 58(1) and (2) of the DESDA:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that:
58 (1) Les seuls moyens d’appel sont les suivants:
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500494` offsets `176-184`; context: They also do not consider new evidence.
- Evidence: `evidence_fact` cue `found that` at chunk `4500496` offsets `83-93`; context: [25] The Appeal Division applied the correct test in refusing leave and reasonably found that the Applicant had failed to raise a ground of appeal that had a reasonable chance of success.
- Evidence: `reasoning_application` cue `applied` at chunk `4500496` offsets `25-32`; context: [25] The Appeal Division applied the correct test in refusing leave and reasonably found that the Applicant had failed to raise a ground of appeal that had a reasonable chance of success.
- Evidence: `evidence_fact` cue `found that` at chunk `4500497` offsets `25-35`; context: [26] The Appeal Division found that the General Division had considered the entirety of the medical evidence and had only emphasized Dr.
- Evidence: `reasoning_application` cue `because` at chunk `4500497` offsets `152-159`; context: Chan’s report, because it was consistent and in keeping with the other medical evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500498` offsets `131-139`; context: However, it is only the medical evidence which was before the General Division which is relevant for consideration.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500498` offsets `99-106`; context: However, it is only the medical evidence which was before the General Division which is relevant for consideration.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4500499` offsets `105-114`; context: Therefore, this judicial review is dismissed without costs.
- Evidence: `disposition` cue `dismissed` at chunk `4500499` offsets `140-149`; context: Therefore, this judicial review is dismissed without costs.

#### Section text

V. Issues [13] There are 2 issues for determination:
Should Mr. Parchment have received an in person hearing? Is the decision of the Appeal division reasonable?
VI. Standard of review [14] The applicable standard of review of an Appeal Division decision is reasonableness (Tracey v Canada (Attorney General), 2015 FC 1300, at paras 18-23, confirmed by Karadeolian v Canada (Attorney General), 2016 FC 615, at para 7).

[15] As a result, this Court is tasked with determining whether the Appeal Division’s conclusions are defensible in respect to the facts and the law. (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at paras 15 and 16; Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).

[16] Issues of procedural fairness are considered on the standard of correctness (Moodie v Canada (Attorney General), 2015 FCA 87 at para 50; Mission Institution v Khela, 2014 SCC 24 at para 79 and Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43).
VII. Analysis I. Should Mr. Parchment have received an in person hearing? [17] Mr. Parchment argues that the General Division should have granted him an in person hearing. He argues that the Appeal Division failed to acknowledge this error.

[18] The Appeal Division considered this issue, but determined that Mr. Parchment’s procedural fairness rights were not breached when the General Division hearing was held by teleconference, rather than in person. He did not show that he was disadvantaged by the fact he gave his testimony via teleconference. Further, it was within the discretion of the General Division to decide on the format of the hearing (section 21 of the Social Security Tribunal Regulations, SOR/2013-60). The General Division opted to hold the hearing by teleconference, as they determined it was the most expedient manner to proceed considering previous adjournments and the late submissions of a large volume of documents.

[19] Mr. Parchment does not point to evidence that was overlooked by the General division. Additionally, he does not allege that there were technical difficulties with the teleconference hearing. Given this, and the fact that the General Division has the discretion to decide how to hold hearings, I agree with the Appeal Division that this does not constitute a valid ground of appeal under section 58 of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA].

[20] Therefore, I conclude that this argument is without merit.
II. Is the decision of the Appeal division reasonable? [21] Mr. Parchment argues that the Appeal Division failed to give proper consideration to several medical reports, in particular, the reports of Dr. Sommerville, Dr. West and Dr. Chan. He argues that these reports prove he is disabled from employment.

[22] On an appeal, the Appeal Division considers the following as outlined in subsection 58(1) and (2) of the DESDA:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that:
58 (1) Les seuls moyens d’appel sont les suivants:
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
Criteria
Critère
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès

[23] In considering the appeal, the Appeal Division has a limited mandate. They have no authority to conduct a rehearing of Mr. Parchment’s case. They also do not consider new evidence. The Appeal Division’s jurisdiction is restricted to determining if the General Division committed an error (ss. 58(1) (a) through (c) of the DESDA) and the Appeal Division is satisfied that an appeal has a reasonable chance of success (58(2) of the DESDA). Only if the criteria of ss. 58(1) and (2) are met does the Appeal Division then grant leave to appeal.

[24] In Osaj v Canada (Attorney General), 2016 FC 115, the Court stated at paragraph 12 that having a reasonable chance of success in this context “means having some arguable ground upon which the proposed appeal might succeed.”

[25] The Appeal Division applied the correct test in refusing leave and reasonably found that the Applicant had failed to raise a ground of appeal that had a reasonable chance of success.

[26] The Appeal Division found that the General Division had considered the entirety of the medical evidence and had only emphasized Dr. Chan’s report, because it was consistent and in keeping with the other medical evidence. Further, in considering the appeal, it was not the role of the Appeal Division to assign weight to the evidence. (Simpson v Canada (Attorney General), 2012 FCA 82 at para 10)

[27] Mr. Parchment also seeks to rely on medical reports dated after the General Division hearing. However, it is only the medical evidence which was before the General Division which is relevant for consideration.

[28] Mr. Parchment has not identified a reviewable error upon which this Court is entitled to intervene. Therefore, this judicial review is dismissed without costs.


## 9903:3 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `87f9013ee3b3aa48e0427b617c88d4641cc35696c381120bfb5144dc1fa76a2e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9903:3:subtheme:1 · paragraphs 22-23

- Raw key terms: `application, attorney, awarded, canada, cause, costs, court, date`
- Display key terms: `awarded, costs, date`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: awarded, costs, date Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is dismissed. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4500499` offsets `244-253`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed. No costs are awarded.
"Ann Marie McDonald"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1219-16
STYLE OF CAUSE:
STERLING PARCHMENT v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
February 1, 2017


## 9903:4 · paragraphs 24-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `52a099fc2a46a64da79f00331167e21a517c26cd582dd7b2736673d94d846a67`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9903:4:subtheme:1 · paragraphs 24-24

- Raw key terms: `appearances, applicant, april, attorney, behalf, canada, dated, deputy`
- Display key terms: `april, behalf, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, behalf, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MCDONALD J.
DATED:
APRIL 10, 2017
APPEARANCES:
Sterling Parchment
For The Applicant
(ON HIS OWN BEHALF)
Sandra L. Doucette
For The Respondent
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
