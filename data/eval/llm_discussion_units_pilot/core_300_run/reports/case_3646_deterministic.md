# Discussion Units: case 3646

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **5**
- Paragraph source hashes: **50**
- Sub-themes: **9**

## 3646:1 · paragraphs 0-3

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6408760dd065418a949f99686b24819d1d9cade53af1bfe2fdf593655d382e7c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3646:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `attorney, decision, general, appeal, applicant, application, canada, court`
- Display key terms: `none`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: no filtered content terms Rule/authority context: The Appeal Division granted the respondent, Miss Gail Dean, leave to appeal a decision of the General Division of the SST, which had denied her appeal with respect to her application for a disability pension benefit unde Operative outcome context: The Appeal Division granted the respondent, Miss Gail Dean, leave to appeal a decision of the General Division of the SST, which had denied her appeal with respect to her application for a disability pension benefit unde | [3] For the following reasons, this application will be granted. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4222495` offsets `385-390`; context: The Appeal Division granted the respondent, Miss Gail Dean, leave to appeal a decision of the General Division of the SST, which had denied her appeal with respect to her application for a disability pension benefit under the Canada Pension Plan, RSC 1985, c C-8 [CPP].
- Evidence: `disposition` cue `granted` at chunk `4222495` offsets `189-196`; context: The Appeal Division granted the respondent, Miss Gail Dean, leave to appeal a decision of the General Division of the SST, which had denied her appeal with respect to her application for a disability pension benefit under the Canada Pension Plan, RSC 1985, c C-8 [CPP].
- Evidence: `disposition` cue `granted` at chunk `4222497` offsets `56-63`; context: [3] For the following reasons, this application will be granted.

#### Section text

Canada (Attorney General) v. Dean
Court (s) Database
Federal Court Decisions
Date
2020-02-05
Neutral citation
2020 FC 206
File numbers
T-1145-19
Decision Content
Date: 20200205
Docket: T-1145-19
Citation: 2020 FC 206
Ottawa, Ontario, and St. John’s, Newfoundland and Labrador
February 5, 2020
PRESENT: Mr. Justice Boswell
BETWEEN:
ATTORNEY GENERAL OF CANADA
Applicant
and
GAIL DEAN
Respondent
JUDGMENT AND REASONS

[1] The applicant, the Attorney General of Canada, seeks judicial review of a decision of the Appeal Division of the Social Security Tribunal [SST] dated June 14, 2019. The Appeal Division granted the respondent, Miss Gail Dean, leave to appeal a decision of the General Division of the SST, which had denied her appeal with respect to her application for a disability pension benefit under the Canada Pension Plan, RSC 1985, c C-8 [CPP].

[2] The Attorney General asks the Court to set aside the Appeal Division’s decision and refer the matter back to a different member of the Appeal Division for redetermination with such directions as the Court considers appropriate. This request for relief requires the Court to determine if it was reasonable for the Appeal Division to grant leave to appeal.

[3] For the following reasons, this application will be granted.


## 3646:2 · paragraphs 4-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5ba44acbe28b165ec3778630ea7f4577ae26b672b7492c48889d82e95d4e86ee`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3646:2:subtheme:1 · paragraphs 4-13

- Raw key terms: `dean, miss, appeal, disability, division, medical, application, because`
- Display key terms: `dean, miss, disability, division, medical, because`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: dean, miss, disability, division, medical, because Rule/authority context: [4] Miss Dean, who represents herself in this matter, applied for a disability benefit under the CPP in September 2016 on the basis that she was unable to work because of various medical conditions, including almost tota | [6] Service Canada refused Miss Dean’s application for a disability pension benefit in January 2017 because she did not qualify under the CPP. Application context: [4] Miss Dean, who represents herself in this matter, applied for a disability benefit under the CPP in September 2016 on the basis that she was unable to work because of various medical conditions, including almost tota | [6] Service Canada refused Miss Dean’s application for a disability pension benefit in January 2017 because she did not qualify under the CPP. Operative outcome context: Upon reconsideration, Service Canada upheld its position that Miss Dean did not qualify for disability benefits because she had made insufficient contributions to the CPP. | A year or so later in June 2018, the General Division dismissed the appeal. Evidence spans paragraphs 4-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4222498` offsets `87-92`; context: [4] Miss Dean, who represents herself in this matter, applied for a disability benefit under the CPP in September 2016 on the basis that she was unable to work because of various medical conditions, including almost total blindness in her left eye and diabetic foot ulcers that affected her ability to stand and walk.
- Evidence: `reasoning_application` cue `applied` at chunk `4222498` offsets `54-61`; context: [4] Miss Dean, who represents herself in this matter, applied for a disability benefit under the CPP in September 2016 on the basis that she was unable to work because of various medical conditions, including almost total blindness in her left eye and diabetic foot ulcers that affected her ability to stand and walk.
- Evidence: `governing_rule` cue `under` at chunk `4222500` offsets `128-133`; context: [6] Service Canada refused Miss Dean’s application for a disability pension benefit in January 2017 because she did not qualify under the CPP.
- Evidence: `reasoning_application` cue `because` at chunk `4222500` offsets `100-107`; context: [6] Service Canada refused Miss Dean’s application for a disability pension benefit in January 2017 because she did not qualify under the CPP.
- Evidence: `disposition` cue `upheld` at chunk `4222500` offsets `248-254`; context: Upon reconsideration, Service Canada upheld its position that Miss Dean did not qualify for disability benefits because she had made insufficient contributions to the CPP.
- Evidence: `evidence_fact` cue `determined that` at chunk `4222501` offsets `50-65`; context: [7] In a letter dated May 1, 2017, Service Canada determined that Miss Dean only had CPP contributions in two of the last six years; that she did not have CPP contributions for at least 25 years, including three of the last six years; and, that she did not qualify under the “late applicant” or the child-rearing provisions of the CPP.
- Evidence: `governing_rule` cue `under` at chunk `4222501` offsets `265-270`; context: [7] In a letter dated May 1, 2017, Service Canada determined that Miss Dean only had CPP contributions in two of the last six years; that she did not have CPP contributions for at least 25 years, including three of the last six years; and, that she did not qualify under the “late applicant” or the child-rearing provisions of the CPP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222502` offsets `381-389`; context: The General Division agreed with the determination by the Minister of Employment and Social Development that Miss Dean did not qualify for a disability pension because she failed to provide medical evidence to show she had a condition that was severe and prolonged at or before the relevant time, known as the minimum qualifying period [MQP].
- Evidence: `reasoning_application` cue `because` at chunk `4222502` offsets `343-350`; context: The General Division agreed with the determination by the Minister of Employment and Social Development that Miss Dean did not qualify for a disability pension because she failed to provide medical evidence to show she had a condition that was severe and prolonged at or before the relevant time, known as the minimum qualifying period [MQP].
- Evidence: `disposition` cue `dismissed` at chunk `4222502` offsets `161-170`; context: A year or so later in June 2018, the General Division dismissed the appeal.
- Evidence: `governing_rule` cue `under` at chunk `4222504` offsets `84-89`; context: [10] After summarizing the background to the appeal, the Appeal Division noted that under the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA], an appeal to the Appeal Division is not a rehearing of a claim.
- Evidence: `governing_rule` cue `under` at chunk `4222505` offsets `116-121`; context: [11] The Appeal Division observed that leave to appeal is refused if the appeal has no reasonable chance of success under subsection 58(2) of the DESDA.
- Evidence: `disposition` cue `granted` at chunk `4222505` offsets `193-200`; context: The Appeal Division remarked that to be granted leave to appeal there must be at least one ground of appeal that falls under the DESDA and on which the appeal has a reasonable chance of success.
- Evidence: `evidence_fact` cue `determined that` at chunk `4222506` offsets `259-274`; context: The Appeal Division determined that repetition of this information was not a ground of appeal under the DESDA and leave to appeal could not be granted on this basis.
- Evidence: `governing_rule` cue `under` at chunk `4222506` offsets `333-338`; context: The Appeal Division determined that repetition of this information was not a ground of appeal under the DESDA and leave to appeal could not be granted on this basis.
- Evidence: `reasoning_application` cue `because` at chunk `4222506` offsets `80-87`; context: [12] In response to Miss Dean’s argument that leave to appeal should be granted because of her medical conditions, the Appeal Division noted that this information had been presented to the General Division and considered by that division.
- Evidence: `disposition` cue `granted` at chunk `4222506` offsets `72-79`; context: [12] In response to Miss Dean’s argument that leave to appeal should be granted because of her medical conditions, the Appeal Division noted that this information had been presented to the General Division and considered by that division.

#### Section text

I. Background

[4] Miss Dean, who represents herself in this matter, applied for a disability benefit under the CPP in September 2016 on the basis that she was unable to work because of various medical conditions, including almost total blindness in her left eye and diabetic foot ulcers that affected her ability to stand and walk. In response to her application, Service Canada sent Miss Dean a letter in late December 2016 requesting medical information.

[5] This letter explained that, based on her earnings and contributions to the CPP, she last met the earnings and contributions criteria in December 1993. It also informed Miss Dean that to qualify for a CPP disability benefit, Service Canada would have to find her unable to do any type of work in 1993 to the date of her application and into the future. Specifically, the letter asked Miss Dean who her doctors were in 1993, what her main medical condition was then, and how it prevented her from working. Miss Dean responded by telling Service Canada that this information was unknown to her.

[6] Service Canada refused Miss Dean’s application for a disability pension benefit in January 2017 because she did not qualify under the CPP. Miss Dean applied for reconsideration of Service Canada’s decision. Upon reconsideration, Service Canada upheld its position that Miss Dean did not qualify for disability benefits because she had made insufficient contributions to the CPP.

[7] In a letter dated May 1, 2017, Service Canada determined that Miss Dean only had CPP contributions in two of the last six years; that she did not have CPP contributions for at least 25 years, including three of the last six years; and, that she did not qualify under the “late applicant” or the child-rearing provisions of the CPP. This letter noted that a medical adjudicator had considered the employment and medical information in her file from December 1993 to the date of her application for disability benefits, and that her work activity and employment earnings in 2003, 2004, 2015 and 2016 showed that she was able to work during those years.

[8] Miss Dean appealed the reconsideration decision to the General Division of the SST in early June 2017. A year or so later in June 2018, the General Division dismissed the appeal. The General Division agreed with the determination by the Minister of Employment and Social Development that Miss Dean did not qualify for a disability pension because she failed to provide medical evidence to show she had a condition that was severe and prolonged at or before the relevant time, known as the minimum qualifying period [MQP].

[9] Miss Dean appealed the General Division’s decision to the Appeal Division of the SST in early August 2018.
II. The Appeal Division Decision

[10] After summarizing the background to the appeal, the Appeal Division noted that under the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA], an appeal to the Appeal Division is not a rehearing of a claim. The Appeal Division further noted that under subsection 58(1) of the DESDA, there are only three kinds of errors that can be considered: the General Division failed to observe a principle of natural justice or made a jurisdictional error, made an error in law, or based its decision on an erroneous finding of fact made in a perverse or capricious manner or without regard for the material before it.

[11] The Appeal Division observed that leave to appeal is refused if the appeal has no reasonable chance of success under subsection 58(2) of the DESDA. The Appeal Division remarked that to be granted leave to appeal there must be at least one ground of appeal that falls under the DESDA and on which the appeal has a reasonable chance of success.

[12] In response to Miss Dean’s argument that leave to appeal should be granted because of her medical conditions, the Appeal Division noted that this information had been presented to the General Division and considered by that division. The Appeal Division determined that repetition of this information was not a ground of appeal under the DESDA and leave to appeal could not be granted on this basis.

## 3646:3 · paragraphs 14-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6f2f624204f327725ebe5bdc5f8d43759bbd189e0edab96213eefdf46ff5ec97`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3646:3:subtheme:1 · paragraphs 14-16

- Raw key terms: `appeal, division, therefore, attorney, basis, canada, chance, claimant`
- Display key terms: `division, therefore, basis, chance`
- Argument roles: `disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, reasoning_application Display terms: division, therefore, basis, chance Application context: Therefore, the General Division may have erred in law, and the appeal has a reasonable chance of success on this basis. | [11] Leave to appeal is therefore granted. Operative outcome context: [11] Leave to appeal is therefore granted. Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222508` offsets `138-146`; context: The decision states that a claimant must provide some objective medical evidence of their disability, and that the medical evidence must relate to the date of the MQP as well as continuously since.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4222508` offsets `516-525`; context: Therefore, the General Division may have erred in law, and the appeal has a reasonable chance of success on this basis.
- Evidence: `reasoning_application` cue `therefore` at chunk `4222509` offsets `24-33`; context: [11] Leave to appeal is therefore granted.
- Evidence: `disposition` cue `granted` at chunk `4222509` offsets `34-41`; context: [11] Leave to appeal is therefore granted.

#### Section text

[13] The Appeal Division continued by stating:

[10] However, the General Division may have made an error in law. The decision states that a claimant must provide some objective medical evidence of their disability, and that the medical evidence must relate to the date of the MQP as well as continuously since. However, the Federal Court of Appeal teaches that a claimant must provide some objective medical evidence of their disability.6 [Warren v Canada (Attorney General), 2008 FCA 377]. It does not require that this evidence points to the MQP or thereafter. Therefore, the General Division may have erred in law, and the appeal has a reasonable chance of success on this basis.

[11] Leave to appeal is therefore granted.


## 3646:4 · paragraphs 17-47

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e54f9feebeb63f1bef9899ad5ffc1fa9ae51f049ab96863b5ce03efff3fe5f75`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3646:4:subtheme:1 · paragraphs 17-37

- Raw key terms: `canada, appeal, disability, court, attorney, division, evidence, general`
- Display key terms: `disability, division`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: disability, division Rule/authority context: [14] The Supreme Court of Canada has recently recalibrated the framework for determining the applicable standard of review for administrative decisions on the merits. | [17] If the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome; nor is i Application context: [15] The starting point is the presumption that a standard of reasonableness applies in all cases and a reviewing court should derogate from this presumption only where required by a clear indication of legislative inten | [19] The Attorney General contends that the Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success because the General Division found the statutory scheme and jurisprudence require objec Operative outcome context: [22] In this case, the Appeal Division granted leave to appeal because it determined that the appeal had a reasonable chance of success since the General Division made an error in law. | [26] Third, the Appeal Division’s interpretation of Warren runs counter to jurisprudence which has upheld the statutory requirement for medical evidence of the disabling condition at the MQP. Evidence spans paragraphs 17-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `standard of review` at chunk `4222510` offsets `104-122`; context: [14] The Supreme Court of Canada has recently recalibrated the framework for determining the applicable standard of review for administrative decisions on the merits.
- Evidence: `reasoning_application` cue `applies` at chunk `4222511` offsets `77-84`; context: [15] The starting point is the presumption that a standard of reasonableness applies in all cases and a reviewing court should derogate from this presumption only where required by a clear indication of legislative intent, or when the rule of law requires the standard of correctness to be applied (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 10, 16 and 17 [Vavilov]; Canada Post Corp v Canadian Union of Postal Workers, 2019 SCC 67 at para 27).
- Evidence: `evidence_fact` cue `evidence` at chunk `4222513` offsets `273-281`; context: [17] If the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome; nor is it the function of the reviewing court to reweigh the evidence (Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61).
- Evidence: `governing_rule` cue `principles` at chunk `4222513` offsets `61-71`; context: [17] If the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome; nor is it the function of the reviewing court to reweigh the evidence (Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61).
- Evidence: `governing_rule` cue `standard of review` at chunk `4222514` offsets `9-27`; context: [18] The standard of review of Appeal Division decisions is reasonableness (Garvey v Canada (Attorney General), 2018 FCA 118 at para 1; Sjogren v Canada (Attorney General), 2019 FCA 157 at para 6; Canada (Attorney General) v Hoffman, 2015 FC 1348 at paras 26 and 27).
- Evidence: `evidence_fact` cue `evidence` at chunk `4222515` offsets `233-241`; context: [19] The Attorney General contends that the Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success because the General Division found the statutory scheme and jurisprudence require objective medical evidence of a disabling condition at the time of the MQP.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4222515` offsets `193-206`; context: [19] The Attorney General contends that the Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success because the General Division found the statutory scheme and jurisprudence require objective medical evidence of a disabling condition at the time of the MQP.
- Evidence: `reasoning_application` cue `because` at chunk `4222515` offsets `133-140`; context: [19] The Attorney General contends that the Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success because the General Division found the statutory scheme and jurisprudence require objective medical evidence of a disabling condition at the time of the MQP.
- Evidence: `evidence_fact` cue `record` at chunk `4222516` offsets `66-72`; context: [20] Miss Dean did not file written submissions or a respondent’s record.
- Evidence: `counterargument_limitation` cue `however` at chunk `4222516` offsets `82-89`; context: She did however, during the hearing of this matter, express frustration with the process thus far and informed the Court that she has been unable to obtain copies of her medical records from 1993.
- Evidence: `evidence_fact` cue `determined that` at chunk `4222518` offsets `74-89`; context: [22] In this case, the Appeal Division granted leave to appeal because it determined that the appeal had a reasonable chance of success since the General Division made an error in law.
- Evidence: `reasoning_application` cue `because` at chunk `4222518` offsets `63-70`; context: [22] In this case, the Appeal Division granted leave to appeal because it determined that the appeal had a reasonable chance of success since the General Division made an error in law.
- Evidence: `disposition` cue `granted` at chunk `4222518` offsets `39-46`; context: [22] In this case, the Appeal Division granted leave to appeal because it determined that the appeal had a reasonable chance of success since the General Division made an error in law.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222520` offsets `69-77`; context: [24] First, Warren does not stand for the proposition that objective evidence does not need to point to the MQP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222521` offsets `483-491`; context: The clear wording in the Canada Pension Plan Regulations, CRC, c 385 [Regulations] required documentary evidence from Miss Dean about her claimed medical condition at her MQP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222522` offsets `144-152`; context: [26] Third, the Appeal Division’s interpretation of Warren runs counter to jurisprudence which has upheld the statutory requirement for medical evidence of the disabling condition at the MQP.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4222522` offsets `75-88`; context: [26] Third, the Appeal Division’s interpretation of Warren runs counter to jurisprudence which has upheld the statutory requirement for medical evidence of the disabling condition at the MQP.
- Evidence: `disposition` cue `upheld` at chunk `4222522` offsets `99-105`; context: [26] Third, the Appeal Division’s interpretation of Warren runs counter to jurisprudence which has upheld the statutory requirement for medical evidence of the disabling condition at the MQP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222523` offsets `38-46`; context: [27] This Court has held that medical evidence dated after an applicant’s MQP is irrelevant.
- Evidence: `disposition` cue `allowed` at chunk `4222523` offsets `157-164`; context: In Canada (Attorney General) v Hoffman, 2015 FC 1348, the Court allowed an application for judicial review of a decision of the Appeal Division which had granted leave to appeal, finding that:
- Evidence: `evidence_fact` cue `Evidence` at chunk `4222524` offsets `5-13`; context: [48] Evidence subsequent to the end of the MQP is not relevant, given the Applicant did not appear to prove her disability prior to the MQP, and it is unclear on what basis or evidence the Member found that the Respondent has a reasonable chance of success on appeal.
- Evidence: `governing_rule` cue `under` at chunk `4222526` offsets `93-98`; context: [29] Paragraph 44(1) (b) of the CPP says a disability pension shall be paid to a contributor under the age of 65, to whom no retirement pension is payable, who is “disabled” as defined under the CPP and has contributed or is deemed to have contributed to the CPP for a specified number of years within the contributory period.
- Evidence: `governing_rule` cue `under` at chunk `4222527` offsets `199-204`; context: [30] Applicants establish eligibility for disability benefits only if they satisfy both statutory tests at the time of application: first, the severe and prolonged mental or physical disability test under subsection 42(2) of the CPP; and second, the recency of contribution test under paragraphs 44(1) (b) and 44(2) (a) of the CPP (Granovsky at para 10).

#### 3646:4:subtheme:2 · paragraphs 38-39

- Raw key terms: `applicant, canada, disability, para, severe, statutory, test, appeal`
- Display key terms: `disability, para, severe, statutory`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: disability, para, severe, statutory Rule/authority context: [33] Employability is the key measure of a severe disability under the CPP (Canada (Attorney General) v Fink, 2006 FCA 354 at para 2; leave to appeal refused Lorena Fink v Attorney General of Canada, SCC No 31917). | [34] A disability is prolonged under subparagraph 42(2) (a) (ii) of the CPP only if it is likely to be long continued and of indefinite duration or is likely to result in death. Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4222530` offsets `624-631`; context: The statutory test for severity requires an “air of reality” in assessing whether an applicant is incapable regularly of pursuing any substantially gainful occupation (Villani at para 46).
- Evidence: `governing_rule` cue `under` at chunk `4222530` offsets `61-66`; context: [33] Employability is the key measure of a severe disability under the CPP (Canada (Attorney General) v Fink, 2006 FCA 354 at para 2; leave to appeal refused Lorena Fink v Attorney General of Canada, SCC No 31917).
- Evidence: `governing_rule` cue `under` at chunk `4222531` offsets `31-36`; context: [34] A disability is prolonged under subparagraph 42(2) (a) (ii) of the CPP only if it is likely to be long continued and of indefinite duration or is likely to result in death.

#### 3646:4:subtheme:3 · paragraphs 40-41

- Raw key terms: `disabled, made, applicant, applicants, become, birthday, branch, claim`
- Display key terms: `disabled, made, become, birthday, branch`
- Argument roles: `governing_rule, party_position`
- Explanation: Observed roles: governing_rule, party_position Display terms: disabled, made, become, birthday, branch Position/evidence statements: [35] Subsection 68(1) of the Regulations stipulates that where applicants claim they are disabled, they must provide a report of their physical or mental disability detailing the nature, extent and prognosis of the disab Rule/authority context: A person’s contributory period starts with the inception of the CPP on January 1, 1966 or the month following the person’s 18th birthday, whichever is later, and ends with the month in which the applicant is determined t Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `4222532` offsets `74-79`; context: [35] Subsection 68(1) of the Regulations stipulates that where applicants claim they are disabled, they must provide a report of their physical or mental disability detailing the nature, extent and prognosis of the disability, the findings upon which the diagnosis or prognosis was made, and any other relevant details about the disability.
- Evidence: `governing_rule` cue `under` at chunk `4222533` offsets `549-554`; context: A person’s contributory period starts with the inception of the CPP on January 1, 1966 or the month following the person’s 18th birthday, whichever is later, and ends with the month in which the applicant is determined to have become disabled under the CPP.

#### 3646:4:subtheme:4 · paragraphs 42-43

- Raw key terms: `application, contributory, dean, last, miss, stipulates, above, affords`
- Display key terms: `contributory, dean, last, miss, stipulates, above, affords`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: contributory, dean, last, miss, stipulates, above, affords Application context: Miss Dean could not avail herself of this provision because there was no medical information relating to her MQP of December 31, 1993. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `record` at chunk `4222534` offsets `351-357`; context: The record shows that Miss Dean had CPP contributions in only two of the last six years prior to her application (in 2015 and 2016) and that she did not have CPP contributions for at least 25 years, including three of the last six years.
- Evidence: `reasoning_application` cue `because` at chunk `4222535` offsets `507-514`; context: Miss Dean could not avail herself of this provision because there was no medical information relating to her MQP of December 31, 1993.

#### 3646:4:subtheme:5 · paragraphs 44-47

- Raw key terms: `appeal, division, dean, decision, general, miss, application, aside`
- Display key terms: `division, dean, miss, aside`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, reasoning_application Display terms: division, dean, miss, aside Application context: This application for judicial review is therefore granted. Operative outcome context: This application for judicial review is therefore granted. Evidence spans paragraphs 44-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4222536` offsets `57-65`; context: [39] The CPP legislative scheme clearly requires medical evidence of a disabling condition at the time of the MQP.
- Evidence: `reasoning_application` cue `therefore` at chunk `4222537` offsets `206-215`; context: This application for judicial review is therefore granted.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4222537` offsets `145-151`; context: [40] The Appeal Division’s reasons for granting Miss Dean’s application for leave to appeal the General Division’s decision are unreasonable and cannot be justified.
- Evidence: `disposition` cue `granted` at chunk `4222537` offsets `216-223`; context: This application for judicial review is therefore granted.

#### Section text

III. Analysis
A. What is the Standard of Review?

[14] The Supreme Court of Canada has recently recalibrated the framework for determining the applicable standard of review for administrative decisions on the merits.

[15] The starting point is the presumption that a standard of reasonableness applies in all cases and a reviewing court should derogate from this presumption only where required by a clear indication of legislative intent, or when the rule of law requires the standard of correctness to be applied (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 10, 16 and 17 [Vavilov]; Canada Post Corp v Canadian Union of Postal Workers, 2019 SCC 67 at para 27). Neither circumstance is present in this case to justify a departure from the presumption of reasonableness review.

[16] Reasonableness review is concerned with both the decision-making process and its outcome. It tasks the Court with reviewing an administrative decision for the existence of internally coherent reasoning and the presence of justification, transparency and intelligibility. A reasonable decision is “one that is based on an internally coherent and rational chain of analysis and that is justified in relation to the facts and law that constrain the decision maker. The reasonableness standard requires that a reviewing court defer to such a decision”. Vavilov at paras 12, 85, 86 and 99; Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).

[17] If the process and the outcome fit comfortably with the principles of justification, transparency and intelligibility, it is not open to a reviewing court to substitute its own view of a preferable outcome; nor is it the function of the reviewing court to reweigh the evidence (Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 59 and 61).

[18] The standard of review of Appeal Division decisions is reasonableness (Garvey v Canada (Attorney General), 2018 FCA 118 at para 1; Sjogren v Canada (Attorney General), 2019 FCA 157 at para 6; Canada (Attorney General) v Hoffman, 2015 FC 1348 at paras 26 and 27). This pre-Vavilov jurisprudence continues to offer insight into the applicable standard of review (Vavilov at para 143).
B. The Parties’ Submissions
(1) The Attorney General’s Submissions

[19] The Attorney General contends that the Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success because the General Division found the statutory scheme and jurisprudence require objective medical evidence of a disabling condition at the time of the MQP. In the Attorney General’s view, the Appeal Division’s decision is unreasonable and does not fall within a range of possible, acceptable outcomes that are defensible in respect of the facts and law.
(2) Miss Dean’s Submissions

[20] Miss Dean did not file written submissions or a respondent’s record. She did however, during the hearing of this matter, express frustration with the process thus far and informed the Court that she has been unable to obtain copies of her medical records from 1993.
C. The Decision is Unreasonable

[21] Subsection 58(2) of the DESDA requires the Appeal Division to grant leave to appeal a General Division decision if the appeal has a reasonable chance of success. A reasonable chance of success means having some arguable ground upon which the proposed appeal might succeed (Osaj v Canada (Attorney General), 2016 FC 115 at para 12). The only grounds of appeal are prescribed in subsection 58(1) of the DESDA: the General Division committed a breach of natural justice, made an error of law, or made an erroneous finding of fact in a perverse and capricious manner or without regard for the material before it (Cameron v Canada (Attorney General), 2018 FCA 100 at para 2).

[22] In this case, the Appeal Division granted leave to appeal because it determined that the appeal had a reasonable chance of success since the General Division made an error in law. In the Appeal Division’s view, the General Division may have erred in law in finding that Miss Dean was required to provide objective medical evidence of her disability and that such evidence must relate to the date of the MQP as well as continuously since. The Appeal Division stated that, while Warren v Canada (Attorney General), 2008 FCA 377 [Warren] says a claimant must provide some objective medical evidence of their disability, the Federal Court of Appeal does not require this evidence to correlate with the MQP or thereafter.

[23] The Appeal Division’s interpretation of Warren is flawed.

[24] First, Warren does not stand for the proposition that objective evidence does not need to point to the MQP. The Court of Appeal in Warren judicially reviewed a Pension Appeals Board decision that found an applicant did not have a disability as defined in the CPP at the relevant MQP. The Court of Appeal found that the Board made no error in law in requiring objective medical evidence of the applicant’s disability, noting that it was well established in law that an applicant must provide some objective medical evidence (Warren at paras 1 and 4).

[25] Second, the Appeal Division’s interpretation of Warren does not align with the CPP legislative scheme. I agree with the Attorney General that the clear and unambiguous wording of the legislation states that a disability benefit is payable only if an applicant has made the required contributions to the CPP and has been found disabled within the meaning of the legislation. The clear wording in the Canada Pension Plan Regulations, CRC, c 385 [Regulations] required documentary evidence from Miss Dean about her claimed medical condition at her MQP.

[26] Third, the Appeal Division’s interpretation of Warren runs counter to jurisprudence which has upheld the statutory requirement for medical evidence of the disabling condition at the MQP. For example, in Gilroy v Canada (Attorney General), 2008 FCA 116 at para 3, the Federal Court of Appeal determined that it could not overturn a decision denying a disability benefit as there was no evidence the applicant could not undertake employment at or before her MQP.

[27] This Court has held that medical evidence dated after an applicant’s MQP is irrelevant. In Canada (Attorney General) v Hoffman, 2015 FC 1348, the Court allowed an application for judicial review of a decision of the Appeal Division which had granted leave to appeal, finding that:

[48] Evidence subsequent to the end of the MQP is not relevant, given the Applicant did not appear to prove her disability prior to the MQP, and it is unclear on what basis or evidence the Member found that the Respondent has a reasonable chance of success on appeal.

[28] The purpose of disability benefits is to replace the incomes of Canadians with disabilities unable to work on a long-term basis. It is not a social welfare scheme; rather, it is a contributory plan in which Parliament has defined both the benefits and the terms of entitlement (Granovsky v Canada (Minister of Employment and Immigration), 2000 SCC 28 at para 9 [Granovsky]).

[29] Paragraph 44(1) (b) of the CPP says a disability pension shall be paid to a contributor under the age of 65, to whom no retirement pension is payable, who is “disabled” as defined under the CPP and has contributed or is deemed to have contributed to the CPP for a specified number of years within the contributory period. Subsection 2(1) defines a contributor as a person who has made an employee’s contribution in a prescribed manner. Eligibility is based on contributions made to the CPP. Based on those contributions, an applicant establishes an MQP.

[30] Applicants establish eligibility for disability benefits only if they satisfy both statutory tests at the time of application: first, the severe and prolonged mental or physical disability test under subsection 42(2) of the CPP; and second, the recency of contribution test under paragraphs 44(1) (b) and 44(2) (a) of the CPP (Granovsky at para 10).

[31] With respect to the first branch of the test, subsection 42(2) says a disability pension is payable to an applicant who is determined in the prescribed manner to have a severe and prolonged mental or physical disability. Subparagraph 42(2) (a)(i) prescribes that a disability is severe only if, by reason of the disability, the person cannot regularly pursue any substantially gainful occupation.

[32] Subsection 68.1(1) of the Regulations defines “substantially gainful” as an occupation that provides a salary or wages equal to or greater than the maximum annual amount a person could receive as a disability pension. It is not the employment that must be “regular” but, rather, the contributor’s incapacity to work (Atkinson v Canada (Attorney General), 2014 FCA 187 at para 37).

[33] Employability is the key measure of a severe disability under the CPP (Canada (Attorney General) v Fink, 2006 FCA 354 at para 2; leave to appeal refused Lorena Fink v Attorney General of Canada, SCC No 31917). Employability occurs in the context of commercial realities and an applicant’s circumstances; it is not determined only by reference to an applicant’s chosen occupation. Rather, employability under the CPP is in relation to any substantially gainful occupation (Villani v Canada (Attorney General), 2001 FCA 248 at para 45 [Villani]). The statutory test for severity requires an “air of reality” in assessing whether an applicant is incapable regularly of pursuing any substantially gainful occupation (Villani at para 46).

[34] A disability is prolonged under subparagraph 42(2) (a) (ii) of the CPP only if it is likely to be long continued and of indefinite duration or is likely to result in death. The “severe” and “prolonged” statutory requirements are cumulative, so that if an applicant does not meet one or the other condition, the application for a disability pension fails. It is not an error for the SST to make a negative determination on one branch of the test and not make a finding on the other branch (Klabouch v Canada (Minister of Social Development), 2008 FCA 33 at para 10).

[35] Subsection 68(1) of the Regulations stipulates that where applicants claim they are disabled, they must provide a report of their physical or mental disability detailing the nature, extent and prognosis of the disability, the findings upon which the diagnosis or prognosis was made, and any other relevant details about the disability.

[36] The second branch of the test (the recency of contribution) is that an applicant must have made contributions to the CPP for the MQP. Paragraph 44(2) (b) defines the start and end date of an individual’s contributory period; that is, the timespan during which an individual may contribute to the CPP. A person’s contributory period starts with the inception of the CPP on January 1, 1966 or the month following the person’s 18th birthday, whichever is later, and ends with the month in which the applicant is determined to have become disabled under the CPP.

[37] Within the contributory period, paragraph 44(2) (a) stipulates that an applicant must have made CPP contributions on earnings above a year’s basic exemption amount for at least four of the previous six calendar years, either in whole or in part, or where CPP contributions were made for 25 years or more at least three of the last six years. The record shows that Miss Dean had CPP contributions in only two of the last six years prior to her application (in 2015 and 2016) and that she did not have CPP contributions for at least 25 years, including three of the last six years.

[38] Subparagraph 44(1) (b) (ii) affords eligibility protection for late applicants. This provision stipulates that applicants who do not meet the MQP requirement at the time of application may still qualify for benefits if they can establish they were disabled at an earlier time when they last met the contributory requirements, and continued to be disabled at the time of the application (Kaminski v Canada (Attorney General), 2014 FC 238 at para 16). Miss Dean could not avail herself of this provision because there was no medical information relating to her MQP of December 31, 1993.
IV. Conclusion

[39] The CPP legislative scheme clearly requires medical evidence of a disabling condition at the time of the MQP. The Appeal Division unreasonably found Miss Dean’s appeal had a reasonable chance of success.

[40] The Appeal Division’s reasons for granting Miss Dean’s application for leave to appeal the General Division’s decision are unreasonable and cannot be justified. This application for judicial review is therefore granted.

[41] The Appeal Division’s decision is set aside, and the matter returned to the Appeal Division to be redetermined by a different member of the Appeal Division.

[42] The Attorney General does not seek costs; so, there will be no order as to costs.


## 3646:5 · paragraphs 48-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f2d1551deaeb33065ae0f1d76a0f0cdbfcf930276bd3a0ec47c98dd7b265aa14`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3646:5:subtheme:1 · paragraphs 48-49

- Raw key terms: `boswell, judgment, t-1145-19, appearances, applicant, application, attorney, behalf`
- Display key terms: `boswell, t-1145-19, behalf`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: boswell, t-1145-19, behalf Operative outcome context: JUDGMENT in T-1145-19 THIS COURT’S JUDGMENT is that: the application for judicial review is granted; and there is no order as to costs. Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `4222539` offsets `179-186`; context: JUDGMENT in T-1145-19
THIS COURT’S JUDGMENT is that: the application for judicial review is granted; and there is no order as to costs.

#### Section text

JUDGMENT in T-1145-19
THIS COURT’S JUDGMENT is that: the application for judicial review is granted; and there is no order as to costs.
"Keith M. Boswell"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1145-19
STYLE OF CAUSE:
ATTORNEY GENERAL OF CANADA v GAIL DEAN
PLACE OF HEARING:
Ottawa, Ontario and St. John’s, Newfoundland and Labrador via teleconference
DATE OF HEARING:
January 23, 2020
REASONS FOR JUDGMENT AND JUDGMENT:
BOSWELL J.
DATED:
February 5, 2020
APPEARANCES:
Matthew Vens
For The Applicant
Gail Dean
For The Respondent
(ON HER OWN BEHALF)
SOLICITORS OF RECORD:
Attorney General of Canada
Ottawa, Ontario
For The Applicant
