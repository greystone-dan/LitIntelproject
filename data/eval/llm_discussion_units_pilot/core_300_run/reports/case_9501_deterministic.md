# Discussion Units: case 9501

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **27**
- Continuity pairs: **26**
- Discussion Units: **4**
- Paragraph source hashes: **27**
- Sub-themes: **9**

## 9501:1 · paragraphs 0-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2cece3b89e80cb4d4482d11207dc7cbc6d6058492ba5c083adcb0cd285676b75`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9501:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `glover, sst-gd, decision, disability, severe, date, denied, prolonged`
- Display key terms: `glover, sst-gd, disability, severe, date, denied, prolonged`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: glover, sst-gd, disability, severe, date, denied, prolonged Rule/authority context: Glover, the applicant, applied for a disability pension under the Canada Pension Plan, RSC 1985, c C-8 [CPP]. | However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April, 2013. Application context: Glover, the applicant, applied for a disability pension under the Canada Pension Plan, RSC 1985, c C-8 [CPP]. | In this case I am unable to conclude that the SST-AD decision to deny leave to appeal the negative SST-GD decision was unreasonable or that the process was procedurally unfair. Operative outcome context: His application was denied and the denial was upheld on reconsideration. | Leave was denied. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4480614` offsets `706-716`; context: The SST-GD found that Mr.
- Evidence: `governing_rule` cue `under` at chunk `4480614` offsets `467-472`; context: Glover, the applicant, applied for a disability pension under the Canada Pension Plan, RSC 1985, c C-8 [CPP].
- Evidence: `reasoning_application` cue `applied` at chunk `4480614` offsets `434-441`; context: Glover, the applicant, applied for a disability pension under the Canada Pension Plan, RSC 1985, c C-8 [CPP].
- Evidence: `disposition` cue `denied` at chunk `4480614` offsets `541-547`; context: His application was denied and the denial was upheld on reconsideration.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480615` offsets `266-274`; context: Glover submits that the SST-AD erred in failing to consider new evidence that demonstrated he suffered from a severe and prolonged disability.
- Evidence: `disposition` cue `denied` at chunk `4480615` offsets `120-126`; context: Leave was denied.
- Evidence: `reasoning_application` cue `conclude` at chunk `4480616` offsets `295-303`; context: In this case I am unable to conclude that the SST-AD decision to deny leave to appeal the negative SST-GD decision was unreasonable or that the process was procedurally unfair.
- Evidence: `disposition` cue `denied` at chunk `4480616` offsets `483-489`; context: The application for judicial review is denied for the reasons that follow.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4480618` offsets `124-135`; context: However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April, 2013.
- Evidence: `counterargument_limitation` cue `However` at chunk `4480618` offsets `115-122`; context: However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April, 2013.

#### 9501:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `business, concluded, considered, criterion, decision, disability, evidence, glover`
- Display key terms: `business, concluded, considered, criterion, disability, glover`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: business, concluded, considered, criterion, disability, glover Position/evidence statements: Glover’s counsel submitted that the SST-GD had erred by drawing an incorrect conclusion from the evidence and had based its decision on an erroneous finding of fact. Rule/authority context: It noted that pursuant to subsection 58(3) of the DESDA that it must either grant or refuse leave to appeal, and that leave is to be refused if the SST-AD is satisfied the appeal has no reasonable chance of success (subs Application context: The SST-GD found his work as an estimator only ceased because he was not contacted for further work. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4480620` offsets `118-125`; context: [9] After reviewing the evidence including the medical reports placed before it, the SST-GD, undertook an analysis of whether Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480620` offsets `24-32`; context: [9] After reviewing the evidence including the medical reports placed before it, the SST-GD, undertook an analysis of whether Mr.
- Evidence: `issue` cue `question` at chunk `4480621` offsets `124-132`; context: It did not question that Mr.
- Evidence: `party_position` cue `submitted` at chunk `4480621` offsets `833-842`; context: Glover’s counsel submitted that the SST-GD had erred by drawing an incorrect conclusion from the evidence and had based its decision on an erroneous finding of fact.
- Evidence: `evidence_fact` cue `found that` at chunk `4480621` offsets `214-224`; context: Glover had sustained injuries following his motor vehicle accident, but found that he had continued to work in his business in a modified role until 2011 and as an estimator for several months in 2012.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4480621` offsets `996-1007`; context: It noted that pursuant to subsection 58(3) of the DESDA that it must either grant or refuse leave to appeal, and that leave is to be refused if the SST-AD is satisfied the appeal has no reasonable chance of success (subsection 58(2)).
- Evidence: `reasoning_application` cue `because` at chunk `4480621` offsets `398-405`; context: The SST-GD found his work as an estimator only ceased because he was not contacted for further work.

#### 9501:1:subtheme:3 · paragraphs 8-11

- Raw key terms: `evidence, sst-ad, appeal, canada, condition, counsel, decision, glover`
- Display key terms: `sst-ad, condition, glover`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: sst-ad, condition, glover Rule/authority context: Standard of Review [15] The parties agree and the jurisprudence establishes that a decision of the SST-AD denying leave to appeal is to be reviewed against a reasonableness standard (Canada (Attorney General) v Hines, 20 | [16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minis Application context: [16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minis Operative outcome context: Glover’s counsel argued in oral submissions that the SST-GD was seeking and should have allowed Mr. Evidence spans paragraphs 8-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4480622` offsets `632-638`; context: Issues [14] The applicant raises the following issues:
A.
- Evidence: `evidence_fact` cue `found that` at chunk `4480622` offsets `114-124`; context: However it found that the SST-GD had considered Mr.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4480622` offsets `958-976`; context: Standard of Review [15] The parties agree and the jurisprudence establishes that a decision of the SST-AD denying leave to appeal is to be reviewed against a reasonableness standard (Canada (Attorney General) v Hines, 2016 FC 112 at para 28, citing Tracey v Canada (Attorney General), 2015 FC 1300 at para 17 [Tracey]).
- Evidence: `counterargument_limitation` cue `However` at chunk `4480622` offsets `103-110`; context: However it found that the SST-GD had considered Mr.
- Evidence: `issue` cue `whether` at chunk `4480623` offsets `22-29`; context: [16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at para 27).
- Evidence: `evidence_fact` cue `Evidence` at chunk `4480623` offsets `319-327`; context: Consideration of the Evidence [17] Mr.
- Evidence: `governing_rule` cue `standard of review` at chunk `4480623` offsets `170-188`; context: [16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at para 27).
- Evidence: `reasoning_application` cue `applies` at chunk `4480623` offsets `189-196`; context: [16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at para 27).
- Evidence: `disposition` cue `allowed` at chunk `4480623` offsets `539-546`; context: Glover’s counsel argued in oral submissions that the SST-GD was seeking and should have allowed Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480624` offsets `879-887`; context: The implication being that the SST-AD was satisfied that the SST-GD had not indicated additional evidence was preferred but rather considered the evidence placed before it.
- Evidence: `counterargument_limitation` cue `but` at chunk `4480624` offsets `902-905`; context: The implication being that the SST-AD was satisfied that the SST-GD had not indicated additional evidence was preferred but rather considered the evidence placed before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480625` offsets `46-54`; context: [19] With respect to the attempt to place new evidence before the SST-AD as part of the application for leave, this was addressed by Justice Michael Manson in Canada (Attorney General) v O’Keefe, 2016 FC 503 at paragraph 28 [O’Keefe], where he states:

#### 9501:1:subtheme:4 · paragraphs 12-14

- Raw key terms: `application, evidence, leave, sst-ad, appeal, decision, desda, section`
- Display key terms: `leave, sst-ad, desda, section`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: leave, sst-ad, desda, section Rule/authority context: [28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory. Operative outcome context: Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal. Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4480626` offsets `645-651`; context: Further, the SST-AD’s leave decision demarcates the issues on appeal that have a reasonable chance of success (Belo-Alves v Canada (Attorney General), 2014 FC 1100 at paras 71-73).
- Evidence: `evidence_fact` cue `evidence` at chunk `4480626` offsets `407-415`; context: Unlike an appeal before the former PAB, which was de novo, an appeal to the SST-AD does not allow for new evidence and is limited to the three grounds of appeal listed in section 58.
- Evidence: `governing_rule` cue `under` at chunk `4480626` offsets `127-132`; context: [28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory.
- Evidence: `disposition` cue `granted` at chunk `4480626` offsets `528-535`; context: Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480627` offsets `195-203`; context: In doing so I note that the DESDA does make provision, at section 66, for the SST-GD to rescind or amend a decision where new evidence is presented by way of application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480628` offsets `76-84`; context: [21] I am satisfied that the SST-AD did not err in refusing to consider new evidence advanced in support of the application for leave.

#### 9501:1:subtheme:5 · paragraphs 15-16

- Raw key terms: `appeal, decision, evidence, glover, medical, proposed, raised, respect`
- Display key terms: `glover, medical, proposed, raised, respect`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: glover, medical, proposed, raised, respect Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4480629` offsets `101-106`; context: [22] With respect to the reasonableness of the SST-AD decision, the SST-AD accurately identified the issue raised and the requirement for Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480629` offsets `330-338`; context: Glover’s medical evidence and the evidence relating to his post-accident work record.
- Evidence: `counterargument_limitation` cue `but` at chunk `4480629` offsets `273-276`; context: The SST-AD noted the grounds of appeal but found the SST-GD had considered Mr.
- Evidence: `issue` cue `issues` at chunk `4480630` offsets `60-66`; context: [23] In reaching these conclusions the SST-AD addressed the issues raised by Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480630` offsets `586-594`; context: Glover argues that he was inadequately represented before the SST-GD and SST-AD and as a result relevant medical evidence was not placed before the decision-makers.
- Evidence: `counterargument_limitation` cue `However` at chunk `4480630` offsets `638-645`; context: However Mr.

#### 9501:1:subtheme:6 · paragraphs 17-21

- Raw key terms: `counsel, canada, court, establish, addressed, appeal, applicant, assistance`
- Display key terms: `establish, addressed, assistance`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: establish, addressed, assistance Evidence spans paragraphs 17-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4480631` offsets `33-38`; context: [25] In the criminal context the issue of ineffective assistance of counsel was addressed by the Supreme Court of Canada in R v GDB, 2000 SCC 22 [GDB].
- Evidence: `evidence_fact` cue `evidence` at chunk `4480634` offsets `82-90`; context: [27] In this case the bare allegation of ineffective counsel is only supported by evidence of a complaint to the Law Society of Upper Canada.
- Evidence: `counterargument_limitation` cue `but` at chunk `4480634` offsets `376-379`; context: The complaint effectively repeats the allegation of incompetence but provides no evidence in support of the allegation.

#### Section text

Glover v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-04-12
Neutral citation
2017 FC 363
File numbers
T-1510-15
Decision Content
Date: 20170412
Docket: T-1510-15
Citation: 2017 FC 363
Ottawa, Ontario, April 12, 2017
PRESENT: The Honourable Mr. Justice Gleeson
BETWEEN:
EDWARD GLOVER
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Overview [1] Mr. Glover, the applicant, applied for a disability pension under the Canada Pension Plan, RSC 1985, c C-8 [CPP]. His application was denied and the denial was upheld on reconsideration. Mr. Glover appealed the negative decision to the Social Security Tribunal-General Division [SST-GD]. The SST-GD found that Mr. Glover had failed to establish that he suffered from a severe disability as defined in the CPP.

[2] Mr. Glover sought leave to appeal this decision to the Social Security Tribunal-Appeal Division [SST-AD]. Leave was denied. It is that decision that is now before the Court for judicial review. Mr. Glover submits that the SST-AD erred in failing to consider new evidence that demonstrated he suffered from a severe and prolonged disability. He further submits that the process before both the SST-GD and the SST-AD was procedurally unfair due to the ineffective assistance of his representative.

[3] The Department of Employment and Social Development Act, SC 2005, c 34 [DESDA] identifies the grounds of appeal from an SST-GD decision and provides that the SST-AD shall refuse to grant leave where it is satisfied the appeal has no reasonable chance of success. In this case I am unable to conclude that the SST-AD decision to deny leave to appeal the negative SST-GD decision was unreasonable or that the process was procedurally unfair. The application for judicial review is denied for the reasons that follow.
II. Background A. General [4] Mr. Glover worked in the construction and masonry industry for many years and had owned his own masonry company. In 2008 he was involved in motor vehicle accident. As a result of that accident he states he is no longer able to work due to generalized musculoskeletal pain, whiplash and abnormal discs in the cervical spine.

[5] Subsequent to the accident Mr. Glover’s company continued to operate. He provided some administrative and advisory services to the company until it went bankrupt in 2011. He also performed some work in 2012 but has not looked for any employment since on the basis that there were no other jobs he could feasibly do in the masonry trade due to his physical limitations.

[6] Mr. Glover’s denial of disability benefits was appealed to the Office of the Commissioner of Review Tribunals. However, pursuant to section 257 of the Jobs, Growth and Long-Term Prosperity Act, SC 2012, c 19, the matter was transferred to the SST-GD in April, 2013.
B. SST-GD Decision [7] In its decision, the SST-GD identifies the requirements to qualify for a disability pension as set out at subparagraph 44(1)(b) of the CPP: (1) be under 65 years of age; (2) not be in receipt of the CPP retirement pension; (3) be disabled; and (4) have made valid contributions to the CPP for not less than the Minimum Qualifying Period [MQP]. The SST-GD noted that an applicant will only be considered disabled where they establish: (1) they suffer from a severe and prolonged mental or physical disability as set out at subparagraph 42(2)(a) of the CPP; and (2) they suffered from that severe and prolonged disability on or before the end of the MQP date.

[8] The SST-GD determined Mr. Glover’s MQP date to be December 31, 2014 and that it was required to determine if it was more likely than not that Mr. Glover had a severe and prolonged disability on or before the MQP date.

[9] After reviewing the evidence including the medical reports placed before it, the SST-GD, undertook an analysis of whether Mr. Glover had established he suffered from a severe and prolonged disability. The SST-GD noted that the “severe” criterion must be assessed in a real-world context (Villani v Canada (Attorney General), 2001 FCA 248 at para 39). In considering this criterion the SST-GD noted Mr. Glover’s age, his level of education, and ability to communicate in English. The SST-GD also considered the experience he had gained working in the masonry business and noted that having owned his own business for 13 years he would have obtained administrative and supervisory experience leading a team of employees. At paragraph 33 of its decision, the SST-GD concluded that Mr. Glover possessed transferable skills and would be a “candidate for suitable re-training for a more sedentary role working within his functional limitations.”

[10] Having concluded that Mr. Glover possessed transferrable skills, the SST-GD addressed his capacity to work. It did not question that Mr. Glover had sustained injuries following his motor vehicle accident, but found that he had continued to work in his business in a modified role until 2011 and as an estimator for several months in 2012. The SST-GD found his work as an estimator only ceased because he was not contacted for further work. It noted the absence of updated medical reports after 2011 indicating any incapacity or a decline in Mr. Glover’s health. The SST-GD concluded that Mr. Glover had not demonstrated that he suffered a “severe” disability and that it was therefore unnecessary to make a finding on the “prolonged” criterion.
C. SST-AD Leave to Appeal Decision [11] The SST-AD noted that Mr. Glover’s counsel submitted that the SST-GD had erred by drawing an incorrect conclusion from the evidence and had based its decision on an erroneous finding of fact. It noted that pursuant to subsection 58(3) of the DESDA that it must either grant or refuse leave to appeal, and that leave is to be refused if the SST-AD is satisfied the appeal has no reasonable chance of success (subsection 58(2)). The SST-AD noted that a reasonable chance of success equates to an arguable case. It then considered whether the appeal had a reasonable chance of success.

[12] The SST-AD addressed the arguments advanced in support of the position that the SST-GD had erred. However it found that the SST-GD had considered Mr. Glover’s post-accident work history and the medical and other reports that had been placed in evidence. The SST-AD held that the SST-GD’s conclusions were based on a considered analysis of the facts and that Mr. Glover’s counsel was simply inviting the SST-AD to reweigh the evidence. On this basis it concluded the appeal had no reasonable chance of success.
III. Legislation [13] Relevant portions of the CPP and DESDA are reproduced at Appendix A for ease of reference.
IV. Issues [14] The applicant raises the following issues:
A. The SST-AD failed to consider all of the relevant evidence relating to the applicant’s medical condition rendering the process unfair and the decision not to grant leave unreasonable; and
B. The applicant was ineffectively represented before the SST-GD and SST-AD.
V. Standard of Review [15] The parties agree and the jurisprudence establishes that a decision of the SST-AD denying leave to appeal is to be reviewed against a reasonableness standard (Canada (Attorney General) v Hines, 2016 FC 112 at para 28, citing Tracey v Canada (Attorney General), 2015 FC 1300 at para 17 [Tracey]).

[16] When considering whether there was a procedural fairness breach arising out of the allegations of incompetent or negligent representation of counsel the correctness standard of review applies (Galyas v Canada (Minister of Citizenship and Immigration), 2013 FC 250 at para 27).
VI. Analysis A. Consideration of the Evidence [17] Mr. Glover argues that the evidence before the SST-GD was incomplete, something the SST-GD noted in its decision. Mr. Glover’s counsel argued in oral submissions that the SST-GD was seeking and should have allowed Mr. Glover to obtain additional evidence before it rendered its negative decision. He also argues that the SST-AD having been provided with updated information relating to his medical condition had an obligation to consider that evidence in rendering the leave to appeal decision. Mr. Glover submits that in the circumstances there was a breach of procedural fairness and the decision is unreasonable. I disagree.

[18] Contrary to the submissions made by Mr. Glover’s counsel, the SST-GD did not request or seek out further information. Instead the SST-GD noted at paragraph 40 of its decision that “[t]here have been no updated medical reports submitted beyond 2011 to suggest any ongoing incapacity to work or a decline in the Appellant’s health condition”. It is trite law that Mr. Glover had the burden of establishing his claim before the SST-GD and demonstrating to the SST-AD that his appeal possessed a reasonable chance of success (Tracey at para 31). The SST-GD had no duty to request further information or advance Mr. Glover’s case on his behalf. Indeed, the SST-AD noted at paragraph 9 of its decision that the SST-GD “considered the medical and other reports that were before him”. The implication being that the SST-AD was satisfied that the SST-GD had not indicated additional evidence was preferred but rather considered the evidence placed before it.

[19] With respect to the attempt to place new evidence before the SST-AD as part of the application for leave, this was addressed by Justice Michael Manson in Canada (Attorney General) v O’Keefe, 2016 FC 503 at paragraph 28 [O’Keefe], where he states:

[28] Moreover, the legislative scheme governing the SST-AD is distinguishable from the former PAB scheme and the cases decided under it which viewed such decisions as interlocutory. Under sections 55 to 58 of the DESDA, the test for obtaining leave to appeal and the nature of the appeal has changed. Unlike an appeal before the former PAB, which was de novo, an appeal to the SST-AD does not allow for new evidence and is limited to the three grounds of appeal listed in section 58. Also, under subsection 58(5), once leave is granted, the application for leave becomes the notice of appeal. Further, the SST-AD’s leave decision demarcates the issues on appeal that have a reasonable chance of success (Belo-Alves v Canada (Attorney General), 2014 FC 1100 at paras 71-73).

[20] I adopt and endorse the reasoning of Justice Manson in O’Keefe. In doing so I note that the DESDA does make provision, at section 66, for the SST-GD to rescind or amend a decision where new evidence is presented by way of application. There is no indication on the record that Mr. Glover sought to do so. Indeed, in submissions to the SST-AD for leave to appeal, counsel for the applicant wrote “this is not a new fact application”.

[21] I am satisfied that the SST-AD did not err in refusing to consider new evidence advanced in support of the application for leave. There was no breach of procedural fairness.

[22] With respect to the reasonableness of the SST-AD decision, the SST-AD accurately identified the issue raised and the requirement for Mr. Glover to demonstrate “…some arguable ground upon which the proposed appeal might succeed”. The SST-AD noted the grounds of appeal but found the SST-GD had considered Mr. Glover’s medical evidence and the evidence relating to his post-accident work record. The SST-AD found the arguments in support of the appeal repeated the submissions made before the SST-GD and that the generalised allegations of error were nothing more than an effort to have the SST-AD reweigh the evidence.

[23] In reaching these conclusions the SST-AD addressed the issues raised by Mr. Glover, explained the reasons for finding the proposed appeal did not disclose a reasonable chance of success and rendered its decision. The decision is within the range of possible, acceptable outcomes which are defensible in respect of the facts and law and is justified, transparent and intelligible (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47).
B. Inadequate representation [24] Mr. Glover argues that he was inadequately represented before the SST-GD and SST-AD and as a result relevant medical evidence was not placed before the decision-makers. However Mr. Glover provides little evidence in support of the allegation of inadequate representation.

[25] In the criminal context the issue of ineffective assistance of counsel was addressed by the Supreme Court of Canada in R v GDB, 2000 SCC 22 [GDB]. To succeed an applicant must establish that counsel’s acts or omissions: (1) constituted incompetence; and (2) that an injustice resulted, in other words the result would have been different (GDB at para 26).

[26] The burden is on the applicant to establish the performance and the prejudice components of the test. The analysis proceeds from a strong presumption that counsel’s conduct fell within the range of reasonable professional assistance (GDB at para 27). In Hallatt v Canada, 2004 FCA 104 at para 21 the Federal Court of Appeal recognized that GDB was a criminal case and stated:

[21] […] this must be taken into account … [i]n civil disputes where an individual’s constitutionally protected rights are not at stake, concerns about the propriety of counsel’s trial strategy and conduct and their competence to make tactical decisions can usually be adequately addressed through a claim for damages and negligence against the solicitor, or a complaint to the governing law society.

[27] In this case the bare allegation of ineffective counsel is only supported by evidence of a complaint to the Law Society of Upper Canada. The document simply states “The Paralegal failed on multiple occasions to have material available for the General Division decision, and for the Leave Appeal decision”. The complaint effectively repeats the allegation of incompetence but provides no evidence in support of the allegation.

[28] Recognizing the strong presumption in favour of adequate representation and the requirement to establish actual prejudice, Mr. Glover has failed to demonstrate any basis justifying the Court’s intervention.


## 9501:2 · paragraphs 22-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `005acdff761a291b488c911ac6f1e18103138bddc0c18be7c871d4b3f1c32419`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9501:2:subtheme:1 · paragraphs 22-23

- Raw key terms: `accident, allegation, appeal, application, assistance, awarded, bald, cannot`
- Display key terms: `accident, allegation, assistance, awarded, bald, cannot`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, reasoning_application Display terms: accident, allegation, assistance, awarded, bald, cannot Application context: In light of these facts it was not unreasonable for the SST-AD to conclude that there was no reasonable chance of success on appeal. Operative outcome context: Glover’s medical circumstances, the application is dismissed. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4480635` offsets `237-245`; context: Conclusion [29] The evidence established that Mr.
- Evidence: `reasoning_application` cue `conclude` at chunk `4480635` offsets `721-729`; context: In light of these facts it was not unreasonable for the SST-AD to conclude that there was no reasonable chance of success on appeal.
- Evidence: `counterargument_limitation` cue `However` at chunk `4480635` offsets `409-416`; context: However the SST-GD reasonably concluded that Mr.
- Evidence: `disposition` cue `dismissed` at chunk `4480635` offsets `952-961`; context: Glover’s medical circumstances, the application is dismissed.

#### Section text

VII. Conclusion [29] The evidence established that Mr. Glover suffered injuries in the 2008 motor vehicle accident and the injuries impacted his work capacity in a physically demanding occupation. However the SST-GD reasonably concluded that Mr. Glover possessed transferable work skills, he retained a capacity to work, had continued to work until 2012 in a modified role and ceased work at that time when he was not offered subsequent work. In light of these facts it was not unreasonable for the SST-AD to conclude that there was no reasonable chance of success on appeal. Similarly the bald allegation of ineffective assistance of counsel cannot succeed. While I am sympathetic to Mr. Glover’s medical circumstances, the application is dismissed.

[30] The respondent did not seek costs and none will be awarded.


## 9501:3 · paragraphs 24-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3de43ad2bf7438569a7e1a37d4daa8fe61e34e4f77817feec38796bebc90f8cb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9501:3:subtheme:1 · paragraphs 24-25

- Raw key terms: `canada, date, general, hearing, record, abusive, accord, accordance`
- Display key terms: `date, hearing, abusive, accord, accordance`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, hearing, abusive, accord, accordance No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed. No costs are awarded.
"Patrick Gleeson"
Judge
APPENDIX A
Canada Pension Plan, RSC, 1985, c C-8
[…]
42(2) For the purposes of this Act,
(a) a person shall be considered to be disabled only if he is determined in prescribed manner to have a severe and prolonged mental or physical disability, and for the purposes of this paragraph,
(i) a disability is severe only if by reason thereof the person in respect of whom the determination is made is incapable regularly of pursuing any substantially gainful occupation, and
(ii) a disability is prolonged only if it is determined in prescribed manner that the disability is likely to be long continued and of indefinite duration or is likely to result in death; and
(b) a person is deemed to have become or to have ceased to be disabled at the time that is determined in the prescribed manner to be the time when the person became or ceased to be, as the case may be, disabled, but in no case shall a person — including a contributor referred to in subparagraph 44(1)(b)(ii) — be deemed to have become disabled earlier than fifteen months before the time of the making of any application in respect of which the determination is made.
[…]
44 (1) Subject to this Part,
[…]
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom no retirement pension is payable, who is disabled and who
(i) has made contributions for not less than the minimum qualifying period,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.1 had not been made;
[…]
60 (1) No benefit is payable to any person under this Act unless an application therefor has been made by him or on his behalf and payment of the benefit has been approved under this Act.
[…]
81 (1) Where
[…]
(b) an applicant is dissatisfied with any decision made under section 60,
[…]
the dissatisfied party or, subject to the regulations, any person on behalf thereof may, within ninety days after the day on which the dissatisfied party was notified in the prescribed manner of the decision or determination, or within such longer period as the Minister may either before or after the expiration of those ninety days allow, make a request to the Minister in the prescribed form and manner for a reconsideration of that decision or determination.
[…]
(2) The Minister shall reconsider without delay any decision or determination referred to in subsection (1) or (1.1) and may confirm or vary it, and may approve payment of a benefit, determine the amount of a benefit or determine that no benefit is payable, and shall notify in writing the party who made the request under subsection (1) or (1.1) of the Minister’s decision and of the reasons for it.
(3) The Minister may, on new facts, rescind or amend a decision made by him or her under this Act.
[…]
82 A party who is dissatisfied with a decision of the Minister made under section 81, including a decision in relation to further time to make a request, or, subject to the regulations, any person on their behalf, may appeal the decision to the Social Security Tribunal established under section 44 of the Department of Employment and Social Development Act.
[…]
42(2) Pour l’application de la présente loi :
a) une personne n’est considérée comme invalide que si elle est déclarée, de la manière prescrite, atteinte d’une invalidité physique ou mentale grave et prolongée, et pour l’application du présent alinéa :
(i) une invalidité n’est grave que si elle rend la personne à laquelle se rapporte la déclaration régulièrement incapable de détenir une occupation véritablement rémunératrice,
(ii) une invalidité n’est prolongée que si elle est déclarée, de la manière prescrite, devoir vraisemblablement durer pendant une période longue, continue et indéfinie ou devoir entraîner vraisemblablement le décès;
b) une personne est réputée être devenue ou avoir cessé d’être invalide à la date qui est déterminée, de la manière prescrite, être celle où elle est devenue ou a cessé d’être, selon le cas, invalide, mais en aucun cas une personne — notamment le cotisant visé au sous-alinéa 44(1)b)(ii) — n’est réputée être devenue invalide à une date antérieure de plus de quinze mois à la date de la présentation d’une demande à l’égard de laquelle la détermination a été faite.
[…]
44 (1) Sous réserve des autres dispositions de la présente partie :
[…]
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si un partage des gains non ajustés ouvrant droit à pension n’avait pas été effectué en application des articles 55 et 55.1;
[…]
60 (1) Aucune prestation n’est payable à une personne sous le régime de la présente loi, sauf si demande en a été faite par elle ou en son nom et que le paiement en ait été approuvé selon la présente loi.
[…]
81 (1) Dans les cas où :
[…]
b) un requérant n’est pas satisfait d’une décision rendue en application de l’article 60,
[…]
ceux-ci peuvent, ou, sous réserve des règlements, quiconque de leur part, peut, dans les quatre-vingt-dix jours suivant le jour où ils sont, de la manière prescrite, avisés de la décision ou de l’arrêt, ou dans tel délai plus long qu’autorise le ministre avant ou après l’expiration de ces quatre-vingt-dix jours, demander par écrit à celui-ci, selon les modalités prescrites, de réviser la décision ou l’arrêt.
[…]
(2) Le ministre reconsidère sans délai toute décision ou tout arrêt visé au paragraphe (1) ou (1.1) et il peut confirmer ou modifier cette décision ou arrêt; il peut approuver le paiement d’une prestation et en fixer le montant, de même qu’il peut arrêter qu’aucune prestation n’est payable et il doit dès lors aviser par écrit de sa décision motivée la personne qui a fait la demande en vertu des paragraphes (1) ou (1.1).
3) Le ministre peut, en se fondant sur des faits nouveaux, annuler ou modifier une décision qu’il a lui-même rendue conformément à la présente loi.
[…]
82 La personne qui se croit lésée par une décision du ministre rendue en application de l’article 81, notamment une décision relative au délai supplémentaire, ou, sous réserve des règlements, quiconque de sa part, peut interjeter appel de la décision devant le Tribunal de la sécurité sociale, constitué par l’article 44 de la Loi sur le ministère de l’Emploi et du Développement social.
Department of Employment and Social Development Act, SC 2005, c 34
Appeal — time limit
52 (1) An appeal of a decision must be brought to the General Division in the prescribed form and manner and within,
(a) in the case of a decision made under the Employment Insurance Act, 30 days after the day on which it is communicated to the appellant; and
(b) in any other case, 90 days after the day on which the decision is communicated to the appellant.
(2) The General Division may allow further time within which an appeal may be brought, but in no case may an appeal be brought more than one year after the day on which the decision is communicated to the appellant.
53 (1) The General Division must summarily dismiss an appeal if it is satisfied that it has no reasonable chance of success.
(2) The General Division must give written reasons for its decision and send copies to the appellant and the Minister or the Commission, as the case may be, and any other party.
(3) The appellant may appeal the decision to the Appeal Division.
54 (1) The General Division may dismiss the appeal or confirm, rescind or vary a decision of the Minister or the Commission in whole or in part or give the decision that the Minister or the Commission should have given.
(2) The General Division must give written reasons for its decision and send copies to the appellant and the Minister or the Commission, as the case may be, and any other party.
55 Any decision of the General Division may be appealed to the Appeal Division by any person who is the subject of the decision and any other prescribed person.
56 (1) An appeal to the Appeal Division may only be brought if leave to appeal is granted.
(2) Despite subsection (1), no leave is necessary in the case of an appeal brought under subsection 53(3).
57 (1) An application for leave to appeal must be made to the Appeal Division in the prescribed form and manner and within,
(a) in the case of a decision made by the Employment Insurance Section, 30 days after the day on which it is communicated to the appellant; and
(b) in the case of a decision made by the Income Security Section, 90 days after the day on which the decision is communicated to the appellant.
(2) The Appeal Division may allow further time within which an application for leave to appeal is to be made, but in no case may an application be made more than one year after the day on which the decision is communicated to the appellant.
58 (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
(3) The Appeal Division must either grant or refuse leave to appeal.
(4) The Appeal Division must give written reasons for its decision to grant or refuse leave and send copies to the appellant and any other party.
(5) If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed.
59 (1) The Appeal Division may dismiss the appeal, give the decision that the General Division should have given, refer the matter back to the General Division for reconsideration in accordance with any directions that the Appeal Division considers appropriate or confirm, rescind or vary the decision of the General Division in whole or in part.
(2) The Appeal Division must give written reasons for its decision and send copies to the appellant and any other party.
[…]
66 (1) The Tribunal may rescind or amend a decision given by it in respect of any particular application if
(a) in the case of a decision relating to the Employment Insurance Act, new facts are presented to the Tribunal or the Tribunal is satisfied that the decision was made without knowledge of, or was based on a mistake as to, some material fact; or
(b) in any other case, a new material fact is presented that could not have been discovered at the time of the hearing with the exercise of reasonable diligence.
(2) An application to rescind or amend a decision must be made within one year after the day on which a decision is communicated to the appellant.
(3) Each person who is the subject of a decision may make only one application to rescind or amend that decision.
(4) A decision is rescinded or amended by the same Division that made it.
Modalités de présentation
52 (1) L’appel d’une décision est interjeté devant la division générale selon les modalités prévues par règlement et dans le délai suivant :
a) dans le cas d’une décision rendue au titre de la Loi sur l’assurance-emploi, dans les trente jours suivant la date où l’appelant reçoit communication de la décision;
b) dans les autres cas, dans les quatre-vingt-dix jours suivant la date où l’appelant reçoit communication de la décision.
(2) La division générale peut proroger d’au plus un an le délai pour interjeter appel.
53 (1) La division générale rejette de façon sommaire l’appel si elle est convaincue qu’il n’a aucune chance raisonnable de succès.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et, selon le cas, au ministre ou à la Commission, et à toute autre partie.
(3) L’appelant peut en appeler à la division d’appel de cette décision.
54 (1) La division générale peut rejeter l’appel ou confirmer, infirmer ou modifier totalement ou partiellement la décision visée par l’appel ou rendre la décision que le ministre ou la Commission aurait dû rendre.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et, selon le cas, au ministre ou à la Commission, et à toute autre partie.
55 Toute décision de la division générale peut être portée en appel devant la division d’appel par toute personne qui fait l’objet de la décision et toute autre personne visée par règlement.
56 (1) Il ne peut être interjeté d’appel à la division d’appel sans permission.
(2) Toutefois, il n’est pas nécessaire d’obtenir une permission dans le cas d’un appel interjeté au titre du paragraphe 53(3).
57 (1) La demande de permission d’en appeler est présentée à la division d’appel selon les modalités prévues par règlement et dans le délai suivant :
a) dans le cas d’une décision rendue par la section de l’assurance-emploi, dans les trente jours suivant la date où l’appelant reçoit communication de la décision;
b) dans le cas d’une décision rendue par la section de la sécurité du revenu, dans les quatre-vingt-dix jours suivant la date où l’appelant reçoit communication de la décision.
(2) La division d’appel peut proroger d’au plus un an le délai pour présenter la demande de permission d’en appeler.
58 (1) Les seuls moyens d’appel sont les suivants :
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.
(3) Elle accorde ou refuse cette permission.
(4) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et à toute autre partie.
(5) Dans les cas où la permission est accordée, la demande de permission est assimilée à un avis d’appel et celui-ci est réputé avoir été déposé à la date du dépôt de la demande de permission.
59 (1) La division d’appel peut rejeter l’appel, rendre la décision que la division générale aurait dû rendre, renvoyer l’affaire à la division générale pour réexamen conformément aux directives qu’elle juge indiquées, ou confirmer, infirmer ou modifier totalement ou partiellement la décision de la division générale.
(2) Elle rend une décision motivée par écrit et en fait parvenir une copie à l’appelant et à toute autre partie.
[…]
66 (1) Le Tribunal peut annuler ou modifier toute décision qu’il a rendue relativement à une demande particulière :
a) dans le cas d’une décision visant la Loi sur l’assurance-emploi, si des faits nouveaux lui sont présentés ou s’il est convaincu que la décision a été rendue avant que soit connu un fait essentiel ou a été fondée sur une erreur relative à un tel fait;
b) dans les autres cas, si des faits nouveaux et essentiels qui, au moment de l’audience, ne pouvaient être connus malgré l’exercice d’une diligence raisonnable lui sont présentés.
(2) La demande d’annulation ou de modification doit être présentée au plus tard un an après la date où l’appelant reçoit communication de la décision.
(3) Il ne peut être présenté plus d’une demande d’annulation ou de modification par toute partie visée par la décision.
(4) La décision est annulée ou modifiée par la division qui l’a rendue.
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1510-15
STYLE OF CAUSE:
EDWARD GLOVER v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
February 1, 2017


## 9501:4 · paragraphs 26-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ec10f7ae0b508b1f58be6f4c6532215c672d08bc9d7a7bed9890b2366402295f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9501:4:subtheme:1 · paragraphs 26-26

- Raw key terms: `appearances, applicant, april, attorney, barristers, canada, corporation, dated`
- Display key terms: `april, barristers, corporation, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, barristers, corporation, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GLEESON J.
DATED:
April 12, 2017
APPEARANCES:
Sidney Klotz
For The Applicant
Sylvie Doire
For The Respondent
SOLICITORS OF RECORD:
Jennifer Klotz Law Firm
Professional Corporation
Barristers and Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
