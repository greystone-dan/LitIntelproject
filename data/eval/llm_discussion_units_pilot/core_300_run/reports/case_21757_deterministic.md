# Discussion Units: case 21757

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **28**
- Continuity pairs: **27**
- Discussion Units: **3**
- Paragraph source hashes: **28**
- Sub-themes: **8**

## 21757:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b75e72177b3b98572132858372bd14e154bff4d6da2251147701a99240ba6d6a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21757:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicants, mendez, reported, mexico, police, state, authorities, based`
- Display key terms: `mendez, reported, mexico, police, state, authorities, based`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: mendez, reported, mexico, police, state, authorities, based Rule/authority context: [1] The applicants seek judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5020885` offsets `229-239`; context: 27 (IRPA) of a decision of the Refugee Protection Division (RPD), dated October 3, 2007, wherein the RPD found that the applicants were neither Convention refugees nor persons in need of protection.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5020885` offsets `40-51`; context: [1] The applicants seek judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020889` offsets `118-126`; context: Mendez based on inconsistencies in his evidence and with his Personal Information Form.

#### 21757:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `applicants, issues, panel, presumption, protection, rebutted, state, analysis`
- Display key terms: `issues, presumption, protection, rebutted, state, analysis`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: issues, presumption, protection, rebutted, state, analysis Rule/authority context: ANALYSIS: Standard of Review: Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5020890` offsets `445-451`; context: Issues:
- Evidence: `evidence_fact` cue `found that` at chunk `5020890` offsets `36-46`; context: [6] In the result, the panel member found that the applicants had not rebutted the presumption of state protection with clear and convincing evidence.
- Evidence: `issue` cue `issues` at chunk `5020891` offsets `8-14`; context: [7] The issues on this application were whether the panel had erred in its credibility findings and erred in its finding that the applicants had not rebutted the presumption of state protection.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5020891` offsets `205-223`; context: ANALYSIS:
Standard of Review:

#### 21757:1:subtheme:3 · paragraphs 8-10

- Raw key terms: `canada, court, decision, paragraph, supreme, citizenship, courts, deference`
- Display key terms: `paragraph, supreme, courts, deference`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: paragraph, supreme, courts, deference Rule/authority context: In determining which of the remaining two standards would be appropriate in a given set of circumstances, the Supreme Court proposed a two-step process at paragraph 62: First, courts ascertain whether the jurisprudence h Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5020892` offsets `676-683`; context: In determining which of the remaining two standards would be appropriate in a given set of circumstances, the Supreme Court proposed a two-step process at paragraph 62:
First, courts ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5020892` offsets `688-701`; context: In determining which of the remaining two standards would be appropriate in a given set of circumstances, the Supreme Court proposed a two-step process at paragraph 62:
First, courts ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question.

#### 21757:1:subtheme:4 · paragraphs 11-12

- Raw key terms: `canada, decision, protection, standard, state, against, applied, apply`
- Display key terms: `protection, standard, state, against, applied, apply`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: protection, standard, state, against, applied, apply Rule/authority context: [12] The weight of the jurisprudence prior to Dunsmuir had established that overall, the standard of review of a state protection decision should be reasonableness: Chaves v. Application context: 74, is then applied. | In my view, that standard should continue to apply. Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5020895` offsets `392-400`; context: That is a question of mixed fact and law for which less deference should be shown the tribunal’s decision.
- Evidence: `reasoning_application` cue `applied` at chunk `5020895` offsets `247-254`; context: 74, is then applied.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5020896` offsets `23-36`; context: [12] The weight of the jurisprudence prior to Dunsmuir had established that overall, the standard of review of a state protection decision should be reasonableness: Chaves v.
- Evidence: `reasoning_application` cue `apply` at chunk `5020896` offsets `507-512`; context: In my view, that standard should continue to apply.

#### 21757:1:subtheme:5 · paragraphs 13-17

- Raw key terms: `applicant, evidence, findings, concerns, credibility, given, member, panel`
- Display key terms: `findings, concerns, credibility, given`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: findings, concerns, credibility, given Position/evidence statements: [14] The applicant submits that the member erred in making adverse credibility findings when there were plausible explanations for each apparent inconsistency, contradiction or omission in his evidence. Application context: Nonetheless, I am unable to conclude from a review of the reasons provided and the relevant testimony that the member made his findings of fact without regard for the evidence or in a perverse or capricious manner. Evidence spans paragraphs 13-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5020897` offsets `56-64`; context: [13] Justice James Russell recently commented upon this question in Woods v.
- Evidence: `party_position` cue `submits` at chunk `5020898` offsets `19-26`; context: [14] The applicant submits that the member erred in making adverse credibility findings when there were plausible explanations for each apparent inconsistency, contradiction or omission in his evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020898` offsets `193-201`; context: [14] The applicant submits that the member erred in making adverse credibility findings when there were plausible explanations for each apparent inconsistency, contradiction or omission in his evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020899` offsets `49-57`; context: [15] I would note that the principal applicant’s evidence was given through an interpreter and some allowance must be made for the confusion that sometimes results in those circumstances.
- Evidence: `reasoning_application` cue `conclude` at chunk `5020899` offsets `216-224`; context: Nonetheless, I am unable to conclude from a review of the reasons provided and the relevant testimony that the member made his findings of fact without regard for the evidence or in a perverse or capricious manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020900` offsets `90-98`; context: [16] I might have reached a different conclusion on certain points had I been hearing the evidence.
- Evidence: `counterargument_limitation` cue `But` at chunk `5020900` offsets `434-437`; context: But it is not for me to reweigh the evidence and substitute my own conclusions for those of the tribunal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020901` offsets `227-235`; context: Absent irrelevant considerations or a failure to provide reasons based on the evidence, the court should not interfere.

#### 21757:1:subtheme:6 · paragraphs 18-24

- Raw key terms: `state, canada, immigration, minister, protection, burden, citizenship, evidence`
- Display key terms: `state, protection, burden`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: state, protection, burden Position/evidence statements: [18] The applicants submit that the member erred in not considering whether the state protection available to them in Mexico would be effective citing critical comments in the objective documentary evidence: Garcia v. Evidence spans paragraphs 18-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5020902` offsets `68-75`; context: [18] The applicants submit that the member erred in not considering whether the state protection available to them in Mexico would be effective citing critical comments in the objective documentary evidence: Garcia v.
- Evidence: `party_position` cue `submit` at chunk `5020902` offsets `20-26`; context: [18] The applicants submit that the member erred in not considering whether the state protection available to them in Mexico would be effective citing critical comments in the objective documentary evidence: Garcia v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020902` offsets `198-206`; context: [18] The applicants submit that the member erred in not considering whether the state protection available to them in Mexico would be effective citing critical comments in the objective documentary evidence: Garcia v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020905` offsets `114-122`; context: [21] The Federal Court of Appeal has recently addressed the burden of proof, standard of proof and quality of the evidence necessary to meet the standard in Canada (Minister of Citizenship and Immigration) v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5020906` offsets `131-139`; context: [22] Paraphrasing from paragraphs 17 to 30 of Carillo, the applicant bears both an evidentiary and legal burden: he must introduce evidence of inadequate state protection and must convince the trier of fact on a balance of probabilities that the evidence adduced establishes that the state protection is inadequate.

#### Section text

Mendez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-05-07
Neutral citation
2008 FC 584
File numbers
IMM-4439-07
Decision Content
Date: 20080507
Docket: IMM-4439-07
Citation: 2008 FC 584
Toronto, Ontario, May 7, 2008
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
LUIS ARCEO MENDEZ
RAMONA ROMO SEGURA
SERGIO EFREN ARCEO ROMO
LUIS ANTONIO ARCEO ROMO
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicants seek judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (IRPA) of a decision of the Refugee Protection Division (RPD), dated October 3, 2007, wherein the RPD found that the applicants were neither Convention refugees nor persons in need of protection.

[2] The applicants are a husband and wife and their two children, all citizens of Mexico. Their claims for refugee protection are based on the allegations of Mr. Mendez (the principal applicant). Mr. Mendez alleges that as a result of his involvement in election campaigns in his home town of Pajacuaran in the state of Michoacan he became aware of corrupt election practices and reported them to the police. Reports were taken, but Mr. Mendez asserts that nothing was done.

[3] Mr. Mendez says that threats were made to him over the telephone and that in mid-February of 2006 Ms Segura and their youngest son were approached and threatened with kidnapping and death if Mr. Mendez did not leave Mexico or stop his activities. On March 22, 2006, Mr. Mendez was attacked while in La Barca in Jalisco state. He required medical attention as a result of the attack and was off work for ten days. This assault was not reported to the authorities.

[4] After threats began again on April 2, 2006, the family moved to Mexico City. The family claims to have been threatened there as well, both on the street and over the telephone. These threats were again not reported to police. The applicants state that it was at this point that they obtained passports and fled the country.

[5] The panel member made a number of adverse credibility findings against Mr. Mendez based on inconsistencies in his evidence and with his Personal Information Form. The member also found that the information reported to the police by Mr. Mendez was vague and insufficient and would not have supported a meaningful investigation, that he had failed to follow up as to what actions the authorities were taking and had failed to report several incidents to the police.

[6] In the result, the panel member found that the applicants had not rebutted the presumption of state protection with clear and convincing evidence. Despite indications of problems with some individuals in the Mexican security forces, the member found that the authorities in that country were making serious efforts to fight corruption and the claimants had not exhausted the mechanisms available to them for protection in their own country.
Issues:

[7] The issues on this application were whether the panel had erred in its credibility findings and erred in its finding that the applicants had not rebutted the presumption of state protection.
ANALYSIS:
Standard of Review:

[8] Recently in Dunsmuir v. New Brunswick 2008 SCC 9, [2008] S.C.J. No. 9, the Supreme Court of Canada revisited the approach to be taken in the judicial review of decisions of administrative tribunals. Among the most important consequences was the Supreme Court's decision to reduce the available standards of review from three to two, collapsing the standard of reasonableness simpliciter and patent unreasonableness into a "single form of ‘reasonableness’ review" (paragraph 45). In determining which of the remaining two standards would be appropriate in a given set of circumstances, the Supreme Court proposed a two-step process at paragraph 62:
First, courts ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of [deference] to be accorded with regard to a particular category of question. Second, where the first inquiry proves unfruitful, courts must proceed to an analysis of the factors making it possible to identify the proper standard of review.

[9] In Mugesera v. Canada (Minister of Citizenship and Immigration), 2005 SCC 40, [2005] 2 S.C.R. 100 at paragraph 38, the Supreme Court had previously held that findings of fact by a tribunal are entitled to great deference by a reviewing court. Having regard to paragraph 18.1(4)(d) of the Federal Courts Act, R.S.C. 1985, c. F-7, the court can intervene only if it considers that the tribunal based its decision or order on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

[10] Since Dunsmuir was released, several Judges of this Court have reached the conclusion that the Supreme Court’s decision does not change the law in respect of factual findings subject to the limitation in paragraph 18.1(4)(d): Da Mota v. Canada (Minister of Citizenship and Immigration), 2008 FC 386, [2008] F.C.J. No. 509 at paragraph 14; Obeid v. Canada (Minister of Citizenship and Immigration), 2008 FC 503, [2008] F.C.J. No. 633; Naumets v. Canada (Minister of Citizenship and Immigration), 2008 FC 522, [2008] F.C.J. No. 655..

[11] The findings of fact that underlie a state protection determination must also be assessed against the standard in paragraph 18.1(4)(d). The test set out in Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, [1993] S.C.J. No. 74, is then applied. Do the facts constitute “clear and convincing confirmation of a state’s inability to protect” so as to rebut the presumption? That is a question of mixed fact and law for which less deference should be shown the tribunal’s decision.

[12] The weight of the jurisprudence prior to Dunsmuir had established that overall, the standard of review of a state protection decision should be reasonableness: Chaves v. Canada (Minister of Citizenship and Immigration), 2005 FC 193, [2005] F.C.J. No. 232; Muszynski v. Canada (Minister of Citizenship and Immigration), 2005 FC 1075, [2005] F.C.J. No. 1329; Franklyn v. Canada (Minister of Citizenship and Immigration), 2005 FC 1249, [2005] F.C.J. No. 1508. In my view, that standard should continue to apply.

[13] Justice James Russell recently commented upon this question in Woods v. Canada (Minister of Citizenship and Immigration), 2008 FC 446, [2008] F.C.J. No. 570 at paragraph 32:
The central issue in this case is whether, given the facts… which the Board accepted, the presumption of adequate state protection was rebutted. I regard this as a question of mixed fact and law reviewable on a standard of reasonableness. Following Dunsmuir, the analysis of the Board's decision will be concerned with "the existence of justification, transparency and intelligibility within the decision-making process" (Dunsmuir at para. 47). If the Decision does not fall "within a range of possible, acceptable outcomes which are defensible in respect of the facts and law," the Decision shall be set aside.
Did the Panel err in its credibility findings?

[14] The applicant submits that the member erred in making adverse credibility findings when there were plausible explanations for each apparent inconsistency, contradiction or omission in his evidence. Counsel for the applicant took me to each credibility finding and to the corresponding pages of the transcript of the oral hearing in which the panel member’s concerns were addressed.

[15] I would note that the principal applicant’s evidence was given through an interpreter and some allowance must be made for the confusion that sometimes results in those circumstances. Nonetheless, I am unable to conclude from a review of the reasons provided and the relevant testimony that the member made his findings of fact without regard for the evidence or in a perverse or capricious manner.

[16] I might have reached a different conclusion on certain points had I been hearing the evidence. For example, the member found that no reasonable explanation had been provided for the applicant’s failure to report his concerns about corrupt election practices to more senior levels of his political party. The applicant’s explanation, which I might have found to be reasonable, was that he had expected a response from the police. But it is not for me to reweigh the evidence and substitute my own conclusions for those of the tribunal. In any event, given the number of points on which incredibility was found, none should be seen as a determinative factor.

[17] The assertion that the principal applicant had plausible explanations for the concerns of the Panel is not sufficient to overturn the findings. Absent irrelevant considerations or a failure to provide reasons based on the evidence, the court should not interfere. On the totality of the evidence, the credibility finding was reasonable.
Did the Panel err in its finding that the applicants had not rebutted the presumption of state protection?

[18] The applicants submit that the member erred in not considering whether the state protection available to them in Mexico would be effective citing critical comments in the objective documentary evidence: Garcia v. Canada (Minister of Citizenship and Immigration), 2007 FC 79, [2007] F.C.J. No. 118 and M.L.R.T. v. Canada (Minister of Citizenship and Immigration), 2005 FC 1690, [2005] F.C.J. No. 2094.

[19] A number of decisions of this Court have held that effectiveness is too high a standard: Smirnov v. Canada (Secretary of State) (T.D.), [1995] 1 F.C. 780, [1994] F.C.J. No. 1922. See also Ferguson v. Canada (Minister of Citizenship and Immigration), 2002 FCT 1212, [2002] F.C.J. No. 1636 at para.7; Syed v. Canada (Minister of Citizenship and Immigration), (2000), 195 F.T.R. 39, [2000] F.C.J. No. 1556; Malik v. Canada (Minister of Citizenship and Immigration), 2004 FC 189, [2004] F.C.J. No. 217; Saeed v. Canada (Minister of Citizenship and Immigration), 2006 FC 1016, [2006] F.C.J. No. 1281.

[20] It is well established that individuals claiming refugee status must provide clear and convincing confirmation of their state’s inability to protect: Ward, above. The protection afforded by the state need not be perfect: Canada (Minister of Employment and Immigration) v. Villafranca, (1992), 99 D.L.R. (4th) 334, 18 Imm. L. R. (2d) 130 (F.C.A.).

[21] The Federal Court of Appeal has recently addressed the burden of proof, standard of proof and quality of the evidence necessary to meet the standard in Canada (Minister of Citizenship and Immigration) v. Carrillo, 2008 FCA 94, [2008] F.C.J. No. 399.

[22] Paraphrasing from paragraphs 17 to 30 of Carillo, the applicant bears both an evidentiary and legal burden: he must introduce evidence of inadequate state protection and must convince the trier of fact on a balance of probabilities that the evidence adduced establishes that the state protection is inadequate. The evidence must have sufficient probative value to meet the applicable standard of proof. The evidence will have sufficient probative value if it convinces the trier of fact on the balance of probabilities that the state protection is inadequate. The evidence must be relevant, reliable and convincing.

[23] The test is not effectiveness but adequacy. In the present instance, the RPD was not persuaded that the state protection available to the applicants in Mexico was inadequate. Given that Mexico is a democracy with functioning political and judicial systems, the burden on the applicants to rebut the presumption of state protection was necessarily a heavy one. The finding that the applicants had failed to meet their burden to rebut the presumption was within the spectrum of reasonable decisions open to the Panel and I see no reason to interfere with that conclusion.

[24] No serious questions of general importance were proposed and none will be certified.


## 21757:2 · paragraphs 25-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2c5379658249dd7c89d0f50ae0e735a45b7f7f55c67c6ca3220d8170a54e83f3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21757:2:subtheme:1 · paragraphs 25-26

- Raw key terms: `application, arceo, cause, certified, citizenship, counsel, court, date`
- Display key terms: `arceo, certified, date`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: arceo, certified, date No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
IT IS THE JUDGMENT OF THIS COURT that the application is dismissed, and no questions are certified.
“Richard G. Mosley”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-4439-07

STYLE OF CAUSE: LUIS ARCEO MENDEZ ET AL V.
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: May 6, 2008
REASONS FOR 

## 21757:3 · paragraphs 27-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `65f141bce9cd283833b0391fc331bbb16005ddb21aebe10b8d203a84850463d2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21757:3:subtheme:1 · paragraphs 27-27

- Raw key terms: `addinall, appearances, applicants, attorney, barrister, canada, dated, deputy`
- Display key terms: `addinall, barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: addinall, barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 27-27. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: Mosley, J.
DATED: May 7, 2008
APPEARANCES:
Richard Addinall FOR THE APPLICANTS
Judy Michaely FOR THE RESPONDENT
SOLICITORS OF RECORD:
Richard Addinall,
Barrister and Solicitor FOR THE APPLICANTS
Toronto, Ontario
John H. Sims, Q.C.
Deputy Attorney General of Canada FOR THE RESPONDENT
