# Discussion Units: case 23342

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **68**
- Continuity pairs: **67**
- Discussion Units: **6**
- Paragraph source hashes: **68**
- Sub-themes: **20**

## 23342:1 · paragraphs 0-7

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `49e0d35df5c880add1256f02c4dda39ea1c2160550193f651a8b38562daf0def`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `immigration, court, decision, decisions, judicial, parminder, protection, refugee`
- Display key terms: `decisions, judicial, parminder, protection, refugee`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: decisions, judicial, parminder, protection, refugee Rule/authority context: Parminder Singh seeks judicial review of a decision by the RAD, dated September 26, 2013, whereby it confirmed the decision of the RPD that he is neither a Convention refugee within the meaning of section 96 of the Immig Application context: [1] This application for judicial review concerns the power and duties of the newly constituted Refugee Appeal Division of the Immigration and Refugee Board [RAD], not so much with respect to the standard of intervention | In its analysis of the RPD decision, the RAD applied the reasonableness standard; it considered its mandate essentially akin to that of this Court when undertaking a judicial review of a RPD decision. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096512` offsets `392-400`; context: [1] This application for judicial review concerns the power and duties of the newly constituted Refugee Appeal Division of the Immigration and Refugee Board [RAD], not so much with respect to the standard of intervention that it should apply when sitting in appeal of decisions by the Refugee Protection Division [RPD], but rather with respect to the criteria it must consider upon admitting evidence not before the RPD.
- Evidence: `reasoning_application` cue `apply` at chunk `5096512` offsets `236-241`; context: [1] This application for judicial review concerns the power and duties of the newly constituted Refugee Appeal Division of the Immigration and Refugee Board [RAD], not so much with respect to the standard of intervention that it should apply when sitting in appeal of decisions by the Refugee Protection Division [RPD], but rather with respect to the criteria it must consider upon admitting evidence not before the RPD.
- Evidence: `governing_rule` cue `under` at chunk `5096513` offsets `318-323`; context: Parminder Singh seeks judicial review of a decision by the RAD, dated September 26, 2013, whereby it confirmed the decision of the RPD that he is neither a Convention refugee within the meaning of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] nor a person in need of protection under its subsection 97(1).
- Evidence: `reasoning_application` cue `applied` at chunk `5096513` offsets `391-398`; context: In its analysis of the RPD decision, the RAD applied the reasonableness standard; it considered its mandate essentially akin to that of this Court when undertaking a judicial review of a RPD decision.

#### 23342:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `court, decisions, position, review, addition, alvarez, alyafi, appeal`
- Display key terms: `decisions, position, review, addition, alvarez, alyafi`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: decisions, position, review, addition, alvarez, alyafi Rule/authority context: [4] For the purpose of the present application, it is sufficient to say that this Court clearly rejected the position taken by the RAD in the decision under review, that it owes deference to the findings of the RPD and t Application context: [4] For the purpose of the present application, it is sufficient to say that this Court clearly rejected the position taken by the RAD in the decision under review, that it owes deference to the findings of the RPD and t Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5096514` offsets `891-897`; context: In addition, early this month in Alyafi v Canada (Minister of Immigration and Citizenship), 2014 FC 952, Justice Martineau, who did not specifically need to take position on these issues, made an interesting review of this Court’s previous decisions.
- Evidence: `governing_rule` cue `under` at chunk `5096515` offsets `151-156`; context: [4] For the purpose of the present application, it is sufficient to say that this Court clearly rejected the position taken by the RAD in the decision under review, that it owes deference to the findings of the RPD and that it should apply the reasonableness standard, as this Court does when reviewing the RPD decisions that are not subject to an appeal before the RAD.
- Evidence: `reasoning_application` cue `apply` at chunk `5096515` offsets `234-239`; context: [4] For the purpose of the present application, it is sufficient to say that this Court clearly rejected the position taken by the RAD in the decision under review, that it owes deference to the findings of the RPD and that it should apply the reasonableness standard, as this Court does when reviewing the RPD decisions that are not subject to an appeal before the RAD.

#### 23342:1:subtheme:3 · paragraphs 5-7

- Raw key terms: `admit, applicant, application, demonstrate, determined, evidence, failed, identity`
- Display key terms: `admit, demonstrate, determined, failed, identity`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: admit, demonstrate, determined, failed, identity Rule/authority context: [5] However and as indicated above, the principal issue in this application for judicial review, as framed by the applicant, is whether it was reasonable for the RAD to refuse to admit a piece of evidence—a 2002 grade 12 | [6] The RAD applied the jurisprudence of this Court interpreting paragraph 113(a) of the Act mutatis mutandis to the interpretation of its subsection 110(4). Application context: [6] The RAD applied the jurisprudence of this Court interpreting paragraph 113(a) of the Act mutatis mutandis to the interpretation of its subsection 110(4). Operative outcome context: [7] For the reasons discussed below, this application for judicial review will be granted. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5096516` offsets `50-55`; context: [5] However and as indicated above, the principal issue in this application for judicial review, as framed by the applicant, is whether it was reasonable for the RAD to refuse to admit a piece of evidence—a 2002 grade 12 diploma—that had not been before the RPD, pursuant to subsection 110(4) of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096516` offsets `196-204`; context: [5] However and as indicated above, the principal issue in this application for judicial review, as framed by the applicant, is whether it was reasonable for the RAD to refuse to admit a piece of evidence—a 2002 grade 12 diploma—that had not been before the RPD, pursuant to subsection 110(4) of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5096516` offsets `263-274`; context: [5] However and as indicated above, the principal issue in this application for judicial review, as framed by the applicant, is whether it was reasonable for the RAD to refuse to admit a piece of evidence—a 2002 grade 12 diploma—that had not been before the RPD, pursuant to subsection 110(4) of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096517` offsets `213-221`; context: Paragraph 113(a) deals with the admissibility of fresh evidence before a Pre-Removal Risk Assessment [PRRA] officer (that had not been before the RPD).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5096517` offsets `24-37`; context: [6] The RAD applied the jurisprudence of this Court interpreting paragraph 113(a) of the Act mutatis mutandis to the interpretation of its subsection 110(4).
- Evidence: `reasoning_application` cue `applied` at chunk `5096517` offsets `12-19`; context: [6] The RAD applied the jurisprudence of this Court interpreting paragraph 113(a) of the Act mutatis mutandis to the interpretation of its subsection 110(4).
- Evidence: `disposition` cue `granted` at chunk `5096518` offsets `82-89`; context: [7] For the reasons discussed below, this application for judicial review will be granted.

#### Section text

Singh v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-10-28
Neutral citation
2014 FC 1022
File numbers
IMM-6711-13
Notes
A correction was made on June 02, 2015.
Reported Decision
Decision Content
Date: 20141028
Docket: IMM-6711-13
Citation: 2014 FC 1022
Ottawa, Ontario, October 28, 2014
PRESENT: The Honourable Madam Justice Gagné
BETWEEN:
PARMINDER SINGH
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This application for judicial review concerns the power and duties of the newly constituted Refugee Appeal Division of the Immigration and Refugee Board [RAD], not so much with respect to the standard of intervention that it should apply when sitting in appeal of decisions by the Refugee Protection Division [RPD], but rather with respect to the criteria it must consider upon admitting evidence not before the RPD.

[2] Mr. Parminder Singh seeks judicial review of a decision by the RAD, dated September 26, 2013, whereby it confirmed the decision of the RPD that he is neither a Convention refugee within the meaning of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] nor a person in need of protection under its subsection 97(1). In its analysis of the RPD decision, the RAD applied the reasonableness standard; it considered its mandate essentially akin to that of this Court when undertaking a judicial review of a RPD decision.

[3] There are several recent decisions of this Court concerning both the role of the newly created RAD, and of this Court upon judicial review of decisions made by the RAD (see Iyamuremye v Canada (Minister of Citizenship and Immigration), 2014 FC 494; Garcia Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702; Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711; Huruglica v Canada (Minister of Citizenship and Immigration), 2014 CF 799 [Huruglica]; Njeukam v Canada (Minister of Citizenship and Immigration), 2014 FC 859; Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858; and Spasoja c Canada (Minister of Citizenship and Immigration), 2014 FC 913). In addition, early this month in Alyafi v Canada (Minister of Immigration and Citizenship), 2014 FC 952, Justice Martineau, who did not specifically need to take position on these issues, made an interesting review of this Court’s previous decisions.

[4] For the purpose of the present application, it is sufficient to say that this Court clearly rejected the position taken by the RAD in the decision under review, that it owes deference to the findings of the RPD and that it should apply the reasonableness standard, as this Court does when reviewing the RPD decisions that are not subject to an appeal before the RAD.

[5] However and as indicated above, the principal issue in this application for judicial review, as framed by the applicant, is whether it was reasonable for the RAD to refuse to admit a piece of evidence—a 2002 grade 12 diploma—that had not been before the RPD, pursuant to subsection 110(4) of the Act. The diploma would allegedly confirm that the RPD had unreasonably determined that the applicant failed to demonstrate his identity, and that he was not credible.

[6] The RAD applied the jurisprudence of this Court interpreting paragraph 113(a) of the Act mutatis mutandis to the interpretation of its subsection 110(4). Paragraph 113(a) deals with the admissibility of fresh evidence before a Pre-Removal Risk Assessment [PRRA] officer (that had not been before the RPD). While the RAD ultimately held that the RPD unreasonably determined that the applicant had failed to satisfactorily demonstrate his identity for other reasons, the applicant maintains that the credibility determination was compromised by the RAD’s refusal to admit his new evidence.

[7] For the reasons discussed below, this application for judicial review will be granted.


## 23342:2 · paragraphs 8-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `76be7ae18e3d5ecae28d81a3a1b0b3c4cb601946e8a5885c71b22e5c84b97af5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:2:subtheme:1 · paragraphs 8-28

- Raw key terms: `applicant, credibility, identity, diploma, document, order, bhupinder, canada`
- Display key terms: `credibility, identity, diploma, document, order, bhupinder`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: credibility, identity, diploma, document, order, bhupinder Position/evidence statements: He alleged before the RPD a well-founded fear of persecution based on “imputed political opinion” and also claimed to be a person in need of protection. | [14] The applicant claimed to have arrived with some genuine documents, including his birth certificate, a 1998 school report card, as well as two school diplomas (a grade 10 diploma from 2000, and a grade 12 diploma fro Rule/authority context: The Impugned RAD Decision [23] The applicant sought to produce his 2002 high school diploma before the RAD, arguing that it was new evidence pursuant to subsection 110(4) of the Act. | [27] The RAD also dismissed the applicant’s request for a hearing pursuant to subsection 110(6) of the Act, in order to reassess his credibility in light of the production of the 2002 diploma. Application context: [17] Despite not being satisfied with his identity demonstration, the RPD continued with its analysis, concluding that even had the applicant sufficiently demonstrated his identity, his refugee claim would still have bee | As such, the RAD applied the criteria emanating from Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385 [Raza] at para 13, and evaluated the credibility, the relevance, the newness, and the materiality Operative outcome context: [17] Despite not being satisfied with his identity demonstration, the RPD continued with its analysis, concluding that even had the applicant sufficiently demonstrated his identity, his refugee claim would still have bee | [27] The RAD also dismissed the applicant’s request for a hearing pursuant to subsection 110(6) of the Act, in order to reassess his credibility in light of the production of the 2002 diploma. Evidence spans paragraphs 8-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5096518` offsets `265-272`; context: He alleged before the RPD a well-founded fear of persecution based on “imputed political opinion” and also claimed to be a person in need of protection.
- Evidence: `party_position` cue `claimed` at chunk `5096523` offsets `19-26`; context: [14] The applicant claimed to have arrived with some genuine documents, including his birth certificate, a 1998 school report card, as well as two school diplomas (a grade 10 diploma from 2000, and a grade 12 diploma from 2002).
- Evidence: `counterargument_limitation` cue `However` at chunk `5096523` offsets `348-355`; context: However, only the grade 10 diploma was before the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096524` offsets `311-319`; context: Moreover, considering the importance of this evidence for the applicant’s narrative, the RPD held that his inability to produce it negatively affected his credibility.
- Evidence: `reasoning_application` cue `because` at chunk `5096526` offsets `229-236`; context: [17] Despite not being satisfied with his identity demonstration, the RPD continued with its analysis, concluding that even had the applicant sufficiently demonstrated his identity, his refugee claim would still have been denied because it lacked credibility.
- Evidence: `disposition` cue `denied` at chunk `5096526` offsets `222-228`; context: [17] Despite not being satisfied with his identity demonstration, the RPD continued with its analysis, concluding that even had the applicant sufficiently demonstrated his identity, his refugee claim would still have been denied because it lacked credibility.
- Evidence: `party_position` cue `submitted` at chunk `5096531` offsets `379-388`; context: Pursuant to subsection 3(3) of the Refugee Appeal Division Rules, SOR/2012-257, the applicant submitted a written statement detailing how his documentary evidence satisfied the requirements of subsection 110(4) of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096531` offsets `234-242`; context: The Impugned RAD Decision [23] The applicant sought to produce his 2002 high school diploma before the RAD, arguing that it was new evidence pursuant to subsection 110(4) of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5096531` offsets `243-254`; context: The Impugned RAD Decision [23] The applicant sought to produce his 2002 high school diploma before the RAD, arguing that it was new evidence pursuant to subsection 110(4) of the Act.
- Evidence: `evidence_fact` cue `determined that` at chunk `5096532` offsets `13-28`; context: [24] The RAD determined that subsection 110(4) is very similar to paragraph 113(a) of the Act, which deals with the admissibility of fresh evidence before a PRRA officer.
- Evidence: `reasoning_application` cue `applied` at chunk `5096532` offsets `188-195`; context: As such, the RAD applied the criteria emanating from Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385 [Raza] at para 13, and evaluated the credibility, the relevance, the newness, and the materiality of the evidence in order to decide on its admissibility.
- Evidence: `party_position` cue `argued` at chunk `5096533` offsets `315-321`; context: The applicant argued that he needed it for his appeal in order to prove that the RPD had erred in not believing that CIC had seized it.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5096536` offsets `66-77`; context: [27] The RAD also dismissed the applicant’s request for a hearing pursuant to subsection 110(6) of the Act, in order to reassess his credibility in light of the production of the 2002 diploma.
- Evidence: `disposition` cue `dismissed` at chunk `5096536` offsets `18-27`; context: [27] The RAD also dismissed the applicant’s request for a hearing pursuant to subsection 110(6) of the Act, in order to reassess his credibility in light of the production of the 2002 diploma.
- Evidence: `governing_rule` cue `standard of review` at chunk `5096537` offsets `27-45`; context: [28] With respect to which standard of review to apply to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399, the RAD held that the RPD, as a first instance tribunal, is owed deference, and that its findings of fact and of mixed fact and law decisions must be assessed on a reasonableness standard.
- Evidence: `reasoning_application` cue `apply` at chunk `5096537` offsets `49-54`; context: [28] With respect to which standard of review to apply to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399, the RAD held that the RPD, as a first instance tribunal, is owed deference, and that its findings of fact and of mixed fact and law decisions must be assessed on a reasonableness standard.

#### 23342:2:subtheme:2 · paragraphs 29-32

- Raw key terms: `applicant, respect, credibility, failed, identity, reasonable, satisfactorily, whether`
- Display key terms: `respect, credibility, failed, identity, reasonable, satisfactorily, whether`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: respect, credibility, failed, identity, reasonable, satisfactorily, whether Evidence spans paragraphs 29-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5096539` offsets `320-327`; context: In doing so, the RAD noted that its purpose is not to “re-evaluate the evidence,” nor to proceed with “a microscopic analysis” of the RPD’s decision, but rather determine whether this was a reasonable outcome.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096539` offsets `220-228`; context: In doing so, the RAD noted that its purpose is not to “re-evaluate the evidence,” nor to proceed with “a microscopic analysis” of the RPD’s decision, but rather determine whether this was a reasonable outcome.
- Evidence: `counterargument_limitation` cue `but` at chunk `5096539` offsets `299-302`; context: In doing so, the RAD noted that its purpose is not to “re-evaluate the evidence,” nor to proceed with “a microscopic analysis” of the RPD’s decision, but rather determine whether this was a reasonable outcome.
- Evidence: `issue` cue `whether` at chunk `5096540` offsets `362-369`; context: Nonetheless, it was unreasonable that the RPD did not consider the probative value of the school diploma (and the 1998 report card) in assessing whether the applicant had satisfactorily demonstrated his identity, even though it had assessed the document for other reasons.
- Evidence: `evidence_fact` cue `determined that` at chunk `5096541` offsets `22-37`; context: [32] However, the RAD determined that the RPD’s overall credibility assessment was reasonable.

#### Section text

I. Background [8] The applicant is a 30 year old citizen of India. He alleged before the RPD a well-founded fear of persecution based on “imputed political opinion” and also claimed to be a person in need of protection.

[9] During his school days, the applicant was friends with one Bhupinder Singh. He graduated in 2002, at which time he returned to his family’s farm.

[10] In November 2012, after several years of not having heard from him, Bhupinder Singh showed up unannounced at the applicant’s house to spend the night. A few days later, the Indian police arrived at the applicant’s house and arrested him in order to ask him questions about Bhupinder Singh. The applicant was detained, tortured and released three days later. He was admitted to a hospital for five days, where he was treated for stomach pains.

[11] The applicant was arrested a second time, 15 days later, in order to be asked more questions about Bhupinder Singh. After a 1 day detention, he was unconditionally released.

[12] Following his second arrest, the applicant’s mother decided to pay an agent so her son could safely leave India. He left India on January 28, 2013, and arrived in Canada the following day. His inland refugee claim was received on February 21, 2013.
II. The RPD decision [13] The applicant’s refugee claim hearing was rejected on May 1, 2013. The RPD held that the applicant failed to satisfactorily establish his identity.

[14] The applicant claimed to have arrived with some genuine documents, including his birth certificate, a 1998 school report card, as well as two school diplomas (a grade 10 diploma from 2000, and a grade 12 diploma from 2002). The RPD found it noteworthy to add that neither diploma had been examined by the Canada Border Services Agency [CBSA]. However, only the grade 10 diploma was before the RPD. In addition to not confirming his identity, the fact that the 2002 diploma was missing could not corroborate that the applicant had studied with Bhupinder Singh until 2002.

[15] The applicant alleged that his grade 12 diploma had been taken by Citizenship and Immigration Canada [CIC] when he had been detained upon arrival, and that CIC failed to forward it to the RPD. The RPD did not believe that CIC was in possession of the document. Moreover, considering the importance of this evidence for the applicant’s narrative, the RPD held that his inability to produce it negatively affected his credibility.

[16] The RPD did not believe that the applicant’s birth certificate was sufficient to demonstrate his identity.

[17] Despite not being satisfied with his identity demonstration, the RPD continued with its analysis, concluding that even had the applicant sufficiently demonstrated his identity, his refugee claim would still have been denied because it lacked credibility. Notably, the RPD drew negative inferences from the fact that the applicant had amended his original Basis of Claim form [BOC] to reflect that his father’s stroke occurred between his two arrests (and not following his second arrest). The Board considered this to be a significant event in the applicant’s life, and so he should not have made a chronological error in this respect.

[18] The RPD also drew negative inferences as it seemingly misunderstood the difference between a heart attack and a stroke. The applicant had written in his BOC that his father had suffered a stroke, and had produced a medical report indicating that his father had suffered from facial paralysis in late November 2012, and was advised to seek bed rest for five days. Yet the RPD could not accept that a man suffering from a heart condition would be issued such a medical report. Moreover, the applicant had testified that his father became bedridden, almost paralyzed, and required assistance to complete basic life tasks; yet the medical note does not mention a bedridden person, but rather someone who suffers from facial paralysis and who has to stay in bed for a five-day period.

[19] The RPD also did not believe that the applicant had to go to the hospital following the torture he suffered when first detained, as the medical note he produced (and the list of drugs it claims were administered to him) does not corroborate his allegations. No explanation was provided as to why these specific drugs would not be administered to a torture victim.

[20] Finally, even had the applicant established his identity and been considered credible, he had an internal flight alternative [IFA] in Mumbai, Delhi or Bangalore.

[21] The applicant appealed this decision to the RAD, invoking three main grounds: (1) the RPD erred in analyzing his identity; (2) the RPD did not properly evaluate his credibility; and (3) the RPD erred in its IFA analysis.

[22] On September 26, 2013 the applicant’s appeal was rejected by a one member panel of the RAD.
III. The Impugned RAD Decision [23] The applicant sought to produce his 2002 high school diploma before the RAD, arguing that it was new evidence pursuant to subsection 110(4) of the Act. Pursuant to subsection 3(3) of the Refugee Appeal Division Rules, SOR/2012-257, the applicant submitted a written statement detailing how his documentary evidence satisfied the requirements of subsection 110(4) of the Act.

[24] The RAD determined that subsection 110(4) is very similar to paragraph 113(a) of the Act, which deals with the admissibility of fresh evidence before a PRRA officer. As such, the RAD applied the criteria emanating from Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385 [Raza] at para 13, and evaluated the credibility, the relevance, the newness, and the materiality of the evidence in order to decide on its admissibility.

[25] In his written statement, the applicant pled that he only became aware on June 11, 2013 that this document had been faxed on February 25, 2013 by CIC (which had seized it on January 29, 2013) to the applicant’s former lawyer. As such, it had been impossible for him to produce it before the RPD. The applicant argued that he needed it for his appeal in order to prove that the RPD had erred in not believing that CIC had seized it. Considering that his failure to produce this diploma negatively affected his overall credibility, the applicant argued that it was of paramount importance to have it before the RAD.

[26] The RAD concluded that at the date of the hearing before the RPD, the applicant could have produced the document, and so it could not be admissible before the RAD. Considering that he had not taken a complaint procedure against his former lawyer for failing to advise him that the document was in her possession before the RPD hearing, the RAD presumed that the applicant had been made aware of the document’s retrieval from CIC:

[28] . . . En effet, si ce document a été saisi, le 29 janvier 2013, par les autorités de l’immigration, il n’en demeure pas moins que, le 25 février 2013, une copie de ce document a été transmise par télécopieur à son avocate. Un membre du Barreau du Québec a envers son client, un devoir de compétence ainsi que des obligations de loyauté, d’intégrité, d’indépendance, de désintéressement, de diligence et de prudence. Dans le cadre de la présente procédure d’appel, l’appelant n’a pas invoqué que son avocate a agi avec incompétence et il n’a pas fourni la preuve qu’il avait, d’une manière ou d’une autre, formulé une plainte contre son ancienne avocate et que celle-ci en a été informée de manière à ce qu’elle puisse, au besoin, se faire entendre à ce sujet. [Emphasis added.]

[27] The RAD also dismissed the applicant’s request for a hearing pursuant to subsection 110(6) of the Act, in order to reassess his credibility in light of the production of the 2002 diploma. Considering the document was deemed inadmissible, there was no ground to hold a hearing.

[28] With respect to which standard of review to apply to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399, the RAD held that the RPD, as a first instance tribunal, is owed deference, and that its findings of fact and of mixed fact and law decisions must be assessed on a reasonableness standard. Questions of law and of procedural fairness are to be evaluated on the correctness standard.

[29] As such, the three grounds of appeal (dealing with the applicant’s identity, his credibility, and his IFA) were reviewed on the reasonableness standard.

[30] With respect to the applicant’s identity, the RAD held that the RPD unreasonably concluded that he had failed to satisfactorily demonstrate it. In doing so, the RAD noted that its purpose is not to “re-evaluate the evidence,” nor to proceed with “a microscopic analysis” of the RPD’s decision, but rather determine whether this was a reasonable outcome.

[31] The RAD agreed that the applicant had failed to make sufficient efforts in order to provide documents establishing his identity, and that the RPD was right to draw a negative credibility finding in this respect. Nonetheless, it was unreasonable that the RPD did not consider the probative value of the school diploma (and the 1998 report card) in assessing whether the applicant had satisfactorily demonstrated his identity, even though it had assessed the document for other reasons.

[32] However, the RAD determined that the RPD’s overall credibility assessment was reasonable.

[33] Finally, the RAD did not address the RPD’s determination with respect to his IFA, considering the applicant was deemed not to be credible.


## 23342:3 · paragraphs 33-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `51ca7cad5a3befc1f32c2c3bcaec60fd6e6edcb14e684ad39eff6b4085672458`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:3:subtheme:1 · paragraphs 33-34

- Raw key terms: `decision, review, standard, agree, appeal, applicant, applying, deference`
- Display key terms: `review, standard, agree, applying, deference`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: review, standard, agree, applying, deference Rule/authority context: Issues and Standard of Review [34] The applicant only raises one issue: • Was the Refugee Appeal Division’s overall decision reasonable? Evidence spans paragraphs 33-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5096542` offsets `148-154`; context: Issues and Standard of Review [34] The applicant only raises one issue:
• Was the Refugee Appeal Division’s overall decision reasonable?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5096542` offsets `159-177`; context: Issues and Standard of Review [34] The applicant only raises one issue:
• Was the Refugee Appeal Division’s overall decision reasonable?

#### 23342:3:subtheme:2 · paragraphs 35-37

- Raw key terms: `interpretation, applied, correctness, court, home, para, respondent, standard`
- Display key terms: `interpretation, applied, correctness, home, para, standard`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: interpretation, applied, correctness, home, para, standard Position/evidence statements: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should b Rule/authority context: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should b Application context: [36] However, the issue before the Court is rather whether the RAD erred in its interpretation of subsection 110(4) of the Act by using the Raza test and if it reasonably applied it. | [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should b Evidence spans paragraphs 35-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5096544` offsets `18-23`; context: [36] However, the issue before the Court is rather whether the RAD erred in its interpretation of subsection 110(4) of the Act by using the Raza test and if it reasonably applied it.
- Evidence: `reasoning_application` cue `applied` at chunk `5096544` offsets `171-178`; context: [36] However, the issue before the Court is rather whether the RAD erred in its interpretation of subsection 110(4) of the Act by using the Raza test and if it reasonably applied it.
- Evidence: `party_position` cue `argues` at chunk `5096545` offsets `77-83`; context: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should be subject to the reasonableness standard, as it involves a tribunal considering and applying its home statute: while errors of law are generally governed by a correctness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096545` offsets `203-211`; context: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should be subject to the reasonableness standard, as it involves a tribunal considering and applying its home statute: while errors of law are generally governed by a correctness standard.
- Evidence: `governing_rule` cue `standard of review` at chunk `5096545` offsets `20-38`; context: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should be subject to the reasonableness standard, as it involves a tribunal considering and applying its home statute: while errors of law are generally governed by a correctness standard.
- Evidence: `reasoning_application` cue `applied` at chunk `5096545` offsets `39-46`; context: [37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should be subject to the reasonableness standard, as it involves a tribunal considering and applying its home statute: while errors of law are generally governed by a correctness standard.
- Evidence: `reasoning_application` cue `apply` at chunk `5096546` offsets `291-296`; context: [38] The respondent further cites Saskatchewan (Human Rights Commission) v Whatcott, 2013 SCC 11 at para 167, interpreting Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, [2011] 3 SCR 654 [Alberta Teachers] at para 30 on the exceptions where correctness will apply:
This principle [of deference] applies unless the interpretation of the home statute falls into one of the categories of questions to which the correctness standard continues to apply, i.

#### 23342:3:subtheme:3 · paragraphs 38-38

- Raw key terms: `admissibility, argues, central, circumstances, correctness, evidence, expertise, importance`
- Display key terms: `admissibility, argues, central, circumstances, correctness, expertise, importance`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: admissibility, argues, central, circumstances, correctness, expertise, importance Position/evidence statements: [39] As such, the respondent argues that the admissibility of new evidence before the RAD is within the tribunal’s expertise and does not involve a question of central importance to the legal system as a whole or any oth Evidence spans paragraphs 38-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096547` offsets `148-156`; context: [39] As such, the respondent argues that the admissibility of new evidence before the RAD is within the tribunal’s expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `party_position` cue `argues` at chunk `5096547` offsets `29-35`; context: [39] As such, the respondent argues that the admissibility of new evidence before the RAD is within the tribunal’s expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096547` offsets `66-74`; context: [39] As such, the respondent argues that the admissibility of new evidence before the RAD is within the tribunal’s expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.

#### Section text

IV. Issues and Standard of Review [34] The applicant only raises one issue:
• Was the Refugee Appeal Division’s overall decision reasonable?

[35] The parties both plead that the RAD owes the RPD deference and that it should review the RPD decision applying the reasonableness standard. Respectfully, I do not agree.

[36] However, the issue before the Court is rather whether the RAD erred in its interpretation of subsection 110(4) of the Act by using the Raza test and if it reasonably applied it.

[37] As regards the standard of review applied by this Court, the respondent argues that the RAD’s determination of the appropriate analysis that is to be conducted in assessing the admissibility of new evidence should be subject to the reasonableness standard, as it involves a tribunal considering and applying its home statute: while errors of law are generally governed by a correctness standard. “ Dunsmuir [v New Brunswick, 2008 SCC 9] (at para. 54), says that if the interpretation of the home statute or a closely related statute by an expert decision maker is reasonable, there is no error of law justifying intervention ” (Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 44).

[38] The respondent further cites Saskatchewan (Human Rights Commission) v Whatcott, 2013 SCC 11 at para 167, interpreting Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, [2011] 3 SCR 654 [Alberta Teachers] at para 30 on the exceptions where correctness will apply:
This principle [of deference] applies unless the interpretation of the home statute falls into one of the categories of questions to which the correctness standard continues to apply, i.e., “constitutional questions, questions of law that are of central importance to the legal system as a whole and that are outside the adjudicator’s expertise, . . . ‘[q]uestions regarding the jurisdictional lines between two or more competing specialized tribunals’ [and] true questions of jurisdiction or vires . . . ”.

[39] As such, the respondent argues that the admissibility of new evidence before the RAD is within the tribunal’s expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.

## 23342:4 · paragraphs 39-51

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0ba876b0adcd47d6b6c92c8767dadcfc909e7546242b48539ab2e115e3e17bb8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:4:subtheme:1 · paragraphs 39-40

- Raw key terms: `agree, alberta, binnie, british, bureaucratic, canada, case, central`
- Display key terms: `agree, alberta, binnie, british, bureaucratic, case, central`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: agree, alberta, binnie, british, bureaucratic, case, central Rule/authority context: [41] In Alberta Teachers, Justice Binnie set out that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration. Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5096549` offsets `57-62`; context: [41] In Alberta Teachers, Justice Binnie set out that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.
- Evidence: `evidence_fact` cue `found that` at chunk `5096549` offsets `578-588`; context: In McLean v British Columbia (Securities Commission), 2013 SCC 67, the Court found that deference is owed to provincial securities’ regulators interpretation of statute of limitation provisions, despite it being a “technical” question, rather than a “bureaucratic” one.
- Evidence: `governing_rule` cue `under` at chunk `5096549` offsets `179-184`; context: [41] In Alberta Teachers, Justice Binnie set out that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.

#### 23342:4:subtheme:2 · paragraphs 41-42

- Raw key terms: `applicant, claim, evidence, expected, reasonably, time, accessibles, admit`
- Display key terms: `expected, reasonably, time, accessibles, admit`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: expected, reasonably, time, accessibles, admit Position/evidence statements: [44] The applicant argues that by not admitting the 2002 school diploma into evidence, the RAD failed to admit a document that not only goes to the core of his story, but also to the RPD’s finding of credibility which co Application context: [42] Therefore, I am of the view that both the RAD’s interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the  | The RAD failed to properly apply Raza, as this “new evidence” satisfies the Raza test insofar that the document: (a) is credible; (b) is pertinent; (c) is “new” in that it can refute a factual conclusion drawn by the RPD Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096550` offsets `106-114`; context: [42] Therefore, I am of the view that both the RAD’s interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096550` offsets `565-573`; context: Legislation [43] Subsection 110(4) and paragraph 113(a) of the Immigration and Refugee Protection Act provide as follows:
110 (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5096550` offsets `5-14`; context: [42] Therefore, I am of the view that both the RAD’s interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.
- Evidence: `party_position` cue `argues` at chunk `5096551` offsets `19-25`; context: [44] The applicant argues that by not admitting the 2002 school diploma into evidence, the RAD failed to admit a document that not only goes to the core of his story, but also to the RPD’s finding of credibility which consequently, gravely prejudices his claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096551` offsets `77-85`; context: [44] The applicant argues that by not admitting the 2002 school diploma into evidence, the RAD failed to admit a document that not only goes to the core of his story, but also to the RPD’s finding of credibility which consequently, gravely prejudices his claim.
- Evidence: `reasoning_application` cue `apply` at chunk `5096551` offsets `289-294`; context: The RAD failed to properly apply Raza, as this “new evidence” satisfies the Raza test insofar that the document: (a) is credible; (b) is pertinent; (c) is “new” in that it can refute a factual conclusion drawn by the RPD; (d) is of substantial character; and (e) was not raised before the board through no fault of the applicant.
- Evidence: `counterargument_limitation` cue `but` at chunk `5096551` offsets `167-170`; context: [44] The applicant argues that by not admitting the 2002 school diploma into evidence, the RAD failed to admit a document that not only goes to the core of his story, but also to the RPD’s finding of credibility which consequently, gravely prejudices his claim.

#### 23342:4:subtheme:3 · paragraphs 43-46

- Raw key terms: `paragraph, applicant, available, because, claim, credibility, expressly, fact`
- Display key terms: `paragraph, available, because, credibility, expressly, fact`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: paragraph, available, because, credibility, expressly, fact Position/evidence statements: [46] Meanwhile, the respondent argues the RAD used the proper test by interpreting subsection 110(4) of the Act in light of similar wording in paragraph 113(a); an interpretation of the latter can assist this Court in in Application context: The document was of critical probative value to the applicant’s claim because it proved that he attended school with Bhupinder Singh at that time and that he was not lying about this fact; 2. | Accordingly, the respondent agrees that the series of factors set forth in Raza apply, and that it was available to the RAD to consider them. Evidence spans paragraphs 43-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096552` offsets `788-796`; context: The RAD recognized that the failure to produce the document was the fault of the lawyer yet nonetheless it blamed the applicant, whose case was entirely in the hands of his lawyer(s), and who likely did not know what documents may have been missing from his file or that the document in question was of such critical importance to his claim.
- Evidence: `evidence_fact` cue `testimony` at chunk `5096552` offsets `400-409`; context: Although the document was initially seized by the CBSA, the RPD did not believe this part of the applicant’s testimony when in fact it was true (i.
- Evidence: `reasoning_application` cue `because` at chunk `5096552` offsets `169-176`; context: The document was of critical probative value to the applicant’s claim because it proved that he attended school with Bhupinder Singh at that time and that he was not lying about this fact;
2.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5096552` offsets `291-299`; context: Although the document was initially seized by the CBSA, the RPD did not believe this part of the applicant’s testimony when in fact it was true (i.
- Evidence: `party_position` cue `argues` at chunk `5096553` offsets `31-37`; context: [46] Meanwhile, the respondent argues the RAD used the proper test by interpreting subsection 110(4) of the Act in light of similar wording in paragraph 113(a); an interpretation of the latter can assist this Court in interpreting the former.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5096553` offsets `243-254`; context: Accordingly, the respondent agrees that the series of factors set forth in Raza apply, and that it was available to the RAD to consider them.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096554` offsets `168-176`; context: [13] As I read paragraph 113(a), it is based on the premise that a negative refugee determination by the RPD must be respected by the PRRA officer, unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `5096554` offsets `2139-2146`; context: (b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

#### 23342:4:subtheme:4 · paragraphs 47-48

- Raw key terms: `above, applicant, asked, case, consider, documents, each, establish`
- Display key terms: `above, asked, case, consider, documents, each, establish`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: above, asked, case, consider, documents, each, establish Position/evidence statements: [47] The applicant was required to establish that he could not have reasonably been expected to provide the newly submitted documents at his RPD hearing. Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096556` offsets `146-154`; context: [15] I do not suggest that the questions listed above must be asked in any particular order, or that in every case the PRRA officer must ask each question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096556` offsets `217-225`; context: What is important is that the PRRA officer must consider all evidence that is presented, unless it is excluded on one of the grounds stated in paragraph [13] above.
- Evidence: `party_position` cue `submitted` at chunk `5096557` offsets `114-123`; context: [47] The applicant was required to establish that he could not have reasonably been expected to provide the newly submitted documents at his RPD hearing.

#### 23342:4:subtheme:5 · paragraphs 49-50

- Raw key terms: `paragraph, subsection, administrative, appeal, application, applications, aside, automatic`
- Display key terms: `paragraph, subsection, administrative, applications, aside, automatic`
- Argument roles: `disposition, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position Display terms: paragraph, subsection, administrative, applications, aside, automatic Position/evidence statements: [49] Unlike a PRRA officer, the RAD is a quasi-judicial administrative tribunal, trusted to act as an instance of appeal of the RPD’s determination of a refugee’s claim. Rule/authority context: [48] It is worthwhile to explore whether it is reasonable for there to be an application of paragraph 113(a) jurisprudence when considering said paragraph mutatis mutandis to subsection 110(4) of the Act. | While both a PRRA decision and a RPD decision in certain instances of restriction—as detailed in subsection 110(2), are not subject to appeal, except in circumstances where there are applications for leave and for judici Operative outcome context: Moreover, in revisiting the RPD’s decision, unlike this Court, the RAD has the power—as expressly granted by the legislature under paragraph 111(b), to set aside the RPD’s decision and substitute a determination that, in Evidence spans paragraphs 49-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5096558` offsets `33-40`; context: [48] It is worthwhile to explore whether it is reasonable for there to be an application of paragraph 113(a) jurisprudence when considering said paragraph mutatis mutandis to subsection 110(4) of the Act.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5096558` offsets `109-122`; context: [48] It is worthwhile to explore whether it is reasonable for there to be an application of paragraph 113(a) jurisprudence when considering said paragraph mutatis mutandis to subsection 110(4) of the Act.
- Evidence: `party_position` cue `claim` at chunk `5096559` offsets `163-168`; context: [49] Unlike a PRRA officer, the RAD is a quasi-judicial administrative tribunal, trusted to act as an instance of appeal of the RPD’s determination of a refugee’s claim.
- Evidence: `governing_rule` cue `under` at chunk `5096559` offsets `462-467`; context: While both a PRRA decision and a RPD decision in certain instances of restriction—as detailed in subsection 110(2), are not subject to appeal, except in circumstances where there are applications for leave and for judicial review by this Court, the RPD’s determination of a claim not falling under the scope of a restriction stipulated under subsection 110(2) is subject to an automatic right of appeal to the RAD.
- Evidence: `disposition` cue `granted` at chunk `5096559` offsets `771-778`; context: Moreover, in revisiting the RPD’s decision, unlike this Court, the RAD has the power—as expressly granted by the legislature under paragraph 111(b), to set aside the RPD’s decision and substitute a determination that, in its opinion, should have been made.

#### 23342:4:subtheme:6 · paragraphs 51-51

- Raw key terms: `acting, appellate, assessed, assure, body, chance, circumscribed, claim`
- Display key terms: `acting, appellate, assessed, assure, body, chance, circumscribed`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: acting, appellate, assessed, assure, body, chance, circumscribed Evidence spans paragraphs 51-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5096560` offsets `513-520`; context: Instead, the PRRA officer is specifically looking as to whether new evidence has come to life since the RPD’s rejection of the claim for determining a risk of persecution, a danger of torture, a risk to life or a risk of cruel and unusual treatment or punishment.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096560` offsets `525-533`; context: Instead, the PRRA officer is specifically looking as to whether new evidence has come to life since the RPD’s rejection of the claim for determining a risk of persecution, a danger of torture, a risk to life or a risk of cruel and unusual treatment or punishment.
- Evidence: `counterargument_limitation` cue `but` at chunk `5096560` offsets `805-808`; context: The underlying rationale for paragraph 113(a) of the Act is not appellate in nature but rather to assure the claimant has a last chance to have any new risks of refoulement (not previously assessed by the RPD) assessed before removal can take place.

#### Section text

[40] I agree with the respondent.

[41] In Alberta Teachers, Justice Binnie set out that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.” The Supreme Court of Canada has since not identified a case that raised a “question of central importance to the legal system as a whole.” Moreover, since Alberta Teachers, the Supreme Court of Canada has reiterated its strict limitations to the use of the exceptions to the reasonableness standard. In McLean v British Columbia (Securities Commission), 2013 SCC 67, the Court found that deference is owed to provincial securities’ regulators interpretation of statute of limitation provisions, despite it being a “technical” question, rather than a “bureaucratic” one.

[42] Therefore, I am of the view that both the RAD’s interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.
V. Legislation [43] Subsection 110(4) and paragraph 113(a) of the Immigration and Refugee Protection Act provide as follows:
110 (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
110. (4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
113. Consideration of an application for protection shall be as follows:
(a) an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably available, or that the applicant could not reasonably have been expected in the circumstances to have presented, at the time of the rejection;
113. Il est disposé de la demande comme il suit:
a) le demandeur d’asile débouté ne peut présenter que des éléments de preuve survenus depuis le rejet ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’il n’était pas raisonnable, dans les circonstances, de s’attendre à ce qu’il les ait présentés au moment du rejet;
VI. Analysis • Was the RAD’s interpretation of subsection 110(4) of the Act reasonable?

[44] The applicant argues that by not admitting the 2002 school diploma into evidence, the RAD failed to admit a document that not only goes to the core of his story, but also to the RPD’s finding of credibility which consequently, gravely prejudices his claim. The RAD failed to properly apply Raza, as this “new evidence” satisfies the Raza test insofar that the document: (a) is credible; (b) is pertinent; (c) is “new” in that it can refute a factual conclusion drawn by the RPD; (d) is of substantial character; and (e) was not raised before the board through no fault of the applicant. The RAD could not have reasonably expected that it be produced by the applicant at the time of the RPD hearing.

[45] The applicant adds that the RAD failed to give sufficient weight to the following factors:
1. The document was of critical probative value to the applicant’s claim because it proved that he attended school with Bhupinder Singh at that time and that he was not lying about this fact;
2. Although the document was initially seized by the CBSA, the RPD did not believe this part of the applicant’s testimony when in fact it was true (i.e. this demonstrates that the applicant was not lying); and
3. The RAD recognized that the failure to produce the document was the fault of the lawyer yet nonetheless it blamed the applicant, whose case was entirely in the hands of his lawyer(s), and who likely did not know what documents may have been missing from his file or that the document in question was of such critical importance to his claim.

[46] Meanwhile, the respondent argues the RAD used the proper test by interpreting subsection 110(4) of the Act in light of similar wording in paragraph 113(a); an interpretation of the latter can assist this Court in interpreting the former. Accordingly, the respondent agrees that the series of factors set forth in Raza apply, and that it was available to the RAD to consider them. I quote the relevant parts of Raza in full:

[13] As I read paragraph 113(a), it is based on the premise that a negative refugee determination by the RPD must be respected by the PRRA officer, unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD. Paragraph 113(a) asks a number of questions, some expressly and some by necessary implication, about the proposed new evidence. I summarize those questions as follows:
1. Credibility: Is the evidence credible, considering its source and the circumstances in which it came into existence? If not, the evidence need not be considered.
2. Relevance: Is the evidence relevant to the PRRA application, in the sense that it is capable of proving or disproving a fact that is relevant to the claim for protection? If not, the evidence need not be considered.
3. Newness: Is the evidence new in the sense that it is capable of:
(a) proving the current state of affairs in the country of removal or an event that occurred or a circumstance that arose after the hearing in the RPD, or
(b) proving a fact that was unknown to the refugee claimant at the time of the RPD hearing, or
(c) contradicting a finding of fact by the RPD (including a credibility finding)?
If not, the evidence need not be considered.
4. Materiality: Is the evidence material, in the sense that the refugee claim probably would have succeeded if the evidence had been made available to the RPD? If not, the evidence need not be considered.
5. Express statutory conditions:
(a) If the evidence is capable of proving only an event that occurred or circumstances that arose prior to the RPD hearing, then has the applicant established either that the evidence was not reasonably available to him or her for presentation at the RPD hearing, or that he or she could not reasonably have been expected in the circumstances to have presented the evidence at the RPD hearing? If not, the evidence need not be considered.
(b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

[14] The first four questions, relating to credibility, relevance, newness and materiality, are necessarily implied from the purpose of paragraph 113(a) within the statutory scheme of the IRPA relating to refugee claims and pre removal risk assessments. The remaining questions are asked expressly by paragraph 113(a).

[15] I do not suggest that the questions listed above must be asked in any particular order, or that in every case the PRRA officer must ask each question. What is important is that the PRRA officer must consider all evidence that is presented, unless it is excluded on one of the grounds stated in paragraph [13] above.

[47] The applicant was required to establish that he could not have reasonably been expected to provide the newly submitted documents at his RPD hearing. The respondent maintains the RAD did not err in finding that he failed to do so.

[48] It is worthwhile to explore whether it is reasonable for there to be an application of paragraph 113(a) jurisprudence when considering said paragraph mutatis mutandis to subsection 110(4) of the Act.

[49] Unlike a PRRA officer, the RAD is a quasi-judicial administrative tribunal, trusted to act as an instance of appeal of the RPD’s determination of a refugee’s claim. While both a PRRA decision and a RPD decision in certain instances of restriction—as detailed in subsection 110(2), are not subject to appeal, except in circumstances where there are applications for leave and for judicial review by this Court, the RPD’s determination of a claim not falling under the scope of a restriction stipulated under subsection 110(2) is subject to an automatic right of appeal to the RAD. Only upon receiving the “final” RAD decision can the claimant seek leave to this Court. Moreover, in revisiting the RPD’s decision, unlike this Court, the RAD has the power—as expressly granted by the legislature under paragraph 111(b), to set aside the RPD’s decision and substitute a determination that, in its opinion, should have been made.

[50] A PRRA officer is not a quasi-judicial body, nor does he or she have an appellate function when faced with a RPD decision. The PRRA officer is an employee of the Minister, acting within his or her employer’s discretion (insofar as it is circumscribed by the Act and the Regulations). The PRRA officer must give deference to the RPD’s determination of the claim, to the extent that the facts remain unchanged from the time it had rendered its decision. Instead, the PRRA officer is specifically looking as to whether new evidence has come to life since the RPD’s rejection of the claim for determining a risk of persecution, a danger of torture, a risk to life or a risk of cruel and unusual treatment or punishment. The underlying rationale for paragraph 113(a) of the Act is not appellate in nature but rather to assure the claimant has a last chance to have any new risks of refoulement (not previously assessed by the RPD) assessed before removal can take place.

## 23342:5 · paragraphs 52-66

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b98f55d2c66276914569c4c78810e055fe45679ea652194a28727d05264f0214`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:5:subtheme:1 · paragraphs 52-53

- Raw key terms: `admissible, appeal, appellate, arose, available, circumstances, claim, considers`
- Display key terms: `admissible, appellate, arose, available, circumstances, considers`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: admissible, appellate, arose, available, circumstances, considers Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096561` offsets `139-147`; context: The latter provision sets out that the RAD can only declare evidence admissible if it arose after the RPD’s rejection of the claim or if it was not reasonably available or if the person could not reasonably have been expected in the circumstances to have presented it (unlike for paragraph 113(a), the French version of subsection 110(4) does not use “reasonably have been expected” but rather the equivalent of “normally have been expected”).

#### 23342:5:subtheme:2 · paragraphs 54-58

- Raw key terms: `appeal, claimant, admissibility, criteria, evidence, fact-based, full, hearing`
- Display key terms: `admissibility, criteria, fact-based, full, hearing`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: admissibility, criteria, fact-based, full, hearing Application context: Given this requirement, the approach taken to applying admissibility criteria - either strictly or leniently - is of paramount importance because when a claimant, who is deserving of a hearing, is refused one, serious is | [55] Accordingly, in order for there to be a “full fact-based appeal” before the RAD, the criteria for the admissibility of evidence must be sufficiently flexible to ensure it can occur. Operative outcome context: In the case at bar, the applicant was in fact denied a hearing because the 2002 school diploma was deemed inadmissible. Evidence spans paragraphs 54-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5096563` offsets `29-36`; context: [53] However, in considering whether to grant a hearing, the RAD may only look to admissible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096563` offsets `93-101`; context: [53] However, in considering whether to grant a hearing, the RAD may only look to admissible evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5096563` offsets `241-248`; context: Given this requirement, the approach taken to applying admissibility criteria - either strictly or leniently - is of paramount importance because when a claimant, who is deserving of a hearing, is refused one, serious issues of procedural equity are potentially implicated.
- Evidence: `disposition` cue `denied` at chunk `5096563` offsets `423-429`; context: In the case at bar, the applicant was in fact denied a hearing because the 2002 school diploma was deemed inadmissible.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096565` offsets `124-132`; context: [55] Accordingly, in order for there to be a “full fact-based appeal” before the RAD, the criteria for the admissibility of evidence must be sufficiently flexible to ensure it can occur.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5096565` offsets `5-16`; context: [55] Accordingly, in order for there to be a “full fact-based appeal” before the RAD, the criteria for the admissibility of evidence must be sufficiently flexible to ensure it can occur.
- Evidence: `reasoning_application` cue `apply` at chunk `5096567` offsets `79-84`; context: [57] In sum, I am of the view that it was unreasonable for the RAD to strictly apply the Raza test in interpreting subsection 110(4) of the Act all the while failing to appreciate that its role is quite different from that of a PRRA officer.

#### 23342:5:subtheme:3 · paragraphs 59-62

- Raw key terms: `applicant, evidence, believed, cbsa, document, fact, file, lawyer`
- Display key terms: `believed, cbsa, document, fact, file, lawyer`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: believed, cbsa, document, fact, file, lawyer Application context: [60] Moreover, it was not reasonable for the RAD to conclude that the applicant should have brought the documentary evidence before the RPD. Evidence spans paragraphs 59-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5096568` offsets `161-166`; context: [58] In order to achieve statutory coherence, in that the RAD would be able to hear fleshed out appeals of questions of fact and of mixed fact and law, the main issue is whether the evidence “was not reasonably available, or that the person could not reasonably (or normally according to the French version) have been expected in the circumstances to have presented.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096568` offsets `182-190`; context: [58] In order to achieve statutory coherence, in that the RAD would be able to hear fleshed out appeals of questions of fact and of mixed fact and law, the main issue is whether the evidence “was not reasonably available, or that the person could not reasonably (or normally according to the French version) have been expected in the circumstances to have presented.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096569` offsets `116-124`; context: [60] Moreover, it was not reasonable for the RAD to conclude that the applicant should have brought the documentary evidence before the RPD.
- Evidence: `reasoning_application` cue `conclude` at chunk `5096569` offsets `52-60`; context: [60] Moreover, it was not reasonable for the RAD to conclude that the applicant should have brought the documentary evidence before the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096570` offsets `156-164`; context: [61] In my mind, it was unreasonable for the RAD to expect the applicant to file a complaint against his former lawyer as a prerequisite for filing the new evidence before the RAD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5096571` offsets `46-54`; context: [62] The applicant’s request to file this new evidence fell squarely, in my view, within the scope of subsection 110(4) of the Act and it met its explicit criteria.

#### 23342:5:subtheme:4 · paragraphs 63-64

- Raw key terms: `general, hearing, importance, proposed, question, appeal, applicant, asked`
- Display key terms: `hearing, importance, proposed, question, asked`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: hearing, importance, proposed, question, asked Evidence spans paragraphs 63-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096572` offsets `75-83`; context: [63] Counsels for the parties were asked at the hearing if they proposed a question of general importance for certification, which they did not.
- Evidence: `issue` cue `question` at chunk `5096573` offsets `181-189`; context: [64] As a result of certain comments made by the Court during the hearing, counsel for the respondent, with the consent of counsel for the applicant, subsequently proposed the same question of general importance as was proposed before Justice Phelan in Huruglica:
Within the RAD’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division, does the RAD owe deference to RPD findings of fact and of mixed fact and law?
- Evidence: `evidence_fact` cue `record` at chunk `5096573` offsets `347-353`; context: [64] As a result of certain comments made by the Court during the hearing, counsel for the respondent, with the consent of counsel for the applicant, subsequently proposed the same question of general importance as was proposed before Justice Phelan in Huruglica:
Within the RAD’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division, does the RAD owe deference to RPD findings of fact and of mixed fact and law?

#### 23342:5:subtheme:5 · paragraphs 65-66

- Raw key terms: `citizenship, immigration, minister, above, appeal, applicant, application, applied`
- Display key terms: `above, applied`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: above, applied Rule/authority context: However, I view the following questions as being of general importance and determinative in the case at bar: • What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpre Application context: However, I view the following questions as being of general importance and determinative in the case at bar: • What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpre Operative outcome context: Conclusion [66] For these reasons, I find that both the RAD’s interpretation of subsection 110(4) of the Act and its application to the facts before it are unreasonable such that the application for judicial review shoul Evidence spans paragraphs 65-66. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5096574` offsets `52-60`; context: [65] As indicated above, I am of the view that said question is not determinative of the present case and that it would not be determinative of an appeal.
- Evidence: `governing_rule` cue `standard of review` at chunk `5096574` offsets `271-289`; context: However, I view the following questions as being of general importance and determinative in the case at bar:
• What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of subsection 110(4) of the Immigration and Refugee Protection Act, SC 2001, c 27?
- Evidence: `reasoning_application` cue `applied` at chunk `5096574` offsets `300-307`; context: However, I view the following questions as being of general importance and determinative in the case at bar:
• What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of subsection 110(4) of the Immigration and Refugee Protection Act, SC 2001, c 27?
- Evidence: `counterargument_limitation` cue `However` at chunk `5096574` offsets `155-162`; context: However, I view the following questions as being of general importance and determinative in the case at bar:
• What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of subsection 110(4) of the Immigration and Refugee Protection Act, SC 2001, c 27?
- Evidence: `disposition` cue `granted` at chunk `5096574` offsets `1139-1146`; context: Conclusion [66] For these reasons, I find that both the RAD’s interpretation of subsection 110(4) of the Act and its application to the facts before it are unreasonable such that the application for judicial review should be granted and the above questions certified.

#### Section text

[51] The language of paragraph 113(a) is similar to that of subsection 110(4). The latter provision sets out that the RAD can only declare evidence admissible if it arose after the RPD’s rejection of the claim or if it was not reasonably available or if the person could not reasonably have been expected in the circumstances to have presented it (unlike for paragraph 113(a), the French version of subsection 110(4) does not use “reasonably have been expected” but rather the equivalent of “normally have been expected”). The RAD however considers this evidence in a very different light than does the PRRA officer; it is doing so in an appellate review of the correctness of the RPD’s determination.

[52] I recognize that an appeal to the RAD is mostly intended as a “paper-based” appeal.

[53] However, in considering whether to grant a hearing, the RAD may only look to admissible evidence. Given this requirement, the approach taken to applying admissibility criteria - either strictly or leniently - is of paramount importance because when a claimant, who is deserving of a hearing, is refused one, serious issues of procedural equity are potentially implicated. In the case at bar, the applicant was in fact denied a hearing because the 2002 school diploma was deemed inadmissible.

[54] Further, a restrictive interpretation of this new section would limit the ability of a claimant to get a “full fact-based appeal,” as former Minister of Citizenship and Immigration Jason Kenney intended. I quote his remarks in Hansard (41st Parliament, 1st Session, Tuesday March 6, 2012):
“I reiterate that the bill would also create the new refugee appeal division. The vast majority of claimants who are coming from countries that do normally produce refugees would for the first time, if rejected at the refugee protection division, have access to a full fact-based appeal at the refugee appeal division of the IRB. This is the first government to have created a full fact-based appeal.” [Emphasis added.]

[55] Accordingly, in order for there to be a “full fact-based appeal” before the RAD, the criteria for the admissibility of evidence must be sufficiently flexible to ensure it can occur. Often, the evidence at stake will be essential for proving the factual basis of the errors the claimant alleges were made by the RPD. This consideration becomes all the more pertinent in light of the strict timelines a claimant now faces for initially submitting evidence before the RPD. A claimant now has 50 days to present all documents from the date he or she made the claim; the previous legislative scheme required the documents 20 days prior to a hearing, which, on average, took much longer to take place. When the RPD confronts a claimant on the weakness of his evidentiary record, the RAD should, in subsequent review of the decision, have some leeway in order to allow the claimant to respond to the deficiencies raised

[56] But there is more. In Raza, Justice Sharlow distinguishes between the express and the implicit questions raised by paragraph 113(a) of the Act and specifically states that the four implied questions (credibility, relevance, newness and materiality) find their source in the purpose of paragraph 113(a) within the statutory scheme of the Act relating to refugee claims and PRRA applications. In my view, they need to be addressed in that specific context and are not transferable in the context of an appeal before the RAD.

[57] In sum, I am of the view that it was unreasonable for the RAD to strictly apply the Raza test in interpreting subsection 110(4) of the Act all the while failing to appreciate that its role is quite different from that of a PRRA officer.

[58] In order to achieve statutory coherence, in that the RAD would be able to hear fleshed out appeals of questions of fact and of mixed fact and law, the main issue is whether the evidence “was not reasonably available, or that the person could not reasonably (or normally according to the French version) have been expected in the circumstances to have presented.”
Was the RAD’s application of subsection 110(4) of the Act to the facts of this case reasonable? [59] In the case at bar, the evidence at issue could be material for demonstrating that the RPD erred in two key credibility findings: first, the RPD wrongly believed that the CBSA had not confiscated the 2002 diploma, and second, that the document lends further credence that the applicant did in fact go to school with Bhupinder Singh until 2002. These findings surely affected the totality of the credibility assessment made by the RPD.

[60] Moreover, it was not reasonable for the RAD to conclude that the applicant should have brought the documentary evidence before the RPD. The document was not in his possession, and he mistakenly believed that CBSA still had it, based on the fact that the agency had seized it from him initially. The RAD seemingly recognized that the failure to produce the document was the fault of the lawyer. The CBSA had faxed it to the lawyer after the RPD hearing and the lawyer had failed to forward it to the applicant before the RAD determination.

[61] In my mind, it was unreasonable for the RAD to expect the applicant to file a complaint against his former lawyer as a prerequisite for filing the new evidence before the RAD. It was unreasonable for the RAD to expect the applicant to know of the complaints procedure before the Barreau du Québec, much less be willing to attack the competence and ethics of that lawyer.

[62] The applicant’s request to file this new evidence fell squarely, in my view, within the scope of subsection 110(4) of the Act and it met its explicit criteria.
* * *

[63] Counsels for the parties were asked at the hearing if they proposed a question of general importance for certification, which they did not.

[64] As a result of certain comments made by the Court during the hearing, counsel for the respondent, with the consent of counsel for the applicant, subsequently proposed the same question of general importance as was proposed before Justice Phelan in Huruglica:
Within the RAD’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division, does the RAD owe deference to RPD findings of fact and of mixed fact and law?

[65] As indicated above, I am of the view that said question is not determinative of the present case and that it would not be determinative of an appeal. However, I view the following questions as being of general importance and determinative in the case at bar:
• What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of subsection 110(4) of the Immigration and Refugee Protection Act, SC 2001, c 27?
• In considering the role of a Pre-Removal Risk Assessment officer and that of the Refugee Appeal Division of the Immigration and Refugee Board, sitting in appeal of a decision of the Refugee Protection Division, does the test set out in Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385 for the interpretation of paragraph 113(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 apply to its subsection 110(4)?
VII. Conclusion [66] For these reasons, I find that both the RAD’s interpretation of subsection 110(4) of the Act and its application to the facts before it are unreasonable such that the application for judicial review should be granted and the above questions certified.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The applicant’s Application for Judicial Review is granted;
2. The decision of the Refugee Appeal Division of the Immigration and Refugee Board, dated September 26, 2013, is set aside and the matter is remitted back to a different member for re-determination;
3. The following questions of general importance are certified:
• What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of subsection 110(4) of the Immigration and Refugee Protection Act, SC 2001, c 27?
• In considering the role of a Pre-Removal Risk Assessment officer and that of the Refugee Appeal Division of the Immigration and Refugee Board, sitting in appeal of a decision of the Refugee Protection Division, does the test set out in Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385 for the interpretation of paragraph 113(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 apply to its subsection 110(4)?
"Jocelyne Gagné"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6711-13
STYLE OF CAUSE:
PARMINDER SINGH v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, Quebec
DATE OF HEARING:
July 2, 2014


## 23342:6 · paragraphs 67-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7a33c8d7a5f4aede7e272a56fd3b47d89c6a35049f2e66877dc18ac2c4d8133e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23342:6:subtheme:1 · paragraphs 67-67

- Raw key terms: `appearances, applicant, attorney, barrister, blanchard, canada, claude, dated`
- Display key terms: `barrister, blanchard, claude, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, blanchard, claude, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 67-67. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GAGNÉ J.
DATED:
October 28, 2014
APPEARANCES:
Me Claude Whalen
For The Applicant
Me Mario Blanchard
For The Respondent
SOLICITORS OF RECORD:
Me Claude Whalen
Barrister and Solicitor
Montréal, Quebec
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
For The Respondent
