# Discussion Units: case 19705

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **55**
- Continuity pairs: **54**
- Discussion Units: **5**
- Paragraph source hashes: **55**
- Sub-themes: **18**

## 19705:1 · paragraphs 0-0

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `477892367a7f262fc41696473b545044d61c86bc08161f282e795276e20ff420`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19705:1:subtheme:1 · paragraphs 0-0

- Raw key terms: `adam, applicants, bleda, bledy, canada, citation, citizenship, content`
- Display key terms: `adam, bleda, bledy, citation, content`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adam, bleda, bledy, citation, content No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 0-0. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

Bledy v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-02-22
Neutral citation
2011 FC 210
File numbers
IMM-3354-10
Decision Content
Federal Court
Cour fédérale
Date: 20110222
Docket: IMM-3354-10
Citation: 2011 FC 210
Ottawa, Ontario, February 22, 2011
PRESENT: The Honourable Mr. Justice Scott
BETWEEN:
JOSEF BLEDY
HELENA SAMKOVA
ADAM FRANTISEK BLEDY
JENIFER BLEDA
JOSEF BLEDY (JR)
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

## 19705:2 · paragraphs 1-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f9348ef8421ce2a33eec77a860e725509ae8d4c756539b622566635ea04c4cfa`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19705:2:subtheme:1 · paragraphs 1-8

- Raw key terms: `applicants, czech, applicant, board, claim, principal, republic, canada`
- Display key terms: `czech, principal, republic`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: czech, principal, republic Position/evidence statements: [4] The applicants claimed protection as convention refugees, alleging a well-founded fear of persecution in the Czech Republic based on their Roma ethnicity. | [5] In the principal applicant’s Personal Information Form (PIF), he alleged the following facts in support of his family’s claim: (a) In kindergarten, the principal applicant had been verbally harassed for being a Roma  Rule/authority context: [1] This is an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of the Refugee Protection Division of the Immigration and Re | Failing a successful claim under section 96 of the IRPA, the applicants also claimed protection under subsection 97(1) of the IRPA, based on their fear of being victims of further violence in the Czech Republic, as well  Application context: (c) The Czech students at the regular school would swear, demean and attack both the principal applicant and his spouse because they were Roma. | Second, the Board concluded that “some of the details surrounding the rape are inaccurate” and therefore gave “little weight to the statement that the rape occurred because the second claimant’s mother was of Roma ethnic Operative outcome context: (c) The principal applicant’s brother-in-law, Stefan, was attacked in the Czech Republic only three days after being returned home from Canada following a denied refugee claim. Evidence spans paragraphs 1-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4933799` offsets `28-39`; context: [1] This is an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board of Canada (Board), dated May 25, 2010, refusing the applicants’ claim for refugee protection after determining that they were neither convention refugees nor persons in need of protection.
- Evidence: `party_position` cue `claimed` at chunk `4933802` offsets `19-26`; context: [4] The applicants claimed protection as convention refugees, alleging a well-founded fear of persecution in the Czech Republic based on their Roma ethnicity.
- Evidence: `governing_rule` cue `under` at chunk `4933802` offsets `186-191`; context: Failing a successful claim under section 96 of the IRPA, the applicants also claimed protection under subsection 97(1) of the IRPA, based on their fear of being victims of further violence in the Czech Republic, as well as based on their assertion that they, as Romani citizens, would receive inadequate healthcare if returned to the Czech Republic.
- Evidence: `party_position` cue `claim` at chunk `4933803` offsets `124-129`; context: [5] In the principal applicant’s Personal Information Form (PIF), he alleged the following facts in support of his family’s claim:
(a) In kindergarten, the principal applicant had been verbally harassed for being a Roma child.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933803` offsets `2322-2330`; context: Despite having evidence (a description of the car and semen samples), and despite the applicants checking with the police on multiple occasions, the police never found the assailant.
- Evidence: `reasoning_application` cue `because` at chunk `4933803` offsets `530-537`; context: (c) The Czech students at the regular school would swear, demean and attack both the principal applicant and his spouse because they were Roma.
- Evidence: `party_position` cue `claim` at chunk `4933804` offsets `131-136`; context: [6] At the hearing before the Board, the principal applicant added the following additional allegations in support of his family’s claim:
(a) In 1992, when he was a young boy, his cousin was attacked and killed by skinheads.
- Evidence: `disposition` cue `denied` at chunk `4933804` offsets `692-698`; context: (c) The principal applicant’s brother-in-law, Stefan, was attacked in the Czech Republic only three days after being returned home from Canada following a denied refugee claim.
- Evidence: `evidence_fact` cue `testimony` at chunk `4933805` offsets `766-775`; context: This finding was due to a discrepancy between the principal applicant’s PIF and his testimony with regards to the number of attackers involved.
- Evidence: `reasoning_application` cue `therefore` at chunk `4933805` offsets `551-560`; context: Second, the Board concluded that “some of the details surrounding the rape are inaccurate” and therefore gave “little weight to the statement that the rape occurred because the second claimant’s mother was of Roma ethnicity”.

#### Section text

[1] This is an application, pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board of Canada (Board), dated May 25, 2010, refusing the applicants’ claim for refugee protection after determining that they were neither convention refugees nor persons in need of protection.

[2] For the reasons discussed below, I am allowing this application for judicial review.
Background

[3] Mr. Josef Bledy (the principal applicant) was born May 5, 1983 and is a citizen of the Czech Republic. He and his family (together, the applicants) – his common-law spouse, Helena Samkova (born October 10, 1983), his son, Josef Bledy Jr. (born June 10, 2002), his daughter, Jenifer Bledy (born February 3, 2004), and his son, Adam Frantisek Bledy (born September 24, 2008) – arrived in Canada on December 17, 2009 and claimed refugee protection on December 19, 2009.

[4] The applicants claimed protection as convention refugees, alleging a well-founded fear of persecution in the Czech Republic based on their Roma ethnicity. Failing a successful claim under section 96 of the IRPA, the applicants also claimed protection under subsection 97(1) of the IRPA, based on their fear of being victims of further violence in the Czech Republic, as well as based on their assertion that they, as Romani citizens, would receive inadequate healthcare if returned to the Czech Republic.

[5] In the principal applicant’s Personal Information Form (PIF), he alleged the following facts in support of his family’s claim:
(a) In kindergarten, the principal applicant had been verbally harassed for being a Roma child. He defended himself physically and was expelled.
(b) Both the principal applicant and his spouse received their education via “special” schools for children with mental disabilities.
(c) The Czech students at the regular school would swear, demean and attack both the principal applicant and his spouse because they were Roma. They complained to the teachers and director, but no action was taken.
(d) As a child, the principal applicant was prevented from participating in sports (hockey, soccer, karate) organized by his home municipality, because he attended a “special” school.
(e) Josef Jr. was also placed in a “special” school despite his parents’ attempts to register him in a regular school and despite the fact that his parents believed he had performed well on his entrance exams.
(f) The principal applicant was prevented from participating in a bricklayer apprenticeship due to insufficient education. Although he had been registered at the employment office since he was 15 years old, he had received only limited employment because of his poor schooling and his ethnicity.
(g) In August of 2005, while in Pisek to visit his aunt, the principal applicant and his cousin were attacked by 12 skinheads who yelled various racial slurs. They were kicked until the cousin had a concussion. The aunt called the police, but the police laughed at them and accused them of provoking the attack.
(h) In January of 2006, while at a disco in Protivin, the principal applicant and two cousins were attacked by a group of 30-40 skinheads. One cousin was stabbed, while the principal applicant and the other cousin had concussions and were bleeding. The other patrons at the disco did nothing to intervene. The police were called, but they accused the boys of provoking the skinheads. The police did not write up a report.
(i) In August of 2007, the principal applicant’s mother-in-law was raped and beaten by a man who swore at her using various racial slurs. She was left in the woods unconscious. The police laughed at her and suggested she made it up or that it was her fault. Despite having evidence (a description of the car and semen samples), and despite the applicants checking with the police on multiple occasions, the police never found the assailant.
(j) In December of 2007, the applicants were visiting their parents in Vimperk for Christmas. On Christmas day, their house was set on fire, but it was saved by firefighters. The next day, the basement was set on fire, it was again extinguished. On December 28th, the roof was set on fire and on the 29th, the whole roof burned down along with part of the house. Although the applicants did not see the attackers, they heard on the news that it was a “racist attack”. The applicants’ parents were given alternate temporary accommodations by the city. However, those alternate accommodations had no water, toilet, or bathroom.
(k) In November of 2008, the principal applicant, his spouse and her four cousins, were attacked by 6 skinheads with baseball bats while at a local pub celebrating the christening of Adam. Before fleeing the scene, the skinheads let off 5 pistol rounds as a warning. The police called an ambulance and left in pursuit of the attackers. Although the police took statements from the principal applicant and his family, the applicants never heard anything further about the investigation.

[6] At the hearing before the Board, the principal applicant added the following additional allegations in support of his family’s claim:
(a) In 1992, when he was a young boy, his cousin was attacked and killed by skinheads. Counsel for the applicants provided the Board with a video recording of a news report regarding the incident.
(b) The principal applicant’s eldest son was attacked on his first day of school by a group of 6 Czech boys. His son came home with a black eye, but the teacher said that his son had started the fight.
(c) The principal applicant’s brother-in-law, Stefan, was attacked in the Czech Republic only three days after being returned home from Canada following a denied refugee claim.
(d) There are skinheads among the Czech police. On one occasion, a police officer approached the principal applicant in the park and asked, “What are you black mug doing here?”
Impugned Decision

[7] The Board began its reasons by noting that it had “some credibility concerns.” First, it indicated that the principal applicant testified that he had suffered a concussion as a result of the attack in Pisek and that he had spent some time in hospital, whereas, in his PIF he did not mention that he was in hospital. The Board found this to be an embellishment and that the applicant was, in fact, never in hospital as a result of any skinhead attacks. Second, the Board concluded that “some of the details surrounding the rape are inaccurate” and therefore gave “little weight to the statement that the rape occurred because the second claimant’s mother was of Roma ethnicity”. This finding was due to a discrepancy between the principal applicant’s PIF and his testimony with regards to the number of attackers involved.

[8] The Board then went on to discuss “discrimination vs. persecution”. It acknowledged that Romani children in the Czech Republic are still “systematically turned away from regular schools” and sent to remedial schools that cater to developmental disabilities. It further acknowledged that these remedial schools provide substandard levels of education that do “not meet the minimum requirements for dignity.”

## 19705:3 · paragraphs 9-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9740e7a36288a2810de58011f28ddb25e4e6bfa3b3b6f5c8fa0666c611ce26f0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19705:3:subtheme:1 · paragraphs 9-15

- Raw key terms: `board, concluded, discrimination, persecution, acknowledged, against, applicant, applicants`
- Display key terms: `concluded, discrimination, persecution, acknowledged, against`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: concluded, discrimination, persecution, acknowledged, against Application context: Regarding the alleged fires during Christmas of 2007, the Board concluded that there was no persuasive evidence that the fires were set because the inhabitants were Roma. Evidence spans paragraphs 9-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4933807` offsets `702-717`; context: It also pointed to a decision of the European Court of Human Rights [ECHR] which determined that the Czech Republic had indirectly discriminated against certain students by placing them in remedial schools.
- Evidence: `evidence_fact` cue `found that` at chunk `4933808` offsets `215-225`; context: ” However, it found that since steps were being taken to deal with this discrimination, and since the ECHR decision meant that the applicants would have a remedy with regards to their eldest son’s placement, the Board concluded that the situation with respect to education did not rise to the level of persecution.
- Evidence: `counterargument_limitation` cue `However` at chunk `4933808` offsets `203-210`; context: ” However, it found that since steps were being taken to deal with this discrimination, and since the ECHR decision meant that the applicants would have a remedy with regards to their eldest son’s placement, the Board concluded that the situation with respect to education did not rise to the level of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933811` offsets `325-333`; context: Regarding the alleged fires during Christmas of 2007, the Board concluded that there was no persuasive evidence that the fires were set because the inhabitants were Roma.
- Evidence: `reasoning_application` cue `because` at chunk `4933811` offsets `358-365`; context: Regarding the alleged fires during Christmas of 2007, the Board concluded that there was no persuasive evidence that the fires were set because the inhabitants were Roma.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933812` offsets `370-378`; context: ” The Board indicated that the physical attacks on the applicants would be canvassed in the subsequent section on state protection and that; ultimately, there was no persuasive evidence of a sustained or systemic violation of basic human rights demonstrative of a failure of state protection.

#### 19705:3:subtheme:2 · paragraphs 16-17

- Raw key terms: `board, cases, concluded, evidence, found, noted, police, presumption`
- Display key terms: `cases, concluded, noted, police, presumption`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: cases, concluded, noted, police, presumption Application context: [16] On the issue of state protection, the Board found that because the Czech Republic is a democracy, the presumption of state protection is strong. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933814` offsets `12-17`; context: [16] On the issue of state protection, the Board found that because the Czech Republic is a democracy, the presumption of state protection is strong.
- Evidence: `evidence_fact` cue `found that` at chunk `4933814` offsets `49-59`; context: [16] On the issue of state protection, the Board found that because the Czech Republic is a democracy, the presumption of state protection is strong.
- Evidence: `reasoning_application` cue `because` at chunk `4933814` offsets `60-67`; context: [16] On the issue of state protection, the Board found that because the Czech Republic is a democracy, the presumption of state protection is strong.
- Evidence: `evidence_fact` cue `found that` at chunk `4933815` offsets `63-73`; context: [17] With respect to the 2006 incident at the disco, the Board found that it was apparent that the police investigated the situation and took statements from bystanders and concluded that no charges were to be laid.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4933815` offsets `722-730`; context: Although the applicants’ may not have been satisfied with the result, the Board found that they had not rebutted the presumption of state protection with clear and convincing evidence.

#### 19705:3:subtheme:3 · paragraphs 18-18

- Raw key terms: `applicants, board, claim, issues, protection, rejected, ultimately`
- Display key terms: `issues, protection, rejected, ultimately`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: issues, protection, rejected, ultimately Evidence spans paragraphs 18-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4933816` offsets `74-80`; context: Issues

#### Section text

[9] It then referred to a report from the Roma Education Fund which indicated there had been improvements in recent years: preparatory classes for children from difficult backgrounds, additional teachers’ assistants to work in schools that had a high proportion of Roma, free pre-school education, secondary school scholarships for Roma students, abolition of special-education schools, and increased government funding. The Board also referred to a government program entitled, “Reintegration of Roma Pupils”, the objective of which was to correct cases where Romani students were wrongfully placed in remedial schools. It also pointed to a decision of the European Court of Human Rights [ECHR] which determined that the Czech Republic had indirectly discriminated against certain students by placing them in remedial schools. The verdict obliged the Czech Republic to enact legislation prohibiting discrimination against Romani children in the education system.

[10] The Board acknowledged that the treatment of the applicants, in placing them in remedial schooling, was “obviously a form of discrimination along with the verbal insults and the physical assaults.” However, it found that since steps were being taken to deal with this discrimination, and since the ECHR decision meant that the applicants would have a remedy with regards to their eldest son’s placement, the Board concluded that the situation with respect to education did not rise to the level of persecution.

[11] Turning to the principal applicant’s difficulty in finding employment, the Board acknowledged that there may have been some discrimination.

[12] With respect to the allegation that the police had discriminated against the principal applicant by calling him names, the Board noted that this had only occurred once.

[13] The Board then considered two of the alleged assaults. Regarding the alleged attack in Pisek in 2005, the Board reiterated that it had “some concerns about the embellishment of the details” surrounding that incident. Regarding the alleged fires during Christmas of 2007, the Board concluded that there was no persuasive evidence that the fires were set because the inhabitants were Roma.

[14] The Board then indicated that the word “persecution” had been ascribed the meaning of “sustained or systemic violation of basic human rights demonstrative of a failure of state protection.” The Board indicated that the physical attacks on the applicants would be canvassed in the subsequent section on state protection and that; ultimately, there was no persuasive evidence of a sustained or systemic violation of basic human rights demonstrative of a failure of state protection.

[15] It concluded its analysis of persecution by stating: “I have also considered these matters singularly and cumulatively and find that they do not rise to the level of persecution in either instance.”

[16] On the issue of state protection, the Board found that because the Czech Republic is a democracy, the presumption of state protection is strong. The Board pointed to Czech legislation which provided protection for the Roma, including anti-discrimination and hate crimes legislation. It specifically pointed to reforms in the Czech police force: the introduction of Roma Police Assistants, the recruitment of Romani police officers, and the training of police on how to better interact with minorities. The Board also noted that the Czech judiciary had prosecuted a number of hate crimes committed against the Roma and that the number of such proceedings had increased in recent years. In addition to the police, the Board pointed to other avenues of assistance for the Romani: the Czech Ombudsman, the approximately 400 Romani NGOs, the Czech Trade Inspectorate, the Czech Helsinki Committee to investigate cases of police misconduct, and the Social Inclusion Agency. The Board concluded that the “preponderance of the documentary evidence indicates that the Czech Republic government is making very serious efforts to provide protection to the Roma whether as victims of hate crime, assist in obtaining health care or education, or inclusion into Czech society.”

[17] With respect to the 2006 incident at the disco, the Board found that it was apparent that the police investigated the situation and took statements from bystanders and concluded that no charges were to be laid. It found that it would be difficult to arrive at a clear picture of what occurred without any police reports or other statements. With respect to the incident at the pub in 2008, the Board noted that the police arrived and chased after the attackers. As such, the police did take some action. Furthermore, the police were actively involved in investigating the fires. On the whole, the Board concluded that in cases where the applicants asked for police help, there was evidence that the police responded. Although the applicants’ may not have been satisfied with the result, the Board found that they had not rebutted the presumption of state protection with clear and convincing evidence.

[18] Ultimately, the Board rejected the applicants’ claim for protection.
Issues

## 19705:4 · paragraphs 19-53

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d7b6ceb77cb97ac8d44bc7404e56b2e7c4679cbcdfef6487718b7fefb8f7b446`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19705:4:subtheme:1 · paragraphs 19-20

- Raw key terms: `court, persecution, protection, review, standard, state, above, acws`
- Display key terms: `persecution, protection, review, standard, state, above, acws`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: persecution, protection, review, standard, state, above, acws Rule/authority context: Standard of Review | It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 1 Application context: It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 1 Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4933817` offsets `9-15`; context: [19] The issues before the Court are the following:
(a) Did the Board err in finding that the applicants did not face persecution in the Czech Republic?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4933817` offsets `263-281`; context: Standard of Review
- Evidence: `issue` cue `issue` at chunk `4933818` offsets `453-458`; context: It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 168 ACWS (3d) 596 at paras 11-13.
- Evidence: `governing_rule` cue `standard of review` at chunk `4933818` offsets `418-436`; context: It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 168 ACWS (3d) 596 at paras 11-13.
- Evidence: `reasoning_application` cue `apply` at chunk `4933818` offsets `440-445`; context: It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 168 ACWS (3d) 596 at paras 11-13.

#### 19705:4:subtheme:2 · paragraphs 21-23

- Raw key terms: `applicants, board, persecution, analysis, czech, evidence, physical, republic`
- Display key terms: `persecution, analysis, czech, physical, republic`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: persecution, analysis, czech, physical, republic Position/evidence statements: [22] The applicants argue that the Board erred by not properly considering whether, cumulatively, the discrimination and the physical attacks they experienced in the Czech Republic constituted persecution. | [23] The applicants further submit that the Board compounded this error by only addressing two of the incidents of harassment and physical attack - the 2005 incident in Pisek, and the 2007 fire incident - as part of its  Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4933819` offsets `287-294`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `counterargument_limitation` cue `But` at chunk `4933819` offsets `257-260`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `issue` cue `whether` at chunk `4933820` offsets `75-82`; context: [22] The applicants argue that the Board erred by not properly considering whether, cumulatively, the discrimination and the physical attacks they experienced in the Czech Republic constituted persecution.
- Evidence: `party_position` cue `argue` at chunk `4933820` offsets `20-25`; context: [22] The applicants argue that the Board erred by not properly considering whether, cumulatively, the discrimination and the physical attacks they experienced in the Czech Republic constituted persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933820` offsets `276-284`; context: They claim that the Board simply proceeded sequentially through their evidence without appreciating the totality of it.
- Evidence: `party_position` cue `submit` at chunk `4933821` offsets `28-34`; context: [23] The applicants further submit that the Board compounded this error by only addressing two of the incidents of harassment and physical attack - the 2005 incident in Pisek, and the 2007 fire incident - as part of its persecution analysis, and left other incidents for consideration as part of the state protection analysis only.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933821` offsets `493-501`; context: They allege that the Board completely failed to address certain incidents, such as: the murder of the principal applicant’s cousin (which was supported by video evidence), the attack on the principal applicant’s son, and the attack on the principal applicant’s brother-in-law.

#### 19705:4:subtheme:3 · paragraphs 24-26

- Raw key terms: `applicants, attacks, board, considered, persecution, physical, alleged, amounted`
- Display key terms: `attacks, considered, persecution, physical, alleged, amounted`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: attacks, considered, persecution, physical, alleged, amounted Position/evidence statements: [24] The applicants also argue that the Board erred in its treatment of the documentary evidence as to persecution. | [25] The respondent argues that the Board considered the physical attacks on the applicants, singularly and cumulatively, and reasonably found that they did not rise to the level of persecution. Rule/authority context: [26] In order to be considered a convention refugee under section 96 of the IRPA, an applicant must demonstrate that they hold a well-founded fear of being persecuted on the basis of their race, religion, nationality, me Application context: [26] In order to be considered a convention refugee under section 96 of the IRPA, an applicant must demonstrate that they hold a well-founded fear of being persecuted on the basis of their race, religion, nationality, me Evidence spans paragraphs 24-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4933822` offsets `278-284`; context: They submit that the Board was selective in its treatment of the evidence regarding education, and that it completely ignored the country conditions documents on issues such as: physical attacks, employment discrimination, and housing discrimination.
- Evidence: `party_position` cue `argue` at chunk `4933822` offsets `25-30`; context: [24] The applicants also argue that the Board erred in its treatment of the documentary evidence as to persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933822` offsets `88-96`; context: [24] The applicants also argue that the Board erred in its treatment of the documentary evidence as to persecution.
- Evidence: `party_position` cue `argues` at chunk `4933823` offsets `20-26`; context: [25] The respondent argues that the Board considered the physical attacks on the applicants, singularly and cumulatively, and reasonably found that they did not rise to the level of persecution.
- Evidence: `evidence_fact` cue `found that` at chunk `4933823` offsets `137-147`; context: [25] The respondent argues that the Board considered the physical attacks on the applicants, singularly and cumulatively, and reasonably found that they did not rise to the level of persecution.
- Evidence: `governing_rule` cue `under` at chunk `4933824` offsets `52-57`; context: [26] In order to be considered a convention refugee under section 96 of the IRPA, an applicant must demonstrate that they hold a well-founded fear of being persecuted on the basis of their race, religion, nationality, membership in a particular social group, or because of their political opinion.
- Evidence: `reasoning_application` cue `because` at chunk `4933824` offsets `262-269`; context: [26] In order to be considered a convention refugee under section 96 of the IRPA, an applicant must demonstrate that they hold a well-founded fear of being persecuted on the basis of their race, religion, nationality, membership in a particular social group, or because of their political opinion.

#### 19705:4:subtheme:4 · paragraphs 27-31

- Raw key terms: `cumulative, consider, fear, canada, immigration, indicated, minister, nature`
- Display key terms: `cumulative, consider, fear, indicated, nature`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: cumulative, consider, fear, indicated, nature Position/evidence statements: The Federal Court of Appeal indicated in Munderere v Canada (Minister of Citizenship and Immigration), 2008 FCA 84, 291 DLR (4th) 68, at para 42, that: …the Board is duty bound to consider all of the events which may hav | In such situations, the various elements involved may, if taken together, produce an effect on the mind of the applicant that can reasonably justify a claim to well-founded fear of persecution on “cumulative grounds”… Rule/authority context: [28] Justice Eleanor Dawson in Mete v Canada (Minister of Citizenship and Immigration), 2005 FC 840, 46 Imm LR (3d) 232, at paras 4-6, indicated: 4 The following three legal principles are not controversial. | [29] The United Nations High Commissioner for Refugees’ Handbook on Procedures and Criteria for Determining Refugee Status under the 1951 Convention and the 1967 Protocol relating to the Status of Refugees (the “UN Handb Application context: 129, the Federal Court of Appeal defined persecution in terms of: to harass or afflict with repeated acts of cruelty or annoyance; to afflict persistently; to afflict or punish because of particular opinions or adherence Evidence spans paragraphs 27-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4933825` offsets `275-282`; context: [27] It has been recognized, on numerous occasions, that where the evidence establishes a series of actions which can be characterized as discriminatory, if not persecutory, it is incumbent on the Board to consider the cumulative nature of that conduct in order to determine whether, if taken together, it might constitute a valid basis for a well-founded fear of persecution.
- Evidence: `party_position` cue `claim` at chunk `4933825` offsets `625-630`; context: The Federal Court of Appeal indicated in Munderere v Canada (Minister of Citizenship and Immigration), 2008 FCA 84, 291 DLR (4th) 68, at para 42, that:
…the Board is duty bound to consider all of the events which may have an impact on a claimant's claim that he or she has a well founded fear of persecution, including those events which, if taken individually, do not amount to persecution, but if taken together, may justify a claim to a well founded fear of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933825` offsets `67-75`; context: [27] It has been recognized, on numerous occasions, that where the evidence establishes a series of actions which can be characterized as discriminatory, if not persecutory, it is incumbent on the Board to consider the cumulative nature of that conduct in order to determine whether, if taken together, it might constitute a valid basis for a well-founded fear of persecution.
- Evidence: `counterargument_limitation` cue `but` at chunk `4933825` offsets `769-772`; context: The Federal Court of Appeal indicated in Munderere v Canada (Minister of Citizenship and Immigration), 2008 FCA 84, 291 DLR (4th) 68, at para 42, that:
…the Board is duty bound to consider all of the events which may have an impact on a claimant's claim that he or she has a well founded fear of persecution, including those events which, if taken individually, do not amount to persecution, but if taken together, may justify a claim to a well founded fear of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933826` offsets `759-767`; context: 5 Second, in cases where the evidence establishes a series of actions characterized to be discriminatory, and not persecutory, there is a requirement to consider the cumulative nature of that conduct.
- Evidence: `governing_rule` cue `principles` at chunk `4933826` offsets `174-184`; context: [28] Justice Eleanor Dawson in Mete v Canada (Minister of Citizenship and Immigration), 2005 FC 840, 46 Imm LR (3d) 232, at paras 4-6, indicated:
4 The following three legal principles are not controversial.
- Evidence: `reasoning_application` cue `because` at chunk `4933826` offsets `471-478`; context: 129, the Federal Court of Appeal defined persecution in terms of: to harass or afflict with repeated acts of cruelty or annoyance; to afflict persistently; to afflict or punish because of particular opinions or adherence to a particular creed or mode of worship; a particular course or period of systematic infliction of punishment directed against those holding a particular belief; and persistent injury or annoyance from any source.
- Evidence: `governing_rule` cue `under` at chunk `4933827` offsets `123-128`; context: [29] The United Nations High Commissioner for Refugees’ Handbook on Procedures and Criteria for Determining Refugee Status under the 1951 Convention and the 1967 Protocol relating to the Status of Refugees (the “UN Handbook”) explains the rationale behind the requirement to consider the cumulative nature of past experiences, it indicates that:
- Evidence: `party_position` cue `claim` at chunk `4933828` offsets `414-419`; context: In such situations, the various elements involved may, if taken together, produce an effect on the mind of the applicant that can reasonably justify a claim to well-founded fear of persecution on “cumulative grounds”…

#### 19705:4:subtheme:5 · paragraphs 32-33

- Raw key terms: `applicants, aware, cumulative, discriminatory, persecution, sequentially, acts, aggregate`
- Display key terms: `aware, cumulative, discriminatory, persecution, sequentially, acts, aggregate`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: aware, cumulative, discriminatory, persecution, sequentially, acts, aggregate Application context: The Board went on, after presenting a definition of “persecution”, to conclude: “I have… considered these matters singularly and cumulatively and find that they do not rise to the level of persecution in either instance. Evidence spans paragraphs 32-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4933830` offsets `192-199`; context: [31] A careful reading of the Board’s decision leaves no doubt that it was aware of its obligation to consider the cumulative effects of the applicants’ past experiences in order to determine whether the applicants held a well-founded fear of persecution, as opposed to mere discrimination, in the Czech Republic.
- Evidence: `reasoning_application` cue `conclude` at chunk `4933830` offsets `871-879`; context: The Board went on, after presenting a definition of “persecution”, to conclude: “I have… considered these matters singularly and cumulatively and find that they do not rise to the level of persecution in either instance.
- Evidence: `counterargument_limitation` cue `However` at chunk `4933830` offsets `502-509`; context: ” However, the Board posed this question only after considering the applicants’ past experiences sequentially; it first considered the discrimination they faced surrounding education, then the employment discrimination, followed by the discrimination by the police, and finally the physical assaults.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933831` offsets `448-456`; context: [32] Justice Yves de Montigny made a similar observation in Tetik v Canada (Minister of Citizenship and Immigration), 2009 FC 1240, 86 Imm LR (3d) 154, at para 27:
…The RPD was obviously aware of the cumulative persecution test, but in fact did not review the discriminatory acts as a whole and proceeded sequentially through the chronology recounted by the applicants without appreciating the totality or cumulative effect of their uncontradicted evidence about the treatment that they had endured.

#### 19705:4:subtheme:6 · paragraphs 34-40

- Raw key terms: `board, applicants, discrimination, applicant, czech, employment, persecution, reasons`
- Display key terms: `discrimination, czech, employment, persecution`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: discrimination, czech, employment, persecution Application context: There is no indication in the Decision as to what test and what reasoning the Board applied to the issue of whether the cumulative impact of discrimination did not amount to persecution. Evidence spans paragraphs 34-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933832` offsets `90-95`; context: [33] The Board’s analysis in the present case is also somewhat similar to the analysis at issue in Rahman v Canada (Minister of Citizenship and Immigration), 2009 FC 768, 348 FTR 69.
- Evidence: `reasoning_application` cue `applied` at chunk `4933832` offsets `1660-1667`; context: There is no indication in the Decision as to what test and what reasoning the Board applied to the issue of whether the cumulative impact of discrimination did not amount to persecution.
- Evidence: `counterargument_limitation` cue `However` at chunk `4933834` offsets `384-391`; context: ” However, as the applicants rightly point out, this is problematic: it suggests that the Board did not necessarily consider the totality of the physical assaults before determining that the cumulative effect of the attacks, coupled with the discrimination in other areas, did not amount to persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933836` offsets `112-120`; context: [37] Finally, with respect to the applicants’ argument that the Board erred in its treatment of the documentary evidence as to Romani persecution in the Czech Republic, Justice John O’Keefe did indicate at para 25, in Kaleja v Canada (Minister of Citizenship and Immigration), 2010 FC 252, that, “the principle that documentary evidence on persecution of a particular social group should be seriously evaluated is applicable to Roma cases.
- Evidence: `counterargument_limitation` cue `However` at chunk `4933836` offsets `670-677`; context: However, the Board failed to canvass the documentary evidence related to the other areas of concern raised by the applicants, principally: employment and the fear of being physically attacked.
- Evidence: `counterargument_limitation` cue `however` at chunk `4933837` offsets `277-284`; context: [38] For example, the US Department of State (US DOS) report on the human rights practices in the Czech Republic entitled, “Country Reports on Human Rights Practices for 2008” (February 25, 2009), indicated that:
The law prohibits employment discrimination based on ethnicity; however, Roma continued to face discrimination in both employment and education.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933838` offsets `57-65`; context: [39] Instead of addressing any of the country conditions evidence as to employment, the Board determined that, “there may have been discrimination” in relation to the principal applicant’s employment.

#### 19705:4:subtheme:7 · paragraphs 41-42

- Raw key terms: `applicants, board, conditions, country, czech, determination, objective, persecution`
- Display key terms: `conditions, country, czech, determination, objective, persecution`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: conditions, country, czech, determination, objective, persecution Application context: [41] These omissions by the Board lead me to conclude that the Board’s determination that the applicants’ experiences in the Czech Republic did “not rise to the level of persecution” was unreasonable. Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933839` offsets `42-47`; context: [40] The same US DOS report addressed the issue of physical attacks against the Roma.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933839` offsets `474-482`; context: ” The Board should have addressed this type of objective country conditions evidence before making a determination as to whether what the applicants had faced in the Czech Republic amounted to persecution or merely discrimination.
- Evidence: `reasoning_application` cue `conclude` at chunk `4933840` offsets `45-53`; context: [41] These omissions by the Board lead me to conclude that the Board’s determination that the applicants’ experiences in the Czech Republic did “not rise to the level of persecution” was unreasonable.

#### 19705:4:subtheme:8 · paragraphs 43-44

- Raw key terms: `applicants, board, czech, erred, failed, ignored, protection, republic`
- Display key terms: `czech, erred, failed, ignored, protection, republic`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: czech, erred, failed, ignored, protection, republic Position/evidence statements: [42] The applicants argue that the Board erred by referring to, and taking note of, only selective documentary evidence on the issue of state protection. | [43] The applicants further submit that the Board erred by not properly considering their previous unsuccessful attempts to obtain protection in the Czech Republic. Evidence spans paragraphs 43-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933841` offsets `127-132`; context: [42] The applicants argue that the Board erred by referring to, and taking note of, only selective documentary evidence on the issue of state protection.
- Evidence: `party_position` cue `argue` at chunk `4933841` offsets `20-25`; context: [42] The applicants argue that the Board erred by referring to, and taking note of, only selective documentary evidence on the issue of state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933841` offsets `111-119`; context: [42] The applicants argue that the Board erred by referring to, and taking note of, only selective documentary evidence on the issue of state protection.
- Evidence: `party_position` cue `submit` at chunk `4933842` offsets `28-34`; context: [43] The applicants further submit that the Board erred by not properly considering their previous unsuccessful attempts to obtain protection in the Czech Republic.

#### 19705:4:subtheme:9 · paragraphs 45-46

- Raw key terms: `applicants, board, protection, state, adequacy, adequate, analysis, analyzing`
- Display key terms: `protection, state, adequacy, adequate, analysis, analyzing`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: protection, state, adequacy, adequate, analysis, analyzing Position/evidence statements: [44] Overall, the applicants argue that the mere existence of state protection remedies is insufficient, and that an assessment of the adequacy of state protection includes determining whether, in practice, those remedie | [45] The respondent argues that the applicants did not satisfy the legal or evidentiary burden of providing evidence of sufficient probative value to rebut the presumption of state protection. Evidence spans paragraphs 45-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4933843` offsets `185-192`; context: [44] Overall, the applicants argue that the mere existence of state protection remedies is insufficient, and that an assessment of the adequacy of state protection includes determining whether, in practice, those remedies are useful.
- Evidence: `party_position` cue `argue` at chunk `4933843` offsets `29-34`; context: [44] Overall, the applicants argue that the mere existence of state protection remedies is insufficient, and that an assessment of the adequacy of state protection includes determining whether, in practice, those remedies are useful.
- Evidence: `party_position` cue `argues` at chunk `4933844` offsets `20-26`; context: [45] The respondent argues that the applicants did not satisfy the legal or evidentiary burden of providing evidence of sufficient probative value to rebut the presumption of state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933844` offsets `108-116`; context: [45] The respondent argues that the applicants did not satisfy the legal or evidentiary burden of providing evidence of sufficient probative value to rebut the presumption of state protection.

#### 19705:4:subtheme:10 · paragraphs 47-48

- Raw key terms: `pointed, protection, state, ability, above, access, acws, adequate`
- Display key terms: `pointed, protection, state, ability, above, access, acws, adequate`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: pointed, protection, state, ability, above, access, acws, adequate Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933845` offsets `131-136`; context: [46] The Board focused the bulk of its state protection analysis on considering the country conditions evidence set out in the IRB issue paper entitled, “Czech Republic: Fact-finding Mission Report on State Protection” (June 2009).
- Evidence: `evidence_fact` cue `evidence` at chunk `4933845` offsets `103-111`; context: [46] The Board focused the bulk of its state protection analysis on considering the country conditions evidence set out in the IRB issue paper entitled, “Czech Republic: Fact-finding Mission Report on State Protection” (June 2009).

#### 19705:4:subtheme:11 · paragraphs 49-51

- Raw key terms: `board, country, evidence, applicants, conditions, czech, government, however`
- Display key terms: `country, conditions, czech, government, however`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: country, conditions, czech, government, however Application context: [49] In the present case, I find that it was unreasonable for the Board to have focused on the “very serious efforts” being employed by the Czech Republic to protect Romani citizens to the exclusion of the evidence showi Evidence spans paragraphs 49-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4933847` offsets `2090-2095`; context: Even the document relied on by the Board, the 2009 issue paper, indicated:
Other NGO interlocutors claimed that the police tended to address acts of extremism only when they were considered serious or too high-profile to ignore…
- Evidence: `evidence_fact` cue `evidence` at chunk `4933847` offsets `88-96`; context: [48] Completely absent from the Board’s discussion was any recognition of the objective evidence pointing towards a potential inadequacy in state protection.
- Evidence: `counterargument_limitation` cue `however` at chunk `4933847` offsets `759-766`; context: The US DOS report on the human rights practices in the Czech Republic entitled, “Country Reports on Human Rights Practices for 2008” (February 25, 2009), indicated:
The laws prohibit discrimination based on race, gender, disability, language, or social status; however, significant societal discrimination against Roma and women persisted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933848` offsets `206-214`; context: [49] In the present case, I find that it was unreasonable for the Board to have focused on the “very serious efforts” being employed by the Czech Republic to protect Romani citizens to the exclusion of the evidence showing that, in practice, those efforts may have been inadequate.
- Evidence: `reasoning_application` cue `I find` at chunk `4933848` offsets `26-32`; context: [49] In the present case, I find that it was unreasonable for the Board to have focused on the “very serious efforts” being employed by the Czech Republic to protect Romani citizens to the exclusion of the evidence showing that, in practice, those efforts may have been inadequate.
- Evidence: `counterargument_limitation` cue `However` at chunk `4933848` offsets `363-370`; context: However, in view of the fact that reliable and relevant country conditions evidence supporting the applicants’ position had been presented, the Board had an obligation to acknowledge that evidence and explain why it was satisfied that, despite that evidence, the government’s “very serious efforts” were sufficient: see Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration) (1998), 157 FTR 35, 83 ACWS (3d) 264 (TD).
- Evidence: `evidence_fact` cue `evidence` at chunk `4933849` offsets `82-90`; context: [50] Given the Board’s unreasonable treatment of the objective country conditions evidence, it is unnecessary to move on to consider the Board’s treatment of the applicants’ personal experiences with respect to state protection.

#### 19705:4:subtheme:12 · paragraphs 52-53

- Raw key terms: `allowed, allowing, analysis, analyze, andr, application, bledy, board`
- Display key terms: `allowed, allowing, analysis, analyze, andr, bledy`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: allowed, allowing, analysis, analyze, andr, bledy Operative outcome context: the application for judicial review is allowed; and 2. Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4933850` offsets `52-60`; context: [51] Since the Board failed to properly analyze the question of persecution, and since the Board erred in its state protection analysis by inadequately surveying the country conditions evidence, I am allowing this application for judicial review.
- Evidence: `evidence_fact` cue `evidence` at chunk `4933850` offsets `185-193`; context: [51] Since the Board failed to properly analyze the question of persecution, and since the Board erred in its state protection analysis by inadequately surveying the country conditions evidence, I am allowing this application for judicial review.
- Evidence: `disposition` cue `allowed` at chunk `4933850` offsets `329-336`; context: the application for judicial review is allowed; and
2.

#### Section text

[19] The issues before the Court are the following:
(a) Did the Board err in finding that the applicants did not face persecution in the Czech Republic?
(b) Did the Board err in finding that state protection was available to the applicants in the Czech Republic?
Standard of Review

[20] The identification of persecution behind incidents of discrimination or harassment has consistently been reviewed by this Court against a standard of reasonableness: see Tetik v Canada (Minister of Citizenship and Immigration), 2009 FC 1240, 86 Imm LR (3d) 154, at para 25; Liang v Canada (Minister of Citizenship and Immigration), 2008 FC 450, 166 ACWS (3d) 950, at para 12. It is also well-established that the standard of review to apply to the issue of state protection is reasonableness: see Tetik, above, at para 25; Mendez v Canada (Minister of Citizenship and Immigration), 2008 FC 584, 168 ACWS (3d) 596 at paras 11-13.

[21] In Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190, at para 47, the Supreme Court of Canada held that:
…reasonableness is concerned mostly with the existence of justification, transparency and intelligibility within the decision-making process. But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
Argument and Analysis
(a) Did the Board err in finding that the applicants did not face persecution in the Czech Republic?

[22] The applicants argue that the Board erred by not properly considering whether, cumulatively, the discrimination and the physical attacks they experienced in the Czech Republic constituted persecution. They claim that the Board simply proceeded sequentially through their evidence without appreciating the totality of it. They argue that it was incumbent on the Board to explain why it found that their experiences, cumulatively, did not amount to persecution.

[23] The applicants further submit that the Board compounded this error by only addressing two of the incidents of harassment and physical attack - the 2005 incident in Pisek, and the 2007 fire incident - as part of its persecution analysis, and left other incidents for consideration as part of the state protection analysis only. They allege that the Board completely failed to address certain incidents, such as: the murder of the principal applicant’s cousin (which was supported by video evidence), the attack on the principal applicant’s son, and the attack on the principal applicant’s brother-in-law.

[24] The applicants also argue that the Board erred in its treatment of the documentary evidence as to persecution. They submit that the Board was selective in its treatment of the evidence regarding education, and that it completely ignored the country conditions documents on issues such as: physical attacks, employment discrimination, and housing discrimination. The applicants claim that it was incumbent on the Board to explicitly discuss this evidence as it ran counter to the Board’s ultimate conclusion that the applicants’ experiences had not amounted to persecution.

[25] The respondent argues that the Board considered the physical attacks on the applicants, singularly and cumulatively, and reasonably found that they did not rise to the level of persecution. The respondent submits that every serious incident alleged by the applicants had been dealt with in the Board’s reasons. Ultimately, the respondent contends, the applicants have not demonstrated that the Board’s finding as to a lack of persecution was unreasonable.

[26] In order to be considered a convention refugee under section 96 of the IRPA, an applicant must demonstrate that they hold a well-founded fear of being persecuted on the basis of their race, religion, nationality, membership in a particular social group, or because of their political opinion.

[27] It has been recognized, on numerous occasions, that where the evidence establishes a series of actions which can be characterized as discriminatory, if not persecutory, it is incumbent on the Board to consider the cumulative nature of that conduct in order to determine whether, if taken together, it might constitute a valid basis for a well-founded fear of persecution. The Federal Court of Appeal indicated in Munderere v Canada (Minister of Citizenship and Immigration), 2008 FCA 84, 291 DLR (4th) 68, at para 42, that:
…the Board is duty bound to consider all of the events which may have an impact on a claimant's claim that he or she has a well founded fear of persecution, including those events which, if taken individually, do not amount to persecution, but if taken together, may justify a claim to a well founded fear of persecution.

[28] Justice Eleanor Dawson in Mete v Canada (Minister of Citizenship and Immigration), 2005 FC 840, 46 Imm LR (3d) 232, at paras 4-6, indicated:
4 The following three legal principles are not controversial. First, in Rajudeen v. Canada (Minister of Employment and Immigration) (1984), 55 N.R. 129, the Federal Court of Appeal defined persecution in terms of: to harass or afflict with repeated acts of cruelty or annoyance; to afflict persistently; to afflict or punish because of particular opinions or adherence to a particular creed or mode of worship; a particular course or period of systematic infliction of punishment directed against those holding a particular belief; and persistent injury or annoyance from any source.
5 Second, in cases where the evidence establishes a series of actions characterized to be discriminatory, and not persecutory, there is a requirement to consider the cumulative nature of that conduct. This requirement reflects the fact that prior incidents are capable of forming the foundation of present fear. See: Retnem v. Canada (Minister of Employment and Immigration) (1991), 132 N.R. 53 (F.C.A.). This is also expressed in the UNHCR Handbook on Procedures and Criteria for Determining Refugee Status ("Handbook on Refugee Status") in the following terms, at paragraph 53…
6 Third, it is an error of law for the RPD not to consider the cumulative nature of the conduct directed against a claimant. See: Bobrik v. Canada (Minister of Citizenship and Immigration) (1994), 85 F.T.R. 13 (T.D.) at paragraph 22, and the authorities there reviewed by my colleague Madam Justice Tremblay-Lamer.
[Emphasis added]

[29] The United Nations High Commissioner for Refugees’ Handbook on Procedures and Criteria for Determining Refugee Status under the 1951 Convention and the 1967 Protocol relating to the Status of Refugees (the “UN Handbook”) explains the rationale behind the requirement to consider the cumulative nature of past experiences, it indicates that:

[53]…an applicant may have been subjected to various measures not in themselves amounting to persecution (e.g. discrimination in different forms), in some cases combined with other adverse factors (e.g. general atmosphere of insecurity in the country of origin). In such situations, the various elements involved may, if taken together, produce an effect on the mind of the applicant that can reasonably justify a claim to well-founded fear of persecution on “cumulative grounds”…

[30] The obligation to consider the cumulative effect of past treatment also reflects the principle that prior incidents are capable of forming the basis of present fear: see Retnem v Canada (Minister of Employment and Immigration) (1991), 132 NR 53, 27 ACWS (3d) 481 (FCA). As Chief Justice Arthur Thurlow indicated in Alfredo Manuel Oyarzo Marchant v Minister of Employment and Immigration, [1982] 2 FC 779 (CA):
…since it is the foundation for a present fear that must be considered, such incidents in the past are part of the whole picture and cannot be discarded entirely as a basis for fear, even though what has happened since has left them in the background.

[31] A careful reading of the Board’s decision leaves no doubt that it was aware of its obligation to consider the cumulative effects of the applicants’ past experiences in order to determine whether the applicants held a well-founded fear of persecution, as opposed to mere discrimination, in the Czech Republic. At paragraph 26 of its reasons, the Board asked the right question: “Does the discrimination suffered by these claimants amount to persecution when considered singularly or cumulatively?” However, the Board posed this question only after considering the applicants’ past experiences sequentially; it first considered the discrimination they faced surrounding education, then the employment discrimination, followed by the discrimination by the police, and finally the physical assaults. The Board went on, after presenting a definition of “persecution”, to conclude: “I have… considered these matters singularly and cumulatively and find that they do not rise to the level of persecution in either instance.” It failed to provide any analysis of the cumulative effects of the discriminatory incidents and explain why these incidents, in the aggregate, did not amount to persecution.

[32] Justice Yves de Montigny made a similar observation in Tetik v Canada (Minister of Citizenship and Immigration), 2009 FC 1240, 86 Imm LR (3d) 154, at para 27:
…The RPD was obviously aware of the cumulative persecution test, but in fact did not review the discriminatory acts as a whole and proceeded sequentially through the chronology recounted by the applicants without appreciating the totality or cumulative effect of their uncontradicted evidence about the treatment that they had endured. This was a crucial error…

[33] The Board’s analysis in the present case is also somewhat similar to the analysis at issue in Rahman v Canada (Minister of Citizenship and Immigration), 2009 FC 768, 348 FTR 69. Justice James Russell, in that case, indicated, at paras 65-67:
65 The Board says at paragraph 21 that the determination that the Applicant will not be persecuted if returned to Lebanon is made "by not only scrutinizing the various forms of discrimination that the claimant has endured, but also by examining the various forms of discrimination cumulatively." The Board then goes on to scrutinize "the various forms of discrimination" separately, but never provides any real explanation as to why the cumulative impact does not amount to persecution.
66 As Justice Dawson pointed out in Mete v. Canada (Minister of Citizenship and Immigration) 2005 FC 840 at paragraph 9 "it is insufficient for the RPD to simply state that it has considered the cumulative nature of the discriminatory acts."
67 As in Mete, the Board in the present case "completely failed to consider the cumulative effect of the conduct characterized ... to be discriminatory or harassing, as required by the Federal Court of Appeal in Retnem, [1991] F.C.J. No. 428, and as explained in the Handbook on Refugee Status." It is not enough for the Officer to simply say that he has examined "the various form of discrimination cumulatively." The reasons need to articulate why the long history of appalling discrimination by the State of Lebanon against the Applicant as a stateless Palestinian does not amount to persecution. There is no indication in the Decision as to what test and what reasoning the Board applied to the issue of whether the cumulative impact of discrimination did not amount to persecution.
[Emphasis added]

[34] Since the Board specifically acknowledged in its reasons that what the applicants had experienced with respect to their education, the repeated verbal insults, and the numerous physical assaults, was “obviously” discriminatory in nature, and since the Board acknowledged that there “may have been discrimination” relating to the principal applicant’s employment, it was incumbent on the Board to explain why this wide-ranging discrimination did not amount, cumulatively, to persecution.

[35] I also support the applicants’ view that the Board erred in only mentioning two of the assaults as part of its “discrimination vs. persecution” analysis: the 2005 incident in Pisek, with which the Board had credibility concerns, and the 2007 house fires. The Board indicated, “[t]he physical attacks on the claimants are considered in the following section on state protection.” However, as the applicants rightly point out, this is problematic: it suggests that the Board did not necessarily consider the totality of the physical assaults before determining that the cumulative effect of the attacks, coupled with the discrimination in other areas, did not amount to persecution. Justice de Montigny in Tetik, above, at para 29, indicated:
29 Furthermore, I agree with the applicants that the RPD did not consider the most serious harassment acts in the persecution analysis, but only in the state protection part of its reasons. The RPD focused on the minor incidents and on the events that do not even constitute discrimination (ostracism by the families, Ceday's treatment in kindergarten) in the part of its reasons dealing with persecution. The more serious incidents of threats and assaults were discussed but only in the context of state protection. The physical assaults they have suffered should have been considered in the cumulative effect analysis; failing to do so means that the RPD did not consider the totality of the circumstances before concluding there was an absence of persecution. [Emphasis added]

[36] Some of the alleged assaults were not referenced by the Board at all. Assaults that were mentioned by the principal applicant for the first time at the hearing before the Board (and not mentioned in the applicants’ PIFs) were not considered by the Board in its reasons. Included amongst the incidents omitted by the Board from its reasons were: the allegation that the principal applicant’s cousin had been attacked and killed by skinheads in 1992, the allegation that the principal applicant’s eldest son was attacked on his first day of school, as well as the allegation that the principal applicant’s brother-in-law had recently been attacked in the Czech Republic following a failed refugee claim in Canada. Since the Board did not indicate that it had any credibility concerns with respect to these allegations, it should have considered these assaults as part of its cumulative analysis.

[37] Finally, with respect to the applicants’ argument that the Board erred in its treatment of the documentary evidence as to Romani persecution in the Czech Republic, Justice John O’Keefe did indicate at para 25, in Kaleja v Canada (Minister of Citizenship and Immigration), 2010 FC 252, that, “the principle that documentary evidence on persecution of a particular social group should be seriously evaluated is applicable to Roma cases.” The Board adequately addressed the documentary evidence as it pertained to access to education by noting both that there was “still a lot of prejudice” in this regard, and that measures were being taken to improve the situation. However, the Board failed to canvass the documentary evidence related to the other areas of concern raised by the applicants, principally: employment and the fear of being physically attacked.

[38] For example, the US Department of State (US DOS) report on the human rights practices in the Czech Republic entitled, “Country Reports on Human Rights Practices for 2008” (February 25, 2009), indicated that:
The law prohibits employment discrimination based on ethnicity; however, Roma continued to face discrimination in both employment and education. Precise figures were unavailable, but the unemployment rate for Roma was estimated to be approximately 75 percent. Some employers refused to hire Roma and requested that local labour offices not send them Romani applicants.
[Emphasis added]

[39] Instead of addressing any of the country conditions evidence as to employment, the Board determined that, “there may have been discrimination” in relation to the principal applicant’s employment. This failure by the Board to acknowledge reliable documentary evidence linking discrimination to very high levels of unemployment for Roma in the Czech Republic constitutes an error to properly engage with the evidence before it.

[40] The same US DOS report addressed the issue of physical attacks against the Roma. It indicated, “Neo Nazis, members of the far right Workers Party, and skinheads attacked and harassed Roma and other minorities during the year,” as well as that, “[m]embers and sympathizers of skinhead organizations were the most frequent perpetrators of acts of interethnic violence, particularly against Roma.” The Board should have addressed this type of objective country conditions evidence before making a determination as to whether what the applicants had faced in the Czech Republic amounted to persecution or merely discrimination.

[41] These omissions by the Board lead me to conclude that the Board’s determination that the applicants’ experiences in the Czech Republic did “not rise to the level of persecution” was unreasonable. The Board failed to conduct a proper cumulative analysis, failed to sufficiently address the individual incidents of mistreatment alleged by the applicants, and failed to adequately canvas the objective country conditions documents.
(b) Did the Board err in finding that state protection was available to the applicants in the Czech Republic?

[42] The applicants argue that the Board erred by referring to, and taking note of, only selective documentary evidence on the issue of state protection. They submit that the Board ignored or failed to take note of documentary evidence that tended to demonstrate that state protection was, in fact, inadequate for similarly situated individuals in the Czech Republic.

[43] The applicants further submit that the Board erred by not properly considering their previous unsuccessful attempts to obtain protection in the Czech Republic. They point out that the Board completely failed to address state protection in the context of the adult applicants’ allegations that: they were ignored by their teachers when they were attacked as children, they were laughed at by the police after the 2005 attacks in Pisek, they were laughed at by the police with respect to the 2007 rape, nobody was punished with respect to the murder of the principal applicant’s cousin in 1992, the principal applicant’s cousin was unable to receive police protection regarding the incident in 2010, and that the police have skinheads among them and had used racist insults against the principal applicant and other Roma in the past.

[44] Overall, the applicants argue that the mere existence of state protection remedies is insufficient, and that an assessment of the adequacy of state protection includes determining whether, in practice, those remedies are useful. The applicants argue that, in light of the errors in analyzing the country conditions documents, as well as the errors in assessing the applicants’ personal attempts to obtain state protection, the Board’s analysis of the adequacy of state protection was unreasonable.

[45] The respondent argues that the applicants did not satisfy the legal or evidentiary burden of providing evidence of sufficient probative value to rebut the presumption of state protection. As such, the respondent submits that the Board’s decision that state protection in the Czech Republic was adequate was reasonable.

[46] The Board focused the bulk of its state protection analysis on considering the country conditions evidence set out in the IRB issue paper entitled, “Czech Republic: Fact-finding Mission Report on State Protection” (June 2009). As outlined above, the Board pointed to legislative prohibitions on discrimination as well as measures implemented to reform the country’s police force and increase access to protection for the Romani population. The Board concluded that the, “preponderance of the documentary evidence” indicated that the Czech government was making “very serious efforts” to protect t

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 19705:5 · paragraphs 54-54

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7e09ec2e3c44acd69469dd9783601adc93cc103ee83dd61bf9b72bd6b7a145b3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 19705:5:subtheme:1 · paragraphs 54-54

- Raw key terms: `appearances, applicants, attorney, barrister, brad, canada, daniel, dated`
- Display key terms: `barrister, brad, daniel, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, brad, daniel, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 54-54. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: SCOTT J.
DATED: February 22, 2011
APPEARANCES:
Daniel Radin
FOR THE APPLICANTS
Brad Gotkin
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Daniel Radin
Barrister and Solicitor
Toronto, ON
FOR THE APPLICANTS
Myles J. Kirvan
Deputy Attorney General of Canada
Toronto, ON
FOR THE RESPONDENT
