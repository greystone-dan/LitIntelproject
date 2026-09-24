# Discussion Units: case 13837

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **21**
- Continuity pairs: **20**
- Discussion Units: **3**
- Paragraph source hashes: **21**
- Sub-themes: **8**

## 13837:1 · paragraphs 0-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dec876990f80c3ffdcd3e44193a6ae9479afef9ec84f5a653e13e193656c445b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13837:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, today, database, hours, manager, mehfooz, officer, sales`
- Display key terms: `today, database, hours, manager, mehfooz, officer, sales`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: today, database, hours, manager, mehfooz, officer, sales Position/evidence statements: He claimed that his work at Today HR qualified him as a Corporate Sales Manager, as defined by National Occupancy Classification Code 0601 [NOC 0601]. | [5] On December 16, 2014, the Officer sent the Applicant a procedural fairness letter [PF letter] which expressed “serious concerns” about the application, stating she had grounds to believe he had not acquired the requi Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of a Citizenship and Immigration Canada [CIC] Case Officer [O Application context: Mehfooz applied for permanent residence as a member of the CEC. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4680633` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of a Citizenship and Immigration Canada [CIC] Case Officer [Officer] dated February 9, 2015, refusing to grant the Applicant permanent residence as a member of Canadian Experience Class [CEC].
- Evidence: `party_position` cue `claimed` at chunk `4680634` offsets `93-100`; context: He claimed that his work at Today HR qualified him as a Corporate Sales Manager, as defined by National Occupancy Classification Code 0601 [NOC 0601].
- Evidence: `reasoning_application` cue `applied` at chunk `4680634` offsets `34-41`; context: Mehfooz applied for permanent residence as a member of the CEC.
- Evidence: `party_position` cue `claimed` at chunk `4680636` offsets `340-347`; context: [5] On December 16, 2014, the Officer sent the Applicant a procedural fairness letter [PF letter] which expressed “serious concerns” about the application, stating she had grounds to believe he had not acquired the requisite experience, and in particular, that he had not actually performed the duties of an Account Manager Sales as he had claimed.

#### 13837:1:subtheme:2 · paragraphs 5-6

- Raw key terms: `canada, court, decision, dunsmuir, judicial, make, para, reasonable`
- Display key terms: `dunsmuir, judicial, make, para, reasonable`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: dunsmuir, judicial, make, para, reasonable Position/evidence statements: Decision under Review [7] The Officer rejected the application for permanent residence on the basis that she was not satisfied that the Applicant had “performed the duties of Account manager sales, NOC 0601 for the emplo Rule/authority context: Decision under Review [7] The Officer rejected the application for permanent residence on the basis that she was not satisfied that the Applicant had “performed the duties of Account manager sales, NOC 0601 for the emplo | [10] In Dunsmuir at para 47, the Supreme Court of Canada explained what is required of a court reviewing on the reasonableness standard of review: A court conducting a review for reasonableness inquires into the qualitie Application context: Leave to apply for judicial review of that decision was granted on October 30, 2015. Operative outcome context: Leave to apply for judicial review of that decision was granted on October 30, 2015. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4680637` offsets `1065-1070`; context: ” Second, the Officer took issue with the organizational chart provided for Today HR.
- Evidence: `party_position` cue `claimed` at chunk `4680637` offsets `552-559`; context: Decision under Review [7] The Officer rejected the application for permanent residence on the basis that she was not satisfied that the Applicant had “performed the duties of Account manager sales, NOC 0601 for the employer Today Employment &HR ltd as claimed in [his] application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4680637` offsets `1750-1758`; context: Discussion and Analysis [8] In my respectful view, the application should be dismissed for the following reasons:
The Officer did not violate procedural fairness because she put her credibility concerns to the Applicant in the PF letter; The Officer did not rely on extrinsic evidence because her internet searches yielded no information and she did not rely on the absence of evidence to make her decision; The Officer’s decision to refuse the application was reasonable; it was intelligible and based on the evidence.
- Evidence: `governing_rule` cue `under` at chunk `4680637` offsets `309-314`; context: Decision under Review [7] The Officer rejected the application for permanent residence on the basis that she was not satisfied that the Applicant had “performed the duties of Account manager sales, NOC 0601 for the employer Today Employment &HR ltd as claimed in [his] application.
- Evidence: `reasoning_application` cue `apply` at chunk `4680637` offsets `220-225`; context: Leave to apply for judicial review of that decision was granted on October 30, 2015.
- Evidence: `disposition` cue `granted` at chunk `4680637` offsets `267-274`; context: Leave to apply for judicial review of that decision was granted on October 30, 2015.
- Evidence: `issue` cue `whether` at chunk `4680638` offsets `521-528`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.
- Evidence: `governing_rule` cue `standard of review` at chunk `4680638` offsets `127-145`; context: [10] In Dunsmuir at para 47, the Supreme Court of Canada explained what is required of a court reviewing on the reasonableness standard of review:
A court conducting a review for reasonableness inquires into the qualities that make a decision reasonable, referring both to the process of articulating the reasons and to outcomes.
- Evidence: `counterargument_limitation` cue `But` at chunk `4680638` offsets `491-494`; context: But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### 13837:1:subtheme:3 · paragraphs 7-9

- Raw key terms: `applicant, experience, alleged, application, canada, citizenship, concerned, concerns`
- Display key terms: `experience, alleged, concerned, concerns`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: experience, alleged, concerned, concerns Rule/authority context: In Dunsmuir at para 50, the Supreme Court of Canada explained what is required of a court reviewing on the correctness standard of review: When applying the correctness standard, a reviewing court will not show deference Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4680639` offsets `475-483`; context: In Dunsmuir at para 50, the Supreme Court of Canada explained what is required of a court reviewing on the correctness standard of review:
When applying the correctness standard, a reviewing court will not show deference to the decision maker's reasoning process; it will rather undertake its own analysis of the question.
- Evidence: `governing_rule` cue `standard of review` at chunk `4680639` offsets `281-299`; context: In Dunsmuir at para 50, the Supreme Court of Canada explained what is required of a court reviewing on the correctness standard of review:
When applying the correctness standard, a reviewing court will not show deference to the decision maker's reasoning process; it will rather undertake its own analysis of the question.
- Evidence: `issue` cue `issue` at chunk `4680640` offsets `1276-1281`; context: No doubt to some extent, the Applicant’s credibility was in issue, but that could be said in many if not all cases where weight or sufficiency of evidence is concerned.
- Evidence: `evidence_fact` cue `evidence` at chunk `4680640` offsets `258-266`; context: Second, officers must disclose extrinsic evidence relied upon and give the applicant an opportunity to respond to concerns arising therefrom where two conditions are met: first, where the evidence is truly extrinsic, i.
- Evidence: `counterargument_limitation` cue `but` at chunk `4680640` offsets `1283-1286`; context: No doubt to some extent, the Applicant’s credibility was in issue, but that could be said in many if not all cases where weight or sufficiency of evidence is concerned.

#### 13837:1:subtheme:4 · paragraphs 10-13

- Raw key terms: `applicant, conducted, database, information, internet, officer, view, arising`
- Display key terms: `conducted, database, information, internet, officer, view, arising`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: conducted, database, information, internet, officer, view, arising Position/evidence statements: In Animodi v Canada (Minister of Citizenship and Immigration), 2015 FC 929 [Animodi], a CIC officer conducted a Google search on Angola’s country conditions to supplement what she perceived to be the meagre evidence subm Application context: Justice Russell held there was no procedural unfairness because the search yielded no “novel and significant” information (Animodi at para 85, citing Mancia v Canada (Minister of Citizenship and Immigration), [1998] 3 FC Evidence spans paragraphs 10-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4680642` offsets `416-423`; context: Two further questions that arise are: (1) whether the Officer relied on the internet and D&B database searches; and (2) whether these searches were disclosed to the Applicant such that he could respond to them.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4680642` offsets `174-182`; context: Further Reliance on Extrinsic Evidence [17] Applicants have the right to be made aware of truly extrinsic evidence relied upon by an Officer that they could not reasonably anticipate, and to respond to concerns arising therefrom.
- Evidence: `evidence_fact` cue `record` at chunk `4680643` offsets `22-28`; context: [18] According to the record, extrinsic sources were consulted by CIC at five different times:
The GCMS notes for June 6, 2014, state “Web-based search conducted – Online information verified.
- Evidence: `party_position` cue `submitted` at chunk `4680644` offsets `324-333`; context: In Animodi v Canada (Minister of Citizenship and Immigration), 2015 FC 929 [Animodi], a CIC officer conducted a Google search on Angola’s country conditions to supplement what she perceived to be the meagre evidence submitted in a PRRA application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4680644` offsets `315-323`; context: In Animodi v Canada (Minister of Citizenship and Immigration), 2015 FC 929 [Animodi], a CIC officer conducted a Google search on Angola’s country conditions to supplement what she perceived to be the meagre evidence submitted in a PRRA application.
- Evidence: `reasoning_application` cue `because` at chunk `4680644` offsets `508-515`; context: Justice Russell held there was no procedural unfairness because the search yielded no “novel and significant” information (Animodi at para 85, citing Mancia v Canada (Minister of Citizenship and Immigration), [1998] 3 FC 461, [1998] FCJ No 565 (FCA) at para 22).

#### 13837:1:subtheme:5 · paragraphs 14-16

- Raw key terms: `decision, entitled, falls, letter, officers, para, reasonable, today`
- Display key terms: `entitled, falls, letter, officers, para, reasonable, today`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: entitled, falls, letter, officers, para, reasonable, today Application context: In my view it was reasonable on this record for the Officer to conclude the Applicant submitted insufficient evidence of his job duties at Today HR. Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4680646` offsets `55-60`; context: [21] These searches do not raise a procedural fairness issue.
- Evidence: `evidence_fact` cue `record` at chunk `4680646` offsets `484-490`; context: In my view it was reasonable on this record for the Officer to conclude the Applicant submitted insufficient evidence of his job duties at Today HR.
- Evidence: `reasoning_application` cue `conclude` at chunk `4680646` offsets `510-518`; context: In my view it was reasonable on this record for the Officer to conclude the Applicant submitted insufficient evidence of his job duties at Today HR.

#### 13837:1:subtheme:6 · paragraphs 17-17

- Raw key terms: `arises, certify, neither, none, party, proposed, question`
- Display key terms: `arises, certify, neither, none, proposed, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: arises, certify, neither, none, proposed, question Evidence spans paragraphs 17-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4680649` offsets `30-38`; context: [25] Neither party proposed a question to certify, and none arises.

#### Section text

Mehfooz v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2016-02-09
Neutral citation
2016 FC 165
File numbers
IMM-888-15
Decision Content
Date: 20160209
Docket: IMM-888-15
Citation: 2016 FC 165
Ottawa, Ontario, February 9, 2016
PRESENT: The Honourable Mr. Justice Brown
BETWEEN:
ALI MEHFOOZ
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of a decision of a Citizenship and Immigration Canada [CIC] Case Officer [Officer] dated February 9, 2015, refusing to grant the Applicant permanent residence as a member of Canadian Experience Class [CEC]. I would dismiss this application for the following reasons.
I. Facts [2] The Applicant, Mr. Ali Mehfooz, and his wife are citizens of Pakistan. The Applicant obtained two Canadian university degrees, a Bachelor of Business Administration (in 2006) and a graduate certificate (in 2012). From 2012 to 2013, he held two full time jobs. His first job was working for Today Employment and HR Ltd. [Today HR] as an Account Manager Sales. The Applicant was employed there from September 2012 to October 2013, working a total of 1,952 hours. Today HR is a Brampton-based employment agency. Ms. Farkhanda Ijaz is the President of Today HR and her spouse, Mr. Ijaz Hussain, is the Chief Executive Officer. The Applicant’s second job was working for Glentel Inc., selling cellphones at a booth in a shopping mall. The Applicant worked there five days a week from November 2012 to October 2013, all day on most weekends and from 4 p.m. to 9 p.m. on most weekdays.

[3] In November 2013, Mr. Mehfooz applied for permanent residence as a member of the CEC. He claimed that his work at Today HR qualified him as a Corporate Sales Manager, as defined by National Occupancy Classification Code 0601 [NOC 0601]. On July 7, 2014, CIC sent the Applicant an email requesting additional information about Today HR and the Applicant’s working hours. The Applicant replied on July 15, 2014, and included a letter from Today HR, dated July 9, 2014, which confirmed that the firm had 308 employees and revenues of $1.2 million in 2013, and that the Applicant had worked 1,952 hours for Today HR.

[4] On July 28, 2014, CIC requested that Today HR be looked up on the Dun & Bradstreet [D&B] database. The Global Case Management System [GCMS] notes state that this search was “inconclusive”. The matter was subsequently referred for further review by the internal Anti-Fraud Unit [AF Unit], which conducted phone interviews with Glentel and with Ijaz Hussain, CEO of Today HR, concerning the Applicant’s work schedule and performed tasks, before returning the file to the Officer for review.

[5] On December 16, 2014, the Officer sent the Applicant a procedural fairness letter [PF letter] which expressed “serious concerns” about the application, stating she had grounds to believe he had not acquired the requisite experience, and in particular, that he had not actually performed the duties of an Account Manager Sales as he had claimed. Further, concerns were expressed about his period of employment, and hours of work. The PF letter outlined that internet and database searches had been conducted with regards to Today HR but that these failed to yield information regarding the nature and size of the company. Today HR had no website. The letter included a demand for a number of documents including the company’s tax and banking material, and other information such as marketing material, an organization chart listing all of its employees and positions and where the Applicant worked, how many employees there are, and an explanation of the company’s business lines.

[6] The Applicant replied on January 1, 2015. On February 6, 2015, the Officer refused the application for permanent residence. Her decision was communicated to the Applicant in a letter dated February 9, 2015. Leave to apply for judicial review of that decision was granted on October 30, 2015.
II. Decision under Review [7] The Officer rejected the application for permanent residence on the basis that she was not satisfied that the Applicant had “performed the duties of Account manager sales, NOC 0601 for the employer Today Employment &HR ltd as claimed in [his] application.” She did not find that the documents the Applicant sent on January 14, 2015, allayed concerns expressed in the PF letter. The rejection letter included two specific reasons for the refusal. First, the Officer was not satisfied by Mr. Ijaz Hussain’s explanation that Today HR had experienced website problems because its domain had expired. She believed it was “unclear … why a company with 308 employees would have a website that was temporarily suspended.” Second, the Officer took issue with the organizational chart provided for Today HR. She found it was “basic” considering Today HR’s size and noted that it did not include the position of Managing Director despite the marketing pamphlet’s identification of Mr. Ijaz Hussain as such.
III. Issues 1. Did the Officer violate procedural fairness?
2. Was the Officer’s decision to refuse the permanent residence application reasonable?
IV. Discussion and Analysis [8] In my respectful view, the application should be dismissed for the following reasons:
The Officer did not violate procedural fairness because she put her credibility concerns to the Applicant in the PF letter; The Officer did not rely on extrinsic evidence because her internet searches yielded no information and she did not rely on the absence of evidence to make her decision; The Officer’s decision to refuse the application was reasonable; it was intelligible and based on the evidence.
A. Standard of Review [9] In Dunsmuir v New Brunswick, 2008 SCC 9 at paras 57 and 62 [Dunsmuir], the Supreme Court of Canada held that a standard of review analysis is unnecessary where “the jurisprudence has already determined in a satisfactory manner the degree of deference to be accorded with regard to a particular category of question.” It is established that an Officer’s analysis of eligibility for permanent residence involves an assessment of the evidence and the exercise of discretion and is reviewable on the standard of reasonableness: Hamza v Canada (Minister of Citizenship and Immigration), 2013 FC 264 at para 14 [Hamza]; Qin v Canada (Minister of Citizenship and Immigration), 2013 FC 147 at para 16 [Qin].

[10] In Dunsmuir at para 47, the Supreme Court of Canada explained what is required of a court reviewing on the reasonableness standard of review:
A court conducting a review for reasonableness inquires into the qualities that make a decision reasonable, referring both to the process of articulating the reasons and to outcomes. In judicial review, reasonableness is concerned mostly with the existence of justification, transparency and intelligibility within the decision-making process. But it is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

[11] Questions of procedural fairness are reviewed on the correctness standard: Hamza at para 13; Sketchley v Canada (Attorney General), 2005 FCA 404 at para 53. In Dunsmuir at para 50, the Supreme Court of Canada explained what is required of a court reviewing on the correctness standard of review:
When applying the correctness standard, a reviewing court will not show deference to the decision maker's reasoning process; it will rather undertake its own analysis of the question. The analysis will bring the court to decide whether it agrees with the determination of the decision maker; if not, the court will substitute its own view and provide the correct answer. From the outset, the court must ask whether the tribunal’s decision was correct.
B. Procedural Fairness [12] The onus is on a visa applicant to establish that he or she meets the requirements in the Regulations (Hamza at para 22). An application must be complete, relevant, convincing and unambiguous (Obeta v Canada (Minister of Citizenship and Immigration), 2012 FC 1542 at para 25). It is also well-established that the duty of procedural fairness owed to visa applicants falls on the low end of the spectrum (Hamza at para 23). Thus, CIC need not give applicants a “running score” of the weaknesses of their application (Rukmangathan v Canada (Minister of Citizenship and Immigration) 2004 FC 284 at para 23); it is their duty to file a complete application. In this case it was essential for the Applicant to file material that supported his claimed experience underlying his request for acceptance into the CEC. Failure to prove experience would be fatal to this application.

[13] That said, two procedural fairness obligations are recognized. First, an officer may need to apprise an applicant of concerns regarding his or her credibility or the authenticity of documents (Hamza at para 25). Second, officers must disclose extrinsic evidence relied upon and give the applicant an opportunity to respond to concerns arising therefrom where two conditions are met: first, where the evidence is truly extrinsic, i.e. “novel and significant”, and secondly where it is information the applicant could not reasonably have anticipated: Joseph v Canada (Minister of Citizenship and Immigration), 2015 FC 904; Toma v Canada (Minister of Citizenship and Immigration), 2006 FC 780 at para 14, citing Rothstein J in Dasent v Canada (Minister of Citizenship and Immigration), [1995] 1 FC 720 (TD) that extrinsic evidence is that of which an applicant “could not reasonably be expected to have knowledge.”
C. Opportunity to Respond to Credibility Concerns [14] To succeed on this point, the Applicant must establish that the Officer had credibility concerns as opposed to weight or sufficiency of evidence concerns. In my view, the Officer’s concerns dealt with the sufficiency or weight of the evidence. No doubt to some extent, the Applicant’s credibility was in issue, but that could be said in many if not all cases where weight or sufficiency of evidence is concerned. In my view, one must look to the dominant or over-arching feature of the Officer’s concern and determine if that related to credibility, on the one hand, or whether in reality the Officer was simply concerned with the sufficiency or weight of the evidence submitted. Here, I am satisfied the Officer was concerned with the weight of the evidence and in particular whether the Applicant had acquired the experience alleged. The Applicant had outlined a list of duties in his application, a list predominantly copied from the NOC job outline on CIC’s website. When asked for more details, a further list was submitted which was in reality the same list as the first except slightly rephrased to increase the breadth of the experience allegedly obtained. Little was provided to show that he actually had that experience, as called for in the PF letter – he provided no examples of what he did, for example. In my view, the Officer reasonably concluded that the evidence was insufficient.

[15] The Officer, on the other hand, was very concerned with the experience alleged by the Applicant and made those concerns crystal clear to the Applicant in the PF letter, stating that: “[t]he onus is on you to demonstrate that you are working for an existing employer, that you are working in the capacity declared and that you are working for the period of time declared. To date I am not satisfied that you have the experience you would require to qualify in this program” [emphasis added]. I am unable to see how the Officer’s concerns with the Applicant’s experience could have been expressed more clearly.

[16] Taken as a whole, in my view the PF letter supplied ample notice of the Officer’s concerns. There was no breach of procedural fairness.
D. Further Reliance on Extrinsic Evidence [17] Applicants have the right to be made aware of truly extrinsic evidence relied upon by an Officer that they could not reasonably anticipate, and to respond to concerns arising therefrom. Two further questions that arise are: (1) whether the Officer relied on the internet and D&B database searches; and (2) whether these searches were disclosed to the Applicant such that he could respond to them.

[18] According to the record, extrinsic sources were consulted by CIC at five different times:
The GCMS notes for June 6, 2014, state “Web-based search conducted – Online information verified. (…) Website: todayemployment.com”; The GCMS notes for July 7, 2014, state “Web-search on employer reveals this to be a small size temporary employment agency and it seems inconceivable for applicant to be - i)recruiting, organizing, trainingn [sic] and managing sales support staff or ii)planning, directing and evaluating the activities of sales/marketing department”; A D&B database search was conducted on August 19, 2014, and deemed inconclusive by CIC on September 10, 2014; On October 16, 2014, CIC searched “Yellow Pages / 411” and Google Maps to verify Today HR’s contact information; The GCMS notes for December 3, 2014, state “Despite an internet and database search of “Today Employment and HR Ltd”, I note that very limited information exist for employer Today Employment & HR Ltd. (…) Furthermore, since Information obtained from open sources concerning the employer is not conclusive, I have concerns about the nature and existence of the employer and that is warrant the needs [sic] of a full time account manager sales”.

[19] In my respectful view, the Officer did not rely on the D&B database search(es) in making her decision. In Animodi v Canada (Minister of Citizenship and Immigration), 2015 FC 929 [Animodi], a CIC officer conducted a Google search on Angola’s country conditions to supplement what she perceived to be the meagre evidence submitted in a PRRA application. The officer’s affidavit explained that she found nothing online to contribute to her decision. Justice Russell held there was no procedural unfairness because the search yielded no “novel and significant” information (Animodi at para 85, citing Mancia v Canada (Minister of Citizenship and Immigration), [1998] 3 FC 461, [1998] FCJ No 565 (FCA) at para 22). Similarly, I see no procedural unfairness arising out of the inconclusive D&B search(es) here.

[20] In terms of the remaining internet searches, I am satisfied the Applicant could reasonably have anticipated that such information would be consulted by CIC. The information searched is publicly available through simple internet searches anyone with a computer may perform. I frankly see no need to send PF letters where, as here, the Officer conducted routine internet searches that the Applicant could easily have performed himself and which in my respectful view he could and should reasonably have anticipated.

[21] These searches do not raise a procedural fairness issue.
E. Was the Officer’s Decision Reasonable? [22] An officer must undertake a qualitative assessment of an applicant’s experience to determine whether he or she falls within a permissible NOC code (Qin at para 30). It is not enough that the job description submitted reproduces the NOC requirements, and in my view where they do, officers are entitled to and should proceed with caution. In my view it was reasonable on this record for the Officer to conclude the Applicant submitted insufficient evidence of his job duties at Today HR. The burden was on the Applicant to provide a clear and complete application particularly concerning his experience. He was warned in the PF letter that the Officer was not convinced by the simple list of duties he provided; yet the list of duties given in the Hussain Affidavit by way of a response was substantially the same (except that it inexplicably claimed even greater experience in some respects).

[23] It was also reasonable to expect Today HR to have a functional website and to find that its organizational structure was confusing. Officers are entitled to rely on common sense.

[24] Those conclusions are certainly justified, transparent and intelligible based on the GCMS notes and the refusal letter (Dunsmuir at para 47). In my view, the decision falls within the range of possible, acceptable outcomes which are defensible in respect of the facts and law as set out in Dunsmuir.

[25] Neither party proposed a question to certify, and none arises.


## 13837:2 · paragraphs 18-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `53d25f048374ef6e40ce6505cce454dd791650c09df3ce492f8421763d92251a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13837:2:subtheme:1 · paragraphs 18-19

- Raw key terms: `application, brown, cause, certification, certified, citizenship, conclusion, costs`
- Display key terms: `brown, certification, certified, conclusion, costs`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: brown, certification, certified, conclusion, costs Application context: Conclusion [26] Therefore this application should be dismissed, without certification of a question. Operative outcome context: Conclusion [26] Therefore this application should be dismissed, without certification of a question. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4680649` offsets `162-170`; context: Conclusion [26] Therefore this application should be dismissed, without certification of a question.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4680649` offsets `87-96`; context: Conclusion [26] Therefore this application should be dismissed, without certification of a question.
- Evidence: `disposition` cue `dismissed` at chunk `4680649` offsets `124-133`; context: Conclusion [26] Therefore this application should be dismissed, without certification of a question.

#### Section text

V. Conclusion [26] Therefore this application should be dismissed, without certification of a question.
JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed, no question is certified, and there is no order as to costs.
“Henry S. Brown”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-888-15
STYLE OF CAUSE:
ALI MEHFOOZ v
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
January 28, 2016


## 13837:3 · paragraphs 20-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5d3317941739fae9a454e22446ed4f40786721a0eb55619308a1236be3226e11`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13837:3:subtheme:1 · paragraphs 20-20

- Raw key terms: `appearances, applicant, attorney, barrister, brown, canada, dated, deputy`
- Display key terms: `barrister, brown, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, brown, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
BROWN J.
DATED:
FEBRUARY 9, 2016
APPEARANCES:
Raisa Sharipova
For The Applicant
Lucan Gregory
For The Respondent
SOLICITORS OF RECORD:
Raisa Sharipova
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
