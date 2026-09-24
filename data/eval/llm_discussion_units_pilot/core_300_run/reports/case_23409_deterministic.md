# Discussion Units: case 23409

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **77**
- Continuity pairs: **76**
- Discussion Units: **5**
- Paragraph source hashes: **77**
- Sub-themes: **26**

## 23409:1 · paragraphs 0-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ce1a7c1a269173829f7199418bf9f7070ffbf9825790e4075b1a54fc79dc57a6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23409:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, canada, decision, immigration, court, october, protection, reasons`
- Display key terms: `october, protection`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: october, protection Rule/authority context: On October 2, 2013, the RPD determined that the applicant is neither a Convention “refugee” or a “person in need of protection”, under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA Application context: The fear of the applicant, who is a Sunni, is based on the fact that he risks being forced to join an army accused of participating in war crimes, that he is already perceived by the authorities as a political activist b Operative outcome context: For the reasons that follow, the application for judicial review is allowed by the Court. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `allowed` at chunk `5099974` offsets `327-334`; context: For the reasons that follow, the application for judicial review is allowed by the Court.
- Evidence: `evidence_fact` cue `determined that` at chunk `5099975` offsets `570-585`; context: On October 2, 2013, the RPD determined that the applicant is neither a Convention “refugee” or a “person in need of protection”, under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `governing_rule` cue `under` at chunk `5099975` offsets `671-676`; context: On October 2, 2013, the RPD determined that the applicant is neither a Convention “refugee” or a “person in need of protection”, under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `reasoning_application` cue `because` at chunk `5099975` offsets `383-390`; context: The fear of the applicant, who is a Sunni, is based on the fact that he risks being forced to join an army accused of participating in war crimes, that he is already perceived by the authorities as a political activist because of his fundraising activities for victims of the civil war and, finally, since his family is rich, that he risks being kidnapped or extorted in Syria.

#### 23409:1:subtheme:2 · paragraphs 4-5

- Raw key terms: `appeal, applicant, dismissed, found, judicial, member, para, paras`
- Display key terms: `dismissed, judicial, para, paras`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: dismissed, judicial, para, paras Rule/authority context: First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13). Application context: First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13). | In summary, the RPD could reasonably conclude that the risk of being enrolled in the Syrian army was speculative as long as the applicant continued to study in Canada (paras 19 to 23). Operative outcome context: Gallagher (member), dismissed the applicant’s appeal. | Therefore, the RAD dismissed the applicant’s appeal, hence this application for judicial review. Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5099977` offsets `210-216`; context: First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13).
- Evidence: `evidence_fact` cue `found that` at chunk `5099977` offsets `411-421`; context: Since these are questions of fact (the applicant’s credibility) or mixed fact and law (determination of a generalized risk), he found that the RPD’s decision must be reviewed using the standard of judicial review of reasonableness, as defined in Dunsmuir v New Brunswick, 2008 SCC 9 at para 47 (Dunsmuir) and Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 at para 95.
- Evidence: `governing_rule` cue `standard of review` at chunk `5099977` offsets `170-188`; context: First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13).
- Evidence: `reasoning_application` cue `applied` at chunk `5099977` offsets `199-206`; context: First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13).
- Evidence: `disposition` cue `dismissed` at chunk `5099977` offsets `107-116`; context: Gallagher (member), dismissed the applicant’s appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099978` offsets `87-95`; context: [5] Second, the member refused to hold an oral hearing, being of the view that the new evidence provided by the applicant is not determinative (paras 14 to 18).
- Evidence: `reasoning_application` cue `conclude` at chunk `5099978` offsets `291-299`; context: In summary, the RPD could reasonably conclude that the risk of being enrolled in the Syrian army was speculative as long as the applicant continued to study in Canada (paras 19 to 23).
- Evidence: `disposition` cue `dismissed` at chunk `5099978` offsets `656-665`; context: Therefore, the RAD dismissed the applicant’s appeal, hence this application for judicial review.

#### 23409:1:subtheme:3 · paragraphs 6-8

- Raw key terms: `appeal, conducted, para, review, scope, standard, according, apply`
- Display key terms: `conducted, para, review, scope, standard, according, apply`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: conducted, para, review, scope, standard, according, apply Position/evidence statements: [7] The respondent argues that the scope of the review conducted by the RAD on appeal arises from its expertise. Rule/authority context: This application for judicial review instead relates to the scope on appeal of the review of evidence in the RPD record that the RAD conducted under sections 110 and 111 of the IRPA. Application context: In this case, the member did not apply the appropriate mode of analysis. | In this case, the respondent alleges that the Court should apply the standard of reasonableness to the interpretation that the member made of the scope of the provisions in the IRPA, because although it is a question of  Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5099979` offsets `461-469`; context: According to the applicant, the interpretation of these provisions raises a question of law, which must be reviewed on a standard of correctness (Budhai v Canada (Attorney General), 2002 FCA 298 at para 22 and Canada (Attorney General) v Hunter, 2013 FCA 12 at para 4).
- Evidence: `evidence_fact` cue `evidence` at chunk `5099979` offsets `295-303`; context: This application for judicial review instead relates to the scope on appeal of the review of evidence in the RPD record that the RAD conducted under sections 110 and 111 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5099979` offsets `345-350`; context: This application for judicial review instead relates to the scope on appeal of the review of evidence in the RPD record that the RAD conducted under sections 110 and 111 of the IRPA.
- Evidence: `reasoning_application` cue `apply` at chunk `5099979` offsets `688-693`; context: In this case, the member did not apply the appropriate mode of analysis.
- Evidence: `issue` cue `question` at chunk `5099980` offsets `321-329`; context: In this case, the respondent alleges that the Court should apply the standard of reasonableness to the interpretation that the member made of the scope of the provisions in the IRPA, because although it is a question of law, it is not a question of law of “central importance to the legal system as a whole” (Dunsmuir, above at para 60; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at para 84 (Alberta Teachers’ Association)).
- Evidence: `party_position` cue `argues` at chunk `5099980` offsets `19-25`; context: [7] The respondent argues that the scope of the review conducted by the RAD on appeal arises from its expertise.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099980` offsets `694-702`; context: Indeed, nothing requires the RAD to reassess the evidence presented by a refugee claimant before the RPD, especially since the appeal on the record prepared by the RPD is not a de novo appeal.
- Evidence: `reasoning_application` cue `apply` at chunk `5099980` offsets `172-177`; context: In this case, the respondent alleges that the Court should apply the standard of reasonableness to the interpretation that the member made of the scope of the provisions in the IRPA, because although it is a question of law, it is not a question of law of “central importance to the legal system as a whole” (Dunsmuir, above at para 60; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at para 84 (Alberta Teachers’ Association)).
- Evidence: `counterargument_limitation` cue `although` at chunk `5099980` offsets `304-312`; context: In this case, the respondent alleges that the Court should apply the standard of reasonableness to the interpretation that the member made of the scope of the provisions in the IRPA, because although it is a question of law, it is not a question of law of “central importance to the legal system as a whole” (Dunsmuir, above at para 60; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at para 84 (Alberta Teachers’ Association)).
- Evidence: `reasoning_application` cue `applied` at chunk `5099981` offsets `98-105`; context: [8] According to settled law from this Court, it seems that the standard of correctness should be applied to the scope of the review conducted by the RAD on appeal (Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 20 (Iyamuremye); Garcia Alvarez v Canada (Citizenship and Immigration), 2014 FC 702 at para 17 (Garcia Alvarez); Eng v Canada (Citizenship and Immigration), 2014 FC 711 at para 18 (Eng); Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 at paras 24 to 34 (Huruglica)).

#### 23409:1:subtheme:4 · paragraphs 9-10

- Raw key terms: `appeal, canada, case, determinative, review, acceptable, adopted, believe`
- Display key terms: `case, determinative, review, acceptable, adopted, believe`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: case, determinative, review, acceptable, adopted, believe Application context: [10] It is sufficient to conclude today that the interpretation adopted by Member Gallagher is not an acceptable outcome in respect of the law, as the appeal before the RAD is simply not a judicial review, which is a rev Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5099982` offsets `263-268`; context: Other colleagues of the Court have ruled on this last issue.
- Evidence: `reasoning_application` cue `conclude` at chunk `5099983` offsets `25-33`; context: [10] It is sufficient to conclude today that the interpretation adopted by Member Gallagher is not an acceptable outcome in respect of the law, as the appeal before the RAD is simply not a judicial review, which is a reviewable error that is determinative in this case (Spasoja c Canada (Citoyenneté et Immigration), 2014 CF 913 at paras 3, 9, 11 and 47 (Spasoja)).

#### 23409:1:subtheme:5 · paragraphs 11-13

- Raw key terms: `appeal, decision, evidence, refugee, aside, cannot, claim, decisions`
- Display key terms: `refugee, aside, cannot, decisions`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: refugee, aside, cannot, decisions Position/evidence statements: After all, it was the RPD who heard the witnesses and assessed the probative value of documentary evidence submitted by the parties. Rule/authority context: … […] (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois : (a) the decision of the Refu Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5099984` offsets `193-201`; context: 1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099984` offsets `1950-1958`; context: …
[…]
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `governing_rule` cue `under` at chunk `5099984` offsets `1901-1906`; context: …
[…]
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5099984` offsets `1878-1884`; context: …
[…]
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `issue` cue `question` at chunk `5099985` offsets `207-215`; context: [12] Although it is clear on reading the above provisions that the RAD may set aside the RPD’s decision and substitute the decision that should have been made, it must be noted that this does not settle the question of the said [translation] “deference” that an appeal tribunal should or should not give to findings of fact, or mixed facts and law, by the court of first instance.
- Evidence: `party_position` cue `submitted` at chunk `5099985` offsets `488-497`; context: After all, it was the RPD who heard the witnesses and assessed the probative value of documentary evidence submitted by the parties.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099985` offsets `479-487`; context: After all, it was the RPD who heard the witnesses and assessed the probative value of documentary evidence submitted by the parties.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099986` offsets `386-394`; context: Further, the RAD may enter new evidence in an appeal and decide to hold an oral hearing in cases specified by Parliament (subsections 110(3) to (6) of the IRPA).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5099986` offsets `285-291`; context: For example, even if a country is not part of those that are excluded from an appeal, when the RPD refers in its decision to no credible basis for the refugee claim (subsection 107(2) of the IRPA), there cannot be an appeal before the RAD (paragraph 110(2)(c) of the IRPA).

#### 23409:1:subtheme:6 · paragraphs 14-17

- Raw key terms: `above, decision, deference, review, court, judicial, administrative, allows`
- Display key terms: `above, deference, review, judicial, administrative, allows`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: above, deference, review, judicial, administrative, allows Rule/authority context: These general principles of judicial review are not displaced by section 18. | [16] To date, with respect to the case law of the RAD and the Federal Court, on the scope of the review conducted on appeal by the RAD, three different approaches to deference owed to the RPD can be noted: (1) the standa Application context: The following warning again applies: judicial review is not an appeal and is conducted exclusively by superior courts. Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5099987` offsets `537-543`; context: However, if the text of the Act allows it, the courts will not interpret the grounds for review as standards of review and will have to show more or less deference, depending on the nature of the issues raised by the parties: Dunsmuir, above, and Canada (Citizenship and Immigration) v Khosa, [2009] 1 SCR 339, 2009 SCC 12 (Khosa).
- Evidence: `counterargument_limitation` cue `However` at chunk `5099987` offsets `341-348`; context: However, if the text of the Act allows it, the courts will not interpret the grounds for review as standards of review and will have to show more or less deference, depending on the nature of the issues raised by the parties: Dunsmuir, above, and Canada (Citizenship and Immigration) v Khosa, [2009] 1 SCR 339, 2009 SCC 12 (Khosa).
- Evidence: `issue` cue `whether` at chunk `5099988` offsets `332-339`; context: Some deference is also owed, regardless of whether the court has had the advantage of either receiving or not receiving a statutory direction, explicit or by necessary implication.
- Evidence: `governing_rule` cue `principles` at chunk `5099988` offsets `484-494`; context: These general principles of judicial review are not displaced by section 18.
- Evidence: `governing_rule` cue `standard of review` at chunk `5099989` offsets `477-495`; context: [16] To date, with respect to the case law of the RAD and the Federal Court, on the scope of the review conducted on appeal by the RAD, three different approaches to deference owed to the RPD can be noted: (1) the standard of judicial review, or “reasonableness” (decision of Member Gallagher and various other RAD decisions); (2) the standard of appellate review or of “palpable and overriding error” (Garcia Alvarez, Eng and Spasoja, above); and (3) a composite and variable standard of review resulting from the nature of the claim before the RAD—characterized as a “hybrid appeal”—and the particular nature of questions of fact, or of mixed fact and law, raised by an appellant (Huruglica, above).
- Evidence: `reasoning_application` cue `applies` at chunk `5099990` offsets `163-170`; context: The following warning again applies: judicial review is not an appeal and is conducted exclusively by superior courts.

#### 23409:1:subtheme:7 · paragraphs 18-22

- Raw key terms: `court, fact, findings, standard, canada, error, judge, review`
- Display key terms: `fact, findings, standard, error, judge, review`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: fact, findings, standard, error, judge, review Rule/authority context: It is also the standard of review applied by Member Gallagher in this file and by other members of the RAD up to now. | [19] Indeed, given that the appeal is not a new trial, it must be asked what is the standard of review applicable on appeals with respect to the trial judge’s findings. Application context: Further, this is the test that this Court applies to findings of fact, and mixed fact and law, of the RPD in cases where there was no appeal to the RAD (see for example Vitalis v Canada (Citizenship and Immigration), 201 | Therefore, in Housen, the Supreme Court of Canada clearly indicated that, in principle, it is not the role of appellate courts to second-guess the weight assigned by a trial judge to the various items of evidence and it  Evidence spans paragraphs 18-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5099991` offsets `244-251`; context: Its analysis will be concerned with the existence of justification, transparency and intelligibility within the decision-making process, and also with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law (Dunsmuir, above at para 47).
- Evidence: `governing_rule` cue `standard of review` at chunk `5099991` offsets `1293-1311`; context: It is also the standard of review applied by Member Gallagher in this file and by other members of the RAD up to now.
- Evidence: `reasoning_application` cue `applies` at chunk `5099991` offsets `934-941`; context: Further, this is the test that this Court applies to findings of fact, and mixed fact and law, of the RPD in cases where there was no appeal to the RAD (see for example Vitalis v Canada (Citizenship and Immigration), 2014 FC 723 at paras 3-4; Kotai v Canada (Citizenship and Immigration), 2013 FC 693 at para 10; Wei v Canada (Citizenship and Immigration), 2012 FC 854 at paras 39-41).
- Evidence: `counterargument_limitation` cue `but` at chunk `5099991` offsets `765-768`; context: This does not refer to a decision that another decision-maker with knowledge of the same facts and the applicable law may have made, but only to a “reasonable” decision—even if it is not the best decision in the circumstances and it opens itself to criticism.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099992` offsets `711-719`; context: Therefore, in Housen, the Supreme Court of Canada clearly indicated that, in principle, it is not the role of appellate courts to second-guess the weight assigned by a trial judge to the various items of evidence and it is only when the inference-drawing process itself is palpably in error that an appellate court can interfere with the trial judge’s finding of fact.
- Evidence: `governing_rule` cue `standard of review` at chunk `5099992` offsets `84-102`; context: [19] Indeed, given that the appeal is not a new trial, it must be asked what is the standard of review applicable on appeals with respect to the trial judge’s findings.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5099992` offsets `507-516`; context: Therefore, in Housen, the Supreme Court of Canada clearly indicated that, in principle, it is not the role of appellate courts to second-guess the weight assigned by a trial judge to the various items of evidence and it is only when the inference-drawing process itself is palpably in error that an appellate court can interfere with the trial judge’s finding of fact.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099993` offsets `472-480`; context: Justice Fish, writing for the majority, explained that the standard of palpable and overriding error applies to all the trial judge’s findings of fact, including those relating to credibility, the facts proven directly, the facts inferred and the overall assessment of the evidence.
- Evidence: `reasoning_application` cue `applies` at chunk `5099993` offsets `300-307`; context: Justice Fish, writing for the majority, explained that the standard of palpable and overriding error applies to all the trial judge’s findings of fact, including those relating to credibility, the facts proven directly, the facts inferred and the overall assessment of the evidence.
- Evidence: `governing_rule` cue `standard of review` at chunk `5099994` offsets `83-101`; context: [21] However, Justice Fish also raised reasonableness in the implementation of the standard of review:

#### 23409:1:subtheme:8 · paragraphs 23-23

- Raw key terms: `above, affected, appeal, appellate, because, characterized, clearly, course`
- Display key terms: `above, affected, appellate, because, characterized, clearly, course`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: above, affected, appellate, because, characterized, clearly, course Application context: … [A]s a matter of principle, it seems to me that unreasonable findings of fact—relating to credibility, to primary or inferred “evidential” facts, or to facts in issue—are reviewable on appeal because they are “palpably Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5099996` offsets `338-343`; context: …
[A]s a matter of principle, it seems to me that unreasonable findings of fact—relating to credibility, to primary or inferred “evidential” facts, or to facts in issue—are reviewable on appeal because they are “palpably” or “clearly” wrong.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099996` offsets `164-172`; context: [56] In my respectful view, the test is met as well where the trial judge’s findings of fact can properly be characterized as “unreasonable” or “unsupported by the evidence”.
- Evidence: `reasoning_application` cue `because` at chunk `5099996` offsets `369-376`; context: …
[A]s a matter of principle, it seems to me that unreasonable findings of fact—relating to credibility, to primary or inferred “evidential” facts, or to facts in issue—are reviewable on appeal because they are “palpably” or “clearly” wrong.
- Evidence: `counterargument_limitation` cue `however` at chunk `5099996` offsets `506-513`; context: I need hardly repeat, however, that appellate intervention will only be warranted where the court can explain why or in what respect the impugned finding is unreasonable or unsupported by the evidence.

#### Section text

Alyafi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-10-08
Neutral citation
2014 FC 952
File numbers
IMM-1091-14
Decision Content
Date: 20141008
Docket: IMM-1091-14
Citation: 2014 FC 952
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Toronto, Ontario, October 8, 2014
Present: The Honourable Mr. Justice Martineau
BETWEEN:
AGHIAD ALYAFI
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The applicant is challenging the legality of a decision of the Refugee Appeal Division (RAD) of the Immigration and Refugee Board (IRB) of Canada, which confirms a previous decision of the Refugee Protection Division (RPD) denying him refugee protection. For the reasons that follow, the application for judicial review is allowed by the Court.

[2] The applicant is a Syrian national. In 2010, he came to study in Canada. In 2013, with a temporary visa, valid until January 31, 2015, he made a refugee claim. The fear of the applicant, who is a Sunni, is based on the fact that he risks being forced to join an army accused of participating in war crimes, that he is already perceived by the authorities as a political activist because of his fundraising activities for victims of the civil war and, finally, since his family is rich, that he risks being kidnapped or extorted in Syria. On October 2, 2013, the RPD determined that the applicant is neither a Convention “refugee” or a “person in need of protection”, under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).

[3] The applicant appealed this decision to the RAD.

[4] On January 30, 2014, the sole RAD member designated to hear the matter, Stephen J. Gallagher (member), dismissed the applicant’s appeal. First, the member asked what standard of review should be applied to issues raised on appeal by the applicant (RAD decision, paras 11 to 13). Since these are questions of fact (the applicant’s credibility) or mixed fact and law (determination of a generalized risk), he found that the RPD’s decision must be reviewed using the standard of judicial review of reasonableness, as defined in Dunsmuir v New Brunswick, 2008 SCC 9 at para 47 (Dunsmuir) and Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 at para 95.

[5] Second, the member refused to hold an oral hearing, being of the view that the new evidence provided by the applicant is not determinative (paras 14 to 18). After which, he found that the RPD’s conclusions are, in all respects, reasonable (para 32). In summary, the RPD could reasonably conclude that the risk of being enrolled in the Syrian army was speculative as long as the applicant continued to study in Canada (paras 19 to 23). The RPD’s findings of lack of personalized risk (paras 24 and 25) and implausibility that the applicant is perceived as a political activist by the authorities (paras 26 to 34) are also reasonable. Therefore, the RAD dismissed the applicant’s appeal, hence this application for judicial review.

[6] Today, the applicant does not attack the member’s refusal to hold an oral hearing or the reasonableness of the conclusion on the speculative nature of the applicant’s enrollment in the Syrian army. This application for judicial review instead relates to the scope on appeal of the review of evidence in the RPD record that the RAD conducted under sections 110 and 111 of the IRPA. According to the applicant, the interpretation of these provisions raises a question of law, which must be reviewed on a standard of correctness (Budhai v Canada (Attorney General), 2002 FCA 298 at para 22 and Canada (Attorney General) v Hunter, 2013 FCA 12 at para 4). In this case, the member did not apply the appropriate mode of analysis. That is sufficient to set aside the RAD decision. Alternatively, the findings regarding generalized risk and implausibility are unreasonable.

[7] The respondent argues that the scope of the review conducted by the RAD on appeal arises from its expertise. In this case, the respondent alleges that the Court should apply the standard of reasonableness to the interpretation that the member made of the scope of the provisions in the IRPA, because although it is a question of law, it is not a question of law of “central importance to the legal system as a whole” (Dunsmuir, above at para 60; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at para 84 (Alberta Teachers’ Association)). Moreover, the member did not commit any reviewable error. Indeed, nothing requires the RAD to reassess the evidence presented by a refugee claimant before the RPD, especially since the appeal on the record prepared by the RPD is not a de novo appeal. In this case, both the standard of judicial review of reasonableness and the standard on appeal of palpable and overriding error lead to the same result, that the Court should not intervene.

[8] According to settled law from this Court, it seems that the standard of correctness should be applied to the scope of the review conducted by the RAD on appeal (Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 20 (Iyamuremye); Garcia Alvarez v Canada (Citizenship and Immigration), 2014 FC 702 at para 17 (Garcia Alvarez); Eng v Canada (Citizenship and Immigration), 2014 FC 711 at para 18 (Eng); Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 at paras 24 to 34 (Huruglica)).

[9] Nevertheless, I do not believe that the choice of the standard of correctness is determinative in this case, or that it is necessary to define the exact scope of the review conducted by the RAD on appeal. Other colleagues of the Court have ruled on this last issue. Serious questions of general importance regarding the RAD’s jurisdiction and the role on appeal were or are being certified in various matters, but it must be expected that it will take several months before the Federal Court of Appeal or even the Supreme Court of Canada makes a decision.

[10] It is sufficient to conclude today that the interpretation adopted by Member Gallagher is not an acceptable outcome in respect of the law, as the appeal before the RAD is simply not a judicial review, which is a reviewable error that is determinative in this case (Spasoja c Canada (Citoyenneté et Immigration), 2014 CF 913 at paras 3, 9, 11 and 47 (Spasoja)).

[11] Paragraphs 110(1) and 111(1) and (2) of the IRPA state:
110. (1) Subject to subsections (1.1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
110. (1) Sous réserve des paragraphes (1.1) et (2), la personne en cause et le ministre peuvent, conformément aux règles de la Commission, porter en appel — relativement à une question de droit, de fait ou mixte — auprès de la Section d’appel des réfugiés la décision de la Section de la protection des réfugiés accordant ou rejetant la demande d’asile.
…
[…]
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
…
[…]
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.

[12] Although it is clear on reading the above provisions that the RAD may set aside the RPD’s decision and substitute the decision that should have been made, it must be noted that this does not settle the question of the said [translation] “deference” that an appeal tribunal should or should not give to findings of fact, or mixed facts and law, by the court of first instance. After all, it was the RPD who heard the witnesses and assessed the probative value of documentary evidence submitted by the parties. Moreover, the RAD exercises a specialized jurisdiction on appeal at least equal to that of the RPD at trial. Otherwise, the creation of a specialized appeal tribunal for refugee determination would serve no purpose.

[13] Additionally, not all RPD decisions may be subject to an appeal to the RAD. For example, even if a country is not part of those that are excluded from an appeal, when the RPD refers in its decision to no credible basis for the refugee claim (subsection 107(2) of the IRPA), there cannot be an appeal before the RAD (paragraph 110(2)(c) of the IRPA). Further, the RAD may enter new evidence in an appeal and decide to hold an oral hearing in cases specified by Parliament (subsections 110(3) to (6) of the IRPA). In this last case, it can probably be argued that it is a kind of de novo appeal, a point that I do not have to rule on today.

[14] The very concept of “deference” originated in case law. When Parliament wants to limit the courts’ power of intervention, it will adopt so-called “privative” clauses. It could also provide that a decision may be set aside for one reason or another, as is the case at subsection 18.1(4) of the Federal Courts Act, RSC 1985, c F-7 (FCA). However, if the text of the Act allows it, the courts will not interpret the grounds for review as standards of review and will have to show more or less deference, depending on the nature of the issues raised by the parties: Dunsmuir, above, and Canada (Citizenship and Immigration) v Khosa, [2009] 1 SCR 339, 2009 SCC 12 (Khosa).

[15] As the Supreme Court of Canada has already decided, with or without a privative clause, a measure of deference is appropriate where a particular decision has been allocated to an administrative decision-maker in matters relating to its role, function and expertise (Dunsmuir, above). Some deference is also owed, regardless of whether the court has had the advantage of either receiving or not receiving a statutory direction, explicit or by necessary implication. These general principles of judicial review are not displaced by section 18.1 of the FCA, which deals essentially with grounds of review of administrative action, and not of standards of review (Khosa, above).

[16] To date, with respect to the case law of the RAD and the Federal Court, on the scope of the review conducted on appeal by the RAD, three different approaches to deference owed to the RPD can be noted: (1) the standard of judicial review, or “reasonableness” (decision of Member Gallagher and various other RAD decisions); (2) the standard of appellate review or of “palpable and overriding error” (Garcia Alvarez, Eng and Spasoja, above); and (3) a composite and variable standard of review resulting from the nature of the claim before the RAD—characterized as a “hybrid appeal”—and the particular nature of questions of fact, or of mixed fact and law, raised by an appellant (Huruglica, above).

[17] Let us consider the first approach. Deference given to findings of fact or mixed fact and law by a reviewing Court is well known. The following warning again applies: judicial review is not an appeal and is conducted exclusively by superior courts. It is, above all, a review of the lawfulness of the administrative tribunal’s decision, whereas the appeal relates to the merit and opportunity to make a different decision from that of the tribunal of first instance. Characterizing a decision as “unreasonable”, thus allows a court of law, in the absence of a statutory appeal, to ensure that administrative tribunal respects the law and that a palpable injustice will not be committed, so that the legal remedy is to return the matter to the administrative decision-maker and not to make the decision that should have been made.

[18] The role of a reviewing court is by definition limited. It is well settled by case law. Its analysis will be concerned with the existence of justification, transparency and intelligibility within the decision-making process, and also with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law (Dunsmuir, above at para 47). It even goes so far as affording great deference to the interpretation that the administrative tribunal may make of its home statute when it does not concern jurisdiction or a question of law of central importance for the system. This does not refer to a decision that another decision-maker with knowledge of the same facts and the applicable law may have made, but only to a “reasonable” decision—even if it is not the best decision in the circumstances and it opens itself to criticism. Further, this is the test that this Court applies to findings of fact, and mixed fact and law, of the RPD in cases where there was no appeal to the RAD (see for example Vitalis v Canada (Citizenship and Immigration), 2014 FC 723 at paras 3-4; Kotai v Canada (Citizenship and Immigration), 2013 FC 693 at para 10; Wei v Canada (Citizenship and Immigration), 2012 FC 854 at paras 39-41). It is also the standard of review applied by Member Gallagher in this file and by other members of the RAD up to now. This first approach was rejected by the Court as we will see below, but before examining my colleagues’ decisions, let us examine the second approach, which is also applied throughout Canada by the general courts of appeal.

[19] Indeed, given that the appeal is not a new trial, it must be asked what is the standard of review applicable on appeals with respect to the trial judge’s findings. The standard of review applicable to pure questions of law is that of correctness, while following the standard of review applicable to findings of fact, these findings can only be overturned if it is established that the trial judge committed a palpable and overriding error: Housen v Nikolaisen, [2002] 2 SCR 235, 2002 SCC 33 (Housen). Therefore, in Housen, the Supreme Court of Canada clearly indicated that, in principle, it is not the role of appellate courts to second-guess the weight assigned by a trial judge to the various items of evidence and it is only when the inference-drawing process itself is palpably in error that an appellate court can interfere with the trial judge’s finding of fact. In passing, the same high degree of deference should apply to the trial judge’s assessment of the credibility of a witness and the other findings of fact (Housen, above at paras 23 and 24).

[20] More specific information as to the scope of the standard of palpable and overriding error was later provided by the Supreme Court of Canada in HL v Canada (Attorney General), 2005 SCC 25 (HL). Justice Fish, writing for the majority, explained that the standard of palpable and overriding error applies to all the trial judge’s findings of fact, including those relating to credibility, the facts proven directly, the facts inferred and the overall assessment of the evidence.

[21] However, Justice Fish also raised reasonableness in the implementation of the standard of review:

[55] … [A]n appellate court will not interfere with the trial judge’s findings of fact unless it can plainly identify the imputed error, and that error is shown to have affected the result.

[56] In my respectful view, the test is met as well where the trial judge’s findings of fact can properly be characterized as “unreasonable” or “unsupported by the evidence”. …
[A]s a matter of principle, it seems to me that unreasonable findings of fact—relating to credibility, to primary or inferred “evidential” facts, or to facts in issue—are reviewable on appeal because they are “palpably” or “clearly” wrong. The same is true of findings that are unsupported by the evidence. I need hardly repeat, however, that appellate intervention will only be warranted where the court can explain why or in what respect the impugned finding is unreasonable or unsupported by the evidence. And the reviewing court must of course be persuaded that the impugned factual finding is likely to have affected the result. (HL, above, at paras 55-56; emphasis in original).

## 23409:2 · paragraphs 24-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `06aace0f44f5900d0f77bafba2edaf08235f9c66e15685f78695668e87ea2ad6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23409:2:subtheme:1 · paragraphs 24-25

- Raw key terms: `cannot, court, determines, evidence, para, above, appeal, appellate`
- Display key terms: `cannot, determines, para, above, appellate`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: cannot, determines, para, above, appellate Application context: [23] “Palpable and overriding” error was also defined as follows by the Court of Appeal of Quebec in Parizeau c Barreau du Québec, 2011 QCCA 1498 at para 91 (Parizeau): [translation] Palpable and overriding error is an e Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5099997` offsets `194-201`; context: Appellate scrutiny determines whether inferences drawn by the judge are “reasonably supported by the evidence”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099997` offsets `265-273`; context: Appellate scrutiny determines whether inferences drawn by the judge are “reasonably supported by the evidence”.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5099997` offsets `309-315`; context: If they are, the reviewing court cannot reweigh the evidence by substituting, for the reasonable inference preferred by the trial judge, an equally—or even more—persuasive inference of its own (HL, above at para 74).
- Evidence: `evidence_fact` cue `evidence` at chunk `5099998` offsets `321-329`; context: [23] “Palpable and overriding” error was also defined as follows by the Court of Appeal of Quebec in Parizeau c Barreau du Québec, 2011 QCCA 1498 at para 91 (Parizeau):
[translation]
Palpable and overriding error is an error that, in its undeniability – and therefore not a difference of opinion on the assessment of the evidence – determines the outcome of the dispute in that the conclusion of the trier of fact, i.
- Evidence: `reasoning_application` cue `therefore` at chunk `5099998` offsets `258-267`; context: [23] “Palpable and overriding” error was also defined as follows by the Court of Appeal of Quebec in Parizeau c Barreau du Québec, 2011 QCCA 1498 at para 91 (Parizeau):
[translation]
Palpable and overriding error is an error that, in its undeniability – and therefore not a difference of opinion on the assessment of the evidence – determines the outcome of the dispute in that the conclusion of the trier of fact, i.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5099998` offsets `455-461`; context: the result of his or her decision, cannot hold, thus, ipso facto, making the decision unreasonable.

#### 23409:2:subtheme:2 · paragraphs 26-27

- Raw key terms: `appeal, court, error, palpable, according, basis, case, centre`
- Display key terms: `error, palpable, according, basis, case, centre`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: error, palpable, according, basis, case, centre Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5099999` offsets `281-286`; context: [24] The Court of Appeal of Quebec had previously provided the following explanations in Regroupement des CHSLD Christ-Roy (Centre hospitalier, soins longue durée) c Comité provincial des malades, 2007 QCCA 1068 at para 55:
[translation]
An error in the determination of a fact in issue is only palpable if its immediacy or obviousness is clearly identified in the reassessment of the relevant part of the evidence and a different finding on this fact in issue ought to be mafa necessary basis in fact, thereby leading to a false operative part of the trial decision and requiring the reworking of this part for that reason.
- Evidence: `evidence_fact` cue `evidence` at chunk `5099999` offsets `406-414`; context: [24] The Court of Appeal of Quebec had previously provided the following explanations in Regroupement des CHSLD Christ-Roy (Centre hospitalier, soins longue durée) c Comité provincial des malades, 2007 QCCA 1068 at para 55:
[translation]
An error in the determination of a fact in issue is only palpable if its immediacy or obviousness is clearly identified in the reassessment of the relevant part of the evidence and a different finding on this fact in issue ought to be mafa necessary basis in fact, thereby leading to a false operative part of the trial decision and requiring the reworking of this part for that reason.

#### 23409:2:subtheme:3 · paragraphs 28-28

- Raw key terms: `above, appeal, assessment, certain, consider, corresponds, decision, deference`
- Display key terms: `above, assessment, certain, consider, corresponds, deference`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: above, assessment, certain, consider, corresponds, deference Evidence spans paragraphs 28-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5100001` offsets `493-501`; context: It is also a question of “palpable and overriding error” (at paras 1 and 39).
- Evidence: `evidence_fact` cue `evidence` at chunk `5100001` offsets `247-255`; context: In this decision, Justice Shore indicated that the role of the RAD is not that of judicial review, but rather of appeal and that the RAD had to consider all the evidence and make its own assessment (at paras 30-38).
- Evidence: `counterargument_limitation` cue `but` at chunk `5100001` offsets `185-188`; context: In this decision, Justice Shore indicated that the role of the RAD is not that of judicial review, but rather of appeal and that the RAD had to consider all the evidence and make its own assessment (at paras 30-38).

#### Section text

[22] Justice Fish also noted that:
Not infrequently, different inferences may reasonably be drawn from facts found by the trial judge to have been directly proven. Appellate scrutiny determines whether inferences drawn by the judge are “reasonably supported by the evidence”. If they are, the reviewing court cannot reweigh the evidence by substituting, for the reasonable inference preferred by the trial judge, an equally—or even more—persuasive inference of its own (HL, above at para 74).

[23] “Palpable and overriding” error was also defined as follows by the Court of Appeal of Quebec in Parizeau c Barreau du Québec, 2011 QCCA 1498 at para 91 (Parizeau):
[translation]
Palpable and overriding error is an error that, in its undeniability – and therefore not a difference of opinion on the assessment of the evidence – determines the outcome of the dispute in that the conclusion of the trier of fact, i.e. the result of his or her decision, cannot hold, thus, ipso facto, making the decision unreasonable.

[24] The Court of Appeal of Quebec had previously provided the following explanations in Regroupement des CHSLD Christ-Roy (Centre hospitalier, soins longue durée) c Comité provincial des malades, 2007 QCCA 1068 at para 55:
[translation]
An error in the determination of a fact in issue is only palpable if its immediacy or obviousness is clearly identified in the reassessment of the relevant part of the evidence and a different finding on this fact in issue ought to be mafa necessary basis in fact, thereby leading to a false operative part of the trial decision and requiring the reworking of this part for that reason.

[25] According to my understanding, a palpable and overriding error is thus a clear and discernible error that has an important influence on the outcome of the dispute. I now come to the case law of this Court on the scope of the RAD review on appeal.

[26] The first decision on this topic was made on May 26, 2014, in Iyamuremye, above. In this decision, Justice Shore indicated that the role of the RAD is not that of judicial review, but rather of appeal and that the RAD had to consider all the evidence and make its own assessment (at paras 30-38). However, on questions of fact, Justice Shore indicates that a certain degree of deference is required, which corresponds to the standard of “reasonableness” (at paras 2 and 40). It is also a question of “palpable and overriding error” (at paras 1 and 39).

## 23409:3 · paragraphs 29-73

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6389df0dece7cf3ae5b464079ff4247fb6e9c54428c4fbdd0a6056d9b73df8cd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23409:3:subtheme:1 · paragraphs 29-31

- Raw key terms: `appellate, body, case, court, fact, first, instance, made`
- Display key terms: `appellate, body, case, fact, first, instance, made`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: appellate, body, case, fact, first, instance, made Rule/authority context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness. Application context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness. Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5100003` offsets `141-148`; context: [39] The Court recognizes that it would be absurd, and contrary to subsection 110(3), to task the RAD with re-examining, for every instance, whether the claimants are in fact refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `testimony` at chunk `5100003` offsets `483-492`; context: It is clear from the case law that an appellate body cannot substitute its own reasoning for that of a specialized tribunal of first instance, the tribunal of fact, having the advantage of having heard viva voce testimony and with its authority conferred by the Inquiries Act, unless the trial judge made a “palpable and overriding error” that led to an erroneous result …
- Evidence: `governing_rule` cue `standard of review` at chunk `5100004` offsets `76-94`; context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `5100004` offsets `101-108`; context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness.

#### 23409:3:subtheme:2 · paragraphs 32-34

- Raw key terms: `above, court, appeal, assessment, cannot, decision, determine, evidence`
- Display key terms: `above, assessment, cannot, determine`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, assessment, cannot, determine Rule/authority context: [28] In this first decision, Justice Shore avoided characterizing the new action before the RAD as an “appeal de novo”, such as for appeals brought before the Immigration Appeal Division (IAD) under section 67 of the IRP Application context: Basing himself on what the Court of Appeal of Quebec wrote in Parizeau, above, and by analogy in the scheme of the IAD, Justice Shore reiterated that the RAD cannot be assimilated to a judicial review body and therefore  Evidence spans paragraphs 32-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5100005` offsets `267-274`; context: [41] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir, above; Newfoundland and Labrador Nurses’ Union, above; Alberta Teachers’ Association, above).
- Evidence: `evidence_fact` cue `evidence` at chunk `5100005` offsets `139-147`; context: [41] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir, above; Newfoundland and Labrador Nurses’ Union, above; Alberta Teachers’ Association, above).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5100005` offsets `615-621`; context: According to this trio of judgments by the Supreme Court of Canada, the RAD cannot exempt itself from considering the evidence as a whole.
- Evidence: `issue` cue `whether` at chunk `5100006` offsets `430-437`; context: It follows that to determine whether the RPD’s decision is “reasonable”, the RAD must consider the evidence presented to the RPD and conduct “an independent assessment of all of the evidence” (at paras 3 and 41).
- Evidence: `evidence_fact` cue `evidence` at chunk `5100006` offsets `353-361`; context: That said, he nevertheless finds that “this limitation in no way diminishes the jurisdiction conferred upon the RAD to review the evidence that was before the RPD” (at para 35).
- Evidence: `governing_rule` cue `under` at chunk `5100006` offsets `193-198`; context: [28] In this first decision, Justice Shore avoided characterizing the new action before the RAD as an “appeal de novo”, such as for appeals brought before the Immigration Appeal Division (IAD) under section 67 of the IRPA.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5100006` offsets `237-249`; context: That said, he nevertheless finds that “this limitation in no way diminishes the jurisdiction conferred upon the RAD to review the evidence that was before the RPD” (at para 35).
- Evidence: `reasoning_application` cue `therefore` at chunk `5100007` offsets `500-509`; context: Basing himself on what the Court of Appeal of Quebec wrote in Parizeau, above, and by analogy in the scheme of the IAD, Justice Shore reiterated that the RAD cannot be assimilated to a judicial review body and therefore must not apply the standard of judicial review (Eng, above at paras 23 to 28; Garcia Alvarez, above, at paras 22 to 27).

#### 23409:3:subtheme:3 · paragraphs 35-39

- Raw key terms: `decision, error, overriding, palpable, above, justice, made, reasonableness`
- Display key terms: `error, overriding, palpable, above, justice, made, reasonableness`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: error, overriding, palpable, above, justice, made, reasonableness Rule/authority context: [30] Therefore, it may be said that Justice Shore is no longer “entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness” (Iyamuremye, above at pa Application context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness. | [30] Therefore, it may be said that Justice Shore is no longer “entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness” (Iyamuremye, above at pa Evidence spans paragraphs 35-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5100008` offsets `79-86`; context: [29] … When analyzing a decision of the RPD, the RAD must not merely determine whether it was made in a reasonable manner, but, rather, analyze whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error (Housen, above).
- Evidence: `counterargument_limitation` cue `but` at chunk `5100008` offsets `123-126`; context: [29] … When analyzing a decision of the RPD, the RAD must not merely determine whether it was made in a reasonable manner, but, rather, analyze whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error (Housen, above).
- Evidence: `reasoning_application` cue `apply` at chunk `5100009` offsets `243-248`; context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness.
- Evidence: `counterargument_limitation` cue `However` at chunk `5100009` offsets `125-132`; context: However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `5100010` offsets `480-488`; context: In summary, according to Justice Shore, the RAD must conduct its own assessment of all the evidence, but in doing so, it still owes some deference to the RPD’s findings of fact, because it is the tribunal of first instance and it has the advantage hearing testimony viva voce (Eng, above at para 34; Garcia Alvarez, above at para 33).
- Evidence: `governing_rule` cue `standard of review` at chunk `5100010` offsets `108-126`; context: [30] Therefore, it may be said that Justice Shore is no longer “entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness” (Iyamuremye, above at para 40).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100010` offsets `5-14`; context: [30] Therefore, it may be said that Justice Shore is no longer “entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness” (Iyamuremye, above at para 40).
- Evidence: `counterargument_limitation` cue `but` at chunk `5100010` offsets `490-493`; context: In summary, according to Justice Shore, the RAD must conduct its own assessment of all the evidence, but in doing so, it still owes some deference to the RPD’s findings of fact, because it is the tribunal of first instance and it has the advantage hearing testimony viva voce (Eng, above at para 34; Garcia Alvarez, above at para 33).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100011` offsets `428-437`; context: Therefore, the matter will have to be referred back” (para 56).

#### 23409:3:subtheme:4 · paragraphs 40-43

- Raw key terms: `above, assessment, conclusion, credibility, huruglica, made, njeukam, paras`
- Display key terms: `above, assessment, conclusion, credibility, huruglica, made, njeukam, paras`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: above, assessment, conclusion, credibility, huruglica, made, njeukam, paras Evidence spans paragraphs 40-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5100013` offsets `299-306`; context: It must review all aspects of the RPD’s decision and come to an independent assessment of whether the claimant is a Convention refugee or a person in need of protection.
- Evidence: `issue` cue `issues` at chunk `5100014` offsets `98-104`; context: [55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5100016` offsets `229-237`; context: [14] Except in cases where the credibility of a witness is critical or determinative or when the RPD has a particular benefit from the RAD to draw a specific conclusion, the RAD must not give any deference to the analysis of the evidence made by the RPD: see Huruglica, at paras 37 and 55.

#### 23409:3:subtheme:5 · paragraphs 44-54

- Raw key terms: `standard, appeal, justice, above, court, decision, error, overriding`
- Display key terms: `standard, justice, above, error, overriding`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: standard, justice, above, error, overriding Position/evidence statements: The parties did not argue that the decisions of Justice Shore or the standard of palpable and overriding error should be applied. | Therefore, both counsel who argued this matter before the Court were particularly bothered by the Court’s questions. Rule/authority context: [34] In short, we may speak above of a composite and variable standard of review flowing from a “hybrid appeal” and the particular nature of the questions of fact, or mixed fact and law. | [81] The Supreme Court and our court have consistently repeated the following instruction: the appeal tribunal may, in principle, correct any error of law in the decision under appeal or any palpable and overriding error Application context: Therefore, the use of the standard of reasonableness was not determinative; Justice Locke dismissed the application for judicial review. | The parties did not argue that the decisions of Justice Shore or the standard of palpable and overriding error should be applied. Operative outcome context: Therefore, the use of the standard of reasonableness was not determinative; Justice Locke dismissed the application for judicial review. Evidence spans paragraphs 44-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5100017` offsets `239-247`; context: For example, in Njeukam, above, where it was a pure question of credibility (the RPD’s non-credibility finding was based on the testimony of the refugee claimant herself), the RAD had to show deference (Njeukam, above at paras 18-20).
- Evidence: `evidence_fact` cue `testimony` at chunk `5100017` offsets `315-324`; context: For example, in Njeukam, above, where it was a pure question of credibility (the RPD’s non-credibility finding was based on the testimony of the refugee claimant herself), the RAD had to show deference (Njeukam, above at paras 18-20).
- Evidence: `governing_rule` cue `standard of review` at chunk `5100017` offsets `62-80`; context: [34] In short, we may speak above of a composite and variable standard of review flowing from a “hybrid appeal” and the particular nature of the questions of fact, or mixed fact and law.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100017` offsets `422-431`; context: Therefore, the use of the standard of reasonableness was not determinative; Justice Locke dismissed the application for judicial review.
- Evidence: `counterargument_limitation` cue `However` at chunk `5100017` offsets `559-566`; context: However, in Yetna, above, Justice Locke determined that, since some findings of the RPD on the credibility of the applicant were not based only on her testimony, but also on evidence in the record, the RPD enjoyed no advantage over the RAD when it made its findings and the RAD had to reconsider the evidence on this topic (Yetna, above at paras 21-25).
- Evidence: `disposition` cue `dismissed` at chunk `5100017` offsets `512-521`; context: Therefore, the use of the standard of reasonableness was not determinative; Justice Locke dismissed the application for judicial review.
- Evidence: `party_position` cue `argue` at chunk `5100018` offsets `213-218`; context: The parties did not argue that the decisions of Justice Shore or the standard of palpable and overriding error should be applied.
- Evidence: `reasoning_application` cue `applied` at chunk `5100018` offsets `314-321`; context: The parties did not argue that the decisions of Justice Shore or the standard of palpable and overriding error should be applied.
- Evidence: `counterargument_limitation` cue `However` at chunk `5100018` offsets `412-419`; context: However, the hearings also took place before Huruglica, which Justice Locke applied with different results, was decided.
- Evidence: `evidence_fact` cue `found that` at chunk `5100019` offsets `416-426`; context: After reviewing the legislative scheme governing the RAD, he found that it leaves no room for the RAD to show deference to the RPD:
[translation]
The legislative scheme does not give any indication that deference was considered by Parliament.
- Evidence: `evidence_fact` cue `found that` at chunk `5100020` offsets `424-434`; context: Like Justice Shore, Justice Roy drew a parallel between the RAD’s scheme and the legislative scheme reviewed in Parizeau, above, and, after analyzing the legislative debates relating to the creation of the RAD, he found that it exercises an appellate function and jurisdiction, not a role of judicial review.
- Evidence: `counterargument_limitation` cue `However` at chunk `5100020` offsets `519-526`; context: However, Justice Roy indicates that an appeal does not mean a new trial or a reconsideration of the matter in its entirety and that the standard applicable during any appeal should also be applicable to RAD appeals:
[translation]
- Evidence: `governing_rule` cue `under` at chunk `5100022` offsets `171-176`; context: [81] The Supreme Court and our court have consistently repeated the following instruction: the appeal tribunal may, in principle, correct any error of law in the decision under appeal or any palpable and overriding error in the determination of the facts or in the application of law (if it was correctly determined) to the facts.
- Evidence: `reasoning_application` cue `apply` at chunk `5100023` offsets `78-83`; context: [40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (para 37).
- Evidence: `evidence_fact` cue `found that` at chunk `5100024` offsets `28-38`; context: [38] Therefore, Justice Roy found that the standards applicable by the RAD are the standards applicable on appeal, i.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100024` offsets `5-14`; context: [38] Therefore, Justice Roy found that the standards applicable by the RAD are the standards applicable on appeal, i.
- Evidence: `party_position` cue `argued` at chunk `5100025` offsets `313-319`; context: Therefore, both counsel who argued this matter before the Court were particularly bothered by the Court’s questions.
- Evidence: `governing_rule` cue `standard of review` at chunk `5100025` offsets `55-73`; context: [39] It is not difficult to imagine that the choice of standard of review may have a direct impact on the result of the appeal.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100025` offsets `285-294`; context: Therefore, both counsel who argued this matter before the Court were particularly bothered by the Court’s questions.
- Evidence: `party_position` cue `argued` at chunk `5100026` offsets `106-112`; context: [40] By relying in particular on Justice Phelan’s decision in Huruglica, above, counsel for the applicant argued that, in applying the standard of reasonableness, Member Gallagher had not fulfilled his mandate since he did not conduct his own legal analysis of the facts and the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5100026` offsets `279-287`; context: [40] By relying in particular on Justice Phelan’s decision in Huruglica, above, counsel for the applicant argued that, in applying the standard of reasonableness, Member Gallagher had not fulfilled his mandate since he did not conduct his own legal analysis of the facts and the evidence.
- Evidence: `party_position` cue `argued` at chunk `5100027` offsets `300-306`; context: Counsel for the respondent also argued that Justice Shore, in Iyamuremye, above, had erred in law by indicating that the RAD had to conduct an independent assessment of all the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5100027` offsets `445-453`; context: Counsel for the respondent also argued that Justice Shore, in Iyamuremye, above, had erred in law by indicating that the RAD had to conduct an independent assessment of all the evidence.
- Evidence: `reasoning_application` cue `Because` at chunk `5100027` offsets `128-135`; context: Because of its expertise in the field, it was reasonable for the RAD to apply the standard of judicial review of reasonableness.

#### 23409:3:subtheme:6 · paragraphs 55-58

- Raw key terms: `canada, comity, court, immigration, judge, judicial, principle, applied`
- Display key terms: `comity, judge, judicial, principle, applied`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: comity, judge, judicial, principle, applied Rule/authority context: It would be expected that the principle of judicial comity is particularly important in immigration matters, since under the IRPA, decisions of this Court may uniquely be subject to an appeal to the Federal Court of Appe Application context: And what gives the rule of law its precedence is its universality: It applies equally to all; there is no place for judicial or administrative discretion. | As Justice Wilson stated in Re Hansard Spruce Mills Ltd, [1954] 4 DLR 590 (BCSC), the statements of which were recalled by this Court in Alfred v Canada (Minister of Citizenship and Immigration), 2005 FC 1134 at para 15: Evidence spans paragraphs 55-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5100028` offsets `782-790`; context: It would be expected that the principle of judicial comity is particularly important in immigration matters, since under the IRPA, decisions of this Court may uniquely be subject to an appeal to the Federal Court of Appeal if a question of general importance is certified.
- Evidence: `governing_rule` cue `under` at chunk `5100028` offsets `669-674`; context: It would be expected that the principle of judicial comity is particularly important in immigration matters, since under the IRPA, decisions of this Court may uniquely be subject to an appeal to the Federal Court of Appeal if a question of general importance is certified.
- Evidence: `reasoning_application` cue `applies` at chunk `5100028` offsets `236-243`; context: And what gives the rule of law its precedence is its universality: It applies equally to all; there is no place for judicial or administrative discretion.
- Evidence: `reasoning_application` cue `because` at chunk `5100029` offsets `567-574`; context: As Justice Wilson stated in Re Hansard Spruce Mills Ltd, [1954] 4 DLR 590 (BCSC), the statements of which were recalled by this Court in Alfred v Canada (Minister of Citizenship and Immigration), 2005 FC 1134 at para 15:
I have no power to overrule a brother Judge, I can only differ from him, and the effect of my doing so is not to settle but rather to unsettle the law, because, following such a difference of opinion, the unhappy litigant is confronted with conflicting opinions emanating from the same Court and therefore of the same legal weight.
- Evidence: `reasoning_application` cue `Applied` at chunk `5100031` offsets `85-92`; context: Applied to decisions rendered by judges of the Federal Court, the principle is to the effect that a substantially similar decision rendered by a judge of this Court should be followed in the interest of advancing certainty in the law …

#### 23409:3:subtheme:7 · paragraphs 59-60

- Raw key terms: `comity, create, decision, different, injustice, judicial, previous, principle`
- Display key terms: `comity, create, different, injustice, judicial, previous, principle`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: comity, create, different, injustice, judicial, previous, principle Rule/authority context: [45] I repeat: the principle of judicial comity aims therefore to prevent the creation of conflicting lines of jurisprudence and to encourage certainty in the law. Application context: [45] I repeat: the principle of judicial comity aims therefore to prevent the creation of conflicting lines of jurisprudence and to encourage certainty in the law. Evidence spans paragraphs 59-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5100032` offsets `207-212`; context: Where the issue to be decided is different;
3.
- Evidence: `issue` cue `question` at chunk `5100033` offsets `220-228`; context: Generally, a judge should follow a decision on the same question of one of his or her colleagues, unless the previous decision differs in the facts, a different question is asked, the decision is clearly wrong or the application of the decision would create an injustice.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5100033` offsets `111-124`; context: [45] I repeat: the principle of judicial comity aims therefore to prevent the creation of conflicting lines of jurisprudence and to encourage certainty in the law.
- Evidence: `reasoning_application` cue `therefore` at chunk `5100033` offsets `53-62`; context: [45] I repeat: the principle of judicial comity aims therefore to prevent the creation of conflicting lines of jurisprudence and to encourage certainty in the law.

#### 23409:3:subtheme:8 · paragraphs 61-62

- Raw key terms: `appeal, applicable, canada, case, counsel, court, error, federal`
- Display key terms: `applicable, case, error, federal`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: applicable, case, error, federal Rule/authority context: [46] From the point of view of the facts, this case does not call for a reconsideration of the principles of law applicable or for a new interpretation of sections 110 and 111 of the IRPA. Application context: For the same reasons as my colleagues, I conclude that in applying the standard of judicial review of reasonableness, Member Gallagher committed a reviewable error in law: the RAD is an appellate body, not a judicial rev | Because of its expertise, as a specialized appeal tribunal, I feel that it is the kind of question that the RAD can easily settle and should have the chance to decide, preferably before the Federal Court of Appeal or the Evidence spans paragraphs 61-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5100034` offsets `193-198`; context: The issue is always the same question of law or of jurisdiction relating to scope of the appellate review conducted by the RAD.
- Evidence: `governing_rule` cue `principles` at chunk `5100034` offsets `95-105`; context: [46] From the point of view of the facts, this case does not call for a reconsideration of the principles of law applicable or for a new interpretation of sections 110 and 111 of the IRPA.
- Evidence: `reasoning_application` cue `conclude` at chunk `5100034` offsets `771-779`; context: For the same reasons as my colleagues, I conclude that in applying the standard of judicial review of reasonableness, Member Gallagher committed a reviewable error in law: the RAD is an appellate body, not a judicial review body and it must not assess its role based on criteria of judicial review.
- Evidence: `issue` cue `question` at chunk `5100035` offsets `758-766`; context: Because of its expertise, as a specialized appeal tribunal, I feel that it is the kind of question that the RAD can easily settle and should have the chance to decide, preferably before the Federal Court of Appeal or the Supreme Court of Canada do (without having perhaps the benefit of knowing the RAD’s point of view).
- Evidence: `evidence_fact` cue `evidence` at chunk `5100035` offsets `428-436`; context: There is no agreement on either side of the very notion of credibility, or on the applicable test for the inferences that may be drawn by the RPD from the documentary evidence.
- Evidence: `reasoning_application` cue `Because` at chunk `5100035` offsets `668-675`; context: Because of its expertise, as a specialized appeal tribunal, I feel that it is the kind of question that the RAD can easily settle and should have the chance to decide, preferably before the Federal Court of Appeal or the Supreme Court of Canada do (without having perhaps the benefit of knowing the RAD’s point of view).

#### 23409:3:subtheme:9 · paragraphs 63-65

- Raw key terms: `above, appeal, appropriate, case, chairperson, considers, constitute, court`
- Display key terms: `above, appropriate, case, chairperson, considers, constitute`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, appropriate, case, chairperson, considers, constitute Rule/authority context: That said, nothing prevents the Chairperson of the IRB to constitute a three-member panel of the RAD to hear the case, which could confer the value of precedent on the RAD decision under paragraph 171(c) of the IRPA, and Application context: Therefore, it is only in exceptional cases that the Court will give directions equivalent to a directed verdict and this power will only be rarely used when the issue is of a factual nature (Xie, above at para 18; Canada Evidence spans paragraphs 63-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5100036` offsets `584-589`; context: Therefore, it is only in exceptional cases that the Court will give directions equivalent to a directed verdict and this power will only be rarely used when the issue is of a factual nature (Xie, above at para 18; Canada (Minister of Human Resources Development) v Rafuse, 2002 FCA 31 at para 14).
- Evidence: `evidence_fact` cue `evidence` at chunk `5100036` offsets `388-396`; context: [48] In Xie v Canada (Minister of Employment and Immigration) (1994) 75 FTR 125 (FC) (Xie), the Court stated that even if it had the jurisdiction to refer the case back for determination in accordance with such directions as it considers to be appropriate, the Court should leave the specialized tribunals the right to exercise their jurisdiction and make decisions on merit based on the evidence before them (at para 18).
- Evidence: `reasoning_application` cue `Therefore` at chunk `5100036` offsets `423-432`; context: Therefore, it is only in exceptional cases that the Court will give directions equivalent to a directed verdict and this power will only be rarely used when the issue is of a factual nature (Xie, above at para 18; Canada (Minister of Human Resources Development) v Rafuse, 2002 FCA 31 at para 14).
- Evidence: `issue` cue `issues` at chunk `5100037` offsets `560-566`; context: According to the IRB Web site, when it concerns the RAD, the Chairperson will constitute a three-member panel if at least one of the following criteria is met:
• The appeal raises unusually complex or emerging legal issues.
- Evidence: `governing_rule` cue `under` at chunk `5100038` offsets `553-558`; context: That said, nothing prevents the Chairperson of the IRB to constitute a three-member panel of the RAD to hear the case, which could confer the value of precedent on the RAD decision under paragraph 171(c) of the IRPA, and on the approach used.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5100038` offsets `71-77`; context: [50] Member Gallagher, who made the impugned decision in January 2014, cannot be criticized for not considering the case law of the Court cited above.

#### 23409:3:subtheme:10 · paragraphs 66-67

- Raw key terms: `appeal, approach, approaches, canada, court, federal, issue, judges`
- Display key terms: `approach, approaches, federal, judges`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: approach, approaches, federal, judges Application context: [51] For practical reasons, if we wish to be pragmatic, our Court may have to resolve—so long as the Federal Court of Appeal and the Supreme Court of Canada have not ruled on the issue—not to intervene in judicial review | [52] In our hierarchical justice system, the RAD must give effect to the judgments of this Court and it should wait for the urbi et orbi benediction of the Federal Court of Appeal or of the Supreme Court of Canada itself Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5100039` offsets `179-184`; context: [51] For practical reasons, if we wish to be pragmatic, our Court may have to resolve—so long as the Federal Court of Appeal and the Supreme Court of Canada have not ruled on the issue—not to intervene in judicial review when the RAD applies the second or third approach.
- Evidence: `reasoning_application` cue `applies` at chunk `5100039` offsets `234-241`; context: [51] For practical reasons, if we wish to be pragmatic, our Court may have to resolve—so long as the Federal Court of Appeal and the Supreme Court of Canada have not ruled on the issue—not to intervene in judicial review when the RAD applies the second or third approach.
- Evidence: `issue` cue `issue` at chunk `5100040` offsets `855-860`; context: If it can be said that the first approach became moot (the standard of judicial review of reasonableness was rejected by the Court), the person who could predict today which of the other two approaches would finally prevail would be quite clever; especially since the situation could again change as other judges choose to rule on the issue.
- Evidence: `reasoning_application` cue `apply` at chunk `5100040` offsets `252-257`; context: [52] In our hierarchical justice system, the RAD must give effect to the judgments of this Court and it should wait for the urbi et orbi benediction of the Federal Court of Appeal or of the Supreme Court of Canada itself, before imposing any desire to apply the reasonableness standard of judicial review in any appeal of an RPD decision.

#### 23409:3:subtheme:11 · paragraphs 68-69

- Raw key terms: `appeal, question, review, above, allowed, applicant, application, apply`
- Display key terms: `question, review, above, allowed, apply`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: question, review, above, allowed, apply Rule/authority context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under th Application context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under th Operative outcome context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under th Evidence spans paragraphs 68-69. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5100041` offsets `20-27`; context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under the IRPA since the RAD chose to apply a standard of review of reasonableness corresponding to an application for judicial review, such that this application for judicial review must be allowed and the matter returned to the RAD for redetermination of the appeal (Spasoja, above at paras 2, 3 and 47).
- Evidence: `governing_rule` cue `under` at chunk `5100041` offsets `212-217`; context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under the IRPA since the RAD chose to apply a standard of review of reasonableness corresponding to an application for judicial review, such that this application for judicial review must be allowed and the matter returned to the RAD for redetermination of the appeal (Spasoja, above at paras 2, 3 and 47).
- Evidence: `reasoning_application` cue `apply` at chunk `5100041` offsets `250-255`; context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under the IRPA since the RAD chose to apply a standard of review of reasonableness corresponding to an application for judicial review, such that this application for judicial review must be allowed and the matter returned to the RAD for redetermination of the appeal (Spasoja, above at paras 2, 3 and 47).
- Evidence: `disposition` cue `allowed` at chunk `5100041` offsets `204-211`; context: [53] In conclusion, whether it is a question of jurisdiction or a question of interpretation falling within the RAD’s specialized expertise, in this case, the applicant did not have the appeal that he is allowed under the IRPA since the RAD chose to apply a standard of review of reasonableness corresponding to an application for judicial review, such that this application for judicial review must be allowed and the matter returned to the RAD for redetermination of the appeal (Spasoja, above at paras 2, 3 and 47).
- Evidence: `issue` cue `question` at chunk `5100042` offsets `78-86`; context: [54] Counsel for the respondent proposes that the Court certify the following question: [translation] “Considering the legislative framework of the RAD, what is the scope of the review conducted by the RAD on appeal when it considers an appeal of an RPD decision?

#### 23409:3:subtheme:12 · paragraphs 70-71

- Raw key terms: `appeal, appeals, certification, conducted, counsel, jurisdiction, multiplicity, question`
- Display key terms: `appeals, certification, conducted, jurisdiction, multiplicity, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: appeals, certification, conducted, jurisdiction, multiplicity, question Evidence spans paragraphs 70-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5100043` offsets `65-73`; context: [55] Counsel for the applicant objects to the certification of a question.
- Evidence: `issue` cue `question` at chunk `5100044` offsets `28-36`; context: [56] In this case, the same question was proposed by the respondent to Justice Phelan in Huruglica, above, and after the Court’s verification, he certified it in the following words: [translation] “What is the scope of the review conducted by the Refugee Appeal Division when it considers an appeal of a decision of the Refugee Protection Division?

#### 23409:3:subtheme:13 · paragraphs 72-73

- Raw key terms: `certified, court, question, allow, appeal, canada, certainly, certifying`
- Display key terms: `certified, question, allow, certainly, certifying`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: certified, question, allow, certainly, certifying Evidence spans paragraphs 72-73. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5100045` offsets `183-191`; context: [57] As the Federal Court of Appeal stated in Varela v Canada (Citizenship and Immigration), 2009 FCA 145, the provision preventing any appeal to the Federal Court of Appeal unless a question is certified “fits within a larger scheme designed to ensure that a claimant’s right to seek the intervention of the courts is not invoked lightly, and that such intervention, when justified, is timely” (at para 23).
- Evidence: `issue` cue `question` at chunk `5100046` offsets `8-16`; context: [58] No question will be certified in this file by the Court.

#### Section text

[27] This is how Justice Shore summarizes his thinking on the subject:

[39] The Court recognizes that it would be absurd, and contrary to subsection 110(3), to task the RAD with re-examining, for every instance, whether the claimants are in fact refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA. It is clear from the case law that an appellate body cannot substitute its own reasoning for that of a specialized tribunal of first instance, the tribunal of fact, having the advantage of having heard viva voce testimony and with its authority conferred by the Inquiries Act, unless the trial judge made a “palpable and overriding error” that led to an erroneous result …

[40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness. It is well established that an appellate body must review the findings of a tribunal of first instance by applying a correctness standard to findings that involve questions of law, and applying a reasonableness standard to those involving questions of mixed fact and law …

[41] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir, above; Newfoundland and Labrador Nurses’ Union, above; Alberta Teachers’ Association, above). According to this trio of judgments by the Supreme Court of Canada, the RAD cannot exempt itself from considering the evidence as a whole. [Emphasis added]

[28] In this first decision, Justice Shore avoided characterizing the new action before the RAD as an “appeal de novo”, such as for appeals brought before the Immigration Appeal Division (IAD) under section 67 of the IRPA. That said, he nevertheless finds that “this limitation in no way diminishes the jurisdiction conferred upon the RAD to review the evidence that was before the RPD” (at para 35). It follows that to determine whether the RPD’s decision is “reasonable”, the RAD must consider the evidence presented to the RPD and conduct “an independent assessment of all of the evidence” (at paras 3 and 41). In this regard, it is a variation of the third approach proposing a composite and variable standard of review (Huruglica, above). I will return to this vital point below, given that it is a finding of law that is not shared by certain members of the Court, including Justice Roy, who wanted to avoid the problem resulting from any [translation] “blurring of lines” (Spasoja, above at para 21).

[29] In Eng and Garcia Alvarez, above, decided at the same time on July 17, 2014, Justice Shore returned to his analysis of the law and this time he breathed new life into the standard of palpable and overriding error that had only been raised in Iyamuremye, above, as we have seen before. Basing himself on what the Court of Appeal of Quebec wrote in Parizeau, above, and by analogy in the scheme of the IAD, Justice Shore reiterated that the RAD cannot be assimilated to a judicial review body and therefore must not apply the standard of judicial review (Eng, above at paras 23 to 28; Garcia Alvarez, above, at paras 22 to 27). While acknowledging that “an appeal before the RAD is not an appeal de novo” (Garcia Alvarez, above at para 25; Eng, above at para 26), Justice Shore explains further:

[29] … When analyzing a decision of the RPD, the RAD must not merely determine whether it was made in a reasonable manner, but, rather, analyze whether the RPD relied on a wrong principle of law or misassessed the facts to the point of making a palpable and overriding error (Housen, above).

[30] “Palpable and overriding error” is often used interchangeably with the “clearly wrong” or “unreasonable” decision test. However, this is the appellate-level standard of intervention that a specialized appeal tribunal such as the RAD must apply when reviewing a decision and not the judicial review standard of reasonableness. Even though there are similarities, these standards are different. [Emphasis added]

[30] Therefore, it may be said that Justice Shore is no longer “entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness” (Iyamuremye, above at para 40). The result is that the RAD had committed a reviewable error by using the standard of review of reasonableness rather than that of palpable and overriding error. In summary, according to Justice Shore, the RAD must conduct its own assessment of all the evidence, but in doing so, it still owes some deference to the RPD’s findings of fact, because it is the tribunal of first instance and it has the advantage hearing testimony viva voce (Eng, above at para 34; Garcia Alvarez, above at para 33). In passing, in Garcia Alvarez and Eng, above, Justice Shore noted that:
The idea that the RAD may substitute an original decision by a determination that should have been rendered without first assessing the evidence is completely inconsistent with the purpose of the IRPA and the case law dealing with the virtually identical wording of subsection 67(2) (Garcia Alvarez, above at para 33; Eng, above at para 34)

[31] However, there is a different way to address the scope of the RAD’s appellate review. For the purposes of being well understood, I spoke earlier of “a third approach”. In Huruglica, above, made on August 22, 2014, Justice Phelan had previously arrived at the same result as Justice Shore in Eng and Garcia Alvarez, above: “[The RAD] should have done more than address the decision from the perspective of “reasonableness”. Therefore, the matter will have to be referred back” (para 56). Like Justice Shore, Justice Phelan noted that the RAD is not a judicial review body; therefore, it must not limit itself to assessing the reasonableness of the RPD’s decision (paras 35 to 49). And if a comparison must be made with other administrative appeal schemes, that of the IAD is the most relevant (paras 50 to 53). In this sense, the thinking of Justice Phelan concurs with that of Justice Shore.

[32] I come to the key element of Justice Phelan’s reasoning. According to my colleague, the RAD’s power of intervention in relation to the RPD’s findings of fact is more important than the mere power to intervene when there is a palpable and overriding error:

[54] Having concluded that the RAD erred in reviewing the RPD’s decision on the standard of reasonableness, I have further concluded that for the reasons above, the RAD is required to conduct a hybrid appeal. It must review all aspects of the RPD’s decision and come to an independent assessment of whether the claimant is a Convention refugee or a person in need of protection. Where its assessment departs from that of the RPD, the RAD must substitute its own decision.

[55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error”. (Huruglica, above at paras 54-55).

[33] It is this more nuanced approach that was recently endorsed by Justice Locke in two decisions made on September 10, 2014: Njeukam v Canada (Citizenship and Immigration), 2014 FC 859 (Njeukam), and Yetna v Canada (Citizenship and Immigration), 2014 FC 858 (Yetna). Justice Locke stated that:

[14] Except in cases where the credibility of a witness is critical or determinative or when the RPD has a particular benefit from the RAD to draw a specific conclusion, the RAD must not give any deference to the analysis of the evidence made by the RPD: see Huruglica, at paras 37 and 55. The RAD has as much expertise as the RPD and maybe more with respect to the analysis of the relevant documents and the representations from the parties. (Njeukam, above at para 14; see also Yetna, above at para 17).

[34] In short, we may speak above of a composite and variable standard of review flowing from a “hybrid appeal” and the particular nature of the questions of fact, or mixed fact and law. For example, in Njeukam, above, where it was a pure question of credibility (the RPD’s non-credibility finding was based on the testimony of the refugee claimant herself), the RAD had to show deference (Njeukam, above at paras 18-20). Therefore, the use of the standard of reasonableness was not determinative; Justice Locke dismissed the application for judicial review. However, in Yetna, above, Justice Locke determined that, since some findings of the RPD on the credibility of the applicant were not based only on her testimony, but also on evidence in the record, the RPD enjoyed no advantage over the RAD when it made its findings and the RAD had to reconsider the evidence on this topic (Yetna, above at paras 21-25). The use of the standard of reasonableness proved fatal and the application for judicial review was allowed by the Court.

[35] I pause here before continuing this analysis of case law. The hearings in Njeukam and Yetna took place on July 15 and 16, 2014, before the Eng and Garcia Alvarez decisions were published. The parties did not argue that the decisions of Justice Shore or the standard of palpable and overriding error should be applied. In Yetna, counsel for the applicant instead argued the standard of the “wrong” decision. However, the hearings also took place before Huruglica, which Justice Locke applied with different results, was decided. Nevertheless, nothing indicates that Justice Locke requested or received additional arguments from the parties regarding Eng, Alvarez Garcia or Huruglica.

[36] This application for judicial review was heard on September 24, 2014. To my knowledge, the most recent decision on the scope of the RAD’s appellate review was that made a day earlier in Spasoja, above. Justice Roy favoured the application of the standard of palpable and overriding error and set aside the first and third approaches described above. After reviewing the legislative scheme governing the RAD, he found that it leaves no room for the RAD to show deference to the RPD:
[translation]
The legislative scheme does not give any indication that deference was considered by Parliament. Rather, we are facing a scheme where if there is, for example, an error of fact, the matter must be returned to the RPD if a reassessment of the evidence before the RPD is required for a decision. There is no room for deference in such a scheme. (Spasoja, above at para 24).

[37] As for the ultimate result, Justice Roy stated that he shared the view of Justice Phelan in Huruglica, above, and the finding that Justice Shore made in Garcia Alvarez and Eng, above (Spasoja at para 12). Like Justice Shore, Justice Roy drew a parallel between the RAD’s scheme and the legislative scheme reviewed in Parizeau, above, and, after analyzing the legislative debates relating to the creation of the RAD, he found that it exercises an appellate function and jurisdiction, not a role of judicial review. However, Justice Roy indicates that an appeal does not mean a new trial or a reconsideration of the matter in its entirety and that the standard applicable during any appeal should also be applicable to RAD appeals:
[translation]

[39] If the appeal discussed in sections 110 and 111 of the Act must be dealt with as an appeal and not a quasi-judicial review, this does not mean that it will be an opportunity for a new trial or a reconsideration of the matter in its entirety. The Court of Appeal of Quebec makes a very attractive proposition in Parizeau, above, that the appeal of an administrative decision before another administrative tribunal should be treated like any other appeal:

[81] The Supreme Court and our court have consistently repeated the following instruction: the appeal tribunal may, in principle, correct any error of law in the decision under appeal or any palpable and overriding error in the determination of the facts or in the application of law (if it was correctly determined) to the facts. This standard is just as valid for the appeals filed with administrative tribunals and the standard for intervention developed in matters of judicial appeal may certainly be transposed to the quasi-judicial appeal, with reservations and modifications required by the particular law of each case and the general rules of administrative law.
The error of fact must be palpable and overriding to succeed on appeal. The standard of correctness prevails for questions of law. I do not see why it should not be so in an administrative appeal.

[40] My colleague Justice Phelan would have preferred in Huruglica, above, to apply the standard of reasonableness to questions of credibility (para 37). With respect, I am still concerned with the blurring of lines. It seems to be preferable to focus on the standard of palpable and overriding error on appeals on questions of fact. There is nothing a new in proposing that an appeal tribunal show deference when a body whose decision is being appealed flows from considerable discretion such as assessing credibility. The law is clear: the RAD does not hear witnesses except in very exceptional and specific cases. The credibility to be given to the witnesses heard by the RPD is its responsibility and the RAD, on appeal, must show deference (Lensen v Lensen, [1987] 2 SCR 672; R v Burke, [1996] 1 SCR 474). (Spasoja, above, at paras 39-40; emphasis added).

[38] Therefore, Justice Roy found that the standards applicable by the RAD are the standards applicable on appeal, i.e. the standard of palpable and overriding error for the RPD’s findings of fact, while the RAD must correct any error of law by the RPD that is determinative.

[39] It is not difficult to imagine that the choice of standard of review may have a direct impact on the result of the appeal. Moreover, there are currently three approaches. Only the first was categorically rejected by the Court. This leaves two others that seem to wish to compete. Therefore, both counsel who argued this matter before the Court were particularly bothered by the Court’s questions.

[40] By relying in particular on Justice Phelan’s decision in Huruglica, above, counsel for the applicant argued that, in applying the standard of reasonableness, Member Gallagher had not fulfilled his mandate since he did not conduct his own legal analysis of the facts and the evidence. It argued that it was also what the Court had decided in Garcia Alvarez, Eng and Huruglica, above, even if the judges had referred to different tests.

[41] Counsel for the respondent indicated that his mandate was clear: the Court’s prior case law simply should not be followed. Because of its expertise in the field, it was reasonable for the RAD to apply the standard of judicial review of reasonableness. Full stop. Counsel for the respondent also argued that Justice Shore, in Iyamuremye, above, had erred in law by indicating that the RAD had to conduct an independent assessment of all the evidence. That was also the case with Justice Phelan, in Huruglica, above, when he decided that the RAD was required to hear the matter as a “hybrid appeal”. In the alternative, counsel for the respondent argued that the standard of “palpable and overriding error” should be applied, if the first approach, i.e. the reasonableness standard of judicial review , is not used.

[42] As we said above, standards of review are judicial creations. Nonetheless, once established, they must be respected by the courts just as any other rule of law. And what gives the rule of law its precedence is its universality: It applies equally to all; there is no place for judicial or administrative discretion. Further, following the principle of judicial comity and, unless certain exceptions apply, a judge of this Court should not deviate from decisions made by his or her colleagues to avoid creating a situation of uncertainty in the law. It would be expected that the principle of judicial comity is particularly important in immigration matters, since under the IRPA, decisions of this Court may uniquely be subject to an appeal to the Federal Court of Appeal if a question of general importance is certified. Therefore, it is desirable to have some consistency in the Court’s decisions. Yes, the judge can make the law, but when each judge makes his or her own law, the rule law that is no longer applied withers. To use descriptive language, the law loses weight and this unbearable lightness of being makes it irrelevant, leaving more room than is needed for administrative or legal discretion.

[43] Today, I feel as though I face an Olympic dilemma: I am asked to choose between two contradictory approaches (the first approach having been eliminated) adopted by colleagues of the Court. As Justice Wilson stated in Re Hansard Spruce Mills Ltd, [1954] 4 DLR 590 (BCSC), the statements of which were recalled by this Court in Alfred v Canada (Minister of Citizenship and Immigration), 2005 FC 1134 at para 15:
I have no power to overrule a brother Judge, I can only differ from him, and the effect of my doing so is not to settle but rather to unsettle the law, because, following such a difference of opinion, the unhappy litigant is confronted with conflicting opinions emanating from the same Court and therefore of the same legal weight.

[44] In Almrei v Canada (Citizenship and Immigration), 2007 FC 1025, Justice Lemieux summarized the possible exceptions to the principle of judicial comity:

[61] The principle of judicial comity is well-recognized by the judiciary in Canada. Applied to decisions rendered by judges of the Federal Court, the principle is to the effect that a substantially similar decision rendered by a judge of this Court should be followed in the interest of advancing certainty in the law …

[62] There are a number of exceptions to the principle of judicial comity as expressed above they are:
1. The existence of a different factual matrix or evidentiary basis between the two cases;
2. Where the issue to be decided is different;
3. Where the previous condition failed to consider legislation or binding authorities that would have produced a different result, i.e., was manifestly wrong; and;
4. The decision it followed would create an injustice.

[45] I repeat: the principle of judicial comity aims therefore to prevent the creation of conflicting lines of jurisprudence and to encourage certainty in the law. Generally, a judge should follow a decision on the same question of one of his or her colleagues, unless the previous decision differs in the facts, a different question is asked, the decision is clearly wrong or the application of the decision would create an injustice. Judicial comity requires much humility and mutual respect. If the rule of law does not tolerate arbitrariness, judicial comity, its loyal companion, relies on reason and the good judgement of each person. Failing a final judgment from the highest court, respect for the other’s opinion can speak volumes. In short, judicial comity is elegance incarnate in the person of the magistrate who respects the value of precedents.

[46] From the point of view of the facts, this case does not call for a reconsideration of the principles of law applicable or for a new interpretation of sections 110 and 111 of the IRPA. The issue is always the same question of law or of jurisdiction relating to scope of the appellate review conducted by the RAD. Further, it cannot be said that Justices Shore, Phelan or Roy did not thoroughly canvas the relevant law or case law. However,

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23409:4 · paragraphs 74-75

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bd749e57509e3ed47db3d7afb79e382d5856c68683874409287368328869a73c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23409:4:subtheme:1 · paragraphs 74-75

- Raw key terms: `accompanying, adjudges, aghiad, allowed, alyafi, appeal, applicant, application`
- Display key terms: `accompanying, adjudges, aghiad, allowed, alyafi`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: accompanying, adjudges, aghiad, allowed, alyafi No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 74-75. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THE COURT ORDERS AND ADJUDGES that the application for judicial review is allowed. The impugned decision is set aside and the matter returned to the Refugee Appeal Division for redetermination of the applicant’s appeal. The RAD will have to consider the directions provided by the Court in the reasons accompanying this judgment. No question is certified.
“Luc Martineau”
Judge
Certified true translation
Catherine Jones, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-1091-14
STYLE OF CAUSE:
AGHIAD ALYAFI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, QuEbec
DATE OF HEARING:
september 24, 2014


## 23409:5 · paragraphs 76-76

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e2187c431a160bfef3e61709e4c21029513b3ba7ac0b861fd2f95020f53d2819`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23409:5:subtheme:1 · paragraphs 76-76

- Raw key terms: `appearances, applicant, attorney, beaumier, bellefleur, canada, coline, cormie`
- Display key terms: `beaumier, bellefleur, coline, cormie`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: beaumier, bellefleur, coline, cormie No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 76-76. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MARTINEAU J.
DATED:
october 8, 2014
APPEARANCES:
Coline Bellefleur
FOR the applicant
Thomas Cormie
FOR the respondent
SOLICITORS OF RECORD:
Taillefer Beaumier Plouffe Kano s.e.n.c.r.l.
Montréal, Quebec
FOR the applicant
William F. Pentney
Deputy Attorney General of Canada
Ottawa, Ontario
FOR the respondent
