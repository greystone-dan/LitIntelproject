# Discussion Units: case 10200

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **19**
- Continuity pairs: **18**
- Discussion Units: **5**
- Paragraph source hashes: **19**
- Sub-themes: **9**

## 10200:1 · paragraphs 0-1

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `235807ec05dac6527b2e4e126ea7b4f013496e2cae2c95e6249f2fd8dce2b340`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10200:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `appeal, application, division, ingram, judicial, leave, reasons, review`
- Display key terms: `division, ingram, judicial, leave, review`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: division, ingram, judicial, leave, review Rule/authority context: Introduction [1] Carol Ingram has brought an application for judicial review under s 18. Application context: The application for judicial review is therefore allowed. Operative outcome context: The Appeal Division denied her application for leave to appeal a decision of the Tribunal’s General Division. | The application for judicial review is therefore allowed. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4513064` offsets `476-481`; context: Introduction [1] Carol Ingram has brought an application for judicial review under s 18.
- Evidence: `disposition` cue `denied` at chunk `4513064` offsets `642-648`; context: The Appeal Division denied her application for leave to appeal a decision of the Tribunal’s General Division.
- Evidence: `reasoning_application` cue `therefore` at chunk `4513065` offsets `194-203`; context: The application for judicial review is therefore allowed.
- Evidence: `disposition` cue `allowed` at chunk `4513065` offsets `204-211`; context: The application for judicial review is therefore allowed.

#### Section text

Ingram v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-03-06
Neutral citation
2017 FC 259
File numbers
T-1157-16
Decision Content
Date: 20170306
Docket: T-1157-16
Citation: 2017 FC 259
Ottawa, Ontario, March 6, 2017
PRESENT: The Honourable Mr. Justice Fothergill
BETWEEN:
CAROL INGRAM
Applicant
and
THE ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Introduction [1] Carol Ingram has brought an application for judicial review under s 18.1 of the Federal Courts Act, RSC 1985, c F-7 of a decision of the Appeal Division of the Social Security Tribunal dated June 13, 2016. The Appeal Division denied her application for leave to appeal a decision of the Tribunal’s General Division. The General Division denied Ms. Ingram’s application for a disability pension under the Canada Pension Plan [CPP].

[2] For the reasons that follow, I have concluded that the Appeal’s Division’s dismissal of Ms. Ingram’s application for leave to appeal was unreasonable. The application for judicial review is therefore allowed.


## 10200:2 · paragraphs 2-4

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c00318463dbbae37f9c3aa76532c3995aab41f9105ee3c29f142e7aea0f0db40`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10200:2:subtheme:1 · paragraphs 2-3

- Raw key terms: `december, division, general, ingram, account, appeal, appealed, application`
- Display key terms: `december, division, ingram, account, appealed`
- Argument roles: `disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, reasoning_application Display terms: december, division, ingram, account, appealed Application context: Ingram applied for a disability pension in January 2012. Operative outcome context: The application was denied on July 19, 2012. Evidence spans paragraphs 2-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4513065` offsets `243-250`; context: Ingram applied for a disability pension in January 2012.
- Evidence: `disposition` cue `denied` at chunk `4513065` offsets `313-319`; context: The application was denied on July 19, 2012.
- Evidence: `evidence_fact` cue `found that` at chunk `4513066` offsets `25-35`; context: [4] The General Division found that the date for Ms.

#### 10200:2:subtheme:2 · paragraphs 4-4

- Raw key terms: `advice, advised, assessed, attempt, back-to-work, conditions, continued, contributory`
- Display key terms: `advice, advised, assessed, attempt, back-to-work, conditions, continued, contributory`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: advice, advised, assessed, attempt, back-to-work, conditions, continued, contributory Rule/authority context: However, the General Division continued: Her return to work was a result of determined perseverance, medical treatment and mitigation strategies, under painful conditions. Application context: The Tribunal therefore must decide if this unusually long period of a “back-to-work attempt” was successful and whether or not the earnings of 2012 through 2014 were gainful. Evidence spans paragraphs 4-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4513067` offsets `771-778`; context: The Tribunal therefore must decide if this unusually long period of a “back-to-work attempt” was successful and whether or not the earnings of 2012 through 2014 were gainful.
- Evidence: `evidence_fact` cue `found that` at chunk `4513067` offsets `25-35`; context: [5] The General Division found that, if Ms.
- Evidence: `governing_rule` cue `under` at chunk `4513067` offsets `378-383`; context: However, the General Division continued:
Her return to work was a result of determined perseverance, medical treatment and mitigation strategies, under painful conditions.
- Evidence: `reasoning_application` cue `therefore` at chunk `4513067` offsets `672-681`; context: The Tribunal therefore must decide if this unusually long period of a “back-to-work attempt” was successful and whether or not the earnings of 2012 through 2014 were gainful.
- Evidence: `counterargument_limitation` cue `However` at chunk `4513067` offsets `232-239`; context: However, the General Division continued:
Her return to work was a result of determined perseverance, medical treatment and mitigation strategies, under painful conditions.

#### Section text

II. Background [3] Ms. Ingram applied for a disability pension in January 2012. The application was denied on July 19, 2012. Her application for reconsideration was denied on December 6, 2012. She appealed to the General Division of the Social Security Tribunal. Her appeal was heard by the General Division on September 8, 2015, and dismissed on October 29, 2015.

[4] The General Division found that the date for Ms. Ingram’s minimum qualifying period [MQP] was December 31, 2011. After the hearing, the General Division asked Ms. Ingram to provide an updated Record of Earnings, together with any submissions she wished to make. The information she provided confirmed that Ms. Ingram had earnings and CPP contributions for the years 2013 and 2014, but no earnings in the years 2010, 2011 or 2012. The General Division maintained the initial MQP, but noted that two years of valid earnings would now have to be taken into account.

[5] The General Division found that, if Ms. Ingram had been assessed as of the date of her MQP, there would be “little doubt” that she had a severe disability in 2008, and that she met the requirements for contributory eligibility. However, the General Division continued:
Her return to work was a result of determined perseverance, medical treatment and mitigation strategies, under painful conditions. She “needed the money” and was prepared to ignore and “work through” her pain and the advice of her family doctor who advised her to not work, steel herself up and punish herself with the pain she had described as the recovery reward for her persistence. The Tribunal therefore must decide if this unusually long period of a “back-to-work attempt” was successful and whether or not the earnings of 2012 through 2014 were gainful.

## 10200:3 · paragraphs 5-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `db8d2e3664ef8defa7b1c39735e50b7b1abc918a339736d21df062a20ce99792`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10200:3:subtheme:1 · paragraphs 5-7

- Raw key terms: `case, demonstrated, gainful, general, work, accordingly, actually, advantage`
- Display key terms: `case, demonstrated, gainful, work, accordingly, actually, advantage`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: case, demonstrated, gainful, work, accordingly, actually, advantage Application context: Accordingly, the Tribunal cannot find that her medical conditions amount to a level of severity that meet the CPP disability test. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4513070` offsets `112-120`; context: [54] To establish severe disability, Appellants must not only show a serious health problem, but where there is evidence of work capacity after the MQP, (which the Tribunal finds in this case), must also show an effort at obtaining and maintaining employment has been unsuccessful by reason of the health condition.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4513070` offsets `453-464`; context: Accordingly, the Tribunal cannot find that her medical conditions amount to a level of severity that meet the CPP disability test.

#### 10200:3:subtheme:2 · paragraphs 8-9

- Raw key terms: `applicant, attorney, canada, considered, disability, gainful, general, para`
- Display key terms: `considered, disability, gainful, para`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: considered, disability, gainful, para Rule/authority context: Decision under Review [8] The Appeal Division denied Ms. | [11] Pursuant to s 44(1)(b) of the Canada Pension Plan, RSC 1985, c C-8, a disability pension is paid to a disabled person who (i) is under sixty-five years of age; (ii) does not receive a retirement pension; and (iii) h Application context: [7] The General Division found that the test for severity had not been met, and it was therefore unnecessary to consider whether the disability was also prolonged. | Prior to reforms that were introduced in 2014, the test consistently applied was whether an applicant had “any disability which renders an applicant incapable of pursuing with consistent frequency any truly remunerative  Operative outcome context: The General Division dismissed the appeal, and Ms. Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4513071` offsets `121-128`; context: [7] The General Division found that the test for severity had not been met, and it was therefore unnecessary to consider whether the disability was also prolonged.
- Evidence: `evidence_fact` cue `found that` at chunk `4513071` offsets `25-35`; context: [7] The General Division found that the test for severity had not been met, and it was therefore unnecessary to consider whether the disability was also prolonged.
- Evidence: `governing_rule` cue `under` at chunk `4513071` offsets `299-304`; context: Decision under Review [8] The Appeal Division denied Ms.
- Evidence: `reasoning_application` cue `therefore` at chunk `4513071` offsets `87-96`; context: [7] The General Division found that the test for severity had not been met, and it was therefore unnecessary to consider whether the disability was also prolonged.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4513071` offsets `687-699`; context: Nevertheless, the Appeal Division was satisfied that the General Division had turned its mind to other factors.
- Evidence: `disposition` cue `dismissed` at chunk `4513071` offsets `185-194`; context: The General Division dismissed the appeal, and Ms.
- Evidence: `issue` cue `whether` at chunk `4513072` offsets `634-641`; context: Prior to reforms that were introduced in 2014, the test consistently applied was whether an applicant had “any disability which renders an applicant incapable of pursuing with consistent frequency any truly remunerative occupation” in a “real world” context (Villani v Canada (Attorney General), 2001 FCA 248 at para 38).
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4513072` offsets `5-16`; context: [11] Pursuant to s 44(1)(b) of the Canada Pension Plan, RSC 1985, c C-8, a disability pension is paid to a disabled person who (i) is under sixty-five years of age; (ii) does not receive a retirement pension; and (iii) has made valid contributions to the CPP for at least the MQP.
- Evidence: `reasoning_application` cue `applied` at chunk `4513072` offsets `622-629`; context: Prior to reforms that were introduced in 2014, the test consistently applied was whether an applicant had “any disability which renders an applicant incapable of pursuing with consistent frequency any truly remunerative occupation” in a “real world” context (Villani v Canada (Attorney General), 2001 FCA 248 at para 38).

#### 10200:3:subtheme:3 · paragraphs 10-11

- Raw key terms: `appeal, division, failed, finding, general, ability, acted, appeals`
- Display key terms: `division, failed, finding, ability, acted, appeals`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, failed, finding, ability, acted, appeals Rule/authority context: Ingram argues that the Appeal Division unreasonably concluded that the General Division applied the correct legal test in finding that she was not disabled. Application context: Ingram argues that the Appeal Division unreasonably concluded that the General Division applied the correct legal test in finding that she was not disabled. Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4513073` offsets `429-436`; context: An appeal to the Appeal Division may be made only where the General Division: (a) failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction; (b) erred in law in making its decision, whether or not the error appears on the face of the record; or (c) based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it (DESDA, s 58(1); Canada (Attorney General) v O'keefe, 2016 FC 503 at para 29).
- Evidence: `evidence_fact` cue `record` at chunk `4513073` offsets `481-487`; context: An appeal to the Appeal Division may be made only where the General Division: (a) failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction; (b) erred in law in making its decision, whether or not the error appears on the face of the record; or (c) based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it (DESDA, s 58(1); Canada (Attorney General) v O'keefe, 2016 FC 503 at para 29).
- Evidence: `evidence_fact` cue `evidence` at chunk `4513074` offsets `223-231`; context: She says the General Division failed to weigh all of the evidence in assessing the severity of her disability.
- Evidence: `governing_rule` cue `legal test` at chunk `4513074` offsets `117-127`; context: Ingram argues that the Appeal Division unreasonably concluded that the General Division applied the correct legal test in finding that she was not disabled.
- Evidence: `reasoning_application` cue `applied` at chunk `4513074` offsets `97-104`; context: Ingram argues that the Appeal Division unreasonably concluded that the General Division applied the correct legal test in finding that she was not disabled.

#### 10200:3:subtheme:4 · paragraphs 12-15

- Raw key terms: `division, appeal, application, conclusion, general, ingram, advice, chance`
- Display key terms: `division, conclusion, ingram, advice, chance`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: division, conclusion, ingram, advice, chance Application context: [14] The Respondent defends the Appeal Division’s decision as reasonable, and says that it properly applied the test to determine the existence of a “reasonable chance of success” (citing Tracey; Canada (Human Resources  | Ingram’s application should be denied because her disability was not sufficiently severe. Operative outcome context: Ingram’s application should be denied because her disability was not sufficiently severe. | [17] The application for judicial review is therefore allowed, and the matter is remitted to a differently-constituted panel of the Appeal Division for reconsideration. Evidence spans paragraphs 12-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4513075` offsets `400-406`; context: The Respondent maintains that the Appeal Division considered the legal and factual issues presented by Ms.
- Evidence: `reasoning_application` cue `applied` at chunk `4513075` offsets `100-107`; context: [14] The Respondent defends the Appeal Division’s decision as reasonable, and says that it properly applied the test to determine the existence of a “reasonable chance of success” (citing Tracey; Canada (Human Resources Development) v Hogervorst, 2007 FCA 41; Fancy v Canada (Attorney General), 2010 FCA 63 [Fancy]).
- Evidence: `reasoning_application` cue `because` at chunk `4513076` offsets `636-643`; context: Ingram’s application should be denied because her disability was not sufficiently severe.
- Evidence: `disposition` cue `denied` at chunk `4513076` offsets `629-635`; context: Ingram’s application should be denied because her disability was not sufficiently severe.
- Evidence: `reasoning_application` cue `I find` at chunk `4513077` offsets `463-469`; context: Ingram should continue to ignore the advice of her physician and maintain her employment despite debilitating pain, I find that the Appeal’s Division’s conclusion that she did not have an arguable appeal was unreasonable.
- Evidence: `reasoning_application` cue `therefore` at chunk `4513078` offsets `44-53`; context: [17] The application for judicial review is therefore allowed, and the matter is remitted to a differently-constituted panel of the Appeal Division for reconsideration.
- Evidence: `disposition` cue `allowed` at chunk `4513078` offsets `54-61`; context: [17] The application for judicial review is therefore allowed, and the matter is remitted to a differently-constituted panel of the Appeal Division for reconsideration.

#### Section text

[6] The General Division concluded:

[53] It is the Tribunal's view that the Appellant's personal characteristics actually work to her advantage in terms of her being employable in the real world which has been demonstrated. She has transferable skills. As a result, the scope of substantially gainful occupations is much broader for the Appellant than would be the case for a much older, less educated Appellant, with limited English or French language skills.

[54] To establish severe disability, Appellants must not only show a serious health problem, but where there is evidence of work capacity after the MQP, (which the Tribunal finds in this case), must also show an effort at obtaining and maintaining employment has been unsuccessful by reason of the health condition. (as per Inclima v. The Attorney General of Canada, [2003 FCA 117]). Her gainful work from 2013 into 2015 has demonstrated this capacity. Accordingly, the Tribunal cannot find that her medical conditions amount to a level of severity that meet the CPP disability test.

[7] The General Division found that the test for severity had not been met, and it was therefore unnecessary to consider whether the disability was also prolonged. The General Division dismissed the appeal, and Ms. Ingram sought leave from the Appeal Division to appeal that decision.
III. Decision under Review [8] The Appeal Division denied Ms. Ingram’s application for leave to appeal on June 13, 2016, concluding that her appeal had no reasonable chance of success. The Appeal Division acknowledged that the General Division had placed significant emphasis on Ms. Ingram’s earnings in 2013 to 2015 in determining whether she was capable of pursuing substantially gainful employment. Nevertheless, the Appeal Division was satisfied that the General Division had turned its mind to other factors. The Appeal Division concluded as follows:
Given that the General Division did not focus exclusively on the Applicant’s earnings and considered other factors in assessing the severity of her disability, I am not satisfied that the appeal has a reasonable chance of success.
IV. Issue [9] The sole issued raised by this application for judicial review is whether the Appeal Division’s decision to refuse leave to appeal was reasonable.
V. Analysis [10] Decisions of the Appeal Division of the Social Security Tribunal on applications for leave to appeal involve questions of mixed fact and law, and are subject to review by this Court against the standard of reasonableness (Tracey v Canada (Attorney General), 2015 FC 1300 at para 17 [Tracey]; Jama v Canada (Attorney General), 2016 FC 1290 at paras 12-15). The Court will intervene only if the decision falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).

[11] Pursuant to s 44(1)(b) of the Canada Pension Plan, RSC 1985, c C-8, a disability pension is paid to a disabled person who (i) is under sixty-five years of age; (ii) does not receive a retirement pension; and (iii) has made valid contributions to the CPP for at least the MQP. A person is considered to be disabled if the person is determined to have a severe and prolonged mental or physical disability (CPP, s 42(2)). A disability is severe if a person is incapable of regularly pursuing any substantially gainful occupation (CPP, s 42(2)(a)(i)). Prior to reforms that were introduced in 2014, the test consistently applied was whether an applicant had “any disability which renders an applicant incapable of pursuing with consistent frequency any truly remunerative occupation” in a “real world” context (Villani v Canada (Attorney General), 2001 FCA 248 at para 38).

[12] Appeals from the General Division of the Social Security Tribunal to the Appeal Division are governed by the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA]. An appeal to the Appeal Division may be made only where the General Division: (a) failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction; (b) erred in law in making its decision, whether or not the error appears on the face of the record; or (c) based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it (DESDA, s 58(1); Canada (Attorney General) v O'keefe, 2016 FC 503 at para 29). Leave to appeal will be refused where the Appeal Division is satisfied the appeal has “no reasonable chance of success” (DESDA, s 58(2)).

[13] Ms. Ingram argues that the Appeal Division unreasonably concluded that the General Division applied the correct legal test in finding that she was not disabled. She says the General Division failed to weigh all of the evidence in assessing the severity of her disability. In particular, she says that the General Division focused unduly on her post-MQP earnings and her ability to complete tasks at work, and gave insufficient consideration to the evidence of her medical condition.

[14] The Respondent defends the Appeal Division’s decision as reasonable, and says that it properly applied the test to determine the existence of a “reasonable chance of success” (citing Tracey; Canada (Human Resources Development) v Hogervorst, 2007 FCA 41; Fancy v Canada (Attorney General), 2010 FCA 63 [Fancy]). The Respondent maintains that the Appeal Division considered the legal and factual issues presented by Ms. Ingram, and provided a reasonable explanation for its conclusion that the General Division did not rely exclusively on Ms. Ingram’s earnings for the years 2013, 2014 and 2015, but also considered the “constellation” of medical issues bearing on her application.

[15] The General Division accepted that Ms. Ingram met the test of severe disability in 2008, that she had no earnings in the years 2010, 2011 or 2012, and only modest earnings in the years 2013 and 2014. The General Division also accepted that she achieved these modest earnings despite “punishing” herself by working through considerable pain, and against the advice of her family doctor. The General Division also appears to have accepted that Ms. Ingram’s medical condition would not improve. It is difficult to reconcile these findings with the General Division’s ultimate conclusion that Ms. Ingram’s application should be denied because her disability was not sufficiently severe.

[16] The threshold for granting leave to appeal a decision of the General Division is low: “no reasonable chance of success”. This has been interpreted to mean that an appellant must demonstrate an “arguable case” (Fancy at para 4). In light of the internal inconsistencies of the General Division’s decision, and its apparent assumption that Ms. Ingram should continue to ignore the advice of her physician and maintain her employment despite debilitating pain, I find that the Appeal’s Division’s conclusion that she did not have an arguable appeal was unreasonable.

[17] The application for judicial review is therefore allowed, and the matter is remitted to a differently-constituted panel of the Appeal Division for reconsideration.


## 10200:4 · paragraphs 16-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `47b4cc950aa063d727ac77f3bcc208f1d465433f302455f794be2e32a2247d08`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10200:4:subtheme:1 · paragraphs 16-17

- Raw key terms: `allowed, appeal, application, attorney, canada, carol, cause, constituted`
- Display key terms: `allowed, carol, constituted`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: allowed, carol, constituted Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is allowed, and the matter is remitted to a differently constituted panel of the Appeal Division of the Social Security Tribunal for reconsiderat Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `allowed` at chunk `4513078` offsets `247-254`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is allowed, and the matter is remitted to a differently constituted panel of the Appeal Division of the Social Security Tribunal for reconsideration.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is allowed, and the matter is remitted to a differently constituted panel of the Appeal Division of the Social Security Tribunal for reconsideration.
"Simon Fothergill"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1157-16
STYLE OF CAUSE:
CAROL INGRAM v THE ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Ottawa, Ontario
DATE OF HEARING:
March 2, 2017


## 10200:5 · paragraphs 18-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e941d1ebea872d45b711bd687a45378d79668a8ba53ab14c07551b155bc24b43`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10200:5:subtheme:1 · paragraphs 18-18

- Raw key terms: `appearances, applicant, attorney, barristers, canada, clinic, cornwall, coulombe`
- Display key terms: `barristers, clinic, cornwall, coulombe`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, clinic, cornwall, coulombe No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 18-18. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
FOTHERGILL J.
DATED:
March 6, 2017
APPEARANCES:
Robert Coulombe
For The Applicant
Hasan Junaid
For The Respondent
SOLICITORS OF RECORD:
Stormont Dundas and Glengary Legal Clinic
Barristers and Solicitors
Cornwall, Ontario
For The Applicant
William F. Pentney, Q.C.
Deputy Attorney General of Canada
Ottawa, Ontario
For The Respondent
