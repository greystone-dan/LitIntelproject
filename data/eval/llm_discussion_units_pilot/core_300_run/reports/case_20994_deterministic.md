# Discussion Units: case 20994

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **32**
- Continuity pairs: **31**
- Discussion Units: **2**
- Paragraph source hashes: **32**
- Sub-themes: **6**

## 20994:1 · paragraphs 0-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3a986aa35fd16794c10b71de4678bce38ed3bd27125f2a02739896895ac0e667`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20994:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `mexico, montemayor, protection, individual, associates, court, state, canada`
- Display key terms: `mexico, montemayor, protection, individual, associates, state`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: mexico, montemayor, protection, individual, associates, state Rule/authority context: The Standard of Review | Application of the Standard of Review to the RPD's Decision 1. Application context: [1] This application for judicial review is dismissed because the applicants have failed to establish that it was unreasonable for the Refugee Protection Division of the Immigration and Refugee Board (RPD) to conclude th | 190 the Court has found that deference remains appropriate where a finding of state protection is made and that the reasonableness standard ought to be applied. Operative outcome context: [1] This application for judicial review is dismissed because the applicants have failed to establish that it was unreasonable for the Refugee Protection Division of the Immigration and Refugee Board (RPD) to conclude th Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4989615` offsets `54-61`; context: [1] This application for judicial review is dismissed because the applicants have failed to establish that it was unreasonable for the Refugee Protection Division of the Immigration and Refugee Board (RPD) to conclude that adequate state protection exists for them in Mexico.
- Evidence: `disposition` cue `dismissed` at chunk `4989615` offsets `44-53`; context: [1] This application for judicial review is dismissed because the applicants have failed to establish that it was unreasonable for the Refugee Protection Division of the Immigration and Refugee Board (RPD) to conclude that adequate state protection exists for them in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989621` offsets `98-106`; context: Montemayor had failed to provide “clear and convincing” evidence of Mexico’s inability or unwillingness to extend protection, the RPD made a number of findings:
· First, the RPD found that the Public Ministry made efforts to resolve Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989622` offsets `42-50`; context: [8] The RPD also reviewed the documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989623` offsets `94-102`; context: The RPD misapprehended the evidence about the nature of protection provided to the applicants in Mexico, and erred by relying upon the serious efforts test without considering the effectiveness of the available protection.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4989623` offsets `644-662`; context: The Standard of Review
- Evidence: `evidence_fact` cue `found that` at chunk `4989624` offsets `331-341`; context: 190 the Court has found that deference remains appropriate where a finding of state protection is made and that the reasonableness standard ought to be applied.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4989624` offsets `717-735`; context: Application of the Standard of Review to the RPD's Decision
1.
- Evidence: `reasoning_application` cue `applied` at chunk `4989624` offsets `465-472`; context: 190 the Court has found that deference remains appropriate where a finding of state protection is made and that the reasonableness standard ought to be applied.

#### 20994:1:subtheme:2 · paragraphs 11-13

- Raw key terms: `efforts, made, protection, action, appeal, attorney, burden, canada`
- Display key terms: `efforts, made, protection, action, burden`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: efforts, made, protection, action, burden Position/evidence statements: In Hinzman, cited above, the Federal Court of Appeal made the following points: 41 In evaluating the appellants' claims, the starting point must be the direction from the Supreme Court of Canada that refugee protection i Rule/authority context: [11] I begin by briefly reviewing the principles that underlie the concept of state protection. | [12] Recently, the Federal Court of Appeal applied those principles to a review of a decision of the RPD that had concluded that adequate state protection existed in Mexico. Application context: [12] Recently, the Federal Court of Appeal applied those principles to a review of a decision of the RPD that had concluded that adequate state protection existed in Mexico. Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4989625` offsets `2202-2210`; context: elaborated on these principles and highlighted that the more democratic a country, the more the claimant must have done to seek out the protection of his or her home state:
When the state in question is a democratic state, as in the case at bar, the claimant must do more than simply show that he or she went to see some members of the police force and that his or her efforts were unsuccessful.
- Evidence: `party_position` cue `claims` at chunk `4989625` offsets `209-215`; context: In Hinzman, cited above, the Federal Court of Appeal made the following points:
41 In evaluating the appellants' claims, the starting point must be the direction from the Supreme Court of Canada that refugee protection is meant to be a form of surrogate protection to be invoked only in those situations where the refugee claimant has unsuccessfully sought the protections of his home state.
- Evidence: `governing_rule` cue `principles` at chunk `4989625` offsets `38-48`; context: [11] I begin by briefly reviewing the principles that underlie the concept of state protection.
- Evidence: `issue` cue `issue` at chunk `4989626` offsets `422-427`; context: It then reviewed the various steps taken by the authorities to address the issue: see the Board's reasons at pages 43 to 49 of the appeal book.
- Evidence: `evidence_fact` cue `found that` at chunk `4989626` offsets `1053-1063`; context: It found that Mexico is a fledgling democracy governed by the rule of law: ibidem, at pages 43-44.
- Evidence: `governing_rule` cue `principles` at chunk `4989626` offsets `57-67`; context: [12] Recently, the Federal Court of Appeal applied those principles to a review of a decision of the RPD that had concluded that adequate state protection existed in Mexico.
- Evidence: `reasoning_application` cue `applied` at chunk `4989626` offsets `43-50`; context: [12] Recently, the Federal Court of Appeal applied those principles to a review of a decision of the RPD that had concluded that adequate state protection existed in Mexico.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4989626` offsets `2470-2476`; context: 36 Considering the principles relating to the burden of proof, the standard of proof and the quality of the evidence needed to meet that standard defined as a balance of probabilities against the factual context, I cannot say that it is an error or unreasonable for the Board to have concluded that the respondent has failed to establish that the state protection is inadequate.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989627` offsets `104-112`; context: Did the RPD misapprehend the evidence about the nature of the protection provided to the applicants in Mexico, and err by relying upon the serious efforts test, without considering the effectiveness of the protection that was provided?

#### 20994:1:subtheme:3 · paragraphs 14-23

- Raw key terms: `protection, state, evidence, applicants, submissions, agencies, alleged, applicants'`
- Display key terms: `protection, state, submissions, agencies, alleged, applicants'`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: protection, state, submissions, agencies, alleged, applicants' Position/evidence statements: [14] The applicants argue that the RPD "misapprehends and exaggerates the evidence of what steps the state actually took" in their case and further erred by relying "on the serious efforts test without considering whethe | [17] The applicants essentially argue that the RPD relied upon the existence of state protection agencies that had no jurisdiction to protect the applicants and failed to appreciate that the agent of persecution was an i Application context: The individual was said to have "political influence" such that the applicants would get no police or state protection because of the individual's "political and financial power". | [23] For the following reasons, I find the RPD did not so err. Evidence spans paragraphs 14-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4989628` offsets `214-221`; context: [14] The applicants argue that the RPD "misapprehends and exaggerates the evidence of what steps the state actually took" in their case and further erred by relying "on the serious efforts test without considering whether the past protection was effective.
- Evidence: `party_position` cue `argue` at chunk `4989628` offsets `20-25`; context: [14] The applicants argue that the RPD "misapprehends and exaggerates the evidence of what steps the state actually took" in their case and further erred by relying "on the serious efforts test without considering whether the past protection was effective.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989628` offsets `74-82`; context: [14] The applicants argue that the RPD "misapprehends and exaggerates the evidence of what steps the state actually took" in their case and further erred by relying "on the serious efforts test without considering whether the past protection was effective.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989629` offsets `129-137`; context: Montemayor’s own evidence was that he filed a denunciation with the Public Ministry, the Public Ministry arranged for conciliation between the parties and, when that process proved unsuccessful, the dispute was referred to the court for determination.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989630` offsets `908-916`; context: Did the RPD ignore evidence concerning the agent of persecution and the mandates, relevance and effectiveness of specific state protection agencies?
- Evidence: `party_position` cue `argue` at chunk `4989631` offsets `32-37`; context: [17] The applicants essentially argue that the RPD relied upon the existence of state protection agencies that had no jurisdiction to protect the applicants and failed to appreciate that the agent of persecution was an individual.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989631` offsets `393-401`; context: Further, the applicants argue that the RPD failed to consider the effectiveness of the protection provided by failing to grapple with the conflicting documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4989634` offsets `58-66`; context: [20] Second, the applicants' submissions ignore their own evidence about the nature of the power and influence exercised by the individual.
- Evidence: `reasoning_application` cue `because` at chunk `4989634` offsets `259-266`; context: The individual was said to have "political influence" such that the applicants would get no police or state protection because of the individual's "political and financial power".
- Evidence: `evidence_fact` cue `evidence` at chunk `4989636` offsets `51-59`; context: [22] Finally, the RPD acknowledged the documentary evidence and submissions before it which were to the effect that "crime and corruption continue to be problems is in Mexico".
- Evidence: `counterargument_limitation` cue `However` at chunk `4989636` offsets `177-184`; context: However, the RPD found that "[b]ased on the totality of the evidence adduced, the panel finds that adequate, though not necessarily perfect" state protection was available to the applicants in Mexico.
- Evidence: `reasoning_application` cue `I find` at chunk `4989637` offsets `32-38`; context: [23] For the following reasons, I find the RPD did not so err.

#### 20994:1:subtheme:4 · paragraphs 24-27

- Raw key terms: `case, against, applicants, canada, claimant, initial, noted, paragraph`
- Display key terms: `case, against, initial, noted, paragraph`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: case, against, initial, noted, paragraph Application context: Montemayor testified that the individual did ultimately comply with a notice to appear that was served upon him because "if he had not appeared after having received the third Notice to Appear, then the police would have | But where, as in this case, the state was bringing proceedings against the agent of persecution, it was reasonable for the RPD to conclude that the making of the initial complaint was insufficient to rebut the presumptio Operative outcome context: [27] For these reasons, the application for judicial review will be dismissed. Evidence spans paragraphs 24-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4989638` offsets `745-750`; context: He further testified that the threats and violence that occurred in 2006 happened:
CLAIMANT: Because [the individual] knew that if the case was referred from the Public Ministry to the Courts, the Courts will have to issue an apprehension order against him.
- Evidence: `reasoning_application` cue `because` at chunk `4989638` offsets `407-414`; context: Montemayor testified that the individual did ultimately comply with a notice to appear that was served upon him because "if he had not appeared after having received the third Notice to Appear, then the police would have taken him".
- Evidence: `reasoning_application` cue `conclude` at chunk `4989639` offsets `866-874`; context: But where, as in this case, the state was bringing proceedings against the agent of persecution, it was reasonable for the RPD to conclude that the making of the initial complaint was insufficient to rebut the presumption of state protection.
- Evidence: `disposition` cue `dismissed` at chunk `4989641` offsets `68-77`; context: [27] For these reasons, the application for judicial review will be dismissed.

#### 20994:1:subtheme:5 · paragraphs 28-29

- Raw key terms: `question, applicants, application, approach, believe, carillo, certification, certified`
- Display key terms: `question, approach, believe, carillo, certification, certified`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: question, approach, believe, carillo, certification, certified Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4989642` offsets `52-60`; context: [28] Counsel for the applicants posed the following question for certification: "Does the Carillo decision require claimants to make determined efforts to approach the state, even if they believe the approach would invite persecution?
- Evidence: `issue` cue `question` at chunk `4989643` offsets `63-71`; context: [29] In my view, the law on this point is well-settled and the question would not be determinative of this application.

#### Section text

Montemayor Romero v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-08-28
Neutral citation
2008 FC 977
File numbers
IMM-1146-08
Decision Content
Date: 20080828
Docket: IMM-1146-08
Citation: 2008 FC 977
Ottawa, Ontario, August 28, 2008
PRESENT: The Honourable Madam Justice Dawson
BETWEEN:
SANTIAGO COSME MONTEMAYOR ROMERO
MARIA SUSANA DE LA ROSA GOMEZ
MOISES MONTEMAYOR DE LA ROSA
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This application for judicial review is dismissed because the applicants have failed to establish that it was unreasonable for the Refugee Protection Division of the Immigration and Refugee Board (RPD) to conclude that adequate state protection exists for them in Mexico.
Background Facts

[2] Santiago Cosme Montemayor Romero, his wife, Maria Susana De La Rosa Gomez, and their son, Moises Montemayor De La Rosa, are citizens of Mexico. Mr. Montemayor and his family seek protection from an individual (the individual) who is said to be a powerful businessman with influence in the ruling National Action Party. Mr. Montemayor says that the individual and his associates threatened him and his family.

[3] On November 28, 2003, Mr. Montemayor filed a denunciation against the individual with the Public Ministry of the Attorney General of Justice of Mexico State (Public Ministry), citing fraud and threats committed by the individual.

[4] Mr. Montemayor continued to receive threats from the individual and his associates.

[5] The denunciation filed with the Public Ministry led to an unsuccessful conciliation process and, ultimately, the dispute was to be referred to the Court.

[6] Mr. Montemayor says that, after his complaint was to be referred to the Court, the threats from the individual and his associates increased. On February 19, 2006, an unsuccessful attempt was made to break into Mr. Montemayor’s house. The would-be intruders left behind a threatening note. On March 3, 2006, Mr. Montemayor’s house was stoned and he received a threatening telephone call. On March 6, 2006, another threatening phone call was received, telling Mr. Montemayor that “they” knew the daily patterns of his wife and son. Mr. Montemayor and his family immediately left their home to stay with friends. Shortly thereafter, they left Mexico for Canada and made their claim for protection.
The Decision of the RPD

[7] In support of its conclusion that Mr. Montemayor had failed to provide “clear and convincing” evidence of Mexico’s inability or unwillingness to extend protection, the RPD made a number of findings:
· First, the RPD found that the Public Ministry made efforts to resolve Mr. Montemayor’s complaint. The RPD noted that the parties proceeded to a conciliation process and, when that process failed, the matter was referred to the Court for determination.
· Second, the RPD found that, after receiving threats from the individual and his associates, Mr. Montemayor made no attempt to seek protection from police or any other state authority.
· Third, the RPD found that Mr. Montemayor elected to leave Mexico and seek protection in Canada before his dispute with the individual was determined by the Court.
· Fourth, the RPD found that it was reasonable to expect Mr. Montemayor to seek protection from state agencies in Mexico, including the Human Rights Commission (Commission), the Federal Agency of Investigations and the Secretariat of Public Services, before seeking international protection.

[8] The RPD also reviewed the documentary evidence. The RPD made the following observations:
· While the RPD acknowledged that there continued to be problems in Mexico regarding crime, it was not persuaded that Mr. Montemayor would not receive protection from the individual and his associates.
· The RPD also acknowledged that corruption was an ongoing problem in Mexico, but noted that the documentary evidence indicated that Mexico was aggressively targeting corruption and bribery.
· Based on the whole of the evidence, the RPD concluded that adequate, though not necessarily perfect, protection would be available to Mr. Montemayor and his family in Mexico.
The Asserted Errors

[9] Three errors are asserted by the applicants. They are that:
1. The RPD misapprehended the evidence about the nature of protection provided to the applicants in Mexico, and erred by relying upon the serious efforts test without considering the effectiveness of the available protection.
2. The RPD ignored evidence concerning the agent of persecution and the mandates, relevance and effectiveness of specific state protection agencies.
3. The RPD erred by requiring the applicants to exhaust all avenues of protection, to approach the state again after they did not initially receive protection and to approach human rights commissions.
The Standard of Review

[10] A finding as to the adequacy of state protection has been held to be reviewable against the reasonableness simpliciter standard. See: Hinzman v. Canada (Minister of Citizenship and Immigration) (2007), 362 N.R. 1 at paragraph 38 (F.C.A.). Following the decision in Dunsmuir v. New Brunswick, [2008] 1 S.C.R. 190 the Court has found that deference remains appropriate where a finding of state protection is made and that the reasonableness standard ought to be applied. See, for example, Eler v. Canada (Minister of Citizenship and Immigration), [2008] F.C.J. No. 418 at paragraphs 6 to 7 and Cervantes v. Canada (Minister of Citizenship and Immigration), [2008] F.C.J. No. 848 at paragraph 7.
Application of the Standard of Review to the RPD's Decision
1. General Principles

[11] I begin by briefly reviewing the principles that underlie the concept of state protection. In Hinzman, cited above, the Federal Court of Appeal made the following points:
41 In evaluating the appellants' claims, the starting point must be the direction from the Supreme Court of Canada that refugee protection is meant to be a form of surrogate protection to be invoked only in those situations where the refugee claimant has unsuccessfully sought the protections of his home state. In Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689 at page 709 ("Ward"), La Forest J., speaking for the Court, explained this concept as follows:
At the outset, it is useful to explore the rationale underlying the international refugee protection regime, for this permeates the interpretation of the various terms requiring examination. International refugee law was formulated to serve as a back-up to the protection one expects from the state of which an individual is a national. It was meant to come into play only in situations when that protection is unavailable, and then only in certain situations. The international community intended that persecuted individuals be required to approach their home state for protection before the responsibility of other states becomes engaged. [Emphasis added in original.]
[…]
43 In Ward, the Supreme Court explained at page 725 that in refugee law, there is a presumption of state protection:
...nations should be presumed capable of protecting their citizens. Security of nationals is, after all, the essence of sovereignty. Absent a situation of complete breakdown of state apparatus, such as that recognized in Lebanon in Zalzali, it should be assumed that the state is capable of protecting a claimant.
44 To rebut the presumption, the Court stated that "clear and convincing confirmation of a state's inability to protect must be provided": Ward at page 724.
45 In Kadenko v. Canada (Solicitor General) (1996), 143 D.L.R. (4th) 532 at page 534 (F.C.A.), Décary J.A. elaborated on these principles and highlighted that the more democratic a country, the more the claimant must have done to seek out the protection of his or her home state:
When the state in question is a democratic state, as in the case at bar, the claimant must do more than simply show that he or she went to see some members of the police force and that his or her efforts were unsuccessful. The burden of proof that rests on the claimant is, in a way, directly proportional to the level of democracy in the state in question: the more democratic the state's institutions, the more the claimant must have done to exhaust all the courses of action open to him or her. [Emphasis added in original.]

[12] Recently, the Federal Court of Appeal applied those principles to a review of a decision of the RPD that had concluded that adequate state protection existed in Mexico. In Carillo v. Canada (Minister of Citizenship and Immigration), [2008] F.C.J. No. 399 the Court wrote:
31 The Board acknowledged the prevalence of domestic abuse in Mexico. It then reviewed the various steps taken by the authorities to address the issue: see the Board's reasons at pages 43 to 49 of the appeal book.
32 It proceeded to review the law governing the presumption of state protection. It stated that local failures to provide effective policing do not amount to a lack of state protection. Relying upon the findings of this Court in Kadenko v. Canada (Solicitor General) (1996), 143 D.L.R. (4th) 532, leave to appeal to the Supreme Court of Canada, [1996] S.C.C.A. No. 612, refused on May 8, 1997, it stated that "the more democratic the state's institutions, the more the claimant must have done to exhaust all the courses of action open to him or her": ibidem. It found that Mexico is a fledgling democracy governed by the rule of law: ibidem, at pages 43-44.
33 The Board found that the respondent had failed to make determined efforts to seek protection. She reported to police only once during more than four years of alleged abuse: ibidem, at page 45.
34 In addition, the Board concluded based on the evidence before it that the respondent did not make additional effort to seek protection from the authorities when the local police officers allegedly did not provide the protection she was seeking: ibidem. She could have sought redress through National or State Human Rights Commissions, the Secretariat of Public Administration, the Program Against Impunity, the General Comptroller's Assistance Directorate and the complaints procedure at the office of the Federal Attorney General: ibidem, at page 49.
35 Finally, the Board noted the respondent's omission to make a complaint about the involvement of the abuser's brother, who allegedly is a federal judicial police officer, when the evidence indicates that substantial, meaningful and often successful efforts have been made at the federal level to combat crime and corruption: ibidem, at pages 46 and 49.
36 Considering the principles relating to the burden of proof, the standard of proof and the quality of the evidence needed to meet that standard defined as a balance of probabilities against the factual context, I cannot say that it is an error or unreasonable for the Board to have concluded that the respondent has failed to establish that the state protection is inadequate.

[13] I now turn to the submissions made by the applicants in this case.
2. Did the RPD misapprehend the evidence about the nature of the protection provided to the applicants in Mexico, and err by relying upon the serious efforts test, without considering the effectiveness of the protection that was provided?

[14] The applicants argue that the RPD "misapprehends and exaggerates the evidence of what steps the state actually took" in their case and further erred by relying "on the serious efforts test without considering whether the past protection was effective."

[15] In my view, the RPD neither misapprehended nor exaggerated the steps taken by the Mexican authorities. Mr. Montemayor’s own evidence was that he filed a denunciation with the Public Ministry, the Public Ministry arranged for conciliation between the parties and, when that process proved unsuccessful, the dispute was referred to the court for determination. As the RPD noted, the process, though perhaps delayed, was in progress at the time that Mr. Montemayor and his family left for Canada. While perhaps more could have been done more quickly, no state is required to guarantee the perfect protection of its citizens at all times. See: Canada (Minister of Employment and Immigration) v. Villafranca (1992), 150 N.R. 232 (F.C.A.).

[16] In my further view, contrary to the applicants' submissions, the RPD did not fail to consider the effectiveness of Mexico's efforts to provide protection. For example:
· At page 6 of its reasons, after the RPD referred to efforts to reform the federal police, the RPD considered the steps taken operationally to enforce the internal regulations of the Federal Preventive Police;
· at page 7 of its reasons, after referring to the intent of the Fox administration to target corruption, the RPD referred to steps taken to give effect to that intent. Those steps included investigations, the imposition of sanctions, improved pay and benefits for officials liable to be corrupted, and improved hiring practices; and
· at page 8 of its reasons, after referring to the enactment of laws to eliminate corruption and bribery, the RPD reviewed the steps taken to enforce that legislation.
3. Did the RPD ignore evidence concerning the agent of persecution and the mandates, relevance and effectiveness of specific state protection agencies?

[17] The applicants essentially argue that the RPD relied upon the existence of state protection agencies that had no jurisdiction to protect the applicants and failed to appreciate that the agent of persecution was an individual. Further, the applicants argue that the RPD failed to consider the effectiveness of the protection provided by failing to grapple with the conflicting documentary evidence.

[18] Again, I respectfully disagree. In my view, the RPD did not err as alleged. I reach this conclusion for the following reasons.

[19] First, the applicants' submissions do not challenge the fact that one of the RPD's findings was that the applicants had failed to seek protection by lodging any complaint with the police about the threats and vandalism. Without doubt, the police were a relevant state protection agency.

[20] Second, the applicants' submissions ignore their own evidence about the nature of the power and influence exercised by the individual. The individual was said to have "political influence" such that the applicants would get no police or state protection because of the individual's "political and financial power". Given the alleged nature of the individual’s influence and the nature of the alleged corruption, it was reasonable for the RPD to point to state agencies such as the Federal Agency of Investigations, the Secretariat of Public Services, the Commission, and the Telephone Assistance System for Citizens. On this point, the RPD noted that the Federal Agency of Investigations dealt with "corrupt state officials," the Secretariat of Public Services dealt with "complaints regarding misconduct and corruption," the Commission dealt with "police misconduct," and the Telephone Assistance System for Citizens received "complaints regarding misconduct of public servants."

[21] Third, by recognizing the nature of the influence the individual was said to possess, the RPD recognized that the alleged persecutor was an individual.

[22] Finally, the RPD acknowledged the documentary evidence and submissions before it which were to the effect that "crime and corruption continue to be problems is in Mexico". However, the RPD found that "[b]ased on the totality of the evidence adduced, the panel finds that adequate, though not necessarily perfect" state protection was available to the applicants in Mexico. There was documentary evidence to support the RPD's conclusion and its conclusion was reasonably supported by the documentary evidence.
4. Did the RPD err by requiring the applicants to exhaust all avenues of protection, to approach the state again after they did not initially receive protection and to approach human rights commissions?

[23] For the following reasons, I find the RPD did not so err.

[24] First, it was reasonable for the RPD to find that the filing of a denunciation and subsequent departure from Mexico while that process was continuing did not constitute clear and convincing proof of Mexico's inability to protect the applicants. As to the effectiveness of that process, Mr. Montemayor testified that the individual did ultimately comply with a notice to appear that was served upon him because "if he had not appeared after having received the third Notice to Appear, then the police would have taken him". He further testified that the threats and violence that occurred in 2006 happened:
CLAIMANT: Because [the individual] knew that if the case was referred from the Public Ministry to the Courts, the Courts will have to issue an apprehension order against him.
MEMBER: Sorry, what would they do?
CLAIMANT: That because he knew that if the case was referred from the Public Ministry to the Courts the Courts would have to issue an apprehension order against him.

[25] Second, in Carillo, cited above, the Federal Court of Appeal approved findings of the RPD, made in somewhat analogous circumstances, that where an initial effort to seek state protection was unsuccessful, the claimant was obliged to make "determined efforts to seek protection" and an "additional effort" may well be required (see paragraphs 33 and 34 of the decision). This is not to say that in every case repeated or determined efforts must be made to access state protection. Such a result would be contrary to the teaching of the Supreme Court of Canada in Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689 that a refugee claimant is only obliged to seek protection where such protection might be reasonably forthcoming. But where, as in this case, the state was bringing proceedings against the agent of persecution, it was reasonable for the RPD to conclude that the making of the initial complaint was insufficient to rebut the presumption of state protection. As the Court of Appeal noted in Hinzman, at paragraph 57, "a claimant coming from a democratic country will have a heavy burden when attempting to show that he should not have been required to exhaust all of the recourses available to him domestically before claiming refugee status."

[26] Finally, with respect to the relevance of the Commission, I adopt the comments of my colleague Justice Barnes in Sanchez v. Canada (Minister of Citizenship and Immigration), [2008] F.C.J. No. 182. At paragraph 10 he wrote:
10 I also do not accept that the Board erred by referring to agencies which may not have a direct responsibility for the provision of protective assistance, such as the Mexican Human Rights Commission. State agencies which are outside of the criminal justice system, and even a person's employer, can play a helpful role in cases like this where the initial local police response may not be adequate. In this case there were a number of alternate agencies noted by the Board which could have been approached and it is surprising that the Applicants chose not to do so in the face of the events they described.
Conclusion

[27] For these reasons, the application for judicial review will be dismissed.

[28] Counsel for the applicants posed the following question for certification: "Does the Carillo decision require claimants to make determined efforts to approach the state, even if they believe the approach would invite persecution?" Counsel for the Minister opposed certification of the question.

[29] In my view, the law on this point is well-settled and the question would not be determinative of this application. No question will be certified.


## 20994:2 · paragraphs 30-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e6f4bca7ae9381e5d2a82bdf1d5dbf0e5b8c6ff0fa79a87f33bb722dc0b8c02e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 20994:2:subtheme:1 · paragraphs 30-31

- Raw key terms: `dawson, judgment, adjudges, appearances, applicants, application, associates, attorney`
- Display key terms: `dawson, adjudges, associates`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: dawson, adjudges, associates Operative outcome context: The application for judicial review is dismissed. Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4989643` offsets `239-248`; context: The application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
1. The application for judicial review is dismissed.
“Eleanor R. Dawson”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-1146-08
STYLE OF CAUSE: SANTIAGO COSME MONTEMAYOR ROMERO ET AL., Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION, Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: AUGUST 13, 2008
REASONS FOR JUDGMENT
AND JUDGMENT: DAWSON, J.
DATED: AUGUST 28, 2008
APPEARANCES:
MS. LEIGH SALSBERG FOR THE APPLICANTS
MS. LAOURA CHRISTODOULIDES FOR THE RESPONDENT
SOLICITORS OF RECORD:
JACKMAN & ASSOCIATES FOR THE APPLICANTS
TORONTO, ONTARIO
JOHN H. SIMS, Q.C. FOR THE RESPONDENT
DEPUTY ATTORNEY GENERAL OF CANADA
