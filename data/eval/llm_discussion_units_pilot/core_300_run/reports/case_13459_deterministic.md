# Discussion Units: case 13459

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **21**
- Continuity pairs: **20**
- Discussion Units: **4**
- Paragraph source hashes: **21**
- Sub-themes: **6**

## 13459:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ee10f1bcbce2dc061317849187238f803238ce048d4e8c3bc151397760453793`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13459:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, application, decision, gift, immigration, momodu, reasons, annis`
- Display key terms: `gift, momodu, annis`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: gift, momodu, annis Rule/authority context: [1] This is an application by Gift Momodu [the Principal Applicant] for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by the Refuge Operative outcome context: [2] For the reasons that follow, the application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4662985` offsets `88-99`; context: [1] This is an application by Gift Momodu [the Principal Applicant] for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by the Refugee Appeal Division [RAD] confirming the Refugee Protection Division’s [RPD] finding that the Applicants are neither Convention refugees nor persons in need of protection under sections 96 and 97(1) of the Act.
- Evidence: `disposition` cue `dismissed` at chunk `4662986` offsets `52-61`; context: [2] For the reasons that follow, the application is dismissed.

#### Section text

Momodu v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-12-09
Neutral citation
2015 FC 1365
File numbers
IMM-656-15
Decision Content
Date: 20151209
Docket: IMM-656-15
Citation: 2015 FC 1365
Ottawa, Ontario, December 9, 2015
PRESENT: The Honourable Mr. Justice Annis
BETWEEN:
CORDILIA GIFT MOMODU
IKECHUKWU BASSEY (MINOR)
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application by Gift Momodu [the Principal Applicant] for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act] of a decision by the Refugee Appeal Division [RAD] confirming the Refugee Protection Division’s [RPD] finding that the Applicants are neither Convention refugees nor persons in need of protection under sections 96 and 97(1) of the Act.

[2] For the reasons that follow, the application is dismissed.


## 13459:2 · paragraphs 3-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `08333b69e0c37845b909357d90220a02821c0cd74b3110c3800f30441559a8a1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13459:2:subtheme:1 · paragraphs 3-8

- Raw key terms: `applicants, applicant, because, evidence, government, harcourt, nigeria, port`
- Display key terms: `because, government, harcourt, nigeria, port`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: because, government, harcourt, nigeria, port Position/evidence statements: The Principal Applicant claims that MJ’s “thugs” in Nigeria would find her if she returned. | [10] The Applicants argued that the RPD erred in concluding that the objective evidence demonstrated that the Nigerian government treats human trafficking seriously. Rule/authority context: Standard of Review [6] It is common ground that the standard of review is reasonableness and that the legal test to assess an IFA is based on a two-prong analysis set out in Rasaratnam v Canada (Minister of Citizenship a Application context: The Principal Applicant alleges that she fears returning to Nigeria because a woman named Mercy John [MJ] trafficked her as a prostitute in Italy and upon her return to Nigeria threatened to kill her and her child and ha | On the one occasion when she was located by the thugs in Lagos, she testified that it was because she was seen by a relative of MJ when she went to show her parents her baby in Uromi. Operative outcome context: The RPD’s finding was upheld by the RAD. Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4662986` offsets `440-446`; context: The Principal Applicant claims that MJ’s “thugs” in Nigeria would find her if she returned.
- Evidence: `reasoning_application` cue `because` at chunk `4662986` offsets `182-189`; context: The Principal Applicant alleges that she fears returning to Nigeria because a woman named Mercy John [MJ] trafficked her as a prostitute in Italy and upon her return to Nigeria threatened to kill her and her child and harm her family if she did not repay money owing from the proceeds of prostitution.
- Evidence: `issue` cue `Issue` at chunk `4662987` offsets `292-297`; context: Issue [5] The only issue this application raises is whether the RAD erred by failing to take into consideration evidence in the record supporting that no reasonable IFA existed for the Applicants.
- Evidence: `evidence_fact` cue `found that` at chunk `4662987` offsets `66-76`; context: [4] The Applicants’ refugee claims were rejected by the RPD which found that a viable internal flight alternative [IFA] existed for the Applicants in Port Harcourt, a large city in Nigeria.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4662987` offsets `494-512`; context: Standard of Review [6] It is common ground that the standard of review is reasonableness and that the legal test to assess an IFA is based on a two-prong analysis set out in Rasaratnam v Canada (Minister of Citizenship and Immigration), [1992] 1 FC 706: the first requirement being the freedom from persecution and the second, being the reasonability of refuge.
- Evidence: `reasoning_application` cue `because` at chunk `4662987` offsets `1743-1750`; context: On the one occasion when she was located by the thugs in Lagos, she testified that it was because she was seen by a relative of MJ when she went to show her parents her baby in Uromi.
- Evidence: `disposition` cue `upheld` at chunk `4662987` offsets `269-275`; context: The RPD’s finding was upheld by the RAD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662988` offsets `43-51`; context: [9] The RPD and RAD’s conclusion that this evidence is not indicative that MJ’s thugs could locate the Applicants in Port Harcourt is reasonable.
- Evidence: `party_position` cue `argued` at chunk `4662989` offsets `20-26`; context: [10] The Applicants argued that the RPD erred in concluding that the objective evidence demonstrated that the Nigerian government treats human trafficking seriously.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662989` offsets `79-87`; context: [10] The Applicants argued that the RPD erred in concluding that the objective evidence demonstrated that the Nigerian government treats human trafficking seriously.
- Evidence: `reasoning_application` cue `because` at chunk `4662989` offsets `310-317`; context: This conclusion was in response to the Principal Applicant’s testimony that she thought she could not access police protection in Port Harcourt because of her experiences in Lagos.
- Evidence: `party_position` cue `argue` at chunk `4662990` offsets `20-25`; context: [11] The Applicants argue that the RPD was selective in its reliance upon the US State Department [USSD] 2014 country Trafficking in Persons Report [the 2014 USSD Report].
- Evidence: `counterargument_limitation` cue `however` at chunk `4662991` offsets `313-320`; context: [12] The passage cited by the Applicants in their memorandum (drafted by a different counsel at the hearing) does not appear to reflect the conclusions of the 2014 USSD Report, which states as follows:
The Government of Nigeria does not fully comply with the minimum standards for the elimination of trafficking; however, it is making significant efforts to do so.

#### 13459:2:subtheme:2 · paragraphs 9-14

- Raw key terms: `applicant, harcourt, port, principal, applicants, evidence, living, conclusion`
- Display key terms: `harcourt, port, principal, living, conclusion`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: harcourt, port, principal, living, conclusion Position/evidence statements: [19] I also disagree with the Applicants’ submissions that the RPD and RAD were not alert in applying the Gender Guidelines in considering these claims. Application context: [14] I find the RAD’s conclusion reasonable as the Applicants have not demonstrated by actual and concrete evidence that it is more than likely that they will be discovered if they relocate to Port Harcourt. Evidence spans paragraphs 9-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4662992` offsets `278-283`; context: In any event, I do not see how this evidence is relevant to the IFA issue, which is premised on the Principal Applicant avoiding being located by MJ’s thugs in Port Harcourt.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662992` offsets `42-50`; context: [13] The 2014 USSD Report contained other evidence on efforts to implement its laws sufficient to demonstrate that Nigeria treats human trafficking seriously and would respond to a complaint by the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662993` offsets `107-115`; context: [14] I find the RAD’s conclusion reasonable as the Applicants have not demonstrated by actual and concrete evidence that it is more than likely that they will be discovered if they relocate to Port Harcourt.
- Evidence: `reasoning_application` cue `I find` at chunk `4662993` offsets `5-11`; context: [14] I find the RAD’s conclusion reasonable as the Applicants have not demonstrated by actual and concrete evidence that it is more than likely that they will be discovered if they relocate to Port Harcourt.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662996` offsets `51-59`; context: [18] The RAD adopted the RPD’s conclusion that the evidence did not support a finding that Principal Applicant met the description of a displaced woman at risk.
- Evidence: `party_position` cue `claims` at chunk `4662997` offsets `145-151`; context: [19] I also disagree with the Applicants’ submissions that the RPD and RAD were not alert in applying the Gender Guidelines in considering these claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662997` offsets `176-184`; context: The Guidelines are not evidence and cannot cure insufficiencies or defects in the evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4662997` offsets `189-195`; context: The Guidelines are not evidence and cannot cure insufficiencies or defects in the evidence.

#### 13459:2:subtheme:3 · paragraphs 15-17

- Raw key terms: `board, canada, citizenship, concluded, court, decision, distinguishable, immigration`
- Display key terms: `concluded, distinguishable`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: concluded, distinguishable Application context: [20] I also conclude that the decisions relied upon by the Applicants with respect to the failure to apply the Gender Guidelines, are distinguishable. | [22] On the basis of the foregoing reasons, the Court concludes that the RAD’s decision falls within the range of reasonable acceptable outcomes and is justified, transparent and intelligible based upon the facts and law Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4662998` offsets `382-387`; context: No similar issue was raised in this matter.
- Evidence: `reasoning_application` cue `conclude` at chunk `4662998` offsets `12-20`; context: [20] I also conclude that the decisions relied upon by the Applicants with respect to the failure to apply the Gender Guidelines, are distinguishable.
- Evidence: `counterargument_limitation` cue `although` at chunk `4662998` offsets `227-235`; context: In Idrees v Canada (Minister of Citizenship and Immigration), 2014 FC 1194, although addressing the second prong of the IFA test, the Court concluded that the Board had failed to consider the ethnic violence in the IFA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4662999` offsets `264-272`; context: Justice Rennie concluded quite correctly that the Board erred when it referred to the Applicant’s ability to establish a new home in Canada as evidence of adaptability.
- Evidence: `reasoning_application` cue `concludes` at chunk `4663000` offsets `54-63`; context: [22] On the basis of the foregoing reasons, the Court concludes that the RAD’s decision falls within the range of reasonable acceptable outcomes and is justified, transparent and intelligible based upon the facts and law.

#### Section text

I. Background [3] The Applicants are from Nigeria. The Principal Applicant alleges that she fears returning to Nigeria because a woman named Mercy John [MJ] trafficked her as a prostitute in Italy and upon her return to Nigeria threatened to kill her and her child and harm her family if she did not repay money owing from the proceeds of prostitution. The Principal Applicant claims that MJ’s “thugs” in Nigeria would find her if she returned.

[4] The Applicants’ refugee claims were rejected by the RPD which found that a viable internal flight alternative [IFA] existed for the Applicants in Port Harcourt, a large city in Nigeria. No new evidence was submitted in support of the appeals. The RPD’s finding was upheld by the RAD.
II. Issue [5] The only issue this application raises is whether the RAD erred by failing to take into consideration evidence in the record supporting that no reasonable IFA existed for the Applicants.
III. Standard of Review [6] It is common ground that the standard of review is reasonableness and that the legal test to assess an IFA is based on a two-prong analysis set out in Rasaratnam v Canada (Minister of Citizenship and Immigration), [1992] 1 FC 706: the first requirement being the freedom from persecution and the second, being the reasonability of refuge. The onus is on the Principal Applicant “to prove actual and concrete evidence of conditions which would jeopardize … her life” (Amit v Canada (Minister of Citizenship and Immigration), 2012 FC 381, para 3).
IV. Analysis [7] The Applicants submit that the RAD erred by failing to take into consideration vital evidence in the record supporting that no reasonable IFA existed for them. The Respondent argues that the Applicants are essentially asking the Court to re-weigh the evidence.
A. Freedom from persecution [8] The RAD concluded that the evidence did not support a finding that MJ’s thugs could locate the Applicants in Port Harcourt. In responding to questions from the RPD, the Principal Applicant testified that when in Delta, prior to departing for Canada, the thugs did not locate her. On the one occasion when she was located by the thugs in Lagos, she testified that it was because she was seen by a relative of MJ when she went to show her parents her baby in Uromi. The RAD noted that more caution in maintaining relations with her parents would prevent inadvertent disclosure of her whereabouts.

[9] The RPD and RAD’s conclusion that this evidence is not indicative that MJ’s thugs could locate the Applicants in Port Harcourt is reasonable.

[10] The Applicants argued that the RPD erred in concluding that the objective evidence demonstrated that the Nigerian government treats human trafficking seriously. This conclusion was in response to the Principal Applicant’s testimony that she thought she could not access police protection in Port Harcourt because of her experiences in Lagos. The RPD pointed out that the Principal Applicant did not complain about her experiences in Lagos to the authorities.

[11] The Applicants argue that the RPD was selective in its reliance upon the US State Department [USSD] 2014 country Trafficking in Persons Report [the 2014 USSD Report]. They cited passages from the report to the effect that “the government did not demonstrate sufficient progress in its anti-trafficking law enforcement efforts” which were ignored. [Emphasis added]

[12] The passage cited by the Applicants in their memorandum (drafted by a different counsel at the hearing) does not appear to reflect the conclusions of the 2014 USSD Report, which states as follows:
The Government of Nigeria does not fully comply with the minimum standards for the elimination of trafficking; however, it is making significant efforts to do so. During the reporting period, the government demonstrated an increase in anti-trafficking law enforcement efforts by increasing the number of trafficking investigations, prosecutions and convictions and by providing extensive specialized anti-trafficking training to officials from various government ministries and agencies. The National Agency for the Prohibition of Trafficking in Persons and Other Related Matters (NAPTIP) increased protection efforts by developing a formal referral mechanism for victim protection, increasing the capacity of its shelters, and identifying and providing services to a larger number of victims. Despite these efforts, the government has yet to pass draft legislation that would restrict the ability of judges to offer fines in lieu of prison time during sentencing and, with the exception of receiving training from NAPTIP, the Ministry of Labor did not make any new efforts to address labor trafficking during the reporting period. Additionally, despite the growing number of Nigerian trafficking victims identified abroad, the government has yet to implement formal procedures for the return and reintegration of Nigerian victims.
[Emphasis added]

[13] The 2014 USSD Report contained other evidence on efforts to implement its laws sufficient to demonstrate that Nigeria treats human trafficking seriously and would respond to a complaint by the Applicants. In any event, I do not see how this evidence is relevant to the IFA issue, which is premised on the Principal Applicant avoiding being located by MJ’s thugs in Port Harcourt.

[14] I find the RAD’s conclusion reasonable as the Applicants have not demonstrated by actual and concrete evidence that it is more than likely that they will be discovered if they relocate to Port Harcourt.
B. The Reasonability of the IFA [15] With respect to the reasonability of the Applicants living in Port Harcourt, the Principal Applicant specifically testified before the RPD that she would be able to live in Port Harcourt if she did not encounter problems from being located by MJ. The RPD found this evidence significant in concluding that it is not objectively unreasonable for the Applicants to seek refuge in Port Harcourt.

[16] In follow-up questions from her counsel, the Principal Applicant testified that she did not speak the language in Port Harcourt, that she did not have any family or know any persons living there, nor would she have a job there.

[17] The Applicants also referred to reports indicating that women were vulnerable to abuse, harassment and trafficking when relocating to another area in Nigeria without economic means or family networks. In particular, these reports detailed some of the factors that are constraints on women who consider relocating in Nigeria. These included lack of information on the part of the women themselves, their level of empowerment, the lack of accommodation, job opportunities and poverty.

[18] The RAD adopted the RPD’s conclusion that the evidence did not support a finding that Principal Applicant met the description of a displaced woman at risk. It pointed out that the Principal Applicant had proven to be a resourceful woman who had traveled to the United States and to Canada on her own, besides living in Italy. Her home town is an hour or so away from Port Harcourt. The RPD also noted that she had past experience in childcare and had worked as a hawker, which was employment that she could pursue in Port Harcourt.

[19] I also disagree with the Applicants’ submissions that the RPD and RAD were not alert in applying the Gender Guidelines in considering these claims. The Guidelines are not evidence and cannot cure insufficiencies or defects in the evidence. The two panels found that the circumstances of the Principal Applicant did not meet the profile described in the objective country condition evidence, such that it would not be unreasonable for the Applicants to live securely in Port Harcourt.

[20] I also conclude that the decisions relied upon by the Applicants with respect to the failure to apply the Gender Guidelines, are distinguishable. In Idrees v Canada (Minister of Citizenship and Immigration), 2014 FC 1194, although addressing the second prong of the IFA test, the Court concluded that the Board had failed to consider the ethnic violence in the IFA. No similar issue was raised in this matter. This issue also appears to be more relevant to the first prong of the test.

[21] Similarly, the decision of Utoh v Canada (Minister of Citizenship and Immigration), 2012 FC 399 is distinguishable. Justice Rennie concluded quite correctly that the Board erred when it referred to the Applicant’s ability to establish a new home in Canada as evidence of adaptability. How one integrates into Canadian society bears little relevance to relocating within the foreign national’s country of origin. The adaptability of the Principal Applicant in this matter relates to her ability to take herself out of danger and travel unaccompanied to foreign lands, in addition to her childcare and employment experiences.

[22] On the basis of the foregoing reasons, the Court concludes that the RAD’s decision falls within the range of reasonable acceptable outcomes and is justified, transparent and intelligible based upon the facts and law.


## 13459:3 · paragraphs 18-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `435b9d00215e940a2a0dd22bc462243c6d7e739c66849fee8cf271d9f29eaeb2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13459:3:subtheme:1 · paragraphs 18-19

- Raw key terms: `annis, appeal, application, bassey, cause, certified, citizenship, conclusion`
- Display key terms: `annis, bassey, certified, conclusion`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: annis, bassey, certified, conclusion Operative outcome context: Conclusion [23] The application is dismissed. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4663000` offsets `274-282`; context: No question is certified for appeal.
- Evidence: `disposition` cue `dismissed` at chunk `4663000` offsets `260-269`; context: Conclusion [23] The application is dismissed.

#### Section text

V. Conclusion [23] The application is dismissed. No question is certified for appeal.
JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed and no question is certified for appeal.
"Peter Annis"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-656-15
STYLE OF CAUSE:
CORDILIA GIFT MOMODU AND IKECHUKWU BASSEY (MINOR) v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
november 25, 2015


## 13459:4 · paragraphs 20-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b5b48eda40feddc8e1c106876e2b5511ae8ed365926310a1734541e229cb40b3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13459:4:subtheme:1 · paragraphs 20-20

- Raw key terms: `annis, appearances, applicants, attorney, babalola, barrister, canada, christopher`
- Display key terms: `annis, babalola, barrister, christopher`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: annis, babalola, barrister, christopher No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND reasons:
ANNIS J.
DATED:
december 9, 2015
APPEARANCES:
Oluwakemi Oduwole
For The Applicants
Christopher Crighton
For The Respondent
SOLICITORS OF RECORD:
Johnson Babalola
Barrister & Solicitors
North York, Ontario
For The Applicants
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
