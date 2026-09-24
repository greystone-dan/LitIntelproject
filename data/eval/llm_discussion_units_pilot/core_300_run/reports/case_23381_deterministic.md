# Discussion Units: case 23381

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **58**
- Continuity pairs: **57**
- Discussion Units: **5**
- Paragraph source hashes: **58**
- Sub-themes: **18**

## 23381:1 · paragraphs 0-1

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `087b28732f838a34c99d0e86beca874ef6de93352556b0438783dc88ae1274a3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23381:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `judicial, reasons, review, akuffo, analyzing, appeal, applicant, application`
- Display key terms: `judicial, review, akuffo, analyzing`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: judicial, review, akuffo, analyzing Rule/authority context: Edwin Yaw Sarfo Akuffo [applicant] seeks judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Board, dated September 18, 2013, whereby it confirmed the decision of the Refugee Application context: The RAD applied the reasonableness standard to the RPD’s finding of credibility and, after analyzing the three main issues raised by the applicant, found that it fell well within the range of possible outcomes. Operative outcome context: [2] For the reasons discussed below, this application for judicial review will be dismissed. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5098591` offsets `1100-1106`; context: The RAD applied the reasonableness standard to the RPD’s finding of credibility and, after analyzing the three main issues raised by the applicant, found that it fell well within the range of possible outcomes.
- Evidence: `evidence_fact` cue `found that` at chunk `5098591` offsets `1132-1142`; context: The RAD applied the reasonableness standard to the RPD’s finding of credibility and, after analyzing the three main issues raised by the applicant, found that it fell well within the range of possible outcomes.
- Evidence: `governing_rule` cue `under` at chunk `5098591` offsets `891-896`; context: Edwin Yaw Sarfo Akuffo [applicant] seeks judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Board, dated September 18, 2013, whereby it confirmed the decision of the Refugee Protection Division [RPD] that the applicant was neither a Convention refugee within the meaning of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] nor a person in need of protection under its subsection 97(1).
- Evidence: `reasoning_application` cue `applied` at chunk `5098591` offsets `992-999`; context: The RAD applied the reasonableness standard to the RPD’s finding of credibility and, after analyzing the three main issues raised by the applicant, found that it fell well within the range of possible outcomes.
- Evidence: `disposition` cue `dismissed` at chunk `5098592` offsets `82-91`; context: [2] For the reasons discussed below, this application for judicial review will be dismissed.

#### Section text

Akuffo v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-11-12
Neutral citation
2014 FC 1063
File numbers
IMM-6640-13
Decision Content
Date: 20141112
Docket: IMM-6640-13
Citation: 2014 FC 1063
Ottawa, Ontario, November 12, 2014
PRESENT: The Honourable Madam Justice Gagné
BETWEEN:
EDWIN YAW SARFO AKUFFO
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview [1] Mr. Edwin Yaw Sarfo Akuffo [applicant] seeks judicial review of a decision by the Refugee Appeal Division [RAD] of the Immigration and Refugee Board, dated September 18, 2013, whereby it confirmed the decision of the Refugee Protection Division [RPD] that the applicant was neither a Convention refugee within the meaning of section 96 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] nor a person in need of protection under its subsection 97(1). The RPD found the applicant’s claim to be devoid of credibility. The RAD applied the reasonableness standard to the RPD’s finding of credibility and, after analyzing the three main issues raised by the applicant, found that it fell well within the range of possible outcomes.

[2] For the reasons discussed below, this application for judicial review will be dismissed.


## 23381:2 · paragraphs 2-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9700711740c6fcb2522fb9a915b5489094cc36f7382b40db5cde2c0757ef90be`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23381:2:subtheme:1 · paragraphs 2-8

- Raw key terms: `applicant, ghana, relationship, years, canada, claims, eight, feared`
- Display key terms: `ghana, relationship, years, claims, eight, feared`
- Argument roles: `party_position, reasoning_application`
- Explanation: Observed roles: party_position, reasoning_application Display terms: ghana, relationship, years, claims, eight, feared Position/evidence statements: He did not claim refugee status in the UK because he is well known in the Ghanaian community in Britain and he feared his life would be in danger there too. | [8] […] The tribunal is of the opinion that risking making love in a house where there is twenty people inside and then walking hand in hand in the streets of Ghana after having been caught making love, is not compatible Application context: In that capacity, the applicant applied for a visitor visa to come to Canada, as he feared for his life. | He did not claim refugee status in the UK because he is well known in the Ghanaian community in Britain and he feared his life would be in danger there too. Evidence spans paragraphs 2-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5098595` offsets `183-190`; context: In that capacity, the applicant applied for a visitor visa to come to Canada, as he feared for his life.
- Evidence: `party_position` cue `claim` at chunk `5098596` offsets `109-114`; context: He did not claim refugee status in the UK because he is well known in the Ghanaian community in Britain and he feared his life would be in danger there too.
- Evidence: `reasoning_application` cue `because` at chunk `5098596` offsets `140-147`; context: He did not claim refugee status in the UK because he is well known in the Ghanaian community in Britain and he feared his life would be in danger there too.
- Evidence: `party_position` cue `claims` at chunk `5098597` offsets `343-349`; context: [8] […] The tribunal is of the opinion that risking making love in a house where there is twenty people inside and then walking hand in hand in the streets of Ghana after having been caught making love, is not compatible with the behavior of someone who declared having been scared once caught in the act, nor with the behavior of someone who claims to have been secretive and low key about his relationship for eight years.
- Evidence: `party_position` cue `claims` at chunk `5098598` offsets `98-104`; context: [13] […] The tribunal simply finds not plausible that a young educated artist and businessman who claims having had an intimate relationship with another man for eight years, would have no knowledge that having sex with another man is a crime in his country, nor have not known that the conditions for homosexuals in his country are quite serious and that the Ghanaian society in general is against them, not just the vigilantes.

#### 23381:2:subtheme:2 · paragraphs 9-11

- Raw key terms: `claimant, finds, tribunal, asylum, canada, credibility, fears, further`
- Display key terms: `finds, asylum, credibility, fears, further`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: finds, asylum, credibility, fears, further Position/evidence statements: The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it Application context: The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it | Therefore, the tribunal finds that the claimant’s behavior is not compatible with someone who fears for his life. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5098599` offsets `479-484`; context: The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it and in the end, accepted to go back to the United Kingdom where he believed he could not ask for asylum, because he first wanted to talk to a lawyer or figure out “how to come up with the asylum issue.
- Evidence: `party_position` cue `argued` at chunk `5098599` offsets `268-274`; context: The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it and in the end, accepted to go back to the United Kingdom where he believed he could not ask for asylum, because he first wanted to talk to a lawyer or figure out “how to come up with the asylum issue.
- Evidence: `reasoning_application` cue `because` at chunk `5098599` offsets `135-142`; context: The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it and in the end, accepted to go back to the United Kingdom where he believed he could not ask for asylum, because he first wanted to talk to a lawyer or figure out “how to come up with the asylum issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098600` offsets `153-161`; context: [17] The tribunal, given the claimant’s inability to give a satisfactory explanation to his behavior when he arrived in Canada, gives more weight to the evidence and facts presented by the minister’s representative which demonstrate that the claimant went to the United Kingdom to attend one of his sisters’ wedding, then came to Canada as a visitor but when refused entry, asked for asylum.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5098600` offsets `392-401`; context: Therefore, the tribunal finds that the claimant’s behavior is not compatible with someone who fears for his life.
- Evidence: `counterargument_limitation` cue `but` at chunk `5098600` offsets `350-353`; context: [17] The tribunal, given the claimant’s inability to give a satisfactory explanation to his behavior when he arrived in Canada, gives more weight to the evidence and facts presented by the minister’s representative which demonstrate that the claimant went to the United Kingdom to attend one of his sisters’ wedding, then came to Canada as a visitor but when refused entry, asked for asylum.

#### 23381:2:subtheme:3 · paragraphs 12-15

- Raw key terms: `credibility, decision, respect, appeal, applicant, canada, claim, determination`
- Display key terms: `credibility, respect, determination`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, respect, determination Rule/authority context: His application invoked two grounds: the first relates to which standard of review the RAD should use to determine the appeal and the second pertains to the reasonableness of the RPD’s determination with respect to his c | [12] With respect to the standard of review to be applied to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 [Newton], the RAD held that the RPD, as a first instance tribunal, is  Application context: [12] With respect to the standard of review to be applied to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 [Newton], the RAD held that the RPD, as a first instance tribunal, is  Evidence spans paragraphs 12-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5098602` offsets `114-119`; context: [9] The RPD also was of the opinion that someone who is homosexual and who is asking refugee status based on that issue would not have omitted to mention that he was now seeing a man in Canada, until the very end of the hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098602` offsets `436-444`; context: The applicant did not present new evidence nor request an oral hearing.
- Evidence: `governing_rule` cue `standard of review` at chunk `5098602` offsets `538-556`; context: His application invoked two grounds: the first relates to which standard of review the RAD should use to determine the appeal and the second pertains to the reasonableness of the RPD’s determination with respect to his credibility and, more generally, to his claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098604` offsets `462-470`; context: The rationale is that the appeal did not qualify for a hearing and only the RPD held a hearing directly questioning the applicant and reviewed the evidence before reaching its conclusion.
- Evidence: `governing_rule` cue `standard of review` at chunk `5098604` offsets `25-43`; context: [12] With respect to the standard of review to be applied to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 [Newton], the RAD held that the RPD, as a first instance tribunal, is owed deference, and so its credibility findings must be assessed on a reasonableness standard.
- Evidence: `reasoning_application` cue `applied` at chunk `5098604` offsets `50-57`; context: [12] With respect to the standard of review to be applied to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 [Newton], the RAD held that the RPD, as a first instance tribunal, is owed deference, and so its credibility findings must be assessed on a reasonableness standard.
- Evidence: `counterargument_limitation` cue `but` at chunk `5098604` offsets `576-579`; context: The RAD added that it was not intended to act as a de novo appeal board, but rather to review the RPD decision for reasonableness, as understood by the Supreme Court of Canada’s pronouncements in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir].
- Evidence: `evidence_fact` cue `found that` at chunk `5098605` offsets `57-67`; context: [13] As for the RPD’s credibility determination, the RAD found that it was within the “range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47).

#### 23381:2:subtheme:4 · paragraphs 16-17

- Raw key terms: `application, facts, review, standard, accepted, analysis, applicant, applied`
- Display key terms: `facts, review, standard, accepted, analysis, applied`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: facts, review, standard, accepted, analysis, applied Rule/authority context: Issues and Standard of Review [15] This application raises the following issues: 1. | [16] The parties do not take a position as to the standard of review that should be used by this Court while reviewing the RAD’s interpretation of sections 110, 111, 162 and 171 of the Act [RAD Provisions], and its appli Application context: What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law and credibility findings? Operative outcome context: The applicant did not seek protection upon arrival but only after he was denied entry and accepted to make arrangements to be returned to the United Kingdom [UK]. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5098606` offsets `404-410`; context: Issues and Standard of Review [15] This application raises the following issues:
1.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5098606` offsets `415-433`; context: Issues and Standard of Review [15] This application raises the following issues:
1.
- Evidence: `reasoning_application` cue `applied` at chunk `5098606` offsets `543-550`; context: What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law and credibility findings?
- Evidence: `disposition` cue `denied` at chunk `5098606` offsets `216-222`; context: The applicant did not seek protection upon arrival but only after he was denied entry and accepted to make arrangements to be returned to the United Kingdom [UK].
- Evidence: `governing_rule` cue `standard of review` at chunk `5098607` offsets `50-68`; context: [16] The parties do not take a position as to the standard of review that should be used by this Court while reviewing the RAD’s interpretation of sections 110, 111, 162 and 171 of the Act [RAD Provisions], and its application to the facts of this case.

#### 23381:2:subtheme:5 · paragraphs 18-20

- Raw key terms: `alberta, apply, canada, correctness, court, expertise, general, home`
- Display key terms: `alberta, apply, correctness, expertise, home`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: alberta, apply, correctness, expertise, home Rule/authority context: [17] In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], Justice Phelan acknowledged that there was no jurisprudence of the Federal Court of Appeal or of this Court on that specific  Application context: However, at paragraph 26, relying on Newton and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, he finds that, as “the issue of law is one of general interest to the legal system”, this Cour | [19] First, in Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167, interpreting Alberta Teachers, the Supreme Court of Canada revisits the exceptions where the correctness standard will apply: This  Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5098608` offsets `220-225`; context: [17] In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], Justice Phelan acknowledged that there was no jurisprudence of the Federal Court of Appeal or of this Court on that specific issue.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5098608` offsets `141-154`; context: [17] In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], Justice Phelan acknowledged that there was no jurisprudence of the Federal Court of Appeal or of this Court on that specific issue.
- Evidence: `reasoning_application` cue `apply` at chunk `5098608` offsets `456-461`; context: However, at paragraph 26, relying on Newton and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, he finds that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.
- Evidence: `counterargument_limitation` cue `However` at chunk `5098608` offsets `227-234`; context: However, at paragraph 26, relying on Newton and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, he finds that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.
- Evidence: `reasoning_application` cue `apply` at chunk `5098610` offsets `208-213`; context: [19] First, in Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167, interpreting Alberta Teachers, the Supreme Court of Canada revisits the exceptions where the correctness standard will apply:
This principle [of deference] applies unless the interpretation of the home statute falls into one of the categories of questions to which the correctness standard continues to apply, i.

#### 23381:2:subtheme:6 · paragraphs 21-22

- Raw key terms: `court, importance, justice, legal, outside, standard, adjudicator, administrative`
- Display key terms: `importance, justice, legal, outside, standard, adjudicator, administrative`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: importance, justice, legal, outside, standard, adjudicator, administrative Rule/authority context: [21] Second, in Alberta Teachers, Justice Binnie elaborated that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration. Application context: [20] In other words, in order for this Court to apply a correctness standard to an administrative tribunal’s interpretation of its own statute, each criterion must be met: i) the question of law has to be of central impo Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098611` offsets `179-187`; context: [20] In other words, in order for this Court to apply a correctness standard to an administrative tribunal’s interpretation of its own statute, each criterion must be met: i) the question of law has to be of central importance to the legal system as a whole; and ii) the question of law has to fall outside the adjudicator’s expertise.
- Evidence: `reasoning_application` cue `apply` at chunk `5098611` offsets `48-53`; context: [20] In other words, in order for this Court to apply a correctness standard to an administrative tribunal’s interpretation of its own statute, each criterion must be met: i) the question of law has to be of central importance to the legal system as a whole; and ii) the question of law has to fall outside the adjudicator’s expertise.
- Evidence: `issue` cue `issue` at chunk `5098612` offsets `68-73`; context: [21] Second, in Alberta Teachers, Justice Binnie elaborated that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.
- Evidence: `governing_rule` cue `under` at chunk `5098612` offsets `190-195`; context: [21] Second, in Alberta Teachers, Justice Binnie elaborated that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.

#### 23381:2:subtheme:7 · paragraphs 23-24

- Raw key terms: `appeal, applicable, correctness, court, found, justice, labour, legal`
- Display key terms: `applicable, correctness, justice, labour, legal`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: applicable, correctness, justice, labour, legal Rule/authority context: Continuing on the standard of review, the Supreme Court found that the dispute had “little legal consequence outside the sphere of labour law and that, not its potential real-world consequences, determines the applicable Application context: The New Brunswick Court of Appeal, as a result of its finding that the dispute was of wider public concern, had felt otherwise; it had applied a correctness standard to the board’s analytical framework for determining th Operative outcome context: The Supreme Court found that arbitrators had a broad mandate (albeit, not boundless) where their expertise allowed them to issue arbitral awards by reasonably applying a common law or equitable principle. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098613` offsets `369-377`; context: The Court of Appeal had seen this as a question of law of central importance to the legal system as a whole, and that it did not fall within the expertise of labour arbitrators.
- Evidence: `evidence_fact` cue `found that` at chunk `5098613` offsets `159-169`; context: [22] In Nor-Man Regional Health Authority Inc v Manitoba Association of Health Care Professionals, 2011 SCC 59 [Nor-Man], Justice Fish, for a unanimous Court, found that the Manitoba Court of Appeal erred in choosing correctness as an applicable standard to an arbitrator allegedly misconstruing the equitable remedy of estoppel.
- Evidence: `disposition` cue `allowed` at chunk `5098613` offsets `615-622`; context: The Supreme Court found that arbitrators had a broad mandate (albeit, not boundless) where their expertise allowed them to issue arbitral awards by reasonably applying a common law or equitable principle.
- Evidence: `issue` cue `issues` at chunk `5098614` offsets `813-819`; context: Continuing on the standard of review, the Supreme Court found that the dispute had “little legal consequence outside the sphere of labour law and that, not its potential real-world consequences, determines the applicable standard of review” (at para 66, per Justice Moldaver, dissenting on other issues).
- Evidence: `evidence_fact` cue `found that` at chunk `5098614` offsets `573-583`; context: Continuing on the standard of review, the Supreme Court found that the dispute had “little legal consequence outside the sphere of labour law and that, not its potential real-world consequences, determines the applicable standard of review” (at para 66, per Justice Moldaver, dissenting on other issues).
- Evidence: `governing_rule` cue `standard of review` at chunk `5098614` offsets `535-553`; context: Continuing on the standard of review, the Supreme Court found that the dispute had “little legal consequence outside the sphere of labour law and that, not its potential real-world consequences, determines the applicable standard of review” (at para 66, per Justice Moldaver, dissenting on other issues).
- Evidence: `reasoning_application` cue `applied` at chunk `5098614` offsets `373-380`; context: The New Brunswick Court of Appeal, as a result of its finding that the dispute was of wider public concern, had felt otherwise; it had applied a correctness standard to the board’s analytical framework for determining the validity of an employer’s random alcohol testing policy.

#### 23381:2:subtheme:8 · paragraphs 25-26

- Raw key terms: `attorney, because, canada, canadian, court, found, general, issue`
- Display key terms: `because, canadian`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: because, canadian Rule/authority context: In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods ar | [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outsi Application context: In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods ar | [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outsi Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098615` offsets `281-289`; context: In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods are generally of central importance to the fair administration of justice, there was no reason why the particular limitation period at issue in the appeal was of particular significance.
- Evidence: `evidence_fact` cue `found that` at chunk `5098615` offsets `57-67`; context: [24] In McLean, the British Columbia Court of Appeal had found that the interpretation of a statutory limitation period provision by an administrative tribunal would attract a standard of correctness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5098615` offsets `219-237`; context: In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods are generally of central importance to the fair administration of justice, there was no reason why the particular limitation period at issue in the appeal was of particular significance.
- Evidence: `reasoning_application` cue `because` at chunk `5098615` offsets `362-369`; context: In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods are generally of central importance to the fair administration of justice, there was no reason why the particular limitation period at issue in the appeal was of particular significance.
- Evidence: `issue` cue `question` at chunk `5098616` offsets `113-121`; context: [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outside of issues arising under [the] statutory scheme”.
- Evidence: `evidence_fact` cue `found that` at chunk `5098616` offsets `98-108`; context: [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outside of issues arising under [the] statutory scheme”.
- Evidence: `governing_rule` cue `under` at chunk `5098616` offsets `241-246`; context: [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outside of issues arising under [the] statutory scheme”.
- Evidence: `reasoning_application` cue `because` at chunk `5098616` offsets `171-178`; context: [25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outside of issues arising under [the] statutory scheme”.

#### 23381:2:subtheme:9 · paragraphs 27-28

- Raw key terms: `provisions, question, standard, application, attracts, canada, case, central`
- Display key terms: `provisions, question, standard, attracts, case, central`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: provisions, question, standard, attracts, case, central Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098617` offsets `174-182`; context: [26] In my view and in light of the consistent and firm position taken by the Supreme Court of Canada, the interpretation of the RAD Provisions by the RAD does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `issue` cue `question` at chunk `5098618` offsets `98-106`; context: [27] Finally, the application of the RAD Provisions to the facts of this, or any given case, is a question of mixed fact and law and also attracts the reasonableness standard.

#### Section text

II. Background [3] The applicant is a citizen of Ghana. He alleged before the RPD a well-founded fear of persecution based on his homosexuality and, as homosexuality is illegal in Ghana, that he is a person in need of protection.

[4] The applicant was in a relationship with a Mr. Manu for 8 years prior to leaving Ghana. They kept their relationship “secret and low key.”

[5] On November 8, 2012, the applicant hosted his own birthday party, and he and Mr. Manu went to a bedroom to engage in sexual relations. A group of vigilantes apprehended them during the act, assaulted and threatened them. Later that night, he was once more apprehended walking hand in hand with Mr. Manu and aggressed by the vigilantes. The applicant went to file a report at the police station the same day. The police allegedly refused to help him due to his sexual orientation. The applicant began to receive threats from the vigilantes. As a result, he hid in his mother’s storage space.

[6] The applicant is a musician and rumours of his homosexuality spread in his neighbourhood. He is also director of a travel agency and tour company. In that capacity, the applicant applied for a visitor visa to come to Canada, as he feared for his life.

[7] The applicant flew to Canada via London to ask his sisters who live there for financial help. He did not claim refugee status in the UK because he is well known in the Ghanaian community in Britain and he feared his life would be in danger there too.
III. The RPD Decision [8] On May 14, 2013, the RPD determined he was neither a Convention refugee nor a person in need of protection. The RPD simply did not find him to be credible. Notably:

[8] […] The tribunal is of the opinion that risking making love in a house where there is twenty people inside and then walking hand in hand in the streets of Ghana after having been caught making love, is not compatible with the behavior of someone who declared having been scared once caught in the act, nor with the behavior of someone who claims to have been secretive and low key about his relationship for eight years.
[…]

[13] […] The tribunal simply finds not plausible that a young educated artist and businessman who claims having had an intimate relationship with another man for eight years, would have no knowledge that having sex with another man is a crime in his country, nor have not known that the conditions for homosexuals in his country are quite serious and that the Ghanaian society in general is against them, not just the vigilantes. For all these reasons, there is a serious doubt in the mind of the Tribunal that the claimant is a homosexual.
[…]

[16] The tribunal finds the claimant’s answers unsatisfactory. The tribunal is of the opinion that an individual who flees his country because he fears for his life and with the intention of seeking asylum, would not have tried to get admitted in Canada as a visitor, argued about it and in the end, accepted to go back to the United Kingdom where he believed he could not ask for asylum, because he first wanted to talk to a lawyer or figure out “how to come up with the asylum issue.”

[17] The tribunal, given the claimant’s inability to give a satisfactory explanation to his behavior when he arrived in Canada, gives more weight to the evidence and facts presented by the minister’s representative which demonstrate that the claimant went to the United Kingdom to attend one of his sisters’ wedding, then came to Canada as a visitor but when refused entry, asked for asylum. Therefore, the tribunal finds that the claimant’s behavior is not compatible with someone who fears for his life. The claimant’s credibility is further diminished.
[…]

[22] The tribunal finds that had the claimant been homosexual, he would not have used such general and distant terms as, for example, “that category” when talking about his sexual orientation or be unable to give detailed information about an eight year relationship with the same man, especially if they were, as mentioned by the claimant, seeing each other two to three times a week. The claimant’s credibility with regard to his sexual orientation is further impugned.

[9] The RPD also was of the opinion that someone who is homosexual and who is asking refugee status based on that issue would not have omitted to mention that he was now seeing a man in Canada, until the very end of the hearing.
IV. The Impugned RAD Decision [10] On June 11, 2013, the applicant appealed to the RAD. The Minister of Public Safety and Emergency Preparedness intervened on July 9, 2013. The applicant did not present new evidence nor request an oral hearing. His application invoked two grounds: the first relates to which standard of review the RAD should use to determine the appeal and the second pertains to the reasonableness of the RPD’s determination with respect to his credibility and, more generally, to his claim.

[11] On September 18, 2013, the RAD confirmed the RPD’s decision.

[12] With respect to the standard of review to be applied to the RPD’s decision, invoking Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 [Newton], the RAD held that the RPD, as a first instance tribunal, is owed deference, and so its credibility findings must be assessed on a reasonableness standard. The rationale is that the appeal did not qualify for a hearing and only the RPD held a hearing directly questioning the applicant and reviewed the evidence before reaching its conclusion. The RAD added that it was not intended to act as a de novo appeal board, but rather to review the RPD decision for reasonableness, as understood by the Supreme Court of Canada’s pronouncements in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir].

[13] As for the RPD’s credibility determination, the RAD found that it was within the “range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47). While the claimant’s explanations for his behaviour for the events that occurred during his birthday party—notably that his boyfriend was “passionate” and that the invitees were viewed as “open-minded”—may be viewed as reasonable, the RAD concluded that the RPD’s analysis is reasonable “when looking at the claim as a whole.” Moreover, found the RAD, the RPD did not engage with “stereotypical considerations.”

[14] Finally, considering the great lengths the applicant went to come to Canada, he should have had a better idea of Canada’s refugee system. The applicant did not seek protection upon arrival but only after he was denied entry and accepted to make arrangements to be returned to the United Kingdom [UK]. In proceeding with this analysis, the RAD went over facts not mentioned in the RPD’s decision.
V. Issues and Standard of Review [15] This application raises the following issues:
1. What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law and credibility findings?
2. Is the RAD’s decision reasonable?

[16] The parties do not take a position as to the standard of review that should be used by this Court while reviewing the RAD’s interpretation of sections 110, 111, 162 and 171 of the Act [RAD Provisions], and its application to the facts of this case.

[17] In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], Justice Phelan acknowledged that there was no jurisprudence of the Federal Court of Appeal or of this Court on that specific issue. However, at paragraph 26, relying on Newton and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, he finds that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions. In doing so, he rejects the respondent’s view that the Supreme Court of Canada in Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 [Alberta Teachers] would have dictated otherwise. At paragraph 31, Justice Phelan states that the excerpts of Alberta Teachers relied upon by the respondent are not relevant as they are “predicated on the administrative tribunal using its expertise in interpreting its home statute”.

[18] With all due respect, I do not agree with Justice Phelan for two main reasons.

[19] First, in Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167, interpreting Alberta Teachers, the Supreme Court of Canada revisits the exceptions where the correctness standard will apply:
This principle [of deference] applies unless the interpretation of the home statute falls into one of the categories of questions to which the correctness standard continues to apply, i.e., “constitutional questions, questions of law that are of central importance to the legal system as a whole and that are outside the adjudicator’s expertise, . . . [q]uestions regarding the jurisdictional lines between two or more competing specialized tribunals [and] true questions of jurisdiction or vires” (Canada (Canadian Human Rights Commission) v. Canada (Attorney General), 2011 SCC 53, [2011] 3 S.C.R. 471, at para. 18, per LeBel and Cromwell JJ.) . . . [Emphasis added].

[20] In other words, in order for this Court to apply a correctness standard to an administrative tribunal’s interpretation of its own statute, each criterion must be met: i) the question of law has to be of central importance to the legal system as a whole; and ii) the question of law has to fall outside the adjudicator’s expertise. Even if I agreed with Justice Phelan that “the determination of the RAD’s standard of intervention for an appeal of the RPD decision is outside its expertise and experience”, the first part of the test still must be met in order for the correctness standard to apply.

[21] Second, in Alberta Teachers, Justice Binnie elaborated that an issue of general legal importance is one “whose resolution has significance outside the operation of the statutory scheme under consideration.” Since Alberta Teachers, the Supreme Court of Canada has reiterated its strict limitations to the use of the exceptions to the reasonableness standard (see for example McLean v British Columbia (Securities Commission), 2013 SCC 67 [McLean]). More importantly, since Alberta Teachers, the Supreme Court of Canada has not yet found one situation which falls into this particular exception to the reasonableness standard.

[22] In Nor-Man Regional Health Authority Inc v Manitoba Association of Health Care Professionals, 2011 SCC 59 [Nor-Man], Justice Fish, for a unanimous Court, found that the Manitoba Court of Appeal erred in choosing correctness as an applicable standard to an arbitrator allegedly misconstruing the equitable remedy of estoppel. The Court of Appeal had seen this as a question of law of central importance to the legal system as a whole, and that it did not fall within the expertise of labour arbitrators. The Supreme Court found that arbitrators had a broad mandate (albeit, not boundless) where their expertise allowed them to issue arbitral awards by reasonably applying a common law or equitable principle.

[23] In Communications, Energy and Paperworkers Union of Canada, Local 30 v Irving Pulp & Paper Ltd, 2013 SCC 34, [2013] 2 SCR 458, the Supreme Court of Canada held that its findings in Nor-Man above were directly applicable to the case. The New Brunswick Court of Appeal, as a result of its finding that the dispute was of wider public concern, had felt otherwise; it had applied a correctness standard to the board’s analytical framework for determining the validity of an employer’s random alcohol testing policy. Continuing on the standard of review, the Supreme Court found that the dispute had “little legal consequence outside the sphere of labour law and that, not its potential real-world consequences, determines the applicable standard of review” (at para 66, per Justice Moldaver, dissenting on other issues).

[24] In McLean, the British Columbia Court of Appeal had found that the interpretation of a statutory limitation period provision by an administrative tribunal would attract a standard of correctness. In rejecting this standard of review, the Supreme Court of Canada held that the question was not one of law of central importance to the legal system as a whole because while as a conceptual matter, limitation periods are generally of central importance to the fair administration of justice, there was no reason why the particular limitation period at issue in the appeal was of particular significance. The Court found that the impugned provisions in the case merely implicated a question of statutory interpretation, though it featured complex legal doctrines.The Court reiterated at paragraph 27, that the “general question” exception was simply one that “[b]ecause of [its] impact on the administration of justice as a whole, . . . [required] uniform and consistent answers” (citing Dunsmuir, at para 60) and is said to “safeguard a basic consistency in the fundamental legal order of our country” (citing Canada (Canadian Human Rights Commission) v Canada (Attorney General) 2011 SCC 53 at para 22). In the case before it, the Court did not view the “uniformity” criterion mentioned above, as adequately engaged by the mere possibility that in the case before it, other provincial and territorial securities commissions could have arrived at different interpretations of their own statutory limitation periods.

[25] Finally, in Canadian National Railway Co v Canada (Attorney General), 2014 SCC 40, the Court found that the question raised did not fit into the exceptional category because it did not “have precedential value outside of issues arising under [the] statutory scheme”. The question involved confidential contracts as provided under the Canada Transportation Act, SC 1996, c 10 and the availability of a mechanism set up to deal with complaints, limited to shippers that met conditions stipulated in the provision at issue (paras 55 and 60).

[26] In my view and in light of the consistent and firm position taken by the Supreme Court of Canada, the interpretation of the RAD Provisions by the RAD does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard. The issue of interpretation does not have significance outside the operation of these specific provisions, the very same provisions that only dictate the role and duties of the RAD.

[27] Finally, the application of the RAD Provisions to the facts of this, or any given case, is a question of mixed fact and law and also attracts the reasonableness standard.


## 23381:3 · paragraphs 29-51

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a2e2aac9685340ef06cb0c2bd205d1dbe57c31c0610497a1eb2f931b6ca823d6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23381:3:subtheme:1 · paragraphs 29-30

- Raw key terms: `fact, intervention, mixed, standard, agree, analysis, appeal, applied`
- Display key terms: `fact, intervention, mixed, standard, agree, analysis, applied`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: fact, intervention, mixed, standard, agree, analysis, applied Application context: What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law or to its credibility findings? | [28] The parties do not agree which standard of intervention the RAD must apply in appeal of RPD’s decisions on questions of fact or mixed fact and law. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `5098618` offsets `247-254`; context: What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law or to its credibility findings?
- Evidence: `reasoning_application` cue `apply` at chunk `5098619` offsets `74-79`; context: [28] The parties do not agree which standard of intervention the RAD must apply in appeal of RPD’s decisions on questions of fact or mixed fact and law.

#### 23381:3:subtheme:2 · paragraphs 31-33

- Raw key terms: `tribunal, appeal, appellate, argues, claims, court, newton, skills`
- Display key terms: `appellate, argues, claims, newton, skills`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: appellate, argues, claims, newton, skills Position/evidence statements: [29] The applicant argues that the RAD should have used a correctness standard. | [31] The respondent argues that an appellate administrative tribunal should apply the reasonableness standard when reviewing questions of fact or mixed fact and law from the decision of a lower tribunal. Rule/authority context: Newton concerns the basic structure and interrelationship of the tribunals in Alberta that review the conduct of police officers when that conduct is called into question during disciplinary proceedings under the Police  Application context: Both possess specialized knowledge and skills with regard to adjudicating refugee claims, therefore, there is no need for the RAD to defer to the RPD. | [31] The respondent argues that an appellate administrative tribunal should apply the reasonableness standard when reviewing questions of fact or mixed fact and law from the decision of a lower tribunal. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098620` offsets `347-355`; context: Newton concerns the basic structure and interrelationship of the tribunals in Alberta that review the conduct of police officers when that conduct is called into question during disciplinary proceedings under the Police Act, RSA 2000, c P-17.
- Evidence: `party_position` cue `argues` at chunk `5098620` offsets `19-25`; context: [29] The applicant argues that the RAD should have used a correctness standard.
- Evidence: `governing_rule` cue `under` at chunk `5098620` offsets `388-393`; context: Newton concerns the basic structure and interrelationship of the tribunals in Alberta that review the conduct of police officers when that conduct is called into question during disciplinary proceedings under the Police Act, RSA 2000, c P-17.
- Evidence: `reasoning_application` cue `therefore` at chunk `5098621` offsets `163-172`; context: Both possess specialized knowledge and skills with regard to adjudicating refugee claims, therefore, there is no need for the RAD to defer to the RPD.
- Evidence: `party_position` cue `argues` at chunk `5098622` offsets `20-26`; context: [31] The respondent argues that an appellate administrative tribunal should apply the reasonableness standard when reviewing questions of fact or mixed fact and law from the decision of a lower tribunal.
- Evidence: `reasoning_application` cue `apply` at chunk `5098622` offsets `76-81`; context: [31] The respondent argues that an appellate administrative tribunal should apply the reasonableness standard when reviewing questions of fact or mixed fact and law from the decision of a lower tribunal.

#### 23381:3:subtheme:3 · paragraphs 34-46

- Raw key terms: `credibility, applicant, deference, finding, advantage, decision, erred, fact`
- Display key terms: `credibility, deference, finding, advantage, erred, fact`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, deference, finding, advantage, erred, fact Position/evidence statements: [40] The applicant argues that the RAD was unreasonable in its determination that the RPD reasonably assessed the claimant’s credibility on the basis of three different matters. | [44] The respondent argues that it is not the RAD’s role to reassess evidence on appeal and conduct a new evaluation of the applicant’s credibility, absent new evidence. Rule/authority context: In my view, this implies that the RAD should avoid using and relying on both the jurisprudence and the vocabulary as developed in the context of judicial review. Application context: [33] There is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD. Evidence spans paragraphs 34-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5098623` offsets `774-780`; context: In addition, in Alyafi v Canada (Minister of Immigration and Citizenship), 2014 FC 952, Justice Martineau who did not specifically need to take position on these issues, conducted an interesting review of this Court’s previous decisions.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5098624` offsets `231-244`; context: In my view, this implies that the RAD should avoid using and relying on both the jurisprudence and the vocabulary as developed in the context of judicial review.
- Evidence: `reasoning_application` cue `apply` at chunk `5098624` offsets `100-105`; context: [33] There is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD.
- Evidence: `party_position` cue `argues` at chunk `5098631` offsets `19-25`; context: [40] The applicant argues that the RAD was unreasonable in its determination that the RPD reasonably assessed the claimant’s credibility on the basis of three different matters.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098633` offsets `189-197`; context: [42] Secondly, the RAD erred in finding it reasonable that the RPD found it implausible that the appellant was unaware of the risks he faced in Ghana as a homosexual, given the documentary evidence.
- Evidence: `counterargument_limitation` cue `but` at chunk `5098633` offsets `426-429`; context: The applicant was aware that homosexuality was socially unacceptable in Ghana, but did not think it was serious until he was attacked.
- Evidence: `party_position` cue `argues` at chunk `5098635` offsets `20-26`; context: [44] The respondent argues that it is not the RAD’s role to reassess evidence on appeal and conduct a new evaluation of the applicant’s credibility, absent new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098635` offsets `69-77`; context: [44] The respondent argues that it is not the RAD’s role to reassess evidence on appeal and conduct a new evaluation of the applicant’s credibility, absent new evidence.

#### 23381:3:subtheme:4 · paragraphs 47-49

- Raw key terms: `evidence, applicant, case, even, need, presented, view, analysis`
- Display key terms: `case, even, need, presented, view, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: case, even, need, presented, view, analysis Evidence spans paragraphs 47-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5098636` offsets `53-60`; context: [45] Again, there is no need in this case to analyze whether the appeal before the RAD is a de novo hearing when new evidence is presented and a hearing is held, as suggested by the respondent’s argument.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098636` offsets `117-125`; context: [45] Again, there is no need in this case to analyze whether the appeal before the RAD is a de novo hearing when new evidence is presented and a hearing is held, as suggested by the respondent’s argument.
- Evidence: `counterargument_limitation` cue `However` at chunk `5098636` offsets `205-212`; context: However, the RAD is to review and reassess the evidence even if no new evidence is presented and no hearing is held.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098637` offsets `95-103`; context: In its assessment of the evidence presented before the RPD, the RAD gave proper deference to the RPD’s credibility findings, which were sufficient for the RAD to reasonably confirm the RPD’s overall conclusion that the applicant was neither a Convention refugee nor a person in need of protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098638` offsets `364-372`; context: This is a strong indication that the RAD had reviewed the evidence given by the applicant and reassessed the claim in light of its own finding that some explanations given by the applicant were reasonable.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5098638` offsets `204-216`; context: The RAD concluded that even if these explanations seemed reasonable, it was nevertheless of the view that the RPD’s analysis was reasonable when looking at the claim as a whole.

#### 23381:3:subtheme:5 · paragraphs 50-51

- Raw key terms: `applicant, assessment, fact, accused, allegedly, analysis, answering, appeal`
- Display key terms: `assessment, fact, accused, allegedly, analysis, answering`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: assessment, fact, accused, allegedly, analysis, answering Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5098639` offsets `88-93`; context: [48] The RAD reasonably found that the RPD’s credibility assessment was a determinative issue in the appeal and that there were enough negative inferences to be drawn from the applicant’s testimony to uphold the RPD decision.
- Evidence: `evidence_fact` cue `found that` at chunk `5098639` offsets `24-34`; context: [48] The RAD reasonably found that the RPD’s credibility assessment was a determinative issue in the appeal and that there were enough negative inferences to be drawn from the applicant’s testimony to uphold the RPD decision.
- Evidence: `issue` cue `question` at chunk `5098640` offsets `24-32`; context: [49] Finally, as to the question of the applicant’s subjective fear of returning to Ghana, the RAD did in fact make its own assessment of the evidence and provided a more detailed analysis than did the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098640` offsets `142-150`; context: [49] Finally, as to the question of the applicant’s subjective fear of returning to Ghana, the RAD did in fact make its own assessment of the evidence and provided a more detailed analysis than did the RPD.

#### Section text

VI. Analysis 1. What is the appropriate standard of intervention to be applied by the RAD to RPD determinations of fact or mixed fact and law or to its credibility findings?

[28] The parties do not agree which standard of intervention the RAD must apply in appeal of RPD’s decisions on questions of fact or mixed fact and law.

[29] The applicant argues that the RAD should have used a correctness standard. The RAD does not owe the RPD the same level of deference as the Alberta Court of Appeal found in Newton. Newton concerns the basic structure and interrelationship of the tribunals in Alberta that review the conduct of police officers when that conduct is called into question during disciplinary proceedings under the Police Act, RSA 2000, c P-17. The initial investigation and prosecution of police misconduct is performed within police forces, by senior police officers. Appeals are then available to the Law Enforcement Review Board, which is a civilian tribunal. The Court of Appeal held that the court of first instance (the Presiding Officer) had considerable expertise over the matter more so than did the appellate tribunal (Law Enforcement Review Board), which provides civilian oversight. As such, the Presiding Officer’s greater expertise led to a greater deference owed.

[30] Meanwhile, the RPD and RAD are both divisions of the same tribunal. Both possess specialized knowledge and skills with regard to adjudicating refugee claims, therefore, there is no need for the RAD to defer to the RPD.

[31] The respondent argues that an appellate administrative tribunal should apply the reasonableness standard when reviewing questions of fact or mixed fact and law from the decision of a lower tribunal. The respondent points us to pronouncements by the Federal Court of Appeal, in the context of employment insurance claims (Budhai v Canada (Attorney General), 2002 FCA 298 at paras 22-48; Canada (Attorney General) v White, 2011 FCA 190 at para 2; Karelia v Canada (Minister of Human Resources and Skills Development), 2012 FCA 140 at para 12). This approach has also been followed where administrative tribunals sit on appeal (Newton).

[32] This Court has recently issued several decisions concerning the role of the newly created RAD (see Iyamuremye v Canada (Minister of Citizenship and Immigration), 2014 FC 494; Garcia Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 [Garcia Alvarez]; Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711 [Eng]; Huruglica; Njeukam v Canada (Minister of Citizenship and Immigration), 2014 FC 859 [Njeukam]; Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 [Yetna] and Spasoja v Canada (Minister of Citizenship and Immigration), 2014 FC 913 [Spasoja] . In addition, in Alyafi v Canada (Minister of Immigration and Citizenship), 2014 FC 952, Justice Martineau who did not specifically need to take position on these issues, conducted an interesting review of this Court’s previous decisions.

[33] There is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD. In my view, this implies that the RAD should avoid using and relying on both the jurisprudence and the vocabulary as developed in the context of judicial review.

[34] With that said, there also appears to be a consensus that when no hearing is held before the RAD, the latter owes deference to the RPD’s credibility findings.

[35] The opinions rather diverge on: i) the level of deference that is owed or its exact definition; and ii) the scope of the questions of fact and questions of mixed fact and law for which deference is owed.

[36] Justices Phelan (Huruglica) and Locke (Njeukam and Yetna) relying on the language of RAD Provisions along with the broad remedial power conferred to the RAD, concluded that except when a witness’ credibility is critical or determinative, or where a particular advantage is enjoyed by the RPD, no deference is owed by the RAD to the RPD’s finding of law, fact and mixed fact and law (see e.g., Yetna at para 17). While Justice Phelan does not indicate the level of deference that would be owed to the RPD’s credibility finding, Justice Locke, citing Justice Phelan, refers to the RAD as having erred in concluding a reasonableness standard was applicable to the RPD decision.

[37] Justices Shore (Garcia Alvarez and Eng) and Roy (Spasoja) are rather of the view that the RAD owes deference to the RPD on all questions of fact and mixed fact and law, not just on credibility findings or on matters where the RPD enjoys a particular advantage in reaching such a conclusion. In addition, they are of the view that the RAD should only intervene where there is an “overriding and palpable” error.

[38] Although I am far from being convinced that there is a real and pragmatic difference between an “unreasonable” error and an “overriding and palpable” one, I am of the view that said distinction would have no impact in the case at bar.

[39] However, I agree with Justice Phelan’s finding that deference is only owed by the RAD to the RPD’s credibility findings and where the RPD enjoys a particular advantage in reaching its conclusion.
2. Is the RAD’s decision reasonable?

[40] The applicant argues that the RAD was unreasonable in its determination that the RPD reasonably assessed the claimant’s credibility on the basis of three different matters.

[41] Firstly, with regards to the events that occurred at his birthday party, the RAD failed to properly consider the applicant’s arguments before it with respect to plausibility of naïve or imprudent behaviour. While the applicant may not have acted prudently at all times during that night, this does not warrant a negative credibility finding. The applicant explained that he thought people might not notice the handholding and that it was late at night. He explained his boyfriend was feeling passionate, which led them to spontaneously make love during his house party. Furthermore, the applicant is a musician and an artist, meaning the individuals in his social circle hold more liberal views about homosexuality. Thus, the applicant was less worried about engaging in sexual intimacy in the privacy of his bedroom, during a party with open-minded guests.

[42] Secondly, the RAD erred in finding it reasonable that the RPD found it implausible that the appellant was unaware of the risks he faced in Ghana as a homosexual, given the documentary evidence. Moreover, the RAD erred in finding that the RPD did not rely on stereotypical considerations in determining that the applicant is not a homosexual. The applicant was aware that homosexuality was socially unacceptable in Ghana, but did not think it was serious until he was attacked. He may still be coming to terms with his identity and may have difficulty speaking freely about sexual orientation to an authority figure.

[43] Finally, the RAD erred with respect to the RPD’s determination of the applicant’s lack of subjective fear of persecution. The RAD should not have expected the applicant to know the asylum process in Canada.

[44] The respondent argues that it is not the RAD’s role to reassess evidence on appeal and conduct a new evaluation of the applicant’s credibility, absent new evidence. There was no de novo hearing and the RPD’s decision was to be reviewed on a standard of reasonableness. Furthermore, the reasons need not mention all evidence in microscopic detail. The RAD – as well as the RPD – rejected the applicant’s refugee claim considering the evidence as a whole.

[45] Again, there is no need in this case to analyze whether the appeal before the RAD is a de novo hearing when new evidence is presented and a hearing is held, as suggested by the respondent’s argument. However, the RAD is to review and reassess the evidence even if no new evidence is presented and no hearing is held. That is its role as an appellate tribunal.

[46] In the case at bar, I am of the view that the RAD did just that. In its assessment of the evidence presented before the RPD, the RAD gave proper deference to the RPD’s credibility findings, which were sufficient for the RAD to reasonably confirm the RPD’s overall conclusion that the applicant was neither a Convention refugee nor a person in need of protection.

[47] The RAD did consider the applicant’s explanations for his behaviour during his birthday party and later on the same night. The RAD concluded that even if these explanations seemed reasonable, it was nevertheless of the view that the RPD’s analysis was reasonable when looking at the claim as a whole. This is a strong indication that the RAD had reviewed the evidence given by the applicant and reassessed the claim in light of its own finding that some explanations given by the applicant were reasonable.

[48] The RAD reasonably found that the RPD’s credibility assessment was a determinative issue in the appeal and that there were enough negative inferences to be drawn from the applicant’s testimony to uphold the RPD decision. The RPD did note that the applicant was vague and halted when answering questions regarding his lifestyle. It was reasonable for the RAD to consider the applicant’s age and the fact that he had allegedly been in a long term homosexual relationship, when assessing whether or not the RPD was, as accused by the applicant, only relying on stereotypes.

[49] Finally, as to the question of the applicant’s subjective fear of returning to Ghana, the RAD did in fact make its own assessment of the evidence and provided a more detailed analysis than did the RPD.


## 23381:4 · paragraphs 52-56

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `86b1dc20867dcfc461016b8bb9b5e8b1f45d3ab91db50770b72e652e6fad5589`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23381:4:subtheme:1 · paragraphs 52-53

- Raw key terms: `application, addressed, already, applicant, appropriate, case, cases, certification`
- Display key terms: `addressed, already, appropriate, case, cases, certification`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: addressed, already, appropriate, case, cases, certification Application context: Conclusion [50] I find it reasonable that the RAD deferred to the RPD’s credibility findings. Operative outcome context: Therefore, the application for judicial review will be dismissed. Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5098640` offsets `355-363`; context: I also find that its overall reassessment of the evidence is reasonable.
- Evidence: `reasoning_application` cue `I find` at chunk `5098640` offsets `228-234`; context: Conclusion [50] I find it reasonable that the RAD deferred to the RPD’s credibility findings.
- Evidence: `disposition` cue `dismissed` at chunk `5098640` offsets `434-443`; context: Therefore, the application for judicial review will be dismissed.
- Evidence: `issue` cue `question` at chunk `5098641` offsets `141-149`; context: [51] In a correspondence addressed to the Court after the hearing, the respondent expressed the view that it is not appropriate to certify a question in this case, in light of the number of cases challenged before the Court, dealing with RAD decisions and the numerous questions of general importance already certified.
- Evidence: `counterargument_limitation` cue `However` at chunk `5098641` offsets `320-327`; context: However, as I am dismissing the applicant’s application, it is the applicant that would loose a right if no question is certified and the applicant has not waived his right to propose a question for certification.

#### 23381:4:subtheme:2 · paragraphs 54-56

- Raw key terms: `appeal, case, certified, determinative, hearing, immigration, record, agree`
- Display key terms: `case, certified, determinative, hearing, agree`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: case, certified, determinative, hearing, agree Rule/authority context: [53] I believe the following questions are determinative of this case and would be determinative of an appeal: (a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s inte Application context: I do not agree with the applicant because such a general question is not determinative of this case, nor would it be determinative of an appeal. | [53] I believe the following questions are determinative of this case and would be determinative of an appeal: (a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s inte Operative outcome context: The application for judicial review is dismissed; 2. Evidence spans paragraphs 54-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5098642` offsets `66-74`; context: [52] At the hearing, counsel for the applicant suggested that the question “what is the appellate role of the RAD?
- Evidence: `reasoning_application` cue `because` at chunk `5098642` offsets `177-184`; context: I do not agree with the applicant because such a general question is not determinative of this case, nor would it be determinative of an appeal.
- Evidence: `evidence_fact` cue `record` at chunk `5098643` offsets `607-613`; context: (b) Within the Refugee Appeal Division’s statutory framework where the appeal proceeds on the basis of the Refugee Protection Division record of the proceedings, what is the level of deference owed by the Refugee Appeal Division to the Refugee Protection Division findings of fact and of mixed fact and law, more specifically to its credibility findings?
- Evidence: `governing_rule` cue `standard of review` at chunk `5098643` offsets `120-138`; context: [53] I believe the following questions are determinative of this case and would be determinative of an appeal:
(a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of sections 110, 111, 162 and 171 of the Immigration and Refugee Protection Act, SC 2001, c 27, and more specifically when reviewing its determination of the level of deference owed to the Refugee Protection Division’s credibility findings?
- Evidence: `reasoning_application` cue `applied` at chunk `5098643` offsets `149-156`; context: [53] I believe the following questions are determinative of this case and would be determinative of an appeal:
(a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of sections 110, 111, 162 and 171 of the Immigration and Refugee Protection Act, SC 2001, c 27, and more specifically when reviewing its determination of the level of deference owed to the Refugee Protection Division’s credibility findings?
- Evidence: `disposition` cue `dismissed` at chunk `5098643` offsets `909-918`; context: The application for judicial review is dismissed;
2.

#### Section text

VII. Conclusion [50] I find it reasonable that the RAD deferred to the RPD’s credibility findings. I also find that its overall reassessment of the evidence is reasonable. Therefore, the application for judicial review will be dismissed.
* * *

[51] In a correspondence addressed to the Court after the hearing, the respondent expressed the view that it is not appropriate to certify a question in this case, in light of the number of cases challenged before the Court, dealing with RAD decisions and the numerous questions of general importance already certified. However, as I am dismissing the applicant’s application, it is the applicant that would loose a right if no question is certified and the applicant has not waived his right to propose a question for certification.

[52] At the hearing, counsel for the applicant suggested that the question “what is the appellate role of the RAD?” be certified in this case. I do not agree with the applicant because such a general question is not determinative of this case, nor would it be determinative of an appeal.

[53] I believe the following questions are determinative of this case and would be determinative of an appeal:
(a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of sections 110, 111, 162 and 171 of the Immigration and Refugee Protection Act, SC 2001, c 27, and more specifically when reviewing its determination of the level of deference owed to the Refugee Protection Division’s credibility findings?
(b) Within the Refugee Appeal Division’s statutory framework where the appeal proceeds on the basis of the Refugee Protection Division record of the proceedings, what is the level of deference owed by the Refugee Appeal Division to the Refugee Protection Division findings of fact and of mixed fact and law, more specifically to its credibility findings?
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application for judicial review is dismissed;
2. The following questions are certified:
(a) What standard of review should be applied by this Court when reviewing the Refugee Appeal Division’s interpretation of sections 110, 111, 162 and 171 of the Immigration and Refugee Protection Act, SC 2001, c 27, and more specifically when reviewing its determination of the level of deference owed to the Refugee Protection Division’s credibility findings?
(b) Within the Refugee Appeal Division’s statutory framework where the appeal proceeds on the basis of the Refugee Protection Division record of the proceedings, what is the level of deference owed by the Refugee Appeal Division to the Refugee Protection Division findings of fact and of mixed fact and law, more specifically to its credibility findings?
"Jocelyne Gagné"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6640-13
STYLE OF CAUSE:
EDWIN YAW SARFO AKUFFO v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, Quebec
DATE OF HEARING:
July 3, 2014


## 23381:5 · paragraphs 57-57

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `399f62f22d86b947fb215b7b81214429480b6f9a98c7b1a9ce0881e3ee73d714`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23381:5:subtheme:1 · paragraphs 57-57

- Raw key terms: `appearances, applicant, attorney, barrister, canada, dated, deputy, gagn`
- Display key terms: `barrister, dated, deputy, gagn`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, dated, deputy, gagn No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 57-57. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GAGNÉ J.
DATED:
november 12, 2014
APPEARANCES:
Me Jessica Ann Lipes
For The Applicant
Me Suzanne Trudel
For The Respondent
SOLICITORS OF RECORD:
Me Jessica Ann Lipes
Barrister and Solicitor
Montréal, Quebec
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
For The Respondent
