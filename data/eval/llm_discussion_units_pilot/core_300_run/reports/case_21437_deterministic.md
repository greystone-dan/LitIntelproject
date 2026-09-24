# Discussion Units: case 21437

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **3**
- Paragraph source hashes: **30**
- Sub-themes: **10**

## 21437:1 · paragraphs 0-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d2c2270c2c2f10eb0ac7e74c5800c4b868902f27230c4df3e25ce5f8a30e20ab`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21437:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, board, decision, immigration, refugee, application, april, august`
- Display key terms: `refugee, april, august`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: refugee, april, august Rule/authority context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5007272` offsets `27-32`; context: [1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S.

#### 21437:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `applicant, applied, board, ceased, refugee, status, accordance, alleges`
- Display key terms: `applied, ceased, refugee, status, accordance, alleges`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: applied, ceased, refugee, status, accordance, alleges Application context: [3] On June 22, 2006, the respondent applied to the Board for a determination of whether the applicant’s refugee status had ceased in accordance with section 108 of the Act, and section 57 of the Convention Refugee Deter | It indicated that the applicant’s explanation that he had applied for a Congolese passport with the intention of helping a business associate could not overcome the spirit and the letter of paragraph 108(1)(a) which impl Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5007274` offsets `81-88`; context: [3] On June 22, 2006, the respondent applied to the Board for a determination of whether the applicant’s refugee status had ceased in accordance with section 108 of the Act, and section 57 of the Convention Refugee Determination Division Rules.
- Evidence: `reasoning_application` cue `applied` at chunk `5007274` offsets `37-44`; context: [3] On June 22, 2006, the respondent applied to the Board for a determination of whether the applicant’s refugee status had ceased in accordance with section 108 of the Act, and section 57 of the Convention Refugee Determination Division Rules.
- Evidence: `issue` cue `ISSUE` at chunk `5007275` offsets `677-682`; context: ISSUE
- Evidence: `evidence_fact` cue `determined that` at chunk `5007275` offsets `49-64`; context: [4] In its decision of August 8, 2007, the Board determined that the applicant’s refugee status had ceased.
- Evidence: `reasoning_application` cue `applied` at chunk `5007275` offsets `166-173`; context: It indicated that the applicant’s explanation that he had applied for a Congolese passport with the intention of helping a business associate could not overcome the spirit and the letter of paragraph 108(1)(a) which implies that refugee status is lost when one voluntarily reavails himself of the protection of his country of nationality.

#### 21437:1:subtheme:3 · paragraphs 5-6

- Raw key terms: `applicant, board, review, standard, actually, application, appreciation, appropriate`
- Display key terms: `review, standard, actually, appreciation, appropriate`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position Display terms: review, standard, actually, appreciation, appropriate Position/evidence statements: The applicant contends that the Board ignored his explanations as to why he obtained a Congolese passport. Rule/authority context: STANDARD OF REVIEW | [6] Neither the applicant nor the respondent made representations in their memorandum as to the appropriate standard of review. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5007276` offsets `13-18`; context: [5] The sole issue raised by this application is whether the Board erred in determining that the applicant had reavailed himself of the protection of his country of nationality.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5007276` offsets `178-196`; context: STANDARD OF REVIEW
- Evidence: `party_position` cue `contends` at chunk `5007277` offsets `142-150`; context: The applicant contends that the Board ignored his explanations as to why he obtained a Congolese passport.
- Evidence: `governing_rule` cue `standard of review` at chunk `5007277` offsets `108-126`; context: [6] Neither the applicant nor the respondent made representations in their memorandum as to the appropriate standard of review.
- Evidence: `counterargument_limitation` cue `However` at chunk `5007277` offsets `235-242`; context: However, a fair reading of the Board’s decision indicates that the Board did in fact consider the applicant’s explanations.

#### 21437:1:subtheme:4 · paragraphs 7-8

- Raw key terms: `dunsmuir, paragraph, states, altered, analysis, attract, brunswick, cannot`
- Display key terms: `dunsmuir, paragraph, states, altered, analysis, attract, brunswick, cannot`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: dunsmuir, paragraph, states, altered, analysis, attract, brunswick, cannot Rule/authority context: New Brunswick, 2008 SCC 9, the Supreme Court altered the standard of review analysis, moving from three to two standards of review: reasonableness and correctness. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5007278` offsets `334-340`; context: In that decision, the Court states at paragraph 51 that “[…] questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5007278` offsets `88-106`; context: New Brunswick, 2008 SCC 9, the Supreme Court altered the standard of review analysis, moving from three to two standards of review: reasonableness and correctness.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5007278` offsets `341-347`; context: In that decision, the Court states at paragraph 51 that “[…] questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness.

#### 21437:1:subtheme:5 · paragraphs 9-10

- Raw key terms: `above, decision, expertise, factors, nature, question, reasonableness, special`
- Display key terms: `above, expertise, factors, nature, question, reasonableness, special`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: above, expertise, factors, nature, question, reasonableness, special Rule/authority context: [9] Considering the above mentioned factors, the factual nature of the present question, and the special expertise of the Board, the Court finds the standard of review to be that of reasonableness. Application context: [55] A consideration of the following factors will lead to the conclusion that the decision maker should be given deference and a reasonableness test applied: - A privative clause: this is a statutory direction from Parl Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5007280` offsets `401-409`; context: - The nature of the question of law.
- Evidence: `reasoning_application` cue `applied` at chunk `5007280` offsets `150-157`; context: [55] A consideration of the following factors will lead to the conclusion that the decision maker should be given deference and a reasonableness test applied:
- A privative clause: this is a statutory direction from Parliament or a legislature indicating the need for deference.
- Evidence: `issue` cue `question` at chunk `5007281` offsets `79-87`; context: [9] Considering the above mentioned factors, the factual nature of the present question, and the special expertise of the Board, the Court finds the standard of review to be that of reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5007281` offsets `149-167`; context: [9] Considering the above mentioned factors, the factual nature of the present question, and the special expertise of the Board, the Court finds the standard of review to be that of reasonableness.

#### 21437:1:subtheme:6 · paragraphs 11-20

- Raw key terms: `paragraph, protection, reavailment, refugee, country, court, himself, nationality`
- Display key terms: `paragraph, protection, reavailment, refugee, country, himself, nationality`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: paragraph, protection, reavailment, refugee, country, himself, nationality Rule/authority context: [10] The issue of what constitutes “voluntary reavailment” under paragraph 108(1)(a) of the Act is the sole point of contention between the parties. | Article 1C(1) of the Convention reads: “This Convention shall cease to apply to any person falling under the terms of section A if: (1) He has voluntarily reavailed himself of the protection of the country of his nationa Application context: Article 1C(1) of the Convention reads: “This Convention shall cease to apply to any person falling under the terms of section A if: (1) He has voluntarily reavailed himself of the protection of the country of his nationa | Instructively, it states that “[i]f a refugee applies for and obtains a national passport or its renewal, it will, in the absence of proof to the contrary, be presumed that he intends to avail himself of the protection o Evidence spans paragraphs 11-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5007282` offsets `9-14`; context: [10] The issue of what constitutes “voluntary reavailment” under paragraph 108(1)(a) of the Act is the sole point of contention between the parties.
- Evidence: `governing_rule` cue `under` at chunk `5007282` offsets `59-64`; context: [10] The issue of what constitutes “voluntary reavailment” under paragraph 108(1)(a) of the Act is the sole point of contention between the parties.
- Evidence: `governing_rule` cue `under` at chunk `5007284` offsets `354-359`; context: Article 1C(1) of the Convention reads: “This Convention shall cease to apply to any person falling under the terms of section A if: (1) He has voluntarily reavailed himself of the protection of the country of his nationality […].
- Evidence: `reasoning_application` cue `apply` at chunk `5007284` offsets `326-331`; context: Article 1C(1) of the Convention reads: “This Convention shall cease to apply to any person falling under the terms of section A if: (1) He has voluntarily reavailed himself of the protection of the country of his nationality […].
- Evidence: `governing_rule` cue `under` at chunk `5007285` offsets `100-105`; context: [13] As a starting point, paragraph 119 indicates that there are three requirements for reavailment under the Convention: (a) voluntariness: the refugee must act voluntarily; (b) intention: the refugee must intend by his action to reavail himself of the protection of the country of his nationality; and (c) reavailment: the refugee must actually obtain such protection.
- Evidence: `reasoning_application` cue `applies` at chunk `5007286` offsets `234-241`; context: Instructively, it states that “[i]f a refugee applies for and obtains a national passport or its renewal, it will, in the absence of proof to the contrary, be presumed that he intends to avail himself of the protection of the country of his nationality.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5007287` offsets `5-16`; context: [15] Accordingly, the UNHCR Handbook suggests that while a passport application creates a presumption of intention to reavail, proof to the contrary may refute that presumption.
- Evidence: `evidence_fact` cue `found that` at chunk `5007289` offsets `166-176`; context: [17] In Chandrakumar above, the Court reviewed a decision of the Convention Refugee Determination Division (the CRDD), established under the previous Act, wherein it found that the applicants were not Convention refugees because the principal applicant’s act of renewing his Sri Lankan passport indicated that he sought to reavail himself of the protection of his country.
- Evidence: `governing_rule` cue `under` at chunk `5007289` offsets `131-136`; context: [17] In Chandrakumar above, the Court reviewed a decision of the Convention Refugee Determination Division (the CRDD), established under the previous Act, wherein it found that the applicants were not Convention refugees because the principal applicant’s act of renewing his Sri Lankan passport indicated that he sought to reavail himself of the protection of his country.
- Evidence: `reasoning_application` cue `because` at chunk `5007289` offsets `221-228`; context: [17] In Chandrakumar above, the Court reviewed a decision of the Convention Refugee Determination Division (the CRDD), established under the previous Act, wherein it found that the applicants were not Convention refugees because the principal applicant’s act of renewing his Sri Lankan passport indicated that he sought to reavail himself of the protection of his country.

#### 21437:1:subtheme:7 · paragraphs 21-25

- Raw key terms: `applicant, congolese, court, passport, because, board, decision, finds`
- Display key terms: `congolese, passport, because, finds`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: congolese, passport, because, finds Application context: He further indicated that because he did not yet have a Canadian passport, the Thai Embassy would not issue him a visa. | [21] Given the fact that the applicant was already in possession of the Congolese passport when his Canadian travel document was stolen, the Court finds irrelevant his argument that because a Canadian Immigration Officer Evidence spans paragraphs 21-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5007292` offsets `348-353`; context: He further indicated that because he did not yet have a Canadian passport, the Thai Embassy would not issue him a visa.
- Evidence: `reasoning_application` cue `because` at chunk `5007292` offsets `272-279`; context: He further indicated that because he did not yet have a Canadian passport, the Thai Embassy would not issue him a visa.
- Evidence: `reasoning_application` cue `because` at chunk `5007293` offsets `182-189`; context: [21] Given the fact that the applicant was already in possession of the Congolese passport when his Canadian travel document was stolen, the Court finds irrelevant his argument that because a Canadian Immigration Officer requested a Congolese passport, his action cannot be considered reavailment.
- Evidence: `reasoning_application` cue `because` at chunk `5007295` offsets `152-159`; context: But here his explanations as a whole were not discarded by the Board because they were not credible; on the contrary the decision seems to imply that, the simple fact of possessing a Congolese passport that the applicant refused for a very specific reason to return to the Congolese authorities when requested by them to do so, constitutes proof of his intention to reavail himself of the protection of his country of nationality.

#### 21437:1:subtheme:8 · paragraphs 26-26

- Raw key terms: `agrees, certify, court, general, interest, parties, question`
- Display key terms: `agrees, certify, interest, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agrees, certify, interest, question Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5007297` offsets `56-64`; context: [25] The Court agrees with the parties that there is no question of general interest to certify.

#### Section text

Nsende v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-04-23
Neutral citation
2008 FC 531
File numbers
IMM-3635-07
Notes
Reported Decision
Decision Content
Date: 20080423
Docket: IMM-3635-07
Citation: 2008 FC 531
Montréal, Quebec, April 23, 2008
PRESENT: The Honourable Maurice E. Lagacé
BETWEEN:
Jean Claude NSENDE
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application under subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act) for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board), dated August 8, 2007, rejecting under section 108(a) of the Act, the applicant’s claim for refugee protection.

[2] A citizen of the Democratic Republic of Congo (DRC), the applicant was determined to be a Convention refugee by the Board on July 6, 2001.

[3] On June 22, 2006, the respondent applied to the Board for a determination of whether the applicant’s refugee status had ceased in accordance with section 108 of the Act, and section 57 of the Convention Refugee Determination Division Rules.

[4] In its decision of August 8, 2007, the Board determined that the applicant’s refugee status had ceased. It indicated that the applicant’s explanation that he had applied for a Congolese passport with the intention of helping a business associate could not overcome the spirit and the letter of paragraph 108(1)(a) which implies that refugee status is lost when one voluntarily reavails himself of the protection of his country of nationality. The Board also indicated that the fact that the applicant kept his passport even though he alleges that Congolese authorities requested its return demonstrated that he wished to continue to benefit from the protection of the DRC.
ISSUE

[5] The sole issue raised by this application is whether the Board erred in determining that the applicant had reavailed himself of the protection of his country of nationality.
STANDARD OF REVIEW

[6] Neither the applicant nor the respondent made representations in their memorandum as to the appropriate standard of review. The applicant contends that the Board ignored his explanations as to why he obtained a Congolese passport. However, a fair reading of the Board’s decision indicates that the Board did in fact consider the applicant’s explanations. Thus, the Court finds that what the applicant is actually challenging is the Board’s appreciation of that explanation.

[7] In the case of Dunsmuir v. New Brunswick, 2008 SCC 9, the Supreme Court altered the standard of review analysis, moving from three to two standards of review: reasonableness and correctness. In that decision, the Court states at paragraph 51 that “[…] questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness. Some legal issues, however, attract the more deferential standard of reasonableness”.

[8] Further, Dunsmuir states at paragraph 55 :

[55] A consideration of the following factors will lead to the conclusion that the decision maker should be given deference and a reasonableness test applied:
- A privative clause: this is a statutory direction from Parliament or a legislature indicating the need for deference.
- A discrete and special administrative regime in which the decision maker has special expertise […].
- The nature of the question of law. A question of law that is of “central importance to the legal system ... and outside the ... specialized area of expertise” of the administrative decision maker will always attract a correctness standard […]. On the other hand, a question of law that does not rise to this level may be compatible with a reasonableness standard where the two above factors so indicate.

[9] Considering the above mentioned factors, the factual nature of the present question, and the special expertise of the Board, the Court finds the standard of review to be that of reasonableness. According to this standard, the Court’s analysis of the Board’s decision will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] […] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at paragraph 47).
ANALYSIS

[10] The issue of what constitutes “voluntary reavailment” under paragraph 108(1)(a) of the Act is the sole point of contention between the parties. There is little precedent relative to this provision and its interpretation by this Court.

[11] Paragraph 108(1)(a) of the Act reads as follows:
108. (1) A claim for refugee protection shall be rejected, and a person is not a Convention refugee or a person in need of protection, in any of the following circumstances:
(a) the person has voluntarily reavailed himself of the protection of their country of nationality;
[…]
108. (1) Est rejetée la demande d’asile et le demandeur n’a pas qualité de réfugié ou de personne à protéger dans tel des cas suivants :
a) il se réclame de nouveau et volontairement de la protection du pays dont il a la nationalité;
[…]

[12] In order to determine what is meant by “reavailment” paragraph 108(1)(a) of the Act, it may be useful to examine the interpretation that has been given to its source article in the 1951 Convention relating to the Status of Refugees (the Convention). Article 1C(1) of the Convention reads: “This Convention shall cease to apply to any person falling under the terms of section A if: (1) He has voluntarily reavailed himself of the protection of the country of his nationality […].” Paragraphs 118 to 125 of the Handbook on Procedures and Criteria for Determining Refugee Status under the 1951 Convention and the 1967 Protocol relating to the Status of Refugees of the United Nations High Commission for Refugees (the UNHCR Handbook) provide some interpretative guidance as to the meaning of reavailment.

[13] As a starting point, paragraph 119 indicates that there are three requirements for reavailment under the Convention: (a) voluntariness: the refugee must act voluntarily; (b) intention: the refugee must intend by his action to reavail himself of the protection of the country of his nationality; and (c) reavailment: the refugee must actually obtain such protection.

[14] Further, the UNHRC Handbook highlights the distinction between “actual reavailment of protection and occasional and incidental contacts with the national authorities” (paragraph 21). Instructively, it states that “[i]f a refugee applies for and obtains a national passport or its renewal, it will, in the absence of proof to the contrary, be presumed that he intends to avail himself of the protection of the country of his nationality.”

[15] Accordingly, the UNHCR Handbook suggests that while a passport application creates a presumption of intention to reavail, proof to the contrary may refute that presumption.

[16] The above interpretation is broadly consistent with the decisions of this Court in Yada v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 37 (QL) and also in Chandrakumar v. Canada (Minister of Employment and Immigration), [1997] F.C.J. No. 615 (QL).

[17] In Chandrakumar above, the Court reviewed a decision of the Convention Refugee Determination Division (the CRDD), established under the previous Act, wherein it found that the applicants were not Convention refugees because the principal applicant’s act of renewing his Sri Lankan passport indicated that he sought to reavail himself of the protection of his country.

[18] In that particular case, the applicant cited with approval of the Court an excerpt from James C. Hathaway’s book, The Law of Refugee Status, Butterworths, Toronto,1991, at page 193, where Professor Hathaway made the following observations regarding reavailment:
[…] the diplomatic request must be made as an act of re-availment of protection, thus implying an intention to have one’s interests defended by the issuing state. In contrast, most ordinary, purely practical forms of diplomatic contact such as requests for the certification of educational or occupational qualifications, or access to personal birth, marital, and other records, are dictated by practical necessity, rather than by a desire for protection.…
[…]
Since there is not automatic linkage between the issuance or renewal of a passport and the granting of protection, it is critical that the real reason it is being sought form part of the determination authority’s considerations. Unless the refugee’s motive is genuinely the entrusting of her interests to the protection of the state of her nationality, the requisite intent is absent.
(emphasis added)

[19] In Chandrakumar above, the Court went on to find that the CRDD committed an error “by failing to explore the principal applicant’s motivations in applying to renew his Sri Lankan passport while in Germany” (paragraph 6). It was also of the view that the CRDD must engage in an analysis of the “intention behind the renewal of a passport”, and that it was unreasonable to assume that the simple action of renewing a passport without any indication of the requisite intent was sufficient to establish reavailment (paragraph 5).

[20] At the hearing, the applicant offered an explanation for seeking a passport from the DRC. He indicated that he was attempting to travel to Thailand in order to have precious gems cut cheaply as part of his international business activities. He further indicated that because he did not yet have a Canadian passport, the Thai Embassy would not issue him a visa. The applicant traveled to Belgium, where a friend and business associate convinced him to get a Congolese passport. They picked up all the necessary documents for him, dropped them off when they were completed, and later retrieved his passport for him. Upon returning to Montreal, the applicant received a letter from the Congolese Embassy in Belgium stating that he had been issued a passport by mistake as he had refugee status in Canada and requested it be returned. He indicated that he had not returned the passport because the Congolese authorities refused to refund the fee he had paid to obtain it.

[21] Given the fact that the applicant was already in possession of the Congolese passport when his Canadian travel document was stolen, the Court finds irrelevant his argument that because a Canadian Immigration Officer requested a Congolese passport, his action cannot be considered reavailment.

[22] However, the Court finds that the Board erred in its consideration of the applicant’s explanation relating to his business activities in Thailand. As outlined in Dunsmuir, above, a review on the standard of reasonableness is concerned with the “existence of justification, transparency and intelligibility” in the decision. With respect, the Court finds a justification lacking in the present case. It is unclear to the Court why the Board believed that the applicant’s explanation with respect to why he obtained a Congolese passport was insufficient. This conclusion may have been open to the Board to make; however, the Court finds it unreasonable that the Board failed to indicate why this explanation was insufficient. If the Board did not believe the applicant’s explanation and found him not to be credible then it should have said so. If it had another reason for not finding the explanation sufficient, it should have stated so as well, especially with the type of explanations provided here by the applicant to rebut his presumed intention “to avail himself of the protection of the country of his nationality”.

[23] True the burden was on the applicant to rebut this presumption, and he tried. But here his explanations as a whole were not discarded by the Board because they were not credible; on the contrary the decision seems to imply that, the simple fact of possessing a Congolese passport that the applicant refused for a very specific reason to return to the Congolese authorities when requested by them to do so, constitutes proof of his intention to reavail himself of the protection of his country of nationality. The Court cannot accept such implied finding in the present affair in view of the inexistence of any credibility finding in the decision with respect to the applicant’s explanations.

[24] For the foregoing reasons the Court finds the Board’s decision to be unreasonable.

[25] The Court agrees with the parties that there is no question of general interest to certify.


## 21437:2 · paragraphs 27-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b1ee9b5071ecb9d05f6f752c05bdbad5078d03544956007de50488681c19104e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21437:2:subtheme:1 · paragraphs 27-28

- Raw key terms: `reasons, allows, applicant, application, back, board, cause, ceased`
- Display key terms: `allows, back, ceased`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: allows, back, ceased Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5007297` offsets `262-269`; context: JUDGMENT
FOR THE FOREGOING REASONS, THE COURT allows the application and refers the matter back to a newly constituted Board for rehearing and redetermination as to whether the applicant has or has not ceased to be a Convention refugee.

#### Section text

JUDGMENT
FOR THE FOREGOING REASONS, THE COURT allows the application and refers the matter back to a newly constituted Board for rehearing and redetermination as to whether the applicant has or has not ceased to be a Convention refugee.
“Maurice E. Lagacé”
Deputy Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3635-07
STYLE OF CAUSE: Jean Claude NSENDE v.
M.C.I.
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: March 26, 2008
REASONS FOR 

## 21437:3 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2fa7b5649ce4df029f820c0d40d282ded4e0a2706dcd30b969966d659bcb14cd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21437:3:subtheme:1 · paragraphs 29-29

- Raw key terms: `allen, appearances, applicant, april, artinian, associ, attorney, canada`
- Display key terms: `allen, april, artinian, associ`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allen, april, artinian, associ No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT LAGACÉ D.J.
AND JUDGMENT:
DATED: April 23, 2008
APPEARANCES:
Victor Artinian
FOR THE APPLICANT
Simone Truong
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Joseph W. Allen & Associés
Montréal, Quebec
FOR THE APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
