# Discussion Units: case 33549

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **46**
- Continuity pairs: **45**
- Discussion Units: **2**
- Paragraph source hashes: **46**
- Sub-themes: **6**

## 33549:1 · paragraphs 0-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `20865d4d6ce8f2ed02d5ce0cbfd31f63ec281824437e36167ebe45177b1a6696`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33549:1:subtheme:1 · paragraphs 0-13

- Raw key terms: `applicants, application, canada, evidence, immigration, citizenship, decision, minister`
- Display key terms: `none`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, party_position Display terms: no filtered content terms Position/evidence statements: [9] On March 10, 2006, the applicants claimed refugee protection. | [12] On June 5, 2007, the applicants submitted a PRRA application, which was subsequently denied. Operative outcome context: ), at page 319, paragraph 8 in fine and 9; Application for leave to appeal to the Supreme Court of Canada denied on February 20, 1992: [1992] 138 N. | [10] On October 24, 2006, the Immigration and Refugee Board (IRB) denied the applicants’ claim, finding that they were not credible and that they should have been able to avail themselves of Mexican state protection. Evidence spans paragraphs 0-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554317` offsets `19-27`; context: [1] The absence of evidence as to the existence of irreparable harm is sufficient in and of itself to dismiss the stay application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554318` offsets `35-43`; context: [2] The applicants have adduced no evidence of personal risk should they return to Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554319` offsets `62-70`; context: [3] It is not sufficient for claimants to provide documentary evidence about problematic situations in their country in order to be recognized as "Convention refugees" or "persons in need of protection".
- Evidence: `evidence_fact` cue `evidence` at chunk `5554320` offsets `16-24`; context: [4] Documentary evidence about the current general situation in a refugee claimant's country cannot by itself establish that the refugee claim is well-founded (Alexibich v.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5554320` offsets `93-99`; context: [4] Documentary evidence about the current general situation in a refugee claimant's country cannot by itself establish that the refugee claim is well-founded (Alexibich v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554321` offsets `42-50`; context: [5] With respect to the assessment of the evidence, it is up to the panel, and not the applicants, to weigh the evidence before it and to make the appropriate findings.
- Evidence: `disposition` cue `denied` at chunk `5554321` offsets `529-535`; context: ), at page 319, paragraph 8 in fine and 9; Application for leave to appeal to the Supreme Court of Canada denied on February 20, 1992: [1992] 138 N.
- Evidence: `party_position` cue `claimed` at chunk `5554325` offsets `38-45`; context: [9] On March 10, 2006, the applicants claimed refugee protection.
- Evidence: `disposition` cue `denied` at chunk `5554326` offsets `66-72`; context: [10] On October 24, 2006, the Immigration and Refugee Board (IRB) denied the applicants’ claim, finding that they were not credible and that they should have been able to avail themselves of Mexican state protection.
- Evidence: `disposition` cue `dismissed` at chunk `5554327` offsets `42-51`; context: [11] On March 20, 2007, the Federal Court dismissed the application for judicial review of the IRB decision dated October 24, 2006.
- Evidence: `party_position` cue `submitted` at chunk `5554328` offsets `37-46`; context: [12] On June 5, 2007, the applicants submitted a PRRA application, which was subsequently denied.
- Evidence: `disposition` cue `denied` at chunk `5554328` offsets `90-96`; context: [12] On June 5, 2007, the applicants submitted a PRRA application, which was subsequently denied.

#### 33549:1:subtheme:2 · paragraphs 14-15

- Raw key terms: `appeal, canada, court, federal, tests, adopted, applicants, application`
- Display key terms: `federal, tests, adopted`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: federal, tests, adopted Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5554330` offsets `87-94`; context: [14] In order to evaluate the merits of the stay application, the Court must determine whether the applicants met the tests laid down by the Federal Court of Appeal in Toth v.
- Evidence: `issue` cue `issue` at chunk `5554331` offsets `317-322`; context: These three tests are
· the existence of a serious issue;
· the existence of irreparable harm;
· and the weighing of the balance of convenience.

#### 33549:1:subtheme:3 · paragraphs 16-21

- Raw key terms: `applicants, found, mexico, protection, prra, application, officer, refugee`
- Display key terms: `mexico, protection, prra, officer, refugee`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: mexico, protection, prra, officer, refugee Application context: [19] On the one hand, the PRRA officer noted that the RPD’s reasons indicate that the RPD found the applicants’ account lacked credibility because of contradictions and omissions in their account. Evidence spans paragraphs 16-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5554332` offsets `67-72`; context: [16] The applicants failed to demonstrate that there was a serious issue to be tried in their application for leave respecting the PRRA officer’s decision, that irreparable harm would result from their removal to Mexico or that their inconvenience would be greater than that caused to the public interest in ensuring that the immigration process provided for in the Immigration and Refugee Protection Act, S.
- Evidence: `issue` cue `question` at chunk `5554333` offsets `48-56`; context: [17] The determination of risk is essentially a question of fact and, for this reason, great deference must be accorded thereto.
- Evidence: `reasoning_application` cue `because` at chunk `5554335` offsets `139-146`; context: [19] On the one hand, the PRRA officer noted that the RPD’s reasons indicate that the RPD found the applicants’ account lacked credibility because of contradictions and omissions in their account.
- Evidence: `evidence_fact` cue `found that` at chunk `5554336` offsets `26-36`; context: [20] Furthermore, the RPD found that the applicants, who had never complained to the authorities in their country, were not successful in demonstrating that state protection was not available in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554337` offsets `65-73`; context: [21] It was up to the applicants to advance clear and convincing evidence of Mexico’s inability to protect its nationals (Canada (Attorney General) v.

#### 33549:1:subtheme:4 · paragraphs 22-40

- Raw key terms: `evidence, applicants, officer, protection, canada, state, documentary, mexico`
- Display key terms: `officer, protection, state, documentary, mexico`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application Display terms: officer, protection, state, documentary, mexico Position/evidence statements: [22] The applicants also had to prove that they had exhausted all of the avenues available in their country before being able to claim protection elsewhere, which they did not successfully do in this case (Kadenko v. | [33] The applicants claim that the PRRA officer allegedly carried out an incomplete analysis of the evidence presented in support of their record and that he is supposed to have disregarded certain evidence they produced Application context: This argument should therefore not be accepted by the Court. Operative outcome context: In so doing, the panel may choose from among the evidence as it sees fit, and this choice is an integral part of its role and expertise (Mahendran, above; Application for leave to appeal to the Supreme Court of Canada de Evidence spans paragraphs 22-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5554338` offsets `129-134`; context: [22] The applicants also had to prove that they had exhausted all of the avenues available in their country before being able to claim protection elsewhere, which they did not successfully do in this case (Kadenko v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554339` offsets `63-71`; context: [23] On the other hand, the officer noted that the documentary evidence analyzed by the RPD in 2006 is essentially the same as it is today.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554340` offsets `37-45`; context: [24] With respect to the documentary evidence, the PRRA officer found that the objective documentary evidence regarding the situation in Mexico did not support the applicants’ submissions on the inability of the Mexican state to provide them with adequate protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554347` offsets `101-109`; context: [30] In their memorandum, the applicants referred to various excerpts from the objective documentary evidence in order to highlight the situation of violence in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554348` offsets `63-71`; context: [31] It is not sufficient for claimants to provide documentary evidence about problematic situations in their country in order to be recognized as “Convention refugees” or “persons in need of protection”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554349` offsets `17-25`; context: [32] Documentary evidence about the current general situation in a refugee claimant’s country cannot by itself establish that the refugee claim is well-founded (Alexibich, above; Ithibu, above).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5554349` offsets `94-100`; context: [32] Documentary evidence about the current general situation in a refugee claimant’s country cannot by itself establish that the refugee claim is well-founded (Alexibich, above; Ithibu, above).
- Evidence: `party_position` cue `claim` at chunk `5554350` offsets `20-25`; context: [33] The applicants claim that the PRRA officer allegedly carried out an incomplete analysis of the evidence presented in support of their record and that he is supposed to have disregarded certain evidence they produced in support of their claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554350` offsets `100-108`; context: [33] The applicants claim that the PRRA officer allegedly carried out an incomplete analysis of the evidence presented in support of their record and that he is supposed to have disregarded certain evidence they produced in support of their claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554352` offsets `36-44`; context: [35] On the other hand, there is no evidence in the record demonstrating that these documents were indeed submitted to the PRRA officer.
- Evidence: `reasoning_application` cue `therefore` at chunk `5554352` offsets `280-289`; context: This argument should therefore not be accepted by the Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554353` offsets `43-51`; context: [36] With respect to the assessment of the evidence, it is up to the panel, and not the applicants, to weigh the evidence before it and to make the appropriate findings.
- Evidence: `disposition` cue `denied` at chunk `5554353` offsets `388-394`; context: In so doing, the panel may choose from among the evidence as it sees fit, and this choice is an integral part of its role and expertise (Mahendran, above; Application for leave to appeal to the Supreme Court of Canada denied on February 20, 1992, above; Hassan, above; Akinlolu, above).
- Evidence: `evidence_fact` cue `evidence` at chunk `5554355` offsets `36-44`; context: [38] The applicants have adduced no evidence of personal risk should they return to Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5554356` offsets `20-28`; context: [39] The absence of evidence as to the existence of irreparable harm is sufficient in and of itself to dismiss the stay application.

#### 33549:1:subtheme:5 · paragraphs 41-43

- Raw key terms: `interest, balance, canada, convenience, immigration, issue, public, stay`
- Display key terms: `interest, balance, convenience, public, stay`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: interest, balance, convenience, public, stay Application context: It is well known that the present procedures were put in place because a practice had grown up in which many cases, totally devoid of merit, were initiated in the court, indeed were clogging the court, for the sole purpo Operative outcome context: This is the public interest which in my view must be weighed against the potential harm to the applicant if a stay is not granted. Evidence spans paragraphs 41-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5554357` offsets `159-164`; context: 535 (QL), discussed the issue of balance of convenience in regard to a stay application and the public interest that must be considered:
- Evidence: `issue` cue `issue` at chunk `5554358` offsets `16-21`; context: [18] What is in issue, however, when considering balance of convenience, is the extent to which the granting of stays might become a practice which thwarts the efficient operation of the immigration legislation.
- Evidence: `reasoning_application` cue `because` at chunk `5554358` offsets `275-282`; context: It is well known that the present procedures were put in place because a practice had grown up in which many cases, totally devoid of merit, were initiated in the court, indeed were clogging the court, for the sole purpose of buying the appellants further time in Canada.
- Evidence: `disposition` cue `granted` at chunk `5554358` offsets `799-806`; context: This is the public interest which in my view must be weighed against the potential harm to the applicant if a stay is not granted.

#### Section text

Alba v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2007-10-29
Neutral citation
2007 FC 1116
File numbers
IMM-3943-07
Decision Content
Date: 20071029
Docket: IMM-3943-07
Citation: 2007 FC 1116
Ottawa, Ontario, October 29, 2007
PRESENT: The Honourable Mr. Justice Shore
BETWEEN:
RICARDO MORALES ALBA
MARICRUZ ORALES BARRADAS
XIOMARA YEDID MORALES MORALES
LEILANI DESIRE MORALES MORALES
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
INTRODUCTION

[1] The absence of evidence as to the existence of irreparable harm is sufficient in and of itself to dismiss the stay application.

[2] The applicants have adduced no evidence of personal risk should they return to Mexico.

[3] It is not sufficient for claimants to provide documentary evidence about problematic situations in their country in order to be recognized as "Convention refugees" or "persons in need of protection". The claimants must also demonstrate a connection between that evidence and their personal situation, which they failed to do (Rahaman v. Canada (Minister of Citizenship and Immigration), 2002 FCA 89, [2002] F.C.J. No. 302 (F.C.A.) (QL)).

[4] Documentary evidence about the current general situation in a refugee claimant's country cannot by itself establish that the refugee claim is well-founded (Alexibich v. Canada (Minister of Citizenship and Immigration), 2002 FCT 53, [2002] F.C.J. No. 57 (QL); Ithibu v. Canada (Minister of Citizenship and Immigration), 2001 FCT 288, [2001] F.C.J. No. 499 (QL)).

[5] With respect to the assessment of the evidence, it is up to the panel, and not the applicants, to weigh the evidence before it and to make the appropriate findings. In so doing, the panel may choose from among the evidence as it sees fit, and this choice is an integral part of its role and expertise (Mahendran v. Canada (Minister of Employment and Immigration), [1991] F.C.J. No. 549 (QL), (1991) 134 N.R. 316 (F.C.A.), at page 319, paragraph 8 in fine and 9; Application for leave to appeal to the Supreme Court of Canada denied on February 20, 1992: [1992] 138 N.R. 404 (No. 22661); Hassan v. Canada (Minister of Employment and Immigration), [1992] F.C.J. No. 946 (QL), (1992) 147 N.R. 317 (F.C.A.); Akinlolu v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 296 (QL)).
JUDICIAL PROCEDURE

[6] This is an application to stay a removal order issued against the applicants, and the said application is joined to an application for leave and judicial review (ALJR) challenging the decision of the pre‑removal risk assessment officer (PRRA officer), N. Gagné, dated July 20, 2007, denying the PRRA application.
FACTS

[7] The applicants, a married couple and their two children, are Mexican citizens.

[8] On February 23, 2006, the applicants arrived in Canada.

[9] On March 10, 2006, the applicants claimed refugee protection.

[10] On October 24, 2006, the Immigration and Refugee Board (IRB) denied the applicants’ claim, finding that they were not credible and that they should have been able to avail themselves of Mexican state protection.

[11] On March 20, 2007, the Federal Court dismissed the application for judicial review of the IRB decision dated October 24, 2006.

[12] On June 5, 2007, the applicants submitted a PRRA application, which was subsequently denied.

[13] On September 24, 2007, the applicants filed an ALJR of the negative PRRA decision.
ANALYSIS

[14] In order to evaluate the merits of the stay application, the Court must determine whether the applicants met the tests laid down by the Federal Court of Appeal in Toth v. Canada (Minister of Employment and Immigration) (1988), 86 N.R. 302 (F.C.A.), [1988] F.C.J. No. 587 (QL).

[15] In this proceeding, the Federal Court of Appeal adopted three tests that it imported from the case law on injunctions, specifically from the Supreme Court of Canada decision in Manitoba (Attorney General) v. Metropolitan Stores (MTS) Ltd., [1987] 1 S.C.R. 110. These three tests are
· the existence of a serious issue;
· the existence of irreparable harm;
· and the weighing of the balance of convenience.

[16] The applicants failed to demonstrate that there was a serious issue to be tried in their application for leave respecting the PRRA officer’s decision, that irreparable harm would result from their removal to Mexico or that their inconvenience would be greater than that caused to the public interest in ensuring that the immigration process provided for in the Immigration and Refugee Protection Act, S.C. 2001, c. 27, follows its course.
SERIOUS ISSUE
i) The applicants should have been able to avail themselves of Mexican state protection

[17] The determination of risk is essentially a question of fact and, for this reason, great deference must be accorded thereto.

[18] In support of their PRRA application, the applicants reiterated the same facts and fears as those previously examined by the Refugee Protection Division (RPD) and found to be not credible.

[19] On the one hand, the PRRA officer noted that the RPD’s reasons indicate that the RPD found the applicants’ account lacked credibility because of contradictions and omissions in their account.

[20] Furthermore, the RPD found that the applicants, who had never complained to the authorities in their country, were not successful in demonstrating that state protection was not available in Mexico.

[21] It was up to the applicants to advance clear and convincing evidence of Mexico’s inability to protect its nationals (Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689).

[22] The applicants also had to prove that they had exhausted all of the avenues available in their country before being able to claim protection elsewhere, which they did not successfully do in this case (Kadenko v. Canada (Solicitor General) (1996), 143 D.L.R. (4th) 532 (F.C.A.)).

[23] On the other hand, the officer noted that the documentary evidence analyzed by the RPD in 2006 is essentially the same as it is today.

[24] With respect to the documentary evidence, the PRRA officer found that the objective documentary evidence regarding the situation in Mexico did not support the applicants’ submissions on the inability of the Mexican state to provide them with adequate protection.

[25] In this regard, in Espinosa v. Canada (Minister of Citizenship and Immigration), 2005 FC 1393, [2005] F.C.J. No. 1737 (QL), Justice Yves de Montigny indicated that the presumption of state protection cannot be easily rebutted:

[7] . . . To rebut this presumption, it would not be sufficient to allege that the police are corrupt or that a police officer did not follow up on a complaint. From this point of view, I, like many of my colleagues, am willing to admit that Mexico is able to protect its citizens even though this protection is far from perfect. . . . (Emphasis added.)

[26] Furthermore, the protection provided by the state does not have to be perfect, but simply adequate, as the state is not able to protect all of its citizens at all times (Canada (Minister of Employment and Immigration) v. Villafranca (1993) 18 Imm. L.R. (2d) 130, [1992] F.C.J. No. 1189 (QL)).

[27] In this regard, this Court’s recent case law is that state protection is available in Mexico and that the state is making efforts to address problems linked to corruption and crime (Burgos v. Canada (Minister of Citizenship and Immigration), 2006 FC 1537, [2006] F.C.J. No. 1924 (QL); Lopez v. Canada (Minister of Citizenship and Immigration), 2007 FC 198, [2007] F.C.J. No. 278 (QL)).

[28] Thus, the PRRA officer considered the serious efforts of the Mexican authorities to address, among other things, the phenomenon of corruption within the state and police forces.

[29] Given the foregoing, it was certainly not unreasonable for the PRRA officer to find that the applicants could have availed themselves of state protection.

[30] In their memorandum, the applicants referred to various excerpts from the objective documentary evidence in order to highlight the situation of violence in Mexico.

[31] It is not sufficient for claimants to provide documentary evidence about problematic situations in their country in order to be recognized as “Convention refugees” or “persons in need of protection”. The claimants must also demonstrate a connection between that evidence and their personal situation, which they failed to do (Rahaman, above).

[32] Documentary evidence about the current general situation in a refugee claimant’s country cannot by itself establish that the refugee claim is well-founded (Alexibich, above; Ithibu, above).

[33] The applicants claim that the PRRA officer allegedly carried out an incomplete analysis of the evidence presented in support of their record and that he is supposed to have disregarded certain evidence they produced in support of their claim.

[34] On the one hand, at page 3 of his decision, the officer specifically mentions all of the documents submitted by the applicants in support of their claim.

[35] On the other hand, there is no evidence in the record demonstrating that these documents were indeed submitted to the PRRA officer. In particular, the applicants’ written submissions for their PRRA application do not contain any list of documents filed. This argument should therefore not be accepted by the Court.

[36] With respect to the assessment of the evidence, it is up to the panel, and not the applicants, to weigh the evidence before it and to make the appropriate findings. In so doing, the panel may choose from among the evidence as it sees fit, and this choice is an integral part of its role and expertise (Mahendran, above; Application for leave to appeal to the Supreme Court of Canada denied on February 20, 1992, above; Hassan, above; Akinlolu, above).
IRREPARABLE HARM

[37] It is important to note that the Court defined irreparable harm in Kerrutt v. Canada (Minister of Employment and Immigration), (1992) 53 F.T.R. 93, [1992] F.C.J. No. 237 (QL), as the return of a person to a country where his or her safety or life is in jeopardy.

[38] The applicants have adduced no evidence of personal risk should they return to Mexico.

[39] The absence of evidence as to the existence of irreparable harm is sufficient in and of itself to dismiss the stay application.
BALANCE OF CONVENIENCE

[40] Justice Barbara Reed, in Membreno-Garcia v. Canada (Minister of Employment and Immigration), [1992] 3 F.C. 306, [1992] F.C.J. No. 535 (QL), discussed the issue of balance of convenience in regard to a stay application and the public interest that must be considered:

[18] What is in issue, however, when considering balance of convenience, is the extent to which the granting of stays might become a practice which thwarts the efficient operation of the immigration legislation. It is well known that the present procedures were put in place because a practice had grown up in which many cases, totally devoid of merit, were initiated in the court, indeed were clogging the court, for the sole purpose of buying the appellants further time in Canada. There is a public interest in having a system which operates in an efficient, expeditious and fair manner and which, to the greatest extent possible, does not lend itself to abusive practices. This is the public interest which in my view must be weighed against the potential harm to the applicant if a stay is not granted. (Emphasis added.)
CONCLUSION

[41] The applicants benefited from all of the legal avenues available to them. The respondent’s interest in enforcing the removal order promptly takes precedence over the hardship that the applicants may suffer.


## 33549:2 · paragraphs 44-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c14d1fc057c229576037e53bfc5732fb8799aebe68f3f1677799926fc55e5220`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33549:2:subtheme:1 · paragraphs 44-45

- Raw key terms: `applicants, judgment, shore, alba, anderson, andrea, appearances, application`
- Display key terms: `shore, alba, anderson, andrea`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: shore, alba, anderson, andrea No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS that the applicants’ stay application be dismissed.
“Michel M.J. Shore”
Judge
Certified true translation
Janine Anderson, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3943-07
STYLE OF CAUSE: RICARDO MORALES ALBA
MARICRUZ ORALES BARRADAS
XIOMARA YEDID MORALES MORALES
LEILANI DESIRE MORALES MORALES
v. THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: October 26, 2007
(by conference call)
REASONS FOR JUDGMENT
AND JUDGMENT: SHORE J.
DATED: October 29, 2007
APPEARANCES:
Cristina Marinelli FOR THE APPLICANTS
Andrea Shahin FOR THE RESPONDENT
SOLICITORS OF RECORD:
CRISTINA MARINELLI FOR THE APPLICANTS
Montréal, Quebec
JOHN H. SIMS, Q.C. FOR THE RESPONDENT
Deputy Attorney General of Canada
