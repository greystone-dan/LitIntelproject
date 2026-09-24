# Discussion Units: case 23256

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **56**
- Continuity pairs: **55**
- Discussion Units: **4**
- Paragraph source hashes: **56**
- Sub-themes: **18**

## 23256:1 · paragraphs 0-6

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e82e74763a26ba170b7ebbb33ad0bff58656f9807bed6c26e525de34c4161f77`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23256:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, decision, franciska, immigration, spasoja, appeal, application, canada`
- Display key terms: `franciska, spasoja`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: franciska, spasoja Rule/authority context: The application for judicial review was filed pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (Act). Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5092102` offsets `287-298`; context: The application for judicial review was filed pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (Act).

#### 23256:1:subtheme:2 · paragraphs 2-4

- Raw key terms: `case, court, appeal, decision, heard, identify, issue, reasonableness`
- Display key terms: `case, heard, identify, reasonableness`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application Display terms: case, heard, identify, reasonableness Position/evidence statements: The applicant thus did not try to submit arguments on the basis of the particular facts of this case. Rule/authority context: She instead claims that she was denied the appeal entitled to her under the Act. | It fully availed itself of Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 (Dunsmuir), and of the case law of this Court to identify its “standard of review”. Application context: She is therefore asking to be heard by the RAD on the appropriate basis, which is not the deference that accompanies the reasonableness standard chosen by the RAD. | [6] Thus, the RAD wanted to recognize the expertise of the RPD and therefore wanted to adopt the standard of reasonableness except for questions of law or natural justice (which now fall within procedural fairness). Operative outcome context: She instead claims that she was denied the appeal entitled to her under the Act. Evidence spans paragraphs 2-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092103` offsets `13-18`; context: [2] The only issue before the Court is to evaluate the RAD’s role when it heard the appeal of the RPD decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `5092103` offsets `308-311`; context: The issue is whether that approach is consistent with the legislation enacted in 2001, 2010 and 2012 but implemented by the government only on December 15, 2012 (SI/2012‑94).
- Evidence: `issue` cue `issue` at chunk `5092104` offsets `14-19`; context: [3] Given the issue at hand, the facts in the case are of little importance.
- Evidence: `party_position` cue `submit` at chunk `5092104` offsets `111-117`; context: The applicant thus did not try to submit arguments on the basis of the particular facts of this case.
- Evidence: `governing_rule` cue `under` at chunk `5092104` offsets `245-250`; context: She instead claims that she was denied the appeal entitled to her under the Act.
- Evidence: `reasoning_application` cue `therefore` at chunk `5092104` offsets `267-276`; context: She is therefore asking to be heard by the RAD on the appropriate basis, which is not the deference that accompanies the reasonableness standard chosen by the RAD.
- Evidence: `disposition` cue `denied` at chunk `5092104` offsets `211-217`; context: She instead claims that she was denied the appeal entitled to her under the Act.
- Evidence: `governing_rule` cue `standard of review` at chunk `5092105` offsets `361-379`; context: It fully availed itself of Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 (Dunsmuir), and of the case law of this Court to identify its “standard of review”.
- Evidence: `reasoning_application` cue `therefore` at chunk `5092105` offsets `67-76`; context: [6] Thus, the RAD wanted to recognize the expertise of the RPD and therefore wanted to adopt the standard of reasonableness except for questions of law or natural justice (which now fall within procedural fairness).

#### 23256:1:subtheme:3 · paragraphs 5-6

- Raw key terms: `case, correctness, court, dunsmuir, four, identified, issues, judicial`
- Display key terms: `case, correctness, dunsmuir, four, identified, issues, judicial`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: case, correctness, dunsmuir, four, identified, issues, judicial Rule/authority context: It also seems that the RAD chooses the correctness standard for questions of law, which is different from judicial review, where the presumption is that a question of law also falls under the standard of reasonableness ( | [8] Issues of central importance to the legal system are one of the four categories identified by the case law of the Supreme Court as requiring the correctness standard of review, which is more favourable to judicial in Application context: Justice Phelan found that the issue of the applicable standard had to be assessed by this Court on the basis of correctness because it is a question of general interest to the legal system that goes beyond the scope of t | It seems to me that another category identified in Dunsmuir could apply in this case: Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5092106` offsets `249-255`; context: [25] Relying on the reasoning of the Alberta Court of Appeal and on the factors identified in its analysis of Newton, and making the necessary adjustments to the particular context of the RPD and the RAD, I am of the opinion that, except for strict issues of law or natural justice, it is appropriate for us, as RAD members, to extend the same deference to RPD decision.
- Evidence: `evidence_fact` cue `found that` at chunk `5092106` offsets `1864-1874`; context: Justice Phelan found that the issue of the applicable standard had to be assessed by this Court on the basis of correctness because it is a question of general interest to the legal system that goes beyond the scope of the administrative tribunal’s expertise.
- Evidence: `governing_rule` cue `under` at chunk `5092106` offsets `875-880`; context: It also seems that the RAD chooses the correctness standard for questions of law, which is different from judicial review, where the presumption is that a question of law also falls under the standard of reasonableness (Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, [2011] 3 SCR 654, at paragraph 34; Canadian National Railway Co.
- Evidence: `reasoning_application` cue `because` at chunk `5092106` offsets `1973-1980`; context: Justice Phelan found that the issue of the applicable standard had to be assessed by this Court on the basis of correctness because it is a question of general interest to the legal system that goes beyond the scope of the administrative tribunal’s expertise.
- Evidence: `issue` cue `Issues` at chunk `5092107` offsets `4-10`; context: [8] Issues of central importance to the legal system are one of the four categories identified by the case law of the Supreme Court as requiring the correctness standard of review, which is more favourable to judicial intervention.
- Evidence: `governing_rule` cue `standard of review` at chunk `5092107` offsets `161-179`; context: [8] Issues of central importance to the legal system are one of the four categories identified by the case law of the Supreme Court as requiring the correctness standard of review, which is more favourable to judicial intervention.
- Evidence: `reasoning_application` cue `apply` at chunk `5092107` offsets `298-303`; context: It seems to me that another category identified in Dunsmuir could apply in this case:

#### Section text

Spasoja v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-09-23
Neutral citation
2014 FC 913
File numbers
IMM-7630-13
Decision Content
Date: 20140923
Docket: IMM-7630-13
Citation: 2014 FC 913
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, September 23, 2014
PRESENT: The Honourable Mr. Justice Roy
BETWEEN:
FRANCISKA SPASOJA
Applicant
and
MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application for judicial review filed by the applicant, Franciska Spasoja, of the decision of the Refugee Appeal Division (RAD) that confirmed the determination of the Refugee Protection Division (RPD), deeming it reasonable. The application for judicial review was filed pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27 (Act).

[2] The only issue before the Court is to evaluate the RAD’s role when it heard the appeal of the RPD decision. As will be discussed further, in this case, the RAD chose to act as a sort of reviewing court. The issue is whether that approach is consistent with the legislation enacted in 2001, 2010 and 2012 but implemented by the government only on December 15, 2012 (SI/2012‑94).

[3] Given the issue at hand, the facts in the case are of little importance. The applicant thus did not try to submit arguments on the basis of the particular facts of this case. She instead claims that she was denied the appeal entitled to her under the Act. She is therefore asking to be heard by the RAD on the appropriate basis, which is not the deference that accompanies the reasonableness standard chosen by the RAD.
I. Facts [4] The applicant is a Kosovar Serb. She is Catholic by religion. She states that she fears persecution in her country of citizenship, Kosovo, because the Muslim population apparently challenged her way of life, which was suspected as being homosexual because she is single and allegedly had a circle of friends that consisted of mostly women. She was purportedly threatened and discriminated against, namely with respect to employment.
II. Decision under review [5] The decision under review is that of the Refugee Appeal Division. In very well articulated reasons, the RAD sought to determine the scope of the appeals it must hear. Recognizing from the outset that it was not a judicial review exercised by a court, and that the Act indeed refers to an appeal, the RAD seemed to find inspiration in the decision of the Alberta Court of Appeal in Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 (Newton) to identify a standard of review that corresponds to the standard of review in judicial review matters.

[6] Thus, the RAD wanted to recognize the expertise of the RPD and therefore wanted to adopt the standard of reasonableness except for questions of law or natural justice (which now fall within procedural fairness). It fully availed itself of Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 (Dunsmuir), and of the case law of this Court to identify its “standard of review”. The RAD found the following at paragraph 25:

[25] Relying on the reasoning of the Alberta Court of Appeal and on the factors identified in its analysis of Newton, and making the necessary adjustments to the particular context of the RPD and the RAD, I am of the opinion that, except for strict issues of law or natural justice, it is appropriate for us, as RAD members, to extend the same deference to RPD decision. In fact, this is the same deference as that which courts of law are required to extend to first level decision makers when the issue is a question of fact or a question of mixed law and fact.
In fact, the RAD identified its standard in the same terms as Dunsmuir and by citing the decision at the now famous paragraph 47. It also seems that the RAD chooses the correctness standard for questions of law, which is different from judicial review, where the presumption is that a question of law also falls under the standard of reasonableness (Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, [2011] 3 SCR 654, at paragraph 34; Canadian National Railway Co. v Canada (Attorney General), 2014 SCC 40 (CN v Canada), at paragraph 55) when an administrative tribunal is interpreting its home statue or a statute directly related to its mandate. Regarding the four types of questions of law identified in Dunsmuir, above, that call for the correctness standard of review, it seems that there is consensus that that would be the appropriate standard for both the RAD and the courts.
III. Standard of review and analysis [7] My colleague Justice Michael Phelan rendered a decision on August 22 on the same issues as those raised in this case (Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 (Huruglica)). In that decision, the RAD also found, based on Newton, above, that it had to impose a standard of review of reasonableness. Justice Phelan found that the issue of the applicable standard had to be assessed by this Court on the basis of correctness because it is a question of general interest to the legal system that goes beyond the scope of the administrative tribunal’s expertise. As already stated, it is clear from Dunsmuir, above, that not many issues determined by an administrative tribunal are reviewed on a basis other than reasonableness, including questions of law. The type of issue identified by Justice Phelan is one of them.

[8] Issues of central importance to the legal system are one of the four categories identified by the case law of the Supreme Court as requiring the correctness standard of review, which is more favourable to judicial intervention. It seems to me that another category identified in Dunsmuir could apply in this case:

## 23256:2 · paragraphs 7-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `8e655c196a16b37fa9c8af061e657aa16dc9b41e2081ace91425a6bddc2e2448`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23256:2:subtheme:1 · paragraphs 7-8

- Raw key terms: `standard, accepted, administrative, another, apply, applying, assn, attorney`
- Display key terms: `standard, accepted, administrative, another, apply, applying, assn`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: standard, accepted, administrative, another, apply, applying, assn Rule/authority context: The standard pursuant to which an administrative tribunal can quash a decision by another administrative tribunal can probably be equated with “jurisdictional lines” (in French “délimitation des compétences respectives”) Application context: [9] I would have come to the same conclusion by applying the standard of reasonableness to the issue of the standard that the RAD must apply to RPD decisions. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5092108` offsets `418-429`; context: The standard pursuant to which an administrative tribunal can quash a decision by another administrative tribunal can probably be equated with “jurisdictional lines” (in French “délimitation des compétences respectives”) if it is accepted that the tribunals involved here are competing specialized tribunals, even if they are both within the Immigration and Refugee Board of Canada.
- Evidence: `issue` cue `issue` at chunk `5092109` offsets `95-100`; context: [9] I would have come to the same conclusion by applying the standard of reasonableness to the issue of the standard that the RAD must apply to RPD decisions.
- Evidence: `reasoning_application` cue `apply` at chunk `5092109` offsets `135-140`; context: [9] I would have come to the same conclusion by applying the standard of reasonableness to the issue of the standard that the RAD must apply to RPD decisions.

#### 23256:2:subtheme:2 · paragraphs 9-12

- Raw key terms: `canada, court, meaning, unreasonable, above, advice, agree, analysis`
- Display key terms: `meaning, unreasonable, above, advice, agree, analysis`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: meaning, unreasonable, above, advice, agree, analysis Position/evidence statements: [11] In this case, while the RAD claimed to want to avoid duplicating the role of the RPD, it in fact transformed an appellate jurisdiction into judicial review using the same case law from the Supreme Court and this Cou Evidence spans paragraphs 9-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092110` offsets `135-140`; context: [10] Recently, the Supreme Court of Canada found that there was a reviewable error in a case where an access to information law was at issue.
- Evidence: `evidence_fact` cue `found that` at chunk `5092110` offsets `43-53`; context: [10] Recently, the Supreme Court of Canada found that there was a reviewable error in a case where an access to information law was at issue.
- Evidence: `issue` cue `whether` at chunk `5092111` offsets `179-186`; context: A recommendation, whether express or inferable, is still a recommendation.
- Evidence: `party_position` cue `claimed` at chunk `5092112` offsets `33-40`; context: [11] In this case, while the RAD claimed to want to avoid duplicating the role of the RPD, it in fact transformed an appellate jurisdiction into judicial review using the same case law from the Supreme Court and this Court in judicial review of immigration matters.

#### 23256:2:subtheme:3 · paragraphs 13-14

- Raw key terms: `appeal, fact, person, states, subject, subsection, accordance, accordant`
- Display key terms: `fact, person, states, subject, subsection, accordance, accordant`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: fact, person, states, subject, subsection, accordance, accordant Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092114` offsets `82-87`; context: An appellate jurisdiction is at issue and nothing else.
- Evidence: `evidence_fact` cue `record` at chunk `5092115` offsets `127-133`; context: The appeal proceeds on the basis of the record of proceedings and new documentary evidence, in addition of course to receiving written submissions from the parties (subsection 110(3)).
- Evidence: `counterargument_limitation` cue `but` at chunk `5092115` offsets `539-542`; context: In fact, the Act even expands the availability by rendering admissible the evidence that was available but that the person who is the subject of the appeal “could not reasonably have been expected in the circumstances to have presented, at the time of the rejection”.

#### Section text

[61] Questions regarding the jurisdictional lines between two or more competing specialized tribunals have also been subject to review on a correctness basis: Regina Police Assn. Inc. v. Regina (City) Board of Police Commissioners, [2000] 1 S.C.R. 360, 2000 SCC 14; Quebec (Commission des droits de la personne et des droits de la jeunesse) v. Quebec (Attorney General), [2004] 2 S.C.R. 185, 2004 SCC 39.
The standard pursuant to which an administrative tribunal can quash a decision by another administrative tribunal can probably be equated with “jurisdictional lines” (in French “délimitation des compétences respectives”) if it is accepted that the tribunals involved here are competing specialized tribunals, even if they are both within the Immigration and Refugee Board of Canada.

[9] I would have come to the same conclusion by applying the standard of reasonableness to the issue of the standard that the RAD must apply to RPD decisions.

[10] Recently, the Supreme Court of Canada found that there was a reviewable error in a case where an access to information law was at issue. In Untel v Ontario (Finances), 2014 SCC 36 (Ontario (Finances)), the Supreme Court quickly found that the interpretation given to two words (“advice” and “recommendation”), which resulted in them being given the same meaning, rendered the interpretation questionable and unreasonable.

[24] However, it appears to me that the approach taken in MOT and by the Adjudicator left no room for “advice” to have a distinct meaning from “recommendation”. A recommendation, whether express or inferable, is still a recommendation. “Advice” must have a distinct meaning. I agree with Evans J.A. in 3430901 Canada Inc. v. Canada (Minister of Industry), 2001 FCA 254, [2002] 1 F.C. 421 (“Telezone”), that in exempting “advice and recommendations” from disclosure, the legislative intention must be that the term “advice” has a broader meaning than the term “recommendations” (para. 50 (emphasis deleted)). Otherwise, it would be redundant. By leaving no room for “advice” to have a distinct meaning from “recommendation”, the Adjudicator’s decision was unreasonable.

[11] In this case, while the RAD claimed to want to avoid duplicating the role of the RPD, it in fact transformed an appellate jurisdiction into judicial review using the same case law from the Supreme Court and this Court in judicial review of immigration matters. The redundancy with the RPD that the RAD stated it wanted to avoid was created with judicial review, which must be judicial, by definition, and not administrative. That approach would appear to be as unreasonable as the interpretation given to the two words in Ontario (Finances). Here, the use of the term “appeal” and the appeal regime set out in the Act must be given a meaning other than simply an equivalent to judicial review. In my view, an examination of the wording of the Act that created the RAD, which was essentially enacted in 2001, long before the significant shift in Dunsmuir, above, and which only came into force on December 15, 2012, must be closely examined to discern Parliament’s intent with respect to the meaning of that appellate jurisdiction.
IV. Analysis [12] As for the ultimate result, I share the opinion of my colleague Justice Phelan in Huruglica, above, that the RAD committed a reviewable error according to any of the standards of review when it reviewed an RPD decision “on the reasonableness standard rather than conducting an independent assessment of the Applicants’ claim.” That is also the finding arrived at by Justice Shore in Alvarez v Canada (Citizenship and Immigration), 2014 FC 702 and Eng v Canada (Citizenship and Immigration), 2014 FC 711, which were both rendered on July 17.

[13] I agree, to a very great extent, with the Court’s analysis of the Act in Huruglica, above. I will focus on certain provisions.

[14] The Act is clear in both official languages. An appellate jurisdiction is at issue and nothing else. Subsection 110(1) states the following:
Appeal
Appel
110. (1) Subject to subsections (1.1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
110. (1) Sous réserve des paragraphes (1.1) et (2), la personne en cause et le ministre peuvent, conformément aux règles de la Commission, porter en appel — relativement à une question de droit, de fait ou mixte — auprès de la Section d’appel des réfugiés la décision de la Section de la protection des réfugiés accordant ou rejetant la demande d’asile.

[15] The Act also clearly states the manner in which the RAD must fulfill its mandate. The appeal proceeds on the basis of the record of proceedings and new documentary evidence, in addition of course to receiving written submissions from the parties (subsection 110(3)). The new evidence that did not exist at the time of the hearing before the RPD, or that was not available at that time, is admissible on appeal (subsection 110(4)). In fact, the Act even expands the availability by rendering admissible the evidence that was available but that the person who is the subject of the appeal “could not reasonably have been expected in the circumstances to have presented, at the time of the rejection”.

## 23256:3 · paragraphs 15-54

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `18eb7842882390b9dc1dc145897e2b64ab152dfb7493d4075ba640f11523b455`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23256:3:subtheme:1 · paragraphs 15-18

- Raw key terms: `evidence, hearing, appeal, cannot, decision, determination, made, matter`
- Display key terms: `hearing, cannot, determination, made, matter`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: hearing, cannot, determination, made, matter Rule/authority context: 37] Referrals Renvoi (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois : (a) the decis | With respect, I cannot see how such a legislative scheme could easily accommodate a standard of review in which deference prevails. Application context: If the RAD cannot dispose of the appeal by confirming the RPD determination or by substituting the determination that, in its opinion, should have been made, but the determination is erroneous, the matter may be referred Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092116` offsets `136-141`; context: [16] In a situation where documentary evidence is presented on appeal (subsection 110(3)), a hearing may be held if it raises a serious issue with respect to credibility (in addition to the fact that the documentary evidence is central to the decision and would justify allowing or rejecting the refugee protection claim: subsection 110(6)).
- Evidence: `evidence_fact` cue `evidence` at chunk `5092116` offsets `38-46`; context: [16] In a situation where documentary evidence is presented on appeal (subsection 110(3)), a hearing may be held if it raises a serious issue with respect to credibility (in addition to the fact that the documentary evidence is central to the decision and would justify allowing or rejecting the refugee protection claim: subsection 110(6)).
- Evidence: `evidence_fact` cue `evidence` at chunk `5092117` offsets `1503-1511`; context: 37]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `governing_rule` cue `under` at chunk `5092117` offsets `1454-1459`; context: 37]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5092117` offsets `1431-1437`; context: 37]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092118` offsets `342-350`; context: It can refer the matter back to the RPD only in specific circumstances, that is, when the decision is erroneous and when the decision cannot be confirmed or substituted by the RAD without holding a new hearing to reassess the evidence before the RPD.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5092118` offsets `250-256`; context: It can refer the matter back to the RPD only in specific circumstances, that is, when the decision is erroneous and when the decision cannot be confirmed or substituted by the RAD without holding a new hearing to reassess the evidence before the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092119` offsets `193-201`; context: Those circumstances do not include rehearing the evidence already before the RPD.
- Evidence: `governing_rule` cue `standard of review` at chunk `5092119` offsets `588-606`; context: With respect, I cannot see how such a legislative scheme could easily accommodate a standard of review in which deference prevails.
- Evidence: `reasoning_application` cue `because` at chunk `5092119` offsets `452-459`; context: If the RAD cannot dispose of the appeal by confirming the RPD determination or by substituting the determination that, in its opinion, should have been made, but the determination is erroneous, the matter may be referred back because a reassessment of the evidence is required.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5092119` offsets `237-243`; context: If the RAD cannot dispose of the appeal by confirming the RPD determination or by substituting the determination that, in its opinion, should have been made, but the determination is erroneous, the matter may be referred back because a reassessment of the evidence is required.

#### 23256:3:subtheme:2 · paragraphs 19-24

- Raw key terms: `back, cannot, decisions, deference, determination, judicial, reasonableness, referred`
- Display key terms: `back, cannot, decisions, deference, determination, judicial, reasonableness, referred`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: back, cannot, decisions, deference, determination, judicial, reasonableness, referred Application context: [23] Therefore, it is not difficult to accept that the standard of reasonableness prevails in administrative matters because review is not as much about appropriateness as it is about legality: because there is more than | [42] Moreover, even if one could conceive of a situation in which a clearly or highly irrational decision were distinguishable from a merely irrational decision, it would be unpalatable to require parties to accept an ir Evidence spans paragraphs 19-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5092120` offsets `485-493`; context: There is no question of owing deference: the determination is confirmed or a new determination is substituted.
- Evidence: `evidence_fact` cue `record` at chunk `5092120` offsets `222-228`; context: To the contrary, the Act instructs the RAD to examine the record of proceedings before the RPD while admitting additional evidence, in the prescribed circumstances.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5092123` offsets `5-14`; context: [23] Therefore, it is not difficult to accept that the standard of reasonableness prevails in administrative matters because review is not as much about appropriateness as it is about legality: because there is more than one possible reasonable result and administrative tribunals have special expertise, superior courts will intervene only in situations where the decision is unreasonable.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5092123` offsets `426-432`; context: Moreover, an unreasonable decision cannot be lawful, thus requiring judicial review.
- Evidence: `reasoning_application` cue `because` at chunk `5092124` offsets `245-252`; context: [42] Moreover, even if one could conceive of a situation in which a clearly or highly irrational decision were distinguishable from a merely irrational decision, it would be unpalatable to require parties to accept an irrational decision simply because, on a deferential standard, the irrationality of the decision is not clear enough.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092125` offsets `367-375`; context: Rather, we are dealing with a scheme where if there is, for example, an error of fact, the matter must be referred back to the RPD if a reassessment of the evidence before the RPD is required for a determination.

#### 23256:3:subtheme:3 · paragraphs 25-26

- Raw key terms: `appeal, case, above, administrative, alberta, appellate, authority, cannot`
- Display key terms: `case, above, administrative, alberta, appellate, authority, cannot`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: case, above, administrative, alberta, appellate, authority, cannot Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5092126` offsets `670-678`; context: Its role is that stated at the outset of section 110 of the Act: an appeal on a question of law, of fact or of mixed law and fact.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092126` offsets `431-439`; context: In this case, the RAD does not rehear the evidence that was before the RPD (moreover, it is prohibited by the Act) and, without clear indication, it also cannot duplicate the judicial review function.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5092126` offsets `543-549`; context: In this case, the RAD does not rehear the evidence that was before the RPD (moreover, it is prohibited by the Act) and, without clear indication, it also cannot duplicate the judicial review function.

#### 23256:3:subtheme:4 · paragraphs 27-28

- Raw key terms: `case, decision, legislative, scheme, activities, alberta, appeal, appellate`
- Display key terms: `case, legislative, scheme, activities, alberta, appellate`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: case, legislative, scheme, activities, alberta, appellate Application context: That case law is of only very relative relevance because the legislative schemes are so different. | That decision by the Quebec Court of Appeal will therefore be of greater interest in resolving this matter. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5092128` offsets `94-102`; context: The respective role of the reviewing and reviewed tribunal is first and foremost a question of statutory interpretation.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092128` offsets `547-555`; context: In fact, the de novo hearing by the reviewing tribunal involved in that decision consisted in a completely new hearing, with new evidence and new participants.
- Evidence: `reasoning_application` cue `because` at chunk `5092128` offsets `627-634`; context: That case law is of only very relative relevance because the legislative schemes are so different.
- Evidence: `reasoning_application` cue `therefore` at chunk `5092129` offsets `226-235`; context: That decision by the Quebec Court of Appeal will therefore be of greater interest in resolving this matter.

#### 23256:3:subtheme:5 · paragraphs 29-31

- Raw key terms: `appeal, court, review, appellate, applications, barreau, case, committee`
- Display key terms: `review, appellate, applications, barreau, case, committee`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: review, appellate, applications, barreau, case, committee Rule/authority context: [28] In Parizeau, after a remarkable examination of the Quebec case law and the jurisprudence of the Supreme Court of Canada, the Court of Appeal decided that the legislative scheme at issue in that case created a true a Application context: [47] To identify the standard that applies to the Professions Tribunal that examined the decision of the Applications Committee, one must first determine the jurisdictional function of the Professions Tribunal in a matte Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092130` offsets `185-190`; context: [28] In Parizeau, after a remarkable examination of the Quebec case law and the jurisprudence of the Supreme Court of Canada, the Court of Appeal decided that the legislative scheme at issue in that case created a true appeal and not a proceeding consisting of a quasi-judicial review.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5092130` offsets `80-93`; context: [28] In Parizeau, after a remarkable examination of the Quebec case law and the jurisprudence of the Supreme Court of Canada, the Court of Appeal decided that the legislative scheme at issue in that case created a true appeal and not a proceeding consisting of a quasi-judicial review.
- Evidence: `reasoning_application` cue `applies` at chunk `5092132` offsets `35-42`; context: [47] To identify the standard that applies to the Professions Tribunal that examined the decision of the Applications Committee, one must first determine the jurisdictional function of the Professions Tribunal in a matter such as this.
- Evidence: `counterargument_limitation` cue `However` at chunk `5092132` offsets `386-393`; context: However, is that an appellate function in the proper sense to which the usual standards in similar cases must apply (that is: the standard of correctness to questions of law and the palpable and overriding error standard to questions of fact or questions of mixed fact and law)?

#### 23256:3:subtheme:6 · paragraphs 32-36

- Raw key terms: `appeal, legislative, professions, tribunal, court, function, intervention, jurisdiction`
- Display key terms: `legislative, professions, function, intervention, jurisdiction`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: legislative, professions, function, intervention, jurisdiction Position/evidence statements: The legislature did not restrict the appellate function given to the Professions Tribunal and, in matters of discipline and in matters of admission and readmission, it conferred on it the broadest power of intervention,  Rule/authority context: Therefore, both in Quebec law and federal law, the wording of the provision creating the proceeding must be carefully examined to know which decision of which authorities are subject to an appeal, on what grounds the app Application context: The use of the term “appeal”, both in the Act respecting the Barreau du Québec and the Professional Code, while not decisive, seems telling, especially in the context described by authors Pierre Issalys and Denis Lemieux | It seems to have taken particular note of the power of intervention given to the Professions Tribunal to conclude that there was appellate jurisdiction: [translation] Evidence spans paragraphs 32-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5092133` offsets `2702-2709`; context: Therefore, both in Quebec law and federal law, the wording of the provision creating the proceeding must be carefully examined to know which decision of which authorities are subject to an appeal, on what grounds the appeal may be founded, under what conditions—namely the time limit—it may be introduced, whether it suspends the application of the decision at issue, and what powers the administrative tribunal has with respect to receiving evidence and with respect to the content of its decision.
- Evidence: `evidence_fact` cue `record` at chunk `5092133` offsets `1661-1667`; context: • It is directed at the decision of the lower body, on the basis of the facts established before it and the applicable law: the appeal reopens the debate on the basis of the record as it was constituted at the time of the initial decision.
- Evidence: `governing_rule` cue `under` at chunk `5092133` offsets `2636-2641`; context: Therefore, both in Quebec law and federal law, the wording of the provision creating the proceeding must be carefully examined to know which decision of which authorities are subject to an appeal, on what grounds the appeal may be founded, under what conditions—namely the time limit—it may be introduced, whether it suspends the application of the decision at issue, and what powers the administrative tribunal has with respect to receiving evidence and with respect to the content of its decision.
- Evidence: `reasoning_application` cue `therefore` at chunk `5092133` offsets `632-641`; context: The use of the term “appeal”, both in the Act respecting the Barreau du Québec and the Professional Code, while not decisive, seems telling, especially in the context described by authors Pierre Issalys and Denis Lemieux:
[translation]
The scope of the intervention of the administrative tribunal and consequently the extent of its jurisdiction are therefore determined by the wording in the legislative provisions that create the proceeding before the tribunal.
- Evidence: `counterargument_limitation` cue `however` at chunk `5092133` offsets `1919-1926`; context: Fairly often, however, the jurisdiction of the administrative tribunal will be structured or interpreted in a manner that departs from that reference model.
- Evidence: `evidence_fact` cue `found that` at chunk `5092134` offsets `56-66`; context: [30] In examining these indicators, the Court of Appeal found that there was appellate jurisdiction.
- Evidence: `reasoning_application` cue `conclude` at chunk `5092134` offsets `206-214`; context: It seems to have taken particular note of the power of intervention given to the Professions Tribunal to conclude that there was appellate jurisdiction:
[translation]
- Evidence: `party_position` cue `submitted` at chunk `5092135` offsets `649-658`; context: The legislature did not restrict the appellate function given to the Professions Tribunal and, in matters of discipline and in matters of admission and readmission, it conferred on it the broadest power of intervention, which is to “confirm, alter or quash any decision submitted to it and render the decision which it considers should have been rendered in first instance” (sections 175 and 182.
- Evidence: `reasoning_application` cue `applies` at chunk `5092136` offsets `629-636`; context: The analysis carried out by the Court of Appeal applies to sections 110 and 111 of the Act.

#### 23256:3:subtheme:7 · paragraphs 37-40

- Raw key terms: `cette, cision, committee, fugi, pour, refugee, section, appeal`
- Display key terms: `cette, cision, committee, fugi, pour, refugee, section`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: cette, cision, committee, fugi, pour, refugee, section Rule/authority context: However, in addition the divisions will ensure consistency in refugee decision-making by developing coherent national jurisprudence in refugee law issues. Application context: But as I’ve already indicated, we think we will have a better-quality decision-because we’ll have had two goes, two kicks, at the can. | It’s gone through some growth, not only because of the volume but also because of the demands made on it. Evidence spans paragraphs 37-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5092138` offsets `795-801`; context: However, in addition the divisions will ensure consistency in refugee decision-making by developing coherent national jurisprudence in refugee law issues.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5092138` offsets `766-779`; context: However, in addition the divisions will ensure consistency in refugee decision-making by developing coherent national jurisprudence in refugee law issues.
- Evidence: `reasoning_application` cue `because` at chunk `5092138` offsets `1974-1981`; context: But as I’ve already indicated, we think we will have a better-quality decision-because we’ll have had two goes, two kicks, at the can.
- Evidence: `issue` cue `issues` at chunk `5092139` offsets `422-428`; context: It is a full review on issues of fact, issues of law, issues of fact and law.
- Evidence: `counterargument_limitation` cue `but` at chunk `5092139` offsets `2330-2333`; context: The refugee appeal division will have experienced refugee decision makers providing access to appeal for not only every negative claim, but also for the minister where she is unhappy with any of the positive decisions.
- Evidence: `reasoning_application` cue `because` at chunk `5092140` offsets `918-925`; context: It’s gone through some growth, not only because of the volume but also because of the demands made on it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092141` offsets `566-574`; context: Unlike the appeal process proposed in the past and the one dormant in our current legislation, this refugee appeal division, or RAD, would allow for the introduction of new evidence and, in certain circumstances, provide for an oral hearing.

#### 23256:3:subtheme:8 · paragraphs 41-46

- Raw key terms: `appeal, appeals, court, decision, review, tribunal, above, fact`
- Display key terms: `appeals, review, above, fact`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: appeals, review, above, fact Rule/authority context: (6 mars 2012) What we are proposing in C-31 goes above and beyond our legal and humanitarian obligations under both the Charter of Rights and Freedoms and the UN convention on refugees. | [81] The Supreme Court and this Court have repeatedly indicated the following: the appeal tribunal may in principle rectify any error in law in the decision under appeal or any palpable and overriding error in the determ Application context: [40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (paragraph 37). Operative outcome context: In the event that a negative RPD decision is upheld on appeal, appellants would have the right to seek leave for judicial review of the appeal decision from the Federal Court. Evidence spans paragraphs 41-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5092142` offsets `315-323`; context: [36] The Immigration and Refugee Board Chairperson, Brian Goodman, stated the following on May 6, 2010, before the House Committee:
If a refugee claim is rejected by the RPD, all claimants except those from places or classes of nationals designated by the minister would have a right of appeal on the merits on all question to the IRB’s new refugee appeal division, RAD, staffed by Governor in Council appointees.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092142` offsets `440-448`; context: The RAD would receive new evidence and, in certain circumstances, would hold an oral hearing.
- Evidence: `disposition` cue `upheld` at chunk `5092142` offsets `553-559`; context: In the event that a negative RPD decision is upheld on appeal, appellants would have the right to seek leave for judicial review of the appeal decision from the Federal Court.
- Evidence: `governing_rule` cue `under` at chunk `5092143` offsets `1209-1214`; context: (6 mars 2012)
What we are proposing in C-31 goes above and beyond our legal and humanitarian obligations under both the Charter of Rights and Freedoms and the UN convention on refugees.
- Evidence: `governing_rule` cue `under` at chunk `5092146` offsets `157-162`; context: [81] The Supreme Court and this Court have repeatedly indicated the following: the appeal tribunal may in principle rectify any error in law in the decision under appeal or any palpable and overriding error in the determination of the facts or in the application of the law (if it was correctly identified) to the facts.
- Evidence: `reasoning_application` cue `apply` at chunk `5092147` offsets `78-83`; context: [40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (paragraph 37).

#### 23256:3:subtheme:9 · paragraphs 47-48

- Raw key terms: `appeal, novo, appellate, black, cannot, cases, certain, clear`
- Display key terms: `novo, appellate, black, cannot, cases, certain, clear`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: novo, appellate, black, cannot, cases, certain, clear Rule/authority context: [42] With respect, in the statutory scheme under review, I cannot find any indicators providing for an appeal de novo. Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5092148` offsets `19-24`; context: [41] The remaining issue is the nature of the appeal.
- Evidence: `evidence_fact` cue `record` at chunk `5092148` offsets `222-228`; context: An Appeal in which the appellate court uses the trial court’s record but reviews the evidence and law without deference to the trial court’s rulings.
- Evidence: `governing_rule` cue `under` at chunk `5092149` offsets `43-48`; context: [42] With respect, in the statutory scheme under review, I cannot find any indicators providing for an appeal de novo.

#### 23256:3:subtheme:10 · paragraphs 49-52

- Raw key terms: `review, appeal, canada, judicial, appeals, courts, entitled, evidence`
- Display key terms: `review, judicial, appeals, courts, entitled`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: review, judicial, appeals, courts, entitled Rule/authority context: [43] Instead, the scheme under review addresses appeals on specific questions, be it of fact, of law or of mixed law and fact (subsection 110(1)). | [45] Finally, the remedies that may be imposed (section 111 of the Act) appear to fall more under appeals than judicial review or quasi-judicial review (section 52 of the Federal Courts Act). Application context: A due diligence test applies to determine whether the party should have reasonably discovered, before the trial, the fact that it is claiming to be new. | The same is true for criminal matters (see Palmer v The Queen, [1980] 1 SCR 759, applied more recently in R v JAA, 2011 SCC 17, [2011] 1 SCR 628). Evidence spans paragraphs 49-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5092150` offsets `1070-1077`; context: A due diligence test applies to determine whether the party should have reasonably discovered, before the trial, the fact that it is claiming to be new.
- Evidence: `evidence_fact` cue `record` at chunk `5092150` offsets `280-286`; context: It will be on the basis of the record of proceedings before the RPD that the appeal will be heard based on the questions identified and raised, subject to the documentary evidence (subsection 110(3)) or evidence that is consistent with subsection 110(4).
- Evidence: `governing_rule` cue `under` at chunk `5092150` offsets `25-30`; context: [43] Instead, the scheme under review addresses appeals on specific questions, be it of fact, of law or of mixed law and fact (subsection 110(1)).
- Evidence: `reasoning_application` cue `applies` at chunk `5092150` offsets `1049-1056`; context: A due diligence test applies to determine whether the party should have reasonably discovered, before the trial, the fact that it is claiming to be new.
- Evidence: `issue` cue `issue` at chunk `5092151` offsets `669-674`; context: One might even think that the existence of an opportunity to present new evidence helps to confirm that the appeal at issue here must be treated like an appeal, purely and simply.
- Evidence: `evidence_fact` cue `evidence` at chunk `5092151` offsets `46-54`; context: [44] There is nothing unusual in allowing new evidence on appeal.
- Evidence: `reasoning_application` cue `applied` at chunk `5092151` offsets `257-264`; context: The same is true for criminal matters (see Palmer v The Queen, [1980] 1 SCR 759, applied more recently in R v JAA, 2011 SCC 17, [2011] 1 SCR 628).
- Evidence: `governing_rule` cue `under` at chunk `5092152` offsets `92-97`; context: [45] Finally, the remedies that may be imposed (section 111 of the Act) appear to fall more under appeals than judicial review or quasi-judicial review (section 52 of the Federal Courts Act).
- Evidence: `governing_rule` cue `under` at chunk `5092153` offsets `398-403`; context: Conclusion [47] In this case, the applicant did not have the appeal to which she is entitled under the Act since the RAD chose to apply a reasonableness standard of review corresponding to an application for judicial review.
- Evidence: `reasoning_application` cue `Because` at chunk `5092153` offsets `5-12`; context: [46] Because the recourse described in the Act is an appeal, as it moreover is identified in the Act, the appellate standards will be those of “correctness and palpable and overriding error” (Agraira v Canada (Public Safety and Emergency Preparedness), 2013 SCC 36, [2013] 2 SCR 559, at paragraph 45).

#### 23256:3:subtheme:11 · paragraphs 53-54

- Raw key terms: `above, adjudges, agreed, agreement, allowed, allowing, anderson, appeal`
- Display key terms: `above, adjudges, agreed, agreement, allowed, allowing, anderson`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: above, adjudges, agreed, agreement, allowed, allowing, anderson Rule/authority context: [48] The parties are in agreement, and the Court concedes, that this is the type of case where there could very well be a “serious question of general importance” allowing an appeal to the Federal Court of Appeal under p Operative outcome context: Given that a question is supposed to be certified in Huruglica, above, it was agreed that the parties in this case would be allowed to study these reasons and the question to be certified in that case. Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5092154` offsets `131-139`; context: [48] The parties are in agreement, and the Court concedes, that this is the type of case where there could very well be a “serious question of general importance” allowing an appeal to the Federal Court of Appeal under paragraph 74(d) of the Act.
- Evidence: `governing_rule` cue `under` at chunk `5092154` offsets `213-218`; context: [48] The parties are in agreement, and the Court concedes, that this is the type of case where there could very well be a “serious question of general importance” allowing an appeal to the Federal Court of Appeal under paragraph 74(d) of the Act.
- Evidence: `disposition` cue `allowed` at chunk `5092154` offsets `371-378`; context: Given that a question is supposed to be certified in Huruglica, above, it was agreed that the parties in this case would be allowed to study these reasons and the question to be certified in that case.

#### Section text

[16] In a situation where documentary evidence is presented on appeal (subsection 110(3)), a hearing may be held if it raises a serious issue with respect to credibility (in addition to the fact that the documentary evidence is central to the decision and would justify allowing or rejecting the refugee protection claim: subsection 110(6)).

[17] An important feature of the statutory scheme put in place is the directive given by Parliament regarding decisions that may be rendered by the RAD. I reproduce section 111 of the Act as follows:
Decision
Décision
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
(1.1) [Repealed, 2012, c. 17, s. 37]
(1.1) [Abrogé, 2012, ch. 17, art. 37]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.

[18] As can be seen, the RAD confirms or substitutes the determination that, in its opinion, should have been made. It can refer the matter back to the RPD only in specific circumstances, that is, when the decision is erroneous and when the decision cannot be confirmed or substituted by the RAD without holding a new hearing to reassess the evidence before the RPD. It is only in such a case that the matter may be referred back.

[19] For now, two observations should be noted. First, the Act is clear that the RAD may only consider a new hearing in specific circumstances. Those circumstances do not include rehearing the evidence already before the RPD. If the RAD cannot dispose of the appeal by confirming the RPD determination or by substituting the determination that, in its opinion, should have been made, but the determination is erroneous, the matter may be referred back because a reassessment of the evidence is required. With respect, I cannot see how such a legislative scheme could easily accommodate a standard of review in which deference prevails.

[20] The second observation is that the legislative scheme, viewed as a whole, does not at all suggest deference within the meaning of the reasonableness standard. To the contrary, the Act instructs the RAD to examine the record of proceedings before the RPD while admitting additional evidence, in the prescribed circumstances. The English version of subsection 111(1) specifically states “[a]fter considering the appeal” before stating the possible outcomes for the RAD. There is no question of owing deference: the determination is confirmed or a new determination is substituted. If there was an error of fact or law, or mixed fact and law, but the RAD cannot confirm or substitute its determination without a new hearing to reassess the evidence before the RPD, the matter is referred back. I fail to see where deference, arising from the reasonableness standard, fits into that scheme considered as a whole.

[21] It also seems that the problem results from a blurring of lines. Judicial review, with its inherent deference, stems from a very different logic than an appeal, which also explains why decisions that have been deemed unreasonable are referred back to the administrative tribunal rather than substituted with a determination.

[22] Judicial review exists to ensure the legality of decisions made by the government, to enforce the rule of law. The concept is eloquently stated in Dunsmuir, above.

[23] Therefore, it is not difficult to accept that the standard of reasonableness prevails in administrative matters because review is not as much about appropriateness as it is about legality: because there is more than one possible reasonable result and administrative tribunals have special expertise, superior courts will intervene only in situations where the decision is unreasonable. Moreover, an unreasonable decision cannot be lawful, thus requiring judicial review. Once again, Dunsmuir is informative:

[42] Moreover, even if one could conceive of a situation in which a clearly or highly irrational decision were distinguishable from a merely irrational decision, it would be unpalatable to require parties to accept an irrational decision simply because, on a deferential standard, the irrationality of the decision is not clear enough. It is also inconsistent with the rule of law to retain an irrational decision.

[24] That cannot be said for appeals, which are the exclusive creation of Parliament. As I have tried to explain, the legislative scheme does not give any indication that deference was considered by Parliament. Rather, we are dealing with a scheme where if there is, for example, an error of fact, the matter must be referred back to the RPD if a reassessment of the evidence before the RPD is required for a determination. There is no place for deference in such a scheme. I share the opinion of Justice Phelan that “if the RAD simply reviews RPD decisions for reasonableness, then its appellate role is curtailed” (Huruglica, above, paragraph 39). I add that the legislative scheme gives no indication that the bar must be so high.

[25] That said, with respect, I also share the view of Justice Phelan that the creation of an appellate level between an administrative jurisdiction and judicial review would suggest that Parliament wanted to create something different between those two levels. The RAD is not the authority that hears the matter and it is also not the authority that reviews the legality of the decision. In this case, the RAD does not rehear the evidence that was before the RPD (moreover, it is prohibited by the Act) and, without clear indication, it also cannot duplicate the judicial review function. Its role is that stated at the outset of section 110 of the Act: an appeal on a question of law, of fact or of mixed law and fact. The Act then even states the record of proceedings on which the RAD must rely. It also sets out the decisions that may be rendered.

[26] The RAD relied to a very great extent on Newton, above. The legislative scheme that had to be examined in Newton was not in any way related to the legislative scheme in this case. Furthermore, the Alberta Court of Appeal had the foresight to note the following:

[57] . . . The respective role of the reviewing and reviewed tribunal is first and foremost a question of statutory interpretation. It involves determining what function the Legislature intended the initial tribunal to perform, and what type of supervisory role is intended for the appellate tribunal.
The decision in Newton is a function of the very specific scheme in force regarding policing activities in Alberta. In fact, the de novo hearing by the reviewing tribunal involved in that decision consisted in a completely new hearing, with new evidence and new participants. That case law is of only very relative relevance because the legislative schemes are so different.

[27] The legislative scheme examined in Parizeau c Barreau du Québec, 2011 QCCA 1498, [2011] RJQ 1506 (Parizeau) is more closely related to the legislative scheme in this case. That decision by the Quebec Court of Appeal will therefore be of greater interest in resolving this matter.

[28] In Parizeau, after a remarkable examination of the Quebec case law and the jurisprudence of the Supreme Court of Canada, the Court of Appeal decided that the legislative scheme at issue in that case created a true appeal and not a proceeding consisting of a quasi-judicial review. In that case, it was the Professions Tribunal that had been given appellate jurisdiction concerning the Barreau du Québec’s Applications Committee, which had to rule on Ms. Parizeau’s reinstatement on the Roll of the Order of Advocates.

[29] The Court of Appeal concluded that the indicators from the review of the enabling legislation led to the finding that it was a true appeal. In my opinion, that is also the case for the RAD. Paragraphs 47 and 48 of the decision express this clearly.
[translation]

[47] To identify the standard that applies to the Professions Tribunal that examined the decision of the Applications Committee, one must first determine the jurisdictional function of the Professions Tribunal in a matter such as this. An Act respecting the Barreau du Québec and the Professional Code speak of an appeal of Applications Committee decisions to the Professions Tribunal. However, is that an appellate function in the proper sense to which the usual standards in similar cases must apply (that is: the standard of correctness to questions of law and the palpable and overriding error standard to questions of fact or questions of mixed fact and law)? Or is it, despite the term used in the Act, a more limited function like the one exercised by a court on judicial review that would command the application of similar standards, as redefined by the Supreme Court in Dunsmuir?

[48] A reading of the provisions reproduced above indicates, at least at first glance, that the legislator provided for a right of appeal and gave the Professions Tribunal—an administrative (or quasi‑judicial, if you prefer) tribunal—powers ordinarily associated with that function. The use of the term “appeal”, both in the Act respecting the Barreau du Québec and the Professional Code, while not decisive, seems telling, especially in the context described by authors Pierre Issalys and Denis Lemieux:
[translation]
The scope of the intervention of the administrative tribunal and consequently the extent of its jurisdiction are therefore determined by the wording in the legislative provisions that create the proceeding before the tribunal. In federal law, they very often create a right to an “appeal” before the tribunal, without any other details. Such a proceeding thus presents, in principle, five characteristics:
• It involves challenging a decision rendered by a body that is lower than the review body, by either party to the proceeding that led to that decision: those who had the right to participate in arriving at the initial decision have a right of appeal.
• It is brought before a higher body, completely separate from the one that rendered the impugned decision: the appeal body must be an impartial third party and have a higher-level authority.
• It must be brought within a set time frame: the existence of a right of appeal must not jeopardize legal certainty.
• It is directed at the decision of the lower body, on the basis of the facts established before it and the applicable law: the appeal reopens the debate on the basis of the record as it was constituted at the time of the initial decision.
• It includes the opportunity for the higher body to completely substitute its determination for that of the lower body: the appeal allows for a new determination of the matter.
Fairly often, however, the jurisdiction of the administrative tribunal will be structured or interpreted in a manner that departs from that reference model.
In Quebec law, since the adoption of An Act respecting administrative justice, the legislature systematically uses the word “proceeding” instead of “appeal” when conferring jurisdiction on an administrative tribunal. The legislature also reserves the right to specify the scope of jurisdiction in legislation conferring jurisdiction.
Therefore, both in Quebec law and federal law, the wording of the provision creating the proceeding must be carefully examined to know which decision of which authorities are subject to an appeal, on what grounds the appeal may be founded, under what conditions—namely the time limit—it may be introduced, whether it suspends the application of the decision at issue, and what powers the administrative tribunal has with respect to receiving evidence and with respect to the content of its decision.

[30] In examining these indicators, the Court of Appeal found that there was appellate jurisdiction. It seems to have taken particular note of the power of intervention given to the Professions Tribunal to conclude that there was appellate jurisdiction:
[translation]

[76] The legislature gives the Professions Tribunal, a specialized administrative tribunal, an appeal function with respect to committees’ decisions regarding discipline and admission or readmission to professional orders, according to the specific terms of the appeal. May we, in the absence of specific legislative guidance, transform this appeal into a quasi-judicial review? The legislature did not restrict the appellate function given to the Professions Tribunal and, in matters of discipline and in matters of admission and readmission, it conferred on it the broadest power of intervention, which is to “confirm, alter or quash any decision submitted to it and render the decision which it considers should have been rendered in first instance” (sections 175 and 182.6 of the Professional Code), wording with respect to which Justice Fish, in Pigeon v. Daigneault, stated the following: “[f]rom a statutory point of view, more sweeping powers of appellate intervention . . . are difficult to conceive.”
In the case at bar, not only does the Act provide for an appeal, which is already an important indication, but it also clearly states the decisions that must be made. In my opinion, that is determinative. That led the Court of Appeal to come to the conclusion that I share and that, in my opinion, is also consistent with the legislative scheme enacted in the Act:
[translation]

[78] All of this, and primarily respect for legislative intent, not to mention the protection of the litigants to whom recourse is available, weighs against treating appeals before the Professions Tribunal as a form of judicial review and also weighs against developing a policy of deference the effect of which would be to turn appeals before this tribunal into pseudo-judicial reviews. In our opinion, the Professions Tribunal does exercise an appeal function and jurisdiction.
In my view, the considerations raised by the Court of Appeal are in large part present in this case. The analysis carried out by the Court of Appeal applies to sections 110 and 111 of the Act.

[31] Furthermore, even though legislative debates have questionable weight in the interpretation of a statute (CN v Canada, above, at paragraph 47), it is impossible to ignore the discussions at the time when the RAD was created in 2001 and at the time of the amendments made to the legislative scheme in 2010 and 2012, even though the legislative provisions came into force finally on December 15, 2012.

[32] Those discussions, in my view, leave no place for an RAD jurisdiction that has the nature of a quasi-judicial review. Thus, in his appearance before the parliamentary committee of the House of Commons, Peter Showler, then Chairperson of the Immigration and Refugee Board, testified on Bill C-11, which became the Immigration and Refugee Protection Act, SC, 2001, c 27, regarding the RAD’s jurisdiction:
It is expected that the RAD will produce two different but complementary results. By reviewing individual RPD decisions on the merits, the RAD can efficiently remedy errors made by the RPD. That, if you will, is the safety net for the RPD. However, in addition the divisions will ensure consistency in refugee decision-making by developing coherent national jurisprudence in refugee law issues. As I said to this committee before, we don’t see that as a benefit simply in that it will improve the quality of our decision-making. If there is more coherent, consistent jurisprudence, we think RPD decision-makers can actually make their decisions more quickly as well.
Nous croyons que la SAR obtiendra deux résultats différents, mais complémentaires. En examinant les décisions individuelles de la SPR sur le fond, la SAR pourra, de manière efficace, corriger les erreurs faites par la SPR. De plus, la Section assurer la cohérence dans le processus décisionnel grâce à la jurisprudence uniforme à l’échelle du pays que cette section établira sur les questions liées au droit des réfugiés. Comme je l’ai déjà dit devant votre comité, ce système n’aura pas selon nous pour seul avantage d’améliorer la qualité de nos décisions. Si la jurisprudence est plus cohérente et uniforme, les décideurs de la SPR pourront en fait également rendre leurs décisions plus rapidement.
. . .
[…]
So there’s a significant difference between them. We think the total result will end up the same as before. But as I’ve already indicated, we think we will have a better-quality decision-because we’ll have had two goes, two kicks, at the can. There’s not only been the original decision, but also a clear, authoritative, experienced review of that decision. (March 20, 2001)
Il y a donc une importante différence entre les deux. Nous pensons qu’en fin de compte le délai sera le même délai qu’auparavant. Mais comme je l’ai déjà dit, nous escomptons des décisions de meilleure qualité, parce que nous aurons bénéficié de deux essais. Il y aura en effet la décision originale, suivie d’une révision de cette décision par des personnes expérimentées et faisant autorité. (20 mars 2001)

[33] Mr. Showler spoke again on May 8, 2001, and October 1, 2001, before the Senate Standing Committee on Social Affairs, Science and Technology. He stated the following:
Let’s clarify that the Refugee Appeal Division has two quite separate objectives. The first we’ve already discussed: it’s the safety net, if you will, to catch the inevitable mistakes that are bound to occur at the first level. It is a full review on issues of fact, issues of law, issues of fact and law. In that sense, it’s very different from the present judicial review process. It will be able to look substantively at the decisions, and if the RAD has a different view of the facts of the case, it can either overturn the decision or confirm it.
J’aimerais préciser tout d’abord que la Section d’appel des réfugiés vise deux objectifs bien distincts. Nous avons déjà parlé du premier: il s’agit du filet de sécurité, si vous voulez, pour attraper les erreurs inévitables qui se produiront sûrement en première instance. On procède à un examen complet des questions de fait, des questions de droit, des questions de fait et de droit. En ce sens, c’est une méthode très différente de celle du processus judiciaire actuel. On pourra procéder à une étude de fond des décisions, et si la SAR interprète les faits différemment, elle peut renverser la décision ou la confirmer.
I hope you’re aware that ordinarily, judicial review is very limited. It’s really only a review if there’s been an error of law. The judicial review process decision does not replace that of the first-level decision makers. The Refugee Appeal Division performs a far more substantive review. (May 8, 2001)
J’espère que vous savez que, ordinairem

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23256:4 · paragraphs 55-55

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b2278d48219d714d9c88bf8c5882a4ca77983e090a64a3e25919bde4513dbfca`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23256:4:subtheme:1 · paragraphs 55-55

- Raw key terms: `appearances, applicant, associ, attorney, canada, counsel, dated, deputy`
- Display key terms: `associ, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associ, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 55-55. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
ROY J.
DATED:
September 23, 2014
APPEARANCES:
Eric Taillefer
FOR THE APPLICANT
Evangelos Liosis
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Handfield & Associés
Counsel
Montréal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
