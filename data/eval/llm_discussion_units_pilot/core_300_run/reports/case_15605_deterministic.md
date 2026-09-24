# Discussion Units: case 15605

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **51**
- Continuity pairs: **50**
- Discussion Units: **3**
- Paragraph source hashes: **51**
- Sub-themes: **11**

## 15605:1 · paragraphs 0-47

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b61218c7e3955faeedee3fb2f8846ee218182d83dc0b8a4c002d372e7f2b29b6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 15605:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicant, application, computer, systems, canada, decision, permanent, residence`
- Display key terms: `computer, systems, permanent, residence`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position Display terms: computer, systems, permanent, residence Position/evidence statements: On November 2, 2000, he submitted an application for permanent residence under the independent category, indicating that his intended occupations were Computer Systems Analyst, listed under National Occupational Classifi | [3] The applicant claimed to have worked over thirteen years in the computer programming and systems analysis field, with a variety of companies in India. Rule/authority context: On November 2, 2000, he submitted an application for permanent residence under the independent category, indicating that his intended occupations were Computer Systems Analyst, listed under National Occupational Classifi | [6] The applicant was assessed under the occupations of Computer Systems Analyst and Computer Programmer for which he required a total 70 units of assessment. Operative outcome context: For the reasons outlined below, I prefer the evidence of the applicant and find that he was denied procedural fairness. | [4] The applicant was granted a student authorization to study in Canada in 2000, at the Computek Institute of Technology. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4741921` offsets `424-432`; context: There is a clear conflict between their evidence.
- Evidence: `disposition` cue `denied` at chunk `4741921` offsets `526-532`; context: For the reasons outlined below, I prefer the evidence of the applicant and find that he was denied procedural fairness.
- Evidence: `party_position` cue `submitted` at chunk `4741922` offsets `65-74`; context: On November 2, 2000, he submitted an application for permanent residence under the independent category, indicating that his intended occupations were Computer Systems Analyst, listed under National Occupational Classification ("NOC") 2162, and Computer Programmer, NOC 2163.
- Evidence: `governing_rule` cue `under` at chunk `4741922` offsets `114-119`; context: On November 2, 2000, he submitted an application for permanent residence under the independent category, indicating that his intended occupations were Computer Systems Analyst, listed under National Occupational Classification ("NOC") 2162, and Computer Programmer, NOC 2163.
- Evidence: `party_position` cue `claimed` at chunk `4741923` offsets `18-25`; context: [3] The applicant claimed to have worked over thirteen years in the computer programming and systems analysis field, with a variety of companies in India.
- Evidence: `disposition` cue `granted` at chunk `4741924` offsets `22-29`; context: [4] The applicant was granted a student authorization to study in Canada in 2000, at the Computek Institute of Technology.
- Evidence: `governing_rule` cue `under` at chunk `4741926` offsets `31-36`; context: [6] The applicant was assessed under the occupations of Computer Systems Analyst and Computer Programmer for which he required a total 70 units of assessment.

#### 15605:1:subtheme:2 · paragraphs 7-16

- Raw key terms: `immigration, officer, canada, visa, applicant, applicant's, employment, computer`
- Display key terms: `officer, visa, applicant's, employment, computer`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: officer, visa, applicant's, employment, computer Position/evidence statements: [9] In addition to the officer's Computer Assisted Immigration Processing System ("CAIPS") notes provided in the tribunal record submitted to the court, the officer elaborated upon these concerns in an affidavit sworn on | [11] The applicant argues that the visa officer failed to apprise him of her concerns in three important areas that played a significant role in her decision to refuse his application for permanent residence. Rule/authority context: [8] Since the applicant did not obtain the necessary 70 units of assessment and because he was awarded no units of assessment for the experience factor, he was not eligible for an immigrant visa pursuant to the former Im | [13] The applicant also submits that it was perverse for the visa officer to conclude that he had demonstrated no experience in his chosen occupations when she awarded him the requisite points under the Education and Tra Application context: Therefore, the officer found that he did not have the qualifications and experience of a Computer Programmer or Systems Analyst as set out in the NOC descriptions. | [8] Since the applicant did not obtain the necessary 70 units of assessment and because he was awarded no units of assessment for the experience factor, he was not eligible for an immigrant visa pursuant to the former Im Evidence spans paragraphs 7-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4741927` offsets `489-497`; context: In addition, the visa officer stated in the refusal letter that the applicant's responses to her computer programming questions, as well as his inability to adequately explain discrepancies in his claimed employment experience, led the officer to question the credibility and the reliability of his documents.
- Evidence: `evidence_fact` cue `found that` at chunk `4741927` offsets `575-585`; context: Therefore, the officer found that he did not have the qualifications and experience of a Computer Programmer or Systems Analyst as set out in the NOC descriptions.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4741927` offsets `552-561`; context: Therefore, the officer found that he did not have the qualifications and experience of a Computer Programmer or Systems Analyst as set out in the NOC descriptions.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741928` offsets `195-206`; context: [8] Since the applicant did not obtain the necessary 70 units of assessment and because he was awarded no units of assessment for the experience factor, he was not eligible for an immigrant visa pursuant to the former Immigration Regulations, 1978, SOR/78-172, s.
- Evidence: `reasoning_application` cue `because` at chunk `4741928` offsets `80-87`; context: [8] Since the applicant did not obtain the necessary 70 units of assessment and because he was awarded no units of assessment for the experience factor, he was not eligible for an immigrant visa pursuant to the former Immigration Regulations, 1978, SOR/78-172, s.
- Evidence: `party_position` cue `submitted` at chunk `4741929` offsets `129-138`; context: [9] In addition to the officer's Computer Assisted Immigration Processing System ("CAIPS") notes provided in the tribunal record submitted to the court, the officer elaborated upon these concerns in an affidavit sworn on May 16, 2003, almost a full year after the date of the interview.
- Evidence: `evidence_fact` cue `record` at chunk `4741929` offsets `122-128`; context: [9] In addition to the officer's Computer Assisted Immigration Processing System ("CAIPS") notes provided in the tribunal record submitted to the court, the officer elaborated upon these concerns in an affidavit sworn on May 16, 2003, almost a full year after the date of the interview.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741930` offsets `60-69`; context: [10] The applicant challenges the accuracy of the officer's affidavit on the ground that it contains a number of statements that were not supported by the evidence before the officer.
- Evidence: `party_position` cue `argues` at chunk `4741931` offsets `19-25`; context: [11] The applicant argues that the visa officer failed to apprise him of her concerns in three important areas that played a significant role in her decision to refuse his application for permanent residence.
- Evidence: `party_position` cue `submits` at chunk `4741932` offsets `28-35`; context: [12] Further, the applicant submits that it was not reasonably open to the visa officer to conclude that he did not possess the necessary work experience and education to qualify for selection as a Computer Systems Analyst and/or Computer Programmer.
- Evidence: `reasoning_application` cue `conclude` at chunk `4741932` offsets `91-99`; context: [12] Further, the applicant submits that it was not reasonably open to the visa officer to conclude that he did not possess the necessary work experience and education to qualify for selection as a Computer Systems Analyst and/or Computer Programmer.
- Evidence: `party_position` cue `submits` at chunk `4741933` offsets `24-31`; context: [13] The applicant also submits that it was perverse for the visa officer to conclude that he had demonstrated no experience in his chosen occupations when she awarded him the requisite points under the Education and Training Factor ("ETF").
- Evidence: `governing_rule` cue `under` at chunk `4741933` offsets `193-198`; context: [13] The applicant also submits that it was perverse for the visa officer to conclude that he had demonstrated no experience in his chosen occupations when she awarded him the requisite points under the Education and Training Factor ("ETF").
- Evidence: `reasoning_application` cue `conclude` at chunk `4741933` offsets `77-85`; context: [13] The applicant also submits that it was perverse for the visa officer to conclude that he had demonstrated no experience in his chosen occupations when she awarded him the requisite points under the Education and Training Factor ("ETF").
- Evidence: `party_position` cue `submits` at chunk `4741934` offsets `225-232`; context: The respondent submits that the officer's version of the interview as recorded in those notes should be preferred to the extent of any contradiction with the applicant's affidavit sworn in September 2002, several months after the interview.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741934` offsets `110-119`; context: [14] The respondent conceded during the course of the hearing that there were difficulties with the officer's affidavit.
- Evidence: `counterargument_limitation` cue `however` at chunk `4741934` offsets `134-141`; context: I was urged, however, to rely on the CAIPS notes as an accurate record of the interview.
- Evidence: `party_position` cue `submits` at chunk `4741935` offsets `20-27`; context: [15] The respondent submits that the visa officer reasonably concluded that the applicant had failed to discharge his burden, pursuant to section 8(1) of the former Immigration Act, R.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741935` offsets `126-137`; context: [15] The respondent submits that the visa officer reasonably concluded that the applicant had failed to discharge his burden, pursuant to section 8(1) of the former Immigration Act, R.
- Evidence: `counterargument_limitation` cue `however` at chunk `4741935` offsets `567-574`; context: The respondent argues that the applicant's submissions amount to a disagreement with the visa officer's conclusions, however, this is not a ground to find a reviewable error on judicial review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4741936` offsets `46-64`; context: [16] The respondent refers to the deferential standard of review of visa officer decisions with respect to applications for permanent residence, set out in To v.

#### 15605:1:subtheme:3 · paragraphs 17-19

- Raw key terms: `applicant, respondent, visa, applicant's, canada, employment, experience, intended`
- Display key terms: `visa, applicant's, employment, experience, intended`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: visa, applicant's, employment, experience, intended Position/evidence statements: )(QL), the respondent submits that the determination of whether a person has performed the duties of his intended occupation is a pure question of fact and subject to the standard set out in section 18. | [18] In the present case, the respondent argues that the officer reasonably concluded that the applicant had failed to demonstrate that he had any employment experience in his intended occupations. Application context: [19] The respondent submits that the officer's concerns with discrepancies in the applicant's claimed work experience were reasonable, as the applicant had claimed to be working for one particular company in April 2000,  Evidence spans paragraphs 17-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4741937` offsets `260-267`; context: )(QL), the respondent submits that the determination of whether a person has performed the duties of his intended occupation is a pure question of fact and subject to the standard set out in section 18.
- Evidence: `party_position` cue `submits` at chunk `4741937` offsets `226-233`; context: )(QL), the respondent submits that the determination of whether a person has performed the duties of his intended occupation is a pure question of fact and subject to the standard set out in section 18.
- Evidence: `party_position` cue `argues` at chunk `4741938` offsets `41-47`; context: [18] In the present case, the respondent argues that the officer reasonably concluded that the applicant had failed to demonstrate that he had any employment experience in his intended occupations.
- Evidence: `evidence_fact` cue `evidence` at chunk `4741938` offsets `232-240`; context: This finding was based on all the evidence before the visa officer, including the applicant's responses to the technical questions posed and the officer's questions regarding his employment history.
- Evidence: `party_position` cue `submits` at chunk `4741939` offsets `20-27`; context: [19] The respondent submits that the officer's concerns with discrepancies in the applicant's claimed work experience were reasonable, as the applicant had claimed to be working for one particular company in April 2000, when he applied for a student authorization for Canada, and then in the material in support of his application for permanent residence, the applicant's employment with that company was listed as having terminated in 1993.
- Evidence: `reasoning_application` cue `applied` at chunk `4741939` offsets `228-235`; context: [19] The respondent submits that the officer's concerns with discrepancies in the applicant's claimed work experience were reasonable, as the applicant had claimed to be working for one particular company in April 2000, when he applied for a student authorization for Canada, and then in the material in support of his application for permanent residence, the applicant's employment with that company was listed as having terminated in 1993.

#### 15605:1:subtheme:4 · paragraphs 20-25

- Raw key terms: `applicant, officer, concerns, visa, fairness, apprise, duty, employment`
- Display key terms: `officer, concerns, visa, fairness, apprise, duty, employment`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: officer, concerns, visa, fairness, apprise, duty, employment Position/evidence statements: [20] Secondly, the respondent submits that the officer did not err in awarding units of assessment pursuant to the Education and Training Factor, and awarding him zero units for the experience factor. Rule/authority context: [20] Secondly, the respondent submits that the officer did not err in awarding units of assessment pursuant to the Education and Training Factor, and awarding him zero units for the experience factor. | In my opinion, for the reasons that will follow, the applicant's version is to be preferred, and pursuant to this evidence, I am persuaded that the visa officer breached the duty of fairness owed to the applicant in not  Application context: The respondent also argues that the case authorities relied on by the applicant do not deal with the ETF but rather the occupational factor and therefore do not stand for the principle that the award of units under this  Evidence spans paragraphs 20-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4741940` offsets `731-737`; context: ISSUES
- Evidence: `party_position` cue `submits` at chunk `4741940` offsets `30-37`; context: [20] Secondly, the respondent submits that the officer did not err in awarding units of assessment pursuant to the Education and Training Factor, and awarding him zero units for the experience factor.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741940` offsets `228-237`; context: The officer attests in her affidavit that the CAIPS system "automatically" awards applicants this factor after input of the number of units for education and the NOC code for a particular occupation.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741940` offsets `99-110`; context: [20] Secondly, the respondent submits that the officer did not err in awarding units of assessment pursuant to the Education and Training Factor, and awarding him zero units for the experience factor.
- Evidence: `reasoning_application` cue `therefore` at chunk `4741940` offsets `545-554`; context: The respondent also argues that the case authorities relied on by the applicant do not deal with the ETF but rather the occupational factor and therefore do not stand for the principle that the award of units under this factor is consistent with the applicant having met the employment requirements in his intended occupation(s).
- Evidence: `counterargument_limitation` cue `but` at chunk `4741940` offsets `506-509`; context: The respondent also argues that the case authorities relied on by the applicant do not deal with the ETF but rather the occupational factor and therefore do not stand for the principle that the award of units under this factor is consistent with the applicant having met the employment requirements in his intended occupation(s).
- Evidence: `evidence_fact` cue `evidence` at chunk `4741941` offsets `339-347`; context: Were the visa officer's findings that the applicant was not occupationally qualified to serve as either a Computer Systems Analyst or Computer Programmer reasonably open to her on the evidence?
- Evidence: `evidence_fact` cue `evidence` at chunk `4741942` offsets `169-177`; context: [22] It is well established that in the context of visa officer decisions procedural fairness requires that an applicant be given an opportunity to respond to extrinsic evidence relied upon by the visa officer and to be apprised of the officer's concerns arising therefrom: Muliadi, supra.
- Evidence: `evidence_fact` cue `evidence` at chunk `4741944` offsets `216-224`; context: In my opinion, for the reasons that will follow, the applicant's version is to be preferred, and pursuant to this evidence, I am persuaded that the visa officer breached the duty of fairness owed to the applicant in not giving him an opportunity to respond to her concerns in several key areas which appear to have been critical to her decision to refuse his application for permanent residence.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741944` offsets `199-210`; context: In my opinion, for the reasons that will follow, the applicant's version is to be preferred, and pursuant to this evidence, I am persuaded that the visa officer breached the duty of fairness owed to the applicant in not giving him an opportunity to respond to her concerns in several key areas which appear to have been critical to her decision to refuse his application for permanent residence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4741944` offsets `551-557`; context: Further, most of the officer's concerns in this case cannot be said to have emanated directly from the requirements of the legislation, such as, for example, the officer's concerns with the look and form of the applicant's educational documents and her view that his marks at Computek Institute were "low".
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741945` offsets `50-59`; context: [25] As noted above, the applicant attests in his affidavit that in several key areas, the visa officer did not apprise him of her concerns or give him an opportunity to respond.

#### 15605:1:subtheme:5 · paragraphs 26-27

- Raw key terms: `applicant, caips, indicate, interview, notes, officer, simultaneously, typed`
- Display key terms: `caips, indicate, interview, notes, officer, simultaneously, typed`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: caips, indicate, interview, notes, officer, simultaneously, typed Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4741946` offsets `131-136`; context: [26] The officer responds to such comments as follows at paragraph 21 of her affidavit:
With respect to the Applicant having taken issue with statements made in the CAIPS notes, wherein I have indicated that the Applicant "could not respond" or "did not respond", I state that whenever I indicate such, the Applicant has not responded in any manner to the particular inquiry.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741946` offsets `77-86`; context: [26] The officer responds to such comments as follows at paragraph 21 of her affidavit:
With respect to the Applicant having taken issue with statements made in the CAIPS notes, wherein I have indicated that the Applicant "could not respond" or "did not respond", I state that whenever I indicate such, the Applicant has not responded in any manner to the particular inquiry.

#### 15605:1:subtheme:6 · paragraphs 28-36

- Raw key terms: `officer, applicant, interview, affidavit, canada, notes, officer's, applicant's`
- Display key terms: `officer, interview, affidavit, notes, officer's, applicant's`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: officer, interview, affidavit, notes, officer's, applicant's Application context: I am not prepared to adopt the approach that counsel for the respondent seemed to be suggesting, that is, that visa officers have no interest in these applications, therefore their version should be believed when it conf | and I therefore strongly dispute her comments that "Subj. Evidence spans paragraphs 28-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4741948` offsets `80-88`; context: [28] As conceded by the respondent at the hearing, the officer's CAIPS notes in question were prepared more than three weeks after the interview and not simultaneously during the interview as attested to by the officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4741949` offsets `393-401`; context: The longer an officer waits to create such a transcription of the events of the interview, the less probative these notes become as evidence as to what occurred at the interview.
- Evidence: `counterargument_limitation` cue `However` at chunk `4741949` offsets `700-707`; context: However, in this case there are no handwritten notes from the officer on the certified tribunal record before this Court.
- Evidence: `reasoning_application` cue `therefore` at chunk `4741950` offsets `668-677`; context: I am not prepared to adopt the approach that counsel for the respondent seemed to be suggesting, that is, that visa officers have no interest in these applications, therefore their version should be believed when it conflicts with that of an applicant.
- Evidence: `evidence_fact` cue `record` at chunk `4741951` offsets `402-408`; context: Further, her account of the interview is vulnerable due to the fact that she failed to record her impressions of it during the interview, or closely thereafter.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741952` offsets `459-468`; context: I prefer the applicant's affidavit on these points, and find that the applicant was not apprised of the visa officer's concerns in these areas, or given a chance to respond to them.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741954` offsets `63-72`; context: [34] In contrast, the applicant attests at paragraph 15 of his affidavit that the officer did not ask him any questions concerning his studies in Canada, except for a few questions concerning the courses that he had completed.
- Evidence: `reasoning_application` cue `therefore` at chunk `4741954` offsets `268-277`; context: and I therefore strongly dispute her comments that "Subj.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741955` offsets `383-392`; context: The explanations provided by the applicant in his affidavit persuade me that he would have had something to say in response, had he been informed as to the officer's impressions of his marks, at the interview.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741956` offsets `255-264`; context: In her affidavit, the officer explains her concerns related to these two diplomas, in that they were of "poor quality", lacked security features and the applicant's full name did not appear on either document.

#### 15605:1:subtheme:7 · paragraphs 37-38

- Raw key terms: `applicant, concerns, diplomas, documents, educational, officer, visa, accredited`
- Display key terms: `concerns, diplomas, documents, educational, officer, visa, accredited`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: concerns, diplomas, documents, educational, officer, visa, accredited Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4741957` offsets `279-287`; context: The applicant states, at paragraph 17 of his affidavit, that the officer did not question him about these diplomas, apart from a few questions concerning his studies at "Born Brilliant Software Education".
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741957` offsets `168-177`; context: [37] The applicant attests that the interview lasted no longer than 30 minutes, whereas the visa officer makes no comment on the length of the interview, either in her affidavit or the CAIPS notes.
- Evidence: `evidence_fact` cue `evidence` at chunk `4741958` offsets `175-183`; context: The applicant was aware that evidence of his educational background was required in order to satisfy his onus of proof.
- Evidence: `counterargument_limitation` cue `but` at chunk `4741958` offsets `390-393`; context: The visa officer's problems with two of his diplomas, in that they do not contain his full name, but rather state "R.

#### 15605:1:subtheme:8 · paragraphs 39-46

- Raw key terms: `applicant, applicant's, officer, application, fairness, breaches, employment, experience`
- Display key terms: `applicant's, officer, fairness, breaches, employment, experience`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: applicant's, officer, fairness, breaches, employment, experience Position/evidence statements: [39] The applicant has also submitted that the CAIPS notes do not accurately reflect what he stated at the interview in regards to the issues of his claimed employment experience being compared to his experience as claim | In his affidavit, the applicant claims that he was able to answer these questions with no difficulty whatsoever. Rule/authority context: [40] The applicant's submission in relation to breaches of procedural fairness because of alleged undertakings that the officer made, but did not complete, is best left for another day, as I am not satisfied that the cas | [46] I note that pursuant to recent amendments to the Immigration and Refugee Protection Regulations, SOR/2002-227, as amended by SOR/2003-383, the respondent's reconsideration of this application will benefit from dual  Application context: [40] The applicant's submission in relation to breaches of procedural fairness because of alleged undertakings that the officer made, but did not complete, is best left for another day, as I am not satisfied that the cas | Due to such breaches in procedural fairness, it is not possible to know if the outcome would have been different had the applicant had a full and fair opportunity to respond to the officer's concerns, and therefore, his  Evidence spans paragraphs 39-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4741959` offsets `135-141`; context: [39] The applicant has also submitted that the CAIPS notes do not accurately reflect what he stated at the interview in regards to the issues of his claimed employment experience being compared to his experience as claimed in his request for a student authorization in 2000 and his employment in Canada.
- Evidence: `party_position` cue `submitted` at chunk `4741959` offsets `28-37`; context: [39] The applicant has also submitted that the CAIPS notes do not accurately reflect what he stated at the interview in regards to the issues of his claimed employment experience being compared to his experience as claimed in his request for a student authorization in 2000 and his employment in Canada.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741959` offsets `351-360`; context: In these areas, I again prefer the applicant's affidavit evidence, that he stated that the information on these applications was identical and that the officer could verify this by obtaining the documentation related to that application.
- Evidence: `issue` cue `issue` at chunk `4741960` offsets `265-270`; context: [40] The applicant's submission in relation to breaches of procedural fairness because of alleged undertakings that the officer made, but did not complete, is best left for another day, as I am not satisfied that the cases cited by the applicant in support of this issue are directly on point, as they deal with actions of the Immigration and Refugee Board, a decision-maker acting in a distinct context, pursuant to different rules of procedure and different expectations of fairness.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741960` offsets `405-416`; context: [40] The applicant's submission in relation to breaches of procedural fairness because of alleged undertakings that the officer made, but did not complete, is best left for another day, as I am not satisfied that the cases cited by the applicant in support of this issue are directly on point, as they deal with actions of the Immigration and Refugee Board, a decision-maker acting in a distinct context, pursuant to different rules of procedure and different expectations of fairness.
- Evidence: `reasoning_application` cue `because` at chunk `4741960` offsets `79-86`; context: [40] The applicant's submission in relation to breaches of procedural fairness because of alleged undertakings that the officer made, but did not complete, is best left for another day, as I am not satisfied that the cases cited by the applicant in support of this issue are directly on point, as they deal with actions of the Immigration and Refugee Board, a decision-maker acting in a distinct context, pursuant to different rules of procedure and different expectations of fairness.
- Evidence: `party_position` cue `claims` at chunk `4741961` offsets `443-449`; context: In his affidavit, the applicant claims that he was able to answer these questions with no difficulty whatsoever.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4741961` offsets `418-427`; context: In his affidavit, the applicant claims that he was able to answer these questions with no difficulty whatsoever.
- Evidence: `counterargument_limitation` cue `However` at chunk `4741961` offsets `524-531`; context: However, according to the visa officer, although the applicant answered all six questions, he did not correctly answer four of the six.
- Evidence: `reasoning_application` cue `therefore` at chunk `4741962` offsets `767-776`; context: Due to such breaches in procedural fairness, it is not possible to know if the outcome would have been different had the applicant had a full and fair opportunity to respond to the officer's concerns, and therefore, his application will be sent back for reassessment in accordance with these reasons.
- Evidence: `counterargument_limitation` cue `However` at chunk `4741962` offsets `142-149`; context: However, in my view, this was not the sole or primary reason for the refusal, as the officer's negative views of "discrepancies" concerning his claimed employment experience, and the credibility and reliability of his documents, were also central to her decision to deny his application.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4741965` offsets `243-252`; context: Therefore, no costs shall be awarded.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4741966` offsets `17-28`; context: [46] I note that pursuant to recent amendments to the Immigration and Refugee Protection Regulations, SOR/2002-227, as amended by SOR/2003-383, the respondent's reconsideration of this application will benefit from dual assessment, pursuant to the former Act and the current Immigration and Refugee Protection Act, S.

#### 15605:1:subtheme:9 · paragraphs 47-47

- Raw key terms: `allowed, application, certified, judicial, question, review`
- Display key terms: `allowed, certified, judicial, question, review`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: allowed, certified, judicial, question, review Operative outcome context: [47] This application for judicial review is allowed. Evidence spans paragraphs 47-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4741967` offsets `57-65`; context: No question is certified.
- Evidence: `disposition` cue `allowed` at chunk `4741967` offsets `45-52`; context: [47] This application for judicial review is allowed.

#### Section text

Rukmangathan v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-02-26
Neutral citation
2004 FC 284
File numbers
IMM-4007-02
Decision Content
Date: 20040226
Docket: IMM-4007-02
Citation: 2004 FC 284
Toronto, Ontario, February 26th, 2004
Present: The Honourable Mr. Justice Mosley
BETWEEN:
PANDI RUKMANGATHAN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] This is an application for judicial review of the decision of visa officer Moira Escott (the "visa officer"), dated June 17, 2002, denying Mr. Pandi Rukmangathan's application for permanent residence in Canada. Both the applicant and the visa officer have filed affidavits in these proceedings concerning what transpired at an interview held at Detroit, Michigan on May 21, 2002. There is a clear conflict between their evidence. For the reasons outlined below, I prefer the evidence of the applicant and find that he was denied procedural fairness.
BACKGROUND

[2] The applicant is a citizen of India. On November 2, 2000, he submitted an application for permanent residence under the independent category, indicating that his intended occupations were Computer Systems Analyst, listed under National Occupational Classification ("NOC") 2162, and Computer Programmer, NOC 2163. His wife and two minor children were listed as accompanying dependants.

[3] The applicant claimed to have worked over thirteen years in the computer programming and systems analysis field, with a variety of companies in India. His application was also supported by several post-university training certificates in computer programming and computer systems development.

[4] The applicant was granted a student authorization to study in Canada in 2000, at the Computek Institute of Technology. The applicant completed three diplomas at this Institute in computer programming, systems analysis and network engineering, during his two and a half years of study there.

[5] The applicant attended a personal interview with the visa officer at the Canadian Consulate General in Detroit, Michigan on May 21, 2002. The officer's decision, denying his application for permanent residence, was communicated to him by letter dated June 17, 2002.
The Visa Officer's Decision

[6] The applicant was assessed under the occupations of Computer Systems Analyst and Computer Programmer for which he required a total 70 units of assessment. He was awarded 59 as follows:
Age 10
Occupational Factor 00
ETF [Educational Training Factor]/ SVP 15
Experience 00
Arranged Employment 00
Demographic Factor 08
Education 15
English 07
French 00
Bonus 00
Personal Suitability 04
Total 59

[7] In arriving at her decision, the visa officer concluded that the points awarded to Mr. Rukmangathan accurately reflected his chances for successful settlement in Canada. He did not, in her view, display a fluent ability to speak English. In addition, the visa officer stated in the refusal letter that the applicant's responses to her computer programming questions, as well as his inability to adequately explain discrepancies in his claimed employment experience, led the officer to question the credibility and the reliability of his documents. Therefore, the officer found that he did not have the qualifications and experience of a Computer Programmer or Systems Analyst as set out in the NOC descriptions.

[8] Since the applicant did not obtain the necessary 70 units of assessment and because he was awarded no units of assessment for the experience factor, he was not eligible for an immigrant visa pursuant to the former Immigration Regulations, 1978, SOR/78-172, s. 9(1)(b)(I) (the Aformer Regulations").

[9] In addition to the officer's Computer Assisted Immigration Processing System ("CAIPS") notes provided in the tribunal record submitted to the court, the officer elaborated upon these concerns in an affidavit sworn on May 16, 2003, almost a full year after the date of the interview.
APPLICANT'S SUBMISSIONS

[10] The applicant challenges the accuracy of the officer's affidavit on the ground that it contains a number of statements that were not supported by the evidence before the officer. He urges the court to disregard that affidavit in its entirety or, in the alternative, to disregard those portions that are in direct conflict with the applicant's evidence. He also questions the accuracy of the CAIPS notes, attesting that they did not correctly reflect many of his responses at the interview.

[11] The applicant argues that the visa officer failed to apprise him of her concerns in three important areas that played a significant role in her decision to refuse his application for permanent residence. These are: the visa officer's concerns regarding the quality of his answers to her computer programming questions, her concerns with his marks at the Computek Institute of Technology and the need for him to take such training, and her concerns with his educational studies in India. He contends that the visa officer's failure to apprise him of these concerns is a breach of her duty to act fairly: Muliadi v. Canada (Minister of Employment and Immigration), [1986] 2 F.C. 205 (C.A.).

[12] Further, the applicant submits that it was not reasonably open to the visa officer to conclude that he did not possess the necessary work experience and education to qualify for selection as a Computer Systems Analyst and/or Computer Programmer. In the applicant's submission, he adequately explained the alleged discrepancies regarding his employment. The visa officer erred by ignoring these explanations: Yang v. Canada (Minister of Employment and Immigration), [1992] F.C.J. No. 632 (T.D.) (QL).

[13] The applicant also submits that it was perverse for the visa officer to conclude that he had demonstrated no experience in his chosen occupations when she awarded him the requisite points under the Education and Training Factor ("ETF"). Awarding him the requisite units under this factor is consistent with a finding that he met the employment requirements of his intended occupations: Dauz v. Canada (Minister of Citizenship and Immigration) (1999), 173 F.T.R. 288, Osman v. Canada (Minister of Citizenship and Immigration) (2000), 181 F.T.R. 304 and Liu v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1408 (T.D.)(QL). The applicant further argues that it was incumbent on the visa officer to assess his experience in each of the various responsibilities in his occupation in order to award units of assessment for experience and the officer erred by failing to do so: Hajariwala v. Canada (Minister of Employment and Immigration), [1989] 2 F.C. 79 (T.D.).
RESPONDENT'S SUBMISSIONS

[14] The respondent conceded during the course of the hearing that there were difficulties with the officer's affidavit. I was urged, however, to rely on the CAIPS notes as an accurate record of the interview. The respondent submits that the officer's version of the interview as recorded in those notes should be preferred to the extent of any contradiction with the applicant's affidavit sworn in September 2002, several months after the interview. In support, the respondent relies on Paracha v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 1786 (T.D.)(QL) and Sehgal v. Canada (Minister of Citizenship and Immigration), [2001] F.C.J. No. 385 (T.D.)(QL).

[15] The respondent submits that the visa officer reasonably concluded that the applicant had failed to discharge his burden, pursuant to section 8(1) of the former Immigration Act, R.S.C. 1985, c. I-2 (the "former Act"), of satisfying her that he met the legislative requirements for admission to Canada. Specifically, the visa officer was not satisfied that he had the NOC-defined employment experience as a computer programmer or systems analyst. The respondent argues that the applicant's submissions amount to a disagreement with the visa officer's conclusions, however, this is not a ground to find a reviewable error on judicial review.

[16] The respondent refers to the deferential standard of review of visa officer decisions with respect to applications for permanent residence, set out in To v. Canada (Minister of Employment and Immigration), [1996] F.C.J. No. 696 (C.A.)(QL), namely the same standard established in Maple Lodge Farms Ltd. v. Government of Canada, [1982] 2 S.C.R. 2. The respondent also relies on the more recent case law of Liu v. Canada (Minister of Citizenship and Immigration) (2001), 208 F.T.R. 99 where this court has described this standard as equating to the reasonableness simpliciter standard.

[17] Relying on Dizon v. Canada (Minister of Citizenship and Immigration), [2002] F.C.J. No. 135 (T.D.)(QL) and Seepersaud v. Canada (Minister of Citizenship and Immigration), [2001] F.C.J. No. 1316 (T.D.)(QL), the respondent submits that the determination of whether a person has performed the duties of his intended occupation is a pure question of fact and subject to the standard set out in section 18.1(4)(d) of the Federal Courts Act, R.S.C. 1985, c. F-7. Moreover, visa officers should be afforded deference in determining whether an applicant satisfied the requirements of a particular occupation: Madan v. Canada (Minister of Citizenship and Immigration) (1999), 172 F.T.R. 262.

[18] In the present case, the respondent argues that the officer reasonably concluded that the applicant had failed to demonstrate that he had any employment experience in his intended occupations. This finding was based on all the evidence before the visa officer, including the applicant's responses to the technical questions posed and the officer's questions regarding his employment history.

[19] The respondent submits that the officer's concerns with discrepancies in the applicant's claimed work experience were reasonable, as the applicant had claimed to be working for one particular company in April 2000, when he applied for a student authorization for Canada, and then in the material in support of his application for permanent residence, the applicant's employment with that company was listed as having terminated in 1993. Further, the respondent submits that the visa officer's concerns as to the veracity of the applicant's documents were reasonable.

[20] Secondly, the respondent submits that the officer did not err in awarding units of assessment pursuant to the Education and Training Factor, and awarding him zero units for the experience factor. The officer attests in her affidavit that the CAIPS system "automatically" awards applicants this factor after input of the number of units for education and the NOC code for a particular occupation. The respondent also argues that the case authorities relied on by the applicant do not deal with the ETF but rather the occupational factor and therefore do not stand for the principle that the award of units under this factor is consistent with the applicant having met the employment requirements in his intended occupation(s).
ISSUES

[21] 1. Did the visa officer breach the duty of fairness by not apprising the applicant of her concerns and by failing to comply with her undertakings?
2. Were the visa officer's findings that the applicant was not occupationally qualified to serve as either a Computer Systems Analyst or Computer Programmer reasonably open to her on the evidence?
ANALYSIS

[22] It is well established that in the context of visa officer decisions procedural fairness requires that an applicant be given an opportunity to respond to extrinsic evidence relied upon by the visa officer and to be apprised of the officer's concerns arising therefrom: Muliadi, supra. In my view, the Federal Court of Appeal's endorsement in Muliadi, supra, of Lord Parker's comments in In re H.K. (An Infant), [1967] 2 Q.B. 617, indicates that the duty of fairness may require immigration officials to inform applicants of their concerns with applications so that an applicant may have a chance to "disabuse" an officer of such concerns, even where such concerns arise from evidence tendered by the applicant. Other decisions of this court support this interpretation of Muliadi, supra. See, for example, Fong v. Canada (Minister of Employment and Immigration), [1990] 3 F.C. 705 (T.D.), John v. Canada (Minister of Citizenship and Immigration), [2003] F.C.J. No. 350 (T.D.)(QL) and Cornea v. Canada (Minister of Citizenship and Immigration) (2003), 30 Imm. L.R. (3d) 38 (F.C.T.D.), where it had been held that a visa officer should apprise an applicant at an interview of her negative impressions of evidence tendered by the applicant.

[23] However, this principle of procedural fairness does not stretch to the point of requiring that a visa officer has an obligation to provide an applicant with a "running score" of the weaknesses in their application: Asghar v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 1091 (T.D.)(QL) at para. 21 and Liao v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1926 (T.D.)(QL) at para. 23. And there is no obligation on the part of a visa officer to apprise an applicant of her concerns that arise directly from the requirements of the former Act or Regulations: Yu v. Canada (Minister of Employment and Immigration) (1990), 36 F.T.R. 296, Ali v. Canada (Minister of Citizenship and Immigration) (1998), 151 F.T.R. 1 and Bakhtiania v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No.1023 (T.D.)(QL).

[24] The affidavits filed in this proceeding present starkly contradictory versions of the interview. In my opinion, for the reasons that will follow, the applicant's version is to be preferred, and pursuant to this evidence, I am persuaded that the visa officer breached the duty of fairness owed to the applicant in not giving him an opportunity to respond to her concerns in several key areas which appear to have been critical to her decision to refuse his application for permanent residence. Further, most of the officer's concerns in this case cannot be said to have emanated directly from the requirements of the legislation, such as, for example, the officer's concerns with the look and form of the applicant's educational documents and her view that his marks at Computek Institute were "low".

[25] As noted above, the applicant attests in his affidavit that in several key areas, the visa officer did not apprise him of her concerns or give him an opportunity to respond.

[26] The officer responds to such comments as follows at paragraph 21 of her affidavit:
With respect to the Applicant having taken issue with statements made in the CAIPS notes, wherein I have indicated that the Applicant "could not respond" or "did not respond", I state that whenever I indicate such, the Applicant has not responded in any manner to the particular inquiry. The CAIPS notes are typed by me simultaneously with the interview as it transpires.
[Emphasis added]

[27] The statement from the visa officer, highlighted above, that she took the CAIPS notes simultaneously as the interview transpired, is undermined by the CAIPS notes themselves, which indicate that they were typed "17-JUN-2002", by "MLE". "MLE" are the initials of the visa officer, that is Moria Lucy Escott. The interview of the applicant was held on May 21, 2002. Further, the CAIPS notes entry from May 28, 2002, also typed by the visa officer, states "NOTES TO FOLLOW".

[28] As conceded by the respondent at the hearing, the officer's CAIPS notes in question were prepared more than three weeks after the interview and not simultaneously during the interview as attested to by the officer.

[29] The value of information contained in CAIPS notes, in my view, is largely tied to the fact that it is created either simultaneously, or within a very short time period, from the actual interview with the applicant, when the memory of the officer is fresh. The longer an officer waits to create such a transcription of the events of the interview, the less probative these notes become as evidence as to what occurred at the interview. I should note that where an officer makes dated, handwritten notes at the time of the interview and then later transcribes these into CAIPS, this will counter the negative impression by providing a contemporaneous record of the interview, in a different form. However, in this case there are no handwritten notes from the officer on the certified tribunal record before this Court.

[30] The following comments of Justice Reed in Parveen v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 660 (T.D.)(QL), aptly describe an important point regarding cases such as the present one, where an officer and an applicant have presented very different descriptions of what transpired at the interview. As she stated at paragraph 10:
...Visa officers deal with many applications, one can expect that they will not have as precise a memory of the event as does the applicant. I am not prepared to adopt the approach that counsel for the respondent seemed to be suggesting, that is, that visa officers have no interest in these applications, therefore their version should be believed when it conflicts with that of an applicant. Once a visa officer's decision is challenged that person has an interest in justifying his or her decision. This is an entirely natural reaction. At that point the visa officer is not a disinterested person.

[31] Here, the memory of the visa officer has been placed in doubt, given that she has attested to writing the notes at the time of the interview, when clearly she wrote them close to a month past that time. The events of the interview cannot be said to have occurred precisely as the officer has attested to them. Further, her account of the interview is vulnerable due to the fact that she failed to record her impressions of it during the interview, or closely thereafter.

[32] Turning now to the visa officer's problems with the applicant's application, which the applicant maintains were never raised at the interview, namely, why he had taken further courses in Canada, the consideration that his marks were "low" (although they were in the mid-70s range) and the "poor quality" of two of his educational documents, in my view, these concerns should have been placed before the applicant for a response. I prefer the applicant's affidavit on these points, and find that the applicant was not apprised of the visa officer's concerns in these areas, or given a chance to respond to them. In this manner, the officer breached the duty of fairness.

[33] The officer had concerns with the fact that the applicant decided to study in Canada for over two years at Computek Institute of Technology, if he was already a qualified systems analyst and programmer, with several years of work experience. The officer attests that the applicant could offer no explanation as to why he came to study in Canada.

[34] In contrast, the applicant attests at paragraph 15 of his affidavit that the officer did not ask him any questions concerning his studies in Canada, except for a few questions concerning the courses that he had completed. The applicant goes on to state:
...and I therefore strongly dispute her comments that "Subj. could not respond". If she had bothered to ask, I would have stated that in the ever-changing information technology field, it is absolutely essential for one to maintain current as to new technologies and programming languages and to upgrade one's skills.

[35] Secondly, the officer's view that the applicant's grades at Computek were "low", is strange, given that they appear to have been in the mid-70's, however, such reasoning may have been open to the officer, had she informed the applicant that she had problems believing that someone with his experience would receive these marks. The explanations provided by the applicant in his affidavit persuade me that he would have had someth

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 15605:2 · paragraphs 48-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b8e4109385fbe6f4d93e03e9dbfa21b7902a9e4ba465d702ce6b29b3ff00e8f0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 15605:2:subtheme:1 · paragraphs 48-49

- Raw key terms: `above, allowed, applicant, applicant's, application, aside, canada, cause`
- Display key terms: `above, allowed, applicant's, aside`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: above, allowed, applicant's, aside No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
THIS COURT ORDERS that this application for judicial review is allowed, the officer's decision dated June 17, 2002 is set aside and the applicant's application for permanent residence in Canada is remitted for reconsideration by a different officer. No question is certified.
"Richard G. Mosley"
J.F.C.
I HEREBY CERTIFY that the above document is a true copy of the original filed of record in the Registry of the Federal Court the __________ day of _____________ A.D. 2004
Dated this _______ day of _______________, 2004
_______________________________
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-4007-02

STYLE OF CAUSE: PANDI RUKMANGATHAN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: FEBRUARY 25, 2004
REASONS FOR 

## 15605:3 · paragraphs 50-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c00cc6976adb3c9c0d5055ea0c749da3c64f726c2056e9e0ae7aa22b849a3bee`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 15605:3:subtheme:1 · paragraphs 50-50

- Raw key terms: `appearances, applicant, attorney, canada, citizenship, court, date, dated`
- Display key terms: `date, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 50-50. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY : MOSLEY J.
DATED: FEBRUARY 26, 2004
APPEARANCES:
Mr. Ian R.J. Wong
FOR APPLICANT
Mr. Stephen Jarvis
FOR RESPONDENT
SOLICITORS OF RECORD:
Ian R.J. Wong
Toronto, Ontario
FOR APPLICANT
Morris Rosenberg
Deputy Attorney General of Canada
Toronto, Ontario
FOR RESPONDENT
FEDERAL COURT
TRIAL DIVISION
Date: 20040226
Docket: IMM-4007-02
BETWEEN:
PANDI RUKMANGATHAN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
AND ORDER
