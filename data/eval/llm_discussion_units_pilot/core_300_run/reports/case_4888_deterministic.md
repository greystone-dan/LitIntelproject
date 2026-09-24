# Discussion Units: case 4888

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **33**
- Continuity pairs: **32**
- Discussion Units: **2**
- Paragraph source hashes: **33**
- Sub-themes: **9**

## 4888:1 · paragraphs 0-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5fb271df68891bc4f3baba4dee9078483da2efbe9264c1a8e0b6112d437e0171`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4888:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, secret, service, canada, days, decision, report, syrian`
- Display key terms: `secret, service, days, report, syrian`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: secret, service, days, report, syrian Rule/authority context: In a decision on April 21, 2004, the Board determined that the applicant was not a Convention refugee or person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act (IRPA). | Being under constant surveillance by the secret service, he then decided to apply for a visitor's visa for Canada and take advantage of the World Youth Days in Toronto with Pope John Paul II for the trip. Application context: He then applied for a year's unpaid leave, which he was granted. | He applied for refugee status in May 2003. Operative outcome context: He then applied for a year's unpaid leave, which he was granted. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4272732` offsets `189-204`; context: In a decision on April 21, 2004, the Board determined that the applicant was not a Convention refugee or person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act (IRPA).
- Evidence: `governing_rule` cue `under` at chunk `4272732` offsets `280-285`; context: In a decision on April 21, 2004, the Board determined that the applicant was not a Convention refugee or person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act (IRPA).
- Evidence: `evidence_fact` cue `evidence` at chunk `4272735` offsets `191-199`; context: He was also detained for a period of 48 to 72 hours (the evidence is not clear on this point), during which he was beaten, and then released.
- Evidence: `governing_rule` cue `under` at chunk `4272736` offsets `182-187`; context: Being under constant surveillance by the secret service, he then decided to apply for a visitor's visa for Canada and take advantage of the World Youth Days in Toronto with Pope John Paul II for the trip.
- Evidence: `reasoning_application` cue `applied` at chunk `4272736` offsets `119-126`; context: He then applied for a year's unpaid leave, which he was granted.
- Evidence: `disposition` cue `granted` at chunk `4272736` offsets `167-174`; context: He then applied for a year's unpaid leave, which he was granted.
- Evidence: `reasoning_application` cue `applied` at chunk `4272737` offsets `200-207`; context: He applied for refugee status in May 2003.

#### 4888:1:subtheme:2 · paragraphs 7-7

- Raw key terms: `answers, applicant's, arduous, avoided, board, contradictions, credibility, established`
- Display key terms: `answers, applicant's, arduous, avoided, contradictions, credibility, established`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: answers, applicant's, arduous, avoided, contradictions, credibility, established Evidence spans paragraphs 7-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4272738` offsets `101-109`; context: [7] At the outset, the Board noted that the applicant's identity had been established and was not in question.
- Evidence: `evidence_fact` cue `testimony` at chunk `4272738` offsets `138-147`; context: However, it noted that his testimony was "very arduous", questions had to be repeated several times, his answers were evasive and he repeatedly avoided the issue.
- Evidence: `counterargument_limitation` cue `However` at chunk `4272738` offsets `111-118`; context: However, it noted that his testimony was "very arduous", questions had to be repeated several times, his answers were evasive and he repeatedly avoided the issue.

#### 4888:1:subtheme:3 · paragraphs 8-14

- Raw key terms: `applicant, board, respondent, argued, arrest, based, board's, fear`
- Display key terms: `arrest, based, board's, fear`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: arrest, based, board's, fear Position/evidence statements: [9] First, the applicant argued that he was not properly represented before the Board. | He submitted that in finding his story to be a complete fabrication, the Board acted in a speculative and arbitrary way. Rule/authority context: Ultimately, in the Board's view, the applicant's actions did not indicate a subjective fear under section 96 of the Act and there were no substantial grounds for applying section 97. Application context: [14] Finally, the respondent contended that the applicant failed to establish a subjective fear, pointing out that he did not apply for refugee protection until May 2003, one month after a warrant was issued for his arre Operative outcome context: [8] The Board considered in particular the vagueness surrounding the length of his detention and circumstances of his release, the implausibility of the rejection of his resignation and the fact that it was highly unlike Evidence spans paragraphs 8-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4272739` offsets `566-571`; context: Ultimately, in the Board's view, the applicant's actions did not indicate a subjective fear under section 96 of the Act and there were no substantial grounds for applying section 97.
- Evidence: `disposition` cue `allowed` at chunk `4272739` offsets `253-260`; context: [8] The Board considered in particular the vagueness surrounding the length of his detention and circumstances of his release, the implausibility of the rejection of his resignation and the fact that it was highly unlikely the applicant would have been allowed to leave Syria without difficulty if he was in fact wanted by the secret service.
- Evidence: `party_position` cue `argued` at chunk `4272740` offsets `25-31`; context: [9] First, the applicant argued that he was not properly represented before the Board.
- Evidence: `party_position` cue `submitted` at chunk `4272741` offsets `189-198`; context: He submitted that in finding his story to be a complete fabrication, the Board acted in a speculative and arbitrary way.
- Evidence: `party_position` cue `argued` at chunk `4272742` offsets `20-26`; context: [11] The respondent argued that the applicant had not shown that his counsel was incompetent, and added that in any event, that would not explain the contradictions in his testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4272742` offsets `172-181`; context: [11] The respondent argued that the applicant had not shown that his counsel was incompetent, and added that in any event, that would not explain the contradictions in his testimony.
- Evidence: `party_position` cue `argued` at chunk `4272743` offsets `191-197`; context: [12] On the Board's assessment of the evidence, counsel for the respondent thoroughly went over all of the various contradictions and implausibilities noted by the Board, point by point, and argued that the evidence supported those findings.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272743` offsets `38-46`; context: [12] On the Board's assessment of the evidence, counsel for the respondent thoroughly went over all of the various contradictions and implausibilities noted by the Board, point by point, and argued that the evidence supported those findings.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272744` offsets `155-163`; context: [13] The respondent further maintained that the Board could not give any weight to the summons and arrest warrant in view of its finding that based on the evidence as a whole, the applicant was not credible.
- Evidence: `reasoning_application` cue `apply` at chunk `4272745` offsets `126-131`; context: [14] Finally, the respondent contended that the applicant failed to establish a subjective fear, pointing out that he did not apply for refugee protection until May 2003, one month after a warrant was issued for his arrest and nearly a year after a summons had been issued.

#### 4888:1:subtheme:4 · paragraphs 15-21

- Raw key terms: `board, applicant's, applicant, court, claimant, fact, hearing, argued`
- Display key terms: `applicant's, fact, hearing`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position Display terms: applicant's, fact, hearing Position/evidence statements: At most, as the applicant argued in his supplementary affidavit, counsel's deficiencies in preparing for the hearing and drawing up the list of exhibits might explain the Panel's impatience with him. Rule/authority context: Representation by a non-lawyer is not in itself a breach of the principles of natural justice. | [17] Additionally, on the findings of fact made by the Board regarding the applicant's credibility, it should be noted again that the applicable standard of review is that of the patently unreasonable decision. Evidence spans paragraphs 15-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `4272746` offsets `186-196`; context: Representation by a non-lawyer is not in itself a breach of the principles of natural justice.
- Evidence: `party_position` cue `argued` at chunk `4272747` offsets `185-191`; context: At most, as the applicant argued in his supplementary affidavit, counsel's deficiencies in preparing for the hearing and drawing up the list of exhibits might explain the Panel's impatience with him.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4272747` offsets `213-222`; context: At most, as the applicant argued in his supplementary affidavit, counsel's deficiencies in preparing for the hearing and drawing up the list of exhibits might explain the Panel's impatience with him.
- Evidence: `counterargument_limitation` cue `However` at chunk `4272747` offsets `359-366`; context: However, a careful reading of the transcript does not support such a finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272748` offsets `321-329`; context: As a tribunal specializing in this area, it is up to the Board to assess the credibility of the witnesses and evidence before it.
- Evidence: `governing_rule` cue `standard of review` at chunk `4272748` offsets `145-163`; context: [17] Additionally, on the findings of fact made by the Board regarding the applicant's credibility, it should be noted again that the applicable standard of review is that of the patently unreasonable decision.
- Evidence: `evidence_fact` cue `testimony` at chunk `4272749` offsets `183-192`; context: First, the Board was certainly entitled to make adverse credibility findings based on the evasive and arduous nature of the applicant's testimony (Das v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4272750` offsets `136-145`; context: [19] The Court also feels entitled to note several contradictions and implausibilities in the applicant's Personal Information Form and testimony.
- Evidence: `counterargument_limitation` cue `However` at chunk `4272750` offsets `293-300`; context: However, taken together, the Board was perfectly entitled to find as it did.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272752` offsets `657-665`; context: Notice to parties - Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
- Evidence: `governing_rule` cue `under` at chunk `4272752` offsets `202-207`; context: [21] It is true that the Board relied on its specialized knowledge of Syria in finding it unlikely that the applicant would have been able to leave the country without difficulty if he had in fact been under secret service surveillance.

#### 4888:1:subtheme:5 · paragraphs 22-23

- Raw key terms: `applicant, based, board, canada, finding, actions, adjel, administrative`
- Display key terms: `based, finding, actions, adjel, administrative`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: based, finding, actions, adjel, administrative Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4272753` offsets `301-308`; context: It is well-settled case law that the reasons of an administrative tribunal must be taken as a whole in determining whether its decision was reasonable, and analysis does not involve determining whether each point in its reasoning meets the reasonableness test (see in particular Stelco Inc.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272754` offsets `595-603`; context: A careful reading of section 96 of the IRPA indicates that the burden on refugee claimants is twofold: they must show by their conduct and actions that they really do fear persecution in their country, and that the fear is based on objective and verifiable evidence (Rajudeen v.

#### 4888:1:subtheme:6 · paragraphs 24-25

- Raw key terms: `board, credibility, accept, account, against, applicant, applicant's, application`
- Display key terms: `credibility, accept, account, against, applicant's`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: credibility, accept, account, against, applicant's Position/evidence statements: [25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating: Also, given all the evidence and the claimant's general lack of credibility, th Rule/authority context: [25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating: Also, given all the evidence and the claimant's general lack of credibility, th Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4272755` offsets `366-373`; context: These are undoubtedly factors that the Board could take into account in assessing whether he had a subjective fear (Huerta v.
- Evidence: `party_position` cue `argued` at chunk `4272756` offsets `28-34`; context: [25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating:
Also, given all the evidence and the claimant's general lack of credibility, the panel believes that there are no substantial grounds warranting the application of subsection 97(1) of the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272756` offsets `161-169`; context: [25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating:
Also, given all the evidence and the claimant's general lack of credibility, the panel believes that there are no substantial grounds warranting the application of subsection 97(1) of the Act.
- Evidence: `governing_rule` cue `under` at chunk `4272756` offsets `85-90`; context: [25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating:
Also, given all the evidence and the claimant's general lack of credibility, the panel believes that there are no substantial grounds warranting the application of subsection 97(1) of the Act.

#### 4888:1:subtheme:7 · paragraphs 26-29

- Raw key terms: `paragraph, section, applicant's, board, credibility, evidence, necessarily, persecuted`
- Display key terms: `paragraph, section, applicant's, credibility, necessarily, persecuted`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: paragraph, section, applicant's, credibility, necessarily, persecuted Rule/authority context: [26] It is well settled that an adverse credibility finding, though it may be conclusive of a refugee claim under section 96 of the Act, is not necessarily conclusive of a claim under subsection 97(1). | Accordingly, the applicant's lack of credibility could be held against him under both section 96 and paragraph 97(1)(a). Application context: Accordingly, the applicant's lack of credibility could be held against him under both section 96 and paragraph 97(1)(a). Evidence spans paragraphs 26-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4272757` offsets `408-415`; context: When considering section 97, the Board must decide whether the claimant's removal would subject him personally to the dangers and risks stipulated in paragraphs 97(1)(a) and (b) of the Act (Bouaouni v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4272757` offsets `234-242`; context: The reason for this is that the evidence necessary to establish the well-foundedness of a claim under section 97 differs from that required by section 96.
- Evidence: `governing_rule` cue `under` at chunk `4272757` offsets `108-113`; context: [26] It is well settled that an adverse credibility finding, though it may be conclusive of a refugee claim under section 96 of the Act, is not necessarily conclusive of a claim under subsection 97(1).
- Evidence: `evidence_fact` cue `evidence` at chunk `4272759` offsets `175-183`; context: The fact that the documentary evidence shows that the human rights situation in a country is problematic does not necessarily mean there is a risk to a given individual (Ahmad v.
- Evidence: `governing_rule` cue `under` at chunk `4272759` offsets `534-539`; context: Accordingly, the applicant's lack of credibility could be held against him under both section 96 and paragraph 97(1)(a).
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4272759` offsets `459-470`; context: Accordingly, the applicant's lack of credibility could be held against him under both section 96 and paragraph 97(1)(a).
- Evidence: `evidence_fact` cue `testimony` at chunk `4272760` offsets `555-564`; context: Although the Board did not expressly say so in its reasons (which, incidentally, would have been preferable), the transcripts of the applicant's testimony clearly indicate the Board's doubts on this point.
- Evidence: `counterargument_limitation` cue `however` at chunk `4272760` offsets `247-254`; context: Apparently, however, the arrest warrant was issued by the department of justice after the applicant lost some documents and failed to report for work at the end of his leave.

#### 4888:1:subtheme:8 · paragraphs 30-31

- Raw key terms: `reasons, accordingly, alaa, application, board, cause, certified, citizenship`
- Display key terms: `accordingly, alaa, certified`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: accordingly, alaa, certified Application context: [30] For all these reasons, I find that the Board made no patently unreasonable error. Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4272761` offsets `155-163`; context: No question is certified.
- Evidence: `reasoning_application` cue `I find` at chunk `4272761` offsets `28-34`; context: [30] For all these reasons, I find that the Board made no patently unreasonable error.

#### Section text

Jarada v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-03-24
Neutral citation
2005 FC 409
File numbers
IMM-4638-04
Decision Content
Date: 20050324
Docket: IMM-4638-04
Citation: 2005 FC 409
BETWEEN:
ALAA JARADA
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
de MONTIGNY J.

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board). In a decision on April 21, 2004, the Board determined that the applicant was not a Convention refugee or person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act (IRPA).

[2] The applicant is a citizen of Syria. He was an accountant working as an auditor at the Syrian department of finance.

[3] According to the applicant, in the course of his duties, he audited the books of a business owned by the son of an influential member of the Syrian secret service and discovered tax fraud. He said he informed his superior, who directed him to make a favourable report concealing the fraud. He failed to do this and, when he filed his report on January 25, 2002, his superior asked him to change it and to make no mention of the fraud. When he refused, his superior threatened him. Then, two days later, he was given a notice of transfer to the archives branch. He refused the transfer and requested ten days' vacation with the intention of reporting the matter to departmental authorities.

[4] A few days later, on February 1, 2002, the secret service allegedly came to his home, searched his house and took documents away. He was also detained for a period of 48 to 72 hours (the evidence is not clear on this point), during which he was beaten, and then released. He then went to the hospital to get treatment for his injuries and made a report at the hospital police detachment.

[5] He returned to work on February 7, 2002, and then on March 1 tendered his resignation, which was rejected. He then applied for a year's unpaid leave, which he was granted. Being under constant surveillance by the secret service, he then decided to apply for a visitor's visa for Canada and take advantage of the World Youth Days in Toronto with Pope John Paul II for the trip. He arrived in Canada on July 9, 2002.

[6] Following his arrival in Canada, he was ordered (at his residence in Syria) to report to the Syrian secret service (on July 20, 2002), and a warrant for his arrest was issued on April 3, 2003. He applied for refugee status in May 2003.
Board's decision

[7] At the outset, the Board noted that the applicant's identity had been established and was not in question. However, it noted that his testimony was "very arduous", questions had to be repeated several times, his answers were evasive and he repeatedly avoided the issue. After finding several contradictions, omissions and implausibilities in his testimony, the Board held that it could not give any credibility to his story.

[8] The Board considered in particular the vagueness surrounding the length of his detention and circumstances of his release, the implausibility of the rejection of his resignation and the fact that it was highly unlikely the applicant would have been allowed to leave Syria without difficulty if he was in fact wanted by the secret service. Finally, the Board did not believe the explanations given by the applicant to try to justify his delay in claiming refugee status. Ultimately, in the Board's view, the applicant's actions did not indicate a subjective fear under section 96 of the Act and there were no substantial grounds for applying section 97.
Applicant's arguments

[9] First, the applicant argued that he was not properly represented before the Board. Apparently, the person who acted for him before the Board, though claiming to be a lawyer, was not a member in good standing of the Barreau du Québec. The applicant claimed that he was prejudiced by his counsel's failure to explain the nature of the process for claiming refugee status in Canada, to prepare him properly for the hearing and to draw up a list of exhibits in support of his claim.

[10] Further, he maintained that the Board failed to rule on the risk of return, even when it expressed no doubt at the hearing as to the authenticity of his summons and arrest warrant. He submitted that in finding his story to be a complete fabrication, the Board acted in a speculative and arbitrary way.
Respondent's arguments

[11] The respondent argued that the applicant had not shown that his counsel was incompetent, and added that in any event, that would not explain the contradictions in his testimony. Consequently, he could not blame his counsel for the Board's finding, based on his testimony, that he lacked credibility and did not have a subjective fear.

[12] On the Board's assessment of the evidence, counsel for the respondent thoroughly went over all of the various contradictions and implausibilities noted by the Board, point by point, and argued that the evidence supported those findings. She added that the Board was entitled to find that the applicant lacked credibility, based on his evasive and arduous testimony, and was not required to tell him it had doubts about his version of events.

[13] The respondent further maintained that the Board could not give any weight to the summons and arrest warrant in view of its finding that based on the evidence as a whole, the applicant was not credible.

[14] Finally, the respondent contended that the applicant failed to establish a subjective fear, pointing out that he did not apply for refugee protection until May 2003, one month after a warrant was issued for his arrest and nearly a year after a summons had been issued. The Board was entitled to find that this delay was inconsistent with the behaviour of a person who truly feared for his life.
Analysis

[15] First, the applicant's arguments based on the alleged deficiencies of his counsel before the Board must be rejected. Representation by a non-lawyer is not in itself a breach of the principles of natural justice. As the Act expressly authorizes other counsel to act before the Board, for this Court to intervene it would have to be shown that counsel's incompetence had risen to the level of actual prejudice to the claimant (Robles v. M.C.I., [2003] F.C.J. No. 520 (F.C.); Cove v. M.C.I., [2001] F.C.J. No. 482 (F.C.); Fatima v. M.C.I., [2000] F.C.J. No. 308 (F.C.)):
167. (1) Both a person who is the subject of Board proceedings and the Minister may, at their own expense, be represented by a barrister or solicitor or other counsel.

[16] In the case at bar, the applicant failed to establish such prejudice. There is nothing to indicate to the Court that the representation was not adequate. At most, as the applicant argued in his supplementary affidavit, counsel's deficiencies in preparing for the hearing and drawing up the list of exhibits might explain the Panel's impatience with him. However, a careful reading of the transcript does not support such a finding. The Panel's impatience was actually due to the applicant's evasive answers and the fact that the questions had to be repeated several times. As to the apparent confusion around the filing of certain exhibits, there is nothing to indicate that the Board held that against him.

[17] Additionally, on the findings of fact made by the Board regarding the applicant's credibility, it should be noted again that the applicable standard of review is that of the patently unreasonable decision. As a tribunal specializing in this area, it is up to the Board to assess the credibility of the witnesses and evidence before it. This Court's intervention is warranted only if the applicant shows that the inferences drawn by the Board were patently unreasonable (Cepeda-Gutierrez v. M.C.I., [1998] F.C.J. No. 1425 (F.C.); Aguebor v. M.E.I., [1993] F.C.J. No. 732 (F.C.A.); Silvanathan v. M.C.I., [2003] F.C.J. No. 662 (F.C.)).

[18] What is the situation in the case at bar? First, the Board was certainly entitled to make adverse credibility findings based on the evasive and arduous nature of the applicant's testimony (Das v. M.C.I., [2003] F.C.J. No. 303 (F.C.); Wen v. M.E.I., [1994] F.C.J. No. 907 (F.C.A.)).

[19] The Court also feels entitled to note several contradictions and implausibilities in the applicant's Personal Information Form and testimony. Clearly, not all these contradictions and implausibilities are of equal importance, and there may even be credible explanations for some of them. However, taken together, the Board was perfectly entitled to find as it did.

[20] Contrary to what was argued by the applicant, the Board did not have to tell him during the hearing that it doubted his story. The precedents in this Court clearly establish that the burden of proof is on the claimant, and the Board is not required to disclose its assessment of the facts before it prior to making its decision (Sarker v. M.C.I., [1998] F.C.J. No. 987 (F.C.); Zheng v. M.C.I., [2000] F.C.J. No. 2002 (F.C.); Ayodele v. M.C.I., [1997] F.C.J. No. 1833 (F.C.)).

[21] It is true that the Board relied on its specialized knowledge of Syria in finding it unlikely that the applicant would have been able to leave the country without difficulty if he had in fact been under secret service surveillance. Rule 18 of the Refugee Protection Division Rules provides the following:
18. Notice to parties - Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
18. Avis aux parties - Avant d'utiliser un renseignement ou une opinion qui est du ressort de sa spécialisation, la Section en avise le demandeur d'asile ou la personne protégée et le ministre - si celui-ci est présent à l'audience - et leur donne la possibilité de :
a) faire des observations sur la fiabilité et l'utilisation du renseignement ou de l'opinion;
b) fournir des éléments de preuve à l'appui de leurs observations". La Commission ne s'étant pas conformée à cette Règle, ses conclusions sur ce point ne sauraient être retenues.

[22] That said, disregarding this provision is not critical, as the Board relied on a number of other contradictions and implausibilities in finding that the applicant was not credible. It is well-settled case law that the reasons of an administrative tribunal must be taken as a whole in determining whether its decision was reasonable, and analysis does not involve determining whether each point in its reasoning meets the reasonableness test (see in particular Stelco Inc. v. British Steel Canada Inc., [2000] 3 F.C. 282 (F.C.A.); Yassine v. M.E.I., [1994] F.C.J. No. 949 (F.C.A.)). In the case at bar, the Board based its finding on several points, and the rejection of one of them does not make its decision unreasonable.

[23] Counsel for the applicant dwelt at length on the current situation in Syria, the systematic human rights violations and the all-powerful secret service operating completely beyond the rule of law. Assuming all this to be true (and the Board made no finding on that), the applicant still had to show a subjective fear of persecution. A careful reading of section 96 of the IRPA indicates that the burden on refugee claimants is twofold: they must show by their conduct and actions that they really do fear persecution in their country, and that the fear is based on objective and verifiable evidence (Rajudeen v. M.E.I., [1984] F.C.J. No. 601 (F.C.A.); Adjel v. M.E.I., [1989] 2 F.C. 680 (F.C.A.); Yusuf v. M.E.I., [1992] 1 F.C. 629 (F.C.A.); A.G. of Canada v. Ward, [1993] 2 S.C.R. 689).

[24] The Board considered that the applicant's delay in claiming refugee status, together with the fact that he did not leave Syria until four months after his detention, even though he had had a visitor's visa since April 29, 2002, worked against him and undermined his credibility. These are undoubtedly factors that the Board could take into account in assessing whether he had a subjective fear (Huerta v. M.E.I., [1993] F.C.J. No. 271 (F.C.A.); Gamassi v. M.C.I., [2000] F.C.J. No. 1841 (F.C.)). He did attempt to explain the delay (he was still hoping things could be worked out, through friends in high places), but the Board did not accept his explanation, and the Court does not regard that as sufficient reason for intervention.

[25] Finally, the applicant argued that the Board erred in not considering his claim under section 97 of the Act separately, simply stating:
Also, given all the evidence and the claimant's general lack of credibility, the panel believes that there are no substantial grounds warranting the application of subsection 97(1) of the Act.

[26] It is well settled that an adverse credibility finding, though it may be conclusive of a refugee claim under section 96 of the Act, is not necessarily conclusive of a claim under subsection 97(1). The reason for this is that the evidence necessary to establish the well-foundedness of a claim under section 97 differs from that required by section 96. When considering section 97, the Board must decide whether the claimant's removal would subject him personally to the dangers and risks stipulated in paragraphs 97(1)(a) and (b) of the Act (Bouaouni v. M.C.I., [2003] F.C.J. No. 1540 (F.C.)).

[27] Further, there are objective and subjective components to section 96, which is not the case for paragraph 97(1)(a): a person relying on this paragraph must show on a balance of probabilities that he or she is more likely than not to be persecuted (Chan v. M.E.I., [1995] 3 S.C.R. 593; Li v. M.C.I., [2005] F.C.J. No. 1 (F.C.A.)).

[28] That said, the assessment of the applicant's potential risk of being persecuted if he were sent back to his country must be individualized. The fact that the documentary evidence shows that the human rights situation in a country is problematic does not necessarily mean there is a risk to a given individual (Ahmad v. M.C.I., [2004] F.C.J. No. 995 (F.C.); Gonulcan v. M.C.I., [2004] F.C.J. No. 486 (F.C.); Rahim v. M.C.I., [2005] F.C.J. No. 18 (F.C.)). Accordingly, the applicant's lack of credibility could be held against him under both section 96 and paragraph 97(1)(a).

[29] At the hearing, counsel for the respondent conceded that the applicant could legitimately have relied on paragraph 97(1)(a) of the Act in claiming refugee status if the arrest warrant had been issued by the Syrian secret service. Apparently, however, the arrest warrant was issued by the department of justice after the applicant lost some documents and failed to report for work at the end of his leave. Although the Board did not expressly say so in its reasons (which, incidentally, would have been preferable), the transcripts of the applicant's testimony clearly indicate the Board's doubts on this point.
Conclusion

[30] For all these reasons, I find that the Board made no patently unreasonable error. I would accordingly dismiss the application for judicial review. No question is certified.
"Yves de Montigny"
Judge
Certified true translation
Peter Douglas
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4638-04
STYLE OF CAUSE: ALAA JARADA v. MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: January 25, 2005
REASONS FOR 

## 4888:2 · paragraphs 32-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fc4d9e8a68925b7d5f04d5be0242071f382b55b9d814ff6322534f20d9e7a326`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4888:2:subtheme:1 · paragraphs 32-32

- Raw key terms: `alain, appearances, applicant, attorney, brochu, canada, dated, deputy`
- Display key terms: `alain, brochu, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alain, brochu, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 32-32. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER BY: The Honourable Mr. Justice de Montigny
DATED: March 24, 2005
APPEARANCES:
Alain Joffe FOR THE APPLICANT
Isabelle Brochu FOR THE RESPONDENT
SOLICITORS OF RECORD:
Alain Joffe FOR THE APPLICANT
Montréal, Quebec
John H. Sims, Q.C. FOR THE RESPONDENT
Deputy Attorney General of Canada
Ottawa, Ontario
