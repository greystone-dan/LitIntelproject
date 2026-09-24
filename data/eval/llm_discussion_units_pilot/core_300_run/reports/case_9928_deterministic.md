# Discussion Units: case 9928

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **44**
- Continuity pairs: **43**
- Discussion Units: **6**
- Paragraph source hashes: **44**
- Sub-themes: **12**

## 9928:1 · paragraphs 0-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `79757faeecd0aac776aa7e9249559d1dfcbbfedd4aee632bbfa78d1528aa4638`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `marcia, employment, insurance, application, back, background, decision, facts`
- Display key terms: `marcia, employment, insurance, back, background, facts`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: marcia, employment, insurance, back, background, facts Rule/authority context: Marcia, this is a judicial review application which is governed by administrative law principles. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501577` offsets `821-829`; context: It appears that the complete story including new evidence has never all been before a decision maker for a number of reasons.
- Evidence: `governing_rule` cue `principles` at chunk `4501579` offsets `110-120`; context: Marcia, this is a judicial review application which is governed by administrative law principles.

#### 9928:1:subtheme:2 · paragraphs 6-8

- Raw key terms: `marcia, caring, discuss, distraught, herself, meeting, office, phone`
- Display key terms: `marcia, caring, discuss, distraught, herself, meeting, office, phone`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: marcia, caring, discuss, distraught, herself, meeting, office, phone Application context: At the time she prided herself as being trusted with information and duties beyond the scope of her employment because of caring so much about the residents and her job. Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4501583` offsets `383-388`; context: The next day, she went to her Director’s office to tell her side of the story and resolve the issue.
- Evidence: `reasoning_application` cue `because` at chunk `4501583` offsets `947-954`; context: At the time she prided herself as being trusted with information and duties beyond the scope of her employment because of caring so much about the residents and her job.

#### 9928:1:subtheme:3 · paragraphs 9-15

- Raw key terms: `marcia, work, felt, weeks, care, clients, during, employee`
- Display key terms: `marcia, work, felt, weeks, care, clients, during, employee`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: marcia, work, felt, weeks, care, clients, during, employee Application context: Her doctor advised her to take time off work because of the stress this incident had caused her. | Marcia being unable to apply for medical disability because of her age felt her only alternative was to quit. Operative outcome context: On January 23, 2015, the Commission allowed Ms. Evidence spans paragraphs 9-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4501586` offsets `70-78`; context: Marcia was so upset that her trustworthiness was called into question and that such a small matter had escalated so quickly, that she went to her family doctor.
- Evidence: `reasoning_application` cue `because` at chunk `4501586` offsets `475-482`; context: Her doctor advised her to take time off work because of the stress this incident had caused her.
- Evidence: `reasoning_application` cue `apply` at chunk `4501587` offsets `32-37`; context: Marcia being unable to apply for medical disability because of her age felt her only alternative was to quit.
- Evidence: `disposition` cue `allowed` at chunk `4501591` offsets `122-129`; context: On January 23, 2015, the Commission allowed Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501592` offsets `160-168`; context: Marcia was requesting the Appeal Division to re-weigh evidence already presented to the General Division.

#### 9928:1:subtheme:4 · paragraphs 16-18

- Raw key terms: `decision, judicial, record, review, already, evidence, general, maker`
- Display key terms: `judicial, review, already, maker`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: judicial, review, already, maker Evidence spans paragraphs 16-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4501593` offsets `185-190`; context: Preliminary Issue [19] Ms.
- Evidence: `evidence_fact` cue `Record` at chunk `4501593` offsets `222-228`; context: Marcia filed a Motion Record the day of the hearing that was not compliant with the rules in a number of aspects.
- Evidence: `evidence_fact` cue `Record` at chunk `4501594` offsets `44-50`; context: [20] I will accept the non-compliant Motion Record for filing but dismiss the motion to file new evidence.
- Evidence: `evidence_fact` cue `Record` at chunk `4501595` offsets `64-70`; context: [21] The Judicial Review will proceed on the Certified Tribunal Record which contains the evidentiary record that was before the decision maker.

#### Section text

Marcia v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2016-12-09
Neutral citation
2016 FC 1367
File numbers
T-297-16
Decision Content
Date: 20161209
Docket: T-297-16
Citation: 2016 FC 1367
Ottawa, Ontario, December 9, 2016
PRESENT: The Honourable Madam Justice McVeigh
BETWEEN:
DERINA MARCIA
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Introduction [1] The Applicant, Derina Marcia [“Ms. Marcia”], challenges a decision dated January 13, 2016, from the Social Security Tribunal – Appeal Division [the Appeal Division], which refused leave to appeal. Ms. Marcia represented herself at the Federal Court. What I heard is a very human story by a hardworking, articulate, and wonderfully caring 71 year old woman. It appears that the complete story including new evidence has never all been before a decision maker for a number of reasons.
II. Background [2] Ms. Marcia was employed by the John Howard Society of Saskatchewan from June 1, 2009 to October 31, 2014. She was in the position of Residential Youth Caseworker from 2009 to 2012 and Supported Independent living Caseworker from 2012 to 2014. Ms. Marcia is passionate about her work with youth at risk. There is no doubt that early on in this saga, something went terribly wrong. She related all of the very emotional facts in great detail from the beginning to the ultimate refusal by the Appeal Division.

[3] The foundation of this judicial review is a determination that Ms. Marcia has to pay back $4,407.00 of employment insurance benefits. The Social Security Commission determined Ms. Marcia was not entitled to the benefits as she voluntarily left her job rather than having left for just cause as provided for in the Employment Insurance Act, SC 1996, c 23, ss 29, 30 [EI Act].

[4] As explained to Ms. Marcia, this is a judicial review application which is governed by administrative law principles. The judicial review will be of a decision on a standard of reasonableness. I can only review the legality of the decision, not determine the merits or do any fact finding.

[5] This is not the legal vehicle that can have Ms. Marcia not having to pay back the employment insurance money or the former employment relationship resolved. I cannot unwind time and start this all over again.

[6] The background to this case is important to understand how all of this started and to untangle how Ms. Marcia got to this point. I listened carefully to all the facts but will not recite the details or the individuals’ names regarding the genesis of Ms. Marcia’s application for employment insurance.

[7] On September 30, 2014, unaware she was doing something wrong, Ms. Marcia obtained the personal phone number of a residential home employee from a staff coordinator and contacted that casual employee about union business. This act was in breach of John Howard Society’s privacy policy and John Howard Society’s contractual agreement with the province of Saskatchewan. Even though she had no idea it was a breach of conduct, she accepted responsibility and apologized for doing it.

[8] The union representative suggested that Ms. Marcia go to the provincial director’s office and repeat what she had told the union representative and this could be settled. Ms Marcia went to his office and was told that he would not discuss it and that her superior would deal with her. The next day, she went to her Director’s office to tell her side of the story and resolve the issue. She did not understand the seriousness of the breach or that the meeting was to be any more than a discussion of what had transpired so that the supervisor knew her side of the story. Ms. Marcia was offered and declined to have a union representative present at this meeting as she could not imagine it was necessary just to talk about something that had innocently occurred; this was especially true since she was a valued and trusted employee. At the time she prided herself as being trusted with information and duties beyond the scope of her employment because of caring so much about the residents and her job.

[9] Ms. Marcia was shocked at the meeting when she was handed a prepared disciplinary letter marked confidential and not to be shared with anyone. Ms. Marcia was not given an opportunity to discuss the circumstances of her taking the phone number. She was distraught by the letter and the process by which she was reprimanded. She felt that the relationship of trust between herself and her employer was broken as the entire job was built on trust considering her job was caring for vulnerable youth.

[10] Her superior took a phone call during the conversation with Ms. Marcia, and as a result she left the office when the telephone call came in. Her superior said she would find her and finish their conversation after she dealt with the phone call. Ms. Marcia waited and when no one showed up, she went home distraught.

[11] Ms. Marcia was so upset that her trustworthiness was called into question and that such a small matter had escalated so quickly, that she went to her family doctor. She related how her integrity had been called into question despite being a trusted employee; she felt the employee-employer relationship had been destroyed. She loved her job and took very seriously her clients’ care. The whole process shook her to her core. Her doctor advised her to take time off work because of the stress this incident had caused her. She took two weeks stress leave from work during which time she contemplated about what to do about her future. During her two weeks leave, she spoke with her union representative for advice, who suggested she apply for short term disability. Ms. Marcia informed them she was not eligible as she was over 70 years old so that was not an option. No one ever mentioned she could file a grievance regarding the reprimand letter.

[12] Ms. Marcia being unable to apply for medical disability because of her age felt her only alternative was to quit. She said this was an attack on her integrity as a person and as an employee and she could not continue to work there. She could not imagine how her doctor’s advice could be met other than by quitting her job.

[13] Upon her return to work, Ms. Marcia gave two weeks’ notice of her intention to resign. Her employer urged her to reconsider but Ms. Marcia felt that employer/employee trust had been irreparably damaged and with that she did not know how she could continue to independently do her job for the residents. During the meeting when she handed in her resignation, the meeting was interrupted by another personal care worker needing to see her superior. Ms. Marcia had to leave the room to give them privacy and she was never called back in to finish the meeting. So she went back to her office and a couple of hours later she was emailed that her resignation was accepted and was not contacted other than a co-worker said to hand in her cellular phone.

[14] After she gave her two weeks’ notice, Ms. Marcia was very busy trying to meet all her clients and their social workers to ensure the transition to a different worker would be smooth. During this time she never looked for other work as these two weeks were very demanding and she did not consider doing it during work hours as this would not have been ethical.

[15] Ms. Marcia did not attempt to speak a second time with her supervisor about errors in the process or factual errors as she was too distraught and concerned for the youths’ care handover. She completed her final two weeks of work as she felt a duty to the clients with whom she worked and cared for so much.

[16] On November 20, 2014, Ms. Marcia made a claim for employment insurance benefits. On January 23, 2015, the Commission allowed Ms. Marcia benefits on the basis of just cause for voluntarily leaving her employment. On February 9, 2015, the John Howard Society made a request for reconsideration and on April 20, 2015, the Commission reversed its decision. As a result, the Commission claimed an overpayment to Ms. Marcia in the amount of $4,407.00. The Commission’s reversal led to the September 3, 2015 appeal and dismissal of Ms. Marcia’s application by the Commission’s General Division [the General Division].

[17] The Appeal Division reviewed the permissible grounds for appeal and came to a determination that Ms. Marcia was requesting the Appeal Division to re-weigh evidence already presented to the General Division. It noted that the role of the Appeal Division is not to re-hear cases de novo; specifically, that new evidence not directly relating to a reviewable error was not normally admissible. The presiding member of the Appeal Division requested further submissions from Ms. Marcia including full and detailed grounds of appeal. No grounds with a reviewable error were submitted.

[18] On January 13, 2016, the Appeal Division refused leave to appeal the General Division’s decision on the basis that the appeal had no reasonable chance of success.
III. Preliminary Issue [19] Ms. Marcia filed a Motion Record the day of the hearing that was not compliant with the rules in a number of aspects. The motion sought to introduce “fresh and new evidence” to be considered at the judicial review. The new evidence sought to be admitted is a Physician’s letter dated March 23, 2015, and submitted to the Tribunal for Leave to Appeal; Saskatchewan Government and General Employees’ Union [SGEU] letters dated November 18, 2015, and December 17, 2015; and pages 97-99 of the SGEU agreement with the John Howard Society and SGEU. The grounds and the relief of the Motion Record are similar to what was already before the Court in the Judicial Review. The Respondent had no opportunity to provide written submissions in response to the Motion Record.

[20] I will accept the non-compliant Motion Record for filing but dismiss the motion to file new evidence. As a general rule, a Judicial Review will proceed on the material that was before the decision maker. The new evidence contained in the Motion Record does not meet the test for admission as an exception to the rule as it is not necessary as a general background nor is it necessary for procedural defects or to highlight there was no evidence before the decision maker. The evidence within the motion is the gist of what is already contained in the Judicial Review application (Association of Universities and Colleges of Canada v Canadian Copyright Licensing Agency, 2012 FCA 22 at para 20).

[21] The Judicial Review will proceed on the Certified Tribunal Record which contains the evidentiary record that was before the decision maker.


## 9928:2 · paragraphs 19-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3cb1990ac23f65fd51dfa8633182dd4ac2524334be52dc7ce1568ef12c3d77bd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:2:subtheme:1 · paragraphs 19-20

- Raw key terms: `canada, standard, acceptable, appeal, breach, brunswick, citizenship, correctness`
- Display key terms: `standard, acceptable, breach, brunswick, correctness`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: standard, acceptable, breach, brunswick, correctness Rule/authority context: Standard of Review [23] The Standard of Review when reviewing Social Security Tribunal – Appeal Division leave decisions is reasonableness (Tracey v Canada (AG), 2015 FC 1300 at paras 17-23). Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4501595` offsets `149-154`; context: Issue [22] Was the decision of the Appeal Division not to grant leave reasonable?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4501595` offsets `234-252`; context: Standard of Review [23] The Standard of Review when reviewing Social Security Tribunal – Appeal Division leave decisions is reasonableness (Tracey v Canada (AG), 2015 FC 1300 at paras 17-23).

#### Section text

IV. Issue [22] Was the decision of the Appeal Division not to grant leave reasonable?
V. Standard of Review [23] The Standard of Review when reviewing Social Security Tribunal – Appeal Division leave decisions is reasonableness (Tracey v Canada (AG), 2015 FC 1300 at paras 17-23). The Court must be satisfied as to the existence of justification, transparency and intelligibility within the decision-making process, and find that the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law (Dunsmuir v New Brunswick, 2008 SCC 9 at paras 47-48 [Dunsmuir]).

[24] Any breach of procedural fairness will be reviewed on a correctness standard (Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43).


## 9928:3 · paragraphs 21-33

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3ddd083e38c7ee65d7d07b74b099e78f505c84187b8ac11291ed875df2696c94`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:3:subtheme:1 · paragraphs 21-24

- Raw key terms: `appeal, cause, clear, division, doctor, employee, employer, evidence`
- Display key terms: `clear, division, doctor, employee, employer`
- Argument roles: `disposition, evidence_fact`
- Explanation: Observed roles: disposition, evidence_fact Display terms: clear, division, doctor, employee, employer Operative outcome context: Marcia argues that she should be allowed to present and correct factual errors made throughout the process. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501597` offsets `616-624`; context: She feels her union has equally failed her for poor representation given that evidence she feels is crucial has been left out and that no one ever mentioned the possibility of using the grievance process as disability was not an option available to her.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501598` offsets `211-219`; context: Marcia argues that the Appeal Division failed to allow her to provide further new medical evidence (dated October 21, 2015) that clarified the doctor’s brief first note when he explained in his new doctor’s note that she should quit her job for the sake of her health.
- Evidence: `disposition` cue `allowed` at chunk `4501598` offsets `42-49`; context: Marcia argues that she should be allowed to present and correct factual errors made throughout the process.
- Evidence: `evidence_fact` cue `determined that` at chunk `4501599` offsets `60-75`; context: [28] Finally, she cannot believe that after Social Security determined that she had just cause for voluntarily leaving her employment and paid her employment insurance that as a former valued employee, the John Howard Society would contest her receiving employment insurance.

#### 9928:3:subtheme:2 · paragraphs 25-26

- Raw key terms: `appeal, decision, division, grounds, reasonable, three, acted, appears`
- Display key terms: `division, grounds, reasonable, three, acted, appears`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: division, grounds, reasonable, three, acted, appears Rule/authority context: ” An applicant must satisfy the Appeal Division that their appeal has a reasonable chance of success on at least one of the three grounds found under subsection 58(1): (a) The General Division failed to observe a princip Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4501600` offsets `684-691`; context: ” An applicant must satisfy the Appeal Division that their appeal has a reasonable chance of success on at least one of the three grounds found under subsection 58(1):
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or,
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4501600` offsets `736-742`; context: ” An applicant must satisfy the Appeal Division that their appeal has a reasonable chance of success on at least one of the three grounds found under subsection 58(1):
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or,
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `under` at chunk `4501600` offsets `457-462`; context: ” An applicant must satisfy the Appeal Division that their appeal has a reasonable chance of success on at least one of the three grounds found under subsection 58(1):
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or,
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

#### 9928:3:subtheme:3 · paragraphs 27-33

- Raw key terms: `marcia, appeal, division, evidence, general, attorney, canada, cannot`
- Display key terms: `marcia, division, cannot`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position Display terms: marcia, division, cannot Position/evidence statements: Marcia requested that she submit additional information on grounds he could review. Rule/authority context: The legal test for just cause is set out in s. | This is where it must be frustrating to be met with administrative law principles as a self-represented person. Operative outcome context: 30 indicates that a person cannot receive benefits if they left voluntarily without cause or if they were dismissed for misconduct. Evidence spans paragraphs 27-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4501602` offsets `44-49`; context: Marcia did not raise a justiciable issue with a reasonable chance of success to the Appeal Division.
- Evidence: `party_position` cue `submit` at chunk `4501602` offsets `182-188`; context: Marcia requested that she submit additional information on grounds he could review.
- Evidence: `issue` cue `whether` at chunk `4501603` offsets `492-499`; context: The onus is on the Commission to show that the person left their job voluntarily and then the onus shifts to the person to show whether they had just cause for voluntarily leaving their job (Tanguay v Unemployment Insurance Commission, [1985] FCJ No 910 (FCA)).
- Evidence: `governing_rule` cue `legal test` at chunk `4501603` offsets `246-256`; context: The legal test for just cause is set out in s.
- Evidence: `disposition` cue `dismissed` at chunk `4501603` offsets `126-135`; context: 30 indicates that a person cannot receive benefits if they left voluntarily without cause or if they were dismissed for misconduct.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501605` offsets `9-17`; context: [34] New evidence is not permissible at the Appeal Division as it is limited to the grounds in subsection 58(1) and the appeal does not constitute a hearing de novo.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501606` offsets `50-58`; context: Marcia says the doctor’s note is not new evidence, it is just a clarification letter and the SGEU letter just verifies facts so the Appeal Division should have considered them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501607` offsets `81-89`; context: Marcia that these new documents are not new evidence.
- Evidence: `governing_rule` cue `principles` at chunk `4501607` offsets `162-172`; context: This is where it must be frustrating to be met with administrative law principles as a self-represented person.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501608` offsets `102-110`; context: Marcia presented to the Appeal Division that they make a decision that involved weighing the evidence including new evidence that was not before the General Division.
- Evidence: `governing_rule` cue `under` at chunk `4501608` offsets `465-470`; context: The submissions before the Appeal Division did not point to any error that the General Division made under s.

#### Section text

VI. Analysis [25] I will dismiss this application for the reasons that follow.

[26] Ms. Marcia is upset at her union, previous employer and the tribunal/judicial process generally. She has clearly spent an enormous amount of time researching and submitting information to various tribunals which she feels has been largely ignored. It is equally clear she feels she has not been given a fair shake by her employer (for giving her the disciplinary letter without discussion in the first place; plus she feels she exhausted all avenues of internal dispute resolution by attempting to speak to the regional supervisor). She feels her union has equally failed her for poor representation given that evidence she feels is crucial has been left out and that no one ever mentioned the possibility of using the grievance process as disability was not an option available to her.

[27] Ms. Marcia argues that she should be allowed to present and correct factual errors made throughout the process. Ms. Marcia argues that the Appeal Division failed to allow her to provide further new medical evidence (dated October 21, 2015) that clarified the doctor’s brief first note when he explained in his new doctor’s note that she should quit her job for the sake of her health. She says the Appeal Division decision should also have considered: the SGEU letters by Kelly Hardy Labour Relations Officer dated November 17 and December 17, 2015, which stating her union had not agreed to the reprimand letter that was issued to Ms. Marcia which is contrary to what her employer verbally told her. Ms. Marcia feels that this new evidence creates a just cause for her quitting the John Howard Society and the Appeal Division should have considered this new evidence as well as any other new evidence she has now produced to correct the facts, such as portions of the collective agreement between her former employee and the union; a Regina Public School Pamphlet.

[28] Finally, she cannot believe that after Social Security determined that she had just cause for voluntarily leaving her employment and paid her employment insurance that as a former valued employee, the John Howard Society would contest her receiving employment insurance. She says if the Appeal Division or the General Division would read her doctor’s follow up clarification report that it is clear she left her job for just cause and should be entitled to benefits as was originally determined.

[29] The test for determining leave to appeal a decision of the General Division is found at subsection 58(2) of the Department of Employment and Social Development Act, SC 2005, c 34 [the DESDA]: “leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.” An applicant must satisfy the Appeal Division that their appeal has a reasonable chance of success on at least one of the three grounds found under subsection 58(1):
(a) The General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) The General Division erred in law in making its decision, whether or not the error appears on the face of the record; or,
(c) The General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

[30] None of these three grounds having been argued by Ms. Marcia, the Respondent submits the Appeal Division’s decision was reasonable.

[31] Ms. Marcia did not raise a justiciable issue with a reasonable chance of success to the Appeal Division. The presiding member in an effort to help Ms. Marcia requested that she submit additional information on grounds he could review. Ms. Marcia mistakenly believed she had already done so. In order to have a reasonable chance at success in the context of s. 58(2), is that the proposed appeal must have some arguable grounds to succeed (Osaj v Canada (Attorney General), 2016 FC 115 at para 12).

[32] The EI Act, s. 30 indicates that a person cannot receive benefits if they left voluntarily without cause or if they were dismissed for misconduct. Ms. Marcia would have to prove that she left voluntarily but had just cause for doing so. The legal test for just cause is set out in s. 29 of the EI Act and contains a non-exhaustive list of what is just cause. The onus is on the Commission to show that the person left their job voluntarily and then the onus shifts to the person to show whether they had just cause for voluntarily leaving their job (Tanguay v Unemployment Insurance Commission, [1985] FCJ No 910 (FCA)).

[33] Justice Layden-Stevenson noted in Canada (Attorney General) v White, 2011 FCA 190 at paragraph 5, that an employee has an obligation to resolve disputes with an employer or demonstrate that they tried to find other employment before they voluntarily quit their job.

[34] New evidence is not permissible at the Appeal Division as it is limited to the grounds in subsection 58(1) and the appeal does not constitute a hearing de novo. As Ms. Marcia’s new evidence pertaining to the General Division’s decision could not be admitted, the Appeal Division did not err in not accepting it (Alves v Canada (Attorney General), 2014 FC 1100 at para 73). Parliament has determined that the Appeal Division is limited by the statute to what they can grant leave on (DESDA).

[35] Ms. Marcia says the doctor’s note is not new evidence, it is just a clarification letter and the SGEU letter just verifies facts so the Appeal Division should have considered them.

[36] I cannot legally agree with Ms. Marcia that these new documents are not new evidence. This is where it must be frustrating to be met with administrative law principles as a self-represented person.

[37] Ms. Marcia presented to the Appeal Division that they make a decision that involved weighing the evidence including new evidence that was not before the General Division. It was reasonable for the Appeal Division to not reweigh evidence or consider the new evidence to find the General Division in error for not considering evidence that was not before them. The submissions before the Appeal Division did not point to any error that the General Division made under s. 58(2) which would make their decision to not grant leave unreasonable.

## 9928:4 · paragraphs 34-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bc070736dcaf00e7b3d1b91143755cdefcfe6403eddb5bddc39916217ff1c0cd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:4:subtheme:1 · paragraphs 34-38

- Raw key terms: `appeal, division, evidence, tribunal, allowing, another, different, doctor`
- Display key terms: `division, allowing, another, different, doctor`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: division, allowing, another, different, doctor Application context: Having failed to do so, even after having been prompted to do so by the Tribunal, I find that this application for leave to appeal does not have a reasonable chance of success and must be refused. | She says that because she did not have legal representation, the General Division failed in its duty as it should have assisted an unrepresented individual by allowing her to clarify the first medical note by filing anot Evidence spans paragraphs 34-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `I find` at chunk `4501609` offsets `489-495`; context: Having failed to do so, even after having been prompted to do so by the Tribunal, I find that this application for leave to appeal does not have a reasonable chance of success and must be refused.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501610` offsets `171-179`; context: Marcia argued that it was procedurally unfair that the Appeal Division did not allow the medical note from her doctor that clarified the previously filed medical evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4501610` offsets `195-202`; context: She says that because she did not have legal representation, the General Division failed in its duty as it should have assisted an unrepresented individual by allowing her to clarify the first medical note by filing another.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501611` offsets `107-115`; context: [40] She also filed two SGEU letters that address a factual error where the union contradicts the employer evidence that they agreed with the letter of reprimand as well as another document.
- Evidence: `counterargument_limitation` cue `but` at chunk `4501611` offsets `320-323`; context: While not making a determination, it is possible that this information in a different forum could have led to different outcome, but this is not the forum.
- Evidence: `evidence_fact` cue `evidence` at chunk `4501612` offsets `116-124`; context: [41] The tribunal rightly classed the doctor’s note, two union letters and the Regina Public School Document as new evidence, for which they had no authority to consider.

#### 9928:4:subtheme:2 · paragraphs 39-40

- Raw key terms: `assistance, attempt, authority, consider, cost, costs, employer, employment`
- Display key terms: `assistance, attempt, authority, consider, cost, costs, employer, employment`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: assistance, attempt, authority, consider, cost, costs, employer, employment Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4501614` offsets `192-198`; context: Marcia and her employer could not attempt to resolve some issues with the assistance of a mediator.

#### Section text

[38] The following was the conclusion of the Appeal Division:
It is not sufficient for an Applicant to plead that the General Division member was mistaken in his or her conclusions and ask the Appeal Division for a different outcome. In order to have a reasonable chance of success, the Applicant must explain in some detail how in their view at least one reviewable error set out in the Act has been made. Having failed to do so, even after having been prompted to do so by the Tribunal, I find that this application for leave to appeal does not have a reasonable chance of success and must be refused.

[39] Ms. Marcia argued that it was procedurally unfair that the Appeal Division did not allow the medical note from her doctor that clarified the previously filed medical evidence. She says that because she did not have legal representation, the General Division failed in its duty as it should have assisted an unrepresented individual by allowing her to clarify the first medical note by filing another.

[40] She also filed two SGEU letters that address a factual error where the union contradicts the employer evidence that they agreed with the letter of reprimand as well as another document. While not making a determination, it is possible that this information in a different forum could have led to different outcome, but this is not the forum.

[41] The tribunal rightly classed the doctor’s note, two union letters and the Regina Public School Document as new evidence, for which they had no authority to consider. There was no breach of procedural fairness in not allowing new evidence before the Appeal Division.

[42] The decision of the tribunal not to grant leave is reasonable.

[43] I make two observations now that all the factual information is gathered. The first observation is that I see no reason that Ms. Marcia and her employer could not attempt to resolve some issues with the assistance of a mediator. My second observation is employment insurance could consider an equitable resolution to the payback request. These are only my observations and have no authority in law.

[44] The Respondent did not ask for cost and there will be no order as to costs.


## 9928:5 · paragraphs 41-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e0a1b3ecdfea8b48c9737559cc612e83d7734341819166be9607222dc9fa47a8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:5:subtheme:1 · paragraphs 41-42

- Raw key terms: `application, attorney, canada, cause, costs, court, date, derina`
- Display key terms: `costs, date, derina`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: costs, date, derina Operative outcome context: The application is dismissed; 2. Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4501615` offsets `143-152`; context: The application is dismissed;
2.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application is dismissed;
2. No costs are ordered.
"Glennys L. McVeigh"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-297-16
STYLE OF CAUSE:
DERINA MARCIA v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Regina, Saskatchewan
DATE OF HEARING:
SEPTEMBER 1, 2016


## 9928:6 · paragraphs 43-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e10866c8653dd512014af07d9616b98add7e677c75bceb8eacc0fa19ec5f8731`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9928:6:subtheme:1 · paragraphs 43-43

- Raw key terms: `appearances, applicant, attorney, canada, dated, december, deputy, derina`
- Display key terms: `dated, december, deputy, derina`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, december, deputy, derina No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 43-43. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MCVEIGH J.
DATED:
DECEMBER 9, 2016
APPEARANCES:
Derina Marcia
For The Applicant
Vanessa Luna
For The Respondent
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Gatineau, Quebec
For The Respondent
