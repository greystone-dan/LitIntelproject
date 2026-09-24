# Discussion Units: case 4538

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **24**
- Continuity pairs: **23**
- Discussion Units: **2**
- Paragraph source hashes: **24**
- Sub-themes: **5**

## 4538:1 · paragraphs 0-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `235526af51852d16d9c2fbb2afeb196b5d2b9eb9660de683be2af4f23f3bf340`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4538:1:subtheme:1 · paragraphs 0-16

- Raw key terms: `applicant, principal, ramos, argentina, applicants, board, abuse, protection`
- Display key terms: `principal, ramos, argentina, abuse, protection`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: principal, ramos, argentina, abuse, protection Position/evidence statements: [15] The Applicants argue that the Board erred in its finding about the availability of state protection in Argentina and that the Board ignored relevant evidence in reaching its conclusion, thereby making a perverse fin | [16] Second, the Applicants argue that the Board erroneously applied the wrong test in determining that state protection was available to her. Rule/authority context: Pursuant to Rule 10 of the Convention Refugee Determination Division Rules, all claims are being heard together. Application context: [16] Second, the Applicants argue that the Board erroneously applied the wrong test in determining that state protection was available to her. Evidence spans paragraphs 0-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4255400` offsets `434-449`; context: In its decision dated November 7, 2001, the Board determined that the Applicants are not convention refugees.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4255401` offsets `234-245`; context: Pursuant to Rule 10 of the Convention Refugee Determination Division Rules, all claims are being heard together.
- Evidence: `evidence_fact` cue `testimony` at chunk `4255411` offsets `37-46`; context: [12] The Board found the Applicants' testimony to be credible but reached the conclusion that state protection was available.
- Evidence: `counterargument_limitation` cue `but` at chunk `4255411` offsets `62-65`; context: [12] The Board found the Applicants' testimony to be credible but reached the conclusion that state protection was available.
- Evidence: `evidence_fact` cue `evidence` at chunk `4255412` offsets `164-172`; context: [13] The Board concluded that there is reasonable and adequate protection for the Principal Applicant in Argentina and placed significant weight on the documentary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4255413` offsets `94-102`; context: These claimants have not provided any persuasive evidence to show that they could not seek state protection in Argentina, that such protection would not be forthcoming, or that they have exhausted all remedies available to them in advance of seeking international protection.
- Evidence: `party_position` cue `argue` at chunk `4255414` offsets `20-25`; context: [15] The Applicants argue that the Board erred in its finding about the availability of state protection in Argentina and that the Board ignored relevant evidence in reaching its conclusion, thereby making a perverse finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4255414` offsets `154-162`; context: [15] The Applicants argue that the Board erred in its finding about the availability of state protection in Argentina and that the Board ignored relevant evidence in reaching its conclusion, thereby making a perverse finding.
- Evidence: `counterargument_limitation` cue `but` at chunk `4255414` offsets `403-406`; context: In particular, the Applicants argue that the Board relied on the fact that a law had been passed for the protection of women against domestic violence, in the state of Mendoza, but no steps had been taken to implement that law.
- Evidence: `party_position` cue `argue` at chunk `4255415` offsets `28-33`; context: [16] Second, the Applicants argue that the Board erroneously applied the wrong test in determining that state protection was available to her.
- Evidence: `reasoning_application` cue `applied` at chunk `4255415` offsets `61-68`; context: [16] Second, the Applicants argue that the Board erroneously applied the wrong test in determining that state protection was available to her.

#### 4538:1:subtheme:2 · paragraphs 17-18

- Raw key terms: `applicants, available, board, canada, considered, immigration, minister, protection`
- Display key terms: `available, considered, protection`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: available, considered, protection Position/evidence statements: [17] The Respondent submits that the Board properly dealt with the issue of state protection. Application context: [18] In my opinion, the Applicants have succeeded in demonstrating that the Board applied the wrong test in determining whether the state protection was available. Operative outcome context: The application for judicial review is allowed and the matter is remitted to a different panel of the C. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4255416` offsets `67-72`; context: [17] The Respondent submits that the Board properly dealt with the issue of state protection.
- Evidence: `party_position` cue `submits` at chunk `4255416` offsets `20-27`; context: [17] The Respondent submits that the Board properly dealt with the issue of state protection.
- Evidence: `issue` cue `whether` at chunk `4255417` offsets `120-127`; context: [18] In my opinion, the Applicants have succeeded in demonstrating that the Board applied the wrong test in determining whether the state protection was available.
- Evidence: `evidence_fact` cue `evidence` at chunk `4255417` offsets `718-726`; context: The words used by the panel and its references to the evidence suggest that it my have required the Applicant to exhaust absolutely all avenues of protection rather than taking all steps reasonable in the circumstances to seek protection in the country of origin.
- Evidence: `reasoning_application` cue `applied` at chunk `4255417` offsets `82-89`; context: [18] In my opinion, the Applicants have succeeded in demonstrating that the Board applied the wrong test in determining whether the state protection was available.
- Evidence: `disposition` cue `allowed` at chunk `4255417` offsets `1256-1263`; context: The application for judicial review is allowed and the matter is remitted to a different panel of the C.

#### 4538:1:subtheme:3 · paragraphs 19-20

- Raw key terms: `board, decision, application, aside, basis, consideration, consisted, differently`
- Display key terms: `aside, basis, consideration, consisted, differently`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: aside, basis, consideration, consisted, differently Rule/authority context: [19] In my opinion, application of the wrong legal test is a sufficient basis upon which to set aside the decision of the Board. Operative outcome context: [20] The decision of the Board is quashed and the matter is to be remitted to a differently consisted panel for consideration on the merits. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `legal test` at chunk `4255418` offsets `45-55`; context: [19] In my opinion, application of the wrong legal test is a sufficient basis upon which to set aside the decision of the Board.
- Evidence: `disposition` cue `quashed` at chunk `4255419` offsets `34-41`; context: [20] The decision of the Board is quashed and the matter is to be remitted to a differently consisted panel for consideration on the merits.

#### 4538:1:subtheme:4 · paragraphs 21-21

- Raw key terms: `application, arising, certified, general, importance, question`
- Display key terms: `arising, certified, importance, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: arising, certified, importance, question Evidence spans paragraphs 21-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4255420` offsets `18-26`; context: [21] There was no question of general importance arising from this application and no question will be certified.

#### Section text

Peralta v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2002-09-20
Neutral citation
2002 FCT 989
File numbers
IMM-5451-01
Decision Content
Date: 20020920
Docket: IMM-5451-01
Neutral citation: 2002 FCT 989
Toronto, Ontario, Friday, the 20th day of September, 2002
PRESENT: The Honourable Madam Justice Heneghan
BETWEEN:
GLORIA DEL CARMEN PERALTA
VALENTINA PERALTA
MARIA JIMENA CORREA PERALTA
(a.k.a. MARIA JIMENA CORREA)
Applicants
- and -
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER
Introduction

[1] Ms. Gloria Del Carmen Peralta ("Principal Applicant") is the mother of Valentina Peralta and Maria Jimena Correa Peralta (collectively, the"Applicants"). The Applicants seek judicial review pursuing to section 82.1(1) of the Immigration Act, R.S.C. 1985, c. I-2, as amended, of a decision of the Immigration and Refugee Board, Convention Refugee Determination Division ("Board"). In its decision dated November 7, 2001, the Board determined that the Applicants are not convention refugees.
Facts

[2] The Applicants are all citizens of Argentina. Valentina Peralta is the minor daughter of the Principal Applicant and her claim is joined with that of her mother. Maria Jimena Correa Peralta is an adult and advances her own claim. Pursuant to Rule 10 of the Convention Refugee Determination Division Rules, all claims are being heard together.

[3] The Principal Applicant bases her claim for Convention Refugee Status upon membership in a particular social group, that is an Argentine woman subject to domestic and sexual abuse. The adult daughter bases her claim upon family membership, and alleges a fear of persecution resulting from the actions of her mother's former boyfriend, Juan Luis Ramos.

[4] The Principal Applicant began to date Mr. Ramos in Mendoza, Argentina, in December of 1997. He subjected her to physical, verbal and sexual abuse. In June 1998, the Principal Applicant was so badly injured by him that she sought medical attention and reported the incident to the police. The police told her they did not get involved in family matters and advised her to be an obedient girlfriend.

[5] In July 1998, the Principal Applicant was subject to further physical abuse and rape at the hands of Mr. Ramos. She required treatment from a doctor and gynecologist. At this time, she also sought help from a women centre and received one hour counselling sessions. She sought legal assistance from a lawyer who offered mediation services. Mr. Ramos refused to participate. The lawyer advised the Principal Applicant that pursuit of legal action would be lengthy and possibly dangerous to her safety.

[6] In January of 1999, the Principal Applicant learned that she was pregnant. Her pregnancy enraged Mr. Ramos. The physical and verbal abuse continued.

[7] The Principal Applicant testified that Mr. Ramos would come to her place of employment. The police were often called and arrived on one occasion, but did not arrest Mr. Ramos.

[8] The Principal Applicant recounted another incident were she was badly battered by Mr. Ramos. She required transportation to the hospital by ambulance. She reported the incident to the police and later learned that, while her file had been sent to the prosecutor's office, no action was taken against Mr. Ramos.

[9] After the birth of Valentina, Mr. Ramos continued to beat the Principal Applicant. He raped her again and threatened the child in October 1999. As the result of a similar incident in April 2000, the Applicants fled to the home of a friend.

[10] Mr. Ramos discovered where the Principal Applicant was living and persisted in making threats against her, in her home and at her place of employment. The Principal Applicant fled Argentina with her minor daughter on July 30, 2000, staying in the United States of America for a period of four weeks before landing in Canada.

[11] The Applicant's adult daughter remained in Argentina until April 2001. She says that Mr. Ramos made threatening phone calls to her and followed her. In April 2001, the adult daughter came to Canada.

[12] The Board found the Applicants' testimony to be credible but reached the conclusion that state protection was available. It cited documentary evidence to the effect that Argentina is enacting laws aimed at protecting women in domestic abuse situations. At the same time, the Board noted that those laws were applicable only in certain areas of Argentina and did not carry any sanctions against the perpetrator of domestic violence.

[13] The Board concluded that there is reasonable and adequate protection for the Principal Applicant in Argentina and placed significant weight on the documentary evidence. It concluded that the Principal Applicant had not shown that the government of Argentina could not or would not protect her and determined that the Applicants' fear of persecution was not well founded.

[14] In particular, the Board concluded:
... These claimants have not provided any persuasive evidence to show that they could not seek state protection in Argentina, that such protection would not be forthcoming, or that they have exhausted all remedies available to them in advance of seeking international protection.
Applicants' Submissions

[15] The Applicants argue that the Board erred in its finding about the availability of state protection in Argentina and that the Board ignored relevant evidence in reaching its conclusion, thereby making a perverse finding. In particular, the Applicants argue that the Board relied on the fact that a law had been passed for the protection of women against domestic violence, in the state of Mendoza, but no steps had been taken to implement that law.

[16] Second, the Applicants argue that the Board erroneously applied the wrong test in determining that state protection was available to her. The Applicant said that the Board required her to show that she had exhausted all avenues of protection, before seeking the protection of another country, and that this is the wrong test in law.
Respondent's Submissions

[17] The Respondent submits that the Board properly dealt with the issue of state protection. Relying on the decision of this Court in Canada (Minister of Employment and Immigration) v. Villafranca (1992), 18 Imm. L.R. (2d) 130 (F.C.A), the Respondent argues that the home state, that is Argentina, is not required to provide perfect protection at all times to its citizens. The Respondent argues that the Board reasonably considered whether state protection was reasonably available to the Applicants and concluded that it was.
Analysis

[18] In my opinion, the Applicants have succeeded in demonstrating that the Board applied the wrong test in determining whether the state protection was available. According to its reasons, the Board required the Applicants to show that they had exhausted all avenues of protection. This test was found to be erroneous by Justice Rothstein in Jane Doe v. Canada (Minister of Citizenship and Immigration) (21 November 1996), action number IMM-1514-95 (F.C.T.D.). In that case, Justice Rothstein said as follows:
I am not satisfied that the panel of the C.R.D.D. applied the correct test in respect of the Applicant seeking the protection of the state in this case. The words used by the panel and its references to the evidence suggest that it my have required the Applicant to exhaust absolutely all avenues of protection rather than taking all steps reasonable in the circumstances to seek protection in the country of origin. In this case the seeking of protection had to be considered not only in the context of the country of origin in general but also with respect to all the steps the Applicant did take and the interaction the Applicant had with the authorities in the very unusual circumstances of this case. The application for judicial review is allowed and the matter is remitted to a different panel of the C.R.D.D. for redetermination only in respect of the matter of state protection.

[19] In my opinion, application of the wrong legal test is a sufficient basis upon which to set aside the decision of the Board.

[20] The decision of the Board is quashed and the matter is to be remitted to a differently consisted panel for consideration on the merits.

[21] There was no question of general importance arising from this application and no question will be certified.


## 4538:2 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cfe99815c8184e544e6fa3b0882e105cb8c2491ad6ed111039fc2bf10903e16e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4538:2:subtheme:1 · paragraphs 22-23

- Raw key terms: `canada, court, federal, heneghan, imm-5451-01, order, record, solicitors`
- Display key terms: `federal, heneghan, imm-5451-01, order, solicitors`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: federal, heneghan, imm-5451-01, order, solicitors No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
The application for judicial review is allowed and the matter remitted to a differently constituted panel for consideration.
No question will be certified.
"E. Heneghan"
J.F.C.C.
FEDERAL COURT OF CANADA
Names of Counsel and Solicitors of Record
COURT NO: IMM-5451-01

STYLE OF CAUSE: GLORIA DEL CARMEN PERALTA
VALENTINA PERALTA
MARIA JIMENA CORREA PERALTA
(a.k.a. MARIA JIMENA CORREA)
Applicants
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
DATE OF HEARING: WEDNESDAY, SEPTEMBER 18, 2002
PLACE OF HEARING: TORONTO, ONTARIO
REASONS FOR ORDER
AND ORDER BY: HENEGHAN J.
DATED: FRIDAY, SEPTEMBER 20, 2002
APPEARANCES: Mr. J. Byron Thomas
For the Applicants
Ms. Deborah Drukarsh
For the Respondent
SOLICITORS OF RECORD: Mr. J. Byron Thomas
5468 Dundas Street West
Suite 402
Toronto, Ontario
M9B 6E3
For the Applicants
Morris Rosenberg
Deputy Attorney General of Canada
For the Respondent
FEDERAL COURT OF CANADA
Date: 20020920
Docket: IMM-5451-01
BETWEEN:
GLORIA DEL CARMEN PERALTA
VALENTINA PERALTA
MARIA JIMENA CORREA PERALTA
(a.k.a. MARIA JIMENA CORREA)
Applicants
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
AND ORDER
