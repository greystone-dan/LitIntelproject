# Discussion Units: case 20182

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **3**
- Paragraph source hashes: **50**
- Sub-themes: **9**

## 20182:1 · paragraphs 0-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `810e4fc0d006fc9897ba3ec330a07bf73be604cb188f533b672b287d1f425d23`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20182:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `applicant, husband, macedo, principal, daughters, decision, late, police`
- Display key terms: `husband, macedo, principal, daughters, late, police`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: husband, macedo, principal, daughters, late, police Position/evidence statements: [3] The principal applicant claims that she lived under the control of a violent and controlling husband, Pablo Macedo Muñoz, from 1989 to June 2007. | · The notary gave her some advice, including that she should go to Canada and claim refugee protection. Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S. | [3] The principal applicant claims that she lived under the control of a violent and controlling husband, Pablo Macedo Muñoz, from 1989 to June 2007. Application context: · There was no autopsy because of the pressure exerted by José Victor Macedo Muñoz. | [9] Thus, the principal applicant feared that her daughters could be kidnapped or killed because of the allocation of land owned by her late husband’s family and because José Victor Macedo Muñoz was the main suspect in h Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4953636` offsets `311-326`; context: In that decision, the panel determined that the applicants were neither Convention refugees nor persons in need of protection under sections 96 and 97 of the Act.
- Evidence: `governing_rule` cue `under` at chunk `4953636` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claims` at chunk `4953638` offsets `28-34`; context: [3] The principal applicant claims that she lived under the control of a violent and controlling husband, Pablo Macedo Muñoz, from 1989 to June 2007.
- Evidence: `governing_rule` cue `under` at chunk `4953638` offsets `50-55`; context: [3] The principal applicant claims that she lived under the control of a violent and controlling husband, Pablo Macedo Muñoz, from 1989 to June 2007.
- Evidence: `party_position` cue `claim` at chunk `4953643` offsets `1237-1242`; context: · The notary gave her some advice, including that she should go to Canada and claim refugee protection.
- Evidence: `reasoning_application` cue `because` at chunk `4953643` offsets `886-893`; context: · There was no autopsy because of the pressure exerted by José Victor Macedo Muñoz.
- Evidence: `reasoning_application` cue `because` at chunk `4953644` offsets `89-96`; context: [9] Thus, the principal applicant feared that her daughters could be kidnapped or killed because of the allocation of land owned by her late husband’s family and because José Victor Macedo Muñoz was the main suspect in his death.

#### 20182:1:subtheme:2 · paragraphs 11-12

- Raw key terms: `applicants, decision, panel, story, added, adequate, applicant, authorities`
- Display key terms: `story, added, adequate, authorities`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: story, added, adequate, authorities Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4953646` offsets `65-70`; context: [11] The panel found that the applicants’ fear related to a land issue was not credible.
- Evidence: `evidence_fact` cue `found that` at chunk `4953646` offsets `15-25`; context: [11] The panel found that the applicants’ fear related to a land issue was not credible.
- Evidence: `evidence_fact` cue `determined that` at chunk `4953647` offsets `45-60`; context: [12] As for the rest of the story, the panel determined that the applicants made no effort to seek protection from the authorities and failed to demonstrate clearly and convincingly that the Mexican authorities were unable to provide adequate protection (Panel’s Decision, paragraphs 26 and 45).

#### 20182:1:subtheme:3 · paragraphs 13-23

- Raw key terms: `panel, applicant, principal, victor, credible, macedo, mentioned, applicants`
- Display key terms: `principal, victor, credible, macedo, mentioned`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: principal, victor, credible, macedo, mentioned Position/evidence statements: The fact that the applicant waited almost two and a half years to submit these new grounds did not strengthen her credibility at all. Rule/authority context: [20] In the panel’s view, the explanations provided by the principal applicant as to why she had not filed a complaint against her ex-brother-in-law, Jose Victor, did not constitute clear and convincing evidence of the l Application context: [13] First, the panel determined that the applicants’ story was not credible primarily because of the disparity between the story contained in the Personal Information Form (PIF), the interview and the amendments to the  | [14] The panel did not find it credible that the principal applicant had not mentioned in her PIF that she feared José Victor Macedo Muñoz because of an issue related to the possession of family land. Operative outcome context: [23] Consequently, the panel concluded that the applicants’ application should be dismissed. Evidence spans paragraphs 13-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `4953648` offsets `252-260`; context: [13] First, the panel determined that the applicants’ story was not credible primarily because of the disparity between the story contained in the Personal Information Form (PIF), the interview and the amendments to the PIF (Exhibit P-10, Amendment to Question 31 of the PIF, filed with the Board on May 4, 2010, pages 150‑157 of the Board’s record).
- Evidence: `evidence_fact` cue `determined that` at chunk `4953648` offsets `22-37`; context: [13] First, the panel determined that the applicants’ story was not credible primarily because of the disparity between the story contained in the Personal Information Form (PIF), the interview and the amendments to the PIF (Exhibit P-10, Amendment to Question 31 of the PIF, filed with the Board on May 4, 2010, pages 150‑157 of the Board’s record).
- Evidence: `reasoning_application` cue `because` at chunk `4953648` offsets `87-94`; context: [13] First, the panel determined that the applicants’ story was not credible primarily because of the disparity between the story contained in the Personal Information Form (PIF), the interview and the amendments to the PIF (Exhibit P-10, Amendment to Question 31 of the PIF, filed with the Board on May 4, 2010, pages 150‑157 of the Board’s record).
- Evidence: `issue` cue `issue` at chunk `4953649` offsets `153-158`; context: [14] The panel did not find it credible that the principal applicant had not mentioned in her PIF that she feared José Victor Macedo Muñoz because of an issue related to the possession of family land.
- Evidence: `reasoning_application` cue `because` at chunk `4953649` offsets `139-146`; context: [14] The panel did not find it credible that the principal applicant had not mentioned in her PIF that she feared José Victor Macedo Muñoz because of an issue related to the possession of family land.
- Evidence: `reasoning_application` cue `because` at chunk `4953650` offsets `357-364`; context: ”, the applicant replied that she was afraid of the sons of Jorge Salinas, Luis Chachahuate, and the police because her husband had had problems with those people.
- Evidence: `party_position` cue `submit` at chunk `4953651` offsets `503-509`; context: The fact that the applicant waited almost two and a half years to submit these new grounds did not strengthen her credibility at all.
- Evidence: `evidence_fact` cue `determined that` at chunk `4953651` offsets `264-279`; context: The panel determined that if the principal applicant really feared José Victor Macedo Muñoz, she would have mentioned it to the immigration officer in order to substantiate her fear.
- Evidence: `evidence_fact` cue `Record` at chunk `4953652` offsets `317-323`; context: Marta Valenzuela, dated May 5, 2010, at pages 187-195 of the Tribunal Record).
- Evidence: `evidence_fact` cue `evidence` at chunk `4953655` offsets `203-211`; context: [20] In the panel’s view, the explanations provided by the principal applicant as to why she had not filed a complaint against her ex-brother-in-law, Jose Victor, did not constitute clear and convincing evidence of the lack of state protection or rebut the presumption established in the jurisprudence that states are capable of protecting their citizens.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4953655` offsets `288-301`; context: [20] In the panel’s view, the explanations provided by the principal applicant as to why she had not filed a complaint against her ex-brother-in-law, Jose Victor, did not constitute clear and convincing evidence of the lack of state protection or rebut the presumption established in the jurisprudence that states are capable of protecting their citizens.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953656` offsets `69-77`; context: [21] The panel subsequently completed an analysis of the documentary evidence on Mexico and mentioned the National Documentation Package on Mexico (see IRB, Ottawa, National Documentation Package on Mexico, October 2, 2009).
- Evidence: `evidence_fact` cue `evidence` at chunk `4953657` offsets `47-55`; context: [22] The panel also reviewed the contradictory evidence and stated that the national human rights commission (CNDH) believes that some members of the local and state police forces are involved in kidnappings, extortion and collaboration with organized crime.
- Evidence: `counterargument_limitation` cue `However` at chunk `4953657` offsets `259-266`; context: However, the panel also specifically stated that the Mexican government has implemented extensive human rights training programs for the police forces in general.
- Evidence: `disposition` cue `dismissed` at chunk `4953658` offsets `82-91`; context: [23] Consequently, the panel concluded that the applicants’ application should be dismissed.

#### 20182:1:subtheme:4 · paragraphs 24-25

- Raw key terms: `issue, protection, accepted, adequate, against, alors, appartenance, application`
- Display key terms: `protection, accepted, adequate, against, alors, appartenance`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: protection, accepted, adequate, against, alors, appartenance Rule/authority context: Standard of review Application context: [24] The following provisions of the Immigration and Refugee Protection Act apply to this proceeding: Convention refugee 96. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4953659` offsets `3747-3752`; context: Issue
- Evidence: `reasoning_application` cue `apply` at chunk `4953659` offsets `76-81`; context: [24] The following provisions of the Immigration and Refugee Protection Act apply to this proceeding:
Convention refugee
96.
- Evidence: `issue` cue `issue` at chunk `4953660` offsets `54-59`; context: [25] On this application for judicial review the only issue is as follows: Are the panel’s findings on state protection and the lack of credibility reasonable?
- Evidence: `governing_rule` cue `Standard of review` at chunk `4953660` offsets `160-178`; context: Standard of review

#### 20182:1:subtheme:5 · paragraphs 26-37

- Raw key terms: `panel, canada, immigration, court, credibility, evidence, minister, applicant`
- Display key terms: `credibility`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility Position/evidence statements: [29] The principal applicant maintains that she did not mention the contents of Exhibit P-10 submitted on May 4, 2010, at her interview with the officer or in her original PIF because of her fear of returning to Mexico,  | [31] This Court has confirmed on a number of occasions that all the important facts of a claim must appear in the PIF and that failing to mention them could affect the credibility of part or all of the testimony. Application context: [29] The principal applicant maintains that she did not mention the contents of Exhibit P-10 submitted on May 4, 2010, at her interview with the officer or in her original PIF because of her fear of returning to Mexico,  | [35] The Court concurs with counsel for the respondent because it is for the panel to assess the probative value of the psychological report in relation to the other evidence, especially since the psychological report re Evidence spans paragraphs 26-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4953661` offsets `212-218`; context: questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness .
- Evidence: `party_position` cue `submitted` at chunk `4953664` offsets `93-102`; context: [29] The principal applicant maintains that she did not mention the contents of Exhibit P-10 submitted on May 4, 2010, at her interview with the officer or in her original PIF because of her fear of returning to Mexico, i.
- Evidence: `reasoning_application` cue `because` at chunk `4953664` offsets `176-183`; context: [29] The principal applicant maintains that she did not mention the contents of Exhibit P-10 submitted on May 4, 2010, at her interview with the officer or in her original PIF because of her fear of returning to Mexico, i.
- Evidence: `party_position` cue `claim` at chunk `4953666` offsets `89-94`; context: [31] This Court has confirmed on a number of occasions that all the important facts of a claim must appear in the PIF and that failing to mention them could affect the credibility of part or all of the testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4953666` offsets `202-211`; context: [31] This Court has confirmed on a number of occasions that all the important facts of a claim must appear in the PIF and that failing to mention them could affect the credibility of part or all of the testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4953667` offsets `256-265`; context: [32] It was open to the panel to gauge the principal applicant’s credibility and to draw negative inferences about the disparities between her statements in the original PIF, in the interview notes, in the amended narrative of the PIF and in the viva voce testimony, for which the principal applicant provided no satisfactory, plausible or credible explanation in the circumstances (He v.
- Evidence: `party_position` cue `submits` at chunk `4953669` offsets `20-27`; context: [34] The respondent submits that the panel was aware of the contents of the psychological report and assessed this evidence in the context of the case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953669` offsets `115-123`; context: [34] The respondent submits that the panel was aware of the contents of the psychological report and assessed this evidence in the context of the case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953670` offsets `166-174`; context: [35] The Court concurs with counsel for the respondent because it is for the panel to assess the probative value of the psychological report in relation to the other evidence, especially since the psychological report refers to Esteban Zeferino’s current state of mind and makes no findings as to her state of mind in 2007.
- Evidence: `reasoning_application` cue `because` at chunk `4953670` offsets `55-62`; context: [35] The Court concurs with counsel for the respondent because it is for the panel to assess the probative value of the psychological report in relation to the other evidence, especially since the psychological report refers to Esteban Zeferino’s current state of mind and makes no findings as to her state of mind in 2007.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953671` offsets `240-248`; context: 399, at paragraph 38, defines the burden of proof, the standard of proof and the quality of the evidence of an allegation that state protection is inadequate or non‑existent for one of its citizens:
- Evidence: `evidence_fact` cue `evidence` at chunk `4953672` offsets `123-131`; context: [38] A refugee who claims that the state protection is inadequate or non-existent bears the evidentiary burden of adducing evidence to that effect and the legal burden of persuading the trier of fact that his or her claim in this respect is founded.

#### 20182:1:subtheme:6 · paragraphs 38-45

- Raw key terms: `protection, mexico, applicants, canada, citizenship, immigration, minister, seek`
- Display key terms: `protection, mexico, seek`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: protection, mexico, seek Rule/authority context: [37] The jurisprudence has repeatedly recognized that where the state in question is a democratic state, like Mexico, the applicants’ obligation to seek state protection increases. Application context: [38] The applicants maintain that they did not request state protection because they did not have confidence in the protection that would be offered. Evidence spans paragraphs 38-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4953673` offsets `73-81`; context: [37] The jurisprudence has repeatedly recognized that where the state in question is a democratic state, like Mexico, the applicants’ obligation to seek state protection increases.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4953673` offsets `9-22`; context: [37] The jurisprudence has repeatedly recognized that where the state in question is a democratic state, like Mexico, the applicants’ obligation to seek state protection increases.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953674` offsets `187-195`; context: There is a great deal of documentary evidence about police corruption in Mexico.
- Evidence: `reasoning_application` cue `because` at chunk `4953674` offsets `72-79`; context: [38] The applicants maintain that they did not request state protection because they did not have confidence in the protection that would be offered.
- Evidence: `counterargument_limitation` cue `However` at chunk `4953674` offsets `231-238`; context: However, the Court notes that the same evidence shows that there were other courses of action available to them.

#### 20182:1:subtheme:7 · paragraphs 46-46

- Raw key terms: `application, case, certify, court, dismissed, evidence, facts, given`
- Display key terms: `case, certify, dismissed, facts, given`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: case, certify, dismissed, facts, given Operative outcome context: For these reasons, the application for judicial review will be dismissed. Evidence spans paragraphs 46-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4953681` offsets `206-214`; context: There is no question to certify.
- Evidence: `evidence_fact` cue `evidence` at chunk `4953681` offsets `42-50`; context: [43] Given the facts of this case and the evidence in the record, there is no justification for the Court to intervene.
- Evidence: `disposition` cue `dismissed` at chunk `4953681` offsets `183-192`; context: For these reasons, the application for judicial review will be dismissed.

#### Section text

Zeferino v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-04-13
Neutral citation
2011 FC 456
File numbers
IMM-4058-10
Decision Content
Federal Court
Cour fédérale
Date: 20110413
Docket: IMM-4058-10
Citation: 2011 FC 456
[UNREVISED CERTIFIED ENGLISH TRANSLATION]
Ottawa, Ontario, April 13, 2011
PRESENT: The Honourable Mr. Justice Boivin
BETWEEN:
MARIA LUISA ESTEBAN ZEFERINO
MASSIEL MACEDO ESTEBAN
DIANA BERTHA MACEDO ESTEBAN
Applicants
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (hereinafter the Act), for judicial review of a decision dated June 17, 2010, by the Immigration and Refugee Board, Refugee Protection Division (hereinafter the panel). In that decision, the panel determined that the applicants were neither Convention refugees nor persons in need of protection under sections 96 and 97 of the Act.
Facts

[2] The principal applicant, Maria Luisa Esteban Zeferino, and her two daughters, Massiel Macedo Esteban and Diana Bertha Macedo Esteban, are Mexican and arrived in Canada in August 2007.

[3] The principal applicant claims that she lived under the control of a violent and controlling husband, Pablo Macedo Muñoz, from 1989 to June 2007. It is alleged that on June 27, 2007, the applicant’s husband was found lying near his car after he had gone to work. He had been attacked and died in hospital from injuries to his leg that had been inflicted during the attack. The police suspected an employee and the victim’s brother, José Victor Macedo Muñoz, of committing the crime.

[4] Following this event, José Victor Macedo Muñoz told the applicant to report to the police that her husband had injured himself and that he had no enemies. Mr. Muñoz allegedly paid the doctor to proceed with the burial as quickly as possible, but the doctor confirmed to the applicant that he had already performed the autopsy and that the victim had died from an attack with a machete.

[5] The police officers who were present took the applicant’s statement but did not believe it. The police continued to suspect the employee and the victim’s brother and asked the applicant to make another statement if she obtained new information or developed suspicions about someone. If that happened, the police said that they would exhume the body of her late husband.

[6] In the past, the principal applicant’s late husband had received threats from three different sources while he was alive.

[7] Since her husband’s death, the applicant has been afraid that strangers would take reprisals against her daughters and would like her daughters to live in an environment free of violence.

[8] On March 5, 2010, almost two and a half years after the events, the principal applicant provided new allegations that added an agent of persecution and a basis for her fear. Essentially, the principal applicant added the following:
· The members of her ex‑spouse’s family are violent people who do not get along with each other or with their neighbours. José Victor Macedo Muñoz is a rapist.
· The family conflicts concern the management of the land owned by the family. The applicant’s late husband was the administrator of his family’s property.
· On his death bed, Pablo Macedo Muñoz asked that his daughters be protected from his brother.
· When the victim’s brother told the applicant to tell the police that the victim had no enemies, he also threatened her.
· The police did not believe the applicant and told her that all of this was very suspicious.
· There was no autopsy because of the pressure exerted by José Victor Macedo Muñoz.
· He took the principal applicant to a notary to have her sign a document so that he could represent her in everything.
· This document indicates that the principal applicant can be deprived of all her property.
· The notary gave her some advice, including that she should go to Canada and claim refugee protection.
· Her ex-husband’s family wanted steps to be taken so that the principal applicant’s ex-brother‑in‑law, José Victor Macedo Muñoz, could obtain parental authority over her daughters.

[9] Thus, the principal applicant feared that her daughters could be kidnapped or killed because of the allocation of land owned by her late husband’s family and because José Victor Macedo Muñoz was the main suspect in his death.
Impugned decision

[10] In making its decision, the panel took into consideration the Chairperson’s Guideline entitled Women Refugee Claimants Fearing Gender‑Related Persecution, issued by the Immigration and Refugee Board (IRB), March 1993, updated in November 1996.

[11] The panel found that the applicants’ fear related to a land issue was not credible. In the panel’s view, that part of the testimony was added to embellish the principal applicant’s story (Panel’s Decision, at paragraph 24).

[12] As for the rest of the story, the panel determined that the applicants made no effort to seek protection from the authorities and failed to demonstrate clearly and convincingly that the Mexican authorities were unable to provide adequate protection (Panel’s Decision, paragraphs 26 and 45).

[13] First, the panel determined that the applicants’ story was not credible primarily because of the disparity between the story contained in the Personal Information Form (PIF), the interview and the amendments to the PIF (Exhibit P-10, Amendment to Question 31 of the PIF, filed with the Board on May 4, 2010, pages 150‑157 of the Board’s record).

[14] The panel did not find it credible that the principal applicant had not mentioned in her PIF that she feared José Victor Macedo Muñoz because of an issue related to the possession of family land. It also noted that if the principal applicant had fled Mexico with her daughters to escape from José Victor Macedo Muñoz she would have stated that in her PIF. Instead, she said that she feared strangers.

[15] In addition, the panel did not find it credible that the principal applicant had not mentioned her fear of José Victor Macedo Muñoz when she was interviewed 17 days after her admission to Canada. When asked [translation] “Who are you afraid of?”, the applicant replied that she was afraid of the sons of Jorge Salinas, Luis Chachahuate, and the police because her husband had had problems with those people. The applicant did not say at the interview that she feared José Victor Macedo Muñoz because of problems related to the possession of family land.

[16] The applicant testified that she was afraid the Canadian authorities would reveal that she was afraid of José Victor Macedo Muñoz and that this fear was the reason for her silence. The panel did not accept this explanation, finding it not credible. The panel determined that if the principal applicant really feared José Victor Macedo Muñoz, she would have mentioned it to the immigration officer in order to substantiate her fear. The fact that the applicant waited almost two and a half years to submit these new grounds did not strengthen her credibility at all.

[17] Given the negative credibility findings, the panel gave no probative value to the psychological report filed as Exhibit P‑11 on the day of the hearing before the panel (Exhibit P-11, Psychological Report: Maria Luisa Esteban Zeferino, by Dr. Marta Valenzuela, dated May 5, 2010, at pages 187-195 of the Tribunal Record).

[18] Moreover, the panel concluded that the applicants had not satisfied their obligation to seek protection from the Mexican authorities.

[19] Indeed, the panel noted that the police strongly suspected that José Victor Macedo Muñoz had murdered Pablo Macedo Muñoz. The police asked the principal applicant to file a subsequent written statement if she developed new suspicions. When questioned as to why she had not sought police protection, the principal applicant replied that the Mexican police force is corrupt. She based her statement on events dating back to 1994 when her husband and José Victor Macedo Muñoz allegedly killed an individual. They subsequently gave the police money and were not bothered after that.

[20] In the panel’s view, the explanations provided by the principal applicant as to why she had not filed a complaint against her ex-brother-in-law, Jose Victor, did not constitute clear and convincing evidence of the lack of state protection or rebut the presumption established in the jurisprudence that states are capable of protecting their citizens.

[21] The panel subsequently completed an analysis of the documentary evidence on Mexico and mentioned the National Documentation Package on Mexico (see IRB, Ottawa, National Documentation Package on Mexico, October 2, 2009). The panel concluded that Mexico is a democracy whose government generally respects the rights of its citizens.

[22] The panel also reviewed the contradictory evidence and stated that the national human rights commission (CNDH) believes that some members of the local and state police forces are involved in kidnappings, extortion and collaboration with organized crime. However, the panel also specifically stated that the Mexican government has implemented extensive human rights training programs for the police forces in general. The panel also reviewed the 2008 court reforms and the recent legislation that requires police personnel to meet a superior level of training on human rights and other procedures.

[23] Consequently, the panel concluded that the applicants’ application should be dismissed.
Relevant statutory provisions

[24] The following provisions of the Immigration and Refugee Protection Act apply to this proceeding:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques:
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
Person in need of protection
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée:
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant:
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Personne à protéger
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.
Issue

[25] On this application for judicial review the only issue is as follows: Are the panel’s findings on state protection and the lack of credibility reasonable?
Standard of review

[26] The Supreme Court of Canada in Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] 1 S.C.R. 190, at paragraph 51, recognized that “... questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness ...”.

[27] As to the questions involving the assessment of credibility, the Court will only intervene if the panel based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it (Aguebor v. Canada (Minister of Employment and Immigration) (F.C.A.), (1993), 160 N.R. 315, 42 A.C.W.S. (3d) 886).

[28] The panel’s findings on state protection are reviewable against the standard of reasonableness (see Huerta v. Canada (Minister of Citizenship and Immigration), 2008 FC 586, [2008] F.C.J. No. 737, at paragraph 14).
Analysis

[29] The principal applicant maintains that she did not mention the contents of Exhibit P-10 submitted on May 4, 2010, at her interview with the officer or in her original PIF because of her fear of returning to Mexico, i.e., her fear that she and her two daughters would be killed or persecuted by the primary agent of persecution. The applicant submits that the panel should have assessed her explanations objectively, taking into consideration the battered woman syndrome and Dr. Marta Valenzuela’s psychological report.

[30] The respondent maintains that, as the panel noted in its reasons (Panel’s Decision, at paragraphs 16, 18 and 20), the agent of persecution in the person of José Victor Macedo Muñoz and the new basis for fear had not been raised before, at the point of entry into Canada when the applicants asked for asylum, at the interview in this regard with an immigration officer 17 days after their arrival in the country or in their original PIF completed and signed in October 2007 with the assistance of their counsel at the time.

[31] This Court has confirmed on a number of occasions that all the important facts of a claim must appear in the PIF and that failing to mention them could affect the credibility of part or all of the testimony. Furthermore, the RPD is entitled to review the contents of the PIF before and after its amendment and may draw negative inferences about credibility if matters it considers important were added to the PIF by an amendment later (Taheri v. Canada (Minister of Citizenship and Immigration), 2001 FCT 886, [2001] F.C.J. No. 1252, at paragraphs 4 and 6; Grinevich v. Canada (Minister of Citizenship and Immigration), (1997) 70 A.C.W.S. (3d) 1059, [1997] F.C.J. No. 444).

[32] It was open to the panel to gauge the principal applicant’s credibility and to draw negative inferences about the disparities between her statements in the original PIF, in the interview notes, in the amended narrative of the PIF and in the viva voce testimony, for which the principal applicant provided no satisfactory, plausible or credible explanation in the circumstances (He v. Canada (Minister of Employment and Immigration), (1994), 49 A.C.W.S. (3d) 562, [1994] F.C.J. No. 1107). In this case, and the Court agrees with counsel for the respondent, the evidence shows that the applicants’ story and narrative changed over the last two years.

[33] As for the psychological report, the applicant maintains that the panel should first have read Dr. Valenzuela’s psychological report and taken it into account in assessing the credibility of the refugee claim, even in assessing the relevance of omissions in the interview notes and the first PIF before it was amended by Exhibit P-10. The applicants submit that the psychological report refers to the principal applicant’s vulnerability, which could have affected her testimonial capacity.

[34] The respondent submits that the panel was aware of the contents of the psychological report and assessed this evidence in the context of the case. The respondent notes that the panel’s negative credibility finding was not based on deficiencies in the applicant’s testimony at the hearing before the Board. The deficiencies did not involve memory lapses or hesitations in answering questions, errors in dates or other difficulties referred to in the psychological report.

[35] The Court concurs with counsel for the respondent because it is for the panel to assess the probative value of the psychological report in relation to the other evidence, especially since the psychological report refers to Esteban Zeferino’s current state of mind and makes no findings as to her state of mind in 2007.

[36] In terms of state protection, the decision in Carrillo v. Canada (Minister of Citizenship and Immigration), 2008 FCA 94, [2008] F.C.J. No. 399, at paragraph 38, defines the burden of proof, the standard of proof and the quality of the evidence of an allegation that state protection is inadequate or non‑existent for one of its citizens:

[38] A refugee who claims that the state protection is inadequate or non-existent bears the evidentiary burden of adducing evidence to that effect and the legal burden of persuading the trier of fact that his or her claim in this respect is founded. The standard of proof applicable is the balance of probabilities and there is no requirement of a higher degree of probability than what that standard usually requires. As for the quality of the evidence required to rebut the presumption of state protection, the presumption is rebutted by clear and convincing evidence that the state protection is inadequate or non-existent.

[37] The jurisprudence has repeatedly recognized that where the state in question is a democratic state, like Mexico, the applicants’ obligation to seek state protection increases. They must establish that they tried to exhaust all the courses of action open to them to obtain the required protection (see Kadenko v. Canada (Minister of Citizenship and Immigration), [1996] F.C.J. No. 1376, 68 A.C.W.S. (3d) 334).

[38] The applicants maintain that they did not request state protection because they did not have confidence in the protection that would be offered. There is a great deal of documentary evidence about police corruption in Mexico. However, the Court notes that the same evidence shows that there were other courses of action available to them.

[39] In particular, it was recognized in Sosa v. Canada (Minister of Citizenship and Immigration), 200

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 20182:2 · paragraphs 47-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b4537d31ce8a60a8b48ddac532caf151546f1aef70c2c6f98887ffd8b0a7ddfc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20182:2:subtheme:1 · paragraphs 47-48

- Raw key terms: `application, boivin, cause, certified, court, date, dismissed, docket`
- Display key terms: `boivin, certified, date, dismissed`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: boivin, certified, date, dismissed No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT RULES that
1. This application for judicial review is dismissed.
2. No question will be certified.
“Richard Boivin”
Judge
Certified true translation
Mary Jo Egan, LLB
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4058-10
STYLE OF CAUSE: MARIA LUISA ESTEBAN ZEFERINO et al
v. MCI
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: March 22, 2011
REASONS FOR 

## 20182:3 · paragraphs 49-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2e3ff45be0d07e7cd3500f6f2fa863dcc3de5e4c9dbd58ac3832ac9aaffcf94e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20182:3:subtheme:1 · paragraphs 49-49

- Raw key terms: `alain, appearances, applicants, april, attorney, bernard, boivin, canada`
- Display key terms: `alain, april, bernard, boivin`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alain, april, bernard, boivin No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: BOIVIN J.
DATED: April 13, 2011
APPEARANCES:
Alain Joffe
FOR THE APPLICANTS
Christine Bernard
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Law Office
Montréal, Quebec
FOR THE APPLICANTS
Myles J. Kirvan
Deputy Attorney General of Canada
FOR THE RESPONDENT
