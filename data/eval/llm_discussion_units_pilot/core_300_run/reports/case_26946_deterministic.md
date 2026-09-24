# Discussion Units: case 26946

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **63**
- Continuity pairs: **62**
- Discussion Units: **5**
- Paragraph source hashes: **63**
- Sub-themes: **16**

## 26946:1 · paragraphs 0-10

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b4aa93087befc3cb10a067cc4492f514c970df206134a6b21568180424e4e577`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26946:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `application, applicant, principal, applicants, immigration, rahmatian, december, document`
- Display key terms: `principal, rahmatian, december, document`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: principal, rahmatian, december, document Position/evidence statements: He claims to have specifically asked Mr. | [5] The principal applicant acknowledges that he signed his application form but alleges that he was never given an opportunity to review what was submitted by Mr. Rule/authority context: [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] of a decision of Immigration Counsellor A. | The Fairness Letter notified him that the officer had been unable to verify the authenticity of the False Document, and as a result, he was considering a finding that he was inadmissible for misrepresentation pursuant to Application context: Yousef Oloumi [the principal applicant], filed an application for permanent residence in the Federal Skilled Worker class and his spouse and sons applied as accompanying family members. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5266802` offsets `247-262`; context: Luhowy [the counsellor] made on December 23, 2010, where he determined that the applicants are inadmissible pursuant to section 40(1)(a) of the Act, due to misrepresentation of a material fact in their application for permanent residence.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5266802` offsets `47-58`; context: [1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] of a decision of Immigration Counsellor A.
- Evidence: `reasoning_application` cue `applied` at chunk `5266803` offsets `270-277`; context: Yousef Oloumi [the principal applicant], filed an application for permanent residence in the Federal Skilled Worker class and his spouse and sons applied as accompanying family members.
- Evidence: `party_position` cue `claims` at chunk `5266805` offsets `211-217`; context: He claims to have specifically asked Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5266805` offsets `331-334`; context: Rahmatian about the requirement to take an IELTS test as part of his application, but was told that he could write the test at some point in the future, as the processing of his application could take three or four years.
- Evidence: `party_position` cue `submitted` at chunk `5266806` offsets `147-156`; context: [5] The principal applicant acknowledges that he signed his application form but alleges that he was never given an opportunity to review what was submitted by Mr.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5266808` offsets `387-398`; context: The Fairness Letter notified him that the officer had been unable to verify the authenticity of the False Document, and as a result, he was considering a finding that he was inadmissible for misrepresentation pursuant to subsection 40(1)(a) of the Act.
- Evidence: `party_position` cue `submitted` at chunk `5266809` offsets `211-220`; context: [8] The officer rejected the explanation that the principal applicant was not aware of the False Document as not credible since the application clearly indicated that an English language test was required to be submitted with the application.
- Evidence: `governing_rule` cue `under` at chunk `5266809` offsets `387-392`; context: On December 23, 2010, the counsellor accepted the recommendation that the principal applicant be found to be inadmissible for misrepresentation under subsection 40(1)(a) of the Act.

#### 26946:1:subtheme:2 · paragraphs 9-10

- Raw key terms: `applicants, application, court, evidence, additional, adduce, administration, agree`
- Display key terms: `additional, adduce, administration, agree`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: additional, adduce, administration, agree Position/evidence statements: (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants : a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence s | [10] The respondent submits that the applicants have filed evidence that was not before the counsellor in his decision. Application context: The respondent submits that these exceptions do not apply in this case, and therefore the evidence should be struck from the application record. Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `QUESTION` at chunk `5266810` offsets `645-653`; context: (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente loi;
PRELIMINARY QUESTION
Can the Court consider the evidence submitted by the applicants that was not before the decision-maker?
- Evidence: `party_position` cue `submitted` at chunk `5266810` offsets `690-699`; context: (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente loi;
PRELIMINARY QUESTION
Can the Court consider the evidence submitted by the applicants that was not before the decision-maker?
- Evidence: `evidence_fact` cue `evidence` at chunk `5266810` offsets `681-689`; context: (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente loi;
PRELIMINARY QUESTION
Can the Court consider the evidence submitted by the applicants that was not before the decision-maker?
- Evidence: `issue` cue `issues` at chunk `5266811` offsets `245-251`; context: The respondent submits that the applicants are not entitled to adduce fresh evidence upon judicial review, except to resolve issues of procedural fairness or jurisdiction: Vong v Canada (Minister of Citizenship and Immigration), 2006 FC 1480 at paragraphs 35-36, 38; Alabadleh v Canada (Minister of Citizenship and Immigration), 2006 FC 716 at paragraph 6.
- Evidence: `party_position` cue `submits` at chunk `5266811` offsets `20-27`; context: [10] The respondent submits that the applicants have filed evidence that was not before the counsellor in his decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5266811` offsets `59-67`; context: [10] The respondent submits that the applicants have filed evidence that was not before the counsellor in his decision.
- Evidence: `reasoning_application` cue `apply` at chunk `5266811` offsets `529-534`; context: The respondent submits that these exceptions do not apply in this case, and therefore the evidence should be struck from the application record.

#### Section text

Oloumi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-04-13
Neutral citation
2012 FC 428
File numbers
IMM-3290-11
Decision Content
Date: 20120413
Docket: IMM-3290-11
Citation: 2012 FC 428
Ottawa, Ontario, April 13, 2012
PRESENT: The Honourable Madam Justice Tremblay-Lamer
BETWEEN:
YOUSEF OLOUMI
SEPIDEH ASSADISAMI
SHERVIN OLOUMI
ARMIN OLOUMI
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review pursuant to section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] of a decision of Immigration Counsellor A. Luhowy [the counsellor] made on December 23, 2010, where he determined that the applicants are inadmissible pursuant to section 40(1)(a) of the Act, due to misrepresentation of a material fact in their application for permanent residence.
BACKGROUND FACTS

[2] The applicants, Yousef Oloumi, Sepideh Assadisami, Shervin Oloumi, and Armin Oloumi, are citizens of Iran. In 2005, Mr. Yousef Oloumi [the principal applicant], filed an application for permanent residence in the Federal Skilled Worker class and his spouse and sons applied as accompanying family members. He is a dentist.

[3] In 2005, the principal applicant hired an immigration consultant, Mr. Arash Rahmatian [Mr. Rahmatian] of Queen Consultants Corporation to assist him in the preparation of his application for permanent residence in Canada. The consultant was not an authorized immigration consultant or lawyer. He prepared the application and translated it into English. The application was received on or before March 5, 2005 by the Canadian Embassy in Damascus.

[4] The principal applicant states that, unbeknownst to him, Mr. Rahmatian included an International English Language Testing System [IELTS] test result that turned out to be fraudulent [the False Document]. He claims to have specifically asked Mr. Rahmatian about the requirement to take an IELTS test as part of his application, but was told that he could write the test at some point in the future, as the processing of his application could take three or four years.

[5] The principal applicant acknowledges that he signed his application form but alleges that he was never given an opportunity to review what was submitted by Mr. Rahmatian.

[6] On July 16, 2010, the application was transferred to the Canadian Embassy in Warsaw as part of backlog reduction. On the same day, Canadian officials contacted the principal applicant to request updated information, as the processing of their application was set to begin.

[7] On October 20, 2010, Immigration Officer M. Maryszczak [the officer] sent the principal applicant a letter detailing his concerns with his application [the Fairness Letter]. The Fairness Letter notified him that the officer had been unable to verify the authenticity of the False Document, and as a result, he was considering a finding that he was inadmissible for misrepresentation pursuant to subsection 40(1)(a) of the Act. Another consultant the applicants had retained by that time responded on December 22, 2010, stating that the principal applicant was unaware of the False Document and had been the victim of a fraudulent immigration consultant, and asked that he not be penalized for Mr. Rahmatian’s actions.

[8] The officer rejected the explanation that the principal applicant was not aware of the False Document as not credible since the application clearly indicated that an English language test was required to be submitted with the application. On December 23, 2010, the counsellor accepted the recommendation that the principal applicant be found to be inadmissible for misrepresentation under subsection 40(1)(a) of the Act.
APPLICABLE LAW

[9] Section 40(1)(a) of the Act states:
40. (1) A permanent resident or a foreign national is inadmissible for misrepresentation
(a) for directly or indirectly misrepresenting or withholding material facts relating to a relevant matter that induces or could induce an error in the administration of this Act;
40. (1) Emportent interdiction de territoire pour fausses déclarations les faits suivants :
a) directement ou indirectement, faire une présentation erronée sur un fait important quant à un objet pertinent, ou une réticence sur ce fait, ce qui entraîne ou risque d’entraîner une erreur dans l’application de la présente loi;
PRELIMINARY QUESTION
Can the Court consider the evidence submitted by the applicants that was not before the decision-maker?

[10] The respondent submits that the applicants have filed evidence that was not before the counsellor in his decision. The respondent submits that the applicants are not entitled to adduce fresh evidence upon judicial review, except to resolve issues of procedural fairness or jurisdiction: Vong v Canada (Minister of Citizenship and Immigration), 2006 FC 1480 at paragraphs 35-36, 38; Alabadleh v Canada (Minister of Citizenship and Immigration), 2006 FC 716 at paragraph 6. The respondent submits that these exceptions do not apply in this case, and therefore the evidence should be struck from the application record. I agree and thus the Court will not rely on this additional evidence.
ISSUES

## 26946:2 · paragraphs 11-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2db467080c8f73bb479031cbe489f915e3562e5d533701dc2b34631a15ecc594`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26946:2:subtheme:1 · paragraphs 11-12

- Raw key terms: `misrepresentation, standard, applicants, application, canada, citizenship, conclude, counsellor`
- Display key terms: `misrepresentation, standard, conclude, counsellor`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: misrepresentation, standard, conclude, counsellor Rule/authority context: STANDARD OF REVIEW Application context: [11] The issues in this application are: 1) Was it reasonable for the counsellor to conclude that there was a misrepresentation? | [12] Misrepresentation is an issue of mixed fact and law and is therefore reviewable on the reasonableness standard: Karami v Canada (Minister of Citizenship and Immigration), 2009 FC 788, 349 FTR 96 at paragraph 14. Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5266812` offsets `9-15`; context: [11] The issues in this application are:
1) Was it reasonable for the counsellor to conclude that there was a misrepresentation?
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `5266812` offsets `315-333`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `conclude` at chunk `5266812` offsets `84-92`; context: [11] The issues in this application are:
1) Was it reasonable for the counsellor to conclude that there was a misrepresentation?
- Evidence: `issue` cue `issue` at chunk `5266813` offsets `29-34`; context: [12] Misrepresentation is an issue of mixed fact and law and is therefore reviewable on the reasonableness standard: Karami v Canada (Minister of Citizenship and Immigration), 2009 FC 788, 349 FTR 96 at paragraph 14.
- Evidence: `reasoning_application` cue `therefore` at chunk `5266813` offsets `64-73`; context: [12] Misrepresentation is an issue of mixed fact and law and is therefore reviewable on the reasonableness standard: Karami v Canada (Minister of Citizenship and Immigration), 2009 FC 788, 349 FTR 96 at paragraph 14.

#### 26946:2:subtheme:2 · paragraphs 13-14

- Raw key terms: `question, questions, reviewed, standard, added, adjudicator, alberta, apply`
- Display key terms: `question, questions, reviewed, standard, added, adjudicator, alberta, apply`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: question, questions, reviewed, standard, added, adjudicator, alberta, apply Application context: ] In other words, since Dunsmuir, for the correctness standard to apply, the question has to not only be one of central importance to the legal system but also outside the adjudicator’s specialized area of expertise. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5266814` offsets `22-29`; context: [13] The questions of whether section 40(1)(a) includes a knowledge component is a question of law related to the interpretation of the officer’s home statute and will thus also be reviewed on a reasonableness standard: Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at paragraphs 46 and 48:
- Evidence: `issue` cue `question` at chunk `5266815` offsets `530-538`; context: ]
In other words, since Dunsmuir, for the correctness standard to apply, the question has to not only be one of central importance to the legal system but also outside the adjudicator’s specialized area of expertise.
- Evidence: `reasoning_application` cue `apply` at chunk `5266815` offsets `519-524`; context: ]
In other words, since Dunsmuir, for the correctness standard to apply, the question has to not only be one of central importance to the legal system but also outside the adjudicator’s specialized area of expertise.

#### 26946:2:subtheme:3 · paragraphs 15-17

- Raw key terms: `misrepresentation, clearly, conclude, document, false, ielts, reasonable, report`
- Display key terms: `misrepresentation, clearly, conclude, document, false, ielts, reasonable, report`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: misrepresentation, clearly, conclude, document, false, ielts, reasonable, report Position/evidence statements: [14] The applicants submit that there was no misrepresentation, because the False Document was clearly not a test result. | [15] The respondent submits that the False Document was clearly designed to mislead the immigration authorities to believe it was an IELTS Test Report. Application context: His decision that an inquiry does not automatically terminate as a result of his extending the 90-day period only after the expiry of that period is therefore reviewable on the reasonableness standard. | [14] The applicants submit that there was no misrepresentation, because the False Document was clearly not a test result. Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5266816` offsets `149-155`; context: 50(5) PIPA relates to the interpretation of his own statute, is within his expertise and does not raise issues of general legal importance or true jurisdiction.
- Evidence: `reasoning_application` cue `therefore` at chunk `5266816` offsets `355-364`; context: His decision that an inquiry does not automatically terminate as a result of his extending the 90-day period only after the expiry of that period is therefore reviewable on the reasonableness standard.
- Evidence: `party_position` cue `submit` at chunk `5266817` offsets `20-26`; context: [14] The applicants submit that there was no misrepresentation, because the False Document was clearly not a test result.
- Evidence: `reasoning_application` cue `because` at chunk `5266817` offsets `64-71`; context: [14] The applicants submit that there was no misrepresentation, because the False Document was clearly not a test result.
- Evidence: `party_position` cue `submits` at chunk `5266818` offsets `20-27`; context: [15] The respondent submits that the False Document was clearly designed to mislead the immigration authorities to believe it was an IELTS Test Report.

#### 26946:2:subtheme:4 · paragraphs 18-23

- Raw key terms: `applicants, document, misrepresentation, false, immigration, language, test, applicant`
- Display key terms: `document, misrepresentation, false, language`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: document, misrepresentation, false, language Position/evidence statements: [17] The applicants submit in the alternative that if there was a misrepresentation, it was not material. | [19] The applicants submit that this case is similar to Zaib v Canada (Minister of Citizenship and Immigration), 2010 FC 769, and Medel v Canada (Minister of Employment and Immigration), [1990] 2 FC 345 (CA): in those ca Application context: It was thus wholly reasonable for the counsellor to conclude that it was intended to mislead the authorities to believe it to be an authentic test result. | [20] The applicants also submit that the officer erred by finding their response to the Fairness Letter implausible—since their consultant was so unscrupulous as to falsify a language test result, it was unreasonable to  Evidence spans paragraphs 18-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5266819` offsets `865-870`; context: Issue No.
- Evidence: `reasoning_application` cue `conclude` at chunk `5266819` offsets `762-770`; context: It was thus wholly reasonable for the counsellor to conclude that it was intended to mislead the authorities to believe it to be an authentic test result.
- Evidence: `party_position` cue `submit` at chunk `5266820` offsets `20-26`; context: [17] The applicants submit in the alternative that if there was a misrepresentation, it was not material.
- Evidence: `party_position` cue `submit` at chunk `5266822` offsets `20-26`; context: [19] The applicants submit that this case is similar to Zaib v Canada (Minister of Citizenship and Immigration), 2010 FC 769, and Medel v Canada (Minister of Employment and Immigration), [1990] 2 FC 345 (CA): in those cases, the visa officer misinformed the applicants regarding the basis for the concerns about misrepresentation.
- Evidence: `party_position` cue `submit` at chunk `5266823` offsets `25-31`; context: [20] The applicants also submit that the officer erred by finding their response to the Fairness Letter implausible—since their consultant was so unscrupulous as to falsify a language test result, it was unreasonable to conclude that the consultant would not also falsify the form on which the applicants are purported to have acknowledged submitting those results.
- Evidence: `reasoning_application` cue `conclude` at chunk `5266823` offsets `220-228`; context: [20] The applicants also submit that the officer erred by finding their response to the Fairness Letter implausible—since their consultant was so unscrupulous as to falsify a language test result, it was unreasonable to conclude that the consultant would not also falsify the form on which the applicants are purported to have acknowledged submitting those results.
- Evidence: `party_position` cue `submits` at chunk `5266824` offsets `20-27`; context: [21] The respondent submits that the applicants’ submissions on materiality are contrary to the wording of section 40(1)(a) of the Act—when the False Document was submitted, it was the only evidence of the principal applicant’s language proficiency.
- Evidence: `evidence_fact` cue `evidence` at chunk `5266824` offsets `190-198`; context: [21] The respondent submits that the applicants’ submissions on materiality are contrary to the wording of section 40(1)(a) of the Act—when the False Document was submitted, it was the only evidence of the principal applicant’s language proficiency.

#### 26946:2:subtheme:5 · paragraphs 24-25

- Raw key terms: `material, misrepresentation, provision, purpose, underlying, accomplish, accuracy, administration`
- Display key terms: `material, misrepresentation, provision, purpose, underlying, accomplish, accuracy, administration`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: material, misrepresentation, provision, purpose, underlying, accomplish, accuracy, administration Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5266825` offsets `20-27`; context: [22] In determining whether a misrepresentation is material, regard must be had for the wording of the provision, and its underlying purpose.

#### 26946:2:subtheme:6 · paragraphs 26-28

- Raw key terms: `application, document, false, material, applicant, applicants, because, fact`
- Display key terms: `document, false, material, because, fact`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: document, false, material, because, fact Position/evidence statements: The materiality analysis is not limited to a particular point in time in the processing of the application—the fact that the principal applicant had submitted more recent language test results does not render the earlier Application context: As soon as the False Document was submitted, it could have induced an error in the administration of the Act, because a decision-maker could have relied upon it to conclude that the principal applicant had demonstrated l | The False Document was thus clearly material because the application could not have been processed without it. Evidence spans paragraphs 26-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5266827` offsets `47-54`; context: [24] In this case, the misrepresented fact was whether the principal applicant had passed an IELTS language test.
- Evidence: `reasoning_application` cue `because` at chunk `5266827` offsets `372-379`; context: As soon as the False Document was submitted, it could have induced an error in the administration of the Act, because a decision-maker could have relied upon it to conclude that the principal applicant had demonstrated language proficiency.
- Evidence: `reasoning_application` cue `because` at chunk `5266828` offsets `227-234`; context: The False Document was thus clearly material because the application could not have been processed without it.
- Evidence: `party_position` cue `submitted` at chunk `5266829` offsets `280-289`; context: The materiality analysis is not limited to a particular point in time in the processing of the application—the fact that the principal applicant had submitted more recent language test results does not render the earlier misrepresentation immaterial.

#### 26946:2:subtheme:7 · paragraphs 29-31

- Raw key terms: `applicants, document, false, issue, knowledge, misrepresentation, officer, pursuant`
- Display key terms: `document, false, knowledge, misrepresentation, officer, pursuant`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: document, false, knowledge, misrepresentation, officer, pursuant Rule/authority context: [28] Therefore, I find that the visa officer was reasonable to conclude that the False Document constituted a material misrepresentation pursuant to section 40(1)(a) of the Act. | [29] The applicants suggest that in order to be found inadmissible pursuant to section 40(1)(a) of the Act, a party must have acted with subjective intent, i. Application context: Here, the ‘test’ for which the False Document purports to provide results never occurred, and thus the reasoning from that case does not apply. | [28] Therefore, I find that the visa officer was reasonable to conclude that the False Document constituted a material misrepresentation pursuant to section 40(1)(a) of the Act. Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5266830` offsets `209-214`; context: Here, language test results are clearly relevant to the application at issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5266830` offsets `378-386`; context: The decision in Zaib is also distinguishable: the officer in that case was mistakenly informed that a letter confirming the applicant’s degree was forged—further evidence proved that the degree itself was authentic.
- Evidence: `reasoning_application` cue `apply` at chunk `5266830` offsets `569-574`; context: Here, the ‘test’ for which the False Document purports to provide results never occurred, and thus the reasoning from that case does not apply.
- Evidence: `issue` cue `Issue` at chunk `5266831` offsets `178-183`; context: Issue No.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5266831` offsets `137-148`; context: [28] Therefore, I find that the visa officer was reasonable to conclude that the False Document constituted a material misrepresentation pursuant to section 40(1)(a) of the Act.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5266831` offsets `5-14`; context: [28] Therefore, I find that the visa officer was reasonable to conclude that the False Document constituted a material misrepresentation pursuant to section 40(1)(a) of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5266832` offsets `67-78`; context: [29] The applicants suggest that in order to be found inadmissible pursuant to section 40(1)(a) of the Act, a party must have acted with subjective intent, i.

#### 26946:2:subtheme:8 · paragraphs 32-35

- Raw key terms: `decision, justice, misrepresentation, applicant, applicants, fact, knowledge, above`
- Display key terms: `justice, misrepresentation, fact, knowledge, above`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: justice, misrepresentation, fact, knowledge, above Rule/authority context: In Osisanwo, the applicant was found inadmissible under section 40(1)(a) by Citizenship and Immigration Canada (CIC) because she had listed her husband as the father of her two children, when in fact he was only the biol | He concluded that, because the applicants in the decision under review had no reason to believe they were misrepresenting a material fact, it was unreasonable to find them inadmissible for misrepresentation. Application context: In Osisanwo, the applicant was found inadmissible under section 40(1)(a) by Citizenship and Immigration Canada (CIC) because she had listed her husband as the father of her two children, when in fact he was only the biol | He concluded that, because the applicants in the decision under review had no reason to believe they were misrepresenting a material fact, it was unreasonable to find them inadmissible for misrepresentation. Operative outcome context: [31] In conducting the judicial review of this decision, Justice Hughes surveyed cases in which a misrepresentation finding was upheld, and noted that they all contained an element of mens rea, or subjective intent. Evidence spans paragraphs 32-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5266833` offsets `181-189`; context: [30] The applicants cite the recent decision of Justice Hughes, in Osisanwo et al v Canada (Minister of Citizenship and Immigration), 2011 FC 1126 (Osisanwo), which considered this question.
- Evidence: `governing_rule` cue `under` at chunk `5266833` offsets `241-246`; context: In Osisanwo, the applicant was found inadmissible under section 40(1)(a) by Citizenship and Immigration Canada (CIC) because she had listed her husband as the father of her two children, when in fact he was only the biological child of one.
- Evidence: `reasoning_application` cue `because` at chunk `5266833` offsets `308-315`; context: In Osisanwo, the applicant was found inadmissible under section 40(1)(a) by Citizenship and Immigration Canada (CIC) because she had listed her husband as the father of her two children, when in fact he was only the biological child of one.
- Evidence: `issue` cue `question` at chunk `5266834` offsets `439-447`; context: He certified a question on the issue, but the respondent did not pursue an appeal.
- Evidence: `governing_rule` cue `under` at chunk `5266834` offsets `274-279`; context: He concluded that, because the applicants in the decision under review had no reason to believe they were misrepresenting a material fact, it was unreasonable to find them inadmissible for misrepresentation.
- Evidence: `reasoning_application` cue `because` at chunk `5266834` offsets `235-242`; context: He concluded that, because the applicants in the decision under review had no reason to believe they were misrepresenting a material fact, it was unreasonable to find them inadmissible for misrepresentation.
- Evidence: `counterargument_limitation` cue `but` at chunk `5266834` offsets `462-465`; context: He certified a question on the issue, but the respondent did not pursue an appeal.
- Evidence: `disposition` cue `upheld` at chunk `5266834` offsets `128-134`; context: [31] In conducting the judicial review of this decision, Justice Hughes surveyed cases in which a misrepresentation finding was upheld, and noted that they all contained an element of mens rea, or subjective intent.
- Evidence: `reasoning_application` cue `I find` at chunk `5266835` offsets `5-11`; context: [32] I find that the decision in Osisanwo is not of assistance to the applicants in this case.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5266835` offsets `161-167`; context: That decision was dependent on a highly unusual set of facts, and cannot be relied upon for the general proposition that a misrepresentation must always require subjective knowledge.
- Evidence: `reasoning_application` cue `applies` at chunk `5266836` offsets `340-347`; context: He went on to hold that section 40 applies where an applicant adopts a misrepresentation but then clarifies it prior to a decision.

#### 26946:2:subtheme:9 · paragraphs 36-42

- Raw key terms: `canada, immigration, citizenship, minister, reasonably, applicant, applicants, application`
- Display key terms: `reasonably`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: reasonably Position/evidence statements: Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. Rule/authority context: [15] Under s. Application context: In that case, the applicant was found inadmissible for misrepresentation because he had failed to disclose the existence of a child that the Board found he reasonably should have suspected was his own. | Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. Operative outcome context: that she had been “granted landing… by reason of any fraudulent or improper means”. Evidence spans paragraphs 36-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5266837` offsets `492-500`; context: ) Justice Harrington considered certifying a question similar to that in Osisanwo, above, but concluded that the decision was unreasonable on other grounds.
- Evidence: `reasoning_application` cue `because` at chunk `5266837` offsets `221-228`; context: In that case, the applicant was found inadmissible for misrepresentation because he had failed to disclose the existence of a child that the Board found he reasonably should have suspected was his own.
- Evidence: `counterargument_limitation` cue `but` at chunk `5266837` offsets `537-540`; context: ) Justice Harrington considered certifying a question similar to that in Osisanwo, above, but concluded that the decision was unreasonable on other grounds.
- Evidence: `governing_rule` cue `Under` at chunk `5266839` offsets `5-10`; context: [15] Under s.
- Evidence: `party_position` cue `claimed` at chunk `5266840` offsets `387-394`; context: Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error.
- Evidence: `reasoning_application` cue `because` at chunk `5266840` offsets `374-381`; context: Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error.
- Evidence: `disposition` cue `granted` at chunk `5266840` offsets `808-815`; context: that she had been “granted landing… by reason of any fraudulent or improper means”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5266841` offsets `49-58`; context: [36] When considered within its factual context, therefore, the exception in Medel is relatively narrow.
- Evidence: `evidence_fact` cue `evidence` at chunk `5266842` offsets `474-482`; context: Section 16(1) of the Act reads that “[a] person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.

#### Section text

[11] The issues in this application are:
1) Was it reasonable for the counsellor to conclude that there was a misrepresentation?
2) If so, was it reasonable for the counsellor to conclude that this misrepresentation was material?
3) Does section 40(1)(a) require the applicants’ knowledge of the misrepresentation?
STANDARD OF REVIEW

[12] Misrepresentation is an issue of mixed fact and law and is therefore reviewable on the reasonableness standard: Karami v Canada (Minister of Citizenship and Immigration), 2009 FC 788, 349 FTR 96 at paragraph 14.

[13] The questions of whether section 40(1)(a) includes a knowledge component is a question of law related to the interpretation of the officer’s home statute and will thus also be reviewed on a reasonableness standard: Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at paragraphs 46 and 48:

[46] At para. 22 of Canada (Canadian Human Rights Commission), LeBel and Cromwell JJ. state:
On the other hand, our Court has reaffirmed that general questions of law that are both of central importance to the legal system as a whole and outside the adjudicator’s specialized area of expertise, must still be reviewed on a standard of correctness, in order to safeguard a basic consistency in the fundamental legal order of our country. [Emphasis added.]
In other words, since Dunsmuir, for the correctness standard to apply, the question has to not only be one of central importance to the legal system but also outside the adjudicator’s specialized area of expertise.
[…]

[48] The Commissioner’s interpretation of s. 50(5) PIPA relates to the interpretation of his own statute, is within his expertise and does not raise issues of general legal importance or true jurisdiction. His decision that an inquiry does not automatically terminate as a result of his extending the 90-day period only after the expiry of that period is therefore reviewable on the reasonableness standard. (Emphasis added.)
ANALYSIS
Issue No.1 Was it reasonable for the counsellor to conclude that there was a misrepresentation?

[14] The applicants submit that there was no misrepresentation, because the False Document was clearly not a test result. While the document mimics the appearance of an IELTS Test Report, it states that it is “just a domestic document”. Thus, no reasonable person could conclude that it was an IELTS Test Report, and there is no misrepresentation.

[15] The respondent submits that the False Document was clearly designed to mislead the immigration authorities to believe it was an IELTS Test Report. Thus, the respondent submits there clearly was a misrepresentation.

[16] The Court agrees with the respondent that the False Document constitutes a misrepresentation: an examination of its physical appearance reveals that it is clearly designed to imitate the appearance of an IELTS Test Report. There is no other plausible purpose behind the submission of the False Document other than to mislead the immigration authorities into thinking that the file was complete and that the principal applicant had satisfied the language requirements. An official doing an initial completeness review of the file would not necessarily notice that it was fraudulent. I do not accept that any reasonable person would say that the purpose of this document was anything other than to mislead. It was thus wholly reasonable for the counsellor to conclude that it was intended to mislead the authorities to believe it to be an authentic test result.
Issue No. 2 Was it reasonable for the counsellor to conclude that the misrepresentation was material?

[17] The applicants submit in the alternative that if there was a misrepresentation, it was not material. The applicants rely on the CIC Enforcement Manual ENF 2, Evaluating Inadmissibility, which states that a misrepresentation should only be considered material if it affects the process. Since only the most recent language test results are to be considered, the False Document could not have affected the process.

[18] The applicants rely on Ali v Canada (Minister of Citizenship and Immigration), 2008 FC 166, in which the applicant committed a misrepresentation by submitting a fraudulent document, but the Court found the misrepresentation to be immaterial.

[19] The applicants submit that this case is similar to Zaib v Canada (Minister of Citizenship and Immigration), 2010 FC 769, and Medel v Canada (Minister of Employment and Immigration), [1990] 2 FC 345 (CA): in those cases, the visa officer misinformed the applicants regarding the basis for the concerns about misrepresentation. The applicants assert that the officer misled them in the Fairness Letter, stating that they had submitted an unverifiable IELTS Test Report—since the False Document was clearly not a test result, this was inaccurate information.

[20] The applicants also submit that the officer erred by finding their response to the Fairness Letter implausible—since their consultant was so unscrupulous as to falsify a language test result, it was unreasonable to conclude that the consultant would not also falsify the form on which the applicants are purported to have acknowledged submitting those results.

[21] The respondent submits that the applicants’ submissions on materiality are contrary to the wording of section 40(1)(a) of the Act—when the False Document was submitted, it was the only evidence of the principal applicant’s language proficiency. Had it not been submitted, the application would have been deemed incomplete and returned. Thus, the misrepresentation affected the process, and was material: Guan v Canada (Minister of Citizenship and Immigration), 2009 FC 274. I agree for the following reasons.

[22] In determining whether a misrepresentation is material, regard must be had for the wording of the provision, and its underlying purpose.

[23] Section 40(1)(a) is to be given a broad interpretation in order to promote its underlying purpose: Khan v Canada (Minister of Citizenship and Immigration), 2008 FC 512 at paragraph 25. The objective of this provision is to deter misrepresentation and maintain the integrity of the immigration process— to accomplish this objective, the onus is placed on the applicant to ensure the completeness and accuracy of his or her application. Section 40(1)(a) is broadly worded to encompass misrepresentations even if made by another party, without the knowledge of the applicant: Jiang v Canada (Minister of Citizenship and Immigration), 2011 FC 942, at paragraph 35; Wang v Canada (Minister of Citizenship and Immigration), 2005 FC 1059 at paragraphs 55-56. The applicant cannot misrepresent or withhold any material facts that could induce an error in the administration of the Act.

[24] In this case, the misrepresented fact was whether the principal applicant had passed an IELTS language test. There is no doubt this fact was material to his application—federal skilled worker applicants must demonstrate language proficiency to be accepted. As soon as the False Document was submitted, it could have induced an error in the administration of the Act, because a decision-maker could have relied upon it to conclude that the principal applicant had demonstrated language proficiency.

[25] I agree with the respondent that to be material, a misrepresentation need not be decisive or determinative. It will be material if it is important enough to affect the process. The False Document was thus clearly material because the application could not have been processed without it.

[26] The fact that the misrepresentation was caught before the final assessment of the application does not assist the applicants. The materiality analysis is not limited to a particular point in time in the processing of the application—the fact that the principal applicant had submitted more recent language test results does not render the earlier misrepresentation immaterial. Such a result would reflect a narrow understanding of materiality that is contrary to the wording and purpose of section 40(1)(a) of the Act. The False Document was submitted and it was material.

[27] This case is distinguishable from Ali, above: there, the fraudulent document was irrelevant to the determination of the application. Here, language test results are clearly relevant to the application at issue. The decision in Zaib is also distinguishable: the officer in that case was mistakenly informed that a letter confirming the applicant’s degree was forged—further evidence proved that the degree itself was authentic. Here, the ‘test’ for which the False Document purports to provide results never occurred, and thus the reasoning from that case does not apply.

[28] Therefore, I find that the visa officer was reasonable to conclude that the False Document constituted a material misrepresentation pursuant to section 40(1)(a) of the Act.
Issue No. 3 Does section 40(1)(a) require the applicants’ knowledge of the misrepresentation?

[29] The applicants suggest that in order to be found inadmissible pursuant to section 40(1)(a) of the Act, a party must have acted with subjective intent, i.e. knowledge of the misrepresentation.

[30] The applicants cite the recent decision of Justice Hughes, in Osisanwo et al v Canada (Minister of Citizenship and Immigration), 2011 FC 1126 (Osisanwo), which considered this question. In Osisanwo, the applicant was found inadmissible under section 40(1)(a) by Citizenship and Immigration Canada (CIC) because she had listed her husband as the father of her two children, when in fact he was only the biological child of one. The couple had briefly separately almost 30 years prior, and during that separation the applicant had had a one-time affair with another man. The couple then reconciled and neither suspected that the husband was not the father of the child in question. This fact only came to light when an official at CIC ordered DNA testing. Despite the lack of knowledge on the part of the applicant, she was declared inadmissible for misrepresentation pursuant to section 40(1)(a).

[31] In conducting the judicial review of this decision, Justice Hughes surveyed cases in which a misrepresentation finding was upheld, and noted that they all contained an element of mens rea, or subjective intent. He concluded that, because the applicants in the decision under review had no reason to believe they were misrepresenting a material fact, it was unreasonable to find them inadmissible for misrepresentation. He certified a question on the issue, but the respondent did not pursue an appeal.

[32] I find that the decision in Osisanwo is not of assistance to the applicants in this case. That decision was dependent on a highly unusual set of facts, and cannot be relied upon for the general proposition that a misrepresentation must always require subjective knowledge. Rather, the general rule is that a misrepresentation can occur without the applicant’s knowledge, as noted by Justice Russell in Jiang, above, at paragraph 35:

[35] With respect to inadmissibility based on misrepresentation, this Court has already given section 40 a broad and robust interpretation. In Khan, above, Justice O’Keefe held that the wording of the Act must be respected and section 40 should be given the broad interpretation that its wording demands. He went on to hold that section 40 applies where an applicant adopts a misrepresentation but then clarifies it prior to a decision. In Wang v Canada (Minister of Citizenship and Immigration), 2005 FC 1059, this Court held that section 40 applies to an applicant where the misrepresentation was made by another party to the application and the applicant had no knowledge of it. The Court stated that an initial reading of section 40 would not support this interpretation but that the section should be interpreted in this manner to prevent an absurd result. (Emphasis added.)
A few cases have carved out a narrow exception to this rule, but this will only apply for truly exceptional circumstances, where the applicant honestly and reasonably believed they were not misrepresenting a material fact.

[33] In Osisanwo, Justice Hughes cites the decision of Justice Harrington in Singh v Canada (Minister of Citizenship and Immigration), 2010 FC 378. In that case, the applicant was found inadmissible for misrepresentation because he had failed to disclose the existence of a child that the Board found he reasonably should have suspected was his own. (Notably, like the applicants in the case before me, this applicant was found to not be credible.) Justice Harrington considered certifying a question similar to that in Osisanwo, above, but concluded that the decision was unreasonable on other grounds.

[34] The passage of Singh referred to by Justice Hughes contains an oft-cited portion of Justice O’Reilly’s judgment in Baro v Canada (Minister of Citizenship and Immigration), 2007 FC 1299:

[15] Under s. 40(1)(a) of IRPA, a person is inadmissible to Canada if he or she “withholds material facts relating to a relevant matter that induces or could induce an error in the administration” of the Act. In general terms, an applicant for permanent residence has a “duty of candour” which requires disclosure of material facts. This duty extends to variations in his or her personal circumstances, including a change of marital status: Mohammed v. Canada (Minister of Citizenship and Immigration), [1997] 3 F.C. 299 (F.C.T.D.) (QL). Even an innocent failure to provide material information can result in a finding of inadmissibility; for example, an applicant who fails to include all of her children in her application may be inadmissible: Bickin v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No.1495 (F.C.T.D.) (QL). An exception arises where applicants can show that they honestly and reasonably believed that they were not withholding material information: Medel v. Canada (Minister of Employment and Immigration), [1990] 2 F.C. 345, [1990] F.C.J. No. 318 (F.C.A.) (QL). (Emphasis added.)

[35] Despite being frequently cited, the “exception” referred to in this passage has received limited application. Its originating case, Medel, above, involved an unusual set of facts: the applicant was being sponsored by her husband, but unbeknownst to her the husband withdrew his sponsorship. Canadian officials then misled the applicant by asking her to return the visa because they claimed it contained an error. They implied it would be returned to her, corrected. The applicant had English-speaking relatives inspect the visa and, after they assured her that nothing was wrong with it, she used it to enter Canada. The Immigration Appeal Board found her to be a person described in section 27(1)(e) of the former Immigration Act, 1976, SC 1976-77, c 52 [now RSC 1985, c I-2)], i.e. that she had been “granted landing… by reason of any fraudulent or improper means”. This finding was set aside by the Federal Court of Appeal because the applicant had “reasonably believed” that she was not withholding information relevant to her admission.

[36] When considered within its factual context, therefore, the exception in Medel is relatively narrow. As Justice MacKay noted while distinguishing the case before him in Mohammed v Canada (Minister of Citizenship & Immigration), [1997] 3 FC 299:
41 The present circumstances may also be distinguished from those in Medel on the basis that the information which the applicant failed to disclose was not information regarding which he was truly subjectively unaware. The applicant in the present case was not unaware that he was married. Nor was it information, as in Medel, the knowledge of which was beyond his control. This was not information which had been concealed from him or about which he had been misled by Embassy officials. The applicant's alleged ignorance regarding the requirement to report such a material change in his marital status and his inability to communicate this information to an immigration officer upon arrival does not, in my opinion, constitute “subjective unawareness” of the material information as contemplated in Medel. (Emphasis added)
Furthermore, I emphasize that a determinative factor in the Medel case was that the applicant had reasonably believed that she was not withholding information from Canadian authorities. In contrast, in the case before this Court the applicants did not act reasonably—the principal applicant failed to review his application to ensure its accuracy.

[37] It must be kept in mind that foreign nationals seeking to enter Canada have a duty of candour: Bodine v Canada (Minister of Citizenship and Immigration), 2008 FC 848, at paragraph 41; Baro v Canada (Minister of Citizenship and Immigration), 2007 FC 1299 at paragraph 15. Section 16(1) of the Act reads that “[a] person who makes an application must answer truthfully all questions put to them for the purpose of the examination and must produce a visa and all relevant evidence and documents that the officer reasonably requires.”

[38] As noted in Bodine (at paragraph 44):
…The purpose of section 40(1)(a) of the Act is to ensure that applicants provide complete, honest and truthful information in every manner when applying for entry into Canada (see De Guzman v. Canada (Minister of Citizenship and Immigration), 2005 FCA 436 (F.C.T.D.), Khan v. Canada (Minister of Citizenship and Immigration), 2008 FC 512 (F.C.T.D.), Wang v. Canada (Minister of Citizenship and Immigration), 2005 FC 1059 (F.C.T.D.), aff’d on other grounds, 2006 FCA 345 (F.C.A.)). In some situations, even silence can be a misrepresentation (see Mohammed v. Canada (Minister of Citizenship and Immigration), [1997] 3 F.C. 299) and the present facts went well beyond mere silence.

## 26946:3 · paragraphs 43-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5019e99855150367dc35851f73312499f8d2a0413c515edfe19f08629ba5b973`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26946:3:subtheme:1 · paragraphs 43-50

- Raw key terms: `applicants, application, applicant, consultant, immigration, signed, above, canada`
- Display key terms: `consultant, signed, above`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: consultant, signed, above Position/evidence statements: In essence, they submit that the fraudulence of their immigration consultant should serve as a defence to the application of section 40(1)(a). | [16] The applicant was in Bangladesh at the time the updated application was submitted. Rule/authority context: In my view, there is no such defence under the Act: the wording of section 40(1)(a) is broad enough to encompass misrepresentations made by another party, of which the applicant was unaware: Wang, above at paragraphs 55- | [44] I additionally do not find that there is any relevant defence under the common law. Application context: There is no further entitlement to now try again to prove that they were defrauded and therefore should not be found inadmissible. Evidence spans paragraphs 43-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `5266845` offsets `170-176`; context: In essence, they submit that the fraudulence of their immigration consultant should serve as a defence to the application of section 40(1)(a).
- Evidence: `party_position` cue `submitted` at chunk `5266848` offsets `77-86`; context: [16] The applicant was in Bangladesh at the time the updated application was submitted.
- Evidence: `governing_rule` cue `under` at chunk `5266849` offsets `206-211`; context: In my view, there is no such defence under the Act: the wording of section 40(1)(a) is broad enough to encompass misrepresentations made by another party, of which the applicant was unaware: Wang, above at paragraphs 55-56.
- Evidence: `governing_rule` cue `under` at chunk `5266850` offsets `67-72`; context: [44] I additionally do not find that there is any relevant defence under the common law.
- Evidence: `evidence_fact` cue `evidence` at chunk `5266851` offsets `433-441`; context: The applicants provided no supporting evidence of their claim to have been innocent in the misrepresentation, and the officer is not required to make further inquiries if the applicants’ response to the Fairness Letter was deficient: Pan v Canada (Minister of Citizenship and Immigration), 2010 FC 838 at paragraph 28.
- Evidence: `reasoning_application` cue `therefore` at chunk `5266851` offsets `1157-1166`; context: There is no further entitlement to now try again to prove that they were defrauded and therefore should not be found inadmissible.

#### Section text

[39] In keeping with this duty of candour, there is, in my opinion, a duty for an applicant to make sure that when making an application, the documents are complete and accurate. It is too easy to later claim innocence and blame a third party when, as in the present case, the application form clearly stated that language results were to be attached, and the form was signed by the applicants. It is only in exceptional cases where an applicant can demonstrate that they honestly and reasonably believed that they were not withholding material information, where “the knowledge of which was beyond their control”, that an applicant may be able to take advantage of an exception to the application of section 40(1)(a). This is not such a case.

[40] The applicants allege that they had no knowledge of the misrepresentation and wish to exonerate themselves by blaming their immigration consultant. In essence, they submit that the fraudulence of their immigration consultant should serve as a defence to the application of section 40(1)(a).

[41] In response to this submission, I adopt the argument of the respondents, that the decisions in Cao v Canada (Minister of Citizenship and Immigration), 2010 FC 450, and Haque v Canada (Minister of Citizenship and Immigration), 2011 FC 315, require that an applicant be held responsible for the contents of an application which he or she has signed.

[42] Justice Mosley’s comments at paragraph 16 of Haque, above, are instructive:

[16] The applicant was in Bangladesh at the time the updated application was submitted. He admitted during the phone conversation on May 26th that he “could have signed the blank form for the consultant”. The new form had further discrepancies. The applicant apparently chose to rely on the consultant to submit the required information without personally verifying that it was accurate.
The applicants in this case chose to rely on their consultant. It would be contrary to the applicant’s duty of candour to permit the applicant to rely now on his failure to review his own application. It was his responsibility to ensure his application was truthful and complete—he was negligent in performing this duty.

[43] Furthermore, in order for the applicants to rely on a ‘defence’ to the finding of misrepresentation, that defence must be grounded either in statute or common law. In my view, there is no such defence under the Act: the wording of section 40(1)(a) is broad enough to encompass misrepresentations made by another party, of which the applicant was unaware: Wang, above at paragraphs 55-56. Furthermore, in Haque v Canada (Minister of Citizenship and Immigration), 2011 FC 315, the Court held that the fact that an immigration consultant was to blame for the misrepresentation was no defence. As already discussed, the applicants cannot avail themselves of the exception for an innocent mistake.

[44] I additionally do not find that there is any relevant defence under the common law. The applicants were entitled to procedural fairness, but that entitlement was minimal and it was satisfied in this case: the applicants received the Fairness Letter advising them of the officer’s concerns about the False Document, and giving them 30 days to respond. The applicants’ response to the Fairness Letter was a brief email from their new consultant, stating they were duped by their earlier consultant, and asking that they not be punished for his actions.

[45] As demonstrated by the CAIPS notes, the officer considered this response, but found it not credible since the application form clearly stated that language results were attached and that form was signed by the applicants. The Court finds that it was reasonably open to the officer to reach this conclusion, faced with no more than the bald assertion by the applicants that they were duped. The applicants provided no supporting evidence of their claim to have been innocent in the misrepresentation, and the officer is not required to make further inquiries if the applicants’ response to the Fairness Letter was deficient: Pan v Canada (Minister of Citizenship and Immigration), 2010 FC 838 at paragraph 28. As stated by Justice Crampton (as he then was), “To impose such an obligation on a visa officer would be akin to requiring a visa officer to give advance notice of a negative decision, an obligation that has been expressly rejected. (Ahmed v Canada (Minister of Citizenship and Immigration), [1997] FCJ No 940 (QL); Sharma, above)” (ibid at paragraph 28). There is no further entitlement to now try again to prove that they were defrauded and therefore should not be found inadmissible.

## 26946:4 · paragraphs 51-61

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8ff277667f5b887b979e4a3a396e7ec77830c4ace0ef64c969613868f916fd46`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26946:4:subtheme:1 · paragraphs 51-56

- Raw key terms: `applicants, applicant, application, care, fraudulent, officer, case, clearly`
- Display key terms: `care, fraudulent, officer, case, clearly`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: care, fraudulent, officer, case, clearly Position/evidence statements: However, as already discussed, the applicants in this case did not act with care—they failed to take responsibility for the contents of their application, and review it before it was submitted. | [48] The applicants submit that the visa officer had failed meet the duty of care required in the situation. Rule/authority context: Furthermore, subject to the narrow exception discussed above, this Court has consistently found that an applicant can be inadmissible under section 40(1)(a) for misrepresentations made by another without the applicant’s  Application context: Therefore, the applicants cannot rely on the reasoning from this case to claim a defence to the finding of misrepresentation. | They suggest that the False Document should have been immediately returned when it was received, because it was clearly a copy and not an original. Evidence spans paragraphs 51-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `5266852` offsets `471-480`; context: However, as already discussed, the applicants in this case did not act with care—they failed to take responsibility for the contents of their application, and review it before it was submitted.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5266852` offsets `671-680`; context: Therefore, the applicants cannot rely on the reasoning from this case to claim a defence to the finding of misrepresentation.
- Evidence: `counterargument_limitation` cue `However` at chunk `5266852` offsets `288-295`; context: However, as already discussed, the applicants in this case did not act with care—they failed to take responsibility for the contents of their application, and review it before it was submitted.
- Evidence: `party_position` cue `submit` at chunk `5266854` offsets `20-26`; context: [48] The applicants submit that the visa officer had failed meet the duty of care required in the situation.
- Evidence: `reasoning_application` cue `because` at chunk `5266854` offsets `206-213`; context: They suggest that the False Document should have been immediately returned when it was received, because it was clearly a copy and not an original.
- Evidence: `reasoning_application` cue `apply` at chunk `5266855` offsets `44-49`; context: [49] The concept of a duty of care does not apply in this context—the applicants were subject to a duty of candour, which they did not satisfy.
- Evidence: `reasoning_application` cue `conclude` at chunk `5266856` offsets `251-259`; context: When the visa officer later examined the False Document, he noted several problems with it (likely including the fact that it was evidently a copy), which led him to conclude it was fraudulent.
- Evidence: `evidence_fact` cue `found that` at chunk `5266857` offsets `285-295`; context: Furthermore, subject to the narrow exception discussed above, this Court has consistently found that an applicant can be inadmissible under section 40(1)(a) for misrepresentations made by another without the applicant’s knowledge.
- Evidence: `governing_rule` cue `under` at chunk `5266857` offsets `329-334`; context: Furthermore, subject to the narrow exception discussed above, this Court has consistently found that an applicant can be inadmissible under section 40(1)(a) for misrepresentations made by another without the applicant’s knowledge.
- Evidence: `counterargument_limitation` cue `However` at chunk `5266857` offsets `101-108`; context: However, this problem does not amount to a defence against the operation of section 40(1)(a).

#### 26946:4:subtheme:2 · paragraphs 57-58

- Raw key terms: `application, question, applicant, certification, certified, constituted, court, dismissed`
- Display key terms: `question, certification, certified, constituted, dismissed`
- Argument roles: `disposition, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, issue, party_position, reasoning_application Display terms: question, certification, certified, constituted, dismissed Position/evidence statements: [53] The applicant has submitted the following question for the Court’s certification: Is a foreign national inadmissible for misrepresenting a material fact if at the time of filing his/her application for permanent res Application context: [52] The application must therefore be dismissed. Operative outcome context: [52] The application must therefore be dismissed. Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `5266858` offsets `60-68`; context: Certified Question
- Evidence: `reasoning_application` cue `therefore` at chunk `5266858` offsets `26-35`; context: [52] The application must therefore be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5266858` offsets `39-48`; context: [52] The application must therefore be dismissed.
- Evidence: `issue` cue `question` at chunk `5266859` offsets `47-55`; context: [53] The applicant has submitted the following question for the Court’s certification:
Is a foreign national inadmissible for misrepresenting a material fact if at the time of filing his/her application for permanent residence or at the time of granting permanent residence he/she had no knowledge of the material fact that constituted such misrepresentation?
- Evidence: `party_position` cue `submitted` at chunk `5266859` offsets `23-32`; context: [53] The applicant has submitted the following question for the Court’s certification:
Is a foreign national inadmissible for misrepresenting a material fact if at the time of filing his/her application for permanent residence or at the time of granting permanent residence he/she had no knowledge of the material fact that constituted such misrepresentation?

#### 26946:4:subtheme:3 · paragraphs 59-61

- Raw key terms: `application, case, certified, court, immigration, question, above, already`
- Display key terms: `case, certified, question, above, already`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application Display terms: case, certified, question, above, already Position/evidence statements: [54] The respondent submits that no question should be certified in this case as too many factual conclusions would have to be presumed in the applicants’ favour. Rule/authority context: Based on my reasoning above, I find that the answer to this question is already well-settled in this Court’s jurisprudence and thus decline to certify the question. Application context: Based on my reasoning above, I find that the answer to this question is already well-settled in this Court’s jurisprudence and thus decline to certify the question. Operative outcome context: This application for judicial review is dismissed; and 2. Evidence spans paragraphs 59-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5266860` offsets `36-44`; context: [54] The respondent submits that no question should be certified in this case as too many factual conclusions would have to be presumed in the applicants’ favour.
- Evidence: `party_position` cue `submits` at chunk `5266860` offsets `20-27`; context: [54] The respondent submits that no question should be certified in this case as too many factual conclusions would have to be presumed in the applicants’ favour.
- Evidence: `counterargument_limitation` cue `However` at chunk `5266860` offsets `163-170`; context: However, if the Court disagrees with its submissions on this point, the respondent submits that the following question should be certified:
Where supporting documentation is submitted with a signed application form for permanent residence in Canada, but the applicant later states that he or she had no knowledge of the documentation submitted or part thereof, is the applicant still responsible for the veracity of all the supporting documentation for the purposes of the application of paragraph 40(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27, as amended?
- Evidence: `issue` cue `question` at chunk `5266861` offsets `20-28`; context: [55] In order for a question to be certified, it must arise from the case before the Court and raise a question of law of general importance that has not already been determined by the Federal Court: Hyunh v R, [1995] 1 FC 633, 88 FTR 60.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5266861` offsets `348-361`; context: Based on my reasoning above, I find that the answer to this question is already well-settled in this Court’s jurisprudence and thus decline to certify the question.
- Evidence: `reasoning_application` cue `I find` at chunk `5266861` offsets `268-274`; context: Based on my reasoning above, I find that the answer to this question is already well-settled in this Court’s jurisprudence and thus decline to certify the question.
- Evidence: `disposition` cue `dismissed` at chunk `5266861` offsets `487-496`; context: This application for judicial review is dismissed; and
2.

#### Section text

[46] The applicants seek to rely on the decision in Doe v Canada (Citizenship and Immigration), 2010 FC 284 at paragraph 28, for the proposition that the negligence of counsel (or in this case, fraudulence of a consultant) should not cause an applicant who has acted with care to suffer. However, as already discussed, the applicants in this case did not act with care—they failed to take responsibility for the contents of their application, and review it before it was submitted. An applicant has to verify the accuracy and completeness of the required information before signing it. It is not sufficient to not exercise diligence and then plead ignorance when caught. Therefore, the applicants cannot rely on the reasoning from this case to claim a defence to the finding of misrepresentation.

[47] Furthermore, it seems to me that when a consultant, like in the present case, provides information that does not coincide with the instructions provided with an application, an applicant should be alerted to the possibility that the consultant’s advice may not be accurate and should inquire with officials before signing the application to make sure that what the consultant said was accurate.

[48] The applicants submit that the visa officer had failed meet the duty of care required in the situation. They suggest that the False Document should have been immediately returned when it was received, because it was clearly a copy and not an original. The applicants’ argument seems to be an attempt to separate the fraudulent aspect of the False Document from its other deficiencies—i.e. that the visa officer should have first realized the False Document was a copy and not an original, and then, rather than inspect it any further, immediately return it to the applicants and ask for an original instead.

[49] The concept of a duty of care does not apply in this context—the applicants were subject to a duty of candour, which they did not satisfy. The initial screening officer was simply tasked with undertaking a “completeness” check of the application file. He owed no “duty of care” to the applicants.

[50] The requirements of procedural fairness—which did exist—were in fact satisfied. When the visa officer later examined the False Document, he noted several problems with it (likely including the fact that it was evidently a copy), which led him to conclude it was fraudulent. The visa officer’s obligation at that point was to advise the applicants that they were potentially inadmissible for misrepresentation. He discharged this obligation by sending the Fairness Letter and thus satisfied the requirements of procedural fairness.

[51] The Court acknowledges that the problem of fraudulent immigration consultants is a serious one. However, this problem does not amount to a defence against the operation of section 40(1)(a). Furthermore, subject to the narrow exception discussed above, this Court has consistently found that an applicant can be inadmissible under section 40(1)(a) for misrepresentations made by another without the applicant’s knowledge. There can thus clearly be no subjective intent or knowledge requirement to section 40: this would be contrary to the broad interpretation that the wording and purpose of the provision requires.

[52] The application must therefore be dismissed.
Certified Question

[53] The applicant has submitted the following question for the Court’s certification:
Is a foreign national inadmissible for misrepresenting a material fact if at the time of filing his/her application for permanent residence or at the time of granting permanent residence he/she had no knowledge of the material fact that constituted such misrepresentation?

[54] The respondent submits that no question should be certified in this case as too many factual conclusions would have to be presumed in the applicants’ favour. However, if the Court disagrees with its submissions on this point, the respondent submits that the following question should be certified:
Where supporting documentation is submitted with a signed application form for permanent residence in Canada, but the applicant later states that he or she had no knowledge of the documentation submitted or part thereof, is the applicant still responsible for the veracity of all the supporting documentation for the purposes of the application of paragraph 40(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27, as amended?

[55] In order for a question to be certified, it must arise from the case before the Court and raise a question of law of general importance that has not already been determined by the Federal Court: Hyunh v R, [1995] 1 FC 633, 88 FTR 60. Based on my reasoning above, I find that the answer to this question is already well-settled in this Court’s jurisprudence and thus decline to certify the question.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. This application for judicial review is dismissed; and
2. No question of general importance is certified.
“Danièle Tremblay-Lamer”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3290-11
STYLE OF CAUSE: Yousef Oloumi et al. v The Minister of Citizenship and Immigration
PLACE OF HEARING: Montréal (Québec)
DATE OF HEARING: March 21, 2012
REASONS FOR 

## 26946:5 · paragraphs 62-62

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `427ce48e6c860a2c52f99b65a5afdf9920a53f10cd2338bf7bf7cb3d695efca6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26946:5:subtheme:1 · paragraphs 62-62

- Raw key terms: `appearances, applicants, april, attorney, brisebois, canada, catherine, chalk`
- Display key terms: `april, brisebois, catherine, chalk`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, brisebois, catherine, chalk No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 62-62. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: TREMBLAY-LAMER J.
DATED: April 13, 2012
APPEARANCES:
Mr. David Chalk
FOR THE APPLICANTS
Mr. Normand Lemyre
Ms. Catherine Brisebois
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Robinson Sheppard Shapiro
Montréal (Québec)
FOR THE APPLICANTS
Myles J. Kirvan,
Deputy Attorney General of Canada
Montréal (Québec)
FOR THE RESPONDENT
