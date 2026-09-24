# Discussion Units: case 10669

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **43**
- Continuity pairs: **42**
- Discussion Units: **4**
- Paragraph source hashes: **43**
- Sub-themes: **14**

## 10669:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `368eb1d392a723216d1bb7b4131d5648bffbd72cba0322b145a93e99c993a423`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10669:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `respondent, identity, application, authorities, beken, refugee, asylum, claim`
- Display key terms: `identity, authorities, beken, refugee, asylum`
- Argument roles: `counterargument_limitation, disposition, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, party_position, reasoning_application Display terms: identity, authorities, beken, refugee, asylum Position/evidence statements: asylum application file together with the documents related to his status in Norway, where he claims to have lost his refugee status because he had been out of the country for more than six months. | He submitted that the respondent had failed to establish his identity. Rule/authority context: A few months later, while he was still in Norway, he applied for asylum under another identity, Beken Kera Milka. | He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, th Application context: He told Norwegian authorities that he wished to visit a friend instead of stating the real reason he was in Norway, which was to apply for asylum. | He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, th Operative outcome context: His application was granted. | He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, th Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4537151` offsets `750-755`; context: A few months later, while he was still in Norway, he applied for asylum under another identity, Beken Kera Milka.
- Evidence: `reasoning_application` cue `apply` at chunk `4537151` offsets `558-563`; context: He told Norwegian authorities that he wished to visit a friend instead of stating the real reason he was in Norway, which was to apply for asylum.
- Evidence: `counterargument_limitation` cue `however` at chunk `4537151` offsets `639-646`; context: He was, however, given a copy of the passport.
- Evidence: `disposition` cue `granted` at chunk `4537151` offsets `812-819`; context: His application was granted.
- Evidence: `governing_rule` cue `under` at chunk `4537152` offsets `182-187`; context: He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, the name under which he had applied for an American visa in 2007, after having agreed to a marriage of convenience with a friend who had just won a lottery granting access to permanent residence in the United States.
- Evidence: `reasoning_application` cue `applied` at chunk `4537152` offsets `386-393`; context: He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, the name under which he had applied for an American visa in 2007, after having agreed to a marriage of convenience with a friend who had just won a lottery granting access to permanent residence in the United States.
- Evidence: `disposition` cue `denied` at chunk `4537152` offsets `239-245`; context: He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, the name under which he had applied for an American visa in 2007, after having agreed to a marriage of convenience with a friend who had just won a lottery granting access to permanent residence in the United States.
- Evidence: `reasoning_application` cue `therefore` at chunk `4537153` offsets `156-165`; context: He therefore left Norway for Mexico on January 27, 2014.
- Evidence: `disposition` cue `granted` at chunk `4537153` offsets `72-79`; context: [4] The respondent subsequently turned to Mexico, where the authorities granted him a six‑month temporary visa.
- Evidence: `party_position` cue `claims` at chunk `4537155` offsets `283-289`; context: asylum application file together with the documents related to his status in Norway, where he claims to have lost his refugee status because he had been out of the country for more than six months.
- Evidence: `reasoning_application` cue `because` at chunk `4537155` offsets `322-329`; context: asylum application file together with the documents related to his status in Norway, where he claims to have lost his refugee status because he had been out of the country for more than six months.
- Evidence: `party_position` cue `submitted` at chunk `4537156` offsets `107-116`; context: He submitted that the respondent had failed to establish his identity.
- Evidence: `disposition` cue `denied` at chunk `4537157` offsets `31-37`; context: [8] On April 27, 2016, the RPD denied the respondent’s refugee claim, finding that he had not established his identity.

#### 10669:1:subtheme:2 · paragraphs 10-11

- Raw key terms: `appear, birth, confusion, date, dates, december, file, identity`
- Display key terms: `appear, birth, confusion, date, dates, december, file, identity`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: appear, birth, confusion, date, dates, december, file, identity Position/evidence statements: As for the date of birth, the respondent claimed he did not know his true date of birth and had thus always used a fictitious date, December 29, 1976. Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537159` offsets `573-578`; context: The RPD deemed that it had not received information that would have clarified this issue.
- Evidence: `party_position` cue `claimed` at chunk `4537160` offsets `455-462`; context: As for the date of birth, the respondent claimed he did not know his true date of birth and had thus always used a fictitious date, December 29, 1976.
- Evidence: `evidence_fact` cue `found that` at chunk `4537160` offsets `725-735`; context: It found that the confusion surrounding the respondent’s date of birth was such that it was impossible to determine what said date could be, whereas this is an important aspect of establishing a refugee claimant’s identity.
- Evidence: `counterargument_limitation` cue `However` at chunk `4537160` offsets `309-316`; context: However, the RPD noted that, even when adjusting for the two calendars, the years of birth do not align.

#### 10669:1:subtheme:3 · paragraphs 12-13

- Raw key terms: `appeal, evidence, member, refugee, addressed, administrative, admissibility, alleged`
- Display key terms: `refugee, addressed, administrative, admissibility, alleged`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: refugee, addressed, administrative, admissibility, alleged Position/evidence statements: The Member found that it was inadmissible, as the respondent had been unable, in her view, to provide a satisfactory explanation for why that evidence could not have been submitted to the RPD before the refugee claim was Operative outcome context: The Member found that it was inadmissible, as the respondent had been unable, in her view, to provide a satisfactory explanation for why that evidence could not have been submitted to the RPD before the refugee claim was Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537161` offsets `87-92`; context: [12] The RAD member who heard the respondent’s appeal [the Member] first addressed the issue of the admissibility of the new documentary evidence the respondent filed in support of his appeal.
- Evidence: `party_position` cue `submitted` at chunk `4537161` offsets `364-373`; context: The Member found that it was inadmissible, as the respondent had been unable, in her view, to provide a satisfactory explanation for why that evidence could not have been submitted to the RPD before the refugee claim was denied.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537161` offsets `137-145`; context: [12] The RAD member who heard the respondent’s appeal [the Member] first addressed the issue of the admissibility of the new documentary evidence the respondent filed in support of his appeal.
- Evidence: `disposition` cue `denied` at chunk `4537161` offsets `414-420`; context: The Member found that it was inadmissible, as the respondent had been unable, in her view, to provide a satisfactory explanation for why that evidence could not have been submitted to the RPD before the refugee claim was denied.
- Evidence: `issue` cue `issues` at chunk `4537162` offsets `262-268`; context: Huruglica, 2016 FCA 93 [Huruglica] regarding the RAD’s role as an administrative appeal body and a subsequent decision by three RAD members on the level of deference owed to the RPD with respect to issues of credibility, the Member stated that she would [translation] “conduct an independent analysis of the evidence to determine whether the RPD had committed the errors alleged by the appellant” and that [translation] “if an error of fact, law or mixed fact and law was committed, [she would] intervene through one of the remedies set out in sections 110 and 111 of the [Immigration and Refugee Protection Act, SC 2001, c 27 (Act)].
- Evidence: `evidence_fact` cue `evidence` at chunk `4537162` offsets `372-380`; context: Huruglica, 2016 FCA 93 [Huruglica] regarding the RAD’s role as an administrative appeal body and a subsequent decision by three RAD members on the level of deference owed to the RPD with respect to issues of credibility, the Member stated that she would [translation] “conduct an independent analysis of the evidence to determine whether the RPD had committed the errors alleged by the appellant” and that [translation] “if an error of fact, law or mixed fact and law was committed, [she would] intervene through one of the remedies set out in sections 110 and 111 of the [Immigration and Refugee Protection Act, SC 2001, c 27 (Act)].

#### 10669:1:subtheme:4 · paragraphs 14-14

- Raw key terms: `added, american, apart, appeal, authorities, beken, biometric, birth`
- Display key terms: `added, american, apart, authorities, beken, biometric, birth`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: added, american, apart, authorities, beken, biometric, birth Position/evidence statements: [14] On the merits of the appeal, the Member, recognizing that the issue of a refugee claimant’s identity is a question of fact and that it is determinative, criticized the RPD for having rejected outright the documents  Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537163` offsets `67-72`; context: [14] On the merits of the appeal, the Member, recognizing that the issue of a refugee claimant’s identity is a question of fact and that it is determinative, criticized the RPD for having rejected outright the documents the respondent had submitted to establish his identity, even though those documents had not been issued as identity documents.
- Evidence: `party_position` cue `submitted` at chunk `4537163` offsets `239-248`; context: [14] On the merits of the appeal, the Member, recognizing that the issue of a refugee claimant’s identity is a question of fact and that it is determinative, criticized the RPD for having rejected outright the documents the respondent had submitted to establish his identity, even though those documents had not been issued as identity documents.
- Evidence: `evidence_fact` cue `testimony` at chunk `4537163` offsets `667-676`; context: She specifically criticized the RPD in this regard for having placed too much emphasis on the fact that the respondent had lied to the Norwegian and American authorities, stating that, apart from the problem of the respondent’s date of birth, the RPD had not identified any inconsistencies or contradictions between his testimony and the evidence.

#### Section text

Canada (Public Safety and Emergency Preparedness) v. Gebrewold
Court (s) Database
Federal Court Decisions
Date
2018-04-06
Neutral citation
2018 FC 374
File numbers
IMM-4058-17
Decision Content
Date: 20180406
Docket: IMM‑4058‑17
Citation: 2018 FC 374
[UNREVISED CERTIFIED ENGLISH TRANSLATION]
Ottawa, Ontario, April 6, 2018
PRESENT: The Honourable Mr. Justice LeBlanc
BETWEEN:
THE MINISTER OF PUBLIC SAFETY AND EMERGENCY PREPAREDNESS
Applicant
and
BEKEN SHITAYE GEBREWOLD
Respondent
JUDGMENT AND REASONS
I. Introduction

[1] The applicant, the Minister of Public Safety and Emergency Preparedness [the Minister], is contesting, by way of judicial review, a decision by the Immigration and Refugee Board’s Refugee Appeal Division [RAD], which set aside a decision by the Refugee Protection Division [RPD] to dismiss the respondent’s refugee claim on the grounds that he had failed to establish his identity.
II. Background
A. The respondent’s migratory background

[2] The respondent is Ethiopian. He reports that he was born on December 29, 1976. His migratory path is unusual, to say the least. He left Ethiopia for Norway in 2009, fearing the security forces of the regime in power, who suspected him of belonging to and participating in the activities of the Oromo Liberation Front. At that time, he had an Ethiopian passport, which he states was issued in 2007 to Beken Shitaye Gebrewold. He told Norwegian authorities that he wished to visit a friend instead of stating the real reason he was in Norway, which was to apply for asylum. They did not believe him, and his passport was seized. He was, however, given a copy of the passport. A few months later, while he was still in Norway, he applied for asylum under another identity, Beken Kera Milka. His application was granted.

[3] In 2013, fearing that Ethiopian nationals living in Norway might report him to the authorities, the respondent planned to leave Norway. He first tried to obtain an American visa under the name Beken Kera Milka, but his application was denied, as the American authorities noted that the respondent’s fingerprints matched those of Beken Shitaye Gebrewold, the name under which he had applied for an American visa in 2007, after having agreed to a marriage of convenience with a friend who had just won a lottery granting access to permanent residence in the United States. The ploy was discovered, and the visa application was denied. The passport the respondent provided in support of that first visa application was issued to Beken Shitaye Gebrewold, born on September 30, 1967.

[4] The respondent subsequently turned to Mexico, where the authorities granted him a six‑month temporary visa. The visa was issued to Beken Kera Milka. He therefore left Norway for Mexico on January 27, 2014. In July 2014, he went to the United States to apply for asylum there. Prior to doing so, he destroyed the documents in his possession from the Norwegian authorities, including, apparently, the copy of the passport seized by the Norwegian authorities in 2009. Thus, he arrived at the U.S. border without identity documents. He told the American authorities that he had travelled to Mexico directly from Ethiopia. The respondent was placed in detention. In January 2015, the American authorities discovered that he had lived in Norway. The respondent was informed of this. He subsequently withdrew his application for asylum. He later pleaded guilty to charges of fraud and misrepresentation. A notice of removal was issued against him. He was to appear in person in Baltimore on June 16, 2015, for the execution of the removal order that had been issued against him. He did not appear, fearing that he would be sent back to Ethiopia.
B. Arrival in Canada and refugee claim

[5] On July 22, 2015, the respondent went to Buffalo with the aim of crossing the Canadian border, which he did, illegally, on August 25, 2015. When he arrived in Canada, he was stopped by officers of the Royal Canadian Mounted Police and handed over to the Canada Border Services Agency [CBSA] authorities. He made a refugee claim. He had no identity documents on his person.

[6] The hearing before the RPD was scheduled for November 25, 2015. In anticipation of the hearing, the RPD, in a letter dated October 29, 2015, required the respondent to provide his U.S. asylum application file together with the documents related to his status in Norway, where he claims to have lost his refugee status because he had been out of the country for more than six months.

[7] The day before the hearing, the Minister served notice of his intention to intervene in the matter. He submitted that the respondent had failed to establish his identity. The hearing was postponed to February 3, 2016. It continued on March 9 and 31, 2016.
C. The RPD’s decision

[8] On April 27, 2016, the RPD denied the respondent’s refugee claim, finding that he had not established his identity. In particular, the RPD was not satisfied with the respondent’s efforts to obtain information from either the Norwegian or the American authorities, including the passport seized by Norwegian authorities in 2009 or, at the very least, a copy of that passport, which the RPD considered to be of prime importance. Moreover, in the absence of that passport and of the U.S. asylum application file, the RPD gave little weight to the national identity card filed by the respondent: it deemed it to be in [translation] “pitiful condition” and noted that the year of birth appearing on the card, 1966 -, did not correspond to any of the birth years in the file.

[9] The RPD also gave little weight to the other documents provided by the respondent to establish his identity as Beken Shitaye Gebrewold, since they were not government‑issued identity documents. There was a document related to a vehicle, an insurance certificate, photographs taken from a graduation album, a diploma from the Ministry of Education, a general Agriculture diploma, a certificate of education, a translated excerpt from a newspaper related to a request to change names from Kekele to Beken, two documents from “Ambo University College” and a document entitled “Student clearance/withdrawal form”.

[10] Lastly, the RPD noted the confusion surrounding the respondent’s date of birth, specifying that the respondent reported that he was born on December 29, 1976, when he arrived in Canada, whereas other birth dates appear in his file: September 30, 1967, according to the passport provided in support of his American visa application in 2007; July 19, 1975, the date of birth associated with Beken Kera Milka; and 1966, which is the year of birth appearing on the national identity card. The RPD deemed that it had not received information that would have clarified this issue.

[11] Moreover, the RPD rejected the respondent’s attempts to explain the discrepancies among the birth years and the confusion surrounding his true date of birth. With regard to the years, the discrepancies could apparently be explained by the use of a calendar other than the Gregorian calendar in Ethiopia. However, the RPD noted that, even when adjusting for the two calendars, the years of birth do not align. As for the date of birth, the respondent claimed he did not know his true date of birth and had thus always used a fictitious date, December 29, 1976. The RPD noted, however, that this did not explain why that date -, or at the very least December 29, did not appear in the other dates of birth in the file. It found that the confusion surrounding the respondent’s date of birth was such that it was impossible to determine what said date could be, whereas this is an important aspect of establishing a refugee claimant’s identity.
D. The RAD’s decision

[12] The RAD member who heard the respondent’s appeal [the Member] first addressed the issue of the admissibility of the new documentary evidence the respondent filed in support of his appeal. The Member found that it was inadmissible, as the respondent had been unable, in her view, to provide a satisfactory explanation for why that evidence could not have been submitted to the RPD before the refugee claim was denied.

[13] Proceeding to cite Canada (Citizenship and Immigration) v. Huruglica, 2016 FCA 93 [Huruglica] regarding the RAD’s role as an administrative appeal body and a subsequent decision by three RAD members on the level of deference owed to the RPD with respect to issues of credibility, the Member stated that she would [translation] “conduct an independent analysis of the evidence to determine whether the RPD had committed the errors alleged by the appellant” and that [translation] “if an error of fact, law or mixed fact and law was committed, [she would] intervene through one of the remedies set out in sections 110 and 111 of the [Immigration and Refugee Protection Act, SC 2001, c 27 (Act)].”

[14] On the merits of the appeal, the Member, recognizing that the issue of a refugee claimant’s identity is a question of fact and that it is determinative, criticized the RPD for having rejected outright the documents the respondent had submitted to establish his identity, even though those documents had not been issued as identity documents. She specifically criticized the RPD in this regard for having placed too much emphasis on the fact that the respondent had lied to the Norwegian and American authorities, stating that, apart from the problem of the respondent’s date of birth, the RPD had not identified any inconsistencies or contradictions between his testimony and the evidence. Moreover, she added that the evidence from the American authorities, namely the biometric data, leads to the conclusion that Beken Shitaye Gebrewold and Beken Kera Milka are one and the same person. It also confirms the respondent’s travel history.

## 10669:2 · paragraphs 15-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1ca23205f7a7e6ee689b8734abb3c7b75c629fd9201744d5bab91a4213aa714b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10669:2:subtheme:1 · paragraphs 15-18

- Raw key terms: `appellant, balance, birth, case, date, identity, member, probabilities`
- Display key terms: `appellant, balance, birth, case, date, identity, probabilities`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: appellant, balance, birth, case, date, identity, probabilities Position/evidence statements: [46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to con Application context: [46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to con | [47] With respect to the date of birth, I find that this is a case where he can be given the benefit of the doubt. Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4537165` offsets `292-298`; context: [46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to conclude on a balance of probabilities that the appellant is indeed who he claims to be, Beken Shitaye Gebrewold, an Ethiopian citizen.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537165` offsets `177-185`; context: [46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to conclude on a balance of probabilities that the appellant is indeed who he claims to be, Beken Shitaye Gebrewold, an Ethiopian citizen.
- Evidence: `reasoning_application` cue `conclude` at chunk `4537165` offsets `217-225`; context: [46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to conclude on a balance of probabilities that the appellant is indeed who he claims to be, Beken Shitaye Gebrewold, an Ethiopian citizen.
- Evidence: `evidence_fact` cue `testimony` at chunk `4537166` offsets `301-310`; context: Even though I was not present in the courtroom to observe him, I noted that his testimony was fluid, that he answered the questions in a straightforward manner and that he provided details.
- Evidence: `reasoning_application` cue `I find` at chunk `4537166` offsets `40-46`; context: [47] With respect to the date of birth, I find that this is a case where he can be given the benefit of the doubt.
- Evidence: `counterargument_limitation` cue `but` at chunk `4537167` offsets `181-184`; context: Consequently, she set aside the RPD’s decision but referred the case back to it so that it could decide on the merit of the refugee claim itself.

#### 10669:2:subtheme:2 · paragraphs 19-20

- Raw key terms: `having, issue, member, respondent, acceptable, account, affidavit, american`
- Display key terms: `having, acceptable, account, affidavit, american`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: having, acceptable, account, affidavit, american Position/evidence statements: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and  | Lastly, he submits that the respondent’s failure to swear an affidavit in support of his position in this judicial review is fatal to his case. Rule/authority context: Issue and standard of review Application context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and  Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4537168` offsets `235-243`; context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.
- Evidence: `party_position` cue `argues` at chunk `4537168` offsets `179-185`; context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537168` offsets `281-289`; context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.
- Evidence: `reasoning_application` cue `because` at chunk `4537168` offsets `433-440`; context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.
- Evidence: `counterargument_limitation` cue `but` at chunk `4537168` offsets `496-499`; context: He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.
- Evidence: `issue` cue `Issue` at chunk `4537169` offsets `300-305`; context: Issue and standard of review
- Evidence: `party_position` cue `submits` at chunk `4537169` offsets `162-169`; context: Lastly, he submits that the respondent’s failure to swear an affidavit in support of his position in this judicial review is fatal to his case.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4537169` offsets `212-221`; context: Lastly, he submits that the respondent’s failure to swear an affidavit in support of his position in this judicial review is fatal to his case.
- Evidence: `governing_rule` cue `standard of review` at chunk `4537169` offsets `310-328`; context: Issue and standard of review

#### 10669:2:subtheme:3 · paragraphs 21-25

- Raw key terms: `canada, case, identity, paragraph, accept, acceptable, citizenship, immigration`
- Display key terms: `case, identity, paragraph, accept, acceptable`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: case, identity, paragraph, accept, acceptable Rule/authority context: It is not disputed that the standard of review that applies in this case is that of reasonableness (Huruglica, at paragraph 35; Paye v. | [22] Moreover, pursuant to section 106 of the Act, the fact that a foreign national who arrives in Canada without acceptable identity documents can neither provide an explanation nor prove having taken the required steps Application context: It is not disputed that the standard of review that applies in this case is that of reasonableness (Huruglica, at paragraph 35; Paye v. | This is the case because a number of important factors in implementing this regime, such as admissibility in Canada, evaluating the need for protection, assessing the risk to public safety in Canada or the propensity to  Evidence spans paragraphs 21-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537170` offsets `9-14`; context: [19] The issue here is to determine whether the Member, in finding as she did, committed a reviewable error within the meaning of subsection 18.
- Evidence: `governing_rule` cue `standard of review` at chunk `4537170` offsets `222-240`; context: It is not disputed that the standard of review that applies in this case is that of reasonableness (Huruglica, at paragraph 35; Paye v.
- Evidence: `reasoning_application` cue `applies` at chunk `4537170` offsets `246-253`; context: It is not disputed that the standard of review that applies in this case is that of reasonableness (Huruglica, at paragraph 35; Paye v.
- Evidence: `issue` cue `whether` at chunk `4537171` offsets `212-219`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v.
- Evidence: `counterargument_limitation` cue `But` at chunk `4537171` offsets `182-185`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v.
- Evidence: `reasoning_application` cue `because` at chunk `4537172` offsets `411-418`; context: This is the case because a number of important factors in implementing this regime, such as admissibility in Canada, evaluating the need for protection, assessing the risk to public safety in Canada or the propensity to accept or reject the controls required by the Act, depend upon it.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4537173` offsets `15-26`; context: [22] Moreover, pursuant to section 106 of the Act, the fact that a foreign national who arrives in Canada without acceptable identity documents can neither provide an explanation nor prove having taken the required steps to obtain the documents can affect the RPD’s assessment of the claimant’s credibility.

#### 10669:2:subtheme:4 · paragraphs 26-27

- Raw key terms: `whether, address, advantage, analysis, appeal, applying, aspect, assessing`
- Display key terms: `whether, address, advantage, analysis, applying, aspect, assessing`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: whether, address, advantage, analysis, applying, aspect, assessing Rule/authority context: While it is true that it must carry out its own analysis of the file in applying the correctness standard of review, except with regard to assessing credibility or the value of oral testimonies, where the RAD, when the R Application context: [24] I therefore consider the issue to be whether it was reasonable for the RAD, considering all the circumstances of this case, to disregard this problem by giving the respondent the benefit of the doubt. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537175` offsets `30-35`; context: [24] I therefore consider the issue to be whether it was reasonable for the RAD, considering all the circumstances of this case, to disregard this problem by giving the respondent the benefit of the doubt.
- Evidence: `reasoning_application` cue `therefore` at chunk `4537175` offsets `7-16`; context: [24] I therefore consider the issue to be whether it was reasonable for the RAD, considering all the circumstances of this case, to disregard this problem by giving the respondent the benefit of the doubt.
- Evidence: `issue` cue `whether` at chunk `4537176` offsets `298-305`; context: In other words, it is insufficient for the RAD to ask whether it would have reached a different conclusion had it been in the RPD’s position, without regard for any aspect of the RPD’s decision (Huruglica, at paragraph 79).
- Evidence: `governing_rule` cue `standard of review` at chunk `4537176` offsets `592-610`; context: While it is true that it must carry out its own analysis of the file in applying the correctness standard of review, except with regard to assessing credibility or the value of oral testimonies, where the RAD, when the RPD truly enjoys a meaningful advantage over it, must occasionally show deference (Huruglica, at paragraph 70), its role is to “catch all mistakes made by the RPD, be it on the law or the facts” (Huruglica, at paragraph 98).

#### 10669:2:subtheme:5 · paragraphs 28-33

- Raw key terms: `respondent, benefit, doubt, general, given, authorities, birth, context`
- Display key terms: `benefit, doubt, given, authorities, birth, context`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: benefit, doubt, given, authorities, birth, context Position/evidence statements: Still, this does not explain how the fact that the respondent testified in a direct and fluid manner resolves the inconsistencies and contradictions in his testimony and in the evidence in general and argues, in that con Application context: The RAD decision reads as if, on this issue, it conducted a de novo proceeding and, therefore, without regard to the RPD decision on this issue, based its findings on the recording of the hearing before the RPD. | Canada (Minister of Citizenship and Immigration), 2003 FCT 454 [Noga], the benefit of the doubt principle “applies in a limited number of circumstances”. Evidence spans paragraphs 28-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537177` offsets `313-318`; context: I infer from this that it was satisfied that the RPD had not erred in finding as it did regarding this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537177` offsets `81-89`; context: [26] However, for all practical purposes, the RAD conceded that the respondent’s evidence contained inconsistencies and contradictions with respect to his date of birth (RAD Decision, at paragraphs 41 and 46).
- Evidence: `reasoning_application` cue `therefore` at chunk `4537177` offsets `571-580`; context: The RAD decision reads as if, on this issue, it conducted a de novo proceeding and, therefore, without regard to the RPD decision on this issue, based its findings on the recording of the hearing before the RPD.
- Evidence: `party_position` cue `argues` at chunk `4537178` offsets `600-606`; context: Still, this does not explain how the fact that the respondent testified in a direct and fluid manner resolves the inconsistencies and contradictions in his testimony and in the evidence in general and argues, in that context, in favour of giving the respondent the benefit of the doubt.
- Evidence: `evidence_fact` cue `testimony` at chunk `4537178` offsets `317-326`; context: The RAD’s only justification was to note that the respondent [translation] “answered the questions directly”, “in a straightforward manner”, that his testimony [translation] “was fluid” and that he [translation] “provided details”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537179` offsets `251-259`; context: Benefit of the doubt should be given only “when all available evidence has been obtained and checked and when the examiner is satisfied as to the applicant’s general credibility”, which assumes that the applicant’s statements are “coherent and plausible” (Noga, at paragraphs 10 to 12).
- Evidence: `reasoning_application` cue `applies` at chunk `4537179` offsets `142-149`; context: Canada (Minister of Citizenship and Immigration), 2003 FCT 454 [Noga], the benefit of the doubt principle “applies in a limited number of circumstances”.
- Evidence: `evidence_fact` cue `record` at chunk `4537180` offsets `565-571`; context: Moreover, I note in the record that, according to the checks conducted by the CBSA, the Ethiopian authorities have been using Gregorian calendar dates on passports for decades.

#### 10669:2:subtheme:6 · paragraphs 34-36

- Raw key terms: `benefit, birth, date, doubt, principle, respondent, application, claimant`
- Display key terms: `benefit, birth, date, doubt, principle`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: benefit, birth, date, doubt, principle Application context: [32] I find the RAD’s decision to be all the more unintelligible concerning the issue of the date of birth since the refugee claimant in this case, throughout his migratory path, obtained or attempted to obtain the right | [34] The RPD found that the confusion surrounding the respondent’s date of birth was such that it could not [translation] “conclude that the [respondent] had been able to persuade [it] as to what his date of birth could  Evidence spans paragraphs 34-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4537183` offsets `80-85`; context: [32] I find the RAD’s decision to be all the more unintelligible concerning the issue of the date of birth since the refugee claimant in this case, throughout his migratory path, obtained or attempted to obtain the right to enter a foreign country by misrepresenting his identity and destroying the documents that could have adversely affected him in this regard.
- Evidence: `evidence_fact` cue `record` at chunk `4537183` offsets `403-409`; context: It seems to me that, with such a track record, and considering the number of birth dates on record, the inconsistencies and contradictions in the evidence presented by the respondent to try to explain the situation and the findings about the respondent’s lack of effort to produce satisfactory evidence in this regard, the RAD should have explained, other than by giving its general impressions on the manner in which the respondent testified before the RPD, how the benefit of the doubt principle could apply in the circumstances.
- Evidence: `reasoning_application` cue `I find` at chunk `4537183` offsets `5-11`; context: [32] I find the RAD’s decision to be all the more unintelligible concerning the issue of the date of birth since the refugee claimant in this case, throughout his migratory path, obtained or attempted to obtain the right to enter a foreign country by misrepresenting his identity and destroying the documents that could have adversely affected him in this regard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4537184` offsets `120-128`; context: [33] This is even more troubling given that the RAD, as I mentioned previously, seemed to concede that the respondent’s evidence regarding his date of birth contained contradictions and inconsistencies.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4537184` offsets `203-215`; context: Nevertheless, two essential considerations in the application of the benefit of the doubt principle are that the refugee claimant’s statements be “coherent and plausible” (Noga, at paragraphs 10 to 12).
- Evidence: `evidence_fact` cue `found that` at chunk `4537185` offsets `13-23`; context: [34] The RPD found that the confusion surrounding the respondent’s date of birth was such that it could not [translation] “conclude that the [respondent] had been able to persuade [it] as to what his date of birth could be, an important element in establishing any person’s identity.
- Evidence: `reasoning_application` cue `conclude` at chunk `4537185` offsets `123-131`; context: [34] The RPD found that the confusion surrounding the respondent’s date of birth was such that it could not [translation] “conclude that the [respondent] had been able to persuade [it] as to what his date of birth could be, an important element in establishing any person’s identity.

#### 10669:2:subtheme:7 · paragraphs 37-38

- Raw key terms: `case, decision, accordance, according, address, advantageous, affects, allowed`
- Display key terms: `case, accordance, according, address, advantageous, affects, allowed`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: case, accordance, according, address, advantageous, affects, allowed Application context: [36] The Minister’s application for judicial review will therefore be allowed, the RAD’s decision will be set aside, and the case will be referred back to a different RAD member for redetermination in accordance with the Operative outcome context: [36] The Minister’s application for judicial review will therefore be allowed, the RAD’s decision will be set aside, and the case will be referred back to a different RAD member for redetermination in accordance with the Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4537186` offsets `180-187`; context: [35] Lastly, I note that the RAD, whose leniency toward the respondent is based exclusively on its assessment of the manner in which he testified before the RPD, does not indicate whether this is a case where it was required to show deference to the RPD.
- Evidence: `evidence_fact` cue `testimony` at chunk `4537186` offsets `512-521`; context: Nevertheless, according to the teachings in Huruglica, in order to proceed with a non‑deferential analysis of a refugee claimant’s credibility or of the value of the claimant’s testimony, the RAD must be satisfied, on a case‑by‑case basis, that it is in an equally advantageous position as the RPD to do so.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4537186` offsets `335-347`; context: Nevertheless, according to the teachings in Huruglica, in order to proceed with a non‑deferential analysis of a refugee claimant’s credibility or of the value of the claimant’s testimony, the RAD must be satisfied, on a case‑by‑case basis, that it is in an equally advantageous position as the RPD to do so.
- Evidence: `reasoning_application` cue `therefore` at chunk `4537187` offsets `57-66`; context: [36] The Minister’s application for judicial review will therefore be allowed, the RAD’s decision will be set aside, and the case will be referred back to a different RAD member for redetermination in accordance with these Reasons.
- Evidence: `disposition` cue `allowed` at chunk `4537187` offsets `70-77`; context: [36] The Minister’s application for judicial review will therefore be allowed, the RAD’s decision will be set aside, and the case will be referred back to a different RAD member for redetermination in accordance with these Reasons.

#### 10669:2:subtheme:8 · paragraphs 39-39

- Raw key terms: `agree, appeal, case, certify, court, federal, need, opinion`
- Display key terms: `agree, case, certify, federal, need, opinion`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, case, certify, federal, need, opinion Evidence spans paragraphs 39-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4537188` offsets `73-81`; context: [37] The parties agree that there is no need, in this case, to certify a question for the Federal Court of Appeal.

#### Section text

[15] The Member concluded as follows:
[translation]

[46] Apart from the date of birth, all of the documents filed, some of which were issued by the Ethiopian ministry of education and bear seals that were not questioned, and the evidence as a whole make it possible to conclude on a balance of probabilities that the appellant is indeed who he claims to be, Beken Shitaye Gebrewold, an Ethiopian citizen.

[47] With respect to the date of birth, I find that this is a case where he can be given the benefit of the doubt. In listening to the recording of the hearing, I noted that the appellant answered the questions directly. Even though I was not present in the courtroom to observe him, I noted that his testimony was fluid, that he answered the questions in a straightforward manner and that he provided details. In terms of his identity, I find that there are no serious grounds to doubt his testimony before the RPD, nor before the Canadian authorities, even though some of his statements to the Norwegian and American authorities were false.

[16] Thus, the Member stated that she was of the view that the respondent had established his identity on a balance of probabilities. Consequently, she set aside the RPD’s decision but referred the case back to it so that it could decide on the merit of the refugee claim itself.

[17] The Minister is criticizing the Member for having conducted her analysis based on an unduly narrow reading of the relevant statutory provisions and of the RPD’s decision. He argues in this regard that the RAD could not reasonably question, when taking into account all of the evidence on record, the RPD’s finding that the respondent had failed to produce acceptable identity documents, and thus to prove his identity, not only because of the weak probative value of the documents he filed, but also, and especially, because of his behaviour towards the authorities, whether Canadian, Norwegian, American or Mexican, concerning the issue of his identity.

[18] He also criticizes the Member for having given the respondent the benefit of the doubt, without valid justification, regarding his date of birth. Lastly, he submits that the respondent’s failure to swear an affidavit in support of his position in this judicial review is fatal to his case.
III. Issue and standard of review

[19] The issue here is to determine whether the Member, in finding as she did, committed a reviewable error within the meaning of subsection 18.1(4) of the Federal Courts Act, RSC, 1985, c F‑7. It is not disputed that the standard of review that applies in this case is that of reasonableness (Huruglica, at paragraph 35; Paye v. Canada (Citizenship and Immigration), 2017 FC 685, at paragraph 3; Nazari v. Canada (Citizenship and Immigration), 2017 FC 561, at paragraph 12; Gu v. Canada (Citizenship and Immigration), 2017 FC 543, at paragraph 20; Singh v. Canada (Citizenship and Immigration), 2017 FC 719, at paragraph 9).

[20] I reiterate that the reasonableness of a decision “is concerned mostly with the existence of justification, transparency and intelligibility within the decision‑making process. But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at paragraph 47 [Dunsmuir]).
IV. Analysis

[21] As I recently reiterated, this Court has consistently held that identity is the cornerstone of the Canadian immigration regime (Bah v. Canada (Citizenship and Immigration), 2016 FC 373, at paragraph 7; see also Canada (Minister of Citizenship and Immigration) v. Singh, 2004 FC 1634, at paragraph 38; Canada (Citizenship and Immigration) v. X, 2010 FC 1095, 375 FTR 204, at paragraph 23). This is the case because a number of important factors in implementing this regime, such as admissibility in Canada, evaluating the need for protection, assessing the risk to public safety in Canada or the propensity to accept or reject the controls required by the Act, depend upon it.

[22] Moreover, pursuant to section 106 of the Act, the fact that a foreign national who arrives in Canada without acceptable identity documents can neither provide an explanation nor prove having taken the required steps to obtain the documents can affect the RPD’s assessment of the claimant’s credibility.

[23] The date of birth, like first and last names, is clearly an essential component of identity. Yet, in this case, even if we accept that the RAD could reasonably find that the respondent’s real first and last names are indeed, on a balance of probabilities, Beken Shitaye Gebrewold, the date of birth, as the RAD recognized by noting the inconsistencies and contradictions identified by the RPD, remains problematic.

[24] I therefore consider the issue to be whether it was reasonable for the RAD, considering all the circumstances of this case, to disregard this problem by giving the respondent the benefit of the doubt. I do not believe so.

[25] In my view, the RAD’s decision contains flaws in this regard in terms of internal consistency and intelligibility. I reiterate that the RAD’s role is not to carry out a de novo examination of the refugee claim that the RPD had to address. In other words, it is insufficient for the RAD to ask whether it would have reached a different conclusion had it been in the RPD’s position, without regard for any aspect of the RPD’s decision (Huruglica, at paragraph 79). The RAD is an appeal body. While it is true that it must carry out its own analysis of the file in applying the correctness standard of review, except with regard to assessing credibility or the value of oral testimonies, where the RAD, when the RPD truly enjoys a meaningful advantage over it, must occasionally show deference (Huruglica, at paragraph 70), its role is to “catch all mistakes made by the RPD, be it on the law or the facts” (Huruglica, at paragraph 98).

[26] However, for all practical purposes, the RAD conceded that the respondent’s evidence contained inconsistencies and contradictions with respect to his date of birth (RAD Decision, at paragraphs 41 and 46). I infer from this that it was satisfied that the RPD had not erred in finding as it did regarding this issue. In this context, it was insufficient, in my view, for the RAD to give the respondent the benefit of the doubt without stating how the RPD erred in not doing the same. The RAD decision reads as if, on this issue, it conducted a de novo proceeding and, therefore, without regard to the RPD decision on this issue, based its findings on the recording of the hearing before the RPD. However, as noted above, it was not permitted to do so.

[27] The RAD decision is also problematic if one assumes that the RAD was implicitly criticizing the RPD for not having given the respondent the benefit of the doubt. The RAD’s only justification was to note that the respondent [translation] “answered the questions directly”, “in a straightforward manner”, that his testimony [translation] “was fluid” and that he [translation] “provided details”. Still, this does not explain how the fact that the respondent testified in a direct and fluid manner resolves the inconsistencies and contradictions in his testimony and in the evidence in general and argues, in that context, in favour of giving the respondent the benefit of the doubt.

[28] As the Court noted in Noga v. Canada (Minister of Citizenship and Immigration), 2003 FCT 454 [Noga], the benefit of the doubt principle “applies in a limited number of circumstances”. Benefit of the doubt should be given only “when all available evidence has been obtained and checked and when the examiner is satisfied as to the applicant’s general credibility”, which assumes that the applicant’s statements are “coherent and plausible” (Noga, at paragraphs 10 to 12).

[29] Yet, this was not demonstrated by the RAD, which was satisfied with a general observation about the manner in which the respondent testified before the RPD. Furthermore, the RAD is silent with regard to the respondent’s statements about the use of a calendar that differs from the Gregorian calendar in Ethiopia and about the date of December 29, 1976, which he alleges to have always considered to be his date of birth, statements that, for what I consider to be reasonable grounds, the RPD had not found to be plausible and coherent. Moreover, I note in the record that, according to the checks conducted by the CBSA, the Ethiopian authorities have been using Gregorian calendar dates on passports for decades.

[30] The RAD is also silent on the efforts the respondent made to obtain documents that would prove his identity, including his date of birth. In particular, the RPD stated that it was unsatisfied with the respondent’s efforts to obtain at the very least a copy of the passport seized by the Norwegian authorities in 2009, which could enlighten the Canadian authorities as to the respondent’s date of birth and identity in general. The RAD does not explain how this finding constituted an error, nor how the respondent could nonetheless be given the benefit of the doubt in such a context.

[31] I also note in this regard that, on September 29, 2015, the respondent allegedly told the CBSA authorities that the counsel representing him in his dealings with the American authorities was in possession of both the travel document the Norwegian authorities had given to him and his Ethiopian passport. As the Minister notes, there is no indication in the file that the respondent took the required measures to obtain those documents from that individual.

[32] I find the RAD’s decision to be all the more unintelligible concerning the issue of the date of birth since the refugee claimant in this case, throughout his migratory path, obtained or attempted to obtain the right to enter a foreign country by misrepresenting his identity and destroying the documents that could have adversely affected him in this regard. It seems to me that, with such a track record, and considering the number of birth dates on record, the inconsistencies and contradictions in the evidence presented by the respondent to try to explain the situation and the findings about the respondent’s lack of effort to produce satisfactory evidence in this regard, the RAD should have explained, other than by giving its general impressions on the manner in which the respondent testified before the RPD, how the benefit of the doubt principle could apply in the circumstances.

[33] This is even more troubling given that the RAD, as I mentioned previously, seemed to concede that the respondent’s evidence regarding his date of birth contained contradictions and inconsistencies. Nevertheless, two essential considerations in the application of the benefit of the doubt principle are that the refugee claimant’s statements be “coherent and plausible” (Noga, at paragraphs 10 to 12).

[34] The RPD found that the confusion surrounding the respondent’s date of birth was such that it could not [translation] “conclude that the [respondent] had been able to persuade [it] as to what his date of birth could be, an important element in establishing any person’s identity.” In my opinion, that finding alone required that the RAD provide a robust demonstration of the application of the benefit of the doubt principle. That demonstration was not made.

[35] Lastly, I note that the RAD, whose leniency toward the respondent is based exclusively on its assessment of the manner in which he testified before the RPD, does not indicate whether this is a case where it was required to show deference to the RPD. The RAD’s decision does not address this issue other than in theoretical terms. Nevertheless, according to the teachings in Huruglica, in order to proceed with a non‑deferential analysis of a refugee claimant’s credibility or of the value of the claimant’s testimony, the RAD must be satisfied, on a case‑by‑case basis, that it is in an equally advantageous position as the RPD to do so. However, such an analysis does not appear anywhere in the RAD’s decision in this case, which affects the transparency and intelligibility of the decision‑making process.

[36] The Minister’s application for judicial review will therefore be allowed, the RAD’s decision will be set aside, and the case will be referred back to a different RAD member for redetermination in accordance with these Reasons.

[37] The parties agree that there is no need, in this case, to certify a question for the Federal Court of Appeal. I agree with that opinion.


## 10669:3 · paragraphs 40-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d4d9776c3ce98ad1777be58cf49ff9cb1fec43e1ff4543e5e5f4f748ab71ce06`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10669:3:subtheme:1 · paragraphs 40-41

- Raw key terms: `allowed, appeal, application, aside, back, beken, board, case`
- Display key terms: `allowed, aside, back, beken, case`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allowed, aside, back, beken, case No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
The application for judicial review is allowed;
The decision by the Immigration and Refugee Board’s Refugee Appeal Division dated September 5, 2017, is set aside, and the case is referred back to a different Refugee Appeal Division member for redetermination;
No question is certified.
“René LeBlanc”
Judge
Certified true translation
This 12th day of November 2019
Lionbridge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM‑4058‑17
STYLE OF CAUSE:
MINISTER OF PUBLIC SAFETY AND EMERGENCY PREPAREDNESS v. BEKEN SHITAYE GEBREWOLD
PLACE OF HEARING:
Montreal, Quebec
DATE OF HEARING:
March 26, 2018


## 10669:4 · paragraphs 42-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ceb6c7dc37b64f1c4548332884d5d29bd3b7ed6c39c12b28ac6172407633b5f0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10669:4:subtheme:1 · paragraphs 42-42

- Raw key terms: `appearances, applicant, april, attorney, blanchard, canada, counsel, dated`
- Display key terms: `april, blanchard, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, blanchard, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 42-42. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
LEBLANC J.
DATED:
April 6, 2018
APPEARANCES:
Mario Blanchard
For the Applicant
Stéphanie Valois
For the Respondent
SOLICITORS OF RECORD:
Nathalie G. Drouin
Deputy Attorney General of Canada
Ottawa, Ontario
For the Applicant
Stéphanie Valois
Counsel
Montreal, Quebec
For the Respondent
