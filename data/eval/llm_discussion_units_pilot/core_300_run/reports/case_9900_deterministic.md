# Discussion Units: case 9900

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **98**
- Continuity pairs: **97**
- Discussion Units: **8**
- Paragraph source hashes: **98**
- Sub-themes: **32**

## 9900:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9f8396bd0e0c1da9f7a29fd1726849c33c1a907817ceed7064b3eb5207b12684`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicants, canada, claims, decision, falun, gong, applicant, practice`
- Display key terms: `claims, falun, gong, practice`
- Argument roles: `disposition, governing_rule, party_position`
- Explanation: Observed roles: disposition, governing_rule, party_position Display terms: claims, falun, gong, practice Position/evidence statements: The Principal Applicant claims she attended group practice with her friend on Saturdays and also practiced daily at home. | The Principal Applicant hid at the home of her former schoolmate; during this time, she claims the PSB continued to seek her and also threatened her parents-in-law. Rule/authority context: [1] This is an application under s 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of  | DECISION UNDER REVIEW Operative outcome context: [6] In a Decision dated December 14, 2016, the RAD confirmed the RPD’s decision and dismissed the Applicants’ appeal. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4500347` offsets `27-32`; context: [1] This is an application under s 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB], dated December 14, 2016 [Decision], which rejected the Applicants’ claims for refugee protection pursuant to ss 96 and 97(1) of the IRPA.
- Evidence: `party_position` cue `claims` at chunk `4500349` offsets `339-345`; context: The Principal Applicant claims she attended group practice with her friend on Saturdays and also practiced daily at home.
- Evidence: `party_position` cue `claims` at chunk `4500350` offsets `542-548`; context: The Principal Applicant hid at the home of her former schoolmate; during this time, she claims the PSB continued to seek her and also threatened her parents-in-law.
- Evidence: `governing_rule` cue `UNDER` at chunk `4500351` offsets `302-307`; context: DECISION UNDER REVIEW
- Evidence: `disposition` cue `dismissed` at chunk `4500352` offsets `84-93`; context: [6] In a Decision dated December 14, 2016, the RAD confirmed the RPD’s decision and dismissed the Applicants’ appeal.

#### 9900:1:subtheme:2 · paragraphs 7-9

- Raw key terms: `applicant, concurred, falun, principal, because, claim, clear, co-practitioners`
- Display key terms: `concurred, falun, principal, because, clear, co-practitioners`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: concurred, falun, principal, because, clear, co-practitioners Position/evidence statements: [8] The RAD concurred with the RPD and drew a negative inference due to the inconsistency between the Principal Applicant’s Basis of Claim [BOC] form and testimony at the RPD hearing regarding the frequency of her Falun  Application context: The RAD rejected the explanation that the inconsistency was due to incorrect instructions from her counsel’s staff because the BOC instructions were clear and the Principal Applicant had been represented by competent cou | The RAD rejected the explanation that her counsel’s staff had instructed her to omit the information because the instructions were clear to state all important information and the detainment of all her co-practitioners w Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500353` offsets `89-94`; context: [7] The RAD concurred with the RPD that the lack of corroborative evidence regarding the issue that prompted the Principal Applicant to join Falun Gong, namely her husband’s disappearance in 2012, called into question why she would turn to an illegal cult.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500353` offsets `66-74`; context: [7] The RAD concurred with the RPD that the lack of corroborative evidence regarding the issue that prompted the Principal Applicant to join Falun Gong, namely her husband’s disappearance in 2012, called into question why she would turn to an illegal cult.
- Evidence: `party_position` cue `Claim` at chunk `4500354` offsets `133-138`; context: [8] The RAD concurred with the RPD and drew a negative inference due to the inconsistency between the Principal Applicant’s Basis of Claim [BOC] form and testimony at the RPD hearing regarding the frequency of her Falun Gong practice.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500354` offsets `154-163`; context: [8] The RAD concurred with the RPD and drew a negative inference due to the inconsistency between the Principal Applicant’s Basis of Claim [BOC] form and testimony at the RPD hearing regarding the frequency of her Falun Gong practice.
- Evidence: `reasoning_application` cue `because` at chunk `4500354` offsets `350-357`; context: The RAD rejected the explanation that the inconsistency was due to incorrect instructions from her counsel’s staff because the BOC instructions were clear and the Principal Applicant had been represented by competent counsel.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500355` offsets `458-466`; context: The RAD rejected the explanation that her counsel’s staff had instructed her to omit the information because the instructions were clear to state all important information and the detainment of all her co-practitioners was an integral portion of the evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4500355` offsets `309-316`; context: The RAD rejected the explanation that her counsel’s staff had instructed her to omit the information because the instructions were clear to state all important information and the detainment of all her co-practitioners was an integral portion of the evidence.

#### 9900:1:subtheme:3 · paragraphs 10-11

- Raw key terms: `applicant, concurred, hiding, place, principal, testimony, actually, agreed`
- Display key terms: `concurred, hiding, place, principal, testimony, actually, agreed`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: concurred, hiding, place, principal, testimony, actually, agreed Position/evidence statements: [11] The RAD concurred with the RPD that, on a balance of probabilities, the Principal Applicant had not been in hiding as claimed in May 2014. Application context: At the RPD hearing, the Principal Applicant had testified that she had stayed in her original residence because she could not find a hiding place, but then changed her testimony to state that she had stayed with her form Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4500356` offsets `181-189`; context: [10] The RAD concurred with the RPD that the inconsistency in the testimony before the RPD regarding where the Principal Applicant kept her copy of her Zhuan Falun book called into question whether she actually had a copy or ever read it.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500356` offsets `66-75`; context: [10] The RAD concurred with the RPD that the inconsistency in the testimony before the RPD regarding where the Principal Applicant kept her copy of her Zhuan Falun book called into question whether she actually had a copy or ever read it.
- Evidence: `party_position` cue `claimed` at chunk `4500357` offsets `123-130`; context: [11] The RAD concurred with the RPD that, on a balance of probabilities, the Principal Applicant had not been in hiding as claimed in May 2014.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500357` offsets `312-321`; context: At the RPD hearing, the Principal Applicant had testified that she had stayed in her original residence because she could not find a hiding place, but then changed her testimony to state that she had stayed with her former schoolmate.
- Evidence: `reasoning_application` cue `because` at chunk `4500357` offsets `248-255`; context: At the RPD hearing, the Principal Applicant had testified that she had stayed in her original residence because she could not find a hiding place, but then changed her testimony to state that she had stayed with her former schoolmate.

#### 9900:1:subtheme:4 · paragraphs 12-19

- Raw key terms: `airport, applicant, china, passport, principal, documentation, falun, gong`
- Display key terms: `airport, china, passport, principal, documentation, falun, gong`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: airport, china, passport, principal, documentation, falun, gong Position/evidence statements: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her fami Application context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her fami | The RAD found it reasonable to expect that the Principal Applicant, an individual expecting to avoid arrest and detention by leaving the country, would inquire about the services provided by a smuggler, particularly beca Evidence spans paragraphs 12-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4500358` offsets `223-231`; context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB.
- Evidence: `party_position` cue `claimed` at chunk `4500358` offsets `125-132`; context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500358` offsets `281-289`; context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB.
- Evidence: `reasoning_application` cue `because` at chunk `4500358` offsets `193-200`; context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB.
- Evidence: `counterargument_limitation` cue `however` at chunk `4500358` offsets `233-240`; context: The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB.
- Evidence: `issue` cue `issue` at chunk `4500359` offsets `259-264`; context: While the PSB’s policy on the issuance of a summons was not uniform across the country, the RAD noted that it was unreasonable for the PSB to not issue a summons in circumstances where the PSB had been vigorous in pursuing the Principal Applicant by attending her family home up to 8 times and arresting all her co-practitioners, who were allegedly still in detention.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500363` offsets `53-61`; context: [17] The RAD also reviewed the Principal Applicant’s evidence of the smuggler she used to exit China and found it to be vague and lacking in detail.
- Evidence: `reasoning_application` cue `because` at chunk `4500363` offsets `365-372`; context: The RAD found it reasonable to expect that the Principal Applicant, an individual expecting to avoid arrest and detention by leaving the country, would inquire about the services provided by a smuggler, particularly because she had testified that she joined Falun Gong only after being reassured there were safety measures in place.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500363` offsets `482-489`; context: However, the RAD also noted that its plausibility conclusion was based on recent information in the National Documentation Package for China [NDP].
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4500365` offsets `368-379`; context: Accordingly, the RAD did not accept that the Principal Applicant could bypass all of the security controls in place.

#### 9900:1:subtheme:5 · paragraphs 20-20

- Raw key terms: `activities, alleged, applicant, authorities, aware, canada, china, chinese`
- Display key terms: `activities, alleged, authorities, aware, china, chinese`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: activities, alleged, authorities, aware, china, chinese Position/evidence statements: The RAD also found that the RPD could import credibility findings from the Principal Applicant’s testimony regarding her practice in China in the determination of her sur place claim. Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4500366` offsets `581-587`; context: ISSUES
- Evidence: `party_position` cue `claim` at chunk `4500366` offsets `378-383`; context: The RAD also found that the RPD could import credibility findings from the Principal Applicant’s testimony regarding her practice in China in the determination of her sur place claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500366` offsets `102-110`; context: [20] The RAD concurred with the RPD that the Principal Applicant had not provided sufficient credible evidence to establish her identity as a Falun Gong practitioner or that she was wanted by the PSB.

#### Section text

Huang v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2017-08-10
Neutral citation
2017 FC 762
File numbers
IMM-53-17
Decision Content
Date: 20170810
Docket: IMM-53-17
Citation: 2017 FC 762
Ottawa, Ontario, August 10, 2017
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
GUIMEI HUANG
JIAHAO WU
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. INTRODUCTION

[1] This is an application under s 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] for judicial review of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB], dated December 14, 2016 [Decision], which rejected the Applicants’ claims for refugee protection pursuant to ss 96 and 97(1) of the IRPA.
II. BACKGROUND

[2] The Applicants are citizens of the People’s Republic of China. They are a mother [Principal Applicant] and son [Minor Applicant] and allege that they fear persecution for reasons relating to the Principal Applicant’s practice of Falun Gong.

[3] The Principal Applicant began practicing Falun Gong in May 2013. She says she was introduced to the practice by a friend who believed that Falun Gong would help her relax and improve her health, which had deteriorated after her husband left her for another woman in 2011 and then disappeared in September 2012. The Principal Applicant claims she attended group practice with her friend on Saturdays and also practiced daily at home.

[4] In May 2014, the Principal Applicant traveled to Japan and was required to work overtime upon her return. Consequently, she did not attend her Falun Gong practice group. On the second day after her return from Japan, the Principal Applicant says her mother-in-law telephoned to inform her that the Public Security Bureau [PSB] had arrested the other four members of her practice group and demanded the Principal Applicant report to them immediately. The Principal Applicant hid at the home of her former schoolmate; during this time, she claims the PSB continued to seek her and also threatened her parents-in-law. The Principal Applicant subsequently hired a smuggler to help her and her son flee to Canada.

[5] On August 22, 2014, the Applicants arrived in Canada and made claims for refugee protection. Their application was heard on July 11 and 26, 2016 and rejected by the Refugee Protection Division [RPD] of the IRB on August 8, 2016. The Applicants appealed the RPD’s decision to the RAD.
III. DECISION UNDER REVIEW

[6] In a Decision dated December 14, 2016, the RAD confirmed the RPD’s decision and dismissed the Applicants’ appeal.
A. Reason for Joining Falun Gong

[7] The RAD concurred with the RPD that the lack of corroborative evidence regarding the issue that prompted the Principal Applicant to join Falun Gong, namely her husband’s disappearance in 2012, called into question why she would turn to an illegal cult.
B. Practice of Falun Gong

[8] The RAD concurred with the RPD and drew a negative inference due to the inconsistency between the Principal Applicant’s Basis of Claim [BOC] form and testimony at the RPD hearing regarding the frequency of her Falun Gong practice. The RAD rejected the explanation that the inconsistency was due to incorrect instructions from her counsel’s staff because the BOC instructions were clear and the Principal Applicant had been represented by competent counsel.
C. Arrest of Four Co-Practitioners

[9] The RAD concurred with the RPD that it was not reasonable or plausible for the Principal Applicant to omit from her claim that she had asked her former schoolmate to ask about the other co-practitioners. The RAD rejected the explanation that her counsel’s staff had instructed her to omit the information because the instructions were clear to state all important information and the detainment of all her co-practitioners was an integral portion of the evidence.
D. Copy of Zhuan Falun

[10] The RAD concurred with the RPD that the inconsistency in the testimony before the RPD regarding where the Principal Applicant kept her copy of her Zhuan Falun book called into question whether she actually had a copy or ever read it. The RPD had found it was unreasonable and implausible that the Principal Applicant would read this complex book once and then cease to study it after previously testifying that she read it daily.
E. Applicant’s Residency and Place of Hiding

[11] The RAD concurred with the RPD that, on a balance of probabilities, the Principal Applicant had not been in hiding as claimed in May 2014. At the RPD hearing, the Principal Applicant had testified that she had stayed in her original residence because she could not find a hiding place, but then changed her testimony to state that she had stayed with her former schoolmate. The RPD was not satisfied with the explanation and lack of corroborative evidence in this regard and, consequently, drew a negative inference. The RAD agreed.
F. Minor Applicant’s Expulsion

[12] The RAD concurred with the RPD’s finding that the Minor Applicant was not expelled from school. The Principal Applicant claimed she did not bring up her son’s expulsion at the RPD hearing because she misunderstood the question; however, the RPD did not find any corroborative evidence that her son or any of her family members had suffered ill-effects due to her practice of Falun Gong, despite the 8 alleged visits by the PSB. Based on the lack of evidence, the RAD rejected the explanation and agreed with the RPD’s finding.
G. Summons

[13] The RAD drew a negative inference from the lack of a summons issued by the PSB for the Principal Applicant. While the PSB’s policy on the issuance of a summons was not uniform across the country, the RAD noted that it was unreasonable for the PSB to not issue a summons in circumstances where the PSB had been vigorous in pursuing the Principal Applicant by attending her family home up to 8 times and arresting all her co-practitioners, who were allegedly still in detention.
H. Exit

[14] The RAD concurred with the RPD’s findings that it was not credible or plausible for the Principal Applicant to leave China using her own passport after coming to the attention of the PSB. The RAD further concluded that this finding undermined the Principal Applicant’s credibility regarding her allegations that she was pursued by the PSB as a result of her Falun Gong practice.

[15] In reviewing the documentation, the RAD noted that the Golden Shield, China’s national security computer network, contained information about criminal fugitives and passport information as well as extensive tracking and control mechanisms. The documentation indicated that the Golden Shield was used by airport security officials and had been used to detain people who were in the database. Additionally, the documentation indicated that the Golden Shield had been used to track down Falun Gong practitioners.

[16] The RAD then quoted the Exit and Entry Administration Law of China, which requires documentation for all travel and prohibits suspects or defendants in criminal cases from exiting the country. The RAD also referred to other documentation indicating that the Chinese border authorities have implemented exit control procedures and can prevent departure with or without complete control formalities, such as reporting up the hierarchy to the High People’s Court. The documentation also states that airport travellers pass through at least four checkpoints that require the presentation of a passport before exiting. Moreover, the Chinese authorities can deny exit if a traveller does not hold valid documentation or is a suspect in a criminal case.

[17] The RAD also reviewed the Principal Applicant’s evidence of the smuggler she used to exit China and found it to be vague and lacking in detail. The RAD found it reasonable to expect that the Principal Applicant, an individual expecting to avoid arrest and detention by leaving the country, would inquire about the services provided by a smuggler, particularly because she had testified that she joined Falun Gong only after being reassured there were safety measures in place. However, the RAD also noted that its plausibility conclusion was based on recent information in the National Documentation Package for China [NDP]. The RAD found it reasonable to expect that the Golden Shield and other systems would be used to prevent the compromise of airport security controls by a single individual, such as an official bribed by a smuggler. Furthermore, the RAD found that the evidence suggested the Principal Applicant’s passport had been examined numerous times during her exit and that it was improbable that a smuggler would have known who to bribe in order to facilitate safe passage through the airport.

[18] In support of the RAD’s finding, the Decision cited the RAD decision of X (Re), 2015 CanLII 72857 (CA IRB) [X (Re)], which found it unlikely that a wanted person could depart China from an international airport using their own passport.

[19] In light of the Principal Applicant’s allegation that the PSB continued to pursue her, the RAD found it reasonable to expect the authorities would have entered her information into the Golden Shield. While corruption exists, the documentation indicates that corrupt practices occur in departments concerning the management of funds, not airport security systems. Accordingly, the RAD did not accept that the Principal Applicant could bypass all of the security controls in place.
I. Sur Place

[20] The RAD concurred with the RPD that the Principal Applicant had not provided sufficient credible evidence to establish her identity as a Falun Gong practitioner or that she was wanted by the PSB. The RAD also found that the RPD could import credibility findings from the Principal Applicant’s testimony regarding her practice in China in the determination of her sur place claim. The RAD then found that there was insufficient credible evidence to establish that the Chinese authorities would be aware of the Principal Applicant’s alleged Falun Gong activities in Canada.
IV. ISSUES

## 9900:2 · paragraphs 21-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a932ccd0812834ae02b5f69ae0a6622a5a386908982ca0883b0ba77a8a49a90d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:2:subtheme:1 · paragraphs 21-24

- Raw key terms: `standard, canada, para, review, analysis, applicable, applicants, bias`
- Display key terms: `standard, para, review, analysis, applicable, bias`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: standard, para, review, analysis, applicable, bias Position/evidence statements: [21] The Applicants submit that the following are at issue in this application: Does the RAD’s analysis give rise to a reasonable apprehension of bias and a jurisdictional error? Rule/authority context: STANDARD OF REVIEW | [22] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500367` offsets `53-58`; context: [21] The Applicants submit that the following are at issue in this application:
Does the RAD’s analysis give rise to a reasonable apprehension of bias and a jurisdictional error?
- Evidence: `party_position` cue `submit` at chunk `4500367` offsets `20-26`; context: [21] The Applicants submit that the following are at issue in this application:
Does the RAD’s analysis give rise to a reasonable apprehension of bias and a jurisdictional error?
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4500367` offsets `254-272`; context: STANDARD OF REVIEW
- Evidence: `issue` cue `question` at chunk `4500368` offsets `230-238`; context: Instead, where the standard of review applicable to a particular question before the court is settled in a satisfactory manner by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4500368` offsets `96-114`; context: [22] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance.
- Evidence: `governing_rule` cue `under` at chunk `4500369` offsets `102-107`; context: [23] Allegations of bias, if found, can give rise to a breach of procedural fairness and are reviewed under the correctness standard: Gaziova v Canada (Citizenship and Immigration), 2017 FC 679 at para 24.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500370` offsets `129-137`; context: [24] The standard of review applicable to the RAD’s factual findings regarding the Applicants’ credibility and assessment of the evidence, including an alleged deliberate omission of jurisprudence, is reasonableness: Chen v Canada (Citizenship and Immigration), 2017 FC 539 at para 19.
- Evidence: `governing_rule` cue `standard of review` at chunk `4500370` offsets `9-27`; context: [24] The standard of review applicable to the RAD’s factual findings regarding the Applicants’ credibility and assessment of the evidence, including an alleged deliberate omission of jurisprudence, is reasonableness: Chen v Canada (Citizenship and Immigration), 2017 FC 539 at para 19.

#### Section text

[21] The Applicants submit that the following are at issue in this application:
Does the RAD’s analysis give rise to a reasonable apprehension of bias and a jurisdictional error?
In the alternative, did the RAD make unreasonable credibility findings?
V. STANDARD OF REVIEW

[22] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is settled in a satisfactory manner by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless, or where the relevant precedents appear to be inconsistent with new developments in the common law principles of judicial review, must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis: Agraira v Canada (Public Safety and Emergency Preparedness), 2013 SCC 36 at para 48.

[23] Allegations of bias, if found, can give rise to a breach of procedural fairness and are reviewed under the correctness standard: Gaziova v Canada (Citizenship and Immigration), 2017 FC 679 at para 24.

[24] The standard of review applicable to the RAD’s factual findings regarding the Applicants’ credibility and assessment of the evidence, including an alleged deliberate omission of jurisprudence, is reasonableness: Chen v Canada (Citizenship and Immigration), 2017 FC 539 at para 19.

## 9900:3 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `27ba26a667974d737199aab4793dde5c6f242eadd27c514cd4f1b11571ab5aae`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:3:subtheme:1 · paragraphs 25-25

- Raw key terms: `above, acceptable, analysis, another, canada, citizenship, concerned, court`
- Display key terms: `above, acceptable, analysis, another, concerned`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: above, acceptable, analysis, another, concerned Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4500371` offsets `219-226`; context: [25] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### Section text

[25] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at para 47, and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”
VI. STATUTORY PROVISIONS

## 9900:4 · paragraphs 26-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `06ec6773e27abd9a1b3308f2031df541ecbe3f8b8060b31f62642d540066382d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:4:subtheme:1 · paragraphs 26-27

- Raw key terms: `applicants, apprehension, bias, error, jurisdictional, accepted, adequate, against`
- Display key terms: `apprehension, bias, error, jurisdictional, accepted, adequate, against`
- Argument roles: `party_position, reasoning_application`
- Explanation: Observed roles: party_position, reasoning_application Display terms: apprehension, bias, error, jurisdictional, accepted, adequate, against Position/evidence statements: [27] The Applicants submit that the Decision raises a reasonable apprehension of bias and jurisdictional error, which is in itself sufficient to warrant judicial intervention. Application context: Person in need of protection Personne à protéger 97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, th Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4500372` offsets `2314-2321`; context: Person in need of protection
Personne à protéger
97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97 (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `party_position` cue `submit` at chunk `4500373` offsets `20-26`; context: [27] The Applicants submit that the Decision raises a reasonable apprehension of bias and jurisdictional error, which is in itself sufficient to warrant judicial intervention.

#### 9900:4:subtheme:2 · paragraphs 28-30

- Raw key terms: `applicants, submit, canada, china, counsel, credibility, findings, jurisprudence`
- Display key terms: `submit, china, credibility, findings, jurisprudence`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: submit, china, credibility, findings, jurisprudence Position/evidence statements: [28] The Applicants argue that the RAD member deliberately omitted jurisprudence contradicting the finding that they would not have been able to leave China on their own passports if they were fugitives. | The Applicants submit that the RAD’s conduct creates a perception that the jurisprudence favouring the Applicants was intentionally ignored because Applicants’ counsel was unaware of the jurisprudence, thus giving rise t Rule/authority context: [28] The Applicants argue that the RAD member deliberately omitted jurisprudence contradicting the finding that they would not have been able to leave China on their own passports if they were fugitives. | The Applicants submit that the RAD’s conduct creates a perception that the jurisprudence favouring the Applicants was intentionally ignored because Applicants’ counsel was unaware of the jurisprudence, thus giving rise t Application context: [29] The test for an apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through, would conclude that it is more likely than not that the de Evidence spans paragraphs 28-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500374` offsets `494-499`; context: The Applicants submit evidence in the form of an affidavit sworn by Michael Korman, an immigration counsel, that the RAD member deciding the case was aware of jurisprudence that overturned RAD decisions where the plausibility of claimants’ exits from China using their own passports was an issue on appeal, including: Zhang v Canada (Citizenship and Immigration), 2008 FC 533 at paras 5, 9, 10 [Zhang]; Sun v Canada (Citizenship and Immigration), 2015 FC 387 at paras 13, 26 [Sun]; Ren v Canada (Citizenship and Immigration), 2015 FC 1402 at para 16 [Ren]; Yang v Canada (Citizenship and Immigration), 2016 FC 543 at paras 12-14 [Yang].
- Evidence: `party_position` cue `argue` at chunk `4500374` offsets `20-25`; context: [28] The Applicants argue that the RAD member deliberately omitted jurisprudence contradicting the finding that they would not have been able to leave China on their own passports if they were fugitives.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500374` offsets `226-234`; context: The Applicants submit evidence in the form of an affidavit sworn by Michael Korman, an immigration counsel, that the RAD member deciding the case was aware of jurisprudence that overturned RAD decisions where the plausibility of claimants’ exits from China using their own passports was an issue on appeal, including: Zhang v Canada (Citizenship and Immigration), 2008 FC 533 at paras 5, 9, 10 [Zhang]; Sun v Canada (Citizenship and Immigration), 2015 FC 387 at paras 13, 26 [Sun]; Ren v Canada (Citizenship and Immigration), 2015 FC 1402 at para 16 [Ren]; Yang v Canada (Citizenship and Immigration), 2016 FC 543 at paras 12-14 [Yang].
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500374` offsets `67-80`; context: [28] The Applicants argue that the RAD member deliberately omitted jurisprudence contradicting the finding that they would not have been able to leave China on their own passports if they were fugitives.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500374` offsets `1044-1051`; context: However, the Decision cites only X (Re), above, a decision that is not favourable to the Applicants.
- Evidence: `issue` cue `whether` at chunk `4500375` offsets `45-52`; context: [29] The test for an apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through, would conclude that it is more likely than not that the decision-maker, whether consciously or unconsciously, would not decide fairly: Committee for Justice and Liberty v Canada (National Energy Board), [1978] 1 SCR 369 at 394.
- Evidence: `party_position` cue `submit` at chunk `4500375` offsets `405-411`; context: The Applicants submit that the RAD’s conduct creates a perception that the jurisprudence favouring the Applicants was intentionally ignored because Applicants’ counsel was unaware of the jurisprudence, thus giving rise to a reasonable apprehension that the RAD member was biased.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500375` offsets `465-478`; context: The Applicants submit that the RAD’s conduct creates a perception that the jurisprudence favouring the Applicants was intentionally ignored because Applicants’ counsel was unaware of the jurisprudence, thus giving rise to a reasonable apprehension that the RAD member was biased.
- Evidence: `reasoning_application` cue `conclude` at chunk `4500375` offsets `168-176`; context: [29] The test for an apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through, would conclude that it is more likely than not that the decision-maker, whether consciously or unconsciously, would not decide fairly: Committee for Justice and Liberty v Canada (National Energy Board), [1978] 1 SCR 369 at 394.
- Evidence: `party_position` cue `submit` at chunk `4500376` offsets `40-46`; context: [30] In the alternative, the Applicants submit that the RAD made unreasonable credibility findings that warrant judicial intervention.

#### 9900:4:subtheme:3 · paragraphs 31-33

- Raw key terms: `applicants, china, above, airport, applicant, based, because, canada`
- Display key terms: `china, above, airport, based, because`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: china, above, airport, based, because Position/evidence statements: [31] In addition to the submissions on bias above, the Applicants submit that the finding on the plausibility of the Applicants exiting China on their own passports is unreasonable because it is based on the speculative  | [33] The Applicants submit that it was unreasonable for the RAD to reject their explanation for the lack of evidence concerning the Principal Applicant’s husband’s departure in 2011 and his disappearance in 2012. Rule/authority context: [32] In support of this argument, the Applicants rely on jurisprudence in which the Court has overturned decisions where the issue concerns whether an applicant could exit China via the airport on their own passports: Zh Application context: [31] In addition to the submissions on bias above, the Applicants submit that the finding on the plausibility of the Applicants exiting China on their own passports is unreasonable because it is based on the speculative  | The Principal Applicant explained that her family had not provided affidavits because they were illiterate and did not want to get involved. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4500377` offsets `477-485`; context: ” The RAD also did not question the RPD’s finding that corruption in China existed.
- Evidence: `party_position` cue `submit` at chunk `4500377` offsets `66-72`; context: [31] In addition to the submissions on bias above, the Applicants submit that the finding on the plausibility of the Applicants exiting China on their own passports is unreasonable because it is based on the speculative assumption that the smuggler could not ensure their unobstructed passage.
- Evidence: `reasoning_application` cue `because` at chunk `4500377` offsets `181-188`; context: [31] In addition to the submissions on bias above, the Applicants submit that the finding on the plausibility of the Applicants exiting China on their own passports is unreasonable because it is based on the speculative assumption that the smuggler could not ensure their unobstructed passage.
- Evidence: `issue` cue `issue` at chunk `4500378` offsets `125-130`; context: [32] In support of this argument, the Applicants rely on jurisprudence in which the Court has overturned decisions where the issue concerns whether an applicant could exit China via the airport on their own passports: Zhang; Sun; Ren; Yang, all above; and Yao v Canada (Citizenship and Immigration), 2016 FC 927 at para 9 [Yao].
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500378` offsets `57-70`; context: [32] In support of this argument, the Applicants rely on jurisprudence in which the Court has overturned decisions where the issue concerns whether an applicant could exit China via the airport on their own passports: Zhang; Sun; Ren; Yang, all above; and Yao v Canada (Citizenship and Immigration), 2016 FC 927 at para 9 [Yao].
- Evidence: `party_position` cue `submit` at chunk `4500379` offsets `20-26`; context: [33] The Applicants submit that it was unreasonable for the RAD to reject their explanation for the lack of evidence concerning the Principal Applicant’s husband’s departure in 2011 and his disappearance in 2012.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500379` offsets `108-116`; context: [33] The Applicants submit that it was unreasonable for the RAD to reject their explanation for the lack of evidence concerning the Principal Applicant’s husband’s departure in 2011 and his disappearance in 2012.
- Evidence: `reasoning_application` cue `because` at chunk `4500379` offsets `291-298`; context: The Principal Applicant explained that her family had not provided affidavits because they were illiterate and did not want to get involved.

#### Section text

[26] The following provisions of the IRPA are relevant in this application:
Convention Refugee
Définition de réfugié
96 A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96 A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
Personne à protéger
97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97 (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
VII. ARGUMENTS
A. Applicants
(1) Apprehension of Bias and Jurisdictional Error

[27] The Applicants submit that the Decision raises a reasonable apprehension of bias and jurisdictional error, which is in itself sufficient to warrant judicial intervention.

[28] The Applicants argue that the RAD member deliberately omitted jurisprudence contradicting the finding that they would not have been able to leave China on their own passports if they were fugitives. The Applicants submit evidence in the form of an affidavit sworn by Michael Korman, an immigration counsel, that the RAD member deciding the case was aware of jurisprudence that overturned RAD decisions where the plausibility of claimants’ exits from China using their own passports was an issue on appeal, including: Zhang v Canada (Citizenship and Immigration), 2008 FC 533 at paras 5, 9, 10 [Zhang]; Sun v Canada (Citizenship and Immigration), 2015 FC 387 at paras 13, 26 [Sun]; Ren v Canada (Citizenship and Immigration), 2015 FC 1402 at para 16 [Ren]; Yang v Canada (Citizenship and Immigration), 2016 FC 543 at paras 12-14 [Yang]. Mr. Korman presented the aforementioned jurisprudence to the RAD member during the representation of his own clients in prior hearings, thereby demonstrating that the RAD member knew of these decisions. However, the Decision cites only X (Re), above, a decision that is not favourable to the Applicants.

[29] The test for an apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through, would conclude that it is more likely than not that the decision-maker, whether consciously or unconsciously, would not decide fairly: Committee for Justice and Liberty v Canada (National Energy Board), [1978] 1 SCR 369 at 394. The Applicants submit that the RAD’s conduct creates a perception that the jurisprudence favouring the Applicants was intentionally ignored because Applicants’ counsel was unaware of the jurisprudence, thus giving rise to a reasonable apprehension that the RAD member was biased. Furthermore, the Applicants submit that the RAD exceeded its jurisdiction by intentionally omitting this jurisprudence and became an adversary rather than an impartial decision-maker.
(2) Credibility Findings

[30] In the alternative, the Applicants submit that the RAD made unreasonable credibility findings that warrant judicial intervention.
(a) Exit from China

[31] In addition to the submissions on bias above, the Applicants submit that the finding on the plausibility of the Applicants exiting China on their own passports is unreasonable because it is based on the speculative assumption that the smuggler could not ensure their unobstructed passage. Moreover, the RAD acknowledged “isolated incidents of successful evasion” and that “it might be possible for a smuggler to bypass some of the security controls.” The RAD also did not question the RPD’s finding that corruption in China existed. Consequently, the Applicants submit that it is not clear how it is implausible for a smuggler to evade border controls by bribing airport officials and bypassing security measures.

[32] In support of this argument, the Applicants rely on jurisprudence in which the Court has overturned decisions where the issue concerns whether an applicant could exit China via the airport on their own passports: Zhang; Sun; Ren; Yang, all above; and Yao v Canada (Citizenship and Immigration), 2016 FC 927 at para 9 [Yao].
(b) Motivation for Joining Falun Gong

[33] The Applicants submit that it was unreasonable for the RAD to reject their explanation for the lack of evidence concerning the Principal Applicant’s husband’s departure in 2011 and his disappearance in 2012. The Principal Applicant explained that her family had not provided affidavits because they were illiterate and did not want to get involved. Additionally, her friend told her to forget about the events in China and did not know how to write the contents of the letter. The Applicants submit that it is reasonable to expect that illiterate family and friends will not be able to provide written evidence, and will be reluctant about involvement in an international refugee claim against the country in which they still reside. The RAD’s finding is based on pure conjecture and is therefore unreasonable: Yu v Canada (Citizenship and Immigration), 2015 FC 167 at para 12.
(c) Summons

## 9900:5 · paragraphs 34-89

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9730e8a412dff1285afbb7f4db12a895658317583f3491d832367e0ab6029e42`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:5:subtheme:1 · paragraphs 34-35

- Raw key terms: `applicant, applicants, falun, principal, zhuan, accordingly, acknowledges, adverse`
- Display key terms: `falun, principal, zhuan, accordingly, acknowledges, adverse`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: falun, principal, zhuan, accordingly, acknowledges, adverse Position/evidence statements: Accordingly, the Applicants submit that this conclusion is arbitrary, speculative, and lacks transparency. | [35] The Applicants argue that, contrary to the RAD’s finding, the Principal Applicant’s testimony regarding the whereabouts of her Zhuan Falun book is not an omission or a contradiction. Application context: [34] The Applicants take the position that it was unreasonable for the RAD to conclude that the Principal Applicant was not credible in her allegations of pursuit by the PSB due to a lack of a summons. Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4500380` offsets `903-909`; context: Accordingly, the Applicants submit that this conclusion is arbitrary, speculative, and lacks transparency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500380` offsets `294-302`; context: The RAD acknowledges that the PSB was not consistent in issuing summonses and does not cite evidence to support its assumption that the PSB would have issued a summons in the Principal Applicant’s circumstances.
- Evidence: `reasoning_application` cue `conclude` at chunk `4500380` offsets `78-86`; context: [34] The Applicants take the position that it was unreasonable for the RAD to conclude that the Principal Applicant was not credible in her allegations of pursuit by the PSB due to a lack of a summons.
- Evidence: `party_position` cue `argue` at chunk `4500381` offsets `20-25`; context: [35] The Applicants argue that, contrary to the RAD’s finding, the Principal Applicant’s testimony regarding the whereabouts of her Zhuan Falun book is not an omission or a contradiction.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500381` offsets `89-98`; context: [35] The Applicants argue that, contrary to the RAD’s finding, the Principal Applicant’s testimony regarding the whereabouts of her Zhuan Falun book is not an omission or a contradiction.

#### 9900:5:subtheme:2 · paragraphs 36-42

- Raw key terms: `respondent, applicant, applicants, evidence, principal, reasonable, smuggler, authorities`
- Display key terms: `principal, reasonable, smuggler, authorities`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: principal, reasonable, smuggler, authorities Position/evidence statements: [36] The Applicants also submit that the RAD’s rejection of the Principal Applicant’s explanation for not raising the issue of her son’s expulsion from school is unreasonable. | [38] The Respondent submits that the RAD’s credibility findings are reasonable. Application context: She did not raise the issue because she did not know there was a misunderstanding. | Ren, on the other hand, is not applicable because the suggestion in that decision was that bribing a single individual would be sufficient in facilitating an exit from China without difficulty; in the present case, the A Evidence spans paragraphs 36-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500382` offsets `118-123`; context: [36] The Applicants also submit that the RAD’s rejection of the Principal Applicant’s explanation for not raising the issue of her son’s expulsion from school is unreasonable.
- Evidence: `party_position` cue `submit` at chunk `4500382` offsets `25-31`; context: [36] The Applicants also submit that the RAD’s rejection of the Principal Applicant’s explanation for not raising the issue of her son’s expulsion from school is unreasonable.
- Evidence: `reasoning_application` cue `because` at chunk `4500382` offsets `389-396`; context: She did not raise the issue because she did not know there was a misunderstanding.
- Evidence: `issue` cue `issue` at chunk `4500383` offsets `405-410`; context: The Applicants also take issue with the RAD’s failure to appreciate that the Chinese authorities monitor the movements of Falun Gong practitioners in Canada, as demonstrated by the documentary evidence, and use facial recognition technology to identify people of interest.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500383` offsets `81-89`; context: [37] The Applicants take the position that the RAD’s assessment of the sur place evidence was unreasonable.
- Evidence: `party_position` cue `submits` at chunk `4500384` offsets `20-27`; context: [38] The Respondent submits that the RAD’s credibility findings are reasonable.
- Evidence: `party_position` cue `submits` at chunk `4500385` offsets `20-27`; context: [39] The Respondent submits that, given the documentary evidence regarding the use and reach of the Golden Shield, it was reasonable for the RAD to find it highly unlikely that a smuggler would have prior knowledge of who to bribe in order to facilitate safe passage through the airport, particularly since the Applicants traveled on their own passports and alleged that the PSB were in continuous and vigorous pursuit.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500385` offsets `56-64`; context: [39] The Respondent submits that, given the documentary evidence regarding the use and reach of the Golden Shield, it was reasonable for the RAD to find it highly unlikely that a smuggler would have prior knowledge of who to bribe in order to facilitate safe passage through the airport, particularly since the Applicants traveled on their own passports and alleged that the PSB were in continuous and vigorous pursuit.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500386` offsets `182-190`; context: [40] The Respondent views the Applicants’ argument that the RAD should have considered the possibility that all the controls could be circumvented as an alternate inference from the evidence.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500386` offsets `192-199`; context: However, it is insufficient to demonstrate that another conclusion could have been reached; the Applicants have the onus to demonstrate that the RAD’s inferences were not supported by the evidence, which they failed to do.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500387` offsets `114-122`; context: [41] The Respondent also takes the position that the RAD was reasonable in finding that the Principal Applicant’s evidence regarding the smuggler was vague and lacking in detail.
- Evidence: `party_position` cue `argues` at chunk `4500388` offsets `33-39`; context: [42] Furthermore, the Respondent argues that the Applicants’ particular reliance on Sun and Ren, both above, are misplaced.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500388` offsets `128-136`; context: The evidence in Sun regarding information sharing is outdated as it is dated July 2009, whereas the RAD relied upon a NDP dated April 29, 2016 that indicates the Chinese authorities have expanded the breadth and complexity of the information-sharing regime and have tightened airport security.
- Evidence: `reasoning_application` cue `because` at chunk `4500388` offsets `460-467`; context: Ren, on the other hand, is not applicable because the suggestion in that decision was that bribing a single individual would be sufficient in facilitating an exit from China without difficulty; in the present case, the Applicants’ arguments imply that the smuggler could remove the Principal Applicant’s information from the Golden Shield.

#### 9900:5:subtheme:3 · paragraphs 43-45

- Raw key terms: `argues, evidence, reasonable, respondent, allegedly, applicant, canada, citizenship`
- Display key terms: `argues, reasonable, allegedly`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: argues, reasonable, allegedly Position/evidence statements: [43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using th | The Respondent also argues that the RAD’s concern was the absence of any evidence regarding her reasons for joining Falun Gong that would establish her claim, not whether her family and friends were illiterate. Rule/authority context: [43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using th Application context: [45] Given the Principal Applicant’s assertion that the PSB remained in continuous and vigorous pursuit of her, the Respondent submits that it was reasonable for the RAD to conclude that a summons likely would have been  Evidence spans paragraphs 43-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500389` offsets `98-103`; context: [43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using their own passport.
- Evidence: `party_position` cue `argues` at chunk `4500389` offsets `25-31`; context: [43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using their own passport.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500389` offsets `337-345`; context: Each decision must be based on the facts of each case, the analysis conducted, and the documentary evidence before the tribunal.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500389` offsets `41-54`; context: [43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using their own passport.
- Evidence: `issue` cue `question` at chunk `4500390` offsets `302-310`; context: As this was the reason she allegedly began practicing Falun Gong, it was reasonable for the RAD to concur with the RPD that the lack of corroborative evidence called into question the Principal Applicant’s motives for practicing Falun Gong.
- Evidence: `party_position` cue `argues` at chunk `4500390` offsets `392-398`; context: The Respondent also argues that the RAD’s concern was the absence of any evidence regarding her reasons for joining Falun Gong that would establish her claim, not whether her family and friends were illiterate.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500390` offsets `74-82`; context: [44] Despite the RPD’s request, the Principal Applicant failed to provide evidence to support her husband’s disappearance in 2012.
- Evidence: `party_position` cue `submits` at chunk `4500391` offsets `127-134`; context: [45] Given the Principal Applicant’s assertion that the PSB remained in continuous and vigorous pursuit of her, the Respondent submits that it was reasonable for the RAD to conclude that a summons likely would have been issued if the allegations were true, even though the PSB’s policy on the issuance of summonses may not be uniform across China.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500391` offsets `443-451`; context: As in Lan Cao v Canada (Citizenship and Immigration), 2012 FC 1398 at para 35, the documentary evidence did not directly contradict the RAD’s finding in this regard.
- Evidence: `reasoning_application` cue `conclude` at chunk `4500391` offsets `173-181`; context: [45] Given the Principal Applicant’s assertion that the PSB remained in continuous and vigorous pursuit of her, the Respondent submits that it was reasonable for the RAD to conclude that a summons likely would have been issued if the allegations were true, even though the PSB’s policy on the issuance of summonses may not be uniform across China.

#### 9900:5:subtheme:4 · paragraphs 46-47

- Raw key terms: `falun, issue, respondent, zhuan, applicant, based, because, book`
- Display key terms: `falun, zhuan, based, because, book`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: falun, zhuan, based, because, book Position/evidence statements: [46] Nonetheless, the Respondent submits that this issue is not determinative as there were other inconsistencies. Application context: The RAD rejected the explanation that she had hidden the book after finishing it because she had omitted her completion of the book and because the book was complex. Operative outcome context: The RAD’s credibility finding was based on the totality of the discrepancies; as such, even if this is an error the Decision may still be upheld: Nyathi v Canada (Minister of Citizenship and Immigration), 2003 FC 1119 at Evidence spans paragraphs 46-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500392` offsets `51-56`; context: [46] Nonetheless, the Respondent submits that this issue is not determinative as there were other inconsistencies.
- Evidence: `party_position` cue `submits` at chunk `4500392` offsets `33-40`; context: [46] Nonetheless, the Respondent submits that this issue is not determinative as there were other inconsistencies.
- Evidence: `disposition` cue `upheld` at chunk `4500392` offsets `253-259`; context: The RAD’s credibility finding was based on the totality of the discrepancies; as such, even if this is an error the Decision may still be upheld: Nyathi v Canada (Minister of Citizenship and Immigration), 2003 FC 1119 at para 18.
- Evidence: `issue` cue `issue` at chunk `4500393` offsets `644-649`; context: Given the Principal Applicant’s testimony that she read the book daily in China, it was reasonable for the RAD to make its findings on this issue.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500393` offsets `48-57`; context: [47] The Respondent takes the position that the testimony regarding the location of the Zhuan Falun book contains an inconsistency.
- Evidence: `reasoning_application` cue `because` at chunk `4500393` offsets `419-426`; context: The RAD rejected the explanation that she had hidden the book after finishing it because she had omitted her completion of the book and because the book was complex.

#### 9900:5:subtheme:5 · paragraphs 48-50

- Raw key terms: `reasonable, respondent, applicant, applicants, apprehension, bias, finding, principal`
- Display key terms: `reasonable, apprehension, bias, finding, principal`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: reasonable, apprehension, bias, finding, principal Position/evidence statements: The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the  | [49] The Respondent submits that it was reasonable for the RAD to make a negative credibility finding based on a number of inconsistencies, some of which have not been challenged by the Applicants. Application context: The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the  Evidence spans paragraphs 48-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500394` offsets `451-456`; context: The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the RAD to consider the explanation to determine whether it was sufficient and the Court should not re-weigh the evidence: Ma v Canada (Citizenship and Immigration), 2011 FC 417 at para 39.
- Evidence: `party_position` cue `submits` at chunk `4500394` offsets `411-418`; context: The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the RAD to consider the explanation to determine whether it was sufficient and the Court should not re-weigh the evidence: Ma v Canada (Citizenship and Immigration), 2011 FC 417 at para 39.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500394` offsets `39-47`; context: [48] In the Decision, the RAD found no evidence that family members had incurred any harm or threats, which, combined with the Principal Applicant’s failure to bring forth her son’s alleged expulsion from school at the RPD hearing, supported the finding that the Minor Applicant had not been expelled.
- Evidence: `reasoning_application` cue `because` at chunk `4500394` offsets `472-479`; context: The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the RAD to consider the explanation to determine whether it was sufficient and the Court should not re-weigh the evidence: Ma v Canada (Citizenship and Immigration), 2011 FC 417 at para 39.
- Evidence: `party_position` cue `submits` at chunk `4500395` offsets `20-27`; context: [49] The Respondent submits that it was reasonable for the RAD to make a negative credibility finding based on a number of inconsistencies, some of which have not been challenged by the Applicants.
- Evidence: `party_position` cue `argues` at chunk `4500396` offsets `20-26`; context: [50] The Respondent argues that the Applicants have not met the high standard required to establish a reasonable apprehension of bias.

#### 9900:5:subtheme:6 · paragraphs 51-52

- Raw key terms: `above, chinese, evidence, para, regarding, ability, airport, allegations`
- Display key terms: `above, chinese, para, regarding, ability, airport, allegations`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, chinese, para, regarding, ability, airport, allegations Rule/authority context: Moreover, the RAD member in question found that the jurisprudence of Zhang, Ren, and Sun, all above, was inapplicable in both RAD decisions because they were based on dated documentary evidence with limited information o Application context: Moreover, the RAD member in question found that the jurisprudence of Zhang, Ren, and Sun, all above, was inapplicable in both RAD decisions because they were based on dated documentary evidence with limited information o Operative outcome context: While there are cases in which the Court has disagreed with the RAD’s findings regarding an applicant’s ability to leave China, there are also cases where the Court has upheld those findings. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4500397` offsets `632-638`; context: Each decision is fact-specific and the Decision demonstrates the RAD’s grasp of the relevant issues and evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500397` offsets `643-651`; context: Each decision is fact-specific and the Decision demonstrates the RAD’s grasp of the relevant issues and evidence.
- Evidence: `disposition` cue `upheld` at chunk `4500397` offsets `516-522`; context: While there are cases in which the Court has disagreed with the RAD’s findings regarding an applicant’s ability to leave China, there are also cases where the Court has upheld those findings.
- Evidence: `issue` cue `issue` at chunk `4500398` offsets `53-58`; context: [52] Second, the Applicants’ argument regarding this issue effectively disputes the RAD’s weighing of the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500398` offsets `106-114`; context: [52] Second, the Applicants’ argument regarding this issue effectively disputes the RAD’s weighing of the evidence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500398` offsets `377-390`; context: Moreover, the RAD member in question found that the jurisprudence of Zhang, Ren, and Sun, all above, was inapplicable in both RAD decisions because they were based on dated documentary evidence with limited information on the Golden Shield and Chinese border controls.
- Evidence: `reasoning_application` cue `because` at chunk `4500398` offsets `465-472`; context: Moreover, the RAD member in question found that the jurisprudence of Zhang, Ren, and Sun, all above, was inapplicable in both RAD decisions because they were based on dated documentary evidence with limited information on the Golden Shield and Chinese border controls.

#### 9900:5:subtheme:7 · paragraphs 53-54

- Raw key terms: `applicants, constitute, evidence, activities, additionally, alleged, appear, applicant`
- Display key terms: `constitute, activities, additionally, alleged, appear`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: constitute, activities, additionally, alleged, appear Position/evidence statements: [53] The Respondent submits the RAD’s assessment of the sur place claim is reasonable. | [54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence. Rule/authority context: [54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence. Application context: Given the credibility issues, it was reasonable for the RAD to find the Principal Applicant would not be perceived as a Falun Gong practitioner and, therefore, would not be pursued by the PSB. Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4500399` offsets `554-560`; context: Given the credibility issues, it was reasonable for the RAD to find the Principal Applicant would not be perceived as a Falun Gong practitioner and, therefore, would not be pursued by the PSB.
- Evidence: `party_position` cue `submits` at chunk `4500399` offsets `20-27`; context: [53] The Respondent submits the RAD’s assessment of the sur place claim is reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500399` offsets `286-294`; context: The RAD did not dismiss the claim on the basis that the Principal Applicant was not a genuine Falun Gong practitioner; instead, the RAD found the Applicants had failed to present sufficient credible evidence that the Principal Applicant’s alleged Falun Gong activities in Canada had come to the attention of the Chinese authorities.
- Evidence: `reasoning_application` cue `therefore` at chunk `4500399` offsets `681-690`; context: Given the credibility issues, it was reasonable for the RAD to find the Principal Applicant would not be perceived as a Falun Gong practitioner and, therefore, would not be pursued by the PSB.
- Evidence: `party_position` cue `argue` at chunk `4500400` offsets `20-25`; context: [54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500400` offsets `177-185`; context: [54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500400` offsets `82-95`; context: [54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence.

#### 9900:5:subtheme:8 · paragraphs 55-57

- Raw key terms: `applicants, respondent, above, additionally, based, china, court, decisions`
- Display key terms: `above, additionally, based, china, decisions`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: above, additionally, based, china, decisions Position/evidence statements: [56] Contrary to the Respondent’s submission, the Applicants submit that Ren and Sun, both above, are not distinguishable. | [57] The Applicants reiterate that the explanation for the lack of corroborative evidence regarding the disappearance of the Principal Applicant’s husband in 2012 is not implausible and argue that the Respondent’s positi Application context: Additionally, in Ren, the RPD relied on and cited from the same document regarding the Golden Shield that is cited in the Decision; accordingly, the Court’s decision dealt with the same evidence that is at issue in the p Operative outcome context: [55] Additionally, the Applicants disagree that the RAD member’s omission of Zhang, Ren and Sun, all above, in previous RAD decisions is immaterial; these RAD decisions have been granted leave for judicial review before  Evidence spans paragraphs 55-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500401` offsets `249-254`; context: [55] Additionally, the Applicants disagree that the RAD member’s omission of Zhang, Ren and Sun, all above, in previous RAD decisions is immaterial; these RAD decisions have been granted leave for judicial review before this Court based on the same issue.
- Evidence: `disposition` cue `granted` at chunk `4500401` offsets `179-186`; context: [55] Additionally, the Applicants disagree that the RAD member’s omission of Zhang, Ren and Sun, all above, in previous RAD decisions is immaterial; these RAD decisions have been granted leave for judicial review before this Court based on the same issue.
- Evidence: `issue` cue `issue` at chunk `4500402` offsets `511-516`; context: Additionally, in Ren, the RPD relied on and cited from the same document regarding the Golden Shield that is cited in the Decision; accordingly, the Court’s decision dealt with the same evidence that is at issue in the present case.
- Evidence: `party_position` cue `submit` at chunk `4500402` offsets `61-67`; context: [56] Contrary to the Respondent’s submission, the Applicants submit that Ren and Sun, both above, are not distinguishable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500402` offsets `175-183`; context: In both decisions, as in the present case, the only evidence regarding what the smuggler did for the applicants was that bribes were paid to officials: Ren at para 6; Sun at para 8.
- Evidence: `reasoning_application` cue `accordingly` at chunk `4500402` offsets `437-448`; context: Additionally, in Ren, the RPD relied on and cited from the same document regarding the Golden Shield that is cited in the Decision; accordingly, the Court’s decision dealt with the same evidence that is at issue in the present case.
- Evidence: `party_position` cue `argue` at chunk `4500403` offsets `186-191`; context: [57] The Applicants reiterate that the explanation for the lack of corroborative evidence regarding the disappearance of the Principal Applicant’s husband in 2012 is not implausible and argue that the Respondent’s position on this matter is without merit.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500403` offsets `81-89`; context: [57] The Applicants reiterate that the explanation for the lack of corroborative evidence regarding the disappearance of the Principal Applicant’s husband in 2012 is not implausible and argue that the Respondent’s position on this matter is without merit.

#### 9900:5:subtheme:9 · paragraphs 58-61

- Raw key terms: `applicants, applicant, evidence, falun, principal, argue, authorities, canada`
- Display key terms: `falun, principal, argue, authorities`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: falun, principal, argue, authorities Position/evidence statements: [58] The Applicants disagree with the Respondent on this issue and argue that there is no evidence whatsoever to suggest that the Chinese authorities serve summonses on criminal suspects, their family members, or even no | [60] The Applicants argue that the RAD’s finding that the Principal Applicant should have brought forth the subject of her son’s expulsion at the RPD hearing is illogical because she did not know there was a misunderstan Application context: [60] The Applicants argue that the RAD’s finding that the Principal Applicant should have brought forth the subject of her son’s expulsion at the RPD hearing is illogical because she did not know there was a misunderstan Evidence spans paragraphs 58-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500404` offsets `57-62`; context: [58] The Applicants disagree with the Respondent on this issue and argue that there is no evidence whatsoever to suggest that the Chinese authorities serve summonses on criminal suspects, their family members, or even notify suspects or family members of the existence of a summons.
- Evidence: `party_position` cue `argue` at chunk `4500404` offsets `67-72`; context: [58] The Applicants disagree with the Respondent on this issue and argue that there is no evidence whatsoever to suggest that the Chinese authorities serve summonses on criminal suspects, their family members, or even notify suspects or family members of the existence of a summons.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500404` offsets `90-98`; context: [58] The Applicants disagree with the Respondent on this issue and argue that there is no evidence whatsoever to suggest that the Chinese authorities serve summonses on criminal suspects, their family members, or even notify suspects or family members of the existence of a summons.
- Evidence: `evidence_fact` cue `testimony` at chunk `4500405` offsets `76-85`; context: [59] The Applicants reiterate their argument that the Principal Applicant’s testimony regarding the location of the Zhuan Falun book is not inconsistent.
- Evidence: `party_position` cue `argue` at chunk `4500406` offsets `20-25`; context: [60] The Applicants argue that the RAD’s finding that the Principal Applicant should have brought forth the subject of her son’s expulsion at the RPD hearing is illogical because she did not know there was a misunderstanding at that time.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500406` offsets `289-297`; context: Furthermore, the failure to provide corroborative evidence on this matter does not justify a rejection of the Principal Applicant’s explanation; corroborative evidence is not required for refugee claimants and the RAD cannot disbelieve claimants merely due to its absence or make negative credibility findings in the absence of evidence to contradict such allegations: Ahortor v Canada (Minister of Employment and Immigration), [1993] FCJ No 705 at para 45.
- Evidence: `reasoning_application` cue `because` at chunk `4500406` offsets `171-178`; context: [60] The Applicants argue that the RAD’s finding that the Principal Applicant should have brought forth the subject of her son’s expulsion at the RPD hearing is illogical because she did not know there was a misunderstanding at that time.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4500406` offsets `457-463`; context: Furthermore, the failure to provide corroborative evidence on this matter does not justify a rejection of the Principal Applicant’s explanation; corroborative evidence is not required for refugee claimants and the RAD cannot disbelieve claimants merely due to its absence or make negative credibility findings in the absence of evidence to contradict such allegations: Ahortor v Canada (Minister of Employment and Immigration), [1993] FCJ No 705 at para 45.
- Evidence: `party_position` cue `submit` at chunk `4500407` offsets `20-26`; context: [61] The Applicants submit that the evidence submitted to establish the sur place claim consisted of more than just photos of the Principal Applicant practicing Falun Gong publicly in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500407` offsets `36-44`; context: [61] The Applicants submit that the evidence submitted to establish the sur place claim consisted of more than just photos of the Principal Applicant practicing Falun Gong publicly in Canada.

#### 9900:5:subtheme:10 · paragraphs 62-63

- Raw key terms: `applicant, applicants, because, china, credibility, failed, findings, left`
- Display key terms: `because, china, credibility, failed, findings, left`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: because, china, credibility, failed, findings, left Rule/authority context: [63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security m Application context: [62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result. | [63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security m Operative outcome context: [62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result. Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4500408` offsets `339-345`; context: ” This amounts to a general adverse credibility finding that is based upon a series of negative inferences related to key issues in the Applicants’ claim for protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500408` offsets `102-110`; context: [62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result.
- Evidence: `reasoning_application` cue `because` at chunk `4500408` offsets `46-53`; context: [62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4500408` offsets `785-797`; context: Nevertheless, as the Respondent concedes, “it was the totality of these findings that led the RAD to conclude that the [Principal Applicant] was not credible with respect to her allegations of FG practice in China.
- Evidence: `disposition` cue `dismissed` at chunk `4500408` offsets `13-22`; context: [62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result.
- Evidence: `issue` cue `issue` at chunk `4500409` offsets `362-367`; context: [63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security measures in place at the airport, and that indeed the RAD went so far as to demonstrate a reasonable apprehension of bias in dealing with this issue because it failed to reference and apply supporting jurisprudence of which the RAD member was aware, but of which Applicants’ counsel was not.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500409` offsets `420-433`; context: [63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security measures in place at the airport, and that indeed the RAD went so far as to demonstrate a reasonable apprehension of bias in dealing with this issue because it failed to reference and apply supporting jurisprudence of which the RAD member was aware, but of which Applicants’ counsel was not.
- Evidence: `reasoning_application` cue `because` at chunk `4500409` offsets `368-375`; context: [63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security measures in place at the airport, and that indeed the RAD went so far as to demonstrate a reasonable apprehension of bias in dealing with this issue because it failed to reference and apply supporting jurisprudence of which the RAD member was aware, but of which Applicants’ counsel was not.

#### 9900:5:subtheme:11 · paragraphs 64-65

- Raw key terms: `addition, allegation, alleged, analysis, apparatus, appellant, attention, authorities`
- Display key terms: `addition, allegation, alleged, analysis, apparatus, appellant, attention, authorities`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: addition, allegation, alleged, analysis, apparatus, appellant, attention, authorities Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500410` offsets `82-87`; context: [64] The RAD devotes considerable attention (paras 22-42 of the Decision) to this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500411` offsets `24-32`; context: [36] The RAD finds that evidence reveals that the Golden Shield system is an intensive security apparatus that is far-reaching and encompassing.

#### 9900:5:subtheme:12 · paragraphs 66-71

- Raw key terms: `china, appellant, evidence, finds, airport, highly, information, passport`
- Display key terms: `china, appellant, finds, airport, highly, information, passport`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: china, appellant, finds, airport, highly, information, passport Application context: The RAD further finds that this undermines the credibility of the Appellant’s allegations that she was being pursued by the PSB because of her Falun Gong activities. Evidence spans paragraphs 66-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4500412` offsets `1124-1131`; context: With respect to flights into the country, it appears that China maintains a “stop list,” which bars the passenger from boarding the aircraft; however, the NDP remains silent on whether a similar list exists for outbound flights.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500412` offsets `33-41`; context: [37] The RAD also notes that the evidence suggests that the Appellant’s passport was examined numerous times.
- Evidence: `counterargument_limitation` cue `however` at chunk `4500412` offsets `1089-1096`; context: With respect to flights into the country, it appears that China maintains a “stop list,” which bars the passenger from boarding the aircraft; however, the NDP remains silent on whether a similar list exists for outbound flights.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500414` offsets `36-44`; context: [39] The RAD is aware that there is evidence in the record which establishes that there is corruption in China.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500414` offsets `112-119`; context: However, the RAD notes that the very comprehensive Australian Refugee Review Tribunal Background paper on official Corruption in China and the other objective evidence in the record makes no mention that corruption extends to the airport security apparatus.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500415` offsets `45-53`; context: [40] The RAD does not accept the Appellant’s evidence as credible with respect to her passage through an international airport, while wanted by the PSB.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500417` offsets `48-56`; context: [42] After its own review and assessment of the evidence, the RAD agrees with the RPD’s findings and does not find it credible or plausible that the Appellant was able to leave China on her own passport after coming to the attention of the PSB.
- Evidence: `reasoning_application` cue `because` at chunk `4500417` offsets `373-380`; context: The RAD further finds that this undermines the credibility of the Appellant’s allegations that she was being pursued by the PSB because of her Falun Gong activities.

#### 9900:5:subtheme:13 · paragraphs 72-76

- Raw key terms: `officials, able, airport, canada, china, computer, evidence, wanted`
- Display key terms: `officials, able, airport, china, computer, wanted`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: officials, able, airport, china, computer, wanted Rule/authority context: The standard of review applicable is, therefore, correctness. Application context: The standard of review applicable is, therefore, correctness. Evidence spans paragraphs 72-76. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500418` offsets `61-66`; context: [65] The Applicants’ criticism of the RAD’s handling of this issue is detailed and nuanced and deserves to be quoted in full:
6.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500418` offsets `2188-2196`; context: The evidence before the Court reveals that the RAD Member was aware of the Court’s contradictory jurisprudence.
- Evidence: `governing_rule` cue `standard of review` at chunk `4500418` offsets `285-303`; context: The standard of review applicable is, therefore, correctness.
- Evidence: `reasoning_application` cue `therefore` at chunk `4500418` offsets `319-328`; context: The standard of review applicable is, therefore, correctness.
- Evidence: `counterargument_limitation` cue `however` at chunk `4500418` offsets `2036-2043`; context: The problem, however, is that the RAD knowingly omitted to mention the recent body of binding Federal Court jurisprudence contradicting the finding in X(Re).
- Evidence: `evidence_fact` cue `testimony` at chunk `4500419` offsets `162-171`; context: Zhang’s testimony that, while she went through three security checkpoints at the Beijing airport, her snakehead had told her that her name was not “put through” the computer and that he had bribed “the customs.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4500419` offsets `713-721`; context: Although the People’s Republic of China does have a problem with corruption, I do not find it plausible that the smuggler would be able to bribe possibly hundreds of officials, as there would be no guarantee as to which border police would be on duty or as to which line the claimant (and smuggler) would be directed to.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500422` offsets `21-29`; context: [11] In view of this evidence, the Board engaged in speculation when it concluded that possibly hundreds of officials had to be bribed.

#### 9900:5:subtheme:14 · paragraphs 77-81

- Raw key terms: `applicant, china, leave, passport, able, evidence, exit, explanation`
- Display key terms: `china, leave, passport, able, exit, explanation`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: china, leave, passport, able, exit, explanation Application context: In light of the fact that the Board itself recognized that bribery is prevalent and that it is possible that information would not be effectively shared, the Board was not entitled to conclude that the Applicant’s story  Evidence spans paragraphs 77-81. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4500423` offsets `352-360`; context: Although recognizing that bribery is prevalent in China, the Board did not accept the explanation that the smuggler had bribed a customs agent, noting that if the PSB had been so intent on arresting him, then he would have been arrested regardless of a single bribe.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500424` offsets `1746-1754`; context: It was equally entirely speculative to find that the Applicant could not plausibly have travelled through China to apply for a US visa without being detected; this finding does not rest on any evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4500424` offsets `1501-1509`; context: In light of the fact that the Board itself recognized that bribery is prevalent and that it is possible that information would not be effectively shared, the Board was not entitled to conclude that the Applicant’s story is implausible.
- Evidence: `evidence_fact` cue `found that` at chunk `4500425` offsets `495-505`; context: Justice Phelan found that:
- Evidence: `evidence_fact` cue `evidence` at chunk `4500426` offsets `151-159`; context: There was no evidence that one had to bribe every official in the “chain of departure”.
- Evidence: `counterargument_limitation` cue `but` at chunk `4500426` offsets `367-370`; context: The decision does not address the Applicant’s evidence that the customs officer did not scan her passport or type anything into the computer but merely stamped the passport.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500427` offsets `99-107`; context: [13] Before finding it implausible to exit China, the RAD (and RPP) had to address the Applicant’s evidence.

#### 9900:5:subtheme:15 · paragraphs 82-83

- Raw key terms: `airport, always, applicant, apply, authorities, because, china, conduct`
- Display key terms: `airport, always, apply, authorities, because, china, conduct`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: airport, always, apply, authorities, because, china, conduct Position/evidence statements: The applicant submitted that this was possible because the smuggler made arrangements for him, but the RPD found the preponderance of documentary evidence stating that airport authorities conduct thorough screening of pa Rule/authority context: This deliberate omission of relevant and contradictory jurisprudence is troubling. Application context: 1 They were, therefore, clearly known to the RAD Member. | The applicant submitted that this was possible because the smuggler made arrangements for him, but the RPD found the preponderance of documentary evidence stating that airport authorities conduct thorough screening of pa Operative outcome context: It is respectfully requested that this Application be allowed on this basis alone. Evidence spans paragraphs 82-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500428` offsets `2072-2077`; context: The issue of the Applicants’ exit from China has already been canvassed above.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500428` offsets `26-34`; context: [14] There was sufficient evidence of corruption of officials and a bribery scheme that the RAD had to explain why it was not reasonable that such occurred in this case.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500428` offsets `744-757`; context: This deliberate omission of relevant and contradictory jurisprudence is troubling.
- Evidence: `reasoning_application` cue `therefore` at chunk `4500428` offsets `557-566`; context: 1 They were, therefore, clearly known to the RAD Member.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500428` offsets `2147-2154`; context: However, in addition to the reasonable apprehension of bias created by the RAD’s assessment of this issue, the RAD’s finding that the Applicant could not plausibly have circumvented China’s border security measures while using her own passport was also unreasonable.
- Evidence: `disposition` cue `allowed` at chunk `4500428` offsets `1663-1670`; context: It is respectfully requested that this Application be allowed on this basis alone.
- Evidence: `party_position` cue `submitted` at chunk `4500429` offsets `161-170`; context: The applicant submitted that this was possible because the smuggler made arrangements for him, but the RPD found the preponderance of documentary evidence stating that airport authorities conduct thorough screening of passengers to be more convincing.
- Evidence: `evidence_fact` cue `found that` at chunk `4500429` offsets `12-22`; context: [9] The RPD found that the applicant’s ability to pass through the airport without difficulty supported the finding that his passport was genuine.
- Evidence: `reasoning_application` cue `because` at chunk `4500429` offsets `194-201`; context: The applicant submitted that this was possible because the smuggler made arrangements for him, but the RPD found the preponderance of documentary evidence stating that airport authorities conduct thorough screening of passengers to be more convincing.
- Evidence: `counterargument_limitation` cue `but` at chunk `4500429` offsets `242-245`; context: The applicant submitted that this was possible because the smuggler made arrangements for him, but the RPD found the preponderance of documentary evidence stating that airport authorities conduct thorough screening of passengers to be more convincing.

#### 9900:5:subtheme:16 · paragraphs 84-85

- Raw key terms: `applicants, arrest, case, china, court, even, evidence, findings`
- Display key terms: `arrest, case, china, even, findings`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: arrest, case, china, even, findings Position/evidence statements: The RAD’s unreasonable determination on this issue was fatal to the Applicants’ entire claim and is, therefore, sufficient to warrant the Court’s intervention. | The Applicants argue that the RAD should have entertained the possibility that the smuggler could have circumvented all the security measures and, everyone at the checkpoints. Application context: [18] I note here that the RPD even acknowledged systematic corruption in China and the fact that regulations are not always applied evenly. | The Applicants’ arguments on this issue should, therefore, be dismissed. Operative outcome context: The Applicants’ arguments on this issue should, therefore, be dismissed. Evidence spans paragraphs 84-85. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500430` offsets `528-533`; context: The RAD’s unreasonable determination on this issue was fatal to the Applicants’ entire claim and is, therefore, sufficient to warrant the Court’s intervention.
- Evidence: `party_position` cue `claim` at chunk `4500430` offsets `570-575`; context: The RAD’s unreasonable determination on this issue was fatal to the Applicants’ entire claim and is, therefore, sufficient to warrant the Court’s intervention.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500430` offsets `306-314`; context: In my view, the evidence did not support such a belief.
- Evidence: `reasoning_application` cue `applied` at chunk `4500430` offsets `124-131`; context: [18] I note here that the RPD even acknowledged systematic corruption in China and the fact that regulations are not always applied evenly.
- Evidence: `issue` cue `issue` at chunk `4500431` offsets `1118-1123`; context: The Applicants’ arguments on this issue should, therefore, be dismissed.
- Evidence: `party_position` cue `argue` at chunk `4500431` offsets `140-145`; context: The Applicants argue that the RAD should have entertained the possibility that the smuggler could have circumvented all the security measures and, everyone at the checkpoints.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500431` offsets `580-588`; context: However, in assessing the reasonableness of a decision-maker’s credibility findings, it is not sufficient for the Applicant to demonstrate that different conclusions could have been reached on the evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `4500431` offsets `1132-1141`; context: The Applicants’ arguments on this issue should, therefore, be dismissed.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500431` offsets `383-390`; context: However, in assessing the reasonableness of a decision-maker’s credibility findings, it is not sufficient for the Applicant to demonstrate that different conclusions could have been reached on the evidence.
- Evidence: `disposition` cue `dismissed` at chunk `4500431` offsets `1146-1155`; context: The Applicants’ arguments on this issue should, therefore, be dismissed.

#### 9900:5:subtheme:17 · paragraphs 86-87

- Raw key terms: `based, canada, citizenship, findings, immigration, regard, above, acted`
- Display key terms: `based, findings, regard, above, acted`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: based, findings, regard, above, acted Rule/authority context: [67] I agree with the Respondent that the RAD’s negative findings are based upon factual conclusions and are not driven by a reliance on X (Re), above, to the exclusion of other jurisprudence. Application context: In my view, the RAD acted reasonably in this respect because the country condition information before this RAD was more up to date and was not before the Court in the earlier decisions, specifically in regard to China’s  Evidence spans paragraphs 86-87. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500432` offsets `272-277`; context: This does not mean, of course, that other jurisprudence is not relevant to the issue of whether the RAD’s factual conclusions are reasonable.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500432` offsets `178-191`; context: [67] I agree with the Respondent that the RAD’s negative findings are based upon factual conclusions and are not driven by a reliance on X (Re), above, to the exclusion of other jurisprudence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500433` offsets `50-58`; context: [20] The RAD reviewed the most recent documentary evidence and noted the fact of corruption in China.
- Evidence: `reasoning_application` cue `because` at chunk `4500433` offsets `470-477`; context: In my view, the RAD acted reasonably in this respect because the country condition information before this RAD was more up to date and was not before the Court in the earlier decisions, specifically in regard to China’s exit controls and the Golden Shield.

#### 9900:5:subtheme:18 · paragraphs 88-89

- Raw key terms: `above, applicant, applicants, apply, case, checkpoint, china, concern`
- Display key terms: `above, apply, case, checkpoint, china, concern`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, apply, case, checkpoint, china, concern Rule/authority context: I don’t see anything vague about this evidence and the Principal Applicant does not appear to have been asked for any more detail than she gave; d) The RAD cites its previous decision in X (Re), above, to support its con Application context: ” This is an exercise in wilful blindness given the fact that the RPD found that “there is systemic corruption in China and airport officials can be bribed” and “authorities in China do not always apply regulations evenl | She was asked why she did not apply for the visa herself and she replied that she was in hiding and the PSB was looking for her. Evidence spans paragraphs 88-89. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500434` offsets `116-121`; context: The issue for the Court is solely that of reasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500434` offsets `472-480`; context: As in Yang, above, “There was sufficient evidence of corruption of officials and a bribery scheme that the RAD had to explain why it was not reasonable that such occurred in this case.
- Evidence: `reasoning_application` cue `apply` at chunk `4500434` offsets `1098-1103`; context: ” This is an exercise in wilful blindness given the fact that the RPD found that “there is systemic corruption in China and airport officials can be bribed” and “authorities in China do not always apply regulations evenly.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4500434` offsets `2070-2082`; context: ” Nevertheless, the RAD acknowledged “isolated incidents of successful evasion” and neglects the warnings in Ren, and Zhang, both above, that “one official with access to the computer system would be sufficient.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500435` offsets `45-53`; context: [34] The RAD also finds that the Appellant’s evidence of the smuggler was vague and lacking detail.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4500435` offsets `1873-1886`; context: I don’t see anything vague about this evidence and the Principal Applicant does not appear to have been asked for any more detail than she gave;
d) The RAD cites its previous decision in X (Re), above, to support its conclusions of implausibility but neglects to address Federal Court jurisprudence in such cases as Zhang, Sun, Ren, Yang, and Yao, all above, that conflicts with at least some of the RAD’s conclusions in this case.
- Evidence: `reasoning_application` cue `apply` at chunk `4500435` offsets `1187-1192`; context: She was asked why she did not apply for the visa herself and she replied that she was in hiding and the PSB was looking for her.
- Evidence: `counterargument_limitation` cue `but` at chunk `4500435` offsets `1835-1838`; context: I don’t see anything vague about this evidence and the Principal Applicant does not appear to have been asked for any more detail than she gave;
d) The RAD cites its previous decision in X (Re), above, to support its conclusions of implausibility but neglects to address Federal Court jurisprudence in such cases as Zhang, Sun, Ren, Yang, and Yao, all above, that conflicts with at least some of the RAD’s conclusions in this case.

#### Section text

[34] The Applicants take the position that it was unreasonable for the RAD to conclude that the Principal Applicant was not credible in her allegations of pursuit by the PSB due to a lack of a summons. The RAD acknowledges that the PSB was not consistent in issuing summonses and does not cite evidence to support its assumption that the PSB would have issued a summons in the Principal Applicant’s circumstances. Moreover, this Court has found if the norm in an applicant’s region is for the PSB to not leave a summons, then the norm is presumed to be followed regardless of the number of visits from the PSB: Liang v Canada (Citizenship and Immigration), 2011 FC 65 at paras 13-14 [Liang]. Furthermore, even if a summons had been issued, there is no evidence that the Principal Applicant would be aware of it since her family and friends would not necessarily be notified. Accordingly, the Applicants submit that this conclusion is arbitrary, speculative, and lacks transparency.
(d) Copy of Zhuan Falun

[35] The Applicants argue that, contrary to the RAD’s finding, the Principal Applicant’s testimony regarding the whereabouts of her Zhuan Falun book is not an omission or a contradiction. The Principal Applicant had stated that she read the book every day; later, she stated that she hid the book after she finished reading it. This is neither inconsistent nor an omission and is not a basis for an adverse credibility finding.
(e) Minor Applicant’s Expulsion

[36] The Applicants also submit that the RAD’s rejection of the Principal Applicant’s explanation for not raising the issue of her son’s expulsion from school is unreasonable. The Principal Applicant misunderstood the question and thought she was asked whether her son had ever attended school, not whether he attended after the PSB began their pursuit of her. She did not raise the issue because she did not know there was a misunderstanding.
(f) Sur Place

[37] The Applicants take the position that the RAD’s assessment of the sur place evidence was unreasonable. By the time the analysis reached the sur place submissions, the RAD had already determined the Principal Applicant was not credible and her allegations were false, thereby tainting the sur place analysis: Liu v Canada (Citizenship and Immigration), 2014 FC 972 at para 8. The Applicants also take issue with the RAD’s failure to appreciate that the Chinese authorities monitor the movements of Falun Gong practitioners in Canada, as demonstrated by the documentary evidence, and use facial recognition technology to identify people of interest. This evidence, in conjunction with the fact that the PSB has the Principal Applicant’s photograph from her resident identity card, demonstrates more than the mere possibility that the Chinese authorities are aware of her pro-Falun Gong activities in Canada and that she could be identified, as found in Liang v Canada (Citizenship and Immigration), 2016 FC 258 at para 13.
B. Respondent
(1) Credibility Findings

[38] The Respondent submits that the RAD’s credibility findings are reasonable.
(a) Exit from China

[39] The Respondent submits that, given the documentary evidence regarding the use and reach of the Golden Shield, it was reasonable for the RAD to find it highly unlikely that a smuggler would have prior knowledge of who to bribe in order to facilitate safe passage through the airport, particularly since the Applicants traveled on their own passports and alleged that the PSB were in continuous and vigorous pursuit. It was also reasonable for the RAD to expect that the local authorities would have entered the Principal Applicant’s information into the Golden Shield. Moreover, the RAD was reasonable in finding that despite the possibility that some security controls could be bypassed, it was highly unlikely that all of the controls could be bypassed.

[40] The Respondent views the Applicants’ argument that the RAD should have considered the possibility that all the controls could be circumvented as an alternate inference from the evidence. However, it is insufficient to demonstrate that another conclusion could have been reached; the Applicants have the onus to demonstrate that the RAD’s inferences were not supported by the evidence, which they failed to do. Additionally, the Applicants have failed to provide evidence that supports the alternative inferences, i.e. how the smuggler could have bypassed all of the security controls.

[41] The Respondent also takes the position that the RAD was reasonable in finding that the Principal Applicant’s evidence regarding the smuggler was vague and lacking in detail. It is reasonable to expect that an individual who leaves a country in order to avoid arrest and detention would want to know how the smuggler plans to ensure safe passage.

[42] Furthermore, the Respondent argues that the Applicants’ particular reliance on Sun and Ren, both above, are misplaced. The evidence in Sun regarding information sharing is outdated as it is dated July 2009, whereas the RAD relied upon a NDP dated April 29, 2016 that indicates the Chinese authorities have expanded the breadth and complexity of the information-sharing regime and have tightened airport security. Ren, on the other hand, is not applicable because the suggestion in that decision was that bribing a single individual would be sufficient in facilitating an exit from China without difficulty; in the present case, the Applicants’ arguments imply that the smuggler could remove the Principal Applicant’s information from the Golden Shield. Based on the evidence on the Golden Shield, it was reasonable to expect that the system could not be compromised by a single individual. Additionally, the Principal Applicant’s allegation that the PSB continues to pursue her undermines the suggestion that her information was removed from the system.

[43] The Respondent also argues that the jurisprudence cited by the Applicants in regards to this issue does not mean the RAD may never draw adverse inferences when a Chinese fugitive is able to exit the country using their own passport. Each decision must be based on the facts of each case, the analysis conducted, and the documentary evidence before the tribunal. Moreover, there are decisions from this Court in which such an adverse finding has been found to be reasonable: Ma v Canada (Citizenship and Immigration), 2015 FC 838 at para 53 [Ma]; Lin v Canada (Citizenship and Immigration), 2008 FC 698 at paras 10, 13, 16 [Lin]; Sui v Canada (Citizenship and Immigration), 2016 FC 406 at paras 37-43 [Sui].
(b) Motivation for Joining Falun Gong

[44] Despite the RPD’s request, the Principal Applicant failed to provide evidence to support her husband’s disappearance in 2012. As this was the reason she allegedly began practicing Falun Gong, it was reasonable for the RAD to concur with the RPD that the lack of corroborative evidence called into question the Principal Applicant’s motives for practicing Falun Gong. The Respondent also argues that the RAD’s concern was the absence of any evidence regarding her reasons for joining Falun Gong that would establish her claim, not whether her family and friends were illiterate.
(c) Summons

[45] Given the Principal Applicant’s assertion that the PSB remained in continuous and vigorous pursuit of her, the Respondent submits that it was reasonable for the RAD to conclude that a summons likely would have been issued if the allegations were true, even though the PSB’s policy on the issuance of summonses may not be uniform across China. As in Lan Cao v Canada (Citizenship and Immigration), 2012 FC 1398 at para 35, the documentary evidence did not directly contradict the RAD’s finding in this regard. Additionally, the Respondent argues that it was reasonable for the RAD to expect the Principal Applicant would have been aware of a summons if one were issued since she was in communication with her mother-in-law and the PSB had allegedly visited her mother-in-law’s home several times.

[46] Nonetheless, the Respondent submits that this issue is not determinative as there were other inconsistencies. The RAD’s credibility finding was based on the totality of the discrepancies; as such, even if this is an error the Decision may still be upheld: Nyathi v Canada (Minister of Citizenship and Immigration), 2003 FC 1119 at para 18.
(d) Copy of Zhuan Falun

[47] The Respondent takes the position that the testimony regarding the location of the Zhuan Falun book contains an inconsistency. The Principal Applicant originally stated that she read the Zhuan Falun book at home daily and only went to the practice site on the weekend, but she then stated that she hid the book at the practice site. The RAD rejected the explanation that she had hidden the book after finishing it because she had omitted her completion of the book and because the book was complex. Given the Principal Applicant’s testimony that she read the book daily in China, it was reasonable for the RAD to make its findings on this issue.
(e) Minor Applicant’s Expulsion

[48] In the Decision, the RAD found no evidence that family members had incurred any harm or threats, which, combined with the Principal Applicant’s failure to bring forth her son’s alleged expulsion from school at the RPD hearing, supported the finding that the Minor Applicant had not been expelled. The Principal Applicant had the onus of providing corroborating evidence and failed to do so. The Respondent submits that the RAD’s findings on this issue are reasonable because the mere fact that an applicant provides an explanation does not mean the explanation must be accepted; accordingly, it was open to the RAD to consider the explanation to determine whether it was sufficient and the Court should not re-weigh the evidence: Ma v Canada (Citizenship and Immigration), 2011 FC 417 at para 39.
(f) Other Discrepancies

[49] The Respondent submits that it was reasonable for the RAD to make a negative credibility finding based on a number of inconsistencies, some of which have not been challenged by the Applicants. These unchallenged inconsistencies include: the frequency of the Principal Applicant’s attendance at her Falun Gong group practice; the omission of information regarding the arrest of her co-practitioners; and the discrepancy regarding her place of hiding.
(2) Apprehension of Bias

[50] The Respondent argues that the Applicants have not met the high standard required to establish a reasonable apprehension of bias.

[51] First, the Decision is highly factual and contains a detailed analysis of the PSB’s information-sharing regime, Chinese airport security control procedures, sectors involving corruption problems, and the Principal Applicant’s allegations that the PSB continued to vigorously pursue her after she left China with the assistance of a smuggler. While there are cases in which the Court has disagreed with the RAD’s findings regarding an applicant’s ability to leave China, there are also cases where the Court has upheld those findings. Each decision is fact-specific and the Decision demonstrates the RAD’s grasp of the relevant issues and evidence. The fact that not every factor or piece of evidence was listed in the reasons is not fatal to the Decision or demonstrative of bias: Ma, above, at para 53; Lin, above, at paras 10, 13, 16; Sui, above.

[52] Second, the Applicants’ argument regarding this issue effectively disputes the RAD’s weighing of the evidence. Evidence that is ambiguous and equivocal does not warrant judicial intervention as long as the conclusion is not wrong on its face: Conkova v Canada (Citizenship and Immigration), [2000] FCJ No 300 at para 5. Moreover, the RAD member in question found that the jurisprudence of Zhang, Ren, and Sun, all above, was inapplicable in both RAD decisions because they were based on dated documentary evidence with limited information on the Golden Shield and Chinese border controls.
(3) Sur Place

[53] The Respondent submits the RAD’s assessment of the sur place claim is reasonable. The RAD did not dismiss the claim on the basis that the Principal Applicant was not a genuine Falun Gong practitioner; instead, the RAD found the Applicants had failed to present sufficient credible evidence that the Principal Applicant’s alleged Falun Gong activities in Canada had come to the attention of the Chinese authorities. The Applicants failed to meet the onus of showing an objective basis for their prospective fear of persecution. Given the credibility issues, it was reasonable for the RAD to find the Principal Applicant would not be perceived as a Falun Gong practitioner and, therefore, would not be pursued by the PSB. Additionally, it was reasonable for the RAD to find that a few photos of the Principal Applicant in an unknown place with an unknown group do not constitute sufficient evidence to establish that the Chinese authorities would be aware of her alleged Falun Gong activities.
C. Applicants’ Reply
(1) Apprehension of Bias

[54] The Applicants argue that the RAD’s knowing failure to mention contradictory jurisprudence that did not appear to be known to their counsel has nothing to do with weighing evidence. The RAD’s failure to consider the conflicting evidence does not constitute re-weighing.

[55] Additionally, the Applicants disagree that the RAD member’s omission of Zhang, Ren and Sun, all above, in previous RAD decisions is immaterial; these RAD decisions have been granted leave for judicial review before this Court based on the same issue. Moreover, the Applicants note that the Respondent is silent on the applicability of Yang and Yao, both above.
(2) Credibility Findings
(a) Exit from China

[56] Contrary to the Respondent’s submission, the Applicants submit that Ren and Sun, both above, are not distinguishable. In both decisions, as in the present case, the only evidence regarding what the smuggler did for the applicants was that bribes were paid to officials: Ren at para 6; Sun at para 8. Additionally, in Ren, the RPD relied on and cited from the same document regarding the Golden Shield that is cited in the Decision; accordingly, the Court’s decision dealt with the same evidence that is at issue in the present case. While the evidence regarding the Golden Shield in Sun is different from the documentation in the Applicants’ case, the Applicants submit that this does not lessen the decision’s relevance. In Sun, the Court found that it is impermissibly speculative to assume that a fugitive claimant could not exit China using his or her own passport and with the assistance of a smuggler; these are the circumstances of the present case. Finally, the Applicants submit that Yang and Yao are relevant because they were based on the NDP relied upon in the Decision.
(b) Motivation for Joining Falun Gong

[57] The Applicants reiterate that the explanation for the lack of corroborative evidence regarding the disappearance of the Principal Applicant’s husband in 2012 is not implausible and argue that the Respondent’s position on this matter is without merit.
(c) Summons

[58] The Applicants disagree with the Respondent on this issue and argue that there is no evidence whatsoever to suggest that the Chinese authorities serve summonses on criminal suspects, their family members, or even notify suspects or family members of the existence of a summons.
(d) Copy of Zhuan Falun

[59] The Applicants reiterate their argument that the Principal Applicant’s testimony regarding the location of the Zhuan Falun book is not inconsistent.
(e) Minor Applicant’s Expulsion

[60] The Applicants argue that the RAD’s finding that the Principal Applicant should have brought forth the subject of her son’s expulsion at the RPD hearing is illogical because she did not know there was a misunderstanding at that time. Furthermore, the failure to provide corroborative evidence on this matter does not justify a rejection of the Principal Applicant’s explanation; corroborative evidence is not required for refugee claimants and the RAD cannot disbelieve claimants merely due to its absence or make negative credibility findings in the absence of evidence to contradict such allegations: Ahortor v Canada (Minister of Employment and Immigration), [1993] FCJ No 705 at para 45.
(f) Sur Place

[61] The Applicants submit that the evidence submitted to establish the sur place claim consisted of more than just photos of the Principal Applicant practicing Falun Gong publicly in Canada. The Applicants had also submitted documentary evidence that speaks to the vigorous and aggressive measures of Chinese authorities in monitoring the activities of Falun Gong practitioners in Canada. This evidence, which included the Chinese authorities’ advanced facial recognition technology and possession of the Principal Applicant’s photograph, support the sur place claim.
VIII. ANALYSIS

[62] The RAD dismissed the Applicants’ appeal because they “failed to provide credible or trustworthy evidence to support [the Principal Applicant’s] allegation of FG practice and the PSB being in pursuit as a result.” This amounts to a general adverse credibility finding that is based upon a series of negative inferences related to key issues in the Applicants’ claim for protection. The Applicants do not challenge some of the RAD’s negative findings so that these aspects of the Decision must be taken as reasonable. This includes inconsistencies in how frequently the Principal Applicant attended group Falun Gong practices in China, a lack of information about the arrest of her co-practitioners in China, and discrepancies related to her place of hiding before she left China. Nevertheless, as the Respondent concedes, “it was the totality of these findings that led the RAD to conclude that the [Principal Applicant] was not credible with respect to her allegations of FG practice in China.”
A. Exit From China

[63] One of the central tenets of the Applicants’ case for review is that the RPD made unreasonable credibility findings about how the Principal Applicant could have left China using her own passport given the security measures in place at the airport, and that indeed the RAD went so far as to demonstrate a reasonable apprehension of bias in dealing with this issue because it failed to reference and apply supporting jurisprudence of which the RAD member was aware, but of which Applicants’ counsel was not.

[64] The RAD devotes considerable attention (paras 22-42 of the Decision) to this issue. The heart of the analysis is as follows:

[36] The RAD finds that evidence reveals that the Golden Shield system is an intensive security apparatus that is far-reaching and encompassing. The RAD finds that given the importance of this system to Chinese authorities in monitoring its citizens, it is reasonable to expect that the use of the apparatus is also monitored and that there are redundant systems in place to prevent the system from being compromised by a single individual. In addition, the RAD notes that the Appellant has alleged that the PSB have continued to pursue her after her departure from China. The RAD finds that this allegation undermines the suggestion that her name was somehow removed from the computer system.

[37] The RAD also notes that the evidence suggests that the Appellant’s passport was examined numerous times. The RAD finds it highly improbable that the smuggler would have the prior knowledge of who to bribe in order to facilitate safe travel through each checkpoint. The RAD also notes that Article 51 of the Exit and Entry Administration law of the People’s Republic of China requires that companies involved in the transportation of goods and passengers in and out of Chinese ports must declare information on the goods and passengers in advance of their departure or entry to the country. Chinese border authorities are provided what is described as “advance passenger information”·on arriving and departing passengers. This information contains 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 9900:6 · paragraphs 90-94

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d583e9e6ad4aaf15e430fea130cef01161241ea40c1e07a2ad67695a4dd83cf0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:6:subtheme:1 · paragraphs 90-92

- Raw key terms: `above, claim, credibility, applicants, decision, errors, negative, place`
- Display key terms: `above, credibility, errors, negative, place`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: above, credibility, errors, negative, place Application context: ” See Liang, above, at paras 11-14; c) There were no real inconsistencies or omissions in the Principal Applicant’s testimony about her Zhuan Falun text; d) The Principal Applicant’s evidence about her son’s expulsion co Evidence spans paragraphs 90-92. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500436` offsets `187-195`; context: [69] It also seems to me that the RAD makes the following materials errors:
a) The RAD mischaracterizes the Principal Applicant’s explanation as to why she could not obtain corroborative evidence about her husband’s disappearance from family and friends.
- Evidence: `reasoning_application` cue `because` at chunk `4500436` offsets `1009-1016`; context: ” See Liang, above, at paras 11-14;
c) There were no real inconsistencies or omissions in the Principal Applicant’s testimony about her Zhuan Falun text;
d) The Principal Applicant’s evidence about her son’s expulsion could not have been brought before the RPD because, as the Principal Applicant makes clear in her affidavit, she could not have been aware of any misunderstanding about her evidence before the RPD.
- Evidence: `counterargument_limitation` cue `However` at chunk `4500437` offsets `124-131`; context: However, I think the above are sufficient to render the Decision unsafe and unreasonable.

#### 9900:6:subtheme:2 · paragraphs 93-94

- Raw key terms: `court, able, above, acknowledges, adduced, agree, applied, arisen`
- Display key terms: `able, above, acknowledges, adduced, agree, applied, arisen`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: able, above, acknowledges, adduced, agree, applied, arisen Application context: This does not means that I am establishing any kind of precedent that can be applied in future cases. Evidence spans paragraphs 93-94. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4500439` offsets `119-124`; context: [72] I am aware that similar cases to the present have arisen frequently in the Court, particularly with regard to the issue of whether claimants are able to exit China with their own passports given the Golden Shield system in place.
- Evidence: `evidence_fact` cue `evidence` at chunk `4500439` offsets `355-363`; context: In my view – and the Respondent acknowledges this – it really depends upon the facts and evidence adduced in each case.
- Evidence: `reasoning_application` cue `applied` at chunk `4500439` offsets `623-630`; context: This does not means that I am establishing any kind of precedent that can be applied in future cases.
- Evidence: `issue` cue `question` at chunk `4500440` offsets `31-39`; context: [73] Counsel agree there is no question or certification and the Court concurs.

#### Section text

[69] It also seems to me that the RAD makes the following materials errors:
a) The RAD mischaracterizes the Principal Applicant’s explanation as to why she could not obtain corroborative evidence about her husband’s disappearance from family and friends. The Principal Applicant didn’t just say that these people were illiterate, she explained that they “did not want to get involved” and this is readily understandable and plausible given what could happen to them in China if they assist the Principal Applicant with her Falun Gong refugee claim;
b) There is no real evidence to support the RAD conclusion that the “lack of a summons or arrest warrant, when one should reasonably been issued, damages the credibility of the [Principal Applicant].” See Liang, above, at paras 11-14;
c) There were no real inconsistencies or omissions in the Principal Applicant’s testimony about her Zhuan Falun text;
d) The Principal Applicant’s evidence about her son’s expulsion could not have been brought before the RPD because, as the Principal Applicant makes clear in her affidavit, she could not have been aware of any misunderstanding about her evidence before the RPD.

[70] The RAD also based its cumulative negative credibility finding on other factors that the Applicants’ do not challenge. However, I think the above are sufficient to render the Decision unsafe and unreasonable.
C. Sur Place Claim

[71] The RAD’s findings on the sur place aspect of the Applicants’ claim are tainted by the negative credibility findings from the rest of the Decision. In my view, then, the sur place claim also needs to be reconsidered in light of the reviewable errors identified above.

[72] I am aware that similar cases to the present have arisen frequently in the Court, particularly with regard to the issue of whether claimants are able to exit China with their own passports given the Golden Shield system in place. Decisions have gone both ways. In my view – and the Respondent acknowledges this – it really depends upon the facts and evidence adduced in each case. In the present case, I think there are sufficient concerns about the factual findings of the RAD, as outlined above, to require a reconsideration of this case. This does not means that I am establishing any kind of precedent that can be applied in future cases.

[73] Counsel agree there is no question or certification and the Court concurs.


## 9900:7 · paragraphs 95-96

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2fbd8935e5acfa2189102bfff6fa56c81e043a639785c822378f6a28886ddaef`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:7:subtheme:1 · paragraphs 95-96

- Raw key terms: `imm-53-17, allowed, application, cause, certification, citizenship, constituted, court`
- Display key terms: `imm-53-17, allowed, certification, constituted`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-53-17, allowed, certification, constituted Operative outcome context: JUDGMENT IN IMM-53-17 THIS COURT’S JUDGMENT is that The application is allowed. Evidence spans paragraphs 95-96. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4500440` offsets `277-285`; context: The Decision is quashed and the matter is returned for reconsideration by a differently constituted RAD;
There is no question for certification.
- Evidence: `disposition` cue `allowed` at chunk `4500440` offsets `151-158`; context: JUDGMENT IN IMM-53-17
THIS COURT’S JUDGMENT is that
The application is allowed.

#### Section text

JUDGMENT IN IMM-53-17
THIS COURT’S JUDGMENT is that
The application is allowed. The Decision is quashed and the matter is returned for reconsideration by a differently constituted RAD;
There is no question for certification.
“James Russell”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-53-17
STYLE OF CAUSE:
GUIMEI HUANG ET AL v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
JULY 26, 2017


## 9900:8 · paragraphs 97-97

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6cf7dd4719deb4e72b8e1310a811059f52403fed71d7964dd426ad2a78a61cf7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9900:8:subtheme:1 · paragraphs 97-97

- Raw key terms: `appearances, applicants, attorney, august, barristers, canada, christopher, crighton`
- Display key terms: `august, barristers, christopher, crighton`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, barristers, christopher, crighton No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 97-97. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
RUSSELL J.
DATED:
August 10, 2017
APPEARANCES:
Michael Korman
For The ApplicantS
Christopher Crighton
For The Respondent
SOLICITORS OF RECORD:
Otis & Korman
Barristers and Solicitors
Toronto, Ontario
For The ApplicantS
Attorney General of Canada
Toronto, Ontario
For The Respondent
