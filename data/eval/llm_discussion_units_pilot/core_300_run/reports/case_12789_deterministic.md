# Discussion Units: case 12789

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **3**
- Paragraph source hashes: **30**
- Sub-themes: **9**

## 12789:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `57a4e1bcfc204854efcb2a3f80e3c59e8ff59f164a9c078b9cc433e6a5c609c7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12789:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, application, decision, hongxin, immigration, reasons, alleges, authorities`
- Display key terms: `hongxin, alleges, authorities`
- Argument roles: `disposition, reasoning_application`
- Explanation: Observed roles: disposition, reasoning_application Display terms: hongxin, alleges, authorities Application context: [2] For the reasons set out below, I find that this application ought to be granted. Operative outcome context: [2] For the reasons set out below, I find that this application ought to be granted. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `I find` at chunk `4635431` offsets `35-41`; context: [2] For the reasons set out below, I find that this application ought to be granted.
- Evidence: `disposition` cue `granted` at chunk `4635431` offsets `76-83`; context: [2] For the reasons set out below, I find that this application ought to be granted.

#### Section text

Sun v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-03-27
Neutral citation
2015 FC 387
File numbers
IMM-8088-13
Decision Content
Date: 20150327
Docket: IMM-8088-13
Citation: 2015 FC 387
Ottawa, Ontario, March 27, 2015
PRESENT: The Honourable Mr. Justice de Montigny
BETWEEN:
HONGXIN SUN
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application for leave and judicial review of a decision rendered November 13, 2013 by the Immigration and Refugee Board, Refugee Protection Division (the Board) rejecting the refugee claim of Hongxin Sun (the Applicant) for lack of credibility. The Applicant alleges that he faces persecution by the Chinese authorities due to his Christian faith and membership in an underground Protestant church.

[2] For the reasons set out below, I find that this application ought to be granted.


## 12789:2 · paragraphs 3-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `df5d823aeae81b75c681939cda19a1fed593e7b0ab1859e9890e1ea63e891bfb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12789:2:subtheme:1 · paragraphs 3-8

- Raw key terms: `applicant, claims, alleges, church, friend, stomach, told, underground`
- Display key terms: `claims, alleges, church, friend, stomach, told, underground`
- Argument roles: `counterargument_limitation, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, party_position, reasoning_application Display terms: claims, alleges, church, friend, stomach, told, underground Position/evidence statements: [4] The Applicant claims that he had been suffering from stomach problems that worsened in March 2010, despite medical treatment. | He claims that in the following month, Liang Wang prayed for him and his condition improved until mid-May 2010, when his stomach pain disappeared. Application context: [7] On June 26, 2011, the Applicant alleges that the underground church was raided by the Chinese Public Service Bureau (PSB), but that they were warned by a lookout and he was therefore able to escape and hide at a frie Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4635432` offsets `18-24`; context: [4] The Applicant claims that he had been suffering from stomach problems that worsened in March 2010, despite medical treatment.
- Evidence: `party_position` cue `claims` at chunk `4635433` offsets `217-223`; context: He claims that in the following month, Liang Wang prayed for him and his condition improved until mid-May 2010, when his stomach pain disappeared.
- Evidence: `party_position` cue `claims` at chunk `4635434` offsets `155-161`; context: He claims that he introduced his friend De Cai Liu to the faith, who joined the church in January 2011.
- Evidence: `party_position` cue `claims` at chunk `4635435` offsets `364-370`; context: The Applicant claims that the PSB returned to his house to arrest him a total of seven more times, showing his wife a warrant for his arrest on October 11, 2011.
- Evidence: `reasoning_application` cue `therefore` at chunk `4635435` offsets `177-186`; context: [7] On June 26, 2011, the Applicant alleges that the underground church was raided by the Chinese Public Service Bureau (PSB), but that they were warned by a lookout and he was therefore able to escape and hide at a friend’s house.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635436` offsets `1000-1003`; context: The impugned decision [9] The Board accepted that the Applicant had suffered from stomach problems, but stated that it “believes very little if anything else the claimant had to say with respect to his allegations of persecution in China”.

#### 12789:2:subtheme:2 · paragraphs 9-13

- Raw key terms: `applicant, board, found, explanation, noted, although, arrest, evidence`
- Display key terms: `explanation, noted, although, arrest`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: explanation, noted, although, arrest Position/evidence statements: The Board also found that it was entitled to import a negative credibility finding into a claimant’s refugee “sur place” claim, and that his attendance at a Canadian church was likely intended to bolster his claim. | [14] In addition, the Board found that the Applicant’s explanation for why he did not claim in the US unsatisfactory, noting that the Applicant was aware of the American refugee process and would not have missed the oppo Evidence spans paragraphs 9-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4635437` offsets `440-446`; context: The Board noted the following inconsistencies and implausibilities in his testimony:
When asked why Liang Wang only introduced him to Jesus Christ in April 2010 when he had been aware of the Applicant’s health issues for about a year, the Applicant’s answer was evasive and unsatisfactory.
- Evidence: `evidence_fact` cue `testimony` at chunk `4635437` offsets `304-313`; context: The Board noted the following inconsistencies and implausibilities in his testimony:
When asked why Liang Wang only introduced him to Jesus Christ in April 2010 when he had been aware of the Applicant’s health issues for about a year, the Applicant’s answer was evasive and unsatisfactory.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4635437` offsets `838-846`; context: Although the Applicant stated that he was introduced to Jesus Christ in mid-May 2010 and cured around the same time (instantaneous recovery), he also said that he was cured when he and his friends prayed every day for him (gradual recovery).
- Evidence: `issue` cue `question` at chunk `4635438` offsets `493-501`; context: Although the Applicant said that he misunderstood the question, thinking that the Board was asking whether the police had an arrest warrant the first time they came to his house, the Board found that the question was clear and that this explanation was insufficient.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635438` offsets `78-86`; context: [11] The Board went on to note that the Applicant had provided no independent evidence to corroborate his testimony.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635438` offsets `198-201`; context: Concerning the copy of the arrest warrant, the Board found that it was possible, but unlikely given the country condition documentation, that the PSB would refuse to give his wife a copy of the arrest warrant.
- Evidence: `party_position` cue `claim` at chunk `4635439` offsets `376-381`; context: The Board also found that it was entitled to import a negative credibility finding into a claimant’s refugee “sur place” claim, and that his attendance at a Canadian church was likely intended to bolster his claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635439` offsets `130-138`; context: [12] With respect to his attendance and baptism at a Christian church in Canada, the Board noted that the Applicant had presented evidence of his attendance but that attendance did not demonstrate that the Applicant was truly a person of Christian faith.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635439` offsets `157-160`; context: [12] With respect to his attendance and baptism at a Christian church in Canada, the Board noted that the Applicant had presented evidence of his attendance but that attendance did not demonstrate that the Applicant was truly a person of Christian faith.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4635440` offsets `352-360`; context: Although recognizing that bribery is prevalent in China, the Board did not accept the explanation that the smuggler had bribed a customs agent, noting that if the PSB had been so intent on arresting him, then he would have been arrested regardless of a single bribe.
- Evidence: `party_position` cue `claim` at chunk `4635441` offsets `86-91`; context: [14] In addition, the Board found that the Applicant’s explanation for why he did not claim in the US unsatisfactory, noting that the Applicant was aware of the American refugee process and would not have missed the opportunity to claim asylum if he truly had a subjective fear of persecution.
- Evidence: `evidence_fact` cue `found that` at chunk `4635441` offsets `28-38`; context: [14] In addition, the Board found that the Applicant’s explanation for why he did not claim in the US unsatisfactory, noting that the Applicant was aware of the American refugee process and would not have missed the opportunity to claim asylum if he truly had a subjective fear of persecution.

#### 12789:2:subtheme:3 · paragraphs 14-18

- Raw key terms: `board, applicant, christ, evidence, claimant, credibility, cured, fact`
- Display key terms: `christ, credibility, cured, fact`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: christ, credibility, cured, fact Rule/authority context: Analysis [17] The standard of review with respect to credibility findings of the Board is undoubtedly reasonableness: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732, at para 4, 160 NR 315 (F Application context: The Board found it therefore possible, but unlikely, that an underground church raid would take place in Jilin. | So, this was gradual and not instantaneous because it was accomplished through a daily regiment of prayers. Evidence spans paragraphs 14-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4635442` offsets `377-382`; context: Issue [16] This matter raises only one issue: Is the Board’s credibility finding reasonable?
- Evidence: `evidence_fact` cue `found that` at chunk `4635442` offsets `110-120`; context: [15] The Board also considered the country condition documentation on persecution of Christians in China, and found that incidents were rare and exceptional in Jilin province, and that there was no evidence of prosecutions for proselytizing in Jilin province.
- Evidence: `governing_rule` cue `standard of review` at chunk `4635442` offsets `492-510`; context: Analysis [17] The standard of review with respect to credibility findings of the Board is undoubtedly reasonableness: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732, at para 4, 160 NR 315 (FCA); Tomic v Canada (Minister of Citizenship and Immigration), 2015 FC 126, at para 21.
- Evidence: `reasoning_application` cue `therefore` at chunk `4635442` offsets `279-288`; context: The Board found it therefore possible, but unlikely, that an underground church raid would take place in Jilin.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635442` offsets `299-302`; context: The Board found it therefore possible, but unlikely, that an underground church raid would take place in Jilin.
- Evidence: `issue` cue `whether` at chunk `4635443` offsets `186-193`; context: In fact, the Board had serious doubts as to whether the Applicant was miraculously cured as a result of his belief in Jesus Christ, and this skepticism pervades the whole decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635443` offsets `517-520`; context: To be sure, the Board did note, at paragraph 16 of its reasons, that “it may not be significant whether or not it was the medicine or the prayers that contributed to the claimant’s alleged cure but that he ‘believes’ [panel’s emphasis] he was cured by prayers”.
- Evidence: `evidence_fact` cue `record` at chunk `4635444` offsets `151-157`; context: Yet a careful reading of the record shows that the Applicant never said he was introduced to Christ in May 2010.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635446` offsets `244-252`; context: But according to the evidence before the panel it was not instantaneous healing for he said “I took no more medication, every day I pray, my friends prayed and there was no more stomach pain”.
- Evidence: `reasoning_application` cue `because` at chunk `4635446` offsets `459-466`; context: So, this was gradual and not instantaneous because it was accomplished through a daily regiment of prayers.

#### 12789:2:subtheme:4 · paragraphs 19-20

- Raw key terms: `agree, applicant, believe, believed, board, irrelevant, recovery, religious`
- Display key terms: `agree, believe, believed, irrelevant, recovery, religious`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: agree, believe, believed, irrelevant, recovery, religious Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4635447` offsets `67-74`; context: [21] I agree with counsel for the Applicant that it was irrelevant whether the “miracle” of the Applicant’s cure actually occurred.
- Evidence: `issue` cue `issues` at chunk `4635448` offsets `978-984`; context: Inconsistencies in the evidence must be sufficiently serious and must concern matters sufficiently relevant to the issues being adjudicated to warrant an adverse credibility finding: Djama v Canada (Minister of Employment and Immigration), [1992] FCJ No 531; Menjivar v Canada (Minister of Citizenship and Immigration), 2006 FC 11, at para 26.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635448` offsets `886-894`; context: Inconsistencies in the evidence must be sufficiently serious and must concern matters sufficiently relevant to the issues being adjudicated to warrant an adverse credibility finding: Djama v Canada (Minister of Employment and Immigration), [1992] FCJ No 531; Menjivar v Canada (Minister of Citizenship and Immigration), 2006 FC 11, at para 26.

#### 12789:2:subtheme:5 · paragraphs 21-22

- Raw key terms: `accept, analysis, applicant, belief, board, fact, find, found`
- Display key terms: `accept, analysis, belief, fact, find`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: accept, analysis, belief, fact, find Application context: The Board faulted the Applicant because he only mentioned in his oral testimony, in answer to a question from the Board, that De Cai Liu suffered from depression. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4635449` offsets `215-223`; context: The Board faulted the Applicant because he only mentioned in his oral testimony, in answer to a question from the Board, that De Cai Liu suffered from depression.
- Evidence: `evidence_fact` cue `testimony` at chunk `4635449` offsets `63-72`; context: [23] The same goes for the Board’s analysis of the Applicant’s testimony regarding his friend De Cai Liu’s conversion.
- Evidence: `reasoning_application` cue `because` at chunk `4635449` offsets `151-158`; context: The Board faulted the Applicant because he only mentioned in his oral testimony, in answer to a question from the Board, that De Cai Liu suffered from depression.
- Evidence: `evidence_fact` cue `testimony` at chunk `4635450` offsets `60-69`; context: [24] Overall, the Board’s reasons regarding the Applicant’s testimony are replete with sarcasm and unduly focus on insignificant and irrelevant inconsistencies.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4635450` offsets `312-320`; context: Although I am prepared to accept that the Applicant sometimes gave confused responses to questions put to him by the Board, I am concerned that the Board’s analysis was coloured by its skepticism with respect to the Applicant’s allegation that he was miraculously cured.

#### 12789:2:subtheme:6 · paragraphs 23-26

- Raw key terms: `applicant, board, country, evidence, possible, respect, across, arrest`
- Display key terms: `country, possible, respect, across, arrest`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: country, possible, respect, across, arrest Rule/authority context: It should also be noted that the United States is a designated country under section 101(1)(e) of the Immigration and Refugee Protection Act, SC 2001, c 27 (see Immigration and Refugee Protection Regulations, SOR/2002-22 Application context: In light of the fact that the Board itself recognized that bribery is prevalent and that it is possible that information would not be effectively shared, the Board was not entitled to conclude that the Applicant’s story  | The Board could reasonably conclude that incidents in Jilin were rare and on the low end of the spectrum within China, and that it was possible but unlikely that a church raid would occur there. Evidence spans paragraphs 23-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4635451` offsets `502-507`; context: It is true that the Response to Information Request on arrest warrants and summonses quoted by the Board indicates that the PSB normally delivers a summons to the person, that the Procuratorate will issue an arrest warrant after the PSB has investigated the case and has evidence that the suspect committed the crime, and that it is possible to obtain a copy of these documents by request to the PSB.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635451` offsets `574-582`; context: It is true that the Response to Information Request on arrest warrants and summonses quoted by the Board indicates that the PSB normally delivers a summons to the person, that the Procuratorate will issue an arrest warrant after the PSB has investigated the case and has evidence that the suspect committed the crime, and that it is possible to obtain a copy of these documents by request to the PSB.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635452` offsets `1746-1754`; context: It was equally entirely speculative to find that the Applicant could not plausibly have travelled through China to apply for a US visa without being detected; this finding does not rest on any evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4635452` offsets `1501-1509`; context: In light of the fact that the Board itself recognized that bribery is prevalent and that it is possible that information would not be effectively shared, the Board was not entitled to conclude that the Applicant’s story is implausible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635453` offsets `75-83`; context: [27] I have similar concerns with respect to the Board’s assessment of the evidence concerning the frequency of acts of persecution towards Christians in Jilin province.
- Evidence: `reasoning_application` cue `conclude` at chunk `4635453` offsets `197-205`; context: The Board could reasonably conclude that incidents in Jilin were rare and on the low end of the spectrum within China, and that it was possible but unlikely that a church raid would occur there.
- Evidence: `counterargument_limitation` cue `but` at chunk `4635453` offsets `314-317`; context: The Board could reasonably conclude that incidents in Jilin were rare and on the low end of the spectrum within China, and that it was possible but unlikely that a church raid would occur there.
- Evidence: `governing_rule` cue `under` at chunk `4635454` offsets `584-589`; context: It should also be noted that the United States is a designated country under section 101(1)(e) of the Immigration and Refugee Protection Act, SC 2001, c 27 (see Immigration and Refugee Protection Regulations, SOR/2002-227, s 159.
- Evidence: `reasoning_application` cue `therefore` at chunk `4635454` offsets `750-759`; context: 3), and therefore claimants arriving through the US are not normally eligible for referral to the Board.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4635454` offsets `184-192`; context: Although refugee claimants are not obliged to seek asylum in the first country they enter after flight, the failure to claim is considered a relevant consideration to impugn the credibility of a claimant, provided it is not the sole basis of the credibility finding (Gavryushenko v Canada (MCI), [2000] FCJ No 1209, at para 11).

#### 12789:2:subtheme:7 · paragraphs 27-28

- Raw key terms: `place, accordingly, acquired, analysis, another, applicant, application, appraisal`
- Display key terms: `place, accordingly, acquired, analysis, another, appraisal`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: place, accordingly, acquired, analysis, another, appraisal Position/evidence statements: [29] As for the Board’s assessment of the Applicant’s sur place claim, the Board was certainly entitled to import its credibility findings to determine the bona fide of that claim. Application context: Conclusion [30] For all of the foregoing reasons, I find that this application for judicial review must be granted. Operative outcome context: Conclusion [30] For all of the foregoing reasons, I find that this application for judicial review must be granted. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4635455` offsets `591-599`; context: The problem here is that the findings of the Board with respect to the genuineness of the Applicant’s story are themselves open to question and are fraught with a number of deficiencies.
- Evidence: `party_position` cue `claim` at chunk `4635455` offsets `64-69`; context: [29] As for the Board’s assessment of the Applicant’s sur place claim, the Board was certainly entitled to import its credibility findings to determine the bona fide of that claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4635455` offsets `762-770`; context: In such a context, the inference drawn by the Board is unwarranted and it would be unreasonable to assume that the evidence relating to the Applicant’s knowledge of Christianity and to his attendance of a church in Canada was fabricated in order to bolster his refugee claim.
- Evidence: `reasoning_application` cue `I find` at chunk `4635455` offsets `976-982`; context: Conclusion [30] For all of the foregoing reasons, I find that this application for judicial review must be granted.
- Evidence: `counterargument_limitation` cue `however` at chunk `4635455` offsets `1368-1375`; context: In the case at bar, however, the country condition evidence is far from compelling one way or another, and the appraisal of the situation on the ground cannot be totally divorced from the assessment of the Applicant’s story.
- Evidence: `disposition` cue `granted` at chunk `4635455` offsets `1033-1040`; context: Conclusion [30] For all of the foregoing reasons, I find that this application for judicial review must be granted.

#### Section text

I. Facts [3] The Applicant is a citizen of the People’s Republic of China, and lived with his wife and son in the city of Yanji, in Jilin province.

[4] The Applicant claims that he had been suffering from stomach problems that worsened in March 2010, despite medical treatment. According to his medical records, the Applicant regularly consulted a gastroenterologist from July 2009 until March 2010, at which time he began consulting a Chinese traditional medicine specialist until April 17, 2010.

[5] The Applicant alleges that in mid-April 2010, his friend Liang Wang introduced him to Jesus Christ. Liang Wang told him that Jesus Christ cured his allergic asthma, gave him a Bible and showed him how to pray. He claims that in the following month, Liang Wang prayed for him and his condition improved until mid-May 2010, when his stomach pain disappeared. The Applicant claims that he then joined the same underground church that Liang Wang belonged to, attending his first service on May 23, 2010. He claims that he was baptized on December 25, 2010 when he received his first Holy Communion, and attended church services every week.

[6] The Applicant further alleges that he began to serve as a lookout for the underground church, and introduced the faith to close family and friends. He claims that he introduced his friend De Cai Liu to the faith, who joined the church in January 2011.

[7] On June 26, 2011, the Applicant alleges that the underground church was raided by the Chinese Public Service Bureau (PSB), but that they were warned by a lookout and he was therefore able to escape and hide at a friend’s house. The following day, the PSB allegedly came to his house to arrest him and questioned his family about his whereabouts. The Applicant claims that the PSB returned to his house to arrest him a total of seven more times, showing his wife a warrant for his arrest on October 11, 2011. His wife told him that three of the church members, including Liang Wang, had been arrested and detained. In his amended Personal Information Form (PIF), the Applicant added that his wife went to the PSB in November 2011 to request a copy of the arrest warrant, but that they had refused to provide a copy.

[8] The Applicant noted in his PIF that he had hired a smuggler to help him obtain a US visa and leave the country, and that he flew first to Seattle on September 17, 2011, and then crossed the border on foot, arriving in Vancouver on September 20, 2011. He filed his refugee claim on September 22, 2011. At the hearing, the Applicant explained that the smuggler made the arrangements for his US visa using his genuine passport, and that he attended an interview at the US Embassy in Beijing for that purpose. When asked how he managed to leave the country while an arrest warrant was issued against him, the Applicant said that the smuggler had bribed the customs agents. When asked why he had not claimed refugee status in the US, the Applicant answered that the smuggler had told him that his claim was more likely to succeed in Canada and that refugees were treated like prisoners in the US.
II. The impugned decision [9] The Board accepted that the Applicant had suffered from stomach problems, but stated that it “believes very little if anything else the claimant had to say with respect to his allegations of persecution in China”.

[10] First, the Board concluded that the Applicant had fabricated the entire story of the miraculous cure, his membership in the underground church and the subsequent raid and arrest, and that he was not a man of Christian faith. The Board noted the following inconsistencies and implausibilities in his testimony:
When asked why Liang Wang only introduced him to Jesus Christ in April 2010 when he had been aware of the Applicant’s health issues for about a year, the Applicant’s answer was evasive and unsatisfactory. When asked how he knew it was God that had cured him and not medicine, the Applicant stated that he had stopped his medication at that point and his friend’s prayers healed him. The Board found this answer to be unreasonably vague and evasive, and concluded that he “was not healed miraculously of any stomach ulcer”. Although the Applicant stated that he was introduced to Jesus Christ in mid-May 2010 and cured around the same time (instantaneous recovery), he also said that he was cured when he and his friends prayed every day for him (gradual recovery). When questioned about his wife’s reaction to these events, the Applicant said that his wife witnessed the miracle of his recovery and believed that God healed him, but that she did not accept religion and was an atheist. When questioned about De Cai Liu, the Applicant said that De Cai Liu was cured of depression by God, but this important element was not mentioned in the Applicant’s PIF. When asked why he thought De Cai Liu was convinced of the miracle of God, but his wife was not, the Applicant said he believed in freedom of religion and would not force his faith on his wife. The Board found that this explanation did not answer the question and was evasive. Although recognizing that the Applicant had some knowledge of God and the Bible, this was inconclusive with respect to practice in China since he had been attending a church in Canada since his arrival. The Board found there was no persuasive evidence that the Applicant was able to talk about the precepts of Christianity.

[11] The Board went on to note that the Applicant had provided no independent evidence to corroborate his testimony. Concerning the copy of the arrest warrant, the Board found that it was possible, but unlikely given the country condition documentation, that the PSB would refuse to give his wife a copy of the arrest warrant. The Board also noted that the Applicant had initially said that there was no arrest warrant issued against him. Although the Applicant said that he misunderstood the question, thinking that the Board was asking whether the police had an arrest warrant the first time they came to his house, the Board found that the question was clear and that this explanation was insufficient.

[12] With respect to his attendance and baptism at a Christian church in Canada, the Board noted that the Applicant had presented evidence of his attendance but that attendance did not demonstrate that the Applicant was truly a person of Christian faith. The Board also found that it was entitled to import a negative credibility finding into a claimant’s refugee “sur place” claim, and that his attendance at a Canadian church was likely intended to bolster his claim.

[13] Concerning the smuggling story, the Board found it unlikely that the Applicant would be able to travel within China and to leave the country on his own passport without a hitch while an arrest warrant was allegedly issued against him. The Board noted that the country condition documentation demonstrates that a national policing database exists. Although recognizing that bribery is prevalent in China, the Board did not accept the explanation that the smuggler had bribed a customs agent, noting that if the PSB had been so intent on arresting him, then he would have been arrested regardless of a single bribe.

[14] In addition, the Board found that the Applicant’s explanation for why he did not claim in the US unsatisfactory, noting that the Applicant was aware of the American refugee process and would not have missed the opportunity to claim asylum if he truly had a subjective fear of persecution.

[15] The Board also considered the country condition documentation on persecution of Christians in China, and found that incidents were rare and exceptional in Jilin province, and that there was no evidence of prosecutions for proselytizing in Jilin province. The Board found it therefore possible, but unlikely, that an underground church raid would take place in Jilin.
III. Issue [16] This matter raises only one issue: Is the Board’s credibility finding reasonable?
IV. Analysis [17] The standard of review with respect to credibility findings of the Board is undoubtedly reasonableness: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732, at para 4, 160 NR 315 (FCA); Tomic v Canada (Minister of Citizenship and Immigration), 2015 FC 126, at para 21.

[18] I agree with counsel for the Applicant that the credibility findings of the Board are tenuous and lack transparency and intelligibility. In fact, the Board had serious doubts as to whether the Applicant was miraculously cured as a result of his belief in Jesus Christ, and this skepticism pervades the whole decision. To be sure, the Board did note, at paragraph 16 of its reasons, that “it may not be significant whether or not it was the medicine or the prayers that contributed to the claimant’s alleged cure but that he ‘believes’ [panel’s emphasis] he was cured by prayers”. The problem is that the gist of the Board’s reasons is at odds with these cautionary words.

[19] First of all, the Board seems to be thinking that the Applicant suggested he was instantaneously healed in May 2010. Yet a careful reading of the record shows that the Applicant never said he was introduced to Christ in May 2010. He has consistently declared that he was introduced to Christ in April 2010, that he and his friend prayed regularly thereafter and that he accepted Christ when he recovered from his illness in mid-May 2010. He has always described the process as a gradual one, and so it seems to me that the Board’s finding on this point is unfounded on the evidence.

[20] The Board’s skepticism of the Applicant’s faith transpires in the following paragraph:

[15] For example, the claimant said that he was introduced to Christ in the middle of May 2010 and “in the middle of May 2010, I was no longer suffering from stomach pain anymore”. That has a ring of instantaneous healing. But according to the evidence before the panel it was not instantaneous healing for he said “I took no more medication, every day I pray, my friends prayed and there was no more stomach pain”. So, this was gradual and not instantaneous because it was accomplished through a daily regiment of prayers. There is no evidence before this panel how many prayers were prayed or how long a period they prayed, or that he had stopped taking his medication before the middle of May 2010. In fact, his testimony is that “At the time when my friend came and told me about God I stopped my medication…” In other words, he stopped taking his medicine in the middle of May and he got healing in the middle of May. If indeed the claimant was cured of his medical problems, he had no way of knowing that it was because of prayers and not the medicine that he had been taking, according to the evidence, right up to the middle of May which is when he said that he got healed. It is reasonable to believe that some medicine takes a longer period of time than others to work, as well, some may not work. So, the medicine could have just worked for him around the same time he stopped taking it and started prayer.

[21] I agree with counsel for the Applicant that it was irrelevant whether the “miracle” of the Applicant’s cure actually occurred. The Board may not have shared the Applicant’s belief that God was at the source of his medical recovery, but this does not mean that the Applicant does not sincerely believe it himself and is not a practicing Christian that may be subject to persecution. The Applicant explained that he stopped taking his medication in April 2010 and prayed, and that this was why he believed that God caused his recovery in May 2010. With respect, I fail to see how this explanation is vague or evasive. It clearly addressed the Board’s question, and it is not incoherent. It may not have been enough to convince the Board member to convert to Christianity himself, but that is not the point. A refugee claimant is evidently not required to prove divine intervention to demonstrate his fear of religious persecution, and it is not the Board’s role to make findings of fact on miracles.

[22] Similarly irrelevant are the religious beliefs of the Applicant’s wife. I agree that the Applicant’s answers regarding his wife’s beliefs were confusing. On the one hand, he maintained that his wife believed that God cured him, but that she was not interested in religion and that she was an atheist. When the Board asked how she could believe that God cured him and also be an atheist, he replied that she had witnessed his recovery and prayers, and that “she might assume it was God who cured me”. The Board was certainly entitled to find the Applicant’s explanations with respect to what his wife believed confusing and difficult to follow, and even contradictory. Yet the Applicant’s wife’s beliefs are irrelevant to the Applicant’s claim, and have no bearing on the Applicant’s own beliefs or the veracity of his allegations concerning the church raid. Inconsistencies in the evidence must be sufficiently serious and must concern matters sufficiently relevant to the issues being adjudicated to warrant an adverse credibility finding: Djama v Canada (Minister of Employment and Immigration), [1992] FCJ No 531; Menjivar v Canada (Minister of Citizenship and Immigration), 2006 FC 11, at para 26.

[23] The same goes for the Board’s analysis of the Applicant’s testimony regarding his friend De Cai Liu’s conversion. The Board faulted the Applicant because he only mentioned in his oral testimony, in answer to a question from the Board, that De Cai Liu suffered from depression. I fail to see why the Board found problematic the fact that he had not mentioned that detail in the narrative of his PIF; this was not a key fact related to the Applicant’s belief and the police raid. Furthermore, this omission was never put to the Applicant at the hearing. Moreover, it was totally inappropriate to query why the Applicant was able to convince De Cai Liu to accept Jesus Christ, but was not able to convince his wife, as these are personal matters that are beyond the Applicant’s control and have no bearing upon his own beliefs. Finally, I find the following comments totally unfitting and out of place:
The claimant testified that De Cai Liu was suffering from depression and had been to the doctors but they were unable to cure him as well (the doctors somehow couldn’t help Liang Wang of his asthma, couldn’t help De Cai Liu of his depression and couldn’t help the claimant of his ulcer). It would seem like very stubborn strains of different illnesses that seem to attack these individuals within the space of a few months. These illnesses required divine intervention as the doctors don’t seem to be able to help.

[24] Overall, the Board’s reasons regarding the Applicant’s testimony are replete with sarcasm and unduly focus on insignificant and irrelevant inconsistencies. The Board even went as far as drawing an adverse credibility inference from the fact that the Applicant said “first” twice when beginning his answers. Although I am prepared to accept that the Applicant sometimes gave confused responses to questions put to him by the Board, I am concerned that the Board’s analysis was coloured by its skepticism with respect to the Applicant’s allegation that he was miraculously cured. Instead of assessing the sincerity of the Applicant’s belief and the veracity of his story concerning the church raid, the Board gave undue weight to minor details, found inconsistencies in perceived discrepancies that were reasonably explained by the Applicant, and questioned his faith on the basis of other people’s behaviour for which he could not be held responsible. On that basis, I am prepared to find that the Board’s assessment of the Applicant’s credibility was flawed and lacked transparency and intelligibility.

[25] The Board also found, based on the country condition documentation, that it was more likely than not, that Chinese authorities would have provided a copy of a summons or arrest warrant on request, and that the failure to provide a copy of the arrest warrant suggested that it simply did not exist. It is true that the Response to Information Request on arrest warrants and summonses quoted by the Board indicates that the PSB normally delivers a summons to the person, that the Procuratorate will issue an arrest warrant after the PSB has investigated the case and has evidence that the suspect committed the crime, and that it is possible to obtain a copy of these documents by request to the PSB. Yet the same Response to Information Request also notes that there are discrepancies in the implementation of the law across the country. The Board was certainly entitled to disbelieve the Applicant’s allegation that his wife had asked for a copy of the arrest warrant but had been turned down, but it could not use the Response to Information Request as a basis for that conclusion without discussing the caveat with respect to the disparities in the enforcement of the law throughout the country. As for the contradiction found by the Board between what the Applicant wrote in his PIF (that his wife was shown a warrant but could not obtain a copy) and his testimony (where he apparently said that no warrant was issued), a careful reading of the transcript shows that the question was far from clear and that the Applicant genuinely misunderstood the question.

[26] The Board’s finding that it was implausible the Applicant would be able to leave China undetected on his own genuine passport while an arrest warrant was issued against him, especially after the PSB had allegedly visited his house eight times looking for him, is equally questionable. The Board based its finding mainly on a Response to Information Request reporting the existence and expansion of a national Chinese policing database used by the PSB and at ports of entry and exit of the country. The same document also mentions that challenges remain with respect to information sharing between regional police units, and the Board itself recognizes that there is wide administrative discretion across the county and that bribery is prevalent in China. It is well established that implausibility findings may only be made in the “clearest of cases” (Valtchev v Canada (Minister of Citizenship and Immigration), 2001 FCT 776, at para 7), where “the facts as presented are either so far outside the realm of what could reasonably be expected that the trier of fact can reasonably find that it could not possibly have happened” (Lorne Waldman, Immigration Law and Practice (Markham, ON: Butterworths, 1992), s 8.22, cited in Divsalar v Canada (Minister of Citizenship and Immigration), 2002 FCT 653, at para 24). In light of the fact that the Board itself recognized that bribery is prevalent and that it is possible that information would not be effectively shared, the Board was not entitled to conclude that the Applicant’s story is implausible. It was equally entirely speculative to find that the Applicant could not plausibly have travelled through China to apply for a US visa without being detected; this finding does not rest on any evidence.

[27] I have similar concerns with respect to the Board’s assessment of the evidence concerning the frequency of acts of persecution towards Christians in Jilin province. The Board could reasonably conclude that incidents in Jilin were rare and on the low end of the spectrum within China, and that it was possible but unlikely that a church raid would occur there. The Board nevertheless recognizes that there are statements in the China Aid Association Report, upon which it relies, to the effect that reported incidents should not be confused with actual incidents, and that the reported events represent only the tip of the iceberg. Accordingly, the documentary evidence may not add weight to the Applicant’s testimony or prove that the church raid occurred, but it could not be used to doubt the objective veracity of the Applicant’s fear of 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 12789:3 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `19a8af6de2af9dc8ac2066869e0f44be7f3feaa4dd38991d2e782b0bfa22fd93`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12789:3:subtheme:1 · paragraphs 29-29

- Raw key terms: `appearances, applicant, attorney, barrister, canada, crawford, dated, deputy`
- Display key terms: `barrister, crawford, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, crawford, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
DE MONTIGNY J.
DATED:
march 27, 2015
APPEARANCES:
Ann Crawford
For The Applicant
Ildiko Erdei
For The Respondent
SOLICITORS OF RECORD:
Ann Crawford
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
