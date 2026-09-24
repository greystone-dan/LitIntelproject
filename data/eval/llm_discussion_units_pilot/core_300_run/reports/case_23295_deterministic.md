# Discussion Units: case 23295

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **24**
- Continuity pairs: **23**
- Discussion Units: **3**
- Paragraph source hashes: **24**
- Sub-themes: **8**

## 23295:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dcd5f25dff8b44c1e439dd6be28def681eab17d5535fc0312726fbffbe591881`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23295:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicants, malhotra, brother, canada, claim, decision, immigration, older`
- Display key terms: `malhotra, brother, older`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: malhotra, brother, older Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Application context: The applicants did not want to register because they were afraid that this process would enable Mr. Operative outcome context: The RAD dismissed the applicants’ appeal from a decision dated June 28, 2013, by the Refugee Protection Division [RPD], which rejected their refugee claim. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5094168` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB].
- Evidence: `disposition` cue `dismissed` at chunk `5094168` offsets `252-261`; context: The RAD dismissed the applicants’ appeal from a decision dated June 28, 2013, by the Refugee Protection Division [RPD], which rejected their refugee claim.
- Evidence: `reasoning_application` cue `because` at chunk `5094169` offsets `689-696`; context: The applicants did not want to register because they were afraid that this process would enable Mr.

#### 23295:1:subtheme:2 · paragraphs 3-9

- Raw key terms: `applicants, bangalore, decision, malhotra, another, chandigarh, evidence, brother`
- Display key terms: `bangalore, malhotra, another, chandigarh, brother`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: bangalore, malhotra, another, chandigarh, brother Position/evidence statements: A week after the hearing, but before the RPD’s decision was issued, the applicants submitted an affidavit of Mr. | [12] First, they submitted that the RPD had erred in its assessment of the IFA by not considering a number of pieces of evidence that showed that the applicants would probably be at risk even if they relocated to Mumbai  Evidence spans paragraphs 3-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5094170` offsets `711-716`; context: RPD decision [6] The RPD found that the availability of an internal flight alternative [IFA] was the determinative issue.
- Evidence: `evidence_fact` cue `found that` at chunk `5094170` offsets `621-631`; context: RPD decision [6] The RPD found that the availability of an internal flight alternative [IFA] was the determinative issue.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5094170` offsets `364-372`; context: Impugned decision [5] Although this application is directed at the RAD’s decision, to understand the criticisms levelled at that decision, it is useful to summarize the grounds the RPD relied on as the basis for dismissing the applicants’ refugee claim.
- Evidence: `party_position` cue `submitted` at chunk `5094171` offsets `338-347`; context: A week after the hearing, but before the RPD’s decision was issued, the applicants submitted an affidavit of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5094171` offsets `219-227`; context: The RPD member asked him if he had proof that they had temporarily relocated to Bangalore, and it was agreed that he would file evidence of this after the hearing.
- Evidence: `counterargument_limitation` cue `but` at chunk `5094171` offsets `281-284`; context: A week after the hearing, but before the RPD’s decision was issued, the applicants submitted an affidavit of Mr.
- Evidence: `evidence_fact` cue `found that` at chunk `5094172` offsets `93-103`; context: Moreover, it found that the applicants had not shown that there was no IFA in Bangalore.
- Evidence: `evidence_fact` cue `determined that` at chunk `5094173` offsets `19-34`; context: [9] First, the RPD determined that the applicants had not demonstrated that it would be possible for the applicants’ brother to locate them if they moved to Bangalore.
- Evidence: `counterargument_limitation` cue `but` at chunk `5094173` offsets `416-419`; context: The RPD also noted the evidence relating to the circumstances that could lead to security checks but concluded from the documentary evidence that, in the absence of a central database, the verification reports are kept in the regional police stations, which makes it very difficult, if not impossible, to locate a person unless the police take specific steps to find an individual.
- Evidence: `party_position` cue `submitted` at chunk `5094175` offsets `17-26`; context: [12] First, they submitted that the RPD had erred in its assessment of the IFA by not considering a number of pieces of evidence that showed that the applicants would probably be at risk even if they relocated to Mumbai or Bangalore.
- Evidence: `evidence_fact` cue `evidence` at chunk `5094175` offsets `120-128`; context: [12] First, they submitted that the RPD had erred in its assessment of the IFA by not considering a number of pieces of evidence that showed that the applicants would probably be at risk even if they relocated to Mumbai or Bangalore.
- Evidence: `party_position` cue `argued` at chunk `5094176` offsets `28-34`; context: [13] Second, the applicants argued that the RPD had breached its duty of procedural fairness by not considering and addressing in its decision the affidavits of Mr.

#### 23295:1:subtheme:3 · paragraphs 10-11

- Raw key terms: `availability, concluded, decision, evidence, found, address, analyzing, applicants`
- Display key terms: `availability, concluded, address, analyzing`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: availability, concluded, address, analyzing Application context: [15] The RAD found that the RPD had correctly applied the two branches of the test developed for analyzing the availability of an IFA. Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5094177` offsets `267-274`; context: Referring to the decision in Cepeda-Gutierrez v Canada, 1998 CanLII 8667 [Cepada-Gutierrez], the RAD stated that it had to determine whether the RPD had failed to consider or address in its decision important evidence that contradicted its findings and concluded that this was not the case.
- Evidence: `evidence_fact` cue `found that` at chunk `5094177` offsets `49-59`; context: [14] Applying a reasonableness standard, the RAD found that the RPD’s conclusion regarding the availability of an IFA was reasonable.
- Evidence: `evidence_fact` cue `found that` at chunk `5094178` offsets `13-23`; context: [15] The RAD found that the RPD had correctly applied the two branches of the test developed for analyzing the availability of an IFA.
- Evidence: `reasoning_application` cue `applied` at chunk `5094178` offsets `46-53`; context: [15] The RAD found that the RPD had correctly applied the two branches of the test developed for analyzing the availability of an IFA.
- Evidence: `counterargument_limitation` cue `but` at chunk `5094178` offsets `334-337`; context: Malhotra’s brother’s motive for revenge but had concluded that the applicants had not demonstrated the risk they would face if returned to India.

#### 23295:1:subtheme:4 · paragraphs 12-16

- Raw key terms: `applicants, clear, decision, evidence, found, reasonable, brother, consider`
- Display key terms: `clear, reasonable, brother, consider`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: clear, reasonable, brother, consider Position/evidence statements: Issues [17] The applicants submit that the RAD’s decision was unreasonable. Application context: The RAD considered that the statements in the affidavits added nothing because they confirmed what Mr. | Malhotra’s brother to locate the applicants because of his connections with the police. Evidence spans paragraphs 12-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5094179` offsets `554-559`; context: The RAD also found that it was clear from the RPD’s decision that it had weighed the contradictory evidence regarding mandatory registration but that this issue was not as important as the issue of the actual danger the applicants would face if returned to India.
- Evidence: `party_position` cue `submit` at chunk `5094179` offsets `695-701`; context: Issues [17] The applicants submit that the RAD’s decision was unreasonable.
- Evidence: `evidence_fact` cue `found that` at chunk `5094179` offsets `21-31`; context: [16] Second, the RAD found that the affidavits of Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5094179` offsets `261-268`; context: The RAD considered that the statements in the affidavits added nothing because they confirmed what Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5094179` offsets `540-543`; context: The RAD also found that it was clear from the RPD’s decision that it had weighed the contradictory evidence regarding mandatory registration but that this issue was not as important as the issue of the actual danger the applicants would face if returned to India.
- Evidence: `evidence_fact` cue `evidence` at chunk `5094181` offsets `210-218`; context: However, it is clear that the RAD understood that the applicants were arguing that the RPD had not dealt with this evidence (see para 10 of the RAD’s decision) but that it found, in light of Cepada-Gutierrez, that this evidence was not important enough to justify its intervention.
- Evidence: `counterargument_limitation` cue `However` at chunk `5094181` offsets `95-102`; context: However, it is clear that the RAD understood that the applicants were arguing that the RPD had not dealt with this evidence (see para 10 of the RAD’s decision) but that it found, in light of Cepada-Gutierrez, that this evidence was not important enough to justify its intervention.
- Evidence: `evidence_fact` cue `found that` at chunk `5094182` offsets `20-30`; context: [21] First, the RAD found that the RPD had considered the evidence that could explain the desire for revenge on the part of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5094183` offsets `25-33`; context: [22] The other pieces of evidence that were not mentioned in the RPD’s decision all relate to the registration and verification process in a city like Bangalore and to the ability of Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5094183` offsets `231-238`; context: Malhotra’s brother to locate the applicants because of his connections with the police.
- Evidence: `counterargument_limitation` cue `but` at chunk `5094183` offsets `649-652`; context: It is clear from the RPD’s decision that it had emotionally reviewed the contradictory evidence in this regard but had concluded that, in the absence of central police databases, it was very difficult to find a person following a security check unless there was a match between that person and the information held by the regional police.

#### 23295:1:subtheme:5 · paragraphs 17-18

- Raw key terms: `addressed, applicants, bangalore, family, first, friend, information, malhotra`
- Display key terms: `addressed, bangalore, family, first, friend, information, malhotra`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: addressed, bangalore, family, first, friend, information, malhotra Position/evidence statements: It noted as well that this allegation was also in the applicants’ Basis of Claim Form. | The applicants submit that the evidence did not show that Mr. Application context: I also listened to excerpts of the hearing before the RPD and reviewed the form completed by the applicants, and I find that the RAD properly concluded that the information contained in the affidavits added nothing. | Malhotra’s friend does not, therefore, contain any information that Mr. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5094184` offsets `141-146`; context: [24] First, the RAD indicated that it had listened to the CD of the hearing held before the RPD and concluded that it clearly shows that the issue of an IFA in Bangalore had been addressed at the hearing and that Mr.
- Evidence: `party_position` cue `Claim` at chunk `5094184` offsets `394-399`; context: It noted as well that this allegation was also in the applicants’ Basis of Claim Form.
- Evidence: `reasoning_application` cue `I find` at chunk `5094184` offsets `519-525`; context: I also listened to excerpts of the hearing before the RPD and reviewed the form completed by the applicants, and I find that the RAD properly concluded that the information contained in the affidavits added nothing.
- Evidence: `party_position` cue `submit` at chunk `5094185` offsets `1123-1129`; context: The applicants submit that the evidence did not show that Mr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5094185` offsets `262-271`; context: The affidavit of Mr.
- Evidence: `reasoning_application` cue `therefore` at chunk `5094185` offsets `307-316`; context: Malhotra’s friend does not, therefore, contain any information that Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `5094185` offsets `111-118`; context: However, he also stated in writing and when he testified that he could not move to Bangalore permanently without registering with the authorities.

#### 23295:1:subtheme:6 · paragraphs 19-20

- Raw key terms: `commit, error, find, abandon, accordingly, admitted, adopted, although`
- Display key terms: `commit, error, find, abandon, accordingly, admitted, adopted, although`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: commit, error, find, abandon, accordingly, admitted, adopted, although Position/evidence statements: Malhotra himself admitted before the RPD that, despite all his attempts, he did not know whether the properties in which he claims to have rights really exist. Application context: Malhotra did not say that he was ready to abandon his efforts, I find that it was reasonable to analyze the availability of an IFA on the basis of this assumption. | [28] For all these reasons, I find that the RAD did not commit any error that warrants the intervention of the Court. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5094186` offsets `292-299`; context: Malhotra himself admitted before the RPD that, despite all his attempts, he did not know whether the properties in which he claims to have rights really exist.
- Evidence: `party_position` cue `claims` at chunk `5094186` offsets `327-333`; context: Malhotra himself admitted before the RPD that, despite all his attempts, he did not know whether the properties in which he claims to have rights really exist.
- Evidence: `evidence_fact` cue `evidence` at chunk `5094186` offsets `386-394`; context: On the other hand, the evidence does not show that Mr.
- Evidence: `reasoning_application` cue `I find` at chunk `5094186` offsets `81-87`; context: Malhotra did not say that he was ready to abandon his efforts, I find that it was reasonable to analyze the availability of an IFA on the basis of this assumption.
- Evidence: `reasoning_application` cue `I find` at chunk `5094187` offsets `28-34`; context: [28] For all these reasons, I find that the RAD did not commit any error that warrants the intervention of the Court.

#### Section text

Malhotra v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-08-01
Neutral citation
2014 FC 768
File numbers
IMM-6899-13
Decision Content
Date: 20140801
Docket: IMM-6899-13
Citation: 2014 FC 768
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, August 1, 2014
PRESENT: The Honourable Madam Justice Bédard
BETWEEN:
SUNIL MALHOTRA
SHIKHA THUKRAL
SHUCHI
Applicants
and
MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Board of Canada [IRB]. The RAD dismissed the applicants’ appeal from a decision dated June 28, 2013, by the Refugee Protection Division [RPD], which rejected their refugee claim. For the reasons that follow, the application is dismissed.
I. Background [2] The applicants are citizens of India. Mr. Malhotra alleges that his older brother, who took care of him after the death of their parents in the 1990’s, refused to give him his share of the family properties. He tried in vain to recover his share of the family inheritance, and over time the conflict between the two brothers escalated.

[3] Mr. Malhotra fears his older brother whom he describes as an influential person who has contacts with the police. Mr. Malhotra contends that he was attacked by individuals who were hired by his brother and that some women, who he claims were also hired by his brother, attempted to kidnap his daughter. After these events, the applicants left Chandigarh and relocated temporarily in Mumbai with his parents. They then went to a friend of Mr. Malhotra’s in Bangalore. The applicants claim that their parents and friends could not put them up permanently unless they complied with the mandatory registration process at the regional police office. The applicants did not want to register because they were afraid that this process would enable Mr. Malhotra’s brother to locate them as a result of his contacts with the police.

[4] The applicants eventually returned to Chandigarh, and they lived with another friend of Mr. Malhotra. On November 5, 2012, three armed individuals showed up at their friend’s house and threatened to kill Mr. Malhotra, kidnap the applicants’ daughter and rape Ms. Shuchi. In January 2013, the applicants left their country for Canada.
II. Impugned decision [5] Although this application is directed at the RAD’s decision, to understand the criticisms levelled at that decision, it is useful to summarize the grounds the RPD relied on as the basis for dismissing the applicants’ refugee claim.
RPD decision [6] The RPD found that the availability of an internal flight alternative [IFA] was the determinative issue.

[7] At the hearing, Mr. Malhotra testified about his family’s temporary move to Bangalore. The RPD member asked him if he had proof that they had temporarily relocated to Bangalore, and it was agreed that he would file evidence of this after the hearing. A week after the hearing, but before the RPD’s decision was issued, the applicants submitted an affidavit of Mr. Malhotra’s friend who confirmed that the applicants had stayed with him temporarily in Bangalore. The friend also stated that Mr. Malhotra could not work and live in Bangalore permanently without registering and submitting to a police verification process. The applicants also filed an affidavit of another friend of Mr. Malhotra who put them up on their return to Chandigarh.

[8] The RPD did not make a negative credibility finding against the applicants. Moreover, it found that the applicants had not shown that there was no IFA in Bangalore.

[9] First, the RPD determined that the applicants had not demonstrated that it would be possible for the applicants’ brother to locate them if they moved to Bangalore. The RPD noted that the evidence was divided as to the obligation for anyone who relocates to another town to register with a landlord or new employer. The RPD also noted the evidence relating to the circumstances that could lead to security checks but concluded from the documentary evidence that, in the absence of a central database, the verification reports are kept in the regional police stations, which makes it very difficult, if not impossible, to locate a person unless the police take specific steps to find an individual.

[10] Second, the RPD indicated that it did not understand why Mr. Malhotra’s brother would maintain an interest in the applicants if they chose to live somewhere other than Chandigarh and if Mr. Malhotra abandoned any effort to obtain his share of the family properties.
RAD’s decision [11] The applicants appealed the RPD’s decision. They advanced two grounds of appeal.

[12] First, they submitted that the RPD had erred in its assessment of the IFA by not considering a number of pieces of evidence that showed that the applicants would probably be at risk even if they relocated to Mumbai or Bangalore.

[13] Second, the applicants argued that the RPD had breached its duty of procedural fairness by not considering and addressing in its decision the affidavits of Mr. Malhotra’s friends that were filed after the hearing.

[14] Applying a reasonableness standard, the RAD found that the RPD’s conclusion regarding the availability of an IFA was reasonable. Referring to the decision in Cepeda-Gutierrez v Canada, 1998 CanLII 8667 [Cepada-Gutierrez], the RAD stated that it had to determine whether the RPD had failed to consider or address in its decision important evidence that contradicted its findings and concluded that this was not the case.

[15] The RAD found that the RPD had correctly applied the two branches of the test developed for analyzing the availability of an IFA. Citing certain passages from the RPD decision, the RAD determined first that it was clear from the decision that the RPD had considered the evidence about Mr. Malhotra’s brother’s motive for revenge but had concluded that the applicants had not demonstrated the risk they would face if returned to India.

[16] Second, the RAD found that the affidavits of Mr. Malhotra’s friends were not important enough that omitting to mention them in the decision constituted a breach of procedural fairness. The RAD considered that the statements in the affidavits added nothing because they confirmed what Mr. Malhotra had already said about the applicants’ stay in Bangalore and the mandatory registration process. The RAD also found that it was clear from the RPD’s decision that it had weighed the contradictory evidence regarding mandatory registration but that this issue was not as important as the issue of the actual danger the applicants would face if returned to India.
III. Issues [17] The applicants submit that the RAD’s decision was unreasonable. They formulated three criticisms of the RAD’s decision:
• The RAD erred by not finding that the RPD had failed to consider critical evidence that showed there was no IFA available in Bangalore;
• The RAD erred by finding that the RPD had not erred in failing to consider the affidavits filed after the hearing;
• The RAD erred by not noting the error committed by the RPD when it required in its IFA analysis that the applicant renounce his share of the inheritance.
IV. Analysis Did the RAD err by finding that the RPD had assessed the evidence reasonably and that its conclusion as to the availability of an IFA was reasonable? [18] The evidence that the RPD allegedly did not deal with is as follows:
• Mr. Malhotra’s sister informed him that, following his departure, their older brother swore to kill the applicants if they returned to India regardless of where they lived;
• Mr. Malhotra’s brother is very influential and has the support of the police and some politicians;
• The police have information about the dispute between Mr. Malhotra and his brother;
• The desire for revenge on the part of Mr. Malhotra’s brother is deeply rooted;
• The affidavit of Mr. Malhotra’s friend confirms that the applicants could not move to Bangalore because of the mandatory registration and verification process;
• The documentary evidence establishes that the police frequently arrest individuals because of pressure by influential people or corruption.

[19] With respect, I consider that the RAD’s assessment of the RPD’s evidentiary findings was entirely reasonable and that the reasons in support of its conclusion were reasonably articulated.

[20] It is true that the RPD did not specifically deal with the facts set out at paragraph 18. However, it is clear that the RAD understood that the applicants were arguing that the RPD had not dealt with this evidence (see para 10 of the RAD’s decision) but that it found, in light of Cepada-Gutierrez, that this evidence was not important enough to justify its intervention. I agree.

[21] First, the RAD found that the RPD had considered the evidence that could explain the desire for revenge on the part of Mr. Malhotra’s brother, that is, Mr. Malhotra’s attempts to recover his share of the inheritance. This finding is reasonable in light of the evidence and the excerpts from the RPD’s decision cited by the RAD. The evidence that the RAD allegedly failed to address and that relates to the motive of Mr. Malhotra’s brother for harming the applicants (that the desire for revenge on the part of Mr. Malhotra’s brother was deeply rooted and that he had sworn to attack the applicants if they returned to India) could not have had an impact on the findings of the RPD or the RAD. As stated, it is clear from the two decisions that both the RPD and the RAD understood Mr. Malhotra’s allegations concerning the nature of the dispute between him and his brother and the latter’s motive for wanting to harm his family.

[22] The other pieces of evidence that were not mentioned in the RPD’s decision all relate to the registration and verification process in a city like Bangalore and to the ability of Mr. Malhotra’s brother to locate the applicants because of his connections with the police. The RAD properly found that it was reasonable for the RPD to have considered that the applicants had not established that Mr. Malhotra’s brother could locate them. The RAD found that the RPD had reviewed the contradictory evidence about the registration process. It is clear from the RPD’s decision that it had emotionally reviewed the contradictory evidence in this regard but had concluded that, in the absence of central police databases, it was very difficult to find a person following a security check unless there was a match between that person and the information held by the regional police. This finding was reasonable having regard to the evidence adduced before the RPD. In such a context, the fact that the Chandigarh police had information about the dispute between Mr. Malhotra and his brother, that Mr. Malhotra’s brother had contacts with the Chandigarh police and that the documentary evidence showed that the police frequently arrest individuals because of pressure by influential persons do not constitute crucial evidence. There was no evidence in the record that the applicants were of such interest to the Chandigarh police force that it would take extraordinary steps to track them down across the country.
Did the RAD err by finding that the RPD had not erred in failing to consider the affidavits filed after the hearing? [23] It is true that the RPD did not mention in its decision the affidavits filed by the applicants after the hearing. However, it cannot be inferred from this omission that the RPD did not consider the affidavits. In any event, I consider that the RAD reasonably concluded that these affidavits added nothing and that they were not determinative.

[24] First, the RAD indicated that it had listened to the CD of the hearing held before the RPD and concluded that it clearly shows that the issue of an IFA in Bangalore had been addressed at the hearing and that Mr. Malhotra had testified about the temporary relocation of his family at a friend’s house in Bangalore. It noted as well that this allegation was also in the applicants’ Basis of Claim Form. I also listened to excerpts of the hearing before the RPD and reviewed the form completed by the applicants, and I find that the RAD properly concluded that the information contained in the affidavits added nothing.

[25] First, Mr. Malhotra stated in writing and when he testified that he had lived with a friend in Bangalore. However, he also stated in writing and when he testified that he could not move to Bangalore permanently without registering with the authorities. The affidavit of Mr. Malhotra’s friend does not, therefore, contain any information that Mr. Malhotra had not addressed, and the RPD did not make a negative credibility finding against the applicants. In addition, the information about the mandatory registration process was not determinative because the RPD found that, despite the registration, it was difficult to locate individuals who have been the subject of a security check, in the absence of a centralized data bank.
Did the RAD err by not noting the error committed by the RPD when it required in its IFA analysis that Mr. Malhotra renounce his share of the inheritance? [26] The applicants also fault the RAD for not recognizing the error committed by the RPD when it required as a premise to the IFA analysis that Mr. Malhotra abandon any attempt to recover his share of the inheritance. The applicants submit that the evidence did not show that Mr. Malhotra was ready to renounce his share of the family inheritance.

[27] Although Mr. Malhotra did not say that he was ready to abandon his efforts, I find that it was reasonable to analyze the availability of an IFA on the basis of this assumption. On the one hand, Mr. Malhotra himself admitted before the RPD that, despite all his attempts, he did not know whether the properties in which he claims to have rights really exist. On the other hand, the evidence does not show that Mr. Malhotra took steps to attempt to recover his share of the family inheritance since he arrived in Canada. Finally, in the context of this case, it was not unreasonable to expect that Mr. Malhotra abandon these efforts in order to keep his family safe instead of having to go into exile in another country. Accordingly, I find that the RAD did not commit an error err by not intervening with respect to the premise adopted by the RPD in its analysis of the availability of an IFA.

[28] For all these reasons, I find that the RAD did not commit any error that warrants the intervention of the Court.


## 23295:2 · paragraphs 21-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a0831a5348a574d9eb4106ea65e7c01a6c373091706c1a1aa698f924962a1c50`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23295:2:subtheme:1 · paragraphs 21-22

- Raw key terms: `adjudges, application, cause, certified, citizenship, court, dard, date`
- Display key terms: `adjudges, certified, dard, date`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adjudges, certified, dard, date No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that the application for judicial review is dismissed. No question is certified.
“Marie-Josee Bédard”
Judge
Certified true translation
Mary Jo Egan, LLB
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6899-13
STYLE OF CAUSE:
SUNIL MALHOTRA, SHIKHA THUKRAL SHUCHI v MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
MONTRÉAL, QUEBEC
DATE OF HEARING:
JULY 10, 2014
REASONS FOR 

## 23295:3 · paragraphs 23-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8ed5653c39601f10946d4965572dcd983d308cc3b300ee48b31472b44f16047b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23295:3:subtheme:1 · paragraphs 23-23

- Raw key terms: `appearances, applicants, attorney, august, canada, claude, counsel, dard`
- Display key terms: `august, claude, dard`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, claude, dard No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT:
BÉDARD J.
DATED:
AUGUST 1, 2014
APPEARANCES:
Claude Whalen
FOR THE APPLICANTS
Emilie Tremblay
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Counsel
Montréal, Quebec
FOR THE APPLICANTS
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
