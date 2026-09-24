# Discussion Units: case 1901

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **69**
- Continuity pairs: **68**
- Discussion Units: **7**
- Paragraph source hashes: **69**
- Sub-themes: **20**

## 1901:1 · paragraphs 0-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a5db8402198e01554199dd86478bbb4af14d10178208d009bf1aaf159adb0abe`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `applicant, husband, board, immigration, application, decision, ping, applied`
- Display key terms: `husband, ping, applied`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: husband, ping, applied Rule/authority context: [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: Her husband applied to immigrate to Canada in the entrepreneur category and included her as an accompanying spouse in his application. | [4] The applicant applied for Canadian citizenship in 2001. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4161601` offsets `47-58`; context: [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `applied` at chunk `4161603` offsets `254-261`; context: Her husband applied to immigrate to Canada in the entrepreneur category and included her as an accompanying spouse in his application.
- Evidence: `reasoning_application` cue `applied` at chunk `4161604` offsets `18-25`; context: [4] The applicant applied for Canadian citizenship in 2001.
- Evidence: `evidence_fact` cue `found that` at chunk `4161605` offsets `95-105`; context: [5] After an investigation was done and the applicant and her husband were interviewed, it was found that her husband had made a material misrepresentation by failing to disclose his relationship with Ping He, and failing to disclose his son at the time of his application for permanent residence in Canada.
- Evidence: `evidence_fact` cue `found that` at chunk `4161608` offsets `14-24`; context: [8] The Board found that on the balance of probabilities, the applicant's husband was legally married to Ping He at the time he applied for permanent residence.
- Evidence: `reasoning_application` cue `applied` at chunk `4161608` offsets `128-135`; context: [8] The Board found that on the balance of probabilities, the applicant's husband was legally married to Ping He at the time he applied for permanent residence.

#### 1901:1:subtheme:2 · paragraphs 9-10

- Raw key terms: `administration, applicant, board, dependant, error, fact, granted, huang`
- Display key terms: `administration, dependant, error, fact, granted, huang`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: administration, dependant, error, fact, granted, huang Rule/authority context: Under the former Immigration Act, allegations of misrepresentation were made under s. Application context: In that case a mother and son applied for admission as permanent residents to Canada. | More specifically, at the relevant time of landing, the now husband was still married to Ping He and therefore, the applicant was not a sponsorable dependant, and would not have been granted landing as a dependant. Operative outcome context: was granted landing by reason of . | More specifically, at the relevant time of landing, the now husband was still married to Ping He and therefore, the applicant was not a sponsorable dependant, and would not have been granted landing as a dependant. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4161609` offsets `581-588`; context: any fraudulent or improper means or misrepresentation of any material fact, whether exercised or made by himself or by any other person;
Under the present Act a person is inadmissible for:
.
- Evidence: `evidence_fact` cue `testimony` at chunk `4161609` offsets `1135-1144`; context: " In the absence of any oral testimony from Ms.
- Evidence: `governing_rule` cue `Under` at chunk `4161609` offsets `358-363`; context: Under the former Immigration Act, allegations of misrepresentation were made under s.
- Evidence: `reasoning_application` cue `applied` at chunk `4161609` offsets `2502-2509`; context: In that case a mother and son applied for admission as permanent residents to Canada.
- Evidence: `disposition` cue `granted` at chunk `4161609` offsets `470-477`; context: was granted landing by reason of .
- Evidence: `reasoning_application` cue `therefore` at chunk `4161610` offsets `381-390`; context: More specifically, at the relevant time of landing, the now husband was still married to Ping He and therefore, the applicant was not a sponsorable dependant, and would not have been granted landing as a dependant.
- Evidence: `disposition` cue `granted` at chunk `4161610` offsets `463-470`; context: More specifically, at the relevant time of landing, the now husband was still married to Ping He and therefore, the applicant was not a sponsorable dependant, and would not have been granted landing as a dependant.

#### 1901:1:subtheme:3 · paragraphs 11-13

- Raw key terms: `board, canada, appellant, family, found, husband, immigration, likely`
- Display key terms: `appellant, family, husband, likely`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: appellant, family, husband, likely Application context: [11] The Board therefore found the exclusion order to be valid in law, and then turned its mind to the question of discretionary relief as follows: Discretionary Relief The test to be applied in the exercise of discretio Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161611` offsets `103-111`; context: [11] The Board therefore found the exclusion order to be valid in law, and then turned its mind to the question of discretionary relief as follows:
Discretionary Relief
The test to be applied in the exercise of discretionary jurisdiction is:"the Immigration Appeal Division must be satisfied that, at the time that the appeal is disposed of .
- Evidence: `reasoning_application` cue `therefore` at chunk `4161611` offsets `15-24`; context: [11] The Board therefore found the exclusion order to be valid in law, and then turned its mind to the question of discretionary relief as follows:
Discretionary Relief
The test to be applied in the exercise of discretionary jurisdiction is:"the Immigration Appeal Division must be satisfied that, at the time that the appeal is disposed of .
- Evidence: `issue` cue `whether` at chunk `4161612` offsets `222-229`; context: [12] The Board noted that while it accepted the applicant's testimony that she may not have been told about the previous marriage and son, it appeared that neither she nor her husband had taken reasonable steps to confirm whether the husband was legally married to Ping He, and instead maintained their position that he was not legally married to her.
- Evidence: `evidence_fact` cue `testimony` at chunk `4161612` offsets `60-69`; context: [12] The Board noted that while it accepted the applicant's testimony that she may not have been told about the previous marriage and son, it appeared that neither she nor her husband had taken reasonable steps to confirm whether the husband was legally married to Ping He, and instead maintained their position that he was not legally married to her.
- Evidence: `counterargument_limitation` cue `however` at chunk `4161612` offsets `361-368`; context: They did however, subsequently obtain a divorce certificate in relation to his marriage with Ping He, and they then remarried in Canada.
- Evidence: `evidence_fact` cue `found that` at chunk `4161613` offsets `15-25`; context: [13] The Board found that those misrepresentations were very serious as they related to marital status and family composition and would have had a direct bearing on the acceptance of the applications and the approvals for landing in Canada.

#### 1901:1:subtheme:4 · paragraphs 14-23

- Raw key terms: `board, canada, applicant, daughter, found, husband, noted, child`
- Display key terms: `daughter, husband, noted, child`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: daughter, husband, noted, child Position/evidence statements: [22] The Board noted that the minor child was born in Canada and was five-years old, she was involved in many activities (including swimming, gymnastics, ballet, church activities), she was recently accepted into a priva Application context: Accordingly, there would be no impact to any family in Canada if the applicant and her husband were removed. Evidence spans paragraphs 14-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4161614` offsets `423-430`; context: The Board found that the applicant expressed genuine regret for what had happened and what might be the consequences if she is removed from Canada, but did not take reasonable steps to clarify whether or not her husband was legally married to Ping He, instead continuing to maintain they were not legally married.
- Evidence: `evidence_fact` cue `found that` at chunk `4161614` offsets `240-250`; context: The Board found that the applicant expressed genuine regret for what had happened and what might be the consequences if she is removed from Canada, but did not take reasonable steps to clarify whether or not her husband was legally married to Ping He, instead continuing to maintain they were not legally married.
- Evidence: `evidence_fact` cue `evidence` at chunk `4161615` offsets `104-112`; context: Based in part, upon evidence by witnesses, the Board did not accept that their Canadian businesses had in any way been affected by the removal proceedings, or that they would require the husband's presence in Canada in the near future.
- Evidence: `evidence_fact` cue `found that` at chunk `4161616` offsets `15-25`; context: [16] The Board found that the applicant had demonstrated establishment in Canada as evidenced by her long-term residency in Canada (eight years), she has taken courses in English, has recently re-entered the workforce, raised their daughter in Canada, has been actively involved in her church, volunteers in the community and has taken the initiative to improve her skills and qualifications.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4161617` offsets `132-143`; context: Accordingly, there would be no impact to any family in Canada if the applicant and her husband were removed.
- Evidence: `counterargument_limitation` cue `However` at chunk `4161618` offsets `174-181`; context: However, the husband has not developed connections in Canada with the exception of two or three business associates, and only occasionally participates with the applicant and their child in community or church activities when he is in Canada.
- Evidence: `evidence_fact` cue `found that` at chunk `4161619` offsets `15-25`; context: [19] The Board found that there was little evidence that the applicant's husband would suffer any hardship if removed from Canada, and that his concern was simply for the applicant and their daughter to remain in Canada.
- Evidence: `evidence_fact` cue `testimony` at chunk `4161620` offsets `37-46`; context: [20] The Board noted the applicant's testimony that she would suffer significant hardship if she was removed from Canada as she had a strong desire to live in Canada, she would not be able to work in China due to her age, that she would have trouble communicating effectively with her in-laws due to language difficulties, and there would be significant hardship for her daughter due to limited opportunities for education and other activities in China.
- Evidence: `counterargument_limitation` cue `however` at chunk `4161620` offsets `470-477`; context: The Board found however, that there was no evidence of adverse country conditions in China.
- Evidence: `evidence_fact` cue `found that` at chunk `4161621` offsets `202-212`; context: The Board found that the circumstances of the case did not support the objective of, or achievement of, family reunification.
- Evidence: `party_position` cue `claimed` at chunk `4161622` offsets `378-385`; context: [22] The Board noted that the minor child was born in Canada and was five-years old, she was involved in many activities (including swimming, gymnastics, ballet, church activities), she was recently accepted into a private school for kindergarten, she has been living with one parent in Canada most of her life, she did not like China when she visited it, and the applicant had claimed that the daughter would not have comparable opportunities for education and other activities in China.
- Evidence: `evidence_fact` cue `evidence` at chunk `4161622` offsets `540-548`; context: The Board held however, that there was no credible evidence to support those claims.
- Evidence: `counterargument_limitation` cue `however` at chunk `4161622` offsets `504-511`; context: The Board held however, that there was no credible evidence to support those claims.
- Evidence: `evidence_fact` cue `found that` at chunk `4161623` offsets `15-25`; context: [23] The Board found that as a Canadian citizen, the minor child had the right to stay in Canada, but it was likely she would return with her parents to China.
- Evidence: `counterargument_limitation` cue `but` at chunk `4161623` offsets `98-101`; context: [23] The Board found that as a Canadian citizen, the minor child had the right to stay in Canada, but it was likely she would return with her parents to China.

#### 1901:1:subtheme:5 · paragraphs 24-25

- Raw key terms: `board, compassionate, humanitarian, appeals, applicant, applicant's, based, capricious`
- Display key terms: `compassionate, humanitarian, appeals, applicant's, based, capricious`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: compassionate, humanitarian, appeals, applicant's, based, capricious Operative outcome context: [24] The Board determined that there were insufficient humanitarian and compassionate grounds that warranted special relief, and dismissed the appeals. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4161624` offsets `152-158`; context: Issues
- Evidence: `evidence_fact` cue `determined that` at chunk `4161624` offsets `15-30`; context: [24] The Board determined that there were insufficient humanitarian and compassionate grounds that warranted special relief, and dismissed the appeals.
- Evidence: `disposition` cue `dismissed` at chunk `4161624` offsets `129-138`; context: [24] The Board determined that there were insufficient humanitarian and compassionate grounds that warranted special relief, and dismissed the appeals.

#### 1901:1:subtheme:6 · paragraphs 26-30

- Raw key terms: `applicant, submitted, made, person, words, another, application, case`
- Display key terms: `submitted, made, person, words, another, case`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: submitted, made, person, words, another, case Position/evidence statements: [26] The applicant submitted that consideration of the meaning of the word "indirectly" should be interpreted in light of the forms prescribed by the regulations. | [27] The applicant submitted that therefore, an indirect misrepresentation would be a representation initiated by her, but made by someone else in relation to her application, not her husband's. Application context: [27] The applicant submitted that therefore, an indirect misrepresentation would be a representation initiated by her, but made by someone else in relation to her application, not her husband's. | The Board, in this case, should therefore not be adding words to the statute to interpret the word "indirectly" to include unknowing dependants in the misrepresentations of the principal applicant, when Parliament expres Evidence spans paragraphs 26-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161626` offsets `277-285`; context: The only representations the applicant made are contained in her application form which does not contain a single question regarding her husband, not even his name.
- Evidence: `party_position` cue `submitted` at chunk `4161626` offsets `19-28`; context: [26] The applicant submitted that consideration of the meaning of the word "indirectly" should be interpreted in light of the forms prescribed by the regulations.
- Evidence: `party_position` cue `submitted` at chunk `4161627` offsets `19-28`; context: [27] The applicant submitted that therefore, an indirect misrepresentation would be a representation initiated by her, but made by someone else in relation to her application, not her husband's.
- Evidence: `reasoning_application` cue `therefore` at chunk `4161627` offsets `34-43`; context: [27] The applicant submitted that therefore, an indirect misrepresentation would be a representation initiated by her, but made by someone else in relation to her application, not her husband's.
- Evidence: `party_position` cue `submitted` at chunk `4161628` offsets `19-28`; context: [28] The applicant submitted that if the legislators intended to exclude the applicant due to a misrepresentation made by another applicant, then the legislation ought to state that, as it did in the Immigration Act, supra.
- Evidence: `party_position` cue `submitted` at chunk `4161629` offsets `19-28`; context: [29] The applicant submitted that the Courts have taken the position that the addition of words to legislation is a matter for Parliament (see R.
- Evidence: `reasoning_application` cue `therefore` at chunk `4161629` offsets `212-221`; context: The Board, in this case, should therefore not be adding words to the statute to interpret the word "indirectly" to include unknowing dependants in the misrepresentations of the principal applicant, when Parliament expressly removed that provision in the new legislation.
- Evidence: `party_position` cue `submitted` at chunk `4161630` offsets `19-28`; context: [30] The applicant submitted that the Court has held that for a person to fall within the ambit of paragraph 27(1)(e), they must have a subjective knowledge of the facts being concealed (see Mugesera v.

#### 1901:1:subtheme:7 · paragraphs 31-32

- Raw key terms: `applicant, board, husband, husband's, accepted, accordingly, actions, allowing`
- Display key terms: `husband, husband's, accepted, accordingly, actions, allowing`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: husband, husband's, accepted, accordingly, actions, allowing Position/evidence statements: [32] The applicant submitted that the Board erred in failing to consider the possibility of allowing the appeal by the applicant while dismissing the appeal by the husband. Rule/authority context: [31] Accordingly, as the Board accepted that the applicant may not have known about her husband's previous relationship or his son, she should not have been found inadmissible pursuant to paragraph 40 (1)(a) of IRPA. Application context: [31] Accordingly, as the Board accepted that the applicant may not have known about her husband's previous relationship or his son, she should not have been found inadmissible pursuant to paragraph 40 (1)(a) of IRPA. Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4161631` offsets `176-187`; context: [31] Accordingly, as the Board accepted that the applicant may not have known about her husband's previous relationship or his son, she should not have been found inadmissible pursuant to paragraph 40 (1)(a) of IRPA.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4161631` offsets `5-16`; context: [31] Accordingly, as the Board accepted that the applicant may not have known about her husband's previous relationship or his son, she should not have been found inadmissible pursuant to paragraph 40 (1)(a) of IRPA.
- Evidence: `party_position` cue `submitted` at chunk `4161632` offsets `19-28`; context: [32] The applicant submitted that the Board erred in failing to consider the possibility of allowing the appeal by the applicant while dismissing the appeal by the husband.

#### 1901:1:subtheme:8 · paragraphs 33-41

- Raw key terms: `board, canada, applicant, child, submitted, canadian, erred, misrepresentation`
- Display key terms: `child, submitted, canadian, erred, misrepresentation`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: child, submitted, canadian, erred, misrepresentation Position/evidence statements: The applicant further submitted that it was unreasonable for the Board to have expected the applicant to have done anything to confirm the husband's alleged first marriage when she was not a party to it and would likely  | [34] The applicant submitted that the Board erred in finding that family reunification in this case would be better facilitated if both parents and the child lived together in the same country. Application context: [39] Accordingly, even if the misrepresentation provisions of IRPA were to apply to the applicant, the breach would be insufficient to warrant the removal of someone firmly established in Canada. | [40] The respondent submitted that the interpretation of subsection 40(1) that was applied by the Board is consistent with the modern approach to statutory interpretation articulated by the Supreme Court of Canada in Re  Evidence spans paragraphs 33-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4161633` offsets `90-96`; context: [33] The Board erred by treating the applicant and her husband as a single entity even on issues that had nothing to do with the applicant.
- Evidence: `party_position` cue `submitted` at chunk `4161633` offsets `162-171`; context: The applicant further submitted that it was unreasonable for the Board to have expected the applicant to have done anything to confirm the husband's alleged first marriage when she was not a party to it and would likely not have been given the information.
- Evidence: `party_position` cue `submitted` at chunk `4161634` offsets `19-28`; context: [34] The applicant submitted that the Board erred in finding that family reunification in this case would be better facilitated if both parents and the child lived together in the same country.
- Evidence: `party_position` cue `submitted` at chunk `4161638` offsets `19-28`; context: [38] The applicant submitted that the Board erred in concluding that the "negative factors outweigh those in favour of the appellants.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4161639` offsets `5-16`; context: [39] Accordingly, even if the misrepresentation provisions of IRPA were to apply to the applicant, the breach would be insufficient to warrant the removal of someone firmly established in Canada.
- Evidence: `party_position` cue `submitted` at chunk `4161640` offsets `20-29`; context: [40] The respondent submitted that the interpretation of subsection 40(1) that was applied by the Board is consistent with the modern approach to statutory interpretation articulated by the Supreme Court of Canada in Re Rizzo and Rizzo Shoes [1998] 1 S.
- Evidence: `reasoning_application` cue `applied` at chunk `4161640` offsets `83-90`; context: [40] The respondent submitted that the interpretation of subsection 40(1) that was applied by the Board is consistent with the modern approach to statutory interpretation articulated by the Supreme Court of Canada in Re Rizzo and Rizzo Shoes [1998] 1 S.
- Evidence: `party_position` cue `submitted` at chunk `4161641` offsets `20-29`; context: [41] The respondent submitted that if the applicant's argument is accepted and she was not found to have "indirectly misrepresented" through her husband's misrepresentation, she would be able to remain in Canada and then sponsor her husband back to Canada.

#### 1901:1:subtheme:9 · paragraphs 42-42

- Raw key terms: `applicant, clearly, exercised, fact, former, found, himself, immigration`
- Display key terms: `clearly, exercised, fact, former, himself`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: clearly, exercised, fact, former, himself Position/evidence statements: [42] The respondent submitted that the purpose of section 40 can be seen through a look at the relevant provisions of the former Immigration Act, R. Rule/authority context: The applicant would clearly have been found to be inadmissible under paragraph 27(1)(e) of the former Act, which referred to misrepresentation of any material fact whether exercised by himself or by any other person. Evidence spans paragraphs 42-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4161642` offsets `331-338`; context: The applicant would clearly have been found to be inadmissible under paragraph 27(1)(e) of the former Act, which referred to misrepresentation of any material fact whether exercised by himself or by any other person.
- Evidence: `party_position` cue `submitted` at chunk `4161642` offsets `20-29`; context: [42] The respondent submitted that the purpose of section 40 can be seen through a look at the relevant provisions of the former Immigration Act, R.
- Evidence: `governing_rule` cue `under` at chunk `4161642` offsets `230-235`; context: The applicant would clearly have been found to be inadmissible under paragraph 27(1)(e) of the former Act, which referred to misrepresentation of any material fact whether exercised by himself or by any other person.

#### Section text

Wang v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-08-03
Neutral citation
2005 FC 1059
File numbers
IMM-5815-04
Notes
Digest
Decision Content
Date: 20050803
Docket: IMM-5815-04
Citation: 2005 FC 1059
Toronto, Ontario, August 3, 2005
PRESENT: THE HONOURABLE MR. JUSTICE JOHN A. O'KEEFE
BETWEEN:
XIAO QIONG WANG
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 ("IRPA"), of a decision of the Immigration Appeal Division of the Immigration and Refugee Board (the "Board"), dated June 1, 2004, (i) upholding the validity of the exclusion order made against the applicant based on indirect misrepresentation, and (ii) determining that there were insufficient humanitarian and compassionate ("H & C") considerations to warrant special relief.

[2] The applicant requested that the decision of the Board dated June 1, 2004 be set aside and a new hearing be directed to be held by a different member.
Background

[3] The applicant, Xiao Qiong Wang (the "applicant") is a citizen of China and was a permanent resident of Canada. The applicant married Ying Jun Huang (her "husband") on July 12, 1990. The applicant came to Canada on a student visa in 1996. Her husband applied to immigrate to Canada in the entrepreneur category and included her as an accompanying spouse in his application. They were landed on September 10, 1998. The applicant gave birth to a Canadian born daughter on March 2, 1999.

[4] The applicant applied for Canadian citizenship in 2001. She and her husband were requested to attend an interview with Citizenship and Immigration ("CIC") and to bring any documents related to previous marriages. The applicant alleged that this was the first time her husband had told her about his previous relationship with a woman named Ping He before he met the applicant and that they had a son.

[5] After an investigation was done and the applicant and her husband were interviewed, it was found that her husband had made a material misrepresentation by failing to disclose his relationship with Ping He, and failing to disclose his son at the time of his application for permanent residence in Canada.

[6] The applicant and her husband were the subject of an admissibility hearing at the Immigration Division of the Board where an exclusion order was issued by a Board Member against the applicant's husband for directly misrepresenting a material fact. An exclusion order was also issued against the applicant on the basis of indirectly misrepresenting a material fact due to being an accompanying spouse on her husband's application.

[7] The decision was appealed to the Immigration Appeal Division. Both the applicant and her husband testified that the applicant had no knowledge of her husband's previous relationship with Ping He, or about his son, until she received the letter from CIC.
Reasons of the Board
Husband's Inadmissibility

[8] The Board found that on the balance of probabilities, the applicant's husband was legally married to Ping He at the time he applied for permanent residence. The Board found the husband's evidence that he had not in fact married Ping He to not be credible.
Applicant's Inadmissibility

[9] The Board adopted the Immigration Division's analysis and conclusion that the applicant was inadmissible on the basis of indirect misrepresentations.
Between the former Immigration Act and the present Immigration and Refugee Protection Act, there was a change in the language used to 'catch' dependents in the misrepresentations of principal applicants. Under the former Immigration Act, allegations of misrepresentation were made under s. 27(1)(e): . . .
. . . was granted landing by reason of . . . any fraudulent or improper means or misrepresentation of any material fact, whether exercised or made by himself or by any other person;
Under the present Act a person is inadmissible for:
. . . directly or indirectly misrepresenting or withholding materials facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
Under the former Act a dependent would be removable from Canada for having been granted landing by reason of the misrepresentation of the principal applicant - a misrepresentation "exercised or made by himself or by any other person." In the absence of any oral testimony from Ms. Wang there was no evidence whether she knew a) that Mr. Huang was married to Ping He b) that he was likely not free marry to her in 1990 c) that he did not divorce Ping He until 2000, and d) that Mr. Huang has had a child with Ping He. Nonetheless under the former Act knowledge of the misrepresentation by the dependent was unnecessary in order to find the person described. In Mohammed v. MCI [1997] 3 F.C. 299 (T.D.) Mr. Justice MacKay for the Federal Court said:
To interpret "misrepresentation" in paragraph 27(1)(e) as being restricted to wilful or intentional misrepresentation, of which the applicant must be subjectively aware, would limit the final phrase of the provision so that a misrepresentation committed by a person other than the applicant of which the applicant was unaware would not be held to constitute a misrepresentation under paragraph 27(1)(e) of the Act.
In my opinion, the interpretation advanced by counsel for the applicant renders paragraph 27(1)(e) not only inconsistent, but reads into it a requirement of mens rea or wrongful intent which is simply not supported by the plain language of the provision. Nor, in my view, is such an interpretation supported by the jurisprudence of this Court, exemplified by D'Souza v. Minister of Employment and Immigration. [1983] 1 F.C. 343 (C.A.).
In that case a mother and son applied for admission as permanent residents to Canada. The son, as his mother's dependant, made his own application, in which there were no errors. His mother's application, however, contained misrepresentation of a material fact about him, of which he was not aware. The principal argument on behalf of the applicant was that because he did not make, and was unaware that his mother had made, a misrepresentation, paragraph 27(1)(e) of the Act [S.C. 1976-77, c. 52] did not apply to him. Indeed, it was urged that given the severe consequences of deportation resulting from finding him to be a person under paragraph 27(1)(e), the provision should be read as inapplicable where, at the time of being granted entry, the applicant was subjectively unaware a misrepresentation had been made. This argument was dismissed by the Federal Court of Appeal, which held that although the evidence may suggest the applicant was truly unaware of the misrepresentation, the interpretation of paragraph 27(1)(e) as requiring an element of subjective knowledge was simply not supported by the language of the provision. On this point, Thurlow C.J., writing for the Court stated as follows:
But be that as it may, to adopt the proposed construction of the statute would, in my opinion, require the addition of words limiting its application to situations where the person concerned had knowledge of the making of the statement. I do not think the Court can supply or insert such wording. If the statute is to be so limited it is, in my opinion a matter for Parliament. The submission therefore fails.
Under the current legislation there is no longer a reference to a misrepresentation by any other person. The new language is "directly or indirectly". In my opinion it is not immediately apparent by this language that "indirectly" means a misrepresentation by another person. Nonetheless I can find no other logical interpretation. If "indirectly"were not to include misrepresentations by principal applicants on behalf of dependents, dependents would not be removable from Canada along with the principal applicant through whose auspices they achieved landing. This could lead to the division of families or to the abandonment of dependents in Canada. It could lead to unacceptable situations where a dependent spouse has to sponsor back to Canada the principal applicant who had been removed. Principal applicants could take advantage of such a lacuna to bring persons to Canada through misrepresentation who would not then be removable. Furthermore I cannot conclude that it was the intention of Parliament with the new legislation to eliminate dependents being caught by the misrepresentations of principal applicants. The language of the new legislation may not be obvious but a reasonable interpretation leads to this conclusion.

[10] The Board then stated that despite being allegedly unaware of the misrepresentation by her husband, the applicant indirectly misrepresented that she was the spouse of Mr. Huang, a material fact that did induce or could have induced an error in the administration of the Act. More specifically, at the relevant time of landing, the now husband was still married to Ping He and therefore, the applicant was not a sponsorable dependant, and would not have been granted landing as a dependant.

[11] The Board therefore found the exclusion order to be valid in law, and then turned its mind to the question of discretionary relief as follows:
Discretionary Relief
The test to be applied in the exercise of discretionary jurisdiction is:"the Immigration Appeal Division must be satisfied that, at the time that the appeal is disposed of . . . taking into account the best interests of a child directly affected by the decision, sufficient humanitarian and compassionate considerations warrant special relief in light of all the circumstances of the case".
. . . I regard the following factors to be the appropriate considerations in the exercise of discretionary jurisdiction in the context of an appeal based on misrepresentation. The factors are . . .:
_ the seriousness of the misrepresentation leading to the removal order and the circumstances surrounding it;
_ the remorsefulness of the appellant;
_ the length of time spent in Canada and the degree to which the appellant is established in Canada;
_ the appellant's family in Canada and the impact on the family that removal would cause;
_ the best interests of a child directly affected by the decision;
_ the support available to the appellant in the family and the community; and
_ the degree of hardship that would be caused by the appellant by removal from Canada, including the conditions in the likely country of removal
The exercise of discretion must also be consistent with the objectives of the Act, one of which is set out in section 3(1)(h), which recognizes the need to protect the health and safety of Canadians and to maintain the security of Canadian society. This objective includes the maintenance of the integrity of the immigration system in the face of misrepresentations made by potential immigrants.
The seriousness of the misrepresentation leading to a removal order and the circumstances surrounding it

[12] The Board noted that while it accepted the applicant's testimony that she may not have been told about the previous marriage and son, it appeared that neither she nor her husband had taken reasonable steps to confirm whether the husband was legally married to Ping He, and instead maintained their position that he was not legally married to her. They did however, subsequently obtain a divorce certificate in relation to his marriage with Ping He, and they then remarried in Canada. Further, her husband has maintained contact with and provided support for his son, both before and after immigrating to Canada. However, the son was not disclosed in any documents related to their immigration or otherwise disclosed to immigration officials.

[13] The Board found that those misrepresentations were very serious as they related to marital status and family composition and would have had a direct bearing on the acceptance of the applications and the approvals for landing in Canada. Even though the applicant herself had not made any misrepresentations, she would likely not have qualified to be landed in Canada as the spouse of her now husband. The Board determined that this was a negative factor to which it attached significant weight.
The remorsefulness of the appellant

[14] The Board noted that the applicant's husband had not expressed genuine remorse for his actions in relation to the misrepresentations, although he did express remorse for the consequences of his actions on his wife and child. The Board found that the applicant expressed genuine regret for what had happened and what might be the consequences if she is removed from Canada, but did not take reasonable steps to clarify whether or not her husband was legally married to Ping He, instead continuing to maintain they were not legally married. The Board viewed this as another negative factor weighing against the applicant and her husband.
The length of time spent in Canada and the degree to which the appellant is established in Canada

[15] The Board noted that the husband had not spent much time in Canada since 1998. Based in part, upon evidence by witnesses, the Board did not accept that their Canadian businesses had in any way been affected by the removal proceedings, or that they would require the husband's presence in Canada in the near future. The husband visited the applicant and minor child on special occasions three to five times per year. The Board found that the husband had not taken steps to become established in Canada.

[16] The Board found that the applicant had demonstrated establishment in Canada as evidenced by her long-term residency in Canada (eight years), she has taken courses in English, has recently re-entered the workforce, raised their daughter in Canada, has been actively involved in her church, volunteers in the community and has taken the initiative to improve her skills and qualifications.
The applicant's family in Canada and the impact on the family that the removal would cause

[17] The Board noted that other than their daughter, neither the applicant nor her husband had any family members living in Canada. Accordingly, there would be no impact to any family in Canada if the applicant and her husband were removed.
The support available to the applicant in the family and the community

[18] The Board noted that the applicant and her daughter actively participate in the community and their church and have a number of friends and a support network in Canada. However, the husband has not developed connections in Canada with the exception of two or three business associates, and only occasionally participates with the applicant and their child in community or church activities when he is in Canada.
The degree of hardship that would be caused to the applicant by removal from Canada, including the conditions in the likely country of removal

[19] The Board found that there was little evidence that the applicant's husband would suffer any hardship if removed from Canada, and that his concern was simply for the applicant and their daughter to remain in Canada.

[20] The Board noted the applicant's testimony that she would suffer significant hardship if she was removed from Canada as she had a strong desire to live in Canada, she would not be able to work in China due to her age, that she would have trouble communicating effectively with her in-laws due to language difficulties, and there would be significant hardship for her daughter due to limited opportunities for education and other activities in China. The Board found however, that there was no evidence of adverse country conditions in China. Further, the applicant and her husband lived in China for most of their lives without any apparent difficulties, she was well educated and was employed when she left China, she acquired additional skills and experience during her time in Canada, all of the close family members are in China so she will have family support there, and there is no credible evidence that she would not have employment opportunities or be able to pursue her involvement with her religion or singing in China.

[21] The Board noted counsel for the applicant's submissions that IRPA's objective of family reunification would best be served by allowing the applicant and her daughter to remain in Canada. The Board found that the circumstances of the case did not support the objective of, or achievement of, family reunification. Further, in light of the husband's intention to remain predominantly outside of Canada (in China), and visit the applicant and their daughter only occasionally, in the circumstances of this case, family reunification would be better facilitated by the family living in China.
The best interests of a child directly affected by the decision

[22] The Board noted that the minor child was born in Canada and was five-years old, she was involved in many activities (including swimming, gymnastics, ballet, church activities), she was recently accepted into a private school for kindergarten, she has been living with one parent in Canada most of her life, she did not like China when she visited it, and the applicant had claimed that the daughter would not have comparable opportunities for education and other activities in China. The Board held however, that there was no credible evidence to support those claims. Both the applicant and her husband had educational opportunities in China. The applicant was a professional opera singer and her husband was an accomplished pianist and both received their training in China. They have the financial resources to provide for private schooling and other activities for their daughter.

[23] The Board found that as a Canadian citizen, the minor child had the right to stay in Canada, but it was likely she would return with her parents to China. Given her young age and family circumstances, she would be able to adapt to life in China. While there would likely be an adjustment period, she is able to speak Mandarin, and would have the support of relatives in China. Further, given the specific circumstances of her parents, it would be in her best interest for her family unit to live together in China.

[24] The Board determined that there were insufficient humanitarian and compassionate grounds that warranted special relief, and dismissed the appeals.
Issues

[25] 1. Did the Board err in holding the applicant had indirectly misrepresented herself?
2. Was the member's refusal to find sufficient humanitarian and compassionate factors based on erroneous findings of fact made in a perverse and capricious manner?
Applicant's Submissions

[26] The applicant submitted that consideration of the meaning of the word "indirectly" should be interpreted in light of the forms prescribed by the regulations. The only representations the applicant made are contained in her application form which does not contain a single question regarding her husband, not even his name. There is nothing in the officially prescribed forms to indicate that she is, or will be held to be, responsible for misrepresentations made by another applicant.

[27] The applicant submitted that therefore, an indirect misrepresentation would be a representation initiated by her, but made by someone else in relation to her application, not her husband's. In other words, to be an indirect misrepresentation made by the applicant, it would have to be shown that there was information made in relation to her application by some other person that amounts to a misrepresentation of her information.

[28] The applicant submitted that if the legislators intended to exclude the applicant due to a misrepresentation made by another applicant, then the legislation ought to state that, as it did in the Immigration Act, supra. The repealed Act used the specific words "made by himself or by any other person".

[29] 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 1901:2 · paragraphs 43-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b90c00d53f0a9bef61b6cd976354611e1c58375939aabe4044a5e642f4429ea4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:2:subtheme:1 · paragraphs 43-45

- Raw key terms: `irpa, absurdity, amount, analysis, applicant, applicant's, assertions, aware`
- Display key terms: `irpa, absurdity, amount, analysis, applicant's, assertions, aware`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: irpa, absurdity, amount, analysis, applicant's, assertions, aware Position/evidence statements: [45] The respondent submitted that contrary to the applicant's assertions, the Board was at all times aware of the difference between her circumstances and her husband's circumstances, including (i) the applicant herself Rule/authority context: [44] It would therefore lead to an absurdity if a person who would clearly be inadmissible under the Immigration Act would no longer be inadmissible under IRPA. Application context: [44] It would therefore lead to an absurdity if a person who would clearly be inadmissible under the Immigration Act would no longer be inadmissible under IRPA. Evidence spans paragraphs 43-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4161644` offsets `91-96`; context: [44] It would therefore lead to an absurdity if a person who would clearly be inadmissible under the Immigration Act would no longer be inadmissible under IRPA.
- Evidence: `reasoning_application` cue `therefore` at chunk `4161644` offsets `14-23`; context: [44] It would therefore lead to an absurdity if a person who would clearly be inadmissible under the Immigration Act would no longer be inadmissible under IRPA.
- Evidence: `party_position` cue `submitted` at chunk `4161645` offsets `20-29`; context: [45] The respondent submitted that contrary to the applicant's assertions, the Board was at all times aware of the difference between her circumstances and her husband's circumstances, including (i) the applicant herself did not make any misrepresentations; (ii) unlike her husband, she expressed genuine remorse; and (iii) unlike her husband, the applicant had spent a significant amount of time in Canada and had demonstrated establishment in Canada.

#### 1901:2:subtheme:2 · paragraphs 46-48

- Raw key terms: `minister, misrepresentation, canada, citizenship, clarations, court, dans, faire`
- Display key terms: `misrepresentation, clarations, dans, faire`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: misrepresentation, clarations, dans, faire Position/evidence statements: For example, the applicant argued that the Board placed "undue emphasis" on the misrepresentation. Rule/authority context: (1) A permanent resident or a foreign national is inadmissible for misrepresentation (a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce Application context: (2) The following provisions govern subsection (1): (a) the permanent resident or the foreign national continues to be inadmissible for misrepresentation for a period of two years following, in the case of a determinatio Operative outcome context: (e) was granted landing by reason of possession of a false or improperly obtained passport, visa or other document pertaining to his admission or by reason of any fraudulent or improper means or misrepresentation of any  Evidence spans paragraphs 46-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161646` offsets `263-271`; context: The question of weight of evidence is not properly the subject of judicial review (see Suresh v.
- Evidence: `party_position` cue `argued` at chunk `4161646` offsets `187-193`; context: For example, the applicant argued that the Board placed "undue emphasis" on the misrepresentation.
- Evidence: `evidence_fact` cue `evidence` at chunk `4161646` offsets `285-293`; context: The question of weight of evidence is not properly the subject of judicial review (see Suresh v.
- Evidence: `issue` cue `whether` at chunk `4161647` offsets `564-571`; context: (e) was granted landing by reason of possession of a false or improperly obtained passport, visa or other document pertaining to his admission or by reason of any fraudulent or improper means or misrepresentation of any material fact, whether exercised or made by himself or by any other person;
27(1) L'agent d'immigration ou l'agent de la paix doit faire part au sous-ministre, dans un rapport écrit et circonstancié, de renseignements concernant un résident permanent et indiquant que celui-ci, selon le cas:
.
- Evidence: `disposition` cue `granted` at chunk `4161647` offsets `337-344`; context: (e) was granted landing by reason of possession of a false or improperly obtained passport, visa or other document pertaining to his admission or by reason of any fraudulent or improper means or misrepresentation of any material fact, whether exercised or made by himself or by any other person;
27(1) L'agent d'immigration ou l'agent de la paix doit faire part au sous-ministre, dans un rapport écrit et circonstancié, de renseignements concernant un résident permanent et indiquant que celui-ci, selon le cas:
.
- Evidence: `governing_rule` cue `under` at chunk `4161648` offsets `605-610`; context: (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
(b) for being or having been sponsored by a person who is determined to be inadmissible for misrepresentation;
(c) on a final determination to vacate a decision to allow the claim for refugee protection by the permanent resident or the foreign national; or
(d) on ceasing to be a citizen under paragraph 10(1)(a) of the Citizenship Act, in the circumstances set out in subsection 10(2) of that Act.
- Evidence: `reasoning_application` cue `apply` at chunk `4161648` offsets `1136-1141`; context: (2) The following provisions govern subsection (1):
(a) the permanent resident or the foreign national continues to be inadmissible for misrepresentation for a period of two years following, in the case of a determination outside Canada, a final determination of inadmissibility under subsection (1) or, in the case of a determination in Canada, the date the removal order is enforced; and
(b) paragraph (1)(b) does not apply unless the Minister is satisfied that the facts of the case justify the inadmissibility.

#### Section text

[43] When Parliament introduced the new IRPA, one of the objects of the Act was to strengthen inadmissibility as seen in the clause by clause analysis prepared for IRPA.

[44] It would therefore lead to an absurdity if a person who would clearly be inadmissible under the Immigration Act would no longer be inadmissible under IRPA. Further, the plain meaning of "indirect" supports the Board's interpretation.
Humanitarian and compassionate considerations

[45] The respondent submitted that contrary to the applicant's assertions, the Board was at all times aware of the difference between her circumstances and her husband's circumstances, including (i) the applicant herself did not make any misrepresentations; (ii) unlike her husband, she expressed genuine remorse; and (iii) unlike her husband, the applicant had spent a significant amount of time in Canada and had demonstrated establishment in Canada.

[46] The applicant's situation was fully considered. What she is now asking the Court to do is re-weigh the weight given by the Board to the different factors. For example, the applicant argued that the Board placed "undue emphasis" on the misrepresentation. The question of weight of evidence is not properly the subject of judicial review (see Suresh v. Canada 2002 SCC 1; Hawthorne v. Canada (Minister of Citizenship and Immigration) MCI 2002 FCA 475).
Relevant Statutory Provisions

[47] Paragraph 27(1)(e) of the Immigration Act, supra, states:
27(1) An immigration officer or a peace officer shall forward a written report to the Deputy Minister setting out the details of any information in the possession of the immigration officer or peace officer indicating that a permanent resident is a person who
. . .
(e) was granted landing by reason of possession of a false or improperly obtained passport, visa or other document pertaining to his admission or by reason of any fraudulent or improper means or misrepresentation of any material fact, whether exercised or made by himself or by any other person;
27(1) L'agent d'immigration ou l'agent de la paix doit faire part au sous-ministre, dans un rapport écrit et circonstancié, de renseignements concernant un résident permanent et indiquant que celui-ci, selon le cas:
. . .
e) a obtenu le droit d'établissement soit sur la foi d'un passeport, visa - ou autre document relatif à son admission - faux ou obtenu irrégulièrement, soit par des moyens frauduleux ou irréguliers ou encore par suite d'une fausse indication sur un fait important, même si ces moyens ou déclarations sont le fait d'un tiers;

[48] Subsections 40(1) and (2) of IRPA states :
40. (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
(b) for being or having been sponsored by a person who is determined to be inadmissible for misrepresentation;
(c) on a final determination to vacate a decision to allow the claim for refugee protection by the permanent resident or the foreign national; or
(d) on ceasing to be a citizen under paragraph 10(1)(a) of the Citizenship Act, in the circumstances set out in subsection 10(2) of that Act.
(2) The following provisions govern subsection (1):
(a) the permanent resident or the foreign national continues to be inadmissible for misrepresentation for a period of two years following, in the case of a determination outside Canada, a final determination of inadmissibility under subsection (1) or, in the case of a determination in Canada, the date the removal order is enforced; and
(b) paragraph (1)(b) does not apply unless the Minister is satisfied that the facts of the case justify the inadmissibility.
40. (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants:
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d'entraîner une erreur dans l'application de la présente loi;
b) être ou avoir été parrainé par un répondant dont il a été statué qu'il est interdit de territoire pour fausses déclarations;
c) l'annulation en dernier ressort de la décision ayant accueilli la demande d'asile;
d) la perte de la citoyenneté au titre de l'alinéa 10(1)a) de la Loi sur la citoyenneté dans le cas visé au paragraphe 10(2) de cette loi.
(2) Les dispositions suivantes s'appliquent au paragraphe (1):
a) l'interdiction de territoire court pour les deux ans suivant la décision la constatant en dernier ressort, si le résident permanent ou l'étranger n'est pas au pays, ou suivant l'exécution de la mesure de renvoi;
b) l'alinéa (1)b) ne s'applique que si le ministre est convaincu que les faits en cause justifient l'interdiction.
Analysis and Decision

## 1901:3 · paragraphs 49-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bbc5073f06248e713086d8f0e86cdb7b0378094c7e38be35d418ee9071af607e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:3:subtheme:1 · paragraphs 49-50

- Raw key terms: `accompanying, already, applicant, applied, baker, basis, birth, board`
- Display key terms: `accompanying, already, applied, baker, basis, birth`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: accompanying, already, applied, baker, basis, birth Rule/authority context: [49] Standard of Review The standard of review on questions of statutory interpretation is correctness. Application context: When her husband applied to Immigration Canada, the applicant was included as an accompanying spouse. Evidence spans paragraphs 49-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161649` offsets `111-119`; context: On the question of humanitarian and compassionate considerations, on the basis of Baker, supra, and the cases that followed it, I am satisfied that the decision should be reviewed on the reasonableness simpliciter standard.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4161649` offsets `5-23`; context: [49] Standard of Review
The standard of review on questions of statutory interpretation is correctness.
- Evidence: `issue` cue `Issue` at chunk `4161650` offsets `5-10`; context: [50] Issue 1
Did the Board err in holding the applicant had indirectly misrepresented herself?
- Evidence: `reasoning_application` cue `applied` at chunk `4161650` offsets `259-266`; context: When her husband applied to Immigration Canada, the applicant was included as an accompanying spouse.

#### Section text

[49] Standard of Review
The standard of review on questions of statutory interpretation is correctness. On the question of humanitarian and compassionate considerations, on the basis of Baker, supra, and the cases that followed it, I am satisfied that the decision should be reviewed on the reasonableness simpliciter standard.

[50] Issue 1
Did the Board err in holding the applicant had indirectly misrepresented herself?
The applicant came to Canada on a student visa in 1996. She had married her husband in 1990. Her husband, unbeknownst to her, was already married. When her husband applied to Immigration Canada, the applicant was included as an accompanying spouse. They were landed in September 1998 and the applicant gave birth to a Canadian born daughter in March 1999.

## 1901:4 · paragraphs 51-56

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `80de60967e1c692fc04bd1a3c6781c3e9c8f3c01831967ba8f7672ea14ffa7ac`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:4:subtheme:1 · paragraphs 51-52

- Raw key terms: `applicant, husband, married, accompanying, against, application, applied, around`
- Display key terms: `husband, married, accompanying, against, applied, around`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: husband, married, accompanying, against, applied, around Rule/authority context: The exclusion order against the applicant was issued pursuant to paragraph 40(1)(a) of IRPA. Application context: [51] The applicant applied to Canadian Citizenship in 2001 and around the time of being interviewed, her husband told her for the first time that he was previously married and had a son. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4161651` offsets `19-26`; context: [51] The applicant applied to Canadian Citizenship in 2001 and around the time of being interviewed, her husband told her for the first time that he was previously married and had a son.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4161652` offsets `427-438`; context: The exclusion order against the applicant was issued pursuant to paragraph 40(1)(a) of IRPA.

#### 1901:4:subtheme:2 · paragraphs 53-56

- Raw key terms: `applicant, irpa, meaning, paragraph, canada, facts, husband's, include`
- Display key terms: `irpa, meaning, paragraph, facts, husband's, include`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: irpa, meaning, paragraph, facts, husband's, include Position/evidence statements: [55] The applicant submitted that the plain meaning of the words of the section would not include persons such as the applicant as she did not misrepresent the facts or withhold material facts. Application context: [56] An initial reading of paragraph 40(1)(a) of IRPA would appear to support the applicant's assertion that paragraph 40(1)(a) does not apply to misrepresentations by other persons. Evidence spans paragraphs 53-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161653` offsets `9-17`; context: [53] The question now becomes whether paragraph 40(1)(a) of IRPA, when it speaks of "indirectly misrepresenting or withholding material facts" includes the situation of the applicant who did not know of her husband's previous marriage, or the fact that he had a son.
- Evidence: `issue` cue `question` at chunk `4161654` offsets `1644-1652`; context: Although the Court of Appeal looked to the plain meaning of the specific provisions in question in the present case, with respect, I believe that the court did not pay sufficient attention to the scheme of the ESA, its object or the intention of the legislature; nor was the context of the words in issue appropriately recognized.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4161654` offsets `114-122`; context: 27 at paragraphs 21 to 23 states:
Although much has been written about the interpretation of legislation (see, e.
- Evidence: `party_position` cue `submitted` at chunk `4161655` offsets `19-28`; context: [55] The applicant submitted that the plain meaning of the words of the section would not include persons such as the applicant as she did not misrepresent the facts or withhold material facts.
- Evidence: `reasoning_application` cue `apply` at chunk `4161656` offsets `137-142`; context: [56] An initial reading of paragraph 40(1)(a) of IRPA would appear to support the applicant's assertion that paragraph 40(1)(a) does not apply to misrepresentations by other persons.
- Evidence: `counterargument_limitation` cue `However` at chunk `4161656` offsets `183-190`; context: However, if the section is given this meaning, it would lead to a potential absurdity in that an applicant could directly misrepresent in an application and bring a person such as the applicant in with him or her, and that person would then not be removable from Canada if the person had no knowledge of the misrepresentation.

#### Section text

[51] The applicant applied to Canadian Citizenship in 2001 and around the time of being interviewed, her husband told her for the first time that he was previously married and had a son.

[52] As a result of the husband's failure to disclose on his application that he was married and had a son, an exclusion order was issued against the husband for directly misrepresenting a material fact. An exclusion order was also issued against the applicant for indirectly misrepresenting a material fact due to being an accompanying spouse on her husband's application. The exclusion order against the applicant was issued pursuant to paragraph 40(1)(a) of IRPA.

[53] The question now becomes whether paragraph 40(1)(a) of IRPA, when it speaks of "indirectly misrepresenting or withholding material facts" includes the situation of the applicant who did not know of her husband's previous marriage, or the fact that he had a son.

[54] The Supreme Court of Canada in Rizzo & Rizzo Shoes Ltd. (Re) 1998 1 S.C.R. 27 at paragraphs 21 to 23 states:
Although much has been written about the interpretation of legislation (see, e.g., Ruth Sullivan, Statutory Interpretation (1997); Ruth Sullivan, Driedger on the Construction of Statutes (3rd ed. 1994) (hereinafter "Construction of Statutes"); Pierre-André Côté, The Interpretation of Legislation in Canada (2nd ed. 1991)), Elmer Driedger in Construction of Statutes (2nd ed. 1983) best encapsulates the approach upon which I prefer to rely. He recognizes that statutory interpretation cannot be founded on the wording of the legislation alone. At p. 87 he states:
Today there is only one principle or approach, namely, the words of an Act are to be read in their entire context and in their grammatical and ordinary sense harmoniously with the scheme of the Act, the object of the Act, and the intention of Parliament.
Recent cases which have cited the above passage with approval include: R. v. Hydro-Québec, [1997] 1 S.C.R. 213; Royal Bank of Canada v. Sparrow Electric Corp., [1997] 1 S.C.R. 411; Verdun v. Toronto-Dominion Bank, [1996] 3 S.C.R. 550; Friesen v. Canada, [1995] 3 S.C.R. 103.
I also rely upon s. 10 of the Interpretation Act, R.S.O. 1980, c. 219, which provides that every Act "shall be deemed to be remedial" and directs that every Act shall "receive such fair, large and liberal construction and interpretation as will best ensure the attainment of the object of the Act according to its true intent, meaning and spirit".
Although the Court of Appeal looked to the plain meaning of the specific provisions in question in the present case, with respect, I believe that the court did not pay sufficient attention to the scheme of the ESA, its object or the intention of the legislature; nor was the context of the words in issue appropriately recognized. I now turn to a discussion of these issues.

[55] The applicant submitted that the plain meaning of the words of the section would not include persons such as the applicant as she did not misrepresent the facts or withhold material facts. In paragraph 22(1)(e) of the Immigration Act, supra, reference was made to misrepresentation of material facts by the applicant or "any other person". Paragraph 40(1)(a) of IRPA does not contain the same wording.

[56] An initial reading of paragraph 40(1)(a) of IRPA would appear to support the applicant's assertion that paragraph 40(1)(a) does not apply to misrepresentations by other persons. However, if the section is given this meaning, it would lead to a potential absurdity in that an applicant could directly misrepresent in an application and bring a person such as the applicant in with him or her, and that person would then not be removable from Canada if the person had no knowledge of the misrepresentation. I am of the view that paragraph 40(1)(a) can be interpreted so as to apply to the applicant. The word "indirectly" can be interpreted to cover the situation such as the present one where the applicant relied on being included in her husband's application, even though she did not know of his being married with a son.

## 1901:5 · paragraphs 57-65

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `beb41bef4a3b4d559f91f635ee54bf604fe268f094ba8bd716b65ae92bdbddcf`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:5:subtheme:1 · paragraphs 57-58

- Raw key terms: `irpa, above, abuse, adding, analysis, another, applicant, bill`
- Display key terms: `irpa, above, abuse, adding, analysis, another, bill`
- Argument roles: `counterargument_limitation, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, party_position, reasoning_application Display terms: irpa, above, abuse, adding, analysis, another, bill Position/evidence statements: Interpreting paragraph 40(1)(a) of IRPA to deem indirect misrepresentations as equivalent to the provision by another is not, as the applicant submitted, adding words to the statute. Application context: [58] I would therefore find that the Board did not err in holding that the applicant had indirectly misrepresented facts to immigration officials. Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `but` at chunk `4161657` offsets `298-301`; context: [57] The above interpretation is supported by the content found at clause 40 of the explanatory clause-by-clause analysis of Bill C-11 (now IRPA) document which states:
This section is similar to provisions of the current act concerning misrepresentation by either permanent or temporary residents but modifies those provisions to enhance enforcement tools designed to eliminate abuse.
- Evidence: `party_position` cue `submitted` at chunk `4161658` offsets `290-299`; context: Interpreting paragraph 40(1)(a) of IRPA to deem indirect misrepresentations as equivalent to the provision by another is not, as the applicant submitted, adding words to the statute.
- Evidence: `reasoning_application` cue `therefore` at chunk `4161658` offsets `13-22`; context: [58] I would therefore find that the Board did not err in holding that the applicant had indirectly misrepresented facts to immigration officials.

#### 1901:5:subtheme:2 · paragraphs 59-60

- Raw key terms: `applicant, board, separately, agree, appeared, applicant's, application, applications`
- Display key terms: `separately, agree, appeared, applicant's, applications`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: separately, agree, appeared, applicant's, applications Position/evidence statements: The applicant submitted that the Board made an error in not dealing with the applicant's and her husband's application separately from each other and further, that the Board erred in making the determination that there w Evidence spans paragraphs 59-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4161659` offsets `5-10`; context: [59] Issue 2
Was the member's refusal to find sufficient humanitarian and compassionate factors based on erroneous findings of fact made in a perverse and capricious manner?
- Evidence: `party_position` cue `submitted` at chunk `4161659` offsets `188-197`; context: The applicant submitted that the Board made an error in not dealing with the applicant's and her husband's application separately from each other and further, that the Board erred in making the determination that there were insufficient H & C grounds.

#### 1901:5:subtheme:3 · paragraphs 61-64

- Raw key terms: `board, applicant, issue, make, afoul, applicant's, application, argument`
- Display key terms: `make, afoul, applicant's, argument`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: make, afoul, applicant's, argument Application context: [64] The application for judicial review is therefore dismissed. Operative outcome context: [64] The application for judicial review is therefore dismissed. Evidence spans paragraphs 61-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161661` offsets `9-17`; context: [61] The question of placing undue weight on the misrepresentation as compared to the positive factors militating in favour of the applicant is an issue within the purview of the Board.
- Evidence: `issue` cue `issue` at chunk `4161662` offsets `25-30`; context: [62] With respect to the issue of family reunification, this issue was raised by the applicant before the Board and dealt with by the Board.
- Evidence: `reasoning_application` cue `therefore` at chunk `4161664` offsets `44-53`; context: [64] The application for judicial review is therefore dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4161664` offsets `54-63`; context: [64] The application for judicial review is therefore dismissed.

#### 1901:5:subtheme:4 · paragraphs 65-65

- Raw key terms: `administration, applicant, application, certification, certify, dependant, directly, error`
- Display key terms: `administration, certification, certify, dependant, directly, error`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: administration, certification, certify, dependant, directly, error Position/evidence statements: [65] The applicant proposed a serious question of general importance for certification regarding the interpretation of paragraph 40(1)(a) of IRPA and the respondent submitted a similar question. Rule/authority context: I am prepared to certify the following question as a serious question of general importance: Under s. Evidence spans paragraphs 65-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161665` offsets `38-46`; context: [65] The applicant proposed a serious question of general importance for certification regarding the interpretation of paragraph 40(1)(a) of IRPA and the respondent submitted a similar question.
- Evidence: `party_position` cue `submitted` at chunk `4161665` offsets `165-174`; context: [65] The applicant proposed a serious question of general importance for certification regarding the interpretation of paragraph 40(1)(a) of IRPA and the respondent submitted a similar question.
- Evidence: `governing_rule` cue `Under` at chunk `4161665` offsets `288-293`; context: I am prepared to certify the following question as a serious question of general importance:
Under s.

#### Section text

[57] The above interpretation is supported by the content found at clause 40 of the explanatory clause-by-clause analysis of Bill C-11 (now IRPA) document which states:
This section is similar to provisions of the current act concerning misrepresentation by either permanent or temporary residents but modifies those provisions to enhance enforcement tools designed to eliminate abuse.

[58] I would therefore find that the Board did not err in holding that the applicant had indirectly misrepresented facts to immigration officials. Interpreting paragraph 40(1)(a) of IRPA to deem indirect misrepresentations as equivalent to the provision by another is not, as the applicant submitted, adding words to the statute. It is giving substance to Parliament's intent.

[59] Issue 2
Was the member's refusal to find sufficient humanitarian and compassionate factors based on erroneous findings of fact made in a perverse and capricious manner?
The applicant submitted that the Board made an error in not dealing with the applicant's and her husband's application separately from each other and further, that the Board erred in making the determination that there were insufficient H & C grounds.

[60] With respect to treating the applications separately, I do not agree with the applicant. The Board appeared to be aware of difference in circumstances between the applicant and her husband. By way of example, the Board noted that:
1. Ms. Wang herself did not make any misrepresentations.
2. Ms. Wang, unlike her husband, did express genuine regret for what happened.
3. Ms. Wang spent much more time in Canada than her husband and has demonstrated establishment in Canada, unlike her husband.

[61] The question of placing undue weight on the misrepresentation as compared to the positive factors militating in favour of the applicant is an issue within the purview of the Board. It is not for the Court to intervene other than in exceptional cases. The applicant's argument is centred on the position that she should not have to pay the price for her husband's misrepresentation when she played no knowing part in it. While it is an unfortunate situation, the applicant does fall afoul of paragraph 40(1)(a) of IRPA, and the Board is entitled to determine the weight to be given various factors, and make the determination it did.

[62] With respect to the issue of family reunification, this issue was raised by the applicant before the Board and dealt with by the Board.

[63] I am satisfied that the Board did not make a reviewable error in dealing with the H & C considerations, including the best interests of the child.

[64] The application for judicial review is therefore dismissed.

[65] The applicant proposed a serious question of general importance for certification regarding the interpretation of paragraph 40(1)(a) of IRPA and the respondent submitted a similar question. I am prepared to certify the following question as a serious question of general importance:
Under s. 40(1)(a) of the Immigration and Refugee Protection Act, which reads:
A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act . . .
is a permanent resident inadmissible for indirectly misrepresenting a material fact if they are landed as the dependant of a principal applicant who misrepresented material facts on his application for landing?
ORDER

## 1901:6 · paragraphs 66-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ac94901ffe3e92bdb0ead779bbeb782ff3344b7efbd11250cfb51b531a93eb2a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:6:subtheme:1 · paragraphs 66-67

- Raw key terms: `applicant, immigration, administration, application, british, cause, certified, citizenship`
- Display key terms: `administration, british, certified`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: administration, british, certified Rule/authority context: The following question is certified as a serious question of general importance: Under s. Operative outcome context: The application for judicial review is dismissed. Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4161666` offsets `95-103`; context: The following question is certified as a serious question of general importance:
Under s.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4161666` offsets `789-795`; context: O'Keefe"
JUDGE
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-5815-04
- Evidence: `governing_rule` cue `Under` at chunk `4161666` offsets `162-167`; context: The following question is certified as a serious question of general importance:
Under s.
- Evidence: `disposition` cue `dismissed` at chunk `4161666` offsets `67-76`; context: The application for judicial review is dismissed.

#### Section text

[66] IT IS ORDERED that:
1. The application for judicial review is dismissed.
2. The following question is certified as a serious question of general importance:
Under s. 40(1)(a) of the Immigration and Refugee Protection Act, which reads:
A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act . . .
is a permanent resident inadmissible for indirectly misrepresenting a material fact if they are landed as the dependant of a principal applicant who misrepresented material facts on his application for landing?
"John A. O'Keefe"
JUDGE
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-5815-04

STYLE OF CAUSE: XIAO QIONG WANG
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
PLACE OF HEARING: VANCOUVER, BRITISH COLUMBIA
DATE OF HEARING: MARCH 16, 2005
REASONS FOR 

## 1901:7 · paragraphs 68-68

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b520da5ebfdb415417193aa482de1d28b162a2278eaaed0564ddfdd1f5ba4269`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1901:7:subtheme:1 · paragraphs 68-68

- Raw key terms: `appearances, applicant, attorney, august, bond, british, canada, columbia`
- Display key terms: `august, bond, british, columbia`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, bond, british, columbia No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 68-68. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: O'KEEFE J.
DATED: AUGUST 3, 2005
APPEARANCES:
Phillip J. Rankin FOR APPLICANT
Sandra Weafer FOR RESPONDENT
SOLICITORS OF RECORD:
Rankin & Bond
Vancouver, British Columbia FOR APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada FOR RESPONDENT
