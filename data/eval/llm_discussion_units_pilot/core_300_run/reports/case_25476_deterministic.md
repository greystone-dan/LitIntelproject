# Discussion Units: case 25476

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **68**
- Continuity pairs: **67**
- Discussion Units: **5**
- Paragraph source hashes: **68**
- Sub-themes: **14**

## 25476:1 · paragraphs 0-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b741f3609a05d76c92a4974ce5d174cf245a3bcefc4a1a01ffed03028f62d0a2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25476:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, canada, decision, falun, gong, group, identity, immigration`
- Display key terms: `falun, gong, group, identity`
- Argument roles: `evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position Display terms: falun, gong, group, identity Position/evidence statements: [5] On 16 November 2009, the Applicant claimed protection in Canada. | [7] Prior to the hearing, the Applicant submitted several documents to the RPD to prove his identity: his Resident Identity Card (RIC), household register card (Hukou), a Divorce Certificate, and an out-patient record fr Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c. | DECISION UNDER REVIEW Allegations Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5199351` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c.
- Evidence: `party_position` cue `claimed` at chunk `5199355` offsets `39-46`; context: [5] On 16 November 2009, the Applicant claimed protection in Canada.
- Evidence: `governing_rule` cue `UNDER` at chunk `5199355` offsets `219-224`; context: DECISION UNDER REVIEW
Allegations
- Evidence: `party_position` cue `submitted` at chunk `5199357` offsets `40-49`; context: [7] Prior to the hearing, the Applicant submitted several documents to the RPD to prove his identity: his Resident Identity Card (RIC), household register card (Hukou), a Divorce Certificate, and an out-patient record from the Medical Institute of Fu Zhou City (Out-patient Record).
- Evidence: `evidence_fact` cue `record` at chunk `5199357` offsets `211-217`; context: [7] Prior to the hearing, the Applicant submitted several documents to the RPD to prove his identity: his Resident Identity Card (RIC), household register card (Hukou), a Divorce Certificate, and an out-patient record from the Medical Institute of Fu Zhou City (Out-patient Record).

#### 25476:1:subtheme:2 · paragraphs 8-10

- Raw key terms: `applicant, canada, citizen, documents, found, weight, actually, addition`
- Display key terms: `citizen, documents, weight, actually, addition`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: citizen, documents, weight, actually, addition Position/evidence statements: [9] The RPD also noted that the Applicant’s Hukou and Divorce Certificate contained the same identification number as the RIC he had submitted. Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5199358` offsets `281-287`; context: The RPD found that this answer did not address the issues raised in the Forensic Report and gave more weight to the Forensic Report than to the Applicant’s testimony, noting that the Forensic Report was authored by experts in counterfeiting.
- Evidence: `evidence_fact` cue `found that` at chunk `5199358` offsets `238-248`; context: The RPD found that this answer did not address the issues raised in the Forensic Report and gave more weight to the Forensic Report than to the Applicant’s testimony, noting that the Forensic Report was authored by experts in counterfeiting.
- Evidence: `issue` cue `whether` at chunk `5199359` offsets `358-365`; context: The Out-patient Record contained limited information about the Applicant’s citizenship so the RPD placed little weight on it in determining whether he was actually a citizen of the PRC.
- Evidence: `party_position` cue `submitted` at chunk `5199359` offsets `133-142`; context: [9] The RPD also noted that the Applicant’s Hukou and Divorce Certificate contained the same identification number as the RIC he had submitted.
- Evidence: `evidence_fact` cue `found that` at chunk `5199359` offsets `169-179`; context: For this reason, the RPD found that these documents were also fraudulent.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5199360` offsets `64-73`; context: [10] In addition to his identity documents, the RPD examined an affidavit from the Applicant’s daughter in Canada.

#### 25476:1:subtheme:3 · paragraphs 11-18

- Raw key terms: `applicant, found, falun, gong, article, criminal, documents, notice`
- Display key terms: `falun, gong, article, criminal, documents, notice`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: falun, gong, article, criminal, documents, notice Position/evidence statements: [11] In addition to the concerns it had with the Applicants identity documents, the RPD was troubled by other documents he submitted to prove his claim. | ” Although the translation at the hearing and the translation the Applicant submitted both referred to Article 92, in the Decision the RPD said that the difference in interpretation did not account for the difference in  Rule/authority context: The translated copy of the Notice the Applicant submitted indicated that he was summoned to the PSB in Chang Le City under the “Regulations of the ‘Criminal Law of the People’s Republic of China, Article 92, section 1”. Operative outcome context: The RPD denied his claim. Evidence spans paragraphs 11-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5199361` offsets `671-676`; context: net: Criminal Law of the People’s Republic of China, established that Article 92(1) of the Criminal Law of the PRC refers to “citizens’ lawful income, savings, houses and other means of livelihood” which gives no authority to anyone to issue a Notice.
- Evidence: `party_position` cue `submitted` at chunk `5199361` offsets `123-132`; context: [11] In addition to the concerns it had with the Applicants identity documents, the RPD was troubled by other documents he submitted to prove his claim.
- Evidence: `governing_rule` cue `under` at chunk `5199361` offsets `270-275`; context: The translated copy of the Notice the Applicant submitted indicated that he was summoned to the PSB in Chang Le City under the “Regulations of the ‘Criminal Law of the People’s Republic of China, Article 92, section 1”.
- Evidence: `evidence_fact` cue `found that` at chunk `5199362` offsets `119-129`; context: The RPD found that there was a significant difference between the appearance and content of the information in the Notice and the examples in RIR CHN42444.
- Evidence: `party_position` cue `submitted` at chunk `5199363` offsets `500-509`; context: ” Although the translation at the hearing and the translation the Applicant submitted both referred to Article 92, in the Decision the RPD said that the difference in interpretation did not account for the difference in the article number.
- Evidence: `evidence_fact` cue `found that` at chunk `5199363` offsets `672-682`; context: The RPD found that the Notice was fraudulent, based on its concerns about the Applicant’s other documents and the differences between the Notice before it and the examples in RIR CHN42444.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5199363` offsets `426-434`; context: ” Although the translation at the hearing and the translation the Applicant submitted both referred to Article 92, in the Decision the RPD said that the difference in interpretation did not account for the difference in the article number.
- Evidence: `party_position` cue `submitted` at chunk `5199364` offsets `24-33`; context: [14] The Applicant also submitted a visiting card from Bai Sha Prison in Fu Zhou City (Visiting Card).
- Evidence: `evidence_fact` cue `found that` at chunk `5199364` offsets `111-121`; context: The RPD found that this document did not show that a member of the Applicant’s group had been arrested.
- Evidence: `evidence_fact` cue `found that` at chunk `5199365` offsets `13-23`; context: [15] The RPD found that the Applicant was not a Falun Gong practitioner in the PRC, that there had been no raid or arrests, and that the authorities in the PRC were not looking for him.
- Evidence: `evidence_fact` cue `testimony` at chunk `5199366` offsets `308-317`; context: The RPD reviewed the Applicant’s testimony that he had practised alone every day while he was in the PRC and had practiced in a group once per week.
- Evidence: `evidence_fact` cue `found that` at chunk `5199367` offsets `106-116`; context: [17] Although the Applicant had testified that he had attended classes to learn about Falun Gong, the RPD found that he had given vague answers when asked about what he had learned.
- Evidence: `evidence_fact` cue `found that` at chunk `5199368` offsets `13-23`; context: [18] The RPD found that the Applicant had not discharged the burden on him to establish a serious possibility that he would be persecuted or that he faced a risk to his life or of cruel and unusual treatment or punishment or a risk of torture if he were returned to the PRC.
- Evidence: `disposition` cue `denied` at chunk `5199368` offsets `283-289`; context: The RPD denied his claim.

#### Section text

Lin v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-03-05
Neutral citation
2012 FC 288
File numbers
IMM-4836-11
Decision Content
Federal Court
Cour fédérale
Date: 20120305
Docket: IMM-4836-11
Citation: 2012 FC 288
Ottawa, Ontario, March 5, 2012
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
LIEN LIN
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
INTRODUCTION

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC­ 2001, c. 27 (Act) for judicial review of the decision of the Refugee Protection Division (RPD) of the Immigration and Refugee Board, dated 29 June 2011 (Decision), which refused the Applicant’s application to be deemed a Convention refugee or a person in need of protection under sections 96 and 97 of the Act.
BACKGROUND

[2] The Applicant is a 57-year-old citizen of the People’s Republic of China (PRC) who says he is a Falun Gong practitioner. He has a son and daughter living Canada.

[3] In 2008, one of the Applicant’s friends introduced him to the practice of Falun Gong. He says he began practising Falun Gong exercises at his home in December 2008 and joined a group in January 2009. The Applicant says that his group was raided by agents of the Public Security Bureau (PSB) on 22 August 2009. The instructor and two members of the group were arrested at that time. After the raid, the Applicant went into hiding and, on 23 August 2009, PSB agents went to his home to look for him. While they were at his home, the PSB interrogated his mother and brother, and then left a Notice of Summoning (Notice), which required him to attend at the PSB office in Chang Le. The PSB also searched for him at the homes of his other siblings in the PRC.

[4] In February 2010, the Applicant learned from his mother that his group instructor had been sentenced to four years imprisonment. The other two members of his group were each sentenced to three years imprisonment. The Applicant was afraid that he too would be imprisoned, so he hired a smuggler and fled the PRC. The Applicant travelled to Hong Kong on 10 October 2009 and then to Toronto on the same day.

[5] On 16 November 2009, the Applicant claimed protection in Canada. The RPD heard his claim on 19 May 2011 and made its Decision on 29 June 2011. The RPD notified the Applicant of its Decision on 6 July 2011.
DECISION UNDER REVIEW
Allegations

[6] The RPD reviewed the Applicant’s story of his conversion to Falun Gong, the raid on his group, the PSB’s interrogation of his family, and the imprisonment of his fellow practitioners.
Identity

[7] Prior to the hearing, the Applicant submitted several documents to the RPD to prove his identity: his Resident Identity Card (RIC), household register card (Hukou), a Divorce Certificate, and an out-patient record from the Medical Institute of Fu Zhou City (Out-patient Record). To establish the authenticity of his documents, the RPD sent them to the RCMP Forensic Science and Identification Services Laboratory (RCMP Lab) for analysis. In its report (Forensic Report) the RCMP Lab said it did not have a genuine specimen for comparison, so the authenticity of the Applicant’s RIC was inconclusive. The Forensic Report also noted that the RIC was printed with an inkjet printer and that this was not known as a means for printing genuine RICs.

[8] At the hearing, the RPD presented the Applicant with the Forensic Report and asked him to comment. He said that his RIC was in his possession at all times, except when it was with the smuggler he hired to bring him to Canada. The RPD found that this answer did not address the issues raised in the Forensic Report and gave more weight to the Forensic Report than to the Applicant’s testimony, noting that the Forensic Report was authored by experts in counterfeiting. The RPD found that the RIC was not authentic.

[9] The RPD also noted that the Applicant’s Hukou and Divorce Certificate contained the same identification number as the RIC he had submitted. For this reason, the RPD found that these documents were also fraudulent. The Out-patient Record contained limited information about the Applicant’s citizenship so the RPD placed little weight on it in determining whether he was actually a citizen of the PRC. The RPD also noted that the Immigration and Refugee Board’s Response to Information Request (RIR) CHN103134.E indicates that fraudulent documents are readily available in the PRC.

[10] In addition to his identity documents, the RPD examined an affidavit from the Applicant’s daughter in Canada. In her affidavit, she said that the Applicant was her father and that he was a citizen of the PRC. The daughter’s affidavit persuaded the RPD that the Applicant is a citizen of the PRC.
Other Documents

[11] In addition to the concerns it had with the Applicants identity documents, the RPD was troubled by other documents he submitted to prove his claim. The translated copy of the Notice the Applicant submitted indicated that he was summoned to the PSB in Chang Le City under the “Regulations of the ‘Criminal Law of the People’s Republic of China, Article 92, section 1”. The RPD noted that a document printed from http://www.com-law.net: Criminal Law of the People’s Republic of China, established that Article 92(1) of the Criminal Law of the PRC refers to “citizens’ lawful income, savings, houses and other means of livelihood” which gives no authority to anyone to issue a Notice.

[12] The RPD also referred to RIR CHN42444.E, which identifies different kinds of summonses issued in the PRC. The RPD found that there was a significant difference between the appearance and content of the information in the Notice and the examples in RIR CHN42444.E. The RIR said that a Notice of Summons to testify refers to Article 92 of the PRC Criminal Procedure Law.

[13] At the hearing, Applicant’s counsel identified a potential problem in the translation of the Notice. Counsel said that he thought it did not say “criminal law of the People’s Republic of China,” as the translator he had hired said it did. The RPD’s interpreter examined the Notice at the hearing and translated it as saying “the first section of the article 92 of the People’s Republic of China criminal litigation law.” Although the translation at the hearing and the translation the Applicant submitted both referred to Article 92, in the Decision the RPD said that the difference in interpretation did not account for the difference in the article number. The RPD found that the Notice was fraudulent, based on its concerns about the Applicant’s other documents and the differences between the Notice before it and the examples in RIR CHN42444.E.

[14] The Applicant also submitted a visiting card from Bai Sha Prison in Fu Zhou City (Visiting Card). The RPD found that this document did not show that a member of the Applicant’s group had been arrested. It based this finding on the Applicant having tendered other false documents and RIR CHN103134.E, which indicate that fraudulent documents were readily available in the PRC.
Falun Gong Practice

[15] The RPD found that the Applicant was not a Falun Gong practitioner in the PRC, that there had been no raid or arrests, and that the authorities in the PRC were not looking for him.

[16] The RPD noted that it was difficult to assess if the Applicant is a genuine Falun Gong practitioner and said that it had taken into account his three years of formal education. It also said it had considered the fact that he had only practised Falun Gong for 2 ½ years. The RPD reviewed the Applicant’s testimony that he had practised alone every day while he was in the PRC and had practiced in a group once per week. He said his practice involved learning the movements of Falun Gong exercises and listening to his instructor talk about the benefits of Falun Gong. When the RPD asked the Applicant about the Zhuan Falun – the main text of Falun Gong – he could not remember details. He also testified that he practised alone at home in Canada and joined a group here one month after he arrived.

[17] Although the Applicant had testified that he had attended classes to learn about Falun Gong, the RPD found that he had given vague answers when asked about what he had learned. The RPD found that the Applicant had knowledge of the major Falun Gong books, and what “falun” was, but also found that he had difficulty explaining the purposes of Falun Gong exercises. He was unable to identify some aspects of the first and fourth exercises. The RPD found that the Applicant was not a genuine Falun Gong practitioner. It relied on a quotation from Master Li – the founder of Falun Gong – and said that failure to understand the philosophies of Falun Gong makes practising Falun Gong exercises no more beneficial than any other qigong exercises.
Conclusion

[18] The RPD found that the Applicant had not discharged the burden on him to establish a serious possibility that he would be persecuted or that he faced a risk to his life or of cruel and unusual treatment or punishment or a risk of torture if he were returned to the PRC. The RPD denied his claim.
STATUTORY PROVISIONS

## 25476:2 · paragraphs 19-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c99d20e64ce4b6a31f08924451bab547231ee8785877330a4209497eae554b8e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25476:2:subtheme:1 · paragraphs 19-19

- Raw key terms: `accepted, adequate, against, alors, appartenance, applicable, article, autres`
- Display key terms: `accepted, adequate, against, alors, appartenance, applicable, article, autres`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accepted, adequate, against, alors, appartenance, applicable, article, autres Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj Evidence spans paragraphs 19-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5199369` offsets `3333-3339`; context: […]
ISSUES
- Evidence: `reasoning_application` cue `because` at chunk `5199369` offsets `1175-1182`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
[…]
Définition de « réfugié »
96.

#### Section text

[19] The following provisions of the Act are applicable in this proceeding:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political
opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
Person in Need of Protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning ­ of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
[…]
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa
résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
[…]
ISSUES

## 25476:3 · paragraphs 20-64

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cc2811867b10a4ec7bf580c3a5489480965b2bb1d74e2676278a227da1ec08bc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25476:3:subtheme:1 · paragraphs 20-21

- Raw key terms: `review, standard, adopt, analysis, applicable, applicant, application, brunswick`
- Display key terms: `review, standard, adopt, analysis, applicable, brunswick`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: review, standard, adopt, analysis, applicable, brunswick Rule/authority context: STANDARD OF REVIEW | [21] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5199370` offsets `40-46`; context: [20] The Applicant raises the following issues in this application:
a.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5199370` offsets `249-267`; context: STANDARD OF REVIEW
- Evidence: `issue` cue `question` at chunk `5199371` offsets `220-228`; context: Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `5199371` offsets `86-104`; context: [21] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance.

#### 25476:3:subtheme:2 · paragraphs 22-33

- Raw key terms: `applicant, fraudulent, finding, says, unreasonable, because, canada, citizenship`
- Display key terms: `fraudulent, finding, says, unreasonable, because`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: fraudulent, finding, says, unreasonable, because Position/evidence statements: A finding that one identity document is fraudulent is not enough to establish that all of the documents a claimant submits are untrustworthy. Rule/authority context: It is well established that findings of fact are to be examined on a standard of review of reasonableness. | [33] The RPD said in the Decision that Even taking into consideration his limited formal education and his allegedly recent practice of Falun Gong, the determination he was not a Falun Gong practitioner in China and the  Application context: Contrary to the RPD’s finding, the Applicant says that his RIC is actually consistent with other genuine RICs so the RPD had no reasonable basis to conclude that his RIC is fraudulent. | The RPD found that his Hukou and Divorce Certificate are fraudulent because they contain the same identity number as appeared in the RIC. Evidence spans paragraphs 22-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5199372` offsets `10-16`; context: [22] Both issues the Applicant has raised in this case challenge the RPD’s findings of fact.
- Evidence: `governing_rule` cue `standard of review` at chunk `5199372` offsets `162-180`; context: It is well established that findings of fact are to be examined on a standard of review of reasonableness.
- Evidence: `issue` cue `whether` at chunk `5199373` offsets `219-226`; context: [23] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `party_position` cue `submits` at chunk `5199374` offsets `399-406`; context: A finding that one identity document is fraudulent is not enough to establish that all of the documents a claimant submits are untrustworthy.
- Evidence: `evidence_fact` cue `evidence` at chunk `5199374` offsets `250-258`; context: He says that Rasheed v Canada (Minister of Citizenship and Immigration) 2004 FC 587 establishes that documents should be presumed valid unless there is evidence to suggest they are not.
- Evidence: `evidence_fact` cue `found that` at chunk `5199375` offsets `286-296`; context: The RPD also found that the features of the Applicant’s RIC were inconsistent with the features of genuine RICs without explaining the inconsistencies.
- Evidence: `reasoning_application` cue `conclude` at chunk `5199375` offsets `573-581`; context: Contrary to the RPD’s finding, the Applicant says that his RIC is actually consistent with other genuine RICs so the RPD had no reasonable basis to conclude that his RIC is fraudulent.
- Evidence: `evidence_fact` cue `found that` at chunk `5199376` offsets `13-23`; context: [26] The RPD found that the Applicant had established his identity, but he says that its finding that the RIC is fraudulent tainted its assessment of the rest of his claim.
- Evidence: `reasoning_application` cue `because` at chunk `5199376` offsets `241-248`; context: The RPD found that his Hukou and Divorce Certificate are fraudulent because they contain the same identity number as appeared in the RIC.
- Evidence: `counterargument_limitation` cue `but` at chunk `5199376` offsets `68-71`; context: [26] The RPD found that the Applicant had established his identity, but he says that its finding that the RIC is fraudulent tainted its assessment of the rest of his claim.
- Evidence: `evidence_fact` cue `found that` at chunk `5199377` offsets `79-89`; context: [27] In addition to rejecting his RIC, Hukou, and Divorce Certificate, the RPD found that the Notice was not an authentic document.
- Evidence: `reasoning_application` cue `because` at chunk `5199377` offsets `320-327`; context: This finding was unreasonable because the examples in RIR CHN42444.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5199377` offsets `132-140`; context: Although the RPD accepted that the Notice refers to article 92 of the Criminal Procedural Law, not the Criminal law, it found that the Notice was fraudulent.
- Evidence: `reasoning_application` cue `because` at chunk `5199378` offsets `38-45`; context: [28] The RPD also rejected the Notice because the section of the criminal law listed in it was different from that in the example in RIR CHN42444.
- Evidence: `reasoning_application` cue `Because` at chunk `5199379` offsets `5-12`; context: [29] Because the RPD’s finding that the Applicant’s documentation was fraudulent was unreasonable, and this impugned the Applicant’s credibility, the Decision must be returned for reconsideration.
- Evidence: `evidence_fact` cue `found that` at chunk `5199380` offsets `17-27`; context: [30] Although it found that the Applicant knows about Falun Gong and provided photographs of him participating in Falun Gong activities, the RPD found that he is not a genuine practitioner.
- Evidence: `reasoning_application` cue `because` at chunk `5199381` offsets `258-265`; context: He has met this low standard because he said that his practice of Falun Gong involved learning the exercises of Falun Gong, describing the benefits of involvement in Falun Gong, and showing how his life had improved since he started practising Falun Gong.
- Evidence: `governing_rule` cue `principles` at chunk `5199383` offsets `453-463`; context: [33] The RPD said in the Decision that
Even taking into consideration his limited formal education and his allegedly recent practice of Falun Gong, the determination he was not a Falun Gong practitioner in China and the authorities are not interested him, together with the determination that the claimant has provided fraudulent documentation to embellish his claim, leads the panel to determine that the claimant does not abide by the central guiding principles of Falun Gong, which are Truthfulness, Compassion, and Forbearance.

#### 25476:3:subtheme:3 · paragraphs 34-38

- Raw key terms: `applicant, fraudulent, reasonable, respondent, credibility, documents, findings, genuine`
- Display key terms: `fraudulent, reasonable, credibility, documents, findings, genuine`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: fraudulent, reasonable, credibility, documents, findings, genuine Position/evidence statements: The RIC he submitted was not consistent with genuine RICs; b. Application context: The Bai Sha Prison visiting card was suspect because the other documents the Applicant submitted were fraudulent. | It was therefore reasonable for the RPD to reject the Notice on this basis. Evidence spans paragraphs 34-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5199384` offsets `43-50`; context: [34] This shows that the RPD’s analysis of whether or not the Applicant is a genuine Falun Gong practitioner was tainted by its unreasonable finding that his RIC is fraudulent.
- Evidence: `party_position` cue `submitted` at chunk `5199385` offsets `169-178`; context: The RIC he submitted was not consistent with genuine RICs;
b.
- Evidence: `evidence_fact` cue `testimony` at chunk `5199385` offsets `301-310`; context: The Applicant did not adequately address the inconclusive Forensic Report in his testimony;
c.
- Evidence: `reasoning_application` cue `because` at chunk `5199385` offsets `613-620`; context: The Bai Sha Prison visiting card was suspect because the other documents the Applicant submitted were fraudulent.
- Evidence: `evidence_fact` cue `evidence` at chunk `5199386` offsets `85-93`; context: [36] The Respondent notes that the RPD is entitled to prefer and rely on documentary evidence over a claimant’s testimony, even if it finds that a claimant is credible and trustworthy.
- Evidence: `evidence_fact` cue `found that` at chunk `5199387` offsets `18-28`; context: [37] When the RPD found that the Hukou and the Divorce Certificate were fraudulent, the RPD acted reasonably.
- Evidence: `reasoning_application` cue `therefore` at chunk `5199388` offsets `443-452`; context: It was therefore reasonable for the RPD to reject the Notice on this basis.

#### 25476:3:subtheme:4 · paragraphs 39-44

- Raw key terms: `applicant, decision, falun, genuine, gong, analysis, beliefs, documents`
- Display key terms: `falun, genuine, gong, analysis, beliefs, documents`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: falun, genuine, gong, analysis, beliefs, documents Position/evidence statements: The RPD looked at his limited education and his practice of Falun Gong; it also considered its determination that authorities in the PRC were not looking for him and the fact that he had submitted fraudulent documentatio Application context: Based on all of these factors, it was not unreasonable for the RPD to conclude that he did not abide by the tenets of Falun Gong and to reject his explanation of why he did not know much about Falun Gong. | The Forensic Report found that the authenticity of the RIC was “inconclusive” but the RPD rejected the RIC as genuine because: a. Evidence spans paragraphs 39-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5199389` offsets `5-12`; context: [39] Whether or not the RPD’s credibility finding was reasonable, its finding that the Applicant is not a genuine Falun Gong practitioner was fatal to his claim.
- Evidence: `party_position` cue `submitted` at chunk `5199390` offsets `673-682`; context: The RPD looked at his limited education and his practice of Falun Gong; it also considered its determination that authorities in the PRC were not looking for him and the fact that he had submitted fraudulent documentation.
- Evidence: `evidence_fact` cue `found that` at chunk `5199390` offsets `13-23`; context: [40] The RPD found that the Applicant had some knowledge of Falun Gong but also found that he did not abide by the central philosophies of Falun Gong.
- Evidence: `reasoning_application` cue `conclude` at chunk `5199390` offsets `779-787`; context: Based on all of these factors, it was not unreasonable for the RPD to conclude that he did not abide by the tenets of Falun Gong and to reject his explanation of why he did not know much about Falun Gong.
- Evidence: `counterargument_limitation` cue `but` at chunk `5199390` offsets `71-74`; context: [40] The RPD found that the Applicant had some knowledge of Falun Gong but also found that he did not abide by the central philosophies of Falun Gong.
- Evidence: `evidence_fact` cue `record` at chunk `5199391` offsets `218-224`; context: In this case, the RPD’s findings had a basis in the record and are within the Dunsmuir range of possible, acceptable outcomes.
- Evidence: `evidence_fact` cue `evidence` at chunk `5199393` offsets `94-102`; context: [43] The RPD’s findings regarding the RIC permeate the whole Decision and other documents and evidence the Applicant provided were not reasonably assessed.
- Evidence: `reasoning_application` cue `because` at chunk `5199393` offsets `274-281`; context: The Forensic Report found that the authenticity of the RIC was “inconclusive” but the RPD rejected the RIC as genuine because:
a.
- Evidence: `counterargument_limitation` cue `but` at chunk `5199393` offsets `234-237`; context: The Forensic Report found that the authenticity of the RIC was “inconclusive” but the RPD rejected the RIC as genuine because:
a.

#### 25476:3:subtheme:5 · paragraphs 45-55

- Raw key terms: `applicant, finding, authenticity, basis, documents, notice, authentic, chinese`
- Display key terms: `finding, authenticity, basis, documents, notice, authentic, chinese`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: finding, authenticity, basis, documents, notice, authentic, chinese Position/evidence statements: Why she would have provided such information at a time when she claims not to have known the card was fraudulent does not appear to have been considered. | [51] As the Applicant points out, the RPD then went on to reject nearly all of the other documents he submitted to support his claim. Application context: As noted, the board rejected all of the tendered documents on the basis that the RIC was fraudulent and because of the prevalence of fabricated Chinese documentation. | The reasoning is, basically, “because the RIC is not authentic the other documents are inauthentic. Evidence spans paragraphs 45-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5199395` offsets `304-312`; context: The RPD then relies on these unexplained inconsistencies without question.
- Evidence: `evidence_fact` cue `testimony` at chunk `5199395` offsets `86-95`; context: The RPD declined to accept the Applicant’s testimony by relying upon a Forensic Report which says that authenticity is “inconclusive,” and also refers to inconsistencies that are never explained.
- Evidence: `evidence_fact` cue `evidence` at chunk `5199396` offsets `59-67`; context: [46] In any event, the Forensic Report itself is obviously evidence that, whatever the inconsistencies were, they were not sufficient to show that the RIC was inauthentic.
- Evidence: `party_position` cue `claims` at chunk `5199398` offsets `975-981`; context: Why she would have provided such information at a time when she claims not to have known the card was fraudulent does not appear to have been considered.
- Evidence: `reasoning_application` cue `because` at chunk `5199398` offsets `467-474`; context: As noted, the board rejected all of the tendered documents on the basis that the RIC was fraudulent and because of the prevalence of fabricated Chinese documentation.
- Evidence: `reasoning_application` cue `because` at chunk `5199400` offsets `267-274`; context: The reasoning is, basically, “because the RIC is not authentic the other documents are inauthentic.
- Evidence: `party_position` cue `submitted` at chunk `5199401` offsets `102-111`; context: [51] As the Applicant points out, the RPD then went on to reject nearly all of the other documents he submitted to support his claim.
- Evidence: `evidence_fact` cue `determined that` at chunk `5199401` offsets `1011-1026`; context: The RPD compared the Notice to these examples and determined that it was significantly different in appearance.
- Evidence: `counterargument_limitation` cue `However` at chunk `5199401` offsets `739-746`; context: However, the RPD nevertheless impugned the authenticity of the document.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5199403` offsets `5-16`; context: [53] Accordingly, based on the information in the RIR, the fact that the Notice is different in certain aspects from the samples attached to the RIR is neither surprising nor suspicious.
- Evidence: `evidence_fact` cue `found that` at chunk `5199404` offsets `18-28`; context: [54] The RPD also found that the Notice was not genuine because the article from China’s Criminal Procedure Law referenced in it is different from the one referenced in the sample Notice of Summons in the RIR CHN42444.
- Evidence: `reasoning_application` cue `because` at chunk `5199404` offsets `56-63`; context: [54] The RPD also found that the Notice was not genuine because the article from China’s Criminal Procedure Law referenced in it is different from the one referenced in the sample Notice of Summons in the RIR CHN42444.
- Evidence: `counterargument_limitation` cue `However` at chunk `5199404` offsets `221-228`; context: However, both the Applicant’s Notice and the sample Notice of Summons referenced the same article.
- Evidence: `party_position` cue `submitted` at chunk `5199405` offsets `337-346`; context: The RPD uses the same reasoning to reject the authenticity of the Visiting Card the Applicant submitted as evidence that one of his fellow practitioners was arrested.
- Evidence: `evidence_fact` cue `evidence` at chunk `5199405` offsets `350-358`; context: The RPD uses the same reasoning to reject the authenticity of the Visiting Card the Applicant submitted as evidence that one of his fellow practitioners was arrested.

#### 25476:3:subtheme:6 · paragraphs 56-60

- Raw key terms: `knowledge, applicant, falun, gong, abide, assessment, based, better`
- Display key terms: `knowledge, falun, gong, abide, assessment, based, better`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: knowledge, falun, gong, abide, assessment, based, better Rule/authority context: Even after taking into consideration his limited formal education and his allegedly recent practice of Falun Gong, the determination that he was not a Falun Gong practitioner in China and that the authorities are not int | [59] It is significant to note on this point that this Court’s jurisprudence imposes a very low standard on refugee claimants to demonstrate religious knowledge as a requirement for proving religious identity. Application context: [57] The RPD appears to say that the Applicant does not abide by the central guiding principle of “Truthfulness” because he has “provided fraudulent documentation to embellish his claim. Evidence spans paragraphs 56-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5199406` offsets `814-824`; context: Even after taking into consideration his limited formal education and his allegedly recent practice of Falun Gong, the determination that he was not a Falun Gong practitioner in China and that the authorities are not interested in him, together with the determination that the claimant has provided fraudulent documentation to embellish his claim, leads the panel to determine that the claimant does not abide by the central guiding principles of Falun Gong, which are Truthfulness, Compassion and Forbearance.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5199406` offsets `145-153`; context: [56] The RPD also buttressed its finding that the Applicant is not a genuine Falun Gong practitioner with its findings on inauthentic documents:
Although the claimant has some knowledge of Falun Gong and has provided pictures of participating in Falun Gong activities, the panel determines, based on a balance probabilities [sic], that he is not a genuine Falun Gong practitioner.
- Evidence: `reasoning_application` cue `because` at chunk `5199407` offsets `113-120`; context: [57] The RPD appears to say that the Applicant does not abide by the central guiding principle of “Truthfulness” because he has “provided fraudulent documentation to embellish his claim.
- Evidence: `evidence_fact` cue `testimony` at chunk `5199408` offsets `38-47`; context: [58] As the Applicant points out, his testimony ultimately did not persuade the RPD that he knew enough about Falun Gong.
- Evidence: `counterargument_limitation` cue `However` at chunk `5199408` offsets `122-129`; context: However, as the RPD itself acknowledged, the Applicant had only three years of formal education and his practice of Falun Gong is relatively recent.
- Evidence: `evidence_fact` cue `determined that` at chunk `5199409` offsets `287-302`; context: In Chen, above, for example, the Court set aside the RPD’s decision where it determined that the claimant was not a genuine Christian based in part on the its finding of inadequate religious knowledge.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5199409` offsets `63-76`; context: [59] It is significant to note on this point that this Court’s jurisprudence imposes a very low standard on refugee claimants to demonstrate religious knowledge as a requirement for proving religious identity.

#### 25476:3:subtheme:7 · paragraphs 61-63

- Raw key terms: `above, against, applicant, based, canada, circumstances, claimant, decision`
- Display key terms: `above, against, based, circumstances`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: above, against, based, circumstances Evidence spans paragraphs 61-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5199411` offsets `566-572`; context: From the transcript of the hearing, it is clear that his few points of error on doctrinal issues are vastly outweighed by his knowledge of the Christian faith.
- Evidence: `evidence_fact` cue `determined that` at chunk `5199411` offsets `56-71`; context: [60] Similarly, in Huang, above, Justice Richard Mosley determined that the RPD acted unreasonably when it concluded that the claimant was not a Christian based on insufficient knowledge of Christianity.
- Evidence: `issue` cue `issue` at chunk `5199412` offsets `313-318`; context: It erroneously weighed his testimony on this issue against its own misguided idea of what a person in the Applicant’s circumstances should or would know or understand.
- Evidence: `evidence_fact` cue `testimony` at chunk `5199412` offsets `295-304`; context: It erroneously weighed his testimony on this issue against its own misguided idea of what a person in the Applicant’s circumstances should or would know or understand.

#### 25476:3:subtheme:8 · paragraphs 64-64

- Raw key terms: `agree, certification, concurs, counsel, court, question`
- Display key terms: `agree, certification, concurs, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, certification, concurs, question Evidence spans paragraphs 64-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5199414` offsets `31-39`; context: [63] Counsel agree there is no question for certification and the Court concurs.

#### Section text

[20] The Applicant raises the following issues in this application:
a. Whether the RPD’s conclusion that his documents were fraudulent was reasonable;
b. Whether the RPD’s conclusion that he was not a genuine Falun Gong practitioner was reasonable.
STANDARD OF REVIEW

[21] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9, held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[22] Both issues the Applicant has raised in this case challenge the RPD’s findings of fact. It is well established that findings of fact are to be examined on a standard of review of reasonableness. (See Dunsmuir, above, at paragraph 51, Mugesera v Canada (Minister of Citizenship and Immigration) 2005 SCC 40 at paragraph 38, and Williams v Canada (Minister of Citizenship and Immigration) 2005 FCA 126 at paragraph 17). The standard of review on both issues in this case is reasonableness.

[23] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at paragraph 47, and Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at paragraph 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”
ARGUMENTS
The Applicant
The RPD Unreasonably Found the Applicant’s Documents were Fraudulent

[24] The Applicant says that the RPD does not have any expertise in evaluating foreign documents. He says that Rasheed v Canada (Minister of Citizenship and Immigration) 2004 FC 587 establishes that documents should be presumed valid unless there is evidence to suggest they are not. A finding that one identity document is fraudulent is not enough to establish that all of the documents a claimant submits are untrustworthy.

[25] In this case, the RPD based its finding that his documents are fraudulent on a finding that the Applicant’s RIC is fraudulent. When it found the RIC was fraudulent, the RPD went beyond the Forensic Report’s statement that the authenticity of his RIC was inconclusive. The RPD also found that the features of the Applicant’s RIC were inconsistent with the features of genuine RICs without explaining the inconsistencies. Contrary to the RPD’s finding, the Applicant says that his RIC is actually consistent with other genuine RICs so the RPD had no reasonable basis to conclude that his RIC is fraudulent.

[26] The RPD found that the Applicant had established his identity, but he says that its finding that the RIC is fraudulent tainted its assessment of the rest of his claim. The RPD found that his Hukou and Divorce Certificate are fraudulent because they contain the same identity number as appeared in the RIC. The unreasonable finding on the RIC was key to the RPD’s findings on the Hukou and Divorce Certificate. This means that these findings are also unreasonable.

[27] In addition to rejecting his RIC, Hukou, and Divorce Certificate, the RPD found that the Notice was not an authentic document. Although the RPD accepted that the Notice refers to article 92 of the Criminal Procedural Law, not the Criminal law, it found that the Notice was fraudulent. This finding was unreasonable because the examples in RIR CHN42444.E, which the RPD relied upon, are outdated. The examples in the RIR are from 2004 and do not show what a summons issued in 2009, like his, would look like. Further, the RIR does not say that the examples it contains are the only form of summons in the PRC or that summonses are the same all over the PRC. Rather, RIR CHN42444.E says that “there can be substantial regional variances in law enforcement, in which some differences are written into polices, but ‘in most instances rule of the book gives way to norms in the street.’” The RPD unreasonably rejected the Notice based on a misguided interpretation of RIR CHN42444.E.

[28] The RPD also rejected the Notice because the section of the criminal law listed in it was different from that in the example in RIR CHN42444.E. The Applicant says that the article referenced in the Notice and in the example is actually the same, so it was unreasonable for the RPD to reject the Notice on this basis. The RPD also acted unreasonably when it rejected the Notice and the Visiting Card based on its finding that the Applicant’s other documents were fraudulent.

[29] Because the RPD’s finding that the Applicant’s documentation was fraudulent was unreasonable, and this impugned the Applicant’s credibility, the Decision must be returned for reconsideration.
The RPD’s finding the Applicant is not a genuine Falun Gong Practitioner was Unreasonable

[30] Although it found that the Applicant knows about Falun Gong and provided photographs of him participating in Falun Gong activities, the RPD found that he is not a genuine practitioner. He says that, given his limited formal education and recent introduction to Falun Gong practice, this finding was unreasonable.

[31] The Applicant says Chen v Canada (Minister of Citizenship and Immigration) 2007 FC 270 establishes that there is a very low standard on refugee claimants to demonstrate religious knowledge to prove their religious identity. He has met this low standard because he said that his practice of Falun Gong involved learning the exercises of Falun Gong, describing the benefits of involvement in Falun Gong, and showing how his life had improved since he started practising Falun Gong.

[32] The Applicant also points to Huang v Canada (Minister of Citizenship and Immigration) 2008 FC 346 which cautions against examining claimants religious knowledge microscopically. In the instant case, the RPD similarly engaged in an inappropriately microscopic examination of the Applicant’s beliefs. Rather than looking at the genuineness of his beliefs, the RPD compared his knowledge against its own standard of what a person in the same circumstances should believe. This approach was unreasonable, so the Decision must be returned for reconsideration.

[33] The RPD said in the Decision that
Even taking into consideration his limited formal education and his allegedly recent practice of Falun Gong, the determination he was not a Falun Gong practitioner in China and the authorities are not interested him, together with the determination that the claimant has provided fraudulent documentation to embellish his claim, leads the panel to determine that the claimant does not abide by the central guiding principles of Falun Gong, which are Truthfulness, Compassion, and Forbearance.

[34] This shows that the RPD’s analysis of whether or not the Applicant is a genuine Falun Gong practitioner was tainted by its unreasonable finding that his RIC is fraudulent. The entire Decision is unreasonable.
The Respondent
The RPD’s Credibility Findings Were Reasonable

[35] The Respondent says that the RPD identified several credibility concerns which rebutted the presumption that the Applicant’s documents were truthful:
a. The RIC he submitted was not consistent with genuine RICs;
b. The Applicant did not adequately address the inconclusive Forensic Report in his testimony;
c. The Applicant’s Hukou and Divorce Certificate contained the same national identity number as the fraudulent RIC;
d. The Out-patient Record contained limited information on his citizenship;
e. The Notice was different from examples in RIR CHN42444.E;
f. The Bai Sha Prison visiting card was suspect because the other documents the Applicant submitted were fraudulent.

[36] The Respondent notes that the RPD is entitled to prefer and rely on documentary evidence over a claimant’s testimony, even if it finds that a claimant is credible and trustworthy. In this case, the RPD had concerns about the Applicant’s credibility, so it reasonably preferred the documentary evidence over his testimony. It was reasonable for the RPD to find that the Applicant was not credible based on its findings that his identity documents, the Notice, and the Visiting Card were fraudulent.

[37] When the RPD found that the Hukou and the Divorce Certificate were fraudulent, the RPD acted reasonably. These documents contained the same national identity number as did the fraudulent RIC, so their authenticity stood or fell with that document. In addition to the fraudulent RIC, the RPD found that, based on documentary evidence which showed that fraudulent documents are easy to obtain in the PRC, the Hukou and Divorce Certificate were fraudulent. The RPD’s finding that the RIC is fraudulent was reasonable, so the other findings which flow from it were also reasonable.

[38] Although the Applicant has challenged the RPD’s reliance on RIR CHN42444.E in examining the Notice, the Respondent points out that this was the most up-to-date information available to the RPD. The RPD’s reliance on this document was reasonable. Though there may be regional variation in the form of notices of summoning, the Applicant has not shown that the standards disclosed in RIR CHN42444.E were not practised in his region. It was therefore reasonable for the RPD to reject the Notice on this basis.
The Applicant is not a Genuine Falun Gong Practitioner

[39] Whether or not the RPD’s credibility finding was reasonable, its finding that the Applicant is not a genuine Falun Gong practitioner was fatal to his claim. In addition to its concerns about the Applicant’s documents, the RPD also had concerns about the genuineness of his Falun Gong beliefs. Even though he testified that he practised Falun Gong regularly, he was unable to provide details about Zhuan Falun. He also gave vague answers about what he had learned in classes in Canada, and he had difficulty explaining the purposes of the exercises.

[40] The RPD found that the Applicant had some knowledge of Falun Gong but also found that he did not abide by the central philosophies of Falun Gong. The transcript indicates that he was unable to explain the purposes of the second, third, fourth, and fifth exercises. The Applicant has said that the RPD’s analysis of his Falun Gong beliefs was unreasonably microscopic, but the RPD actually considered the Applicant’s particular circumstances and the documentary evidence before it. The RPD looked at his limited education and his practice of Falun Gong; it also considered its determination that authorities in the PRC were not looking for him and the fact that he had submitted fraudulent documentation. Based on all of these factors, it was not unreasonable for the RPD to conclude that he did not abide by the tenets of Falun Gong and to reject his explanation of why he did not know much about Falun Gong.

[41] A finding that the Applicant is not a genuine Falun Gong practitioner is a finding of fact within the RPD’s specialized knowledge and should be given deference. In this case, the RPD’s findings had a basis in the record and are within the Dunsmuir range of possible, acceptable outcomes. The Court should not substitute its decision for the RPD’s even if it would have arrived at a different conclusion.
ANALYSIS

[42] For the most part, I agree with the Applicant’s assessment of the reviewable errors that arise from this Decision.

[43] The RPD’s findings regarding the RIC permeate the whole Decision and other documents and evidence the Applicant provided were not reasonably assessed. The Forensic Report found that the authenticity of the RIC was “inconclusive” but the RPD rejected the RIC as genuine because:
a. “In the remarks section [of the Forensic Report], it is noted that the examined People’s Republic of China national identification card was printed by inkjet, which is not known as being used to print genuine PRC national identity cards”; and
b. “Further, the features of the card are inconsistent with the information available on genuine Chinese national identification cards.”

[44] The RPD then says that it “gives more weight to the laboratory report since it comes from sources who are experts in the field of counterfeiting.”

[45] This conclusion makes no sense to me. The RPD declined to accept the Applicant’s testimony by relying upon a Forensic Report which says that authenticity is “inconclusive,” and also refers to inconsistencies that are never explained. The RPD then relies on these unexplained inconsistencies without question. The Respondent has not pointed to any such inconsistencies, and there is nothing before me to show how the Applicant’s RIC was inconsistent in any material way with the description contained in the RPD’s own documentation. It is difficult to see how the Applicant could address “inconsistencies” when the RPD itself did not know what they were and so could not put them to him.

[46] In any event, the Forensic Report itself is obviously evidence that, whatever the inconsistencies were, they were not sufficient to show that the RIC was inauthentic. The Forensic Report even appears to contradict itself: it says that there are no genuine specimens with which to compare the Applicant’s RIC, but also says that “the features of this card are inconsistent with the information available on genuine Chinese National Identification Cards.” Although the Forensic Report may have been authored by experts in counterfeiting, I do not see how these experts could say that the RIC was inconsistent with information available when, by their own admission, they had no genuine samples.

[47] In this context, the RPD’s finding that the RIC was inauthentic has no reasonable basis to support it. Yet this finding is then used to find the Applicant’s other documents inauthentic which, in turn, are then used to bolster a finding that the Applicant is not a genuine Falun Gong practitioner.

[48] Justice Layden-Stevenson has the following to say on point in Lin v Canada (Minister of Citizenship and Immigration) 2006 FC 84 at paragraph 12:
The fact that the first RIC was found to be fraudulent does not necessarily mean that the second RIC, the child's birth certificate, the school certificate and the household registration card are also fraudulent. As noted, the board rejected all of the tendered documents on the basis that the RIC was fraudulent and because of the prevalence of fabricated Chinese documentation. No effort was made to ascertain the authenticity of the other documents. Ms. Lin maintained that they were authentic and that she did not know that the RIC was not genuine. She had no explanation other than the card had been in the possession of the snakehead until he was paid. The board was not satisfied with that explanation because she had not provided it earlier in her PIF. Why she would have provided such information at a time when she claims not to have known the card was fraudulent does not appear to have been considered. The PIF does state that the RIC was in China.

[49] It is also unreasonable that, having concluded that the Applicant is indeed a citizen of the PRC, the RPD does not take that factor into account when assessing the authenticity of the Applicant’s documentation. Why would an authentic citizen not have an authentic RIC?

[50] The RPD’s unreasonable finding regarding the RIC then unreasonably taints its assessment of the balance of the Applicant’s claim. The RPD rejects his other identity documents on the basis of its unreasonable findings about his RIC. The reasoning is, basically, “because the RIC is not authentic the other documents are inauthentic.” Hence, if the original finding was unreasonable, as I believe it was, then the subsequent findings about the Applicant’s identity documents are equally unreasonable.

[51] As the Applicant points out, the RPD then went on to reject nearly all of the other documents he submitted to support his claim. The RPD began by finding that the Notice is fraudulent. The Applicant submitted the Notice along with its English translation. At the hearing, it was determined, through consultation with the assigned RPD-certified interpreter, that the English translation of the Notice the Applicant supplied contains an error. The English translation refers to Article 92(1) of the Criminal Law of the PRC, which is not the statute actually referenced in the Applicant’s original Notice. The RPD accepted that the Notice actually refers to the Criminal Procedure Law and that the English translation contains an error. However, the RPD nevertheless impugned the authenticity of the document. In this regard, the RPD referred to documentation from its own National Documentation Package which provides examples of Chinese Notices of Summons. The RPD compared the Notice to these examples and determined that it was significantly different in appearance.

[52] I accept the Applicant’s argument that this finding was entirely unreasonable. RIR CHN42444.E, which the RPD relied upon, dated from June 2004. It is highly unlikely that this document could be a reliable authority as to what a Notice issued in 2009 would look like. In any event, RIR CHN42444.E specifies that the example summonses are “samples.” The document does not say that these are the only forms of summonses issued by Chinese authorities; nor does it say that the style and content of summonses is uniform throughout China. On the contrary, as the Applicant points out, the document shows that procedural laws are not uniformly implemented in the PRC. In particular,
[…]while procedural laws in China are expected to be uniformly implemented and concerted efforts have been made by the Minister of Public Security to improve policing standards, in practice, the “PSP [Public Security Bureau] has yet to arrive as a rule of law institution.” According to the associate professor, there can be substantial regional variances in law enforcement, in which some differences are written into policies, but “in most instances rule of the book gives way to norms in the street.”

[53] Accordingly, based on the information in the RIR, the fact that the Notice is different in certain aspects from the samples attached to the RIR is neither surprising nor suspicious. I agree with the Applicant that the RPD erred by rejecting his Notice on the basis of an overly strict and ultimately misguided interpretation of an outdated document.

[54] The RPD also found that the Notice was not genuine because the article from China’s Criminal Procedure Law referenced in it is different from the one referenced in the sample Notice of Summons in the RIR CHN42444.E. However, both the Applicant’s Notice and the sample Notice of Summons referenced the same article. As the RPD stated, the sample Notice of Summons refers to “Article 92.” The Applicant’s Notice also refers to Article 92. Accordingly, in my view, the RPD’s finding here is clearly erroneous.

[55] It is also significant to note with respect to the Notice that the RPD again relies on its “previous determinations with respect to other identity documents as not being authentic” as a basis for rejecting the authenticity of the Notice. The RPD uses the same reasoning to reject the authenticity of the Visiting Card the Applicant submitted as evidence that one of his fellow practitioners was arrested. Again, it is clear the RPD’s initial unreasonable finding with respect to the Applicant’s RIC tainted its entire analysis of his claim.

[56] The RPD also buttressed its finding that the Applicant is not a genuine Falun G

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 25476:4 · paragraphs 65-66

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f8ecbf12e536c7c7e2536a0d6b4314849e26034c2eb1a0fc330445f669a3288a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25476:4:subtheme:1 · paragraphs 65-66

- Raw key terms: `allowed, applicant, application, cause, certification, citizenship, constituted, counsel`
- Display key terms: `allowed, certification, constituted`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allowed, certification, constituted No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 65-66. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application is allowed. The decision is quashed and the matter is returned for reconsideration by a differently constituted RPD.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-4836-11

STYLE OF CAUSE: LIEN LIN
Applicant
- and -
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: January 31, 2012
REASONS FOR 

## 25476:5 · paragraphs 67-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `854de6ab9cc004a7434644001a78530c0d936edd8e097685268c320f9e793ce1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25476:5:subtheme:1 · paragraphs 67-67

- Raw key terms: `appearances, applicant, attorney, barristers, canada, dated, deputy, elyse`
- Display key terms: `barristers, dated, deputy, elyse`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, dated, deputy, elyse No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 67-67. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: HON. MR. JUSTICE RUSSELL
DATED: March 5, 2012
APPEARANCES:
Elyse Korman APPLICANT
Meva Motwani RESPONDENT
SOLICITORS OF RECORD:
OTIS & KORMAN APPLICANT
Barristers & Solicitors
Toronto, Ontario
Myles J. Kirvan RESPONDENT
Deputy Attorney General of Canada
