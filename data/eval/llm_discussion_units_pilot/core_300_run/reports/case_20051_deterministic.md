# Discussion Units: case 20051

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **45**
- Continuity pairs: **44**
- Discussion Units: **6**
- Paragraph source hashes: **45**
- Sub-themes: **13**

## 20051:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `946254f3cf3e2c48c54b052160c9ce66ab65faadf27d291d21a747dc88d5f114`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicants, application, decision, immigration, june, reasons, based, board`
- Display key terms: `june, based`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: june, based Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated June 17, 2010, wherein the Applicants were determined to be neither  Operative outcome context: [2] Based on the reasons that follow, this application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4948261` offsets `274-279`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated June 17, 2010, wherein the Applicants were determined to be neither convention refugees nor persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, RS 2001, c 27 [IRPA].
- Evidence: `disposition` cue `dismissed` at chunk `4948262` offsets `58-67`; context: [2] Based on the reasons that follow, this application is dismissed.

#### Section text

Kaleja v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-06-09
Neutral citation
2011 FC 668
File numbers
IMM-4106-10
Decision Content
Federal Court
Cour fédérale
Date: 20110609
Docket: IMM-4106-10
Citation: 2011 FC 668
Ottawa, Ontario, June 9, 2011
PRESENT: The Honourable Mr. Justice Near
BETWEEN:
MICHAL KALEJA
DAGMAR KALEJOVA
TEREZIE KALEJOVA
LUCIE KALEJOVA
MICHAELA KALEJOVA
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated June 17, 2010, wherein the Applicants were determined to be neither convention refugees nor persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, RS 2001, c 27 [IRPA].

[2] Based on the reasons that follow, this application is dismissed.


## 20051:2 · paragraphs 3-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c45355cded420ff52cab662a7bb33c9c8f6eebf51642961251181a68aa2560a9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:2:subtheme:1 · paragraphs 3-10

- Raw key terms: `applicants, father, michaela, attacked, boyfriend, abusive, afraid, arrived`
- Display key terms: `father, michaela, attacked, boyfriend, abusive, afraid, arrived`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: father, michaela, attacked, boyfriend, abusive, afraid, arrived Position/evidence statements: She claimed to have been in the Ukraine with her boyfriend, the father of her child. Application context: [4] The Applicants allege they suffered various and ongoing forms of discrimination because of their Roma ethnicity. | In the Port of Entry interview she explained that she had run off to be with him because she was scared to tell her parents that she was pregnant. Evidence spans paragraphs 3-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4948264` offsets `84-91`; context: [4] The Applicants allege they suffered various and ongoing forms of discrimination because of their Roma ethnicity.
- Evidence: `party_position` cue `claimed` at chunk `4948268` offsets `86-93`; context: She claimed to have been in the Ukraine with her boyfriend, the father of her child.
- Evidence: `evidence_fact` cue `testimony` at chunk `4948268` offsets `367-376`; context: At the hearing, the testimony revealed that Michaela’s boyfriend was abusive and the Applicants claimed to be afraid of him and the other Ukrainian men who attacked them.
- Evidence: `reasoning_application` cue `because` at chunk `4948268` offsets `248-255`; context: In the Port of Entry interview she explained that she had run off to be with him because she was scared to tell her parents that she was pregnant.
- Evidence: `evidence_fact` cue `determined that` at chunk `4948269` offsets `14-29`; context: [9] The Board determined that the evidence relating to Michaela’s abusive former boyfriend was unreliable and that there was not a serious possibility that the Applicants would be at risk of harm from him.

#### 20051:2:subtheme:2 · paragraphs 11-11

- Raw key terms: `ability, acknowledged, adequacy, adequate, always, applicants, assessed, attitudes`
- Display key terms: `ability, acknowledged, adequacy, adequate, always, assessed, attitudes`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: ability, acknowledged, adequacy, adequate, always, assessed, attitudes Evidence spans paragraphs 11-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4948270` offsets `140-145`; context: The Board found that the determinative issue in the claim was state protection.
- Evidence: `evidence_fact` cue `found that` at chunk `4948270` offsets `111-121`; context: The Board found that the determinative issue in the claim was state protection.

#### Section text

I. Background
A. Factual Background

[3] The Applicants are citizens of the Czech Republic. The father, Michal Kaleja, is Roma. His wife, Dagmar Kalejova, is Caucasian. They have three daughters, Michaela, Terezie and Lucie, who are perceived as Roma. They fear persecution on the grounds of race and membership in a particular social group.

[4] The Applicants allege they suffered various and ongoing forms of discrimination because of their Roma ethnicity. The father’s Personal Information Form (PIF) recounts harassment, intimidation and other forms of persecution at the hands of Skinheads, Neo-nazis and Caucasians while growing up and continuing on in adulthood. The Applicants regularly faced discrimination from their neighbours. The children were harassed at school.

[5] The PIF lists several specific incidents. Among them, Neo-nazis threw a molotov cocktail through the Applicants’ window in 2001. The father claims he was viciously attacked by Skinheads in 2006. He was stabbed during the incident. In 2002 a neighbourhood Caucasian child threatened to kill Lucie with a rock. Terezie was falsely accused of stealing a cell phone at school in 2000. Her mother was called. The incident escalated and the mother needed to call the police.

[6] According to the PIF the police were called after each one of these incidents, but the result was the same. The police would take part in questioning but nothing else would ever happen. However, on at least one occasion the father admitted to being too afraid to press charges.

[7] Michaela left home in 2008 and did not return. A few weeks later, some Ukrainian-Russian men allegedly entered the Applicants’ home and attacked the family, warning them not to look for Michaela, otherwise risk being killed. The family believed the young men were associated with Michaela’s Ukrainian boyfriend. Soon after this, the family, minus Michaela, took steps to leave the country and arrived in Canada on May 12, 2008.

[8] Michaela arrived separately in Toronto on December 5, 2008. She was pregnant. She claimed to have been in the Ukraine with her boyfriend, the father of her child. In the Port of Entry interview she explained that she had run off to be with him because she was scared to tell her parents that she was pregnant. He threw her out 5 months later. At the hearing, the testimony revealed that Michaela’s boyfriend was abusive and the Applicants claimed to be afraid of him and the other Ukrainian men who attacked them.
B. Impugned Decision

[9] The Board determined that the evidence relating to Michaela’s abusive former boyfriend was unreliable and that there was not a serious possibility that the Applicants would be at risk of harm from him.

[10] The rest of the claim was assessed on the risk of harm based on the Applicants’ Roma ethnicity. The Board found that the determinative issue in the claim was state protection. While the Board acknowledged that the experience of the Applicants was mixed with respect to the ability and willingness of the state to protect, the Board found that when the Applicants called the police they responded. While the protection offered was not always effective, the Board found that the Applicants had failed to rebut the presumption of state protection based on the test of adequacy. The Applicants were unable to provide clear and convincing evidence that the Czech state is unwilling or unable to provide adequate protection. The Board went on to examine what efforts the Czech Republic has undertaken to protect Roma, and the effects of those efforts. The Board concluded that the Applicants “did not experience failure of the protection of the state as much as a failure of societal attitudes in the Czech Republic”, and that there was no evidence that adequate state protection would not be reasonably forthcoming should the Applicants need it.
II. Issues

## 20051:3 · paragraphs 12-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a92617b0dfa7f0336af405863c19435306d99e066fd0024a3c1fe43531ea211d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:3:subtheme:1 · paragraphs 12-13

- Raw key terms: `board, credibility, standard, analysis, applicants, application, assessment, canada`
- Display key terms: `credibility, standard, analysis, assessment`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: credibility, standard, analysis, assessment Rule/authority context: Standard of Review Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4948271` offsets `43-49`; context: [11] This application raises the following issues:
(a) Did the Board make an unreasonable credibility finding?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4948271` offsets `325-343`; context: Standard of Review
- Evidence: `evidence_fact` cue `evidence` at chunk `4948272` offsets `115-123`; context: [12] It is well-established that decisions of the Board as to credibility and the interpretation and assessment of evidence are all reviewable on a standard of reasonableness (Lawal v Canada (Minister of Citizenship and Immigration), 2010 FC 558 at para 11; NOO v Canada (Minister of Citizenship and Immigration), 2009 FC 1045, [2009] FCJ No 1286 at para 38).

#### 20051:3:subtheme:2 · paragraphs 14-17

- Raw key terms: `board, finding, applicants, boyfriend, canada, erred, evidence, michaela`
- Display key terms: `finding, boyfriend, erred, michaela`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: finding, boyfriend, erred, michaela Position/evidence statements: [16] The Applicants submit that the Board erred in several regards. Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4948273` offsets `23-28`; context: [13] The determinative issue in the present case was state protection.
- Evidence: `issue` cue `whether` at chunk `4948274` offsets `240-247`; context: It is also concerned with whether the decision falls within a range of acceptable outcomes that are defensible in respect of the facts and law.
- Evidence: `evidence_fact` cue `found that` at chunk `4948275` offsets `15-25`; context: [15] The Board found that there was no threat to the family from Michaela’s boyfriend, and even if the Board erred in this assessment they did not find, on a forward-looking basis, an objectively well-founded fear or harm or future risk.
- Evidence: `party_position` cue `submit` at chunk `4948276` offsets `20-26`; context: [16] The Applicants submit that the Board erred in several regards.
- Evidence: `evidence_fact` cue `testimony` at chunk `4948276` offsets `313-322`; context: Secondly, the Board erred in drawing a negative inference from Michaela’s inconsistent testimony regarding the abusive relationship.

#### 20051:3:subtheme:3 · paragraphs 18-24

- Raw key terms: `board, evidence, boyfriend, court, credibility, hearing, para, reasonable`
- Display key terms: `boyfriend, credibility, hearing, para, reasonable`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: boyfriend, credibility, hearing, para, reasonable Position/evidence statements: She claimed not to know his last name or what he did for a living. | [22] As the Respondent submits, the Applicants’ submissions with respect to the credibility findings are nothing more than an invitation for this Court to reweigh evidence that has already been reasonably assessed by the Application context: [17] With respect, I find no reviewable error with respect to any of the above issues. | [20] At the POE Michaela would not reveal her boyfriend’s name because she did not want to get him into trouble with the Czech authorities. Evidence spans paragraphs 18-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4948277` offsets `79-85`; context: [17] With respect, I find no reviewable error with respect to any of the above issues.
- Evidence: `reasoning_application` cue `I find` at chunk `4948277` offsets `19-25`; context: [17] With respect, I find no reviewable error with respect to any of the above issues.
- Evidence: `evidence_fact` cue `testimony` at chunk `4948278` offsets `237-246`; context: [18] In terms of credibility findings, it is open and reasonable, and is in fact a well-accepted and standard practice, for the Board to base credibility findings on omissions and inconsistencies between POE notes, PIFs and a claimant’s testimony at the hearing.
- Evidence: `evidence_fact` cue `testimony` at chunk `4948279` offsets `242-251`; context: It is not enough for an applicant to say that what he said in oral testimony was an elaboration.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948280` offsets `85-93`; context: [19] The Board explicitly considered the Gender Guidelines in relation to Michaela’s evidence and stated at para 11 of the reasons:
while I certainly accept and understand that some women might not reveal the existence of abuse in their relationship immediately, in this case reviewing as a whole the notes taken when she first made her claim for protection reveals a different story.
- Evidence: `party_position` cue `claimed` at chunk `4948281` offsets `144-151`; context: She claimed not to know his last name or what he did for a living.
- Evidence: `reasoning_application` cue `because` at chunk `4948281` offsets `63-70`; context: [20] At the POE Michaela would not reveal her boyfriend’s name because she did not want to get him into trouble with the Czech authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948282` offsets `274-282`; context: Based on the evidence, this was a reasonable finding.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4948282` offsets `167-179`; context: The Board was nevertheless not convinced that the boyfriend posed a risk of prospective harm to the family.
- Evidence: `party_position` cue `submits` at chunk `4948283` offsets `23-30`; context: [22] As the Respondent submits, the Applicants’ submissions with respect to the credibility findings are nothing more than an invitation for this Court to reweigh evidence that has already been reasonably assessed by the Board.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948283` offsets `163-171`; context: [22] As the Respondent submits, the Applicants’ submissions with respect to the credibility findings are nothing more than an invitation for this Court to reweigh evidence that has already been reasonably assessed by the Board.

#### 20051:3:subtheme:4 · paragraphs 25-26

- Raw key terms: `applicants, board, adequate, applied, case, claim, clear, contentions`
- Display key terms: `adequate, applied, case, clear, contentions`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: adequate, applied, case, clear, contentions Position/evidence statements: [24] The Applicants submit that the Board applied the incorrect test and erred in finding that the Applicants had not rebutted the presumption. Application context: [24] The Applicants submit that the Board applied the incorrect test and erred in finding that the Applicants had not rebutted the presumption. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4948284` offsets `23-28`; context: [23] The determinative issue in this claim for protection was state protection.
- Evidence: `evidence_fact` cue `found that` at chunk `4948284` offsets `90-100`; context: The Board found that the Applicants did not provide clear and convincing evidence that adequate state protection would not be forthcoming should they need it.
- Evidence: `party_position` cue `submit` at chunk `4948285` offsets `20-26`; context: [24] The Applicants submit that the Board applied the incorrect test and erred in finding that the Applicants had not rebutted the presumption.
- Evidence: `reasoning_application` cue `applied` at chunk `4948285` offsets `42-49`; context: [24] The Applicants submit that the Board applied the incorrect test and erred in finding that the Applicants had not rebutted the presumption.

#### 20051:3:subtheme:5 · paragraphs 27-32

- Raw key terms: `state, adequate, board, protection, czech, republic, applicants, effective`
- Display key terms: `state, adequate, protection, czech, republic, effective`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: state, adequate, protection, czech, republic, effective Position/evidence statements: [30] The Applicants submit that the Board erred in its analysis by not considering the effects of cumulative persecution. Application context: The Board applied the correct test. | ” The father goes on to say that they were afraid of pressing charges because they feared retaliation. Evidence spans paragraphs 27-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4948286` offsets `331-338`; context: This Court has recently and repeatedly confirmed the Federal Court of Appeal’s ruling in Carillo v Canada (Minister of Citizenship and Immigration), 2008 FCA 94, 69 Imm LR (3d) 309 that that the test for a finding of state protection is whether that protection is adequate, not whether it is effective, per se.
- Evidence: `reasoning_application` cue `applied` at chunk `4948286` offsets `68-75`; context: The Board applied the correct test.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948287` offsets `260-268`; context: [26] The Board is not obliged to prove that the Czech Republic can offer the Applicant effective state protection, rather, the Applicant bears the legal burden of rebutting the presumption that adequate state protection exists by adducing clear and convincing evidence which satisfies the Board on a balance of probabilities (Carillo, above, at para 30).
- Evidence: `evidence_fact` cue `evidence` at chunk `4948288` offsets `221-229`; context: The Board noted that there are concerns that these efforts are not adequate but that the preponderance of the evidence indicates that the state is taking action against extremists and does not condone or acquiesce to extremist actions, and those actions are effective.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948289` offsets `61-69`; context: [28] The Applicants did not provide any clear and convincing evidence that the Czech Republic continues to be unable or unwilling to protect them.
- Evidence: `reasoning_application` cue `because` at chunk `4948289` offsets `424-431`; context: ” The father goes on to say that they were afraid of pressing charges because they feared retaliation.
- Evidence: `counterargument_limitation` cue `However` at chunk `4948289` offsets `457-464`; context: However, unwillingness to access state protection is not a basis for proving that it does not exist.
- Evidence: `reasoning_application` cue `I find` at chunk `4948290` offsets `5-11`; context: [29] I find that the Board’s finding of fact regarding state protection in the Czech Republic was reasonable, and established that state protection, while at times ineffective, was adequate.
- Evidence: `party_position` cue `submit` at chunk `4948291` offsets `20-26`; context: [30] The Applicants submit that the Board erred in its analysis by not considering the effects of cumulative persecution.

#### 20051:3:subtheme:6 · paragraphs 33-36

- Raw key terms: `analysis, board, protection, section, claimant, claimants, determined, fear`
- Display key terms: `analysis, protection, section, determined, fear`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: analysis, protection, section, determined, fear Position/evidence statements: However, as the Respondent submits, Munderere has the effect of reaffirming that, as the Board determined in the instant matter, the availability of state protection is key for determining whether the claimant has a well | [33] The Applicant submits that claimants are entitled to a separate section 97 analysis if there is credible evidence. Rule/authority context: [32] The substance of the Board’s section 97 analysis reads as follows: There was no residual information upon which a claim under this section could be determined that was not already considered above. Application context: Therefore, I find that claimants are not persons in need of protection and their claims under section 97 of the IRPA fail. Evidence spans paragraphs 33-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4948292` offsets `358-365`; context: However, as the Respondent submits, Munderere has the effect of reaffirming that, as the Board determined in the instant matter, the availability of state protection is key for determining whether the claimant has a well-founded fear of persecution.
- Evidence: `party_position` cue `submits` at chunk `4948292` offsets `196-203`; context: However, as the Respondent submits, Munderere has the effect of reaffirming that, as the Board determined in the instant matter, the availability of state protection is key for determining whether the claimant has a well-founded fear of persecution.
- Evidence: `counterargument_limitation` cue `However` at chunk `4948292` offsets `169-176`; context: However, as the Respondent submits, Munderere has the effect of reaffirming that, as the Board determined in the instant matter, the availability of state protection is key for determining whether the claimant has a well-founded fear of persecution.
- Evidence: `issue` cue `whether` at chunk `4948293` offsets `28-35`; context: [45] The plain fact is that whether a claimant relies on a single or a number of events taken together, he still has the obligation to satisfy the Board that, at the time of the hearing, he has a well founded fear of persecution in regard to the country from which he seeks protection.
- Evidence: `evidence_fact` cue `determined that` at chunk `4948294` offsets `153-168`; context: [32] The substance of the Board’s section 97 analysis reads as follows:
There was no residual information upon which a claim under this section could be determined that was not already considered above.
- Evidence: `governing_rule` cue `under` at chunk `4948294` offsets `125-130`; context: [32] The substance of the Board’s section 97 analysis reads as follows:
There was no residual information upon which a claim under this section could be determined that was not already considered above.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4948294` offsets `203-212`; context: Therefore, I find that claimants are not persons in need of protection and their claims under section 97 of the IRPA fail.
- Evidence: `party_position` cue `submits` at chunk `4948295` offsets `19-26`; context: [33] The Applicant submits that claimants are entitled to a separate section 97 analysis if there is credible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948295` offsets `110-118`; context: [33] The Applicant submits that claimants are entitled to a separate section 97 analysis if there is credible evidence.

#### 20051:3:subtheme:7 · paragraphs 37-39

- Raw key terms: `canada, citizenship, court, evidence, immigration, minister, need, person`
- Display key terms: `need, person`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: need, person Position/evidence statements: Similarly, in the present matter the Applicants section 97 claim rested entirely upon their assertion that they would be persecuted for being Roma. Rule/authority context: [34] The jurisprudence on this issue is mixed, but, as per Justice Mosley at para 22 of Soleimanian v Canada (Minister of Citizenship and Immigration), 2004 FC 1660, 135 ACWS (3d) 474: | The only alternative basis upon which the Board might have determined that the Applicants were in need of protection under section 97 was their fear of Michaela’s former boyfriend. Evidence spans paragraphs 37-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4948296` offsets `31-36`; context: [34] The jurisprudence on this issue is mixed, but, as per Justice Mosley at para 22 of Soleimanian v Canada (Minister of Citizenship and Immigration), 2004 FC 1660, 135 ACWS (3d) 474:
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4948296` offsets `9-22`; context: [34] The jurisprudence on this issue is mixed, but, as per Justice Mosley at para 22 of Soleimanian v Canada (Minister of Citizenship and Immigration), 2004 FC 1660, 135 ACWS (3d) 474:
- Evidence: `evidence_fact` cue `evidence` at chunk `4948297` offsets `117-125`; context: [22] This Court seems to have come to a consensus that a separate section 97 analysis is not required if there is no evidence that could go to establishing that the person is in need of protection […]
- Evidence: `party_position` cue `claim` at chunk `4948298` offsets `198-203`; context: Similarly, in the present matter the Applicants section 97 claim rested entirely upon their assertion that they would be persecuted for being Roma.
- Evidence: `evidence_fact` cue `found that` at chunk `4948298` offsets `29-39`; context: [35] In that case, the Court found that there was no other evidence before the Board that the claimant was a person in need of protection.
- Evidence: `governing_rule` cue `under` at chunk `4948298` offsets `404-409`; context: The only alternative basis upon which the Board might have determined that the Applicants were in need of protection under section 97 was their fear of Michaela’s former boyfriend.
- Evidence: `counterargument_limitation` cue `However` at chunk `4948298` offsets `468-475`; context: However, a negative credibility finding in relation to a section 96 claim obviates the need to consider it under section 97 (Mejia v Canada (Minister of Citizenship and Immigration), 2010 FC 410).

#### Section text

[11] This application raises the following issues:
(a) Did the Board make an unreasonable credibility finding?
(b) Did the Board err in its analysis of state protection?
(c) Did the Board ignore the Applicants’ claim of cumulative persecution?
(d) Did the Board err in failing to conduct a separate section 97 analysis?
III. Standard of Review

[12] It is well-established that decisions of the Board as to credibility and the interpretation and assessment of evidence are all reviewable on a standard of reasonableness (Lawal v Canada (Minister of Citizenship and Immigration), 2010 FC 558 at para 11; NOO v Canada (Minister of Citizenship and Immigration), 2009 FC 1045, [2009] FCJ No 1286 at para 38).

[13] The determinative issue in the present case was state protection. This is a determination of mixed fact and law, which is within the specialized expertise of the Board. As such, it is also reviewable on a standard of reasonableness (Zupko v Canada (Minister of Citizenship and Immigration), 2010 FC 1319 at para 5).

[14] As set out in Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, reasonableness requires consideration of the existence of justification, transparency, and intelligibility in the decision-making process. It is also concerned with whether the decision falls within a range of acceptable outcomes that are defensible in respect of the facts and law.
IV. Argument and Analysis
A. Did the Board Make an Unreasonable Credibility Finding?

[15] The Board found that there was no threat to the family from Michaela’s boyfriend, and even if the Board erred in this assessment they did not find, on a forward-looking basis, an objectively well-founded fear or harm or future risk. The Board based this first conclusion on its characterization of the evidence relating to the boyfriend as unreliable. Michaela testified that her boyfriend started hitting her when she declined to marry him, yet, this information was not provided in her Port of Entry (POE) interview or PIF. The prospective risk finding was based on a lack of persuasive evidence that the boyfriend had any kind of power or influence that would enable him to find out if any of the Applicants were to return to the Czech Republic.

[16] The Applicants submit that the Board erred in several regards. Firstly, the Board ought to have considered that the boyfriend has an interest in finding Michaela as he has enforceable rights and obligations to the child. Secondly, the Board erred in drawing a negative inference from Michaela’s inconsistent testimony regarding the abusive relationship. Thirdly, the Board erred in failing to explain why they ignored the evidence that the boyfriend had called her and threatened her in Canada.

[17] With respect, I find no reviewable error with respect to any of the above issues. The Board discussed the possibility of the boyfriend wanting to obtain custody of the child at the hearing. The below exchange illustrates that a potential custody battle is of no real concern to the Applicants:
Q: Okay. So now two parents have rights to the child, both the man and the woman but one of them, if they’re separated, usually one of them gets custody which means they get to care for them and keep them and raise them and so on and sometimes it takes a court to decide which parent gets to do that and sometimes it turns out the mom gets the child and the dad is supposed to support with some finances and gets to see the child once in a while and sometimes it’s the other way around.
So is there a court in the Czech Republic that you can or your daughter can go and do that? If you know.
A: Yes, it’s possible but this child doesn’t have the father’s name and he is not in the birth certificate as a child. (CTR pg 602)

[18] In terms of credibility findings, it is open and reasonable, and is in fact a well-accepted and standard practice, for the Board to base credibility findings on omissions and inconsistencies between POE notes, PIFs and a claimant’s testimony at the hearing. The Respondent provided, and I accept, a concise statement of the law on PIF omissions by way of Justice Max Teitelbaum writing in Basseghi v Canada (Minister of Citizenship and Immigration), 52 ACWS (3d) 165, [1994] FCJ No. 1867 (QL) at para 33:

[33] It is not incorrect to say that answers given in a PIF should be brief but it is incorrect to say that the answers should not be complete with all of the relevant facts. It is not enough for an applicant to say that what he said in oral testimony was an elaboration. All relevant and important facts should be included in one's PIF. The oral evidence should go on to explain the information contained in the PIF.

[19] The Board explicitly considered the Gender Guidelines in relation to Michaela’s evidence and stated at para 11 of the reasons:
while I certainly accept and understand that some women might not reveal the existence of abuse in their relationship immediately, in this case reviewing as a whole the notes taken when she first made her claim for protection reveals a different story.

[20] At the POE Michaela would not reveal her boyfriend’s name because she did not want to get him into trouble with the Czech authorities. She claimed not to know his last name or what he did for a living. She claimed he had lost interest in her. Michaela’s story changed at the hearing. The Board was entitled to draw a negative credibility inference and this Court must uphold that finding as long as it is reasonable. I find that it is.

[21] The Board did consider the threatening telephone call in the reasons, mentioning it explicitly at para 14. The Board does not debate its existence. The Board was nevertheless not convinced that the boyfriend posed a risk of prospective harm to the family. Based on the evidence, this was a reasonable finding.

[22] As the Respondent submits, the Applicants’ submissions with respect to the credibility findings are nothing more than an invitation for this Court to reweigh evidence that has already been reasonably assessed by the Board. Consequently, I must refuse the invitation to invent an alternative line of reasoning as that falls outside the scope of this Court’s duty upon judicial review.
B. Did the Board Err in its Analysis of State Protection?

[23] The determinative issue in this claim for protection was state protection. The Board found that the Applicants did not provide clear and convincing evidence that adequate state protection would not be forthcoming should they need it.

[24] The Applicants submit that the Board applied the incorrect test and erred in finding that the Applicants had not rebutted the presumption. In their written submissions the Applicants support these contentions with long excerpts of case law.

[25] I accept the Respondent’s submissions on this point. The Board applied the correct test. This Court has recently and repeatedly confirmed the Federal Court of Appeal’s ruling in Carillo v Canada (Minister of Citizenship and Immigration), 2008 FCA 94, 69 Imm LR (3d) 309 that that the test for a finding of state protection is whether that protection is adequate, not whether it is effective, per se. This was observed by Justice Richard Mosley in Flores v Canada (Minister of Citizenship and Immigration), 2008 FC 723 wherein he also commented that, “It is not enough for a claimant merely to show that his government has not always been effective at protecting persons in his particular situation” (at para 10).

[26] The Board is not obliged to prove that the Czech Republic can offer the Applicant effective state protection, rather, the Applicant bears the legal burden of rebutting the presumption that adequate state protection exists by adducing clear and convincing evidence which satisfies the Board on a balance of probabilities (Carillo, above, at para 30). The quality of the evidence will be proportional to the level of democracy of the state (Avila v Canada (Minister of Citizenship and Immigration), 2006 FC 359, 295 FTR 35 at para 30).

[27] The Board undertook a detailed consideration of the Czech Republic’s current efforts to protect the Roma. The Board noted that there are concerns that these efforts are not adequate but that the preponderance of the evidence indicates that the state is taking action against extremists and does not condone or acquiesce to extremist actions, and those actions are effective. The Board further notes that discrimination against the Roma in the Czech Republic is prevalent. However, that Czech Republic was taking steps to assist the Roma in several ways to ensure that they would be able to participate in Czech society. Among these initiatives was the establishment of an agency to combat the social exclusion experienced by the Roma and improve socio-economic conditions through improved access to employment and mainstream education.

[28] The Applicants did not provide any clear and convincing evidence that the Czech Republic continues to be unable or unwilling to protect them. In fact, the father recounted an incident in his PIF where the police told a family that was harassing the Applicants “to be grateful that the Kaleja family was not pressing charges and prosecuting the case.” The father goes on to say that they were afraid of pressing charges because they feared retaliation. However, unwillingness to access state protection is not a basis for proving that it does not exist.

[29] I find that the Board’s finding of fact regarding state protection in the Czech Republic was reasonable, and established that state protection, while at times ineffective, was adequate.
C. Did the Board Ignore the Applicants’ Claim of Cumulative Persecution?

[30] The Applicants submit that the Board erred in its analysis by not considering the effects of cumulative persecution. I do not find this argument persuasive. The doctrine of cumulative persecution allows for the possibility that non-persecutory actions may accumulate and give rise to a well-founded fear of persecution. In the present matter, there was never any dispute that the harassment and discrimination suffered by the Applicants amounted to persecution due to their ethnicity. The Board did not find otherwise. What the Board did find, and what disposed of the Applicants’ claim, was that the state was able to offer them adequate protection.

[31] The Applicants relied on Munderere v Canada (Minister of Citizenship and Immigration), 2008 FCA 84, 291 DLR (4th) 68 in making the cumulative persecution argument. However, as the Respondent submits, Munderere has the effect of reaffirming that, as the Board determined in the instant matter, the availability of state protection is key for determining whether the claimant has a well-founded fear of persecution. The Court stated at para 45:

[45] The plain fact is that whether a claimant relies on a single or a number of events taken together, he still has the obligation to satisfy the Board that, at the time of the hearing, he has a well founded fear of persecution in regard to the country from which he seeks protection. He has to show that by reason of a Convention ground, he is unable or unwilling to avail himself of the protection of that country. Thus, in the present matter, are the respondents unable or unwilling to avail themselves of the protection of Rwanda or, to put it in a different way, is Rwanda able to protect the respondents should they return?
D. Did the Board Err in Failing to Conduct a Separate Section 97 Analysis?

[32] The substance of the Board’s section 97 analysis reads as follows:
There was no residual information upon which a claim under this section could be determined that was not already considered above. Therefore, I find that claimants are not persons in need of protection and their claims under section 97 of the IRPA fail.

[33] The Applicant submits that claimants are entitled to a separate section 97 analysis if there is credible evidence.

[34] The jurisprudence on this issue is mixed, but, as per Justice Mosley at para 22 of Soleimanian v Canada (Minister of Citizenship and Immigration), 2004 FC 1660, 135 ACWS (3d) 474:

[22] This Court seems to have come to a consensus that a separate section 97 analysis is not required if there is no evidence that could go to establishing that the person is in need of protection […]

[35] In that case, the Court found that there was no other evidence before the Board that the claimant was a person in need of protection. Similarly, in the present matter the Applicants section 97 claim rested entirely upon their assertion that they would be persecuted for being Roma. The only alternative basis upon which the Board might have determined that the Applicants were in need of protection under section 97 was their fear of Michaela’s former boyfriend. However, a negative credibility finding in relation to a section 96 claim obviates the need to consider it under section 97 (Mejia v Canada (Minister of Citizenship and Immigration), 2010 FC 410). Evidence for both sections was the same, co-mingled and intended to support either finding, but was found to be insufficient to do so.
V. Conclusion

## 20051:4 · paragraphs 40-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e2786cffa71a8dc8ab2ef3bf7e198815e52000f7dd86a924b31a3bd1fd0e33fa`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:4:subtheme:1 · paragraphs 40-41

- Raw key terms: `above, applicant, application, behalf, broad, case, cases, certification`
- Display key terms: `above, behalf, broad, case, cases, certification`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: above, behalf, broad, case, cases, certification Position/evidence statements: v McDougall case that dealt with standard of proof required in civil cases and the requirement for an applicant to submit "clear and convincing evidence" in order to rebut the presumption of state protection and as such  Operative outcome context: [37] In consideration of the above conclusions, this application for judicial review is dismissed. Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4948299` offsets `54-62`; context: [36] Counsel for the Applicant proposed the following question for certification:
In light of F.
- Evidence: `party_position` cue `submit` at chunk `4948299` offsets `591-597`; context: v McDougall case that dealt with standard of proof required in civil cases and the requirement for an applicant to submit "clear and convincing evidence" in order to rebut the presumption of state protection and as such find that the suggested question does not raise an issue of broad significance.
- Evidence: `evidence_fact` cue `evidence` at chunk `4948299` offsets `165-173`; context: v McDougall, 2008 SCC 53, has the test for "clear and convincing" evidence been removed in relation to the quality of evidence required to rebut the presumption of state protection?
- Evidence: `disposition` cue `dismissed` at chunk `4948300` offsets `88-97`; context: [37] In consideration of the above conclusions, this application for judicial review is dismissed.

#### Section text

[36] Counsel for the Applicant proposed the following question for certification:
In light of F.H. v McDougall, 2008 SCC 53, has the test for "clear and convincing" evidence been removed in relation to the quality of evidence required to rebut the presumption of state protection?
I have reviewed the written submissions made on behalf of the Applicant and the Respondent and find that the above noted question should not be certified. I see no inconsistency between the F.H. v McDougall case that dealt with standard of proof required in civil cases and the requirement for an applicant to submit "clear and convincing evidence" in order to rebut the presumption of state protection and as such find that the suggested question does not raise an issue of broad significance.

[37] In consideration of the above conclusions, this application for judicial review is dismissed.


## 20051:5 · paragraphs 42-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a780d719f5eced75812b4aae2054b26167a47ac9502c4ff97699f229850754ad`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:5:subtheme:1 · paragraphs 42-43

- Raw key terms: `application, cause, court, date, dismissed, docket, february, federal`
- Display key terms: `date, dismissed, february, federal`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: date, dismissed, february, federal Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is dismissed. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4948300` offsets `178-187`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed.
“ D. G. Near ”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4106-10
STYLE OF CAUSE: KALEJA ET AL. v. MCI
PLACE OF HEARING: TORONTO
DATE OF HEARING: FEBRUARY 17, 2011
REASONS FOR 

## 20051:6 · paragraphs 44-44

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `93de5386ec84addcc229219a4bc39dae14a7351659b8a1baeabd814a7fd4c994`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20051:6:subtheme:1 · paragraphs 44-44

- Raw key terms: `alex, appearances, applicants, attorney, barrister, canada, crane, dated`
- Display key terms: `alex, barrister, crane, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alex, barrister, crane, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 44-44. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT BY: NEAR J.
DATED: JUNE 9, 2011
APPEARANCES:
Micheal Crane
FOR THE APPLICANTS
Alex Kam
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Michael Crane
Barrister & Solicitor
Toronto, Ontario
FOR THE APPLICANTS
Myles J. Kirvan
Deputy Attorney General Canada
FOR THE RESPONDENT
