# Discussion Units: case 25626

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **24**
- Continuity pairs: **23**
- Discussion Units: **2**
- Paragraph source hashes: **24**
- Sub-themes: **3**

## 25626:1 · paragraphs 0-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e4aadd23c0e0e83e7e4aee1ab2f42cf3feb2d9ae42b99f5e5bb7376fae8248df`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25626:1:subtheme:1 · paragraphs 0-14

- Raw key terms: `canada, applicant, decision, india, officer, visa, work, application`
- Display key terms: `india, officer, visa, work`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, reasoning_application Display terms: india, officer, visa, work Application context: The reasons issued in this case apply equally to the companion file and a copy will be placed on that file. | The motion was therefore dismissed and the application heard on the merits. Operative outcome context: For the reasons that follow, the applications are granted. | The motion was therefore dismissed and the application heard on the merits. Evidence spans paragraphs 0-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5206049` offsets `433-441`; context: The applicant challenges the decision on the basis of breach of procedural fairness, reviewable on a standard of correctness, and on the basis that the Officer’s decision cannot be sustained when assessed against a reasonableness standard for failing to take certain evidence into account.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5206049` offsets `337-343`; context: The applicant challenges the decision on the basis of breach of procedural fairness, reviewable on a standard of correctness, and on the basis that the Officer’s decision cannot be sustained when assessed against a reasonableness standard for failing to take certain evidence into account.
- Evidence: `reasoning_application` cue `apply` at chunk `5206050` offsets `171-176`; context: The reasons issued in this case apply equally to the companion file and a copy will be placed on that file.
- Evidence: `disposition` cue `granted` at chunk `5206050` offsets `297-304`; context: For the reasons that follow, the applications are granted.
- Evidence: `reasoning_application` cue `therefore` at chunk `5206052` offsets `357-366`; context: The motion was therefore dismissed and the application heard on the merits.
- Evidence: `disposition` cue `dismissed` at chunk `5206052` offsets `367-376`; context: The motion was therefore dismissed and the application heard on the merits.
- Evidence: `reasoning_application` cue `applied` at chunk `5206053` offsets `29-36`; context: [5] Shyam and Shalik Chhetri applied to the High Commission in India for a Canadian temporary work visa (TWV).
- Evidence: `evidence_fact` cue `EVIDENCE` at chunk `5206055` offsets `869-877`; context: 00 CAD ABILITY IN ENGLISH IS REQUIRED — NO EVIDENCE PRESENTED THAT APPLICANT HAS THE ABILITY.
- Evidence: `disposition` cue `denied` at chunk `5206055` offsets `27-33`; context: [7] Both applications were denied by the Visa Officer at the High Commission in India, in November 2010.
- Evidence: `evidence_fact` cue `EVIDENCE` at chunk `5206056` offsets `777-785`; context: 00 CAD ABILITY IN ENGLISH IS REQUIRED — NO EVIDENCE PRESENTED THAT APPLICANT HAS THE ABILITY.
- Evidence: `evidence_fact` cue `evidence` at chunk `5206060` offsets `959-967`; context: It was not reasonable for the Officer, without a stronger method of comparison such as cost of living between the Applicant’s presumed low income in India and earnings in Canada, to presume overstay based on this factor especially since the evidence before the Officer indicated that the Applicant while in India had some assets to his name.
- Evidence: `reasoning_application` cue `therefore` at chunk `5206060` offsets `1275-1284`; context: Further, while economic incentive to stay in Canada is a reasonable consideration on the part of the Officer, the majority of applicants would have some economic incentive to come work in Canada, and this incentive therefore cannot so easily correlate with overstay since it is inconsistent with the work permit scheme.
- Evidence: `reasoning_application` cue `applied` at chunk `5206061` offsets `29-36`; context: [13] This principle has been applied in other decisions of this Court: Cao v Canada (Citizenship and Immigration), 2010 FC 941, per Justice Martineau; Khatoon v Canada (Citizenship and Immigration), 2008 FC 276, per Justice Temblay-Lamer; Dhanoa v Canada (Citizenship and Immigration), 2009 FC 729, per Justice Harrington; and Rengasamy v Canada (Citizenship and Immigration), 2009 FC 1229, per Justice O'Reilly.
- Evidence: `evidence_fact` cue `evidence` at chunk `5206062` offsets `447-455`; context: It is only through objective evidence of countervailing strong social and economic links to the home country that the onus to establish an intent to return be discharged.
- Evidence: `reasoning_application` cue `therefore` at chunk `5206062` offsets `21-30`; context: [14] The focus must, therefore, be on the strength of ties to the home country.
- Evidence: `counterargument_limitation` cue `but` at chunk `5206062` offsets `373-376`; context: In this sense the relative economic advantage is a necessary component of the decision, but it is not the only part of the analysis.

#### 25626:1:subtheme:2 · paragraphs 15-21

- Raw key terms: `officer, visa, applicants, canada, employment, applicant, application, citizenship`
- Display key terms: `officer, visa, employment`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: officer, visa, employment Position/evidence statements: The Officer also noted deficiencies in the proof of prior employment by the same proposed employer, but the basis on which she decided that the pay records submitted were not genuine, is unclear. Application context: [19] To conclude on the reasonableness of the decision, it will be recalled that the Officer decided that the applicants could seek “to remain in Canada by any means on completion of the offered employment”. Operative outcome context: [21] For these reasons, this application for judicial review is granted and the matter remitted to a different visa officer for re-determination. Evidence spans paragraphs 15-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5206063` offsets `190-198`; context: There were however further aspects of the Officer’s decision which call its reasonableness into question.
- Evidence: `evidence_fact` cue `record` at chunk `5206063` offsets `319-325`; context: The Officer wrote that it was “not clear if the employer is a Canadian citizen and why he is going to Canada”, yet the record included a letter from the employer that he was the Chief Executive Officer of Husky Oil, resident in Calgary.
- Evidence: `counterargument_limitation` cue `however` at chunk `5206063` offsets `105-112`; context: There were however further aspects of the Officer’s decision which call its reasonableness into question.
- Evidence: `counterargument_limitation` cue `However` at chunk `5206065` offsets `398-405`; context: However, in this case, there was no analysis by the Officer upon which she concluded that the applicants did not possess the requisite English language ability as necessitated by the job requirements.
- Evidence: `party_position` cue `submitted` at chunk `5206066` offsets `306-315`; context: The Officer also noted deficiencies in the proof of prior employment by the same proposed employer, but the basis on which she decided that the pay records submitted were not genuine, is unclear.
- Evidence: `evidence_fact` cue `found that` at chunk `5206067` offsets `296-306`; context: In Do v Canada (Minister of Citizenship and Immigration), 2004 FC 1269 the visa officer found that the job offer was submitted to help the applicant gain access to Canada so that he could eventually sponsor his family members.
- Evidence: `reasoning_application` cue `conclude` at chunk `5206067` offsets `8-16`; context: [19] To conclude on the reasonableness of the decision, it will be recalled that the Officer decided that the applicants could seek “to remain in Canada by any means on completion of the offered employment”.
- Evidence: `counterargument_limitation` cue `However` at chunk `5206068` offsets `415-422`; context: However, assessing the decision as a whole, it does not meet the required standards of justification and intelligibility as set forth in Khosa v Canada (Citizenship and Immigration), 2010 FC 83.
- Evidence: `disposition` cue `granted` at chunk `5206069` offsets `64-71`; context: [21] For these reasons, this application for judicial review is granted and the matter remitted to a different visa officer for re-determination.

#### Section text

Chhetri v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-07-12
Neutral citation
2011 FC 872
File numbers
IMM-6943-10, IMM-6944-10
Decision Content
Federal Court
Cour fédérale
Date: 20110712
Docket: IMM-6943-10
IMM-6944-10
Citation: 2011 FC 872
Ottawa, Ontario, July 12, 2011
PRESENT: The Honourable Mr. Justice Rennie
BETWEEN:
IMM-6943-10
SHYAM THAPA CHHETRI
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
AND
IMM-6944-10
SHALIK RAM THAPA CHHETRI
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicant seeks to set aside a decision of a Visa Officer at the High Commission in New Delhi, India refusing an application for a temporary work visa (TWV). The applicant challenges the decision on the basis of breach of procedural fairness, reviewable on a standard of correctness, and on the basis that the Officer’s decision cannot be sustained when assessed against a reasonableness standard for failing to take certain evidence into account.

[2] This application was heard at the same time as that of Shalik Chhetri v. Canada (Minister of Citizenship and Immigration) IMM-6944-10. The reasons issued in this case apply equally to the companion file and a copy will be placed on that file. For the reasons that follow, the applications are granted.
Preliminary Motion

[3] At the outset of this hearing the respondent Minister moved to have the applications struck on the grounds that they were moot. The applicants had, subsequent to the rejection of their application for a TWV, reapplied. Those applications had also been rejected and judicial review had been commenced of those decisions.

[4] In my view, the existing applications are not moot. The second refusal did not insulate the first decision from review. There remains a live controversy between the parties as to adequacy of the reasons for rejecting the application. There remains a lis between the parties and the fact is that this decision could have practical effect. The motion was therefore dismissed and the application heard on the merits.
Facts

[5] Shyam and Shalik Chhetri applied to the High Commission in India for a Canadian temporary work visa (TWV). The applications were based on an October 5, 2010 positive labour market opinion (LMO) provided by Service Canada in respect of positions as “Domestic Servants” to the Chief Executive Officer of Husky Oil and Gas, Mr. Asim Ghosh, who is located in Calgary, Alberta. In letters to the High Commission in India Mr. Ghosh wrote that the applicants’ work duties would include: “…preparing all meals in the three Indian cuisines of Behgali, U.P. and South Indian, shopping for food, laundry, ironing, cleaning the residence, serving daily meals, serving and assisting with entertainment, household maintenance including janitorial, gardening, pruning, grass cutting, snow removal, grooming and exercising of pets, and car washing.”

[6] Mr. Ghosh further advised that both Shyam and Shalik had in the past worked for him in these positions. Attached to the applicants’ applications were photocopies of entries from a ledger which showed past employment with Mr. Ghosh. The applicants were to be paid $13.72 per hour and scheduled to work 40 hours per week. They were to be provided with 10 weeks of paid vacation, as well as medical and dental benefits. The duration of the employment contract was one year. While transportation costs from India to Calgary would be borne by Mr. Ghosh, accommodation upon arrival would not.

[7] Both applications were denied by the Visa Officer at the High Commission in India, in November 2010. The Visa Officer wrote in her decision regarding Shyam:
“DIVORCED MALE TO WORK AS DOMESTIC SERVANT IN CANADA. PREVIOUS EXPERIENCE IN HOME OF POTENTIAL EMPLOYER IN INDIA SINCE 1999. NOT CLEAR IF EMPLOYER IS CANADIAN CITIZEN OR PERMANENT RESIDENT AND WHY HE IS GOING TO CANADA. LETTER ON FILE FROM EMPLOYER THAT HE IS FAMILIAR WITH APPLICANT WORK AS HE HAS BEEN EMPLOYED AT. HIS RESIDENCE IN INDIA. HAS SUBMITTED COPY OF NOTEBOOK PAGES DATED MAY 07- SEP 10 WHICH APPEARS TO BE SALARY PAID BUT NO INDICATION OF NAME, SIGNATURE OF RECEIPT APPEARS TO BE THAT OF APPLICANT. SALARY PER MONTH RANGES FROM 6000INR/MONTH (130.00 CAD) — 80001N1{ (186.00) SALARY TO BE PAID 13.72/HOUR X 40 HOURS PER WEEK X 52 WEEKS PER YEAR = 28537.00 CAD ABILITY IN ENGLISH IS REQUIRED — NO EVIDENCE PRESENTED THAT APPLICANT HAS THE ABILITY. APPLICANT IS CITIZEN OF NEPAL WHO APPEARS TO HAVE BEEN IN INDIA FOR 12 YEARS. MOTHER AND SIBLINGS LIVE IN NEPAL YET PASSPORT ISSUED 2002 SHOWS NO TRAVEL BACK. NOTE THAT THERE IS A STARK CONTRAST IN WAGES AND WORKING CONDITIONS BETWEEN CANADA AND INDIA. IN ADDITION TO DIFFICULT LIVING AND WORKING CONDITIONS AND LIMITED PROSPECTS FOR ADVANCEMENT IN INDIA FOR PERSONS IN THIS PROFESSION, THERE IS A STRONG INCENTIVE FOR THIS APPLICANT TO REMAIN IN CANADA BY ANY MEANS ON COMPLETION OF THE OFFERED EMPLOYMENT. THIS IS ESPECIALLY TRUE GIVEN THAT THE APPLICANT HAS NO TIES TO INDIA AND WEAK TIES TO NEPAL. NOT SATISFIED APPLICANT NO T HAS A GENUINE TEMP PURPOSE FOR TRAVEL TO CANADA NOT SATISFIED MEETS REQUIREMENTS OF R200(1)(B) REFUSED.”

[8] And in respect of her decision regarding Shalik, the officer wrote:
“MARRIED MALE TO WORK AS DOMESTIC SERVANT IN CANADA. PREVIOUS EXPERIENCE IN HOME OF POTENTIAL EMPLOYER IN INDIA SINCE 1999. NOT CLEAR IF EMPLOYER IS CANADIAN CITIZEN OR PERMANENT RESIDENT AND WHY HE IS GOING TO CANADA. LETTER ON FILE FROM EMPLOYER THAT HE IS FAMILIAR WITH APPLICANT WORK AS HE HAS BEEN EMPLOYED AT HIS RESIDENCE IN INDIA. HAS SUBMITTED COPY OF NOTEBOOK PAGES DATED MAY 07- SEP 10 WHICH APPEARS TO BE SALARY PAID BUT NO INDICATION OF NAME, SIGNATURE OF RECEIPT APPEARS TO BE THAT OF APPLICANT. SALARY PER MONTH RANGES FROM S500LNRIMONTH (130.00 CAD) — 8000INR (186.00) SALARY TO BE PAID 13.72/HOUR X 40 HOURS PER WEEK X 52 WEEKS PER YEAR = 28537.00 CAD ABILITY IN ENGLISH IS REQUIRED — NO EVIDENCE PRESENTED THAT APPLICANT HAS THE ABILITY. APPLICANT IS CITIZEN OF NEPAL WHO APPEARS TO HAVE BEEN IN INDIA FOR 12 YEARS. MOTHER, WIFE AND TWO CHILDREN LIVE IN NEPAL YET PASSPORT ISSUED 2009 SHOWS NO TRAVEL BACK. NOTE THAT THERE IS A STARK CONTRAST IN WAGES AND WORKING CONDITIONS BETWEEN CANADA AND INDIA. IN ADDITION TO DIFFICULT LIVING AND WORKING CONDITIONS AND LIMITED PROSPECTS FOR ADVANCEMENT IN INDIA FOR PERSONS IN THIS PROFESSION, THERE IS A STRONG INCENTIVE FOR THIS APPLICANT TO REMAIN IN CANADA BY ANY MEANS ON COMPLETION OF THE
OFFERED EMPLOYMENT. THIS IS ESPECIALLY TME GIVEN THAT THE APPLICANT HAS NO TIES TO INDIA AND WEAK TIES TO NEPAL. NOT SATISFIED APPLICANT NO T HAS A GENUINE TEMP PURPOSE FOR TRAVEL TO CANADA NOT SATISFIED MEETS REQUIREMENTS OF R200(1)(B) REFUSED.”

[9] Decisions of visa officers in their assessment of the facts and the weight to be accorded criteria relevant to temporary work visas are entitled to considerable deference. The combined effect of section 11(1) of the Immigration and Refugee Protection Act, 2001, c. 27 (IRPA) and Division 3 of Part 11 of the Immigration and Refugee Protection Regulations (SOR/2002-227) (the Regulations) is to require visa officers to be satisfied that the individuals are not inadmissible and that they will leave Canada on expiry of their visa. It is often over-looked that it must be “established” that the foreign national will leave at the end of their visa. The combined effect of the IRPA and the Regulations does not leave much room for officers to give the applicant the benefit of the doubt; rather there is a positive obligation that it be established that the foreign national will leave before the visa be issued.

[10] Foreign nationals are entitled to the minimum degree of procedural fairness. There is no obligation on the visa officer to advise the applicant of concerns about, or deficiencies in, their application or to offer an interview. Nor, as Rothstein J.A. (ex officio) said in Qin v Canada (Minister of Citizenship and Immigration), 2002 FCT 815, does the onus shift to the visa officer to take any additional steps to address or satisfy outstanding concerns. The foreign national has no right or interest at play. It is for these reasons that it is often difficult to set aside, on judicial review, a visa officer’s decision.

[11] This, however, is one of those rare cases where the decision cannot stand. The Visa Officer premised her decision on what has been determined by this Court to be an irrelevant criteria, namely “… the stark contrast in wages and working conditions between Canada and India.” This, in the Visa Officer’s opinion, meant that “there was a strong incentive for the applicant to remain in Canada by any means following on completion of the offered employment.”

[12] The possibility of financial betterment or career experience cannot, in and of itself, constitute a valid reason for rejecting an application. As has been pointed out in a number of decisions, these are the factors that motivate potential applicants. The very reasons for coming, and the catalyst which makes the TWV program viable cannot be a reason for rejecting applicants. In Minhas v Canada (Citizenship and Immigration), 2009 FC 696, Justice Tremblay-Lamer held:
… difference in salaries between India and Canada may indicate incentive to stay only when the cost of living is also considered. Standard of living in the home country is also important to determining where the Applicant may be better off [].
It was not reasonable for the Officer, without a stronger method of comparison such as cost of living between the Applicant’s presumed low income in India and earnings in Canada, to presume overstay based on this factor especially since the evidence before the Officer indicated that the Applicant while in India had some assets to his name.
Further, while economic incentive to stay in Canada is a reasonable consideration on the part of the Officer, the majority of applicants would have some economic incentive to come work in Canada, and this incentive therefore cannot so easily correlate with overstay since it is inconsistent with the work permit scheme.

[13] This principle has been applied in other decisions of this Court: Cao v Canada (Citizenship and Immigration), 2010 FC 941, per Justice Martineau; Khatoon v Canada (Citizenship and Immigration), 2008 FC 276, per Justice Temblay-Lamer; Dhanoa v Canada (Citizenship and Immigration), 2009 FC 729, per Justice Harrington; and Rengasamy v Canada (Citizenship and Immigration), 2009 FC 1229, per Justice O'Reilly.

[14] The focus must, therefore, be on the strength of ties to the home country. Visa officers must assess the strength of the ties that bind or pull the applicant to their home country against the incentives, economic and otherwise, that might induce the foreign national to overstay. In this sense the relative economic advantage is a necessary component of the decision, but it is not the only part of the analysis. It is only through objective evidence of countervailing strong social and economic links to the home country that the onus to establish an intent to return be discharged.

[15] As noted, the economic incentives played a determinative role in the Officer’s decision. There were however further aspects of the Officer’s decision which call its reasonableness into question. The Officer wrote that it was “not clear if the employer is a Canadian citizen and why he is going to Canada”, yet the record included a letter from the employer that he was the Chief Executive Officer of Husky Oil, resident in Calgary. The Officer noted that there was no evidence of English language ability as required by the Labour Market Opinion, yet there was a letter from the employer confirming the ability of the applicants to fulfill all the requirements of the position. While this letter does not displace or bind the Visa Officers’ assessment of the language skill or requirement in any way, it was nevertheless some evidence which was before the Officer when the Officer concluded that there was no evidence. Whether it constitutes sufficient evidence is another matter for another day, but that letter, to the extent that it is evidence, needed to be considered and assessed in the context of the proposed employment.

[16] The duties for the position did not require the applicants to have a fluent understanding of English as confirmed by the LMO. The job duties were almost wholly related to work in Mr. Ghosh’s private residence and did not involve or require any meaningful interactions with the public. As stated in Chen v Canada (Minister of Citizenship and Immigration [2005] FCJ No 1674, visa officers may determine that an applicant requires language requirements independent or different than those set forth in the LMO if relevant to performance of the job duties.

[17] In the discharge of their responsibilities, visa officers can consider any factor relating to the bona fides of the both the employment offer and the bona fides of the employee. The LMO is not determinative of how the discretion will be exercised. It is a procedural pre-condition to the exercise of the discretion, and part of the factual landscape against which the application is assessed. However, in this case, there was no analysis by the Officer upon which she concluded that the applicants did not possess the requisite English language ability as necessitated by the job requirements.

[18] In assessing the strength of family ties to Nepal, the Officer, in respect of the applicant Shyam, overlooked the existence of a child in Nepal. The Officer also noted deficiencies in the proof of prior employment by the same proposed employer, but the basis on which she decided that the pay records submitted were not genuine, is unclear.

[19] To conclude on the reasonableness of the decision, it will be recalled that the Officer decided that the applicants could seek “to remain in Canada by any means on completion of the offered employment”. In Do v Canada (Minister of Citizenship and Immigration), 2004 FC 1269 the visa officer found that the job offer was submitted to help the applicant gain access to Canada so that he could eventually sponsor his family members. Von Finckenstein J., in finding that the visa officer erred in making this assertion, stated that:
No rationale was given for this assertion and there is no evidence to that effect on the record.

[20] This is not to say that the Visa Officer’s concerns were without foundation. There was good reason to be concerned both, by the absence of travel back to Nepal, by the lack of proof of any economic or legal interests in Nepal, and the uncertainty of the family situation in Nepal. A yellow flag was reasonably raised, and, in most cases, that would be sufficient to dismiss an application for judicial review. However, assessing the decision as a whole, it does not meet the required standards of justification and intelligibility as set forth in Khosa v Canada (Citizenship and Immigration), 2010 FC 83.

[21] For these reasons, this application for judicial review is granted and the matter remitted to a different visa officer for re-determination.


## 25626:2 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `686e1b850db362f7cd7339f636741139a423f85a51bc45789ebf44b28212aeae`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25626:2:subtheme:1 · paragraphs 22-23

- Raw key terms: `imm-6944-10, judgment, reasons, rennie, alberta, appearances, applicant, applications`
- Display key terms: `imm-6944-10, rennie, alberta, applications`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: imm-6944-10, rennie, alberta, applications Operative outcome context: These applications for judicial review are granted and the matters remitted to a different visa officer for re-consideration. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `5206069` offsets `232-239`; context: These applications for judicial review are granted and the matters remitted to a different visa officer for re-consideration.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
1. These applications for judicial review are granted and the matters remitted to a different visa officer for re-consideration.
2. A copy of these reasons shall be placed on file IMM-6944-10, which was heard at the same time.
3. No questions arise for certification.
"Donald J. Rennie"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-6943-10 & IMM-6944-10
STYLE OF CAUSE: SHYAM THAPA CHHETRI v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
SHALIK RAM THAPA CHHETRI v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Calgary, Alberta
DATE OF HEARING: July 5, 2011
REASONS FOR JUDGMENT
AND JUDGMENT: RENNIE J.
DATED: July 12, 2011
APPEARANCES:
Michael Sherritt
IMM-6943-10 & IMM-6944-10
FOR THE APPLICANT
Brad Hardstaff
IMM-6943-10 & IMM-6944-10
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Sherritt Greene
Barristers & Solicitors
Calgary, Alberta
FOR THE APPLICANT
Myles J. Kirvan,
Deputy Attorney General of Canada
Calgary, Alberta
FOR THE RESPONDENT
