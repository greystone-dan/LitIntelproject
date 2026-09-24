# Discussion Units: case 16152

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **17**
- Continuity pairs: **16**
- Discussion Units: **2**
- Paragraph source hashes: **17**
- Sub-themes: **5**

## 16152:1 · paragraphs 0-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cb0f8c2c06f91d573392dcd9ba429f0e5466cf22d9001e59ad3fa990fca0fc21`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 16152:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, claims, canada, abuse, daughter, decision, immigration, mother`
- Display key terms: `claims, abuse, daughter, mother`
- Argument roles: `party_position, reasoning_application`
- Explanation: Observed roles: party_position, reasoning_application Display terms: claims, abuse, daughter, mother Position/evidence statements: As a result, she claims that following their departure to Canada, she became emotionally dependent on Jong Kook Cho. | [4] She claims that her husband was verbally and psychologically abusive towards her from the very beginning of their marriage. Application context: [5] The Applicant said that she told no one about the incidents because of her personal shame and because of the societal stigma attached to such claims. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4762375` offsets `87-93`; context: As a result, she claims that following their departure to Canada, she became emotionally dependent on Jong Kook Cho.
- Evidence: `party_position` cue `claims` at chunk `4762376` offsets `8-14`; context: [4] She claims that her husband was verbally and psychologically abusive towards her from the very beginning of their marriage.
- Evidence: `party_position` cue `claims` at chunk `4762377` offsets `146-152`; context: [5] The Applicant said that she told no one about the incidents because of her personal shame and because of the societal stigma attached to such claims.
- Evidence: `reasoning_application` cue `because` at chunk `4762377` offsets `64-71`; context: [5] The Applicant said that she told no one about the incidents because of her personal shame and because of the societal stigma attached to such claims.

#### 16152:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `abuse, applicant, protection, seek, state, accusing, argues, dependence`
- Display key terms: `abuse, protection, seek, state, accusing, argues, dependence`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: abuse, protection, seek, state, accusing, argues, dependence Position/evidence statements: [7] The Applicant argues that it was reasonable for her, given her particular situation, not to seek state protection. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUE` at chunk `4762378` offsets `135-140`; context: POINTS IN ISSUE
- Evidence: `party_position` cue `argues` at chunk `4762379` offsets `18-24`; context: [7] The Applicant argues that it was reasonable for her, given her particular situation, not to seek state protection.

#### 16152:1:subtheme:3 · paragraphs 8-13

- Raw key terms: `protection, state, applicant, basis, decision, effective, even, korea`
- Display key terms: `protection, state, basis, effective, even, korea`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: protection, state, basis, effective, even, korea Rule/authority context: [11] The standard of review on state protection is patent unreasonableness. Application context: [10] An Applicant's subjective reluctance to engage the state in providing protection is not a sufficient basis to conclude that state protection is not available or effective. | [13] Therefore, despite counsel's persuasive efforts, this Court can find no basis upon which to intervene in this decision. Evidence spans paragraphs 8-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4762380` offsets `63-70`; context: [8] The Applicant further says that the RPD failed to consider whether state protection was effective in Korea.
- Evidence: `reasoning_application` cue `conclude` at chunk `4762382` offsets `115-123`; context: [10] An Applicant's subjective reluctance to engage the state in providing protection is not a sufficient basis to conclude that state protection is not available or effective.
- Evidence: `governing_rule` cue `standard of review` at chunk `4762383` offsets `9-27`; context: [11] The standard of review on state protection is patent unreasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4762384` offsets `266-274`; context: It would be unreasonable to suggest that the RPD must conduct a full review of the effectiveness of state protection in Korea (even if that were possible) in the absence of significant evidence of its ineffectiveness.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4762385` offsets `5-14`; context: [13] Therefore, despite counsel's persuasive efforts, this Court can find no basis upon which to intervene in this decision.

#### 16152:1:subtheme:4 · paragraphs 14-15

- Raw key terms: `application, cause, certified, citizenship, counsel, court, date, dismissed`
- Display key terms: `certified, date, dismissed`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: certified, date, dismissed Operative outcome context: [14] This application for judicial review will be dismissed. Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4762386` offsets `64-72`; context: No question will be certified.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4762386` offsets `171-177`; context: Phelan"
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-8191-04
- Evidence: `disposition` cue `dismissed` at chunk `4762386` offsets `50-59`; context: [14] This application for judicial review will be dismissed.

#### Section text

Kim v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-08-17
Neutral citation
2005 FC 1126
File numbers
IMM-8191-04
Decision Content
Date: 20050817
Docket: IMM-8191-04
Citation: 2005 FC 1126
BETWEEN:
EUN MEE KIM and INN WOO CHO
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
PHELAN J.

[1] Ms. Eun Mee Kim (Applicant) was found not to be a refugee or a person in need of protection by the Refugee Protection Division (RPD) of the Immigration and Refugee Board (IRB). This is her judicial review of that decision.
BACKGROUND

[2] The Applicant, a female citizen of the Republic of Korea, who is joined in her claim by her 9 year old daughter Inn Woo Cho, bases her claim on spousal abuse. She claims that state protection is not available to her.

[3] The Applicant has a mother and her only sibling living in Canada. As a result, she claims that following their departure to Canada, she became emotionally dependent on Jong Kook Cho. They married in 1995.

[4] She claims that her husband was verbally and psychologically abusive towards her from the very beginning of their marriage. She was physically assaulted and threatened at various times with either a hammer or with a knife.

[5] The Applicant said that she told no one about the incidents because of her personal shame and because of the societal stigma attached to such claims. It was only in 2003, when her mother visited her, that the abuse came out in the open. Her mother took charge of the situation, obtained emotional counselling for the Applicant and moved her and her daughter to Canada.

[6] At no time between 1995 and 2003, despite the physical and psychological abuse, did the Applicant seek state protection.
POINTS IN ISSUE

[7] The Applicant argues that it was reasonable for her, given her particular situation, not to seek state protection. The Applicant says that the societal values and the shame of accusing a husband of abuse, her emotional dependence on her husband, and, her loneliness in Korea are all factors which make her failure to seek state protection reasonable.

[8] The Applicant further says that the RPD failed to consider whether state protection was effective in Korea. The Applicant says that the RPD's error was to consider whether organizational structures were in place to the exclusion of considering whether those structures functioned properly.
DETERMINATION

[9] The burden of establishing that state protection is either non-existent or inadequate rests with the Applicant. There is a presumption in favour of the existence of state protection. (See; Canada (Minister of Employment and Immigration) v. Ward (1993), 103 D.L.R.(4th)).

[10] An Applicant's subjective reluctance to engage the state in providing protection is not a sufficient basis to conclude that state protection is not available or effective. In this case, the Applicant never sought any aspect of state protection, even when her mother came to her physical and emotional aid.

[11] The standard of review on state protection is patent unreasonableness. The RPD took account of the state structure for the protection of abused women; it considered the U.S. DOS reports which referred to some problems in executing on the policies of increased protection for abused women.

[12] The RPD's decision, read as a whole, is a reasonable and balanced decision. It would be unreasonable to suggest that the RPD must conduct a full review of the effectiveness of state protection in Korea (even if that were possible) in the absence of significant evidence of its ineffectiveness. There is nothing to suggest that Korea's state protection is a sham or an exercise of "form over substance".

[13] Therefore, despite counsel's persuasive efforts, this Court can find no basis upon which to intervene in this decision.

[14] This application for judicial review will be dismissed. No question will be certified.
(s) "Michael L. Phelan"
Judge
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-8191-04

STYLE OF CAUSE: EUN MEE KIM and INN WOO CHO v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: July 27, 2005
REASONS FOR 

## 16152:2 · paragraphs 16-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ea1020de805573cf1842a8f41dadf24983d2c9100a369bae9dddf7318798db85`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 16152:2:subtheme:1 · paragraphs 16-16

- Raw key terms: `appearances, applicants, attorney, august, bellissimo, canada, dated, deputy`
- Display key terms: `august, bellissimo, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, bellissimo, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 16-16. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER: Phelan J.
DATED: August 17, 2005
APPEARANCES:
Mr. J. Norris Ormston FOR THE APPLICANTS
Ms. Sally Thomas FOR THE RESPONDENT
SOLICITORS ON THE RECORD:
Ormston, Bellissimo, Yousan
Toronto, Ontario FOR THE APPLICANTS
Mr. John H. Sims, Q.C.
Deputy Attorney General of Canada
Ottawa, Ontario FOR THE RESPONDENT
