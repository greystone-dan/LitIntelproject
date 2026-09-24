# Discussion Units: case 14430

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **42**
- Continuity pairs: **41**
- Discussion Units: **2**
- Paragraph source hashes: **42**
- Sub-themes: **9**

## 14430:1 · paragraphs 0-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6cf0c0032b34afd98e98066e9cb653909582c097defd9452f3f608007a6520f9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14430:1:subtheme:1 · paragraphs 0-14

- Raw key terms: `applicant, board, certificate, decision, refugee, udps, applicant's, application`
- Display key terms: `certificate, refugee, udps, applicant's`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: certificate, refugee, udps, applicant's Position/evidence statements: [3] The applicant claims to be a citizen of the Democratic Republic of the Congo and a member of the Union pour la démocratie et le progrès social [Union for democracy and social progress] (the UDPS). | [10] The Board gave no weight to the driver's licence, which the applicant claimed to have obtained in 1996, because the Board noted that it had actually been issued on November 10, 1997, and delivered on November 18, 19 Rule/authority context: This is an application for judicial review of that decision under subsection 72(1) of the Immigration and Refugee Protection Act, S. | [6] The Board determined that the applicant was neither a "refugee" within the meaning of section 96 of the IRPA nor a "person in need of protection" under subsection 97(1) of the same Act. Application context: [10] The Board gave no weight to the driver's licence, which the applicant claimed to have obtained in 1996, because the Board noted that it had actually been issued on November 10, 1997, and delivered on November 18, 19 | [11] In addition, because there was no stamp on the marriage certificate, the Board noted that the applicant had failed to produce the proxy he claimed to have given his brother in order to enter into his marriage in Kin Operative outcome context: [5] On November 19, 2004, the application for leave to commence an application for judicial review was allowed. Evidence spans paragraphs 0-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4705367` offsets `163-178`; context: [1] On March 31, 2004, a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) was made by Member Jean-Marie Chastenay, who determined that the applicant was neither a refugee nor a person in need of protection.
- Evidence: `governing_rule` cue `under` at chunk `4705367` offsets `311-316`; context: This is an application for judicial review of that decision under subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claims` at chunk `4705369` offsets `18-24`; context: [3] The applicant claims to be a citizen of the Democratic Republic of the Congo and a member of the Union pour la démocratie et le progrès social [Union for democracy and social progress] (the UDPS).
- Evidence: `disposition` cue `allowed` at chunk `4705371` offsets `103-110`; context: [5] On November 19, 2004, the application for leave to commence an application for judicial review was allowed.
- Evidence: `evidence_fact` cue `determined that` at chunk `4705372` offsets `14-29`; context: [6] The Board determined that the applicant was neither a "refugee" within the meaning of section 96 of the IRPA nor a "person in need of protection" under subsection 97(1) of the same Act.
- Evidence: `governing_rule` cue `under` at chunk `4705372` offsets `150-155`; context: [6] The Board determined that the applicant was neither a "refugee" within the meaning of section 96 of the IRPA nor a "person in need of protection" under subsection 97(1) of the same Act.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705374` offsets `85-93`; context: [8] The Board was of the view that the applicant had not met his burden of producing evidence establishing that he was a citizen of the Democratic Republic of the Congo:
The claimant may be from the DRC [Democratic Republic of the Congo]; however, the panel does not know where he comes from, where he lived, for how long and with what status.
- Evidence: `counterargument_limitation` cue `however` at chunk `4705374` offsets `239-246`; context: [8] The Board was of the view that the applicant had not met his burden of producing evidence establishing that he was a citizen of the Democratic Republic of the Congo:
The claimant may be from the DRC [Democratic Republic of the Congo]; however, the panel does not know where he comes from, where he lived, for how long and with what status.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705375` offsets `43-51`; context: [9] The following documents were among the evidence to which the Board gave no weight: driver's licence, marriage certificate, UDPS combatant certificate, UDPS membership card, photos, clipping from the Observateur newspaper.
- Evidence: `party_position` cue `claimed` at chunk `4705376` offsets `75-82`; context: [10] The Board gave no weight to the driver's licence, which the applicant claimed to have obtained in 1996, because the Board noted that it had actually been issued on November 10, 1997, and delivered on November 18, 1997, when the applicant was in jail.
- Evidence: `reasoning_application` cue `because` at chunk `4705376` offsets `109-116`; context: [10] The Board gave no weight to the driver's licence, which the applicant claimed to have obtained in 1996, because the Board noted that it had actually been issued on November 10, 1997, and delivered on November 18, 1997, when the applicant was in jail.
- Evidence: `party_position` cue `claimed` at chunk `4705377` offsets `144-151`; context: [11] In addition, because there was no stamp on the marriage certificate, the Board noted that the applicant had failed to produce the proxy he claimed to have given his brother in order to enter into his marriage in Kinshasa, in the Democratic Republic of the Congo, when he was in the United States.
- Evidence: `reasoning_application` cue `because` at chunk `4705377` offsets `18-25`; context: [11] In addition, because there was no stamp on the marriage certificate, the Board noted that the applicant had failed to produce the proxy he claimed to have given his brother in order to enter into his marriage in Kinshasa, in the Democratic Republic of the Congo, when he was in the United States.
- Evidence: `evidence_fact` cue `found that` at chunk `4705378` offsets `15-25`; context: [12] The Board found that the applicant had never been a member of the UDPS, because the combatant certificate was signed by someone calling himself the Co-President, even though, according to the documentary evidence, there was no such position, and because the membership card did not look like the official version in the Political Handbook 1999.
- Evidence: `reasoning_application` cue `because` at chunk `4705378` offsets `77-84`; context: [12] The Board found that the applicant had never been a member of the UDPS, because the combatant certificate was signed by someone calling himself the Co-President, even though, according to the documentary evidence, there was no such position, and because the membership card did not look like the official version in the Political Handbook 1999.

#### 14430:1:subtheme:2 · paragraphs 15-16

- Raw key terms: `applicant, applicant's, board, accept, according, acknowledged, addition, advice`
- Display key terms: `applicant's, accept, according, acknowledged, addition, advice`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: applicant's, accept, according, acknowledged, addition, advice Application context: However, the Board did not accept his explanation that he was rejected because of inconsistencies due to poor interpretation, since that explanation was contradicted by his answer to question 41 on his PIF, according to  Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4705381` offsets `300-308`; context: However, the Board did not accept his explanation that he was rejected because of inconsistencies due to poor interpretation, since that explanation was contradicted by his answer to question 41 on his PIF, according to which he had been given bad advice by a fellow Congolese countryman.
- Evidence: `reasoning_application` cue `because` at chunk `4705381` offsets `188-195`; context: However, the Board did not accept his explanation that he was rejected because of inconsistencies due to poor interpretation, since that explanation was contradicted by his answer to question 41 on his PIF, according to which he had been given bad advice by a fellow Congolese countryman.
- Evidence: `counterargument_limitation` cue `However` at chunk `4705381` offsets `117-124`; context: However, the Board did not accept his explanation that he was rejected because of inconsistencies due to poor interpretation, since that explanation was contradicted by his answer to question 41 on his PIF, according to which he had been given bad advice by a fellow Congolese countryman.
- Evidence: `issue` cue `ISSUES` at chunk `4705382` offsets `510-516`; context: ISSUES
- Evidence: `evidence_fact` cue `testimony` at chunk `4705382` offsets `412-421`; context: This, in addition to the lack of identification, deprived the Board of important and relevant documents that might have corroborated the applicant's testimony: Elazi v.

#### 14430:1:subtheme:3 · paragraphs 17-18

- Raw key terms: `board, identity, refugee, access, adar, analysis, applicant's, appropriate`
- Display key terms: `identity, refugee, access, adar, analysis, applicant's, appropriate`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: identity, refugee, access, adar, analysis, applicant's, appropriate Application context: On judicial review, the Court must show deference to the Board's assessment of the identity documents and testimony of the refugee claimants because the Board had first-hand access to them and possesses a high level of e Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4705383` offsets `9-14`; context: [17] The issue that arises in the case at bar is the following: was it patently unreasonable for the Board to reject the applicant's refugee claim on the ground that he had failed to establish his identity?
- Evidence: `evidence_fact` cue `testimony` at chunk `4705384` offsets `461-470`; context: On judicial review, the Court must show deference to the Board's assessment of the identity documents and testimony of the refugee claimants because the Board had first-hand access to them and possesses a high level of expertise in this area.
- Evidence: `reasoning_application` cue `because` at chunk `4705384` offsets `496-503`; context: On judicial review, the Court must show deference to the Board's assessment of the identity documents and testimony of the refugee claimants because the Board had first-hand access to them and possesses a high level of expertise in this area.

#### 14430:1:subtheme:4 · paragraphs 19-19

- Raw key terms: `acceptable, acceptables, account, claimant, compte, credibility, d'identit, demandeur`
- Display key terms: `acceptable, acceptables, account, compte, credibility, d'identit, demandeur`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acceptable, acceptables, account, compte, credibility, d'identit, demandeur Evidence spans paragraphs 19-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4705385` offsets `145-152`; context: The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.

#### 14430:1:subtheme:5 · paragraphs 20-23

- Raw key terms: `board, according, applicant, applicant's, argued, erred, evidence, explanation`
- Display key terms: `according, applicant's, erred, explanation`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: according, applicant's, erred, explanation Position/evidence statements: [20] The applicant argued that the Board erred in drawing an adverse credibility inference from his inability to explain why the same photo was on three identity documents, one from 1996, one from 1997 and one from 1998. | He argued that there was evidence of the route he took because he did produce the bus ticket he used to get to the Lacolle border crossing to claim refugee status. Application context: He argued that there was evidence of the route he took because he did produce the bus ticket he used to get to the Lacolle border crossing to claim refugee status. Evidence spans paragraphs 20-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `argued` at chunk `4705386` offsets `19-25`; context: [20] The applicant argued that the Board erred in drawing an adverse credibility inference from his inability to explain why the same photo was on three identity documents, one from 1996, one from 1997 and one from 1998.
- Evidence: `evidence_fact` cue `testimony` at chunk `4705387` offsets `131-140`; context: According to the applicant's testimony before the Board, "[TRANSLATION] .
- Evidence: `evidence_fact` cue `evidence` at chunk `4705388` offsets `143-151`; context: However, in light of the other evidence the Board considered and addressed in its reasons, the error is not critical.
- Evidence: `counterargument_limitation` cue `However` at chunk `4705388` offsets `112-119`; context: However, in light of the other evidence the Board considered and addressed in its reasons, the error is not critical.
- Evidence: `party_position` cue `argued` at chunk `4705389` offsets `218-224`; context: He argued that there was evidence of the route he took because he did produce the bus ticket he used to get to the Lacolle border crossing to claim refugee status.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705389` offsets `156-164`; context: [23] According to the applicant, the Board's decision was largely based on his itinerary before coming to Canada and on the fact that he did not produce in evidence the travel document he used to leave his country.
- Evidence: `reasoning_application` cue `because` at chunk `4705389` offsets `270-277`; context: He argued that there was evidence of the route he took because he did produce the bus ticket he used to get to the Lacolle border crossing to claim refugee status.

#### 14430:1:subtheme:6 · paragraphs 24-35

- Raw key terms: `board, applicant, documents, applicant's, canada, identity, claimed, evidence`
- Display key terms: `documents, applicant's, identity, claimed`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: documents, applicant's, identity, claimed Position/evidence statements: [24] The applicant also claimed there was evidence of his identity: his Congolese passport seized by the United States Immigration and Naturalization Service (USINS) in the United States. | The Board pointed out that the documents the applicant claimed to have given back to his smuggler might have corroborated his identity. Rule/authority context: The respondent pointed out that the applicant said that he himself produced, before the Board, documents from his USINS file in order to prove his identity, which begs the question why, under the circumstances, did he no | Under the circumstances, it was not patently unreasonable for the Board to give the marriage certificate no weight. Application context: [25] The respondent pointed out that the Board properly applied the principle, from the decision of Nadon J. | In terms of the driver's licence, the applicant argued that if the Board "[TRANSLATION] does not believe that the applicant applied for the licence before going to jail as he explained, the Member may logically believe t Operative outcome context: The decisions of this Court indicate clearly that a refugee claim must be dismissed once the Board determines that the identity of the claimant has not been proven: Najam v. Evidence spans paragraphs 24-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4705390` offsets `528-536`; context: The respondent pointed out that the applicant said that he himself produced, before the Board, documents from his USINS file in order to prove his identity, which begs the question why, under the circumstances, did he not produce the other documents?
- Evidence: `party_position` cue `claimed` at chunk `4705390` offsets `24-31`; context: [24] The applicant also claimed there was evidence of his identity: his Congolese passport seized by the United States Immigration and Naturalization Service (USINS) in the United States.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705390` offsets `42-50`; context: [24] The applicant also claimed there was evidence of his identity: his Congolese passport seized by the United States Immigration and Naturalization Service (USINS) in the United States.
- Evidence: `governing_rule` cue `under` at chunk `4705390` offsets `542-547`; context: The respondent pointed out that the applicant said that he himself produced, before the Board, documents from his USINS file in order to prove his identity, which begs the question why, under the circumstances, did he not produce the other documents?
- Evidence: `reasoning_application` cue `applied` at chunk `4705391` offsets `56-63`; context: [25] The respondent pointed out that the Board properly applied the principle, from the decision of Nadon J.
- Evidence: `party_position` cue `claimed` at chunk `4705394` offsets `447-454`; context: The Board pointed out that the documents the applicant claimed to have given back to his smuggler might have corroborated his identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705394` offsets `367-375`; context: It looked at the applicant's itinerary incidentally, and did not find that he was trying to keep information from the Board, but rather that he failed to produce sufficient evidence in that regard.
- Evidence: `counterargument_limitation` cue `but` at chunk `4705394` offsets `319-322`; context: It looked at the applicant's itinerary incidentally, and did not find that he was trying to keep information from the Board, but rather that he failed to produce sufficient evidence in that regard.
- Evidence: `party_position` cue `argued` at chunk `4705395` offsets `173-179`; context: In terms of the driver's licence, the applicant argued that if the Board "[TRANSLATION] does not believe that the applicant applied for the licence before going to jail as he explained, the Member may logically believe that the applicant was not in jail.
- Evidence: `reasoning_application` cue `applied` at chunk `4705395` offsets `249-256`; context: In terms of the driver's licence, the applicant argued that if the Board "[TRANSLATION] does not believe that the applicant applied for the licence before going to jail as he explained, the Member may logically believe that the applicant was not in jail.
- Evidence: `reasoning_application` cue `because` at chunk `4705396` offsets `216-223`; context: [28] In terms of the driver's licence, I note that according to the applicant, both of the dates on the licence - the licence "issued" date, November 10, 1997, and the renewal date, November 13, 1997 - are mistakes, because the licence was issued in 1996.
- Evidence: `party_position` cue `claimed` at chunk `4705397` offsets `429-436`; context: Furthermore, the applicant failed to produce the proxy he claimed to have given his brother, a document which would have served to corroborate the marriage.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705397` offsets `212-220`; context: According to the documentary evidence, there have been stamps on official documents since 1998, indicating the legal or administrative fees associated with the issuing of those documents.
- Evidence: `governing_rule` cue `Under` at chunk `4705397` offsets `528-533`; context: Under the circumstances, it was not patently unreasonable for the Board to give the marriage certificate no weight.
- Evidence: `evidence_fact` cue `testimony` at chunk `4705398` offsets `214-223`; context: A careful reading of the transcript of the applicant's testimony on this point shows that he was unable to provide a satisfactory explanation of the shortcomings the Board identified in these documents.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705400` offsets `158-166`; context: [32] In addition, the Board's finding as to the applicant's credibility was also based on his lack of knowledge of the UDPS and on the inconsistencies in his evidence.
- Evidence: `counterargument_limitation` cue `but` at chunk `4705400` offsets `220-223`; context: The applicant was given the opportunity to respond, but failed to satisfy the Board with his answers.
- Evidence: `party_position` cue `claimed` at chunk `4705401` offsets `64-71`; context: [33] Last, I cannot find that the Board erred, as the applicant claimed, in not giving the refugee claim further consideration.
- Evidence: `disposition` cue `dismissed` at chunk `4705401` offsets `202-211`; context: The decisions of this Court indicate clearly that a refugee claim must be dismissed once the Board determines that the identity of the claimant has not been proven: Najam v.

#### 14430:1:subtheme:7 · paragraphs 36-38

- Raw key terms: `identity, applicant, board, board's, central, claimant, court, credibility`
- Display key terms: `identity, board's, central, credibility`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: identity, board's, central, credibility Rule/authority context: The standard of review in credibility cases being the patently unreasonable nature of the Board's decision, it is logical to conclude that the question of whether the claimant possesses acceptable documentation establish Application context: The standard of review in credibility cases being the patently unreasonable nature of the Board's decision, it is logical to conclude that the question of whether the claimant possesses acceptable documentation establish | Accordingly, the intervention of this Court by way of judicial review is unwarranted. Operative outcome context: The application is dismissed. Evidence spans paragraphs 36-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4705402` offsets `57-63`; context: [14] Section 106 of the Act makes it clear that identity issues go to the credibility of the Applicant.
- Evidence: `governing_rule` cue `standard of review` at chunk `4705402` offsets `108-126`; context: The standard of review in credibility cases being the patently unreasonable nature of the Board's decision, it is logical to conclude that the question of whether the claimant possesses acceptable documentation establishing identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding.
- Evidence: `reasoning_application` cue `conclude` at chunk `4705402` offsets `229-237`; context: The standard of review in credibility cases being the patently unreasonable nature of the Board's decision, it is logical to conclude that the question of whether the claimant possesses acceptable documentation establishing identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705403` offsets `243-251`; context: I agree with the Respondent that if the identity of the claimant is not proven, the claim must fail; that means the Board need not pursue an analysis of the evidence in relation to other aspects of the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4705404` offsets `169-177`; context: [34] In short, the Board's finding that the applicant failed to establish his identity was central to the credibility finding, and in my view, in light of the facts and evidence in the record, it was not patently unreasonable.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4705404` offsets `227-238`; context: Accordingly, the intervention of this Court by way of judicial review is unwarranted.
- Evidence: `disposition` cue `dismissed` at chunk `4705404` offsets `332-341`; context: The application is dismissed.

#### 14430:1:subtheme:8 · paragraphs 39-40

- Raw key terms: `application, blanchard, cause, certified, contemplated, court, date, dismissed`
- Display key terms: `blanchard, certified, contemplated, date, dismissed`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: blanchard, certified, contemplated, date, dismissed Operative outcome context: The application for judicial review is dismissed. Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4705405` offsets `50-58`; context: [35] The parties did not suggest that any serious question of general importance be certified as contemplated by paragraph 74(d) of the Immigration and Refugee Protection Act, S.
- Evidence: `disposition` cue `dismissed` at chunk `4705405` offsets `321-330`; context: The application for judicial review is dismissed.

#### Section text

Ipala v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-04-08
Neutral citation
2005 FC 472
File numbers
IMM-3932-04
Decision Content
Date: 2005020408
Docket: IMM-3932-04
Citation: 2005 FC 472
Ottawa, Ontario, April 8, 2005
Present: Mr. Justice Blanchard
BETWEEN:
NKUM-ILUB IPALA
Applicant
- and -
MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER
INTRODUCTION

[1] On March 31, 2004, a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) was made by Member Jean-Marie Chastenay, who determined that the applicant was neither a refugee nor a person in need of protection. This is an application for judicial review of that decision under subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the IRPA).

[2] By way of relief, the applicant is asking this Court to allow the application for judicial review, set aside the Panel's decision and refer the matter back to the Board.
FACT SITUATION

[3] The applicant claims to be a citizen of the Democratic Republic of the Congo and a member of the Union pour la démocratie et le progrès social [Union for democracy and social progress] (the UDPS). As such, he says he took part in a demonstration against the Laurent Désiré Kabila government. He was arrested in the night of November 7-8, 1997, and released on November 28, 1997. He says he left the Democratic Republic of the Congo on December 7, 1997, and arrived in the United States on December 8, 1997.

[4] He made a refugee claim in Canada on June 28, 2003, and that claim was rejected by the Board on March 31, 2004, on the ground that he had not met the burden of establishing his identity.

[5] On November 19, 2004, the application for leave to commence an application for judicial review was allowed.
IMPUGNED DECISION

[6] The Board determined that the applicant was neither a "refugee" within the meaning of section 96 of the IRPA nor a "person in need of protection" under subsection 97(1) of the same Act.

[7] The applicant's refugee claim failed the first determination the Board has to make: identity. The applicant produced no acceptable identification within the meaning of section 106 of the IRPA.

[8] The Board was of the view that the applicant had not met his burden of producing evidence establishing that he was a citizen of the Democratic Republic of the Congo:
The claimant may be from the DRC [Democratic Republic of the Congo]; however, the panel does not know where he comes from, where he lived, for how long and with what status. The panel does not know if the claimant is a citizen of the DRC or a citizen or permanent resident of another country. The panel does not know when he left his country nor what route he took to come to Canada.

[9] The following documents were among the evidence to which the Board gave no weight: driver's licence, marriage certificate, UDPS combatant certificate, UDPS membership card, photos, clipping from the Observateur newspaper. The Board also had the applicant's Personal Information Form (PIF) and testimony.

[10] The Board gave no weight to the driver's licence, which the applicant claimed to have obtained in 1996, because the Board noted that it had actually been issued on November 10, 1997, and delivered on November 18, 1997, when the applicant was in jail. The Board rejected the applicant's claim that the dates were wrong.

[11] In addition, because there was no stamp on the marriage certificate, the Board noted that the applicant had failed to produce the proxy he claimed to have given his brother in order to enter into his marriage in Kinshasa, in the Democratic Republic of the Congo, when he was in the United States.

[12] The Board found that the applicant had never been a member of the UDPS, because the combatant certificate was signed by someone calling himself the Co-President, even though, according to the documentary evidence, there was no such position, and because the membership card did not look like the official version in the Political Handbook 1999. In addition, the Board found that the applicant knew nothing about the political structure of the UDPS, and this undermined his credibility.

[13] The Board also noted that the photos of the applicant on his driver's licence, UDPS membership card and UDPS combatant certificate were identical, even though it was a 1996 membership card, a 1997 driver's licence and a 1998 combatant certificate. The applicant was unable to explain that, and according to the Board, this undermined his credibility.

[14] The Board saw as self-serving the missing person's notice in the Observateur newspaper of August 5, 2003, and gave it no weight. The Board asked the applicant about the reason for the notice indicating that the Ipala family was looking for their son, and was not satisfied with his answer that his immediate family (his father, mother, etc.) knew his whereabouts but his extended family did not.

[15] Last, the Board acknowledged that the applicant did report his unsuccessful refugee claim in the United States. However, the Board did not accept his explanation that he was rejected because of inconsistencies due to poor interpretation, since that explanation was contradicted by his answer to question 41 on his PIF, according to which he had been given bad advice by a fellow Congolese countryman. This was another factor undermining the applicant's credibility, in the Board's opinion.

[16] In short, the Board stated that the applicant had not compensated for the lack of documentation establishing his citizenship by obtaining independent corroboration. The Board noted that he did not have his passport or the plane ticket he had used to travel. This, in addition to the lack of identification, deprived the Board of important and relevant documents that might have corroborated the applicant's testimony: Elazi v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 212 (QL).
ISSUES

[17] The issue that arises in the case at bar is the following: was it patently unreasonable for the Board to reject the applicant's refugee claim on the ground that he had failed to establish his identity?
ANALYSIS

[18] The appropriate standard for reviewing the Board's assessment of identity documents is patent unreasonableness: Gasparyan v. Canada (Minister of Citizenship and Immigration), 2003 FC 863; Adar v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 695 (QL); Mbabazi v. Canada (Minister of Citizenship and Immigration), 2002 FCT 1191. On judicial review, the Court must show deference to the Board's assessment of the identity documents and testimony of the refugee claimants because the Board had first-hand access to them and possesses a high level of expertise in this area.

[19] Section 106 of the IRPA states:
106. The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have taken reasonable steps to obtain the documentation.
106. La Section de la protection des réfugiés prend en compte, s'agissant de crédibilité, le fait que, n'étant pas muni de papiers d'identité acceptables, le demandeur ne peut raisonnablement en justifier la raison et n'a pas pris les mesures voulues pour s'en procurer.

[20] The applicant argued that the Board erred in drawing an adverse credibility inference from his inability to explain why the same photo was on three identity documents, one from 1996, one from 1997 and one from 1998.

[21] At the hearing, the Court noted that an explanation was in fact given in relation to the photos. According to the applicant's testimony before the Board, "[TRANSLATION] . . . there are eight prints, so you can use the same sheet of photos for . . . for various purposes".

[22] I accept the applicant's arguments on this point. The Board erred in saying no explanation had been given. However, in light of the other evidence the Board considered and addressed in its reasons, the error is not critical.

[23] According to the applicant, the Board's decision was largely based on his itinerary before coming to Canada and on the fact that he did not produce in evidence the travel document he used to leave his country. He argued that there was evidence of the route he took because he did produce the bus ticket he used to get to the Lacolle border crossing to claim refugee status.

[24] The applicant also claimed there was evidence of his identity: his Congolese passport seized by the United States Immigration and Naturalization Service (USINS) in the United States. In his opinion, the Board could have easily had access to the file. The respondent replied that this was yet another indication of the applicant's lack of credibility. The respondent pointed out that the applicant said that he himself produced, before the Board, documents from his USINS file in order to prove his identity, which begs the question why, under the circumstances, did he not produce the other documents?

[25] The respondent pointed out that the Board properly applied the principle, from the decision of Nadon J., as he then was, in Elazi, supra, that the Board can legitimately express reservations about a claimant claiming to have destroyed, lost or given back to the smuggler, the passport and plane ticket used to come to Canada:

[17] I take this opportunity to add that it is entirely reasonable for the Refugee Division to attach great importance to a claimant's passport and his air ticket. In my opinion, these documents are essential to establish the claimant's identity and his journey to come to Canada. . . .

[18] Minimizing the importance of the passport and air ticket as documents to be produced or ignoring their non-submission for all sorts of reasons in my opinion only serves to encourage all those whose only purpose is to take advantage of a system which is intended solely to enable genuine refugees to come to Canada.

[26] In my view, the applicant has misinterpreted the basis for the Board's decision. The Board based its decision on the lack of credibility of the applicant, who failed to prove his identity. It looked at the applicant's itinerary incidentally, and did not find that he was trying to keep information from the Board, but rather that he failed to produce sufficient evidence in that regard. The Board pointed out that the documents the applicant claimed to have given back to his smuggler might have corroborated his identity.

[27] Last, the applicant challenged the fact that the Board gave no weight to his driver's licence and marriage certificate. In terms of the driver's licence, the applicant argued that if the Board "[TRANSLATION] does not believe that the applicant applied for the licence before going to jail as he explained, the Member may logically believe that the applicant was not in jail." As for the marriage certificate, the applicant asserted that marriage by proxy does occur in the Democratic Republic of the Congo and that he had no reason to make one up.

[28] In terms of the driver's licence, I note that according to the applicant, both of the dates on the licence - the licence "issued" date, November 10, 1997, and the renewal date, November 13, 1997 - are mistakes, because the licence was issued in 1996. In my view, since there were two different dates on the same document, it was not patently unreasonable to reject the applicant's explanation and, as a result, to give the licence no weight.

[29] It may well be that marriage by proxy occurs in the Democratic Republic of the Congo. As the Board indicated, there was no stamp on the marriage certificate of October 25, 2001. According to the documentary evidence, there have been stamps on official documents since 1998, indicating the legal or administrative fees associated with the issuing of those documents. Furthermore, the applicant failed to produce the proxy he claimed to have given his brother, a document which would have served to corroborate the marriage. Under the circumstances, it was not patently unreasonable for the Board to give the marriage certificate no weight.

[30] Two other pieces of identification were also produced: the UDPS membership card and the UDPS combatant certificate. The Board doubted their authenticity. A careful reading of the transcript of the applicant's testimony on this point shows that he was unable to provide a satisfactory explanation of the shortcomings the Board identified in these documents.

[31] I accept the respondent's argument that it is for the Board to assess and weigh the value of the identity documents and that in the case at bar, the applicant did not establish that this assessment was patently unreasonable: Aleshkina v. Canada (Minister of Citizenship and Immigration), 2002 FCT 589.

[32] In addition, the Board's finding as to the applicant's credibility was also based on his lack of knowledge of the UDPS and on the inconsistencies in his evidence. The applicant was given the opportunity to respond, but failed to satisfy the Board with his answers. In the case at bar, in my view, the Board made no reviewable error and its findings were not patently unreasonable.

[33] Last, I cannot find that the Board erred, as the applicant claimed, in not giving the refugee claim further consideration. The decisions of this Court indicate clearly that a refugee claim must be dismissed once the Board determines that the identity of the claimant has not been proven: Najam v. Canada (Minister of Citizenship and Immigration), 2004 FC 425; Husein v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 726 (QL). I thus defer to the reasoning of Beaudry J. in Najam, supra, and find that the Board did not err in not taking its analysis any further:

[14] Section 106 of the Act makes it clear that identity issues go to the credibility of the Applicant. The standard of review in credibility cases being the patently unreasonable nature of the Board's decision, it is logical to conclude that the question of whether the claimant possesses acceptable documentation establishing identity is to be reviewed by this Court only if the Board came to a patently unreasonable finding. . . .
. . .

[16] The proof of a claimant's identity is of central importance to his or her claim. I agree with the Respondent that if the identity of the claimant is not proven, the claim must fail; that means the Board need not pursue an analysis of the evidence in relation to other aspects of the claim. . . . (Emphasis added)
CONCLUSION

[34] In short, the Board's finding that the applicant failed to establish his identity was central to the credibility finding, and in my view, in light of the facts and evidence in the record, it was not patently unreasonable. Accordingly, the intervention of this Court by way of judicial review is unwarranted. The application is dismissed.

[35] The parties did not suggest that any serious question of general importance be certified as contemplated by paragraph 74(d) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27. No serious question of general importance will be certified.
ORDER
THE COURT ORDERS:
1. The application for judicial review is dismissed.
2. No serious question of general importance is certified.
"Edmond P. Blanchard"
Judge
Certified true translation
Peter Douglas
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3932-04
STYLE OF CAUSE: Nkum-Ilub Ipala v. MCI
PLACE OF HEARING: Montréal, Quebec
DATE OF HEARING: February 15, 2005
REASONS FOR 

## 14430:2 · paragraphs 41-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2e6705c076f2b91ee4bbf53423c9f57d0bbaa9a44655e7e864df966ab4743491`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14430:2:subtheme:1 · paragraphs 41-41

- Raw key terms: `appearances, applicant, april, attorney, blanchard, bureau, canada, date`
- Display key terms: `april, blanchard, bureau, date`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, blanchard, bureau, date No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER: The Honourable Mr. Justice Edmond P. Blanchard
DATE OF REASONS: April 8, 2005
APPEARANCES:
Eveline Fiset FOR THE APPLICANT
Simone Truong FOR THE RESPONDENT
SOLICITORS OF RECORD:
Eveline Fiset FOR THE APPLICANT
477, rue St-François-Xavier
Bureau 308
Montréal, Quebec H2Y 2T2
514-904-0048, Fax: 514-904-0281
John J. Sims, Q.C. FOR THE RESPONDENT
Deputy Attorney General of Canada
514-283-3295, Fax: 514-283-3856
