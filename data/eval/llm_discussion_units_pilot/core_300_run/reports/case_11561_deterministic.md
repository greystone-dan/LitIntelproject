# Discussion Units: case 11561

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **4**
- Paragraph source hashes: **30**
- Sub-themes: **12**

## 11561:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `50a6ce5ce3ddbbde43a1e2043ce9eb985875d763e582ad80627d5d07b20b299c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11561:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `adrian, applicants, decision, dusan, ferenc, horvath, immigration, leticia`
- Display key terms: `adrian, dusan, ferenc, horvath, leticia`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: adrian, dusan, ferenc, horvath, leticia Rule/authority context: [1] The Applicants, citizens of Hungary of Roma ethnicity, seek judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA or the Act) of a decision of the Refugee Appeal Di Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4582047` offsets `80-85`; context: [1] The Applicants, citizens of Hungary of Roma ethnicity, seek judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA or the Act) of a decision of the Refugee Appeal Division (RAD) of the Immigration and Refugee Protection Board dated July 13, 2017.

#### 11561:1:subtheme:2 · paragraphs 2-2

- Raw key terms: `applicants, assessment, background, concluded, credibility, decision, different, erred`
- Display key terms: `assessment, background, concluded, credibility, different, erred`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: assessment, background, concluded, credibility, different, erred Evidence spans paragraphs 2-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4582048` offsets `8-14`; context: [2] The issues raised by the Applicants focus on whether the RAD erred in the assessment of their credibility and in weighing the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582048` offsets `130-138`; context: [2] The issues raised by the Applicants focus on whether the RAD erred in the assessment of their credibility and in weighing the evidence.

#### 11561:1:subtheme:3 · paragraphs 3-5

- Raw key terms: `applicants, friend, accept, accepted, another, area, assaults, assistance`
- Display key terms: `friend, accept, accepted, another, area, assaults, assistance`
- Argument roles: `counterargument_limitation, evidence_fact, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position Display terms: friend, accept, accepted, another, area, assaults, assistance Position/evidence statements: They claim that they were forcibly evicted from the home and had to accept shelter in a wood shed on the property of a friend in another municipality. Evidence spans paragraphs 3-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `4582049` offsets `316-321`; context: They claim that they were forcibly evicted from the home and had to accept shelter in a wood shed on the property of a friend in another municipality.
- Evidence: `counterargument_limitation` cue `but` at chunk `4582049` offsets `288-291`; context: They retained the pro bono services of a Budapest lawyer to help them fight the decision but were unsuccessful.
- Evidence: `evidence_fact` cue `found that` at chunk `4582050` offsets `121-131`; context: But on a balance of probabilities, the RPD found that the claimants were not credible witnesses and that they would not be subject to persecution or face a danger to their lives if they were to return to Hungary.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582051` offsets `74-82`; context: [5] Of greatest concern to the RPD was the lack of supporting documentary evidence regarding their eviction and claims of assaults requiring hospital care.

#### 11561:1:subtheme:4 · paragraphs 6-12

- Raw key terms: `horvath, applicants, assault, contradictory, evidence, found, provided, suffers`
- Display key terms: `horvath, assault, contradictory, provided, suffers`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: horvath, assault, contradictory, provided, suffers Position/evidence statements: The Applicants submitted new evidence in support of their appeal pursuant to s 110(4) of the IRPA. Rule/authority context: The Applicants did not request a hearing and the RAD did not hold a hearing pursuant to s 110(6) of the IRPA. | Standard of Review Application context: [11] The RAD did not accept that the Applicants had been evicted from their home because of their Roma ethnicity. Evidence spans paragraphs 6-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4582052` offsets `157-164`; context: The RPD found that he and his wife provided contradictory statements regarding whether this was caused by a racially motivated assault or an accident.
- Evidence: `evidence_fact` cue `found that` at chunk `4582052` offsets `86-96`; context: The RPD found that he and his wife provided contradictory statements regarding whether this was caused by a racially motivated assault or an accident.
- Evidence: `evidence_fact` cue `found that` at chunk `4582053` offsets `143-153`; context: [7] The RPD accepted that Roma are discriminated against in Hungary and that some are subjected to pernicious, racially-motivated attacks, but found that this does not establish that all individuals of Roma ethnicity face a serious possibility of treatment that rises to the level of persecution.
- Evidence: `party_position` cue `submitted` at chunk `4582054` offsets `173-182`; context: The Applicants submitted new evidence in support of their appeal pursuant to s 110(4) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582054` offsets `187-195`; context: The Applicants submitted new evidence in support of their appeal pursuant to s 110(4) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4582054` offsets `124-135`; context: The Applicants did not request a hearing and the RAD did not hold a hearing pursuant to s 110(6) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582055` offsets `302-310`; context: Given the contradictory evidence provided to the RPD, the RAD was not satisfied that it was racially motivated.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582057` offsets `174-182`; context: It rejected the explanation that the supporting documentary evidence of the eviction had been thrown out by the friend in Hungary.
- Evidence: `reasoning_application` cue `because` at chunk `4582057` offsets `81-88`; context: [11] The RAD did not accept that the Applicants had been evicted from their home because of their Roma ethnicity.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4582058` offsets `329-347`; context: Standard of Review

#### 11561:1:subtheme:5 · paragraphs 13-14

- Raw key terms: `decision, issue, acceptable, accord, agree, attention, brunswick, canada`
- Display key terms: `acceptable, accord, agree, attention, brunswick`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acceptable, accord, agree, attention, brunswick Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `4582059` offsets `502-507`; context: Issue
- Evidence: `issue` cue `issue` at chunk `4582060` offsets `14-19`; context: [14] The sole issue for consideration is whether the decision is reasonable.

#### Section text

Horvath v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2018-02-08
Neutral citation
2018 CF 147
File numbers
IMM-3425-17
Decision Content
Date: 20180208
Docket: IMM-3425-17
Citation: 2018 FC 147
Toronto, Ontario, February 8, 2018
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
DUSAN FERENC HORVATH
TUNDE VOLOPICH
LETICIA HORVATH
ADRIAN HORVATH
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction

[1] The Applicants, citizens of Hungary of Roma ethnicity, seek judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA or the Act) of a decision of the Refugee Appeal Division (RAD) of the Immigration and Refugee Protection Board dated July 13, 2017. The RAD confirmed the decision of the Refugee Protection Division (RPD) that the Applicants, Mr. Dusan Ferenc Horvath, Ms. Tunde Volopich, and their minor children, Leticia Horvath and Adrian Horvath, are neither Convention refugees nor persons in need of protection pursuant to s 96 and 97 of the IRPA.

[2] The issues raised by the Applicants focus on whether the RAD erred in the assessment of their credibility and in weighing the evidence. The question overall is whether the decision was reasonable. For the reasons that follow, I have concluded that it was not and that the matter should be remitted for redetermination by a different RAD member.
II. Background

[3] The Applicants were residents of Miskolc. The municipality was engaged in the clearance of sub-standard housing in the area in which they lived. They were told that their home would be included. They retained the pro bono services of a Budapest lawyer to help them fight the decision but were unsuccessful. They claim that they were forcibly evicted from the home and had to accept shelter in a wood shed on the property of a friend in another municipality. With the assistance of family members, they made their way to Canada and sought refugee protection.

[4] The RPD accepted their identity as Hungarian nationals of Roma ethnicity. But on a balance of probabilities, the RPD found that the claimants were not credible witnesses and that they would not be subject to persecution or face a danger to their lives if they were to return to Hungary.

[5] Of greatest concern to the RPD was the lack of supporting documentary evidence regarding their eviction and claims of assaults requiring hospital care. The Applicants testified that they had entrusted their records to a friend who had inadvertently disposed of them as garbage.

[6] Mr. Horvath suffers from advanced glaucoma and says that he is now blind. The RPD found that he and his wife provided contradictory statements regarding whether this was caused by a racially motivated assault or an accident.

[7] The RPD accepted that Roma are discriminated against in Hungary and that some are subjected to pernicious, racially-motivated attacks, but found that this does not establish that all individuals of Roma ethnicity face a serious possibility of treatment that rises to the level of persecution. Even if the Applicants’ allegations were credible, the RPD concluded, their experience would not amount to discrimination amounting to persecution. This included the discrimination faced by the minor Applicants in school, as described by the oldest child in his testimony.

[8] The RPD’s decision was appealed to the RAD. The Applicants did not request a hearing and the RAD did not hold a hearing pursuant to s 110(6) of the IRPA. The Applicants submitted new evidence in support of their appeal pursuant to s 110(4) of the IRPA. All of the new evidence was accepted by the RAD. It confirmed that the Applicants did reside at the address they had claimed; a fact questioned by the RPD.

[9] Chart notes from St. Joseph’s Health Centre in Toronto appear to confirm that Mr. Horvath suffers from advanced “end stage” glaucoma but do not indicate the cause, a matter of some concern to the RAD. Mr. Horvath alleged that he was blind as a result of a physical assault. Given the contradictory evidence provided to the RPD, the RAD was not satisfied that it was racially motivated.

[10] An updated psychological report indicating that Mr. Horvath suffers from Post-traumatic Stress Disorder was also admitted but given little weight as it could not be used to establish the credibility of the refugee claim: B296 v Canada (MCI), 2015 FC 761 at paras 54-57, citing Kaur v Canada (MCI), 2012 FC 1379, [2014] 2 FCR 3.

[11] The RAD did not accept that the Applicants had been evicted from their home because of their Roma ethnicity. It rejected the explanation that the supporting documentary evidence of the eviction had been thrown out by the friend in Hungary. The RAD found that the Applicants did not make reasonable efforts to obtain police and medical reports, and rejected Mr. Horvath’s explanation that he didn’t know he could get such reports. He had also provided contradictory evidence to the RPD regarding an assault that allegedly occurred on May 1, 2015. His explanation was that he had confused this incident with another.

[12] The RAD had a major concern with the failure of the Applicants to mention any of the alleged multiple incidents of physical assault at the Port of Entry interview. Rather than discussing those incidents, described later to the RPD, Mr. Horvath’s major concern was said to be the fear of sending his children to school.
III. Standard of Review

[13] The parties agree that the standard for the Court’s review of the RAD decision is reasonableness. I agree. The Court must accord the decision maker deference and pay respectful attention to the reasons offered in support of a decision: Dunsmuir v New Brunswick, 2008 SCC 9 at para 47 [Dunsmuir]. The RAD’s findings of fact and determinations of credibility must fall within the range of possible, acceptable outcomes: Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at paras 44, 59.
IV. Issue

[14] The sole issue for consideration is whether the decision is reasonable.
V. Relevant Legislation

## 11561:2 · paragraphs 15-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `059f58fa50183a8c934838af927ab8da3272f6c6851fdb3507f9b6bfb73451db`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11561:2:subtheme:1 · paragraphs 15-16

- Raw key terms: `appeal, decision, hearing, proceed, without, written, accept, accepted`
- Display key terms: `hearing, proceed, without, written, accept, accepted`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: hearing, proceed, without, written, accept, accepted Position/evidence statements: In their written representations on this application and at the hearing, they have submitted that the RAD’s decision to proceed without a hearing was unreasonable. Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4582061` offsets `2295-2300`; context: […]
[…]
Hearing
Audience
110(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
- Evidence: `evidence_fact` cue `record` at chunk `4582061` offsets `300-306`; context: 1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
- Evidence: `party_position` cue `submitted` at chunk `4582062` offsets `251-260`; context: In their written representations on this application and at the hearing, they have submitted that the RAD’s decision to proceed without a hearing was unreasonable.

#### 11561:2:subtheme:2 · paragraphs 17-18

- Raw key terms: `hearing, irpa, refugee, accepted, admitted, allow, allowing, appeal`
- Display key terms: `hearing, irpa, refugee, accepted, admitted, allow, allowing`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: hearing, irpa, refugee, accepted, admitted, allow, allowing Rule/authority context: [17] If new evidence is admitted pursuant to IRPA s 110(4), the RAD “may hold a hearing” if the evidence (a) raises a serious issue with respect to credibility, (b) is central to the decision with respect to the refugee  Application context: The onus rests with the RAD to consider and apply the statutory criteria reasonably: Zhou v Canada (Citizenship and Immigration), 2015 FC 911 at para 11; see also Strachn v Canada (Citizenship and Immigration), 2012 FC 9 Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4582063` offsets `126-131`; context: [17] If new evidence is admitted pursuant to IRPA s 110(4), the RAD “may hold a hearing” if the evidence (a) raises a serious issue with respect to credibility, (b) is central to the decision with respect to the refugee claims, and (c) if accepted, would justify allowing or rejecting the refugee claim, pursuant to s 110(6) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582063` offsets `12-20`; context: [17] If new evidence is admitted pursuant to IRPA s 110(4), the RAD “may hold a hearing” if the evidence (a) raises a serious issue with respect to credibility, (b) is central to the decision with respect to the refugee claims, and (c) if accepted, would justify allowing or rejecting the refugee claim, pursuant to s 110(6) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4582063` offsets `33-44`; context: [17] If new evidence is admitted pursuant to IRPA s 110(4), the RAD “may hold a hearing” if the evidence (a) raises a serious issue with respect to credibility, (b) is central to the decision with respect to the refugee claims, and (c) if accepted, would justify allowing or rejecting the refugee claim, pursuant to s 110(6) of the IRPA.
- Evidence: `reasoning_application` cue `apply` at chunk `4582064` offsets `399-404`; context: The onus rests with the RAD to consider and apply the statutory criteria reasonably: Zhou v Canada (Citizenship and Immigration), 2015 FC 911 at para 11; see also Strachn v Canada (Citizenship and Immigration), 2012 FC 984 at para 34: Boyce v Canada (Citizenship and Immigration), 2016 FC 922 at paras 47-48.
- Evidence: `counterargument_limitation` cue `However` at chunk `4582064` offsets `198-205`; context: However, neither IRPA nor the RAD Rules impose a burden on appellants either to request, or to satisfy the RAD that the circumstances merit an oral hearing.

#### 11561:2:subtheme:3 · paragraphs 19-22

- Raw key terms: `applicants, accepted, canada, credibility, entry, evidence, given, hearing`
- Display key terms: `accepted, credibility, entry, given, hearing`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: accepted, credibility, entry, given, hearing Rule/authority context: [22] This Court has previously cautioned against the overreliance on Port of Entry notes given the circumstances under which they are made: Wu v Canada (Citizenship and Immigration), 2010 FC 1102 at para 16; Seenivasan v Evidence spans paragraphs 19-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4582065` offsets `35-41`; context: [19] Given the serious credibility issues which arose from the RPD hearing and considering the new evidence accepted by the RAD, the RAD should have convened an oral hearing before dismissing the Applicants’ appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582065` offsets `99-107`; context: [19] Given the serious credibility issues which arose from the RPD hearing and considering the new evidence accepted by the RAD, the RAD should have convened an oral hearing before dismissing the Applicants’ appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582066` offsets `44-52`; context: [20] In this instance, the RAD accepted new evidence that was directly contradictory to the RPD’s findings regarding the Applicants’ residence and which went to the core of their credibility.
- Evidence: `evidence_fact` cue `testimony` at chunk `4582067` offsets `95-104`; context: [21] Overall, the Applicants’ account was consistent between the Port of Entry notes and their testimony at the RPD hearing but for minor differences and the additional details provided later.
- Evidence: `governing_rule` cue `under` at chunk `4582068` offsets `113-118`; context: [22] This Court has previously cautioned against the overreliance on Port of Entry notes given the circumstances under which they are made: Wu v Canada (Citizenship and Immigration), 2010 FC 1102 at para 16; Seenivasan v Canada (Citizenship and Immigration), 2015 FC 1410 at para 21.

#### 11561:2:subtheme:4 · paragraphs 23-24

- Raw key terms: `applicants, canada, corroborating, corroborative, evidence, para, accept, accord`
- Display key terms: `corroborating, corroborative, para, accept, accord`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: corroborating, corroborative, para, accept, accord Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4582069` offsets `609-614`; context: ” This was a veiled way of saying that the RAD did not believe the Applicants and would not believe them on this key issue without corroborative documentary evidence: see Liban v Canada (MCI), 2008 FC 1252 at para 14.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582069` offsets `213-221`; context: [23] The RAD did accept that the municipality of Miskolc was carrying out a demolition programme in the area of the city where the Applicants resided but rejected their explanation for why they had no documentary evidence of their eviction.
- Evidence: `evidence_fact` cue `evidence` at chunk `4582070` offsets `19-27`; context: [24] Corroborative evidence was only required if the RAD had (1) reason to doubt the Applicants’ claim and (2) the corroborating evidence could reasonably be expected to be available: Ndjavera v Canada (Citizenship and Immigration), 2013 FC 452 at para 6.

#### 11561:2:subtheme:5 · paragraphs 25-26

- Raw key terms: `serious, above, acceptable, address, another, applicants, application, central`
- Display key terms: `serious, above, acceptable, address, another, central`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: serious, above, acceptable, address, another, central Position/evidence statements: [25] Credibility was at the core of the RPD’s findings regarding the persecution claimed by the Applicants. Operative outcome context: For that reason, this application will be granted and the matter remitted for reconsideration by another RAD member. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4582071` offsets `180-186`; context: The RAD erred in failing to hold an oral hearing to address the serious issues of credibility that were central to the RPD decision.
- Evidence: `party_position` cue `claimed` at chunk `4582071` offsets `81-88`; context: [25] Credibility was at the core of the RPD’s findings regarding the persecution claimed by the Applicants.
- Evidence: `evidence_fact` cue `record` at chunk `4582071` offsets `285-291`; context: The RAD’s findings are not supported by the record and its conclusion was not “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir, above at para 47.
- Evidence: `disposition` cue `granted` at chunk `4582071` offsets `493-500`; context: For that reason, this application will be granted and the matter remitted for reconsideration by another RAD member.
- Evidence: `issue` cue `question` at chunk `4582072` offsets `38-46`; context: [26] Neither party proposed a serious question of general importance and none will be certified.

#### Section text

[15] The relevant provisions of the IRPA read as follows:
Appeal to Refugee Appeal Division
Appel devant la Section d’appel des réfugiés
[…]
[…]
Procedure
Fonctionnement
110(3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
110(3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
[…]
[…]
Evidence that may be presented
Éléments de preuve admissibles
110(4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
110(4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
[…]
[…]
Hearing
Audience
110(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
VI. Analysis
A. Was the decision reasonable?

[16] In their appeal statement, the Applicants did not ask for a hearing before the RAD “except if the RAD is unable to substitute its decision for that of [the RPD]”. In their written representations on this application and at the hearing, they have submitted that the RAD’s decision to proceed without a hearing was unreasonable.

[17] If new evidence is admitted pursuant to IRPA s 110(4), the RAD “may hold a hearing” if the evidence (a) raises a serious issue with respect to credibility, (b) is central to the decision with respect to the refugee claims, and (c) if accepted, would justify allowing or rejecting the refugee claim, pursuant to s 110(6) of the IRPA.

[18] The RAD rules allow an appellant to request a hearing. They must do so in writing with a supporting memorandum: Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules], s 3(3)(d)(ii), 3(3)(g). However, neither IRPA nor the RAD Rules impose a burden on appellants either to request, or to satisfy the RAD that the circumstances merit an oral hearing. The onus rests with the RAD to consider and apply the statutory criteria reasonably: Zhou v Canada (Citizenship and Immigration), 2015 FC 911 at para 11; see also Strachn v Canada (Citizenship and Immigration), 2012 FC 984 at para 34: Boyce v Canada (Citizenship and Immigration), 2016 FC 922 at paras 47-48.

[19] Given the serious credibility issues which arose from the RPD hearing and considering the new evidence accepted by the RAD, the RAD should have convened an oral hearing before dismissing the Applicants’ appeal.

[20] In this instance, the RAD accepted new evidence that was directly contradictory to the RPD’s findings regarding the Applicants’ residence and which went to the core of their credibility. The RPD and RAD also had questions about Mr. Horvath’s blindness that were found to undermine his credibility on a material point. The RAD found contradictions in his narrative and his testimony regarding the incident in 2006 which he said was the cause, including with respect to his contacts with the police. As a result, the RAD found that he had failed to establish that the blindness was due to a physical assault motivated by his Roma identity.

[21] Overall, the Applicants’ account was consistent between the Port of Entry notes and their testimony at the RPD hearing but for minor differences and the additional details provided later. It was unreasonable to expect that the Applicants would provide a complete account of their experiences at the Port of Entry. They had just arrived in Canada after completing a long journey with their children. It is apparent that the officer completing the notes did not want to record many details and made mistakes while completing the record. Some details provided and entered in the notes were undoubtedly the result of confusion by either the Applicants or the officer. The adult Applicants’ concern for their children’s safety at school was not inconsistent with the tale they later told.

[22] This Court has previously cautioned against the overreliance on Port of Entry notes given the circumstances under which they are made: Wu v Canada (Citizenship and Immigration), 2010 FC 1102 at para 16; Seenivasan v Canada (Citizenship and Immigration), 2015 FC 1410 at para 21.

[23] The RAD did accept that the municipality of Miskolc was carrying out a demolition programme in the area of the city where the Applicants resided but rejected their explanation for why they had no documentary evidence of their eviction. In doing so, the RAD effectively refused to accord weight to the Applicants’ story without corroborating evidence. This was described as an “insufficient explanation for the lack of documentary evidence in support of their allegation of being evicted.” This was a veiled way of saying that the RAD did not believe the Applicants and would not believe them on this key issue without corroborative documentary evidence: see Liban v Canada (MCI), 2008 FC 1252 at para 14.

[24] Corroborative evidence was only required if the RAD had (1) reason to doubt the Applicants’ claim and (2) the corroborating evidence could reasonably be expected to be available: Ndjavera v Canada (Citizenship and Immigration), 2013 FC 452 at para 6. The RAD failed to intelligibly and transparently explain why it disbelieved the Applicants and why they had to provide corroborating documents.

[25] Credibility was at the core of the RPD’s findings regarding the persecution claimed by the Applicants. The RAD erred in failing to hold an oral hearing to address the serious issues of credibility that were central to the RPD decision. The RAD’s findings are not supported by the record and its conclusion was not “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”: Dunsmuir, above at para 47. For that reason, this application will be granted and the matter remitted for reconsideration by another RAD member.

[26] Neither party proposed a serious question of general importance and none will be certified.


## 11561:3 · paragraphs 27-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d1d7f18b1fb9e3aa466610b6a3726eecee14004dd764032f108051a7270deeb8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11561:3:subtheme:1 · paragraphs 27-28

- Raw key terms: `imm-3425-17, appeal, application, cause, certified, citizenship, court, date`
- Display key terms: `imm-3425-17, certified, date`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: imm-3425-17, certified, date Operative outcome context: JUDGMENT in IMM-3425-17 THIS COURT’S JUDGMENT is that: The application is granted and the matter is remitted to a different member of the Refugee Appeal Division for reconsideration; and No questions are certified. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `4582072` offsets `171-178`; context: JUDGMENT in IMM-3425-17
THIS COURT’S JUDGMENT is that:
The application is granted and the matter is remitted to a different member of the Refugee Appeal Division for reconsideration; and
No questions are certified.

#### Section text

JUDGMENT in IMM-3425-17
THIS COURT’S JUDGMENT is that:
The application is granted and the matter is remitted to a different member of the Refugee Appeal Division for reconsideration; and
No questions are certified.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3425-17
STYLE OF CAUSE:
DUSAN FERENC HORVATH ET AL V THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
toronto, ontario
DATE OF HEARING:
FEBRUARY 5, 2018


## 11561:4 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `625b38a9a348f441cabe0c4bac8f29be95322dc6c3d2979cbb6b4ef935677315`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11561:4:subtheme:1 · paragraphs 29-29

- Raw key terms: `appearances, applicants, attorney, barristers, canada, dated, february, general`
- Display key terms: `barristers, dated, february`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, dated, february No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
mosley, J.
DATED:
FEBRUARY 8, 2018
APPEARANCES:
Peter G. Ivanyi
For The APPLICANTS
Nadine Silverman
For The RESPONDENT
SOLICITORS OF RECORD:
Rochon Genova LLP
Barristers and Solicitors
Toronto, Ontario
For The APPLICANTS
Attorney General of Canada
Toronto, Ontario
For The RESPONDENT
