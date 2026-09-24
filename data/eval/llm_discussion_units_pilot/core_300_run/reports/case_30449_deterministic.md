# Discussion Units: case 30449

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **34**
- Continuity pairs: **33**
- Discussion Units: **3**
- Paragraph source hashes: **34**
- Sub-themes: **8**

## 30449:1 · paragraphs 0-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `34facf80f24e4abb147620b9f454366f1ddb173cdd117926280efcd227a90af6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30449:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `milovac, application, decision, general, agreement, appeal, attorney, canada`
- Display key terms: `milovac, agreement`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: milovac, agreement Position/evidence statements: [3] As a preliminary matter, the Respondent submits that some of the documents Mr. Rule/authority context: [2] For the reasons that follow, I am not persuaded that the decision under review is unreasonable. Application context: Milovac’s actions as described below constituted misconduct, and he was therefore disqualified from receiving employment insurance benefits [EI benefits] due to section 30 of the Employment Insurance Act, SC 1996, c 23 [ | Therefore, this application is dismissed. Operative outcome context: Therefore, this application is dismissed. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `therefore` at chunk `5416716` offsets `248-257`; context: Milovac’s actions as described below constituted misconduct, and he was therefore disqualified from receiving employment insurance benefits [EI benefits] due to section 30 of the Employment Insurance Act, SC 1996, c 23 [the Act].
- Evidence: `governing_rule` cue `under` at chunk `5416717` offsets `70-75`; context: [2] For the reasons that follow, I am not persuaded that the decision under review is unreasonable.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5416717` offsets `100-109`; context: Therefore, this application is dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5416717` offsets `131-140`; context: Therefore, this application is dismissed.
- Evidence: `party_position` cue `submits` at chunk `5416718` offsets `44-51`; context: [3] As a preliminary matter, the Respondent submits that some of the documents Mr.
- Evidence: `evidence_fact` cue `Record` at chunk `5416718` offsets `119-125`; context: Milovac included in the Application Record were not before the Appeal Division and should be assigned no weight: Al-Quq v Canada (Attorney General), 2018 FC 574 [Al-Quq].
- Evidence: `evidence_fact` cue `record` at chunk `5416719` offsets `487-493`; context: In my view, none of those facts are in dispute; the inclusion of these five documents in the record adds nothing to the application.

#### 30449:1:subtheme:2 · paragraphs 5-12

- Raw key terms: `employer, milovac, vaccination, applied, dismissed, employees, non-compliance, rights`
- Display key terms: `employer, milovac, vaccination, applied, dismissed, employees, non-compliance, rights`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: employer, milovac, vaccination, applied, dismissed, employees, non-compliance, rights Rule/authority context: 1, pour recevoir des prestations de chômage; (b) the claimant is disentitled under sections 31 to 33 in relation to the employment. Application context: Accordingly, the impugned documents will not be considered in determining this application. | It applied to Mr. Operative outcome context: Milovac applied for an exemption based on freedom of conscience as prescribed by section 2(a) of the Canadian Charter of Rights and Freedoms, Part 1 of the Constitution Act, 1982, being Schedule B to the Canada Act 1982  | Milovac that he would be dismissed by October 31, 2021, if he did not comply in updating his vaccination status. Evidence spans paragraphs 5-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5416720` offsets `457-465`; context: “New” information can be introduced on an application for judicial review when the jurisdiction of a tribunal is in question; see the decision in Gitxsan Treaty Society v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5416720` offsets `102-110`; context: [5] Justice Heneghan, at paras 24–26 of Al-Quq, correctly set out how this Court treats alleged “new” evidence that was not before the decision-maker:
According to the decisions of this Court, the general rule is that only the material that was before the decision‑maker can be considered by the Court in an application for judicial review.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5416721` offsets `117-128`; context: Accordingly, the impugned documents will not be considered in determining this application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5416722` offsets `826-834`; context: • If there is a valid human rights grounds (including religion) with evidence acceptable to HCCSS and in accordance with the Ontario Human Rights Code.
- Evidence: `reasoning_application` cue `applied` at chunk `5416722` offsets `202-209`; context: It applied to Mr.
- Evidence: `reasoning_application` cue `applied` at chunk `5416724` offsets `16-23`; context: Milovac applied for an exemption based on freedom of conscience as prescribed by section 2(a) of the Canadian Charter of Rights and Freedoms, Part 1 of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), c 11 [the Charter], but the Employer denied it and reiterated the consequences of non-compliance.
- Evidence: `disposition` cue `denied` at chunk `5416724` offsets `271-277`; context: Milovac applied for an exemption based on freedom of conscience as prescribed by section 2(a) of the Canadian Charter of Rights and Freedoms, Part 1 of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), c 11 [the Charter], but the Employer denied it and reiterated the consequences of non-compliance.
- Evidence: `reasoning_application` cue `because` at chunk `5416725` offsets `99-106`; context: Milovac that he was being placed on unpaid leave because he had not reported his vaccination status.
- Evidence: `disposition` cue `dismissed` at chunk `5416725` offsets `242-251`; context: Milovac that he would be dismissed by October 31, 2021, if he did not comply in updating his vaccination status.
- Evidence: `disposition` cue `dismissed` at chunk `5416726` offsets `95-104`; context: Milovac did not disclose his vaccination status by October 31, 2021, and the Employer dismissed him the next day for non-compliance.
- Evidence: `governing_rule` cue `under` at chunk `5416727` offsets `1073-1078`; context: 1, pour recevoir des prestations de chômage;
(b) the claimant is disentitled under sections 31 to 33 in relation to the employment.
- Evidence: `reasoning_application` cue `applied` at chunk `5416727` offsets `17-24`; context: Milovac applied for EI benefits following his dismissal.
- Evidence: `disposition` cue `denied` at chunk `5416727` offsets `126-132`; context: The Canada Employment Insurance Commission [the Commission] denied his claim, finding that he was dismissed due to his own misconduct.

#### 30449:1:subtheme:3 · paragraphs 13-15

- Raw key terms: `misconduct, because, claimant, commission, division, employer, general, milovac`
- Display key terms: `misconduct, because, commission, division, employer, milovac`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: misconduct, because, commission, division, employer, milovac Rule/authority context: But the employer’s policy provides for medical exemptions and valid exemptions under the provincial Human Rights Code. Application context: [13] There is no dispute that the exceptions above do not apply. | Milovac submitted that his Employer’s conduct was wrongful because it did not align with the Charter. Operative outcome context: The General Division dismissed the appeal. Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5416728` offsets `74-82`; context: The sole question was whether Mr.
- Evidence: `reasoning_application` cue `apply` at chunk `5416728` offsets `58-63`; context: [13] There is no dispute that the exceptions above do not apply.
- Evidence: `evidence_fact` cue `found that` at chunk `5416729` offsets `212-222`; context: It found that Mr.
- Evidence: `governing_rule` cue `under` at chunk `5416729` offsets `712-717`; context: But the employer’s policy provides for medical exemptions and valid exemptions under the provincial Human Rights Code.
- Evidence: `reasoning_application` cue `because` at chunk `5416729` offsets `442-449`; context: Milovac submitted that his Employer’s conduct was wrongful because it did not align with the Charter.
- Evidence: `counterargument_limitation` cue `but` at chunk `5416729` offsets `77-80`; context: Milovac, reconsidered its decision, but ultimately maintained it.
- Evidence: `disposition` cue `dismissed` at chunk `5416729` offsets `187-196`; context: The General Division dismissed the appeal.
- Evidence: `reasoning_application` cue `I find` at chunk `5416730` offsets `68-74`; context: [15] At paragraph 42, the General Division summarized its findings:
I find that the Claimant’s action, namely going against his employer’s COVID-19 vaccination policy was wilful.

#### 30449:1:subtheme:4 · paragraphs 16-21

- Raw key terms: `appeal, division, general, decision, milovac, argument, employment, erred`
- Display key terms: `division, milovac, argument, employment, erred`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: division, milovac, argument, employment, erred Rule/authority context: It found that the General Division’s analysis aligned with binding decisions from the Federal Court of Appeal, specifically Canada (Attorney General) v Lemire, 2010 FCA 314 [Lemire], wherein at paragraph 15 it stated: [I | Milovac’s submission that his employment contract and collective agreement relieved him from having to get the COVID-19 vaccination pursuant to the Employer’s policy. Application context: Milovac then applied to the Appeal Division for leave to appeal. | [19] I agree with the Respondent that this Court reviews leave to appeal decisions from the Appeal Division on a reasonableness standard: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 2 Operative outcome context: The Appeal Division denied leave to appeal. Evidence spans paragraphs 16-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5416731` offsets `345-350`; context: Specifically, the Appeal Division found that there was no reasonable argument that the General Division erred in law by focusing on the narrow issue of whether Mr.
- Evidence: `evidence_fact` cue `found that` at chunk `5416731` offsets `121-131`; context: It found that he did not raise an argument that had a reasonable chance of success.
- Evidence: `governing_rule` cue `under` at chunk `5416731` offsets `736-741`; context: It found that the General Division’s analysis aligned with binding decisions from the Federal Court of Appeal, specifically Canada (Attorney General) v Lemire, 2010 FCA 314 [Lemire], wherein at paragraph 15 it stated:
[It] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal: Meunier v.
- Evidence: `reasoning_application` cue `applied` at chunk `5416731` offsets `22-29`; context: Milovac then applied to the Appeal Division for leave to appeal.
- Evidence: `disposition` cue `denied` at chunk `5416731` offsets `94-100`; context: The Appeal Division denied leave to appeal.
- Evidence: `evidence_fact` cue `found that` at chunk `5416732` offsets `30-40`; context: [17] The Appeal Division also found that there was no reasonable argument that the General Division erred in dismissing Mr.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5416732` offsets `256-267`; context: Milovac’s submission that his employment contract and collective agreement relieved him from having to get the COVID-19 vaccination pursuant to the Employer’s policy.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5416733` offsets `77-83`; context: [18] The Appeal Division concluded that the decision of the General Division cannot be interfered with in the absence of establishing that it was based on a perverse or capricious finding of fact.
- Evidence: `reasoning_application` cue `applied` at chunk `5416734` offsets `275-282`; context: [19] I agree with the Respondent that this Court reviews leave to appeal decisions from the Appeal Division on a reasonableness standard: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 23, 25; and see examples of the reasonableness standard applied in recent leave to appeal decisions from the Appeal Division in Cecchetto v Canada (Attorney General), 2023 FC 102 [Cecchetto] at para 20, Gauvreau v Canada (Attorney General), 2021 FC 92 at paras 24-27.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5416735` offsets `77-86`; context: Milovac makes several submissions in his memorandum of argument and affidavit in support of the application.
- Evidence: `governing_rule` cue `under` at chunk `5416735` offsets `451-456`; context: I summarize these to be the following:
The Appeal Division ignored that he made a decision to protect his heart from COVID-19 vaccine side effects and that was based on “good, valid and lawful reasons;” namely, the heart attack he had in 2016, and the consequences thereof, and that the Employer ignored his request for an exemption under the Charter based on freedom of conscience;
The Appeal Division ignored his “repeated assertions” that he did not foresee that his employment would be terminated even though he admitted to receiving letters advising that termination may occur;
The Appeal Division erred in agreeing with the General Division that Directive #6 excuses the Employer from breaching the employment contract; and
The Appeal Division failed to determine that the employment contract was unlawfully and unilaterally breached when it added a new essential condition of employment, namely, to be vaccinated.

#### 30449:1:subtheme:5 · paragraphs 22-23

- Raw key terms: `appeal, chance, division, milovac, reasonable, success, address, advanced`
- Display key terms: `chance, division, milovac, reasonable, success, address, advanced`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: chance, division, milovac, reasonable, success, address, advanced Rule/authority context: Milovac raised an argument in his leave application which had a reasonable chance of success in establishing an error in the decision of the General Division as required under paragraph 58(1)(c) of the Department of Empl Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5416737` offsets `14-22`; context: [22] The only question the Appeal Division was required to address was whether Mr.
- Evidence: `governing_rule` cue `under` at chunk `5416737` offsets `253-258`; context: Milovac raised an argument in his leave application which had a reasonable chance of success in establishing an error in the decision of the General Division as required under paragraph 58(1)(c) of the Department of Employment and Social Development Act, SC 2005, c 34.
- Evidence: `evidence_fact` cue `found that` at chunk `5416738` offsets `113-123`; context: Milovac and found that none had a reasonable chance of success on appeal.

#### 30449:1:subtheme:6 · paragraphs 24-30

- Raw key terms: `appeal, division, employer, milovac, because, court, decision, employment`
- Display key terms: `division, employer, milovac, because, employment`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: division, employer, milovac, because, employment Application context: [24] The Appeal Division found that the arguments about the General Division’s findings of fact could not succeed because each of its findings were supported by the evidence on the record. | Milovac strongly believes that the Employer’s policy was an over-reaction to the COVID-19 pandemic, and unfairly applied to him given his previous heart attack and his outstanding performance as an employee. Operative outcome context: Milovac was dismissed due to his own misconduct, so he was disqualified from receiving EI benefits. Evidence spans paragraphs 24-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5416739` offsets `294-299`; context: Moreover, the Appeal Division noted that these findings of fact were not directly material to the narrow issue that the General Division had to decide: that is, whether Mr.
- Evidence: `evidence_fact` cue `found that` at chunk `5416739` offsets `25-35`; context: [24] The Appeal Division found that the arguments about the General Division’s findings of fact could not succeed because each of its findings were supported by the evidence on the record.
- Evidence: `reasoning_application` cue `because` at chunk `5416739` offsets `114-121`; context: [24] The Appeal Division found that the arguments about the General Division’s findings of fact could not succeed because each of its findings were supported by the evidence on the record.
- Evidence: `evidence_fact` cue `determined that` at chunk `5416741` offsets `50-65`; context: [26] The Appeal Division correctly and reasonably determined that the General Division found that Mr.
- Evidence: `disposition` cue `dismissed` at chunk `5416741` offsets `114-123`; context: Milovac was dismissed due to his own misconduct, so he was disqualified from receiving EI benefits.
- Evidence: `reasoning_application` cue `applied` at chunk `5416742` offsets `149-156`; context: Milovac strongly believes that the Employer’s policy was an over-reaction to the COVID-19 pandemic, and unfairly applied to him given his previous heart attack and his outstanding performance as an employee.
- Evidence: `counterargument_limitation` cue `However` at chunk `5416742` offsets `438-445`; context: However, the alleged violation of the collective agreement was properly dealt with by way of a union grievance.
- Evidence: `reasoning_application` cue `because` at chunk `5416743` offsets `335-342`; context: In dismissing the application to review the decision of the Appeal Division not to grant leave to appeal, the Court stated at paragraph 48:
Despite the Applicant’s arguments, there is no basis to overturn the Appeal Division’s decision because of its failure to assess or rule on the merits, legitimacy, or legality of Directive 6.
- Evidence: `reasoning_application` cue `because` at chunk `5416744` offsets `84-91`; context: Milovac lost his employment as a result of his misconduct because he was aware of the Employer’s vaccination policy and the consequences that would result from refusing to comply, has not been shown to be unreasonable.

#### Section text

Milovac v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2023-08-24
Neutral citation
2023 FC 1120
File numbers
T-813-23
Decision Content
Date: 20230824
Docket: T-813-23
Citation: 2023 FC 1120
Ottawa, Ontario, August 24, 2023
PRESENT: The Honourable Mr. Justice Zinn
BETWEEN:
DAVID MILOVAC
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] Mr. Milovac asks the Court to set aside the decision of the Social Security Tribunal’s Appeal Division denying him leave to appeal its General Division’s decision that Mr. Milovac’s actions as described below constituted misconduct, and he was therefore disqualified from receiving employment insurance benefits [EI benefits] due to section 30 of the Employment Insurance Act, SC 1996, c 23 [the Act].

[2] For the reasons that follow, I am not persuaded that the decision under review is unreasonable. Therefore, this application is dismissed.

[3] As a preliminary matter, the Respondent submits that some of the documents Mr. Milovac included in the Application Record were not before the Appeal Division and should be assigned no weight: Al-Quq v Canada (Attorney General), 2018 FC 574 [Al-Quq]. Specifically, the Respondent objects to the following documents:
Hospital Discharge Report, June 25, 2016;
Performance Appraisal Documents, May 30, 2021;
CUPE Grievance Form, Sept. 8, 2021;
Collective Agreement, April 1, 2018, to March 31, 2021; and
Mortality Weekly Report, Aug. 6, 2021.

[4] Mr. Milovac submits that the first four documents do not add anything new to the application and were included by him as he doubted that the relevant decision-makers believed that he had suffered a heart attack that resulted in a weakened heart, that a grievance alleging a violation of the collective agreement had been filed, and that he had been seen by the Employer as a good employee. In my view, none of those facts are in dispute; the inclusion of these five documents in the record adds nothing to the application. Their elimination does not prejudice the submissions that Mr. Milovac wishes to make.

[5] Justice Heneghan, at paras 24–26 of Al-Quq, correctly set out how this Court treats alleged “new” evidence that was not before the decision-maker:
According to the decisions of this Court, the general rule is that only the material that was before the decision‑maker can be considered by the Court in an application for judicial review.
“New” information can be introduced on an application for judicial review when the jurisdiction of a tribunal is in question; see the decision in Gitxsan Treaty Society v. Hospital Employees’ Union et al, [2000] 1 F.C. 135.
In my opinion, the “new” material submitted by the Applicant does not fall within this exception. The exhibits that were not before the decision‑maker will not be considered in the determination of the within application for judicial review.

[6] There is no challenge to the jurisdiction of the Social Security Tribunal’s Appeal Division in this application. Accordingly, the impugned documents will not be considered in determining this application.

[7] Mr. Milovac worked at Mississauga Halton Local Health Integration Network, a community care agency [the Employer]. The Chief Medical Officer of Ontario issued a Directive #6 related to COVID-19. It applied to Mr. Milovac’s Employer. In accordance with that Directive, the Employer issued a policy, the relevant part of which provides as follows:
As a requirement of Directive 6, issued on August 17, 2021, and this policy, HCCSS employees are required to provide proof of vaccination with the following exceptions:
• If there is a valid medical reason, (i.e. documented medical reason for not being fully vaccinated against COVID-19 and the effective time-period for the medical reason). This must be provided by a Medical Doctor or Nurse Practitioner.
• If there is a valid human rights grounds (including religion) with evidence acceptable to HCCSS and in accordance with the Ontario Human Rights Code.

[8] In September 2021, the Employer sent an email to its employees stating that in accordance with the Province’s Directive #6 all employees must show proof of vaccination against COVID-19 or get an exception for medical or human rights reasons. It stated that non-compliance would result in discipline, suspension, or dismissal.

[9] Mr. Milovac applied for an exemption based on freedom of conscience as prescribed by section 2(a) of the Canadian Charter of Rights and Freedoms, Part 1 of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), c 11 [the Charter], but the Employer denied it and reiterated the consequences of non-compliance. Mr. Milovac did not report his vaccination status.

[10] On October 1, 2021, the Employer advised Mr. Milovac that he was being placed on unpaid leave because he had not reported his vaccination status. On October 18, 2021, the Employer sent another letter warning Mr. Milovac that he would be dismissed by October 31, 2021, if he did not comply in updating his vaccination status.

[11] Mr. Milovac did not disclose his vaccination status by October 31, 2021, and the Employer dismissed him the next day for non-compliance.

[12] Mr. Milovac applied for EI benefits following his dismissal. The Canada Employment Insurance Commission [the Commission] denied his claim, finding that he was dismissed due to his own misconduct. It held that he was disqualified for EI benefits by section 30(1) of the Act:
30 (1) A claimant is disqualified from receiving any benefits if the claimant lost any employment because of their misconduct or voluntarily left any employment without just cause, unless
30 (1) Le prestataire est exclu du bénéfice des prestations s’il perd un emploi en raison de son inconduite ou s’il quitte volontairement un emploi sans justification, à moins, selon le cas :
(a) the claimant has, since losing or leaving the employment, been employed in insurable employment for the number of hours required by section 7 or 7.1 to qualify to receive benefits; or
a) que, depuis qu’il a perdu ou quitté cet emploi, il ait exercé un emploi assurable pendant le nombre d’heures requis, au titre de l’article 7 ou 7.1, pour recevoir des prestations de chômage;
(b) the claimant is disentitled under sections 31 to 33 in relation to the employment.
b) qu’il ne soit inadmissible, à l’égard de cet emploi, pour l’une des raisons prévues aux articles 31 à 33.

[13] There is no dispute that the exceptions above do not apply. The sole question was whether Mr. Milovac lost his employment because of his misconduct.

[14] The Commission, as requested by Mr. Milovac, reconsidered its decision, but ultimately maintained it. Mr. Milovac appealed the decision to the General Division. The General Division dismissed the appeal. It found that Mr. Milovac was dismissed due to his own misconduct, and section 30 of the Act disqualified him from receiving regular EI benefits following his dismissal. Mr. Milovac submitted that his Employer’s conduct was wrongful because it did not align with the Charter. The General Division at paragraph 32 of its decision rejected this argument:
The Claimant did identify the Charter in his request for an exemption. But the employer’s policy provides for medical exemptions and valid exemptions under the provincial Human Rights Code. The employer decided that the Claimant’s request did not meet the criteria under its policy.

[15] At paragraph 42, the General Division summarized its findings:
I find that the Claimant’s action, namely going against his employer’s COVID-19 vaccination policy was wilful. He made a conscious, deliberate, and intentional choice not [to] report his vaccination status. He did so knowing that his employer would likely fire him. For these reasons, I find that the Commission has proven that there was misconduct.

[16] Mr. Milovac then applied to the Appeal Division for leave to appeal. The Appeal Division denied leave to appeal. It found that he did not raise an argument that had a reasonable chance of success. Specifically, the Appeal Division found that there was no reasonable argument that the General Division erred in law by focusing on the narrow issue of whether Mr. Milovac was dismissed due to his misconduct within the meaning of the Act. It found that the General Division’s analysis aligned with binding decisions from the Federal Court of Appeal, specifically Canada (Attorney General) v Lemire, 2010 FCA 314 [Lemire], wherein at paragraph 15 it stated:
[It] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal: Meunier v. Canada (Employment and Immigration Commission) (1996), 208 N.R. 377 at paragraph 2.

[17] The Appeal Division also found that there was no reasonable argument that the General Division erred in dismissing Mr. Milovac’s submission that his employment contract and collective agreement relieved him from having to get the COVID-19 vaccination pursuant to the Employer’s policy. It summarized the findings of the General Division at paragraph 14 of the Appeal Decision:
In this case, the General Division made these findings:
• The employer’s COVID-19 vaccination policy did not breach the collective agreement or unilaterally change the Claimant’s conditions of employment;
• The collective agreement gave employees the right to refuse influenza vaccinations, but it did not allow them to refuse all vaccinations; and
• Although Directive 6 did not require dismissal for noncompliance, the employer had wide latitude to ensure its employees complied with its COVID-19 vaccination policy.

[18] The Appeal Division concluded that the decision of the General Division cannot be interfered with in the absence of establishing that it was based on a perverse or capricious finding of fact. It found none.

[19] I agree with the Respondent that this Court reviews leave to appeal decisions from the Appeal Division on a reasonableness standard: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 23, 25; and see examples of the reasonableness standard applied in recent leave to appeal decisions from the Appeal Division in Cecchetto v Canada (Attorney General), 2023 FC 102 [Cecchetto] at para 20, Gauvreau v Canada (Attorney General), 2021 FC 92 at paras 24-27.

[20] Mr. Milovac makes several submissions in his memorandum of argument and affidavit in support of the application. I summarize these to be the following:
The Appeal Division ignored that he made a decision to protect his heart from COVID-19 vaccine side effects and that was based on “good, valid and lawful reasons;” namely, the heart attack he had in 2016, and the consequences thereof, and that the Employer ignored his request for an exemption under the Charter based on freedom of conscience;
The Appeal Division ignored his “repeated assertions” that he did not foresee that his employment would be terminated even though he admitted to receiving letters advising that termination may occur;
The Appeal Division erred in agreeing with the General Division that Directive #6 excuses the Employer from breaching the employment contract; and
The Appeal Division failed to determine that the employment contract was unlawfully and unilaterally breached when it added a new essential condition of employment, namely, to be vaccinated.

[21] Mr. Milovac submits that rather than conducting its own analysis, the Appeal Division parroted the decision of the General Division.

[22] The only question the Appeal Division was required to address was whether Mr. Milovac raised an argument in his leave application which had a reasonable chance of success in establishing an error in the decision of the General Division as required under paragraph 58(1)(c) of the Department of Employment and Social Development Act, SC 2005, c 34.

[23] I agree with the Respondent that the Appeal Division responded to the arguments advanced by Mr. Milovac and found that none had a reasonable chance of success on appeal.

[24] The Appeal Division found that the arguments about the General Division’s findings of fact could not succeed because each of its findings were supported by the evidence on the record. Moreover, the Appeal Division noted that these findings of fact were not directly material to the narrow issue that the General Division had to decide: that is, whether Mr. Milovac had committed misconduct within the meaning of the Act.

[25] I further agree that the Appeal Division correctly noted that the General Division’s decision followed binding Federal Court decisions and there was nothing erroneous in its legal analysis.

[26] The Appeal Division correctly and reasonably determined that the General Division found that Mr. Milovac was dismissed due to his own misconduct, so he was disqualified from receiving EI benefits. To succeed on the leave application, Mr. Milovac had to advance some argument challenging the General Division’s decision that he engaged in misconduct through failing to comply with his Employer’s vaccination requirements despite being warned of the consequences. He advanced none, other than the mere assertion that he did not foresee that his employment would be terminated, even though he accepts these facts. He was wilfully blind to the circumstances facing him. That does not amount to a reasonable chance of success on appeal.

[27] The Court appreciates that Mr. Milovac strongly believes that the Employer’s policy was an over-reaction to the COVID-19 pandemic, and unfairly applied to him given his previous heart attack and his outstanding performance as an employee. The Court also understands that he is strongly of the view that his concerns about the violation of his Charter rights and employment contract were not dealt with by any of the decision-makers. However, the alleged violation of the collective agreement was properly dealt with by way of a union grievance. The Appeal Division at paragraph 19 observed that this Court has previously ruled that Charter concerns are not matters properly before this tribunal.

[28] Cecchetto involved a claimant’s refusal to follow his employer’s COVID-19 vaccination policy. In dismissing the application to review the decision of the Appeal Division not to grant leave to appeal, the Court stated at paragraph 48:
Despite the Applicant’s arguments, there is no basis to overturn the Appeal Division’s decision because of its failure to assess or rule on the merits, legitimacy, or legality of Directive 6. That sort of finding was not within the mandate or jurisdiction of the Appeal Division, nor the SST-GD [citations omitted].

[29] The finding that Mr. Milovac lost his employment as a result of his misconduct because he was aware of the Employer’s vaccination policy and the consequences that would result from refusing to comply, has not been shown to be unreasonable.

[30] The parties agreed that no costs would be awarded.


## 30449:2 · paragraphs 31-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dc3b2d389aff16f8d29ff3dc3223476855ea9586bb459dff3c0deb65d93fbc38`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30449:2:subtheme:1 · paragraphs 31-32

- Raw key terms: `t-813-23, application, attorney, august, canada, cause, costs, court`
- Display key terms: `t-813-23, august, costs`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: t-813-23, august, costs Operative outcome context: JUDGMENT in T-813-23 THIS COURT’S JUDGMENT is that this application is dismissed, without costs. Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5416745` offsets `127-136`; context: JUDGMENT in T-813-23
THIS COURT’S JUDGMENT is that this application is dismissed, without costs.

#### Section text

JUDGMENT in T-813-23
THIS COURT’S JUDGMENT is that this application is dismissed, without costs.
"Russel W. Zinn"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-813-23
STYLE OF CAUSE:
DAVID MILOVAC v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
HELD BY VIDEOCONFERENCE
DATE OF HEARING:
August 16, 2023


## 30449:3 · paragraphs 33-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5806c83eda8ee6c0b4607fa73e77e369926ef2863007c1094a32a2086663a813`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 30449:3:subtheme:1 · paragraphs 33-33

- Raw key terms: `appearances, applicant, attorney, august, behalf, canada, dated, david`
- Display key terms: `august, behalf, dated, david`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, behalf, dated, david No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 33-33. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
ZINN J.
DATED:
august 24, 2023
APPEARANCES:
David Milovac
For The Applicant (ON HIS OWN BEHALF)
Ian McRobbie
For The Respondent
SOLICITORS OF RECORD:
Attorney General of Canada Gatineau, Quebec
For The Respondent
