# Discussion Units: case 21053

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **93**
- Continuity pairs: **92**
- Discussion Units: **6**
- Paragraph source hashes: **93**
- Sub-themes: **26**

## 21053:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fb213727a956acbae2b2d41dbb8503dfcce7d54b0b1746a145ccc8ab1a22db14`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `applicant, principal, protection, mexico, applicants, board, daughters, gang`
- Display key terms: `principal, protection, mexico, daughters, gang`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: principal, protection, mexico, daughters, gang Rule/authority context: [1] This is an application pursuant to s. | DECISION UNDER REVIEW Application context: Both he and his son fled Mexico and arrived in Canada on November 4, 2004 and applied for refugee protection. Operative outcome context: [5] The Principal Applicant filed a formal complaint against the gang with the police, but her complaint was dismissed on the grounds that her allegations lacked evidence. Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4991692` offsets `27-38`; context: [1] This is an application pursuant to s.
- Evidence: `reasoning_application` cue `applied` at chunk `4991694` offsets `504-511`; context: Both he and his son fled Mexico and arrived in Canada on November 4, 2004 and applied for refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991696` offsets `162-170`; context: [5] The Principal Applicant filed a formal complaint against the gang with the police, but her complaint was dismissed on the grounds that her allegations lacked evidence.
- Evidence: `disposition` cue `dismissed` at chunk `4991696` offsets `109-118`; context: [5] The Principal Applicant filed a formal complaint against the gang with the police, but her complaint was dismissed on the grounds that her allegations lacked evidence.
- Evidence: `governing_rule` cue `UNDER` at chunk `4991698` offsets `75-80`; context: DECISION UNDER REVIEW
- Evidence: `evidence_fact` cue `testimony` at chunk `4991699` offsets `68-77`; context: [8] The Board considered the Principal Applicant’s oral and written testimony, her counsel’s submissions and all of the documentary evidence provided.
- Evidence: `evidence_fact` cue `found that` at chunk `4991700` offsets `14-24`; context: [9] The Board found that there was adequate state protection for individuals like the Applicants in Mexico and concluded that the Applicants had not met the burden of establishing “clear and convincing” proof of a lack of state protection for individuals like them in Mexico in accordance with the governing jurisprudence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4991700` offsets `308-321`; context: [9] The Board found that there was adequate state protection for individuals like the Applicants in Mexico and concluded that the Applicants had not met the burden of establishing “clear and convincing” proof of a lack of state protection for individuals like them in Mexico in accordance with the governing jurisprudence.
- Evidence: `evidence_fact` cue `found that` at chunk `4991701` offsets `15-25`; context: [10] The Board found that the Principal Applicant’s testimony indicated that the kidnapping incident occurred on March 23, 2003 and that members of the Los Macizos gang were captured and jailed by the authorities, thus indicating that the Mexican authorities had taken action against her husband’s kidnappers.

#### 21053:1:subtheme:2 · paragraphs 11-13

- Raw key terms: `applicant, available, board, police, principal, state, against, assistance`
- Display key terms: `available, police, principal, state, against, assistance`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: available, police, principal, state, against, assistance Application context: The Principal Applicant had no awareness of other services available to her to deal with corrupt federal and state employees; however, she was certain that these state institutions would have helped her had she applied f Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4991702` offsets `636-643`; context: The Principal Applicant had no awareness of other services available to her to deal with corrupt federal and state employees; however, she was certain that these state institutions would have helped her had she applied for help from them.
- Evidence: `evidence_fact` cue `found that` at chunk `4991703` offsets `15-25`; context: [12] The Board found that ignorance was no excuse for the Principal Applicant’s failure to pursue the avenues of protection available to her in her own country, instead of taking the extreme measures of seeking protection abroad.
- Evidence: `evidence_fact` cue `found that` at chunk `4991704` offsets `318-328`; context: The Board found that the state and the Human Rights Commission would provide the Principal Applicant with assistance.

#### 21053:1:subtheme:3 · paragraphs 14-14

- Raw key terms: `adequate, although, applicant, available, board, clear, conclusion, convincing`
- Display key terms: `adequate, although, available, clear, conclusion, convincing`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: adequate, although, available, clear, conclusion, convincing Application context: [14] In conclusion, the Board found that the Principal Applicant lived in a democracy and was therefore obliged to seek protection in Mexico before invoking international protection. Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4991705` offsets `455-461`; context: ISSUES
- Evidence: `evidence_fact` cue `found that` at chunk `4991705` offsets `30-40`; context: [14] In conclusion, the Board found that the Principal Applicant lived in a democracy and was therefore obliged to seek protection in Mexico before invoking international protection.
- Evidence: `reasoning_application` cue `therefore` at chunk `4991705` offsets `94-103`; context: [14] In conclusion, the Board found that the Principal Applicant lived in a democracy and was therefore obliged to seek protection in Mexico before invoking international protection.
- Evidence: `counterargument_limitation` cue `although` at chunk `4991705` offsets `346-354`; context: The Board found adequate, although not perfect, state protection was available to the Principal Applicant should she return to Mexico.

#### Section text

Sanchez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-12-01
Neutral citation
2008 FC 1336
File numbers
IMM-5283-07
Notes
Reported Decision
Decision Content
Date: 20081201
Docket: IMM-5283-07
Citation: 2008 FC 1336
Ottawa, Ontario, December 1, 2008
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
PATRICIA TORRES SANCHEZ
DIANA RAMOS TORRES
LAURA RAMOS TORRES
DANIELA RAMOS TORRES
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to s. 72 (1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (Act) for judicial review of a decision of the Refugee Protection Division of the Immigration Refugee Board (Board), dated November 22, 2007 (Decision) refusing the Applicants’ application to be deemed Convention refugees or persons in need of protection under section 96 and section 97 of the Act.
BACKGROUND

[2] Patricia Sanchez (Principal Applicant) and her daughters Diana, Laura and Daniela are citizens of Mexico.

[3] The Principal Applicant’s husband, Martin Rodriguez, was kidnapped on March 23, 2003 by the Los Macizos gang. He was released 20 days later after a ransom payment was made to the gang. Some of the gang members were jailed for the kidnapping. During a TV program, the Principal Applicant learned that gang members had bribed jail officers and had escaped. The escaped kidnappers harassed the Principal Applicant’s husband. Both he and his son fled Mexico and arrived in Canada on November 4, 2004 and applied for refugee protection. After the Principal Applicant’s husband fled Mexico, the Principal Applicant and her daughters moved in with her mother.

[4] The Los Macizos gang began harassing the Principal Applicant and her daughters after her husband’s departure. They followed her, asked her to disclose her husband’s whereabouts, and attempted to kidnap her. They told the Principal Applicant they would kill her and her daughters if she did not tell them where her husband was.

[5] The Principal Applicant filed a formal complaint against the gang with the police, but her complaint was dismissed on the grounds that her allegations lacked evidence. The Principal Applicant says that the police promised to send a police patrol to monitor her residence but they did not do so.

[6] The Principal Applicant and her daughters arrived in Canada on June 27, 2006 by plane and made claims for refugee protection in Toronto.

[7] The Applicants’ refugee hearing was held on October 29, 2007.
DECISION UNDER REVIEW

[8] The Board considered the Principal Applicant’s oral and written testimony, her counsel’s submissions and all of the documentary evidence provided. The Board addressed the documentary evidence pertaining to measures in Mexico for dealing with crime, including kidnapping and corruption, as well as evidence about the police, the availability of means for lodging complaints and, in general, the level of democracy in Mexico.
State Protection

[9] The Board found that there was adequate state protection for individuals like the Applicants in Mexico and concluded that the Applicants had not met the burden of establishing “clear and convincing” proof of a lack of state protection for individuals like them in Mexico in accordance with the governing jurisprudence.

[10] The Board found that the Principal Applicant’s testimony indicated that the kidnapping incident occurred on March 23, 2003 and that members of the Los Macizos gang were captured and jailed by the authorities, thus indicating that the Mexican authorities had taken action against her husband’s kidnappers. In addition, the Principal Applicant did not seek out state protection in Mexico, but only sought help from the police on one occasion. No redress was sought for the threats or mistreatment that the Principal Applicant allegedly received from members of the gang.

[11] The Board also noted that the Principal Applicant did not seek assistance from the Federal Agency of Investigations (AFI) that deals with corrupt state officials, drug traffickers and violent kidnappers. The Principal Applicant indicated that she knew about the Human Rights Commission that handled complaints about police misconduct, and situations where citizens’ rights are violated, but she did not seek their help. The Principal Applicant had no awareness of other services available to her to deal with corrupt federal and state employees; however, she was certain that these state institutions would have helped her had she applied for help from them.

[12] The Board found that ignorance was no excuse for the Principal Applicant’s failure to pursue the avenues of protection available to her in her own country, instead of taking the extreme measures of seeking protection abroad. The Board cited documentary evidence that Mexico is a federal republic with a bicameral legislature that has federal and state police. There is also state protection for individuals in similar situations to the Applicants. The Board found no lack of police protection for victims of gang violence or corruption, and no persuasive evidence to suggest that the Special Investigations into Organized Crime (SIEDO) would not assist the Applicants against the Los Macizos gang. The evidence showed that SIEDO had broken up four gangs and had assisted in joint USA/Mexico investigations to arrest members of organized crime groups.

[13] The Board recognized that, although corruption was still an ongoing problem in Mexico, the Government of Mexico continued to promote anti-corruption efforts. The Board was not persuaded that there was a lack of action by the state authorities against corrupt government officials, including the police. The Board found that the state and the Human Rights Commission would provide the Principal Applicant with assistance. There was no evidence to suggest they would not ensure that adequate state protection was available to the Principal Applicant and her daughters should they return to Mexico.

[14] In conclusion, the Board found that the Principal Applicant lived in a democracy and was therefore obliged to seek protection in Mexico before invoking international protection. She had not discharged the onus upon her of showing clear and convincing proof of the state’s inability or unwillingness to protect her. The Board found adequate, although not perfect, state protection was available to the Principal Applicant should she return to Mexico.
ISSUES

## 21053:2 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3bd830f03d7384394359f2cf0291a022e727434f79f1d6037a39e1ada7f24f78`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:2:subtheme:1 · paragraphs 15-15

- Raw key terms: `applicants, application, attorney, behalf, board, canada, commit, documentary`
- Display key terms: `behalf, commit, documentary`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: behalf, commit, documentary Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991706` offsets `46-51`; context: [15] The Applicants have raised the following issue:
1) Did the Board commit an error of law in preferring the documentary evidence over the Applicants’ evidence?
- Evidence: `evidence_fact` cue `evidence` at chunk `4991706` offsets `123-131`; context: [15] The Applicants have raised the following issue:
1) Did the Board commit an error of law in preferring the documentary evidence over the Applicants’ evidence?

#### Section text

[15] The Applicants have raised the following issue:
1) Did the Board commit an error of law in preferring the documentary evidence over the Applicants’ evidence?
2) Does the mere existence of “serious efforts” on behalf of a state equate to state protection?
3) Did the Board err in their application of Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689?
STATUTORY PROVISIONS

## 21053:3 · paragraphs 16-74

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8c99c732a66a93667e272950429740e73135959b85f1a562fc2a89e49b8674e2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:3:subtheme:1 · paragraphs 16-17

- Raw key terms: `canada, having, review, standards, accepted, adequate, against, alors`
- Display key terms: `having, review, standards, accepted, adequate, against, alors`
- Argument roles: `counterargument_limitation, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, reasoning_application Display terms: having, review, standards, accepted, adequate, against, alors Rule/authority context: STANDARD OF REVIEW Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj | New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in tr Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4991707` offsets `3726-3744`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `because` at chunk `4991707` offsets `1175-1182`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `reasoning_application` cue `apply` at chunk `4991708` offsets `248-253`; context: New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (Dunsmuir at para.
- Evidence: `counterargument_limitation` cue `although` at chunk `4991708` offsets `92-100`; context: New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (Dunsmuir at para.

#### 21053:3:subtheme:2 · paragraphs 18-19

- Raw key terms: `canada, court, held, standard, adopt, analysis, applicable, case`
- Display key terms: `standard, adopt, analysis, applicable, case`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: standard, adopt, analysis, applicable, case Rule/authority context: [18] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991709` offsets `198-206`; context: Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4991709` offsets `62-80`; context: [18] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance.
- Evidence: `issue` cue `issues` at chunk `4991710` offsets `302-308`; context: However, this is dependent on the specific circumstances of the case being examined and the issues raised.
- Evidence: `counterargument_limitation` cue `However` at chunk `4991710` offsets `210-217`; context: However, this is dependent on the specific circumstances of the case being examined and the issues raised.

#### 21053:3:subtheme:3 · paragraphs 20-21

- Raw key terms: `canada, citizenship, immigration, minister, paragraphs, patent, review, standard`
- Display key terms: `paragraphs, patent, review, standard`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: paragraphs, patent, review, standard Rule/authority context: [20] When a board prefers documentary evidence over the testimony of a witness, this involves an issue of credibility and invokes a standard of review of patent unreasonableness: Li v. | [21] When the Court is reviewing a decision involving state protection, the standard of review is reasonableness simpliciter: Sanchez v. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991711` offsets `97-102`; context: [20] When a board prefers documentary evidence over the testimony of a witness, this involves an issue of credibility and invokes a standard of review of patent unreasonableness: Li v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991711` offsets `38-46`; context: [20] When a board prefers documentary evidence over the testimony of a witness, this involves an issue of credibility and invokes a standard of review of patent unreasonableness: Li v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4991711` offsets `132-150`; context: [20] When a board prefers documentary evidence over the testimony of a witness, this involves an issue of credibility and invokes a standard of review of patent unreasonableness: Li v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4991712` offsets `76-94`; context: [21] When the Court is reviewing a decision involving state protection, the standard of review is reasonableness simpliciter: Sanchez v.

#### 21053:3:subtheme:4 · paragraphs 22-25

- Raw key terms: `canada, applicants, board, case, citizenship, documentary, evidence, immigration`
- Display key terms: `case, documentary`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: case, documentary Position/evidence statements: [24] The Applicants submit that it was not open to the Board to prefer documentary evidence to the testimony of the Principal Applicant when there were no adverse credibility findings made regarding the Principal Applica Rule/authority context: [22] The application of the test in Ward is a mixed question of fact and law and the standard of review is reasonableness simpliciter: Stapleton v. | [23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness. Application context: [23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness. | In the absence of stating that the Applicants’ evidence is not credible, the Board concludes that “it gives more weight to the documentary evidence because it comes from reputable, knowledgeable sources, none of whom hav Evidence spans paragraphs 22-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991713` offsets `52-60`; context: [22] The application of the test in Ward is a mixed question of fact and law and the standard of review is reasonableness simpliciter: Stapleton v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4991713` offsets `85-103`; context: [22] The application of the test in Ward is a mixed question of fact and law and the standard of review is reasonableness simpliciter: Stapleton v.
- Evidence: `issue` cue `issues` at chunk `4991714` offsets `168-174`; context: [23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4991714` offsets `851-859`; context: ARGUMENTS
The Applicants
Board Preferring Documentary Evidence
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4991714` offsets `91-104`; context: [23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness.
- Evidence: `reasoning_application` cue `I find` at chunk `4991714` offsets `120-126`; context: [23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness.
- Evidence: `party_position` cue `submit` at chunk `4991715` offsets `20-26`; context: [24] The Applicants submit that it was not open to the Board to prefer documentary evidence to the testimony of the Principal Applicant when there were no adverse credibility findings made regarding the Principal Applicant’s testimony and written evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991715` offsets `83-91`; context: [24] The Applicants submit that it was not open to the Board to prefer documentary evidence to the testimony of the Principal Applicant when there were no adverse credibility findings made regarding the Principal Applicant’s testimony and written evidence.
- Evidence: `reasoning_application` cue `concludes` at chunk `4991715` offsets `508-517`; context: In the absence of stating that the Applicants’ evidence is not credible, the Board concludes that “it gives more weight to the documentary evidence because it comes from reputable, knowledgeable sources, none of whom have any interest in the outcome of this particular refugee hearing.
- Evidence: `evidence_fact` cue `testimony` at chunk `4991716` offsets `134-143`; context: [25] The Applicants point out that clear and convincing proof of a state’s inability to protect can be found by relying solely on the testimony of a claimant: Torres v.

#### 21053:3:subtheme:5 · paragraphs 26-28

- Raw key terms: `applicants, board, canada, citizenship, immigration, minister, protection, state`
- Display key terms: `protection, state`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: protection, state Position/evidence statements: [26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claiman | [27] The Applicants submit that the Board erred by relying upon the Mexican Government’s “serious efforts” in putting into place a legislative and procedural framework to combat kidnappings and corruption. Rule/authority context: Hence, it was under an obligation to explain its rejection in clear terms, and a failure to do so is a reviewable error. Application context: [26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claiman Evidence spans paragraphs 26-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991717` offsets `464-472`; context: ) 2005 FC 873 where, in rejecting a claim, the board did not call into question the applicant’s credibility and accepted her testimony.
- Evidence: `party_position` cue `submit` at chunk `4991717` offsets `29-35`; context: [26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claimant would not receive state protection against the gang she fears should she return to Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991717` offsets `184-192`; context: [26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claimant would not receive state protection against the gang she fears should she return to Mexico.
- Evidence: `governing_rule` cue `under` at chunk `4991717` offsets `945-950`; context: Hence, it was under an obligation to explain its rejection in clear terms, and a failure to do so is a reviewable error.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991717` offsets `130-138`; context: [26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claimant would not receive state protection against the gang she fears should she return to Mexico.
- Evidence: `counterargument_limitation` cue `however` at chunk `4991717` offsets `571-578`; context: The board in Kaur stated in its decision, however, that there was “no credible and trustworthy” evidence to indicate that the applicant would be persecuted if she were returned to Malaysia.
- Evidence: `issue` cue `question` at chunk `4991718` offsets `393-401`; context: The Applicants argue that to require the Principal Applicant to go to corrupt police officials for protection (officials who are in all likelihood are involved with the criminal gangs in question) would amount to requiring the Principal Applicant to risk her life in an effort to seek police assistance merely to prove the unavailability of state protection: D’Mello v.
- Evidence: `party_position` cue `submit` at chunk `4991718` offsets `20-26`; context: [27] The Applicants submit that the Board erred by relying upon the Mexican Government’s “serious efforts” in putting into place a legislative and procedural framework to combat kidnappings and corruption.
- Evidence: `party_position` cue `submit` at chunk `4991719` offsets `20-26`; context: [28] The Applicants submit that the Board’s conclusion that the Applicants should have exhausted all existing remedies before claiming protection in Canada was an incorrect interpretation of Ward and N.
- Evidence: `counterargument_limitation` cue `however` at chunk `4991719` offsets `543-550`; context: Canada (Minister of Citizenship and Immigration) 2005 FC 193 at paragraph 15:
In my view, however, Ward, supra and Kadenko, supra, cannot be interpreted to suggest that an individual will be required to exhaust all avenues before the presumption of state protection can be rebutted (see Sanchez v.

#### 21053:3:subtheme:6 · paragraphs 29-33

- Raw key terms: `applicants, board, evidence, documentary, mexico, police, corruption, canada`
- Display key terms: `documentary, mexico, police, corruption`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: documentary, mexico, police, corruption Position/evidence statements: [30] The Applicants contend that they had good reasons not to seek protection in Mexico, including the degree of corruption existing at all levels of the state and the reprisals they would be exposed to if they filed a c | [31] The Applicants also submit that the Board must weigh all the evidence in its totality and cannot examine each part in isolation: Owusu v. Application context: A reading of the Board’s decision leads one to conclude that the Board ignored significant parts of the evidence and on several occasions made findings of fact which are contrary to the evidence. | They conclude by stating that the Board committed a reviewable error in not mentioning or discussing in its Decision the evidence that corroborated the Applicants’ testimony that corruption is widespread in Mexico, and t Evidence spans paragraphs 29-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4991720` offsets `473-480`; context: Documentary evidence also revealed that kidnapping remains a serious problem at all social levels, regardless of whether the victim is wealthy or not: U.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991720` offsets `109-117`; context: [29] The Applicants say that the Board erred in finding that they had failed to provide clear and convincing evidence of a lack of state protection.
- Evidence: `party_position` cue `contend` at chunk `4991721` offsets `20-27`; context: [30] The Applicants contend that they had good reasons not to seek protection in Mexico, including the degree of corruption existing at all levels of the state and the reprisals they would be exposed to if they filed a complaint with the Mexican authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991721` offsets `345-353`; context: The Board rejected the Applicants’ explanations without taking all of the documentary evidence and their testimony into account.
- Evidence: `party_position` cue `submit` at chunk `4991722` offsets `25-31`; context: [31] The Applicants also submit that the Board must weigh all the evidence in its totality and cannot examine each part in isolation: Owusu v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991722` offsets `66-74`; context: [31] The Applicants also submit that the Board must weigh all the evidence in its totality and cannot examine each part in isolation: Owusu v.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4991722` offsets `95-101`; context: [31] The Applicants also submit that the Board must weigh all the evidence in its totality and cannot examine each part in isolation: Owusu v.
- Evidence: `party_position` cue `argue` at chunk `4991723` offsets `28-33`; context: [32] The Applicants further argue that the Board was selective in its choice of documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991723` offsets `92-100`; context: [32] The Applicants further argue that the Board was selective in its choice of documentary evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991723` offsets `1137-1145`; context: A reading of the Board’s decision leads one to conclude that the Board ignored significant parts of the evidence and on several occasions made findings of fact which are contrary to the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991724` offsets `74-82`; context: [33] The Applicants quote extensively from other parts of the documentary evidence in order to support their submissions concerning corruption in Mexico.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991724` offsets `159-167`; context: They conclude by stating that the Board committed a reviewable error in not mentioning or discussing in its Decision the evidence that corroborated the Applicants’ testimony that corruption is widespread in Mexico, and that in a case such as the present it is pointless to contact the police.

#### 21053:3:subtheme:7 · paragraphs 34-37

- Raw key terms: `applicants, board, canada, citizenship, evidence, immigration, minister, applicant`
- Display key terms: `none`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: no filtered content terms Position/evidence statements: [36] The Applicants argue that the Board again relied on selected portions of the documentary evidence and chose those aspects which supported its conclusion, particularly the anti-corruption efforts of the Fox administr Rule/authority context: 44: …Canadian jurisprudence has repeatedly stated that there is no further burden on an Applicant to seek assistance from human rights organizations. Evidence spans paragraphs 34-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991725` offsets `30-35`; context: [34] The Applicants also take issue with the reasonableness of the Board’s finding that “[t]here is no persuasive evidence to suggest that the Human Rights Commission will not ensure that adequate state protection is available to the claimant should she return to Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991725` offsets `114-122`; context: [34] The Applicants also take issue with the reasonableness of the Board’s finding that “[t]here is no persuasive evidence to suggest that the Human Rights Commission will not ensure that adequate state protection is available to the claimant should she return to Mexico.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4991725` offsets `900-913`; context: 44:
…Canadian jurisprudence has repeatedly stated that there is no further burden on an Applicant to seek assistance from human rights organizations.
- Evidence: `issue` cue `question` at chunk `4991726` offsets `33-41`; context: [35] In addition, the Applicants question the reasonableness of the Board’s finding that the Human Rights Commission is effective when the documentary evidence reveals that it has no legal authority or power to do anything, save making recommendations which are non-binding and carry no legal weight.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991726` offsets `151-159`; context: [35] In addition, the Applicants question the reasonableness of the Board’s finding that the Human Rights Commission is effective when the documentary evidence reveals that it has no legal authority or power to do anything, save making recommendations which are non-binding and carry no legal weight.
- Evidence: `party_position` cue `argue` at chunk `4991727` offsets `20-25`; context: [36] The Applicants argue that the Board again relied on selected portions of the documentary evidence and chose those aspects which supported its conclusion, particularly the anti-corruption efforts of the Fox administration.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991727` offsets `94-102`; context: [36] The Applicants argue that the Board again relied on selected portions of the documentary evidence and chose those aspects which supported its conclusion, particularly the anti-corruption efforts of the Fox administration.
- Evidence: `counterargument_limitation` cue `However` at chunk `4991727` offsets `463-470`; context: However, if there is documentary evidence that is central to the applicant’s position and supports the position, then that evidence must be considered by the Board.

#### 21053:3:subtheme:8 · paragraphs 38-46

- Raw key terms: `board, evidence, protection, applicants, canada, citizenship, documentary, immigration`
- Display key terms: `protection, documentary`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: protection, documentary Position/evidence statements: [42] The Respondent submits that the Applicants’ argument that the Board ignored the documentary evidence which identified deficiencies within the Mexican state protection apparatus is incorrect. | [45] The Respondent contends that the Board did not err in stating that it “preferred” the documentary evidence to the evidence of the Applicants. Application context: The Applicants say that the Board did not pay sufficient attention to the “unable” part of the “unable or, because of that risk, unwilling to avail of the protection” test found in the Act. | [40] The Applicants conclude that the Board disregarded relevant evidence. Evidence spans paragraphs 38-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4991729` offsets `551-558`; context: In deciding whether adequate state protection is available, the Board must consider not only whether there are measures in place that could be used to protect a refugee claimant, but also whether those measures are likely to be effective: Elcock v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991729` offsets `215-223`; context: ) the Court faulted the Board for making no reference to the significant documentary evidence which was supportive of the claim in that case.
- Evidence: `issue` cue `whether` at chunk `4991730` offsets `144-151`; context: The Board must consider not only whether the state is actually capable of providing protection but also whether it is willing to act.
- Evidence: `reasoning_application` cue `because` at chunk `4991730` offsets `640-647`; context: The Applicants say that the Board did not pay sufficient attention to the “unable” part of the “unable or, because of that risk, unwilling to avail of the protection” test found in the Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991731` offsets `65-73`; context: [40] The Applicants conclude that the Board disregarded relevant evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991731` offsets `20-28`; context: [40] The Applicants conclude that the Board disregarded relevant evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4991731` offsets `85-91`; context: The Board cannot, without giving reasonable grounds, ignore or dismiss the contents of a document dealing expressly with state protection in a given region: Renteria v.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4991732` offsets `334-342`; context: The Respondent
Preferring Documentary Evidence
- Evidence: `party_position` cue `submits` at chunk `4991733` offsets `20-27`; context: [42] The Respondent submits that the Applicants’ argument that the Board ignored the documentary evidence which identified deficiencies within the Mexican state protection apparatus is incorrect.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991733` offsets `97-105`; context: [42] The Respondent submits that the Applicants’ argument that the Board ignored the documentary evidence which identified deficiencies within the Mexican state protection apparatus is incorrect.
- Evidence: `counterargument_limitation` cue `but` at chunk `4991733` offsets `267-270`; context: The Board recognized the prevalence of crime and corruption in Mexico, but concluded that the state was dealing with those problems.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991734` offsets `231-239`; context: 1760 at paragraph 10:
In his argument, counsel for the applicant underlines small excerpts from the documentary evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4991734` offsets `432-438`; context: One cannot “dissect” the evidence and use only that portion which underlines one’s point of view.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991735` offsets `85-93`; context: [44] The Respondent points out that a Board has no obligation to list every piece of evidence that it examines: Hassan v.
- Evidence: `party_position` cue `contends` at chunk `4991736` offsets `20-28`; context: [45] The Respondent contends that the Board did not err in stating that it “preferred” the documentary evidence to the evidence of the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991736` offsets `103-111`; context: [45] The Respondent contends that the Board did not err in stating that it “preferred” the documentary evidence to the evidence of the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991737` offsets `96-104`; context: [46] The Respondent says that the Board’s giving more weight to the large amount of documentary evidence, which did not support the assertions made in the Applicant’s PIF narrative and testimony, is not a reviewable error.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4991737` offsets `233-239`; context: The Board cannot simply accept the Applicant’s subjective belief that state protection is not available without sufficient evidence to establish that this fear is objectively reasonable: Kim v.

#### 21053:3:subtheme:9 · paragraphs 47-50

- Raw key terms: `protection, respondent, paragraph, protect, state, villafranca, applicant, applicants`
- Display key terms: `protection, paragraph, protect, state, villafranca`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: protection, paragraph, protect, state, villafranca Position/evidence statements: [48] The Respondent submits that international refugee law is only intended to come into play in situations where home state protection is unavailable, and then only in certain situations: Ward. Application context: The Respondent also says that the Principal Applicant is not entitled to seek the surrogate protection of Canada simply because there is some risk that she may be the victim of a crime in her country of nationality. Evidence spans paragraphs 47-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4991738` offsets `501-508`; context: The Respondent also says that the Principal Applicant is not entitled to seek the surrogate protection of Canada simply because there is some risk that she may be the victim of a crime in her country of nationality.
- Evidence: `party_position` cue `submits` at chunk `4991739` offsets `20-27`; context: [48] The Respondent submits that international refugee law is only intended to come into play in situations where home state protection is unavailable, and then only in certain situations: Ward.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991740` offsets `184-192`; context: The Applicant’s evidence that she did not believe the police would protect her was not sufficient to rebut the presumption of state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991741` offsets `595-603`; context: Moreover, as Mexico is a functioning multiparty democracy, the burden of proof on the Applicants to provide clear and convincing evidence to rebut the state’s presumed ability to protect is also higher than in other cases.

#### 21053:3:subtheme:10 · paragraphs 51-52

- Raw key terms: `applicants, board, cites, respondent, submits, analysis, asserting, attempting`
- Display key terms: `cites, submits, analysis, asserting, attempting`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: cites, submits, analysis, asserting, attempting Position/evidence statements: The Respondent submits that there was insufficient evidence to establish that the Los Macizos gang in question had any influence over the local police force. | The Respondent submits it was reasonable for the Board to conclude that the Applicants had not done so in this case. Application context: The Respondent submits it was reasonable for the Board to conclude that the Applicants had not done so in this case. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991742` offsets `333-341`; context: The Respondent submits that there was insufficient evidence to establish that the Los Macizos gang in question had any influence over the local police force.
- Evidence: `party_position` cue `submits` at chunk `4991742` offsets `246-253`; context: The Respondent submits that there was insufficient evidence to establish that the Los Macizos gang in question had any influence over the local police force.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991742` offsets `282-290`; context: The Respondent submits that there was insufficient evidence to establish that the Los Macizos gang in question had any influence over the local police force.
- Evidence: `party_position` cue `submits` at chunk `4991743` offsets `220-227`; context: The Respondent submits it was reasonable for the Board to conclude that the Applicants had not done so in this case.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991743` offsets `263-271`; context: The Respondent submits it was reasonable for the Board to conclude that the Applicants had not done so in this case.

#### 21053:3:subtheme:11 · paragraphs 53-62

- Raw key terms: `applicant, board, evidence, principal, protection, case, decision, documentary`
- Display key terms: `principal, protection, case, documentary`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: principal, protection, case, documentary Application context: [56] The Board says that it gives less weight to the “written evidence” and “oral testimony” of the Principal Applicant because the Principal Applicant has an interest in this case and the other sources are reputable. | The Board adopted as a principle of its Decision that other evidence was to be preferred over the “written evidence and oral testimony given by the Applicant” because the other evidence came from sources having no intere Evidence spans paragraphs 53-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4991744` offsets `33-39`; context: [53] I have reviewed each of the issues raised by the Applicant.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4991744` offsets `92-100`; context: More Weight to Documentary Evidence
- Evidence: `evidence_fact` cue `evidence` at chunk `4991745` offsets `71-79`; context: [54] With regard to the Board’s stated preference for the “documentary evidence, prepared by reputable sources having no interest in the outcome of this case, describing country conditions and availability of state protection for individuals similarly situated as the claimant” as opposed to the “written evidence and oral testimony given by the claimant,” there is, in my view, a reviewable error in this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991746` offsets `573-581`; context: The Board did not weigh the Principal Applicant’s credible subjective beliefs concerning the unavailability of state protection against other documentary evidence that suggested state protection was adequate, even though not perfect.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991747` offsets `62-70`; context: [56] The Board says that it gives less weight to the “written evidence” and “oral testimony” of the Principal Applicant because the Principal Applicant has an interest in this case and the other sources are reputable.
- Evidence: `reasoning_application` cue `because` at chunk `4991747` offsets `120-127`; context: [56] The Board says that it gives less weight to the “written evidence” and “oral testimony” of the Principal Applicant because the Principal Applicant has an interest in this case and the other sources are reputable.
- Evidence: `evidence_fact` cue `found that` at chunk `4991748` offsets `262-272`; context: Canada (Minister of Citizenship and Immigration) 2004 FC 1037 at paragraph 7, which warning has been reiterated by this Court in other cases, including Kaur, where Justice Dawson found that the Board could not make the finding it did unless it rejected the applicant’s testimony and explained why it rejected it.
- Evidence: `counterargument_limitation` cue `However` at chunk `4991748` offsets `583-590`; context: However, it is equally trite law that where the RPD rejects sworn testimony, reasons must be given for doing so.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991749` offsets `71-79`; context: [58] In the present case, the Board did not just weigh the Applicant’s evidence against other evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4991749` offsets `263-270`; context: The Board adopted as a principle of its Decision that other evidence was to be preferred over the “written evidence and oral testimony given by the Applicant” because the other evidence came from sources having no interest in the case and because those sources were more reputable.
- Evidence: `counterargument_limitation` cue `however` at chunk `4991751` offsets `237-244`; context: ” Even here, however, the Board does not say that the Applicants were obliged to exhaust “all” courses of action available to them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991752` offsets `9-17`; context: [61] The evidence is that the Principal Applicant did not attempt to seek protection from the police, or to contact any other agency or institution for assistance.

#### 21053:3:subtheme:12 · paragraphs 63-65

- Raw key terms: `serious, board, efforts, protection, actual, address, applicants, available`
- Display key terms: `serious, efforts, protection, actual, address, available`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: serious, efforts, protection, actual, address, available Application context: The Board examines and discusses the actual impact of various initiatives and concludes that they are having an impact and that real protection is available. Evidence spans paragraphs 63-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991754` offsets `44-49`; context: [63] I can find no reviewable error on this issue.
- Evidence: `issue` cue `whether` at chunk `4991755` offsets `205-212`; context: [64] The Applicants say that the Board relied upon the Mexican government’s “serious efforts” to put in place a legislative and procedural framework to combat kidnapping and corruption but did not address whether those efforts have resulted in effective protection.
- Evidence: `reasoning_application` cue `concludes` at chunk `4991756` offsets `201-210`; context: The Board examines and discusses the actual impact of various initiatives and concludes that they are having an impact and that real protection is available.

#### 21053:3:subtheme:13 · paragraphs 66-69

- Raw key terms: `protection, state, authorities, case, claimant, democracy, find, issue`
- Display key terms: `protection, state, authorities, case, democracy, find`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: protection, state, authorities, case, democracy, find Application context: [67] The decisive issue in this case is the Principal Applicant’s contention that she declined to seek state protection because there was no point in doing so. | In view of the fact that the United States is a democracy that has adopted a comprehensive scheme to ensure those who object to military service are dealt with fairly, I conclude that the appellants have adduced insuffic Evidence spans paragraphs 66-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991757` offsets `44-49`; context: [66] I can find no reviewable error on this issue.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4991757` offsets `108-116`; context: Error in Applying Ward and Failure to Deal with Contrary Evidence
- Evidence: `issue` cue `issue` at chunk `4991758` offsets `18-23`; context: [67] The decisive issue in this case is the Principal Applicant’s contention that she declined to seek state protection because there was no point in doing so.
- Evidence: `reasoning_application` cue `because` at chunk `4991758` offsets `120-127`; context: [67] The decisive issue in this case is the Principal Applicant’s contention that she declined to seek state protection because there was no point in doing so.
- Evidence: `reasoning_application` cue `conclude` at chunk `4991759` offsets `1002-1010`; context: In view of the fact that the United States is a democracy that has adopted a comprehensive scheme to ensure those who object to military service are dealt with fairly, I conclude that the appellants have adduced insufficient support to satisfy this high threshold.

#### 21053:3:subtheme:14 · paragraphs 70-73

- Raw key terms: `applicants, board, documentary, evidence, state, amount, applicant, arguments`
- Display key terms: `documentary, state, amount, arguments`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: documentary, state, amount, arguments Application context: [71] The Applicants point out that there was a significant amount of documentary evidence supporting their position that the Mexican state cannot protect them and the Principal Applicant could not go to the police becaus Evidence spans paragraphs 70-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991761` offsets `12-17`; context: [70] So the issue becomes whether, in the present case, the Board was dealing with no more than a subjective reluctance to engage the state.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991762` offsets `81-89`; context: [71] The Applicants point out that there was a significant amount of documentary evidence supporting their position that the Mexican state cannot protect them and the Principal Applicant could not go to the police because of their corrupt involvement with kidnappers and the inevitable reprisals that would follow any complaint.
- Evidence: `reasoning_application` cue `because` at chunk `4991762` offsets `214-221`; context: [71] The Applicants point out that there was a significant amount of documentary evidence supporting their position that the Mexican state cannot protect them and the Principal Applicant could not go to the police because of their corrupt involvement with kidnappers and the inevitable reprisals that would follow any complaint.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4991762` offsets `139-145`; context: [71] The Applicants point out that there was a significant amount of documentary evidence supporting their position that the Mexican state cannot protect them and the Principal Applicant could not go to the police because of their corrupt involvement with kidnappers and the inevitable reprisals that would follow any complaint.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991763` offsets `88-96`; context: [72] The Applicants say that the Board was very selective in its use of the documentary evidence and simply chose passages that would support its conclusions, while neglecting to deal with evidence that was contrary to those conclusions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991764` offsets `115-123`; context: [73] The Respondent makes the usual arguments that the Board was not obliged to mention every piece of documentary evidence, and that the Board fully recognizes that corruption and kidnapping continue to be a problem in Mexico, and that state protection is not perfect.

#### 21053:3:subtheme:15 · paragraphs 74-74

- Raw key terms: `active, agree, analysis, applicants, available, barnes, board, board's`
- Display key terms: `active, agree, analysis, available, barnes, board's`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: active, agree, analysis, available, barnes, board's Evidence spans paragraphs 74-74. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991765` offsets `234-239`; context: When faced with a similar issue in Sanchez, Justice Barnes had the following to say at paragraph 11:
I also do not agree that the Board ignored documentary evidence which detailed deficiencies within the Mexican criminal justice system.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991765` offsets `364-372`; context: When faced with a similar issue in Sanchez, Justice Barnes had the following to say at paragraph 11:
I also do not agree that the Board ignored documentary evidence which detailed deficiencies within the Mexican criminal justice system.
- Evidence: `counterargument_limitation` cue `but` at chunk `4991765` offsets `563-566`; context: The Board referred to problems of official corruption and to the prevalence of crime (including kidnapping) in Mexico but found that the state was motivated and was taking active steps to respond.

#### Section text

[16] The following provisions of the Act are applicable in these proceedings:
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
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
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Personne à protéger
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.
STANDARD OF REVIEW

[17] In Dunsmuir v. New Brunswick, 2008 SCC 9, the Supreme Court of Canada recognized that, although the reasonableness simpliciter and patent unreasonableness standards are theoretically different, “the analytical problems that arise in trying to apply the different standards undercut any conceptual usefulness created by the inherently greater flexibility of having multiple standards of review” (Dunsmuir at para. 44). Consequently, the Supreme Court of Canada held that the two reasonableness standards should be collapsed into a single form of “reasonableness” review.

[18] The Supreme Court of Canada in Dunsmuir also held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to the particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis.

[19] Generally speaking, this Court has held that refugee decisions be reviewed on a standard of patent unreasonableness: Kovacs v. Canada (Minister of Citizenship and Immigration), [2006] 2 F.C.R. 455 (F.C.). However, this is dependent on the specific circumstances of the case being examined and the issues raised.

[20] When a board prefers documentary evidence over the testimony of a witness, this involves an issue of credibility and invokes a standard of review of patent unreasonableness: Li v. Canada (Minister of Citizenship and Immigration) 2001 FCT 1238 at paragraph 23 and Yener v. Canada (Minister of Citizenship and Immigration) 2008 FC 372 at paragraphs 28 and 29.

[21] When the Court is reviewing a decision involving state protection, the standard of review is reasonableness simpliciter: Sanchez v. Canada (Minister of Citizenship and Immigration) 2008 FC 66 except when reviewing the existence of an internal flight alternative, when a standard of patent unreasonableness has been used: Rosales v. Canada (Minister of Citizenship and Immigration) 2008 FC 257 at paragraphs 12 and 13.

[22] The application of the test in Ward is a mixed question of fact and law and the standard of review is reasonableness simpliciter: Stapleton v. Canada (Minister of Citizenship and Immigration) 2006 FC 1320 at paragraph 18.

[23] Thus, in light of the Supreme Court of Canada’s decision in Dunsmuir and the previous jurisprudence of this Court, I find the standard of review applicable to the issues in this case to be reasonableness. When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at paragraph 47). Put another way, the Court should only intervene if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law”.
ARGUMENTS
The Applicants
Board Preferring Documentary Evidence

[24] The Applicants submit that it was not open to the Board to prefer documentary evidence to the testimony of the Principal Applicant when there were no adverse credibility findings made regarding the Principal Applicant’s testimony and written evidence. The Applicants rely upon Coitinho v. Canada (Minister of Citizenship and Immigration) 2004 FC 1037 at paragraph 7:
The Board goes on to make a most disturbing finding. In the absence of stating that the Applicants’ evidence is not credible, the Board concludes that “it gives more weight to the documentary evidence because it comes from reputable, knowledgeable sources, none of whom have any interest in the outcome of this particular refugee hearing.” This statement is tantamount to stating that documentary evidence should always be preferred to that of refugee claimant’s because the latter is interested in the outcome of the hearing. If permitted, such reasoning would always defeat a claimant’s evidence. The Board’s decision in this case does not inform the reader why the Applicants’ evidence, when supposed to be presumed true (Adu supra) was considered suspect…

[25] The Applicants point out that clear and convincing proof of a state’s inability to protect can be found by relying solely on the testimony of a claimant: Torres v. Canada (Minister of Citizenship and Immigration) 2005 FC 660 and Musorin v. Canada (Minister of Citizenship and Immigration) 2005 FC 408. In the present case, there are instances where the Board’s findings of credibility are inextricably linked to its findings on state protection, so that an error in the former invalidates the latter: Lebbe v. Canada (Minister of Citizenship and Immigration) 2006 FC 564. The Board erred in preferring, without any reasons, the documentary evidence to the oral and written evidence of the Primary Applicant. The Applicants say this invalidates the Board’s findings on state protection.

[26] The Applicants go on to submit that, in the absence of explicit findings of non-credibility, it was not open to the Board to conclude that “the panel does not have any persuasive evidence to believe that the claimant would not receive state protection against the gang she fears should she return to Mexico.” The Applicants rely on Kaur v. Canada (Minister of Citizenship and Immigration.) 2005 FC 873 where, in rejecting a claim, the board did not call into question the applicant’s credibility and accepted her testimony. The board in Kaur stated in its decision, however, that there was “no credible and trustworthy” evidence to indicate that the applicant would be persecuted if she were returned to Malaysia. Justice Dawson found that the board could not make such a finding unless it rejected the applicant’s testimony, which it appeared not to do. If the Board in the present case did reject the Applicant’s testimony. Hence, it was under an obligation to explain its rejection in clear terms, and a failure to do so is a reviewable error.
Existence of “Serious Efforts”

[27] The Applicants submit that the Board erred by relying upon the Mexican Government’s “serious efforts” in putting into place a legislative and procedural framework to combat kidnappings and corruption. The Applicants argue that to require the Principal Applicant to go to corrupt police officials for protection (officials who are in all likelihood are involved with the criminal gangs in question) would amount to requiring the Principal Applicant to risk her life in an effort to seek police assistance merely to prove the unavailability of state protection: D’Mello v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 72 (F.C.T.D.) and Torres.
Application of Ward

[28] The Applicants submit that the Board’s conclusion that the Applicants should have exhausted all existing remedies before claiming protection in Canada was an incorrect interpretation of Ward and N.K. v. Canada (Minister of Citizenship and Immigration), [1996] F.C.J. No. 1376 (F.C.A.), as the law does not impose any obligation on refugee claimants to “exhaust all courses of action open to him or her.” The Applicants cite and rely upon Chaves v. Canada (Minister of Citizenship and Immigration) 2005 FC 193 at paragraph 15:
In my view, however, Ward, supra and Kadenko, supra, cannot be interpreted to suggest that an individual will be required to exhaust all avenues before the presumption of state protection can be rebutted (see Sanchez v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 536 (T.D.) and Peralta v. Canada (Minister of Citizenship and Immigration) (1996), 123 F.T.R. 153 (F.C.T.D.))…

[29] The Applicants say that the Board erred in finding that they had failed to provide clear and convincing evidence of a lack of state protection. There was evidence before the Board which demonstrated the degree of corruption within police forces in Mexico, and that many police officials are involved in activities related to kidnappings by various gangs. Documentary evidence also revealed that kidnapping remains a serious problem at all social levels, regardless of whether the victim is wealthy or not: U.S. Department of State: Country Reports on Human Rights Practices: Mexico, 2006.

[30] The Applicants contend that they had good reasons not to seek protection in Mexico, including the degree of corruption existing at all levels of the state and the reprisals they would be exposed to if they filed a complaint with the Mexican authorities. The Board rejected the Applicants’ explanations without taking all of the documentary evidence and their testimony into account. The Applicants submit that the Board misunderstood and misapplied Ward and N.K.. The Board’s finding that the Applicants should have first approached the police in Mexico was unreasonable.

[31] The Applicants also submit that the Board must weigh all the evidence in its totality and cannot examine each part in isolation: Owusu v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 33 (F.C.A.); Lai v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 826 (F.C.A.) and Hilo v. Canada (Minister of Employment and Immigration), [1991] F.C.J. No. 228 (F.C.A.).

[32] The Applicants further argue that the Board was selective in its choice of documentary evidence. For example, the Board relied on reports that Mexico maintains preventative and judicial police forces, yet the Board does not mention that the state-level preventive police force is supposed to be the most corrupt of all. As well, the Board relies on the fact that the Mexican Government continues to push forward anti-corruption reforms, but failed to mention other documentary evidence that expressed reservations about the commitment and the ability of the government to achieve its stated goals. This selective reliance on documentary evidence by the Board makes the decision non-sustainable: Manoharan v. Canada (Minister of Citizenship and Immigration), [1996] F.C.J. No. 356 (F.C.T.D.) at para. 3; Muralidharan v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 843 (F.C.T.D.) and Balasingham v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 1387 (F.C.T.D.). The Applicants quote and rely upon Manoharan and the words of Justice Reed:
3. A reading of the Board’s decision leads one to conclude that the Board ignored significant parts of the evidence and on several occasions made findings of fact which are contrary to the evidence.

[33] The Applicants quote extensively from other parts of the documentary evidence in order to support their submissions concerning corruption in Mexico. They conclude by stating that the Board committed a reviewable error in not mentioning or discussing in its Decision the evidence that corroborated the Applicants’ testimony that corruption is widespread in Mexico, and that in a case such as the present it is pointless to contact the police.

[34] The Applicants also take issue with the reasonableness of the Board’s finding that “[t]here is no persuasive evidence to suggest that the Human Rights Commission will not ensure that adequate state protection is available to the claimant should she return to Mexico.” The Applicants say that the case law demonstrates that refugee claimants have no obligation to turn to a country’s human rights organization for help. In Kaur v. Canada (Minister of Citizenship and Immigration), [2005] F.C.J. No. 1858 (FC), this Court held that it was unreasonable for a board to have expected the Applicants to have approached the country’s human rights organization for help. In coming to that conclusion, Justice de Montigny at paragraph 31 in Kaur cites the decision of Justice Lemieux in Balogh v. Canada (Minister of Citizenship and Immigration), [2002] F.C.J. No. 1080 (F.C.T.D.) at para. 44:
…Canadian jurisprudence has repeatedly stated that there is no further burden on an Applicant to seek assistance from human rights organizations.

[35] In addition, the Applicants question the reasonableness of the Board’s finding that the Human Rights Commission is effective when the documentary evidence reveals that it has no legal authority or power to do anything, save making recommendations which are non-binding and carry no legal weight.

[36] The Applicants argue that the Board again relied on selected portions of the documentary evidence and chose those aspects which supported its conclusion, particularly the anti-corruption efforts of the Fox administration. The Applicants cite and rely upon P.K.R. v. Canada (Minister of Citizenship and Immigration), [2004] FC 1460 at paragraph 17:
The law is clear that the Board need not refer to every piece of evidence that was before it in its decision. However, if there is documentary evidence that is central to the applicant’s position and supports the position, then that evidence must be considered by the Board. The failure to refer to this evidence is a reviewable error.

[37] The Applicants also rely upon Babai v. Canada (Minister of Citizenship and Immigration) 2004 FC 1341 at paragraphs 35 and 36 and Cepeda-Gutierrez v. Canada (Minister of Citizenship and Immigration) (1998), 157 F.T.R. 35 (T.D.) at paragraphs 16 and 17.

[38] The Applicants point out that in Orgona v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1316 (F.C.T.D.) the Court faulted the Board for making no reference to the significant documentary evidence which was supportive of the claim in that case. The Court concluded that, when documentary evidence is selectively relied upon, a tribunal errs in law by ignoring relevant evidence. The Applicants also cite and rely upon T.M.C. v. Canada (Minister of Citizenship and Immigration) 2004 FC 1670 for the following:
8. In deciding whether adequate state protection is available, the Board must consider not only whether there are measures in place that could be used to protect a refugee claimant, but also whether those measures are likely to be effective: Elcock v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 1438 (T.D.) (QL); Cho v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1371 (T.D.) (QL). There is no doubt that Grenada is beginning to take steps to address what appears to be a serious problem of violence against women and children. However, as I read the documentary evidence that was before the Board, these are merely incipient measures indicating a growing willingness to respond to these forms of violence. They fall far short of providing actual protection, except in a very small number of cases.

[39] The Applicants agree that state protection does not need to be perfect, but it does have to be effective. The Board must consider not only whether the state is actually capable of providing protection but also whether it is willing to act. Legislation and procedures in themselves do not suffice to establish the reality of protection unless they are given effect in practice: Molnar v. Canada (Minister of Citizenship and Immigration) 2002 FCT 1081 and Mohacsi v. Canada (Minister of Citizenship and Immigration) 2003 FCT 429. The Applicants say that the Board did not pay sufficient attention to the “unable” part of the “unable or, because of that risk, unwilling to avail of the protection” test found in the Act.

[40] The Applicants conclude that the Board disregarded relevant evidence. The Board cannot, without giving reasonable grounds, ignore or dismiss the contents of a document dealing expressly with state protection in a given region: Renteria v. Canada (Minister of Citizenship and Immigration) 2006 FC 160.

[41] The Board committed several reviewable errors which affected the fairness of the Applicants’ hearing. The Board also erred in law in finding that the Applicants were not Convention refugees or persons in need of protection. These errors are important enough to constitute reviewable errors.
The Respondent
Preferring Documentary Evidence

[42] The Respondent

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 21053:4 · paragraphs 75-82

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2c7699cbdabf7a97158d0473eecf4d3496f558714090be8557f809d3207ce9a5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:4:subtheme:1 · paragraphs 75-76

- Raw key terms: `evidence, adduced, approach, board, cannot, case, clear, correct`
- Display key terms: `adduced, approach, cannot, case, clear, correct`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: adduced, approach, cannot, case, clear, correct Rule/authority context: [76] Notwithstanding these clear principles, much will depend upon the facts of each case and the approach of the Board to the particular situation before it and the evidence adduced. Evidence spans paragraphs 75-76. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991766` offsets `120-128`; context: [75] I also think the Respondent is correct to emphasize that in Johal at paragraph 10 that “[o]ne cannot ‘dissect’ the evidence and use only that portion which underlines one’s point of view.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991767` offsets `166-174`; context: [76] Notwithstanding these clear principles, much will depend upon the facts of each case and the approach of the Board to the particular situation before it and the evidence adduced.
- Evidence: `governing_rule` cue `principles` at chunk `4991767` offsets `33-43`; context: [76] Notwithstanding these clear principles, much will depend upon the facts of each case and the approach of the Board to the particular situation before it and the evidence adduced.

#### 21053:4:subtheme:2 · paragraphs 77-77

- Raw key terms: `absence, addition, administrative, agencies, agency, agency's, allocation, analysis`
- Display key terms: `absence, addition, administrative, agencies, agency, agency's, allocation, analysis`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: absence, addition, administrative, agencies, agency, agency's, allocation, analysis Rule/authority context: [77] In this regard, the Court must also keep in mind the oft-stated principles enunciated by Justice Evans in Cepeda: 14. Application context: This inference is made easier to draw because the Board’s reasons dealt with other items of evidence indicating that a return would not be unduly harsh. Evidence spans paragraphs 77-77. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991768` offsets `3247-3255`; context: In other words, the agency's burden of explanation increases with the relevance of the evidence in question to the disputed facts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991768` offsets `405-413`; context: 1(4)(d) of the Federal Court Act does not authorize the Court to substitute its view of the facts for that of the Board, which has the benefit not only of seeing and hearing the witnesses, but also of the expertise of its members in assessing evidence relating to facts that are within their area of specialized expertise.
- Evidence: `governing_rule` cue `principles` at chunk `4991768` offsets `69-79`; context: [77] In this regard, the Court must also keep in mind the oft-stated principles enunciated by Justice Evans in Cepeda:
14.
- Evidence: `reasoning_application` cue `because` at chunk `4991768` offsets `4142-4149`; context: This inference is made easier to draw because the Board’s reasons dealt with other items of evidence indicating that a return would not be unduly harsh.

#### 21053:4:subtheme:3 · paragraphs 78-79

- Raw key terms: `applicant, kidnappers, police, address, agency, applicants, because, board`
- Display key terms: `kidnappers, police, address, agency, because`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: kidnappers, police, address, agency, because Position/evidence statements: [78] The Principal Applicant contends that she fears kidnappers, so that the only relevant agency of protection is the police. Application context: [79] She says she did not go to the police because they are in league with kidnappers and reprisals would inevitably follow. Evidence spans paragraphs 78-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `contends` at chunk `4991769` offsets `29-37`; context: [78] The Principal Applicant contends that she fears kidnappers, so that the only relevant agency of protection is the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991770` offsets `161-169`; context: She also says that there was cogent evidence before the Board to support this position, which evidence the Board did not address and, as was pointed out by this Court in Petra Kimma Roberts v.
- Evidence: `reasoning_application` cue `because` at chunk `4991770` offsets `43-50`; context: [79] She says she did not go to the police because they are in league with kidnappers and reprisals would inevitably follow.
- Evidence: `counterargument_limitation` cue `However` at chunk `4991770` offsets `539-546`; context: However, if there is documentary evidence that is central to the applicant’s position and supports this position, then that evidence must be considered by the Board.

#### 21053:4:subtheme:4 · paragraphs 80-82

- Raw key terms: `board, evidence, case, initiatives, report, abducted, abuse, abuses`
- Display key terms: `case, initiatives, report, abducted, abuse, abuses`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: case, initiatives, report, abducted, abuse, abuses Rule/authority context: [80] In the present case, the Board referred to the initiatives of the Fox administration to support the Board’s conclusions, but did not deal, for example, with the evidence in Lost in Transition: Bold Ambitions, Limite Evidence spans paragraphs 80-82. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4991771` offsets `306-312`; context: [80] In the present case, the Board referred to the initiatives of the Fox administration to support the Board’s conclusions, but did not deal, for example, with the evidence in Lost in Transition: Bold Ambitions, Limited Results Under Fox, a May 2006 report about Mexico’s efforts to address human rights issues, which unambiguously concluded that abuses related to law enforcement misconduct continue to exist and that “while ambitious on paper,” the Fox initiatives “have largely failed to achieve their principal goals.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991771` offsets `166-174`; context: [80] In the present case, the Board referred to the initiatives of the Fox administration to support the Board’s conclusions, but did not deal, for example, with the evidence in Lost in Transition: Bold Ambitions, Limited Results Under Fox, a May 2006 report about Mexico’s efforts to address human rights issues, which unambiguously concluded that abuses related to law enforcement misconduct continue to exist and that “while ambitious on paper,” the Fox initiatives “have largely failed to achieve their principal goals.
- Evidence: `governing_rule` cue `Under` at chunk `4991771` offsets `230-235`; context: [80] In the present case, the Board referred to the initiatives of the Fox administration to support the Board’s conclusions, but did not deal, for example, with the evidence in Lost in Transition: Bold Ambitions, Limited Results Under Fox, a May 2006 report about Mexico’s efforts to address human rights issues, which unambiguously concluded that abuses related to law enforcement misconduct continue to exist and that “while ambitious on paper,” the Fox initiatives “have largely failed to achieve their principal goals.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991772` offsets `103-111`; context: [81] In addition, with regards to the Mexican state’s initiatives against kidnapping, there was cogent evidence before the Board that “while there has been success in dismantling major kidnapping rings, the result has apparently been a proliferation of smaller groups that are ‘more ruthless’ when the victims’ family is unable to pay the ransom demand…” These so-called “amateurish outfits” have been known to be extremely violent towards their captives, reportedly raping female victims and committing bodily harm against abducted males.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991773` offsets `32-40`; context: [82] There was also significant evidence before the Board in this case of police complicity with kidnappers and that “citizens are hesitant to report police abuse and many people are cautious about going anywhere near a police station.

#### Section text

[75] I also think the Respondent is correct to emphasize that in Johal at paragraph 10 that “[o]ne cannot ‘dissect’ the evidence and use only that portion which underlines one’s point of view.”

[76] Notwithstanding these clear principles, much will depend upon the facts of each case and the approach of the Board to the particular situation before it and the evidence adduced.

[77] In this regard, the Court must also keep in mind the oft-stated principles enunciated by Justice Evans in Cepeda:
14. It is well established that section 18.1(4)(d) of the Federal Court Act does not authorize the Court to substitute its view of the facts for that of the Board, which has the benefit not only of seeing and hearing the witnesses, but also of the expertise of its members in assessing evidence relating to facts that are within their area of specialized expertise. In addition, and more generally, considerations of the efficient allocation of decision-making resources between administrative agencies and the courts strongly indicate that the role to be played in fact-finding by the Court on an application for judicial review should be merely residual. Thus, in order to attract judicial intervention under section 18.1(4)(d), the applicant must satisfy the Court, not only that the Board made a palpably erroneous finding of material fact, but also that the finding was made “without regard to the evidence”: see, for example, Rajapakse v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 649 (F.C.T.D.); Sivasamboo v. Canada (Minister of Employment and Immigration), [1995] 1 F.C. 741 (F.C.T.D.).
15 The Court may infer that the administrative agency under review made the erroneous finding of fact "without regard to the evidence" from the agency's failure to mention in its reasons some evidence before it that was relevant to the finding, and pointed to a different conclusion from that reached by the agency. Just as a court will only defer to an agency's interpretation of its constituent statute if it provides reasons for its conclusion, so a court will be reluctant to defer to an agency's factual determinations in the absence of express findings, and an analysis of the evidence that shows how the agency reached its result.
16. On the other hand, the reasons given by administrative agencies are not to be read hypercritically by a court (Medina v. Canada (Minister of Employment and Immigration) (1990), 12 Imm L.R. (2d) 33 (F.C.A.)), nor are agencies required to refer to every piece of evidence that they received that is contrary to their finding, and to explain how they dealt with it (see, for example, Hassan v. Canada (Minister of Employment and Immigration) (1992), 147 N.R. 317 (F.C.A.). That would be far too onerous a burden to impose upon administrative decision-makers who may be struggling with a heavy case-load and inadequate resources. A statement by the agency in its reasons for decision that, in making its findings, it considered all the evidence before it, will often suffice to assure the parties, and a reviewing court, that the agency directed itself to the totality of the evidence when making its findings of fact.
17. However, the more important the evidence that is not mentioned specifically and analyzed in the agency's reasons, the more willing a court may be to infer from the silence that the agency made an erroneous finding of fact “without regard to the evidence”: Bains v. Canada (Minister of Employment and Immigration) (1993), 63 F.T.R. 312 (F.C.T.D.). In other words, the agency's burden of explanation increases with the relevance of the evidence in question to the disputed facts. Thus, a blanket statement that the agency has considered all the evidence will not suffice when the evidence omitted from any discussion in the reasons appears squarely to contradict the agency's finding of fact. Moreover, when the agency refers in some detail to evidence supporting its finding, but is silent on evidence pointing to the opposite conclusion, it may be easier to infer that the agency overlooked the contradictory evidence when making its finding of fact.
…
27. Finally, I must consider whether the Refugee Division made this erroneous finding of fact “without regard for the material before it.” In my view, the evidence was so important to the applicant’s case that it can be inferred from the Refugee Division’s failure to mention it in its reasons that the finding of fact was made without regard to it. This inference is made easier to draw because the Board’s reasons dealt with other items of evidence indicating that a return would not be unduly harsh. The inclusion of the “boilerplate” assertion that the Board considered all the evidence before it is not sufficient to prevent this inference from being drawn, given the importance of the evidence to the applicant’s claim.

[78] The Principal Applicant contends that she fears kidnappers, so that the only relevant agency of protection is the police. Other organizations that monitor and deal with corruption in the police force are not relevant to the risks which the Applicants face.

[79] She says she did not go to the police because they are in league with kidnappers and reprisals would inevitably follow. She also says that there was cogent evidence before the Board to support this position, which evidence the Board did not address and, as was pointed out by this Court in Petra Kimma Roberts v. Canada (Minister of Citizenship and Immigration), [2004] FC 1460 at paragraph 17, this was a reviewable error:
The law is clear that the Board need not refer to every piece of evidence that was before it in its decision. However, if there is documentary evidence that is central to the applicant’s position and supports this position, then that evidence must be considered by the Board. The failure to refer to this evidence is a reviewable error.

[80] In the present case, the Board referred to the initiatives of the Fox administration to support the Board’s conclusions, but did not deal, for example, with the evidence in Lost in Transition: Bold Ambitions, Limited Results Under Fox, a May 2006 report about Mexico’s efforts to address human rights issues, which unambiguously concluded that abuses related to law enforcement misconduct continue to exist and that “while ambitious on paper,” the Fox initiatives “have largely failed to achieve their principal goals.”

[81] In addition, with regards to the Mexican state’s initiatives against kidnapping, there was cogent evidence before the Board that “while there has been success in dismantling major kidnapping rings, the result has apparently been a proliferation of smaller groups that are ‘more ruthless’ when the victims’ family is unable to pay the ransom demand…” These so-called “amateurish outfits” have been known to be extremely violent towards their captives, reportedly raping female victims and committing bodily harm against abducted males.

[82] There was also significant evidence before the Board in this case of police complicity with kidnappers and that “citizens are hesitant to report police abuse and many people are cautious about going anywhere near a police station.”

## 21053:5 · paragraphs 83-90

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c8d00f2c25f0e011e60a6ebed328b54afcce0128de34ab1ed3c5f47c15851bbc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:5:subtheme:1 · paragraphs 83-84

- Raw key terms: `evidence, organizations, accountable, actions, authorities, clear, commissions, competence`
- Display key terms: `organizations, accountable, actions, authorities, clear, commissions, competence`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: organizations, accountable, actions, authorities, clear, commissions, competence Evidence spans paragraphs 83-84. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991774` offsets `229-237`; context: [83] There was also clear evidence that the various Human Rights Commissions were “on the whole ineffective in holding authorities accountable for their actions and that many national and international human rights organizations question their competence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991774` offsets `26-34`; context: [83] There was also clear evidence that the various Human Rights Commissions were “on the whole ineffective in holding authorities accountable for their actions and that many national and international human rights organizations question their competence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991775` offsets `20-28`; context: [84] There was also evidence that the preventive police are the most corrupt of the police organizations in Mexico.

#### 21053:5:subtheme:2 · paragraphs 85-90

- Raw key terms: `board, evidence, cogent, conclusions, contradicts, applicant, case, clear`
- Display key terms: `cogent, conclusions, contradicts, case, clear`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: cogent, conclusions, contradicts, case, clear Rule/authority context: [89] Reading the Decision as a whole, it is my view that the Board does not engage with clear evidence that contradicts his own inclusions in the way that the jurisprudence of this Court says it should engage with that e Application context: This becomes particularly problematic in a case where, as I have found, the Board also made a reviewable error by discounting the Principal Applicant’s own testimony because she was not a disinterested party. Evidence spans paragraphs 85-90. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4991776` offsets `315-320`; context: All of this is highly relevant to the issue of why the Principal Applicant did not go to the police.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991776` offsets `34-42`; context: [85] All in all, there was cogent evidence before the Board that the police in Mexico are corrupt and have extensive involvement with kidnapping gangs, that human rights commissions are ineffective, and that government initiatives to deal with the problem have largely failed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991777` offsets `72-80`; context: [86] In other words, it was the usual “mixed bag,” but in this case the evidence that refuted the Board’s conclusions on this point was so cogent and so important to the Applicants’ case, that the Board’s failure to deal with it and to simply rely upon the usual presumptions of state protection looks more like defending a general position on Mexico than addressing the specifics of the evidence before the Board in this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991778` offsets `24-32`; context: [87] If there is cogent evidence before the Board that government efforts are failing and that many normal citizens will not go near a police station, then I think great care is needed before the Court can accept the frequently used “mixed bag” rationale for not mentioning clear evidence that contradicts the Board’s conclusions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991779` offsets `112-120`; context: [88] I agree with the Respondent that, as a general principle, a Board is not obliged to mention every piece of evidence.
- Evidence: `counterargument_limitation` cue `However` at chunk `4991779` offsets `122-129`; context: However, the Board should not paper over compelling evidence that directly contradicts its own conclusions with phrases such as “the panel does not disagree,” or “based on the totality of the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4991780` offsets `94-102`; context: [89] Reading the Decision as a whole, it is my view that the Board does not engage with clear evidence that contradicts his own inclusions in the way that the jurisprudence of this Court says it should engage with that evidence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4991780` offsets `159-172`; context: [89] Reading the Decision as a whole, it is my view that the Board does not engage with clear evidence that contradicts his own inclusions in the way that the jurisprudence of this Court says it should engage with that evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4991780` offsets `395-402`; context: This becomes particularly problematic in a case where, as I have found, the Board also made a reviewable error by discounting the Principal Applicant’s own testimony because she was not a disinterested party.

#### Section text

[83] There was also clear evidence that the various Human Rights Commissions were “on the whole ineffective in holding authorities accountable for their actions and that many national and international human rights organizations question their competence.”

[84] There was also evidence that the preventive police are the most corrupt of the police organizations in Mexico.

[85] All in all, there was cogent evidence before the Board that the police in Mexico are corrupt and have extensive involvement with kidnapping gangs, that human rights commissions are ineffective, and that government initiatives to deal with the problem have largely failed. All of this is highly relevant to the issue of why the Principal Applicant did not go to the police.

[86] In other words, it was the usual “mixed bag,” but in this case the evidence that refuted the Board’s conclusions on this point was so cogent and so important to the Applicants’ case, that the Board’s failure to deal with it and to simply rely upon the usual presumptions of state protection looks more like defending a general position on Mexico than addressing the specifics of the evidence before the Board in this case.

[87] If there is cogent evidence before the Board that government efforts are failing and that many normal citizens will not go near a police station, then I think great care is needed before the Court can accept the frequently used “mixed bag” rationale for not mentioning clear evidence that contradicts the Board’s conclusions.

[88] I agree with the Respondent that, as a general principle, a Board is not obliged to mention every piece of evidence. However, the Board should not paper over compelling evidence that directly contradicts its own conclusions with phrases such as “the panel does not disagree,” or “based on the totality of the evidence.” The Board should engage with that evidence and say why it can be discounted or why other evidence is to be preferred.

[89] Reading the Decision as a whole, it is my view that the Board does not engage with clear evidence that contradicts his own inclusions in the way that the jurisprudence of this Court says it should engage with that evidence. This becomes particularly problematic in a case where, as I have found, the Board also made a reviewable error by discounting the Principal Applicant’s own testimony because she was not a disinterested party.

[90] This is a reviewable error and the matter needs to be reconsidered.


## 21053:6 · paragraphs 91-92

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `99b1d58ccc5c41a8475755dab308585cca00e632c0c9d5f941fb2c1ed00e29e1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21053:6:subtheme:1 · paragraphs 91-92

- Raw key terms: `judgment, reasons, russell, adjudges, allowed, amini, appearances, applicant`
- Display key terms: `russell, adjudges, allowed, amini`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: russell, adjudges, allowed, amini Operative outcome context: For the reasons given, the application for judicial review is allowed and the matter is returned for reconsideration by a different officer. Evidence spans paragraphs 91-92. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4991781` offsets `277-285`; context: There is no question for certification.
- Evidence: `disposition` cue `allowed` at chunk `4991781` offsets `183-190`; context: For the reasons given, the application for judicial review is allowed and the matter is returned for reconsideration by a different officer.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that
1. For the reasons given, the application for judicial review is allowed and the matter is returned for reconsideration by a different officer.
2. There is no question for certification.
“James Russell”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-5283-07
STYLE OF CAUSE: PATRICIA TORRES SANCHEZ, DIANA RAMOS TORRES, LAURA RAMOS TORRES, DANIELA RAMOS TORRES
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: October 8, 2008
REASONS FOR JUDGMENT
AND JUDGMENT: JUSTICE RUSSELL
DATED: December 1, 2008
APPEARANCES:
Mr. Ali M. Amini
FOR THE APPLICANT
Mr. Manuel Mendelzon
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Amini Carlson LLP
BARRISTER AND SOLICITOR
TORONTO, ONTARIO
FOR THE APPLICANT
JOHN H.SIMS, Q.C.
DEPUTY ATTORNEY GENERAL OF CANADA
TORONTO, ONTARIO
FOR THE RESPONDENT
