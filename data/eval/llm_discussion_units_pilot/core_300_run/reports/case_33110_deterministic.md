# Discussion Units: case 33110

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **24**
- Continuity pairs: **23**
- Discussion Units: **3**
- Paragraph source hashes: **24**
- Sub-themes: **6**

## 33110:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f4b215e237135ab367ee53d006f6edef7223bdb7e8c0dafcb5436f3c90a5204e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33110:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, canada, immigration, best, citizenship, decision, interests, minister`
- Display key terms: `best, interests`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: best, interests Position/evidence statements: The Applicant submitted that the best interests of his grandchildren would be negatively impacted by his removal because he is the only father figure in his grandchildren’s life and he provides significant support to the | [7] The Applicant argues that the Decision was unreasonable because the Officer’s analysis of the best interests of the Applicant’s grandchildren was deficient. Rule/authority context: The primary H&C consideration raised in the application is the best interests of the Applicant’s grandchildren, all of who are under the age of 10, and the harm that they will suffer if their grandfather is forced to lea | 817 (QL) (Baker) recognized that this section conveys a broad discretion on a visa officer; however, it held that an officer must exercise this discretion reasonably, paying particular attention to the best interests of  Application context: [1] In the present Application, a grandfather of four Canadian born children (the Applicant), who applied to remain in Canada as a permanent resident on Humanitarian and Compassionate (H&C) grounds, challenges the Decisi | The Applicant submitted that the best interests of his grandchildren would be negatively impacted by his removal because he is the only father figure in his grandchildren’s life and he provides significant support to the Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5536865` offsets `98-105`; context: [1] In the present Application, a grandfather of four Canadian born children (the Applicant), who applied to remain in Canada as a permanent resident on Humanitarian and Compassionate (H&C) grounds, challenges the Decision of a Visa Officer (Officer) who found there are insufficient H&C considerations to warrant approval of his request.
- Evidence: `party_position` cue `submitted` at chunk `5536867` offsets `393-402`; context: The Applicant submitted that the best interests of his grandchildren would be negatively impacted by his removal because he is the only father figure in his grandchildren’s life and he provides significant support to them and their single-parent 26-year-old mother.
- Evidence: `governing_rule` cue `under` at chunk `5536867` offsets `275-280`; context: The primary H&C consideration raised in the application is the best interests of the Applicant’s grandchildren, all of who are under the age of 10, and the harm that they will suffer if their grandfather is forced to leave Canada.
- Evidence: `reasoning_application` cue `because` at chunk `5536867` offsets `492-499`; context: The Applicant submitted that the best interests of his grandchildren would be negatively impacted by his removal because he is the only father figure in his grandchildren’s life and he provides significant support to them and their single-parent 26-year-old mother.
- Evidence: `governing_rule` cue `standard of review` at chunk `5536869` offsets `377-395`; context: 817 (QL) (Baker) recognized that this section conveys a broad discretion on a visa officer; however, it held that an officer must exercise this discretion reasonably, paying particular attention to the best interests of the child and that, therefore, the appropriate standard of review of an H&C decision is reasonable simpliciter.
- Evidence: `reasoning_application` cue `therefore` at chunk `5536869` offsets `350-359`; context: 817 (QL) (Baker) recognized that this section conveys a broad discretion on a visa officer; however, it held that an officer must exercise this discretion reasonably, paying particular attention to the best interests of the child and that, therefore, the appropriate standard of review of an H&C decision is reasonable simpliciter.
- Evidence: `counterargument_limitation` cue `however` at chunk `5536869` offsets `202-209`; context: 817 (QL) (Baker) recognized that this section conveys a broad discretion on a visa officer; however, it held that an officer must exercise this discretion reasonably, paying particular attention to the best interests of the child and that, therefore, the appropriate standard of review of an H&C decision is reasonable simpliciter.
- Evidence: `party_position` cue `argues` at chunk `5536871` offsets `18-24`; context: [7] The Applicant argues that the Decision was unreasonable because the Officer’s analysis of the best interests of the Applicant’s grandchildren was deficient.
- Evidence: `evidence_fact` cue `evidence` at chunk `5536871` offsets `271-279`; context: In addition, the Applicant argues that the Officer breached due process by relying on two extrinsic pieces of evidence which were never put to the Applicant.
- Evidence: `reasoning_application` cue `because` at chunk `5536871` offsets `60-67`; context: [7] The Applicant argues that the Decision was unreasonable because the Officer’s analysis of the best interests of the Applicant’s grandchildren was deficient.

#### 33110:1:subtheme:2 · paragraphs 8-11

- Raw key terms: `best, child, demonstrate, interests, affected, alive, canada, children`
- Display key terms: `best, child, demonstrate, interests, affected, alive, children`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: best, child, demonstrate, interests, affected, alive, children Rule/authority context: 75 states that an H&C decision will be unreasonable if the decision-maker does not adequately consider the best interests of the children affected by the decision: The principles discussed above indicate that, for the ex | Best interests of the child The Immigration and Refugee Protection Act introduces a statutory obligation to take into account the best interests of a child who is directly affected by a decision under A25(1), when examin Application context: Therefore, in order to assess whether the Officer was “alert, alive and sensitive”, the content of this requirement must be addressed. Evidence spans paragraphs 8-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5536872` offsets `939-946`; context: Therefore, in order to assess whether the Officer was “alert, alive and sensitive”, the content of this requirement must be addressed.
- Evidence: `governing_rule` cue `principles` at chunk `5536872` offsets `187-197`; context: 75 states that an H&C decision will be unreasonable if the decision-maker does not adequately consider the best interests of the children affected by the decision:
The principles discussed above indicate that, for the exercise of the discretion to fall within the standard of reasonableness, the decision-maker should consider children's best interests as an important factor, give them substantial weight, and be alert, alive and sensitive to them.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5536872` offsets `909-918`; context: Therefore, in order to assess whether the Officer was “alert, alive and sensitive”, the content of this requirement must be addressed.
- Evidence: `counterargument_limitation` cue `although` at chunk `5536872` offsets `514-522`; context: [Emphasis added]
This quote emphasizes that, although a child’s best interests should be given substantial weight, it will not necessarily be the determining factor in every case, (Legault v.
- Evidence: `issue` cue `issues` at chunk `5536873` offsets `1644-1650`; context: Some examples of factors that applicants may raise include:
• the age of the child;
• the level of dependency between the child and the H&C applicant;
• the degree of the child’s establishment in Canada;
• the child’s links to the country in relation to which the H&C decision is being considered;
• medical issues or special needs the child may have;
• the impact to the child’s education;
• matters related to the child’s gender.
- Evidence: `governing_rule` cue `under` at chunk `5536873` offsets `676-681`; context: Best interests of the child
The Immigration and Refugee Protection Act introduces a statutory obligation to take into account the best interests of a child who is directly affected by a decision under A25(1), when examining
the circumstances of a foreign national under this section.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5536873` offsets `268-276`; context: Although the best interests of the child is a fact specific analysis, the Guidelines at s.

#### 33110:1:subtheme:3 · paragraphs 12-18

- Raw key terms: `decision, officer, applicant, child, diabetes, association, best, canadian`
- Display key terms: `officer, child, diabetes, association, best, canadian`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: officer, child, diabetes, association, best, canadian Position/evidence statements: [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to resp Application context: [15] As a result, I find that the decision is unreasonable. | [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to resp Evidence spans paragraphs 12-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5536876` offsets `376-383`; context: To demonstrate sensitivity, the officer must be able to clearly articulate the suffering of a child that will result from a negative decision, and then say whether, together with a consideration of other factors, the suffering warrants humanitarian and compassionate relief.
- Evidence: `evidence_fact` cue `Record` at chunk `5536877` offsets `1807-1813`; context: [Emphasis added]
(Decision, Tribunal Record, p.
- Evidence: `counterargument_limitation` cue `However` at chunk `5536877` offsets `690-697`; context: However, family separation is within the normal consequences of the removal of someone who has no recognized status to remain in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5536878` offsets `480-488`; context: The evidence on the record with respect to Alexsey’s health, which was apparently neglected by the Officer, is as follows:
My greatest concern is for a Russian man from Latvia by the name of Alexei Kolosovs.
- Evidence: `reasoning_application` cue `I find` at chunk `5536879` offsets `18-24`; context: [15] As a result, I find that the decision is unreasonable.
- Evidence: `party_position` cue `argues` at chunk `5536880` offsets `19-25`; context: [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to respond.
- Evidence: `evidence_fact` cue `evidence` at chunk `5536880` offsets `128-136`; context: [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to respond.
- Evidence: `reasoning_application` cue `because` at chunk `5536880` offsets `82-89`; context: [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to respond.
- Evidence: `counterargument_limitation` cue `but` at chunk `5536880` offsets `138-141`; context: [16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to respond.

#### 33110:1:subtheme:4 · paragraphs 19-20

- Raw key terms: `find, according, acknowledge, additionally, allow, amounts, applicant, assessment`
- Display key terms: `find, according, acknowledge, additionally, allow, amounts, assessment`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: find, according, acknowledge, additionally, allow, amounts, assessment Application context: [19] The Applicant’s H&C submissions indicate he would have difficult obtaining employment in Latvia because he does not speak Latvian and the language laws require competency in Latvian. | [20] As a result, I find that the Decision was rendered in breach of due process. Operative outcome context: I could find nothing in my research that would allow me to conclude that they are denied employment as a general rule”. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5536883` offsets `859-866`; context: It is not clear whether the Applicant knew of the opinion expressed some four years before, but, in any event, he had no notice that it would be used to his detriment in the present H&C proceeding.
- Evidence: `evidence_fact` cue `evidence` at chunk `5536883` offsets `1061-1069`; context: Indeed, there is no evidence concerning the reliability of the source the PRRA officer used, or whether the language laws in Latvia had changed in the intervening years.
- Evidence: `reasoning_application` cue `because` at chunk `5536883` offsets `101-108`; context: [19] The Applicant’s H&C submissions indicate he would have difficult obtaining employment in Latvia because he does not speak Latvian and the language laws require competency in Latvian.
- Evidence: `disposition` cue `denied` at chunk `5536883` offsets `805-811`; context: I could find nothing in my research that would allow me to conclude that they are denied employment as a general rule”.
- Evidence: `reasoning_application` cue `I find` at chunk `5536884` offsets `18-24`; context: [20] As a result, I find that the Decision was rendered in breach of due process.

#### Section text

Kolosovs v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-02-07
Neutral citation
2008 FC 165
File numbers
IMM-873-07
Notes
Digest
Decision Content
Date: 20080207
Docket: IMM-873-07
Citation: 2008 FC 165
Toronto, Ontario, February 7, 2008
PRESENT: The Honourable Mr. Justice Campbell
BETWEEN:
ALEKSEJS VITALY KOLOSOVS
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] In the present Application, a grandfather of four Canadian born children (the Applicant), who applied to remain in Canada as a permanent resident on Humanitarian and Compassionate (H&C) grounds, challenges the Decision of a Visa Officer (Officer) who found there are insufficient H&C considerations to warrant approval of his request.

[2] Originally born in Russia, the Applicant worked in Latvia for some years aboard a fish boat which entered St. John’s harbour in 1997, and as a result of the owners of the vessel declaring bankruptcy while in that port, he left the ship and entered the Canadian immigration system. Since his arrival, the Applicant has, at times, held valid work permits, and when he had these permits he was hired by Newfoundland employers who have expressed a need for his net-making expertise. The Applicant made several applications to remain in Canada, all of which were unsuccessful. On his scheduled deportation date in April of 2005, the Applicant went into “sanctuary” at West End Baptist Church, St. John’s, Newfoundland, where he is currently living.

[3] The Applicant’s H&C application consists of written submissions by the Applicant and supporting documentation, including 26 letters of support. The primary H&C consideration raised in the application is the best interests of the Applicant’s grandchildren, all of who are under the age of 10, and the harm that they will suffer if their grandfather is forced to leave Canada. The Applicant submitted that the best interests of his grandchildren would be negatively impacted by his removal because he is the only father figure in his grandchildren’s life and he provides significant support to them and their single-parent 26-year-old mother. Several of the letters of support, written by the Applicant’s daughter-in-law, the Applicant’s potential employers, and other members of the community, note that this support is especially important since one of the grandchildren, three-year-old Alexsey, requires extra care because he suffers from diabetes. In addition to the children’s best interests, the H&C application details that the Applicant: has no citizenship; would have difficulty obtaining a job if he were returned to Latvia as he has not been there in many years and does not speak Latvian; has two job offers in Canada where his skills are in demand; and is a well regarded member of the community in which he lives.

[4] The Officer’s legal basis for assessing the Applicant’s H&C submission is found in s.25(1) of the Immigration and Refugee Protection Act S.C. 2001, c. 27, which specifically notes that the best interests of children should be considered:
25. (1) The Minister shall, upon request of a foreign national who is inadmissible or who does not meet the requirements of this Act, and may, on the Minister’s own initiative, examine the circumstances concerning the foreign national and may grant the foreign national permanent resident status or an exemption from any applicable criteria or obligation of this Act if the Minister is of the opinion that it is justified by humanitarian and compassionate considerations relating to them, taking into account the best interestss of a child directly affected, or by public policy considerations.
25. (1) Le ministre doit, sur demande d’un étranger interdit de territoire ou qui ne se conforme pas à la présente loi, et peut, de sa propre initiative, étudier le cas de cet étranger et peut lui octroyer le statut de résident permanent ou lever tout ou partie des critères et obligations applicables, s’il estime que des circonstances d’ordre humanitaire relatives à l’étranger — compte tenu de l’intérêt supérieur de l’enfant directement touché — ou l’intérêt public le justifient.
[Emphasis added]

[5] The Supreme Court of Canada in Baker v. Canada (Minister of Citizenship and Immigration), [1999] 2 S.C.R. 817 (QL) (Baker) recognized that this section conveys a broad discretion on a visa officer; however, it held that an officer must exercise this discretion reasonably, paying particular attention to the best interests of the child and that, therefore, the appropriate standard of review of an H&C decision is reasonable simpliciter.

[6] Baker at para. 73 also recognizes that the guidelines promulgated by the Minister of Citizenship and Immigration to aid visa officers in making H&C decisions, IP 5 Immigrant Applications in Canada made on Humanitarian or Compassionate Grounds (Guidelines), can be a “useful indicator of what constitutes a reasonable interpretation of the power conferred by the section”.

[7] The Applicant argues that the Decision was unreasonable because the Officer’s analysis of the best interests of the Applicant’s grandchildren was deficient. In addition, the Applicant argues that the Officer breached due process by relying on two extrinsic pieces of evidence which were never put to the Applicant. I agree with both of these arguments.
I. Requirements for Determining the Best Interests of the Child

[8] Baker at para. 75 states that an H&C decision will be unreasonable if the decision-maker does not adequately consider the best interests of the children affected by the decision:
The principles discussed above indicate that, for the exercise of the discretion to fall within the standard of reasonableness, the decision-maker should consider children's best interests as an important factor, give them substantial weight, and be alert, alive and sensitive to them.
[Emphasis added]
This quote emphasizes that, although a child’s best interests should be given substantial weight, it will not necessarily be the determining factor in every case, (Legault v. Canada (Minister of Citizenship and Immigration), [2002] 4 F.C. 358 (C.A)). To come to a reasonable decision, a decision-maker must demonstrate that he or she is alert, alive and sensitive to the best interests of the children under consideration. Therefore, in order to assess whether the Officer was “alert, alive and sensitive”, the content of this requirement must be addressed.
A. Alert

[9] The word alert implies awareness. When an H&C application indicates that a child that will be directly affected by the decision, a visa officer must demonstrate an awareness of the child’s best interests by noting the ways in which those interests are implicated. Although the best interests of the child is a fact specific analysis, the Guidelines at s. 5.19, provide a starting point for a visa officer by setting out some factors that often arise in H&C applications:
5.19. Best interests of the child
The Immigration and Refugee Protection Act introduces a statutory obligation to take into account the best interests of a child who is directly affected by a decision under A25(1), when examining
the circumstances of a foreign national under this section. This codifies departmental practice into legislation, thus eliminating any doubt that the interests of a child will be taken into account.
Officers must always be alert and sensitive to the interests of children when examining A25(1) requests. However, this obligation only arises when it is sufficiently clear from the material submitted to the decision-maker that an application relies, in whole or at least in part, on this factor.
….
Generally, factors relating to a child’s emotional, social, cultural and physical welfare should be taken into account, when raised. Some examples of factors that applicants may raise include:
• the age of the child;
• the level of dependency between the child and the H&C applicant;
• the degree of the child’s establishment in Canada;
• the child’s links to the country in relation to which the H&C decision is being considered;
• medical issues or special needs the child may have;
• the impact to the child’s education;
• matters related to the child’s gender.
[Emphasis added]
B. Alive

[10] The requirement that a child’s best interests be given careful consideration was reiterated by the Federal Court of Appeal in Hawthorne v. Canada (Minister of Citizenship and Immigration), [2003] 2 F.C. 555 (C.A) (QL) at para. 52:
The requirement that officers' reasons clearly demonstrate that the best interests of an affected child have received careful attention no doubt imposes an administrative burden. But this is as it should be. Rigorous process requirements are fully justified for the determination of subsection 114(2) applications that may adversely affect the welfare of children with the right to reside in Canada: vital interests of the vulnerable are at stake and opportunities for substantive judicial review are limited.

[11] Once an officer is aware of the best interest factors in play in an H&C application, these factors must be considered in their full context and the relationship between the factors and other elements of the fact scenario concerned must be fully understood. Simply listing the best interest factors in play without providing an analysis on their inter-relationship is not being alive to the factors. In my opinion, in order to be alive to a child’s best interests, it is necessary for a visa officer to demonstrate that he or she well understands the perspective of each of the participants in a given fact scenario, including the child if this can reasonably determined.
C. Sensitive

[12] It is only after a visa officer has gained a full understanding of the real life impact of a negative H&C decision on the best interests of a child can the officer give those best interests sensitive consideration. To demonstrate sensitivity, the officer must be able to clearly articulate the suffering of a child that will result from a negative decision, and then say whether, together with a consideration of other factors, the suffering warrants humanitarian and compassionate relief. As stated in Baker at para. 75:
“ … where the interests of children are minimized, in a manner inconsistent with Canada's humanitarian and compassionate tradition and the Minister's guidelines, the decision will be unreasonable”
II. Did the Officer Meet the Requirements for Determining Best Interests?

[13] The Officer’s determination of best interests of the children in the present case is as follows:
Best interests of the children
The applicant has 4 Canadian grandchildren in Newfoundland. He states that those children and he would suffer if he has to leave Canada for Latvia. He says that he is their primary father figure and the only one who could teach them their Russian heritage. The father of those children, the applicant’s son, was deported to Latvia in 2005.
The applicant states that the children and their Canadian mother depend on him for emotional and financial support.
I acknowledge that the return of the applicant to Latvia will cause hardship to his 4 grandchildren. However, family separation is within the normal consequences of the removal of someone who has no recognized status to remain in Canada. I note that there is no indication on file that this situation would mean unusual and undeserved or disproportionate hardship.
In addition, the applicant affirms that one of his grandchildren suffers from Type-2 diabetes. I note that with proper treatment, the condition of the child is manageable. His situation can be improved by eating healthy meals and snacks, enjoying regular physical activity and taking diabetes medications (including insulin), if prescribed by the doctor (see Type 2 diabetes: the basics on the Canadian Diabetes Association website).
I also note that the applicant has his own family back in Latvia, a daughter and a son.
I have considered the best interests of the 4 Canadian children and find that the applicant has not established that returning to Latvia and leaving them behind would have a significant negative impact on those children that would amount to unusual and undeserved or disproportionate hardship.
[Emphasis added]
(Decision, Tribunal Record, p.8)

[14] In my opinion this passage does not meet the standard set above for an alert, alive, and sensitive determination of the best interests of the Applicant’s grandchildren. There is no meaningful critical analysis of the best interests of these children in their real life situation. In particular, it is obvious from cursory acknowledgement in the decision of Alexsey’s diabetic condition that the Officer was not alert, nor alive, to the seriousness of his health problem. The evidence on the record with respect to Alexsey’s health, which was apparently neglected by the Officer, is as follows:
My greatest concern is for a Russian man from Latvia by the name of Alexei Kolosovs. He has been in Sanctuary at the West End Baptist Church since April 26, 2005. The day of his scheduled deportation his 2 year old grandson was in very serious condition in the Children’s Hospital, where he had been brought 3 days earlier in a diabetic coma…It was Alexei that was there at the birth of the children and has been the emotional and financial (before his work permit was revoked) support of this little family.
(Letter dated 23 February 2006, Tribunal Record, p. 101)
He is especially close to his grandchildren and has in fact been very much the emotional and financial support for them. The youngest grandchildren are 2 year old twins, one of whom is named after Alexi. This grandchild suffers with juvenile diabetes and was in the hospital at the time Alexi was to be deported. His grandchildren need him as a male role model in their lives.
(Letter dated 6 February 2006, Tribunal Record p.104)
Days before his scheduled deportation in April 2005, Mr. Kolosovs’s[sic] 2 year old grandson [also named Alexi] was brought to the Janeway Children’s Hospital emergency room where he was subsequently diagnosed with juvenile diabetes. His concern for his grandson’s health and the circumstances of the rest of the family led Mr. Kolosovs to seek sanctuary in West End Baptist church.
(Letter dated 25 November 2005, Tribunal Record p.106)
The child was diagnosed with juvenile diabetes, an illness that is extremely hard to control in a small child. This little boy is one of a twin and he has had several severe relapses that required hospitalization. Alexey loves his grandchildren, and they love him.
(Letter dated 8 September 2006, Tribunal Record p. 130)
In my opinion, the glib use of an undue hardship standard in the present case certainly reflects a lack of sensitivity to each of the children.

[15] As a result, I find that the decision is unreasonable.
III. Was the Decision Rendered in Breach of Due Process?

[16] The Applicant argues that the Decision was rendered in breach of due process because the Officer twice relied on extrinsic evidence, but did not give the Applicant an opportunity to consider the evidence and to respond. This requirement is emphasized at several points in the Guidelines:
11.1 Procedural fairness
Officers must follow procedural fairness in making their decisions.
Officers should:
· carefully consider all the information before them;
· inform the applicant when considering outside information, giving the applicant a chance to respond;
· request any additional information needed;
5.6. First-step assessment: Toward the H&C decision
…
The decision-maker considers the applicant's submissions in light of all the information known to the officer. If the information is extrinsic (i.e., information from a source other than the applicant or information to which the applicant does not have access or is not aware is being used in the decision), this information should be shared with the applicant, and submissions on the information should be invited, before the information is used in the decision.

[17] The Officer used two pieces of information in contravention of this fairness rule: with respect to Alexsey’s condition, general information on the treatment of Type 2 diabetes from the Canadian Diabetes Association website; and internal “notes to file” respecting the Applicant’s negative 2003 PRRA decision. In my opinion, the use of each piece of information had an unfair negative impact in the Decision.

[18] The Canadian Diabetes Association information appears to be geared towards adults seeking to tailor their life style to minimize their Type 2 diabetes symptoms, and is of minimal relevance to a young child that already has serious onset.

[19] The Applicant’s H&C submissions indicate he would have difficult obtaining employment in Latvia because he does not speak Latvian and the language laws require competency in Latvian. The internal “notes to file” are used to conclude that this was not an important factor as follows:
Additionally, I acknowledge that in the Note to file of the applicant’s pre-removal risk assessment (PRRA), the officer wrote:
“Concerning the applicant’s stated risk re denial of employment I am satisfied that this amounts to speculation. I realize that some occupations require a proficiency in the Latvian language but not all do. According to one source members of Russian ethnic group comprises 29.6% of the population of Latvia. I could find nothing in my research that would allow me to conclude that they are denied employment as a general rule”.
It is not clear whether the Applicant knew of the opinion expressed some four years before, but, in any event, he had no notice that it would be used to his detriment in the present H&C proceeding. Indeed, there is no evidence concerning the reliability of the source the PRRA officer used, or whether the language laws in Latvia had changed in the intervening years.

[20] As a result, I find that the Decision was rendered in breach of due process.


## 33110:2 · paragraphs 21-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `edde9cd2c5cf37fbb3ae200eb5b24a49dad7cca4c9961c2e0d3daccde46a97df`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33110:2:subtheme:1 · paragraphs 21-22

- Raw key terms: `accordingly, aleksejs, aside, back, campbell, cause, citizenship, counsel`
- Display key terms: `accordingly, aleksejs, aside, back, campbell`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: accordingly, aleksejs, aside, back, campbell No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
Accordingly, I set aside the Decision, and refer the matter back for re-determination before a different visa officer.
“Douglas R. Campbell”
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-873-07

STYLE OF CAUSE: ALEKSEJS VITALY KOLOSOVS v. THE MINISTER
OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: FEBRUARY 4, 2008
REASONS FOR 

## 33110:3 · paragraphs 23-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7cc710d6548d43c258e68410f87e1f41d74f578b63ef2dd18998b3e8408a1124`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33110:3:subtheme:1 · paragraphs 23-23

- Raw key terms: `appearances, applicant, attorney, barrister, campbell, canada, dated, deputy`
- Display key terms: `barrister, campbell, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, campbell, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: CAMPBELL J.
DATED: FEBRUARY 7, 2008
APPEARANCES:
ELIZABETH LIM FOR THE APPLICANT
RHONDA MARQUIS FOR THE RESPONDENT
SOLICITORS OF RECORD:
ELIZABETH LIM
Barrister & Solicitor
Toronto, Ontario FOR THE APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada
Toronto, Ontario FOR THE RESPONDENT
