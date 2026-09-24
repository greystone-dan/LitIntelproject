# Discussion Units: case 7522

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **96**
- Continuity pairs: **95**
- Discussion Units: **4**
- Paragraph source hashes: **96**
- Sub-themes: **26**

## 7522:1 · paragraphs 0-47

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d6a815ed74cd3cf4d40ff643aa9f492d325e2ae3290ffa891688248d4f18e436`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7522:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `immigration, respondents, decision, appeal, because, canada, citizenship, dated`
- Display key terms: `because, dated`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: because, dated Position/evidence statements: The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are force Rule/authority context: ” Consequently, the RAD set aside the RPD’s determination and substituted its own pursuant to paragraph 111(1)(b) of the Immigration and Refugee Protection Act, SC 2001, c 27 (“IRPA”). Application context: In a decision dated August 22, 2018, the Refugee Protection Division (“RPD”) of the Immigration and Refugee Board (“IRB”) rejected the claims because it was not satisfied that the respondents had established their person | The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are force Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4399945` offsets `363-370`; context: In a decision dated August 22, 2018, the Refugee Protection Division (“RPD”) of the Immigration and Refugee Board (“IRB”) rejected the claims because it was not satisfied that the respondents had established their personal identities as citizens of Eritrea.
- Evidence: `party_position` cue `claimed` at chunk `4399946` offsets `545-552`; context: The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are forced to return may face arbitrary arrest, detention, harsh punishments, torture, recruitment to indefinite military services or forced labour.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399946` offsets `445-453`; context: The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are forced to return may face arbitrary arrest, detention, harsh punishments, torture, recruitment to indefinite military services or forced labour.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4399946` offsets `794-805`; context: ” Consequently, the RAD set aside the RPD’s determination and substituted its own pursuant to paragraph 111(1)(b) of the Immigration and Refugee Protection Act, SC 2001, c 27 (“IRPA”).
- Evidence: `reasoning_application` cue `because` at chunk `4399946` offsets `392-399`; context: The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are forced to return may face arbitrary arrest, detention, harsh punishments, torture, recruitment to indefinite military services or forced labour.

#### 7522:1:subtheme:2 · paragraphs 4-23

- Raw key terms: `alazar, canada, eritrea, asmara, nablush, because, identity, sons`
- Display key terms: `alazar, eritrea, asmara, nablush, because, identity, sons`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: alazar, eritrea, asmara, nablush, because, identity, sons Position/evidence statements: Further, I do not agree with the Minister that the RAD lacked jurisdiction to consider the sur place aspects of the respondents’ claims. Rule/authority context: [4] The Minister now applies under subsection 72(1) of the IRPA for judicial review of the RAD’s decision. | None of these statements were under oath or solemn affirmation and none of the authors of the letters attended the RPD hearing. Application context: [4] The Minister now applies under subsection 72(1) of the IRPA for judicial review of the RAD’s decision. | Alazar testified that she was not questioned by border control officials because the agent said she did not speak English. Evidence spans paragraphs 4-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4399948` offsets `802-807`; context: With respect to the manner in which the decision was made, the Minister submits that, if the RAD did have jurisdiction to consider the sur place aspects of the claims, it breached the requirements of procedural fairness by making a positive determination on this basis without first giving the Minister notice that this issue was in play and an opportunity to be heard.
- Evidence: `governing_rule` cue `under` at chunk `4399948` offsets `29-34`; context: [4] The Minister now applies under subsection 72(1) of the IRPA for judicial review of the RAD’s decision.
- Evidence: `reasoning_application` cue `applies` at chunk `4399948` offsets `21-28`; context: [4] The Minister now applies under subsection 72(1) of the IRPA for judicial review of the RAD’s decision.
- Evidence: `issue` cue `whether` at chunk `4399949` offsets `521-528`; context: Since this is a sufficient basis to set aside the decision and remit the matter to a new decision maker, it is neither necessary nor appropriate to consider whether the RAD’s determination that the respondents are Convention refugees is unreasonable.
- Evidence: `party_position` cue `claims` at chunk `4399949` offsets `262-268`; context: Further, I do not agree with the Minister that the RAD lacked jurisdiction to consider the sur place aspects of the respondents’ claims.
- Evidence: `counterargument_limitation` cue `However` at chunk `4399949` offsets `270-277`; context: However, I do agree that the RAD did not comply with the requirements of procedural fairness.
- Evidence: `evidence_fact` cue `testimony` at chunk `4399950` offsets `307-316`; context: Alazar also described her experiences in Eritrea and her fear of returning there in her testimony before the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `4399955` offsets `881-888`; context: Alazar testified that she was not questioned by border control officials because the agent said she did not speak English.
- Evidence: `reasoning_application` cue `because` at chunk `4399956` offsets `156-163`; context: He could not accompany his family to Canada because of the ruse that the agent was Ms.
- Evidence: `reasoning_application` cue `because` at chunk `4399957` offsets `161-168`; context: Alazar stated that she believed if she returned to Eritrea she would be arrested, imprisoned and tortured by the government because she left the country illegally, because she had made a refugee claim against Eritrea, and because she was seen as disloyal to the government.
- Evidence: `reasoning_application` cue `because` at chunk `4399958` offsets `585-592`; context: The notice stated that Article 1F(b) – which excludes from refugee protection anyone about whom there are serious reasons for considering that “he has committed a serious non-political crime outside the country of refuge prior to his admission to that country as a refugee” – may be engaged because it appeared that Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399960` offsets `278-286`; context: Alazar and filing documentary evidence.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4399962` offsets `450-458`; context: Evidence of Identity
- Evidence: `evidence_fact` cue `testimony` at chunk `4399963` offsets `141-150`; context: Instead, to corroborate her testimony that she and her sons are who she said they are, Ms.
- Evidence: `governing_rule` cue `under` at chunk `4399963` offsets `1144-1149`; context: None of these statements were under oath or solemn affirmation and none of the authors of the letters attended the RPD hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4399963` offsets `1855-1862`; context: Alazar was not present because she was at work that day.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399964` offsets `83-91`; context: Nablush described above as evidence of their personal identities.
- Evidence: `reasoning_application` cue `apply` at chunk `4399965` offsets `156-161`; context: She did not apply for a new one while she was still in Eritrea.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399966` offsets `799-807`; context: ) She was also concerned about causing problems for family members in Eritrea if she asked them to help her obtain evidence from there to establish her identity.
- Evidence: `reasoning_application` cue `because` at chunk `4399966` offsets `165-172`; context: She stated that this was not possible because she had left the country illegally.

#### 7522:1:subtheme:3 · paragraphs 24-25

- Raw key terms: `filed, minister, post-hearing, submissions, addition, agency, altered, analyses`
- Display key terms: `filed, post-hearing, submissions, addition, agency, altered, analyses`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: filed, post-hearing, submissions, addition, agency, altered, analyses Application context: The print methods employed to produce this document are commercially available and therefore highly subject to illegitimate production. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4399968` offsets `863-870`; context: Further:
The physical examination of this document will not reveal whether it has been improperly issued, obtained by means of fraud or genuinely issued to a different person.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399968` offsets `263-271`; context: The reports stated that no evidence that the documents had been altered was found but all three reports were inconclusive with respect to the authenticity of the documents.
- Evidence: `reasoning_application` cue `therefore` at chunk `4399968` offsets `1122-1131`; context: The print methods employed to produce this document are commercially available and therefore highly subject to illegitimate production.
- Evidence: `counterargument_limitation` cue `but` at chunk `4399968` offsets `318-321`; context: The reports stated that no evidence that the documents had been altered was found but all three reports were inconclusive with respect to the authenticity of the documents.

#### 7522:1:subtheme:4 · paragraphs 26-28

- Raw key terms: `alazar, counsel, eritrea, claim, claimant, claims, credible, evidence`
- Display key terms: `alazar, eritrea, claims, credible`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: alazar, eritrea, claims, credible Evidence spans paragraphs 26-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4399970` offsets `296-302`; context: With respect to identity, Minister’s counsel raised a number of issues concerning the quality of the evidence of identity that was presented and concerning the absence of better evidence of identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399970` offsets `333-341`; context: With respect to identity, Minister’s counsel raised a number of issues concerning the quality of the evidence of identity that was presented and concerning the absence of better evidence of identity.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4399970` offsets `841-847`; context: Additionally, the Principal Claimant cannot be regarded as a credible witness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399971` offsets `86-94`; context: [27] In written submissions on behalf of the respondents, counsel maintained that the evidence presented to the RPD was sufficient to establish their personal identities.

#### 7522:1:subtheme:5 · paragraphs 29-30

- Raw key terms: `identity, issue, respondents, abroad, absent, accepted, accordingly, alazar`
- Display key terms: `identity, abroad, absent, accepted, accordingly, alazar`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: identity, abroad, absent, accepted, accordingly, alazar Position/evidence statements: [29] The RPD rejected the respondents’ claims in a decision dated August 22, 2018. Application context: o The reports also stated that while there was no evidence that the documents had been altered, the print methods used to produce them “are commercially available and therefore highly subject to illegitimate production. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4399973` offsets `99-104`; context: The dispositive issue was identity.
- Evidence: `party_position` cue `claims` at chunk `4399973` offsets `39-45`; context: [29] The RPD rejected the respondents’ claims in a decision dated August 22, 2018.
- Evidence: `issue` cue `question` at chunk `4399974` offsets `2616-2624`; context: As a result, neither the RPD nor Minister’s counsel had an opportunity to question them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399974` offsets `275-283`; context: Given the objective evidence that it is difficult to obtain Eritrean passports, the RPD found that it was reasonable that they did not have passports.
- Evidence: `reasoning_application` cue `therefore` at chunk `4399974` offsets `1602-1611`; context: o The reports also stated that while there was no evidence that the documents had been altered, the print methods used to produce them “are commercially available and therefore highly subject to illegitimate production.
- Evidence: `counterargument_limitation` cue `but` at chunk `4399974` offsets `3202-3205`; context: ”
The RPD accepted the letters from the Eritrean Canadian Community Centre of Metropolitan Toronto and from the Geez Rite Eritrean Catholic Chaplaincy as sufficient evidence of the respondents’ Eritrean ethnicity but neither provided credible or trustworthy evidence to establish their personal identities.

#### 7522:1:subtheme:6 · paragraphs 31-47

- Raw key terms: `respondents, evidence, alazar, appeal, hearing, because, eritrea, time`
- Display key terms: `alazar, hearing, because, eritrea, time`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: alazar, hearing, because, eritrea, time Position/evidence statements: The RAD also found in respect of both statutory declarations that they were “provided in response to RPD findings, and therefore could not have reasonably been expected to have been presented at the time of the rejection Rule/authority context: [34] In the statement required by subrule 3(3)(b) of the Refugee Appeal Division Rules, SOR/2012-257 (“RAD Rules”), the respondents indicated that they were seeking the admission of new evidence under subsection 110(4) o | DECISION UNDER REVIEW A. Application context: Alazar in Eritrea as well as why they had not attended the RPD hearing (one could not take time off work, the other had been difficult to reach because he had been very busy at work). | The RAD also found in respect of both statutory declarations that they were “provided in response to RPD findings, and therefore could not have reasonably been expected to have been presented at the time of the rejection Operative outcome context: [40] Despite admitting the new evidence, the RAD denied the respondents’ request for a hearing. | [47] Accordingly, the RAD allowed the appeal and, pursuant to paragraph 111(1)(b) of the IRPA, set aside the determination of the RPD and substituted its own determination that the respondents are Convention refugees. Evidence spans paragraphs 31-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4399975` offsets `35-40`; context: [31] Since identity is a threshold issue, the failure to establish it meant that the claims must fail.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4399977` offsets `61-70`; context: [33] In support of their appeal, the respondents tendered an affidavit from Ms.
- Evidence: `reasoning_application` cue `because` at chunk `4399977` offsets `726-733`; context: Alazar in Eritrea as well as why they had not attended the RPD hearing (one could not take time off work, the other had been difficult to reach because he had been very busy at work).
- Evidence: `evidence_fact` cue `evidence` at chunk `4399978` offsets `186-194`; context: [34] In the statement required by subrule 3(3)(b) of the Refugee Appeal Division Rules, SOR/2012-257 (“RAD Rules”), the respondents indicated that they were seeking the admission of new evidence under subsection 110(4) of the IRPA (i.
- Evidence: `governing_rule` cue `under` at chunk `4399978` offsets `195-200`; context: [34] In the statement required by subrule 3(3)(b) of the Refugee Appeal Division Rules, SOR/2012-257 (“RAD Rules”), the respondents indicated that they were seeking the admission of new evidence under subsection 110(4) of the IRPA (i.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399979` offsets `99-107`; context: [35] In their written submissions in support of the appeal, the respondents contended that the new evidence met the test for admission and that it “further establishes Ms.
- Evidence: `evidence_fact` cue `Record` at chunk `4399980` offsets `65-71`; context: [36] As required by subrule 3(2) of the RAD Rules, a copy of the Record was provided to the Minister.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4399981` offsets `110-118`; context: The Admissibility of the New Evidence
- Evidence: `governing_rule` cue `UNDER` at chunk `4399981` offsets `65-70`; context: DECISION UNDER REVIEW
A.
- Evidence: `party_position` cue `claims` at chunk `4399982` offsets `502-508`; context: The RAD also found in respect of both statutory declarations that they were “provided in response to RPD findings, and therefore could not have reasonably been expected to have been presented at the time of the rejection of [the] claims.
- Evidence: `evidence_fact` cue `found that` at chunk `4399982` offsets `13-23`; context: [38] The RAD found that the statutory declaration from Mr.
- Evidence: `governing_rule` cue `under` at chunk `4399982` offsets `92-97`; context: Hagos met the test for admission under subsection 110(4) of the IRPA while the one from Mr.
- Evidence: `reasoning_application` cue `therefore` at chunk `4399982` offsets `391-400`; context: The RAD also found in respect of both statutory declarations that they were “provided in response to RPD findings, and therefore could not have reasonably been expected to have been presented at the time of the rejection of [the] claims.
- Evidence: `counterargument_limitation` cue `However` at chunk `4399982` offsets `511-518`; context: ” However, because Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4399983` offsets `180-187`; context: Alazar with her husband were new because they were in response to the RPD’s concerns during the hearing that Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399984` offsets `31-39`; context: [40] Despite admitting the new evidence, the RAD denied the respondents’ request for a hearing.
- Evidence: `governing_rule` cue `under` at chunk `4399984` offsets `114-119`; context: The RAD concluded under subsection 110(6) of the IRPA that a hearing was not warranted because, while the new evidence was relevant, it would not justify allowing or rejecting the claims if accepted.
- Evidence: `reasoning_application` cue `because` at chunk `4399984` offsets `183-190`; context: The RAD concluded under subsection 110(6) of the IRPA that a hearing was not warranted because, while the new evidence was relevant, it would not justify allowing or rejecting the claims if accepted.
- Evidence: `disposition` cue `denied` at chunk `4399984` offsets `49-55`; context: [40] Despite admitting the new evidence, the RAD denied the respondents’ request for a hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399986` offsets `236-244`; context: As well, there was no evidence that a genuine Eritrean birth certificate would have had security features that were missing from the ones that were tendered.
- Evidence: `evidence_fact` cue `found that` at chunk `4399987` offsets `94-104`; context: [43] With respect to the failure to seek the assistance of family members in Eritrea, the RAD found that Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `4399988` offsets `61-71`; context: Nablush’s driver’s licence, the RAD found that Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399989` offsets `25-33`; context: [45] On the basis of the evidence before it, the RAD found that the respondents had established their claimed identities as Eritrean citizens.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399990` offsets `320-328`; context: According to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are forced to return may face arbitrary arrest, detention, harsh punishments, torture, recruitment to indefinite military services or forced labour [here the RAD cites a June 14, 2017, IRB Response to Information Request entitled “Eritrea: Situation of people returning to the country after they either spent time, claimed refugee status, or were seeking asylum abroad (July 2015-May 2017)].
- Evidence: `reasoning_application` cue `I find` at chunk `4399990` offsets `844-850`; context: As a result, I find that the Appellants do have a well-founded fear of persecution should they be forced to return to Eritrea.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4399991` offsets `50-61`; context: [47] Accordingly, the RAD allowed the appeal and, pursuant to paragraph 111(1)(b) of the IRPA, set aside the determination of the RPD and substituted its own determination that the respondents are Convention refugees.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4399991` offsets `5-16`; context: [47] Accordingly, the RAD allowed the appeal and, pursuant to paragraph 111(1)(b) of the IRPA, set aside the determination of the RPD and substituted its own determination that the respondents are Convention refugees.
- Evidence: `disposition` cue `allowed` at chunk `4399991` offsets `26-33`; context: [47] Accordingly, the RAD allowed the appeal and, pursuant to paragraph 111(1)(b) of the IRPA, set aside the determination of the RPD and substituted its own determination that the respondents are Convention refugees.

#### Section text

Canada (Citizenship and Immigration) v. Alazar
Court (s) Database
Federal Court Decisions
Date
2021-06-21
Neutral citation
2021 FC 637
File numbers
IMM-1168-20
Notes
A correction was made on September 6, 2022
Reported Decision
Decision Content
Date: 20210621
Docket: IMM-1168-20
Citation: 2021 FC 637
Ottawa, Ontario, June 21, 2021
PRESENT: Mr. Justice Norris
BETWEEN:
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Applicant
and
SARA MARSALA ALAZAR
SAMIEL ARAIA BEYENE
SELEMUN ARAIA BEYENE
Respondents
JUDGMENT AND REASONS
I. OVERVIEW

[1] The respondents – a mother and her two teenage sons – sought refugee protection in Canada on the basis of a fear of persecution in Eritrea due to the principal claimant’s perceived anti-government political opinions. In a decision dated August 22, 2018, the Refugee Protection Division (“RPD”) of the Immigration and Refugee Board (“IRB”) rejected the claims because it was not satisfied that the respondents had established their personal identities as citizens of Eritrea.

[2] The respondents appealed this decision to the Refugee Appeal Division (“RAD”) of the IRB. In a decision dated January 21, 2020, the RAD concluded that the RPD had erred in its findings regarding identity. Being satisfied that the respondents had established their personal identities, the RAD then went on to find that they are Convention refugees. The RAD reached this latter conclusion because, “[a]ccording to objective country condition evidence contained in the National Documentation Package, returnees who have left illegally or have claimed asylum and are forced to return may face arbitrary arrest, detention, harsh punishments, torture, recruitment to indefinite military services or forced labour.” Consequently, the RAD set aside the RPD’s determination and substituted its own pursuant to paragraph 111(1)(b) of the Immigration and Refugee Protection Act, SC 2001, c 27 (“IRPA”).

[3] The Minister of Citizenship and Immigration had intervened before the RPD but did not intervene in the respondents’ appeal to the RAD.

[4] The Minister now applies under subsection 72(1) of the IRPA for judicial review of the RAD’s decision. The Minister challenges both the substance of the decision and the manner in which it was made. With respect to the substance of the decision, the Minister submits that the RAD’s findings on identity and Convention refugee status are unreasonable. The Minister also submits that the RAD did not have jurisdiction to consider the sur place aspects of the respondents’ claims. With respect to the manner in which the decision was made, the Minister submits that, if the RAD did have jurisdiction to consider the sur place aspects of the claims, it breached the requirements of procedural fairness by making a positive determination on this basis without first giving the Minister notice that this issue was in play and an opportunity to be heard.

[5] As I will explain in the reasons that follow, the Minister has not persuaded me that the RAD’s identity finding is unreasonable. Further, I do not agree with the Minister that the RAD lacked jurisdiction to consider the sur place aspects of the respondents’ claims. However, I do agree that the RAD did not comply with the requirements of procedural fairness. Since this is a sufficient basis to set aside the decision and remit the matter to a new decision maker, it is neither necessary nor appropriate to consider whether the RAD’s determination that the respondents are Convention refugees is unreasonable.
II. BACKGROUND
A. The Respondents’ Claims for Protection

[6] The grounds for seeking protection are set out in Basis of Claim forms completed by Sara Marsala Alazar, the principal claimant, on her own behalf and on behalf of her sons shortly after they arrived in Canada. Ms. Alazar also described her experiences in Eritrea and her fear of returning there in her testimony before the RPD.

[7] Ms. Alazar states that she was born in December 1970 in the City of Asmara in Eritrea. At the time, Eritrea was a province of Ethiopia. It became an independent nation in 1993. Ms. Alazar belongs to the Tigrigna ethnic group.

[8] Ms. Alazar married Araia Beyene Nablush in January 2001. Mr. Nablush was born in Asmara in July 1965. Ms. Alazar and Mr. Nablush have two sons who were born in Asmara in June 2002 and January 2006, respectively.

[9] Ms. Alazar alleges that on February 3, 2016, she and Mr. Nablush were arrested at their home by armed security agents and taken by a police vehicle to a prison close to Asmara. Ms. Alazar was eventually released on February 26, 2016. Mr. Nablush was released on May 12, 2016. While they were detained, both were interrogated and subjected to physical and verbal abuse, including torture. Both were accused of being members of the Eritrean People’s Democratic Party-Zete and of working against the Eritrean government. Ms. Alazar explained that the suspicions related mainly to her husband but she was arrested too to see if she knew anything. According to Ms. Alazar, neither she nor her husband had been politically active previously.

[10] When Ms. Alazar was released she was told to report to the police every month, to not leave Asmara without the consent of security officials, and to not be found at any public meeting. She was also told that if she failed to comply with these conditions, she would be executed. Ms. Alazar testified that she reported to police four times before leaving Eritrea.

[11] With the assistance of a smuggler, the family left Asmara by car on June 28, 2016, and crossed the border into Sudan illegally two days later. In Sudan, Mr. Nablush contacted an agent who arranged travel to Canada for Ms. Alazar and their two sons. The agent obtained false passports for them as well as airline tickets. (At the RPD hearing, Ms. Alazar testified that this had cost $35,000 USD. Family members had provided the necessary funds.) In the company of the agent, who was posing as her husband, Ms. Alazar and her sons left Khartoum on August 30, 2016, and arrived in Toronto the next day via Cairo. At the RPD hearing, Ms. Alazar testified that she never saw the passports they travelled on. The agent had held onto them throughout the trip and was the one who presented them in Toronto. Ms. Alazar testified that she was not questioned by border control officials because the agent said she did not speak English.

[12] Mr. Nablush had remained in Sudan but eventually left for Kampala, Uganda, after he was detained in Sudan. He could not accompany his family to Canada because of the ruse that the agent was Ms. Alazar’s husband. He was not able to come afterwards because he could not afford to engage another agent. He decided to wait overseas to see what happened with the refugee claims in Canada.

[13] In her Basis of Claim form, Ms. Alazar stated that she believed if she returned to Eritrea she would be arrested, imprisoned and tortured by the government because she left the country illegally, because she had made a refugee claim against Eritrea, and because she was seen as disloyal to the government.
B. The Minister’s Intervention

[14] By notice dated December 8, 2016, the Minister indicated his intent to intervene in the proceeding before the RPD in relation to Article 1F(b) of the United Nations Convention Relating to the Status of Refugees, 28 July 1951, 189 UNTS 150 (“Refugee Convention”), identity and credibility. The notice stated that Article 1F(b) – which excludes from refugee protection anyone about whom there are serious reasons for considering that “he has committed a serious non-political crime outside the country of refuge prior to his admission to that country as a refugee” – may be engaged because it appeared that Ms. Alazar may have abducted her minor children when she travelled to Canada with them and remained here without the permission of their father. The notice also stated that the Minister “has serious concerns regarding the principal claimant’s credibility and all claimants’ identities.” As will be seen below, the Article 1F(b) concern was eventually withdrawn.

[15] A third-party Designated Representative was appointed for the minor claimants in April 2018. All three claimants were represented by a lawyer at the RPD.

[16] The hearing before the RPD took place on June 28, 2018. (A previous attendance on April 5, 2018, was adjourned on consent without the substance of the claims being addressed.) Counsel for the Minister took part in the hearing, questioning Ms. Alazar and filing documentary evidence. Counsel for the Minister also provided post-hearing written submissions, as did counsel for the respondents.
C. Evidence Relating to Article 1F(b) Exclusion

[17] Ms. Alazar testified that she left for Canada with her sons with their father’s permission; indeed, he was the one who had made all the arrangements. She and her sons have kept in regular contact with Mr. Nablush since they have been in Canada.

[18] Ms. Alazar provided a letter from Mr. Nablush in which he confirmed that he did not object to her having taken their sons to Canada or to her seeking refugee protection in Canada on their behalf. As proof of his identity, Mr. Nablush provided his Eritrean driver’s licence. (Mr. Nablush had sent his driver’s licence to Ms. Alazar in Canada but it had not arrived at the time of the RPD hearing. It was filed post-hearing without objection.)
D. Evidence of Identity

[19] The respondents did not provide any primary forms of identification to establish their personal identities. Instead, to corroborate her testimony that she and her sons are who she said they are, Ms. Alazar provided the following documentary evidence:
Copies of their respective birth certificates with translations.The birth certificates were issued by the Public Registration in the City of Asmara.All three were issued on November 25, 2009, and were numbered sequentially.Ms. Alazar testified that neither she nor her sons had had birth certificates previously.They only obtained these when her late father’s estate was being settled.They did not leave Eritrea with the birth certificates; rather, Ms. Alazar’s mother sent them to her later in Canada.
Letters from two individuals in Toronto, Hailemariam Fsshaye Hagos and Simon Hagos Berhe.Both men attested to having known Ms. Alazar in Eritrea.On the basis of interviews with these two men, the Program Coordinator with the Eritrean Canadian Community Centre of Metropolitan Toronto in turn attested in a letter that Ms. Alazar and her sons are Eritrean.None of these statements were under oath or solemn affirmation and none of the authors of the letters attended the RPD hearing.
A letter from the Chaplain of the Eritrean Catholic Ge’ez Rite Church in Toronto purporting to confirm Ms. Alazar’s Eritrean nationality and confirming her and her sons’ membership and attendance at the church.
Two photographs of family members taken in Eritrea.One depicted Ms. Alazar’s husband and their older son in 2004 or 2005.Ms. Alazar testified that she took the photograph.The other was a group photograph in which Ms. Alazar’s father and a number of other members of her family were depicted.The occasion was the acceptance of one of Ms. Alazar’s nieces into an order of nuns.Ms. Alazar was not present because she was at work that day.She did not know when the picture was taken but it was “a long time ago.”(Ms. Alazar’s father passed away in 2004.)
Two photographs of Ms. Alazar with family members taken in Eritrea.One depicted her, her parents, and her younger brother.It was taken around 1994.The other was of Ms. Alazar and her father.Ms. Alazar thought this photograph had been taken before the other one but she did not give a date.Her mother had sent all of the photographs to her in Canada.

[20] The respondents also relied on the letter from Mr. Nablush described above as evidence of their personal identities.

[21] Ms. Alazar testified that she had had a national identity card but it was taken from her when she was detained in 2016 and never returned. She did not apply for a new one while she was still in Eritrea.

[22] Ms. Alazar testified that since she had been in Canada she had not attempted to obtain photo identification from Eritrea. She stated that this was not possible because she had left the country illegally. She also testified that she did not have any other documents that would assist in establishing her identity. The family had left behind most of their belongings in the house they had been renting in Asmara and Ms. Alazar did not know what had become of them. She did not contact her former employer in Eritrea for confirmation of her employment because she did not want to cause problems for them. (Ms. Alazar testified that she had worked for the same employer for 15 years.) She was also concerned about causing problems for family members in Eritrea if she asked them to help her obtain evidence from there to establish her identity.

[23] The Designated Representative for the minor claimants related their recollections of their lives in Eritrea to the RPD. The Designated Representative stated that she had “no doubt that the boys are from Eritrea and lived there for some time.”

[24] Prior to the hearing, the Minister submitted the three birth certificates for analysis by a Canada Border Services Agency (“CBSA”) document examiner. The reports of these analyses (all dated April 12, 2018) were filed as exhibits. The reports stated that no evidence that the documents had been altered was found but all three reports were inconclusive with respect to the authenticity of the documents. The following comments were made with respect to each of the birth certificates:
The questioned document does not appear to contain any security features that would assist in determining the authenticity of the document. In addition, we do not have a specimen and/or genuine sample of this document. This limits the conclusion of my analysis and as such, my results remain inconclusive.
Further:
The physical examination of this document will not reveal whether it has been improperly issued, obtained by means of fraud or genuinely issued to a different person.
This document does not contain any recognizable security features. The print methods employed to produce this document are commercially available and therefore highly subject to illegitimate production.
This document contains no photograph, signature or biometric information to reliably link the document to the bearer and therefore does not provide reliable evidence of the bearer’s identity.
E. Post-Hearing Submissions

[25] Both the Minister and the respondents provided post-hearing written submissions. The Minister’s submissions were filed on July 13, 2018; the respondents’ were filed on July 20, 2018.

[26] After formally withdrawing the concern with respect to Article 1F(b) of the Refugee Convention, counsel for the Minister focused on concerns with respect to the claimants’ personal identities and the credibility of the claims. With respect to identity, Minister’s counsel raised a number of issues concerning the quality of the evidence of identity that was presented and concerning the absence of better evidence of identity. With respect to credibility, Minister’s counsel raised a number of issues concerning Ms. Alazar’s narrative of her experiences in Eritrea. In summary, Minister’s counsel submitted that “due to the inconsistencies, contradictions, and omissions presented by the Claimants, there are serious concerns regarding their credibility, and the credibility of their refugee claim. Additionally, the Principal Claimant cannot be regarded as a credible witness.”

[27] In written submissions on behalf of the respondents, counsel maintained that the evidence presented to the RPD was sufficient to establish their personal identities. With respect to the substance of the claims, counsel wrote the following: “It is respectfully submitted that the well-founded fear of the adult female claimant must not be forgotten in this case. Mrs. Sara Alazar provided moving and credible testimony in regard to the fact that she experienced rape and torture while in detention in Eritrea. There has been no evidence presented to contradict this oral evidence provided by Mrs. Alazar.” After referring to IRB Chairperson’s Guideline 4, counsel then continued as follows:
Further, it is submitted that the Board Member must consider the subjective fear that Mrs. Alazar would have in returning to Eritrea, should her refugee claim be rejected, given the fact that she has already experienced rape and torture in her country. To return this woman to a country in which it is well-documented that rampant human rights occur [sic], and in which she has already suffered so much, would be a travesty of justice.

[28] Counsel for the respondents did not make specific submissions regarding a fear of persecution or ill-treatment based on the fact that Ms. Alazar and her children had left Eritrea illegally or that they had sought asylum in Canada.
F. The RPD Decision

[29] The RPD rejected the respondents’ claims in a decision dated August 22, 2018. The dispositive issue was identity.

[30] The RPD concluded on a balance of probabilities that the respondents had failed to establish their identities. In summary, this conclusion was based on the following considerations:
The respondents did not present any primary forms of identification.Given the objective evidence that it is difficult to obtain Eritrean passports, the RPD found that it was reasonable that they did not have passports.The RPD noted that Ms. Alazar had explained that her national identity card was seized when she was arrested and was not returned to her.The RPD stated: “Regardless of the alleged circumstances of why the national identity card was not presented, the panel notes that the principal claimant did not proffer it as establishing her personal identity or country of nationality.”
The only documentation tendered by the respondents to establish their identities was the birth certificates.The RPD concluded that the birth certificates were not authentic and, as such, carried no weight in establishing identity.Further, the tendering of inauthentic documents undermined the respondents’ credibility.The RPD concluded that the birth certificates were not authentic for the following reasons:
o As stated in the reports of the CBSA document examiner, the birth certificates do not contain any recognizable security features.Further, there was no photograph, signature or biometric information that would link the document to the bearer.
o The reports also stated that while there was no evidence that the documents had been altered, the print methods used to produce them “are commercially available and therefore highly subject to illegitimate production.”
o An official stamp on each document that was partly in English misspelled the word “cemetery” as “cemetry”.
o Reports in the National Documentation Package confirmed the availability and prevalence of fraudulent identity documents in Eritrea and in Eritrean communities abroad.
The reasons given by Ms. Alazar for not trying to obtain other documentation to support her and her sons’ identities – she did not want to endanger her mother, her brother or her former employer – are not borne out by the evidence.Specifically, there was no evidence that Ms. Alazar’s mother or brother “were experiencing any problems at the hands of the Eritrean authorities.”This, in turn, undermined the credibility of the respondents with respect to their identities.
The letters from two community members attesting to their knowledge of Ms. Alazar were unsworn.Neither individual attended the hearing.As a result, neither the RPD nor Minister’s counsel had an opportunity to question them.Ms. Alazar had made little, if any, effort to secure their attendance despite the importance of the issues the RPD was being asked to determine, including the threshold iss

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 7522:2 · paragraphs 48-90

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3ee17e36779acbdebcd2d481245f4e55a1fe7e5e00d17d71223720e724218444`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7522:2:subtheme:1 · paragraphs 48-53

- Raw key terms: `para, decision, standard, vavilov, basis, maker, reasonableness, review`
- Display key terms: `para, standard, vavilov, basis, maker, reasonableness, review`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: para, standard, vavilov, basis, maker, reasonableness, review Rule/authority context: This includes a finding with respect to identity, a fact-driven determination (Denis v Canada (Citizenship and Immigration), 2018 FC 1182 at para 5; see also pre-RAD jurisprudence concerning the review of identity findin | [49] That this is the appropriate standard of review has been reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65. Evidence spans paragraphs 48-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4399992` offsets `352-365`; context: This includes a finding with respect to identity, a fact-driven determination (Denis v Canada (Citizenship and Immigration), 2018 FC 1182 at para 5; see also pre-RAD jurisprudence concerning the review of identity findings such as Rahal v Canada (Citizenship and Immigration), 2012 FC 319 at para 48, and Su v Canada (Citizenship and Immigration), 2012 FC 743 at para 5).
- Evidence: `governing_rule` cue `standard of review` at chunk `4399993` offsets `34-52`; context: [49] That this is the appropriate standard of review has been reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65.
- Evidence: `evidence_fact` cue `evidence` at chunk `4399996` offsets `521-529`; context: Importantly, when applying the reasonableness standard, it is not the role of the reviewing court to reweigh or reassess the evidence considered by the decision maker or to interfere with factual findings unless there are exceptional circumstances (Vavilov at para 125).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4399996` offsets `274-280`; context: Before a decision can be set aside on this basis, the reviewing court must be satisfied that “there are sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency” (Vavilov at para 100).

#### 7522:2:subtheme:2 · paragraphs 54-55

- Raw key terms: `basis, claims, consider, issue, jurisdiction, matter, minister, place`
- Display key terms: `basis, claims, consider, jurisdiction, matter, place`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: basis, claims, consider, jurisdiction, matter, place Rule/authority context: This strongly suggests that questions about the RAD’s jurisdiction to determine certain issues itself as opposed to referring the matter to the RPD should be answered under a correctness standard. Application context: [54] The majority in Vavilov held that the rule of law requires courts to apply the standard of correctness to certain types of legal questions including “questions regarding the jurisdictional boundaries between two or  Evidence spans paragraphs 54-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4399997` offsets `334-339`; context: This issue was not raised before the RAD and, as a result, it is not addressed in the RAD’s decision.
- Evidence: `issue` cue `issues` at chunk `4399998` offsets `375-381`; context: This strongly suggests that questions about the RAD’s jurisdiction to determine certain issues itself as opposed to referring the matter to the RPD should be answered under a correctness standard.
- Evidence: `governing_rule` cue `under` at chunk `4399998` offsets `454-459`; context: This strongly suggests that questions about the RAD’s jurisdiction to determine certain issues itself as opposed to referring the matter to the RPD should be answered under a correctness standard.
- Evidence: `reasoning_application` cue `apply` at chunk `4399998` offsets `74-79`; context: [54] The majority in Vavilov held that the rule of law requires courts to apply the standard of correctness to certain types of legal questions including “questions regarding the jurisdictional boundaries between two or more administrative bodies” (at para 53; see also paras 63 to 64).
- Evidence: `counterargument_limitation` cue `However` at chunk `4399998` offsets `484-491`; context: However, for present purposes, it is not necessary to come to a definitive conclusion about this.

#### 7522:2:subtheme:3 · paragraphs 56-58

- Raw key terms: `minister, analysis, fairness, issues, procedural, refugees, requirements, review`
- Display key terms: `analysis, fairness, issues, procedural, refugees, requirements, review`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: analysis, fairness, issues, procedural, refugees, requirements, review Position/evidence statements: b) Did the RAD have jurisdiction to consider the sur place claims? Rule/authority context: This is functionally the same as applying the correctness standard of review: see Canadian Pacific Railway Co at paras 49-56 and Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2 Application context: [57] The Minister submits that the RAD’s identity findings are unreasonable because the RAD failed to address two arguments made by the Minister at the RPD – namely, that Ms. Evidence spans paragraphs 56-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4399999` offsets `139-146`; context: [55] Finally, with regard to the procedure followed by the RAD, there is no dispute here concerning how a reviewing court should determine whether the requirements of procedural fairness were met.
- Evidence: `governing_rule` cue `standard of review` at chunk `4399999` offsets `726-744`; context: This is functionally the same as applying the correctness standard of review: see Canadian Pacific Railway Co at paras 49-56 and Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2020 FCA 196 at para 35.
- Evidence: `issue` cue `issues` at chunk `4400000` offsets `23-29`; context: [56] I would frame the issues raised in this application for judicial review as follows:
a) Is the RAD’s determination that the respondents had established their identities as citizens of Eritrea unreasonable?
- Evidence: `party_position` cue `claims` at chunk `4400000` offsets `269-275`; context: b) Did the RAD have jurisdiction to consider the sur place claims?
- Evidence: `reasoning_application` cue `because` at chunk `4400001` offsets `76-83`; context: [57] The Minister submits that the RAD’s identity findings are unreasonable because the RAD failed to address two arguments made by the Minister at the RPD – namely, that Ms.

#### 7522:2:subtheme:4 · paragraphs 59-61

- Raw key terms: `agree, appeal, arguments, basis, case, claims, consider, decision`
- Display key terms: `agree, arguments, basis, case, claims, consider`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: agree, arguments, basis, case, claims, consider Position/evidence statements: Did the RAD have jurisdiction to consider the sur place claims? Application context: As it was required to do, the RAD made its own findings on identity because, on a correctness standard, it found that the RPD had erred in several material respects. Evidence spans paragraphs 59-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4400002` offsets `368-376`; context: This latitude is especially apt when, as is the case here, the arguments in question were not made on the appeal to the RAD but only earlier in the process, to the RPD.
- Evidence: `evidence_fact` cue `record` at chunk `4400002` offsets `127-133`; context: It is well-established that a decision maker is not required to address every argument that arises on the record (Vavilov at para 91, citing Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708, at para 16).
- Evidence: `issue` cue `issues` at chunk `4400003` offsets `62-68`; context: [59] In any event, these arguments are peripheral to the core issues relating to the question of identity in this case.
- Evidence: `party_position` cue `claims` at chunk `4400003` offsets `851-857`; context: Did the RAD have jurisdiction to consider the sur place claims?
- Evidence: `evidence_fact` cue `found that` at chunk `4400003` offsets `227-237`; context: As it was required to do, the RAD made its own findings on identity because, on a correctness standard, it found that the RPD had erred in several material respects.
- Evidence: `reasoning_application` cue `because` at chunk `4400003` offsets `188-195`; context: As it was required to do, the RAD made its own findings on identity because, on a correctness standard, it found that the RPD had erred in several material respects.
- Evidence: `counterargument_limitation` cue `however` at chunk `4400004` offsets `283-290`; context: Before doing so, however, it may be helpful to begin by examining more closely the nature of the respondents’ claims for protection.

#### 7522:2:subtheme:5 · paragraphs 62-64

- Raw key terms: `fear, persecution, place, alazar, asylum, basis, because, claimed`
- Display key terms: `fear, persecution, place, alazar, asylum, basis, because, claimed`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: fear, persecution, place, alazar, asylum, basis, because, claimed Position/evidence statements: [63] As set out above, the RAD determined the respondents to be Convention refugees solely on the basis that, as “returnees who have left illegally or have claimed asylum” they had a well-founded fear of persecution shou Application context: [61] Typically, a refugee will leave their home country because of a fear of being persecuted there. | Alazar claimed that she was at risk because of her suspected political sympathies (for which she was arbitrarily detained and subjected to serious abuse while she was in Eritrea). Evidence spans paragraphs 62-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4400005` offsets `975-982`; context: As Hathaway and Foster explain, the present tense of Article 1A(2) of the Refugee Convention – “is outside the country of his nationality” (which is also found in paragraph 96(a) of the IRPA) – “ensures that all persons compelled to remain outside their own country – whether already present in, or forced to flee to, a foreign state – are equally entitled to benefit from the surrogate international protection of refugee law” (James C.
- Evidence: `reasoning_application` cue `because` at chunk `4400005` offsets `56-63`; context: [61] Typically, a refugee will leave their home country because of a fear of being persecuted there.
- Evidence: `reasoning_application` cue `because` at chunk `4400006` offsets `167-174`; context: Alazar claimed that she was at risk because of her suspected political sympathies (for which she was arbitrarily detained and subjected to serious abuse while she was in Eritrea).
- Evidence: `party_position` cue `claimed` at chunk `4400007` offsets `156-163`; context: [63] As set out above, the RAD determined the respondents to be Convention refugees solely on the basis that, as “returnees who have left illegally or have claimed asylum” they had a well-founded fear of persecution should they be forced to return to Eritrea.

#### 7522:2:subtheme:6 · paragraphs 65-66

- Raw key terms: `because, irpa, issue, jurisdiction, minister, place, according, addressed`
- Display key terms: `because, irpa, jurisdiction, place, according, addressed`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: because, irpa, jurisdiction, place, according, addressed Position/evidence statements: In Jianzhu v Canada (Citizenship and Immigration), 2015 FC 551 at para 12, Justice Simpson held as follows with respect to a RAD decision dismissing an appeal and finding that the applicants did not have a sur place clai Rule/authority context: According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the I | [65] There is support for the Minister’s position in this Court’s jurisprudence. Application context: According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the I | The RAD did not cite any authority for taking this step, and section 111(1)(b) of [the IRPA] does not apply because there was no RPD decision to set aside. Evidence spans paragraphs 65-66. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400008` offsets `148-153`; context: According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the IRPA, as it purported to do.
- Evidence: `governing_rule` cue `under` at chunk `4400008` offsets `285-290`; context: According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the IRPA, as it purported to do.
- Evidence: `reasoning_application` cue `because` at chunk `4400008` offsets `126-133`; context: According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the IRPA, as it purported to do.
- Evidence: `issue` cue `issue` at chunk `4400009` offsets `716-721`; context: In these circumstances, since it felt that the issue ought to have been decided, the RAD should have referred the Sur Place Claim back to the RPD for a decision.
- Evidence: `party_position` cue `claim` at chunk `4400009` offsets `297-302`; context: In Jianzhu v Canada (Citizenship and Immigration), 2015 FC 551 at para 12, Justice Simpson held as follows with respect to a RAD decision dismissing an appeal and finding that the applicants did not have a sur place claim when the RPD had not made any findings in relation to the sur place claim (which was based on religious practice in Canada):
In my view, the RAD lacked jurisdiction to independently decide the Sur Place Claim.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4400009` offsets `66-79`; context: [65] There is support for the Minister’s position in this Court’s jurisprudence.
- Evidence: `reasoning_application` cue `apply` at chunk `4400009` offsets `615-620`; context: The RAD did not cite any authority for taking this step, and section 111(1)(b) of [the IRPA] does not apply because there was no RPD decision to set aside.

#### 7522:2:subtheme:7 · paragraphs 67-69

- Raw key terms: `appeal, addressed, basis, decision, issue, matter, respect, address`
- Display key terms: `addressed, basis, matter, respect, address`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: addressed, basis, matter, respect, address Rule/authority context: (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois : (a) the decision of the Refugee Pr Application context: [66] Similarly, in Ojarikre v Canada (Citizenship and Immigration), 2015 FC 896 at para 20, Justice Annis held as follows with respect to a RAD decision dismissing an appeal on the basis of an Internal Flight Alternative Evidence spans paragraphs 67-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400010` offsets `231-236`; context: [66] Similarly, in Ojarikre v Canada (Citizenship and Immigration), 2015 FC 896 at para 20, Justice Annis held as follows with respect to a RAD decision dismissing an appeal on the basis of an Internal Flight Alternative when this issue was not addressed in the RPD’s decision or raised by either party in the appeal to the RAD:
The Court is in agreement with the Applicant’s submissions that the RAD does not possess the jurisdiction to consider an issue that, although fully canvassed before the RPD, was not relied upon in its decision and therefore was not the subject matter of the Applicant’s appeal.
- Evidence: `reasoning_application` cue `therefore` at chunk `4400010` offsets `543-552`; context: [66] Similarly, in Ojarikre v Canada (Citizenship and Immigration), 2015 FC 896 at para 20, Justice Annis held as follows with respect to a RAD decision dismissing an appeal on the basis of an Internal Flight Alternative when this issue was not addressed in the RPD’s decision or raised by either party in the appeal to the RAD:
The Court is in agreement with the Applicant’s submissions that the RAD does not possess the jurisdiction to consider an issue that, although fully canvassed before the RPD, was not relied upon in its decision and therefore was not the subject matter of the Applicant’s appeal.
- Evidence: `counterargument_limitation` cue `although` at chunk `4400010` offsets `462-470`; context: [66] Similarly, in Ojarikre v Canada (Citizenship and Immigration), 2015 FC 896 at para 20, Justice Annis held as follows with respect to a RAD decision dismissing an appeal on the basis of an Internal Flight Alternative when this issue was not addressed in the RPD’s decision or raised by either party in the appeal to the RAD:
The Court is in agreement with the Applicant’s submissions that the RAD does not possess the jurisdiction to consider an issue that, although fully canvassed before the RPD, was not relied upon in its decision and therefore was not the subject matter of the Applicant’s appeal.
- Evidence: `issue` cue `issue` at chunk `4400011` offsets `173-178`; context: [67] With all due respect to those who hold a different view, I am not persuaded that the RAD deciding an appeal on a basis not addressed by the RPD raises a jurisdictional issue (as opposed to an issue of procedural fairness, a topic I will address below).
- Evidence: `evidence_fact` cue `evidence` at chunk `4400012` offsets `1288-1296`; context: (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `governing_rule` cue `under` at chunk `4400012` offsets `1239-1244`; context: (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400012` offsets `1216-1222`; context: (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.

#### 7522:2:subtheme:8 · paragraphs 70-71

- Raw key terms: `appeal, claim, considering, consistent, decision, determination, determine, division`
- Display key terms: `considering, consistent, determination, determine, division`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: considering, consistent, determination, determine, division Rule/authority context: Notably, the mandate of the RPD under subsection 107(1) of the IRPA is to “determine” whether the claimant is a Convention refugee (or a person in need of protection). | This translates into the application of the correctness standard of review. Application context: Further, at paragraph 103 (emphasis added): I conclude from my statutory analysis that with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral Evidence spans paragraphs 70-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4400013` offsets `111-117`; context: [69] In my view, those who consider that paragraph 111(1)(b) of the IRPA imposes a jurisdictional limit on the issues the RAD may consider have interpreted the provision too broadly.
- Evidence: `governing_rule` cue `under` at chunk `4400013` offsets `510-515`; context: Notably, the mandate of the RPD under subsection 107(1) of the IRPA is to “determine” whether the claimant is a Convention refugee (or a person in need of protection).
- Evidence: `issue` cue `question` at chunk `4400014` offsets `265-273`; context: [70] Additionally, this interpretation is consistent with the now well-established view that paragraph 111(1)(a) of the IRPA permits the RAD to “confirm the determination of the Refugee Protection Division” (emphasis added) even if it finds that the RPD erred on a question of law, of fact or of mixed fact and law.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400014` offsets `809-817`; context: It can also set it aside, substituting its own determination of the claim, unless it is satisfied that it cannot do either without hearing the evidence presented to the RPD: paragraph 111(2)(b) of the IRPA.
- Evidence: `governing_rule` cue `standard of review` at chunk `4400014` offsets `556-574`; context: This translates into the application of the correctness standard of review.
- Evidence: `reasoning_application` cue `conclude` at chunk `4400014` offsets `919-927`; context: Further, at paragraph 103 (emphasis added):
I conclude from my statutory analysis that with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400014` offsets `772-778`; context: It can also set it aside, substituting its own determination of the claim, unless it is satisfied that it cannot do either without hearing the evidence presented to the RPD: paragraph 111(2)(b) of the IRPA.

#### 7522:2:subtheme:9 · paragraphs 72-73

- Raw key terms: `huruglica, addressed, appeal, aside, back, basis, bears, cannot`
- Display key terms: `huruglica, addressed, aside, back, basis, bears, cannot`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: huruglica, addressed, aside, back, basis, bears, cannot Rule/authority context: [71] As reflected in the foregoing dicta, the only jurisdictional constraint on the RAD’s power to dispose of an appeal is found in subsection 111(2) of the IRPA, which provides that two conditions must be satisfied befo Evidence spans paragraphs 72-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4400015` offsets `529-536`; context: They are, first, that the RAD is of the opinion that the decision of the RPD is wrong in law, in fact or in mixed fact and law and, second, that the RAD is of the opinion that it cannot determine whether to confirm the RPD’s determination or to set it aside and substitute the determination that, in its opinion, should have been made, without hearing the evidence that was presented to the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400015` offsets `689-697`; context: They are, first, that the RAD is of the opinion that the decision of the RPD is wrong in law, in fact or in mixed fact and law and, second, that the RAD is of the opinion that it cannot determine whether to confirm the RPD’s determination or to set it aside and substitute the determination that, in its opinion, should have been made, without hearing the evidence that was presented to the RPD.
- Evidence: `governing_rule` cue `under` at chunk `4400015` offsets `266-271`; context: [71] As reflected in the foregoing dicta, the only jurisdictional constraint on the RAD’s power to dispose of an appeal is found in subsection 111(2) of the IRPA, which provides that two conditions must be satisfied before the RAD may refer a matter back to the RPD under paragraph 111(1)(c) instead of determining the claim itself.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400015` offsets `512-518`; context: They are, first, that the RAD is of the opinion that the decision of the RPD is wrong in law, in fact or in mixed fact and law and, second, that the RAD is of the opinion that it cannot determine whether to confirm the RPD’s determination or to set it aside and substitute the determination that, in its opinion, should have been made, without hearing the evidence that was presented to the RPD.

#### 7522:2:subtheme:10 · paragraphs 74-75

- Raw key terms: `basis, irpa, minister, person, protection, refugee, without, address`
- Display key terms: `basis, irpa, person, protection, refugee, without, address`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: basis, irpa, person, protection, refugee, without, address Evidence spans paragraphs 74-75. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400017` offsets `128-133`; context: [73] In sum, contrary to the Minister’s submission, paragraph 111(1)(b) of the IRPA refers to the determination of the ultimate issue of whether a person is a Convention refugee (or a person in need of protection) and not to the subsidiary findings on a question of law, fact or mixed fact and law on which the RPD’s determination of this issue was based.
- Evidence: `evidence_fact` cue `record` at chunk `4400018` offsets `133-139`; context: [74] Subsection 110(3) of the IRPA provides that generally an appeal to the RAD “must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division.

#### 7522:2:subtheme:11 · paragraphs 76-77

- Raw key terms: `appeal, appellant, basis, canada, citizenship, fairness, immigration, para`
- Display key terms: `appellant, basis, fairness, para`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: appellant, basis, fairness, para Rule/authority context: [76] Usually this principle is invoked where the RAD has confirmed the RPD’s determination under paragraph 111(1)(a) of the IRPA that the appellant is not a Convention refugee but rests this conclusion on a different bas Evidence spans paragraphs 76-77. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400019` offsets `357-362`; context: ” This Court has recognized that, notwithstanding this rule, deciding an appeal on a new ground without first giving notice to the parties that the issue is in play can breach the requirements of procedural fairness.
- Evidence: `evidence_fact` cue `record` at chunk `4400019` offsets `647-653`; context: Justice Hughes expressed this exception to the general rule as follows in Husian v Canada (Citizenship and Immigration), 2015 FC 684 at para 10: “The point is that if the RAD chooses to take a frolic and venture into the record to make further substantive findings, it should give some sort of notice to the parties and give them an opportunity to make submissions.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `4400019` offsets `243-258`; context: ” This Court has recognized that, notwithstanding this rule, deciding an appeal on a new ground without first giving notice to the parties that the issue is in play can breach the requirements of procedural fairness.
- Evidence: `governing_rule` cue `under` at chunk `4400020` offsets `91-96`; context: [76] Usually this principle is invoked where the RAD has confirmed the RPD’s determination under paragraph 111(1)(a) of the IRPA that the appellant is not a Convention refugee but rests this conclusion on a different basis than the RPD.

#### 7522:2:subtheme:12 · paragraphs 78-79

- Raw key terms: `adversarial, balance, distinct, done, duty, ensure, mian, process`
- Display key terms: `adversarial, balance, distinct, done, duty, ensure, mian, process`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: adversarial, balance, distinct, done, duty, ensure, mian, process Evidence spans paragraphs 78-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4400021` offsets `26-33`; context: [77] The precise test for whether procedural fairness required notice to the parties and an opportunity to be heard is whether the ground on which the RAD decided the matter is a new issue in the sense that it is legally and factually distinct from the grounds of appeal advanced and cannot reasonably be said to stem from the issues on appeal as framed by the parties: see Ching v Canada (Citizenship and Immigration), 2015 FC 725 at paras 65 to 76, adopting the test in R v Mian, 2014 SCC 54 at para 30.
- Evidence: `issue` cue `question` at chunk `4400022` offsets `177-185`; context: [78] Even though both Mian and GF concerned criminal appeals, which involve interests and procedures quite distinct from those implicated in appeals to the RAD, there can be no question that in every case the RAD is required to strike the right balance between the adversarial process and its duty to ensure that a claim for protection is determined correctly.

#### 7522:2:subtheme:13 · paragraphs 80-81

- Raw key terms: `appeal, appellant, basis, complaint, even, fairness, minister, notice`
- Display key terms: `appellant, basis, complaint, even, fairness, notice`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: appellant, basis, complaint, even, fairness, notice Application context: Thus, before even considering how this test applies to the sur place claims, it is necessary to address the respondents’ principal submission that the Minister cannot claim the benefit of the test now because he did not  Evidence spans paragraphs 80-81. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4400023` offsets `106-113`; context: [79] When, as it did here, the RAD substitutes a determination that an appellant is a Convention refugee, whether on the basis of a new ground or otherwise, the appellant will have no cause for complaint.
- Evidence: `reasoning_application` cue `applies` at chunk `4400023` offsets `430-437`; context: Thus, before even considering how this test applies to the sur place claims, it is necessary to address the respondents’ principal submission that the Minister cannot claim the benefit of the test now because he did not intervene in the appeal to the RAD.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400023` offsets `546-552`; context: Thus, before even considering how this test applies to the sur place claims, it is necessary to address the respondents’ principal submission that the Minister cannot claim the benefit of the test now because he did not intervene in the appeal to the RAD.
- Evidence: `issue` cue `issue` at chunk `4400024` offsets `116-121`; context: [80] I do not agree that the notion of who is a party to an appeal to the RAD for purposes of the kind of notice at issue here should be construed so narrowly.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400024` offsets `517-525`; context: (The Minister may well also have the right to present evidence on the new issue; however, since the Minister’s complaint here is limited to the denial of the right to make submissions on the basis of the record before the RPD, I leave this question open.
- Evidence: `counterargument_limitation` cue `however` at chunk `4400024` offsets `544-551`; context: (The Minister may well also have the right to present evidence on the new issue; however, since the Minister’s complaint here is limited to the denial of the right to make submissions on the basis of the record before the RPD, I leave this question open.

#### 7522:2:subtheme:14 · paragraphs 82-83

- Raw key terms: `appeal, appeals, concerned, decision, interest, minister, party, person`
- Display key terms: `appeals, concerned, interest, person`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: appeals, concerned, interest, person Application context: If the person concerned applies to reinstate an appeal that was withdrawn, the RAD must, without delay, provide a copy of the application to the Minister (RAD Rules, subrule 48(3)). Evidence spans paragraphs 82-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4400025` offsets `156-164`; context: [81] Subject to certain exceptions that are irrelevant here, both the person concerned and the Minister have the right to appeal a decision of the RPD on a question of law, of fact or of mixed fact and law (IRPA, subsection 110(1)).
- Evidence: `counterargument_limitation` cue `However` at chunk `4400025` offsets `420-427`; context: ” However, I do not agree that, for procedural fairness purposes, this is exhaustive of the Minister’s interest in appeals to the RAD by persons concerned.
- Evidence: `evidence_fact` cue `Record` at chunk `4400026` offsets `658-664`; context: When an appeal by the person concerned is perfected, the RAD must provide a copy of the Appellant’s Record to the Minister without delay (RAD Rules, subrule 3(2)).
- Evidence: `reasoning_application` cue `applies` at chunk `4400026` offsets `1500-1507`; context: If the person concerned applies to reinstate an appeal that was withdrawn, the RAD must, without delay, provide a copy of the application to the Minister (RAD Rules, subrule 48(3)).

#### 7522:2:subtheme:15 · paragraphs 84-85

- Raw key terms: `appeal, application, cannot, fairness, minister, procedural, respondents, whether`
- Display key terms: `cannot, fairness, procedural, whether`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: cannot, fairness, procedural, whether Evidence spans paragraphs 84-85. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4400027` offsets `406-413`; context: Crucially, such notice allows the Minister to make informed and timely decisions about whether to intervene in a pending appeal and whether to pursue an application for leave and judicial review of a decision once it is made.
- Evidence: `evidence_fact` cue `Record` at chunk `4400027` offsets `645-651`; context: Thus, I cannot agree with the respondents that, having opted not to intervene after receiving their Record, the Minister had no right to notice of a subsequent development affecting the determination of the appeal and the respondents’ claims for protection.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400027` offsets `553-559`; context: Thus, I cannot agree with the respondents that, having opted not to intervene after receiving their Record, the Minister had no right to notice of a subsequent development affecting the determination of the appeal and the respondents’ claims for protection.
- Evidence: `issue` cue `question` at chunk `4400028` offsets `82-90`; context: To reiterate, the question is whether the ground on which the RAD decided the appeal is a new issue in the sense that it is legally and factually distinct from the grounds of appeal advanced and cannot reasonably be said to stem from the issues as framed by the respondents (the respondents being the only party to the appeal for the purpose of this part of the analysis).

#### 7522:2:subtheme:16 · paragraphs 86-87

- Raw key terms: `appeal, claims, framed, grounds, place, respondents, address, addressed`
- Display key terms: `claims, framed, grounds, place, address, addressed`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: claims, framed, grounds, place, address, addressed Evidence spans paragraphs 86-87. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400029` offsets `76-81`; context: [85] Applying this test, I have concluded that the sur place claim is a new issue and, as a result, the RAD was required to give notice to the Minister (and, of course, to the respondents) that it could be considered in deciding the appeal and, further, that all parties should have had an opportunity to address this issue before the appeal was decided.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400029` offsets `730-738`; context: The sur place claims are legally and factually distinct from the grounds of appeal related to the threshold issue of identity and also from the new evidence tendered by the respondents.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4400029` offsets `783-789`; context: Moreover, they cannot reasonably be said to stem from the issues as framed by the respondents in their appeal.

#### 7522:2:subtheme:17 · paragraphs 88-89

- Raw key terms: `decision, fairness, opportunity, procedural, requirements, respondents, above, address`
- Display key terms: `fairness, opportunity, procedural, requirements, above, address`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: fairness, opportunity, procedural, requirements, above, address Application context: ” Regrettably, because of how the RAD proceeded, this did not happen. Evidence spans paragraphs 88-89. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4400031` offsets `91-97`; context: [87] As I have explained above, in deciding an appeal the RAD has jurisdiction to consider issues the RPD did not address in its decision and, further, the RAD is not limited to considering the issues raised on appeal.
- Evidence: `counterargument_limitation` cue `However` at chunk `4400031` offsets `219-226`; context: However, when, as happened here, the case has materially shifted away from the RPD’s decision and the appeal as it was framed by the respondents, the RAD breached the requirements of procedural fairness by deciding the appeal on the basis on which it did without first giving the Minister notice that a new issue was in play and an opportunity to be heard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400032` offsets `545-553`; context: As the Supreme Court of Canada held in Baker (at para 22), “the purpose of the participatory rights contained within the duty of procedural fairness is to ensure that administrative decisions are made using a fair and open procedure, appropriate to the decision being made and its statutory, institutional, and social context, with an opportunity for those affected by the decision to put forward their views and evidence fully and have them considered by the decision-maker.
- Evidence: `reasoning_application` cue `because` at chunk `4400032` offsets `622-629`; context: ” Regrettably, because of how the RAD proceeded, this did not happen.

#### 7522:2:subtheme:18 · paragraphs 90-90

- Raw key terms: `address, already, issue, necessary, stated`
- Display key terms: `address, already, necessary, stated`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: address, already, necessary, stated Evidence spans paragraphs 90-90. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4400033` offsets `67-72`; context: [89] As I have already stated, it is not necessary to address this issue.

#### Section text

IV. STANDARD OF REVIEW

[48] It is well-established that the substance of the RAD’s decision is reviewed on a reasonableness standard (Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 35). This includes a finding with respect to identity, a fact-driven determination (Denis v Canada (Citizenship and Immigration), 2018 FC 1182 at para 5; see also pre-RAD jurisprudence concerning the review of identity findings such as Rahal v Canada (Citizenship and Immigration), 2012 FC 319 at para 48, and Su v Canada (Citizenship and Immigration), 2012 FC 743 at para 5).

[49] That this is the appropriate standard of review has been reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65. Reasonableness is now the presumptive standard of review for administrative decisions, subject to specific exceptions “only where required by a clear indication of legislative intent or by the rule of law” (Vavilov at para 10). There is no basis for derogating from this presumption here.

[50] A reasonable decision “is one that is based on an internally coherent and rational chain of analysis and that is justified in relation to the facts and law that constrain the decision maker” (Vavilov at para 85). A decision that displays these qualities is entitled to deference from the reviewing court (ibid.).

[51] As discussed in Vavilov, the exercise of public power “must be justified, intelligible and transparent, not in the abstract but to the individuals subject to it” (at para 95). For this reason, an administrative decision maker has a responsibility “to justify to the affected party, in a manner that is transparent and intelligible, the basis on which it arrived at a particular conclusion” (Vavilov at para 96).

[52] As the applicant, the onus is on the Minister to demonstrate that the RAD’s decision is unreasonable. Before a decision can be set aside on this basis, the reviewing court must be satisfied that “there are sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency” (Vavilov at para 100). Importantly, when applying the reasonableness standard, it is not the role of the reviewing court to reweigh or reassess the evidence considered by the decision maker or to interfere with factual findings unless there are exceptional circumstances (Vavilov at para 125).

[53] As noted above, the Minister challenges the RAD’s decision in part on the basis that it did not have jurisdiction to consider the sur place aspect of the claims. According to the Minister, having found material errors in the RPD’s identity findings, the RAD was required to refer the matter to the RPD for re-determination. This issue was not raised before the RAD and, as a result, it is not addressed in the RAD’s decision.

[54] The majority in Vavilov held that the rule of law requires courts to apply the standard of correctness to certain types of legal questions including “questions regarding the jurisdictional boundaries between two or more administrative bodies” (at para 53; see also paras 63 to 64). This strongly suggests that questions about the RAD’s jurisdiction to determine certain issues itself as opposed to referring the matter to the RPD should be answered under a correctness standard. However, for present purposes, it is not necessary to come to a definitive conclusion about this. Even approaching the issue on the most favourable basis from the Minister’s perspective and applying a correctness standard of review, as I explain below, the Minister has not persuaded me that the RAD did not have jurisdiction to consider the sur place aspects of the claims.

[55] Finally, with regard to the procedure followed by the RAD, there is no dispute here concerning how a reviewing court should determine whether the requirements of procedural fairness were met. The reviewing court must conduct its own analysis of the process followed by the decision maker and determine for itself whether the process was fair having regard to all the relevant circumstances, including those identified in Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 at paras 21 to 28: see Canadian Pacific Railway Co v Canada (Attorney General), 2018 FCA 69 at para 54, and Elson v Canada (Attorney General), 2019 FCA 27 at para 31. This is functionally the same as applying the correctness standard of review: see Canadian Pacific Railway Co at paras 49-56 and Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2020 FCA 196 at para 35. The burden is on the Minister to demonstrate that the requirements of procedural fairness were not met.
V. ISSUES

[56] I would frame the issues raised in this application for judicial review as follows:
a) Is the RAD’s determination that the respondents had established their identities as citizens of Eritrea unreasonable?
b) Did the RAD have jurisdiction to consider the sur place claims?
c) Did the RAD breach the requirements of procedural fairness by determining that the respondents are Convention refugees sur place without first giving the Minister notice that this issue was in play and an opportunity to be heard?
d) Is the RAD’s determination that the respondents are Convention refugees unreasonable?
VI. ANALYSIS
A. Is the RAD’s determination that the respondents had established their identities as citizens of Eritrea unreasonable?

[57] The Minister submits that the RAD’s identity findings are unreasonable because the RAD failed to address two arguments made by the Minister at the RPD – namely, that Ms. Alazar’s explanation for why she did not have a national identity card was implausible and that her claim to know nothing about the passports she and her sons had travelled on was not credible.

[58] I do not agree. It is well-established that a decision maker is not required to address every argument that arises on the record (Vavilov at para 91, citing Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708, at para 16). This latitude is especially apt when, as is the case here, the arguments in question were not made on the appeal to the RAD but only earlier in the process, to the RPD. The RPD did not adopt those arguments in its reasons and, as a result, they were not addressed in the respondents’ submissions to the RAD. As the Supreme Court observes in Vavilov, the review of an administrative decision “can be divorced neither from the institutional context in which the decision was made nor from the history of the proceedings” (at para 91).

[59] In any event, these arguments are peripheral to the core issues relating to the question of identity in this case. As it was required to do, the RAD made its own findings on identity because, on a correctness standard, it found that the RPD had erred in several material respects. The Minister has not attempted to demonstrate that the RPD did not commit the errors identified by the RAD. The RAD also based its identity findings in part on the new evidence it admitted on appeal and the Minister has not challenged the RAD’s new evidence rulings, either. Bearing in mind that it is not my role to reweigh evidence and that deference is owed to the decision maker on this issue, the Minister has not persuaded me that there is any basis to interfere with the RAD’s findings on identity.
B. Did the RAD have jurisdiction to consider the sur place claims?

[60] The Minister submits that the RAD did not have jurisdiction to consider the respondents’ sur place claims and, consequently, committed a reviewable error in determining the respondents to be Convention refugees on this basis. As I will explain, I do not agree. Before doing so, however, it may be helpful to begin by examining more closely the nature of the respondents’ claims for protection.

[61] Typically, a refugee will leave their home country because of a fear of being persecuted there. Indeed, this is exactly what Ms. Alazar says she did. While this sequence of events may be typical, it is not required in order to be recognized as a Convention refugee. An individual who, when they are abroad, finds that they cannot safely return to their home country is referred to as a refugee sur place. For example, a fear of persecution can arise as a result of a regime change that occurred while the claimant was working or studying abroad. Similarly, political activities engaged in by a claimant while they were elsewhere may put them at risk should they return to their country of nationality. As Hathaway and Foster explain, the present tense of Article 1A(2) of the Refugee Convention – “is outside the country of his nationality” (which is also found in paragraph 96(a) of the IRPA) – “ensures that all persons compelled to remain outside their own country – whether already present in, or forced to flee to, a foreign state – are equally entitled to benefit from the surrogate international protection of refugee law” (James C. Hathaway and Michelle Foster, The Law of Refugee Status (2nd ed) (Cambridge, UK: Cambridge University Press, 2014) at 75-76). See also UNHCR Handbook on Procedures and Criteria for Determining Refugee Status and Guidelines on International Protection (Reissued February 2019) at paras 94 to 96.

[62] It is not always easy (or even necessary) to draw a bright line between sur place claims and others. In the present case, Ms. Alazar claimed that she was at risk because of her suspected political sympathies (for which she was arbitrarily detained and subjected to serious abuse while she was in Eritrea). This was the principal basis of her claim for protection. She also claimed that she was at risk because she left Eritrea illegally and contrary to an order to remain in Asmara. The latter ground is causally connected to the events that gave rise to the fear of persecution in the first place – she fled Eritrea because of those events – but it crystalized only after Ms. Alazar left Asmara and then, a short time later, Eritrea. It thus has elements of a sur place claim, even if it is not exclusively so. On the other hand, the risk Ms. Alazar could face as a failed asylum seeker is clearly a sur place claim: the basis for this aspect of her claim arose only after she had left Eritrea and had made a claim for refugee protection in Canada.

[63] As set out above, the RAD determined the respondents to be Convention refugees solely on the basis that, as “returnees who have left illegally or have claimed asylum” they had a well-founded fear of persecution should they be forced to return to Eritrea. While the RAD did not use this terminology in its decision, there is no dispute that its determination can fairly be characterized as a finding that the respondents are Convention refugees sur place.

[64] The Minister submits that the RAD did not have jurisdiction to consider the sur place claims. According to the Minister, because this specific issue was not addressed by the RPD, the RAD could not “substitute” its determination concerning the sur place claims for that of the RPD under paragraph 111(1)(b) of the IRPA, as it purported to do.

[65] There is support for the Minister’s position in this Court’s jurisprudence. In Jianzhu v Canada (Citizenship and Immigration), 2015 FC 551 at para 12, Justice Simpson held as follows with respect to a RAD decision dismissing an appeal and finding that the applicants did not have a sur place claim when the RPD had not made any findings in relation to the sur place claim (which was based on religious practice in Canada):
In my view, the RAD lacked jurisdiction to independently decide the Sur Place Claim. The RAD did not cite any authority for taking this step, and section 111(1)(b) of [the IRPA] does not apply because there was no RPD decision to set aside. In these circumstances, since it felt that the issue ought to have been decided, the RAD should have referred the Sur Place Claim back to the RPD for a decision. Given that it did not take this approach, the RAD’s decision was unreasonable.

[66] Similarly, in Ojarikre v Canada (Citizenship and Immigration), 2015 FC 896 at para 20, Justice Annis held as follows with respect to a RAD decision dismissing an appeal on the basis of an Internal Flight Alternative when this issue was not addressed in the RPD’s decision or raised by either party in the appeal to the RAD:
The Court is in agreement with the Applicant’s submissions that the RAD does not possess the jurisdiction to consider an issue that, although fully canvassed before the RPD, was not relied upon in its decision and therefore was not the subject matter of the Applicant’s appeal.

[67] With all due respect to those who hold a different view, I am not persuaded that the RAD deciding an appeal on a basis not addressed by the RPD raises a jurisdictional issue (as opposed to an issue of procedural fairness, a topic I will address below).

[68] To begin with the statutory provisions, subsection 111(1) of the IRPA states the following:
111 (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
111 (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.

[69] In my view, those who consider that paragraph 111(1)(b) of the IRPA imposes a jurisdictional limit on the issues the RAD may consider have interpreted the provision too broadly. Considering the text, context and purpose of the provision, the words “the determination” do not refer to any and all findings made by the RPD but, rather, only to that tribunal’s finding on the ultimate issue of whether the claimant is a Convention refugee (or a person in need of protection). Notably, the mandate of the RPD under subsection 107(1) of the IRPA is to “determine” whether the claimant is a Convention refugee (or a person in need of protection). This narrower interpretation of paragraph 111(1)(b) is consistent with the wording of subsection 110(1) of the IRPA, which stipulates that an appeal to the RAD is an appeal “against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.” It is also consistent with the French version of subsection 111(1), which uses the phrase “la décision attaquée.”

[70] Additionally, this interpretation is consistent with the now well-established view that paragraph 111(1)(a) of the IRPA permits the RAD to “confirm the determination of the Refugee Protection Division” (emphasis added) even if it finds that the RPD erred on a question of law, of fact or of mixed fact and law. As the Federal Court of Appeal explained in Huruglica at paragraph 78 (emphasis added):
[T]he role of the RAD is to intervene when the RPD is wrong in law, in fact or in fact and law. This translates into the application of the correctness standard of review. If there is an error, the RAD can still confirm the decision of the RPD on another basis. It can also set it aside, substituting its own determination of the claim, unless it is satisfied that it cannot do either without hearing the evidence presented to the RPD: paragraph 111(2)(b) of the IRPA.
Further, at paragraph 103 (emphasis added):
I conclude from my statutory analysis that with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard. Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred. Having done this, the RAD is to provide a final determination, either by confirming the RPD decision or setting it aside and substituting its own determination of the merits of the refugee claim. It is only when the RAD is of the opinion that it cannot provide such a final determination without hearing the oral evidence presented to the RPD that the matter can be referred back to the RPD for redetermination. No other interpretation of the relevant statutory provisions is reasonable.

[71] As reflected in the foregoing dicta, the only jurisdictional constraint on the RAD’s power to dispose of an appeal is found in subsection 111(2) of the IRPA, which provides that two conditions must be satisfied before the RAD may refer a matter back to the RPD under paragraph 111(1)(c) instead of determining the claim itself. They are, first, that the RAD is of the opinion that the decision of the RPD is wrong in law, in fact or in mixed fact and law and, second, that the RAD is of the opinion that it cannot determine whether to confirm the RPD’s determination or to set it aside and substitute the determination that, in its opinion, should have been made, without hearing the evidence that was presented to the RPD. If these conditions are not satisfied, the RAD is required to determine the claim itself. There is no suggestion in Huruglica that the RAD cannot, as a matter of jurisdiction, substitute its own determination of the merits of the refugee claim on a basis that was not addressed by the RPD in its decision.

[72] It bears noting that both Jianzhu and Ojarikre were decided before Huruglica.

[73] In sum, contrary to the Minister’s submission, paragraph 111(1)(b) of the IRPA refers to the determination of the ultimate issue of whether a person is a Convention refugee (or a person in need of protection) and not to the subsidiary findings on a question of law, fact or mixed fact and law on which the RPD’s determination of this issue was based. As a result, it does not preclude the RAD from substituting its determination of a claim for that of the RPD on a ground that the RPD did not address. That being said, even if paragraph 111(1)(b) of the IRPA does not impose a jurisdictional constraint on the powers of the RAD to determine a claim for protection on a basis not addressed by the RPD, doing so can still raise procedural fairness concerns. I turn to this issue now.
C. Did the RAD breach the requirements of procedural fairness by determining that the respondents are Convention refugees sur place without first giving the Minister notice that this issue was in play and an opportunity to be heard?

[74] Subsection 110(3) of the IRPA provides that generally an appeal to the RAD “must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division.” Subsection 110(4), which governs the admission of new evidence from the person who is the subject of the appeal, creates an exception to this general

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 7522:3 · paragraphs 91-93

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e456acca19d89374a087ac54fe6507ec80d1e5bd60ce4c93d0059f14e4c3855f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7522:3:subtheme:1 · paragraphs 91-93

- Raw key terms: `agree, allowed, appeal, application, arise, aside, basis, calling`
- Display key terms: `agree, allowed, arise, aside, basis, calling`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: agree, allowed, arise, aside, basis, calling Rule/authority context: [91] The parties did not propose any serious questions of general importance for certification under paragraph 74(d) of the IRPA. Operative outcome context: [90] For these reasons, the Minister’s application for judicial review is allowed. Evidence spans paragraphs 91-93. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4400034` offsets `320-328`; context: For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400034` offsets `298-306`; context: For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.
- Evidence: `disposition` cue `allowed` at chunk `4400034` offsets `74-81`; context: [90] For these reasons, the Minister’s application for judicial review is allowed.
- Evidence: `governing_rule` cue `under` at chunk `4400035` offsets `95-100`; context: [91] The parties did not propose any serious questions of general importance for certification under paragraph 74(d) of the IRPA.

#### Section text

VII. CONCLUSION

[90] For these reasons, the Minister’s application for judicial review is allowed. The decision of the Refugee Appeal Division dated January 21, 2020, is set aside and the matter is remitted for redetermination by a different decision maker. For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.

[91] The parties did not propose any serious questions of general importance for certification under paragraph 74(d) of the IRPA. I agree that none arise.


## 7522:4 · paragraphs 94-95

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0d6a0435e2bae99ec2e62e93da1da9770b2487a8826b1ca7f65cdd57d522caef`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7522:4:subtheme:1 · paragraphs 94-95

- Raw key terms: `court, dated, general, imm-1168-20, judgment, minister, norris, respondents`
- Display key terms: `dated, imm-1168-20, norris`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: dated, imm-1168-20, norris Operative outcome context: JUDGMENT IN IMM-1168-20 THIS COURT’S JUDGMENT is that The application for judicial review is allowed. Evidence spans paragraphs 94-95. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4400035` offsets `494-502`; context: For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.
- Evidence: `evidence_fact` cue `evidence` at chunk `4400035` offsets `472-480`; context: For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.
- Evidence: `disposition` cue `allowed` at chunk `4400035` offsets `248-255`; context: JUDGMENT IN IMM-1168-20
THIS COURT’S JUDGMENT is that
The application for judicial review is allowed.

#### Section text

JUDGMENT IN IMM-1168-20
THIS COURT’S JUDGMENT is that
The application for judicial review is allowed.
The decision of the Refugee Appeal Division dated January 21, 2020, is set aside and the matter is remitted for redetermination by a different decision maker.
For greater certainty, unless the Minister presents new evidence calling into question the personal identities of the respondents, the RAD shall proceed on the basis that the personal identities of the respondents are established.
No question of general importance is stated.
“John Norris”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-1168-20
STYLE OF CAUSE:
THE MINISTER OF CITIZENSHIP AND IMMIGRATION v SARA MARSALA ALAZAR ET AL
HEARING HELD BY VIDEOCONFERENCE ON MAY 5, 2021 FROM OTTAWA, ONTARIO (COURT) AND TORONTO, ONTARIO (PARTIES)
JUDGMENT AND REASONS:
NORRIS J.
DATED:
June 21, 2021
APPEARANCES:
Monmi Goswami
For The Applicant
Vakkas Bilsin
For The RespondentS
SOLICITORS OF RECORD:
Attorney General of Canada
Toronto, Ontario
For The Applicant
Lewis & Associates
Toronto, Ontario
For The RespondentS
