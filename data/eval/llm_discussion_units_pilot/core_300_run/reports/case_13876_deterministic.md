# Discussion Units: case 13876

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **42**
- Continuity pairs: **41**
- Discussion Units: **4**
- Paragraph source hashes: **42**
- Sub-themes: **7**

## 13876:1 · paragraphs 0-1

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4a77e75a6cf19f32f1c3a32d771627b9cc0091935fc6dae78a50f6919ac5da83`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13876:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `application, reasons, appeal, applicant, attorney, british, canada, citation`
- Display key terms: `british, citation`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: british, citation Rule/authority context: Overview [1] This is an application for judicial review of a decision of the Social Security Tribunal – Appeal Division [SST-AD] granting leave to appeal pursuant to section 58 of the Department of Employment and Social  Operative outcome context: [2] For the reasons that follow, the application will be granted. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4682116` offsets `563-574`; context: Overview [1] This is an application for judicial review of a decision of the Social Security Tribunal – Appeal Division [SST-AD] granting leave to appeal pursuant to section 58 of the Department of Employment and Social Development Act, S.
- Evidence: `disposition` cue `granted` at chunk `4682117` offsets `57-64`; context: [2] For the reasons that follow, the application will be granted.

#### Section text

Canada (Attorney General) v. Hines
Court (s) Database
Federal Court Decisions
Date
2016-02-01
Neutral citation
2016 FC 112
File numbers
T-1223-15
Decision Content
Date: 20160201
Docket: T-1223-15
Citation: 2016 FC 112
Vancouver, British Columbia, February 1, 2016
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
ATTORNEY GENERAL OF CANADA
Applicant
and
MAUREEN B. HINES
Respondent
JUDGMENT AND REASONS
I. Overview [1] This is an application for judicial review of a decision of the Social Security Tribunal – Appeal Division [SST-AD] granting leave to appeal pursuant to section 58 of the Department of Employment and Social Development Act, S.C. 2005, c. 34 [DESDA].

[2] For the reasons that follow, the application will be granted.


## 13876:2 · paragraphs 2-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0424de2ced0ec885498e1c58670839ddfdc9b4a64fc7645c594bdb170deb0192`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13876:2:subtheme:1 · paragraphs 2-16

- Raw key terms: `respondent, appeal, decision, hines, application, esdc, reconsideration, sst-gd`
- Display key terms: `hines, esdc, reconsideration, sst-gd`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: hines, esdc, reconsideration, sst-gd Position/evidence statements: [17] First, the SST-AD found that her notice of appeal had been perfected when she submitted a copy of the reconsideration decision on August 15, 2014, which they determined was only five (5) days late. Rule/authority context: Background [3] On February 26, 2006, the Respondent applied for a retirement pension under the Canada Pension Plan, R. | The third application was the subject of the decision to grant leave to appeal which is under review. Application context: Background [3] On February 26, 2006, the Respondent applied for a retirement pension under the Canada Pension Plan, R. | The pension was terminated in 1998 because the Respondent informed CPP that she was seeking self-employment and, despite several requests, failed to complete the required disability reassessment questionnaire. Operative outcome context: It was denied because the Respondent did not meet the legislative requirements for the benefit as she was already in receipt of a CPP retirement pension. | On November 28, 2014, the Respondent filed submissions as to why she should be granted an extension. Evidence spans paragraphs 2-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4682117` offsets `155-160`; context: Background [3] On February 26, 2006, the Respondent applied for a retirement pension under the Canada Pension Plan, R.
- Evidence: `reasoning_application` cue `applied` at chunk `4682117` offsets `122-129`; context: Background [3] On February 26, 2006, the Respondent applied for a retirement pension under the Canada Pension Plan, R.
- Evidence: `evidence_fact` cue `record` at chunk `4682118` offsets `185-191`; context: The record also indicates that Ms.
- Evidence: `governing_rule` cue `under` at chunk `4682119` offsets `180-185`; context: The third application was the subject of the decision to grant leave to appeal which is under review.
- Evidence: `reasoning_application` cue `because` at chunk `4682119` offsets `294-301`; context: The pension was terminated in 1998 because the Respondent informed CPP that she was seeking self-employment and, despite several requests, failed to complete the required disability reassessment questionnaire.
- Evidence: `disposition` cue `denied` at chunk `4682119` offsets `527-533`; context: It was denied because the Respondent did not meet the legislative requirements for the benefit as she was already in receipt of a CPP retirement pension.
- Evidence: `counterargument_limitation` cue `however` at chunk `4682122` offsets `89-96`; context: [8] On July 7, 2014, the Respondent communicated her intent to appeal the ESDC decision; however, she failed to include all of the necessary information, specifically a copy of the ESDC’s reconsideration decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `4682123` offsets `285-288`; context: On July 14, 2014, the Respondent filed additional documents but again failed to include the ESDC decision.
- Evidence: `disposition` cue `granted` at chunk `4682125` offsets `273-280`; context: On November 28, 2014, the Respondent filed submissions as to why she should be granted an extension.
- Evidence: `reasoning_application` cue `because` at chunk `4682126` offsets `575-582`; context: Nevertheless, the SST-GD placed “extensive weight” on the lack of an arguable case: the Respondent’s appeal was bound to fail because she was 68 years old when she made her 2013 application.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4682126` offsets `449-461`; context: Nevertheless, the SST-GD placed “extensive weight” on the lack of an arguable case: the Respondent’s appeal was bound to fail because she was 68 years old when she made her 2013 application.
- Evidence: `reasoning_application` cue `apply` at chunk `4682128` offsets `564-569`; context: She also stated that “Perhaps ignorance (not knowing that it was an option) is not considered a case” and questioned: “Is there no concession for an individual that did not have the mental or physical capabilities in which it was critical to apply/appeal for these benefits.
- Evidence: `reasoning_application` cue `apply` at chunk `4682129` offsets `141-146`; context: Hines with the ESDC she states that the reason she did not apply for a CPP disability pension between the age of 60 and 65 was because she was not aware of the benefits or that applying was an option.
- Evidence: `disposition` cue `granted` at chunk `4682129` offsets `347-354`; context: Appeal Division Decision [16] On June 24, 2015, the SST-AD granted the Respondent leave to appeal.
- Evidence: `party_position` cue `submitted` at chunk `4682130` offsets `83-92`; context: [17] First, the SST-AD found that her notice of appeal had been perfected when she submitted a copy of the reconsideration decision on August 15, 2014, which they determined was only five (5) days late.
- Evidence: `evidence_fact` cue `found that` at chunk `4682130` offsets `23-33`; context: [17] First, the SST-AD found that her notice of appeal had been perfected when she submitted a copy of the reconsideration decision on August 15, 2014, which they determined was only five (5) days late.

#### 13876:2:subtheme:2 · paragraphs 17-18

- Raw key terms: `division, found, sst-ad, absolute, appeal, appears, appellant, applicable`
- Display key terms: `division, sst-ad, absolute, appears, appellant, applicable`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, sst-ad, absolute, appears, appellant, applicable Rule/authority context: [19] Third, the SST-AD found that while the Respondent had not raised any of the grounds for appeal under s 58 (1) of DESDA, the Appeal Division may “determine if there is an error of law, whether or not the error appear Application context: These provisions stipulate that the Minister of National Revenue may deem an application to have been made at an earlier date if an applicant can establish they were continuously incapable of forming or expressing an int Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4682132` offsets `189-196`; context: [19] Third, the SST-AD found that while the Respondent had not raised any of the grounds for appeal under s 58 (1) of DESDA, the Appeal Division may “determine if there is an error of law, whether or not the error appears on the face of the record.
- Evidence: `evidence_fact` cue `found that` at chunk `4682132` offsets `23-33`; context: [19] Third, the SST-AD found that while the Respondent had not raised any of the grounds for appeal under s 58 (1) of DESDA, the Appeal Division may “determine if there is an error of law, whether or not the error appears on the face of the record.
- Evidence: `governing_rule` cue `under` at chunk `4682132` offsets `100-105`; context: [19] Third, the SST-AD found that while the Respondent had not raised any of the grounds for appeal under s 58 (1) of DESDA, the Appeal Division may “determine if there is an error of law, whether or not the error appears on the face of the record.
- Evidence: `evidence_fact` cue `found that` at chunk `4682133` offsets `16-26`; context: [20] The SST-AD found that the General Division had regarded the Applicant’s age as an absolute bar to entitlement of CPP disability benefits without considering any applicable exceptions to this general rule.
- Evidence: `reasoning_application` cue `apply` at chunk `4682133` offsets `508-513`; context: These provisions stipulate that the Minister of National Revenue may deem an application to have been made at an earlier date if an applicant can establish they were continuously incapable of forming or expressing an intention to apply for a pension.

#### 13876:2:subtheme:3 · paragraphs 19-22

- Raw key terms: `deemed, demande, time, application, became, become, disability, disabled`
- Display key terms: `deemed, demande, time, became, become, disability, disabled`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: deemed, demande, time, became, become, disability, disabled Rule/authority context: (1) Sous réserve des autres dispositions de la présente partie : (a) a retirement pension shall be paid to a contributor who has reached sixty years of age; a) une pension de retraite doit être payée à un cotisant qui a  | 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt o Application context: 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt o Operative outcome context: ” This was the sole ground upon which the SST-AD granted leave. Evidence spans paragraphs 19-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4682134` offsets `446-453`; context: On that basis, the SST-AD found that: “while ultimately there may not have been sufficient or any evidence to support a finding of incapacity, there is an arguable case as to whether the General Division committed a palpable and overriding error if it failed to consider the incapacity provisions.
- Evidence: `evidence_fact` cue `found that` at chunk `4682134` offsets `297-307`; context: On that basis, the SST-AD found that: “while ultimately there may not have been sufficient or any evidence to support a finding of incapacity, there is an arguable case as to whether the General Division committed a palpable and overriding error if it failed to consider the incapacity provisions.
- Evidence: `disposition` cue `granted` at chunk `4682134` offsets `617-624`; context: ” This was the sole ground upon which the SST-AD granted leave.
- Evidence: `governing_rule` cue `under` at chunk `4682135` offsets `1637-1642`; context: (1) Sous réserve des autres dispositions de la présente partie :
(a) a retirement pension shall be paid to a contributor who has reached sixty years of age;
a) une pension de retraite doit être payée à un cotisant qui a atteint l’âge de soixante ans;
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom no retirement pension is payable, who is disabled and who
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) has made contributions for not less than the minimum qualifying period,
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.
- Evidence: `governing_rule` cue `under` at chunk `4682137` offsets `758-763`; context: 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt of a retirement pension and the applicant is deemed to have become disabled for the purposes of entitlement to the disability benefit in or after the month for which the retirement pension first became payable.
- Evidence: `reasoning_application` cue `apply` at chunk `4682137` offsets `630-635`; context: 1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt of a retirement pension and the applicant is deemed to have become disabled for the purposes of entitlement to the disability benefit in or after the month for which the retirement pension first became payable.

#### Section text

II. Background [3] On February 26, 2006, the Respondent applied for a retirement pension under the Canada Pension Plan, R.S.C., 1985, c. C-8 (CPP). Her application was approved, and she has received this pension since March 1, 2006.

[4] The Respondent was diagnosed with bilateral breast cancer in June 2008. She was treated surgically and with chemotherapy and hormone therapy, and had a high risk of recurrence. The record also indicates that Ms. Hines was diagnosed with a major depressive disorder sometime before March 2011. In March 2011, a qualified practitioner noted that she was having difficulty working, and unable to return to work due to her depressed mood, decreased motivation, impaired concentration and memory difficulties. In March 2014, another practitioner indicated that the Respondent had difficulty walking, getting up from a chair, and had difficulty with memory and organizing her thoughts.

[5] The Respondent has made three applications for CPP disability benefits in her lifetime. The third application was the subject of the decision to grant leave to appeal which is under review.
1) The first application was made June 2, 1992. It was approved. The pension was terminated in 1998 because the Respondent informed CPP that she was seeking self-employment and, despite several requests, failed to complete the required disability reassessment questionnaire.
2) The second application was made April 27, 2011. It was denied because the Respondent did not meet the legislative requirements for the benefit as she was already in receipt of a CPP retirement pension. The Respondent was informed by Service Canada that a CPP retirement pension can be cancelled in favour of a CPP disability benefit only it the applicant is deemed to have become disabled before the beginning of their retirement pension.
3) The third application was made June 10, 2013. It was denied by the Department of Employment and Social Development Canada (ESDC) because she did not satisfy the legislative requirement that a person must be between the ages of 18 and 65 to qualify for a CPP disability pension. Ms. Hines turned 65 on May 19, 2010.

[6] When completing the third application’s disability questionnaire, the Respondent indicated that she was suffering from post-chemotherapy cognitive impairment and had developed osteoporosis. Consequently she had trouble with mental focus and was unable to continue working as a bookkeeper. Ms. Hines also indicated that she worked in a part-time capacity as a food product demonstrator in a warehouse store from May 4, 2012 until January 8, 2013, was physically unable to continue that work, and that she had unsuccessfully attempted to find other employment.

[7] On June 24, 2013, the Respondent sought reconsideration of her third application. The ESDC maintained its decision. The Respondent was informed in a letter dated May 2, 2014, that she could file a notice of appeal with the General Division of the Social Security Tribunal [SST-GD] within 90 days of the date she received the reconsideration decision. She was also informed what documentation and information were required to complete the notice.

[8] On July 7, 2014, the Respondent communicated her intent to appeal the ESDC decision; however, she failed to include all of the necessary information, specifically a copy of the ESDC’s reconsideration decision.

[9] On July 11, 2014, the Respondent was advised by the SST-GD that her notice of appeal was incomplete, and she was reminded that a completed notice must be received within 90 days of receiving the reconsideration decision. On July 14, 2014, the Respondent filed additional documents but again failed to include the ESDC decision. On August 11, 2014, the SST-GD sent a second letter to the Respondent reminding her that her notice of appeal was incomplete and what was required.

[10] On August 15, 2014, the Respondent filed a copy of the reconsideration decision.

[11] On November 14, 2014, the SST-GD advised the Respondent that her notice of appeal appeared to be late, that she could request an extension of time for filing, and how to go about doing so. On November 28, 2014, the Respondent filed submissions as to why she should be granted an extension.

[12] On April 21, 2015, the SST-GD issued its decision refusing to grant an extension of time on the basis that there was no arguable case. It concluded that the appeal was not perfected until November 28, 2014. The SST-GD was satisfied that she had a continual intention to appeal, that there was a reasonable explanation for the delay (she “simply did not understand how to do so”), and that there would be no prejudice in allowing the extension. Nevertheless, the SST-GD placed “extensive weight” on the lack of an arguable case: the Respondent’s appeal was bound to fail because she was 68 years old when she made her 2013 application.

[13] On May 8, 2015, the Respondent sought leave to appeal the SST-GD’s decision denying an extension. Ms. Hines’ letter of appeal did not allege any errors in the SST-GD’s decision or raise any of the grounds for appeal set out in s 58 (1) of DESDA.

[14] In her letter of appeal, Ms. Hines stated that she found out about CPP disability from her doctor in May 2011. The Respondent noted that she has been diagnosed with post-chemotherapy cognitive impairment which affects her ability to understand and make decisions and that she was suffering from long-term depression. She also stated that “Perhaps ignorance (not knowing that it was an option) is not considered a case” and questioned: “Is there no concession for an individual that did not have the mental or physical capabilities in which it was critical to apply/appeal for these benefits.”

[15] It is also noteworthy that in many of the letters and documents filed by Ms. Hines with the ESDC she states that the reason she did not apply for a CPP disability pension between the age of 60 and 65 was because she was not aware of the benefits or that applying was an option.
III. Appeal Division Decision [16] On June 24, 2015, the SST-AD granted the Respondent leave to appeal.

[17] First, the SST-AD found that her notice of appeal had been perfected when she submitted a copy of the reconsideration decision on August 15, 2014, which they determined was only five (5) days late.

[18] Second, the SST-AD calculated that the minimum qualifying period when the Respondent would have had to be found disabled was on or before December 31, 2005. The reasoning behind this calculation was not explained.

[19] Third, the SST-AD found that while the Respondent had not raised any of the grounds for appeal under s 58 (1) of DESDA, the Appeal Division may “determine if there is an error of law, whether or not the error appears on the face of the record.” It was then noted that a decision to grant an extension is discretionary and to overturn a discretionary order an appellant must prove the decision-maker committed a palpable and overriding error of law. The SST-AD relied on Decor Grates Inc v Imperial Manufacturing Group Inc, 2015 FCA 100, para 23, to support this assertion.

[20] The SST-AD found that the General Division had regarded the Applicant’s age as an absolute bar to entitlement of CPP disability benefits without considering any applicable exceptions to this general rule. One possible exception is found in s 60 (8) – s 60 (11) of the CPP. These provisions stipulate that the Minister of National Revenue may deem an application to have been made at an earlier date if an applicant can establish they were continuously incapable of forming or expressing an intention to apply for a pension.

[21] The SST-AD noted that if Ms. Hines was continuously incapable of forming or expressing an intention to make an application for benefits from the time she became incapacitated until the date of her 2013 application she might yet qualify for a CPP disability pension. On that basis, the SST-AD found that: “while ultimately there may not have been sufficient or any evidence to support a finding of incapacity, there is an arguable case as to whether the General Division committed a palpable and overriding error if it failed to consider the incapacity provisions.” This was the sole ground upon which the SST-AD granted leave.
IV. Relevant Legislation [22] The grounds for appeal to the SST-AD are set out in DESDA as follows:
Grounds of appeal
Moyens d’appel
58. (1) The only grounds of appeal are that
58. (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
Criteria
Critère
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.
…
…
Leave granted
Permission accordée
(5) If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed.
(5) Dans les cas où la permission est accordée, la demande de permission est assimilée à un avis d’appel et celui-ci est réputé avoir été déposé à la date du dépôt de la demande de permission.

[23] Subsection 44 (1) of the CPP sets out the eligibility requirements for CPP pensions:
Benefits payable
Prestations payables
44. (1) Subject to this Part,
44. (1) Sous réserve des autres dispositions de la présente partie :
(a) a retirement pension shall be paid to a contributor who has reached sixty years of age;
a) une pension de retraite doit être payée à un cotisant qui a atteint l’âge de soixante ans;
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom no retirement pension is payable, who is disabled and who
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) has made contributions for not less than the minimum qualifying period,
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.1 had not been made;
(iii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si un partage des gains non ajustés ouvrant droit à pension n’avait pas été effectué en application des articles 55 et 55.1;

[24] The time period within which a person may be deemed disabled is defined in the CPP as follows:
When person deemed disabled
Personne déclarée invalide
42 (2) For the purposes of this Act,
(2) Pour l’application de la présente loi :
(b) a person is deemed to have become or to have ceased to be disabled at the time that is determined in the prescribed manner to be the time when the person became or ceased to be, as the case may be, disabled, but in no case shall a person — including a contributor referred to in subparagraph 44(1)(b)(ii) — be deemed to have become disabled earlier than fifteen months before the time of the making of any application in respect of which the determination is made.
b) une personne est réputée être devenue ou avoir cessé d’être invalide à la date qui est déterminée, de la manière prescrite, être celle où elle est devenue ou a cessé d’être, selon le cas, invalide, mais en aucun cas une personne — notamment le cotisant visé au sous-alinéa 44(1)b)(ii) — n’est réputée être devenue invalide à une date antérieure de plus de quinze mois à la date de la présentation d’une demande à l’égard de laquelle la détermination a été faite.

[25] The provision addressing the cancellation of a retirement pension in favour of a disability pension is set out in the CPP as follows:
Request to cancel benefit
Demande de cessation de prestation
66.1 (1) A beneficiary may, in prescribed manner and within the prescribed time interval after payment of a benefit has commenced, request cancellation of that benefit.
66.1 (1) Un bénéficiaire peut demander la cessation d’une prestation s’il le fait de la manière prescrite et, après que le paiement de la prestation a commencé, durant la période de temps prescrite à cet égard.
Exception
Exception
(1.1) Subsection (1) does not apply to the cancellation of a retirement pension in favour of a disability benefit where an applicant for a disability benefit under this Act or under a provincial pension plan is in receipt of a retirement pension and the applicant is deemed to have become disabled for the purposes of entitlement to the disability benefit in or after the month for which the retirement pension first became payable.
(1.1) Toutefois, le bénéficiaire d’une prestation de retraite ne peut remplacer cette prestation par une prestation d’invalidité si le requérant est réputé être devenu invalide, en vertu de la présente loi ou aux termes d’un régime provincial de pensions, au cours du mois où il a commencé à toucher sa prestation de retraite ou par la suite.

## 13876:3 · paragraphs 23-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c5ce0315b43fd900af508ce4c144999679cce25fbe0d69f606868551f9471c14`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13876:3:subtheme:1 · paragraphs 23-33

- Raw key terms: `hines, application, disability, pension, accordance, applicant, attorney, benefit`
- Display key terms: `hines, disability, pension, accordance, benefit`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: hines, disability, pension, accordance, benefit Position/evidence statements: Applicant’s position [29] The Applicant argues that the SST-AD’s decision was unreasonable for two reasons: the SST-GD did not err in finding that there was no arguable case, and the SST-GD did not err by failing to cons | [36] The Applicant asserts that s 60 of the CPP must be interpreted narrowly “it does not require consideration of the capacity to make, prepare, process or complete an application for disability benefits, but only the c Rule/authority context: Standard of Review [28] The applicable standard of review of the SST-AD’s decision is reasonableness. | 1 of the CPP, a retirement pension may only be cancelled if a pensioner under the age of 65 becomes disabled within one month of their retirement pension becoming payable. Application context: Application Application (11) Subsections (8) to (10) apply only to individuals who were incapacitated on or after January 1, 1991. | The Respondent does not qualify for a CPP disability pension because she was already in receipt of a CPP retirement pension when she made her 2013 application. Evidence spans paragraphs 23-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4682138` offsets `3972-3978`; context: Issues [27] The sole issue in this appeal is the reasonableness of SST-AD’s decision to grant leave to appeal.
- Evidence: `party_position` cue `argues` at chunk `4682138` offsets `4388-4394`; context: Applicant’s position [29] The Applicant argues that the SST-AD’s decision was unreasonable for two reasons: the SST-GD did not err in finding that there was no arguable case, and the SST-GD did not err by failing to consider incapacity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682138` offsets `213-221`; context: [26] The provisions of the CPP dealing with incapacity read as follows:
Incapacity
Incapacité
60 (8) Where an application for a benefit is made on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that the person had been incapable of forming or expressing an intention to make an application on the person’s own behalf on the day on which the application was actually made, the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person’s last relevant period of incapacity to have commenced, whichever is the later.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4682138` offsets `4087-4105`; context: Standard of Review [28] The applicable standard of review of the SST-AD’s decision is reasonableness.
- Evidence: `reasoning_application` cue `apply` at chunk `4682138` offsets `3732-3737`; context: Application
Application
(11) Subsections (8) to (10) apply only to individuals who were incapacitated on or after January 1, 1991.
- Evidence: `reasoning_application` cue `because` at chunk `4682139` offsets `212-219`; context: The Respondent does not qualify for a CPP disability pension because she was already in receipt of a CPP retirement pension when she made her 2013 application.
- Evidence: `governing_rule` cue `under` at chunk `4682140` offsets `101-106`; context: 1 of the CPP, a retirement pension may only be cancelled if a pensioner under the age of 65 becomes disabled within one month of their retirement pension becoming payable.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4682140` offsets `201-212`; context: Accordingly, Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682142` offsets `335-343`; context: (2) The SST-GD did not err by failing to consider incapacity [35] The Attorney General submits that there is no obligation to consider incapacity when there is no evidence to support a conclusion that a claimant’s condition meets the definition.
- Evidence: `party_position` cue `asserts` at chunk `4682143` offsets `19-26`; context: [36] The Applicant asserts that s 60 of the CPP must be interpreted narrowly “it does not require consideration of the capacity to make, prepare, process or complete an application for disability benefits, but only the capacity, quite simply, of ‘forming or expressing an intention to make an application’”: Attorney General of Canada v.
- Evidence: `governing_rule` cue `under` at chunk `4682143` offsets `545-550`; context: The Attorney General also argues that a lack of knowledge of an entitlement to a benefit does not constitute incapacity to form or express an intention to make an application under the CPP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682144` offsets `22-30`; context: [37] Furthermore, the evidence before the SST-GD precludes a finding that the Respondent was continuously incapable of forming or expressing an intention to apply for a benefit.
- Evidence: `reasoning_application` cue `apply` at chunk `4682144` offsets `157-162`; context: [37] Furthermore, the evidence before the SST-GD precludes a finding that the Respondent was continuously incapable of forming or expressing an intention to apply for a benefit.
- Evidence: `party_position` cue `submits` at chunk `4682145` offsets `19-26`; context: [38] The Applicant submits that the record establishes that between 2006 and 2013 Ms.
- Evidence: `evidence_fact` cue `record` at chunk `4682145` offsets `36-42`; context: [38] The Applicant submits that the record establishes that between 2006 and 2013 Ms.
- Evidence: `reasoning_application` cue `apply` at chunk `4682145` offsets `143-148`; context: Hines had the capacity to form and express the intent to apply for a benefit.
- Evidence: `party_position` cue `submitted` at chunk `4682148` offsets `525-534`; context: An excerpt from the on-line website Wikipedia she submitted in support of her application describes this as “post-chemo positive impairment”.

#### 13876:3:subtheme:2 · paragraphs 34-40

- Raw key terms: `appeal, hines, record, disability, evidence, finding, application, capacity`
- Display key terms: `hines, disability, finding, capacity`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: hines, disability, finding, capacity Application context: Hines simply did not know that she could apply for a CPP disability pension when she remained eligible to do so. Operative outcome context: [48] On a plain reading of the decision, the Member granted leave on a purely theoretical basis unsupported by the record as to the sole possible ground of appeal. | [49] In the result, the application for judicial review will be allowed, the SST-AD decision will be set aside, and the matter referred back to another member of the Appeal Division for redetermination in accordance with Evidence spans paragraphs 34-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4682149` offsets `582-587`; context: Hines did not raise the issue of incapacity, and the evidence does not support a finding that she was continuously incapable of forming or expressing an intention to apply for a benefit at any time after her illness was acute.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682149` offsets `54-62`; context: Hines was unable to point to any evidence in the record that would support a finding that she was continuously impaired at the relevant times within the meaning of the statute.
- Evidence: `reasoning_application` cue `apply` at chunk `4682149` offsets `281-286`; context: Hines simply did not know that she could apply for a CPP disability pension when she remained eligible to do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682150` offsets `442-450`; context: There was no evidence in the appeal record to support that finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682151` offsets `215-223`; context: The Member made no finding that there was evidence of incapacity in the record that would support an exception to the statutory age limitation but invited the parties to make submissions on that point.
- Evidence: `counterargument_limitation` cue `but` at chunk `4682151` offsets `316-319`; context: The Member made no finding that there was evidence of incapacity in the record that would support an exception to the statutory age limitation but invited the parties to make submissions on that point.
- Evidence: `evidence_fact` cue `evidence` at chunk `4682152` offsets `238-246`; context: It must be determined on the basis of the medical evidence and the individual’s activities.
- Evidence: `evidence_fact` cue `record` at chunk `4682153` offsets `115-121`; context: [48] On a plain reading of the decision, the Member granted leave on a purely theoretical basis unsupported by the record as to the sole possible ground of appeal.
- Evidence: `counterargument_limitation` cue `but` at chunk `4682153` offsets `271-274`; context: The factors considered would militate in favour of a disability finding, had the respondent been eligible, but not a capacity finding.
- Evidence: `disposition` cue `granted` at chunk `4682153` offsets `52-59`; context: [48] On a plain reading of the decision, the Member granted leave on a purely theoretical basis unsupported by the record as to the sole possible ground of appeal.
- Evidence: `disposition` cue `allowed` at chunk `4682154` offsets `64-71`; context: [49] In the result, the application for judicial review will be allowed, the SST-AD decision will be set aside, and the matter referred back to another member of the Appeal Division for redetermination in accordance with these reasons.

#### Section text

[26] The provisions of the CPP dealing with incapacity read as follows:
Incapacity
Incapacité
60 (8) Where an application for a benefit is made on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that the person had been incapable of forming or expressing an intention to make an application on the person’s own behalf on the day on which the application was actually made, the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person’s last relevant period of incapacity to have commenced, whichever is the later.
(8) Dans le cas où il est convaincu, sur preuve présentée par le demandeur ou en son nom, que celui-ci n’avait pas la capacité de former ou d’exprimer l’intention de faire une demande le jour où celle-ci a été faite, le ministre peut réputer cette demande de prestation avoir été faite le mois qui précède celui au cours duquel la prestation aurait pu commencer à être payable ou, s’il est postérieur, le mois au cours duquel, selon le ministre, la dernière période pertinente d’incapacité du demandeur a commencé.
(9) Where an application for a benefit is made by or on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that
(9) Le ministre peut réputer une demande de prestation avoir été faite le mois qui précède le premier mois au cours duquel une prestation aurait pu commencer à être payable ou, s’il est postérieur, le mois au cours duquel, selon lui, la dernière période pertinente d’incapacité du demandeur a commencé, s’il est convaincu, sur preuve présentée par le demandeur :
(a) the person had been incapable of forming or expressing an intention to make an application before the day on which the application was actually made,
a) que le demandeur n’avait pas la capacité de former ou d’exprimer l’intention de faire une demande avant la date à laquelle celle-ci a réellement été faite;
(b) the person had ceased to be so incapable before that day, and
b) que la période d’incapacité du demandeur a cessé avant cette date;
c) the application was made
c) que la demande a été faite, selon le cas :
(i) within the period that begins on the day on which that person had ceased to be so incapable and that comprises the same number of days, not exceeding twelve months, as in the period of incapacity, or
(i) au cours de la période — égale au nombre de jours de la période d’incapacité mais ne pouvant dépasser douze mois — débutant à la date où la période d’incapacité du demandeur a cessé,
(ii) where the period referred to in subparagraph (i) comprises fewer than thirty days, not more than one month after the month in which that person had ceased to be so incapable,
(ii) si la période décrite au sous-alinéa (i) est inférieure à trente jours, au cours du mois qui suit celui au cours duquel la période d’incapacité du demandeur a cessé.
the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person’s last relevant period of incapacity to have commenced, whichever is the later.
[blank] [en blanc]
Period of incapacity
Période d’incapacité
(10) For the purposes of subsections (8) and (9), a period of incapacity must be a continuous period except as otherwise prescribed.
(10) Pour l’application des paragraphes (8) et (9), une période d’incapacité doit être continue à moins qu’il n’en soit prescrit autrement.
Application
Application
(11) Subsections (8) to (10) apply only to individuals who were incapacitated on or after January 1, 1991.
(11) Les paragraphes (8) à (10) ne s’appliquent qu’aux personnes incapables le 1er janvier 1991 dont la période d’incapacité commence à compter de cette date.
V. Issues [27] The sole issue in this appeal is the reasonableness of SST-AD’s decision to grant leave to appeal.
VI. Standard of Review [28] The applicable standard of review of the SST-AD’s decision is reasonableness. I agree with and adopt the analysis of Madame Justice Roussel in Tracey v Canada (Attorney General), 2015 FC 1300, para 17.
VII. Submissions of the Parties A. Applicant’s position [29] The Applicant argues that the SST-AD’s decision was unreasonable for two reasons: the SST-GD did not err in finding that there was no arguable case, and the SST-GD did not err by failing to consider incapacity.
(1) The SST-GD did not err in finding that there was no arguable case. [30] In accordance with s 44 (1) (b) of the CPP, an applicant must be under the age of 65 to qualify for disability. The Respondent does not qualify for a CPP disability pension because she was 68 years old when she made her 2013 application.

[31] In accordance with s 44(1) (b) of the CPP, a person is ineligible to receive a disability pension if they are in receipt of a retirement pension. The Respondent does not qualify for a CPP disability pension because she was already in receipt of a CPP retirement pension when she made her 2013 application.

[32] In accordance with s 66.1 of the CPP, a retirement pension may only be cancelled if a pensioner under the age of 65 becomes disabled within one month of their retirement pension becoming payable. Accordingly, Ms. Hines would have to have become disabled no later than April 2006.

[33] In accordance with s 42(2) (b) of the CPP, no person can be deemed to have become disabled earlier than 15 months before their application is made. Consequently, the earliest date Ms. Hines can be deemed to have become disabled is March 2012.

[34] When s 66.1 and s 42(2) (b) are read together it is impossible for Ms. Hines to have her retirement pension cancelled on the basis of her 2013 disability application.
(2) The SST-GD did not err by failing to consider incapacity [35] The Attorney General submits that there is no obligation to consider incapacity when there is no evidence to support a conclusion that a claimant’s condition meets the definition.

[36] The Applicant asserts that s 60 of the CPP must be interpreted narrowly “it does not require consideration of the capacity to make, prepare, process or complete an application for disability benefits, but only the capacity, quite simply, of ‘forming or expressing an intention to make an application’”: Attorney General of Canada v. Danielson, 2008 FCA 78, para 5. The Attorney General also argues that a lack of knowledge of an entitlement to a benefit does not constitute incapacity to form or express an intention to make an application under the CPP.

[37] Furthermore, the evidence before the SST-GD precludes a finding that the Respondent was continuously incapable of forming or expressing an intention to apply for a benefit. As noted by Justice Létourneau in Canada (Attorney General) v Kirkland, 2008 FCA 144, at para 7: “activities of a claimant during an alleged period of incapacity ‘may be relevant to cast light on his or her continuous incapacity to form or express the requisite intention and ought to be considered’”. Citing Danielson (above), Justice Létourneau also noted that the "capacity to form the intention to apply for benefits is not different in kind from the capacity to form an intention with respect to other choices which present themselves to an applicant.” (See also Ramlochan v AG (Canada), T-148-13, paras 34-35).

[38] The Applicant submits that the record establishes that between 2006 and 2013 Ms. Hines had the capacity to form and express the intent to apply for a benefit. They point to the fact that the Respondent cared for her mother from 2005-2007; applied for employment insurance sickness benefits in 2008; applied on her own behalf for a disability pension in April 2011, and worked part-time for eight (8) months as a warehouse demonstrator in 2013.
B. Respondent’s position [39] The Respondent represented herself in these proceedings. She filed no written materials in advance of the hearing.

[40] Shortly before the scheduled hearing, Ms. Hines wrote to the Court to ask that arrangements be made to permit her to appear by telephone. In her letter, she set out a number of reasons why it would be impractical if not impossible for her to appear in person given her physical limitations and constrained financial circumstances. She did not request an adjournment and did not suggest that her circumstances would improve at any foreseeable time so as to permit her to appear in person for the hearing if it was rescheduled. As a result, the Court issued a direction permitting her to appear by telephone to make her oral representations from her home.

[41] At the scheduled hearing, Ms. Hines appeared by telephone. In response to questions from the Court, she indicated that she was able to hear the proceedings clearly and understood the nature of the process. The Court had no difficulty hearing or understanding Ms. Hines as she spoke in a clear and articulate manner and responded appropriately to the questions posed to her.

[42] In her oral representations, Ms. Hines explained that she had suffered serious injuries as a result of a motor vehicle accident in 1989. She was on long-term disability in the 1990s and had thereafter returned to work as a bookkeeper. She suffered from depression and was coping with raising two children as a single parent and her mother’s terminal illness. Following the cancer diagnosis, surgery and chemotherapy, she experienced what she described as “chemo brain”. An excerpt from the on-line website Wikipedia she submitted in support of her application describes this as “post-chemo positive impairment”. She could not continue as a bookkeeper and took a job as a food demonstrator. Her Doctor recommended that she leave that position, and she has been unable to obtain or function in a job since 2012.

[43] When asked, Ms. Hines was unable to point to any evidence in the record that would support a finding that she was continuously impaired at the relevant times within the meaning of the statute. Rather, as she candidly acknowledged, Ms. Hines simply did not know that she could apply for a CPP disability pension when she remained eligible to do so.
VIII. Analysis [44] While Ms. Hines’ situation is very unfortunate, I agree with the Applicant that the SST-AD’s decision is unreasonable and must be set aside. In her application for leave to appeal, Ms. Hines did not raise the issue of incapacity, and the evidence does not support a finding that she was continuously incapable of forming or expressing an intention to apply for a benefit at any time after her illness was acute. Where there is no evidence, a tribunal need not consider every possible exception or ground for relief.

[45] The SST-GD did not err in finding Ms. Hines ineligible for a CPP disability pension. They were correct in finding that Ms. Hines did not meet the statutory requirements for the benefit as she was over the age of 65 and already in receipt of a CPP retirement pension. The only possible ground to support an appeal was that she lacked the capacity to form and express an intention to make an application at the relevant time. There was no evidence in the appeal record to support that finding.

[46] The Appeal Division’s reasons for granting leave to appeal lack the transparency, intelligibility and justification required to satisfy the standard of reasonableness. The Member made no finding that there was evidence of incapacity in the record that would support an exception to the statutory age limitation but invited the parties to make submissions on that point.

[47] The Federal Court of Appeal has affirmed that capacity is to be considered in light of the ordinary meaning of the term: Sedrak v Canada (Social Development), 2008 FCA 86, paras 3-4. It must be determined on the basis of the medical evidence and the individual’s activities. Unfortunately for Ms. Hines, a lack of knowledge about entitlement to a disability pension does not fall within the scope of incapacity.

[48] On a plain reading of the decision, the Member granted leave on a purely theoretical basis unsupported by the record as to the sole possible ground of appeal. The factors considered would militate in favour of a disability finding, had the respondent been eligible, but not a capacity finding. While the circumstances experienced by Ms. Hines call for sympathy, they did not establish a lack of capacity at the relevant time.

[49] In the result, the application for judicial review will be allowed, the SST-AD decision will be set aside, and the matter referred back to another member of the Appeal Division for redetermination in accordance with these reasons.
JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is allowed, the decision of the SST-AD is set aside, and this matter is referred back for redetermination by another member of the SST-AD in accordance with these reasons.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1223-15
STYLE OF CAUSE:
ATTORNEY GENERAL OF CANADA v MAUREEN B. HINES
PLACE OF HEARING:
Vancouver, British Columbia
DATE OF HEARING:
January 25, 2016


## 13876:4 · paragraphs 41-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e30a776ffe739a06e85b78910c1be9444d4558c5e347bdf7ccba0f25c773c269`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13876:4:subtheme:1 · paragraphs 41-41

- Raw key terms: `appearances, applicant, attorney, behalf, british, canada, columbia, dated`
- Display key terms: `behalf, british, columbia, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, british, columbia, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MOSLEY J.
DATED:
FEBRUARY 1, 2016
APPEARANCES:
Vanessa Luna
For The Applicant
Maureen B. Hines
THE RESPONDENT on her own behalf
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Vancouver, British Columbia
For The Applicant
