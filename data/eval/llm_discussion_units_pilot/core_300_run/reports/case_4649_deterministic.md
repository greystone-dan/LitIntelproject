# Discussion Units: case 4649

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **49**
- Continuity pairs: **48**
- Discussion Units: **2**
- Paragraph source hashes: **49**
- Sub-themes: **6**

## 4649:1 · paragraphs 0-10

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6d118542806a289366675fece8dc1a3590c3ac8152e1693ab1ab6a4c72c5cd50`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4649:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `applicant, date, decision, application, april, employment, income, letter`
- Display key terms: `date, april, employment, income, letter`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: date, april, employment, income, letter Position/evidence statements: She asserted that she had submitted the requested documents on April 23, 2021 and, based on her Notice of Assessment and tax return for 2020, that she had met the $5000 minimum income criteria. Rule/authority context: The Second Decision is the decision under review in this application. Application context: [3] The Applicant applied for and received the CRB for seven two-week periods between September 27, 2020 and January 2, 2021. Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `4261404` offsets `612-619`; context: However, the CRB is administered by CRA.
- Evidence: `reasoning_application` cue `applied` at chunk `4261405` offsets `18-25`; context: [3] The Applicant applied for and received the CRB for seven two-week periods between September 27, 2020 and January 2, 2021.
- Evidence: `counterargument_limitation` cue `However` at chunk `4261405` offsets `204-211`; context: However, she received a response informing her that her application could not be processed at that time, it had been selected for further validation, and that identified documents were required before the applications could be processed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4261406` offsets `234-243`; context: In her affidavit, affirmed on August 11, 2021 and filed in support of her application for judicial review, the Applicant states that she provided with that letter her 2020 tax return (I note, however, that the document included with her letter at Exhibit C of her affidavit is a CRA 2020 Assessment that states that her income tax filing date was February 22, 2021 and the date of assessment was March 4, 2021).
- Evidence: `counterargument_limitation` cue `however` at chunk `4261406` offsets `419-426`; context: In her affidavit, affirmed on August 11, 2021 and filed in support of her application for judicial review, the Applicant states that she provided with that letter her 2020 tax return (I note, however, that the document included with her letter at Exhibit C of her affidavit is a CRA 2020 Assessment that states that her income tax filing date was February 22, 2021 and the date of assessment was March 4, 2021).
- Evidence: `evidence_fact` cue `found that` at chunk `4261409` offsets `207-217`; context: CRA found that the Applicant was not eligible as she did not meet the following criteria:
You did not earn at least $5,000 (before taxes) of employment or net self-employment income in 2019, 2020, or in the 12 months before the date of your first application.
- Evidence: `party_position` cue `submitted` at chunk `4261411` offsets `101-110`; context: She asserted that she had submitted the requested documents on April 23, 2021 and, based on her Notice of Assessment and tax return for 2020, that she had met the $5000 minimum income criteria.
- Evidence: `governing_rule` cue `under` at chunk `4261412` offsets `224-229`; context: The Second Decision is the decision under review in this application.

#### Section text

Aryan v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2022-02-04
Neutral citation
2022 FC 139
File numbers
T-1133-21
Decision Content
Date: 20220204
Docket: T-1133-21
Citation: 2022 FC 139
Ottawa, Ontario, February 4, 2022
PRESENT: The Honourable Madam Justice Strickland
BETWEEN:
MARIA ARYAN
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] The Applicant, Ms. Maria Aryan, brings this application for judicial review of a decision made by a benefits compliance officer [Officer] of the Canada Revenue Agency [CRA] dated June 17, 2021. The Officer found the Applicant was not eligible to receive the Canada Recovery Benefit [CRB].
Background

[2] The Canada Recovery Benefits Act, SC 2020, c 12, s 2, [CRB Act], came into effect on October 2, 2020 and established the CRB. The CRB was available to provide income support, for any two-week period beginning on September 27, 2020, and ending on October 23, 2021, to eligible employed and self-employed individuals who were directly affected by the COVID-19 pandemic. One of the eligibility requirements was a minimum income of $5000 received from specified sources within specified periods. The Minister responsible for the CRB is the Minister of Employment and Social Development (CRB Act, ss 2, 3 and 4). However, the CRB is administered by CRA.

[3] The Applicant applied for and received the CRB for seven two-week periods between September 27, 2020 and January 2, 2021. In January 2021, she attempted to apply online for an eighth two-week period. However, she received a response informing her that her application could not be processed at that time, it had been selected for further validation, and that identified documents were required before the applications could be processed. The response listed this documentation, for self-employed persons, as invoices for services rendered, receipt of payment for the services rendered, documentation showing income was earned from carrying on a “trade or business” and, any other documentation that would substantiate $5000 in employment or self-employment.

[4] On February 22, 2021, the Applicant wrote to CRA indicating that she had filed her 2020 income tax return and that it indicates that she met the minimum income requirement in 2020 as a result of her self-employment income. In her affidavit, affirmed on August 11, 2021 and filed in support of her application for judicial review, the Applicant states that she provided with that letter her 2020 tax return (I note, however, that the document included with her letter at Exhibit C of her affidavit is a CRA 2020 Assessment that states that her income tax filing date was February 22, 2021 and the date of assessment was March 4, 2021). The Applicant asked that she be provided with online access to file her CRB application.

[5] On April 6, 2021, the Applicant wrote to CRA stating that she began work as a self-employed person in January 2020 providing in-house services such as cleaning, preparing food, serving guests, and washing dishes at an hourly rate inclusive of fee, tips etc. She stated that she received payment in cash. Further, that in April 2020 she registered for Employment Insurance [EI] for self-employed persons and, in November 2020, she opened a bank account for her work activities. She enclosed:
her CRA issued Notice of Assessment for the 2020 taxation year, dated March 4, 2021;
an HSBC bank statement for the period November 7 – December 7, 2020; and
a copy of a confirmation of Employment Insurance registration having an effective date of April 12, 2020.

[6] By letter dated April 23, 2021, the Applicant also provided HSBC bank statements for the period December 7, 2020 to April 6, 2021.

[7] On April 30, 2021, CRA advised the Applicant that, further to a conversation on April 23, 2021, CRA had not received the documents requested in order to confirm her CRB eligibility [First Decision]. CRA found that the Applicant was not eligible as she did not meet the following criteria:
You did not earn at least $5,000 (before taxes) of employment or net self-employment income in 2019, 2020, or in the 12 months before the date of your first application.

[8] The First Decision also advised the Applicant that if she did not agree with this determination then she could request a second review within 30 days of the date of that letter. The second review would be completed by an officer who was not involved in the first review decision.

[9] By letter dated May 11, 2021, the Applicant requested a second review. She asserted that she had submitted the requested documents on April 23, 2021 and, based on her Notice of Assessment and tax return for 2020, that she had met the $5000 minimum income criteria. She again described her employment and again noted that the documents previously submitted indicated that she had $5350 of net self-employment income in 2020, that she had registered for EI for self-employed persons in April, opened a bank account for her business in November 2020, and provided bank statements from November 2020 to May 2021. She attached:
a copy of the First Decision;
a copy of her previously submitted Notice of Assessment for the 2020 taxation year, dated March 4, 2021;
a print-out of the above-mentioned 2020 Assessment for the 2020 tax year from CRA’s MyAccount website;
a copy of the previously provided confirmation of Employment Insurance registration having an effective date of April 12, 2020; and
copies of the previously provided HSBC bank statements for the period November 7, 2020 to April 6, 2021, as well as a statement for the period April 7 to May 6, 2021.

[10] By letter of June 17, 2021, the Officer provided CRA’s negative decision regarding the Applicant’s April 6, 2021 request for a second review of the CRB application [Second Decision]. The Second Decision is the decision under review in this application.
Second Decision

## 4649:2 · paragraphs 11-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0b26d1e8caf51c1447666cbb724639f87425a52fedff439abc647fec0f0eeded`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4649:2:subtheme:1 · paragraphs 11-13

- Raw key terms: `application, canada, decision, employment, review, benefit, date, development`
- Display key terms: `employment, review, benefit, date, development`
- Argument roles: `disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position, reasoning_application Display terms: employment, review, benefit, date, development Position/evidence statements: Counsel for the Respondent submits that because the Minister of National Revenue is not directly affected by the decision, which was made by the CRA on behalf of the Minister of Employment and Social Development, the pro Rule/authority context: (ministre) Eligibility 3(1) A person is eligible for a Canada recovery benefit for any two-week period falling within the period beginning on September 27, 2020 and ending on October 23, 2021 if … (d) in the case of an a Application context: [12] The Second Decision also indicated that if the Applicant disagreed with the decision she could apply to this Court for judicial review within 30 days of the date of the letter. | Counsel for the Respondent submits that because the Minister of National Revenue is not directly affected by the decision, which was made by the CRA on behalf of the Minister of Employment and Social Development, the pro Operative outcome context: As you did not meet the eligibility criteria to qualify for CRB, any future CRB applications will be denied, unless you can provide proof that you are able to satisfy the eligibility criteria. Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `denied` at chunk `4261413` offsets `541-547`; context: As you did not meet the eligibility criteria to qualify for CRB, any future CRB applications will be denied, unless you can provide proof that you are able to satisfy the eligibility criteria.
- Evidence: `issue` cue `whether` at chunk `4261414` offsets `1384-1391`; context: 1) in respect of a two-week period beginning in 2021, they had, for 2019 or for 2020 or in the 12-month period preceding the day on which they make the application, a total income of at least $5,000 from the sources referred to in subparagraphs (d)(i) to (v);
…
(i) they sought work during the two-week period, whether as an employee or in self-employment;
…
Income from self-employment
(2) For the purpose of paragraphs (1)(d) to (f), income from self-employment is revenue from the self-employment less expenses incurred to earn that revenue.
- Evidence: `governing_rule` cue `under` at chunk `4261414` offsets `757-762`; context: (ministre)
Eligibility
3(1) A person is eligible for a Canada recovery benefit for any two-week period falling within the period beginning on September 27, 2020 and ending on October 23, 2021 if
…
(d) in the case of an application made under section 4 in respect of a two-week period beginning in 2020, they had, for 2019 or in the 12-month period preceding the day on which they make the application, a total income of at least $5,000…
(e) in the case of an application made under section 4 by a person other than a person referred to in paragraph (e.
- Evidence: `reasoning_application` cue `apply` at chunk `4261414` offsets `100-105`; context: [12] The Second Decision also indicated that if the Applicant disagreed with the decision she could apply to this Court for judicial review within 30 days of the date of the letter.
- Evidence: `party_position` cue `submits` at chunk `4261415` offsets `221-228`; context: Counsel for the Respondent submits that because the Minister of National Revenue is not directly affected by the decision, which was made by the CRA on behalf of the Minister of Employment and Social Development, the proper responding party is the Attorney General of Canada, in accordance with Rule 303 of the Federal Courts Rules, SOR/98-106.
- Evidence: `reasoning_application` cue `because` at chunk `4261415` offsets `234-241`; context: Counsel for the Respondent submits that because the Minister of National Revenue is not directly affected by the decision, which was made by the CRA on behalf of the Minister of Employment and Social Development, the proper responding party is the Attorney General of Canada, in accordance with Rule 303 of the Federal Courts Rules, SOR/98-106.

#### 4649:2:subtheme:2 · paragraphs 14-18

- Raw key terms: `applicant, canada, decision, based, issued, matter, minister, officer`
- Display key terms: `based, issued, matter, officer`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: based, issued, matter, officer Position/evidence statements: [16] The parties submit and I agree that the standard of review applicable to the merits of the decision is reasonableness (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov]. | She submits that, based on those documents, she established that she met the $5000 minimum income criteria and was therefore eligible to apply for and receive the CRB. Rule/authority context: Issues and Standard of Review | [16] The parties submit and I agree that the standard of review applicable to the merits of the decision is reasonableness (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov]. Application context: Accordingly, I will order that the style of cause will be amended, replacing the Minister of National Revenue with the Attorney General of Canada as the named respondent (Hasselsjo v Canada (Attorney General), 2021 CanLI | She submits that, based on those documents, she established that she met the $5000 minimum income criteria and was therefore eligible to apply for and receive the CRB. Evidence spans paragraphs 14-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4261416` offsets `362-368`; context: Issues and Standard of Review
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4261416` offsets `373-391`; context: Issues and Standard of Review
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4261416` offsets `117-128`; context: Accordingly, I will order that the style of cause will be amended, replacing the Minister of National Revenue with the Attorney General of Canada as the named respondent (Hasselsjo v Canada (Attorney General), 2021 CanLII 89551 (FC) at para 2).
- Evidence: `issue` cue `issue` at chunk `4261417` offsets `306-311`; context: [15] While the Applicant makes various submissions in support of her view that the Second Decision was unreasonable, unfair, not transparent, unintelligible, unjustified and failed to consider the harsh impact it had on her livelihood, having reviewed her submissions in whole, it is my view that the sole issue in this matter is whether the Second Decision was reasonable.
- Evidence: `party_position` cue `submit` at chunk `4261418` offsets `17-23`; context: [16] The parties submit and I agree that the standard of review applicable to the merits of the decision is reasonableness (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov].
- Evidence: `governing_rule` cue `standard of review` at chunk `4261418` offsets `45-63`; context: [16] The parties submit and I agree that the standard of review applicable to the merits of the decision is reasonableness (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov].
- Evidence: `party_position` cue `submits` at chunk `4261419` offsets `318-325`; context: She submits that, based on those documents, she established that she met the $5000 minimum income criteria and was therefore eligible to apply for and receive the CRB.
- Evidence: `reasoning_application` cue `therefore` at chunk `4261419` offsets `429-438`; context: She submits that, based on those documents, she established that she met the $5000 minimum income criteria and was therefore eligible to apply for and receive the CRB.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4261420` offsets `34-43`; context: [18] The Respondent has filed the affidavit of Ms.

#### 4649:2:subtheme:3 · paragraphs 19-26

- Raw key terms: `applicant, officer, review, second, agent, found, income, report`
- Display key terms: `officer, review, second, agent, income, report`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: officer, review, second, agent, income, report Position/evidence statements: [23] The Second Review Report records that during a March 26, 2021 telephone call the first CRA agent advised the Applicant to submit further documentation as the information she had provided was not sufficient proof of  | [24] The first CRA agent records, on April 28, 2021, that they reviewed the bank statements submitted by the Applicant for January, February, March and April of 2021. Application context: The letter would also advise the applicant of their right to apply to the Federal Court for a judicial review within 30 days of the eligibility notice. Evidence spans paragraphs 19-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4261421` offsets `1612-1619`; context: If required, the reviewing agent would contact the applicant to request any additional supporting documentation; and
on completion of the review, that agent made an independent determination of whether the applicant was eligible for the CRB.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4261421` offsets `19-28`; context: [19] The Officer’s Affidavit describes the general process followed by CRA in validating a CRB application.
- Evidence: `reasoning_application` cue `apply` at chunk `4261421` offsets `1911-1916`; context: The letter would also advise the applicant of their right to apply to the Federal Court for a judicial review within 30 days of the eligibility notice.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4261422` offsets `19-28`; context: [20] The Officer’s Affidavit also deposes that the initial CRA agent and other CRA officers involved in attempting to validate a CRB application set out their findings, notes, and interactions with the applicant in the CRA’s Special Assessment Observations notepad [SA Notepad].
- Evidence: `evidence_fact` cue `affidavit` at chunk `4261423` offsets `399-408`; context: A copy of the Second Review Report is attached as an exhibit to her affidavit and is also found in the certified tribunal record.
- Evidence: `party_position` cue `submit` at chunk `4261425` offsets `127-133`; context: [23] The Second Review Report records that during a March 26, 2021 telephone call the first CRA agent advised the Applicant to submit further documentation as the information she had provided was not sufficient proof of her income.
- Evidence: `party_position` cue `submitted` at chunk `4261426` offsets `92-101`; context: [24] The first CRA agent records, on April 28, 2021, that they reviewed the bank statements submitted by the Applicant for January, February, March and April of 2021.
- Evidence: `evidence_fact` cue `found that` at chunk `4261426` offsets `446-456`; context: The first agent found that the Applicant’s home services appeared to be casual income and not self-employment.
- Evidence: `counterargument_limitation` cue `However` at chunk `4261426` offsets `167-174`; context: However, it could not be determined what income the Applicant earned in 2019, 2020 or in the last 12 months.
- Evidence: `party_position` cue `claimed` at chunk `4261427` offsets `669-676`; context: No invoices were provided for the services, advertising was said to have been by word of mouth and the Applicant claimed she was paid all in cash.
- Evidence: `evidence_fact` cue `found that` at chunk `4261427` offsets `173-183`; context: [25] As to the second review, the Officer records that the Applicant’s 2020 tax assessment and bank statements for December 2020 to April 2021 were reviewed but the Officer found that the Applicant was not eligible for the CRB as she had not established income of at least $5000 prior to the first period of benefits.
- Evidence: `evidence_fact` cue `record` at chunk `4261428` offsets `21-27`; context: [26] In my view, the record demonstrates that the Officer considered all of the documents submitted by the Applicant as well as the Applicant’s explanations as to why these documents did not demonstrate her income during the relevant period.

#### 4649:2:subtheme:4 · paragraphs 27-33

- Raw key terms: `applicant, earned, income, application, states, date, employment, information`
- Display key terms: `earned, income, states, date, employment, information`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: earned, income, states, date, employment, information Position/evidence statements: [27] Thus, contrary to the Applicant’s submissions, I am not persuaded that in conducting the second review the Officer overlooked any information submitted by the Applicant. | [28] Similarly, the Applicant takes issue with the Officer’s statement that the submitted bank statements did not prove the income was earned “prior to March 2020”. Rule/authority context: As I understand her submission, she asserts that in her case the relevant time period for the $5000 minimum income is the 12-month period preceding her first CRB application (pursuant to s. | If a small business owner operates as an individual they bill clients in their own name, if they operate under a registered business name they bill their clients in the business name. Application context: If an applicant did not earn at least $5000 in 2019, they are to be asked if they were working and earned income between January 1, 2020 and the date they applied for the benefit, the source of the income and the amount  Evidence spans paragraphs 27-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4261429` offsets `425-433`; context: Nor does anything turn on the fact that the notes for the second review indicate that the second review started on June 9, 2021 and that a decision letter was sent on June 10, 2021 while the Officer answered “5 days” to the written cross-examination question of how much time she spent in total to review the case and make her decision.
- Evidence: `party_position` cue `submitted` at chunk `4261429` offsets `147-156`; context: [27] Thus, contrary to the Applicant’s submissions, I am not persuaded that in conducting the second review the Officer overlooked any information submitted by the Applicant.
- Evidence: `evidence_fact` cue `record` at chunk `4261429` offsets `651-657`; context: What is relevant is whether the Officer considered all of the documents provided in support of the application and I am satisfied that the record establishes that she did.
- Evidence: `issue` cue `issue` at chunk `4261430` offsets `36-41`; context: [28] Similarly, the Applicant takes issue with the Officer’s statement that the submitted bank statements did not prove the income was earned “prior to March 2020”.
- Evidence: `party_position` cue `submitted` at chunk `4261430` offsets `80-89`; context: [28] Similarly, the Applicant takes issue with the Officer’s statement that the submitted bank statements did not prove the income was earned “prior to March 2020”.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4261430` offsets `340-351`; context: As I understand her submission, she asserts that in her case the relevant time period for the $5000 minimum income is the 12-month period preceding her first CRB application (pursuant to s.
- Evidence: `reasoning_application` cue `applied` at chunk `4261434` offsets `459-466`; context: If an applicant did not earn at least $5000 in 2019, they are to be asked if they were working and earned income between January 1, 2020 and the date they applied for the benefit, the source of the income and the amount earned.
- Evidence: `party_position` cue `submit` at chunk `4261435` offsets `1222-1228`; context: Example 2:
Applicant wants to submit receipts to support that she provided babysitting or child care services.
- Evidence: `governing_rule` cue `under` at chunk `4261435` offsets `315-320`; context: If a small business owner operates as an individual they bill clients in their own name, if they operate under a registered business name they bill their clients in the business name.

#### 4649:2:subtheme:5 · paragraphs 34-48

- Raw key terms: `applicant, income, officer, earned, record, return, review, application`
- Display key terms: `income, officer, earned, return, review`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: income, officer, earned, return, review Position/evidence statements: [39] The Applicant submits that the CRB Guideline does not ask the agent to audit an applicant’s tax return and income. | The Applicant also submits that because her 2020 return has not been audited, then that her self-reported income is implicitly proven and must be accepted as such by the Officer. Rule/authority context: And while tax assessments are one document that could provide income information to CRA with respect to CRB eligibility, they do not “prove” that the Applicant actually earned the income that she reported in filing her i | [43] In conclusion, I am satisfied that the Officer reasonably sought further documentation, consistent with the guidance set out in the CRB Guidelines, and which documents the Applicant was required to provide pursuant  Application context: The Applicant also submits that because her 2020 return has not been audited, then that her self-reported income is implicitly proven and must be accepted as such by the Officer. | The application for judicial review is therefore dismissed. Operative outcome context: I would first note that the Applicant did not assert in her application for judicial review that she had been denied procedural fairness. | The application for judicial review is therefore dismissed. Evidence spans paragraphs 34-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `4261436` offsets `400-408`; context: Further, as is apparent from the record, the requests made to the Applicant for supporting documentation were in keeping with those suggested by the CRB Guideline and the Common Question and Answer “Script” found in the CTR.
- Evidence: `evidence_fact` cue `record` at chunk `4261436` offsets `255-261`; context: Further, as is apparent from the record, the requests made to the Applicant for supporting documentation were in keeping with those suggested by the CRB Guideline and the Common Question and Answer “Script” found in the CTR.
- Evidence: `evidence_fact` cue `evidence` at chunk `4261437` offsets `17-25`; context: [35] There is no evidence to support the Applicant’s position that the Officer was obliged to accept her 2020 income tax assessment as sole and conclusive proof of her income.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4261437` offsets `497-508`; context: And while tax assessments are one document that could provide income information to CRA with respect to CRB eligibility, they do not “prove” that the Applicant actually earned the income that she reported in filing her income tax return, or that her income was earned from an eligible source prior to September 27, 2020, pursuant to ss.
- Evidence: `party_position` cue `submits` at chunk `4261441` offsets `19-26`; context: [39] The Applicant submits that the CRB Guideline does not ask the agent to audit an applicant’s tax return and income.
- Evidence: `counterargument_limitation` cue `but` at chunk `4261441` offsets `134-137`; context: This is true, but the Officer did not purport to conduct an income tax audit.
- Evidence: `party_position` cue `submits` at chunk `4261442` offsets `295-302`; context: The Applicant also submits that because her 2020 return has not been audited, then that her self-reported income is implicitly proven and must be accepted as such by the Officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4261442` offsets `153-161`; context: [40] Thus, contrary to the Applicant’s view, the Officer was not purporting to audit her 2020 income tax return nor is her 2020 tax assessment the “best evidence”, conclusive proof, or CRA confirmation that she earned and received her reported self-employment income in 2020.
- Evidence: `reasoning_application` cue `because` at chunk `4261442` offsets `308-315`; context: The Applicant also submits that because her 2020 return has not been audited, then that her self-reported income is implicitly proven and must be accepted as such by the Officer.
- Evidence: `party_position` cue `assert` at chunk `4261443` offsets `335-341`; context: I would first note that the Applicant did not assert in her application for judicial review that she had been denied procedural fairness.
- Evidence: `evidence_fact` cue `record` at chunk `4261443` offsets `445-451`; context: In any event, the record establishes that the first agent did indicate the type of supporting documents that could be submitted.
- Evidence: `disposition` cue `denied` at chunk `4261443` offsets `399-405`; context: I would first note that the Applicant did not assert in her application for judicial review that she had been denied procedural fairness.
- Evidence: `party_position` cue `submits` at chunk `4261444` offsets `28-35`; context: [42] Finally, the Applicant submits that the CRA took her 2020 income, based on her 2020 tax return, into account when reducing her Canada Child Benefit but disregarded it when reviewing her CRB application.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4261444` offsets `338-347`; context: Further, while the Applicant attaches as an exhibit to her affidavit a document she identifies as a printout of the Canada Child Benefit page from her CRA account, this is not found in the certified tribunal record and the Officer’s Affidavit states that the Officer did not review the document in making her decision as it was not made available to her during her review.
- Evidence: `counterargument_limitation` cue `but` at chunk `4261444` offsets `153-156`; context: [42] Finally, the Applicant submits that the CRA took her 2020 income, based on her 2020 tax return, into account when reducing her Canada Child Benefit but disregarded it when reviewing her CRB application.
- Evidence: `evidence_fact` cue `record` at chunk `4261445` offsets `1028-1034`; context: The Applicant did not provide any documentation which might have identified the clients for whom she provided services, the dates on which those services were provided and a description of the services, the hourly rate she billed for her services, her record keeping of the provision of those services and amount and form of payment received for the services, or any documentation whatsoever to demonstrate that she actually performed the services and was paid for them.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4261445` offsets `211-222`; context: [43] In conclusion, I am satisfied that the Officer reasonably sought further documentation, consistent with the guidance set out in the CRB Guidelines, and which documents the Applicant was required to provide pursuant to s.
- Evidence: `party_position` cue `claimed` at chunk `4261446` offsets `250-257`; context: [44] The record also establishes that the Officer considered the documentation that was provided by the Applicant but found that it was insufficient to prove that the Applicant had actually earned and received $5350 in business income in 2020 as she claimed.
- Evidence: `evidence_fact` cue `record` at chunk `4261446` offsets `9-15`; context: [44] The record also establishes that the Officer considered the documentation that was provided by the Applicant but found that it was insufficient to prove that the Applicant had actually earned and received $5350 in business income in 2020 as she claimed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4261447` offsets `392-400`; context: Based on the reasons, the evidence and record before me, I am not satisfied that the Applicant has met her burden.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4261447` offsets `244-250`; context: In that regard, the Court must be satisfied “that there are sufficiently serious short comings in the decision such that it cannot be said to exhibit the requisite degree of justification, transparency and intelligibility” (Vavilov at para 100).
- Evidence: `reasoning_application` cue `therefore` at chunk `4261448` offsets `118-127`; context: The application for judicial review is therefore dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4261448` offsets `128-137`; context: The application for judicial review is therefore dismissed.
- Evidence: `party_position` cue `submit` at chunk `4261449` offsets `111-117`; context: [47] The Respondent requested costs in the event that the application is dismissed and that it be permitted to submit a draft bill of costs and related submissions in support of this.
- Evidence: `reasoning_application` cue `accordingly` at chunk `4261449` offsets `331-342`; context: In my view, this was not a complex matter and it would be preferable if the parties could arrive at an agreed lump sum figure and advise the Court accordingly so that a reflective order as to costs may be issued.
- Evidence: `disposition` cue `dismissed` at chunk `4261449` offsets `73-82`; context: [47] The Respondent requested costs in the event that the application is dismissed and that it be permitted to submit a draft bill of costs and related submissions in support of this.

#### Section text

[11] The decision states:
We are writing to advise you of our decision regarding your request dated April 6, 2021, for a second review of your Canada Recovery Benefit (CRB) application.
Based on our review, you are not eligible.
You did not meet the following criteria:
You did not earn at least $5,000 (before taxes) of employment or net self-employment income in 2019, 2020, or in the 12 months before the date of your first application.
As you did not meet the eligibility criteria to qualify for CRB, any future CRB applications will be denied, unless you can provide proof that you are able to satisfy the eligibility criteria.
If you received a CRB payment that you were not eligible for, you will be required to repay the amount.

[12] The Second Decision also indicated that if the Applicant disagreed with the decision she could apply to this Court for judicial review within 30 days of the date of the letter.
Relevant Legislation
Canada Recovery Benefits Act, SC 2020, c 12, s 2 [CRB Act, or the Act]
Definitions
2 The following definitions apply in this Act.
COVID-19 means the coronavirus disease 2019. (COVID-19)
Her Majesty means Her Majesty in right of Canada. (Sa Majesté)
……
Minister means the Minister of Employment and Social Development. (ministre)
Eligibility
3(1) A person is eligible for a Canada recovery benefit for any two-week period falling within the period beginning on September 27, 2020 and ending on October 23, 2021 if
…
(d) in the case of an application made under section 4 in respect of a two-week period beginning in 2020, they had, for 2019 or in the 12-month period preceding the day on which they make the application, a total income of at least $5,000…
(e) in the case of an application made under section 4 by a person other than a person referred to in paragraph (e.1) in respect of a two-week period beginning in 2021, they had, for 2019 or for 2020 or in the 12-month period preceding the day on which they make the application, a total income of at least $5,000 from the sources referred to in subparagraphs (d)(i) to (v);
…
(i) they sought work during the two-week period, whether as an employee or in self-employment;
…
Income from self-employment
(2) For the purpose of paragraphs (1)(d) to (f), income from self-employment is revenue from the self-employment less expenses incurred to earn that revenue.
Application
4(1) A person may, in the form and manner established by the Minister, apply for a Canada recovery benefit for any two-week period falling within the period beginning on September 27, 2020 and ending on October 23, 2021.
(2) No application is permitted to be made on any day that is more than 60 days after the end of the two-week period to which the benefit relates.
Attestation
5 (1) Subject to subsections (2) to (5), a person must, in their application, attest that they meet each of the eligibility conditions referred to in paragraphs 3(1)(a) to (n).
Exception — paragraphs 3(1)(d) and (e)
(2) A person is not required to attest to their income under paragraphs 3(1)(d) and (e) if they have previously received any benefit under this Act and they attest to that fact.
Obligation to provide information
6 An applicant must provide the Minister with any information that the Minister may require in respect of the application.
Payment of benefit
7 The Minister must pay a Canada recovery benefit to a person who makes an application under section 4 and who is eligible for the benefit.
Preliminary Matter

[13] As a preliminary matter, the Respondent’s written submissions indicated that the Minister of National Revenue is improperly named as the respondent in this application for judicial review. Counsel for the Respondent submits that because the Minister of National Revenue is not directly affected by the decision, which was made by the CRA on behalf of the Minister of Employment and Social Development, the proper responding party is the Attorney General of Canada, in accordance with Rule 303 of the Federal Courts Rules, SOR/98-106.

[14] At the hearing of this matter the Applicant advised that she agreed with the Respondent on this point, as do I. Accordingly, I will order that the style of cause will be amended, replacing the Minister of National Revenue with the Attorney General of Canada as the named respondent (Hasselsjo v Canada (Attorney General), 2021 CanLII 89551 (FC) at para 2).
Issues and Standard of Review

[15] While the Applicant makes various submissions in support of her view that the Second Decision was unreasonable, unfair, not transparent, unintelligible, unjustified and failed to consider the harsh impact it had on her livelihood, having reviewed her submissions in whole, it is my view that the sole issue in this matter is whether the Second Decision was reasonable.

[16] The parties submit and I agree that the standard of review applicable to the merits of the decision is reasonableness (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov].
Analysis

[17] The essence of the Applicant’s submissions is that it was unreasonable for the Officer to disregard and not to accept her 2020 Notice of Assessment, as issued by CRA, and the CRA 2020 Assessment printed from the Applicant’s CRA MyAccount webpage, as proof that she earned $5350 in net self-employment income. She submits that, based on those documents, she established that she met the $5000 minimum income criteria and was therefore eligible to apply for and receive the CRB. According to the Applicant, refusing to accept her income tax assessment as sufficient proof of income and instead requiring additional proof that the required income was earned and received runs contrary to the CRB Act’s purpose of supporting Canada’s economic recovery in response to the COVID-19 pandemic.

[18] The Respondent has filed the affidavit of Ms. Christine Perun, a CRA benefits compliance agent and the person who made the Second Decision, sworn on September 10, 2021 [Officer’s Affidavit]. The Applicant issued a written cross-examination of the Officer based on her affidavit and received the Officer’s written answers which were affirmed on October 1, 2021.

[19] The Officer’s Affidavit describes the general process followed by CRA in validating a CRB application. This includes that:
upon application, the applicant would receive a message advising them that their application was being reviewed and providing them with a toll-free number to call;
the applicant would call the CRA and speak to a Canada Emergency Benefit Validation agent;
the agent would go over the CRB’s eligibility requirements with the applicant and attempt to determine if they met the criteria. Attached as Exhibit “A” of the Officer’s Affidavit is a document entitled “Confirming CERB, CRB, CRSB or CRCB Eligibility” [CRB Guideline] which document the Officer deposes was used by CRA agents to guide them in determining if an applicant was eligible for the CRB;
if necessary, the agent could also request any additional documents or information from the applicant prior to determining their CRB eligibility;
if the applicant was found to be ineligible for the CRB, the agent would then notify them by letter which letter also advised the applicant of their right to have the decision reviewed by another CRA agent, the second review;
if an applicant requested a second review, the matter would be assigned to a new CRA agent who had not previously been involved. The reviewing agent would review the available information, including any fresh documentation and submissions provided by the applicant. If required, the reviewing agent would contact the applicant to request any additional supporting documentation; and
on completion of the review, that agent made an independent determination of whether the applicant was eligible for the CRB. If the applicant was found to be ineligible, a report detailing the reasons for the denial would be prepared and the applicant would be notified of the reviewing agent’s decision by letter. The letter would also advise the applicant of their right to apply to the Federal Court for a judicial review within 30 days of the eligibility notice.

[20] The Officer’s Affidavit also deposes that the initial CRA agent and other CRA officers involved in attempting to validate a CRB application set out their findings, notes, and interactions with the applicant in the CRA’s Special Assessment Observations notepad [SA Notepad].

[21] The Officer states that, in this matter, relevant entries from the SA Notepad, including the entries that she made, are reproduced in the “SA Database Observations” section of the Second Review Report, Case Analysis for CRB [Second Review Report], that she prepared after the Applicant was found to be ineligible for the CRB. A copy of the Second Review Report is attached as an exhibit to her affidavit and is also found in the certified tribunal record.

[22] I note that, similar to Global Case Management System notes utilized by immigration officers, the Second Review Report forms part of the reasons for the Officer’s decision (Sedoh v Canada (Citizenship and Immigration), 2021 FC 1431 at para 36; Ezou v Canada (Citizenship and Immigration), 2021 FC 251 at para 17; McClintock's Ski School & Pro Shop Inc. v. Canada (Attorney General), 2021 FC 471 at para 26; Vavilov at paras 94-98).

[23] The Second Review Report records that during a March 26, 2021 telephone call the first CRA agent advised the Applicant to submit further documentation as the information she had provided was not sufficient proof of her income. During a April 4, 2021 call the Applicant (through her husband) was asked if she had had receipts or invoices for the services she provided and was told that none were available as the Applicant had been paid in cash for everything. Asked how the Applicant was advertising her services, the agent was advised that this was by word of mouth. Asked if bank statements could be submitted to show the alleged loss of income, the response was that they could be submitted but that the Applicant and her spouse shared a joint account and most of her income was not deposited into her personal account until one was opened for her in November 2020.

[24] The first CRA agent records, on April 28, 2021, that they reviewed the bank statements submitted by the Applicant for January, February, March and April of 2021. However, it could not be determined what income the Applicant earned in 2019, 2020 or in the last 12 months. The Applicant had reported that she was paid in cash for all of her services and she advertises her business by word of mouth through family and friends. The first agent found that the Applicant’s home services appeared to be casual income and not self-employment. The first agent concluded that the Applicant’s documents did not support the $5000 eligibility criteria and were insufficient.

[25] As to the second review, the Officer records that the Applicant’s 2020 tax assessment and bank statements for December 2020 to April 2021 were reviewed but the Officer found that the Applicant was not eligible for the CRB as she had not established income of at least $5000 prior to the first period of benefits. The bank statements provided by the Applicant showed only a few transfers in and out of the bank account and there was nothing to confirm who this money was received from, nor did this prove that the money was earned prior to March 2020. No invoices were provided for the services, advertising was said to have been by word of mouth and the Applicant claimed she was paid all in cash. The second review notes state that, in order for the Applicant to be eligible, CRA would need bank statements and invoices to coincide with the amounts (claimed as earned income) as well as proof that the Applicant was continuing to look for work. A breakdown of the expenses of the company would also be required. The Officer found that the Applicant was not eligible for the CRB as the Applicant stated that she cannot provide the necessary documentation to confirm her income.

[26] In my view, the record demonstrates that the Officer considered all of the documents submitted by the Applicant as well as the Applicant’s explanations as to why these documents did not demonstrate her income during the relevant period. Moreover, in the written cross-examination of the Officer, the Applicant asked why the Officer “did not consider Maria Aryan’s letters and explanations in the course of your review”. The Officer responded that the review was document driven and that the letters were considered but they did not provide the information needed to support the Applicant’s claimed earned income.

[27] Thus, contrary to the Applicant’s submissions, I am not persuaded that in conducting the second review the Officer overlooked any information submitted by the Applicant. Nor does anything turn on the fact that the notes for the second review indicate that the second review started on June 9, 2021 and that a decision letter was sent on June 10, 2021 while the Officer answered “5 days” to the written cross-examination question of how much time she spent in total to review the case and make her decision. What is relevant is whether the Officer considered all of the documents provided in support of the application and I am satisfied that the record establishes that she did.

[28] Similarly, the Applicant takes issue with the Officer’s statement that the submitted bank statements did not prove the income was earned “prior to March 2020”. As I understand her submission, she asserts that in her case the relevant time period for the $5000 minimum income is the 12-month period preceding her first CRB application (pursuant to s. 3(1)(d) of the CRB Act), which was for the two-week period commencing on September 27, 2020. In my view, while the Officer could have been more precise in identifying the relevant period, again, nothing turns on this point. The Officer’s relevant finding was that the submitted bank statements, detailing cash and e-transfer deposits between November 2020 and May 2021, do not prove the source of the amounts deposited nor when they were earned. This is so regardless of whether the relevant earning period was the 12-month period “prior to March 2020” or prior to September 27, 2020.

[29] Further, in my view, the Applicant’s main submission, being that the Officer was obliged to accept her 2020 income tax assessment as proof of her earned income cannot succeed.

[30] First, section 6 of the CRB Act explicitly states that an applicant must provide the Minister of Employment and Social Development with any information that the Minister may require in respect of the application.

[31] Second, the CRA Guideline addresses the proof needed to establish the $5000 minimum income that an applicant must have earned to be eligible to receive the CRB. The CRB Guideline states that to be eligible for the benefits an applicant must have earned a minimum of $5000 in 2019 or within the 12 months prior to the date of their application. Agents are to use their “judgement, experience and expertise” in deciding if proof is required. If the applicant is unable to provide any of the documents suggested, agents are to work with them to see what other acceptable documents they may have.

[32] The CRB Guideline states that income must be from employment or self-employment. This can be established by review of the 2019 income tax return, including self-employment income indicated on lines 13499 to 14299 (gross income) and lines 13500 to 14300 (net income) of their 2019 income tax return. If an applicant did not earn at least $5000 in 2019, they are to be asked if they were working and earned income between January 1, 2020 and the date they applied for the benefit, the source of the income and the amount earned. The document instructs that “If you determine that documentation is required, advise the applicant what needs to be provided to show they made at least $5000 in the last 12 months”.

[33] As to self-employment income, the document states:
Self-employment income
Small business owners can receive income from their business in different ways, including as salary, business income or dividends.
If a small business owner operates as an individual they bill clients in their own name, if they operate under a registered business name they bill their clients in the business name. If the business has a name other than their own, there should be a separate bank account.
Things to consider for small business owners:
- Do they have business cards to promote their business?
- Do they advertised? E.g. Kijiji, Marketplace, Craigslist, their own website?
- Do they actively seek employment opportunities?
- Do they have a registered BN?
- Do they perform regular work and provide to non-related persons?
- If they are always paid in cash, do they have proof they keep track of hours and payments?
Example 1:
Applicant wants to include ‘dog walking’ services as income. They should be able to produce invoices (in real time) to their clients that show the date of the service, the name of the client (type of animal or number of animals), cost of service, type of payment received.
Example 2:
Applicant wants to submit receipts to support that she provided babysitting or child care services. Any receipts or invoices they have should include the name of the parent, names of the children and address of the person they provided the service too. The applicant’s information (including SIN) should be provided on the receipt so the individual could claim child care expenses.
……..
Acceptable proof:
- Invoice for services rendered, for self employed individuals or sub contractors. For example an invoice for painting a house or a cleaning service etc. Must include the date of the service, who the service was for, and the applicant’s or company’s name.
- Documentation for receipt of payment for the service provided, e.g. statement of account, or bill of sale showing a payment and the remaining balance owed
- Documentation showing income is earned from carrying on a "trade or business" as a-sole proprietor, an independent contractor, or some form of partnership
- Contracts
- A list of expenses to support the net result of earnings
- Proof of advertising
- Any other documentation that will substantiate $5,000.00 in self employment income

[34] Given this, it was open to the first CRA agent to request additional documentation from the Applicant to establish an earned minimum income of $5000, in the relevant period, as an eligibility requirement for the CRB. Further, as is apparent from the record, the requests made to the Applicant for supporting documentation were in keeping with those suggested by the CRB Guideline and the Common Question and Answer “Script” found in the CTR.

[35] There is no evidence to support the Applicant’s position that the Officer was obliged to accept her 2020 income tax assessment as sole and conclusive proof of her income. And while tax assessments are one document that could provide income information to CRA with respect to CRB eligibility, they do not “prove” that the Applicant actually earned the income that she reported in filing her income tax return, or that her income was earned from an eligible source prior to September 27, 2020, pursuant to ss. 3(1)(d)(i-v) of the CRB Act.

[36] In her answers to the written cross-examination, the Officer states that she did consider the income claimed on the Applicant’s 2020 tax assessment, however, that CRA requires documents to support the Applicant’s income amount claimed on her return. Further, agents are trained not to take the taxpayer filing their tax return as sole proof of income. She explained this by stating that “Filing a tax return is a self-assessed document and we as reviewers are required to ensure that this income was in fact earned and received by the taxpayer as would be the same in an audit procedure”.

[37] When as

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]

