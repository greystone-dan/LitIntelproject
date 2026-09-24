# Discussion Units: case 23057

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **107**
- Continuity pairs: **106**
- Discussion Units: **5**
- Paragraph source hashes: **107**
- Sub-themes: **31**

## 23057:1 · paragraphs 0-68

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `420d637ccf456fbed4dd430705d976c02e37e1408edaad3936c754c7765ec492`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23057:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, airport, already, appeal, application, applied, arising, attorney`
- Display key terms: `airport, already, applied, arising`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: airport, already, applied, arising Rule/authority context: Guida Belo-Alves (the “Applicant”) seeks judicial review, pursuant to section 18. Application context: In its decision, the Review Tribunal determined that it did not have the jurisdiction to deal with the matter before it because the issues being raised had already been finally decided by a different review tribunal, and Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5080925` offsets `1028-1034`; context: In its decision, the Review Tribunal determined that it did not have the jurisdiction to deal with the matter before it because the issues being raised had already been finally decided by a different review tribunal, and therefore the principle of res judicata applied.
- Evidence: `evidence_fact` cue `determined that` at chunk `5080925` offsets `933-948`; context: In its decision, the Review Tribunal determined that it did not have the jurisdiction to deal with the matter before it because the issues being raised had already been finally decided by a different review tribunal, and therefore the principle of res judicata applied.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5080925` offsets `556-567`; context: Guida Belo-Alves (the “Applicant”) seeks judicial review, pursuant to section 18.
- Evidence: `reasoning_application` cue `because` at chunk `5080925` offsets `1016-1023`; context: In its decision, the Review Tribunal determined that it did not have the jurisdiction to deal with the matter before it because the issues being raised had already been finally decided by a different review tribunal, and therefore the principle of res judicata applied.

#### 23057:1:subtheme:2 · paragraphs 3-3

- Raw key terms: `another, applicant, back, collision, foot, hand, injuries, involved`
- Display key terms: `another, back, collision, foot, hand, injuries, involved`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: another, back, collision, foot, hand, injuries, involved Evidence spans paragraphs 3-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5080928` offsets `264-270`; context: As a result of the injuries, the Applicant has had on-going medical issues.

#### 23057:1:subtheme:3 · paragraphs 4-6

- Raw key terms: `applicant, benefits, dated, december, decision, denied, disability, disabled`
- Display key terms: `benefits, dated, december, denied, disability, disabled`
- Argument roles: `disposition, reasoning_application`
- Explanation: Observed roles: disposition, reasoning_application Display terms: benefits, dated, december, denied, disability, disabled Application context: [6] The Applicant applied for CPP Disability Benefits for the first time on October 10, 1995. | The tribunal concluded that the Applicant was not precluded from performing some type of substantially gainful employment, and was therefore not disabled within the meaning of paragraph 42(2)(a) of the Plan. Operative outcome context: [7] The Applicant’s initial application for CPP Disability Benefits was denied on December 18, 1995. | [8] In a decision dated February 25, 1999, the review tribunal dismissed the Applicant’s appeal. Evidence spans paragraphs 4-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5080929` offsets `18-25`; context: [6] The Applicant applied for CPP Disability Benefits for the first time on October 10, 1995.
- Evidence: `disposition` cue `denied` at chunk `5080930` offsets `72-78`; context: [7] The Applicant’s initial application for CPP Disability Benefits was denied on December 18, 1995.
- Evidence: `reasoning_application` cue `therefore` at chunk `5080931` offsets `228-237`; context: The tribunal concluded that the Applicant was not precluded from performing some type of substantially gainful employment, and was therefore not disabled within the meaning of paragraph 42(2)(a) of the Plan.
- Evidence: `disposition` cue `dismissed` at chunk `5080931` offsets `63-72`; context: [8] In a decision dated February 25, 1999, the review tribunal dismissed the Applicant’s appeal.

#### 23057:1:subtheme:4 · paragraphs 7-8

- Raw key terms: `applicant, application, benefits, disability, first, review, second, tribunal`
- Display key terms: `benefits, disability, first, review, second`
- Argument roles: `disposition, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, issue, party_position, reasoning_application Display terms: benefits, disability, first, review, second Position/evidence statements: [9] On May 20, 2003, the Applicant submitted a second application for CPP Disability Benefits. | At the same time, she made a request to re-open her first appeal on the basis additional medical reports, which she claimed raised new facts. Application context: [10] The Applicant applied to a second review tribunal to appeal the denial of her second CPP Disability Benefits application. Operative outcome context: Human Resources and Skills Development Canada denied the Applicant’s second application for CPP Disability Benefits on the grounds that the issue was res judicata, having already been determined finally by the first revi Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080932` offsets `235-240`; context: Human Resources and Skills Development Canada denied the Applicant’s second application for CPP Disability Benefits on the grounds that the issue was res judicata, having already been determined finally by the first review tribunal.
- Evidence: `party_position` cue `submitted` at chunk `5080932` offsets `35-44`; context: [9] On May 20, 2003, the Applicant submitted a second application for CPP Disability Benefits.
- Evidence: `disposition` cue `denied` at chunk `5080932` offsets `141-147`; context: Human Resources and Skills Development Canada denied the Applicant’s second application for CPP Disability Benefits on the grounds that the issue was res judicata, having already been determined finally by the first review tribunal.
- Evidence: `party_position` cue `claimed` at chunk `5080933` offsets `243-250`; context: At the same time, she made a request to re-open her first appeal on the basis additional medical reports, which she claimed raised new facts.
- Evidence: `reasoning_application` cue `applied` at chunk `5080933` offsets `19-26`; context: [10] The Applicant applied to a second review tribunal to appeal the denial of her second CPP Disability Benefits application.

#### 23057:1:subtheme:5 · paragraphs 9-16

- Raw key terms: `applicant, application, decision, appeal, appeals, review, board, dated`
- Display key terms: `appeals, review, dated`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: appeals, review, dated Application context: [13] On December 19, 2007, the Applicant applied to the Pension Appeals Board for an extension of time to file an appeal from the second review tribunal decision. Operative outcome context: [11] In a decision dated April 12, 2005, the review tribunal denied the appeal and the request to re-open the first appeal. | That application was denied by the Pension Appeals Board in a decision dated May 1, 2007. Evidence spans paragraphs 9-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080934` offsets `146-151`; context: It concluded that the issue of the Applicant’s eligibility for CPP Disability Benefits was res judicata, having been finally decided in the proceedings arising out of the Applicant’s first application.
- Evidence: `disposition` cue `denied` at chunk `5080934` offsets `61-67`; context: [11] In a decision dated April 12, 2005, the review tribunal denied the appeal and the request to re-open the first appeal.
- Evidence: `reasoning_application` cue `applied` at chunk `5080936` offsets `41-48`; context: [13] On December 19, 2007, the Applicant applied to the Pension Appeals Board for an extension of time to file an appeal from the second review tribunal decision.
- Evidence: `disposition` cue `denied` at chunk `5080936` offsets `184-190`; context: That application was denied by the Pension Appeals Board in a decision dated May 1, 2007.
- Evidence: `disposition` cue `quashed` at chunk `5080937` offsets `62-69`; context: [14] On April 24, 2009, Justice Campbell of the Federal Court quashed the Pension Appeals Board’s decision and sent the matter back for re-determination.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080938` offsets `175-183`; context: On September 16, 2010, the Pension Appeals Board dismissed the appeal, finding that the evidence submitted by the Applicant did not constitute “new facts.
- Evidence: `disposition` cue `granted` at chunk `5080938` offsets `48-55`; context: [15] On May 27, 2009, the Pension Appeals Board granted the Applicant leave to appeal.
- Evidence: `disposition` cue `dismissed` at chunk `5080939` offsets `214-223`; context: On May 18, 2011, the Federal Court of Appeal dismissed the application for judicial review, holding that the Pension Appeal Board’s decision reasonably concluded that the reports did not constitute new facts.
- Evidence: `disposition` cue `denied` at chunk `5080940` offsets `115-121`; context: The application was denied in a decision dated August 31, 2006.
- Evidence: `disposition` cue `upheld` at chunk `5080941` offsets `89-95`; context: [18] In a decision dated January 30, 2007, Human Resources and Skills Development Canada upheld the denial of her application.

#### 23057:1:subtheme:6 · paragraphs 17-18

- Raw key terms: `applicant, decision, review, third, tribunal, already, appeal, appeals`
- Display key terms: `review, third, already, appeals`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: review, third, already, appeals Application context: It found that the issue was already decided, and was therefore res judicata. | [20] On December 17, 2012, the Applicant applied to the Pension Appeals Board for leave to appeal the decision of the third Review Tribunal. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080942` offsets `368-373`; context: It found that the issue was already decided, and was therefore res judicata.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080942` offsets `274-282`; context: Its decision was issued on September 21, 2012, with the Review Tribunal finding that it had no jurisdiction to review all the evidence and substitute its decision for that of the first review tribunal.
- Evidence: `reasoning_application` cue `therefore` at chunk `5080942` offsets `403-412`; context: It found that the issue was already decided, and was therefore res judicata.
- Evidence: `reasoning_application` cue `applied` at chunk `5080943` offsets `41-48`; context: [20] On December 17, 2012, the Applicant applied to the Pension Appeals Board for leave to appeal the decision of the third Review Tribunal.

#### 23057:1:subtheme:7 · paragraphs 19-21

- Raw key terms: `appeal, applicant, application, leave, filed, review, tribunal, amend`
- Display key terms: `leave, filed, review, amend`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: leave, filed, review, amend Rule/authority context: Pursuant to section 260, which is a transitional provision of the enabling legislation, the Jobs, Growth and Long-term Prosperity Act, S. | THE DECISION UNDER REVIEW [24] In her decision, the Member of the SST provided a brief history of the proceedings leading up to the Applicant’s application for leave to appeal the decision of the Review Tribunal. Operative outcome context: [22] On July 16, 2013, the SST dismissed the Applicant’s application for leave to appeal. Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080944` offsets `217-228`; context: Pursuant to section 260, which is a transitional provision of the enabling legislation, the Jobs, Growth and Long-term Prosperity Act, S.
- Evidence: `disposition` cue `dismissed` at chunk `5080945` offsets `31-40`; context: [22] On July 16, 2013, the SST dismissed the Applicant’s application for leave to appeal.
- Evidence: `governing_rule` cue `UNDER` at chunk `5080946` offsets `391-396`; context: THE DECISION UNDER REVIEW [24] In her decision, the Member of the SST provided a brief history of the proceedings leading up to the Applicant’s application for leave to appeal the decision of the Review Tribunal.

#### 23057:1:subtheme:8 · paragraphs 22-24

- Raw key terms: `appeal, chance, member, reasonable, success, decision, pursuant, subsection`
- Display key terms: `chance, reasonable, success, pursuant, subsection`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: chance, reasonable, success, pursuant, subsection Rule/authority context: [25] Pursuant to subsection 58(2) of the Department of Human Resources and Skills Development Act, S. | As such, the determination of whether the application had a reasonable chance of success would be evaluated as a de novo appeal, pursuant to subsection 84(1) of the Plan, as it read immediately before April 1, 2013. Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080947` offsets `157-162`; context: 34 ( the “DHRSDA”) the Member identified the issue as whether the appeal from the Review Tribunal’s decision of September 21, 2012 had a reasonable chance of success.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080947` offsets `5-16`; context: [25] Pursuant to subsection 58(2) of the Department of Human Resources and Skills Development Act, S.
- Evidence: `issue` cue `whether` at chunk `5080948` offsets `227-234`; context: As such, the determination of whether the application had a reasonable chance of success would be evaluated as a de novo appeal, pursuant to subsection 84(1) of the Plan, as it read immediately before April 1, 2013.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5080948` offsets `326-337`; context: As such, the determination of whether the application had a reasonable chance of success would be evaluated as a de novo appeal, pursuant to subsection 84(1) of the Plan, as it read immediately before April 1, 2013.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080949` offsets `40-48`; context: [27] The Member noted that adducing new evidence, and demonstrating an error of law or a significant error of fact can demonstrate that an appeal has a reasonable chance of success, relying in this regard on the decision in Canada (Attorney General) v.

#### 23057:1:subtheme:9 · paragraphs 25-31

- Raw key terms: `review, applicant, argument, member, tribunal, found, appeal, application`
- Display key terms: `review, argument`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: review, argument Rule/authority context: Any application for leave to appeal filed before April 1, 2013 under subsection 83(1) of the Canada Pension Plan, as it read immediately before the coming into force of section 229, is deemed to be an application for lea Application context: The provisions of the Canada Pension Plan and Old Age Security Act repealed by this Act, and their related regulations, continue to apply to appeals of which a Review Tribunal or the Pension Appeals Board remains seized  Evidence spans paragraphs 25-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5080950` offsets `289-295`; context: [28] In response to the Applicant’s argument that her matter was not properly considered at prior hearings before the third Review Tribunal, the Member found that the decisions of the previous Review Tribunals were final, and that the Review Tribunal did not have jurisdiction to consider issues relating to those decisions.
- Evidence: `evidence_fact` cue `found that` at chunk `5080950` offsets `152-162`; context: [28] In response to the Applicant’s argument that her matter was not properly considered at prior hearings before the third Review Tribunal, the Member found that the decisions of the previous Review Tribunals were final, and that the Review Tribunal did not have jurisdiction to consider issues relating to those decisions.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080951` offsets `430-438`; context: The Member noted that neither argument presented new evidence, nor pointed to a reviewable error in fact or law by the Review Tribunal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080954` offsets `117-125`; context: [32] The Member refused the application for leave to appeal on the basis that the Applicant had not produced any new evidence, nor pointed to an error in fact or law, nor presented any argument that would have a reasonable chance of success.
- Evidence: `governing_rule` cue `under` at chunk `5080956` offsets `150-155`; context: Any application for leave to appeal filed before April 1, 2013 under subsection 83(1) of the Canada Pension Plan, as it read immediately before the coming into force of section 229, is deemed to be an application for leave to appeal filed with the Appeal Division of the Social Security Tribunal on April 1, 2013, if no decision has been rendered with respect to leave to appeal.
- Evidence: `reasoning_application` cue `apply` at chunk `5080956` offsets `1025-1030`; context: The provisions of the Canada Pension Plan and Old Age Security Act repealed by this Act, and their related regulations, continue to apply to appeals of which a Review Tribunal or the Pension Appeals Board remains seized under this Act, with any necessary adaptations.

#### 23057:1:subtheme:10 · paragraphs 32-36

- Raw key terms: `applicant, argues, appeal, application, certain, leave, reports, submits`
- Display key terms: `argues, certain, leave, reports, submits`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: argues, certain, leave, reports, submits Position/evidence statements: [39] The Applicant argues that the SST erred in denying her application for leave to appeal. | [40] The Applicant submits that these reports raise new material facts that were not previously discoverable with reasonable diligence. Rule/authority context: What is the appropriate standard of review; and 2. | Respondent’s Submissions [43] The Respondent submits that the appropriate standard of review of the decision to deny leave to appeal is reasonableness. Application context: As well, she submits that the condition of the review tribunal file, concerning her third application for CPP Disability Benefits, gave rise to a breach of procedural fairness because the pages were not numbered. Operative outcome context: She submits that she is disabled within the meaning of paragraph 42(2)(a) of the Plan, and that she should be allowed to submit certain medical reports that she considers new facts, in order to show that she is disabled. | She argues that the refusal to admit the reports has denied her the right to a fair hearing. Evidence spans paragraphs 32-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5080957` offsets `585-592`; context: (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `5080957` offsets `637-643`; context: (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `standard of review` at chunk `5080957` offsets `1655-1673`; context: What is the appropriate standard of review; and
2.
- Evidence: `counterargument_limitation` cue `However` at chunk `5080957` offsets `157-164`; context: However, the relevant provisions of the statute have not changed.
- Evidence: `party_position` cue `argues` at chunk `5080958` offsets `19-25`; context: [39] The Applicant argues that the SST erred in denying her application for leave to appeal.
- Evidence: `disposition` cue `allowed` at chunk `5080958` offsets `203-210`; context: She submits that she is disabled within the meaning of paragraph 42(2)(a) of the Plan, and that she should be allowed to submit certain medical reports that she considers new facts, in order to show that she is disabled.
- Evidence: `party_position` cue `submits` at chunk `5080959` offsets `19-26`; context: [40] The Applicant submits that these reports raise new material facts that were not previously discoverable with reasonable diligence.
- Evidence: `party_position` cue `argues` at chunk `5080960` offsets `93-99`; context: She argues that the refusal to admit the reports has denied her the right to a fair hearing.
- Evidence: `disposition` cue `denied` at chunk `5080960` offsets `142-148`; context: She argues that the refusal to admit the reports has denied her the right to a fair hearing.
- Evidence: `party_position` cue `argues` at chunk `5080961` offsets `24-30`; context: [42] The Applicant also argues that certain information that she requested from the Minister and the Office of the Commissioner of Review Tribunals was not produced.
- Evidence: `governing_rule` cue `standard of review` at chunk `5080961` offsets `456-474`; context: Respondent’s Submissions [43] The Respondent submits that the appropriate standard of review of the decision to deny leave to appeal is reasonableness.
- Evidence: `reasoning_application` cue `because` at chunk `5080961` offsets `342-349`; context: As well, she submits that the condition of the review tribunal file, concerning her third application for CPP Disability Benefits, gave rise to a breach of procedural fairness because the pages were not numbered.

#### 23057:1:subtheme:11 · paragraphs 37-39

- Raw key terms: `appeal, leave, respondent, test, argues, dhrsda, granting, grounds`
- Display key terms: `leave, argues, dhrsda, granting, grounds`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: leave, argues, dhrsda, granting, grounds Position/evidence statements: [44] The Respondent then argues that the issue of whether the Tribunal selected the correct test for granting leave to appeal is likewise reviewable on the standard of reasonableness. | [45] The Respondent submits that previously, the test for leave to appeal was whether there was an “arguable case”. Rule/authority context: Pursuant to subsection 58(2) of the DHRSDA, there is a new test for granting leave to appeal, that is whether the appeal has a “reasonable chance of success. Evidence spans paragraphs 37-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080962` offsets `41-46`; context: [44] The Respondent then argues that the issue of whether the Tribunal selected the correct test for granting leave to appeal is likewise reviewable on the standard of reasonableness.
- Evidence: `party_position` cue `argues` at chunk `5080962` offsets `25-31`; context: [44] The Respondent then argues that the issue of whether the Tribunal selected the correct test for granting leave to appeal is likewise reviewable on the standard of reasonableness.
- Evidence: `issue` cue `whether` at chunk `5080963` offsets `78-85`; context: [45] The Respondent submits that previously, the test for leave to appeal was whether there was an “arguable case”.
- Evidence: `party_position` cue `submits` at chunk `5080963` offsets `20-27`; context: [45] The Respondent submits that previously, the test for leave to appeal was whether there was an “arguable case”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080963` offsets `559-567`; context: The new test does not include the submission and consideration of new evidence.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080963` offsets `116-127`; context: Pursuant to subsection 58(2) of the DHRSDA, there is a new test for granting leave to appeal, that is whether the appeal has a “reasonable chance of success.
- Evidence: `party_position` cue `argues` at chunk `5080964` offsets `20-26`; context: [46] The Respondent argues that although the Member appears to have analysed the Applicant’s application for leave based on the former test, the grounds of appeal set out in subsection 58(1) of the DHRSDA were still addressed in her decision.

#### 23057:1:subtheme:12 · paragraphs 40-41

- Raw key terms: `applicant, facts, judicata, previous, reasonable, submits, already, analysis`
- Display key terms: `facts, judicata, previous, reasonable, submits, already, analysis`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: facts, judicata, previous, reasonable, submits, already, analysis Position/evidence statements: [47] He submits that the doctrine of res judicata applies, and that the Member’s decision to deny leave was reasonable. | [48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Appl Application context: [47] He submits that the doctrine of res judicata applies, and that the Member’s decision to deny leave was reasonable. | [48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Appl Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5080965` offsets `315-321`; context: As well, he argues that the Applicant has failed to provide new facts that would justify re-opening the decision of the first review tribunal, and that the SST had no authority to reconsider the issues that were before the previous two review tribunals or the Pension Appeals Board.
- Evidence: `party_position` cue `submits` at chunk `5080965` offsets `8-15`; context: [47] He submits that the doctrine of res judicata applies, and that the Member’s decision to deny leave was reasonable.
- Evidence: `reasoning_application` cue `applies` at chunk `5080965` offsets `50-57`; context: [47] He submits that the doctrine of res judicata applies, and that the Member’s decision to deny leave was reasonable.
- Evidence: `issue` cue `issue` at chunk `5080966` offsets `345-350`; context: That issue is res judicata.
- Evidence: `party_position` cue `submits` at chunk `5080966` offsets `29-36`; context: [48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Applicant, specifically the reports of Drs.
- Evidence: `evidence_fact` cue `determined that` at chunk `5080966` offsets `170-185`; context: [48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Applicant, specifically the reports of Drs.
- Evidence: `reasoning_application` cue `because` at chunk `5080966` offsets `128-135`; context: [48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Applicant, specifically the reports of Drs.

#### 23057:1:subtheme:13 · paragraphs 42-43

- Raw key terms: `fairness, file, procedural, review, tribunal, address, administrative, appeal`
- Display key terms: `fairness, file, procedural, review, address, administrative`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: fairness, file, procedural, review, address, administrative Position/evidence statements: [49] Finally, the Respondent submits that the Applicant’s complaint that the third Review Tribunal did not return the tribunal file to her is an administrative complaint that is irrelevant to this application. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5080967` offsets `430-436`; context: Issues of procedural fairness are reviewable on the standard of correctness; see the decision in Canada (Citizenship and Immigration) v.
- Evidence: `party_position` cue `submits` at chunk `5080967` offsets `29-36`; context: [49] Finally, the Respondent submits that the Applicant’s complaint that the third Review Tribunal did not return the tribunal file to her is an administrative complaint that is irrelevant to this application.
- Evidence: `evidence_fact` cue `record` at chunk `5080968` offsets `114-120`; context: [51] In my opinion, there has been no breach of procedural fairness in respect of the preparation of the tribunal record.

#### 23057:1:subtheme:14 · paragraphs 44-48

- Raw key terms: `decision, appeal, appeals, application, board, leave, pension, similar`
- Display key terms: `appeals, leave, pension, similar`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: appeals, leave, pension, similar Rule/authority context: [54] The SST is a new federal tribunal that replaced the Pension Appeals Board as of April 1, 2013 pursuant to section 260 of the Jobs, Growth and Long-term Prosperity Act. | [56] The grounds for appeal and the test for granting leave to appeal have changed under the new legislation; however, the process for applying for leave to appeal is substantially similar to that of the previous regime  Application context: [56] The grounds for appeal and the test for granting leave to appeal have changed under the new legislation; however, the process for applying for leave to appeal is substantially similar to that of the previous regime  Evidence spans paragraphs 44-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5080969` offsets `80-85`; context: [52] Further, the fact that the records were not admitted into the record is an issue related to the merits of the decision since those records were deemed to not constitute new facts.
- Evidence: `evidence_fact` cue `record` at chunk `5080969` offsets `67-73`; context: [52] Further, the fact that the records were not admitted into the record is an issue related to the merits of the decision since those records were deemed to not constitute new facts.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5080971` offsets `99-110`; context: [54] The SST is a new federal tribunal that replaced the Pension Appeals Board as of April 1, 2013 pursuant to section 260 of the Jobs, Growth and Long-term Prosperity Act.
- Evidence: `governing_rule` cue `under` at chunk `5080973` offsets `83-88`; context: [56] The grounds for appeal and the test for granting leave to appeal have changed under the new legislation; however, the process for applying for leave to appeal is substantially similar to that of the previous regime and as such, the same analysis will continue to apply in judicial review of decisions made under the new scheme.
- Evidence: `reasoning_application` cue `apply` at chunk `5080973` offsets `268-273`; context: [56] The grounds for appeal and the test for granting leave to appeal have changed under the new legislation; however, the process for applying for leave to appeal is substantially similar to that of the previous regime and as such, the same analysis will continue to apply in judicial review of decisions made under the new scheme.
- Evidence: `counterargument_limitation` cue `however` at chunk `5080973` offsets `110-117`; context: [56] The grounds for appeal and the test for granting leave to appeal have changed under the new legislation; however, the process for applying for leave to appeal is substantially similar to that of the previous regime and as such, the same analysis will continue to apply in judicial review of decisions made under the new scheme.

#### 23057:1:subtheme:15 · paragraphs 49-50

- Raw key terms: `applied, canada, consiglio, correct, decision, first, inquiry, paragraph`
- Display key terms: `applied, consiglio, correct, first, inquiry, paragraph`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: applied, consiglio, correct, first, inquiry, paragraph Rule/authority context: [57] Under the previous scheme, this Court held that judicial review of decisions to grant or refuse an application for leave to appeal involves a two-step inquiry. Application context: First, the Court must ask whether the tribunal applied the correct test, and second, whether a reviewable error was made in determining whether the requirements of the test were made out; see the decision in Consiglio v. | [58] The first question, that is whether the correct test was applied, is reviewable on the correctness standard; see the decision in Zakaria, supra at paragraph 35. Evidence spans paragraphs 49-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5080974` offsets `191-198`; context: First, the Court must ask whether the tribunal applied the correct test, and second, whether a reviewable error was made in determining whether the requirements of the test were made out; see the decision in Consiglio v.
- Evidence: `governing_rule` cue `Under` at chunk `5080974` offsets `5-10`; context: [57] Under the previous scheme, this Court held that judicial review of decisions to grant or refuse an application for leave to appeal involves a two-step inquiry.
- Evidence: `reasoning_application` cue `applied` at chunk `5080974` offsets `212-219`; context: First, the Court must ask whether the tribunal applied the correct test, and second, whether a reviewable error was made in determining whether the requirements of the test were made out; see the decision in Consiglio v.
- Evidence: `issue` cue `question` at chunk `5080975` offsets `15-23`; context: [58] The first question, that is whether the correct test was applied, is reviewable on the correctness standard; see the decision in Zakaria, supra at paragraph 35.
- Evidence: `reasoning_application` cue `applied` at chunk `5080975` offsets `62-69`; context: [58] The first question, that is whether the correct test was applied, is reviewable on the correctness standard; see the decision in Zakaria, supra at paragraph 35.

#### 23057:1:subtheme:16 · paragraphs 51-52

- Raw key terms: `question, reasonableness, standard, adoption, agree, although, appeal, applied`
- Display key terms: `question, reasonableness, standard, adoption, agree, although, applied`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: question, reasonableness, standard, adoption, agree, although, applied Rule/authority context: Earlier jurisprudence applied the correctness standard of review to the question of choosing the right test. Application context: Adoption of the reasonableness standard could lead to uncertainty as to what test is to be applied in deciding to grant leave. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5080976` offsets `74-82`; context: [59] I do not agree with the submissions of the Respondent that the first question is reviewable on a standard of reasonableness.
- Evidence: `issue` cue `question` at chunk `5080977` offsets `109-117`; context: [60] Although granting or refusing leave to appeal involves an interpretation of the SST’s home statute, the question of whether the correct test was selected by the Member only has two possible outcomes: either the correct test was selected or it was not.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5080977` offsets `392-405`; context: Earlier jurisprudence applied the correctness standard of review to the question of choosing the right test.
- Evidence: `reasoning_application` cue `applied` at chunk `5080977` offsets `348-355`; context: Adoption of the reasonableness standard could lead to uncertainty as to what test is to be applied in deciding to grant leave.

#### 23057:1:subtheme:17 · paragraphs 53-56

- Raw key terms: `appeal, test, application, canada, chance, decision, leave, member`
- Display key terms: `chance, leave`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: chance, leave Rule/authority context: [63] The test for granting leave to appeal under the current legislation is to be discerned from the provisions of the DHRSDA. | [64] The test under the former regime was one developed by the jurisprudence, that is, at common law. Evidence spans paragraphs 53-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5080978` offsets `26-33`; context: [61] I will first address whether the Member selected the correct test for assessing the application for leave to appeal.
- Evidence: `issue` cue `whether` at chunk `5080979` offsets `247-254`; context: For this reason, the determination of whether the appeal has a reasonable chance of success will be made on the basis of an appeal de novo in accordance with subsection 84(1) of the Canada Pension Plan (CPP) as it read immediately before April 1, 2013.
- Evidence: `governing_rule` cue `under` at chunk `5080980` offsets `43-48`; context: [63] The test for granting leave to appeal under the current legislation is to be discerned from the provisions of the DHRSDA.
- Evidence: `governing_rule` cue `under` at chunk `5080981` offsets `14-19`; context: [64] The test under the former regime was one developed by the jurisprudence, that is, at common law.

#### 23057:1:subtheme:18 · paragraphs 57-66

- Raw key terms: `appeal, leave, subsection, application, basis, common, considered, decision`
- Display key terms: `leave, subsection, basis, common, considered`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: leave, subsection, basis, common, considered Rule/authority context: [65] Under the former regime an appellant could rely on the submission of new material facts to establish an arguable case. | [69] Pursuant to section 260, which is a transitional provision of the Jobs, Growth and Long-term Prosperity Act, the Applicant’s application for leave to appeal was deemed to be filed with the SST on April 1, 2013. Application context: whether the decision maker has applied the right test – that is, whether the application raises an arguable case without otherwise assessing the merits of the application, and 2. | This test is narrower than the test that was previously applied, which did not list grounds of appeal. Evidence spans paragraphs 57-66. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5080982` offsets `368-374`; context: I refer to the decision in Callihoo, supra at paragraph 15 where the Court said the following:
On the basis of this recent jurisprudence, in my view the review of a decision concerning an application for leave to appeal to the PAB involves two issues,
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080982` offsets `692-700`; context: If new evidence is adduced with the application, if the application raises an issue of law or of relevant significant facts not appropriate considered by the Review Tribunal in its decision, an arguable issue is raised for consideration and it warrants the grant of leave.
- Evidence: `governing_rule` cue `Under` at chunk `5080982` offsets `5-10`; context: [65] Under the former regime an appellant could rely on the submission of new material facts to establish an arguable case.
- Evidence: `reasoning_application` cue `applied` at chunk `5080982` offsets `410-417`; context: whether the decision maker has applied the right test – that is, whether the application raises an arguable case without otherwise assessing the merits of the application, and
2.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080986` offsets `5-16`; context: [69] Pursuant to section 260, which is a transitional provision of the Jobs, Growth and Long-term Prosperity Act, the Applicant’s application for leave to appeal was deemed to be filed with the SST on April 1, 2013.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080987` offsets `5-16`; context: [70] Pursuant to subsection 58(2) of the DHRSDA, which is the legislation governing appeals to the SST, leave to appeal to the SST is refused if the appeal has no reasonable chance of success.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5080988` offsets `5-16`; context: [71] Pursuant to subsection 58(1), there are now only three grounds of appeal, first, a breach of natural justice; second, an error law; and third, an erroneous finding of fact made in a perverse and capricious manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080990` offsets `263-271`; context: Adducing new evidence is no longer a ground of appeal, and the Member erred in considering it as such.
- Evidence: `governing_rule` cue `Under` at chunk `5080990` offsets `5-10`; context: [73] Under the current legislation, an appeal will only have a reasonable chance of success if it is based on one of the three enumerated grounds.
- Evidence: `reasoning_application` cue `applied` at chunk `5080990` offsets `203-210`; context: This test is narrower than the test that was previously applied, which did not list grounds of appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5080991` offsets `167-175`; context: Rather, she relied on the common law factors of adducing new evidence, or demonstrating an error of law or significant error of fact, as addressed in Zakaria, supra.

#### 23057:1:subtheme:19 · paragraphs 67-68

- Raw key terms: `applicant, application, erred, fact, member, notwithstanding, opinion, acted`
- Display key terms: `erred, fact, notwithstanding, opinion, acted`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: erred, fact, notwithstanding, opinion, acted Rule/authority context: She did not have discretion to deviate from that statutory regime and apply the former test, notwithstanding the fact that the Applicant applied for leave to appeal prior to the introduction of new legislation governing  Application context: [75] In my opinion, the Member was required to apply the test set out in section 58 of the DHRSDA. Evidence spans paragraphs 67-68. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5080992` offsets `449-456`; context: I find that the Member erred by failing to apply the correct test in determining whether or not to grant the Applicant’s application for leave to appeal.
- Evidence: `governing_rule` cue `under` at chunk `5080992` offsets `352-357`; context: She did not have discretion to deviate from that statutory regime and apply the former test, notwithstanding the fact that the Applicant applied for leave to appeal prior to the introduction of new legislation governing applications for leave to appeal under the Plan.
- Evidence: `reasoning_application` cue `apply` at chunk `5080992` offsets `47-52`; context: [75] In my opinion, the Member was required to apply the test set out in section 58 of the DHRSDA.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5080992` offsets `192-207`; context: She did not have discretion to deviate from that statutory regime and apply the former test, notwithstanding the fact that the Applicant applied for leave to appeal prior to the introduction of new legislation governing applications for leave to appeal under the Plan.

#### Section text

Belo-Alves v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2014-11-21
Neutral citation
2014 FC 1100
File numbers
T-1823-13
Notes
A correction was made on August 5, 2015
Reported Decision
Decision Content
Date: 20141121
Docket: T-1823-13
Citation: 2014 FC 1100
Ottawa, Ontario, November 21, 2014
PRESENT: The Honourable Madam Justice Heneghan
BETWEEN:
GUIDA BELO-ALVES
Applicant
and
THE ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. INTRODUCTION [1] Ms. Guida Belo-Alves (the “Applicant”) seeks judicial review, pursuant to section 18.1 of the Federal Courts Act, R.S.C. 1985, c-7 (the “Federal Courts Act”), of a decision dated July 16, 2013 of a Member (the “Member”) of the Appeal Division of the Social Security Tribunal (the “SST” or the “Tribunal”), refusing the Applicant leave to appeal a decision of a Review Tribunal (the “Review Tribunal”). In its decision, the Review Tribunal determined that it did not have the jurisdiction to deal with the matter before it because the issues being raised had already been finally decided by a different review tribunal, and therefore the principle of res judicata applied.
II. BACKGROUND [2] This matter has a long and complicated history, arising out of a series of claims made by the Applicant for Canada Pension Plan Disability Benefits (“CPP Disability Benefits”), pursuant to paragraph 42(2)(a) of the Canada Pension Plan, R.S.C. 1985, c-8 (the “Plan”). The following facts are taken from the Tribunal Record and the Application Records filed by the Applicant and the Respondent.

[3] The Applicant was previously employed as a “systems coordinator” in a dress manufacturing company and a part-time translator for the Immigration Department at the Toronto Airport.

[4] In September 1988, the Applicant was involved in a motor vehicle collision. As a result of the collision, the Applicant suffered a whiplash type injury. She returned to work after the injury, but required physiotherapy.

[5] In May 1989, the Applicant was again involved in another, more serious motor vehicle collision, which resulted in serious injuries to her scalp, neck, back, left foot and knee and right hand. As a result of the injuries, the Applicant has had on-going medical issues. She has not worked as of May 6, 1989.

[6] The Applicant applied for CPP Disability Benefits for the first time on October 10, 1995. The Applicant’s Minimum Qualifying Period (“MQP”), that is, the date by which she would have qualified for CPP Disability Benefits by demonstrating she was disabled, was, and remains, December 31, 1996.

[7] The Applicant’s initial application for CPP Disability Benefits was denied on December 18, 1995. In a decision dated September 10, 1997, the Minister of Human Resources and Skills Development upheld the denial. The Applicant appealed this decision to a review tribunal of the Office of the Commissioner of Review Tribunals.

[8] In a decision dated February 25, 1999, the review tribunal dismissed the Applicant’s appeal. The tribunal concluded that the Applicant was not precluded from performing some type of substantially gainful employment, and was therefore not disabled within the meaning of paragraph 42(2)(a) of the Plan. Leave to appeal to the Pension Appeals Board was denied.

[9] On May 20, 2003, the Applicant submitted a second application for CPP Disability Benefits. Human Resources and Skills Development Canada denied the Applicant’s second application for CPP Disability Benefits on the grounds that the issue was res judicata, having already been determined finally by the first review tribunal.

[10] The Applicant applied to a second review tribunal to appeal the denial of her second CPP Disability Benefits application. At the same time, she made a request to re-open her first appeal on the basis additional medical reports, which she claimed raised new facts. The hearing before the second review tribunal took place on March 10, 2005.

[11] In a decision dated April 12, 2005, the review tribunal denied the appeal and the request to re-open the first appeal. It concluded that the issue of the Applicant’s eligibility for CPP Disability Benefits was res judicata, having been finally decided in the proceedings arising out of the Applicant’s first application.

[12] In relation to the new facts application, the review tribunal concluded that the reports presented either did not constitute new facts, or were established too long after the Applicant’s MQP of December 31, 1996 to assist in evaluating her conditions at the time of her MQP.

[13] On December 19, 2007, the Applicant applied to the Pension Appeals Board for an extension of time to file an appeal from the second review tribunal decision. That application was denied by the Pension Appeals Board in a decision dated May 1, 2007. The Applicant applied for judicial review of that decision.

[14] On April 24, 2009, Justice Campbell of the Federal Court quashed the Pension Appeals Board’s decision and sent the matter back for re-determination.

[15] On May 27, 2009, the Pension Appeals Board granted the Applicant leave to appeal. On September 16, 2010, the Pension Appeals Board dismissed the appeal, finding that the evidence submitted by the Applicant did not constitute “new facts.”

[16] On October 18th, 2010, the Applicant filed a Notice of Application for judicial review of the decision of the Pension Appeals Board in the Federal Court of Appeal. On May 18, 2011, the Federal Court of Appeal dismissed the application for judicial review, holding that the Pension Appeal Board’s decision reasonably concluded that the reports did not constitute new facts.

[17] On December 19, 2005, the Applicant made a third application for CPP Disability Benefits. The application was denied in a decision dated August 31, 2006. The Applicant sought reconsideration of the denial.

[18] In a decision dated January 30, 2007, Human Resources and Skills Development Canada upheld the denial of her application. The Applicant once again appealed the decision to the Review Tribunal. The hearing of the third appeal was held in abeyance until various appeals in relation to her second application for CPP Disability Benefits were resolved.

[19] On July 31, 2012, the hearing for the denial of the Applicant’s third claim for CPP Disability Benefits took place before the Review Tribunal. Its decision was issued on September 21, 2012, with the Review Tribunal finding that it had no jurisdiction to review all the evidence and substitute its decision for that of the first review tribunal. It found that the issue was already decided, and was therefore res judicata.

[20] On December 17, 2012, the Applicant applied to the Pension Appeals Board for leave to appeal the decision of the third Review Tribunal.

[21] On April 1, 2013, the Office of the Commissioner of Review Tribunals and the Pension Appeals Board were replaced by the Social Security Tribunal – General Division and Social Security Tribunal – Appeal Division. Pursuant to section 260, which is a transitional provision of the enabling legislation, the Jobs, Growth and Long-term Prosperity Act, S.C. 2012 c. 19 (the “Jobs, Growth and Long-term Prosperity Act”) the Applicant’s application for leave to appeal was treated as if it had been filed with the SST on April 1, 2013.

[22] On July 16, 2013, the SST dismissed the Applicant’s application for leave to appeal.

[23] On August 8, 2013, the Applicant filed her Notice of Application for judicial review in the Federal Court of Appeal. In an Order dated October 31, 2013, Justice Stratas of the Federal Court of Appeal transferred the application for judicial review to the Federal Court. On November 14, 2013, Justice Roy of the Federal Court made an Order to amend the style of cause.
III. THE DECISION UNDER REVIEW [24] In her decision, the Member of the SST provided a brief history of the proceedings leading up to the Applicant’s application for leave to appeal the decision of the Review Tribunal.

[25] Pursuant to subsection 58(2) of the Department of Human Resources and Skills Development Act, S.C. 2005 c. 34 ( the “DHRSDA”) the Member identified the issue as whether the appeal from the Review Tribunal’s decision of September 21, 2012 had a reasonable chance of success.

[26] The Member held that the Application would be examined on the basis of the legitimate expectations of the Applicant at the time the leave application was filed with the Pension Appeals Board. As such, the determination of whether the application had a reasonable chance of success would be evaluated as a de novo appeal, pursuant to subsection 84(1) of the Plan, as it read immediately before April 1, 2013.

[27] The Member noted that adducing new evidence, and demonstrating an error of law or a significant error of fact can demonstrate that an appeal has a reasonable chance of success, relying in this regard on the decision in Canada (Attorney General) v. Zakaria, 2011 FC 136.

[28] In response to the Applicant’s argument that her matter was not properly considered at prior hearings before the third Review Tribunal, the Member found that the decisions of the previous Review Tribunals were final, and that the Review Tribunal did not have jurisdiction to consider issues relating to those decisions.

[29] The Member concluded that the Applicant’s argument that the third Review Tribunal did not return the review tribunal file to her was not a ground of appeal that had a reasonable chance of success. The Member found there was also no reasonable chance of success for the Applicant’s argument related to the administrative procedures with the Plan disability appeal process. The Member noted that neither argument presented new evidence, nor pointed to a reviewable error in fact or law by the Review Tribunal.

[30] The Member found there was no merit to the Applicant’s argument that the Review Tribunal did not provide a complete file for the hearing. The Member observed that it is the obligation of the parties to a proceeding to ensure that the tribunal has all relevant material before it.

[31] Finally, the Member considered the Applicant’s argument that the Review Tribunal discriminated against her and her children. The Member found the Applicant’s arguments relative to this complaint to be unclear, and consequently, did not have a reasonable chance of success. In this regard, the Member relied on the decision in Pantic v. Canada (Attorney General), 2011 FC 591.

[32] The Member refused the application for leave to appeal on the basis that the Applicant had not produced any new evidence, nor pointed to an error in fact or law, nor presented any argument that would have a reasonable chance of success.
IV. RELEVANT LEGISLATION [33] The following legislation is relevant to this application for judicial review:

[34] Paragraph 42(2)(a) of the Plan states:
42(2) For the purposes of this Act,
(a) a person shall be considered to be disabled only if he is determined in prescribed manner to have a severe and prolonged mental or physical disability, and for the purposes of this paragraph,
(i) a disability is severe only if by reason thereof the person in respect of whom the determination is made is incapable regularly of pursuing any substantially gainful occupation, and
(ii) a disability is prolonged only if it is determined in prescribed manner that the disability is likely to be long continued and of indefinite duration or is likely to result in death; and
…
42(2) Pour l’application de la présente loi :
a) une personne n’est considérée comme invalide que si elle est déclarée, de la manière prescrite, atteinte d’une invalidité physique ou mentale grave et prolongée, et pour l’application du présent alinéa :
(i) une invalidité n’est grave que si elle rend la personne à laquelle se rapporte la déclaration régulièrement incapable de détenir une occupation véritablement rémunératrice,
(ii) une invalidité n’est prolongée que si elle est déclarée, de la manière prescrite, devoir vraisemblablement durer pendant une période longue, continue et indéfinie ou devoir entraîner vraisemblablement le décès;
…

[35] Sections 260 and 262 of the Jobs, Growth and Long-term Prosperity Act state:
260. Any application for leave to appeal filed before April 1, 2013 under subsection 83(1) of the Canada Pension Plan, as it read immediately before the coming into force of section 229, is deemed to be an application for leave to appeal filed with the Appeal Division of the Social Security Tribunal on April 1, 2013, if no decision has been rendered with respect to leave to appeal.
260. Toute demande de permission d’interjeter appel présentée avant le 1er avril 2013, au titre du paragraphe 83(1) du Régime de pensions du Canada, dans sa version antérieure à l’entrée en vigueur de l’article 229, est réputée être une demande de permission d’en appeler présentée le 1er avril 2013 à la division d’appel du Tribunal de la sécurité sociale si aucune décision n’a été rendue relativement à cette demande.
262. The provisions of the Canada Pension Plan and Old Age Security Act repealed by this Act, and their related regulations, continue to apply to appeals of which a Review Tribunal or the Pension Appeals Board remains seized under this Act, with any necessary adaptations.
262. Les dispositions du Régime de pensions du Canada et de la Loi sur la sécurité de la vieillesse abrogées par la présente loi et leurs règlements continuent de s’appliquer, avec les adaptations nécessaires, aux appels dont un tribunal de révision ou la Commission d’appel des pensions demeure saisi au titre de la présente loi.

[36] The DHRSDA, which is the legislation governing the SST has since been renamed the Department of Employment and Social Development Act, S.C. 2005 c. 34. However, the relevant provisions of the statute have not changed. In any event, at the time the Member made her decision, subsections 58(1) and 58(2) of the DHRSDA read as follows:
58. (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
58. (1) Les seuls moyens d’appel sont les suivants :
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.
V. ISSUES [37] This application for judicial review raises the following two issues:
1. What is the appropriate standard of review; and
2. Did the SST commit a reviewable error in refusing the Applicant’s application for leave to appeal the decision of the third Review Tribunal.
VI. SUBMISSIONS A. Applicant’s Submissions [38] The Applicant did not make submissions on the appropriate standard of review.

[39] The Applicant argues that the SST erred in denying her application for leave to appeal. She submits that she is disabled within the meaning of paragraph 42(2)(a) of the Plan, and that she should be allowed to submit certain medical reports that she considers new facts, in order to show that she is disabled.

[40] The Applicant submits that these reports raise new material facts that were not previously discoverable with reasonable diligence. She argues that there are certain disability claims that must be assessed as a claimant’s condition, treatment, and prognosis evolve.

[41] As well, the Applicant pleads that there have been breaches of procedural fairness. She argues that the refusal to admit the reports has denied her the right to a fair hearing.

[42] The Applicant also argues that certain information that she requested from the Minister and the Office of the Commissioner of Review Tribunals was not produced. As well, she submits that the condition of the review tribunal file, concerning her third application for CPP Disability Benefits, gave rise to a breach of procedural fairness because the pages were not numbered.
B. Respondent’s Submissions [43] The Respondent submits that the appropriate standard of review of the decision to deny leave to appeal is reasonableness.

[44] The Respondent then argues that the issue of whether the Tribunal selected the correct test for granting leave to appeal is likewise reviewable on the standard of reasonableness. In this regard, he relies on the decisions in Alberta (Information and Privacy Commissioner) v. Alberta Teachers’ Association, [2011] 3 S.C.R. 654 at paragraph 30 and Agraira v. Canada (Public Safety and Emergency Preparedness), [2013] 2 S.C.R. 559.

[45] The Respondent submits that previously, the test for leave to appeal was whether there was an “arguable case”. Pursuant to subsection 58(2) of the DHRSDA, there is a new test for granting leave to appeal, that is whether the appeal has a “reasonable chance of success.” Subsection 58(1) specifically sets out the grounds for appeal, that is a failure to observe a principle of natural justice; an error of law; or an erroneous finding of fact made in a perverse or capricious manner. The new test does not include the submission and consideration of new evidence.

[46] The Respondent argues that although the Member appears to have analysed the Applicant’s application for leave based on the former test, the grounds of appeal set out in subsection 58(1) of the DHRSDA were still addressed in her decision.

[47] He submits that the doctrine of res judicata applies, and that the Member’s decision to deny leave was reasonable. As well, he argues that the Applicant has failed to provide new facts that would justify re-opening the decision of the first review tribunal, and that the SST had no authority to reconsider the issues that were before the previous two review tribunals or the Pension Appeals Board.

[48] Further, the Respondent submits that the Applicant does not have a reasonable chance of success in the present application because previous proceedings have already determined that the evidence presented by the Applicant, specifically the reports of Drs. Esperanca and Brock and the Sleep Analysis report, do not constitute new facts. That issue is res judicata.

[49] Finally, the Respondent submits that the Applicant’s complaint that the third Review Tribunal did not return the tribunal file to her is an administrative complaint that is irrelevant to this application. The Respondent argues that this complaint is not a ground of appeal that has a reasonable chance of success.
VII. DISCUSSION AND DISPOSITION [50] I will first address the Applicant’s arguments about procedural fairness. Issues of procedural fairness are reviewable on the standard of correctness; see the decision in Canada (Citizenship and Immigration) v. Khosa, [2009] 1 S.C.R. 339 at paragraph 43.

[51] In my opinion, there has been no breach of procedural fairness in respect of the preparation of the tribunal record. The fact that pages were not numbered in the review tribunal’s file is immaterial and does not give rise to a breach of procedural fairness.

[52] Further, the fact that the records were not admitted into the record is an issue related to the merits of the decision since those records were deemed to not constitute new facts. That issue is re

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23057:2 · paragraphs 69-78

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6783c18cc4a79e10fcdcd66eb355640d48e4c8ef345c1600d48fdec8aae246c3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23057:2:subtheme:1 · paragraphs 69-73

- Raw key terms: `decision, filed, applicant, application, apply, canada, court, doctrine`
- Display key terms: `filed, apply, doctrine`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: filed, apply, doctrine Rule/authority context: 1985 c I-21 states that where a former enactment is repealed and replaced by a new enactment, proceedings commenced under the former enactment are to be continued in conformity with the new enactment, insofar as it is po Application context: [79] In the present case, the transitional provisions of the Jobs, Growth and Long-term Prosperity Act provide that the provisions of the Plan repealed by that statute continue to apply to matters for which the Pension A | That doctrine applies to questions of procedural fairness; see the decision in Baker v. Evidence spans paragraphs 69-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `5080994` offsets `354-362`; context: In this regard, I refer to the decision in Reference Re Constitutional Question Act (B.
- Evidence: `reasoning_application` cue `apply` at chunk `5080996` offsets `180-185`; context: [79] In the present case, the transitional provisions of the Jobs, Growth and Long-term Prosperity Act provide that the provisions of the Plan repealed by that statute continue to apply to matters for which the Pension Appeals Board remains seized, that is appeals that were filed and heard before April 1, 2013; see subsection 258(1) and section 262 of the Jobs, Growth and Long-term Prosperity Act.
- Evidence: `governing_rule` cue `under` at chunk `5080997` offsets `184-189`; context: 1985 c I-21 states that where a former enactment is repealed and replaced by a new enactment, proceedings commenced under the former enactment are to be continued in conformity with the new enactment, insofar as it is possible to do so consistently with the new enactment.
- Evidence: `reasoning_application` cue `applies` at chunk `5080998` offsets `202-209`; context: That doctrine applies to questions of procedural fairness; see the decision in Baker v.

#### 23057:2:subtheme:2 · paragraphs 74-77

- Raw key terms: `effect, review, decision, error, judicial, practical, relief, allow`
- Display key terms: `effect, review, error, judicial, practical, relief, allow`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: effect, review, error, judicial, practical, relief, allow Rule/authority context: [83] Pursuant to section 18. | [84] The Supreme Court of Canada has held that prerogative relief, such as setting aside the decision under review, may be refused on the ground of futility in circumstances where issuing the relief will be of no value o Evidence spans paragraphs 74-77. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5080999` offsets `14-22`; context: [82] The next question for consideration is what is the effect of the Member’s error in choosing the test.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5081000` offsets `5-16`; context: [83] Pursuant to section 18.
- Evidence: `governing_rule` cue `under` at chunk `5081001` offsets `102-107`; context: [84] The Supreme Court of Canada has held that prerogative relief, such as setting aside the decision under review, may be refused on the ground of futility in circumstances where issuing the relief will be of no value or have no practical effect; see the decisions in Friends of the Oldman River Society v.

#### 23057:2:subtheme:3 · paragraphs 78-78

- Raw key terms: `already, another, appeal, applicant, application, applies, assessment, attempt`
- Display key terms: `already, another, applies, assessment, attempt`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: already, another, applies, assessment, attempt Application context: [86] If the matter is sent back and a different member applies the correct test, the application for leave to appeal will fail because a final decision has already been made on the issue whether she is disabled within th Evidence spans paragraphs 78-78. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5081003` offsets `181-186`; context: [86] If the matter is sent back and a different member applies the correct test, the application for leave to appeal will fail because a final decision has already been made on the issue whether she is disabled within the meaning of paragraph 42(2)(a) of the Plan.
- Evidence: `reasoning_application` cue `applies` at chunk `5081003` offsets `55-62`; context: [86] If the matter is sent back and a different member applies the correct test, the application for leave to appeal will fail because a final decision has already been made on the issue whether she is disabled within the meaning of paragraph 42(2)(a) of the Plan.

#### Section text

[77] It is unclear as to what the Member means by the words “legitimate expectations” at the time the Applicant filed the application for leave to appeal. The doctrine of legitimate expectations is an aspect of procedural fairness and is limited to the rules of procedural fairness. In this regard, I refer to the decision in Reference Re Constitutional Question Act (B.C.) (1991), 127 N.R. 161 (S.C.C.) at paragraphs 56 and 57 as follows:
56. The doctrine of legitimate expectations was discussed in the reasons of the majority in Old St. Boniface Residents Assn. Inc. v. Winnipeg (City), [1990] 3 S.C.R. 1170, 116 N.R. 46, 69 Man. R. (2d) 134. That judgment cites seven cases dealing with the doctrine, and then goes on:
The principle developed in these cases is simply an extension of the rules of natural justice and procedural fairness. It afford a party affected by the decision of a public official an opportunity to make representations in circumstances in which there otherwise would be no such opportunity. The court supplies the omission where, based on the conduct of the public official, a party has been led to believe that his or her rights would not be affected without consultation. (At p. 1204 S.C.R.):
…
57. There is no support in Canadian or English cases for the position that the doctrine of legitimate expectations can create substantive rights. It is a part of the rules of procedural fairness which can govern administrative bodies. Where it is applicable, it can create a right to make representations or to be consulted. It does not fetter the decision following the representation or consultation.

[78] The Supreme Court of Canada has held that no one has a vested right to continuance of the law as it stood in the past; see the decision in Gustavson Drilling (1964) Ltd. v. Minister of National Revenue, [1977] 1 S.C.R. 271 at 282.

[79] In the present case, the transitional provisions of the Jobs, Growth and Long-term Prosperity Act provide that the provisions of the Plan repealed by that statute continue to apply to matters for which the Pension Appeals Board remains seized, that is appeals that were filed and heard before April 1, 2013; see subsection 258(1) and section 262 of the Jobs, Growth and Long-term Prosperity Act. These provisions make it clear that Parliament intended that matters dealt with by the SST would be subject to the new legislation. The Pension Appeals Board remained subject to the former legislation during the transitional period.

[80] I note that subsection 44(c) of the Interpretation Act, R.S.C. 1985 c I-21 states that where a former enactment is repealed and replaced by a new enactment, proceedings commenced under the former enactment are to be continued in conformity with the new enactment, insofar as it is possible to do so consistently with the new enactment.

[81] In my opinion, the Member erred in assessing the Applicant’s leave application in accordance with the doctrine of legitimate expectations at the time the leave application was filed. That doctrine applies to questions of procedural fairness; see the decision in Baker v. Canada (Minister of Citizenship and Immigration), [1999] 2 S.C.R. 817 at paragraph 26. It does not apply to an expectation that the law would remain unchanged.

[82] The next question for consideration is what is the effect of the Member’s error in choosing the test. In other words, is that error a sufficient basis to allow this application for judicial review?

[83] Pursuant to section 18.1(3) of the Federal Courts Act, relief in applications for judicial review is discretionary; see the decision in Khosa, supra at paragraph 40. “Discretionary” in this context means that not every error of law will result in a remedy to an applicant.

[84] The Supreme Court of Canada has held that prerogative relief, such as setting aside the decision under review, may be refused on the ground of futility in circumstances where issuing the relief will be of no value or have no practical effect; see the decisions in Friends of the Oldman River Society v. Canada (Minister of Transport), [1992] 1 S.C.R. 3 at 80 and Lavoie v. Canada (Minister of the Environment) (2002), 291 N.R. 282 (F.C.A.) at paragraphs 18-19.

[85] In my opinion, sending this matter back to the SST for re-determination will have no practical effect.

[86] If the matter is sent back and a different member applies the correct test, the application for leave to appeal will fail because a final decision has already been made on the issue whether she is disabled within the meaning of paragraph 42(2)(a) of the Plan. A new assessment of her application for leave to appeal will also fail for another reason, that is the Applicant’s attempt to introduce “new facts” to challenge the finding that she is not disabled.

## 23057:3 · paragraphs 79-103

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a097fe0c5fb0fddde1e49b88b74daae87e765acce2d8387d7f25f33e8cda913b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23057:3:subtheme:1 · paragraphs 79-82

- Raw key terms: `judicata, danyluk, decided, decision, estoppel, rule, abuses, actions`
- Display key terms: `judicata, danyluk, decided, estoppel, rule, abuses, actions`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: judicata, danyluk, decided, estoppel, rule, abuses, actions Application context: When res judicata applies, a litigant is “estopped” by the previous proceeding. | [90] There is a public policy element to res judicata because it is intended to advance the interests of justice and prevent abuses of the decision making process. Evidence spans paragraphs 79-82. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5081004` offsets `16-22`; context: [87] Both these issues, that is the finding of no disability within the meaning of the Plan and the finding that there are no new facts, have already been finally decided and are subject to the evidentiary rule res judicata and the law of estoppel.
- Evidence: `evidence_fact` cue `evidence` at chunk `5081006` offsets `31-39`; context: [89] Res judicata is a rule of evidence and a part of the law of estoppel.
- Evidence: `reasoning_application` cue `applies` at chunk `5081006` offsets `400-407`; context: When res judicata applies, a litigant is “estopped” by the previous proceeding.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5081006` offsets `261-267`; context: Res judicata stands for the concept that once a dispute has been decided with finality, it cannot be re-litigated; see the decision in Danyluk v.
- Evidence: `reasoning_application` cue `because` at chunk `5081007` offsets `54-61`; context: [90] There is a public policy element to res judicata because it is intended to advance the interests of justice and prevent abuses of the decision making process.

#### 23057:3:subtheme:2 · paragraphs 83-84

- Raw key terms: `decision, estoppel, issue, action, applies, canada, cannot, cause`
- Display key terms: `estoppel, action, applies, cannot`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: estoppel, action, applies, cannot Position/evidence statements: [92] In the present proceedings, the Respondent submits that issue estoppel applies. Application context: [92] In the present proceedings, the Respondent submits that issue estoppel applies. Evidence spans paragraphs 83-84. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5081008` offsets `73-78`; context: [91] In Canada, res judicata has two forms: cause of action estoppel and issue estoppel; see the decision in Toronto (City) v.
- Evidence: `issue` cue `issue` at chunk `5081009` offsets `61-66`; context: [92] In the present proceedings, the Respondent submits that issue estoppel applies.
- Evidence: `party_position` cue `submits` at chunk `5081009` offsets `48-55`; context: [92] In the present proceedings, the Respondent submits that issue estoppel applies.
- Evidence: `reasoning_application` cue `applies` at chunk `5081009` offsets `76-83`; context: [92] In the present proceedings, the Respondent submits that issue estoppel applies.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5081009` offsets `257-263`; context: Issue estoppel stands for the proposition that once a question of fact or law has been litigated and determined by a competent decision maker, the decision is final and it cannot be re-determined in subsequent proceedings; see the decision in Danyluk, supra at paragraphs 24-25.

#### 23057:3:subtheme:3 · paragraphs 85-86

- Raw key terms: `decided, issue, paragraph, proceeding, allow, applicant, canada, court`
- Display key terms: `decided, paragraph, proceeding, allow`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: decided, paragraph, proceeding, allow Rule/authority context: “Disability” for that purpose means that a person falls within the definition of “disability” pursuant to paragraph 42(2)(a) of the Plan. Evidence spans paragraphs 85-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5081010` offsets `94-99`; context: [93] In Danyluk, supra at paragraph 25, the Supreme Court of Canada held that the elements of issue estoppel are as follows:
1.
- Evidence: `issue` cue `issues` at chunk `5081011` offsets `36-42`; context: [94] In the present proceeding, two issues have been finally decided.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5081011` offsets `293-304`; context: “Disability” for that purpose means that a person falls within the definition of “disability” pursuant to paragraph 42(2)(a) of the Plan.

#### 23057:3:subtheme:4 · paragraphs 87-90

- Raw key terms: `applicant, disability, facts, issue, material, medical, plan, reports`
- Display key terms: `disability, facts, material, medical, plan, reports`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: disability, facts, material, medical, plan, reports Rule/authority context: [97] The Applicant is claiming disability benefits under the Plan. Evidence spans paragraphs 87-90. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5081012` offsets `16-21`; context: [95] The second issue that has been finally decided is that the medical reports presented by the Applicant do not constitute new material facts.
- Evidence: `issue` cue `issue` at chunk `5081013` offsets `60-65`; context: [96] Applying the rule of res judicata and the principle of issue estoppel, neither the question of the Applicant’s “disability” nor the status of the medical reports as “new material facts” can be re-litigated.
- Evidence: `governing_rule` cue `under` at chunk `5081014` offsets `51-56`; context: [97] The Applicant is claiming disability benefits under the Plan.

#### 23057:3:subtheme:5 · paragraphs 91-96

- Raw key terms: `disability, applicant, benefits, plan, claim, decision, first, appeal`
- Display key terms: `disability, benefits, plan, first`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: disability, benefits, plan, first Rule/authority context: Under the Plan, “disability” is determined by a Disability Adjudicator for the Plan. | [100] Under the statutory test for disability, the question is not whether an applicant has health problems, but rather, whether an applicant has a disability that is both severe and prolonged, so as to render the claima Application context: In that decision, it was found that the Applicant was not disabled within the meaning of the Plan because the Applicant was deemed able to perform some form of light work on a regular basis. Operative outcome context: That decision was upheld on reconsideration on September 10, 1997. | This finding was ultimately upheld on appeal to the Federal Court of Appeal. Evidence spans paragraphs 91-96. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5081016` offsets `5-12`; context: [99] Whether or not a person is eligible for CPP Disability Benefits depends on whether the individual meets the definition of disability set out in paragraph 42(2)(a) of the Plan.
- Evidence: `governing_rule` cue `Under` at chunk `5081016` offsets `218-223`; context: Under the Plan, “disability” is determined by a Disability Adjudicator for the Plan.
- Evidence: `issue` cue `question` at chunk `5081017` offsets `51-59`; context: [100] Under the statutory test for disability, the question is not whether an applicant has health problems, but rather, whether an applicant has a disability that is both severe and prolonged, so as to render the claimant disabled within the meaning of the Plan.
- Evidence: `governing_rule` cue `Under` at chunk `5081017` offsets `6-11`; context: [100] Under the statutory test for disability, the question is not whether an applicant has health problems, but rather, whether an applicant has a disability that is both severe and prolonged, so as to render the claimant disabled within the meaning of the Plan.
- Evidence: `evidence_fact` cue `determined that` at chunk `5081018` offsets `245-260`; context: A disability will only be considered prolonged if it is determined that it is to be long continued and of indefinite duration, or likely to result in death; see subparagraph 42(2)(a)(ii) of the Plan.
- Evidence: `evidence_fact` cue `found that` at chunk `5081019` offsets `113-123`; context: In that decision, it was found that the Applicant was not disabled within the meaning of the Plan because the Applicant was deemed able to perform some form of light work on a regular basis.
- Evidence: `reasoning_application` cue `because` at chunk `5081019` offsets `186-193`; context: In that decision, it was found that the Applicant was not disabled within the meaning of the Plan because the Applicant was deemed able to perform some form of light work on a regular basis.
- Evidence: `disposition` cue `upheld` at chunk `5081019` offsets `297-303`; context: That decision was upheld on reconsideration on September 10, 1997.
- Evidence: `disposition` cue `upheld` at chunk `5081020` offsets `348-354`; context: This finding was ultimately upheld on appeal to the Federal Court of Appeal.

#### 23057:3:subtheme:6 · paragraphs 97-98

- Raw key terms: `applicant, decided, appealed, appeals, available, benefits, board, claim`
- Display key terms: `decided, appealed, appeals, available, benefits`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position Display terms: decided, appealed, appeals, available, benefits Position/evidence statements: [106] Similarly, the status of the medical reports presented by the Applicant, as constituting new facts, has also been finally decided in the proceedings related to her second claim. Rule/authority context: That first decision, having been reviewed and appealed through all the processes available under the Plan, was final. Evidence spans paragraphs 97-98. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5081022` offsets `19-27`; context: [105] As such, the question of whether the Applicant is disabled within the meaning of the Plan has been decided.
- Evidence: `governing_rule` cue `under` at chunk `5081022` offsets `205-210`; context: That first decision, having been reviewed and appealed through all the processes available under the Plan, was final.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5081022` offsets `323-338`; context: The claims for benefits were all made pursuant to the Plan, and involved the same parties, notwithstanding the fact that the Pension Appeals Board’s role is now fulfilled by the SST.
- Evidence: `party_position` cue `claim` at chunk `5081023` offsets `177-182`; context: [106] Similarly, the status of the medical reports presented by the Applicant, as constituting new facts, has also been finally decided in the proceedings related to her second claim.

#### 23057:3:subtheme:7 · paragraphs 99-103

- Raw key terms: `applicant, federal, appeal, application, benefits, claim, costs, court`
- Display key terms: `federal, benefits, costs`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: federal, benefits, costs Rule/authority context: [109] In the exercise of my discretion pursuant to subsection 18. | [111] Pursuant to Rule 400 of the Federal Courts Rules, SOR/98-106 the Court enjoys full discretion over costs. Application context: [107] In my opinion, the doctrine of issue estoppel applies, and the matter is res judicata. Operative outcome context: 1(3) of the Federal Courts Act, I decline to grant a remedy for the Member’s error of law and this application for judicial review is dismissed. Evidence spans paragraphs 99-103. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5081024` offsets `37-42`; context: [107] In my opinion, the doctrine of issue estoppel applies, and the matter is res judicata.
- Evidence: `reasoning_application` cue `applies` at chunk `5081024` offsets `52-59`; context: [107] In my opinion, the doctrine of issue estoppel applies, and the matter is res judicata.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5081026` offsets `39-50`; context: [109] In the exercise of my discretion pursuant to subsection 18.
- Evidence: `disposition` cue `dismissed` at chunk `5081026` offsets `199-208`; context: 1(3) of the Federal Courts Act, I decline to grant a remedy for the Member’s error of law and this application for judicial review is dismissed.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5081028` offsets `6-17`; context: [111] Pursuant to Rule 400 of the Federal Courts Rules, SOR/98-106 the Court enjoys full discretion over costs.

#### Section text

[87] Both these issues, that is the finding of no disability within the meaning of the Plan and the finding that there are no new facts, have already been finally decided and are subject to the evidentiary rule res judicata and the law of estoppel.

[88] The application of the legal principle of res judicata means that the Applicant has no ground of appeal that would have a reasonable chance of success and that standard is the relevant standard that she must meet.

[89] Res judicata is a rule of evidence and a part of the law of estoppel. Generally speaking, the law of estoppel prevents parties from proceeding with certain actions. Res judicata stands for the concept that once a dispute has been decided with finality, it cannot be re-litigated; see the decision in Danyluk v. Ainsworth Technologies Inc., [2001] 2 S.C.R. 460 at paragraph 20. When res judicata applies, a litigant is “estopped” by the previous proceeding.

[90] There is a public policy element to res judicata because it is intended to advance the interests of justice and prevent abuses of the decision making process. It aims to avoid duplicative litigation, possible inconsistent results, undue cost, and vexing litigants multiple times with the same cause; see the decision in Danyluk, supra at paragraphs 18-20.

[91] In Canada, res judicata has two forms: cause of action estoppel and issue estoppel; see the decision in Toronto (City) v. C.U.P.E., Local 79 [2003] 3 S.C.R. 77 at paragraph 23.

[92] In the present proceedings, the Respondent submits that issue estoppel applies. Issue estoppel stands for the proposition that once a question of fact or law has been litigated and determined by a competent decision maker, the decision is final and it cannot be re-determined in subsequent proceedings; see the decision in Danyluk, supra at paragraphs 24-25.

[93] In Danyluk, supra at paragraph 25, the Supreme Court of Canada held that the elements of issue estoppel are as follows:
1. The same question has been decided;
2. The judicial decision was final; and
3. The parties to the previous decision are the same parties to the proceeding in which issue estoppel is raised.

[94] In the present proceeding, two issues have been finally decided. The first issue that has been finally decided is the status of the Applicant as not being disabled for the purposes of the Plan. “Disability” for that purpose means that a person falls within the definition of “disability” pursuant to paragraph 42(2)(a) of the Plan. The Plan does not allow a person to self-assess as “disabled.”

[95] The second issue that has been finally decided is that the medical reports presented by the Applicant do not constitute new material facts.

[96] Applying the rule of res judicata and the principle of issue estoppel, neither the question of the Applicant’s “disability” nor the status of the medical reports as “new material facts” can be re-litigated.

[97] The Applicant is claiming disability benefits under the Plan. I note that the Plan is a statutory scheme that allows for the payment of benefits in defined situations as set out in the legislation.

[98] As discussed in Granovsky v. Canada (Minister of Employment and Immigration), [2000] 1 S.C.R. 703, the Plan is not a social welfare scheme, but a program to provide social insurance to eligible Canadians who lose earnings due to disability, among other things.

[99] Whether or not a person is eligible for CPP Disability Benefits depends on whether the individual meets the definition of disability set out in paragraph 42(2)(a) of the Plan. It is not a self-assessment process. Under the Plan, “disability” is determined by a Disability Adjudicator for the Plan. The decision to grant a disability benefit requires compliance with the statutory terms.

[100] Under the statutory test for disability, the question is not whether an applicant has health problems, but rather, whether an applicant has a disability that is both severe and prolonged, so as to render the claimant disabled within the meaning of the Plan.

[101] A disability will only be considered severe if it renders the claimant incapable of regularly pursuing any substantially gainful employment; see subparagraph 42(2)(a)(i) of the Plan. A disability will only be considered prolonged if it is determined that it is to be long continued and of indefinite duration, or likely to result in death; see subparagraph 42(2)(a)(ii) of the Plan. Both of these elements must be satisfied to be eligible for CPP Disability Benefits.

[102] The initial decision denying the Applicant’s claim was made on December 10, 1995. In that decision, it was found that the Applicant was not disabled within the meaning of the Plan because the Applicant was deemed able to perform some form of light work on a regular basis. That decision was upheld on reconsideration on September 10, 1997. It was reviewed and upheld by the first review tribunal on February 25, 1999 and the Applicant’s application for leave to appeal was refused on October 29, 1999. At that point, the decision that the Applicant was not disabled within the meaning of the Plan became final.

[103] The Applicant’s second claim for CPP Disability Benefits was made on May 20, 2003. This claim involved an application to re-open the decision of the first review tribunal on the basis of new facts, as set out in certain medical reports. The review tribunal concluded that the reports did not constitute new facts. This finding was ultimately upheld on appeal to the Federal Court of Appeal. At that point in the proceedings, a final decision was made that there were no new facts.

[104] The present proceedings arise out of the Applicant’s third claim for CPP Disability Benefits. The claim is in respect of the same injuries, arising from the same accident, that were assessed in her first claim. Her MQP has not changed from December 31, 1996.

[105] As such, the question of whether the Applicant is disabled within the meaning of the Plan has been decided. That first decision, having been reviewed and appealed through all the processes available under the Plan, was final. The claims for benefits were all made pursuant to the Plan, and involved the same parties, notwithstanding the fact that the Pension Appeals Board’s role is now fulfilled by the SST.

[106] Similarly, the status of the medical reports presented by the Applicant, as constituting new facts, has also been finally decided in the proceedings related to her second claim.

[107] In my opinion, the doctrine of issue estoppel applies, and the matter is res judicata. The Applicant was found not to be disabled within the meaning of paragraph 42(2)(a) of the Plan. The additional reports presented by her were found not to raise new facts in the proceedings arising from her second claim for CPP Disability Benefits.

[108] Further, the changes to the legislative scheme mean that adducing new facts is no longer a ground of appeal. The Applicant does not have a ground of appeal with a reasonable chance of success, and sending the matter back to the SST for re-determination will make no difference to the outcome of the application for leave to appeal.

[109] In the exercise of my discretion pursuant to subsection 18.1(3) of the Federal Courts Act, I decline to grant a remedy for the Member’s error of law and this application for judicial review is dismissed.

[110] The Respondent seeks costs on the basis that that the Applicant has pursued her claim for CPP Disability Benefits through several proceedings up to and including the Federal Court of Appeal.

[111] Pursuant to Rule 400 of the Federal Courts Rules, SOR/98-106 the Court enjoys full discretion over costs. I am not persuaded that costs against the Applicant are justified in this case and make no Order as to costs.


## 23057:4 · paragraphs 104-105

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2c6081ebd2f817c7a37e0c797d1556d57f3b73ecc41497fb3dbcb5677c4b459e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23057:4:subtheme:1 · paragraphs 104-105

- Raw key terms: `application, attorney, belo-alves, canada, cause, costs, court, courts`
- Display key terms: `belo-alves, costs, courts`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: belo-alves, costs, courts Rule/authority context: In the exercise of my discretion pursuant to the Federal Courts Rules SOR/98-106, I make no order as to costs. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is dismissed. Evidence spans paragraphs 104-105. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5081028` offsets `344-355`; context: In the exercise of my discretion pursuant to the Federal Courts Rules SOR/98-106, I make no order as to costs.
- Evidence: `disposition` cue `dismissed` at chunk `5081028` offsets `300-309`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed. In the exercise of my discretion pursuant to the Federal Courts Rules SOR/98-106, I make no order as to costs.
“E. Heneghan”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1823-13
STYLE OF CAUSE:
GUIDA BELO-ALVES v THE ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Ottawa, Ontario
DATE OF HEARING:
may 22, 2014


## 23057:5 · paragraphs 106-106

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `47bb81b0ebc8c54ab630db5bc196e8749703f3e5161377f3922e1df0512827c5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23057:5:subtheme:1 · paragraphs 106-106

- Raw key terms: `appearances, applicant, attorney, behalf, belo-alves, canada, dated, deputy`
- Display key terms: `behalf, belo-alves, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, belo-alves, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 106-106. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
hENEGHAN J.
DATED:
nOVEMBER 21, 2014
APPEARANCES:
Guida Belo-Alves
For The Applicant
(on her own behalf)
Sara Jane Harvey
For The Respondent
SOLICITORS OF RECORD:
Guida Belo-Alves
Etobicoke, ON
For The Applicant
(ON HER OWN BEHALF)
William F. Pentney
Deputy Attorney General of Canada
Ottawa, Ontario
For The Respondent
